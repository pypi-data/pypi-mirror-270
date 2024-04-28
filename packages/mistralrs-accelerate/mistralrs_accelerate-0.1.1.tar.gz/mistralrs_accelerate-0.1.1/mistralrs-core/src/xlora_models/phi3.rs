#![allow(clippy::cast_possible_truncation, clippy::cast_precision_loss)]

// This implementation is based on:
// https://huggingface.co/microsoft/Phi-3-mini-4k-instruct/blob/main/modeling_phi3.py
use candle_core::{quantized::QMatMul, DType, Device, IndexOp, Module, Result, Tensor, D};
use candle_nn::VarBuilder;
use mistralrs_lora::{layer::QLinear, linear_no_bias, LinearLayerLike, LoraConfig, Ordering};
use std::sync::Arc;
use tqdm::Iter;
use tracing::info;

use crate::{
    device_map::DeviceMapper,
    layers::{PhiRotaryEmbedding, RmsNorm},
    models::phi3::Config,
    pipeline::{extract_logits, NormalModel},
    DeviceMapMetadata,
};

use crate::models::{flash_attn, repeat_kv, Cache};

use super::{classifier::XLoraClassifier, NonGranularState, ScalingsMaker, XLoraConfig};

#[derive(Debug, Clone)]
struct Attention {
    qkv_proj: Arc<dyn LinearLayerLike + Send + Sync>,
    o_proj: Arc<dyn LinearLayerLike + Send + Sync>,
    num_heads: usize,
    num_kv_heads: usize,
    num_kv_groups: usize,
    head_dim: usize,
    rotary_emb: Arc<PhiRotaryEmbedding>,
    use_flash_attn: bool,
}

impl Attention {
    fn new(
        rotary_emb: Arc<PhiRotaryEmbedding>,
        cfg: &Config,
        vb: VarBuilder,
        lora_config: &[(String, LoraConfig)],
        count: &mut usize,
        ord: &Ordering,
    ) -> Result<Self> {
        let num_heads = cfg.num_attention_heads;
        let num_kv_heads = cfg.num_key_value_heads;
        let head_dim = cfg.head_dim();
        let op_size = num_heads * head_dim + 2 * num_kv_heads * head_dim;
        let qkv_proj = linear_no_bias(
            cfg.hidden_size,
            op_size,
            vb.pp("qkv_proj"),
            lora_config,
            count,
            ord,
        )?;
        let o_proj = linear_no_bias(
            num_heads * head_dim,
            cfg.hidden_size,
            vb.pp("o_proj"),
            lora_config,
            count,
            ord,
        )?;
        Ok(Self {
            qkv_proj,
            o_proj,
            rotary_emb,
            num_heads,
            num_kv_heads,
            num_kv_groups: num_heads / num_kv_heads,
            head_dim,
            use_flash_attn: cfg.use_flash_attn,
        })
    }

