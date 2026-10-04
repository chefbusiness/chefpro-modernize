# Kit Gestión de Personal y Turnos v2.0 (ES) — inventario de F1 para Restaurant Staff Scheduling Kit Pro (EN)

> Sesión Claude Code, 3-oct-2026. Fuente = los **9 xlsx PUBLICADOS** de `astro-site/public/dl/kit-gestion-personal/`
> (sha256 de cada uno en `censo_es.json`), nunca un generador. Todos los recuentos salen de `extraer_textos.py`
> (`censo_es.json` + `textos_es.json`) y `gate_f1.py` comprueba que la tabla §0 coincide con el censo. Celdas
> citadas como `libro:Hoja!celda`. Los defectos heredados (§3) NO se corrigen en el ES desde esta carpeta.

## 0. Totales del kit (censo)

| Libro | Hojas | Texto | Fórmulas | Fx→hoja | DV | CF | Merges | Protegidas | Fechas | Horas | Fmt € | Textos € | Norma ES | Verdes | Desbloq. |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 01-cuadrante-turnos-semanal | 4 | 163 | 1757 | 1200 | 9 | 44 | 15 | 3 | 0 | 0 | 0 | 0 | 6 | 1384 | 1384 |
| 02-control-horas-extras | 3 | 52 | 1085 | 420 | 7 | 8 | 6 | 2 | 300 | 600 | 34 | 2 | 9 | 2163 | 2163 |
| 03-coste-laboral-mensual | 4 | 114 | 142 | 1 | 8 | 0 | 14 | 3 | 0 | 0 | 164 | 14 | 9 | 169 | 169 |
| 04-onboarding-nuevo-empleado | 2 | 227 | 54 | 0 | 1 | 1 | 9 | 1 | 50 | 0 | 0 | 0 | 14 | 202 | 202 |
| 05-planificacion-vacaciones | 5 | 148 | 1145 | 742 | 6 | 23 | 17 | 4 | 415 | 0 | 0 | 0 | 7 | 2526 | 2526 |
| 06-evaluacion-desempeno | 4 | 159 | 66 | 0 | 2 | 12 | 54 | 3 | 8 | 0 | 0 | 0 | 1 | 216 | 216 |
| 07-directorio-plantilla | 3 | 76 | 304 | 150 | 5 | 28 | 14 | 2 | 301 | 0 | 30 | 0 | 22 | 632 | 632 |
| BONUS-01-briefing-cambio-turno | 2 | 78 | 14 | 0 | 3 | 5 | 18 | 1 | 0 | 0 | 13 | 6 | 4 | 145 | 145 |
| BONUS-02-calculadora-plantilla-optima | 3 | 148 | 26 | 5 | 11 | 6 | 18 | 2 | 0 | 0 | 5 | 6 | 2 | 63 | 63 |
| **Total** | **30** | **1165** | **4593** | **2518** | **52** | **127** | **165** | **21** | **1074** | **600** | **246** | **28** | **74** | **7500** | **7500** |

Columnas: «Fechas» / «Horas» = celdas con formato de fecha / de hora (vacías incluidas); «Fmt €» = celdas con formato
de número con €; «Textos €» y «Norma ES» = celdas de texto que citan €/EUR o normativa/administración española
(`RX_MONEDA`, `RX_NORMA` del extractor); «Protegidas» = hojas protegidas (sin contraseña).

Transversal (los 9 libros):
- **Sin gráficos, sin imágenes, sin nombres definidos.** Las 21 hojas de trabajo están **protegidas SIN contraseña**;
  las 9 `Instrucciones`, no. Las 7.500 celdas verdes (`E8F5E9`) son exactamente las 7.500 desbloqueadas.
- 30 hojas, 30 áreas de impresión, 14 títulos de impresión, 17 paneles, 27 columnas ocultas (01 `Cuadrante
  Semanal!R:AR`, cálculo auxiliar). Papel **A4 (`paperSize 9`) en las 30**; pie `AI Chef Pro · aichef.pro ·
  Página &P de &N`; línea de marca `AI Chef Pro · aichef.pro — Kit Gestión de Personal y Turnos` en A2 de las hojas
  de trabajo; `© 2026 AI Chef Pro · aichef.pro` al pie (invariable).
