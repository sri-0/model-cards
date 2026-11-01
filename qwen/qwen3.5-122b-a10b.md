---
id: qwen/qwen3.5-122b-a10b
name: Qwen3.5 122B A10B
owned_by: qwen
type: llm
description: "Qwen3.5 122B A10B is Alibaba's open-weight (Apache-2.0) vision-language mixture-of-experts model with 122B total and 10B active parameters, Gated DeltaNet attention, thinking mode and a 262,144-token native context."
aliases: [Qwen/Qwen3.5-122B-A10B, qwen3.5-122b-a10b, "qwen3.5:122b"]
context_length: 262144
max_output_tokens: 65536
capabilities: [tool_calling, reasoning, vision, structured_output]
supported_parameters: [frequency_penalty, include_reasoning, logit_bias, logprobs, max_tokens, min_p, presence_penalty, reasoning, repetition_penalty, response_format, seed, stop, structured_outputs, temperature, tool_choice, tools, top_k, top_logprobs, top_p]
architecture:
  input_modalities: [text, image, video]
  output_modalities: [text]
  tokenizer: Qwen3
open_weights: true
license: Apache-2.0
release_date: "2026-02-24"
pricing:
  input: 0.26
  output: 2.08
benchmarks:
  intelligence_index: 15.6
  coding_index: 43.3
  omniscience_index: -41.5
  humanitys_last_exam: 25.2
  gpqa_diamond: 85.7
  scicode: 39.7
  terminal_bench_hard: 31.1
  terminal_bench_4: 0
  long_context_reasoning: 76.3
  ifbench: 75.7
  tau2_bench: 93.6
  mmmu_pro: 75
  output_tokens_per_second: 127.4
  time_to_first_token_seconds: 2.32
benchmark_variant: Qwen3.5 122B A10B (Reasoning)
sources:
  - https://openrouter.ai/qwen/qwen3.5-122b-a10b
  - https://openrouter.ai/api/v1/models
  - https://artificialanalysis.ai/models/qwen3-5-122b-a10b
  - https://huggingface.co/Qwen/Qwen3.5-122B-A10B
  - https://github.com/QwenLM/Qwen3.5
  - https://ollama.com/library/qwen3.5
  - https://www.alibabacloud.com/help/en/model-studio/model-pricing
  - https://www.alibabacloud.com/help/en/model-studio/text-generation-model
retrieved: "2026-10-16"
---

# Qwen3.5 122B A10B

## Overview
Qwen3.5-122B-A10B was released on 2026-02-24. It is a vision-language mixture-of-experts model with 122B total and 10B activated parameters: 48 layers alternating three Gated DeltaNet blocks with one gated attention block, each followed by a 256-expert MoE layer (8 routed plus 1 shared active). OpenRouter's listing says it is second only to Qwen3.5-397B-A17B in the series, with text capability well above Qwen3-235B-2507 and vision above Qwen3-VL-235B. Native context is 262,144 tokens (1,010,000 with YaRN); OpenRouter lists 262,144 with a 65,536-token output limit. Thinking is on by default. Weights are Apache-2.0 on Hugging Face; Ollama serves `qwen3.5:122b` (81 GB) and Model Studio serves `qwen3.5-122b-a10b` under its legacy models at $0.4 input and $3.2 output per million tokens.

## Strengths
- Qwen reports SWE-bench Verified 72.0, Terminal Bench 2 49.4, GPQA Diamond 86.6, HLE with CoT 25.3, MMMU-Pro 76.9, MathVision 86.2, BrowseComp 63.8 and OSWorld-Verified 58.0.
- Artificial Analysis (Qwen3.5 122B A10B, Reasoning): Coding Index 43.3, tau2-bench 93.6%, GPQA Diamond 85.7%, long-context reasoning 76.3%, IFBench 75.7%, MMMU-Pro 75%.
- 127.4 tokens per second and 2.32 s to first token in AA's test.

## Limitations
- AA Intelligence Index 15.6 and Omniscience -41.5; Terminal-Bench 4.0 0% and Terminal-Bench Hard 31.1%.
- Humanity's Last Exam 25.2% in AA's test.
- 122B of weights need multi-GPU memory (Qwen's reference vLLM command uses tensor parallel 8); keep at least 128K tokens of context.

## Good for
- Agentic coding and search agents at MoE inference cost.
- Document, chart and video understanding.
- Self-hosted deployments wanting near-flagship Qwen3.5 quality.
