# model-cards

Offline reference cards for large language models, one Markdown file per model.

The cards are written for agents and servers that run without internet access.
Each card says what a model is, what it does well, where it falls short, and
the published numbers behind that: context window, output limit, pricing,
licence, release date, knowledge cutoff and independent benchmark results.

The agentlite agent server reads this directory (set `MODEL_CARDS_DIR` to a
local checkout) and uses the cards to fill in the model list its providers
report. One card covers a model everywhere it is
served: OpenRouter, the vendor's own API, a cloud platform, LiteLLM or a local
vLLM/Ollama deployment all point at the same file through its `id` and
`aliases`.

## Layout and naming

```
anthropic/claude-sonnet-4.5.md     id: anthropic/claude-sonnet-4.5
google/gemma-4-31b-it.md           id: google/gemma-4-31b-it
meta-llama/llama-3.3-70b-instruct.md
scripts/refresh_openrouter.py      refreshes the OpenRouter-derived fields
```

- The file path is the model's **OpenRouter id** plus `.md`. The `id` field in
  the frontmatter repeats it.
- A model that OpenRouter does not list gets an id in the same style: the
  lower-cased Hugging Face repository name (for example `google/gemma-4-12b-it`
  for `google/gemma-4-12B-it`). The card says so in its overview.
- Every other name a provider uses goes in `aliases`: vendor API ids and dated
  snapshots (`claude-sonnet-4-5-20250929`, `gpt-5.4-2026-03-05`), cloud ids
  (`anthropic.claude-sonnet-4-5-20250929-v1:0`, `claude-sonnet-4-5@20250929`),
  LiteLLM-style prefixed ids (`zai/glm-4.6`, `moonshot/kimi-k2.5`), Hugging Face
  repositories (`zai-org/GLM-4.6`) and Ollama tags (`llama3.3:70b`).
- Match ids and aliases case-insensitively. Hugging Face names are mixed case;
  OpenRouter ids are lower case.
- Batch, free and other routing variants (`:batch`, `:free`) share the card of
  the base model.

## Card format

A card is YAML frontmatter followed by a short Markdown body.

```markdown
---
id: anthropic/claude-sonnet-4.5
name: Claude Sonnet 4.5
owned_by: anthropic
type: llm
description: One sentence on what the model is.
aliases: [claude-sonnet-4-5-20250929, claude-sonnet-4-5, ...]
context_length: 1000000
...
retrieved: "2026-10-14"
---

# Claude Sonnet 4.5

## Overview
## Strengths
## Limitations
## Good for
```

### Frontmatter fields

Every field except `id`, `name`, `type`, `sources` and `retrieved` is optional.
A field is left out when no source publishes the value; nothing is estimated.

| Field | Type | Unit / values | Source |
|---|---|---|---|
| `id` | string | OpenRouter id, also the file path | OpenRouter |
| `name` | string | display name | OpenRouter (vendor prefix removed), else Artificial Analysis |
| `owned_by` | string | organisation: `anthropic`, `openai`, `z-ai`, `moonshotai`, `mistralai`, `meta`, `google` | id prefix (`meta-llama` maps to `meta`) |
| `type` | string | `llm` or `embedding` | |
| `description` | string | one sentence | written from the sources |
| `aliases` | list of strings | other ids for the same model | vendor docs, Hugging Face, LiteLLM model catalogue, Ollama library |
| `context_length` | integer | tokens (input + output window) | OpenRouter `context_length`; Artificial Analysis for models OpenRouter does not list |
| `max_output_tokens` | integer | tokens per response | OpenRouter `top_provider.max_completion_tokens` |
| `capabilities` | list | any of `tool_calling`, `reasoning`, `vision`, `structured_output` | derived from OpenRouter: `tools`, `reasoning` and `structured_outputs` in `supported_parameters`; `image` in input modalities |
| `supported_parameters` | list | request parameters | OpenRouter `supported_parameters` |
| `architecture.input_modalities` | list | `text`, `image`, `file`, `audio`, `video` | OpenRouter |
| `architecture.output_modalities` | list | `text`, `image`, ... | OpenRouter |
| `architecture.tokenizer` | string | tokenizer family | OpenRouter |
| `open_weights` | boolean | weights downloadable | Artificial Analysis, Hugging Face, vendor docs |
| `license` | string | `proprietary`, or the open licence (`MIT`, `Apache-2.0`, `Modified MIT`, `Llama 4 Community License`, `Gemma Terms of Use`, ...) | Artificial Analysis, Hugging Face |
| `release_date` | string | `YYYY-MM-DD` | vendor docs (Anthropic), else Artificial Analysis |
| `knowledge_cutoff` | string | `YYYY-MM` | vendor docs; else OpenRouter `knowledge_cutoff`; else Artificial Analysis. Only values the vendor has published. For Claude models this is Anthropic's *reliable knowledge cutoff*; the body gives the training data cutoff when it differs |
| `pricing.input` | number | USD per million input tokens | OpenRouter `pricing.prompt` x 1,000,000 |
| `pricing.output` | number | USD per million output tokens | OpenRouter `pricing.completion` x 1,000,000 |
| `pricing.cache_read` | number | USD per million cached input tokens read | OpenRouter `pricing.input_cache_read` x 1,000,000 |
| `pricing.cache_write` | number | USD per million tokens written to cache | OpenRouter `pricing.input_cache_write` x 1,000,000 |
| `benchmarks.*` | numbers | see below | Artificial Analysis |
| `benchmark_variant` | string | the Artificial Analysis configuration the benchmark numbers belong to, e.g. `Claude Opus 5.5 (Max, Default Fallback)` | Artificial Analysis |
| `sources` | list of URLs | every page the card's facts came from | |
| `retrieved` | string | `YYYY-MM-DD` the sources were read | |

