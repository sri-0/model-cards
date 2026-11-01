---
id: qwen/qwen2.5-omni-3b
name: Qwen2.5 Omni 3B
owned_by: qwen
type: llm
description: Qwen2.5 Omni 3B is Qwen's April 2025 smaller end-to-end omni-modal model that takes text, images, audio and video and streams text and speech, released under the non-commercial Qwen Research License.
aliases: [Qwen/Qwen2.5-Omni-3B]
context_length: 32768
capabilities: [vision]
architecture:
  input_modalities: [text, image, audio, video]
  output_modalities: [text, audio]
open_weights: true
license: Qwen Research License Agreement
release_date: "2025-04-30"
sources:
  - https://huggingface.co/Qwen/Qwen2.5-Omni-3B
  - https://huggingface.co/api/models/Qwen/Qwen2.5-Omni-3B
  - https://huggingface.co/Qwen/Qwen2.5-Omni-3B/raw/main/config.json
  - https://huggingface.co/Qwen/Qwen2.5-Omni-3B/blob/main/LICENSE
  - https://github.com/QwenLM/Qwen2.5-Omni
  - https://qwenlm.github.io/blog/qwen2.5-omni/
  - https://openrouter.ai/api/v1/models
retrieved: "2026-11-01"
---

# Qwen2.5 Omni 3B

## Overview
Qwen2.5-Omni-3B was released on 2025-04-30, according to the Qwen2.5-Omni GitHub README, so that more platforms can run Qwen2.5-Omni (the Hugging Face repo was created the same day). OpenRouter does not list it and Artificial Analysis has no page for it; the id follows the Hugging Face repo. It shares the 7B model's Thinker-Talker design and TMRoPE: the Thinker reads text, images, audio and video and the Talker streams speech. config.json gives the Thinker 36 layers and 32,768 positions; Hugging Face counts 5.54B parameters across all parts. Qwen gives a minimum of 18.38 GB of GPU memory in BF16 for a 15-second video and 28.22 GB for 60 seconds. The weights use the Qwen Research License, which allows non-commercial use only. Ollama and Alibaba Cloud Model Studio do not list it.

## Strengths
- Qwen reports OmniBench 52.19%, MMAU 63.30, LibriSpeech test-clean/other WER 2.2/4.5 and VoiceBench average 68.81.
- Vision: MMMU 53.1, MathVista 59.4, DocVQA 93.3 and Video-MME 68.6 with subtitles.
- Text: MMLU-Pro 40.4, MATH 63.6 and GSM8K 82.6.
- Speech translation on CoVoST2 en-zh scores 41.4, the same as the 7B model.

## Limitations
- Non-commercial licence.
- Below Qwen2.5-Omni-7B on most benchmarks Qwen lists, for example OmniBench 52.19% against 56.13%.
- No reasoning mode or documented tool calling; no published knowledge cutoff.

## Good for
- Research prototypes of voice and video assistants on smaller GPUs.
- Audio understanding and captioning experiments.
- Comparing omni-model quality across sizes.
