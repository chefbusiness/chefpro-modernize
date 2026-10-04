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

## 8. Ronda de arreglos (4-oct, sesión Claude Code) — la única tras `REVISION-FINAL.md`

Implementador único. Solo textos: **ninguna fórmula, valor ni fila nueva** (G1 sigue con 772/737 fórmulas y 64/66
tareas; caché numérica de los 4 libros idéntica celda a celda; `cifras_caso.json` igual sin `meta`). Todo lo que abre
xlsx/docx, en el VPS (`/root/wt-bp2fix`, ya borrado); de vuelta por `scp` con sha256 iguales. Antes, en la rama del #110,
el FHRS 0-5 de FT/CAF (`9fa48603` + `f8d10072`, nota en `../business-plans-en/F2-NOTAS.md` §8), traído aquí con
`git pull --rebase` sin conflictos.

**Mecanismo (para la próxima vez):** `POR_CELDA` solo actúa sobre apariciones marcadas `regenerar` en `textos_es.json`,
así que añadir una celda exige **re-extraer** (`bp2.py extraer_textos`, VPS). Diff de la re-extracción comprobado: solo
las 5 apariciones nuevas pasan a `regenerar` (+ `tratamientos`) y, en `censo_es.json`, el `fmt` de `consumibles_pct`
(pct0 → pct1, el cambio de token de §7.2 que nunca se había re-extraído; cosmético: `ensamblar_docx` toma el formato de
`TOKENS_DOCX`). Para UNA celda de una cadena compartida basta un override (`textos_en/overrides_G*.json`, una entrada por
id y fichero, sin re-extraer). Una cadena con TODAS sus apariciones en `POR_CELDA` pasaría a GX y descuadraría los JSON:
por eso C9 va por override.

### 8.1 Arreglado

