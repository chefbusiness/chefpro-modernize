# Revisión adversarial final (D111): BBQ Catering Business Plan Kit (EN, $39)

> Sesión Claude Code, 24-oct-2026. Solo lectura sobre `wt-bbq/astro-site/public/dl/bbq-catering-business-plan/` (4 ficheros, sha256 = F2-NOTAS §8, Mac = VPS en `7adc0353`) y la ficha `bbq-catering-business-plan.ts`. Leído entero en el VPS: docx (110 párrafos con texto), libro (9 hojas, caché y fórmulas), calculadora (5 hojas) y checklist (68 tareas × 4 columnas). Fuentes abiertas: 25 TAC §228.221 (Cornell), boletín del Corpus Christi FD (PDF, texto extraído), DSHS Texas cottage food. Los artículos del Food Code se contrastan con lo citado en research §6.4 (no reabierto): 145/155/165 °F, 135 °F, 135→70 °F en 2 h y 41 °F en 6 h, recalentado a 165 °F, todo correcto en los 4 ficheros.

## Recálculo a mano: todo cuadra con la caché y con el docx

| Cifra | A mano | Caché / docx |
|---|---|---|
| Ventas | 150 × 75 × $38 = **427,500** ($2,850 por evento) · variables 24.64 + 4.2 + 3.5 + 0.9 + 3 + 3 = 39.24 % → margen 60.76 % | ✓ / ✓ (60.8 %) |
| Resultado | fijos 219,993.83 (D&A 10,511.43 + intereses 10,100) · EBT 39,755.17 · impuesto 25 % · neto **29,816** (7.0 %) · EBITDA 60,367 (14.1 %) | ✓ / ✓ |
| Equilibrio | contribución 38 − 14.9112 = 23.0888 por invitado · 219,993.83 ÷ 23.0888 ÷ 75 = 127.04 → **128** · caja (219,993.83 − 10,511.43 + 10,645.96) ÷ 1,731.66 = 127.12 → 128 · holgura 18.0 %, caída 15.3 % | ✓ / ✓ |
| Préstamo | necesidad 135,670.60 − 35,000 = 100,670.60 → **101,000** (sobrante 329.40 = 0.24 %) · 101,000 × 0.10 ÷ (1 − 1.1^−7) = **20,745.96** · interés año 1 10,100 · principal 10,645.96 | ✓ / ✓ |
| DSCR | (39,755.17 − 9,938.79 + 10,511.43 + 10,100) ÷ 20,745.96 = **2.43×** (año 2 3.36×; desde año 3 4.01×) | ✓ / ✓ |
| Contingencia / CAPEX | 10 % × (20,000 + 3,500 + 18,000 + 3,000 + 500) = **4,500** · 75,200 + 1,800 + 1,800 + 4,500 = 83,300 · circulante 3 × 209,482.40 ÷ 12 = 52,370.60 | ✓ / ✓ |
| Pesimista | 113 × 34.20 × 68 = 262,792.80 · EBT −60,320.92 (EBITDA −39,709) · caja 52,370.60 − 60,320.92 + 10,511.43 − 10,645.96 = **−8,084.85** | ✓ / ✓ («the cash runs out», [58], [99]) |
| Mezcla ¶56 | 48,400 + 110,250 + 87,120 + 135,200 + 46,800 = 427,770; 11,090 invitados (73.9; $38.57) · bodas 20/150 = 13 %, 135,200/427,770 = 32 % · mes mínimo 2 = $41,591; picos mayo, junio y octubre con Month 1 = marzo | ✓ / ✓ |
| Calculadora (boda) | comida 130 × $8 = 1,040 + 97.50 + 10.58 + personal ((2×21 + 5×18) × 8 + 10×21) × 1.1 = 1,392.60 + 642 = 3,182.68 · ÷ 0.5 ÷ 130 = 48.96 → **49.00** · subtotal 6,370 + 650 = 7,020 → **$54.00** repartido · SC 702 · impuesto 617.76 · total 8,339.76 · depósito 4,169.88 | ✓ (drop-off $22.50 y graduación $34.50 dentro de ±10 %) |
| Shopping list | escala lineal: 300 inv. = 150 lb cocinadas → 271.2 lb crudas (2 × 135.6); piezas con ROUNDUP; sides 18.75 gal; 10 servers | ✓ |

