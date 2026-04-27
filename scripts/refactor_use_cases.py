#!/usr/bin/env python3
"""
Split src/data/use-cases.ts into:
  - src/data/use-cases.ts (metadata only — id, type, iconKey, colorTheme, slug, content: makeContent('id'))
  - src/data/use-cases-content.es.ts (Record<string, UseCaseContent> with all 51 ES content blobs)
  - src/data/use-cases-content.en.ts (empty Partial<Record<string, UseCaseContent>>, ready for EN translations)

This is a one-shot mechanical refactor — IDEMPOTENT it is NOT (run only once on the original file).
"""

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "src" / "data" / "use-cases.ts"
OUT_TS = ROOT / "src" / "data" / "use-cases.ts"
OUT_ES = ROOT / "src" / "data" / "use-cases-content.es.ts"
OUT_EN = ROOT / "src" / "data" / "use-cases-content.en.ts"

src_text = SRC.read_text()
lines = src_text.split("\n")

# Find each spoke's id line and the matching `content: makeStubContent({` line.
# Then find the closing `    }),` line that ends the content object.
# Layout per spoke:
#   {
#     id: 'xxx',                      <- LINE A
#     type: '...',
#     iconKey: '...',
#     colorTheme: '...',
#     slug: { ... },
#     content: makeStubContent({       <- LINE B (open)
#       h1: '...',
#       ...
#       galleryImages: [
#         '...',
#       ],
#     }),                              <- LINE C (close)
#   },

id_line_re = re.compile(r"^    id: '([^']+)',\s*$")
open_re = re.compile(r"^    content: makeStubContent\(\{\s*$")
close_re = re.compile(r"^    \}\),\s*$")

spokes = []  # list of (id, line_open_idx, line_close_idx)
n = len(lines)
i = 0
while i < n:
    m = id_line_re.match(lines[i])
    if m:
        spoke_id = m.group(1)
        # find next `    content: makeStubContent({`
        j = i + 1
        while j < n and not open_re.match(lines[j]):
            j += 1
        if j == n:
            raise SystemExit(f"No content open after id={spoke_id} (line {i+1})")
        # find next `    }),` after open
        k = j + 1
        while k < n and not close_re.match(lines[k]):
            k += 1
        if k == n:
            raise SystemExit(f"No content close after id={spoke_id} (line {j+1})")
        spokes.append((spoke_id, j, k))
        i = k + 1
    else:
        i += 1

print(f"Found {len(spokes)} spokes")

# Sanity: there should be no duplicate ids
ids = [s[0] for s in spokes]
assert len(ids) == len(set(ids)), f"Duplicate ids: {[x for x in ids if ids.count(x) > 1]}"

# Build the ES content map
es_entries = []
for spoke_id, open_idx, close_idx in spokes:
    # The object literal is between open_idx (`    content: makeStubContent({`)
    # and close_idx (`    }),`). The actual object is `{ ... }`.
    # Lines we want: from `      h1: '...',` through `    },` (the inner closing).
    # We'll reconstruct the object literal as `{` + body + `}` indented at 2 spaces (for the Record value).
    body_lines = lines[open_idx + 1 : close_idx]
    # Each body line is currently indented at 6 spaces (for the inner properties).
    # In the new file they should sit inside `'id': { ... }` at object-literal indent.
    # We keep their original indent for minimum diff/risk.
    body = "\n".join(body_lines)
    es_entries.append(f"  '{spoke_id}': {{\n{body}\n  }},")

es_text = (
    "// AUTO-GENERATED via scripts/refactor_use_cases.py\n"
    "// Do not edit by hand unless you understand the structure.\n"
    "// This file holds Spanish content for all use-case spokes.\n"
    "// English content lives in use-cases-content.en.ts.\n"
    "\n"
    "import type { UseCaseContent } from './use-cases';\n"
    "\n"
    "export const USE_CASES_CONTENT_ES: Record<string, UseCaseContent> = {\n"
    + "\n".join(es_entries)
    + "\n};\n"
)