    #[allow(clippy::too_many_arguments)]
    fn forward(
        &mut self,
        xs: &Tensor,
        attention_mask: Option<&Tensor>,
        seqlen_offsets: &[usize],
        _start_offsets_kernel: Tensor,
        kv_cache: &mut Option<(Tensor, Tensor)>,
        scalings: Option<Tensor>,
        global_scaling_weight: f64,
        is_scaling_pass: Option<f64>,
    ) -> Result<Tensor> {
        let (b_sz, q_len, _) = xs.dims3()?;

        let original_dtype = xs.dtype();
        let mut xs = xs.clone();
        if self.qkv_proj.is_quant() {
            xs = xs.to_dtype(DType::F32)?;
        }
        let mut qkv = self.qkv_proj.lora_forward(
            &xs,
            scalings.clone(),
            global_scaling_weight,
            is_scaling_pass,
        )?;
        if self.qkv_proj.is_quant() {
            qkv = qkv.to_dtype(original_dtype)?;
        }
        let query_pos = self.num_heads * self.head_dim;
        let q = qkv.narrow(D::Minus1, 0, query_pos)?;
        let k = qkv.narrow(D::Minus1, query_pos, self.num_kv_heads * self.head_dim)?;
        let v = qkv.narrow(
            D::Minus1,
            query_pos + self.num_kv_heads * self.head_dim,
            self.num_kv_heads * self.head_dim,
        )?;

        let q = q
            .reshape((b_sz, q_len, self.num_heads, self.head_dim))?
            .transpose(1, 2)?;
        let k = k
            .reshape((b_sz, q_len, self.num_kv_heads, self.head_dim))?
            .transpose(1, 2)?;
        let v = v
            .reshape((b_sz, q_len, self.num_kv_heads, self.head_dim))?
            .transpose(1, 2)?;

        let (q, k) = self.rotary_emb.forward(&q, &k, seqlen_offsets)?;

        let (k, v) = match &*kv_cache {
            None => (k, v),
            Some((prev_k, prev_v)) => {
                let k = Tensor::cat(&[prev_k, &k], 2)?;
                let v = Tensor::cat(&[prev_v, &v], 2)?;
                (k, v)
            }
        };
        *kv_cache = Some((k.clone(), v.clone()));

        let k = repeat_kv(k, self.num_kv_groups)?.contiguous()?;
        let v = repeat_kv(v, self.num_kv_groups)?.contiguous()?;

        let mut attn_output = if self.use_flash_attn {
            // flash-attn expects (b_sz, seq_len, nheads, head_dim)
            let q = q.transpose(1, 2)?;
            let k = k.transpose(1, 2)?;
            let v = v.transpose(1, 2)?;
            let softmax_scale = 1f32 / (self.head_dim as f32).sqrt();
            flash_attn(&q, &k, &v, softmax_scale, q_len > 1)?.transpose(1, 2)?
        } else {
            let scale = 1f64 / f64::sqrt(self.head_dim as f64);
            let attn_weights = (q.matmul(&k.transpose(2, 3)?)? * scale)?;

            let attn_weights = match attention_mask {
                None => attn_weights,
                Some(mask) => attn_weights.broadcast_add(mask)?,
            };
            let attn_weights = candle_nn::ops::softmax_last_dim(&attn_weights)?;
            attn_weights.matmul(&v)?
        };
        if self.qkv_proj.is_quant() {
            attn_output = attn_output.to_dtype(DType::F32)?;
        }
        let mut res = self.o_proj.lora_forward(
            &attn_output.transpose(1, 2)?.reshape((b_sz, q_len, ()))?,
            scalings.clone(),
            global_scaling_weight,
            is_scaling_pass,
        )?;
        if self.qkv_proj.is_quant() {
            res = res.to_dtype(original_dtype)?;
        }
        Ok(res)
    }
}

#[derive(Debug, Clone)]
struct Mlp {
    gate_up_proj: Arc<dyn LinearLayerLike + Send + Sync>,
    down_proj: Arc<dyn LinearLayerLike + Send + Sync>,
    act_fn: candle_nn::Activation,
    i_size: usize,
}

impl Mlp {
    fn new(
        cfg: &Config,
        vb: VarBuilder,
        lora_config: &[(String, LoraConfig)],
        count: &mut usize,
        ord: &Ordering,
    ) -> Result<Self> {
        let hidden_size = cfg.hidden_size;
        let i_size = cfg.intermediate_size;
        let gate_up_proj = linear_no_bias(
            hidden_size,
            2 * i_size,
            vb.pp("gate_up_proj"),
            lora_config,
            count,
            ord,
        )?;
        let down_proj = linear_no_bias(
            i_size,
            hidden_size,
            vb.pp("down_proj"),
            lora_config,
            count,
            ord,
        )?;
        Ok(Self {
            gate_up_proj,
            down_proj,
            act_fn: cfg.hidden_act,
            i_size,
        })
    }

    fn forward(
        &self,
        xs: &Tensor,
        scalings: Option<Tensor>,
        global_scaling_weight: f64,
        is_scaling_pass: Option<f64>,
    ) -> Result<Tensor> {
        let original_dtype = xs.dtype();
        let mut xs = xs.clone();
        if self.gate_up_proj.is_quant() {
            xs = xs.to_dtype(DType::F32)?;
        }
        let up_states = self.gate_up_proj.lora_forward(
            &xs,
            scalings.clone(),
            global_scaling_weight,
            is_scaling_pass,
        )?;
        let gate = up_states.narrow(D::Minus1, 0, self.i_size)?;
        let up_states = up_states.narrow(D::Minus1, self.i_size, self.i_size)?;
        let up_states = (up_states * gate.apply(&self.act_fn))?;
        let mut res = self.down_proj.lora_forward(
            &up_states,
            scalings,
            global_scaling_weight,
            is_scaling_pass,
        )?;
        if self.gate_up_proj.is_quant() {
            res = res.to_dtype(original_dtype)?;
        }
        Ok(res)
    }
}

#[derive(Debug, Clone)]
struct DecoderLayer {
    self_attn: Attention,
    mlp: Mlp,
    input_layernorm: RmsNorm,
    post_attention_layernorm: RmsNorm,
}

