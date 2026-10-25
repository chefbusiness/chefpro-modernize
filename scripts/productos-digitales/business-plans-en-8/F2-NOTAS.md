# Pizza Shop Business Plan Kit (EN) — F2 (entregables) · notas

> Sesión Claude Code, 25-oct-2026. **Paso 1a de la F2-EN** (SPEC delta §9, D154): conjunto «piz», clones del Bar EN,
> caso US + D15, E5, tokens, `RX_PIZ_NO`, dry-run sobre el **dry-run ES** y regresión. Implementador único (opus), sin
> subagentes, **sin commits** (los hace el orquestador). Código en el Mac (worktree `wt-pizza-en`); lo que abre xlsx/docx,
> en el **VPS** (`/root/wt-pizza-en`, venv `/root/venv-guias`). Rama `feat/pizza-shop-business-plan-en` (apilada sobre la
> ES). La calculadora (`calculadora_piz.py`, D145) es de OTRO agente en paralelo: no se toca aquí.

## 1. Cómo se montó el conjunto «piz» (libro gemelo del tapas bar ES → molde y diccionario del BAR EN; docx de PAEL)

`BP_CONJUNTO=piz` → `mapas_piz.instalar(M)`, `mapas.DATOS = business-plans-en-8/`, lanzador `bp8.py`. **Único cambio en
código común**: la rama `elif CONJUNTO == 'piz'` de `business-plans-en/mapas.py` (+ el mensaje de error).

**Fuente ES en UN sitio**: `mapas_piz.FUENTE_ES` = `$PIZ_FUENTE_ES` o, sin la variable, `astro-site/public/dl/
plan-negocio-pizzeria` (el ES FINAL). El 1a corre con `PIZ_FUENTE_ES=/root/tmp-pizen/fuente-es/plan-negocio-pizzeria`, una
**copia congelada** del dry-run ES (`/root/tmp-piz-f2/motor/dryrun/plan-negocio-pizzeria/`, que el agente del motor ES sigue
regenerando): plan `aad4cabe…`, checklist `56a304c0…` (ya con «Campana» bien escrita: `B36` = B12…B21, la fila 16 entra
en equipo). `bp8.py verificar` avisa si la fuente deja de casar con el censo.

| Fichero | Qué lleva |
|---|---|
| `mapas_piz.py` | Producto D133 (`dir_es` = `FUENTE_ES`), libros `PIZP`/`PIZC`, pestañas D146 (todas ≤ 31), 80 tareas 12/15/14/13/13/13, parches **E2 solo `G14`**, **E4** (`Staffing!C12`) y **E5** (`G11`: `H11*0.21` → `H11*'0. Supuestos'!$B$40`), versión PIZP 52 / PIZC 11 (E1 en A53 / A12), zona D19 por cabecera (filas 35-47, sin D18), docx de PAEL (131, H1 37…109, `ULTIMO_9` 108, tandas `piz_a`/`piz_b`), `PRESTAMO_SEMILLA` 200,000 (punto fijo), autotest, grupos y **diccionario**: Bar EN por celda (`textos_es` + `GM/GR/GBAR-plan/GBAR-check` + `GR.revision` + `datos_bar.POR_CELDA`) → Bar EN por texto → BP/BP2, con la normalización «comensal(es)» → «cubierto(s)»; `RX_REESCRIBIR` (vocabulario y caso del bar: clasifica propuestas); **9 sha256** del diccionario del Bar en `SHA_BAR` |
| `datos_piz.py` | FIJOS (D139 filas 7-24, D140 A2/A10/A11/A25-A34 y los 7 puestos, títulos, D19, fase 2), POR_CELDA (8: `3-Year P&L!H4` y `F11` (E5 + nota de Texas reescrita), `0. Assumptions!A62`/`C62`/`C63` (D141), `12-Month Cash Flow!O5`/`A34` (D144), `Staffing!A29`), `REGLA_UNIDADES` (masa en gramos, D145), `cifras_prohibidas()` (D149) + `RX_PIZ_NO`, 110 tokens (los del motor con «Comensales…» + 18 partidas propias + `lena_ano`, `plataforma_pct`, `comision_pct`…), `DOCX_FIJOS` (índices de PAEL), 61 `DOCX_NOTAS` por ranura (sección + FORMA del Bar EN; §9 = 102-108 con los temas de D147, la 108 con la nota UK), pistas (caso D137, inversión D139, 13 filas D19 de D142, 26 por texto de D146), glosario research §9, caso US (`VALORES_EN`, 110 celdas) y `CALIBRACION_D15` (3) |
| `bp8.py` | Lanzador (copia de `bp3.py`) + `derivar_formulas`, `verificar`, `calculadora`, `barrido`, `calibracion` |
| `derivar_formulas_piz.py` + `formulas_piz_manual.py` → `formulas_piz.json` | 17 fórmulas con texto: **11 derivadas** de su gemela (Bar EN primero, luego FT/CAF y REST/PAN) y **6 manuales** (C9, C50, D27, D37, F13, `Break-Even!A28`); 0 pendientes |
| `calibracion_piz.py` | D15 de D137 sobre el informe de `aplicar_en --json`: holgura ≥ 15 %, DSCR ≥ 1.25, saldo > 0, cobertura ≥ 98 %, **neto a régimen (año 3) ≤ 12 %** y los 5 umbrales D142 en verde los 3 años; dice la palanca si falla |
| `barrido_piz.py` | Barrido independiente (`--dir`, `--parcial`: en el 1a, las piezas aún en ES cuentan como pendientes) contra `RX_PIZ_NO`, cifras prohibidas, español y no latinos |
| `inventario_delta.py` · `resumen_entregables.py` | Clones del Bar para el 1c (re-medición frente al tapas bar ES y al Bar EN; el docx, si existe) y para el paso 4 |
| `docx_es_piz.json` | **Marcador «pendiente»** (`meta.pendiente`): el Word ES no existe; lo sustituye `bp8.py extraer_docx` en el 1c |
| `BRIEF-TRADUCTORES.md` | Las 4 tandas, con el glosario de research §9 pegado entero (§1) |

