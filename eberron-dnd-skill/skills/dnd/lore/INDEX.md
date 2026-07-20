# Eberron Lorebook — INDEX & Canon Authority

This `lore/` directory is **THE canonical, most up-to-date lorebook** for this skill. It
is the authoritative source of Eberron truth for every campaign run here.

## CANON-PRECEDENCE RULE (read and obey)

When any two sources disagree about setting facts, apply this order — **higher wins**:

1. **Campaign state files** (`~/eberron-dnd/campaigns/<name>/` — `state.md`, `world.md`,
   `npcs.md`, `session-log.md`, character files). **What actually happened in play
   overrides everything.** If the campaign established it, it is true for that campaign.
2. **This bundled `lore/` corpus** (the distilled reference briefs **and** the full text
   under `lore/fulltext/`). This is the **authoritative current Eberron canon.** It
   **beats the model's training knowledge, any generic Eberron/D&D memory, and any
   external source.** If you "remember" Eberron lore differently from `lore/`, **`lore/`
   wins — never contradict it.** When lore shaped a scene, name the lore file in your
   SOURCE line.
3. **Bundled SRD / rules data** for mechanics (`data/srd-2014/*.json`,
   `data/dnd5e_srd.json`, and the rulebook texts in `lore/fulltext/rulebooks/`), accessed
   via `scripts/lookup.py` and `scripts/lore_search.py`.
4. **DM improvisation** — only when **none** of the above covers something. When you
   improvise a fact, **flag it as new canon** and **record it into the campaign's
   `world.md`** so it persists and becomes level-1 canon for that campaign thereafter.

## Lookup order for any lore or rules question

1. **Rules/monsters/spells/items:** `python3 scripts/lookup.py <category> "<name>"` (SRD,
   offline) first.
2. **Eberron lore / non-SRD / setting content:** `python3 scripts/lore_search.py "<term>"`
   over this corpus. Restrict with `--files <substring>` (e.g. `--files news`,
   `--files rulebooks`) and use `--list` to see which files match.
3. **Distilled briefs** (this directory) give you the structured summary; **`fulltext/`**
   gives you the source article text to quote/cite.
4. If nothing matches, tell the player and improvise per precedence rule #4.

## The lorebook is EXTENSIBLE (maintenance note)

This corpus is **designed to grow.** To add new canon:

1. Drop a new `.md` or `.txt` file into `lore/fulltext/` (or append a
   `## <Title> (Source: <filename>)` section to an existing category file).
2. Add one line to the **Full-text corpus** table below in this INDEX.
3. That's it — `lore_search.py` walks the whole `lore/` tree, so the new document becomes
   **searchable canon automatically.** No rebuild step, no code change.

Keep new files plain text/markdown and reasonably sized (any single file well under the
100 MB per-file limit). The package budget is generous (≤50 MB **zipped**); text
compresses well, so adding lore is cheap.

---

## Distilled reference briefs (this directory)

Structured, DM-facing summaries. Each cites the source articles it distills.

| File | Covers |
|------|--------|
| `world-primer.md` | Eberron tone (noir/pulp), core truths, the Last War, magic-as-tech, the Prophecy, planes. |
| `dragonmarked-houses.md` | The thirteen (twelve + Tarkanan) Dragonmarked Houses, marks, guild services. |
| `nations.md` | The Five Nations + Cyre/Mournland, Mror Holds, Droaam, Darguun, Eldeen, Zilargo, Lhazaar, etc. |
| `religions.md` | Sovereign Host, Silver Flame (Purge, templars), Blood of Vol, Dark Six, druid sects, cults. |
| `organizations.md` | Emerald Claw, the Chamber, Heirs of Dhakaan, House Tarkanan, monastic orders, guilds. |
| `races-cultures.md` | Warforged, shifters, changelings, kalashtar, goblinoids, and cultural notes. |
| `psionics.md` | Dal Quor/Xoriat theory, Sarlona, kalashtar/Inspired, psionic classes and adaptation. |
| `prestige-classes.md` | Eberron/3.5e prestige classes distilled from the article PDFs. |
| `bestiary.md` | Fight-Club NPC/monster statblocks (by CR) + how to look up rulebook monsters. |
| `news-gazette.md` | 998 YK in-world newspaper stories as ready session hooks. |
| `adventure-hooks.md` | "Steal This Hook!" hooks, larger adventures/locales, elemental-cult conversions. |
| `rules-supplements.md` | Index/distill of the bundled rulebooks & crunch supplements. |
| `srd-quick-tables.md` | Frequently used open-license SRD tables (conditions, DCs, XP, etc.). |

## Full-text corpus (`lore/fulltext/`)

De-duplicated source text (90 unique documents). Each category `.md` file holds multiple
articles, each under a `## <Title> (Source: <filename>)` header. Search with
`lore_search.py`.

| File | Contents |
|------|----------|
| `fulltext/dragonshards-houses.md` | Dragonshards: Dragonmarked House articles (4). |
| `fulltext/dragonshards-religion-druids.md` | Dragonshards: Silver Flame, druids, lycanthropes, faiths (7). |
| `fulltext/dragonshards-organizations.md` | Dragonshards: Dhakaan, Children of Khyber, monastic orders, strike forces (7). |
| `fulltext/eberron-expanded-sourcebooks.md` | "Eberron Expanded" sourcebook-adaptation articles (5). |
| `fulltext/prestige-classes.md` | Prestige-class & character-option articles (8). |
| `fulltext/fight-club-statblocks.md` | Fully-statted NPC/monster articles (10). |
| `fulltext/adventure-hooks.md` | "Steal This Hook!" and adventure/locale articles (10). |
| `fulltext/news-998yk.md` | *Sharn Inquisitive* / *Korranberg Chronicle* 998 YK stories (18). |
| `fulltext/supplements-crunch.md` | Article-format crunch supplements (5). |

### `lore/fulltext/rulebooks/` (full rulebook texts)

`srd-ogl-5.1.txt` (open, quotable), `players-handbook-2024.txt`, `monster-manual-2024.txt`,
`monster-manual-2014.txt`, `monster-manual-expanded-1.txt`, `monster-manual-expanded-2.txt`,
`monster-manual-expanded-3.txt`, `dungeon-masters-guide-2014.txt`,
`fizbans-treasury-of-dragons.txt`, `players-handbook-2-3.5e.txt`, `complete-warrior.txt`,
`princes-of-the-apocalypse-5e.txt`, `dragon-delves-5e.txt`, `storm-kings-thunder-5e.txt`,
`reigns-homebrew-compendium.txt`, `adventure-ill-wind-in-friezford.txt`.

> **Copyright note:** the SRD/OGL text is open and may be quoted. Other rulebook texts are
> included for personal tabletop use — **distill mechanics in your own words; do not
> reproduce long verbatim passages** from copyrighted books.
