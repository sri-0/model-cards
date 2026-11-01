---
id: z-ai/glm-4.5-flash
name: GLM-4.5-Flash
owned_by: z-ai
type: llm
description: GLM-4.5-Flash is the free API tier of Z.ai's GLM-4.5 series, a text model with switchable thinking, tool calling and a 128K-token context, now retired on Zhipu's China platform.
aliases: [glm-4.5-flash, zai/glm-4.5-flash]
capabilities: [tool_calling, reasoning, structured_output]
architecture:
  input_modalities: [text]
  output_modalities: [text]
sources:
  - https://docs.z.ai/guides/llm/glm-4.5
  - https://docs.z.ai/guides/overview/pricing
  - https://docs.bigmodel.cn/cn/guide/models/free/glm-4.5-flash
  - https://openrouter.ai/api/v1/models
  - https://raw.githubusercontent.com/BerriAI/litellm/main/model_prices_and_context_window.json
retrieved: "2026-11-01"
---

# GLM-4.5-Flash

## Overview
GLM-4.5-Flash is the free member of Z.ai's GLM-4.5 series, which also includes GLM-4.5, GLM-4.5-Air and their high-speed X versions. OpenRouter does not list it and there is no Hugging Face repository; the id is Z.ai's API id `glm-4.5-flash`. Zhipu documents a 128K-token context and 96K maximum output, text in and text out, with the same hybrid reasoning as GLM-4.5: `thinking.type` set to `enabled` or `disabled`, with dynamic thinking on by default. Neither Z.ai nor Zhipu states its parameter count or which checkpoint it serves. Zhipu's bigmodel.cn platform retired it on 2026-01-30 and now routes its requests to GLM-4.7-Flash; Z.ai's global pricing page still lists it as free.

## Strengths
- Free for input, cached input and output on Z.ai's API.
- Function calling, streaming, context caching, structured JSON output and MCP tools, per Zhipu's documentation.
- Zhipu says it is tuned for tool use, web browsing, software engineering and front-end work, and can drive Claude Code or Roo Code.

## Limitations
- No published benchmarks; Artificial Analysis does not test it.
- Text only.
- Retired on Zhipu's mainland China platform, where GLM-4.7-Flash replaced it; Z.ai's pricing page also lists GLM-4.7-Flash as free.

## Good for
- Prototyping and low-volume tools where cost matters more than guaranteed capacity.
- Existing integrations already pinned to `glm-4.5-flash`.
