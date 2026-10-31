# Sushi Restaurant Business Plan Kit (EN) — F2 (entregables) · notas
> Sesión Claude Code, 31-oct-2026, lead F2 (opus; decisiones delegadas). Fuente: `../plan-sushi/F1-camino.md` §6-§7 + US §n.
> Rama `feat/sushi-restaurant-business-plan-en` (apilada sobre la ES `51060183`); xlsx/docx en el VPS (`/root/wt-sushi-en`,
> `/root/tmp-sus-en/`). Mac: solo lectura, edición, git y `py_compile` (regla térmica); traductores y calculadora (sonnet)
> validan por ssh en el VPS.

## 1. Conjunto «sus» (libro ES = semilla de la taquería LIVE con la rotación ENCENDIDA → rejilla del Taco EN, sin desplazar Break-Even)
Cambio común: `elif CONJUNTO == 'sus'` en `business-plans-en/mapas.py` + alta G9 (`censo-entregables.py` `PRODUCTOS_LETTER`,
`postprocess-transversal.py` `EXCLUIDOS`). FUENTE ES fija (`SHA_ES` `9d6c2fdc…` · `db87cd9e…` · `ac6a4994…` = `dl/plan-negocio-sushi-bar/`
de `51060183`, Mac = VPS), sin paso 1c. Medido el 31-oct: ES sushi = rejilla ES taquería salvo las mismas 4 fórmulas de texto
(C50, D27, D37, F13).

