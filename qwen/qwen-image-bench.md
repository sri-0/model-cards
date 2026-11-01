---
id: qwen/qwen-image-bench
name: Qwen Image Bench Q-Judger
owned_by: qwen
type: llm
description: Q-Judger (Hugging Face repo Qwen-Image-Bench) is Qwen's May 2026 open-weight (Apache-2.0) judge model, fine-tuned from Qwen3.6-27B, that scores text-to-image outputs against a prompt and returns structured JSON.
aliases: [Qwen/Qwen-Image-Bench]
context_length: 262144
capabilities: [reasoning, vision, structured_output]
architecture:
  input_modalities: [text, image]
  output_modalities: [text]
open_weights: true
license: Apache-2.0
release_date: "2026-05-21"
sources:
  - https://huggingface.co/Qwen/Qwen-Image-Bench
  - https://huggingface.co/api/models/Qwen/Qwen-Image-Bench
  - https://huggingface.co/Qwen/Qwen-Image-Bench/raw/main/config.json
  - https://openrouter.ai/api/v1/models
retrieved: "2026-11-01"
---

# Qwen Image Bench Q-Judger

## Overview
Q-Judger is the judge model of Qwen-Image-Bench, a benchmark for text-to-image generation. Its Hugging Face repo was created on 2026-05-21, which this card uses as the release date; the paper is arXiv 2605.28091. OpenRouter does not list it and Artificial Analysis has no page for it; the id follows the Hugging Face repo name. It is fine-tuned from Qwen3.6-27B (Hugging Face counts 27.4B parameters; config.json sets 262,144 positions). Given a text prompt and a generated image, it reasons in thinking mode and then outputs JSON scores per sub-dimension: 0 (fail), 1 (pass), 2 (excel) or N/A, mapped to 0, 60 and 100 and averaged up a three-level hierarchy. The five top-level dimensions are Quality, Aesthetics, Alignment, Real-world Fidelity and Creative Generation, covering areas such as text rendering, world knowledge, fairness and visual storytelling. Qwen's judge.py script in the Qwen-Image-Bench GitHub repository runs it through ms-swift.

## Strengths
- Qwen reports Spearman rank correlations with human expert rankings of 0.89 to 0.92 per dimension and 0.92 overall, across 18 text-to-image models.
- Fine-grained, checklist-based scores rather than one number.

## Limitations
- Qwen's judge script expects prompt ids 1 to 1,000 that match the benchmark metadata.
- Qwen's validation covers model-level rankings across 18 models, not per-image agreement with people.
- Not a general assistant; no published knowledge cutoff.

## Good for
- Evaluating text-to-image models on Qwen-Image-Bench.
- Automated image quality review in generation pipelines.
- Research on vision-language judges.
