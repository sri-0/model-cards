---
id: moonshotai/kimi-dev-72b
name: Kimi-Dev-72B
owned_by: moonshotai
type: llm
description: Kimi-Dev-72B is Moonshot AI's open-weight (MIT) coding model for software-engineering issue resolution, a dense 72B model fine-tuned from Qwen2.5-72B with reinforcement learning on real repositories.
aliases: [moonshotai/Kimi-Dev-72B]
context_length: 131072
architecture:
  input_modalities: [text]
  output_modalities: [text]
open_weights: true
license: MIT
release_date: "2025-06-16"
sources:
  - https://huggingface.co/moonshotai/Kimi-Dev-72B
  - https://huggingface.co/api/models/moonshotai/Kimi-Dev-72B
  - https://huggingface.co/moonshotai/Kimi-Dev-72B/raw/main/config.json
  - https://github.com/MoonshotAI/Kimi-Dev
  - https://openrouter.ai/api/v1/models
retrieved: "2026-11-01"
---

# Kimi-Dev-72B

## Overview
Kimi-Dev-72B is Moonshot AI's open-source coding model for resolving GitHub-style issues, published on Hugging Face on 2025-06-16. It is a dense model fine-tuned from Qwen2.5-72B (Qwen2 architecture, 80 layers, 131,072 positions in config.json) and optimised with large-scale reinforcement learning: it patches real repositories inside Docker and is rewarded only when the whole test suite passes. Moonshot's GitHub repository ships an Agentless-style, two-stage rollout: file localisation, then code editing on the complete located files, in two roles, BugFixer and TestWriter. OpenRouter does not list it; the id follows the Hugging Face repo. Weights are MIT-licensed.

## Strengths
- Moonshot reports 60.4% on SWE-bench Verified, which it describes as the best open-source result at release.
- Rewards tied to full test-suite passes push it towards patches that actually run.
- Standard transformers and vLLM serving; Moonshot's example uses vLLM with tensor parallelism 8.
- Writes unit tests as well as fixes, through the TestWriter role.

## Limitations
- A June 2025 specialist: later general models, including Moonshot's own Kimi K2 releases, report higher SWE-bench Verified scores.
- 72B dense parameters need several GPUs at full precision.
- Tuned for the repository-repair workflow; Moonshot publishes no general chat or tool-calling results.
- The rollout code expects preprocessed repository-structure data from the Agentless project.

## Good for
- Research on automated program repair and SWE-bench-style evaluation.
- Self-hosted bug-fixing and test-writing pipelines.
