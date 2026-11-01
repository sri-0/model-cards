---
id: qwen/webworld-14b
name: WebWorld 14B
owned_by: qwen
type: llm
description: WebWorld 14B is Qwen's February 2026 open-weight (Apache-2.0) web world model, fine-tuned from Qwen3-14B to predict the next page state of a website after a web agent's action.
aliases: [Qwen/WebWorld-14B]
context_length: 40960
capabilities: [reasoning]
architecture:
  input_modalities: [text]
  output_modalities: [text]
open_weights: true
license: Apache-2.0
release_date: "2026-02-13"
sources:
  - https://huggingface.co/Qwen/WebWorld-14B
  - https://huggingface.co/api/models/Qwen/WebWorld-14B
  - https://huggingface.co/Qwen/WebWorld-14B/raw/main/config.json
  - https://openrouter.ai/api/v1/models
retrieved: "2026-11-01"
---

# WebWorld 14B

## Overview
WebWorld-14B is one of three open-web world models (8B, 14B, 32B) that Qwen built for training and evaluating web agents. Its Hugging Face repo was created on 2026-02-13, which this card uses as the release date; the paper is arXiv 2602.14721. OpenRouter does not list it and Artificial Analysis has no page for it; the id follows the Hugging Face repo. The model card's series table gives Qwen3-14B as the base model, and config.json sets 40,960 positions. Trained on more than a million real web interaction trajectories, it takes the current page state and an agent action (click, fill, scroll, goto, tab and keyboard actions) and predicts the next state, keeping the input format: accessibility tree, HTML, XML, Markdown or plain language. It uses chain-of-thought reasoning for transitions and simulates more than 30 steps. Qwen recommends the 14B and 32B sizes for higher-fidelity simulation and long-horizon robustness. It loads with transformers (vLLM optional).

## Strengths
- Qwen reports average Factuality and Web Turing scores of 70.7 and 44.7 on WebWorld-Bench, against 71.3 and 47.4 for Claude Opus 4.1, 70.3 and 43.2 for Gemini 3 Pro and 59.5 and 35.4 for GPT-4o.
- Qwen reports agent-training gains with WebWorld data of 8.3 points on MiniWob++ and 9.2 on WebArena for Qwen3-14B.
- Qwen says WebWorld beats GPT-5 as a world model for inference-time lookahead search.

## Limitations
- Not a chat or agent model: it simulates environments rather than completing tasks.
- Qwen recommends task-specific fine-tuning on in-domain trajectories for the best results in a given environment.
- No published knowledge cutoff.

## Good for
- Higher-fidelity simulation than the 8B size at moderate cost.
- Offline training and testing of browser agents without live sites.
- Research on world models for web navigation.
