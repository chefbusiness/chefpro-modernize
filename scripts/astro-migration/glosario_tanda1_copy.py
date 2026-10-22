#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Términos de la tanda 1: slugs nativos y el copy de cada idioma."""
from copy_de import COPY as DE
from copy_en import COPY as EN
from copy_es import COPY as ES
from copy_fr import COPY as FR
from copy_it import COPY as IT
from copy_nl import COPY as NL
from copy_pt import COPY as PT

LANGS = ["es", "en", "fr", "de", "it", "pt", "nl"]
BY_LANG = {"es": ES, "en": EN, "fr": FR, "de": DE, "it": IT, "pt": PT, "nl": NL}

SLUGS = {
    "manie": {
        "es": "beurre-manie",
        "en": "beurre-manie",
        "fr": "beurre-manie",
        "de": "mehlbutter",
        "it": "beurre-manie",
        "pt": "beurre-manie",
        "nl": "beurre-manie",
    },
    "napar": {
        "es": "napar-una-salsa",
        "en": "nap-a-sauce",
        "fr": "napper-une-sauce",
        "de": "nappieren",
        "it": "salsa-nappante",
        "pt": "napar-um-molho",
        "nl": "saus-napperen",
    },
    "montar": {
        "es": "montar-al-burro",
        "en": "monter-au-beurre",
        "fr": "monter-au-beurre",
        "de": "sauce-mit-butter-montieren",
        "it": "mantecare",
        "pt": "montar-na-manteiga",
        "nl": "saus-monteren-met-boter",
    },
    "blanc": {
        "es": "beurre-blanc",
        "en": "beurre-blanc",
        "fr": "beurre-blanc",
        "de": "beurre-blanc",
        "it": "burro-bianco",
        "pt": "beurre-blanc",
        "nl": "beurre-blanc",
    },
    "gastrique": {
        "es": "gastrique",
        "en": "gastrique",
        "fr": "gastrique",
        "de": "gastrique",
        "it": "gastrique",
        "pt": "gastrique",
        "nl": "gastrique",
    },
    "yema": {
        "es": "ligado-con-yema",
        "en": "egg-yolk-liaison",
        "fr": "liaison-au-jaune",
        "de": "legierung-mit-eigelb",
        "it": "legante-al-tuorlo",
        "pt": "ligacao-com-gema",
        "nl": "liaison-met-eigeel",
    },
    "glace": {
        "es": "glace-de-viande",
        "en": "glace-de-viande",
        "fr": "glace-de-viande",
        "de": "fleischglace",
        "it": "glace-de-viande",
        "pt": "glace-de-viande",
        "nl": "vleesglace",
    },
    "fumet": {
        "es": "fumet-de-pescado",
        "en": "fish-fumet",
        "fr": "fumet-de-poisson",
        "de": "fischfond-fumet",
        "it": "fumetto",
        "pt": "fumet-de-peixe",
        "nl": "visfumet",
    },
    "papilla": {
        "es": "papilla-de-almidon",
        "en": "starch-slurry",
        "fr": "liaison-a-la-fecule",
        "de": "staerkebrei",
        "it": "sospensione-di-amido",
        "pt": "papas-de-amido",
        "nl": "zetmeelpap",
    },
    "roux": {
        "es": "roux-concepto-y-definicion",
        "en": "what-is-a-roux",
        "fr": "qu-est-ce-qu-un-roux",
        "de": "mehlschwitze",
        "it": "roux",
        "pt": "o-que-e-um-roux",
        "nl": "wat-is-een-roux",
    },
    "emulsion": {
        "es": "emulsion-concepto-definicion",
        "en": "what-is-an-emulsion",
        "fr": "emulsion-culinaire",
        "de": "emulsion-kueche",
        "it": "emulsione",
        "pt": "emulsao",
        "nl": "emulsie",
    },
    "demi": {
        "es": "demi-glace-concepto-y-definicion",
        "en": "what-is-demi-glace",
        "fr": "demi-glace",
        "de": "demi-glace",
        "it": "demi-glace",
        "pt": "demi-glace",
        "nl": "demi-glace",
    },
}

# img: clave de glosario_tanda1.IMG. cta: chef | calc.
# Roux, emulsión y demi-glace ya están publicados en español: no se regeneran.
META = [
    ("manie", "roux", "chef", False),
    ("napar", "napar", "chef", False),
    ("montar", "montar", "chef", False),
    ("blanc", "blanc", "chef", False),
    ("gastrique", "gastrique", "chef", False),
    ("yema", "yema", "chef", False),
    ("glace", "glace", "calc", False),
    ("fumet", "fumet", "calc", False),
    ("papilla", "papilla", "chef", False),
    ("roux", "rouxpage", "calc", True),
    ("emulsion", "emulsion", "chef", True),
    ("demi", "demi", "calc", True),
]

TERMS = []
for tid, img, cta, existente_es in META:
    TERMS.append({
        "id": tid,
        "img": img,
        "cta": cta,
        "slugs": SLUGS[tid],
        "copy": {lang: BY_LANG[lang][tid] for lang in LANGS},
        "skip_es": existente_es,
        "attach_es": existente_es,
    })