## BLOQUEANTE (0)

Ninguno: ni cifras mal calculadas, ni fórmulas rotas, ni temperaturas de seguridad erróneas, ni afirmaciones legales tajantes sin «ask your county / fire marshal».

## MAYOR (6)

**M1. docx [96]: «Disposables, wood and cooking fuel add 4%».** El libro dice 3.5 % (`0. Assumptions!B15`, `3-Year P&L!E15`). Causa: el token `{{consumibles_pct}}` usa el formato `pct0` (`business-plans-en/mapas.py:600`). Arreglo: formato `pct1` para ese token en el conjunto `bbq` (o texto fijo) → «Disposables, wood and cooking fuel add 3.5%». Toca la cifra impresa en el docx, no el libro.

**M2. El checklist no tiene ninguna tarea de financiación, aunque el docx la promete.** docx [114]: «"Phase 1 - Business Setup" covers the LLC, the tax registrations, the bank account and the conversation with your lender»: no hay ninguna tarea con lender, loan ni SBA en las 68. Además, el mismo párrafo dice que la Phase 3 cubre «the smoker trailer, the van…», que están en `Phase 2!B10-B12`. Y «Do not move to the next phase while the permits of the current one are still open» choca con los plazos, que se solapan (cada fase vuelve a empezar en «Week 1»). Arreglo (texto, sin cifras):
- (a) `Phase 1!B12:E12` (software, que ya está en `Startup Costs!A16`): B «Take this plan to two lenders and apply for your loan (bank or SBA 7(a))» · C «Owner / Accountant» · D «Weeks 3-6» · E «Bring the Word plan, the Excel projections and written quotes for the smoker trailer and the van. SBA 7(a) loans go through participating banks: ask what owner equity they expect and how long approval takes, and do not sign for the trailer until the loan is approved.» El software pasa a `Phase 5!E14`, añadiendo al final «Pick catering software that sends the quote, collects the e-signature and takes the deposit by card or ACH.» Hay que tocar `GBQ-check.json` y las pistas de `TAREAS` en `datos_bbq`.
- (b) docx [114] completo: «The roadmap follows the six phases of the startup checklist that comes with the kit. "Phase 1 - Business Setup" covers the LLC, the tax registrations, the bank account, the loan application, your contract and your food safety plan. "Phase 2 - Pits, Fire & Permits" covers the commissary agreement, the health permit, the fire rules, the smoker trailer and the van, and the insurance. "Phase 3 - Equipment" covers the holding and carving gear, the live-fire rig and propane backup, the meat and wood suppliers and a full test cook. "Phase 4 - Staff" covers W-2 hiring, payroll and training. "Phase 5 - Marketing" builds the website, the Google Business Profile, the directory listings, the venue and planner outreach and the first tastings. "Phase 6 - First 90 Days" runs the first events and reviews each one against the plan. The phases overlap week by week, but do not book a paid event while any permit is still open.»
- Si no se toca el checklist, quitar al menos «the loan application».

