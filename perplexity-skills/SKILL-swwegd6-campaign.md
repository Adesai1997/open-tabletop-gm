---
name: SKILL-swwegd6-campaign
description: Star Wars D6 Rebellion-era campaign context — Ord Mantell, NPCs, factions, arc, SWAPI integration guide, and sourcebook extension format.
tags: [star-wars, campaign, weg-d6, rebellion-era, swapi]
---

# Star Wars D6 — Campaign Context
*Upload this file to Perplexity Computer alongside SKILL-gm-core.md and SKILL-swwegd6-rules.md.*
*This file provides the GM with a working Rebellion-era campaign setup and instructions for SWAPI integration and future sourcebooks.*

---

## Default Campaign: The Spark That Lights the Flame

**Era:** Galactic Civil War — approximately 1 BBY
**Primary Location:** Ord Mantell — Worlport Starport District
**Tone:** Lived-in, morally grey, scrappy. Han Solo energy. Death Star not yet destroyed.

### Campaign Arc (6-Beat Structure)

| Beat | Status | What Changes |
|---|---|---|
| Inciting Incident | pending | The cargo job the party is running is connected to Imperial intelligence project COBALT |
| Complication | pending | An Imperial Inquisitor arrives on Ord Mantell |
| Midpoint Shift | pending | The party must choose: run with the credits, or help the Rebels |
| All Is Lost | pending | A key Rebel contact is captured |
| Final Confrontation | pending | Disrupt Project COBALT or escape with the intelligence |
| Resolution | pending | The galaxy is different based on the choice made |

---

## World

**Ord Mantell:** Mid Rim world. Imperial customs presence, notorious for crime syndicates. Worlport is a dense starport city of cantinas, black markets, junkyards, and industrial districts.

**Setting atmosphere:** Humid, overcast, smells of ozone and ration packs. The Empire is present but corrupt — local Moffs look the other way for credits. Betrayal is a live possibility from almost every NPC.

### Key Locations

| Location | Notes |
|---|---|
| Docking Bay 94B | Party's ship; starting location |
| The Grinding Wheel Cantina | Faction hub; Darro's meeting spot |
| Scrapyard District (Sector 9) | Rebel cell safehouse |
| Imperial Customs Station Kappa | Checkpoints on all off-planet departures |
| Zann Consortium Waystation | Debt collection; avoid if possible |

---

## Factions

| Faction | Disposition | Notes |
|---|---|---|
| Galactic Empire / Project COBALT | Antagonist | Intelligence cell hunting Rebel sympathisers |
| Rebel Alliance — Sabre Cell | Potential ally | Underground cell; low on credits and trust |
| Zann Consortium | Neutral/threat | Crime syndicate; party owes them money |
| Darro's Network | Unknown | Contact whose loyalties are ambiguous |

---

## NPCs

### Darro Vel
**Species:** Bothan | **Type:** Independent cargo broker / Rebel sympathiser
**Attributes:** DEX 2D+1 | KNO 3D+2 | MEC 2D | PER 4D | STR 2D | TEC 2D
**Key Skills:** bargain 5D, streetwise 4D+2, persuasion 4D+1, con 4D, search 3D+1
**FP:** 1 | **CP:** 3 | **DSP:** 0 | **Wound:** Healthy
**Personality:** Cautious, dry humour, deeply loyal to those he's vouched for. Paranoid in crowds.
**Secret:** The cargo is encrypted Rebel cell communications. He doesn't know the Empire has already flagged him.
**Quote:** *"I don't ask what's in the crates. You shouldn't either."*

---

### Inquisitor Veth Naraal *(Do not introduce before the Complication beat)*
**Species:** Human | **Type:** Imperial Inquisitor
**Attributes:** DEX 4D+1 | KNO 3D | MEC 3D | PER 4D | STR 3D+2 | TEC 2D+1
**Key Skills:** lightsaber 6D, dodge 5D, intimidation 5D, search 4D+2, sense 4D, control 3D+2
**Force Powers:** lightsaber combat, sense path, combat sense, danger sense, affect mind
**FP:** 3 | **CP:** 5 | **DSP:** 4 | **Wound:** Healthy
**Personality:** Ice-cold professionalism. She does not negotiate. She collects.
**Quote:** *"You are not the target. Tell me where the target is, and this ends."*
**GM Note:** Naraal is a living dark side temptation for Force-sensitive party members. She knows it and uses it.

---

