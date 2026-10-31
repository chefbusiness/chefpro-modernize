# SPEC — `business-plans-en-14/calculadora_sus.py` (Sushi Fish, Rice & Costing Calculator, EN/US)

Write `scripts/productos-digitales/business-plans-en-14/calculadora_sus.py` = the ES calculator
`scripts/productos-digitales/plan-sushi/calculadora_sus_es.py` (same 4-sheet structure, same rows/blocks/formula logic,
same `calcular()` mirror, `EXPUESTOS`, `valores_expuestos`, protection without password, green inputs unlocked,
inject_cache, autotest with pycel + cache = `calcular()` with 3 input sets) TRANSLATED with the code pattern of the EN
twin `scripts/productos-digitales/business-plans-en-13/calculadora_pol.py` (imports of `mapas as M` with
`os.environ.setdefault('BP_CONJUNTO', 'sus')`, `_PL = M.PLANES['sus']`, VERSION/MES from mapas, VERSION_LINEA, FOOTER_EN,
FIRMA_EN, AVISO_EN, URL_TIENDA, US Letter, number formats without currency symbol and labels with «($)», docProps in
English, `--salida` generates + inject_cache + autotest, `--autotest` only tests an existing file, PROHIBIDOS list +
`datos_sus.RX_SUS_NO` + `M.no_latinos` + `M.restos_espanol` checks on every text cell, `motor.gate_formatos`).

- File: `sushi-fish-rice-costing-calculator.xlsx`. Visible name: **«Sushi Fish, Rice & Costing Calculator»**; docProps
  title «Sushi Fish, Rice & Costing Calculator (Fish Yield, Sushi Rice and Cost per Piece)».
- Sheets: `Fish Yield` · `Sushi Rice` · `Costing` · `Instructions`.
- Units: fish in **$/lb**, portions in **oz** with the grey constant «16 oz per lb» (no typed numbers in formulas except
  0/1); vinegar in **fl oz** per lb of cooked rice and **$/gallon** with the grey constant «128 fl oz per gallon»; «60
  minutes per hour» constant. °F only in instruction text. No kg, g, ml, °C, € anywhere (metric only in parentheses in
  instruction text if at all).
- Every default is «Kit estimate, editable» unless a source is given (sources = `business-plans-en-14/F1-research-us-delta.md` §4-§5).

## Fish Yield (= ES `Pescado`): 3 fish + 1 free column, B..E
| # | Name | $/lb | yield (loin/usable) | trim reused |
|---|---|---|---|---|
| 0 | Whole farmed Atlantic salmon | 7.50 | 0.55 | 0.15 |
| 1 | Salmon fillet, skin-on, pin-bone out | 20.00 | 0.85 | 0.03 |
| 2 | Yellowfin tuna saku block (frozen) | 23.00 | 0.90 | 0.05 |
| 3 | Other fish (type yours) | 24.50 | 0.80 | 0.05 |
Price note: «No wholesale price was read for sushi salmon in Oct 2026: NYC auction reports $18-24/lb for sushi salmon (weak source) and yellowfin saku retails at about $22.99/lb (Costco). The kit puts 7.50 · 20.00 · 23.00 · 24.50 $/lb. Kit estimate (Oct 2026): replace with your distributor's price.» Yield note: usable loin 45-60% of a whole salmon (secondary sources); measure it with 3 fish (Instructions).
Common inputs: case shrink 5% · oz of neta per nigiri slice 0.5 · oz per sashimi cut 0.5 · oz of fish per roll 1.5 · cleaning minutes per whole fish 25 («No source: time it») · head sushi chef cost per hour $33.00 («$5,199 a month × 12 + 10% payroll taxes ÷ 2,080 h ≈ $33/h») · weight of a whole fish 11 lb · parasite dropdown (informative, changes no figure) with 3 options and reminders:
1. «I freeze in-house: −4 °F for 7 days or a −31 °F option» → «FDA Food Code 2022, 3-402.11: −4 °F or below for 168 hours (7 days), or −31 °F until solid and 15 hours, or −31 °F until solid and 24 hours at −4 °F. Log time and temperature of every lot and keep the records 90 days (3-402.12).»
2. «Arrives frozen with a supplier letter» → «Keep the supplier's written agreement or statement for every lot: it must show the freezing time and temperature. Keep it 90 days after you serve the fish (3-402.12).»
3. «Exempt: tuna species or feed-raised aquaculture» → «Tuna (Thunnus species) and feed-raised aquaculture fish such as farmed salmon are exempt only with a written statement from the supplier or the farm. File it and ask again if the source changes.»
Outputs: usable share · **COST PER USABLE LB** = price ÷ (yield + trim) ÷ (1 − shrink) [defaults ≈ 11.28 · 23.92 · 25.48 · 32.24] · cost of a nigiri slice / sashimi cut / roll fish = cost per lb × oz ÷ 16 · labor block: cleaning cost of a whole fish = min ÷ 60 × $/h · usable lb of a whole fish = weight × yield of column 0 · labor per usable lb · whole cost with labor · **«THE WHOLE FISH PAYS OFF AS LONG AS CLEANING COSTS LESS THAN ($ per usable lb)»** = fillet cost − whole cost · verdict «The whole fish pays off» / «Buy the fillet» · reminder of the parasite case.

