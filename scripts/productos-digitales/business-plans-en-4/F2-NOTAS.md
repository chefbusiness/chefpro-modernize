# Catering Business Plan Kit (EN) — F2 (entregables) · notas

> Sesión Claude Code, 11-oct-2026. **Paso 1 de la F2** (conjunto «cat», extracción, reuso, caso US + D15, fórmulas
> D72, 4 tandas, calculadora D76, regresión). Implementador único, sin subagentes. Código en el Mac; lo que abre
> xlsx/docx, en el **VPS** (`/root/wt-cat`, venv `/root/venv-guias`). Rama `feat/catering-business-plan-en`.

## 1. Cómo se montó el conjunto «cat» (fuente ES del circuito = FOOD TRUCK ES)

Como el bar (`BP_CONJUNTO=cat` → `mapas_cat.instalar(M)`, `mapas.DATOS = business-plans-en-4/`, lanzador `bp4.py`).
**Lo nuevo**: la fuente del circuito son los 3 ficheros del **FT ES**, no el catering ES; el contenido de catering entra
por las pistas y `fuente_es_cat.json`, y el reuso es **por celda** (EN publicado del FT en ESA celda).

| Fichero | Qué lleva |
|---|---|
| `mapas_cat.py` | Producto D66-D68 (`dir_es` = FT ES; `slug_es` = gemelo hreflang), pestañas (F2 «Phase 2 - Kitchen, Van, Permits»), 68 tareas 11/13/12/10/12/10, **7 parches** (E2 ×2, `Staffing!B20` → `$B$4`, `Staffing!C9` → SUMPRODUCT (E4), `Break-Even!B31/D31/E31` ±$10/+$20), versión A73/A11, zonas celda a celda (D18 35-51, D19 55-68 y **zona «TAREA»: B-E de las 68 tareas**), docx 131 párrafos (H1 37…109, último de §9 = 108), grupos, `FT_CELDA` (EN publicado del FT por celda + `overrides_GFT`) y `FT_TEXTO` (mensajes de DV) |
| `datos_cat.py` | FIJOS (27 nuevos: motor permutado D72, títulos, D19, comisiones del marketplace), POR_CELDA (43: Supuestos, filas 7-23 de la inversión, P&L A22/A27/A34/A35/A55, 4 puestos + cobertura + nota W-2/AB5 en `Staffing!A24`, `Cash Flow!O5`), cifras y vocabulario prohibidos (D70, D72 + importes del caso FT EN), 114 tokens (alias de catering + 6 partidas + 2 derivadas), notas del docx (las 61 ranuras), pistas (caso, D18, D19 por fila, **68 tareas por fila**), glosario, caso US, `CALIBRACION_D15`, FORMULAS_EN |
| `bp4.py` | Lanzador (copia de `bp3.py`) + `verificar` (exige 272 celdas de tarea en GCAT-check) + `fuente` + `calculadora` |
| `fuente_cat.py` → `fuente_es_cat.json` | Contenido del catering ES para los redactores: 108 tareas por fase (21 marcadas fuera: SOLO_ES y MULTICOCINA), 119 párrafos y 7 tablas del docx ES |
| `calculadora_cat.py` · `BRIEF-TRADUCTORES.md` | D76 (§5) · brief de las 4 tandas (adaptado del bar) |

**Grupos** (`textos_es.json`, 959 cadenas):

| Grupo | Cadenas | Palabras ES | Qué es | Va a |
|---|---|---|---|---|
| GM | 335 | 3.669 | Motor común FT/CAF cuyo EN del FT vale para catering (sin vocabulario de food truck ni de local) | nadie: `textos_en/GM.json` ya escrito |
| GR | 7 | 277 | EN del FT reutilizable con «revisar contexto» (build-out, menu price, delivery, títulos de fase) | `textos_en/GR.json` escrito; revisión en GCAT-check |
| **GCAT-plan** | 206 | 4.356 | 78 de texto libre (las propias del FT + las del motor con clientes/día, días, ticket, camión…) + 128 celdas D18/D19; 150 con `propuesta_en` del FT | tanda 1 (a) |
| **GCAT-check** | 272 | 1.286 | 68 tareas × 4 columnas, una por celda, con pista de la tarea de catering de esa ranura | tanda 1 (b) |
| GX | 139 | 724 | Pestañas, CLAVES, FIJOS, POR_CELDA, versión, pie, docProps | nadie |

