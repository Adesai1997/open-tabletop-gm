# Star Wars D6 — Session Start Checklist
*Upload this file to Perplexity Computer alongside the other SKILL files.*
*Read this file at the start of every session.*

---

## Before You Begin

Tell the GM the following at session start:

1. **Character name and sheet** — paste your character in compact format (see SKILL-swwegd6-campaign.md for format)
2. **Campaign state** — paste or summarise:
   - Current location
   - Active quests and their status
   - Current wound level
   - Current CP, FP, and DSP totals
   - Any factions you've interacted with and their current attitude
3. **Which arc beat is next** (from the six-beat arc)
4. **Any sourcebook extensions in use** (e.g. "Galaxy Guide 6 is active")

---

## Session Start Prompt (copy-paste this)

> I'm ready to play. Here's my current state:
>
> **Character:** [Name] — [Species] [Template]
> DEX Xd | KNO Xd | MEC Xd | PER Xd | STR Xd | TEC Xd
> Key Skills: [list]
> FP: X | CP: X | DSP: X | Wound: [level]
> Equipment: [list]
>
> **Campaign:** [campaign name]
> Location: [current location]
> Active quests: [list]
> Next arc beat: [beat name]
> Factions: [status with each faction]
>
> **Extensions active:** [list any sourcebook files, or "none"]
>
> Please load SKILL-gm-core.md, SKILL-swwegd6-rules.md, SKILL-swwegd6-campaign.md, and this file, then begin the session.

---

## GM Startup Sequence

When the session prompt arrives, the GM will:

1. Confirm all uploaded skill files are loaded
2. Read GM Style Notes (SKILL-swwegd6-campaign.md) for calibration
3. Note the next arc beat and plan how to advance it naturally
4. Check SWAPI for any canonical entities in the current location
5. Open the session with a grounding paragraph: **where you are, what you sense, what the immediate tension is**
6. Enter GM mode — no command prefix needed after that

---

## Between Sessions

After each session, record:

```
Session [N] notes:
- CP awarded: [X] (for [reason])
- FP awarded: [X] (for [reason])
- DSP gained: [X] (for [reason])
- Wound level at end: [level]
- Arc beat status: [beat name] — [pending / triggered / complete]
- Key NPC attitude changes: [list]
- Faction moves this session: [list]
- Open threads for next session: [list]
```

---

## Quick Rules Card

**Rolling:** State the action → GM sets difficulty → roll XD (+pips) → compare to difficulty

**Wild Die (different-colour die):** 6 = exploding (roll again, add); 1 = complication

**Multiple actions in a round:** Every action after the first costs −1D to ALL rolls

**Damage resolution:** Attacker rolls weapon damage → Defender rolls Strength (+ armor) → compare difference to wound track

**Spend Character Points:** After rolling, before GM declares result → +1D to that roll

**Spend Force Points:** Declare before rolling → double ALL dice this round (cannot combine with CP)

**Dark Side Point:** Awarded by GM for evil acts; stack up to Perception score before falling to the dark side

**Difficulty Numbers at a glance:**
- Very Easy: 1–5
- Easy: 6–10
- Moderate: 11–15
- Difficult: 16–20
- Very Difficult: 21–30
- Heroic: 31+

---

## SWAPI Quick Reference

Pull canonical data mid-session:

| Want to know | URL |
|---|---|
| A character's stats | `https://swapi.dev/api/people/?search=[name]` |
| A planet's details | `https://swapi.dev/api/planets/?search=[name]` |
| A starship's specs | `https://swapi.dev/api/starships/?search=[name]` |
| A vehicle's specs | `https://swapi.dev/api/vehicles/?search=[name]` |
| A species' data | `https://swapi.dev/api/species/?search=[name]` |

If the entity isn't in SWAPI (EU/Legends/WEG-original), use sourcebook stats or improvise.

---

## Adding Sourcebooks Mid-Campaign

1. Upload `SKILL-swwegd6-[sourcebook-name].md` to Perplexity Computer
2. In your session start prompt, add it to "Extensions active"
3. Tell the GM explicitly which sourcebook templates, species, or locations you want to draw from that session
4. The GM will reference the file for those stats — it doesn't change the core rules, it adds options

---

## File Load Order

When uploading to Perplexity Computer, upload in this order:

1. `SKILL-gm-core.md` — GM persona and craft (always required)
2. `SKILL-swwegd6-rules.md` — mechanical rules (always required)
3. `SKILL-swwegd6-campaign.md` — campaign, NPCs, SWAPI, sourcebook guide (always required)
4. `SKILL-session-start.md` — this file (always required)
5. `SKILL-swwegd6-[sourcebook-name].md` — any extensions (optional, per session)

All four core files together = ~29,000 characters, well within Perplexity Computer's context budget.
