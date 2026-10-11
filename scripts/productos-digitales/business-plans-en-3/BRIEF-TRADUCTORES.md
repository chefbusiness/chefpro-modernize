# Brief para los traductores (subagentes Sonnet) — Bar Business Plan Kit (EN)

> Sesión Claude Code, 11-oct-2026. F2 del producto 11 de la tienda EN (SPEC delta §7 pasos 2-3). Regla 1bis: los
> textos de producto los escriben subagentes Anthropic, **nunca bridge.py**. Carpetas (worktree del Mac):
> `scripts/productos-digitales/business-plans-en-3/` (= `BP3/`, datos y salidas del bar),
> `scripts/productos-digitales/business-plans-en-2/` (= `BP2/`, restaurante + panadería) y
> `scripts/productos-digitales/business-plans-en/` (= `BP/`, el código común y el brief de FT/CAF).
>
> **Cuatro tandas**, máximo 2 subagentes a la vez (`istats cpu temp` < 62 °C en el Mac):
> **tanda 1 = (a) GBAR-plan ‖ (b) GBAR-check** → **tanda 2 = (c) bar_a ‖ (d) bar_b**.
> Los docx usan tokens: pueden ir en paralelo con la tanda 1 si hay hueco térmico; no necesitan las cifras.
> **GM y GR no se traducen**: sus 397 + 97 cadenas son idénticas a otras ya traducidas (FT/CAF, REST/PAN) y su EN ya
> está en `BP3/textos_en/GM.json` y `GR.json` (los escribe `bp3.py preparar_tandas`). GR se **revisa** en la tanda (b).

**Cómo usar este brief**: el orquestador pega al subagente la sección **0 de `BP/BRIEF-TRADUCTORES.md`** (reglas
comunes: idioma, cero español, moneda, formato US, marca, cifras, pestañas citadas, glosario) + la sección **0** de
este fichero + la de su tanda. El subagente no hace commit y no toca nada más que su salida.

---

## 0. Lo que cambia frente a los briefs de FT/CAF y REST/PAN (manda sobre ellos en lo que choque)

**Qué lees** (y nada más): tu entrada `BP3/tandas/<TANDA>.entrada.json`; `BP3/SPEC-delta.md` (D48-D65);
`BP3/F1-research-us-delta.md` §1, §4, §5, §6 y §8; de lo heredado, solo lo que tu entrada cite (`BP/SPEC.md` §1-§4,
`BP2/SPEC-delta.md` D37-D38, `BP2/F1-research-us-delta.md` §3-§5); `BP/textos_en/glosario-GM.json`.

**Validación** (en el Mac, solo JSON):

```bash
istats cpu temp | head -1
python3 scripts/productos-digitales/business-plans-en-3/bp3.py check_textos --tanda <TANDA>
```

Itera hasta `OK (0 errores, …)` y revisa los AVISOS reales (longitud EN/ES, «oficio»). Responde solo con: fichero
escrito, nº de claves, resultado del check y 3-5 decisiones que deban conocer las demás tandas.

**Concepto (D51): NEIGHBORHOOD BAR WITH SMALL PLATES.** Un bar de barrio con cócteles, cerveza de grifo (draft) y vino,
y una cocina corta de **small plates** para compartir; **~65 % de las ventas en bebida**, 60 plazas (14 en barra) +
patio, abierto 7 días de tarde a noche. «Tapas» solo como **«small plates (tapas-style)»** y solo la primera vez en el
docx; **nunca «tapas bar» ni «gastrobar»** (el check lo rechaza). No es un nightclub (puerta, DJ, aforo, sin cocina) ni
una brewery (fabricación con licencia federal TTB). No canibaliza al Restaurant Business Plan Kit (comida 70 / bebida
30, servicio de mesa): aquí manda el **coste de bebida (pour cost)** y la **licencia de alcohol es el camino crítico**.

**Volumen diario = covers (D55).** El libro dice **«covers»** (24 cadenas reutilizadas del restaurante, sin retocar);
en el docx y la landing, **«guests (covers)»** la primera vez y «covers» después. Rotación = **seat turns**. Nunca
«customers» para el volumen.

