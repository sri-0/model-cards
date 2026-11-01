---
id: qwen/qwen3.5-9b
name: Qwen3.5 9B
owned_by: qwen
type: llm
description: "Qwen3.5 9B is Alibaba's 9B-parameter dense open-weight (Apache-2.0) vision-language model with a hybrid Gated DeltaNet and gated attention design, thinking mode and a 262,144-token native context."
aliases: [Qwen/Qwen3.5-9B, "qwen3.5:9b"]
context_length: 262144
max_output_tokens: 32768
capabilities: [tool_calling, reasoning, vision, structured_output]
supported_parameters: [frequency_penalty, include_reasoning, logit_bias, logprobs, max_tokens, min_p, presence_penalty, reasoning, repetition_penalty, response_format, seed, stop, structured_outputs, temperature, tool_choice, tools, top_k, top_logprobs, top_p]
architecture:
  input_modalities: [text, image, video]
  output_modalities: [text]
  tokenizer: Qwen3
open_weights: true
license: Apache-2.0
release_date: "2026-03-02"
pricing:
  input: 0.1
  output: 0.15
benchmarks:
  intelligence_index: 11.2
  coding_index: 23.5
  omniscience_index: -53.5
  humanitys_last_exam: 14.9
  gpqa_diamond: 80.6
  scicode: 29.5
  terminal_bench_hard: 24.2
  terminal_bench_4: 0.5
  long_context_reasoning: 70
  ifbench: 66.7
  tau2_bench: 86.8
  mmmu_pro: 69.2
  output_tokens_per_second: 60.1
  time_to_first_token_seconds: 2.04
benchmark_variant: Qwen3.5 9B (Reasoning)
sources:
  - https://openrouter.ai/qwen/qwen3.5-9b
  - https://openrouter.ai/api/v1/models
  - https://artificialanalysis.ai/models/qwen3-5-9b
  - https://huggingface.co/Qwen/Qwen3.5-9B
  - https://github.com/QwenLM/Qwen3.5
  - https://ollama.com/library/qwen3.5
retrieved: "2026-10-16"
---

# Qwen3.5 9B

## Overview
Qwen3.5-9B was released on 2026-03-02 (date from the QwenLM GitHub README) as the largest of the four small Qwen3.5 models. It is a dense 9B-parameter causal language model with a vision encoder, taking text, image and video input. Its 32 layers repeat three Gated DeltaNet linear-attention blocks followed by one gated attention block, and the model was trained with early fusion on multimodal tokens. The native context is 262,144 tokens, extensible to 1,010,000 with YaRN; OpenRouter lists 262,144 with a 32,768-token output limit. Thinking mode is on by default and can be switched off per request with `enable_thinking: false`. Qwen states support for 201 languages and dialects. Weights are on Hugging Face under Apache-2.0 and Ollama serves the model as `qwen3.5:9b`.

## Strengths
- Qwen reports GPQA Diamond 81.7, MMLU-Pro 82.5, TAU2-Bench 79.1, MMMU-Pro 70.1 and OCRBench 89.2, above GPT-OSS-20B on the knowledge rows (74.8 MMLU-Pro, 71.5 GPQA Diamond).
- Artificial Analysis (Qwen3.5 9B, Reasoning): tau2-bench 86.8%, GPQA Diamond 80.6%, long-context reasoning 70%, MMMU-Pro 69.2%.
- Fits one GPU: Qwen's reference vLLM command uses tensor parallel 1 for the full 262,144-token context.

## Limitations
- Artificial Analysis Intelligence Index 11.2, Coding Index 23.5 and Omniscience -53.5; Terminal-Bench 4.0 0.5% and Terminal-Bench Hard 24.2%.
- 60.1 tokens per second and 2.04 s to first token in AA's test.
- Qwen reports LiveCodeBench v6 65.6, below GPT-OSS-20B (74.6).
- Qwen advises keeping at least 128K tokens of context so thinking is not cut short.

## Good for
- Local multimodal assistants and document, chart or video understanding on a single GPU.
- Tool-calling agents where a 9B model is acceptable.
- Fine-tuning from the Qwen3.5-9B-Base checkpoint.
