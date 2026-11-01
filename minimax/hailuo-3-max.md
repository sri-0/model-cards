---
id: minimax/hailuo-3-max
name: MiniMax H3 Max
owned_by: minimax
type: video
description: MiniMax H3 Max is a speed-focused variant of MiniMax H3, post-trained by fal and served on MiniMax's V2 video API, generating 5-15 second clips at 480p or 768p from text, keyframes or image, video and audio references.
aliases: [MiniMax-H3-Max, minimax/MiniMax-H3-Max, hailuo-3-max, h3_max, minimax/h3-max/text-to-video, minimax/h3-max/image-to-video, minimax/h3-max/reference-to-video]
capabilities: [vision]
supported_parameters: [max_tokens, temperature, top_p]
architecture:
  input_modalities: [text, image]
  output_modalities: [video]
  tokenizer: Other
open_weights: false
license: proprietary
release_date: "2026-08-26"
sources:
  - https://platform.minimax.io/docs/faq/models
  - https://platform.minimax.io/docs/release-notes/models
  - https://platform.minimax.io/docs/api-reference/video-generation-v2-create
  - https://platform.minimax.io/docs/pricing/overview
  - https://fal.ai/models/minimax/h3-max/text-to-video/llms.txt
  - https://fal.ai/learn/devs/minimax-h3-vs-minimax-h3-max
  - https://openrouter.ai/minimax/hailuo-3-max
  - https://openrouter.ai/api/v1/models?output_modalities=all
  - https://artificialanalysis.ai/video/leaderboard/text-to-video
  - https://artificialanalysis.ai/video/leaderboard/image-to-video
  - https://docs.dev.runwayml.com/guides/pricing/
  - https://raw.githubusercontent.com/BerriAI/litellm/main/model_prices_and_context_window.json
retrieved: "2026-11-01"
---

# MiniMax H3 Max

## Overview
`MiniMax-H3-Max` is one of four `model` values on MiniMax's V2 video endpoint (`POST /v2/video_generation`), described there as the fast generation variant and in MiniMax's model list as a high-speed model post-trained on H3. fal says its research team post-trained it from the open H3 weights for prompt adherence and aesthetics, and Artificial Analysis credits it to Fal; OpenRouter, whose id this card uses (slug dated 2026-09-01), calls it a MiniMax model released jointly with fal.ai and lists text and image input only. MiniMax gives no release date, so the date above is Artificial Analysis's. It covers text-to-video, first- and/or last-frame image-to-video and reference-to-video with image, video and audio inputs, at 480p or 768p for 5-15 seconds. It is the only model that takes `extra.prompt_expansion_mode` (`disabled`, `balanced` by default, or `quality`). Pay-as-you-go prices are $0.08 per output second at 768p and $0.05 at 480p; input video costs $0.143/s at 768p and $0.0553/s at 480p, images beyond the first two cost $0.074 each and audio input is free.

## Strengths
- Artificial Analysis (read 2026-11-01): second of 36 on AA-Video-T2V-Silent v2.1 (Elo 1140) and third of 33 on AA-Video-I2V-Silent v2.1 (Elo 1122); seventh of 31 on AA-Video-T2V v2.1 (Elo 1149) and eighth of 29 on AA-Video-I2V v2.1 (Elo 1117).
- Same 768p output price as H3, plus a 480p tier.
- Prompt expansion can be reduced or switched off per request.

## Limitations
- No 2K output and no 4-second clips.
- Input video and extra images cost more than on H3, and only two images per task are free.
- No published weights and no MiniMax release note or technical report.
- Pay-as-you-go only; video packages do not cover the H3 family.

## Good for
- Fast drafts of shots that will be finalised on H3.
- Short social clips at 480p or 768p.
