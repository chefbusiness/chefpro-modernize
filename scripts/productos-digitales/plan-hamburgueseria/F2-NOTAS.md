# Plan de Negocio: Hamburguesería Smash ES 1.0 — F2 (entregables) · calibración, decisiones y gates

> Sesión Claude Code, 31-oct-2026 (F2, decisiones delegadas). SPEC = `F1-camino.md` §2 (firmada por el orquestador), §3-§4 y
> §9. Mac = código y redacción; VPS = motor, openpyxl, python-docx y gates (`/root/wt-smash`, salidas `/root/tmp-ham-f2/`).
> Cero código común (ni `motor.py`, ni `grupo_a.py`, ni `main.py`). Semilla: el Sushi Bar LIVE.

## 1. Ficheros

| Fichero | Qué es |
|---|---|
| `planes-v2_0/contenido_plan_negocio_hamburgueseria/{__init__,a}.py` | Contenido = el del Sushi Bar (rotación ENCENDIDA, techo 3,5, comensal equivalente) con el caso B de R §3, el `VOCABULARIO` de §2 y las notas de R §3 |
| `plan-hamburgueseria/semilla_ham.py` | Semilla sobre el Sushi Bar LIVE (plan + checklist): 18 partidas (99.500 € + imprevistos = 104.350 €), 9 fijos (14.400 €), títulos, docProps |
| `plan-hamburgueseria/datos_checklist.py` | 80 tareas 12/15/14/13/13/13 en «F1 - Constitución» · «F2 - Local, humos y gas» · «F3 - Carne, fritura y sanidad» · «F4 - Personal y alérgenos» · «F5 - Carta, marca y delivery» · «F6 - Apertura y 90 días» |
| `plan-hamburgueseria/ham_version.py` · `main_ham.py` · `ciclo.sh` | 1.0 · noviembre 2026 + `main.py --dry-run --origen` (`SCR=/root/tmp-ham-f2/motor`) |
| `plan-hamburgueseria/cifras_ham_es.py` | 199 tokens (`cifras_caso_es.json`) + D9 + Mes 1 = enero; `--calc` lee el `EXPUESTOS` de la calculadora |
| `plan-hamburgueseria/calculadora_ham_es.py` | Calculadora `Carne` · `Patatas` · `Escandallo` (14 productos) · `Instrucciones` + `--autotest` (644 comprobaciones). Sin `--autotest` genera; con él, solo prueba el fichero que ya hay |
| `plan-hamburgueseria/tandas_docx.py` · `docx_ham_es.py` · `BRIEF-REDACTORES.md` · `barrido_es.py` · `textos/ham_es_{a,b}.json` | Herramienta del Word (61 ranuras en 2 tandas: a §1-5, 29 párrafos; b §6-10, 32), `PROHIBIDOS` (Sushi, Taquería, Pollería, Pizzería y errores legales de la carne) y `AVISOS` |
| `astro-site/public/dl/plan-negocio-hamburgueseria/` | `plan-financiero-hamburgueseria.xlsx` · `checklist-apertura-hamburgueseria.xlsx` · `calculadora-carne-patatas-escandallo-hamburgueseria.xlsx` · `plan-de-negocio-hamburgueseria.docx` (la guía de equivalencias es de la F3) |

## 2. Decisiones que se apartan de la SPEC (y por qué)

1. **Suministros 1.100 €/mes (SPEC 1.150 €).** Con 1.150 € la demo §2.11.5 salía con exit 1: en la ventana de 74 comensales el
   resultado de los 3 años daba −80 € y el año 3 no tributaba. Con 1.100 €, +1.720 €. Es la única palanca tocada; comensales,
   ticket, días y préstamo son los firmados.
2. **Ticket de plataforma 33,47 € con IVA** (29,10 × 1,15 = 33,465; 26,45 € y 30,42 € sin IVA; 17,90 € por comensal equivalente).
   La SPEC decía 33,45 / 26,46 / 30,43 € y no cuadraba al céntimo. Word [49] y `Supuestos!C5` dicen lo mismo.
3. **RD-34: exceso de 943 € (0,5 %)** con el préstamo firmado de 130.000 € (la cuenta a mano de la SPEC daba 795 €, 0,4 %; dentro
   del ± 1.000 €).
4. **`PROHIBIDOS` ajustados**: `helad` fuera (el helado de los batidos es del caso); «pan común» pasa a aviso (sólo para decir que
   el pan de hamburguesa no lo es); `mochi` como palabra entera; `(?<!\d)75 ?°C` y `(?<!\d)68 ?°C` (para no cazar 175 °C ni 168).
