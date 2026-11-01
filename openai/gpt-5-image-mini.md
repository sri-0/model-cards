---
id: openai/gpt-5-image-mini
name: GPT-5 Image Mini
owned_by: openai
type: image
description: GPT-5 Image Mini is OpenRouter's pairing of OpenAI's GPT-5 Mini with GPT Image 1 Mini, returning text and images from one chat request at lower cost than GPT-5 Image.
context_length: 400000
max_output_tokens: 128000
capabilities: [reasoning, vision, structured_output]
supported_parameters: [include_reasoning, logprobs, max_tokens, reasoning, response_format, seed, structured_outputs, temperature, top_logprobs, top_p, verbosity]
architecture:
  input_modalities: [file, image, text]
  output_modalities: [image, text]
  tokenizer: GPT
open_weights: false
license: proprietary
pricing:
  input: 2.5
  output: 2
  cache_read: 0.25
sources:
  - https://openrouter.ai/openai/gpt-5-image-mini
  - https://openrouter.ai/api/v1/models
  - https://openrouter.ai/api/v1/models?output_modalities=image
  - https://developers.openai.com/api/docs/models
  - https://developers.openai.com/api/docs/guides/image-generation
  - https://developers.openai.com/api/docs/deprecations
  - https://artificialanalysis.ai/image/leaderboard/text-to-image
retrieved: "2026-11-01"
---

# GPT-5 Image Mini

## Overview
OpenRouter lists GPT-5 Image Mini as openai/gpt-5-image-mini (added 2025-10-16) and describes it as GPT-5 Mini's language capabilities combined with GPT Image 1 Mini for efficient image generation: a natively multimodal model with instruction following, text rendering and detailed image editing at reduced latency and cost. OpenAI's own model docs have no gpt-5-image-mini id; OpenAI offers image generation to gpt-5 and newer models as a tool in the Responses API. On OpenRouter it accepts text, images and files, returns text and images, and has a 400,000-token context window with up to 128,000 output tokens. Reasoning is mandatory. It is served on OpenRouter's chat completions, completions, messages, responses and images endpoints. Pricing is $2.50 per million input tokens, $2 per million text output tokens, $0.25 per million cached input tokens and $8 per million image output tokens.

## Strengths
- Text and images in one turn at a fifth of GPT-5 Image's image output price ($8 against $40 per million tokens).
- Structured outputs, logprobs and seed support (OpenRouter).
- A 400,000-token context window.

## Limitations
- No Artificial Analysis rating of its own. OpenRouter says it uses GPT Image 1 Mini, which AA rates at Elo 936 for GPT Image 1 Mini (medium) on AA-Image-T2I v2.1 (read 2026-11-01), rank 71.
- OpenAI's deprecation page shuts gpt-image-1-mini down on its own API on 2026-12-01.
- Text input costs ten times OpenRouter's GPT-5 Mini rate ($2.50 against $0.25).
- Mandatory reasoning adds latency and tokens to every request.

## Good for
- Lower-cost chat applications that answer and illustrate in one call through OpenRouter.
- Quick image drafts alongside text answers.
