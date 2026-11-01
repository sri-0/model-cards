---
id: qwen/qwen2.5-vl-72b-instruct
name: Qwen2.5 VL 72B Instruct
owned_by: qwen
type: llm
description: Qwen2.5 VL 72B Instruct is Alibaba's 72B-parameter open-weight vision-language model (Qwen licence) for image, document, video and GUI understanding, announced in January 2025.
aliases: [Qwen/Qwen2.5-VL-72B-Instruct, "qwen2.5vl:72b"]
context_length: 128000
max_output_tokens: 115200
capabilities: [vision, structured_output]
supported_parameters: [frequency_penalty, logit_bias, logprobs, max_tokens, presence_penalty, repetition_penalty, response_format, seed, stop, structured_outputs, temperature, top_k, top_logprobs, top_p]
architecture:
  input_modalities: [text, image]
  output_modalities: [text]
  tokenizer: Qwen
open_weights: true
license: Qwen License Agreement
release_date: "2025-01-26"
knowledge_cutoff: "2024-06"
pricing:
  input: 0.8
  output: 1
  cache_read: 0.4
sources:
  - https://openrouter.ai/qwen/qwen2.5-vl-72b-instruct
  - https://openrouter.ai/api/v1/models
  - https://huggingface.co/Qwen/Qwen2.5-VL-72B-Instruct
  - https://qwenlm.github.io/blog/qwen2.5-vl/
  - https://github.com/QwenLM/Qwen2.5-VL
  - https://ollama.com/library/qwen2.5vl
retrieved: "2026-10-16"
---

# Qwen2.5 VL 72B Instruct

## Overview
Qwen2.5 VL 72B Instruct is the largest of the three Qwen2.5-VL sizes (3B, 7B, 72B). The Qwen blog post is dated 2025-01-26, which this card uses; the Qwen GitHub README dates the release 2025-01-28 and OpenRouter lists 2025-02-01. The Hugging Face card describes dynamic resolution and frame-rate sampling for video, mRoPE aligned to absolute time, and a vision encoder with window attention, SwiGLU and RMSNorm. config.json ships at 32,768 tokens; Qwen says YaRN extension harms temporal and spatial localisation and is not recommended. OpenRouter lists a 128,000-token context and 115,200 output tokens, with vision and structured outputs but no tool calling. The weights use the Qwen licence. Inference needs transformers built from source (qwen2_5_vl) and the qwen-vl-utils package. Ollama serves it as qwen2.5vl:72b. Qwen3-VL and the Qwen3.5 to Qwen3.8 generations, which have their own cards, supersede it.

## Strengths
- Qwen reports MMMU val 70.2, MMMU-Pro 51.1, MathVista mini 74.8, DocVQA val 96.4 and OCRBench 885.
- Qwen reports VideoMME 73.3 without subtitles, ScreenSpot 87.1 and AndroidWorld 35%, and says it understands videos over an hour long.
- Returns bounding boxes or points as JSON for object grounding and structured output for invoices, forms and tables.
- Acts as a visual agent for computer and phone use.

## Limitations
- Qwen reports OSWorld 8.83, below Claude's 14.90 in the same table.
- No Artificial Analysis figures are recorded on this card.
- No tool calling through OpenRouter and no reasoning mode.
- Qwen licence rather than Apache 2.0, and a 72B model to host.

## Good for
- Document parsing, chart reading and OCR in production pipelines.
- Video understanding with event localisation.
- GUI grounding for computer-use agents.
