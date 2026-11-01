---
id: openai/gpt-4o-transcribe-diarize
name: GPT-4o Transcribe Diarize
owned_by: openai
type: llm
description: GPT-4o Transcribe Diarize is OpenAI's deprecated speech-to-text model with built-in speaker diarization on the Transcription API, shutting down on 2027-02-26.
aliases: [gpt-4o-transcribe-diarize, azure/gpt-4o-transcribe-diarize]
context_length: 16000
max_output_tokens: 2000
architecture:
  input_modalities: [text, audio]
  output_modalities: [transcription]
open_weights: false
license: proprietary
knowledge_cutoff: "2024-06"
sources:
  - https://developers.openai.com/api/docs/models/gpt-4o-transcribe-diarize
  - https://developers.openai.com/api/docs/guides/speech-to-text
  - https://developers.openai.com/api/docs/guides/transcription
  - https://developers.openai.com/api/reference/resources/audio/subresources/transcriptions/methods/create
  - https://developers.openai.com/api/docs/pricing
  - https://developers.openai.com/api/docs/deprecations
  - https://developers.openai.com/api/docs/changelog
  - https://artificialanalysis.ai/speech-to-text
  - https://openrouter.ai/api/v1/models?output_modalities=transcription
  - https://raw.githubusercontent.com/BerriAI/litellm/main/model_prices_and_context_window.json
retrieved: "2026-11-01"
---

# GPT-4o Transcribe Diarize

## Overview
Deprecated: OpenAI announced on 2026-08-26 that gpt-4o-transcribe-diarize shuts down on 2027-02-26, together with whisper-1, gpt-4o-transcribe and gpt-4o-mini-transcribe, and points users to gpt-transcribe or gpt-live-transcribe. OpenAI's guides still name this model for speaker-labelled transcripts until shutdown and state that gpt-live-transcribe returns no speaker labels. OpenRouter does not list it, so the id is OpenAI's API id under the vendor prefix; OpenAI's docs give no release date. OpenAI describes it as an ASR model with built-in speaker diarization, available only on the Transcription API (/v1/audio/transcriptions), not in Realtime sessions. It has a 16,000-token context window, 2,000 output tokens and a June 2024 knowledge cutoff, and costs $2.50 per million audio input tokens and $10 per million output tokens (about $0.006 per minute).

## Strengths
- The diarized_json format returns segments with speaker, start and end fields.
- Up to four known-speaker reference clips (2 to 10 seconds each) map segments to named speakers.
- Streaming emits a segment event as each speaker segment completes.
- Build-tier limits of 5,000 RPM and 100,000 TPM.

## Limitations
- Deprecated; shuts down on 2027-02-26.
- No prompt, no logprobs and no timestamp_granularities; formats are json, text and diarized_json only.
- Audio longer than 30 seconds needs chunking_strategy set to auto or a VAD configuration.
- Streamed text deltas carry no speaker until the segment is final.
- Not on Artificial Analysis's speech-to-text board (read 2026-11-01).

## Good for
- Meeting, interview and call transcripts that need speaker labels until February 2027.
- Matching segments to known agents or hosts from short voice samples.
