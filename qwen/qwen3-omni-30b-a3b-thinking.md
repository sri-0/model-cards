---
id: qwen/qwen3-omni-30b-a3b-thinking
name: Qwen3 Omni 30B A3B Thinking
owned_by: qwen
type: llm
description: Qwen3 Omni 30B A3B Thinking is the reasoning model of Qwen's September 2025 Qwen3-Omni release, an open-weight (Apache-2.0) mixture-of-experts Thinker that reasons over text, images, audio and video and answers in text.
aliases: [Qwen/Qwen3-Omni-30B-A3B-Thinking]
context_length: 65536
capabilities: [tool_calling, reasoning, vision]
architecture:
  input_modalities: [text, image, audio, video]
  output_modalities: [text]
open_weights: true
license: Apache-2.0
release_date: "2025-09-22"
benchmarks:
  gpqa_diamond: 72.6
  humanitys_last_exam: 7.5
  ifbench: 43.4
  long_context_reasoning: 0
  mmmu_pro: 60.2
  output_tokens_per_second: 102.2
  tau2_bench: 21.3
  terminal_bench_hard: 3.8
  time_to_first_token_seconds: 1.9
benchmark_variant: Qwen3 Omni 30B A3B (Reasoning)
sources:
  - https://huggingface.co/Qwen/Qwen3-Omni-30B-A3B-Thinking
  - https://huggingface.co/api/models/Qwen/Qwen3-Omni-30B-A3B-Thinking
  - https://huggingface.co/Qwen/Qwen3-Omni-30B-A3B-Thinking/raw/main/config.json
  - https://artificialanalysis.ai/models/qwen3-omni-30b-a3b
  - https://github.com/QwenLM/Qwen3-Omni
  - https://openrouter.ai/api/v1/models
retrieved: "2026-11-01"
---

# Qwen3 Omni 30B A3B Thinking

## Overview
Qwen3-Omni-30B-A3B-Thinking is the reasoning model of Qwen3-Omni, released on 2025-09-22 according to the Qwen3-Omni GitHub README (Artificial Analysis agrees; the Hugging Face repo was created 2025-09-15). OpenRouter does not list it; the id follows the Hugging Face repo. It contains only the Thinker of Qwen3-Omni's Thinker-Talker design: it takes text, images, audio and video, reasons with chain of thought and returns text only. config.json gives a 48-layer text model with 128 experts (8 active) and 65,536 positions, the context Artificial Analysis also lists; Hugging Face counts 31.7B parameters. It handles 119 text languages and 19 speech input languages. In BF16 with transformers, Qwen gives a minimum of 68.74 GB of GPU memory for a 15-second video, rising to 131.65 GB for 120 seconds. Ollama does not list it.

## Strengths
- Qwen reports text GPQA 73.1, IFEval 85.1 and WritingBench 85.5, and vision MMMU 75.6, MathVista 80.0 and MathVision 62.9.
- Qwen reports VoiceBench overall 88.8 and MMSU 83.0, above the Instruct model's 85.5 and 68.1, and DailyOmni 75.8.
- Artificial Analysis (Qwen3 Omni 30B A3B (Reasoning)): GPQA Diamond 72.6%, MMMU-Pro 60.2%, IFBench 43.4%, 102.2 output tokens per second and 1.9 s to first token.

## Limitations
- Artificial Analysis long-context reasoning 0%, Terminal-Bench Hard 3.8%, tau2-bench 21.3% and Humanity's Last Exam 7.5%.
- No speech output.
- Qwen reports AIME25 73.7 and BFCL-v3 63.2, below Qwen3-30B-A3B-Thinking-2507's 85.0 and 72.4.
- No published knowledge cutoff.

## Good for
- Reasoning over recorded audio such as meetings, lectures and sound scenes.
- Visual maths and science questions.
- Audio-visual question answering where text output is enough.
