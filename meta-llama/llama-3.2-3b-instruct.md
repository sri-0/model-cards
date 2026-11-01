---
id: meta-llama/llama-3.2-3b-instruct
name: Llama 3.2 3B Instruct
owned_by: meta
type: llm
description: Llama 3.2 3B Instruct is Meta's small open-weight Llama 3.2 text model, distilled from Llama 3.1 for on-device dialogue, tool calling and summarisation.
aliases: [meta-llama/Llama-3.2-3B-Instruct, meta-llama/Llama-3.2-3B-Instruct-SpinQuant_INT4_EO8, meta-llama/Llama-3.2-3B-Instruct-QLORA_INT4_EO8, "llama3.2:3b", "meta.llama3-2-3b-instruct-v1:0"]
context_length: 131072
max_output_tokens: 117964
capabilities: [structured_output]
supported_parameters: [frequency_penalty, logit_bias, logprobs, max_tokens, min_p, presence_penalty, repetition_penalty, seed, stop, structured_outputs, temperature, top_k, top_logprobs, top_p]
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
  input: 0.05
  output: 0.33
benchmarks:
  gpqa_diamond: 25.5
  humanitys_last_exam: 5.3
  ifbench: 26.2
  long_context_reasoning: 4.3
  tau2_bench: 21.1
benchmark_variant: Llama 3.2 Instruct 3B
sources:
  - https://openrouter.ai/meta-llama/llama-3.2-3b-instruct
  - https://openrouter.ai/api/v1/models
  - https://artificialanalysis.ai/models/llama-3-2-instruct-3b
  - https://huggingface.co/meta-llama/Llama-3.2-3B-Instruct
  - https://huggingface.co/api/models/meta-llama/Llama-3.2-3B-Instruct
  - https://huggingface.co/api/models?author=meta-llama
  - https://dev.meta.ai/llama/docs/model-cards-and-prompt-formats/llama3_2
  - https://docs.aws.amazon.com/bedrock/latest/userguide/model-lifecycle-legacy.html
  - https://ollama.com/library/llama3.2
retrieved: "2026-11-01"
---

# Llama 3.2 3B Instruct

## Overview
Llama 3.2 3B Instruct (3.21B parameters) is the larger of the two text models in Meta's Llama 3.2 release of September 25, 2024. Like the 1B, it was pruned and pretrained against logits from Llama 3.1 8B and 70B, on up to 9 trillion tokens with a December 2023 data cutoff. Meta tunes it for multilingual dialogue, knowledge retrieval, summarisation and prompt rewriting in eight languages, with a 128k context window; OpenRouter lists 131,072 tokens and up to 117,964 output tokens. Meta also publishes 4-bit SpinQuant and QAT+LoRA versions for devices, with an 8k context. Lifecycle: Amazon Bedrock retired `meta.llama3-2-3b-instruct-v1:0` on 2026-07-07, and Artificial Analysis marks the model deprecated.

## Strengths
- Cheap on OpenRouter: $0.05 input and $0.33 output per million tokens, with structured outputs.
- Meta's BF16 results: 63.4 MMLU, 77.4 IFEval, 77.7 GSM8K, 67.0 BFCL V2 and 84.7 recall on multi-needle retrieval.
- Custom function calling defined in the system or user prompt.
- Runs on phones. On a OnePlus 12 with ExecuTorch, Meta measured 19.7 tokens per second for SpinQuant against 7.6 for BF16, with a 2,435 MB file.

## Limitations
- Low capability. Artificial Analysis (Llama 3.2 Instruct 3B) reports 25.5% on GPQA Diamond, 26.2% on IFBench, 21.1% on tau2-bench and 4.3% on long-context reasoning.
- No built-in tools (Brave Search, Wolfram Alpha), unlike the larger Llama 3.1 models, and OpenRouter lists no tool calling for this id.
- Text only, and knowledge stops at December 2023.

## Good for
- On-device assistants and writing helpers.
- Summaries, query rewriting and simple extraction at low cost.
- Small agents that call a few custom functions.
