---
id: openai/o3-deep-research
name: o3-deep-research
owned_by: openai
type: llm
description: o3-deep-research was OpenAI's deep research variant of o3 for long, multi-step web and private-data research in the Responses API, released in June 2025 and shut down on 23 July 2026.
aliases: [o3-deep-research, o3-deep-research-2025-06-26, azure/o3-deep-research]
context_length: 200000
max_output_tokens: 100000
capabilities: [reasoning, vision]
architecture:
  input_modalities: [text, image]
  output_modalities: [text]
open_weights: false
license: proprietary
release_date: "2025-06-24"
knowledge_cutoff: "2024-06"
sources:
  - https://developers.openai.com/api/docs/models/o3-deep-research
  - https://developers.openai.com/api/docs/models/all
  - https://developers.openai.com/api/docs/guides/deep-research
  - https://developers.openai.com/api/docs/changelog
  - https://developers.openai.com/api/docs/deprecations
  - https://learn.microsoft.com/en-us/azure/foundry/openai/concepts/model-retirement-schedule
  - https://openrouter.ai/api/v1/models
  - https://raw.githubusercontent.com/BerriAI/litellm/main/model_prices_and_context_window.json
retrieved: "2026-11-01"
---

# o3-deep-research

## Overview
Shut down: OpenAI announced the deprecation on 22 April 2026 and shut `o3-deep-research` and its snapshot `o3-deep-research-2025-06-26` down on 23 July 2026, naming `gpt-5.6-sol` as the replacement. OpenRouter does not list it; the id is OpenAI's API id. OpenAI's changelog dates the release 24 June 2025, alongside o4-mini-deep-research. The deep research guide says it finds, analyses and synthesises hundreds of sources into an analyst-level report. A request must include at least one data source (web search, remote MCP servers, or file search over vector stores) and can add code interpreter. The model page gives a 200,000-token context window, 100,000 max output tokens, a June 2024 knowledge cutoff, reasoning tokens and text and image input, on Responses and Batch only. OpenAI priced it at 10 USD input, 2.50 cached input and 40 USD output per million tokens, plus tool-call fees. Microsoft Foundry still lists version 2025-06-26 as deprecated, retiring on 19 November 2026.

## Strengths
- OpenAI's most capable deep research model while it was offered.
- Combines web search, MCP connectors and file search in one research run, with every tool call listed in the output.

## Limitations
- Shut down on OpenAI's API; Azure retires it on 19 November 2026.
- Runs can take tens of minutes; OpenAI recommends background mode, which is not compatible with Zero Data Retention.
- No clarification or prompt-rewriting step in the API: it expects a fully formed prompt.
- No function calling listed, and no Artificial Analysis results.

## Good for
- Recognising the id in research agents built in 2025 and 2026.
- Azure deployments until November 2026, then migration to `gpt-5.6-sol`.
