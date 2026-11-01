---
id: mistralai/shieldstral-1.0-3b
name: Shieldstral 1.0 3B
owned_by: mistralai
type: llm
description: Shieldstral 1.0 is Mistral AI's 3.8B open-weight (Apache-2.0) policy-adaptive safety classifier that answers a natural-language yes/no moderation question about text, images or both with a single calibrated score.
aliases: [mistralai/Shieldstral-1.0-3B]
context_length: 32768
capabilities: [vision]
architecture:
  input_modalities: [text, image]
  output_modalities: [text]
open_weights: true
license: Apache-2.0
release_date: "2026-08-04"
sources:
  - https://huggingface.co/mistralai/Shieldstral-1.0-3B
  - https://huggingface.co/api/models/mistralai/Shieldstral-1.0-3B
  - https://huggingface.co/mistralai/Shieldstral-1.0-3B/raw/main/config.json
  - https://huggingface.co/mistralai/Shieldstral-1.0-3B/raw/main/README.md
  - https://docs.mistral.ai/getting-started/models
  - https://docs.mistral.ai/models/shieldstral-1-0
  - https://docs.mistral.ai/inference/labs
  - https://docs.mistral.ai/inference/pricing
  - https://mistral.ai/news/shieldstral
  - https://openrouter.ai/api/v1/models
retrieved: "2026-11-01"
---

# Shieldstral 1.0 3B

## Overview
Shieldstral 1.0 was announced on 4 August 2026. OpenRouter does not list it; the id follows the Hugging Face repo mistralai/Shieldstral-1.0-3B. Mistral lists it as a self-hosted Public Preview Labs model with no API id. It is a 3.8B-parameter (BF16) classifier fine-tuned from Ministral 3 3B Base 2512 with the Pixtral vision encoder. Each request pairs a fixed system message with an Instruct block (context and strictness), a Query (one yes/no question such as "Does this content promote physical violence?") and a Document (prompt, response, prompt-response pair, or image with optional text). The softmax over the yes and no logits is the safety score; Mistral's evaluations threshold it at 0.5. Mistral trained it on up to 32k tokens and recommends staying within that; config.json allows 262,144 positions. The technical report is arXiv 2607.25857.

## Strengths
- Mistral says it matches or beats open guard models up to seven times its size. Prompt-classification F1 is 88.1 on WildGuardTest, 84.1 on ToxicChat and 99.4 on HarmBench; on the English prompt and response sets it is ahead of gpt-oss-safeguard-20B or within 2.6 points, and ahead of Llama Guard 4 12B on every row.
- Multimodal: 97.7 F1 on VLGuard and 81.8 on UnsafeBench.
- Policies are set at inference time, so new taxonomies need no retraining.
- Apache 2.0; fits 16 GB of VRAM in BF16 with vLLM 0.26.0 or later; llama.cpp, SGLang, transformers and Axolotl fine-tuning are documented.

## Limitations
- One policy question per call.
- Not served on Mistral's API; Labs models are not recommended for production.
- Weaker on RTP-LX prompts (70.3 F1) and the LlavaGuard set (72.0); twelve documented languages.

## Good for
- Self-hosted prompt, response and refusal classification next to a local model.
- Image and image-plus-text moderation on one small GPU.
- Safety policies that fixed moderation taxonomies do not cover.
