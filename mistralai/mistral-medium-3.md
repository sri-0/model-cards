---
id: mistralai/mistral-medium-3
name: Mistral Medium 3
owned_by: mistralai
type: llm
description: Mistral Medium 3 (mistral-medium-2505) is Mistral AI's proprietary mid-size multimodal model released in May 2025 at $0.40 input and $2 output per million tokens, with a Mistral retirement date of 2026-08-31.
aliases: [mistral-medium-2505, vertex_ai/mistral-medium-3, "mistral-medium-3@001", azure_ai/mistral-medium-2505, watsonx/mistralai/mistral-medium-2505]
context_length: 131072
max_output_tokens: 104857
capabilities: [tool_calling, vision, structured_output]
supported_parameters: [frequency_penalty, max_tokens, presence_penalty, response_format, seed, stop, structured_outputs, temperature, tool_choice, tools, top_p]
architecture:
  input_modalities: [text, image, file]
  output_modalities: [text]
  tokenizer: Mistral
open_weights: false
license: proprietary
release_date: "2025-05-07"
knowledge_cutoff: "2025-03"
pricing:
  input: 0.4
  output: 2
  cache_read: 0.04
benchmarks:
  gpqa_diamond: 57.8
  humanitys_last_exam: 4.0
  ifbench: 39.3
  long_context_reasoning: 31.3
  mmmu_pro: 53.0
  output_tokens_per_second: 45.7
  tau2_bench: 24.3
  terminal_bench_hard: 3.8
  time_to_first_token_seconds: 2.48
benchmark_variant: Mistral Medium 3
sources:
  - https://openrouter.ai/mistralai/mistral-medium-3
  - https://openrouter.ai/api/v1/models
  - https://openrouter.ai/api/v1/models/mistralai/mistral-medium-3/endpoints
  - https://artificialanalysis.ai/models/mistral-medium-3
  - https://docs.mistral.ai/getting-started/models
  - https://docs.mistral.ai/models/mistral-medium-3-25-05
  - https://docs.mistral.ai/getting-started/changelog
  - https://mistral.ai/news/mistral-medium-3
  - https://github.com/BerriAI/litellm/blob/main/model_prices_and_context_window.json
retrieved: "2026-11-01"
---

# Mistral Medium 3

## Overview
Mistral Medium 3 (API id mistral-medium-2505, version 25.05) was released on 2025-05-07. Mistral calls it a frontier-class multimodal model: it accepts text and images, returns text, and has a 128K context window. Mistral priced it at $0.40 input and $2 output per million tokens and claimed performance at or above 90% of Claude Sonnet 3.7, with benchmark tables published only as images. The weights are not public; Mistral offered hybrid, on-premises and in-VPC deployment on four GPUs and above. The API supports function calling, structured outputs, document question answering, predicted outputs, batching and the agents and conversations endpoints. Mistral's docs give a deprecation date of 2026-05-22 and a retirement date of 2026-08-31 and name Mistral Medium 3.5 as the replacement, itself deprecated on 2026-10-31 in favour of Mistral Large 4. OpenRouter still listed it with Mistral as the only provider at retrieval, with a knowledge cutoff of March 2025.

## Strengths
- Artificial Analysis (Mistral Medium 3): 57.8% on GPQA Diamond, 53.0% on MMMU-Pro and 39.3% on IFBench.
- Low OpenRouter price for its tier: $0.40 input, $2 output and $0.04 cached input per million tokens.
- Image input plus tool calling and structured outputs in one model.

## Limitations
- Past its retirement date on Mistral's API, and proprietary: self-hosting needs a Mistral contract.
- Slow on Artificial Analysis: 45.7 output tokens per second and 2.48 s to first token.
- Weak agentic results: 24.3% on tau2-bench and 3.8% on Terminal-Bench Hard. No reasoning mode.
- Mistral's own benchmark figures are not published as text.

## Good for
- Existing integrations that still route to mistral-medium-2505 through OpenRouter or a cloud partner.
- Document and image question answering at low cost where retirement is acceptable.
- A baseline when evaluating Mistral Medium 3.5 or Mistral Large 4 as the replacement.
