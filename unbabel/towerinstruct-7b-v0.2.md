---
id: unbabel/towerinstruct-7b-v0.2
name: TowerInstruct 7B v0.2
owned_by: unbabel
type: llm
description: TowerInstruct 7B v0.2 is Unbabel's 2024 open-weight translation model, a Llama 2 7B continued-pretrained for 10 languages and fine-tuned on the TowerBlocks dataset, now superseded by Tower+.
aliases: [Unbabel/TowerInstruct-7B-v0.2]
context_length: 4096
architecture:
  input_modalities: [text]
  output_modalities: [text]
open_weights: true
license: CC-BY-NC-4.0
release_date: "2024-02-09"
sources:
  - https://huggingface.co/Unbabel/TowerInstruct-7B-v0.2
  - https://huggingface.co/api/models/Unbabel/TowerInstruct-7B-v0.2
  - https://huggingface.co/Unbabel/TowerInstruct-7B-v0.2/raw/main/config.json
  - https://arxiv.org/abs/2402.17733
  - https://arxiv.org/html/2402.17733
  - https://unbabel.com/announcing-tower-an-open-multilingual-llm-for-translation-related-tasks/
  - https://arxiv.org/abs/2506.17080
retrieved: "2026-10-16"
---

# TowerInstruct 7B v0.2

## Overview
TowerInstruct 7B v0.2 comes from the Tower project of Unbabel, Instituto Superior Técnico and CentraleSupélec (arXiv 2402.17733, COLM 2024). OpenRouter does not list it; the id follows the Hugging Face repo name Unbabel/TowerInstruct-7B-v0.2. Unbabel's blog update of 2024-02-09 announced this iteration, the day the repo was created. TowerBase 7B is Llama 2 7B continued-pretrained on 20 billion tokens (two-thirds monolingual, one-third parallel) for English, German, French, Dutch, Italian, Spanish, Portuguese, Korean, Russian and Chinese; TowerInstruct is TowerBase fine-tuned for 4 epochs at 2,048 sequence length on TowerBlocks (translation, post-editing, MT evaluation, NER, paraphrasing, chat and code data). v0.2 improves document-level translation over v0.1. Prompts use ChatML with no system prompt. config.json gives 4,096 positions; the weights are float32 (6.74B parameters). The licence is CC-BY-NC 4.0, with Llama 2 under the Llama 2 Community License. Unbabel's Tower+ models (June 2025) supersede it.

## Strengths
- The Tower paper reports Comet-22 for TowerInstruct 7B of 88.51 (en-xx) and 88.27 (xx-en) on Flores-200, 84.28 and 82.77 on WMT23 and 87.01 on TICO-19; GPT-4 scored 89.13, 88.42, 86.01, 83.69 and 87.52.
- Post-editing 82.69 (en-xx) and named-entity recognition 71.68 in the same paper, against 81.47 and 50.22 for GPT-3.5-turbo.

## Limitations
- 10 languages only; not aligned to human preferences, so hallucinations and harmful output are possible.
- Not intended as a chatbot, code assistant or document-level translator (model card).
- The Hugging Face page warns that the transformers "translation" pipeline is unsupported in transformers v5: load the model with AutoModelForCausalLM or pin transformers<5.
- 4,096-token window; non-commercial licence; superseded by Tower+.

## Good for
- Sentence and paragraph translation among the 10 languages on one GPU.
- Post-editing, NER and paraphrase tasks from the TowerBlocks prompt set.
- Reproducing published Tower results.
