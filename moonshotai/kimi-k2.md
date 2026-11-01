---
id: moonshotai/kimi-k2
name: Kimi K2 0711
owned_by: moonshotai
type: llm
description: Kimi K2 Instruct (0711) is Moonshot AI's first open-weight 1T-parameter mixture-of-experts model (32B active), a non-thinking text model built for tool use and agentic coding with a 128K-token context.
aliases: [kimi-k2-0711-preview, moonshotai/Kimi-K2-Instruct]
context_length: 131072
max_output_tokens: 98304
capabilities: [tool_calling]
supported_parameters: [frequency_penalty, max_tokens, presence_penalty, repetition_penalty, seed, stop, temperature, tool_choice, tools, top_k, top_p]
architecture:
  input_modalities: [text]
  output_modalities: [text]
  tokenizer: Other
open_weights: true
license: Modified MIT
release_date: "2025-07-11"
knowledge_cutoff: "2024-12"
pricing:
  input: 0.57
  output: 2.3
benchmarks:
  gpqa_diamond: 76.6
  humanitys_last_exam: 7.4
  ifbench: 41.5
  long_context_reasoning: 53.0
  output_tokens_per_second: 47.6
  tau2_bench: 61.1
  terminal_bench_hard: 15.9
  time_to_first_token_seconds: 1.9
benchmark_variant: Kimi K2
sources:
  - https://openrouter.ai/moonshotai/kimi-k2
  - https://openrouter.ai/api/v1/models
  - https://artificialanalysis.ai/models/kimi-k2
  - https://huggingface.co/moonshotai/Kimi-K2-Instruct
  - https://huggingface.co/api/models/moonshotai/Kimi-K2-Instruct
  - https://huggingface.co/moonshotai/Kimi-K2-Instruct/raw/main/config.json
  - https://platform.kimi.ai/docs/models.md
retrieved: "2026-11-01"
---

# Kimi K2 0711

## Overview
Kimi K2 Instruct, released on 2025-07-11, is the post-trained chat model of Moonshot AI's Kimi K2. The Hugging Face card describes a mixture-of-experts model with 1T total and 32B activated parameters (384 experts, 8 per token, MLA attention), pre-trained on 15.5T tokens with the MuonClip optimiser. Moonshot calls it "reflex-grade", with no long thinking. It takes text and returns text, with a 128K context. Weights are on Hugging Face as `moonshotai/Kimi-K2-Instruct` under a Modified MIT licence. Moonshot's API id was `kimi-k2-0711-preview`; Moonshot lists it as discontinued on 2026-05-25, and Artificial Analysis marks the model deprecated in favour of Kimi K2 0905. OpenRouter still serves it through Novita (FP8).

## Strengths
- Moonshot reports 65.8% on SWE-bench Verified (single attempt, bash/editor tools), 53.7% on LiveCodeBench v6 and 89.8% on IFEval.
- Tool calling is a design focus; Moonshot reports 70.6% on Tau2 retail.
- Short time to first token: Artificial Analysis measured 1.9 s.

## Limitations
- No reasoning mode. Artificial Analysis measured 7.4% on Humanity's Last Exam and 53% on AA-LCR.
- Superseded by Kimi K2 0905 (256K context) and later Kimi models; no longer on Moonshot's own API.
- About 1T parameters in block-FP8, so self-hosting needs a multi-GPU cluster.
- OpenRouter lists no structured-output support.

## Good for
- Existing pipelines pinned to the original Kimi K2 behaviour.
- Agentic coding and tool-use workloads where latency matters more than deep reasoning.
