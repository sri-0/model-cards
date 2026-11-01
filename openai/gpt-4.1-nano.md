---
id: openai/gpt-4.1-nano
name: GPT-4.1 Nano
owned_by: openai
type: llm
description: GPT-4.1 nano is the fastest and cheapest model of OpenAI's GPT-4.1 series, shut down on OpenAI's API on 2026-10-23 but still listed by OpenRouter.
aliases: [gpt-4.1-nano, gpt-4.1-nano-2025-04-14, "openai/gpt-4.1-nano:batch", azure/gpt-4.1-nano, azure/gpt-4.1-nano-2025-04-14]
context_length: 1047576
max_output_tokens: 942818
capabilities: [tool_calling, vision, structured_output]
supported_parameters: [max_completion_tokens, response_format, seed, structured_outputs, temperature, tool_choice, tools, top_p]
architecture:
  input_modalities: [image, text, file]
  output_modalities: [text]
  tokenizer: GPT
open_weights: false
license: proprietary
release_date: "2025-04-14"
knowledge_cutoff: "2024-06"
pricing:
  input: 0.1
  output: 0.4
  cache_read: 0.03
benchmarks:
  coding_index: 11.1
  gpqa_diamond: 51.2
  humanitys_last_exam: 3.8
  ifbench: 32.0
  long_context_reasoning: 20.3
  mmmu_pro: 40.1
  output_tokens_per_second: 277.5
  tau2_bench: 17.3
  terminal_bench_hard: 3.8
  time_to_first_token_seconds: 1.46
benchmark_variant: GPT-4.1 nano
sources:
  - https://openrouter.ai/openai/gpt-4.1-nano
  - https://openrouter.ai/api/v1/models
  - https://artificialanalysis.ai/models/gpt-4-1-nano
  - https://developers.openai.com/api/docs/models/gpt-4.1-nano
  - https://developers.openai.com/api/docs/deprecations
  - https://learn.microsoft.com/en-us/azure/ai-foundry/openai/concepts/models
  - https://raw.githubusercontent.com/BerriAI/litellm/main/model_prices_and_context_window.json
retrieved: "2026-11-01"
---

# GPT-4.1 Nano

## Overview
GPT-4.1 nano is the fastest and cheapest model of OpenAI's GPT-4.1 series, released on 2025-04-14 (Artificial Analysis date; pinned snapshot `gpt-4.1-nano-2025-04-14`). It takes text and images and returns text, with a 1,047,576-token context window and a June 2024 knowledge cutoff. OpenAI documents 32,768 max output tokens; OpenRouter reports 942,818, the value the frontmatter carries. OpenAI served it on Chat Completions, Responses, Batch and Fine-tuning, with function calling, structured outputs, predicted outputs, prompt caching and image input, and no reasoning step. OpenAI lists it as Shut down: announced 2026-04-22, it left the API on 2026-10-23 with `gpt-5.6-luna` as the substitute. Its model page suggests GPT-5 nano, and Artificial Analysis lists GPT-5 nano as its successor. Azure's model list still includes version 2025-04-14. OpenRouter still listed it on 2026-11-01 at $0.10 input and $0.40 output per million tokens, with cache reads at $0.03 (OpenAI charged $0.025).

## Strengths
- The fastest GPT-4.1 model: Artificial Analysis measured about 278 output tokens per second, against about 165 for GPT-4.1.
- The cheapest of the series, with a Coding Index of 11.1 reported through OpenRouter.
- 51.2% on GPQA Diamond and 40.1% on MMMU-Pro.

## Limitations
- Shut down on OpenAI's own API; only third-party listings remain.
- Weak long-context reasoning (20.3% on AA-LCR) and tool use (17.3% on tau2-bench, 3.8% on Terminal-Bench Hard).
- 1.46-second time to first token, slower than GPT-4.1 and GPT-4.1 mini.
- Knowledge stops at June 2024.

## Good for
- Classification and routing where cost per call matters most.
- Simple extraction over long inputs.
- Batch jobs through providers that still serve it.
