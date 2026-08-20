# Agent instructions for this repo

This file is read by coding agents generally (Codex, GitHub Copilot,
Claude Code, etc.). Skills with fuller instructions live at
`.agents/skills/*/SKILL.md` — the
[Agent Skills](https://agentskills.io/specification) open standard for
skill discovery, read by Codex, Copilot, Gemini CLI, Cursor, and other
standards-compliant agents. (Claude Code additionally auto-loads its own native
`.claude/skills/*/SKILL.md`; on this repo that's a manually-kept-in-sync
duplicate, not a link — see the note in each skill for why.) Those
`SKILL.md` files are the
authoritative source; this AGENTS.md is a portable summary for agents
that read this file but don't scan skill directories on their own.

## Converting a source PDF/image to Markdown (marker_single)

`marker_single` (from the `marker-pdf` Python package) converts a PDF
or image into structured Markdown, including tables — better than the
repo's plain-text `scripts/extract_pdf_text.py` for anything with
tables (frequency bands, license classes, etc.).

Verified working invocation for this repo's source corpus in
`Kilder/primar/` (all of it text-based PDFs, confirmed via
`Kilder/tekst/*.txt`):

```bash
marker_single "Kilder/primar/<file>.pdf" \
  --output_format markdown \
  --output_dir Kilder/markdown \
  --mode fast \
  --disable_ocr \
  --disable_tqdm
```

Output lands at `Kilder/markdown/<stem>/<stem>.md`. A ready-made
wrapper that also fails loudly if the output is missing/empty:

```bash
.agents/skills/run-marker-single/smoke.sh "Kilder/primar/<file>.pdf" "Kilder/markdown"
```

If `marker_single` isn't on `PATH`, install with `pip install
marker-pdf`.

**Keep `--disable_ocr` for this repo's PDFs.** Every current source
PDF in `Kilder/primar/` has a real text layer, so OCR is never
actually needed there, and it's the fast/reliable path (a few seconds
per document). The one case where OCR *would* be needed is a scanned
image with no text layer (e.g. `Bok/Innhold-*.jpg`) — `--disable_ocr`
on those produces an empty `.md`, which is expected, not a bug.

For that OCR case: drop `--disable_ocr` and make sure Docker Desktop
is running first (it spins up a vLLM container). This has been
verified working, but budget for it — the first run ever on a machine
pulls a 23.3 GB image (~25+ minutes just for that), and even with the
image cached it can take several minutes per page and occasionally
fails with `vllm server failed to become healthy ... within 600.0s`;
retrying the same command has been enough to recover.

Full details, gotchas, and troubleshooting:
[.agents/skills/run-marker-single/SKILL.md](.agents/skills/run-marker-single/SKILL.md).
