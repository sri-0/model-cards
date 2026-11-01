---
id: deepseek/deepseek-v3.1-terminus
name: DeepSeek V3.1 Terminus
owned_by: deepseek
type: llm
description: DeepSeek V3.1 Terminus is the September 2025 refinement of DeepSeek V3.1 (671B MoE, 37B active, MIT) that fixes language mixing and improves code and search agents.
aliases: [deepseek-ai/DeepSeek-V3.1-Terminus, "deepseek-v3.1:671b"]
context_length: 163840
max_output_tokens: 147456
capabilities: [tool_calling, reasoning, structured_output]
supported_parameters: [frequency_penalty, include_reasoning, max_tokens, reasoning, response_format, stop, structured_outputs, temperature, tool_choice, tools, top_k, top_p]
architecture:
  input_modalities: [text]
  output_modalities: [text]
  tokenizer: DeepSeek
  instruct_type: deepseek-v3.1
open_weights: true
license: MIT
release_date: "2025-09-22"
knowledge_cutoff: "2025-03"
pricing:
  input: 0.27
  output: 1
benchmarks:
  intelligence_index: 14.8
  coding_index: 43.5
  agentic_index: 6.8
  omniscience_index: -26.4
  humanitys_last_exam: 16.4
  gpqa_diamond: 79.2
  scicode: 38
  terminal_bench_hard: 30.3
  terminal_bench_4: 0
  long_context_reasoning: 69.3
  ifbench: 57
  tau2_bench: 37.1
benchmark_variant: DeepSeek V3.1 Terminus (Reasoning)
sources:
  - https://openrouter.ai/deepseek/deepseek-v3.1-terminus
  - https://openrouter.ai/api/v1/models
  - https://artificialanalysis.ai/models/deepseek-v3-1-terminus
  - https://huggingface.co/deepseek-ai/DeepSeek-V3.1-Terminus
  - https://api-docs.deepseek.com/news/news250922
  - https://api-docs.deepseek.com/news/news250929
  - https://api-docs.deepseek.com/updates
  - https://ollama.com/library/deepseek-v3.1
retrieved: "2026-10-16"
---

# DeepSeek V3.1 Terminus

## Overview
DeepSeek V3.1 Terminus, released 2025-09-22 under the MIT licence, is a maintenance update of DeepSeek V3.1 (671B MoE, 37B active, 128K context) that keeps the hybrid thinking/non-thinking design while fixing user-reported problems: fewer Chinese-English mix-ups and stray characters, and better code and search agents. The vendor ids `deepseek-chat` (non-thinking) and `deepseek-reasoner` (thinking) served it from 2025-09-22 until V3.2 Exp replaced it on 2025-09-29; a temporary comparison endpoint ran until 2025-10-15. The vendor API no longer serves it; it is available from the weights and through OpenRouter. Ollama's `deepseek-v3.1:671b` tag (404 GB, Q4_K_M) carries Terminus. Superseded by `deepseek/deepseek-v3.2-exp`.

## Strengths
- DeepSeek reports gains over V3.1: Humanity's Last Exam 15.9 to 21.7, BrowseComp 30.0 to 38.5, SWE-bench Verified 66.0 to 68.4, SWE-bench Multilingual 54.5 to 57.8, Terminal-bench 31.3 to 36.7.
- Artificial Analysis (variant DeepSeek V3.1 Terminus (Reasoning)): Coding Index 43.5, long-context reasoning 69.3%, IFBench 57.0%, GPQA Diamond 79.2%.
- OpenRouter output limit 147,456 tokens.

## Limitations
- AA Intelligence Index 14.8, Agentic Index 6.8, tau2-bench 37.1%; no AA speed figures.
- Omniscience Index -26.4.
- Known checkpoint issue: `self_attn.o_proj` weights are not in the UE8M0 FP8 scale format.
- No cached-input price on OpenRouter.

## Good for
- Teams on V3.1 who need the language-consistency fixes.
- Code and search agents using DeepSeek's tool template.
- Baseline comparisons with V3.2 Exp, which was trained to match it.
