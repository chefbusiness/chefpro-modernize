# Paella Catering Business Plan Kit (EN) — F2 (entregables) · notas

> Sesión Claude Code, 24-oct-2026. **Paso 1 de la F2** (conjunto «pael», extracción, diccionario en cadena BBQ → catering,
> caso US + D15, 4 tandas preparadas solo con lo que cambia, calculadora D123-D124, regresión). Implementador único, sin
> subagentes. Código en el Mac (worktree `wt-paella`); lo que abre xlsx/docx, en el **VPS** (`/root/wt-paella`, venv
> `/root/venv-guias`). Rama `feat/paella-catering-business-plan-en` (apilada sobre el BBQ cerrado, `4610f8da`). CPU del Mac
> < 54 °C en todo el paso.

## 1. Cómo se montó el conjunto «pael» (fuente ES del circuito = FOOD TRUCK ES; diccionario = BBQ → CATERING; código = BBQ)

`BP_CONJUNTO=pael` → `mapas_pael.instalar(M)`, `mapas.DATOS = business-plans-en-7/`, lanzador `bp7.py`. **Único cambio en
código común**: la rama `elif CONJUNTO == 'pael'` de `business-plans-en/mapas.py` (+ el mensaje de error). El reuso por
celda va **en cadena** (D119): el EN del BBQ cerrado en esa celda y, si no hay, el EN publicado del catering. `bp7.py
verificar` comprueba los **16 sha256** (8 del BBQ en `mapas_pael.SHA_BBQ`, fijados sobre `4610f8da`, + los 8 del catering
de siempre): 0 derivas.

| Fichero | Qué lleva |
|---|---|
| `mapas_pael.py` | Producto D114-D116 (`dir_es` = FT ES, `slug_es` = paellero ES), libros `PAEP`/`PAEC`, pestaña F2 «Phase 2 - Propane & Permits» (27 car.), 68 tareas 11/13/12/10/12/10, los **7 parches** del BBQ sin cambios (Break-Even ±$3 / +$6), zonas D18/D19/TAREA, docx 131 ranuras, `RX_REESCRIBIR` = vocabulario y caso del BBQ + lo que sigue vetado del catering (salen burners, stations y «paella chef»), **51 `FORZAR_TRADUCTORES`** (los del BBQ), `D19_CON_PROPUESTA` = 58, 60, 62, 64, 65, 67, `propuesta_de` (BBQ → catering), transformación mecánica de la columna C del checklist («Pitmaster» → «Paella chef», D125), `PRESTAMO_SEMILLA` = 64,000 |
| `datos_pael.py` | FIJOS (31: motor, títulos, D19, líneas «paella packages / add-ons» y su coste, «Disposables & cooking fuel»), POR_CELDA (66: Supuestos, inversión 7-23 y A31 con los huecos del BBQ, P&L, 4 puestos W-2, `Cash Flow!O5`, notas del motor), `REGLA_UNIDADES` (paelleras en pulgadas con cm, azafrán en gramos, el mínimo del Food Code nombrado como tal), cifras prohibidas (paellero, BBQ, catering, mobile bar, FT) + `RX_PAEL_NO` (D128), tokens (alias de eventos, 11 partidas propias con `inv_quemadores` / `inv_paelleras` / `inv_propano` / `inv_montaje`, `pago_dias` en su celda), 61 `DOCX_NOTAS` (nivel + pista + **PROPUESTA EN DEL BBQ de la ranura** + ES 2.2 del paellero en las «adaptar» y «nueva»), pistas (caso, D18 con 4 filas específicas, 14 filas D19, **68 tareas `TAREAS_PAEL`** con las columnas que cambian), glosario §9 completo, caso US, `CALIBRACION_D15` (vacía), FORMULAS_EN |
| `bp7.py` | Lanzador (copia de `bp6.py`) + `verificar` (272 celdas de tarea en GPA-check ∪ GLB-check + los 16 sha256) + `fuente` + `calculadora` + `barrido` |
| `fuente_pael.py` → `fuente_es_pael.json` | Checklist ES del paellero desde `paellero-2_2/datos_checklist.py` (83 tareas, 10 SOLO_ES y 8 parciales marcadas), docx ES 2.2 por ranura (61), manual técnico (178 párrafos, 10 tablas), carta de 12 paellas (89), 10 experiencias (56), contrato (94) y catálogo de equipo (132) |
| `calculadora_pael.py` · `barrido_pael.py` · `BRIEF-TRADUCTORES.md` | D123-D124 (§5) · barrido del paso 3 · brief de las 4 tandas con el **glosario §9 completo pegado** y la regla «redactar, no traducir: la propuesta del BBQ da la forma; la pista manda; cero vocabulario BBQ» |

