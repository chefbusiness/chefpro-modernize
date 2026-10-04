# Brief para los traductores (subagentes Sonnet) — Food Truck + Coffee Shop Business Plan Kit (EN)

> Sesión Claude Code, 4-oct-2026. F2, paso 2 y paso 4 de la SPEC §7. Regla 1bis: los textos de producto los escriben
> subagentes Anthropic, **nunca bridge.py**. Carpeta de trabajo (worktree del Mac):
> `scripts/productos-digitales/business-plans-en/` (en adelante `BP/`). Cada tanda es **un** subagente. Orden:
> **(a) GM primero** (fija el glosario); luego **(b) GFT** y **(c) GCAF** en paralelo; los docx **(d)-(g)** cuando
> exista `cifras_caso.json` o en paralelo con (b)-(c) (los docx usan tokens: no necesitan las cifras para escribirse).
> Máximo 2 subagentes a la vez (`istats cpu temp` < 62 °C en el Mac).

**Cómo usar este brief**: el orquestador pega al subagente la sección **0** (común) + la sección de su tanda. El
subagente no hace commit (lo hace el orquestador) y no toca ningún otro fichero que su salida.

---

## 0. Reglas comunes (todas las tandas)

**Qué lees** (y nada más, para no gastar contexto):
1. Tu fichero de entrada `BP/tandas/<TANDA>.entrada.json` (compacto: cadenas o párrafos, pistas, glosario,
   pestañas, claves, textos fijados, tokens).
2. `BP/SPEC.md` §0, §1 (decisiones D1-D29), §2.3 (glosario), §3, §4 y §6.
3. `BP/F1-research-us.md` §3, §4, §5 y §7 (cifras US con fuente, marco legal US + notas UK, caso de ejemplo).
4. Solo para GFT/GCAF y los docx: `BP/textos_en/glosario-GM.json` si ya existe (lo deja la tanda GM).

**Qué escribes**: un JSON UTF-8 en la ruta `salida` de tu entrada, con **todas** las claves de tu entrada y ninguna
más (`{"c0123": "…"}` en los xlsx; `{"39": "…"}` en los docx). Comillas del JSON escapadas como `\"`.

**Idioma y tono**: inglés de **EE. UU.**, cercano y claro, de tú a tú («you»), sin jerga corporativa ni traducción
literal. Mercado = **base US con notas UK** solo donde la SPEC las pone (D21-D22, §4.2). El lector es quien abre un food
truck o un coffee shop y quizá enseña el plan a un banco.

**Reglas duras** (las comprueba `check_textos.py`; un error bloquea):
- **Cero español**: ni palabras, ni tildes (salvo café, sauté, entrée, purée, jalapeño, crème brûlée), ni «¿¡«»»,
  ni siglas o normativa española (IVA, SS, SMI, ICO, ENISA, LIS, LIVA, IAE, CCAA, ITV, APPCC, DDD, PRL, RGPD,
  Veri*factu, SL, autónomo, convenio, Hacienda, Seguridad Social, modelo 303, BOE…). Cada trámite español se
  **sustituye** por su equivalente US de la tabla SPEC §4.2 / research §5; si no tiene equivalente, se reescribe o se
  quita. Nunca se traduce el nombre de una ley u organismo español.
- **Moneda**: en los **xlsx** sin símbolo (D8): «(€)» fuera, «€/mes» → «per month», «12 €» → «12». En el **docx**,
  «$» solo dentro de tokens o en datos de research con su fuente. Nunca «€», «EUR», «euros».
- **Formato US**: punto decimal y coma de miles («0.35 = 35%», «1,234.5»); unidades US (sq ft, gallons, lb).
- **Marca**: AI Chef Pro · aichef.pro. Nunca «ChefBusiness» ni «chefbusiness.co».
- Nunca «SBA minimum», «approval guaranteed», «verified (against the law)»; nunca historia de versiones («v1.1»,
  «the previous version», «now», «before»): la EN nace en 2.2 (D18).
