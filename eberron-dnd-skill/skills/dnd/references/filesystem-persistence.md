# Filesystem Persistence Protocol

The heart of this skill. A campaign must feel **continuous across every session**, even
though each new agent session starts with a fresh context window. This file defines
exactly how the DM stores, retrieves, and repairs campaign state **entirely on the local
filesystem** — no cloud store, no `upload_file`/`search_files`, no `memory_update`, no
network. NPCs, world state, and past decisions persist because they are written to plain
files and read back.

**Read this file at every `/dm load` and `/dm new`.**

---

## 1. One Store, One Truth

All campaign state lives in **local files** under the campaign root:

```
$GM_CAMPAIGN_ROOT/campaigns/<name>/        (default root: ~/eberron-dnd)
  state.md            # live state — the single source of truth
  world.md            # setting, factions, nodes, calendar
  npcs.md             # NPC roster (name/motivation/secret/flaw/disposition + relationships)
  session-log.md      # per-session log + continuity archive
  characters/<pc>.md  # one file per player character (full sheet — canonical)
  memory/<pc>-card.md # compact PC Memory Card (auto-maintained recall layer — see §8)
  tracker.json        # combat/condition/concentration/death-save state (scripts)
  calendar.json       # in-world date/time (scripts)
  graph.json          # deterministic campaign graph (scripts)
```

There is **no separate canonical store** to sync to — the files under
`campaigns/<name>/` *are* canonical. Override the root with **`GM_CAMPAIGN_ROOT`**
(legacy `DND_CAMPAIGN_ROOT` honored as a fallback). Runtime markers (active-campaign
pointer, autosave counters, name registry) live under `$GM_CAMPAIGN_ROOT/.runtime/`.

Use **lowercase-hyphen** campaign and PC names (e.g. `sharn-shadows`, `vesper`).

---

## 2. Saving — write local files (`/dm save`, `/dm end`, after any consequential change)

1. Write the change to the **local file** immediately (always).
2. `state.md` must be accurate after every save — it is the compaction anchor
   (see §5). Update **Current Situation**, **World State**, and **Live State Flags**.
3. Append/refresh the current entry in `session-log.md`.
4. **Overwrite in place** — never create `state (1).md` duplicates. The scripts and the
   next session read exactly these paths.

**Immediate-update triggers** (update the local file the moment they happen): HP change,
spell slot spent, item gained/lost, condition applied/removed, attunement change, XP
awarded, NPC disposition shift, faction move, in-world time advance. Script state
(`tracker.json`, `calendar.json`, `graph.json`) is written by the helper scripts as you
use them.

**NEVER lose a PC.** Any HP change, level-up, item gain/loss, or bond/goal/flaw change
must update **both** `characters/<pc>.md` **and** `memory/<pc>-card.md` in the **same
turn** (see §8). The card and the sheet may never drift apart.

---

## 3. Loading — read local files (`/dm load <name>`)

1. Resolve the campaign directory: `$GM_CAMPAIGN_ROOT/campaigns/<name>/` (use
   `python3 scripts/paths.py campaign <name>` or `campaigns_dir` to confirm the path).
   If it does not exist, tell the player there is no saved state and offer `/dm new`.
2. Read files in this order: **`state.md` (Live State Flags first)** → **each PC's
   `memory/<pc>-card.md` (compact recall — read BEFORE the full sheet)** → `world.md` →
   `npcs.md` → `characters/*.md` (full sheets, for detail the card does not carry).
   If a host memory facility is available, also query it per PC (see §8.3).
3. Also read `references/rules-5e.md`, `references/gm-craft.md`,
   `references/canonical-dm-rules.md`, and this file into context.
4. If `tracker.json` / `calendar.json` are absent, recompute: re-init the calendar from
   `state.md`'s in-world date
   (`calendar.py -c <name> init --date "<D Month YYYY>" ...`).
5. Deliver the in-character recap **from the freshly read files**, not from memory or
   compressed context.

`scripts/campaign_search.py -c <name> "<keywords>"` greps the campaign's own files for a
fact; `scripts/session_recap.py` produces a deterministic state diff between snapshots.

---

## 4. Which Campaign Am I In? (the runtime pointer replaces "Brain memory")

There is **no external memory index.** The active campaign is tracked by a local marker
under `.runtime/` (written by `/dm load` / `/dm new`, read by autosave). To answer "where
were we?" at the top of a new session:

1. `/dm list` — enumerate `campaigns/*/state.md`.
2. `python3 scripts/autosave_checkpoint.py --status` — prints the active campaign and turn
   count from the runtime marker.
3. Then `/dm load <name>` and read `state.md` for the full recap.

Do **not** attempt any `memory_update` / `memory_search` — those tools are intentionally
absent from this build.

---

## 5. Compaction Resilience

Long sessions get compacted; the middle of the context window is the least reliable place
for a fact. Therefore:

- **Never trust compressed context for a state claim.** Before any recap, status readout,
  or assertion about cover, positioning, NPC stance, faction standing, HP, or slots,
  **re-read the smallest covering section of `state.md`** — start with **Live State
  Flags**, then the specific section you need.
- Keep **Live State Flags** in `state.md` continuously accurate — the designated
  compaction anchor: current cover/position, non-neutral faction stances, notable NPC
  dispositions, and resource watchpoints (warlock pact slots, attunement /3, active
  concentration, low consumables).
- The **STATE** block you emit every few turns is a live mirror of these flags; if the two
  ever disagree, re-read the file and correct.
- After a `/dm load`, the **file** — not the summary that triggered the load — is
  authoritative.
