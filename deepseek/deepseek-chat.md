---
id: deepseek/deepseek-chat
name: DeepSeek V3
owned_by: deepseek
type: llm
description: DeepSeek V3 is DeepSeek's December 2024 Mixture-of-Experts chat model (671B parameters, 37B active) whose weights are released under the DeepSeek Model License.
aliases: [deepseek-ai/DeepSeek-V3, deepseek-chat, "deepseek-v3:671b"]
context_length: 163840
max_output_tokens: 16384
capabilities: [tool_calling, structured_output]
supported_parameters: [frequency_penalty, logit_bias, max_tokens, min_p, presence_penalty, repetition_penalty, response_format, seed, stop, structured_outputs, temperature, tool_choice, tools, top_k, top_p]
architecture:
  input_modalities: [text]
  output_modalities: [text]
  tokenizer: DeepSeek
open_weights: true
license: DEEPSEEK LICENSE AGREEMENT
release_date: "2024-12-26"
knowledge_cutoff: "2024-07"
pricing:
  input: 0.32
  output: 0.89
benchmarks:
  intelligence_index: 8.5
  omniscience_index: -41.6
  humanitys_last_exam: 2.9
  gpqa_diamond: 55.7
  scicode: 35.8
  terminal_bench_hard: 6.8
  terminal_bench_4: 0
  long_context_reasoning: 29.3
  ifbench: 34.8
  tau2_bench: 22.8
  output_tokens_per_second: 37
  time_to_first_token_seconds: 1.3
benchmark_variant: "DeepSeek V3 (Dec '24)"
sources:
  - https://openrouter.ai/deepseek/deepseek-chat
  - https://openrouter.ai/api/v1/models
  - https://artificialanalysis.ai/models/deepseek-v3
  - https://huggingface.co/deepseek-ai/DeepSeek-V3
  - https://api-docs.deepseek.com/news/news1226
  - https://api-docs.deepseek.com/updates
  - https://api-docs.deepseek.com/quick_start/pricing
  - https://huggingface.co/deepseek-ai/DeepSeek-V3/blob/main/LICENSE-MODEL
  - https://ollama.com/library/deepseek-v3
retrieved: "2026-10-16"
---

# DeepSeek V3

## Overview
DeepSeek V3 was released on 2024-12-26 as a Mixture-of-Experts model with 671B total parameters and 37B activated per token, built on Multi-head Latent Attention and DeepSeekMoE and pre-trained on 14.8 trillion tokens with FP8 training. The Hugging Face card gives a 128K context; OpenRouter lists 163,840 tokens and a 16,384-token output limit. The vendor API id `deepseek-chat` served it until 2025-03-24, when the same id moved to DeepSeek V3 0324; the id was retired on 2026-07-24, so the model is now available only as weights or through third parties (OpenRouter routes to two providers). The code is MIT, but the weights are under the DeepSeek Model License, which permits commercial use. Superseded by `deepseek/deepseek-chat-v3-0324`.

## Strengths
- DeepSeek reports MMLU-Pro 75.9, MATH-500 90.2, AIME 2024 39.2, LiveCodeBench 40.5 and SWE-bench Verified 42.0 for the chat model.
- Function calling, JSON output and FIM completion.
- Low OpenRouter price: $0.32 input and $0.89 output per million tokens.

## Limitations
- No thinking mode; Artificial Analysis Intelligence Index 8.5 and Terminal-Bench Hard 6.8% (variant DeepSeek V3 (Dec '24)).
- Omniscience Index -41.6, so factual recall needs checking.
- Slow in AA's measurement: 37 tokens per second and 1.3 s to first token.
- Self-hosting needs a multi-GPU node: FP8 weights only (685B on disk including 14B of MTP weights), Transformers not supported directly; use SGLang, vLLM 0.6.6 or later, LMDeploy or TensorRT-LLM. The Ollama tag `deepseek-v3:671b` is 404 GB and needs Ollama 0.5.5 or later.

## Good for
- Pipelines pinned to the December 2024 weights.
- Low-cost chat, code and Chinese-language tasks that do not need reasoning.
- Research on the V3 architecture (MLA, auxiliary-loss-free load balancing, multi-token prediction).
