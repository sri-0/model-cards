---
id: qwen/qwen3.6-27b
name: Qwen3.6 27B
owned_by: qwen
type: llm
description: "Qwen3.6 27B is Alibaba's 27B-parameter dense open-weight (Apache-2.0) vision-language model, the Qwen3.5-27B successor tuned for agentic coding, with optional preservation of thinking across turns and a 262,144-token native context."
aliases: [Qwen/Qwen3.6-27B, qwen3.6-27b, "qwen3.6:27b"]
context_length: 262144
max_output_tokens: 81920
capabilities: [tool_calling, reasoning, vision, structured_output]
supported_parameters: [frequency_penalty, include_reasoning, logit_bias, logprobs, max_tokens, min_p, presence_penalty, reasoning, repetition_penalty, response_format, seed, stop, structured_outputs, temperature, tool_choice, tools, top_k, top_logprobs, top_p]
architecture:
  input_modalities: [text, image, video]
  output_modalities: [text]
  tokenizer: Qwen3
open_weights: true
license: Apache-2.0
release_date: "2026-04-22"
pricing:
  input: 0.32
  output: 3.2
benchmarks:
  intelligence_index: 21.4
  coding_index: 53.7
  agentic_index: 18.5
  omniscience_index: -20
  humanitys_last_exam: 23.1
  gpqa_diamond: 84.2
  scicode: 42.8
  terminal_bench_hard: 34.8
  terminal_bench_4: 0
  long_context_reasoning: 77.3
  ifbench: 67.6
  tau2_bench: 94.2
  mmmu_pro: 74.6
  output_tokens_per_second: 55.7
  time_to_first_token_seconds: 3.62
benchmark_variant: Qwen3.6 27B (Reasoning)
sources:
  - https://openrouter.ai/qwen/qwen3.6-27b
  - https://openrouter.ai/api/v1/models
  - https://artificialanalysis.ai/models/qwen3-6-27b
  - https://huggingface.co/Qwen/Qwen3.6-27B
  - https://github.com/QwenLM/Qwen3.6
  - https://ollama.com/library/qwen3.6
  - https://www.alibabacloud.com/help/en/model-studio/model-pricing
  - https://www.alibabacloud.com/help/en/model-studio/text-generation-model
retrieved: "2026-10-16"
---

# Qwen3.6 27B

## Overview
Qwen3.6-27B was released on 2026-04-22, six days after Qwen3.6-35B-A3B, as the dense member of the first open Qwen3.6 pair. It keeps the Qwen3.5-27B architecture (64 layers of Gated DeltaNet and gated attention blocks with dense feed-forward layers, a vision encoder, text, image and video input) and, according to Qwen, prioritises stability and coding: front-end workflows and repository-level reasoning. New in 3.6 is `preserve_thinking`, an option that keeps reasoning traces from earlier turns, which Qwen says improves agent consistency and can cut redundant reasoning. Thinking is on by default. Native context is 262,144 tokens (1,010,000 with YaRN); OpenRouter lists 262,144 with an 81,920-token output limit. Qwen recommends vLLM 0.19.0 or SGLang 0.5.10 or later. Weights are Apache-2.0; Ollama serves `qwen3.6:27b` and Model Studio serves `qwen3.6-27b` under its legacy models at $0.6 input and $3.6 output per million tokens.

## Strengths
- Qwen reports SWE-bench Verified 77.2, SWE-bench Pro 53.5, Terminal-Bench 2.0 59.3, SkillsBench 48.2, LiveCodeBench v6 83.9, GPQA Diamond 87.8 and AndroidWorld 70.3, up from 75.0, 51.2, 41.6, 27.2, 80.7, 85.5 and 64.2 for Qwen3.5-27B in the same table.
- Artificial Analysis (Qwen3.6 27B, Reasoning): Coding Index 53.7, tau2-bench 94.2%, long-context reasoning 77.3%, GPQA Diamond 84.2%, MMMU-Pro 74.6%.

## Limitations
- AA Intelligence Index 21.4, Agentic Index 18.5, Omniscience -20; Terminal-Bench 4.0 0%, Terminal-Bench Hard 34.8%, IFBench 67.6%.
- 55.7 tokens per second and 3.62 s to first token in AA's test.
- Qwen's reference vLLM command uses tensor parallel 8; keep at least 128K tokens of context.

## Good for
- Agentic coding assistants, especially front-end and repository-scale work.
- Multi-turn agents that benefit from preserved thinking.
- Local deployment through Ollama.
