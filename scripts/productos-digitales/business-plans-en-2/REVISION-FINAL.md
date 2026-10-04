# Revisión adversarial final — Restaurant y Bakery Business Plan Kit (EN) · 4-oct-2026 · sesión Claude Code

Una ronda sobre `feat/business-plans-en-2` @ `2dec08df` (PR #111). Los 6 ficheros publicados tienen el mismo sha256 en
el Mac y en el VPS (los de `F2-NOTAS.md` §7.6). En el VPS, en un worktree limpio (`/root/wt-bp2rev`, ya borrado), volqué
fórmulas y caché con openpyxl (`data_only`) y los docx con python-docx. **Las cifras están recalculadas a mano** desde
los inputs, no copiadas de la caché. Corrí `bp2.py gates_en` y salieron **G1-G9 TODO VERDE**. Lentes: prestamista/CPA,
inspector/abogado, ficheros y copy.

**Veredicto: se puede vender tras una ronda corta de textos (unos 30-45 min, sin tocar fórmulas ni estructura).** No
encontré ningún bloqueante. Hay 2 mayores: uno es una repetición parcial del B1 de los hermanos y el otro es un error de
calendario del checklist que afecta a un comprador de EE. UU. Los números cuadran al dólar entre xlsx, docx,
`cifras_caso.json`, fichas y hub. De lo que ya se cazó en FT/CAF, quedan restos menores de m7 (C corp), m16 (FHRS) y m17
(EIN).

---

## BLOQUEANTE

Ninguno.

## MAYOR

### M1 · Licencia de alcohol en el checklist del restaurante: fase 6 y «1 day»
- **Dónde**: `restaurant-opening-checklist.xlsx` → `Opening Checklist!B60/D60` (fase 6, «Obligations to close before
  opening (months 6-8)», Timing **«1 day»**). Ninguna tarea de la fase 2 pide la licencia.
- **Por qué importa**: el mismo kit dice otra cosa en tres sitios:
  - docx §9 [119]: «the item most likely to set the opening date… Expect months of processing».
  - docx §10 [128]: la fase 2 incluye «the start of… the liquor license application».
  - FAQ de la landing «How do I open a restaurant»: «Apply for your liquor license early».

  Un comprador que siga el checklist pediría la licencia en el mes 6-8 pensando que es un trámite de un día. En muchos
  estados tarda de 3 a 12 meses (con cupo, además hay que comprar un traspaso), y eso retrasa la apertura con el alquiler
  ya corriendo. Es la herencia de la tarea ES «cartel de prohibición de venta de alcohol a menores» (1 día).
- **Arreglo (solo texto, por `POR_CELDA`)**:
  - `B60`: «Liquor license: apply right after signing the lease (state alcohol agency + local approval); have it issued
    and posted before opening, with age-restriction signage».
  - `D60`: «Start in Phase 2: often 3-12 months».
  - `F60`: empezar con «Apply as soon as the lease is signed: it is often the longest wait.»
  - Docx [128]: si no se crea tarea en la fase 2, cambiar «Phase 2 … covers … the liquor license application» por «Phase 6
    … covers … the liquor license (apply as soon as the lease is signed)». Sin cambiar estructura, la tarea sigue
    contando en G1.

### M2 · Repetición parcial del B1: `Instructions!A7` del restaurante sigue vendiendo «the four alternative financing sources»
- **Dónde**: `restaurant-financial-projections.xlsx` → `Instructions!A7`: «…and the four alternative financing sources
  on "7. Financing"». En la panadería (`Instructions!A7`) y en FT/CAF está corregido: «rows 8-11 count as sources but are
  not amortized: Your bank or SBA 7(a) loan goes in "Loan requested" on "0. Assumptions"».
- **Por qué importa**: es justo la frase que la revisión de FT/CAF metió en el B1. Las Instrucciones son lo primero que se
  lee y empujan a teclear el préstamo SBA en las filas 8-9, que no se amortizan. El riesgo queda mitigado porque
  `7. Financing!A7:A9`, `C8`, `C9`, `C18` y `0. Assumptions!C31` sí están bien.
- **Arreglo**: el mismo texto de la panadería en RESTP `Instructions!A7`, adaptando las pestañas numeradas
  («"3. Break-Even"», «"4. Scenarios"», «"6. 12-Month Cash Flow"», «"7. Financing"»).

## MENOR

| # | Dónde | Qué | Arreglo |
|---|---|---|---|
| m1 | RESTC `Opening Checklist!C47`, `C48`, `C74` | El responsable sale como «Equipment» (soft opening, grand opening, reseñas). Una sola cadena ES «Equipo» (c0746) sirve de categoría (col. A, filas 27-30) y de responsable; aquí es «Team» | `POR_CELDA` RESTC C47/C48/C74 → «Team» |
| m2 | Docx REST [107] y PAN [103]; `F2-NOTAS` §7 dice «25 % de C corp» | **Resto de m7**: el docx aplica «an effective 25%» sin decir que es una C corporation, y §9 ([115] REST, [106] PAN) recomienda LLC o empresario individual. Además, el dueño cobra nómina W-2 | Lo mismo que FT/CAF: «(a C corporation example; pass-through owners set it to 0 and pay tax on the profit personally)» |
| m3 | Docx REST [115] | **Resto de m17**: el EIN «is needed to hire employees and to pay sales and excise taxes». El sales tax es estatal (el texto de la panadería [106] está bien) | «…to hire employees and to file federal employment and excise tax returns» |
| m4 | RESTC `F21` «Food Hygiene Rating (1-5)»; docx PAN [110] «from 1 to 5» | La escala FHRS va de **0 a 5** (0 = urgent improvement necessary). La parte de Escocia (FHIS) sí está | «(0-5)» / «from 0 to 5». El origen es `F1-research-us-delta.md` l. 107 «FHRS 1-5»; revisar también FT/CAF |
| m5 | Docx REST [101] | «the head chef and the **floor lead** join» dos meses antes. Staffing no tiene jefe de sala (R5); el organigrama [99] ya se corrigió | «the head chef and a lead server» |
| m6 | Docx REST [101] vs `1. Startup Costs` | El docx incorpora al chef dos meses antes de abrir y al resto del equipo una semana antes. Esa nómina previa a la apertura (≈ $15,000-20,000) no está en los costes de arranque, y el P&L empieza el día de apertura (`D12`). Un CPA lo echa en falta en los usos de fondos. El fondo de maniobra lo absorbe: saldo mínimo $124,652 | Una frase en [106] o [109]: «pre-opening payroll and training come out of the working capital reserve», o quitar los plazos de [101] |
| m7 | RESTP `0. Assumptions!C24` vs docx REST [81] | La nota dice «(NNN rent plus CAM charges, if your lease has them)» y el docx dice «it is base rent only. If the lease is triple net (NNN), we add…». El research (l. 139) confirma que son $30/sq ft NNN, es decir, sin CAM ni impuestos. Con $6-12/sq ft de CAM/NNN (+$17-34K al año), el neto del año 1 baja de 7.9 % a 6.7-5.5 % y la holgura de caja de 21.5 % a 18-15 % | Alinear C24 con el docx: «The example is base rent only: add NNN / CAM charges (property tax, building insurance, common-area maintenance) here». Es la misma decisión que m5 de CAF |
| m8 | RESTP `Instructions!C51`, `C52` | La fuente del food cost 25-35 % y del personal 25-33 % es «**Papaya (papaya.co.th)**», un blog de un TPV tailandés. Le resta credibilidad ante un banco de EE. UU. justo en el bono 2 «(Sourced)» | Citar una fuente US (Restaurant365 o Toast ya se usan) o poner «Kit estimate» |
| m9 | Ficha REST, bono 2 «**US Market Data** & Industry Benchmarks (Sourced)», $29, contado en «Total value $158» | El §3 del docx dice que no cita ningún dato nacional («We do not quote a single national establishment count or sales total here»). La tabla D19 tiene 10 filas, 4 de ellas «Kit estimate» y 2 de Papaya. El título promete más de lo que hay, y además se cuenta dos veces (igual que el m19 de FT/CAF, que quedó para John) | Título como el de la panadería («Restaurant Industry Benchmarks (Sourced)»). El valor de $29 es decisión de tienda |
| m10 | PANP `3-Year P&L!F10` | «Many states exempt bakery goods sold to go and tax what is eaten in the shop (**California, for instance, does so with its 80/80 rule**)». La regla 80/80 de California hace lo contrario: si más del 80 % de las ventas son comida y más del 80 % de esa comida es gravable, la comida fría para llevar también tributa. No es la regla que exime la bollería para llevar | «(California, for instance; under its 80/80 rule, a shop whose food sales are mostly taxable may have to tax cold food to go as well)» |
| m11 | PAN: docx §6/§9, `Startup Costs`, PANC `Phase 2!E14` | Ni rastro del **separador de grasas**. Muchos programas municipales de FOG lo exigen a cualquier establecimiento alimentario, también a obradores (mantequilla, lavado de amasadora). La nota E14 dice «no used cooking oil to manage», pero eso no exime del interceptor | E14 o docx [107]: «ask the plumbing department whether a grease interceptor is required (many cities require one for bakeries too)» |
| m12 | PANP `0. Assumptions!C14` | «inside the **25-30%**… for coffee», con B14 = **22 %** y la tabla (`Instructions!B57`) ya en 20-30 %. La F2 corrigió F11 y la tabla, pero no esta nota | «inside the 20-30%…» |
| m13 | PANP `Staffing!J23` (y J21) | «The head baker alone. If your bakery starts with two people, raise it here», con **B23 = 2**. J21 «one fixed person plus reinforcement» con B21 = 2 (calibración D15 de la F2) | J23: «The head baker and the baker»; J21: «two people on average…» |
| m14 | PANP `Instructions!D47` vs `0. Assumptions!B58/C58` | D47 dice que la media ponderada de cobro es «a few days»; B58 = 1 y C58 «about a day» | «about a day» |
| m15 | PANP `Instructions!D46` | «Year 2 … is the year when loan repayment weighs the most»: con cuota anual constante y sin carencia, el servicio de la deuda es igual todos los años (herencia ES) | Quitar la subordinada |
| m16 | PANC `Phase 2!E13` | La nota de «Ingredient and allergen labels…» es la genérica de carteles («federal and state labor law posters… If you serve alcohol, your state liquor license…»). No viene a cuento en una panadería sin alcohol | `POR_CELDA`: «Label packaged and wholesale items with the ingredient list, net contents and the 9 major allergens (FDA); your health department may ask for more» |
| m17 | RESTC `F14` | La tarea B14 habla de «owners' draws and self-employment tax», pero la nota es la de alta como empleador («Registration steps and unemployment insurance rates…») | «Owners of an LLC or sole proprietorship are not on payroll: they take draws and pay self-employment tax. Ask your accountant how to set it up» |
| m18 | Docx PAN [114] | «the pessimistic case of 140 transactions a day **shows how much room we have** if the counter builds slowly»: en ese caso la caja se agota (−$63,796). [103] sí lo dice | «…shows what happens if the counter builds slowly: without corrective action, the reserve runs out» |
| m19 | Docx REST [122] | «under the **Licensing Act 2003**»: esa ley solo rige en Inglaterra y Gales (Escocia: Licensing (Scotland) Act 2005; Irlanda del Norte, régimen propio) | «(England and Wales; Scotland and Northern Ireland have their own licensing laws)» |
| m20 | Uso de fondos (los dos) | Con un SBA 7(a), la comisión de garantía de la SBA y los costes de cierre (varían con el importe y el año fiscal) no aparecen en los usos. El banco suele financiarlos dentro del préstamo | Nota en `7. Financing!C14` o en el docx: «with an SBA 7(a), add the SBA guarantee fee and closing costs to your startup costs» |
| m21 | Fichas: testimonios | «they approved the loan **in 10 days**» (REST) y «approved EUR 65,000 of financing» (PAN): en EE. UU., un testimonio de resultado se lee como resultado típico (FTC, 16 CFR 255.2). Se mitiga porque llevan «Spanish edition» y existe «approval is never guaranteed». R12/D26 ya anotado | Decisión de John; lo mínimo, quitar «in 10 days» |
| m22 | `7. Financing!C9` (los dos) | «up to **$50,000**»: el changelog y la FAQ prometen «No currency symbol in the workbooks» | «up to 50,000» (o matizar el changelog) |
| m23 | Docx PAN [103] | El optimista da transacciones y resultado, pero no ticket ($10.91) ni días (320) (m2 de FT/CAF); el pesimista sí | Añadir «at $10.91 over 320 days» |
| m24 | PANP `Instructions!D66` | «A bakery takes longer to pay back its investment than a coffee shop»: en la propia tienda, el payback de la panadería es de 2.6 años y el de la cafetería de 2.9 | Quitar la comparación |
| m25 | RESTP, orden de pestañas | `Instructions` queda entre `5. Staffing` y `6. 12-Month Cash Flow` (heredado del ES; D33 la lista la última) | Cosmético; si se toca, es una excepción estructural. Se puede dejar |

Observación (no exige cambio, como el m20 de FT/CAF): el caso REST sale en el lado optimista para un banco. El prime cost
es 58.4 %, por debajo del 60-65 % (el docx [108] lo declara). Hay 10 personas (7.95 FTE) para 2 servicios × 12 h × 310
días con barra, el EBITDA es del 17.6 % y el seguro es de $9,000 con liquor liability. Además, el food cost se calibró de
30 a 29 % para pasar el umbral del 65 %. Todo está dentro de rangos con fuente y declarado, pero un prestamista
escéptico preguntará por la plantilla.

---

## Lo que SÍ está bien (comprobado)

**Recalculado a mano (Restaurant · Bakery):**
- **Ventas año 1**:
  - 125 × 28 × 310 = **$1,085,000**; años 2-3: $1,193,500 / $1,265,110.
  - 210 × 10 × 310 = **$651,000**; años 2-3: $729,120 / $780,158.
- **Variables y margen bruto**:
  - REST 220,255 + 78,120 + 16,275 + 0 + 37,975 + 21,700 = 374,325, margen bruto **65.5 %**. COGS 27.5 %; prime cost
    27.5 + 30.9 = **58.4 %**.
  - PAN 166,005 + 21,483 + 19,530 + 0 + 22,785 + 13,020 = 242,823, margen bruto **62.7 %**. COGS 28.8 %.
- **Inversión** (partidas sumadas una a una):
  - REST: CAPEX **$388,700** (153,800 + 102,000 + 81,400 + 16,000 + 17,500 + 18,000), con la licencia de alcohol de
    $15,000 en `1. Startup Costs!B42` (no amortizada, sin impuesto), más fondo de maniobra 3 × (597,021 − 37,037)/12 =
    **$139,996**. Total **$528,696**.
  - PAN: CAPEX **$182,500** + fondo **$84,209** = **$266,709**.
  - Bases amortizables: 179,800/10 + 133,400/7 = **$37,037** · 70,400/10 + 88,500/7 = **$19,683**.
- **Fijos**: **$597,021** (REST) · **$356,519** (PAN), sumados línea a línea.
- **Resultado**:
  - BAI $113,654 · $51,658; impuesto 25 %; neto **$85,240 (7.9 %)** · **$38,744 (6.0 %)**.
  - Años 2/3: $134,419 / $165,663 · $71,907 / $92,427.
  - EBITDA $190,591 (17.6 %) · $91,041 (14.0 %).
- **Sales tax fuera de ingresos; lo liquidado es lo cobrado**:
  - REST: cobrado 1,085,000 × 8 % = **$86,800**. Liquidado en el año: T1 13,976 (`E19` = suma de los meses 1-3) +
    T2 23,184 + T3 22,449 = 59,610. El T4 ($27,190) se paga en enero.
  - PAN: 553,350 × 1.6 % + 97,650 × 8 % = **$16,666** (tipo efectivo 2.56 %). Liquidado 2,926 + 4,220 + 4,085; T4
    $5,434 en enero.
  - El precio con impuesto: $30.24 · $10.256.
- **E2**: REST `G14:G15` y PAN `G13:G14` = `$B$41` = 0. La fila 17 (soportado) es 0 todo el año y las compras salen
  con (1 + 0).
- **E3**: `G10` = H10 × 0 + (1 − H10) × B39 = 0.2 × 8 % = **1.6 %**. La base del impuesto es solo la parte no exenta
  (20 % de la línea de panadería) y el café tributa entero (prudente: en CA el café para llevar está exento).
- **E4**: `C13` = SUMPRODUCT = **7.95** (1 + 1 + 2 + 2 + 2 × 0.5 + 0.75 + 0.2) · `C11` = **5.56** (1 + 1 + 1 + 3 × 0.67
  + 0.4 + 0.15). Las horas del propio libro (15,900 · 11,120 ÷ 2,000) dan lo mismo.
- **Nóminas**:
  - $334,884 · $220,836 (bruto × 1.10 × 12).
  - Ningún sueldo bajo el suelo: el más bajo es $15.60/h en REST (servers, part-time, dishwasher, relief) y $15.52/h en
    PAN (counter staff, 3 × 0.67 FTE).
  - Sin tip credit (nota `5. Staffing!J9`, D38), cargas del 10 % y nadie pasa de 40 h.
  - Cobertura **107 %** (15,900 / 14,880) · **112 %** (11,120 / 9,920).
- **Préstamo** (francés, anual, 10 años al 10 %, sin carencia):
  - 399,000 × 0.1 / (1 − 1.1⁻¹⁰) = **$64,935.41** · 197,000 → **$32,060.84**.
  - Intereses del año 1: 39,900 · 19,700. El cuadro cierra a 0.
- **DSCR** (después de impuestos), año a año:
  - REST (85,240 + 37,037 + 39,900) / 64,935 = **2.50×**, después 3.22× y 3.66×; mínimo de la vida del préstamo 2.50×.
  - PAN 78,126 / 32,061 = **2.44×**, después 3.43× y 4.03×; mínimo 2.44×.
- **Equilibrio**:
  - Margen de contribución 18.34 · 6.27.
  - Contable 105.01 → **106** cubiertos ($911,483) · 183.42 → **184** transacciones ($568,611).
  - Caja (+ principal − amortización) 102.90 → **103** · 179.66 → **180**.
  - Holgura **21.5 %** · **16.9 %** (≥ 15 %).
  - Rotaciones: 1.84 implícitas, 1.51 para el equilibrio de caja, techo 3 (68 plazas = 15 mesas × 4 + 8 taburetes).
- **Caja**: mínimo **$124,652** · **$76,772** (mes 2). Cierre del mes 12: $308,868 · $161,114. El flujo del año 1
  ($168,872 REST) cuadra con neto + amortización − principal + impuesto diferido + T4 + desfases de cobro y pago.
- **Payback**: REST 2 + (528,696 − 371,030) / 237,342 = **2.7** (CAPEX 2.1) · PAN 2 + (266,709 − 188,180) / 129,214 =
  **2.6** (CAPEX 1.9).
- **Escenarios**:
  - REST 91 × 24.46 × 300 = $667,758 (−$159,640, caja −$7,642) · 148 × 28.46 × 320 = $1,347,866.
  - PAN 140 × 7.64 × 300 = $320,880 (−$155,327, caja −$63,796) · 233 × 10.91 × 320 = $813,450.
- **Fondos**: 130,000 + 399,000 = 529,000 frente a 528,696 (+$304; aportación del 25 %) · 70,000 + 197,000 frente a
  266,709 (+$291; 26 %).

**Coherencia**:
- docx ↔ xlsx ↔ `cifras_caso.json`: unas 40 cifras cotejadas en cada docx, sin una discrepancia (inversión y partidas,
  ventas de los 3 años, márgenes, prime cost, equilibrios, caja mínima, DSCR, cuota, payback, escenarios, plantilla y
  cobertura).
- Fichas:
  - REST: $28.00, 65.5 %, 106 frente a 125, $528,696 ($388,700 + $139,996), $15,000.
  - PAN: $10.00, 62.7 %, 184 frente a 210, $266,709 ($182,500 + $84,209).
- Conteos: 9 hojas; 772 / 737 fórmulas («more than 700»); 64 tareas [10, 8, 8, 7, 8, 15, 8] y 66 [11, 12, 12, 10, 11,
  10]; 7 y 6 puestos con los mismos rótulos en ficha, FAQ, grid y dashboard; 10 secciones.

**Ficheros**:
- `gates_en` G1-G9 **TODO VERDE**: G1 con E2/E3/E4, G6 con 0 diferencias con la referencia ES recalculada, G9 con 0
  defectos y 0 no latinos.
- 0 errores en caché. Sin «€», «m²» ni «ChefBusiness» en los 6 ficheros (D34 aplicado: A1 «AI Chef Pro» y pie
  aichef.pro). El docx no tiene restos en español.
- US Letter en las 27 hojas y en los 2 docx (12240×15840). `fullCalcOnLoad=1`, sin vínculos externos, protección sin
  contraseña.
- docProps (D20: título, asunto v2.2, keywords y en-US en los docx) y aviso D21 en `Instructions` de los 4 libros.
- DV del checklist del restaurante `✓,—,N/A` (D35) con su contador; la panadería tiene `✓,☐,N/A` por fase.

**Ya resuelto de lo cazado en FT/CAF**:
- Préstamo = fila 7 con rótulos y notas (A7-A9, C8, C9, C18, C31; salvo M2).
- Tarjeta 3.5 % combinada, sin aritmética.
- B58 = 1 con su nota (REST).
- Notas C18, C21 (pagas mensuales) y C52 (la rampa conserva el total).
- Docx con cuota «annual equivalent» y escenarios con caja estimada.
- Sin «regular price» en los 2 correos.
- Carrusel EN solo Excel + Word (`PlanNegocioLandingPage.astro` l. 194-201).
- Bono 1 «Included in the plan» y total $158.
- Sin `aggregateRating` ni `review`, Product USD 39.00.
- FHIS de Escocia en REST.

**Legal, correcto**:
- 21 CFR 1.226-1.227 (exención de retail food establishment: ventas a consumidores > ventas al resto).
- Cottage food frente a obrador comercial (D39), con health department o agricultura según el estado.
- Plan review → food establishment permit; certificate of occupancy tras las inspecciones finales.
- Type I hood / UL 300 / NFPA 96 «where adopted»; grease interceptor «where the code calls for one» (REST).
- Licencia de alcohol estatal + local, con cupo, liquor liability y servicio responsable; $15,000 siempre presentado como
  ejemplo de estado sin cupo (fila, tabla D19, §9, FAQ y changelog).
- Tip credit federal ($2.13 / $5.12) y los 7 estados sin él (DOL).
- I-9, W-4, new-hire reporting, workers' comp «almost every state», CFPM y food handler.
- 9 alérgenos con sésamo; Bill Emerson.
- UK: 28 días, VAT 701/14 (frío para llevar zero-rated, en local y caliente al 20 %), 14 alérgenos.

**Copy**:
- FAQ verificadas contra los ficheros (salvo M1). DSCR 1.25×, Microloan hasta $50,000 y «lender-ready, approval never
  guaranteed».
- Testimonios marcados «Spanish edition», sin cifras del producto ES (con la salvedad de m21).
- Las rutas de descarga de `get-download-urls.ts` coinciden con los nombres D32.
- Los 11 enlaces de los correos apuntan a landings EN que existen en el repo.

**Pendiente fuera de esta revisión**:
- Verificación humana del alto de filas en Excel y a 360 px.
- Gates contra preview (no hay preview del #111, `F3-NOTAS.md`).
- Payment Links de John.