**Grupos** (`textos_es.json`, 959 cadenas, sha256 `30b07f0339d7e02a…`):

| Grupo | Cadenas | Palabras ES | Qué es | Va a |
|---|---|---|---|---|
| GM | 312 | 3.472 | Motor cuyo EN (BBQ = catering) no trae vocabulario ni caso del BBQ | nadie: `textos_en/GM.json` ya escrito |
| GRB-plan | 98 | 1.648 | EN del BBQ que vale con revisión: 54 celdas de la tabla D18, 23 notas del motor y **21 celdas limpias de las filas D19 con propuesta** | `textos_en/GRB-plan.json` escrito; revisión en la tanda (a) |
| GLB-check | 202 | 850 | **199 celdas de tarea** cuya propuesta del BBQ vale tal cual (C con «Paella chef») + 3 textos del checklist | nadie: `textos_en/GLB-check.json` ya escrito |
| **GPA-plan** | 109 | 2.967 | 74 de texto libre (51 forzadas + 23 con vocabulario BBQ: notas C, D de inversión, F del P&L, J de Staffing, 14 celdas D18, A5) + **35 celdas D19** (32 de las 8 filas nuevas + 3 sucias de las filas con propuesta) | tanda 1 (a) |
| **GPA-check** | 73 | 455 | Las celdas que CAMBIAN de las 68 tareas (columnas marcadas en `TAREAS_PAEL` + 2 por palabra vetada) | tanda 1 (b) |
| GX | 165 | 918 | Pestañas, CLAVES, FIJOS, POR_CELDA, versión, pie, docProps | nadie |

Docx (`docx_es_pael.json`, VERDE): 131 párrafos, 0 multi-run; 61 ranuras → **pael_a 29 / 2.954 palabras de ranura ·
pael_b 32 / 3.765**; cada una con su nota (19.185 palabras en total con las propuestas del BBQ y el ES 2.2).

## 2. No regresión (VPS, con la rama `pael` en `mapas.py`; `/tmp/regresion-pael.sh`, no versionado, reproducible con la tabla)

| Conjunto | `mapas` | `gates_en` (dl/ publicados) · `--autotest` | `ensamblar_docx --autotest` | `check_textos` | calculadora `--autotest` |
|---|---|---|---|---|---|
| FT/CAF (`mapas.py`, `gates_en.py`…) | 0 errores | **TODO VERDE** · **20/20** | **18/18** | las 7 OK | — |
| REST/PAN (`bp2.py`) | 0 errores | **TODO VERDE** · **20/20** | **16/16** | las 8 OK | — |
| BAR (`bp3.py`) | 0 errores | **TODO VERDE** · **20/20** | **8/8** | las 6 OK | — |
| CAT (`bp4.py`) | 0 errores | **TODO VERDE** · **20/20** | **8/8** | las 6 OK | VERDE (136) |
| MBAR (`bp5.py`) | 0 errores | **TODO VERDE** · **20/20** | **8/8** | las 6 OK | VERDE (778) |
| BBQ (`bp6.py`) | 0 errores | **TODO VERDE** · **20/20** | **8/8** | las 6 OK | VERDE (581) |
| PAEL (`bp7.py`) | 0 errores (`verificar` OK, 16 sha256) | parcial G1, G3-G7 **VERDE** sobre el dry-run (§3) | **8/8** | GM · GRB-plan · GLB-check OK; el resto, pendiente de redactar | VERDE (509) |

## 3. Caso US, dry-run y calibración D15 (`bp7.py aplicar_en --dry-run --parcial --salida /tmp/pael-dry`, VPS)

Research §8 / SPEC D118 tal cual (135 eventos × $40 × 58 invitados, inversión con los huecos del BBQ, D120): **D15 en verde
sin tocar `B4` ni `B35`** (holgura 15.8 %, DSCR mín 2.47, saldo mín > 0, cobertura 138 %). Préstamo de punto fijo
**$64,000** (semilla 62,000 → 64,000 → 64,000; `PRESTAMO_SEMILLA` = 64,000): supera el tope de $50,000 del SBA Microloan
y encaja en un **SBA 7(a)** (D118). **`CALIBRACION_D15` queda vacía** (G7: 0 calibraciones citadas).

Resultado (caché del dry-run, `cifras_caso.json` de esta carpeta, 118 tokens):
- Ventas **$313,200** / $344,520 / $365,191 (**$2,320 por evento**, 7,830 invitados).
- CAPEX **$49,480** (44,700 + fianza 1,100 + 1 mes previo 1,100 + contingencia 10 % × 25,800 = 2,580, por fórmula) + fondo
  de maniobra $39,486 = **$88,966** · fondos propios $25,000 (28 %) + préstamo **$64,000** al 10 % a 7 años (cuota $13,146).
