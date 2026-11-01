---
id: openai/gpt-5.4-image-2
name: GPT-5.4 Image 2
owned_by: openai
type: image
description: GPT-5.4 Image 2 is OpenRouter's pairing of OpenAI's GPT-5.4 with GPT Image 2 image generation, moving between reasoning, coding and image output in one chat request.
aliases: [openai/gpt-5.4-image-2-20260421]
context_length: 272000
max_output_tokens: 128000
capabilities: [reasoning, vision, structured_output]
supported_parameters: [include_reasoning, logprobs, max_tokens, reasoning, reasoning_effort, response_format, seed, structured_outputs, top_logprobs, verbosity]
architecture:
  input_modalities: [image, text, file]
  output_modalities: [image, text]
  tokenizer: GPT
open_weights: false
license: proprietary
pricing:
  input: 8
  output: 15
  cache_read: 2
sources:
  - https://openrouter.ai/openai/gpt-5.4-image-2
  - https://openrouter.ai/api/v1/models
  - https://openrouter.ai/api/v1/models?output_modalities=image
  - https://developers.openai.com/api/docs/models
  - https://developers.openai.com/api/docs/models/gpt-image-2
  - https://developers.openai.com/api/docs/guides/image-generation
  - https://artificialanalysis.ai/image/leaderboard/text-to-image
  - https://artificialanalysis.ai/image/leaderboard/editing
retrieved: "2026-11-01"
---

# GPT-5.4 Image 2

## Overview
OpenRouter lists GPT-5.4 Image 2 as openai/gpt-5.4-image-2 (canonical slug openai/gpt-5.4-image-2-20260421, added 2026-04-21) and describes it as OpenAI's GPT-5.4 combined with image generation from GPT Image 2, letting users move between reasoning, coding and visual generation in one interaction. OpenAI's own model docs have no such id; they list GPT Image 2 (snapshot gpt-image-2-2026-04-21) as a separate image model and offer image generation to gpt-5 and newer models as a Responses API tool. On OpenRouter it accepts text, images and files, returns text and images, and has a 272,000-token context window with up to 128,000 output tokens. Reasoning is optional and off by default, with efforts none, low, medium (default), high and xhigh. It is served on OpenRouter's chat completions, completions, messages, responses and images endpoints. Pricing is $8 per million input tokens, $15 per million text output tokens, $2 per million cached input tokens and $30 per million image output tokens.

## Strengths
- Built on a current image model: Artificial Analysis (read 2026-11-01) rates GPT Image 2 (high) at Elo 1186 on AA-Image-T2I v2.1 (rank 3) and 1136 on AA-Image-Editing v2.1. These are GPT Image 2's scores, not this pairing's.
- Configurable reasoning effort, including none for fast replies.
- Structured outputs, logprobs and seed support.

## Limitations
- No Artificial Analysis rating of its own.
- Behind GPT Image 2.5 Sunburst (max) and Flare (max), at 1222 and 1207 on the same text-to-image board.
- Text input costs more than OpenRouter's GPT-5.4 rate ($8 against $2.50 per million tokens).
- Smaller context than GPT-5 Image (272,000 against 400,000 tokens).

## Good for
- Agents that reason or write code and also generate or edit images.
- Image work through OpenRouter that needs GPT Image 2 quality inside a chat flow.