### Prexis "Prex" Dhul
**Species:** Sullustan | **Type:** Rebel cell technician / slicer
**Attributes:** DEX 2D+1 | KNO 3D | MEC 3D+2 | PER 3D | STR 2D | TEC 5D
**Key Skills:** computer programming/repair 6D+2, astrogation 5D, security 4D+1, space transports repair 4D+1
**Special Ability:** +1D astrogation; +1D search in underground/enclosed spaces (Sullustan species trait)
**FP:** 1 | **CP:** 3 | **DSP:** 0 | **Wound:** Healthy
**Personality:** Excitable, talks fast, trusts competence over credentials.
**Quote:** *"I can get you out. I just need eight minutes and for everyone to stop shooting at me."*

---

## Active Quests

**The Cobalt Job** — Deliver a sealed cargo container to "Darro" at Docking Bay 94B. Pay: 2,000 credits. No questions asked. Status: active.

**Debt & Complications** — One character owes 5,000 credits to the Zann Consortium. First payment due in 3 sessions.

---

## GM Style Notes

*(Update this section after each session as you learn what this player responds to.)*

---

## SWAPI Integration

**What SWAPI covers:** Canonical data from the six theatrical films (Episodes I–VI) — characters, planets, species, starships, vehicles, films.

**API endpoint:** `https://swapi.dev/api/`

**Available resources:**
- `/people/` — characters (height, mass, birth year, homeworld, films)
- `/planets/` — planetary data (climate, terrain, population, diameter)
- `/starships/` — starship specs (MGLT, hyperdrive rating, crew, passengers, cargo capacity, consumables)
- `/vehicles/` — ground/atmo vehicle specs
- `/species/` — species data (classification, average lifespan, language, homeworld)
- `/films/` — film metadata

**How to use in play:**
When a player encounters a canonical entity (Millennium Falcon, Hoth, Wookiees, X-Wing, Leia Organa), call the SWAPI endpoint for that resource and adapt the canonical stats to WEG D6 notation. For example:

- `GET https://swapi.dev/api/starships/?search=Millennium+Falcon` → returns hull length, hyperdrive rating, MGLT, crew count. Use for WEG D6 starship stats.
- `GET https://swapi.dev/api/species/?search=Wookiee` → returns average height, lifespan, language. Use for in-game description and roleplaying.
- `GET https://swapi.dev/api/planets/?search=Ord+Mantell` → confirms film appearance, terrain.

**What SWAPI does NOT cover:** Legends/EU content, WEG sourcebook-original species/planets, post-Episode VI material. For those, use sourcebook stats directly or create original ones.

**If SWAPI is unavailable or returns no match:** Note "SWAPI: no canonical data — using sourcebook/improvised stats" and proceed. This never blocks play.

---

## Sourcebook Extensions

The core rulebook is the foundation. Any WEG Star Wars sourcebook can be added as an extension file.

### Extension file format

Create a file named `SKILL-swwegd6-[sourcebook-name].md` with YAML frontmatter:

```
---
name: SKILL-swwegd6-[sourcebook-name]
description: [Sourcebook Name] extension for WEG Star Wars D6.
tags: [star-wars, weg-d6, sourcebook]
---

# [Sourcebook Name] — WEG Star Wars Extension
*Supplement to SKILL-swwegd6-rules.md and SKILL-swwegd6-campaign.md*

## New Species
## New Vehicle/Starship Stats
## New Equipment
## New Templates
## New Locations
## GM Adventure Seeds
```

### Priority sourcebooks to add

| Sourcebook | What it adds |
|---|---|
| Galaxy Guide 1: A New Hope | Film-accurate templates, Mos Eisley detail |
| Galaxy Guide 6: Tramp Freighters | Expanded smuggler life, ship customisation, cargo tables |
| Galaxy Guide 8: Scouts | Wilderness survival, scout templates, exploration rules |
| Galaxy Guide 9: Fragments from the Rim | Fringe characters, crime lord tables, Hutt Space |
| Heroes & Rogues | 20+ detailed character templates |
| Creatures of the Galaxy | Full bestiary with stats |
| Planets of the Galaxy Vol. 1–3 | Detailed planet entries for all major worlds |
| Dark Empire Sourcebook | Post-RotJ era, Emperor reborn arc |

---

## Character Sheet Format

When tracking a character in conversation, use this compact format:

```
**[Character Name]** ([Species] [Template])
DEX Xd | KNO Xd | MEC Xd | PER Xd | STR Xd | TEC Xd
Key Skills: [skill Xd, skill Xd, ...]
FP: X | CP: X | DSP: X
Wound: [Healthy / Stunned / Wounded / Wounded Twice / Incapacitated / Mortally Wounded]
Equipment: [list]
Notes: [background, connections, debts]
```
