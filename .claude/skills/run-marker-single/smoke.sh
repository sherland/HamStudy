#!/usr/bin/env bash
# Smoke test for marker_single: converts one PDF to markdown and checks the
# output looks real (non-empty .md, no traceback). Works from git-bash,
# WSL, or any POSIX shell on this machine.
#
# Usage:
#   ./smoke.sh [INPUT_FILE] [OUTPUT_DIR]
#
# Defaults to a small known-good file from this repo's source corpus.
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../../.." && pwd)"
INPUT="${1:-$REPO_ROOT/Kilder/primar/IARU-R1_HF-bandplan_effective-2016.pdf}"
OUTPUT_DIR="${2:-$REPO_ROOT/Kilder/markdown}"

MARKER_BIN="$(command -v marker_single || true)"
if [ -z "$MARKER_BIN" ]; then
  MARKER_BIN="/c/Users/stein/AppData/Local/Programs/Python/Python313/Scripts/marker_single.exe"
fi
if [ ! -x "$MARKER_BIN" ] && ! command -v "$MARKER_BIN" >/dev/null 2>&1; then
  echo "marker_single not found on PATH or at the known fallback path." >&2
  echo "Install with: pip install marker-pdf" >&2
  exit 1
fi

if [ ! -f "$INPUT" ]; then
  echo "Input file not found: $INPUT" >&2
  exit 1
fi

echo "Converting: $INPUT"
echo "Output dir: $OUTPUT_DIR"

"$MARKER_BIN" "$INPUT" \
  --output_format markdown \
  --output_dir "$OUTPUT_DIR" \
  --mode fast \
  --disable_ocr \
  --disable_tqdm

STEM="$(basename "$INPUT")"
STEM="${STEM%.*}"
OUT_MD="$OUTPUT_DIR/$STEM/$STEM.md"

if [ ! -s "$OUT_MD" ]; then
  echo "FAIL: expected markdown output not found or empty: $OUT_MD" >&2
  exit 1
fi

LINES="$(wc -l < "$OUT_MD")"
echo "OK: wrote $OUT_MD ($LINES lines)"
head -n 5 "$OUT_MD"
