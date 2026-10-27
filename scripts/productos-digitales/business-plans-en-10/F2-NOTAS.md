# Ice Cream Shop Business Plan Kit (EN) — F2 (entregables) · notas

> Sesión Claude Code, 27-oct-2026. **Paso 1a de la F2-EN** (SPEC delta §8, D207): conjunto «ice», clones de la Pizza EN
> (D192), caso US D191 + D15, tokens, `POR_CELDA`, `RX_ICE_NO` y cifras prohibidas (D202), extracción sobre el **ES
> FINAL y LIVE**, `preparar_tandas`, dry-run y regresión. Implementador único (opus), sin subagentes. Código en el Mac
> (worktree `wt-icecream`); lo que abre xlsx/docx, en el **VPS** (`/root/wt-icecream`, venv `/root/venv-guias`,
> temporales en `/root/tmp-icen/` y `/tmp/ice-*`). Rama `feat/ice-cream-shop-business-plan-en`. Decisión de orquestador
> previa: **D190 tal cual** (base pasteurizada comprada a una central con licencia; pasteurizar = variante sin Excel).

## 1. Cómo se montó el conjunto «ice» (libro gemelo de la panadería ES 2.2 → código y molde de la PIZZA EN)

`BP_CONJUNTO=ice` → `mapas_ice.instalar(M)`, `mapas.DATOS = business-plans-en-10/`, lanzador `bp10.py`. **Único cambio en
código común**: la rama `elif CONJUNTO == 'ice'` de `business-plans-en/mapas.py` (+ el mensaje de error). Choque de merge
trivial con la F1 paralela (D156-D185), que añade su `elif` en el mismo sitio.

**Fuente ES en UN sitio**: `mapas_ice.FUENTE_ES` = `astro-site/public/dl/plan-negocio-heladeria` (`$ICE_FUENTE_ES` solo
para pruebas). Es el ES final: plan `a99b1686…`, checklist `d8ec6c6f…`, Word `04739dfe…` (= inv. cabecera; `bp10.py
verificar` falla si cambian: `mapas_ice.SHA_ES`). No hay paso 1c.

