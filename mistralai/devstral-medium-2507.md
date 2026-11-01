---
id: mistralai/devstral-medium-2507
name: Devstral Medium
owned_by: mistralai
type: llm
description: Devstral Medium is Mistral AI's proprietary, API-only agentic coding model of July 2025, built with All Hands AI and retired from Mistral's API in May 2026 in favour of Mistral Medium 3.5.
aliases: [devstral-medium-2507]
context_length: 128000
capabilities: [tool_calling, structured_output]
architecture:
  input_modalities: [text]
  output_modalities: [text]
open_weights: false
license: proprietary
release_date: "2025-07-10"
benchmarks:
  gpqa_diamond: 49.2
  humanitys_last_exam: 3.8
  ifbench: 29.9
  long_context_reasoning: 32.0
  tau2_bench: 19.9
  terminal_bench_hard: 9.1
benchmark_variant: Devstral Medium
sources:
  - https://docs.mistral.ai/getting-started/models
  - https://docs.mistral.ai/models/devstral-medium-1-0-25-07
  - https://docs.mistral.ai/resources/changelogs
  - https://artificialanalysis.ai/models/devstral-medium
  - https://mistral.ai/news/devstral-2507
  - https://mistral.ai/news/devstral-2-vibe-cli
  - https://openrouter.ai/api/v1/models
  - https://raw.githubusercontent.com/BerriAI/litellm/main/model_prices_and_context_window.json
retrieved: "2026-11-01"
---

# Devstral Medium

## Overview
Devstral Medium (version 25.07, API id devstral-medium-2507) was announced on 10 July 2025 together with Devstral Small 1.1, both built in collaboration with All Hands AI. OpenRouter does not list it and Mistral publishes no weights, so the id is the vendor API id under the vendor prefix. Mistral's model page lists it as Premier with a 128k context, text input, structured outputs, function calling, document QnA, prefix completion and batching; Artificial Analysis records 256,000 tokens instead, and this card follows Mistral. It was deprecated on 27 February 2026 and retired on 31 May 2026, with Mistral Medium 3.5 as Mistral's replacement (Artificial Analysis points to Devstral 2). Mistral's Devstral 2 announcement shows the alias devstral-medium-latest against Devstral 2, so that alias is not listed here.

## Strengths
- Mistral reports 61.6% on SWE-bench Verified, above Gemini 2.5 Pro and GPT-4.1 at a quarter of the price per the announcement.
- Priced at launch at $0.40 input and $2.00 output per million tokens, the same as Mistral Medium 3.
- Mistral offered on-premise deployment and custom fine-tuning for enterprises.

## Limitations
- Retired from Mistral's API with no self-hosting option for the public.
- Artificial Analysis (variant Devstral Medium) measured 9.1% on Terminal-Bench Hard, 19.9% on tau2-bench and 49.2% on GPQA Diamond, with no Intelligence Index, speed or price.
- Text only, no reasoning mode, and no published parameter count or knowledge cutoff.

## Good for
- Interpreting past results and cost figures from devstral-medium-2507 deployments.
- Migration planning: Mistral names Mistral Medium 3.5 as the successor.
