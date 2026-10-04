# Revisión adversarial final — Food Truck y Coffee Shop Business Plan Kit (EN) · 4-oct-2026 · sesión Claude Code

Una ronda, sobre `feat/business-plans-en` @ `b218c1df` (PR #110). Los 6 ficheros publicados se revisaron con sus hashes
(Mac = VPS). En el VPS, en un worktree limpio (ya borrado), se volcaron fórmulas y caché con openpyxl (`data_only`) y
los docx con python-docx. Las cifras de abajo están **recalculadas a mano** a partir de los inputs, no copiadas de la
caché. Lentes: prestamista/CPA, inspector/abogado, ficheros, copy y promesas.

**Veredicto: NO está listo para vender tal cual.** Hay 1 bloqueante, que se arregla cambiando solo textos (unos
15 min, sin tocar fórmulas), y 3 mayores. Todo lo demás se sostiene: los números cuadran al dólar entre xlsx, docx,
`cifras_caso.json` y landings.

---

## BLOQUEANTE

### B1 · La deuda SBA puede quedar fuera del P&L y del DSCR, y por defecto el docx ya contradice al Excel
- **Dónde**: `*-financial-projections.xlsx` → `Financing!A7:C11` (FT y CAF). `Instructions!A7` vende las filas 8-11
  como «the four alternative funding sources».
- **Qué pasa**: el cuadro de amortización, los intereses del P&L (`Financing!B44/B46/B48`) y el DSCR (`B51:B54`) leen
  **solo** `'0. Assumptions'!B31` (= fila 7, «Loan (bank or lender)»). Las filas 8 «SBA-guaranteed loan (7(a), through
  your bank)» y 9 «SBA Microloan» se suman a las fuentes (`B12`), pero **no se amortizan nunca**.
  - **Por defecto**: el docx FT ([42]) dice «a $112,000 **SBA 7(a)** loan», mientras la hoja que mira el banco enseña
    «SBA-guaranteed loan (7(a)): 0» y los 112,000 en la fila genérica. El mismo dossier se contradice.
  - **Lo que hará el comprador** (la landing, el FAQ y el correo hablan de SBA 7(a)): teclear su préstamo SBA en la
    fila 8. Entonces `B15` sale en positivo (ámbar), y `B18` le propone bajar B31 («Loan that would match sources…»).
    Con B31 = 0 desaparecen el cuadro, los intereses y el DSCR (queda en blanco). Si no lo baja, la deuda extra no paga
    ni intereses ni principal. En los dos casos el plan llega al banco **sin servicio de una deuda que sí existe**.
- **Arreglo (solo textos, la paridad de fórmulas G1 queda intacta)**:
  - `A7` → «Loan requested — bank or SBA 7(a) (from "0. Assumptions"; amortized below)».
  - `A8` → «Second loan (NOT in the schedule or the DSCR: add its payment to fixed costs)» y `A9` → «SBA Microloan (NOT
    in the schedule or the DSCR)». Notas C7-C9 a juego.
  - `0. Assumptions!C31` y `C33`: «if your loan is SBA 7(a), this is the cell».
  - Landing (grid «Financing Plan», FAQ «present this plan to a lender»), los 2 correos y el changelog: «the loan
    schedule and the DSCR cover your main loan (bank or SBA 7(a))».

## MAYOR

### M1 · Comisión de tarjeta: la nota dice una aritmética falsa, y el semáforo verde del CAF depende de ella
- **Dónde**: FT `0. Assumptions!C18` («The example (2.9%) is roughly 2.6% plus 0.15 per sale … averaged over the
  check»); viene de `F1-research-us.md` §3. CAF `B18` = 2.9 % con el mismo origen. Los docx lo repiten: FT [96], CAF [105].
- **Por qué está mal**: con un ticket de $15.12 (impuesto incluido), 2.6 % + $0.15 son **$0.54, es decir 3.9 % de la
  venta sin impuesto**, no 2.9 %. En el CAF ($11.88): $0.46, es decir **4.2 %**. Un CPA lo ve en segundos.
- **Impacto recalculado** (todos los tickets con tarjeta a 2.6 % + 15¢):
  - FT: +$2,852 al año → neto año 1 del 7.1 % al **6.4 %**, holgura del 21.6 % al **19.6 %**, DSCR de 2.02× a 1.93×.
    Sigue pasando D15.
  - CAF: +$6,658 al año → neto año 1 del 6.3 % al **5.4 % (REVIEW, rojo)**, holgura del 17.6 % al **15.3 %** (al
    filo), equilibrio contable de 123 a 125 clientes/día.
- **Arreglo**: reescribir C18 en los dos planes como «blended rate; at 2.6% + 15¢ a 15 ticket costs about 3.6%;
  negotiated interchange-plus plans and cash sales bring it down: test 3.5%». Mínimo, quitar la aritmética. Si se sube a
  3.5 %, la calibración D15 del CAF hay que repetirla (y regenerar docx y landings).

### M2 · La landing enseña Google Sheets (y PDF) justo debajo de «Microsoft Excel and Word files»
- **Dónde**: el marquee de logos de `PlanNegocioLandingPage.astro` en las 2 landings EN (comprobado en el preview: 8
  repeticiones de «Google Sheets» y de «PDF», bajo «Print, Delegate and Control · Microsoft Excel and Word files…»).
- **Por qué importa**: D25 y el brief lo prohíben (no hay test en Sheets), y el kit no trae ningún PDF. Visualmente se
  lee como compatibilidad prometida. F3 lo dejó como residuo para no romper el byte a byte de las ES.
- **Arreglo**: condicionar el array `apps` por `lang` (en EN, sin Google Sheets ni PDF). Las ES no cambian y
  `tienda-gate --es-identico` sigue verde.

### M3 · Los correos afirman «regular price $129», un precio al que nunca se ha vendido
- **Dónde**: `emails/broadcast-{food-truck,coffee-shop}-business-plan-lanzamiento-en.html`: «The launch price is $39
  (regular price $129)».
- **Por qué importa**: en EE. UU., una afirmación de «precio habitual» que nunca se ha ofrecido es el ejemplo de manual
  de la FTC (16 CFR 233.1) y de las leyes estatales de publicidad engañosa. El tachado de la landing es política de
  tienda (decide John); la frase del correo es una afirmación literal y se quita sin coste.
- **Arreglo**: «The launch price is $39: a one-time payment…» (sin «regular price»). Lo mismo en futuros correos EN.

## MENOR

| # | Dónde | Qué | Arreglo |
|---|---|---|---|
| m1 | docx FT [99] | «The plan also has to survive a bad stretch» y el pesimista con −$49,025, pero no dice que la caja **se agota** (`Scenarios!B25` = −14,020, en rojo) | Una frase con el saldo estimado del pesimista |
| m2 | docx FT [99], CAF [133] | Los escenarios citan clientes e ingresos, pero no el ticket ni los días que también cambian (FT $11.67; CAF $10.33 y 329 días). 53 × 14 × 260 ≠ $160,813: el lector no puede reproducir la cifra | Añadir ticket y días a cada escenario |
| m3 | docx FT [107]; checklist FT `Phase 2!B14/E14`; landing FT FAQ «What does the truck itself need?» | «CDL **only** if GVWR ≥ 26,001 lb»: falta la regla de combinación (camión + remolque de > 10,000 lb con GCWR ≥ 26,001 → Class A), y la §6 del docx propone remolque | «…or when towing a trailer over 10,000 lb GVWR with a combined rating of 26,001 lb or more» |
| m4 | checklist FT `Phase 3!E10` | «The kit's bare minimum is about 10.5 gallons fresh and 16 gray (40 and 60 liters)»: es la cifra española, sin fuente US. Muchos condados piden bastante más; un depósito pequeño no pasa el plan review | Quitar el «bare minimum» y los litros; dejar «your county sets the minimum (often far above 10 gallons)» |
| m5 | docx CAF [97]; `0. Assumptions!C24` CAF | «Rent and the rest of our occupancy costs come to $54,000»: es solo la renta base. NNN/CAM e impuesto sobre la propiedad no están modelados, y la nota de la celda no pide incluirlos | Docx: «base rent of $54,000 (add NNN/CAM charges)»; C24: «include NNN / CAM charges in this cell» |
| m6 | docx CAF [99] | Atribuye la fontanería a la partida eléctrica/HVAC de $15,000 (la fontanería es su propia línea de $10,000) y dice que la contingencia vive «inside the working capital reserve» (es la línea `Startup Costs!B32`, $8,300) | Corregir las dos frases |
| m7 | docx §8 FT [97] / CAF [130]; `0. Assumptions!C37` | El impuesto del 25 % es de C corporation (lo explica C37), pero el docx no lo dice, y el checklist y la §9 empujan LLC o empresario individual. Además, el dueño cobra nómina W-2 (en LLC unipersonal o empresario individual serían retiradas + self-employment tax) | Docx: «25% (C corporation example; pass-through owners set 0 and pay personally)» |
| m8 | `0. Assumptions!A21` (ambos) | «Pay periods per year = 12» con DV 12-16: en EE. UU., *pay periods* es la frecuencia de nómina (26 quincenal). El concepto «extra pay period» es español | «Monthly salaries per year (keep 12 in the US)» |
| m9 | `0. Assumptions!C58` (ambos) | La nota dice «paid on the spot (0 days)» y el valor es 1 (cambio de F2 por la DV) | «1 day: card settlements arrive the next business day» |
| m10 | `0. Assumptions!C52` FT/CAF; CAF `Instructions!D67` | Dan a entender que la rampa baja las ventas del año 1 frente al régimen estable. El modelo **conserva el total anual** (B4 es la media del año 1) y solo redistribuye por meses (`12-Month Cash Flow!O7` lo dice bien) | Alinear C52 y D67 con O7 |
| m11 | CAF `Phase 4!E5`; CAF `Staffing!A8` | Turnos de 6 am a 3 pm y de 2 pm a 10 pm = 16 h al día (Staffing cubre 13), y turno de 9 h (horas extra diarias en CA y otros estados). «Brunch cook (weekends)» a 0.8 FTE = 32 h → 16 h/día si solo trabaja el fin de semana | Turnos coherentes con 13 h; quitar «(weekends)» o explicar los días |
| m12 | FT `Instructions!D43` | «It was the same expense written in two places. Now…»: es historia de versiones (D18 la prohíbe) | «Writing it in two places counts it twice: here it lives in one cell» |
| m13 | landing FT, grid «Mobile Kitchen Equipment» + FAQ del camión | «each one is a line in the startup costs»: plancha, freidora, campana y frío son UNA línea («Kitchen and refrigeration equipment»), y el lavamanos va con los depósitos | «all budgeted in the startup costs (kitchen equipment, generator, tanks and sinks, propane and suppression)» |
| m14 | `src/data/productos-changelog.ts` 2.2 (ambos) | «square feet and gallons»: el FT no tiene sq ft y el CAF no tiene galones. «No currency symbol in the workbooks»: el CAF tiene «$1M» en `0. Assumptions!C27` y `Phase 2!E12` | Unidades por plan; «1M» sin símbolo |
| m15 | docx FT [94], CAF [128] | «annual payment of $23,005 / $33,200»: el modelo amortiza en anualidades y el SBA en mensualidades (≈ $1,858/mes en el FT, unos $700/año menos). Es conservador, pero choca con el banco | «(annual equivalent; your lender will set monthly payments)» |
| m16 | docx FT [108], CAF [142]; checklists | «Food Hygiene Rating 1-5» para todo el Reino Unido: Escocia usa el FHIS (Pass / Improvement Required) | «(England, Wales and NI; Scotland uses FHIS)» |
| m17 | docx CAF [137] | EIN «needed … to pay sales and excise taxes»: el sales tax es estatal (el IRS lo pide para empleados, *employment* y *excise*) | «…to hire employees and file federal employment and excise returns» |
| m18 | checklists FT `Phase 4!B14`, CAF `Phase 4!B16`; FT `Phase 5!E16` | Tarea de origen RGPD sin base federal (como mucho CCPA/BIPA estatales) y autorreferencia «Your checklist promises a QR loyalty program» | Mencionar los relojes biométricos (BIPA) o fundir con la de privacidad; reescribir E16 |
| m19 | fichas (bonus 1) | El bono de $29 «Permits & Licenses Guide» es la §9 del docx más una fase del checklist: valor contado dos veces en el «Total value $187». Está declarado en la descripción | Decisión de tienda (John); se anota |
| m20 | calibración D15 (F2-NOTAS §7.1) | El FT sube de 70 a 80 clientes/día de media en el año 1 para pasar la holgura. Está dentro del rango de ventas de research ($291K frente a una media de $346K de camiones ya rodados), pero un prestamista escéptico lo verá optimista para un camión nuevo | Observación; no exige cambio |

---

## Lo que SÍ está bien (comprobado)

**Recalculado a mano (FT · CAF):**
- **Ventas año 1**: 80 × 14 × 260 = **$291,200** · 140 × 11 × 340 = **$523,600**. Años 2-3: $334,880 / $368,368 ·
  $560,252 / $588,265.
- **Variables**: FT 74,422 + 10,782 + 11,648 + 8,445 + 0 + 14,560 = 119,856 → margen bruto **58.84 %** · CAF 64,403 +
  74,142 + 15,708 + 15,184 + 0 + 10,472 = 179,909 → **65.64 %**. Mercancía 29.3 % · 26.5 %.
- **Fijos** (suma línea a línea): FT **$143,648** (amortización 77,220/7 + 24,500/7 = 14,531; intereses 11,200) · CAF
  **$299,605** (91,300/10 + 76,500/7 = 20,059; intereses 20,400). Fondo de maniobra = 3 × (fijos − amortización)/12 =
  **$32,279** · **$69,887**.
- **Inversión**: partidas sumadas = CAPEX **$114,120** · **$193,800** (contingencia 8 % × 71,500 = 5,720; 10 % × 83,000
  = 8,300). Caja total **$146,399** · **$263,687**. Fuentes 35,000 + 112,000 · 60,000 + 204,000, con diferencia
  +$601 / +$313 (≤ 5 %). Aportación propia **24 %** · **23 %**.
- **Resultado**: BAI **$27,695** · **$44,086**; impuesto 25 %; neto **$20,771 (7.1 %)** · **$33,064 (6.3 %)**.
  EBITDA $53,427 (18.3 %) · $84,544 (16.1 %).
- **Sales tax**: los ingresos del P&L no lo llevan. Cobrado en el año 291,200 × 8 % = **$23,296** · **$41,888**. La
  liquidación de abril = lo cobrado en enero-marzo (FT 846.6 + 1,017.9 + 1,404.5 = **3,269.0** = `E19`). El T4 va en
  enero (nota A34).
- **E2**: `G13:G14` = `$B$41` = 0, así que no hay crédito por compras, y la fila 17 (input tax) es 0 todo el año.
- **Nóminas**: FT $76,216.80 · CAF $168,946.80 (bruto × 1.10 × 12). Fila mensual constante (6,351.40 · 14,078.90).
  Ningún sueldo bajo $7.25/h: el más bajo, $15.60/h. Nadie pasa de 40 h, así que no hay horas extra FLSA. Cobertura
  4,020/3,900 = **103 %** · 8,700/8,840 = **98.4 %**.
- **Préstamo** (francés, anual): 112,000 × 0.10 / (1 − 1.1⁻⁷) = **$23,005.42** · 204,000 × 0.10 / (1 − 1.1⁻¹⁰) =
  **$33,200.06**. Interest-only = 0 y el cuadro cierra a 0.
- **DSCR**: FT (20,771 + 14,531 + 11,200) / 23,005 = **2.02×**, después 2.65× y 3.08× (mínimo 2.02×) · CAF 73,523 /
  33,200 = **2.21×**, después 2.61× y 2.88× (mínimo 2.21×).
- **Equilibrio**: margen de contribución 8.2377 · 7.2204. Contable 67.07 → **68** · 122.04 → **123** clientes/día. Caja
  65.80 → **66** · 119.09 → **120**. Holgura **21.6 %** · **17.6 %** (≥ 15 %).
- **Caja mínima**: **$24,672** (mes 4) · **$63,228** (mes 2).
- **Payback del proyecto**: 2 + (146,399 − 107,487)/70,938 = **2.5 años** · 255,956 < 263,687 → **más de 3 años**.
  Sobre CAPEX: **2.1** · **2.4**.
- **Escenarios**: FT 53 × 11.67 × 260 = $160,813 (−$49,025), 116 × 16.33 × 260 = $492,513 · CAF 112 × 10.33 × 329 =
  $380,640 (−$49,753), 161 × 11.67 × 351 = $659,483.

**Coherencia**:
- docx ↔ xlsx ↔ `cifras_caso.json`: unas 45 cifras cotejadas en cada docx, sin una sola discrepancia.
- Landings: $14, 29.3 %, 58.8 %, 68 frente a 80, $146,399 · $11, 65.6 %, 123, $263,687.
- Conteos del producto: 68 tareas (11/13/12/10/12/10) y 75 (11/13/15/12/14/10); 9 hojas; 722 y 742 fórmulas («more
  than 700»); 4 y 6 puestos; la tabla de sensibilidad tiene 20 combinaciones.

**Ficheros**:
- `gates_en.py` G1-G9 **TODO VERDE**, ejecutado en el VPS sobre un worktree limpio.
- 0 errores en caché (#REF/#NAME/#DIV/#VALUE/#N/A), 0 «€», «m²», «ChefBusiness», «v1.1», «Fichero» o normativa
  española, y 0 caracteres no latinos.
- US Letter en las 32 hojas y en los 2 docx (12240×15840); `fullCalcOnLoad=1`; sin vínculos externos; docProps D20;
  docx en-US.
- Aviso D21 en los 4 xlsx; protección sin contraseña.

**Legal**: estas afirmaciones son correctas:
- EIN gratis (IRS); 9 alérgenos con el sésamo desde 2023 (FASTER Act); workers' comp «almost every state».
- Microloan hasta $50,000; aportación propia «often around 10 %» (SBA SOP 50 10 8); sin «SBA minimum».
- UK: registro 28 días antes y gratis, en el council donde se guarda la furgoneta; VAT 20 % en comida caliente y en
  local; 14 alérgenos.
- Licencia de venta ambulante por ciudad e intransferible; commissary «most health departments»; NFPA 96 «where
  adopted»; liquor license solo si se sirve alcohol.

**Copy**:
- Sin `aggregateRating` ni `review` en el JSON-LD; Product USD 39.00.
- Testimonios marcados como «Spanish edition» y sin cifras del producto.
- Nombres y precios coherentes en ficha, hub, dashboard y correos; los 6 enlaces de venta cruzada de los correos dan
  200 en producción.

**Flujo post-pago** (`gate-flujo-postpago.py --base <preview> … --only <slug>`):
- Los dos fallan **solo por el Payment Link**: landing con `#comprar`, ausencia en `payment-links.ts` y env
  `VITE_STRIPE_PAYMENT_LINK_*` inexistentes.
- Las 3 descargas de cada uno responden (dl_ok 3/3, 200 con content-type de Office). Landing, `/access` y `/library`
  dan 200, con las puertas cripto en el HTML y `product-prices.ts` al día.
- Un 502 suelto del CAF en la primera pasada no se repitió en el reintento ni en 3 curl (transitorio del preview).
- El aviso de `stripe-webhook` 501 es global y anterior.
