---
id: meta-llama/llama-2-13b-chat
name: Llama 2 13B Chat
owned_by: meta
type: llm
description: Llama 2 13B Chat is Meta's July 2023 open-weight, English-only 13B dialogue model with a 4k context, long since superseded by the Llama 3 family.
aliases: [meta-llama/Llama-2-13b-chat-hf, meta-llama/Llama-2-13b-chat, "llama2:13b-chat", "llama2:13b", meta.llama2-13b-chat-v1, meta/llama-2-13b-chat]
context_length: 4096
architecture:
  input_modalities: [text]
  output_modalities: [text]
open_weights: true
license: Llama 2 Community License
release_date: "2023-07-18"
knowledge_cutoff: "2022-09"
benchmarks:
  gpqa_diamond: 32.1
  humanitys_last_exam: 4.8
benchmark_variant: Llama 2 Chat 13B
sources:
  - https://huggingface.co/meta-llama/Llama-2-13b-chat-hf
  - https://huggingface.co/api/models/meta-llama/Llama-2-13b-chat-hf
  - https://huggingface.co/api/models/meta-llama/Llama-2-13b-chat
  - https://huggingface.co/meta-llama/Meta-Llama-3-8B-Instruct
  - https://artificialanalysis.ai/models/llama-2-chat-13b
  - https://dev.meta.ai/llama/docs/model-cards-and-prompt-formats/meta-llama-2
  - https://docs.aws.amazon.com/bedrock/latest/userguide/model-lifecycle-legacy.html
  - https://ollama.com/library/llama2
  - https://github.com/BerriAI/litellm/blob/main/model_prices_and_context_window.json
  - https://openrouter.ai/api/v1/models
retrieved: "2026-11-01"
---

# Llama 2 13B Chat

## Overview
Lifecycle: superseded. Artificial Analysis marks it deprecated in favour of Llama 3 70B Instruct, and OpenRouter no longer lists it. LiteLLM still lists the Bedrock id `meta.llama2-13b-chat-v1`, but Bedrock's current lifecycle pages no longer list Llama 2. The weights remain on Hugging Face (`meta-llama/Llama-2-13b-chat-hf`, plus the original-format `meta-llama/Llama-2-13b-chat`) and in Ollama (`llama2:13b-chat`). Llama 2 Chat is the dialogue-tuned version of Meta's Llama 2 family (7B, 13B and 70B), released on July 18, 2023 per Artificial Analysis. This 13B model (13.0B parameters per Hugging Face) is a dense transformer without grouped-query attention, pretrained on 2 trillion tokens and tuned with SFT, RLHF and over a million human-annotated examples. Meta gives a 4k context, a September 2022 pretraining cutoff with some tuning data up to July 2023, and English as the only intended language. Prompts must use the `[INST]` and `<<SYS>>` format. Licence: Llama 2 Community License.

## Strengths
- Low toxicity in Meta's tests: 0.00% toxic generations on ToxiGen and 62.18% truthful and informative answers on TruthfulQA.
- Mature, widely packaged weights; Ollama's `llama2:13b` package is 7.4 GB.
- Simple, well-documented chat template.

## Limitations
- Very weak by current standards. Meta's own Llama 3 card measures it at 47.8 MMLU, 22.3 GPQA, 14.0 HumanEval, 77.4 GSM-8K and 6.7 MATH.
- Artificial Analysis (Llama 2 Chat 13B): 32.1% on GPQA Diamond and 4.8% on Humanity's Last Exam.
- 4k context, English only, no tool calling, and knowledge from 2022.

## Good for
- Legacy applications still pinned to Llama 2.
- Research baselines and reproductions of 2023 results.
- Mid-sized local deployments where an old 4k-context chat model is acceptable.