- 52 DV: 24 de lista literal (4.814 celdas con DV en total), 1 personalizada con literales (05 `Calendario
  Anual!B36:BB36` = «Alta»/«Normal»), el resto decimales, fecha, hora y mensajes sin regla.
- 127 CF. Casi todas son **`containsText` con SEARCH** (subcadena y sin distinguir mayúsculas): el semáforo genérico
  del kit es `⛔` / `EXCESO` (rojo) · `⚠` (ámbar) · `OK` (verde) en 01, 02 y 05; el resto lleva tokens propios
  (02 EXCEDE / cerca del límite / dentro; 05 TEMP. ALTA / EXCESO y los códigos V-B-F-PE; 06 las cinco notas; 07
  VENCIDO / URGENTE / PRONTO y 🔴🟡🟢; B01 CUADRA / FALTAN / SOBRAN y CONFORME / FUERA DE RANGO; B02 los dos
  semáforos). **Consecuencia para la EN: un mensaje traducido puede cambiar de color sin que nada falle** («cook»
  contiene «ok»): `mapas.cruzar_censo` lo comprueba literal a literal.
- 4.593 fórmulas en 441 patrones de fila (`mapas.patron`), 2.518 con referencia a otra hoja. 172 literales distintos
  entre fórmulas, CF, DV e ítems de lista: mensajes de alerta, códigos de turno, tipos de negocio (claves de VLOOKUP),
  estados.
- Formatos: `dd/mm/yyyy` (fechas), `dd/mm` (05 fila 5), `hh:mm` (02 entradas y salidas, 600 celdas), 246 celdas con
  `#,##0.00 €` o `€#,##0.00`. Las horas de la tabla de turnos (01 `Turnos!C5:D12`) son **números de 0 a 24**, no horas.
- docProps iguales en los 9 salvo el título («NN · título · Kit Gestión de Personal y Turnos»): `subject` «Kit
  Gestión de Personal y Turnos · v2.0», `keywords` «kit gestion personal, AI Chef Pro», `description`
  «aichef.pro/kit-gestion-personal», `category` «AI Chef Pro · Productos digitales». Versión en las 9
  Instrucciones: «Versión 2.0 · agosto 2026 · aichef.pro/kit-gestion-personal · info@aichef.pro»; firma de autor
  «Diseñado por John Guerrero — chef y consultor gastronómico desde 2010…».
- **Datos de ejemplo**: casi ninguno. Solo la ficha rellena del 06 (`Ficha (ejemplo relleno)!C4:D44`, una jefa de
  partida de cuarto frío), el tipo «Restaurante Casual» del B02 y los valores por defecto de los parámetros.
- Enlaces entre libros (solo en texto): 01 ↔ 05 (mismos códigos V/B), 01 ↔ 07 (aviso de menores), 02 ← 03 (coste
  por hora), 03 ← 02 (coste de horas extra), 03 ↔ B02 (mismos diez tipos y umbrales), 06 ↔ 07 ↔ 01 (30 empleados).

## 1. Contenido específico de España, por libro

