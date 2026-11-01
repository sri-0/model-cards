---
id: openai/gpt-4o-transcribe
name: GPT-4o Transcribe
owned_by: openai
type: llm
description: GPT-4o Transcribe is OpenAI's deprecated speech-to-text model built on GPT-4o, served on the transcription and Realtime APIs until it shuts down on 2027-02-26.
aliases: [gpt-4o-transcribe, azure/gpt-4o-transcribe]
context_length: 128000
max_output_tokens: 115200
architecture:
  input_modalities: [audio]
  output_modalities: [transcription]
  tokenizer: GPT
open_weights: false
license: proprietary
release_date: "2025-03-20"
knowledge_cutoff: "2024-06"
pricing:
  input: 2.5
  output: 10
sources:
  - https://developers.openai.com/api/docs/models/gpt-4o-transcribe
  - https://developers.openai.com/api/docs/models
  - https://developers.openai.com/api/docs/pricing
  - https://developers.openai.com/api/docs/deprecations
  - https://developers.openai.com/api/docs/changelog
  - https://developers.openai.com/api/docs/guides/speech-to-text
  - https://developers.openai.com/api/reference/resources/audio/subresources/transcriptions/methods/create
  - https://artificialanalysis.ai/speech-to-text
  - https://artificialanalysis.ai/speech-to-text/models/gpt-4o-audio
  - https://openrouter.ai/openai/gpt-4o-transcribe
  - https://openrouter.ai/api/v1/models?output_modalities=transcription
  - https://openrouter.ai/api/v1/models/openai/gpt-4o-transcribe/endpoints
  - https://raw.githubusercontent.com/BerriAI/litellm/main/model_prices_and_context_window.json
retrieved: "2026-11-01"
---

# GPT-4o Transcribe

## Overview
GPT-4o Transcribe was added to the Audio API on 2025-03-20 (OpenAI changelog); gpt-4o-transcribe is its only snapshot. OpenRouter lists it on its transcription API under this id. OpenAI describes it as a speech-to-text model that uses GPT-4o, with a lower word error rate and better language recognition than the original Whisper models. OpenAI's model page gives audio and text input, a 16,000-token context window, 2,000 output tokens and a June 2024 knowledge cutoff; the frontmatter follows OpenRouter's 128,000 and 115,200. It runs on /v1/audio/transcriptions and the Realtime API at $2.50 per million audio input tokens and $10 per million output tokens on both OpenAI and OpenRouter, which OpenAI estimates at $0.006 per minute. OpenAI deprecated it on 2026-08-26 with whisper-1, gpt-4o-mini-transcribe and gpt-4o-transcribe-diarize; all shut down on 2027-02-26, replaced by gpt-transcribe or gpt-live-transcribe.

## Strengths
- Artificial Analysis AA-WER v2 (read 2026-11-01): 4.0%, with 2.7% on AA-AgentTalk, 2.8% on VoxPopuli-Cleaned-AA and 7.7% on Earnings22-Cleaned-AA, at a 36.6 median speed factor; whisper-1 scores 4.1% and GPT-4o Mini Transcribe 4.5%.
- Prompting, streaming and token logprobs.
- Files up to 25 MB in mp3, mp4, mpeg, mpga, m4a, wav and webm.

## Limitations
- Deprecated; shuts down on 2027-02-26.
- json is the only response format: no srt, vtt, verbose_json or timestamps.
- No translation endpoint and no speaker labels (that is gpt-4o-transcribe-diarize).
- Artificial Analysis chunks Earnings22 audio to about nine minutes for this model because of its time limits.
- Twice the price of GPT-4o Mini Transcribe, which OpenAI's changelog (2026-01-13) recommends for the best results; GPT Transcribe scores 3.3% on the same board at $4.50 per 1,000 minutes.
- Build-tier limits of 2,000 RPM and 100,000 TPM.

## Good for
- Integrations pinned to this model until February 2027.
- Batch transcription where plain JSON text is enough.
- Realtime API transcription already built on it.