Docx (`docx_es_cat.json`, VERDE): 131 párrafos, 0 multi-run; 61 ranuras a escribir → **cat_a 29 / 2.954 palabras de
ranura · cat_b 32 / 3.765**, cada una con su nota de catering (`DOCX_NOTAS`, §9 = 7 notas legales D78, el 108 cierra
con la nota UK).

## 2. No regresión de FT/CAF, REST/PAN y BAR (VPS, con la rama `cat` en `mapas.py`)

| Conjunto | `mapas` | `gates_en` (dl/ publicados) · `--autotest` | `ensamblar_docx --autotest` | `check_textos --todas` |
|---|---|---|---|---|
| FT/CAF (`mapas.py`, `gates_en.py`…) | 0 errores | **TODO VERDE** G1-G9 · **20/20** | **18/18** | las 7 OK |
| REST/PAN (`bp2.py`) | 0 errores | **TODO VERDE** · **20/20** | **16/16** | las 8 OK |
| BAR (`bp3.py`) | 0 errores | **TODO VERDE** · **20/20** | **8/8** | las 6 OK |
| CAT (`bp4.py`) | 0 errores (cruce con el censo + `verificar` OK) | parcial G1, G3-G7 VERDE sobre el dry-run | **8/8** | GM OK · GR OK · el resto, pendiente de redactar |
Único cambio en el código común: la rama `elif CONJUNTO == 'cat'` de `mapas.py`. `check_textos` del catering caza lo
inyectado (vocabulario D72, cifras ES; «Corporate customers» permitido).

## 3. Caso US y dry-run (`bp4.py aplicar_en --dry-run --parcial --salida /tmp/cat-dry`, VPS)

Research §8 tal cual (170 eventos × $60 × 60 invitados): préstamo $145,000, **holgura de caja 14.2 % (< 15 %)** → D15
ROJO. Aplicada la regla D70 (B4 de 10 en 10): con **180** la cobertura de horas bajaba a 97.1 % (12 h × 4.3 personas ×
180 = 9,288 h frente a 9,020), así que el pool de personal de eventos sube de 0.22 a 0.23 FTE por persona y su bruto en
proporción. `CALIBRACION_D15` (G7 exige cada celda citada aquí):

| Celda | Research | Calibrado | Motivo |
|---|---|---|---|
| CATP 0. Supuestos!B4 | 170 | **180** | D15: holgura 14.2 % → 19.6 %; 180 × $60 × 60 = $648,000 |
| CATP Escenarios!B5 | 128 | **135** | pesimista = 180 × 0.75 (proporción de research) |
| CATP Escenarios!D5 | 213 | **225** | optimista = 180 × 1.25 |
| CATP Personal!C7 | 0.22 | **0.23** | cobertura ≥ 98 % con 180 eventos (8 personas × 0.23 FTE) |
| CATP Personal!D7 | 5,796 | **6,060** | 8 × 0.23 × 173.33 h × $19 |

Resultado (caché del dry-run, `cifras_caso.json` de `/tmp/cat-dry`): ventas **$648,000** / $745,200 / $819,720 ·
CAPEX **$107,200** (la contingencia del 10 % va sobre las filas 7+8+11+12+15 = $47,000, no solo 7-8 como estimó
research: +$1,100) + fondo de maniobra $78,253 = **$185,453** · fondos propios $40,000 (22 %) + préstamo **$146,000**
(punto fijo, 1 vuelta con la semilla) · margen bruto 60.6 % · mercancía 29.4 % · personal 34.4 % · comisaria 4.6 % ·
EBITDA $94,276 (14.5 %) · neto $48,466 (**7.5 %**) · equilibrio **151 eventos/año** (contable = caja) · holgura 20 % ·
DSCR mín **2.60×** · saldo mínimo $50,545 (mes 4) · payback 1.9 años · 11 personas = 4.59 FTE, cobertura 99 % ·
$3,600 por evento, 10,800 invitados · pesimista $400,950, −$85,091 y **caja −$7,173** (se agota: el docx debe decirlo,
como el FT) · optimista $965,250 y +$256,875. Los 5 umbrales del P&L en verde los 3 años (con E51 = 60 %, §4).

