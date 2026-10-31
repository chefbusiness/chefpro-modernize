# Plan de Negocio: Sushi Bar ES 1.0 — F2 (entregables) · calibración, decisiones y gates

> Sesión Claude Code, 31-oct-2026 (F2 nocturna, decisiones delegadas). SPEC = `F1-camino.md` §2 (firmada por el
> orquestador), §3-§4 y §7. Mac = código y redacción; VPS = motor, openpyxl, python-docx y gates (`/root/wt-sushi`,
> salidas `/root/tmp-sus-f2/`). Cero código común (ni `motor.py`, ni `grupo_a.py`, ni `main.py`, ni el pid en `PRODUCTOS`).

## 1. Ficheros

| Fichero | Qué es |
|---|---|
| `planes-v2_0/contenido_plan_negocio_sushi_bar/{__init__,a}.py` | Contenido = el de la Taquería (rotación ENCENDIDA, comensal) con el caso de R §3 y el `VOCABULARIO` de la Pollería (`_SIN_TILDES`, sin pan, O5 con diciembre pico y agosto valle) |
| `plan-sushi/semilla_sus.py` | `semilla_pol.py` SIN `_sin_rotacion`, sobre la Taquería LIVE (plan + checklist): 18 partidas (98.500 € + imprevistos = 103.350 €), 9 fijos (13.850 €), títulos, docProps, `Instrucciones!A3`; asserts `B60/B61` = 7/12, `PyG!G13` valor y `Supuestos!B50` fórmula (rotación viva) |
| `plan-sushi/datos_checklist.py` | 80 tareas 12/15/14/13/13/13, pestañas ≤ 29, fuente primaria en el docstring (RD 1021/2022 art. 8.1-8.2 y 4.1, Rgto. 853/2004 anexo III secc. VIII, RD 1086/2020 art. 30.2-30.7 con el 30.5 del shari, RD 126/2015 arts. 4-5, LIVA 91…) |
| `plan-sushi/sus_version.py` · `main_sus.py` · `ciclo.sh` | 1.0 · noviembre 2026 + `main.py --dry-run --origen` (`SCR=/root/tmp-sus-f2/motor`) |
| `plan-sushi/cifras_sus_es.py` | 192 tokens (`cifras_caso_es.json`) + D9 (= Taquería, 12) + Mes 1 = enero (3) + **`prueba_sushi`** (4: techo 3,0 y caso 2,0-2,4; aforo 36; 0 restos; rótulos «Comensales/día»); `--calc` lee TODO el `EXPUESTOS` de la calculadora (11) |
| `plan-sushi/calculadora_sus_es.py` | Calculadora `Pescado` · `Arroz` · `Escandallo` · `Instrucciones` (Sonnet, sobre los helpers de la Pollería) + `--autotest` (580 comprobaciones) |
| `plan-sushi/tandas_docx.py` · `docx_sus_es.py` · `BRIEF-REDACTORES.md` · `barrido_es.py` | Herramienta del Word: `GEMELA` = `../plan-taqueria/textos`; `JERGA`, `PISTAS` (10), `PROHIBIDOS` (restos de Taquería, Pollería y Pizzería), `art30_mal` ampliada (RD 1420/2006 sin «derog» y «7 días» = ERROR), `AVISOS` |
| `astro-site/public/dl/plan-negocio-sushi-bar/` | `plan-financiero-sushi-bar.xlsx` · `checklist-apertura-sushi-bar.xlsx` · `calculadora-pescado-arroz-escandallo-sushi-bar.xlsx` · `plan-de-negocio-sushi-bar.docx` (la guía de equivalencias es de la F3) |

## 2. Decisiones que se apartan de la SPEC (y por qué)

1. **`pct_delivery` 0,24 (SPEC 0,25).** La demo §2.11.9 del motor prueba la sensibilidad poniendo la plataforma a 25 %
   (`grupo_a.DIRECCIONES`, `delivery_sup: lambda v: 0.25`): con el caso ya en 0,25 no cambia nada y `main.py` sale con exit 1
   (medido en la vuelta 1). Sin tocar código común, el caso baja a 0,24 (R daba 26 % de plataforma): unos 13 pedidos de
   plataforma y 8,5 para recoger al día; sala 63 %, recogida 13 %, plataforma 24 %; la media de los canales da 20,08 € (≥ los
   20,00 € del caso). El gate de `cifras` ya pedía < 25 % (= Taquería). Cambian en consecuencia las notas de `a.py`, el
   checklist (techo del 24 %) y las pistas.
