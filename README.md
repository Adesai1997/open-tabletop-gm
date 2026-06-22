# open-tabletop-gm

<div align="center">
  <img src="docs/icons/logo_primary_fullcolor.png" width="280" alt="open-tabletop-gm">
</div>

An LLM-agnostic Game Master framework for persistent tabletop RPG campaigns. Built to run on any model available through [OpenCode](https://opencode.ai), locally hosted models via [LM Studio](https://lmstudio.ai), or any other LLM service.

D&D 5e is included as the reference system. Any other tabletop RPG can be added by writing a system module — see [SYSTEM-PORTING.md](SYSTEM-PORTING.md).

> **Using Claude?** This framework was extracted from [`claude-dnd-skill`](https://github.com/Bobby-Gray/claude-dnd-skill), a Claude Code-specific version with deeper integration. If you're running Claude Code, that repo will give you a more optimised experience.

![open-tabletop-gm demo](docs/screenshots/demo-v3.gif)

---

## What it is

A GM framework that offloads everything mechanical to Python so the LLM can focus on narration and judgment:

- <img src="docs/icons/scroll.png" height="18"> **Persistent campaigns** — state, world, NPCs, and character sheets survive across sessions in plain Markdown files
- <img src="docs/icons/dagger.png" height="18"> **Python toolchain** — dice, combat initiative, HP tracking, timed effects, conditions, calendar, campaign search; all run locally with zero LLM involvement
- <img src="docs/icons/crystal_ball.png" height="18"> **Cinematic display companion** — optional Flask web app that renders your session as a live display on any browser or TV, with a real-time stat sidebar, effect pills, and player input panel
- <img src="docs/icons/dragon.png" height="18"> **System plugin architecture** — D&D 5e ships as the reference implementation; swap in any TTRPG by writing a system module
- <img src="docs/icons/spellbook.png" height="18"> **Campaign relationship graph** — typed-edge graph alongside the markdown campaign files, with verbatim source-anchors on every edge; `scene-context` query auto-pulled at `/gm load` to surface who-knows-whom in the current scene without re-reading full NPC files; designed to hold long-session continuity when context compaction strips files out of scope. Manual + query-only in this fork (no LLM dependency); see [`CHANGELOG.md`](CHANGELOG.md) for the why

---

## System plugin architecture

The framework is split into two layers:

```
SKILL.md                    ← GM core: pacing, NPCs, improvisation, world craft
                               Never changes. Works for any game.

systems/<your-system>/
  system.md                 ← Your game's rules: dice, stats, health, resources
                               Loaded alongside SKILL.md at session start.
```

`SKILL.md` contains everything about *being a good GM*. `system.md` contains everything about *your specific game*. The GM model reads both at session start — it brings the craft, your system module brings the rules.

**D&D 5e ships as the reference implementation.** It demonstrates what a complete system module looks like: dice conventions, ability scores, spell slots, conditions, death saves, SRD lookup, and character scripts.

**Building a new system module** takes one file to start — a filled-in `systems/TEMPLATE.md` for your game. You can start with just dice resolution and health, play a session, then iterate. Full porting guide: [SYSTEM-PORTING.md](SYSTEM-PORTING.md).

---

## Supported games (out of the box)

| System | Module | Notes |
|--------|--------|-------|
| D&D 5e | `systems/dnd5e/` | Full support — scripts, SRD dataset, character tools |
| Star Wars D6 (WEG 2e Revised) | `systems/swwegd6/` | Full support — character scripts, wound tracking, Force mechanics, SWAPI integration, Rebellion-era sample campaign |

**Adding your own:** Copy `systems/TEMPLATE.md` to `systems/<your-system>/system.md` and fill it in. See [SYSTEM-PORTING.md](SYSTEM-PORTING.md) for a compatibility breakdown of popular systems (Pathfinder 2e, Vampire: The Masquerade, Cyberpunk RED, Warhammer 40k).

---

## Perplexity Computer

If you're running sessions via **Perplexity Computer** (AI with file upload) rather than OpenCode, use the skill files in [`perplexity-skills/`](perplexity-skills/):

| File | Purpose |
|---|---|
| `SKILL-gm-core.md` | GM persona, craft principles, session structure |
| `SKILL-swwegd6-rules.md` | Complete WEG D6 mechanics — dice, wounds, Force, combat, advancement |
| `SKILL-swwegd6-campaign.md` | Rebellion-era sample campaign, NPCs, SWAPI integration guide, sourcebook extension format |
| `SKILL-session-start.md` | Session start checklist, copy-paste prompt, between-session tracking |

**Upload all four files** to Perplexity Computer at the start of each session. Use the copy-paste session start prompt in `SKILL-session-start.md` to give the GM your current character state. Add optional sourcebook extension files (`SKILL-swwegd6-[name].md`) to bring in Galaxy Guides, Heroes & Rogues, or any other WEG supplement.

---

## Setup

### 1. Install OpenCode

[opencode.ai](https://opencode.ai) — supports Anthropic, OpenAI, Google, Ollama, LM Studio, and any OpenAI-compatible endpoint.

### 2. Clone this repo

```bash
git clone https://github.com/Bobby-Gray/open-tabletop-gm
cd open-tabletop-gm
```

### 3. Install Python dependencies (display companion only)

The core scripts have no dependencies. The optional display companion requires:

```bash
cd display
pip3 install -r requirements.txt
```

### 4. Configure OpenCode

Point OpenCode at this skill by adding the following to your OpenCode config (`~/.config/opencode/opencode.json`):

```json
{
  "instructions": [
    "/path/to/open-tabletop-gm/no_think.md",
    "/path/to/open-tabletop-gm/paths.md",
    "/path/to/open-tabletop-gm/SKILL-commands.md",
    "/path/to/open-tabletop-gm/SKILL-branches.md"
  ]
}
```

`SKILL.md` (the GM persona) is not loaded at startup — it is read from disk the first time a session is loaded, keeping the standing system prompt lean (~2,300 tokens). See [docs/LLM-GUIDE.md](docs/LLM-GUIDE.md) for why this matters on smaller models.

For a local model via LM Studio, add your provider config:

```json
{
  "provider": {
    "lmstudio": {
      "npm": "@ai-sdk/openai-compatible",
      "name": "LM Studio (local)",
      "options": {
        "baseURL": "http://localhost:1234/v1"
      },
      "models": {
        "your-model-id": {
          "name": "Your Model Name"
        }
      }
    }
  }
}
```

### 5. Start a campaign

```
/gm new <campaign-name>
```

The skill walks you through world creation, tone selection, and character setup. Everything is saved to plain Markdown files you can read and edit directly.

For Star Wars D6 specifically:

```
/gm new my-rebellion-campaign swwegd6
```

Or open a Perplexity Computer session, upload the four files from `perplexity-skills/`, and use the session start prompt.

---

## Versioning & updates

Releases are tracked in [`CHANGELOG.md`](CHANGELOG.md) and the current version is in [`VERSION`](VERSION). The skill follows [semantic versioning](https://semver.org/) — `MAJOR.MINOR.PATCH`. Breaking changes that require campaign-data migration bump MAJOR; new opt-in features bump MINOR; bug fixes bump PATCH.

**To check for updates:**

```
/gm update --check    # shows local vs. remote version + commit diff, no pull
/gm update            # pulls if you're behind (fast-forward only; refuses on dirty tree)
```

The `--check` output includes both sides' version strings so you can see at a glance whether you've fallen behind. After pulling, restart your GM session so new skill files load.

This project tracks behind [claude-dnd-skill](https://github.com/Bobby-Gray/claude-dnd-skill) on Claude-specific features and runs ahead on LLM-agnostic concerns. Where the upstream version uses Haiku-backed extraction or Claude API tool calls, this fork either ports a deterministic equivalent or defers until one exists.

---

## Other ways to play

Two sibling projects share this framework's design DNA, in case neither this nor the Claude-specific version fit how you want to set up:

- [claude-dnd-skill](https://github.com/Bobby-Gray/claude-dnd-skill) — Claude Code-specific version with deeper tool-call integration. The right home if you're running Claude.
- [neuralinitiative.ai](https://neuralinitiative.ai) — hosted browser version. Sign in with Google, top up a balance, play. Same model-picker philosophy, refined web GUI, no install. Costs more per session than running your own keys, in exchange for zero setup.

All three share the same maintainer and design DNA — pick the one that matches how you want to set up.

---

## Quick Start

**Improvised campaign** — GM generates world and narrative arc:

```
/gm new my-campaign          # generates world, factions, NPCs, optional story arc
/gm character new            # create a character
/gm load my-campaign         # start a session
```

**Structured campaign** — import a pre-written module:

```
/gm import module.pdf my-campaign   # extract structure and build campaign files
/gm load my-campaign                # start a session — GM enforces the arc beats
```

Once loaded, type naturally — no `/gm` prefix needed. The GM interprets all input as in-game action.

---

## Commands

| Command | What it does |
|---------|-------------|
| `/gm new <name> [system]` | Create a new campaign with world generation |
| `/gm load <name>` | Load an existing campaign and resume |
| `/gm save` | Write session events to log, update state |
| `/gm end` | Save and close session |
| `/gm abandon` | Exit without saving — discards all unsaved changes from this session |
| `/gm list` | List all campaigns |
| `/gm import <filepath> [name]` | Import a pre-written campaign from PDF, markdown, DOCX, or plain text |
| `/gm character new` | Create a new character (uses system module for rules) |
| `/gm character sheet [name]` | Display character sheet |
| `/gm character import <name>` | Import a character from another campaign |
| `/gm characters` | List all characters in the global roster |
| `/gm level up [name]` | Level up a character (D&D / level-based systems) |
| `/gm npc [name]` | Generate or portray an NPC |
| `/gm roll <notation>` | Roll dice: `d20`, `2d6+3`, `d20 adv` |
| `/gm combat start` | Start combat with initiative |
| `/gm rest short\|long` | Short or long rest |
| `/gm recap` | In-character session recap |
| `/gm world` | Display world notes |
| `/gm quests` | Display active quests and open threads |
| `/gm tutor on\|off` | Toggle learning mode hints |
| `/gm arc [status\|advance\|revise\|view]` | Manage the campaign narrative arc |
| `/gm display on [--lan]` | Start the cinematic display companion (optionally in LAN mode) |
| `/gm display off` | Stop the display companion |
| `/gm path [<new>\|reset]` | View or relocate campaign storage via `GM_CAMPAIGN_ROOT` |
| `/gm update [--check]` | Pull the latest skill changes from `origin/main` (refuses on dirty tree, fast-forward only) |
| `/gm graph init` | Initialize the campaign relationship graph (proposes seed nodes + edges; asks for approval) |
| `/gm graph scene-context --place <id> [--present id1,id2]` | Focused subgraph for the current scene; primary in-session query |
| `/gm graph add-edge --from <id> --to <id> --type T --since N` | Record a relationship shift mid-session |
| `/gm graph close-edge --id <id> --at-session N` | Mark an edge as ended (alliance broke, NPC moved away, etc.) |

---

## Narrative arc system

Both campaign modes use the same six-beat three-act structure tracked in `state.md`. Arc type determines how it's populated.

### Improvised (type: dynamic)

Generated at `/gm new` from the world's threat, factions, and setting. Beats are defined by `what_changes` — the narrative consequence that must land — not by a specific scene or event. The GM stays flexible on *how* each beat arrives while committing to *that* it must.

| Act | Beat | What it marks |
|-----|------|---------------|
| 1 | Inciting Incident | The threat becomes personal |
| 1 | Complication | The problem is bigger than it first appeared |
| 2 | Midpoint Shift | What the party thought they were doing changes |
| 2 | All Is Lost | A genuine setback — something fails or collapses |
| 3 | Final Confrontation | The decisive moment the campaign turns on |
| 3 | Resolution | What's different about the world and characters after |

Arc beats are tracked at `/gm end` and marked complete via `/gm arc advance`. When a player choice redirects the story, `/gm arc revise` updates outstanding beats to fit the new direction. When all six beats resolve, a new arc can be generated from the consequences of the first — same world, new story question.

### Structured (type: structured)

Populated by `/gm import` from the source material. Acts contain chapter-level key beats, telegraph scenes that set up each beat naturally, and branching notes. The GM telegraphs before delivering any required beat and steers with world pressure rather than hard walls when players drift.

Both arc types are fully compatible with all system modules and the display companion.

---

## Display companion

An optional Flask web app that renders your session as a cinematic full-screen display — stat sidebar, live effect tracking, player input panel, animated backgrounds.

```bash
bash display/start-display.sh          # localhost, HTTP (default)
bash display/start-display.sh --lan    # LAN mode (phones, tablets, TV), HTTP
bash display/start-display.sh --lan --tls  # LAN mode, HTTPS (public/untrusted networks)
open http://localhost:5001
```

Runs entirely independently of the LLM. If the display isn't running, all scripts fail silently — nothing breaks.

> Screenshots below show the D&D 5e system module (included). The display companion works identically with any system module.

![Session display with stat sidebar and NPC dialogue](docs/screenshots/screenshot-npc-dialogue.png)

![Full display view with combat roll and player input panel](docs/screenshots/screenshot-display.png)

| Stat sidebar | Character sheet |
|---|---|
| ![Stat sidebar](docs/screenshots/sidebar-card.png) | ![Character sheet modal](docs/screenshots/character-sheet-modal.png) |

See [display/README.md](display/README.md) for full documentation.

---

## File layout

```
open-tabletop-gm/
  SKILL.md              ← GM persona and craft (read at session load, not startup)
  SKILL-commands.md     ← command signature reference (always in context)
  SKILL-branches.md     ← branch router: maps each command to its procedure (always in context)
  no_think.md           ← suppresses chain-of-thought preamble on local models
  paths.md              ← absolute path constants for this installation
  SYSTEM-PORTING.md     ← guide for adding new game systems
  perplexity-skills/    ← uploadable skill files for Perplexity Computer sessions
    SKILL-gm-core.md
    SKILL-swwegd6-rules.md
    SKILL-swwegd6-campaign.md
    SKILL-session-start.md
  systems/
    dnd5e/              ← D&D 5e reference implementation
      system.md
      ability-scores.py
      character.py
      lookup.py
      data/             ← bundled SRD dataset
    swwegd6/            ← WEG Star Wars D6 (2e Revised)
      system.md         ← rules context loaded at session start
      character.py      ← character creation, sheet, CP/FP/DSP tracking
      swapi_lookup.py   ← canonical film data via SWAPI
      README.md
    TEMPLATE.md         ← scaffold for building a new system module
  scripts/              ← universal scripts (dice, combat, tracker, calendar, search)
  display/              ← cinematic display companion (Flask)
  templates/            ← blank campaign file templates
  data/campaigns/       ← sample campaign data
    rebellion-era-sample/
      state.md / world.md / npcs.md
```

Campaign data lives outside the repo:
```
~/.local/share/open-tabletop-gm/campaigns/<name>/
  state.md / world.md / npcs.md / session-log.md / characters/
```

---

## Performance on local / smaller models

The Python toolchain offloads everything mechanical — dice, HP math, initiative, timed effects, conditions — so the LLM only handles narration and judgment calls. This means smaller models remain functional even when creative output is limited.

**Practical hardware guidance:**
- **MacBook Air / 24GB unified memory:** Local inference below 70B is unreliable for session load. Use OpenRouter instead — ~$0.01–0.05/session on paid endpoints.
- **64GB+ machine (M3 Max, M4 Max, or equivalent):** Local inference viable at 70B. Qwen3-70B recommended.
- **Multi-GPU workstation:** All local models viable.

See [docs/LLM-GUIDE.md](docs/LLM-GUIDE.md) for full probe results, token usage data, and hardware recommendations.

---

## Contributing

System modules for new games are the most valuable contribution. If you've built and tested a module for a system not listed here, a PR adding `systems/<your-system>/` is welcome. Include at minimum a filled-in `system.md` and a note in the PR about what you tested and how well it worked.

See [CONTRIBUTING.md](CONTRIBUTING.md) for the full guide and the contribution licensing handshake.

---

## License

[AGPL-3.0-or-later](LICENSE). Copyright (c) 2026 Neural Initiative LLC.

Self-hosting and modification are explicitly welcome — fork, run, change as you like. The AGPL specifically protects against re-hosting this as a closed-source SaaS without sharing modifications back. For most users this distinction never matters.
