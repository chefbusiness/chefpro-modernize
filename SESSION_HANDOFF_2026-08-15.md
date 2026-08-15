# Session Handoff — 2026-08-14/15 → siguiente sesión

## TL;DR

Maratón de dos jornadas encadenadas con TRES entregas mayores, todas en
producción y verificadas en vivo:

1. **Los 7 idiomas del sitio quedan homologados.** FR, DE, PT y NL pasaron por
   el pipeline fase10 (el del italiano del 08-08, ahora COMMITEADO): 51 spokes
   cada uno, glosarios medidos contra las plataformas vivas, hubs a paridad
   67/67 con el español y los 5 gates VERDES (`fase10-gate-idioma.py --lang
   fr|de|pt|nl` + `fase9-gate-italiano.py`).
2. **AI Chef Miembro dejó de ser gratis: 10 €/mes con 10.000 créditos** en los
   7 idiomas (decisión de John). Barrido fase11 en locales, spokes, las 7
   páginas de precios hardcodeadas, ~230 posts del blog, JSON-LD y el banner
   promocional que llevaba «PRUEBA GRATIS» y «55+» pintados EN LOS PÍXELES
   (468 referencias, un solo jpeg pisado en su misma ruta). Leitmotiv 55+ →
   **75+ (es/en) y 50+ (it/fr/de/pt/nl)** — la asimetría es a propósito: esas
   plataformas sirven 53-54 agentes de los 89 del español.
3. **Blog italiano: posts 2 y 3 publicados** (`contaminazione-crociata` 1.600/mes
   y `etichettatura-allergeni` 880/mes + clúster 2.280). El triángulo
   pilar ↔ post 2 ↔ post 3 quedó interenlazado. El pilar ya hace 112
   impresiones/semana en su primera semana.

De propina, un **hotfix con nombre y apellidos**: la cookie `preferred-lang`
se sembraba con la VISITA a cualquier URL con prefijo de idioma (no con la
elección), así que abrir un enlace italiano secuestraba la raíz `/` un año —
le pasó a John revisando el blog IT. Corregido en hook + selector del Header
(`a968fd9`).

**HEAD**: `2e947f0` · sitemap reenviado a GSC y descargado por Google el 15 a
las 17:18 (*Valid*, 0 errores, 1.127 URLs indexadas del index).

## Commits de la sesión (todos pusheados, deploy verde)

| Commit | Qué |
|---|---|
| `c775a86` | Post 2 IT (contaminazione crociata) |
| `a968fd9` | Hotfix cookie `preferred-lang` (visita ≠ elección) |
| `ceeac92` | Tooling fase10 commiteado (driver + glosario fr + gate multi-idioma) |
| `36049d0` | **Plan Miembro 10 €** — barrido principal 7 idiomas + blog + banner |
| `4b978dd` | **Homologación FRANCESA** (51/51, hub 43→67 tarjetas) |
| `e601ba4` | Cola larga del blog (~200 posts reescritos con bridge) + 5 componentes con copy hardcodeado |
| `cd96e88` | Auditoría adversarial: los GEMELOS SPA de las landings aún prometían 3.000 créditos (24 páginas) |
| `2015f39` | Post 3 IT (etichettatura allergeni) |
| `542e1db` | **Homologación ALEMANA** (Sie-Form, morfología y elipsis documentadas) |
| `2e947f0` | **PORTUGUÉS + NEERLANDÉS** — los 7 completos |

## Lo que la sesión deja como MÉTODO (no repetir el aprendizaje)

- **Pipeline fase10** (`fase10-traducir-spokes.py` + `fase10-glosario-<lang>.json`
  + `fase10-allowlist-<lang>.json` + `fase10-gate-idioma.py`): traduce con
  bridge `--strict-lang`, valida glosario/protegidos/marcadores por idioma,
  es resumable por spoke en `.work/fase10-<lang>/` y emite el `.ts`. Trampas ya
  pagadas: préstamos de cocina por idioma (ají, huancaína, Chuletón, Roscón,
  Taquería — y en alemán CAPITALIZAN), elipsis de nombres compuestos («Cocina
  Argentina + Brasileña» es elíptico también en destino), morfología alemana
  (nombres flexionados → entrecomillar en nominativo), spokes gigantes por
  mitades/cuartos cuando bridge devuelve vacío, el campo `h1` en el regex de
  rutas, la allowlist se enmascara ANTES que los protegidos y de largo a corto,
  y el chequeo de glosario ignora lo que viva dentro de un literal protegido.
  **El piloto NL salió en dialecto limburgués («AI veur Pizzeria»)** — mirar
  los h1 del emit siempre.
