# Wedding Venue Business Plan Kit (EN) — SPEC DELTA (F1 · 27-oct-2026 · sesión Claude Code)

> Edición EN (EE. UU.) de `plan-negocio-finca-eventos-bodas` 1.0 (45 €), **duplicada del ES LIVE ya revisado**. **Mandan las SPEC
> heredadas** (`../business-plans-en/SPEC.md` D1-D29, `-2/` D30-D47 = **Bakery** (estructura del libro), `-3/` D48-D65, `-4/`…`-7/`,
> `-8/` D133-D155 = **Pizza** (código y método)): aquí solo lo que cambia frente a la Pizza EN. Base: `F1-inventario-delta.md`
> (= **inv. §n**) y `F1-research-us-delta.md` (= **research §n**; manda en caso US, jerga y riesgos). Tamaño **M**: F2 ≤ 1,3 M ·
> F3 ≤ 0,6 M · ≈ 3,5 h; +30 % → se para y se reporta. «decisión SPEC» = choque resuelto aquí. Decisiones **D156-D185**.

## 0. Jerga (John, 13-oct) — manda sobre todo

Glosario obligatorio = **research §9** entero (28 términos + «(e) no se traducen literalmente»), pegado en `BRIEF-TRADUCTORES.md`
(lo escribe el paso 1a de F2, como la pizza) y añadido a `../GLOSARIO-JERGA-ES-EN.md`: «wedding venue» en nombre, H1 y ficheros,
«event venue» como descriptor, «venue» en prosa; **guests · revenue per guest · events per year** (nunca «covers» ni «average
check»); **venue rental fee / site fee**; **exclusive caterer** y **caterer commission** (nunca «canon» ni «royalty»); **retainer**
(nunca «non-refundable» sin el matiz de research §6.7); **seasonal W-2**. Unidades D14: sq ft con m² entre paréntesis donde haya
superficie. Sin tildes.

## 1. Producto (D156-D158)

| D | Tema | Decisión |
|---|---|---|
| D156 | Nombre y URLs | **Wedding Venue Business Plan Kit** · slug/productId `wedding-venue-business-plan` · JWT `wedding-venue-business-plan-jwt` · `/en/digital-products/wedding-venue-business-plan` (+ `/access`, `/library`) · gemelo ES `/plan-negocio-finca-eventos-bodas`, hreflang recíproco (**el ES tiene hoy `locales=['es']`**: F3 lo pasa a `alternatesFamilia`, como PIZ D152) · env `VITE_STRIPE_PAYMENT_LINK_WEDDING_VENUE_BUSINESS_PLAN` · conjunto **`wed`** |
| D156b | SEO | Title «Wedding Venue Business Plan Template: Word + Excel Projections, Pricing Calculator & Rental Agreement \| AI Chef Pro» · **H1 Forma B** `Wedding Venue ` + oro `Business Plan` + «Template for an Event Venue with an Exclusive Caterer: Word Plan + Excel Projections + Pricing Calculator + Venue Rental Agreements + Startup Checklist» · meta, 6 H2, 3 alt y keywords **tal cual research §9** (= docProps) |
| D157 | Precio | **$49** pago único (John: escalera EN = planes $39, este $49 por 5 ficheros, como 45 € frente a 35 €): sin `priceOld`, «-70 %», «Total value», «Save $», «worth $X» ni precio en bonos; sin rating ni review |
| D158 | Ficheros (`dl/wedding-venue-business-plan/`): **5 + guía común** | `wedding-venue-business-plan.docx` «Wedding Venue Business Plan (10 Sections)» · `wedding-venue-financial-projections.xlsx` «Wedding Venue Financial Projections: 3-Year P&L, Cash Flow & Financing» · `wedding-venue-startup-checklist.xlsx` «Wedding Venue Startup Checklist (84 Tasks)» · `wedding-venue-pricing-calculator.xlsx` «Wedding Venue Pricing & Quote Calculator (Season, Day, Retainer & Cancellation Schedule)» · `wedding-venue-rental-agreement-templates.docx` «Venue Rental Agreement Templates: Couples, Corporate Clients & Exclusive Caterer» · bonus **común** `equivalents-guide` → `/dl/en-shared/hospitality-equivalents-us-uk-canada-australia.docx` (la guía ES↔LatAm no cruza, PIZ D135). Claves del dashboard: `plan-negocio`, `plan-financiero`, `checklist-apertura`, `calculadora-pricing`, `modelos-contrato`, `equivalents-guide` |

## 2. Concepto y caso (D159-D160)

