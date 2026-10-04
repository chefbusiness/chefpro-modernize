# Restaurant + Bakery Business Plan Kit (EN) — F2 (entregables) · notas

> Sesión Claude Code, 4-oct-2026. **Tanda 1 de la F2**: generalización del código común de
> `../business-plans-en/` (Food Truck + Coffee Shop, PR #110) a los 4 libros nuevos, extracción y preparación de las
> tandas de traducción. Implementador único (opus), sin subagentes. Código en el Mac; todo lo que abre xlsx/docx, en
> el **VPS** (`/root/wt-bp2`, venv `/root/venv-guias`), de vuelta por `scp` con sha256 iguales. Rama
> `feat/business-plans-en-2` rebasada sobre `feat/business-plans-en` (con la ronda de arreglos `56243d65`) **sin
> conflictos**.

## 1. Cómo se generalizó (y por qué así)

**Decisión: un solo código, dos conjuntos de datos.** Los scripts de `../business-plans-en/` (extraer, aplicar, gates,
ensamblar, check, preparar) son los MISMOS para los cuatro planes; lo que cambia es el módulo de datos:

- `../business-plans-en/mapas.py` lee `BP_CONJUNTO` (por defecto `ftcaf`). Con `restpan`, al FINAL del módulo,
  `mapas_rp.instalar(M)` **sustituye** (no suma) sus datos por los de restaurante + panadería y pone
  `mapas.DATOS = business-plans-en-2/`. Todos los scripts leen y escriben sus JSON en `mapas.DATOS`.
- `bp2.py <script> [args]` fija la variable y lanza el script común: `python3 bp2.py extraer_textos`, etc.
- Datos del conjunto: `mapas_rp.py` (estructura: productos D30-D32, pestañas D33, molde RESTC D35, E2/E3, versión,
  zonas D18/D19, docx D44, grupos, reutilización) y `datos_rp.py` (contenido: FIJOS D34-D37, POR_CELDA, pistas,
  tokens D43, fijos y notas del docx, caso US D42, FORMULAS_EN).

Por qué: el riesgo para FT/CAF queda **solo** en las funciones tocadas (sus datos no cambian ni conviven con los
nuevos), y cada cambio de código es «dirigido por datos» con el valor por defecto que reproduce FT/CAF. Alternativa
descartada: añadir REST/PAN a los diccionarios de `mapas.py` (los bucles `for plan in PLANES` y los FIJOS por texto
mezclarían los dos conjuntos en cada script).

**Qué se generalizó** (todo en `../business-plans-en/`, con el valor de FT/CAF por defecto):

| Pieza | Cambio |
|---|---|
| Resolutor de pestañas | `mapas.norm_hoja()` / `hoja_es(corto, h)` / `hoja_en()`: el código y TOKENS_DOCX usan el nombre canónico («PyG 3 Años», «Financiación»…) y se resuelve a la pestaña real del libro («2. P&L 3 Años», «7. Financiación» del restaurante). `aplicar_en.fila_de`, `Cache`, `d15`, G6 y los tokens pasan por él. En FT/CAF es la identidad |
| Checklists | `MOLDE_CHECK` ('hojas' / 'cabeceras'), `COL_OK`, `FASES_CABECERA` y `contar_tareas()`: RESTC = una hoja, 7 filas-cabecera (A4, A15, A24, A33, A41, A50, A66), tareas con texto en la col. B hasta la 74, OK en la col. E (✓, —, N/A); PANC = pestañas F1-F6 (molde FT/CAF). G1 y el censo cuentan con esa función |
| E2 / E3 | `PARCHES_FORMULA` por libro (REST G14/G15; PAN G13/G14 + **E3 G10 `H10*0.04` → `H10*0`**) y `celdas_e2()` para G6 (antes G13/G14 escritas a mano) |
| D34 marca | FIJOS por texto («ChefBusiness Consultoría Gastronómica» → «AI Chef Pro»; pies «ChefBusiness.co — …» → «AI Chef Pro · aichef.pro/en/digital-products/restaurant-business-plan»; A2/A3 sin «España 2026»; `Inversión!A57`) |
| Coordenadas | `FILA_VERSION` (63/72/11/11 → E1 en A64/A73/A12/A12), zonas D18/D19 por cabecera (REST 34-45 / 49-58, PAN 35-51 / 55-67: coinciden con la SPEC), `DOCX_N_PARRAFOS`, `DOCX_ULTIMO_9`, `DOCX_RESUMEN_TOKENS`, `PRESTAMO_SEMILLA` |
| Tokens del docx | `datos_rp.tokens_rp()`: rótulos por plan («Cubiertos…» / «Transacciones…», «Marketing» PAN, ocupación = alquiler) + 14 partidas propias. REST 91 tokens (87 de celda + 4 derivados) / PAN 88 (84 + 4) |
| Grupos | `GRUPOS`, `GRUPOS_TRADUCTORES`, `GRUPOS_OVERRIDES`, `GRUPOS_DESC`, `grupo_de()`; reutilización `REUSO` (ES → EN de FT/CAF) |
| POR_CELDA | `aplicar_en.capa_fijos` escribe ahora también `mapas.POR_CELDA` (en FT/CAF está vacío) |
| Pistas | `mapas.PISTAS_EXTRA` (pistas por texto del conjunto; vacío en FT/CAF) |
| gates_en | autotest parametrizado por papeles (`mapas.AUTOTEST`: P1/P2/C1/C2 y celdas); `--parcial` (ensayo con grupos sin traducir) |
| aplicar_en | `--prestamo plan=importe` (además de `--prestamo-ft/-caf`) |

## 2. Prueba de no regresión de FT/CAF (VPS, código final `1cd48716` + estos docs)

```bash
cd /root/wt-bp2/scripts/productos-digitales/business-plans-en && PY=/root/venv-guias/bin/python
$PY aplicar_en.py --dry-run --salida /tmp/bp-gen --idempotencia --json /tmp/bp-gen.json
$PY ensamblar_docx.py --plan ft  --cifras /tmp/bp-gen/cifras_caso.json --salida /tmp/bp-gen/food-truck-business-plan/food-truck-business-plan.docx
$PY ensamblar_docx.py --plan caf --cifras /tmp/bp-gen/cifras_caso.json --salida /tmp/bp-gen/coffee-shop-business-plan/coffee-shop-business-plan.docx
$PY ../business-plans-en-2/comparar_publicados.py --dir /tmp/bp-gen --repo /root/wt-bp2
$PY gates_en.py && $PY gates_en.py --autotest && $PY ensamblar_docx.py --autotest --dir /tmp/bp-docx-at
```

| Comprobación | Resultado |
|---|---|
| 6 entregables regenerados vs publicados (`comparar_publicados.py`: sha256 de cada miembro del zip, `docProps/core.xml` sin las 2 fechas) | **6/6 IDÉNTICOS**. El sha256 del fichero entero difiere por construcción (openpyxl y python-docx sellan la hora de guardado y el zip la de cada miembro): también difería con el código SIN tocar (línea base del mismo día en `/root/wt-bp2base`, mismos canónicos) |
| `cifras_caso.json` regenerado vs versionado (sin `meta`) | IGUAL |
| `aplicar_en.py --idempotencia` | 0 diferencias; inject_cache 0 fallos de pycel |
| `gates_en.py` sobre `dl/` (G1-G9) · `--autotest` | TODO VERDE · 20/20 |
| `ensamblar_docx.py --autotest` | 18/18 |
| `extraer_textos.py` + `extraer_docx.py` en ftcaf a `/tmp` vs los JSON versionados (sin `meta`) | textos_es, censo_es (sin la clave nueva `tareas_por_fase`), docx_es_ft, docx_es_caf IGUALES |
| `mapas.py` | 0 errores |

Canónicos (iguales a los publicados): FT projections `68a501c613ca27f9…` · FT checklist `0cb52c8f2868c4ea…` · FT docx
`0dfbbbd4e5ae22bd…` · CAF projections `9e7dcc450feab386…` · CAF checklist `8972369aaafb81af…` · CAF docx
`a48fc0f517e44ac0…`. Observación: `preparar_tandas.py` en ftcaf ya NO reproduce las `tandas/*.entrada.json` versionadas
de FT/CAF, y no por este cambio: la ronda de arreglos del #110 cambió FIJOS (m8, B1) y añadió 5 tokens después de
generarlas. Son entradas ya consumidas: se dejan como estaban.

## 3. Extracción de restaurante + panadería (`bp2.py extraer_textos` / `extraer_docx`, VPS)

**Censo** (= F1-inventario-delta §0): RESTP 9 hojas · 729 textos · 772 fórmulas · 430 con hoja · 24 DV · 70 CF · 15
merges · 180 verdes = desbloqueadas · RESTC 2 · 333 · 2 · 1 DV · 2 CF · 10 merges · 64 verdes · **64 tareas
10/8/8/7/8/15/8** · PANP 9 · 709 · 737 · 423 · 23 · 68 · 5 · 154 · PANC 7 · 383 · 12 · 6 · 12 · 6 · 66 · **66 tareas
11/12/12/10/11/10**. 32 fórmulas con texto (16 + 16).

**Cadenas** (`textos_es.json`, 1.288 cadenas, 2.262 apariciones):

| Grupo | Cadenas | Palabras | Qué es |
|---|---|---|---|
| **GM** | 391 | 4.294 | REUTILIZADAS: idénticas a una común de FT/CAF; su EN sale de `../business-plans-en/textos_en/GM.json` → `textos_en/GM.json` (lo escribe `bp2.py preparar_tandas`). No van a los traductores |
| **GN** | 24 (22 con `propuesta_en` de GCAF) | 280 | Nuevas comunes a REST y PAN |
| **GREST** | 384 (28 con propuesta: 24 GCAF + 4 GFT) | 3.444 | Solo restaurante; 83 celdas de tabla D18/D19 |
| **GPAN** | 385 (12 con propuesta: 7 GCAF + 5 GFT) | 5.126 | Solo panadería; 120 celdas de tabla |
| GX | 104 | 504 | No se traduce (pestañas, CLAVES, FIJOS, POR_CELDA, versión, pie, docProps) |

Para los traductores: **GN + GREST ≈ 3,7 K palabras** y **GPAN ≈ 5,1 K**, de las que 62 cadenas llevan propuesta
(revisar contexto). La SPEC delta estimaba 344/340 nuevas + 6 GN + 85 reutilizables: la diferencia es que las tablas
D18/D19 van celda a celda (un id por celda) y que solo se reutilizan cadenas de tratamiento «traducir» (las de tabla,
nunca).

**Docx** (`docx_es_rest.json` / `docx_es_pan.json`; extraer_docx VERDE, 0 multi-run, Letter): REST 148 párrafos (126
con texto), traducibles 75 / 6.663 palabras → **rest_a 31 párrafos / 3.148 · rest_b 44 / 3.515**; PAN 131 (110),
traducibles 62 / 6.725 → **pan_a 29 / 3.233 · pan_b 33 / 3.492**. Encabezados = los del inventario; fijos del
ensamblador (portada, aviso, índice, cierre: REST 4 líneas de producto, PAN 2 con dos productos cada una).

**Tandas** (`tandas/*.entrada.json`): GN, GREST, GPAN, rest_a, rest_b, pan_a, pan_b + `BRIEF-TRADUCTORES.md` propio
(lo común sigue en `../business-plans-en/BRIEF-TRADUCTORES.md` §0). `bp2.py check_textos --todas`: GM OK (0 errores, 8
avisos de longitud heredados); las otras 7, «falta» hasta que escriban los traductores.

## 4. Decisiones y desviaciones

1. **GM se reutiliza tal cual** (391), salvo una cadena: «Hojas de reclamaciones oficiales y su cartel anunciador» tenía
   en FT/CAF el EN «Commissary agreement signed and a copy on file» (sustitución propia del food truck, que **también
   se publicó en el checklist de la cafetería**, Phase 2: un coffee shop no firma un commissary agreement →
   observación para la próxima versión de CAF). Aquí va por celda (`POR_CELDA`, SPEC delta §3): RESTC B52 «Consumer
   advisory and allergen notice on the menu» y PANC F2!B13 «Ingredient and allergen labels for packaged and wholesale
   products». Tercera celda por `POR_CELDA`: **RESTC Instrucciones!A5** (mismo ES que PANC A5, pero la DV de RESTC es
   ✓, —, N/A: D35/I8).
2. **Las 62 coincidencias con GFT/GCAF** no se aceptan a ciegas: van a su grupo (GN/GREST/GPAN) con `propuesta_en` y
   `propuesta_de`; el traductor la copia o la adapta (SPEC delta §5).
3. **FORMULAS_EN** (32): 23 derivadas automáticamente de su gemela FT/CAF (`derivar_formulas.py`: mismo esqueleto de
   literales y forma; mapa de referencias posición a posición, función y completo) y 9 escritas a mano
   (`formulas_rp_manual.py`, con la misma redacción y referencias del ES: RESTP C50, D13, D55, A29; PANP C9, D28, D38,
   F13, A26). `formulas_rp.json` las guarda; `datos_rp` las carga. `bp2.py mapas` cruza: 0 literales sin EN.
4. **FIJOS nuevos** (D34, D37, I9): títulos y pies del restaurante, «Liquor license + permits (non-quota state
   example)» (`1. Startup Costs!A42`), «Startup Costs — US example (2026)» (PAN A2), «Sales tax rate on alcohol served
   at the counter» (PAN B63), «Tax-exempt share of the line (%)» (PAN H4, D36). La nota de la licencia (D37: «from $50
   to $300,000+…») **no cabe en su fila**: `D42` está vacía en el ES y escribirla sería una celda nueva (G1 solo admite
   E1). Va en la fila 56 de la tabla D19 (pista: sustituye la «tasa de cierre» sin fuente, I10), en §9 del docx y en la
   FAQ de la landing. Fila 57 → prime cost 60-65 % (restaurant365).
5. **Caso US base (D42) ya en `VALORES_EN`** (222 celdas, research delta §7, para que los traductores vean `valor_us`
   y la tanda de `aplicar_en` arranque calibrando): desviaciones de research: **tarjeta 3.5 %** (no 2.9 %: regla M1
   de la revisión final de FT/CAF, `REGLAS_US['tarjeta']`); **PAN fila 9 «Proyecto técnico + certificación» = 6,000
   [kit estimate]** (research da 18 partidas para 19 filas); **REST aforo B51 = 60** (concepto de research §7); el
   resto que research no fija se conserva del ES (crecimiento, varios, rampa, meses de fondo, imprevistos, B60/B61,
   B67, techo de rotaciones `3. Break-Even!B26` = 3). Escenarios con las proporciones del ES (REST 91/125/148 covers ·
   $24.46/$28/$28.46 · 300/310/320; PAN 140/210/233 · $7.64/$10/$10.91 · 300/310/320). `CALIBRACION_D15` vacía.
6. **Pistas** (`PISTAS_EXTRA`): las equivalencias de SPEC delta §3 por texto (LLC, articles, MEP, zoning, campana UL
   300, plan review, terraza, liquor license, hojas de reclamaciones, desperdicio, carteles, USPTO, Indeed…), covers /
   transactions, propinas (D38), panadería comercial frente a cottage food (D39). Por celda: A8 de Instrucciones (sin
   divisores 1,10/1,04), PAN A12 (Word = cifras del Excel), O5 de Tesorería, F10 de la col. H (D36), C62/C63 del
   alcohol (D37), A29 de Staffing (D38) y las filas 56-57 de la D19 del restaurante.

## 5. Ensayo de la tanda siguiente (dry-run `--parcial`, VPS) y riesgos para `aplicar_en`

`bp2.py aplicar_en --dry-run --parcial --salida /tmp/rp-dry` (GM reutilizado; lo no traducido queda en ES) monta los 4
libros sin abortar: E2 2 (REST) y 3 (PAN, con E3), 16 FORMULAS_EN por plan, 71/9/51/5 FIJOS, 118/104 valores; préstamo
por punto fijo en 3 vueltas (**REST $399,000 · PAN $197,000**); inject_cache 772/2/737/12 fórmulas, 0 fallos de pycel.
`bp2.py gates_en --dir /tmp/rp-dry --parcial --solo G1,G3,G4,G5,G6,G7`: **TODO VERDE** (G1: 64 tareas RESTC por
fila-cabecera y 66 PANC; G6: caché = referencia ES recalculada, 0 diferencias). `bp2.py ensamblar_docx --autotest`:
**16/16** (G8 con EN sintético en los dos planes). Caso base sin calibrar:

| | Restaurant | Bakery |
|---|---|---|
| Ventas año 1 · margen bruto · personal · alquiler | $1,085,000 · **64.8 %** (umbral 65 %: ámbar) · 30.9 % · 7.7 % | $651,000 · 62.7 % · 33.9 % · 7.7 % |
| Neto año 1 · DSCR mín · saldo mín · cobertura · holgura de caja | 7.3 % · 2.41× · $124,118 · 106.9 % · 20.2 % | 6.0 % · 2.44× · $76,772 · 138.0 % · 16.9 % |

Riesgos y pendientes para la tanda de `aplicar_en.py` (opus, VPS):

1. **Margen bruto REST 64.8 % < 65 %** (ámbar los 3 años): una palanca D15 (p. ej. food cost de comida 30 → 29 %, o
   bebida 24 → 22 %, dentro de research §4) y anotarla aquí con la celda exacta (`CALIBRACION_D15`; G7 lee **este**
   fichero). PAN holgura 16.9 % (justa sobre 15 %) y neto 6.0 % (sobre el 5 % de D41).
2. **Cobertura PAN 138 %**: plantilla de research (5.55 jornadas) holgada frente a 12 h × 1.5 + producción 4 h × 2; no
   suspende D15, pero un prestamista lo verá como sobredimensionado. Revisar con la calibración.
3. Préstamo REST ≈ $399K con fondos propios $130K (25 %): coherente con D40 (SBA 7(a) a 10 años); el docx lo citará
   por token.
4. `gates_en --autotest` en restpan necesita la copia limpia en verde (G2 con los textos traducidos): correrlo tras las
   tandas. Las mutaciones ya están parametrizadas (RESTC: «tarea borrada» vacía la col. B de la primera tarea).
5. SPEC §7.6 heredado: los 2 slugs en `EXCLUIDOS` de `postprocess-transversal.py` y en `PRODUCTOS_LETTER` de
   `censo-entregables.py` (G9). No se ha tocado.
6. Alto de filas: el EN de las notas largas del restaurante (col. D de la inversión, notas de RESTC col. F) puede
   necesitar `capa_altos`; ya actúa sola, pero la verificación humana a 360 px y en Excel sigue siendo la última.
7. Testimonios de las fichas (R12) y afirmaciones R1-R11: son de la F3 (fuera de esta tanda).

## 6. Comandos

```bash
# VPS (openpyxl / python-docx)
ssh vps
cd /root/chefpro-modernize && git fetch origin && git worktree add --detach /root/wt-bp2 origin/feat/business-plans-en-2
cd /root/wt-bp2/scripts/productos-digitales/business-plans-en-2 && PY=/root/venv-guias/bin/python
$PY bp2.py extraer_textos > /tmp/ext.txt && $PY bp2.py extraer_docx > /tmp/ed.txt && $PY bp2.py mapas
$PY derivar_formulas.py                       # solo si cambian el censo o las fórmulas (escribe formulas_rp.json)
$PY bp2.py aplicar_en --dry-run --parcial --salida /tmp/rp-dry && $PY bp2.py gates_en --dir /tmp/rp-dry --parcial --solo G1,G3,G4,G5,G6,G7
# vuelta: scp de censo_es.json, textos_es.json, docx_es_*.json (y textos_en/GM.json + tandas/ si se regeneran)
# limpieza: cd /root/chefpro-modernize && git worktree remove --force /root/wt-bp2
# Mac (solo JSON)
python3 bp2.py preparar_tandas && python3 bp2.py check_textos --todas
# No regresión de FT/CAF (VPS): ver §2
```

En el VPS `/dev/null` es un fichero normal: redirigir siempre a `/tmp/*.txt`.

## 7. Tanda 2 (4-oct, sesión Claude Code): `aplicar_en` real + calibración D15 + gates + docx + cifras de landing

Implementador único (opus). Todo lo que abre xlsx/docx, en el VPS (`/root/wt-bp2t2`, venv `/root/venv-guias`); de vuelta
por `scp` con sha256 iguales. Se arrancó con todo lo aprendido en la ronda de arreglos de FT/CAF
(`../business-plans-en/F2-NOTAS.md` §8): tarjeta al 3.5 % combinado (`B18`), préstamo = fila 7 con rótulos B1 (FIJOS
comunes), `B58` = 1, 25 % de C corp, pagas mensuales (m8), notas C18/C21/C31/C52/C58 ya en GM.

### 7.1 Calibración D15 (`datos_rp.CALIBRACION_D15`; G7 exige que cada celda esté citada aquí)

Caso de research §7 tal cual (dry-run completo, sin `--parcial`): REST margen bruto **64.8 %** (umbral D41 65 %: ámbar
los 3 años), todo lo demás en verde; PAN todo en verde pero cobertura de horas **138 %**. UNA palanca por plan:

| Celda | Research §7 | Calibrado | Por qué |
|---|---|---|---|
| RESTP 0. Supuestos!B13 | food cost comida 30 % | **29 %** | Dentro del 25-35 % de research §4 (Papaya) y de la fila 51 de la tabla D19. Margen bruto 64.8 → **65.5 %** (verde los 3 años); neto año 1 7.3 → 7.9 %; holgura 20.2 → 21.5 %. Ticket, volumen e inversión intactos (el préstamo no se mueve: depende de la inversión y de los fijos). Descartado bebida 24 → 22 % (research no da rango de bebida) y bajar consumibles o el 2 % de imprevistos (quita prudencia) |
| PANP Personal!B21 | 1.5 personas a la vez en el servicio | **2** | La plantilla NO sobra: 5.56 FTE para $651K de ventas son $117K por FTE (magra) y el personal es el 33.9 % de las ventas, dentro del 24-40 % de Toast. Lo que estaba mal era la comprobación: 210 transacciones/día con rincón de café piden 2 personas en el mostrador durante las 12 h. Cobertura 138 % → **112 %** (el 12 % restante es la producción de día para el mayorista, que la comprobación no cuenta). No cambia ningún coste. Descartado subir las horas de producción antes de abrir a 8 (contradice el arranque 4-5 am de la fila 64 de la tabla D19) |

**PAN, holgura 16.9 % y neto 6.0 %: se quedan.** Pasan D15 (≥ 15 %) y D41 (≥ 5 %), y una palanca de ingresos solo para
ganar colchón haría el ejemplo menos creíble: el neto ya está por encima del 3-5 % típico del sector (Toast) y el EBITDA
del año 2 (18.4 %) ya rozaba el techo del rango de la tabla. Riesgo anotado: cualquier coste nuevo que añada una revisión
la acerca al 15 %.

### 7.2 Otros cambios de datos y una excepción estructural nueva (E4)

| Qué | Antes | Ahora | Por qué |
|---|---|---|---|
| RESTP `0. Supuestos!B51` (aforo, `VALORES_EN`) | 60 | **68** | La inversión presupuesta «15 tables × 4 chairs» + «Bar stools (8 units)» y el rótulo A51 dice «seats at tables + bar»: 60 + 8. Rotaciones implícitas 2.1 → **1.8**/día; las del equilibrio de caja, 1.5 (techo 3). El docx usa el token `aforo` |
| **E4** · RESTP `5. Personal!C13` y PANP `Personal!C11` (`PARCHES_FORMULA`) | `SUM(C6:C12)` / `SUM(C5:C10)` | `SUMPRODUCT(B…,C…)` | El total de la columna FTE sumaba el FTE POR PERSONA aunque varias filas tienen 2-3 personas: «10 people, 5.45 FTE» (REST) y «8 people, 4.22 FTE» (PAN), cuando las horas contratadas de la propia hoja dan **7.95** y **5.56** (÷ 2,000 h). Un CPA lo ve en la misma pestaña, y el docx lo citaba 4 y 3 veces. En FT/CAF no pasa (todas sus filas son de una persona). G1 lo admite porque compara contra el ES parcheado con `PARCHES_FORMULA` (como E2/E3) |
| `Staffing!A28` (los dos, override por celda de c0422) | «FTE is the share of a full-time week» | + «for each person… the TOTAL row multiplies it by the people in each position» | Acompaña a E4 (`textos_en/overrides_GREST.json` / `overrides_GPAN.json`) |
| RESTP `5. Personal!A11` (override de c0398) | «Weekend extra» | **«Dishwasher / weekend extra»** | Es el friegaplatos de 0.75 FTE de research §7 y el docx lo llama «weekend dishwasher»; PAN conserva «Weekend extra» |
| Token `consumibles_pct` | `pct0` | `pct1` | El 1.5 % del restaurante salía «2%» en el docx (PAN: «3.0%») |
| Token nuevo `prime_cost_pct` (derivado: `cogs_pct + personal_pct`) | — | REST **58.4 %** | El docx REST cita tres veces el 60-65 % de Restaurant365: ahora dice también el del caso y por qué queda algo por debajo (la bebida cuesta menos que la comida) |

### 7.3 Textos revisados contra el caso calibrado (tablas D19, notas y docx)

- REST D19: ticket 25-40 (caso $28 → $30.24 con impuesto), alquiler ~7,000 (= caso), food cost 25-35 % (29 %), personal
  25-33 % (30.9 %), neto ≥ 5 % (7.9 %), equilibrio en 12 meses (año 1 sí): **sin contradicción**. Fila 55 (c0527):
  «(median 375,000)» → **«(survey median 375,500)»**, la cifra exacta que confirmó el orquestador; el docx §1 (rest_a 41)
  decía «$375,000, so our plan sits within the range owners actually report» (una mediana no es un rango y el total del
  caso es $528,696): ahora «$375,500; our startup costs of {{capex}} ($388,700) sit close to that figure, and the working
  capital reserve comes on top». Prime cost (fila 57, 60-65 %): el caso da 58.4 % → explicado en el docx (rest_b 108).
- PAN D19: **fila 57 «Beverage cost: coffee 25-30 %»** contradecía el 22 % del caso (research §7) y la nota F11 del P&L
  (c0943) lo repetía con «the cost is high»: las dos pasan a **20-30 %** (kit estimate). **Fila 65 «EBITDA target (year 2)
  10-18 %»**: el caso da 18.4 % en el año 2 → **10-20 %**. Ticket 7-12 ($10), personal 24-40 % (33.9 %), alquiler ≤ 10 %
  (7.7 %), margen bruto ≥ 60 % (62.7 %): sin contradicción.
- Docx REST: §8 (rest_b 108) decía que el coste de mercancía de 27.5 % incluía los consumibles (es solo comida + bebida) →
  reescrito: COGS 27.5 %; con consumibles 1.5 %, tarjeta 3.5 % y la línea de imprevistos, margen bruto 65.5 %. Escenario
  pesimista (rest_b 110): caja estimada −$7,642 → «the working capital reserve would run out before the year ends» (m1 de
  FT/CAF). Organigrama (rest_b 99): fuera el «floor lead» (no hay jefe de sala en Staffing, R5) → «on each shift, a lead
  server or bartender».
- Docx PAN: §8 (pan_b 100) el mismo «Together, cost of goods is 28.8 %» con consumibles y tarjeta dentro → reescrito;
  pesimista (pan_b 103) con su caja estimada (−$63,796) y la misma advertencia; §3 (pan_a 58) **fuera la cita de Zenind**
  ($50-100K+ / $75-150K+): no se pudo abrir la fuente (timeout) ni la confirmó el orquestador → redacción cualitativa. Toast
  3-5 % (pan_a 51) se queda: confirmada.
- Cifras de mercado que quedan en los docx: $375,500 (RestaurantOwner.com vía DoorDash), prime cost 60-65 %
  (Restaurant365), 3-5 % (Toast), tip credit $2.13 / $5.12 y los 7 estados (DOL), $7.25 (DOL), UK (gov.uk). Todas con
  fuente en research o confirmadas.

### 7.4 Caso base final (caché de los xlsx EN = `cifras_caso.json`)

| | Restaurant | Bakery |
|---|---|---|
| Caja total necesaria (CAPEX + fondo de maniobra) | **$528,696** ($388,700 + $139,996) | **$266,709** ($182,500 + $84,209) |
| Fondos propios + préstamo (10 %, 10 años, sin interest-only) | $130,000 (25 %) + **$399,000** | $70,000 (26 %) + **$197,000** |
| Volumen × ticket × días · ventas año 1 | 125 covers × $28.00 × 310 · **$1,085,000** | 210 transactions × $10.00 × 310 · **$651,000** |
| Food cost · COGS · margen bruto | 29 % / 24 % · 27.5 % · **65.5 %** | 30 % / 22 % · 28.8 % · **62.7 %** |
| Personal · ocupación · prime cost | 30.9 % · 7.7 % · 58.4 % | 33.9 % · 7.7 % · — |
| EBITDA año 1 · neto años 1/2/3 | $190,591 (17.6 %) · $85,240 (7.9 %) / $134,419 / $165,663 | $91,041 (14.0 %) · $38,744 (6.0 %) / $71,907 / $92,427 |
| DSCR mínimo · saldo mínimo de caja | **2.50×** · $124,652 (mes 2) | **2.44×** · $76,772 (mes 2) |
| Equilibrio contable / de caja · holgura | 106 / 103 covers/día · **21.5 %** | 184 / 180 transactions/día · **16.9 %** |
| Plantilla · cobertura de horas | 10 personas = 7.95 FTE · 107 % | 8 personas = 5.56 FTE · 112 % |
| Payback del proyecto / sobre CAPEX | 2.7 / 2.1 años | 2.6 / 1.9 años |
| Pesimista: ingresos · resultado · caja estimada | $667,758 · −$159,640 · −$7,642 | $320,880 · −$155,327 · −$63,796 |

Todos los semáforos del P&L en verde los tres años en los dos planes; ningún sueldo bajo el suelo (el más bajo, $15.60/h).

### 7.5 Fichas de landing, changelog y correos (revisados contra los ficheros finales)

- TODO_CIFRA rellenados (formato US): REST caja $528,696, licencia de alcohol **$15,000** (la fila
  `1. Startup Costs!B42`, ejemplo de estado sin cupo), ticket $28.00 / margen bruto 65.5 % / equilibrio 106 covers; PAN
  caja $266,709, ticket $10.00 / 62.7 % / 184 transacciones. Comentarios TODO fuera.
- **B1** (también en las fichas nuevas): FAQ del prestamista, grid «Financing Plan» y `why` «Lender-Ready Format»
  («covering SBA 7(a) loans and SBA Microloans» → el cuadro y el DSCR cubren el préstamo principal; Microloan, inversores y
  subvenciones como otras fuentes sin amortizar), correos y changelog. **Ojo: las fichas de FT y CAF del #110 conservan
  esa frase en `why.reasons[3]`** (la ronda B1 corrigió FAQ y grid, no esa tarjeta): queda para el orquestador. Hub
  (`DigitalProductsHubPage.astro`), tarjeta REST: «SBA 7(a) and Microloan financing with DSCR» → «Loan schedule and DSCR
  (bank or SBA 7(a))», como la de FT.
- **m19**: bono 1 (guía de permisos = §9 + fases del checklist) «Included in the plan»; total **$158** = kit $129 + bono 2
  $29. **M3**: fuera «(regular price $129)» de los 2 correos.
- Puestos: los rótulos reales de `Staffing` (REST: general manager / owner, head chef, line cooks, servers / bartenders,
  part-time servers, dishwasher / weekend extra, vacation and day-off relief; PAN: head baker / owner, baker, bakery
  assistant, counter staff / baristas, weekend extra, vacation and day-off relief). Conteos comprobados: 9 hojas, 772 / 737
  fórmulas en los planes («more than 700»), 64 tareas en 7 fases (10/8/8/7/8/15/8) y 66 en 6 (11/12/12/10/11/10).
- Changelog 2.2: «12 monthly salaries a year (the model's pay count, not your payroll frequency)» (m8), financiación B1,
  PAN «square feet and pounds» (el libro PAN tiene libras: amasadora 55-110 lb, producción en lb; no tiene galones).

### 7.6 Gates, hashes y comandos

| Comprobación (VPS, `/root/wt-bp2t2`) | Resultado |
|---|---|
| `bp2.py aplicar_en --idempotencia` | préstamo por punto fijo en 3 vueltas (REST $399,000 · PAN $197,000); **0 diferencias**; inject_cache 772/2/737/12 fórmulas, 0 fallos de pycel; D15 sin fallos |
| `bp2.py gates_en` (G1-G9) | **TODO VERDE**: G1 64 tareas [10, 8, 8, 7, 8, 15, 8] y 66 [11, 12, 12, 10, 11, 10], 772/737 fórmulas · G2 2,497 textos · G3 27 hojas Letter · G4 398 DV · G5 11 CF · G6 0 diferencias con la referencia ES recalculada · G7 222 valores, 2 calibraciones citadas · G8 los 2 docx · G9 censo-entregables 0 defectos y 0 no latinos |
| `bp2.py gates_en --autotest` · `bp2.py ensamblar_docx --autotest` | **20/20** · **16/16** |
| `bp2.py ensamblar_docx --plan rest` / `--plan pan` | G8 VERDE los dos (pan_b de la tanda Sonnet, ya commiteada, con 2 párrafos corregidos aquí: 100 y 103) |
| Regresión FT/CAF (`BP_CONJUNTO` por defecto): `aplicar_en --dry-run --idempotencia`, docx ft/caf, `comparar_publicados.py`, `gates_en`, `--autotest` | **6/6 IDÉNTICOS** en canónico (los 6 sha256 canónicos de §2) · `cifras_caso.json` FT/CAF igual · 0 diferencias · TODO VERDE · 20/20 |
| Mac: `bp2.py mapas` · `check_textos --todas` · `tienda-gate.py` | 0 errores (97 tokens) · las 8 tandas OK · **verde** (ya sin TODO_CIFRA) |
| `gate-flujo-postpago.py --offline --only <slug>` | solo el Payment Link pendiente de John (y «no trackeado» hasta el commit) |

sha256 (Mac = VPS):

```
0dbb9332fae8f762…  restaurant-business-plan/restaurant-business-plan.docx
a251816dd9302b96…  restaurant-business-plan/restaurant-financial-projections.xlsx
b1882317e5348107…  restaurant-business-plan/restaurant-opening-checklist.xlsx
0d4ed36232321d41…  bakery-business-plan/bakery-business-plan.docx
d6c0125cac44a267…  bakery-business-plan/bakery-financial-projections.xlsx
60b2e24567eb2e9f…  bakery-business-plan/bakery-opening-checklist.xlsx
a32ad833040d5a24…  business-plans-en-2/cifras_caso.json
```

```bash
# VPS
cd /root/chefpro-modernize && git fetch origin && git worktree add --detach /root/wt-bp2t2 origin/feat/business-plans-en-2
cd /root/wt-bp2t2/scripts/productos-digitales/business-plans-en-2 && PY=/root/venv-guias/bin/python
$PY bp2.py aplicar_en --idempotencia --json /tmp/rp-real.json      # 4 xlsx en dl/<slug>/ + cifras_caso.json
$PY bp2.py ensamblar_docx --plan rest && $PY bp2.py ensamblar_docx --plan pan
$PY bp2.py gates_en && $PY bp2.py gates_en --autotest && $PY bp2.py ensamblar_docx --autotest --dir /tmp/rp-docx-at
# regresión FT/CAF: §2 de este fichero
# vuelta: scp de dl/restaurant-business-plan/*, dl/bakery-business-plan/* y cifras_caso.json (sha256 iguales)
```

### 7.7 Riesgos

- **PAN holgura 16.9 %** (D15 ≥ 15 %): pasa, pero cualquier coste que añada una revisión la acerca al límite. Si hiciera
  falta, la palanca prevista es la de research (transacciones en pasos de 5, hasta 230), no el ticket.
- **REST prime cost 58.4 %**, algo por debajo del 60-65 % de referencia: declarado en el docx (rest_b 108). La plantilla no
  incluye beneficios sociales (seguro médico), solo cargas del 10 %.
- **E4 amplía la lista de excepciones estructurales** (SPEC delta §2.1). Es el único cambio de fórmulas fuera de E1-E3;
  G1 lo admite porque compara contra el ES parcheado.
- La celda de la licencia de alcohol ($15,000) es un ejemplo de estado sin cupo: lo dicen la fila 56 de la tabla D19, el
  docx §9 y la FAQ.
- `docx_en_pan_b.json`: 2 párrafos (100 y 103) corregidos sobre la versión ya commiteada de la tanda Sonnet; `check_textos`
  sigue OK.
- Fichas FT/CAF (#110): `why.reasons[3]` aún dice «covering SBA 7(a) loans and SBA Microloans» (B1 a medias).
- Alto de filas con el EN más largo (notas de `0. Assumptions` y de los checklists): `capa_altos` actúa sola; la
  verificación humana en Excel y a 360 px sigue siendo la última palabra.
