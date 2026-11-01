---
id: openai/computer-use-preview
name: computer-use-preview
owned_by: openai
type: llm
description: computer-use-preview was OpenAI's specialised model for the Responses API computer use tool, released in March 2025 and shut down on 23 July 2026.
aliases: [computer-use-preview, computer-use-preview-2025-03-11, azure/computer-use-preview]
context_length: 8192
max_output_tokens: 1024
capabilities: [tool_calling, reasoning, vision]
architecture:
  input_modalities: [text, image]
  output_modalities: [text]
open_weights: false
license: proprietary
release_date: "2025-03-11"
knowledge_cutoff: "2023-10"
sources:
  - https://developers.openai.com/api/docs/models/computer-use-preview
  - https://developers.openai.com/api/docs/models/all
  - https://developers.openai.com/api/docs/changelog
  - https://developers.openai.com/api/docs/deprecations
  - https://developers.openai.com/api/docs/guides/tools-computer-use
  - https://developers.openai.com/api/docs/guides/tools-computer-use-integration
  - https://openrouter.ai/api/v1/models
  - https://raw.githubusercontent.com/BerriAI/litellm/main/model_prices_and_context_window.json
retrieved: "2026-11-01"
---

# computer-use-preview

## Overview
Shut down: OpenAI announced the deprecation on 22 April 2026 and shut `computer-use-preview` and its only snapshot, `computer-use-preview-2025-03-11`, down on 23 July 2026, naming `gpt-5.6-terra` as the substitute. OpenRouter does not list it; the id is OpenAI's API id. OpenAI announced it on 11 March 2025 with the Responses API, its built-in tools and the Agents SDK. It is a specialised model trained to understand and carry out computer tasks through the `computer_use_preview` tool, usable only in the Responses API and Batch. It took text and screenshots, returned text, with each step's action in a `computer_call`, and had an 8,192-token context window, 1,024 max output tokens, reasoning tokens, function calling and an October 2023 knowledge cutoff. OpenAI priced it at 3 USD input and 12 USD output per million tokens. OpenAI's deprecation policy names it as an example of a preview model that can be retired at short notice.

## Strengths
- Purpose-trained for screenshot-driven browser and desktop control.
- Function calling alongside the computer tool.

## Limitations
- Shut down; requests to the id fail.
- Very small context (8,192 tokens) and output limit (1,024 tokens).
- One `action` per `computer_call` and `truncation: "auto"` required, unlike the GA `computer` tool, which batches an `actions[]` array.
- No Artificial Analysis results. Knowledge stops at October 2023.

## Good for
- Recognising the id in older computer-use agents.
- Migration work: OpenAI's integration guide maps it to `gpt-6.1-sol` with `tools: [{ type: "computer" }]`.