| D | Tema | Decisión |
|---|---|---|
| D159 | Concepto | Research §1: **barn/estate wedding & event venue ARRENDADO** (la finca no se compra, D2 ES) a 30-60 min de una ciudad, salón de **200 invitados** sentados, ceremonia exterior con pérgola, bridal suite, aseos ADA, cocina de apoyo para el caterer; el venue factura **venue rental fee + servicios** y cobra una **caterer commission** al **exclusive caterer**, que factura comida y barra a la pareja y sirve el alcohol con su licencia (el venue **no vende alcohol**: B62 = 0). Mes 1 = marzo. Fuera (FAQ y Word §2/§10 como alternativas razonadas, sin Excel): comprar el inmueble, in-house catering (→ Catering Kit), banquet hall urbano, planner |
| D160 | Caso US | `VALORES_EN` = research §8 sobre las celdas de inv. §2.4: **B4 90 · B5 $68 · B6 100** · B7/B8 8/5 % · **B11 0.88** · B13 12 % · B14 0 · B15 1.5 % · **B16 10 % · B17 15 %** · B18 2 % · B20 10 % · B21 12 · B22 15,080 · **B24 $5,000** · B25 2 · B26 $2,000 · B27 $12,000 · B28 1 % · **B30 $200,000 · B31 CALIBRAR** (semilla ≈ $460,000; SBA 7(a) 10 % a 10 años, B34 0) · B35 3 · B37/B38 25 % · **B39/B40 8 % · B41 0** · B42 0 · B44/B45 15/7 · B48 0 · B51 200 · B52/B53 0.45/12 · **B54 4** · **B55 10 %** · B58/B59 10/14 · B60/B61 sin efecto (12 pagas, PIZ D144) · B62 0 · B63 8 % «no effect» · B65-B67 1.15/1.25/15 % · B68 vacío; escenarios 85·$60·85 / 95·$72·115. **Gates del caso (D15 EN)**: holgura de caja año 1 ≥ 15 % · DSCR mín ≥ 1.30 · saldo mínimo de Tesorería > 0 · cobertura ≥ 98 % · neto año 3 ≤ 16 % · exceso de fondos 0-5 % · D164 verde. Palancas en su orden (research §8): holgura → B5 +$2 o B24 $4,500 · neto A3 > 16 % → B7/B8 6/4 % · DSCR → B30 +$25,000 · cobertura → `Personal!B22/B23`. Máx. 3 vueltas, en `CALIBRACION_D15` y `F2-NOTAS`. El Word dice la verdad: el año 1 ya cuenta solo 35 bodas; **ninguna fecha firme sin CUP y certificate of occupancy** (regla M3 del ES) |

## 3. Libro financiero (D161-D167) — conjunto nuevo `wed` (código de la PIZZA, estructura de la PANADERÍA)

