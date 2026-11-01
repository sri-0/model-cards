---
id: openai/gpt-6-sol
name: GPT-6 Sol
owned_by: openai
type: llm
description: GPT-6 Sol is the cost-efficient high-end tier of OpenAI's GPT-6 family, released in September 2026 below the flagship GPT-6 Astra and above GPT-6 Luna, and since followed by GPT-6.1 Sol.
aliases: [gpt-6-sol, openai/gpt-6-sol-20260922, "openai/gpt-6-sol:batch", openai.gpt-6-sol, us.openai.gpt-6-sol, global.openai.gpt-6-sol, azure/gpt-6-sol, azure/gpt-6-sol-2026-09-22]
context_length: 1050000
max_output_tokens: 128000
capabilities: [tool_calling, reasoning, vision, structured_output]
supported_parameters: [include_reasoning, max_completion_tokens, max_tokens, reasoning, reasoning_effort, response_format, seed, structured_outputs, tool_choice, tools, verbosity]
architecture:
  input_modalities: [file, image, text]
  output_modalities: [text]
  tokenizer: GPT
open_weights: false
license: proprietary
release_date: "2026-09-22"
knowledge_cutoff: "2026-04"
pricing:
  input: 2
  output: 10
  cache_read: 0.2
  cache_write: 2.5
benchmarks:
  humanitys_last_exam: 47.9
  long_context_reasoning: 83.7
  mmmu_pro: 82.9
  output_tokens_per_second: 113.6
  scicode: 57.6
  terminal_bench_4: 43.9
  time_to_first_token_seconds: 100.86
benchmark_variant: GPT-6 Sol (Max)
sources:
  - https://openrouter.ai/openai/gpt-6-sol
  - https://openrouter.ai/api/v1/models
  - https://artificialanalysis.ai/models/gpt-6-sol
  - https://artificialanalysis.ai/models/gpt-6-sol-daybreak-blue
  - https://developers.openai.com/api/docs/models/gpt-6-sol
  - https://developers.openai.com/api/docs/models/gpt-daybreak-blue-latest
  - https://developers.openai.com/api/docs/guides/latest-model
  - https://developers.openai.com/api/docs/changelog
  - https://developers.openai.com/api/docs/deprecations
  - https://developers.openai.com/api/docs/pricing
  - https://docs.aws.amazon.com/bedrock/latest/userguide/model-card-openai-gpt-6-sol.html
  - https://learn.microsoft.com/en-us/azure/foundry/foundry-models/concepts/models-sold-directly-by-azure
  - https://raw.githubusercontent.com/BerriAI/litellm/main/model_prices_and_context_window.json
retrieved: "2026-11-01"
---

# GPT-6 Sol

## Overview
GPT-6 Sol was released on September 22, 2026 with GPT-6 Luna, below the flagship GPT-6 Astra. OpenAI built it for complex coding and agentic workflows; OpenRouter says it approaches Astra-level factual reliability at much lower cost. Its model page now points to GPT-6.1 Sol (September 29) as the newer Sol, and OpenAI's GPT-6 guide lists Astra, GPT-6.1 Sol, GPT-6.1 Terra and Luna. It takes text and image input and returns text, with a 1,050,000-token context window (922,000 input), 128,000 max output tokens and an April 20, 2026 knowledge cutoff. `reasoning.effort` supports none, low, medium (default), high, xhigh and max; pro mode is a Responses API setting (see GPT-6 Sol Pro). The only snapshot is `gpt-6-sol`; Foundry's version is 2026-09-22 and Bedrock's id `openai.gpt-6-sol`. OpenAI gives no retirement date and names it the replacement for GPT-5.1 and GPT-5.3-Codex; Artificial Analysis marks it deprecated in favour of GPT-6.1 Sol. AA's separate GPT-6 Sol (Daybreak Blue, max) entry has no results; Daybreak Blue is an approval-only programme for defensive security work, not a separate model.

## Strengths
- Artificial Analysis measured GPT-6 Sol (Max) at 43.9% on Terminal-Bench 4.0, 47.9% on Humanity's Last Exam and 83.7% on AA-LCR.
- About 114 output tokens per second at Max.
- 2 USD input and 10 USD output per million tokens, half GPT-5.6 Sol's price.

## Limitations
- Time to first token at Max was about 101 seconds.
- Chat Completions allows function calling only with effort none; use the Responses API for tools.
- An image-encoding bug that degraded image understanding was fixed on September 25, 2026.
- Prompts over 272,000 input tokens cost 4 and 15 USD per million. Closed weights.

## Good for
- Coding agents at a fifth of Astra's output price.
- Deployments pinned to GPT-6 Sol.
- Replacing GPT-5.1 or GPT-5.3-Codex before April 1, 2027.
