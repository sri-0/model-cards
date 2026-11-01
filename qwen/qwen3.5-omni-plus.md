---
id: qwen/qwen3.5-omni-plus
name: Qwen3.5 Omni Plus
owned_by: qwen
type: llm
description: "Qwen3.5-Omni-Plus is the larger of Alibaba's hosted Qwen3.5-Omni models, taking text, image, audio and video input and returning text or streamed speech, with a 262K-token context, speech input in 113 languages and dialects, voice cloning and web search."
aliases: [qwen3.5-omni-plus, qwen3.5-omni-plus-2026-03-15]
context_length: 262144
max_output_tokens: 65536
capabilities: [tool_calling, vision, structured_output]
architecture:
  input_modalities: [text, image, audio, video]
  output_modalities: [text, audio]
open_weights: false
license: proprietary
release_date: "2026-03-30"
benchmarks:
  gpqa_diamond: 82.6
  humanitys_last_exam: 14.9
  ifbench: 51.2
  long_context_reasoning: 63.7
  mmmu_pro: 70.5
  output_tokens_per_second: 104.1
  tau2_bench: 88.3
  terminal_bench_hard: 21.2
  time_to_first_token_seconds: 2.09
benchmark_variant: Qwen3.5 Omni Plus
sources:
  - https://artificialanalysis.ai/models/qwen3-5-omni-plus
  - https://www.alibabacloud.com/help/en/model-studio/qwen3-5-omni-plus
  - https://www.alibabacloud.com/help/en/model-studio/qwen-omni
  - https://www.alibabacloud.com/help/en/model-studio/models
  - https://www.alibabacloud.com/help/en/model-studio/model-pricing
  - https://www.alibabacloud.com/help/en/model-studio/newly-released-models
  - https://arxiv.org/abs/2604.15804
  - https://openrouter.ai/api/v1/models
retrieved: "2026-11-01"
---

# Qwen3.5 Omni Plus

## Overview
Qwen3.5-Omni-Plus is the larger of the two Qwen3.5-Omni models on Alibaba Cloud Model Studio (`qwen3.5-omni-plus`, currently the 2026-03-15 snapshot); weights are not published and OpenRouter does not list it. The technical report describes a Thinker-Talker design on a Hybrid Attention mixture-of-experts with hundreds of billions of parameters, trained on over 100 million hours of audio-visual data. It accepts any mix of text, images, audio and video in one request and streams text plus speech; requests must set `stream=True`. Model Studio gives a 262,144-token context, 196,608 input and 65,536 output tokens. Its Qwen-Omni guide lists up to 3 hours of audio or 1 hour of video, speech input in 113 languages and dialects, speech output in 36 and 55 voices, with voice cloning on the stable id; the model page claims over 10 hours of audio. There is no thinking mode. Function calling and JSON-object output are documented for China (Beijing) only; web search works in Beijing and Singapore. Singapore prices per million tokens: $1.40 text, image or video input, $11 audio input, $8.30 text output and $44 audio output. Model Studio dates it 2026-03-30 in China and 2026-03-26 in Singapore.

## Strengths
- Qwen reports state-of-the-art results on 215 audio and audio-visual subtasks, ahead of Gemini 3.1 Pro on key audio tasks.
- Artificial Analysis (Qwen3.5 Omni Plus): 88.3% tau2-bench, 82.6% GPQA Diamond, 70.5% MMMU-Pro; 104.1 tokens per second, 2.09 s to first token.

## Limitations
- No reasoning mode; AA measured 14.9% on Humanity's Last Exam.
- Tool calling and structured output in Beijing only.
- Streaming only; dated snapshots cannot use custom voices.

## Good for
- Voice assistants that need spoken replies.
- Audio-visual captioning and analysis; Model Studio points text-only analysis to qwen3.8-omni-flash.
