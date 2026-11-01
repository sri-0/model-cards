---
id: openai/gpt-4o-mini-transcribe
name: GPT-4o Mini Transcribe
owned_by: openai
type: llm
description: GPT-4o Mini Transcribe is OpenAI's deprecated speech-to-text model built on GPT-4o Mini, half the price of GPT-4o Transcribe and recommended by OpenAI over it, shutting down on 2027-02-26.
aliases: [gpt-4o-mini-transcribe, gpt-4o-mini-transcribe-2025-12-15, gpt-4o-mini-transcribe-2025-03-20, azure/gpt-4o-mini-transcribe]
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
  input: 1.25
  output: 5
sources:
  - https://developers.openai.com/api/docs/models/gpt-4o-mini-transcribe
  - https://developers.openai.com/api/docs/models
  - https://developers.openai.com/api/docs/pricing
  - https://developers.openai.com/api/docs/deprecations
  - https://developers.openai.com/api/docs/changelog
  - https://developers.openai.com/api/docs/guides/speech-to-text
  - https://developers.openai.com/api/reference/resources/audio/subresources/transcriptions/methods/create
  - https://developers.openai.com/blog/updates-audio-models
  - https://artificialanalysis.ai/speech-to-text
  - https://artificialanalysis.ai/speech-to-text/models/gpt-4o-audio
  - https://openrouter.ai/openai/gpt-4o-mini-transcribe
  - https://openrouter.ai/api/v1/models?output_modalities=transcription
  - https://raw.githubusercontent.com/BerriAI/litellm/main/model_prices_and_context_window.json
retrieved: "2026-11-01"
---

# GPT-4o Mini Transcribe

## Overview
GPT-4o Mini Transcribe was added to the Audio API on 2025-03-20 (OpenAI changelog). OpenRouter lists it on its transcription API under this id. The snapshots are gpt-4o-mini-transcribe-2025-03-20 and gpt-4o-mini-transcribe-2025-12-15, the default since 2026-01-13. OpenAI describes it as a speech-to-text model that uses GPT-4o Mini, with a lower word error rate and better language recognition than the original Whisper models. OpenAI's model page gives audio and text input, a 16,000-token context window, 2,000 output tokens and a June 2024 knowledge cutoff; the frontmatter follows OpenRouter's 128,000 and 115,200. It runs on /v1/audio/transcriptions and the Realtime API at $1.25 per million audio input tokens and $5 per million output tokens (about $0.003 per minute). The 2025-03-20 snapshot shuts down on 2027-01-20; the model was deprecated on 2026-08-26 and shuts down on 2027-02-26, replaced by gpt-transcribe or gpt-live-transcribe.

## Strengths
- Artificial Analysis AA-WER v2 (read 2026-11-01): 4.5%, with 3.7% on AA-AgentTalk, 2.4% on VoxPopuli-Cleaned-AA and 8.1% on Earnings22-Cleaned-AA, at a 45.7 median speed factor and $3.00 per 1,000 minutes.
- OpenAI says the 2025-12-15 snapshot lowers WER on Common Voice and FLEURS, produces about 90% fewer hallucinations on noisy audio than Whisper v2 and 70% fewer than earlier GPT-4o transcribe models, and is strongest in Mandarin, Hindi, Bengali, Japanese, Indonesian and Italian.
- Prompting, streaming and token logprobs; files up to 25 MB.

## Limitations
- Deprecated; shuts down on 2027-02-26.
- json is the only response format: no timestamps, subtitles, translation or speaker labels.
- Artificial Analysis chunks Earnings22 audio to about nine minutes for this model.
- Build-tier limits of 2,000 RPM and 150,000 TPM.

## Good for
- Low-cost batch transcription until early 2027.
- Realtime API transcription on the cheaper tier.
- Pinning gpt-4o-mini-transcribe-2025-12-15 for reproducible output.
