# Pizza Shop Business Plan Kit (EN, $39) — inventario DELTA de F1 (frente al tapas bar ES y al Bar EN)

> Sesión Claude Code, 25-oct-2026. Fuente medida: los libros ES del **dry-run** de la F2 ES que está corriendo ahora
> (`/root/tmp-piz-f2/motor/dryrun/plan-negocio-pizzeria/`, VPS, `main.py` exit 0, 13/13, checklist C2 de 80 ítems) y la
> calculadora ya generada (`astro-site/public/dl/plan-negocio-pizzeria/calculadora-masa-escandallo-pizzeria.xlsx`, = la de
> `/root/tmp-piz-f2/calc/`), contra el tapas bar ES LIVE (`dl/plan-negocio-tapas-bar/`, semilla del ES) y el Bar EN LIVE
> (`dl/bar-business-plan/`). openpyxl en el VPS (venv `/root/venv-guias`), script suelto por stdin, solo lectura, salida a
> `/tmp`. **El Word ES aún no existe** (§5). Las cifras del caso ES de abajo son del dry-run (sin la revisión final ES):
> **valen para la estructura, no para el gate de cifras**, que se alimenta de `plan-pizzeria/cifras_caso_es.json` (§9).
> Precedentes: `../business-plans-en-3/` (= **BAR**: libro gemelo) y `../business-plans-en-7/` (= **PAEL**: docx de 131
> ranuras, calculadora fuera del motor, diccionario en cadena).

## 0. Lo que manda: el libro es GEMELO del tapas bar; el checklist es nuevo; el Word, el del FT ES

| Comparación | Pestañas | Fórmulas idénticas en la misma celda | Textos idénticos en la misma celda |
|---|---|---|---|
| PIZP (plan pizzería) vs **tapas bar ES** | 9/9, mismos nombres y orden | **731/741** (10 distintas, 0 nuevas, 1 que falta: `G13`) | 431/646 |
| PIZC (checklist) vs tapas bar ES | 7/7 con el molde C2, pero **5 pestañas renombradas** | 0/12 (mismas fórmulas, filas desplazadas) | **24/463** |

Consecuencias: (1) **el código del libro es el del Bar EN** (molde FT/CAF: `_HOJAS_PLAN`, checklist de 6 hojas + Instrucciones,
`MOLDE_CHECK 'hojas'`, `COL_OK 1`, E2/E4), y el **EN del Bar en esa misma celda** es la mejor propuesta para todo lo que el
motor escribe igual; (2) del checklist casi todo es texto nuevo (≈ 3,3 K palabras); (3) el Word ES nace en las **131 ranuras del
FT ES** (no en las 133 del Word del tapas bar), así que la config de docx es la de PAEL, no la del Bar; (4) la calculadora va
fuera del motor como `calculadora_pael.py`. **Cero código común nuevo** salvo la rama `elif CONJUNTO == 'piz'` de `mapas.py`.

## 1. Totales

| Libro | Hojas | Fórmulas | Textos (palabras) | DV | CF | Merges | Desbloqueadas | Tareas | Papel |
|---|---|---|---|---|---|---|---|---|---|
| PIZP `plan-financiero-pizzeria.xlsx` (dry-run, sha `c2718a22…`) | 9 | **741** | 646 (8.422) | 24 | 70 | 5 | 156 | — | A4 |
| PIZC `checklist-apertura-pizzeria.xlsx` (dry-run, `373fca25…`) | 7 | 12 | 463 (3.523) | 6 | 6 | 6 | 80 | **80** (12/15/14/13/13/13) | A4 |
| CALC `calculadora-masa-escandallo-pizzeria.xlsx` (`ba15d673…`) | 3 | **142** (Masa 23 · Escandallo 119) | 189 (1.925) | 8 | 5 | 32 | 275 | — | A4 |
| ref. BARP tapas ES (`a757e15d…`) · Bar EN (`fff7c648…`) | 9 · 9 | 742 · 742 | 721 · 722 | 24 | 70 | 5 | 154 · 153 | — | A4 · Letter |
| ref. BARC tapas ES (`ead94333…`) | 7 | 12 | 428 (1.567) | 6 | 12 | 6 | 73 | 73 (11/13/13/12/14/10) | A4 |

