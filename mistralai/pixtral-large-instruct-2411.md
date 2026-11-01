---
id: mistralai/pixtral-large-instruct-2411
name: Pixtral Large
owned_by: mistralai
type: llm
description: Pixtral Large is Mistral AI's 124B open-weight (Mistral Research License) multimodal model of November 2024, a 1B vision encoder on top of Mistral Large 2, retired from Mistral's API in May 2026.
aliases: [pixtral-large-2411, mistralai/Pixtral-Large-Instruct-2411, pixtral-large-latest, mistral/pixtral-large-latest, "mistral.pixtral-large-2502-v1:0", "us.mistral.pixtral-large-2502-v1:0", "eu.mistral.pixtral-large-2502-v1:0"]
context_length: 131072
capabilities: [tool_calling, vision, structured_output]
architecture:
  input_modalities: [text, image]
  output_modalities: [text]
open_weights: true
license: Mistral Research License
release_date: "2024-11-18"
benchmarks:
  gpqa_diamond: 50.5
  humanitys_last_exam: 2.8
  ifbench: 34.5
  mmmu_pro: 50.6
  tau2_bench: 36.5
benchmark_variant: Pixtral Large
sources:
  - https://huggingface.co/mistralai/Pixtral-Large-Instruct-2411
  - https://huggingface.co/api/models/mistralai/Pixtral-Large-Instruct-2411
  - https://huggingface.co/mistralai/Pixtral-Large-Instruct-2411/raw/main/params.json
  - https://huggingface.co/mistralai/Pixtral-Large-Instruct-2411/raw/main/README.md
  - https://docs.mistral.ai/getting-started/models
  - https://docs.mistral.ai/models/pixtral-large-24-11
  - https://docs.mistral.ai/resources/changelogs
  - https://artificialanalysis.ai/models/pixtral-large-2411
  - https://mistral.ai/news/pixtral-large
  - https://openrouter.ai/api/v1/models
  - https://raw.githubusercontent.com/BerriAI/litellm/main/model_prices_and_context_window.json
retrieved: "2026-11-01"
---

# Pixtral Large

## Overview
Pixtral Large (version 24.11, API id pixtral-large-2411, alias pixtral-large-latest) was announced on 18 November 2024 as Mistral's first frontier-class multimodal model. OpenRouter does not list it; the id follows the Hugging Face repo mistralai/Pixtral-Large-Instruct-2411, and the Bedrock ids (labelled 2502) come from LiteLLM's catalogue. It pairs a 1B-parameter vision encoder with the 123B Mistral Large 2 (2407) decoder, 124B in total, with 131,072 positions in params.json; Mistral says the 128K window fits at least 30 high-resolution images. Weights are under the Mistral Research License for research and educational use; commercial use needs Mistral's commercial licence. Mistral's models page lists it as deprecated on 27 February 2026 and retired on 31 May 2026, with Mistral Medium 3.5 as the replacement (Artificial Analysis points to Mistral Medium 3.1). Its text-only sibling, Mistral Large 24.11, shares the same release.

## Strengths
- Mistral reports 69.4% on MathVista, 93.3% on DocVQA, 80.9% on VQAv2, 88.1% on ChartQA, 64.0% on MMMU and 7.4 on MM-MT-Bench, ahead of GPT-4o and Gemini 1.5 Pro on documents and charts.
- Artificial Analysis (variant Pixtral Large) measured 50.6% on MMMU-Pro and 36.5% on tau2-bench.
- Structured outputs, function calling, predicted outputs and prefix completion on Mistral's API; LiteLLM lists Mistral's price at $2 input and $6 output per million tokens.

## Limitations
- Research-only licence for the weights; no commercial self-hosting without a Mistral licence.
- Retired from Mistral's API.
- The Hugging Face card says the transformers implementation did not work at release; Mistral recommends vLLM 0.6.4.post1 or later.
- Artificial Analysis measured 2.8% on Humanity's Last Exam and publishes no Intelligence Index for it.

## Good for
- Research on document, chart and natural-image understanding with a large open model.
- Existing pipelines that still run the weights under the research licence.
