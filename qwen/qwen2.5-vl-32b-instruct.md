---
id: qwen/qwen2.5-vl-32b-instruct
name: Qwen2.5 VL 32B Instruct
owned_by: qwen
type: llm
description: Qwen2.5 VL 32B Instruct is Qwen's March 2025 open-weight (Apache-2.0) 32B vision-language model, a Qwen2.5-VL size tuned with reinforcement learning for better maths, fine-grained image reasoning and human-preferred answers.
aliases: [Qwen/Qwen2.5-VL-32B-Instruct, Qwen/Qwen2.5-VL-32B-Instruct-AWQ, qwen2.5-vl-32b-instruct, "qwen2.5vl:32b"]
context_length: 128000
capabilities: [vision, structured_output]
architecture:
  input_modalities: [text, image, video]
  output_modalities: [text]
open_weights: true
license: Apache-2.0
release_date: "2025-03-24"
sources:
  - https://huggingface.co/Qwen/Qwen2.5-VL-32B-Instruct
  - https://huggingface.co/api/models/Qwen/Qwen2.5-VL-32B-Instruct
  - https://huggingface.co/api/models?author=Qwen&limit=1000
  - https://huggingface.co/Qwen/Qwen2.5-VL-32B-Instruct/raw/main/config.json
  - https://qwenlm.github.io/blog/qwen2.5-vl-32b/
  - https://github.com/QwenLM/Qwen3-VL
  - https://ollama.com/library/qwen2.5vl/tags
  - https://web.archive.org/web/20260606135246/https://www.alibabacloud.com/help/en/model-studio/models
  - https://openrouter.ai/api/v1/models
retrieved: "2026-11-01"
---

# Qwen2.5 VL 32B Instruct

## Overview
Qwen2.5-VL-32B-Instruct joined the Qwen2.5-VL series two months after launch. The Qwen blog post is dated 2025-03-24, which this card uses; the GitHub README says 2025-03-25 and the Hugging Face repo was created 2025-03-21. OpenRouter does not list it and Artificial Analysis has no page for it; the id follows the Hugging Face repo. Qwen says reinforcement learning gave it more detailed, better-formatted answers, stronger maths and finer image understanding than the earlier sizes. It shares the Qwen2.5-VL design: dynamic resolution and frame rate, time-aligned mRoPE and a window-attention ViT. config.json sets max_position_embeddings to 128,000, which this card uses; the model card says the config is set for 32,768 tokens and advises against YaRN for localisation tasks. Ollama serves it as qwen2.5vl:32b (21 GB). Alibaba Cloud Model Studio (archived 2026-06-06) lists qwen2.5-vl-32b-instruct in Singapore at $1.40 per million input and $4.20 per million output tokens.

## Strengths
- Qwen reports MMMU 70.0, MMMU-Pro 49.5, MathVista 74.7, MathVision 40.0 (above Qwen2.5-VL-72B's 38.1), DocVQA 94.8 and ScreenSpot 88.5.
- The blog says it beats Mistral-Small-3.1-24B and Gemma-3-27B-IT and surpasses Qwen2-VL-72B-Instruct, especially on MMMU, MMMU-Pro and MathVista.
- Text scores: MMLU 78.4, MMLU-Pro 68.8, MATH 82.2, GPQA Diamond 46.0 and HumanEval 91.5.

## Limitations
- Qwen reports AndroidWorld 22.0 and OSWorld 5.92, against 35 and 8.83 for Qwen2.5-VL-72B.
- Gemma-3-27B-IT leads it on MATH (89 against 82.2) in Qwen's text table.
- No reasoning mode, and the chat template has no tool-call support.
- No published knowledge cutoff.

## Good for
- Visual maths and STEM questions.
- Document and chart analysis that needs detailed answers.
- A smaller alternative to Qwen2.5-VL-72B for self-hosting.
