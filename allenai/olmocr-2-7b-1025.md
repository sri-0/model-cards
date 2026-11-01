---
id: allenai/olmocr-2-7b-1025
name: olmOCR-2-7B-1025
owned_by: allenai
type: llm
description: olmOCR-2-7B-1025 is Ai2's Apache-2.0 document OCR model, a Qwen2.5-VL-7B-Instruct fine-tune with GRPO reinforcement learning on unit-test rewards, built to run inside the olmOCR PDF-to-Markdown toolkit.
aliases: [allenai/olmOCR-2-7B-1025, allenai/olmOCR-2-7B-1025-FP8, mlx-community/olmOCR-2-7B-1025-bf16]
context_length: 128000
capabilities: [vision]
architecture:
  input_modalities: [text, image]
  output_modalities: [text]
open_weights: true
license: Apache-2.0
release_date: "2025-10-21"
sources:
  - https://huggingface.co/allenai/olmOCR-2-7B-1025
  - https://huggingface.co/allenai/olmOCR-2-7B-1025-FP8
  - https://huggingface.co/api/models/allenai/olmOCR-2-7B-1025
  - https://huggingface.co/allenai/olmOCR-2-7B-1025/raw/main/config.json
  - https://github.com/allenai/olmocr
  - https://arxiv.org/abs/2510.19817
  - https://arxiv.org/abs/2502.18443
  - https://olmocr.allenai.org/
  - https://github.com/opendatalab/OmniDocBench
  - https://huggingface.co/mlx-community/olmOCR-2-7B-1025-bf16
  - https://openrouter.ai/api/v1/models
retrieved: "2026-11-01"
---

# olmOCR-2-7B-1025

## Overview
Ai2 released olmOCR-2-7B-1025 on 2025-10-21 with olmOCR toolkit v0.4.0, under Apache 2.0, and described it in "olmOCR 2: Unit Test Rewards for Document OCR" (arXiv 2510.19817). OpenRouter does not list it; the id follows the Hugging Face repo `allenai/olmOCR-2-7B-1025` under a new `allenai` directory. It fine-tunes Qwen2.5-VL-7B-Instruct (8.29B parameters, 128,000 positions) on the olmOCR-mix-1025 dataset, then applies GRPO reinforcement learning on synthetic documents scored by unit tests, which lifts maths, tables and other hard cases. Ai2 recommends the FP8 checkpoint for inference and this BF16 one for fine-tuning. The model expects one page image with its longest side at 1,288 pixels and a prompt carrying page metadata, which the toolkit builds; the toolkit also renders, rotates and retries pages and writes Markdown or Dolma JSON.

## Strengths
- olmOCR-bench 82.4 ± 1.1 (FP8) and 82.3 ± 1.1 (BF16) with the toolkit, about 4 points above the previous release; 99.7 on base pages and 96.1 on headers and footers.
- Handles equations, tables, handwriting, multi-column layouts and insets, and drops headers and footers.
- Ai2 puts the cost under $200 per million pages; the toolkit runs on a local GPU or a remote vLLM server.

## Limitations
- Needs a GPU with at least 12 GB; the toolkit wants a clean Python environment plus poppler.
- Weak on old scans (47.7 on olmOCR-bench).
- Trained for English; OmniDocBench v1.6 lists olmOCR (run with SGLang, version not stated) at 85.74, far below the 0.9B to 1.2B leaders.
- Prompting it without the toolkit's metadata lowers quality.

## Good for
- Turning large English PDF collections into clean text for LLM training.
- Teams that want a fully open recipe with data and training code.
