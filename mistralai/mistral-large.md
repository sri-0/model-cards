---
id: mistralai/mistral-large
name: Mistral Large
owned_by: mistralai
type: llm
description: OpenRouter's Mistral Large listing, whose 128K window and November 2024 knowledge cutoff match Mistral Large 2.1 (mistral-large-2411), a dense 123B model released in November 2024 under the Mistral Research License.
aliases: [mistral-large-2411, mistralai/mistral-large-2411, mistralai/Mistral-Large-Instruct-2411, vertex_ai/mistral-large-2411, "mistral-large@2411-001", "mistral-large:123b"]
context_length: 128000
max_output_tokens: 102400
capabilities: [tool_calling, structured_output]
supported_parameters: [frequency_penalty, max_tokens, presence_penalty, response_format, seed, stop, structured_outputs, temperature, tool_choice, tools, top_p]
architecture:
  input_modalities: [text, file]
  output_modalities: [text]
  tokenizer: Mistral
open_weights: true
license: Mistral Research License
release_date: "2024-11-18"
knowledge_cutoff: "2024-11"
pricing:
  input: 2
  output: 6
  cache_read: 0.2
benchmarks:
  gpqa_diamond: 48.6
  humanitys_last_exam: 3.3
  ifbench: 31.2
  tau2_bench: 30.7
  terminal_bench_hard: 6.1
benchmark_variant: "Mistral Large 2 (Nov '24)"
sources:
  - https://openrouter.ai/mistralai/mistral-large
  - https://openrouter.ai/api/v1/models
  - https://openrouter.ai/api/v1/models/mistralai/mistral-large/endpoints
  - https://openrouter.ai/api/v1/models/mistralai/mistral-large-2411/endpoints
  - https://artificialanalysis.ai/models/mistral-large-2
  - https://docs.mistral.ai/getting-started/models
  - https://docs.mistral.ai/models/mistral-large-2-1-24-11
  - https://docs.mistral.ai/models/mistral-large-1-0-24-02
  - https://docs.mistral.ai/getting-started/changelog
  - https://mistral.ai/news/pixtral-large
  - https://huggingface.co/mistralai/Mistral-Large-Instruct-2411
  - https://huggingface.co/api/models/mistralai/Mistral-Large-Instruct-2411
  - https://huggingface.co/mistralai/Mistral-Large-Instruct-2411/raw/main/config.json
  - https://ollama.com/library/mistral-large
  - https://github.com/BerriAI/litellm/blob/main/model_prices_and_context_window.json
retrieved: "2026-11-01"
---

# Mistral Large

## Overview
OpenRouter created this id on 2024-02-26, the day Mistral Large 1.0 was released, and still serves it through Mistral. Its description names Mistral Large 2 (mistral-large-2407), but it gives a 128,000-token window and a November 2024 knowledge cutoff, against 131,072 tokens and March 2024 for the pinned mistralai/mistral-large-2407 listing. This card therefore covers Mistral Large 2.1 (API id mistral-large-2411, version 24.11), released on 2024-11-18 with Pixtral Large; OpenRouter's own mistralai/mistral-large-2411 listing had no endpoints at retrieval. It is a dense 123B model (88 layers, 131,072 positions in config.json) that Mistral says improves long-context understanding, system prompt handling and function calling over 24.07. Weights are on Hugging Face (mistralai/Mistral-Large-Instruct-2411) under the Mistral Research License, which covers research and non-commercial use; commercial self-deployment needs a licence from Mistral. Mistral's docs mark mistral-large-2411 deprecated on 2026-02-27 with a retirement date of 2026-05-31 and name Mistral Medium 3.5 as the replacement, itself deprecated on 2026-10-31 in favour of Mistral Large 4.

## Strengths
- Dozens of languages and 80+ programming languages, per the Hugging Face card.
- Native function calling and JSON output; the card asks for vLLM 0.6.4.post1 and mistral_common 1.5.0 or later.
- Artificial Analysis (Mistral Large 2 (Nov '24)): 48.6% on GPQA Diamond, 31.2% on IFBench and 30.7% on tau2-bench.

## Limitations
- Past its retirement date on Mistral's API, and OpenRouter's $2 input and $6 output per million tokens is high for a 2024 model.
- 6.1% on Terminal-Bench Hard. No image input and no reasoning mode.
- Research licence, so not free for commercial self-hosting.
- Needs over 300 GB of GPU memory, per the Hugging Face card.

## Good for
- Integrations pinned to Mistral Large 2 that have not yet moved to a current model.
- Research use of a large dense multilingual model.
- Retrieval-augmented and long-document question answering within 128K tokens.