**M3. Calculadora: «Equivalent price per lb of cooked meat» engaña a un pitmaster.** Está en `Pricing Calculator!A93:C93` (por defecto $67/lb), en `3 Example Quotes!A93` ($60, $69 y $98/lb) y en `Instructions!A5`. Divide el precio todo incluido por invitado (sides, personal, margen) entre la carne, y C93 añade «the way many drop-off menus quote». Un caterer de Texas lo compara con los precios por libra de su carta (solo carne; los sides van aparte) y ve un precio absurdo. Arreglo (texto):
- A93 «All-in price per lb of cooked meat (sides, staff and margin included)».
- C93 «The price per guest divided by the cooked meat per guest. It includes sides, staff, travel and margin, so do not compare it with by-the-pound menu prices for meat alone.»
- `Instructions!A5`, última frase: «The tab also shows that price per cooked lb, all-in: not comparable with by-the-pound menu prices.»
- Landing (`:100`, `:242`, `:275`): «its all-in equivalent per pound of cooked meat»; título de la razón (`:275`): «BBQ Catering Prices per Guest, Drop-Off vs. Full-Service».
- Si el autotest busca el rótulo, actualizarlo.

**M4. Landing, FAQ «Does it work in the UK, Canada or Australia?» (`:148`): «The calculator gives pounds with kilograms and degrees Fahrenheit with Celsius alongside».** Es falso: la calculadora no tiene ningún kg (trabaja en lb, oz y galones); solo las temperaturas llevan °C. Arreglo: «The calculator works in pounds, ounces and gallons (1 lb = 0.454 kg; 1 gallon = 3.8 liters), shows every temperature in °F with °C alongside, and counts miles, so type kilometers and your cost per km instead.»

**M5. Libro, `Instructions!D64`: «Median hourly wages for restaurant cooks…, nonrestaurant food servers… and chefs and head cooks».** $18.62 y $17.37 (B64) son MEDIAS (research §5: la mediana de cooks es $17.98); solo los $30.03 de chefs son mediana. El docx [88] lo dice bien («mean»). Arreglo: «Mean hourly wages for restaurant cooks (35-2014) and nonrestaurant food servers (35-3041), and the median for chefs and head cooks (35-1011); 75th percentile $21.45 for cooks and $18.51 for servers.» El resto del texto, igual. Sin cifras.

