# Bar Business Plan Kit (EN) — F2 (entregables) · notas

> Sesión Claude Code, 11-oct-2026. **Paso 1 de la F2** (SPEC delta §7.1): el conjunto «bar» sobre el código común de
> `../business-plans-en/`, extracción, diccionario de reutilización, caso US, fórmulas y preparación de las tandas de
> traducción. Implementador único (opus), sin subagentes. Código en el Mac; todo lo que abre xlsx/docx, en el **VPS**
> (`/root/wt-bar`, venv `/root/venv-guias`), de vuelta por `scp` con sha256 iguales. Rama `feat/bar-business-plan-en`
> (F1 `fe3da59f` + merge de `main` con el PR #117).

## 1. Cómo se montó el conjunto «bar» (molde FT/CAF + contenido del restaurante)

Igual que BP2 (`../business-plans-en-2/F2-NOTAS.md` §1): **un solo código, un conjunto de datos más**.
`mapas.py` lee `BP_CONJUNTO`; con `bar`, al final del módulo, `mapas_bar.instalar(M)` sustituye los datos de FT/CAF
por los del bar y pone `mapas.DATOS = business-plans-en-3/`. `bp3.py <script> [args]` fija la variable y lanza el
script común.

| Fichero | Qué lleva |
|---|---|
| `mapas_bar.py` | Estructura: producto D48-D50, pestañas D53 (plan = FT/CAF; checklist = CAFC con «Phase 2 - Location & Licenses»), molde `hojas`, `COL_OK 1`, tareas 11/13/13/12/14/10, E2 (`PyG 3 Años!G13/G14`) y **E4** (`Personal!C12` → `SUMPRODUCT(B5:B11,C5:C11)`), versión BARP A74 / BARC A11 (E1 en A75 / A12), zonas D18/D19 por cabecera, docx (133 párrafos, Heading 1 en 37…111, último de §9 = 110), autotest (P1 = P2, C1 = C2), **grupos** y **diccionario de reutilización** |
| `datos_bar.py` | Contenido: rótulos fijados D54-D55 (FIJOS), POR_CELDA D57/D60, cifras ES prohibidas D52, tokens del docx D61 (100), fijos y notas del docx, pistas por celda y por texto, glosario del bar, caso US D52 (`VALORES_EN`, 114 celdas), `CALIBRACION_D15` (vacía) |
| `derivar_formulas_bar.py` + `formulas_bar_manual.py` → `formulas_bar.json` | D59: **14 derivadas** de su gemela (13 de FT, `Punto Equilibrio!A28` del restaurante, «covers») y **3 manuales** (C50, D27, D37) |
| `bp3.py` | Lanzador (copia de `bp2.py`) + `derivar_formulas` y `verificar` (CELDA_PISTAS / POR_CELDA / DOCX_NOTAS sobre celdas que existen; lo corre también `bp3.py mapas`) |

**Grupos** (D53):

| Grupo | Cadenas | Palabras | Qué es | Va a |
|---|---|---|---|---|
| GM | 397 | 4.228 | Idénticas a una común de FT/CAF (`../business-plans-en/textos_en/GM.json`) | nadie: `textos_en/GM.json` ya escrito |
| **GR** | 97 | 1.057 | Idénticas a una de REST/PAN/CAF/FT ya traducida (prioridad GM → GREST/GN → GCAF → GPAN → GFT, la de F1), solo de «traducir» | `textos_en/GR.json` ya escrito; **revisión** en la tanda GBAR-check (`GR.revision.json`) |
| **GBAR-plan** | 191 | 2.947 | Nuevas del plan: 63 de texto libre (1.637) + 128 celdas de las tablas D18/D19 (1.310; 17 con propuesta, solo D18) | tanda 1 (a) |
| **GBAR-check** | 106 | 657 | Nuevas del checklist | tanda 1 (b) |
| GX | 122 | 749 | Pestañas, CLAVES, FIJOS (94), POR_CELDA (6), versión, pie, docProps | nadie: lo escribe `mapas` |

Total escrito ya en EN: **494 cadenas reutilizadas** (397 GM + 97 GR) + las 122 de GX. F1 contaba 543 reutilizables:
la diferencia son las que aquí van a FIJOS (rótulos de D54-D55 que ya eran GM/CAF en otros kits) y las celdas de las
tablas, que en BP/BP2 también iban por celda y no se reutilizan (D19 cambia entera por D58).

**Cambios en el código común** (todos con el valor de FT/CAF y REST/PAN por defecto):

| Fichero | Cambio |
|---|---|
| `mapas.py` | Rama `elif CONJUNTO == 'bar'`; `grupo_de(…, donde=None)`; `reuso_de(e)` (por defecto, el de antes); `CIFRAS_PROHIBIDAS = []` + `cifras_prohibidas(t)`; autotest con `3 × len(PLANES)` ficheros (antes, 6 fijo) |
| `extraer_textos.py` | Llama a `mapas.grupo_de(…, donde=e['donde'])` y a `mapas.reuso_de(e)` |
| `preparar_tandas.py` | `textos_en/<g>.revision.json` encima de un grupo reutilizado (si existe); lista `revisar_reutilizadas` en la entrada de la tanda que dice `mapas.REVISAR_EN_TANDA` |
| `check_textos.py` | Cifras/términos prohibidos (D52) en `comunes()`; valida `<g>.revision.json` (ids del grupo, texto limpio, aplicada) |
| `gates_en.py` G2 · `ensamblar_docx.py` g8 | Cifras/términos prohibidos (g8 salta la cifra que es el texto de un token: solo pasa en el autotest, que rellena con las cifras ES) |
| `../business-plans-en-2/mapas_rp.py` | `grupo_de(…, donde=None)` |

## 2. No regresión de FT/CAF y REST/PAN (VPS, con todo lo anterior)

| Comprobación | Resultado |
|---|---|
| `extraer_textos` ftcaf / restpan a `/tmp` vs versionados (sin `meta`) | `textos_es.json` **IGUAL** los dos; `censo_es.json` restpan IGUAL, ftcaf IGUAL salvo la clave `tareas_por_fase` (ya conocida: BP2 §2) |
| `mapas.py` · `bp2.py mapas` | 0 errores · 0 errores |
| `gates_en.py` (dl/ publicados) · `--autotest` | **TODO VERDE** G1-G9 · **20/20** |
| `bp2.py gates_en` · `--autotest` | **TODO VERDE** G1-G9 · **20/20** |
| `ensamblar_docx.py --autotest` ftcaf · restpan · bar | **18/18** · **16/16** · **8/8** |
| `check_textos.py --todas` ftcaf · `bp2.py check_textos --todas` | las 7 OK · las 8 OK |

## 3. Extracción del bar (`bp3.py extraer_textos` / `extraer_docx`, VPS)

Censo = F1-inventario-delta §1: BARP 9 hojas · 721 textos · **742 fórmulas** · 425 con hoja · 17 con texto · 24 DV ·
70 CF · 5 merges · 154 verdes = desbloqueadas · BARC 7 · 428 · 12 · 6 DV · 12 CF · 6 merges · 73 verdes · **73 tareas
11/13/13/12/14/10**. `bp3.py mapas`: **0 errores** (VALORES_EN sobre celdas verdes con su rótulo, literales de fórmula
y CF cubiertos, 100 tokens resueltos); `verificar`: 0 errores, 7 avisos (pistas sobre cadenas GM/GR que ya tienen EN:
inofensivos). Docx: VERDE, 133 párrafos, 0 multi-run, Letter; traducibles 62 / 6.630 palabras → **bar_a 32 / 3.535 ·
bar_b 30 / 3.095**; 21 notas por párrafo (§1, §3, §6-§10; §9 = 5 notas D61, el 110 cierra con la nota UK).

sha256 (Mac = VPS) de esta pasada: `censo_es.json`, `textos_es.json`, `docx_es_bar.json` en el commit.

## 4. Decisiones y desviaciones

1. **POR_CELDA** (el mismo ES con otro EN en esa celda): BARC `F2 - Local!C8` «Owner + attorney» y `D8` «Start right
   after signing the lease: often 3-12 months» (D60, lección M1); `B11` «General liability + liquor liability (dram
   shop) insurance»; **`B14`**: «Hojas de reclamaciones…» es GM con el EN del FOOD TRUCK («Commissary agreement…», el
   mismo error que BP2 §4.1 cazó en la cafetería) → «Required public notices posted (health permit, liquor license,
   labor law posters)»; BARP `0. Supuestos!C63` con la nota de Texas (D57); BARP `Personal!A29` = la nota E4 del
   restaurante (override c0422 de BP2) + las propinas (D38): era GM y no había otra celda traducible en `Staffing`.
2. **Overrides heredados**: el diccionario toma los de `overrides_GREST.json` de BP2 (E4 de Staffing, SBA Microloan)
   pero **no** los de FT (commissary) ni CAF (avisos de la fase 2): son de su libro.
3. **FIJOS nuevos** (94 en total): títulos sin «España» ni «tapas bar / gastrobar», las 18 partidas de D54, A2/A10/A11
   y fijos A25-A34 del P&L (D55), los 7 puestos de `Staffing` (D55), «US INDUSTRY BENCHMARKS» (D58) y «PHASE 2:
   LOCATION & LICENSES» (para que la fase diga lo mismo que su pestaña). `A28` del P&L (marketing) y `A22-A24` quedan
   con el EN del motor (GM).
4. **D19 sin propuesta**: las 16 filas (54-69) cambian por las de D58 con una pista por fila (fuente real o «Kit
   estimate»). Reparto: 54 food cost · 55 pour cost total · 56 cerveza · 57 personal · 58 alquiler · 59 ticket ($20-$35,
   Kit estimate) · 60 destilados · 61 vino · 62 seat turns (1.5-3, Kit estimate) · 63 startup leased · 64 liquor license
   · 65 margen bruto ≥ 68 % · 66 liquor liability · 67 reserva operativa ($75,000-$100,000, research §4) · 68 prime cost
   (60-65 %, Restaurant365 vía BP2) · 69 salario mínimo. Las 3 últimas no están en la lista literal de D58: rellenan
   las filas que quedaban con datos con fuente de research (revisión final: confirmar o redactar sin cifra).
5. **Fórmulas (D59)**: C50 sin la cifra del docx ES (compara con el techo de "Break-Even"); D27 con las partidas de
   obra del bloque en minúscula (= base B35 de la amortización); D37 con lo que no se amortiza + «a license bought from
   another owner is an intangible asset: ask your CPA» (D54) y miles con «#,##0».
6. **Caso US (D52) tal cual research §8** en `VALORES_EN` (114 celdas): ningún desvío. Escenarios 71 / 119 covers ×
   $25 / $29 × 340 / 360 días (−25 % / +25 %, ∓$2).

## 5. Ensayo de la tanda siguiente (VPS: `aplicar_en --dry-run --parcial`, gates parciales)

`bp3.py aplicar_en --dry-run --parcial --salida /tmp/bar-dry` (GM + GR en EN; GBAR-plan/check en ES): monta los 2
libros sin abortar (17 FORMULAS_EN, E2 + E4 = 3 parches, 92 + 14 fijos, 114 valores); **préstamo por punto fijo en 1
vuelta: $369,000** (= la estimación de research); inject_cache 742 / 12 fórmulas, **0 fallos de pycel**. Caso base SIN
calibrar — **D15 en verde sin tocar nada**:

| Métrica | Bar (research §8 tal cual) |
|---|---|
| Ventas año 1 · margen bruto · mercancía · personal · alquiler | $923,400 · **69.7 %** (≥ 68) · 24.8 % (≤ 28) · 33.4 % (≤ 35) · 8.4 % (≤ 10) |
| Neto año 1 / 2 / 3 · payback | **8.2 %** / 13.7 % / 16.9 % · 2.5 años |
| DSCR mínimo · saldo mínimo de caja · cobertura · holgura de caja | **2.44×** · $105,666 · **103.7 %** · **21.0 %** |

Todos los semáforos del P&L en verde los 3 años. `bp3.py gates_en --dir /tmp/bar-dry --parcial --solo
G1,G3,G4,G5,G6,G7`: ver §7 (resultado final de esta pasada).

## 6. Comandos para seguir

```bash
# Mac (solo JSON) — tras cada tanda de traducción
python3 scripts/productos-digitales/business-plans-en-3/bp3.py check_textos --tanda GBAR-plan   # | GBAR-check | GR | bar_a | bar_b
python3 scripts/productos-digitales/business-plans-en-3/bp3.py preparar_tandas                  # tras GR.revision.json
python3 scripts/productos-digitales/business-plans-en-3/bp3.py check_textos --todas

# VPS — paso 3 de la F2 (aplicar_en real + calibración + docx + gates)
ssh vps
cd /root/wt-bar && git pull --ff-only
cd scripts/productos-digitales/business-plans-en-3 && PY=/root/venv-guias/bin/python
$PY bp3.py aplicar_en --idempotencia --json /tmp/bar-real.json      # 2 xlsx en dl/bar-business-plan/ + cifras_caso.json
$PY bp3.py ensamblar_docx --plan bar                                # tras bar_a + bar_b
$PY bp3.py gates_en && $PY bp3.py gates_en --autotest && $PY bp3.py ensamblar_docx --autotest --dir /tmp/bar-docx-at
# regresión FT/CAF y REST/PAN: §2 (gates_en.py / bp2.py gates_en + --autotest; ensamblar --autotest)
# vuelta: scp de dl/bar-business-plan/* y cifras_caso.json (sha256 iguales); commit desde el Mac; VPS limpio

# Solo si cambian el censo o las fórmulas (Mac o VPS)
python3 scripts/productos-digitales/business-plans-en-3/bp3.py derivar_formulas
# Solo si cambian mapas_bar/datos_bar en algo que clasifica cadenas (FIJOS, POR_CELDA, zonas): VPS extraer + Mac preparar
$PY bp3.py extraer_textos > /tmp/bar-ext.txt && $PY bp3.py extraer_docx > /tmp/bar-ed.txt && $PY bp3.py mapas
```

En el VPS `/dev/null` es un fichero normal: redirigir a `/tmp/*.txt`. Al copiar del Mac al VPS con `tar`, poner
`COPYFILE_DISABLE=1` (si no, aparecen ficheros `._*` de macOS).

## 7. Resultado de esta pasada y riesgos para el paso 3

**Resultado** (VPS, código y datos de este commit; sha256 Mac = VPS de `censo_es.json` `930348a1…`, `textos_es.json`
`b4c7af64…`, `docx_es_bar.json` `b4278857…`, `formulas_bar.json` `91d1ad13…`, `textos_en/GM.json` `ffbf9780…`,
`textos_en/GR.json` `e7f011fe…`):

| Comprobación | Resultado |
|---|---|
| `bp3.py mapas` (autotest + cruce con el censo + verificar) | 0 errores (16 pestañas, 9 claves, 94 fijos, 17 fórmulas EN, 114 valores, 100 tokens) |
| `bp3.py aplicar_en --dry-run --parcial` | préstamo $369,000 en 1 vuelta · inject_cache 742 / 12, 0 fallos de pycel · D15 sin fallos |
| `bp3.py gates_en --dir /tmp/bar-dry --parcial --solo G1,G3,G4,G5,G6,G7` | **TODO VERDE** (G1 742 fórmulas y 73 tareas [11, 13, 13, 12, 14, 10] · G3 16 hojas Letter · G4 226 valores bajo DV · G5 8 rangos · G6 0 diferencias con la referencia ES recalculada · G7 114 valores) |
| `bp3.py ensamblar_docx --autotest` | 8/8 |
| `bp3.py check_textos --todas` | GM OK · GR OK · GBAR-plan, GBAR-check, bar_a, bar_b «falta» (pendientes de traducir). Sobre un `{}`: «faltan 191 / 106 ids» y «faltan 32 / 30 párrafos». Sobre una salida con defectos inyectados: caza 302.400, «14 pay periods», «payroll taxes of 33%», «tapas bar», «gastrobar», «$50,000» de equity (y deja pasar el del SBA Microloan) |

Cifras del caso sin calibrar (dry-run, = estimación de research §8): caja total **$488,932** (CAPEX $361,700 + fondo
de maniobra $127,232) · fondos propios $120,000 (25 %) + préstamo **$369,000** · ventas año 1 **$923,400** · EBITDA
**18.6 %** · neto 8.2 % · COGS 24.8 % · personal 33.4 % · **prime cost 58.2 %** · equilibrio 81 / 79 covers al día ·
1.6 seat turns · 11 personas = 7.00 FTE (E4) · DSCR año 1 2.44× · payback del CAPEX 2.0 años · pesimista −$122,493 de
resultado y $15,791 de caja estimada (no se agota) · optimista +$322,792. **`CALIBRACION_D15` queda vacía**: el caso de
research pasa D15 y los 5 umbrales de D56 sin tocar ninguna celda (riesgo 2 de la SPEC: EBITDA 18.6 %, < 20 %).

También en este commit (D63, porque G9 los necesita en el paso 4): `bar-business-plan` en `PRODUCTOS_LETTER` de
`censo-entregables.py` y en `EXCLUIDOS` de `postprocess-transversal.py`.

**Riesgos para la generación (paso 3)**:

1. **G2, G8 y G9 aún no se han corrido** sobre el bar: necesitan los textos traducidos (G2 con `--parcial` daría rojo
   por el español que queda) y el docx. `gates_en --autotest` también, tras las tandas (necesita la copia limpia).
2. **GR.revision.json**: si GBAR-check corrige reutilizadas, hay que correr `bp3.py preparar_tandas` (Mac) ANTES de
   `aplicar_en`, o el xlsx saldrá con el EN sin corregir; `check_textos --tanda GR` lo detecta («no está aplicada»).
3. **Alto de filas**: las notas fijadas de `Staffing!A29` (≈ 700 caracteres) y `0. Assumptions!C63` son más largas que
   el ES; `capa_altos` actúa sola, pero la verificación humana en Excel y a 360 px sigue siendo la última palabra.
4. **Tabla D19**: «$20-$35» de ticket y «1.5-3» seat turns son Kit estimate elegidos aquí; las filas 67 (reserva
   operativa) y 68 (prime cost) no están en la lista literal de D58. La revisión final las confirma o las deja sin cifra.
5. **Prime cost 58.2 %** por debajo del 60-65 % full-service: el docx (nota de bar_b 100) lo explica (la bebida cuesta
   menos). EBITDA 18.6 % con bebida al 22 %: el docx dice que el pour cost manda.
6. Si una revisión toca FIJOS, POR_CELDA o zonas, hay que volver a extraer en el VPS (`bp3.py extraer_textos`) y a
   preparar en el Mac: los ids de `textos_es.json` pueden moverse y las salidas de los traductores dejan de casar.
7. El mensaje final de `aplicar_en` dice «4 xlsx» (literal heredado del código común): son 2. Cosmético.

## 8. Cierre de la F2 (11-oct, sesión Claude Code): tandas aplicadas, xlsx + docx EN, gates

**Tandas** (subagentes, validadas por el orquestador; commit `4cfac416`): `textos_en/GBAR-plan.json` (191 claves),
`GBAR-check.json` (106), `GR.revision.json` (2 correcciones: c0721 nota del plan review con la nota UK, c0874 licencias
de música «in the bar»), `docx_en_bar_a.json` (32) y `docx_en_bar_b.json` (30). `bp3.py preparar_tandas` aplicó la
revisión sobre `GR.json`; `bp3.py check_textos --todas`: **las 6 OK** (GM 7 avisos, GR 2, GBAR-plan 1, GBAR-check 6,
bar_a 0, bar_b 1 — de longitud, revisados).

**Un arreglo en el código común** (`e1bbee35`): `check_textos.RX_DOLAR` leía «{{inversion_total}}, made up of…» como
«$488,932, m» × 1.000.000 (el número se comía la coma y la «m» de «made» pasaba por sufijo de millones) y G8 daba
ROJO por un importe inexistente. Ahora el número no termina en coma y el sufijo (K, M, million, thousand) tiene que ser
palabra entera. Regresión: `check_textos --todas` de FT/CAF (7 OK) y REST/PAN (8 OK), gates G1-G9 de los dos conjuntos
VERDE y `ensamblar_docx --autotest` 18/18 y 16/16.

**Generación (VPS, `/root/wt-bar`, `e1bbee35`)**:

| Comprobación | Resultado |
|---|---|
| `bp3.py aplicar_en --idempotencia` | préstamo **$369,000** en 1 vuelta (= research); textos 622 + 332, fijos 92 + 15, valores 114, **faltan 0**; idempotencia **0 diferencias**; inject_cache 742 / 12 fórmulas, **0 fallos de pycel**; D15 sin fallos; los 5 umbrales del P&L en verde los 3 años |
| `bp3.py ensamblar_docx --plan bar` | G8 **VERDE** |
| `bp3.py gates_en` (G1-G9 sobre `dl/bar-business-plan/`) | **TODO VERDE**: G1 742 fórmulas y 73 tareas [11, 13, 13, 12, 14, 10] · G2 1,344 piezas (incluido el gate de cifras ES prohibidas D52) · G3 16 hojas Letter con pie, versión y aviso · G4 226 valores bajo DV · G5 8 rangos de CF · G6 caché = referencia ES recalculada, 0 diferencias · G7 114 valores · G8 docx · G9 `censo-entregables --fail` 0 defectos y `gate-no-latinos` 3 ficheros, 0 caracteres |
| `bp3.py gates_en --autotest` · `ensamblar_docx --autotest` | **20/20** · **8/8** |
| 2.ª pasada completa (`aplicar_en --dry-run` + `ensamblar_docx --salida` en `/tmp/bar-regen`) frente a `dl/` | sha256 CANÓNICO (miembros del zip sin las 2 fechas de `core.xml`) **idéntico en los 3 ficheros**; `cifras_caso.json` igual |
| `resumen_entregables.py` (barrido independiente de los 3 ficheros: celdas, literales de fórmula y párrafos) | 3,429 piezas · **0 cifras ES prohibidas · 0 restos de español · 0 no latinos** |

**Ficheros** (`astro-site/public/dl/bar-business-plan/`, mismo patrón que `restaurant-business-plan/`; `/dl/` no cae
en ninguna regla de `robots.txt`). sha256 Mac = VPS:

| Fichero | Contenido | sha256 |
|---|---|---|
| `bar-business-plan.docx` | 133 párrafos (111 con texto), 10 Heading 1, **7,583 palabras**, US Letter | `ece4f2cbe2cead44…` |
| `bar-financial-projections.xlsx` | **9 hojas, 742 fórmulas**, 114 celdas del caso US | `fbd3e1d912923aea…` |
| `bar-opening-checklist.xlsx` | **7 hojas, 73 tareas** (11/13/13/12/14/10), 12 fórmulas | `e077a4821d7595a5…` |

`cifras_caso.json` (`217e04c2…`, la caché del libro EN calibrado; la leen `ensamblar_docx` y la F3) y
`entregables_bar.json` (`f5055407…`: recuentos, sha256, el caso en texto US y el barrido) quedan en esta carpeta.

**Caso final (leído del libro generado)**: 95 covers × $27.00 sin sales tax ($29.16 con él) × 360 días · bebida 65 %
(alcohol 90 % de la bebida) · 60 plazas, 1.6 seat turns · ventas **$923,400** / $1,061,910 / $1,168,101 · caja total
**$488,932** = CAPEX $361,700 + fondo de maniobra $127,232 (licencia de alcohol $15,000, estado sin cupo) · fondos
propios $120,000 (25 %) + préstamo **$369,000** al 10 % a 10 años, cuota $60,053 · margen bruto 69.7 % · COGS 24.8 % ·
personal 33.4 % · prime cost 58.2 % · alquiler 8.4 % · EBITDA $171,583 (**18.6 %**) · neto $75,358 (8.2 %) / $145,000
/ $197,922 · **DSCR 2.44×** (año 1 = mínimo) · equilibrio **81 covers/día** (contable) y **79** (caja), holgura 21 % ·
saldo mínimo $105,666 (mes 4) · **payback 2.5 años** (2.0 sobre el CAPEX) · 11 personas = 7.00 FTE, cobertura 104 % ·
seguros $12,000/año · pesimista $603,500 de ventas, −$122,493 de resultado y $15,791 de caja (no se agota) ·
optimista $1,242,360 y +$322,792.

**Para el revisor (la revisión adversarial que viene)**:

1. **«guests» frente a «covers» en el docx**: 37 «guests» y 16 «covers» (D55 pedía «guests (covers)» la primera vez y
   luego «covers»). No es un error de cifra, pero conviene mirar la coherencia con el libro, que dice «covers».
2. **Tabla D19** (`Instructions` 54-69): «$20-$35» de ticket y «1.5-3» seat turns como Kit estimate; filas 67 (reserva
   operativa $75,000-$100,000, Poster) y 68 (prime cost 60-65 %, Restaurant365) añadidas aquí, fuera de la lista
   literal de D58. Las fuentes que el docx cita (R Street, Poster, BevSpot, Insureon, Restaurant365) vienen de research
   delta §4-§5; la SPEC §8.5 pide abrir las que se leyeron como resumen antes de dar por buena una cifra.
3. **Notas largas fijadas** (`Staffing!A29` ≈ 700 caracteres, `0. Assumptions!C63` con Texas): `capa_altos` ajusta
   el alto; la vista en Excel/LibreOffice y a 360 px es la última palabra.
4. **Prime cost 58.2 %** (< 60-65 % full-service) y **EBITDA 18.6 %**: el docx §8 lo explica (la bebida cuesta menos;
   el pour cost manda). Pesimista con caja positiva al cierre ($15,791) pero resultado −$122,493.
5. `CALIBRACION_D15` vacía: el caso de research §8 pasa D15 y D56 sin tocar ninguna celda (G7: 0 calibraciones).
6. Testimonios ES de la ficha (SPEC §8.3) y todo lo de la capa de producto: F3, fuera de esta tanda.

```bash
# Reproducir (VPS)
cd /root/wt-bar/scripts/productos-digitales/business-plans-en-3 && PY=/root/venv-guias/bin/python
$PY bp3.py aplicar_en --idempotencia --json /tmp/bar-real.json && $PY bp3.py ensamblar_docx --plan bar
$PY bp3.py gates_en && $PY bp3.py gates_en --autotest && $PY bp3.py ensamblar_docx --autotest --dir /tmp/bar-docx-at
$PY resumen_entregables.py                                   # entregables_bar.json + barrido independiente
```

## 9. Ronda de arreglos tras `REVISION-FINAL.md` (11-oct, sesión Claude Code) — todo por la vía de TEXTO

Aplicados los 7 MAYOR, los 17 MENOR y el opcional de `Instructions!A52`, dentro del circuito (ningún fichero generado
se parchea a mano; M4 sin tocar `B54`):

| Dónde vive | Arreglos |
|---|---|
| `textos_en/GBAR-plan.json` | m3 `Startup Costs!D8` (renovación anual o bienal) · m4 `C44`/`C45` (el draft system pasa a la obra) · m6 `Instructions!D55` (rótulo real) · m7 `C51` (patio solo si abre casi todo el año) · M7 `Instructions!D69` (dol.gov) |
| `textos_en/GBAR-check.json` | M4 `Phase 2!E6` (rent abatement + license contingency) · M7 `Phase 4!E5`, `Phase 4!E13`, `Phase 1!E6` · m10 `Phase 3!E11` (instalador de grifos) · m11 `Phase 1!E8` |
| `textos_en/GR.revision.json` (4 correcciones) | M4 `0. Assumptions!C54` (meses hasta la licencia) · m5 `Scenarios!E24` («"Staffing"») |
| `datos_bar.py` POR_CELDA / FIJOS | m8 `C63` (6.7 % × cuota de alcohol) · m17 `Staffing!A29` (sin la 2.ª frase) · m12 `Phase 3!D5` «1-3 months» · m13 `Phase 6!B6/C6` · A52 «US INDUSTRY BENCHMARKS (sourced) AND KIT ESTIMATES» (c0883 pasa de GM a POR_CELDA) |
| `docx_en_bar_a.json` / `_b.json` | M1 [42], [100] · M2 [102] · M3 [58], [76] · M4 [114] · M5 [59] · M6 [106] · m1 [107] · m2 [42], [118] · m9 [94] · m10 [82] · m14 [116] · m15 [100] · m16 [39] |

Para que el docx no lleve cifras sin token: 5 tokens **derivados del mismo caso** en `datos_bar.TOKENS_PROPIOS`
(`meses_alquiler_previo` 2 · `costes_variables_pct` 30.3 % · `otros_variables_pct` 5.5 % · `pesimista_perdida`
$122,493 · `pesimista_perdida_operativa` $51,388). Re-extracción en el VPS: **mismos ids y mismo ES** que antes.

| Comprobación (VPS, `5be311da`) | Resultado |
|---|---|
| `check_textos --todas` (Mac) | las 6 OK |
| `aplicar_en --idempotencia` | préstamo $369,000 en 1 vuelta · faltan 0 · 0 diferencias · 0 fallos de pycel · D15 sin fallos |
| `ensamblar_docx --plan bar` · `gates_en` G1-G9 | G8 VERDE · **TODO VERDE** (G9: censo-entregables 0 defectos, no latinos 0) |
| `gates_en --autotest` · `ensamblar_docx --autotest` | 20/20 · 8/8 |
| `resumen_entregables.py` | 3,429 piezas · 0 cifras ES prohibidas · 0 español · 0 no latinos |
| `cifras_caso.json` frente al de §8 | **los 100 tokens anteriores, idénticos** (valor y texto); 5 nuevos derivados |

sha256: `bar-business-plan.docx` `d4d9574487edabe8…` · `bar-financial-projections.xlsx` `fff7c6482759c63f…` ·
`bar-opening-checklist.xlsx` `9621312611ab4707…` · `cifras_caso.json` `bc45391432e5742b…`.