**Licencia de alcohol (D54, D57, D60).** Agencia estatal (ABC / control board) + aprobación local; clases **beer & wine**
(desde ~$3,000) y **full liquor** ($12,000-$400,000); en **estados con cupo** se compra o transfiere una licencia
existente a precio de mercado (un orden de magnitud más: Boston > $450,000). El libro presupuesta **un estado SIN
cupo** (fila 8 de `Startup Costs`, rótulo fijado «Liquor license + local permits (non-quota state example)»). Se pide
**al firmar el local** (fase 2 del checklist), **a menudo 3-12 meses**; nunca «un trámite de un día». Una licencia
comprada a otro dueño es un activo intangible: **«ask your CPA»**. Ninguna cifra por estado inventada.

**Dram shop / liquor liability.** El local puede responder del daño que cause un cliente servido en exceso; lo cubre el
seguro de liquor liability (mediana **$2,039/año** en bares pequeños, Insureon; el caso presupuesta $12,000/año de
general + liquor liability + property). Formación de **servicio responsable (TIPS / ServSafe Alcohol)** y control de
edad. Impuesto del alcohol servido (D57): `0. Assumptions!C63` ya está fijado con el ejemplo de Texas.

**Propinas (D38).** El libro **no modela tip credit**: bartenders, barbacks y servers con salario base ≥ $15/h; federal
$2.13/h + tip credit hasta $5.12 donde el estado lo permite; CA, OR, WA, AK, MN, MT y NV no lo permiten (DOL). La nota
de `Staffing!A29` ya lo dice (fijada).

**Cifras del caso ES PROHIBIDAS (D52; `check_textos` las rechaza, también en GR):** 302.400 · 153.327 · 109.450 ·
174.317 · 129.000 · 50.000 (salvo el «up to $50,000» del SBA Microloan) · 17.094 · 115.000 · 270.000 · «34 clientes» ·
«14 pagas» · «33 %» de Seguridad Social; y las del docx ES (1,8 servicios, 12.000 € de fondo de maniobra, 320.000 /
370.000, retorno 18-30 meses, 100.000-140.000 € habituales). Usa `valor_us` (caso US: **95 covers × $27 sin sales tax ×
360 días**, bebida 65 %, alcohol 90 % de la bebida, pour cost 22 %, comida 30 %, alquiler $6,500/mes) o redacta sin
cifra: el caso se recalibra en la tanda de `aplicar_en.py` y una nota con cifra puede quedarse vieja.

**Rótulos fijados** (`fijos_en` de tu entrada, ya los escribe `mapas.py`; si los citas, con esas mismas palabras):
- `Startup Costs` filas 7-24 (D54): LLC formation + legal · Liquor license + local permits (non-quota state example) ·
  Architect, MEP drawings + permit fees · Build-out (second-generation space) · Electrical + HVAC · Plumbing, grease
  interceptor + Type I hood · Kitchen equipment (griddle, fryer, oven) · Refrigeration (walk-in + back-bar coolers) · Bar
  build (bar top + underbar stations) · Draft beer system + installation · Furniture (tables, high-tops + bar stools) ·
  Patio (furniture + awning) · Glassware, smallwares + tableware · Decor, lighting + sound · Exterior signage · Launch
  marketing · Opening inventory (liquor, beer, wine + food) · POS + handhelds + software. Títulos A1-A3 sin «España».
- `3-Year P&L` (D55): A2 «Base case — neighborhood bar with small plates, 60 seats»; A10 «Food sales (small plates)»;
  A11 «Beverage sales (cocktails, beer, wine + non-alcoholic)»; fijos A25-A34 (Insurance (general + liquor liability +
  property) · Accounting + bookkeeping · Equipment maintenance · (fila 28, marketing: la del motor, GM) · Software
  (POS, reservations, inventory) ·
  Cleaning supplies + linens · Waste + grease hauling · Pest control · Music licensing (ASCAP/BMI/SESAC) · Safety +
  responsible-service training).
- `Staffing` A5-A11 (D55): Owner / general manager · Kitchen lead · Bartenders (peak shifts) · Servers (floor & patio) ·
  Line / prep cook · Barback / weekend extra · Relief cover (vacations + days off).