**Grupos** (`textos_es.json` del dry-run, 867 cadenas):

| Grupo | Cadenas | Palabras ES | Qué es | Va a |
|---|---|---|---|---|
| GM | 361 | 3.623 | Mismo ES que el Bar EN en la misma celda (o GM del Bar por texto) con EN limpio | nadie: `textos_en/GM.json` escrito |
| GR | 27 | 319 | EN del Bar de otra celda, de BP/BP2 o casado tras «comensal» → «cubierto» | `textos_en/GR.json` escrito; revisión en (a) |
| **GPIZ-plan** | 139 | 3.560 | 87 de texto libre + **52 celdas D19** (13 filas × 4, sin propuesta) | tanda 1 (a) |
| **GPIZ-check** | 219 | 3.092 | Las 80 tareas y sus cabeceras (casi todo texto nuevo) | tanda 1 (b) |
| GX | 121 | 1.141 | Pestañas, CLAVES, FIJOS (94), POR_CELDA (8), versión, pie, docProps | nadie |

## 2. No regresión (VPS, con la rama `piz` en `mapas.py`; `/tmp/regresion-piz.sh`, no versionado)

Por conjunto: `mapas` (0 errores) + `aplicar_en --dry-run` + `ensamblar_docx --salida` en `/root/tmp-pizen/regresion/` y
**sha256 CANÓNICO** (miembros del zip sin las fechas de `core.xml`, `/tmp/canon_piz.py`) frente a `dl/`:

| Conjunto | `mapas` | Ficheros regenerados = publicados (canónico) |
|---|---|---|
| FT/CAF | 0 errores | 6/6 IGUAL (2 docx + 4 xlsx) |
| REST/PAN (`bp2`) | 0 errores | 6/6 IGUAL |
| BAR (`bp3`) | 0 errores | 3/3 IGUAL |
| CAT (`bp4`) · MBAR (`bp5`) · BBQ (`bp6`) · PAEL (`bp7`) | 0 errores | 3/3 IGUAL cada uno |

**20/20 ficheros IGUAL**; G8 VERDE en los 9 docx. `git status` del VPS: solo `mapas.py` modificado + `business-plans-en-8/`
nuevos (y `dl/pizza-shop-business-plan/pizza-dough-food-cost-calculator.xlsx`, del agente de la calculadora).

## 3. Caso US, dry-run y calibración D15 (`bp8.py aplicar_en --dry-run --parcial --idempotencia --salida /root/tmp-pizen/dry`)

