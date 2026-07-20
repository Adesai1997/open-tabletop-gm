# Command Procedures — `/dm …`

Full step-by-step procedures for all `/dm` slash commands. **Load this file at `/dm load`
/ `/dm new`, or before executing any slash command.** This build is offline and
filesystem-only: there is **no display companion, no phone/dice server, no network, and no
host-platform tools.** All state lives in local files under the campaign root
(`~/eberron-dnd` by default, or `$GM_CAMPAIGN_ROOT`; legacy `$DND_CAMPAIGN_ROOT` honored).

Throughout, `<root>` = the resolved campaign root and `<campaign>` = the campaign's
lowercase-hyphen name. Confirm the path with
`python3 ${CLAUDE_SKILL_DIR}/scripts/paths.py campaign <campaign>`.

**Global rules that apply to every command:**
- **Dice convention (default `roll_mode: players`):** you call for every PC roll with an
  explicit die callout (`ROLL_REQUEST: roll 1d20, add +MOD (skill), vs DC N`) and **STOP
  and wait** for the player's number — never roll a PC's dice. You roll only NPC/monster/
  secret dice via `dice.py`. Advantage/disadvantage: "roll 1d20 twice, tell me both."
  Full spec in SKILL.md and `references/canonical-dm-rules.md`.
- **Lore-first (canon precedence):** before inventing a monster, NPC, faction, location, or
  rule, search — `scripts/lookup.py` (SRD) then `scripts/lore_search.py` (Eberron lore). The
  bundled `lore/` corpus is authoritative canon and beats model memory. Name the file in
  your SOURCE line. See `lore/INDEX.md`.
- **PC Brain (never lose a PC):** each PC has a full sheet `characters/<pc>.md` **and** a
  compact card `memory/<pc>-card.md`. Read the card FIRST at load; refresh it at every save
  /end; update sheet + card **in the same turn** on any HP/level/item/bond change. See
  `references/filesystem-persistence.md § 8`.

---

