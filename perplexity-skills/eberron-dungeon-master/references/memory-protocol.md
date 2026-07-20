# Persistent Memory Protocol

The heart of this skill. A campaign must feel **continuous across every thread**, even though each Perplexity Computer thread starts with a fresh context window. This file defines exactly how the DM stores, retrieves, and repairs campaign state so that NPCs, world state, and past decisions persist — the core continuity mandate of the DND Bot space prompt.

**Read this file at every `/dm load` and `/dm new`.**

---

## 1. Two Stores, One Truth

| Store | Mechanism | Holds | When |
|-------|-----------|-------|------|
| **Project files** (canonical) | `upload_file` (write) · `search_files` (read) | Full campaign state: state, world, NPCs, session log, character sheets | Written at `/dm save` and `/dm end`; read at `/dm load` |
| **Brain memory** (index) | `memory_update` (write) · `memory_search` (read) | A few durable one-liners: active campaign name, PC name/class/level, the single biggest unresolved thread | Written at `/dm end` and after major changes; read at session start |
| **Local working tree** (scratch) | ordinary file read/write under `/home/user/workspace/campaigns/<name>/` | The in-session mutable copy + script data (`tracker.json`, `calendar.json`) | Throughout a live session |

The **project files are the single source of truth.** The local tree is a working copy of them for the current thread. Brain memory is only a lightweight index so a new thread knows *which* campaign to load and can answer "where were we?" before the full files are fetched.

---

## 2. File Naming Convention (project files)

Every campaign file is stored as a project file with a flat, greppable name:

```
campaign--<campaign-name>--state.md
campaign--<campaign-name>--world.md
campaign--<campaign-name>--npcs.md
campaign--<campaign-name>--session-log.md
campaign--<campaign-name>--character--<pc-name>.md   (one per PC)
```

Use lowercase-hyphen campaign and PC names (e.g. `campaign--sharn-shadows--state.md`, `campaign--sharn-shadows--character--vesper.md`). The double-dash separators make `search_files` queries and `/dm list` reliable.

---

## 3. Saving — `upload_file`

At `/dm save`, `/dm end`, and after any consequential change:

1. Write the change to the **local file** first (immediate, always).
2. At a natural breakpoint (end of scene, end of combat, `/dm save`, `/dm end`), `upload_file` each changed local file to its project-file name.
3. **Overwrite, don't duplicate.** Use the `remote_path` / file identifier returned by the earlier `search_files` (or `/dm load`) result so the upload replaces the existing project file. If this is the first save of a new file, create it with the canonical name above.
4. Never leave the canonical store stale after a save — the next thread reads only what was uploaded.

**Immediate-local-update triggers** (update the local file the moment they happen; upload at the next breakpoint): HP change, spell slot spent, item gained/lost, condition applied/removed, attunement change, XP awarded, NPC disposition shift, faction move, in-world time advance.

---

## 4. Loading — `search_files`

At `/dm load <name>` (or when the player references a campaign):

1. `search_files` with focused queries, e.g. `"campaign state <name>"`, `campaign--<name>--state`, `"<name> session log"`. Matched files download to `/home/user/workspace/space_files/`.
2. Copy each matched campaign file into `/home/user/workspace/campaigns/<name>/` as the working tree, keeping their short names (`state.md`, etc.).
3. Read them in this order: **state.md (Live State Flags first)** → world.md → npcs.md → characters/*.md.
4. Recompute script state if `tracker.json` / `calendar.json` are absent (re-`init` the calendar from state.md's in-world date).
5. Deliver the in-character recap **from the freshly read files**, not from memory or compressed context.

At session start of any thread, also run `memory_search` for the active campaign to know which one to offer loading.

---

## 5. Brain Memory — `memory_update` / `memory_search`

Keep Brain memory **tiny and durable**. Write at `/dm end` (and after a level-up or a campaign-defining decision) a single line such as:

> *"Active D&D campaign: 'sharn-shadows' (Eberron). PC Vesper, Half-elf Warlock L3. Session 4 done. Biggest open thread: the Emerald Claw cell beneath Dura still active."*

`memory_search` at the top of a new thread answers "what campaign am I in and where did we leave off?" before the heavier `search_files` load. **Do not** put full state, stat blocks, or lore in Brain memory — that lives in project files.

---

## 6. Compaction Resilience

Long sessions get compacted; the middle of the context window is the least reliable place for a fact. Therefore:

- **Never trust compressed context for a state claim.** Before any recap, status readout, or assertion about cover, positioning, NPC stance, faction standing, HP, or slots, **re-read the smallest covering section of state.md** — start with **Live State Flags**, then the specific section you need.
- Keep **Live State Flags** in state.md continuously accurate — it is the designated compaction anchor: current cover/position, non-neutral faction stances, notable NPC dispositions, and resource watchpoints (warlock pact slots, attunement /3, active concentration, low consumables).
- The **STATE** block you emit every few turns is a live mirror of these flags; if the two ever disagree, re-read the file and correct.
- After a `/dm load`, the file — not the summary that triggered the load — is authoritative.

---

## 7. Continuity Guarantees (space-prompt mandates)

- **NPCs persist.** An NPC's name, motivation, secret, flaw, and disposition carry across every thread. Update disposition based on player behavior and write it back.
- **The world moves without the player.** Record Faction Moves at `/dm end`; surface their consequences when the party next intersects them.
- **Decisions stick.** A choice logged in session-log or Live State Flags must never be silently contradicted in a later thread. If two files conflict, prefer the more specific/recent and note the conflict to the player.
- **Space lore is canonical.** World, factions, and lore stay consistent with the DND Bot space files across all threads; when a space file shaped a scene, name it in the SOURCE section.

---

## 8. Session Lifecycle (memory view)

```
new thread ─► memory_search (which campaign?) ─► /dm load ─► search_files
   ─► copy to local tree ─► read state (Live State Flags first) ─► recap
   ─► PLAY: local-file updates on every change; re-read state.md before any claim
   ─► /dm save (upload_file changed files) at breakpoints
   ─► /dm end (log + faction moves + memory_update + upload_file all) ─► thread ends
```
