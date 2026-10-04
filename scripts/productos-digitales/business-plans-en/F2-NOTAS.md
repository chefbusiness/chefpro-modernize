# Food Truck + Coffee Shop Business Plan Kit (EN) — F2 (entregables) · notas

> Sesión Claude Code, 4-oct-2026. **Tanda 1 de la F2**: SPEC §7 paso 1 (extracción) y preparación del paso 4 (docx).
> Implementador único (opus), sin subagentes. Código escrito en el Mac; todo lo que abre xlsx/docx corrido en el
> **VPS** (`/root/wt-bp`, venv `/root/venv-guias`); los JSON de vuelta por `scp`. Fuente ES en solo lectura
> (`astro-site/public/dl/plan-negocio-food-truck/` y `…/plan-negocio-cafeteria/`, sha256 del censo).

## 1. Qué hay en `scripts/productos-digitales/business-plans-en/`

| Pieza | Qué es | Dónde corre |
|---|---|---|
| `mapas.py` | Productos, ficheros, pestañas (D6), `CLAVES` (D7), `FORMULAS_EN` (33 celdas, de `formulas_en.py`), `PARCHES_FORMULA` (E2), `VALORES_EN` (173 celdas: caso US de research §7, D15-D16), `FORMATOS_EN` (D8), `version_en`, `docprops_en` (D20), `TEXTOS_NUEVOS` (E1, D21), `FIJOS` (52 rótulos de la SPEC), `ZONAS_CELDA` (tablas D18/D19), `CELDA_PISTAS`, `REGLAS_US`, `GLOSARIO`, `TOKENS_DOCX` (90) + `formatear()` + `calcular_cifras()`, `DOCX_FIJOS` / `DOCX_ENCABEZADOS` / `DOCX_MOVER` / `DOCX_RPR_DE` / `DOCX_NOTAS` / `DOCX_TANDAS`, detectores `restos_espanol()` y `no_latinos()`. `python3 mapas.py` = autotest + cruce con el censo | Mac o VPS |
| `formulas_en.py` | Las 33 fórmulas con literales de texto (16 FTP + 17 CAFP) ya en EN, celda a celda | — |
| `extraer_textos.py` | Calcado del financial-kit para los 4 xlsx → `censo_es.json` + `textos_es.json` | VPS |
| `extraer_docx.py` | Censo de los 2 docx → `docx_es_ft.json` / `docx_es_caf.json` (rol, sección, tanda, notas) | VPS |
| `ensamblar_docx.py` | Docx EN: fijos + traducciones + tokens desde `cifras_caso.json`, movimiento CAF, core props, Letter y **G8**; `--autotest` | VPS |
| `preparar_tandas.py` | Entradas compactas de los traductores → `tandas/*.entrada.json` | Mac |
| `check_textos.py` | Validador de la salida de cada tanda (`--tanda X` / `--todas`) | Mac |
| `gate_f1.py` | Gate de los cimientos (SPEC ↔ censo ↔ mapas ↔ docx) | Mac o VPS |
| `BRIEF-TRADUCTORES.md` | Instrucciones para los 7 subagentes Sonnet (a-g) | — |

## 2. Cómo regenerar

```bash
ssh vps
cd /root/chefpro-modernize && git fetch origin && git worktree add --detach /root/wt-bp origin/feat/business-plans-en
cd /root/wt-bp/scripts/productos-digitales/business-plans-en
PY=/root/venv-guias/bin/python
$PY extraer_textos.py > /tmp/ext.txt && $PY extraer_docx.py > /tmp/ed.txt && $PY mapas.py && $PY gate_f1.py
$PY ensamblar_docx.py --autotest --dir /tmp/bp-docx-autotest          # 18/18
# vuelta: scp de censo_es.json, textos_es.json, docx_es_ft.json, docx_es_caf.json (solo si cambian)
# limpieza: cd /root/chefpro-modernize && git worktree remove --force /root/wt-bp
# en el Mac (solo JSON):
python3 preparar_tandas.py && python3 check_textos.py --todas
```

En el VPS `/dev/null` es un fichero normal: redirigir siempre a `/tmp/*.txt`.

## 3. Resultados (4-oct)

**Censo** (= F1-inventario §0): FTP 9 hojas · 690 textos · 722 fórmulas · 419 con hoja · 24 DV · 68 CF · 5 merges ·
135 verdes = desbloqueadas · 517 celdas con formato € · 16 fórmulas con texto · FTC 7 · 403 · 12 · 0 · 6 · 12 · 6 · 68
(= 68 tareas 11/13/12/10/12/10) · CAFP 9 · 730 · 742 · 423 · 24 · 70 · 5 · 159 · 531 · 17 · CAFC 7 · 438 · 12 · 0 · 6 · 12
· 6 · 75 (11/13/15/12/14/10). 32 hojas protegidas sin contraseña; papel A4 (9) en las 32.

