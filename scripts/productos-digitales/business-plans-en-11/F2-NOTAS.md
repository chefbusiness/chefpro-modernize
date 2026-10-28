# Coffee Cart Business Plan Kit (EN) — F2 (entregables) · notas

> Sesión Claude Code, 28-oct-2026. **Paso 1a** (conjunto «cof», extracción, diccionario en cadena Paella → Catering, caso US
> + D15, 4 tandas + la del contrato preparadas solo con lo que cambia, regresión). Implementador único (opus), sin
> subagentes. Código en el Mac (worktree `wt-coffeecart`, rama `feat/coffee-cart-business-plan`, apilada sobre la del ES en
> `d8984ffd`); lo que abre xlsx/docx, en el **VPS** (`/root/wt-coffeecart`, venv `/root/venv-guias`, scratch `/root/tmp-cof/`).
> El ES (`/root/wt-cafemovil`, `/root/tmp-caf-f2/`) solo se LEYÓ. Sin commits (los hace el orquestador).

## 1. Cómo se montó el conjunto «cof» (fuente ES del circuito = FOOD TRUCK ES; diccionario = PAELLA → CATERING; código = PAELLA)

`BP_CONJUNTO=cof` → `mapas_cof.instalar(M)`, `mapas.DATOS = business-plans-en-11/`, lanzador `bp11.py`. **Único cambio en
código común**: la rama `elif CONJUNTO == 'cof'` de `business-plans-en/mapas.py` (+ el mensaje de error). El reuso por celda
va **en cadena** (D221): el EN de la Paella LIVE en esa celda y, si no hay, el del catering publicado. `bp11.py verificar`
comprueba los **18 sha256** (10 de la paella en `mapas_cof.SHA_PAEL`, fijados sobre `d8984ffd`, + los 8 del catering): 0
derivas.

| Fichero | Qué lleva |
|---|---|
| `mapas_cof.py` | Producto D216-D218, libros `COFP`/`COFC`, pestaña F2 «Phase 2 - Permits & Commissary» (30 car.), 68 tareas 11/13/12/10/12/10, los 7 parches con el Break-Even en **±$1 / +$2**, zonas D18/D19/TAREA, docx 131 ranuras, `RX_REESCRIBIR` = vocabulario y caso de la paella + catering/BBQ residual + «marketplace», **87 `FORZAR_TRADUCTORES`** (los 51 de la paella + 36 celdas con pista de café: C25/C30/C63, F16/F51/F56, E23, `Instructions!A12` y las filas D18 39/41/42/43/44/49/50), `D19_CON_PROPUESTA` = 65, 67, columna C mecánica («Paella chef» → «Lead barista», «Event staff» → «Event baristas»), `PRESTAMO_SEMILLA` = 71,000 |
| `datos_cof.py` | FIJOS (motor de eventos, títulos, D19, dos líneas, canal de festivales), POR_CELDA (≈ 75: Supuestos, inversión 7-23 y A31, P&L, 4 puestos W-2, **O5, O20 y A34 con Month 1 = marzo**, notas del motor con la holgura corregida), `REGLA_UNIDADES`, cifras prohibidas (ES de la cafetería leído de su `cifras_caso_es.json` si `COF_CIFRAS_ES`, Paella, BBQ, catering, bar móvil, FT) + `RX_COF_NO`, tokens (alias de eventos, 11 partidas propias `inv_carro` … `inv_energia`, `festivales_pct`), 61 `DOCX_NOTAS` (nivel + pista + PROPUESTA EN DE LA PAELLA + ES 1.0 de la ranura cuando exista), pistas (caso, D18, 14 filas D19, **68 tareas `TAREAS_COF`**), glosario §9, caso US, `CALIBRACION_D15` (vacía), FORMULAS_EN |
| `bp11.py` | Lanzador + `verificar` (272 celdas en GCF-check ∪ GLP-check + 18 sha256) + `fuente`, `barrido`, `calibracion`, `contrato`, `check_contrato` (y `calculadora`, que avisa: paso 1b) |
| `fuente_cof.py` → `fuente_es_cof.json` | Del ES en F2 (`COF_FUENTE_ES`, `COF_DL_ES`): checklist (80 tareas), contrato (91 párrafos en el worktree ES), tabla de escalado (`datos_escalado.py`), calculadora borrador (`/root/tmp-caf-f2/calc_pub/`, 4 hojas); **pendiente: docx ES por ranura (0/61)** |
| `calibracion_cof.py` · `barrido_cof.py` (`--dir`) · `check_contrato.py` · `contrato_cof.py` · `regresion_cof.sh` · `canon.py` | D15 sobre el informe · barrido de los 5 entregables · tanda del contrato (1 parte) · contrato en Letter sobre el molde ES · regresión de los 10 conjuntos |

