---
id: z-ai/autoglm-phone-9b
name: AutoGLM-Phone-9B
owned_by: z-ai
type: llm
description: AutoGLM-Phone-9B is Z.ai's open-weight (MIT) 9B vision-language model for operating Chinese smartphone apps from natural-language instructions, used by the Open-AutoGLM Phone Agent framework.
aliases: [zai-org/AutoGLM-Phone-9B]
context_length: 65536
capabilities: [vision]
architecture:
  input_modalities: [text, image]
  output_modalities: [text]
open_weights: true
license: MIT
release_date: "2025-12-08"
sources:
  - https://huggingface.co/zai-org/AutoGLM-Phone-9B
  - https://huggingface.co/api/models/zai-org/AutoGLM-Phone-9B
  - https://huggingface.co/zai-org/AutoGLM-Phone-9B/raw/main/config.json
  - https://github.com/zai-org/Open-AutoGLM
  - https://docs.bigmodel.cn/cn/guide/models/vlm/autoglm-phone
  - https://docs.bigmodel.cn/cn/update/new-releases
  - https://openrouter.ai/api/v1/models
retrieved: "2026-11-01"
---

# AutoGLM-Phone-9B

## Overview
AutoGLM-Phone-9B is the model behind Open-AutoGLM's Phone Agent; its Hugging Face repository was created on 2025-12-08, and Zhipu launched the AutoGLM-Phone framework on 2025-12-11. It is fine-tuned from GLM-4.1V-9B-Base and shares the GLM-4.1V-9B-Thinking architecture (65,536 positions in config.json). The agent reads screenshots, plans the next step and acts through ADB on Android, HDC on HarmonyOS or WebDriverAgent on iPhone: launching apps, tapping, typing, swiping, long-pressing and going back. Z.ai says this checkpoint is optimised for Chinese apps; the Multilingual variant covers English. Zhipu's bigmodel.cn API also offers an `autoglm-phone` model (20K context, 2,048 output tokens, Chinese, Android), without saying which checkpoint it runs. OpenRouter does not list it; the id follows the Hugging Face repo. Weights are MIT-licensed.

## Strengths
- Zhipu says the framework is adapted to more than 50 mainstream Chinese apps for shopping, travel, food delivery, media and news.
- Built-in confirmation for sensitive actions and human takeover for logins and captchas.
- Remote ADB over Wi-Fi, and integration with Midscene.js for scripted Android and iOS automation.
- Deploys like GLM-4.1V-9B-Thinking; Z.ai points to its GLM-V repository for serving.

## Limitations
- Z.ai restricts the project to research and education and prohibits illegal data access or system interference.
- Optimised for Chinese apps; English apps need AutoGLM-Phone-9B-Multilingual.
- Z.ai publishes no benchmark scores on the model card.

## Good for
- Research on mobile GUI agents and phone automation.
- Automating tasks across Chinese Android apps from natural-language commands.
