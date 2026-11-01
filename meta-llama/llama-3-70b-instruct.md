---
id: meta-llama/llama-3-70b-instruct
name: Llama 3 70B Instruct
owned_by: meta
type: llm
description: Llama 3 70B Instruct is Meta's April 2024 open-weight, English-focused 70B chat model with an 8k context, since superseded by Llama 3.1 70B and Llama 3.3 70B.
aliases: [meta-llama/Meta-Llama-3-70B-Instruct, "llama3:70b", "llama3:70b-instruct", "meta.llama3-70b-instruct-v1:0", meta/llama3-70b-instruct-maas]
context_length: 8192
architecture:
  input_modalities: [text]
  output_modalities: [text]
open_weights: true
license: Llama 3 Community License
release_date: "2024-04-18"
knowledge_cutoff: "2023-12"
benchmarks:
  gpqa_diamond: 37.9
  humanitys_last_exam: 4.5
  ifbench: 37.1
  long_context_reasoning: 0
  tau2_bench: 0
  terminal_bench_hard: 0.8
benchmark_variant: Llama 3 Instruct 70B
sources:
  - https://huggingface.co/meta-llama/Meta-Llama-3-70B-Instruct
  - https://huggingface.co/api/models/meta-llama/Meta-Llama-3-70B-Instruct
  - https://artificialanalysis.ai/models/llama-3-instruct-70b
  - https://dev.meta.ai/llama/docs/model-cards-and-prompt-formats/meta-llama-3
  - https://dev.meta.ai/llama/docs/model-cards-and-prompt-formats
  - https://docs.aws.amazon.com/bedrock/latest/userguide/model-lifecycle-legacy.html
  - https://ollama.com/library/llama3
  - https://github.com/BerriAI/litellm/blob/main/model_prices_and_context_window.json
  - https://openrouter.ai/api/v1/models
retrieved: "2026-11-01"
---

# Llama 3 70B Instruct

## Overview
Lifecycle: superseded. Artificial Analysis marks it deprecated in favour of Llama 3.1 70B Instruct (itself now replaced by Llama 3.3 70B), OpenRouter no longer lists it, Amazon Bedrock moved `meta.llama3-70b-instruct-v1:0` to Legacy on 2026-09-30 with end-of-life on 2027-03-30, and LiteLLM records Azure AI retiring it on 2025-06-30 and Together AI's Turbo version on 2025-12-23. The weights remain on Hugging Face (`meta-llama/Meta-Llama-3-70B-Instruct`) and in Ollama (`llama3:70b`). Meta released Llama 3 on April 18, 2024. The 70B instruct model is a dense transformer with grouped-query attention, pretrained on more than 15 trillion tokens with a December 2023 knowledge cutoff and tuned with SFT and RLHF for English dialogue. It has an 8k context window (Artificial Analysis lists 8,192 tokens) and is released under the Llama 3 Community License.

## Strengths
- Meta's results: 82.0 MMLU, 39.5 GPQA, 81.7 HumanEval, 93.0 GSM-8K and 50.4 MATH, against 52.9, 21.0, 25.6, 57.5 and 11.6 for Llama 2 70B Chat.
- Artificial Analysis (Llama 3 Instruct 70B): 37.1% on IFBench and 37.9% on GPQA Diamond, ahead of the 8B.
- Easy to upgrade: Meta says prompt-format changes for Llama 3.1 are handled in the tokenizer configuration, so the newer model is a drop-in replacement.

## Limitations
- Short 8k context; Artificial Analysis scores it 0 on long-context reasoning and tau2-bench.
- 4.5% on Humanity's Last Exam and 0.8% on Terminal-Bench Hard.
- English only, no documented tool calling, no image input.
- Heavy to self-host for its capability; Ollama's `llama3:70b` package is 40 GB.

## Good for
- Existing Llama 3 deployments until they move to Llama 3.3 70B.
- English chat, summarisation and drafting within an 8k window.
- Reproducing results that were built on Llama 3 70B.