Textos del plan que difieren del tapas por hoja: Instrucciones 68 · Inversión 42 · Supuestos 39 · PyG 29 · Personal 17 ·
Punto Equilibrio 12 · Escenarios 5 · Tesorería 3 (≈ 215 cadenas; muchas solo por `VOCABULARIO` cubierto → **comensal**).

## 2. Delta del libro, celda a celda (lo que F2 mapea)

1. **Fórmulas distintas (10)**: `0. Supuestos!C9` (texto del PVP con IVA), `C50` (rotaciones), `Inversión!B27` (imprevistos =
   10 % de **B7-B11**), `B35` (obra = B7-B11 + B27), `B36` (maquinaria = B12-B15 + **B17**-B21), `D27` y `D37` (listas de partidas),
   `Punto Equilibrio!A28` («comensales»), `PyG!F13` (añade «Harina, quesos, aceite… al 4 %…») y **`PyG!G11`** = línea partida
   `H11*0.21+(1-H11)*'0. Supuestos'!$B$39` (el tapas y el Bar EN: la de `B62/B16/B63/B40`). Las 5 de texto nuevo (C9, C50, D27, D37,
   F13) y A28 van a `formulas_piz_manual.py`; el resto se deriva de la gemela como `derivar_formulas_bar.py`.
2. **`PyG!G13` es VALOR** (0,064 = `IVA_COMPRAS`, verde y desbloqueada): por eso 741 y no 742. **`G14`** = la fórmula del tapas (E2
   del Bar le aplica igual). **`H4`** = «Bebida para llevar o a domicilio al 21 % (%)» y **`H11` = 0,07** (verde). Columna H vacía en
   el resto de filas.
3. **Supuestos** (rótulo propio o valor que cambia): `B4` «Comensales/día…» 66 · `B5` 19,50 · `B6` 300 · `B11` 0,82 · `B13`/`B14`
   0,235/0,27 · `B15` 0,03 · `B16`/`B17` 0,10/0,30 · `B18` 0,008 · `B20` 0,33 · `B21` 14 · `B22` 17.094 · `B24` 2.100 · `B25` 3 ·
   `B26` 1.100 · `B27` 1.800 · `B28` 0,02 · `B30`/`B31` 65.000/158.000 · `B32` 6 % · `B33` 7 · `B34` 1 · `B37`/`B38` 15/25 % ·
   `B39`/`B40`/`B41` 10/21/21 % · `B44`/`B45` 10/10 · `B51` 50 · `B52`/`B53` 0,75/4 · `B54` 3 · `B55` 0,10 · `B58`/`B59` 2/30 ·
   **`B60`/`B61` = 11/4** (pagas extra con Mes 1 = septiembre) · **`B62` «Bebida que compras al 21 % (alcohol y refrescos con
   azúcar)…» 0,8** · `B63` 0,10 «sin efecto» · `B65`/`B66`/`B67` 1/1,25/0,15 · `B68` «convenio provincial» 0.
4. **Inversión** (A1-A3 propios, sin «España 2026»; 18 partidas 7-24, misma clase de amortización por fila que el tapas salvo B16):
   7 proyecto de actividad y salida de humos · 8 obra, rótulo y fachada · 9 chimenea doble pared, filtro y bancada · 10 eléctrica ·
   11 fontanería, separador de grasas, clima y extracción · 12 horno de leña Ø 120-130 · 13 amasadora de espiral · 14 mesa fría de
   pizza · 15 armarios para cajas de bolas + arcón · **16 «Campaña con motor, freidora y fogón de apoyo»** · 17 lavado e inox ·
   18 utillaje y menaje · 19 barra (cafetera, botellero, cerveza) · 20 mobiliario de sala y terraza · 21 TPV Veri\*factu ·
   22 constitución, licencia, tasas, registro y APPCC · 23 marca, web, formación y lanzamiento · 24 stock inicial.
