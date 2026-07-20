---
name: eberron-lorekeeper
description: "Eberron and D&D lore + rules knowledge base distilled from the DND Bot project library. Load when you need setting facts about Eberron (Khorvaire, the Last War, the Mourning, year 998 YK), dragonmarked houses (Phiarlan, Lyrandar, Tharashk, Cannith, Kundarak, Deneith), nations (Five Nations, Droaam, Mror Holds, Lhazaar, Zilargo, Eldeen Reaches, Valenar, Aerenal, Sarlona, Xen'drik/Stormreach), religions (Silver Flame, Sovereign Host, Blood of Vol, Cults of the Dragon Below, druid sects, monastic orders), organizations (Heirs of Dhakaan, Children of Khyber/House Tarkanan, Dreaming Dark, Emerald Claw, Aurum, Lord of Blades), races (warforged, kalashtar, changelings, shifters, Mror dwarves, Valenar elves), psionics and Dal Quor/Xoriat theory, prestige classes, monster/stat-block lookups, adventure hooks, 998 YK news as session hooks, and SRD quick tables (conditions, CR/XP, encounter multipliers). Use for 'what does the library say about X', campaign knowledge base, monster lookup, or DND Bot lore queries."
license: "SRD content under OGL v1.0a; distilled Eberron summaries are original prose describing copyrighted material for reference only."
metadata:
  author: eberron-lorekeeper-builder
  version: '1.0'
---

# Eberron Lorekeeper — Knowledge Repository

This skill is the **lore and rules knowledge base** for the "DND Bot" Perplexity project, which
holds ~498 D&D files (Eberron *Dragonshards* articles, *Eberron Expanded* sourcebook adaptations,
*Steal This Hook!* adventure hooks, *Fight Club* NPC/monster stat blocks, prestige classes, in-world
998 YK news items, and full rulebooks including the OGL SRD). It is the companion to the
`eberron-dungeon-master` skill: the DM skill runs play; this skill answers *"what does the library
actually say about X?"* with sourced, distilled facts.

## When to use this skill
- A player, DM, or agent asks about Eberron setting lore (a house, nation, faith, organization,
  race, NPC, place, event, or the timeline).
- You need a monster or NPC stat block, a prestige class, a feat, or a rules table.
- You need an adventure hook or a session seed grounded in the library.
- You need a mid-session rules reference (a condition, a CR→XP value, an encounter multiplier, a
  skill/DC, or an SRD spell summary).
- You are verifying a fact before improvising, per the project's prime directive: **search the
  library first; only invent when nothing relevant exists, and say so when you do.**

## How this repository is organized
Everything lives under `references/`. Read only the file(s) you need for the question at hand:

| File | Read it when you need… |
|------|------------------------|
| `catalog.md` | The master list of every known project file + how to retrieve any file at runtime. |
| `world-primer.md` | Eberron 101: the Last War, Treaty of Thronehold, Galifar, the Mourning, tone (noir + pulp), the calendar/months/days, year 998 YK, currency. |
| `dragonmarked-houses.md` | The dragonmarked houses (deep detail on Phiarlan's Serpentine Table; Lyrandar, Tharashk, Cannith, Kundarak, Deneith, Sivis, Medani, Vadalis, Orien, Ghallanda, Jorasco, Thuranni). |
| `nations.md` | The Five Nations + Droaam, Mror Holds, Lhazaar, Zilargo, Eldeen Reaches, Talenta, Valenar, Aerenal, Sarlona (Riedra/Adar), Xen'drik/Stormreach — character, rulers, conflicts. |
| `religions.md` | Silver Flame, Sovereign Host, Blood of Vol, Cults of the Dragon Below, Undying Court, druid sects, monastic orders, the Lycanthrope Purge. |
| `organizations.md` | Heirs of Dhakaan, Children of Khyber / House Tarkanan, Dreaming Dark / Blades of the Quori, Emerald Claw, Aurum, Lord of Blades, Daughters of Sora Kell, Eldeen Wolves, and more. |
| `races-cultures.md` | Warforged (incl. druids & the ninja Guile), kalashtar, changelings, shifters, Mror dwarves, Valenar/Aereni elves, drow, goblinoids. |
| `psionics.md` | Psionics theory (Dal Quor/Xoriat), Sarlona, quori-warrior traditions, *Complete Psionic* / *Psionics of Incarnum* / expanded psionic classes. |
| `prestige-classes.md` | Full requirements/features for every prestige class in the corpus (Body Leech, Psychic Theurge, Child of Khyber, and the divine PrCs / Order of the Chalice). |
| `bestiary.md` | Notable stat blocks (Taibo, Imbrudar, Bhissok, Beshappal, Chuladoal, Drashan, the four psionic monsters, tether hound, Guile) + how to look up rulebook monsters. |
| `news-gazette.md` | Every dated 998 YK news item, each written up as a ready-to-run session hook with its source. |
| `adventure-hooks.md` | *Steal This Hook!* hooks, Strike Force: Dhakaan, and the 5e adventure outlines (Princes of the Apocalypse). |
| `rules-supplements.md` | Index of the crunch books (2024 PHB, MM, DMG, Fizban's, PHB II, Complete Warrior, Heroes of Battle, Stronghold Builder's) — what each covers and when to search it. |
| `srd-quick-tables.md` | Open-licensed SRD tables a DM needs mid-session: conditions, XP-by-CR, encounter multipliers, skills, ability/DC scale, common spells. |
| `SRD-OGL_V1.1-full.txt` | The complete SRD 5.1 text (OGL v1.0a). Grep it for any rule, spell, class, or monster verbatim; it is open content and safe to quote. |

## Runtime search protocol (retrieving project files not distilled here)
The distilled references capture the extracted corpus. For any file marked "retrieve at runtime" in
`catalog.md`, or for the full rulebooks, fetch it live:
1. Call the `search_files` tool (the `files` / `search_files_v2` connector) with a query built from
   the file's distinctive title words or the topic (e.g. `Vvaraak prophecy code`, `Stronghold
   Builder base construction`, `Way of the Ascendant Dragon monk`).
2. Matching PDFs download to `/home/user/workspace/space_files/…`; open them with `read`.
3. For big rulebooks, search for the *specific* creature/spell/rule, not the whole book.

## SOURCE citation rule (mandatory)
Every fact you surface from this repository must name its origin file inline, exactly as the
references do, e.g. `(Source: House-Phiarlan-Part-Three.pdf)` or `(Source: Heirs-of-Dhakaan.pdf)`.
When a fact comes from the SRD, cite `(Source: SRD-OGL_V1.1.txt)`. This mirrors the DND Bot project's
required `SOURCE` line. If you must invent something because the library is silent, say so
explicitly and do **not** attach a false source.

## Content integrity rules
- **Never fabricate.** Only report what the corpus contains. If unknown, say the library does not
  cover it and offer to retrieve a runtime file.
- **Copyright:** Do not reproduce long verbatim passages from copyrighted rulebooks (2024 PHB, MM,
  DMG, Fizban's, etc.) — the references distill and index them. SRD/OGL content *may* be quoted.
- **Conflicts:** If two sources disagree, prefer the more specific or more recent one and note the
  conflict (the references flag known conflicts, e.g. who controls the Fist of Onatar).
- **Dates** in Eberron news are given in the Galifar calendar, year 998 YK (see world-primer.md).
