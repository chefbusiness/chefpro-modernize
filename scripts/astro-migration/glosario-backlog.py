#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Backlog maestro del glosario gastronómico, organizado por agente.

Lee el catálogo del sitio (scripts/astro-migration/fase8c-agentes/catalogo-hub.json)
y cruza cada término semilla con los posts ya publicados (categoría glosario en
español y slugs de cualquier idioma). No inventa volúmenes de búsqueda.

Salida:
  GLOSARIO_BACKLOG.json
  GLOSARIO_BACKLOG.md
"""
from __future__ import annotations

import json
import re
import unicodedata
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
CATALOGO = REPO / "scripts/astro-migration/fase8c-agentes/catalogo-hub.json"
BLOG = REPO / "astro-site/src/content/blog"
OUT_JSON = REPO / "GLOSARIO_BACKLOG.json"
OUT_MD = REPO / "GLOSARIO_BACKLOG.md"

# Términos que esta tanda publica o reescribe. El estado «publicado» sale del
# cruce con los ficheros; esta lista solo documenta la tanda en el encabezado.
TANDA_1 = [
    "homogeneización",
    "abocar / abocado",
    "hidrólisis",
    "maceración",
    "roux / Mehlschwitze",
    "demi-glace",
    "reacción de Maillard",
    "beurre manié",
    "napar / nappé",
    "montar al burro",
    "beurre blanc",
    "gastrique",
    "ligado con yema",
    "glace de viande",
    "fumet",
    "papilla de almidón",
    "emulsión",
]


def norm(s: str) -> str:
    s = s.lower().strip()
    s = unicodedata.normalize("NFD", s)
    s = "".join(c for c in s if unicodedata.category(c) != "Mn")
    s = s.replace("ß", "ss")
    s = re.sub(r"[^a-z0-9]+", " ", s)
    return re.sub(r"\s+", " ", s).strip()


def cargar_publicados():
    """slug normalizado y título normalizado de cada post de glosario ES,
    más todos los slugs del blog (cualquier idioma)."""
    glosario = []
    slugs = []
    for md in BLOG.glob("*/*.md"):
        text = md.read_text(encoding="utf-8")
        slug = md.stem
        slugs.append(norm(slug.replace("-", " ")))
        if md.parent.name != "es":
            continue
        if not re.search(r"^category:\s*glosario\s*$", text, re.M):
            continue
        m = re.search(r'^title:\s*"(.*)"\s*$', text, re.M)
        title = m.group(1) if m else slug
        glosario.append((norm(slug.replace("-", " ")), norm(title), f"es/{slug}"))
    return glosario, slugs


def publicado(termino: str, glosario, slugs) -> str | None:
    n = norm(termino)
    if len(n) < 4:
        # Términos cortos (roux, fond, jus): solo coincidencia de token en el slug.
        token = rf"(^| ){re.escape(n)}( |$)"
        for slug_n, _title, ref in glosario:
            if re.search(token, slug_n):
                return ref
        return None
    for slug_n, title, ref in glosario:
        if n in slug_n or n in title:
            return ref
        # el slug es la forma corta del término («demi glace» dentro de «demi glace concepto»)
        if slug_n.startswith(n + " ") or slug_n == n:
            return ref
    return None


OFICIO = [
    "mise en place", "ficha técnica", "escandallo", "merma", "rendimiento",
    "alérgeno", "lote", "trazabilidad", "abatido", "regeneración",
    "servicio", "pase", "comanda", "briefing de cocina", "partida",
]

COCINA = OFICIO + [
    "roux", "beurre manié", "napar", "montar al burro", "beurre blanc",
    "demi-glace", "glace de viande", "fumet", "fondo oscuro", "fondo blanco",
    "emulsión", "ligado con yema", "gastrique", "deglasar", "reducción",
    "reacción de Maillard", "caramelización", "hidrólisis", "maceración",
    "salmuera", "confitar", "brasear", "escalfar", "sofrito", "mirepoix",
    "bouquet garni", "court-bouillon", "concassé", "brunoise", "juliana",
    "papilla de almidón", "beurre monté", "velouté", "bechamel", "holandesa",
    "vinagreta", "mayonesa", "homogeneización", "esferificación", "gelificación",
]

PASTELERIA = OFICIO + [
    "merengue", "pata de gato", "pâte à bombe", "cremeux", "ganache",
    "praliné", "feuilletage", "detrempe", "touraje", "puff pastry",
    "bizcocho", "genovesa", "joconde", "dacquoise", "sablée",
    "crema pastelera", "crema diplomática", "mousseline", "chantilly",
    "baumé", "punto de bola", "punto de hebra", "invertir azúcar",
    "gelatina", "pectina", "agar", "isomalt", "cacao en manteca",
    "atemperado", "cristalización", "actividad de agua", "baño maría",
    "manga", "cornet", "glaseado espejo", "coulis", "compota",
    "fermentación de masa", "masa madre dulce", "streusel",
]

CHOCOLATE = OFICIO + [
    "atemperado", "curva de temperado", "cristal V", "manteca de cacao",
    "cobertura", "porcentaje de cacao", "ganache", "praliné", "gianduja",
    "tableta", "bonbón", "corteza", "molde de policarbonato", "desmoldeo",
    "bloom de grasa", "bloom de azúcar", "viscosidad", "fluidez",
    "conchado", "refinado", "nibs", "licor de cacao", "cacao en polvo",
    "emulsión de ganache", "lecitina", "vainilla", "inclusión",
    "chocolate ruby", "origen único", "bean to bar", "tueste de cacao",
    "acidez del cacao", "astringencia", "shelf life", "actividad de agua",
    "envasado", "temperatura de obrador", "humedad relativa",
]

HELADO = OFICIO + [
    "mix de helado", "sólidos totales", "sólidos lácteos", "grasa láctea",
    "poder anticongelante", "PAC", "POD", "overrun", "mantecatura",
    "maduración del mix", "homogeneización", "pasteurización del mix",
    "estabilizante", "emulsionante", "neutro", "sacarosa", "dextrosa",
    "azúcar invertido", "maltodextrina", "fibra", "proteína láctea",
    "sorbete", "sherbet", "granizado", "semifrío", "parfait",
    "vitrina de helado", "cadena de frío", "choque térmico", "recristalización",
    "sabor a recalentado", "balance dulzor", "cata de helado", "curva de servicio",
    "vaso", "cucurucho", "topping", "variegato", "ripple",
]

PAN = OFICIO + [
    "masa madre", "prefermento", "poolish", "biga", "esponja",
    "autólisis", "hidratación", "amasado", "desarrollo del gluten",
    "ventana de gluten", "pliegue", "fermentación en bloque", "puntado",
    "formado", "banneton", "greñado", "vapor de horno", "resorte de horno",
    "miga", "cortezas", "gelatinización del almidón", "reacción de Maillard",
    "harina de fuerza", "cenizas", "W del alveograma", "P/L",
    "centeno", "integral", "masa vieja", "retardo en frío",
    "biga líquida", "levadura", "sal en masa", "división",
    "fermentar en frío", "horno de solera", "caída", "sobre fermentación",
]

FERMENT = OFICIO + [
    "fermentación láctica", "fermentación alcohólica", "fermentación acética",
    "koji", "miso", "garum", "shoyu", "kombucha", "kéfir", "kvass",
    "chucrut", "kimchi", "encurtido", "salmuera", "actividad de agua",
    "pH", "cultivo iniciador", "inoculación", "anaerobiosis", "aerobiosis",
    "moho noble", "levadura salvaje", "bacterias lácticas", "SCOBY",
    "hidrólisis", "proteólisis", "umami", "glutamato", "histamina",
    "seguridad fermentada", "botulismo en anaerobiosis", "pasteurizar fermento",
    "backslopping", "madre", "temperatura de cámara", "tiempo de cura",
    "salazón", "deshidratación", "aminoácidos libres",
]

VEG = OFICIO + [
    "proteína vegetal", "legumbre", "seitán", "tofu", "tempeh",
    "jackfruit", "seta", "umami vegetal", "kombu", "miso",
    "aquafaba", "emulsión sin huevo", "lecitina de soja", "metilcelulosa",
    "gelificación vegetal", "almidón", "fibra", "texturizado de guisante",
    "caldo vegetal", "fondo vegetal", "sofrito", "parrilla de verdura",
    "marcado", "glaseado de verdura", "puré", "aceite de hierbas",
    "fermentado vegetal", "queso vegetal", "nata vegetal", "mantequilla vegetal",
    "alérgeno de fruto seco", "alérgeno de soja", "alérgeno de gluten",
    "carta plant-based", "coste de proteína vegetal", "sustituto de huevo",
    "agar", "pectina", "goma xantana",
]

PAIRING = OFICIO + [
    "food pairing", "compuesto aromático", "puente de sabor", "contraste",
    "afinidad", "maridaje", "umami", "acidez", "grasa", "dulzor",
    "amargor", "sal", "textura", "temperatura de servicio", "vino",
    "cerveza", "sake", "té", "cóctel", "destilado",
    "tanino", "cuerpo", "persistencia", "retrogusto", "equilibrio",
    "salsa como puente", "reducción", "ácido", "graso sobre amargo",
    "queso y vino", "postre y vino dulce", "picante y dulce",
    "fermentado y láctico", "ahumado", "yodo", "hierba", "especiado",
    "carta de maridajes", "precio de copa", "margen de bodega",
]

LEX = COCINA[:40] + [
    "definición operativa", "sinónimo de oficio", "falso amigo",
    "término de sala", "término de obrador", "unidad", "proceso", "aditivo",
]

CONSULT = OFICIO + [
    "food cost", "ingeniería de menú", "margen de contribución", "precio de venta",
    "ticket medio", "rotación de mesa", "prime cost", "coste de personal",
    "escandallo", "merma teórica", "merma real", "inventario",
    "ficha técnica", "alergenos en carta", "APPCC", "proveedor",
    "estacionalidad", "carta ingeniería", "plato estrella", "plato perro",
    "plato puzzle", "plato vaca", "umbral de rentabilidad", "punto muerto",
    "horas de cocina", "productividad", "estándar de receta", "porcionado",
    "compra", "recepción de género", "FIFO", "mermas de preparación",
    "coste de salsa", "rendimiento de despiece", "canal", "delivery",
]

HOTEL = [
    "room service", "banquete", "BEO", "coffee break", "buffet",
    "mise en place de banquet", "recalentado de buffet", "cadena de calor",
    "cadena de frío", "minibar", "amenities", "outlet", "F&B cost",
    "ingeniería de menú hotelero", "desayuno", "show cooking de buffet",
    "staff meal", "coste por cubierto", "no-show de banquete", "garantía de pax",
    "alergia en banquete", "menú de grupo", "menú de habitación",
    "in-room dining", "horario de cocina 24h", "pastelería de hotel",
    "panadería de hotel", "barra de lobby", "late night menu",
    "occupancy y previsión de cubiertos", "paquete de boda", "coffee break dulce",
    "estación de huevos", "estación de fruta", "merma de buffet",
    "regeneración en sala de banquetes", "etiqueta de buffet", "HACCP hotelero",
    "coste de desayuno", "upselling de room service", "minibar food cost",
]

ALERGENOS = OFICIO + [
    "gluten", "crustáceos", "huevo", "pescado", "cacahuete", "soja",
    "leche", "frutos de cáscara", "apio", "mostaza", "sésamo",
    "sulfitos", "altramuces", "moluscos", "Reglamento 1169",
    "contaminación cruzada", "trazas", "ficha de alérgenos", "carta de alérgenos",
    "información oral", "Anexo II", "salsa con gluten", "roux y gluten",
    "lecitina de soja", "sulfitos en el vino de salsa", "apio en el mirepoix",
    "frutos secos en obrador", "aceite compartido", "plancha compartida",
    "alternativa sin alérgeno", "declaración en delivery", "etiqueta de envase",
    "formación de sala", "pregunta del comensal", "anafilaxia",
]

MERMAS = OFICIO + [
    "merma de limpieza", "merma de cocción", "merma de porcionado",
    "rendimiento neto", "peso bruto", "peso neto", "factor de corrección",
    "despiece", "recorte", "hueso", "piel", "espinas",
    "aprovechamiento", "fondo con recortes", "fumet con espinas",
    "inventario teórico", "inventario real", "rotura", "caducidad",
    "FIFO", "merma evitable", "merma inevitable", "estándar de merma",
    "sobreproducción", "plato devuelto", "buffet sobrante", "pan del día",
    "aceite de fritura", "recorte de pastelería", "cáscara", "posos de café",
    "coste de la merma", "registro de merma", "causa de merma",
    "formación de partida", "porcionadora", "balanza",
]

CATERING = OFICIO + [
    "evento", "pax", "briefing de evento", "producción anticipada",
    "transporte", "cadena de frío en ruta", "regeneración en sala",
    "montaje", "desmontaje", "ficha de evento", "alergias del brief",
    "menú de boda", "menú corporativo", "coffee break", "cóctel de pie",
    "estación de vivo", "show cooking", "vaisselle", "dotación",
    "merma de evento", "sobras", "depósito", "seña", "balance de evento",
    "coste por comensal", "personal extra", "timing de servicio",
    "emplatado en línea", "buffet de evento", "etiqueta", "protocolo",
    "menú infantil", "menú vegano de evento", "bebida incluida",
    "barra", "maridaje de evento", "postre de corte",
]

BURGER = OFICIO + [
    "smash", "blend de carne", "punto de la carne", "Maillard en plancha",
    "pan brioche", "pan potato", "salsa de la casa", "encurtido",
    "queso fundido", "bacon", "fritura", "aceite de freidora",
    "patata", "doble cocción de patata", "ticket de burger", "combo",
    "delivery de burger", "tiempo de ticket", "holding", "vapor del pan",
    "merma de blend", "rendimiento de la pieza", "food cost de burger",
    "estación de plancha", "estación de fritura", "montaje",
    "alergeno del pan", "gluten", "lactosa del queso", "mostaza",
    "carta corta", "especial de temporada", "smash vs thick",
    "jugo", "reposo de la carne", "sal en el blend", "cadena de frío de la carne",
]

TRUCK = OFICIO + [
    "food truck", "commissary", "ruta", "generador", "agua a bordo",
    "carta corta", "mise en place previa", "regeneración", "ventana de servicio",
    "ticket medio de calle", "tiempo de cola", "menú de tres pasos",
    "food cost de truck", "merma por clima", "licencia", "punto de venta",
    "propina", "combo de calle", "bebida", "alergenos en ventana",
    "limpieza de camión", "aceite", "gas", "nevera de camión",
    "producción en obrador", "transporte de género", "cadena de frío",
    "evento privado con truck", "temporada", "lluvia y ventas",
    "marca en el camión", "redes", "reserva de plaza", "coste de plaza",
    "personal de ventana", "cierre de caja",
]

BAR = OFICIO + [
    "mise en place de barra", "especificación de cóctel", "dilución",
    "shake", "stir", "build", "hielo", "jigger", "bitter",
    "almíbar", "cordial", "shrub", "fermentado de barra", "garum de barra",
    "destilado", "vermú", "vino por copa", "cerveza de barril",
    "espuma de sifón", "clarificación", "leche clarificada", "fat wash",
    "coste de cóctel", "merma de cítrico", "bottle keep", "happy hour",
    "carta de barra", "maridaje", "café de especialidad", "espresso",
    "leche texturizada", "latte art", "temperatura de extracción",
    "molienda", "ratio de café", "cata", "servicio de vino",
    "decantar", "abocar", "copa", "temperatura de servicio",
]

MARKETING = [
    "keyword local", "SEO de restaurante", "Google Business Profile",
    "reseña", "respuesta a reseña", "foto de plato", "reel",
    "copy de carta", "descripción de plato", "menú engineering visible",
    "ticket medio", "oferta", "captación", "retención", "newsletter",
    "reserva", "no-show", "delivery", "marketplace", "comisión de app",
    "foto de obrador", "historia de origen", "estacionalidad en redes",
    "alergenos en la web", "carta digital", "QR", "precio psicológico",
    "ancla de precio", "plato bandera", "contenido de proceso",
    "calendario editorial", "UGC", "colaboración local", "influencer de barrio",
    "landing de reserva", "llamada a la acción", "prueba social",
    "posicionamiento", "propuesta de valor", "tono de marca",
]

SALA = [
    "mise en place de sala", "briefing de servicio", "comanda", "pase de sala",
    "marcaje", "cubierto", "servicio a la francesa", "servicio a la inglesa",
    "servicio a la rusa", "empanado de mesa", "crumb", "decantar",
    "escanciar", "abocar en sala", "maridaje de sala", "sugerencia",
    "alergia en sala", "tiempo de mesa", "rotación", "queja",
    "recuperación de queja", "cuenta", "propina", "reserva",
    "no-show", "walk-in", "lista de espera", "plano de sala",
    "estación de camarero", "runner", "sommelier", "jefe de sala",
    "protocolo", "etiqueta", "pan de cortesía", "agua",
    "café de cierre", "petit four", "despedida", "feedback de sala a cocina",
    "tempo del menú", "venta sugerida",
]

GESTION = CONSULT + [
    "cuenta de resultados", "cash flow", "IVA", "nómina", "turno",
    "cuadrante", "productividad por hora", "coste de ocupación",
    "alquiler", "suministros", "mantenimiento", "punto de pedido",
    "stock de seguridad", "pedido a proveedor", "albarán", "factura",
    "margen bruto", "margen neto", "umbral de rentabilidad",
]

HOSTELERIA = [
    "concepto de negocio", "propuesta de valor", "ticket", "cubierto",
    "ocupación", "estacionalidad", "turno de comida", "turno de cena",
    "delivery", "take away", "dark kitchen", "terraza", "barra",
    "licencia de actividad", "aforo", "ruido", "horario",
    "convenio de hostelería", "formación", "rotación de personal",
    "cultura de equipo", "estándar de servicio", "manual de operaciones",
    "APPCC", "limpieza", "apertura", "cierre", "caja",
    "reserva", "reputación", "competencia de barrio", "proveedor local",
    "sostenibilidad operativa", "desperdicio", "energía de cocina",
    "agua", "seguro", "inspección", "libro de reclamaciones",
    "menú del día", "carta", "menú degustación", "evento privado",
]

PROFESION = [
    "chef", "jefe de cocina", "sous chef", "chef de partie", "commis",
    "pastelero", "panadero", "heladero", "chocolatero", "sumiller",
    "jefe de sala", "maître", "camarero", "barista", "bartender",
    "gerente", "propietario", "consultor gastronómico", "F&B manager",
    "brigada", "partida", "briefing", "formación en el puesto",
    "estándar", "repetibilidad", "oficio", "juicio sensorial",
    "fatiga de servicio", "liderazgo de pase", "relevo", "cuaderno de partida",
    "vocabulario de cocina", "orden de trabajo", "crítica de plato",
    "cata", "calibración del equipo", "carrera", "aprendizaje",
    "mentor", "escuela", "prácticas", "coste de un error en servicio",
    "responsabilidad del alérgeno", "ética del producto",
]

COCINAS = {
    "Cocina Alemana": ["sauerbraten", "spätzle", "schnitzel", "pretzel", "chucrut", "bratwurst", "kartoffelknödel", "saumagen", "schwarzwälder", "leberkäse", "brezel", "senf", "rindswurst", "eintopf", "rote grütze", "marzipan", "stollen", "currywurst", "flammkuchen", "maultaschen"],
    "Cocina Belga": ["moules", "fritas belgas", "waffle", "carbonade", "waterzooi", "speculoos", "cerveza trapense", "endivia", "anguila en verde", "stoofvlees", "gofre de Lieja", "chocolate belga", "croqueta de gamba", "tomate-crevette", "filet américain", "witloof", "tarta de arroz", "jenever", "conejo a la cerveza", "vol-au-vent"],
    "Cocina Británica": ["roast", "yorkshire pudding", "gravy", "shepherd's pie", "fish and chips", "bangers", "black pudding", "scone", "clotted cream", "custard", "sticky toffee", "beef wellington", "full breakfast", "cornish pasty", "scotch egg", "crumble", "trifle", "mince pie", "bubble and squeak", "ploughman's"],
    "Cocina Croata": ["peka", "pašticada", "crni rižot", "buzara", "štrukli", "kulen", "janjetina", "blitva", "gregada", "fritaja", "sarma", "palačinke", "rakija", "pršut", "sir iz ulja", "maneštra", "brodet", "fritule", "rozata", "paški sir"],
    "Cocina Española": ["sofrito", "fondo", "salsa española", "allioli", "escabeche", "adobo", "salmuera", "paella", "socarrat", "jamón", "tapa", "ración", "guiso", "pisto", "romesco", "pil-pil", "salsa verde", "fritura andaluza", "asador", "arroz caldoso"],
    "Cocina Francesa": ["roux", "fonds", "demi-glace", "velouté", "béchamel", "hollandaise", "béarnaise", "mirepoix", "bouquet garni", "brunoise", "julienne", "concassé", "napper", "monter au beurre", "beurre blanc", "gastrique", "fumet", "glace", "liaison", "court-bouillon"],
    "Cocina Griega": ["sofrito griego", "horiatiki", "tzatziki", "moussaka", "pastitsio", "souvlaki", "gyro", "spanakopita", "dolma", "avgolemono", "taramasalata", "fava", "horta", "aceite de oliva", "orégano seco", "limón", "yogur", "filo", "baklava", "ouzo"],
    "Cocina Italiana": ["soffritto", "soffritto di odori", "ragù", "fondo bruno", "fumetto", "mantecare", "risotto", "sfumare", "pomodoro", "pasta fresca", "sfoglia", "besciamella", "ragù alla bolognese", "brasato", "brodo", "battuto", "odori", "aglio olio", "pesto", "sugo"],
    "Cocina Países Bajos": ["stamppot", "erwtensoep", "bitterballen", "kroket", "haring", "poffertjes", "pannenkoek", "hutspot", "boerenkool", "rookworst", "frikandel", "kapsalon", "drop", "speculaas", "oliebollen", "stroopwafel", "kaas", "mosterdsoep", "zuurkool", "appelmoes"],
    "Cocina Portuguesa": ["refogado", "caldo verde", "bacalhau", "açorda", "cataplana", "arroz de marisco", "francesinha", "prego", "alheira", "chouriço", "piri-piri", "amêijoas", "polvo à lagareiro", "cozido", "leitão", "pastel de nata", "arroz doce", "sardinhas", "caldo", "azeite"],
    "Cocina Suiza": ["fondue", "raclette", "rösti", "zürcher geschnetzeltes", "älplermagronen", "birchermüesli", "basler läckerli", "cervelat", "maluns", "capuns", "saucisse aux choux", "papel", "queso de alp", "chocolate suizo", "merengue", "crema de chocolate", "vino suizo", "hierbas de los Alpes", "pan de centeno", "caldo de ternera"],
    "Cocina Turca": ["soğan", "salça", "yoğurt", "kebap", "pide", "lahmacun", "börek", "dolma", "mercimek", "ezogelin", "menemen", "köfte", "baklava", "lokum", "ayran", "sumak", "pul biber", "nar ekşisi", "zeytinyağı", "pilav"],
    "Cocina Argentina": ["asado", "parrilla", "achuras", "chimichurri", "salsa criolla", "empanada", "provoleta", "matambre", "vacío", "entrana", "molleja", "choripán", "dulce de leche", "alfajor", "medialuna", "mate", "malbec", "humita", "locro", "fugazza"],
    "Cocina Brasileña": ["refogado", "feijoada", "farofa", "moqueca", "acarajé", "vatapá", "caruru", "pão de queijo", "brigadeiro", "coxinha", "churrasco", "picanha", "caipirinha", "dendê", "mandioca", "tapioca", "arroz e feijão", "vinagrete", "queijo coalho", "açaí"],
    "Cocina Chilena": ["sofrito", "pebre", "merkén", "empanada de pino", "pastel de choclo", "cazuela", "curanto", "mariscal", "chupe", "porotos", "completo", "mote", "sopaipilla", "manjar", "pejerrey", "reineta", "chorrillana", "plateada", "charquicán", "ajo"],
    "Cocina Colombiana": ["hogao", "ajiaco", "bandeja paisa", "arepa", "sancocho", "lechona", "empanada", "patacón", "arroz con coco", "suero", "aji", "frijol", "chicharrón", "buñuelo", "natilla", "obleas", "changua", "mute", "tamal", "chocolatada"],
    "Cocina Dominicana": ["sofrito", "sancocho", "la bandera", "mangú", "los tres golpes", "chicharrón", "moro", "habichuelas", "pollo guisado", "queso frito", "casabe", "yaniqueque", "majarete", "habichuela con dulce", "chinola", "wasakaka", "chivo liniero", "arroz", "plátano", "ají"],
    "Cocina Ecuatoriana": ["encebollado", "ceviche", "llapingacho", "fritada", "hornado", "locro", "seco de chivo", "encocado", "bolón", "patacón", "aji criollo", "mote", "humita", "colada morada", "fanesca", "cuy", "chaulafán", "encebolla", "verde", "maní"],
    "Cocina Jamaicana": ["jerk", "escoveitch", "ackee", "saltfish", "rice and peas", "curry goat", "oxtail", "festival", "bammy", "callaloo", "pimento", "scotch bonnet", "allspice", "browning", "rundown", "patty", "festival dumpling", "sorrel", "plantain", "thyme"],
    "Cocina Mexicana": ["sofrito", "recaudo", "mole", "nixtamal", "masa", "salsa roja", "salsa verde", "adobo", "marinada", "barbacoa", "birria", "consomé", "taco", "tortilla", "chile", "epazote", "hoja santa", "achiote", "escabeche", "caldo"],
    "Cocina Paraguaya": ["so'o", "chipa", "sopa paraguaya", "vorí vorí", "mbeyú", "chipa guasu", "payagua mascada", "locro", "asado", "borracho", "kosereva", "dulce de mamón", "tereré", "mandioca", "queso paraguay", "morcilla", "chorizo", "empanada", "mbaipy", "cocido"],
    "Cocina Peruana": ["aderezo", "ají amarillo", "ají panca", "leche de tigre", "ceviche", "tiradito", "lomo saltado", "ají de gallina", "causa", "anticucho", "pachamanca", "chaufa", "huancaína", "ocopa", "rocoto", "culantro", "choclo", "cancha", "suspiro", "picarones"],
    "Cocina Venezolana": ["sofrito", "pabellón", "arepa", "hallaca", "cachapa", "tequeño", "asado negro", "caraotas", "tajadas", "perico", "queso de mano", "guayanesa", "hervido", "sancocho", "empanada", "golfeado", "quesillo", "papelón", "aliño", "guasacaca"],
    "Cocina China": ["wok hei", "velveting", "salteado", "vapor", "rojo cocido", "cinco especias", "salsa de soja", "doubanjiang", "shaoxing", "almidón de maíz", "dim sum", "bao", "jiaozi", "arroz frito", "fideos", "caldo maestro", "glaseado cantonés", "aceite de sésamo", "jengibre", "cebolleta"],
    "Cocina India": ["tadka", "masala", "garam masala", "curry", "dosa", "idli", "naan", "roti", "dal", "raita", "chutney", "tandoor", "biryani", "ghee", "paneer", "tikka", "korma", "vindaloo", "sambar", "rasam"],
    "Cocina Japonesa": ["dashi", "kombu", "katsuobushi", "umami", "shoyu", "miso", "mirin", "sake de cocina", "sushi", "nigiri", "sashimi", "tempura", "donabe", "kaiseki", "agemono", "nimono", "yakimono", "sunomono", "shio", "koji"],
    "Cocina Tailandesa": ["pasta de curry", "leche de coco", "fish sauce", "galanga", "hierba limón", "lima kaffir", "chili", "pad thai", "tom yum", "tom kha", "som tum", "mango sticky rice", "nam pla", "palm sugar", "tamarindo", "albahaca thai", "cilantro raíz", "wokk", "salteado", "balance ácido-sal-dulce-picante"],
}

BANCOS_POR_NOMBRE = {
    "Cocina Creativa": COCINA + ["plato de autor", "textura", "deconstrucción", "snack", "bocado"],
    "Pastelería Creativa": PASTELERIA,
    "Chocolatería Creativa": CHOCOLATE,
    "Heladería Creativa": HELADO,
    "Panadería Creativa": PAN,
    "Fermentus Con AI+": FERMENT,
    "VegChef Plant-Based": VEG,
    "Food Pairing AI": PAIRING,
    "Gastro Lexicum": LEX,
    "Consultor Gastronómico": CONSULT,
    "Chef Consultor Pro": CONSULT + ["auditoría de cocina", "estándar de receta", "formación de brigada"],
    "Heladero Consultor Pro": HELADO + ["carta de heladería", "vitrina", "coste del mix"],
    "Chocolatero Consultor Pro": CHOCOLATE + ["obrador", "escaparate", "temperatura de tienda"],
    "Pastelero Consultor Pro": PASTELERIA + ["obrador", "vitrina", "pedido de encargo"],
    "Pizzero Consultor Pro": OFICIO + ["masa", "hidratación de pizza", "poolish", "biga", "fermentación en frío", "horno de pizza", "solera", "cornicione", "salsa de tomate", "mozzarella", "fior di latte", "estirado", "pala", "pizza a la pala", "napolitana", "romana", "new york", "pepperoni", "alicci", "merma de masa", "food cost de pizza", "tiempo de ticket", "delivery de pizza", "corte", "aceite de acabado", "albahaca", "horno de leña", "temperatura de solera", "burbuja", "leopardo", "stretchar", "porcionado de bola", "cadena de frío de la masa"],
    "Barista Consultor Pro": OFICIO + ["espresso", "ratio", "extracción", "molienda", "tiempo de shot", "crema", "canalización", "temperatura del agua", "leche texturizada", "microespuma", "latte art", "filtro", "pour over", "inmersión", "tueste", "origen", "cata", "acidez del café", "dulzor del café", "amargor", "agua del café", "descalcificación", "merma de café", "food cost de bebida", "carta de cafetería", "brunch", "pastelería de barra", "ticket", "take away"],
    "Sommelier Consultor Pro": OFICIO + ["cata", "servicio de vino", "decantar", "copas", "temperatura de servicio", "maridaje", "carta de vinos", "margen de bodega", "compra de vino", "añada", "crianza", "tanino", "acidez", "cuerpo", "dulzor residual", "vino abocado", "espumoso", "generoso", "sake", "cerveza de guarda", "corcho", "reducción en botella", "fault", "por copa", "coravin", "bodega", "rotación de botella", "sugerencia de sala", "maridaje de menú"],
    "Bartender Consultor Pro": BAR,
    "Panadero Consultor Pro": PAN + ["obrador", "cuota de horno", "pedido de tienda", "merma de pan"],
    "Chef Privado Pro": COCINA[:25] + ["menú a domicilio", "showcooking", "brief del cliente", "alergias del hogar", "compra para evento", "emplatado en casa", "timing", "vaisselle", "menú de familia", "restricción", "presupuesto del cliente", "degustación privada", "cocina de casa", "transporte de plato", "servicio en mesa del cliente"],
    "Chef Ejecutivo Pro": CONSULT + ["menú de grupo", "estándar multi-local", "ingeniería de carta"],
    "Gerente de Restaurante Pro": GESTION[:40],
    "Comida del Personal": OFICIO + ["staff meal", "coste de personal meal", "nutrición de brigada", "turno partido", "familia", "aprovechamiento", "menú de equipo", "alergias del equipo", "cocción de gran volumen", "tiempo de comida", "satisfacción de brigada", "presupuesto diario", "variedad semanal", "proteína", "verdura", "legumbre", "batch cooking", "regeneración", "higiene del office", "feedback del equipo"],
    "ID Alérgenos": ALERGENOS,
    "Mermas GenCal": MERMAS,
    "Calcula Pax": OFICIO + ["pax", "gramaje por comensal", "merma de evento", "bebida por persona", "pan por persona", "producción por pax", "buffer", "no-show", "menú infantil", "menú de staff del evento", "hielo", "vajilla por pax", "timing", "estación", "porcionado", "ficha por comensal", "coste por cabeza", "proteína por persona", "guarnición", "salsa por ración", "postre de corte", "café", "agua", "restricciones del listado", "producción escalada"],
    "Conversor Ing": ["gramo", "kilogramo", "mililitro", "litro", "onza", "libra", "cup", "cucharada", "cucharadita", "°C", "°F", "porcentaje de panadero", "ratio", "partes", "concentración", "baumé", "brix", "salmuera %", "factor", "densidad", "conversión de horno", "gas mark", "pieza", "manojo", "lata", "botella", "ración", "yield", "peso escurrido", "peso neto", "alérgeno en la conversión", "redondeo de ficha", "unidad de compra", "unidad de receta"],
    "Mental Coach": PROFESION[:30] + ["estrés de servicio", "comunicación de brigada", "feedback", "error en el pase", "recuperación", "liderazgo", "relevo de turno", "conflicto", "briefing", "cierre de servicio"],
    "Catering AI+": CATERING,
    "Burger Pro AI+": BURGER,
    "Food Truck AI+": TRUCK,
    "Bar & Lounge AI+": BAR,
    "Casual Restaurants AI+": GESTION[:20] + ["menú del día", "plato de carta", "ticket", "turno", "familia", "combo", "take away", "terraza", "barra", "postre", "café", "pan", "ensalada", "guarnición", "salsa de la casa", "especial del día", "merma del día", "apertura", "cierre", "reserva de grupo"],
    "Sosa Ingredients Agent": ["texturizante", "esferificación", "alginato", "calcic", "agar", "goma xantana", "goma garrofín", "lecitina", "metilcelulosa", "maltodextrina", "isomalt", "gelatina", "pectina", "gellan", "iota", "kappa", "albúmina", "yopol", "aire", "espuma", "gel", "noodles de agar", "crujiente", "polvo de aceite", "emulsión", "estabilizante", "dosis", "dispersión", "hidratación del texturizante", "reposo", "gelificación en frío", "gelificación en caliente", "sabor neutro", "ficha de aplicación", "alergeno del texturizante"],
    "tSpoonLab Agent": ["escandallo", "ficha técnica", "alergenos", "coste", "valor nutricional", "porción", "merma", "proceso", "foto de ficha", "ingrediente", "subreceta", "salsa como subreceta", "actualización de precio", "proveedor", "etiqueta", "APPCC en ficha", "tiempo de proceso", "utensilio", "punto de cocción", "rendimiento", "lote", "versión de ficha", "aprobación", "publicación en carta", "formación con la ficha", "unidad de receta", "peso neto", "peso bruto", "factor de corrección", "método", "temperatura de cocción", "enfriamiento", "abatido en ficha", "regeneración en ficha", "vida útil", "lote de producción", "responsable de ficha"],
    "InstaFlow AI Pro": MARKETING[:25] + ["reel de proceso", "carrusel de receta", "story de pase", "hashtag local", "CTA a reserva"],
    "PinterAI Content Pro": MARKETING[:28] + ["pin de receta", "tablero de temporada", "foto vertical", "guardado", "tráfico a carta", "idea de emplatado", "color del plato", "texto del pin", "estacionalidad visual", "enlace a la carta", "tablero de salsas", "tablero de obrador"],
    "Pinterest Pins Gen": MARKETING[:25] + ["pin", "texto sobre foto", "estacionalidad visual", "idea de emplatado", "color de plato", "formato vertical", "portada de receta", "ingrediente hero", "proceso en cuatro fotos", "guardado", "tablero"],
    "BlogPost SEO Gen+": MARKETING[:24] + ["intención de búsqueda", "definición", "pregunta frecuente", "enlace interno", "title", "meta description", "hreflang", "variante ortográfica", "People Also Ask", "párrafo de definición", "glosario"],
    "Keyword Discovery AI+": ["keyword", "intención", "sinónimo", "variante ortográfica", "búsqueda local", "long tail", "pregunta", "comparación", "cómo se hace", "qué es", "precio", "cerca de mí", "en inglés de cocina", "falso amigo", "estacional", "marca vs genérico", "canibalización", "página existente", "glosario", "carta", "blog", "landing", "SERP", "título", "meta", "FAQ", "entidad", "modificador local", "idioma de búsqueda", "demanda de definición", "demanda de proceso", "demanda de compra"],
    "MenuDish Local SEO": MARKETING[:24] + ["Google Business", "categoría del local", "foto de fachada", "horario", "menú en la ficha", "pregunta de Maps", "reseña reciente", "publicación de plato", "categoría de cocina", "atributos del local", "enlace de reserva", "foto de carta"],
    "Gastro Calendar": ["calendario de carta", "temporada", "festivo", "campaña", "menú de navidad", "menú de verano", "producto de mes", "publicación", "reserva de campaña", "proveedor de temporada", "merma de campaña", "post de calendario", "story", "evento del barrio", "feria", "puente", "cierre por festivo", "especial de un día", "comunicación al equipo", "briefing de campaña", "menú de Semana Santa", "menú de feria", "producto de otoño", "producto de primavera", "cambio de carta", "comunicación de alérgeno de campaña", "coste del menú festivo", "previsión de cubiertos", "briefing de sala", "foto de campaña", "reserva de grupo", "cierre de inventario de campaña"],
    "ChatGPT 5.5": ["prompt", "contexto", "ficha técnica asistida", "revisión humana", "alérgeno no delegable", "borrador de carta", "traducción de menú", "tono", "límite del modelo", "verificación", "instrucción de sistema", "ejemplo", "formato de salida", "tabla", "lista", "temperatura que se contrasta", "norma que se contrasta", "no inventar cifra", "borrador de post", "borrador de respuesta a reseña", "resumen de briefing", "traducción de alérgeno", "adaptación de mercado", "registro de cambios", "versión", "fuente", "duda de partida", "juicio del chef", "lo que el modelo no prueba", "lo que el cocinero firma"],
    "Sonar Deep Research": ["fuente", "cita", "normativa", "no inventar cifra", "comparar fuentes", "fecha de la fuente", "SERP", "intención", "resumen para cocina", "duda que se verifica en el pase", "reglamento", "ficha técnica oficial", "precio de mercado con fecha", "contraste de dos fuentes", "lo que no dice la fuente", "alcance geográfico", "idioma de la fuente", "actualización", "resumen para el gerente", "resumen para el chef", "alerta de cifra huérfana", "norma de alérgenos", "norma de higiene", "convenio", "impuesto", "licencia", "no es asesoría legal", "pregunta siguiente", "hueco de la fuente", "decisión que sigue siendo del local"],
    "Timlup – Asistente de Checklists": ["apertura", "cierre", "limpieza", "APPCC", "temperatura", "registro", "turno", "responsable", "incidencia", "check de cámara", "check de aceite", "check de baño maría", "recepción", "alérgenos del día", "briefing", "cierre de caja", "merma del día", "pedido", "mantenimiento", "formación", "check de pase", "check de sala", "check de baños", "check de barra", "aceite de fritura", "etiquetado del día", "FIFO del día", "temperaturas de entrega", "firma", "plan de acción", "reincidencia", "foto de incidencia"],
}

HOTEL_NOMBRES = {
    "Hotel Staff Meal Planner": "staff meal",
    "Hotel Bar & Lounge Menu AI": "barra de hotel",
    "In-Room Dining Optimizer": "room service",
    "F&B Reporting Assistant": "informe F&B",
    "Buffet Master AI": "buffet",
    "Hotel Pastelería & Panadería Pro": "pastelería de hotel",
    "Desarrollador de Conceptos F&B": "concepto F&B",
    "Hotel F&B Cost Controller": "food cost hotelero",
    "Mini-Bar & Amenities AI": "minibar",
    "Diseñador de Menú Room Service": "menú de habitación",
    "Banquet Event Order AI": "BEO",
    "Hotel Menu Engineering Pro": "ingeniería de menú hotelero",
}


def terminos_de(nombre: str) -> list[str]:
    if nombre in BANCOS_POR_NOMBRE:
        base = BANCOS_POR_NOMBRE[nombre]
    elif nombre in HOTEL_NOMBRES:
        foco = HOTEL_NOMBRES[nombre]
        base = HOTEL + [foco, f"estándar de {foco}", f"merma de {foco}", f"coste de {foco}", f"alergenos en {foco}"]
    elif nombre in COCINAS:
        base = OFICIO + COCINAS[nombre] + [
            "fondo", "salsa", "guarnición", "cocción", "fermentación",
            "escandallo del plato", "merma del despiece", "alérgeno del plato",
            "emplatado", "porción", "proveedor local", "temporada",
            "ficha técnica", "carta", "servicio",
        ]
    else:
        base = COCINA
    vistos = []
    seen = set()
    for t in base:
        k = norm(t)
        if k in seen:
            continue
        seen.add(k)
        vistos.append(t)
        if len(vistos) >= 42:
            break
    return vistos


TRANSVERSALES = [
    ("Sala", "Oficio de sala, fuera del catálogo de agentes de cocina.", SALA),
    ("Gestión", "Números del negocio: margen, caja, turno y compra.", GESTION[:42]),
    ("Hostelería", "El local como sistema: concepto, turno, norma y equipo.", HOSTELERIA),
    ("La profesión", "Oficios, brigada y el juicio que un agente no sustituye.", PROFESION),
]


def main():
    catalogo = json.loads(CATALOGO.read_text(encoding="utf-8"))
    glosario, slugs = cargar_publicados()
    agentes = []
    for bloque in catalogo:
        for ag in bloque["agentes"]:
            if ag["nombre"] in ("¿Quién Soy?",):
                continue
            términos = []
            for t in terminos_de(ag["nombre"]):
                ref = publicado(t, glosario, slugs)
                términos.append({
                    "termino": t,
                    "estado": "publicado" if ref else "semilla",
                    "post": ref,
                })
            agentes.append({
                "categoria": bloque["categoria"],
                "agente": ag["nombre"],
                "libreria": ag.get("post"),
                "terminos": términos,
                "publicados": sum(1 for x in términos if x["estado"] == "publicado"),
                "semillas": sum(1 for x in términos if x["estado"] == "semilla"),
            })
    transversales = []
    for nombre, nota, banco in TRANSVERSALES:
        términos = []
        seen = set()
        for t in banco:
            k = norm(t)
            if k in seen:
                continue
            seen.add(k)
            ref = publicado(t, glosario, slugs)
            términos.append({"termino": t, "estado": "publicado" if ref else "semilla", "post": ref})
            if len(términos) >= 42:
                break
        transversales.append({
            "area": nombre,
            "nota": nota,
            "terminos": términos,
            "publicados": sum(1 for x in términos if x["estado"] == "publicado"),
            "semillas": sum(1 for x in términos if x["estado"] == "semilla"),
        })

    payload = {
        "programa": "Glosario gastronómico aichef.pro",
        "tanda": 1,
        "fecha": "2026-10-22",
        "nota": (
            "Semillas de trabajo para 1-2 años. No son volúmenes de búsqueda. "
            "«Publicado» significa que ya hay un post de glosario en español cuyo "
            "slug o título contiene el término. Las cifras de Search Console del "
            "encargo (homogeneización, abocar/abocado, hidrólisis, maceración, roux, "
            "demi-glace, Maillard) no se han recontado en esta tanda."
        ),
        "agentes": len(agentes),
        "terminos_semilla": sum(len(a["terminos"]) for a in agentes),
        "ya_publicados_en_agentes": sum(a["publicados"] for a in agentes),
        "tanda_1": TANDA_1,
        "catalogo": agentes,
        "transversales": transversales,
    }
    OUT_JSON.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    lineas = [
        "# Glosario gastronómico — backlog maestro",
        "",
        "Programa de 1 a 2 años. Cada ficha se escribe en los 7 idiomas del sitio, al mismo nivel, con el término que la gente busca en ese mercado. El español va delante. Esto es la tanda 1: el mapa, no las miles de fichas.",
        "",
        "Fuente de agentes: `scripts/astro-migration/fase8c-agentes/catalogo-hub.json`. Un agente del catálogo que no es oficio de cocina (`¿Quién Soy?`) no entra. Las áreas de sala, gestión, hostelería y la profesión van al final: no son agentes, y hacen falta igual.",
        "",
        "Estado **publicado**: ya existe un post de la categoría glosario en español. Estado **semilla**: propuesto, sin ficha todavía. No hay volúmenes inventados. Las impresiones de Search Console que cita el encargo de esta tanda (homogeneización 13.214 a posición 6,6; abocar/abocado por encima de 20.000 y sin cubrir bien «abocado»; hidrólisis, maceración, roux, demi-glace y Maillard) se tratan como dato del encargo, no como una medición nueva.",
        "",
        f"Agentes: **{payload['agentes']}**. Términos semilla en agentes: **{payload['terminos_semilla']}**. De esos, el cruce marca **{payload['ya_publicados_en_agentes']}** como ya publicados en el glosario español.",
        "",
        "## Tanda 1 — lo que sale en esta entrega",
        "",
        "Quick wins en español (title, definición de 40–60 palabras, FAQ con DefinedTerm y FAQPage, variantes y CTA): homogeneización, abocar/abocado, hidrólisis, maceración, roux, demi-glace y reacción de Maillard. El slug `maillard-concepto-y-definicion-2` pasa con 301 a `/blog/reaccion-de-maillard`.",
        "",
        "Definiciones nuevas del clúster de salsas, emulsiones y cocina de fondos, en los 7 idiomas: beurre manié, napar, montar al burro, beurre blanc, gastrique, ligado con yema, glace de viande, fumet y papilla de almidón. Roux (en alemán, Mehlschwitze), emulsión y demi-glace se abren en los idiomas que aún no los tenían y apuntan al post español ya publicado.",
        "",
        "## Por agente",
        "",
    ]
    cat = None
    for ag in agentes:
        if ag["categoria"] != cat:
            cat = ag["categoria"]
            lineas += [f"### {cat}", ""]
        lib = f" · librería `{ag['libreria']}`" if ag["libreria"] else ""
        lineas.append(
            f"#### {ag['agente']}{lib} — {ag['publicados']} publicados, {ag['semillas']} semillas"
        )
        lineas.append("")
        for t in ag["terminos"]:
            marca = "publicado" if t["estado"] == "publicado" else "semilla"
            extra = f" (`{t['post']}`)" if t["post"] else ""
            lineas.append(f"- {t['termino']} — {marca}{extra}")
        lineas.append("")
    lineas += ["## Áreas transversales", ""]
    for area in transversales:
        lineas.append(f"### {area['area']}")
        lineas.append("")
        lineas.append(area["nota"])
        lineas.append("")
        lineas.append(f"{area['publicados']} publicados, {area['semillas']} semillas.")
        lineas.append("")
        for t in area["terminos"]:
            marca = "publicado" if t["estado"] == "publicado" else "semilla"
            extra = f" (`{t['post']}`)" if t["post"] else ""
            lineas.append(f"- {t['termino']} — {marca}{extra}")
        lineas.append("")
    OUT_MD.write_text("\n".join(lineas), encoding="utf-8")
    print(f"agentes={payload['agentes']} semillas={payload['terminos_semilla']} publicados={payload['ya_publicados_en_agentes']}")
    for ag in agentes:
        n = len(ag["terminos"])
        if n < 30 or n > 50:
            print(f"  FUERA DE RANGO {ag['agente']}: {n}")


if __name__ == "__main__":
    main()