- **Barrido fase11** (`fase11-plan-miembro-{locales,spokes,blog}.py` +
  `blog-cola`): reutilizable cuando John quite el gratis de otros SaaS.
  Exentos A PROPÓSITO: free tools de la web, Miselup y Timlup (anclar
  reemplazos por href — un replace sin anclar se llevó 25 CTAs de Miselup y
  hubo que revertirlo). El validador es fail-closed con listas KEEP explícitas.
- **La «vía 3» (copy hardcodeado) tiene más superficie de la que parece**: 5
  componentes de página con bloques por idioma (UseCasePageContent,
  UseCasesHubPage, ConsultoriaGastroProHubPage, PSeoCitiesHubPage,
  PSeoCityPageContent) **y sus gemelos SPA** — el `.astro` corregido no basta,
  el `.tsx` renderiza como island. Igual con los locales: solo un recorrido
  CON LISTAS (como `hojas()` del gate) ve los arrays (keywords de alérgenos,
  FAQs de tools).

## Decisiones que esperan a John

1. **Checkouts de `ptapp` y `nlapp`** — los únicos sin el plan de 10 €/10.000
   (medido en su payload; los otros 5 ya lo sirven). Los checkouts son SUYOS.
2. **El tier «Guest» de Pickaxe sigue gratis** (200 créditos/mes en `app`,
   `limit:-1337` en pt/nl) — tras el cambio es el gratis de facto. ¿Demo
   deliberada o entra en la purga?
3. **Catálogo pentalingüe**: it 54 · fr/de/pt/nl 53 agentes frente a 89 ES.
   Cuando los iguale, el «50+» de esos 5 idiomas pasa a «75+» (1 parámetro en
   `Hero.astro`/`SocialProofStrip.astro` + locales).
4. **Google Ads**: la conversión configurada medía el registro GRATUITO, que
   ya no existe — crear la acción de compra (10 €) sobre el success de Stripe
   y degradar la vieja antes de que la campaña optimice a una señal muerta.
5. **`toolAlergenos.faq[0]`** cita «sanciones de entre 3.000€ y 600.000€» en 7
   idiomas — afirmación legal preexistente sin verificar contra la norma real.
6. El cutover de `enblog` de siempre (`CUTOVER_ENBLOG_PENDIENTE.md`).

## Lo siguiente (mi frente: astro/idiomas/contenidos)

- **Posts 4-5 del blog italiano**: `7 principi haccp` (390/mes) y
  `temperature frigorifero haccp` (260/mes) — cierran el clúster; el research
  crudo sigue en `.work/research-blog-italiano.md` (solo en este VPS).
- **Blogs fr/de/pt/nl**: cada uno exige su keyword research nacional ANTES de
  escribir nada (`dataforseo.py` con `--pais/--idioma` explícitos; el default
  es España y ya quemó una tanda una vez).
- Vigilar el arranque GSC de los árboles nuevos (fr ya venía plano en ~15
  impresiones/día; it multiplicó ×5 en una semana tras su homologación).

## Estado del entorno

- Repo limpio tras el push final, `main` == `origin/main`.
- Último build: **1.253 páginas, verde**. Los 5 gates de idioma VERDES.
- Producción verificada en vivo: pt/nl/de con 0 restos de castellano en los
  spokes muestreados; plan de 10 € servido en home y las 7 páginas de precios.
- `.work/` (gitignorado, SOLO este VPS): research italiano, artefactos
  fase10 de los 4 idiomas (`*.ok.json` = fuente de reemisión), copys fase11.
