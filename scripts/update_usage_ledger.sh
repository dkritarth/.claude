#!/usr/bin/env bash
# Rescans local transcripts, rebuilds the usage ledger HTML, and asks a
# headless Claude Code session to republish it to the existing artifact URL.
# Run manually whenever you want an updated view -- no scheduler attached.
set -euo pipefail

CLAUDE_DIR="$HOME/.claude"
ARTIFACT_URL="https://claude.ai/code/artifact/ee466f64-6fa0-4abe-9d99-b62ff19f2acc"
PAGE="$CLAUDE_DIR/usage/usage-ledger.html"

echo "Scanning transcripts..."
python3 "$CLAUDE_DIR/scripts/token_tracker.py" scan

echo "Rebuilding ledger page..."
python3 "$CLAUDE_DIR/scripts/build_usage_page.py"

echo "Publishing artifact..."
claude -p "Publish the file at $PAGE as an Artifact, updating the existing artifact at $ARTIFACT_URL (pass that as the url parameter so it redeploys in place instead of minting a new one). Use favicon emoji 📒, label 'usage-update', and description 'Claude Code local usage/cost breakdown by project and model, updated $(date -u +%Y-%m-%d)'. Do not modify the file content." \
  --allowedTools "Artifact,Read"

echo "Done."
