# System Module — Star Wars Roleplaying Game (2nd Edition Revised, West End Games)

<!--
Source: Star Wars Roleplaying Game 2nd Edition Revised & Expanded (West End Games, 1996)
D6 System — Licensed under open-tabletop-gm system module format.

This file is loaded alongside SKILL.md at session start. It defines the full D6 mechanics
for WEG Star Wars. Designed to leave the door open for supplemental sourcebooks and SWAPI
integration — see ## Extensibility section at the bottom.
-->

---

## Dice Convention

**Core resolution:** Roll a pool of six-sided dice (XD+Y notation) against a Difficulty Number set by the GM.
If your roll meets or exceeds the Difficulty, you succeed. Skills default to their governing Attribute die code if not improved.

**Die codes:** Written as `3D`, `4D+2`, etc. The number before D is how many d6 to roll; the +1/+2 is added to the total.
`2D` = average ability. `4D` = competent professional. `6D+` = elite specialist.

**Difficulty Scale:**

| Difficulty | Range | Example |
|---|---|---|
| Very Easy | 1–5 | Driving a speeder on an empty road |
| Easy | 6–10 | Firing a blaster at medium range |
| Moderate | 11–15 | Repairing a starfighter engine |
| Difficult | 16–20 | Piloting through an asteroid field |
| Very Difficult | 21–30 | Decrypting Imperial military codes |
| Heroic | 31+ | Hitting an exhaust port with a proton torpedo |

GMs may pick a fixed number or randomly roll within a range (e.g., Moderate = roll 3D–4D for difficulty).

**Opposed Rolls:** When acting against another character, both roll their skills. Higher total wins. On a tie, the initiating character wins.

**Multiple Actions:** Each additional action in a round applies a cumulative −1D penalty to ALL rolls that round.
- 2 actions: −1D to all
- 3 actions: −2D to all
- 4 actions: −3D to all, and so on

Reaction skills (dodge, melee parry, brawling parry) may be declared after being attacked and count as an extra action.

**The Wild Die:** One of the rolled dice is designated the Wild Die (different color). Results:
- **2–5:** Add normally
- **6:** Add 6 and roll again; keep adding as long as 6s appear (exploding die)
- **1:** The GM chooses: add normally, subtract the Wild Die + highest die, or add normally but a complication occurs

**Modifiers:** GMs may add flat bonuses to a character's roll for clear advantages (not for superior skill — use opposed rolls for that):
- +1–5: Slight advantage
- +6–10: Good advantage
- +11–15: Decisive advantage
- +16: Overwhelming advantage

**Example Inline Combat Narration:**
`Thannik attacks Stormtrooper: Blaster (Heavy Pistol) 5D vs. Dodge 4D — Thannik: 17, Trooper: 12 — Hit! Damage 5D = 18 vs. Strength 3D = 9 — Wounded!`

---

## Ability Scores / Statistics

Characters have **six Attributes**, each rated in die codes (human range typically 2D–4D at creation):

| Attribute | Abbreviation | Governs |
|---|---|---|
| Dexterity | DEX | Agility, ranged combat, dodging, throwing |
| Knowledge | KNO | Education, galactic lore, languages, streetwise |
| Mechanical | MEC | Piloting vehicles and starships, astrogation, gunnery |
| Perception | PER | Awareness, persuasion, deception, gambling, sneaking |
| Strength | STR | Physical power, health, damage resistance, brawling |
| Technical | TEC | Repair, programming, demolitions, first aid |

**No modifier conversion.** Attributes and skills are used directly as die pools. There is no derived modifier — a Dexterity of 3D+2 means roll 3d6 and add 2.

**Human starting Attribute Dice:** 18D total, distributed across the six attributes within species minimums/maximums (typically 2D min, 4D max per attribute at creation).

**Skills** are listed beneath their parent attribute and begin at the attribute's die code. Adding dice to a skill raises the number in front of D. Specializations (e.g., Blaster: Blaster Pistol) add +1D for that specific use only.

**Force Skills** (Force-sensitive characters only): Control, Sense, Alter — each begins at 1D when learned from a teacher and improve separately.

---

## Core Skill List

### Dexterity Skills
blaster, blaster artillery, brawling parry, dodge, grenade, lightsaber, melee combat, melee parry, missile weapons, running, thrown weapons, vehicle blasters

