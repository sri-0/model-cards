---
id: unbabel/tower-plus-72b
name: Tower+ 72B
owned_by: unbabel
type: llm
description: Tower+ 72B is Unbabel's largest open-weight translation and multilingual instruction model, built on Qwen 2.5 72B for 22 languages under a CC-BY-NC-SA 4.0 licence.
aliases: [Unbabel/Tower-Plus-72B]
context_length: 32768
architecture:
  input_modalities: [text]
  output_modalities: [text]
open_weights: true
license: CC-BY-NC-SA-4.0
release_date: "2025-06-09"
sources:
  - https://huggingface.co/Unbabel/Tower-Plus-72B
  - https://huggingface.co/api/models/Unbabel/Tower-Plus-72B
  - https://huggingface.co/Unbabel/Tower-Plus-72B/raw/main/config.json
  - https://arxiv.org/abs/2506.17080
  - https://arxiv.org/html/2506.17080
retrieved: "2026-10-16"
---

# Tower+ 72B

## Overview
Tower+ 72B is the largest of Unbabel's Tower+ models (2B, 9B and 72B), described in arXiv 2506.17080 (submitted 2025-06-20). OpenRouter does not list it; the id follows the Hugging Face repo name Unbabel/Tower-Plus-72B, and the release date is the repo creation date (2025-06-09) because no vendor announcement states one. It is built on Qwen 2.5 72B (the smaller models use Gemma 2) and uses Qwen's ChatML chat template. The model card lists three training stages, continued pretraining, instruction tuning and Weighted Preference Optimization, each including parallel and multilingual data for 22 languages. config.json gives 32,768 positions, while the model card states 131,072 tokens with 8,192 recommended for generation; the config value is what vLLM and transformers apply by default. Safetensors metadata gives 72.7B bfloat16 parameters. The Hugging Face licence tag is CC-BY-NC-SA 4.0 (the card text says CC-BY-NC 4.0); commercial use is excluded either way.

## Strengths
- Unbabel reports (paper Table 1) WMT24++ xCOMET-xxl of 86.68 on seven high-resource languages, the best open-weight score and level with GPT-4o-1120's 86.69; 83.29 on 15 and 83.74 on all 24 directions.
- Same table: M-ArenaHard 54.52 and IFEval 89.02 against 50.00 and 88.44 for Qwen 2.5 72B; IF-MT 5.55 for instruction following and 88.95 for translation quality (GPT-4o-1120: 5.81 and 89.35).

## Limitations
- Non-commercial licence.
- Dense 72B weights need several GPUs; Unbabel's vLLM example uses tensor parallelism of 4.
- On the 15- and 24-language averages the 9B model scores higher (83.57 and 84.38).
- Text only; no documented tool calling or reasoning mode.

## Good for
- Highest-quality translation among the covered high-resource languages.
- Translation with formatting or terminology instructions.
- One model for multilingual chat and translation in non-commercial settings.
