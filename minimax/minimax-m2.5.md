---
id: minimax/minimax-m2.5
name: MiniMax M2.5
owned_by: minimax
type: llm
description: MiniMax-M2.5 is MiniMax's February 2026 open-weight text model (230B total, 10B active parameters, reasoning always on), trained with reinforcement learning for coding, agentic search, tool use and office work, served in standard and Lightning speeds.
aliases: [MiniMax-M2.5, MiniMax-M2.5-highspeed, minimax/MiniMax-M2.5-lightning, minimax/minimax-m2.5-20260211, MiniMaxAI/MiniMax-M2.5, minimax.minimax-m2.5, azure_ai/FW-MiniMax-M2.5]
context_length: 204800
max_output_tokens: 32768
capabilities: [tool_calling, reasoning, structured_output]
supported_parameters: [frequency_penalty, include_reasoning, logit_bias, logprobs, max_tokens, min_p, presence_penalty, reasoning, repetition_penalty, response_format, seed, stop, structured_outputs, temperature, tool_choice, tools, top_k, top_logprobs, top_p]
architecture:
  input_modalities: [text]
  output_modalities: [text]
  tokenizer: Other
open_weights: true
license: MiniMax Model License
release_date: "2026-02-12"
pricing:
  input: 0.27
  output: 0.95
  cache_read: 0.03
benchmarks:
  gpqa_diamond: 84.8
  humanitys_last_exam: 20.5
  ifbench: 71.6
  long_context_reasoning: 73.3
  output_tokens_per_second: 34.7
  tau2_bench: 95.3
  terminal_bench_hard: 34.8
  time_to_first_token_seconds: 1.78
benchmark_variant: MiniMax-M2.5
sources:
  - https://openrouter.ai/minimax/minimax-m2.5
  - https://openrouter.ai/api/v1/models
  - https://artificialanalysis.ai/models/minimax-m2-5
  - https://huggingface.co/MiniMaxAI/MiniMax-M2.5
  - https://huggingface.co/api/models/MiniMaxAI/MiniMax-M2.5
  - https://huggingface.co/MiniMaxAI/MiniMax-M2.5/raw/main/config.json
  - https://huggingface.co/MiniMaxAI/MiniMax-M2.5/raw/main/LICENSE-MODEL
  - https://raw.githubusercontent.com/MiniMax-AI/MiniMax-M2.5/main/LICENSE-MODEL
  - https://raw.githubusercontent.com/MiniMax-AI/MiniMax-M2.5/main/LICENSE-CODE
  - https://www.minimax.io/news/minimax-m25
  - https://platform.minimax.io/docs/faq/models.md
  - https://platform.minimax.io/docs/release-notes/models.md
  - https://platform.minimax.io/docs/api-reference/text-anthropic-api.md
  - https://raw.githubusercontent.com/BerriAI/litellm/main/model_prices_and_context_window.json
retrieved: "2026-11-01"
---

# MiniMax M2.5

## Overview
MiniMax-M2.5 was released on 2026-02-12 (MiniMax news post; Artificial Analysis and the Hugging Face repo date agree, and the release notes say February 2026). MiniMax announced two versions of equal capability, M2.5 at about 50 tokens per second and M2.5-Lightning at 100; its API lists `MiniMax-M2.5` and `MiniMax-M2.5-highspeed`. It keeps the M2 architecture (230B total, 10B active parameters, text only, reasoning always on), trained with reinforcement learning in what MiniMax says were hundreds of thousands of real-world environments; it tends to write a spec before coding. OpenRouter lists 204,800 context and 32,768 output tokens. The repo's `LICENSE-MODEL` is the MiniMax Model License (version dated 2026-02-13) and `LICENSE-CODE` is MIT with a "MiniMax M2.5" attribution clause; the card metadata says Modified-MIT and AA lists MIT. MiniMax closed M2.5 to new users on 2026-10-19 and retires it on 2026-11-18; plan traffic now goes to M3.1-Flash.

## Strengths
- Artificial Analysis (MiniMax-M2.5): 95.3% on tau2-bench, 84.8% on GPQA Diamond, 73.3% on AA-LCR and 34.8% on Terminal-Bench Hard.
- MiniMax reports 80.2% SWE-bench Verified, 51.3% Multi-SWE-Bench and 76.3% BrowseComp with context management, and a 37% faster SWE-bench run than M2.1.
- Trained on more than ten programming languages; Word, Excel and PowerPoint deliverables are a stated focus.
- Lowest output price of the M2 series on OpenRouter: $0.27 input, $0.95 output, $0.03 cache read per million tokens. Also on Bedrock as `minimax.minimax-m2.5`.

## Limitations
- Text only; 32,768 output tokens on OpenRouter.
- Slow in AA's measurement: 34.7 output tokens per second and 1.78 s to first token.
- The licence differs between sources (see overview); read `LICENSE-MODEL` before commercial use.
- Retired from MiniMax's API on 2026-11-18.

## Good for
- Cost-sensitive coding, search and office-document agents on third-party hosts.
- Self-hosting with SGLang, vLLM, Transformers or KTransformers.
