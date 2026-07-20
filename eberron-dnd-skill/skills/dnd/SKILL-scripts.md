# Scripts Reference

Full syntax for all Python helper scripts. Load this file once at `/dm load`, then it stays
in context for the session. This build is **offline and filesystem-only** — there is no
display companion, no phone/dice server, and no network calls in play.

> **Path note:** commands below use `${CLAUDE_SKILL_DIR}` for the skill directory. This file
> is read verbatim, so that token is **not** auto-expanded — substitute the absolute skill-
> dir path (from `SKILL.md`) before running, or the command fails with a broken `/scripts/…`
> path. Scripts also resolve their own location, so running them from the `scripts/`
> directory works too. Campaign data lives under the campaign root (`~/eberron-dnd` by
> default, or `$GM_CAMPAIGN_ROOT`; legacy `$DND_CAMPAIGN_ROOT` honored).

---

## Dice Script — `scripts/dice.py`

**For NPC / monster / secret rolls only.** Under the default `roll_mode: players`, the DM
rolls **only** the DM's own dice with this script; **players roll their own PC dice
externally** (e.g. <https://rolladie.net/>) — you issue a `ROLL_REQUEST` callout and wait
for their number (see SKILL.md "Dice convention"). **Never sample dice mentally** — when it
*is* your roll (an NPC/monster/secret roll, or any roll under `roll_mode: auto`), always use
this script and show the math inline.

```bash
python3 ${CLAUDE_SKILL_DIR}/scripts/dice.py d20+5
python3 ${CLAUDE_SKILL_DIR}/scripts/dice.py 2d6+3
python3 ${CLAUDE_SKILL_DIR}/scripts/dice.py 4d6kh3        # ability score roll
python3 ${CLAUDE_SKILL_DIR}/scripts/dice.py d20 adv       # advantage
python3 ${CLAUDE_SKILL_DIR}/scripts/dice.py d20+3 dis     # disadvantage + modifier
python3 ${CLAUDE_SKILL_DIR}/scripts/dice.py d20 --silent  # returns integer only (hidden roll)
python3 ${CLAUDE_SKILL_DIR}/scripts/dice.py d20+4 --label "Goblin attack"
```

Flags nat 20 (CRITICAL HIT) and nat 1 (FUMBLE) automatically. Use `--silent` for hidden
NPC/secret rolls where you narrate only the perceived result. **Do not use this to resolve a
PC's attack, check, save, death save, concentration save, or the PC's own initiative under
`roll_mode: players`** — call for the roll and wait. (NPC/monster initiative is DM-rolled via
`combat.py init`.)

---

## Ability Scores Script — `scripts/ability-scores.py`
```bash
python3 ${CLAUDE_SKILL_DIR}/scripts/ability-scores.py roll
python3 ${CLAUDE_SKILL_DIR}/scripts/ability-scores.py pointbuy
python3 ${CLAUDE_SKILL_DIR}/scripts/ability-scores.py pointbuy --check STR=15 DEX=10 CON=15 INT=8 WIS=11 CHA=12
python3 ${CLAUDE_SKILL_DIR}/scripts/ability-scores.py modifiers STR=15 DEX=10 CON=15 INT=8 WIS=11 CHA=12
```
(Note the hyphen in the filename.) Roll mode generates 3 arrays (4d6kh3 × 6 each). Point buy
mode prints the cost table; `--check` validates against the 27-point budget.

---

## XP Script — `scripts/xp.py`
Awards XP for combat and qualifying non-combat encounters. Reads character files from the
campaign directory and updates XP. All tables (difficulty thresholds, CR→XP, monster
multipliers, level advancement) are codified in the script — the DM only decides the
difficulty tier or provides a monster list. (No display push in this build.)

```bash
# Preview — no files modified:
python3 ${CLAUDE_SKILL_DIR}/scripts/xp.py calc --level 3 --players 2 --difficulty hard --type combat
python3 ${CLAUDE_SKILL_DIR}/scripts/xp.py calc --level 3 --players 2 --monsters "goblin:1/4:3,hobgoblin:1:1"

# Award after a combat encounter — difficulty-rated (when a full monster list is unavailable):
python3 ${CLAUDE_SKILL_DIR}/scripts/xp.py award \
  --campaign <name> --characters "Aldric,Vesper" --difficulty hard --type combat

# Award after a combat encounter — exact CR calculation (preferred):
python3 ${CLAUDE_SKILL_DIR}/scripts/xp.py award \
  --campaign <name> --characters "Aldric,Vesper" \
  --monsters "goblin:1/4:3,hobgoblin:1:1" --note "Ambush in the alley"

# Award for a qualifying non-combat encounter:
python3 ${CLAUDE_SKILL_DIR}/scripts/xp.py award \
  --campaign <name> --characters "Aldric,Vesper" --difficulty medium --type noncombat \
  --note "guild informant interrogation"
```

**Difficulty tiers:** `easy` `medium` `hard` `deadly`. **Types:** `combat` `noncombat`.
**Monster CR formats:** `1/4`, `0.25`, `1/2`, `1/8`, or integer. **Count:** omit for 1
(`"dragon:10"`), explicit for groups (`"goblin:1/4:3"`). **Multiplier** (auto): ×1 (1),
×1.5 (2), ×2 (3–6), ×2.5 (7–10), ×3 (11–14), ×4 (15+). `award` updates the character file XP
field and flags LEVEL UP PENDING when a threshold is crossed. **After awarding XP, update
each affected PC's memory card** (`memory/<pc>-card.md`) if the level or key resources change.

---

## Combat Script — `scripts/combat.py`
```bash
# Roll initiative for ALL combatants (DM-rolled, both PCs and NPCs) and print tracker:
python3 ${CLAUDE_SKILL_DIR}/scripts/combat.py init '<JSON>'
# JSON: [{"name":"Vesper","dex_mod":2,"hp":12,"ac":16,"type":"pc"}, ...]

# Reprint tracker from saved state:
python3 ${CLAUDE_SKILL_DIR}/scripts/combat.py tracker '<JSON>' <round_num>

# Resolve a single NPC/monster attack (DM roll):
python3 ${CLAUDE_SKILL_DIR}/scripts/combat.py attack --atk 4 --ac 15 --dmg 2d6+2
```
`init` outputs a `STATE_JSON:` line — store it in `state.md → ## Active Combat` between
turns. Initiative is DM-rolled for everyone regardless of `roll_mode`; **PC attacks and
damage during the fight are still player-rolled** (issue `ROLL_REQUEST` callouts).

---

## Character Script — `scripts/character.py`
```bash
# Full stat block from raw scores:
python3 ${CLAUDE_SKILL_DIR}/scripts/character.py calc --class fighter --level 1 \
    STR=15 DEX=10 CON=15 INT=9 WIS=11 CHA=14 \
    --proficient STR CON Athletics Intimidation Perception Survival

# Level-up HP and bonus calculation:
python3 ${CLAUDE_SKILL_DIR}/scripts/character.py levelup --class fighter --from 1 --hp-roll 7 --con-mod 2

# XP tracking:
python3 ${CLAUDE_SKILL_DIR}/scripts/character.py xp --level 1 --gained 150
```
After any character-file change, **update the PC memory card the same turn** (see the PC
Brain in SKILL.md / `references/filesystem-persistence.md § 8`).

---

## Lore Search — `scripts/lore_search.py`
Searches the **bundled Eberron lorebook** (`lore/` — distilled briefs + `fulltext/`
articles + `fulltext/rulebooks/`). This is the authoritative canon lookup for Eberron and
non-SRD content (use `lookup.py` first for SRD mechanics). Case-insensitive; ranks results by
match count. Zero network, zero LLM.

```bash
python3 ${CLAUDE_SKILL_DIR}/scripts/lore_search.py "Phiarlan"           # search everything
python3 ${CLAUDE_SKILL_DIR}/scripts/lore_search.py "Silver Flame" --list # matching files only
python3 ${CLAUDE_SKILL_DIR}/scripts/lore_search.py "warforged" -n 5      # cap results
python3 ${CLAUDE_SKILL_DIR}/scripts/lore_search.py "beholder" --files rulebooks  # restrict to rulebook texts
python3 ${CLAUDE_SKILL_DIR}/scripts/lore_search.py "dragon prophecy" --any        # match ANY term (default: all)
```
Flags: `--list` (files only), `--files <substring>` (restrict to paths containing the
substring, e.g. `news`, `rulebooks`, `dragonshards`), `--any` (OR instead of AND), `-n N`
(max results). The corpus is **extensible** — dropping a file into `lore/fulltext/` (plus a
line in `lore/INDEX.md`) makes it searchable canon automatically, no rebuild. Name the
matched file in your SOURCE line.

---

## Tracker Script — `scripts/tracker.py`
Tracks conditions, concentration, timed effects, and death saves. State persists at
`<campaign>/tracker.json`.

```bash
CAMP=my-campaign

# Timed effects — duration: 10r (rounds), 60m (minutes), 8h (hours), indef; append 'conc' for concentration
python3 ${CLAUDE_SKILL_DIR}/scripts/tracker.py -c $CAMP effect start "Vesper" "Web" 10r conc
python3 ${CLAUDE_SKILL_DIR}/scripts/tracker.py -c $CAMP effect start "Aldric" "Hunter's Mark" indef
python3 ${CLAUDE_SKILL_DIR}/scripts/tracker.py -c $CAMP effect end   "Vesper" "Web"
python3 ${CLAUDE_SKILL_DIR}/scripts/tracker.py -c $CAMP effect tick  "Vesper"   # on actor's turn — decrements, prints expiry

# Conditions
python3 ${CLAUDE_SKILL_DIR}/scripts/tracker.py -c $CAMP condition add "Aldric" poisoned
python3 ${CLAUDE_SKILL_DIR}/scripts/tracker.py -c $CAMP condition remove "Aldric" poisoned
python3 ${CLAUDE_SKILL_DIR}/scripts/tracker.py -c $CAMP condition clear "Aldric"

# Concentration (auto-clears previous when switching spells)
python3 ${CLAUDE_SKILL_DIR}/scripts/tracker.py -c $CAMP concentrate "Vesper" "Bless"
python3 ${CLAUDE_SKILL_DIR}/scripts/tracker.py -c $CAMP concentrate "Vesper" break

# Death saves (player-rolled d20 — record the reported result)
python3 ${CLAUDE_SKILL_DIR}/scripts/tracker.py -c $CAMP saves "Aldric" success
python3 ${CLAUDE_SKILL_DIR}/scripts/tracker.py -c $CAMP saves "Aldric" failure
python3 ${CLAUDE_SKILL_DIR}/scripts/tracker.py -c $CAMP saves "Aldric" stable
python3 ${CLAUDE_SKILL_DIR}/scripts/tracker.py -c $CAMP saves "Aldric" reset

# Status / clear
python3 ${CLAUDE_SKILL_DIR}/scripts/tracker.py -c $CAMP status
python3 ${CLAUDE_SKILL_DIR}/scripts/tracker.py -c $CAMP clear           # conditions + concentration + effects
python3 ${CLAUDE_SKILL_DIR}/scripts/tracker.py -c $CAMP clear --all     # also clears death saves
```
**When to run:** condition applied/removed; concentration begins/lost (immediately); PC drops
to 0 HP; each death save reported by the player; end of encounter → `clear`.

---

## Calendar Script — `scripts/calendar.py`
Defaults to the **Galifar calendar** for Eberron campaigns (12 months of 28 days, 7-day week,
YK dating). Set it up at `/dm new`.

```bash
CAMP=my-campaign

# One-time setup (Eberron / Galifar calendar):
python3 ${CLAUDE_SKILL_DIR}/scripts/calendar.py -c $CAMP init \
    --date "8 Vult 998" --time "morning" \
    --months "Zarantyr,Olarune,Therendor,Eyre,Dravago,Nymm,Lharvion,Barrakas,Rhaan,Sypheros,Aryth,Vult" \
    --month-length 28 \
    --day-names "Sul,Mol,Zol,Wir,Zor,Far,Sar"

# Time advancement
python3 ${CLAUDE_SKILL_DIR}/scripts/calendar.py -c $CAMP advance 8 hours
python3 ${CLAUDE_SKILL_DIR}/scripts/calendar.py -c $CAMP advance 2 days
python3 ${CLAUDE_SKILL_DIR}/scripts/calendar.py -c $CAMP rest short   # +1 hour
python3 ${CLAUDE_SKILL_DIR}/scripts/calendar.py -c $CAMP rest long    # +8 hours

# Query / manual set
python3 ${CLAUDE_SKILL_DIR}/scripts/calendar.py -c $CAMP now
python3 ${CLAUDE_SKILL_DIR}/scripts/calendar.py -c $CAMP set "22 Vult 998" evening
python3 ${CLAUDE_SKILL_DIR}/scripts/calendar.py -c $CAMP time night
```
**When to run:** after every rest; after significant travel/time skip; keep `state.md`'s
in-world date in sync via `calendar.py set`.

---

## Campaign Search — `scripts/campaign_search.py`
Keyword search across the **campaign's own files** (not the lorebook — use `lore_search.py`
for that). Run this before loading full files into context to find a past event, NPC detail,
or thread.

