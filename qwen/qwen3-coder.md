---
id: qwen/qwen3-coder
name: Qwen3 Coder 480B A35B
owned_by: qwen
type: llm
description: Qwen3 Coder 480B A35B Instruct is Qwen's July 2025 open-weight (Apache-2.0) mixture-of-experts coding model with 480B total and 35B active parameters, built for agentic coding with a native 262,144-token context.
aliases: [Qwen/Qwen3-Coder-480B-A35B-Instruct, "qwen3-coder:480b"]
context_length: 262144
max_output_tokens: 65536
capabilities: [tool_calling, structured_output]
supported_parameters: [frequency_penalty, logit_bias, logprobs, max_tokens, min_p, presence_penalty, repetition_penalty, response_format, seed, stop, structured_outputs, temperature, tool_choice, tools, top_k, top_logprobs, top_p]
architecture:
  input_modalities: [text]
  output_modalities: [text]
  tokenizer: Qwen3
open_weights: true
license: Apache-2.0
release_date: "2025-07-22"
knowledge_cutoff: "2025-06"
pricing:
  input: 0.3
  output: 1
  cache_read: 0.1
benchmarks:
  intelligence_index: 11.9
  omniscience_index: -22.2
  humanitys_last_exam: 4.5
  gpqa_diamond: 61.8
  terminal_bench_hard: 18.9
  long_context_reasoning: 45.7
  ifbench: 40.5
  tau2_bench: 43.6
  output_tokens_per_second: 95.1
  time_to_first_token_seconds: 0.93
benchmark_variant: Qwen3 Coder 480B A35B Instruct
sources:
  - https://openrouter.ai/qwen/qwen3-coder
  - https://openrouter.ai/api/v1/models
  - https://artificialanalysis.ai/models/qwen3-coder-480b-a35b-instruct
  - https://huggingface.co/Qwen/Qwen3-Coder-480B-A35B-Instruct
  - https://qwenlm.github.io/blog/qwen3-coder/
  - https://ollama.com/library/qwen3-coder
retrieved: "2026-10-16"
---

# Qwen3 Coder 480B A35B

## Overview
Qwen3-Coder-480B-A35B-Instruct was announced in the Qwen blog on 2025-07-22 as the first and largest Qwen3-Coder model. The Hugging Face card gives 480B total and 35B activated parameters, 62 layers, grouped-query attention with 96 query and 8 key-value heads, 160 experts with 8 active, and a native context of 262,144 tokens, extendable to 1M tokens with YaRN. It runs only in non-thinking mode, uses a purpose-built function-call format, and ships with the Qwen Code CLI (adapted from Gemini CLI) plus instructions for Claude Code and Cline. The blog's API examples use the hosted id qwen3-coder-plus on Model Studio. OpenRouter lists a 262,144-token context, 65,536 output tokens and a June 2025 cutoff, and notes that Alibaba's endpoints charge more above 128K input tokens. Ollama serves it as qwen3-coder:480b. Qwen3-Coder-Next and the Qwen3.5 to Qwen3.8 generations, which have their own cards, supersede it.

## Strengths
- Qwen says it sets state-of-the-art results among open models on agentic coding, browser use and tool use, and on SWE-bench Verified without test-time scaling; the blog gives no figures in text.
- Artificial Analysis (Qwen3 Coder 480B A35B Instruct): Terminal-Bench Hard 18.9%, tau2-bench 43.6%, long-context reasoning 45.7%, Omniscience -22.2, the best Omniscience score among the Qwen3 cards.
- 95.1 output tokens per second and 0.93 s to first token in Artificial Analysis' measurements.
- Tool calling, structured outputs and prompt caching on OpenRouter.

## Limitations
- Artificial Analysis Intelligence Index 11.9, GPQA Diamond 61.8% and Humanity's Last Exam 4.5%.
- No thinking mode and text input only.
- Qwen recommends 65,536 output tokens, so budgets must be generous.
- 480B total parameters need a multi-GPU node to self-host.

## Good for
- Repository-scale agentic coding with Qwen Code, Claude Code or Cline.
- Function-calling and browser-use agents.
- Long-context code review across large codebases.
