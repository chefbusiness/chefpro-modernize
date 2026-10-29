# Taco Shop Business Plan Kit (EN) — revisión adversarial final de la F2 (una ronda)
> Sesión Claude Code, 29-oct-2026 (opus). Sobre el paso real del VPS (`/root/wt-taco-en`, rama @ `c2f54a20` + esta ronda).
> Pregunta: ¿se puede vender en EE. UU. tal cual? Cruce Word ↔ libro (caché `data_only`) ↔ calculadora ↔ checklist,
> legal US (F1 §6), jerga (§9) y restos de otros conjuntos. **0 B · 5 M · 8 m: los 13 ARREGLADOS; cifras del caso intactas (D15 verde).**

## Hallazgos (B bloqueante · M mayor · m menor) — todos ARREGLADOS en fuente
| # | Dónde | Qué | Arreglo |
|---|---|---|---|
| M1 | financial-projections `12-Month Cash Flow!O20` (GM c0526, reutilizada) | «Months 4, 7 and 10: December, March and June **with Month 1 in September**»: calendario de otro conjunto (aquí Mes 1 = enero; las liquidaciones caen en E20/H20/K20) | `textos_en/GM.revision.json`: April, July, October; Q4 en el Month 13 (enero) |
| M2 | startup-checklist `Phase 6!E13` (c0845) | Cita el kit «Recurring Tasks: Mexican Taqueria», que NO está en la tienda EN (`kit-tareas-taqueria` sin `urlByLang.en`) | Sin producto inexistente: parte diario + calculadora del kit |
| M3 | Word §6 ¶81 (taq_b 81) ↔ calculadora `Tortillas!B15/B29` | El Word ponía la máquina de $7,808 en la variante nixtamal y «masa harina and a press… around 660»; la calculadora mete máquina + 0.75 FTE en la opción masa harina y da **656.4** | ¶81 reescrito (máquina + persona → ≈ 656); 660 → 656 también en ¶114 y `Phase 1!E7` (c0625) |
| M4 | startup-checklist `Phase 3!E5` (c0711) | «four burners for cones of about **66-77 lb (30-35 kg)**» (conversión del ES) contra el caso de **30 lb** y el Avantco de 3 quemadores del Word | Decidido: manda el caso → «three- or four-burner models sized for the cones you will run (30 lb (13.6 kg) in the case)» |
| M5 | Word ¶49 y ¶94 (`{{cogs_pct}}`), ¶43 y ¶86 (`{{plantilla_jornadas}}`) | Word «26.2%» y «5.02 FTE»; el libro MUESTRA **26.3%** (`3-Year P&L!B52` = 0.2625, `0.0%`) y **5.03** (`Staffing!C12` = 5.025, `#,##0.00`): `mapas.formatear` redondea al par | Tokens `cogs_pct_xl` y `plantilla_jornadas_xl` (`datos_taq._como_excel`: 15 cifras + mitad arriba); código común intacto |
| m1 | Word ¶43, ¶78 · projections `Instructions!B38` (c0446) | «about **208** tacos»; la calculadora da 207.36 (`Trompo Yield!B26`) | → 207 |
| m2 | projections `Staffing!J20` (GM c0387) | «the **January closure**»: el caso abre en enero y no cierra | `GM.revision.json`: sin cierre |
| m3 | Word ¶49 (taq_a 49) | «2.6 tacos, a quesadilla or a side» suma > $17.50 (`0. Assumptions!C5`: «some quesadilla») | 1 de cada 5 quesadilla/gringa y 1 de cada 4 side (= la cuenta del caso) |
| m4 | Word ¶72 ↔ checklist `Phase 5!E16` y P&L `F28` | «two dates… without inventing more» frente a 4 fechas en el libro y el checklist | Añadidas Independence Day (sept.) y Day of the Dead (nov.) |
| m5 | checklist `Phase 1!D12`/`E12` (GRC c0640) | Plazo «Week 1» y nota «apply as soon as you sign the lease» (el contrato es la semana 6) | E12: «Start in week 1: ask your ABC agency and city… file as soon as you sign the lease» (`Week 1` es GM compartida con D8) |
| m6 | Word ¶48 | «an aguas frescas (16 oz)» | «an agua fresca» |
| m7 | calculadora `Tortillas!A9/A14`, `Instructions!A13`; checklist `Phase 1!E7` | «tortillera» sin glosa | «tortilla maker» |
| m8 | projections `Instructions!A12` (c0415) | «desserts» en la media del food cost (la carta US no tiene postres) | «chips and guacamole and birria» |