- `scripts/autosave_checkpoint.py` snapshots `state.md` to a recovery file under
  `.runtime/` on a cadence; `install_autosave_hook.py` can wire it to run automatically.

---

## 6. Continuity Guarantees (canonical mandates)

- **NPCs persist.** An NPC's name, motivation, secret, flaw, and disposition carry across
  every session. Update disposition based on player behavior and write it back to
  `npcs.md`.
- **The world moves without the player.** Record Faction Moves at `/dm end` in
  `state.md → ## Faction Moves`; surface their consequences when the party next intersects
  them.
- **Decisions stick.** A choice logged in `session-log.md` or Live State Flags must never
  be silently contradicted later. If two files conflict, prefer the more specific/recent
  and note the conflict to the player.
- **Lore is canonical.** World, factions, and lore stay consistent with the bundled
  `lore/` corpus across all sessions; when a lore file shaped a scene, name it in the
  SOURCE section. (Canon precedence: campaign state files override everything, then
  `lore/`, then SRD/rules data, then DM improvisation recorded into `world.md` — see
  `lore/INDEX.md`.)

---

## 7. Session Lifecycle (filesystem view)

```
new session ─► /dm list  or  autosave_checkpoint.py --status  (which campaign?)
   ─► /dm load <name> ─► read state.md (Live State Flags first)
                        → memory/<pc>-card.md (each PC, FIRST) → world/npcs/characters
                        → (query host memory per PC if available)
   ─► recap FROM FILES
   ─► PLAY: local-file updates on every change (sheet + card same turn);
           re-read state.md before any claim
   ─► /dm save (rewrite changed files + refresh each PC card) at breakpoints
   ─► /dm end (log + faction moves + arc advance + rewrite all files + refresh cards
              + mirror each card to host memory if available) ─► session ends
```

---

## 8. The PC Brain — Dual-Mode Memory Layer

Every player character gets a **brain**: a compact, always-current memory of who they are
and where they stand, engineered so that no context compaction and no fresh session can
ever lose a PC. It has two modes. **Mode A (filesystem) is always on and is the source of
truth. Mode B (host memory) is an optional recall accelerator.**

### 8.1 Mode A — PC Memory Card (canonical, filesystem, always)

Alongside each full sheet `characters/<pc>.md`, the DM maintains a **compact auto-
maintained card** at `memory/<pc>-card.md` in the campaign dir. The full sheet is the
complete record; the **card is the fast recall layer** — small enough to always read in
full at load, before touching the sheet. Template: `templates/pc-memory-card.md`.

The card holds exactly the fields needed to run and recall the PC without re-parsing the
full sheet:

- **Identity:** name, race/lineage (+ dragonmark if any), class(es) + level, background.
- **Vitals:** current HP / max HP, AC, key defenses (saves, resistances).
- **Key resources:** spell-slot line, warlock pact slots (⚠ short-rest), important limited
  features, attunement count (/3).
- **Signature items:** attuned/notable magic items and irreplaceable gear.
- **Bonds / goals / flaws:** the character's drivers, in one line each.
- **Key relationships & NPC attitudes:** the handful of NPCs this PC cares about and how
  each currently regards them.
- **Unresolved personal threads:** open hooks tied specifically to this PC.

**When to write the card:** at every `/dm save` and every `/dm end` (full refresh), and
immediately on any **HP change, level-up, item gain/loss, or bond/goal/flaw change**
(targeted update, same turn as the sheet edit — see "NEVER lose a PC" in §2).

**When to read the card:** **FIRST**, at every `/dm load`, before the full sheet — it is
the compaction-resilient recall. Re-read it (not compressed context) before any status
readout or recap of a PC's condition, resources, or relationships.

### 8.2 Mode B — Host-memory hook (optional adapter, when available)

If — and only if — the **host agent** provides a persistent cross-session memory facility,
the DM should **mirror each PC's Memory Card into it** as a recall accelerator. Examples of
such facilities:

- **Perplexity Computer "Brain"** (`memory_update` / `memory_search`),
- **Claude Code / Claude.ai memory**, or
- any equivalent host-provided durable key-value or note store.

Contract for the adapter (keep it strictly optional — **no hard dependency**):

- **One memory entry per PC**, keyed by campaign + character (e.g.
  `eberron:<campaign>:pc:<name>`). **Update the existing entry — never duplicate.** The
  entry's body is the current Memory Card text.
- **Write** at `/dm end` (and optionally `/dm save`): after refreshing the filesystem card,
  push the same text to the host store.
- **Query** at `/dm load` / session start: after reading the filesystem card, query the
  host store for that PC to catch anything the local files somehow lack. **On any conflict,
  the filesystem card wins** — host memory is only an accelerator, never authority. If the
  two disagree, trust the file and overwrite the host entry.
- **Graceful absence:** this build ships **no** host-memory tools. If none is available
  (the standalone default), skip Mode B silently — the filesystem card already guarantees
  full continuity. Never make session flow depend on a host store existing.

### 8.3 Precedence & the "never lose a PC" guarantee

1. **Full sheet `characters/<pc>.md`** — complete canonical PC record.
2. **Card `memory/<pc>-card.md`** — compact mirror of the sheet's live-critical fields;
   source of truth for fast recall; always kept in lockstep with the sheet.
3. **Host memory entry** (if any) — convenience mirror of the card; lowest authority.

The sheet and the card are updated in the **same turn** on every HP change, level-up, item
gain/loss, or bond change. Because the card is tiny and read in full at every load, a PC's
state survives any compaction, crash, or fresh session with zero loss.
