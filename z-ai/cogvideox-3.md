---
id: z-ai/cogvideox-3
name: CogVideoX-3
owned_by: z-ai
type: video
description: CogVideoX-3 is Z.ai's API-only video generation model for text-to-video, image-to-video and start-and-end-frame video, with output up to 4K, 60 fps and 10 seconds, plus optional AI sound effects.
aliases: [cogvideox-3]
architecture:
  input_modalities: [text, image]
  output_modalities: [video]
open_weights: false
release_date: "2025-07-15"
sources:
  - https://docs.z.ai/guides/video/cogvideox-3
  - https://docs.z.ai/api-reference/video/generate-video
  - https://docs.z.ai/guides/overview/pricing
  - https://docs.bigmodel.cn/cn/guide/models/video-generation/cogvideox-3
  - https://docs.bigmodel.cn/cn/update/new-releases
  - https://huggingface.co/api/models?author=zai-org
  - https://openrouter.ai/api/v1/models
retrieved: "2026-11-01"
---

# CogVideoX-3

## Overview
CogVideoX-3 is the only video generation model on Z.ai's pricing page, launched on Zhipu's platform on 2025-07-15. OpenRouter does not list it and Z.ai has not published its weights; the id is Z.ai's API id `cogvideox-3`. Generation is asynchronous: a request returns a task id, and the result is fetched later. Input is a prompt of up to 512 characters, an image (PNG or JPEG, up to 5 MB) or both; passing two images sets the first and last frames, which works in `speed` mode only. Options are `quality` or `speed` mode (default `speed`), AI sound effects (`with_audio`, off by default), resolutions from 1280x720 up to 3840x2160 including portrait and square sizes, 30 or 60 fps, and 5- or 10-second clips. Z.ai charges $0.2 per video.

## Strengths
- Z.ai says it gives clearer, more stable subjects with less distortion, even with large movements.
- Better instruction following and more realistic physical behaviour than earlier CogVideoX models, per Z.ai.
- Handles both photorealistic and 3D-style scenes.
- Start-and-end-frame mode creates a transition between two stills.

## Limitations
- Closed weights; the last open checkpoint in the family is CogVideoX1.5-5B from November 2024.
- Clips are 10 seconds at most.
- Z.ai publishes no quantitative benchmarks for it, only example clips.
- Start-and-end-frame mode cannot use `quality` mode.

## Good for
- Short product ads, tourism promos and social clips from a photo or a line of copy.
- Animating storyboards or character art into preview shots.
