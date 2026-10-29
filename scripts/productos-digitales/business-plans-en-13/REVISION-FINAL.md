# Rotisserie Chicken Restaurant Business Plan Kit (EN): revisión adversarial final de la F2 (una ronda)
> Sesión Claude Code, 29-oct-2026 (opus). Sobre el paso real del VPS (`/root/wt-rotisserie-en`, rama @ `e603860d` + esta ronda).
> Pregunta: ¿se puede vender en EE. UU. tal cual? Cruce Word ↔ libro (caché `data_only`) ↔ calculadora ↔ checklist,
> legal US (F1 §6), jerga (§9) y restos de otros conjuntos. **0 B · 3 M · 6 m: los 9 ARREGLADOS; cifras del caso intactas (D15 verde).**

## Hallazgos (B bloqueante · M mayor · m menor), todos ARREGLADOS en fuente
| # | Dónde | Qué | Arreglo |
|---|---|---|---|
| M1 | Word ¶78, ¶79, ¶112 · checklist `Phase 1!E7` (c0621) | Citan las pestañas «Bird Cost» y «Rotisserie Loads», que no existen: las hojas son `Chicken Yield` · `Rotisserie` · `Costing` · `Instructions` | → «Chicken Yield» y «Rotisserie» (`docx_en_pol_b` 78/79/112, `GPOL-check` c0621) |
| M2 | Word ¶105 · checklist `Phase 3!B11/E11` (c0724, c0726) · projections `Instructions!D44` (c0467) · calculadora `Instructions!A8` | «TPHC 4 h… a las 4 h enfría con registro para mañana»: bajo TPHC (3-501.19) lo que llega a 4 h se vende o se tira, NUNCA se enfría; `Instructions!B44` ya decía «then discard» (contradicción interna) | SOP = hot holding ≥ 135 °F con hora y límite propio de 4 h (enfriar o tirar); TPHC como vía alternativa: a las 4 h se tira, sin enfriar ni recalentar |
| M3 | Gates G8 y barrido ROJOS · Word ¶81 · `Startup Costs!D12` (c0155) · `Instructions!D40` (c0451) | `\$27\b` (caso Bar EN) casaba con «$27,945» (pérdida del pesimista) y obligó a escribir «27,500 to 35,950 US dollars»; «1 therm = 100,000 BTU» casaba con los $100,000 del Taco EN | `datos_pol.py`: `$27`/`$36` con `(?![.,]\d)` y `EXCEPCION_CIFRA {100000: BTU/therm}`; importes con «$» en los 3 sitios |
| m1 | Word ¶48, ¶49, ¶95 · P&L `A11`/`F11` · `0. Assumptions!C14` (c0024) · `Startup Costs!D24` (c0180) · checklist `Phase 5!B11` (c0796) · calculadora `Costing!L13`/`A25` | Marca registrada «Inca Kola» en 10 sitios | Genérico: «sodas», «Peruvian golden soda», «Peruvian or other soda»; `RX_POL_NO` la veta desde ahora |
| m2 | P&L `F10` (c0214) | Reparto 42 + 42 + 15 = 99 % | 42.5 % + 42.5 % + 15 % |
| m3 | Word ¶43 | «a second rotisserie cook who also covers prep and relief»: funde dos puestos de `Staffing` (A6 y A11) y la lista no suma 10 personas | Dos puestos, como ¶85 |
| m4 | `0. Assumptions!C13` (c0022) | «sandwich or bowl about 21%»; la calculadora da 21.6 % (`Costing!H33`) | → 22 % |
| m5 | `0. Assumptions!C8` (c0014) · checklist `Phase 1!E7` | «before the afternoon rush»; la calculadora fija el pico del domingo en la comida (hasta 1:30 PM, `Rotisserie!B13/B14`) | «before the Sunday lunch peak» |
| m6 | checklist `Phase 3!E14` (c0733) | Etiqueta 3-602.11 sin la cantidad neta (el Word ¶105 sí la pide) | Añadida «the net quantity» |

