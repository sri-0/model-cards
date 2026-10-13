---
id: meta/muse-glimmer-30b
name: Muse Glimmer 30B
owned_by: meta
type: llm
description: Muse Glimmer 30B is Meta Superintelligence Labs' dense, open-weight (Apache-2.0) multimodal model, distilled from Muse Spark to run agents locally on consumer hardware.
aliases: [muse-glimmer-30b, meta-models/Muse-Glimmer-30B]
context_length: 131072
max_output_tokens: 16384
capabilities: [tool_calling, reasoning, vision, structured_output]
supported_parameters: [frequency_penalty, include_reasoning, logit_bias, max_tokens, min_p, presence_penalty, reasoning, reasoning_effort, repetition_penalty, response_format, seed, stop, structured_outputs, temperature, tool_choice, tools, top_k, top_p]
architecture:
  input_modalities: [text, image]
  output_modalities: [text]
  tokenizer: Other
open_weights: true
license: Apache-2.0
release_date: "2026-08-10"
knowledge_cutoff: "2026-01"
pricing:
  input: 0.3
  output: 1.2
  cache_read: 0.04
benchmarks:
  intelligence_index: 17.5
  coding_index: 49
  agentic_index: 8.5
  omniscience_index: -32.9
  humanitys_last_exam: 22
  gpqa_diamond: 83.5
  scicode: 44.9
  terminal_bench_4: 0.5
  long_context_reasoning: 83.3
  mmmu_pro: 74.3
  output_tokens_per_second: 124.2
  time_to_first_token_seconds: 0.99
benchmark_variant: Muse Glimmer (High)
sources:
  - https://openrouter.ai/meta/muse-glimmer-30b
  - https://openrouter.ai/api/v1/models
  - https://artificialanalysis.ai/models/muse-glimmer
  - https://huggingface.co/meta-models/Muse-Glimmer-30B
  - https://github.com/BerriAI/litellm/blob/main/model_prices_and_context_window.json
retrieved: "2026-10-14"
---

# Muse Glimmer 30B

## Overview
Muse Glimmer is the open-weight member of Meta's Muse family, released in August 2026 under Apache 2.0. It is a dense causal transformer of about 29.6B parameters, including a roughly 1.8B-parameter perception encoder. It takes interleaved text and images, returns text, and has a 131,072-token context window. Meta's model card gives a knowledge cutoff of January 4, 2026 and says it runs locally without cloud infrastructure or network access.

## Strengths
- Trained for agent work: tool calls with precise schemas, multi-step reasoning, and recovery when a tool call fails. Reasoning effort is controllable.
- Local deployment: Meta's 4-bit quantizations bring the language model under 20 GB, targeting 24 GB or 32 GB of VRAM, with 1.0% and 0.2% measured degradation. Full precision targets 64 GB.
- Ships a DFlash speculative-decoding drafter for faster generation.
- Artificial Analysis (Muse Glimmer, High variant): Intelligence Index 17.5, coding index 49, GPQA Diamond 83.5%, long-context reasoning 83.3%, 124.2 tokens per second, 0.99 s to first token.
- Trained on data from more than 100 languages.

## Limitations
- Smaller context (131,072 tokens) than the hosted Muse models, and OpenRouter caps output at 16,384 tokens.
- Scores -32.9 on Artificial Analysis' Omniscience index, so check factual answers.
- Low on hard terminal work: 0.5% on Terminal-Bench 4 and an agentic index of 8.5.
- No audio or video input.

## Good for
- Offline or air-gapped agents on a single workstation GPU.
- Reading screenshots, charts and documents alongside conversation.
- Tool-calling assistants in scaffolds such as Hermes Agent.