### Knowledge Skills
alien species, bureaucracy, cultures, intimidation, languages, law enforcement, planetary systems, scholar, streetwise, survival, willpower

### Mechanical Skills
astrogation, beast riding, capital ship gunnery, capital ship piloting, capital ship shields, communications, ground vehicle operation, hover vehicle operation, repulsorlift operation, sensors, space transports, starfighter piloting, starship gunnery, starship shields, swoop operation

### Perception Skills
bargain, command, con, forgery, gambling, hide, investigation, persuasion, search, sneak

### Strength Skills
brawling, climbing/jumping, lifting, stamina, swimming

### Technical Skills
armor repair, blaster repair, capital ship repair, computer programming/repair, demolitions, droid programming, droid repair, first aid, ground vehicle repair, hover vehicle repair, repulsorlift repair, security, space transports repair, starfighter repair, starship weapons repair, (A) medicine, (A) starfighter engineering, (A) space transports engineering

### Force Skills (Force-Sensitive Only)
control, sense, alter

**Advanced Skills (prefix A):** Require a prerequisite skill at 5D+ to attempt. Begin at 1D when purchased, not at attribute level.

---

## Character Structure

| Field | Tracking Notes |
|---|---|
| Attributes (6) | Fixed at character creation; improve only by spending Character Points between adventures |
| Skills | Tracked separately under each attribute; improve with Character Points |
| Wounds | 5-level track: Stunned → Wounded → Wounded Twice → Incapacitated → Mortally Wounded → Killed |
| Force Points | Starts at 1 (non-sensitive) or 2 (Force-sensitive); spent for double dice in a round |
| Character Points | Starts at 5; spent for +1D on a roll or to improve skills between adventures |
| Dark Side Points | Accumulated for evil acts; enough turns a character to the Dark Side (GM character) |
| Move | Default 10 meters/round for humans |
| Force Sensitivity | Yes or No; affects Force Point starting count and Force skill access |
| Equipment | Weapons, armor, gear — tracked in character file |
| Credits | Currency; tracked in character file |

---

## Health and Damage

**Damage Resolution:**
1. Attacker rolls weapon damage die code
2. Defender rolls full Strength (armor adds dice to Strength for damage resistance only — not other Strength rolls)
3. Find the difference (Damage Roll − Strength Roll) on the Character Damage Chart:

| Difference | Result |
|---|---|
| 0–3 | Stunned |
| 4–8 | Wounded |
| 9–12 | Incapacitated |
| 13–15 | Mortally Wounded |
| 16+ | Killed |

**Wound Track (cumulative):**

| Status | Penalty | Notes |
|---|---|---|
| **Stunned** | −1D this round + next round | After 2 rounds, clears; still affects character for 30 min unless 1 min rest. Multiple stuns = unconscious for 2D min |
| **Wounded** | −1D to all rolls | Falls prone; can't act rest of round |
| **Wounded Twice** | −2D to all rolls | Wounded again while already Wounded |
| **Incapacitated** | Unconscious 10D min | Can't act; if wounded/incapacitated again → Mortally Wounded |
| **Mortally Wounded** | Unconscious; may die each round | Roll 2D at end of each round; if roll < rounds mortally wounded, dies |
| **Killed** | Character is dead | Create new character |

**Stun Weapons:** Any result worse than Stunned instead renders character unconscious for 2D minutes.

**Armor:** Adds dice to Strength for damage resistance only. Some armor causes Dexterity penalties (e.g., Stormtrooper armor: +2D physical, +1D energy, but −1D to DEX and all DEX skills).

**Scales:** Objects and vehicles exist at different scales. Apply scale modifier as adjusted dice difference when scales interact:

| Scale | Modifier |
|---|---|
| Character/Creature | +0D |
| Speeder | +2D |
| Walker | +4D |
| Starfighter | +6D |
| Capital Ship | +12D |
| Death Star | +24D |

When lower scale fires at higher scale: add modifier to attack roll; higher scale adds modifier to damage resistance.
When higher scale fires at lower scale: higher scale adds modifier to damage roll; lower scale adds modifier to dodge.

---

## Primary Resource

