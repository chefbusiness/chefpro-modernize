# Brief para los traductores (subagentes Sonnet) — Wedding Venue Business Plan Kit (EN)

> Sesión Claude Code, 27-oct-2026 (F2-EN, paso 1a: preparado; **no se ha traducido nada**). SPEC delta D156-D180 (+ §11,
> decisiones de orquestador del 27-oct) y **§0, regla de jerga**. Regla 1bis: los textos de producto los escriben
> subagentes Anthropic, **nunca bridge.py**. Carpetas (worktree del Mac): `scripts/productos-digitales/business-plans-en-9/`
> (= `BP9/`, datos y salidas del wedding venue), `scripts/productos-digitales/business-plans-en-8/` (= `BP8/`, la **Pizza
> EN** cerrada: misma maquinaria y la FORMA de los textos del motor) y `scripts/productos-digitales/business-plans-en/`
> (= `BP/`, el código común y el brief de FT/CAF). Fuente ES: el LIVE de `astro-site/public/dl/plan-negocio-finca-eventos-bodas/`.
>
> **Tanda 1 = DOS traductores en paralelo, sin pisarse** (cada uno escribe SOLO sus ficheros de salida; `istats cpu temp`
> < 62 °C en el Mac antes de lanzar):
>
> | Traductor | Entradas (`BP9/tandas/`) | Salidas (`BP9/textos_en/`) | Cadenas / párrafos | Palabras ES |
> |---|---|---|---|---|
> | **A** | `GWED-plan.entrada.json` (incluye `revisar_reutilizadas` = GR) + `contrato_2.entrada.json` | `GWED-plan.json` + `GR.revision.json` + `contrato_en_2.json` | 187 cad. + 11 GR + 48 párr. | 3,967 + 256 + 1,419 ≈ **5.6 K** |
> | **B** | `GWED-check.entrada.json` + `contrato_1.entrada.json` | `GWED-check.json` + `contrato_en_1.json` | 241 cad. + 102 párr. | 2,720 + 3,324 ≈ **6.0 K** |
>
> **No se escriben** GM (306 cadenas: mismo ES exacto que una cadena GM del motor de la Pizza EN o de BP/BP2, EN limpio) ni
> GR (11: se **revisan** en A): los escribe `bp9.py preparar_tandas`. La **calculadora** (D168) NO va en tandas: es código
> (`calculadora_wed.py` = `../plan-finca-eventos/calculadora_fin_es.py` traducida y adaptada, paso 1b, como la de la Pizza y
> la del BBQ). **Tanda 2** (Word, `wed_a` ‖ `wed_b`) después de la 1 y del `aplicar_en` real (§4).

**Cómo usar este brief**: el orquestador pega al subagente la sección **0 de `BP/BRIEF-TRADUCTORES.md`** (reglas comunes:
idioma, cero español, moneda, formato US, marca, cifras, pestañas citadas, glosario) + las secciones **0 y 1** de este
fichero (la 1 es el glosario de research §9 completo, OBLIGATORIO) + la de su traductor (§2 o §3). El subagente no hace
commit y no toca nada más que sus salidas.

---

## 0. Lo que cambia frente al brief de la Pizza EN (manda sobre él en lo que choque)

**Qué lees** (y nada más): tus entradas `BP9/tandas/*.entrada.json`; `BP9/SPEC-delta.md` (D156-D180 y §11);
`BP9/F1-research-us-delta.md` §1, §4, §5, §6, §8 y §9; como FORMA (registro, longitud, fuentes comunes) el EN de la Pizza en
`BP8/textos_en/{GPIZ-plan,GPIZ-check}.json`: **su vocabulario (pizza, covers, dine-in, oven, food cost…) NO vale**.