- **Cifras del caso ES prohibidas** (12 €, 45 clientes, 250 días, 9,80 €, 100 clientes, 17.094 €, 33 %, 14 pagas,
  73.000 €, 27 clientes…). En los xlsx, si una nota cita el valor de su fila, usa `valor_us` de tu entrada (el caso US
  que escribirá `aplicar_en.py`) o redacta sin cifra. En el docx, las cifras del plan **solo** como tokens `{{…}}`.
- Sin caracteres no latinos; sin IDs internos (SPEC, D9, E2, [kit estimate], research).
- Pestañas y valores citados: con su nombre EN entre **comillas dobles rectas** ("0. Assumptions", "Staffing",
  "Yes"). Las tienes en `pestanas_es_en` y `claves_es_en`; los rótulos ya fijados por la SPEC, en `fijos_en`: si los
  citas, con esas mismas palabras.

**Glosario** (`glosario` de tu entrada; el del financial-kit manda): ventas → sales · facturación → revenue ·
inversión inicial → startup costs · fondo de maniobra → working capital · carencia → interest-only period ·
amortización (activo) → depreciation · amortización (préstamo) → principal repaid · cuadro de amortización →
amortization schedule · cargas de empresa → employer payroll taxes · pagas → pay periods · aparcamiento y base del
vehículo → commissary & truck parking · venta ambulante → mobile vending · gestor/gestoría → accountant / bookkeeper ·
gestor de residuos → licensed waste / grease hauler · carnet de manipulador → food handler card · APPCC →
HACCP-based food safety plan · registro sanitario → health permit · DDD → pest control · ticket medio → average check ·
PVP con IVA → menu price incl. sales tax · «sin IVA» → «excl. sales tax» · TPV → POS · RRSS → social media.

**Validación (obligatoria antes de terminar)**, en el Mac (solo JSON, sin carga):

```bash
istats cpu temp | head -1
python3 scripts/productos-digitales/business-plans-en/check_textos.py --tanda <TANDA>
```

Itera hasta `OK (0 errores, …)`. Revisa los AVISOS (longitud, palabras de oficio sospechosas) y corrige los que sean
reales. Al terminar, responde al orquestador solo con: fichero escrito, nº de claves, resultado del check y 3-5
decisiones de traducción que el resto de tandas deba conocer.

---

## (a) Tanda GM — xlsx, cadenas comunes a FT y CAF (427 cadenas · ≈ 4.600 palabras)

- Entrada `BP/tandas/GM.entrada.json` · salida `BP/textos_en/GM.json` · check `--tanda GM`.
- Son los rótulos y notas del **motor común** (las 9 hojas del plan financiero) y el molde común de los checklists
  (cabeceras, contador, Instrucciones). Se traducen una vez para los dos productos: **no** escribas «food truck» ni
  «coffee shop» en ellas (valen para los dos).
- **Límites de Excel**: las cadenas con `max_len` son títulos (≤ 32) y mensajes (≤ 255) de validación de datos.
  Mensajes con punto decimal («Enter a percentage between 0 and 1 (0.35 = 35%).»).
- Decisiones que te tocan (detalle en SPEC §1): D9 sales tax (P&L **excl.** sales tax; cash flow **incl.** lo cobrado;
  liquidación trimestral «quarterly filer»; mensual → nota); D10 «effective income tax rate» y «net operating losses»
  (federal: hasta el 80 % de la base; el modelo compensa el 100 %: dilo como simplificación); D11 «employer payroll
  taxes» ≈ 10 %, 12 pay periods (las extras solo si > 12: «only if pay periods > 12»), suelo = mayor entre el mínimo
  federal y el estatal/local, 40 h (FLSA), 50 semanas, propinas no modeladas; D12 depreciation lineal de libros
  (MACRS / Section 179 solo en nota); D13 «lender», SBA 7(a), tipo «not APR», DSCR 1.15× / 1.25× **sin «SBA minimum»**,
  aportación propia: «lenders usually expect an owner equity injection (often around 10% for SBA start-ups; many want
  20-30%)»; D16 los umbrales del P&L se presentan como «kit benchmark (editable estimate)»; D17 la nota del DSCR del
  año 1 se conserva (avisa si el usuario pone interest-only); D21 nada (el aviso legal lo escribe mapas).