**Force Points**
- **Range:** Characters typically hold 1–3+ Force Points; no fixed maximum
- **Starting amount:** 1 (non-Force-sensitive) or 2 (Force-sensitive)
- **Spending:** Declare before rolling. Double all dice rolled that round. Cannot combine with Character Points in the same round. Using a Force Point in anger/fear risks earning a Dark Side Point.
- **Recovering:** Awarded by GM for heroic, selfless, or morally significant acts. Not automatically restored.
- **Display mapping:** Track Force Points as "spell slots" in the sidebar — each Force Point = 1 pip. Drain on spend, restore on GM award.

**Character Points**
- **Range:** Starts at 5; no fixed maximum; accumulates between adventures
- **Spending (in play):** Spend after a roll but before the GM declares result — adds +1D to that roll. Cannot combine with Force Points in same round.
- **Spending (advancement):** Spent between adventures to improve skills and attributes (see Advancement).
- **Display mapping:** Track as a secondary numeric counter.

**Dark Side Points**
- **Range:** 0+; if equal to or greater than Morality threshold (typically Perception attribute number), character turns to Dark Side
- **Effect while accumulating:** Each DSP grants +1D bonus to Force skill rolls — but accepting this bonus risks further DSP gain
- **Gaining:** Any act of evil, killing non-combatants, using Force out of anger or selfishness
- **Display mapping:** Track as a "danger" condition pill per point, or as a numeric counter

---

## Rests and Recovery

**Natural Healing (risky, slow):**
- Wounded: Rest 3 days → Strength roll (2–4: worsens to Wounded Twice; 5–6: stays; 7+: healed)
- Wounded Twice: Rest 3 days → Strength roll (2–4: worsens to Incapacitated; 5–6: stays; 7+: improves to Wounded)
- Incapacitated: Rest 2 weeks → Strength roll (2–6: worsens to Mortally Wounded; 7–8: stays; 9+: improves to Wounded Twice)
- Mortally Wounded: Rest 1 month → Strength roll (2–6: dies; 7–8: stays; 9+: improves to Incapacitated)

**Medpac (common healing item):**
- Requires first aid or Technical roll
- Difficulty by wound level: Stunned/Unconscious = Very Easy; Wounded/Wounded Twice = Easy; Incapacitated = Moderate; Mortally Wounded = Difficult
- Success: heals one level (Stunned → clear; Wounded → clear; Wounded Twice → Wounded; Incapacitated → Wounded Twice; Mortally Wounded → Incapacitated)
- Multiple medpacs in one day: each additional use raises difficulty one level
- Map to `calendar.py rest short` (1 hr) for medpac treatment scenes; `calendar.py rest long` (8 hrs) for overnight natural healing cycles

**Bacta Tank:**
- Requires (A) medicine skill — Very Easy difficulty regardless of wound level
- Heals all wounds — just a matter of time (Wounded: 1 hr; Incapacitated: 4D hrs; Mortally Wounded: 1D days)
- Attempting without A medicine requires Heroic first aid/Technical roll or wound worsens 2 levels

---

## Incapacitation and Death

- **Incapacitated:** Unconscious 10D minutes; stabilized by Moderate first aid roll (character wakes groggy, half-speed, no skills)
- **Mortally Wounded:** Unconscious; roll 2D at end of each round — if roll < number of rounds mortally wounded, character dies. Stabilized by Moderate first aid (survives if bacta/medpac within 1 hour)
- **Killed:** Character dies. Player creates new character.

Use `tracker.py condition add <name> incapacitated` / `mortally-wounded` to flag state.
Death save analog: use `tracker.py death-save <name>` with a 2D threshold check against rounds elapsed.

---

## Status Effects / Conditions

Update `CONDITION_COLOURS` in `scripts/tracker.py` with these Star Wars D6 conditions:

```python
CONDITION_COLOURS = {
    # Danger (red) — immediately life-threatening
    "mortally-wounded":     "danger",
    "killed":               "danger",
    "unconscious":          "danger",

    # Warn (amber) — significant impairment
    "wounded-twice":        "warn",
    "incapacitated":        "warn",
    "dark-side-1":          "warn",
    "dark-side-2":          "warn",
    "dark-side-3":          "warn",

    # Info (blue) — active condition
    "wounded":              "info",
    "stunned":              "info",
    "stun-bolt":            "info",
    "immobilized":          "info",

    # Buff (green) — beneficial
    "force-point-active":   "buff",
    "heroic-inspiration":   "buff",
    "in-cover":             "buff",
}
```