impl DecoderLayer {
    fn new(
        rotary_emb: Arc<PhiRotaryEmbedding>,
        cfg: &Config,
        vb: VarBuilder,
        lora_config: &[(String, LoraConfig)],
        count: &mut usize,
        ord: &Ordering,
    ) -> Result<Self> {
        let self_attn =
            Attention::new(rotary_emb, cfg, vb.pp("self_attn"), lora_config, count, ord)?;
        let mlp = Mlp::new(cfg, vb.pp("mlp"), lora_config, count, ord)?;
        let input_layernorm =
            RmsNorm::new(cfg.hidden_size, cfg.rms_norm_eps, vb.pp("input_layernorm"))?;
        let post_attention_layernorm = RmsNorm::new(
            cfg.hidden_size,
            cfg.rms_norm_eps,
            vb.pp("post_attention_layernorm"),
        )?;
        Ok(Self {
            self_attn,
            mlp,
            input_layernorm,
            post_attention_layernorm,
        })
    }

    #[allow(clippy::too_many_arguments)]
    fn forward(
        &mut self,
        xs: &Tensor,
        attention_mask: Option<&Tensor>,
        seqlen_offsets: &[usize],
        start_offsets_kernel: Tensor,
        kv_cache: &mut Option<(Tensor, Tensor)>,
        scalings: Option<Tensor>,
        global_scaling_weight: f64,
        is_scaling_pass: Option<f64>,
    ) -> Result<Tensor> {
        let residual = xs;
        let xs = self.input_layernorm.forward(xs)?;
        let xs = self.self_attn.forward(
            &xs,
            attention_mask,
            seqlen_offsets,
            start_offsets_kernel,
            kv_cache,
            scalings.clone(),
            global_scaling_weight,
            is_scaling_pass,
        )?;
        let xs = (xs + residual)?;
        let residual = &xs;
        let xs = self.mlp.forward(
            &xs.apply(&self.post_attention_layernorm)?,
            scalings,
            global_scaling_weight,
            is_scaling_pass,
        );
        residual + xs
    }
}

pub struct Model {
    embed_tokens: candle_nn::Embedding,
    layers: Vec<DecoderLayer>,
    norm: RmsNorm,
    lm_head: QLinear,
    dtype: DType,
    pub device: Device,
    pub cache: Cache,
    pub max_seq_len: usize,
    mapper: Box<dyn DeviceMapper + Send + Sync>,
    xlora_classifier: Option<XLoraClassifier>,
}

impl Model {
    pub fn new(
        cfg: &Config,
        vb: VarBuilder,
        lora_config: &[(String, LoraConfig)],
        xlora_config: Option<XLoraConfig>,
        xlora_ordering: Ordering,
        _is_gptx: bool,
        mapper: DeviceMapMetadata,
    ) -> Result<Self> {
        let vb_m = vb.pp("model");
        let embed_tokens =
            candle_nn::embedding(cfg.vocab_size, cfg.hidden_size, vb_m.pp("embed_tokens"))?;
        let mut layers = Vec::with_capacity(cfg.num_hidden_layers);
        let vb_l = vb_m.pp("layers");
        let mapper = mapper.into_mapper(cfg.num_hidden_layers, vb.device())?;
        let mut count = 0;
        for layer_idx in 0..cfg.num_hidden_layers {
            let rotary_emb = Arc::new(PhiRotaryEmbedding::new(
                vb.dtype(),
                cfg,
                mapper.device_for(layer_idx).unwrap_or(vb.device()),
            )?);
            let layer = DecoderLayer::new(
                rotary_emb.clone(),
                cfg,
                mapper.set_device(layer_idx, vb_l.pp(layer_idx)),
                lora_config,
                &mut count,
                &xlora_ordering,
            )?;
            layers.push(layer)
        }
        if xlora_config.is_none() {
            // We are now a LoRA model so we must merge the weights
            info!("Merging LoRA adapters.");
            for layer in layers.iter_mut().tqdm() {
                Arc::get_mut(&mut layer.self_attn.qkv_proj)
                    .unwrap()
                    .merge_weights()?;
                Arc::get_mut(&mut layer.self_attn.o_proj)
                    .unwrap()
                    .merge_weights()?;

                Arc::get_mut(&mut layer.mlp.down_proj)
                    .unwrap()
                    .merge_weights()?;
                Arc::get_mut(&mut layer.mlp.gate_up_proj)
                    .unwrap()
                    .merge_weights()?;
            }
        }
        let norm = RmsNorm::new(cfg.hidden_size, cfg.rms_norm_eps, vb_m.pp("norm"))?;
        let lm_head = candle_nn::linear_no_bias(cfg.hidden_size, cfg.vocab_size, vb.pp("lm_head"))?;
        Ok(Self {
            embed_tokens,
            layers,
            norm,
            lm_head: QLinear::from_linear(lm_head),
            device: vb.device().clone(),
            dtype: vb.dtype(),
            cache: Cache::new(cfg.num_hidden_layers, true),
            max_seq_len: cfg.max_position_embeddings,
            mapper,
            xlora_classifier: xlora_config.map(|xlora_config| {
                XLoraClassifier::new(xlora_config, count, lora_config.len(), vb, false).unwrap()
            }),
        })
    }

