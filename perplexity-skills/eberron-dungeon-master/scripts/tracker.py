#!/usr/bin/env python3
"""
tracker.py — session-state tracker for conditions, concentration, effects, and death saves

Stores state per-campaign under GM_CAMPAIGN_ROOT (default
/home/user/workspace/campaigns/<campaign>/tracker.json). Outputs formatted
status to the terminal. Adapted from Bobby-Gray/open-tabletop-gm
(AGPL-3.0-or-later) to run standalone: the display-companion push_stats.py /
send.py hooks have been removed so the script needs no external services.

Usage:
    CAMPAIGN=my-campaign
    python3 tracker.py -c $CAMPAIGN condition add <entity> <condition>
    python3 tracker.py -c $CAMPAIGN condition remove <entity> <condition>
    python3 tracker.py -c $CAMPAIGN condition clear <entity>
    python3 tracker.py -c $CAMPAIGN concentrate <entity> "<spell name>"
    python3 tracker.py -c $CAMPAIGN concentrate <entity> break
    python3 tracker.py -c $CAMPAIGN effect start <entity> "<spell>" <duration> [conc]
    python3 tracker.py -c $CAMPAIGN effect end   <entity> "<spell>"
    python3 tracker.py -c $CAMPAIGN effect tick  <entity>
    python3 tracker.py -c $CAMPAIGN saves <entity> success
    python3 tracker.py -c $CAMPAIGN saves <entity> failure
    python3 tracker.py -c $CAMPAIGN saves <entity> stable
    python3 tracker.py -c $CAMPAIGN saves <entity> reset
    python3 tracker.py -c $CAMPAIGN status [entity]
    python3 tracker.py -c $CAMPAIGN clear [--all]
"""

import json
import os
import sys
import argparse
import time
import pathlib

from _paths import campaigns_dir as _campaigns_dir

_CAMPAIGNS_DIR = _campaigns_dir()

CONDITION_COLOURS = {
    # 5e defaults
    "unconscious":    "danger",
    "paralyzed":      "danger",
    "petrified":      "danger",
    "stunned":        "danger",
    "incapacitated":  "warn",
    "frightened":     "warn",
    "poisoned":       "warn",
    "charmed":        "warn",
    "exhausted":      "warn",
    "grappled":       "info",
    "restrained":     "info",
    "prone":          "info",
    "blinded":        "info",
    "deafened":       "info",
    "invisible":      "buff",

    # Star Wars D6 / generic system extensions
    "mortally-wounded":   "danger",
    "killed":             "danger",
    "wounded-twice":      "warn",
    "wounded":            "info",
    "stun-bolt":          "info",
    "immobilized":        "info",
    "force-point-active": "buff",
    "heroic-inspiration": "buff",
    "in-cover":           "buff",
    "dark-side-1":        "warn",
    "dark-side-2":        "warn",
    "dark-side-3":        "warn",
    "dark-side-4":        "warn",
    "dark-side-5":        "warn",
    "dark-side-6":        "warn",
}


def _state_path(campaign: str) -> str:
    d = str(_CAMPAIGNS_DIR / campaign)
    os.makedirs(d, exist_ok=True)
    return os.path.join(d, "tracker.json")


def _load(campaign: str) -> dict:
    path = _state_path(campaign)
    try:
        with open(path) as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}


def _save(campaign: str, state: dict) -> None:
    with open(_state_path(campaign), "w") as f:
        json.dump(state, f, indent=2)


def _entity(state: dict, name: str) -> dict:
    key = name.lower()
    if key not in state:
        state[key] = {
            "name": name,
            "conditions": [],
            "concentration": None,
            "effects": [],
            "death_saves": {"successes": 0, "failures": 0, "stable": False},
        }
    state[key].setdefault("effects", [])
    return state[key]


def _parse_duration(dur_str: str):
    d = dur_str.strip().lower()
    if d.endswith("r"):
        try:
            return {"duration_type": "rounds", "duration_remaining": int(d[:-1])}
        except ValueError:
            return None
    elif d.endswith("m"):
        try:
            return {"duration_type": "minutes", "duration_seconds": int(d[:-1]) * 60, "started_at": time.time()}
        except ValueError:
            return None
    elif d.endswith("h"):
        try:
            return {"duration_type": "hours", "duration_seconds": int(d[:-1]) * 3600, "started_at": time.time()}
        except ValueError:
            return None
    elif d == "indef":
        return {"duration_type": "indefinite"}
    return None


