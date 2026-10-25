#!/usr/bin/env bash
# Build unseenet.org: gather the pages from every repository, then mkdocs.
#   pip install -r requirements.txt
#   ./build.sh                 # into site/
#   ./build.sh serve           # preview at http://127.0.0.1:8000
#   ./build.sh --local unseenet=../unseenet [serve]   # with a local checkout
set -euo pipefail
cd "$(dirname "$0")"
ARGS=(); SERVE=
for a in "$@"; do if [ "$a" = serve ]; then SERVE=1; else ARGS+=("$a"); fi; done
python tools/gather.py "${ARGS[@]+"${ARGS[@]}"}"
if [ -n "$SERVE" ]; then mkdocs serve; else
  mkdocs build --strict
  cp -r site-extra/.well-known site/          # mkdocs skips dot folders
fi