**Concepto (D159): BARN / ESTATE WEDDING & EVENT VENUE en una propiedad ARRENDADA** a 30-60 min de una ciudad media-grande
de EE. UU.: salón para **200 invitados sentados**, ceremonia exterior con pérgola, bridal suite, aseos ADA, parking de grava
y una cocina de apoyo (prep & warming) para el caterer. El venue factura **venue rental fee / site fee + servicios** y cobra
una **caterer commission** a su **exclusive caterer**, que factura comida y barra a la pareja y sirve el alcohol con SU
licencia: **el venue no vende comida ni alcohol**. Mes 1 = marzo (el permiso y la obra se cierran en el invierno). «Wedding
venue» en el nombre, «event venue» como descriptor y «venue» en prosa: **nunca «finca», «estate» ni «farm» como nombre del
negocio** (sí «barn venue» como tipo). Volumen = **guests · revenue per guest · events per year** (nunca «covers»,
«customers» ni «average check»). Fuera (alternativas razonadas, sin Excel): comprar el inmueble (SBA 504), in-house
catering (→ Catering Business Plan Kit), banquet hall urbano, wedding planner.

**Caso US** (dry-run del paso 1a, `BP9/F2-NOTAS.md` §3; D160 con la calibración D15): **90 guests × $68 × 100 events =
$612,000** (35 weddings, 25 corporate, 30 private celebrations, 10 micro weddings) · 88 % venue rental & services / 12 %
caterer commission (10 % de la venta de F&B del caterer) · CAPEX **$570,500** (19 partidas $503,500 + imprevistos de obra
$37,000 por fórmula + fianza $10,000 + 4 meses de renta previa $20,000) + fondo de maniobra $99,216 = **$669,716** · propios
$200,000 (30 %) + préstamo **$470,000** (SBA 7(a), 10 %, 10 años) · variables 16.6 % · personal 31.4 % · renta 9.8 % ·
EBITDA 26.3 % · **neto 8.9 %** (14.2 % el año 3) · equilibrio de caja ≈ 84 eventos del tamaño medio, holgura 20 % · DSCR mín
1.86×. Las notas del libro describen el **método** o usan `valor_us`; el Word cita el caso SOLO con tokens `{{…}}`.
**Ninguna cifra del ES** (D173: el gate caza los importes del caso ES en € y en $, «82 guests», «$37 per guest», «120
events», «12 %» de canon, «14 pay periods», «33 %» de cargas, «8.8 %») **ni de la Pizza EN** (sus importes, «62 covers»,
«$36», «300 days»).

**Lo que el check rechaza** (`datos_wed.RX_WED_NO` + `cifras_prohibidas`; **cero rastro de pizza, panadería ni España**):
pizza, pizzaiolo, dough, wood-fired, covers per day, average check, croissant, sourdough, bakery business; finca, canon,
IVA, convenio, SMI, autónomo, comunidad autónoma, ayuntamiento, SGAE/AGEDI, «testigo», TRLGDCU, LAU, LIVA, arras, señal,
fijo discontinuo, calificación urbanística, Orden INT, RD, BOE; parrilla/brasa/pitmaster/smoker/paella/food truck;
España/Spain/Spanish; VAT fuera de la nota UK; m², kg, km, litros o °C fuera de paréntesis.

**Unidades (D14, `datos_wed.REGLA_UNIDADES`)**: superficie en **sq ft con los m² entre paréntesis** («5,000 sq ft (465
m²)»), millas, °F, galones; fechas **mm/dd/yyyy**; importes **$1,000.00**.

**Decisiones de orquestador del 27-oct (mandan; SPEC-delta §11)**:
1. **Arrendamiento**: la obra (≈ $570K de CAPEX) se hace sobre suelo ajeno. Donde toque (Word §2/§9/§10, checklist fase 1
   y 2, notas de `0. Assumptions` C31/C54 y de `Startup Costs` D24): lease largo cuya duración **contando las prórrogas** sea
   al menos la del préstamo, dicho como «**SBA lenders typically require…; confirm with your lender**» (sin citar una regla
   concreta); **purchase option o right of first refusal**; **consentimiento del propietario a la obra y a usar el lease
   como garantía**; negociar una **TI allowance**; **lease contingent on CUP approval**. Comprar (SBA 504) = variante del
   Word, sin Excel.
2. **FTC Cooling-Off Rule (16 CFR Part 429)**: excluye los arrendamientos de inmuebles: **NUNCA se afirma que aplique** a un
   contrato de venue. Forma única: «If you sign couples at bridal shows or off-site, ask your attorney whether the FTC
   Cooling-Off Rule or your state\'s home-solicitation law applies; many venues give a short cancellation window for
   show-floor signings anyway.» (checklist fase 6 fila 7, contrato, Word §9).