**Cadenas** (`textos_es.json`, 1.292 cadenas, 2.314 apariciones):

| Grupo | Cadenas | Palabras | Plan / checklist | Celda a celda (D18/D19) | Con límite DV |
|---|---|---|---|---|---|
| **GM** (comunes FT + CAF) | 427 | 4.607 | 370 / 59 | 0 | 19 |
| **GFT** (solo food truck) | 365 | 5.231 | 225 / 141 | 124 | 0 |
| **GCAF** (solo cafetería) | 418 | 4.477 | 256 / 162 | 127 | 0 |
| **GX** (no se traduce) | 82 | 385 | — | — | — |

GX = 16 pestañas (`mapa-hoja`), 2 claves (`Sí`, `No`) y 64 `regenerar` (52 FIJOS, 2 líneas de versión, 1 pie y 9
docProps). Fuera de
las cadenas: 5 sin letras (`☐` ×155, `✓`, `OK`, `N/A`, `AI Chef Pro`) y los **47 literales de fórmula con letras**
(FTP 41 + CAFP 44 distintos por libro): los cubren `CLAVES` (`Sí`, `No`, `CUMPLE`, `REVISAR`, `Más de 3 años`, `N/A`)
y las 33 celdas de `FORMULAS_EN`; ninguno va a los traductores. La SPEC estimaba GM ≈ 475 / GFT ≈ 335 / GCAF ≈ 380: la
diferencia es que los rótulos fijados por la SPEC pasaron a GX y que las tablas D18/D19 van celda a celda.

**Docx** (`docx_es_*.json`): FT **131** párrafos (110 con texto, 114 de un run, 17 sin runs) · CAF **167** (145 con
texto, 149 de un run, 18 sin runs). **0 párrafos multi-run** en los dos (la «121 con texto» del inventario contaba
también los párrafos de un run vacío). Estilos: Normal + 10 Heading 1; página ya US Letter; `styles.xml` ya en en-US.
Traducibles: FT 61 párrafos / 6.719 palabras (ft_a 29 · ft_b 32), CAF 94 / 6.208 (caf_a 47 · caf_b 47).

**Gates**: `mapas.py` 0 errores · `gate_f1.py` VERDE (CAPEX del caso US: FT 114,120 ≈ research 114,000; CAF 193,800 ≈
190,000) · `extraer_docx.py` VERDE · `ensamblar_docx.py --autotest` **18/18** (sintético EN de los 2 planes → G8 VERDE
con rPr/pPr idénticos y tokens rellenados; CAF movido y 134 sin rojo; ES con prefijo → ROJO por español; token
desconocido / párrafo que falta → aborta; importe sin fuente, `chefbusiness.co`, «[Contenido pendiente» → ROJO) ·
`check_textos.py` probado con salidas sintéticas buenas (OK) y malas (5 errores cazados).

## 4. Decisiones y desviaciones de la SPEC

1. **Nombres de grupo**: la SPEC §7 llama GM a las comunes (que SÍ se traducen); el financial-kit usaba GM para «no se
   traduce». Aquí lo que no se traduce es **GX**.
2. **`FORMULAS_EN` celda a celda**, no por patrón: las fórmulas de texto citan otras filas con referencias relativas
   (`TEXT(C24,…)` en la fila 26) y el patrón del financial-kit solo vale para fórmulas de una sola fila. La lógica y las
   referencias son las del ES; solo cambia el texto, salvo: CAF `0. Supuestos!C50` (el ES escribía «la celda de
   arriba» para B51, que está debajo, y montaba el decimal con coma → «below» y punto), singular/plural de
   «month(s)» en Inversión D21/D25 (FT) y D30/D34 (CAF), Tesorería O11 (el ES decía «las primeras compras se pagan en el
   año siguiente»: son las últimas), D33/D42 con «#,##0» y las listas de partidas en minúscula (no calcan rótulos que
   escriben los traductores), Punto Equilibrio A26/A28 («no principal is repaid this year (interest-only period or no
   loan)»). Las filas que citan esas fórmulas («Revenue needed per year», «Year») se fijan en `FIJOS` para que casen.
3. **`FIJOS`** (52): los rótulos que la SPEC escribe literalmente (D9-D13, D18-D20, Tesorería 16-20, «Month n», firma,
   «Más plantillas…», «INDUSTRY BENCHMARKS», checklist A3 con el nombre comercial). Tesorería 16-17 llevan « (memo)» además del nombre de la
   SPEC (traducen el «(memoria)» del ES: son filas de memoria, no de caja).
