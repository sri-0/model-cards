---
id: minimax/minimax-m2.7
name: MiniMax M2.7
owned_by: minimax
type: llm
description: MiniMax-M2.7 is MiniMax's March 2026 M2-series text model (230B total, 10B active parameters, reasoning always on) for agent harnesses, software engineering and office-document work, with weights under a non-commercial licence.
aliases: [MiniMax-M2.7, MiniMax-M2.7-highspeed, minimax/minimax-m2.7-20260318, MiniMaxAI/MiniMax-M2.7, "minimax-m2.7:cloud"]
context_length: 204800
max_output_tokens: 131072
capabilities: [tool_calling, reasoning]
supported_parameters: [frequency_penalty, include_reasoning, logit_bias, max_tokens, min_p, presence_penalty, reasoning, repetition_penalty, response_format, seed, stop, temperature, tool_choice, tools, top_k, top_p]
architecture:
  input_modalities: [text]
  output_modalities: [text]
  tokenizer: Other
open_weights: true
license: MiniMax-M2.7 License
release_date: "2026-03-18"
pricing:
  input: 0.3
  output: 1.2
  cache_read: 0.06
benchmarks:
  coding_index: 52.6
  agentic_index: 15.3
  gpqa_diamond: 87.4
  humanitys_last_exam: 29.6
  ifbench: 75.7
  long_context_reasoning: 78.3
  output_tokens_per_second: 41.7
  scicode: 50.1
  tau2_bench: 84.8
  terminal_bench_4: 0
  terminal_bench_hard: 39.4
  time_to_first_token_seconds: 1.72
benchmark_variant: MiniMax-M2.7
sources:
  - https://openrouter.ai/minimax/minimax-m2.7
  - https://openrouter.ai/api/v1/models
  - https://artificialanalysis.ai/models/minimax-m2-7
  - https://huggingface.co/MiniMaxAI/MiniMax-M2.7
  - https://huggingface.co/api/models/MiniMaxAI/MiniMax-M2.7
  - https://huggingface.co/MiniMaxAI/MiniMax-M2.7/raw/main/config.json
  - https://huggingface.co/MiniMaxAI/MiniMax-M2.7/raw/main/LICENSE
  - https://www.minimax.io/news/minimax-m27-en
  - https://platform.minimax.io/docs/faq/models.md
  - https://platform.minimax.io/docs/guides/local-deploy-m2-7.md
  - https://platform.minimax.io/docs/release-notes/models.md
  - https://platform.minimax.io/docs/api-reference/text-anthropic-api.md
  - https://ollama.com/library/minimax-m2.7
retrieved: "2026-11-01"
---

# MiniMax M2.7

## Overview
MiniMax-M2.7 was released on 2026-03-18 (MiniMax news post and release notes; Artificial Analysis agrees) as the `MiniMax-M2.7` and faster `MiniMax-M2.7-highspeed` API models; the weights followed on Hugging Face on 2026-04-09. It is the last M2-series release before M3: the same 230B-total, 10B-active mixture-of-experts design as M2 (62 layers, 256 experts with 8 routed per token, FP8 weights, 204,800 positions in config.json), text in and text out, reasoning always on. MiniMax calls it its first model to take part in its own development: an internal version tuned a coding scaffold over 100+ rounds for a 30% gain. OpenRouter lists a 204,800-token context and 131,072 output tokens. MiniMax closed M2.7 to new API users on 2026-10-19 and retires it on 2026-11-18; plan traffic now goes to MiniMax-M3.1-Flash.

## Strengths
- Artificial Analysis (MiniMax-M2.7): 87.4% on GPQA Diamond, 78.3% on AA-LCR, 75.7% on IFBench and 39.4% on Terminal-Bench Hard, the M2 series' best on each, plus 84.8% on tau2-bench.
- MiniMax reports 56.22% on SWE-Pro, 76.5 on SWE Multilingual, 57.0% on Terminal Bench 2 and an ELO of 1495 on GDPval-AA, with multi-round Word, Excel and PowerPoint editing.
- Native Agent Teams for multi-agent work; SGLang, vLLM and Transformers deployment guides; an NVIDIA NIM endpoint.
- $0.30 input, $1.20 output and $0.06 cache read per million tokens on OpenRouter.

## Limitations
- Text only.
- The weights licence (titled "NON-COMMERCIAL LICENSE"; MiniMax's docs call it the MiniMax-M2.7 License) requires prior written authorisation from MiniMax for any commercial use and a "Built with MiniMax M2.7" notice.
- 0% on Terminal-Bench 4.0 on AA, and 41.7 output tokens per second, a third of M2's measured speed.
- Retired from MiniMax's API on 2026-11-18.

## Good for
- Self-hosted coding and office-document agents for personal or research use.
- Existing M2.7 integrations on OpenRouter or third-party hosts until they move to M3.1-Flash.