OUT_ES.write_text(es_text)
print(f"Wrote {OUT_ES} ({len(es_text)} chars, {len(spokes)} entries)")

# Build the EN content map (empty initially — translations populate it spoke by spoke)
en_text = (
    "// English content for use-case spokes.\n"
    "// Each entry mirrors the structure of USE_CASES_CONTENT_ES.\n"
    "// Missing entries fall back to ES at runtime via makeContent() in use-cases.ts.\n"
    "\n"
    "import type { UseCaseContent } from './use-cases';\n"
    "\n"
    "export const USE_CASES_CONTENT_EN: Partial<Record<string, UseCaseContent>> = {\n"
    "  // Populate spoke by spoke as translations land.\n"
    "};\n"
)
OUT_EN.write_text(en_text)
print(f"Wrote {OUT_EN}")

# Now rewrite use-cases.ts:
# - Replace `function makeStubContent` block with `function makeContent` that imports both maps.
# - Replace each `content: makeStubContent({...})` block with `content: makeContent('id'),`.

# Find the makeStubContent helper
stub_start_re = re.compile(r"^const STUB_LANGS:")
stub_end_re = re.compile(r"^\}\s*$")
stub_start = None
for idx, ln in enumerate(lines):
    if stub_start_re.match(ln):
        stub_start = idx
        break
if stub_start is None:
    raise SystemExit("Could not find STUB_LANGS line")
# Find closing `}` of makeStubContent function
stub_end = None
for idx in range(stub_start + 1, len(lines)):
    if stub_end_re.match(lines[idx]):
        # check that this is the function's closing brace (next non-empty line should be `export const USE_CASES`)
        # for safety we find the SECOND `}` after 'function makeStubContent' is detected
        if "function makeStubContent" in "\n".join(lines[stub_start:idx + 1]):
            stub_end = idx
            break
if stub_end is None:
    raise SystemExit("Could not find end of makeStubContent function")

new_helper = """const STUB_LANGS: LangCode[] = ['en', 'fr', 'de', 'it', 'pt', 'nl'];

import { USE_CASES_CONTENT_ES } from './use-cases-content.es';
import { USE_CASES_CONTENT_EN } from './use-cases-content.en';

function makeContent(id: string): Record<LangCode, UseCaseContent> {
  const es = USE_CASES_CONTENT_ES[id];
  if (!es) {
    throw new Error(`Missing ES content for use-case id: ${id}`);
  }
  const en = USE_CASES_CONTENT_EN[id] ?? es;
  const out: Record<LangCode, UseCaseContent> = {
    es,
    en,
    fr: es,
    de: es,
    it: es,
    pt: es,
    nl: es,
  };
  return out;
}"""

# Build new lines: keep [0:stub_start], replace [stub_start:stub_end+1], append rest.
# But we also need to replace each spoke's content block. Easier approach: build a new
# output line-by-line, using the spoke ranges to skip + emit a single replacement line.

# Build set of (open_idx, close_idx) per spoke
spoke_ranges = {(o, c): sid for sid, o, c in spokes}
# index by open
spoke_by_open = {o: (sid, c) for sid, o, c in spokes}

out_lines = []
i = 0
n = len(lines)
while i < n:
    if i == stub_start:
        out_lines.append(new_helper)
        i = stub_end + 1
        continue
    if i in spoke_by_open:
        sid, close_idx = spoke_by_open[i]
        out_lines.append(f"    content: makeContent('{sid}'),")
        i = close_idx + 1
        continue
    out_lines.append(lines[i])
    i += 1

new_text = "\n".join(out_lines)
OUT_TS.write_text(new_text)
print(f"Wrote {OUT_TS} ({len(new_text)} chars)")

# Quick sanity: number of `content: makeContent(` should equal len(spokes)
assert new_text.count("content: makeContent(") == len(spokes), \
    f"Expected {len(spokes)} makeContent calls, got {new_text.count('content: makeContent(')}"

print("Refactor done.")