| Libro | Lo que es mercado español (y lo que la EN tiene que decidir) |
|---|---|
| 01 | Parámetros `Turnos!B2` = 9 h (jornada ordinaria máx., art. 34.3 ET) y `B3` = 12 h (descanso entre jornadas, art. 34.3 ET; nota sobre la Directiva 2003/88/CE). Códigos M/T/N/P/D/L/V/B; horas como número 0-24 («15,5 = 15:30»). Alertas K (descanso), L (descanso semanal 1,5 días, art. 37.1 ET), M (jornada semanal vs contrato, 40), N (jornada diaria; 8 h si menor), P (menores: sin noche ni doble, art. 6 ET) |
| 02 | Horas extra **diarias** sobre lo contratado (G = 8); tipos Voluntaria / Obligatoria / Fuerza mayor / **Compensada con descanso** / **Complementaria (contrato parcial)**; tope **80 h/año** (art. 35.2 ET) en `Resumen Mensual!F3`; recargo 1,25 «según tu convenio» (art. 35.1); tarifa 12 € ; horas `hh:mm` de 24 h |
| 03 | Cotización empresa **33 %** (CNAE, AT/EP, FOGASA, MEI) en `Nóminas!C2` y `Previsión!B16`; **14 pagas** (DV 12/14/15) prorrateadas; 46,5 semanas efectivas (30 días naturales, art. 38 ET, + 14 festivos); «personal externo / ETT»; diez tipos de negocio españoles con umbrales de ratio; 1.500 €/mes de salario medio; aviso «contrástalo con tu gestoría» |
| 04 | Bloque legal español: alta en Seguridad Social TA.2/S antes de empezar (art. 32.3 RD 84/1996), Contrat@ (SEPE) en 10 días hábiles, copia básica a la RLT, modelo 145 de IRPF, DNI/NIE, RGPD, convenio, PRL y reconocimiento médico, carnet de manipulador, 14 alérgenos, formación en igualdad; plazos «Día -1/1/3/7/15/30» ligados a la fórmula de `H` de cada fila |
| 05 | 30 días **naturales** de vacaciones (art. 38 ET) en `Saldo Vacaciones!B2`; calendario fijado con 2 meses de antelación (art. 38.3); prorrateo para el finiquito; códigos V/B/F/PE; lunes de la semana 1 (`B5` = 4-ene-2027); temporada «Alta»; lista de 14 puestos de hostelería española |
| 06 | Universal (escala 1-5, N/A, histórico trimestral). Localizar solo la ficha de ejemplo (nombre, puesto «Jefa de partida — cuarto frío», «registros APPCC», «cubiertos») |
| 07 | DNI/NIE, NAF (Seguridad Social), grupo profesional y convenio, cinco modalidades de contrato del RDL 32/2021, «Completa/Parcial» (art. 12.4.c ET), carnet de manipulador y PRL como caducidades; bloque **RGPD** (arts. 5, 6, 9, 15-22) y conservación 4 años (art. 34.9 ET, art. 21 LISOS); aviso de menor «sin nocturnidad ni horas extra (art. 6 ET)»; preaviso de 15 días (art. 49.1.c ET) |
| B01 | Arqueo de caja en € con tolerancia 5 € y lectura Z del TPV; temperaturas de cambio de turno en **°C** (cámara 0-4, congelador −30/−18, vitrina 0-4, caliente 65-90) como autocontrol APPCC |
| B02 | Salario medio 1.500 € en 14 pagas, cotización 33 %, ticket medio 25 € «sin IVA»; ejemplo de Instrucciones con cifras derivadas (52.000 € de ventas, 16.292,50 € de coste, 31,3 %); refuerzo con «horas complementarias, fijo-discontinuo o contrato por circunstancias de la producción» |

## 2. Lo que la EN hereda tal cual

- Toda la estructura (hojas, rangos, merges, áreas, títulos, paneles, anchos, colores, celdas verdes, protección sin
  contraseña, columnas ocultas), las cuatro alertas del cuadrante, el cómputo mensual, el saldo y la cobertura de
  vacaciones, la ficha y el histórico de evaluación, las alertas de vencimientos, el arqueo y la calculadora.
- Los 30 empleados por libro, los ratios de cubiertos por puesto y los diez umbrales de ratio de coste laboral
  (reglas del sector, no norma española), las 13 fórmulas de vencimientos y los resúmenes.

## 3. Defectos heredados (no se tocan aquí)

- **I1 · Horas de turno como número** (01 `Turnos!C5:D12`): «7» y «15,5» en vez de horas reales. Funciona, pero no
  admite reloj de 12 h y un «7:00» tecleado como hora rompe el cálculo sin avisar. EN: horas reales (SPEC D8).
- **I2 · Sumas en coma flotante sin redondeo** en el descanso entre jornadas (01 `AM:AR`): con números enteros no
  falla; con horas reales daría 9,9999 < 10. EN: `ROUND(…,2)` (D8).
- I3 · Tokens de CF que ningún mensaje produce (`EXCESO` en los rangos del 01/02/05, `URGENTE`/`PRONTO` en el 07,
  `OK` en 02 F). Cosmético; la EN los conserva para no romper la paridad de CF.