| Fichero | Qué lleva |
|---|---|
| `mapas_ice.py` | Producto D186 (`ice-cream-shop-business-plan`), libros `HELP`/`HELC`, pestañas D199 (≤ 31), 80 tareas 12/15/15/12/13/13, **E2 solo `G14`** (sin E3/E4/E5: inv. §2.2 y §2.6), versión HELP 52 / HELC 11 (E1 en A53 / A12), zona D19 por cabecera (35-47), docx de PIZ (131, H1 37…109, `ULTIMO_9` 108, tandas `ice_a`/`ice_b`), `PRESTAMO_SEMILLA` 162,000, autotest, G4 heredado (`CLAVES['—'] = '☐'`) y el **diccionario en cadena sin normalizar** (inv. §6): Pizza EN por celda (checklist casado por POSICIÓN de pestaña) → Pizza EN por texto → Bakery (GPAN/GN con `overrides_` de la misma celda) → Bar → BP (GM → REST → CAF → FT). `RX_REESCRIBIR` (vocabulario de pizza, panadería y bar + caso de la pizza) clasifica las propuestas. **10 sha256** del diccionario de la Pizza EN en `SHA_PIZ` |
| `datos_ice.py` | FIJOS (D193 filas 7-25, D194 A2/A10/A11/A25-A35 y los 6 puestos, títulos, D19, A63), **POR_CELDA (7)**: `Startup Costs!D12` (base comprada; el pasteurizador = variante, D190/D193), `0. Assumptions!C62`/`C63` (sin alcohol), `12-Month Cash Flow!O5`/`A34`/`O20` (Mes 1 = marzo, D195: el c0531 de la pizza decía septiembre), `Staffing!A28` (sin E4 y sin propinas), `REGLA_UNIDADES` (°F, sq ft, gal/qt/pint, lb/gal), `REGLA_BASE` (D190), `cifras_prohibidas()` (D202) + `RX_ICE_NO`, 112 tokens (los del motor con «Clientes» + 19 `inv_*` + `aforo`, `comida_pct`, `bebida_pct`, `delivery_pct`, `comision_pct`, `produccion_horas`, `sabores`, `fijos_anual`, `prime_cost_pct`…), `DOCX_FIJOS` (cierre 127-129 = Ice Cream Shop Checklists Kit Pro · Food Cost Kit Pro · HACCP Food Safety Kit Pro), 61 `DOCX_NOTAS` (sección + FORMA de la Pizza EN; las ranuras que sustituyen bloques ES de D200 y las 7 de §9), pistas (caso D191, inversión D193, 13 filas D19 de D196, 31 por texto de D190/D199), glosario research §9, caso US (`VALORES_EN`, 110 celdas) y `CALIBRACION_D15` (vacía: §3) |
| `bp10.py` | Lanzador (copia de `bp8.py` sin `calculadora`) + `derivar_formulas`, `verificar` (sha256 del ES final y de la Pizza EN), `barrido`, `calibracion` |
| `derivar_formulas_ice.py` + `formulas_ice_manual.py` → `formulas_ice.json` | 16 fórmulas con texto: **12 derivadas** de su gemela (Pizza EN primero, luego REST/PAN, Bar y FT/CAF) y **4 manuales** (C9, D28, D38, F13; cada literal ≤ 255 caracteres, troceado con `"…"&"…"`); 0 pendientes |
| `calibracion_ice.py` · `barrido_ice.py` · `resumen_entregables.py` | D15 de D191 · barrido (`--dir`, `--parcial`) → `barrido_ice.json` · resumen del paso 4 → `entregables_ice.json` |
| `check_revision.py` | Valida `textos_en/GR.revision.json` o `GRC.revision.json` en un temporal propio (fusión + `check_textos --fichero`): los dos traductores no corren `preparar_tandas` |
| `regresion_ice.sh` · `canon.py` | Regresión de los 8 conjuntos (versionada; la de la pizza vivía en `/tmp`) y sha256 canónico |
| `BRIEF-TRADUCTORES.md` | Las 4 tandas, con el glosario de research §9 pegado entero (§1), la tabla de encaje de tareas (§3) y el comando de validación de cada tanda (§5) |

**Grupos** (`textos_es.json` del ES final, 866 cadenas):

| Grupo | Cadenas | Palabras ES | Qué es | Va a |
|---|---|---|---|---|
| GM | 369 | 3,681 | Motor común: mismo ES que una cadena GM de la Pizza EN (348), BP (18) o el Bar (3), EN limpio | nadie: `textos_en/GM.json` escrito |
| GR | 14 | 276 | EN de la Pizza EN (GPIZ-plan / GR), la Bakery (GPAN, 7) o REST (1) en el plan | `textos_en/GR.json` escrito; revisión en (a) |
| **GRC** | 73 | 369 | EN de la Pizza EN (GPIZ-check / GR) en el checklist: plazos, responsables, cabeceras, tareas | `textos_en/GRC.json` escrito; revisión en (b) |
| **GICE-plan** | 131 | 3,089 | 79 de texto libre + **52 celdas D19** (13 filas × 4, sin propuesta) | tanda 1 (a) |
| **GICE-check** | 157 | 2,459 | Las 80 tareas, sus notas y cabeceras + el mensaje de la DV (con propuesta, D199: ☐) | tanda 1 (b) |
| GX | 122 | 997 | Pestañas (15), CLAVES (2) y 105 «regenerar» (FIJOS, POR_CELDA, versión, pie, docProps) | nadie |

**Desdoble GR/GRC frente a la pizza** (decisión fuera de la SPEC): con un solo GR revisado en GICE-plan, 73 de las 87
reutilizadas con revisión serían del checklist y las revisaría el traductor del plan. `GRC` (solo HELC) va a la tanda
GICE-check: cada traductor revisa las de su libro y la carga queda pareja (≈ 3,1 K + 0,3 K palabras frente a ≈ 2,4 K +
0,4 K). Mecanismo genérico (`REVISAR_EN_TANDA`, `escribir_reusadas`): cero código común.