Pricing is OpenRouter's list price for the model's main endpoint. Where
OpenRouter charges more for long prompts (for example above 200,000 tokens),
the card body says so. Vendor and self-hosted prices differ.

### Benchmarks

All benchmark numbers come from [Artificial Analysis](https://artificialanalysis.ai)
(AA). AA tests each model in one or more configurations (reasoning effort,
thinking on or off). A card records the configuration AA lists first for the
model, normally its highest-effort reasoning setting, and names it in
`benchmark_variant`. Lower-effort settings score lower, answer sooner and use
fewer tokens.

| Field | Meaning | Unit |
|---|---|---|
| `intelligence_index` | AA Intelligence Index v4.3.2: weighted average of 10 evaluations across agents (30%), coding (20%), scientific reasoning (20%) and general knowledge work (30%) | 0-100 |
| `coding_index` | AA Coding Index, as reported in OpenRouter's `benchmarks.artificial_analysis` (not shown on AA's current model pages) | 0-100 |
| `agentic_index` | AA Agentic Index, from the same OpenRouter field | 0-100 |
| `omniscience_index` | AA-Omniscience: rewards correct answers, penalises wrong ones, so guessing costs points | -100 to 100 |
| `humanitys_last_exam` | Humanity's Last Exam, text-only subset | % correct |
| `gpqa_diamond` | GPQA Diamond (retired from the index; kept where AA published it) | % correct |
| `scicode` | SciCode | % correct |
| `terminal_bench_hard` | Terminal-Bench Hard (earlier AA terminal agent benchmark) | % of tasks passed |
| `terminal_bench_4` | Terminal-Bench 4.0, mini-swe-agent harness | % of tasks passed |
| `long_context_reasoning` | AA-LCR, questions over ~100k-token document sets | % correct |
| `ifbench` | IFBench instruction following | % correct |
| `tau2_bench` | tau2-bench agent/user tool-use simulation | % of tasks passed |
| `mmmu_pro` | MMMU-Pro visual reasoning | % correct |
| `output_tokens_per_second` | median output speed on the provider AA measures (usually the vendor's API) | tokens per second |
| `time_to_first_token_seconds` | median time to the first streamed token | seconds |

Notes:

- There is no `math_index`. AA no longer publishes a separate maths index, so
  the field is omitted everywhere.
- For reasoning models AA's time to first token includes hidden thinking time.
  At maximum effort this can be minutes, not seconds.
- AA percentages are stored as 0-100 with one decimal. A `0` is a published
  zero, not a missing value (Terminal-Bench 4.0 is hard enough that many
  models score zero).

### Body

120-300 words of plain Markdown with four sections: **Overview**,
**Strengths**, **Limitations**, **Good for**. It is written from the card's
sources only (OpenRouter's description, vendor documentation, Hugging Face
model cards, AA's published results) and says which AA configuration a quoted
number belongs to. Lifecycle status (deprecated, retirement date) goes in the
body.

## Sources policy

- Never invent or estimate a number. If no source publishes a value, leave the
  field out.
- Field priority: OpenRouter for limits, parameters, modalities and price;
  vendor documentation for knowledge cutoff, release date (where the vendor
  states one) and API ids; Artificial Analysis for benchmarks and release
  dates otherwise; Hugging Face for open-weight licences and repository names.
- Every card lists the pages it used in `sources` and the date they were read
  in `retrieved`.
- When sources disagree, the frontmatter follows the priority above and the
  body names the difference (for example Anthropic's 200K context for Claude
  Sonnet 4.5 against OpenRouter's 1M).

## Adding a card

1. Find the OpenRouter id: `curl -s https://openrouter.ai/api/v1/models | jq -r '.data[].id' | grep <name>`.
   If OpenRouter does not list the model, use the lower-cased Hugging Face
   repository name.
2. Create `<id>.md` with the frontmatter above. Copy an existing card of the
   same vendor as a template.
3. Fill the OpenRouter fields from `jq '.data[] | select(.id=="<id>")'` (or run
   `scripts/refresh_openrouter.py` after creating the file with `id` set).
4. Open `https://artificialanalysis.ai/models/<slug>` and copy the figures for
   the first listed configuration into `benchmarks`, with its name in
   `benchmark_variant`.
5. Add vendor API ids, cloud ids and Hugging Face repositories to `aliases`.
6. Write the body from the sources. List every source URL and set `retrieved`.
7. Check the frontmatter parses, for example
   `python3 -c "import sys,yaml; yaml.safe_load(open(sys.argv[1]).read().split('---')[1])" <file>`.

## Refreshing

`scripts/refresh_openrouter.py` (standard library only, no API key) re-reads
OpenRouter's public model list and rewrites `context_length`,
`max_output_tokens`, `capabilities`, `supported_parameters`, `architecture` and
`pricing` on every card OpenRouter lists. It leaves everything else alone.

```bash
python3 scripts/refresh_openrouter.py --dry-run         # show which cards would change
python3 scripts/refresh_openrouter.py                   # rewrite them
python3 scripts/refresh_openrouter.py --set-retrieved   # also set retrieved to today
```

Artificial Analysis figures, vendor ids, dates and the body are refreshed by
hand. Bump `retrieved` when you re-check a whole card.

## Cards

64 cards, retrieved 2026-10-14. Intelligence Index is Artificial Analysis v4.3.2 for the configuration named in each card's `benchmark_variant`.

| Card | Name | Context (tokens) | Open weights | AA Intelligence Index |
|---|---|---:|---|---:|
| [`anthropic/claude-fable-5`](anthropic/claude-fable-5.md) | Claude Fable 5 | 1,000,000 | no | 49.6 |
| [`anthropic/claude-fable-5.1`](anthropic/claude-fable-5.1.md) | Claude Fable 5.1 | 1,000,000 | no | 53.4 |
| [`anthropic/claude-haiku-4.5`](anthropic/claude-haiku-4.5.md) | Claude Haiku 4.5 | 200,000 | no | 16.9 |
| [`anthropic/claude-haiku-5.5`](anthropic/claude-haiku-5.5.md) | Claude Haiku 5.5 | 1,000,000 | no | 43.4 |
| [`anthropic/claude-opus-4.5`](anthropic/claude-opus-4.5.md) | Claude Opus 4.5 | 200,000 | no | 29.1 |
| [`anthropic/claude-opus-4.6`](anthropic/claude-opus-4.6.md) | Claude Opus 4.6 | 1,000,000 | no | 31.9 |
| [`anthropic/claude-opus-4.7`](anthropic/claude-opus-4.7.md) | Claude Opus 4.7 | 1,000,000 | no | 40.7 |
| [`anthropic/claude-opus-4.8`](anthropic/claude-opus-4.8.md) | Claude Opus 4.8 | 1,000,000 | no | 41.8 |
| [`anthropic/claude-opus-5`](anthropic/claude-opus-5.md) | Claude Opus 5 | 1,000,000 | no | 50.8 |
| [`anthropic/claude-opus-5.5`](anthropic/claude-opus-5.5.md) | Claude Opus 5.5 | 1,000,000 | no | 57.6 |
| [`anthropic/claude-sonnet-4.5`](anthropic/claude-sonnet-4.5.md) | Claude Sonnet 4.5 | 1,000,000 | no | 20.7 |
| [`anthropic/claude-sonnet-4.6`](anthropic/claude-sonnet-4.6.md) | Claude Sonnet 4.6 | 1,000,000 | no | 30.1 |
| [`anthropic/claude-sonnet-5`](anthropic/claude-sonnet-5.md) | Claude Sonnet 5 | 1,000,000 | no | 38.2 |
| [`anthropic/claude-sonnet-5.5`](anthropic/claude-sonnet-5.5.md) | Claude Sonnet 5.5 | 1,000,000 | no | 56 |
| [`openai/gpt-5.4`](openai/gpt-5.4.md) | GPT-5.4 | 1,050,000 | no | 39 |
| [`openai/gpt-5.4-mini`](openai/gpt-5.4-mini.md) | GPT-5.4 Mini | 400,000 | no | 24.1 |
| [`openai/gpt-5.4-nano`](openai/gpt-5.4-nano.md) | GPT-5.4 Nano | 400,000 | no | 20.7 |
| [`openai/gpt-5.4-pro`](openai/gpt-5.4-pro.md) | GPT-5.4 Pro | 1,050,000 | no |  |
| [`z-ai/glm-4.5-air`](z-ai/glm-4.5-air.md) | GLM 4.5 Air | 131,072 | yes | 11.1 |
| [`z-ai/glm-4.6`](z-ai/glm-4.6.md) | GLM 4.6 | 204,800 | yes | 18.5 |
| [`z-ai/glm-4.6v`](z-ai/glm-4.6v.md) | GLM 4.6V | 131,072 | yes | 11.2 |
| [`z-ai/glm-4.7`](z-ai/glm-4.7.md) | GLM 4.7 | 204,800 | yes | 22.2 |
| [`z-ai/glm-4.7-flash`](z-ai/glm-4.7-flash.md) | GLM 4.7 Flash | 200,000 | yes | 14.9 |
| [`z-ai/glm-5`](z-ai/glm-5.md) | GLM 5 | 204,800 | yes | 27.9 |
| [`z-ai/glm-5-turbo`](z-ai/glm-5-turbo.md) | GLM 5 Turbo | 202,752 | no | 26.6 |
| [`z-ai/glm-5.1`](z-ai/glm-5.1.md) | GLM 5.1 | 204,800 | yes | 26.1 |
| [`z-ai/glm-5.2`](z-ai/glm-5.2.md) | GLM 5.2 | 1,048,576 | yes | 33.7 |
| [`z-ai/glm-5.3`](z-ai/glm-5.3.md) | GLM 5.3 | 1,048,576 | yes | 44.8 |
| [`z-ai/glm-5.3-flash`](z-ai/glm-5.3-flash.md) | GLM 5.3 Flash | 1,048,576 | yes | 41.8 |
| [`z-ai/glm-5.3-flashx`](z-ai/glm-5.3-flashx.md) | GLM 5.3 FlashX | 1,048,576 | not stated |  |
| [`z-ai/glm-5.3-prime`](z-ai/glm-5.3-prime.md) | GLM 5.3 Prime | 1,000,000 | not stated |  |
| [`z-ai/glm-5v-turbo`](z-ai/glm-5v-turbo.md) | GLM 5V Turbo | 202,752 | no | 23.5 |
| [`moonshotai/kimi-k2-thinking`](moonshotai/kimi-k2-thinking.md) | Kimi K2 Thinking | 262,144 | yes | 22 |
| [`moonshotai/kimi-k2.5`](moonshotai/kimi-k2.5.md) | Kimi K2.5 | 262,144 | yes | 23.5 |
| [`moonshotai/kimi-k2.6`](moonshotai/kimi-k2.6.md) | Kimi K2.6 | 262,144 | yes | 27 |
| [`moonshotai/kimi-k2.7-code`](moonshotai/kimi-k2.7-code.md) | Kimi K2.7 Code | 262,144 | yes | 25.8 |
| [`moonshotai/kimi-k3`](moonshotai/kimi-k3.md) | Kimi K3 | 1,048,576 | yes | 43.6 |
| [`mistralai/codestral-2508`](mistralai/codestral-2508.md) | Codestral 2508 | 256,000 | no |  |
| [`mistralai/devstral-2512`](mistralai/devstral-2512.md) | Devstral 2 2512 | 262,144 | yes | 8.6 |
| [`mistralai/ministral-14b-2512`](mistralai/ministral-14b-2512.md) | Ministral 3 14B 2512 | 262,144 | yes | 6 |
| [`mistralai/ministral-3b-2512`](mistralai/ministral-3b-2512.md) | Ministral 3 3B 2512 | 131,072 | yes | 4.8 |
| [`mistralai/ministral-8b-2512`](mistralai/ministral-8b-2512.md) | Ministral 3 8B 2512 | 262,144 | yes | 5.5 |
| [`mistralai/mistral-large-2512`](mistralai/mistral-large-2512.md) | Mistral Large 3 2512 | 262,144 | yes | 9.3 |
| [`mistralai/mistral-large-4-0`](mistralai/mistral-large-4-0.md) | Mistral Large 4 | 1,048,576 | not stated | 38.4 |
| [`mistralai/mistral-medium-3-5`](mistralai/mistral-medium-3-5.md) | Mistral Medium 3.5 | 262,144 | yes | 14.2 |
| [`mistralai/mistral-small-2603`](mistralai/mistral-small-2603.md) | Mistral Small 4 | 262,144 | yes | 11.3 |
| [`mistralai/mistral-small-3.2-24b-instruct`](mistralai/mistral-small-3.2-24b-instruct.md) | Mistral Small 3.2 24B | 256,000 | yes | 8.2 |
| [`meta-llama/llama-3.1-8b-instruct`](meta-llama/llama-3.1-8b-instruct.md) | Llama 3.1 8B Instruct | 131,072 | yes | 6.9 |
| [`meta-llama/llama-3.3-70b-instruct`](meta-llama/llama-3.3-70b-instruct.md) | Llama 3.3 70B Instruct | 131,072 | yes | 7.7 |
| [`meta-llama/llama-4-maverick`](meta-llama/llama-4-maverick.md) | Llama 4 Maverick | 1,048,576 | yes | 10 |
| [`meta-llama/llama-4-scout`](meta-llama/llama-4-scout.md) | Llama 4 Scout | 1,310,720 | yes | 8.1 |
| [`meta-llama/llama-guard-4-12b`](meta-llama/llama-guard-4-12b.md) | Llama Guard 4 12B | 163,840 | yes |  |
| [`meta/muse-glimmer-30b`](meta/muse-glimmer-30b.md) | Muse Glimmer 30B | 131,072 | yes | 17.5 |
| [`meta/muse-spark-1.3`](meta/muse-spark-1.3.md) | Muse Spark 1.3 | 1,048,576 | no | 48.1 |
| [`meta/muse-spark-1.3-contributor`](meta/muse-spark-1.3-contributor.md) | Muse Spark 1.3 Contributor | 1,048,576 | no |  |
| [`meta/muse-wonder`](meta/muse-wonder.md) | Muse Wonder | 1,048,576 | no | 52.4 |
| [`google/gemma-3-12b-it`](google/gemma-3-12b-it.md) | Gemma 3 12B | 131,072 | yes | 3.8 |
| [`google/gemma-3-27b-it`](google/gemma-3-27b-it.md) | Gemma 3 27B | 131,072 | yes | 4.9 |
| [`google/gemma-3-4b-it`](google/gemma-3-4b-it.md) | Gemma 3 4B | 131,072 | yes | 4.8 |
| [`google/gemma-4-12b-it`](google/gemma-4-12b-it.md) | Gemma 4 12B | 262,144 | yes | 14.2 |
| [`google/gemma-4-26b-a4b-it`](google/gemma-4-26b-a4b-it.md) | Gemma 4 26B A4B | 262,144 | yes | 16.7 |
| [`google/gemma-4-31b-it`](google/gemma-4-31b-it.md) | Gemma 4 31B | 262,144 | yes | 14.7 |
| [`google/gemma-4-e2b-it`](google/gemma-4-e2b-it.md) | Gemma 4 E2B | 128,000 | yes | 7.8 |
| [`google/gemma-4-e4b-it`](google/gemma-4-e4b-it.md) | Gemma 4 E4B | 128,000 | yes | 8.9 |
