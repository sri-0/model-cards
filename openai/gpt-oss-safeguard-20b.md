---
id: openai/gpt-oss-safeguard-20b
name: gpt-oss-safeguard-20b
owned_by: openai
type: llm
description: gpt-oss-safeguard-20b is OpenAI's open-weight (Apache-2.0) 21B-parameter safety reasoning model, fine-tuned from gpt-oss-20b to classify content against a policy supplied in the prompt.
aliases: [openai/gpt-oss-safeguard-20b, "gpt-oss-safeguard:20b", openai.gpt-oss-safeguard-20b, groq/openai/gpt-oss-safeguard-20b, fireworks_ai/accounts/fireworks/models/gpt-oss-safeguard-20b]
context_length: 131072
max_output_tokens: 65536
capabilities: [tool_calling, reasoning, structured_output]
supported_parameters: [include_reasoning, max_tokens, reasoning, response_format, seed, stop, structured_outputs, temperature, tool_choice, tools, top_p]
architecture:
  input_modalities: [text]
  output_modalities: [text]
  tokenizer: GPT
open_weights: true
license: Apache-2.0
release_date: "2025-10-29"
pricing:
  input: 0.075
  output: 0.3
  cache_read: 0.0375
sources:
  - https://openrouter.ai/openai/gpt-oss-safeguard-20b
  - https://openrouter.ai/api/v1/models
  - https://huggingface.co/openai/gpt-oss-safeguard-20b
  - https://huggingface.co/api/models/openai/gpt-oss-safeguard-20b
  - https://openai.com/index/introducing-gpt-oss-safeguard/
  - https://openai.com/index/gpt-oss-safeguard-technical-report/
  - https://cookbook.openai.com/articles/gpt-oss-safeguard-guide
  - https://github.com/openai/gpt-oss-safeguard
  - https://github.com/roostorg/open-models
  - https://ollama.com/library/gpt-oss-safeguard
  - https://raw.githubusercontent.com/BerriAI/litellm/main/model_prices_and_context_window.json
retrieved: "2026-10-16"
---

# gpt-oss-safeguard-20b

## Overview
gpt-oss-safeguard-20b was released on 2025-10-29 as a research preview, with gpt-oss-safeguard-120b, under Apache 2.0 and OpenAI's gpt-oss usage policy. It is a fine-tune of gpt-oss-20b (21B total, 3.6B active parameters, 131,072-token context) trained to reason from a written policy supplied at inference time and label content under it. It takes the policy as the system message and the content as the user message, and answers in the harmony format: a reasoning channel, then the label the policy asks for (0/1 or JSON with a category and rationale). It is an open-weight version of OpenAI's internal Safety Reasoner. OpenAI developed the release with ROOST, which launched its Model Community for open safety models the same day. It fits a 16 GB GPU; the Ollama tag is gpt-oss-safeguard:20b.

## Strengths
- Bring-your-own-policy classification: changing a policy means editing the prompt, not retraining.
- OpenAI reports both safeguard models beat gpt-5-thinking and base gpt-oss on its internal multi-policy accuracy test and slightly on its 2022 moderation dataset.
- Full chain of thought and low, medium or high reasoning effort for auditing decisions.
- Cheap on OpenRouter: $0.075 per million input and $0.30 per million output tokens.

## Limitations
- Classifiers trained on tens of thousands of labelled examples can still beat it; on ToxicChat gpt-5-thinking and Safety Reasoner scored marginally higher.
- Slower and more compute-hungry than a conventional classifier; OpenAI pre-filters with small high-recall classifiers.
- Not meant as an end-user chat model; OpenAI points those uses to gpt-oss.
- No Artificial Analysis results; harmony format required.

## Good for
- Trust-and-safety pipelines with evolving or nuanced policies and few labelled samples.
- LLM input and output filtering and offline content labelling.
- Policy iteration where explainable labels matter more than latency.