4. **`VALORES_EN`** (173): research §7 tal cual; préstamo `B31 = CALIBRAR` (lo fija `aplicar_en.py`: el que propone
   `Financing`, redondeado a 1,000 por arriba); escenarios pesimista/optimista con las mismas proporciones que el ES
   [kit estimate]. **Se conservan del ES** (research no los fija): crecimiento años 2-3 (B7/B8), mezcla comida/bebida
   (B11), varios (B28: el 5 % del FT incluye el combustible), meses de fondo de maniobra (B35), rampa (B52/B53), meses
   de renta antes de abrir (B54), % de imprevistos (B55), días de cobro (B58), meses de paga extra (B60/B61, sin efecto
   con 12 pagas), aforo (B51), estacionalidad, CAF `PyG!E50` (margen bruto ≥ 65 %) y CAF `Personal!B20:B21` (13 h × 2
   personas: cobertura 8,700 / 8,840 = 98.4 %). Cada uno puede moverse en la calibración D15 solo si un semáforo lo
   exige, y se anota aquí.
5. **Zonas celda a celda** (tablas «QUÉ HA CAMBIADO…» → D18 y «DATOS DE REFERENCIA» → D19 de Instrucciones: FT filas
   35-51 y 55-68; CAF 36-50 y 54-70): un id por celda (también las celdas sin letras, «28-33 %»), porque su EN depende
   de la fila. Marcadas `por_celda: true`: `aplicar_en.py` las aplica SOLO en su celda.
6. **Docx CAF, defecto I7 del ES**: §8 dice «[Contenido pendiente de generacion]» (párrafo 134, run en ROJO) y el bloque
   financiero vive dentro de §7 (110-119, con «PLAN FINANCIERO» como seudo-título). La EN lo **mueve**: tras el
   separador de §8 van 110 (subtítulo), 134 (resumen nuevo, solo tokens) y 111-119 (`DOCX_MOVER`); nº de párrafos y
   secuencia de estilos intactos (todos Normal). El 134 toma el rPr del 112 (`DOCX_RPR_DE`). G8 admite las dos cosas
   por nombre; nada más se mueve ni cambia de formato.
7. **Multi-run**: no hay ninguno. Si un docx futuro los tuviera, `ensamblar_docx.py` los acepta solo si todos los runs
   comparten rPr (el texto va al primero y se borran los demás); con formatos distintos aborta (no se pierde formato
   en silencio).
8. **Portada, aviso, índice, encabezados D22 y cierre D23** los escribe el ensamblador (`DOCX_FIJOS`), no los
   traductores: así la marca y los títulos no dependen de nadie. Cierre: los 4 productos de D23 **sin precios**, con
   el nombre real de la tienda EN para el eBook: «Gastro Pro Prompts eBook (300+ AI prompts)» (la SPEC decía «AI
   Prompts eBook», que no existe con ese nombre). En el FT solo hay 3 líneas de producto: la 127 lleva dos.
9. **Tokens** (90; los de rótulo por plan solo existen en su plan: FT 82, CAF 85). Fuente = (hoja ES, rótulo exacto
   de la col. A, columna) resuelta por `extraer_textos.py` a celda en cada plan (`censo_es.json → tokens_docx`, con el
   valor ES en caché como comprobación de tipo); 4 derivados (`ventas_dia`, `ebitda_a1`, `ebitda_pct_a1`,
   `aportacion_pct`). Formatos US: `usd` «$254,800», `usd2` «$14.00», `int`, `ceil` (clientes de equilibrio, hacia
   arriba como la interpretación del libro), `pct0`/`pct1`, `x2` «1.84×», `dec1`/`dec2`, `anos1` «2.8 years» o «more
   than 3 years». Lista: clientes_dia, clientes_a2, clientes_a3, ticket, precio_menu, dias, crecimiento_a2,
   crecimiento_a3, sales_tax, impuesto_beneficios, food_cost_comida, food_cost_bebida, consumibles_pct, tarjeta_pct,
   cargas_pct, salario_minimo_federal, alquiler_mes, suministros_mes, seguros_anual, vida_obra, vida_equipo, ventas_a1,
   ventas_a2, ventas_a3, ventas_dia, cogs_pct, margen_bruto_pct, personal_a1, personal_pct, ocupacion_anual,
   ocupacion_pct, marketing_anual, costes_fijos_a1, amortizacion_anual, intereses_a1, resultado_antes_impuestos_a1,
   ebitda_a1, ebitda_pct_a1, resultado_neto_a1, resultado_neto_a2, resultado_neto_a3, margen_neto_a1, inversion_total,
   capex, fondo_maniobra, necesidad_caja, fondos_propios, prestamo, aportacion_pct, tipo_prestamo, plazo_prestamo,
   cuota_anual, dscr_a1, dscr_min, dscr_limite, dscr_objetivo, equilibrio_clientes_dia, equilibrio_ventas,
   equilibrio_caja_clientes_dia, equilibrio_caja_ventas, holgura_caja_pct, saldo_minimo, mes_saldo_minimo, payback,
   payback_capex, plantilla_puestos, plantilla_jornadas, cobertura_horas, horas_semana, pesimista_clientes,
   optimista_clientes, pesimista_ventas, optimista_ventas, pesimista_resultado, optimista_resultado, inv_lanzamiento,
   inv_stock; solo FT: inv_vehiculo, inv_adaptacion, inv_equipo_cocina, inv_generador, inv_permisos; solo CAF:
   inv_obra, inv_instalaciones, inv_espresso, inv_mobiliario, inv_barra, inv_terraza, aforo, rotaciones_dia.
