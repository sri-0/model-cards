---
id: z-ai/glm-4.5v
name: GLM 4.5V
owned_by: z-ai
type: llm
description: GLM-4.5V is Z.ai's open-weight (MIT) vision-language reasoning model built on GLM-4.5-Air (106B total, 12B active), for image, video, document and GUI tasks with a switchable thinking mode.
aliases: [glm-4.5v, zai/glm-4.5v, zai-org/GLM-4.5V, zai-org/GLM-4.5V-FP8]
context_length: 65536
max_output_tokens: 16384
capabilities: [tool_calling, reasoning, vision]
supported_parameters: [frequency_penalty, include_reasoning, max_tokens, presence_penalty, reasoning, repetition_penalty, response_format, seed, stop, temperature, tool_choice, tools, top_k, top_p]
architecture:
  input_modalities: [text, image]
  output_modalities: [text]
  tokenizer: Other
open_weights: true
license: MIT
release_date: "2025-08-11"
knowledge_cutoff: "2024-12"
pricing:
  input: 0.6
  output: 1.8
  cache_read: 0.11
benchmarks:
  gpqa_diamond: 68.4
  humanitys_last_exam: 6.3
  ifbench: 34.2
  long_context_reasoning: 0
  mmmu_pro: 50.5
  output_tokens_per_second: 63.2
  tau2_bench: 22.5
  terminal_bench_hard: 5.3
  time_to_first_token_seconds: 3.32
benchmark_variant: GLM-4.5V (Reasoning)
sources:
  - https://openrouter.ai/z-ai/glm-4.5v
  - https://openrouter.ai/api/v1/models
  - https://artificialanalysis.ai/models/glm-4-5v
  - https://huggingface.co/zai-org/GLM-4.5V
  - https://huggingface.co/api/models/zai-org/GLM-4.5V
  - https://huggingface.co/zai-org/GLM-4.5V/raw/main/config.json
  - https://docs.z.ai/guides/vlm/glm-4.5v
  - https://docs.z.ai/guides/overview/pricing
  - https://docs.bigmodel.cn/cn/update/new-releases
  - https://raw.githubusercontent.com/BerriAI/litellm/main/model_prices_and_context_window.json
retrieved: "2026-11-01"
---

# GLM 4.5V

## Overview
GLM-4.5V was released on 2025-08-11. Z.ai builds it on the GLM-4.5-Air text model (106B total, 12B active parameters) and continues the GLM-4.1V-Thinking training approach. Z.ai's API accepts video, images, text and files and returns up to 16K tokens; OpenRouter lists text and image input with a 65,536-token context, matching the 65,536 positions in config.json. A thinking-mode switch works as in GLM-4.5. Grounding answers mark bounding boxes as `[x1,y1,x2,y2]` coordinates normalised to 0-1000. Weights and an FP8 build are on Hugging Face under MIT, with transformers, vLLM and SGLang support.

## Strengths
- Z.ai reports state-of-the-art results among open models of its scale on 42 public vision-language benchmarks at launch.
- Covers webpage-to-code from screenshots or recordings, GUI agents, chart and long-document parsing, video understanding and object grounding.
- Artificial Analysis measured 50.5% on MMMU-Pro and 63.2 output tokens per second on GLM-4.5V (Reasoning).

## Limitations
- Artificial Analysis marks it deprecated, succeeded by GLM-4.6V.
- Text-only reasoning is weak: 6.3% on Humanity's Last Exam, 22.5% on tau2-bench and 0% on AA-LCR, whose roughly 100K-token inputs exceed its 64K window.
- 16K output limit on Z.ai's API.

## Good for
- Screenshot-to-code and GUI automation where GLM-4.6V is not yet adopted.
- Document, chart and video question answering on self-hosted multi-GPU servers.
