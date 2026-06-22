# WEG Star Wars D6 — System Module

This directory contains the complete **West End Games Star Wars Roleplaying Game (2nd Edition Revised, 1996)** port for open-tabletop-gm.

---

## Files

| File | Purpose |
|---|---|
| `system.md` | Full D6 rules context loaded alongside `SKILL.md` at session start |
| `character.py` | Character creation, sheet display, CP/FP/DSP tracking, skill improvement |
| `swapi_lookup.py` | SWAPI integration — pull canonical film data for people, planets, species, vehicles, starships |

---

## Quick Start

### 1. Start a session

Load the system module alongside the GM skill:

```
/gm new my-rebellion-campaign swwegd6
```

Or manually specify the system file path in your OpenCode config.

### 2. Create a character

```bash
python3 systems/swwegd6/character.py new
python3 systems/swwegd6/character.py sheet "Han Solo"
```

### 3. Track conditions in play

```bash
# Wounded by a blaster bolt
python3 scripts/tracker.py -c my-campaign condition add "Thannik" wounded

# Force Point spent this round
python3 scripts/tracker.py -c my-campaign condition add "Thannik" force-point-active

# Award Force Points after a heroic act
python3 systems/swwegd6/character.py update "Thannik" fp +1

# Spend Character Points between sessions to improve blaster by 1 pip
python3 systems/swwegd6/character.py improve "Thannik" blaster 1
```

### 4. Look up a canonical Star Wars entity

```bash
python3 systems/swwegd6/swapi_lookup.py people "Leia Organa"
python3 systems/swwegd6/swapi_lookup.py starships "Millennium Falcon"
python3 systems/swwegd6/swapi_lookup.py planets Hoth
```

---

## Wound Track Quick Reference

| Status | Die Penalty | Recovery |
|---|---|---|
| Stunned | −1D (2 rounds) | Auto-clears; rest removes sooner |
| Wounded | −1D all rolls | Medpac (Easy) or 3 days rest + STR roll |
| Wounded Twice | −2D all rolls | Medpac (Moderate) or 3 days rest + STR roll |
| Incapacitated | Unconscious 10D min | Moderate first aid; 2 weeks + STR roll |
| Mortally Wounded | Unconscious; 2D death check each round | Difficult first aid + bacta within 1 hr |
| Killed | Dead | New character |

---

## Extensibility

**More sourcebooks:** Add a `## Sourcebook: [Name]` section to `system.md` for Galaxy Guide entries, Heroes & Rogues templates, Dark Empire rules, etc.

**SWAPI:** `swapi_lookup.py` covers Episodes IV–VI. For Legends/EU content, use WEG sourcebook stats. The lookup script gracefully returns a "use sourcebook" message for unknown entities.

**Other systems:** Nothing in this directory affects other system modules. Add a parallel `systems/<other-system>/` folder for any other game.
