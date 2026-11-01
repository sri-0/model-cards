---
id: qwen/qwen3-vl-235b-a22b-instruct
name: Qwen3 VL 235B A22B Instruct
owned_by: qwen
type: llm
description: Qwen3 VL 235B A22B Instruct is Qwen's September 2025 open-weight (Apache-2.0) flagship vision-language mixture-of-experts model (235B total, 22B active) for image, video, document and GUI understanding with a native 256K context.
aliases: [Qwen/Qwen3-VL-235B-A22B-Instruct, "qwen3-vl:235b-a22b-instruct"]
context_length: 262144
max_output_tokens: 32768
capabilities: [tool_calling, vision, structured_output]
supported_parameters: [frequency_penalty, logit_bias, logprobs, max_tokens, min_p, presence_penalty, repetition_penalty, response_format, seed, stop, structured_outputs, temperature, tool_choice, tools, top_k, top_logprobs, top_p]
architecture:
  input_modalities: [text, image]
  output_modalities: [text]
  tokenizer: Qwen3
open_weights: true
license: Apache-2.0
release_date: "2025-09-23"
knowledge_cutoff: "2025-03"
pricing:
  input: 0.21
  output: 1.9
  cache_read: 0.1
benchmarks:
  intelligence_index: 9.9
  omniscience_index: -52.7
  humanitys_last_exam: 6.6
  gpqa_diamond: 71.2
  terminal_bench_hard: 6.8
  long_context_reasoning: 32.7
  ifbench: 42.7
  tau2_bench: 35.1
  mmmu_pro: 67.6
  output_tokens_per_second: 31.4
  time_to_first_token_seconds: 1.42
benchmark_variant: Qwen3 VL 235B A22B Instruct
sources:
  - https://openrouter.ai/qwen/qwen3-vl-235b-a22b-instruct
  - https://openrouter.ai/api/v1/models
  - https://artificialanalysis.ai/models/qwen3-vl-235b-a22b-instruct
  - https://huggingface.co/Qwen/Qwen3-VL-235B-A22B-Instruct
  - https://github.com/QwenLM/Qwen3-VL
  - https://ollama.com/library/qwen3-vl
retrieved: "2026-10-16"
---

# Qwen3 VL 235B A22B Instruct

## Overview
Qwen3-VL-235B-A22B-Instruct was released on 2025-09-23 together with its Thinking variant, according to the Qwen3-VL GitHub README, which also lists the Qwen3-VL paper of 2025-11-27. The Hugging Face card describes three architecture changes: Interleaved-MRoPE positional embeddings over time, width and height for long video; DeepStack fusion of multi-level ViT features; and text-timestamp alignment for event localisation. It gives a native 256K context expandable to 1M, OCR in 32 languages (up from 19), 2D and 3D grounding, GUI operation on PC and mobile, and visual coding that generates Draw.io, HTML, CSS and JavaScript from images. Benchmark tables are published as images only. Inference needs transformers 4.57.0. OpenRouter lists a 262,144-token context, 32,768 output tokens, a March 2025 cutoff, and tool calling, vision and structured outputs. On Ollama, qwen3-vl:235b and qwen3-vl:235b-a22b resolve to the Thinking build; qwen3-vl:235b-a22b-instruct is this model. The Qwen3.5 to Qwen3.8 generations, which have their own cards, supersede it.

## Strengths
- Artificial Analysis (Qwen3 VL 235B A22B Instruct): MMMU-Pro 67.6%, GPQA Diamond 71.2%, IFBench 42.7%, tau2-bench 35.1%.
- Qwen says text performance matches the flagship Qwen3 language models, with the same tool-calling support.
- Long video understanding with second-level indexing and multi-image, multi-turn dialogue.
- Prompt caching on OpenRouter at 0.10 USD per million cached tokens read.

## Limitations
- Artificial Analysis Intelligence Index 9.9, Omniscience -52.7, Terminal-Bench Hard 6.8%, long-context reasoning 32.7%, Humanity's Last Exam 6.6%.
- 31.4 output tokens per second and 1.42 s to first token in Artificial Analysis' measurements.
- No thinking mode in this variant and 32,768 output tokens on OpenRouter.
- 235B total parameters need a multi-GPU node to self-host.

## Good for
- Document AI, chart and table extraction and multilingual OCR.
- GUI agents and computer-use automation.
- Video analysis with precise timestamps.
