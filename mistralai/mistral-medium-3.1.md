---
id: mistralai/mistral-medium-3.1
name: Mistral Medium 3.1
owned_by: mistralai
type: llm
description: Mistral Medium 3.1 (mistral-medium-2508) is the August 2025 update of Mistral AI's proprietary mid-size multimodal model, with the same 128K context window and price as Mistral Medium 3 and a Mistral retirement date of 2026-08-31.
aliases: [mistral-medium-2508]
context_length: 131072
max_output_tokens: 104857
capabilities: [tool_calling, vision, structured_output]
supported_parameters: [frequency_penalty, max_tokens, presence_penalty, response_format, seed, stop, structured_outputs, temperature, tool_choice, tools, top_p]
architecture:
  input_modalities: [text, image, file]
  output_modalities: [text]
  tokenizer: Mistral
open_weights: false
license: proprietary
release_date: "2025-08-12"
knowledge_cutoff: "2025-06"
pricing:
  input: 0.4
  output: 2
  cache_read: 0.04
benchmarks:
  coding_index: 20.5
  agentic_index: 1.9
  gpqa_diamond: 58.8
  humanitys_last_exam: 4.7
  ifbench: 39.8
  long_context_reasoning: 42.7
  mmmu_pro: 54.2
  scicode: 32.4
  tau2_bench: 40.6
  terminal_bench_4: 0
  terminal_bench_hard: 10.6
benchmark_variant: Mistral Medium 3.1
sources:
  - https://openrouter.ai/mistralai/mistral-medium-3.1
  - https://openrouter.ai/api/v1/models
  - https://openrouter.ai/api/v1/models/mistralai/mistral-medium-3.1/endpoints
  - https://artificialanalysis.ai/models/mistral-medium-3-1
  - https://docs.mistral.ai/getting-started/models
  - https://docs.mistral.ai/models/mistral-medium-3-1-25-08
  - https://docs.mistral.ai/getting-started/changelog
  - https://mistral.ai/news/mistral-medium-3
retrieved: "2026-11-01"
---

# Mistral Medium 3.1

## Overview
Mistral Medium 3.1 (API id mistral-medium-2508, version 25.08) was released on 2025-08-12 as an update to Mistral Medium 3 with, in Mistral's words, improvements to tone and performance. It keeps the 128K context window, text and image input, and the $0.40 input and $2 output per million tokens price. The weights are not public. The API supports function calling, structured outputs, document question answering, predicted outputs, batching and the agents and conversations endpoints with built-in tools. Mistral's docs give a deprecation date of 2026-05-22 and a retirement date of 2026-08-31 and name Mistral Medium 3.5 as the replacement, itself deprecated on 2026-10-31 in favour of Mistral Large 4. OpenRouter still listed it with Mistral as the only provider at retrieval, with a knowledge cutoff of June 2025.

## Strengths
- Artificial Analysis (Mistral Medium 3.1): 58.8% on GPQA Diamond, 54.2% on MMMU-Pro, 42.7% on AA-LCR and 40.6% on tau2-bench, each above Mistral Medium 3.
- Coding Index 20.5 in OpenRouter's Artificial Analysis field.
- Same low price as Mistral Medium 3, with $0.04 cached input.

## Limitations
- Past its retirement date on Mistral's API, and proprietary.
- Agentic Index 1.9; 0% on Terminal-Bench 4.0 and 10.6% on Terminal-Bench Hard.
- No reasoning mode. Artificial Analysis published no speed or latency figures at retrieval.
- Mistral has not described the 3.1 changes beyond tone and performance.

## Good for
- Existing integrations pinned to mistral-medium-2508 through OpenRouter.
- Long-document and image question answering at low cost where retirement is acceptable.
- A baseline when evaluating Mistral Medium 3.5 or Mistral Large 4 as the replacement.
