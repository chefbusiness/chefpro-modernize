#!/usr/bin/env python3
"""
Batch generator for Consultoría Gastro Pro images via Gemini Nano Banana 2.

Generates 69 images (60 gallery + 11 OG, minus 2 pilots already done):
- 5 more gallery imgs for consultor-gastronomico
- 6 gallery imgs for 9 remaining consultores = 54
- 10 OG social imgs for spokes (1200x630)

Strategy: pairs of parallel HTTP requests (avoid rate limits).
Each image: API call -> /tmp/ PNG -> sips JPG to destination -> clean.
"""

import base64
import json
import subprocess
import os
import time
from concurrent.futures import ThreadPoolExecutor, as_completed

API_KEY = os.environ.get("GEMINI_API_KEY") or os.environ.get("GOOGLE_API_KEY")
if not API_KEY:
    raise SystemExit(
        "Set GEMINI_API_KEY env var before running. "
        "Get one at https://aistudio.google.com/apikey — do NOT hardcode it here."
    )
ENDPOINT = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-3.1-flash-image-preview:generateContent?key={API_KEY}"

PROJECT_ROOT = "/Users/johnguerrero/chefpro-modernize"
GALLERY_DIR = f"{PROJECT_ROOT}/public/lovable-uploads/ai-gallery"
OG_DIR = f"{PROJECT_ROOT}/public/og/use-cases"
TMP_DIR = "/tmp"

STYLE_BASE = (
    "Cinematic editorial photograph, horizontal 16:9, hyperrealistic, 35mm film grain, "
    "natural window light + warm pendant lamps, professional contemporary mood, warm and approachable. "
    "Brass, walnut, cream, muted gold materials. Shallow depth of field, slight softness in background. "
    "No text overlays. No visible logos. Real candid working moment, not posed. "
    "High-end hospitality consultancy context."
)

# Per-consultor identity (gender, age, look) for testimonial coherence
CONSULTORES = {
    "consultor-gastronomico": {
        "person": "a senior Spanish gastronomic consultant (45-year-old man, smart casual blazer no tie, eyeglasses, salt-and-pepper hair)",
        "setting": "a contemporary restaurant open kitchen / consultancy office",
        "tool": "tablet with financial dashboards",
        "action_label": "dashboard",
        "action": "presenting financial dashboards on a sleek tablet, charts visible on screen",
    },
    "chef-consultor": {
        "person": "a senior consultant chef (42-year-old Spanish man wearing a chef coat with discreet stripes, technical confident expression)",
        "setting": "a high-end Michelin-style open kitchen",
        "tool": "recipe folder and ingredient samples",
        "action_label": "emplatado",
        "action": "plating an haute cuisine signature dish with tweezers, focused gesture",
    },
    "heladero-consultor": {
        "person": "a master gelato consultant (38-year-old Italian woman in a clean artisan apron, brown hair tied back, attentive precise gestures)",
        "setting": "a contemporary artisan gelato lab",
        "tool": "thermometer, scale, gelato recipe sheets",
        "action_label": "mantecadora",
        "action": "operating a polished stainless-steel mantecadora gelato machine, fresh gelato batch visible",
    },
    "chocolatero-consultor": {
        "person": "a master chocolatier consultant (44-year-old Catalan woman in spotless chocolatier coat, focused expression, precise hand gestures)",
        "setting": "a premium chocolate workshop with tempering machine",
        "tool": "couverture samples and recipe sheets",
        "action_label": "temperado",
        "action": "tempering chocolate on a marble slab, glossy chocolate flowing under controlled hand",
    },
    "pastelero-consultor": {
        "person": "a pastry consultant chef (40-year-old woman, pastry chef coat with clean apron, focused calm gesture)",
        "setting": "a professional pastry obrador with stainless steel surfaces",
        "tool": "piping bag and decoration tools",
        "action_label": "decoracion",
        "action": "decorating an elegant entremet cake with precise piping technique",
    },
    "pizzero-consultor": {
        "person": "a Neapolitan pizzaiolo consultant (50-year-old Italian man with traditional white apron, focused serious expression, hands floured)",
        "setting": "an authentic Neapolitan pizzeria with wood-fired oven glowing in background",
        "tool": "marble counter with dough balls",
        "action_label": "horno",
        "action": "sliding a freshly stretched pizza into a wood-fired oven with a long peel, flames visible",
    },
    "barista-consultor": {
        "person": "a specialty coffee barista consultant (33-year-old Danish woman, modern apron, eyeglasses, focused expression)",
        "setting": "a sleek specialty coffee shop with espresso machine",
        "tool": "espresso machine and pour-over kit",
        "action_label": "extraccion",
        "action": "calibrating an espresso shot, golden crema flowing from a portafilter spout, precision moment",
    },
    "sommelier-consultor": {
        "person": "a senior sommelier consultant (42-year-old Spanish woman wearing elegant dark sommelier attire, focused tasting expression)",
        "setting": "an elegant wine cellar with rows of bottles",
        "tool": "Riedel wine glass and tasting notes",
        "action_label": "cata",
        "action": "evaluating a glass of red wine against natural light, swirling glass in hand, focused tasting",
    },
    "bartender-consultor": {
        "person": "a senior bartender consultant (38-year-old man with dark apron, slight tattoos on forearms, confident expression)",
        "setting": "a premium signature cocktail bar",
        "tool": "shaker, jigger, premium spirits",
        "action_label": "coctel",
        "action": "finishing a signature cocktail with smoking garnish, attention to craft detail",
    },
    "panadero-consultor": {
        "person": "a senior Spanish baker consultant (55-year-old man with baker apron, floured hands, experienced expression)",
        "setting": "a traditional craft bakery obrador with steam oven in background",
        "tool": "dough, scoring lame, scale",
        "action_label": "fermentacion",
        "action": "scoring a freshly proofed sourdough loaf with a lame, fermentation jars visible on shelf",
    },
}