- Checklist: títulos «BAR OPENING CHECKLIST — NEIGHBORHOOD BAR WITH SMALL PLATES», «PHASE 2: LOCATION & LICENSES»;
  F2-8 responsable «Owner + attorney» y plazo «Start right after signing the lease: often 3-12 months»; F2-11 «General
  liability + liquor liability (dram shop) insurance»; F2-14 «Required public notices posted (health permit, liquor
  license, labor law posters)».
- Pestañas (D53): «0. Assumptions», «Startup Costs», «3-Year P&L», «Break-Even», «Scenarios», «Staffing»,
  «Instructions», «12-Month Cash Flow», «Financing» · checklist «Phase 1 - Business Setup», «Phase 2 - Location &
  Licenses», «Phase 3 - Build-Out & Equipment», «Phase 4 - Staff», «Phase 5 - Marketing», «Phase 6 - First 90 Days».

**Glosario del bar** (en tu entrada, sobre el de FT/CAF y el del financial-kit, que mandan): cubiertos → covers ·
tapas/raciones → small plates · barra → bar · camarero de barra → bartender · ayudante de barra → barback · terraza →
patio / sidewalk café · grifos → draft beer system / taps · tiraje → pouring / draft service · coste de bebida → pour
cost / beverage cost · licencia de alcohol → liquor license · RC por alcohol → liquor liability (dram shop) insurance ·
distribuidor → licensed distributor (three-tier system) · comandero → handheld POS · vermut → vermouth.

**Formato US**: punto decimal y coma de miles, «%» pegado al número, sin símbolo de moneda en el xlsx («in your
currency»), «$» solo en el docx y en rangos de mercado con fuente (research). Pestañas citadas entre comillas dobles
rectas con su nombre EN.

---

## (a) Tanda GBAR-plan — xlsx del plan financiero (191 cadenas · ≈ 2.950 palabras; 128 celdas de tabla)

Entrada `BP3/tandas/GBAR-plan.entrada.json` → salida `BP3/textos_en/GBAR-plan.json` (`{"<id>": "<EN>"}` con TODOS los
ids y nada más). Validación:

```bash
python3 scripts/productos-digitales/business-plans-en-3/bp3.py check_textos --tanda GBAR-plan
```

- **63 cadenas de texto libre (≈ 1.640 palabras)**: notas de la col. C de `0. Assumptions` (sin «v1.1», «el documento
  de este plan», «1,24 servicios», «1,8 en el almuerzo»: describen el caso US con `valor_us` o sin cifra), notas de la
  col. D de `Startup Costs` (pista D54 por fila; la de la fila 8, la nota de la licencia), notas del P&L y de
  `Staffing`, y las filas 1, 11 y 12 de `Instructions` (A12: el Word usa las MISMAS cifras de ejemplo que el libro;
  fuera «versión 1.1»).
- **128 celdas de las tablas de `Instructions`, una por celda** (`por_celda: true`, incluidas las celdas sin letras
  como «28-32 %», que pasan a su valor US):
  - **D18, filas 35-50: «WHY THIS MODEL IS BUILT THIS WAY»** (Topic | Common shortcut | This workbook | Why). Col. B =
    el atajo típico de las plantillas, col. C = lo que hace ESTE libro, col. D = por qué. Sin historia de versiones,
    **sin cifras del caso** (ni ES ni US: cambian al recalibrar), sin normativa española (fila 45: Impuesto de
    Sociedades → «effective income tax rate» y NOL; fila 47: equity + loan sin importes). 17 celdas traen
    `propuesta_en` del mismo ES en otro libro: revísala, vale solo si encaja en esa celda.
  - **D19, filas 54-69: «US INDUSTRY BENCHMARKS»** (Benchmark | Value | Source | Note). **Cada fila cambia según su
    pista D58** (sin propuesta): food cost 25-35 % · pour cost total 18-24 % · cerveza 24 % · personal ≤ 35 % (Kit
    estimate) · alquiler ≤ 10 % (Kit estimate) · ticket $20-$35 (Kit estimate) · destilados 15 % · vino 28 % · seat
    turns 1.5-3 (Kit estimate) · startup $110,000-$550,000 / media $425,500 · liquor license · margen bruto ≥ 68 % (Kit
    benchmark) · liquor liability $2,039/año · reserva operativa $75,000-$100,000 · prime cost 60-65 % · salario mínimo
    federal $7.25/h + el estatal (DOL). `Source` = la fuente que dice la pista o «Kit estimate» / «Kit benchmark
    (editable estimate)»; **nunca «Fichero v1.1»**. Las filas sin fuente del ES (ocupación, merma, consumiciones de
    barra, EBITDA, retorno) desaparecen.
