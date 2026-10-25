#!/usr/bin/env python3
"""Gather the pages of unseenet.org into build/ (unseenet#547).

    python tools/gather.py [--local unseenet=../unseenet ...]

Reads sources.yml, checks each source out into build/sources/<name> (or uses a
local checkout given with --local, for previewing a change before it is
merged), copies its docs into build/docs/<into>, the UN-RFCs into
build/docs/spec/, and this repository's pages/ on top. Writes
build/origins.json: for every page, the address to edit it at, which the
hooks use for the "Edit" button, since the pages come from several
repositories.
"""

from __future__ import annotations

import argparse
import json
import shutil
import subprocess
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
BUILD = ROOT / "build"
THIS = "unseenet/unseenet-docs"


def checkout(repo: str, ref: str, dest: Path) -> None:
    if dest.exists():
        shutil.rmtree(dest)
    subprocess.run(["git", "clone", "-q", "--depth", "1", "--branch", ref,
                    f"https://github.com/{repo}", str(dest)], check=True)


def copy_tree(src: Path, dest: Path, origin: str, origins: dict[str, str], site: Path,
              wins: bool = False) -> list[str]:
    """Copy src into dest; return the pages that were already there."""
    clashes = []
    for f in sorted(src.rglob("*")):
        if not f.is_file():
            continue
        rel = f.relative_to(src)
        target = dest / rel
        page = target.relative_to(site).as_posix()
        if target.exists() and page.endswith(".md"):
            clashes.append(page)
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(f, target)
        if page.endswith(".md"):
            origins[page] = f"{origin}/{rel.as_posix()}"
    return clashes


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--local", action="append", default=[], metavar="NAME=PATH",
                    help="use a local checkout for a source, e.g. unseenet=../unseenet")
    args = ap.parse_args(argv)
    local = dict(x.split("=", 1) for x in args.local)

    sources = yaml.safe_load((ROOT / "sources.yml").read_text())["sources"]
    site = BUILD / "docs"
    if site.exists():
        shutil.rmtree(site)
    site.mkdir(parents=True)
    origins: dict[str, str] = {}

    for s in sources:
        name = s["repo"].split("/", 1)[1]
        if name in local:
            where = Path(local[name]).resolve()
            print(f"{s['repo']}: local checkout {where}")
        else:
            where = BUILD / "sources" / name
            print(f"{s['repo']}@{s['ref']}")
            checkout(s["repo"], s["ref"], where)
        edit = f"https://github.com/{s['repo']}/edit/{s['ref']}"
        into = site / s.get("into", "")
        copy_tree(where / s["docs"], into, f"{edit}/{s['docs']}", origins, site)
        if s.get("spec"):
            spec, rfc = site / "spec", where / s["spec"]
            spec.mkdir(parents=True, exist_ok=True)
            for f in sorted(rfc.glob("un-rfc-*.md")) + [rfc / "LICENSE.md"]:
                shutil.copy2(f, spec / f.name)
                origins[f"spec/{f.name}"] = f"{edit}/{s['spec']}/{f.name}"
            shutil.copy2(rfc / "README.md", spec / "index.md")
            origins["spec/index.md"] = f"{edit}/{s['spec']}/README.md"
        if s.get("src"):
            link = BUILD / "src"
            if link.is_symlink() or link.exists():
                link.unlink() if link.is_symlink() else shutil.rmtree(link)
            link.symlink_to(where / s["src"])

    clashes = copy_tree(ROOT / "pages", site, f"https://github.com/{THIS}/edit/main/pages",
                        origins, site)
    for page in clashes:
        print(f"  {page}: pages/ wins over the source's copy (being moved here)")
    (BUILD / "origins.json").write_text(json.dumps(origins, indent=1, sort_keys=True))
    print(f"{len(origins)} pages in {site.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