## 2. No regresión (VPS, con la rama `ice` en `mapas.py`; `bash business-plans-en-10/regresion_ice.sh`)

Por conjunto: `mapas` (0 errores) + `aplicar_en --dry-run` + `ensamblar_docx --salida` en `/root/tmp-icen/regresion/` (+ la
calculadora de la pizza) y **sha256 CANÓNICO** (`canon.py`: miembros del zip sin las fechas de `core.xml`) frente a `dl/`:

| Conjunto | `mapas` | Ficheros regenerados = publicados (canónico) |
|---|---|---|
| FT/CAF · REST/PAN (`bp2`) | 0 errores | 6/6 + 6/6 IGUAL |
| BAR (`bp3`) · CAT (`bp4`) · MBAR (`bp5`) · BBQ (`bp6`) · PAEL (`bp7`) | 0 errores | 3/3 IGUAL cada uno |
| PIZ (`bp8`) | 0 errores | 4/4 IGUAL (2 xlsx + docx + calculadora) |

**31/31 ficheros IGUAL** (log `/tmp/ice-regresion.log`); G8 VERDE en los 10 docx; `git status` del VPS limpio.

## 3. Caso US, dry-run y calibración D15 (`bp10.py aplicar_en --dry-run --parcial --idempotencia --salida /root/tmp-icen/dry`)

Research §8 / SPEC D191 tal cual (**vuelta 0, sin palancas**): préstamo de punto fijo **$162,000** (semilla 162,000 →
162,000 en 1 vuelta), holgura **18.3 %** (≥ 15 %), DSCR mín **2.26×**, saldo mínimo **$46,060** (Mes 1 = marzo), cobertura
**105.3 %**, neto año 3 **8.6 %** (≤ 12 %) y los 5 umbrales D196 en verde los 3 años → **`CALIBRACION_D15` vacía**. La
instrucción del orquestador (primero B30 +$10,000; solo si no basta, ticket $7.75) no hace falta: la holgura ya pasa.
Por qué research §8 la daba «justa» (≈ 15.4 %): la medía sobre las ventas (1 − equilibrio / ventas); el libro la mide
sobre el equilibrio de caja (`Break-Even!B24` = clientes previstos / clientes de equilibrio de caja − 1), como en la pizza.

- Ventas **$383,625** / $414,315 / $435,031 (165 customers × $7.50 × 310; $8.10 con sales tax).
- CAPEX **$204,100** (19 partidas $186,000 + fianza 2 meses $5,000 + 2 meses de renta previa $5,000 + imprevistos por
  fórmula $8,100) + fondo de maniobra $52,771 = **$256,871** · propios $95,000 (37 %) + préstamo **$162,000** al 10 % a 10
  años (cuota $26,365).
- Margen tras variables **68.2 %** · COGS 22.3 % · personal **$128,185 (33.4 %)** (6 personas = 3.05 FTE, cobertura 105 %) ·
  prime cost 55.7 % · alquiler 7.8 % · fijos $16,600 · EBITDA $66,747 (**17.4 %**) · amortización $21,767 · intereses
  $16,200 · neto **$21,585 (5.6 %)** / $32,045 (7.7 %) / $37,480 (**8.6 %** a régimen).
- Equilibrio **147** customers/día contable · **140** de caja → holgura **18 %** · DSCR mín **2.26×** · payback > 3 años.
- Pesimista (140 · $7.00 · 300) **$294,000**, resultado −$32,344 y caja estimada **$32,029** (no se agota) · optimista
  (190 · $8.00 · 320) $486,400 y +$98,872.

## 4. Gates del paso 1a (VPS, sobre el dry-run)

