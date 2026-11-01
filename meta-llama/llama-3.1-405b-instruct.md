---
id: meta-llama/llama-3.1-405b-instruct
name: Llama 3.1 405B Instruct
owned_by: meta
type: llm
description: Llama 3.1 405B Instruct is the largest model in Meta's July 2024 Llama 3.1 family, an open-weight, text-only 405B dense model for multilingual dialogue and tool use.
aliases: [meta-llama/Llama-3.1-405B-Instruct, meta-llama/Meta-Llama-3.1-405B-Instruct, meta-llama/Llama-3.1-405B-Instruct-FP8, "llama3.1:405b", "meta.llama3-1-405b-instruct-v1:0", meta/llama-3.1-405b-instruct-maas]
context_length: 128000
capabilities: [tool_calling]
architecture:
  input_modalities: [text]
  output_modalities: [text]
open_weights: true
license: Llama 3.1 Community License
release_date: "2024-07-23"
knowledge_cutoff: "2023-12"
benchmarks:
  gpqa_diamond: 51.5
  humanitys_last_exam: 4.0
  ifbench: 39.0
  long_context_reasoning: 25.3
  tau2_bench: 19.0
  terminal_bench_hard: 6.8
benchmark_variant: Llama 3.1 Instruct 405B
sources:
  - https://huggingface.co/meta-llama/Llama-3.1-405B-Instruct
  - https://huggingface.co/api/models/meta-llama/Llama-3.1-405B-Instruct
  - https://huggingface.co/api/models?author=meta-llama
  - https://artificialanalysis.ai/models/llama-3-1-instruct-405b
  - https://dev.meta.ai/llama/docs/model-cards-and-prompt-formats/llama3_1
  - https://dev.meta.ai/llama/docs/model-cards-and-prompt-formats/llama3_2
  - https://docs.aws.amazon.com/bedrock/latest/userguide/model-lifecycle-legacy.html
  - https://ollama.com/library/llama3.1
  - https://github.com/BerriAI/litellm/blob/main/model_prices_and_context_window.json
  - https://openrouter.ai/api/v1/models
retrieved: "2026-11-01"
---

# Llama 3.1 405B Instruct

## Overview
Llama 3.1 405B Instruct is the flagship of Meta's Llama 3.1 family, released on July 23, 2024 (405.9B BF16 parameters per Hugging Face). OpenRouter does not list it; the id follows the Hugging Face repo `meta-llama/Llama-3.1-405B-Instruct` (the older name `Meta-Llama-3.1-405B-Instruct` redirects to it), and Meta also ships an FP8 checkpoint. It is a dense, text-only transformer with grouped-query attention, pretrained on about 15 trillion tokens with a December 2023 cutoff and tuned for dialogue in eight languages. Meta gives a 128k context window; Artificial Analysis lists 128,000 tokens. The Llama 3.1 Community License allows using its outputs to improve other models, including synthetic data generation and distillation. Lifecycle: Amazon Bedrock retired `meta.llama3-1-405b-instruct-v1:0` on 2026-07-07.

## Strengths
- Meta's results: 87.3 MMLU, 88.6 IFEval, 50.7 GPQA, 89.0 HumanEval, 73.8 MATH, 88.5 BFCL and 91.6 multilingual MGSM.
- Tool use with custom JSON functions and the built-in Brave Search, Wolfram Alpha and code-interpreter tools; Meta recommends the 70B or 405B when conversation and tool calls are mixed.
- Ahead of the Llama 3.1 8B and 70B on Artificial Analysis (Llama 3.1 Instruct 405B): 51.5% on GPQA Diamond, 39% on IFBench and 25.3% on long-context reasoning.

## Limitations
- Heavy to self-host: the Ollama `llama3.1:405b` package alone is 243 GB.
- Weak against current models: 4% on Humanity's Last Exam, 19% on tau2-bench and 6.8% on Terminal-Bench Hard, with no Intelligence Index.
- No image input, no reasoning mode, and knowledge stops at December 2023.
- Fewer hosted options now that OpenRouter does not list it and Bedrock has retired it.

## Good for
- Self-hosted deployments that need the largest dense Llama 3.1 model.
- Synthetic data generation and distillation into smaller models.
- Multilingual tool-calling assistants on existing Llama 3.1 infrastructure.
