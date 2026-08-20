---
name: run-marker-single
description: Convert a PDF (or scanned image) in this repo to Markdown using marker_single. Use when asked to run marker, convert a PDF to markdown, extract text/tables from a source document, or add a new primary source to Kilder/.
---

`marker_single` is a CLI tool (from the `marker-pdf` Python package, already
installed for this user) that converts one document into structured
Markdown/JSON/HTML — including tables, unlike the repo's existing
`scripts/extract_pdf_text.py` (plain-text pypdf extraction, no table
structure). Drive it via
`.claude/skills/run-marker-single/smoke.sh`, or call `marker_single`
directly — it's a one-shot CLI, there's no server/process to manage.

This skill is duplicated at `.agents/skills/run-marker-single/` — the
[Agent Skills](https://agentskills.io/specification) cross-client
convention read by Codex, Copilot, Gemini CLI, Cursor, and other
standards-compliant agents, in addition to Claude Code's native
`.claude/skills/`. It's a plain file copy, not a link: NTFS junctions
were tried first but don't survive `git add` (git dereferences them
and commits two independent copies anyway — confirmed with `git add
--dry-run`) and broke the moment a parent directory got renamed, so a
junction bought nothing but fragility. **When editing this skill,
update both `SKILL.md`/`smoke.sh` copies** (`.claude/skills/` and
`.agents/skills/`) — they must stay identical by hand. See
[AGENTS.md](../../../AGENTS.md) at the repo root for the
client-agnostic summary.

All paths below are relative to the repo root
(`c:\Source\HAM\Research`).

## Prerequisites

Already installed on this machine:

```bash
python -m pip show marker-pdf
# → Version: 2.0.0
```

If it's missing elsewhere: `pip install marker-pdf`. There is no
`--version` flag — `pip show marker-pdf` is how you check the version.

The binary is on this machine at:

```
C:\Users\stein\AppData\Local\Programs\Python\Python313\Scripts\marker_single.exe
```

`smoke.sh` looks for `marker_single` on `PATH` first and falls back to
that absolute path, so it works whether or not the Python `Scripts`
directory has been added to `PATH`.

## Run (agent path)

Convert a file with the smoke script (verified working on this repo's
corpus of source PDFs):

```bash
.claude/skills/run-marker-single/smoke.sh
# → converts Kilder/primar/IARU-R1_HF-bandplan_effective-2016.pdf
# → writes Kilder/markdown/IARU-R1_HF-bandplan_effective-2016/IARU-R1_HF-bandplan_effective-2016.md
# → OK: wrote .../IARU-R1_HF-bandplan_effective-2016.md (162 lines)
```

Convert a specific file to a specific output directory:

```bash
.claude/skills/run-marker-single/smoke.sh "Kilder/primar/CEPT_TR_61-02_2024-02-16.pdf" "Kilder/markdown"
```

Or call `marker_single` directly (this is what the script wraps) —
this is the invocation to use for every text-based source PDF in this
repo:

```bash
marker_single "Kilder/primar/CEPT_TR_61-02_2024-02-16.pdf" \
  --output_format markdown \
  --output_dir Kilder/markdown \
  --mode fast \
  --disable_ocr \
  --disable_tqdm
```

Output lands at `<output_dir>/<input-stem>/<input-stem>.md`, plus a
`<stem>_meta.json` (table of contents + per-page stats — check
`text_extraction_method` per page: `pdftext` means it read the real
text layer, no OCR involved) and any extracted images as
`_page_N_Picture_M.jpeg` next to the markdown.

For a scanned source with no text layer (e.g. `Bok/Innhold-*.jpg`),
drop `--disable_ocr` — but make sure Docker Desktop is running first.
Verified working:

```bash
marker_single "Bok/Innhold-2.jpg" \
  --output_format markdown \
  --output_dir Kilder/markdown \
  --mode fast \
  --disable_tqdm
# → Table processing stats: {'tables_ocr': 8, 'tables_total': 8}
# → Saved markdown to Kilder/markdown\Innhold-2
# → Total time: 248.77 (this run; first-ever run on a machine is much
#   longer — see Gotchas)
```

Other useful flags:

| flag | effect |
|---|---|
| `--output_format json\|html\|chunks` | different output shape, same content |
| `--page_range 0,5-10` | convert only specific pages (0-indexed) — use for the large `IARU-R1_VHF-Handbook_v10.02.pdf` (7 MB) instead of the whole doc |
| `--output_dir DIR` | where results are written |

## Run (human path)

Same command, just read the resulting `.md` file afterward. No
separate human path — it's a one-shot conversion, not something with
a UI to click through.

