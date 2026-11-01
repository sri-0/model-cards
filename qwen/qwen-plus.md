---
id: qwen/qwen-plus
name: Qwen-Plus
owned_by: qwen
type: llm
description: Qwen-Plus is Alibaba Cloud Model Studio's hosted, closed-weight mid-tier Qwen text model, listed on OpenRouter with a 1,000,000-token context and now marked legacy by Model Studio.
aliases: [qwen-plus]
context_length: 1000000
max_output_tokens: 32768
capabilities: [tool_calling, structured_output]
supported_parameters: [frequency_penalty, logprobs, max_tokens, presence_penalty, response_format, seed, stop, structured_outputs, temperature, tool_choice, tools, top_k, top_logprobs, top_p]
architecture:
  input_modalities: [text]
  output_modalities: [text]
  tokenizer: Qwen
open_weights: false
license: proprietary
knowledge_cutoff: "2025-03"
pricing:
  input: 0.26
  output: 0.78
  cache_read: 0.052
  cache_write: 0.325
sources:
  - https://openrouter.ai/qwen/qwen-plus
  - https://openrouter.ai/api/v1/models
  - https://www.alibabacloud.com/help/en/model-studio/text-generation-model
retrieved: "2026-10-16"
---

# Qwen-Plus

## Overview
Qwen-Plus is an API-only model served by Alibaba Cloud Model Studio (DashScope id qwen-plus) and relayed by OpenRouter; no weights are published. OpenRouter's description calls it a 131K-context model based on the Qwen2.5 foundation model, while its listing gives a 1,000,000-token context, 32,768 output tokens and a March 2025 knowledge cutoff; the frontmatter follows the listing. Model Studio's text generation page lists "qwen-plus and its snapshots" under Legacy Qwen, a section it describes as no longer recommended, with a 1M context and support for thinking mode, function calling, built-in tools and structured output. The page does not name the snapshots, so none are recorded here. No vendor release date was found and Artificial Analysis publishes no figures for it. Qwen3.5-Plus, Qwen3.6-Plus and Qwen3.7-Plus, which have their own cards, are its successors.

## Strengths
- Tool calling, structured outputs, logprobs and seed through OpenRouter.
- 1,000,000-token context on OpenRouter and Model Studio.
- Prompt caching on OpenRouter at 0.052 USD per million cached input tokens read.
- Low list price at 0.26 USD input and 0.78 USD output per million tokens.

## Limitations
- Closed weights; available only through Alibaba Cloud or OpenRouter.
- Model Studio lists it as legacy, so new work should target the Qwen3.5 or later Plus models.
- OpenRouter exposes no reasoning parameter even though Model Studio says thinking mode is supported.
- No independent benchmark results on this card, and the sources disagree on the context length (131K in the description, 1M in the listing).

## Good for
- Existing Model Studio integrations pinned to qwen-plus.
- Long-document summarisation and extraction at low cost.
- Text-only assistants that need cached prompts.
