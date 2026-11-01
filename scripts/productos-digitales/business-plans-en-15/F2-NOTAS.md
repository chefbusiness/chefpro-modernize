# Burger Restaurant Business Plan Kit (EN) — F2 (entregables) · notas
> Sesión Claude Code, 31-oct-2026, lead F2 (opus; decisiones delegadas). Fuente: `../plan-hamburgueseria/F1-camino.md` §6-§7 + US §n.
> Rama `feat/burger-restaurant-business-plan-en` (apilada sobre la ES; la ES cerrada `e883ebaa` fusionada en `4d346461`); xlsx/docx
> en el VPS (`/root/wt-burger-en`, `/root/tmp-bur-en/`). Mac: solo lectura, edición, git y `py_compile`; los subagentes sonnet
> (calculadora, tandas a+b, tandas c+d; uno a la vez) validan por ssh en el VPS.

## 1. Conjunto «bur» (libro ES = semilla del Sushi Bar LIVE con la rotación ENCENDIDA → rejilla del Sushi EN, sin desplazar Break-Even)
Cambio común (= `07e7513a`): `elif CONJUNTO == 'bur'` en `business-plans-en/mapas.py` + altas de lista (`resync_es.py` `range(2, 16)`
y los 5 bloques de sha del `bur`, `censo-entregables.py` `PRODUCTOS_LETTER`, `postprocess-transversal.py` `EXCLUIDOS`). FUENTE ES fija
(`SHA_ES` `ad0fad74…` · `1d061df4…` · `ec69d114…` = `dl/plan-negocio-hamburgueseria/` de `e883ebaa`, Mac = VPS), sin paso 1c.
Medido el 31-oct: ES hamburguesería = rejilla ES sushi bar (mismas 9 + 7 pestañas, mismas celdas) salvo 4 fórmulas de texto (C50,
D27, D37, F13: las mismas 4 que el sushi frente a la taquería), 139 textos del plan y 172 del checklist.

| Fichero | Qué lleva |
|---|---|
| `mapas_bur.py` | Producto §6, `BURP`/`BURC`, pestañas (F2 «Phase 2 - Hood & Permits», F3 «Phase 3 - Beef & Health»), 80 tareas 12/15/14/13/13/13, parches E2/E4/E5, versión A51/A11, D19 de 12 filas, docx 131 (`bur_a`/`bur_b`), diccionario en cadena (Sushi EN por celda → Taco EN por texto → Rotisserie EN → Sushi EN por texto → Pizza EN → Bakery → Bar → BP), `SHA_SUS` + `SHA_TAQ` + `SHA_POL` + `SHA_PIZ` (42 OK), `RX_REESCRIBIR` con el vocabulario del sushi y «servers» (sin «counter service» ni «kiosk», que valen aquí) |
| `datos_bur.py` | FIJOS (inversión 18, P&L, 9 fijos, 7 puestos, títulos, fases 2/3), 7 POR_CELDA, caso US (127 valores), 111 tokens, notas del docx (61; §9 = 102-108, UK y Australia sin cifras de cocción en 108), pistas (D19, Staffing J, Supuestos C), glosario US §9, `cifras_prohibidas()` + `RX_BUR_NO` |
| `bp15.py` · `derivar_formulas_bur.py` · `formulas_bur_manual.py` | Lanzador · 17 fórmulas EN: 13 derivadas (gemela Sushi EN primero; una gemela con vocabulario de otro negocio en el literal se salta) + 4 manuales (C50 troceado, D27, D37, F13; ≤ 255) |
| `calculadora_bur.py` (sonnet, `SPEC-calculadora.md`) | `smash-burger-patty-costing-calculator.xlsx` («Smash Burger Patty, Fries & Costing Calculator»): `Beef & Patty` · `Fries & Oil` · `Costing` (14 productos) · `Instructions`; oz/lb con constantes grises «16 oz per lb» y «60 minutes per hour»; autotest 1,271 VERDE |
| `calibracion_bur` · `barrido_bur` · `resumen_entregables` · `volcar_en` · `anotar_tandas_docx` · `check_revision` · `canon` · `regresion_bur.sh` | Clones del Sushi EN (palancas de US §8; regresión de los 14 conjuntos publicados) |
| `BRIEF-TRADUCTORES.md` · `cifras_calculadora.md` | 4 tandas, bloque legal US de la carne picada y la fritura, encaje de las 80 tareas, validación por ssh · caché de la calculadora citable en el Word (en `M.FUENTES_CIFRAS`) |

