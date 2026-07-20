#!/usr/bin/env python3
"""
lore_search.py — offline full-text search over the bundled Eberron lore library.

Searches the skill's `lore/` corpus (distilled references + `lore/fulltext/`
articles + `lore/fulltext/rulebooks/`) with case-insensitive substring matching
and simple relevance ranking. Prints the matching sections/paragraphs together
with their source filename so the DM can cite them (SOURCE line).

Usage:
    python3 lore_search.py "Phiarlan"
    python3 lore_search.py "Silver Flame" "Purge"      # all terms (AND) ranked first
    python3 lore_search.py warforged --any             # OR match (any term)
    python3 lore_search.py "Droaam" --files news       # restrict to filenames matching 'news'
    python3 lore_search.py "dragonmark" --list          # list matching files only
    python3 lore_search.py "lightning rail" -n 5        # cap number of shown snippets

Flags:
    --any            match ANY term (default: prefer sections matching ALL terms)
    --files <sub>    only search files whose path contains <sub> (e.g. 'news', 'rulebooks')
    --list           list matching files with hit counts, no snippets
    -n, --max N      max snippets to print (default 12)
    -C, --context N  paragraphs of surrounding context is not used; snippets are
                     whole sections/paragraphs. N caps snippet char length (default 900)

Resolves the lore dir relative to this script: ../lore/.
"""

import argparse
import os
import pathlib
import re
import sys

LORE_DIR = pathlib.Path(__file__).resolve().parent.parent / "lore"

# Files large enough that we search by paragraph rather than whole-section.
SECTION_SPLIT = re.compile(r"\n(?=#{1,3}\s)")      # markdown headers
PARA_SPLIT = re.compile(r"\n\s*\n")


def _iter_files(files_filter):
    """Yield (relpath, abspath) for every .md/.txt file under lore/."""
    if not LORE_DIR.exists():
        return
    for root, _dirs, names in os.walk(LORE_DIR):
        for n in sorted(names):
            if not (n.endswith(".md") or n.endswith(".txt")):
                continue
            ap = pathlib.Path(root) / n
            rel = ap.relative_to(LORE_DIR).as_posix()
            if files_filter and files_filter.lower() not in rel.lower():
                continue
            yield rel, ap


def _split_blocks(text):
    """Split a document into searchable blocks.

    Markdown files split on headers (keeps a section together with its title);
    plain text splits on blank-line paragraphs. Overlong blocks are further
    chunked so a snippet stays readable.
    """
    blocks = []
    parts = SECTION_SPLIT.split(text)
    if len(parts) == 1:
        parts = PARA_SPLIT.split(text)
    for p in parts:
        p = p.strip()
        if not p:
            continue
        if len(p) > 4000:
            # chunk very long blocks by paragraph
            for sub in PARA_SPLIT.split(p):
                sub = sub.strip()
                if sub:
                    blocks.append(sub)
        else:
            blocks.append(p)
    return blocks


def _title_of(block):
    """Return the header line of a markdown block, if any."""
    first = block.splitlines()[0].strip() if block else ""
    if first.startswith("#"):
        return first.lstrip("#").strip()
    return ""


def _score(block, terms):
    """Count total occurrences of all terms (case-insensitive)."""
    low = block.lower()
    counts = {t: low.count(t) for t in terms}
    total = sum(counts.values())
    matched_terms = sum(1 for c in counts.values() if c > 0)
    return total, matched_terms


def search(terms, files_filter=None, require_all=True, max_snips=12, snip_len=900):
    terms = [t.lower() for t in terms]
    hits = []  # (matched_terms, total, rel, title, block)
    file_hitcount = {}
    for rel, ap in _iter_files(files_filter):
        try:
            text = ap.read_text(encoding="utf-8", errors="replace")
        except OSError:
            continue
        for block in _split_blocks(text):
            total, matched = _score(block, terms)
            if total == 0:
                continue
            if require_all and matched < len(terms):
                # keep as a weaker match, but rank below full matches
                pass
            hits.append((matched, total, rel, _title_of(block), block))
            file_hitcount[rel] = file_hitcount.get(rel, 0) + total
    # rank: most terms matched, then most occurrences, then shorter block
    hits.sort(key=lambda h: (-h[0], -h[1], len(h[4])))
    return hits[:max_snips], file_hitcount


def _highlight(block, terms, snip_len):
    """Trim a block to a window around the first term hit, with a header line."""
    low = block.lower()
    pos = min((low.find(t) for t in terms if low.find(t) != -1), default=0)
    start = max(0, pos - snip_len // 3)
    end = min(len(block), start + snip_len)
    snippet = block[start:end].strip()
    if start > 0:
        snippet = "… " + snippet
    if end < len(block):
        snippet = snippet + " …"
    return snippet


def main():
    ap = argparse.ArgumentParser(
        description="Offline full-text search over the bundled Eberron lore library.")
    ap.add_argument("terms", nargs="+", help="search term(s)")
    ap.add_argument("--any", action="store_true",
                    help="match ANY term (default prefers sections matching ALL terms)")
    ap.add_argument("--files", default=None,
                    help="only search files whose path contains this substring")
    ap.add_argument("--list", action="store_true",
                    help="list matching files with hit counts, no snippets")
    ap.add_argument("-n", "--max", type=int, default=12,
                    help="max snippets to print (default 12)")
    ap.add_argument("-C", "--context", type=int, default=900,
                    help="max snippet length in characters (default 900)")
    args = ap.parse_args()

    if not LORE_DIR.exists():
        print(f"Lore directory not found: {LORE_DIR}", file=sys.stderr)
        sys.exit(1)

    hits, file_hitcount = search(
        args.terms, files_filter=args.files, require_all=not args.any,
        max_snips=args.max, snip_len=args.context)

    query = " ".join(args.terms)
    if not hits:
        print(f"No lore matches for '{query}'"
              + (f" in files matching '{args.files}'." if args.files else "."))
        print("Nothing in the bundled corpus covers this — you may improvise and "
              "flag it as new canon (record it in the campaign's world.md).")
        return

    if args.list:
        print(f"Files matching '{query}' ({len(file_hitcount)}):")
        for rel, c in sorted(file_hitcount.items(), key=lambda x: -x[1]):
            print(f"  {c:>4} hits  {rel}")
        return

    print(f"Lore matches for '{query}' — {len(hits)} snippet(s) "
          f"(from {len(file_hitcount)} file(s)):\n")
    for matched, total, rel, title, block in hits:
        head = f"[{rel}]" + (f"  §{title}" if title else "")
        print("=" * 70)
        print(head)
        print("-" * 70)
        print(_highlight(block, [t.lower() for t in args.terms], args.context))
        print()
    print("Cite the source filename(s) above in your SOURCE line. "
          "lore/ is canonical over training-knowledge Eberron lore.")


if __name__ == "__main__":
    main()