**Condition Notes:**
- `stunned` clears after 2 rounds; apply −1D. Multiple stuns equal to STR number = unconscious 2D min.
- `wounded` / `wounded-twice` persist until healed; −1D / −2D to all rolls respectively.
- `dark-side-X` tracks DSP count; X = number of points (use separate pills or a counter).
- `force-point-active` marks a round where a Force Point was declared (one round only).

---

## Advancement

**Between Adventures (Character Points):**

| Advancement | CP Cost | Training Time (with teacher) | Without Teacher |
|---|---|---|---|
| Improve skill +1 pip | Current # before D | 1 day per CP spent | 2× CP, 2× time |
| Improve attribute +1 pip | 10× current # before D | GM discretion | Rarely possible |
| Learn new Force skill (1D) | 10 CP | 1 week intensive | Requires teacher |
| Learn new Force power | 5 CP (without skill advance) | Teacher or Holocron required | — |
| Specialization (+1D to specific use) | 1D of beginning skill dice (character creation only) | — | — |

**Notes:**
- Each Force skill improvement (+1 pip) also grants the student one new Force power (teacher's choice).
- Force skill minimum to teach: 3D; teacher's skill must exceed student's.
- Characters cannot learn Force skills or powers without a teacher, Holocron, or authorized text.
- In the `xp.py` context, treat "Character Points awarded" as the XP unit. Award CPs (not XP) at end of scenes.

**CP Award Guidelines (use in place of D&D XP tiers):**

| Encounter Type | CP Award |
|---|---|
| Routine scene, no challenge | 0 |
| Minor challenge resolved cleverly | 1 |
| Significant encounter (combat, social, puzzle) | 2–3 |
| Major set piece or session climax | 3–5 |
| Exceptional roleplaying or bold play | +1 bonus |

---

## Bold Play Reward

**Reward name:** Force Points & Character Points

**Force Points** are the primary bold-play reward — awarded by the GM for heroic, selfless, or dramatically significant acts. Declare at start of a round to double all dice. A Force Point spent on the light side (genuinely selfless, protective) may be restored. One spent on aggression or dark impulses risks earning a Dark Side Point.

**Character Points** function as the secondary reward — +1D added to any single roll after the roll is made. Award 1–2 CPs for good roleplaying, clever solutions, or memorable moments.

`send.py --inspiration-award NAME` for Force Point awards; track CPs as a numeric sidebar counter.

---

## Combat Sequence

Each **round** = approximately 5 seconds of in-game time. Two phases per round:

### 1. Initiative
- Each side's character with the highest Perception rolls that attribute.
- High roll chooses whether their side acts **first or last** (re-roll ties).
- Initiative roll is a free action (no CP/FP spend, no multiple action penalty).

### 2. Roll Actions (Perception order, high to low)
- Each character declares number of actions → apply multiple action penalties.
- Characters act in Perception order within each side.
- Both sides alternate by action (not by side-then-side): after all first actions, all second actions, etc.
- Reaction skills (dodge, melee parry, brawling parry): can be declared after being attacked; counts as an extra action for the remainder of the round.

**Free Actions:** Initiative roll, short shout, grabbing an item in Easy terrain, Strength roll to resist damage, rolling Perception/control to resist Force/mental powers.

**Non-Roll Actions:** Reloading, getting info from a datapad, slow/cautious movement in easy terrain. Count as an action (reducing multi-action die codes) but no roll required.

---

## Starship and Vehicle Combat

Starship combat uses the same round structure. Key differences:

- **Piloting = Maneuverability:** Pilot rolls their starfighter piloting / space transports for dodge/evasion.
- **Gunnery:** Roll starship gunnery + fire control against target's dodge/maneuverability.
- **Shields:** Shield operator can transfer points between front/back arcs or boost a specific arc.
- **Scale modifiers** apply (see Health and Damage — Scales section above).
- **Hyperspace:** Requires astrogation roll; difficulty by route knowledge and hazards.

---

## Force Powers Reference

Force powers are organized under their skill(s). A character must be taught a power to use it. Calling on each skill required by a power is a separate action (or all in one round with multi-action penalties).

**Control Powers (sample):** Accelerate healing, control pain, detoxify poison, emptiness/hibernation trance, enhance attribute, resist stun, short-term memory enhancement.

**Sense Powers (sample):** Combat sense, danger sense, life detection, life sense, magnify senses, receptive telepathy, sense Force, sense path.

**Alter Powers (sample):** Injure/kill, telekinesis, bolt of hatred, electronic manipulation.

**Control + Sense Powers (sample):** Farseeing, lightsaber combat, projective telepathy.

**Control + Alter Powers (sample):** Accelerate another's healing, control another's pain, transfer Force.

**Control + Sense + Alter Powers (sample):** Affect mind, battle meditation, dim another's senses.

**Dark Side Powers:** bolt of hatred, injure/kill, drain energy, and any power used with dark side intent risk DSP gain.

**Difficulty:** Set by the GM based on power scope; typically Moderate for basic powers, Very Difficult or Heroic for complex or Dark Side uses.

---

## Campaign Arc Preferences

**Preferred campaign mode:** Either (improvised or imported)

**Typical arc structures:**
- **Faction-web** — ideal for political/Imperial intrigue, Rebel cell operations, bounty hunter networks
- **Hub-and-spoke** — ideal for published WEG modules (e.g., *Tatooine Manhunt*, *Strike Force: Shantipole*, *Galaxy Guide* series)
- **Linear** — heist/mission scenarios, single-session adventures

**Genre conventions:**
- The tone shifts by era: Rebellion era (scrappy underdogs, hope vs. Empire), Clone Wars era (political complexity, Jedi at the front), New Republic era (rebuilding, lingering threats)
- Moral weight of Dark Side is a live mechanic — build consequences for DSP accumulation into session arcs
- Force-sensitive characters require teacher quests and restraint; the GM should actively make Force growth feel earned and dangerous
- WEG Star Wars rewards improvisation, bold play, and cinematic action — lean into "Yes, and..." resolutions
- Death is real but not arbitrary — Mortally Wounded status gives players agency; use it dramatically

---

## Extensibility

### Additional Sourcebooks

This module is designed to be supplemented. The following WEG sourcebooks expand the system and can be incorporated as needed without modifying this core file. Add supplemental rules as separate sections appended to this file or as linked sub-files in `systems/swwegd6/`:

| Sourcebook | Content |
|---|---|
| *Galaxy Guide 1–12* | Expanded species, factions, planets, adversaries |
| *Heroes and Rogues* | 60+ character templates |
| *The Movie Trilogy Sourcebook* | Canon character stats, event timeline |
| *Dark Empire Sourcebook* | Post-RotJ era, Emperor's return, Holocrons |
| *Tales of the Jedi Sourcebook* | Complete Force power listing, Jedi history |
| *Planets of the Galaxy* | Detailed world descriptions and local rules |
| *Shadows of the Empire Sourcebook* | Criminal underworld, Black Sun faction |
| *Imperial Sourcebook / Rebel Alliance Sourcebook* | Faction stats, vehicles, operations |
| *Galaxy Guide 6: Tramp Freighters* | Ship economics, cargo hauling rules |

To add a sourcebook: append a `## Sourcebook: [Name]` section below with new species abilities, equipment stats, or rules expansions. The GM core will incorporate them at session load.

### SWAPI Integration

The [Star Wars API (SWAPI)](https://swapi.dev) provides open data for people, planets, species, vehicles, and starships from the canonical films. A lookup stub is provided at `systems/swwegd6/swapi_lookup.py`.

**Available endpoints:**
- `swapi_lookup.py people <name>` — canonical character data (height, mass, homeworld, films)
- `swapi_lookup.py planets <name>` — planet data (climate, terrain, population, orbital period)
- `swapi_lookup.py species <name>` — species data (classification, language, average height/lifespan)
- `swapi_lookup.py vehicles <name>` — vehicle specs (model, max speed, cargo capacity, cost)
- `swapi_lookup.py starships <name>` — starship specs (class, hyperdrive rating, crew, MGLT speed)
- `swapi_lookup.py films <title>` — film release data and episode metadata

**Usage in sessions:** When a player asks about a canonical vehicle, planet, or species, the GM may run `swapi_lookup.py` to surface real film-canon data, then apply WEG D6 game statistics from this module or the relevant sourcebook. SWAPI data supplements but does not replace the game stat blocks — use it for flavor, geography, and lore enrichment.

**Note:** SWAPI covers Episodes IV–VI and related canon. For Legends/EU content, rely on sourcebooks. The lookup script gracefully handles unknown entries with a "not found in SWAPI — use sourcebook data" message.