# Action 5 label per consultor (matches paths cabled in use-cases-content.es.consultor.ts)
# Variants needed: hero, fichas, cliente|reunion, equipo, ACTION (above), presentacion
# Exceptions: consultor-gastronomico uses "reunion" + "dashboard" (action) instead of cliente
#             chef-consultor uses "reunion" + "emplatado" (action)
VARIANTS = {
    "consultor-gastronomico": ["hero", "fichas", "reunion", "equipo", "dashboard", "presentacion"],
    "chef-consultor":        ["hero", "fichas", "reunion", "equipo", "emplatado",   "presentacion"],
    "heladero-consultor":    ["hero", "fichas", "cliente", "equipo", "mantecadora", "presentacion"],
    "chocolatero-consultor": ["hero", "fichas", "cliente", "equipo", "temperado",   "presentacion"],
    "pastelero-consultor":   ["hero", "fichas", "cliente", "equipo", "decoracion",  "presentacion"],
    "pizzero-consultor":     ["hero", "fichas", "cliente", "equipo", "horno",       "presentacion"],
    "barista-consultor":     ["hero", "fichas", "cliente", "equipo", "extraccion",  "presentacion"],
    "sommelier-consultor":   ["hero", "fichas", "cliente", "equipo", "cata",        "presentacion"],
    "bartender-consultor":   ["hero", "fichas", "cliente", "equipo", "coctel",      "presentacion"],
    "panadero-consultor":    ["hero", "fichas", "cliente", "equipo", "fermentacion","presentacion"],
}


def build_prompt(slug, variant):
    c = CONSULTORES[slug]
    if variant == "hero":
        scene = f"{c['person']} standing confidently in {c['setting']}, reviewing professional notes or {c['tool']}, clear protagonist in sharp focus"
    elif variant == "fichas":
        scene = f"overhead or side view of the hands of {c['person']} writing technical specs and pricing on a clipboard or tablet in {c['setting']}, {c['tool']} visible, careful focused gesture"
    elif variant in ("cliente", "reunion"):
        scene = f"{c['person']} sitting across a young client (junior chef or restaurant owner) reviewing documents or tablet together in {c['setting']}, both engaged, candid consulting moment"
    elif variant == "equipo":
        scene = f"{c['person']} teaching and directing a small team (3-5 people) in {c['setting']}, demonstrating a technique with hands or pointing, didactic moment of staff training"
    elif variant == "presentacion":
        scene = f"professional meeting: {c['person']} presenting a project dashboard or proposal on a tablet to a client and an investor across a polished wooden table in a modern boardroom or open kitchen, blueprints and reports visible"
    else:
        # the unique action variant — uses CONSULTORES[slug]['action']
        scene = f"close action shot of {c['person']} {c['action']}, technical authority moment, in {c['setting']}"
    return f"{scene}. {STYLE_BASE}"


def build_og_prompt(slug):
    """Wide social-share variant of the hero (1200x630 aspect)."""
    c = CONSULTORES[slug]
    scene = (
        f"Editorial wide social-share composition (1200x630). {c['person']} in {c['setting']}, "
        f"holding a tablet showing a project dashboard or {c['tool']} on the table. "
        f"Subject placed off-center to leave breathing room on one side. Confident professional pose."
    )
    return f"{scene}. {STYLE_BASE}"


def api_generate(prompt, out_png):
    body = json.dumps({
        "contents": [{"parts": [{"text": prompt}]}],
        "generationConfig": {"responseModalities": ["IMAGE"]},
    })
    try:
        result = subprocess.run(
            ["curl", "-s", "--max-time", "120", "-X", "POST", ENDPOINT,
             "-H", "Content-Type: application/json", "-d", body],
            capture_output=True, text=True, timeout=140,
        )
    except subprocess.TimeoutExpired:
        return "NETWORK_ERROR: curl timeout"
    if result.returncode != 0:
        return f"NETWORK_ERROR: curl rc={result.returncode} {result.stderr[:200]}"
    try:
        data = json.loads(result.stdout)
    except json.JSONDecodeError as e:
        return f"PARSE_ERROR: {e} body={result.stdout[:200]}"
    if "error" in data:
        return f"API_ERROR: {data['error'].get('message', 'unknown')[:200]}"
    parts = data.get("candidates", [{}])[0].get("content", {}).get("parts", [])
    if not parts:
        return "BLOCKED_OR_EMPTY"
    for p in parts:
        if "inlineData" in p:
            with open(out_png, "wb") as f:
                f.write(base64.b64decode(p["inlineData"]["data"]))
            return "OK"
    return "NO_IMAGE_DATA"


