---
id: minimax/minimax-m3
name: MiniMax M3
owned_by: minimax
type: llm
description: MiniMax-M3 is MiniMax's open-weight native multimodal mixture-of-experts model (about 428B total, 23B active parameters) with MiniMax Sparse Attention, a 1M-token context window and text, image and video input, built for long-horizon agentic and coding work.
aliases: [MiniMax-M3, minimax/minimax-m3-20260531, MiniMaxAI/MiniMax-M3, MiniMaxAI/MiniMax-M3-MXFP8, azure_ai/FW-MiniMax-M3, "minimax-m3:cloud"]
context_length: 1048576
max_output_tokens: 512000
capabilities: [tool_calling, reasoning, vision, structured_output]
supported_parameters: [frequency_penalty, include_reasoning, logit_bias, logprobs, max_tokens, min_p, presence_penalty, reasoning, repetition_penalty, response_format, seed, stop, structured_outputs, temperature, tool_choice, tools, top_k, top_logprobs, top_p]
architecture:
  input_modalities: [text, image, video]
  output_modalities: [text]
  tokenizer: Other
open_weights: true
license: MiniMax Community License
release_date: "2026-06-01"
pricing:
  input: 0.3
  output: 1.2
  cache_read: 0.06
benchmarks:
  coding_index: 58.6
  agentic_index: 29.5
  gpqa_diamond: 92.9
  humanitys_last_exam: 39.0
  ifbench: 82.9
  intelligence_index: 18.7
  long_context_reasoning: 83.0
  mmmu_pro: 78.6
  omniscience_index: -5.5
  output_tokens_per_second: 106.2
  scicode: 47.1
  tau2_bench: 88.9
  terminal_bench_4: 2.0
  terminal_bench_hard: 42.4
  time_to_first_token_seconds: 1.11
benchmark_variant: MiniMax-M3
sources:
  - https://openrouter.ai/minimax/minimax-m3
  - https://openrouter.ai/api/v1/models
  - https://artificialanalysis.ai/models/minimax-m3
  - https://huggingface.co/MiniMaxAI/MiniMax-M3
  - https://huggingface.co/api/models/MiniMaxAI/MiniMax-M3
  - https://huggingface.co/MiniMaxAI/MiniMax-M3/raw/main/config.json
  - https://huggingface.co/MiniMaxAI/MiniMax-M3/raw/main/LICENSE
  - https://huggingface.co/MiniMaxAI/MiniMax-M3-MXFP8
  - https://arxiv.org/abs/2606.13392
  - https://www.minimax.io/models/text/m3
  - https://platform.minimax.io/docs/faq/models.md
  - https://platform.minimax.io/docs/guides/text-generation.md
  - https://platform.minimax.io/docs/api-reference/text-anthropic-api.md
  - https://platform.minimax.io/docs/api-reference/text-openai-api.md
  - https://platform.minimax.io/docs/guides/local-deploy-m3.md
  - https://platform.minimax.io/docs/pricing/overview.md
  - https://platform.minimax.io/docs/release-notes/models.md
  - https://raw.githubusercontent.com/BerriAI/litellm/main/model_prices_and_context_window.json
  - https://ollama.com/library/minimax-m3
retrieved: "2026-11-01"
---

# MiniMax M3

## Overview
MiniMax-M3 was released on 2026-06-01 (MiniMax release notes and Artificial Analysis); weights reached Hugging Face on 2026-06-02 under the MiniMax Community License, in BF16 and MXFP8 (about 444 GB). It is a native multimodal mixture-of-experts model with about 428B total and 23B activated parameters and text, image and video input. MiniMax Sparse Attention (MSA, arXiv 2606.13392) gives it a 1M-token context; MiniMax claims 9x prefill and 15x decode speedups over M2 at 1M. Its API guarantees at least 512K of that window, and OpenRouter's top provider serves 524,288 tokens. The Hugging Face card lists `thinking` modes enabled, adaptive and disabled; on MiniMax's Anthropic-compatible API thinking is off unless `adaptive` is sent, while the OpenAI-compatible API thinks by default.

## Strengths
- Artificial Analysis Intelligence Index v5 of 18.7 (MiniMax-M3), with 92.9% on GPQA Diamond, 88.9% on tau2-bench, 83.0% on AA-LCR, 82.9% on IFBench and 78.6% on MMMU-Pro.
- Fast: 106.2 output tokens per second and 1.11 s to first token on AA.
- MiniMax reports 83.5 on BrowseComp and 37.1 on PostTrainBench.
- $0.30 input, $1.20 output and $0.06 cache read per million tokens on OpenRouter; MiniMax's API doubles the rate above 512K input tokens.
- Serving recipes for SGLang, vLLM, Transformers, KTransformers, unsloth and ATOM.

## Limitations
- 2.0% on Terminal-Bench 4.0 and an Omniscience Index of -5.5 on AA.
- MiniMax's reference deployment is eight B200 GPUs on an experimental SGLang build, validated for 1K to 128K inputs and not for video.
- Commercial use requires a "Built with MiniMax M3" notice, a one-time notice to MiniMax, and written authorisation above US$20 million yearly revenue.
- MiniMax-M3.1-Flash (2026-10-19) scores 28.9 on AA's index at half the API price.

## Good for
- Long-context work over documents, code and video.
- Agentic search and tool use.
- Self-hosted multimodal deployments where the licence terms fit.
