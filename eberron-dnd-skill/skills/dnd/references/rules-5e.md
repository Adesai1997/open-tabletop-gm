# D&D 5e — Mechanical Authority

The complete rules the DM must apply. Merges the canonical DM prompt's mechanics with a
5e system module. **Never fabricate or bend a rule.** Where this file and
`canonical-dm-rules.md` overlap, the **canonical file is authoritative** (this file is the
working expansion with script commands).

**Script-first lookup order** for any monster, spell, item, magic item, condition,
class/subclass feature, class, or race:

1. **Run `scripts/lookup.py` FIRST** — it reads the bundled open-licensed 5e SRD dataset
   in `data/srd-2014/` (and `data/dnd5e_srd.json`) offline and prints a compact,
   authoritative stat block or rules entry. Never recite an SRD stat block, spell, or
   condition from memory when `lookup.py` can produce it. Examples:
   `python3 scripts/lookup.py monster "goblin"`, `... spell "fireball"`,
   `... condition "prone"`, `... magic-item "bag of holding"`, `... feature "rage"`,
   `... class "barbarian"`, `... race "elf"`.
2. **Then search the bundled `lore/` corpus** (`scripts/lore_search.py "<term>"`) for
   **Eberron-specific or non-SRD content** (setting monsters, dragonmarks, prestige
   classes, House rules) and for the full rulebook texts under `lore/fulltext/rulebooks/`
   (Player's Handbook, DMG, Monster Manual, etc.). `lore/` is **authoritative** for
   anything the SRD does not cover, and for setting flavor / house rules it overrides the
   generic SRD entry. **`lore/` also beats the model's training knowledge** (canon
   precedence — see `lore/INDEX.md`).
3. If neither the SRD nor `lore/` has it, **say so before inventing**, then record the
   invention into the campaign's `world.md` as new canon.

**Read this file at every `/dm load` and whenever a mechanical question arises.**

**Ruleset:** default `2014` (classic 5e / original SRD). A campaign may set `2024` on its
state.md header line (`**Ruleset:** 2024`) for the 2024 revision. Honor whichever the
campaign declares.

---

## 1. When to Roll & the DC Scale

Roll **before** narrating an outcome. State what to roll and the target number, then
**stop and wait** for the result (see Dice Convention below). Call for a roll only when
success is uncertain **and** failure matters — routine tasks by a competent character just
succeed.

| DC | Difficulty |
|----|-----------|
| 5  | Very Easy |
| 10 | Easy |
| 15 | Medium |
| 20 | Hard |
| 25 | Very Hard |
| 30 | Nearly Impossible |

Reward a clever or bold player-proposed action with a **fair DC** rather than blocking it.

---

## 2. Dice Convention — players roll their own dice (default `roll_mode: players`)

**The DM does not roll dice for player characters.** By default the player rolls their own
PC dice — physical dice or an online roller such as **rolladie.net**. This convention is
governed by `canonical-dm-rules.md` and refined here for the scripts:

- For **every player-facing roll**, issue a `ROLL_REQUEST` naming **die type, number of
  dice, modifier, and the DC/AC when visible**:
  - `ROLL_REQUEST: roll 1d20, add +5 (Athletics), vs DC 15`
  - `ROLL_REQUEST: attack — roll 1d20, add +7, vs AC 14`
  - `Damage: roll 2d6, add +3`
- **Advantage/disadvantage:** *"roll 1d20 twice, tell me both numbers"* — take higher
  (adv) or lower (dis).
- After the callout, **STOP and WAIT** for the reported number. **Never roll for a PC,
  never assume, never auto-resolve.** If no number comes back, **re-ask.**
- **DM rolls only NPC / monster / secret dice** via `scripts/dice.py` (use `--silent` for
  hidden rolls), showing math inline.
- **Player-rolled:** ability checks, attacks, damage, saving throws, **death saves**,
  **concentration saves**, and **the PC's initiative**. **DM-rolled:** NPC/monster
  initiative and attacks.
- *(Optional `roll_mode: auto`: DM openly rolls everything with `dice.py`. `players` is
  the default.)*

---

## 3. Core Mechanics

- **Ability check:** `d20 + ability modifier + proficiency bonus (if proficient)` vs DC.
- **Attack roll:** `d20 + ability modifier + proficiency bonus` vs target AC. Ability =
  STR (melee), DEX (ranged or finesse), or the spellcasting ability for spells.
