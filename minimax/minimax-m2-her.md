---
id: minimax/minimax-m2-her
name: MiniMax M2-her
owned_by: minimax
type: llm
description: MiniMax M2-her is MiniMax's text-only dialogue model for role-play and multi-turn character chat, served through its API as M2-her with a 64K context, 2,048-token replies and persona and sample-message roles.
aliases: [minimax-m2-her, M2-her, minimax/minimax-m2-her-20260123]
context_length: 65536
max_output_tokens: 2048
capabilities: []
supported_parameters: [max_tokens, temperature, top_p]
architecture:
  input_modalities: [text]
  output_modalities: [text]
  tokenizer: Other
pricing:
  input: 0.3
  output: 1.2
  cache_read: 0.03
sources:
  - https://openrouter.ai/minimax/minimax-m2-her
  - https://openrouter.ai/api/v1/models
  - https://platform.minimax.io/docs/guides/text-chat.md
  - https://platform.minimax.io/docs/guides/text-generation.md
  - https://platform.minimax.io/docs/faq/models.md
  - https://platform.minimax.io/docs/release-notes/models.md
retrieved: "2026-11-01"
---

# MiniMax M2-her

## Overview
MiniMax M2-her is MiniMax's dialogue model for role-play and multi-turn character chat; OpenRouter describes it as dialogue-first, built to stay consistent in tone and personality. MiniMax's chat-model guide fixes the API id as `M2-her`, gives a 64K context window and `max_completion_tokens` of up to 2,048, and adds roles beyond system, user and assistant: `user_system` for the user's persona, `group` for a scene or conversation name, and `sample_message_user` and `sample_message_ai` for example turns, which count toward input tokens (MiniMax recommends one to three short examples). OpenRouter lists it as minimax/minimax-m2-her (canonical slug minimax-m2-her-20260123) with 65,536 context, 2,048 output tokens, and $0.30 input, $1.20 output and $0.03 cache read per million tokens. MiniMax's release notes do not date it, so the card has no release date. No weights are published and Artificial Analysis has no page for it, so there are no benchmarks. MiniMax's model list now marks M2-her as retired on its own API.

## Strengths
- Persona, group and sample-message roles make character setup explicit rather than prompt-engineered.
- Built for consistent tone and personality across multi-turn conversations.
- Cheap on OpenRouter, with cache-read pricing.

## Limitations
- Text only: MiniMax's guide says it does not accept mixed text and image input.
- No tool calling, reasoning or structured output on OpenRouter; only max_tokens, temperature and top_p are supported.
- Replies are capped at 2,048 tokens and the window is 64K.
- MiniMax publishes no benchmarks or model details for it.
- Retired on MiniMax's own API, with no stated end date on OpenRouter.

## Good for
- Companion, role-play and interactive-fiction chat.
- Character-driven dialogue for games and story apps.