**Grupos** (`textos_es.json`, 959 cadenas): GM **310** (3.365 pal.) · GRP-plan **59** (revisión) · GLP-check **186** (183 celdas de
tarea tal cual) · **GCF-plan 148** (3.557 pal. ES; 121 pistas) · **GCF-check 89** (543 pal.; 66 pistas) · GX 167. Docx
(`docx_es_cof.json`): 131 párrafos, 0 multi-run, 61 ranuras → **cof_a 29 / 2.954 pal. · cof_b 32 / 3.765**. Contrato:
`tandas/contrato.entrada.json` = 92 párrafos ES, 3.047 palabras (el del repo, `d8984ffd`).

Checklist por tarea (sobre las filas FINALES de la paella, tras su revisión): **22 L · 42 A · 4 N** (nuevas: máquinas y
molinos, siropes y leches vegetales, segunda estación, agua de la espresso). Por celda solo cambian 89 de 272.

## 2. No regresión (VPS, `regresion_cof.sh`, 1 min)

`mapas` 0 errores en los 10 conjuntos · `aplicar_en --dry-run` + `ensamblar_docx` (+ calculadora de la pizza, calculadora
y contrato de la finca EN) → **39/39 ficheros IGUAL** (sha256 canónico), 0 DISTINTO, todos rc 0 · `bp11.py mapas` 0 errores ·
`git status` del VPS: solo la rama `cof` de `mapas.py` y `business-plans-en-11/`.

## 3. Caso US, dry-run y calibración D15 (`bp11.py aplicar_en --dry-run --parcial --salida /root/tmp-cof/dry --json …`)

Research §8 con las bases de las fórmulas (D222): **D15 en VERDE sin tocar nada** (`calibracion_cof.py`). Préstamo de punto
fijo **$71,000** (semilla 68,000 → 71,000 → 71,000; research ≈ $68,700): supera el Microloan de $50,000 → **SBA 7(a)**.
`CALIBRACION_D15` vacía (G7: 0 calibraciones citadas).

- Ventas **$203,490** / $223,839 / $237,269 (170 × 95 × $12.60; **$1,197 por evento**; 16,150 invitados; años 2-3: 187 y 198 eventos).
- CAPEX **$71,290** (67,100 + fianza 700 + 1 mes previo 700 + contingencia 10 % × 27,900 = 2,790) + fondo de maniobra
  $29,000 = **$100,290** · propios $30,000 (30 %) + préstamo **$71,000** al 10 % a 7 años (cuota $14,584).
- Margen bruto **75.3 %** · mercancía 13.9 % · personal **36.6 %** ($74,501) · commissary 4.1 % · EBITDA $44,327 (**21.8 %**) ·
  intereses $7,100 · neto **$20,162 (9.9 %)** / 13.4 % / **15.1 %**.
- Equilibrio **141 eventos** contable / **138** de caja → holgura **24.1 %** (caída absorbible 19 %) · **DSCR mín 2.58×** ·
  saldo mínimo **$17,705 en el mes 7** (septiembre: tras julio-agosto y el primer pago trimestral del sales tax) · payback 2.3
  años · 5 personas, 1.54 FTE, cobertura 162 %.
- Pesimista (128 · $11.34 · 86) **$124,831**, resultado −$32,348 y **caja −$487: se agota (por poco)** → el docx §8 [99] lo
  dice · optimista (212 · $13.86 · 105) $308,524 y +$105,973 (≤ `B51` 350).
- Umbrales D225 (≥ 72 % · ≤ 20 % · ≤ 40 % · ≤ 6 % · ≥ 5 %) verdes los 3 años.

