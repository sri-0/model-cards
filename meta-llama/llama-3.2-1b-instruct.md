---
id: meta-llama/llama-3.2-1b-instruct
name: Llama 3.2 1B Instruct
owned_by: meta
type: llm
description: Llama 3.2 1B Instruct is Meta's smallest open-weight Llama 3.2 text model, distilled from Llama 3.1 for on-device dialogue, rewriting and summarisation.
aliases: [meta-llama/Llama-3.2-1B-Instruct, meta-llama/Llama-3.2-1B-Instruct-SpinQuant_INT4_EO8, meta-llama/Llama-3.2-1B-Instruct-QLORA_INT4_EO8, "llama3.2:1b", "meta.llama3-2-1b-instruct-v1:0"]
context_length: 60000
max_output_tokens: 54000
supported_parameters: [frequency_penalty, logit_bias, max_tokens, min_p, presence_penalty, repetition_penalty, seed, stop, temperature, top_k, top_p]
architecture:
  input_modalities: [text]
  output_modalities: [text]
  tokenizer: Llama3
  instruct_type: llama3
open_weights: true
license: Llama 3.2 Community License
release_date: "2024-09-25"
knowledge_cutoff: "2023-12"
pricing:
  input: 0.027
  output: 0.201
benchmarks:
  gpqa_diamond: 19.6
  humanitys_last_exam: 5.5
  ifbench: 22.8
  long_context_reasoning: 6.7
  tau2_bench: 0
  terminal_bench_hard: 0
benchmark_variant: Llama 3.2 Instruct 1B
sources:
  - https://openrouter.ai/meta-llama/llama-3.2-1b-instruct
  - https://openrouter.ai/api/v1/models
  - https://artificialanalysis.ai/models/llama-3-2-instruct-1b
  - https://huggingface.co/meta-llama/Llama-3.2-1B-Instruct
  - https://huggingface.co/api/models/meta-llama/Llama-3.2-1B-Instruct
  - https://huggingface.co/api/models?author=meta-llama
  - https://dev.meta.ai/llama/docs/model-cards-and-prompt-formats/llama3_2
  - https://docs.aws.amazon.com/bedrock/latest/userguide/model-lifecycle-legacy.html
  - https://ollama.com/library/llama3.2
retrieved: "2026-11-01"
---

# Llama 3.2 1B Instruct

## Overview
Llama 3.2 1B Instruct (1.23B parameters) is the smallest text model in Meta's Llama 3.2 release of September 25, 2024. Meta pruned it and used logits from Llama 3.1 8B and 70B as token-level targets during pretraining on up to 9 trillion tokens, with a December 2023 data cutoff. It is tuned for multilingual dialogue, retrieval, summarisation and prompt rewriting in eight languages. Meta gives a 128k context window; OpenRouter's current endpoint serves 60,000 tokens with up to 54,000 output tokens. Meta also publishes 4-bit SpinQuant and QAT+LoRA versions for phones and edge devices, with an 8k context. Lifecycle: Amazon Bedrock retired `meta.llama3-2-1b-instruct-v1:0` on 2026-07-07, and Artificial Analysis marks the model deprecated.

## Strengths
- Very cheap on OpenRouter: $0.027 input and $0.201 output per million tokens.
- Built for devices. On a OnePlus 12 with ExecuTorch, Meta measured 50.2 tokens per second for SpinQuant against 19.2 for BF16, with a 1,083 MB file.
- Meta's BF16 results: 49.3 MMLU, 59.5 IFEval and 75.0 recall on multi-needle retrieval.
- Custom functions can be defined in the prompt (no built-in tools).

## Limitations
- Very low capability. Artificial Analysis (Llama 3.2 Instruct 1B) reports 19.6% on GPQA Diamond, 22.8% on IFBench, 6.7% on long-context reasoning and zero on tau2-bench and Terminal-Bench Hard.
- OpenRouter lists no tool calling or structured outputs for this id.
- Text only, and knowledge stops at December 2023.

## Good for
- On-device assistants, short summaries and text rewriting.
- Cheap query rewriting, tagging and routing.
- Edge deployments with tight memory or power budgets.
