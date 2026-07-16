#!/usr/bin/env python3
"""
Regenerates the usage-ledger HTML report from ~/.claude/usage/usage.jsonl.

Run token_tracker.py scan first (weekly_usage_report.sh does this). Writes
~/.claude/usage/usage-ledger.html, self-contained and ready for the
Artifact tool to publish.
"""
import json
from pathlib import Path
from datetime import datetime, timezone
from collections import defaultdict

CLAUDE_DIR = Path.home() / ".claude"
USAGE_LOG = CLAUDE_DIR / "usage" / "usage.jsonl"
OUT_FILE = CLAUDE_DIR / "usage" / "usage-ledger.html"

MODEL_NAMES = {
    "claude-sonnet-5": "Sonnet 5",
    "claude-haiku-4-5-20251001": "Haiku 4.5",
    "claude-sonnet-4-6": "Sonnet 4.6",
    "claude-opus-4-8": "Opus 4.8",
    "claude-fable-5": "Fable 5",
}


def clean_label(raw):
    s = raw
    if s.startswith("-Users-kritarth-"):
        s = s[len("-Users-kritarth-"):]
    elif s == "-Users-kritarth":
        return "home (~/.claude)"
    s = s.replace("--", " / ").replace("-", " ").strip()
    return s or "home (~/.claude)"


def build():
    rows = []
    with USAGE_LOG.open() as f:
        for line in f:
            line = line.strip()
            if line:
                rows.append(json.loads(line))

    by_project = defaultdict(lambda: {"in": 0, "out": 0, "cache_read": 0, "cache_creation": 0, "cost": 0.0, "msgs": 0})
    by_model = defaultdict(lambda: {"in": 0, "out": 0, "cache_read": 0, "cache_creation": 0, "cost": 0.0, "msgs": 0})

    for r in rows:
        for bucket, key in ((by_project, r["project"]), (by_model, r["model"])):
            d = bucket[key]
            d["in"] += r["input_tokens"]
            d["out"] += r["output_tokens"]
            d["cache_read"] += r.get("cache_read_tokens", 0)
            d["cache_creation"] += r.get("cache_creation_tokens", 0)
            d["cost"] += r["cost_usd"]
            d["msgs"] += 1

    grand = {
        "in": sum(d["in"] for d in by_model.values()),
        "out": sum(d["out"] for d in by_model.values()),
        "cache_read": sum(d["cache_read"] for d in by_model.values()),
        "cache_creation": sum(d["cache_creation"] for d in by_model.values()),
        "msgs": sum(d["msgs"] for d in by_model.values()),
        "cost": sum(d["cost"] for d in by_model.values()),
    }

    data = {
        "by_project": {clean_label(p): d for p, d in by_project.items()},
        "by_model": {MODEL_NAMES.get(m, m): d for m, d in by_model.items()},
        "grand_total": grand,
        "generated_at": datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC"),
        "project_count": len(by_project),
        "model_count": len(by_model),
    }

    html = TEMPLATE.replace("__DATA_JSON__", json.dumps(data))
    OUT_FILE.write_text(html)
    print(f"wrote {OUT_FILE} ({len(rows)} messages, ${grand['cost']:.2f} est.)")


