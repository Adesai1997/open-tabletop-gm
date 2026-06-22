#!/usr/bin/env python3
"""
character.py — WEG Star Wars D6 character creation & sheet tool

Usage:
    python3 character.py new                         # interactive guided creation
    python3 character.py sheet <name>                # display character sheet
    python3 character.py list                        # list all characters
    python3 character.py update <name> cp <amount>   # add/subtract Character Points
    python3 character.py update <name> fp <amount>   # add/subtract Force Points
    python3 character.py update <name> dsp <amount>  # add/subtract Dark Side Points
    python3 character.py update <name> wound <level> # set wound level
    python3 character.py improve <name> <skill> <pips># spend CPs to improve a skill

Character data is stored as JSON in:
    ~/.local/share/open-tabletop-gm/characters/<name>.json
"""

import json
import os
import sys
import argparse
import pathlib

CHARS_DIR = pathlib.Path.home() / ".local" / "share" / "open-tabletop-gm" / "characters"
CHARS_DIR.mkdir(parents=True, exist_ok=True)

ATTRIBUTES = ["dexterity", "knowledge", "mechanical", "perception", "strength", "technical"]

SKILLS_BY_ATTR = {
    "dexterity": ["blaster", "blaster_artillery", "brawling_parry", "dodge", "grenade",
                  "lightsaber", "melee_combat", "melee_parry", "missile_weapons",
                  "running", "thrown_weapons", "vehicle_blasters"],
    "knowledge": ["alien_species", "bureaucracy", "cultures", "intimidation", "languages",
                  "law_enforcement", "planetary_systems", "scholar", "streetwise",
                  "survival", "willpower"],
    "mechanical": ["astrogation", "beast_riding", "capital_ship_gunnery", "capital_ship_piloting",
                   "capital_ship_shields", "communications", "ground_vehicle_op",
                   "hover_vehicle_op", "repulsorlift_op", "sensors", "space_transports",
                   "starfighter_piloting", "starship_gunnery", "starship_shields", "swoop_op"],
    "perception": ["bargain", "command", "con", "forgery", "gambling", "hide",
                   "investigation", "persuasion", "search", "sneak"],
    "strength":   ["brawling", "climbing_jumping", "lifting", "stamina", "swimming"],
    "technical":  ["armor_repair", "blaster_repair", "capital_ship_repair",
                   "computer_programming", "demolitions", "droid_programming",
                   "droid_repair", "first_aid", "ground_vehicle_repair",
                   "hover_vehicle_repair", "repulsorlift_repair", "security",
                   "space_transports_repair", "starfighter_repair", "starship_weapons_repair"],
}

FORCE_SKILLS = ["control", "sense", "alter"]

WOUND_LEVELS = ["healthy", "stunned", "wounded", "wounded_twice", "incapacitated",
                "mortally_wounded", "killed"]

WOUND_PENALTIES = {
    "healthy": "+0D", "stunned": "-1D this + next round", "wounded": "-1D all",
    "wounded_twice": "-2D all", "incapacitated": "unconscious",
    "mortally_wounded": "unconscious; roll 2D/round or die", "killed": "dead",
}

# Die code helpers

def _parse_dc(dc_str: str) -> tuple[int, int]:
    """Parse a die code like '3D+2' into (dice, pips). Returns (0,0) on failure."""
    s = dc_str.strip().upper().replace("+", "")
    if "D" not in s:
        return (0, 0)
    parts = s.split("D")
    try:
        dice = int(parts[0]) if parts[0] else 0
        pips = int(parts[1]) if len(parts) > 1 and parts[1] else 0
        pips = min(pips, 2)  # WEG only uses +1 or +2
        return (dice, pips)
    except ValueError:
        return (0, 0)


def _fmt_dc(dice: int, pips: int) -> str:
    if pips:
        return f"{dice}D+{pips}"
    return f"{dice}D"


def _dc_to_total_pips(dice: int, pips: int) -> int:
    return dice * 3 + pips