3. (Correo EN de lanzamiento: 23-feb-2027 14:00Z; no es de esta tanda.)
4. **Lo «(resumen)» de research** (The Knot, NY A20-51S, Missouri, CA Civ. Code §1671, 40 CFR 141.2, Wisconsin, rentas,
   seguros, sprinklers, fosa séptica) **no va como cifra rotunda ni como cita**: «typical range, get local quotes», «Kit
   estimate» o «ask your [state agency / county / attorney / CPA]». La revisión D174 abrirá lo que deba volver.

**Claims que no se hacen**: que un permiso basta, que el venue tiene licencia de alcohol, rentabilidades de la SERP,
«non-refundable» sin la tabla de cancelación, que los edificios viejos quedan «grandfathered», umbrales de sprinklers con
cifra (IBC 903.2.1.2 «as adopted»), cifras de fosa séptica o sprinklers de anécdotas.

---

## 1. Glosario OBLIGATORIO (research §9, pegado entero; también en `../GLOSARIO-JERGA-ES-EN.md` §«Fincas de eventos y bodas»)

### Research §9 — Jerga profesional US (glosario OBLIGATORIO de los traductores; se añade a `../GLOSARIO-JERGA-ES-EN.md`)

(a) **Nombre**: **«Wedding Venue Business Plan Kit»** en landing/H1/ficheros (`wedding-venue-business-plan`); «event venue» como
descriptor y sinónimo; «venue» a secas en prosa. Nunca «estate», «farm» ni «finca» como nombre del negocio (sí «barn venue» como tipo).

| # | ES finca | Término US | Fuente / estado |
|---|---|---|---|
| 1 | Finca de eventos | **wedding venue / event venue** (tipos: **barn venue**, estate venue, farm venue, banquet hall) | DFS 1,000 / 720; wedding barn 6,600 |
| 2 | Alquiler del espacio | **venue rental fee** / **site fee** (+ «venue fee» si es % de F&B) | DFS 40; fichas §5.1; Edison Ford |
| 3 | Catering exclusivo · homologados | **exclusive caterer** · **preferred vendor list** · **in-house catering** | DFS 10 · 260; SERP |
| 4 | Canon del catering | **caterer commission** (% of F&B) / **exclusivity fee** | §5.3 (no «canon», no «royalty») |
| 5 | Invitados · recuento final | **guests** · **guest count** · **final headcount** (due X days before) | uso del sector |
| 6 | Mínimo garantizado | **guaranteed guest count** · **food & beverage minimum** (del caterer) | DFS 90 (F&B minimum) |
| 7 | Señal / reserva | **retainer** (aplicado al precio) · **booking deposit**; «non-refundable» solo con el matiz de §6.7 | DFS «wedding venue deposit» 90 |
| 8 | Fianza por daños | **security deposit / damage deposit** (refundable, itemized) | uso del sector |
| 9 | Barra libre · resopón | **open bar / hosted bar** (del caterer) · **late-night snack** | MBAR §9 |
| 10 | Coordinación del día | **venue coordinator** (del venue) ≠ **day-of coordinator** (de la pareja) | DFS 140 / 1,900 |
| 11 | Montaje y recogida | **setup / teardown (breakdown)** · **load-in / load-out** | uso del sector |
| 12 | Plan B de lluvia | **rain plan / inclement-weather plan** (tent backup) | uso del sector |
| 13 | Aforo | **maximum occupancy / occupant load** (lo fija el fire marshal) | IBC §6.2 |
| 14 | Calificación urbanística / licencia de actividad | **zoning approval: conditional (special) use permit** · **certificate of occupancy** (assembly, Group A-2) | DFS CUP 1,600; §6.1-6.2 |
| 15 | Prueba de menú | **tasting** | uso del sector |
| 16 | Visitas · jornada de puertas abiertas | **venue tours / site visits** · **open house** | DFS 260 · 110 |
| 17 | Temporada alta / media / baja | **peak / shoulder / off-peak (off-season)** | DFS peak wedding season 480; fichas §5.1 |
| 18 | Preboda · boda íntima · cena de la víspera | **rehearsal** · **micro wedding / elopement** · **rehearsal dinner** | DFS 8,100 · 1,900 · 12,100 |
| 19 | Suite de novios | **bridal suite** · **groom's lounge** | DFS 2,400 |
| 20 | Proveedores externos | **outside vendors** · **outside catering fee** · **cake-cutting fee** · **corkage fee** | DFS 10 · 210 · 4,400 |
| 21 | Portales de bodas | **The Knot / WeddingWire storefront (listing)** · venue marketplaces (Peerspace) | SERP; §5.3 |
| 22 | Seguro RC · certificado | **general liability** · **host liquor liability** · **event insurance** · **COI / additional insured** | DFS 12,100 · 1,900; ✅ MBAR |
| 23 | Fijo discontinuo | **seasonal employee (W-2)** | ✅ hermanos |
| 24 | Grupo electrógeno · limitador | **standby generator** · **decibel limit / sound meter, music curfew** | uso del sector |
| 25 | Aseos adaptados · saneamiento · pozo | **ADA-compliant restrooms** · **septic system** · **well (public water system)** | §6.3-6.4 |
| 26 | Software de reservas | **venue management software** (Tripleseat, Perfect Venue, HoneyBook) | DFS 260; tripleseat 60,500 |
| 27 | Invitado / ticket / días | **guests · revenue per guest · events per year** (nunca «covers» ni «average check») | motor de eventos (✅ CAT/BBQ) |
| 28 | Dossier | **wedding brochure / pricing guide** | uso del sector |

