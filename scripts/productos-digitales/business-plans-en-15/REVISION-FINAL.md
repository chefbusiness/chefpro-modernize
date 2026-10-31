# Burger Restaurant Business Plan Kit (EN): revisión adversarial final de la F2 (una ronda)
> Sesión Claude Code, 31-oct-2026 (opus, el lead). Sobre el paso real del VPS (`/root/wt-burger-en`), con el Word volcado párrafo a
> párrafo, los textos EN del plan y del checklist (`textos_en/GBUR-*.json`, `GR/GRC.revision.json`) y las celdas legales de la
> calculadora. Pregunta: ¿se puede vender en EE. UU. tal cual? Cruce Word ↔ caché del libro ↔ calculadora ↔ checklist, legal US
> (F1 §6), jerga (§9) y restos de otros conjuntos. **0 B · 3 M · 5 m: los 8 ARREGLADOS en fuente (solo texto); cifras del caso y
> valores por defecto intactos (D15 verde).**

## Hallazgos (B bloqueante · M mayor · m menor), todos ARREGLADOS
| # | Dónde | Qué | Arreglo |
|---|---|---|---|
| M1 | Word ¶74 y ¶113 (frente a ¶54, F5!E13 y la research §6.10) | «the burger travels well, but the fries…»: contradice ¶54 y la research (la smash llega PEOR: la crust se ablanda en ~15 min) | «a smash burger travels worse than it looks… and the fries suffer most» |
| M2 | Word ¶46 | La variante gourmet: «its risk is the cooking temperature, which your food safety plan has to decide» (marco español: allí decide el APPCC; en EE. UU. el Food Code fija 155 °F y lo poco hecho exige advisory) | «a burger cooked to order needs the consumer advisory of Food Code 3-603.11 on the menu» |
| M3 | Word ¶43 | «With you are a grill cook…»: el caso lleva DOS grill cooks (Staffing fila 6, ¶85, checklist F4!E9) | «two grill cooks, a fry and prep cook…» |
| m1 | Word ¶49 | Un pedido take-out de $28.00 «is roughly two combos' worth» (2 × $15.99 = $31.98) | «a little less than two combos» |
| m2 | Word ¶113 | «promising "gluten-free" fries: it is not promised» (frase rota) | «calling the fries "gluten-free": never promise it, and give the breaded chicken its own fryer» |
| m3 | `0. Assumptions!C35` (c0063) | La rampa enero-abril «when the calendar is also at its slowest»: el mes más flojo es febrero y marzo-abril no lo son | «takes in the slow weeks of January and February» |
| m4 | checklist F1!E6 (c0624) | Superficies de las variantes (ghost kitchen 450-650 sq ft, burger bar 1,300-1,600 sq ft) sin fuente en la research | Variantes sin cifra («a smaller space with no dining room») |
| m5 | checklist F3!E9 (c0726) | «a plan you will show an inspector does not need it» (frase sin sentido tras quitar la regla española de la madurada) | «This plan has no dry-aged beef program: the burgers use fresh ground chuck from those suppliers» |

**Aceptados sin parche**: Word ¶80 «flat-top at 400-450 °F» (CHK-B, en la research §6.7) y «about 90 seconds on the first side and 60 on
the second» (guía de oficio heredada del ES, marcada «a guide» y separada de la regla de seguridad); ¶95 compra de reventa con resale
certificate («your accountant should confirm»); ¶72 «football season» (calendario de marketing, sin cifra); ¶99 sensibilidad «+$0.75
per lb adds about $0.28 to a double» (research §10, 6 oz × $0.75 ÷ 16, sin merma); la diferencia teórico 25.7 % ↔ plan 34 % se explica
sin puntos inventados (= M3 del ES).

## Sin hallazgo (comprobado)
Word ↔ caché: 195 × $16.50 × 360 = $1,158,300; $382,704 = $257,450 + $125,254; propios $130,000 = 34 %; préstamo $253,000 y cuota
$41,175; neto $87,459 (7.6 %), $113,854, $131,875; EBITDA $167,720 (14.5 %); prime cost 62.7 %; equilibrio 160 / 157; holgura 24 %; DSCR
3.37×; saldo mínimo $136,539 en enero; payback 2.4 / 1.7; escenarios $990,450 (+$23,372, el Word lo llama beneficio) / $1,362,025
(+$229,781); $17.82 con impuesto (16.50 × 1.08); $15,080 = $7.25 × 2,080. Check por canal: (107 × 15 + 36 × 28 + 19 × 32) ÷ 195 =
$16.52. Calculadora: las 19 cifras de `cifras_calculadora.md` citadas tal cual (¶48, ¶65, ¶78, ¶94, ¶114) y sus cuatro pestañas por su
nombre; checklist 80 = 12/15/14/13/13/13 = ¶116. Legal US: 155 °F 17 s y las tres alternativas de 3-401.11(A)(2) (¶104, F3!E10,
calculadora `Instructions!A13`); advisory 3-603.11 solo si cooked to order, con 3-401.11(D) y 3-801.11 (¶105, F3!B12/E12); grinding logs
sin afirmar obligación, FSIS 9 CFR 320.1(b)(4) citado con su alcance (¶104, F3!E7, `Beef & Patty!B42`, `Instructions!A14`); 41 °F y
3-302.11; Type I + UL 300 + NFPA 96 (¶103, F2!E13, F6!E13); TPM sin límite federal; acrilamida sin límite federal y Prop 65 con KFC
2007 de la research (¶105, F3!E13); 9 alérgenos con sésamo, mostaza no major (¶106, F4!E16, `Instructions!A28`); «gluten-free» solo
negado; beer license sin prometerla; W-2, sin servers ni tip credit; nota UK y Australia al final de ¶108 sin cifras de cocción. Cero
español, cero vocabulario de sushi, taco, pollo o pizza (barrido y `RX_BUR_NO`); productos del cierre, todos en la tienda EN.

## Gates finales (VPS, tras la ronda) y sha256 (Mac = VPS)
Ver `F2-NOTAS.md` §5 y el informe de cierre de la sesión: `check_textos --todas` 0 errores · `aplicar_en --idempotencia` 0 dif. · D15
VERDE · G1-G9 · `--autotest` · docx autotest · barrido · resumen · censo `--letter` · no latinos · LIT255.
