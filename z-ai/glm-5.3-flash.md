---
id: z-ai/glm-5.3-flash
name: GLM 5.3 Flash
owned_by: z-ai
type: llm
description: GLM-5.3-Flash is Z.ai's open-weight multimodal reasoning model (320B total, 18B active parameters) with text, image and video input and a 1M-token context window.
aliases: [glm-5.3-flash, zai/glm-5.3-flash, zai-org/GLM-5.3-Flash, zai-org/GLM-5.3-Flash-BF16]
context_length: 1048576
max_output_tokens: 943718
capabilities: [tool_calling, reasoning, vision, structured_output]
supported_parameters: [frequency_penalty, include_reasoning, logit_bias, logprobs, max_tokens, min_p, parallel_tool_calls, presence_penalty, reasoning, reasoning_effort, repetition_penalty, response_format, seed, stop, structured_outputs, temperature, tool_choice, tools, top_k, top_logprobs, top_p]
architecture:
  input_modalities: [text, image, video]
  output_modalities: [text]
  tokenizer: Other
open_weights: true
license: MIT
release_date: "2026-08-26"
pricing:
  input: 0.0261
  output: 0.9
  cache_read: 0.0108
benchmarks:
  intelligence_index: 41.8
  coding_index: 71.5
  agentic_index: 50.9
  omniscience_index: 7.5
  humanitys_last_exam: 39.9
  gpqa_diamond: 91.2
  scicode: 51.6
  terminal_bench_4: 32.8
  long_context_reasoning: 80
  output_tokens_per_second: 66.7
  time_to_first_token_seconds: 2.86
benchmark_variant: GLM-5.3-Flash
sources:
  - https://openrouter.ai/z-ai/glm-5.3-flash
  - https://openrouter.ai/api/v1/models
  - https://artificialanalysis.ai/models/glm-5-3-flash
  - https://docs.z.ai/guides/vlm/glm-5.3-flash
  - https://huggingface.co/zai-org/GLM-5.3-Flash
  - https://github.com/BerriAI/litellm/blob/main/model_prices_and_context_window.json
retrieved: "2026-10-14"
---

# GLM 5.3 Flash

## Overview
GLM-5.3-Flash was released in August 2026. Z.ai calls it the first native multimodal model in the GLM-5 series. It uses a hybrid of sparse and linear attention, which Z.ai says reduces attention computation and KV cache by 3.01x and 4.44x compared with GLM-5.3. Inputs are text, images, video and files; output is text. Z.ai documents a 1M-token context window and 128K max output. Thinking is always enabled. Weights are on Hugging Face as `zai-org/GLM-5.3-Flash` under the MIT licence.

## Strengths
- Artificial Analysis rates GLM-5.3-Flash among the leading models on its Intelligence Index (score 42, against a median of 18 for comparable open-weight models) and well priced.
- Vision is built into the coding loop: Z.ai describes UI reproduction from screenshots and browser or GUI operation.
- Tool calling, structured output and context caching on the Z.ai API.
- Short time to first token (about 2.9 seconds per Artificial Analysis).

## Limitations
- Artificial Analysis measured it as slower than average (about 67 tokens per second) and very verbose.
- Reasoning cannot be turned off.
- Self-hosting still requires serving 320B parameters.

## Good for
- Frontend and visual coding from screenshots or recordings.
- Long-horizon agent tasks with mixed text and image input.
- Office deliverables, document processing and research workflows.
- Cost-sensitive deployments that need a capable open-weight multimodal model.
