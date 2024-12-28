#!/usr/bin/env bash
set -eu -o pipefail

function scroll {
  d="$(mktemp -d)";
  f="$d/out.png";
  uv run ./scroll.py "$@" "$f" >/dev/null;
  echo "$f"
}

function from-gif {
  d="$(mktemp -d)";
  f="$d/out.png";
  uv run ./from_gif.py "$@" "$f" >/dev/null;
  echo "$f"
}

# "$(scroll down "$HOME/Documents/ledtag/38c3-45.png")"

# uv run ./led-badge-11x44.py -B50 -s7,10,9 -m3,5,5 \
#   "owoce 8106"
#   "$(scroll right "$HOME/Documents/ledtag/longcat.png")" \
#   "$(scroll down "$HOME/Documents/ledtag/cat.png")"

# uv run ./led-badge-11x44.py -B50 -s7,10,9 -m3,5,5 \
#   "$HOME/Documents/ledtag/nametag.png" \
#   "$(scroll right "$HOME/Documents/ledtag/longcat.png")" \
#   "$(scroll down "$HOME/Documents/ledtag/cat.png")"

# uv run ./led-badge-11x44.py -B50 -s7,10,9 -m3,5,5 \
#   "$HOME/Documents/ledtag/nametag.png" \
#   "$(scroll right "$HOME/Documents/ledtag/longcat-dark.png")" \
#   "$(scroll down "$HOME/Documents/ledtag/cat.png")"

uv run ./led-badge-11x44.py -s7,9 -m0,5 \
  "hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhrmny - 6691" \
  "$(BACKGROUND=black from-gif "$HOME/Documents/ledtag/hrmny/train.gif")"

# uv run ./led-badge-11x44.py -s9 -m5 \
#   "$(BACKGROUND=black from-gif "$HOME/Documents/ledtag/hrmny/train.gif")"

# uv run ./led-badge-11x44.py -s9 -m5 \
#   "$(BACKGROUND=black from-gif "$HOME/Documents/ledtag/hrmny/train.gif")"

# uv run ./led-badge-11x44.py -B50 -s7 -m3 "$HOME/Documents/ledtag/nametag.png"

# uv run ./led-badge-11x44.py -B50 -s10 -m5 \
#   "$(scroll right "$HOME/Documents/ledtag/longcat-dark.png")"

# d="$(mktemp -d)"; f="$d/out.png"; uv run ./scroll.py "right" "$HOME/Documents/ledtag/longcat-dark.png" "$f"; open "$f"
