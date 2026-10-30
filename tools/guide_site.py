#!/usr/bin/env python3
"""The user guide as a folder for an Unseenet site: unseenet.help.guide (#7).

    python tools/guide_site.py build/docs OUT

Reads the guide's pages (build/docs/use/, after tools/gather.py has put the
pictures from unseenet-gui beside them) and writes OUT/: one Markdown file per
page and the pictures they show, for the core's site import to publish:

    unseenet site-publish OUT unseenet.help.guide@ph5fc5hop5232qsz --yes

UN-RFC 0031 Markdown has no tabs, admonitions or keyboard keys, so:

- each tab (=== "Graphical") becomes a heading of its own, its text unindented;
- a box (!!! tip "Do this now") becomes a quote with its title in bold;
- ++ctrl+p++ becomes `Ctrl+P`;
- `{ ... }` attribute lists go;
- a link to another guide page stays relative (the site import makes it a page
  link); a link elsewhere on unseenet.org becomes its address there;
- pictures Unseenet cannot carry (SVG: the terminal client's) are left out, and
  the others are copied into OUT/img/;
- pages about the web (WEB_ONLY) stay on unseenet.org, and links to them go there.

The Markdown in pages/use/ stays the one source; this runs from CI after the docs
are built (the core's publish-guide workflow), never by hand edits in Unseenet.
"""

from __future__ import annotations

import re
import shutil
import sys
from pathlib import Path, PurePosixPath

SITE = "https://unseenet.org/"
GUIDE = "use"
# pages that are about the web and stay there: links to them go to unseenet.org
WEB_ONLY = {"show-your-name.md"}
NOTE = ("\n\n---\n\n*This is the user guide from [unseenet.org](https://unseenet.org/use/), "
        "published here by the project. Something wrong or missing? Say so in "
        "!unseenet.help, or open an "
        "[issue on GitHub](https://github.com/unseenet/unseenet-docs/issues).*\n")

KEYS = {"ctrl": "Ctrl", "shift": "Shift", "alt": "Alt", "escape": "Esc", "enter": "Enter",
        "space": "Space", "tab": "Tab", "question-mark": "?", "up": "↑", "down": "↓"}
TABS = {"Graphical": "In the graphical client", "Terminal": "In the terminal client"}


def key(m: re.Match) -> str:
    parts = m.group(1).split("+")
    out = [KEYS.get(p, p.upper() if len(p) > 1 else p) for p in parts]
    if len(parts) > 1:                         # Ctrl+P, not Ctrl+p
        out[-1] = out[-1].upper() if len(out[-1]) == 1 else out[-1]
    return "`" + "+".join(out) + "`"


def link(target: str, page: PurePosixPath) -> str | None:
    """What a relative link in a guide page becomes; None leaves it out (a picture)."""
    if re.match(r"^[a-z][a-z0-9+.-]*:", target) or target.startswith("#"):
        return target
    path, _, anchor = target.partition("#")
    full = PurePosixPath(*_resolve(page.parent / path))
    if full.parent == PurePosixPath(GUIDE) and full.suffix == ".md" and full.name not in WEB_ONLY:
        return full.name + ("#" + anchor if anchor else "")       # another guide page
    if full.suffix == ".md":
        stem = full.with_suffix("")
        web = "" if stem.name == "index" and stem.parent == PurePosixPath(".") else \
            (str(stem.parent) + "/" if stem.name == "index" else str(stem) + "/")
        return SITE + web + ("#" + anchor if anchor else "")
    return SITE + str(full)


def _resolve(p: PurePosixPath) -> list[str]:
    parts: list[str] = []
    for part in p.parts:
        if part == "..":
            parts.pop()
        elif part != ".":
            parts.append(part)
    return parts


def convert(text: str, page: PurePosixPath, docs: Path, out: Path) -> str:
    lines, result, i = text.splitlines(), [], 0
    while i < len(lines):
        line = lines[i]
        tab = re.match(r'^=== "(.+)"\s*$', line)
        box = re.match(r'^!!! \w+(?: "(.*)")?\s*$', line)
        if tab or box:
            body, i = [], i + 1
            while i < len(lines) and (lines[i].startswith("    ") or not lines[i].strip()):
                body.append(lines[i][4:])
                i += 1
            while body and not body[-1].strip():
                body.pop()
            if tab:
                result += ["#### " + TABS.get(tab.group(1), tab.group(1)), ""] + body + [""]
            else:
                title = box.group(1)
                quoted = ([f"> **{title}**", ">"] if title else []) + \
                    [("> " + b).rstrip() for b in body]
                result += quoted + [""]
            continue
        result.append(line)
        i += 1
    text = "\n".join(result)
    text = re.sub(r"\+\+([a-z0-9+-]+?)\+\+", key, text)
    text = re.sub(r"\{[^{}\n]*\}(?=\s|$)", "", text)               # attribute lists

    def picture(m: re.Match) -> str:
        alt, target = m.group(1), m.group(2)
        src = docs / PurePosixPath(*_resolve(page.parent / target))
        if src.suffix.lower() not in (".png", ".jpg", ".jpeg", ".gif", ".webp") or not src.exists():
            return ""
        (out / "img").mkdir(exist_ok=True)
        shutil.copy(src, out / "img" / src.name)
        return f"![{alt}](img/{src.name})"

    text = re.sub(r"!\[([^\]]*)\]\(([^)\s]+)\)", picture, text)
    text = re.sub(r"(?<!!)\[([^\]]+)\]\(([^)\s]+)\)",
                  lambda m: f"[{m.group(1)}]({link(m.group(2), page)})", text)
    text = text.replace("Each page has a tab for the **graphical** client and one for the\n"
                        "**terminal** client; pick the one you use, and the other pages follow your choice.",
                        "Each page says how in the **graphical** client and in the **terminal**\nclient.")
    text = re.sub(r"\n{3,}", "\n\n", text).strip() + "\n"
    return text


def main() -> int:
    docs, out = Path(sys.argv[1]), Path(sys.argv[2])
    if out.exists():
        shutil.rmtree(out)
    out.mkdir(parents=True)
    pages = sorted(p for p in (docs / GUIDE).glob("*.md") if p.name not in WEB_ONLY)
    if not pages:
        sys.exit(f"no guide pages in {docs / GUIDE}: run tools/gather.py first")
    for src in pages:
        page = PurePosixPath(GUIDE) / src.name
        text = convert(src.read_text(encoding="utf-8"), page, docs, out)
        (out / src.name).write_text(text + (NOTE if src.name == "index.md" else ""), encoding="utf-8")
    print(f"{len(pages)} pages into {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