## Verify it's working

```bash
.claude/skills/run-marker-single/smoke.sh
echo $?   # 0 on success; script also fails loudly if the .md is missing/empty
```

---

## Gotchas

- **`--disable_ocr` is the correct default for this repo's PDFs, not
  a compromise.** Every source PDF already checked into
  `Kilder/primar/` has a real embedded text layer (confirmed via
  `Kilder/tekst/*.txt`, produced by `scripts/extract_pdf_text.py`), so
  `text_extraction_method: pdftext` is used and OCR is never needed.
  Without `--disable_ocr`, `--mode fast` still silently tries to spin
  up an OCR *recognition* backend for any table it isn't fully
  confident about — see next point.
- **OCR (i.e. `--mode fast`/`balanced` without `--disable_ocr`) needs
  either Docker or llama.cpp, and is slow and somewhat flaky even when
  it works.** Surya's OCR recognition model runs behind an inference
  server — vLLM-in-Docker (auto-selected here because `nvidia-smi`
  finds the RTX 3090) or llama.cpp:
  - Without Docker Desktop running:
    `SpawnError: docker run failed: ... npipe:////./pipe/dockerDesktopLinuxEngine ...`.
    Forcing `SURYA_INFERENCE_BACKEND=llamacpp` avoids Docker but then
    fails with `llama-server binary not found` (llama.cpp isn't
    installed on this machine).
  - **With Docker Desktop running, it works — but budget for it.**
    Verified over 3 attempts on `Bok/Innhold-*.jpg` (scanned images,
    no text layer — `--disable_ocr` on these produces an **empty**
    `.md`, confirmed):
    - First ever run: pulls `vllm/vllm-openai:v0.20.1`, a **23.3 GB**
      image. Total time **~26 minutes** for one page.
    - With the image cached: 1 of 2 follow-up attempts still failed —
      `SpawnError: vllm server failed to become healthy at
      http://127.0.0.1:PORT within 600.0s` (`docker logs` for the
      container came back empty; it had already been torn down). The
      other attempt succeeded in **~4 minutes** for one page.
    - So: works, but plan for a possible retry, and each attempt that
      fails costs the full 10-minute startup timeout before it gives
      up.
- **Output is nested one directory deeper than you'd guess.**
  `--output_dir Kilder/markdown` on `foo.pdf` writes to
  `Kilder/markdown/foo/foo.md`, not `Kilder/markdown/foo.md`.
- **The whole-repo `IARU-R1_VHF-Handbook_v10.02.pdf` is 7 MB / many
  pages** — use `--page_range` to grab only the section you need
  instead of converting the whole handbook.
- **First run on a machine with no model cache is slow** (downloads
  layout/detection models to `~/.cache/huggingface` and
  `~/.cache/datalab`, ~100+ MB). Already cached on this machine — a
  2-page PDF converts in ~4–5 seconds.

## Troubleshooting

- **`SpawnError: docker run failed: ... dockerDesktopLinuxEngine ...`**:
  `--mode fast`/`balanced` tried to OCR something and reached for the
  vLLM-in-Docker backend, but Docker Desktop's Linux engine isn't
  running. Add `--disable_ocr` (works for every text-based PDF in this
  repo), or start Docker Desktop first (Docker Desktop → make sure
  it's actually running, not just installed) if you need real OCR.
- **`SpawnError: llama-server binary not found`**: happened after
  setting `SURYA_INFERENCE_BACKEND=llamacpp` to sidestep the Docker
  issue above — llama.cpp isn't installed on this machine either. Same
  fix: `--disable_ocr` for text-based sources, or install
  `llama-server` for real OCR.
- **`SpawnError: vllm server failed to become healthy at
  http://127.0.0.1:PORT within 600.0s`**: Docker Desktop was running
  and the image was already pulled, but the container still failed to
  come up in time (observed once out of three attempts here, cause
  unclear — `docker ps -a`/`docker logs` showed nothing, the container
  was already gone). Just retry the same command; it succeeded on the
  next attempt without any other change.
- **First real-OCR run takes ~25+ minutes**: it's pulling the 23.3 GB
  `vllm/vllm-openai` image, not stuck. Only happens once per machine —
  subsequent runs (when the container starts successfully) take a
  few minutes per page instead.
- **Output `.md` file exists but is empty**: the input had no text
  layer and OCR was disabled (e.g. a scanned image like
  `Bok/Innhold-1.jpg`). This isn't a bug — re-run without
  `--disable_ocr` once a working OCR backend is available (see
  Gotchas above).
