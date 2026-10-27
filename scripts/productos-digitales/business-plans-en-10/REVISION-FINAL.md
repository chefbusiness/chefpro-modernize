# Ice Cream Shop Business Plan Kit (EN, $39): revisión adversarial final (D203)

> Sesión Claude Code, 27-oct-2026. Una revisión y una ronda de arreglos, todos por texto: ninguna fila, hoja, DV ni fórmula
> tocada. Material leído: los volcados `revision/*.txt` (Word, libro y checklist), SPEC-delta, F1-research-us-delta, F2-NOTAS y
> `cifras_caso.json`. La landing (D204) aún no existe en la rama: es de la F3.
> **Fuentes primarias abiertas el 27-oct**: Vermont Agency of Agriculture (agriculture.vermont.gov/node/474) · Georgia GAC
> 40-2-8-.01(3)(b) (rules.sos.ga.gov/gac/40-2-8) · 21 CFR 135.110 (law.cornell.edu; eCFR redirige a un captcha) · FDA Food
> Code 2022, PDF de fda.gov (2-102.12, 3-304.12, 3-501.17, extraído con `pdftotext` en el VPS) · IDFA «July is National Ice
> Cream Month» y nota de prensa del 15-jul-2019 · HMRC VAT Notice 701/14 §2.2 y §3.5 · Texas Comptroller 96-280 (solo vía
> buscador: sostiene el ejemplo).

**Recuento: 0 B · 5 M · 12 m.** Arreglados: los 5 M y 11 m; queda 1 m sin arreglar (motivo abajo).

## 0. Lo que se ha recalculado y está bien (no tocar)

| Comprobación | Resultado |
|---|---|
| Ventas | 165 × $7.50 × 310 = **$383,625**; años 2-3 $414,315 y $435,031 (+8 % / +5 % de customers: 178.2 y 187.1) ✓ |
| CAPEX | 19 partidas **$186,000** (obra 81,000 + equipo 90,000 + resto 15,000) + fianza $5,000 + renta previa $5,000 + imprevistos **$8,100** (10 % de B7-B11, por fórmula) = **$204,100** ✓ |
| Necesidad y fondo | 3 × ($232,852 − $21,767) / 12 = **$52,771**; necesidad **$256,871**; fuentes 95,000 + 162,000 = $257,000 (+$128.70; préstamo de cuadre $161,871) ✓ |
| Préstamo y DSCR | 162,000 × 0.10 / (1 − 1.1^−10) = **$26,365**; DSCR año 1 (21,585 + 21,767 + 16,200) / 26,365 = **2.26×**; mínimo 2.26× ✓ |
| P&L | COGS 85,548 (**22.3 %**) · margen tras variables **68.2 %** · personal $128,185 (33.4 %) · prime 55.7 % · EBITDA $66,747 (17.4 %) · neto **$21,585 (5.6 %)** → **8.6 %** el año 3 ✓ |
| Equilibrio y holgura | 232,852 / 5.115 / 310 = 146.8 → **147**; caja 221,250 / 5.115 / 310 = 139.5 → **140**; holgura 165 / 139.53 − 1 = **18.3 %** ✓ |
| Escenarios | 140 × $7 × 300 = $294,000 → −$32,344, caja $32,029 · 190 × $8 × 320 = $486,400 → +$98,872 ✓ |
| Caja (Mes 1 = marzo) | Pesos 5/7.5/10/13.5/**16.5 jul**/15/11/6.5/3.5/6/**2.5 ene**/3 = 100 %; nov-feb 15 % (= C35); abr-sep 73.5 %; saldo mínimo **$46,060** en el Mes 1; sales tax remitido en los meses 4, 7 y 10 ($5,914 · $14,386 · $6,713) = O20 y A34 ✓ |
| Personal | Shift lead $2,946 × 12 / 2,080 = $17.0/h (= J6); scooper de temporada $15/h; cobertura 5,612 / 5,332 = 105 % ✓ |
| Word = Excel | Las 40+ cifras del Word casan con las celdas; no promete nada que el libro no haga (pestañas, celdas verdes, B13/B14, B68, Break-Even por año) ✓ |
| D190 | Base pasteurizada comprada en los 3 ficheros; «pasteuriz» solo para la base comprada o la variante; ningún «85 °C» ni pasteurizador en el caso ✓ |
| Normativa bien citada | 135.110 (10 % milkfat, 4.5 lb/gal, 1.6 lb sólidos, custard 1.4 % / 1.12 %) · 3-304.12(D) dipper well de agua corriente · 3-602.11 · 8-201.11 · 29 CFR 570.35 (3 h / 18 h, 21 h de junio a Labor Day) · FASTER Act · IDFA «July is the busiest production month» (2019) · Ohio 155 °F/30 min y 175 °F/25 s · SBA Microloan $50K · NOL 80 % · Vermont y Georgia tras el arreglo ✓ |
| Jerga y restos | customers, scooper, dipping cabinet, batch freezer, hardening, overrun, dipper well; 0 pizzería/panadería/España (barrido 1,383 piezas, 0 fallos) ✓ |

