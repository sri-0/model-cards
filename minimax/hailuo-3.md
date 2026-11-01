---
id: minimax/hailuo-3
name: MiniMax H3
owned_by: minimax
type: video
description: MiniMax H3 is MiniMax's current flagship video model, a 33B open-weight omni-modal transformer that turns text, image, video and audio context into 4-15 second clips with native stereo audio at 768p or 2K.
aliases: [MiniMax-H3, minimax/MiniMax-H3, MiniMaxAI/MiniMax-H3, Comfy-Org/MiniMax-H3, hailuo-3, hailuo3, runwayml/hailuo3, fal_ai/minimax/h3/text-to-video, fal_ai/minimax/h3/reference-to-video]
capabilities: [vision]
supported_parameters: [max_tokens, temperature, top_p]
architecture:
  input_modalities: [text, image, video, audio]
  output_modalities: [video]
  tokenizer: Other
open_weights: true
license: MiniMax H3 Community License Agreement
release_date: "2026-07-31"
sources:
  - https://platform.minimax.io/docs/guides/models-intro
  - https://platform.minimax.io/docs/faq/models
  - https://platform.minimax.io/docs/release-notes/models
  - https://platform.minimax.io/docs/guides/video-generation
  - https://platform.minimax.io/docs/api-reference/video-generation-v2-create
  - https://platform.minimax.io/docs/api-reference/video-generation-v2-regeneration
  - https://platform.minimax.io/docs/guides/local-deploy-h3
  - https://platform.minimax.io/docs/pricing/overview
  - https://www.minimax.io/blog/minimax-h3
  - https://www.minimax.io/news/minimax-h3-open-source
  - https://huggingface.co/MiniMaxAI/MiniMax-H3
  - https://huggingface.co/api/models/MiniMaxAI/MiniMax-H3
  - https://huggingface.co/MiniMaxAI/MiniMax-H3/raw/main/LICENSE
  - https://openrouter.ai/minimax/hailuo-3
  - https://openrouter.ai/api/v1/models?output_modalities=all
  - https://artificialanalysis.ai/video/leaderboard/text-to-video
  - https://artificialanalysis.ai/video/leaderboard/image-to-video
  - https://artificialanalysis.ai/video/models/minimax-h3-768p
  - https://docs.dev.runwayml.com/guides/pricing/
  - https://raw.githubusercontent.com/BerriAI/litellm/main/model_prices_and_context_window.json
retrieved: "2026-11-01"
---

# MiniMax H3

## Overview
MiniMax H3 (`MiniMax-H3`) was released on 2026-07-31 and open-sourced on 2026-08-03 as `MiniMaxAI/MiniMax-H3`; the id is OpenRouter's (listed 2026-07-29). It has three parts: H3-Context-IR, a hosted service that turns multimodal instructions into a structured prompt; H3-Base, the open 33B dense Omni Transformer with a Qwen3-VL-32B encoder and video and stereo audio VAEs, which renders 768p video with sound; and H3-Regenerate-2K, a hosted pass that regenerates that result at 2K. The V2 endpoint (`POST /v2/video_generation`) takes text-to-video, first- and/or last-frame image-to-video, and reference-to-video with up to 9 images, 3 video clips and 3 audio clips. Output is 4-15 s at 24 fps, 21:9 to 9:16. Pay-as-you-go output costs $0.13 per second at 2K and $0.08 at 768p; input video bills at the same rate, images beyond five at $0.04 each, audio free.

## Strengths
- Artificial Analysis (read 2026-11-01, as MiniMax H3 (768p)): AA-Video-T2V v2.1 Elo 1161, third of 31 and the top open-weights model; AA-Video-I2V v2.1 Elo 1128, fourth of 29.
- Stable dialogue in 11 languages, including English, Chinese, Japanese and Arabic.
- Reference-driven editing and brand rendering, per MiniMax.
- Self-hosting through SGLang, vLLM, diffusers and ComfyUI from two BF16 checkpoints.

## Limitations
- The licence excludes the EU, UK, South Korea and US without a separate MiniMax licence, requires a "Powered by MiniMax H3" notice and written approval above US$20M yearly revenue.
- Self-hosted output stops at 768p; Context-IR and 2K regeneration stay hosted.
- Full attention only in the open release; about 108 GB of weights, 8 x B200 reference setup.
- Pay-as-you-go only (video packages exclude H3); prompts are capped at 7,000 characters.

## Good for
- Ads and product video that must reproduce text, logos and reference assets.
- Clips with synchronised sound in one step.
- Self-hosting or fine-tuning outside excluded territories.
