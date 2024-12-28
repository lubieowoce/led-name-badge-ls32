#!/usr/bin/env bash
set -eu -o pipefail
direction="$1"
img="$2"

d="$(mktemp -d)";
f="$d/out.png";
uv run ./scroll.py "$direction" "$img" "$f";
uv run ./led-badge-11x44.py -s9 -m5 "$f"