## Sushi Rice (= ES `Arroz`)
Inputs: raw sushi rice (Calrose) $/lb 1.04 («50 lb bag $51.99 = $1.04/lb, webstaurantstore.com, Oct 2026; medium grain $1.24-1.28/lb») · raw → cooked factor 2.2 · sushi vinegar (sushi-zu) fl oz per lb of cooked rice 1.5 · sushi vinegar $/gallon 20.50 («seasoned rice vinegar about $20.50/gal, webstaurantstore.com») · oz of sushi rice: nigiri 0.75 · maki (thin roll) 2.5 · inside-out roll 3.0 · hand roll 2.0 · poke bowl 6.0 · nori $ per sheet 0.31 («100 full sheets $31.49, webstaurantstore.com») · sheets: nigiri 0.05 · maki 0.5 · inside-out roll 0.5 · hand roll 0.5 · poke 0.1 · rice thrown out at close 5% · covers per day 115 («the case of the business plan») · oz of sushi rice per cover 5.0 · constants 16 oz per lb, 128 fl oz per gallon.
Outputs: **LB OF SUSHI RICE PER LB OF RAW RICE** = factor × (1 + vinegar fl oz ÷ 16) [≈ 2.41] · **COST PER LB OF SUSHI RICE** = (rice + factor × vinegar ÷ 128 × $/gal) ÷ lb of sushi rice · with close discard · **NIGIRI PER LB OF RAW RICE** = 16 × lb sushi rice ÷ oz per nigiri [≈ 51] · rice cost and nori cost per piece type · sushi rice sold per day (lb) = covers × oz ÷ 16 · **LB OF RAW RICE PER DAY** · with discard. Fixed note (instead of the ES «Kit de Tareas»): «Time-stamp every batch (TPHC, 4 hours) or, if your county approved a variance, log the pH of every batch in your HACCP plan records.»

## Costing (= ES `Escandallo`)
General inputs: **sales tax included in menu prices 0%** («US menus usually exclude sales tax: leave 0%. Type your rate only if your prices include it; UK: VAT is 20% dine-in and cold take-out sushi is often zero-rated») · target food cost 30% · watch band 5 points · to-go packaging per order $0.60 · marketplace packaging per order $1.00 · marketplace price markup 15% · marketplace commission 25% («on the price before tax; check your contract»). Links to the Sushi Rice sheet (cost per lb of sushi rice with discard, nori per sheet).
Products (name, fish column 0 none / 1-4 = Fish Yield column B-E, oz neta, oz sushi rice, nori sheets, other ingredients $, menu price $, units per week):
| Product | fish | oz neta | oz rice | nori | other $ | price $ | units/wk |
|---|---|---|---|---|---|---|---|
| Salmon nigiri (2 pcs) | 2 | 1.0 | 1.5 | 0.10 | 0.05 | 7.00 | 140 |
| Tuna nigiri (2 pcs) | 3 | 1.0 | 1.5 | 0.10 | 0.05 | 7.50 | 90 |
| Salmon sashimi (5 pcs) | 2 | 2.5 | 0 | 0 | 0.08 | 14.00 | 50 |
| Salmon maki (6 pcs) | 2 | 1.0 | 2.5 | 0.5 | 0.05 | 6.50 | 30 |
| California roll (8 pcs) | 0 | 0 | 3.0 | 0.5 | 0.75 | 8.50 | 120 |
| Spicy tuna roll (8 pcs) | 3 | 2.0 | 3.0 | 0.5 | 0.25 | 9.50 | 100 |
| Shrimp tempura roll (8 pcs) | 0 | 0 | 3.0 | 0.5 | 2.20 | 11.00 | 80 |
| Salmon hand roll | 2 | 1.0 | 2.0 | 0.5 | 0.30 | 7.00 | 40 |
| Salmon poke bowl (uses whole-salmon trim) | 1 | 4.0 | 6.0 | 0.1 | 1.20 | 16.00 | 50 |
| Sushi platter, 12 pcs | 2 | 3.0 | 6.0 | 0.5 | 0.40 | 22.00 | 30 |
| Party platter, 24 pcs | 2 | 6.0 | 12.0 | 1.0 | 0.60 | 42.00 | 15 |
| Gyoza (6 pcs) | 0 | 0 | 0 | 0 | 1.60 | 8.00 | 60 |
| Edamame | 0 | 0 | 0 | 0 | 0.70 | 5.50 | 60 |
| Mochi ice cream (2 pcs) | 0 | 0 | 0 | 0 | 1.40 | 6.00 | 40 |
Notes: «Other ingredients: imitation crab $1.80/lb, avocado, cucumber, sauces, sesame, tempura shrimp ($16.44/lb, 16/20), wasabi and ginger, at Kit estimate prices». Outputs per product (same columns as ES): cost · price before tax · food cost % with traffic light (On target / Watch the cost / Above target) · suggested price · **margin $ by channel** (dine-in = price − cost; take-out/pickup = dine-in − to-go packaging; marketplace = price × (1 + markup) × (1 − commission) − cost − marketplace packaging) · rank by dine-in margin. Totals: weekly sales before tax, weekly food cost, **WEIGHTED FOOD COST** + traffic light. Fixed warning: «Tempura and gyoza travel badly: keep them off the marketplace menu or warn the guest.» Bridge note: «The plan's 32% food cost (0. Assumptions B13 of the Financial Projections) is the real usage of the whole menu, with case shrink, trim that is not reused, rice and nori thrown out, staff meals and comps: this weighted theoretical cost comes out lower. Do not copy it into the plan.»

