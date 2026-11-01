---
id: mistralai/voxtral-small-24b-2507
name: Voxtral Small 24B 2507
owned_by: mistralai
type: llm
description: Voxtral Small is Mistral AI's 24B open-weight (Apache-2.0) speech and text model built on Mistral Small 3 that transcribes, translates and answers questions about audio.
aliases: [mistralai/Voxtral-Small-24B-2507, voxtral-small-2507, voxtral-small-latest, mistral/voxtral-small-2507, mistral/voxtral-small-latest, mistral.voxtral-small-24b-2507]
context_length: 32768
max_output_tokens: 26214
capabilities: [tool_calling, structured_output]
supported_parameters: [frequency_penalty, max_tokens, presence_penalty, response_format, seed, stop, structured_outputs, temperature, tool_choice, tools, top_p]
architecture:
  input_modalities: [text, audio, file]
  output_modalities: [text]
  tokenizer: Mistral
open_weights: true
license: Apache-2.0
release_date: "2025-07-15"
pricing:
  input: 0.1
  output: 0.3
  cache_read: 0.01
sources:
  - https://openrouter.ai/mistralai/voxtral-small-24b-2507
  - https://openrouter.ai/api/v1/models
  - https://huggingface.co/mistralai/Voxtral-Small-24B-2507
  - https://huggingface.co/api/models/mistralai/Voxtral-Small-24B-2507
  - https://docs.mistral.ai/getting-started/models
  - https://docs.mistral.ai/models/voxtral-small-25-07
  - https://docs.mistral.ai/studio/audio/overview
  - https://mistral.ai/news/voxtral
  - https://arxiv.org/abs/2507.13264
  - https://raw.githubusercontent.com/BerriAI/litellm/main/model_prices_and_context_window.json
retrieved: "2026-10-16"
---

# Voxtral Small 24B 2507

## Overview
Voxtral Small (API id voxtral-small-2507, alias voxtral-small-latest) was released on 2025-07-15 as Mistral's first audio-input instruct model. It adds a 640M-parameter audio encoder to Mistral Small 3, 24.3B parameters in total, and takes audio and text in one chat completion request. The 32k-token context covers about 30 minutes of audio for transcription or 40 minutes for understanding; language detection is automatic across English, Spanish, French, Portuguese, Hindi, German, Dutch and Italian, and a transcription mode runs on the audio transcriptions endpoint. Weights are on Hugging Face under Apache 2.0. Mistral's API charges $0.004 per minute of audio, or $0.1 per million input and $0.4 per million output tokens, against OpenRouter's $0.1 and $0.3 above.

## Strengths
- Mistral's paper reports 3.35% WER on FLEURS English and 8.58% on Mozilla Common Voice English, against 4.00% and 22.91% for Whisper large-v3.
- Speech translation: 57.3 BLEU on FLEURS en-fr and 56.6 on de-en, the best in Mistral's comparison with GPT-4o mini Audio and Gemini 2.5 Flash.
- 88.4% on spoken Openbook QA and 89.7% on spoken GSM8K in the same paper.
- Function calling from spoken requests and multi-turn, multi-clip audio chat.

## Limitations
- System prompts are not supported; function calling is labelled experimental.
- Needs about 55 GB of GPU memory in bf16, vLLM 0.10.0 or transformers 4.54.0 or later, and mistral-common 1.8.1 or later.
- Audio per request is capped by the 32k context; longer recordings need chunking or Voxtral Mini Transcribe 2.
- Artificial Analysis publishes no Intelligence Index for it.

## Good for
- Transcription with summaries, structured extraction or question answering in one call.
- Voice-driven agents that trigger tools from spoken intent.
- Self-hosted multilingual speech pipelines for European languages and Hindi.
