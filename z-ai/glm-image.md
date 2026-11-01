---
id: z-ai/glm-image
name: GLM-Image
owned_by: z-ai
type: image
description: GLM-Image is Z.ai's open-weight (MIT) image generation and editing model, a 9B autoregressive generator with a 7B diffusion decoder, aimed at text-heavy and knowledge-intensive images such as posters and diagrams.
aliases: [glm-image, zai-org/GLM-Image]
architecture:
  input_modalities: [text, image]
  output_modalities: [image]
open_weights: true
license: MIT
release_date: "2026-01-14"
sources:
  - https://huggingface.co/zai-org/GLM-Image
  - https://huggingface.co/api/models/zai-org/GLM-Image
  - https://docs.z.ai/guides/image/glm-image
  - https://docs.z.ai/api-reference/image/generate-image
  - https://docs.z.ai/guides/overview/pricing
  - https://docs.z.ai/release-notes/new-released
  - https://openrouter.ai/api/v1/models
retrieved: "2026-11-01"
---

# GLM-Image

## Overview
GLM-Image was released on 2026-01-14 as Z.ai's flagship image model; Z.ai says it was trained entirely on domestic Chinese chips. It combines a 9B autoregressive generator, initialised from GLM-4-9B-0414 with visual tokens added to the vocabulary, and a 7B single-stream DiT decoder with a Glyph Encoder for accurate text strokes. The generator first writes about 256 compact tokens, then expands to 1K-4K tokens for 1K-2K images. Post-training uses GRPO with separate feedback for semantics and for fine detail. One model does text-to-image and image-to-image (editing, style transfer, subject and identity consistency). On Z.ai's API, `glm-image` costs $0.015 per image and returns an image URL; width and height run from 512 to 2048 px in multiples of 32. OpenRouter does not list it; the id follows the Hugging Face repo. Weights are MIT, with Apache-2.0 tokenizer and ViT parts from X-Omni.

## Strengths
- Z.ai reports first place among open models on CVTG-2K (word accuracy 0.9116, NED 0.9557) and LongText-Bench (0.9524 English, 0.9788 Chinese).
- Strong at posters, slides, science illustrations, multi-panel comics and e-commerce images that carry a lot of text.
- Runs in transformers plus diffusers, or SGLang with OpenAI-style image endpoints.

## Limitations
- Z.ai says inference optimisation is still limited and costly; with CPU offload it needs about 23 GB of GPU memory and runs slower.
- Text to render must be in quotation marks, and Z.ai recommends rewriting prompts with GLM-4.7 for best results.
- General image quality is on par with mainstream latent diffusion models rather than ahead.

## Good for
- Marketing and commercial designs that need legible Chinese or English text.
- Educational and technical diagrams.
- Self-hosted image generation under a permissive licence.