| D | Tema | Decisión |
|---|---|---|
| D161 | Código y diccionario | Código común **solo** `elif CONJUNTO == 'wed'` en `../business-plans-en/mapas.py` (copia de `:1240-1247`). Clones de inv. §7 en esta carpeta. Plan `_HOJAS_PLAN` = el de la pizza (mismas 9 pestañas) con **constantes de fila de la panadería** (inv. §0.1: Bakery EN ya pasó esa estructura por el común); checklist `hojas`, `COL_OK 1`; **docx = config de PAEL/PIZ** (131). **Diccionario por TEXTO, no por celda** (decisión SPEC frente al «por celda» del Bar en la pizza: ningún EN es gemelo de celda de la finca, inv. §0.2): pizza EN (GM, GR, GPIZ-plan, GPIZ-check + `*.revision.json`) → Bakery/BP (GPAN, GREST, GN, GM, GCAF, GFT) → BBQ/PAEL; **normalización previa = VOCABULARIO de la finca invertido** (invitado→cubierto, eventos→días, finca→local, espacio y servicios→comida, canon→bebida…); todo lo normalizado y todo lo reutilizado de otra celda va a **GR con revisión en la tanda 1**. Grupos `GM · GR · GWED-plan · GWED-check · GX`. `verificar`: sha256 de los 5 ES LIVE + los de la pizza EN. Regresión: ftcaf, restpan, bar, cat, mbar, bbq, pael, piz. **Motor SIN permutar** (inv. §0.4): no se copian los 7 parches de mbar/bbq/pael |
| D162 | Inversión 7-25 (solo rótulo e importe; la clase la fija la fila) | Las 19 partidas de research §8 = **$503,500** (obra $370,000 en 7, 9, 10, 12, 13, 15, 16, 20, 21, 22 · equipo $97,000 en 11, 14, 17, 18, 19 · no amortizable $36,500 en 8, 23, 24, 25); imprevistos **por fórmula** (`B55` 10 % de la obra = $37,000); `A26` «Lease security deposit» · `A27` «Rent during permitting and build-out» · `A28` «Build-out contingency». A1-A3 «US kit example (2026) — barn conversion on a leased property; replace with your own quotes». Notas de las filas 9-12, 20: «sprinklers need city water; a tank and fire pump, a new septic system or a strict county can double this line» (research §4). Col. E: la reescribe el motor (M8 ES) → en EN «Taxed?» sin efecto (B41 = 0) |
| D163 | P&L, fijos, personal | A2 «Base case — barn wedding & event venue, 200 guests, exclusive caterer» · A10 «Venue rental & event services» · A11 «Caterer commission (exclusive caterer)» · A13 «Direct event costs» · A14 «Cost of the commission (none)» · A15 «Event consumables» · A16 «Commissions to planners and venue marketplaces» · fijos 26-35 (**$62,000**, research §8: marketing 18,000 · bridal shows & open houses 5,000 · grounds contractors 10,000 · repairs & furniture 7,000 · accounting, payroll & legal 5,000 · software, CRM, web & phone 3,600 · safety training & compliance 600 · property taxes passed through & local fees 6,000 · sprinkler, alarm, extinguisher & generator inspections 2,800 · cleaning supplies, pest control & septic pumping 4,000). **Staffing** 6 filas (personas·FTE·bruto mes de la fila; ≥ suelo, 12 pagas): Owner — GM, sales & tours 1·1.0·$4,500 · Venue coordinator (seasonal, Mar-Nov) 1·0.75·$3,380 · Facilities & grounds 1·0.8·$3,050 · Event attendants (setup, parking & restrooms; seasonal part-time W-2) 2·0.35·$2,062 · Weekend sales & tours 1·0.2·$763 · Housekeeping & turnover 1·0.25·$780; B13/B14 $8,000; cobertura = ES (se recalcula). Nota: el dueño cobra por debajo de BLS planners ($29.41) |
| D164 | Sales tax (inv. §2.3) | `G10` (venue rental & services) **0.08** por `VALORES_EN` con nota «taxable in some states (e.g. Missouri; New York when charged with catering), exempt in others: ask your state's department of revenue» · `G11` (caterer commission) **0** con nota «treated as a fee your caterer pays you, not a retail sale (New York example): confirm with your CPA» · **`G13` → 0** «no input credit» · **`G14` → E2** (`$B$41`) · `B39`/`B40` 8 %, `B41` 0, `B62` 0 «the venue sells no alcohol», `B63` «no effect». Tesorería 16-20 = Bar EN; `A34` = texto de la pizza EN; `O16` (trimestres del 303 del VOCABULARIO finca) → «plan quarters» de la pizza EN. Sin E3 ni E5 (no hay literal en la columna H) |
| D165 | Umbrales y D19 | `E51` 85 % · `E53` 15 % · `E54` 35 % · `E55` 12 % · `E56` 5 % (research §5.2). **D19** (`Instructions` 34-48; sin D18), «US WEDDING VENUE BENCHMARKS (sourced) AND KIT ESTIMATES», 14 filas: Month 1 = March (Kit) · event mix (research §8, Kit) · Saturday ceiling ≈ 30-35 prime Saturdays a year (Kit) · US weddings: 117 guests, $34,200 (The Knot 2026) · venue rental fee $3,500-$9,950 (5 rate cards, research §5.1) · booking lead time (Kit) · direct cost per event (Kit) · caterer commission ≈ 10 % (public examples) · venue staff per event (Kit) · sales tax on venue charges varies (MO, NY) · sprinklers: A-2, ≥ 100 occupants or > 5,000 sq ft as adopted (IBC 903.2.1.2) · noise and curfew: county CUP conditions (Lake County FL example) · well water: public water system ≥ 25 people ≥ 60 days (40 CFR 141.2, **solo si la revisión D174 lo abre**; si no, «ask your state drinking water program») · minimum wage federal $7.25 + state (DOL). Solo lo «leída/medido» lleva fuente; lo «(resumen)» = «industry example»; lo demás, Kit estimate |
| D166 | Fórmulas y excepciones | Con texto: las 10 derivables (inv. §2.2) + manuales **C9, D28, D38, F13, F14, O11** (`D38` lista las 4 partidas no amortizables por su rótulo EN). Numéricas distintas (B28, B36, B37) = ES sin tocar. **E1** aviso D21 (WEDP `A54`, WEDC `A12`) · **E2** solo `G14` · **E4** `Staffing!C11` → `SUMPRODUCT(B5:B10,C5:C10)` (3.70 FTE con el caso). Sin E3/E5. G1 = **734** fórmulas y **84** tareas |
| D167 | Mes 1, estacionalidad y pagas | **Mes 1 = marzo** (como el ES); **pesos US** en `12-Month Cash Flow!B5:M5` por `VALORES_EN` = research §8 (,050 ,075 ,105 ,120 ,080 ,085 ,130 ,145 ,070 ,060 ,035 ,045; `assert` suma 1.000): decisión SPEC frente a la pizza (que dejó los del ES) porque el pico US es octubre-septiembre-junio y el español junio-septiembre. `O5` «Month 1 = MARCH: permits and build-out close over the winter before; peaks in October (Month 8), September (Month 7) and June (Month 4); the low is January (Month 11). If you open in another month, rotate the row». `O13`/`B60`/`B61`: sin pagas extra (12 pagas) |

## 4. Calculadora (D168) — `calculadora_wed.py` = `../plan-finca-eventos/calculadora_fin_es.py` traducida y adaptada (VPS)

