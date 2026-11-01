---
id: z-ai/glm-4.6v-flash
name: GLM-4.6V-Flash
owned_by: z-ai
type: llm
description: GLM-4.6V-Flash is the 9B open-weight (MIT) member of Z.ai's GLM-4.6V vision-language series, with native multimodal function calling, switchable thinking and a 128K-token context, free on Z.ai's API.
aliases: [glm-4.6v-flash, GLM-4.6V-FlashX, zai-org/GLM-4.6V-Flash]
context_length: 131072
capabilities: [tool_calling, reasoning, vision]
architecture:
  input_modalities: [text, image, video, file]
  output_modalities: [text]
open_weights: true
license: MIT
release_date: "2025-12-08"
sources:
  - https://huggingface.co/zai-org/GLM-4.6V-Flash
  - https://huggingface.co/api/models/zai-org/GLM-4.6V-Flash
  - https://huggingface.co/zai-org/GLM-4.6V-Flash/raw/main/config.json
  - https://docs.z.ai/guides/vlm/glm-4.6v
  - https://docs.z.ai/guides/overview/pricing
  - https://docs.bigmodel.cn/cn/guide/models/free/glm-4.6v-flash
  - https://docs.bigmodel.cn/cn/guide/models/vlm/glm-4.6v
  - https://docs.bigmodel.cn/cn/update/new-releases
  - https://openrouter.ai/api/v1/models
retrieved: "2026-11-01"
---

# GLM-4.6V-Flash

## Overview
GLM-4.6V-Flash launched with the GLM-4.6V series on 2025-12-08. It is the lightweight 9B model for local deployment and low latency, beside the 106B GLM-4.6V. It takes video, images, text and files, has a 128K context (131,072 positions in config.json) and can switch thinking on or off. GLM-4.6V is the first GLM vision series with native function calling: images and screenshots can be passed as tool arguments, and visual tool results feed back into reasoning. On Z.ai's API, `glm-4.6v-flash` is free and GLM-4.6V-FlashX, which Zhipu labels the lightweight high-speed 9B version, costs $0.04 input, $0.004 cached input and $0.4 output per million tokens. OpenRouter lists only the 106B GLM-4.6V. Weights are on Hugging Face as `zai-org/GLM-4.6V-Flash` under MIT.

## Strengths
- Zhipu says the 9B GLM-4.6V-Flash beats Qwen3-VL-8B overall on its multimodal benchmark set.
- Interleaved image-text content generation, document and chart understanding, and screenshot-to-HTML front-end replication.
- Long multimodal inputs: Z.ai says 128K covers about 150 document pages, 200 slides or an hour of video.
- Runs on SGLang 0.5.6.post1 or later, or vLLM 0.12.0 or later with transformers 5.

## Limitations
- Z.ai says pure-text question answering still has significant room for improvement.
- It may overthink, repeat itself or restate the answer at the end.
- Counting and identifying specific people remain weak.
- Artificial Analysis does not test it.

## Good for
- Free or self-hosted multimodal agents that pass screenshots to tools.
- Document, slide and video question answering on a single machine.
- Front-end replication from screenshots.
