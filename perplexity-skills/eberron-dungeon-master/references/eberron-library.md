# Using the Eberron Library (Space Files)

The DND Bot project holds **~498 uploaded files**: the core rulebooks plus a deep Eberron library of Dragonshards articles, prestige classes, adventures, monsters, organizations, and in-world news items. **These files are the DM's source library.** Before improvising lore, a monster, an NPC, a location, a faction, a prestige class, a magic item, or a ruling, **search the space files first and use what you find.** Only invent when nothing relevant exists — and say so when you do.

**Read this file at `/dm load` and `/dm new`, and consult it before any act of world-building.**

---

## 1. The Search-First Rule

Whenever you are about to create anything that could plausibly already exist in the library:

1. Run `search_files` with **1–3 focused queries** (see query patterns below). Matched PDFs download to `/home/user/workspace/space_files/`.
2. `read` the matched files (the `read` tool extracts PDF text and page images).
3. **Use what you find** — adopt its names, stats, tone, and factions rather than a generic substitute.
4. **Cite it** in the response's **SOURCE** section by filename.
5. Only if nothing relevant is found, invent — and note in SOURCE that it was improvised because the library had no match.

If two space files conflict, prefer the **more specific or more recent** one and note the conflict to the player.

---

## 2. What's in the Library (categories)

| Category | Use for | Example filenames |
|----------|---------|-------------------|
| **Core rulebooks** | Rules adjudication, spells, monsters, items | Player's Handbook, Dungeon Master's Guide, Monster Manual, Basic Rules |
| **Dragonshards / lore articles** | Setting tone, factions, religion, regions | "Religion in Eberron", "The Children of Khyber", "Children of Khyber" |
| **Prestige classes** | NPC/PC advanced builds | "The Body Leech (Prestige Class)", "Taibo, the Ethereal Filcher Monk" |
| **Adventures / modules** | Ready-made scenarios, maps, encounters | "TARTH MOORDA", "Strike Force: Dhakaan", "Stronghold Enhance" |
| **Monsters** | Stat blocks, tactics, setting-appropriate foes | "Ravaging Monsters", "Reptilian Tool of Tiamat", "Children of Khyber" |
| **Organizations / factions** | Antagonists, patrons, intrigue | "The Children of Khyber", "Red Gauntlet Regiment Reunites in Sharn" |
| **News items (session hooks)** | Live quest seeds and rumours | "Relief Convoy Attacked in Aundair", "Report: Critical Gaps Exist in Graywall Defenses", "Repairs Interrupt Lightning Rail", "Revival of Wyvern Hunt Takes 12 Wyverns", "Sudden Retirements Leave Phiarlan Musicians in Demand", "Researchers Crack Code of Vvaraak" |

*(Filenames above are drawn from the visible project file list; the full library is ~498 files — always search rather than relying on this sample.)*

---

## 3. Query Patterns

Keep queries short and specific. Run them through `search_files`.

- **A monster:** `"Eberron aberration monster"`, `"undead stat block"`, or the creature name.
- **A faction / organization:** `"Emerald Claw"`, `"Dragonmarked House Cannith"`, `"Cults of the Dragon Below"`, `"Children of Khyber"`.
- **A location:** `"Sharn district"`, `"the Mournland"`, `"Graywall defenses"`.
- **A prestige class / build:** `"prestige class"`, `"Body Leech"`.
- **A quest hook / rumour:** `"Aundair convoy attack"`, `"lightning rail repairs"`, `"wyvern hunt"`.
- **A rule / spell / item:** `"grappling rules"`, `"warlock pact magic"`, `"attunement magic item"`.
- **Religion / cosmology:** `"Sovereign Host"`, `"Silver Flame"`, `"Blood of Vol"`, `"religion Eberron"`.

Reading a downloaded PDF: `read` the file at `/home/user/workspace/space_files/<filename>` (use `offset`/`limit` for long adventures).

---

## 4. News Items as Living Hooks

The news-style files are the setting's pulse. At `/dm new`, seed **1–2 quest hooks** directly from them, and during play use them as rumours the party overhears. They also drive **Faction Moves**: a headline like "Relief Convoy Attacked in Aundair" or "Report: Critical Gaps Exist in Graywall Defenses" is a faction acting off-screen — reflect that momentum in the world even if the party never engages it.

---

## 5. Eberron Setting Defaults

Unless the player says otherwise, the world is **Eberron**:

- **Post-Last-War**, year ~998 YK. The five nations (Breland, Karrnath, Thrane, Aundair, Cyre — now the Mournland) hold an uneasy peace under the Treaty of Thronehold.
- **Magic as technology:** the lightning rail, elemental airships, everyday magewright services, warforged, House Cannith creation forges.
- **The twelve Dragonmarked Houses** run the economy as quasi-guild dynasties (Cannith, Deneith, Ghallanda, Jorasco, Kundarak, Lyrandar, Medani, Orien, Phiarlan, Sivis, Tharashk, Thuranni, plus Vadalis). **Aberrant** marks are feared; the **Mark of Death** is lost.
- **Tone:** pulp-noir adventure with political intrigue — morally grey, not high-fantasy black-and-white.
- **Faiths:** Sovereign Host, the Dark Six, the Silver Flame, the Blood of Vol, the Cults of the Dragon Below, the Path of Light. See "Religion in Eberron".
- **Calendar:** Galifar calendar — 12 months × 28 days; months Zarantyr → Vult; weekdays Sul, Mol, Zol, Wir, Zor, Far, Sar (see world.md template and `calendar.py init`).
- **Signature locations:** Sharn (City of Towers), the Mournland, Q'barra, the Shadow Marches, Droaam (Graywall), Xen'drik, Karrnath's undead legions.

When a player prefers a non-Eberron or homebrew setting, honor it — but still search the space files for reusable monsters, rules, and prestige classes.

---

## 6. Citing Sources in Play

Every response that used the library names the file in its **SOURCE** section, e.g.:

```
SOURCE: "The Children of Khyber" (faction & aberration lore for the cultists);
        Monster Manual (base stat block for the grells).
```

If a scene was fully improvised, say so: `SOURCE: improvised — no matching space file found for a Sharn dockside fixer.`
