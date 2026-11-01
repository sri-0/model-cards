---
id: meta/muse-spark-1.2
name: Muse Spark 1.2
owned_by: meta
type: llm
description: Muse Spark 1.2 is Meta's proprietary multimodal reasoning model from August 2026, tuned for coding workflows with more reliable tool calling and a 1M-token context.
aliases: [muse-spark-1.2]
context_length: 1048576
max_output_tokens: 943718
capabilities: [tool_calling, reasoning, vision, structured_output]
supported_parameters: [include_reasoning, max_tokens, reasoning, reasoning_effort, repetition_penalty, response_format, structured_outputs, temperature, tool_choice, tools, top_k, top_p]
architecture:
  input_modalities: [text, image, video, file]
  output_modalities: [text]
  tokenizer: Other
open_weights: false
license: proprietary
release_date: "2026-08-05"
pricing:
  input: 1.25
  output: 4.25
  cache_read: 0.15
benchmarks:
  coding_index: 72.2
  agentic_index: 43.2
  gpqa_diamond: 90.4
  humanitys_last_exam: 45.5
  long_context_reasoning: 79.0
  output_tokens_per_second: 263.9
  scicode: 57.4
  terminal_bench_4: 7.1
  time_to_first_token_seconds: 11.3
benchmark_variant: Muse Spark 1.2 (Xhigh)
sources:
  - https://openrouter.ai/meta/muse-spark-1.2
  - https://openrouter.ai/api/v1/models
  - https://artificialanalysis.ai/models/muse-spark-1-2
  - https://dev.meta.ai/models/muse-spark-1-2
  - https://dev.meta.ai/models/muse-spark
  - https://dev.meta.ai/models/muse-spark-open
  - https://dev.meta.ai/docs/models
  - https://dev.meta.ai/docs/pricing-rate-limits
  - https://dev.meta.ai/docs/reasoning
  - https://github.com/BerriAI/litellm/blob/main/model_prices_and_context_window.json
retrieved: "2026-11-01"
---

# Muse Spark 1.2

## Overview
Muse Spark 1.2 (API id `muse-spark-1.2`) is the second Muse Spark version on Meta Model API, released on August 5, 2026 per Artificial Analysis. Meta describes it as optimised for real coding workflows, with higher first-attempt accuracy and more reliable tool calling; its docs now call it "the previous version". Meta says the open-weight Muse Spark Open is derived from the Muse Spark model it released in August. Reasoning is always on, with effort from minimal to xhigh; "max" is not available. Meta lists text, image, video, audio and PDF input, while OpenRouter lists text, images, video and files. The context is 1,048,576 tokens, with up to 943,718 output tokens on OpenRouter. Lifecycle: Meta still serves it on pay-as-you-go and in Muse Code, but recommends Muse Spark 1.3 for new work, and Artificial Analysis marks 1.2 deprecated in favour of 1.3.

## Strengths
- Meta's figures for 1.2 at xhigh, from the Muse Spark 1.3 page: 82.9 Terminal-Bench 2.1, 55.0 DeepSWE v1.1, 85.9 DeepSearchQA and 1615 on GDPval-AA v2.
- Meta recommends 1.2 for audio input, because audio is not fully supported on 1.3.
- Artificial Analysis (Muse Spark 1.2, Xhigh): 90.4% on GPQA Diamond, 79% on long-context reasoning, a coding index of 72.2 and an agentic index of 43.2, at 263.9 tokens per second and 11.3 s to first token.
- A Contributor variant (`meta/muse-spark-1.2-contributor`) costs $0.10 input and $0.20 output per million tokens.

## Limitations
- Behind 1.3 on Meta's own long-context and workflow tests: 55.5 against 98.1 on MRCR 512K-1M, and 38.2 against 49.6 on AutomationBench.
- 7.1% on Terminal-Bench 4.0.
- Proprietary and API-only, so it cannot run in a network-isolated deployment.

## Good for
- Agent and coding workloads that include audio.
- Existing integrations pinned to `muse-spark-1.2`.
- Cost-sensitive sub-agent tasks and tight tool loops, Meta's suggested use for Muse Spark.