`bp4.py gates_en --dir /tmp/cat-dry --parcial --solo G1,G3,G4,G5,G6`: **TODO VERDE** (722 fórmulas; 68 tareas
[11, 13, 12, 10, 12, 10]; 16 hojas Letter; 202 valores bajo DV; 8 rangos de CF; caché = referencia ES recalculada, 0
diferencias). G7 VERDE con estas notas (§2).

## 4. Decisiones y desviaciones de la SPEC

1. **Pestaña F2 = «Phase 2 - Kitchen, Van, Permits»**: la de D77 tiene 32 caracteres y Excel admite 31. El título de la
   hoja (sin límite) conserva «PHASE 2: KITCHEN, VAN & PERMITS».
2. **Umbral de margen bruto 60 %, no 62 % (D75)**: el «margen bruto» del motor resta también tarjeta (2.5 %),
   comisión del marketplace (1.5 %) y varios (3 %); el 67.6 % de research §8 solo restaba mercancía + desechables. Con
   62 % el propio caso salía ámbar los 3 años. Es una línea (`datos_cat.valores_cat`, E51): si se prefiere 62 %, el
   caso queda en REVIEW y no cambia nada más.
3. **Calibración** (§3): B4 170 → 180 por la regla D70, más el pool de personal de eventos (no previsto por research)
   para no romper la cobertura de horas.
4. **`B51`** no entra en ninguna fórmula del FT (medido en el censo): queda como DATO INFORMATIVO «Max events a year
   your kitchen and crew can handle» = 250 (D70), con nota para compararlo con B4 y el optimista.
5. **Gate de vocabulario D72 también en el docx y en los traductores** (va en `CIFRAS_PROHIBIDAS`, que leen G2,
   `check_textos` y g8): un competidor food truck se nombra «mobile food vendors». «customers» se permite solo en
   «corporate customers» (y en la frase sintética de `ensamblar_docx --autotest`, que es código común y la dice).
6. **Checklist celda a celda** (zona «TAREA»): el FT repite textos ES («Titular», «Ayuntamiento», «1 semana») en tareas
   que en catering son distintas; con un id por celda cada ranura lleva su tarea. Para que la pista D19 no se cuele en
   las tareas, `PISTA_D19` pasa a genérica y la de cada fila D19 va por celda.
7. **Mensajes de DV compartidos** (B6 = invitados, B58/B59 = días): a los redactores, un texto para los dos.
8. **BAR/REST no aportan al diccionario**: las cadenas ES son las del FT (solo coincide el motor, ya GM).
9. **Fuera de mi alcance (paso 3/F3)**: `catering-business-plan` en `PRODUCTOS_LETTER` de `censo-entregables.py` y en
   `EXCLUIDOS` de `postprocess-transversal.py` (G9 de `gates_en` los necesita; hoy se pasa con `--letter --only`).

## 5. Calculadora D76 (`calculadora_cat.py` → `astro-site/public/dl/catering-business-plan/catering-pricing-calculator.xlsx`)

3 pestañas: «Pricing Calculator» (19 entradas verdes con DV: listas de estilo de servicio y Yes/No del sales tax sobre
el service charge; enteros, importes ≥ 0, porcentajes 0-1, margen 0-95 %; tabla editable de invitados por server por
estilo), «3 Example Quotes» (corporate drop-off lunch · wedding buffet · plated dinner, con las MISMAS fórmulas) e
«Instructions» (IRS Rev. Rul. 2012-18, sales tax CA / NY / TX, VAT UK, Kit estimates, firma, versión y aviso). Precio
por invitado = coste directo ÷ (1 − margen objetivo), redondeado a 0.50 por arriba; el margen se calcula; la propina
voluntaria queda fuera del total. docProps D20, Letter + ajuste + pie, hojas protegidas sin contraseña.

| Ejemplo (Kit estimate) | Invitados | Precio | Subtotal | Service charge | Tax | Total | Margen |
|---|---|---|---|---|---|---|---|
| Corporate drop-off lunch | 40 | 30.50 | 1,220.00 | 0.00 | 97.60 | 1,317.60 | 55.5 % |
| Wedding buffet | 120 | 106.50 | 12,780.00 | 2,556.00 | 1,226.88 | 16,562.88 | 50.1 % |
| Plated dinner (estado que no grava el SC) | 60 | 85.50 | 5,130.00 | 1,026.00 | 410.40 | 6,566.40 | 50.2 % |

