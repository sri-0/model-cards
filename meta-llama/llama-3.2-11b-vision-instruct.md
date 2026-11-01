---
id: meta-llama/llama-3.2-11b-vision-instruct
name: Llama 3.2 11B Vision Instruct
owned_by: meta
type: llm
description: Llama 3.2 11B Vision Instruct is Meta's smaller open-weight Llama 3.2 multimodal model, adding image understanding to a Llama 3.1 text model through a cross-attention vision adapter.
aliases: [meta-llama/Llama-3.2-11B-Vision-Instruct, "llama3.2-vision:11b", "meta.llama3-2-11b-instruct-v1:0", meta-llama/llama-3-2-11b-vision-instruct]
context_length: 128000
capabilities: [tool_calling, vision]
architecture:
  input_modalities: [text, image]
  output_modalities: [text]
open_weights: true
license: Llama 3.2 Community License
release_date: "2024-09-25"
knowledge_cutoff: "2023-12"
benchmarks:
  gpqa_diamond: 22.1
  humanitys_last_exam: 5.5
  ifbench: 30.4
  long_context_reasoning: 12.7
  mmmu_pro: 29.3
  output_tokens_per_second: 30.3
  tau2_bench: 14.6
  terminal_bench_hard: 0.8
  time_to_first_token_seconds: 1.28
benchmark_variant: Llama 3.2 Instruct 11B (Vision)
sources:
  - https://huggingface.co/meta-llama/Llama-3.2-11B-Vision-Instruct
  - https://huggingface.co/api/models/meta-llama/Llama-3.2-11B-Vision-Instruct
  - https://artificialanalysis.ai/models/llama-3-2-instruct-11b-vision
  - https://dev.meta.ai/llama/docs/model-cards-and-prompt-formats/llama3_2
  - https://docs.aws.amazon.com/bedrock/latest/userguide/model-lifecycle-legacy.html
  - https://ollama.com/library/llama3.2-vision
  - https://github.com/BerriAI/litellm/blob/main/model_prices_and_context_window.json
  - https://openrouter.ai/api/v1/models
retrieved: "2026-11-01"
---

# Llama 3.2 11B Vision Instruct

## Overview
Llama 3.2 11B Vision Instruct (10.6B parameters) is the smaller of Meta's two Llama 3.2 multimodal models, released on September 25, 2024. OpenRouter does not list it; the id follows the Hugging Face repo `meta-llama/Llama-3.2-11B-Vision-Instruct`. Meta adds a separately trained vision adapter, a set of cross-attention layers fed by an image encoder, to a Llama 3.1 text model, trained on 6B image-text pairs. It takes text, or text plus an image, and returns text. With text-only input it behaves like the Llama 3.1 text models, including their tool calling. Meta gives a 128k context window (Artificial Analysis lists 128,000 tokens) and a December 2023 cutoff. Lifecycle: Amazon Bedrock retired `meta.llama3-2-11b-instruct-v1:0` on 2026-07-07.

## Strengths
- Meta's results: 88.4 DocVQA, 83.4 ChartQA, 91.1 AI2 Diagram and 50.7 MMMU (val).
- Small enough for local use: Ollama's `llama3.2-vision:11b` package is 7.8 GB.
- Quick first token: 1.28 s on the provider Artificial Analysis measured.
- Drop-in image understanding for prompts written for Llama 3.1.

## Limitations
- English is the only supported language for image-plus-text tasks.
- No tool calling when the input includes an image.
- Meta says the Llama 3.2 multimodal models are not accessible from the EU.
- Low scores from Artificial Analysis (Llama 3.2 Instruct 11B (Vision)): 29.3% on MMMU-Pro, 22.1% on GPQA Diamond and 14.6% on tau2-bench, at 30.3 output tokens per second.

## Good for
- English document and chart question answering.
- Image captioning and visual question answering on modest hardware.
- Adding image input to an existing Llama 3.1 prompt setup.