- Los ratios auditados «CUMPLE/REVISAR» ya son «OK/REVIEW»; «Sí/No» → «Yes/No» (no están en tu fichero).
- Al terminar, escribe además `BP/textos_en/glosario-GM.json`: `{término ES: término EN}` con los términos que hayas
  fijado y no estén en el glosario (≤ 40 entradas). GFT y GCAF lo leen.

## (b) Tanda GFT — xlsx, solo food truck (365 cadenas · ≈ 5.200 palabras; 124 son celdas de tabla)

- Entrada `BP/tandas/GFT.entrada.json` · salida `BP/textos_en/GFT.json` · check `--tanda GFT`. Lee antes
  `textos_en/glosario-GM.json`.
- **Plan financiero FT** — partidas en las MISMAS filas, con el rótulo US del caso de research §7 (el valor lo pone
  `aplicar_en.py`; tú escribes rótulo y nota):
  - `Inversión Inicial` filas 7-20: 7 used food truck · 8 build-out and wrap · 9 kitchen and refrigeration equipment
    · 10 generator · 11 propane system and fire suppression · 12 fresh / gray water tanks and handwashing sinks
    (litros → galones: «check your county») · 13 LLC formation and legal · 14 first-year permits and licenses · 15
    health plan review and drawings · 16 POS and card reader · 17 smallwares and packaging · 18 opening inventory ·
    19 launch marketing · 20 awning, folding tables and banners. Notas de la col. D sin cifras ES; la de la col. E
    «¿Lleva IVA?» es común (GM).
  - `PyG 3 Años` fijos filas 26-35: annual permits · truck maintenance and inspections · marketing · accounting /
    bookkeeping · software (POS, website, social) · cleaning supplies · waste and grease disposal · pest control ·
    **training and certifications** (fila 34, en el ES era prevención de riesgos) · **music licensing (ASCAP, BMI,
    SESAC)** (fila 35). Fila 22 = «Commissary & truck parking». Comentarios de umbral (F51-F56): «kit benchmark
    (editable estimate)», sin citar la tabla «Fichero v1.1».
  - `Personal` filas 5-8: owner (chef, manager and driver) 1.0 FTE · cook-cashier 0.8 · events and festival help
    0.15 · vacation and day-off relief 0.06. Notas sin «30 días de vacaciones» ni Estatuto: US no fija vacaciones por
    ley federal; FLSA para horas extra.
  - `0. Supuestos`: B24 es commissary + parking (no hay local); B25 fianza 1 mes; notas con `valor_us`.
- **Tablas de Instrucciones celda a celda** (`por_celda: true`, un id por celda; filas 35-51 = D18 y 55-68 = D19):
  - **D18 «WHY THIS MODEL IS BUILT THIS WAY»** (Topic | Common shortcut | This workbook | Why): cada fila explica el
    atajo que suelen tomar las plantillas típicas (col. B), lo que hace este libro (col. C) y por qué (col. D). **Sin**
    «v1.1», sin cifras del caso (cambian al recalcular: describe el método), sin normativa ES. Las filas de «Impuesto
    de Sociedades» y «Sueldos y SMI» pasan a income tax / minimum wage US.
  - **D19 «INDUSTRY BENCHMARKS»** (Benchmark | Value | Source | Note): Value = rango US de research §4/§3 en formato
    US («28-35%», «10-15», sin «$»: es xlsx); Source = dominio de la fuente de research («Toast (pos.toasttab.com)»,
    «BizBuySell», «beancount.io», «7shifts», «Kit estimate»…), **nunca** «Fichero v1.1» ni «BOE»; Note breve. Si
    research no tiene la fila (p. ej. «Servicios por día»), Value razonable + «Kit estimate». Fila de convenio →
    «Minimum wage» / «Federal $7.25/h; your state or city may be higher» / «DOL (dol.gov)».