2. **Food cost teórico 16 %, no 20-22 %.** Con los escandallos de R §2 (todos entre el 9 y el 20 %), la semana ponderada de
   la calculadora sale en **16,1 %** (`FC_PONDERADO`): el «20-22 %» de R §0.4/§2 no lo sostiene su propia tabla. **El caso se
   queda en el 29 %** (lado prudente; la Guía Restaurante Japonés da 30-35 % para un japonés con pescado de calidad) y el
   puente deja de ser aritmético (+4 +1 +2 +1): Word, `a.py` y calculadora dicen lo mismo, sin puntos inventados: merma de
   vitrina y recorte, sobrepeso de neta y shari, shari/nori/salsas tirados, comidas del personal e invitaciones, menú del
   día y precios del pescado estimados; «mide tu consumo el primer trimestre; cada punto vale {PUNTO_FOOD_COST_A1}»
   (4.029 €). Bajar el caso al 26 % habría subido el neto al ≈ 11 % sobre un escandallo con fuentes 🟡: no compensa.
3. **«validado/a» y «tapa» fuera** (prohibidos de la familia): «temperatura justificada ante sanidad», «APPCC que lo
   justifique», «cierre» del envase.
4. **`PROHIBIDOS`**: sale `cubeta` (la vitrina de sushi va en cubetas GN); no entra `espada` (pez espada); entran los restos
   de la Pollería (`poller`, `asador de pollos`, `pollo a la brasa`, `pollo asado`, `broaster`) y `pan común` (el sushi bar no
   vende pan). `art30_mal` caza también el RD 1420/2006 sin «derog» a ±160 caracteres y «7 días» junto a anisakis o
   congelación (= ERROR en `check`, `barrido` y `docx`).
5. **Préstamo 131.000 €** (SPEC ≈ 128.000 €): con 128.000 € RD-34 dio −2.359 € (−1,3 %); con 131.000 €, +596 € (0,3 %).
6. **Calculadora** (Sonnet): rótulos «Gyozas (6 piezas)», «Edamame (ración)», «Mochi (2 piezas)» (el gate de formatos marca
   «unidades» como recuento); el umbral «el entero compensa» va en rótulo + celda (A34/B34), no en una frase con el número.

## 3. Calibración (1 vuelta de 3)

Vuelta 1 (SPEC tal cual): `main.py` exit 1 por la demo §2.11.9 (plataforma = 25 %) y RD-34 (−1,3 %). Vuelta 2: plataforma
0,24 y préstamo 131.000 € → `ciclo.sh` **TODO VERDE** y `cifras_sus_es.py --calc` **D9 VERDE** (19/19), sin ninguna palanca
de R §3 (holgura A1 27,8 % ≥ 15 %; neto 9,1/10,4/9,8 %, dentro de 7-12 %).

## 4. Cifras del caso (`cifras_caso_es.json`, 192 tokens, con `--calc` de la calculadora de `dl/`)

- Ventas **474.000 / 502.440 / 522.538 €** (79 × 20,00 € × 300) · margen bruto 58,2 % · mercancía 28,9 % · personal
  159.722 € (33,7 %; 7 filas, 5,35 jornadas) · alquiler 4,1 % · EBITDA 67.859 € (14,3 %).
- Neto **43.149 € (9,1 %) / 52.106 € (10,4 %) / 51.086 € (9,8 %)**.
- Partidas + imprevistos 103.350 € · CAPEX 109.750 € · fondo 53.908 € · inversión 163.658 € · IVA 21.746 € ·
  **necesidad 185.404 €** · 55.000 € propios + **131.000 €** · exceso 596 € (0,3 %) · cuota 26.641 € · **DSCR mín. 2,52**.
- Equilibrio contable 65 comensales (holgura 22,6 %); caja 62 / 69 / 71 · **holgura A1 27,8 %** (21,5 / 23,3 %).
- **Saldo mínimo 68.304 € en el Mes 1 (enero)** · cierre 144.399 € · payback **2,5** (número; 1,7 sobre el CAPEX) ·
  cobertura 114 % · rotación 2,2 (techo 3,0; equilibrio de caja 1,72; sala sola 1,25) · IVA bebida 10,8 % (H 7 %).
- Escenarios 381.140 € (neto −3.234 €) / 576.450 € (+93.788 €).
- Calculadora: kilo útil 14,29 € (salmón entero) · 24,16 € (lomo) · 28,81 € (atún) · 2,42 kg de shari por kg de arroz ·
  **121 nigiris por kilo** · 4,9 kg de arroz al día · nigiri de salmón 11,3 % · combinado de 24 15,9 % · ponderado 16,1 % ·
  margen del combinado de 24: 22,16 € en sala, 16,12 € en plataforma.

## 5. Gates (VPS, 31-oct)

