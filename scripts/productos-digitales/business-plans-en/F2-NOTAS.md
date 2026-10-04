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