- **Checklist FT** (D24): misma tarea por fila (11/13/12/10/12/10), equivalente US de SPEC §4.2: col. B trámite, C
  responsable (Owner, Accountant, Attorney, Health department, City, DMV, Insurance agent, Fire marshal…), D plazo
  realista US («Same day (online)», «2-6 weeks»…), E nota; la nota UK, si aplica, al final de la col. E de la fila
  equivalente (registro en el council 28 días antes, street trading licence, Food Hygiene Rating 1-5, 14 alérgenos).
  Las hojas de reclamaciones (F2) → **commissary agreement**; ITV/carnet → DMV / CDL solo si GVWR ≥ 26,001 lb + fire
  marshal. Títulos de fase coherentes con las pestañas EN («PHASE 2: TRUCK & PERMITS»). A3 (afirmación «verificado»)
  no existe en EN: el checklist es «a starting point».

## (c) Tanda GCAF — xlsx, solo cafetería (418 cadenas · ≈ 4.400 palabras; 127 son celdas de tabla)

- Entrada `BP/tandas/GCAF.entrada.json` · salida `BP/textos_en/GCAF.json` · check `--tanda GCAF`. Lee antes
  `textos_en/glosario-GM.json`. El concepto es «coffee shop with brunch» (D2).
- **Plan financiero CAF**:
  - `Inversión Inicial` filas 7-29: 7 LLC formation and legal · 8 licenses and health plan review · 9 architect and
    building permits · 10 construction / build-out · 11 electrical and HVAC · 12 plumbing (grease interceptor, floor
    drains, handwashing sinks) · 13 coffee grinders · 14 oven · 15 refrigerated display case · 16 refrigeration · 17
    griddle / panini press · 18 blenders, juicer, toaster · 19 commercial dishwasher · 20 dining room furniture · 21
    counter and pastry display · 22 patio / sidewalk seating · 23 smallwares, cups and glassware · 24 decor and
    lighting · 25 signage · 26 launch marketing · 27 opening inventory · 28 espresso machine (2 groups) · 29 POS and
    software. Notas sin m² (→ sq ft), sin «licencia inocua», sin marcas (A8 de la SPEC: «with reference prices»).
  - `PyG 3 Años` fijos filas 26-34: accounting / bookkeeping · equipment maintenance · marketing · software · cleaning
    · waste and recycling · pest control · music licensing (ASCAP, BMI, SESAC) · **training and certifications** (fila
    34). Fila 22 = «Rent». Comentarios de umbral: «kit benchmark (editable estimate)».
  - `Personal` filas 5-10: owner-barista 1.0 · morning barista 1.0 · afternoon barista-server 1.0 · brunch cook 0.8 ·
    weekend extra 0.45 · vacation and day-off relief 0.1.
  - `0. Supuestos` C50 la escribe mapas (fórmula); B51 aforo «seats (tables + bar)».
- **Tablas D18 (filas 36-50) y D19 (filas 54-70)**: mismas reglas que GFT; ticket coffee shop $7.81-$11.11 (sin «$»
  en el xlsx), clientes/día 100-250, ocupación 10 % objetivo / 15 % máximo [AU → «Kit estimate» para US], mercancía
  25-35 %, personal 30-35 % (alarma > 40 %), neto 8-12 %. «Rotación por franja horaria» no existe (A9): no la inventes.
  Filas de convenio y SMI → mínimo federal $7.25/h + estatal/local (DOL), sin «2026» ni «BOE».