| Comprobación | Resultado |
|---|---|
| `bp10.py mapas` (autotest + cruce con el censo + `verificar`) | **0 errores** (16 pestañas, 9 claves, 97 fijos, 16 fórmulas EN, 110 valores, 112 tokens) · verificar OK: zona D19 52 celdas en GICE-plan sin propuesta, 10 sha256 de la Pizza EN OK, ES = sha256 de F1; 6 avisos (FIJOS del motor sin uso) |
| `extraer_docx` | 131 párrafos (110 con texto, 61 traducibles: ice_a 29 / 3,039 palabras · ice_b 32 / 3,780), 10 Heading 1, 0 multi-run · único ERROR = **página A4** del Word ES (igual que la pizza: el ensamblador la pasa a Letter) |
| `aplicar_en --dry-run --parcial --idempotencia` | préstamo $162,000 en 1 vuelta · idempotencia **0 diferencias** · inject_cache 736 + 12 fórmulas, **0 fallos de pycel** · faltan 131 + 169 textos (GICE pendientes: parcial) |
| `bp10.py calibracion` | **VERDE** (holgura 18.3 %, DSCR 2.26, saldo $46,060, cobertura 105.3 %, neto año 3 8.6 %, D196 verde) |
| `gates_en --parcial --solo G1,G3,G4,G5,G6,G7` | G1 VERDE (736 fórmulas · 80 tareas [12, 15, 15, 12, 13, 13]) · G3 VERDE (16 hojas Letter) · **G4 VERDE (233 valores bajo DV**, la DV `✓,☐,N/A` del arreglo heredado) · G5 VERDE (8 rangos CF) · G6 VERDE (caché = ES recalculado, 0 diferencias; D15 2.26 / $46,060 / 105.3 % / 18.3 %) · **G7 VERDE** (110 valores; 0 calibraciones que citar) → **TODO VERDE** |
| `bp10.py barrido --dir /root/tmp-icen/dry/ice-cream-shop-business-plan --parcial` | 1,267 piezas · **0 fallos** (RX_ICE_NO, cifras ES / Pizza / Bakery / Bar / FT / REST, español, no latinos); 131 + 169 piezas aún en ES = pendientes de la tanda 1 |
| `check_textos --tanda GM / GR / GRC` (Mac) | OK los 3 (0 errores; 6 avisos de longitud en GM) · `check_revision.py GR / GRC` OK |

### 4.1 Cierre del paso 1a

- **G7 rojo en la primera corrida** (FileNotFoundError): faltaba este `F2-NOTAS.md` (`mapas.NOTAS_F2`); verde al escribirlo.
- **Barrido, 1 fallo en la primera corrida**: `Startup Costs!D12` («$25,000-45,000») daba «45,000» como cifra del caso FT EN. `_importes_research()` leía solo el primer extremo de un rango en dólares; ahora lee los dos (research §4 y SPEC D190/D193 citan el rango) → 0 fallos.
- **2.ª pasada** (`aplicar_en --dry-run --parcial` en `/root/tmp-icen/dry2`): sha256 canónico **IGUAL** en los 2 xlsx (`fbf3488d…`, `77f633c7…`); `cifras_caso.json` igual salvo `generado`.
- Ficheros de prueba (solo en el VPS): `/root/tmp-icen/dry/ice-cream-shop-business-plan/ice-cream-shop-financial-projections.xlsx` (`18bc2c79…`), `…/ice-cream-shop-startup-checklist.xlsx` (`e9575961…`), `/root/tmp-icen/dry/cifras_caso.json` (`80b56e06…`), informe `/root/tmp-icen/dry.json`. sha256 Mac = VPS: `textos_es.json` `31e644d2…`, `censo_es.json` `f4f05622…`, `formulas_ice.json` `7edf5e1a…`, `textos_en/GM.json` `9f4492e0…`, `GR.json` `7f12edbd…`, `GRC.json` `ad2e73e9…`, `docx_es_ice.json` `d259192f…`.
- **Tandas de la tanda 1 listas** (`tandas/`): `GICE-plan.entrada.json` (131 cadenas, 3,057 palabras en la entrada, 114 pistas, + 14 GR a revisar) ‖ `GICE-check.entrada.json` (157 cadenas, 2,414 palabras, 42 pistas, + 73 GRC a revisar). Validación de cada traductor: `bp10.py check_textos --tanda <G>` + `check_revision.py GR|GRC` (BRIEF §5). `ice_a`/`ice_b` ya generadas (29 / 32 párrafos) para el paso 3, que las regenera.

