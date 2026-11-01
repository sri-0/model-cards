---
id: mistralai/devstral-small-2-24b-instruct-2512
name: Devstral Small 2
owned_by: mistralai
type: llm
description: Devstral Small 2 is Mistral AI's 24B open-weight (Apache-2.0) agentic coding model with image input, released in December 2025 alongside Devstral 2 and the Vibe CLI.
aliases: [mistralai/Devstral-Small-2-24B-Instruct-2512, labs-devstral-small-2512, devstral-small-latest, mistral/devstral-small-latest, "devstral-small-2:24b"]
context_length: 262144
capabilities: [tool_calling, vision, structured_output]
architecture:
  input_modalities: [text, image]
  output_modalities: [text]
open_weights: true
license: Apache-2.0
release_date: "2025-12-09"
benchmarks:
  gpqa_diamond: 53.2
  humanitys_last_exam: 3.5
  ifbench: 31.2
  long_context_reasoning: 28.0
  mmmu_pro: 44.6
  scicode: 32.4
  tau2_bench: 23.4
  terminal_bench_4: 0
  terminal_bench_hard: 16.7
benchmark_variant: Devstral Small 2
sources:
  - https://huggingface.co/mistralai/Devstral-Small-2-24B-Instruct-2512
  - https://huggingface.co/api/models/mistralai/Devstral-Small-2-24B-Instruct-2512
  - https://huggingface.co/mistralai/Devstral-Small-2-24B-Instruct-2512/raw/main/config.json
  - https://huggingface.co/mistralai/Devstral-Small-2-24B-Instruct-2512/raw/main/README.md
  - https://docs.mistral.ai/getting-started/models
  - https://docs.mistral.ai/models/devstral-small-2-25-12
  - https://docs.mistral.ai/models/devstral-small-1-1-25-07
  - https://docs.mistral.ai/models/devstral-small-1-0-25-05
  - https://docs.mistral.ai/inference/labs
  - https://docs.mistral.ai/resources/changelogs
  - https://artificialanalysis.ai/models/devstral-small-2
  - https://mistral.ai/news/devstral-2-vibe-cli
  - https://mistral.ai/news/devstral-2507
  - https://ollama.com/library/devstral-small-2/tags
  - https://openrouter.ai/api/v1/models
  - https://raw.githubusercontent.com/BerriAI/litellm/main/model_prices_and_context_window.json
retrieved: "2026-11-01"
---

# Devstral Small 2

## Overview
Devstral Small 2 was released on 9 December 2025 with Devstral 2 and the Mistral Vibe CLI. OpenRouter does not list it; the id follows the Hugging Face repo mistralai/Devstral-Small-2-24B-Instruct-2512. On Mistral's API it was a Labs model, labs-devstral-small-2512 (alias devstral-small-latest), deprecated on 27 February 2026 and retired on 31 March 2026 with Mistral Medium 3.5 as the replacement. The published checkpoint is FP8 (24.0B parameters, 22.2B of them FP8), fine-tuned from Mistral Small 3.1 24B Base 2503 with the Ministral 3 architecture and Llama 4-style rope scaling; config.json allows 393,216 positions but Mistral documents a 256k context. Unlike Devstral Small 1.0 (devstral-small-2505, retired 30 November 2025) and 1.1 (devstral-small-2507, 53.6% SWE-bench Verified, retired 31 May 2026), it accepts images. Those earlier models have their own Hugging Face repos and Artificial Analysis pages and are not aliases of this card.

## Strengths
- Mistral reports 68.0% on SWE-bench Verified, 55.7% on SWE-bench Multilingual and 22.5% on Terminal Bench 2, and said the API price after the launch free period would be $0.10 input and $0.30 output per million tokens.
- Apache 2.0, and small enough for one RTX 4090 or a 32 GB Mac; vLLM, SGLang, transformers, llama.cpp, LM Studio and Ollama (devstral-small-2:24b) are documented.
- Works with Mistral Vibe, Cline, Kilo Code, Claude Code, OpenHands and SWE-agent scaffolds; Mistral recommends temperature 0.2.

## Limitations
- Artificial Analysis scores it 0% on Terminal-Bench 4.0 and 16.7% on Terminal-Bench Hard (variant Devstral Small 2) and publishes no Intelligence Index for it.
- Retired from Mistral's API; Labs models were never recommended for production.
- No reasoning mode.

## Good for
- Local coding agents on a single GPU.
- Multi-file edits and codebase exploration with tool calls.
- Fine-tuning a permissively licensed coding model.