## Instructions (= ES `Instrucciones`, US content)
Steps: weigh 10 slices and 10 rice balls and type the average; measure the yield of 3 whole salmon (raw weight, usable loin, reused trim); parasite rule (Food Code 2022 3-402.11 three options; exemptions tuna species and feed-raised aquaculture with written statement; supplier letter; records 90 days, 3-402.12; «sushi-grade» has no legal definition); sushi rice (TCS: TPHC 3-501.19 up to 4 hours with the time marked and a written procedure, then discard; or a variance with a HACCP plan for acidified rice, 3-502.11 — the Food Code annex gives pH < 4.2 as an example critical limit and each county sets its own: the kit does not set a legal pH); scombrotoxin: receive tuna, yellowtail and mackerel at 40 °F or below; consumer advisory 3-603.11 on the menu and the marketplace listings; sales tax (menu prices before tax); the cost per piece of this calculator is NOT copied into the plan; «Kit estimate, editable»; the version line; the AI Chef Pro signature (FIRMA_EN), the store URL and AVISO_EN as in `calculadora_pol.py`. Name the other files of the kit exactly: «Sushi Restaurant Financial Projections», «Sushi Restaurant Startup Checklist», «Sushi Restaurant Business Plan».

## EXPUESTOS (names exactly)
COST_LB_WHOLE_SALMON (Fish Yield B cost per usable lb) · COST_LB_SALMON_FILLET (C) · COST_LB_TUNA_SAKU (D) · WHOLE_PAYS_OFF_BELOW (X) · LB_SUSHI_RICE_PER_LB (Sushi Rice) · NIGIRI_PER_LB_RICE · RICE_PER_DAY_LB · FC_SALMON_NIGIRI · FC_CALIFORNIA_ROLL · FC_SPICY_TUNA_ROLL · FC_PARTY_PLATTER_24 · MARGIN_DINEIN_PLATTER24 · MARGIN_MARKETPLACE_PLATTER24 · FC_WEIGHTED.

## Autotest (= ES + EN twin)
pycel and cache ± 0.01 against `calcular()` with 3 input sets · cost per usable lb = price ÷ (y + t) ÷ (1 − s) · nigiri per lb = 16 × f × (1 + z ÷ 16) ÷ g · marketplace margin < take-out < dine-in for both platters · salmon nigiri default FC in 18-30% · spicy tuna roll default FC > target (above 30%) · Letter paper, protection, 0 formulas without cache, 0 typed numbers in formulas (except 0/1) · `motor.gate_formatos` 0 · DV · docProps · PROHIBIDOS (add: sushiman, combinado, vitrina, surimi, sushi-grade without negation, «−20 °C», kg, g, ml, €, IVA, RD 1021, RD 1086, anisakis rule ES, taco, trompo, rotisserie, pizza) + `datos_sus.RX_SUS_NO` + no latinos 0 · then `python3 scripts/productos-digitales/parche_xml_xlsx.py --check <file>` must be clean.
