# D&D 5e — Mechanical Authority

The complete rules the DM must apply. This merges the DND Bot space prompt's mechanical rules with the D&D 5e system module from Bobby-Gray/open-tabletop-gm. **Never fabricate or bend a rule.** If unsure, `search_files` the space's core rulebooks (Player's Handbook, DMG, Monster Manual, Basic Rules) first; if still unsure, say so. When the space contains a house rule or setting mechanic, it overrides the generic ruling here — check for one before defaulting.

**Read this file at every `/dm load` and whenever a mechanical question arises.**

**System version:** default `2014` (classic 5e / original SRD). A campaign may set `2024` on its state.md header line (`**System Version:** 2024`) for the 2024 revision. Honor whichever the campaign declares.

---

## 1. When to Roll & the DC Scale

Roll **before** narrating an outcome. State what to roll and the target number, then **stop and wait** for the result (see Dice Convention). Call for a roll only when success is uncertain **and** failure matters — routine tasks by a competent character just succeed.

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

## 2. Core Mechanics

- **Ability check:** `d20 + ability modifier + proficiency bonus (if proficient)` vs DC.
- **Attack roll:** `d20 + ability modifier + proficiency bonus` vs target AC. Ability = STR (melee), DEX (ranged or finesse), or the spellcasting ability for spells.
- **Saving throw:** `d20 + ability modifier + proficiency bonus (if proficient)` vs DC.
- **Advantage / Disadvantage:** roll two d20, take higher (adv) or lower (dis). Multiple sources do **not** stack; a single source of each cancels out entirely regardless of count. Use `dice.py d20 adv` / `dice.py d20 dis` (NPC/secret rolls only).
- **Natural 20 on an attack:** automatic hit and a critical — **double the damage dice only** (not modifiers). **Natural 1 on an attack:** automatic miss.
- **Passive check:** `10 + all applicable modifiers` (no roll).

**Ability modifier** = `floor((score − 10) / 2)`. Score 1 = −5, 10/11 = +0, 20 = +5.

**Proficiency bonus by level:** +2 (1–4), +3 (5–8), +4 (9–12), +5 (13–16), +6 (17–20).

Verify character math with `character.py calc` — never hand-calculate secondary stats.

---

## 3. Combat Procedure

1. **Surprise:** compare attackers' Stealth vs defenders' passive Perception. The surprised side takes no turn in round 1 and can't react until its first turn ends.
2. **Initiative:** `d20 + DEX modifier` for every combatant. Order holds the whole combat. **Always GM-rolled** via `combat.py init '[{...}]'` regardless of `roll_mode`.
3. **A turn:** move up to speed + **one action** + **one bonus action** (only if a feature grants it) + **one free object interaction** + **one reaction per round** (usable on others' turns).
4. **Concentration:** on taking damage while concentrating, make a **CON save, DC 10 or half the damage taken, whichever is higher**. Only **one** concentration spell at a time — starting a new one drops the old.
5. **Death saves** (at 0 HP, start of turn, `d20`, no modifiers): **10+ = success**, **9 or lower = failure**. Three successes = stable; three failures = dead. **Natural 20 = regain 1 HP** (conscious). **Natural 1 = two failures.** Taking any damage at 0 HP = one failure (**two on a crit** or if the damage kills). Track via `tracker.py saves <name> success|failure|stable|reset`.

Resolve NPC attacks with `combat.py attack --atk <bonus> --ac <target_ac> --dmg <notation> [--crit]`. Track conditions/concentration/effects with `tracker.py`.

---

## 4. Spellcasting by Caster Type

- **Prepared casters — Cleric, Druid, Paladin:** know the full class list; prepare **(spellcasting ability modifier + class level)** spells after a long rest.
- **Known casters — Bard, Sorcerer, Ranger:** fixed set of known spells; may swap **one** on level-up.
- **Spellbook caster — Wizard:** prepares **(INT modifier + wizard level)** spells from the spellbook.
- **Warlock — Pact Magic:** few slots, **always cast at the highest available slot level**, and they **recharge on a SHORT rest**, not a long rest. ⚠ **This is the most commonly broken rule in 5e and must NEVER be violated.** Track warlock slots separately from other casters'.
- **Cantrips** are unlimited. **Ritual casting** takes 10 extra minutes and consumes no slot (if the spell has the ritual tag and the class allows it).
- **Track every slot spent.** Emit `SPELL_SLOT_USED` in MECHANICS and update the character file / STATE. Never skip slot tracking.

---

## 5. Conditions

Track all standard conditions **exactly as written**: **blinded, charmed, deafened, frightened, grappled, incapacitated, invisible, paralyzed, petrified, poisoned, prone, restrained, stunned, unconscious**, and **exhaustion levels 1–6**. Apply/remove via `tracker.py condition add|remove|clear <entity> <condition>` and report `CONDITION_APPLIED` / `CONDITION_REMOVED`.

Severity cue (for emphasis, not a rule): red = Unconscious/Paralyzed/Petrified/Stunned; amber = Incapacitated/Frightened/Poisoned/Charmed/Exhausted; blue = Grappled/Restrained/Prone/Blinded/Deafened; green = Invisible.

---

## 6. Rests

- **Short rest (1 hour):** spend any number of Hit Dice; roll each + CON mod to recover HP. Some features (and **Warlock Pact Magic slots**) recharge. Advance time: `calendar.py -c <name> rest short`.
- **Long rest (8 hours):** restore all HP; regain half of maximum Hit Dice (round up); restore all spell slots; restore most features. Advance time: `calendar.py -c <name> rest long`. Clear round-based tracker state: `tracker.py -c <name> clear --all`.

---

## 7. XP Thresholds (total XP to reach each level)

| Lvl | XP | Lvl | XP | Lvl | XP | Lvl | XP |
|----|----|----|----|----|----|----|----|
| 2 | 300 | 7 | 23,000 | 12 | 100,000 | 17 | 225,000 |
| 3 | 900 | 8 | 34,000 | 13 | 120,000 | 18 | 265,000 |
| 4 | 2,700 | 9 | 48,000 | 14 | 140,000 | 19 | 305,000 |
| 5 | 6,500 | 10 | 64,000 | 15 | 165,000 | 20 | 355,000 |
| 6 | 14,000 | 11 | 85,000 | 16 | 195,000 | | |

Award XP after any resolved encounter that presented genuine challenge (combat, consequential social challenge, investigation milestone, dangerous non-combat task). Do **not** award for routine travel, trivial talk, rest, or automatic successes. Rate difficulty **as it was experienced**, not as designed. Use `xp.py award --campaign <name> --characters "<names>" [--monsters "name:cr:count,..." | --difficulty easy|medium|hard|deadly --type combat|noncombat]`. Report `XP_GAINED`.

---

## 8. Encounter Balance (XP Budget)

Use Challenge Rating and an XP budget. **Multiply total monster XP** by the group multiplier before comparing to the party's threshold:

| Number of monsters | Multiplier |
|--------------------|-----------|
| 1 | ×1 |
| 2 | ×1.5 |
| 3–6 | ×2 |
| 7–10 | ×2.5 |
| 11–14 | ×3 |
| 15+ | ×4 |

Preview with `xp.py calc --level <L> --players <N> --monsters "goblin:1/4:3,orc:1/2:2"` (or `--difficulty`).

**Low level / solo play:** cap enemy HP, avoid multiattack for level-1 foes, limit to 1–2 enemies, and leave an escape route.

**Check the space files** for setting-appropriate monsters, prestige classes, or factions before building an encounter (e.g. "Ravaging Monsters", "Reptilian Tool of Tiamat", prestige-class PDFs).

---

## 9. Monster Tactics by Intelligence

Scale enemy tactics to their INT:

- **Low INT (animal/mindless):** no plan — attack the nearest, fight to the death.
- **Moderate INT:** basic tactics — gang up, use simple cover, flee when clearly losing.
- **High INT:** use terrain, focus-fire the biggest threat or the healer, set ambushes, retreat to regroup, take hostages, and **negotiate** when it serves them.

---

## 10. Attunement & Economy

- **Attunement cap: 3 magic items per character.** Never allow a fourth. Track in the character sheet.
- Use standard equipment pricing as the baseline economy, scaled by settlement size. Check the space files for setting-specific goods or House services (e.g. Jorasco healing, Orien lightning-rail fares, Sivis message stations) before pricing.
- Track inventory, consumables, currency, and carrying capacity. **Deny actions when a required item is missing.**

---

## 11. Inspiration & Bold Play

Award **Inspiration** immediately when a player makes a bold roleplay choice, acts on a flaw/bond/ideal, or elevates the scene. Say why, then move on. A character holds only **one** Inspiration at a time. Spending Inspiration grants advantage on one roll.

---

## Script Quick Reference

| Need | Command |
|------|---------|
| NPC / secret dice | `dice.py <notation> [--silent]` (e.g. `d20+5`, `2d6+3`, `4d6kh3`, `d20 adv`) |
| Initiative (all combatants) | `combat.py init '[{"name","dex_mod","hp","ac","type"}]'` |
| NPC attack | `combat.py attack --atk N --ac N --dmg 1d8+3 [--crit]` |
| Conditions / concentration / death saves / effects | `tracker.py -c <name> ...` |
| In-world time | `calendar.py -c <name> advance N days` · `rest short|long` · `now` |
| Ability scores | `ability_scores.py roll` · `pointbuy --check STR=15 ...` |
| Character math | `character.py calc --class ... --level ... STR=15 ... --proficient ...` |
| XP award | `xp.py award --campaign <name> --characters "..." --monsters "..."` |

All scripts require `python3` and are run from the `scripts/` directory (they import the local `_paths.py`). Set `GM_CAMPAIGN_ROOT` if you move the working tree; default is `/home/user/workspace/campaigns`.
