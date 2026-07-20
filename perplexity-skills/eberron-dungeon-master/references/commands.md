# `/dm` Command Procedures

Command procedures for the Eberron Dungeon Master, adapted from Bobby-Gray/open-tabletop-gm's `SKILL-commands.md` for Perplexity Computer. The upstream `/gm` prefix becomes **`/dm`**. Persistence uses **project files** (`upload_file` / `search_files`) plus `memory_update` instead of a git-backed home directory — see `memory-protocol.md`.

**Read this file at `/dm load` and `/dm new`.** Once a campaign is loaded, stay in GM mode: interpret all subsequent messages as in-game actions, no prefix needed.

Local working tree: `/home/user/workspace/campaigns/<name>/` (files: `state.md`, `world.md`, `npcs.md`, `session-log.md`, `characters/<pc>.md`, plus script data `tracker.json` / `calendar.json`). Canonical durable store: project files named `campaign--<name>--*.md`.

---

## Command Signatures

| Command | Description |
|---|---|
| `/dm new <name>` | Create a new campaign (Eberron default). World-gen procedure below. |
| `/dm load <name>` | Restore a campaign from project files and enter GM mode. |
| `/dm save` | Persist current state back to project files. |
| `/dm end` | End the session: calibrate, log, faction moves, `memory_update`, persist. |
| `/dm recap` | Re-read state.md (Live State Flags first) + session-log; 3–5 sentence in-character recap. |
| `/dm list` | List campaigns found via `search_files` for `campaign-- *--state.md`. |
| `/dm roll <notation>` | NPC/secret roll via `dice.py`. Never for a PC unless `roll_mode: auto`. |
| `/dm combat start` | Roll initiative for all combatants; open the tracker. |
| `/dm combat end` | Close combat; award XP; clear round-based tracker state. |
| `/dm rest <short\|long>` | Process a rest (HP, slots, hit dice, time). |
| `/dm character new [pc-name]` | Build a PC (race, class, background, scores, equipment). |
| `/dm character sheet [pc-name]` | Display the character sheet. |
| `/dm character levelup [pc-name]` | Apply a level-up. |
| `/dm npc <name>` | Generate or retrieve an NPC (space-search first). |
| `/dm quests` | Show active quests + open threads from state.md. |
| `/dm world` | Display world.md for the current campaign. |
| `/dm tutor <on\|off>` | Toggle tutor mode (`tutor_mode` in Session Flags). |
| `/dm rollmode <players\|auto>` | Set who rolls PC dice (`roll_mode` in Session Flags). |
| `/dm arc [status\|advance\|revise]` | Manage a dynamic campaign arc (see gm-craft.md). |
| `/dm abandon` | Exit without saving. Confirm first. |

---

## `/dm new <name>` — World Generation

1. **Setting.** Default to **Eberron** unless the player says otherwise. Note it: this world runs on the Galifar calendar, Dragonmarked Houses, the five nations recovering from the Last War, and magic-as-technology.
2. Create the local dir `/home/user/workspace/campaigns/<name>/characters/`. Copy the five templates from `assets/templates/` into it.
3. Ask **party size and starting level**.
4. **Tone wizard** (one message, all four): Tone · Magic level · Setting type · Danger level. Eberron defaults: pulp-noir + intrigue, high/industrialised magic, post-war, standard danger.
5. **World Foundations** → world.md. Register the calendar: `calendar.py -c <name> init --date "15 Aryth 998" --time morning --months "Zarantyr,Olarune,Therendor,Eyre,Dravago,Nymm,Lharvion,Barrakas,Rhaan,Sypheros,Aryth,Vult" --month-length 28 --day-names "Sul,Mol,Zol,Wir,Zor,Far,Sar"`. Seed the in-world date in state.md.
6. **Three Truths** (settlement, nearby threat, mystery) → world.md. **Before inventing**, `search_files` the space for a fitting Eberron location/threat and use it.
7. **Escalation Arc** (five stages) → world.md; set stage 1 in state.md.
8. **2 Factions / Dragonmarked Houses** → world.md + one-line summaries in state.md. Prefer canonical Eberron factions found in space files (Houses, Emerald Claw, the Chamber, Cults of the Dragon Below, etc.).
9. **3 NPCs** with the full schema (name, motivation, secret, flaw, disposition) + a relationship web → npcs.md.
10. **3–5 Quest Seeds** → world.md. Pull **1–2 from the space's Eberron news items** as live hooks (e.g. "Relief Convoy Attacked in Aundair").
11. **Roll handling.** Ask: *"Dice — `players` (default: you roll your own PCs and I wait) or `auto` (I roll everything openly)?"* Write `roll_mode:` to state.md → Session Flags. Default `players`.
12. **Dynamic arc (optional).** Ask: *"Generate a committed narrative arc? [y/n — recommended]"* If yes, derive theme, resolution, and six beats (see gm-craft.md → Six-Beat Arc) into state.md → Campaign Arc with `type: dynamic`. If no, set `type: sandbox`.
13. Write state.md (session count 0, starting location, system version). **Persist** all files to project files (see memory-protocol.md → save). `memory_update` the active campaign name + PC summary.
14. Confirm. Offer `/dm character new`. Open with a vivid, hook-driven first scene grounded in space lore.

