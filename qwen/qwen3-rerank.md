---
id: qwen/qwen3-rerank
name: Qwen3 Rerank
owned_by: qwen
type: reranker
description: Alibaba Cloud Model Studio's text reranking API model for semantic search and RAG, scoring up to 500 documents per request in 100+ languages with optional English task instructions.
aliases: [qwen3-rerank]
architecture:
  input_modalities: [text]
  output_modalities: [rerank]
open_weights: false
license: proprietary
sources:
  - https://www.alibabacloud.com/help/en/model-studio/rerank
  - https://www.alibabacloud.com/help/en/model-studio/text-rerank-api
  - https://www.alibabacloud.com/help/en/model-studio/model-pricing
  - https://github.com/QwenLM/Qwen3-Embedding/blob/main/evaluation/task_prompts.json
  - https://openrouter.ai/api/v1/models?output_modalities=all
retrieved: "2026-11-01"
---

# Qwen3 Rerank

## Overview
qwen3-rerank is the text reranking model in Alibaba Cloud Model Studio (DashScope), offered in the Singapore region at $0.1 per million input tokens with a 1 million-token free quota; output is free. Alibaba retired gte-rerank on 2026-05-30 and names qwen3-rerank as its replacement. OpenRouter does not list it; the id is the Model Studio API id, and Alibaba does not say whether it is the same model as the open-weight Qwen3-Reranker. It takes up to 500 documents and 120,000 tokens per request (query tokens times documents plus all document tokens). Alibaba's two pages differ on the per-item limit, 32,768 tokens on the rerank guide against 4,000 on the API reference, so the card has no `context_length`; items over the limit return HTTP 400 rather than being truncated. An optional English `instruct` sets the ranking task (question answering by default, or semantic similarity), with more prompts linked from the Qwen3-Embedding repository. It is served through the DashScope API and an OpenAI-compatible `/reranks` endpoint.

## Strengths
- 100+ languages, against 50+ for gte-rerank-v2.
- Instructions switch between answer-finding and semantic-similarity ranking.
- Up to 500 documents per request.

## Limitations
- Singapore only; Beijing lists gte-rerank-v2 and the multimodal qwen3-vl-rerank instead.
- Conflicting per-item token limits in Alibaba's documentation.
- No published benchmark scores or release date; proprietary.

## Good for
- Reranking for RAG on Alibaba Cloud Model Studio.
- FAQ matching with the semantic-similarity instruction.
- Migrations from the retired gte-rerank.
