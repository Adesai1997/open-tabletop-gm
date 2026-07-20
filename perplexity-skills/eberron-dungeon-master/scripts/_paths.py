"""
_paths.py — standalone campaign path resolver for the eberron-dungeon-master skill.

Replaces the upstream open-tabletop-gm scripts/paths.py (which resolved to
~/open-tabletop-gm). In the Perplexity Computer sandbox, campaign working files
live under the workspace so they can be uploaded to / restored from the project's
Files section between threads.

Set GM_CAMPAIGN_ROOT to move the local working tree. Defaults to
/home/user/workspace/campaigns.

Adapted from Bobby-Gray/open-tabletop-gm (AGPL-3.0-or-later).
"""

import os
import pathlib

_DEFAULT_ROOT = pathlib.Path("/home/user/workspace/campaigns")


def _root() -> pathlib.Path:
    raw = os.environ.get("GM_CAMPAIGN_ROOT", "")
    if raw.strip():
        return pathlib.Path(raw.strip()).expanduser().resolve()
    return _DEFAULT_ROOT


def campaigns_dir() -> pathlib.Path:
    """Return the campaigns directory under the configured root.

    In this standalone skill there is no separate campaigns/ subdirectory —
    each campaign is a directory directly under the root, e.g.
    /home/user/workspace/campaigns/<name>/. This keeps local working files
    aligned with the campaign--<name>--*.md project-file naming convention.
    """
    return _root()


def campaign_dir(name: str) -> pathlib.Path:
    return campaigns_dir() / name


if __name__ == "__main__":
    print(f"Campaign root: {_root()}")
