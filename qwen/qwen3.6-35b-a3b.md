---
id: qwen/qwen3.6-35b-a3b
name: Qwen3.6 35B A3B
owned_by: qwen
type: llm
description: "Qwen3.6 35B A3B is Alibaba's open-weight (Apache-2.0) vision-language mixture-of-experts model with 35B total and 3B active parameters, the first Qwen3.6 open release, tuned for agentic coding with preserved thinking and a 262,144-token native context."
aliases: [Qwen/Qwen3.6-35B-A3B, qwen3.6-35b-a3b, "qwen3.6:35b"]
context_length: 262144
max_output_tokens: 235929
capabilities: [tool_calling, reasoning, vision, structured_output]
supported_parameters: [frequency_penalty, include_reasoning, logit_bias, logprobs, max_tokens, min_p, presence_penalty, reasoning, repetition_penalty, response_format, seed, stop, structured_outputs, temperature, tool_choice, tools, top_k, top_logprobs, top_p]
architecture:
  input_modalities: [text, image, video]
  output_modalities: [text]
  tokenizer: Qwen
open_weights: true
license: Apache-2.0
release_date: "2026-04-16"
pricing:
  input: 0.15
  output: 1
  cache_read: 0.05
benchmarks:
  intelligence_index: 18.2
  coding_index: 41.9
  agentic_index: 13.1
  omniscience_index: -22.2
  humanitys_last_exam: 22.2
  gpqa_diamond: 84.1
  scicode: 36.6
  terminal_bench_hard: 34.8
  terminal_bench_4: 0
  long_context_reasoning: 71.7
  ifbench: 64.4
  tau2_bench: 95.3
  mmmu_pro: 75
  output_tokens_per_second: 134.1
  time_to_first_token_seconds: 2.06
benchmark_variant: Qwen3.6 35B A3B (Reasoning)
sources:
  - https://openrouter.ai/qwen/qwen3.6-35b-a3b
  - https://openrouter.ai/api/v1/models
  - https://artificialanalysis.ai/models/qwen3-6-35b-a3b
  - https://huggingface.co/Qwen/Qwen3.6-35B-A3B
  - https://github.com/QwenLM/Qwen3.6
  - https://ollama.com/library/qwen3.6
  - https://www.alibabacloud.com/help/en/model-studio/model-pricing
  - https://www.alibabacloud.com/help/en/model-studio/text-generation-model
retrieved: "2026-10-16"
---

# Qwen3.6 35B A3B

## Overview
Qwen3.6-35B-A3B, released on 2026-04-16, was the first open-weight Qwen3.6 model. It keeps the Qwen3.5-35B-A3B architecture: 40 layers alternating three Gated DeltaNet blocks with one gated attention block, 256-expert MoE layers activating 8 routed experts plus 1 shared, 35B total and 3B active parameters, and a vision encoder for image and video input. Qwen says the release prioritises stability and real-world coding (front-end workflows, repository-level reasoning) and adds `preserve_thinking`, which keeps reasoning traces from earlier turns for agent consistency. Thinking is on by default. Native context is 262,144 tokens (1,010,000 with YaRN); OpenRouter lists 262,144 with a 235,929-token output limit and $0.05 cached-input pricing. Qwen recommends vLLM 0.19.0 or SGLang 0.5.10 or later. Weights are Apache-2.0; Ollama serves `qwen3.6:35b` and Model Studio serves `qwen3.6-35b-a3b` under its legacy models at $0.375 input and $2.25 output per million tokens.

## Strengths
- Qwen reports SWE-bench Verified 73.4, SWE-bench Pro 49.5, Terminal-Bench 2.0 51.5, LiveCodeBench v6 80.4, GPQA 86.0, OmniDocBench 1.5 89.9 and MMMU-Pro 75.3, up from 70.0, 44.6, 40.5, 74.6, 84.2, 89.3 and 75.1 for Qwen3.5-35B-A3B.
- Fast: 134.1 tokens per second and 2.06 s to first token in Artificial Analysis' test.
- Artificial Analysis (Qwen3.6 35B A3B, Reasoning): tau2-bench 95.3%, MMMU-Pro 75%, GPQA Diamond 84.1%, Coding Index 41.9.

## Limitations
- AA Intelligence Index 18.2, Agentic Index 13.1, Omniscience -22.2; Terminal-Bench 4.0 0%, Terminal-Bench Hard 34.8%, IFBench 64.4%, Humanity's Last Exam 22.2%.
- All 35B parameters must be loaded although 3B are active; keep at least 128K tokens of context.

## Good for
- Cheap, fast coding and tool-use agents.
- Document OCR and visual grounding workloads.
- Local inference through Ollama.