(e) **No se traducen literalmente**: «finca» → **venue** (o «property» para el inmueble) · «canon» → **caterer commission** ·
«IVA» → **sales tax** · «calificación urbanística/licencia» → **CUP + certificate of occupancy** · «autoprotección» → **fire code,
occupant load, sprinklers** · «comida testigo» → *no aplica* (eliminar) · «14 alérgenos» → **9 major allergens (caterer)** · «fijos
discontinuos» → **seasonal W-2** · «TRLGDCU/fuero del consumidor» → **state consumer law; governing law & venue clause** · «arras /
señal» → **retainer** · «SL/autónomo» → **LLC** · «gestoría» → **CPA / bookkeeper** · «ayuntamiento/comunidad» → **county / state** ·
«SGAE» → **ASCAP/BMI/SESAC** · «ceremonia civil (Ley 15/2015)» → *el venue acoge; licencia y officiant según el estado*.

**Capas (1) y (2)**: **Wedding Venue Business Plan Kit** · slug `wedding-venue-business-plan` · ficheros y pestañas en SPEC D158/D169.

**Responsables del checklist** (columna C; cadenas cortas que se repiten): Titular → **Owner** · Gestoría → **CPA /
bookkeeper** · Técnico → **Architect / code consultant** · Abogado → **Attorney** · Corredor de seguros → **Insurance agent**
· Catering → **Caterer** · Coordinación → **Venue coordinator** · Auxiliares → **Event attendants** · Constructora →
**General contractor** · Instalador autorizado → **Licensed contractor** · Jardinero → **Landscaper** · Fotógrafo →
**Photographer** · Laboratorio → **Certified lab**.

---

## 2. Traductor A — (a1) GWED-plan + revisión de GR · (a2) contrato parte 2 (Modelo 2)

**(a1)** Entrada `BP9/tandas/GWED-plan.entrada.json` (187 cadenas, 3,967 palabras, 98 pistas; 21 con `propuesta_en`).
Salidas: `BP9/textos_en/GWED-plan.json` (**TODOS** los ids de `cadenas` y nada más) y `BP9/textos_en/GR.revision.json` (de la
lista `revisar_reutilizadas.GR`, 11: **solo** las que cambian, `{}` si ninguna).

- **Propuestas** (`propuesta_en`): vienen de la Pizza EN tras invertir el vocabulario de la finca (invitado → cubierto,
  canon → bebida, espacio y servicios → comida…): por eso dicen FOOD/BEVERAGE, covers, shift, delivery. **Reescríbelas**
  para el venue: «Venue rental & services share of total sales», «Caterer commission share of total sales», «Direct event
  cost on venue rental & services», «Cost of the commission (none) on commission sales», «Variable cost per guest»,
  «Contribution margin per guest», «Venue staff needed at the same time on an event day», «Off-day hours per event (tours,
  setup, turnover)»… La forma (longitud, registro) de la propuesta vale; su vocabulario no.