- **Checklist CAF** (11/13/15/12/14/10): como GFT con las equivalencias de local de SPEC §4.2: zoning check antes de
  firmar, building permits, certificate of occupancy, sidewalk café permit, commercial lease review (NNN/CAM, personal
  guarantee), general liability + BOP, liquor license solo si sirves alcohol.

---

## Docx — reglas comunes de las tandas (d)-(g)

- Entrada `BP/tandas/<tanda>.entrada.json`; salida `BP/docx_en_<tanda>.json` = `{"<i>": "<párrafo EN>"}` con TODOS los
  `i` de `parrafos`. Check `--tanda <tanda>`.
- **Párrafo a párrafo** (D22): cada párrafo EN conserva el papel y la idea del ES adaptados a EE. UU., con longitud
  parecida (0.6-1.5×). Texto plano: sin listas, viñetas, markdown ni saltos de línea. `rol: subtitulo` = una línea en
  Title Case, < 80 caracteres, sin punto final.
- **No escribes** portada, aviso legal, índice, encabezados «N. …» ni el cierre: los pone `ensamblar_docx.py`
  (D22-D23; los ves en `fijos_que_no_escribes`). Tampoco el separador «━━━».
- Voz del plan: «we» (el equipo promotor) y el lector lo adapta a su negocio. Marca: AI Chef Pro (nunca
  ChefBusiness).
- **Cifras del plan = tokens** `{{nombre}}` de `tokens` de tu entrada (minúsculas exactas). El ensamblador las
  rellena desde el xlsx EN recalculado (D22: se acaba la contradicción docx ↔ Excel). Ejemplos: «We project year-1
  revenue of {{ventas_a1}} ({{clientes_dia}} customers a day at an average check of {{ticket}}, {{dias}} days a
  year)»; «a payback of {{payback}}» (el token ya trae «years» o «more than 3 years»); «a pre-tax result of
  {{pesimista_resultado}}» (puede salir negativo: no escribas «a loss of»). Cash break-even = «cash break-even (loan
  payments in, depreciation out)»: {{equilibrio_caja_clientes_dia}} (A2 de la SPEC).
- **Datos de mercado**: solo los de research §3-§5 nombrando la fuente en el texto («according to Toast», «Homebase
  puts…») o en redacción cualitativa. Las cifras marcadas «(resumen)» en research solo si abres la página con
  WebFetch y la cifra está; si no, sin cifra. Los hechos legales de research §5 (9 alérgenos, CDL 26,001 lb, $7.25/h,
  28 días UK…) se pueden afirmar nombrando el organismo, sin URL. **Nada inventado**: ni «23 % de crecimiento», ni
  «2.500 food trucks», ni ciudades o mercados españoles. El check rechaza importes «$» y porcentajes que no sean token
  ni estén en research/SPEC.
- Notas por párrafo (`nota`): mandan sobre esta sección.

## (d) Tanda ft_a — docx FT §1-§5 (29 párrafos · ≈ 2.950 palabras)

- §1 Executive Summary: oportunidad de mercado, concepto, inversión ({{inversion_total}}, {{necesidad_caja}}), financiación ({{fondos_propios}} +
  {{prestamo}} SBA 7(a), «lender-ready, approval not guaranteed»), ventas y resultado (tokens), equipo
  ({{plantilla_puestos}} people, {{plantilla_jornadas}} FTE). §2 Concept & Value Proposition (el ES cita «45,000 to
  85,000 euros»: usa {{capex}}, o el rango de Homebase $100,000-$250,000 nombrando la fuente solo si lo confirmas con
  WebFetch — research lo marca «resumen»). §3 Market Analysis: hábitos,
  canales (offices, breweries, events, catering), regulación por ciudad, tendencias — cualitativo o research. §4
  Competitive Analysis: otros trucks, quick service, Porter/SWOT, barreras = permisos por ciudad y commissary. §5
  Marketing Plan: Instagram/TikTok, Google Business Profile, Yelp, Roaming Hunger / StreetFoodFinder, catering y
  eventos, fidelización por QR; presupuesto {{marketing_anual}}.