def _fmt_effect(eff: dict) -> str:
    dt = eff.get("duration_type", "indefinite")
    if dt == "rounds":
        return f"{eff.get('duration_remaining', 0)} rnd"
    elif dt in ("minutes", "hours"):
        elapsed = time.time() - eff.get("started_at", time.time())
        remaining = max(0, eff.get("duration_seconds", 0) - elapsed)
        if remaining <= 0:
            return "expired"
        m, s = divmod(int(remaining), 60)
        if m >= 60:
            h, m = divmod(m, 60)
            return f"{h}h {m}m"
        return f"{m}:{s:02d}"
    return "∞"


def _push_conditions(entity_name: str, conditions):
    # Display-companion hook removed for standalone operation. No-op.
    return


def _send_announce(msg: str):
    # Display-companion hook removed for standalone operation. No-op.
    return


def cmd_effect(campaign: str, action: str, entity_name: str, spell: str = "", duration: str = "", is_conc: bool = False):
    state = _load(campaign)
    ent = _entity(state, entity_name)
    if action == "start":
        dur = _parse_duration(duration)
        if not spell or not dur:
            print("  error: effect start requires <entity> <spell> <duration>")
            return
        effect = {"name": spell, "concentration": is_conc, **dur}
        ent["effects"] = [e for e in ent["effects"] if e["name"].lower() != spell.lower()]
        ent["effects"].append(effect)
        if is_conc:
            ent["concentration"] = spell
            _send_announce(f"{entity_name} — concentrating on {spell}")
        print(f"  + {entity_name}: {spell}{' [conc]' if is_conc else ''} · {_fmt_effect(effect)}")
    elif action == "end":
        removed = [e for e in ent["effects"] if e["name"].lower() == spell.lower()]
        ent["effects"] = [e for e in ent["effects"] if e["name"].lower() != spell.lower()]
        if removed and any(e.get("concentration") for e in removed) and (ent.get("concentration") or "").lower() == spell.lower():
            ent["concentration"] = None
        print(f"  - {entity_name}: {spell} ends")
    elif action == "tick":
        kept, expired = [], []
        for e in ent.get("effects", []):
            if e.get("duration_type") == "rounds":
                e = dict(e)
                e["duration_remaining"] = max(0, e.get("duration_remaining", 1) - 1)
                if e["duration_remaining"] <= 0:
                    expired.append(e)
                else:
                    kept.append(e)
            else:
                kept.append(e)
        ent["effects"] = kept
        for e in expired:
            print(f"  ! {entity_name}: {e['name']} EXPIRED")
    _save(campaign, state)


def cmd_condition(campaign: str, entity_name: str, action: str, condition: str = ""):
    state = _load(campaign)
    ent = _entity(state, entity_name)
    conds = ent["conditions"]
    cond = condition.lower() if condition else ""
    if action == "add":
        if cond and cond not in conds:
            conds.append(cond)
            _push_conditions(entity_name, conds)
            _send_announce(f"{entity_name} → {cond.capitalize()}")
            print(f"  + {entity_name}: {cond}")
    elif action == "remove":
        if cond in conds:
            conds.remove(cond)
            _push_conditions(entity_name, conds)
            _send_announce(f"{entity_name} — {cond.capitalize()} ends")
            print(f"  - {entity_name}: {cond} removed")
    elif action == "clear":
        conds.clear()
        _push_conditions(entity_name, [])
        print(f"  {entity_name}: conditions cleared")
    ent["conditions"] = conds
    _save(campaign, state)


def cmd_concentrate(campaign: str, entity_name: str, spell_or_break: str):
    state = _load(campaign)
    ent = _entity(state, entity_name)
    if spell_or_break.lower() == "break":
        old = ent.get("concentration")
        ent["concentration"] = None
        print(f"  {entity_name}: concentration on '{old}' broken" if old else f"  {entity_name}: was not concentrating")
    else:
        ent["concentration"] = spell_or_break
        print(f"  {entity_name}: concentrating on '{spell_or_break}'")
    _save(campaign, state)


