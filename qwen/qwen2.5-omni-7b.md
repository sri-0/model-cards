---
id: qwen/qwen2.5-omni-7b
name: Qwen2.5 Omni 7B
owned_by: qwen
type: llm
description: Qwen2.5 Omni 7B is Qwen's March 2025 open-weight (Apache-2.0) end-to-end omni-modal model that takes text, images, audio and video and streams answers as text and natural speech.
aliases: [Qwen/Qwen2.5-Omni-7B, Qwen/Qwen2.5-Omni-7B-AWQ, Qwen/Qwen2.5-Omni-7B-GPTQ-Int4, qwen2.5-omni-7b]
context_length: 32768
capabilities: [vision]
architecture:
  input_modalities: [text, image, audio, video]
  output_modalities: [text, audio]
open_weights: true
license: Apache-2.0
release_date: "2025-03-27"
sources:
  - https://huggingface.co/Qwen/Qwen2.5-Omni-7B
  - https://huggingface.co/api/models/Qwen/Qwen2.5-Omni-7B
  - https://huggingface.co/api/models?author=Qwen&limit=1000
  - https://huggingface.co/Qwen/Qwen2.5-Omni-7B/raw/main/config.json
  - https://qwenlm.github.io/blog/qwen2.5-omni/
  - https://github.com/QwenLM/Qwen2.5-Omni
  - https://web.archive.org/web/20260606135246/https://www.alibabacloud.com/help/en/model-studio/models
  - https://openrouter.ai/api/v1/models
retrieved: "2026-11-01"
---

# Qwen2.5 Omni 7B

## Overview
Qwen2.5-Omni-7B was announced in the Qwen blog on 2025-03-27 (the GitHub README says 2025-03-26; the Hugging Face repo was created 2025-03-22). OpenRouter does not list it and Artificial Analysis has no page for it; the id follows the Hugging Face repo. It uses a Thinker-Talker design: the Thinker reads text, images, audio and video and writes text, and the Talker streams speech from it; TMRoPE aligns video and audio timestamps. config.json gives the Thinker 32,768 positions; Hugging Face counts 10.7B parameters across all parts. Speech output needs Qwen's fixed system prompt and offers two voices, Chelsie (default) and Ethan; disable_talker() saves about 2 GB. Qwen gives a minimum of 31.11 GB of GPU memory in BF16 for a 15-second video and 60.19 GB for 60 seconds. Qwen publishes AWQ and GPTQ-Int4 builds. Alibaba Cloud Model Studio (archived 2026-06-06) lists qwen2.5-omni-7b in Singapore with a 32,768-token window and 2,048 output tokens, billed per modality.

## Strengths
- Qwen reports OmniBench 56.13% (Gemini 1.5 Pro 42.91%), MMAU 65.6, LibriSpeech test-clean/other WER 1.8/3.4 and VoiceBench average 74.12.
- Vision: MMMU 59.2, MathVista 67.9, DocVQA 95.2 and Video-MME 72.4 with subtitles, close to Qwen2.5-VL-7B.
- The GitHub README says vLLM supports its audio output.

## Limitations
- Text scores trail Qwen2.5-7B: MMLU-Pro 47.0 against 56.3 and GSM8K 88.7 against 91.6.
- MMMU-Pro 36.6, below Qwen2.5-VL-7B's 38.3.
- No reasoning mode or documented tool calling; no published knowledge cutoff.

## Good for
- Voice and video chat assistants that reply in speech.
- Speech recognition and translation with one model.
- Multimodal agents on a single large GPU.
