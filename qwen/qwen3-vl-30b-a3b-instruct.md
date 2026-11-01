---
id: qwen/qwen3-vl-30b-a3b-instruct
name: Qwen3 VL 30B A3B Instruct
owned_by: qwen
type: llm
description: Qwen3 VL 30B A3B Instruct is Qwen's October 2025 open-weight (Apache-2.0) vision-language mixture-of-experts model (30B total, 3B active as its name states) for image, video, document and GUI understanding with a native 256K context.
aliases: [Qwen/Qwen3-VL-30B-A3B-Instruct, "qwen3-vl:30b-a3b-instruct"]
context_length: 262144
max_output_tokens: 16384
capabilities: [tool_calling, vision, structured_output]
supported_parameters: [frequency_penalty, logit_bias, logprobs, max_tokens, min_p, presence_penalty, repetition_penalty, response_format, seed, stop, structured_outputs, temperature, tool_choice, tools, top_k, top_logprobs, top_p]
architecture:
  input_modalities: [text, image]
  output_modalities: [text]
  tokenizer: Qwen3
open_weights: true
license: Apache-2.0
release_date: "2025-10-04"
knowledge_cutoff: "2025-03"
pricing:
  input: 0.15
  output: 0.6
benchmarks:
  intelligence_index: 7.9
  omniscience_index: -63.4
  humanitys_last_exam: 6.3
  gpqa_diamond: 69.5
  terminal_bench_hard: 6.1
  ifbench: 33.1
  tau2_bench: 19
  mmmu_pro: 62.1
  output_tokens_per_second: 26.1
  time_to_first_token_seconds: 2.78
benchmark_variant: Qwen3 VL 30B A3B Instruct
sources:
  - https://openrouter.ai/qwen/qwen3-vl-30b-a3b-instruct
  - https://openrouter.ai/api/v1/models
  - https://artificialanalysis.ai/models/qwen3-vl-30b-a3b-instruct
  - https://huggingface.co/Qwen/Qwen3-VL-30B-A3B-Instruct
  - https://github.com/QwenLM/Qwen3-VL
  - https://ollama.com/library/qwen3-vl
retrieved: "2026-10-16"
---

# Qwen3 VL 30B A3B Instruct

## Overview
Qwen3-VL-30B-A3B-Instruct was released on 2025-10-04 with its Thinking variant and FP8 versions, according to the Qwen3-VL GitHub README; Artificial Analysis lists 2025-10-03 and OpenRouter 2025-10-06. The Hugging Face card gives no parameter table; the name follows Qwen's 30B-total, 3B-active mixture-of-experts naming. It shares the Qwen3-VL architecture: Interleaved-MRoPE for long video, DeepStack fusion of multi-level ViT features and text-timestamp alignment, with a native 256K context expandable to 1M, OCR in 32 languages, 2D and 3D grounding, GUI operation and visual coding from images. Benchmark tables are images only. Inference needs transformers 4.57.0. OpenRouter lists a 262,144-token context, 16,384 output tokens, a March 2025 cutoff, and tool calling, vision and structured outputs. On Ollama, qwen3-vl:30b and qwen3-vl:30b-a3b resolve to the Thinking build; qwen3-vl:30b-a3b-instruct is this model. The Qwen3.5 to Qwen3.8 generations, which have their own cards, supersede it.

## Strengths
- Artificial Analysis (Qwen3 VL 30B A3B Instruct): MMMU-Pro 62.1%, GPQA Diamond 69.5%, IFBench 33.1%.
- About 3B active parameters, so it serves images and video on a single GPU.
- Qwen says text performance matches the flagship Qwen3 models, suiting document AI, OCR and UI assistance.
- Low OpenRouter price at 0.15 USD input and 0.60 USD output per million tokens.

## Limitations
- Artificial Analysis Intelligence Index 7.9, Omniscience -63.4, tau2-bench 19%, Terminal-Bench Hard 6.1%, Humanity's Last Exam 6.3%.
- 26.1 output tokens per second and 2.78 s to first token in Artificial Analysis' measurements.
- No thinking mode in this variant and 16,384 output tokens on OpenRouter.
- No vendor benchmark figures are available in text form.

## Good for
- Local document parsing, OCR and chart reading.
- GUI grounding for lightweight computer-use agents.
- Video question answering on modest hardware.
