---
id: paddlepaddle/pp-chart2table
name: PP-Chart2Table
owned_by: baidu
type: llm
description: PP-Chart2Table is PaddlePaddle's 0.58B-parameter Apache-2.0 chart-parsing model that converts a Chinese or English chart image into a data table; it is the optional chart module of PP-StructureV3.
aliases: [PaddlePaddle/PP-Chart2Table, PaddlePaddle/PP-Chart2Table_safetensors]
context_length: 32768
capabilities: [vision]
architecture:
  input_modalities: [image]
  output_modalities: [text]
open_weights: true
license: Apache-2.0
release_date: "2025-06-05"
sources:
  - https://huggingface.co/PaddlePaddle/PP-Chart2Table
  - https://huggingface.co/api/models/PaddlePaddle/PP-Chart2Table
  - https://huggingface.co/PaddlePaddle/PP-Chart2Table/raw/main/config.json
  - https://huggingface.co/PaddlePaddle/PP-Chart2Table_safetensors
  - https://www.paddleocr.ai/latest/en/version3.x/module_usage/chart_parsing.html
  - https://www.paddleocr.ai/latest/en/version3.x/pipeline_usage/PP-StructureV3.html
  - https://www.paddleocr.ai/latest/en/version3.x/algorithm/PP-StructureV3/PP-StructureV3.html
  - https://openrouter.ai/api/v1/models
retrieved: "2026-11-01"
---

# PP-Chart2Table

## Overview
PaddlePaddle published PP-Chart2Table on Hugging Face on 2025-06-05 under Apache 2.0, with a safetensors repo added on 2026-03-10. OpenRouter does not list it; the id follows the Hugging Face repo `PaddlePaddle/PP-Chart2Table`. It takes a chart image and returns its data as a pipe-separated table. PaddleOCR's docs give 0.58B parameters and 1.4 GB of storage; config.json shows the GOT-OCR2.0 lineage (`GOTQwenForCausalLM`, a Qwen tokenizer, 32,768 positions). Baidu trained it with a "Shuffled Chart Data Retrieval" task and token masking, synthetic data built from seed charts, RAG and LLM personas, and two-stage distillation on unlabelled out-of-distribution charts. It runs through PaddleX (`create_model('PP-Chart2Table')`) or inside PP-StructureV3 with `--use_chart_recognition True`.

## Strengths
- In-house score 75.98; Baidu says it leads models of its size and matches 7B VLMs in key Chinese and English chart scenarios.
- Trained on a dataset of nearly 700,000 entries covering pie, bar, stacked area and other common chart types.
- Plugs into PP-StructureV3 so charts in parsed documents become tables.

## Limitations
- Only in-house benchmarks are published.
- Works on chart crops; layout detection must find the chart first.
- In PP-StructureV3, enabling chart parsing raises A100 time from 1.12 to 2.76 s per page.
- Served through PaddleX and PaddleOCR; the card gives no vLLM or transformers recipe.

## Good for
- Extracting numbers from charts in reports and filings.
- Chinese financial and research documents processed with PP-StructureV3.