- Umbrales del P&L (D56, ya en el libro): margen bruto ≥ 68 % · mercancía ≤ 28 % · personal ≤ 35 % · alquiler ≤ 10 % ·
  neto ≥ 5 %, «kit benchmark (editable estimate)».

## (b) Tanda GBAR-check — xlsx del checklist (106 cadenas · ≈ 660 palabras) + revisión de las 97 reutilizadas GR

Entrada `BP3/tandas/GBAR-check.entrada.json` → **dos** salidas:

1. `BP3/textos_en/GBAR-check.json` (`{"<id>": "<EN>"}` con TODOS los ids de `cadenas`): las 73 tareas en 6 fases
   (11/13/13/12/14/10, no se añaden ni quitan), col. B trámite, C responsable, D plazo US, E notas. Equivalencias de
   SPEC delta §4 (D60; pista por celda): LLC vs S corp con el contador · EIN + state payroll / unemployment
   registration · POS que reporta el sales tax · zoning check antes de firmar · **liquor license en la fase 2** ·
   sidewalk café / patio permit · entertainment permit (música en vivo o DJ) · noise ordinance · architect + MEP →
   building permits + health plan review · Type I hood + UL 300 (NFPA 96) · grease interceptor · draft system
   instalado por el distribuidor (tied-house rules) · offer letters, I-9, W-4 y el mínimo estatal · new-hire reporting ·
   OSHA basics · bar service + responsible beverage service (TIPS / ServSafe Alcohol) y control de edad · alérgenos +
   Food Code · cuentas con distribuidores (three-tier system) · Google, Yelp, OpenTable / Resy · DoorDash / Uber Eats
   solo para la comida. Sin marcas españolas (Mahou, Estrella), sin «300.000 €» de RC, sin «facturación extra 20-30 %».
2. `BP3/textos_en/GR.revision.json`: revisa la lista `revisar_reutilizadas.GR` de tu entrada (97 cadenas, ≈ 1.050
   palabras: notas del motor, trámites y cubiertos del restaurante, filas de la cafetería). Cada una trae `en_actual`
   (el EN ya publicado en otro kit) y `de`. Si `en_actual` vale para un bar de barrio con small plates, **no la
   incluyas**; si no (un restaurante con servicio de mesa, una cafetería con brunch, un food truck), escribe
   `{"<id>": "<EN corregido>"}`. Si ninguna cambia: `{}`. Después, el orquestador (o tú) corre
   `python3 scripts/productos-digitales/business-plans-en-3/bp3.py preparar_tandas`, que aplica la revisión sobre
   `textos_en/GR.json`.

Validación (las dos):

```bash
python3 scripts/productos-digitales/business-plans-en-3/bp3.py check_textos --tanda GBAR-check
python3 scripts/productos-digitales/business-plans-en-3/bp3.py preparar_tandas && \
python3 scripts/productos-digitales/business-plans-en-3/bp3.py check_textos --tanda GR
```

---

## Docx — reglas comunes de las tandas (c)-(d)

Las de `BP/BRIEF-TRADUCTORES.md` («Docx — reglas comunes»: un párrafo EN por párrafo ES, sin saltos de línea en el
cuerpo, subtítulos de una línea sin punto final, toda cifra del caso con su token `{{…}}`, importes y porcentajes de
mercado solo si están en research/SPEC), más:

