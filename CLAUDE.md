# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Purpose

Personal Claude Code configuration and skills repository. Syncs Claude Code settings, custom skills, and agent definitions across machines.

## Setup Commands

Clone with submodules:
```bash
git clone --recursive https://github.com/Kritarth-Dandapat/.claude.git ~/.claude
```

Install dependencies:
```bash
pipx install markitdown  # Required for markitdown-converter skill
```

Restart Claude Code to load settings and skills.

## Repository Structure

```
~/.claude/
├── settings.json              # Global settings (model, theme, hooks, plugins)
├── settings.local.json        # Machine-specific overrides (not committed)
├── keybindings.json           # Custom keyboard shortcuts
├── README.md                  # Setup and overview
├── CLAUDE.md                  # This file
├── skills/
│   ├── academic-humanizer/    # Improve academic writing clarity
│   ├── markitdown-converter/  # PDF/Word/Excel to markdown
│   ├── anthropics-skills/     # Submodule: official Anthropic skills
│   └── mattpocock-skills/     # Submodule: Matt Pocock's skills collection
├── agents/                    # Custom agent definitions (if any)
├── .gitignore                 # Excludes cache, logs, sessions
└── .gitmodules                # Submodule configuration
```

## Key Configuration Files

**settings.json** — Global settings:
- `model`: Default Claude model (currently "haiku")
- `hooks`: SessionStart hook activates caveman mode
- `statusLine`: Custom status line script
- `enabledPlugins`: caveman and agent-skills plugins
- `extraKnownMarketplaces`: Additional skill sources (caveman, anthropic-agent-skills, addy-agent-skills)
- `theme`: "dark" mode

**settings.local.json** — Machine-specific overrides (git-ignored). Use for local customizations without affecting the repo.

## Common Development Tasks

### Add a new skill

Create skill directory with SKILL.md metadata file:
```bash
mkdir -p skills/my-skill
cat > skills/my-skill/SKILL.md << 'EOF'
---
name: my-skill
description: Brief description
---
# My Skill
[Instructions]
EOF
```

Restart Claude Code. Skill loads automatically as `/my-skill`.

### Modify global settings

Edit `settings.json` directly or use Claude Code's `/config` command. Changes take effect on restart.

### Update submodules

Update all submodules (Anthropic and Matt Pocock skills):
```bash
git submodule update --remote
git add .gitmodules skills/anthropics-skills/ skills/mattpocock-skills/
git commit -m "Update skills submodules"
```

Or update a single submodule:
```bash
cd skills/anthropics-skills && git pull origin main && cd ../..
# or
cd skills/mattpocock-skills && git pull origin main && cd ../..
```

### Test a skill before committing

Use the skill in a Claude Code session. Verify it works as expected, then commit with a clear message documenting the skill's purpose.

## Installed Skills

- **academic-humanizer** — Polish academic writing (papers, proposals) while preserving citations and evidence
- **markitdown-converter** — Convert PDFs, Word docs, Excel, PowerPoint, HTML to markdown
- **anthropics-skills/** — Official Anthropic skills (pdf, pptx, xlsx, docx, skill-creator, and 13+ more)
- **mattpocock-skills/** — Matt Pocock's community skills collection (TypeScript, debugging, testing utilities, and more)

See README.md for full skill details and usage.

## Architecture Notes

### Skill Discovery
Skills in `skills/` with a `SKILL.md` file are auto-discovered by Claude Code. The `name:` field in frontmatter determines the slash command (e.g., `name: pdf` → `/pdf`).

### Plugin System
Custom plugins (caveman, agent-skills) are configured in settings.json's `enabledPlugins` and `extraKnownMarketplaces`. This allows extending Claude Code with external plugin repositories.

### Hooks
SessionStart hook activates caveman mode on every session (writing `.caveman-mode-active` file). Supports different intensity levels: lite, full, ultra.

### Submodules
Two git submodules provide external skill collections:
- **anthropics-skills/** — https://github.com/anthropics/skills
- **mattpocock-skills/** — https://github.com/mattpocock/skills

Update all submodules with `git submodule update --remote` or update individually with `cd skills/<submodule> && git pull origin main`.

## What's Git-Ignored

- Logs, cache, and session history
- Daemon state and runtime files
- IDE metadata
- Plugin cache
- Temporary files and backups
- `.env.local`, `.secrets`, and sensitive files

See `.gitignore` for the full list.

## When Cloning to a New Machine

1. Clone with submodules: `git clone --recursive https://github.com/Kritarth-Dandapat/.claude.git ~/.claude`
2. Install dependencies: `pipx install markitdown`
3. Restart Claude Code — settings and skills auto-load

For server/headless setups, only steps 1–2 are needed; CLI usage works without a GUI.

## When Adding Changes

**Skills**: Include a clear SKILL.md with the skill's purpose and usage instructions. Test before committing.

**Settings**: Update settings.json with new hooks, plugins, or configurations. Document the change in commit message if non-obvious.

**Dependencies**: If adding a skill that requires new tools (e.g., a Python library), document installation in this file and in the skill's SKILL.md.