## 2. Decisiones que se apartan de §6 o lo concretan
1. **Inversión 18 = 18 por la clase de la fila ES** ($228,300, F1-camino §6): el hood partido como en el ES (duct + makeup air en la
   obra, fila 9, $8,000; Type I + UL 300 en el equipo, fila 14, $12,000). Imprevistos por fórmula **$11,150** (10 % de 7-11).
2. **Fijos 9 = 9** ($26,000) fila a fila; hood cleaning trimestral (NFPA 96, mucha grasa) en mantenimiento; CFPM y food handler
   cards con la formación (fila 34).
3. **Plantilla** en la fila ES de su jornada: titular → Owner / GM; plancha → Grill cooks (2 × 1.0); montaje y freidora → Fry &
   prep cook; mostrador → Shift lead; auxiliar (0.75) → Counter crew (3 × 0.75); refuerzo (0.5) → Weekend crew (3 × 0.4);
   suplencias → Dish & prep (0.6). **12 personas, 9.05 FTE**, $365,416/año (31.5 %), cobertura 11 h × 3.5 + 2.5 h × 2 → **106 %**.
   A29 (POR_CELDA): counter service, sin servers ni tip credit; el tip jar es del equipo.
4. **`Break-Even!B25` = 5** (F1-camino §6): el caso da 4.4 por plaza con take-out y marketplace y el equilibrio de caja ≈ 3.6 cabe.
   Umbrales P&L: **margen tras variables 52 %** (variables 44.5 %; el 55 % del sushi quedaba en el filo), 33 / 36 / 10 / 5 %.
5. Gate: «195 covers», «360 days», «$17.50» (optimista) y «180 covers» NO se vetan (son del caso burger); sí «115 covers», «310 days»,
   «$32.50», «40 seats», «1,800 sq ft» (Sushi EN), «95 comensales» con lookbehind, «1.7 covers», «fry-top», «value meal», «smashed
   burger», «rolls» (salvo potato rolls), «platter», «servers» (salvo la variante burger bar o negado), «rare / medium-rare» sin
   advisory, afirmar grinding logs obligatorios, «closed Mondays», y las temperaturas ES 75 / 70 / 175 / 63 / 2 / −18 °C (las
   conversiones del Food Code entre paréntesis, sí).
6. Cierre del Word: **Burger Joint Checklists Kit Pro** · Food Cost Kit Pro · HACCP Food Safety Kit Pro · Food Cost + Menu
   Engineering Guide (el hermano de tareas sí existe en EN).
7. Calculadora: el queso entra en $ por loncha ($0.14, un solo input en lugar del par €/kg + g del ES); objetivo de food cost 30 %
   (el 34 % del plan es el consumo de toda la carta: puente sin puntos inventados); fries congeladas por defecto.

## 3. Caso US y D15 (dry-run `/root/tmp-bur-en/dry` = paso real) — **VERDE en la vuelta 0, sin palancas**
Préstamo de punto fijo **$253,000** (semilla 247,000 → 253,000 → 253,000) · ventas **$1,158,300** / $1,227,798 / $1,276,910 (195 ×
$16.50 × 360) · CAPEX $257,450 (18 partidas $228,300 + imprevistos $11,150 + fianza $9,000 + renta previa $9,000) + fondo $125,254 =
**$382,704** · propios $130,000 (34 %) · cuota $41,175 · margen tras variables 55.5 % · COGS 31.2 % · personal 31.5 % · alquiler
4.7 % · prime cost 62.7 % · EBITDA $167,720 (14.5 %) · **neto $87,459 = 7.6 %** / 9.3 % / 10.3 % · equilibrio 160 / 157 covers ·
**holgura 24 %** · **DSCR mín 3.37×** · saldo mín $136,539 (Mes 1) · payback 2.4 (1.7 sobre el CAPEX) · rotación 4.4 · pesimista
$990,450 con **+$23,372** (beneficio, no pérdida) · optimista $1,362,025, +$229,781 · 5 umbrales en verde los 3 años.
`CALIBRACION_D15` vacía (ninguna palanca tocada).
Calculadora (caché, `cifras_calculadora.md`): lb útil $5.41 (blend comprado) · $5.15 (chuck entero, sin mano de obra) · picar en
casa compensa solo si cuesta < $0.26/lb útil («Buy the blend ground») · 5.3 bolas de 3 oz por lb (5.2 con la merma) · 58.5 lb de
carne al día · single $2.00 (24 %) · double $3.21 (29 %) · combo 25 % · triple 32.7 % («Watch the cost») · ponderado **25.7 %**
(el plan usa 34 %) · ración de fries congeladas $0.46 (fresca $0.35 sin mano de obra) · aceite ≈ $0.10 por ración y ≈ 320 lb al
mes · margen del combo $12.07 sala · $11.52 take-out · $9.12 marketplace (−24 %).

