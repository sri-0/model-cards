---
id: deepseek/deepseek-ocr-2
name: DeepSeek-OCR 2
owned_by: deepseek
type: llm
description: DeepSeek-OCR 2 is DeepSeek's Apache-2.0 3B OCR model whose DeepEncoder V2 uses a Qwen2-0.5B-based encoder to reorder vision tokens by reading order before the DeepSeek3B-MoE decoder, scoring 91.09 on OmniDocBench v1.5.
aliases: [deepseek-ai/DeepSeek-OCR-2, mlx-community/DeepSeek-OCR-2-8bit]
context_length: 8192
capabilities: [vision]
architecture:
  input_modalities: [text, image]
  output_modalities: [text]
open_weights: true
license: Apache-2.0
release_date: "2026-01-27"
sources:
  - https://huggingface.co/deepseek-ai/DeepSeek-OCR-2
  - https://huggingface.co/api/models/deepseek-ai/DeepSeek-OCR-2
  - https://huggingface.co/deepseek-ai/DeepSeek-OCR-2/raw/main/config.json
  - https://github.com/deepseek-ai/DeepSeek-OCR-2
  - https://github.com/deepseek-ai/DeepSeek-OCR
  - https://arxiv.org/abs/2601.20552
  - https://github.com/opendatalab/OmniDocBench
  - https://huggingface.co/mlx-community/DeepSeek-OCR-2-8bit
  - https://openrouter.ai/api/v1/models
retrieved: "2026-11-01"
---

# DeepSeek-OCR 2

## Overview
DeepSeek released DeepSeek-OCR 2 on 2026-01-27 under Apache 2.0 (the first version was MIT) with the paper "DeepSeek-OCR 2: Visual Causal Flow" (arXiv 2601.20552, 2026-01-28). OpenRouter does not list it; the id follows the Hugging Face repo `deepseek-ai/DeepSeek-OCR-2` under the `deepseek` directory. Only the encoder changed: DeepEncoder V2 keeps the 80M SAM-base tokenizer but replaces CLIP with a Qwen2-0.5B-based LLM-style encoder whose causal queries reorder vision tokens by the page's logical structure before the unchanged DeepSeek3B-MoE decoder (about 500M active parameters; 3.39B in the checkpoint, 8,192 positions). Its single dynamic mode uses up to six 768-pixel tiles plus a 1024-pixel global view, 256 to 1,120 vision tokens. Prompts match the first version, such as `<image>\n<|grounding|>Convert the document to markdown.`

## Strengths
- OmniDocBench v1.5 overall 91.09, 3.73 points above DeepSeek-OCR with the smallest vision-token budget in DeepSeek's table; reading-order edit distance 0.057 against 0.085.
- OmniDocBench v1.6 overall 90.25 on the official leaderboard.
- Repetition in DeepSeek's production falls to 4.17% on online images and 2.88% on PDF pages.
- Same transformers and vLLM workflow as the first version; community MLX conversion.

## Limitations
- Below the leading 1B-class parsers on OmniDocBench v1.6, such as PaddleOCR-VL-1.6 (96.34) and MinerU2.5-Pro (95.75).
- The repo's vLLM path pins vLLM 0.8.5 with CUDA 11.8; Ollama's library lists only the first version.
- Needs `trust_remote_code` for transformers.

## Good for
- Upgrading DeepSeek-OCR pipelines with no prompt changes.
- Multi-column and complex layouts where reading order matters.
