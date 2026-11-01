---
id: z-ai/scail-2
name: SCAIL-2
owned_by: z-ai
type: video
description: SCAIL-2 is an open-weight (MIT) character animation model from Z.ai and Tsinghua University that animates a reference character from a driving video end to end, without pose skeletons or masks.
aliases: [zai-org/SCAIL-2]
architecture:
  input_modalities: [image, video]
  output_modalities: [video]
open_weights: true
license: MIT
release_date: "2026-06-09"
sources:
  - https://huggingface.co/zai-org/SCAIL-2
  - https://huggingface.co/api/models/zai-org/SCAIL-2
  - https://teal024.github.io/SCAIL-2
  - https://openrouter.ai/api/v1/models
retrieved: "2026-11-01"
---

# SCAIL-2

## Overview
SCAIL-2 is an open-source model for controlled character animation from Tsinghua University and Z.ai, with the paper arXiv 2606.10804 and code at `zai-org/SCAIL-2` on GitHub. Its Hugging Face repository was created on 2026-06-09. Given a reference character image and a driving video, it generates video of that character performing the motion. It also replaces characters in existing footage and handles several characters at once. Earlier methods relied on intermediate representations such as skeleton maps or inpainting masks; SCAIL-2 instead feeds latent visual information directly into a latent video diffusion model through a unified motion-transfer interface with dedicated mask channels and mode-specific RoPE. It was trained on MotionPair-60K, about 60K motion pairs synthesised with SCAIL-Preview, Wan-Animate and MoCha. The checkpoint bundles the Wan 2.1 VAE and UMT5-XXL text encoder. OpenRouter does not list it; the id follows the Hugging Face repo. Weights are MIT-licensed.

## Strengths
- End-to-end driving at 512p or 704p; pose-driven and replacement modes work best at 704p.
- The authors report emergent abilities beyond the teacher models: cross-identity replacement, animals as driving sources and zero-shot use of SAM3D-Body mesh renders as controls.
- Bias-aware DPO and in-context mask conditioning are part of the published training recipe.

## Limitations
- No quantitative benchmark results are published, only side-by-side examples.
- Height and width must both be divisible by 32.
- Inference uses the project's own code and FSDP checkpoint format, not diffusers.
- The project page marks its demo images and videos as academic and non-commercial.

## Good for
- Research on character animation and motion transfer.
- Animating a still character with motion from a reference video, or swapping a character into existing footage.
