---
id: z-ai/glm-5.3-flashx
name: GLM 5.3 FlashX
owned_by: z-ai
type: llm
description: GLM-5.3-FlashX is the high-speed Z.ai API tier of GLM-5.3-Flash, a multimodal reasoning model with a 1M-token context window.
aliases: [glm-5.3-flashx]
context_length: 1048576
max_output_tokens: 131072
capabilities: [tool_calling, reasoning, vision]
supported_parameters: [include_reasoning, max_tokens, reasoning, reasoning_effort, response_format, temperature, tool_choice, tools, top_k, top_p]
architecture:
  input_modalities: [text, image, video]
  output_modalities: [text]
  tokenizer: Other
pricing:
  input: 0.37
  output: 1.25
  cache_read: 0.09
sources:
  - https://openrouter.ai/z-ai/glm-5.3-flashx
  - https://openrouter.ai/api/v1/models
  - https://docs.z.ai/guides/vlm/glm-5.3-flash
  - https://docs.z.ai/guides/overview/pricing
retrieved: "2026-10-14"
---

# GLM 5.3 FlashX

## Overview
GLM-5.3-FlashX is served by Z.ai under the model code `glm-5.3-flashx`. Z.ai and OpenRouter describe it as the high-speed variant of GLM-5.3-Flash, delivering up to 200 tokens per second. It shares GLM-5.3-Flash's hybrid sparse and linear attention architecture (320B total parameters, 18B active per OpenRouter). Inputs are text, images and video; output is text. Z.ai lists a 1M-token context window and 128K max output, with text parameters consistent with GLM-5.3. Thinking is always enabled.

## Strengths
- Faster output than the standard GLM-5.3-Flash endpoint, per Z.ai.
- Same multimodal coding and agent abilities as GLM-5.3-Flash: visual understanding, tool calling and long context.
- Low per-token price on OpenRouter (0.37 USD input and 1.25 USD output per million tokens).

## Limitations
- Open-weight status for this tier is not stated. The published weights are for GLM-5.3-Flash.
- No Artificial Analysis data exists for FlashX. See the GLM-5.3-Flash card for measured figures.
- Z.ai notes FlashX is not yet available on its GLM Coding Plan.
- Reasoning cannot be turned off.

## Good for
- Latency-sensitive coding assistants and agents that need GLM-5.3-Flash quality.
- Interactive visual coding and UI work.
- High-volume workloads where throughput matters.
