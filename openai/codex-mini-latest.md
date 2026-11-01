---
id: openai/codex-mini-latest
name: codex-mini-latest
owned_by: openai
type: llm
description: codex-mini-latest was a fine-tuned version of o4-mini built for the Codex CLI, launched in OpenAI's API in May 2025 and shut down on 12 February 2026.
aliases: [codex-mini-latest, azure/codex-mini, azure_ai/codex-mini]
context_length: 200000
max_output_tokens: 100000
capabilities: [tool_calling, reasoning, vision, structured_output]
architecture:
  input_modalities: [text, image]
  output_modalities: [text]
open_weights: false
license: proprietary
release_date: "2025-05-15"
knowledge_cutoff: "2024-06"
sources:
  - https://developers.openai.com/api/docs/models/codex-mini-latest
  - https://developers.openai.com/api/docs/models/all
  - https://developers.openai.com/api/docs/changelog
  - https://developers.openai.com/api/docs/deprecations
  - https://learn.microsoft.com/en-us/azure/foundry/openai/concepts/model-retirement-schedule
  - https://openrouter.ai/api/v1/models
  - https://raw.githubusercontent.com/BerriAI/litellm/main/model_prices_and_context_window.json
retrieved: "2026-11-01"
---

# codex-mini-latest

## Overview
Shut down: OpenAI notified users on 17 November 2025 and removed `codex-mini-latest` from the API on 12 February 2026, recommending `gpt-5-codex-mini`. The legacy local shell tool, which only this model could use, was retired with it. OpenRouter does not list it; the id is OpenAI's API id. OpenAI launched it in the API on 15 May 2025 for the Codex CLI and describes it as a fine-tuned version of o4-mini; for direct API use OpenAI recommended starting with GPT-4.1. The model page gives a 200,000-token context window, 100,000 max output tokens, a June 2024 knowledge cutoff, reasoning tokens, text and image input, function calling, structured outputs, prompt caching and the Responses API only. OpenAI priced it at 1.50 USD input, 0.375 cached input and 6 USD output per million tokens. Microsoft Foundry lists `codex-mini` version 2025-05-16 as deprecated, with retirement on 15 November 2026 and no replacement named.

## Strengths
- Tuned for Codex CLI coding sessions on top of o4-mini's reasoning.
- Large output budget of 100,000 tokens for long patches.
- Image input, so screenshots could accompany a coding task.

## Limitations
- Shut down on OpenAI's API; only Azure still lists a deployment, until 15 November 2026.
- Priced above o4-mini (1.10 and 4.40 USD) for the same base model.
- OpenAI's docs no longer have a page for its named replacement, `gpt-5-codex-mini`.
- No Artificial Analysis results. Closed weights.

## Good for
- Recognising the id in older Codex CLI configurations.
- Azure deployments that still run `codex-mini` before its November 2026 retirement.
