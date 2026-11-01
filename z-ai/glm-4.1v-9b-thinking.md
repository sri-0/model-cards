---
id: z-ai/glm-4.1v-9b-thinking
name: GLM-4.1V-9B-Thinking
owned_by: z-ai
type: llm
description: GLM-4.1V-9B-Thinking is Z.ai's open-weight (MIT) 9B vision-language reasoning model, built on GLM-4-9B-0414 and trained with reinforcement learning, with a 64K context and images up to 4K resolution.
aliases: [glm-4.1v-thinking-flash, glm-4.1v-thinking-flashx, zai-org/GLM-4.1V-9B-Thinking]
context_length: 65536
capabilities: [reasoning, vision]
architecture:
  input_modalities: [text, image, video]
  output_modalities: [text]
open_weights: true
license: MIT
release_date: "2025-07-02"
sources:
  - https://huggingface.co/zai-org/GLM-4.1V-9B-Thinking
  - https://huggingface.co/api/models/zai-org/GLM-4.1V-9B-Thinking
  - https://huggingface.co/zai-org/GLM-4.1V-9B-Thinking/raw/main/config.json
  - https://huggingface.co/zai-org/GLM-4.5V
  - https://github.com/zai-org/GLM-4
  - https://docs.bigmodel.cn/cn/guide/models/vlm/glm-4.1v-thinking
  - https://docs.bigmodel.cn/cn/update/new-releases
  - https://openrouter.ai/api/v1/models
retrieved: "2026-11-01"
---

# GLM-4.1V-9B-Thinking

## Overview
GLM-4.1V-9B-Thinking was released on 2025-07-02 as the first reasoning model in Z.ai's GLM-V line, succeeding CogVLM2 and GLM-4V. It is built on the GLM-4-9B-0414 language model and trained with Reinforcement Learning with Curriculum Sampling (RLCS) to think step by step before answering. It handles arbitrary aspect ratios and images up to 4K resolution, reads video, works in Chinese and English, and has a 64K context (65,536 positions in config.json). OpenRouter does not list it; the id follows the Hugging Face repo, where a base model (GLM-4.1V-9B-Base) is also published. Zhipu's bigmodel.cn platform serves the GLM-4.1V-Thinking series as `glm-4.1v-thinking-flashx` (2 yuan per million tokens, high-concurrency) and the free `glm-4.1v-thinking-flash`, both with a 64K window. Weights are MIT-licensed.

## Strengths
- Z.ai reports the best result among 10B-class models on 23 of 28 benchmarks, and better than Qwen2.5-VL-72B on 18.
- Covers chart and video understanding, image question answering, subject problem solving, front-end coding from screenshots and GUI operation.
- Small: about 10B parameters including the vision encoder, served with transformers 4.57.1 or later.

## Limitations
- Superseded by GLM-4.5V and the GLM-4.6V series, including the 9B GLM-4.6V-Flash with native function calling.
- Not on Z.ai's international pricing page; only Zhipu's China platform serves it.
- Deep thinking is built in by default, per Zhipu, with no documented switch to turn it off.

## Good for
- Local multimodal reasoning with a small model: diagrams, charts, screenshots and short videos.
- Research baselines for small vision-language models.