10. **`cifras_caso.json`** (lo escribe `aplicar_en.py`): `{"meta": {…}, "ft": {token: {"valor", "fmt", "texto",
    "hoja_es", "celda"} | derivado {"valor", "fmt", "texto", "deriv": true}}, "caf": {…}}`. Se genera con
    `mapas.calcular_cifras(plan, leer, censo["tokens_docx"][plan])`, donde `leer(hoja_es, celda)` lee la caché del xlsx
    EN (traduciendo la hoja con `mapas.hoja_en`). El ensamblador usa «texto» y, si falta, formatea «valor».
11. **Cifras citables en el docx sin token** = los importes «$» y porcentajes que aparecen en `F1-research-us.md` o
    `SPEC.md` (lecturas ES y US de cada número) más los de `REGLAS_US`. Lo comprueban `check_textos.py` y G8; el resto de
    números (años, días, «9 major allergens», «26,001 lb») no se filtran.

## 5. Riesgos y pendientes para la tanda de `aplicar_en.py` (opus, VPS)

1. **Calibración D15 — el margen neto sale rojo en los dos casos base** (estimación a mano con `VALORES_EN`, antes de
   recalcular): FT ventas 254,800, margen bruto ≈ 58.8 % (umbral 58 %: justo), EBITDA ≈ 32k, DSCR ≈ 1.36×, holgura de
   caja ≈ 16 % (umbral 15 %: justo), **neto ≈ 2 % < 6 %**; CAF ventas 499,800, margen bruto ≈ 65.6 %, personal ≈ 33.8 %,
   alquiler ≈ 10.8 %, DSCR ≈ 1.85×, holgura ≈ 20 %, **neto ≈ 4 % < 6 %**. D15 permite dejar los ratios del P&L en rojo/
   ámbar con nota, pero tres márgenes justos (FT bruto, FT holgura, neto) son frágiles: recalcular con pycel antes de
   decidir y anotar aquí cada celda tocada.
2. Orden: E2 (`PARCHES_FORMULA`, espacio ES) → pestañas → `FORMULAS_EN` (celdas exactas, ya en EN: no pasar por
   CLAVES) → resto de fórmulas por CLAVES (`Sí/No/CUMPLE/REVISAR/Más de 3 años`) → textos por aparición (los
   `por_celda` solo en su celda; `FIJOS` por texto) → `VALORES_EN` → formatos → Letter → E1 → protección → docProps →
   `inject_cache` → calibración → `cifras_caso.json` → `ensamblar_docx.py`.
3. `3-Year P&L` lleva «&»: referencias siempre entre comillas simples. Nombres de 31 caracteres exactos:
   «Phase 3 - Build-Out & Equipment».
4. Coordenadas distintas FT/CAF: umbrales FT `PyG!E51,E53:E56` vs CAF `E50,E52:E55`; Inversión FT filas 7-20 vs CAF
   7-29; Personal FT B16:B19 vs CAF B18:B21. Todo va por (corto, hoja, celda) en `mapas.py`.
5. Instrucciones línea «8./9. Word» y la tabla D18 ya no deben decir «v1.1» (G2) — vienen de los traductores.
6. Pasos de la SPEC §7.6 que siguen pendientes: añadir los 2 slugs a `EXCLUIDOS` de `postprocess-transversal.py` y a
   `PRODUCTOS_LETTER` de `censo-entregables.py`.

## 6. Defectos del ES para su próxima v2.x (no se tocan desde aquí)

- **I7 · Docx CAF**: §8 «[Contenido pendiente de generacion]» en rojo y el plan financiero dentro de §7.
- CAF `0. Supuestos!C50`: «las plazas de la celda de arriba» (B51 está debajo).
- `Tesorería 12 meses!O11` (FT y CAF): «las primeras compras se pagan ya en el año siguiente» (son las últimas).
- `Inversión Inicial` D21/D25 (FT) y D30/D34 (CAF): «1 meses».
- `0. Supuestos!B58` (FT y CAF): «Días medios de cobro» = 0 bajo una DV que solo admite 1-365 (la de B6/B58/B59): el
  propio libro rechaza su valor de ejemplo si el usuario lo vuelve a teclear. La DV de B58 debería admitir 0.

## 7. Tanda 2 (4-oct, sesión Claude Code): `aplicar_en.py` + `gates_en.py` + calibración D15 + docx

### 7.1 Calibración D15 (`mapas.CALIBRACION_D15`; G7 exige que cada celda esté citada aquí)

