# Plan de Negocio: Taquería ES 1.0 — F2 (motor) · calibración, decisiones y gates

> Sesión Claude Code, 29-oct-2026. Motor de la F2 (plan + checklist) y herramienta del Word (sin redactar). SPEC =
> `F1-camino.md` §2 (firmada), §3-§4 y §7. Mac = código; VPS = motor (`/root/wt-taqueria`, salidas `/root/tmp-taq-f2/`).
> Cero código común (ni `motor.py`, ni `grupo_a.py`, ni `main.py`, ni el pid en `PRODUCTOS`).

## 1. Ficheros

| Fichero | Qué es |
|---|---|
| `planes-v2_0/contenido_plan_negocio_taqueria/{__init__,a}.py` | Contenido = el de la Pizzería con el caso de R §3 y **Mes 1 = enero** (sin las 9 piezas de septiembre); `VOCABULARIO` con las 9 frases del motor + `O5` de la Tesorería |
| `plan-taqueria/semilla_taq.py` | `semilla_piz.py` sobre la Pizzería LIVE (solo plan + checklist): 18 partidas (95.500 €), 9 fijos (13.800 €), títulos, `B60/B61` = 7/12 (con assert), docProps, `Instrucciones!A3`; sin tocar `PyG!G13` (assert de que ya es valor) |
| `plan-taqueria/datos_checklist.py` | 80 tareas 12/15/14/13/13/13, pestañas ≤ 29, fuente primaria en el docstring (art. 30 = RD 1086/2020 en la redacción del RD 1021/2022) |
| `plan-taqueria/main_taq.py` · `ciclo.sh` | `taq_version` (1.0 · noviembre 2026) + `main.py --dry-run --origen` (`SCR=/root/tmp-taq-f2/motor`) |
| `plan-taqueria/cifras_taq_es.py` | 183 tokens (`cifras_caso_es.json`) + gates D9 + los 3 de §7 F2 (2); `--calc` lee los 5 `EXPUESTOS` de la calculadora (por rótulo si no importa) y no falla si no existe |
| `plan-taqueria/barrido_es.py` | `PROHIBIDOS` + `RX_CAMPANA` + `RX_PUBLICA` + «art. 30» sin RD 1086/2020 (error) + `AVISOS` (uno a uno, sin exit) |
| `plan-taqueria/tandas_docx.py` · `docx_taq_es.py` · `BRIEF-REDACTORES.md` | Herramienta del Word: `GEMELA` = `../plan-pizzeria/textos`; `JERGA`, `PISTAS`, `AVISOS`, `art30_mal`; sin `NOMBRE_CARTA`, `PLIEGO` ni `RX_D11` |
| `astro-site/public/dl/plan-negocio-taqueria/{plan-financiero,checklist-apertura}-taqueria.xlsx` | Salida del ciclo (Mac = VPS) |

## 2. Decisiones que se apartan de la SPEC o del research (y por qué)

1. **Rótulo de `pct_bebida_alc`**: «Bebida que compras al 21 % (cerveza, mezcal, tequila y refrescos azucarados o
   edulcorados) sobre el total de bebida», SIN «aguas frescas»: las aguas frescas se hacen en casa y sus ingredientes se
   compran al 10 % (fruta al 4 %), R §1. El 0,75 y el 18,25 % no cambian; `cifras` busca `^bebida que compras al 21`.
2. **Fijos** (R: 10 filas, 12.600 €): la formación (300 €) entra en la fila de PRL (750 €) y la terraza (1.200 €) en la
   de residuos (1.700 €), = §2. DDD va en fila propia; la limpieza queda en 1.200 € sin DDD.
3. **`FC_TACO_PASTOR` en `pct`** (22,5 %; en `pct0` salía «23 %»): `a.py` cita «22,5 %» (y «24 %» la orden de 3) en la nota
   de `coste_comida`, el umbral `r_cogs` y la referencia de Instrucciones = caché de la calculadora del 29-oct (22,503 %).
4. **`O5` de la Tesorería** traducido por `VOCABULARIO` (opción de §2): Mes 1 = enero, picos en septiembre
   (Independencia), noviembre (Día de Muertos) y diciembre; `A34` del motor ya es correcto con enero.
5. **Gate del art. 30 como ERROR** (no aviso) en `barrido`, `check` y `docx`: todo «art. 30» sin «1086/2020» a ≤ 160
   caracteres, o «art. 30 del RD 1021/2022», rompe. El resto de avisos de §2 sale línea a línea sin cambiar el exit.
6. Tokens nuevos: `IVA_COMPRA_COMIDA/BEBIDA` (8,5/18,3 %), `PRL_FORMACION_ANO`, `MES_PAGA_1/2`, `VENTAS_21_PCT`,
   `CONDUCTO`, `TROMPO`, `PLANCHA`, `FREIDORA`, `FRIO`, `MANTENIMIENTO_CAMPANA`; fuera los de horno, masa y leña.

## 3. Calibración (1 vuelta de 3: la vuelta 1 del arquitecto, reproducida)

Préstamo **118.000 €** + 55.000 € propios, fijos 13.800 € (terraza en residuos): `ciclo.sh` exit 0 **TODO VERDE** a la
primera y `cifras_taq_es.py` **D9 VERDE** (15/15), sin ninguna palanca de R §3. Demo §2.11.5: ok (`inf.json`).

**Sensibilidad del food cost** (§2 «Lo que la F2 mira» (1), vuelta suelta con `coste_comida` 0,30 en
`/root/tmp-taq-f2/sens/`): cada punto de comida = **2.864 €** de EBITDA del año 1; con la comida al 30 %: neto
7,1 / **8,2** / 7,8 % y D9 sigue VERDE. Va a la pista §8 como «unos 2.900 € por punto; al 30 %, un 8 % el año 2».

