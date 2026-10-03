# Kit Plan Financiero v2.0 (ES) — inventario de F1 para Restaurant Financial Plan Kit Pro (EN)

> Sesión Claude Code, 3-oct-2026. Fuente = los **10 xlsx PUBLICADOS** de `astro-site/public/dl/kit-plan-financiero/`
> (sha256 de cada uno en `censo_es.json`), nunca el generador `kit-plan-financiero-v2_0/`. Todos los recuentos salen de
> `extraer_textos.py` (`censo_es.json` + `textos_es.json`) y `gate_f1.py` comprueba que la tabla §0 coincide con el
> censo. Celdas citadas como `libro:Hoja!celda`. Los defectos heredados (§3) NO se corrigen en el ES desde esta carpeta.

## 0. Totales del kit (censo)

| Libro | Hojas | Texto | Fórmulas | Fx→hoja | DV | CF | Gráficos | Merges | Protegidas | Fechas | Fmt € | Textos € | Norma ES | Verdes | Desbloq. |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 01-plan-financiero-previsional | 5 | 143 | 244 | 9 | 6 | 1 | 1 | 9 | 5 | 0 | 594 | 0 | 17 | 399 | 399 |
| 01b-plan-financiero-previsional-5-anos | 7 | 219 | 404 | 15 | 10 | 1 | 1 | 13 | 7 | 0 | 990 | 0 | 27 | 665 | 665 |
| 02-calculadora-punto-equilibrio | 4 | 87 | 67 | 34 | 3 | 1 | 1 | 3 | 4 | 0 | 63 | 11 | 12 | 12 | 21 |
| 03-cash-flow-forecast | 4 | 121 | 201 | 84 | 5 | 3 | 1 | 4 | 4 | 0 | 374 | 1 | 24 | 203 | 203 |
| 04-presupuesto-inversion-capex | 8 | 181 | 300 | 29 | 12 | 1 | 1 | 12 | 8 | 0 | 343 | 39 | 30 | 267 | 267 |
| 05-pyl-mensual-real-vs-presupuesto | 14 | 492 | 1034 | 348 | 13 | 37 | 1 | 26 | 14 | 0 | 720 | 43 | 63 | 292 | 292 |
| 06-dashboard-ratios-financieros | 3 | 137 | 41 | 27 | 1 | 6 | 1 | 3 | 3 | 0 | 18 | 19 | 6 | 13 | 13 |
| 07-informe-viabilidad-bancos | 6 | 161 | 102 | 16 | 7 | 4 | 1 | 6 | 6 | 1 | 132 | 15 | 16 | 69 | 69 |
| BONUS-08-simulador-escenarios | 3 | 51 | 39 | 15 | 2 | 2 | 1 | 5 | 3 | 0 | 39 | 5 | 5 | 18 | 18 |
| BONUS-09-checklist-pre-apertura | 2 | 198 | 5 | 0 | 1 | 3 | 0 | 2 | 2 | 60 | 0 | 0 | 18 | 144 | 240 |
| **Total** | **56** | **1790** | **2437** | **577** | **60** | **59** | **9** | **83** | **56** | **61** | **3273** | **133** | **218** | **2082** | **2187** |

Columnas: «Fechas» = celdas con formato de fecha (vacías incluidas); «Fmt €» = celdas con formato `#,##0.00 €`; «Textos €»
y «Norma ES» = celdas de texto que citan €/EUR o fiscalidad/administración española (`RX_MONEDA`, `RX_NORMA`);
«Protegidas» = hojas protegidas (sin contraseña).

Transversal (los 10 libros):
- **Las 56 hojas están protegidas SIN contraseña, Instrucciones incluidas.** 2.082 celdas verdes (`E8F5E9`), todas
  desbloqueadas; además hay 105 desbloqueadas SIN verde (02, 9; BONUS-09, 96). La EN las conserva tal cual (paridad).
- **9 gráficos** (todos los libros menos el BONUS-09), 20 series, con título en español y título de eje «€» (el del 06
  es «%»). Leídos del ZIP (`extraer_textos.graficos`): hoja ancla, tipo, título, referencias (citan las pestañas por
  nombre: el renombrado tiene que reescribirlas) y caché de textos (vacía en los 9).
- Sin imágenes ni nombres definidos. 0 áreas de impresión, 41 títulos de impresión, 42 paneles. Papel **A4
  (`paperSize 9`)** en las 56; pie `AI Chef Pro · aichef.pro · Página &P de &N`; marca `AI Chef Pro · aichef.pro — Kit
  Plan Financiero para Restaurantes` en A2/B2/B4; `© 2026 AI Chef Pro · aichef.pro` al pie (invariable).
- 60 DV: 1 de lista (BONUS-09 `Checklist!F5:F64` «Pendiente,En curso,Completada»), el resto decimales (≥ 0, 0-1,
  importes que admiten negativo). En el 04 cada pestaña de inversión tiene UNA DV 0-1 que cubre a la vez el IVA % (C) y
  el coeficiente de amortización (H).
- 59 CF: `containsText` con SEARCH (03 «BAJO MÍNIMO»/«OK», 05 ✅ OK / ⚠️ Atención / 🔴 Alerta ×13, 06 seis estados,
  07 ✅/⚠️/🔴, BONUS-09 tres estados) y `expression` (negativos en rojo, saldo bajo umbral, DSCR bajo límite).
- 2.437 fórmulas en 1.172 patrones de fila (`mapas.patron`), 577 con referencia a otra hoja. 38 literales distintos
  (mensajes «Indica …», estados del semáforo, «No se recupera en 5 años», «La carencia no puede…»).
