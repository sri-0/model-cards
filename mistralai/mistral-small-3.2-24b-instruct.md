---
id: mistralai/mistral-small-3.2-24b-instruct
name: Mistral Small 3.2 24B
owned_by: mistralai
type: llm
description: Mistral Small 3.2 is a 24B Apache-2.0 open-weight instruct model from Mistral AI with image input, released in June 2025 as an update to Mistral Small 3.1.
aliases: [mistral-small-2506, mistralai/Mistral-Small-3.2-24B-Instruct-2506]
context_length: 256000
max_output_tokens: 16384
capabilities: [tool_calling, vision, structured_output]
supported_parameters: [frequency_penalty, logit_bias, logprobs, max_tokens, min_p, presence_penalty, repetition_penalty, response_format, seed, stop, structured_outputs, temperature, tool_choice, tools, top_k, top_logprobs, top_p]
architecture:
  input_modalities: [image, text]
  output_modalities: [text]
  tokenizer: Mistral
open_weights: true
license: Apache-2.0
release_date: "2025-06-20"
knowledge_cutoff: "2023-10"
pricing:
  input: 0.09375
  output: 0.25
benchmarks:
  intelligence_index: 8.2
  omniscience_index: -50.6
  humanitys_last_exam: 4.3
  gpqa_diamond: 50.5
  scicode: 28.6
  terminal_bench_hard: 6.8
  terminal_bench_4: 0
  long_context_reasoning: 20.3
  ifbench: 33.5
  tau2_bench: 29.5
  mmmu_pro: 48
  output_tokens_per_second: 36.9
  time_to_first_token_seconds: 0.99
benchmark_variant: Mistral Small 3.2
sources:
  - https://openrouter.ai/mistralai/mistral-small-3.2-24b-instruct
  - https://openrouter.ai/api/v1/models
  - https://artificialanalysis.ai/models/mistral-small-3-2
  - https://docs.mistral.ai/getting-started/models
  - https://huggingface.co/mistralai/Mistral-Small-3.2-24B-Instruct-2506
retrieved: "2026-10-14"
---

# Mistral Small 3.2 24B

## Overview
Mistral Small 3.2 (Hugging Face mistralai/Mistral-Small-3.2-24B-Instruct-2506) is a minor update of Mistral Small 3.1 24B. It accepts text and images and supports tool calling and structured outputs. OpenRouter lists a 256,000-token context window and a 16,384-token output limit. Artificial Analysis lists a 128K context window. OpenRouter gives a knowledge cutoff of October 2023. Mistral's models page lists the API version (mistral-small-2506) as retired: deprecated on 4/30/2026 and retired on 7/31/2026, with Mistral Small 4 as the replacement. The weights remain available and OpenRouter still lists the model.

## Strengths
- Better instruction following than 3.1: Mistral reports Wildbench v2 65.33% and Arena Hard v2 43.1%.
- Fewer runaway outputs: Mistral reports infinite generations down from 2.11% to 1.29%.
- More robust function-calling template than 3.1.
- Artificial Analysis Intelligence Index 8.2 (variant: Mistral Small 3.2), well above average for open-weight non-reasoning models of its size.

## Limitations
- Artificial Analysis marks that Intelligence Index value as estimated.
- Slow on the measured provider: 36.9 output tokens per second (0.99 s to first token).
- Old knowledge cutoff and no reasoning mode.
- No longer served on Mistral's own API.

## Good for
- Self-hosted mid-size assistants under a permissive licence.
- Chart and document question answering with image input.
- Function calling and structured extraction.
- Existing deployments not yet moved to Mistral Small 4.