## 4. Cifras del caso (`cifras_caso_es.json`, 183 tokens, con `--calc` de la calculadora commiteada)
- Ventas **358.050 / 379.533 / 394.714 €** (77 × 15,50 € × 300) · margen bruto 63,3 % · mercancía 26,8 % · personal
  129.521 € (36,2 %; 7 filas, 4,60 jornadas) · alquiler 4,9 % · EBITDA 54.325 € (15,2 %).
- Neto **32.563 € (9,1 %) / 39.022 € (10,3 %) / 37.900 € (9,6 %)**.
- Partidas + imprevistos 100.350 € · CAPEX 106.150 € · fondo 44.850 € · inversión 151.000 € · IVA 21.053 € ·
  **necesidad 172.053 €** · exceso 947 € (0,6 %) · cuota 23.997 € · **DSCR mín. 2,20** (2,29 / 2,20).
- Equilibrio contable 64 comensales (holgura 20,3 %); caja 61 / 69 / 71 · **holgura A1 26,3 %** (18,7 / 19,9 %).
- **Saldo mínimo 50.781 € en el Mes 1 (enero)** · cierre 115.133 € · payback **2,9** (número; 2,0 sobre el CAPEX) ·
  cobertura 106 % · rotación 2,4 (equilibrio 1,90 ≤ 3) · IVA bebida 10,8 % (H 7,5 %).
- Escenarios 282.831 € (neto −9.304 €) / 442.860 € (+78.195 €).
- Calculadora: 278 tacos por cono, rendimiento 64,8 %, taco al pastor 0,61 € (22,5 %), equilibrio 697 tortillas/día.

## 5. Price check (≤ 15 min, buscador sobre makro.es; sin abrir las fichas)

Tortilla: Mexifoods 15 cm, 20 uds, 2,49 € (2,15 € desde 25; ficha trigo/maíz contradictoria) ≈ 0,11-0,12 €/ud: el
0,14 € del caso es prudente. Carne: paleta de cerdo Duroc sin hueso 6,99 €/kg con IVA (≈ 6,35 € sin IVA, **sin stock**);
lomo Duroc 8,13 €/kg con IVA: el 5,50 €/kg del caso puede ser **bajo** (≈ +1,5-2 puntos de food cost de la comida a
6,35 €; D9 aguanta, §3). Aguacate: no buscado. Queda «estimación del kit, editable» (decide el orquestador).

## 6. Gates (VPS, 29-oct)

`ciclo.sh`: exit 0 en ~25 s, **TODO VERDE** (idempotencia 0 · caché 682/741 + 12, 0 fallos pycel · data_only 693 + 59
«""», 0 fallos · blancos 0 · §9 **13/13** · C2 80 ítems · censo `--fail` 0 · moldes **30/30** · 16/16 protegidas ·
demos 2.11 ok). `cifras_taq_es.py --calc`: **D9 VERDE** 15/15 (12 de la Pizzería + `B60/B61` = 7/12 + `Tesorería!B5:M5`
= tupla de enero + Mes 1 = enero coherente con la fila del saldo). `barrido_es.py` sobre los 3 xlsx de `dl/`: **0**,
2 avisos revisados («No prometer «sin gluten»…» y «Sin gluten» sólo con 20 mg/kg…: correctos). `gate_restos_ft.py
--rx-extra` (tapas, heladería y Pizzería): **VERDE** (2). «art. 30» en los xlsx: 2 veces (checklist F3!E11 y plan
Instrucciones!C42), las dos con el RD 1086/2020. `tandas_docx.py preparar`: `taq_es_a` 29 ranuras / 2.954 palabras · `taq_es_b` 32 / 3.765 · 183 tokens.
`check`: sin salida → exit 2; vacío → exit 1; `{}` → «faltan …»; prueba con «art. 30 del RD 1021/2022» y «pizza» →
ERROR, con el RD 1086/2020 → limpio. `docx_taq_es.py --parcial`: 131 párrafos, 10 Heading 1, VERDE; barrido 0.
sha256 Mac = VPS: plan `49290fce…9c85`, checklist `b1758f8a…b12f`.

## 7. Comandos

Subir fichero a fichero con `scp` a `/root/wt-taqueria/…` (nunca `rsync --delete`) · VPS: `bash ciclo.sh` →
`cifras_taq_es.py --xlsx <dryrun>/plan-financiero-taqueria.xlsx --calc <dl>/calculadora-trompo-escandallo-taqueria.xlsx
--salida /root/tmp-taq-f2/cifras_caso_es.json` → `barrido_es.py <dryrun>/*.xlsx` → `gate_restos_ft.py <dryrun> --rx-extra
…` · Mac: `scp` del json a `plan-taqueria/` y `python3 tandas_docx.py preparar` → 2 Sonnet → `check --tanda taq_es_a|b`
· VPS: `docx_taq_es.py --salida /root/tmp-taq-f2/docx`.

## 8. Pendientes para el Word y la revisión

- Subir `textos/taq_es_{a,b}.json` al VPS antes de `docx_taq_es.py`. `{PAYBACK}` hoy es número (2,9): frases que lean
  con número y con «Más de 3 años» (M1 de la Pizzería).
- Si la calculadora cambia: `cifras --calc` y revisar el «22,5 %»/«24 %» de `a.py` (§2.3). Carne (§5): ¿subir 5,50 €/kg?
- La F3 relee la LIVA art. 91 (versión con vigencia 1-12-2026, R §1).
