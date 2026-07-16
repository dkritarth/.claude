#!/usr/bin/env python3
"""
Global Claude Code token/cost tracker.

Scans every session transcript under ~/.claude/projects/**/*.jsonl (this
covers normal chat sessions, and subagent/worktree sessions, since each gets
its own project directory + transcript), extracts per-message model+usage,
prices it, and accumulates results incrementally into ~/.claude/usage/.

Files written (all under ~/.claude/usage/):
  state.json    - {source_file: {"size": int, "count": int}} scan checkpoint
  usage.jsonl   - one row per assistant message (append-only, raw)
  summary.json  - aggregated totals by model / by project / by day

Usage:
  python3 token_tracker.py scan
  python3 token_tracker.py report [--by model|project|day] [--project NAME] [--since YYYY-MM-DD]
"""
import json
import os
import sys
import argparse
from pathlib import Path
from datetime import datetime, timezone
from collections import defaultdict

CLAUDE_DIR = Path.home() / ".claude"
PROJECTS_DIR = CLAUDE_DIR / "projects"
USAGE_DIR = CLAUDE_DIR / "usage"
STATE_FILE = USAGE_DIR / "state.json"
USAGE_LOG = USAGE_DIR / "usage.jsonl"
SUMMARY_FILE = USAGE_DIR / "summary.json"

# Prices in USD per token (converted from $/MTok). Source: claude.com/pricing
# (fetched 2026-07-16). Update here when Anthropic changes pricing.
# Sonnet 5 has a date-dependent price change (introductory -> standard on
# 2026-09-01), handled via _sonnet5_price().
PRICING = {
    "claude-fable-5":     dict(inp=10.00, out=50.00, cache_5m=12.50, cache_1h=20.00, cache_read=1.00),
    "claude-mythos-5":    dict(inp=10.00, out=50.00, cache_5m=12.50, cache_1h=20.00, cache_read=1.00),
    "claude-opus-4-8":    dict(inp=5.00,  out=25.00, cache_5m=6.25,  cache_1h=10.00, cache_read=0.50),
    "claude-opus-4-7":    dict(inp=5.00,  out=25.00, cache_5m=6.25,  cache_1h=10.00, cache_read=0.50),
    "claude-opus-4-6":    dict(inp=5.00,  out=25.00, cache_5m=6.25,  cache_1h=10.00, cache_read=0.50),
    "claude-opus-4-5":    dict(inp=5.00,  out=25.00, cache_5m=6.25,  cache_1h=10.00, cache_read=0.50),
    "claude-opus-4-1":    dict(inp=15.00, out=75.00, cache_5m=18.75, cache_1h=30.00, cache_read=1.50),
    "claude-opus-4":      dict(inp=15.00, out=75.00, cache_5m=18.75, cache_1h=30.00, cache_read=1.50),
    "claude-sonnet-4-6":  dict(inp=3.00,  out=15.00, cache_5m=3.75,  cache_1h=6.00,  cache_read=0.30),
    "claude-sonnet-4-5":  dict(inp=3.00,  out=15.00, cache_5m=3.75,  cache_1h=6.00,  cache_read=0.30),
    "claude-sonnet-4":    dict(inp=3.00,  out=15.00, cache_5m=3.75,  cache_1h=6.00,  cache_read=0.30),
    "claude-haiku-4-5":   dict(inp=1.00,  out=5.00,  cache_5m=1.25,  cache_1h=2.00,  cache_read=0.10),
    "claude-haiku-3-5":   dict(inp=0.80,  out=4.00,  cache_5m=1.00,  cache_1h=1.60,  cache_read=0.08),
}
SONNET5_SWITCH = datetime(2026, 9, 1, tzinfo=timezone.utc)
SONNET5_INTRO = dict(inp=2.00, out=10.00, cache_5m=2.50, cache_1h=4.00, cache_read=0.20)
SONNET5_STANDARD = dict(inp=3.00, out=15.00, cache_5m=3.75, cache_1h=6.00, cache_read=0.30)


def _parse_ts(ts):
    if not ts:
        return None
    try:
        return datetime.fromisoformat(ts.replace("Z", "+00:00"))
    except ValueError:
        return None


