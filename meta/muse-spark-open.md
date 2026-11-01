---
id: meta/muse-spark-open
name: Muse Spark Open
owned_by: meta
type: llm
description: Muse Spark Open is Meta's open-weight 816B-parameter (42B active) mixture-of-experts version of Muse Spark, with text, image, video and audio input and a 1M-token context for agentic coding.
aliases: [meta-models/Muse-Spark-Open-816B-A42B, meta-models/Muse-Spark-Open-816B-A42B-NVFP4, meta-models/muse-spark-open, accounts/fireworks/models/muse-spark-open, muse-spark-open]
context_length: 1048576
max_output_tokens: 131072
capabilities: [tool_calling, reasoning, vision, structured_output]
supported_parameters: [frequency_penalty, include_reasoning, logit_bias, logprobs, max_tokens, min_p, presence_penalty, reasoning, reasoning_effort, repetition_penalty, response_format, seed, stop, structured_outputs, temperature, tool_choice, tools, top_k, top_logprobs, top_p]
architecture:
  input_modalities: [text, image, video, file, audio]
  output_modalities: [text]
  tokenizer: Other
open_weights: true
license: Muse Model License
release_date: "2026-10-15"
knowledge_cutoff: "2026-01"
pricing:
  input: 1.25
  output: 4.25
  cache_read: 0.15
benchmarks:
  intelligence_index: 24.7
  gpqa_diamond: 89.0
  humanitys_last_exam: 43.9
  long_context_reasoning: 78.3
  mmmu_pro: 80.9
  omniscience_index: 25.8
  output_tokens_per_second: 139.3
  scicode: 58.4
  terminal_bench_4: 8.1
  time_to_first_token_seconds: 0.73
benchmark_variant: Muse Spark Open (Xhigh)
sources:
  - https://openrouter.ai/meta/muse-spark-open
  - https://openrouter.ai/api/v1/models
  - https://artificialanalysis.ai/models/muse-spark-open
  - https://huggingface.co/meta-models/Muse-Spark-Open-816B-A42B
  - https://huggingface.co/api/models/meta-models/Muse-Spark-Open-816B-A42B
  - https://huggingface.co/meta-models/Muse-Spark-Open-816B-A42B-NVFP4
  - https://dev.meta.ai/models/muse-spark-open
  - https://dev.meta.ai/docs/muse-spark-open
  - https://dev.meta.ai/docs/muse-spark-open/get-the-model
  - https://dev.meta.ai/docs/muse-spark-open/deploy
  - https://dev.meta.ai/docs/muse-spark-open/settings
  - https://dev.meta.ai/docs/muse-spark-open/prompting
  - https://dev.meta.ai/resources/blog/build-with-muse-spark-open
  - https://dev.meta.ai/docs/models
  - https://github.com/BerriAI/litellm/blob/main/model_prices_and_context_window.json
retrieved: "2026-11-01"
---

# Muse Spark Open

## Overview
Muse Spark Open, released on October 15, 2026, is the open-weight version of Muse Spark. Meta derived it from the Muse Spark model released in August, with extra safety post-training to make it more robust against misuse without system guardrails. It is a sparse mixture-of-experts transformer with 816B total and 42B active parameters (256 experts, 8 active per token) plus a 1.8B perception encoder. It takes text, image, video and audio, returns text, and has a 1,048,576-token context; OpenRouter caps output at 131,072 tokens. Meta's chat template gives a 2026-01-04 knowledge cutoff. Reasoning effort is low, medium, high or xhigh (template default xhigh, OpenRouter default medium). It is not on Meta Model API: download BF16 (about 1.65 TB, 8 x B300) or NVFP4 (about 537 GB, 4 x B300) weights, or use Together AI, Fireworks, Baseten, Groq, Nebius, Modal or OpenRouter.

## Strengths
- Artificial Analysis (Muse Spark Open, Xhigh): Intelligence Index 24.7, 89% on GPQA Diamond, 80.9% on MMMU-Pro, 0.73 s to first token and 139.3 tokens per second. Meta's card quotes an AA Intelligence Index of 39.
- Meta's results at xhigh: 89.2 MCP-Atlas, 80.4 OSWorld Verified, 76.4 Terminal-Bench 2.1 and 60 DeepSWE 1.1.
- Runs on SGLang, vLLM, TensorRT-LLM, Transformers, llama.cpp, MLX (two M5 Ultra Mac Studios) and Unsloth GGUFs.
- The licence allows commercial use, fine-tuning and distillation.

## Limitations
- Licence terms: show "Built with Muse Spark Open"; model-as-a-service businesses above US$20 million revenue need a separate agreement with Meta; not for users under 18.
- Heavy: Meta budgets about 2 TB of VRAM for BF16.
- 8.1% on Terminal-Bench 4.0; with very short or low-resolution videos it may reply that it cannot view the video.

## Good for
- Self-hosted or air-gapped coding agents.
- Fine-tuning and reinforcement-learning post-training.
- Multimodal agents over screenshots, documents, audio and video.
