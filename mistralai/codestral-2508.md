---
id: mistralai/codestral-2508
name: Codestral 2508
owned_by: mistralai
type: llm
description: Codestral 25.08 is Mistral AI's proprietary, API-only code model for low-latency completion tasks such as fill-in-the-middle.
aliases: [codestral-2508, mistral/codestral-2508]
context_length: 256000
max_output_tokens: 204800
capabilities: [tool_calling, structured_output]
supported_parameters: [frequency_penalty, max_tokens, prediction, presence_penalty, response_format, seed, stop, structured_outputs, temperature, tool_choice, tools, top_p]
architecture:
  input_modalities: [text, file]
  output_modalities: [text]
  tokenizer: Mistral
open_weights: false
license: proprietary
knowledge_cutoff: "2025-03"
pricing:
  input: 0.3
  output: 0.9
  cache_read: 0.03
sources:
  - https://openrouter.ai/mistralai/codestral-2508
  - https://openrouter.ai/api/v1/models
  - https://docs.mistral.ai/getting-started/models
  - https://github.com/BerriAI/litellm/blob/main/model_prices_and_context_window.json
retrieved: "2026-10-14"
---

# Codestral 2508

## Overview
Codestral 25.08 (API id codestral-2508) is listed on Mistral's models page as a Premier model, meaning it is served through Mistral's API and its weights are not published. Mistral describes it as its code completion model released at the end of July 2025. OpenRouter lists a 256,000-token context window, up to 204,800 output tokens, text input, tool calling and structured outputs, and a knowledge cutoff of March 2025. It replaces Codestral 25.01 (codestral-2501), which Mistral retired on 11/30/2025.

## Strengths
- Built for high-frequency, low-latency work: fill-in-the-middle (FIM), code correction and test generation.
- Long context for completing code with large surrounding files.
- Low price on OpenRouter: $0.30 input and $0.90 output per million tokens.

## Limitations
- Proprietary and API-only. It cannot be self-hosted, so it is not usable in an offline deployment without a provider.
- No Artificial Analysis data was available for this model at retrieval, so this card has no independent benchmark figures.
- Not a reasoning model and not positioned for long agentic coding runs. Mistral positions Mistral Medium 3.5 as its agentic coding model.

## Good for
- IDE autocomplete and fill-in-the-middle completion.
- Quick code fixes and refactors inside an editor.
- Generating unit tests for existing code.
