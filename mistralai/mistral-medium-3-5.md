---
id: mistralai/mistral-medium-3-5
name: Mistral Medium 3.5
owned_by: mistralai
type: llm
description: Mistral Medium 3.5 is a dense 128B open-weight multimodal model from Mistral AI that handles instruction following, reasoning and coding in one set of weights.
aliases: [mistral-medium-2604, mistral/mistral-medium-2604, mistral/mistral-medium-3-5, mistralai/Mistral-Medium-3.5-128B]
context_length: 262144
max_output_tokens: 209715
capabilities: [tool_calling, reasoning, vision, structured_output]
supported_parameters: [frequency_penalty, include_reasoning, max_tokens, presence_penalty, reasoning, reasoning_effort, response_format, seed, stop, structured_outputs, temperature, tool_choice, tools, top_p]
architecture:
  input_modalities: [text, image, file]
  output_modalities: [text]
  tokenizer: Mistral
open_weights: true
license: Modified MIT
release_date: "2026-04-29"
pricing:
  input: 1.5
  output: 7.5
benchmarks:
  intelligence_index: 14.2
  coding_index: 46.9
  agentic_index: 7
  omniscience_index: -36.8
  humanitys_last_exam: 13.8
  gpqa_diamond: 74.8
  scicode: 40.2
  terminal_bench_hard: 33.3
  terminal_bench_4: 0
  long_context_reasoning: 69.3
  ifbench: 68.8
  tau2_bench: 94.2
  mmmu_pro: 64.9
  output_tokens_per_second: 167
  time_to_first_token_seconds: 2.17
benchmark_variant: Mistral Medium 3.5
sources:
  - https://openrouter.ai/mistralai/mistral-medium-3-5
  - https://openrouter.ai/api/v1/models
  - https://artificialanalysis.ai/models/mistral-medium-3-5
  - https://docs.mistral.ai/getting-started/models
  - https://huggingface.co/mistralai/Mistral-Medium-3.5-128B
  - https://github.com/BerriAI/litellm/blob/main/model_prices_and_context_window.json
retrieved: "2026-10-14"
---

# Mistral Medium 3.5

## Overview
Mistral Medium 3.5 (API id mistral-medium-2604) was released in April 2026. It is a dense 128B model with a 256K-token context window, text and image input, and per-request reasoning effort (none or high). Mistral says it replaces Mistral Medium 3.1 and Magistral in Le Chat and Devstral 2 in its Vibe coding agent. Weights are on Hugging Face (mistralai/Mistral-Medium-3.5-128B) under a Modified MIT licence that allows commercial use with exceptions for companies with large revenue.

## Strengths
- Mistral reports 77.6% on SWE-Bench Verified and 91.4% on τ³-Telecom.
- Artificial Analysis Intelligence Index 14.2 and Coding Index 46.9 (variant: Mistral Medium 3.5).
- Fast: 167 output tokens per second and 2.17 s to first token on Artificial Analysis.
- Native function calling and JSON output. Vision encoder trained to handle variable image sizes and aspect ratios.
- OpenRouter notes it can be self-hosted on as few as four GPUs.

## Limitations
- Artificial Analysis rates it particularly expensive compared with open-weight models of similar size.
- Agentic Index is low (7) on Artificial Analysis.
- The licence restricts companies with large revenue. Check the terms.
- The original Transformers config caused long-context degradation. GGUFs built from the config before the fix are affected, so use updated files.

## Good for
- Agentic coding, including with Mistral Vibe.
- Multi-tool workflows that need reliable function calling.
- Self-hosted general assistants with vision and long context.
- Teams moving off Devstral 2, Magistral or Mistral Medium 3.1.