Mismas hojas (`Calculator` · `Examples` · `Instructions`), mismas filas, helpers, `inject_cache` y autotest (pycel + caché = `calcular()`,
3 ejemplos). Cambios: (1) canal **Couple / Corporate** (el corporativo recibe «plus sales tax»; la pareja, con impuestos); (2) tipologías
**Wedding $8,000 · Corporate $3,500 · Private celebration $4,000 · Micro wedding / elopement $2,000** (tarifa de sábado de temporada
media) con F&B del caterer por invitado **$110 · $50 · $55 · $80** y coste directo **$1,000 · $500 · $500 · $300**; (3) temporadas **Peak
+15 % / Shoulder 0 / Off-peak −20 %** con mínimo de invitados para el presupuesto **100 / 75 / 50**, meses US (may, jun, sep, oct = peak;
abr, jul, ago, nov = shoulder; dic-mar = off-peak) y días **Saturday 0 · Friday or Sunday −15 % · Weekday −30 %** (research §5.1); (4) extras
**ceremony on site $750 · additional hour $500 · premium décor & lighting $800 · rehearsal the day before $400** (sustituye al alojamiento);
(5) personal $18/h + payroll taxes 10 %; redondeo $50; **caterer commission 10 %** (supuesto, «negotiate it»); **sales tax on venue charges
8 %** y **sales tax on the caterer's F&B 8 %** (solo para el presupuesto orientativo de la pareja) con nota de research §6.6; (6) cobros
Couple 25 % / 35 % a 180 días / 40 % a 30 días · Corporate 30/30 a 60/40 a 15 (= ES); **tramos de cancelación = ES** (10/25/50/75/100 % ·
5/15/35/60/100 % a 12/6/3/1/0 meses) con nota «a reasonable estimate of the loss, not a penalty; the contract credits back what you
recover by rebooking the date»; (7) formatos `$#,##0.00`, fechas `mm/dd/yyyy`, Letter, docProps D20. Ejemplos: «Saturday wedding in
peak season» (9-oct-2027, 130 invitados) · «Friday wedding in shoulder season» (16-jul-2027, 100) · «Weekday corporate event»
(21-abr-2027, 50 < mínimo). Gates: autotest VERDE · 0 español / no latinos / cifras ES / `RX_WED_NO`.

## 5. Checklist (D169) — las 84 tareas 12/16/15/13/14/14 del ES, mismas filas (fuente: `../plan-finca-eventos/datos_checklist.py`)

Pestañas (≤ 31): «Phase 1 - Business Setup» · «Phase 2 - Zoning & Permits» · «Phase 3 - Build-Out & Equipment» · «Phase 4 - Staff &
Caterer» · «Phase 5 - Brand & Bookings» · «Phase 6 - Season & Events» · «Instructions». A1 «WEDDING VENUE STARTUP CHECKLIST»;
`Instructions!A3` = nombre comercial. Equivalencias (se suman a BP §4.2, BP2 §3, Bar D60, PIZ D146):