Sin hallazgo (comprobado): Word ↔ caché: inversión 18 filas ($237,832 + $97,876 = $335,708), préstamo $216,000 al 10 %
a 10 años, cuota $35,153, ventas $819,000/$868,140/$902,866, neto $57,946/$77,410/$90,465 (7.1 %), EBITDA $123,379
(15.1 %), personal $271,009 (33.1 %, 10 personas, 6.60 FTE, cobertura 101 %), alquiler $44,796 (5.5 %), equilibrio 110 /
107 covers ($690,723 / $672,519), holgura 22 %, DSCR 2.96×, saldo mín. $103,822 (Mes 1 = enero), payback 2.8 / 2.1,
escenarios ($644,325 −$27,945 · $1,004,550 +$189,018), 130 covers × $17.50 × 360, food 86 % / bebida 14 %, COGS 29/22 %,
rampa 75 % en 4 meses. Word ↔ calculadora: $5.99 por pollo, rendimiento 72 % (70-75 %), whole 31.5 %, family meal 29.6 %,
48 por rotisserie y 96 por carga, 192 de capacidad antes de la 1:30 PM, 65-70 pollos el domingo y 120-150 los días punta,
60-75 pollos/h (research §8). Campana $26,000 dentro de $5,000-$28,000 (REST §3) en Word ¶80, `Startup Costs!D9` y
research. Nombre «Rotisserie Chicken Yield & Costing Calculator» igual en Word, libro, checklist y la propia calculadora.
Legal US: Food Code 2022 (165 °F 3-401.11, 135 °F 3-501.16, cooling 3-501.14, recalentado 3-403.11, plan review 8-201.11,
CFPM 2-102.12, etiqueta 3-602.11, salud del empleado 2-201) con «your county's rules», Type I + UL 300 + makeup air, NFPA 96
cap. 14 para carbón (escape propio, arrestachispas, cenizas), 9 alérgenos con sésamo (FASTER), 21 CFR 101.91 sin prometer
gluten-free, beer & wine sin prometer, W-2/FLSA/I-9/tip pool, SBA 7(a) sin carencia y Microloan $50,000, sales tax 8 % de
ejemplo fuera de ingresos; nota UK aparte; cero normativa española. Jerga: «pollo asado» solo negado (= mexicano),
«peri-peri» en minúscula, «Broaster» solo como «is a brand», «authentic» 0. Productos citados (Food Cost Kit Pro, HACCP
Food Safety Kit Pro, Restaurant Checklists Kit Pro, Food Truck Business Plan Kit, Equivalents Guide): todos en la tienda EN.
No cambiado (decisión): título de docProps de la calculadora «(Chicken Cost, Rotisserie Loads and Plate Costing)», que es
descriptivo y no nombra pestañas; `0. Assumptions!C5` suma $17.45 frente a $17.50 con «about» (cuenta de la research §8).

Lección (a F2-NOTAS): un gate de cifra con `\b` final casa con el prefijo de un importe mayor («$27» en «$27,945»), y el
traductor lo esquivó cambiando el formato («US dollars»): ante un falso positivo se arregla el regex, no el texto.

## Gates finales (VPS, tras la ronda)
`check_textos --todas` (Mac) 0 errores · `mapas` 0 errores · `aplicar_en --idempotencia` 0 dif. · **D15 VERDE** ($216,000;
7.1/8.9/10.0 %; DSCR 2.96×) · `ensamblar_docx` G8 VERDE · calculadora generada + autotest VERDE · `gates_en` **G1-G9 TODO
VERDE** · `--autotest` 20/20 · docx 8/8 · barrido 4 ficheros / 1,708 piezas / 0 fallos · resumen 3,361 piezas 0/0/0 ·
`censo-entregables --fail --letter` 0 defectos · `gate-no-latinos` 0 · `regresion_pol.sh` **48/48 IGUAL** (12 conjuntos) ·
2.ª pasada `canon.py` **4/4 IGUAL**

## sha256 (Mac = VPS)
- `rotisserie-chicken-restaurant-business-plan.docx` 4301cd6c2ee27222635378036ca540b11272d1a7f4eea700e922be4911f614d1
- `rotisserie-chicken-restaurant-financial-projections.xlsx` 66bd508db56f990c0c55a753a810b1fb5668eaae339f88e7d02506084caa1a10
- `rotisserie-chicken-restaurant-startup-checklist.xlsx` f0d73e5c57ddaac9434450ffe1aa58e1472ea31d5fdc56871fc335d1dc6e29d8
- `rotisserie-chicken-yield-costing-calculator.xlsx` d0087c9a5caac832585e85a2464b075373678cf6bcb1b5ae595ff36088423cef