Sin hallazgo (comprobado): todas las cifras del Word contra caché (inversión 18 filas, P&L, equilibrio $535,960/$521,117,
holgura 19 %, DSCR 2.68×, saldo mín. $79,892 en Mes 1 = enero, payback «Over 3 years»/2.3, escenarios, $15/h mínimo en
Staffing, 308 días, 3.8 rotaciones); taco al pastor $0.999 = 25.0 % sobre $4.00; cono 30 lb → 64.8 %; hoja «Tortillas»
existe. Legal US: Food Code 2022 (41/135 °F, recalentado 165 °F en 2 h, TPHC 3-501.19 con procedimiento escrito, plan
review 8-201.11, CFPM 2-102.12), pastor sin cifra única (145/155 °F «set by your county»), Type I + UL 300 + NFPA 96 (carbón
= solid fuel), 9 alérgenos con sésamo (FASTER), 21 CFR 101.91 sin prometer gluten-free, beer & wine sin prometer, W-2 /
FLSA / I-9 / tip pool, SBA 7(a) 10 años sin carencia, sales tax 8 % de ejemplo fuera de ingresos; cero normativa española.
Cero restos de pizza/otros conjuntos tras M1/m2; °F primero, lb/oz, $, Letter; «authentic» 0; «al pastor»/«trompo» glosados.

Lección (a F2-NOTAS): `POR_CELDA` solo actúa sobre celdas «regenerar» de `textos_es.json`; para corregir una cadena GM/GR
reutilizada en ESTE conjunto se usa `textos_en/<g>.revision.json` (lo reaplica `preparar_tandas`), no `POR_CELDA` (exigiría
re-extraer y renumerar ids). Y `formatear` (pct1/dec2) redondea al par: un 0.xx5 exacto sale distinto de lo que muestra Excel.

## Gates finales (VPS, tras la ronda)
`mapas` 0 errores (111 tokens) · `aplicar_en --idempotencia` 0 dif. · **D15 VERDE** ($176,000; 6.3/8.1/9.2 %; DSCR 2.68×) ·
`ensamblar_docx` G8 VERDE · calculadora autotest VERDE · `gates_en` **G1-G9 TODO VERDE** · `--autotest` 20/20 · docx 8/8 ·
barrido 4 ficheros / 1,733 piezas / 0 fallos · resumen 3,383 piezas 0/0/0 · `censo-entregables --fail --letter` 0 defectos ·
`gate-no-latinos` 0 · `check_textos --todas` 0 errores · 2.ª pasada `canon.py` **4/4 IGUAL** · `regresion_taq.sh` **44/44 IGUAL** (11 conjuntos)

## sha256 (Mac = VPS)
- `taco-shop-business-plan.docx` 7341306a6d58cdfafa96b575ad58c6cca25f40953dce223ebab972e273a23ddb
- `taco-shop-financial-projections.xlsx` f8229aead4addf1d3d38c411ce627f51b751ae39eca783343432935b2306189c
- `taco-shop-startup-checklist.xlsx` 4c1d7e751e8224a1e5f05b748dd2ec0426e9be1a5df98f79e898a01ca46f62bf
- `taco-cost-trompo-yield-calculator.xlsx` 9c872ebcf6520c3d8679b3234a01ac3afe6ca84689a45116e67e48b39f76938e