def price_for(model, ts):
    """Look up per-MTok pricing dict for a model id, date-aware for sonnet-5."""
    if not model:
        return None
    if model.startswith("claude-sonnet-5"):
        when = _parse_ts(ts)
        return SONNET5_INTRO if (when is None or when < SONNET5_SWITCH) else SONNET5_STANDARD
    if model in PRICING:
        return PRICING[model]
    # fallback: longest known prefix match, for dated model ids like
    # "claude-opus-4-8-20260615"
    for key in sorted(PRICING, key=len, reverse=True):
        if model.startswith(key):
            return PRICING[key]
    return None


def cost_for_message(model, usage, ts):
    p = price_for(model, ts)
    if p is None or not usage:
        return None
    inp = usage.get("input_tokens", 0) or 0
    out = usage.get("output_tokens", 0) or 0
    cache_read = usage.get("cache_read_input_tokens", 0) or 0
    cc = usage.get("cache_creation") or {}
    c5 = cc.get("ephemeral_5m_input_tokens", 0) or 0
    c1h = cc.get("ephemeral_1h_input_tokens", 0) or 0
    if not c5 and not c1h:
        # older transcripts may only have cache_creation_input_tokens (no
        # 5m/1h split); treat it as 5m-priced, the common default.
        c5 = usage.get("cache_creation_input_tokens", 0) or 0
    cost = (
        inp * p["inp"]
        + out * p["out"]
        + cache_read * p["cache_read"]
        + c5 * p["cache_5m"]
        + c1h * p["cache_1h"]
    ) / 1_000_000
    return round(cost, 8)


def load_state():
    if STATE_FILE.exists():
        return json.loads(STATE_FILE.read_text())
    return {}


def save_state(state):
    STATE_FILE.write_text(json.dumps(state, indent=2))


def load_summary():
    if SUMMARY_FILE.exists():
        return json.loads(SUMMARY_FILE.read_text())
    return {"by_model": {}, "by_project": {}, "by_day": {}, "total": {"tokens_in": 0, "tokens_out": 0, "cost_usd": 0.0, "messages": 0}}


def save_summary(summary):
    SUMMARY_FILE.write_text(json.dumps(summary, indent=2))


def bump(bucket, key, tokens_in, tokens_out, cost):
    row = bucket.setdefault(key, {"tokens_in": 0, "tokens_out": 0, "cost_usd": 0.0, "messages": 0})
    row["tokens_in"] += tokens_in
    row["tokens_out"] += tokens_out
    row["cost_usd"] = round(row["cost_usd"] + cost, 8)
    row["messages"] += 1


def project_name_from_path(path):
    # ~/.claude/projects/<encoded-project-dir>/<session>.jsonl
    return path.parent.name