Research §8 / SPEC D137 tal cual (vuelta 0): préstamo de punto fijo **$200,000** (semilla 192,400 → 200,000 → 200,000: los
imprevistos por fórmula son $9,250 y no $8,300, y hay fila de suplencias), holgura **15.01 %** (justa) y **neto año 1
4.7 %** (ámbar en D142, `E55` 5 %). **Vuelta 1 (única)**, 1.ª palanca de D137 en su opción «B5 $36» (la de «B30
+$10,000» solo sube el neto ≈ 0.1 punto y no saca el ámbar):

- **PIZP 0. Supuestos!B5** = 36 (ticket $35 → $36: sigue dentro de la derivación de research §8, Margherita $18 y
  especialidades $20-24).
- **PIZP Escenarios!B6** = 33.5 y **PIZP Escenarios!D6** = 38.5: los tickets de los escenarios siguen al base con la lógica
  de D137 (∓$2.50); los covers (54 / 70) y los días (295 / 305), tal cual.

Resultado (caché del dry-run, `/root/tmp-pizen/dry/cifras_caso.json`, `calibracion_piz.py` **VERDE**):
- Ventas **$669,600** / $709,776 / $738,167 (62 covers × $36.00 × 300; $38.88 con sales tax) · 1.2 seat turns.
- CAPEX **$242,550** (18 partidas $217,300 + fianza 2 meses + 2 meses de renta previa + imprevistos $9,250) + fondo de
  maniobra $86,724 = **$329,274** · propios $130,000 (39 %) + préstamo **$200,000** al 10 % a 10 años (cuota $32,549).
- Margen bruto **63.5 %** · COGS 26.0 % · personal **32.8 %** (8 personas = 4.72 FTE, cobertura 99 %) · prime cost 58.8 % ·
  alquiler 7.2 % · EBITDA $98,299 (**14.7 %**) · neto **$39,275 (5.9 %)** / $55,600 (7.8 %) / $66,407 (**9.0 %** a régimen,
  ≤ 12 %).
- Equilibrio **55** covers/día contable · **53** de caja → holgura **18 %** · **DSCR mín 2.62×** · saldo mínimo **$92,610**
  (mes 1) · payback del proyecto > 3 años (2.5 sobre el CAPEX) · seguros $7,500 · leña $5,500.
- Pesimista (54 · $33.50 · 295) **$533,655**, resultado −$33,958 y caja estimada **$66,149** (no se agota; por debajo del
  equilibrio de 55 covers) · optimista (70 · $38.50 · 305) $821,975 y +$149,125.
- Los 5 umbrales D142 (62 / 28 / 36 / 10 / 5 %) en verde los 3 años.

## 4. Gates del paso 1a (VPS, sobre el dry-run)

| Comprobación | Resultado |
|---|---|
| `bp8.py mapas` (autotest + cruce con el censo + `verificar`) | **0 errores** (16 pestañas, 9 claves, 94 fijos, 17 fórmulas EN, 110 valores, 110 tokens) · verificar OK: zona D19 52 celdas en GPIZ-plan sin propuesta, 9 sha256 del Bar OK; 7 avisos (5 FIJOS del motor sin uso, 1 pista sobre GM, docx pendiente) |
| `aplicar_en --dry-run --parcial --idempotencia` | préstamo $200,000 en 1 vuelta · idempotencia **0 diferencias** · inject_cache 741 / 12 fórmulas, **0 fallos de pycel** · D15 sin fallos |
| `bp8.py calibracion` | **VERDE** (holgura 18.3 %, DSCR 2.62, saldo $92,610, cobertura 99.1 %, neto año 3 9.0 %, D142 verde) |
| `gates_en --parcial --solo G1,G3,G4,G5,G6,G7` | **G1** VERDE (741 fórmulas · 80 tareas [12, 15, 14, 13, 13, 13]) · **G3** VERDE (16 hojas Letter) · **G4 ROJO (80)**: defecto de la FUENTE ES (§5.1) · **G5** VERDE (8 rangos de CF) · **G6** VERDE (caché = ES recalculado, 0 diferencias) · **G7** VERDE (110 valores, 3 calibraciones citadas) |
| G4 con la DV del checklist corregida (prueba en una copia, `✓,☐,N/A`) | **VERDE** (235 valores bajo DV) |
| `bp8.py barrido --parcial` (piezas ya en EN: GM, GR, GX, FIJOS, POR_CELDA, fórmulas) | 1.272 piezas · **0 fallos** (RX_PIZ_NO, cifras ES / Bar / FT / REST, español, no latinos); 377 piezas aún en ES = pendientes |
| `check_textos --tanda GPIZ-plan` sobre una salida con defectos inyectados | caza los 11: «66 covers», «19.50», «tapas», «IVA», «97/2010» sin contexto, «$27» del Bar, «386,100» del ES, «Authentic Neapolitan», «33%» de cargas, «cocktail», «2 kg»; deja pasar «Verace Pizza Napoletana (AVPN)» |
| 2.ª pasada (`aplicar_en --dry-run --parcial` en `/root/tmp-pizen/dry2`) | sha256 canónico **IGUAL** en los 2 xlsx; `cifras_caso.json` igual salvo `generado` |