5. **PyG**: `A10` «Ventas de pizzería y cocina (sala, para llevar y a domicilio)» · `A11` «Ventas de bebida (cerveza, vino,
   refrescos, agua y café)» · fijos **26-34** (9): gestoría · mantenimiento del horno, «la campaña» y el frío · marketing · software ·
   limpieza, lavandería, EPI, DDD y análisis · **leña** · residuos · SGAE/AGEDI-AIE · PRL. Umbrales `E50` 0,65 · `E52` 0,27 · `E53`
   0,38 · `E54` 0,10 · `E55` 0,05 (`E51` vacío, como el tapas).
6. **Personal**: 7 filas 5-11 (titular-pizzaiolo jefe · pizzaiolo de horno · ayudante de cocina y masa · encargado de sala y barra ·
   camarero de cenas y fines de semana · refuerzo vie-dom · **suplencias** 0,1); `C12 = SUM(C5:C11)` (**E4 aplica**: el caso US
   lleva 2 servers en una fila); cobertura `B19`-`B24` = 40 · 46 · 8,5 · 3 · 2,5 · 1,5 (producción antes de abrir, como el Bar).
7. **Instrucciones = formato heladería, no tapas** (`RECALIBRADO = ()`): uso 1-8 (A4-A12; el 8 «el Word… cita las cifras de este
   Excel»), ratios A14-A22, «CIFRAS DE ESTE PLAN» A24-A31, **D19 en A33-A47** (cabecera 34 + 13 filas: Mes 1 · coste y PVP de la
   Margherita · masa y cocción del pliego · nombre «pizza napoletana» · plataforma con reparto · IVA de la pizza · SMI · personal ·
   alquiler · leña · convenio), **sin bloque D18**, firma A51, **versión A52** (E1 en A53).
8. **Tesorería**: pesos de estacionalidad `B5:M5` girados (Mes 1 = septiembre, 0,084…0,072) con nota **`O5` «Mes 1 = SEPTIEMBRE…»**;
   `O13` pagas extra; filas 16-20 de IVA (repercutido por línea, soportado, arrastre, liquidación trimestral, modelo 303) y **`A34`**
   «los trimestres son de tres meses del plan (septiembre-noviembre…)»: los rótulos 16-20 los tiene ya el Bar EN (sales tax).
   **Frente al Bar EN**: allí Mes 1 = **enero** (pesos del tapas sin girar, 0,064 → pico 0,100 en diciembre; `O5` «Profile for your
   area…»; `A34` «Fourth-quarter sales tax is settled in January…»). Aquí Mes 1 = septiembre girado → `O5` y `A34` son textos nuevos
   (POR_CELDA), no reutilizables del Bar; los pesos se quedan los del ES (research §8).

## 3. IVA → sales tax: cómo se neutraliza (patrón Bar EN D9/D57 + Bakery EN E3)

El Bar EN lo resolvió con valores (`B39 = B40 = B63 = 8 %`, `B41 = 0`) y E2 (`G13`, `G14` → `$B$41`); la Bakery EN, con un
literal de la columna H (**E3**: `H10*0.04` → `H10*0`). La pizzería trae las dos cosas, y se neutraliza así (SPEC D141):
- **`G11`**: el literal `0.21` → `'0. Supuestos'!$B$40` (**E5**, mismo mecanismo `PARCHES_FORMULA` que E3). `H4` «Beverage share
  taxed at the alcohol rate in B40 (%)», `H11` = 0,50 (beer & wine sobre bebida). Con `B40 = B39 = 8 %` el efecto es nulo; el
  usuario de un estado con impuesto propio de alcohol (nota de Texas del Bar D57) solo cambia `B40`.