- **Notas de `0. Assumptions` (col. C)**: el caso de su pista (D160) o el método; un solo sales tax de ejemplo (8 % sobre
  venue rental & services; 0 % sobre la comisión del caterer; B41 = 0, sin crédito por compras). Las de `A62`/`C62`/`A63`/
  `C63`, `3-Year P&L!F10`/`F11`, `12-Month Cash Flow!O5`/`O13`/`O16`/`A34` y `Staffing!A28`/`A29` ya están fijadas
  (POR_CELDA, `datos_wed.py`): úsalas con esas palabras si las citas.
- **Notas de `Startup Costs` (col. D, filas 7-25)**: las 19 partidas de D162 (rótulos ya fijados en `fijos_en`); sin rangos
  de anécdotas (decisión 4): «sprinklers need city water; a tank and fire pump, a new septic system or a strict county can
  double this line» en la fila 10; ADA en la 12; cocina de apoyo (no de producción) en la 16; lease y contratos en la 24.
- **Tabla D19 (`Instructions` 35-48, 55 celdas, una por celda, SIN propuesta)**: cada fila la dicta su pista (D165):
  Benchmark | Value | Source | Note. `A41` ya está fijada («Caterer commission (exclusive caterer)»): escribe B41-D41 a juego.
  Solo lo «leída» lleva fuente; lo «(resumen)» = «Kit estimate» o «ask…». Nada de The Knot, ni del 40 CFR 141.2, ni de
  umbrales de sprinklers con cifra.
- **`Instructions` A4-A12**: A8 sin divisores 1,21 («divide by 1 + your sales tax rate»); A10 con el **Mes 1 = MARCH**; A12:
  el Word cita las cifras de este Excel y la calculadora de precios y los contratos usan los mismos % de cobro y cancelación.
- **`Staffing` J5-J10 y J18-J26**: seasonal W-2, 12 pay periods, FLSA (40 h), nunca 1099 para quien el venue dirige; el
  dueño, por debajo de la mediana nacional de los event planners (BLS) **sin cifra**; servers y bartenders son del caterer.
- **Revisión de GR**: EN de otros kits casado por texto (títulos de hoja, C30 de recursos propios, A55 de imprevistos, F24,
  O7, D31, A7, A11…): confirma o corrige lo que no case con un venue (p. ej. A55 «…of the space block» → «…of the property
  block» / «of the build-out items»).

**(a2)** Entrada `BP9/tandas/contrato_2.entrada.json` (Modelo 2 · catering exclusivo: 48 párrafos ES, 1,419 palabras).
Salida `BP9/textos_en/contrato_en_2.json` = lista `[{"estilo", "texto"}]`. Sigue `reglas` y `decisiones_D171` de la entrada:
«Exclusive Caterer Agreement», B2B, commission [10]% of F&B net of sales tax, service charge and gratuities, statement
mensual + audit right, prep kitchen con el health permit del caterer, **comida testigo fuera**, 9 major food allergens,
personal W-2 del caterer, liquor license/permit + liquor liability $[1,000,000] + workers\' comp + auto con el venue como
additional insured, FOG y residuos, tasting, plazo, governing law (B2B). Corchetes para todo lo editable.

## 3. Traductor B — (b1) GWED-check (las 84 tareas, D169) · (b2) contrato parte 1 (portada + Modelo 1 + Anexo)

