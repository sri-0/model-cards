---
id: deepseek/deepseek-ocr
name: DeepSeek-OCR
owned_by: deepseek
type: llm
description: DeepSeek-OCR is DeepSeek's MIT-licensed 3B end-to-end OCR model (DeepEncoder plus a DeepSeek3B-MoE decoder with about 570M active parameters) that studies optical compression of long contexts into few vision tokens.
aliases: [deepseek-ai/DeepSeek-OCR, deepseek-ocr, "deepseek-ocr:3b", ggml-org/DeepSeek-OCR-GGUF, mlx-community/DeepSeek-OCR-8bit]
context_length: 8192
capabilities: [vision]
architecture:
  input_modalities: [text, image]
  output_modalities: [text]
open_weights: true
license: MIT
release_date: "2025-10-20"
sources:
  - https://huggingface.co/deepseek-ai/DeepSeek-OCR
  - https://huggingface.co/api/models/deepseek-ai/DeepSeek-OCR
  - https://huggingface.co/deepseek-ai/DeepSeek-OCR/raw/main/config.json
  - https://github.com/deepseek-ai/DeepSeek-OCR
  - https://arxiv.org/abs/2510.18234
  - https://arxiv.org/abs/2601.20552
  - https://docs.vllm.ai/projects/recipes/en/latest/DeepSeek/DeepSeek-OCR.html
  - https://ollama.com/library/deepseek-ocr
  - https://huggingface.co/ggml-org/DeepSeek-OCR-GGUF
  - https://huggingface.co/mlx-community/DeepSeek-OCR-8bit
  - https://github.com/allenai/olmocr
  - https://openrouter.ai/api/v1/models
retrieved: "2026-11-01"
---

# DeepSeek-OCR

## Overview
DeepSeek released DeepSeek-OCR on 2025-10-20 under the MIT licence with the paper "DeepSeek-OCR: Contexts Optical Compression" (arXiv 2510.18234). OpenRouter does not list it; the id follows the Hugging Face repo `deepseek-ai/DeepSeek-OCR` under the existing `deepseek` directory. DeepEncoder (a SAM-ViT-B and CLIP-L design) compresses a page into 64 to 400 vision tokens in its native modes (Tiny 512, Small 640, Base 1024, Large 1280 pixels) or tiles it in the dynamic Gundam mode; a DeepSeek3B-MoE decoder (12 layers, 6 of 64 routed experts plus 2 shared, about 570M active) writes the text. The checkpoint has 3.34B parameters and 8,192 positions. Prompts such as `<image>\n<|grounding|>Convert the document to markdown.` or `<image>\nFree OCR.` choose Markdown with layout boxes or plain text; charts, chemical formulas and plane geometry can be re-parsed in a second call.

## Strengths
- DeepSeek reports 97% OCR precision when text tokens are within ten times the vision tokens, and about 60% at 20 times.
- OmniDocBench v1.5 overall 87.36 with nine crops (arXiv 2601.20552); olmOCR-bench 75.7 in AI2's table.
- Trained on 30M PDF pages in about 100 languages; DeepSeek says one A100-40G can produce 200k+ pages of training data a day.
- Upstream vLLM support since 2025-10-23, transformers with `trust_remote_code`, Ollama (`deepseek-ocr:3b`, Ollama 0.13.0 or later), and community GGUF and MLX conversions.

## Limitations
- Repeats itself on 6.25% of online images and 3.69% of PDF pages in DeepSeek's production logs; the vLLM example adds an n-gram logits processor against loops.
- Superseded by DeepSeek-OCR 2 (91.09 on OmniDocBench v1.5).

## Good for
- Bulk PDF-to-Markdown for LLM training data.
- Research on vision-token compression.
