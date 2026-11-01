---
id: mistralai/mistral-small-3.1-24b-instruct
name: Mistral Small 3.1 24B
owned_by: mistralai
type: llm
description: Mistral Small 3.1 is a 24B Apache-2.0 open-weight model from Mistral AI that adds image input and a 128K context window to Mistral Small 3, released in March 2025.
aliases: [mistral-small-2503, mistralai/Mistral-Small-3.1-24B-Instruct-2503, "@cf/mistralai/mistral-small-3.1-24b-instruct", vertex_ai/mistral-small-2503, "mistral-small-2503@001", azure_ai/mistral-small-2503, watsonx/mistralai/mistral-small-3-1-24b-instruct-2503, "mistral-small3.1:24b"]
context_length: 128000
max_output_tokens: 102400
capabilities: [tool_calling, vision, structured_output]
supported_parameters: [frequency_penalty, logit_bias, logprobs, max_tokens, min_p, presence_penalty, repetition_penalty, seed, stop, structured_outputs, temperature, tool_choice, tools, top_k, top_logprobs, top_p]
architecture:
  input_modalities: [text, image]
  output_modalities: [text]
  tokenizer: Mistral
open_weights: true
license: Apache-2.0
release_date: "2025-03-17"
knowledge_cutoff: "2023-10"
pricing:
  input: 0.351
  output: 0.555
benchmarks:
  gpqa_diamond: 45.4
  humanitys_last_exam: 4.3
  ifbench: 29.9
  long_context_reasoning: 22.3
  output_tokens_per_second: 43.9
  scicode: 27.8
  tau2_bench: 25.1
  terminal_bench_4: 0
  terminal_bench_hard: 7.6
  time_to_first_token_seconds: 1.02
benchmark_variant: Mistral Small 3.1
sources:
  - https://openrouter.ai/mistralai/mistral-small-3.1-24b-instruct
  - https://openrouter.ai/api/v1/models
  - https://openrouter.ai/api/v1/models/mistralai/mistral-small-3.1-24b-instruct/endpoints
  - https://artificialanalysis.ai/models/mistral-small-3-1
  - https://docs.mistral.ai/getting-started/models
  - https://docs.mistral.ai/models/mistral-small-3-1-25-03
  - https://docs.mistral.ai/getting-started/changelog
  - https://mistral.ai/news/mistral-small-3-1
  - https://huggingface.co/mistralai/Mistral-Small-3.1-24B-Instruct-2503
  - https://huggingface.co/api/models/mistralai/Mistral-Small-3.1-24B-Instruct-2503
  - https://huggingface.co/mistralai/Mistral-Small-3.1-24B-Instruct-2503/raw/main/config.json
  - https://ollama.com/library/mistral-small3.1
  - https://github.com/BerriAI/litellm/blob/main/model_prices_and_context_window.json
retrieved: "2026-11-01"
---

# Mistral Small 3.1 24B

## Overview
Mistral Small 3.1 (API id mistral-small-2503, version 25.03) was released on 2025-03-17. It builds on Mistral Small 3 (2501) with a vision encoder and a context window extended to 128K tokens (131,072 positions in config.json) at the same 24B size, fine-tuned from Mistral-Small-3.1-24B-Base-2503 under Apache 2.0. Mistral lists two dozen languages from English and French to Arabic, Hindi, Bengali and Vietnamese, says it runs at 150 tokens per second, and says it fits a single RTX 4090 or a Mac with 32 GB of RAM once quantised. The Hugging Face card reports 80.62% on MMLU, 45.96% on GPQA Diamond, 88.41% on HumanEval, 94.08% on DocVQA and 81.20% on RULER at 128K. Mistral's docs list it as deprecated on 2025-11-06 and retired on 2025-11-30, replaced by Mistral Small 4; Mistral Small 3.2 (June 2025) is the direct successor. OpenRouter's only endpoint at retrieval was Cloudflare at $0.351 input and $0.555 output per million tokens.

## Strengths
- Image input, document and chart question answering, and 128K context on a 24B model.
- Native function calling and JSON output; Artificial Analysis (Mistral Small 3.1) measured 43.9 output tokens per second and 1.02 s to first token.
- Artificial Analysis: 45.4% on GPQA Diamond and 22.3% on AA-LCR, up from 0% for Mistral Small 3.
- Permissive licence with base weights for fine-tuning.

## Limitations
- Weak agent and instruction-following results: 25.1% on tau2-bench, 29.9% on IFBench, 7.6% on Terminal-Bench Hard and 0% on Terminal-Bench 4.0.
- Knowledge base dated 2023-10-01 in Mistral's recommended system prompt. No reasoning mode.
- Retired from Mistral's API; OpenRouter's single endpoint does not expose response_format.

## Good for
- Self-hosted assistants that need image understanding on one GPU.
- Long-document question answering under a permissive licence.
- Fine-tuning for domain tasks.
