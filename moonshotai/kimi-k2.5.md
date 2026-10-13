---
id: moonshotai/kimi-k2.5
name: Kimi K2.5
owned_by: moonshotai
type: llm
description: Kimi K2.5 is Moonshot AI's open-weight native multimodal mixture-of-experts model (1T total, 32B active) with instant and thinking modes and agent-swarm task decomposition.
aliases: [kimi-k2.5, moonshot/kimi-k2.5, moonshotai/Kimi-K2.5]
context_length: 262144
max_output_tokens: 235929
capabilities: [tool_calling, reasoning, vision, structured_output]
supported_parameters: [frequency_penalty, include_reasoning, logit_bias, logprobs, max_tokens, min_p, presence_penalty, reasoning, repetition_penalty, response_format, seed, stop, structured_outputs, temperature, tool_choice, tools, top_k, top_logprobs, top_p]
architecture:
  input_modalities: [text, image]
  output_modalities: [text]
  tokenizer: Other
open_weights: true
license: Modified MIT
release_date: "2026-01-27"
pricing:
  input: 0.5
  output: 2.5
  cache_read: 0.15
benchmarks:
  intelligence_index: 23.5
  coding_index: 46.8
  omniscience_index: -7.3
  humanitys_last_exam: 30.7
  gpqa_diamond: 87.9
  terminal_bench_hard: 34.8
  long_context_reasoning: 78
  ifbench: 70.2
  tau2_bench: 95.9
  mmmu_pro: 75.4
  output_tokens_per_second: 60.4
  time_to_first_token_seconds: 1.59
benchmark_variant: Kimi K2.5 (Reasoning)
sources:
  - https://openrouter.ai/moonshotai/kimi-k2.5
  - https://openrouter.ai/api/v1/models
  - https://artificialanalysis.ai/models/kimi-k2-5
  - https://huggingface.co/moonshotai/Kimi-K2.5
  - https://github.com/BerriAI/litellm/blob/main/model_prices_and_context_window.json
retrieved: "2026-10-14"
---

# Kimi K2.5

## Overview
Kimi K2.5 was released in January 2026. Moonshot built it through continual pretraining on about 15 trillion mixed visual and text tokens on top of Kimi-K2-Base. It is a mixture-of-experts model with 1T total and 32B activated parameters and a 256K-token context window. Weights are on Hugging Face (moonshotai/Kimi-K2.5) under a modified MIT licence. On 2026-01-29 Moonshot removed the default system prompt and fixed a chat-template token, so use the updated template.

## Strengths
- Vision grounded in pretraining: Moonshot targets code generation from UI designs and video workflows.
- Supports instant and thinking modes in one model.
- Agent swarm execution: decomposes tasks into parallel sub-tasks run by dynamically created agents.
- Artificial Analysis Intelligence Index 23.5 and Coding Index 46.8 on Kimi K2.5 (Reasoning).

## Limitations
- Artificial Analysis marks its Intelligence Index value as estimated.
- Slower than average on Artificial Analysis: 60.4 output tokens per second, 1.59 s to first token.
- Artificial Analysis rates it somewhat expensive compared with open-weight models of similar size.
- Superseded by Kimi K2.6, Kimi K2.7 Code and Kimi K3, which score higher on Artificial Analysis.

## Good for
- Turning screenshots, mockups and designs into front-end code.
- Visual question answering and tool use grounded in images.
- Parallel multi-agent workflows.
- Existing deployments already tuned for K2.5 that do not need the newer releases.
