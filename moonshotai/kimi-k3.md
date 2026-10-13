---
id: moonshotai/kimi-k3
name: Kimi K3
owned_by: moonshotai
type: llm
description: Kimi K3 is Moonshot AI's 2.8T-parameter open-weight mixture-of-experts reasoning model for coding, knowledge work and agentic tasks, with text, image and video input.
aliases: [kimi-k3, moonshot/kimi-k3, moonshotai/Kimi-K3]
context_length: 1048576
max_output_tokens: 943718
capabilities: [tool_calling, reasoning, vision, structured_output]
supported_parameters: [frequency_penalty, include_reasoning, logit_bias, logprobs, max_tokens, min_p, presence_penalty, reasoning, reasoning_effort, repetition_penalty, response_format, seed, stop, structured_outputs, temperature, tool_choice, tools, top_k, top_logprobs, top_p]
architecture:
  input_modalities: [text, image, video]
  output_modalities: [text]
  tokenizer: Other
open_weights: true
license: Kimi K3 License
release_date: "2026-07-16"
pricing:
  input: 0.73
  output: 10
  cache_read: 0.55
benchmarks:
  intelligence_index: 43.6
  coding_index: 76.2
  agentic_index: 50
  omniscience_index: 19.7
  humanitys_last_exam: 46.9
  gpqa_diamond: 93.5
  scicode: 59.5
  terminal_bench_4: 12.6
  long_context_reasoning: 88.7
  mmmu_pro: 80.5
  output_tokens_per_second: 43.7
  time_to_first_token_seconds: 3.18
benchmark_variant: Kimi K3 (Max)
sources:
  - https://openrouter.ai/moonshotai/kimi-k3
  - https://openrouter.ai/api/v1/models
  - https://artificialanalysis.ai/models/kimi-k3
  - https://huggingface.co/moonshotai/Kimi-K3
  - https://github.com/BerriAI/litellm/blob/main/model_prices_and_context_window.json
retrieved: "2026-10-14"
---

# Kimi K3

## Overview
Kimi K3 is Moonshot AI's open-weight multimodal reasoning model, released in July 2026. The Hugging Face card (moonshotai/Kimi-K3) describes a mixture-of-experts model with 2.8T total and 104B activated parameters (16 of 896 experts per token), built on Kimi Delta Attention and Attention Residuals. It has a 1M-token context window. Weights ship as MXFP4 weights with MXFP8 activations from quantization-aware training, under the Kimi K3 License.

## Strengths
- Highest score among the Kimi cards in this set: Artificial Analysis Intelligence Index 43.6, Coding Index 76.2 and Agentic Index 50 (measured on Kimi K3 (Max)).
- Strong knowledge and long-context results on the same variant: GPQA Diamond 93.5% and AA-LCR 88.7%.
- Moonshot targets long engineering sessions: navigating large repositories, orchestrating terminal tools, debugging and iterating against images, logs, tests and runtime feedback.
- Native vision. OpenRouter lists text, image and video input.

## Limitations
- Slow. Artificial Analysis measured 43.7 output tokens per second and 3.18 s to first token on Kimi K3 (Max), and rates it somewhat verbose.
- Artificial Analysis rates it particularly expensive compared with open-weight models of similar size.
- At 2.8T total parameters the weights are very large to self-host.
- The Kimi K3 License is a custom licence, not a standard open-source one. Check its terms before deployment.
- Terminal-Bench 4.0 score is low (12.6% on Kimi K3 (Max)).

## Good for
- Long-horizon agentic coding over large codebases where quality matters more than latency.
- Research and analysis over very long inputs, up to 1M tokens.
- Work that mixes code with screenshots, diagrams or video.
- Teams that need the strongest open-weight Kimi model and can host it.
