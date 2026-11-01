---
id: meta/muse-spark-1.1
name: Muse Spark 1.1
owned_by: meta
type: llm
description: Muse Spark 1.1 is the first version of Meta's proprietary Muse Spark multimodal reasoning model offered on Meta Model API, launched in public preview in July 2026 for agentic and coding work.
aliases: [muse-spark-1.1]
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
release_date: "2026-07-08"
pricing:
  input: 1.25
  output: 4.25
  cache_read: 0.15
benchmarks:
  coding_index: 71.3
  agentic_index: 25.8
  gpqa_diamond: 89.8
  humanitys_last_exam: 46.2
  long_context_reasoning: 77.7
  output_tokens_per_second: 302.0
  scicode: 58.8
  terminal_bench_4: 6.1
  time_to_first_token_seconds: 12.3
benchmark_variant: Muse Spark 1.1 (Xhigh)
sources:
  - https://openrouter.ai/meta/muse-spark-1.1
  - https://openrouter.ai/api/v1/models
  - https://artificialanalysis.ai/models/muse-spark-1-1
  - https://dev.meta.ai/models/muse-spark-1-1
  - https://dev.meta.ai/docs/models
  - https://dev.meta.ai/docs/pricing-rate-limits
  - https://dev.meta.ai/docs/reasoning
  - https://dev.meta.ai/resources/blog/build-with-muse-spark
  - https://github.com/BerriAI/litellm/blob/main/model_prices_and_context_window.json
retrieved: "2026-11-01"
---

# Muse Spark 1.1

## Overview
Muse Spark 1.1 (API id `muse-spark-1.1`) is the first Muse Spark version Meta opened to developers. Meta's blog of July 8, 2026 announced it in public preview on Meta Model API for US developers, after Muse Spark was introduced in April; Artificial Analysis dates the release July 9. Meta's docs now call it "the original version" of the three Muse Spark versions. Reasoning is always on, with effort from minimal to xhigh (OpenRouter default medium; "none" returns HTTP 400). Meta lists text, image, video, audio and PDF input; OpenRouter lists text, images, video and files. The context is 1,048,576 tokens, with up to 943,718 output tokens on OpenRouter. Lifecycle: Meta still serves it on pay-as-you-go in Standard mode only, with no Contributor tier and no Muse Code access, recommends Muse Spark 1.3 for new work, and Artificial Analysis marks 1.1 deprecated in favour of 1.2.

## Strengths
- Meta's results: 88.1 MCP Atlas, 80.8 OSWorld-Verified, 80.0 Terminal-Bench 2.1, 61.5 SWE-Bench Pro and 62.1 Humanity's Last Exam with tools.
- Artificial Analysis (Muse Spark 1.1, Xhigh): 89.8% on GPQA Diamond, 46.2% on Humanity's Last Exam, 77.7% on long-context reasoning and a coding index of 71.3.
- Fast: 302 output tokens per second and 12.3 s to first token at Xhigh.
- $1.25 input, $4.25 output and $0.15 cached input per million tokens, with no long-context premium; web search grounding adds $2.50 per 1,000 queries.

## Limitations
- Superseded: an agentic index of 25.8 against 43.2 for Muse Spark 1.2, and 6.1% on Terminal-Bench 4.0.
- Proprietary and API-only, so it cannot run in a network-isolated deployment.
- No discounted Contributor mode and not available in Muse Code.

## Good for
- Existing integrations pinned to `muse-spark-1.1`.
- High-throughput sub-agent tasks where speed matters more than peak capability.
- Comparing behaviour across Muse Spark versions.
