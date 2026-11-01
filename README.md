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
  for `google/gemma-4-12B-it`, `paddlepaddle/paddleocr-vl-1.6` for
  `PaddlePaddle/PaddleOCR-VL-1.6`). Where the vendor already has a directory
  here under a different name, that directory wins (`zai-org/GLM-OCR` is
  `z-ai/glm-ocr`, `deepseek-ai/DeepSeek-OCR` is `deepseek/deepseek-ocr`). An
  API-only model with no Hugging Face repository uses the vendor's API id under
  the vendor prefix (`mistralai/voxtral-mini-2602`). The card says so in its
  overview.
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
| `owned_by` | string | organisation that made the model: `anthropic`, `openai`, `z-ai`, `moonshotai`, `minimax`, `mistralai`, `meta`, `google`, `deepseek`, `qwen`, `unbabel`, `baidu`, `ibm`, `microsoft`, `amazon`, `nvidia`, `cohere`, `voyageai`, `perplexity`, `liquid`, `baai`, `jinaai`, `nomic-ai`, `snowflake`, `mixedbread-ai`, `sentence-transformers`, `thenlper`, `allenai`, `opendatalab`, `rednote`, `nanonets`, `datalab`, `lightonai` | id prefix (`meta-llama` maps to `meta`, `paddlepaddle` maps to `baidu`, `ibm-granite` and `docling-project` to `ibm`, `intfloat` to `microsoft`, `alibaba-nlp` to `qwen`, `dots-studio` to `rednote`, `datalab-to` to `datalab`) |
| `type` | string | `llm` (anything that takes a prompt and returns text, including OCR, translation, moderation and speech-to-text models), `embedding`, `reranker`, `tts` (text-to-speech), `image` (image generation or editing), `video` (video generation) or `music` | |
| `description` | string | one sentence | written from the sources |
| `aliases` | list of strings | other ids for the same model | vendor docs, Hugging Face, LiteLLM model catalogue, Ollama library |
| `context_length` | integer | tokens (input + output window) | OpenRouter `context_length`; Artificial Analysis for models OpenRouter does not list |
| `max_output_tokens` | integer | tokens per response | OpenRouter `top_provider.max_completion_tokens` |
| `capabilities` | list | any of `tool_calling`, `reasoning`, `vision`, `structured_output` | derived from OpenRouter: `tools`, `reasoning` and `structured_outputs` in `supported_parameters`; `image` in input modalities |
| `supported_parameters` | list | request parameters | OpenRouter `supported_parameters` |
| `architecture.input_modalities` | list | `text`, `image`, `file`, `audio`, `video` | OpenRouter |
| `architecture.output_modalities` | list | `text`, `image`, `audio`, `video`, and OpenRouter's task outputs: `embeddings` (embedding models), `rerank` (rerankers), `transcription` (speech-to-text), `speech` (text-to-speech). Cards for models OpenRouter does not list use the same values | OpenRouter |
| `architecture.tokenizer` | string | tokenizer family | OpenRouter |
| `open_weights` | boolean | weights downloadable | Artificial Analysis, Hugging Face, vendor docs |
| `license` | string | `proprietary`, or the open licence (`MIT`, `Apache-2.0`, `Modified MIT`, `Llama 4 Community License`, `Gemma Terms of Use`, ...) | Artificial Analysis, Hugging Face |
| `release_date` | string | `YYYY-MM-DD` | vendor docs (Anthropic), else Artificial Analysis |
| `knowledge_cutoff` | string | `YYYY-MM` | vendor docs; else OpenRouter `knowledge_cutoff`; else Artificial Analysis. Only values the vendor has published. For Claude models this is Anthropic's *reliable knowledge cutoff*; the body gives the training data cutoff when it differs |
| `pricing.input` | number | USD per million input tokens | OpenRouter `pricing.prompt` x 1,000,000 |
| `pricing.output` | number | USD per million output tokens | OpenRouter `pricing.completion` x 1,000,000 |
| `pricing.cache_read` | number | USD per million cached input tokens read | OpenRouter `pricing.input_cache_read` x 1,000,000 |
| `pricing.cache_write` | number | USD per million tokens written to cache | OpenRouter `pricing.input_cache_write` x 1,000,000 |
| `embedding_dimensions` | integer | default output dimension of an embedding model; Matryoshka options go in the body | model card |
| `mteb_score` | number | MTEB mean task score of an embedding model; the body names the leaderboard (multilingual v2, English v2) | model card, MTEB leaderboard |
| `benchmarks.*` | numbers | see below | Artificial Analysis |
| `benchmark_variant` | string | the Artificial Analysis configuration the benchmark numbers belong to, e.g. `Claude Opus 5.5 (Max, Default Fallback)` | Artificial Analysis |
| `sources` | list of URLs | every page the card's facts came from | |
| `retrieved` | string | `YYYY-MM-DD` the sources were read | |

Pricing is OpenRouter's list price for the model's main endpoint. Where
OpenRouter charges more for long prompts (for example above 200,000 tokens),
the card body says so. Vendor and self-hosted prices differ. `pricing` holds
per-token prices only: models OpenRouter bills per second of audio, per
character, per image or per video (speech, video and rerank models) have no
`pricing` field, and the body gives the price with its unit.

OpenRouter's default `/api/v1/models` lists only text-output models. Embedding,
rerank, speech, image and video models appear only with
`?output_modalities=all`.

### Benchmarks