`gates_en --dir /root/tmp-cof/dry --parcial --solo G1,G3,G4,G5,G6,G7`: **TODO VERDE** (722 fórmulas; 68 tareas; 16 hojas
Letter; 202 valores bajo DV; caché = referencia ES recalculada, 0 diferencias; 113 valores del caso). `ensamblar_docx
--autotest`: **8/8**. `check_textos` GM · GRP-plan · GLP-check: **OK**. Barrido de lo reutilizado (GM + GRP + GLP) contra
`cifras_prohibidas` y español: **0**; el barrido del dry-run deja 242 fallos = las 237 celdas aún en ES (las de los redactores).

## 4. Decisiones y desviaciones (frente a research §8 y al hermano)

1. **Filas de inversión remapeadas a las bases de las fórmulas** (research numeraba 7-20 a su manera y ponía la contingencia
   «sobre 7, 8, 11, 13, 20»): vehículo 7 / 8 / 11 / 12 / 15 = carro (+ depósitos, bomba y nevera) $13,400 · barra portátil (+ nevera)
   $5,400 · remolque $6,500 · wrap, enganche y rampas $1,500 · plan review $1,100; equipo 9 / 10 / 16 / 17 / 20 = máquinas $15,700
   · molinos $4,800 · TPV $1,000 · batch brewer, cold brew, smallwares y estanterías $3,300 · generador y cables $5,000; sin
   amortizar 13 / 14 / 18 / 19. Total $67,100 (= research); contingencia $2,790 (research $2,980).
2. **Canal B16/B17 = festivales y farmers markets guest-pay con cuota del organizador (5 % × 15 %)**, como el ES (D5: ferias por
   el canal delivery), no los marketplaces de research §8 (20 % × 5 %): duplicar el ES; GigSalad / Thumbtack / The Bash / Zola
   van al marketing fijo (research ya los ponía ahí).
3. **4.ª fila de Staffing**: research daba 3 puestos; el molde exige 4 → los event baristas (3 × 0.08) se parten en 2 × 0.08 +
   «On-call barista / driver» 1 × 0.08: misma masa ($5,644/mes).
4. **Fijos $21,000 en 10 filas** (research dejaba la 10.ª libre): teléfono e internet en la fila de residuos (32), formación y
   catas partidas en 34 / 35 ($400 + $400). Suministros `B26` $100 = combustible del generador, agua y hielo (= FT: el
   generador va en suministros).
5. **Pestaña F2 «Phase 2 - Permits & Commissary»** (la de research tenía 36 caracteres).
6. **Notas O20 y A34 con Month 1 = marzo** (deuda de la pizza; la paella LIVE dice «April, July, October, January»), y C67 / E24
   con la holgura bien definida (deuda del motor, ya corregida en la paella).
7. **Neto año 3 15.1 %**: dentro del tope de cordura de la finca (16 %); no se calibra (D15 no lo pide).
8. **Fuera de mi paso**: `calculadora_cof.py` (paso 1b, D227: duplicar las 4 hojas de la calculadora ES cuando pase su
   revisión) y la re-extracción con el ES final (paso 1c, §6). Alta de `coffee-cart-business-plan` en `PRODUCTOS_LETTER` y
   `EXCLUIDOS` antes de G9 (paso 3).

## 5. Comandos para seguir

```bash
# PASO 1c (VPS) — cuando el ES pase su revisión: re-leer su contenido y sus cifras (solo lectura del ES)
cd /root/wt-coffeecart/scripts/productos-digitales/business-plans-en-11 && PY=/root/venv-guias/bin/python
export COF_FUENTE_ES=/root/wt-cafemovil/scripts/productos-digitales/plan-cafeteria-movil COF_DL_ES=/root/tmp-caf-f2 \
       COF_CIFRAS_ES=/root/tmp-caf-f2/cifras_caso_es.json       # o, con el ES ya en git, sin variables
$PY bp11.py fuente && $PY bp11.py mapas > /root/tmp-cof/mapas.txt && $PY bp11.py preparar_tandas   # notas del docx con el ES
$PY bp11.py check_contrato --preparar                            # si el contrato ES cambió
# PASO 2 — redactores Sonnet (Mac, máx. 2 a la vez; BRIEF-TRADUCTORES.md §0-§1 + su tanda), reanudados con SendMessage
#   tanda 1: (a) GCF-plan + revisión GRP-plan ‖ (b) GCF-check + (e) contrato · tanda 2: (c) cof_a ‖ (d) cof_b
python3 bp11.py check_textos --tanda GCF-plan        # | GCF-check | cof_a | cof_b · check_contrato --todas
# PASO 3 — VPS: aplicar, ensamblar, contrato, gates
$PY bp11.py aplicar_en --idempotencia --json /root/tmp-cof/real.json && $PY bp11.py calibracion /root/tmp-cof/real.json
$PY bp11.py ensamblar_docx --plan cof && $PY bp11.py contrato --salida ../../../astro-site/public/dl/coffee-cart-business-plan --pdf
$PY bp11.py gates_en && $PY bp11.py gates_en --autotest && $PY bp11.py barrido && bash regresion_cof.sh
```

