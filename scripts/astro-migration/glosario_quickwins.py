#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Parche quirúrgico de los quick wins ES. No reconstruye el cuerpo.

Añade la definición de 40–60 palabras, el title y la meta, DefinedTerm,
FAQPage (moviendo la FAQ visible al frontmatter cuando ya estaba en el cuerpo),
variantes de grafía, dos CTA y el 301 de Maillard.
"""
from __future__ import annotations

import html
import re
from pathlib import Path

from copy_es import COPY
from glosario_tanda1 import cta, cta_guest, lead_words, yq

REPO = Path(__file__).resolve().parents[2]
BLOG = REPO / "astro-site/src/content/blog"
REDIRECTS = REPO / "astro-site/public/_redirects"
OLD_MAILLARD = "maillard-concepto-y-definicion-2"
NEW_MAILLARD = "reaccion-de-maillard"


def words(s: str) -> int:
    return lead_words(s)


# Leads escritos aquí (roux, emulsión y demi salen de copy_es para no duplicar).
LEADS = {
    "homogeneizacion-concepto-definicion": (
        "La homogeneización reduce el tamaño de las partículas de una mezcla para que no se separen. "
        "Emulsionar dispersa dos líquidos que no se llevan; homogeneizar afina esa dispersión hasta dejarla estable. "
        "En la cocina explica la leche que no forma nata, una salsa que se mantiene y una vinagreta que no se corta en el pase."
    ),
    "que-significa-abocar-en-cocina": (
        "Abocar es verter un líquido acercando la boca de un recipiente a la del otro, para pasarlo limpio y dejar el poso. "
        "No es decantar un vino de guarda ni colar con un chino. Abocado, con o, es otra cosa: un vino de dulzor moderado, "
        "o quien está destinado a un desenlace. La grafía de cocina lleva b."
    ),
    "hidrolisis-concepto-definicion": (
        "La hidrólisis es la reacción en la que el agua rompe una molécula grande en trozos más pequeños. "
        "En la cocina aparece al madurar una carne, al afinar un queso o al cocer un fondo hasta que el colágeno se vuelve gelatina. "
        "No es la reacción de Maillard, que necesita una superficie seca y un calor que el agua impide."
    ),
    "maceracion-concepto-definicion": (
        "La maceración extrae sabor de un sólido dejado en un líquido o con azúcar, sin la cocción que se llevaría los aromas. "
        "Una fruta con azúcar, una piel en alcohol o una especia en almíbar son maceraciones. "
        "Un marinado ácido de carne es un pariente de otro uso, no el mismo gesto ni el mismo trabajo de partida."
    ),
    "reaccion-de-maillard": (
        "La reacción de Maillard dora y da aroma a tostado cuando aminoácidos y azúcares se encuentran en una superficie seca y caliente. "
        "El agua lo frena, porque esa superficie no pasa del hervor. No es la caramelización, que solo necesita azúcar. "
        "En el pase es la costra de la carne, la corteza del pan y el tueste del café."
    ),
}

META = {
    "homogeneizacion-concepto-definicion": {
        "title": "Homogeneización: qué es y por qué la mezcla no se separa",
        "description": "La homogeneización reduce las partículas de una mezcla para que no se separe. Qué la diferencia de emulsionar, en la leche, las salsas y el pase.",
        "term": "Homogeneización",
        "cta": "chef",
        "busca": (
            "Quien busca homogeneización también teclea homogeneizacion, sin tilde, y a veces homogenización, que no es la grafía correcta. "
            "El proceso es el mismo que se explica aquí: reducir el tamaño de las partículas para que la mezcla no se separe. "
            "No es un sinónimo de emulsión. La emulsión es el sistema de dos líquidos; la homogeneización es el trabajo mecánico que lo afina."
        ),
        "links": [
            ("https://aichef.pro/blog/emulsion-concepto-definicion", "Qué es una emulsión"),
            ("https://aichef.pro/blog/mayonesa-concepto-y-definicion", "La mayonesa"),
        ],
    },
    "que-significa-abocar-en-cocina": {
        "title": "Abocar y abocado: qué significan en cocina y en el vino",
        "description": "Abocar es verter un líquido boca a boca y dejar el poso. Abocado es un vino de dulzor moderado, o estar destinado a algo. Con b, no avocar.",
        "term": "Abocar",
        "cta": "chef",
        "busca": (
            "Las búsquedas mezclan abocar, abocado, abocada y la falta avocar. En cocina el verbo es abocar, con b, de boca. "
            "Avocar es un término jurídico y aquí no significa nada. Abocado, con o, nombra un vino con dulzor moderado y también la expresión estar abocado a un desenlace. "
            "No son el gesto de trasiego."
        ),
        "links": [
            ("https://aichef.pro/blog/maceracion-concepto-definicion", "Qué es la maceración"),
            ("https://aichef.pro/blog/fondo-oscuro-concepto-y-definicion", "El fondo oscuro"),
        ],
    },
    "hidrolisis-concepto-definicion": {
        "title": "Hidrólisis: qué es cuando el agua rompe el alimento",
        "description": "La hidrólisis es la ruptura de una molécula por el agua. Así maduran la carne y el queso, y el colágeno de un fondo acaba en gelatina. No es Maillard.",
        "term": "Hidrólisis",
        "cta": "chef",
        "busca": (
            "Se busca hidrólisis e hidrolisis, sin tilde. Las dos escrituras quieren esta reacción: el agua rompe una molécula grande. "
            "No es la reacción de Maillard ni una caramelización. En la partida se reconoce al madurar, al fermentar o al convertir colágeno en gelatina, sin necesidad de un número que esta ficha no va a inventar."
        ),
        "links": [
            ("https://aichef.pro/blog/reaccion-de-maillard", "La reacción de Maillard"),
            ("https://aichef.pro/blog/maceracion-concepto-definicion", "Qué es la maceración"),
        ],
    },
    "maceracion-concepto-definicion": {
        "title": "Maceración: qué es y en qué no es un marinado",
        "description": "La maceración extrae sabor de un sólido en un líquido o con azúcar, sin cocerlo. No es lo mismo que un marinado ácido de carne ni que infusionar a fuego.",
        "term": "Maceración",
        "cta": "chef",
        "busca": (
            "Se busca maceración, maceracion sin tilde, y macerar. No es lo mismo que marinar, aunque el buscador los junte. "
            "Macerar, en esta ficha, es dejar un sólido en líquido o con azúcar para extraer sabor sin cocción. "
            "Marinar una carne con ácido y grasa es otro gesto, con otro riesgo y otro tiempo de cámara."
        ),
        "links": [
            ("https://aichef.pro/blog/que-significa-abocar-en-cocina", "Qué significa abocar"),
            ("https://aichef.pro/blog/hidrolisis-concepto-definicion", "Qué es la hidrólisis"),
        ],
    },
    "reaccion-de-maillard": {
        "title": "Reacción de Maillard: qué es y en qué no es caramelizar",
        "description": "La reacción de Maillard dora y aromatiza aminoácidos y azúcares en seco. El agua la frena. No es la caramelización, que solo necesita azúcar.",
        "term": "Reacción de Maillard",
        "cta": "chef",
        "busca": (
            "Se busca reacción de Maillard, reaccion de maillard sin tildes, y a secas Maillard. "
            "El slug duplicado, el que llevaba un -2 al final, redirige a esta ficha. "
            "No es la caramelización: esa solo afecta a los azúcares. Maillard necesita también aminoácidos, y una superficie que no esté mojada."
        ),
        "links": [
            ("https://aichef.pro/blog/hidrolisis-concepto-definicion", "Qué es la hidrólisis"),
            ("https://aichef.pro/blog/umami-concepto-y-definicion", "Qué es el umami"),
        ],
    },
    "roux-concepto-y-definicion": {"from_copy": "roux", "cta": "calc"},
    "demi-glace-concepto-y-definicion": {"from_copy": "demi", "cta": "calc"},
    "emulsion-concepto-definicion": {"from_copy": "emulsion", "cta": "chef"},
}

COPY_BUSCA = {
    "roux": (
        "Se busca roux, rue por error, roux blanco, roux rubio y roux oscuro. En alemán el gesto se llama Mehlschwitze. "
        "No es un beurre manié: esa pasta va cruda y al final. Tampoco es una papilla de almidón. "
        "La proporción de la que habla la partida es partes iguales en peso, cocidas antes de mojar."
    ),
    "demi": (
        "Se busca demi-glace, demi glace, demiglace, demi glacé y salsa demi-glace. Son la misma salsa. "
        "No es la glace de viande, que lleva el fondo más lejos y puede no llevar harina. "
        "Si el bote no dice de qué está hecho, el nombre no basta para fiarse."
    ),
    "emulsion": (
        "Se busca emulsión, emulsion con una sola ese, emulsionar y salsa emulsionada. "
        "No es ligar con fécula. Mayonesa, holandesa y vinagreta son emulsiones, y no aguantan el mismo tiempo ni el mismo calor."
    ),
}
COPY_LINKS = {
    "roux": [
        ("https://aichef.pro/blog/beurre-manie", "Qué es el beurre manié"),
        ("https://aichef.pro/blog/ligar-con-maicena", "Ligar con maicena"),
        ("https://aichef.pro/blog/demi-glace-concepto-y-definicion", "Qué es la demi-glace"),
    ],
    "demi": [
        ("https://aichef.pro/blog/glace-de-viande", "Qué es la glace de viande"),
        ("https://aichef.pro/blog/napar-una-salsa", "Qué es napar"),
        ("https://aichef.pro/blog/roux-concepto-y-definicion", "Qué es el roux"),
    ],
    "emulsion": [
        ("https://aichef.pro/blog/beurre-blanc", "Qué es el beurre blanc"),
        ("https://aichef.pro/blog/ligado-con-yema", "El ligado con yema"),
        ("https://aichef.pro/blog/mayonesa-concepto-y-definicion", "La mayonesa"),
    ],
}


def resolve(slug: str) -> dict:
    raw = META[slug]
    if "from_copy" not in raw:
        out = dict(raw)
        out["lead"] = LEADS[slug]
        return out
    src = COPY[raw["from_copy"]]
    return {
        "title": src["title"],
        "description": src["description"],
        "term": src["term"],
        "lead": src["lead"],
        "cta": raw["cta"],
        "busca": COPY_BUSCA[raw["from_copy"]],
        "links": COPY_LINKS[raw["from_copy"]],
        "faq_fallback": src["faq"],
    }


def plain(s: str) -> str:
    s = re.sub(r"<[^>]+>", " ", s)
    s = html.unescape(s)
    return re.sub(r"\s+", " ", s).strip()


def extract_faq(body: str):
    m = re.search(
        r"<h2[^>]*>\s*Preguntas [Ff]recuentes\s*</h2>(.*?)(?=<h2\b|<aside\b|<div style=|<p>\s*<script|$)",
        body,
        re.S,
    )
    if not m:
        return None, body
    block = m.group(1)
    pairs = re.findall(r"<h3>\s*(¿.*?)\s*</h3>\s*<p>(.*?)</p>", block, re.S)
    if len(pairs) < 3:
        pairs = re.findall(
            r"<p>\s*<strong>\s*(¿.*?)\s*</strong>\s*<br\s*/?>\s*(.*?)</p>",
            block,
            re.S,
        )
    if len(pairs) < 3:
        return None, body
    faq = [(plain(q), plain(a)) for q, a in pairs]
    body = body[: m.start()] + body[m.end() :]
    return faq, body


def strip_jsonld(body: str) -> str:
    return re.sub(
        r"\n?<p>\s*<script type=\"application/ld\+json\">.*?</script>\s*</p>",
        "",
        body,
        flags=re.S,
    )


def upsert_block(fm: str, key: str, block: str) -> str:
    pattern = re.compile(rf"\n{key}:.*?(?=\n[A-Za-z][\w]*:|\Z)", re.S)
    if pattern.search("\n" + fm):
        fm = pattern.sub("\n" + block.rstrip("\n"), "\n" + fm, count=1)
        return fm[1:] if fm.startswith("\n") else fm
    return fm.rstrip() + "\n" + block


def set_scalar(fm: str, key: str, value: str) -> str:
    line = f"{key}: {yq(value)}"
    if re.search(rf"^{key}:.*$", fm, re.M):
        return re.sub(rf"^{key}:.*$", line, fm, count=1, flags=re.M)
    return fm.rstrip() + "\n" + line + "\n"


def faq_block(pairs: list[tuple[str, str]]) -> str:
    rows = [f"  - q: {yq(q)}\n    a: {yq(a)}" for q, a in pairs]
    return "faq:\n" + "\n".join(rows) + "\n"


def defined_block(name: str, description: str) -> str:
    return f"definedTerm:\n  name: {yq(name)}\n  description: {yq(description)}\n"


def busca_html(slug: str, meta: dict) -> str:
    lis = "\n".join(
        f'<li><a href="{href}">{html.escape(label)}</a></li>' for href, label in meta["links"]
    )
    return (
        f'\n<h2 data-glosario-busca="1">Cómo se escribe y cómo se busca</h2>\n'
        f"<p>{html.escape(meta['busca'])}</p>\n<ul>\n{lis}\n</ul>\n"
        + cta_guest("es", slug)
    )


def patch_file(src: Path, slug: str) -> str:
    meta = resolve(slug)
    n = words(meta["lead"])
    if not (40 <= n <= 60):
        raise SystemExit(f"{slug}: lead {n}")
    text = src.read_text(encoding="utf-8")
    if not text.startswith("---"):
        raise SystemExit(f"sin frontmatter {src}")
    _, fm, body = text.split("---", 2)
    body = strip_jsonld(body)
    extracted, body = extract_faq(body)
    if extracted:
        pairs = extracted
    elif "\nfaq:" in fm:
        pairs = None  # se conserva el bloque
    else:
        pairs = meta.get("faq_fallback")
        if not pairs:
            raise SystemExit(f"{slug}: sin FAQ")
    fm = set_scalar(fm, "title", meta["title"])
    fm = set_scalar(fm, "description", meta["description"])
    if re.search(r"^modDate:.*$", fm, re.M):
        fm = re.sub(r"^modDate:.*$", "modDate: 2026-10-22", fm, count=1, flags=re.M)
    else:
        fm = fm.rstrip() + "\nmodDate: 2026-10-22\n"
    fm = upsert_block(fm, "definedTerm", defined_block(meta["term"], meta["lead"]))
    if pairs is not None and "\nfaq:" not in fm.split("definedTerm:")[0]:
        # Si ya había faq antes del definedTerm, upsert lo sustituye igual.
        fm = upsert_block(fm, "faq", faq_block(pairs))
    elif pairs is not None:
        fm = upsert_block(fm, "faq", faq_block(pairs))
    if 'data-glosario-lead="1"' not in body:
        opener = (
            f'\n<p data-glosario-lead="1">{html.escape(meta["lead"])}</p>\n'
            + cta("es", meta["cta"], slug)
            + "\n"
        )
        body = opener + body.lstrip("\n")
    if 'data-glosario-busca="1"' not in body:
        body = body.rstrip() + "\n" + busca_html(slug, meta)
    # El enlace viejo de abocar abría la app en la raíz, no la puerta de invitado.
    body = body.replace(
        "https://app.aichef.pro/?utm_source=blog&utm_medium=body&utm_content=abocar",
        "https://app.aichef.pro/invitado?utm_source=web&utm_medium=glosario&utm_content=que-significa-abocar-en-cocina",
    )
    body = body.replace("más de 70 agentes", "los agentes de IA")
    return f"---{fm}---{body if body.startswith(chr(10)) else chr(10)+body}"


def rewrite_maillard_links(text: str) -> str:
    return text.replace(OLD_MAILLARD, NEW_MAILLARD)


def redirects() -> None:
    block = (
        "\n# Glosario tanda 1 (2026-10-22): el slug duplicado de Maillard\n"
        "# va al canónico. La regla del apex cubre el enlace interno viejo;\n"
        "# la del subdominio va antes de la genérica blog.aichef.pro/:slug.\n"
        f"/blog/{OLD_MAILLARD}   /blog/{NEW_MAILLARD}   301\n"
        f"/blog/{OLD_MAILLARD}/  /blog/{NEW_MAILLARD}   301\n"
    )
    sub = (
        f"https://blog.aichef.pro/{OLD_MAILLARD} https://aichef.pro/blog/{NEW_MAILLARD} 301!\n"
        f"https://blog.aichef.pro/{OLD_MAILLARD}/ https://aichef.pro/blog/{NEW_MAILLARD} 301!\n"
    )
    text = REDIRECTS.read_text(encoding="utf-8")
    if f"/blog/{OLD_MAILLARD}" not in text:
        text = block + text
    marker = "https://blog.aichef.pro/:slug https://aichef.pro/blog/:slug 301!"
    if f"https://blog.aichef.pro/{OLD_MAILLARD} " not in text:
        if marker not in text:
            raise SystemExit("no está la genérica del blog")
        text = text.replace(marker, sub + marker, 1)
    REDIRECTS.write_text(text, encoding="utf-8")
    print("redirects ok")


def main() -> None:
    # Maillard se lee del slug viejo y se escribe en el canónico.
    src_maillard = BLOG / "es" / f"{OLD_MAILLARD}.md"
    if src_maillard.exists():
        text = patch_file(src_maillard, NEW_MAILLARD)
        text = rewrite_maillard_links(text)
        dest = BLOG / "es" / f"{NEW_MAILLARD}.md"
        dest.write_text(text, encoding="utf-8")
        src_maillard.unlink()
        print(f"renombrado {NEW_MAILLARD}")
    elif not (BLOG / "es" / f"{NEW_MAILLARD}.md").exists():
        raise SystemExit("no está el post de Maillard")

    for path in BLOG.rglob("*.md"):
        raw = path.read_text(encoding="utf-8")
        if OLD_MAILLARD in raw:
            path.write_text(rewrite_maillard_links(raw), encoding="utf-8")
            print(f"enlace {path.relative_to(BLOG)}")

    for slug in META:
        if slug == NEW_MAILLARD:
            continue
        path = BLOG / "es" / f"{slug}.md"
        if not path.exists():
            raise SystemExit(f"falta {path}")
        path.write_text(patch_file(path, slug), encoding="utf-8")
        print(f"parche {slug}")

    # El canónico ya se escribió; si el bucle no lo cubre en una segunda pasada
    # de lead, no pasa nada: el marcador evita duplicar.
    redirects()
    hrefs = REPO / "scripts/astro-migration/fase8b-fix-hrefs-malformados.py"
    h = hrefs.read_text(encoding="utf-8")
    h2 = h.replace(
        "'maillard': '/blog/maillard-concepto-y-definicion-2'",
        "'maillard': '/blog/reaccion-de-maillard'",
    )
    if h2 != h:
        hrefs.write_text(h2, encoding="utf-8")
        print("mapa de hrefs")


if __name__ == "__main__":
    main()