- Margen bruto **60.9 %** · mercancía 28.8 % · personal **33.8 %** ($105,943) · commissary y almacén 4.2 % · EBITDA
  $39,227 (**12.5 %**) · D&A $5,734 · intereses $6,400 · neto **$20,319 (6.5 %)** / $32,133 / $39,133.
- Equilibrio **116 eventos/año** (115.83 contable · 116.54 de caja → 117) frente a 135 → holgura **15.8 %** (caída
  absorbible **14 %**) · **DSCR mín 2.47×** · saldo mínimo **$31,627** (mes 2) · payback 2.3 años · 7 personas = 2.1 FTE,
  cobertura 138 % · seguros $5,500 · marketing $8,000.
- Pesimista (101 · $36.00 · 52) **$189,072**, resultado −$48,514 (EBITDA ≈ −$36,400) y **caja estimada −$10,040: se
  agota** (el docx §8 [99] tiene que decirlo) · optimista (169 · $44.00 · 64) $475,904 y +$126,196 (dentro de `B51` = 200).
- Los 5 umbrales del P&L (margen bruto ≥ 58 %, mercancía ≤ 35 %, personal ≤ 38 %, commissary ≤ 7 %, neto ≥ 5 %) en verde
  los 3 años.

`bp7.py gates_en --dir /tmp/pael-dry --parcial --solo G1,G3,G4,G5,G6,G7`: **TODO VERDE** (722 fórmulas; 68 tareas [11, 13,
12, 10, 12, 10]; 16 hojas Letter; 202 valores bajo DV; 8 rangos de CF; caché = referencia ES recalculada, 0 diferencias;
113 valores del caso, 0 calibraciones). Barrido de las piezas ya en EN del dry-run (GM, GRB-plan, GLB-check, GX, FIJOS,
POR_CELDA, docx fijos) contra cifras prohibidas y `RX_PAEL_NO`: 0 fugas reales (los avisos son celdas D19 aún en ES del FT,
«v1.1» / «food truck», y `Phase 2!E5`, que reescriben los redactores).

## 4. Decisiones y desviaciones de la SPEC

1. **«Solo lo que de verdad cambia» (orden del orquestador del paso 1) frente a D119/D127**: la SPEC mandaba las 272
   celdas de tarea a GPA-check y las 6 filas D19 con propuesta a GPA-plan. Para que las tandas lleven solo lo que cambia,
   nace el grupo **GLB-check** (reutilizado tal cual, como GM) y las celdas D19 con propuesta limpia van a **GRB-plan**
   (revisión). `verificar` comprueba ahora 272 celdas de tarea en GPA-check ∪ GLB-check. Recuentos: GM 312 (= SPEC) ·
   GRB-plan **98** (SPEC ≈ 77: +21 celdas D19) · GLB-check **202** · GPA-plan **109** (SPEC ≈ 130: −21 D19) · GPA-check **73**
   (SPEC 275) · GX 165.
2. **Checklist: 30 L · 35 A · 3 N** por tarea (inventario §5: 42 / 23 / 3). El inventario numeró las filas con el orden del
   BBQ ANTES de su revisión final (M2 y m9 reordenaron P1, P3 y P6); aquí se clasifica sobre las filas actuales del BBQ y
   con más «A» porque muchas notas del BBQ citan el smoker, la carne o el trailer. Por celda solo cambian **73 de 272**: las
   columnas que marca `TAREAS_PAEL` (E sola en 12 tareas, B y E en 22, B-D-E en 1, las 4 en las 3 nuevas) + `Phase 2!E15`
   («Texas», que se queda) y `Phase 3!E12` («pickup times»). La columna C pasa a «Paella chef» por transformación mecánica
   en el reuso (D125 «mecánico»): ninguna celda va a la tanda solo por eso.
3. **Calibración** (§3): ninguna; préstamo $64,000 (research ≈ $62,400). `Staffing!B17` = 50 semanas (= BBQ), no las 52
   de research: cobertura 138 % (research 144 %).
4. **Tokens**: fuera `inv_vehiculo` e `inv_adaptacion` (el «vehículo» del FT es aquí la fila de los quemadores y
   confundiría); dentro `inv_quemadores` (fila 7), `inv_paelleras` (8), `inv_propano` (9) e `inv_montaje` (20) + los del
   BBQ que siguen valiendo (`inv_almacen`, `inv_furgoneta`, `inv_furgoneta_upfit`, `inv_llc`, `inv_inspeccion`,
   `inv_software`, `inv_herramientas`). Las propuestas del docx traen `{{inv_vehiculo}}`, `{{inv_rig}}`, `{{inv_holding}}`:
   el brief avisa de que no existen.
