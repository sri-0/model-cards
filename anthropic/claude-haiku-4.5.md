---
id: anthropic/claude-haiku-4.5
name: Claude Haiku 4.5
owned_by: anthropic
type: llm
description: Anthropic's small, fast Claude model from October 2025, now a legacy model with a 200K context window, succeeded by Claude Haiku 5.5.
aliases: [claude-haiku-4-5-20251001, claude-haiku-4-5, anthropic.claude-haiku-4-5, "anthropic.claude-haiku-4-5-20251001-v1:0", "claude-haiku-4-5@20251001", anthropic/claude-haiku-4-5]
context_length: 200000
max_output_tokens: 64000
capabilities: [tool_calling, reasoning, vision, structured_output]
supported_parameters: [include_reasoning, max_completion_tokens, max_tokens, reasoning, response_format, stop, structured_outputs, temperature, tool_choice, tools, top_k, top_p]
architecture:
  input_modalities: [text, image, file]
  output_modalities: [text]
  tokenizer: Claude
open_weights: false
license: proprietary
release_date: "2025-10-15"
knowledge_cutoff: "2025-02"
pricing:
  input: 1
  output: 5
  cache_read: 0.1
  cache_write: 1.25
benchmarks:
  intelligence_index: 16.9
  coding_index: 43.9
  agentic_index: 8
  omniscience_index: -4.4
  humanitys_last_exam: 10.4
  gpqa_diamond: 67.2
  scicode: 42.2
  terminal_bench_hard: 27.3
  terminal_bench_4: 0
  long_context_reasoning: 74.3
  ifbench: 54.3
  tau2_bench: 54.7
  mmmu_pro: 58.6
  output_tokens_per_second: 94.7
  time_to_first_token_seconds: 21.6
benchmark_variant: Claude 4.5 Haiku (Reasoning)
sources:
  - https://openrouter.ai/anthropic/claude-haiku-4.5
  - https://openrouter.ai/api/v1/models
  - https://artificialanalysis.ai/models/claude-4-5-haiku-reasoning
  - https://platform.claude.com/docs/en/models/haiku-4-5/overview
retrieved: "2026-10-14"
---

# Claude Haiku 4.5

## Overview
Claude Haiku 4.5 was Anthropic's fastest and most cost-efficient model at release. OpenRouter says it matched Claude Sonnet 4 across reasoning, coding and computer-use tasks, and it introduced extended thinking to the Haiku line. Anthropic lists a 200K-token context window and 64K maximum output. Its status is Active (legacy), with retirement not sooner than October 15, 2026. The API alias claude-haiku-4-5 resolves to the pinned snapshot claude-haiku-4-5-20251001. Its reliable knowledge cutoff is February 2025 and its training data cutoff is July 2025.

## Strengths
- OpenRouter reports a score above 73% on SWE-bench Verified.
- Works with coding, bash, web search and computer-use tools.
- Artificial Analysis rates the Reasoning variant faster than average (about 95 output tokens per second) and fairly concise.
- List price is $1 input and $5 output per million tokens, which Artificial Analysis rates well priced.

## Limitations
- Artificial Analysis measured an Intelligence Index of 16.9 for the Reasoning variant, at the lower end of comparable models (median 27).
- Uses manual extended thinking (thinking.type "enabled"), not adaptive thinking. Anthropic lists the effort parameter as not supported.
- The 200K context window is smaller than the 1M window of Claude Haiku 5.5.
- Retirement can occur from October 15, 2026.

## Good for
- Sub-agents and parallel execution in larger agent systems.
- Real-time and high-volume applications where latency and cost matter.
- Existing integrations that have not yet moved to Haiku 5.5.
