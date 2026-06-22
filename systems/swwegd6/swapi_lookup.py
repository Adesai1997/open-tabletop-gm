#!/usr/bin/env python3
"""
SWAPI Lookup — Star Wars D6 System Module Helper
Queries https://swapi.dev/api for canonical film data to enrich tabletop sessions.

Usage:
    python swapi_lookup.py people "Luke Skywalker"
    python swapi_lookup.py planets Tatooine
    python swapi_lookup.py species Wookiee
    python swapi_lookup.py vehicles "Snowspeeder"
    python swapi_lookup.py starships "Millennium Falcon"
    python swapi_lookup.py films "A New Hope"

Returns a formatted summary suitable for GM/player reference at the table.
SWAPI covers Episodes IV–VI canon. For Legends/EU content, use sourcebook stats.

Requires: requests (pip install requests)
API docs: https://swapi.dev/documentation
"""

import sys

try:
    import requests
except ImportError:
    print("ERROR: 'requests' library not found. Install with: pip install requests")
    sys.exit(1)

BASE_URL = "https://swapi.dev/api"

ENDPOINT_MAP = {
    "people": "people",
    "planets": "planets",
    "species": "species",
    "vehicles": "vehicles",
    "starships": "starships",
    "films": "films",
}

DISPLAY_FIELDS = {
    "people": [("Name", "name"), ("Height", "height"), ("Mass", "mass"), ("Hair Color", "hair_color"), ("Eye Color", "eye_color"), ("Skin Color", "skin_color"), ("Birth Year", "birth_year"), ("Gender", "gender"), ("Homeworld", "homeworld")],
    "planets": [("Name", "name"), ("Rotation Period", "rotation_period"), ("Orbital Period", "orbital_period"), ("Diameter", "diameter"), ("Climate", "climate"), ("Gravity", "gravity"), ("Terrain", "terrain"), ("Surface Water", "surface_water"), ("Population", "population")],
    "species": [("Name", "name"), ("Classification", "classification"), ("Designation", "designation"), ("Average Height", "average_height"), ("Skin Colors", "skin_colors"), ("Hair Colors", "hair_colors"), ("Eye Colors", "eye_colors"), ("Average Lifespan", "average_lifespan"), ("Language", "language")],
    "vehicles": [("Name", "name"), ("Model", "model"), ("Manufacturer", "manufacturer"), ("Cost (credits)", "cost_in_credits"), ("Length (m)", "length"), ("Max Speed", "max_atmosphering_speed"), ("Crew", "crew"), ("Passengers", "passengers"), ("Cargo (kg)", "cargo_capacity"), ("Vehicle Class", "vehicle_class")],
    "starships": [("Name", "name"), ("Model", "model"), ("Manufacturer", "manufacturer"), ("Cost (credits)", "cost_in_credits"), ("Length (m)", "length"), ("Max Speed (atm)", "max_atmosphering_speed"), ("Crew", "crew"), ("Passengers", "passengers"), ("Cargo (kg)", "cargo_capacity"), ("Consumables", "consumables"), ("Hyperdrive Rating", "hyperdrive_rating"), ("MGLT", "MGLT"), ("Starship Class", "starship_class")],
    "films": [("Title", "title"), ("Episode", "episode_id"), ("Director", "director"), ("Producer", "producer"), ("Release Date", "release_date"), ("Opening Crawl", "opening_crawl")],
}


def search_swapi(endpoint: str, query: str):
    try:
        resp = requests.get(f"{BASE_URL}/{endpoint}/", params={"search": query}, timeout=10)
        resp.raise_for_status()
        data = resp.json()
        results = data.get("results", [])
        return results[0] if results else None
    except requests.RequestException as e:
        print(f"ERROR: Could not reach SWAPI — {e}")
        return None


def resolve_url(url: str) -> str:
    try:
        resp = requests.get(url, timeout=8)
        resp.raise_for_status()
        data = resp.json()
        return data.get("name") or data.get("title") or url
    except Exception:
        return url


def format_result(category: str, result: dict) -> str:
    lines = [f"\n{'='*50}", f"  SWAPI: {category.upper()} DATA", f"{'='*50}"]
    for label, key in DISPLAY_FIELDS.get(category, []):
        value = result.get(key, "unknown")
        if key == "homeworld" and isinstance(value, str) and value.startswith("http"):
            value = resolve_url(value)
        if key == "opening_crawl" and isinstance(value, str) and len(value) > 200:
            value = value[:200].replace("\r\n", " ").strip() + "..."
        lines.append(f"  {label:<20} {value}")
    lines.append(f"{'='*50}\n")
    lines.append("NOTE: SWAPI provides film-canon data (Ep. IV–VI).")
    lines.append("For full D6 stat blocks, consult the relevant WEG sourcebook.")
    lines.append("For Legends/EU data, sourcebook data takes precedence.\n")
    return "\n".join(lines)


def main():
    if len(sys.argv) < 3:
        print(__doc__)
        sys.exit(0)
    category = sys.argv[1].lower()
    query = " ".join(sys.argv[2:])
    if category not in ENDPOINT_MAP:
        print(f"Unknown category: '{category}'")
        print(f"Valid categories: {', '.join(ENDPOINT_MAP.keys())}")
        sys.exit(1)
    result = search_swapi(ENDPOINT_MAP[category], query)
    if result is None:
        print(f"\nNot found in SWAPI: '{query}' ({category})")
        print("Suggestion: Check spelling or use a shorter search term.")
        print("For this entity, use sourcebook stat blocks or GM improvisation.")
        sys.exit(0)
    print(format_result(category, result))


if __name__ == "__main__":
    main()