5. **`RX_PAEL_NO`** (D128), con tres matices: (a) «stations» admite además «cooking station», «handwashing station» y
   «propane station» (la SPEC los usa en D120 y en el título de la fase 2); (b) **«induction» y «wood»/«wood-fire» valen**
   (D117: inducción en interiores, leña con permiso), aunque el `RX_BBQ_NO` heredado vetaba «induction»; (c) «Spain» queda
   permitido junto al origen, pero **`check_textos` (código común) rechaza «Spain», «Valencia» y «Spanish market»**: el
   brief dice que no se escriban. Las frases del caso BBQ «75 guests» y «$38» se vetan solo como caso («75 guests per
   event», «$38 per guest», «$38.00»), porque la mezcla de la paella tiene 25 eventos de empresa de 75 invitados a $38.
   Del ES, 18.000 y 20.000 quedan fuera de `CIFRAS_ES` (la van y un importe US plausible).
6. **Notas del docx**: la propuesta del BBQ va entera en la nota de cada ranura (no hay campo propio en el esquema común);
   el ES 2.2 del paellero solo en las 39 «adaptar» y «nueva» (en las 22 «casi literales» sobraría).
7. **D19**: las 6 filas con propuesta se quedan en su fila; la 63 es nueva (paella chef y attendant cobrados aparte,
   cafesevilla.com, leída), como pedía D122; la 68 junta el Kit estimate del propano y los desechables con el ratio de
   personal leído (miamigrillcatering.com).
8. **`cifras_caso.json`** se copia del dry-run (118 tokens); entre dos dry-runs solo cambia la marca de tiempo de `meta`.
9. **Fuera de mi alcance (paso 3/F3)**: `paella-catering-business-plan` en `PRODUCTOS_LETTER` de `censo-entregables.py` y en
   `EXCLUIDOS` de `postprocess-transversal.py` (G9 de `gates_en`); hoy se pasa con `--letter --only`.

## 5. Calculadora D123-D124 (`calculadora_pael.py` → `astro-site/public/dl/paella-catering-business-plan/paella-catering-pricing-calculator.xlsx`)

5 pestañas, **362 fórmulas**: «Pricing Calculator» (36 entradas verdes con DV + 3 en la tabla de paquetes: paquete de una
lista de 3, menu style de la lista de 8 de la hoja 2, tamaño de paellera de la lista de 7, Yes/No del tapas hour y del
sales tax, enteros, importes ≥ 0, oz de arroz 1-8, porcentajes 0-1, comisión ≤ 30 %, margen ≤ 65 %, días 1-730; salidas:
invitados por paellera, paelleras, arroz (lb), caldo (gal), propano (lb) y cilindros de 20 lb (+1 de reserva), estado de
los precios, coste por invitado del estilo, costes, precio por invitado, subtotal, service charge, impuesto, total,
depósito, saldo, comisión, margen calculado, paella chefs (paelleras ÷ 3), ayudante (desde 4 paelleras u 80 invitados) y
servers sugeridos, 4 retenciones por tramo) · «Paella Yield & Pan Sizing» (7 tamaños 18-40 in con cm: invitados por
paellera Kit —36 in = 40 · 32 = 30 · 26 = 18 de research; el resto, la tabla ES × 1.33—, aros, arroz y caldo por paellera
en lb / gal con kg / litros, propano por cocción; 8 menu styles con las oz por invitado de 11 ingredientes y el azafrán en
gramos, el coste Kit por invitado —$8.50 seafood · $7 chicken & seafood · $5 chicken & chorizo · $6 Valencian · $4 farm
vegetable · $6.50 negra · $16.50 lobster · $9 easy-eat—, el coste con TUS precios, los ingredientes sin precio, **el mínimo
del Food Code y el hot holding en columnas propias** y los alérgenos típicos con «Verify with your recipe and suppliers»;
fila verde de precios por lb —azafrán por gramo— y del arroz bomba **en blanco**; notas de *B. cereus*, sobras a la basura,
shellstock tags y alérgenos US frente a UK) · «Shopping List by Guest Count» (tu evento + 40 / 80 / 150 / 300 editables:
paelleras y quemadores, arroz, caldo, los 11 ingredientes del estilo, marisco total, limones, pan, ensalada, alioli,
propano y cilindros, platos, hielo y coolers, chafing dishes del tapas hour, paella chefs, ayudante y servers) · «3 Example
Quotes» · «Instructions» (cómo se usa, Food Code, service charge y gratuity, sales tax, cocinar en el evento y el propano,
sangría, nota UK, Kit estimates, firma, versión y aviso). docProps D20, Letter + ajuste + pie, hojas protegidas sin
contraseña.

