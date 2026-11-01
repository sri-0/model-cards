---
id: openai/whisper-large-v3-turbo
name: Whisper Large V3 Turbo
owned_by: openai
type: llm
description: Whisper large-v3-turbo is OpenAI's 809M-parameter open-weight (MIT) speech recognition model, a pruned and fine-tuned large-v3 with 4 decoder layers instead of 32, much faster for a minor loss in quality.
aliases: [whisper-large-v3-turbo, groq/whisper-large-v3-turbo, watsonx/whisper-large-v3-turbo, cloudflare/@cf/openai/whisper-large-v3-turbo]
architecture:
  input_modalities: [audio]
  output_modalities: [transcription]
  tokenizer: GPT
open_weights: true
license: MIT
release_date: "2024-10-01"
sources:
  - https://huggingface.co/openai/whisper-large-v3-turbo
  - https://huggingface.co/api/models/openai/whisper-large-v3-turbo
  - https://huggingface.co/openai/whisper-large-v3-turbo/raw/main/config.json
  - https://artificialanalysis.ai/speech-to-text
  - https://artificialanalysis.ai/speech-to-text/models/whisper
  - https://openrouter.ai/openai/whisper-large-v3-turbo
  - https://openrouter.ai/api/v1/models?output_modalities=transcription
  - https://openrouter.ai/api/v1/models/openai/whisper-large-v3-turbo/endpoints
  - https://developers.openai.com/api/reference/resources/audio/subresources/transcriptions/methods/create
  - https://raw.githubusercontent.com/BerriAI/litellm/main/model_prices_and_context_window.json
retrieved: "2026-11-01"
---

# Whisper Large V3 Turbo

## Overview
Whisper large-v3-turbo was published on Hugging Face as openai/whisper-large-v3-turbo on 2024-10-01, the release date Artificial Analysis also gives, under the MIT licence (large-v3 itself is Apache-2.0). The model card describes it as a fine-tuned version of a pruned large-v3: the same model with the decoder cut from 32 layers to 4, giving 809M parameters, "way faster" output and a minor quality degradation. It keeps large-v3's 32-layer encoder, 128 mel bins and 30-second window, transcribes and translates speech into English, and returns sentence or word timestamps in transformers. OpenAI's own API does not serve it. OpenRouter lists it on its transcription API as openai/whisper-large-v3-turbo, routed to DeepInfra and Groq; its model page gives $0.000003 per second.

## Strengths
- Artificial Analysis AA-WER v2 (read 2026-11-01) on Groq: 4.6% (3.5% AA-AgentTalk, 4.0% VoxPopuli-Cleaned-AA, 7.5% Earnings22-Cleaned-AA) at a 277.6 median speed factor and $0.67 per 1,000 minutes.
- That is 0.5 points behind large-v3's best host (4.1% on fal.ai, $1.15 per 1,000 minutes).
- About half the parameters of large-v3 (809M against 1,550M).
- MIT licence for the weights.

## Limitations
- Hosting matters: Telnyx's build scores 5.5% at a 37.0 speed factor and $15 per 1,000 minutes.
- Inherits Whisper's 30-second receptive field, so long audio needs chunked or sequential decoding.
- Can output words that were not spoken and repeat itself; accuracy varies by language and accent.
- No diarization; the model card publishes no benchmark of its own.

## Good for
- Fast, low-cost batch transcription on hosted Whisper providers.
- Local or edge transcription where large-v3 is too slow.
- Replacing large-v3 where throughput matters more than the last half-point of WER.