## (e) Tanda ft_b — docx FT §6-§10 (32 párrafos · ≈ 3.750 palabras)

- §6 Operations Plan: truck ({{inv_vehiculo}}, {{inv_adaptacion}}), equipo ({{inv_equipo_cocina}},
  {{inv_generador}}), commissary + parking ({{alquiler_mes}} al mes), logística diaria, inventario, mantenimiento. §7
  Management & Staffing: plantilla con tokens ({{personal_a1}}, {{personal_pct}}, {{cargas_pct}} de payroll taxes,
  {{salario_minimo_federal}} suelo federal anual, {{horas_semana}} h), contratación W-2 vs 1099, formación (food
  handler, CFPM). §8 Financial Plan: SOLO tokens (inversión, ventas años 1-3, COGS, margen, EBITDA, resultado,
  equilibrio contable y de caja, holgura, DSCR mínimo vs objetivo {{dscr_objetivo}}, saldo mínimo y su mes, payback,
  escenarios). §9 Legal Requirements, Permits & Licenses: **7 párrafos en el orden de las notas** (102-108); el 108
  cierra con la nota UK. §10 Conclusions & Action Plan: riesgos, fortalezas, hoja de ruta por fases con los nombres de
  las pestañas del checklist EN («Phase 1 - Business Setup»…), KPIs semanales (sin cifras inventadas: usa tokens).

## (f) Tanda caf_a — docx CAF §1-§5 (47 párrafos · ≈ 3.050 palabras)

- Coffee shop with brunch. §1 con tokens ({{inversion_total}}, {{ventas_a1}}, {{clientes_dia}}, {{ticket}},
  {{equilibrio_clientes_dia}}, {{prestamo}}, {{dscr_min}}). Los subtítulos (`rol: subtitulo`) en Title Case. §3 y §4
  sin «210,000 cafeterías en España» ni datos españoles: specialty coffee y brunch en EE. UU. de forma cualitativa
  o con research (Toast: $80,000-$300,000 de inversión, solo tras confirmarlo con WebFetch: research lo marca
  «resumen»). §5 Marketing Plan con Google Business Profile, Yelp, Instagram, Resy/OpenTable si hay reservas de brunch,
  DoorDash / Uber Eats; presupuesto {{marketing_anual}}.

## (g) Tanda caf_b — docx CAF §6-§10 (47 párrafos · ≈ 3.150 palabras)

- **Movimiento del bloque financiero** (defecto del ES): en el ES, §7 contiene el plan financiero (110-119) y §8 dice
  «[Contenido pendiente de generacion]» (134). El ensamblador deja §7 = 108-109 + 120-131 y §8 = 110 (subtítulo
  «Financial Plan at a Glance»), **134 (resumen nuevo, solo con tokens)**, 111-119. Escribe cada uno para el sitio
  donde va a quedar (notas de la entrada).
- §6 Operations Plan (espresso {{inv_espresso}}, obra {{inv_obra}}, aforo {{aforo}} seats, rotaciones
  {{rotaciones_dia}}); §7 Management & Staffing (perfiles, salarios con tokens y suelo federal/estatal, turnos 40 h,
  formación SCA sin cifras inventadas); §8 como arriba; §9 Legal: **6 párrafos en el orden de las notas** (137-142),
  el 142 cierra con la nota UK; §10 Conclusions & Action Plan (inversión con tokens, no «70.000 a 120.000 euros»).

---

## Después de las 7 tandas (orquestador)

```bash
python3 scripts/productos-digitales/business-plans-en/check_textos.py --todas      # 7 × OK
```

Luego la tanda de `aplicar_en.py` (opus, VPS) consume `textos_en/{GM,GFT,GCAF}.json`, genera `cifras_caso.json` y
llama a `ensamblar_docx.py` con `docx_en_*.json` (F2-NOTAS §5).
