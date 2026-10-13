---
id: mistralai/devstral-2512
name: Devstral 2 2512
owned_by: mistralai
type: llm
description: Devstral 2 is a 123B dense open-weight coding model from Mistral AI built for software engineering agents.
aliases: [devstral-2512, mistralai/Devstral-2-123B-Instruct-2512]
context_length: 262144
max_output_tokens: 209715
capabilities: [tool_calling, structured_output]
supported_parameters: [frequency_penalty, max_tokens, presence_penalty, response_format, seed, stop, structured_outputs, temperature, tool_choice, tools, top_p]
architecture:
  input_modalities: [text, file]
  output_modalities: [text]
  tokenizer: Mistral
open_weights: true
license: Modified MIT
release_date: "2025-12-09"
pricing:
  input: 0.4
  output: 2
  cache_read: 0.04
benchmarks:
  intelligence_index: 8.6
  coding_index: 31.3
  agentic_index: 2.3
  omniscience_index: -46.7
  humanitys_last_exam: 3.6
  gpqa_diamond: 59.4
  scicode: 32.8
  terminal_bench_hard: 18.9
  terminal_bench_4: 0
  long_context_reasoning: 32.3
  ifbench: 38.1
  tau2_bench: 24.9
benchmark_variant: Devstral 2
sources:
  - https://openrouter.ai/mistralai/devstral-2512
  - https://openrouter.ai/api/v1/models
  - https://artificialanalysis.ai/models/devstral-2
  - https://docs.mistral.ai/getting-started/models
  - https://huggingface.co/mistralai/Devstral-2-123B-Instruct-2512
retrieved: "2026-10-14"
---

# Devstral 2 2512

## Overview
Devstral 2 (API id devstral-2512) was released in December 2025. It is a dense model of about 123B parameters with a 256K-token context window and text input. Weights are on Hugging Face (mistralai/Devstral-2-123B-Instruct-2512, FP8) under a modified MIT licence. Mistral's models page lists it as retired from Mistral's API: deprecated on 5/22/2026 and retired on 7/31/2026, with Mistral Medium 3.5 as the suggested replacement. Mistral Medium 3.5 also replaced it in the Vibe coding agent. The weights remain available and OpenRouter still lists the model.

## Strengths
- Built to explore codebases, edit multiple files and drive coding agents.
- Mistral reports 72.2% on SWE-bench Verified, 61.3% on SWE-bench Multilingual and 32.6% on Terminal Bench 2.
- Works with Mistral Vibe, Cline, Kilo Code, Claude Code, OpenHands and SWE Agent scaffolds.
- Artificial Analysis Coding Index 31.3 (variant: Devstral 2), and very concise output.

## Limitations
- No longer served on Mistral's own API.
- Text input only, and no reasoning mode.
- Artificial Analysis Intelligence Index is 8.6 and Agentic Index 2.3. No speed figures were published.
- The dense 123B size needs substantial GPU memory to self-host.

## Good for
- Existing self-hosted coding-agent setups built on Devstral 2.
- Multi-file code changes, bug fixing and legacy code modernisation.
- Fine-tuning for specific languages or large internal codebases.
