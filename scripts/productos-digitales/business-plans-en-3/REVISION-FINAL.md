# Bar Business Plan Kit (EN) — revisión adversarial final (1 ronda) · sesión Claude Code 2026-10-11

Rama `feat/bar-business-plan-en` @ `6fedd0e3`. Revisor: 1 Opus (solo lectura). **Veredicto: listo tras arreglar los 7 MAYOR;
0 BLOQUEANTES.** Cifras clave recalculadas a mano y cuadran al dólar (ventas $923,400 · COGS 24.8 % · personal $308,827 ·
fijos $543,133 · EBITDA $171,583 · equilibrio 81/79 · holgura 21 % · cuota $60,053 · DSCR 2.44× · FM $127,232 · payback 2.5 ·
pesimista −$122,493 / caja $15,791). Fuentes abiertas y conformes: R Street (Boston > $450,000), Poster ($425,500; $110K-$550K;
reserva $75K-$100K; licencias $3K / $12K-$400K), BevSpot (18-24 %; 24/15/28 %), Insureon ($2,039), Restaurant365 ($100K-$850K+;
prime cost 60-65 %), DOL ($2.13/$5.12; 7 estados sin tip credit + Guam; Montana solo negocios > $110K).

**Decisión del orquestador:** se aplican los 7 MAYOR y los 17 MENOR, **todo por la vía de TEXTO** (M4 incluido: no se cambia
`B54`), así que ninguna cifra de `cifras_caso.json` se mueve.

## MAYOR

- **M1 · margen bruto vs COGS** (docx [42], [100]). 100 − 24.8 ≠ 69.7: el 69.7 % descuenta además tarjeta, desechables y
  contingencia (5.5 %; `3-Year P&L!B19` = 30.3 %), y [100] dice que esos costes «are budgeted separately».
  - [42] → «Cost of goods runs at 24.8% of sales; after card fees, disposables and the contingency line (5.5% more), the gross
    margin is 69.7%, and year-1 EBITDA is 18.6% of revenue.» (adaptar a los tokens del párrafo)
  - [100] → «…cost of goods of 24.8% of total sales; with card fees, disposables and contingency the variable costs reach 30.3%,
    for a gross margin of 69.7%» y «Card fees, disposables and contingency are variable costs counted before the gross margin.»
- **M2 · pesimista sin toda la verdad** (docx [102]). EBITDA ≈ −$51,400: la cuota sale de la reserva y un segundo año igual
  agota la caja. Sustituir desde «The pessimistic case…» hasta «$15,791.» y la última frase por: «The pessimistic case assumes
  71 covers a day at an average check of $25.00 over 340 days, for revenue of $603,500 and a pre-tax loss of $122,493.
  Operations lose money even before depreciation and interest (about $51,000), so the loan payment comes out of the working
  capital reserve: the bar ends year 1 with an estimated $15,791 of cash, and a second year like that would run out of cash. …
  Read the pessimistic case as a stress test: if it is plausible in your market, you need a bigger reserve, a smaller loan or a
  smaller opening.» (con tokens donde el párrafo los use)
- **M3 · happy hour / bebida gratis sin aviso legal** (docx [58], [76]; ver [39], [48], [75]). MA (1984) y UT (2011) prohíben
  las ofertas de bebida rebajada; otros estados las limitan.
  - [58] al final: «Check your state's rules first: some states, including Massachusetts and Utah, ban discounted drink specials,
    and many limit free drinks in loyalty programs; there, build the early evening around food specials and events.»
  - [76]: «redeemable for drinks, plates or special experiences» → «redeemable for plates, merchandise or special experiences
    (free drinks are restricted in some states)».
