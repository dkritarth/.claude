# Claude Code Configuration & Skills

Personal Claude Code configuration, settings, and custom skills. Clone this to sync your Claude Code setup across machines.

## Contents

- **settings.json** — Global Claude Code settings (model, appearance, permissions, hooks, etc.)
- **keybindings.json** — Custom keyboard shortcuts
- **CLAUDE.md** — Project-level Claude instructions (if any)
- **skills/** — Custom and curated skills
  - `academic-humanizer/` — Improve academic writing clarity while preserving precision
  - `markitdown-converter/` — Convert PDFs, Word, Excel, PowerPoint, HTML to markdown
  - `anthropics-skills/` — Submodule: Official Anthropic skills (pdf, pptx, xlsx, etc.)
- **agents/** — Custom agent definitions (if any)

## Setup on a New Machine

### 1. Clone the repo

```bash
git clone https://github.com/Kritarth-Dandapat/.claude.git ~/.claude
cd ~/.claude
```

### 2. Initialize submodules

The repo includes the official Anthropic skills as a git submodule:

```bash
git submodule update --init --recursive
```

This pulls in skills from https://github.com/anthropics/skills.

### 3. Install skill dependencies

Some skills require external tools or libraries:

**markitdown-converter:**
```bash
pipx install markitdown
```

**Others** (pdf, pptx, xlsx, etc.) may need additional system packages — see the skill's SKILL.md for details.

### 4. Restart Claude Code

Restart Claude Code (or the IDE extension) to load the new settings and skills:

```bash
# Or restart your IDE
```

Skills are now available via `/skill-name` (e.g., `/pdf`, `/pptx`, `/academic-humanizer`).

## What's Inside Each Skill

### academic-humanizer
Improves clarity and voice of AI-assisted academic writing (papers, theses, proposals). Preserves scholarly conventions, citations, and evidence-binding. [SKILL.md](skills/academic-humanizer/SKILL.md)

### markitdown-converter
Convert documents (PDF, Word, Excel, PowerPoint, HTML, JSON, CSV, etc.) to markdown using Microsoft's markitdown. Perfect for reading complex documents as plain text. [SKILL.md](skills/markitdown-converter/SKILL.md)

### Anthropic Skills (via submodule)
Official skills from Anthropic:
- **pdf** — Read, extract, merge, split PDFs
- **pptx** — Create and edit PowerPoint presentations
- **xlsx** — Read and create Excel spreadsheets
- **docx** — Create and edit Word documents
- **skill-creator** — Generate new skills
- ... and 13 more

Run `/anthropics-skills` or individual skills directly (e.g., `/pdf`, `/pptx`).

## Customizing Your Setup

### Add a new skill

Create a skill directory in `skills/` with a `SKILL.md` file:

```bash
mkdir -p ~/.claude/skills/my-skill
cat > ~/.claude/skills/my-skill/SKILL.md << 'EOF'
---
name: my-skill
description: What this skill does
---
# My Skill
[Instructions here]
EOF
```

Restart Claude Code — the skill loads automatically.

### Modify settings

Edit `~/.claude/settings.json`:

```json
{
  "model": "claude-opus-4-8",
  "theme": "dark",
  ...
}
```

Or use Claude Code's `/config` command to edit interactively.

### Add custom agents

Create agent definitions in `agents/`:

```bash
mkdir -p ~/.claude/agents/my-agent
cat > ~/.claude/agents/my-agent/AGENT.md << 'EOF'
---
name: my-agent
description: Custom agent description
---
[Agent instructions]
EOF
```

## Updating Anthropic Skills

The `skills/anthropics-skills/` submodule points to the official Anthropic skills repository. To update it:

```bash
cd ~/.claude
git submodule update --remote
```

Commit and push:

```bash
git add .gitmodules skills/anthropics-skills/
git commit -m "Update anthropic skills"
git push
```

## What's NOT Included (by design)

- Logs, cache, and session history
- Daemon state and runtime files
- IDE metadata
- Plugin cache
- Backups and temporary files
- `.env.local` and secrets

These are git-ignored to keep the repo lightweight and shareable.

## Cloning to a Server/Remote Machine

```bash
# Clone with submodules
git clone --recursive https://github.com/Kritarth-Dandapat/.claude.git ~/.claude

# Install dependencies (if using markitdown or other skills)
pipx install markitdown

# Claude Code will auto-discover skills and settings on next startup
```

## File Structure

```
~/.claude/
├── .gitignore               # Git ignore rules
├── README.md                # This file
├── settings.json            # Global settings
├── keybindings.json         # Custom keybindings
├── .gitmodules              # Submodule config
├── CLAUDE.md                # User-level Claude instructions
├── skills/
│   ├── academic-humanizer/
│   │   ├── SKILL.md
│   │   └── (supporting files)
│   ├── markitdown-converter/
│   │   ├── SKILL.md
│   │   ├── converter.py
│   │   └── README.md
│   └── anthropics-skills/           # Submodule
│       └── skills/
│           ├── pdf/
│           ├── pptx/
│           ├── xlsx/
│           └── ... (13+ more)
└── agents/                  # Custom agents (if any)
    └── (agent definitions)
```

## License

Personal configuration. Individual skills retain their original licenses (see each SKILL.md).

## Help

- **Claude Code docs:** https://code.claude.com
- **Skill creation:** `/skill-creator`
- **Settings:** `/config` or edit `settings.json` directly
