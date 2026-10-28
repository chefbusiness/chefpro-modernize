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