`ciclo.sh`: exit 0, **TODO VERDE** (idempotencia · caché 682/741 · data_only 693 + 59 «""», 0 fallos · blancos 0 · §9
**13/13** · C2 80 ítems · censo `--fail` 0 · moldes 30/30 · 16/16 protegidas · demos 2.11 ok). `cifras_sus_es.py --calc`:
**D9 VERDE** (19). `calculadora_sus_es.py --autotest`: **580 comprobaciones VERDE**. `barrido_es.py` sobre los 3 xlsx:
**0**, 3 avisos revisados (−18 °C «no sirve para el anisakis» y dos «no prometer sin gluten»: correctos).
`gate_restos_ft.py --rx-extra` (Taquería, Pollería, Pizzería y pids): **VERDE**. `parche_xml_xlsx.py --check` en los 3
xlsx: **LIT255 VERDE**. Word: `tandas_docx.py check` a y b **0 errores** (8 + 9 avisos revisados: longitud de los párrafos
legales, «no se promete sin gluten», «−18 °C no sirve», franquicias sólo como comparación) · `docx_sus_es.py` **VERDE**
(131 párrafos, 10 Heading 1, 7.663 palabras) · barrido de los 4 ficheros **0** (15 avisos, todos usos correctos) ·
`gate_restos_ft.py` 4 ficheros **VERDE**. Tras la revisión, todo regenerado: tokens del Excel idénticos al JSON del Word
(`cmp`). sha256 Mac = VPS: calculadora `f371fe16…`, checklist `db87cd9e…`, Word `ac6a4994…`, plan `9d6c2fdc…`.

## 7. Word y revisión

- Redacción: 2 Sonnet en serie (`sus_es_a` 29 párrafos, `sus_es_b` 32; ≤ 4 rondas de `check` cada uno). El redactor B cazó
  que «en plataforma el margen del combinado cae casi a la mitad» (pista §10 y checklist F5) no casa con la calculadora
  (22,16 → 16,12 €, −27 %): ahora «cae más de un cuarto» en las dos fuentes.
- Revisión adversarial Opus (`REVISION-FINAL.md`): **0 B · 1 M · 24 m** (21 arreglados, 4 aceptados), sin mover cifras ni
  fórmulas. M1: el ticket por canal decía «un combinado de 24 piezas y un extra, 27,00 €» con el combinado a 29,00 € y
  «plataforma un 15 % más cara» sin casar con 15,34 × 1,15: reescrito (Word [49] y `Supuestos!C5`).

## 8. Para la F3 ES (landing, dashboard, correo)

- **Nombre** «Plan de Negocio: Sushi Bar» · 35 € · nº 58 · `calculadora-sushi` = `calculadora-pescado-arroz-escandallo-sushi-bar.xlsx`.
- **Recuentos**: plan de 10 secciones (131 párrafos, unas 7.700 palabras) · Excel de **9 hojas** · checklist de **80
  tareas** en 6 fases (12/15/14/13/13/13; pestañas «F1 - Constitución», «F2 - Local, frío y extracción», «F3 - Pescado, arroz
  y sanidad», «F4 - Personal y alérgenos», «F5 - Carta, marca y delivery», «F6 - Apertura y 90 días») · calculadora de **4
  hojas** (`Pescado` · `Arroz` · `Escandallo` con **14 productos** · `Instrucciones`) · bonus guía de equivalencias.
- **Claims con cifra del Excel** (FAQ de R §6): inversión **163.658 €** (partidas 103.350 €) y necesidad de caja **185.404
  €** (55.000 € propios + 131.000 €) · neto **9,1 %** el año 1 (43.149 €; 10,4/9,8 % los años 2 y 3) · equilibrio de caja
  **62 comensales/día** (holgura 27,8 %) · **121 nigiris por kilo de arroz crudo** (2,42 kg de shari) · sushiman: ofertas
  de 12.000-22.000 €/año, el caso 1.650 €/mes en 14 pagas · franquicias 39.950-300.000 € (emprendedores.es) frente al caso.
- **Repetir en la landing** lo que arregló la revisión: el ticket por canal sin «combinado de 24 + extra = 27 €»; la regla
  del 21 % entera (cerveza, sake, vino y refrescos con azúcares o edulcorantes añadidos que salen del local); el lomo
  comprado a **24,16 €/kg útil**; plataforma **24 %** (no 25-26 %); el margen de plataforma cae **más de un cuarto**; food
  cost teórico **16 %** frente al **29 %** prudente del plan (no «20-22 %»); RD 1420/2006 sólo como derogado; shari a
  temperatura ambiente sólo con el art. 30.5 del RD 1086/2020; nada de «sushi grade».


## 6. Comandos

Mac: código y `git push` · VPS: `git fetch && git merge --ff-only` (antes, `rm` de lo subido con `scp` y sin commitear) →
`bash ciclo.sh` → `calculadora_sus_es.py --salida /root/tmp-sus-f2/calc [--autotest]` → `cifras_sus_es.py --xlsx
<dryrun>/plan-financiero-sushi-bar.xlsx --calc <calc>/calculadora-…xlsx --salida /root/tmp-sus-f2/cifras_caso_es.json` →
`barrido_es.py <xlsx…>` → `../catering-es-2_0/gate_restos_ft.py <dir> --rx-extra '<restos>'` → `parche_xml_xlsx.py
--check` · `tandas_docx.py preparar` y `check` en el VPS (el Mac no ejecuta) · `docx_sus_es.py --salida <dir>`.
