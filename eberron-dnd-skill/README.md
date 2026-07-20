# eberron-dm

An **Eberron-default, filesystem-only Dungeon Master** skill for running persistent
Dungeons & Dragons 5th Edition campaigns with an AI agent (Claude Code, OpenCode, or
any agent that can read a skill and run local Python + shell).

It is a standalone, more comprehensive descendant of two upstream projects (see
**Credits**), rebuilt to:

- **Default to Eberron.** Ships a **bundled canonical lorebook** (`skills/dnd/lore/`) —
  distilled reference briefs plus a de-duplicated full-text corpus of Dragonshards
  articles, prestige classes, adventures, statblocks, 998 YK news, sourcebook crunch,
  and complete rulebook texts — all searchable **offline** with `lore_search.py`.
- **Persist everything on the local filesystem.** Campaigns live under
  `~/eberron-dnd/campaigns/<name>/`. No cloud, no external services, no display
  companion, no network calls.
- **Bundle the 5e SRD (2014)** as structured JSON for instant monster / spell / item /
  rule lookups via `lookup.py`.
- **Put dice in the player's hands by default** (see below).

---

## Dice convention — players roll their own dice (default `roll_mode: players`)

This skill **does not roll dice for player characters.** By default the DM narrates,
then issues an explicit **`ROLL_REQUEST`** naming the exact die, count, modifier, and
target, and **waits** for you to report the result. Roll however you like — physical
dice or an online roller such as **[rolladie.net](https://rolladie.net/)**.

- Every player-facing roll is a callout, e.g.
  `ROLL_REQUEST: roll 1d20, add +5 (Athletics), vs DC 15` or `Damage: roll 2d6, add +3`.
- **Advantage/disadvantage:** *"roll 1d20 twice, tell me both numbers"* — the DM takes
  the higher (advantage) or lower (disadvantage).
- After a callout the DM **stops and waits** for your number. It never rolls for a PC,
  never assumes a result, never auto-resolves; if no number comes back it re-asks.
- **The DM rolls only NPC / monster / secret dice**, via `scripts/dice.py`, showing the
  math inline.
- **Player rolls** include ability checks, attacks, damage, saving throws, **death
  saves**, **concentration saves**, and **the PC's initiative**. (NPC/monster initiative
  is DM-rolled.)

---

## Install

The skill directory is `skills/dnd/` (frontmatter `name: dnd`). Install the whole repo
as a plugin, or point your agent at the skill directory directly.

### Claude Code (plugin)
Place this repo where Claude Code discovers plugins (the plugin manifest is
`.claude-plugin/plugin.json`, name `eberron-dm`). Invoke the skill as `/dm:dnd` or just
describe what you want once a campaign is loaded.

### OpenCode / generic agents
Load `skills/dnd/SKILL.md` as the system/skill instructions. Ensure the agent can:
- **Read/Write/Edit** files, **Glob**, and run **Bash** (Python 3.9+).
- Reach the bundled `scripts/`, `data/`, and `lore/` directories (they resolve
  relative to `SKILL.md` via `CLAUDE_SKILL_DIR`, falling back to the file's own path).

No pip installs are required for the core loop; scripts use only the Python standard
library. (`verb_table_seed.yaml` is read with a tiny built-in parser; PyYAML is
optional.)

### Where your data lives
```
~/eberron-dnd/
  campaigns/<name>/
    state.md  world.md  npcs.md  session-log.md
    characters/<pc>.md
    tracker.json  calendar.json  graph.json  …
  .runtime/            # autosave markers, name registry
```
Override the root with **`GM_CAMPAIGN_ROOT`** (e.g.
`export GM_CAMPAIGN_ROOT=~/Dropbox/eberron-dnd`). The legacy `DND_CAMPAIGN_ROOT` is
honored as a fallback for compatibility with the upstream skill.

---

## What's in the box

```
eberron-dnd-skill/
├─ .claude-plugin/plugin.json     # plugin manifest (name: eberron-dm)
├─ README.md  LICENSE             # AGPL-3.0-or-later
└─ skills/dnd/
   ├─ SKILL.md                    # the DM operating manual (READ FIRST)
   ├─ SKILL-commands.md           # every /dm command
   ├─ SKILL-scripts.md            # every helper script
   ├─ references/                 # merged, authoritative rules & craft (read-when guided)
   │   ├─ canonical-dm-rules.md   # the space-prompt rules — Prime Directives, response format, NEVER DO
   │   ├─ rules-5e.md  gm-craft.md  commands.md
   │   └─ filesystem-persistence.md
   ├─ lore/                       # THE canonical Eberron lorebook (see lore/INDEX.md)
   │   ├─ INDEX.md                # catalog + canon-precedence + lookup order
   │   ├─ *.md                    # distilled reference briefs
   │   └─ fulltext/               # full-text corpus + rulebooks/
   ├─ data/                       # dnd5e_srd.json, dnd5e_supplemental.json, srd-2014/*.json, graph/
   ├─ scripts/                    # Python helpers (dice, combat, xp, lookup, lore_search, …)
   └─ templates/                  # campaign file scaffolds (Eberron-flavored)
```

### The lorebook is canonical and extensible
`skills/dnd/lore/` is declared **the authoritative, most up-to-date Eberron canon** for
this skill. It **beats the model's training knowledge** and any external source. To
extend canon, drop a new `.md`/`.txt` file into `lore/fulltext/` and add one line to
`lore/INDEX.md` — it becomes searchable canon automatically. See `lore/INDEX.md` for the
full canon-precedence rule.

---

## Credits

This project stands on two open works, both **AGPL-3.0-or-later**, and is distributed
under the same license:

- **[neuralinitiative/claude-dnd-skill](https://github.com/neuralinitiative/claude-dnd-skill)**
  — the campaign-engine architecture, command surface, scripts, SRD build, and templates
  that this package adapts. Copyright © Neural Initiative LLC.
- **[Bobby-Gray/open-tabletop-gm](https://github.com/Bobby-Gray)** — the Eberron
  Dungeon Master / Lorekeeper reference approach and GM-craft material that informed the
  merged rules and distilled lore briefs.

The display companion, phone/TV mockups, autorun/TTS features, and all
Perplexity-specific tooling from the upstreams have been **removed**. This build is
filesystem-only.

D&D and Eberron are trademarks of Wizards of the Coast. Bundled SRD content is used under
the Open Gaming License / Creative Commons terms noted in the SRD file itself. Bundled
lore texts are included for personal tabletop use.