- **Saving throw:** `d20 + ability modifier + proficiency bonus (if proficient)` vs DC.
- **Advantage / Disadvantage:** roll two d20, take higher (adv) or lower (dis). Multiple
  sources do **not** stack; a single source of each cancels out entirely regardless of
  count. Use `dice.py d20 adv` / `dice.py d20 dis` (NPC/secret rolls only; players roll
  twice themselves).
- **Natural 20 on an attack:** automatic hit and a critical — **double the damage dice
  only** (not modifiers). **Natural 1 on an attack:** automatic miss.
- **Passive check:** `10 + all applicable modifiers` (no roll).

**Ability modifier** = `floor((score − 10) / 2)`. Score 1 = −5, 10/11 = +0, 20 = +5.
**Proficiency bonus by level:** +2 (1–4), +3 (5–8), +4 (9–12), +5 (13–16), +6 (17–20).
Verify character math with `character.py calc` — never hand-calculate secondary stats.

---

## 4. Combat Procedure

1. **Surprise:** compare attackers' Stealth vs defenders' passive Perception. The
   surprised side takes no turn in round 1 and can't react until its first turn ends.
2. **Initiative:** `d20 + DEX modifier` for every combatant. Order holds the whole combat.
   **NPCs/monsters are always DM-rolled** via `combat.py init '[{...}]'`; **the PC rolls
   their own d20** under `roll_mode: players` (add the PC into the tracker with their
   reported total).
3. **A turn:** move up to speed + **one action** + **one bonus action** (only if a feature
   grants it) + **one free object interaction** + **one reaction per round**.
4. **Concentration:** on taking damage while concentrating, make a **CON save, DC 10 or
   half the damage taken, whichever is higher.** Only **one** concentration spell at a
   time. *(Player-rolled for a PC; DM-rolled for an NPC.)*
5. **Death saves** (at 0 HP, start of turn, `d20`, no modifiers): **10+ = success**, **9
   or lower = failure.** Three successes = stable; three failures = dead. **Natural 20 =
   regain 1 HP.** **Natural 1 = two failures.** Damage at 0 HP = one failure (**two on a
   crit** or if it kills). **Player-rolled**; track via
   `tracker.py saves <name> success|failure|stable|reset`.

Resolve NPC attacks with `combat.py attack --atk <bonus> --ac <target_ac> --dmg <notation>
[--crit]`. For **PC attacks under `roll_mode: players`, call for the roll and wait.** Track
conditions/concentration/effects with `tracker.py`.

---

## 5. Spellcasting by Caster Type

- **Prepared casters — Cleric, Druid, Paladin:** know the full class list; prepare
  **(spellcasting ability modifier + class level)** spells after a long rest.
- **Known casters — Bard, Sorcerer, Ranger:** fixed set of known spells; may swap **one**
  on level-up.
- **Spellbook caster — Wizard:** prepares **(INT modifier + wizard level)** from the
  spellbook.
- **Warlock — Pact Magic:** few slots, **always cast at the highest available slot
  level**, and they **recharge on a SHORT rest**, not a long rest. ⚠ **This is the most
  commonly broken rule in 5e and must NEVER be violated.** Track warlock slots separately.
- **Cantrips** are unlimited. **Ritual casting** takes 10 extra minutes and consumes no
  slot (if the spell has the ritual tag and the class allows it).
- **Track every slot spent.** Emit `SPELL_SLOT_USED` in MECHANICS and update the character
  file / STATE. Never skip slot tracking.

---

## 6. Conditions

Track all standard conditions **exactly as written**: **blinded, charmed, deafened,
frightened, grappled, incapacitated, invisible, paralyzed, petrified, poisoned, prone,
restrained, stunned, unconscious**, and **exhaustion levels 1–6**. Apply/remove via
`tracker.py condition add|remove|clear <entity> <condition>` and report
`CONDITION_APPLIED` / `CONDITION_REMOVED`.

---

## 7. Rests

- **Short rest (1 hour):** spend any number of Hit Dice; roll each + CON mod to recover HP
  *(player-rolled)*. Some features (and **Warlock Pact Magic slots**) recharge. Advance
  time: `calendar.py -c <name> rest short`.
- **Long rest (8 hours):** restore all HP; regain half of maximum Hit Dice (round up);
  restore all spell slots; restore most features. Advance time:
  `calendar.py -c <name> rest long`. Clear round-based tracker state:
  `tracker.py -c <name> clear --all`.

---

