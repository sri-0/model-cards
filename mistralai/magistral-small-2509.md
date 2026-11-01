---
id: mistralai/magistral-small-2509
name: Magistral Small 1.2
owned_by: mistralai
type: llm
description: Magistral Small 1.2 is Mistral AI's 24B open-weight (Apache-2.0) multimodal reasoning model of September 2025, built on Mistral Small 3.2 with reasoning distilled from Magistral Medium.
aliases: [mistralai/Magistral-Small-2509, magistral-small-latest, mistral/magistral-small-latest, mistral.magistral-small-2509, mistralai/Magistral-Small-2509-GGUF, magistral-small-2507, magistral-small-2506]
context_length: 131072
capabilities: [tool_calling, reasoning, vision]
architecture:
  input_modalities: [text, image]
  output_modalities: [text]
open_weights: true
license: Apache-2.0
release_date: "2025-09-18"
benchmarks:
  gpqa_diamond: 66.3
  humanitys_last_exam: 6.4
  ifbench: 44.4
  long_context_reasoning: 19.3
  mmmu_pro: 55.5
  output_tokens_per_second: 105.9
  tau2_bench: 27.8
  terminal_bench_hard: 4.5
  time_to_first_token_seconds: 1.12
benchmark_variant: Magistral Small 1.2
sources:
  - https://huggingface.co/mistralai/Magistral-Small-2509
  - https://huggingface.co/api/models/mistralai/Magistral-Small-2509
  - https://huggingface.co/mistralai/Magistral-Small-2509/raw/main/config.json
  - https://huggingface.co/mistralai/Magistral-Small-2509/raw/main/README.md
  - https://docs.mistral.ai/getting-started/models
  - https://docs.mistral.ai/models/magistral-small-1-2-25-09
  - https://docs.mistral.ai/models/magistral-small-1-1-25-07
  - https://docs.mistral.ai/models/magistral-small-1-0-25-06
  - https://docs.mistral.ai/resources/changelogs
  - https://artificialanalysis.ai/models/magistral-small-2509
  - https://mistral.ai/news/magistral
  - https://openrouter.ai/api/v1/models
  - https://raw.githubusercontent.com/BerriAI/litellm/main/model_prices_and_context_window.json
retrieved: "2026-11-01"
---

# Magistral Small 1.2

## Overview
Magistral Small 1.2 (API id magistral-small-2509, alias magistral-small-latest) was released on 18 September 2025 per Mistral's model page (17 September in the changelog). OpenRouter does not list it; the id follows the Hugging Face repo mistralai/Magistral-Small-2509. It has 24.0B parameters (BF16), fine-tuned from Mistral Small 3.2 24B Instruct 2506 with supervised training on Magistral Medium traces and reinforcement learning, and adds a vision encoder over the text-only 1.0 and 1.1 releases. config.json sets 131,072 positions; Mistral says quality may degrade past 40k tokens. Reasoning sits between [THINK] and [/THINK] tokens; Mistral recommends its system prompt, temperature 0.7 and top_p 0.95. Mistral's API deprecated it on 30 April 2026 and retired it on 31 July 2026 in favour of Mistral Small 4. The retired ids magistral-small-2506 and magistral-small-2507 (1.0 and 1.1, retired 30 November 2025) are aliases so lookups resolve here, although those are older text-only models.

## Strengths
- Mistral reports 86.14% on AIME24, 77.34% on AIME25, 70.07% on GPQA Diamond and 70.88% on LiveCodeBench v5, well above 1.1.
- Artificial Analysis measured 66.3% on GPQA Diamond and 44.4% on IFBench, at 105.9 output tokens per second and 1.12 s to first token; it lists $0.50 input and $1.50 output per million tokens.
- Apache 2.0 weights; Mistral says it fits one RTX 4090 or a 32 GB MacBook once quantised. It runs in vLLM (mistral_common 1.8.5 or later), transformers, LM Studio and llama.cpp, with official GGUF files.

## Limitations
- Low scores on Terminal-Bench Hard (4.5%) and AA-LCR long-context reasoning (19.3%).
- Mistral's API no longer serves it; self-hosting only.
- Mistral recommends max_tokens of 131,072, so reasoning runs can be long.

## Good for
- Local maths, science and code reasoning on a single consumer GPU.
- Multilingual reasoning where the trace must be inspectable.
- Fine-tuning a small reasoning model under a permissive licence.
