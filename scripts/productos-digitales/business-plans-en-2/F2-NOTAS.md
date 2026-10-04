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
