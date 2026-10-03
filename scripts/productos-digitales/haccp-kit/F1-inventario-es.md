# Pack Plantillas APPCC v2.0 (ES) — inventario de F1 para HACCP Food Safety Kit Pro (EN)

> Sesión Claude Code, 3-oct-2026. Fuente = los **21 xlsx PUBLICADOS** de `astro-site/public/dl/pack-appcc/`
> (sha256 de cada uno en `censo_es.json`), nunca un generador. Todos los recuentos salen de `extraer_textos.py`
> (`censo_es.json` + `textos_es.json`) y `gate_f1.py` comprueba que la tabla §0 coincide con el censo. Celdas
> citadas como `libro:Hoja!celda`. Los defectos heredados (§3) NO se corrigen en el ES desde esta carpeta.

## 0. Totales del pack (censo)

| Libro | Hojas | Texto | Fórmulas | Fx→hoja | DV | CF | Merges | Fechas | Fechas texto | Nº ejemplo | Textos °C | Norma ES | Verdes | Áreas |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 01-registro-temperaturas-diario | 2 | 155 | 85 | 0 | 1 | 37 | 10 | 0 | 0 | 6 | 22 | 2 | 336 | 2 |
| 02-registro-temperaturas-recepcion | 3 | 89 | 80 | 40 | 3 | 4 | 7 | 0 | 3 | 12 | 15 | 11 | 368 | 3 |
| 03-plan-limpieza-desinfeccion | 3 | 375 | 1 | 0 | 3 | 25 | 19 | 0 | 0 | 0 | 3 | 6 | 534 | 3 |
| 04-registro-limpieza-diaria | 2 | 98 | 1 | 0 | 2 | 46 | 64 | 0 | 1 | 0 | 1 | 2 | 362 | 2 |
| 05-checklist-recepcion-mercancias | 2 | 77 | 0 | 0 | 2 | 6 | 4 | 0 | 5 | 3 | 1 | 2 | 560 | 2 |
| 06-registro-trazabilidad | 3 | 82 | 0 | 0 | 0 | 0 | 9 | 120 | 11 | 0 | 0 | 8 | 640 | 3 |
| 07-control-plagas-ddd | 3 | 133 | 1 | 0 | 4 | 4 | 13 | 0 | 22 | 43 | 0 | 8 | 1080 | 3 |
| 08-matriz-alergenos | 2 | 186 | 415 | 0 | 2 | 4 | 8 | 0 | 0 | 0 | 0 | 4 | 3400 | 2 |
| 09-control-aceite-fritura | 3 | 61 | 40 | 0 | 3 | 3 | 9 | 0 | 4 | 7 | 4 | 7 | 424 | 3 |
| 10-control-agua-potable | 2 | 48 | 31 | 0 | 3 | 3 | 5 | 0 | 3 | 2 | 0 | 4 | 186 | 2 |
| 11-registro-acciones-correctivas | 2 | 162 | 1 | 0 | 4 | 7 | 8 | 0 | 13 | 0 | 7 | 2 | 480 | 2 |
| 12-analisis-peligros-haccp | 2 | 304 | 34 | 0 | 3 | 3 | 10 | 0 | 0 | 0 | 13 | 14 | 372 | 2 |
| 13-checklist-higiene-personal | 2 | 69 | 0 | 0 | 0 | 0 | 5 | 0 | 0 | 0 | 0 | 6 | 0 | 2 |
| 14-fichas-14-alergenos | 2 | 80 | 0 | 0 | 0 | 0 | 18 | 0 | 0 | 24 | 0 | 6 | 0 | 2 |
| 15-guia-inspeccion-sanidad | 2 | 148 | 7 | 0 | 5 | 33 | 50 | 0 | 0 | 53 | 5 | 11 | 25 | 2 |
| 16-registro-coccion-regeneracion | 2 | 51 | 40 | 0 | 5 | 3 | 7 | 80 | 0 | 12 | 9 | 4 | 360 | 2 |
| 17-registro-enfriamiento-descongelacion | 3 | 73 | 160 | 0 | 6 | 6 | 13 | 240 | 0 | 23 | 13 | 4 | 680 | 3 |
| 18-registro-congelacion-anisakis | 2 | 51 | 80 | 0 | 3 | 3 | 7 | 120 | 0 | 8 | 6 | 6 | 360 | 2 |
| 19-verificacion-termometros | 2 | 54 | 120 | 0 | 3 | 3 | 7 | 40 | 0 | 7 | 15 | 2 | 281 | 2 |
| BONUS-01-registro-formacion | 2 | 57 | 45 | 0 | 5 | 5 | 7 | 122 | 0 | 9 | 0 | 5 | 400 | 2 |
| BONUS-02-protocolo-alerta-alimentaria | 2 | 58 | 0 | 0 | 0 | 0 | 14 | 0 | 0 | 0 | 0 | 9 | 6 | 2 |
| **Total** | **48** | **2411** | **1141** | **40** | **57** | **195** | **294** | **722** | **62** | **209** | **114** | **123** | **10854** | **48** |