```bash
CAMP=my-campaign
python3 ${CLAUDE_SKILL_DIR}/scripts/campaign_search.py -c $CAMP Phiarlan
python3 ${CLAUDE_SKILL_DIR}/scripts/campaign_search.py -c $CAMP "merchant letter" --files log,archive
python3 ${CLAUDE_SKILL_DIR}/scripts/campaign_search.py -c $CAMP VARETH Kel     # multi-keyword AND
python3 ${CLAUDE_SKILL_DIR}/scripts/campaign_search.py -c $CAMP Harwick -C 6   # more context lines
```
File keys: `state`, `log`, `archive`, `world`, `seeds`, `npcs`, `npcsfull`. Default files:
state, log, archive, world, npcs.

---

## Session Recap — `scripts/session_recap.py`
Deterministic state-diff between two character snapshots (HP/temp/level/hit dice/death saves/
conditions/concentration/exhaustion/inspiration/spell slots). Recaps are the single thing
most likely to be hallucinated, so this computes the change set from data. Reads
`<campaign>/characters/*.md` and merges live `tracker.json`. Zero LLM.

```bash
CAMP=my-campaign
python3 ${CLAUDE_SKILL_DIR}/scripts/session_recap.py snapshot --campaign $CAMP   # baseline (run at /dm end)
python3 ${CLAUDE_SKILL_DIR}/scripts/session_recap.py diff --campaign $CAMP       # one-paragraph diff, advances baseline
python3 ${CLAUDE_SKILL_DIR}/scripts/session_recap.py diff --campaign $CAMP --no-roll   # diff without advancing
python3 ${CLAUDE_SKILL_DIR}/scripts/session_recap.py diff --campaign $CAMP --json       # structured change list
python3 ${CLAUDE_SKILL_DIR}/scripts/session_recap.py diff-files before.json after.json
```