| Fichero | Qué lleva |
|---|---|
| `mapas_sus.py` | Producto §6, `SUSP`/`SUSC`, pestañas (F2 «Phase 2 - Hood & Permits», F3 «Phase 3 - Raw Fish & Health»), 80 tareas 12/15/14/13/13/13, parches E2 (G14) / E4 (Staffing!C12) / E5 (G11), versión A51/A11, D19 de 12 filas, docx 131 (`sus_a`/`sus_b`), diccionario en cadena (Taco EN por celda → por texto → Rotisserie EN por texto → Pizza EN → Bakery → Bar → BP), `SHA_TAQ` + `SHA_POL` + `SHA_PIZ` (30 OK, re-medidos tras #186), SIN la regla «—» → ☐ (el ES ya trae «✓,☐,N/A») |
| `datos_sus.py` | FIJOS (inversión 18, P&L, 9 fijos, 7 puestos, títulos, fases 2/3), 7 POR_CELDA, caso US (127 valores), 111 tokens, notas del docx (61; §9 = 102-108, UK en 108), pistas (D19, Staffing J, Supuestos C), glosario US §9, `cifras_prohibidas()` + `RX_SUS_NO` |
| `bp14.py` · `derivar_formulas_sus.py` · `formulas_sus_manual.py` | Lanzador · 17 fórmulas EN: 13 derivadas del Taco EN + 4 manuales (C50, D27, D37, F13; ≤ 255 car.). `derivar` FUNDE los literales troceados del ES (`parche_xml_xlsx.fundir_literales`: el ES LIVE trae D32 partido desde el 30-oct) |
| `calculadora_sus.py` (sonnet, `SPEC-calculadora.md`) | `sushi-fish-rice-costing-calculator.xlsx`: `Fish Yield` · `Sushi Rice` · `Costing` · `Instructions`; lb/oz/fl oz con constantes grises; autotest 585 VERDE |
| `calibracion_sus` · `barrido_sus` · `resumen_entregables` · `volcar_en` · `anotar_tandas_docx` · `check_revision` · `canon` · `regresion_sus.sh` | Clones del Rotisserie EN (palancas de US §8; regresión de los 13 conjuntos publicados) |
| `BRIEF-TRADUCTORES.md` | 4 tandas (una a la vez), bloque legal US del pescado crudo y el arroz, encaje de las 80 tareas, validación por ssh (§5) |

## 2. Decisiones que se apartan de §6 o lo concretan
1. **Diccionario: Taco EN primero** (misma celda, misma rejilla) y luego **Rotisserie EN por texto** exacto (sin alias
   «pedido»: el sushi ES cuenta comensales como la taquería). `RX_REESCRIBIR` sin «servers», «seat turns», «griddle» ni
   «Mondays» (valen en el sushi) y con el vocabulario del pollo y del counter service.
2. **Inversión 18 = 18** con la clase de la fila ES: signage en la obra (8 = $75,000); «electrical, HVAC, plumbing & grease»
   ($26,000) partido en 10 ($11,000) y 11 ($15,000, con las líneas de gas); freezer de −4 °F en la fila del congelador ES (14);
   fryer, range & griddle en la cocina caliente (15); la 16 (campana ES) = walk-in $12,800 (pista «OJO»; la campana va en la 9).
   Imprevistos por fórmula **$13,300** (10 % de 7-11, base con arquitecto y rótulo, = Taco/Rotisserie; US §8 decía $12,800).
3. **Fijos 9 = 9** ($28,000): las renovaciones de permisos (CFPM, HACCP plan / variance) con la formación (fila 34 ES de PRL).
4. **Plantilla** en la fila ES de su jornada: encargado ES (1.0) → sushi chef; camarero de cenas ES (0.75) → servers, host &
   to-go (4 × 0.75); refuerzo ES (0.5) → sushi chef part-time (0.6); suplencias → dish & prep. El dueño es GM; el head sushi
   chef (itamae) es contratado (US §8). 10 personas, **8.6 FTE**, $29,108/mes, $384,226/año (33.2 %); cobertura 7.5 h × 4.5 +
   3 h × 2 → **128.4 %**. A29 (POR_CELDA): servers con propinas aparte, sin tip credit modelado.
5. **`Break-Even!B25` = 3** (US §8 = ES): el caso da 2.9 por plaza con take-out y marketplace; el equilibrio de caja ≈ 2.3 cabe.
   POR_CELDA (7): H4, F11, A62, C62, C63, O5 (enero con los pesos US), Staffing A29. Umbrales P&L 55 / 33 / 36 / 10 / 5 %.
6. Gate: «115 covers», «95 covers» y «$36» NO se vetan (son del caso sushi; coinciden con Taco, Bar y Pizza EN); sí «130
   covers», «360 days», «308 days», «$17.50». Vetados además «sushiman», «combinado», «vitrina», «surimi», «sushi-grade» sin
   negar, «−20 °C … 24 h» fuera de la nota UK, «counter service» fuera de la variante poke, «open 7 days».
7. Cierre del Word: Food Cost Kit Pro · HACCP Food Safety Kit Pro · Restaurant Checklists Kit Pro · Food Cost + Menu Engineering
   Guide (no hay guía de restaurante japonés ni checklists de sushi en la tienda EN).
8. Nombres de fichero (US §9): `sushi-restaurant-{business-plan.docx,financial-projections.xlsx,startup-checklist.xlsx}` ·
   `sushi-fish-rice-costing-calculator.xlsx` («Sushi Fish, Rice & Costing Calculator»).

## 3. Caso US y D15 (dry-run `/root/tmp-sus-en/dry`, = paso real) — **VERDE en la vuelta 0, sin palancas**
Préstamo de punto fijo **$256,000** (semilla 248,000 → 255,000 → 256,000 → 256,000) · ventas **$1,158,625** / $1,228,142 /
$1,277,268 (115 × $32.50 × 310) · CAPEX $255,100 (18 partidas $223,800 + imprevistos $13,300 + fianza $9,000 + renta previa
$9,000) + fondo $130,056 = **$385,156** · propios $130,000 · cuota $41,663 · margen tras variables 58.5 % · COGS 30.8 % ·
personal 33.2 % · alquiler 4.7 % · EBITDA $182,591 · **neto 8.5 % / 10.3 % / 11.4 %** · equilibrio 93 / 92 covers · **holgura
26.3 %** · **DSCR mín 3.59×** · saldo mín $140,937 (Mes 1) · payback 2.3 · pesimista $883,738, −$29,140 · optimista $1,453,140,
+$303,676 · 5 umbrales en verde los 3 años. `CALIBRACION_D15` vacía.
Calculadora (caché): coste por lb útil $11.28 (salmón entero) · $23.92 (filete) · $25.48 (saku de atún); el entero compensa
mientras limpiarlo cueste < $12.65/lb útil · 2.41 lb de shari por lb de arroz · 51 nigiri por lb · 14.9 lb de arroz al día ·
food cost: nigiri de salmón 23.4 %, California 12.2 %, spicy tuna 39.2 %, platter de 24 24.8 %, ponderado 24.2 % (el plan
usa 32 %: el puente, en `0. Assumptions!C13` y en la fila 38 de D19) · margen del platter de 24: $31.60 en sala, $24.83 por
marketplace.

## 4. Tandas (sonnet, UNA a la vez; validación por ssh en el VPS, `BRIEF-TRADUCTORES.md` §5)
| Tanda | Cadenas · palabras ES | Resultado |
|---|---|---|
| (a) GSUS-plan + revisión GR | 117 (69 + 48 de D19) · 3,723 + 39 GR | OK; 1 corrección de GR (c0253) |
| (b) GSUS-check + revisión GRC | 123 · 3,165 + 97 GRC | OK; 2 correcciones de GRC (c0803, c0642: el sake con la licencia de vino) |
| (c)+(d) sus_a + sus_b (un solo agente, en serie) | 29 · 3,207 + 32 · 4,197 | OK; Word de 131 párrafos, 7,583 palabras |
Inyección en `check_textos` (18 defectos: authentic, 79 covers, 20.00, sushiman, combinado, sushi-grade, gluten-free, IVA,
−20 °C 24 h, surimi, taco, rotisserie, 300 days, kg, open 7 days, Spain, €, comensal): **caza los 18**.
Las cifras de la calculadora (no son tokens) son citables en el Word desde `cifras_calculadora.md` (añadido a
`M.FUENTES_CIFRAS` en `mapas_sus.instalar`): sin él, el check rechazaba $11.28, 23 %… y el traductor las quitaba.

## 5. Paso real (VPS) y lo que cazaron los gates
`bp14.py mapas` → `aplicar_en --idempotencia --json /tmp/sus-real.json` → `calibracion` → `ensamblar_docx --plan sus` →
`calculadora --salida $D` → `gates_en` (+ `--autotest`) → `ensamblar_docx --autotest --dir /tmp/sus-docx-at` → `barrido` →
`resumen_entregables.py` → `../censo-entregables.py --fail --letter --only sushi-restaurant-business-plan` + `../gate-no-latinos.py
--only …` → `../parche_xml_xlsx.py --check $D/*.xlsx` → `volcar_en.py --salida /tmp/sus_rev` → revisión opus → 2.ª pasada `canon.py`.
Primer paso real: **G2/barrido ROJOS** por (1) `0. Assumptions!C9` (derivada del Taco EN, literal de 262 car.): `inject_cache`
lo troceaba a 255 y «VAT.» quedaba en un trozo sin «UK» → **C9 manual troceado antes de «In the UK»** (= Rotisserie EN); (2)
falso positivo del regex del ticket ES «20.00» con el precio «7.50 · 20.00 · 23.00 $/lb» de la calculadora → **regex
restringido** a check/ticket o «€» (se arregla el regex, no el texto: lección del Rotisserie); (3) el autotest A del
ensamblador (7/8) marcaba «sus» (clave del plan, funcional ES) en su párrafo sintético → frase sintética retirada del detector
solo en este conjunto. `derivar_formulas` dejaba D32 pendiente porque el ES LIVE trae el literal troceado → funde antes.

## 6. Regresión (código común: solo la rama `elif 'sus'` y dos altas de lista)
`regresion_sus.sh` (13 conjuntos): **22/22 IGUAL** (docx y calculadoras, sha256 canónico), `mapas` rc 0 en todos. Los
`aplicar_en --dry-run` de los xlsx de los 13 conjuntos **abortan antes de construir** por una deriva PREEXISTENTE: #186
reescribió en los ES LIVE la nota «Holgura mínima» (`0. Supuestos!C67`) sin re-extraer el `textos_es.json` de cada conjunto EN
(«textos_es.json dice 'Cuánto puedes caer…' y el ES trae 'Cuánto deben superar…'»). No la causa este cambio (una rama elif no
toca otros conjuntos) y no se arregla aquí: **deuda para la próxima tanda de arreglos** (re-extraer y re-pasar los 13, o fijar
la fuente ES de cada uno a su sha de publicación).

## 7. Revisión final y cierre (detalle en `REVISION-FINAL.md`)
Una ronda opus: **0 B · 2 M · 14 m, los 16 arreglados en fuente** (M1 ticket por canal del marketplace = M1 del ES; M2 el atún
exento sin papel, la declaración escrita es para la acuicultura). Gates finales TODO VERDE, 2.ª pasada `canon.py` 4/4 IGUAL,
sha256 Mac = VPS.
**Para la F3 (landing, nombres exactos)**: `sushi-restaurant-business-plan.docx` («Sushi Restaurant Business Plan (10
Sections)») · `sushi-restaurant-financial-projections.xlsx` (9 hojas) · `sushi-restaurant-startup-checklist.xlsx` (80 tareas,
pestañas «Phase 1 - Business Setup» · «Phase 2 - Hood & Permits» · «Phase 3 - Raw Fish & Health» · «Phase 4 - Staff &
Allergens» · «Phase 5 - Menu, Brand, Delivery» · «Phase 6 - Opening & 90 Days») · `sushi-fish-rice-costing-calculator.xlsx`
(«Sushi Fish, Rice & Costing Calculator»: `Fish Yield` · `Sushi Rice` · `Costing` · `Instructions`) + bonus común de
equivalencias. Cifras para la FAQ: las de §3 (`cifras_caso.json`, `cifras_calculadora.md`); la landing NO promete «sushi-grade»,
ni pH legal, ni la licencia; replica M1 (marketplace ≈ el mismo pedido con la carta un 12-15 % más cara) y M2 (atún exento).