def _pips_to_dc(total_pips: int) -> tuple[int, int]:
    return (total_pips // 3, total_pips % 3)


# Storage

def _char_path(name: str) -> pathlib.Path:
    return CHARS_DIR / f"{name.lower().replace(' ', '_')}.json"


def _load_char(name: str) -> dict:
    p = _char_path(name)
    if not p.exists():
        print(f"  Error: character '{name}' not found.")
        sys.exit(1)
    with open(p) as f:
        return json.load(f)


def _save_char(char: dict) -> None:
    p = _char_path(char["name"])
    with open(p, "w") as f:
        json.dump(char, f, indent=2)


def _prompt(label: str, default: str = "") -> str:
    suffix = f" [{default}]" if default else ""
    val = input(f"  {label}{suffix}: ").strip()
    return val if val else default


def _prompt_dc(label: str, default: str = "2D") -> tuple[int, int]:
    while True:
        raw = _prompt(label, default)
        dc = _parse_dc(raw)
        if dc[0] > 0:
            return dc
        print("    Invalid die code. Use format like 3D or 3D+2")


# Commands

def cmd_new():
    print("\n=== WEG Star Wars D6 — New Character ===")
    name = _prompt("Character name")
    species = _prompt("Species", "Human")
    char_type = _prompt("Template type", "Smuggler")
    gender = _prompt("Gender", "")
    age = _prompt("Age", "")
    force_sensitive = _prompt("Force-sensitive? (yes/no)", "no").lower().startswith("y")

    print("\n  -- Attributes (human default range 2D–4D; 18D total) --")
    attrs = {}
    for attr in ATTRIBUTES:
        dc = _prompt_dc(f"  {attr.capitalize()}", "2D")
        attrs[attr] = {"dice": dc[0], "pips": dc[1]}

    total_attr_pips = sum(_dc_to_total_pips(v["dice"], v["pips"]) for v in attrs.values())
    print(f"  Total attribute dice: {total_attr_pips // 3}D+{total_attr_pips % 3} (18D expected for humans)")

    print("\n  -- Skills (7D to distribute; enter only skills you are improving) --")
    skills = {}
    skill_dice_remaining = 21  # 7D in pips
    for attr_name, skill_list in SKILLS_BY_ATTR.items():
        attr_dc = attrs[attr_name]
        for skill in skill_list:
            val = _prompt(f"  {skill} improvement dice (e.g. 1D, 2D, or blank to skip)", "")
            if val:
                dc = _parse_dc(val)
                if dc[0] > 0:
                    add_pips = _dc_to_total_pips(dc[0], dc[1])
                    skill_dice_remaining -= add_pips
                    base = _dc_to_total_pips(attr_dc["dice"], attr_dc["pips"])
                    final = _pips_to_dc(base + add_pips)
                    skills[skill] = {"dice": final[0], "pips": final[1]}

    if force_sensitive:
        print("\n  -- Force Skills (start at 1D if you have a teacher) --")
        for fs in FORCE_SKILLS:
            val = _prompt(f"  {fs} (1D if known, blank if not yet trained)", "")
            if val:
                dc = _parse_dc(val)
                if dc[0] > 0:
                    skills[fs] = {"dice": dc[0], "pips": dc[1]}

    print("\n  -- Starting Resources --")
    credits = int(_prompt("  Starting credits", "1000"))
    equipment_raw = _prompt("  Equipment (comma-separated)", "Blaster pistol, Utility belt, 100 credits")
    equipment = [e.strip() for e in equipment_raw.split(",") if e.strip()]

    char = {
        "name": name,
        "species": species,
        "type": char_type,
        "gender": gender,
        "age": age,
        "force_sensitive": force_sensitive,
        "attributes": attrs,
        "skills": skills,
        "force_points": 2 if force_sensitive else 1,
        "character_points": 5,
        "dark_side_points": 0,
        "wound_level": "healthy",
        "move": 10,
        "credits": credits,
        "equipment": equipment,
        "background": "",
        "personality": "",
        "objectives": "",
        "quote": "",
    }

    _save_char(char)
    print(f"\n  Character '{name}' saved. Run: python3 character.py sheet {name}")
    return char


def cmd_sheet(name: str):
    c = _load_char(name)
    print(f"\n{'='*56}")
    print(f"  {c['name']}   [{c['type']}]")
    print(f"  Species: {c['species']}  |  Gender: {c.get('gender','')}  |  Age: {c.get('age','')}")
    print(f"  Force-Sensitive: {'Yes' if c['force_sensitive'] else 'No'}")
    print(f"{'='*56}")
    print(f"  {'ATTRIBUTE':<20} {'DIE CODE':<10}")
    for attr in ATTRIBUTES:
        v = c["attributes"][attr]
        print(f"  {attr.capitalize():<20} {_fmt_dc(v['dice'], v['pips']):<10}")
    print(f"{'='*56}")
    print("  IMPROVED SKILLS:")
    for skill, v in c.get("skills", {}).items():
        print(f"    {skill:<32} {_fmt_dc(v['dice'], v['pips'])}")
    print(f"{'='*56}")
    print(f"  Force Points:     {c['force_points']}")
    print(f"  Character Points: {c['character_points']}")
    print(f"  Dark Side Points: {c['dark_side_points']}")
    print(f"  Move:             {c['move']} m/round")
    print(f"  Credits:          {c['credits']}")
    wound = c.get('wound_level', 'healthy')
    print(f"  Wound Status:     {wound.replace('_',' ').title()}  ({WOUND_PENALTIES.get(wound,'')})")
    print(f"{'='*56}")
    print("  EQUIPMENT:")
    for item in c.get("equipment", []):
        print(f"    - {item}")
    if c.get('background'):
        print(f"  Background: {c['background']}")
    if c.get('quote'):
        print(f"  Quote: {c['quote']}")
    print(f"{'='*56}\n")


def cmd_list():
    chars = sorted(CHARS_DIR.glob("*.json"))
    if not chars:
        print("  No characters found.")
        return
    print("\n  Characters:")
    for p in chars:
        with open(p) as f:
            c = json.load(f)
        print(f"    {c['name']:<20} [{c['type']}]  {c['species']}")


def cmd_update(name: str, field: str, amount: str):
    c = _load_char(name)
    amt = int(amount)
    if field == "cp":
        c["character_points"] = max(0, c["character_points"] + amt)
        print(f"  {name}: Character Points → {c['character_points']}")
    elif field == "fp":
        c["force_points"] = max(0, c["force_points"] + amt)
        print(f"  {name}: Force Points → {c['force_points']}")
    elif field == "dsp":
        c["dark_side_points"] = max(0, c["dark_side_points"] + amt)
        print(f"  {name}: Dark Side Points → {c['dark_side_points']}")
    elif field == "wound":
        level = amount.lower().replace(" ", "_")
        if level not in WOUND_LEVELS:
            print(f"  Valid wound levels: {', '.join(WOUND_LEVELS)}")
            return
        c["wound_level"] = level
        print(f"  {name}: Wound → {level.replace('_',' ').title()}  ({WOUND_PENALTIES[level]})")
    else:
        print(f"  Unknown field '{field}'. Use cp, fp, dsp, or wound.")
        return
    _save_char(c)


def cmd_improve(name: str, skill: str, pips_str: str):
    """
    Spend Character Points to improve a skill.
    Cost = current number of dice before the D.
    Example: 3D costs 3 CP for +1 pip (3 pips = +1D).
    """
    c = _load_char(name)
    skill = skill.lower().replace("-", "_").replace(" ", "_")
    pips = int(pips_str)

    # Find current skill level
    if skill in c.get("skills", {}):
        v = c["skills"][skill]
    else:
        # defaults to attribute level
        parent_attr = next((a for a, sl in SKILLS_BY_ATTR.items() if skill in sl), None)
        if parent_attr is None and skill not in FORCE_SKILLS:
            print(f"  Unknown skill '{skill}'.")
            return
        if parent_attr:
            v = c["attributes"][parent_attr]
        else:
            v = {"dice": 1, "pips": 0}  # Force skill starts at 1D

    current_dice = v["dice"]
    cost_per_pip = current_dice  # WEG: cost = current D before decimal
    total_cost = cost_per_pip * pips

    if c["character_points"] < total_cost:
        print(f"  Not enough CPs. Need {total_cost}, have {c['character_points']}.")
        return

    current_total = _dc_to_total_pips(v["dice"], v["pips"])
    new_total = current_total + pips
    new_dc = _pips_to_dc(new_total)
    c["skills"][skill] = {"dice": new_dc[0], "pips": new_dc[1]}
    c["character_points"] -= total_cost
    print(f"  {name}: {skill} {_fmt_dc(v['dice'], v['pips'])} → {_fmt_dc(*new_dc)}  (spent {total_cost} CP; {c['character_points']} remaining)")
    _save_char(c)


# Main

def main():
    p = argparse.ArgumentParser(description="WEG Star Wars D6 character tool")
    sub = p.add_subparsers(dest="cmd")
    sub.add_parser("new", help="Create a new character interactively")
    sh = sub.add_parser("sheet", help="Display character sheet")
    sh.add_argument("name")
    sub.add_parser("list", help="List all characters")
    up = sub.add_parser("update", help="Update CP/FP/DSP/wound")
    up.add_argument("name")
    up.add_argument("field", choices=["cp", "fp", "dsp", "wound"])
    up.add_argument("amount")
    imp = sub.add_parser("improve", help="Spend CPs to improve a skill")
    imp.add_argument("name")
    imp.add_argument("skill")
    imp.add_argument("pips", help="Number of pips to add (3 pips = +1D)")
    args = p.parse_args()
    if args.cmd == "new":
        cmd_new()
    elif args.cmd == "sheet":
        cmd_sheet(args.name)
    elif args.cmd == "list":
        cmd_list()
    elif args.cmd == "update":
        cmd_update(args.name, args.field, args.amount)
    elif args.cmd == "improve":
        cmd_improve(args.name, args.skill, args.pips)
    else:
        p.print_help()

if __name__ == "__main__":
    main()