Con los valores de research §7 tal cual, el caso base recalculado (pycel) daba: FT ventas $254,800 · holgura sobre el
equilibrio de caja **6.4 %** (< 15 %) · neto año 1 **1.8 %** · DSCR mín 1.32× · préstamo $112,000. CAF ventas $499,800 ·
holgura **12.2 %** (< 15 %) · neto año 1 **4.3 %** · DSCR mín 1.86× · préstamo $204,000. Los dos suspendían D15 por la
holgura (con interest-only 0 la cuota completa entra en el equilibrio de caja desde el año 1, D17). Se toca UNA
palanca de ingresos por plan, dentro de lo que sostiene research §4, y los escenarios se reescalan con las mismas
proporciones que el ES:

| Celda | Research §7 | Calibrado | Por qué |
|---|---|---|---|
| FTP 0. Supuestos!B4 | 70 clientes/día | **80** | 80 × $14 × 260 = $291,200: dentro del rango US $250-500K y por debajo de la media de $346K (Toast / BizBuySell, research §4). El ticket ($14) no se toca. Holgura 6 % → 22 %; neto año 1 1.8 % → 7.1 % |
| FTP Escenarios!B5 | 47 | **53** | pesimista = 80 × 30/45 (proporción del ES) |
| FTP Escenarios!D5 | 101 | **116** | optimista = 80 × 65/45 |
| CAFP 0. Supuestos!B5 | $10.50 | **$11.00** | ticket medio de cafetería CON brunch, dentro del rango por transacción $7.81-$11.11 (Dojo Business, research §4; el brunch completo va a $14-20 en la tabla D19). Los clientes (140) no se tocan. Holgura 12 % → 18 %; neto año 1 4.3 % → 6.3 % |
| CAFP Escenarios!B6 | 9.86 | **10.33** | pesimista = 11.00 × 9.20/9.80 |
| CAFP Escenarios!D6 | 11.14 | **11.67** | optimista = 11.00 × 10.40/9.80 |

Descartado: bajar sueldos (la cobertura de horas de la CAF ya va al 98.4 % y los sueldos están en $15-18/h), subir la
aportación propia (la holgura apenas se mueve: −1.5 clientes/día por cada $20K) y acortar el fondo de maniobra (es la
red de seguridad que mira el prestamista). Además, fuera de D15: **`0. Supuestos!B58` = 1** en los dos planes (en
`VALORES_EN`, no en la calibración): el ES trae 0, que viola la DV 1-365 de su propia celda (§6), y en EE. UU. el abono
de las ventas con tarjeta llega el día hábil siguiente. Efecto en caja: 1/30 de las ventas del mes se cobra al mes
siguiente.

### 7.2 Caso base final (caché de los xlsx EN = `cifras_caso.json`)

| | Food truck | Coffee shop |
|---|---|---|
| Caja total necesaria (inversión + fondo de maniobra) | $146,399 (CAPEX $114,120 + $32,279) | $263,687 (CAPEX $193,800 + $69,887) |
| Fondos propios + préstamo (10 %, sin interest-only) | $35,000 (24 %) + $112,000 a 7 años | $60,000 (23 %) + $204,000 a 10 años |
| Clientes/día × ticket × días · ventas año 1 | 80 × $14.00 × 260 · $291,200 | 140 × $11.00 × 340 · $523,600 |
| Margen bruto · personal · ocupación | 58.8 % · 26.2 % · 4.9 % | 65.6 % · 32.3 % · 10.3 % |
| EBITDA año 1 · neto años 1/2/3 | $53,427 (18.3 %) · $20,771 (7.1 %) / $36,433 / $47,685 | $84,544 (16.1 %) · $33,064 (6.3 %) / $47,568 / $57,915 |
| DSCR mínimo del cuadro · saldo mínimo de caja | 2.02× · $24,672 (mes 4) | 2.21× · $63,228 |
| Equilibrio contable / de caja · holgura | 68 / 66 clientes/día · 22 % | 123 / 120 clientes/día · 18 % |
| Cobertura de horas · sueldos bajo el suelo | 103 % · ninguno | 98.4 % · ninguno |
| Payback del proyecto / sobre CAPEX | 2.5 / 2.1 años | más de 3 años / 2.4 años |

Todos los semáforos del P&L en verde los tres años (ninguno queda ámbar: no hace falta nota de excepción).

### 7.3 Textos D19 revisados contra el caso calibrado

- **CAF `Instrucciones` fila 67** (c1108-c1111, `textos_en/GCAF.json`): «Target EBITDA (year 2) · 8-15 % · Kit estimate»
  contradecía al caso (EBITDA año 1 16.1 %, año 2 ≈ 19 %) y a su propio comentario del umbral (`PyG!F55`: «healthy coffee
  shops net about 8-12 % (industry benchmarks table)», fila que no existía): un EBITDA del 8-15 % es incompatible con un
  neto sano del 8-12 %. Pasa a **«Net margin (healthy coffee shop) · 8-12% (under 6%: structural problem) · Bellwether
  Coffee (bellwethercoffee.com)»** con nota que remite a Net income / Sales. Es la fuente de research §4 y la simétrica
  de la fila 62 del FT (Net margin 6-9 %, Beancount). El bono 2 de la landing CAF ya vendía «net margin» en esa tabla.
