---
id: unbabel/tower-plus-9b
name: Tower+ 9B
owned_by: unbabel
type: llm
description: Tower+ 9B is Unbabel's open-weight translation and multilingual instruction model built on Gemma 2 9B, covering 22 languages under a CC-BY-NC-SA 4.0 licence.
aliases: [Unbabel/Tower-Plus-9B]
context_length: 8192
architecture:
  input_modalities: [text]
  output_modalities: [text]
open_weights: true
license: CC-BY-NC-SA-4.0
release_date: "2025-06-09"
sources:
  - https://huggingface.co/Unbabel/Tower-Plus-9B
  - https://huggingface.co/api/models/Unbabel/Tower-Plus-9B
  - https://huggingface.co/Unbabel/Tower-Plus-9B/raw/main/config.json
  - https://arxiv.org/abs/2506.17080
  - https://arxiv.org/html/2506.17080
retrieved: "2026-10-16"
---

# Tower+ 9B

## Overview
Tower+ 9B is the mid-sized model of Unbabel's Tower+ family (2B, 9B and 72B), described in arXiv 2506.17080 (submitted 2025-06-20). OpenRouter does not list it; the id follows the Hugging Face repo name Unbabel/Tower-Plus-9B, and the release date is the repo creation date (2025-06-09) because no vendor announcement states one. It is built on Gemma 2 9B. The model card lists three training stages, continued pretraining, instruction tuning and Weighted Preference Optimization, each including parallel and multilingual data for 22 languages, from German, Spanish and French to Hindi, Icelandic, Japanese and Korean. The context window is 8,192 tokens (model card and config); safetensors metadata gives 9.24B bfloat16 parameters. The Hugging Face licence tag is CC-BY-NC-SA 4.0 (the card text says CC-BY-NC 4.0); commercial use is excluded either way.

## Strengths
- Unbabel reports (paper Table 1) WMT24++ xCOMET-xxl of 86.25 on seven high-resource languages, 83.57 on 15 and 84.38 on all 24 directions, against 86.69, 84.33 and 85.21 for GPT-4o-1120 and 81.93, 75.35 and 76.34 for Gemma 2 9B.
- Same table: IFEval 83.84 and M-ArenaHard 33.47 (Gemma 2 9B: 66.86 and 13.38); IF-MT 4.85 for instruction following and 88.51 for translation quality.
- Scores above the 72B model on the 15- and 24-language WMT24++ averages.

## Limitations
- Non-commercial licence.
- 8,192-token window. Unbabel recommends vLLM and notes Gemma defaults to 4K context, so set VLLM_ALLOW_LONG_MAX_MODEL_LEN=1 and VLLM_WORKER_MULTIPROC_METHOD=spawn.
- Text only; no documented tool calling or reasoning mode.
- Languages outside the 22 covered are unsupported.

## Good for
- Translation across all 22 covered languages on a single GPU.
- Multilingual assistants needing translation and general instruction following.
- Multilingual synthetic data generation, a use case Unbabel names.