- **`G13`** (valor): `VALORES_EN` = **0** con su rótulo (sin crédito por compras en EE. UU.); **`G14`**: E2 del Bar tal cual.
- `B62` (con E2 ya no mueve nada): rótulo «Alcohol share of beverage purchases (reference only: no input credit in the US)», 0,50.
  `B63`: nota «no effect in this workbook» (como el ES). `B41` 0 · `B37`/`B38` 25 %.
- Tesorería 16-20 y `A34`: textos del Bar EN (sales tax collected / remitted) + `A34` nuevo («plan quarters, not calendar quarters»).

## 4. Checklist (PIZC)

Molde C2 idéntico al del Bar (A1 título, A2 fase, cabecera fila 4 `OK | TASK | OWNER | TIMING | NOTES`, contador por hoja, DV
`"✓,☐,N/A"`), pero: **80 tareas 12/15/14/13/13/13** (filas 5-16 · 5-19 · 5-18 · 5-17 · 5-17 · 5-17; contadores en C/E 18 · 21 · 20 ·
19 · 19 · 19); pestañas ES **«F1 - Constitución» · «F2 - Local, humos y licencia» · «F3 - Cocina, horno y sanidad» · «F4 - Personal y
prevención» · «F5 - Carta, marca y delivery» · «F6 - Apertura y 90 días»**; A1 «CHECKLIST DE APERTURA — PIZZERÍA NAPOLITANA»; A2 con
semanas; `Instrucciones!A3` con el **id** «plan-negocio-pizzeria» (defecto I5 del Bar: en EN, el nombre comercial); versión **A11**
(E1 en A12). Solo 24/463 textos coinciden con el tapas: va casi todo a traductores (`GPIZ-check`).

## 5. Docx (pendiente: el Word ES aún no está)

Por `F1-camino.md` §4 y SPEC ES D16: **131 párrafos del FT ES**, 10 H1 en **37 · 44 · 51 · 59 · 67 · 76 · 83 · 91 · 100 · 109**,
índice 24-33, **61 ranuras** (`piz_es_a` §1-5 = 29 · `piz_es_b` §6-10 = 32), §9 = 102-108, `FIJOS[35]` (anexos) y `FIJOS` 127-129
(venta cruzada ES), A4. Es la estructura de `../business-plans-en-7/docx_es_pael.json` (mismos índices: `DOCX_N_PARRAFOS` 131,
`DOCX_ULTIMO_9` '108'). Paso 1 de la F2-EN: `bp8.py extraer_docx` sobre el Word ES final y localizar las ranuras del nombre protegido
con `grep -nE 'ETG|STG|napoletana|pliego|97/2010|2022/2313|2024/1143|AVPN'` en `docx_es_piz.json` (D11 del ES: van en §2 y §9).

## 6. Calculadora (CALC, ya verde en ES: autotest 422)

`Masa` (bloque A por litro de agua con los gramajes del pliego + rango gris, semáforo «dentro de los gramajes del pliego», bloque B %
panadero, coste por bola en `B50`) · `Escandallo` (`B5` **IVA de la pizza 10 %**, `B6` food cost objetivo 25 %, `B7` margen de
vigilancia, `B8` caja para llevar 1 €, `B9` = `'Masa'!$B$50`; 22 ingredientes A-D con **€/kg sin IVA** y merma; 8 pizzas E-L en
**gramos**; PVP **con IVA**; `pvp_sin = PVP/(1+IVA)`, `pvp_obj = coste/obj×(1+IVA)`) · `Instrucciones` (769 palabras, LIVA,
Reg. UE). Formatos `#,##0.00 €` y `#,##0.000 €`; `NOTA_ETG` fija; docProps ES; `PROHIBIDOS` propio. Lo que cambia en EN: SPEC D145.

## 7. Código que se clona (todo en `business-plans-en-8/`)

