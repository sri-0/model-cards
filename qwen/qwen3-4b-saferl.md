---
id: qwen/qwen3-4b-saferl
name: Qwen3 4B SafeRL
owned_by: qwen
type: llm
description: Qwen3 4B SafeRL is a safety-aligned version of Qwen3-4B, released by Qwen in September 2025 under Apache-2.0, trained with reinforcement learning against Qwen3Guard so it refuses harmful prompts without over-refusing.
aliases: [Qwen/Qwen3-4B-SafeRL]
context_length: 40960
capabilities: [tool_calling, reasoning]
architecture:
  input_modalities: [text]
  output_modalities: [text]
open_weights: true
license: Apache-2.0
release_date: "2025-09-30"
sources:
  - https://huggingface.co/Qwen/Qwen3-4B-SafeRL
  - https://huggingface.co/api/models/Qwen/Qwen3-4B-SafeRL
  - https://huggingface.co/Qwen/Qwen3-4B-SafeRL/raw/main/config.json
  - https://huggingface.co/Qwen/Qwen3-4B-SafeRL/raw/main/tokenizer_config.json
  - https://github.com/QwenLM/Qwen3Guard
  - https://openrouter.ai/api/v1/models
retrieved: "2026-11-01"
---

# Qwen3 4B SafeRL

## Overview
Qwen3-4B-SafeRL was released on 2025-09-30, according to the Qwen3Guard GitHub README (the Hugging Face repo was created the same day). OpenRouter does not list it and Artificial Analysis has no page for it; the id follows the Hugging Face repo. It is Qwen3-4B (own card) further trained with reinforcement learning using a hybrid reward: Qwen3Guard-Gen-4B penalises unsafe output and unnecessary refusals, and WorldPM-72B-HelpSteer2 rewards helpfulness. The architecture is unchanged: 4.0B parameters, 36 layers and 40,960 positions in config.json. It keeps Qwen3's hybrid thinking, switchable with enable_thinking, and is used exactly like Qwen3-4B, with transformers 4.51.0 or newer. Ollama and Alibaba Cloud Model Studio do not list it.

## Strengths
- Qwen reports a WildGuard safety rate of 98.1% in non-thinking mode and 97.4% in thinking mode, against 64.7% and 59.0% for Qwen3-4B.
- Refusals on WildGuard fall from 12.9% to 5.3% in non-thinking mode, and Arena-Hard v2 win rate rises from 9.5 to 10.7 (13.7 to 16.6 thinking).
- Apache-2.0, a drop-in replacement for Qwen3-4B.

## Limitations
- Small capability losses in Qwen's table: thinking-mode AIME25 63.5 against 65.6, LiveCodeBench v6 47.5 against 48.4 and GPQA 51.2 against 55.9.
- Non-thinking AIME25 also dips, 18.2 against 19.1; no published knowledge cutoff.

## Good for
- Consumer-facing assistants on small hardware that need safer defaults.
- Research on reinforcement learning for safety alignment.
- A baseline when comparing guard-model rewards.