**Autotest** (`bp4.py calculadora`): inject_cache 68 fórmulas, 0 fallos de pycel; **136 comprobaciones** (pycel + caché
= cálculo en Python) en los 3 ejemplos y la hoja principal, margen ≥ objetivo, interruptor con efecto, 0 cadenas
vacías, 0 verdes bloqueadas, sin «€» ni símbolo en formatos, 0 español / no latinos / cifras prohibidas / anclas →
**VERDE**. `censo-entregables.py --fail --letter --only catering-business-plan`: 0 defectos; `gate-no-latinos`: 0.

## 6. Comandos para seguir

```bash
# PASO 2 — redactores (Mac, máx. 2 a la vez, istats < 62 °C; BRIEF-TRADUCTORES.md). tanda 1: (a) GCAT-plan ‖
#   (b) GCAT-check (+ GR.revision.json) · tanda 2: (c) cat_a ‖ (d) cat_b — entradas en tandas/, salidas en textos_en/ y docx_en_*
python3 scripts/productos-digitales/business-plans-en-4/bp4.py check_textos --tanda GCAT-plan   # | GCAT-check | GR | cat_a | cat_b
python3 scripts/productos-digitales/business-plans-en-4/bp4.py preparar_tandas                  # tras GR.revision.json
python3 scripts/productos-digitales/business-plans-en-4/bp4.py check_textos --todas

# PASO 3 — VPS: aplicar, calibrar (ya fijada), ensamblar, gates
ssh vps
cd /root/wt-cat && git pull --ff-only && cd scripts/productos-digitales/business-plans-en-4 && PY=/root/venv-guias/bin/python
$PY bp4.py aplicar_en --idempotencia --json /tmp/cat-real.json      # 2 xlsx en dl/catering-business-plan/ + cifras_caso.json
$PY bp4.py ensamblar_docx --plan cat                                # tras cat_a + cat_b
$PY bp4.py gates_en && $PY bp4.py gates_en --autotest && $PY bp4.py ensamblar_docx --autotest --dir /tmp/cat-docx-at
$PY bp4.py calculadora --autotest                                   # la calculadora no se regenera si no cambia
# G9: antes, catering-business-plan en PRODUCTOS_LETTER (censo-entregables) y EXCLUIDOS (postprocess-transversal)
# regresión §2; vuelta por scp (sha256 iguales); commit desde el Mac; VPS limpio
# si cambian FIJOS / POR_CELDA / zonas / grupos: $PY bp4.py extraer_textos > /tmp/cat-ext.txt (VPS) y preparar (Mac)
```

VPS: `/dev/null` es un fichero normal (redirigir a `/tmp/*.txt`); copiar del Mac con `COPYFILE_DISABLE=1 tar`.

## 7. Riesgos para los pasos 2-3

1. **Redactar, no traducir**: el `es` de GCAT-check y del docx es la ranura del FOOD TRUCK; si un redactor la
   traduce, saldrá un checklist de camión. Las pistas por fila (68) y las notas por párrafo (61) lo atan; la revisión
   final debe leer el checklist entero.
2. **Vocabulario D72** en GM: se filtró por regex (ES y EN del FT); `gates_en` G2 lo vuelve a barrer en los xlsx
   generados. Si salta algo en GM, pasarlo a POR_CELDA o a FORZAR_TRADUCTORES (`mapas_cat.py`) y re-extraer.
3. **Pesimista con caja negativa** (−$7,173) y **equilibrio contable = de caja (151)**: el docx §8 debe explicarlo (el
   FT tenía lo mismo); la nota E23 de Scenarios lo matiza (el personal de eventos baja con los eventos).
4. Tabla D19: 6 de 14 filas son «Kit estimate» (fuentes «resumen» de research). Si se rehace la extracción, los ids de
   `textos_es.json` pueden moverse y las salidas de los redactores dejan de casar.

## 8. Cierre de la F2 (11-oct, sesión Claude Code): xlsx + docx EN, gates