| Nuevo | Origen | Cambios |
|---|---|---|
| rama `elif CONJUNTO == 'piz'` en `../business-plans-en/mapas.py` | `:1205-1210` (bar) | único cambio en código común (+ mensaje de `:1241`) |
| `mapas_piz.py` | `mapas_bar.py` | `PLANES` (D133), `LIBROS` PIZP/PIZC, pestañas checklist (D146), `TAREAS_POR_FASE` 12/15/14/13/13/13, `PARCHES_FORMULA` E2 solo `G14` + E4 + **E5**, `FILA_VERSION` PIZP 52 · PIZC 11, `ZONAS_CELDA` solo D19 (34-47), **docx de PAEL** (131, H1 de §5, `ULTIMO_9` '108', tandas `piz_a`/`piz_b`), `PRESTAMO_SEMILLA` ≈ 192,400, `AUTOTEST` con las pestañas ES nuevas, grupos `GM · GR · GPIZ-plan · GPIZ-check`, **diccionario**: Bar EN (GM, GR, GBAR-plan, GBAR-check + POR_CELDA) primero y luego BP/BP2, con la normalización ES **comensal(es) → cubierto(s)** antes de buscar |
| `datos_piz.py` | `datos_bar.py` + `cifras_prohibidas()` de `datos_pael.py` | FIJOS, POR_CELDA, `VALORES_EN` (D137-D140), tokens (D147), pistas, glosario research §9, `CIFRAS_ES` + caso Bar EN (D149), `RX_PIZ_NO` |
| `bp8.py` | `bp3.py` (+ subcomandos `calculadora` y `barrido` de `bp7.py`) | `verificar` con los sha256 del ES final y del Bar EN |
| `derivar_formulas_piz.py` · `formulas_piz_manual.py` | los del Bar | gemela = celda del tapas/Bar EN; manuales C9, C50, D27, D37, F13 (+ A28 si la normalización no basta) |
| `inventario_delta.py` · `resumen_entregables.py` | los del Bar | `LIBROS`/`DOCX` de la pizzería; `REF` += BARP/BARC tapas; `FUENTES` += Bar EN (`../business-plans-en-3/textos_en/{GM,GR,GBAR-plan,GBAR-check}.json`) |
| `calculadora_piz.py` · `barrido_piz.py` · `BRIEF-TRADUCTORES.md` | `../plan-pizzeria/calculadora_piz_es.py` · `barrido_pael.py` · el de PAEL | D145 · D149 · glosario §9 pegado entero |

## 8. Defectos del ES detectados (para el orquestador del ES, ANTES de cerrar su F2: el EN duplica el ES revisado)

- **«Campaña» por «Campana»** en `Inversión!A16` («Campaña con motor, freidora y fogón de apoyo») y `PyG!A27` («Mantenimiento del
  horno, la campaña y el frío»). **Consecuencia**: el clasificador de `AMORTIZABLE` no casa «campana» y **la fila 16 (3.000 €) queda
  fuera de `B36`** (la lista de `D37` la pone entre «no se amortizan»): la campana y la freidora son maquinaria. Arreglo en la semilla /
  `a.py` (rótulo) y comprobar que `B36` = B12…B21 entero. Si no se arregla, el EN lo hereda (la fila 16 del EN es el Type I hood).
- `Checklist Instrucciones!A3` con el id interno (I5 del tapas): cosmético en ES; el EN pone el nombre comercial igualmente.

## 9. Paso 1 de la F2-EN: re-medir sobre el ES FINAL (los sha256 de arriba son del dry-run)

```bash
# VPS, worktree EN apilado (/root/wt-pizza-en), con dl/plan-negocio-pizzeria/ final (4 ficheros) y cifras_caso_es.json
cd /root/wt-pizza-en/scripts/productos-digitales/business-plans-en-8 && PY=/root/venv-guias/bin/python
$PY inventario_delta.py > /tmp/piz-inv.txt          # → inventario_delta.json (reuso Bar EN → BP/BP2, fórmulas, caso, docx)
$PY bp8.py extraer_textos > /tmp/piz-ext.txt && $PY bp8.py extraer_docx > /tmp/piz-ed.txt && $PY bp8.py mapas
```
Si una cifra de §2 cambia en el ES final, manda el ES final (este inventario solo fija la estructura).
