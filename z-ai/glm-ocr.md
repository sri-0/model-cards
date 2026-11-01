---
id: z-ai/glm-ocr
name: GLM-OCR
owned_by: z-ai
type: llm
description: GLM-OCR is Z.ai's 0.9B open-weight (MIT) document-parsing model, a CogViT encoder with a GLM-0.5B decoder that reports 94.62 on OmniDocBench v1.5.
aliases: [glm-ocr, glm-ocr:bf16, glm-ocr:q8_0, zai-org/GLM-OCR]
context_length: 131072
capabilities: [vision]
architecture:
  input_modalities: [text, image, file]
  output_modalities: [text]
open_weights: true
license: MIT
release_date: "2026-02-03"
sources:
  - https://huggingface.co/zai-org/GLM-OCR
  - https://huggingface.co/api/models/zai-org/GLM-OCR
  - https://huggingface.co/zai-org/GLM-OCR/raw/main/config.json
  - https://github.com/zai-org/GLM-OCR
  - https://docs.z.ai/guides/vlm/glm-ocr
  - https://docs.z.ai/guides/overview/pricing
  - https://docs.bigmodel.cn/cn/update/new-releases
  - https://ollama.com/library/glm-ocr/tags
  - https://openrouter.ai/api/v1/models
retrieved: "2026-11-01"
---

# GLM-OCR

## Overview
GLM-OCR launched on 2026-02-03 and its technical report (arXiv 2603.10910) followed in March 2026. Z.ai describes a 0.9B-parameter encoder-decoder built on the GLM-V architecture: a CogViT vision encoder, a lightweight connector with token downsampling and a GLM-0.5B decoder, trained with a multi-token prediction loss and full-task reinforcement learning. It supports two prompt types: document parsing (text, formulas, tables) and information extraction into a caller-supplied JSON schema. Z.ai's official SDK adds PP-DocLayoutV3 layout analysis for complete page parsing. On Z.ai's API, `glm-ocr` runs behind the layout-parsing endpoint at $0.03 per million input and output tokens, for images up to 10 MB and PDFs up to 50 MB and 100 pages. OpenRouter does not list it; the id is the Hugging Face repo `zai-org/GLM-OCR` under the z-ai prefix. Weights are MIT-licensed.

## Strengths
- Z.ai reports 94.62 on OmniDocBench v1.5, first overall at release, with strong formula, table and extraction results.
- Z.ai measured 1.86 PDF pages and 0.67 images per second at single concurrency, faster than the OCR systems it compared.
- Handles code-heavy documents, complex tables, seals and handwriting; Chinese, English, French, Spanish, Russian, German, Japanese and Korean.
- Serves on vLLM, SGLang, transformers and Ollama.

## Limitations
- Only the two prompt types are supported; extraction output must follow the JSON schema strictly.
- The full pipeline also includes PP-DocLayoutV3 under Apache 2.0, so both licences apply.
- The official SDK covers document parsing only; extraction runs through the model directly.

## Good for
- High-volume document parsing into Markdown for RAG.
- Form, receipt and ID-card field extraction to JSON.
- Edge or local OCR with a very small model.
