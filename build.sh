#!/usr/bin/env bash
set -eu -o pipefail

function transform {
  d="$(mktemp -d)";
  f="$d/out.png";
  uv run ./scroll.py "$@" "$f" >/dev/null;
  echo "$f"
}

# "$(transform down "$HOME/Documents/ledtag/38c3-45.png")"

# uv run ./led-badge-11x44.py -B50 -s7,10,9 -m3,5,5 \
#   "owoce 8106"
#   "$(transform right "$HOME/Documents/ledtag/longcat.png")" \
#   "$(transform down "$HOME/Documents/ledtag/cat.png")"

# uv run ./led-badge-11x44.py -B50 -s7,10,9 -m3,5,5 \
#   "$HOME/Documents/ledtag/nametag.png" \
#   "$(transform right "$HOME/Documents/ledtag/longcat.png")" \
#   "$(transform down "$HOME/Documents/ledtag/cat.png")"

uv run ./led-badge-11x44.py -B50 -s7,10,9 -m3,5,5 \
  "$HOME/Documents/ledtag/nametag.png" \
  "$(transform right "$HOME/Documents/ledtag/longcat-dark.png")" \
  "$(transform down "$HOME/Documents/ledtag/cat.png")"

# uv run ./led-badge-11x44.py -B50 -s7 -m3 "$HOME/Documents/ledtag/nametag.png"

# uv run ./led-badge-11x44.py -B50 -s10 -m5 \
#   "$(transform right "$HOME/Documents/ledtag/longcat-dark.png")"

# d="$(mktemp -d)"; f="$d/out.png"; uv run ./scroll.py "right" "$HOME/Documents/ledtag/longcat-dark.png" "$f"; open "$f"