def cmd_saves(campaign: str, entity_name: str, action: str):
    state = _load(campaign)
    ent = _entity(state, entity_name)
    saves = ent["death_saves"]
    if action == "success":
        saves["successes"] = min(3, saves["successes"] + 1)
    elif action == "failure":
        saves["failures"] = min(3, saves["failures"] + 1)
    elif action == "stable":
        saves["stable"] = True
    elif action == "reset":
        saves.update({"successes": 0, "failures": 0, "stable": False})
    ent["death_saves"] = saves
    _save(campaign, state)
    print(f"  {entity_name}: {saves['successes']} success(es), {saves['failures']} failure(s){' (stable)' if saves.get('stable') else ''}")


def cmd_status(campaign: str, filter_name: str = ""):
    state = _load(campaign)
    if not state:
        print("  (no tracked entities)")
        return
    entities = list(state.values())
    if filter_name:
        entities = [e for e in entities if filter_name.lower() in e["name"].lower()]
    for ent in entities:
        parts = []
        if ent.get("conditions"):
            parts.append("Conditions: " + ", ".join(c.capitalize() for c in ent["conditions"]))
        if ent.get("concentration"):
            parts.append(f"Concentrating: {ent['concentration']}")
        if ent.get("effects"):
            parts.append("Effects: " + ", ".join(f"{e['name']} · {_fmt_effect(e)}" for e in ent["effects"]))
        ds = ent.get("death_saves", {})
        if ds.get("successes") or ds.get("failures"):
            parts.append(f"Death saves: {ds.get('successes',0)}✓ {ds.get('failures',0)}✗{' (stable)' if ds.get('stable') else ''}")
        print(f"  {ent['name']}:")
        for p in parts or ["clean"]:
            print(f"    {p}")


def cmd_clear(campaign: str, clear_all: bool = False):
    state = _load(campaign)
    for ent in state.values():
        ent["conditions"] = []
        ent["concentration"] = None
        ent["effects"] = []
        _push_conditions(ent["name"], [])
        if clear_all:
            ent["death_saves"] = {"successes": 0, "failures": 0, "stable": False}
    _save(campaign, state)
    print(f"  Cleared {'all state' if clear_all else 'conditions and concentration'} for {len(state)} entities.")


def main():
    p = argparse.ArgumentParser(description="Session condition/death-save tracker.")
    p.add_argument("-c", "--campaign", required=True, metavar="NAME", help="Campaign name")
    sub = p.add_subparsers(dest="cmd")
    eff = sub.add_parser("effect")
    eff.add_argument("action", choices=["start", "end", "tick"])
    eff.add_argument("entity")
    eff.add_argument("spell", nargs="?", default="")
    eff.add_argument("duration", nargs="?", default="")
    eff.add_argument("conc", nargs="?", default="")
    cond = sub.add_parser("condition")
    cond.add_argument("action", choices=["add", "remove", "clear"])
    cond.add_argument("entity")
    cond.add_argument("condition", nargs="?", default="")
    conc = sub.add_parser("concentrate")
    conc.add_argument("entity")
    conc.add_argument("spell")
    sav = sub.add_parser("saves")
    sav.add_argument("entity")
    sav.add_argument("action", choices=["success", "failure", "stable", "reset"])
    stat = sub.add_parser("status")
    stat.add_argument("entity", nargs="?", default="")
    clr = sub.add_parser("clear")
    clr.add_argument("--all", action="store_true")
    args = p.parse_args()
    if args.cmd == "effect":
        cmd_effect(args.campaign, args.action, args.entity, args.spell, args.duration, args.conc.lower() == "conc")
    elif args.cmd == "condition":
        cmd_condition(args.campaign, args.entity, args.action, args.condition)
    elif args.cmd == "concentrate":
        cmd_concentrate(args.campaign, args.entity, args.spell)
    elif args.cmd == "saves":
        cmd_saves(args.campaign, args.entity, args.action)
    elif args.cmd == "status":
        cmd_status(args.campaign, args.entity)
    elif args.cmd == "clear":
        cmd_clear(args.campaign, getattr(args, 'all', False))
    else:
        p.print_help()

if __name__ == "__main__":
    main()