---

## Oracle — `scripts/oracle.py`
Dice-driven solo/improv oracles (Mythic chaos factor, Ironsworn yes/no, Random Event Focus,
scene-meaning word pairs). Seedable (`--seed N`). Chaos factor persists in
`state.md → ## Session Flags` as `chaos_factor: N`. Zero LLM.

```bash
CAMP=my-campaign
python3 ${CLAUDE_SKILL_DIR}/scripts/oracle.py chaos --campaign $CAMP
python3 ${CLAUDE_SKILL_DIR}/scripts/oracle.py chaos set --campaign $CAMP --value 7
python3 ${CLAUDE_SKILL_DIR}/scripts/oracle.py chaos adjust --campaign $CAMP --pc-lost
python3 ${CLAUDE_SKILL_DIR}/scripts/oracle.py ask --likelihood likely --campaign $CAMP
python3 ${CLAUDE_SKILL_DIR}/scripts/oracle.py event
python3 ${CLAUDE_SKILL_DIR}/scripts/oracle.py scene
```
Likelihoods: `sure-thing`, `likely`, `50/50`, `unlikely`, `no-way`. Verdict suffixes: `-and`
(extreme, on doubles), `-but` (qualified, near threshold).

---

## Campaign Graph — `scripts/campaign_graph.py` (+ `scripts/graph_extract_deterministic.py`)
Local-only typed-edge relationship graph at `<campaign>/graph.json`, supplementing the
markdown. Edges are time-stamped so historical state is recoverable. Full command surface in
`SKILL-commands.md → /dm graph`. Deterministic (zero-LLM) extraction pattern-matches the
session log against `data/graph/verb_table_seed.yaml`:

```bash
CAMP=my-campaign
python3 ${CLAUDE_SKILL_DIR}/scripts/campaign_graph.py scene-context --campaign $CAMP --place "<place>" --present "<npcs>" --hops 2 --at-session <N>
python3 ${CLAUDE_SKILL_DIR}/scripts/campaign_graph.py extract --campaign $CAMP --deterministic
python3 ${CLAUDE_SKILL_DIR}/scripts/campaign_graph.py extract --campaign $CAMP --deterministic --apply --min-confidence high
```

---

## SRD Data — `scripts/lookup.py` (+ `build_srd.py`)
The 5e SRD dataset is **bundled** at `${CLAUDE_SKILL_DIR}/data/dnd5e_srd.json` (plus
`data/srd-2014-complete.json (all 25 SRD resources merged in one file, keyed by resource name)`). No runtime download. Use `lookup.py` **first** for any monster,
spell, item, condition, or feature — before improvising from memory.

```bash
python3 ${CLAUDE_SKILL_DIR}/scripts/lookup.py monster "goblin"
python3 ${CLAUDE_SKILL_DIR}/scripts/lookup.py spell "fireball"
python3 ${CLAUDE_SKILL_DIR}/scripts/lookup.py item "cloak of protection"
python3 ${CLAUDE_SKILL_DIR}/scripts/lookup.py feature "sneak attack"
python3 ${CLAUDE_SKILL_DIR}/scripts/lookup.py condition "poisoned"
python3 ${CLAUDE_SKILL_DIR}/scripts/lookup.py monster "dragon" --all   # all fuzzy matches
python3 ${CLAUDE_SKILL_DIR}/scripts/build_srd.py --status              # dataset metadata
```
**Lookup order:** `lookup.py` (SRD mechanics) → `lore_search.py` (Eberron / non-SRD) → say so
and improvise per canon precedence. **When to use:** combat (monster stat blocks), spellcasting
(range/components/duration), conditions (rule text), loot/equipment, NPC generation.