## 5. Defectos y deudas detectados (no bloquean)

1. **Pizza EN LIVE: texto de la DV del checklist con «—»** (confirmado): `business-plans-en-8/textos_en/GR.json` c0659
   «Use the dropdown: ✓, —, N/A. ✓ = done, — = pending…» mientras la lista es `✓,☐,N/A`. Cosmético; en el EN de la
   heladería la cadena va a GICE-check con la regla ☐ (D199). Arreglo de la pizza: una línea en `GR.revision.json` +
   regenerar (otra sesión).
2. ES de la heladería: DV `✓,—,N/A` con celdas en `☐` (sistémico, inv. §8) e `Instrucciones!A3` del checklist con el id
   interno. El EN los corrige (G4 y FIJO).
3. Fórmulas EN derivadas con literales > 255 caracteres (aviso, no error): las heredadas de la pizza y la Bakery ya LIVE
   lo superan (`PIZP` C9/C50/D27/F13, `PANP` D28); las 4 manuales de la heladería van troceadas.

## 6. Pasos siguientes (comandos)

```bash
# Mac — tras la tanda 1 (a ‖ b)
B=scripts/productos-digitales/business-plans-en-10
python3 $B/bp10.py preparar_tandas && python3 $B/bp10.py check_textos --todas
# → commit + push; VPS: git -C /root/wt-icecream pull
# VPS — paso 3
cd /root/wt-icecream/scripts/productos-digitales/business-plans-en-10 && PY=/root/venv-guias/bin/python
$PY bp10.py mapas > /tmp/ice-mapas.txt
$PY bp10.py aplicar_en --idempotencia --json /tmp/ice-real.json > /tmp/ice-aplicar.txt    # 2 xlsx en dl/ + cifras_caso.json
$PY bp10.py calibracion /tmp/ice-real.json
# (tanda 2 ice_a ‖ ice_b con las entradas regeneradas; luego)
$PY bp10.py ensamblar_docx --plan ice
$PY bp10.py gates_en && $PY bp10.py gates_en --autotest && $PY bp10.py ensamblar_docx --autotest --dir /tmp/ice-docx-at
$PY bp10.py barrido && $PY bp10.py verificar && $PY resumen_entregables.py
bash regresion_ice.sh /root/wt-icecream
```

Antes de G9: alta de `ice-cream-shop-business-plan` en `PRODUCTOS_LETTER` de `censo-entregables.py` y en `EXCLUIDOS` de
`postprocess-transversal.py` (D201).

## 7. Paso 3 de D207 (27-oct, sesión Claude Code): textos del libro aplicados, D15 real y entradas de la tanda 2

Tanda 1 de dos traductores sonnet (commits `768e5ec5`, `253d558c`, `556fe5da`): `GICE-plan.json` (131) + `GR.revision.json`
(1: c0086 «indoor seats») ‖ `GICE-check.json` (157) + `GRC.revision.json` (1: c0618 «Owner / Zoning consultant»).
Repaso del orquestador del paso 3 sobre lo sensible (pasteuriz-, custard, gelato, homemade, allergen-free, °C): coherente
con D190 (base comprada; mezcla propia = variante; licencias «ask your state department of agriculture», sin tarifas).

