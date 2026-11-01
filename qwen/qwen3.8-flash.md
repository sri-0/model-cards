---
id: qwen/qwen3.8-flash
name: Qwen3.8 Flash
owned_by: qwen
type: llm
description: "Qwen3.8 Flash is Alibaba's hosted multimodal reasoning model with a 1M-token context, served from the open-weight Qwen3.8-Flash-Next (125B total, 6B active, Qwen Community License 1.0), an experimental preview of the Qwen4 architecture."
aliases: [Qwen/Qwen3.8-Flash-Next, qwen3.8-flash]
context_length: 1000000
max_output_tokens: 131072
capabilities: [tool_calling, reasoning, vision, structured_output]
supported_parameters: [frequency_penalty, include_reasoning, logprobs, max_tokens, presence_penalty, reasoning, response_format, seed, stop, structured_outputs, temperature, tool_choice, tools, top_k, top_logprobs, top_p]
architecture:
  input_modalities: [text, image, video]
  output_modalities: [text]
  tokenizer: Qwen
open_weights: true
license: Qwen Community License 1.0
release_date: "2026-08-26"
pricing:
  input: 0.15
  output: 0.47
  cache_read: 0.016
benchmarks:
  intelligence_index: 39.8
  omniscience_index: -9.7
  humanitys_last_exam: 38
  gpqa_diamond: 92.3
  scicode: 50.6
  terminal_bench_4: 25.3
  long_context_reasoning: 79.7
  mmmu_pro: 79.8
  output_tokens_per_second: 52
  time_to_first_token_seconds: 2.05
benchmark_variant: Qwen3.8-Flash-Next
sources:
  - https://openrouter.ai/qwen/qwen3.8-flash
  - https://openrouter.ai/api/v1/models
  - https://artificialanalysis.ai/models/qwen3-8-flash-next
  - https://huggingface.co/Qwen/Qwen3.8-Flash-Next
  - https://github.com/QwenLM/Qwen3.8-Flash-Next
  - https://huggingface.co/Qwen/Qwen3.8-Flash-Next/blob/main/LICENSE
  - https://www.qwencloud.com/models/qwen3.8-flash
  - https://www.alibabacloud.com/help/en/model-studio/model-pricing
  - https://www.alibabacloud.com/help/en/model-studio/text-generation-model
retrieved: "2026-10-16"
---

# Qwen3.8 Flash

## Overview
OpenRouter's `qwen/qwen3.8-flash` id covers Alibaba's hosted Qwen3.8 Flash and maps to the open weights Qwen/Qwen3.8-Flash-Next, released on 2026-08-26, which Qwen names as the basis of the service. Flash-Next is an experimental preview of the Qwen4 architecture: 48 layers alternating three Gated DeltaNet blocks with one Qwen Sparse Attention block, Gated Residual streams and n-gram embeddings, with 125B parameters (6B activated) plus a 51B n-gram embedding table and a 4B multi-token-prediction head, and a vision encoder for image and video input. Native context is 262,144 tokens (1,000,000 with YaRN); OpenRouter lists 1,000,000 with a 131,072-token output limit. Thinking is on by default with `reasoning_effort` (xhigh default) and `preserve_thinking`. The Qwen Community License 1.0 requires attribution above 100,000,000 monthly active users or US$20,000,000 monthly revenue and a separate licence for model-as-a-service businesses. Qwen Cloud and Model Studio serve `qwen3.8-flash` at $0.15 input and $0.47 output per million tokens ($0.016 cached), the same as OpenRouter, in one tier up to 1M tokens.

## Strengths
- Qwen reports DeepSWE 1.1 58.7, SWE-bench Pro 62.5, SWE-bench Multilingual 81.0, LiveCodeBench v6 91.9, GPQA Diamond 91.7, IFBench 81.3, and AndroidWorld 84.5, above Qwen3.8-27B on each row.
- Artificial Analysis (Qwen3.8-Flash-Next): Intelligence Index 39.8, GPQA Diamond 92.3%, Terminal-Bench 4.0 25.3%, MMMU-Pro 79.8%, long-context reasoning 79.7%; 52 tokens per second, 2.05 s to first token.

## Limitations
- Omniscience -9.7 and Humanity's Last Exam 38% in AA's test.
- New architecture: self-hosting needs an engine that supports it (Qwen lists Transformers, vLLM, SGLang and TokenSpeed), and the 51B embedding table adds memory.
- Not Apache-2.0 licensed.

## Good for
- Low-cost coding assistance and agentic workflows with 1M context.
- Document, chart, desktop-interaction and long-video analysis.
- Claude Code or Codex style tools via the compatible endpoints.