| Ejemplo (Kit estimate; sin precios de ingredientes) | Inv. | Paelleras | Coste | Precio/inv. | Línea §8 | Subtotal | Total | Margen |
|---|---|---|---|---|---|---|---|---|
| Corporate drop-off, chicken & seafood (mín. 20) | 30 | 1 × 36 in | 403.65 | **22.50** | $22 (+2.3 %) | 675.00 | 729.00 | 40.2 % |
| Backyard paella party, seafood (mín. 20) | 45 | 2 × 36 in | 711.90 | **32.00** | $34 (−5.9 %) | 1,440.00 | 1,555.20 | 50.6 % |
| Wedding, tapas hour + 2 paella chefs, helper, 5 servers, rentals $600, service charge 10 % (mín. 50) | 110 | 3 × 36 in | 3,363.75 | **53.00** | $52 (+1.9 %) | 5,830.00 | 6,926.04 | 42.3 % |
| Hoja principal por defecto (live paella party, chicken & seafood) | 58 | 2 × 36 in | 761.40 | 26.50 | — | 1,537.00 | 1,659.96 | 50.5 % |

**Autotest** (`bp7.py calculadora`): inject_cache 362 fórmulas, 0 fallos de pycel; **509 comprobaciones** pycel + caché =
Python en las 4 pestañas de cálculo (hoja principal, tamaños, estilos y filas auxiliares, lista de la compra, 3 ejemplos y
su equivalente con tarifas) + **el estilo de langosta, el interruptor «Tapas hour?», la paellera de 26 in** (con
`set_value`) y **los precios tecleados** (en una copia del fichero: las celdas de precio están vacías) en la hoja principal;
margen ≥ objetivo, ejemplos a ±10 %, ningún precio tecleado, mínimo del Food Code y hot holding en sus columnas, aviso de
alérgenos, 0 cadenas vacías, 0 verdes bloqueadas, sin «€» ni símbolo en formatos, 0 español / no latinos / cifras
prohibidas / `RX_PAEL_NO` / anclas → **VERDE**. `censo-entregables --fail --letter --only paella-catering-business-plan`:
0 defectos; `gate-no-latinos --only`: 0; `barrido_pael`: 520 piezas, 0 fallos. sha256 (Mac = VPS)
`7550983c3ce50c51a30f8a2be2869d0a2c580d2bbdb42bf7bda6420c30e5932d`.

Decisiones de la calculadora: (a) el coste de comida provisional va **por estilo** (research §5 da el Kit por estilo), no
por paquete como el BBQ; (b) los precios de ingredientes viven en la hoja 2 y los usan todas las cotizaciones (también los
ejemplos, que por eso salen con el Kit); (c) el coste por estilo con tus precios se suma término a término y no con
SUMPRODUCT (pycel con numpy 2 devuelve un float que su ROUNDUP no sabe redondear); (d) **para el D129**: el mínimo de
«farm vegetable» cita el 3-401.13 (135 °F para vegetales cocinados para hot holding) y el del conejo dice «check your
county rules (cooking it with the chicken to 165 °F covers it)»: ninguno de los dos lo leyó la research; (e) cancelación
60 / 30 / 14 días con 50 / 75 / 90 / 100 % y depósito 50 % como Kit estimate («US caterers ask 25-50%»); (f) sin gratuity.

## 6. Comandos para seguir