| Id | Qué se hizo | Dónde |
|---|---|---|
| **M1** | Fila 17 (fase 2) = «Sign the commercial lease and file the liquor license application right after (state alcohol agency + local approval)»; F17: la solicitud pide acreditar el local, presentarla al firmar. Fila 60 (fase 6) = «Liquor license issued and posted before opening, with age-restriction signage»; D60 «Start in Phase 2: often 3-12 months»; F60 «Applied for in Phase 2…», cupo, formación de servicio responsable, cartel de edad y «serve no alcohol until the license is issued». Docx §9 [119] «often 3-12 months, so we file the application right after signing the lease»; §10 [128] reescrito fase a fase contra el checklist real (también arregla: seguro en fase 6 y no en la 1, soft opening en fase 5 y no en la 7, CO y health permit en fase 2). FAQ de la landing («Apply for your liquor license early»), §10 [131] y tarjeta del grid / dashboard / changelog / correo («lease and liquor license application» en fase 2, «liquor license issued and posted» en fase 6): dicen lo mismo | RESTC B17/F17 (c0714/c0715), B60/F60 (c0824/c0825) en GREST; D60 por `POR_CELDA`; docx rest_b 119/128; ficha, `RestaurantBusinessPlanDashboard.tsx`, `productos-changelog.ts`, correo |
| **M2** | RESTP `Instructions!A7` con el texto de la panadería y las pestañas numeradas: «…the other funding sources on "7. Financing" (rows 8-11 count as sources but are not amortized: your bank or SBA 7(a) loan goes in "Loan requested" on "0. Assumptions")» | GREST c0432 |
| m1 | RESTC C47/C48/C74 → «Team» (la cadena «Equipo» sigue siendo «Equipment» en A27-A30) | `POR_CELDA` |
| m2 | Docx REST [107] y PAN [103]: «(a C corporation example; pass-through owners set it to 0 and pay tax on the profit personally)» | docx |
| m3 | Docx REST [115]: el EIN «is needed to hire employees and to file federal employment and excise tax returns» | docx |
| m4 | FHRS **0-5**: RESTC F21 (c0730), docx REST [122] («from 0 to 5», FHIS ya estaba) y PAN [110] (+ «Scotland uses the Food Hygiene Information Scheme») | GREST, docx |
| m5 | Docx REST [101]: «the head chef and a lead server join» | docx |
| m6 | Docx REST [101]: «The model starts payroll on opening day, so these pre-opening wages are not a line of their own: they come out of the working capital reserve» (el fondo es 3 meses de fijos, $139,996; saldo mínimo $124,652). Sin tocar valores | docx |
| m7 | Decisión del orquestador: el alquiler del caso ($7,000/mes) es el **coste total de ocupación** (renta base + NNN/CAM estimados). C24 y docx [81] lo dicen así y piden sumar los cargos si el contrato solo da la renta base | GREST c0042, docx rest_b 81 |
| m8 | RESTP `Instructions!C51/C52` (fuente del food cost 25-35 % y del personal 25-33 %): «Papaya (papaya.co.th)» → **«Kit estimate»**. Restaurant365 solo confirma el prime cost 60-65 % (fila 57), no esos dos rangos. La justificación de `CALIBRACION_D15` en §7.1 cita «research §4 (Papaya)» como historia; la fila ya no lo publica | GREST c0515/c0518 |
| m9 | Bono 2 REST «US Industry Benchmarks (Sourced)» (título, item del CTA, `bonusTotalLabel`, comentario de cabecera) y desc con las filas reales de la tabla (ticket, alquiler, food cost, personal, prime cost, inversión, licencia), sin «market data»; correo «US industry benchmarks with their sources». El dashboard y el changelog no lo nombraban. Valor $29 y total $158 intactos (decisión de tienda) | ficha, correo |
| m10 | PANP `3-Year P&L!F10`: fuera la regla 80/80 de California → «Many states exempt bakery goods sold to go and tax what is eaten in the shop, but the rules vary by state: check yours» | GPAN c0941 |
| m11 | PANC `Phase 2!E14`: «Butter and mixer wash water still reach the drain: ask whether you need a grease interceptor where the local plumbing code requires it»; docx PAN [107]: permisos de fontanería «including a grease interceptor where the local plumbing code requires it» | GPAN c1188, docx pan_b 107 |
| m12 | PANP C14: «inside the 20-30%» | GPAN c0870 |
| m13 | PANP `Staffing!J23` «The head baker and the baker…» (B23 = 2); J21 «two in this example, which covers the morning and afternoon peaks and the coffee corner» (B21 = 2) | GPAN c0993/c0989 |
| m14 | PANP `Instructions!D47`: «the weighted average is about a day» (B58 = 1) | GPAN c1053 |
| m15 | PANP `Instructions!D46`: fuera «it is the year when loan repayment weighs the most» | GPAN c1049 |
| m16 | PANC `Phase 2!E13` (override): «Label packaged and wholesale items with the ingredient list, net contents and the 9 major allergens (FDA); your health department may ask for more». RESTC F52 conserva la nota de carteles | `overrides_GPAN.json` c0806 |
| m17 | RESTC F14: «Owners of an LLC or sole proprietorship are not on payroll: they take draws and pay self-employment tax. Ask your accountant how to set it up» (PANC F1!E8 conserva la del alta como empleador) | `POR_CELDA` |
| m18 | Docx PAN [114]: «shows what happens if the counter builds slowly: without corrective action, the reserve runs out» | docx |
| m19 | Docx REST [122] y FAQ UK de la landing: Licensing Act 2003 = «England and Wales; Scotland and Northern Ireland have their own licensing laws» | docx, ficha |
| m20 | Docx REST [111] y PAN [97]: «With an SBA 7(a), the SBA guarantee fee and the closing costs come on top: they change with the loan amount and each fiscal year, so we ask the lender for them and add them to the startup costs». Sin cifra (no confirmada en sba.gov en esta ronda) | docx |
| m21 | Testimonio REST: fuera «in 10 days» y «Total investment: EUR 135,000»; testimonio PAN: fuera «EUR 65,000» («they approved the financing»). Mismo criterio: ningún plazo ni cifra de resultado que no se pueda sostener | fichas |
| m22 | `7. Financing!C9` (los dos): «up to 50,000», sin símbolo (override por libro; el GM común de FT/CAF conserva «$50,000») | `overrides_GREST.json` / `overrides_GPAN.json` c0617 |
| m23 | Docx PAN [103]: el optimista con ticket y días («at {{optimista_ticket}} over {{optimista_dias}} days» → $10.91 / 320) | docx |
| m24 | PANP `Instructions!D66`: fuera la comparación con la cafetería | GPAN c1117 |

Alto de filas (`capa_altos`, solo sube): RESTC fila 17 59.75 → 104.75 y fila 60 134.75 → 149.5 (notas acortadas tras
una primera pasada que daba 149.5 / 194.5); RESTP `Instructions` fila 7 75 → 89.75; PANC `Phase 2` filas 13/14
intercambian alto (104.75 ↔ 59.75) porque la nota larga pasa de E13 a E14.

