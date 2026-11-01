---
id: openai/gpt-5-image
name: GPT-5 Image
owned_by: openai
type: image
description: GPT-5 Image is OpenRouter's pairing of OpenAI's GPT-5 reasoning model with GPT Image 1 image generation, returning text and images from one chat request.
context_length: 400000
max_output_tokens: 128000
capabilities: [reasoning, vision, structured_output]
supported_parameters: [include_reasoning, logprobs, max_tokens, reasoning, response_format, seed, structured_outputs, temperature, top_logprobs, top_p, verbosity]
architecture:
  input_modalities: [image, text, file]
  output_modalities: [image, text]
  tokenizer: GPT
open_weights: false
license: proprietary
pricing:
  input: 10
  output: 10
  cache_read: 1.25
sources:
  - https://openrouter.ai/openai/gpt-5-image
  - https://openrouter.ai/api/v1/models
  - https://openrouter.ai/api/v1/models?output_modalities=image
  - https://developers.openai.com/api/docs/models
  - https://developers.openai.com/api/docs/guides/image-generation
  - https://developers.openai.com/api/docs/deprecations
  - https://artificialanalysis.ai/image/leaderboard/text-to-image
retrieved: "2026-11-01"
---

# GPT-5 Image

## Overview
OpenRouter lists GPT-5 Image as openai/gpt-5-image (added 2025-10-14) and describes it as OpenAI's GPT-5 combined with image generation, bringing GPT-5's reasoning and code quality together with GPT Image 1's instruction following, text rendering and detailed image editing. OpenAI's own model docs have no gpt-5-image id; OpenAI offers image generation to gpt-5 and newer models as a tool in the Responses API. On OpenRouter it accepts text, images and files, returns text and images, and has a 400,000-token context window with up to 128,000 output tokens. Reasoning is mandatory. It is served on OpenRouter's chat completions, completions, messages, responses and images endpoints. Pricing is $10 per million input tokens, $10 per million text output tokens, $1.25 per million cached input tokens and $40 per million image output tokens.

## Strengths
- Text answers and generated or edited images in the same conversation turn.
- Structured outputs, logprobs and seed support (OpenRouter).
- A 400,000-token context window for long multi-turn sessions.

## Limitations
- No Artificial Analysis rating of its own. OpenRouter says it uses GPT Image 1, which AA rates at Elo 1013 for GPT Image 1 (high) on AA-Image-T2I v2.1 (read 2026-11-01), against 1222 for the leader, GPT Image 2.5 Sunburst (max).
- OpenAI shut gpt-image-1 down on its own API on 2026-10-23.
- Image output at $40 per million tokens is the main cost; text input is eight times GPT-5's own rate on OpenRouter's GPT-5 listing.
- Mandatory reasoning adds latency and tokens to every request.

## Good for
- Chat applications that must answer and illustrate in one call through OpenRouter.
- Iterative image editing driven by a reasoning model.