## 1. B: bloqueantes

Ninguno.

## 2. M: mayores (todos arreglados)

| # | Fichero · lugar | Problema (fuente) | Arreglo | Dónde |
|---|---|---|---|---|
| M1 | Word [64] y [104] · `Instructions!B41` · checklist `Phase 1!E9` | «Buying pasteurized base … keeps you a retail food establishment **in most states**». Sin fuente y lo desmiente el propio ejemplo: Vermont exige **Frozen Dessert License** de la Agencia también con base comprada (página leída) y Massachusetts la trata como frozen dessert manufacturer (research §6.1) | «the lighter route (your retail food permit and, in some states, a frozen dessert license)» · B41 «retail permit, plus a frozen dessert license in some states (Vermont)» · E9 «needs your retail food permit and, in some states (Vermont, for example), a frozen dessert license too» | `docx_en_ice_a` 64 · `docx_en_ice_b` 104 · `GICE-plan` c0453 · `GICE-check` c0633 |
| M2 | Word [104] | Georgia: «does not need a dairy manufacturer's license» **sin la condición** de GAC 40-2-8-.01(3)(b): solo si «the products … are to be consumed on the premises». El caso vende pints to go, delivery y catering. Además, la frase de Vermont estaba rota («treats a pasteurized base as a retail frozen dessert license») | «In Vermont, for example, freezing a pasteurized base needs a Frozen Dessert License from the Agency of Agriculture, and only flavorings may be added after pasteurization, while blending your own mix needs a Milk Handler License. In Georgia, a retailer that freezes a mix from a licensed dairy processor is exempt from the Dairy Manufacturer's License only for ice cream eaten on the premises: ask before you sell pints to go, delivery or catering.» | `docx_en_ice_b` 104 |
| M3 | Word [90] y [105] | «At least one person needs the CFPM (2-102.12)»: es la redacción de 2017. El **Food Code 2022** 2-102.12(A) dice «The PERSON IN CHARGE shall be a certified FOOD protection manager» (PDF de la FDA) | [90] «The person in charge of each shift needs the CFPM certification (Food Code 2022, 2-102.12; states still on an older edition ask for at least one certified manager)» · [105] equivalente | `docx_en_ice_b` 90, 105 |
| M4 | `12-Month Cash Flow!O13` | «(in the case, by about $10,000 in September)»: es la cifra del **ES** (10.000 €, correcta allí con 14 pagas). En el caso US el desfase acumulado a final de septiembre es **$13,777** (scooper 1,430 × 12 en 6 meses + summer 715 × 12 en 3 + assistant 610.50 × 12 en 5, frente al reparto en 12) | «(in the case, by about $13,800 at the end of September)» ($14,000 lo rechaza `check_textos`: cifra de otros casos) | `GICE-plan` c0514 |
| M5 | `Startup Costs!D18` · checklist `Phase 1!E5` y `Phase 2!E7` · Word [50] | «No exhaust hood needed: waffle cone irons produce no smoke» / «need no smoke exhaust»: afirmación normativa rotunda sin fuente (la campana la decide el plan reviewer y el código mecánico local), en la tarea que se hace antes de firmar el lease | D18/E7 «Waffle cone irons usually need no exhaust hood: confirm it with your plan reviewer» · E5 «(and whether the waffle cone irons need a hood: usually not)» · [50] «The winter menu needs no cooking line» | `GICE-plan` c0167 · `GICE-check` c0620, c0666 · `docx_en_ice_a` 50 |

## 3. m: menores