5. **Calculadora**: margen del menú en plataforma **7,41 €** (no 7,43 de la SPEC: es el que da el escandallo); bolas porcionadas en
   €/kg; **sin «relleno diario» del aceite** (se quitó porque contradecía «nada añadido al baño»; la revisión leyó la Orden de
   26-1-1989 en origen: el art. 9.1 solo veta «sustancias u objetos extraños», así que reponer con aceite autorizado es legal; el
   checklist F3!E14 conserva el «rellena» y la calculadora no lo necesita, porque el aceite que absorbe la ración ya está en el coste);
   selectores de carne y de patata (`Escandallo!B8/B9`); pedido tipo «2 dobles + 2 patatas»; autotest de 644 comprobaciones.
6. **Revisión** (`REVISION-FINAL.md`, una ronda): 0 B · 4 M · 10 m arreglados, sin mover cifras. Lo que cambia la letra de los
   ficheros: aceite (M1), carne madurada (M2), puente del food cost sin puntos (M3), «28 %%» de la calculadora (M4).

## 3. Calibración

Vuelta con la SPEC: demo §2.11.5 en exit 1 (§2.1). Con suministros a 1.100 €: `ciclo.sh` **TODO VERDE** y `cifras_ham_es.py --calc`
**D9 VERDE**, sin ninguna palanca de R §3: neto 10,2 / 11,4 / 10,7 % (dentro de 7-12 %; el alquiler de 1.700 € no hizo falta),
holgura de caja del año 1 30,9 % (≥ 15 %), DSCR 2,64 (≥ 1,25).

## 4. Cifras del caso (`cifras_caso_es.json`, 199 tokens, con `--calc` de la calculadora de `dl/`)

- Ventas **456.000 / 483.360 / 502.694 €** (95 × 16,00 € × 300) · margen bruto 59,5 % · mercancía 27,5 % · personal 152.274 € (33,4 %;
  7 personas, 5,35 jornadas) · alquiler 3,9 % · EBITDA 71.854 € (15,8 %).
- Neto **46.512 € (10,2 %) / 55.244 € (11,4 %) / 53.709 € (10,7 %)**.
- Partidas + imprevistos 104.350 € · CAPEX 110.350 € · fondo 51.794 € · **inversión total 162.144 €** · IVA 21.914 € · **necesidad
  184.057 €** · 55.000 € propios + **130.000 €** · exceso 943 € (0,5 %) · cuota 26.437 € · **DSCR mín. 2,64** (2,74 el año 2).
- Equilibrio contable 76 comensales (holgura 25,3 %); **de caja 73** / 82 / 84 · **holgura 30,9 %** / 24,0 / 25,7 %.
- Saldo mínimo 61.952 € en el Mes 1 (enero) · cierre 144.816 € · payback 2,4 (1,6 sobre el CAPEX) · cobertura 109 % · **rotación
  2,64** (techo 3,5; equilibrio de caja 2,02; sala sola 1,46) · IVA de la bebida 13,1 % (28 % de la bebida = 4,5 % de las ventas al 21 %).
- Escenarios 359.900 € (neto −2.441 €) / 561.963 € (+100.084 €) · cada punto de food cost 3.830 €.
- Calculadora: kilo útil 9,18 € (blend picado) · 8,59 € (pieza, sin mano de obra) · **10 bolas de 100 g por kilo** (9,7 con la merma de
  cierre) · 15,2 kg de carne al día · simple 1,80 € (22,2 %) · doble 2,90 € (26,8 %) · patata congelada 0,28 € (fresca 0,19 €) · aceite
  0,05 € por ración · ponderado **24,4 %** · margen del menú 10,83 € en sala, 10,38 € para llevar y 7,41 € en plataforma (−31,6 %).

## 5. Gates (VPS, 31-oct, tras la revisión)

`ciclo.sh`: exit 0, **TODO VERDE** (moldes, idempotencia, caché, blancos contaminados, §9, censo `--fail` 0, demos, 16/16 protegidas).
`calculadora_ham_es.py --salida …` y `--autotest`: **644 comprobaciones VERDE**. `cifras_ham_es.py --calc`: **199 tokens, D9 VERDE**, 0
distintos del `cifras_caso_es.json` del repo. Word: `tandas_docx.py check` a **0 errores** (9 avisos) y b **0 errores** (16 avisos:
longitud de los párrafos legales, «sin gluten» no prometido, madurada como prohibición, franquicias como comparación) ·
`docx_ham_es.py` **VERDE** (131 párrafos, 10 Heading 1, 8.096 palabras). `barrido_es.py` sobre los 4: **0 coincidencias** (30 avisos,
todos usos correctos). `gate_restos_ft.py --rx-extra` (Sushi, Taquería, Pollería, Pizzería y pids; `--permitir 'Plan de Negocio: Food
Truck'`): **VERDE**. `parche_xml_xlsx.py --check` en los 3 xlsx: **LIT255 VERDE**, 0 cambios. sha256 Mac = VPS: calculadora
`f092a79b…`, checklist `f997c9a6…`, Word `0ea51bd9…`, plan `05eb9365…` (el plan, el checklist y el Word no son deterministas byte a
byte: cada regeneración cambia el sha por las fechas internas; el contenido no).