VPS: `/dev/null` roto (redirigir a `/tmp` o `/root/tmp-cof/`); `git checkout -- .` y borrar generados sin seguimiento antes de
cada `git pull`.

## 6. Bloqueado por el ES (paso 1c)

- **Docx ES por ranura** (`textos/caf_es_{a,b}.json`): las 61 notas de `cof_a`/`cof_b` llevan pista + propuesta de la paella;
  el párrafo ES de la ranura entra al re-correr `bp11.py fuente/mapas/preparar_tandas` (sin cambiar ids: solo notas).
- **Cifras ES finales** para `CIFRAS_ES` (hoy, el borrador del implementador ES: 108,810 € de ventas, 44,416 € de CAPEX,
  44,500 € de préstamo, 130 × 135 × 6,20 €) y frases («130 events», «135 guests», «6,20 €»).
- **Calculadora** (D227, paso 1b) y, si cambia, el **contrato** ES (la tanda se preparó con el de `d8984ffd`, 92 párrafos).

## 7. Paso 1b + tanda del contrato re-preparada (28-oct, tarde; sesión Claude Code)

Sobre `57362d63` (ES final: calculadora `d3174a8d`, contrato `9273efd3`, `plan-cafeteria-movil/REVISION-FINAL.md`).

- **Tanda (e)** `tandas/contrato.entrada.json` rehecha con el contrato ES FINAL (92 párrafos, 3.074 palabras; sha256 `977badd3…`).
  `check_contrato.py`: cobro y cancelación = los de la calculadora EN (privado: retainer 30 % + 70 % 14 días antes, cortes 60 / 30 /
  14 → 10 / 30 / 60 / 100 %, el último menos lo ahorrado; empresa: 30 % + 70 % net 30, cortes 30 / 15 / 7; festival: en el acto +
  minimum sales guarantee liquidada en 7 días) y traslado de la revisión ES (B1 horas extra = mismo servicio; M6 «IVA incluido» NO
  se copia: «plus applicable sales tax»; m27 → `contrato_cof.py` añade la línea de versión EN al final).
- **`calculadora_cof.py` + `escalado_cof.py`** (fuente única EN de la tabla de escalado): las 4 hojas de la ES («Cost per Drink» ·
  «Pricing Calculator» · «3 Example Quotes» · «Instructions»), misma lógica y mismo autotest. Adaptación US (decisiones de este
  paso, dentro de D227): café y cacao en g con precio por lb, leches y chai en fl oz con precio por galón, sirope por botella (columna
  D «recipe units per price unit», verde); precio de carta sin sales tax (celda para quien lo incluye); carta US (cold brew en lugar
  del café con leche; vasos de 8 / 12 / 16 oz con tapa y funda; avena 25 % de la leche); salida estándar 120 V × 20 A = 2.4 kW frente a
  la máquina de 220 V / 3.4 kW (NEMA 6-20) → aviso, amperios a 220 V y generador en kW (5.5 kW = el del caso); margen objetivo
  **65 / 60 / 20 %** (Flashquotes: precio 2-3 × coste; el ES usa 55 / 50 / 20); **dos entradas nuevas, norma US**: radio gratis del
  travel fee (20 millas) y **minimum sales guarantee** del organizador (la venta del festival es la mayor de las dos); sin referencias
  internas (lección M3 del ES: el autotest veta «research», «SPEC», «§» y el nombre del módulo) y rótulo del tramo 4 de m23.