## `/dm new <campaign-name> [theme]`
1. **Session setup — call `AskUserQuestion`, "Dice rolls?"** (see SKILL.md "Dice
   convention"):
   - `Players roll their own` (default) → write `roll_mode: players` to
     `state.md → ## Session Flags`. You call for each PC roll and wait — never auto-roll a PC.
   - `DM rolls everything openly` → write `roll_mode: auto`. You resolve PC rolls yourself
     with full math shown.
   Default to `roll_mode: players` if dismissed.
2. **Ruleset selection.** Ask: *"D&D 5e ruleset — **2014** (SRD 5.1, default) or **2024**
   (SRD 5.2, weapon mastery + origin feats + background ASIs + revised exhaustion)?"* Default
   `2014`. Write `**Ruleset:** 2014` (or `2024`) to the `state.md` header line.
3. `mkdir -p <root>/campaigns/<name>/characters <root>/campaigns/<name>/memory`
4. Copy and populate templates from `${CLAUDE_SKILL_DIR}/templates/` — `state.md`,
   `world.md`, `npcs.md`, `session-log.md`. Keep the `**Ruleset:**` field from step 2.
5. **Setting.** This skill **defaults to Eberron.** Unless the player asks for another
   setting, set `world.md → Setting: Eberron` and default the in-world calendar to the
   **Galifar calendar** (`templates/world.md` and `templates/state.md` carry the Eberron
   anchors and calendar block). Draw geography, factions, and tone from the bundled `lore/`
   corpus (`lore/world-primer.md`, `nations.md`, `dragonmarked-houses.md`, `religions.md`).
6. Ask: **party size** and **starting level**.
7. **Tone/Genre wizard** (pre-fill Eberron's noir/pulp default; ask to confirm or change):
   Tone, magic level, danger level. Randomize any blank via `dice.py` and log the roll in
   `world.md`.
8. **World foundations** — for Eberron, anchor on a settlement (e.g. a Sharn district), a
   nearby threat, and a mystery, all consistent with `lore/`. Seed
   `state.md → ## World State → In-world date` from the Galifar calendar (e.g. "8 Vult 998
   YK"). Initialize the calendar:
   `python3 ${CLAUDE_SKILL_DIR}/scripts/calendar.py -c <name> init --date "8 Vult 998" --months "Zarantyr,Olarune,Therendor,Eyre,Dravago,Nymm,Lharvion,Barrakas,Rhaan,Sypheros,Aryth,Vult" --day-names "Sul,Mol,Zol,Wir,Zor,Far,Sar"`.
9. **Factions & NPCs** — draw from `lore/organizations.md`, `dragonmarked-houses.md`, and
   the Dragonshards articles in `lore/fulltext/`. Give each NPC name, motivation, secret,
   flaw, disposition, and ≥2 relationships. Write full entries to `npcs.md`.
10. **Quest seeds** — 3–5 hooks from the threat, factions, mystery, and NPC motivations;
    mine `lore/adventure-hooks.md` and `lore/news-gazette.md` for ready material. Write to
    `world.md → ## Quest Seed Bank`.
11. **Campaign arc (optional).** Offer a committed dynamic arc (theme, resolution, Acts 1–3
    with 2 beats each — each beat's `what_changes` written as a CONSEQUENCE not an event,
    with a `world_pressure` move naming real entities). Write to `state.md → ## Campaign Arc`
    as `type: dynamic`, or `type: sandbox` if declined.
12. Write `state.md` with session count 0 and starting location.
13. **Seed the campaign graph** (optional but recommended): `/dm graph init <name>`.
14. Confirm creation; offer `/dm character new`.

---

## `/dm load <campaign-name>`
0. **Pick the campaign if none named.** If a name was given, use it. Otherwise `ls`
   `<root>/campaigns/` and **call `AskUserQuestion` "Which campaign?"** with existing names
   as options (most-recently-played first — sort by `state.md` mtime); "Other" lets them
   type. If none exist, say so and offer `/dm new`.
1. **Session setup — call `AskUserQuestion` "Dice rolls?"** Pre-fill from the saved
   `roll_mode` in `state.md` (else `players`):
   - `Players roll their own` → `roll_mode: players`. Call for each PC roll and wait.
   - `DM rolls everything openly` → `roll_mode: auto`. Resolve PC rolls yourself with math.
2. **Resolve & read the campaign directory** `<root>/campaigns/<name>/` (confirm with
   `paths.py campaign <name>`). If missing, tell the player and offer `/dm new`.
3. **Mark this campaign active:** write `{"name":"<name>"}` to
   `$(python3 ${CLAUDE_SKILL_DIR}/scripts/paths.py runtime-dir)/active-campaign.json`
   (autosave reads this). Read the ruleset:
   `python3 -c "import sys; sys.path.insert(0,'${CLAUDE_SKILL_DIR}/scripts'); from paths import campaign_ruleset; print(campaign_ruleset('<name>'))"`
   and pass `--ruleset <value>` to lookup/combat calls this session.
4. **Read files in this order** (see `references/filesystem-persistence.md`):
   1. **`state.md`** — Live State Flags first, then Current Situation, World State, DM Style
      Notes, Campaign Arc.
   2. **Each PC's `memory/<pc>-card.md`** — the compact PC brain, read BEFORE the full
      sheet. This is the compaction-resilient recall of HP/resources/bonds/relationships.
   3. `world.md` (full — Eberron foundations, factions, nodes).
   4. `npcs.md` (index; read a full NPC entry before voicing that NPC).
   5. `characters/*.md` (full sheets, for detail the card does not carry).
   - Also read `SKILL-scripts.md`, `references/canonical-dm-rules.md`,
     `references/rules-5e.md`, `references/filesystem-persistence.md`, and `lore/INDEX.md`.
5. **Optional host-memory query (Mode B).** If the host provides persistent memory, query it
   per PC (`eberron:<name>:pc:<pc>`) as a recall accelerator. On any conflict, the filesystem
   card wins. This build ships no such tool — skip silently if none exists.
6. **Recalc script state if needed.** If `tracker.json` / `calendar.json` are absent,
   re-init the calendar from `state.md`'s in-world date (step 8 of `/dm new`).
7. **Pull scene-context from the graph** (skips cleanly if uninitialized):
   `python3 ${CLAUDE_SKILL_DIR}/scripts/campaign_graph.py scene-context --campaign <name> --place "<current-location>" --present "<NPCs likely present>" --hops 2 --at-session <N>`.
8. **Optional mechanical recap diff:**
   `python3 ${CLAUDE_SKILL_DIR}/scripts/session_recap.py diff --campaign <name>` — a
   deterministic HP/resource change line since last snapshot.
9. Deliver **one in-character paragraph** recapping the current situation **from the freshly
   read files** — where the party is, what's at stake, what was last happening.
10. Enter active DM mode — no `/dm` prefix needed from here.

---

## `/dm import <filepath> [campaign-name]`
Import a pre-written adventure (`.pdf .md .txt .markdown .docx`) into a playable campaign.

1. **Extract source text:** `python3 ${CLAUDE_SKILL_DIR}/scripts/import_campaign.py "<filepath>" --info`.
   If word count > 4000, chunk it (`--chunks`, then `--chunk N`); otherwise read in full.
   (PDF extraction prefers PyMuPDF; if it prints a `pip3 install pymupdf` notice, tell the
   user and re-run — it falls back to `pdftotext` with weaker segmentation.)
2. **Analyze structure:** title/system, structure type (linear / hub-and-spoke /
   faction-web), acts & chapters, key beats, locations, NPCs, factions, quest hooks,
   starting conditions.
3. **Confirm campaign name** (suggest from the title if not supplied).
4. **Show a summary and confirm** before writing any files (title, type, act/chapter/beat
   counts, NPC/faction/location counts, campaign dir).
5. **Create files** on confirmation:
   - `mkdir -p <root>/campaigns/<name>/characters <root>/campaigns/<name>/memory <root>/campaigns/<name>/source`
   - Copy templates. Write `world.md` (foundations, three truths, threat arc, factions),
     `world-nodes.md` (quest bank + adventure nodes — lazy, not read at load), `npcs.md`
     (index) + full NPC entries, `arc.md` (full act/chapter tree with `source_ref` per
     chapter), and `state.md` (current situation, world state, `## Campaign Arc` with
     `type: structured` pointer only — current + next chapter window).
   - Write the **lazy source corpus**: `source/<chapter-id>.md` per chapter, plus
     `source-index.md`. Validate: `python3 ${CLAUDE_SKILL_DIR}/scripts/corpus_check.py --campaign <name>`.
   - **Eberron cross-check:** where the imported module names factions, deities, or
     locations that exist in `lore/`, prefer the bundled canonical spelling/detail and note
     any conflict.
6. **Gap-fill wizard:** ask for anything the source left ambiguous (starting level, party
   size, in-world date, tone).
7. **Confirm** files written; offer `/dm character new` or `/dm load <name>`.

---

## `/dm save`
Write session events to `session-log.md`; update `state.md` (location, active quests, party
HP/resources, recent events, **Live State Flags**); update any changed `characters/*.md`;
mirror each changed character to the global roster (`<root>/characters/<name>.md`).

- **Refresh each PC's memory card.** After updating a sheet, rewrite
  `memory/<pc>-card.md` so it matches (identity, HP/AC, resources, signature items,
  bonds/goals/flaws, key relationships & NPC attitudes, unresolved threads). Card and sheet
  must never drift. *(Optional Mode B: if a host memory facility exists, mirror the card
  text there — one entry per PC, updated not duplicated.)*
- **Update `## Live State Flags`** — the compaction anchor: each PC's cover + status,
  non-neutral faction stances, notable NPC dispositions, resource watchpoints (warlock pact
  slots, attunement /3, active concentration, low consumables). Correct anything that was
  wrong in the prior save.
- **Inspiration** persists across sessions and is not cleared by a long rest — record it in
  the party status line and on the card.
- **Structured (imported) campaigns:** when a chapter advances, mark it `complete` in
  `arc.md`, set the new chapter `current`, and update the `state.md` arc window
  (`current_chapter`, detail, `next_chapter`, `outstanding_beats`).
- **Faction Moves:** update `state.md → ## Faction Moves` — one line per active faction
  answering "what did they do while the party was occupied?" (draw plausible moves from
  `lore/` factions).
- **Session-log archival** (after session count > 3): keep the 2 most recent full entries
  in `session-log.md`; move older entries to `session-log-archive.md` (append, never
  delete). Extract a 3–5 bullet continuity summary per archived session into
  `state.md → ## Continuity Archive` (mechanical changes, plot beats, disclosed content,
  atmospheric/decision moments — omit pure-relational restatements the graph already holds).
- **Graph relationship-shift sweep:** scan this session's narration for new alliances,
  betrayals, movements, secrets learned, or threads ended; draft `add-edge`/`close-edge`
  calls with `--since <N>`; present the numbered batch and ask *"Apply all? [y/pick/skip]"*.
  Skip entirely if `graph.json` isn't seeded.
- **Snapshot for recap diff:** `python3 ${CLAUDE_SKILL_DIR}/scripts/session_recap.py snapshot --campaign <name>`.
- **Overwrite in place** — never create `state (1).md` duplicates.

---

## `/dm end`
1. Run `/dm save`, then:
   a. Append a **Session Recap** block to `session-log.md` (key events + open threads).
   b. Ask: *"Quick calibration — what worked, and what would you adjust next time?"* Write to
      `### DM Calibration`; if a genuinely new pattern emerged, refine `## DM Style Notes`.
   c. Update `## World State`: did events advance the threat arc, shift factions, or change
      the in-world date? Update all three.
   d. **Arc check (dynamic arcs only):** ask which beats landed; run `/dm arc advance
      <beat-id>` for each. For a beat whose `world_pressure` was delivered but whose
      `what_changes` consequence did NOT land, run `/dm arc revise` immediately.
   e. **Final card + memory refresh:** confirm every PC's `memory/<pc>-card.md` reflects
      end-of-session state (HP, resources, items, bonds, relationships, unresolved threads).
      *(Mode B: if host memory exists, write each card there now.)*
2. **Summarize** XP gained, items gained/lost, and unresolved threads for next time.

---

## `/dm abandon`
Exit the session **without saving**. Use after an error to discard changes since the last
save (or since load).
1. Confirm: *"Abandon session? All unsaved changes will be lost. Type 'yes' to confirm."* —
   do not proceed until confirmed.
2. Do **not** write to `state.md`, `world.md`, `npcs.md`, `session-log.md`, any character
   file, or any memory card.
3. Confirm: *"Session abandoned. No files were written. Run `/dm load <campaign>` to reload
   from the last saved state."*

---

## `/dm list`
Read `<root>/campaigns/*/state.md`; print a summary table: campaign name | last session date
| session count.

---

## `/dm lore <query>` — search the bundled Eberron lorebook
The lore lookup command. Use it whenever a scene touches Eberron lore, or before inventing
anything (canon precedence — see `lore/INDEX.md`).

- `python3 ${CLAUDE_SKILL_DIR}/scripts/lore_search.py "<query>"` — case-insensitive search
  across the whole `lore/` tree (distilled briefs + `fulltext/`). Ranks by match count.
- Flags: `--list` (show matching files only), `--files <substring>` (restrict to files whose
  path contains the substring, e.g. `--files news`, `--files rulebooks`), `--any` (match any
  term rather than all), `-n N` (max results).
- For SRD mechanics (monsters, spells, items, conditions) use `lookup.py` **first** (see
  `/dm roll` neighbors and `SKILL-scripts.md`); use `/dm lore` for Eberron/non-SRD content.
- Report what you found and **name the source file in your SOURCE line.** If nothing matches,
  say so, then improvise per canon precedence and record new canon into `world.md`.
- **Extensible:** any file dropped into `lore/fulltext/` (plus a line in `lore/INDEX.md`)
  becomes searchable canon automatically — no rebuild.

---

## `/dm data [status]`
- `status` → `python3 ${CLAUDE_SKILL_DIR}/scripts/build_srd.py --status` — show bundled
  dataset metadata.
The 5e SRD dataset is **bundled** at `${CLAUDE_SKILL_DIR}/data/dnd5e_srd.json` (plus
`data/srd-2014-complete.json (all 25 SRD resources merged in one file, keyed by resource name)`). No download is required at runtime; this offline build does not sync
from the network.

---

## `/dm path [<new-path> | reset]`
View or configure where campaign/character data is stored (wraps `GM_CAMPAIGN_ROOT`).
- No args → `python3 ${CLAUDE_SKILL_DIR}/scripts/path_config.py` and show output.
- New path → `python3 ${CLAUDE_SKILL_DIR}/scripts/path_config.py set <path>`; remind the user
  the change only takes effect in new shells.
- `reset` → `python3 ${CLAUDE_SKILL_DIR}/scripts/path_config.py reset`.
Default root is `~/eberron-dnd`. Existing campaigns are not auto-migrated.

---

## `/dm character new [campaign-name]`
**Read the campaign ruleset first:**
`python3 -c "import sys; sys.path.insert(0,'${CLAUDE_SKILL_DIR}/scripts'); from paths import campaign_ruleset; print(campaign_ruleset('<campaign>'))"`.

1. Ask: name, **species** (2024) or **race** (2014), class, background. **Eberron races &
   dragonmarks:** check `lore/races-cultures.md` and `lore/dragonmarked-houses.md` for
   warforged, shifters, changelings, kalashtar, and dragonmarked lineages before defaulting
   to a generic race. Apply ASIs per ruleset (2014: race grants them; 2024: background grants
   the ASI + a free Origin Feat).
2. Ask: *"In a sentence, what should the DM know about [Name]?"* Derive ONE pillar (Bond /
   Flaw / Ideal / Goal); store the raw sentence + pillar in `## Character Pillar`. If
   skipped, leave blank — do not invent one.
3. Ability scores: roll (`ability-scores.py roll`, present arrays, player assigns) or point
   buy (`ability-scores.py pointbuy --check <scores>`).
4. Apply racial/background bonuses; run `character.py calc` for secondary stats.
5. Ask: Fighting Style (if applicable), spells (if a caster; check `lore/` for setting spells
   like dragonmark focus items where relevant).
6. Assign starting equipment per class + background.
7. Write `characters/<name>.md` from `templates/character-sheet.md`; set
   `## Campaign History → Origin campaign`. Add `Dragonmark` / `Race-lineage` fields where
   Eberron-relevant.
8. **Create the PC memory card:** write `memory/<name>-card.md` from
   `templates/pc-memory-card.md`, populated from the new sheet (identity, HP/AC, resources,
   signature items, bond/goal/flaw, relationships-none-yet, threads-from-pillar).
9. Add to the `state.md` party line.
10. Mirror to the global roster: `cp characters/<name>.md <root>/characters/<name>.md`.
11. Fetch any non-SRD spells/features the character uses:
    `python3 ${CLAUDE_SKILL_DIR}/scripts/build_supplemental.py --character <root>/campaigns/<name>/characters/<charname>.md`.

---

## `/dm character sheet [name]`
Read `characters/<name>.md` and display cleanly. If name omitted and one PC exists, show it.

## `/dm character import <name> [from:<campaign>]`
1. Find the sheet (`from:<campaign>`, else global roster `<root>/characters/<name>.md`, else
   search all campaigns and ask).
2. Show a summary; ask: *"Import at current level, or level up first?"*
3. Copy to the current campaign's `characters/<name>.md`; reset death saves; update
   Campaign / Last Updated / Previous campaigns.
4. **Create/refresh the PC memory card** `memory/<name>-card.md` from the imported sheet.
5. Add to the `state.md` party line; update the global roster.
6. Run the supplemental builder for any non-SRD entries.
7. Deliver a one-paragraph in-character aside (stepping into a new world).

## `/dm characters`
List all characters in the global roster (`<root>/characters/`): name, race/class/level,
origin campaign, previous campaigns, last updated.

---

## `/dm level up [name]`
1. **XP gate — check first** (2:300, 3:900, 4:2700, 5:6500, 6:14000, 7:23000, 8:34000,
   9:48000, 10:64000, 11:85000, 12:100000, 13:120000, 14:140000, 15:165000, 16:195000,
   17:225000, 18:265000, 19:305000, 20:355000). Insufficient XP → report the deficit and stop
   unless the DM overrides.
2. Read the sheet; run `character.py levelup`; apply class features; ask for HP roll (player-
   rolled: `ROLL_REQUEST: roll 1d<hit-die>, add +CON`) or average.
3. **Ruleset-aware subclass timing:** 2014 uses each class's specified level; 2024 unifies
   subclass choice at level 3. Weapon Mastery (2024) for Fighter/Barbarian/Paladin/Ranger at
   level 1.
4. **Update the sheet AND the memory card in the same turn** (new level, HP/max, resources,
   any new signature features). Update the global roster. Narrate the growth.

---

## `/dm npc [name]`
- **Existing** → read the full entry from `npcs.md` (or `npcs-full.md`) and portray in
  character with voice/quirk.
- **New** → **check `lore/` first** (`lore_search.py`) for an existing Eberron NPC or a
  faction figure before inventing. Generate a full entry: role, CR-appropriate stats,
  demeanor, motivation, secret, flaw, speech quirk, faction, current goal, disposition
  (default neutral), and ≥2 relationships to existing NPCs. Append to `npcs.md`; name the
  `lore/` source if one shaped the NPC.

## `/dm npc attitude <name> <shift>`
Shift the NPC's attitude one step (hostile → unfriendly → neutral → friendly → allied); log
the reason and in-world date in `npcs.md`. If the NPC matters to a PC, update that PC's card
relationships.

---

## `/dm roll <notation>`
Run `python3 ${CLAUDE_SKILL_DIR}/scripts/dice.py <notation>` for **NPC/monster/secret** rolls
only, and display verbatim with math. Examples: `d20`, `2d6+3`, `d20 adv`, `4d6kh3`, and
`--silent` for hidden rolls. **Never use this to roll a PC's dice under `roll_mode: players`
— issue a `ROLL_REQUEST` and wait for the player.**

---

## `/dm combat start`
1. Identify combatants; collect name, DEX mod, HP, AC, type (pc/npc). **Check `lore/` for
   Eberron monster stat blocks** (`lore/bestiary.md`, `lore/fulltext/fight-club-statblocks.md`)
   and `lookup.py` for SRD monsters before improvising.
2. **Initiative is DM-rolled for ALL combatants** (PCs and NPCs) regardless of `roll_mode`:
   `python3 ${CLAUDE_SKILL_DIR}/scripts/combat.py init '<JSON>'`. Display the tracker and the
   per-combatant breakdown. Emit `INITIATIVE_ORDER` in MECHANICS.
3. Save the combat state to `state.md → ## Active Combat`.
4. **Per turn:**
   - **PC turns:** issue explicit `ROLL_REQUEST` callouts (attack, then damage) and **wait**
     for the player's numbers. Never roll a PC's attack/damage/save.
   - **NPC/monster turns:** you roll via `dice.py`/`combat.py`, showing math inline
     (`Goblin attacks: d20+4 = 17 vs AC 16 — hit! 1d6+2 = 5 piercing`).
   - Apply conditions/concentration/death saves via
     `python3 ${CLAUDE_SKILL_DIR}/scripts/tracker.py -c <campaign> ...`. **Death saves and
     concentration saves are player-rolled** with explicit callouts.
   - Emit the mandatory MECHANICS tags (`HP_CHANGE`, `CONDITION_APPLIED`, `CONCENTRATION`,
     `DEATH_SAVE`, etc.) each turn.
   - **Any PC HP change updates that PC's sheet AND card the same turn.**
5. **On combat end:** update HP on sheets + cards, clear `## Active Combat`,
   `tracker.py -c <campaign> clear`, narrate the aftermath, and award XP with `xp.py`
   (emit `XP_GAINED`).

---

## `/dm rest <short|long>`
**Short (1 hour):**
1. Ask how many Hit Dice the player spends; each is **player-rolled**
   (`ROLL_REQUEST: roll 1d<hit-die>, add +CON`). Update HP on sheet + card.
2. Note recharging features (e.g. Second Wind). **Warlock pact spell slots recharge on this
   short rest** — restore them (⚠ the most commonly missed rule).
3. Advance time: `python3 ${CLAUDE_SKILL_DIR}/scripts/calendar.py -c <campaign> rest short`.
4. Clear encounter conditions: `tracker.py -c <campaign> clear` (ask about concentration).

**Long (8 hours):**
1. Restore all HP, half max Hit Dice (round up), all spell slots, most features. Update
   sheet + card.
2. Advance time: `calendar.py -c <campaign> rest long`.
3. Clear all tracker state: `tracker.py -c <campaign> clear --all`.
4. Update the `state.md` in-world date to match the calendar output. (Inspiration is NOT
   cleared by a long rest.)

---

## `/dm recap`
Read `session-log.md`; deliver a 3–5 sentence in-character recap of the most recent session.
For the mechanical half, run
`python3 ${CLAUDE_SKILL_DIR}/scripts/session_recap.py diff --campaign <name>` (deterministic
HP/resource change line — recaps are the #1 thing to hallucinate, so compute it from data).

## `/dm world`
Read and display `world.md`.

## `/dm quests`
Read `state.md` → display Active Quests and Open Threads.

---

## `/dm arc [status|advance|revise|view]`
Manage the campaign arc. `advance`/`revise`/`new` are active only for `type: dynamic`; no-op
for `sandbox`. For `type: structured` (imported), `status`/`view` read from `arc.md`;
chapter advancement happens at `/dm save`.

- **`/dm arc` / `/dm arc status`** — print current act, current beat label, its `what_changes`,
  and `steering_notes` (one screen).
- **`/dm arc advance [beat-id]`** — mark the beat complete; remove from `outstanding_beats`;
  advance `current_beat` (and `current_act` when an act finishes); update `steering_notes`.
  When the final beat completes, offer `/dm arc new` or set `type: sandbox`.
- **`/dm arc view`** — full arc: theme, resolution, all acts/beats with completion status;
  show `## Arc History` if present.
- **`/dm arc revise`** — for a major story turn OR a pre-emption auto-trigger from `/dm end`.
  Show outstanding beats; apply one landing-path template (Cost / Secondary-consequence /
  Deferred) to the affected beat; rewrite `what_changes` (consequence-shaped) and
  `world_pressure` (event-shaped is fine); append to `revision_log`; do NOT touch completed
  beats.
- **`/dm arc new`** — generate a distinct new arc from the consequences of the completed one;
  archive the old arc to `## Arc History`.

---

## `/dm graph <subcommand>` — campaign relationship graph
Local-only typed-edge graph at `<root>/campaigns/<name>/graph.json`, supplementing (not
replacing) the markdown. Edges are time-stamped (`since_session`/`until_session`) so
historical state is recoverable. Auto-pulled at `/dm load` (scene-context) and swept at
`/dm save`. All subcommands invoke
`python3 ${CLAUDE_SKILL_DIR}/scripts/campaign_graph.py <subcommand> --campaign <name> [args]`.

- **`init [campaign-name]`** — propose nodes (`npc_*`/`faction_*`/`place_*`) and starter edges
  from `npcs.md`/`world.md`/`state.md`; show the DM the batch and **ask for approval** before
  writing; use `--since` = current session count.
- **`add-node --type T --name N [--tags …] [--summary …]`** — add one node.
- **`add-edge --from <id> --to <id> --type T [--since N] [--note …]`** — add a typed edge
  (`allied_with`, `opposes`, `member_of`, `lives_in`, `controls`, `knows_about`, …); always
  supply `--since`.
- **`close-edge --id <edge-id> --at-session N`** — end an edge (preserved with
  `until_session`).
- **`list [--type T] [--at-session N]`**, **`show --id <node-id>`** — inspect nodes/edges.
- **`scene-context --place <id> [--present …] [--threads …] [--hops H] [--at-session N]`** —
  the primary in-session query; focused subgraph of the current scene.
- **`subgraph --seed <id> [--seed <id>] [--hops H] [--at-session N]`** — arbitrary-seed
  traversal.
- **`extract [--deterministic] [--apply] …`** — propose new edges from the session log; the
  deterministic mode pattern-matches against `data/graph/verb_table_seed.yaml` with no LLM
  call. Review proposals before applying (or `--apply` with a confidence floor for a hands-off
  sweep at `/dm save`).

---

## `/dm oracle <subcommand>` — solo/improv oracle tools
Dice-driven, seedable (`--seed N`), zero-LLM oracles. All invoke
`python3 ${CLAUDE_SKILL_DIR}/scripts/oracle.py <subcommand>`.
- **`chaos [set|adjust]`** — Mythic chaos factor (1–9), stored as `chaos_factor` in
  `state.md → ## Session Flags`. `adjust --pc-won` (−1) / `--pc-lost` (+1).
- **`ask [--likelihood L] [--chaos C] [--seed S]`** — Ironsworn-style yes/no oracle
  (likelihood ∈ sure-thing/likely/50-50/unlikely/no-way), with `-and`/`-but` qualifiers.
- **`event [--seed S]`** — Mythic random-event focus (d100).
- **`scene [--seed S]`** — two-word scene-meaning spark. Interpret against Eberron threads.

---

## `/dm autosave on` / `/dm autosave off`
Toggle the behind-the-scenes continuity checkpoint (writes `autosave: on|off` to
`state.md → ## Session Flags`; **default on**). When on, the DM silently flushes continuity
anchors (Live State Flags, graph, recent beats, and any changed PC card) at scene boundaries.
Optionally install the deterministic Stop-hook backstop:
`python3 ${CLAUDE_SKILL_DIR}/scripts/install_autosave_hook.py` (`--uninstall` to remove); it
reads the same flag, so `/dm autosave off` silences it without uninstalling.

---

## `/dm oracle`, `/dm graph`, and script details
For full script syntax and flags, Read `${CLAUDE_SKILL_DIR}/SKILL-scripts.md`.
