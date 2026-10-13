---
id: z-ai/glm-5v-turbo
name: GLM 5V Turbo
owned_by: z-ai
type: llm
description: GLM-5V-Turbo is a proprietary Z.ai multimodal model for vision-based coding and GUI agent tasks, accepting image, video and text input with a 200K-token context window.
aliases: [glm-5v-turbo]
context_length: 202752
max_output_tokens: 131072
capabilities: [tool_calling, reasoning, vision]
supported_parameters: [include_reasoning, max_tokens, reasoning, response_format, temperature, tool_choice, tools, top_k, top_p]
architecture:
  input_modalities: [image, text, video]
  output_modalities: [text]
  tokenizer: Other
open_weights: false
license: proprietary
release_date: "2026-04-01"
pricing:
  input: 1.2
  output: 4
  cache_read: 0.24
benchmarks:
  intelligence_index: 23.5
  omniscience_index: -19.3
  humanitys_last_exam: 17.1
  gpqa_diamond: 80.9
  terminal_bench_hard: 32.6
  long_context_reasoning: 70.3
  ifbench: 61.1
  tau2_bench: 98.5
  mmmu_pro: 72.8
benchmark_variant: GLM 5V Turbo (Reasoning)
sources:
  - https://openrouter.ai/z-ai/glm-5v-turbo
  - https://openrouter.ai/api/v1/models
  - https://artificialanalysis.ai/models/glm-5v-turbo
  - https://docs.z.ai/guides/vlm/glm-5v-turbo
  - https://github.com/BerriAI/litellm/blob/main/model_prices_and_context_window.json
retrieved: "2026-10-14"
---

# GLM 5V Turbo

## Overview
GLM-5V-Turbo was released in April 2026 and is Z.ai's first multimodal coding foundation model. It is available through Z.ai's API, not as open weights. It accepts images, video, files and text and returns text, with a 200K-token context window and 128K max output. Z.ai says it uses a new CogViT vision encoder and an MTP architecture, and that it is tuned to work with agents such as Claude Code and OpenClaw. Z.ai lists multiple thinking modes, function calling, streaming and context caching.

## Strengths
- Artificial Analysis rates GLM 5V Turbo (Reasoning) above average on its Intelligence Index (score 23, marked as estimated, against a median of 12).
- Vision tasks tied to code: recreating front-ends from mockups, finding layout bugs from screenshots, exploring websites and GUIs.
- Z.ai reports that adding vision did not reduce its text-only coding results on CC-Bench-V2.

## Limitations
- Closed weights. Cannot be self-hosted.
- Artificial Analysis publishes no speed or latency figures for it.
- Lower Artificial Analysis Intelligence Index than the text-only GLM-5-Turbo.
- Z.ai has since released GLM-5.3-Flash, a newer open-weight multimodal model.

## Good for
- Design-to-code and front-end reproduction from images.
- Debugging rendering problems from screenshots.
- GUI and browser agents that need to read pages, charts and layouts.
