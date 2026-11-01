---
id: openai/gpt-transcribe
name: GPT Transcribe
owned_by: openai
type: llm
description: GPT Transcribe is OpenAI's recommended speech-to-text model for recorded audio, streamed file transcripts and committed Realtime turns, with prompt context, keyword hints and multiple language hints at $0.0045 per minute.
aliases: [gpt-transcribe, azure/gpt-transcribe, openai/gpt-transcribe-20260805]
architecture:
  input_modalities: [audio]
  output_modalities: [transcription]
  tokenizer: GPT
open_weights: false
license: proprietary
release_date: "2026-07-28"
sources:
  - https://openrouter.ai/openai/gpt-transcribe
  - https://openrouter.ai/api/v1/models?output_modalities=transcription
  - https://developers.openai.com/api/docs/models/gpt-transcribe
  - https://developers.openai.com/api/docs/guides/transcription
  - https://developers.openai.com/api/docs/guides/speech-to-text
  - https://developers.openai.com/api/docs/guides/realtime-transcription
  - https://developers.openai.com/api/docs/pricing
  - https://developers.openai.com/api/docs/changelog
  - https://developers.openai.com/api/docs/deprecations
  - https://artificialanalysis.ai/speech-to-text
  - https://artificialanalysis.ai/speech-to-text/models/openai-gpt-transcribe
  - https://raw.githubusercontent.com/BerriAI/litellm/main/model_prices_and_context_window.json
retrieved: "2026-11-01"
---

# GPT Transcribe

## Overview
OpenAI released GPT Transcribe on 2026-07-28 alongside GPT Live Transcribe (OpenAI changelog). OpenRouter lists it on its transcription API as openai/gpt-transcribe (canonical slug openai/gpt-transcribe-20260805). OpenAI's transcription guide recommends it for completed recordings, and it replaces whisper-1, gpt-4o-transcribe, gpt-4o-mini-transcribe and gpt-4o-transcribe-diarize, which shut down on 2027-02-26. It runs on /v1/audio/transcriptions, where it can stream partial text from a finished file, and in Realtime sessions over WebSocket, where it transcribes each committed audio turn and uses earlier turns as context. Requests can carry a free-form prompt, keyword hints and a languages list (it replaces the singular language field); the JSON response includes the detected languages. Files can be up to 25 MB in mp3, mp4, mpeg, mpga, m4a, wav or webm. OpenAI charges $0.0045 per minute of audio; OpenRouter's model page gives $0.000075 per second.

## Strengths
- Artificial Analysis AA-WER v2 (read 2026-11-01): 3.3%, with 2.2% on AA-AgentTalk, 2.7% on VoxPopuli-Cleaned-AA and 6.1% on Earnings22-Cleaned-AA, at a 45.1 median speed factor; best of the OpenAI models on the board (GPT-4o Transcribe 4.0%, whisper-1 4.1%).
- Cheaper than gpt-4o-transcribe and whisper-1 ($0.006 per minute).
- Keyword and multiple-language hints for domain terms and code-switching.
- High Build-tier limits: 5,000 RPM and 2M TPM, up to 30,000 RPM at Grow.

## Limitations
- OpenAI's guide still points to whisper-1 for word timestamps and srt or vtt subtitles, and to gpt-4o-transcribe-diarize for speaker labels.
- Behind the best models on the same board, such as Fun-Realtime-ASR-preview at 1.7%.
- The API rejects the whole request if a keyword contains angle brackets or line breaks, or if the prompt is too long.
- No published context length or knowledge cutoff.

## Good for
- New file-transcription integrations.
- Migrating off whisper-1 and the GPT-4o transcribe models before February 2027.
- Multilingual recordings with domain vocabulary.
