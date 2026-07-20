# Master Catalog — DND Bot Project Library

This catalog lists every known file in the "DND Bot" Perplexity project library, organized by
category with a one-line description. The project holds ~498 files; the entries below are the
files confirmed by content extraction and by project search indexes (mined from
`current_session_context/tool_calls/search_files/*.json` and the project file listing).

## How to retrieve a file at runtime
At runtime, use the `search_files` tool (a.k.a. `search_files_v2` / the `files` connector) with a
query matching the topic or the filename. Matching PDFs are downloaded to
`/home/user/workspace/space_files/…` and can then be opened with the `read` tool. Prefer searching
by the distinctive words in the title (e.g. `House Phiarlan Serpentine Table`, `Heirs of Dhakaan
duur'kala`, `Droaam Graywall`). Full rulebooks (Monster Manual, PHB, DMG, Fizban's) are large —
search for the specific creature/rule/spell rather than downloading the whole book.

Note: files whose names end in `-1`, `-2`, or contain `Copy` are duplicates of the base file and
were processed once. Distilled facts from these documents live in the sibling reference files
(dragonmarked-houses.md, nations.md, religions.md, organizations.md, races-cultures.md,
psionics.md, prestige-classes.md, bestiary.md, news-gazette.md, adventure-hooks.md).

---

## Eberron Dragonshards — lore articles (by Keith Baker et al.)
- **House Phiarlan, Part One.pdf** — Origins of the shadow house: Xen'drik "spirit keepers," exodus to Aerenal, Undying Court, fall of the line of Vol, Mark of Shadow, split to Khorvaire → distilled in dragonmarked-houses.md.
- **House Phiarlan, Part Two.pdf** — Public face: five-headed hydra symbol, mask of shadows, Five Demesnes (Memory/Motion/Music/Shape/Shadow) and their cities, Carnival of Shadows.
- **House Phiarlan, Part Three.pdf** — The Serpentine Table (secret espionage arm), hiring costs, agent ranks (Shadows/Wraiths/Spectres/Ghosts/Lords).
- **Heirs of Dhakaan.pdf** — Dhakaani goblinoid empire remnants in Darguun: hobgoblin/bugbear/goblin roles, duur'kala dirge singers, Silent Clans → organizations.md.
- **The Children of Khyber.pdf** — Aberrant dragonmarks and House Tarkanan; the "child of Khyber" prestige class → prestige-classes.md & organizations.md.
- **Blades of the Quori.pdf** — Kalashtar/Inspired martial traditions (path of shadows, soulknife, jilashtora/ojilashta/tashalantora), Flowing Blade feat → psionics.md & races-cultures.md.
- **Church of the Silver Flame, Part 1.pdf** — Core beliefs, Tira Miron, the Purge of lycanthropes, corruption → religions.md.
- **Church of the Silver Flame, Part 2.pdf** — Ministers, templars, paladins, friars, pilgrims, corruption types, favored weapon (longbow) → religions.md.
- **Druids of Khorvaire, Part One.pdf** — Five druid sects, Druidic language, Shadows of the Forest (King's Forest, Breland) → religions.md.
- **Druids of Khorvaire, Part Two.pdf** — Warforged druids, druids & dragonmarks (wild shape), reincarnation table → religions.md & races-cultures.md.
- **Dwarves of the Mror Holds, Part 2.pdf** — Mror national character, fashion, battle, magic, gnome immigration, the twelve clans → nations.md & races-cultures.md.
- **Lycanthropes and the Purge.pdf** — Origins of lycanthropy, the 800s YK Purge by the Silver Flame, shifters, modern age → religions.md.
- **Monastic Orders.pdf** — Order of the Broken Blade (Dol Dorn), the Flayed Hand (the Mockery), the Shaarat'khesh → religions.md & organizations.md.
- **Psionics in Eberron.pdf** — Dal Quor/Xoriat theory, Sarlona, psionics in Khorvaire, kalashtar-without-psionics rule → psionics.md.
- **Intrigue and Betrayal.pdf** — Noir tone guidance: betrayals, double agents, uncertain allies for Eberron games → world-primer.md.
- **Masters of Magic.pdf** — Rarity of true high-level arcanists (artificers, wizards, sorcerers) in Eberron → world-primer.md.
- **Strike Force: Dhakaan.pdf** — Dhakaani strike-force tactics and encounter templates for high-level parties → adventure-hooks.md & organizations.md.

## Eberron Expanded — sourcebook-adaptation articles (Keith Baker)
- **Heroes of Battle, Part One.pdf** — Adapting *Heroes of Battle* mass-combat rules to Eberron (Last War battles) → rules-supplements.md.
- **Heroes of Battle, Part Two.pdf** — More battlefield/mass-combat adaptation for Eberron.
- **Libris Mortis, Part One.pdf** — Adapting *Libris Mortis* undead to Eberron (Karrnath, Blood of Vol) → bestiary.md.
- **Libris Mortis, Part Two.pdf** — More undead adaptation (Queen of the Dead, etc.).
- **Complete Psionic.pdf** — Adapting *Complete Psionic* (Six Hidden Houses, ardents, lurks) to Eberron → psionics.md.

## Religions & divine reference
- **Religion in Eberron.pdf** — Overview of Eberron faiths (retrieve at runtime; not extracted).
- **More Divinity.pdf** — Web enhancement for *Complete Divine*: four divine prestige classes (Dweomerkeeper, etc.) → prestige-classes.md.
- **FR_Faiths_Enhance.qxd.pdf** — *Faiths & Pantheons* / Forgotten Realms faith enhancement material (crunch reference) → rules-supplements.md.

## Prestige classes & character options
- **The Body Leech (Prestige Class).pdf** — Evil psionic PrC that drains trapped victims; includes the tether hound creature → prestige-classes.md & bestiary.md.
- **Psychic Theurge (Prestige Class).pdf** — Combines divine casting with psionic manifesting → prestige-classes.md.
- **Expanded Classes, Part Four.pdf** — Psionic expanded classes (ardent, divine mind, lurk, erudite) from PHB II/Complete Psionic → psionics.md.
- **Guile, the Warforged Ninja.pdf** — Warforged ninja NPC (agent of House Phiarlan/Shadow, possibly Lord of Blades) with stat blocks by level → bestiary.md & races-cultures.md.
- **Monks with Class.pdf** — Advice and options for playing/building monks → rules-supplements.md.
- **Dragon Shaman -- Elemental Warrior.pdf** — Using the PHB II dragon shaman class → rules-supplements.md.
- **Sturdy Brawlers.pdf** — Brawler/unarmed-combat character options (retrieve at runtime; not extracted).
- **Swashbuckling 101: Combat.pdf** — Swashbuckler combat tactics (retrieve at runtime; not extracted).
- **Swashbucklers with Class.pdf** — Swashbuckler class options (retrieve at runtime; not extracted).
- **091913 Feats.pdf** — Feat compilation (retrieve at runtime for specific feats).
- **Psionics of Incarnum.pdf** — Merges *Magic of Incarnum* with psionics (feats, powers, PrCs) → psionics.md.

## Fight Club / stat-block NPCs & monsters
- **Taibo, the Ethereal Filcher Monk.pdf** — Ethereal filcher/monk NPC with hit-and-run ethereal tactics → bestiary.md.
- **Imbrudar.pdf** — "Brain in a jar" undead psion crime-lord, scaling stat blocks → bestiary.md.
- **Reptilian Tool of Tiamat.pdf** — Bhissok, reptilian bugbear warmage / Talon of Tiamat → bestiary.md.
- **Beshappal, the Vrock Berserker.pdf** — Advanced vrock/barbarian demon, Dance of Ruin → bestiary.md.
- **Chuladoal.pdf** — Fiendish gravetouched-ghoul swarm-shifter (pyro-)troll, scaling CR 8–15 → bestiary.md.
- **Drashan Daverund.pdf** — Maur (devolved storm giant) hulking hurler, drow slave → bestiary.md.
- **Four New Psionic Monsters.pdf** — Dreamfane (CR 9), Gruesome Lurker (CR 3), Spryjack (CR 3), Usunag (CR 8) → bestiary.md.
- **Aleam Valassar, Paladin Assassin.pdf** — Janni paladin secretly possessed by a fiend (assassin); dual stat blocks → bestiary.md.
- **06 House Of Harpies.pdf** — Adventure locale/encounter: a thieves' guild hideout in the trees, harpies → adventure-hooks.md & bestiary.md.

## Steal This Hook! — adventure-hook articles (Doug Beyer, Robert Wiese)
- **Airship Action.pdf** — Airship-themed hooks (Lord of Blades trap, Wistful Wanderer, Mournland storm) → adventure-hooks.md.
- **Mini-Hook Madness.pdf** — 40+ one-line Eberron hooks → adventure-hooks.md.
- **Mysterious Disappearances.pdf** — Disappearance-themed hooks (locked vault, missing mummy, vanished rail car) → adventure-hooks.md.
- **Faith and Deed.pdf** — Religion-themed hooks (stolen dragonshard holy symbol, etc.) → adventure-hooks.md.
- **A Place to Call Home.pdf** — "Home under threat" hooks (Mror Holds magma at the Fist of Onatar) → adventure-hooks.md.
- **"Let's Make a Deal".pdf** (`_Let_s Make a Deal_.pdf`) — Villain-alliance hooks → adventure-hooks.md.
- **Ravaging Monsters.pdf** — Monster-fight hooks tied to *Monster Manual V* (burrow roots, etc.) → adventure-hooks.md.
- **Relics of a Bygone Age.pdf** — Ancient-relic hooks (retrieve at runtime; not extracted).

## Eberron news items — the *Sharn Inquisitive* / *Korranberg Chronicle* (998 YK)
All by David Noonan; each is a dated in-world newspaper story usable as a session hook → news-gazette.md.
- **Prince Aejar's Climbing Expedition to Mount Herrian Overdue.pdf** — Zarantyr 8, 998; Brelish prince lost in the Blackcaps.
- **Lyrandar Investigates Mysterious Lights.pdf** — Zarantyr 6, 998; glowing lights swarm airships over Sharn.
- **Droaam Hordes Press Graywall Defenders.pdf** — Therendor 1, 998; Daughters of Sora Kell assault Graywall.
- **Lhazaar Investment Pacts Announced.pdf** — Therendor 8, 998; House Tharashk dragonshard ventures in the Principalities.
- **Aundair Army Captures Rebel Leader.pdf** — Barrakas 8, 998; Ashbound druid Amleerin the Fox captured.
- **Relief Convoy Attacked in Aundair.pdf** — Nymm 8, 998; aid caravan destroyed near Salanoux.
- **'Dragonslayer' Sniper Claims Sixth Victim.pdf** — Nymm 8, 998; crossbow sniper kills dragonmarked heirs in Sharn.
- **Lhazaar Volcano Erupts.pdf** — Lharvion 8, 998; Mount Cathanikau erupts.
- **Eldeen Wolves Seize Expedition.pdf** — Dravago 22, 998; Eldeen Wolves kidnap Wynarn University expedition.
- **House Lyrandar Mulls New Airship Routes.pdf** — Sypheros 22, 998; proposed new towers to Stormreach etc.
- **Dream Serpent Hides Become Fashion.pdf** — Rhaan 22, 998; Xen'drik dream-serpent capes trend in Korranberg.
- **Banditry Delays Airship's Maiden Voyage.pdf** — Aryth 22, 998; Howling Peaks bandits burn a Power of Purity airship.
- **Repairs Interrupt Lightning Rail.pdf** — Lightning-rail repair news (retrieve at runtime; not extracted).
- **Red Gauntlet Regiment Reunites in Sharn.pdf** — Karrnathi veterans reunion news (retrieve at runtime; not extracted).
- **Researchers Crack Code of Vvaraak.pdf** — Prophecy/Gatekeeper research news (retrieve at runtime; not extracted).
- **Revival of Wyvern Hunt Takes 12 Wyverns.pdf** — Wyvern-hunt news (retrieve at runtime; not extracted).
- **Report: "Critical Gaps" Exist in Graywall Defenses.pdf** — Graywall defense report (retrieve at runtime; not extracted).
- **Sudden Retirements Leave Phiarlan Musicians in Demand.pdf** — Phiarlan entertainer news (retrieve at runtime; not extracted).

## Larger adventures / locations
- **TARTH MOORDA.pdf** — Large adventure/location document (retrieve at runtime; not extracted) → adventure-hooks.md.
- **DnD_Theaters_of_Death.pdf** — *Heroes of Battle* web enhancement: battlefield encounters for characters level 4–10 → adventure-hooks.md & rules-supplements.md.
- **D&D 5e - Princes of the Apocalypse.pdf** — 5e adventure: four elemental cults (Black Earth, Howling Hatred, Crushing Wave, Eternal Flame) in the Dessarin Valley → adventure-hooks.md & rules-supplements.md.
- **D&D 5e - Dragon Delves.pdf** — 5e anthology of dragon-themed short adventures → rules-supplements.md.

## Rulebooks & supplements (large — index only; search at runtime for specifics)
- **SRD-OGL_V1.1.txt** — System Reference Document (5.1, Open Game License). Full text bundled at `references/SRD-OGL_V1.1-full.txt`; distilled tables in srd-quick-tables.md.
- **Player's Handbook [2024]_djvu.txt** — 2024 (5.5e) Player's Handbook. Copyrighted; index in rules-supplements.md.
- **Monster Manual [2024]_djvu.txt** — 2024 Monster Manual. Copyrighted; index in rules-supplements.md & bestiary.md.
- **Monster Manual_djvu.txt** — 5e (2014) Monster Manual. Copyrighted.
- **Monster Manual Expanded 1_djvu.txt** — 3rd-party MM Expanded vol. 1 (new stat blocks & variants).
- **Monster Manual Expanded 2_djvu.txt** / **Monster Manual Expanded 2 v1_djvu.txt** / **Monster Manual Expanded 2(Copy)_djvu.txt** — MM Expanded vol. 2 (dupes).
- **Monster Manual Expanded 3_djvu.txt** — MM Expanded vol. 3.
- **Dungeon Master's Guide_djvu.txt** — 5e Dungeon Master's Guide. Copyrighted.
- **fizban's treasury of dragons.pdf** — 5e dragon splatbook (gem/metallic/chromatic dragons, Way of the Ascendant Dragon monk). Copyrighted.
- **Player_s Handbook II.pdf** — 3.5e PHB II (dragon shaman, expanded classes). Copyrighted.
- **D_D Complete Warrior.pdf** — *Complete Warrior* web enhancement: Order of the Chalice expansion (demon-hunting knights). 
- **Stronghold Enhance.qxd.pdf** — *Stronghold Builder's Guidebook* enhancement (base/stronghold construction) → rules-supplements.md.
- **dnd_re_20040223a.pdf** — "Random Encounters: Nasty Surprises" column (magic-item loss, ability loss perils).
- **pasted-text.txt** — Large pasted rules/reference text dump (retrieve/inspect at runtime if needed).
