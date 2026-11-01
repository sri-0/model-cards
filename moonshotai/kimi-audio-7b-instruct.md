---
id: moonshotai/kimi-audio-7b-instruct
name: Kimi-Audio-7B-Instruct
owned_by: moonshotai
type: llm
description: Kimi-Audio-7B-Instruct is Moonshot AI's open-weight (MIT) audio foundation model for speech recognition, audio understanding and end-to-end speech conversation, returning text and speech.
aliases: [moonshotai/Kimi-Audio-7B-Instruct]
context_length: 8192
architecture:
  input_modalities: [text, audio]
  output_modalities: [text, audio]
open_weights: true
license: MIT
release_date: "2025-04-25"
sources:
  - https://huggingface.co/moonshotai/Kimi-Audio-7B-Instruct
  - https://huggingface.co/api/models/moonshotai/Kimi-Audio-7B-Instruct
  - https://huggingface.co/moonshotai/Kimi-Audio-7B-Instruct/raw/main/config.json
  - https://github.com/MoonshotAI/Kimi-Audio
  - https://openrouter.ai/api/v1/models
retrieved: "2026-11-01"
---

# Kimi-Audio-7B-Instruct

## Overview
Kimi-Audio is Moonshot AI's universal audio model; the instruct checkpoint and inference code were released on 2025-04-25. One model handles speech recognition, audio question answering, audio captioning, speech emotion recognition, sound event and scene classification, and spoken conversation. Audio goes in as continuous acoustic features plus discrete semantic tokens; an LLM core initialised from Qwen2.5-7B has parallel heads for text and audio tokens, and a chunk-wise streaming flow-matching detokenizer turns audio tokens into speech. Moonshot pre-trained it on more than 13 million hours of speech, music and sound plus text. OpenRouter does not list it; the id follows the Hugging Face repo. The weights are MIT-licensed; code derived from Qwen2.5-7B is Apache 2.0.

## Strengths
- Moonshot reports word error rates of 1.28 and 2.42 on LibriSpeech test-clean and test-other, and 0.60 on AISHELL-1.
- Broad audio understanding: 94.85 on VocalSound, 79.84 on CochlScene test and 61.68, 73.27 and 60.66 on the MMAU music, sound and speech splits.
- Spoken chat: a 76.93 VoiceBench average in Moonshot's evaluation.
- Moonshot publishes an evaluation toolkit (Kimi-Audio-Evalkit) to reproduce the numbers.

## Limitations
- Runs through Moonshot's own `kimia_infer` package or Docker image rather than standard transformers or vLLM serving.
- The model card lists English and Chinese only.
- Hugging Face lists about 9.8B parameters in the checkpoint, more than the 7B in its name.
- No OpenAI-compatible transcription or speech endpoint is documented.

## Good for
- English and Chinese speech recognition.
- Audio classification, captioning and question answering in one model.
- Research prototypes of end-to-end voice assistants.
