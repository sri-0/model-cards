---
id: moonshotai/kimi-k2-thinking
name: Kimi K2 Thinking
owned_by: moonshotai
type: llm
description: Kimi K2 Thinking is Moonshot AI's open-weight text-only reasoning model (1T total, 32B active) trained to interleave step-by-step thinking with tool calls.
aliases: [kimi-k2-thinking, moonshotai.kimi-k2-thinking, moonshotai/Kimi-K2-Thinking]
context_length: 262144
max_output_tokens: 98304
capabilities: [tool_calling, reasoning, structured_output]
supported_parameters: [frequency_penalty, include_reasoning, logprobs, max_tokens, presence_penalty, reasoning, repetition_penalty, response_format, seed, stop, structured_outputs, temperature, tool_choice, tools, top_k, top_logprobs, top_p]
architecture:
  input_modalities: [text]
  output_modalities: [text]
  tokenizer: Other
open_weights: true
license: Modified MIT
release_date: "2025-11-06"
pricing:
  input: 0.6
  output: 2.5
  cache_read: 0.15
benchmarks:
  intelligence_index: 22
  omniscience_index: -21.4
  humanitys_last_exam: 23.8
  gpqa_diamond: 83.8
  terminal_bench_hard: 31.1
  long_context_reasoning: 72
  ifbench: 68.1
  tau2_bench: 93
  output_tokens_per_second: 160.2
  time_to_first_token_seconds: 1.2
benchmark_variant: Kimi K2 Thinking
sources:
  - https://openrouter.ai/moonshotai/kimi-k2-thinking
  - https://openrouter.ai/api/v1/models
  - https://artificialanalysis.ai/models/kimi-k2-thinking
  - https://huggingface.co/moonshotai/Kimi-K2-Thinking
  - https://github.com/BerriAI/litellm/blob/main/model_prices_and_context_window.json
retrieved: "2026-10-14"
---

# Kimi K2 Thinking

## Overview
Kimi K2 Thinking was released in November 2025 and extends the Kimi K2 mixture-of-experts architecture (1T total, 32B activated parameters) into agentic reasoning. It has a 256K-token context window and accepts text only. It is a native INT4 model: Moonshot applied quantization-aware training after pre-training to cut latency and GPU memory. Weights are on Hugging Face (moonshotai/Kimi-K2-Thinking) under a modified MIT licence.

## Strengths
- Trained end to end to mix reasoning with function calls. Moonshot reports stable behaviour across 200 to 300 consecutive tool invocations.
- Moonshot-reported results include 71.3% on SWE-bench Verified and 60.2% on BrowseComp, both with tools.
- Fast on Artificial Analysis: 160.2 output tokens per second and 1.2 s to first token.
- Artificial Analysis Intelligence Index 22 (variant: Kimi K2 Thinking).

## Limitations
- Text input only. No vision.
- Artificial Analysis marks its Intelligence Index value as estimated, and rates the model particularly expensive compared with open-weight models of similar size.
- OpenRouter lists a maximum output of 98,304 tokens, lower than later Kimi models.
- Older than Kimi K2.5, K2.6, K2.7 Code and K3, which all score higher on Artificial Analysis.

## Good for
- Research agents that chain many search and tool calls.
- Long multi-step reasoning in text: analysis, maths, planning.
- Text-only coding agents.
- Self-hosted deployments that benefit from the INT4 weights.