Columnas: «Fechas» = celdas con formato de fecha/hora; «Fechas texto» = fechas dd/mm/aaaa escritas como TEXTO;
«Nº ejemplo» = números escritos a mano fuera de Instrucciones (temperaturas, % polares, numeraciones); «Textos °C»
y «Norma ES» = celdas de texto que citan °C o normativa/autoridad española (`RX_NORMA` del extractor).

Transversal (los 21 libros):
- **Sin gráficos, sin imágenes, sin nombres definidos, sin hojas protegidas** (a diferencia del Kit de Inventario).
  Las 10.854 celdas verdes (`E8F5E9`) están todas desbloqueadas: convención «verde = lo que escribes tú».
- Cada libro = `Instrucciones` (sin paneles) + 1-2 hojas de trabajo. 48 áreas de impresión, 25 títulos de impresión,
  25 paneles; papel **A4 (`paperSize 9`) en las 48 hojas** (25 apaisadas, 23 verticales, todas con ajuste a página);
  pie `AI Chef Pro · aichef.pro · Página &P de &N` en las 48.
- 57 DV: 32 de lista (31 literales + 1 que cita hoja: 02 E5:E44 → `'Límites'!$A$5:$A$20`), 13 decimales (8 son
  temperaturas en °C, `cita_temp`), 10 de fecha, 2 de hora. 5.610 celdas con DV.
- 195 CF, **todas de expresión con igualdad exacta** (`OR(C7="ALERTA",…)`), sin `containsText` ni comodines: no hay
  colisiones por subcadena. Cada rango lleva el **semáforo universal** del pack (rojo 7 tokens · ámbar 7 · verde 6:
  ALERTA, RECHAZAR, CAMBIAR, REVISAR, ✗, CADUCADO, EXCESO / VIGILAR, ⚠, INCOMPLETO, CADUCA PRONTO, RENOVAR, FALTA
  CLORO, FALTA TEST / OK, ✓, Cumple, VIGENTE, Completo, APTO) más los tokens propios del rango.
- 1.141 fórmulas en **61 patrones** (filas normalizadas, `mapas.patron`). 18 comparan con números: 16 llevan cifras
  de mercado (límites en °C, cloro, fritura, horas de anisakis, tolerancia del termómetro) y 2 no cambian (riesgo
  1-9 del 12, aviso de 60 días del BONUS-01). Con las referencias del termómetro (19 D, sin comparación) son los
  **17 patrones** de `mapas.FORMULAS_EN`.
- Fechas: 442 `DD/MM/YYYY` (numFmt 164), 120 `HH:MM` (165), 160 `DD/MM/YYYY HH:MM` (165/167). Ninguna con
  `numFmtId 14`. Además, **62 fechas de ejemplo escritas como texto** (defecto I1).
- docProps iguales en los 21 salvo el título: `title` «<título> · Pack de Plantillas APPCC», `subject` «Pack de
  Plantillas APPCC · v2.0», `keywords` «pack appcc, AI Chef Pro», `description` «aichef.pro/pack-appcc»,
  `category` «AI Chef Pro · Productos digitales», `creator` «AI Chef Pro».
- Línea de versión en las 21 Instrucciones: «Versión 2.0 · agosto 2026 · aichef.pro/pack-appcc · info@aichef.pro»;
  firma «— Pack de Plantillas APPCC · AI Chef Pro · aichef.pro» al pie de las 48 hojas.
- **Línea de conservación idéntica en los 21 libros** (45 apariciones + 2 variantes con prefijo): «Conservar al menos
  2 años (trazabilidad y proveedores: 5); el Reg. (CE) 178/2002 exige trazabilidad pero no fija plazo — consulta la
  guía de prácticas correctas de higiene de tu comunidad autónoma.»
- **Circuito de incidencias**: los ejemplos de 01, 02, 07, 10, 16, 17 y 19 abren INC-001…INC-007, que viven en
  `11:Acciones Correctivas!A5:M11`. La historia (cifra → veredicto → incidencia) tiene que sobrevivir a la conversión.

## 1. Contenido específico de España, por libro

