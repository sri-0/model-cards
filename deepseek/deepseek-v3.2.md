---
id: deepseek/deepseek-v3.2
name: DeepSeek V3.2
owned_by: deepseek
type: llm
description: DeepSeek V3.2 is DeepSeek's December 2025 reasoning and agent model (671B MoE, 37B active, MIT) with DeepSeek Sparse Attention and thinking integrated into tool use.
aliases: [deepseek-ai/DeepSeek-V3.2]
context_length: 163840
max_output_tokens: 147456
capabilities: [tool_calling, reasoning, structured_output]
supported_parameters: [frequency_penalty, include_reasoning, logit_bias, logprobs, max_tokens, min_p, presence_penalty, reasoning, repetition_penalty, response_format, seed, stop, structured_outputs, temperature, tool_choice, tools, top_k, top_logprobs, top_p]
architecture:
  input_modalities: [text]
  output_modalities: [text]
  tokenizer: DeepSeek
open_weights: true
license: MIT
release_date: "2025-12-01"
pricing:
  input: 0.259
  output: 0.8
  cache_read: 0.14
benchmarks:
  intelligence_index: 21.5
  coding_index: 44.2
  omniscience_index: -22.5
  humanitys_last_exam: 24.6
  gpqa_diamond: 84
  terminal_bench_hard: 35.6
  long_context_reasoning: 73.3
  ifbench: 60.7
  tau2_bench: 90.6
benchmark_variant: DeepSeek V3.2 (Reasoning)
sources:
  - https://openrouter.ai/deepseek/deepseek-v3.2
  - https://openrouter.ai/api/v1/models
  - https://artificialanalysis.ai/models/deepseek-v3-2
  - https://huggingface.co/deepseek-ai/DeepSeek-V3.2
  - https://api-docs.deepseek.com/news/news251201
  - https://api-docs.deepseek.com/updates
  - https://ollama.com/library/deepseek-v3.2
retrieved: "2026-10-16"
---

# DeepSeek V3.2

## Overview
DeepSeek V3.2, released 2025-12-01 under the MIT licence, is the successor to V3.2 Exp (671B MoE, 37B active, 128K context) and the vendor's first model to integrate thinking into tool use; tools work in both thinking and non-thinking modes. DeepSeek credits DeepSeek Sparse Attention, a scaled reinforcement-learning framework and an agentic task-synthesis pipeline covering more than 1,800 environments and 85K instructions. A high-compute sibling, DeepSeek-V3.2-Speciale (gold-medal results at IMO, IOI, ICPC World Finals and CMO 2025), ran on a temporary API endpoint without tool calls until 2025-12-15 and is on Hugging Face. On the vendor API `deepseek-chat` and `deepseek-reasoner` served V3.2 until DeepSeek V4 took over on 2026-04-24; those ids were retired on 2026-07-24, so V3.2 now comes from the weights or third parties such as OpenRouter. Ollama's `deepseek-v3.2` library was retired on 2026-07-15 with no weights pushed. Superseded by `deepseek/deepseek-v4-flash` and `deepseek/deepseek-v4-pro`.

## Strengths
- DeepSeek describes performance comparable to GPT-5 and reasoning inside tool calls.
- Artificial Analysis (variant DeepSeek V3.2 (Reasoning)): tau2-bench 90.6%, GPQA Diamond 84.0%, long-context reasoning 73.3%, IFBench 60.7%, Coding Index 44.2.
- OpenRouter output limit 147,456 tokens and cached input at $0.14 per million tokens.

## Limitations
- No Jinja chat template; the repo's `encoding` scripts build prompts, and the new `developer` role is for search agents only (the official API rejects it).
- AA Intelligence Index 21.5, HLE 24.6%, Omniscience Index -22.5; no AA speed figures.
- Recommended sampling is temperature 1.0 and top_p 0.95; the Speciale variant has no tool calling.

## Good for
- Agent workloads that need reasoning inside tool calls.
- Maths and competition coding.
- Self-hosted deployments on the same stack as V3.2 Exp.