**(b1)** Entrada `BP9/tandas/GWED-check.entrada.json` (241 cadenas, 2,720 palabras, 132 pistas; 19 con `propuesta_en` de
otros kits). Salida `BP9/textos_en/GWED-check.json` (TODOS los ids). Molde C2 (OK | TASK | OWNER | TIMING | NOTES); pestañas
y A1 («WEDDING VENUE STARTUP CHECKLIST») ya fijados; la cabecera de cada fase (fila 2) se llama como su pestaña
(«PHASE 2: ZONING & PERMITS (18-6 months before)»…). **Cada fila trae su tarea US como pista («D169 tarea US: …»)**: manda
sobre el ES y sobre la propuesta; se reescriben tareas equivalentes **sin mover filas**. Obligatorio (decisiones 1 y 2):
fase 1 fila 14 (lender package + lease ≥ loan term), fase 2 filas 5-10 (zoning check por escrito, lease contingent on CUP,
purchase option / right of first refusal + consentimiento a la obra y a la garantía + TI allowance, CUP, change of
occupancy A-2, fire marshal por escrito), fase 6 fila 7 (Cooling-Off con «ask your attorney whether…»). La «comida testigo»
(fase 4 fila 14 y fase 6 fila 14) **no cruza**: su fila pasa a la tarea US de la pista. Los plazos en meses del plan
(«Month 1», «Months 3-5», «Before signing», «Event day»…). El aviso de la DV (`Usa el desplegable…`) dice «✓, ☐, N/A» con
«☐ = pending» (nunca «—»).

**(b2)** Entrada `BP9/tandas/contrato_1.entrada.json` (102 párrafos ES, 3,324 palabras). Salida
`BP9/textos_en/contrato_en_1.json` = lista `[{"estilo", "texto"}]`. Sigue `reglas` y `decisiones_D171`: portada + **cabecera
fija literal** (la del campo `cabecera_fija`) en los 6 primeros párrafos; Modelo 1 «Venue Rental Agreement (Couples &
Private Events)» con Permits, **2A Contingent booking before permits**, Fees and sales tax, Payment schedule (25/35/40),
**Retainer** (aplicado al precio; lo retenido lo fija SOLO la tabla), Cancellation by the Client (tramos + **rebooking
credit** + «reasonable estimate of the Venue\'s loss, not a penalty»), Cancellation by the Venue, la cláusula OPCIONAL de
firmas fuera del venue con la nota de la Cooling-Off Rule (decisión 2), Governing law, Force majeure, Noise and music
(ASCAP/BMI/SESAC), Outside vendors (COI), Damage and security deposit, Insurance, Food, alcohol and allergens, **Mutual
responsibility**, **Entire agreement and e-signatures**; y el **Corporate & Organization Addendum** (W-9, PO, sales tax
exemption certificate, net terms, 5/15/35/60/100). Nada de derecho español.

## 4. Tanda 2 (después): `wed_a` (§1-5) ‖ `wed_b` (§6-10) — el Word

`BP9/tandas/wed_a.entrada.json` (29 párrafos, 3,071 palabras) y `wed_b.entrada.json` (32 párrafos, 3,551 palabras), ya
preparadas sobre el Word ES LIVE (131 ranuras del FT ES, la estructura de PAEL/PIZ). Cada párrafo trae su nota
(`datos_wed.DOCX_NOTAS`: la sección + la FORMA de la Pizza EN; las 7 de §9 = 102-108 con sus temas de D170, la 108 cierra con
la nota UK) y la entrada trae `notas_del_plan` y los 135 tokens. **Se lanzan tras el `aplicar_en` real** (paso 3) para que
`cifras_caso.json` exista; los ids no cambian.

## 5. Validación (Mac, solo JSON) — el comando exacto de cada traductor

```bash
istats cpu temp | head -1
B9=scripts/productos-digitales/business-plans-en-9
# Traductor A (GR.revision.json: JSON válido con ids de revisar_reutilizadas.GR; lo aplica el orquestador)
python3 $B9/bp9.py check_textos --tanda GWED-plan && python3 $B9/bp9.py check_contrato --parte 2
# Traductor B
python3 $B9/bp9.py check_textos --tanda GWED-check && python3 $B9/bp9.py check_contrato --parte 1
# Orquestador, al recibir las dos: todo junto y GR con la revisión aplicada
python3 $B9/bp9.py preparar_tandas && python3 $B9/bp9.py check_textos --todas && python3 $B9/bp9.py check_contrato --todas
```

(Ningún traductor corre `preparar_tandas`: reescribe las entradas que el otro está leyendo. La revisión de GR la aplica el
orquestador con `preparar_tandas` al recibir las dos tandas.) Itera hasta
`OK (0 errores, …)` y revisa los AVISOS reales. Responde solo con: ficheros escritos, nº de claves / párrafos, resultado de
los checks y 3-5 decisiones que deban conocer las demás tandas.
