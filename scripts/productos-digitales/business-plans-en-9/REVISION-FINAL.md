# Wedding Venue Business Plan Kit (EN, $49): revisión adversarial final (D174)

> Sesión Claude Code, 27-oct-2026. Una revisión y una ronda de arreglos, sobre los volcados `revision/*.txt` de los 5
> entregables, la SPEC-delta (§11 decisiones de orquestador), `F1-research-us-delta.md` y `F2-NOTAS.md`. Las fórmulas se
> han leído en el XML de los xlsx, no en el volcado. Fuentes abiertas: **16 CFR 429.0** y **40 CFR 141.2** en
> law.cornell.edu (eCFR bloquea la descarga automática). La regla SBA del arrendamiento se ha comprobado en dos fuentes
> secundarias (starfieldsmith.com sobre SOP 50 10 7.1, colemanreport.com sobre la Procedural Notice 5000-852522): en 7(a)
> el plazo del arrendamiento, contando las prórrogas que solo puede ejercer el prestatario, *should* igualar o superar el
> del préstamo (en 504, *must*). No se ha abierto la SOP misma, así que el texto se queda en «SBA lenders typically
> require…; confirm with your lender», sin citarla. NY A20-51S, Missouri, CA Civ. Code §1671 y Wisconsin no se han
> abierto y **no aparecen** en ningún entregable (grep 0).

**Recuento: 2 B · 5 M · 21 m** (B y M arreglados; 14 m arreglados y 7 anotados).

## 0. Lo recalculado que está bien (no tocar)

| Comprobación | Resultado |
|---|---|
| Ventas | 90 × $68 × 100 = **$612,000**; A2 $660,960 (+8 %) y A3 $694,008 (+5 %) = 108 y 113 eventos equivalentes ✓ |
| Mezcla y comisión | 35 × 130 + 25 × 70 + 30 × 80 + 10 × 30 = 9,000 invitados → 90 ✓. Con los precios de `Instructions!D36`: $616,900 → $68.54 por invitado y comisión $74,400 = **12.06 %** de las ventas. La comisión del 10 % del F&B (F&B implícito ≈ $81.60 por invitado de media) cuadra con el 12 % del Word [39] ✓ |
| CAPEX | 19 partidas $503,500 (obra $370,000 · equipo $97,000 · no amortizable $36,500) + imprevistos por fórmula 10 % × $370,000 = **$37,000** + fianza $10,000 + renta previa $20,000 = **$570,500**; fondo $99,216 (3 meses de fijos con intereses) → **$669,716**; fuentes $670,000 (+0.04 %) ✓ |
| Préstamo y DSCR | 470,000 × 0.10 / (1 − 1.1^−10) = **$76,490**; principal del año 1 $29,490; DSCR año 1 = (72,800 − 18,200 + 40,990 + 47,000) / 76,490 = **1.86×**; 2.18× y 2.36× ✓ |
| P&L año 1 | Variables $101,347 (16.6 %) → margen bruto 83.4 %; EBITDA $160,791 (26.3 %); BAI $72,800; neto **$54,600 (8.9 %)**; 12.3 % y 14.2 % ✓ |
| Equilibrio y holgura | 437,852 / 56.74 / 100 = 77.2 invitados → $524,751 = **86** eventos; de caja 426,352 / 56.74 = 75.1 → $510,969 = **84** eventos; holgura 90 / 75.14 − 1 = **19.8 %** (27 % y 31 %) ✓ (ver m15) |
| Escenarios | 85 × 85 × $60 = $433,500 y 115 × 95 × $72 = $786,600 ✓ |
| Calculadora | 8,000 × 1.15 = $9,200 + 750 + 2 × 500 + 800 = **$11,750** + 8 % = **$12,690**; 25/35/40 % = $3,172.50 / $4,441.50 / $5,076; 10/09/2027 es sábado; −180 días = 04/12/2027 y −30 = 09/09/2027; comisión 130 × $110 × 10 % = $1,430; margen 82.3 % ✓. Tarifas, F&B y coste directo por tipo = los de `Instructions!D36`/`B40` del libro ✓ |
| Arrendamiento (decisión O1) | En los 3 sitios: Word [41] [47] [93] [97] [102] [114]; checklist `Phase 1!E14`, `Phase 2!B8:E10`; Excel `0. Assumptions!C24`, `Startup Costs!D24`. Compra = SBA 504 sin Excel ✓ |
| Cooling-Off (decisión O2) | 16 CFR 429.0(a)(6) excluye las transacciones «pertaining to the sale or rental of real property». Ningún texto afirma que aplique: Word [69] y [107], checklist `Phase 6!E7`, calculadora `Instructions!A17` y contrato (cláusula 10 opcional entre corchetes + nota de redacción) dicen solo «ask your attorney whether…». No se cita el umbral de $130 ✓ |
| Contrato | Cabecera legal literal; «non-refundable» 0 veces (solo la instrucción «Never write "non-refundable" without the schedule» de la calculadora); tabla 10/25/50/75/100 % con «reasonable estimate… not a penalty», rebooking credit y «to the extent permitted by applicable law»; devolución íntegra si cancela el venue; lluvia no es fuerza mayor; COI y additional insured; host liquor liability del cliente; indemnización recíproca; cero derecho español ✓ |
| Normativa | A-2 y sprinklers «as adopted» sin umbral; ADA Title III y 2010 ADA Standards; alcohol solo del caterer con licencia; FLSA 40 h; $7.25; NOL 80 %; FICA 7.65 %; 9 major food allergens; BLS sin cifra ✓ |
| Jerga y rastros | venue rental fee, exclusive caterer, caterer commission, retainer, day-of coordination, bridal suite, rain plan, guests (nunca covers); barrido 0 de `RX_WED_NO` / cifras ES / pizza; Month 1 = March coherente en O5, C60/C61, A34 y la estacionalidad (picos oct-sep-jun) ✓ |
| Landing | Aún no existe (F3). Debe usar las cifras de abajo y **no** los volúmenes de DataForSEO (M4); la cobertura de horas es ahora 116 % |

