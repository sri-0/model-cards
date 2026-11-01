---
id: mistralai/mixtral-8x22b-instruct
name: Mixtral 8x22B Instruct
owned_by: mistralai
type: llm
description: Mixtral 8x22B Instruct is Mistral AI's Apache-2.0 sparse mixture-of-experts model with 141B total and 39B active parameters and a 64K context window, released in April 2024.
aliases: [open-mixtral-8x22b, open-mixtral-8x22b-2404, mistralai/Mixtral-8x22B-Instruct-v0.1, mixtral-8x22b-instruct, "mixtral:8x22b"]
context_length: 65536
max_output_tokens: 52428
capabilities: [tool_calling, structured_output]
supported_parameters: [frequency_penalty, max_tokens, presence_penalty, response_format, seed, stop, structured_outputs, temperature, tool_choice, tools, top_p]
architecture:
  input_modalities: [text, file]
  output_modalities: [text]
  tokenizer: Mistral
  instruct_type: mistral
open_weights: true
license: Apache-2.0
release_date: "2024-04-17"
knowledge_cutoff: "2024-01"
pricing:
  input: 2
  output: 6
  cache_read: 0.2
benchmarks:
  gpqa_diamond: 33.2
  humanitys_last_exam: 4.0
benchmark_variant: Mixtral 8x22B Instruct
sources:
  - https://openrouter.ai/mistralai/mixtral-8x22b-instruct
  - https://openrouter.ai/api/v1/models
  - https://openrouter.ai/api/v1/models/mistralai/mixtral-8x22b-instruct/endpoints
  - https://artificialanalysis.ai/models/mistral-8x22b-instruct
  - https://docs.mistral.ai/getting-started/models
  - https://docs.mistral.ai/models/mixtral-8x22b-0-1-0-3
  - https://docs.mistral.ai/getting-started/changelog
  - https://mistral.ai/news/mixtral-8x22b
  - https://huggingface.co/mistralai/Mixtral-8x22B-Instruct-v0.1
  - https://huggingface.co/api/models/mistralai/Mixtral-8x22B-Instruct-v0.1
  - https://huggingface.co/mistralai/Mixtral-8x22B-Instruct-v0.1/raw/main/config.json
  - https://ollama.com/library/mixtral
  - https://github.com/BerriAI/litellm/blob/main/model_prices_and_context_window.json
retrieved: "2026-11-01"
---

# Mixtral 8x22B Instruct

## Overview
Mixtral 8x22B Instruct (API id open-mixtral-8x22b, also open-mixtral-8x22b-2404) was released on 2024-04-17. It is a sparse mixture-of-experts model with eight experts and two active per token (config.json), 141B total and 39B active parameters, a 64K context window, and fluency in English, French, Italian, German and Spanish. It is fine-tuned from Mixtral-8x22B-v0.1 under Apache 2.0 and is natively capable of function calling with the v3 tokenizer. Mistral reports 90.8% on GSM8K (maj@8) and 44.6% on MATH (maj@4) for the instruct version. Mistral's docs give about 283 GB of GPU memory at bf16 and about 71 GB at fp4, and list the model as deprecated on 2024-11-30 and retired on 2025-03-30, with Mistral Small 4 as the replacement. Mistral's changelog notes that tool_call_id must not be null when using function calling with it. OpenRouter still listed it with Mistral as the only provider at retrieval, at $2 input and $6 output per million tokens.

## Strengths
- Mistral says its sparse activation makes it faster than any dense 70B model; only 39B parameters are active per token.
- Native function calling and JSON output under a permissive licence.
- Mistral says it outperforms Llama 2 70B on HellaSwag, Arc Challenge and MMLU in French, German, Spanish and Italian.

## Limitations
- Artificial Analysis (Mixtral 8x22B Instruct): 33.2% on GPQA Diamond and 4.0% on Humanity's Last Exam, well below current mid-size models.
- Retired from Mistral's API; OpenRouter's price is high for its results.
- 64K context, five languages, text only, no reasoning mode.
- All 141B parameters must be loaded, so it needs a multi-GPU node unquantised.

## Good for
- Existing self-hosted deployments with the memory to run it.
- Research on mixture-of-experts serving under Apache 2.0.
- Deployments pinned to open-mixtral-8x22b that have not yet moved to Mistral Small 4.
