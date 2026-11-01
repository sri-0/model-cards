---
id: deepseek/deepseek-chat-v3-0324
name: DeepSeek V3 0324
owned_by: deepseek
type: llm
description: DeepSeek V3 0324 is the March 2025 MIT-licensed update of DeepSeek V3 (671B MoE, 37B active) with better reasoning, front-end coding and function calling.
aliases: [deepseek-ai/DeepSeek-V3-0324]
context_length: 163840
max_output_tokens: 115200
capabilities: [tool_calling, structured_output]
supported_parameters: [frequency_penalty, logprobs, max_tokens, response_format, seed, structured_outputs, temperature, tool_choice, tools, top_k, top_logprobs, top_p]
architecture:
  input_modalities: [text]
  output_modalities: [text]
  tokenizer: DeepSeek
open_weights: true
license: MIT
release_date: "2025-03-25"
knowledge_cutoff: "2024-07"
pricing:
  input: 0.29
  output: 1.14
  cache_read: 0.11
benchmarks:
  intelligence_index: 9.7
  coding_index: 21.2
  agentic_index: 0.8
  omniscience_index: -40.7
  humanitys_last_exam: 4.7
  gpqa_diamond: 65.5
  scicode: 39
  terminal_bench_hard: 15.2
  terminal_bench_4: 0
  long_context_reasoning: 40.7
  ifbench: 41
  tau2_bench: 47.1
  output_tokens_per_second: 88.5
  time_to_first_token_seconds: 0.69
benchmark_variant: DeepSeek V3 0324
sources:
  - https://openrouter.ai/deepseek/deepseek-chat-v3-0324
  - https://openrouter.ai/api/v1/models
  - https://artificialanalysis.ai/models/deepseek-v3-0324
  - https://huggingface.co/deepseek-ai/DeepSeek-V3-0324
  - https://api-docs.deepseek.com/news/news250325
  - https://api-docs.deepseek.com/updates
retrieved: "2026-10-16"
---

# DeepSeek V3 0324

## Overview
DeepSeek V3 0324 is the March 2025 checkpoint of DeepSeek V3: the same 671B-parameter MoE (37B active, 128K context per the Hugging Face card) re-released under the MIT licence. The weights appeared on Hugging Face on 2025-03-24, the day the vendor id `deepseek-chat` switched to it; the release note is dated 2025-03-25. `deepseek-chat` moved on to DeepSeek V3.1 on 2025-08-21 and was retired on 2026-07-24, so the model is now served only through third parties such as OpenRouter or from the weights. OpenRouter's top provider offers 128,000 tokens of context against the 163,840 listed for the model, with a 115,200-token output limit. Superseded by `deepseek/deepseek-chat-v3.1`.

## Strengths
- DeepSeek reports gains over V3: MMLU-Pro 75.9 to 81.2, GPQA 59.1 to 68.4, AIME 39.6 to 59.4 and LiveCodeBench 39.2 to 49.2.
- Better front-end code and Chinese writing, more accurate function calling; JSON output and FIM completion supported.
- Artificial Analysis (variant DeepSeek V3 0324): tau2-bench 47.1%, 88.5 tokens per second, 0.69 s to first token.

## Limitations
- No thinking mode; AA Intelligence Index 9.7, Agentic Index 0.8, Terminal-Bench Hard 15.2%.
- Omniscience Index -40.7.
- The vendor API mapped temperature 1.0 to a model temperature of 0.3; self-hosters should set 0.3 directly.
- Same deployment footprint as V3: FP8 weights, multi-GPU node, Transformers not supported directly.

## Good for
- Non-reasoning chat and coding at low cost.
- Web front-end generation and Chinese text.
- Drop-in upgrade for V3 deployments under a permissive licence.