def optimize_to_jpg(src_png, out_jpg, resize_args=None):
    cmd = ["sips"]
    if resize_args:
        cmd.extend(resize_args)
    cmd.extend([src_png, "-s", "format", "jpeg", "-s", "formatOptions", "75", "--out", out_jpg])
    result = subprocess.run(cmd, capture_output=True, text=True)
    return result.returncode == 0


def process_image(task):
    """task = {slug, variant, kind: 'gallery'|'og', out_path}"""
    slug = task["slug"]
    variant = task["variant"]
    kind = task["kind"]
    out_path = task["out_path"]

    if os.path.exists(out_path):
        return f"SKIP (exists): {out_path}"

    prompt = task["prompt"]
    tmp_png = f"{TMP_DIR}/{slug}-{variant}-raw.png"

    # Generate
    status = api_generate(prompt, tmp_png)
    if status != "OK":
        return f"FAIL [{slug}/{variant}]: {status}"

    # Optimize
    if kind == "og":
        resize_args = ["-z", "630", "1200"]
    else:
        resize_args = ["--resampleWidth", "1200"]
    if not optimize_to_jpg(tmp_png, out_path, resize_args):
        return f"FAIL OPTIMIZE [{slug}/{variant}]"

    # Clean
    try:
        os.remove(tmp_png)
    except OSError:
        pass

    sz = os.path.getsize(out_path)
    return f"OK [{slug}/{variant}/{kind}]: {sz//1024}KB"


def build_tasks():
    tasks = []

    # Gallery for each consultor
    for slug, variants in VARIANTS.items():
        for variant in variants:
            out_path = f"{GALLERY_DIR}/consultor-{slug.replace('-consultor', '').replace('consultor-', '')}-{variant}.jpg"
            # IMPORTANT: code paths use different prefixes per consultor (see use-cases-content.es.consultor.ts)
            # Re-map to actual file names:
            #   consultor-gastronomico-* -> consultor-gastronomico-*
            #   chef-consultor          -> consultor-chef-*
            #   heladero-consultor      -> consultor-heladero-*
            #   etc.
            stem_map = {
                "consultor-gastronomico": "consultor-gastronomico",
                "chef-consultor":        "consultor-chef",
                "heladero-consultor":    "consultor-heladero",
                "chocolatero-consultor": "consultor-chocolatero",
                "pastelero-consultor":   "consultor-pastelero",
                "pizzero-consultor":     "consultor-pizzero",
                "barista-consultor":     "consultor-barista",
                "sommelier-consultor":   "consultor-sommelier",
                "bartender-consultor":   "consultor-bartender",
                "panadero-consultor":    "consultor-panadero",
            }
            stem = stem_map[slug]
            out_path = f"{GALLERY_DIR}/{stem}-{variant}.jpg"
            tasks.append({
                "slug": slug,
                "variant": variant,
                "kind": "gallery",
                "out_path": out_path,
                "prompt": build_prompt(slug, variant),
            })

    # OG social per spoke
    for slug in VARIANTS.keys():
        og_filename = slug + ".jpg"
        out_path = f"{OG_DIR}/{og_filename}"
        tasks.append({
            "slug": slug,
            "variant": "og",
            "kind": "og",
            "out_path": out_path,
            "prompt": build_og_prompt(slug),
        })

    return tasks


def main():
    tasks = build_tasks()
    pending = [t for t in tasks if not os.path.exists(t["out_path"])]
    print(f"Total target images: {len(tasks)}")
    print(f"Already exist:       {len(tasks) - len(pending)}")
    print(f"To generate:         {len(pending)}")
    print()

    successes = []
    failures = []

    # Pairs of parallel requests
    BATCH_SIZE = 2
    for i in range(0, len(pending), BATCH_SIZE):
        batch = pending[i:i + BATCH_SIZE]
        with ThreadPoolExecutor(max_workers=BATCH_SIZE) as ex:
            futures = {ex.submit(process_image, t): t for t in batch}
            for fut in as_completed(futures):
                result = fut.result()
                print(result, flush=True)
                if result.startswith("OK"):
                    successes.append(result)
                elif result.startswith("SKIP"):
                    pass
                else:
                    failures.append((futures[fut], result))

        # Small pause between pairs to avoid rate limits
        time.sleep(1.5)

    print()
    print(f"Done. Successes: {len(successes)}  Failures: {len(failures)}")
    if failures:
        print("Failed tasks:")
        for t, msg in failures:
            print(f"  - {t['slug']}/{t['variant']}: {msg}")


if __name__ == "__main__":
    main()
