---
id: qwen/qwen3-omni-30b-a3b-captioner
name: Qwen3 Omni 30B A3B Captioner
owned_by: qwen
type: llm
description: Qwen3 Omni 30B A3B Captioner is Qwen's open-weight (Apache-2.0) audio captioning model, fine-tuned from Qwen3-Omni-30B-A3B-Instruct to write detailed, low-hallucination descriptions of any audio clip.
aliases: [Qwen/Qwen3-Omni-30B-A3B-Captioner, qwen3-omni-30b-a3b-captioner]
context_length: 65536
architecture:
  input_modalities: [audio]
  output_modalities: [text]
open_weights: true
license: Apache-2.0
release_date: "2025-09-22"
sources:
  - https://huggingface.co/Qwen/Qwen3-Omni-30B-A3B-Captioner
  - https://huggingface.co/api/models/Qwen/Qwen3-Omni-30B-A3B-Captioner
  - https://huggingface.co/Qwen/Qwen3-Omni-30B-A3B-Captioner/raw/main/config.json
  - https://huggingface.co/Qwen/Qwen3-Omni-30B-A3B-Instruct
  - https://github.com/QwenLM/Qwen3-Omni
  - https://web.archive.org/web/20260606135246/https://www.alibabacloud.com/help/en/model-studio/models
  - https://openrouter.ai/api/v1/models
retrieved: "2026-11-01"
---

# Qwen3 Omni 30B A3B Captioner

## Overview
Qwen3-Omni-30B-A3B-Captioner was published with the Qwen3-Omni release, which the Qwen3-Omni GitHub README dates 2025-09-22 (the Hugging Face repo was created 2025-09-15). OpenRouter does not list it and Artificial Analysis has no page for it; the id follows the Hugging Face repo. Qwen fine-tuned it from Qwen3-Omni-30B-A3B-Instruct because, it says, the research community lacks a general-purpose audio captioning model. It keeps only the Thinker, a 48-layer mixture-of-experts text model with 128 experts (8 active) and 65,536 positions in config.json; Hugging Face counts 31.7B parameters. It is single-turn: one audio clip in, text out, with no text prompt, and Qwen recommends clips of 30 seconds or less. It runs with transformers built from source or a vLLM branch built from source. Alibaba Cloud Model Studio (archived 2026-06-06) lists qwen3-omni-30b-a3b-captioner in Singapore at $3.81 per million input and $3.06 per million output tokens.

## Strengths
- Describes speech, including several speakers' emotions, languages, intentions and cultural context, according to the model card.
- Describes non-speech audio such as environmental sounds, music and film sound effects, and copes with mixed sources.
- Qwen describes its captions as detailed and low in hallucination.

## Limitations
- Audio input only and no prompt control over what it describes.
- Long clips lose detail; Qwen advises 30 seconds or less.
- Qwen publishes no captioning benchmark scores on the card.

## Good for
- Labelling audio datasets with rich descriptions.
- Sound and music search indexes.
- Accessibility descriptions of audio content.