| Comprobación | Resultado |
|---|---|
| `preparar_tandas` (Mac) | GR.revision y GRC.revision aplicadas (1 + 1); GM/GR/GRC = 369 / 14 / 73 |
| `check_textos --todas` (Mac) | GM OK (6 avisos de longitud) · GR, GRC, GICE-plan, GICE-check OK (0 errores, 0 avisos); ice_a / ice_b pendientes (tanda 2) |
| Alta de G9 (D201) | `ice-cream-shop-business-plan` en `PRODUCTOS_LETTER` de `censo-entregables.py` y en `EXCLUIDOS` de `postprocess-transversal.py` (línea propia + comentario) |
| `bp10.py mapas` (VPS) | 0 errores · verificar OK (6 avisos de FIJOS del motor sin uso) |
| `aplicar_en --idempotencia --json /tmp/ice-real.json` (VPS) | préstamo **$162,000** en 1 vuelta · textos 540 + 366, **faltan 0** · **0 diferencias** entre dos construcciones · inject_cache 736 + 12, **0 fallos de pycel** · 2 xlsx en `dl/ice-cream-shop-business-plan/` + `cifras_caso.json` (112 tokens) |
| `bp10.py calibracion /tmp/ice-real.json` | **VERDE** (= dry-run de §3: holgura 18.3 %, DSCR 2.26, saldo $46,060, cobertura 105.3 %, neto año 3 8.6 %, D196 verde); `CALIBRACION_D15` sigue vacía |
| `gates_en --solo G1,G2,G3,G4,G5,G6,G7,G9` | **TODO VERDE**: G1 736 fórmulas + 80 tareas [12, 15, 15, 12, 13, 13] · **G2 1,299 piezas** (incl. RX_ICE_NO y cifras prohibidas) · G3 16 hojas Letter · G4 233 valores bajo DV · G5 8 rangos CF · G6 0 diferencias · G7 110 valores, 0 calibraciones · **G9** censo 0 defectos + no latinos 0 (2 ficheros). G8 espera al Word (paso 4) |
| `bp10.py barrido` (los 2 xlsx) | 1,267 piezas · **0 fallos** (RX_ICE_NO, cifras ES / Pizza / Bakery / Bar / FT / REST, español, no latinos) → `barrido_ice.json` |

**Caso final** (`cifras_caso.json`, 112 tokens; ninguna cifra distinta del dry-run de §3): ventas **$383,625** / $414,315 /
$435,031 (165 × $7.50 × 310; $8.10 con sales tax) · CAPEX **$204,100** + fondo $52,771 = **$256,871** · propios $95,000
(37 %) + préstamo **$162,000** (cuota $26,365) · margen tras variables 68.2 % · COGS 22.3 % · personal $128,185 (33.4 %) ·
prime cost 55.7 % · fijos $16,600 · EBITDA $66,747 (17.4 %) · neto **$21,585 (5.6 %)** / 7.7 % / **8.6 %** · equilibrio
**147** / **140** customers/día · holgura **18 %** · DSCR mín **2.26×** · saldo mín **$46,060** (Mes 1) · pesimista $294,000 y
−$32,344 (caja $32,029, no se agota) · optimista $486,400 y +$98,872.

| Entregable (`astro-site/public/dl/ice-cream-shop-business-plan/`) | sha256 (Mac = VPS) |
|---|---|
| `ice-cream-shop-financial-projections.xlsx` (9 hojas, 736 fórmulas) | `cbb6c10c…` |
| `ice-cream-shop-startup-checklist.xlsx` (7 hojas, 80 tareas, DV `✓,☐,N/A`) | `776ea70a…` |
| `business-plans-en-10/cifras_caso.json` | `6cbbdb40…` |

**Tanda 2 preparada** (Mac): `bp10.py preparar_tandas` + **`anotar_tandas_docx.py`** (nuevo, solo del conjunto: añade a
cada entrada `cifras_del_caso` = el texto final de los 112 tokens leído de `cifras_caso.json`, para entender el caso; en el
Word siguen yendo SOLO tokens). `tandas/ice_a.entrada.json` (29 párrafos, 3,039 palabras, §1-5) ‖
`tandas/ice_b.entrada.json` (32, 3,780, §6-10); salidas `docx_en_ice_a.json` / `docx_en_ice_b.json`; brief §4 (con la
terminología fijada por la tanda 1) y comando de cada uno en §5:
`python3 scripts/productos-digitales/business-plans-en-10/bp10.py check_textos --tanda ice_a` (o `ice_b`).

Siguiente (paso 4, VPS): `bp10.py ensamblar_docx --plan ice` → `gates_en` completo (G8) + `--autotest` +
`ensamblar_docx --autotest` → `barrido` (3 entregables) → `resumen_entregables.py` → `regresion_ice.sh` → 2.ª pasada →
revisión D203.