```bash
# PASO 2 — redactores Sonnet (Mac, máx. 2 a la vez, istats < 62 °C; BRIEF-TRADUCTORES.md, secciones 0 y 1 + la tanda)
#   tanda 1: (a) GPA-plan + revisión GRB-plan ‖ (b) GPA-check · tanda 2: (c) pael_a ‖ (d) pael_b
B=scripts/productos-digitales/business-plans-en-7
python3 $B/bp7.py check_textos --tanda GPA-plan     # | GPA-check | pael_a | pael_b
python3 $B/bp7.py preparar_tandas && python3 $B/bp7.py check_textos --tanda GRB-plan   # tras GRB-plan.revision.json
python3 $B/bp7.py check_textos --todas
python3 $B/bp7.py verificar                          # avisa si el BBQ o el catering derivan (16 sha256)

# PASO 3 — VPS: aplicar (sin calibración), ensamblar, gates
ssh vps
cd /root/wt-paella && git checkout -q -- . && git pull --ff-only && cd scripts/productos-digitales/business-plans-en-7 && PY=/root/venv-guias/bin/python
$PY bp7.py aplicar_en --idempotencia --json /tmp/pael-real.json   # 2 xlsx en dl/paella-catering-business-plan/ + cifras_caso.json
$PY bp7.py ensamblar_docx --plan pael                             # tras pael_a + pael_b
# G9: antes, paella-catering-business-plan en PRODUCTOS_LETTER (censo-entregables) y EXCLUIDOS (postprocess-transversal)
$PY bp7.py gates_en && $PY bp7.py gates_en --autotest && $PY bp7.py ensamblar_docx --autotest --dir /tmp/pael-docx-at
$PY bp7.py calculadora --autotest && $PY bp7.py barrido            # → entregables_pael.json
/tmp/regresion-pael.sh                                            # regresión §2 (quitar bp7 de los «parciales»)
# vuelta por scp (sha256 iguales); commit desde el Mac; VPS limpio (borrar los generados sin seguimiento)
# si cambian FIJOS / POR_CELDA / zonas / grupos / pistas / FORZAR / TAREAS_PAEL: $PY bp7.py extraer_textos > /tmp/pael-ext.txt
#   y extraer_docx (VPS) y preparar_tandas (Mac); si el BBQ o el catering cambian, bp7.py verificar avisa (sha256)
```

VPS: `/dev/null` es un fichero normal (redirigir a `/tmp/*.txt`); antes de cada `git pull`, `git checkout -- .` y borrar los
ficheros generados sin seguimiento tras comprobar su sha256 (los JSON que ya están en git salen idénticos).

## 7. Riesgos para los redactores (pasos 2-3)

1. **Fuga BBQ**: las propuestas son texto del BBQ (smoker, pitmaster, carving, «pounds of meat», trailer, «pickup») y sus
   tokens (`{{inv_vehiculo}}`, `{{inv_rig}}`, `{{inv_holding}}`, que aquí no existen). `check_textos` caza el vocabulario y
   los tokens; la revisión D129 (6) lee los 4 ficheros enteros.
2. **«Spain» y «Valencia»**: `check_textos` los rechaza siempre; «Valencian paella» y «Spanish» valen. Sin tildes: Serrano
   ham, fideua, smoked paprika, Spanish tortilla.
3. **Legal sin cifras inventadas**: limited food preparation (solo California leída) y propano / carpas (solo Virginia
   leída) van como EJEMPLO con «ask your county» / «check with your fire marshal»; el arroz es TCS: ≥ 135 °F o TPHC 4 h con
   SOP escrito; sobras a la basura; el mínimo del Food Code se nombra como tal.
4. **Realismo (D118)**: 135 eventos = dueño-paella chef a tiempo completo con segundo cocinero los fines de semana, no la
   media del primer año (≈ $225K el año 1); holgura 16 % (caída absorbible 14 %); el pesimista agota la caja (−$10,040) y el
   docx lo dice. [56]: la mezcla (25 + 60 + 25 + 18 + 7 = 135) se escribe «75 guests at $38», nunca «75 guests per event».
5. **[98]**: `{{cobro_dias}}` para los cobros y `{{pago_dias}}` para los pagos a proveedores (D113).
6. **Checklist**: la tanda (b) solo ve 73 celdas; las otras columnas de cada fila son el EN del BBQ que vale: no hay que
   contradecirlas (p. ej. si la B dice «Buy…», la E no puede hablar de alquilar). La revisión final lee las 272.
7. Cifras de mercado solo de research «leída» (check_textos lo comprueba); en la D19, 4 de 14 filas son «Kit estimate» (57
   arroz, 59 invitados por paellera, 61 paelleras y quemadores, 62 marketplace) y la 68 mezcla Kit y fuente leída.
8. Si se rehace la extracción, los ids de `textos_es.json` pueden moverse y las salidas de los redactores dejan de casar.

## 8. Cierre de la F2 (24-oct, sesión Claude Code): xlsx + docx EN, gates, F3 fusionada

Tandas del paso 2 en `b58c30b0` / `12d38ab6` (`check_textos --todas` OK, las 7; GPA-plan con 14 avisos de longitud;
`GRB-plan.revision.json` con 1 corrección). Paso 3 en el VPS sobre `e2ef83b5` (alta de G9: `paella-catering-business-plan`
en `PRODUCTOS_LETTER` de `censo-entregables.py` y en `EXCLUIDOS` de `postprocess-transversal.py`, cada uno en línea propia):
- `aplicar_en --idempotencia`: préstamo **$64,000** en 1 vuelta, textos 535 + 318, faltan 0, **0 diferencias** entre dos
  construcciones, inject_cache 722 / 12 fórmulas y **0 fallos de pycel**, D15 sin fallos (holgura 15.8 %).