    fn prepare_decoder_attention_mask(
        &self,
        b_size: usize,
        tgt_len: usize,
        seqlen_offset: usize,
    ) -> Result<Tensor> {
        let mask: Vec<_> = (0..tgt_len)
            .flat_map(|i| (0..tgt_len).map(move |j| if i < j { f32::NEG_INFINITY } else { 0. }))
            .collect();
        let mask = Tensor::from_slice(&mask, (tgt_len, tgt_len), &self.device)?;
        let mask = if seqlen_offset > 0 {
            let mask0 = Tensor::zeros((tgt_len, seqlen_offset), DType::F32, &self.device)?;
            Tensor::cat(&[&mask0, &mask], D::Minus1)?
        } else {
            mask
        };
        mask.expand((b_size, 1, tgt_len, tgt_len + seqlen_offset))?
            .to_dtype(self.dtype)
    }

    fn calculate_past_kv_len(&mut self, seq_len: usize) -> Result<usize> {
        let cache = self.cache.lock();
        let kv_cache_1 = cache.first().unwrap();
        if kv_cache_1.is_none() {
            return Ok(0);
        }
        let k_cache_1 = &kv_cache_1.as_ref().unwrap().0;
        if k_cache_1.dims()[0] <= seq_len {
            Ok(0)
        } else {
            let indexed = k_cache_1.i(seq_len)?;
            let dims = indexed.dims();
            Ok(dims[dims.len() - 2])
        }
    }

    #[allow(clippy::too_many_arguments)]
    fn inner_forward(
        &mut self,
        input_ids: &Tensor,
        seqlen_offsets: &[usize],
        start_offsets_kernel: Tensor,
        scalings: Option<Tensor>,
        is_full_pass: bool,
        no_kv_cache: bool,
        is_scaling_pass: Option<f64>,
    ) -> Result<Tensor> {
        let (b_size, seq_len) = input_ids.dims2()?;
        let past_key_values_length = self.calculate_past_kv_len(seq_len)?;
        let attention_mask = if seq_len <= 1 {
            None
        } else {
            let mask =
                self.prepare_decoder_attention_mask(b_size, seq_len, past_key_values_length)?;
            Some(mask)
        };
        let mut xs = self.embed_tokens.forward(input_ids)?;
        let mut cache = if is_full_pass {
            if no_kv_cache {
                let mut new_cache = Vec::new();
                for _ in 0..self.cache.xlora_lock().len() {
                    new_cache.push(None);
                }

                *self.cache.xlora_lock() = new_cache.clone();
            }
            self.cache.xlora_lock()
        } else {
            self.cache.lock()
        };
        for (i, layer) in self.layers.iter_mut().enumerate() {
            xs = self.mapper.map(xs, i)?;
            xs = layer.forward(
                &xs,
                attention_mask
                    .as_ref()
                    .map(|m| m.to_device(xs.device()).unwrap())
                    .as_ref(),
                seqlen_offsets,
                start_offsets_kernel.clone(),
                &mut cache[i],
                scalings.clone(),
                self.xlora_classifier
                    .as_ref()
                    .map(|classifier| classifier.get_global_scaling_weight())
                    .unwrap_or(1.0),
                is_scaling_pass,
            )?
        }
        xs.apply(&self.norm)
    }