**M6. `Staffing!J19` contradice el promedio, la regla de 1 server por 25-30 invitados y la propia calculadora.** Texto: «about 1.5 on a drop-off, 3 on a staffed buffet, 4 on a full-service company event, 5 at a wedding and 4 on a live-fire booking». Ponderado con la mezcla del ¶56 sale 2.9, no los 3.4 de B19. Una boda de 130 invitados con la regla de 25-30 necesita 5 servers más el pit, y la boda de ejemplo de la calculadora lleva 2 + 5 = 7. Arreglo (texto; el promedio 3.4 se queda): «Average number of people working each event: about 1.5 on a drop-off, 3 on a staffed buffet for 70, 5 on a full-service company event, 7 at a wedding with the live pit (2 on the pit and 5 servers, as in the calculator's example) and 5 on a live-fire booking (Kit estimate). Weighted by the example mix in the Word plan, that averages about 3.4. Raise it for bigger events: the staffing sizes itself.» (Ponderado: 507.5 ÷ 150 = 3.38.)

## MENOR (18)

1. **docx [104] «with daily logs»**: §228.221(b)(1) pide presentarse a diario en la instalación, no llevar un registro. Texto: «must operate from a central preparation facility or another fixed food establishment and report to it daily for supplies, cleaning and servicing, with a hand sink and potable water, and needs a Certified Food Protection Manager certificate for its permit (25 TAC section 228.221).»
2. **docx [102] «and why that agreement comes before your business license»** → «…before your health permit». La business license está en `Phase 1!B10` y el acuerdo de commissary en la Phase 2.
3. **Workers' comp y Texas** (el comprador tipo): docx [88] «is required in nearly every state» → «is required in nearly every state (Texas is the exception: coverage is optional there, but venues and lenders often ask for it)». Igual en [107] y en `Phase 2!E15`.
4. **CDL** (docx [108] y `Phase 2!E11`) solo habla de la van. Texto: «Federal rules require a commercial driver's license only at 26,001 lb or more (for a pickup and trailer, a combined rating of 26,001 lb or more with a trailer rated over 10,000 lb), which a cargo van or a pickup towing a smoker trailer does not usually reach. If you tow across state lines and the pickup and trailer are rated over 10,000 lb combined, federal motor carrier rules (a USDOT number and a DOT medical card) may apply: check with FMCSA and your state.»
5. **`Phase 2!E9`**: «Also ask venues about burn bans and cooking under tents» → «Check your county's burn ban order before every event (some allow cooking in a closed smoker or grill, others do not) and ask venues about cooking under tents.» Y «about 10 ft of clearance» → «10 ft between your pit and other vendors». El boletín dice «between individual vendors and their equipment».
6. **Arrastre**: «tows at least 3,000 lb (1,360 kg)» (`Startup Costs!D7` y FAQ de coste de la landing, `:92`). El TS500 ya pesa 2,800 lb de envío (research §4), antes de leña, agua y upfit. Texto: «tows at least 5,000 lb (2,270 kg); check the loaded trailer weight against the pickup's rating». Es un Kit estimate, sin fuente.
7. **Calcos y británico**:
   - [49] «to the pack-down» → «to the cleanup»; [80] «then pack-down» → «then breakdown».
   - [43] «The founding team is short.» → «…is small.»
   - [82] «tables, linens and chafing fuel we do not own» → «tables, linens and any chafing dishes we do not own».
   - [62] «a single packer» → «a single meatpacker» (se confunde con la packer brisket).
   - [80] «One, the briefing» y `Phase 6!B5` «Hold the client briefing 3 weeks out» → «the final planning call (with the client) 3 weeks out».
   - `Phase 5!E13` «text or SMS» → «text messages».
8. **docx [41]** repite «The cash needed at opening is $135,671» justo después de «The total startup investment is $135,671»: borrar la segunda frase (y la misma en [94]). El orden de [41] pone «the live-fire rig ($4,500) and the launch budget» detrás del launch, que es de $5,000: «the launch budget ($5,000) and the live-fire rig ($4,500)».
9. **Orden del checklist**:
   - `Phase 1!B5` dice «with your accountant» en la Week 1, pero el contable se contrata en B11 (Weeks 3-4). Además, «LLC or S corp» mezcla entidad y elección fiscal → «Choose your legal structure: an LLC, with or without an S corp election», y subir B11 a la Week 1.
   - `Phase 4!D9` vincula el workers' comp a la nómina en las Weeks 3-5, antes de comprarlo en `Phase 2!D15` (Weeks 6-10) → D15 «Weeks 3-5».
   - `Phase 3` fila 10 (Weeks 2-4) va detrás de la fila 9 (Weeks 4-6): subirla.
   - `Phase 6` fila 11 (cobrar el saldo 3-14 días ANTES del evento) va detrás de las tareas del día: subirla detrás de la fila 6.
10. **`3 Example Quotes!A2` y `B115:B117`**: «the workbook's example mix» no existe (el libro solo tiene el B5 combinado de $38) → «the example mix in the Word plan (section 3)».
11. **Libro, `Instructions!D59`**: «300 guests need roughly 200 lb (91 kg) of raw meat» (Dr. BBQ con ¼-⅓ lb), mientras que la shopping list da 271 lb a 8 oz. Añadir: «at 1/3 lb cooked per guest; at the calculator's 8 oz, about 270 lb (123 kg)».
12. **Aviso del coste provisional**: el precio por invitado (B92) no avisa a su lado de que usa el Kit estimate. B83 está 9 filas más arriba y A116 al final. Añadir a C92: «While "Meat prices" says Missing, this price uses the package food cost estimate, not your meat prices.» Con este aviso, el placeholder ($6.50 / $8 / $17) no se lee como un precio inventado.
13. **`Pricing Calculator!A37`, «Rentals passed through»**: entran en el coste directo y llevan el margen objetivo (en la boda, los $600 se facturan como unos $1,200). Texto: «Rentals for this event (your cost; they carry your margin)». La alternativa, sacarlos del margen, es una fórmula.
14. **`Shopping List!A35`**: los hot boxes solo cuentan las bandejas de carne. G35: «Meat pans only: add carriers for hot sides such as mac and cheese and beans.»
15. **Salchicha de ave**: `Meat Yield!G18` y `Instructions!A12` → «155 °F (68 °C) for 17 s (ground meat, sausage included; 165 °F if it is chicken or turkey sausage)».
16. **Drop-off sin personal**: falta cuánto aguanta la comida fuera del hot holding. `Phase 3!E13`, añadir: «Label each pan with the time it left hot holding and a discard time 4 hours later, or leave chafing dishes; ask your county whether it accepts time as a public health control (Food Code 3-501.19).»
17. **Landing**:
   - `:144` «the share of add-ons» → «the split between BBQ packages and add-ons» (B12 es una fórmula).
   - `:242` «Out come raw and cooked pounds per cut» → «Out come raw pounds and pieces per cut and the total cooked pounds».
   - `:152` «The files have no currency symbol» → «The Excel cells have no currency symbol, so you type amounts in your own currency; the Word plan's example is in US dollars.»
18. **Nota UK y unidades**:
   - docx [108] «charge VAT at 20% on event catering» → «…once you are VAT-registered».
   - Las temperaturas del checklist (`Phase 1!E14`, `Phase 3!E6/E14`, `Phase 6!E8`) van sin °C, a diferencia del docx: añadir «(63 °C)», «(57 °C)», etc. Opcional.

## Comprobado sin hallazgos

- **Unidades**: lb, oz, gal, millas y °F como unidades principales; ninguna métrica sola. Los kg, los litros y los °C siempre van entre paréntesis o en su propia columna.
- **Limpieza de texto**: 0 «€», 0 español y 0 calcos «D-21» (P6 usa «3 weeks out…»). Solo aparecen «BBQ food trucks» como no comprador, «carving station», y «chefs and head cooks» únicamente en la fila OEWS. Ni «grill master», ni «support kitchen», ni «Cambro», ni «freelance».
- **Calidad frente a mínimo**: la calidad y el mínimo del Food Code van en columnas distintas en los 13 cortes. Tri-tip, picanha y tomahawk se quedan en 145 °F, con la nota de «check your county».
- **Rendimientos**: brisket y pork butt al 50 % con fuente; el resto, Kit estimate. Whole hog al 35 % y sausage al 88 % son razonables.
- **«Start the pit by»**: correcto (brisket 03:00 «Event day» para servir a las 18:00) y salta a «Day before» cuando toca.
- **Checklist**: 68 tareas (11/13/12/10/12/10). EIN después de la LLC; nada de bar, catering emplatado ni food truck.
- **Landing**: las cifras del bloque `CASO` coinciden con la caché. También se cumplen los 13 cortes, los 10 menu styles, el 1.25×, las 9 hojas, «more than 700» (722 fórmulas), el depósito del 50 % no modelado (así lo dice), el Insureon y los $8,495-$20,395 (research §4), la nota UK y la guía de equivalencias (`get-download-urls.ts:856`).
- **Fuentes**: Class K de 2.5 gal (9 L) para fogones de combustible sólido, 2A10BC, 10 ft y 200 lb de LP-gas (IFC 906.4.1 / 319.8.1, boletín del Corpus Christi FD). La exclusión de carne y aves del cottage food de Texas, verificada.

## Veredicto

**Listo tras arreglos de texto.** Los 6 MAYOR y los 18 MENOR se arreglan con texto. M1 cambia el formato del token en el ensamblado del docx (de 4 % a 3.5 %), no el libro. M2 cambia una tarea del checklist, sin tocar los recuentos (11/68). Ninguna fórmula ni ninguna cifra del caso cambia. Después hay que volver a pasar `gates_en`, `ensamblar_docx --autotest`, `calculadora --autotest` (por si busca el rótulo de A93) y `barrido_bbq.py`, y actualizar los sha256 en F2-NOTAS §8.