| Libro | Lo que es mercado español (y lo que la EN tiene que decidir) |
|---|---|
| 01 | Límites en fórmula: cámaras 0-4 °C, congeladores ≤ −18 °C, vitrina fría 0-8 °C, baño maría ≥ 65 °C (8 patrones, 84 fórmulas); DV −40…130 °C; lecturas de ejemplo 3,2…6,5 °C (INC-001 a 6,5 °C); horas «08:15» de 24 h; columnas M/T (mañana/tarde) |
| 02 | Hoja `Límites` con 10 familias UE y su base legal (Reg. (CE) 853/2004 Anexo III, RD 1021/2022, RD 1109/1991), máx. en °C; la misma lista en `Instrucciones!B13:B22`; DV −40…60 °C; proveedores «Pescados de la Ría S.L.», «Cárnicas del Norte»; lote + caducidad «07-09-26» |
| 03 | 32 elementos en 6 zonas; «Registro HA», «Registro sanitario», FDS, lejía/hipoclorito 1:50, lavavajillas 60/82 °C, paños a 60 °C, campana y conducto «por empresa autorizada» |
| 04 | Turnos M/T por día (Lun…Dom, 14 casillas), bloque semanal enlazado con el 03 |
| 05 | «SÍ/NO»; criterio «2/3 de vida útil»; Nº albarán; temperaturas de ejemplo en °C (mismas entregas que el 02) |
| 06 | Reg. (CE) 178/2002 arts. 18-19 y el mito de las «4 horas»; autoridad de la comunidad autónoma; «8,4 kg», «6 L»; platos «Merluza a la bilbaína», «Estofado de ternera» |
| 07 | **Nº ROESB**, nº de biocida «ES/BIO-…», bromadiolona/cipermetrina, plazo de seguridad en horas (DV 0-168), empresa DDD |
| 08 | 14 alérgenos del Reg. (UE) 1169/2011 Anexo II + RD 126/2015; S/T/N; especie obligatoria para cereal y fruto de cáscara (fórmula S6:S205); categorías de carta ES (Primeros/Segundos…); 8 platos de ejemplo españoles |
| 09 | **Orden de 26 de enero de 1989**: 25 % de compuestos polares; 180 °C máx.; aceite usado LER 20 01 25 y «gestor autorizado» |
| 10 | **RD 3/2023**: cloro libre 0,2-1,0 mg/L; red municipal / pozo / depósito |
| 11 | 7 incidencias de ejemplo con °C, «albarán», «empresa DDD», «olla de 20 L», «bandejas de menos de 5 cm» |
| 12 | 21 peligros en 7 fases con límites críticos en °C y norma ES (Reg. 852/2004, RD 1021/2022, RD 1420/2006, Reg. 853/2004, Reg. 2073/2005, Ley 17/2011); PCC/PPRo/NO; 3 recuentos H37:H39 |
| 13 | RD 109/2010 (no hay carné de manipulador), 48 h sin síntomas, Reg. 852/2004 Anexo II caps. VIII y XII; cartel imprimible sin celdas verdes |
| 14 | Cartel de los 14 alérgenos (descripción y dónde se encuentran) + protocolo ante reacción con el **112** |
| 15 | 25 puntos con gravedad **Ley 17/2011** (Leve/Grave/Muy grave: 6/16/3), autoevaluación con 7 recuentos, bloques «24 horas previas», «documentos» y «errores que más se sancionan»; firma del autor |
| 16 | 75 °C en el centro; regeneración en < 60 min (criterio del pack tras el RD 1021/2022) |
| 17 | Enfriamiento 60 → 10 °C en ≤ 2 h (1 tramo, columna I = «Destino»); descongelación en cámara ≤ 4 °C y uso ≤ 24 h |
| 18 | Anisakis: −20 °C 24 h o −35 °C 15 h (RD 1021/2022 art. 8, Reg. 853/2004); boquerones; aviso al consumidor art. 8.2 |
| 19 | Hielo 0 °C / ebullición 100 − altitud(m)/300; tolerancia ±1 °C; Madrid a 667 m; altitud en `B3` (verde) |
| B01 | RD 109/2010; 8 tipos de formación; «Válido hasta» con `TODAY()+900/+30/−60` (ejemplos vivos: VIGENTE/RENOVAR/CADUCADO) |
| B02 | Art. 19 del Reg. (CE) 178/2002; Salud Pública de la comunidad autónoma; 112; cartel de 7 pasos y tabla de contactos |

## 2. Lo que la EN hereda tal cual

- Toda la estructura (hojas, rangos, merges, áreas, títulos, paneles, anchos, colores, celdas verdes), el semáforo
  universal y el circuito de incidencias 01/02/07/10/16/17/19 → 11.
- Los recuentos de 03, 04, 07, 08, 11, 12, 15 y B01 (solo cambian sus literales).
- Las fórmulas de tiempo (17 `MOD(E−C,1)*24`, descongelación y anisakis `(E−D)*24`), la numeración del 08 y el
  resumen del 15.

## 3. Defectos heredados (no se tocan aquí; la EN nace corregida — SPEC D26)

- **I1 · Fechas de ejemplo como TEXTO** (62 celdas: 02, 04, 05, 06, 07, 09, 10, 11) en columnas cuyo formato o DV es de
  fecha (06 `Trazabilidad!A5:A44` lleva `DD/MM/YYYY` y sus ejemplos son texto). No ordenan, no filtran y en EE. UU.
  «05/09/2026» se lee 9 de mayo. EN: fechas reales con formato de sistema.
- I2 · Tokens duplicados dentro de una misma regla de CF (09 «FALTA TEST» ×2, 10 «FALTA CLORO» ×2) y tokens del
  semáforo universal que ningún libro produce (EXCESO, CADUCA PRONTO). Cosmético; la EN los conserva para no
  romper la paridad de CF.
