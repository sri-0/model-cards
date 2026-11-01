---
id: deepseek/deepseek-v4-flash-vision-exp
name: DeepSeek V4 Flash Vision Exp
owned_by: deepseek
type: llm
description: DeepSeek V4 Flash Vision Exp is an experimental August 2026 multimodal version of DeepSeek V4 Flash 0731 (284B MoE, 13B active, MIT) that adds image understanding for agents.
aliases: [deepseek-ai/DeepSeek-V4-Flash-Vision-Exp, deepseek-v4-flash-vision-exp]
context_length: 1048576
max_output_tokens: 262144
capabilities: [tool_calling, reasoning, vision, structured_output]
supported_parameters: [frequency_penalty, include_reasoning, logit_bias, logprobs, max_tokens, min_p, presence_penalty, reasoning, reasoning_effort, repetition_penalty, response_format, seed, stop, structured_outputs, temperature, tool_choice, tools, top_k, top_logprobs, top_p]
architecture:
  input_modalities: [text, image]
  output_modalities: [text]
  tokenizer: DeepSeek
open_weights: true
license: MIT
release_date: "2026-08-21"
pricing:
  input: 0.2156
  output: 0.6468
  cache_read: 0.00686
benchmarks:
  intelligence_index: 34.8
  coding_index: 65
  agentic_index: 47.5
  omniscience_index: -17.6
  humanitys_last_exam: 34.5
  gpqa_diamond: 91.3
  scicode: 49.7
  terminal_bench_4: 12.1
  long_context_reasoning: 81.3
  mmmu_pro: 74.8
  output_tokens_per_second: 173
  time_to_first_token_seconds: 1.16
benchmark_variant: DeepSeek V4 Flash Vision (Max)
sources:
  - https://openrouter.ai/deepseek/deepseek-v4-flash-vision-exp
  - https://openrouter.ai/api/v1/models
  - https://artificialanalysis.ai/models/deepseek-v4-flash-vision
  - https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash-Vision-Exp
  - https://api-docs.deepseek.com/news/news260821
  - https://api-docs.deepseek.com/updates
  - https://api-docs.deepseek.com/quick_start/pricing
  - https://api-docs.deepseek.com/guides/vision
retrieved: "2026-10-16"
---

# DeepSeek V4 Flash Vision Exp

## Overview
DeepSeek V4 Flash Vision Exp is DeepSeek's first experimental multimodal V4 model: V4 Flash 0731 (284B MoE, 13B active, 1M context) with vision modules added and continued training. It reached the vendor API on 2026-08-21 as `deepseek-v4-flash-vision-exp`; the weights followed on Hugging Face on 2026-08-31 under the MIT licence, so `open_weights` and `license` here follow the Hugging Face card rather than the earlier proprietary listing. DeepSeek retired it on 2026-09-10 and now routes the legacy id to V4.1 Flash, which has native vision; the model remains available from the weights and on OpenRouter (output limit 262,144 tokens). Superseded by `deepseek/deepseek-v4.1-flash`.

## Strengths
- Text agent parity with 0731 per DeepSeek: Terminal Bench 2.1 83.9, NL2Repo 57.7, DeepSWE 59.3, Toolathlon-Verified 75.9.
- Multimodal agents: ApexBench 36.5, Agents' Last Exam 27.3, Chartography 64.3, ZeroBench 35.0 (pass@5), which DeepSeek describes as close to Opus 4.8.
- Artificial Analysis (variant DeepSeek V4 Flash Vision (Max)): MMMU-Pro 74.8%, Agentic Index 47.5, GPQA Diamond 91.3%, long-context reasoning 81.3%, 173 tokens per second.
- Images in JPEG, PNG, GIF or WebP via base64, URL or the Files API; the vendor billed each image at up to 384 tokens.

## Limitations
- Experimental, and retired from the vendor API after three weeks.
- Terminal-Bench 4.0 12.1%, Omniscience Index -17.6.
- Self-hosting needs the `vllm/vllm-openai:deepseekv4-flash-vision` image or SGLang with DSPARK on four GPUs (DeepSeek's example uses GB300); no Jinja template.

## Good for
- Document, chart and screenshot understanding inside agent loops.
- Computer-use style workflows mixing text and images.
- Reproducing DeepSeek's multimodal agent benchmarks.
