# Rules & Supplement Index

The library holds full rulebooks and crunch supplements, bundled as text under
`lore/fulltext/rulebooks/`. **Do not reproduce long verbatim passages from copyrighted rulebooks**
(2024 PHB, MM, DMG, Fizban's, PHB II, etc.) — distill mechanics in your own words. **SRD/OGL content
may be quoted** (see srd-quick-tables.md and `lore/fulltext/rulebooks/srd-ogl-5.1.txt`). To pull a
specific rule/spell/subclass: run `python3 scripts/lookup.py <category> "<name>"` first (SRD, offline),
then search the bundled rulebook texts with
`python3 scripts/lore_search.py "<term>" --files rulebooks`, and read only the matching section.

**Bundled rulebook filenames** (under `lore/fulltext/rulebooks/`): `srd-ogl-5.1.txt`,
`players-handbook-2024.txt`, `monster-manual-2024.txt`, `monster-manual-2014.txt`,
`monster-manual-expanded-1/2/3.txt`, `dungeon-masters-guide-2014.txt`, `fizbans-treasury-of-dragons.txt`,
`players-handbook-2-3.5e.txt`, `complete-warrior.txt`, `princes-of-the-apocalypse-5e.txt`,
`dragon-delves-5e.txt`, `storm-kings-thunder-5e.txt`, `reigns-homebrew-compendium.txt`,
`adventure-ill-wind-in-friezford.txt`.

## Core 5e / 5.5e rulebooks (copyrighted — index only)
| Book (file) | What it covers | Search it when you need… |
|-------------|----------------|--------------------------|
| **Player's Handbook [2024]** (`Player's Handbook [2024]_djvu.txt`) | 2024 (5.5e) player rules: species, backgrounds, classes/subclasses, feats, equipment, spells, the play rules. | A 2024 class/subclass feature, a species trait, a feat, a spell's current wording, or character-creation rules. |
| **Monster Manual [2024]** (`Monster Manual [2024]_djvu.txt`) | 2024 monster stat blocks & lore. | A current monster stat block or a monster's traits/actions. |
| **Monster Manual** (2014) (`Monster Manual_djvu.txt`) | 2014 5e bestiary. | A classic 5e stat block if you want the older numbers. |
| **Dungeon Master's Guide** (`Dungeon Master's Guide_djvu.txt`) | DM tools: magic items, encounter/treasure building, world/dungeon design, optional rules. | A magic item, treasure table, downtime rule, or encounter-building guidance. |
| **Fizban's Treasury of Dragons** (`fizban's treasury of dragons.pdf`) | Dragon deep-dive: chromatic/metallic/gem dragonborn, Gifts of the Dragon, **Way of the Ascendant Dragon** monk, dragon magic, dragon roleplay, greatwyrms. | Dragon-themed player options or richer dragon stat blocks/lore (great for an Eberron **Argonnessen** or Chamber arc). |

## 3.5e rulebooks & web enhancements (copyrighted — index/distill)
| Book (file) | What it covers | Use it for… |
|-------------|----------------|-------------|
| **Player's Handbook II** (`Player_s Handbook II.pdf`) | 3.5e expansion: new classes (**dragon shaman**, duskblade, knight, beguiler), **expanded classes** mechanic, feats, party roles. | The dragon shaman (see `Dragon-Shaman-Elemental-Warrior.pdf`) and expanded-class options (see psionics.md). |
| **Complete Warrior** web enhancement (`D_D Complete Warrior.pdf`) | Expands the **Order of the Chalice** (demon-hunting Knights of the Chalice): membership, chapter house, 3 NPC stat blocks. Parent book adds martial PrCs/feats (e.g. **hulking hurler**). | Demon-hunting knights (organizations.md), the hulking hurler (Drashan Daverund, bestiary.md), martial feats/PrCs. |
| **Complete Psionic** (`Complete Psionic.pdf` article) | Psionic classes/options (ardent, lurk, **Six Hidden Houses**); Baker's Eberron adaptation. | Psionic character options — seat in Lhazaar/Sarlona (psionics.md). |
| **Psionics of Incarnum** (`Psionics of Incarnum.pdf`) | Bridges *Magic of Incarnum* (soulmelds/essentia) with psionics. | Incarnum + psionic hybrids (psionics.md). |
| **Libris Mortis** adaptation (`Libris Mortis, Part One/Two.pdf`) | Adapting *The Book of Undead* to Eberron (Karrnath, Blood of Vol, Queen of the Dead). | Undead-heavy Karrnath/Blood-of-Vol content (bestiary.md, religions.md). |
| **Heroes of Battle** adaptation (`Heroes of Battle, Part One/Two.pdf`) + **Theaters of Death** (`DnD_Theaters_of_Death.pdf`) | Mass combat, battlefield encounters (level 4–10), war spells/feats/items; adapting to Last-War Eberron; the **Guerilla Warrior** feat. | Running Last-War battles and war-backdrop dungeons (adventure-hooks.md). |
| **Stronghold Builder's Guidebook** enhancement (`Stronghold Enhance.qxd.pdf`) | Building/upgrading strongholds and bases; stronghold spaces and costs. | When PCs build a base, guildhall, or fortress. |
| **Faiths & Pantheons / FR faith enhancement** (`FR_Faiths_Enhance.qxd.pdf`) | Deity write-ups and divine crunch (Forgotten Realms origin). | Divine crunch to reskin for Eberron faiths (religions.md). |
| **Monster Manual Expanded 1/2/3** (`Monster Manual Expanded *_djvu.txt`) | Third-party expansions: new stat blocks, monster variants, boss versions, encounter builders across CRs. | A wider bestiary and higher-CR variants for 5e (bestiary.md). Note vol. 2 has duplicate files (`v1`, `(Copy)`). |

## Article-format crunch (distilled in sibling references)
- **091913 Feats** — a feat compilation (search `lore_search.py "feat"`).
- **Monks with Class**, **Sturdy Brawlers**, **Swashbucklers with Class**,
  **Swashbuckling 101: Combat** — martial character-build advice/options; distilled crunch is in
  `lore/fulltext/supplements-crunch.md` (search with `lore_search.py`).
- **Masters of Magic.pdf** — the rarity of high-level arcanists in Eberron (world-primer.md).
- **Intrigue and Betrayal.pdf** — noir tone/GM craft (world-primer.md).
- **dnd_re_20040223a.pdf** ("Random Encounters: Nasty Surprises") — perils beyond death: **magic-item
  loss** and **ability-score loss** as scarier stakes than dying.
- **More Divinity.pdf** — four divine PrCs incl. the **Dweomerkeeper** (prestige-classes.md).

## The OGL SRD (open content — safe to quote)
- **`references/SRD-OGL_V1.1-full.txt`** — the complete System Reference Document 5.1 under the Open
  Game License v1.0a. Grep/read it for any open rule, condition, spell, class feature, magic item, or
  monster and quote it directly. Key ready-made tables are distilled in **srd-quick-tables.md**.