def scan():
    USAGE_DIR.mkdir(parents=True, exist_ok=True)
    state = load_state()
    summary = load_summary()
    new_rows = []
    # Claude Code writes one transcript line per streamed content block, but
    # each line repeats the SAME cumulative usage for that API call (keyed by
    # message.id). Without this dedup, cost/tokens get counted once per
    # content block instead of once per actual API call -- can inflate
    # totals by several times on tool-heavy sessions. Must be seeded from
    # already-recorded rows, not just this run's new lines: a message's
    # duplicate content-block lines can straddle two separate incremental
    # scan calls if the transcript file was still being written mid-scan.
    seen_msg_ids = set()
    if USAGE_LOG.exists():
        with USAGE_LOG.open() as f:
            for line in f:
                try:
                    mid = json.loads(line).get("message_id")
                except json.JSONDecodeError:
                    continue
                if mid:
                    seen_msg_ids.add(mid)

    if not PROJECTS_DIR.exists():
        print("no projects dir found:", PROJECTS_DIR)
        return

    files = sorted(PROJECTS_DIR.glob("*/*.jsonl"))
    for path in files:
        key = str(path)
        st = state.get(key, {"size": 0, "count": 0})
        size = path.stat().st_size
        if size < st["size"]:
            # file shrank/rotated -- rescan from scratch
            st = {"size": 0, "count": 0}

        with path.open("r", encoding="utf-8", errors="replace") as f:
            for i, line in enumerate(f):
                if i < st["count"]:
                    continue
                line = line.strip()
                if not line:
                    continue
                try:
                    rec = json.loads(line)
                except json.JSONDecodeError:
                    continue
                if rec.get("type") != "assistant":
                    continue
                msg = rec.get("message") or {}
                usage = msg.get("usage")
                model = msg.get("model")
                if not usage or not model:
                    continue
                msg_id = msg.get("id")
                if msg_id:
                    if msg_id in seen_msg_ids:
                        continue
                    seen_msg_ids.add(msg_id)
                ts = rec.get("timestamp")
                cost = cost_for_message(model, usage, ts)
                if cost is None:
                    continue
                inp = usage.get("input_tokens", 0) or 0
                out = usage.get("output_tokens", 0) or 0
                project = project_name_from_path(path)
                session_id = rec.get("sessionId") or rec.get("session_id")
                day = (ts or "")[:10]

                row = {
                    "timestamp": ts,
                    "project": project,
                    "session_id": session_id,
                    "message_id": msg_id,
                    "model": model,
                    "input_tokens": inp,
                    "output_tokens": out,
                    "cache_read_tokens": usage.get("cache_read_input_tokens", 0) or 0,
                    "cache_creation_tokens": (usage.get("cache_creation") or {}).get("ephemeral_5m_input_tokens", 0)
                        + (usage.get("cache_creation") or {}).get("ephemeral_1h_input_tokens", 0)
                        or usage.get("cache_creation_input_tokens", 0) or 0,
                    "cost_usd": cost,
                }
                new_rows.append(row)

                bump(summary["by_model"], model, inp, out, cost)
                bump(summary["by_project"], project, inp, out, cost)
                if day:
                    bump(summary["by_day"], day, inp, out, cost)
                t = summary["total"]
                t["tokens_in"] += inp
                t["tokens_out"] += out
                t["cost_usd"] = round(t["cost_usd"] + cost, 8)
                t["messages"] += 1

                st["count"] += 1

        st["size"] = size
        state[key] = st

    if new_rows:
        with USAGE_LOG.open("a", encoding="utf-8") as f:
            for row in new_rows:
                f.write(json.dumps(row) + "\n")

    save_state(state)
    save_summary(summary)
    print(f"scanned {len(files)} transcript files, {len(new_rows)} new messages recorded")


def report(by="model", project_filter=None, since=None):
    summary = load_summary()
    bucket_key = {"model": "by_model", "project": "by_project", "day": "by_day"}[by]
    bucket = summary.get(bucket_key, {})

    if project_filter or since:
        # recompute from raw log for filtered views
        bucket = defaultdict(lambda: {"tokens_in": 0, "tokens_out": 0, "cost_usd": 0.0, "messages": 0})
        if USAGE_LOG.exists():
            with USAGE_LOG.open() as f:
                for line in f:
                    row = json.loads(line)
                    if project_filter and project_filter not in row["project"]:
                        continue
                    if since and (row["timestamp"] or "") < since:
                        continue
                    k = row["model"] if by == "model" else row["project"] if by == "project" else (row["timestamp"] or "")[:10]
                    b = bucket[k]
                    b["tokens_in"] += row["input_tokens"]
                    b["tokens_out"] += row["output_tokens"]
                    b["cost_usd"] = round(b["cost_usd"] + row["cost_usd"], 8)
                    b["messages"] += 1

    rows = sorted(bucket.items(), key=lambda kv: -kv[1]["cost_usd"])
    total_cost = sum(v["cost_usd"] for _, v in rows)
    total_in = sum(v["tokens_in"] for _, v in rows)
    total_out = sum(v["tokens_out"] for _, v in rows)

    print(f"{'KEY':<40} {'IN':>12} {'OUT':>12} {'MSGS':>7} {'COST_USD':>10}")
    for k, v in rows:
        print(f"{k:<40} {v['tokens_in']:>12,} {v['tokens_out']:>12,} {v['messages']:>7,} {v['cost_usd']:>10.4f}")
    print("-" * 85)
    print(f"{'TOTAL':<40} {total_in:>12,} {total_out:>12,} {sum(v['messages'] for _,v in rows):>7,} {total_cost:>10.4f}")


def main():
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("scan")
    rep = sub.add_parser("report")
    rep.add_argument("--by", choices=["model", "project", "day"], default="model")
    rep.add_argument("--project", default=None, help="substring filter on project dir name")
    rep.add_argument("--since", default=None, help="YYYY-MM-DD, filters raw log")
    args = ap.parse_args()

    if args.cmd == "scan":
        scan()
    elif args.cmd == "report":
        scan()  # always catch up first
        report(by=args.by, project_filter=args.project, since=args.since)


if __name__ == "__main__":
    main()
