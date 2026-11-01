---
id: mistralai/mistral-saba
name: Mistral Saba
owned_by: mistralai
type: llm
description: Mistral Saba is a proprietary 24B model from Mistral AI trained on Middle East and South Asian data for Arabic and Indian-origin languages, released in February 2025 and retired from Mistral's API in September 2025.
aliases: [mistral-saba-2502, mistral-saba-latest, mistralai/mistral-saba-2502, mistral-saba-24b]
context_length: 32768
max_output_tokens: 26214
capabilities: [tool_calling, structured_output]
supported_parameters: [frequency_penalty, max_tokens, presence_penalty, response_format, seed, stop, structured_outputs, temperature, tool_choice, tools, top_p]
architecture:
  input_modalities: [text, file]
  output_modalities: [text]
  tokenizer: Mistral
open_weights: false
license: proprietary
release_date: "2025-02-17"
knowledge_cutoff: "2024-09"
pricing:
  input: 0.2
  output: 0.6
  cache_read: 0.02
benchmarks:
  gpqa_diamond: 42.4
  humanitys_last_exam: 4.3
benchmark_variant: Mistral Saba
sources:
  - https://openrouter.ai/mistralai/mistral-saba
  - https://openrouter.ai/api/v1/models
  - https://openrouter.ai/api/v1/models/mistralai/mistral-saba/endpoints
  - https://artificialanalysis.ai/models/mistral-saba
  - https://docs.mistral.ai/getting-started/models
  - https://docs.mistral.ai/models/mistral-saba-25-02
  - https://docs.mistral.ai/getting-started/changelog
  - https://mistral.ai/news/mistral-saba
  - https://github.com/BerriAI/litellm/blob/main/model_prices_and_context_window.json
retrieved: "2026-11-01"
---

# Mistral Saba

## Overview
Mistral Saba (API id mistral-saba-2502, alias mistral-saba-latest, version 25.02) was released on 2025-02-17. Mistral's docs describe it as a fine-tuned Small model trained on curated datasets from across the Middle East and South Asia: a 24B model with a 32K context window that supports Arabic and many Indian-origin languages, and is particularly strong in South Indian-origin languages such as Tamil. Mistral says it answers at over 150 tokens per second and gives more accurate and relevant responses than models over five times its size; its benchmark results are published only as images. The weights are not public; Mistral offered local deployment within customer premises on single-GPU systems. Mistral's docs list it as deprecated on 2025-06-10 and retired on 2025-09-30, with Mistral Small 4 as the replacement. OpenRouter still listed it with Mistral as the only provider at retrieval, under the canonical slug mistralai/mistral-saba-2502. OpenRouter gives a knowledge cutoff of September 2024.

## Strengths
- Regional language coverage: Arabic and Indian-origin languages, per Mistral.
- Low price on OpenRouter: $0.20 input, $0.60 output and $0.02 cached input per million tokens.
- Function calling and structured outputs on a 24B model.

## Limitations
- Retired from Mistral's API and proprietary; local deployment was offered only through Mistral.
- Artificial Analysis (Mistral Saba): 42.4% on GPQA Diamond and 4.3% on Humanity's Last Exam.
- 32K context, text only, no reasoning mode.
- Mistral's benchmark figures are not published as text.

## Good for
- Existing Arabic, Tamil and other South Asian language deployments still routed through OpenRouter.
- A baseline when evaluating Mistral Small 4 for the same languages.
