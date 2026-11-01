---
id: baidu/unlimited-ocr
name: Unlimited-OCR
owned_by: baidu
type: llm
description: Unlimited-OCR is Baidu's MIT-licensed end-to-end OCR model built on DeepSeek-OCR with Reference Sliding Window Attention, so its KV cache stays constant and it can parse dozens of pages in one 32K-token pass.
aliases: [baidu/Unlimited-OCR]
context_length: 32768
capabilities: [vision]
architecture:
  input_modalities: [text, image]
  output_modalities: [text]
open_weights: true
license: MIT
release_date: "2026-06-22"
sources:
  - https://huggingface.co/baidu/Unlimited-OCR
  - https://huggingface.co/api/models/baidu/Unlimited-OCR
  - https://huggingface.co/baidu/Unlimited-OCR/raw/main/config.json
  - https://arxiv.org/abs/2606.23050
  - https://github.com/baidu/Unlimited-OCR
  - https://recipes.vllm.ai/baidu/Unlimited-OCR
  - https://cloud.baidu.com/doc/OCR/s/fmr1p39gb
  - https://openrouter.ai/api/v1/models
retrieved: "2026-10-16"
---

# Unlimited-OCR

## Overview
Unlimited-OCR was released by Baidu on 2026-06-22 (Hugging Face repo created 2026-06-19) under the MIT licence. OpenRouter does not list it; the id follows the Hugging Face repo `baidu/Unlimited-OCR`. It builds on DeepSeek-OCR: config.json shows its SAM-ViT-B plus CLIP-L encoder and a 12-layer mixture-of-experts decoder (64 routed experts, 6 active; 3.34B parameters in the safetensors), but every decoder attention layer is replaced by Reference Sliding Window Attention (R-SWA, 128-token window), so the KV cache stays constant and one pass can transcribe dozens of pages within 32,768 tokens. It is end-to-end, not a pipeline: `<image>document parsing.` handles one page and `<image>Multi page parsing.` several images or a PDF. Output is Markdown with `<|ref|>`/`<|det|>` grounding tags that callers strip. The repo was updated on 2026-10-14 and has about 1.16 million downloads.

## Strengths
- Constant memory and speed over long outputs; the vLLM recipe says one 8 GB GPU suffices for BF16.
- Serving: transformers 4.57.1 with `trust_remote_code` (`infer` and `infer_multi`), the dedicated vLLM image `vllm/vllm-openai:unlimited-ocr` (vLLM 0.25.0 or later, served name `baidu/Unlimited-OCR`, OpenAI-compatible `/v1`), an SGLang development wheel, Baidu Cloud's asynchronous Unlimited-OCR API (JSON and Markdown, PDFs up to 500 pages), a ModelScope mirror and ms-swift training.

## Limitations
- Needs an n-gram no-repeat logits processor (size 35, window 128 or 1,024 multi-page) or it loops on coordinate tokens; no chat template, prompts must start with `<image>`, and `skip_special_tokens` must be false.
- The model card and abstract give no benchmark scores and no language list beyond "multilingual".
- vLLM support is not in a stable pip wheel; SGLang needs a development build; no GGUF or MLX.

## Good for
- Long multi-page PDFs transcribed in one pass.
- Memory-constrained GPUs where KV-cache growth is the bottleneck.
- Baidu Cloud users wanting the hosted API with cross-page table merging.