Tandas del paso 2 en `ead0a230` / `30d236dd` (`check_textos --todas` OK). Paso 3 en el VPS sobre `30d236dd`:
`aplicar_en --idempotencia` → préstamo **$146,000** en 1 vuelta, textos 564 + 318, faltan 0, **0 diferencias** entre
dos construcciones, inject_cache 722 / 12 fórmulas y **0 fallos de pycel**, D15 sin fallos; `ensamblar_docx --plan cat`
→ G8 VERDE. `catering-business-plan` dado de alta en `PRODUCTOS_LETTER` (`censo-entregables.py`) y `EXCLUIDOS`
(`postprocess-transversal.py`).

**Caso final** (`cifras_caso.json`, 114 tokens): 180 eventos × 60 invitados × $60.00 sin sales tax ($64.80 con él) →
ventas **$648,000** / $745,200 / $819,720 ($3,600 por evento) · CAPEX $107,200 + fondo de maniobra $78,253 =
**$185,453** · fondos propios $40,000 (22 %) + préstamo $146,000 al 10 % a 7 años (cuota $29,989) · margen bruto 60.6 % ·
mercancía 29.4 % · personal 34.4 % · comisaria 4.6 % · EBITDA $94,276 (**14.5 %**) · neto $48,466 (7.5 %) / $87,798 /
$116,937 · equilibrio **151 eventos/año** (contable y de caja), holgura 20 % · **DSCR 2.60×** · saldo mínimo $50,545
(mes 4) · payback 1.9 años (1.3 sobre el CAPEX) · 11 personas = 4.59 FTE, cobertura 99 % · seguros $6,000 · pesimista
$400,950, −$85,091 y caja −$7,173 (el docx §8 lo dice: «in a weak year, cash can run out») · optimista $965,250 y
+$256,875. Los 5 umbrales del P&L en verde los 3 años.

| Comprobación (VPS) | Resultado |
|---|---|
| `bp4.py gates_en` (G1-G9 sobre `dl/catering-business-plan/`) | **TODO VERDE** (G2 incluye vocabulario D72 y cifras prohibidas; G9 = censo-entregables + no latinos) |
| `bp4.py gates_en --autotest` · `ensamblar_docx --autotest` · `calculadora --autotest` | **20/20** · **8/8** · VERDE (136 comprobaciones) |
| `barrido_cat.py` (independiente: celdas, literales de fórmula, DV, docProps, párrafos y tablas) | 1,557 piezas · **0** vocabulario D72 / cifras prohibidas · 0 español · 0 no latinos (`entregables_cat.json`) |
| `censo-entregables --fail --letter --only catering-business-plan` · `gate-no-latinos --only` | 4 ficheros, 802 fórmulas, **0 defectos** · 0 caracteres |
| Regresión §2 (FT/CAF, REST/PAN, BAR) | TODO VERDE · 20/20 · 18/18 · 16/16 · 8/8 · `check_textos` OK |

| Entregable (`astro-site/public/dl/catering-business-plan/`) | Contenido | sha256 (Mac = VPS) |
|---|---|---|
| `catering-business-plan.docx` | 131 párrafos (110 con texto), 10 Heading 1, 6,507 palabras, Letter | `1689a0dbdfe19f8b…` |
| `catering-financial-projections.xlsx` | 9 hojas, 722 fórmulas, caso US calibrado | `c22fb993343373ce…` |
| `catering-pricing-calculator.xlsx` | 3 hojas, 68 fórmulas | `765ea87e9c981660…` |
| `catering-startup-checklist.xlsx` | 7 hojas, 68 tareas (11/13/12/10/12/10), 12 fórmulas | `abea9e278eaafaff…` |

**Para la revisión final (una pasada opus)**: (1) leer el checklist entero: las 272 celdas se escribieron sobre ranuras
del food truck; (2) recalcular a mano 3 cifras (ventas = 180 × 60 × 60, equilibrio 151, DSCR) y abrir 3 fuentes legales
del §9 (eldoradocounty.ca.gov, tax.ny.gov TB-ST-320, IRS Rev. Rul. 2012-18); (3) D19: 6 filas «Kit estimate»;
(4) desviaciones §4 (pestaña de 31 caracteres, umbral 60 %, calibración); (5) notas largas de `Staffing!A24` y
`Cash Flow!O5`: alto de fila en Excel / LibreOffice y a 360 px; (6) «guests» frente a «clients» en el docx.

## 9. Ronda de arreglos tras `REVISION-FINAL.md` (11-oct, sesión Claude Code): todo por la vía de TEXTO

Aplicados los 5 MAYOR y los 14 MENOR sin tocar ninguna fórmula numérica ni ninguna cifra del caso:

