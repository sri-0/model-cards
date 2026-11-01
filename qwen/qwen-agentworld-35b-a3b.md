---
id: qwen/qwen-agentworld-35b-a3b
name: Qwen AgentWorld 35B A3B
owned_by: qwen
type: llm
description: Qwen AgentWorld 35B A3B is Qwen's June 2026 open-weight (Apache-2.0) language world model, a 35B mixture-of-experts (3B active) that simulates agent environments across seven domains by predicting the next environment state.
aliases: [Qwen/Qwen-AgentWorld-35B-A3B]
context_length: 262144
capabilities: [reasoning]
architecture:
  input_modalities: [text]
  output_modalities: [text]
open_weights: true
license: Apache-2.0
release_date: "2026-06-22"
sources:
  - https://huggingface.co/Qwen/Qwen-AgentWorld-35B-A3B
  - https://huggingface.co/api/models/Qwen/Qwen-AgentWorld-35B-A3B
  - https://huggingface.co/Qwen/Qwen-AgentWorld-35B-A3B/raw/main/config.json
  - https://openrouter.ai/api/v1/models
retrieved: "2026-11-01"
---

# Qwen AgentWorld 35B A3B

## Overview
Qwen-AgentWorld-35B-A3B is a language world model: given an agent's action and the interaction history, it reasons with long chain of thought and predicts the next environment state. Its Hugging Face repo was created on 2026-06-22, which this card uses as the release date; the technical report is arXiv 2606.24597. OpenRouter does not list it and Artificial Analysis has no page for it; the id follows the Hugging Face repo. It starts from Qwen3.5-35B-A3B-Base and was trained in three stages: continual pre-training on environment knowledge, supervised fine-tuning for next-state prediction, and GSPO reinforcement learning for fidelity. The card gives 35B total and 3B activated parameters, 40 layers mixing Gated DeltaNet and gated attention, 256 experts (8 routed plus 1 shared) and a 262,144-token context; Qwen advises keeping at least 128K tokens. One model covers seven domains: MCP tool calling, search, terminal, software engineering, Android, web and OS. vLLM needs --language-model-only because the checkpoint has no vision weights.

## Strengths
- Qwen reports an AgentWorldBench overall score of 56.39, against 47.73 for Qwen3.5-35B-A3B and 56.59 for Claude Opus 4.8.
- Qwen says it generalises zero-shot to unseen environments and that world-model RL warm-up transfers to multi-turn tool-calling agent tasks.
- Domain system prompts are published in the GitHub repository.

## Limitations
- Simulates environments; it is not a general assistant.
- GPT-5.4 (58.25) and Claude Opus 4.6 (57.80) score higher overall, as does Qwen-AgentWorld-397B-A17B (58.71), which is not on Hugging Face.
- No published knowledge cutoff.

## Good for
- Training agents against simulated tools, terminals and GUIs.
- Building fictional or perturbed test environments.
- Research on language world models.