- **Medido (VPS)**: 425 fórmulas, 0 fallos de pycel · **autotest 1.122 comprobaciones VERDE** (pycel + caché en las 4 hojas, 3 casos
  propios con `set_value`, tabla de escalado, selector de cliente, radio gratis, garantía, aviso eléctrico, tramos sin huecos día a
  día, Letter + pie + protección, 0 verdes bloqueadas, 0 números tecleados, 0 español / no latinos / cifras prohibidas / anclas) ·
  `censo-entregables --only coffee-cart-business-plan --letter --fail` 0 defectos · `gate-no-latinos` 0 · `barrido_cof --dir` 0 ·
  2.ª generación con sha canónico IGUAL. Mezcla: $1.034 de ingredientes + $0.252 de vaso = **$1.286 por bebida**, carta media $5.88,
  COGS 21.9 %. Ejemplos: boda 130 inv. **$15.00** (= línea de la mezcla) · empresa 90 **$13.00** (+8 % de $12) · farmers market 150
  bebidas: precio mínimo $5.00 frente a $6.50, resultado $384, equilibrio 60 bebidas. Escalado (2 h, tarde): 50 / 100 / 200 / 300
  invitados → 1 / 2 / 3 / 4 baristas, 1 / 1 / 2 / 2 máquinas, 2.2 / 4.1 / 7.8 / 11.6 lb de café, 2 / 4 / 8 / 12 gal de leche.
  `dl/coffee-cart-business-plan/coffee-cart-pricing-calculator.xlsx` sha256 `fa31f453…` (Mac = VPS).
- «cortado» sale del veto de `RX_COF_NO` (es bebida de la carta US) y del brief.

## 8. Paso 1c (28-oct, tarde; sesión Claude Code) — sobre `7d3bf444` (Word ES final `1b43d5fb`, 7.235 palabras)

- `fuente_es_cof.json` rehecho sin variables (todo desde el repo): checklist 80 tareas · **Word ES 61/61 ranuras** · contrato 92 ·
  escalado · calculadora ES final · pendientes: ninguno. `extraer_docx` (VERDE) → las notas de **cof_a (19 de 29) y cof_b (21 de
  32)** llevan el párrafo ES 1.0 FINAL de su ranura (las 21 «casi literales» no lo llevan, como en la paella), con el aviso de que
  si la ranura ES trata otro subtema manda la pista: el **§9 EN conserva su mapa** (commissary [102], permisos [103], electricidad
  y bomberos [104]…), que es lo que promete la landing («Section 9»). `preparar_tandas`: GCF-plan y GCF-check **sin cambios**; cof_a
  / cof_b solo cambian en las notas; `GRP-plan.json` incorpora las 2 correcciones de `GRP-plan.revision.json` (mecanismo normal).
- **Cifras vetadas = ES final** (`plan-cafeteria-movil/cifras_caso_es.json`, el del repo; ya no hace falta `COF_CIFRAS_ES`): 46
  importes ≥ 10.000 € (108.810, 44.416, 60.061, 44.500…; fuera los del propio caso EN, los de la research y los redondos ≤ 50.000)
  + «130 events», «135 guests», «6,20 €». Comprobado: «$25,000», «$50,000», «$13,400», «128 events» y «Cortado» pasan.
- `bp11.py mapas` 0 errores (18 sha256 OK) · calculadora `--autotest` VERDE sobre el fichero de HEAD (`fa31f453…`) · Mac = VPS.
- **§6 queda resuelto**: Word ES, cifras finales, calculadora (§7) y contrato (§7) ya están; las tandas (c) cof_a ‖ (d) cof_b
  pueden arrancar.

## 9. Paso 3 — montaje y gates de los 5 entregables (28-oct, noche; sesión Claude Code) — sobre `f5f244e1`

Todos los textos EN en git (GCF-plan, GRP-plan con su revisión, GCF-check, `contrato_en.json`, `docx_en_cof_{a,b}.json`). VPS
`/root/wt-coffeecart` llevado a la cabeza de la rama (limpio). Alta de `coffee-cart-business-plan` en `PRODUCTOS_LETTER`
(`censo-entregables.py`) y `EXCLUIDOS` (`postprocess-transversal.py`) para G9 (una línea en cada uno; ningún otro código común).

