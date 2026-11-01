---
id: unbabel/towerinstruct-13b-v0.1
name: TowerInstruct 13B v0.1
owned_by: unbabel
type: llm
description: TowerInstruct 13B v0.1 is Unbabel's 2024 open-weight translation model, a Llama 2 13B continued-pretrained for 10 languages and fine-tuned on TowerBlocks, now superseded by Tower+.
aliases: [Unbabel/TowerInstruct-13B-v0.1]
context_length: 4096
architecture:
  input_modalities: [text]
  output_modalities: [text]
open_weights: true
license: CC-BY-NC-4.0
release_date: "2024-01-11"
sources:
  - https://huggingface.co/Unbabel/TowerInstruct-13B-v0.1
  - https://huggingface.co/api/models/Unbabel/TowerInstruct-13B-v0.1
  - https://huggingface.co/Unbabel/TowerInstruct-13B-v0.1/raw/main/config.json
  - https://huggingface.co/api/models/Unbabel/TowerInstruct-13B-v0.2
  - https://arxiv.org/abs/2402.17733
  - https://arxiv.org/html/2402.17733
  - https://unbabel.com/announcing-tower-an-open-multilingual-llm-for-translation-related-tasks/
  - https://arxiv.org/abs/2506.17080
retrieved: "2026-10-16"
---

# TowerInstruct 13B v0.1

## Overview
TowerInstruct 13B v0.1 is the larger of the two original Tower models from Unbabel, Instituto Superior Técnico and CentraleSupélec (arXiv 2402.17733, COLM 2024). OpenRouter does not list it; the id follows the Hugging Face repo name Unbabel/TowerInstruct-13B-v0.1. The release date is Unbabel's blog announcement of 2024-01-11; the Hugging Face repo was created on 2024-01-29. TowerBase 13B is Llama 2 13B continued-pretrained on 20 billion tokens for English, German, French, Dutch, Italian, Spanish, Portuguese, Korean, Russian and Chinese; TowerInstruct is TowerBase fine-tuned for 4 epochs at 2,048 sequence length on TowerBlocks v0.2 (translation, post-editing, MT evaluation, NER, paraphrasing, chat and code data). config.json gives 4,096 positions; the weights are float32 (13.0B parameters). The licence is CC-BY-NC 4.0, with Llama 2 under the Llama 2 Community License. A TowerInstruct-13B-v0.2 repo also exists; Unbabel's Tower+ models (June 2025) supersede the series.

## Strengths
- The Tower paper calls it the open system with the highest translation quality, ahead of Llama 2 70B, Mixtral 8x7B Instruct, NLLB-54B and ALMA-R.
- Comet-22 in that paper: 88.88 (en-xx) and 88.47 (xx-en) on Flores-200, 85.14 and 83.18 on WMT23, 87.32 on TICO-19; GPT-4 scored 89.13, 88.42, 86.01, 83.69 and 87.52.
- Post-editing 83.31 (en-xx) and NER 74.70, the paper's top NER result.

## Limitations
- 10 languages only; not aligned to human preferences, so hallucinations and harmful output are possible.
- Not intended as a chatbot, code assistant or document-level translator (model card).
- The Hugging Face page warns that the transformers "translation" pipeline is unsupported in transformers v5: load the model with AutoModelForCausalLM or pin transformers<5.
- 4,096-token window; float32 checkpoint; non-commercial licence; superseded.

## Good for
- Best translation quality in the original Tower series.
- Post-editing and NER within translation workflows.
- Reproducing published Tower results.
