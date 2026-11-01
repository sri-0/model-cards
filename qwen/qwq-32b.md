---
id: qwen/qwq-32b
name: QwQ 32B
owned_by: qwen
type: llm
description: QwQ 32B is Qwen's March 2025 open-weight (Apache-2.0) 32.5B-parameter reasoning model, post-trained from Qwen2.5-32B with scaled reinforcement learning so that it always thinks before answering.
aliases: [Qwen/QwQ-32B, Qwen/QwQ-32B-AWQ, Qwen/QwQ-32B-GGUF, qwq-32b, "qwq:32b"]
context_length: 40960
capabilities: [tool_calling, reasoning]
architecture:
  input_modalities: [text]
  output_modalities: [text]
open_weights: true
license: Apache-2.0
release_date: "2025-03-06"
benchmarks:
  gpqa_diamond: 59.3
  humanitys_last_exam: 7.3
  ifbench: 38.8
  long_context_reasoning: 26.7
benchmark_variant: QwQ 32B
sources:
  - https://huggingface.co/Qwen/QwQ-32B
  - https://huggingface.co/api/models/Qwen/QwQ-32B
  - https://huggingface.co/api/models?author=Qwen&limit=1000
  - https://huggingface.co/Qwen/QwQ-32B/raw/main/config.json
  - https://huggingface.co/Qwen/QwQ-32B/raw/main/tokenizer_config.json
  - https://artificialanalysis.ai/models/qwq-32b
  - https://qwenlm.github.io/blog/qwq-32b/
  - https://qwenlm.github.io/blog/qwen3/
  - https://ollama.com/library/qwq/tags
  - https://web.archive.org/web/20260606135246/https://www.alibabacloud.com/help/en/model-studio/models
  - https://openrouter.ai/api/v1/models
retrieved: "2026-11-01"
---

# QwQ 32B

## Overview
QwQ-32B is Qwen's medium-sized reasoning model. The Qwen blog announces it on 2025-03-06 (Artificial Analysis and the Hugging Face repo give 2025-03-05). OpenRouter does not list it; the id follows the Hugging Face repo Qwen/QwQ-32B. It starts from Qwen2.5-32B: after a cold start, reinforcement learning first targets maths and coding with an answer verifier and a code execution server, then general abilities. The Hugging Face card gives 32.5B parameters (31.0B non-embedding), 64 layers, 40 query and 8 key-value heads and a full 131,072-token context, the figure Artificial Analysis lists; config.json sets 40,960 positions, which this card uses, and Qwen says to enable YaRN for prompts over 8,192 tokens. Replies always open with a think block. Qwen recommends temperature 0.6, top_p 0.95 and top_k 20 to 40, not greedy decoding. Alibaba Cloud Model Studio (archived 2026-06-06) serves qwq-32b only in the Beijing region, at $0.287 per million input and $0.861 per million output tokens. Ollama serves it as qwq:32b. Artificial Analysis marks it deprecated in favour of Qwen3 32B.

## Strengths
- Qwen says it performs comparably to DeepSeek-R1 (671B total parameters); the blog's benchmark chart is an image.
- The blog says agent abilities are built in, so it uses tools and adapts its reasoning to feedback; the chat template includes tool calls.
- Artificial Analysis (QwQ 32B): GPQA Diamond 59.3%, IFBench 38.8%, long-context reasoning 26.7%.

## Limitations
- Artificial Analysis Humanity's Last Exam 7.3%; no Intelligence Index, agent or speed figures.
- No non-thinking mode; the Qwen3 blog says Qwen3-30B-A3B outperforms it with a tenth of the active parameters.
- Static YaRN in vLLM can hurt short prompts.
- Ollama's q4_K_M build is 20 GB and the fp16 build 66 GB.

## Good for
- Self-hosted maths and coding reasoning.
- Research on RL-trained reasoners.
- Pipelines built on QwQ's output format.