```bash
cd /root/wt-coffeecart/scripts/productos-digitales/business-plans-en-11 && PY=/root/venv-guias/bin/python
D=/root/wt-coffeecart/astro-site/public/dl/coffee-cart-business-plan
$PY bp11.py check_textos --todas && $PY bp11.py check_contrato --todas && $PY bp11.py verificar     # JSON
$PY bp11.py aplicar_en --idempotencia --json /root/tmp-cof/real.json && $PY bp11.py calibracion /root/tmp-cof/real.json
$PY bp11.py ensamblar_docx --plan cof && $PY bp11.py contrato --salida $D --pdf && $PY bp11.py calculadora
$PY bp11.py gates_en && $PY bp11.py gates_en --autotest && $PY bp11.py ensamblar_docx --autotest --dir /root/tmp-cof/docx-at
$PY bp11.py barrido                                       # → entregables_cof.json
cd .. && $PY censo-entregables.py --only coffee-cart-business-plan --fail && $PY gate-no-latinos.py --only coffee-cart-business-plan
cd /root/wt-coffeecart && bash scripts/productos-digitales/business-plans-en-11/regresion_cof.sh /root/wt-coffeecart
# 2.ª pasada: aplicar_en --dry-run --salida /root/tmp-cof/p2 + ensamblar_docx/calculadora/contrato --salida p2/… y canon.py
```

| Gate | Resultado |
|---|---|
| `check_textos --todas` · `check_contrato --todas` · `verificar` | GM, GRP-plan (2 correcciones), GLP-check, GCF-plan (148), GCF-check (89), cof_a (29 · 39 tokens), cof_b (32 · 96 tokens) **OK** · contrato 99 párrafos, 3.212 palabras **OK** · 18 sha256 OK |
| `aplicar_en --idempotencia` | 2.ª construcción 0 diferencias · inject_cache 722 (666) + 12 · 0 fallos de pycel |
| `calibracion` (D15) | **VERDE**: préstamo $71,000 · ventas $203,490 · DSCR 2.58 · saldo mín $17,705 (mes 7) · cobertura 162 % · holgura 24.1 % · neto 9.9 / 13.4 / 15.1 % · exceso 0.7 % · umbrales D225 verdes |
| `ensamblar_docx` · `contrato --pdf` · `calculadora` | Word **G8 VERDE** (131 párrafos, 10 H1, 8.025 palabras) · contrato **VERDE** (100 párrafos con la línea de versión EN al final, 3.227 palabras, Letter, **8 páginas**) · calculadora autotest **1.122 VERDE** |
| `gates_en` | **G1-G9 TODO VERDE** (722 fórmulas · 68 tareas 11/13/12/10/12/10 · 1.285 piezas de texto · 16 hojas Letter · 202 valores bajo DV · 0 diferencias de caché · 113 valores del caso · docx validado · censo 0 · no latinos 0) · `--autotest` **20/20** · docx `--autotest` **8/8** |
| `barrido_cof` | 5 ficheros · 2.092 piezas · **0 fallos** (RX_COF_NO, cifras prohibidas, español, no latinos) |
| `censo-entregables --only … --fail` · `gate-no-latinos --only …` | 5 ficheros (3 xlsx, 2 docx): **0 defectos** · 0 no latinos |
| `paginas-gate.py --only coffee-cart-business-plan` | no aplica: solo lee las fichas ES (`src/data/productos`); la ficha EN no promete páginas (solo «10 sections», «68 tasks») |
| Regresión de los 10 conjuntos | **39/39 IGUAL**, 0 DISTINTO · `bp11.py mapas` 0 errores |
| 2.ª pasada (sha canónico) | **IGUAL** en los 5 |

**Entregables** (`astro-site/public/dl/coffee-cart-business-plan/`, nombres de D218, Mac = VPS):

| Fichero | sha256 |
|---|---|
| `coffee-cart-business-plan.docx` | `ba647bbe117f0ec7…` |
| `coffee-cart-financial-projections.xlsx` | `92e1b56afb0669fa…` |
| `coffee-cart-pricing-calculator.xlsx` | `fa31f453551662b5…` (= el de git: la regeneración da sha canónico igual y se dejó el versionado) |
| `coffee-cart-startup-checklist.xlsx` | `b7235f5105eb782c…` |
| `coffee-catering-service-agreement-template.docx` | `d821fe8a7dc0d26c…` |

