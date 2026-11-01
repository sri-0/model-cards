---
id: mistralai/magistral-medium-2509
name: Magistral Medium 1.2
owned_by: mistralai
type: llm
description: Magistral Medium 1.2 is Mistral AI's proprietary, API-only multimodal reasoning model of September 2025, retired from Mistral's API in July 2026 in favour of Mistral Medium 3.5.
aliases: [magistral-medium-2509, magistral-medium-latest, mistral/magistral-medium-latest, magistral-medium-2507, magistral-medium-2506]
context_length: 128000
capabilities: [tool_calling, reasoning, vision]
architecture:
  input_modalities: [text, image]
  output_modalities: [text]
open_weights: false
license: proprietary
release_date: "2025-09-18"
benchmarks:
  gpqa_diamond: 73.9
  humanitys_last_exam: 10.3
  ifbench: 43.0
  long_context_reasoning: 53.0
  mmmu_pro: 59.7
  tau2_bench: 52.0
  terminal_bench_hard: 12.9
benchmark_variant: Magistral Medium 1.2
sources:
  - https://docs.mistral.ai/getting-started/models
  - https://docs.mistral.ai/models/magistral-medium-1-2-25-09
  - https://docs.mistral.ai/models/magistral-medium-1-1-25-07
  - https://docs.mistral.ai/models/magistral-medium-1-0-25-06
  - https://docs.mistral.ai/resources/changelogs
  - https://artificialanalysis.ai/models/magistral-medium-2509
  - https://huggingface.co/mistralai/Magistral-Small-2509/raw/main/README.md
  - https://mistral.ai/news/magistral
  - https://openrouter.ai/api/v1/models
  - https://raw.githubusercontent.com/BerriAI/litellm/main/model_prices_and_context_window.json
retrieved: "2026-11-01"
---

# Magistral Medium 1.2

## Overview
Magistral Medium 1.2 (version 25.09, API id magistral-medium-2509, alias magistral-medium-latest) is the third release of Mistral's enterprise reasoning line. Mistral's model page dates it 18 September 2025 (the changelog says 17 September). OpenRouter does not list it and Mistral publishes no weights, so the id is the vendor API id under the vendor prefix. It is a Premier (API-only) model with a 128k context, image input, function calling, document QnA and batching. Mistral's models page lists it as deprecated on 22 May 2026 and retired on 31 July 2026, with Mistral Medium 3.5 as the replacement. The earlier ids magistral-medium-2506 (1.0, June 2025) and magistral-medium-2507 (1.1, July 2025) were text-only 40k-context releases retired on 30 November 2025; they are listed as aliases so lookups resolve here.

## Strengths
- Mistral reports 91.82% on AIME24, 83.48% on AIME25, 76.26% on GPQA Diamond and 75.00% on LiveCodeBench v5, against 72.03%, 60.99%, 71.46% and 59.35% for 1.1.
- Artificial Analysis (variant Magistral Medium 1.2) measured 73.9% on GPQA Diamond, 52.0% on tau2-bench and 53.0% on AA-LCR.
- Mistral says the reasoning trace is traceable and written in the user's language.

## Limitations
- Retired from Mistral's API; no weights to self-host.
- Artificial Analysis scores 12.9% on Terminal-Bench Hard and 10.3% on Humanity's Last Exam, and publishes no Intelligence Index, speed or price for it.
- No structured output in Mistral's feature list, and no published parameter count or knowledge cutoff.

## Good for
- Reading results from existing evaluations that used magistral-medium-2509.
- Migration planning: Mistral names Mistral Medium 3.5 as the successor.
