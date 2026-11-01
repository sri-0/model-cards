---
id: openai/gpt-5.6-cyber
name: GPT-5.6 Cyber
owned_by: openai
type: llm
description: GPT-5.6 Cyber is OpenAI's approval-only, purpose-trained cybersecurity model for authorised vulnerability research, exploit validation and security testing, offered through the Daybreak Red tier since August 2026.
aliases: [gpt-5.6-cyber, gpt-daybreak-red-latest, openai.gpt-5.6-cyber, bedrock_mantle/openai.gpt-5.6-cyber]
context_length: 400000
max_output_tokens: 128000
capabilities: [tool_calling, reasoning, vision, structured_output]
architecture:
  input_modalities: [text, image]
  output_modalities: [text]
open_weights: false
license: proprietary
release_date: "2026-08-07"
knowledge_cutoff: "2026-02"
sources:
  - https://developers.openai.com/api/docs/models/gpt-5.6-cyber
  - https://developers.openai.com/api/docs/models/gpt-daybreak-red-latest
  - https://developers.openai.com/api/docs/models/all
  - https://developers.openai.com/api/docs/changelog
  - https://developers.openai.com/api/docs/pricing
  - https://docs.aws.amazon.com/bedrock/latest/userguide/model-card-openai-gpt-56-cyber.html
  - https://openrouter.ai/api/v1/models
  - https://raw.githubusercontent.com/BerriAI/litellm/main/model_prices_and_context_window.json
retrieved: "2026-11-01"
---

# GPT-5.6 Cyber

## Overview
GPT-5.6 Cyber is the model OpenAI's catalogue lists under OpenAI Daybreak as its most advanced cybersecurity model. The page calls `gpt-5.6-cyber` an alias for OpenAI's most advanced purpose-trained cyber models, for approved defenders doing authorised vulnerability research, exploit validation and security testing. It needs separate approval and provisioning through the Daybreak programme. OpenRouter does not list it; the id is OpenAI's API id. The changelog introduced it on 7 August 2026 with two access tiers: Daybreak Blue (general models such as GPT-5.6 Sol) and Daybreak Red (purpose-trained models such as this one). The `gpt-daybreak-red-latest` alias, which pointed here, is now deprecated. On the Responses API it takes text and images, returns text, and has a 400,000-token context window (272,000 input), 128,000 output tokens, reasoning tokens and a 16 February 2026 knowledge cutoff. Tools include web search, file search, code interpreter, hosted shell, apply patch, skills, computer use, MCP and tool search. Amazon Bedrock serves it as `openai.gpt-5.6-cyber` with a 1,050,000-token context window, for customers enrolled in Trusted Access for Cyber.

## Strengths
- OpenAI's top cyber model, cleared for exploit reproduction, penetration testing and red teaming.
- Full agent tool set, including computer use and hosted shell.

## Limitations
- Approval-only; standard API keys cannot call it.
- 12.50 USD input, 1.25 cached input and 75 USD output per million tokens; prompts over 272,000 tokens cost 2x input and 1.5x output, and cache writes 1.25x input. Bedrock in-region prices are 10% higher.
- An alias, so the underlying model can change.
- No Artificial Analysis results.

## Good for
- Authorised offensive-security testing and vulnerability validation by approved teams.