**G2, G8 y G9 no aplican aún**: G2 necesita las tandas (con `--parcial` daría rojo por el español pendiente; el barrido
de arriba cubre lo ya en EN), G8 el Word ES y G9 los ficheros en `dl/` (antes, el alta de `pizza-shop-business-plan` en
`PRODUCTOS_LETTER` de `censo-entregables.py` y en `EXCLUIDOS` de `postprocess-transversal.py`, D148: **pendiente**, no es
código común de este paso).

Ficheros de prueba (solo en el VPS): `/root/tmp-pizen/dry/pizza-shop-business-plan/pizza-shop-financial-projections.xlsx`
(`bc450709…`), `…/pizza-shop-startup-checklist.xlsx` (`3bc583e2…`), `/root/tmp-pizen/dry/cifras_caso.json`, informe
`/root/tmp-pizen/dry.json`. sha256 Mac = VPS: `censo_es.json` `f179ad8a…`, `textos_es.json` `6dfe0e83…`,
`formulas_piz.json` `286b3675…`, `textos_en/GM.json` `6bdadb12…`, `textos_en/GR.json` `c63f4309…`.

## 5. Defectos del ES y decisiones fuera de la SPEC

1. **Defecto ES (para el orquestador del ES, ANTES de cerrar)**: el checklist ES trae la DV `"✓,—,N/A"` y las 80 celdas OK
   con `☐` (que no es de la lista) → G4 ROJO ×80 en el EN, que lo hereda. **Sistémico del motor nuevo**: también en los ES
   LIVE de heladería, finca de eventos y bodas, paellero y parrillero (tapas bar, FT, cafetería, panadería y coctelería
   traen `"✓,☐,N/A"`). Arreglo: DV `"✓,☐,N/A"` (o celdas `—` y el texto de Instrucciones a juego). No se parchea en el EN
   (el EN duplica el ES revisado; `—` no pasa por CLAVES).
2. **Calibración** (§3): `B5` $36 en vez de `B30` +$10,000 (las dos son la 1.ª palanca de D137; solo `B5` saca el neto del
   ámbar) y los tickets de los escenarios a $33.50 / $38.50 (∓$2.50 de D137 sobre el nuevo base).
3. **Clasificación del diccionario**: GM solo con el mismo ES en la misma celda del Bar (o cadena GM del Bar por texto) y EN
   sin `RX_REESCRIBIR`; lo casado tras normalizar «comensal» → «cubierto» va a GR (riesgo 5 de D155); una propuesta con
   vocabulario o caso de bar iría a los traductores con propuesta (en este ES: ninguna).
4. **POR_CELDA directos** en vez de traductores (8 celdas de D141/D144 y la nota de Staffing sin barra de cócteles). La nota
   de Texas de `F11` (D141 pedía la del Bar D57) se reescribe: la mixed beverage tax de Texas es de los locales con permiso
   de mixed beverage; para beer & wine la nota dice «some states tax alcohol differently» con ese ejemplo, sin el 8.25 % /
   6.7 %, que no aplica a un permiso de beer & wine.
5. **Cifras ES prohibidas**: `cifras_caso_es.json` del ES cuando exista (manda); hasta entonces, los importes ≥ 10.000 de los
   tokens ES del censo (28 importes del dry-run, incl. 386.100 y 159.000) + «66 covers» y «19.50» leídos del censo (se
   recalculan solos en el 1c) + las frases fijas de D149; Bar EN (sus importes + «95 covers», «$27», «360 days»), FT y REST.