- `notas_del_plan` de tu entrada (concepto, covers, cifras del docx ES que contradicen al Excel y NO se traducen,
  I1-BAR) y las `nota` por párrafo mandan.
- Tokens propios del bar: `inv_licencia`, `inv_proyecto`, `inv_obra`, `inv_instalaciones`, `inv_campana`, `inv_cocina`,
  `inv_frio`, `inv_barra`, `inv_grifos`, `inv_mobiliario`, `inv_terraza`, `inv_lanzamiento`, `inv_stock`, `inv_tpv`,
  `aforo`, `rotaciones_dia`, `comida_pct`, `bebida_pct`, `alcohol_pct`, `prime_cost_pct`. `clientes_dia`,
  `equilibrio_*_clientes_dia` y `pesimista/optimista_clientes` son **covers**: escribe la palabra al lado del token.
- Fuentes de mercado citables (research delta §4-§5): Restaurant365 ($100,000-$850,000+ para abrir un bar),
  RestaurantOwner.com vía Poster ($110,000-$550,000 en local alquilado, media $425,500; reserva $75,000-$100,000),
  BevSpot (pour cost 18-24 %; cerveza 24 %, destilados 15 %, vino 28 %), Insureon ($2,039/año de liquor liability),
  Restaurant365 (prime cost 60-65 %). **Sin tasa de fracaso de bares** (no hay fuente leída): redacción cualitativa.
- Sin «ICO/ENISA», sin SL, sin convenio, sin superlativos («the most complete»). Financiación: préstamo bancario o SBA
  7(a) a 10 años, «lender-ready, approval not guaranteed».
- El cierre (productos de la tienda) lo escribe el ensamblador (129-131).

## (c) Tanda bar_a — docx §1-§5 (32 párrafos · ≈ 3.540 palabras)

Entrada `BP3/tandas/bar_a.entrada.json` → salida `BP3/docx_en_bar_a.json` (`{"<i>": "<párrafo EN>"}`). §1 resumen
con tokens (inversión, ventas, covers × ticket × días, mezcla de bebida, equilibrio, DSCR, préstamo); §2 concepto
(neighborhood bar with small plates: cócteles, draft, vino y cocina corta; barra de 14 plazas + patio); §3 mercado
con las fuentes de research §4-§5 (nada de mercado español, vermú ni afterwork: happy hour y regulars del barrio, sin
cifras sin fuente); §4 competencia (bares de barrio, cocktail bars, restaurantes con barra; cinco fuerzas y DAFO sin
cifras ES); §5 marketing (Google Business Profile, Yelp, Instagram, OpenTable / Resy; eventos y happy hour; delivery
solo para la comida).

```bash
python3 scripts/productos-digitales/business-plans-en-3/bp3.py check_textos --tanda bar_a
```

## (d) Tanda bar_b — docx §6-§10 (30 párrafos · ≈ 3.100 palabras)

Entrada `BP3/tandas/bar_b.entrada.json` → salida `BP3/docx_en_bar_b.json`. §6 operaciones (local, equipamiento,
distribuidores en el three-tier system, flujo de servicio en barra y sala, control de inventario y pour cost); §7
equipo (puestos reales de `Staffing`, sin tip credit, D38); §8 plan financiero SOLO con tokens (prime cost
`{{prime_cost_pct}}`; el pour cost manda); §9 legal con las 5 notas (106-110; **el 110 cierra con la nota UK**:
premises licence + personal licence, Licensing Act 2003, FHRS, VAT 20 %, 14 alérgenos); §10 conclusiones y hoja de ruta
en el orden del checklist (licencia de alcohol en la fase 2).

```bash
python3 scripts/productos-digitales/business-plans-en-3/bp3.py check_textos --tanda bar_b
```

## Después de las 4 tandas (orquestador)

```bash
python3 scripts/productos-digitales/business-plans-en-3/bp3.py preparar_tandas      # aplica GR.revision.json
python3 scripts/productos-digitales/business-plans-en-3/bp3.py check_textos --todas  # GM, GR, GBAR-plan, GBAR-check + 2 docx
```

Luego la tanda de `aplicar_en.py` (VPS): ver `F2-NOTAS.md` §6.