## 8. XP Thresholds (total XP to reach each level)

| Lvl | XP | Lvl | XP | Lvl | XP | Lvl | XP |
|----|----|----|----|----|----|----|----|
| 2 | 300 | 7 | 23,000 | 12 | 100,000 | 17 | 225,000 |
| 3 | 900 | 8 | 34,000 | 13 | 120,000 | 18 | 265,000 |
| 4 | 2,700 | 9 | 48,000 | 14 | 140,000 | 19 | 305,000 |
| 5 | 6,500 | 10 | 64,000 | 15 | 165,000 | 20 | 355,000 |
| 6 | 14,000 | 11 | 85,000 | 16 | 195,000 | | |

Award XP after any resolved encounter that presented genuine challenge. Do **not** award
for routine travel, trivial talk, rest, or automatic successes. Rate difficulty **as it
was experienced**. Use `xp.py award --campaign <name> --characters "<names>"
[--monsters "name:cr:count,..." | --difficulty easy|medium|hard|deadly
--type combat|noncombat]`. Report `XP_GAINED`.

---

## 9. Encounter Balance (XP Budget)

Multiply total monster XP by the group multiplier before comparing to the party threshold:

| Number of monsters | Multiplier |
|--------------------|-----------|
| 1 | ×1 |
| 2 | ×1.5 |
| 3–6 | ×2 |
| 7–10 | ×2.5 |
| 11–14 | ×3 |
| 15+ | ×4 |

Preview with `xp.py calc --level <L> --players <N> --monsters "goblin:1/4:3,orc:1/2:2"`.

**Low level / solo play:** cap enemy HP, avoid multiattack for level-1 foes, limit to 1–2
enemies, leave an escape route. **Check `lore/`** for setting-appropriate monsters,
prestige classes, or factions before building an encounter (e.g. the Fight Club
statblocks, the prestige-class briefs, "Ravaging Monsters").

---

## 10. Monster Tactics by Intelligence

- **Low INT (animal/mindless):** no plan — attack the nearest, fight to the death.
- **Moderate INT:** basic tactics — gang up, use simple cover, flee when clearly losing.
- **High INT:** use terrain, focus-fire the biggest threat or the healer, set ambushes,
  retreat to regroup, take hostages, and **negotiate** when it serves them.

---

## 11. Attunement & Economy

- **Attunement cap: 3 magic items per character.** Never allow a fourth.
- Use standard equipment pricing as the baseline economy, scaled by settlement size. Check
  `lore/` for setting-specific goods or House services (e.g. Jorasco healing, Orien
  lightning-rail fares, Sivis message stations) before pricing.
- Track inventory, consumables, currency, and carrying capacity. **Deny actions when a
  required item is missing.**

---

## 12. Inspiration & Bold Play

Award **Inspiration** immediately when a player makes a bold roleplay choice, acts on a
flaw/bond/ideal, or elevates the scene. Say why, then move on. A character holds only
**one** Inspiration at a time. Spending Inspiration grants advantage on one roll.

---

## Script Quick Reference

| Need | Command |
|------|---------|
| NPC / secret dice | `dice.py <notation> [--silent]` (e.g. `d20+5`, `2d6+3`, `4d6kh3`, `d20 adv`) |
| Initiative (NPCs) | `combat.py init '[{"name","dex_mod","hp","ac","type"}]'` |
| NPC attack | `combat.py attack --atk N --ac N --dmg 1d8+3 [--crit]` |
| Conditions / concentration / death saves / effects | `tracker.py -c <name> ...` |
| In-world time | `calendar.py -c <name> advance N days` · `rest short|long` · `now` |
| Ability scores | `ability-scores.py roll` · `pointbuy --check STR=15 ...` |
| Character math | `character.py calc --class ... --level ... STR=15 ... --proficient ...` |
| XP award | `xp.py award --campaign <name> --characters "..." --monsters "..."` |
| **SRD lookup (use first)** | `lookup.py monster\|spell\|item\|equipment\|magic-item\|condition\|feature\|class\|race "<name>"` (fuzzy; `--all` lists matches, `--json` raw) |
| **Lore search (Eberron / non-SRD)** | `lore_search.py "<term>"` (`--list`, `--files <sub>`, `--any`) |

All scripts require `python3` and run from the `scripts/` directory (they import the local
`paths.py`). Set **`GM_CAMPAIGN_ROOT`** to move the working tree; default is
`~/eberron-dnd`.