## 1. B: bloqueantes (arreglados)

| # | Fichero · lugar | Defecto | Arreglo (fuente) |
|---|---|---|---|
| B1 | Checklist `Phase 5 - Brand & Bookings!E13` | «The plan assumes **one in five** sales comes through them»: es el 20 % del caso ES. Contradice el Excel (`0. Assumptions!B16` 10 %) y el Word [61] [71] [112] (10 % al 15 %) | «The plan assumes one in ten sales comes through planners and venue marketplaces, at a 15% commission. Marketplaces such as Peerspace…» (`textos_en/GWED-check.json` c0817) |
| B2 | Excel `12-Month Cash Flow!O20` | «Months 4, 7 and 10: **December, March and June with Month 1 in September**»: la nota de la Pizza EN entró por el GM por texto. Contradice el Month 1 = March del libro | «June, September and December with Month 1 in March» (`textos_en/GM.json` c0529; además `POR_CELDA` O20 en `datos_wed.py`, que solo manda si se re-extrae: la cadena es GM «traducir» y `aplicar_en` aplica `POR_CELDA` solo a lo «regenerar») |

## 2. M: mayores (arreglados)

| # | Fichero · lugar | Defecto | Arreglo (fuente) |
|---|---|---|---|
| M1 | Word [58] y [65] | «from year 2, **when you are repaying principal**» / «once you are repaying principal»: venía del ES, que tiene 1 año de carencia. El EN no tiene (`B34` 0; `Break-Even!B12` $29,490 de principal en el año 1; `C34` «SBA 7(a) loans amortize from the start») | [58] «there is no cash in year 1 (the loan payment, principal included, starts in year 1); the margin… then grows to 27% and 31%» · [65] «grows to … with the loan payment already in from year 1» (`docx_en_wed_a.json`) |
| M2 | Excel `0. Assumptions!A39`, `A40`, `C40` | `A40` «Sales tax rate on **alcohol to go**» (rótulo de la pizza) y `C40` «In this plan it applies to everything the venue bills as rental and services». **Ninguna fórmula lee B39, B40, B62 ni B63** (0 referencias en el XML); los tipos que cobra el venue son los verdes de `3-Year P&L!G10/G11`. Quien teclee aquí el tipo de su estado no cambia nada | `A39` «Sales tax rate on food sales (not used: the venue sells no food)» · `A40` «General sales tax rate (reference only: the rates used are on the P&L)» (`POR_CELDA`) · `C40` «REFERENCE ONLY: no formula reads this cell… G10… G11…» (`GWED-plan` c0072) |
| M3 | Excel `0. Assumptions!A9` | «**Menu price** incl. sales tax (calculated)»: el venue no vende menú (jerga, D0) | «Revenue per guest incl. sales tax (calculated)» (`POR_CELDA`) |
| M4 | Word [39] y [54] | [39] «Interest is real: DataForSEO shows roughly 1,000 monthly US searches for "wedding venue business plan" and 720…»: mide a quien busca la plantilla (competidores), no la demanda del venue, y no tiene sitio en un plan para un lender. [54] «DataForSEO shows roughly 6,600… "wedding barn"»: cifra de una herramienta, sin fecha ni fuente pública (el aviso legal promete «public sources named in the text») | [39] frase quitada · [54] «Check the demand in your own area: a keyword tool such as Google Keyword Planner shows how many people around you search for terms like "wedding barn" or "wedding venues near me".» |
| M5 | Word [99] y [47] | El Word promete lo que el Excel no hace: [99] «check it in the Excel by **moving the sales mix**» (B11 solo reparte los mismos $612,000) y [47] «test that in the **pessimistic scenario**» (los escenarios mantienen la mezcla) | [99] «by setting the venue rental & services share to 100% and lowering the revenue per guest by the commission's share» · [47] «test that in the Excel (section 8 explains how)» |

