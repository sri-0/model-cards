---
id: qwen/qwen3-vl-8b-instruct
name: Qwen3 VL 8B Instruct
owned_by: qwen
type: llm
description: Qwen3 VL 8B Instruct is Qwen's October 2025 open-weight (Apache-2.0) dense 8B vision-language model for image, video, document and GUI understanding with a native 256K context.
aliases: [Qwen/Qwen3-VL-8B-Instruct, "qwen3-vl:8b-instruct"]
context_length: 262144
max_output_tokens: 235929
capabilities: [tool_calling, vision, structured_output]
supported_parameters: [frequency_penalty, logit_bias, logprobs, max_tokens, presence_penalty, repetition_penalty, response_format, seed, stop, structured_outputs, temperature, tool_choice, tools, top_k, top_logprobs, top_p]
architecture:
  input_modalities: [image, text]
  output_modalities: [text]
  tokenizer: Qwen3
open_weights: true
license: Apache-2.0
release_date: "2025-10-15"
pricing:
  input: 0.25
  output: 0.75
  cache_read: 0.12
benchmarks:
  intelligence_index: 7.3
  omniscience_index: -51.9
  humanitys_last_exam: 2.7
  gpqa_diamond: 42.7
  terminal_bench_hard: 2.3
  long_context_reasoning: 16.7
  ifbench: 32.3
  tau2_bench: 29.2
  mmmu_pro: 47.3
benchmark_variant: Qwen3 VL 8B Instruct
sources:
  - https://openrouter.ai/qwen/qwen3-vl-8b-instruct
  - https://openrouter.ai/api/v1/models
  - https://artificialanalysis.ai/models/qwen3-vl-8b-instruct
  - https://huggingface.co/Qwen/Qwen3-VL-8B-Instruct
  - https://github.com/QwenLM/Qwen3-VL
  - https://ollama.com/library/qwen3-vl
retrieved: "2026-10-16"
---

# Qwen3 VL 8B Instruct

## Overview
Qwen3-VL-8B-Instruct was released on 2025-10-15 with the 4B size and their Thinking variants, according to the Qwen3-VL GitHub README; Artificial Analysis and OpenRouter list 2025-10-14. The Hugging Face card describes the shared Qwen3-VL architecture: Interleaved-MRoPE positional embeddings for long-horizon video, DeepStack fusion of multi-level ViT features and text-timestamp alignment for event localisation, with a native 256K context expandable to 1M, OCR in 32 languages, 2D and 3D grounding, GUI operation on PC and mobile, and visual coding from images. It is a dense model, as the name indicates. Qwen's suggested generation settings for vision tasks are top_p 0.8, top_k 20, temperature 0.7, presence penalty 1.5 and 16,384 output tokens. Benchmark tables are images only. Inference needs transformers 4.57.0. OpenRouter lists a 262,144-token context, 235,929 output tokens, no knowledge cutoff, and tool calling, vision and structured outputs. On Ollama, qwen3-vl:latest is the 8B Thinking build; qwen3-vl:8b-instruct is this model. The Qwen3.5 to Qwen3.8 generations, which have their own cards, supersede it.

## Strengths
- Artificial Analysis (Qwen3 VL 8B Instruct): MMMU-Pro 47.3%, IFBench 32.3%, tau2-bench 29.2%.
- Small enough for a single consumer GPU while keeping the full Qwen3-VL feature set.
- Prompt caching on OpenRouter at 0.12 USD per million cached tokens read.
- Tool calling and structured outputs on OpenRouter.

## Limitations
- Artificial Analysis Intelligence Index 7.3, Omniscience -51.9, GPQA Diamond 42.7%, long-context reasoning 16.7%, Terminal-Bench Hard 2.3%, Humanity's Last Exam 2.7%; no speed figures were published.
- No thinking mode in this variant.
- No published knowledge cutoff.
- No vendor benchmark figures are available in text form.

## Good for
- On-device OCR, document parsing and screenshot understanding.
- Lightweight GUI agents.
- Video captioning and question answering at low cost.