| Dónde vive | Arreglos |
|---|---|
| `datos_cat.py` POR_CELDA | M1 `Startup Costs!A15` «Health permit plan / SOP review» · M2 `3-Year P&L!A27` «Van maintenance, repairs and inspections» · m9 `Staffing!A24` (corta) · m10 `Cash Flow!O5` (corta) · m4 `0. Assumptions!C20` · m11 `C39` (VAT del catering, Notice 709/1) · m2 `C67` y `Break-Even!E24` (holgura frente a caída absorbible). Las 4 últimas eran GM (motor) y pasan a GX: mismos ids y mismo ES al re-extraer |
| `datos_cat.py` FORMULAS_EN | M2 `3-Year P&L!F18`: el combustible de cada viaje está en «Miscellaneous» (variable) y el mantenimiento en la fila 27 · m11 `Startup Costs!D21` «when the commissary agreement ends» |
| `datos_cat.py` TOKENS | `caida_absorbible_pct` (derivado = holgura ÷ (1 + holgura) = **16%**) para el docx [97] (m2) |
| `textos_en/GCAT-plan.json` | M1 `D15` · M2 `Instructions!A43` «Generator and burner fuel» · M3 `C5` (cómo traer el precio de la calculadora) · m1 `F53` · m8 `Instructions!D66` |
| `textos_en/GCAT-check.json` | M1 `Phase 2!E7` · M3 `Phase 4!E14` · m5 LLC (fila 6) antes que EIN (fila 7) · m6 `Phase 6!B11/E11` · m14 `Phase 2!E6/B13`, `Phase 3!B10` |
| `docx_en_cat_a/_b.json` | M1 [103] · M2 [82] · M3 [106] · M4 [64], [102] · M5 [99] · m2 [97] · m3 [43], [86], [87] · m6 [98] · m7 [106] · m12 [114] · m13 [40], [105] |
| `calculadora_cat.py` | M3 rótulo «PRICE PER GUEST before service charge and tax», notas `C19` (service charge: lo repartido es salario, lo retenido ingreso) y `C32` · m7 `C21` e `Instructions` (NY/TX: «identified as a gratuity», TX > 20 % todo gravado) |

**Desviación**: la nota de M2 en `3-Year P&L!F27` no se puede escribir. La celda está vacía en el FT ES y el código común
solo deja añadir celdas en el aviso D21 (`TEXTOS_NUEVOS`, G1). Esa nota va en `F18`, la nota de la fila de varios, y
en el rótulo A27. «El Dorado County» en `D15` se escribe como «one California county does: eldoradocounty.ca.gov»
porque el detector común de español lee «El» y no se puede tocar.

**Regeneración y gates (VPS)**: `aplicar_en --idempotencia` → préstamo $146,000 en 1 vuelta, 0 diferencias, 0 fallos
de pycel, D15 sin fallos. **`cifras_caso.json`: ninguna cifra cambia**, solo se añade `caida_absorbible_pct` (115
tokens; sha256 `75cc508097d70fa2…`). `ensamblar_docx` G8 VERDE. Calculadora con autotest VERDE (los 3 ejemplos no
cambian). `gates_en` G1-G9 **TODO VERDE** · `--autotest` 20/20 · `ensamblar_docx --autotest` 8/8 · `check_textos
--todas` OK · `barrido_cat.py` 1,557 piezas, 0 fallos · `censo-entregables --letter` 4 ficheros, 0 defectos ·
`gate-no-latinos` 0 · regresión FT/CAF, REST/PAN y BAR en verde.

| Entregable | sha256 (Mac = VPS) |
|---|---|
| `catering-business-plan.docx` (6,662 palabras) | `d35a5e9395cccbe8d93c034817d78c0c30b79670a6fc1aeb8ee2fa21438a046d` |
| `catering-financial-projections.xlsx` | `2265cb3e8d724e1ecb3b5fdee346e61294e8e82b6f5c0be1eb574b05204d506e` |
| `catering-pricing-calculator.xlsx` | `f60afcefbca519d0705657ccd0b2289ac678bbe08ec980078e9a4741ebceb7b3` |
| `catering-startup-checklist.xlsx` | `fc21a29b67a6c749e08421c1781c38447cb34d0ff1317199bc672985e0f57ff4` |
