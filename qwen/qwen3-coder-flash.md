---
id: qwen/qwen3-coder-flash
name: Qwen3 Coder Flash
owned_by: qwen
type: llm
description: Qwen3 Coder Flash is Alibaba Cloud's hosted, closed-weight fast tier of its Qwen3 Coder Plus coding-agent model, served with a 1,000,000-token context and now listed as legacy by Model Studio.
aliases: [qwen3-coder-flash, qwen3-coder-flash-2025-07-28]
context_length: 1000000
max_output_tokens: 65536
capabilities: [tool_calling]
supported_parameters: [frequency_penalty, logprobs, max_tokens, presence_penalty, response_format, seed, stop, temperature, tool_choice, tools, top_k, top_logprobs, top_p]
architecture:
  input_modalities: [text]
  output_modalities: [text]
  tokenizer: Qwen3
open_weights: false
license: proprietary
knowledge_cutoff: "2025-06"
pricing:
  input: 0.195
  output: 0.975
  cache_read: 0.039
  cache_write: 0.24375
sources:
  - https://openrouter.ai/qwen/qwen3-coder-flash
  - https://openrouter.ai/api/v1/models
  - https://www.alibabacloud.com/help/en/model-studio/text-generation-model
  - https://qwenlm.github.io/blog/qwen3-coder/
retrieved: "2026-10-16"
---

# Qwen3 Coder Flash

## Overview
Qwen3 Coder Flash is an API-only model from Alibaba Cloud Model Studio, relayed by OpenRouter; no weights are published. OpenRouter describes it as the fast, cost-efficient version of Alibaba's proprietary Qwen3 Coder Plus, a coding-agent model built for autonomous programming through tool calling and environment interaction, and lists a 1,000,000-token context, 65,536 output tokens and a June 2025 knowledge cutoff; its OpenRouter page was created on 2025-09-17. Model Studio's text generation page lists qwen3-coder-flash with the snapshot qwen3-coder-flash-2025-07-28 under Qwen3-Coder in its legacy section, with a 1M context and support for thinking mode, function calling and structured output but not built-in tools. The Qwen3-Coder blog uses qwen3-coder-plus as the hosted id for the open 480B model's API; Model Studio does not say which open model Flash corresponds to, so none is claimed here. No vendor release date was found and Artificial Analysis publishes no figures. The Qwen3.5 to Qwen3.8 Flash models, which have their own cards, are newer.

## Strengths
- 1,000,000-token context for whole-repository prompts.
- Tool calling through OpenRouter with prompt caching at 0.039 USD per million cached tokens read.
- Low list price at 0.195 USD input and 0.975 USD output per million tokens.
- Qwen Code, Claude Code and Cline integrations documented for the Qwen3-Coder family.

## Limitations
- Closed weights; no self-hosting.
- Model Studio lists it as legacy and no longer recommends it for new work.
- OpenRouter exposes no structured-output or reasoning parameter, although Model Studio says thinking mode is supported.
- No independent benchmark results on this card.

## Good for
- Cheap autonomous coding agents on Alibaba Cloud or OpenRouter.
- Large-codebase tasks that need the 1M context.
- Pinning the dated snapshot for reproducible behaviour.
