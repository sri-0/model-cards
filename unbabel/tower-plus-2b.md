---
id: unbabel/tower-plus-2b
name: Tower+ 2B
owned_by: unbabel
type: llm
description: Tower+ 2B is Unbabel's open-weight translation and multilingual instruction model built on Gemma 2 2B, covering 22 languages under a CC-BY-NC-SA 4.0 licence.
aliases: [Unbabel/Tower-Plus-2B]
context_length: 8192
architecture:
  input_modalities: [text]
  output_modalities: [text]
open_weights: true
license: CC-BY-NC-SA-4.0
release_date: "2025-06-09"
sources:
  - https://huggingface.co/Unbabel/Tower-Plus-2B
  - https://huggingface.co/api/models/Unbabel/Tower-Plus-2B
  - https://huggingface.co/Unbabel/Tower-Plus-2B/raw/main/config.json
  - https://arxiv.org/abs/2506.17080
  - https://arxiv.org/html/2506.17080
retrieved: "2026-10-16"
---

# Tower+ 2B

## Overview
Tower+ 2B is the smallest of Unbabel's three Tower+ models (2B, 9B and 72B), described in arXiv 2506.17080 (submitted 2025-06-20). OpenRouter does not list it; the id follows the Hugging Face repo name Unbabel/Tower-Plus-2B, and the release date is the repo creation date (2025-06-09) because no vendor announcement states one. It is built on Gemma 2 2B and trained in four stages, continued pretraining, instruction tuning, Weighted Preference Optimization and GRPO with verifiable rewards, with parallel and multilingual data for 22 languages at every stage. The context window is 8,192 tokens (model card and config); safetensors metadata gives 2.61B bfloat16 parameters. The Hugging Face licence tag is CC-BY-NC-SA 4.0 (the card text says CC-BY-NC 4.0); commercial use is excluded either way.

## Strengths
- Unbabel reports (paper Table 1) WMT24++ xCOMET-xxl of 81.88 on seven high-resource languages, 78.42 on 15 and 79.13 on all 24 directions, which the paper says matches Llama 3.3 70B (82.74, 78.30 and 79.48).
- Same table: IFEval 67.32 and M-ArenaHard 6.33, both above Unbabel's earlier Tower-v2 70B; IF-MT 2.90 for instruction following and 87.65 for translation quality.
- Unbabel also suggests it for multilingual synthetic data generation.

## Limitations
- Non-commercial licence.
- 8,192-token window. Unbabel recommends vLLM and notes Gemma defaults to 4K context, so set VLLM_ALLOW_LONG_MAX_MODEL_LEN=1 and VLLM_WORKER_MULTIPROC_METHOD=spawn.
- Instruction following well below the 9B and 72B models (IFEval 83.84 and 89.02).
- Text only; no documented tool calling or reasoning mode.

## Good for
- Translation among the 22 covered languages on a small GPU.
- Non-commercial multilingual projects and research.
- The model card's prompt form: "Translate the following English source text to Portuguese (Portugal):" followed by the text.
