---
id: moonshotai/kimi-k2.6
name: Kimi K2.6
owned_by: moonshotai
type: llm
description: Kimi K2.6 is Moonshot AI's open-weight multimodal mixture-of-experts model (1T total, 32B active) for long-horizon coding, interface generation and multi-agent orchestration.
aliases: [kimi-k2.6, moonshot/kimi-k2.6, moonshotai/Kimi-K2.6]
context_length: 262144
max_output_tokens: 235929
capabilities: [tool_calling, reasoning, vision, structured_output]
supported_parameters: [frequency_penalty, include_reasoning, logit_bias, logprobs, max_tokens, min_p, parallel_tool_calls, presence_penalty, reasoning, repetition_penalty, response_format, seed, stop, structured_outputs, temperature, tool_choice, tools, top_k, top_logprobs, top_p]
architecture:
  input_modalities: [text, image]
  output_modalities: [text]
  tokenizer: Other
open_weights: true
license: Modified MIT
release_date: "2026-04-20"
pricing:
  input: 0.65
  output: 3.41
  cache_read: 0.15
benchmarks:
  intelligence_index: 27
  coding_index: 61.8
  agentic_index: 20.5
  omniscience_index: 5.3
  humanitys_last_exam: 37.5
  gpqa_diamond: 91.1
  scicode: 51.5
  terminal_bench_hard: 43.9
  terminal_bench_4: 0.5
  long_context_reasoning: 81
  ifbench: 76
  tau2_bench: 95.9
  mmmu_pro: 79.4
  output_tokens_per_second: 43.4
  time_to_first_token_seconds: 2.92
benchmark_variant: Kimi K2.6 (Reasoning)
sources:
  - https://openrouter.ai/moonshotai/kimi-k2.6
  - https://openrouter.ai/api/v1/models
  - https://artificialanalysis.ai/models/kimi-k2-6
  - https://huggingface.co/moonshotai/Kimi-K2.6
  - https://github.com/BerriAI/litellm/blob/main/model_prices_and_context_window.json
retrieved: "2026-10-14"
---

# Kimi K2.6

## Overview
Kimi K2.6 was released in April 2026. It is a native multimodal mixture-of-experts model with 1T total and 32B activated parameters and a 256K-token context window. OpenRouter lists text and image input. Weights are on Hugging Face (moonshotai/Kimi-K2.6) under a modified MIT licence. Moonshot describes an agent swarm mode that scales to 300 sub-agents executing 4,000 coordinated steps.

## Strengths
- Artificial Analysis Intelligence Index 27 and Coding Index 61.8, measured on Kimi K2.6 (Reasoning).
- Moonshot targets end-to-end coding across Python, Rust and Go, including front-end, DevOps and performance work.
- Turns prompts and visual inputs into working interfaces and lightweight full-stack workflows.
- Built for persistent background agents that run schedules, execute code and coordinate across platforms.

## Limitations
- Slow and verbose on Artificial Analysis: 43.4 output tokens per second, 2.92 s to first token, and 180M tokens generated to run the Intelligence Index (very verbose).
- Artificial Analysis rates it somewhat expensive compared with open-weight models of similar size.
- Kimi K2.7 Code, built on K2.6, uses fewer thinking tokens for coding work according to Moonshot.
- 1T total parameters make self-hosting demanding.

## Good for
- Long autonomous coding runs and multi-agent task decomposition.
- Generating UIs, documents, websites and spreadsheets from prompts and images.
- Background agents that need tool use over many steps.
- Self-hosted deployments that accept a modified MIT licence.