## 4. Tandas (sonnet, UNA a la vez; validación por ssh en el VPS, `BRIEF-TRADUCTORES.md` §5)
| Tanda | Cadenas · palabras ES | Resultado |
|---|---|---|
| (a) GBUR-plan + revisión GR | 115 (67 + 48 de D19) · 3,691 + 41 GR | OK; 2 correcciones de GR (c0099 19 %; c0375 dish & prep $15.50/h) |
| (b) GBUR-check + revisión GRC | 116 · 3,481 + 105 GRC | OK; 1 corrección de GRC (c0802, techo de marketplace 19 %); «spec» → «data sheet» (el check lo veta) |
| (c)+(d) bur_a + bur_b (un solo agente, en serie) | 29 · 3,371 + 32 · 4,563 | OK 0/0; Word de 131 párrafos, 8,225 palabras |
`preparar_tandas` se vuelve a correr tras las revisiones (aplica `GRC.revision.json` a `GRC.json`; sin ese paso, `check_textos
--todas` da ROJO en GRC).

## 5. Paso real (VPS) y lo que cazaron los gates
`git clean` de las salidas copiadas a mano → `pull` → `bp15.py check_textos --todas` → `aplicar_en --idempotencia --json /tmp/bur-real.json`
(0 diferencias entre construcciones) → `calibracion` → `ensamblar_docx --plan bur` (G8) → `calculadora --salida $D` → `gates_en`
(+ `--autotest`) → `ensamblar_docx --autotest --dir /tmp/bur-docx-at` → `barrido` → `resumen_entregables.py` →
`../censo-entregables.py --fail --letter --only burger-restaurant-business-plan` + `../gate-no-latinos.py --only …` →
`../parche_xml_xlsx.py --check $D/*.xlsx`.
Primer paso completo: **G7 ROJO** (faltaba este `F2-NOTAS.md`, que G7 lee) y **GRC ROJO** (revisión sin aplicar, §4). El resto
verde a la primera: G1-G6, G8, G9, barrido 4 ficheros / 1,746 piezas / 0 fallos, LIT255 VERDE.
Lección de tubería: copiar del VPS al Mac con `tar` por ssh (un `scp vps:…/*` lo expande zsh en local y corta la cadena `&&`);
nunca `git clean` en el VPS antes de haber traído las salidas.

## 6. Regresión (código común: solo la rama `elif 'bur'` y las altas de lista)
`regresion_bur.sh` (14 conjuntos, con el `sus`): **53 IGUAL** por sha256 canónico + **3 IGUAL-SEM** (`comparar_sem.py`: Restaurant,
BBQ Catering y Wedding Venue, los xlsx parcheados por XML en #186: alto de fila), `mapas` rc 0 en los 14. Los `aplicar_en --dry-run`
de los 14 conjuntos corren (la deriva de `textos_es.json` de SUS-US-F2 §6 ya no aparece tras el resync del #191).

## 7. Revisión final y cierre (detalle en `REVISION-FINAL.md`)
Una ronda (opus, el lead): **0 B · 3 M · 5 m, los 8 arreglados en fuente** (solo texto; cifras y valores por defecto intactos).
**Para la F3 (landing, nombres exactos)**: `burger-restaurant-business-plan.docx` («Burger Restaurant Business Plan (10 Sections)», 131
párrafos, ≈ 8,200 palabras) · `burger-restaurant-financial-projections.xlsx` (9 hojas) · `burger-restaurant-startup-checklist.xlsx`
(80 tareas: «Phase 1 - Business Setup» · «Phase 2 - Hood & Permits» · «Phase 3 - Beef & Health» · «Phase 4 - Staff & Allergens» ·
«Phase 5 - Menu, Brand, Delivery» · «Phase 6 - Opening & 90 Days») · `smash-burger-patty-costing-calculator.xlsx` («Smash Burger Patty,
Fries & Costing Calculator»: `Beef & Patty` · `Fries & Oil` · `Costing` · `Instructions`) + bonus común de equivalencias. Cifras para la
FAQ: las de §3 (`cifras_caso.json`, `cifras_calculadora.md`): inversión $382,704 ($228,300 de obra y equipo; el FAQ de US §9 decía
$377K: manda el Excel), neto 7.6 %, equilibrio de caja 157 covers, double $3.21 (29 %), combo $12.07 → $9.12 en marketplace. La
landing replica lo de la revisión: la smash viaja PEOR (la crust se ablanda en ~15 min), todo cocido a 155 °F 17 s, advisory solo
si cooked to order, grinding logs sin afirmar obligación, TPM sin límite federal, Prop 65 solo en California, sin «gluten-free».