### 8.2 Aceptado sin arreglar

- **m25** (orden de pestañas de RESTP, `Instructions` entre `5. Staffing` y `6. 12-Month Cash Flow`): mover una hoja es
  una excepción estructural; cosmético, se deja como el ES.
- **m6, el fondo**: la nómina previa a la apertura no se modela como línea propia (sería una fila nueva en
  `1. Startup Costs`); el docx dice de dónde sale.
- **m20, la cifra**: sin importe de la guarantee fee (cambia cada año fiscal y con el importe).
- **m21, el resto**: los testimonios siguen siendo de la edición española con resultado cualitativo («approved the
  loan»); quitar los testimonios o cambiar su formato es decisión de John (R12/D26).
- **RESTC fila 18** (certificate of occupancy en la fase 2, heredado del ES): el docx [128] habla de «the start of… the
  certificate of occupancy» para no contradecir al checklist; mover la tarea a la fase 6 sería cambiar la estructura.
- **FT/CAF fuera de esta rama** (observaciones para el #110, no tocadas: el paso 1 era solo el FHRS): `Financing!C9`
  sigue con «$50,000» (GM común) y sus docx no mencionan la guarantee fee de la SBA.
- Observación del revisor sobre el caso REST optimista para un banco (prime cost 58.4 %, plantilla, EBITDA 17.6 %): sin
  cambio, como el m20 de FT/CAF.

### 8.3 Gates, regresión y hashes

| Comprobación | Resultado |
|---|---|
| `bp2.py extraer_textos` (VPS) | diff = solo las 5 apariciones `POR_CELDA` (+ `fmt` cosmético de `consumibles_pct`) |
| `bp2.py aplicar_en --idempotencia` | préstamo 399,000 / 197,000 en 1 vuelta; **0 diferencias**; RESTC 14 fijos (9 + 5) |
| Cambios celda a celda vs publicados | RESTP 5 · RESTC 10 · PANP 8 · PANC 2 celdas de texto; **caché numérica 0 diferencias**; `cifras_caso.json` igual |
| `bp2.py ensamblar_docx --plan rest / pan` | G8 VERDE; párrafos cambiados: REST 81, 101, 107, 111, 115, 119, 122, 128 · PAN 97, 103, 107, 110, 114 |
| `bp2.py gates_en` · `--autotest` · `ensamblar_docx --autotest` | **TODO VERDE** (G1 64/66 tareas, 772/737 fórmulas; G6 0 diferencias; G9 0 defectos, 0 no latinos) · 20/20 · 16/16 |
| `bp2.py check_textos --todas` (Mac y VPS) · `bp2.py mapas` | las 8 OK · 0 errores (97 tokens) |
| Regresión FT/CAF (`ftcaf`, `comparar_publicados.py`) | **6/6 IDÉNTICOS** en canónico a los del paso 1 (FT checklist `74ff0874…`, FT docx `4bee0054…`, CAF checklist `25a4e336…`, CAF docx `9b33a18a…`; proyecciones `68a501c6…` / `9e7dcc45…` sin cambio); `cifras_caso.json` FT/CAF igual; gates TODO VERDE, 20/20, 18/18 |
| `tienda-gate.py` (estático, Mac) | **verde** |

sha256 (Mac = VPS):

```
caf73b2e0bf241a6…  restaurant-business-plan/restaurant-business-plan.docx
1af892f3461c103c…  restaurant-business-plan/restaurant-financial-projections.xlsx
296d8157e3372d5c…  restaurant-business-plan/restaurant-opening-checklist.xlsx
aa7990f8f99fb4c0…  bakery-business-plan/bakery-business-plan.docx
96317791f9c7648a…  bakery-business-plan/bakery-financial-projections.xlsx
a1236f9e8103b808…  bakery-business-plan/bakery-opening-checklist.xlsx
```

**Ninguna cifra del caso cambió**: fichas, hub, correos y FAQ siguen valiendo ($528,696 / $266,709, 65.5 % / 62.7 %,
106 / 184, $15,000). Lo que sí cambió en la copy: el nombre del bono 2 del restaurante, los dos testimonios y la licencia
de alcohol repartida entre las fases 2 y 6.