| ES | US |
|---|---|
| SL/autónomo, 036/IAE, SS del administrador, Veri\*factu, 303 al 21 %, 115 de la renta, OEPM, RGPD | LLC vs S corp with your CPA · EIN + state payroll/unemployment accounts · business license + sales tax permit (ask if your venue fee is taxable) · bookkeeping + venue software that tracks retainers · lender package: SBA 7(a) quotes · USPTO trademark search · website privacy policy & terms |
| Consulta urbanística, finca con edificaciones, agua/luz/saneamiento, arrendamiento ≥ 15 años, condición suspensiva, reversión de mejoras y opción de compra | **zoning check before signing** · **lease contingent on CUP approval** · term + options ≥ loan term, improvements & landlord consent, purchase option · septic capacity and well (public water system?) checked by an engineer |
| Madrid/Andalucía/Cataluña/C. Valenciana (calificación) · licencia de actividad · aforo y evacuación · ruido y limitador · horario · RC de tu comunidad · pozo | **conditional/special use permit** (hearing, conditions: event cap, hours, traffic) · **change of occupancy to assembly (A-2) + certificate of occupancy** · **ask the building official and fire marshal in writing: occupant load, sprinklers, egress, restrooms, tents** · noise ordinance & music curfew · GL + host liquor liability + property quotes · **no firm dates before CUP and CO: contingent holds with full refund** |
| Obra: proyecto, aseos, eléctrica, grupo, clima, office, carpa, mobiliario, sonido, parking, PCI | architect/code consultant drawings + building permit · **fire sprinkler & alarm** · **ADA restrooms, accessible routes & parking** · electrical service & emergency lighting · generator · HVAC · caterer's prep kitchen (health plan review if your county requires it) · pergola/tent platform · 200 chairs & tables · sound & decibel meter · gravel lot & lighting · final inspections |
| Fijos discontinuos, SS por llamamiento, registro de jornada, PRL · homologar caterings, concesión, canon, **comida testigo**, alérgenos, registro sanitario, proveedores | seasonal W-2 offer letters, I-9, W-4, state minimum wage, workers' comp · time records & overtime (FLSA) · basic safety (OSHA, first aid) · shortlist 1-2 caterers + tasting · **exclusive caterer agreement (commission, audit, minimum)** · caterer's license, health permit, **liquor license/permit** and COI naming the venue · 9 major allergens = caterer · preferred vendor list with COIs · *(comida testigo: se quita; la tarea pasa a «caterer's food safety plan and incident contact»)* |
| Marca, web, fotos, Google, portales, redes, ferias, puertas abiertas, planners, empresas, tarifas, dossier, contrato, CRM | brand · website with availability & tour booking · styled shoot · Google Business Profile & first reviews · **The Knot / WeddingWire storefronts: track cost per lead** · social · bridal shows · open house with the caterer · planners & corporate · pricing by season & day (calculator) · pricing guide · **venue rental agreement** · venue management software |
| Visita y presupuesto, contrato y señal con factura, **sin desistimiento (103.l)**, **fuero del consumidor**, prueba de menú, recuento, plan B, aforo, limitador, **comida testigo**, recogida, canon, reseña, cierre | tour + written quote · signed agreement, retainer and receipt · **3-day cancellation notice if signed at a bridal show (FTC Cooling-Off Rule)** · governing law clause reviewed by your attorney · tasting · final headcount & allergies · rain plan · occupancy check · curfew & decibel limit · walkthrough & damage check (security deposit) · monthly commission statement from the caterer · review, photos & thank-you · quarterly close: occupancy, commission, cash |

## 6. Docx (D170)

Las **131 ranuras del FT ES** (inv. §4); 61 traducidas-adaptadas desde el **Word ES de la finca** (`wed_a` §1-5 ‖ `wed_b` §6-10), un run
por párrafo, **todas las cifras desde `cifras_caso.json`** (tokens D43 + los de eventos del ES que sobreviven: `INVITADOS_EVENTO`,
`PRECIO_INVITADO`, `EVENTOS_ANO`, `BE_EVENTOS(_CAJA)`, `EVENTOS_EQUIVALENTES_A2/A3`, `COMISION_PCT`, `RENTA_MES`, `JORNADAS_EQUIVALENTES`,
`SALDO_MINIMO`, `MES_SALDO_MINIMO_NOMBRE`… + `inv_sprinklers`, `inv_aseos`, `inv_parking`). **No cruza** (research §6): urbanismo
autonómico, Orden INT/1068/2026, RD 1367/2007, RD 3/2023, RD 1086/2020, TRLGDCU, LAU, LIVA, ET 16, SGAE, Ley 15/2015. §2 y §10: buy vs
lease, in-house catering y preferred-vendor model como alternativas razonadas. §9: zoning/CUP, change of occupancy A-2 y sprinklers,
ADA, septic/well, alcohol (exclusive caterer's license; BYOB solo con bartender licenciado + host liquor liability; Wisconsin como
ejemplo de regla estatal), sales tax del venue, música, seguros y COIs, contratos (liquidated damages, Cooling-Off Rule), seasonal
W-2; **nota UK** en 108. FIJOS 35 «Appendices: Excel Financial Plan + Startup Checklist + Pricing Calculator + Rental Agreement
Templates + Equivalents Guide»; cierre 127-129 = **Catering Business Plan Kit** · **Mobile Bar Business Plan Kit** · **Catering
Checklist Templates** (`catering-checklist-templates`).

## 7. Contrato (D171) — `contrato_wed.py` + `textos_en/contrato_en.json` (1 sonnet; molde físico = el docx ES, Letter)

Cabecera fija: «**Template, not legal advice.** Consumer, deposit, alcohol and tax rules vary by state. Have a licensed attorney in your
state review and adapt it before you use it.» Corchetes `[ ]` para todo lo editable; cero cifras del caso. Decisiones:

| ES | EN |
|---|---|
| Modelo 1: Reunidos · 1.ª Objeto · 3.ª Invitados, mínimo y recuento · 9.ª Cambio de fecha · 11.ª Horarios · 13.ª Aforo · 16.ª Plan B lluvia · 20.ª Datos e imagen | **Cruzan** (Parties · Rental & included services · Guest count, guarantee & final headcount · Date change · Setup, event & load-out hours (county curfew) · Maximum occupancy (posted by the fire marshal) · Rain plan (rain is not force majeure) · Photos (separate written release) & privacy) |
| 2.ª Licencias · **2.ª bis Reserva condicionada a la licencia** | **Cambian**: «Permits» (venue warrants zoning approval and certificate of occupancy) · **2A «Contingent booking before permits»**: solo hold con devolución íntegra en [14] días si el CUP/CO no llega a [fecha ≥ 6 meses antes] |
| 4.ª Precio e IVA 21 % · 5.ª Calendario y facturas · 6.ª Señal a cuenta | «Fees and sales tax» («plus applicable sales tax») · «Payment schedule and receipts» (25/35/40 %) · **«Retainer»**: se aplica al precio; lo que se retiene al cancelar lo fija **solo** la tabla de la 7.ª (nunca la palabra «non-refundable» sola) |
| 7.ª Cancelación por tramos · 8.ª Cancelación por la finca y reciprocidad | Tramos ES + **rebooking credit** («if we rebook the date at an equal or higher fee, we refund what we retained minus our documented costs») + «the parties agree this is a reasonable estimate of the venue's loss, not a penalty» · por el venue: devolución íntegra en [14] días + [importe pactado] y ayuda para recolocar |
| 10.ª Sin desistimiento (TRLGDCU 103.l) · 21.ª Fuero del consumidor (art. 90.2) · 17.ª Fuerza mayor (art. 1105 CC) | **Se quitan las citas españolas**: 10.ª → **«Three-day right to cancel if signed away from the venue»** (aviso de la FTC Cooling-Off Rule para firmas en bridal shows ≥ $130, 16 CFR 429, research §6.7) · 21.ª → «Governing law and disputes: [State] law; courts of [county]» (corchetes + revisión de abogado) · 17.ª → force majeure genérica con reembolso o nueva fecha |
| 12.ª Ruido y música (SGAE) · 14.ª Proveedores externos · 15.ª Daños y fianza · 18.ª Seguros · 19.ª Alérgenos | Noise, decibel limit, music licensing (ASCAP/BMI/SESAC) · Outside vendors: **COI naming the venue as additional insured**, licensed bartenders only, no open flame/sparklers sin permiso del fire marshal · **Security deposit** reembolsable con deducciones detalladas en [14] días · Insurance: venue GL; client **event liability + host liquor liability** si hay alcohol · **Food, alcohol & allergens**: del caterer; alcohol solo por el caterer/bartender licenciado, ID, nada a menores ni a personas ebrias |
| (nuevo) | **Mutual responsibility** (cada parte responde de su negligencia; sin indemnidad unilateral) · **Entire agreement & e-signatures** |
| Anexo empresas | **Corporate & organization addendum**: W-9, PO/billing contact, **sales tax exemption certificate** si es exenta, net terms, tramos 5/15/35/60/100 %, foro pactado |
| Modelo 2 catering exclusivo: objeto y exclusividad · facturación directa · **canon 12 % auditable** · office · **comida testigo** · **14 alérgenos** · personal · seguros · horarios, limpieza y residuos · precios mínimos y prueba · duración · entrega · jurisdicción | **«Exclusive Caterer Agreement»**: exclusividad (excepciones: tarta de una bakery con licencia) · factura directa a la pareja con sales tax, **service charge vs. gratuity** a cargo del caterer · **commission [10] % of food & beverage sales, net of sales tax, service charge and gratuities**, statement mensual, audit right, mínimo anual opcional · uso de la prep kitchen (el caterer mantiene su **health permit** y su plan de seguridad alimentaria) · **comida testigo: se quita** · alérgenos: «major food allergens» según la normativa estatal/local · personal W-2 del caterer (FLSA, I-9) · **liquor license/permit del caterer + liquor liability [$1M] + workers' comp + auto**, venue additional insured · grease/FOG y residuos · menús mínimos y tasting · plazo y renovación · entrega · governing law (B2B) |

## 8. Gates (D172), cifras y vocabulario (D173), revisión (D174)

- **D172**: G1-G9 (E1, E2, E4 por nombre) · `RX_WED_NO` y cifras prohibidas 0 en los 5 · `bp9.py calculadora --autotest` · `bp9.py
  contrato` (Letter, autor AI Chef Pro, 0 tokens, aviso de cabecera presente) · barrido · no latinos · `censo-entregables --fail
  --letter --only wedding-venue-business-plan` (alta en `PRODUCTOS_LETTER` y `EXCLUIDOS` antes de G9) · `verificar` · regresión de
  los 8 conjuntos · 2.ª pasada con sha256 canónico igual.
- **D173**: `cifras_prohibidas()` (de la pizza): `CIFRAS_ES` = importes ≥ 10.000 € de `../plan-finca-eventos/cifras_caso_es.json` (los
  pequeños, solo con «€»), fuera los que coinciden con el caso US · `FRASES_ES` («82 guests», «\$?37 per guest», «120 events», «12 ?%»
  junto a commission/canon, «14 pay», «33 ?%», «8[.,]8 ?%», «(?i)\b20 ?% of (sales|bookings)\b») · caso de la **pizza EN**
  (`_cifras_caso('../business-plans-en-8/cifras_caso.json', 'piz')` + «62 covers», «\$36», «300 days»). `RX_WED_NO` = restos de la
  pizza EN y de la Bakery (`pizza|pizzaiolo|\bdough|wood-fired|covers per day|cover count|average check|croissant|sourdough|bakery business`;
  **no** «covers», «oven», «slice», «pastry» ni «bakery» sueltos: falsos positivos en prosa de venue y en la excepción de la tarta
  del contrato) + ES/eventos (`finca|canon|\bIVA\b|convenio|
  \bSMI\b|aut[oó]nomo|comunidad aut|ayuntamiento|SGAE|testigo|TRLGDCU|\bLAU\b|arras|se[ñn]al|fijo discontinuo|calificaci[oó]n|parrill|
  brasa|pitmaster|smoker|paella|food truck`). «non-refundable» no va al regex: la revisión D174 mira cada aparición.
- **D174 Una revisión opus** (tope 2 rondas, arreglos por texto): recalcular ventas, CAPEX con imprevistos de fórmula, equilibrio en
  eventos, holgura y DSCR · jerga (guests, venue rental fee, caterer commission, retainer) · claims: zoning/CUP, sprinklers (IBC
  903.2.1.2 como «as adopted»), ADA, alcohol (Wisconsin), sales tax (MO, NY), deposits (§1671, Cooling-Off) · **abrir** 16 CFR 429,
  40 CFR 141.2 y, si es posible, NY A20-51S y la guía de Missouri; lo que no se abra, sin cita · unidades y fechas de la calculadora ·
  **contrato**: que ninguna cláusula diga «non-refundable» sin la tabla, que la cabecera legal esté y que no quede derecho español ·
  **cero rastro de finca, España ni pizza** · que el Word no prometa lo que el Excel no hace.

## 9. Capa de producto (D175-D177, F3) — duplicar la F3 de la Pizza (`git show 64ace831 -- <fichero>`)

- **D175 Landing** `astro-site/src/data/productos-en/planes/wedding-venue-business-plan.ts` = `cp` de `pizza-shop-business-plan.ts`, SEO
  D156b, FAQ = las 8 de research §3 + canibalización (Catering Business Plan Kit = catering sin espacio; Mobile Bar) + UK/CA/AU; cifras
  MEDIDAS y estables (ventas, CAPEX, eventos de equilibrio, neto %; nada de DSCR, payback ni saldos, D12 ES); **sin testimonios**;
  `omitGlobalApp`; imágenes `plan-finca-*.jpg` del ES sin texto en español + `og-wedding-venue-business-plan.jpg` (recorte del hero);
  tarjetas de la galería = lo que hacen los 5 ficheros (lección M4-M6 de la pizza: nada que el fichero no tenga).
- **D176 Registros**: páginas `en/digital-products/wedding-venue-business-plan{.astro,/access.astro,/library.astro}`, island
  `WeddingVenueBusinessPlanLibraryIsland.tsx`, `src/pages/WeddingVenueBusinessPlanDashboard.tsx` (6 claves de D158; tarjetas
  `calculadora-pricing` y `modelos-contrato` copiadas del dashboard ES de la finca) · `tienda.ts` (FAMILIAS `plan-negocio-finca-eventos-bodas`,
  es + en vivos) y **`plan-negocio-finca-eventos-bodas.astro`** con `alternatesFamilia` (diff de la pizza) · `zona-app.ts` ·
  `get-download-urls.ts` (5 + guía) · `verify-purchase.ts` · `resend-access.ts` · `admin-generate-access.ts` + `AdminGenerateAccess.tsx` ·
  `product-prices.ts` (`usd: 49`, `sync-product-prices.py`) · `payment-links.ts` (tras el link) · `products-catalog.ts` (entrada ES:
  `name.en`, `urlByLang`, `priceByLang`) · config · changelog '1.0' · `linkify-use-case.{ts,tsx}` · **hub EN**: la tarjeta «Business Plan:
  Event & Wedding Venue» (→ ES, `DigitalProductsHubPage.astro` l. 626-643) **pasa a ser la del EN** (lección B1 de la pizza: no dejar
  las dos) · `llms.txt`/`llms-full.txt` (+1) · `sitemap-lastmod.json` · `footerLinks` de los 4 planes EN de eventos (Catering, Mobile Bar,
  BBQ, Paella) + Catering Checklist Templates · FAQ «Is there a plan for a wedding or event venue?» en Catering y Mobile Bar EN ·
  `tienda-gate.py` · correo `broadcast-wedding-venue-business-plan-lanzamiento-en`.
- **D177** Gates F3 = PIZ D153 con `--only wedding-venue-business-plan` · `fase6-gate.py <URL EN>`. **Payment Link: John** (USD 49, prosa
  sin viñetas, éxito → `/en/digital-products/wedding-venue-business-plan/access?session_id={CHECKOUT_SESSION_ID}`). **Correo EN
  23-feb-2027 14:00Z** (CALENDARIO l. 774, siguiente hueco tras la pizza): borrador + prueba + routine ≥ 24-ene. El ES ya está LIVE: no
  hay orden de merge. No se tocan `robots.txt` ni el blog (carril Cursor).

## 10. Plan, presupuesto y riesgos (D178-D180)

| Paso (D178) | Quién | Tokens · reloj |
|---|---|---|
| 1a · rama `wed`, clones, caso, tokens, `RX_WED_NO`, dry-run + D15 (VPS, `/root/wt-wedding`); `BRIEF-TRADUCTORES.md` ‖ 1b `calculadora_wed.py` + autotest ‖ 1c `contrato_en.json` + `contrato_wed.py` | 1 opus ‖ 1 sonnet ‖ 1 sonnet | 0,40 + 0,12 + 0,12 M · 50 min |
| 2 · Tanda 1: GWED-plan (≈ 212 cad., ≈ 4,4 K pal. + revisión GR 61) ‖ GWED-check (224, ≈ 2,65 K) | 2 sonnet | 0,22 M · 25 min |
| 3 · `aplicar_en` + D15 → `cifras_caso.json`; Tanda 2 `wed_a` ‖ `wed_b` (61 ranuras, ≈ 6,5 K pal.); `ensamblar_docx` | VPS + 2 sonnet | 0,22 M · 25 min |
| 4 · Gates D172 + revisión D174 (5 ficheros, foco en el contrato) + 1 ronda; `F2-NOTAS`; commit + push | VPS + 1 opus | 0,24 M · 35 min |
| 5-6 · F3: sonnet A (ficha, páginas, isla, dashboard) ‖ sonnet B (registros, hub, hreflang ES, enlaces, correo); OG, PR, preview, gates, link, LIVE | 2 sonnet + orquestador | 0,58 M · 70 min |
| **Total F2 (≈ 1,30 M) + F3 (≈ 0,58 M)** | | **≈ 1,9 M · ≈ 3,5 h** + el link |

Del ES no hace falta esperar nada: está LIVE y revisado (inv. §0). Si cambia antes de la tanda 1, se re-extrae (inv. §9).
**D179 Riesgos**: (1) **CAPEX y arrendamiento** ($570K de mejoras en suelo ajeno): el Word lo dice con los rangos de research §4 y el
checklist manda a preguntar por escrito; nunca «$X basta» · (2) **holgura** ≈ 17 % con el caso; sprinklers/septic más caros o una renta
mayor la bajan → D160 · (3) **claims legales** (CUP, A-2, ADA, alcohol, sales tax, depósitos): todo con «as adopted / check your county
and state» y el contrato con cabecera legal → D174 · (4) **fuga de la pizza EN** por el GM por texto («covers», «pizza», «oven») y de
las propuestas normalizadas («FOOD/BEVERAGE share») → GR con revisión + `RX_WED_NO` · (5) **contrato sin precedente EN**: 1 sonnet +
foco de la revisión opus; si la F2 pasa de 2,5 h, el Modelo 2 (exclusive caterer) se queda en cláusulas dentro del Word (como D10 ES) ·
(6) canibalización con Catering y Mobile Bar (la landing diferencia: espacio propio) · (7) **F1 paralela (D186+)**: choca en la misma
línea del `elif` de `mapas.py` (conflicto trivial: se apilan las dos ramas) y puede pedir el mismo hueco de correo del 23-feb (lo
asigna el orquestador). **D180 NO se hace**: testimonios, anclas, ratings, anexo por estado, permutar el motor, comprar el inmueble o
in-house catering en el Excel, cambiar filas/hojas/DV, research nueva, posts del blog, compra de prueba, `robots.txt`.

## 11. Decisiones de orquestador, 27-oct (F2 paso 1a; mandan sobre §0-§10 en lo que choquen)

| # | Tema | Decisión de orquestador, 27-oct |
|---|---|---|
| O1 | Obra de ≈ $540-570K sobre una propiedad ARRENDADA (D159/D162) | Se mantiene (el ES también arrienda), pero el Word y el checklist exigen: arrendamiento largo cuya duración **contando las prórrogas** sea al menos la del préstamo («SBA lenders typically require…; confirm with your lender», sin citar una regla que no se haya abierto), **opción de compra o derecho de tanteo** (right of first refusal), **consentimiento del propietario a la obra y a usar el arrendamiento como garantía**, negociar una **TI allowance** y lease contingent on CUP approval. Comprar (SBA 504) = variante en el Word, sin Excel. En el checklist, sin mover filas: fase 1 fila 14 y fase 2 filas 8-10 (pistas de `datos_wed._CHK`) |
| O2 | FTC Cooling-Off Rule (16 CFR Part 429) (D169 fase 6, D171 cláusula 10.ª) | La regla excluye las transacciones relativas al alquiler de inmuebles: **no se afirma que aplique** a un contrato de venue. Forma única: «If you sign couples at bridal shows or off-site, ask your attorney whether the FTC Cooling-Off Rule or your state's home-solicitation law applies; many venues give a short cancellation window for show-floor signings anyway.» En el contrato, como nota de redacción y cláusula OPCIONAL entre corchetes. La revisión D174 lo comprueba abriendo el texto de 16 CFR 429.0 |
| O3 | Correo EN de lanzamiento | **23-feb-2027 14:00Z** (Ice Cream va al 28-feb y el kit Hotel al 5-mar): D177 ya lo dice |
| O4 | Lo «(resumen)» o sin verificar de research (The Knot, NY A20-51S, Missouri, CA Civ. Code §1671, 40 CFR 141.2, Wisconsin, rentas, seguros, sprinklers, fosa séptica) | Fuera de las cifras rotundas: «typical range, get local quotes», «Kit estimate» o «ask your [agency / county / attorney / CPA]» hasta que la revisión D174 lo abra. Afecta a D164 (notas de sales tax sin MO/NY), D165 (D19 sin The Knot, sin 40 CFR 141.2 ni umbral de sprinklers con cifra), D170 (§9) y D171 (sin §1671) |

Decisiones del paso 1a (implementador, 27-oct; detalle en `F2-NOTAS.md` §3 y §5): umbral `E51` 85 % → **80 %** (calibración
D15: el caso de research §8 da 83.4 %) · tabla D19 con las filas del ES (`A41` es FIJO; «Venue rental fee» en la 46) ·
checklist reutilizable no GM → GWED-check · **contrato en la tanda 1** (parte 1 → traductor B, parte 2 → traductor A) y
calculadora como código (paso 1b), en vez de 1c ‖ 1b separados de D178.