## 7. Word y revisión

- Redacción: 2 Sonnet (`ham_es_a` 29 párrafos, `ham_es_b` 32) con el `check` a 0 errores.
- Revisión adversarial (`REVISION-FINAL.md`): **0 B · 4 M · 10 m** (los 14 arreglados) + 6 aceptados. M1 aceite: «sin añadir aceite
  nuevo al baño usado» era una obligación que la Orden no pone. M2 madurada: «no se puede ofrecer/vender como reclamo» falseaba
  Inf26008. M3 `Supuestos!C13`: puente 24 → 28 % con puntos inventados. M4 «28 %%» visible en `Escandallo!A42`.

## 8. Para la F3 ES (landing, dashboard, correo)

- **Nombre** «Plan de Negocio: Hamburguesería Smash» · 35 € · nº 59 · clave **`calculadora-hamburguesa`** =
  `calculadora-carne-patatas-escandallo-hamburgueseria.xlsx`.
- **Recuentos**: plan de 10 secciones (131 párrafos, unas 8.100 palabras) · Excel de **9 hojas** · checklist de **80 tareas** en 6 fases
  (12/15/14/13/13/13; pestañas de §1) · calculadora de **4 hojas** (`Carne` · `Patatas` · `Escandallo` con **14 productos** ·
  `Instrucciones`) · bonus guía de equivalencias.
- **Claims con cifra del Excel**: inversión **162.144 €** (partidas 104.350 €) y necesidad de caja **184.057 €** (55.000 € propios +
  130.000 €) · neto **10,2 %** el año 1 (46.512 €; 11,4 / 10,7 % los años 2 y 3) · equilibrio de caja **73 comensales equivalentes al día**
  (holgura 30,9 %; 24,0 % el año 2) · **10 bolas de 100 g por kilo = 5 dobles** · 15,2 kg de carne al día · doble 2,90 € (26,8 %) · margen
  del menú 10,83 → 7,41 € en plataforma (casi un tercio) · plataforma con techo del 24 % · franquicias 200.000-300.000 € (La Pepita
  250.000 €, emprendedores.es) frente a los 162.144 € del caso.
- **Repetir en la landing** lo que arregló la revisión: la «dry aged burger» fuera porque **no se puede elaborar carne picada con carne
  madurada más de 15 días** (Inf26008), nunca «como reclamo»; el aceite: polares < 25 % y **nada ajeno al aceite añadido al baño** (no
  «sin añadir aceite nuevo»), sin medidor obligatorio; food cost teórico **24,4 %** frente al **28 %** prudente, «unos 4 puntos» sin
  desglose; la regla del 21 % entera (cerveza y refrescos con azúcares o edulcorantes añadidos, también los zero, que salen del local;
  el batido al 10 % 🟡); la AESAN literal (70 °C o más durante al menos 2 minutos, recomendación) y **ninguna temperatura legal de
  cocción**; la plataforma «al 33 %» = 12.300 € más (no «un tercio»); la plancha de 60 a 80 cm, 771-1.399 €.

## 6. Comandos

Mac: código y `git push` · VPS: `git fetch -q && git merge --ff-only origin/feat/plan-negocio-hamburgueseria` (antes, `git checkout --`
de lo subido con `scp` y sin commitear) → `bash ciclo.sh` → `calculadora_ham_es.py --salida /root/tmp-ham-f2/calc` y después
`--autotest` → `cifras_ham_es.py --xlsx <dryrun>/plan-financiero-hamburgueseria.xlsx --calc <calc>/calculadora-…xlsx --salida <tmp>`
(y comparar los tokens con el del repo) → `tandas_docx.py check --tanda ham_es_a|ham_es_b` (desde `/root/wt-smash`) →
`docx_ham_es.py --salida /root/tmp-ham-f2/docx` → `barrido_es.py <los 4>` → `../catering-es-2_0/gate_restos_ft.py <dir> --rx-extra
'<restos>' --permitir 'Plan de Negocio: Food Truck'` → `parche_xml_xlsx.py --check <xlsx…>` → copiar a `dl/` y `sha256sum`.