## 3. m: menores

Arreglados:

| # | Lugar | Arreglo |
|---|---|---|
| m1 | `Staffing!B20/B21` frente a `J20/J21` | Las notas dan 9.7 h y ≈ 2.4 personas con la mezcla US; las celdas seguían con el 9.2 / 2.3 de la mezcla ES de 120 eventos. `VALORES_EN` B20 9.7 · B21 2.35 → cobertura 119.1 % → **115.8 %** (Word [49] y [86] por token: 9.7 h, 2.4, 116 %); D15 sigue VERDE; G7 = 125 valores |
| m2 | `Instructions!D36` | «Weddings 130 guests × ($9,000 site fee + …)» se leía como 130 × $9,000 → «Per event, excl. sales tax: wedding (130 guests) $9,000 site fee + 10% of $110 F&B per guest; …» |
| m3 | `Instructions!B47:D47` y Word [104] | 40 CFR 141.2 abierta: public water system = «regularly serves an average of at least twenty-five individuals daily at least 60 days out of the year» → citada en la fila D19 y en [104], con «ask your state drinking water program» |
| m4 | `Startup Costs!D10` y Word [79] | «Sprinklers need city water» (falso: basta un suministro suficiente) → «need enough water flow: without city water, a tank and fire pump…» |
| m5 | Word [47] [102] · checklist `Phase 2!E8` | Matiz de la SBA: «extension options **that only you can exercise**» |
| m6 | Word [56] | «the peak arrives with summer and early fall» → «the peaks arrive in June and in September-October, and the trough in January and February» (= O5 y [53]) |
| m7 | Word [97] | «a 8% sales tax rate» → «a sales tax rate of 8%» |
| m8 | Word [114] | «it is a seven-figure investment» → «often a seven-figure investment» (sin fuente) |
| m9 | Word [39] | «as a rain plan, a pergola and a tent» → «a pergola and, as a rain plan, a tent» |
| m10 | Contrato cl. 4 · Modelo 2 cl. 5 | «as your state requires» / «your state or local rules» (la 2.ª persona no cabe en un contrato) → «[State] law» / «[State] or local rules» |
| m11 | Contrato cl. 6 | «which replace any other rule about deposits» (un contrato no desplaza la ley) → «any other term of this agreement about deposits» |
| m12 | Contrato cl. 7 | «To the extent permitted by applicable law, they are applied in proportion to that loss» debilitaba la cláusula de liquidated damages (obligaba a probar la pérdida) → «If applicable law limits these amounts, they apply only to the extent that law allows.» |
| m13 | Contrato cl. 20 | «Data controller» (RGPD) → «Privacy contact» |
| m14 | Contrato, anexo de empresas | «interest… without a prior demand» (mora automática de la Ley 3/2004) → «Late amounts bear interest at [1.5]% per month, or the highest rate the law allows if that is lower.» |

Anotados sin tocar (motivo):

