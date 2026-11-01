---
id: unbabel/towerinstruct-mistral-7b-v0.2
name: TowerInstruct Mistral 7B v0.2
owned_by: unbabel
type: llm
description: TowerInstruct Mistral 7B v0.2 is Unbabel's 2024 open-weight translation model built from a Mistral 7B version of TowerBase and fine-tuned on TowerBlocks for 10 languages, now superseded by Tower+.
aliases: [Unbabel/TowerInstruct-Mistral-7B-v0.2]
context_length: 32768
architecture:
  input_modalities: [text]
  output_modalities: [text]
open_weights: true
license: CC-BY-NC-4.0
release_date: "2024-03-26"
sources:
  - https://huggingface.co/Unbabel/TowerInstruct-Mistral-7B-v0.2
  - https://huggingface.co/api/models/Unbabel/TowerInstruct-Mistral-7B-v0.2
  - https://huggingface.co/Unbabel/TowerInstruct-Mistral-7B-v0.2/raw/main/config.json
  - https://arxiv.org/abs/2402.17733
  - https://arxiv.org/html/2402.17733
  - https://arxiv.org/abs/2506.17080
retrieved: "2026-10-16"
---

# TowerInstruct Mistral 7B v0.2

## Overview
TowerInstruct Mistral 7B v0.2 applies the Tower recipe (arXiv 2402.17733, COLM 2024) to a Mistral base instead of Llama 2: a Mistral version of TowerBase fine-tuned on the TowerBlocks dataset. OpenRouter does not list it; the id follows the Hugging Face repo name Unbabel/TowerInstruct-Mistral-7B-v0.2, and the release date is the repo creation date (2024-03-26) because no vendor announcement states one. It supports English, Portuguese, Spanish, French, German, Dutch, Italian, Korean, Chinese and Russian, and Unbabel says its performance is comparable to TowerInstruct 13B at half the size. Prompts use ChatML with no system prompt. config.json gives 32,768 positions with a 4,096-token sliding window; the weights are bfloat16 (7.24B parameters). The model card gives the licence as CC-BY-NC 4.0 and does not mention the base model's terms. Unbabel's Tower+ models (June 2025) supersede it.

## Strengths
- Unbabel states it matches TowerInstruct 13B, for which the Tower paper reports Comet-22 of 85.14 (en-xx) and 83.18 (xx-en) on WMT23 and 88.88 and 88.47 on Flores-200.
- Half the parameters of the 13B model, stored in bfloat16 rather than float32.

## Limitations
- No benchmark figures for this model appear on the model card or in the paper.
- 10 languages only; not aligned to human preferences, so hallucinations and harmful output are possible.
- Not intended as a chatbot, code assistant or document-level translator (model card).
- The Hugging Face page warns that the transformers "translation" pipeline is unsupported in transformers v5: load the model with AutoModelForCausalLM or pin transformers<5.
- Non-commercial licence; superseded by Tower+.

## Good for
- Translation among the 10 languages where 13B-class quality is wanted from a 7B model.
- Post-editing, NER and paraphrase prompts from TowerBlocks.
- Existing Tower deployments that need a smaller checkpoint.
