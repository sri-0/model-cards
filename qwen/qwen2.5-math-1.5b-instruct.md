---
id: qwen/qwen2.5-math-1.5b-instruct
name: Qwen2.5 Math 1.5B Instruct
owned_by: qwen
type: llm
description: Qwen2.5 Math 1.5B Instruct is Qwen's September 2024 open-weight (Apache-2.0) 1.5B maths model that solves English and Chinese maths problems with chain-of-thought and tool-integrated (Python) reasoning.
aliases: [Qwen/Qwen2.5-Math-1.5B-Instruct, qwen2.5-math-1.5b-instruct]
context_length: 4096
architecture:
  input_modalities: [text]
  output_modalities: [text]
open_weights: true
license: Apache-2.0
release_date: "2024-09-19"
sources:
  - https://huggingface.co/Qwen/Qwen2.5-Math-1.5B-Instruct
  - https://huggingface.co/api/models/Qwen/Qwen2.5-Math-1.5B-Instruct
  - https://huggingface.co/api/models?author=Qwen&limit=1000
  - https://huggingface.co/Qwen/Qwen2.5-Math-1.5B-Instruct/raw/main/config.json
  - https://qwenlm.github.io/blog/qwen2.5-math/
  - https://web.archive.org/web/20260606135246/https://www.alibabacloud.com/help/en/model-studio/models
  - https://openrouter.ai/api/v1/models
retrieved: "2026-11-01"
---

# Qwen2.5 Math 1.5B Instruct

## Overview
Qwen2.5-Math-1.5B-Instruct was released in the Qwen2.5-Math blog post of 2024-09-19 with 1.5B, 7B and 72B base and instruct models and the Qwen2.5-Math-RM-72B reward model (the Hugging Face repo was created 2024-09-16). OpenRouter does not list it and Artificial Analysis has no page for it; the id follows the Hugging Face repo. It starts from the Qwen2.5 base model, is pretrained on Qwen Math Corpus v2 (over 1T tokens), and is post-trained with rejection sampling and GRPO reinforcement learning guided by the reward model. Unlike Qwen2-Math it handles Chinese as well as English, and adds tool-integrated reasoning (TIR), where it writes Python to compute answers. Hugging Face counts 1.54B parameters; config.json sets a 4,096-token context. It needs transformers 4.37.0 or newer. Alibaba Cloud Model Studio (archived 2026-06-06) lists qwen2.5-math-1.5b-instruct in the Beijing region only, free for a limited time.

## Strengths
- Qwen reports MATH 79.7 with tool-integrated reasoning, and says the 1.5B model solves 29 of 40 AMC 2023 problems with RM@256 sampling in CoT mode.
- The blog says even this size outperforms most current models on MATH when it can use a Python interpreter.
- The blog describes 13-gram and subsequence decontamination of training data against the evaluation sets.

## Limitations
- Qwen says the series mainly supports English and Chinese maths through CoT and TIR and does not recommend it for other tasks.
- 4,096-token context; TIR needs a code interpreter, such as Qwen-Agent's demo.
- No published knowledge cutoff.

## Good for
- Low-cost maths tutoring and step checking.
- Generating worked solutions for maths datasets.
- Research on tool-integrated reasoning.