`cifras_caso.json` solo cambia el sello `generado`; `entregables_cof.json` nuevo (barrido). VPS: el resto, sin cambios en git.

**Dudas de los redactores para la revisión D232 (no se han tocado):**
1. **cof_a [41]**: cifras de cart-king frente a la tabla de benchmarks (D19 fila 61: «$5,000-25,000» como Kit estimate, «$24,000»
   típico y «$49,000» premium de cart-king.com): comprobar que el Word y la tabla digan lo mismo.
2. **cof_b [104]**: los ejemplos del fire code (NFPA 96 «≥ 12 ft», New Jersey) vienen de resúmenes: confirmar que van como ejemplo
   con «ask your fire marshal».
3. **cof_b [102]**: la salvedad de California (Health & Safety Code §114295, leída solo en resumen): ¿basta el «usually yes … ask your
   county in writing»?
4. **cof_b [98]**: «September, with Month 1 as March» va escrito a mano junto a `{{mes_saldo_minimo}}`: si alguien cambia la
   estacionalidad o el Mes 1, el mes deja de ser septiembre (el token sí cambiaría).

## 10. Review fixes (REVISION-FINAL `a46e24b8`, una ronda; 28-oct, noche; sesión Claude Code)

Por texto en las fuentes JSON (+ `datos_cof.py` y `calculadora_cof.py`); las reutilizadas, por `textos_en/{GM,GLP-check,GRP-plan}.revision.json`
(las aplica `preparar_tandas`). La ficha `.ts` es de otro agente (no tocada).