| # | Lugar | Nota |
|---|---|---|
| m15 | Motor común: `Break-Even!B24`/`E24`, `0. Assumptions!C67`, Word «margin of safety» | La «holgura» es invitados del plan / invitados de equilibrio − 1 (19.8 %); el margen de seguridad clásico es 1 − equilibrio / ventas (16.5 %), y «How far you can fall» lo sobrestima. Igual en todos los kits ES y EN y coherente entre Word y Excel: decisión del orquestador para el motor (también en `ERRATAS-ES.md`) |
| m16 | Calculadora `B59:B63` | Los tramos de cancelación se calculan sobre el total con sales tax (10 % de $12,690). Si el importe retenido lleva sales tax depende del estado; tocarlo es cambiar fórmulas. El contrato dice «% of the total price» y pide abogado |
| m17 | Word [99] | Compara los $538,560 del solo alquiler con el equilibrio de la mezcla con comisión ($510,969); el del solo alquiler sería ≈ $520K (variables 18 %). La conclusión («little cushion») se mantiene |
| m18 | `3-Year P&L!B17` | La tarjeta (2 %) se aplica también a la comisión del caterer, que suele llegar por ACH: ≈ $1,500 de prudencia |
| m19 | Contrato cl. 12 | Atribuye la licencia de la música del DJ o la banda al proveedor del cliente; las licencias ASCAP/BMI/SESAC suelen ser del venue. Va con corchetes y con abogado |
| m20 | Checklist `Phase 1!B9` | El sales tax permit (Month 1) va antes que el EIN (Month 2) |
| m21 | `Startup Costs!E5:E28` | «Taxable / recoverable tax? Yes» no tiene efecto (`B41` 0 %): rótulo del motor |

## 4. Gates tras la ronda (VPS, `/tmp/wed-rev.log` y `/tmp/wed-rev2.log`)

| Comprobación | Resultado |
|---|---|
| `check_textos --todas` · `check_contrato --todas` (Mac) | GM, GR, GWED-plan, GWED-check, wed_a y wed_b **OK (0 errores)**; avisos de longitud: GWED-plan c0152 y wed_b [102]/[107] · contrato 1 OK (109 párrafos) y 2 OK (52) |
| `bp9.py mapas` · `verificar` | 0 errores (7 avisos de siempre: FIJOS del motor sin uso) |
| `aplicar_en --idempotencia` · `calibracion` | préstamo $470,000 · 0 diferencias · **D15 VERDE** (holgura 19.8 %, DSCR 1.86, saldo $66,103, cobertura 115.8 %, neto A3 14.2 %, exceso 0.04 %) |
| `ensamblar_docx --plan wed` | G8 VERDE · **25 páginas** Letter (LibreOffice) |
| `calculadora --salida dl/` · `--autotest` | VERDE, 574 comprobaciones; sha canónico **IGUAL** al anterior (no se commitea: solo cambian las fechas) |
| `contrato --salida dl/ --pdf` | VERDE: 161 párrafos, 5,003 palabras, Letter, **12 páginas** |
| `gates_en` (G1-G9) · `gates_en --autotest` · `ensamblar_docx --autotest` | **TODO VERDE** (G7 125 valores) · 20/20 · 8/8 |
| `barrido` · `censo-entregables --fail --letter --only` · `gate-no-latinos --only` | 1,927 piezas, 0 fallos · 0 defectos · 0 caracteres |
| Regresión de los 8 conjuntos (`/tmp/wed-regresion.sh`) | **30/30 IGUAL** |
| 2.ª pasada (aplicar_en + ensamblar_docx + calculadora + contrato en `/tmp/wed-p2*`) | sha256 canónico **IGUAL** en los 5 · `cifras_caso.json` igual salvo `generado` |

| Entregable (`astro-site/public/dl/wedding-venue-business-plan/`) | sha256 (Mac = VPS) |
|---|---|
| `wedding-venue-business-plan.docx` | `8349e0e95a1dc42a…` |
| `wedding-venue-financial-projections.xlsx` | `69dca2b50c30b72d…` |
| `wedding-venue-pricing-calculator.xlsx` (sin cambios) | `d3a49288a8484289…` |
| `wedding-venue-rental-agreement-templates.docx` | `2dc1d61c3138b640…` |
| `wedding-venue-startup-checklist.xlsx` | `dfabfbd574bcda33…` |

## 5. Para la F3 (landing, dashboard y correo)

Cifras que valen: $612,000 · 100 events · 90 guests · $68 per guest · CAPEX $570,500 · cash needed $669,716 · loan $470,000
(10 years, 10 %) · DSCR 1.86× · cash break-even 84 events · margin 20 % · net 8.9 % → 14.2 % · calculadora: Saturday peak
wedding 130 guests $12,690 with tax. Nada de volúmenes de búsqueda, «non-refundable», Cooling-Off afirmada ni citas SBA.
