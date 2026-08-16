# Session Handoff — 2026-08-15/16 → siguiente sesión

## TL;DR

Dos frentes, los dos COMPLETOS y en producción/`main`:

1. **Blog italiano: clúster sicurezza alimentare CERRADO (posts 4-5).**
   `7-principi-haccp` (390/mes + clúster 1.270) y `temperature-frigorifero-haccp`
   (260/mes + 650) publicados, desplegados y verificados en vivo. Pentágono 1-5
   interenlazado en las dos direcciones; el pilar CEDE su pregunta FAQ de los
   7 principios al post 4 (una Question, una URL — la jugada del post 3 con la
   de los 14). Diferenciador de ambos: separar LEY de PRASSI con la norma
   exacta por valor (verificada contra el cuadro técnico legal; el abatimiento
   NO tiene tiempos legales — Reg. 852/2004 solo pide «il più rapidamente
   possibile»). Gates: faq-dup 0 · h1 0 · sanzioni 0 · fase9 VERDE · build
   1.255 · **enlaces-vivos 206/0** · FAQPage 5+5 verificado en dist Y en vivo.
2. **Research nacional fr/de/pt/nl COMPLETO → 4 roadmaps committeados.**
   Workflow de 4 cazadores (opus, ~840 keywords, ~130 SERP, `--pais` explícito
   2250/2276/2620/2528). `ROADMAP_BLOG_FRANCES.md` (14 posts, ~62.000/mes,
   HACCP 27.100 LOW), `ROADMAP_BLOG_ALEMAN.md` (14, ~33.000),
   `ROADMAP_BLOG_PORTUGUES.md` (14, ~15.000 + upside BR ×10-26),
   `ROADMAP_BLOG_NEERLANDES.md` (12, ~15.000 + Flandes +25-55 %). Refutados
   >80.000/mes de falsos candidatos. Datos crudos en `.work/research-{fr,de,pt,nl}.json`
   y `.work/research-blog-<lang>.md` (SOLO este VPS, gitignorados).

**HEAD**: `57cb3e5` · deploy Netlify verde, las dos URLs nuevas en 200 con su
contenido y el sitemap con lastmod 2026-08-16.

## Commits de la sesión (pusheados, deploy verde)

| Commit | Qué |
|---|---|
| `e3cbb85` | Posts IT 4-5 + 6 imágenes + interenlazado del pentágono + lastmod |
| `57cb3e5` | Los 4 roadmaps nacionales + IT marcado clúster completo + log §8 |

## Lo que la sesión deja como MÉTODO

- **Bridge DILUYE datos fijados aunque vayan marcados «NON MODIFICARE»**: la
  tabla legal del post 5 salió con los máximos de ley rebajados a «0/+4 °C
  prassi» (macinata +2, pollame +4, frattaglie +3, carni +7 → todos diluidos).
  La FAQ del mismo post, con los mismos datos fijados, salió bien. La pasada
  adversarial contra los DATOS FIJADOS, valor a valor, no es opcional.
- **Un build verde NO garantiza emisión** (memoria `build-verde-no-emite`):
  tras `rm -rf .astro dist`, el primer build salió verde con 1.253 páginas SIN
  los dos .md recién escritos; el segundo, idéntico, emitió 1.255. Gate doble:
  comparar recuento `N page(s) built` + `ls` de las URLs nuevas en `dist`.
- **Imágenes: 4 reintentos cazados A OJO** (la regla 6 del roadmap IT paga):
  display en Fahrenheit (172 °F donde debía leer 75 °C), etiquetas «CHICKEN
  STOCK» en inglés, «SALSA POHODORO», y un frigo con los crudos ENCIMA de las
  verduras — ilustraba lo contrario del texto, el clon del fallo del post 1.
- **Las reglas de research NO viajan entre mercados** — cada roadmap lleva las
  suyas medidas. Las que reordenan: el coste se busca como «fiche technique»
  (FR), «Wareneinsatz» (DE, food cost muerto ×20) y NO se busca (NL, 40/mes);
  «segurança alimentar» PT = food security; «mise en place» = diccionario en
  FR, ETT en NL, préstamo válido en DE (6.600 LOW) y PT (1.930); los acentos/
  guiones a veces agrupan y a veces no — SIEMPRE mirar la SERIE mensual, no el
  volumen; el PAA vuelve en inglés si la cadena es inglesa (FAQ desde variante
  local); marcas homónimas por todas partes (sosa=futbolista, Mise en Place=ETT,
  Combinação de Sabores=restaurante con los 9 primeros resultados).

## Decisiones que esperan a John

1. **Orden de arranque de los 4 blogs nuevos** — cada uno exige crear su árbol
   `/xx/blog/` (clon de fase 9 IT) antes del post 1. Mi recomendación: FR
   primero (mayor direccionable, 62k/mes y el pilar HACCP de 27.100 LOW), pero
   es SU llamada. DE necesita además decidir el registro Sie/du del blog (los
   spokes fase10 usan Sie).
2. Heredadas del handoff del 15, siguen pendientes: checkouts de `ptapp`/`nlapp`
   sin el plan de 10 € · tier «Guest» de Pickaxe gratis de facto · catálogo
   pentalingüe (54/53 vs 89) · **Google Ads: crear la conversión de COMPRA
   (10 €) — la configurada medía el registro gratuito que ya no existe** ·
   `toolAlergenos.faq[0]` con sanciones sin verificar · cutover de `enblog`
   (`CUTOVER_ENBLOG_PENDIENTE.md`).

## Lo siguiente (mi frente: astro/idiomas/contenidos)

- **Post 6 del blog IT: `mise en place`** — 18.100/mes, el mayor volumen del
  plan. NO se ataca el término desnudo (SERP de sala): se ataca **«le 7 fasi
  della mise en place»** (PAA repetido ×2), cubriendo cocina Y sala como hace
  el AI Overview. Agente: Chef Esecutivo Pro — **pedir a John el nombre/URL
  exacto en itapp** (regla: la plataforma es la fuente, no el repo; solo
  tenemos verificado `id-alergenos-g6b6g-it`).
- **Crear el árbol del primer blog nuevo** (según decisión de John) clonando
  fase 9: `src/pages/xx/blog/` + categoría + RSS + `blogHubHref`/helpers +
  gates `--lang xx`, y arrancar su post 1 con el pipeline de los posts IT.
- Vigilar en GSC el arranque de los posts 4-5 (el pilar hacía 112 impr./semana
  en su primera semana; los satélites 2-3 acaban de entrar al índice).

## Estado del entorno

- Repo limpio tras push, `main` == `origin/main`, HEAD `57cb3e5`.
- Último build local: **1.255 páginas, verde**; producción verificada en vivo
  (posts nuevos en 200, pilar con 5 Questions y enlaces al 4 y al 5,
  enlaces-vivos 206/0).
- `.work/` (gitignorado, SOLO este VPS): research de los 4 mercados
  (`research-{fr,de,pt,nl}.json` estructurado + `research-blog-<lang>.md`
  crudo), artefactos de los posts IT 4-5 (`post4-*/`, `post5-*/` con prompts,
  cuerpos y FAQ), y todo lo previo de fase10/11.
- Workflow del research reanudable: `wf_c64237cb-181` (por si hay que
  re-consultar a un cazador con su caché).