    #[allow(clippy::too_many_arguments)]
    pub fn forward(
        &mut self,
        input_ids: &Tensor,
        input_ids_full: &Tensor,
        seqlen_offsets: &[usize],
        seqlen_offsets_full: &[usize],
        start_offsets_kernel: Tensor,
        start_offsets_kernel_full: Tensor,
        no_kv_cache: bool,
        non_granular_state: &Option<NonGranularState>,
        context_lens: Vec<usize>,
    ) -> Result<Tensor> {
        if self.xlora_classifier.is_some() {
            let scalings = self.get_scalings(
                input_ids,
                input_ids_full,
                seqlen_offsets,
                seqlen_offsets_full,
                &start_offsets_kernel,
                &start_offsets_kernel_full,
                no_kv_cache,
                non_granular_state,
            )?;

            if no_kv_cache {
                let mut res = self
                    .inner_forward(
                        input_ids_full,
                        seqlen_offsets_full,
                        start_offsets_kernel_full,
                        Some(scalings),
                        true,
                        no_kv_cache,
                        None,
                    )?
                    .contiguous()?;
                if self.lm_head.is_quant() {
                    res = res.to_dtype(DType::F32)?;
                }
                extract_logits(&res.apply(&self.lm_head)?, context_lens)
            } else {
                // is_full_pass=true is ok because no_kv_cache=false
                let mut res = self
                    .inner_forward(
                        input_ids,
                        seqlen_offsets,
                        start_offsets_kernel,
                        Some(scalings),
                        true,
                        no_kv_cache,
                        None,
                    )?
                    .contiguous()?;
                if self.lm_head.is_quant() {
                    res = res.to_dtype(DType::F32)?;
                }
                extract_logits(&res.apply(&self.lm_head)?, context_lens)
            }
        } else {
            let mut res = self
                .inner_forward(
                    input_ids,
                    seqlen_offsets,
                    start_offsets_kernel,
                    None,
                    false,
                    no_kv_cache,
                    None,
                )?
                .contiguous()?;
            if self.lm_head.is_quant() {
                res = res.to_dtype(DType::F32)?;
            }
            extract_logits(&res.apply(&self.lm_head)?, context_lens)
        }
    }
}

impl NormalModel for Model {
    fn forward(
        &mut self,
        _input_ids: &Tensor,
        _seqlen_offsets: &[usize],
        _start_offsets_kernel: Tensor,
        _context_lens: Vec<usize>,
    ) -> Result<Tensor> {
        unreachable!()
    }
    fn xlora_forward(
        &mut self,
        input_ids: &Tensor,
        input_ids_full: &Tensor,
        seqlen_offsets: &[usize],
        seqlen_offsets_full: &[usize],
        start_offsets_kernel: Tensor,
        start_offsets_kernel_full: Tensor,
        no_kv_cache: bool,
        non_granular_state: &Option<crate::xlora_models::NonGranularState>,
        context_lens: Vec<usize>,
    ) -> Result<Tensor> {
        self.forward(
            input_ids,
            input_ids_full,
            seqlen_offsets,
            seqlen_offsets_full,
            start_offsets_kernel,
            start_offsets_kernel_full,
            no_kv_cache,
            non_granular_state,
            context_lens,
        )
    }
    fn cache(&self) -> &Cache {
        &self.cache
    }
    fn device(&self) -> &Device {
        &self.device
    }
    fn is_xlora(&self) -> bool {
        true
    }
    fn max_seq_len(&self) -> usize {
        self.max_seq_len
    }
    fn get_tensors(&mut self) -> Vec<&mut QMatMul> {
        let mut tensors = Vec::new();
        tensors.push(self.lm_head.inner());
        for layer in &mut self.layers {
            tensors.push(Arc::get_mut(&mut layer.self_attn.qkv_proj).unwrap().inner());
            tensors.push(Arc::get_mut(&mut layer.self_attn.o_proj).unwrap().inner());
            tensors.push(Arc::get_mut(&mut layer.mlp.down_proj).unwrap().inner());
            tensors.push(Arc::get_mut(&mut layer.mlp.gate_up_proj).unwrap().inner());
        }
        tensors
    }
}

impl ScalingsMaker for Model {
    fn dtype(&self) -> DType {
        self.dtype
    }
    fn get_cache(&self) -> &Cache {
        &self.cache
    }
    fn get_classifier(&self) -> &XLoraClassifier {
        self.xlora_classifier.as_ref().unwrap()
    }
    fn forward(
        &mut self,
        input_ids: &Tensor,
        seqlen_offsets: &[usize],
        start_offsets_kernel: Tensor,
        scalings: Tensor,
        is_full_pass: bool,
        no_kv_cache: bool,
        is_scaling_pass: Option<f64>,
    ) -> Result<Tensor> {
        self.inner_forward(
            input_ids,
            seqlen_offsets,
            start_offsets_kernel,
            Some(scalings),
            is_full_pass,
            no_kv_cache,
            is_scaling_pass,
        )
    }
}
