---
id: qwen/qwen-tts-realtime
name: Qwen-TTS-Realtime
owned_by: qwen
type: tts
description: "Qwen-TTS-Realtime is a Model Studio Qwen speech synthesis model with bidirectional context awareness for low-latency, multi-voice, dialect and long-text bidirectional streaming in Chinese and English."
aliases: [qwen-tts-realtime-latest, qwen-tts-realtime-2025-07-15]
context_length: 8192
max_output_tokens: 7680
architecture:
  input_modalities: [text]
  output_modalities: [speech]
open_weights: false
license: proprietary
release_date: "2025-07-16"
sources:
  - https://www.alibabacloud.com/help/en/model-studio/newly-released-models
  - http://web.archive.org/web/20260606135246/https://www.alibabacloud.com/help/en/model-studio/models
  - http://web.archive.org/web/20261007164426/https://www.alibabacloud.com/help/en/model-studio/model-pricing
  - http://web.archive.org/web/20261013105614/https://www.alibabacloud.com/help/en/model-studio/model-pricing
  - https://www.alibabacloud.com/help/en/model-studio/model-pricing
  - https://openrouter.ai/api/v1/models
retrieved: "2026-11-01"
---

# Qwen-TTS-Realtime

## Overview
Status: Model Studio's current pricing page no longer lists qwen-tts-realtime; archived pricing pages show it on 2026-10-07 but not on 2026-10-13, and the deprecation page names no date for it. Qwen-TTS-Realtime (Model Studio id `qwen-tts-realtime`, documented as equivalent to `qwen-tts-realtime-2025-07-15`, with a `qwen-tts-realtime-latest` alias) appears in Model Studio's release table from 2025-07-16; no weights are published and OpenRouter does not list it, so the id is the DashScope model id. Model Studio describes a Qwen speech synthesis model with bidirectional context awareness that generates low-latency, high-fidelity speech across several voices, dialects and long texts over bidirectional streaming: text arrives in segments and audio streams back. It uses the default voices only, not cloned or designed voices, and speaks Chinese and English. The archived models page gives an 8,192-token context with 512 input and 7,680 output tokens. It was priced at $0.345 input and $1.721 output per million tokens in China (Beijing).

## Strengths
- Bidirectional streaming for live synthesis of generated text.
- Dialect voices, per Model Studio.

## Limitations
- No longer listed for sale on Model Studio.
- Chinese and English only; default voices only.

## Good for
- Interpreting older real-time integrations that used qwen-tts-realtime.