---

## `/dm load <name>`

1. `search_files` for `campaign--<name>--state.md` (and the other campaign files). Copy each into `/home/user/workspace/campaigns/<name>/`.
2. Read `state.md` — **Live State Flags first**, then Current Situation, Session Flags (`roll_mode`, `tutor_mode`), GM Style Notes, and Campaign Arc.
3. Read `world.md`, `npcs.md`, all `characters/*.md`. Read `rules-5e.md` and this file into context.
4. Re-register the calendar/tracker if their JSON isn't present (recompute from state.md's in-world date).
5. Deliver **one in-character recap paragraph** from the smallest covering section (do not trust compressed context — re-read the source). Enter GM mode.

If no files are found, tell the player this campaign has no saved state and offer `/dm new <name>`.

---

## `/dm save`

1. Update `session-log.md` (append/refresh the current session entry).
2. Update `state.md`: Current Situation, World State, and **Live State Flags** (must be accurate after every save — it is the compaction anchor).
3. **Persist to project files:** `upload_file` each changed campaign file, overwriting the existing project file (use the `remote_path` from the earlier `search_files` result so it overwrites rather than duplicating). Naming: `campaign--<name>--state.md`, `--world.md`, `--npcs.md`, `--session-log.md`, `--character--<pc>.md`.
4. Confirm what was saved.

Also persist immediately (not only at save) after any HP change, spell slot spent, item gained/lost, or condition change — update the local file at once; upload at natural breakpoints (end of combat, end of scene, `/dm save`, `/dm end`).

---

## `/dm end`

1. Do everything in `/dm save`, plus:
2. Append to session-log: **XP awarded**, **items gained/lost**, **NPC attitude shifts**, **unresolved threads**, and **Faction Moves** (what each active faction/House did off-screen — record in state.md → Faction Moves; a move the party didn't prevent should surface next session as a visible change).
3. For **dynamic arcs**: mark any beats that landed (`/dm arc advance`); run the pre-emption check (see gm-craft.md); update `steering_notes`.
4. Update **GM Style Notes** only if a genuinely new pattern about this player emerged.
5. Session-log archival after session count > 3: keep the 2 most recent full entries; move older ones to a `## Continuity Archive` bullet summary in state.md.
6. `memory_update` one durable line: session number, PC level/state, and the biggest unresolved thread.
7. `upload_file` all changed files to project files. Give a spoiler-free session summary to the player.

---

## `/dm character new [pc-name]`

1. Ask whether the player has an existing character or needs one built.
2. If building: walk through **race, class, background, ability scores, equipment** using the Player's Handbook. **`search_files`** the space for setting-specific races or **dragonmarks** (e.g. a Mark of Finding tied to House Tharashk) and offer them.
3. Ability scores: `ability_scores.py roll` (three 4d6kh3 arrays) or `ability_scores.py pointbuy --check ...` (27-point). PCs may roll their own if `roll_mode: players`.
4. Verify all derived stats with `character.py calc --class <c> --level <L> STR=.. --proficient ..`.
5. Write `characters/<pc>.md` from the template (include Dragonmark + Eberron origin fields). Persist as `campaign--<name>--character--<pc>.md`. `memory_update` the PC summary.

---

## `/dm combat start` / `/dm combat end`

- **Start:** gather combatants (PCs from sheets, NPCs from npcs.md/space monster files), roll initiative with `combat.py init` (GM-rolled for all), announce `INITIATIVE_ORDER`, and run turns. Resolve NPC attacks with `combat.py attack`; for PC attacks under `roll_mode: players`, call for the roll and wait. Track conditions/concentration with `tracker.py`.
- **End:** award XP (`xp.py award`), report `XP_GAINED`, clear round-based state (`tracker.py -c <name> clear --all` after a long rest, or targeted `condition remove` otherwise), update state.md, persist.

---

## `/dm rest <short|long>`

Apply the rest rules in `rules-5e.md §6`. **Warlock Pact Magic slots recharge on a SHORT rest.** Advance time with `calendar.py rest short|long`. On a long rest, restore HP/slots/half hit dice and `tracker.py clear --all`. Update the character sheet(s) and STATE; persist.
