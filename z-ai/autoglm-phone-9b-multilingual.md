---
id: z-ai/autoglm-phone-9b-multilingual
name: AutoGLM-Phone-9B-Multilingual
owned_by: z-ai
type: llm
description: AutoGLM-Phone-9B-Multilingual is Z.ai's open-weight (MIT) 9B vision-language model for operating smartphone apps in English and other languages, the multilingual counterpart of AutoGLM-Phone-9B.
aliases: [zai-org/AutoGLM-Phone-9B-Multilingual]
context_length: 65536
capabilities: [vision]
architecture:
  input_modalities: [text, image]
  output_modalities: [text]
open_weights: true
license: MIT
release_date: "2025-12-09"
sources:
  - https://huggingface.co/zai-org/AutoGLM-Phone-9B-Multilingual
  - https://huggingface.co/api/models/zai-org/AutoGLM-Phone-9B-Multilingual
  - https://huggingface.co/zai-org/AutoGLM-Phone-9B-Multilingual/raw/main/config.json
  - https://github.com/zai-org/Open-AutoGLM
  - https://docs.bigmodel.cn/cn/guide/models/vlm/autoglm-phone
  - https://openrouter.ai/api/v1/models
  - https://raw.githubusercontent.com/BerriAI/litellm/main/model_prices_and_context_window.json
retrieved: "2026-11-01"
---

# AutoGLM-Phone-9B-Multilingual

## Overview
AutoGLM-Phone-9B-Multilingual is the second checkpoint for Open-AutoGLM's Phone Agent; its Hugging Face repository was created on 2025-12-09, a day after AutoGLM-Phone-9B. Z.ai says the original model is optimised for Chinese apps, while this one supports English and suits apps with English or other non-Chinese content. Like its sibling, it is fine-tuned from GLM-4.1V-9B-Base and shares the GLM-4.1V-9B-Thinking architecture, with 65,536 positions in config.json. The agent reads phone screenshots, plans the next step and acts through ADB on Android, HDC on HarmonyOS or WebDriverAgent on iPhone. OpenRouter does not list it; the id follows the Hugging Face repo. LiteLLM's catalogue lists a hosted copy on Novita with a 65,536-token context. Weights are MIT-licensed.

## Strengths
- The only AutoGLM phone checkpoint aimed at English-language apps.
- Same agent features as the Chinese model: confirmation before sensitive actions, human takeover for logins and captchas, and remote ADB over Wi-Fi.
- Deploys like GLM-4.1V-9B-Thinking; Z.ai points to its GLM-V repository for serving.

## Limitations
- Z.ai restricts the project to research and education and prohibits illegal data access or system interference.
- The Hugging Face metadata tags the language as Chinese only, and Z.ai publishes no benchmark scores or language list.
- Zhipu's 50-plus supported-app list targets Chinese apps.

## Good for
- Research on mobile GUI agents in English.
- Automating tasks across Android and iOS apps from natural-language commands.