- **FT fila 63** «Payback period · 1-3 years»: se queda (el caso da 2.5 años).
- **CAF fila 68** «Payback period · 24-36 months»: se queda; su nota ya explica que es la referencia medida sobre lo que
  pone el dueño y que el libro publica el payback del PROYECTO (más de 3 años, con fondo de maniobra; 2.4 sobre CAPEX).
- FT fila 60 «Customers per service · 40-80» casa con 80/día de media en 1-2 servicios.

### 7.4 Piezas y comandos

`aplicar_en.py` (punto fijo del préstamo: 80/140K → 111/203K → 112/204K, 3 vueltas; `--idempotencia` 0 diferencias;
inject_cache 722/12/742/12 fórmulas, 0 fallos de pycel; D15 y cifras_caso.json) · `gates_en.py` G1-G9 (+ `--autotest`
20/20) · `ensamblar_docx.py --plan ft|caf` (G8 verde en los dos; CAF con el movimiento I7). En el VPS:

```bash
cd /root/wt-bp/scripts/productos-digitales/business-plans-en && PY=/root/venv-guias/bin/python
$PY aplicar_en.py --idempotencia --json /tmp/bp-real.json    # 4 xlsx en dl/<slug>/ + cifras_caso.json
$PY ensamblar_docx.py --plan ft && $PY ensamblar_docx.py --plan caf
$PY gates_en.py && $PY gates_en.py --autotest                 # TODO VERDE · 20/20
```

Fórmulas finales: FT 722 (plan) + 12 (checklist), CAF 742 + 12 → «more than 700 linked formulas» de las dos landings
sigue siendo cierto. Changelog 2.2: fuera «US date format» (ningún libro tiene fechas); lo demás se comprobó contra los
ficheros (LLC/EIN/seller's permit/plan review/commissary/vending/DMV/fire marshal en el FT; zoning/lease/building
permits/certificate of occupancy en la CAF; galones en el FT, square feet en el docx CAF). Landing FT, bono 2: la tabla
de referencias no tiene fila de commissary (lo mide el semáforo OK / REVIEW) y ahora lo dice así.

### 7.5 Riesgos

- CAF: payback del proyecto «more than 3 years» frente a la referencia 24-36 meses (explicado en la nota de la fila 68).
- Márgenes justos pero en verde: FT margen bruto 58.8 % frente a 58 %; CAF cobertura de horas 98.4 % frente a 98 %
  (13 h × 2 personas se conservan del ES).
- Alto de filas: el EN alarga algunas notas ajustadas (21 filas: cabeceras de `Staffing`, notas de `Instructions`, columna
  E de los checklists). `capa_altos` sube el alto SOLO donde el EN ocupa más líneas que el ES y que su alto (nunca lo
  baja); el aviso D21 (E1) copia el estilo de la línea de versión más el ajuste de texto y su alto. Es una estimación
  conservadora (un carácter por unidad de ancho): la verificación humana en Excel y a 360 px sigue siendo la última
  palabra.
- Testimonios D26 con cifras de la v1.1 del ES: siguen como decidió el orquestador (fuera de esta tanda).

## 8. Ronda de arreglos (4-oct, sesión Claude Code) — la única tras `REVISION-FINAL.md`

Implementador único. Todo lo que abre xlsx/docx, en el VPS (`/root/wt-bpfix`, venv `/root/venv-guias`); de vuelta por
`scp` con sha256 iguales. Sin tocar ninguna fórmula ni la estructura de los libros (G1 sigue verde).

### 8.1 Arreglado

