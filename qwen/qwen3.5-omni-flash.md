---
id: qwen/qwen3.5-omni-flash
name: Qwen3.5 Omni Flash
owned_by: qwen
type: llm
description: "Qwen3.5-Omni-Flash is the faster, lower-priced of Alibaba's hosted Qwen3.5-Omni models, taking text, image, audio and video input and returning text or streamed speech, with a 262K-token context, speech input in 113 languages and dialects and voice cloning."
aliases: [qwen3.5-omni-flash, qwen3.5-omni-flash-2026-03-15]
context_length: 262144
max_output_tokens: 65536
capabilities: [tool_calling, vision]
architecture:
  input_modalities: [text, image, audio, video]
  output_modalities: [text, audio]
open_weights: false
license: proprietary
release_date: "2026-03-30"
benchmarks:
  gpqa_diamond: 74.2
  humanitys_last_exam: 7.6
  ifbench: 38.0
  long_context_reasoning: 52.0
  mmmu_pro: 64.7
  output_tokens_per_second: 238.1
  tau2_bench: 84.5
  terminal_bench_hard: 8.3
  time_to_first_token_seconds: 1.78
benchmark_variant: Qwen3.5 Omni Flash
sources:
  - https://artificialanalysis.ai/models/qwen3-5-omni-flash
  - https://www.alibabacloud.com/help/en/model-studio/qwen3-5-omni-flash
  - https://www.alibabacloud.com/help/en/model-studio/qwen-omni
  - https://www.alibabacloud.com/help/en/model-studio/model-pricing
  - https://www.alibabacloud.com/help/en/model-studio/newly-released-models
  - https://arxiv.org/abs/2604.15804
  - https://openrouter.ai/api/v1/models
retrieved: "2026-11-01"
---

# Qwen3.5 Omni Flash

## Overview
Qwen3.5-Omni-Flash is the lower-priced of the two Qwen3.5-Omni models on Alibaba Cloud Model Studio (`qwen3.5-omni-flash`, currently the 2026-03-15 snapshot); weights are not published and OpenRouter does not list it. The Qwen3.5-Omni technical report describes a Thinker-Talker design on a Hybrid Attention mixture-of-experts trained on over 100 million hours of audio-visual data. It accepts any mix of text, images, audio and video in one request and streams text plus speech; requests must set `stream=True`. Model Studio gives a 262,144-token context, 196,608 input and 65,536 output tokens. The Qwen-Omni guide lists up to 3 hours of audio or 1 hour of video, speech input in 113 languages and dialects, speech output in 36 and 55 voices, with voice cloning on the stable id. There is no thinking mode and no structured output. Function calling is documented for China (Beijing) only; web search works in Beijing and Singapore. Singapore prices per million tokens: $0.40 text, image or video input, $3 audio input, $2.20 text output and $11.90 audio output. Model Studio dates it 2026-03-30 in China and 2026-03-26 in Singapore.

## Strengths
- Per-token prices are 27-29% of Qwen3.5-Omni-Plus's.
- Artificial Analysis (Qwen3.5 Omni Flash): 238.1 tokens per second and 1.78 s to first token, 84.5% tau2-bench, 74.2% GPQA Diamond, 64.7% MMMU-Pro.

## Limitations
- Weaker reasoning: AA measured 7.6% on Humanity's Last Exam and 8.3% on Terminal-Bench Hard.
- Tool calling in Beijing only; no JSON output.
- Streaming only; dated snapshots cannot use custom voices.

## Good for
- Low-latency voice assistants and spoken customer service.
- High-volume audio and video description where cost matters.