6. **Fórmulas manuales**: `C50` sin la cifra del caso ES («51 comensales de sala»: «about three quarters of the covers eat
   in», que no envejece si se calibra `B4`); `F13` sin los tipos de IVA de los alimentos (distribuidor + calculadora).
7. Notas del docx por ranura con los índices de PAEL (61) y la FORMA del Bar EN por sección (no por párrafo: el Bar tiene 133
   párrafos y otra rejilla).

## 6. Paso 1c — comando exacto (ES FINAL) y siguientes

Requisitos: el ES cerrado en `astro-site/public/dl/plan-negocio-pizzeria/` (plan, checklist, **Word**, calculadora) y
`scripts/productos-digitales/plan-pizzeria/cifras_caso_es.json`, con la rama ES pusheada y traída a la EN.

```bash
# VPS — re-extracción sobre el ES FINAL (sin PIZ_FUENTE_ES: la fuente vuelve a dl/plan-negocio-pizzeria)
ssh vps
cd /root/wt-pizza-en && git pull --ff-only          # (o merge de la rama ES cerrada)
cd scripts/productos-digitales/business-plans-en-8 && PY=/root/venv-guias/bin/python && unset PIZ_FUENTE_ES
$PY inventario_delta.py > /tmp/piz-inv.txt && $PY bp8.py extraer_textos > /tmp/piz-ext.txt && \
$PY bp8.py extraer_docx > /tmp/piz-ed.txt && $PY bp8.py derivar_formulas && $PY bp8.py mapas > /tmp/piz-mapas.txt && \
$PY bp8.py preparar_tandas && rm -rf /root/tmp-pizen/dry && \
$PY bp8.py aplicar_en --dry-run --parcial --idempotencia --salida /root/tmp-pizen/dry --json /root/tmp-pizen/dry.json && \
$PY bp8.py calibracion /root/tmp-pizen/dry.json && \
$PY bp8.py gates_en --dir /root/tmp-pizen/dry --parcial --solo G1,G3,G4,G5,G6,G7 && \
$PY bp8.py barrido --dir /root/tmp-pizen/dry/pizza-shop-business-plan --parcial
# vuelta al Mac (solo JSON; sin tocar los .py ni la calculadora del otro agente)
rsync -a --exclude '*.py' --exclude '*.md' --exclude '__pycache__' \
  vps:/root/wt-pizza-en/scripts/productos-digitales/business-plans-en-8/ <worktree Mac>/scripts/productos-digitales/business-plans-en-8/
```

Si el 1c rompe algo: un rótulo ES que cambió rompe su token (`extraer_textos` aborta con el rótulo) o deja un FIJO sin uso
(`verificar` lo avisa) → ajustar `datos_piz.py` (FIJOS / TOKENS_PROPIOS / CELDA_PISTAS por fila); `extraer_docx` exige 131
párrafos con los H1 de §1 (si el Word ES difiere, `mapas_piz.DOCX_*`); localizar las ranuras del nombre protegido con
`grep -nE 'ETG|STG|napoletana|pliego|97/2010|2022/2313|2024/1143|AVPN' docx_es_piz.json` (D11 del ES: van en §2 y §9).
Si la calibración D15 deja de pasar con el ES final, `calibracion_piz.py` dice la palanca (máx. 3 vueltas, en
`CALIBRACION_D15` y aquí).

Después (orquestador): **tanda 1** (a) GPIZ-plan + `GR.revision.json` ‖ (b) GPIZ-check → `bp8.py check_textos --todas` (Mac)
→ `bp8.py preparar_tandas` (aplica la revisión de GR) → **tanda 2** piz_a ‖ piz_b → paso 3-4 en el VPS:

```bash
$PY bp8.py aplicar_en --idempotencia --json /tmp/piz-real.json       # 2 xlsx en dl/pizza-shop-business-plan/ + cifras_caso.json
$PY bp8.py ensamblar_docx --plan piz
$PY bp8.py calculadora --autotest                                     # (la del otro agente)
$PY bp8.py gates_en && $PY bp8.py gates_en --autotest && $PY bp8.py ensamblar_docx --autotest --dir /tmp/piz-docx-at
$PY bp8.py barrido && $PY resumen_entregables.py && /tmp/regresion-piz.sh
```