| Id | Qué se hizo | Dónde |
|---|---|---|
| **B1** | `Financing!A7` = «Loan requested — bank or SBA 7(a) (amortized below)»; A8 = «Other loan (not in the schedule or the DSCR — enter your loan in row 7)»; A9 = «SBA Microloan (not in the schedule or the DSCR — enter your loan in row 7)»; notas C8/C9/C18 a juego; `'0. Assumptions'!C31` (FT c0055, CAF c0885) «if your loan is an SBA 7(a), this is the cell… the only loan the schedule, the P&L interest and the DSCR use»; `Instructions!A7` (c0381/c0994) dice que las filas 8-11 no se amortizan. Docx FT 94 / CAF 113: «bank or SBA 7(a) loan… It is the only debt in this plan, and the DSCR is measured against it». Landings (grid «Financing Plan» + FAQ del prestamista), hub (tarjeta FT), 2 correos y changelog: el cuadro y el DSCR cubren el préstamo principal; Microloan, inversores y subvenciones son otras fuentes, sin amortizar | `mapas.FIJOS`, `textos_en/GM·GFT·GCAF.json`, `docx_en_*_b.json`, fichas, `DigitalProductsHubPage.astro`, correos, `productos-changelog.ts` |
| **M1** | `'0. Assumptions'!B18` = **3.5 %** en los dos planes (`VALORES_EN`; `REGLAS_US['tarjeta']` reescrita). C18 (FT c0032, CAF c0877): «blended rate: a percentage plus a per-transaction fee, which weighs more on small tickets; check your processor's statement», sin la equivalencia 2.6 % + $0.15. Docx CAF 105 añade «a blended rate that includes the per-transaction fees». `F1-research-us.md` §3 queda superado en ese punto | `mapas.VALORES_EN`, textos |
| **M1 → D15** | Con 3.5 % el FT pasa todo (neto año 1 6.7 %, holgura 20 %). La CAF quedaba con el neto del año 1 en **5.9 % (REVIEW)**: se recalibra con UNA palanca, clientes/día **140 → 145** (research §4: 100-250), ticket intacto en $11.00. Escenarios con las proporciones del ES: pesimista 145 × 80/100 = 116, optimista 145 × 115/100 = 166.75 → 167 | `mapas.CALIBRACION_D15`: **CAFP 0. Supuestos!B4** (145), **CAFP Escenarios!B5** (116), **CAFP Escenarios!D5** (167) |
| **M2** | `PlanNegocioLandingPage.astro`: fuera del ES el carrusel enseña solo «Microsoft Excel» y «Microsoft Word» (×16 para que el carril −50 % cubra la pantalla). La rama ES no cambia | componente |
| **M3** | Fuera «(regular price $129)» de los 2 correos. El tachado de la landing no se toca | correos |
| m1 / m2 | Docx FT 99 y CAF 118: ticket y días de cada escenario y el saldo de caja estimado del pesimista (FT −$14,985: «the working capital reserve would run out…»; CAF $33,950). 5 tokens nuevos en `TOKENS_DOCX` (`pesimista_ticket`, `optimista_ticket`, `pesimista_dias`, `optimista_dias`, `pesimista_caja` → `Escenarios` B/D 6-7 y B25), resueltos por `extraer_textos.py` en `censo_es.json` (95 tokens) | `mapas.py`, `censo_es.json`, docx |
| m3 | Regla CDL completa, comprobada en 49 CFR 383.91 (LII/Cornell; FMCSA da 403): Group A = combinación con GCWR ≥ 26,001 lb si lo remolcado pasa de 10,000 lb; Group B = vehículo solo ≥ 26,001 lb. Checklist FT `Phase 2!B14/E14`, docx FT 107, FAQ FT «What does the truck itself need?» (+ «your state DMV may add its own rules») | textos, docx, ficha |
| m4 | `Phase 3!E10` FT: sin la cifra española; «check your county's minimum fresh and gray water tank sizes (in gallons) with the health department» | GFT c0762 |
| m5 | CAF C24 (c0878): «Include NNN / CAM charges… not just the base rent»; docx CAF 97: la línea de ocupación del ejemplo es solo renta base y NNN/CAM se suman si el contrato los repercute | textos, docx |
| m6 | Docx CAF 99: la fontanería tiene su propia línea; la contingencia es una línea de los costes de arranque, aparte del fondo de maniobra | docx |
| m7 | Docx FT 97 y CAF 115: «(a C corporation example; pass-through owners set it to 0 and pay tax on the profit personally)» | docx |
| m8 | A21 (FIJO) = «Monthly pay periods per year (keep 12)»; C21 (c0037) y el error de la DV de B21 (c0132, ≤ 255) explican que son las pagas mensuales del modelo, no la frecuencia de nómina. Changelog: «12 monthly salaries a year (the model's pay count, not your payroll frequency)». El literal «pay periods» de la fórmula `Staffing!A2` (FORMULAS_EN) no se toca: casa con el rótulo | `mapas.FIJOS`, GM |
| m9 | C58 FT (c0098) / CAF (c0900): «At 1 day, card settlements reach your bank the next business day» | textos |
| m10 | C52 FT (c0089) / CAF (c0895): clientes/día = MEDIA del año 1; la rampa reparte las ventas entre meses y conserva el total. CAF `Instructions!D67` (c1111): el año 1 queda bajo por volumen aún creciendo e intereses más altos, no por la rampa | textos |
| m11 | CAF `Phase 4!E5` (c1223): dos turnos de 8 h solapados (7 am-3 pm y 12 pm-8 pm, 13 h abiertos como en Staffing). `Staffing!A8` (c0986) «Brunch cook (4 days, weekends included)» y J8 (c0987) «0.8 FTE = 32 hours, always including Saturday and Sunday»; docx CAF 127 a juego. Sin tocar datos | GCAF, docx |
| m12 | FT `Instructions!D43` (c0438): «Writing it in two places counts it twice: here it lives in one cell…» | GFT |
| m13 | Landing FT, grid «Mobile Kitchen Equipment» y FAQ del camión: «all budgeted in the startup costs (kitchen and refrigeration equipment, generator, water tanks and sinks, propane and fire suppression)» | ficha FT |
| m14 | Changelog: FT «US units (pounds and gallons)», CAF «square feet in the plan». CAF `0. Assumptions!C27` (c0882) y `Phase 2!E12` (c1174): «1 million per occurrence», sin «$» | changelog, GCAF |
| m15 | Docx FT 94 / CAF 113: «(annual equivalent; the lender will set monthly payments)». El cuadro sigue siendo anual (ver 8.2) | docx |
| m16 | FHRS solo en Inglaterra, Gales e Irlanda del Norte; Escocia = FHIS (Pass / Improvement Required): checklist FT `Phase 2!E10` (c0726), CAF `Phase 1!E12` (c1146), docx FT 108 y CAF 142 | textos, docx |
| m17 | Docx CAF 137: el EIN se pide «to hire employees and to file federal employment and excise tax returns» | docx |
| m18 | Checklists `Phase 4` FT B14/E14 y CAF B16/E16 (c0800/c0801): sin base RGPD; relojes biométricos (Illinois BIPA y otros estados) y nóminas seguras. FT `Phase 5!E16` (c0831) sin la autorreferencia | GM, GFT |
| m19 | Bono 1 (guía de permisos = §9 del plan + fases del checklist): valor «Included in the plan»; subtítulo «worth $29, plus a permits guide drawn from the plan itself»; CTA «(included in the plan)»; total **$158** = kit $129 + bono 2 $29. Precio, tachado y «Save $90» intactos | fichas FT y CAF |

### 8.2 Aceptado sin arreglar (exigiría fórmulas o estructura)

- **B1, el fondo**: el modelo amortiza solo la fila 7. Que las filas 8-9 entren en el cuadro y el DSCR es un cambio de
  fórmulas; se resuelve con rótulos y notas. `Financing!C7` está vacía en el ES: escribir allí sería una celda nueva
  (G1 solo admite las de E1), así que el mensaje va en A7, A8/A9, C8/C9 y C18.
- **m15**: cuadro en anualidades (≈ $700/año más conservador que mensualidades en el FT); solo se aclara en el docx.
- **m20**: el FT sigue en 80 clientes/día (observación del revisor, sin cambio).
- **CAF, rotación de mesas**: 145 clientes / 45 plazas = 3.2 rotaciones/día frente al techo de 3 de `Break-Even!B25`
  (con 140 ya eran 3.1). Ese techo solo se compara con lo que exige el equilibrio de caja (2.67): en una cafetería de
  barra parte de los clientes se lleva el café y no ocupa plaza. Observación, sin cambio.
- **m19, bono 2**: la tabla de referencias también vive dentro del libro; la orden fue corregir solo el doble cómputo
  del bono 1. Queda para la decisión de tienda de John.

### 8.3 Caso base final (caché de los xlsx EN = `cifras_caso.json`; sustituye a la tabla de §7.2)

| | Food truck | Coffee shop |
|---|---|---|
| Caja total necesaria (CAPEX + fondo de maniobra) | $146,399 ($114,120 + $32,279) | $263,687 ($193,800 + $69,887) |
| Fondos propios + préstamo | $35,000 (24 %) + $112,000 a 7 años | $60,000 (23 %) + $204,000 a 10 años |
| Clientes/día × ticket × días · ventas año 1 | 80 × $14.00 × 260 · $291,200 | **145** × $11.00 × 340 · **$542,300** |
| Comisión de tarjeta · margen bruto | **3.5 % · 58.2 %** (umbral 58 %) | **3.5 % · 65.0 %** (umbral 65 %) |
| EBITDA año 1 · neto años 1/2/3 | $51,680 (17.7 %) · $19,461 (6.7 %) / $34,926 / $46,028 | $93,565 (17.3 %) · $39,830 (7.3 %) / $54,807 / $65,516 |
| DSCR mínimo · saldo mínimo de caja | 1.96× · $24,330 (mes 4) | 2.42× · $64,487 (mes 2) |
| Equilibrio contable / de caja · holgura | 68 / 67 clientes/día · 20 % | 124 / 121 clientes/día · 21 % |
| Payback del proyecto / sobre CAPEX | 2.6 / 2.1 años | 2.9 / 2.2 años (antes «more than 3 years») |
| Pesimista: ingresos · resultado · caja estimada | $160,813 · −$49,990 · **−$14,985** | $394,234 · −$43,195 · $33,950 |

Todos los semáforos del P&L en verde los tres años; los márgenes brutos quedan justo sobre su umbral (riesgo ya anotado
en §7.5, ahora más ajustado: 58.2 % y 65.0 %). Landings: FT «58.2% gross margin»; CAF «65.0% gross margin and
break-even at 124 customers a day, against 145 expected». Inversión, ticket y food cost no cambian.