- `ensamblar_docx --plan pael`: G8 VERDE (131 párrafos, 10 Heading 1, 8,499 palabras).
- **Coherencia texto ↔ libro** (sin un solo arreglo de texto): (a) docx [56], la mezcla escrita (25 drop-offs de 30 a $22
  · 60 backyard parties de 45 a $34 · 25 eventos de empresa «75 guests at $38» · 18 bodas de 110 a $52 · 7 premium de 70 a
  $65) suma 135 = {{eventos_a1}} y $314,360 frente a los $313,200 del libro (−0.4 %, 57.7 invitados frente a 58); bodas 13 %
  de los eventos (18/135) y 33 % de las ventas (102,960 / 314,360); picos de mayo, junio y octubre y mínimos de enero y
  febrero = la estacionalidad con Month 1 = marzo. (b) [42] «near $225,000 in sales in year 1 (a kit estimate)» = research
  §8. (c) `pesimista_caja` = **−$10,040**: el «the cash runs out» de [58] y [99] es cierto. (d) Depósito: docx [48], [73] y
  [98] «25-50% (kit estimate), the calculator proposes 50%» = libro (`0. Assumptions!C58` «25-50%: Kit estimate»,
  `12-Month Cash Flow!O5` «not modeled») = calculadora (50 % por defecto, «US caterers ask 25-50%») = checklist
  (`Phase 1!E13` «a 25-50% nonrefundable deposit… the pricing calculator suggests 50%»). (e) Porcentajes en claro del docx
  (10 % de contingencia, 20 % de Texas, 28-35 %, 7-8 %, VAT 20 %): todos en research / SPEC (check_textos los coteja).
  Ningún gate saltó por texto; ninguna cifra ni fórmula tocada.

**Caso final** (`cifras_caso.json`, 118 tokens, **ninguna cifra distinta del dry-run** del paso 1; solo cambia la marca de
tiempo; sha256 `b354a97c99b53bde…`):
- 135 eventos × 58 invitados × $40.00 sin sales tax, con el paella chef, el personal y el service charge → ventas
  **$313,200** / $344,520 / $365,191 ($2,320 por evento, 7,830 invitados).
- CAPEX **$49,480** + fondo de maniobra $39,486 = **$88,966** · fondos propios $25,000 (28 %) + préstamo **$64,000** al 10 % a
  7 años (cuota $13,146; SBA 7(a): supera el tope de $50,000 del Microloan).
- Margen bruto 60.9 % · mercancía 28.8 % · personal 33.8 % · commissary y almacén 4.2 % · EBITDA $39,227 (12.5 %) · neto
  **$20,319 (6.5 %)** / $32,133 / $39,133.
- Equilibrio **116 eventos/año** (115.83 contable · 116.54 de caja), holgura **15.8 %** (caída absorbible 14 %) · **DSCR mín
  2.47×** · saldo mínimo $31,627 (mes 2) · payback 2.3 años · 7 personas = 2.1 FTE, cobertura 138 % · seguros $5,500 ·
  marketing $8,000.
- Pesimista (101 · $36.00 · 52) $189,072, −$48,514 y caja **−$10,040: se agota** · optimista (169 · $44.00 · 64) $475,904 y
  +$126,196. Los 5 umbrales del P&L en verde los 3 años.

| Comprobación (VPS) | Resultado |
|---|---|
| `bp7.py gates_en` (G1-G9 sobre `dl/paella-catering-business-plan/`) | **TODO VERDE** (G2 incluye `RX_PAEL_NO` y cifras prohibidas; G9 = censo-entregables + no latinos) |
| `bp7.py gates_en --autotest` · `ensamblar_docx --autotest` · `calculadora --autotest` | **20/20** · **8/8** · VERDE (509 comprobaciones) |
| `barrido_pael.py` (celdas, literales de fórmula, DV, docProps, párrafos y tablas) | 1,889 piezas · **0** `RX_PAEL_NO` / cifras prohibidas · 0 español · 0 no latinos (`entregables_pael.json`) |
| `censo-entregables --fail --letter --only paella-catering-business-plan` · `gate-no-latinos --only` | 4 ficheros, 1,096 fórmulas, **0 defectos** · 0 caracteres |
| `bp7.py verificar` | OK: 272 celdas de tarea (73 + 199) y **16 sha256 del diccionario sin deriva** (BBQ y catering) |
| Regresión §2 (FT/CAF, REST/PAN, BAR, CAT, MBAR, BBQ y PAEL completo) | TODO VERDE · 20/20 en los 7 · docx 18/18 · 16/16 · 8/8 ×5 · `check_textos` 7 / 8 / 6 / 6 / 6 / 6 / 7 OK · calculadoras CAT (136), MBAR (778), BBQ (581) y PAEL (509) VERDE |

