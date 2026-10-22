#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tanda 1 del glosario: fichas nuevas en 7 idiomas y parche de quick wins ES.

No es un ensamblador para volver a correr sobre lo publicado: escribe los .md
nuevos una vez. Si el fichero ya existe, no lo pisa (salvo --force).

No inventa cifras. Las proporciones clásicas (partes iguales de harina y grasa)
son la definición del gesto, no una medición de laboratorio.
"""
from __future__ import annotations

import html
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
BLOG = REPO / "astro-site/src/content/blog"
LANGS = ["es", "en", "fr", "de", "it", "pt", "nl"]

CAT = {
    "es": "glosario",
    "en": "glossary",
    "fr": "glossaire",
    "de": "glossar",
    "it": "glossario",
    "pt": "glossario",
    "nl": "glossarium",
}
CHEF = {
    "es": "https://aichef.pro/usos/rol/chef-jefe-cocina",
    "en": "https://aichef.pro/en/use-cases/role/head-chef",
    "fr": "https://aichef.pro/fr/cas-d-usage/role/chef-cuisinier",
    "de": "https://aichef.pro/de/anwendungsfaelle/rolle/kuechenchef",
    "it": "https://aichef.pro/it/casi-uso/ruolo/capo-cuoco",
    "pt": "https://aichef.pro/pt/casos-uso/funcao/chefe-cozinha",
    "nl": "https://aichef.pro/nl/use-cases/rol/chef-kok",
}
CALC = {
    "es": "https://aichef.pro/calculadora-food-cost-restaurante",
    "en": "https://aichef.pro/en/food-cost-calculator-restaurant",
    "fr": "https://aichef.pro/fr/calculateur-food-cost-restaurant",
    "de": "https://aichef.pro/de/food-cost-rechner-restaurant",
    "it": "https://aichef.pro/it/calcolatore-food-cost-ristorante",
    "pt": "https://aichef.pro/pt/calculadora-food-cost-restaurante",
    "nl": "https://aichef.pro/nl/food-cost-calculator-restaurant",
}
GLOSS = {
    "es": "https://aichef.pro/blog/categoria/glosario",
    "en": "https://aichef.pro/en/blog/category/glossary",
    "fr": "https://aichef.pro/fr/blog/categorie/glossaire",
    "de": "https://aichef.pro/de/blog/kategorie/glossar",
    "it": "https://aichef.pro/it/blog/categoria/glossario",
    "pt": "https://aichef.pro/pt/blog/categoria/glossario",
    "nl": "https://aichef.pro/nl/blog/categorie/glossarium",
}
GUEST = {
    "es": "https://app.aichef.pro/invitado",
    "en": "https://enapp.aichef.pro/guest",
    "fr": "https://frapp.aichef.pro/guest",
    "de": "https://deapp.aichef.pro/guest",
    "it": "https://itapp.aichef.pro/ospite",
    "pt": "https://ptapp.aichef.pro/guest",
    "nl": "https://nlapp.aichef.pro/guest",
}
IMG = {
    "roux": ("/blog-assets/2026/05/roux-destacada.jpg", "/blog-assets/2026/05/bechamel-cuerpo.jpg", "/blog-assets/2026/05/veloute-cuerpo.jpg"),
    "napar": ("/blog-assets/2026/05/veloute-destacada.jpg", "/blog-assets/2026/05/demi-glace-cuerpo.jpg", "/blog-assets/2026/05/espanola-cuerpo.jpg"),
    "montar": ("/blog-assets/2026/05/holandesa-destacada.jpg", "/blog-assets/2026/05/holandesa-cuerpo.jpg", "/blog-assets/2026/05/bearnesa-cuerpo.jpg"),
    "blanc": ("/blog-assets/2026/05/bearnesa-destacada.jpg", "/blog-assets/2026/05/vinagreta-cuerpo.jpg", "/blog-assets/2026/05/mayonesa-cuerpo.jpg"),
    "gastrique": ("/blog-assets/2026/05/pillar-salsas-destacada.jpg", "/blog-assets/2026/05/pillar-salsas-cuerpo.jpg", "/blog-assets/2026/05/umami-cuerpo.jpg"),
    "yema": ("/blog-assets/2026/05/bechamel-destacada.jpg", "/blog-assets/2026/05/fond-cuerpo.jpg", "/blog-assets/2026/05/fondo-blanco-cuerpo.jpg"),
    "glace": ("/blog-assets/2026/05/demi-glace-destacada.jpg", "/blog-assets/2026/05/fondo-oscuro-cuerpo.jpg", "/blog-assets/2026/05/maillard-cuerpo.jpg"),
    "fumet": ("/blog-assets/2026/05/fondo-blanco-destacada.jpg", "/blog-assets/2026/05/veloute-cuerpo.jpg", "/blog-assets/2026/05/fond-cuerpo.jpg"),
    "papilla": ("/blog-assets/2026/05/espanola-destacada.jpg", "/blog-assets/2026/05/roux-cuerpo.jpg", "/blog-assets/2026/05/bechamel-cuerpo.jpg"),
    "rouxpage": ("/blog-assets/2026/05/roux-destacada.jpg", "/blog-assets/2026/05/roux-cuerpo.jpg", "/blog-assets/2026/05/espanola-cuerpo.jpg"),
    "emulsion": ("/blog-assets/2026/03/emulsion-featured.jpg", "/blog-assets/2026/05/mayonesa-cuerpo.jpg", "/blog-assets/2026/05/holandesa-cuerpo.jpg"),
    "demi": ("/blog-assets/2026/05/demi-glace-destacada.jpg", "/blog-assets/2026/05/demi-glace-cuerpo.jpg", "/blog-assets/2026/05/fondo-oscuro-cuerpo.jpg"),
}

# Comprueba que la destacada no se repite en el cuerpo.
for k, (a, b, c) in IMG.items():
    if a in (b, c) or b == c:
        raise SystemExit(f"imagen repetida en {k}")

UI = {
    "es": {
        "chef_k": "Agentes de IA para la partida",
        "chef_p": "Esta técnica se trabaja con los agentes de IA de cocina, desde la ficha web de chef jefe de cocina. No abre un agente concreto de la app.",
        "chef_a": "Ver la ficha de chef jefe de cocina",
        "calc_k": "Calcula el coste de la salsa",
        "calc_p": "Un fondo o una reducción se comen el margen si no los escandallas. La calculadora de food cost está en la web, sin salir del glosario hacia un agente de la app.",
        "calc_a": "Abrir la calculadora de food cost",
        "guest_k": "Prueba los agentes de IA",
        "guest_p": "Entra como invitado y pregunta por esta técnica. La puerta es la de invitado, no la ficha de un agente.",
        "guest_a": "Entrar como invitado",
        "h_que": "Qué es, en la práctica",
        "h_tabla": "Con qué no se confunde",
        "h_partida": "Cómo se comporta en el pase",
        "h_busca": "Cómo se escribe y cómo se busca",
        "rel": "Sigue en el glosario",
        "th": ("Gesto", "Qué hace", "Qué no hace"),
    },
    "en": {
        "chef_k": "AI agents for the pass",
        "chef_p": "Work this technique with the culinary AI agents from the head chef page on the site. It does not open one agent inside the app.",
        "chef_a": "Open the head chef page",
        "calc_k": "Cost the sauce",
        "calc_p": "A stock or a reduction eats the margin if you never cost it. The food cost calculator lives on the site.",
        "calc_a": "Open the food cost calculator",
        "guest_k": "Try the AI agents",
        "guest_p": "Come in as a guest and ask about this technique. The door is the guest home, not a single agent.",
        "guest_a": "Enter as a guest",
        "h_que": "What it is, on the line",
        "h_tabla": "What it is not",
        "h_partida": "How it behaves on the pass",
        "h_busca": "How people search for it",
        "rel": "More from the glossary",
        "th": ("Gesture", "What it does", "What it does not do"),
    },
    "fr": {
        "chef_k": "Agents IA pour le passe",
        "chef_p": "Cette technique se travaille avec les agents IA culinaires, depuis la fiche web du chef cuisinier. Elle n'ouvre pas un agent précis dans l'app.",
        "chef_a": "Voir la fiche du chef cuisinier",
        "calc_k": "Calculez le coût de la sauce",
        "calc_p": "Un fond ou une réduction mange la marge si personne ne le chiffre. Le calculateur de food cost est sur le site.",
        "calc_a": "Ouvrir le calculateur de food cost",
        "guest_k": "Essayez les agents IA",
        "guest_p": "Entrez en invité et posez la question sur cette technique. La porte est l'accueil invité, pas la fiche d'un agent.",
        "guest_a": "Entrer en invité",
        "h_que": "Ce que c'est, en service",
        "h_tabla": "Avec quoi on ne confond pas",
        "h_partida": "Comment ça se tient au passe",
        "h_busca": "Comment on l'écrit et comment on le cherche",
        "rel": "Suite du glossaire",
        "th": ("Geste", "Ce qu'il fait", "Ce qu'il ne fait pas"),
    },
    "de": {
        "chef_k": "KI-Agenten für die Ausgabe",
        "chef_p": "Diese Technik arbeiten Sie mit den kulinarischen KI-Agenten, von der Webseite des Küchenchefs aus. Sie öffnet keinen einzelnen Agenten in der App.",
        "chef_a": "Zur Seite des Küchenchefs",
        "calc_k": "Was die Sauce kostet",
        "calc_p": "Ein Fond oder eine Reduktion frisst die Marge, wenn niemand sie kalkuliert. Der Food-Cost-Rechner liegt auf der Website.",
        "calc_a": "Food-Cost-Rechner öffnen",
        "guest_k": "KI-Agenten ausprobieren",
        "guest_p": "Kommen Sie als Gast herein und fragen Sie nach dieser Technik. Die Tür ist die Gast-Startseite, nicht ein einzelner Agent.",
        "guest_a": "Als Gast eintreten",
        "h_que": "Was es in der Küche ist",
        "h_tabla": "Womit man es nicht verwechselt",
        "h_partida": "Wie es sich an der Ausgabe verhält",
        "h_busca": "Wie man es schreibt und sucht",
        "rel": "Weiter im Glossar",
        "th": ("Geste", "Was sie tut", "Was sie nicht tut"),
    },
    "it": {
        "chef_k": "Agenti IA per il passe",
        "chef_p": "Questa tecnica si lavora con gli agenti IA di cucina, dalla scheda web del capo cuoco. Non apre un agente preciso nell'app.",
        "chef_a": "Apri la scheda del capo cuoco",
        "calc_k": "Calcola il costo della salsa",
        "calc_p": "Un fondo o una riduzione si mangia il margine se nessuno lo costa. Il calcolatore di food cost è sul sito.",
        "calc_a": "Apri il calcolatore di food cost",
        "guest_k": "Prova gli agenti IA",
        "guest_p": "Entra come ospite e chiedi di questa tecnica. La porta è la home ospite, non la scheda di un agente.",
        "guest_a": "Entra come ospite",
        "h_que": "Che cos'è, in servizio",
        "h_tabla": "Con che cosa non si confonde",
        "h_partida": "Come si comporta al passe",
        "h_busca": "Come si scrive e come si cerca",
        "rel": "Continua nel glossario",
        "th": ("Gesto", "Che cosa fa", "Che cosa non fa"),
    },
    "pt": {
        "chef_k": "Agentes de IA para o passe",
        "chef_p": "Esta técnica trabalha-se com os agentes de IA de cozinha, a partir da ficha web do chefe de cozinha. Não abre um agente concreto na app.",
        "chef_a": "Ver a ficha do chefe de cozinha",
        "calc_k": "Calcule o custo do molho",
        "calc_p": "Um fundo ou uma redução come a margem se ninguém o custear. A calculadora de food cost está no site.",
        "calc_a": "Abrir a calculadora de food cost",
        "guest_k": "Experimente os agentes de IA",
        "guest_p": "Entre como convidado e pergunte por esta técnica. A porta é a de convidado, não a ficha de um agente.",
        "guest_a": "Entrar como convidado",
        "h_que": "O que é, no serviço",
        "h_tabla": "Com o que não se confunde",
        "h_partida": "Como se comporta no passe",
        "h_busca": "Como se escreve e como se procura",
        "rel": "Segue no glossário",
        "th": ("Gesto", "O que faz", "O que não faz"),
    },
    "nl": {
        "chef_k": "AI-agents voor de passe",
        "chef_p": "Deze techniek werkt u met de culinaire AI-agents, vanaf de webpagina van de chef-kok. U opent geen losse agent in de app.",
        "chef_a": "Naar de pagina van de chef-kok",
        "calc_k": "Wat de saus kost",
        "calc_p": "Een fond of een reductie eet de marge op als niemand hem doorrekent. De food-costcalculator staat op de site.",
        "calc_a": "Food-costcalculator openen",
        "guest_k": "Probeer de AI-agents",
        "guest_p": "Kom binnen als gast en vraag naar deze techniek. De deur is de gaststart, niet de pagina van één agent.",
        "guest_a": "Als gast naar binnen",
        "h_que": "Wat het in de keuken is",
        "h_tabla": "Waarmee u het niet verwart",
        "h_partida": "Hoe het zich op de passe gedraagt",
        "h_busca": "Hoe u het schrijft en zoekt",
        "rel": "Verder in het glossarium",
        "th": ("Gebaar", "Wat het doet", "Wat het niet doet"),
    },
}


def words(s: str) -> int:
    plain = re.sub(r"<[^>]+>", " ", s)
    plain = html.unescape(plain)
    return len(re.findall(r"\S+", plain))


def lead_words(s: str) -> int:
    return len(re.findall(r"\S+", s))


def yq(s: str) -> str:
    return '"' + s.replace("\\", "\\\\").replace('"', '\\"') + '"'


def cta(lang: str, kind: str, slug: str) -> str:
    ui = UI[lang]
    if kind == "calc":
        href, k, p, a = CALC[lang], ui["calc_k"], ui["calc_p"], ui["calc_a"]
    else:
        href, k, p, a = CHEF[lang], ui["chef_k"], ui["chef_p"], ui["chef_a"]
    return (
        '<aside class="not-prose my-8 rounded-xl border border-primary/20 bg-primary/5 p-6">'
        f'<p class="text-sm font-semibold uppercase tracking-wide text-primary">{html.escape(k)}</p>'
        f'<p class="mt-2 text-foreground">{html.escape(p)}</p>'
        f'<p class="mt-4"><a class="inline-block rounded-lg bg-primary px-5 py-2.5 font-semibold text-primary-foreground" '
        f'href="{href}?utm_source=web&amp;utm_medium=glosario&amp;utm_content={slug}">{html.escape(a)}</a></p>'
        "</aside>"
    )


def cta_guest(lang: str, slug: str) -> str:
    ui = UI[lang]
    href = (
        f"{GUEST[lang]}?utm_source=web&amp;utm_medium=glosario&amp;utm_content={slug}"
    )
    return (
        '<aside class="not-prose my-8 rounded-xl border border-primary/20 bg-primary/5 p-6">'
        f'<p class="text-sm font-semibold uppercase tracking-wide text-primary">{html.escape(ui["guest_k"])}</p>'
        f'<p class="mt-2 text-foreground">{html.escape(ui["guest_p"])}</p>'
        f'<p class="mt-4"><a class="inline-block rounded-lg bg-primary px-5 py-2.5 font-semibold text-primary-foreground" '
        f'href="{href}">{html.escape(ui["guest_a"])}</a></p>'
        "</aside>"
    )


def figura(src: str, alt: str) -> str:
    return (
        f'<figure><img src="{src}" alt="{html.escape(alt)}" loading="lazy" '
        'style="width:100%;height:auto;border-radius:8px;margin:24px 0;" /></figure>'
    )


def tabla(lang: str, rows: list[tuple[str, str, str]]) -> str:
    th = UI[lang]["th"]
    head = "".join(f"<th>{html.escape(x)}</th>" for x in th)
    body = ""
    for a, b, c in rows:
        body += "<tr>" + "".join(f"<td>{html.escape(x)}</td>" for x in (a, b, c)) + "</tr>"
    return (
        '<div class="table-scroll"><table><thead><tr>'
        + head
        + "</tr></thead><tbody>"
        + body
        + "</tbody></table></div>"
    )


def post_url(lang: str, slug: str) -> str:
    if lang == "es":
        return f"https://aichef.pro/blog/{slug}"
    return f"https://aichef.pro/{lang}/blog/{slug}"


def render(term: dict, lang: str, siblings: dict[str, str]) -> str:
    ui = UI[lang]
    c = term["copy"][lang]
    slug = term["slugs"][lang]
    feat, b1, b2 = IMG[term["img"]]
    alt_f = c["alt"][0]
    p_html = [f"<p>{html.escape(p)}</p>" for p in c["paras"]]
    if len(p_html) < 4:
        raise SystemExit(f"{term['id']} {lang}: faltan párrafos")
    head = "\n".join(p_html[:2])
    tail = "\n".join(p_html[2:])
    links = []
    for sid, label in c["links"]:
        href = siblings.get(sid) or sid
        if href.startswith("http"):
            links.append(f'<li><a href="{href}">{html.escape(label)}</a></li>')
        else:
            links.append(f'<li><a href="{post_url(lang, href)}">{html.escape(label)}</a></li>')
    links.append(f'<li><a href="{GLOSS[lang]}">{html.escape(ui["rel"])}</a></li>')
    body = "\n".join([
        f"<p>{html.escape(c['lead'])}</p>",
        cta(lang, term["cta"], slug),
        f"<h2>{html.escape(ui['h_que'])}</h2>",
        head,
        f"<h2>{html.escape(ui['h_tabla'])}</h2>",
        tabla(lang, c["rows"]),
        figura(b1, c["alt"][1]),
        f"<h2>{html.escape(ui['h_partida'])}</h2>",
        tail,
        figura(b2, c["alt"][2]),
        f"<h2>{html.escape(ui['h_busca'])}</h2>",
        f"<p>{html.escape(c['busca'])}</p>",
        "<ul>",
        *links,
        "</ul>",
        cta_guest(lang, slug),
    ])
    nlead = lead_words(c["lead"])
    nbody = words(body)
    if not (40 <= nlead <= 60):
        raise SystemExit(f"{term['id']} {lang}: lead {nlead} palabras")
    if nbody < 450:
        raise SystemExit(f"{term['id']} {lang}: cuerpo {nbody} palabras")
    if re.search(r"[\u4e00-\u9fff\u3040-\u30ff\u0400-\u04ff\uac00-\ud7af]", body + c["title"] + c["description"]):
        raise SystemExit(f"{term['id']} {lang}: caracteres no latinos")
    trans = "\n".join(f"  {l}: {yq(term['slugs'][l])}" for l in LANGS)
    faq = "\n".join(
        f"  - q: {yq(q)}\n    a: {yq(a)}" for q, a in c["faq"]
    )
    fm = (
        "---\n"
        f"title: {yq(c['title'])}\n"
        f"description: {yq(c['description'])}\n"
        "pubDate: 2026-10-22\n"
        "modDate: 2026-10-22\n"
        f"category: {CAT[lang]}\n"
        f"tags: {c['tags']}\n"
        f"lang: {lang}\n"
        f"image: {feat}\n"
        f"imageAlt: {yq(alt_f)}\n"
        "translations:\n"
        f"{trans}\n"
        "definedTerm:\n"
        f"  name: {yq(c['term'])}\n"
        f"  description: {yq(c['lead'])}\n"
        "faq:\n"
        f"{faq}\n"
        "---\n"
    )
    return fm + "\n" + body + "\n"


# El copiado de fichas vive en glosario_tanda1_copy.py para no mezclar el motor
# con el texto. Se importa al final.
def update_llms(terms: list[dict]) -> None:
    """Añade los hubs del glosario y la tanda 1 a llms.txt y llms-full.txt."""
    hubs = " · ".join(
        f"[{lang.upper()}]({GLOSS[lang]})" for lang in LANGS
    )
    lines = [
        "<!-- GLOSARIO-TANDA1-START -->",
        "## Culinary glossary (7 languages)",
        "",
        "The hospitality glossary is no longer Spanish-only. Each language has its own category, native slugs and hreflang across es, en, fr, de, it, pt and nl. Definitions are written for cooks and operators. AI agents are the product positioning: calls to action go to the role page, the food cost calculator or the guest home of the app, never to a single agent URL.",
        "",
        f"Glossary hubs: {hubs}.",
        "",
        "Batch 1, sauces, emulsions and stocks:",
        "",
    ]
    for term in terms:
        bits = []
        for lang in LANGS:
            bits.append(f"[{lang}]({post_url(lang, term['slugs'][lang])})")
        lines.append(f"- {term['copy']['en']['term']}: " + " ".join(bits))
    lines += [
        "",
        "Spanish Search Console pages updated in the same batch: [homogeneización](https://aichef.pro/blog/homogeneizacion-concepto-definicion), [abocar y abocado](https://aichef.pro/blog/que-significa-abocar-en-cocina), [hidrólisis](https://aichef.pro/blog/hidrolisis-concepto-definicion), [maceración](https://aichef.pro/blog/maceracion-concepto-definicion), [reacción de Maillard](https://aichef.pro/blog/reaccion-de-maillard). The old slug maillard-concepto-y-definicion-2 redirects to the Maillard URL.",
        "<!-- GLOSARIO-TANDA1-END -->",
        "",
    ]
    block = "\n".join(lines)
    for path in (
        REPO / "astro-site/public/llms.txt",
        REPO / "astro-site/public/llms-full.txt",
        REPO / "public/llms.txt",
        REPO / "public/llms-full.txt",
    ):
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8")
        text = text.replace(
            "The glossary is currently in Spanish.",
            "The glossary now has a native category in all seven languages.",
        )
        text = text.replace(
            "Spanish only for now.",
            "Native categories now exist in all seven languages.",
        )
        if "<!-- GLOSARIO-TANDA1-START -->" in text:
            text = re.sub(
                r"<!-- GLOSARIO-TANDA1-START -->.*?<!-- GLOSARIO-TANDA1-END -->\n?",
                block,
                text,
                count=1,
                flags=re.S,
            )
        else:
            if not text.endswith("\n"):
                text += "\n"
            text += "\n" + block
        path.write_text(text, encoding="utf-8")
        print(f"llms {path.relative_to(REPO)}")


def main():
    from glosario_tanda1_copy import TERMS  # noqa: WPS433

    siblings = {}
    for term in TERMS:
        for lang, slug in term["slugs"].items():
            siblings[f"{term['id']}:{lang}"] = slug
    # enlaces internos: cada ficha referencia ids de otras fichas del clúster
    written = 0
    for term in TERMS:
        for lang in LANGS:
            slug = term["slugs"][lang]
            dest = BLOG / lang / f"{slug}.md"
            if term.get("skip_es") and lang == "es":
                if term.get("attach_es") and dest.exists():
                    patch_translations(dest, term)
                continue
            if dest.exists() and "--force" not in sys.argv and not term.get("overwrite"):
                continue
            # Mapa de id -> slug en este idioma, para los enlaces del copy.
            local = {t["id"]: t["slugs"][lang] for t in TERMS}
            text = render(term, lang, local)
            dest.parent.mkdir(parents=True, exist_ok=True)
            dest.write_text(text, encoding="utf-8")
            written += 1
            print(f"ok {lang}/{slug} palabras={words(text)}")
    print(f"escritos={written}")
    update_llms(TERMS)


def patch_translations(path: Path, term: dict):
    text = path.read_text(encoding="utf-8")
    if text.startswith("---") and "\ntranslations:" in text.split("---", 2)[1]:
        return
    block = "translations:\n" + "\n".join(
        f"  {l}: {yq(term['slugs'][l])}" for l in LANGS
    ) + "\n"
    # Inserta antes de faq: o antes del cierre del frontmatter.
    parts = text.split("---", 2)
    if len(parts) < 3:
        raise SystemExit(f"sin frontmatter {path}")
    fm = parts[1]
    if "\ndefinedTerm:" not in fm and term["copy"]["es"].get("lead"):
        block += (
            "definedTerm:\n"
            f"  name: {yq(term['copy']['es']['term'])}\n"
            f"  description: {yq(term['copy']['es']['lead'])}\n"
        )
    if "\nfaq:" in fm:
        fm = fm.replace("\nfaq:", "\n" + block + "faq:", 1)
    else:
        fm = fm.rstrip() + "\n" + block
    path.write_text("---" + fm + "---" + parts[2], encoding="utf-8")
    print(f"hreflang {path.name}")


if __name__ == "__main__":
    main()
