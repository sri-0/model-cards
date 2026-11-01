---
id: qwen/qwen3.5-plus-02-15
name: Qwen3.5 Plus 2026-02-15
owned_by: qwen
type: llm
description: "Qwen3.5 Plus (snapshot 2026-02-15) is Alibaba's hosted flagship Qwen3.5 vision-language mixture-of-experts model with a 1M-token context, the production version of the open Qwen3.5-397B-A17B and the snapshot the stable qwen3.5-plus id resolves to."
aliases: [qwen3.5-plus, qwen3.5-plus-2026-02-15]
context_length: 1000000
max_output_tokens: 65536
capabilities: [tool_calling, reasoning, vision, structured_output]
supported_parameters: [frequency_penalty, include_reasoning, logprobs, max_tokens, presence_penalty, reasoning, response_format, seed, stop, structured_outputs, temperature, tool_choice, tools, top_k, top_logprobs, top_p]
architecture:
  input_modalities: [text, image, video]
  output_modalities: [text]
  tokenizer: Qwen3
open_weights: false
license: proprietary
pricing:
  input: 0.26
  output: 1.56
sources:
  - https://openrouter.ai/qwen/qwen3.5-plus-02-15
  - https://openrouter.ai/api/v1/models
  - https://www.qwencloud.com/models/qwen3.5-plus
  - https://huggingface.co/Qwen/Qwen3.5-397B-A17B
  - https://www.alibabacloud.com/help/en/model-studio/model-pricing
  - https://www.alibabacloud.com/help/en/model-studio/text-generation-model
  - https://www.alibabacloud.com/help/en/model-studio/vision-model
retrieved: "2026-10-16"
---

# Qwen3.5 Plus 2026-02-15

## Overview
Qwen3.5 Plus is Alibaba's hosted flagship tier of the Qwen3.5 series, served through Alibaba Cloud Model Studio and Qwen Cloud without published weights; Qwen's Hugging Face card for Qwen3.5-397B-A17B names Qwen3.5 Plus as that model's hosted version with a 1M-token default context, built-in tools and adaptive tool use. This card is the older of the two snapshots OpenRouter serves; the newer qwen/qwen3.5-plus-20260420 improves agentic coding and speed, and both ids remain available. OpenRouter listed this id on 2026-02-16. Model Studio's pricing page says the stable `qwen3.5-plus` is currently equivalent to `qwen3.5-plus-2026-02-15`, and files the Qwen3.5 models as legacy. It takes text, image and video input on a hybrid linear-attention and sparse mixture-of-experts architecture, with thinking togglable per request. OpenRouter lists a 1,000,000-token context and 65,536-token output; Qwen Cloud gives 991K max input and 65K max output. OpenRouter charges $0.26 input and $1.56 output per million tokens up to 256,000 prompt tokens and $0.325 and $1.95 from there; Model Studio's International list price is $0.4 and $2.4 for the first 256K tokens.

## Strengths
- Qwen says the 3.5 series performs on par with state-of-the-art models and is a leap over Qwen3 in text and multimodal work.
- For the open Qwen3.5-397B-A17B it is based on, Qwen reports SWE-bench Verified 76.4, GPQA Diamond 88.4 and MMMU-Pro 79.0; the hosted snapshot is not benchmarked separately there.
- 1M context with built-in tools and adaptive tool use.

## Limitations
- Superseded by the 2026-04-20 snapshot and later Plus-class models; legacy on Model Studio.
- Artificial Analysis figures are not recorded in this card.
- Prompts of 256,000 tokens or more cost more on OpenRouter.

## Good for
- Integrations pinned to the original Qwen3.5 Plus behaviour.
- Multimodal agent and search tasks needing the 1M context.