All benchmark numbers come from [Artificial Analysis](https://artificialanalysis.ai)
(AA). AA tests each model in one or more configurations (reasoning effort,
thinking on or off). A card records the configuration AA lists first for the
model, normally its highest-effort reasoning setting, and names it in
`benchmark_variant`. Lower-effort settings score lower, answer sooner and use
fewer tokens. Models AA does not test (OCR, translation, speech, embeddings,
image and video generation) have no `benchmarks`; the body quotes the vendor's
own numbers, or AA's speech-to-text, text-to-speech, speech-to-speech,
text-to-image, image-editing, text-to-video, image-to-video and music
leaderboards, with the date read, instead.

| Field | Meaning | Unit |
|---|---|---|
| `intelligence_index` | AA Intelligence Index. Cards retrieved from 2026-11-01 carry v5.0: four categories of 25% each, knowledge work (AA-Briefcase v1.1, AutomationBench-AA, GDP.pdf), coding (FrontierCode 2.0, Terminal-Bench 4.0), science (Terminal-Bench-Science 0.1, CritPt v2 hard subset) and general (AA-Omniscience v1.1, HLE-Diamond). Cards retrieved in October 2026 carry v4.3.2: 10 evaluations across agents (30%), coding (20%), scientific reasoning (20%) and general knowledge work (30%). The two versions are not comparable | 0-100 |
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
- AA scores only current models on Intelligence Index v5.0. Older models keep
  their individual evaluation results on AA but have no v5.0 index, so their
  cards have no `intelligence_index`.
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

## Assets

`assets/` holds one icon per `owned_by` value (`assets/openai.svg`,
`assets/moonshotai.jpg`, `assets/baai.webp`). The SVG and JPG files come from
Artificial Analysis (`https://artificialanalysis.ai/img/logos/<creator>`);
vendors AA does not list use their Hugging Face organisation avatar (WebP).
The file name is the `owned_by` value; the extension is the image's real format.

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

1. Find the OpenRouter id: `curl -s 'https://openrouter.ai/api/v1/models?output_modalities=all' | jq -r '.data[].id' | grep <name>`.
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

`scripts/update_readme_index.py` rebuilds the table under `## Cards` below from
the cards' frontmatter (needs PyYAML). Run it after adding or removing a card.

## Cards

683 cards, retrieved 2026-10-14 to 2026-11-01. Intelligence Index is Artificial Analysis v5.0 on cards retrieved from 2026-11-01 and v4.3.2 on earlier cards, for the configuration named in each card's `benchmark_variant`; the two versions are not comparable. Models Artificial Analysis does not test (OCR, translation, speech, embeddings, rerankers, image and video generation) have no index.

| Card | Name | Context (tokens) | Open weights | AA Intelligence Index |
|---|---|---:|---|---:|
| [`anthropic/claude-3-haiku`](anthropic/claude-3-haiku.md) | Claude 3 Haiku | 200,000 | no |  |
| [`anthropic/claude-3-sonnet`](anthropic/claude-3-sonnet.md) | Claude 3 Sonnet | 200,000 | no |  |
| [`anthropic/claude-3.5-haiku`](anthropic/claude-3.5-haiku.md) | Claude 3.5 Haiku | 200,000 | no |  |
| [`anthropic/claude-3.5-sonnet`](anthropic/claude-3.5-sonnet.md) | Claude 3.5 Sonnet | 200,000 | no |  |
| [`anthropic/claude-3.7-sonnet`](anthropic/claude-3.7-sonnet.md) | Claude 3.7 Sonnet | 200,000 | no |  |
| [`anthropic/claude-fable-5.1`](anthropic/claude-fable-5.1.md) | Claude Fable 5.1 | 1,000,000 | no | 53.4 |
| [`anthropic/claude-fable-5`](anthropic/claude-fable-5.md) | Claude Fable 5 | 1,000,000 | no | 49.6 |
| [`anthropic/claude-haiku-4.5`](anthropic/claude-haiku-4.5.md) | Claude Haiku 4.5 | 200,000 | no | 16.9 |
| [`anthropic/claude-haiku-5.5`](anthropic/claude-haiku-5.5.md) | Claude Haiku 5.5 | 1,000,000 | no | 43.4 |
| [`anthropic/claude-mythos-5.1`](anthropic/claude-mythos-5.1.md) | Claude Mythos 5.1 | 1,000,000 | no |  |
| [`anthropic/claude-mythos-5`](anthropic/claude-mythos-5.md) | Claude Mythos 5 | 1,000,000 | no |  |
| [`anthropic/claude-mythos-preview`](anthropic/claude-mythos-preview.md) | Claude Mythos Preview | 1,000,000 | no |  |
| [`anthropic/claude-opus-4.1`](anthropic/claude-opus-4.1.md) | Claude Opus 4.1 | 200,000 | no |  |
| [`anthropic/claude-opus-4.5`](anthropic/claude-opus-4.5.md) | Claude Opus 4.5 | 200,000 | no | 29.1 |
| [`anthropic/claude-opus-4.6`](anthropic/claude-opus-4.6.md) | Claude Opus 4.6 | 1,000,000 | no | 31.9 |
| [`anthropic/claude-opus-4.7`](anthropic/claude-opus-4.7.md) | Claude Opus 4.7 | 1,000,000 | no | 40.7 |
| [`anthropic/claude-opus-4.8`](anthropic/claude-opus-4.8.md) | Claude Opus 4.8 | 1,000,000 | no | 41.8 |
| [`anthropic/claude-opus-4`](anthropic/claude-opus-4.md) | Claude 4 Opus | 200,000 | no |  |
| [`anthropic/claude-opus-5.5`](anthropic/claude-opus-5.5.md) | Claude Opus 5.5 | 1,000,000 | no | 57.6 |
| [`anthropic/claude-opus-5`](anthropic/claude-opus-5.md) | Claude Opus 5 | 1,000,000 | no | 50.8 |
| [`anthropic/claude-sonnet-4.5`](anthropic/claude-sonnet-4.5.md) | Claude Sonnet 4.5 | 1,000,000 | no | 20.7 |
| [`anthropic/claude-sonnet-4.6`](anthropic/claude-sonnet-4.6.md) | Claude Sonnet 4.6 | 1,000,000 | no | 30.1 |
| [`anthropic/claude-sonnet-4`](anthropic/claude-sonnet-4.md) | Claude 4 Sonnet | 1,000,000 | no |  |
| [`anthropic/claude-sonnet-5.5`](anthropic/claude-sonnet-5.5.md) | Claude Sonnet 5.5 | 1,000,000 | no | 56 |
| [`anthropic/claude-sonnet-5`](anthropic/claude-sonnet-5.md) | Claude Sonnet 5 | 1,000,000 | no | 38.2 |
| [`openai/ada`](openai/ada.md) | ada | 2,049 | no |  |
| [`openai/babbage-002`](openai/babbage-002.md) | babbage-002 |  | no |  |
| [`openai/babbage`](openai/babbage.md) | babbage | 2,049 | no |  |
| [`openai/chatgpt-4o-latest`](openai/chatgpt-4o-latest.md) | ChatGPT-4o | 128,000 | no |  |
| [`openai/chatgpt-image-latest`](openai/chatgpt-image-latest.md) | chatgpt-image-latest |  | no |  |
| [`openai/code-cushman-001`](openai/code-cushman-001.md) | code-cushman-001 | 2,048 | no |  |
| [`openai/code-cushman-002`](openai/code-cushman-002.md) | code-cushman-002 | 2,048 | no |  |
| [`openai/code-davinci-001`](openai/code-davinci-001.md) | code-davinci-001 | 8,001 | no |  |
| [`openai/code-davinci-002`](openai/code-davinci-002.md) | code-davinci-002 | 8,001 | no |  |
| [`openai/code-davinci-edit-001`](openai/code-davinci-edit-001.md) | code-davinci-edit-001 |  | no |  |
| [`openai/code-search-ada-code-001`](openai/code-search-ada-code-001.md) | code-search-ada-code-001 | 2,048 | no |  |
| [`openai/code-search-ada-text-001`](openai/code-search-ada-text-001.md) | code-search-ada-text-001 | 2,048 | no |  |
| [`openai/code-search-babbage-code-001`](openai/code-search-babbage-code-001.md) | code-search-babbage-code-001 | 2,048 | no |  |
| [`openai/code-search-babbage-text-001`](openai/code-search-babbage-text-001.md) | code-search-babbage-text-001 | 2,048 | no |  |
| [`openai/codex-mini-latest`](openai/codex-mini-latest.md) | codex-mini-latest | 200,000 | no |  |
| [`openai/computer-use-preview`](openai/computer-use-preview.md) | computer-use-preview | 8,192 | no |  |
| [`openai/curie`](openai/curie.md) | curie | 2,049 | no |  |
| [`openai/dall-e-2`](openai/dall-e-2.md) | DALL·E 2 |  | no |  |
| [`openai/dall-e-3`](openai/dall-e-3.md) | DALL·E 3 |  | no |  |
| [`openai/davinci-002`](openai/davinci-002.md) | davinci-002 |  | no |  |
| [`openai/davinci`](openai/davinci.md) | davinci | 2,049 | no |  |
| [`openai/gpt-3.5-turbo-instruct`](openai/gpt-3.5-turbo-instruct.md) | gpt-3.5-turbo-instruct | 4,096 | no |  |
| [`openai/gpt-3.5-turbo`](openai/gpt-3.5-turbo.md) | GPT-3.5 Turbo | 16,385 | no |  |
| [`openai/gpt-4-32k`](openai/gpt-4-32k.md) | GPT-4 32K | 32,768 | no |  |
| [`openai/gpt-4-turbo`](openai/gpt-4-turbo.md) | GPT-4 Turbo | 128,000 | no |  |
| [`openai/gpt-4-vision-preview`](openai/gpt-4-vision-preview.md) | GPT-4 Turbo with Vision Preview | 128,000 | no |  |
| [`openai/gpt-4.1-mini`](openai/gpt-4.1-mini.md) | GPT-4.1 Mini | 1,047,576 | no |  |
| [`openai/gpt-4.1-nano`](openai/gpt-4.1-nano.md) | GPT-4.1 Nano | 1,047,576 | no |  |
| [`openai/gpt-4.1`](openai/gpt-4.1.md) | GPT-4.1 | 1,047,576 | no |  |
| [`openai/gpt-4.5-preview`](openai/gpt-4.5-preview.md) | GPT-4.5 Preview | 128,000 | no |  |
| [`openai/gpt-4`](openai/gpt-4.md) | GPT-4 | 8,191 | no |  |
| [`openai/gpt-4o-audio-preview`](openai/gpt-4o-audio-preview.md) | GPT-4o Audio Preview | 128,000 | no |  |
| [`openai/gpt-4o-mini-audio-preview`](openai/gpt-4o-mini-audio-preview.md) | GPT-4o Mini Audio Preview | 128,000 | no |  |
| [`openai/gpt-4o-mini-realtime-preview`](openai/gpt-4o-mini-realtime-preview.md) | GPT-4o Mini Realtime Preview | 16,000 | no |  |
| [`openai/gpt-4o-mini-search-preview`](openai/gpt-4o-mini-search-preview.md) | GPT-4o Mini Search Preview | 128,000 | no |  |
| [`openai/gpt-4o-mini-transcribe`](openai/gpt-4o-mini-transcribe.md) | GPT-4o Mini Transcribe | 128,000 | no |  |
| [`openai/gpt-4o-mini-tts`](openai/gpt-4o-mini-tts.md) | GPT-4o Mini TTS |  | no |  |
| [`openai/gpt-4o-mini`](openai/gpt-4o-mini.md) | GPT-4o-mini | 128,000 | no |  |
| [`openai/gpt-4o-realtime-preview`](openai/gpt-4o-realtime-preview.md) | GPT-4o Realtime Preview | 32,000 | no |  |
| [`openai/gpt-4o-search-preview`](openai/gpt-4o-search-preview.md) | GPT-4o Search Preview | 128,000 | no |  |
| [`openai/gpt-4o-transcribe-diarize`](openai/gpt-4o-transcribe-diarize.md) | GPT-4o Transcribe Diarize | 16,000 | no |  |
| [`openai/gpt-4o-transcribe`](openai/gpt-4o-transcribe.md) | GPT-4o Transcribe | 128,000 | no |  |
| [`openai/gpt-4o`](openai/gpt-4o.md) | GPT-4o | 128,000 | no |  |
| [`openai/gpt-5-chat-latest`](openai/gpt-5-chat-latest.md) | GPT-5 Chat | 128,000 | no |  |
| [`openai/gpt-5-codex`](openai/gpt-5-codex.md) | GPT-5 Codex | 400,000 | no |  |
| [`openai/gpt-5-image-mini`](openai/gpt-5-image-mini.md) | GPT-5 Image Mini | 400,000 | no |  |
| [`openai/gpt-5-image`](openai/gpt-5-image.md) | GPT-5 Image | 400,000 | no |  |
| [`openai/gpt-5-mini`](openai/gpt-5-mini.md) | GPT-5 Mini | 400,000 | no |  |
| [`openai/gpt-5-nano`](openai/gpt-5-nano.md) | GPT-5 Nano | 400,000 | no |  |
| [`openai/gpt-5-pro`](openai/gpt-5-pro.md) | GPT-5 Pro | 400,000 | no |  |
| [`openai/gpt-5-search-api`](openai/gpt-5-search-api.md) | GPT-5 Search API | 200,000 | no |  |
| [`openai/gpt-5.1-chat-latest`](openai/gpt-5.1-chat-latest.md) | GPT-5.1 Chat | 128,000 | no |  |
| [`openai/gpt-5.1-codex-max`](openai/gpt-5.1-codex-max.md) | GPT-5.1-Codex-Max | 400,000 | no |  |
| [`openai/gpt-5.1-codex-mini`](openai/gpt-5.1-codex-mini.md) | GPT-5.1-Codex-Mini | 400,000 | no |  |
| [`openai/gpt-5.1-codex`](openai/gpt-5.1-codex.md) | GPT-5.1-Codex | 400,000 | no |  |
| [`openai/gpt-5.1`](openai/gpt-5.1.md) | GPT-5.1 | 400,000 | no |  |
| [`openai/gpt-5.2-chat`](openai/gpt-5.2-chat.md) | GPT-5.2 Chat | 128,000 | no |  |
| [`openai/gpt-5.2-codex`](openai/gpt-5.2-codex.md) | GPT-5.2-Codex | 400,000 | no |  |
| [`openai/gpt-5.2-pro`](openai/gpt-5.2-pro.md) | GPT-5.2 Pro | 400,000 | no |  |
| [`openai/gpt-5.2`](openai/gpt-5.2.md) | GPT-5.2 | 400,000 | no |  |
| [`openai/gpt-5.3-chat-latest`](openai/gpt-5.3-chat-latest.md) | GPT-5.3 Chat | 128,000 | no |  |
| [`openai/gpt-5.3-codex`](openai/gpt-5.3-codex.md) | GPT-5.3-Codex | 400,000 | no |  |
| [`openai/gpt-5.4-cyber`](openai/gpt-5.4-cyber.md) | GPT-5.4 Cyber |  | no |  |
| [`openai/gpt-5.4-image-2`](openai/gpt-5.4-image-2.md) | GPT-5.4 Image 2 | 272,000 | no |  |
| [`openai/gpt-5.4-mini`](openai/gpt-5.4-mini.md) | GPT-5.4 Mini | 400,000 | no | 24.1 |
| [`openai/gpt-5.4-nano`](openai/gpt-5.4-nano.md) | GPT-5.4 Nano | 400,000 | no | 20.7 |
| [`openai/gpt-5.4-pro`](openai/gpt-5.4-pro.md) | GPT-5.4 Pro | 1,050,000 | no |  |
| [`openai/gpt-5.4`](openai/gpt-5.4.md) | GPT-5.4 | 1,050,000 | no | 39 |
| [`openai/gpt-5.5-cyber`](openai/gpt-5.5-cyber.md) | GPT-5.5 Cyber |  | no |  |
| [`openai/gpt-5.5-pro`](openai/gpt-5.5-pro.md) | GPT-5.5 Pro | 1,050,000 | no |  |
| [`openai/gpt-5.5`](openai/gpt-5.5.md) | GPT-5.5 | 1,050,000 | no |  |
| [`openai/gpt-5.6-cyber`](openai/gpt-5.6-cyber.md) | GPT-5.6 Cyber | 400,000 | no |  |
| [`openai/gpt-5.6-luna-pro`](openai/gpt-5.6-luna-pro.md) | GPT-5.6 Luna Pro | 1,050,000 | no |  |
| [`openai/gpt-5.6-luna`](openai/gpt-5.6-luna.md) | GPT-5.6 Luna | 1,050,000 | no |  |
| [`openai/gpt-5.6-sol-pro`](openai/gpt-5.6-sol-pro.md) | GPT-5.6 Sol Pro | 1,050,000 | no |  |
| [`openai/gpt-5.6-sol`](openai/gpt-5.6-sol.md) | GPT-5.6 Sol | 1,050,000 | no |  |
| [`openai/gpt-5.6-terra-pro`](openai/gpt-5.6-terra-pro.md) | GPT-5.6 Terra Pro | 1,050,000 | no |  |
| [`openai/gpt-5.6-terra`](openai/gpt-5.6-terra.md) | GPT-5.6 Terra | 1,050,000 | no |  |
| [`openai/gpt-5`](openai/gpt-5.md) | GPT-5 | 400,000 | no |  |
| [`openai/gpt-6-astra-law`](openai/gpt-6-astra-law.md) | GPT-6 Astra Law |  | no |  |
| [`openai/gpt-6-astra-pro`](openai/gpt-6-astra-pro.md) | GPT-6 Astra Pro | 1,050,000 | no |  |
| [`openai/gpt-6-astra`](openai/gpt-6-astra.md) | GPT-6 Astra | 1,050,000 | no | 56.9 |
| [`openai/gpt-6-luna-decisions`](openai/gpt-6-luna-decisions.md) | GPT-6 Luna Decisions | 1,050,000 | no |  |
| [`openai/gpt-6-luna-pro`](openai/gpt-6-luna-pro.md) | GPT-6 Luna Pro | 1,050,000 | no |  |
| [`openai/gpt-6-luna`](openai/gpt-6-luna.md) | GPT-6 Luna | 1,050,000 | no | 27.8 |
| [`openai/gpt-6-rosalind`](openai/gpt-6-rosalind.md) | GPT-6 Rosalind |  | no |  |
| [`openai/gpt-6-sol-pro`](openai/gpt-6-sol-pro.md) | GPT-6 Sol Pro | 1,050,000 | no |  |
| [`openai/gpt-6-sol`](openai/gpt-6-sol.md) | GPT-6 Sol | 1,050,000 | no |  |
| [`openai/gpt-6.1-sol-pro`](openai/gpt-6.1-sol-pro.md) | GPT-6.1 Sol Pro | 1,050,000 | no |  |
| [`openai/gpt-6.1-sol`](openai/gpt-6.1-sol.md) | GPT-6.1 Sol | 1,050,000 | no | 54.5 |
| [`openai/gpt-6.1-terra-pro`](openai/gpt-6.1-terra-pro.md) | GPT-6.1 Terra Pro | 1,050,000 | no |  |
| [`openai/gpt-6.1-terra`](openai/gpt-6.1-terra.md) | GPT-6.1 Terra | 1,050,000 | no | 51 |
| [`openai/gpt-audio-1.5`](openai/gpt-audio-1.5.md) | GPT Audio 1.5 | 128,000 | no |  |
| [`openai/gpt-audio-mini`](openai/gpt-audio-mini.md) | GPT Audio Mini | 128,000 | no |  |
| [`openai/gpt-audio`](openai/gpt-audio.md) | GPT Audio | 128,000 | no |  |
| [`openai/gpt-chat-latest`](openai/gpt-chat-latest.md) | GPT Chat Latest | 400,000 | no |  |
| [`openai/gpt-image-1-mini`](openai/gpt-image-1-mini.md) | GPT Image 1 Mini | 400,000 | no |  |
| [`openai/gpt-image-1.5`](openai/gpt-image-1.5.md) | GPT Image 1.5 |  | no |  |
| [`openai/gpt-image-1`](openai/gpt-image-1.md) | GPT Image 1 | 400,000 | no |  |
| [`openai/gpt-image-2.5-flare`](openai/gpt-image-2.5-flare.md) | GPT Image 2.5 Flare | 400,000 | no |  |
| [`openai/gpt-image-2.5-sunburst`](openai/gpt-image-2.5-sunburst.md) | GPT Image 2.5 Sunburst | 400,000 | no |  |
| [`openai/gpt-image-2`](openai/gpt-image-2.md) | GPT Image 2 | 400,000 | no |  |
| [`openai/gpt-live-1`](openai/gpt-live-1.md) | GPT-Live 1 |  | no |  |
| [`openai/gpt-live-transcribe`](openai/gpt-live-transcribe.md) | GPT Live Transcribe |  | no |  |
| [`openai/gpt-oss-120b`](openai/gpt-oss-120b.md) | gpt-oss-120b | 131,072 | yes | 11.6 |
| [`openai/gpt-oss-20b`](openai/gpt-oss-20b.md) | gpt-oss-20b | 131,072 | yes | 9 |
| [`openai/gpt-oss-safeguard-120b`](openai/gpt-oss-safeguard-120b.md) | gpt-oss-safeguard-120b | 131,072 | yes |  |
| [`openai/gpt-oss-safeguard-20b`](openai/gpt-oss-safeguard-20b.md) | gpt-oss-safeguard-20b | 131,072 | yes |  |
| [`openai/gpt-realtime-1.5`](openai/gpt-realtime-1.5.md) | GPT Realtime 1.5 | 32,000 | no |  |
| [`openai/gpt-realtime-2.1-mini`](openai/gpt-realtime-2.1-mini.md) | GPT Realtime 2.1 Mini | 128,000 | no |  |
| [`openai/gpt-realtime-2.1`](openai/gpt-realtime-2.1.md) | GPT Realtime 2.1 | 128,000 | no |  |
| [`openai/gpt-realtime-2`](openai/gpt-realtime-2.md) | GPT Realtime 2 | 128,000 | no |  |
| [`openai/gpt-realtime-mini`](openai/gpt-realtime-mini.md) | GPT Realtime Mini | 32,000 | no |  |
| [`openai/gpt-realtime-translate`](openai/gpt-realtime-translate.md) | GPT Realtime Translate | 16,000 | no |  |
| [`openai/gpt-realtime-whisper`](openai/gpt-realtime-whisper.md) | GPT Realtime Whisper | 16,000 | no |  |
| [`openai/gpt-realtime`](openai/gpt-realtime.md) | GPT Realtime | 32,000 | no |  |
| [`openai/gpt-rosalind-discovery`](openai/gpt-rosalind-discovery.md) | GPT-Rosalind Discovery |  | no |  |
| [`openai/gpt-rosalind-research`](openai/gpt-rosalind-research.md) | GPT-Rosalind |  | no |  |
| [`openai/gpt-transcribe`](openai/gpt-transcribe.md) | GPT Transcribe |  | no |  |
| [`openai/o1-mini`](openai/o1-mini.md) | o1-mini | 128,000 | no |  |
| [`openai/o1-preview`](openai/o1-preview.md) | o1 Preview | 128,000 | no |  |
| [`openai/o1-pro`](openai/o1-pro.md) | o1-pro | 200,000 | no |  |
| [`openai/o1`](openai/o1.md) | o1 | 200,000 | no |  |
| [`openai/o3-deep-research`](openai/o3-deep-research.md) | o3-deep-research | 200,000 | no |  |
| [`openai/o3-mini`](openai/o3-mini.md) | o3 Mini | 200,000 | no |  |
| [`openai/o3-pro`](openai/o3-pro.md) | o3 Pro | 200,000 | no |  |
| [`openai/o3`](openai/o3.md) | o3 | 200,000 | no |  |
| [`openai/o4-mini-deep-research`](openai/o4-mini-deep-research.md) | o4-mini-deep-research | 200,000 | no |  |
| [`openai/o4-mini`](openai/o4-mini.md) | o4 Mini | 200,000 | no |  |
| [`openai/omni-moderation-latest`](openai/omni-moderation-latest.md) | omni-moderation |  | no |  |
| [`openai/sora-2-pro`](openai/sora-2-pro.md) | Sora 2 Pro |  | no |  |
| [`openai/sora-2`](openai/sora-2.md) | Sora 2 |  | no |  |
| [`openai/text-ada-001`](openai/text-ada-001.md) | text-ada-001 | 2,049 | no |  |
| [`openai/text-babbage-001`](openai/text-babbage-001.md) | text-babbage-001 | 2,049 | no |  |
| [`openai/text-curie-001`](openai/text-curie-001.md) | text-curie-001 | 2,049 | no |  |
| [`openai/text-davinci-001`](openai/text-davinci-001.md) | text-davinci-001 |  | no |  |
| [`openai/text-davinci-002`](openai/text-davinci-002.md) | text-davinci-002 | 4,097 | no |  |
| [`openai/text-davinci-003`](openai/text-davinci-003.md) | text-davinci-003 | 4,097 | no |  |
| [`openai/text-davinci-edit-001`](openai/text-davinci-edit-001.md) | text-davinci-edit-001 |  | no |  |
| [`openai/text-embedding-3-large`](openai/text-embedding-3-large.md) | Text Embedding 3 Large | 8,192 | no |  |
| [`openai/text-embedding-3-small`](openai/text-embedding-3-small.md) | Text Embedding 3 Small | 8,192 | no |  |
| [`openai/text-embedding-ada-002`](openai/text-embedding-ada-002.md) | Text Embedding Ada 002 | 8,192 | no |  |
| [`openai/text-moderation-latest`](openai/text-moderation-latest.md) | text-moderation |  | no |  |
| [`openai/text-moderation-stable`](openai/text-moderation-stable.md) | text-moderation-stable |  | no |  |
| [`openai/text-search-ada-doc-001`](openai/text-search-ada-doc-001.md) | text-search-ada-doc-001 | 2,048 | no |  |
| [`openai/text-search-ada-query-001`](openai/text-search-ada-query-001.md) | text-search-ada-query-001 | 2,048 | no |  |
| [`openai/text-search-babbage-doc-001`](openai/text-search-babbage-doc-001.md) | text-search-babbage-doc-001 | 2,048 | no |  |
| [`openai/text-search-babbage-query-001`](openai/text-search-babbage-query-001.md) | text-search-babbage-query-001 | 2,048 | no |  |
| [`openai/text-search-curie-doc-001`](openai/text-search-curie-doc-001.md) | text-search-curie-doc-001 | 2,048 | no |  |
| [`openai/text-search-curie-query-001`](openai/text-search-curie-query-001.md) | text-search-curie-query-001 | 2,048 | no |  |
| [`openai/text-search-davinci-doc-001`](openai/text-search-davinci-doc-001.md) | text-search-davinci-doc-001 | 2,048 | no |  |
| [`openai/text-search-davinci-query-001`](openai/text-search-davinci-query-001.md) | text-search-davinci-query-001 | 2,048 | no |  |
| [`openai/text-similarity-ada-001`](openai/text-similarity-ada-001.md) | text-similarity-ada-001 | 2,048 | no |  |
| [`openai/text-similarity-babbage-001`](openai/text-similarity-babbage-001.md) | text-similarity-babbage-001 | 2,048 | no |  |
| [`openai/text-similarity-curie-001`](openai/text-similarity-curie-001.md) | text-similarity-curie-001 | 2,048 | no |  |
| [`openai/text-similarity-davinci-001`](openai/text-similarity-davinci-001.md) | text-similarity-davinci-001 | 2,048 | no |  |
| [`openai/tts-1-hd`](openai/tts-1-hd.md) | TTS-1 HD |  | no |  |
| [`openai/tts-1`](openai/tts-1.md) | TTS-1 |  | no |  |
| [`openai/whisper-1`](openai/whisper-1.md) | Whisper 1 |  | yes |  |
| [`openai/whisper-large-v3-turbo`](openai/whisper-large-v3-turbo.md) | Whisper Large V3 Turbo |  | yes |  |
| [`openai/whisper-large-v3`](openai/whisper-large-v3.md) | Whisper Large V3 |  | yes |  |
| [`z-ai/autoglm-phone-9b-multilingual`](z-ai/autoglm-phone-9b-multilingual.md) | AutoGLM-Phone-9B-Multilingual | 65,536 | yes |  |
| [`z-ai/autoglm-phone-9b`](z-ai/autoglm-phone-9b.md) | AutoGLM-Phone-9B | 65,536 | yes |  |
| [`z-ai/cogvideox-3`](z-ai/cogvideox-3.md) | CogVideoX-3 |  | no |  |
| [`z-ai/cogview4-6b`](z-ai/cogview4-6b.md) | CogView4-6B |  | yes |  |
| [`z-ai/glm-4-32b-0414`](z-ai/glm-4-32b-0414.md) | GLM-4-32B-0414 | 32,768 | yes |  |
| [`z-ai/glm-4.1v-9b-thinking`](z-ai/glm-4.1v-9b-thinking.md) | GLM-4.1V-9B-Thinking | 65,536 | yes |  |
| [`z-ai/glm-4.5-air`](z-ai/glm-4.5-air.md) | GLM 4.5 Air | 131,072 | yes | 11.1 |
| [`z-ai/glm-4.5-flash`](z-ai/glm-4.5-flash.md) | GLM-4.5-Flash |  | not stated |  |
| [`z-ai/glm-4.5`](z-ai/glm-4.5.md) | GLM 4.5 | 131,072 | yes |  |
| [`z-ai/glm-4.5v`](z-ai/glm-4.5v.md) | GLM 4.5V | 65,536 | yes |  |
| [`z-ai/glm-4.6`](z-ai/glm-4.6.md) | GLM 4.6 | 204,800 | yes | 18.5 |
| [`z-ai/glm-4.6v-flash`](z-ai/glm-4.6v-flash.md) | GLM-4.6V-Flash | 131,072 | yes |  |
| [`z-ai/glm-4.6v`](z-ai/glm-4.6v.md) | GLM 4.6V | 131,072 | yes | 11.2 |
| [`z-ai/glm-4.7-flash`](z-ai/glm-4.7-flash.md) | GLM 4.7 Flash | 200,000 | yes | 14.9 |
| [`z-ai/glm-4.7`](z-ai/glm-4.7.md) | GLM 4.7 | 204,800 | yes | 22.2 |
| [`z-ai/glm-5-turbo`](z-ai/glm-5-turbo.md) | GLM 5 Turbo | 202,752 | no | 26.6 |
| [`z-ai/glm-5.1`](z-ai/glm-5.1.md) | GLM 5.1 | 204,800 | yes | 26.1 |
| [`z-ai/glm-5.2`](z-ai/glm-5.2.md) | GLM 5.2 | 1,048,576 | yes | 33.7 |
| [`z-ai/glm-5.3-flash`](z-ai/glm-5.3-flash.md) | GLM 5.3 Flash | 1,048,576 | yes | 41.8 |
| [`z-ai/glm-5.3-flashx-legal`](z-ai/glm-5.3-flashx-legal.md) | GLM-5.3-FlashX-Legal |  | no |  |
| [`z-ai/glm-5.3-flashx`](z-ai/glm-5.3-flashx.md) | GLM 5.3 FlashX | 1,048,576 | not stated |  |
| [`z-ai/glm-5.3-prime`](z-ai/glm-5.3-prime.md) | GLM 5.3 Prime | 1,000,000 | not stated |  |
| [`z-ai/glm-5.3`](z-ai/glm-5.3.md) | GLM 5.3 | 1,048,576 | yes | 44.8 |
| [`z-ai/glm-5`](z-ai/glm-5.md) | GLM 5 | 204,800 | yes | 27.9 |
| [`z-ai/glm-5v-turbo`](z-ai/glm-5v-turbo.md) | GLM 5V Turbo | 202,752 | no | 23.5 |
| [`z-ai/glm-asr-2512`](z-ai/glm-asr-2512.md) | GLM-ASR-2512 |  | no |  |
| [`z-ai/glm-asr-nano-2512`](z-ai/glm-asr-nano-2512.md) | GLM-ASR-Nano-2512 |  | yes |  |
| [`z-ai/glm-image`](z-ai/glm-image.md) | GLM-Image |  | yes |  |
| [`z-ai/glm-ocr`](z-ai/glm-ocr.md) | GLM-OCR | 131,072 | yes |  |
| [`z-ai/glm-tts`](z-ai/glm-tts.md) | GLM-TTS |  | yes |  |
| [`z-ai/glyph`](z-ai/glyph.md) | Glyph | 131,072 | yes |  |
| [`z-ai/scail-2`](z-ai/scail-2.md) | SCAIL-2 |  | yes |  |
| [`moonshotai/kimi-audio-7b-instruct`](moonshotai/kimi-audio-7b-instruct.md) | Kimi-Audio-7B-Instruct | 8,192 | yes |  |
| [`moonshotai/kimi-dev-72b`](moonshotai/kimi-dev-72b.md) | Kimi-Dev-72B | 131,072 | yes |  |
| [`moonshotai/kimi-k2-0905`](moonshotai/kimi-k2-0905.md) | Kimi K2 0905 | 262,144 | yes |  |
| [`moonshotai/kimi-k2-thinking`](moonshotai/kimi-k2-thinking.md) | Kimi K2 Thinking | 262,144 | yes | 22 |
| [`moonshotai/kimi-k2.5`](moonshotai/kimi-k2.5.md) | Kimi K2.5 | 262,144 | yes | 23.5 |
| [`moonshotai/kimi-k2.6`](moonshotai/kimi-k2.6.md) | Kimi K2.6 | 262,144 | yes | 27 |
| [`moonshotai/kimi-k2.7-code`](moonshotai/kimi-k2.7-code.md) | Kimi K2.7 Code | 262,144 | yes | 25.8 |
| [`moonshotai/kimi-k2`](moonshotai/kimi-k2.md) | Kimi K2 0711 | 131,072 | yes |  |
| [`moonshotai/kimi-k3.1-pro`](moonshotai/kimi-k3.1-pro.md) | Kimi K3.1 Pro | 1,048,576 | no | 46 |
| [`moonshotai/kimi-k3`](moonshotai/kimi-k3.md) | Kimi K3 | 1,048,576 | yes | 43.6 |
| [`moonshotai/kimi-linear-48b-a3b-instruct`](moonshotai/kimi-linear-48b-a3b-instruct.md) | Kimi Linear 48B A3B Instruct | 1,048,576 | yes |  |
| [`moonshotai/kimi-vl-a3b-instruct`](moonshotai/kimi-vl-a3b-instruct.md) | Kimi-VL-A3B-Instruct | 131,072 | yes |  |
| [`moonshotai/kimi-vl-a3b-thinking-2506`](moonshotai/kimi-vl-a3b-thinking-2506.md) | Kimi-VL-A3B-Thinking-2506 | 131,072 | yes |  |
| [`moonshotai/moonlight-16b-a3b-instruct`](moonshotai/moonlight-16b-a3b-instruct.md) | Moonlight-16B-A3B-Instruct | 8,192 | yes |  |
| [`minimax/hailuo-2.3`](minimax/hailuo-2.3.md) | MiniMax Hailuo 2.3 |  | no |  |
| [`minimax/hailuo-3-max`](minimax/hailuo-3-max.md) | MiniMax H3 Max |  | no |  |
| [`minimax/hailuo-3`](minimax/hailuo-3.md) | MiniMax H3 |  | yes |  |
| [`minimax/image-01`](minimax/image-01.md) | MiniMax Image-01 |  | no |  |
| [`minimax/minimax-01`](minimax/minimax-01.md) | MiniMax-01 | 1,000,192 | yes |  |
| [`minimax/minimax-h3-highspeed`](minimax/minimax-h3-highspeed.md) | MiniMax H3 Highspeed |  | no |  |
| [`minimax/minimax-h3-lite`](minimax/minimax-h3-lite.md) | MiniMax H3 Lite |  | no |  |
| [`minimax/minimax-hailuo-02`](minimax/minimax-hailuo-02.md) | MiniMax Hailuo 02 |  | no |  |
| [`minimax/minimax-hailuo-2.3-fast`](minimax/minimax-hailuo-2.3-fast.md) | MiniMax Hailuo 2.3 Fast |  | no |  |
| [`minimax/minimax-m1`](minimax/minimax-m1.md) | MiniMax M1 | 1,000,000 | yes |  |
| [`minimax/minimax-m2-her`](minimax/minimax-m2-her.md) | MiniMax M2-her | 65,536 | not stated |  |
| [`minimax/minimax-m2.1`](minimax/minimax-m2.1.md) | MiniMax M2.1 | 204,800 | yes |  |
| [`minimax/minimax-m2.5`](minimax/minimax-m2.5.md) | MiniMax M2.5 | 204,800 | yes |  |
| [`minimax/minimax-m2.7`](minimax/minimax-m2.7.md) | MiniMax M2.7 | 204,800 | yes |  |
| [`minimax/minimax-m2`](minimax/minimax-m2.md) | MiniMax M2 | 204,800 | yes |  |
| [`minimax/minimax-m3.1-flash`](minimax/minimax-m3.1-flash.md) | MiniMax M3.1 Flash | 1,048,576 | yes | 28.9 |
| [`minimax/minimax-m3`](minimax/minimax-m3.md) | MiniMax M3 | 1,048,576 | yes | 18.7 |
| [`minimax/minimax-music3`](minimax/minimax-music3.md) | MiniMax Music 3 |  | yes |  |
| [`minimax/minimax-vl-01`](minimax/minimax-vl-01.md) | MiniMax-VL-01 |  | yes |  |
| [`minimax/speech-02-hd`](minimax/speech-02-hd.md) | MiniMax Speech-02 HD |  | no |  |
| [`minimax/speech-02-turbo`](minimax/speech-02-turbo.md) | MiniMax Speech-02 Turbo |  | no |  |
| [`minimax/speech-2.6-hd`](minimax/speech-2.6-hd.md) | MiniMax Speech 2.6 HD |  | no |  |
| [`minimax/speech-2.6-turbo`](minimax/speech-2.6-turbo.md) | MiniMax Speech 2.6 Turbo |  | no |  |
| [`minimax/speech-2.8-hd`](minimax/speech-2.8-hd.md) | MiniMax Speech 2.8 HD |  | no |  |
| [`minimax/speech-2.8-turbo`](minimax/speech-2.8-turbo.md) | MiniMax Speech 2.8 Turbo |  | no |  |
| [`mistralai/codestral-2508`](mistralai/codestral-2508.md) | Codestral 2508 | 256,000 | no |  |
| [`mistralai/codestral-embed-2505`](mistralai/codestral-embed-2505.md) | Codestral Embed 2505 | 8,192 | no |  |
| [`mistralai/devstral-2512`](mistralai/devstral-2512.md) | Devstral 2 2512 | 262,144 | yes | 8.6 |
| [`mistralai/devstral-medium-2507`](mistralai/devstral-medium-2507.md) | Devstral Medium | 128,000 | no |  |
| [`mistralai/devstral-small-2-24b-instruct-2512`](mistralai/devstral-small-2-24b-instruct-2512.md) | Devstral Small 2 | 262,144 | yes |  |
| [`mistralai/magistral-medium-2509`](mistralai/magistral-medium-2509.md) | Magistral Medium 1.2 | 128,000 | no |  |
| [`mistralai/magistral-small-2509`](mistralai/magistral-small-2509.md) | Magistral Small 1.2 | 131,072 | yes |  |
| [`mistralai/ministral-14b-2512`](mistralai/ministral-14b-2512.md) | Ministral 3 14B 2512 | 262,144 | yes | 6 |
| [`mistralai/ministral-3b-2512`](mistralai/ministral-3b-2512.md) | Ministral 3 3B 2512 | 131,072 | yes | 4.8 |
| [`mistralai/ministral-8b-2512`](mistralai/ministral-8b-2512.md) | Ministral 3 8B 2512 | 262,144 | yes | 5.5 |
| [`mistralai/mistral-7b-instruct-v0.3`](mistralai/mistral-7b-instruct-v0.3.md) | Mistral 7B Instruct v0.3 | 32,768 | yes |  |
| [`mistralai/mistral-embed-2312`](mistralai/mistral-embed-2312.md) | Mistral Embed 2312 | 8,192 | no |  |
| [`mistralai/mistral-large-2407`](mistralai/mistral-large-2407.md) | Mistral Large 2407 | 131,072 | yes |  |
| [`mistralai/mistral-large-2512`](mistralai/mistral-large-2512.md) | Mistral Large 3 2512 | 262,144 | yes | 9.3 |
| [`mistralai/mistral-large-4-0`](mistralai/mistral-large-4-0.md) | Mistral Large 4 | 1,048,576 | not stated | 38.4 |
| [`mistralai/mistral-large`](mistralai/mistral-large.md) | Mistral Large | 128,000 | yes |  |
| [`mistralai/mistral-medium-3-5`](mistralai/mistral-medium-3-5.md) | Mistral Medium 3.5 | 262,144 | yes | 14.2 |
| [`mistralai/mistral-medium-3.1`](mistralai/mistral-medium-3.1.md) | Mistral Medium 3.1 | 131,072 | no |  |
| [`mistralai/mistral-medium-3`](mistralai/mistral-medium-3.md) | Mistral Medium 3 | 131,072 | no |  |
| [`mistralai/mistral-moderation-2603`](mistralai/mistral-moderation-2603.md) | Mistral Moderation 2 | 128,000 | no |  |
| [`mistralai/mistral-nemo`](mistralai/mistral-nemo.md) | Mistral Nemo | 131,072 | yes |  |
| [`mistralai/mistral-ocr-2512`](mistralai/mistral-ocr-2512.md) | Mistral OCR 3 |  | no |  |
| [`mistralai/mistral-ocr-4-1`](mistralai/mistral-ocr-4-1.md) | Mistral OCR 4.1 |  | no |  |
| [`mistralai/mistral-saba`](mistralai/mistral-saba.md) | Mistral Saba | 32,768 | no |  |
| [`mistralai/mistral-small-24b-instruct-2501`](mistralai/mistral-small-24b-instruct-2501.md) | Mistral Small 3 | 32,768 | yes |  |
| [`mistralai/mistral-small-2603`](mistralai/mistral-small-2603.md) | Mistral Small 4 | 262,144 | yes | 11.3 |
| [`mistralai/mistral-small-3.1-24b-instruct`](mistralai/mistral-small-3.1-24b-instruct.md) | Mistral Small 3.1 24B | 128,000 | yes |  |
| [`mistralai/mistral-small-3.2-24b-instruct`](mistralai/mistral-small-3.2-24b-instruct.md) | Mistral Small 3.2 24B | 256,000 | yes | 8.2 |
| [`mistralai/mixtral-8x22b-instruct`](mistralai/mixtral-8x22b-instruct.md) | Mixtral 8x22B Instruct | 65,536 | yes |  |
| [`mistralai/mixtral-8x7b-instruct-v0.1`](mistralai/mixtral-8x7b-instruct-v0.1.md) | Mixtral 8x7B Instruct | 32,768 | yes |  |
| [`mistralai/pixtral-12b-2409`](mistralai/pixtral-12b-2409.md) | Pixtral 12B | 131,072 | yes |  |
| [`mistralai/pixtral-large-instruct-2411`](mistralai/pixtral-large-instruct-2411.md) | Pixtral Large | 131,072 | yes |  |
| [`mistralai/shieldstral-1.0-3b`](mistralai/shieldstral-1.0-3b.md) | Shieldstral 1.0 3B | 32,768 | yes |  |
| [`mistralai/voxtral-4b-tts-2603`](mistralai/voxtral-4b-tts-2603.md) | Voxtral 4B TTS 2603 |  | yes |  |
| [`mistralai/voxtral-mini-2602`](mistralai/voxtral-mini-2602.md) | Voxtral Mini Transcribe 2 |  | no |  |
| [`mistralai/voxtral-mini-3b-2507`](mistralai/voxtral-mini-3b-2507.md) | Voxtral Mini 3B 2507 | 32,768 | yes |  |
| [`mistralai/voxtral-mini-4b-realtime-2602`](mistralai/voxtral-mini-4b-realtime-2602.md) | Voxtral Mini 4B Realtime 2602 | 131,072 | yes |  |
| [`mistralai/voxtral-mini-4b-realtime-arabic`](mistralai/voxtral-mini-4b-realtime-arabic.md) | Voxtral Mini 4B Realtime Arabic | 131,072 | yes |  |
| [`mistralai/voxtral-mini-transcribe-3-0`](mistralai/voxtral-mini-transcribe-3-0.md) | Voxtral Mini Transcribe 3 | 65,536 | no |  |
| [`mistralai/voxtral-mini-transcribe-realtime-3-0`](mistralai/voxtral-mini-transcribe-realtime-3-0.md) | Voxtral Mini Transcribe Realtime 3 |  | no |  |
| [`mistralai/voxtral-mini-tts-3-0`](mistralai/voxtral-mini-tts-3-0.md) | Voxtral TTS 3 | 4,096 | no |  |
| [`mistralai/voxtral-small-24b-2507`](mistralai/voxtral-small-24b-2507.md) | Voxtral Small 24B 2507 | 32,768 | yes |  |
| [`mistralai/voxtral-small-transcribe-3-0`](mistralai/voxtral-small-transcribe-3-0.md) | Voxtral Small Transcribe 3 | 65,536 | no |  |
| [`meta-llama/codellama-13b-instruct`](meta-llama/codellama-13b-instruct.md) | Code Llama 13B Instruct | 16,384 | yes |  |
| [`meta-llama/codellama-34b-instruct`](meta-llama/codellama-34b-instruct.md) | Code Llama 34B Instruct | 16,384 | yes |  |
| [`meta-llama/codellama-70b-instruct`](meta-llama/codellama-70b-instruct.md) | Code Llama 70B Instruct |  | yes |  |
| [`meta-llama/codellama-7b-instruct`](meta-llama/codellama-7b-instruct.md) | Code Llama 7B Instruct | 16,384 | yes |  |
| [`meta-llama/llama-2-13b-chat`](meta-llama/llama-2-13b-chat.md) | Llama 2 13B Chat | 4,096 | yes |  |
| [`meta-llama/llama-2-70b-chat`](meta-llama/llama-2-70b-chat.md) | Llama 2 70B Chat | 4,096 | yes |  |
| [`meta-llama/llama-2-7b-chat`](meta-llama/llama-2-7b-chat.md) | Llama 2 7B Chat | 4,096 | yes |  |
| [`meta-llama/llama-3-70b-instruct`](meta-llama/llama-3-70b-instruct.md) | Llama 3 70B Instruct | 8,192 | yes |  |
| [`meta-llama/llama-3-8b-instruct`](meta-llama/llama-3-8b-instruct.md) | Llama 3 8B Instruct | 8,192 | yes |  |
| [`meta-llama/llama-3.1-405b-instruct`](meta-llama/llama-3.1-405b-instruct.md) | Llama 3.1 405B Instruct | 128,000 | yes |  |
| [`meta-llama/llama-3.1-70b-instruct`](meta-llama/llama-3.1-70b-instruct.md) | Llama 3.1 70B Instruct | 131,072 | yes |  |
| [`meta-llama/llama-3.1-8b-instruct`](meta-llama/llama-3.1-8b-instruct.md) | Llama 3.1 8B Instruct | 131,072 | yes | 6.9 |
| [`meta-llama/llama-3.2-11b-vision-instruct`](meta-llama/llama-3.2-11b-vision-instruct.md) | Llama 3.2 11B Vision Instruct | 128,000 | yes |  |
| [`meta-llama/llama-3.2-1b-instruct`](meta-llama/llama-3.2-1b-instruct.md) | Llama 3.2 1B Instruct | 60,000 | yes |  |
| [`meta-llama/llama-3.2-3b-instruct`](meta-llama/llama-3.2-3b-instruct.md) | Llama 3.2 3B Instruct | 131,072 | yes |  |
| [`meta-llama/llama-3.2-90b-vision-instruct`](meta-llama/llama-3.2-90b-vision-instruct.md) | Llama 3.2 90B Vision Instruct | 128,000 | yes |  |
| [`meta-llama/llama-3.3-70b-instruct`](meta-llama/llama-3.3-70b-instruct.md) | Llama 3.3 70B Instruct | 131,072 | yes | 7.7 |
| [`meta-llama/llama-4-maverick`](meta-llama/llama-4-maverick.md) | Llama 4 Maverick | 1,048,576 | yes | 10 |
| [`meta-llama/llama-4-scout`](meta-llama/llama-4-scout.md) | Llama 4 Scout | 1,310,720 | yes | 8.1 |
| [`meta-llama/llama-guard-2-8b`](meta-llama/llama-guard-2-8b.md) | Llama Guard 2 8B |  | yes |  |
| [`meta-llama/llama-guard-3-11b-vision`](meta-llama/llama-guard-3-11b-vision.md) | Llama Guard 3 11B Vision |  | yes |  |
| [`meta-llama/llama-guard-3-1b`](meta-llama/llama-guard-3-1b.md) | Llama Guard 3 1B |  | yes |  |
| [`meta-llama/llama-guard-3-8b`](meta-llama/llama-guard-3-8b.md) | Llama Guard 3 8B |  | yes |  |
| [`meta-llama/llama-guard-4-12b`](meta-llama/llama-guard-4-12b.md) | Llama Guard 4 12B | 163,840 | yes |  |
| [`meta-llama/llama-prompt-guard-2-22m`](meta-llama/llama-prompt-guard-2-22m.md) | Llama Prompt Guard 2 22M | 512 | yes |  |
| [`meta-llama/llama-prompt-guard-2-86m`](meta-llama/llama-prompt-guard-2-86m.md) | Llama Prompt Guard 2 86M | 512 | yes |  |
| [`meta-llama/llamaguard-7b`](meta-llama/llamaguard-7b.md) | Llama Guard 7B |  | yes |  |
| [`meta-llama/prompt-guard-86m`](meta-llama/prompt-guard-86m.md) | Prompt Guard 86M | 512 | yes |  |
| [`meta/muse-glimmer-30b`](meta/muse-glimmer-30b.md) | Muse Glimmer 30B | 131,072 | yes | 17.5 |
| [`meta/muse-image`](meta/muse-image.md) | Muse Image | 65,536 | no |  |
| [`meta/muse-spark-1.1`](meta/muse-spark-1.1.md) | Muse Spark 1.1 | 1,048,576 | no |  |
| [`meta/muse-spark-1.2-contributor`](meta/muse-spark-1.2-contributor.md) | Muse Spark 1.2 Contributor | 1,048,576 | no |  |
| [`meta/muse-spark-1.2`](meta/muse-spark-1.2.md) | Muse Spark 1.2 | 1,048,576 | no |  |
| [`meta/muse-spark-1.3-contributor`](meta/muse-spark-1.3-contributor.md) | Muse Spark 1.3 Contributor | 1,048,576 | no |  |
| [`meta/muse-spark-1.3`](meta/muse-spark-1.3.md) | Muse Spark 1.3 | 1,048,576 | no | 48.1 |
| [`meta/muse-spark-open`](meta/muse-spark-open.md) | Muse Spark Open | 1,048,576 | yes | 24.7 |
| [`meta/muse-voice-transcribe-1.0`](meta/muse-voice-transcribe-1.0.md) | Muse Voice Transcribe 1.0 |  | no |  |
| [`meta/muse-wonder`](meta/muse-wonder.md) | Muse Wonder | 1,048,576 | no | 52.4 |
| [`google/embeddinggemma-2`](google/embeddinggemma-2.md) | EmbeddingGemma 2 | 8,192 | yes |  |
| [`google/embeddinggemma-300m`](google/embeddinggemma-300m.md) | EmbeddingGemma 300M | 2,048 | yes |  |
| [`google/gemini-embedding-001`](google/gemini-embedding-001.md) | Gemini Embedding 001 | 20,000 | no |  |
| [`google/gemini-embedding-2`](google/gemini-embedding-2.md) | Gemini Embedding 2 | 8,192 | no |  |
| [`google/gemma-3-12b-it`](google/gemma-3-12b-it.md) | Gemma 3 12B | 131,072 | yes | 3.8 |
| [`google/gemma-3-27b-it`](google/gemma-3-27b-it.md) | Gemma 3 27B | 131,072 | yes | 4.9 |
| [`google/gemma-3-4b-it`](google/gemma-3-4b-it.md) | Gemma 3 4B | 131,072 | yes | 4.8 |
| [`google/gemma-4-12b-it`](google/gemma-4-12b-it.md) | Gemma 4 12B | 262,144 | yes | 14.2 |
| [`google/gemma-4-26b-a4b-it`](google/gemma-4-26b-a4b-it.md) | Gemma 4 26B A4B | 262,144 | yes | 16.7 |
| [`google/gemma-4-31b-it`](google/gemma-4-31b-it.md) | Gemma 4 31B | 262,144 | yes | 14.7 |
| [`google/gemma-4-e2b-it`](google/gemma-4-e2b-it.md) | Gemma 4 E2B | 128,000 | yes | 7.8 |
| [`google/gemma-4-e4b-it`](google/gemma-4-e4b-it.md) | Gemma 4 E4B | 128,000 | yes | 8.9 |
| [`google/translategemma-12b-it`](google/translategemma-12b-it.md) | TranslateGemma 12B | 2,048 | yes |  |
| [`google/translategemma-27b-it`](google/translategemma-27b-it.md) | TranslateGemma 27B | 2,048 | yes |  |
| [`google/translategemma-4b-it`](google/translategemma-4b-it.md) | TranslateGemma 4B | 2,048 | yes |  |
| [`deepseek/deepseek-chat-v3-0324`](deepseek/deepseek-chat-v3-0324.md) | DeepSeek V3 0324 | 163,840 | yes | 9.7 |
| [`deepseek/deepseek-chat-v3.1`](deepseek/deepseek-chat-v3.1.md) | DeepSeek V3.1 | 163,840 | yes | 13.5 |
| [`deepseek/deepseek-chat`](deepseek/deepseek-chat.md) | DeepSeek V3 | 163,840 | yes | 8.5 |
| [`deepseek/deepseek-ocr-2`](deepseek/deepseek-ocr-2.md) | DeepSeek-OCR 2 | 8,192 | yes |  |
| [`deepseek/deepseek-ocr`](deepseek/deepseek-ocr.md) | DeepSeek-OCR | 8,192 | yes |  |
| [`deepseek/deepseek-r1-0528`](deepseek/deepseek-r1-0528.md) | DeepSeek R1 0528 | 163,840 | yes | 13.1 |
| [`deepseek/deepseek-r1`](deepseek/deepseek-r1.md) | DeepSeek R1 | 64,000 | yes | 11.4 |
| [`deepseek/deepseek-v3.1-terminus`](deepseek/deepseek-v3.1-terminus.md) | DeepSeek V3.1 Terminus | 163,840 | yes | 14.8 |
| [`deepseek/deepseek-v3.2-exp`](deepseek/deepseek-v3.2-exp.md) | DeepSeek V3.2 Exp | 163,840 | yes | 16.6 |
| [`deepseek/deepseek-v3.2`](deepseek/deepseek-v3.2.md) | DeepSeek V3.2 | 163,840 | yes | 21.5 |
| [`deepseek/deepseek-v4-flash-0731`](deepseek/deepseek-v4-flash-0731.md) | DeepSeek V4 Flash 0731 | 1,048,576 | yes | 34.3 |
| [`deepseek/deepseek-v4-flash-vision-exp`](deepseek/deepseek-v4-flash-vision-exp.md) | DeepSeek V4 Flash Vision Exp | 1,048,576 | yes | 34.8 |
| [`deepseek/deepseek-v4-flash`](deepseek/deepseek-v4-flash.md) | DeepSeek V4 Flash 0423 | 1,048,576 | yes | 24.2 |
| [`deepseek/deepseek-v4-pro-0813`](deepseek/deepseek-v4-pro-0813.md) | DeepSeek V4 Pro 0813 | 1,048,576 | yes | 36 |
| [`deepseek/deepseek-v4-pro`](deepseek/deepseek-v4-pro.md) | DeepSeek V4 Pro 0423 | 1,048,576 | yes | 30.4 |
| [`deepseek/deepseek-v4.1-flash`](deepseek/deepseek-v4.1-flash.md) | DeepSeek V4.1 Flash | 1,048,576 | yes | 39.5 |
| [`qwen/qvq-72b-preview`](qwen/qvq-72b-preview.md) | QVQ 72B Preview | 128,000 | yes |  |
| [`qwen/qvq-max`](qwen/qvq-max.md) | QVQ-Max | 131,072 | no |  |
| [`qwen/qvq-plus`](qwen/qvq-plus.md) | QVQ-Plus |  | no |  |
| [`qwen/qwen-2.5-72b-instruct`](qwen/qwen-2.5-72b-instruct.md) | Qwen2.5 72B Instruct | 32,768 | yes | 7.7 |
| [`qwen/qwen-2.5-7b-instruct`](qwen/qwen-2.5-7b-instruct.md) | Qwen2.5 7B Instruct | 32,768 | yes |  |
| [`qwen/qwen-2.5-coder-32b-instruct`](qwen/qwen-2.5-coder-32b-instruct.md) | Qwen2.5 Coder 32B Instruct | 32,768 | yes | 6.7 |
| [`qwen/qwen-agentworld-35b-a3b`](qwen/qwen-agentworld-35b-a3b.md) | Qwen AgentWorld 35B A3B | 262,144 | yes |  |
| [`qwen/qwen-audio-3.0-asr-flash-filetrans`](qwen/qwen-audio-3.0-asr-flash-filetrans.md) | Qwen-Audio-3.0-ASR-Flash-Filetrans |  | no |  |
| [`qwen/qwen-audio-3.0-asr-flash-streaming`](qwen/qwen-audio-3.0-asr-flash-streaming.md) | Qwen-Audio-3.0-ASR-Flash-Streaming |  | no |  |
| [`qwen/qwen-audio-3.0-asr-flash`](qwen/qwen-audio-3.0-asr-flash.md) | Qwen-Audio-3.0-ASR-Flash |  | no |  |
| [`qwen/qwen-audio-3.0-realtime-flash`](qwen/qwen-audio-3.0-realtime-flash.md) | Qwen-Audio-3.0-Realtime-Flash | 40,960 | no |  |
| [`qwen/qwen-audio-3.0-realtime-plus`](qwen/qwen-audio-3.0-realtime-plus.md) | Qwen-Audio-3.0-Realtime-Plus | 40,960 | no |  |
| [`qwen/qwen-audio-3.0-tts-flash`](qwen/qwen-audio-3.0-tts-flash.md) | Qwen-Audio-3.0-TTS Flash |  | no |  |
| [`qwen/qwen-audio-3.0-tts-plus`](qwen/qwen-audio-3.0-tts-plus.md) | Qwen-Audio-3.0-TTS Plus |  | no |  |
| [`qwen/qwen-audio-3.1-asr-flash-filetrans`](qwen/qwen-audio-3.1-asr-flash-filetrans.md) | Qwen-Audio-3.1-ASR-Flash-Filetrans |  | no |  |
| [`qwen/qwen-audio-3.1-asr-flash-message`](qwen/qwen-audio-3.1-asr-flash-message.md) | Qwen-Audio-3.1-ASR-Flash-Message |  | no |  |
| [`qwen/qwen-audio-3.1-asr-flash-streaming`](qwen/qwen-audio-3.1-asr-flash-streaming.md) | Qwen-Audio-3.1-ASR-Flash-Streaming |  | no |  |
| [`qwen/qwen-audio-3.1-asr-flash`](qwen/qwen-audio-3.1-asr-flash.md) | Qwen-Audio-3.1-ASR-Flash |  | no |  |
| [`qwen/qwen-audio-3.1-realtime-flash`](qwen/qwen-audio-3.1-realtime-flash.md) | Qwen-Audio-3.1-Realtime-Flash | 262,144 | no |  |
| [`qwen/qwen-audio-3.1-realtime-plus`](qwen/qwen-audio-3.1-realtime-plus.md) | Qwen-Audio-3.1-Realtime-Plus | 262,144 | no |  |
| [`qwen/qwen-audio-3.1-tts-flash`](qwen/qwen-audio-3.1-tts-flash.md) | Qwen-Audio-3.1-TTS-Flash |  | no |  |
| [`qwen/qwen-audio-3.1-tts-next`](qwen/qwen-audio-3.1-tts-next.md) | Qwen-Audio-3.1-TTS-Next |  | no |  |
| [`qwen/qwen-audio-3.1-tts-plus`](qwen/qwen-audio-3.1-tts-plus.md) | Qwen-Audio-3.1-TTS-Plus |  | no |  |
| [`qwen/qwen-coder-plus`](qwen/qwen-coder-plus.md) | Qwen-Coder-Plus | 131,072 | no |  |
| [`qwen/qwen-coder-turbo`](qwen/qwen-coder-turbo.md) | Qwen-Coder-Turbo | 131,072 | no |  |
| [`qwen/qwen-deep-research`](qwen/qwen-deep-research.md) | Qwen-Deep-Research | 1,000,000 | no |  |
| [`qwen/qwen-doc-turbo`](qwen/qwen-doc-turbo.md) | Qwen-Doc-Turbo | 262,144 | no |  |
| [`qwen/qwen-drive-1.0-4b`](qwen/qwen-drive-1.0-4b.md) | Qwen Drive 1.0 4B | 32,768 | yes |  |
| [`qwen/qwen-flash-character`](qwen/qwen-flash-character.md) | Qwen-Flash-Character | 32,768 | no |  |
| [`qwen/qwen-flash`](qwen/qwen-flash.md) | Qwen-Flash | 1,000,000 | no |  |
| [`qwen/qwen-image-2.0-pro`](qwen/qwen-image-2.0-pro.md) | Qwen-Image-2.0-Pro |  | no |  |
| [`qwen/qwen-image-2.0`](qwen/qwen-image-2.0.md) | Qwen-Image-2.0 |  | no |  |
| [`qwen/qwen-image-2.1-pro`](qwen/qwen-image-2.1-pro.md) | Qwen Image 2.1 Pro | 65,536 | no |  |
| [`qwen/qwen-image-2.1-turbo`](qwen/qwen-image-2.1-turbo.md) | Qwen Image 2.1 Turbo | 65,536 | yes |  |
| [`qwen/qwen-image-2.1`](qwen/qwen-image-2.1.md) | Qwen-Image-2.1 |  | yes |  |
| [`qwen/qwen-image-2512`](qwen/qwen-image-2512.md) | Qwen-Image-2512 |  | yes |  |
| [`qwen/qwen-image-3-pro`](qwen/qwen-image-3-pro.md) | Qwen Image 3 Pro | 65,536 | no |  |
| [`qwen/qwen-image-3`](qwen/qwen-image-3.md) | Qwen Image 3 | 65,536 | no |  |
| [`qwen/qwen-image-bench`](qwen/qwen-image-bench.md) | Qwen Image Bench Q-Judger | 262,144 | yes |  |
| [`qwen/qwen-image-edit-2509`](qwen/qwen-image-edit-2509.md) | Qwen-Image-Edit-2509 |  | yes |  |
| [`qwen/qwen-image-edit-2511`](qwen/qwen-image-edit-2511.md) | Qwen-Image-Edit-2511 |  | yes |  |
| [`qwen/qwen-image-edit-max`](qwen/qwen-image-edit-max.md) | Qwen-Image-Edit-Max |  | no |  |
| [`qwen/qwen-image-edit-plus`](qwen/qwen-image-edit-plus.md) | Qwen-Image-Edit-Plus |  | no |  |
| [`qwen/qwen-image-edit`](qwen/qwen-image-edit.md) | Qwen-Image-Edit |  | yes |  |
| [`qwen/qwen-image-layered`](qwen/qwen-image-layered.md) | Qwen-Image-Layered |  | yes |  |
| [`qwen/qwen-image-max`](qwen/qwen-image-max.md) | Qwen-Image-Max |  | no |  |
| [`qwen/qwen-image-plus-2026-01-09`](qwen/qwen-image-plus-2026-01-09.md) | Qwen-Image-Plus 2026-01-09 |  | no |  |
| [`qwen/qwen-image`](qwen/qwen-image.md) | Qwen-Image |  | yes |  |
| [`qwen/qwen-long`](qwen/qwen-long.md) | Qwen-Long | 10,000,000 | no |  |
| [`qwen/qwen-math-plus`](qwen/qwen-math-plus.md) | Qwen-Math-Plus | 4,096 | no |  |
| [`qwen/qwen-math-turbo`](qwen/qwen-math-turbo.md) | Qwen-Math-Turbo |  | no |  |
| [`qwen/qwen-max`](qwen/qwen-max.md) | Qwen-Max | 32,768 | no |  |
| [`qwen/qwen-mt-flash`](qwen/qwen-mt-flash.md) | Qwen-MT-Flash | 16,384 | no |  |
| [`qwen/qwen-mt-image-2.0`](qwen/qwen-mt-image-2.0.md) | Qwen-MT-Image-2.0 |  | no |  |
| [`qwen/qwen-mt-image`](qwen/qwen-mt-image.md) | Qwen-MT-Image |  | no |  |
| [`qwen/qwen-mt-lite`](qwen/qwen-mt-lite.md) | Qwen-MT-Lite | 16,384 | no |  |
| [`qwen/qwen-mt-plus`](qwen/qwen-mt-plus.md) | Qwen-MT-Plus | 16,384 | no |  |
| [`qwen/qwen-mt-turbo`](qwen/qwen-mt-turbo.md) | Qwen-MT-Turbo |  | no |  |
| [`qwen/qwen-omni-turbo-realtime`](qwen/qwen-omni-turbo-realtime.md) | Qwen-Omni-Turbo-Realtime | 32,768 | no |  |
| [`qwen/qwen-omni-turbo`](qwen/qwen-omni-turbo.md) | Qwen-Omni-Turbo | 32,768 | no |  |
| [`qwen/qwen-plus-character-ja`](qwen/qwen-plus-character-ja.md) | Qwen-Plus-Character-JA | 8,192 | no |  |
| [`qwen/qwen-plus-character`](qwen/qwen-plus-character.md) | Qwen-Plus-Character | 131,072 | no |  |
| [`qwen/qwen-plus`](qwen/qwen-plus.md) | Qwen-Plus | 1,000,000 | no |  |
| [`qwen/qwen-tts-realtime`](qwen/qwen-tts-realtime.md) | Qwen-TTS-Realtime | 8,192 | no |  |
| [`qwen/qwen-tts`](qwen/qwen-tts.md) | Qwen-TTS | 8,192 | no |  |
| [`qwen/qwen-turbo`](qwen/qwen-turbo.md) | Qwen-Turbo | 1,000,000 | no |  |
| [`qwen/qwen-vl-max`](qwen/qwen-vl-max.md) | Qwen-VL-Max | 131,072 | no |  |
| [`qwen/qwen-vl-ocr`](qwen/qwen-vl-ocr.md) | Qwen-VL-OCR | 38,192 | no |  |
| [`qwen/qwen-vl-plus`](qwen/qwen-vl-plus.md) | Qwen-VL-Plus | 131,072 | no |  |
| [`qwen/qwen2.5-0.5b-instruct`](qwen/qwen2.5-0.5b-instruct.md) | Qwen2.5 0.5B Instruct | 32,768 | yes |  |
| [`qwen/qwen2.5-1.5b-instruct`](qwen/qwen2.5-1.5b-instruct.md) | Qwen2.5 1.5B Instruct | 32,768 | yes |  |
| [`qwen/qwen2.5-14b-instruct-1m`](qwen/qwen2.5-14b-instruct-1m.md) | Qwen2.5 14B Instruct 1M | 1,010,000 | yes |  |
| [`qwen/qwen2.5-14b-instruct`](qwen/qwen2.5-14b-instruct.md) | Qwen2.5 14B Instruct | 32,768 | yes |  |
| [`qwen/qwen2.5-32b-instruct`](qwen/qwen2.5-32b-instruct.md) | Qwen2.5 32B Instruct | 32,768 | yes |  |
| [`qwen/qwen2.5-3b-instruct`](qwen/qwen2.5-3b-instruct.md) | Qwen2.5 3B Instruct | 32,768 | yes |  |
| [`qwen/qwen2.5-7b-instruct-1m`](qwen/qwen2.5-7b-instruct-1m.md) | Qwen2.5 7B Instruct 1M | 1,010,000 | yes |  |
| [`qwen/qwen2.5-coder-0.5b-instruct`](qwen/qwen2.5-coder-0.5b-instruct.md) | Qwen2.5 Coder 0.5B Instruct | 32,768 | yes |  |
| [`qwen/qwen2.5-coder-1.5b-instruct`](qwen/qwen2.5-coder-1.5b-instruct.md) | Qwen2.5 Coder 1.5B Instruct | 32,768 | yes |  |
| [`qwen/qwen2.5-coder-14b-instruct`](qwen/qwen2.5-coder-14b-instruct.md) | Qwen2.5 Coder 14B Instruct | 32,768 | yes |  |
| [`qwen/qwen2.5-coder-3b-instruct`](qwen/qwen2.5-coder-3b-instruct.md) | Qwen2.5 Coder 3B Instruct | 32,768 | yes |  |
| [`qwen/qwen2.5-coder-7b-instruct`](qwen/qwen2.5-coder-7b-instruct.md) | Qwen2.5 Coder 7B Instruct | 32,768 | yes |  |
| [`qwen/qwen2.5-math-1.5b-instruct`](qwen/qwen2.5-math-1.5b-instruct.md) | Qwen2.5 Math 1.5B Instruct | 4,096 | yes |  |
| [`qwen/qwen2.5-math-72b-instruct`](qwen/qwen2.5-math-72b-instruct.md) | Qwen2.5 Math 72B Instruct | 4,096 | yes |  |
| [`qwen/qwen2.5-math-7b-instruct`](qwen/qwen2.5-math-7b-instruct.md) | Qwen2.5 Math 7B Instruct | 4,096 | yes |  |
| [`qwen/qwen2.5-omni-3b`](qwen/qwen2.5-omni-3b.md) | Qwen2.5 Omni 3B | 32,768 | yes |  |
| [`qwen/qwen2.5-omni-7b`](qwen/qwen2.5-omni-7b.md) | Qwen2.5 Omni 7B | 32,768 | yes |  |
| [`qwen/qwen2.5-vl-32b-instruct`](qwen/qwen2.5-vl-32b-instruct.md) | Qwen2.5 VL 32B Instruct | 128,000 | yes |  |
| [`qwen/qwen2.5-vl-3b-instruct`](qwen/qwen2.5-vl-3b-instruct.md) | Qwen2.5 VL 3B Instruct | 128,000 | yes |  |
| [`qwen/qwen2.5-vl-72b-instruct`](qwen/qwen2.5-vl-72b-instruct.md) | Qwen2.5 VL 72B Instruct | 128,000 | yes |  |
| [`qwen/qwen2.5-vl-7b-instruct`](qwen/qwen2.5-vl-7b-instruct.md) | Qwen2.5 VL 7B Instruct | 128,000 | yes |  |
| [`qwen/qwen3-0.6b`](qwen/qwen3-0.6b.md) | Qwen3 0.6B | 40,960 | yes |  |
| [`qwen/qwen3-1.7b`](qwen/qwen3-1.7b.md) | Qwen3 1.7B | 40,960 | yes |  |
| [`qwen/qwen3-14b`](qwen/qwen3-14b.md) | Qwen3 14B | 40,960 | yes | 6.4 |
| [`qwen/qwen3-235b-a22b-2507`](qwen/qwen3-235b-a22b-2507.md) | Qwen3 235B A22B Instruct 2507 | 262,144 | yes | 12 |
| [`qwen/qwen3-235b-a22b-thinking-2507`](qwen/qwen3-235b-a22b-thinking-2507.md) | Qwen3 235B A22B Thinking 2507 | 128,000 | yes | 12.7 |
| [`qwen/qwen3-235b-a22b`](qwen/qwen3-235b-a22b.md) | Qwen3 235B A22B | 40,960 | yes |  |
| [`qwen/qwen3-30b-a3b-instruct-2507`](qwen/qwen3-30b-a3b-instruct-2507.md) | Qwen3 30B A3B Instruct 2507 | 262,144 | yes | 7.5 |
| [`qwen/qwen3-30b-a3b-thinking-2507`](qwen/qwen3-30b-a3b-thinking-2507.md) | Qwen3 30B A3B Thinking 2507 | 262,144 | yes |  |
| [`qwen/qwen3-30b-a3b`](qwen/qwen3-30b-a3b.md) | Qwen3 30B A3B | 40,960 | yes | 7.6 |
| [`qwen/qwen3-32b`](qwen/qwen3-32b.md) | Qwen3 32B | 131,072 | yes | 7.2 |
| [`qwen/qwen3-4b-instruct-2507`](qwen/qwen3-4b-instruct-2507.md) | Qwen3 4B Instruct 2507 | 262,144 | yes |  |
| [`qwen/qwen3-4b-saferl`](qwen/qwen3-4b-saferl.md) | Qwen3 4B SafeRL | 40,960 | yes |  |
| [`qwen/qwen3-4b-thinking-2507`](qwen/qwen3-4b-thinking-2507.md) | Qwen3 4B Thinking 2507 | 262,144 | yes |  |
| [`qwen/qwen3-4b`](qwen/qwen3-4b.md) | Qwen3 4B | 40,960 | yes |  |
| [`qwen/qwen3-8b`](qwen/qwen3-8b.md) | Qwen3 8B | 40,960 | yes |  |
| [`qwen/qwen3-asr-0.6b`](qwen/qwen3-asr-0.6b.md) | Qwen3 ASR 0.6B |  | yes |  |
| [`qwen/qwen3-asr-1.7b`](qwen/qwen3-asr-1.7b.md) | Qwen3 ASR 1.7B |  | yes |  |
| [`qwen/qwen3-asr-flash-filetrans`](qwen/qwen3-asr-flash-filetrans.md) | Qwen3-ASR-Flash-Filetrans |  | no |  |
| [`qwen/qwen3-asr-flash-realtime`](qwen/qwen3-asr-flash-realtime.md) | Qwen3-ASR-Flash-Realtime |  | no |  |
| [`qwen/qwen3-asr-flash`](qwen/qwen3-asr-flash.md) | Qwen3-ASR-Flash |  | no |  |
| [`qwen/qwen3-coder-30b-a3b-instruct`](qwen/qwen3-coder-30b-a3b-instruct.md) | Qwen3 Coder 30B A3B Instruct | 262,144 | yes | 9.6 |
| [`qwen/qwen3-coder-flash`](qwen/qwen3-coder-flash.md) | Qwen3 Coder Flash | 1,000,000 | no |  |
| [`qwen/qwen3-coder-next`](qwen/qwen3-coder-next.md) | Qwen3 Coder Next | 262,144 | yes | 9.2 |
| [`qwen/qwen3-coder-plus`](qwen/qwen3-coder-plus.md) | Qwen3-Coder-Plus | 1,000,000 | no |  |
| [`qwen/qwen3-coder`](qwen/qwen3-coder.md) | Qwen3 Coder 480B A35B | 262,144 | yes | 11.9 |
| [`qwen/qwen3-embedding-0.6b`](qwen/qwen3-embedding-0.6b.md) | Qwen3 Embedding 0.6B | 32,768 | yes |  |
| [`qwen/qwen3-embedding-4b`](qwen/qwen3-embedding-4b.md) | Qwen3 Embedding 4B | 32,768 | yes |  |
| [`qwen/qwen3-embedding-8b`](qwen/qwen3-embedding-8b.md) | Qwen3 Embedding 8B | 40,960 | yes |  |
| [`qwen/qwen3-livetranslate-flash-realtime`](qwen/qwen3-livetranslate-flash-realtime.md) | Qwen3-LiveTranslate-Flash-Realtime | 53,248 | no |  |
| [`qwen/qwen3-livetranslate-flash`](qwen/qwen3-livetranslate-flash.md) | Qwen3-LiveTranslate-Flash |  | no |  |
| [`qwen/qwen3-max-thinking`](qwen/qwen3-max-thinking.md) | Qwen3 Max Thinking | 262,144 | no |  |
| [`qwen/qwen3-max`](qwen/qwen3-max.md) | Qwen3 Max | 262,144 | no |  |
| [`qwen/qwen3-next-80b-a3b-instruct`](qwen/qwen3-next-80b-a3b-instruct.md) | Qwen3 Next 80B A3B Instruct | 262,144 | yes | 9.6 |
| [`qwen/qwen3-next-80b-a3b-thinking`](qwen/qwen3-next-80b-a3b-thinking.md) | Qwen3 Next 80B A3B Thinking | 262,144 | yes | 11.2 |
| [`qwen/qwen3-omni-30b-a3b-captioner`](qwen/qwen3-omni-30b-a3b-captioner.md) | Qwen3 Omni 30B A3B Captioner | 65,536 | yes |  |
| [`qwen/qwen3-omni-30b-a3b-instruct`](qwen/qwen3-omni-30b-a3b-instruct.md) | Qwen3 Omni 30B A3B Instruct | 65,536 | yes |  |
| [`qwen/qwen3-omni-30b-a3b-thinking`](qwen/qwen3-omni-30b-a3b-thinking.md) | Qwen3 Omni 30B A3B Thinking | 65,536 | yes |  |
| [`qwen/qwen3-omni-flash-realtime`](qwen/qwen3-omni-flash-realtime.md) | Qwen3-Omni-Flash-Realtime | 65,536 | no |  |
| [`qwen/qwen3-omni-flash`](qwen/qwen3-omni-flash.md) | Qwen3-Omni-Flash | 65,536 | no |  |
| [`qwen/qwen3-rerank`](qwen/qwen3-rerank.md) | Qwen3 Rerank |  | no |  |
| [`qwen/qwen3-reranker-0.6b`](qwen/qwen3-reranker-0.6b.md) | Qwen3 Reranker 0.6B | 40,960 | yes |  |
| [`qwen/qwen3-reranker-4b`](qwen/qwen3-reranker-4b.md) | Qwen3 Reranker 4B | 40,960 | yes |  |
| [`qwen/qwen3-reranker-8b`](qwen/qwen3-reranker-8b.md) | Qwen3 Reranker 8B | 40,960 | yes |  |
| [`qwen/qwen3-tts-12hz-0.6b-base`](qwen/qwen3-tts-12hz-0.6b-base.md) | Qwen3-TTS-12Hz-0.6B-Base |  | yes |  |
| [`qwen/qwen3-tts-12hz-0.6b-customvoice`](qwen/qwen3-tts-12hz-0.6b-customvoice.md) | Qwen3-TTS-12Hz-0.6B-CustomVoice |  | yes |  |
| [`qwen/qwen3-tts-12hz-1.7b-base`](qwen/qwen3-tts-12hz-1.7b-base.md) | Qwen3-TTS-12Hz-1.7B-Base |  | yes |  |
| [`qwen/qwen3-tts-12hz-1.7b-customvoice`](qwen/qwen3-tts-12hz-1.7b-customvoice.md) | Qwen3-TTS-12Hz-1.7B-CustomVoice |  | yes |  |
| [`qwen/qwen3-tts-12hz-1.7b-voicedesign`](qwen/qwen3-tts-12hz-1.7b-voicedesign.md) | Qwen3-TTS-12Hz-1.7B-VoiceDesign |  | yes |  |
| [`qwen/qwen3-tts-flash-realtime`](qwen/qwen3-tts-flash-realtime.md) | Qwen3-TTS-Flash-Realtime |  | no |  |
| [`qwen/qwen3-tts-flash`](qwen/qwen3-tts-flash.md) | Qwen3-TTS-Flash |  | no |  |
| [`qwen/qwen3-tts-instruct-flash-realtime`](qwen/qwen3-tts-instruct-flash-realtime.md) | Qwen3-TTS-Instruct-Flash-Realtime |  | no |  |
| [`qwen/qwen3-tts-instruct-flash`](qwen/qwen3-tts-instruct-flash.md) | Qwen3-TTS-Instruct-Flash |  | no |  |
| [`qwen/qwen3-tts-vc-2026-01-22`](qwen/qwen3-tts-vc-2026-01-22.md) | Qwen3-TTS-VC 2026-01-22 |  | no |  |
| [`qwen/qwen3-tts-vc-realtime-2026-01-15`](qwen/qwen3-tts-vc-realtime-2026-01-15.md) | Qwen3-TTS-VC-Realtime 2026-01-15 |  | no |  |
| [`qwen/qwen3-tts-vd-2026-01-26`](qwen/qwen3-tts-vd-2026-01-26.md) | Qwen3-TTS-VD 2026-01-26 |  | no |  |
| [`qwen/qwen3-tts-vd-realtime-2026-01-15`](qwen/qwen3-tts-vd-realtime-2026-01-15.md) | Qwen3-TTS-VD-Realtime 2026-01-15 |  | no |  |
| [`qwen/qwen3-vl-235b-a22b-instruct`](qwen/qwen3-vl-235b-a22b-instruct.md) | Qwen3 VL 235B A22B Instruct | 262,144 | yes | 9.9 |
| [`qwen/qwen3-vl-235b-a22b-thinking`](qwen/qwen3-vl-235b-a22b-thinking.md) | Qwen3 VL 235B A22B Thinking | 262,144 | yes |  |
| [`qwen/qwen3-vl-2b-instruct`](qwen/qwen3-vl-2b-instruct.md) | Qwen3 VL 2B Instruct | 262,144 | yes |  |
| [`qwen/qwen3-vl-2b-thinking`](qwen/qwen3-vl-2b-thinking.md) | Qwen3 VL 2B Thinking | 262,144 | yes |  |
| [`qwen/qwen3-vl-30b-a3b-instruct`](qwen/qwen3-vl-30b-a3b-instruct.md) | Qwen3 VL 30B A3B Instruct | 262,144 | yes | 7.9 |
| [`qwen/qwen3-vl-30b-a3b-thinking`](qwen/qwen3-vl-30b-a3b-thinking.md) | Qwen3 VL 30B A3B Thinking | 262,144 | yes | 9.5 |
| [`qwen/qwen3-vl-32b-instruct`](qwen/qwen3-vl-32b-instruct.md) | Qwen3 VL 32B Instruct | 262,144 | yes |  |
| [`qwen/qwen3-vl-32b-thinking`](qwen/qwen3-vl-32b-thinking.md) | Qwen3 VL 32B Thinking | 262,144 | yes |  |
| [`qwen/qwen3-vl-4b-instruct`](qwen/qwen3-vl-4b-instruct.md) | Qwen3 VL 4B Instruct | 262,144 | yes |  |
| [`qwen/qwen3-vl-4b-thinking`](qwen/qwen3-vl-4b-thinking.md) | Qwen3 VL 4B Thinking | 262,144 | yes |  |
| [`qwen/qwen3-vl-8b-instruct`](qwen/qwen3-vl-8b-instruct.md) | Qwen3 VL 8B Instruct | 262,144 | yes | 7.3 |
| [`qwen/qwen3-vl-8b-thinking`](qwen/qwen3-vl-8b-thinking.md) | Qwen3 VL 8B Thinking | 262,144 | yes |  |
| [`qwen/qwen3-vl-embedding-2b`](qwen/qwen3-vl-embedding-2b.md) | Qwen3 VL Embedding 2B | 32,768 | yes |  |
| [`qwen/qwen3-vl-embedding-8b`](qwen/qwen3-vl-embedding-8b.md) | Qwen3 VL Embedding 8B | 32,768 | yes |  |
| [`qwen/qwen3-vl-flash`](qwen/qwen3-vl-flash.md) | Qwen3-VL-Flash |  | no |  |
| [`qwen/qwen3-vl-plus`](qwen/qwen3-vl-plus.md) | Qwen3-VL-Plus | 262,144 | no |  |
| [`qwen/qwen3.5-0.8b`](qwen/qwen3.5-0.8b.md) | Qwen3.5 0.8B | 262,144 | yes |  |
| [`qwen/qwen3.5-122b-a10b`](qwen/qwen3.5-122b-a10b.md) | Qwen3.5 122B A10B | 262,144 | yes | 15.6 |
| [`qwen/qwen3.5-27b`](qwen/qwen3.5-27b.md) | Qwen3.5 27B | 262,144 | yes | 22.9 |
| [`qwen/qwen3.5-2b`](qwen/qwen3.5-2b.md) | Qwen3.5 2B | 262,144 | yes |  |
| [`qwen/qwen3.5-35b-a3b`](qwen/qwen3.5-35b-a3b.md) | Qwen3.5 35B A3B | 262,144 | yes | 19.3 |
| [`qwen/qwen3.5-397b-a17b`](qwen/qwen3.5-397b-a17b.md) | Qwen3.5 397B A17B | 262,144 | yes | 18.4 |
| [`qwen/qwen3.5-4b`](qwen/qwen3.5-4b.md) | Qwen3.5 4B | 262,144 | yes |  |
| [`qwen/qwen3.5-9b`](qwen/qwen3.5-9b.md) | Qwen3.5 9B | 262,144 | yes | 11.2 |
| [`qwen/qwen3.5-flash-02-23`](qwen/qwen3.5-flash-02-23.md) | Qwen3.5 Flash | 1,000,000 | no |  |
| [`qwen/qwen3.5-livetranslate-flash-realtime`](qwen/qwen3.5-livetranslate-flash-realtime.md) | Qwen3.5-LiveTranslate-Flash-Realtime |  | no |  |
| [`qwen/qwen3.5-ocr`](qwen/qwen3.5-ocr.md) | Qwen3.5-OCR | 65,536 | no |  |
| [`qwen/qwen3.5-omni-flash-realtime`](qwen/qwen3.5-omni-flash-realtime.md) | Qwen3.5-Omni-Flash-Realtime | 262,144 | no |  |
| [`qwen/qwen3.5-omni-flash`](qwen/qwen3.5-omni-flash.md) | Qwen3.5 Omni Flash | 262,144 | no |  |
| [`qwen/qwen3.5-omni-plus-realtime`](qwen/qwen3.5-omni-plus-realtime.md) | Qwen3.5-Omni-Plus-Realtime | 262,144 | no |  |
| [`qwen/qwen3.5-omni-plus`](qwen/qwen3.5-omni-plus.md) | Qwen3.5 Omni Plus | 262,144 | no |  |
| [`qwen/qwen3.5-plus-02-15`](qwen/qwen3.5-plus-02-15.md) | Qwen3.5 Plus 2026-02-15 | 1,000,000 | no |  |
| [`qwen/qwen3.5-plus-20260420`](qwen/qwen3.5-plus-20260420.md) | Qwen3.5 Plus 2026-04-20 | 1,000,000 | no |  |
| [`qwen/qwen3.6-27b`](qwen/qwen3.6-27b.md) | Qwen3.6 27B | 262,144 | yes | 21.4 |
| [`qwen/qwen3.6-35b-a3b`](qwen/qwen3.6-35b-a3b.md) | Qwen3.6 35B A3B | 262,144 | yes | 18.2 |
| [`qwen/qwen3.6-flash`](qwen/qwen3.6-flash.md) | Qwen3.6 Flash | 1,000,000 | no |  |
| [`qwen/qwen3.6-max-preview`](qwen/qwen3.6-max-preview.md) | Qwen3.6 Max Preview | 262,144 | no |  |
| [`qwen/qwen3.6-plus`](qwen/qwen3.6-plus.md) | Qwen3.6 Plus | 1,000,000 | no | 27 |
| [`qwen/qwen3.7-flash`](qwen/qwen3.7-flash.md) | Qwen3.7 Flash | 1,000,000 | no |  |
| [`qwen/qwen3.7-max`](qwen/qwen3.7-max.md) | Qwen3.7 Max | 1,000,000 | no | 29.5 |
| [`qwen/qwen3.7-plus`](qwen/qwen3.7-plus.md) | Qwen3.7 Plus | 1,000,000 | no | 25.2 |
| [`qwen/qwen3.7-text-embedding-flash`](qwen/qwen3.7-text-embedding-flash.md) | Qwen3.7 Text Embedding Flash | 128,000 | no |  |
| [`qwen/qwen3.7-text-embedding`](qwen/qwen3.7-text-embedding.md) | Qwen3.7 Text Embedding | 128,000 | no |  |
| [`qwen/qwen3.8-2.4t-a95b`](qwen/qwen3.8-2.4t-a95b.md) | Qwen3.8 2.4T A95B | 1,048,576 | yes | 39.9 |
| [`qwen/qwen3.8-27b`](qwen/qwen3.8-27b.md) | Qwen3.8 27B | 1,000,000 | yes | 33.7 |
| [`qwen/qwen3.8-flash`](qwen/qwen3.8-flash.md) | Qwen3.8 Flash | 1,000,000 | yes | 39.8 |
| [`qwen/qwen3.8-livetranslate-flash-realtime`](qwen/qwen3.8-livetranslate-flash-realtime.md) | Qwen3.8-LiveTranslate-Flash-Realtime | 53,248 | no |  |
| [`qwen/qwen3.8-max-0902`](qwen/qwen3.8-max-0902.md) | Qwen3.8 Max 0902 | 1,000,000 | no | 45.4 |
| [`qwen/qwen3.8-max-prime`](qwen/qwen3.8-max-prime.md) | Qwen3.8 Max Prime | 1,000,000 | no |  |
| [`qwen/qwen3.8-omni-flash-realtime`](qwen/qwen3.8-omni-flash-realtime.md) | Qwen3.8-Omni-Flash-Realtime |  | no |  |
| [`qwen/qwen3.8-omni-flash`](qwen/qwen3.8-omni-flash.md) | Qwen3.8 Omni Flash | 1,000,000 | no |  |
| [`qwen/qwen3guard-gen-0.6b`](qwen/qwen3guard-gen-0.6b.md) | Qwen3Guard Gen 0.6B | 32,768 | yes |  |
| [`qwen/qwen3guard-gen-4b`](qwen/qwen3guard-gen-4b.md) | Qwen3Guard Gen 4B | 32,768 | yes |  |
| [`qwen/qwen3guard-gen-8b`](qwen/qwen3guard-gen-8b.md) | Qwen3Guard Gen 8B | 32,768 | yes |  |
| [`qwen/qwq-32b-preview`](qwen/qwq-32b-preview.md) | QwQ 32B Preview | 32,768 | yes |  |
| [`qwen/qwq-32b`](qwen/qwq-32b.md) | QwQ 32B | 40,960 | yes |  |
| [`qwen/qwq-plus`](qwen/qwq-plus.md) | QwQ-Plus | 131,072 | no |  |
| [`qwen/text-embedding-v4`](qwen/text-embedding-v4.md) | Text Embedding v4 | 8,192 | no |  |
| [`qwen/webworld-14b`](qwen/webworld-14b.md) | WebWorld 14B | 40,960 | yes |  |
| [`qwen/webworld-32b`](qwen/webworld-32b.md) | WebWorld 32B | 40,960 | yes |  |
| [`qwen/webworld-8b`](qwen/webworld-8b.md) | WebWorld 8B | 40,960 | yes |  |
| [`unbabel/tower-plus-2b`](unbabel/tower-plus-2b.md) | Tower+ 2B | 8,192 | yes |  |
| [`unbabel/tower-plus-72b`](unbabel/tower-plus-72b.md) | Tower+ 72B | 32,768 | yes |  |
| [`unbabel/tower-plus-9b`](unbabel/tower-plus-9b.md) | Tower+ 9B | 8,192 | yes |  |
| [`unbabel/towerinstruct-13b-v0.1`](unbabel/towerinstruct-13b-v0.1.md) | TowerInstruct 13B v0.1 | 4,096 | yes |  |
| [`unbabel/towerinstruct-7b-v0.2`](unbabel/towerinstruct-7b-v0.2.md) | TowerInstruct 7B v0.2 | 4,096 | yes |  |
| [`unbabel/towerinstruct-mistral-7b-v0.2`](unbabel/towerinstruct-mistral-7b-v0.2.md) | TowerInstruct Mistral 7B v0.2 | 32,768 | yes |  |
| [`baidu/qianfan-ocr`](baidu/qianfan-ocr.md) | Qianfan-OCR | 32,768 | yes |  |
| [`baidu/unlimited-ocr`](baidu/unlimited-ocr.md) | Unlimited-OCR | 32,768 | yes |  |
| [`paddlepaddle/paddleocr-vl-1.5`](paddlepaddle/paddleocr-vl-1.5.md) | PaddleOCR-VL-1.5 | 131,072 | yes |  |
| [`paddlepaddle/paddleocr-vl-1.6`](paddlepaddle/paddleocr-vl-1.6.md) | PaddleOCR-VL-1.6 | 131,072 | yes |  |
| [`paddlepaddle/paddleocr-vl`](paddlepaddle/paddleocr-vl.md) | PaddleOCR-VL | 131,072 | yes |  |
| [`paddlepaddle/pp-chart2table`](paddlepaddle/pp-chart2table.md) | PP-Chart2Table | 32,768 | yes |  |
| [`paddlepaddle/pp-doclayoutv3`](paddlepaddle/pp-doclayoutv3.md) | PP-DocLayoutV3 |  | yes |  |
| [`paddlepaddle/pp-ocrv5`](paddlepaddle/pp-ocrv5.md) | PP-OCRv5 |  | yes |  |
| [`paddlepaddle/pp-ocrv6`](paddlepaddle/pp-ocrv6.md) | PP-OCRv6 |  | yes |  |
| [`paddlepaddle/pp-structurev3`](paddlepaddle/pp-structurev3.md) | PP-StructureV3 |  | yes |  |
| [`ibm-granite/granite-docling-258m`](ibm-granite/granite-docling-258m.md) | Granite-Docling-258M | 8,192 | yes |  |
| [`ibm-granite/granite-embedding-311m-multilingual-r2`](ibm-granite/granite-embedding-311m-multilingual-r2.md) | Granite Embedding 311M Multilingual R2 | 32,768 | yes |  |
| [`ibm-granite/granite-embedding-97m-multilingual-r2`](ibm-granite/granite-embedding-97m-multilingual-r2.md) | Granite Embedding 97M Multilingual R2 | 32,768 | yes |  |
| [`ibm-granite/granite-embedding-english-r2`](ibm-granite/granite-embedding-english-r2.md) | Granite Embedding English R2 | 8,192 | yes |  |
| [`ibm-granite/granite-embedding-small-english-r2`](ibm-granite/granite-embedding-small-english-r2.md) | Granite Embedding Small English R2 | 8,192 | yes |  |
| [`docling-project/codeformulav2`](docling-project/codeformulav2.md) | CodeFormulaV2 | 8,192 | yes |  |
| [`docling-project/docling-layout-egret`](docling-project/docling-layout-egret.md) | Docling Layout Egret |  | yes |  |
| [`docling-project/docling-layout-heron`](docling-project/docling-layout-heron.md) | Docling Layout Heron |  | yes |  |
| [`docling-project/docling-models`](docling-project/docling-models.md) | Docling Models (TableFormer V1) |  | yes |  |
| [`docling-project/granite-docling-2stage-258m`](docling-project/granite-docling-2stage-258m.md) | Granite-Docling-2stage-258M | 8,192 | yes |  |
| [`docling-project/smoldocling-256m-preview`](docling-project/smoldocling-256m-preview.md) | SmolDocling-256M-preview | 8,192 | yes |  |
| [`docling-project/tableformerv2`](docling-project/tableformerv2.md) | TableFormerV2 |  | yes |  |
| [`alibaba-nlp/gte-multilingual-base`](alibaba-nlp/gte-multilingual-base.md) | gte-multilingual-base | 8,192 | yes |  |
| [`alibaba-nlp/gte-qwen2-7b-instruct`](alibaba-nlp/gte-qwen2-7b-instruct.md) | gte-Qwen2-7B-instruct | 32,768 | yes |  |
| [`allenai/olmocr-2-7b-1025`](allenai/olmocr-2-7b-1025.md) | olmOCR-2-7B-1025 | 128,000 | yes |  |
| [`amazon/titan-embed-image-v1`](amazon/titan-embed-image-v1.md) | Titan Multimodal Embeddings G1 | 128 | no |  |
| [`amazon/titan-embed-text-v1`](amazon/titan-embed-text-v1.md) | Titan Embeddings G1 - Text | 8,192 | no |  |
| [`amazon/titan-embed-text-v2`](amazon/titan-embed-text-v2.md) | Titan Text Embeddings V2 | 8,192 | no |  |
| [`baai/bge-base-en-v1.5`](baai/bge-base-en-v1.5.md) | bge-base-en-v1.5 | 512 | yes |  |
| [`baai/bge-large-en-v1.5`](baai/bge-large-en-v1.5.md) | bge-large-en-v1.5 | 512 | yes |  |
| [`baai/bge-m3`](baai/bge-m3.md) | bge-m3 | 8,194 | yes |  |
| [`baai/bge-reranker-v2-m3`](baai/bge-reranker-v2-m3.md) | bge-reranker-v2-m3 | 8,194 | yes |  |
| [`cohere/embed-v4.0`](cohere/embed-v4.0.md) | Embed 4 | 128,000 | no |  |
| [`cohere/embed-v5.0-fast`](cohere/embed-v5.0-fast.md) | Embed 5 Fast | 128,000 | no |  |
| [`cohere/embed-v5.0-pro`](cohere/embed-v5.0-pro.md) | Embed 5 Pro | 128,000 | no |  |
| [`cohere/rerank-4-fast`](cohere/rerank-4-fast.md) | Rerank 4 Fast | 32,768 | no |  |
| [`cohere/rerank-4-pro`](cohere/rerank-4-pro.md) | Rerank 4 Pro | 32,768 | no |  |
| [`cohere/rerank-v3.5`](cohere/rerank-v3.5.md) | Rerank v3.5 | 4,096 | no |  |
| [`cohere/rerank-v5.0-fast`](cohere/rerank-v5.0-fast.md) | Rerank 5 Fast | 32,768 | no |  |
| [`cohere/rerank-v5.0-pro`](cohere/rerank-v5.0-pro.md) | Rerank 5 Pro | 32,768 | no |  |
| [`datalab-to/chandra-ocr-2`](datalab-to/chandra-ocr-2.md) | Chandra OCR 2 | 262,144 | yes |  |
| [`datalab-to/chandra`](datalab-to/chandra.md) | Chandra | 262,144 | yes |  |
| [`dots-studio/dots.mocr`](dots-studio/dots.mocr.md) | dots.mocr | 131,072 | yes |  |
| [`dots-studio/dots.ocr`](dots-studio/dots.ocr.md) | dots.ocr | 131,072 | yes |  |
| [`intfloat/e5-base-v2`](intfloat/e5-base-v2.md) | E5-Base-v2 | 512 | yes |  |
| [`intfloat/e5-large-v2`](intfloat/e5-large-v2.md) | E5-Large-v2 | 512 | yes |  |
| [`intfloat/e5-mistral-7b-instruct`](intfloat/e5-mistral-7b-instruct.md) | E5 Mistral 7B Instruct | 32,768 | yes |  |
| [`intfloat/multilingual-e5-large-instruct`](intfloat/multilingual-e5-large-instruct.md) | Multilingual E5 Large Instruct | 512 | yes |  |
| [`intfloat/multilingual-e5-large`](intfloat/multilingual-e5-large.md) | Multilingual-E5-Large | 512 | yes |  |
| [`jinaai/jina-embeddings-v4`](jinaai/jina-embeddings-v4.md) | Jina Embeddings v4 | 32,768 | yes |  |
| [`jinaai/jina-embeddings-v5-omni-nano`](jinaai/jina-embeddings-v5-omni-nano.md) | Jina Embeddings v5 Omni Nano | 8,192 | yes |  |
| [`jinaai/jina-embeddings-v5-omni-small`](jinaai/jina-embeddings-v5-omni-small.md) | Jina Embeddings v5 Omni Small | 32,768 | yes |  |
| [`jinaai/jina-embeddings-v5-text-nano`](jinaai/jina-embeddings-v5-text-nano.md) | Jina Embeddings v5 Text Nano | 8,192 | yes |  |
| [`jinaai/jina-embeddings-v5-text-small`](jinaai/jina-embeddings-v5-text-small.md) | Jina Embeddings v5 Text Small | 32,768 | yes |  |
| [`jinaai/jina-reranker-v3.5`](jinaai/jina-reranker-v3.5.md) | jina-reranker-v3.5 | 131,072 | yes |  |
| [`jinaai/jina-reranker-v3`](jinaai/jina-reranker-v3.md) | jina-reranker-v3 | 131,072 | yes |  |
| [`lightonai/lightonocr-1b-1025`](lightonai/lightonocr-1b-1025.md) | LightOnOCR-1B-1025 | 8,192 | yes |  |
| [`lightonai/lightonocr-2-1b`](lightonai/lightonocr-2-1b.md) | LightOnOCR-2-1B | 16,384 | yes |  |
| [`lightonai/lightonocr-3-0.8b`](lightonai/lightonocr-3-0.8b.md) | LightOnOCR-3-0.8B | 262,144 | yes |  |
| [`lightonai/lightonocr-3-1b`](lightonai/lightonocr-3-1b.md) | LightOnOCR-3-1B | 16,384 | yes |  |
| [`lightonai/lightonocr-3-4b`](lightonai/lightonocr-3-4b.md) | LightOnOCR-3-4B | 262,144 | yes |  |
| [`liquid/lfm-2.5-embedding-350m`](liquid/lfm-2.5-embedding-350m.md) | LFM2.5-Embedding-350M | 512 | yes |  |
| [`mixedbread-ai/mxbai-embed-large-v1`](mixedbread-ai/mxbai-embed-large-v1.md) | mxbai-embed-large-v1 | 512 | yes |  |
| [`mixedbread-ai/mxbai-rerank-base-v2`](mixedbread-ai/mxbai-rerank-base-v2.md) | mxbai-rerank-base-v2 | 32,768 | yes |  |
| [`mixedbread-ai/mxbai-rerank-large-v2`](mixedbread-ai/mxbai-rerank-large-v2.md) | mxbai-rerank-large-v2 | 32,768 | yes |  |
| [`nanonets/nanonets-ocr2-3b`](nanonets/nanonets-ocr2-3b.md) | Nanonets-OCR2-3B | 128,000 | yes |  |
| [`nomic-ai/nomic-embed-text-v1.5`](nomic-ai/nomic-embed-text-v1.5.md) | Nomic Embed Text v1.5 | 8,192 | yes |  |
| [`nomic-ai/nomic-embed-text-v2-moe`](nomic-ai/nomic-embed-text-v2-moe.md) | Nomic Embed Text v2 MoE | 512 | yes |  |
| [`nvidia/llama-nemotron-embed-vl-1b-v2`](nvidia/llama-nemotron-embed-vl-1b-v2.md) | Llama Nemotron Embed VL 1B V2 | 131,072 | yes |  |
| [`nvidia/llama-nemotron-rerank-vl-1b-v2`](nvidia/llama-nemotron-rerank-vl-1b-v2.md) | Llama Nemotron Rerank VL 1B V2 | 10,240 | yes |  |
| [`nvidia/nemotron-3-embed-1b`](nvidia/nemotron-3-embed-1b.md) | Nemotron 3 Embed 1B | 32,768 | yes |  |
| [`nvidia/nemotron-3.5-embed-1b`](nvidia/nemotron-3.5-embed-1b.md) | Nemotron 3.5 Embed 1B | 32,768 | yes |  |
| [`nvidia/nemotron-3.5-embed-8b`](nvidia/nemotron-3.5-embed-8b.md) | Nemotron 3.5 Embed 8B | 32,768 | yes |  |
| [`nvidia/nemotron-3.5-rerank-8b`](nvidia/nemotron-3.5-rerank-8b.md) | Nemotron 3.5 Rerank 8B | 32,768 | yes |  |
| [`opendatalab/mineru2.5-2509-1.2b`](opendatalab/mineru2.5-2509-1.2b.md) | MinerU2.5-2509-1.2B | 16,384 | yes |  |
| [`opendatalab/mineru2.5-pro-2604-1.2b`](opendatalab/mineru2.5-pro-2604-1.2b.md) | MinerU2.5-Pro-2604-1.2B |  | yes |  |
| [`opendatalab/mineru2.5-pro-2605-1.2b`](opendatalab/mineru2.5-pro-2605-1.2b.md) | MinerU2.5-Pro-2605-1.2B |  | yes |  |
| [`perplexity/pplx-embed-v1-0.6b`](perplexity/pplx-embed-v1-0.6b.md) | Embed V1 0.6B | 32,000 | yes |  |
| [`perplexity/pplx-embed-v1-4b`](perplexity/pplx-embed-v1-4b.md) | Embed V1 4B | 32,000 | yes |  |
| [`sentence-transformers/all-minilm-l12-v2`](sentence-transformers/all-minilm-l12-v2.md) | all-MiniLM-L12-v2 | 512 | yes |  |
| [`sentence-transformers/all-minilm-l6-v2`](sentence-transformers/all-minilm-l6-v2.md) | all-MiniLM-L6-v2 | 512 | yes |  |
| [`sentence-transformers/all-mpnet-base-v2`](sentence-transformers/all-mpnet-base-v2.md) | all-mpnet-base-v2 | 512 | yes |  |
| [`sentence-transformers/multi-qa-mpnet-base-dot-v1`](sentence-transformers/multi-qa-mpnet-base-dot-v1.md) | multi-qa-mpnet-base-dot-v1 | 512 | yes |  |
| [`sentence-transformers/paraphrase-minilm-l6-v2`](sentence-transformers/paraphrase-minilm-l6-v2.md) | paraphrase-MiniLM-L6-v2 | 512 | yes |  |
| [`snowflake/snowflake-arctic-embed-l-v2.0`](snowflake/snowflake-arctic-embed-l-v2.0.md) | Snowflake Arctic Embed L v2.0 | 8,192 | yes |  |
| [`thenlper/gte-base`](thenlper/gte-base.md) | GTE-Base | 512 | yes |  |
| [`thenlper/gte-large`](thenlper/gte-large.md) | GTE-Large | 512 | yes |  |
| [`voyageai/rerank-2.5-lite`](voyageai/rerank-2.5-lite.md) | rerank-2.5-lite | 32,000 | no |  |
| [`voyageai/rerank-2.5`](voyageai/rerank-2.5.md) | rerank-2.5 | 32,000 | no |  |
| [`voyageai/rerank-3-lite`](voyageai/rerank-3-lite.md) | rerank-3-lite | 32,000 | no |  |
| [`voyageai/rerank-3`](voyageai/rerank-3.md) | rerank-3 | 32,000 | no |  |
| [`voyageai/voyage-3-large`](voyageai/voyage-3-large.md) | voyage-3-large | 32,000 | no |  |
| [`voyageai/voyage-3.5-lite`](voyageai/voyage-3.5-lite.md) | voyage-3.5-lite | 32,000 | no |  |
| [`voyageai/voyage-3.5`](voyageai/voyage-3.5.md) | voyage-3.5 | 32,000 | no |  |
| [`voyageai/voyage-4-large`](voyageai/voyage-4-large.md) | voyage-4-large | 32,000 | no |  |
| [`voyageai/voyage-4-lite`](voyageai/voyage-4-lite.md) | voyage-4-lite | 32,000 | no |  |
| [`voyageai/voyage-4`](voyageai/voyage-4.md) | voyage-4 | 32,000 | no |  |
| [`voyageai/voyage-code-3`](voyageai/voyage-code-3.md) | voyage-code-3 | 32,000 | no |  |
| [`voyageai/voyage-code-4`](voyageai/voyage-code-4.md) | voyage-code-4 | 32,000 | no |  |
| [`voyageai/voyage-context-4`](voyageai/voyage-context-4.md) | voyage-context-4 | 120,000 | no |  |
| [`voyageai/voyage-multimodal-3.5`](voyageai/voyage-multimodal-3.5.md) | voyage-multimodal-3.5 | 32,000 | no |  |
