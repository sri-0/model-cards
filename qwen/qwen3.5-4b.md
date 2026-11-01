---
id: qwen/qwen3.5-4b
name: Qwen3.5 4B
owned_by: qwen
type: llm
description: Qwen3.5 4B is one of Qwen's March 2026 small Qwen3.5 models, a dense open-weight (Apache-2.0) vision-language model with a hybrid Gated DeltaNet and gated attention design, optional thinking and a 262,144-token native context.
aliases: [Qwen/Qwen3.5-4B, "qwen3.5:4b"]
context_length: 262144
capabilities: [tool_calling, reasoning, vision]
architecture:
  input_modalities: [text, image, video]
  output_modalities: [text]
open_weights: true
license: Apache-2.0
release_date: "2026-03-02"
benchmarks:
  gpqa_diamond: 77.1
  humanitys_last_exam: 9.9
  ifbench: 52.0
  long_context_reasoning: 63.0
  mmmu_pro: 65.4
  output_tokens_per_second: 13.4
  tau2_bench: 92.1
  terminal_bench_hard: 18.2
  time_to_first_token_seconds: 0.87
benchmark_variant: Qwen3.5 4B (Reasoning)
sources:
  - https://huggingface.co/Qwen/Qwen3.5-4B
  - https://huggingface.co/api/models/Qwen/Qwen3.5-4B
  - https://huggingface.co/Qwen/Qwen3.5-4B/raw/main/config.json
  - https://artificialanalysis.ai/models/qwen3-5-4b
  - https://github.com/QwenLM/Qwen3.5
  - https://ollama.com/library/qwen3.5/tags
  - https://openrouter.ai/api/v1/models
retrieved: "2026-11-01"
---

# Qwen3.5 4B

## Overview
Qwen3.5-4B was released on 2026-03-02 with the 9B, 4B, 2B and 0.8B sizes, according to the QwenLM GitHub README (Artificial Analysis agrees). OpenRouter does not list it; the id follows the Hugging Face repo, and the 9B size has its own card. It is a causal language model with a vision encoder, trained with early fusion on multimodal tokens, taking text, image and video input. The language model has a hidden size of 2,560 and 32 layers laid out as 8 × (3 × Gated DeltaNet → 1 × gated attention), each followed by a feed-forward layer; Gated DeltaNet uses 32 V and 16 QK linear-attention heads and gated attention 16 query and 4 key-value heads, with tied embeddings and multi-token prediction. The context is 262,144 tokens natively, extensible to 1,010,000. Thinking is on by default, and Qwen advises keeping at least 128K tokens of context so thinking is not cut short; Qwen's serving commands use one GPU. Qwen states support for 201 languages and dialects. Serving uses SGLang or vLLM with the qwen3 reasoning parser and the qwen3_coder tool parser; Ollama serves it as qwen3.5:4b (3.3 to 4.0 GB).

## Strengths
- Qwen reports MMLU-Pro 79.1, GPQA Diamond 76.2, IFEval 89.8, TAU2-Bench 79.9 and AA-LCR 57.0, above GPT-OSS-20B's 74.8, 71.5, 88.2, no score and 30.7.
- Vision: MMMU 77.6, MMMU-Pro 66.3, OCRBench 85.0, VideoMME 83.5 with subtitles and AndroidWorld 58.6.
- Artificial Analysis (Qwen3.5 4B (Reasoning)): tau2-bench 92.1%, GPQA Diamond 77.1%, long-context reasoning 63%, MMMU-Pro 65.4%.

## Limitations
- Qwen reports LiveCodeBench v6 55.8, below GPT-OSS-20B's 74.6.
- Artificial Analysis measured 13.4 output tokens per second; Terminal-Bench Hard 18.2% and Humanity's Last Exam 9.9%.
- No published knowledge cutoff.

## Good for
- Local multimodal assistants for documents, charts and video.
- Tool-calling agents at 4B scale.
- Fine-tuning from the Qwen3.5-4B-Base checkpoint.
