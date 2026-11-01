---
id: qwen/qwen3-vl-30b-a3b-thinking
name: Qwen3 VL 30B A3B Thinking
owned_by: qwen
type: llm
description: Qwen3 VL 30B A3B Thinking is the reasoning variant of Qwen's October 2025 open-weight (Apache-2.0) vision-language mixture-of-experts model (30B total, 3B active as its name states), with a native 256K context.
aliases: [Qwen/Qwen3-VL-30B-A3B-Thinking, "qwen3-vl:30b-a3b-thinking"]
context_length: 262144
max_output_tokens: 235929
capabilities: [tool_calling, reasoning, vision, structured_output]
supported_parameters: [frequency_penalty, include_reasoning, max_tokens, reasoning, response_format, structured_outputs, temperature, tool_choice, tools, top_k, top_p]
architecture:
  input_modalities: [text, image]
  output_modalities: [text]
  tokenizer: Qwen3
open_weights: true
license: Apache-2.0
release_date: "2025-10-04"
knowledge_cutoff: "2025-03"
pricing:
  input: 0.29
  output: 1
benchmarks:
  intelligence_index: 9.5
  omniscience_index: -57.6
  humanitys_last_exam: 8.9
  gpqa_diamond: 72
  terminal_bench_hard: 5.3
  ifbench: 45.1
  tau2_bench: 19.9
  mmmu_pro: 61.8
benchmark_variant: Qwen3 VL 30B A3B (Reasoning)
sources:
  - https://openrouter.ai/qwen/qwen3-vl-30b-a3b-thinking
  - https://openrouter.ai/api/v1/models
  - https://artificialanalysis.ai/models/qwen3-vl-30b-a3b-reasoning
  - https://huggingface.co/Qwen/Qwen3-VL-30B-A3B-Thinking
  - https://github.com/QwenLM/Qwen3-VL
  - https://ollama.com/library/qwen3-vl
retrieved: "2026-10-16"
---

# Qwen3 VL 30B A3B Thinking

## Overview
Qwen3-VL-30B-A3B-Thinking was released on 2025-10-04 alongside the Instruct variant and FP8 builds, according to the Qwen3-VL GitHub README; Artificial Analysis lists 2025-10-03 and OpenRouter 2025-10-06. The Hugging Face card says the Thinking editions enhance reasoning in STEM, maths and complex tasks, and shares the Qwen3-VL architecture: Interleaved-MRoPE for long video, DeepStack fusion of multi-level ViT features and text-timestamp alignment, with a native 256K context expandable to 1M, OCR in 32 languages, 2D and 3D grounding, GUI operation and visual coding from images. The card gives no parameter table; the name follows Qwen's 30B-total, 3B-active naming. Benchmark tables are images only. Inference needs transformers 4.57.0. OpenRouter lists a 262,144-token context, 235,929 output tokens, a March 2025 cutoff, and tool calling, reasoning, vision and structured outputs. On Ollama, qwen3-vl:30b-a3b-thinking is this model, and qwen3-vl:30b and qwen3-vl:30b-a3b resolve to the same build. The Qwen3.5 to Qwen3.8 generations, which have their own cards, supersede it.

## Strengths
- Artificial Analysis (Qwen3 VL 30B A3B (Reasoning)): GPQA Diamond 72%, MMMU-Pro 61.8%, IFBench 45.1%, Humanity's Last Exam 8.9%, each above the Instruct variant.
- About 3B active parameters, so it runs on a single GPU.
- Visible reasoning for STEM and maths questions over images.
- Tool calling with structured outputs on OpenRouter.

## Limitations
- Artificial Analysis Intelligence Index 9.5, Omniscience -57.6, tau2-bench 19.9%, Terminal-Bench Hard 5.3%; no speed figures were published.
- Thinking traces add latency and output tokens, at 1.00 USD per million output tokens on OpenRouter.
- OpenRouter exposes a reduced parameter set (no seed, stop or logprobs).
- No vendor benchmark figures are available in text form.

## Good for
- Visual maths and science problems that need step-by-step reasoning.
- Document and chart analysis where answers must be justified.
- Research on multimodal reasoning on modest hardware.
