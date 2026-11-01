---
id: moonshotai/kimi-k3.1-pro
name: Kimi K3.1 Pro
owned_by: moonshotai
type: llm
description: Kimi K3.1 Pro is Moonshot AI's flagship multimodal reasoning model, a post-trained successor to Kimi K3 for long-horizon coding, 3D creation and financial research, with a 1M-token context window.
aliases: [kimi-k3.1-pro, kimi-k3.1-pro-highspeed, moonshot/kimi-k3.1-pro, moonshotai/kimi-k3.1-pro-20261023]
context_length: 1048576
max_output_tokens: 943718
capabilities: [tool_calling, reasoning, vision, structured_output]
supported_parameters: [frequency_penalty, include_reasoning, logprobs, max_tokens, presence_penalty, reasoning, reasoning_effort, response_format, stop, structured_outputs, tool_choice, tools, top_logprobs]
architecture:
  input_modalities: [text, image, video]
  output_modalities: [text]
  tokenizer: Other
open_weights: false
release_date: "2026-10-23"
pricing:
  input: 2
  output: 10
  cache_read: 0.2
benchmarks:
  humanitys_last_exam: 52.5
  intelligence_index: 46.0
  long_context_reasoning: 86.3
  mmmu_pro: 83.9
  omniscience_index: 29.9
  output_tokens_per_second: 30.9
  scicode: 60.8
  terminal_bench_4: 67.2
  time_to_first_token_seconds: 3.27
benchmark_variant: Kimi K3.1 Pro
sources:
  - https://openrouter.ai/moonshotai/kimi-k3.1-pro
  - https://openrouter.ai/api/v1/models
  - https://artificialanalysis.ai/models/kimi-k3-1-pro
  - https://platform.kimi.ai/docs/guide/kimi-k3-1-pro-quickstart.md
  - https://platform.kimi.ai/docs/models.md
  - https://platform.kimi.ai/docs/pricing/chat.md
  - https://platform.kimi.ai/docs/api/models-overview.md
  - https://huggingface.co/api/models?author=moonshotai
  - https://raw.githubusercontent.com/BerriAI/litellm/main/model_prices_and_context_window.json
retrieved: "2026-11-01"
---

# Kimi K3.1 Pro

## Overview
Kimi K3.1 Pro, released on 2026-10-23, is the first model of Moonshot AI's K3.1 series. Moonshot describes it as a post-trained version of Kimi K3 with substantially more post-training compute, and calls it a 3T-class model; Artificial Analysis lists 2.8T total and 104B active parameters. It accepts text, images and video and has a 1M-token context window. Thinking is always on: `reasoning_effort` takes `low`, `high` or `max` (default `max`), and `temperature`, `top_p` and the penalties are fixed. Moonshot says the full weights will be released by 4 November 2026; on the retrieval date none were on Hugging Face and Artificial Analysis lists it as not open-weight. `kimi-k3.1-pro-highspeed` is the same model at about 2-3 times the speed.

## Strengths
- Artificial Analysis Intelligence Index 46.0, with 67.2% on Terminal-Bench 4.0 and 52.5% on Humanity's Last Exam.
- Strong long-context and visual results: 86.3% on AA-LCR and 83.9% on MMMU-Pro.
- Moonshot reports state-of-the-art results on OfficeQA Pro v2 and SpreadsheetBench v2, and a claim-level hallucination rate that fell from 23.35% for K3 to 6.85% on its stress test.
- Writes and runs Blender, CAD and game-engine scripts for 3D work, per Moonshot.

## Limitations
- Slow: Artificial Analysis measured 30.9 output tokens per second and 3.27 s to first token.
- Thinking cannot be disabled, and vision input does not accept public image URLs (base64 or uploaded files only).
- Moonshot's own K3.1 Pro page still carries unfilled benchmark placeholders, so its headline numbers are not yet published.
- Unlocked on Moonshot's API only after a top-up.

## Good for
- Long-horizon agentic coding and terminal work.
- Financial research, spreadsheet modelling and document-heavy analysis over very long inputs.
- Parametric 3D modelling and game or web scenes built from code.
