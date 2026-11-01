---
id: mistralai/mistral-large-2407
name: Mistral Large 2407
owned_by: mistralai
type: llm
description: Mistral Large 2 (mistral-large-2407) is a dense 123B model from Mistral AI with a 128K context window, released in July 2024 under the Mistral Research License and retired from Mistral's API in March 2025.
aliases: [mistral-large-2407, mistralai/Mistral-Large-Instruct-2407, "mistral.mistral-large-2407-v1:0", "mistral-large@2407", azure_ai/mistral-large-2407]
context_length: 131072
max_output_tokens: 104857
capabilities: [tool_calling, structured_output]
supported_parameters: [frequency_penalty, max_tokens, presence_penalty, response_format, seed, stop, structured_outputs, temperature, tool_choice, tools, top_p]
architecture:
  input_modalities: [text, file]
  output_modalities: [text]
  tokenizer: Mistral
open_weights: true
license: Mistral Research License
release_date: "2024-07-24"
knowledge_cutoff: "2024-03"
pricing:
  input: 2
  output: 6
  cache_read: 0.2
benchmarks:
  gpqa_diamond: 47.2
  humanitys_last_exam: 2.9
  ifbench: 31.6
  long_context_reasoning: 2.0
  tau2_bench: 33.0
benchmark_variant: "Mistral Large 2 (Jul '24)"
sources:
  - https://openrouter.ai/mistralai/mistral-large-2407
  - https://openrouter.ai/api/v1/models
  - https://openrouter.ai/api/v1/models/mistralai/mistral-large-2407/endpoints
  - https://artificialanalysis.ai/models/mistral-large-2407
  - https://docs.mistral.ai/getting-started/models
  - https://docs.mistral.ai/models/mistral-large-2-0-24-07
  - https://docs.mistral.ai/getting-started/changelog
  - https://mistral.ai/news/mistral-large-2407
  - https://huggingface.co/mistralai/Mistral-Large-Instruct-2407
  - https://huggingface.co/api/models/mistralai/Mistral-Large-Instruct-2407
  - https://github.com/BerriAI/litellm/blob/main/model_prices_and_context_window.json
retrieved: "2026-11-01"
---

# Mistral Large 2407

## Overview
Mistral Large 2 (API id mistral-large-2407, version 24.07) was released on 2024-07-24. It is a dense 123B model with a 128K context window, trained on dozens of languages including French, German, Spanish, Italian, Portuguese, Arabic, Hindi, Russian, Chinese, Japanese and Korean, and on 80+ programming languages. Mistral reports 84.0% on MMLU for the pretrained version and says training focused on reducing hallucinations and on acknowledging when the model lacks information. Weights are on Hugging Face (mistralai/Mistral-Large-Instruct-2407, gated behind acceptance of the Mistral Research License); commercial self-deployment needs a licence from Mistral. Mistral's docs give about 297 GB of GPU memory at bf16 and about 75 GB at fp4. They list it as deprecated on 2024-11-30 and retired on 2025-03-30, with Mistral Large 3 as the replacement, itself deprecated on 2026-10-31 in favour of Mistral Large 4. OpenRouter added this pinned listing on 2024-11-19 (UTC), the day after Mistral Large 2.1 (2411) was released, and still listed it with Mistral as the only provider at retrieval.

## Strengths
- Artificial Analysis (Mistral Large 2 (Jul '24)): 47.2% on GPQA Diamond, 33.0% on tau2-bench and 31.6% on IFBench.
- Native function calling and JSON output.
- Mistral says the 123B size allows large throughput on a single node.

## Limitations
- Retired from Mistral's API. OpenRouter's $2 input and $6 output per million tokens is high for its results.
- Long-context reasoning is weak: 2.0% on AA-LCR.
- No image input and no reasoning mode. Knowledge cutoff of March 2024 per OpenRouter.
- Research licence and a large memory footprint.

## Good for
- Deployments pinned to the 2407 weights that cannot yet move to a current Mistral model.
- Multilingual chat and code generation under a research licence.
- Comparing against Mistral Large 2.1 (2411), which improved long context and function calling.