TEMPLATE = r"""<title>Claude Code Usage Ledger</title>
<style>
  :root {
    --bg: #E9EDE2; --surface: #F6F8F1; --surface-2: #FFFFFF;
    --ink: #1E2A20; --ink-dim: #56634F; --ink-faint: #869180;
    --rule: #CBD3BE; --rule-strong: #A9B599;
    --accent: #9C5A2E; --accent-soft: #E6D2BC;
    --flag: #A93E32; --flag-soft: #EFD2CB;
    --ok: #3F7A5C; --ok-soft: #D3E6DA;
    --bar-track: #DDE3D2; --shadow: 0 1px 2px rgba(30,42,32,0.06);
  }
  @media (prefers-color-scheme: dark) {
    :root {
      --bg: #12160E; --surface: #191F14; --surface-2: #1F261A;
      --ink: #E8ECDE; --ink-dim: #A3AF95; --ink-faint: #6C7862;
      --rule: #313A28; --rule-strong: #414D34;
      --accent: #D98A4C; --accent-soft: #3B2C1C;
      --flag: #E0776A; --flag-soft: #3A2320;
      --ok: #7CC49B; --ok-soft: #1F3226;
      --bar-track: #262E1E; --shadow: 0 1px 3px rgba(0,0,0,0.4);
    }
  }
  :root[data-theme="dark"] {
    --bg: #12160E; --surface: #191F14; --surface-2: #1F261A;
    --ink: #E8ECDE; --ink-dim: #A3AF95; --ink-faint: #6C7862;
    --rule: #313A28; --rule-strong: #414D34;
    --accent: #D98A4C; --accent-soft: #3B2C1C;
    --flag: #E0776A; --flag-soft: #3A2320;
    --ok: #7CC49B; --ok-soft: #1F3226;
    --bar-track: #262E1E; --shadow: 0 1px 3px rgba(0,0,0,0.4);
  }
  :root[data-theme="light"] {
    --bg: #E9EDE2; --surface: #F6F8F1; --surface-2: #FFFFFF;
    --ink: #1E2A20; --ink-dim: #56634F; --ink-faint: #869180;
    --rule: #CBD3BE; --rule-strong: #A9B599;
    --accent: #9C5A2E; --accent-soft: #E6D2BC;
    --flag: #A93E32; --flag-soft: #EFD2CB;
    --ok: #3F7A5C; --ok-soft: #D3E6DA;
    --bar-track: #DDE3D2; --shadow: 0 1px 2px rgba(30,42,32,0.06);
  }
  * { box-sizing: border-box; }
  html, body { margin: 0; padding: 0; }
  body {
    background: var(--bg); color: var(--ink);
    font-family: -apple-system, "Segoe UI", "Helvetica Neue", Arial, sans-serif;
    line-height: 1.5; -webkit-font-smoothing: antialiased;
  }
  .mono, .num-cell, .stat-value { font-family: ui-monospace, "SF Mono", "Cascadia Mono", Menlo, Consolas, monospace; font-variant-numeric: tabular-nums; }
  .page { max-width: 920px; margin: 0 auto; padding: 56px 24px 96px; }
  header.masthead { display: flex; flex-direction: column; gap: 6px; padding-bottom: 28px; border-bottom: 1px solid var(--rule-strong); margin-bottom: 20px; }
  .eyebrow { font-size: 12px; letter-spacing: 0.09em; text-transform: uppercase; color: var(--ink-faint); font-weight: 600; }
  h1 { font-size: 30px; font-weight: 700; letter-spacing: -0.01em; margin: 2px 0 0; text-wrap: balance; }
  .subhead { color: var(--ink-dim); font-size: 14.5px; max-width: 62ch; }
  .updated { font-size: 12.5px; color: var(--ink-faint); margin-bottom: 28px; }
  .banner { background: var(--accent-soft); border: 1px solid color-mix(in srgb, var(--accent) 35%, transparent); border-radius: 10px; padding: 16px 20px; margin-bottom: 32px; font-size: 13.5px; color: var(--ink); }
  .banner strong { color: var(--accent); }
  .banner code { background: var(--surface-2); border: 1px solid var(--rule); border-radius: 4px; padding: 1px 5px; font-size: 12px; }
  .stats { display: grid; grid-template-columns: repeat(5, 1fr); gap: 1px; background: var(--rule); border: 1px solid var(--rule); border-radius: 10px; overflow: hidden; margin-bottom: 40px; }
  .stat { background: var(--surface); padding: 16px 14px; display: flex; flex-direction: column; gap: 4px; }
  .stat-label { font-size: 11px; letter-spacing: 0.06em; text-transform: uppercase; color: var(--ink-faint); font-weight: 600; }
  .stat-value { font-size: 19px; font-weight: 600; color: var(--ink); }
  .stat-value.accent { color: var(--accent); }
  section { margin-bottom: 44px; }
  .section-head { display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 4px; }
  h2 { font-size: 17px; font-weight: 700; margin: 0; }
  .section-note { font-size: 12.5px; color: var(--ink-faint); }
  .section-sub { font-size: 13px; color: var(--ink-dim); margin: 4px 0 18px; max-width: 68ch; }
  .ledger { background: var(--surface); border: 1px solid var(--rule); border-radius: 10px; overflow-x: auto; }
  table { width: 100%; border-collapse: collapse; min-width: 640px; }
  thead th { text-align: left; font-size: 10.5px; letter-spacing: 0.06em; text-transform: uppercase; color: var(--ink-faint); font-weight: 600; padding: 12px 14px; border-bottom: 1px solid var(--rule-strong); white-space: nowrap; }
  thead th.num-cell, tbody td.num-cell { text-align: right; }
  tbody td { padding: 11px 14px; font-size: 13px; border-bottom: 1px solid var(--rule); white-space: nowrap; }
  tbody tr:last-child td { border-bottom: none; }
  tbody tr:hover { background: var(--surface-2); }
  td.name-cell { display: flex; flex-direction: column; gap: 6px; min-width: 220px; }
  .name-label { font-weight: 600; font-size: 13px; }
  .bar-track { height: 5px; width: 100%; background: var(--bar-track); border-radius: 3px; overflow: hidden; }
  .bar-fill { height: 100%; background: var(--accent); border-radius: 3px; }
  td.cost-cell { font-weight: 700; color: var(--accent); }
  .msgs-cell { color: var(--ink-faint); }
  .foot { margin-top: 56px; padding-top: 20px; border-top: 1px solid var(--rule); display: flex; flex-direction: column; gap: 10px; font-size: 12.5px; color: var(--ink-faint); }
  .foot strong { color: var(--ink-dim); }
  @media (max-width: 640px) { .stats { grid-template-columns: repeat(2, 1fr); } h1 { font-size: 25px; } }
</style>
<div class="page">
  <header class="masthead">
    <div class="eyebrow">Local transcript audit &middot; ~/.claude</div>
    <h1>Claude Code usage ledger</h1>
    <div class="subhead">Every assistant message across every local project transcript, priced at published per-token API rates and broken out by project and by model. Regenerated weekly.</div>
  </header>
  <div class="updated" id="updated-at"></div>
  <div class="banner"><strong>Not your bill.</strong> You're on a subscription plan &mdash; usage draws down a plan allowance on rolling windows, not per-token API billing. These dollar figures are a hypothetical: what the same tokens would cost at published API rates. Run <code>/usage</code> in an interactive session for your real plan usage.</div>
  <div class="stats" id="stat-row"></div>
  <section>
    <div class="section-head"><h2>By project</h2><span class="section-note" id="project-count"></span></div>
    <div class="section-sub">Sorted by estimated cost.</div>
    <div class="ledger"><table id="project-table"><thead><tr>
      <th>Project</th><th class="num-cell">Messages</th><th class="num-cell">Input</th><th class="num-cell">Output</th><th class="num-cell">Cache read</th><th class="num-cell">Cache write</th><th class="num-cell">Est. cost</th>
    </tr></thead><tbody></tbody></table></div>
  </section>
  <section>
    <div class="section-head"><h2>By model</h2><span class="section-note" id="model-count"></span></div>
    <div class="ledger"><table id="model-table"><thead><tr>
      <th>Model</th><th class="num-cell">Messages</th><th class="num-cell">Input</th><th class="num-cell">Output</th><th class="num-cell">Cache read</th><th class="num-cell">Cache write</th><th class="num-cell">Est. cost</th>
    </tr></thead><tbody></tbody></table></div>
  </section>
  <div class="foot">
    <div>Source: <code>~/.claude/projects/*/*.jsonl</code> transcripts, deduped by message id (each streamed content block otherwise repeats the same usage figures), priced via <code>scripts/token_tracker.py</code> against claude.com/pricing.</div>
    <div>Regenerated weekly by a local launchd job &mdash; <code>scripts/weekly_usage_report.sh</code>.</div>
  </div>
</div>
<script>
const DATA = __DATA_JSON__;
function fmt(n) { return new Intl.NumberFormat('en-US').format(Math.round(n)); }
function fmtCost(n) { return '$' + n.toFixed(2); }

document.getElementById('updated-at').textContent = 'As of ' + DATA.generated_at;
document.getElementById('project-count').textContent = DATA.project_count + ' projects';
document.getElementById('model-count').textContent = DATA.model_count + ' models';

const g = DATA.grand_total;
const stats = [
  { label: 'Messages', value: fmt(g.msgs) },
  { label: 'Input tokens', value: fmt(g.in) },
  { label: 'Output tokens', value: fmt(g.out) },
  { label: 'Cache read tokens', value: fmt(g.cache_read) },
  { label: 'Est. total cost', value: fmtCost(g.cost), accent: true },
];
document.getElementById('stat-row').innerHTML = stats.map(s => `
  <div class="stat"><span class="stat-label">${s.label}</span><span class="stat-value${s.accent ? ' accent' : ''}">${s.value}</span></div>
`).join('');

const projects = Object.entries(DATA.by_project).map(([label, v]) => ({ label, ...v })).sort((a, b) => b.cost - a.cost);
const maxProjectCost = Math.max(...projects.map(p => p.cost), 1);
document.querySelector('#project-table tbody').innerHTML = projects.map(p => `
  <tr>
    <td class="name-cell"><span class="name-label">${p.label}</span><div class="bar-track"><div class="bar-fill" style="width:${(p.cost / maxProjectCost * 100).toFixed(1)}%"></div></div></td>
    <td class="num-cell msgs-cell mono">${fmt(p.msgs)}</td>
    <td class="num-cell mono">${fmt(p.in)}</td>
    <td class="num-cell mono">${fmt(p.out)}</td>
    <td class="num-cell mono">${fmt(p.cache_read)}</td>
    <td class="num-cell mono">${fmt(p.cache_creation)}</td>
    <td class="num-cell cost-cell mono">${fmtCost(p.cost)}</td>
  </tr>
`).join('');

const models = Object.entries(DATA.by_model).map(([label, v]) => ({ label, ...v })).sort((a, b) => b.cost - a.cost);
const maxModelCost = Math.max(...models.map(m => m.cost), 1);
document.querySelector('#model-table tbody').innerHTML = models.map(m => `
  <tr>
    <td class="name-cell"><span class="name-label">${m.label}</span><div class="bar-track"><div class="bar-fill" style="width:${(m.cost / maxModelCost * 100).toFixed(1)}%"></div></div></td>
    <td class="num-cell msgs-cell mono">${fmt(m.msgs)}</td>
    <td class="num-cell mono">${fmt(m.in)}</td>
    <td class="num-cell mono">${fmt(m.out)}</td>
    <td class="num-cell mono">${fmt(m.cache_read)}</td>
    <td class="num-cell mono">${fmt(m.cache_creation)}</td>
    <td class="num-cell cost-cell mono">${fmtCost(m.cost)}</td>
  </tr>
`).join('');
</script>
"""

if __name__ == "__main__":
    build()
