---
id: z-ai/glm-tts
name: GLM-TTS
owned_by: z-ai
type: tts
description: GLM-TTS is Z.ai's open-weight (MIT) zero-shot text-to-speech system, a Llama-architecture text-to-token model plus a flow-matching decoder, with voice cloning from a few seconds of audio and streaming output.
aliases: [glm-tts, zai-org/GLM-TTS]
architecture:
  input_modalities: [text, audio]
  output_modalities: [audio]
open_weights: true
license: MIT
release_date: "2025-12-11"
sources:
  - https://huggingface.co/zai-org/GLM-TTS
  - https://huggingface.co/api/models/zai-org/GLM-TTS
  - https://github.com/zai-org/GLM-TTS
  - https://docs.bigmodel.cn/cn/guide/models/sound-and-video/glm-tts
  - https://docs.bigmodel.cn/cn/update/new-releases
  - https://docs.z.ai/guides/overview/pricing
  - https://openrouter.ai/api/v1/models
retrieved: "2026-11-01"
---

# GLM-TTS

## Overview
GLM-TTS was open-sourced on 2025-12-11, with a technical report (arXiv 2512.14291) on 2025-12-17. It works in two stages: a Llama-architecture language model turns text into speech tokens, then a flow-matching model turns the tokens into a mel-spectrogram and a vocoder produces the waveform. Speaker features come from a 3-10 second prompt clip, so voices clone without fine-tuning. A multi-reward reinforcement learning stage (GRPO, with similarity, CER, emotion and laughter rewards) improves expressiveness, and a "Phoneme-in" mode mixes phonemes into the text to fix polyphones and rare characters. It mainly supports Chinese, with mixed English. Zhipu's China platform serves it as `glm-tts` with preset voices, streaming and a companion GLM-TTS-Clone voice-cloning model; Z.ai's international pricing page does not list it. OpenRouter does not list it; the id follows the Hugging Face repo. Code and weights are MIT-licensed.

## Strengths
- On seed-tts-eval (Chinese), Z.ai reports a CER of 1.03 for GLM-TTS and 0.89 for the RL-tuned GLM-TTS_RL, with speaker similarity of 76.1 and 76.4.
- Zhipu says first audio arrives in under 400 ms on its streaming API, with adjustable speed and volume.
- Runs on GPUs or Huawei Ascend NPUs.

## Limitations
- The README still lists the RL-optimised weights as coming soon, so the 0.89 CER may not apply to the released checkpoint.
- Chinese-first; English is supported mainly inside mixed Chinese text.
- Needs Z.ai's own inference scripts and Python 3.10-3.12; no OpenAI-compatible speech server is documented for self-hosting.

## Good for
- Expressive Chinese narration, audiobooks and customer-service voices.
- Zero-shot voice cloning from a short reference clip.
- Education and reading apps that need exact pronunciation control.
