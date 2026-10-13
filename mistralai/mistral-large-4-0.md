---
id: mistralai/mistral-large-4-0
name: Mistral Large 4
owned_by: mistralai
type: llm
description: Mistral Large 4 is Mistral AI's large multimodal model for reasoning, coding and agentic work, released in October 2026 and listed by Artificial Analysis as a preview.
aliases: [mistral-large-4-0, mistral/mistral-large-4-0]
context_length: 1048576
max_output_tokens: 262144
capabilities: [tool_calling, reasoning, vision, structured_output]
supported_parameters: [frequency_penalty, include_reasoning, logprobs, max_tokens, presence_penalty, reasoning, reasoning_effort, response_format, seed, stop, structured_outputs, temperature, tool_choice, tools, top_logprobs, top_p]
architecture:
  input_modalities: [text, image]
  output_modalities: [text]
  tokenizer: Mistral
release_date: "2026-10-06"
pricing:
  input: 0.68
  output: 2.09
  cache_read: 0.07
benchmarks:
  intelligence_index: 38.4
  omniscience_index: -5.3
  humanitys_last_exam: 35
  scicode: 54.2
  terminal_bench_4: 26.8
  long_context_reasoning: 81.3
  mmmu_pro: 76.4
benchmark_variant: Mistral Large 4 Preview
sources:
  - https://openrouter.ai/mistralai/mistral-large-4-0
  - https://openrouter.ai/api/v1/models
  - https://artificialanalysis.ai/models/mistral-large-4
  - https://docs.mistral.ai/getting-started/models
  - https://github.com/BerriAI/litellm/blob/main/model_prices_and_context_window.json
retrieved: "2026-10-14"
---

# Mistral Large 4

## Overview
Mistral Large 4 (API id mistral-large-4-0) accepts text and image input and returns text. OpenRouter lists a 1,048,576-token context window and up to 262,144 output tokens. Artificial Analysis lists it as "Mistral Large 4 Preview" with 1000B total and 49B active parameters and a 524K-token context window, which differs from OpenRouter's figure. Its licence status is unclear: Mistral's models page lists it as open-weight (version 26.10), while Artificial Analysis lists it without open weights and no Hugging Face repository was found at retrieval. For that reason open_weights and license are omitted from this card's frontmatter.

## Strengths
- Artificial Analysis Intelligence Index 38.4 on Mistral Large 4 Preview, well above the other Mistral models in this set.
- Artificial Analysis rates it well priced compared with models of similar price.
- Supports tool calling, structured outputs and a reasoning_effort parameter on OpenRouter.

## Limitations
- Preview status on Artificial Analysis. Behaviour and limits may change.
- Very verbose: it generated 200M tokens to run the Intelligence Index, against a median of 85M.
- Artificial Analysis had published no speed or latency figures at retrieval.
- Weights availability and licence terms were not confirmed at retrieval, so offline self-hosting cannot be assumed.

## Good for
- The strongest Mistral option for reasoning, coding and agentic tasks where it is served.
- Long-context work that needs image input.
- Evaluating against Mistral Medium 3.5 before migrating, given its preview status.
