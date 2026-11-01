---
id: meta-llama/llama-3.1-70b-instruct
name: Llama 3.1 70B Instruct
owned_by: meta
type: llm
description: Llama 3.1 70B Instruct is Meta's open-weight, text-only 70B instruction-tuned model for multilingual dialogue, released in July 2024 and since superseded by Llama 3.3 70B.
aliases: [meta-llama/Llama-3.1-70B-Instruct, meta-llama/Meta-Llama-3.1-70B-Instruct, "llama3.1:70b", "meta.llama3-1-70b-instruct-v1:0", meta/llama-3.1-70b-instruct-maas]
context_length: 131072
max_output_tokens: 16384
capabilities: [tool_calling, structured_output]
supported_parameters: [frequency_penalty, logit_bias, max_tokens, min_p, presence_penalty, repetition_penalty, response_format, seed, stop, structured_outputs, temperature, tool_choice, tools, top_k, top_p]
architecture:
  input_modalities: [text]
  output_modalities: [text]
  tokenizer: Llama3
  instruct_type: llama3
open_weights: true
license: Llama 3.1 Community License
release_date: "2024-07-23"
knowledge_cutoff: "2023-12"
pricing:
  input: 0.4
  output: 0.4
benchmarks:
  gpqa_diamond: 40.9
  humanitys_last_exam: 4.5
  ifbench: 34.4
  output_tokens_per_second: 40.4
  tau2_bench: 15.2
  terminal_bench_hard: 3.0
  time_to_first_token_seconds: 2.11
benchmark_variant: Llama 3.1 Instruct 70B
sources:
  - https://openrouter.ai/meta-llama/llama-3.1-70b-instruct
  - https://openrouter.ai/api/v1/models
  - https://artificialanalysis.ai/models/llama-3-1-instruct-70b
  - https://huggingface.co/meta-llama/Llama-3.1-70B-Instruct
  - https://huggingface.co/api/models/meta-llama/Llama-3.1-70B-Instruct
  - https://dev.meta.ai/llama/docs/model-cards-and-prompt-formats/llama3_1
  - https://dev.meta.ai/llama/docs/model-cards-and-prompt-formats/llama3_2
  - https://docs.aws.amazon.com/bedrock/latest/userguide/model-lifecycle-legacy.html
  - https://ollama.com/library/llama3.1
  - https://github.com/BerriAI/litellm/blob/main/model_prices_and_context_window.json
retrieved: "2026-11-01"
---

# Llama 3.1 70B Instruct

## Overview
Llama 3.1 70B Instruct is the middle size of Meta's Llama 3.1 family (8B, 70B and 405B), released on July 23, 2024. It is a dense, text-only transformer with grouped-query attention, tuned with supervised fine-tuning and RLHF for dialogue in English, German, French, Italian, Portuguese, Hindi, Spanish and Thai. Meta gives a 128k context window and a December 2023 knowledge cutoff; OpenRouter lists 131,072 tokens with up to 16,384 output tokens. The weights are under the Llama 3.1 Community License and Meta's Acceptable Use Policy. Lifecycle: OpenRouter lists an expiration date of 2026-11-03 for this id, Amazon Bedrock moved `meta.llama3-1-70b-instruct-v1:0` to Legacy on 2026-09-30 with end-of-life on 2027-03-30, and Artificial Analysis marks the model deprecated in favour of Llama 3.3 70B.

## Strengths
- Meta's own results: 83.6 MMLU, 87.5 IFEval, 84.8 BFCL and 86.9 multilingual MGSM.
- Tool use with custom JSON functions and the built-in Brave Search, Wolfram Alpha and code-interpreter tools. Meta recommends the 70B or 405B, not the 8B, when conversation and tool calls are mixed.
- Tool calling and structured outputs through OpenRouter providers at $0.40 per million input and output tokens.
- Widely packaged for local use (Ollama `llama3.1:70b`).

## Limitations
- Weak by current standards. Artificial Analysis (Llama 3.1 Instruct 70B) reports 40.9% on GPQA Diamond, 4.5% on Humanity's Last Exam, 34.4% on IFBench, 15.2% on tau2-bench and 3% on Terminal-Bench Hard, with no Intelligence Index.
- Slow on the provider AA measured: 40.4 output tokens per second and 2.11 s to first token.
- No image input, no reasoning mode, and knowledge stops at December 2023.

## Good for
- Existing deployments that have not yet moved to Llama 3.3 70B.
- Multilingual chat and summarisation in the eight supported languages.
- Self-hosted tool-calling agents where a 70B dense model already fits the hardware.