---

## Continuity Autosave — `scripts/autosave_checkpoint.py`, `scripts/install_autosave_hook.py`
Behind-the-scenes continuity checkpoint so a context compaction never loses the player's
place. Two layers: the in-model micro-save cadence (always available — see SKILL.md and
`/dm autosave`) and an optional Stop-hook backstop.

```bash
python3 ${CLAUDE_SKILL_DIR}/scripts/install_autosave_hook.py            # enable Stop hook
python3 ${CLAUDE_SKILL_DIR}/scripts/install_autosave_hook.py --uninstall
python3 ${CLAUDE_SKILL_DIR}/scripts/install_autosave_hook.py --status
python3 ${CLAUDE_SKILL_DIR}/scripts/autosave_checkpoint.py --status     # active campaign + turn count
python3 ${CLAUDE_SKILL_DIR}/scripts/autosave_checkpoint.py --campaign <name> --snapshot-only
```
`autosave_checkpoint.py` reads the active campaign from `<runtime-dir>/active-campaign.json`
(written at `/dm load`) and the `autosave` flag from that campaign's `state.md`. No-ops when
no campaign is active or `autosave: off`. `--status` also answers "which campaign was I in?"
at the top of a new session.

---

## Paths — `scripts/paths.py`
Resolves code and data roots. Code: `skill_root()`. Data root: `GM_CAMPAIGN_ROOT`
(default `~/eberron-dnd`; legacy `DND_CAMPAIGN_ROOT` fallback).

```bash
python3 ${CLAUDE_SKILL_DIR}/scripts/paths.py campaign <name>   # print a campaign's dir
python3 ${CLAUDE_SKILL_DIR}/scripts/paths.py runtime-dir       # print the .runtime dir
```
Configure the root with `/dm path <new-path>` (wraps `path_config.py`).

---

## Lazy Corpus — `scripts/corpus_check.py`
Imported (structured) campaigns keep the full module text as a lazily-loaded layer
(`world-nodes.md`, `arc.md`, `source-index.md`, `source/<id>.md`). Validate the layout at the
end of `/dm import`:

```bash
python3 ${CLAUDE_SKILL_DIR}/scripts/corpus_check.py --campaign <name>
```
A campaign with no `source/` layer (dynamic/sandbox) is a clean no-op.

---

## Import — `scripts/import_campaign.py`
Extracts source text from a pre-written adventure (`.pdf .md .txt .markdown .docx`) for
`/dm import`. Prefers PyMuPDF for column-aware PDF segmentation (falls back to `pdftotext`).

```bash
python3 ${CLAUDE_SKILL_DIR}/scripts/import_campaign.py "<filepath>" --info    # word count, structure hints
python3 ${CLAUDE_SKILL_DIR}/scripts/import_campaign.py "<filepath>" --chunks  # total chunks
python3 ${CLAUDE_SKILL_DIR}/scripts/import_campaign.py "<filepath>" --chunk 0 # a single chunk
python3 ${CLAUDE_SKILL_DIR}/scripts/import_campaign.py "<filepath>"           # full text (short sources)
```

---

## Other maintenance scripts
- `scripts/build_supplemental.py --character <path>` — fetch non-SRD spells/features a
  character uses into `data/dnd5e_supplemental.json` (skips entries already present).
- `scripts/migrate_ruleset.py <campaign> --check | --ruleset 2014|2024 --yes` — stamp a legacy
  campaign with a ruleset field (idempotent; backs up `state.md` first).
- `scripts/path_config.py [set <path> | reset]` — view/configure `GM_CAMPAIGN_ROOT`.