| Entregable (`astro-site/public/dl/paella-catering-business-plan/`) | Contenido | sha256 (Mac = VPS) |
|---|---|---|
| `paella-catering-business-plan.docx` | 131 párrafos (110 con texto), 10 Heading 1, 8,499 palabras, Letter | `d7eccbf09e08f3b0192e3cd75127f1ac995a69c7f9877bd8c288682ba04fba9e` |
| `paella-catering-financial-projections.xlsx` | 9 hojas, 722 fórmulas, caso US sin calibrar | `765e496038990ff0c0fbb9c1ca711827ea24f8a5eadede4b5dc9c385acbcfe10` |
| `paella-catering-pricing-calculator.xlsx` | 5 hojas, 362 fórmulas | `7550983c3ce50c51a30f8a2be2869d0a2c580d2bbdb42bf7bda6420c30e5932d` |
| `paella-catering-startup-checklist.xlsx` | 7 hojas, 68 tareas (11/13/12/10/12/10), 12 fórmulas | `aa32db167cb0224ece1bf53e3619b64a7817481036e12978f49e1cb7efefd8c6` |

**F3 fusionada** (`origin/feat/paella-catering-business-plan-en-f3`, `a9f3c3cf` + imágenes `8c94d63f`, sin conflictos) y
**cifras de la landing** (bloque `CASO` de `astro-site/src/data/productos-en/planes/paella-catering-business-plan.ts`, ahora
«confirmado con F2-NOTAS §8 (24-oct)»):

| Clave | F3 (provisional) | **Final** |
|---|---|---|
| eventos · invitados · precio · ventas | 135 · 58 · $40.00 · $313,200 | **igual** |
| inversion · circulante · necesidad | $49,480 · $37,920 · $87,400 | **$49,480 · $39,486 · $88,966** |
| propios · prestamo | $25,000 · $62,400 | **$25,000 · $64,000** |
| neto · netoPct | $21,000 · 6.7% | **$20,319 · 6.5%** |
| equilibrio · dscr | 115 · 3.1× | **116 · 2.47×** |
| marketing · seguros · pesimista | $8,000 · $5,500 · 101 / $36.00 / 52 | **igual** (caja −$10,040) |
| ejDropoff · ejFiesta · ejBoda | $22 · $34 · $52 | **$22.50 · $32.00 · $53.00** |
| arrozOz · menuStyles · formulas | 3.25 · 8 · 700 | **igual** (libro 722 → «more than 700»; calculadora 362; 1,096 en los 3 xlsx) |

Frases de la ficha contrastadas con los ficheros (F3-NOTAS §3) y corregidas solo donde no casaban: (1) la calculadora NO
reparte los invitados en paelleras de varios tamaños: calcula las de **un** tamaño elegido → «pans for the size you pick» en
las FAQ del precio y de la paellera de 36 in, en las tarjetas de la calculadora, del pan sizing y de los precios, en el
dashboard, en el correo y en el changelog; (2) «Pans from 18 to 40 inches (45-100 cm)» → **46-100 cm** (18 in = 46 cm); (3)
el checklist pide «a **25-50%** deposit» (la calculadora propone 50 %): tarjeta del checklist y dashboard; (4) FAQ UK / CA /
AU (lección M4 del BBQ): «works in pounds, ounces and gallons, with kilograms and liters alongside on the pan sizing sheet
(1 lb = 0.454 kg; 1 gallon = 3.8 liters), degrees Fahrenheit with Celsius, pan sizes in inches with centimeters, saffron in
grams and miles»; (5) precio por unidad que no confunda: «the price you pay for each ingredient (per pound, saffron per
gram)». Sin «truck» para el vehículo (solo «paella food truck» y el Food Truck Kit). El resto casa: nota UK del docx §9,
los 3 paquetes y el «Tapas hour?», los $/lb en blanco con el Kit por estilo, 4 puestos de `Staffing`, el checklist (contrato,
plan HACCP con arroz TCS, Phase 2 con commissary agreement, condado, fire marshal, cilindros verticales y sujetos, approved
source y shellstock tags 90 días, ServSafe Manager, Thumbtack, Google Business Profile, launch tasting), «excl. sales tax;
staffing and service charge included», el pesimista que agota la caja, 135 eventos = dueño a tiempo completo con segundo
paella chef los fines de semana, depósito de clientes no modelado. `esbuild` de la ficha, del dashboard y del changelog: OK.