| # | Lugar | Problema | Arreglo · dónde |
|---|---|---|---|
| m1 | Checklist `Phase 1!E5` | Cola sin sentido en la tarea de zoning: «Winter then runs on ice cream cakes…» (resto de las crepes del ES) | Quitada · c0620 |
| m2 | Word [78] y [105] | «Date-mark every tub (3-501.17)»: 3-501.17 es para lo **refrigerado** listo para comer (la base abierta), no para el helado congelado | «Date-mark the base when you open it (3-501.17), label every tub with its batch date» · `ice_b` 78, 105 |
| m3 | Word [53] | La Proclamation 5219 nombró el **15-jul-1984**; el «tercer domingo» es la práctica posterior (IDFA lo resume así) | «…and July 15, that year's third Sunday, National Ice Cream Day, which the industry has celebrated on the third Sunday of July ever since» · `ice_a` 53 |
| m4 | `0. Assumptions!C39` | «UK: 20% VAT on hot food and dine-in» (de la pizza): el helado es standard-rated también para llevar (VAT Notice 701/14 §2.2) | «UK: ice cream is standard-rated at 20% VAT, to take away too» · `textos_en/GM.revision.json` c0070 (nuevo; mecanismo de la pizza) |
| m5 | `Instructions!A8` | «The scoop is taxed as prepared food» rotundo | «A scoop is generally taxed…» · c0406 |
| m6 | `3-Year P&L!F10` | Sub-repartos (65/15/10/5/4) leídos sobre «Share of total sales» (con bebida, 109 %) y remite a «Delivery share of sales», que no existe | «Within this line, roughly: … and pints through delivery marketplaces the rest (see "Delivery share of total sales")» · c0215 |
| m7 | `0. Assumptions!C26` | Calco: «the local's history» | «the space's billing history» · c0046 |
| m8 | `Staffing!J7` · Word [87] | «part-time» junto a «about 40 hours a week» y al Word [85] «full time in those months» | J7 «Seasonal W-2 employee: about 40 hours a week…, which equals half a full-time position over the year (part-time on a yearly basis)» · [87] «seasonal W-2 employees» · c0364, `ice_b` 87 |
| m9 | Word [86] | «105 % … with no surplus» | «with a small margin» · `ice_b` 86 |
| m10 | Checklist `Phase 3!E10` | Mínimos de pasteurización sin decir que son de un estado | «(in Ohio, for example, …; your state sets its own)» · c0726 |
| m11 | Checklist `Phase 3!B19/E19` | La tarea es el acuerdo con el proveedor de base y la nota no lo menciona | Antepuesto «Written agreement with the base supplier: delivery at 41 °F (5 °C) or colder, a lot code on every case and a copy of the dairy's license.» · c0748 |
| m12 | Checklist `Phase 1!C9` | Responsable de la decisión de licencia = «Accountant» | **Sin arreglo**: es la cadena c0622 («Gestoría»), compartida por 9 celdas; cambiar solo C9 obliga a un POR_CELDA y a re-extraer `textos_es.json` |

## 4. Notas

- **F3 (landing, hub, correo)**: no copiar «in most states», «no license needed», «no hood needed» ni «at least one CFPM»; Georgia
  solo con su condición «eaten on the premises». La regla B2 (toda licencia prometida con su tarea) ya se cumple: license
  decision (F1 B9), health permit (F3 B8), sales tax permit (F1 B8), patio (F2 B14), building permit/CO (F2 B11, B19).
- `0. Assumptions!A40/A63` (sales tax del alcohol) quedan como celdas dormidas del motor: B62 = 0 y C62/C63 lo explican.
- Fuera de alcance, por si aplica: la Pizza EN y el Ice Cream Shop Checklists Kit Pro pueden llevar la redacción 2017 del
  CFPM («at least one»); no se ha comprobado.
- **ES LIVE**: ninguna errata nueva. El «hasta unos 10.000 € menos en septiembre» del ES es correcto con su plantilla
  (650/325/260 € × 14 pagas × 1,33 → 9.582 €); por eso no se crea `ERRATAS-ES.md`.

## 5. Gates tras la ronda (VPS, `/tmp/ice-rev-*.log`)

| Comprobación | Resultado |
|---|---|
| `check_textos --todas` (Mac) | 7 tandas OK (0 errores; 6 avisos de longitud en GM y 1 en c0633) · `GM.revision.json` aplicada por `preparar_tandas` |
| `bp10.py mapas` · `verificar` | 0 errores (6 avisos de FIJOS sin uso, los de siempre) |
| `aplicar_en --idempotencia` · `calibracion` | préstamo $162,000 en 1 vuelta · faltan 0 · 0 diferencias · 0 fallos de pycel · D15 **VERDE** (cifras sin cambios) |
| `ensamblar_docx --plan ice` | G8 VERDE · 131 párrafos · 7,074 palabras · **24 págs. Letter** (`pdfinfo`) |
| `gates_en` · `--autotest` · `ensamblar_docx --autotest` | **G1-G9 TODO VERDE** · 20/20 · 8/8 |
| `barrido` · `resumen_entregables.py` | 1,383 piezas, 0 fallos · 3,363 piezas, prohibidas / español / no latinos 0 |
| Regresión (`regresion_ice.sh`) | **31/31 IGUAL** |
| 2.ª pasada | sha256 canónico **IGUAL** en los 3; `cifras_caso.json` igual salvo `generado`; se publican los de la 1.ª pasada |

| Entregable (`dl/ice-cream-shop-business-plan/`) | sha256 (Mac = VPS) |
|---|---|
| `ice-cream-shop-business-plan.docx` | `79e36bc75ef528ac…` |
| `ice-cream-shop-financial-projections.xlsx` | `7614f552ad6acf40…` |
| `ice-cream-shop-startup-checklist.xlsx` | `4378abf69e0a927b…` |