- **La TIR (07 `Proyecciones!B24`, `IRR`) no la evalúa pycel**: el ES la cachea aparte por Newton-Raphson
  (`kit-plan-financiero-v2_0/main.py`, `cachear_irr()`); la F2-EN tiene que repetir ese paso tras `inject_cache`.
- Formatos: `#,##0.00 €` (3.273), `0.0%`, `0%`, `0.0" p.p."` (64), `dd/mm/yyyy` (61), `0.00"x"`, `0.00" años"`.
- docProps iguales salvo el título («NN · título · Kit Plan Financiero para Restaurantes»): `subject` «Kit Plan
  Financiero para Restaurantes · v2.0», `keywords` «kit plan financiero, plan de negocio restaurante, …»,
  `description` «aichef.pro/kit-plan-financiero», `category` «AI Chef Pro · Productos digitales».
- **Datos de ejemplo = números**, coherentes entre libros: ticket 22, 55 cubiertos/día, 26 días (02, BONUS-08),
  ventas 31.460 al mes y EBITDA ≈ 17,3 % (02, 06, BONUS-08), saldo inicial 15.000 y umbral 5.000 (03), tasa de
  descuento 8 % e IS 25 % (07). El 07 deja vacíos a propósito importe del préstamo e inversión («ningún dato de ejemplo
  con aspecto de dato real»).

## 1. Contenido específico de España, por libro

| Libro | Lo que es mercado español (y lo que la EN tiene que decidir) |
|---|---|
| 01 / 01b | «(sin IVA)» en las líneas de ingreso; comisión de plataformas 30 % (`Año n!B27`, regla del sector) |
| 02 | Personal fijo «salario bruto + SS empresa», «≈ bruto × 1,32»; «gestoría»; ticket «(€, sin IVA)» |
| 03 | `Parámetros`: tarjeta 65 %, abono D+n, IVA repercutido 10 % y soportado 10 % / 21 %; calendario del **modelo 303** (liquidación trimestral en abril, julio y octubre: `Flujo Mensual!E25`, `H25`, `K25`); SS del mes anterior (fila 18 ← fila 34), **retenciones IRPF mod. 111** (fila 24); cobros y pagos CON IVA |
| 04 | Columnas Base / **IVA %** (21 %) / IVA / Total con IVA; **coeficientes de amortización** fiscales (obra 3 %, cocina 12 %, mobiliario 10 %, tecnología 25 %, `I = B × H`); licencias españolas (apertura, obras, proyecto técnico, certificado energético, autoprotección, Hacienda/SS, registro sanitario, SGAE); traspaso, fianza, notaría; «IVA soportado se recupera vía 303» |
| 05 | «(sin IVA)»; meses en pestañas (Ene…Dic); desviaciones de ratios en «p.p.» |
| 06 | Superficie en **m²** (`Ratios!C11` = 80, ventas por m²); RevPASH en «€/plaza/hora»; benchmarks del sector español (labor < 25 % / > 30 %, alquiler < 8 % / > 12 %) |
| 07 | «Presentación Bancaria»; **Impuesto sobre Sociedades** 25 % con nota art. 29.1 LIS (15 % nueva creación, IRPF del autónomo); préstamo con **TIN/TAE** y **carencia** (6 %, 8 años); «ICO de apertura»; ratios con «Referencia Bancaria»; garantías **SGR**, seguro de caución, pignoración; m² |
| BONUS-08 | «(€, sin IVA)», «gestoría»; números comunes con el 02 |
| BONUS-09 | 54 tareas: SL/autónomo, notario, Registro Mercantil, NIF/CIF, modelo 036/037, OEPM, ICO, subvenciones autonómicas, licencia de actividad, RGSEAA, plan de autoprotección, DDD, Veri*factu, SS/CCC, RETA, convenio provincial, mod. 111 |

## 2. Lo que la EN hereda tal cual

- Toda la estructura (hojas, rangos, merges, títulos de impresión, paneles, anchos, colores, verdes, protección sin
  contraseña, gráficos con sus series y anclas), las fórmulas de proyección, punto de equilibrio, tesorería (desfase de
  tarjeta y de proveedores, saldo encadenado, liquidación trimestral), CAPEX, P&L con semáforo con signo, ratios con
  umbrales en `Benchmarks!F:G`, P&L y flujos del 07 (TIR/VAN/payback del proyecto sin deuda, DSCR sobre la fila 17,
  cuadro francés con carencia y vencimiento), simulador y checklist con contador honesto.
- Los números de ejemplo (moneda neutra) y sus cifras derivadas citadas en texto (17,3 %, 31.460, 6.200, 22, 55, 26).

## 3. Defectos heredados (no se tocan aquí)

- **I1 · `0.0" p.p."` muestra 0,0 para dos puntos** (64 celdas: 05 `Ene..Dic!D24`, `D27:D30` y `Resumen Anual!B24:B25`):
  el valor es una fracción (0,02) y el formato no multiplica por 100. EN: `0.0%` (SPEC D18). Proponer al ES su v2.x.
- **I2 · Título de docProps del BONUS-09 dice «48 Tareas»** con 54 en la hoja. EN nace con 54 (D5).
- **I3 · `06 Benchmarks!B17` dice que los textos C:E «se generan» desde F:G**, pero son texto fijo. EN: se reescribe como
  guía de lectura (FIJOS) sin cambiar la estructura.
- I4 · 105 celdas desbloqueadas sin relleno verde (02, BONUS-09). Cosmético; la EN conserva la paridad.
