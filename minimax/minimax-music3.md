---
id: minimax/minimax-music3
name: MiniMax Music 3
owned_by: minimax
type: music
description: MiniMax Music 3 (API name music-3.0) is MiniMax's open-weight song generator that turns lyrics and a music description into complete songs of up to five minutes as 32 kHz stereo audio.
aliases: [MiniMaxAI/MiniMax-Music3, music-3.0, music-3.0-free]
architecture:
  input_modalities: [text]
  output_modalities: [audio]
open_weights: true
license: MiniMax-Music3 Community License
release_date: "2026-07-16"
sources:
  - https://platform.minimax.io/docs/guides/models-intro
  - https://platform.minimax.io/docs/faq/models
  - https://platform.minimax.io/docs/release-notes/models
  - https://platform.minimax.io/docs/guides/music-generation
  - https://platform.minimax.io/docs/api-reference/music-generation
  - https://platform.minimax.io/docs/guides/local-deploy
  - https://platform.minimax.io/docs/guides/local-deploy-music-3
  - https://platform.minimax.io/docs/pricing/overview
  - https://www.minimax.io/blog/minimax-music-3-0-next-generation-open-weights-production-ready-versatile-music-model
  - https://huggingface.co/MiniMaxAI/MiniMax-Music3
  - https://huggingface.co/api/models/MiniMaxAI/MiniMax-Music3
  - https://huggingface.co/MiniMaxAI/MiniMax-Music3/raw/main/LICENSE
  - https://artificialanalysis.ai/music/leaderboard/vocals
  - https://artificialanalysis.ai/music/leaderboard/instrumental
retrieved: "2026-11-01"
---

# MiniMax Music 3

## Overview
Music-3.0 reached MiniMax's API on 2026-07-16; the weights followed as `MiniMaxAI/MiniMax-Music3`, announced on 2026-08-13. OpenRouter does not list it; the id is the lower-cased Hugging Face repo under the `minimax/` prefix. An 8B Global LLM predicts the first of eight RVQ codebooks frame by frame for song-level structure, and a 0.6B Local LLM fills in the acoustic codes; their fused hidden states drive a 2.4B flow-matching module and a 123M Flow-VAE decoder. Input is lyrics with section tags such as `[Chorus]` plus a music description, ideally a structured caption of genre, BPM, key, vocal details and arrangement. Output is 32 kHz, 16-bit stereo WAV. It self-hosts on SGLang-Omni (`/v1/audio/speech`), diffusers or ComfyUI. On MiniMax's API, `music-3.0` cost $0.15 per song of up to five minutes, but paid music APIs closed to new users on 2026-08-20, the free tiers were discontinued, and the model list now shows music-3.0 as retired; MiniMax points users to these weights or MiniMax Audio.

## Strengths
- AA-Music-Vocal v1.1 (read 2026-11-01): Elo 1000, ninth of 13, above MiniMax Music 2.6 and 2.5+.
- Full songs, from intro to outro, kept coherent for up to five minutes, per MiniMax.
- The diffusers pipeline fits a 24 GB GPU, or 8 GB with slower layer-by-layer offloading.
- Commercial use is allowed with a visible "MiniMax-Music3" credit on the product.

## Limitations
- AA-Music-Instrumental v1.1: Elo 1000, 13th of 19, below Music 2.5+ and 2.6.
- CUDA only and non-streaming; prompts are capped at 5,000 tokens and output at 9,000 frames (25 per second).
- Tags and descriptions steer rather than guarantee tempo, key, instruments or structure.
- Written approval is needed above US$20M yearly revenue; the repo is about 57.4 GB and no minimum hardware is published.

## Good for
- Self-hosted song and jingle generation from lyrics.
- Teams leaving MiniMax's retired music API.
