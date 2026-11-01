---
id: openai/gpt-oss-safeguard-120b
name: gpt-oss-safeguard-120b
owned_by: openai
type: llm
description: gpt-oss-safeguard-120b is OpenAI's open-weight (Apache-2.0) 117B-parameter safety reasoning model, fine-tuned from gpt-oss-120b to classify content against a policy supplied in the prompt.
aliases: [openai/gpt-oss-safeguard-120b, "gpt-oss-safeguard:120b", openai.gpt-oss-safeguard-120b, fireworks_ai/accounts/fireworks/models/gpt-oss-safeguard-120b]
context_length: 131072
capabilities: [reasoning, structured_output]
architecture:
  input_modalities: [text]
  output_modalities: [text]
open_weights: true
license: Apache-2.0
release_date: "2025-10-29"
sources:
  - https://huggingface.co/openai/gpt-oss-safeguard-120b
  - https://huggingface.co/api/models/openai/gpt-oss-safeguard-120b
  - https://huggingface.co/openai/gpt-oss-safeguard-120b/raw/main/config.json
  - https://openai.com/index/introducing-gpt-oss-safeguard/
  - https://openai.com/index/gpt-oss-safeguard-technical-report/
  - https://cookbook.openai.com/articles/gpt-oss-safeguard-guide
  - https://github.com/openai/gpt-oss-safeguard
  - https://github.com/roostorg/open-models
  - https://arxiv.org/abs/2508.10925
  - https://ollama.com/library/gpt-oss-safeguard
  - https://openrouter.ai/api/v1/models
  - https://raw.githubusercontent.com/BerriAI/litellm/main/model_prices_and_context_window.json
retrieved: "2026-10-16"
---

# gpt-oss-safeguard-120b

## Overview
gpt-oss-safeguard-120b was released on 2025-10-29 as a research preview alongside gpt-oss-safeguard-20b, under Apache 2.0 and OpenAI's gpt-oss usage policy. OpenRouter does not list it (only the 20B variant); the id follows the Hugging Face repo openai/gpt-oss-safeguard-120b. It is a fine-tune of gpt-oss-120b: a 36-layer mixture-of-experts model with 117B total and 5.1B active parameters, MXFP4 expert weights that fit one 80 GB GPU, and a 131,072-token context. Given a policy in the system message and content to classify, it reasons in harmony's analysis channel, then emits the requested label (0/1, category ids or JSON with a rationale). OpenAI built it with ROOST, which launched its Model Community for open safety models the same day. They are an open-weight version of OpenAI's internal Safety Reasoner. Ollama serves it as gpt-oss-safeguard:120b.

## Strengths
- Policy-as-prompt: OpenAI reports the safeguard models beat gpt-5-thinking and base gpt-oss on internal multi-policy accuracy, and edge Safety Reasoner on its 2022 moderation dataset (not statistically significant).
- Full chain of thought and configurable reasoning effort (low, medium, high) for auditable decisions.
- Supports Structured Outputs and the Responses API per the technical report.

## Limitations
- Dedicated classifiers trained on tens of thousands of labels can still do better; on ToxicChat it trailed gpt-5-thinking and Safety Reasoner marginally.
- Time and compute intensive at scale; OpenAI gates it behind small high-recall classifiers.
- Needs an 80 GB GPU; the 20B variant is the low-latency option.
- No OpenRouter listing, so no pricing here; no Artificial Analysis results; harmony format required.

## Good for
- Platform-scale trust-and-safety labelling where policies change often.
- Reviewing content flagged by cheaper first-pass classifiers.
- Research on reasoning-based moderation with open weights.
