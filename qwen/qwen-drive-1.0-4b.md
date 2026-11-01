---
id: qwen/qwen-drive-1.0-4b
name: Qwen Drive 1.0 4B
owned_by: qwen
type: llm
description: Qwen Drive 1.0 4B is Qwen's August 2026 open-weight (Apache-2.0) autonomous-driving foundation model that adds 3D perception and trajectory planning modules to an unchanged Qwen3.5-4B vision-language model.
aliases: [Qwen/Qwen-Drive-1.0-4B]
context_length: 32768
capabilities: [vision]
architecture:
  input_modalities: [text, image]
  output_modalities: [text]
open_weights: true
license: Apache-2.0
release_date: "2026-08-27"
sources:
  - https://huggingface.co/Qwen/Qwen-Drive-1.0-4B
  - https://huggingface.co/api/models/Qwen/Qwen-Drive-1.0-4B
  - https://huggingface.co/Qwen/Qwen-Drive-1.0-4B/raw/main/config.json
  - https://openrouter.ai/api/v1/models
retrieved: "2026-11-01"
---

# Qwen Drive 1.0 4B

## Overview
Qwen-Drive-1.0-4B keeps the pretrained Qwen3.5-4B vision-language model untouched and attaches two modules: a BEV perception head for 3D object detection, semantic occupancy and BEV map segmentation, and a Planning Expert that generates future ego trajectories by flow matching (six candidates of 50 points, 5 seconds at 10 Hz). The VLM still answers free-form questions about driving scenes. Its Hugging Face repo was created on 2026-08-27, which this card uses as the release date; the technical report is arXiv 2609.00111. OpenRouter does not list it and Artificial Analysis has no page for it; the id follows the Hugging Face repo. The repo holds the VLM plus perception, planner-sft and planner-rl weights; config.json sets 32,768 positions for the VLM's text model. Inference uses Qwen's code from the QwenLM/Qwen-Drive-1.0 GitHub repository. Training mixes driving data with general vision-language data to limit forgetting.

## Strengths
- Qwen reports NAVSIM PDMS 90.7 (91.4 best-of-6) and WOD-E2E RFS 8.45 validation and 7.91 test for the RL planner, the best scores in its table.
- Driving VQA (SFT model): LingoQA 77.8 and WaymoQA 74.5, against 70.4 and 67.1 for Qwen3.5-4B.
- The SFT model largely keeps general vision: MMStar 75.9 and MMMU 72.7, against 75.3 and 73.4 for Qwen3.5-4B.

## Limitations
- Alpamayo-1.5 leads on AlpaSim at-fault score (0.45 against 0.37) and PAI-AV ADE at 3 seconds (0.35 against 0.42).
- Needs Qwen's custom code; not a standard chat checkpoint.
- No published knowledge cutoff.

## Good for
- Research on vision-language models for autonomous driving.
- Driving-scene question answering and 3D perception studies.
- Open-loop and simulated planning benchmarks.
