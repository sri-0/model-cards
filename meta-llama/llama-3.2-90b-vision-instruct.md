---
id: meta-llama/llama-3.2-90b-vision-instruct
name: Llama 3.2 90B Vision Instruct
owned_by: meta
type: llm
description: Llama 3.2 90B Vision Instruct is Meta's larger open-weight Llama 3.2 multimodal model, adding image understanding to a Llama 3.1 text model through a cross-attention vision adapter.
aliases: [meta-llama/Llama-3.2-90B-Vision-Instruct, "llama3.2-vision:90b", "meta.llama3-2-90b-instruct-v1:0", meta/llama-3.2-90b-vision-instruct-maas, meta-llama/llama-3-2-90b-vision-instruct]
context_length: 128000
capabilities: [tool_calling, vision]
architecture:
  input_modalities: [text, image]
  output_modalities: [text]
open_weights: true
license: Llama 3.2 Community License
release_date: "2024-09-25"
knowledge_cutoff: "2023-12"
benchmarks:
  gpqa_diamond: 43.2
  humanitys_last_exam: 4.5
  mmmu_pro: 39.5
benchmark_variant: Llama 3.2 Instruct 90B (Vision)
sources:
  - https://huggingface.co/meta-llama/Llama-3.2-90B-Vision-Instruct
  - https://huggingface.co/api/models/meta-llama/Llama-3.2-90B-Vision-Instruct
  - https://artificialanalysis.ai/models/llama-3-2-instruct-90b-vision
  - https://dev.meta.ai/llama/docs/model-cards-and-prompt-formats/llama3_2
  - https://docs.aws.amazon.com/bedrock/latest/userguide/model-lifecycle-legacy.html
  - https://ollama.com/library/llama3.2-vision
  - https://github.com/BerriAI/litellm/blob/main/model_prices_and_context_window.json
  - https://openrouter.ai/api/v1/models
retrieved: "2026-11-01"
---

# Llama 3.2 90B Vision Instruct

## Overview
Llama 3.2 90B Vision Instruct (88.8B parameters) is the larger of Meta's two Llama 3.2 multimodal models, released on September 25, 2024. OpenRouter does not list it; the id follows the Hugging Face repo `meta-llama/Llama-3.2-90B-Vision-Instruct`. Meta adds a separately trained vision adapter, a set of cross-attention layers fed by an image encoder, to a Llama 3.1 text model, trained on 6B image-text pairs. It takes text, or text plus an image, and returns text; with text-only input it behaves like the Llama 3.1 text models, including their tool calling. Meta gives a 128k context window (Artificial Analysis lists 128,000 tokens) and a December 2023 cutoff. Lifecycle: Amazon Bedrock retired `meta.llama3-2-90b-instruct-v1:0` on 2026-07-07.

## Strengths
- Meta's image results: 60.3 MMMU (val), 45.2 MMMU-Pro Standard, 90.1 DocVQA, 85.5 ChartQA, 92.3 AI2 Diagram and 57.3 MathVista.
- Meta's text results equal those of Llama 3.1 70B: 86.0 MMLU (CoT), 68.0 MATH and 86.9 MGSM.
- Ahead of the 11B on Artificial Analysis (Llama 3.2 Instruct 90B (Vision)): 39.5% on MMMU-Pro and 43.2% on GPQA Diamond.

## Limitations
- English is the only supported language for image-plus-text tasks, and tool calling is not supported when the input includes an image.
- Meta says the Llama 3.2 multimodal models are not accessible from the EU.
- Large to self-host: Ollama's `llama3.2-vision:90b` package is 55 GB.
- Artificial Analysis publishes only three results for it (4.5% on Humanity's Last Exam), with no speed figures.

## Good for
- Higher-accuracy English document, chart and diagram understanding.
- Visual question answering where the 11B is not accurate enough.
- Replacing a Llama 3.1 70B deployment that now needs image input.
