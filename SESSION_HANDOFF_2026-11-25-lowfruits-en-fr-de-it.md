# Handoff 25 nov 2026 — LowFruits EN, FR, DE e IT (sesión Claude Code, Mac)

> Sesión Claude Code en el Mac. Retoma la sesión nocturna que se cortó a las 02:20 (el Mac se apagó sin batería):
> se recuperó desde el transcript `e21f2d81…jsonl`. Las correcciones de la auditoría de #256 estaban en disco sin commit.
> Fuente de la estrategia: `/Users/johnguerrero/aichef-lowfruits/<Idioma>/aichef-lowfruits-XX-2026-11.md`.

## 1. Decisiones de John

- **«A partir de ahora fusiona tú los PR sin esperarme… luz verde»** (25-nov, mañana). Criterio aplicado: auditoría
  adversarial aplicada + deploy preview verde del ÚLTIMO commit + conflictos resueltos → `gh pr merge N --squash`.
- **LowFruits sin regla de proporcionalidad** (se hacen todas las oportunidades). Proporcionalidad vigente para lo demás.
- **Motor:** borradores con DeepSeek v4.1 flash vía Ori y pasada final de Opus (cifras comparadas por script con el
  original + auditoría adversarial). Las piezas cortas (meta, FAQ, párrafos) se escriben directamente.

## 2. Fusionado hoy (todo en producción salvo lo marcado)

| PR | Idioma | Pieza |
|---|---|---|
| #250, #256, #260 | ES | Planes reales en 44 posts (el «Plan AI Chef Miembro» roto del pipeline del 15-ago) + hallazgos menores |
| #251-#255 | EN | Menu pricing calculator · bloque A · AI recipe generator · AI for bakeries · satélites de librerías |
| #257, #259, #261, #262, #263, #264 | FR | Accord mets-vins · fiche technique + plantilla · bloque A (IA cuisine, calcul food cost **HT**) · tableau des allergènes + plantilla · HACCP (**el post traía el 74 °C de la FDA**) + relevé de temperaturas · glosario menu dégustation |
| #258 | — | `llms.txt` de la tanda nocturna |
| #261 | 7 idiomas | **Fallo de la calculadora de food cost**: el paso 1 pedía el gramaje POR RACIÓN y el código divide entre raciones (coste 4× más bajo y «excelente» falso). Ahora pide la cantidad total de la receta |
| #265, #266, #267 | DE | Wareneinsatz (calculadora renombrada, Excel, MwSt 7 %/19 %) · bloque A (Portionsgrößen: 13k impr./0,28 % CTR → meta con cifras + PDF) · Foodpairing (la tabla del ES en producción afirmaba compuestos falsos: corregida en ES y DE) |
| #268 | — | **Bytes NUL en el HTML de producción** (react-dom 18.3 streaming). `astro-site/scripts/strip-nul-bytes.mjs` tras `astro build`. Verificado: 0 en producción |
| #269 | DE | Alérgenos, HACCP y LMHV contra la normativa alemana (código A–R austriaco, 60 °C BfR, LMIDV § 4 Abs. 4, IfSG § 43) |
| #270 | IT | Glosarios menu degustazione (1.300/mes) y abbinamento cibo-vino (1.180/mes); IVA somministrazione 10 % vino incluido |

**Abierto al escribir esto:** #271 (DE plantillas Allergenliste A–R + HACCP-Vorlagen), con la auditoría aplicándose.

## 3. Normativa verificada (en memoria, con fuentes)

- FR: `reference_normativa-francesa-haccp-alergenos` — anexo IV del arrêté (enfriamiento +63 → +10 °C, J+3) solo es
  obligatorio en restauración colectiva; restaurante = GBPH (< +6 °C en 2 h). 74 °C = FDA, nunca en Francia.
- DE: `reference_normativa-alemana-alergenos-haccp` — información oral permitida con condiciones (LMIDV § 4 Abs. 4);
  sin código de letras oficial (el documentado es el austriaco A–R); Heißhalten ≥ 60 °C (BfR); IfSG § 43.
- MwSt DE 2026: comida en hostelería 7 % permanente, bebidas 19 %. IT: somministrazione 10 % (vino incluido).

## 4. Pendiente

- **IT:** alérgenos (los posts `lista-allergeni-alimentari` y `etichettatura-allergeni` tienen cientos de impresiones en
  pos. 20-40), calcolo food cost (la calculadora IT existe: retitular), manuale HACCP, gestionale ristorante (590).
- **NL** y **PT** (PT-PT y PT-BR): sin empezar.
- **Deuda anotada, fuera de LowFruits:** breadcrumb del JSON-LD de las calculadoras con el hub en español en todos los
  idiomas (`marketing-heads/calculadora-food-cost.ts:46`; patrón del generador Fase 6) · breadcrumb `/de/de/` en
  landings DE (conocido) · «27 Weltküchen» sin verificar en `landingRecetas` · FAQ duplicadas DE preexistentes
  (Kreuzkontamination, Mise en Place) · landing EN de costes con cifras de capa comercial · «14 allergens» en
  `use-cases-content.en.ts`.
- **GSC:** medir en 2-3 semanas las páginas retituladas (raciones DE, calculadoras, landings).

## 5. Gotchas nuevos

- `fase8b-regen-lastmod.py` sigue bajando `/blog/ia-gestion-alergenos-hosteleria` a 22-nov: restaurar a 23 en cada PR.
- Reescribir JSON con `json.dumps` reformatea el fichero entero (diff de 38 KB): editar con reemplazo de texto exacto.
- `gh pr view` puede dar el check del commit ANTERIOR: esperar a que el `headRefOid` coincida antes de fusionar.
- DeepSeek, al traducir, deforma alguna URL («somelier») e inventa matices («se mide al corazón, no en la superficie»;
  la confusión abbinare/marinare): comparar cifras y enlaces por script y leer las secciones delicadas.
- La SERP de «KI Restaurant» (DE) es de un restaurante llamado «Ki»: LowFruits no distingue intención navegacional.
- `mediaanalysisd` (análisis de Fotos de macOS) sube la CPU al 80 % tras un reinicio: no lanzar más de un agente entonces.