- **M4 · 2 meses de alquiler previo vs licencia 3-12 meses** (vía de texto):
  - `0. Assumptions!C54` → «You pay for the space from the day you sign. These months are a startup cost: they do NOT overlap
    the P&L, which starts on opening day. If your liquor license is likely to take longer than the build-out (often 3-12 months
    from signing), enter the months until it is issued, or negotiate a license contingency and rent abatement in the lease.»
  - Checklist `Phase 2!E6` → «Ask for 2-3 months of rent abatement during the build-out and a liquor license contingency, so
    rent does not start, or you can exit, if the license is late or denied.»
  - Docx [114] → «…so start it early, negotiate a license contingency in the lease and, if you expect it to take longer than the
    2 months of pre-opening rent the workbook budgets, raise that number on "0. Assumptions".»
- **M5 · frase sin sentido sobre el payback** (docx [59]) → «The example in this plan, with $361,700 of startup costs, sits
  inside that range, and the workbook puts its payback before debt at 2.5 years.» (con tokens)
- **M6 · la LLC no es federal** (docx [106]) → «You form your entity, usually an LLC, with your state's Secretary of State, and
  at the federal level you get an Employer Identification Number from the IRS at no cost. Also at the state level you register
  for a seller's permit or sales tax account, and your alcohol license comes from a state agency.»
- **M7 · restos españoles:** checklist `Phase 4!E5` → «Overlapping evening shifts; build the schedule around the after-work
  rush, the evening peak and last call» · `Phase 4!E13` «cocktails and vermouth» → «cocktails and wine by the glass» ·
  `Instructions!D69` «there is no union agreement table to copy» → «Check your state and city rates at dol.gov» ·
  `Phase 1!E6` → «Most states let you file online; check the name is available first».

## MENOR

| # | Dónde | Arreglo |
|---|---|---|
| m1 | docx [107] | «which Poster's survey puts at…» → «which Poster puts at $12,000 to $400,000» |
| m2 | docx [42] (y [118]) | tras el neto: «(after a 25% C corporation tax example; pass-through owners set it to 0 and pay tax personally)» |
| m3 | `Startup Costs!D8` | añadir «Most states also charge an annual or biennial renewal fee: add it to your fixed costs» |
| m4 | `Assumptions!C45` / `C44` | C45: «Griddle, fryer, oven, refrigeration, the bar build and furniture»; C44: añadir «including the draft beer system» |
| m5 | `Scenarios!E24` | «"5. Staffing"» → «"Staffing"» |
| m6 | `Instructions!D55` | citar la fila por su rótulo real «Cost of goods sold on BEVERAGE sales» |
| m7 | `Assumptions!C51` | «…dining room seats and bar stools; add patio seats only if they are open most of the year» |
| m8 | `Assumptions!C63` | «…add 6.7% × your alcohol share (about 6 points at 90%) to your beverage cost %» |
| m9 | docx [94] | «US food law requires you to…» → «the FDA Food Code, as adopted by your state, requires you to…» |
| m10 | docx [82], checklist `Phase 3!E11` | «A draft installer, sometimes arranged through your distributor, installs the lines and glycol; budget it yourself» |
| m11 | checklist `Phase 1!E8` | quitar «can affect inspections and your liquor license class» |
| m12 | checklist `Phase 3!D5` | «2-4 weeks» → «1-3 months» |
| m13 | checklist `Phase 6!B6/C6` | B6 «Weekly food and pour cost check»; C6 «Owner + kitchen lead» |
| m14 | docx [116] | añadir «pre-opening payroll and training come out of the working capital reserve» |
| m15 | docx [100] | añadir «employer FICA on reported tips is not modeled (largely offset by the FICA tip credit; ask your CPA)» |
| m16 | docx [39] | tendencia sin fuente → «Many neighborhoods are seeing…» o quitar |
| m17 | `Staffing!A29` | quitar la 2.ª frase («FTE is the share…») para que la fila no mida 284 pt |

Opcional aceptado: `Instructions!A52` → «US INDUSTRY BENCHMARKS (sourced) AND KIT ESTIMATES».
«guests» vs «covers»: no confunde (las cifras siempre con «covers»); no se toca.
