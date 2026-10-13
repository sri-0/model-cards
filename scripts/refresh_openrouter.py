#!/usr/bin/env python3
"""Refresh the OpenRouter-derived fields of every model card.

Fetches https://openrouter.ai/api/v1/models (public, no key) and, for each card
whose `id` OpenRouter lists, rewrites these frontmatter fields:

  context_length, max_output_tokens, capabilities, supported_parameters,
  architecture, pricing

Everything else (name, description, aliases, licence, dates, benchmarks,
sources, body) is left alone. Cards for models OpenRouter does not list are
skipped. Standard library only.

Usage:
  python3 scripts/refresh_openrouter.py              # rewrite cards in place
  python3 scripts/refresh_openrouter.py --dry-run    # print what would change
  python3 scripts/refresh_openrouter.py --set-retrieved   # also set `retrieved` to today
  python3 scripts/refresh_openrouter.py --models-json models.json   # use a saved API response
"""
import argparse
import datetime
import json
import os
import re
import sys
import urllib.request

API = "https://openrouter.ai/api/v1/models"
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MANAGED = ["context_length", "max_output_tokens", "capabilities",
           "supported_parameters", "architecture", "pricing"]


def scalar(v, flow=True):
    if isinstance(v, bool):
        return "true" if v else "false"
    if isinstance(v, (int, float)):
        return str(v)
    s = str(v)
    if s == "" or re.search(r"[:,\[\]{}#&*!|>'\"%@`]", s) or re.fullmatch(r"[\d.eE+-]+", s) \
            or s.lower() in ("true", "false", "null", "yes", "no", "on", "off", "~"):
        return json.dumps(s)
    return s


def per_million(s):
    v = float(f"{float(s) * 1_000_000:.6g}")
    return int(v) if v.is_integer() else v


def fields_from(m):
    """Card fields derived from one OpenRouter model object, as YAML text blocks."""
    out = {}
    params = m.get("supported_parameters") or []
    arch = m.get("architecture") or {}
    ins = arch.get("input_modalities") or []
    if m.get("context_length"):
        out["context_length"] = f"context_length: {m['context_length']}"
    mo = (m.get("top_provider") or {}).get("max_completion_tokens")
    if mo:
        out["max_output_tokens"] = f"max_output_tokens: {mo}"
    caps = [c for c, ok in (("tool_calling", "tools" in params), ("reasoning", "reasoning" in params),
                            ("vision", "image" in ins), ("structured_output", "structured_outputs" in params)) if ok]
    out["capabilities"] = "capabilities: [" + ", ".join(caps) + "]"
    if params:
        out["supported_parameters"] = "supported_parameters: [" + ", ".join(scalar(p) for p in params) + "]"
    a = ["architecture:"]
    for k in ("input_modalities", "output_modalities"):
        if arch.get(k):
            a.append(f"  {k}: [" + ", ".join(scalar(x) for x in arch[k]) + "]")
    for k in ("tokenizer", "instruct_type"):
        if arch.get(k):
            a.append(f"  {k}: {scalar(arch[k])}")
    if len(a) > 1:
        out["architecture"] = "\n".join(a)
    p = m.get("pricing") or {}
    pr = ["pricing:"]
    for src, dst in (("prompt", "input"), ("completion", "output"),
                     ("input_cache_read", "cache_read"), ("input_cache_write", "cache_write")):
        if p.get(src) is not None:
            pr.append(f"  {dst}: {per_million(p[src])}")
    if len(pr) > 1:
        out["pricing"] = "\n".join(pr)
    return out


def split_blocks(fm):
    """Split frontmatter text into [(key, text)] top-level blocks, keeping order."""
    blocks = []
    for line in fm.split("\n"):
        m = re.match(r"^([A-Za-z_][A-Za-z0-9_]*):", line)
        if m:
            blocks.append([m.group(1), line])
        elif blocks:
            blocks[-1][1] += "\n" + line
    return blocks


def refresh(path, models, set_retrieved, dry_run):
    text = open(path, encoding="utf-8").read()
    m = re.match(r"---\n(.*?)\n---\n(.*)", text, re.S)
    if not m:
        print(f"skip (no frontmatter): {path}", file=sys.stderr)
        return False
    fm, body = m.group(1), m.group(2)
    blocks = split_blocks(fm)
    ident = next((b[1].split(":", 1)[1].strip() for b in blocks if b[0] == "id"), None)
    model = models.get(ident)
    if not model:
        return False
    new = fields_from(model)
    keys = [b[0] for b in blocks]
    for key in MANAGED:
        if key in new:
            if key in keys:
                blocks[keys.index(key)][1] = new[key]
            else:  # insert before the first key that follows it in the canonical order
                after = [k for k in ["license", "open_weights", "release_date", "knowledge_cutoff",
                                     "pricing", "benchmarks", "sources"] if k in keys]
                pos = keys.index(after[0]) if after else len(blocks)
                blocks.insert(pos, [key, new[key]])
                keys.insert(pos, key)
    if set_retrieved and "retrieved" in keys:
        blocks[keys.index("retrieved")][1] = f'retrieved: "{datetime.date.today().isoformat()}"'
    out = "---\n" + "\n".join(b[1] for b in blocks) + "\n---\n" + body
    if out == text:
        return False
    if dry_run:
        print(f"would update {os.path.relpath(path, ROOT)}")
    else:
        with open(path, "w", encoding="utf-8") as f:
            f.write(out)
        print(f"updated {os.path.relpath(path, ROOT)}")
    return True


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--set-retrieved", action="store_true")
    ap.add_argument("--models-json", help="read a saved /api/v1/models response instead of fetching")
    args = ap.parse_args()
    if args.models_json:
        data = json.load(open(args.models_json))
    else:
        req = urllib.request.Request(API, headers={"User-Agent": "model-cards-refresh"})
        with urllib.request.urlopen(req, timeout=60) as r:
            data = json.load(r)
    models = {m["id"]: m for m in data["data"]}
    changed = 0
    for dirpath, dirnames, filenames in os.walk(ROOT):
        dirnames[:] = [d for d in dirnames if not d.startswith(".") and d != "scripts"]
        for fn in filenames:
            if fn.endswith(".md") and dirpath != ROOT:
                changed += refresh(os.path.join(dirpath, fn), models, args.set_retrieved, args.dry_run)
    print(f"{changed} card(s) {'would change' if args.dry_run else 'changed'}")


if __name__ == "__main__":
    main()