| # | Aplicado | Dónde |
|---|---|---|
| B1 (lado entregable) | ✅ comparación en prosa cart / trailer / truck en Word **[64]** (§4, barreras de entrada): carro completo $16,600-49,000 (cart-king.com), trailer ≈ $15,000 de construcción + $10,000 de equipo y truck de ≈ $20,000 usado a $80,000 custom (greenjoecoffeeschool.com, precios de 2019), los tres son mobile food units (permiso + plan review + commissary; el truck, además, registro y commercial auto), interior / exterior, y por qué el caso elige carro + barra portátil en remolque cerrado. Sin tabla | `docx_en_cof_a.json` «64» (aviso de longitud 1.96 × la ranura ES: solo aviso) |
| M1 | ✅ fuera los volúmenes de DataForSEO: [39] abre con la demanda y Flashquotes (25,860 reservas, 578 operadores, ≈ 100 invitados, mediana $1,040); [53] «Google Keyword Planner» para medir lo local; [70] sin la cifra | cof_a 39, 53, 70 |
| M2 | ✅ un solo juego cart-king: **carro solo $4,000-25,000 (básico nuevo a custom premium) · equipo completo de un carro ≈ $16,600-49,000 · típico $24,000**; la máquina ≈ $8,500 sigue como Kit estimate | Word [41] y [64] · `Instructions!B61/C61/D61` |
| M3 | ✅ conciliado: GrindKit 20-30 % es sobre ingreso de bebida y aquí los paquetes pagan también a los baristas; el 50-70 % de Flashquotes es después del personal del evento y el {{margen_bruto_pct}} del plan, antes («once the event baristas are paid it falls back into that range»). El «≈ 63 %» del revisor no entra: `check_textos` exige token o fuente para un %, y no hay token | cof_b 96 |
| M4 | ✅ «the sales tax payment due that month (the model settles in June, September and December)» y «(September in the example, which opens in March)» | cof_b 98 |
| M5 | ✅ ejemplo citado como checklist de Lenexa (Kansas, basada en NFPA 96) y «some states, such as New Jersey, may require…»; checklist E9 igual y **sin «(summary)»**; B9 sin «and any propane» | cof_b 104 · `GCF-check` c0734, c0737 |
| M6 | ✅ «keep an eye on year 1, when the loan payment is already running and the cushion over cash break-even is thinnest ({{holgura_caja_pct}}, rising in years 2 and 3)» | cof_b 117 |
| M7 | ✅ «SCALING RULES (kit estimates from US ratios)»; fuera la frase de la tabla del Word en el pie; `Instructions` 5: «Its rules use the same assumptions as the business plan: drinks per guest by service length, 50-65 drinks per barista an hour and 18 g per double shot» | `calculadora_cof.py` |
| m1 | ✅ «(the FDA Food Code cold-holding limit)» en Word [65] [81] [103] [112], checklist F1 E14 · F3 E6 · E14 y calculadora (pie de «Cost per Drink» e «Instructions») | |
| m2 | ✅ `0. Assumptions!C37` y `Instructions!D45`: «…or keep it as a reserve for your personal tax, as the Word plan does» | GM / GRP revisión |
| m3 · m4 · m5 | ✅ [102] sin «As we read it» · «labeled gluten-free» (Word [105], contrato, checklist F3 E10, F4 E14) · «including staff and extras, and in some states travel» (Word [106], contrato, `C9`, `C39`, checklist F1 E10, calculadora) | |
| m6 | ✅ «a lean … (get quotes)» en Word [107] y nota D67; `B27` sin cambios ($3,800, para no mover el caso) | |
| m7 · m8 · m9 | ✅ Sweet Carolinas incluye la avena y cobra $50 por otra leche · fuera «which usually means poorly paid labor» · «the cart order and the insurance» | cof_a 63, 49 · cof_b 114 |
| m10 | ✅ [56] con los invitados de cada tipo (90 / 130 / 45 / 150 bebidas) | cof_a 56 |
| m11 · m12 | ✅ nota del ejemplo 3: «without the guarantee, below 60 drinks you would lose money: the $800 guarantee covers that risk» · ejemplo renombrado **«Community festival, guest-pay»**; Word [40] y [56]: la garantía, solo en algunos festivales. Contrato [93]: ya era condicional («If the Organizer promises…») | calculadora · cof_a 40, 56 |
| m13 · m14 · m15 | ✅ «Many health departments» · «retainer(s)» (F1 E5, E9, `C58`) · `O16` sin «alcohol to go», `A40` «Sales tax rate on alcohol (not used: no alcohol in this plan)», `C40` «Not used…» | GLP / GM revisión, `POR_CELDA`/FIJOS |
| m16 | ❌ no aplicado: la caché de `TEXT(…,"#,##0")` la emula `inject_cache` (código común de toda la familia); Excel lo recalcula al abrir (`fullCalcOnLoad`). Deuda del motor | |
| m21 · m22 · m23 | ✅ «Privacy contact: [name and email]» · «Dated [mm/dd/yyyy].» · «jointly and severally liable» · «represents that it has the authority to sign» · reembolso del Organizer sin doble cuenta · **cláusula «Travel fee»** nueva en la 2 ($[amount] por milla ida y vuelta más allá de [20] millas) | `contrato_en.json` (101 párrafos con la línea de versión) |
| m24 | ✅ portada [16] «US edition with UK notes · Version 2.2 · October 2026» | `datos_cof.py` docx_fijos |
| m17-m20, M8 y el lado ficha de B1 / M2 | — de la ficha (otro agente); cifras para alinear: las de M2 y B1 de esta tabla, ejemplo 3 = «Community festival» | |

**Regenerado y gates (VPS, mismos comandos de §9)**: textos GM, GRP-plan, GLP-check, GCF-plan, GCF-check, cof_a, cof_b **OK** · contrato **OK**
(101 párrafos, 3,259 palabras, 8 páginas) · `aplicar_en --idempotencia` 0 diferencias · **D15 VERDE** (cifras del caso sin cambios) · Word
**G8 VERDE** · calculadora **1,122 VERDE** · **G1-G9 TODO VERDE** · `gates_en --autotest` 20/20 · docx 8/8 · barrido 5 ficheros, 2,093 piezas,
**0** · censo 0 · no latinos 0 · 2.ª pasada **IGUAL** en los 5 · regresión **39/39 IGUAL**.

| Fichero (`dl/coffee-cart-business-plan/`, Mac = VPS) | sha256 |
|---|---|
| `coffee-cart-business-plan.docx` | `a2fd104a4380…` |
| `coffee-cart-financial-projections.xlsx` | `2afefa6797a3…` |
| `coffee-cart-pricing-calculator.xlsx` | `22f292cbb4a7…` |
| `coffee-cart-startup-checklist.xlsx` | `23c741da8255…` |
| `coffee-catering-service-agreement-template.docx` | `644fdd2dfdee…` |
