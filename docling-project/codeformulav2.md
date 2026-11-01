---
id: docling-project/codeformulav2
name: CodeFormulaV2
owned_by: ibm
type: llm
description: CodeFormulaV2 is IBM's 315M-parameter Idefics3-based model that reads a cropped image of code or a formula and returns the code with a language tag or the formula as LaTeX; it is Docling's default code and formula model.
aliases: [docling-project/CodeFormulaV2, ds4sd/CodeFormulaV2]
context_length: 8192
capabilities: [vision]
architecture:
  input_modalities: [image]
  output_modalities: [text]
open_weights: true
license: CDLA-Permissive-2.0
release_date: "2025-08-11"
sources:
  - https://huggingface.co/docling-project/CodeFormulaV2
  - https://huggingface.co/api/models/docling-project/CodeFormulaV2
  - https://huggingface.co/docling-project/CodeFormulaV2/raw/main/config.json
  - https://huggingface.co/docling-project/CodeFormula
  - https://huggingface.co/docling-project/CodeFormula/raw/main/config.json
  - https://arxiv.org/abs/2503.11576
  - https://arxiv.org/abs/2408.09869
  - https://docling-project.github.io/docling/usage/model_catalog/
  - https://openrouter.ai/api/v1/models
retrieved: "2026-11-01"
---

# CodeFormulaV2

## Overview
IBM's Docling team published CodeFormulaV2 on Hugging Face on 2025-08-11 under CDLA-Permissive-2.0. OpenRouter does not list it; the id follows the Hugging Face repo `docling-project/CodeFormulaV2`. It takes an image of a code snippet or formula at 120 DPI. For code it names the programming language and returns the code with its indentation, in the form `<_Java_> System.out.println("Hello World.");`; for formulas it returns LaTeX. It was trained on IBM's SynthFormulaNet and SynthCodeNet datasets and uses the Idefics3 architecture of SmolDocling (315.5M parameters, 8,192 positions). Docling's model catalog lists it as the default model of the code and formula enrichment stage, with Granite-Docling-258M as the alternative, on transformers, MLX or automatic inline engines. It replaces CodeFormula (January 2025, MIT), whose config shows a SAM-style vision tower with an OPT decoder.

## Strengths
- Identifies the language of code blocks and keeps indentation.
- Produces LaTeX for display formulas, so maths survives Markdown export.
- Small enough to run on CPU or Apple Silicon inside Docling.

## Limitations
- The model card publishes no accuracy scores.
- Works on crops only; it needs Docling's layout model to find code and formula regions.
- CDLA-Permissive-2.0 is a data licence rather than a software licence.

## Good for
- Docling enrichment of technical PDFs, papers and manuals.
- LaTeX extraction from maths-heavy documents.
