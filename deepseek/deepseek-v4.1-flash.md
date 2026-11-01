---
id: deepseek/deepseek-v4.1-flash
name: DeepSeek V4.1 Flash
owned_by: deepseek
type: llm
description: DeepSeek V4.1 Flash is DeepSeek's September 2026 multimodal MoE model (552B backbone, 8B active on input and 16B on output, MIT) built on a Causal Encoder-Decoder with a 1M-token context.
aliases: [deepseek-ai/DeepSeek-V4.1-Flash, deepseek-flash, deepseek/deepseek-flash, "~deepseek/deepseek-flash-latest", "deepseek-v4.1-flash:cloud"]
context_length: 1048576
max_output_tokens: 943718
capabilities: [tool_calling, reasoning, vision, structured_output]
supported_parameters: [frequency_penalty, include_reasoning, logit_bias, logprobs, max_tokens, min_p, presence_penalty, reasoning, reasoning_effort, repetition_penalty, response_format, seed, stop, structured_outputs, temperature, tool_choice, tools, top_k, top_logprobs, top_p]
architecture:
  input_modalities: [text, image]
  output_modalities: [text]
  tokenizer: DeepSeek
open_weights: true
license: MIT
release_date: "2026-09-10"
pricing:
  input: 0.02376
  output: 0.72
  cache_read: 0.0054
benchmarks:
  intelligence_index: 39.5
  omniscience_index: -5.3
  humanitys_last_exam: 39.2
  scicode: 51.9
  terminal_bench_4: 26.8
  long_context_reasoning: 84
  mmmu_pro: 77
  output_tokens_per_second: 176.6
  time_to_first_token_seconds: 1.13
benchmark_variant: DeepSeek V4.1 Flash (Max)
sources:
  - https://openrouter.ai/deepseek/deepseek-v4.1-flash
  - https://openrouter.ai/api/v1/models
  - https://artificialanalysis.ai/models/deepseek-v4-1-flash
  - https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash
  - https://api-docs.deepseek.com/news/news260910
  - https://api-docs.deepseek.com/updates
  - https://api-docs.deepseek.com/quick_start/pricing
  - https://api-docs.deepseek.com/guides/thinking_mode
  - https://api-docs.deepseek.com/guides/vision
  - https://openrouter.ai/~deepseek/deepseek-flash-latest
  - https://ollama.com/library/deepseek-v4.1-flash
  - https://docs.litellm.ai/docs/providers/deepseek
retrieved: "2026-10-16"
---

# DeepSeek V4.1 Flash

## Overview
DeepSeek V4.1 Flash, released 2026-09-10 under the MIT licence, is the first model of DeepSeek's Causal Encoder-Decoder (CED) family: a 40-layer transformer (20-layer causal encoder, 20-layer decoder) with a 552B-parameter MoE backbone that activates 8B parameters per token on input and 16B on output. Compressed Sparse Attention 2 and an FP4 main KV cache bring the cache to 890 bytes per token, about a quarter of V4 Flash; a DeepSeek-ViT encoder gives native image input. It was trained from scratch on 45T multimodal tokens with a 1M-token context. The vendor API serves it as `deepseek-flash` (thinking on by default, effort low/high/max, 384K maximum output), and the retired ids `deepseek-v4-flash` and `deepseek-v4-flash-vision-exp` route here. OpenRouter's `~deepseek/deepseek-flash-latest` ("always redirects to the latest model in the DeepSeek Flash family") resolves here; LiteLLM lists `deepseek/deepseek-flash`; Ollama's cloud-only tag is `deepseek-v4.1-flash:cloud` (Ollama states 763B parameters, DeepSeek 552B). Supersedes `deepseek/deepseek-v4-flash-0731`.

## Strengths
- DeepSeek reports at max effort: Terminal-Bench 2.1 90.6, Terminal-Bench 4.0 31.2, DeepSWE v1.1 74.2, CyberGym 88.1, Codeforces 3471, ahead of V4 Pro.
- Artificial Analysis (variant DeepSeek V4.1 Flash (Max)): Intelligence Index 39.5, long-context reasoning 84.0%, MMMU-Pro 77.0%, Terminal-Bench 4.0 26.8%, 176.6 tokens per second.
- Vendor price $0.15 input and $0.60 output per million tokens off-peak ($0.30/$1.20 peak), cache hits $0.003; OpenRouter $0.02376/$0.72.

## Limitations
- The open weights take a 1 to 100 reasoning-effort integer; the vendor API exposes only low, high and max.
- HLE 39.2% and Omniscience Index -5.3 in AA's tests.
- Self-hosting: no Jinja template (use `encoding.py` or the deepseek-recipe Rust library); DeepSeek recommends max_tokens of at least 256K; community inference support is still being developed.

## Good for
- Coding, terminal and computer-use agents with long multi-step runs.
- Image, chart and document understanding alongside text.
- Cache-heavy agent workloads.
