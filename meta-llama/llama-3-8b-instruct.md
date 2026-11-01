---
id: meta-llama/llama-3-8b-instruct
name: Llama 3 8B Instruct
owned_by: meta
type: llm
description: Llama 3 8B Instruct is Meta's April 2024 open-weight, English-focused 8B chat model with an 8k context, since superseded by Llama 3.1 8B Instruct.
aliases: [meta-llama/Meta-Llama-3-8B-Instruct, "llama3:8b", "meta.llama3-8b-instruct-v1:0", meta/llama3-8b-instruct-maas]
context_length: 8192
architecture:
  input_modalities: [text]
  output_modalities: [text]
open_weights: true
license: Llama 3 Community License
release_date: "2024-04-18"
knowledge_cutoff: "2023-03"
benchmarks:
  gpqa_diamond: 29.6
  humanitys_last_exam: 5.1
  ifbench: 24.6
  long_context_reasoning: 0
  tau2_bench: 0
  terminal_bench_hard: 0
benchmark_variant: Llama 3 Instruct 8B
sources:
  - https://huggingface.co/meta-llama/Meta-Llama-3-8B-Instruct
  - https://huggingface.co/api/models/meta-llama/Meta-Llama-3-8B-Instruct
  - https://artificialanalysis.ai/models/llama-3-instruct-8b
  - https://dev.meta.ai/llama/docs/model-cards-and-prompt-formats/meta-llama-3
  - https://dev.meta.ai/llama/docs/model-cards-and-prompt-formats
  - https://docs.aws.amazon.com/bedrock/latest/userguide/model-lifecycle-legacy.html
  - https://ollama.com/library/llama3
  - https://github.com/BerriAI/litellm/blob/main/model_prices_and_context_window.json
  - https://openrouter.ai/api/v1/models
retrieved: "2026-11-01"
---

# Llama 3 8B Instruct

## Overview
Lifecycle: superseded. Artificial Analysis marks it deprecated in favour of Llama 3.1 8B Instruct, OpenRouter no longer lists it, Amazon Bedrock moved `meta.llama3-8b-instruct-v1:0` to Legacy on 2026-09-30 with end-of-life on 2027-03-30, and LiteLLM records Together AI retiring it on 2025-08-28. The weights remain on Hugging Face (`meta-llama/Meta-Llama-3-8B-Instruct`) and in Ollama (`llama3:8b`). Meta released Llama 3 on April 18, 2024 in 8B and 70B sizes. This 8B instruct model is a dense transformer with grouped-query attention, pretrained on more than 15 trillion tokens with a March 2023 knowledge cutoff and tuned with SFT and RLHF for English dialogue. It has an 8k context window (Artificial Analysis lists 8,192 tokens) and is released under the Llama 3 Community License.

## Strengths
- Meta's results: 68.4 MMLU, 34.2 GPQA, 62.2 HumanEval, 79.6 GSM-8K and 30.0 MATH, well ahead of Llama 2 7B Chat.
- Small and cheap to run locally; Ollama's `llama3:8b` package is 4.7 GB.
- Easy to upgrade: Meta says prompt-format changes for Llama 3.1 are handled in the tokenizer configuration, so the newer model is a drop-in replacement.

## Limitations
- Short 8k context; Artificial Analysis scores it 0 on long-context reasoning.
- Weak by current standards: 29.6% on GPQA Diamond, 24.6% on IFBench and 0 on tau2-bench and Terminal-Bench Hard (Llama 3 Instruct 8B).
- English only, no documented tool calling, no image input, and knowledge stops at March 2023.

## Good for
- Existing deployments pinned to Llama 3 that cannot yet move to Llama 3.1.
- Small English chat and summarisation tasks on modest hardware.
- Reproducing results that were built on Llama 3 8B.
