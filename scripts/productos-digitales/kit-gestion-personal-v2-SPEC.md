# Kit Gestión de Personal y Turnos — v2.0 (SPEC, 2026-08-23)

Origen: ronda 1 adversarial (`auditorias/kit-gestion-personal-R1.json`, 3 lentes opus — dominio laboral, técnica Excel,
coherencia comercial; **86 hallazgos**, 21 altas). Lo que sigue es lo que SE HACE; lo demás se descarta en §6 o se pregunta
en §7; la evidencia de cada hallazgo está en el R1, citada aquí por id y no repetida. Método y código de referencia:
`kit-escandallos-v2-SPEC.md` y `kit-inventario-v2-SPEC.md` (motor + grupos, `main.py --dry-run / --solo`, respaldo,
`inject_cache.py` al final, verificación `data_only`, idempotencia por reconstrucción). Paquete nuevo
`scripts/productos-digitales/kit-gestion-personal-v2_0/` (`motor.py`, `grupo_a.py`, `grupo_b.py`, `grupo_c.py`, `main.py`);
ejecución real solo con `KIT_GESTION_PERSONAL_APPLY=1`.

Ficheros: `astro-site/public/dl/kit-gestion-personal/` — **los mismos 9 xlsx con los mismos nombres**: las 9 claves de
descarga (`get-download-urls.ts:234-243`) viajan en emails ya enviados. Se añaden hojas, columnas y filas; no se quita ningún
entregable. Convenciones: editables **verdes `E8F5E9`** con `Protection(locked=False)`, calculadas sin relleno; parámetros en
celda, nunca literales dentro de la fórmula; `IFERROR` y guarda de rango vacío en toda división, media y resta; semáforo por
**formato condicional real** (verde `C6EFCE`, ámbar `FFEB9C`, rojo `FFC7CE`); DV con `showErrorMessage=True`; protección de
hoja **sin contraseña**.

**Medido con pycel el 2026-08-23** (este kit vive de horas y fechas): `MOD` **sí** evalúa con horas —`MOD(D5-C5,1)*24` con
23:00→07:00 da `7.999999999999998`—, así que **toda fórmula de horas va envuelta en `ROUND(...,2)`** o el `inject_cache` graba
ese ruido en el fichero que se descarga; alternativa documentada `IF(D5<C5,D5+1-C5,D5-C5)*24`, que da `8.0` exacto. Funcionan
`SUMIF`, `SUMIFS` (2 criterios), `COUNTIF` con criterio concatenado (`"<"&$B$3`) y comodín (`"🔴*"`, `"?*"`, `"<>"`), `INDEX`,
`MATCH`, `VLOOKUP`, `IFERROR`, `CEILING`, `ROUND`, `TEXT` (también con fechas), `SUMPRODUCT`, `TODAY`, `DATE`, `MONTH`,
`EOMONTH`. **NO**: `COUNTA` (→ `COUNTIF(rango,"<>")`), `MODE`, `DATEDIF` (→ resta de fechas), `WEEKDAY(fecha;tipo)` con
segundo argumento (→ el lunes de la semana 1 en verde y las 52 restantes `=celda_anterior+7`) y `TEXT(fecha,"mmm")`, que
devuelve el mes en inglés. Nada de builds locales ni Playwright; python en serie; `istats` entre barridos.

## 1. Motor común (`motor.py`) — los 9 ficheros

1.1 **Leyenda única** (DOM-27). Jornada (01): `M · T · N · P · D` (doble, nuevo) `· L · V · B`; ausencias (05):
`V · B · F · PE` — el permiso deja de ser `P`, que en el 01 es Partido. Va en la fila 3 de cada rejilla y en las dos
Instrucciones.
1.2 **Formato condicional real** (TEC-17/COM-10; hoy 0 reglas en 8 de las 9 hojas de datos): `semaforo(ws, rango,
vocabulario)` con `containsText` en `01!K:N`, `02!'Resumen Mensual'!F`, `03!'Ratio'!B9`, `05!'Calendario Anual'!B6:BB35` (V
azul `BBDEFB`, B rojo `FFC7CE`, F verde `C8E6C9`, PE naranja `FFE0B2`) y su fila 38, `06!C23` y `07!'Vencimientos'!C/E/G/I`;
banda gris alterna por mes en el 05 con `expression` `=ISODD(MONTH(B$5))` (la evalúa Excel, no pycel). En el 04, las 5
cabeceras de sección se pintan con los colores que sus propias Instrucciones anuncian.
1.3 **Capacidad homogénea: 30 empleados** (DOM-32; hoy 30/20/15/15) en toda hoja indexada por empleado, con fórmula, DV y
verde replicados y el TOTAL desplazado. `02!'Registro Horas'` pasa a **300 filas** (5-304) y sus Instrucciones avisan de que
30 personas generan ~780 registros al mes: hoja por quincena o arrastrar las fórmulas (COM-18).
1.4 **Parámetros en celda verde**, cada uno con su nota de «esto lo fija tu convenio / tu CNAE, edítalo»: tipo de SS, recargo
de hora extra, tarifa hora, límite anual de horas extra, días de convenio, umbrales del semáforo, ratios de cubiertos,
jornada semanal, factor de cobertura, horas por servicio, descanso mínimo entre jornadas y máximo de jornada diaria.
1.5 **Guardas**: ninguna hoja recién descargada puede enseñar un `#¡DIV/0!`, un veredicto, un porcentaje ni un contador
distinto de cero. `=IF(COUNT(rango)=0,"",…)` en medias, `=IF(OR($X="",$Y=""),"",…)` en restas y productos, `IFERROR` en todo
`VLOOKUP`. Gate en `main.py`: tras `inject_cache`, **ningún valor cacheado empieza por `#`**.
1.6 **Formatos y presentación** (TEC-22/TEC-23/TEC-25): `hh:mm` en `02!C:D` (hoy `General`: teclear «9» da 192 h sin aviso),
`dd/mm/yyyy` en toda fecha, `#,##0.00 €` en todo dinero **también de entrada** (`02!B3`, `03!'Ratio'!B4:B5`,
`03!'Previsión'!B22`, `BONUS-02!B9`), `0,0 %` y `0,00`; `freeze_panes` en las 5 hojas que no lo tienen
(`07!'Plantilla'`→`B5`, `01!'Cuadrante Mensual'`→`A5`, `03!'Ratio'`, `03!'Previsión'`, `BONUS-02!'Calculadora'`),
`print_title_rows` y `print_title_cols='$A:$A'` en las rejillas anchas, `fitToWidth=2` en `07!'Plantilla'`; protección de las
22 hojas sin contraseña, con la línea «Revisar → Desproteger hoja (no tiene contraseña)».
1.7 **Instrucciones, bio y versión** reescritas para describir lo que hay. **Bio anclada — hoy no la lleva ninguno de los
9**: «Diseñado por John Guerrero — chef y consultor gastronómico desde 2010, en cocina desde los 17 años ·
johnguerrero.es»; «Versión 2.0 · agosto 2026 · aichef.pro/kit-gestion-personal · info@aichef.pro»; metadata `subject` →
`… · v2.0` (resto según `postprocess-transversal.py`).

## 2. Grupo A — tiempo de trabajo (01, 02, BONUS-01) — `grupo_a.py`

- **01, hoja nueva `Turnos`** (DOM-05/TEC-05, altas): los horarios salen de la fórmula monstruo de `I6`. Tabla verde `A5:E12`
  (Código · Descripción · Hora inicio · Hora fin · Horas): M 7→15 (8) · T 15→23 (8) · N 23→7 (8) · P 10→23 con pausa (9) ·
  **D doble 7→23 (16)** · L/V/B 0→0 (0). Verdes `B2` «Máx. horas de jornada ordinaria diaria» = 9 y `B3` «Descanso mínimo
  entre jornadas (h)» = **12** (art. 34.3 ET; las 11 h que hoy imprime `Instrucciones!B12` son de la Directiva 2003/88/CE).
- **01, las 4 alertas EXISTEN** (DOM-05/DOM-25/TEC-05/COM-01): bloque auxiliar **oculto** `P:AP` — horas de cada día
  `=IFERROR(VLOOKUP($B6,Turnos!$A$5:$E$12,5,FALSE),0)` (P:V), hora de inicio (W:AC, col. 3), hora de fin (AD:AJ, col. 4) y las
  6 transiciones `AK6='=IF(OR($P6=0,$Q6=0),"",IF($AD6<=$W6,$X6-$AD6,24-$AD6+$X6))'`, que contempla el turno que cruza
  medianoche (N seguido de T da 8 h; N seguido de M, 0). Con eso `I6='=SUM($P6:$V6)'` y cinco columnas visibles: `J` **H.
  contratadas/semana** (verde, 40 — hoy el 40 va dentro de la fórmula e ignora a los parciales); `K`
  `=IF($A6="","",IF(COUNTIF($AK6:$AP6,"<"&Turnos!$B$3)>0,"⛔ <"&Turnos!$B$3&" h",""))`; `L`
  `=IF(…,IF(7-COUNTIF($P6:$V6,">0")=0,"⛔ 0 días",IF(…=1,"⚠ 1 día (el ET pide 1,5, acumulable en 14 días — art. 37.1)","")))`;
  `M` `=IF(…,IF($I6>$J6,"⛔ +"&TEXT($I6-$J6,"0")&" h",""))`; `N` jornada diaria / **doble turno**
  `=IF(…,IF(COUNTIF($P6:$V6,">"&Turnos!$B$2)>0,"⛔ jornada > "&Turnos!$B$2&" h",""))`, que es lo que caza el código `D`.
- **01, `Cuadrante Mensual`** (DOM-17/TEC-23/COM-12): deja de ser una rejilla muerta — **5 bloques** de semana (hoy 4 = 28
  días) con la DV `M,T,N,P,D,L,V,B`, la fórmula de horas y la alerta del semanal, `freeze_panes`, `print_title_rows`, total
  mensual por empleado, fila de promedio, **nombres enlazados** (`=IF('Cuadrante Semanal'!$A6="","",'Cuadrante Semanal'!$A6)`)
  e Instrucciones que expliquen para qué sirve la hoja, hoy no mencionada ni una vez.
- **02, cruce de medianoche y turno partido** (DOM-03/DOM-21/TEC-01/COM-07, altas): cabecera `A4:I4` = Empleado · Fecha ·
  Entrada · Salida · **Pausa (h)** · Horas trabajadas · H. contratadas · Horas extra · Tipo, con
  `F5='=IF(OR($C5="",$D5=""),"",ROUND(MOD($D5-$C5,1)*24-IF($E5="",0,$E5),2))'`. La Pausa es lo que hace registrable el
  partido (10:00→23:00 menos 4 h = 9 h), que hoy no cabe en un solo par entrada/salida.
- **02, guarda de «H. Contratadas»** (DOM-11/TEC-09, alta): `H5='=IF(OR($F5="",$G5=""),"",MAX(0,$F5-$G5))'` y `G5:G304`
  precargada a **8** con DV decimal 1-12 — hoy una fila a medias declara extra la jornada entera (168 €/día y empleado).
- **02, `Resumen Mensual` agrega y el recargo es parámetro** (DOM-07/TEC-06/TEC-08/COM-02/COM-14, altas): verdes `B3` tarifa
  hora ordinaria 12,00 € · `D3` **«Recargo de la hora extra (× la ordinaria) — según tu convenio»** = **1,25** · `F3` límite
  anual 80. `B` `=IF($A6="","",ROUND(SUMIF('Registro Horas'!$A$5:$A$304,$A6,'Registro Horas'!$H$5:$H$304),2))` (hoy
  transcripción manual); `C` fuerza mayor o compensadas (dos `SUMIFS` sobre Tipo); `D` computables `=$B6-$C6`; `E` acumuladas
  del año (verde, documentada); `F`
  `=IF(…,IF($E6>$F$3,"⛔ EXCEDE ("&TEXT($E6-$F$3,"0")&" h)",IF($E6>$F$3*0.8,"⚠ cerca del límite","✓ dentro")))` con CF; `G`
  `=IF($B6="","",ROUND($B6*$B$3*$D$3,2))`. Desaparecen las cabeceras «Coste ×1.75» y «Coste ×2.0».
- **02, la cita legal** (DOM-12/COM-19, alta): `Instrucciones!B11-B12` dejan de presentar ×1,75 y ×2,0 como «Legislación
  española» — el **art. 35.1 ET** solo exige que la hora extra no valga menos que la ordinaria, la cuantía la fija el convenio
  o el contrato y puede compensarse con descanso. `B10` gana las excepciones del **art. 35.2** (no computan en el tope de 80 h
  las compensadas con descanso en 4 meses ni las de fuerza mayor), que es lo que descuenta la columna C con la DV ampliada a
  `Voluntaria, Obligatoria, Fuerza mayor, Compensada con descanso`.
- **BONUS-01** (DOM-29/TEC-28): DV `Alta,Media,Baja` en Gravedad (`C17:C22`) y `Urgente,Alta,Normal` en Prioridad
  (`A25:A30`). Bloques nuevos **CAJA** (fondo · recaudación · diferencia `=IF(OR($B_="",$C_=""),"",$C_-$B_)` · firma) y
  **TEMPERATURAS AL CAMBIO DE TURNO** (cámara ≤ 4 °C · congelador ≤ −18 °C · expositor ≤ 4 °C, límite precargado, Conforme
  `=IF(…,IF($B_<=$C_,"✓ CONFORME","⛔ FUERA DE RANGO"))`): es el punto donde el APPCC cambia de responsable. `wrap_text` y
  alto de fila en `A46:D49` (TEC-24).

## 3. Grupo B — coste laboral y dimensionamiento (03, BONUS-02) — `grupo_b.py`

- **03 `Nóminas`** (DOM-08/DOM-31/TEC-14/TEC-26, alta): verde `C2` **«Tipo de SS a cargo de la empresa (%)» = 33 %** con nota
  «ajústalo a tu CNAE, contrato y convenio: un indefinido general ronda el 33-34 % sumando contingencias comunes, desempleo,
  AT/EP, FOGASA, FP y MEI». Columnas: `C` bruto/mes · `D` **Nº de pagas/año** (verde, DV 12/14/15, por defecto 14) · `E`
  prorrateado `=IF(OR($C5="",$D5=""),"",ROUND($C5*$D5/12,2))` · `F` `=IF($E5="","",ROUND($E5*$C$2,2))` · `G` coste total/mes ·
  `H` horas contratadas/semana · `I` **coste/hora** `=IF(OR($G5="",$H5="",$H5=0),"",ROUND($G5/($H5*4.33),2))`, que da uso a la
  columna muerta de hoy y es el número que hay que llevar a `02!B3`. El `0.30` sale de las 21 fórmulas y de `D4`, ahora
  `="SS empresa ("&TEXT($C$2,"0%")&")"`.
- **03, el semáforo** (DOM-16/TEC-10/TEC-11/COM-11/COM-17): deja de felicitar al que no ha medido y de suspender a la alta
  cocina. `B3` tipo de negocio (DV con los 6 de la tabla); `B7='=IF(OR($B$4="",$B$4<=0),"",ROUND($B$5/$B$4,4))'` en `0,0 %`;
  umbrales por `VLOOKUP` sobre dos columnas **numéricas nuevas** de `A13:E19` (objetivo/aceptable: fast casual 0,28/0,30 ·
  casual 0,33/0,35 · fine dining 0,40/0,42 · catering 0,35/0,38 · cafetería 0,32/0,35 · bar 0,30/0,33);
  `B9='=IF($B$7="","— introduce las ventas del mes y las nóminas",IF($B$7<$D$7,"🟢 EXCELENTE (por debajo de tu objetivo)",IF($B$7<=$D$8,"🟡 VIGILAR (en el límite)","🔴 ACCIÓN CORRECTIVA")))'`.
  Sin tipo elegido cae a 30/35 %, el comportamiento de hoy.
- **03 `Previsión por Servicio`: cubiertos por SERVICIO** (DOM-09/TEC-15/TEC-20/COM-09, alta): cadena idéntica a la del
  BONUS-02 — cubiertos/día (80) → servicios/día (DV 1/2/3, = 2) → **cubiertos por servicio** `=ROUND($B$4/$B$5,0)` = 40 →
  personal por servicio con ratios verdes 25/22/80 → presencias/día = 10 → horas semanales = presencias × horas efectivas por
  servicio (verde, 4) × días de apertura (verde, 6) = 240 → **FTE** `=CEILING(240/jornada*cobertura,1)` = **7**. Coste
  `=ROUND(FTE*salario*pagas/12*(1+SS),2)`, rótulo corregido a «Coste laboral estimado del equipo (€/mes)» y remisión al bonus.
- **BONUS-02, resultado por defecto creíble** (DOM-10, alta): hoy da 19 empleados y 622.440 €/año para un casual de 80
  cubiertos — un ratio del 99,7 % frente al 28-33 % de su propia hoja de referencia. Entradas verdes: 80 cubiertos/día · 6
  días/semana · 2 servicios/día · tipo (DV) · **salario medio 1.500 €/mes** (hoy 1.800) · 14 pagas · SS 33 % · **horas
  efectivas por servicio 4** · jornada 40 h · **factor de cobertura 1,15** · ticket medio sin IVA 25 € · **día PICO 120**.
  Resultado: 40/servicio → 2 cocineros + 2 camareros + 1 barra = 5 por servicio → 10 presencias/día → 240 h/semana → **7
  FTE** · 16.292,50 €/mes · 195.510 €/año · ventas 52.000 €/mes · **ratio 31,3 %**, dentro del objetivo casual. El 03
  devuelve los mismos 7: es un caso del gate.
- **BONUS-02, lo demás** (DOM-18/DOM-23/TEC-16/TEC-21/COM-13): `Días de apertura/semana` **entra en la fórmula** (hoy no la
  lee ninguna de las 16) vía las horas semanales; el **día pico** produce el refuerzo por servicio (personal pico − normal),
  que es lo que la landing vende como «picos de demanda»; el tipo de negocio pasa de tres `IF` anidados con cajón de sastre a
  **DV de lista con los 10 nombres** y `VLOOKUP` sobre tres columnas numéricas nuevas de `Ratios por Tipo` (cubiertos por
  empleado y **servicio**: casual 25/22/80 · fine dining 12/10/40 · fast casual 45/40/100 · cafetería 35/30/60 · bar 0/30/35 ·
  pizzería 30/25/90 · dark kitchen 40/0/0 · hotel 20/15/50 · catering 22/15/60 · heladería 40/30/0), con
  `=IF(ratio=0,0,CEILING(…))` para que una dark kitchen no exija camareros. El coste anual deja de multiplicar por 14 a
  escondidas: usa la celda de pagas y la etiqueta dice «bruto mensual en N pagas». Se corrige la nota `A20`.

## 4. Grupo C — ciclo de vida del empleado (04, 05, 06, 07) — `grupo_c.py`

- **04, el contador que cuenta cabeceras** (DOM-01/TEC-02/TEC-13/COM-03, altas — y es la mejora estrella del changelog v1.1,
  que hoy abre en «4 de 51 completadas» y «8,51 %» con el checklist en blanco). Se hacen las dos cosas: las cinco cabeceras de
  la columna F pasan de `✓` a **`Hecho`** y los contadores se acotan por tramo — completadas
  `=COUNTIF($F$7:$F$19,"✓")+COUNTIF($F$23:$F$30,"✓")+COUNTIF($F$34:$F$42,"✓")+COUNTIF($F$46:$F$57,"✓")+COUNTIF($F$61:$F$68,"✓")`,
  total `=COUNTIF($B$7:$B$19,"?*")+…` (sustituye a la constante 47), **aplicables** = total − las marcadas `—` (DOM-28: hoy un
  onboarding bien terminado se queda en el 89 %) y progreso `=IF($C$72>0,$C$71/$C$72,0)` en `0,0 %` → **0 % recién descargado**.
- **04, contenido** (DOM-15/DOM-22/TEC-12): «Categoría» deja de estar cortada a 14 caracteres exactos («FORMACIÓN OBLI»,
  «PERIODO DE PRU» — un `slice[:14]` del generador, revisar el resto de la familia), con la columna a 22. La tarea 4 pasa a
  «Alta en Seguridad Social (TA.2/S) — **OBLIGATORIO ANTES** del inicio de la jornada (art. 32.3 RD 84/1996)» y entran las
  tres que faltaban y tienen plazo: **Contrat@ al SEPE (10 días hábiles)**, **copia básica a la RLT (10 días)** y **modelo
  145 de IRPF** → 50 tareas. «Fecha Límite», hoy vacía en las 47 filas, se precarga: Día −1 / Día 1 / Día 7 / Día 30.
- **05, el calendario cuenta DÍAS** (DOM-04/TEC-04/COM-06, altas): hoy hay **una celda por MES** y quien disfruta agosto
  entero figura con 1 día usado y 29 restantes. Geometría: **una fila por empleado × 53 semanas** (`B:BB`, ancho 2,4),
  elegida frente a la rejilla de 366 días y a las cuatro hojas trimestrales porque (a) **cabe en A4 apaisado** —22 + 53×2,4 ≈
  149 unidades, ~100 % de escala, frente a las ~210 de un trimestre de 93 columnas, que obligan a un 55 % ilegible—, (b) no
  multiplica el mantenimiento en cuatro hojas con los nombres repetidos y (c) **elimina la doble fuente de verdad**, causa
  real del hallazgo: el cómputo no sale de las celdas pintadas sino de las **fechas de las solicitudes aprobadas**. Verdes
  `B2` «Lunes de la semana 1» y `B3` «Días de vacaciones por convenio (naturales)» = 30 (art. 38 ET, con la alternativa de 22
  laborables explicada); fila 4 nº de semana, fila 5 fecha del lunes `=$B5+7` en `dd/mm`; DV `V,B,F,PE,` y color de §1.2.
- **05, hoja nueva `Saldo Vacaciones`** (DOM-19/TEC-18/COM-24): 30 filas con el nombre enlazado al calendario y columnas
  **Fecha de alta** (verde, para el **prorrateo** de quien entra a mitad de año: `=ROUND(derecho*($E$2-$B5+1)/365,1)`), **Días
  por convenio** (verde; vacío = usa el global, hoy el 30 está escrito en 30 fórmulas), **Disfrutados**
  `=SUMIFS(Solicitudes!$D$5:$D$34,Solicitudes!$A$5:$A$34,$A5,Solicitudes!$G$5:$G$34,"Aprobado")`, **Pendientes**, **Restantes**
  = derecho − disfrutados − pendientes (sí descuenta la solicitud en curso) y alerta de saldo negativo.
- **05, `Solicitudes` y `Cobertura`** (DOM-20/COM-20): «Días solicitados» avisa de fechas invertidas
  (`=IF($C5<$B5,"⚠ fechas invertidas",$C5-$B5+1)`), el saldo se lee por `INDEX/MATCH` y una columna verifica que el nombre
  existe en el calendario (`COUNTIF`=0 → aviso; no se usa DV entre hojas por compatibilidad con Google Sheets). **`Cobertura`
  deja de ser una tabla vacía**: fila verde 36 del calendario «Temporada alta (S/N)» precargada en las semanas 27-35 y 51-52,
  fila 37 `=COUNTIF(B$6:B$35,"V")+COUNTIF(B$6:B$35,"B")` y fila 38
  `=IF(B$37=0,"",IF(AND(B$36="S",B$37>0),"⛔ TEMP. ALTA",IF(B$37>Cobertura!$B$10,"⚠ EXCESO","")))`; en `Cobertura`, personal
  mínimo por turno y **máximo de ausencias simultáneas** (verdes), plantilla total `=COUNTIF(…,"?*")`, pico `=MAX(…B$37…)`,
  semanas por encima del máximo, semanas de temporada alta con ausencias y la tabla de sustituciones con DV. Con eso
  «cobertura mínima» y «periodos de máxima demanda» pasan a ser ciertos.
- **06** (DOM-02/DOM-30/TEC-03/TEC-24/COM-04/COM-21, altas): ningún `#¡DIV/0!` en un documento que se firma —
  `C22='=IF(COUNT($C$12:$C$21)=0,"",ROUND(AVERAGE($C$12:$C$21),2))'`, `C23='=IF($C22="","",IF($C22>=4.5,…))'` y una fila
  «Competencias valoradas» `=COUNT($C$12:$C$21)&" de 10"`. La DV pasa de decimal 1-5 a **lista `1,2,3,4,5,N/A`**, para no
  puntuar «Atención al cliente» a un cocinero de partida y que la media salga solo de lo valorado. Las nueve celdas combinadas
  de texto libre reciben `wrap_text` y alto de fila, y entra el bloque **PLAN DE DESARROLLO** (acción formativa · responsable ·
  fecha objetivo · indicador), que la landing promete y no existía.
- **06 `Histórico`** (TEC-27/COM-26): la tendencia compara **los dos últimos trimestres informados** —hoy solo Q4 contra Q3,
  en blanco nueve meses al año—:
  `=IF(COUNT($B5:$E5)<2,"",IF(INDEX($B5:$E5,COUNT($B5:$E5))>INDEX($B5:$E5,COUNT($B5:$E5)-1),"↑ Mejora",IF(<,"↓ Baja","→ Estable")))`
  (medido en pycel; no hace falta `LOOKUP(9^9;…)`). 30 filas, e Instrucciones explican cómo duplicar la ficha y volcar la
  media al histórico, que hoy no se dice en ninguna parte.
- **07, «Alérgenos Propios» SE ELIMINA** (DOM-13/COM-25, alta): dato de salud, categoría especial del **art. 9 RGPD**, que el
  fichero pedía al mismo nivel que la talla de camiseta. No se sustituye por nada. La sección de protección de datos se
  reescribe: **base jurídica** (art. 6.1.b y 6.1.c), **minimización**, **plazos** (registro de jornada 4 años, art. 34.9 ET;
  documentación de cotización 4 años, art. 21 LISOS), **contacto de emergencia** = dato de un tercero al que hay que informar,
  **derechos** de los arts. 15-22 y el **cómo** cifrar el libro («Archivo → Información → Proteger libro → Cifrar»).
- **07, columnas y vencimientos** (DOM-14/DOM-24/TEC-07/TEC-19/COM-16, altas): `Plantilla` pasa a **21 columnas** `A4:U4` con
  **NAF / Nº Seguridad Social**, **Fecha de nacimiento**, **Convenio aplicable**, **Grupo profesional**, **Fin del periodo de
  prueba**, **Caducidad del carnet de manipulador** y **Caducidad de PRL** (convenio y carnets los enumera la landing y no
  existían), más una columna calculada «Aviso»
  `=IF($C5="","",IF(TODAY()-$C5<6570,"⚠ MENOR DE EDAD: sin nocturnidad ni horas extra (art. 6 ET)",""))`. `Vencimientos` deja
  de mirar solo a los **15 primeros de 30** y pasa a **30 filas × 4 vencimientos** (contrato, periodo de prueba, manipulador,
  PRL) con alerta por pares
  `=IF($C7="","",IF($C7-$B$3<0,"❌ VENCIDO hace "&TEXT($B$3-$C7,"0")&" d",IF($C7-$B$3<=30,"🔴 "&TEXT($C7-$B$3,"0")&" d",IF($C7-$B$3<=$B$4,"🟡 …","🟢 OK"))))`,
  antelación de aviso en verde `B4` (60 días) y contador de alertas rojas en cabecera (`COUNTIF` con comodín).

## 5. Integración — landing, dashboard, changelog, catálogo, gates (`integracion`, sonnet)

- **La fuente que sirve producción es `astro-site/src/data/productos/kits/kit-gestion-personal.ts`**; sus gemelos de la SPA
  (`src/pages/KitGestionPersonal.tsx`, `src/components/kit-gestion-personal/*`) son el original del copy VERBATIM y se tocan
  en el mismo commit, o vuelven a divergir.
- **Legal del hero y de la FAQ** (DOM-06/COM-05, altas): `hero.badge:105`, `why.reasons[2]:156`, `faqs[0].a:217` y
  `schema.faqs[0].a:70` dicen que el control horario «es obligatorio desde 2026», que hace falta «software homologado» y que
  hay «multas hasta 10.000 EUR/empleado». El registro de jornada es obligatorio **desde el 12-05-2019 (RD-ley 8/2019, art.
  34.9 ET)**, no existe homologación oficial de sistemas de fichaje y el incumplimiento es **infracción grave (art. 7.5
  LISOS) sancionada por centro de trabajo**, no por trabajador. Badge nuevo: «Registro de jornada obligatorio en España desde
  2019 — planifica turnos, descansos y coste laboral sin errores». La FAQ mantiene el «No» (el kit no sustituye al fichaje)
  sin «homologado» ni año, y cita el rango LISOS con su artículo (§7.2).
- **Promesas que la v2.0 vuelve ciertas y hay que reformular igualmente**: `grid.templates[0]:135` y `ContentGrid.tsx:8`
  («descanso mínimo **11h**») → **12 h, art. 34.3 ET**, ya con las cuatro alertas reales (COM-01); `[1]:136` describe el
  recargo como **parámetro editable** (COM-02); `[4]:139` cobertura y temporada alta (COM-20); `[5]:140` plan de desarrollo
  (COM-21); `[6]:141` convenio y carnets (COM-16); `[8]:143` días de apertura y picos de demanda (COM-13);
  `KitGestionPersonalDashboard.tsx:15-23`, los mismos cambios.
- **Cifras y catálogo**: `why.reasons[3].title:157` («40 EUR/mes») se unifica con `faqs[3].a:229` y `schema.faqs[2].a:78` en
  **30-60 EUR/mes** (COM-23); `products-catalog.ts:56` cambia «Cuadrantes, control de horas, **ratios de productividad**»
  —que no existen— por «Cuadrantes de turnos, horas extra, coste laboral, onboarding, vacaciones y evaluación de equipo», y su
  `description.en` en paralelo (COM-22); `faqs[2].a:225` ya es cierta al resolverse el tipo de negocio por `VLOOKUP` (DOM-23).
- **Tildes y eñes** (DOM-26): toda la copia visible está sin acentos («gestion», «formulas», «Espana», «Desempeno») mientras
  los propios xlsx acentúan bien. Se reescriben `seo`, `schema`, `hero`, `grid`, `why`, `bonus`, `faqs`, `cta` y
  `testimonials` del `.ts` y los mismos ficheros de la SPA. Defecto ya censado en `feedback_acentos_tildes.md`.
- Changelog `productos-changelog.ts:247-264` → **2.0** (2026-08-23), entrada nueva en lenguaje de cliente (turnos de noche
  que ya no dan horas negativas, las cuatro alertas legales, el calendario por semanas con saldo real, el progreso del
  onboarding que arranca en 0 %, la ficha sin errores, el directorio con 30 empleados y sin datos de salud);
  `kit-gestion-personal.ts:295` `updateNote` → «Producto actualizado · Versión 2.0 · agosto 2026». **Emails y claves: no se
  tocan** — `get-download-urls.ts:234-243` intacto y los textos de `verify-purchase.ts` y `resend-access.ts` («9 plantillas»)
  siguen siendo ciertos.
- Gates: `censo-entregables.py --only kit-gestion-personal --fail --quiet` (0 defectos), `gate-flujo-postpago.py --offline
  --only kit-gestion-personal` (9/9), `inject_cache.py` **al final**, verificación `data_only` (ningún cacheado empieza por
  `#`; progreso 0 %; semáforo y nivel en blanco), idempotencia (segunda pasada = 0 cambios), barrido de caracteres no latinos
  y **batería pycel**: 23:00→07:00 = 8,00 h · 19:00→01:30 = 6,50 h · «H. contratadas» vacía → extra en blanco · ficha vacía →
  media en blanco · 03 y BONUS-02 devuelven **7 FTE** con los datos por defecto · T seguido de M dispara la alerta de descanso
  y M seguido de M no.

## 6. Descartado con motivo

- **COM-08** (`aggregateRating` 4,9 con 8 reseñas sin sistema de recogida, `schema.reviews`, los 8 testimonios): **aparcado
  por John** (2026-08-22). La v2.0 vuelve ciertos por sí sola dos de los cuatro testimonios señalados y deja los otros dos
  como duda §7.1.
- **COM-15** (`priceOld: '49 EUR'`, `discountBadge: '-71%'`, «Sube pronto», badge «Nuevo» del hub, `bonus.subtitle`
  «valorados en 18 EUR»): toca el **ancla de precio**, aparcada por John dentro de «extender honestidad a 43 landings». No se
  resuelve aquí de forma distinta al resto del catálogo.
- **Enlaces entre libros**: no. Son 9 ficheros que el cliente descarga a carpetas distintas y una referencia externa acaba en
  `#REF!`; los parámetros compartidos se repiten en verde en cada libro y se documenta de dónde copiarlos. **Rejilla de 366
  días y hojas trimestrales** en el 05: descartadas en §4. **`ListObject`**: no; rangos ampliados con fórmula, DV y verde.

## 7. Dudas para el orquestador

7.1 **Los 4 testimonios con funciones inexistentes (COM-08).** Con la v2.0, Lucía Navarro («me avisa cuando está cerca del
límite legal») y Alberto Méndez («cobertura mínima por puesto») pasan a ser **ciertos**; siguen sin serlo Francisco Torres
(«coste laboral **en tiempo real**»: el 03 es una hoja mensual manual) y Enrique Vidal («2 personas más el viernes y el
sábado»: la calculadora no tiene día de la semana). *Recomiendo* reescribir **solo esos dos**, sin tocar `aggregateRating`.
7.2 **Rango de sanción en la FAQ.** ¿«Infracción grave, art. 7.5 LISOS: de **751 a 7.500 €**, por centro de trabajo» o FAQ sin
importe? *Recomiendo* citarlo con el artículo y verificar el tramo vigente en el BOE dentro del paso de integración.
7.3 **04: de 47 a 50 tareas** (Contrat@, copia básica a la RLT, modelo 145). *Recomiendo sí*: «40+ tareas» sigue siendo cierta.
7.4 **BONUS-02: salario medio por defecto de 1.800 → 1.500 €/mes en 14 pagas.** Es lo que hace que el resultado por defecto
caiga en un ratio del 31,3 % en vez de rondar el 40 %. *Recomiendo sí*, con la nota de que es bruto de convenio, no coste.
7.5 **06: ¿una ficha o varias?** *Recomiendo* una ficha en blanco + una hoja «Ficha (ejemplo relleno)» y la instrucción de
duplicar, antes que 4 fichas vacías que engordan el libro sin resolver nada.
7.6 **07: la hoja pasa a imprimirse en dos páginas A4** (21 columnas, `fitToWidth=2`, nombre repetido con
`print_title_cols`); la alternativa es partirla en dos bloques verticales. *Recomiendo* las dos páginas.

## 7-bis. Decisiones ya fijadas por el orquestador (2026-08-23, antes de construir)

1. **Mismos 9 ficheros, mismos nombres**; se añaden hojas, columnas y filas, no se retira ningún entregable.
2. **Cruce de medianoche** con `MOD` (verificado en pycel) envuelto en `ROUND(...,2)`; alternativa documentada
   `IF(salida<entrada, salida+1-entrada, salida-entrada)*24`.
3. **Recargo de hora extra en celda verde, 1,25 por defecto**, con la nota correcta del art. 35.1 ET: nada de presentar
   ×1,75 / ×2,0 como legislación española. **Guarda de «H. Contratadas» vacía** y **límite de 80 h/año con contador y CF**.
4. **Las 4 alertas del cuadrante se construyen** (no se recorta la promesa) y la cita pasa a **12 h, art. 34.3 ET**.
5. **Cotización empresarial en celda, 33 % por defecto**, con nota de CNAE/convenio, y pagas extra prorrateadas.
6. **«Previsión por Servicio» a cubiertos/SERVICIO**, coherente con el BONUS-02, que debe dar 6-9 FTE para 80 cubiertos/día.
7. **«Alérgenos Propios» se elimina** (art. 9 RGPD) y la sección de protección de datos se reescribe.
8. **`aggregateRating`, reviews, testimonios y ancla de precio NO se tocan** (aparcado por John).
9. **Convenciones de familia**: verdes `E8F5E9`, `IFERROR`, parámetros en celda, protección sin contraseña, bio anclada
   (**inserción**: no la lleva ninguno de los 9), «Versión 2.0 · agosto 2026», metadata, changelog 2.0, `updateNote`,
   `inject_cache` al final, idempotencia, `--dry-run` y `KIT_GESTION_PERSONAL_APPLY=1`.

## 8. Mapa id → sección (86/86)

| id | dónde | qué |
|---|---|---|
| DOM-01 | §4 (04) | contador que no cuenta cabeceras |
| DOM-02 | §4 (06) | guarda del `#¡DIV/0!` en la ficha |
| DOM-03 | §2 (02) | cruce de medianoche con MOD+ROUND |
| DOM-04 | §4 (05) | calendario por semanas + saldo desde solicitudes |
| DOM-05 | §2 (01) | las 4 alertas existen; 12 h art. 34.3 |
| DOM-06 | §5 §7.2 | badge legal: 2019, no 2026; sanción por centro |
| DOM-07 | §2 (02) §5 | recargo en celda verde; FAQ reformulada |
| DOM-08 | §3 (03) | SS empresa en celda 33 % + pagas prorrateadas |
| DOM-09 | §3 (03) | cubiertos por SERVICIO, no por día |
| DOM-10 | §3 (BONUS-02) §7.4 | 7 FTE y ratio 31,3 % por defecto |
| DOM-11 | §2 (02) | guarda de H. contratadas vacía |
| DOM-12 | §2 (02) | art. 35.1 y excepciones del 35.2 |
| DOM-13 | §4 (07) | «Alérgenos Propios» eliminado (art. 9 RGPD) |
| DOM-14 | §4 (07) | vencimientos para los 30 empleados |
| DOM-15 | §4 (04) §7.3 | alta previa a la jornada + Contrat@, RLT, 145 |
| DOM-16 | §3 (03) | semáforo con umbrales por tipo de negocio |
| DOM-17 | §2 (01) | `Cuadrante Mensual` con fórmulas y DV |
| DOM-18 | §3 (BONUS-02) | días de apertura entran en el cálculo |
| DOM-19 | §4 (05) | días de convenio en celda + prorrateo por alta |
| DOM-20 | §4 (05) | `Cobertura` con recuento y alerta reales |
| DOM-21 | §2 (02) | columna Pausa para el turno partido |
| DOM-22 | §4 (04) | categorías sin truncar a 14 caracteres |
| DOM-23 | §3 (BONUS-02) §5 | 10 tipos por DV + VLOOKUP |
| DOM-24 | §4 (07) | NAF, nacimiento, convenio, grupo, carnets |
| DOM-25 | §2 (01) | horas contratadas por empleado, no 40 fijo |
| DOM-26 | §5 | copy con tildes y eñes |
| DOM-27 | §1.1 | leyenda de códigos única (P vs PE) |
| DOM-28 | §4 (04) | denominador sin las tareas «—» |
| DOM-29 | §2 (BONUS-01) | bloques de caja y de temperaturas |
| DOM-30 | §4 (06) | N/A en la escala + media solo de lo valorado |
| DOM-31 | §3 (03) | «Horas Contratadas» → coste/hora |
| DOM-32 | §1.3 | 30 empleados en todo el kit |
| TEC-01 | §2 (02) | MOD verificado en pycel |
| TEC-02 | §4 (04) | COUNTIF acotado por tramo |
| TEC-03 | §4 (06) | `IF(COUNT()=0,"")` en media y nivel |
| TEC-04 | §4 (05) | «Días Usados» deja de contar meses |
| TEC-05 | §2 (01) | alertas reales + hoja mensual viva |
| TEC-06 | §2 (02) | 1,75 y 2,0 salen de las 30 fórmulas |
| TEC-07 | §4 (07) | bloque de vencimientos a 30 filas |
| TEC-08 | §2 (02) | `SUMIF` desde `Registro Horas` |
| TEC-09 | §2 (02) | guarda sobre F, no solo sobre E |
| TEC-10 | §3 (03) | nada de verde con la hoja vacía |
| TEC-11 | §3 (03) | umbrales por `VLOOKUP` sobre la tabla |
| TEC-12 | §4 (04) | `slice[:14]` del generador |
| TEC-13 | §4 (04) | «de 51» y «47» dejan de divergir |
| TEC-14 | §3 (03) | 0,30 en 21 celdas → parámetro |
| TEC-15 | §3 (03/BONUS-02) | un solo modelo de dimensionamiento |
| TEC-16 | §3 (BONUS-02) | DV en tipo de negocio, sin cajón de sastre |
| TEC-17 | §1.2 | formato condicional real |
| TEC-18 | §4 (05) | el saldo descuenta la solicitud en curso |
| TEC-19 | §4 (07) | convenio y carnets como columnas |
| TEC-20 | §3 (03) | rótulo del coste: equipo, no un turno |
| TEC-21 | §3 (BONUS-02) | el ×14 pasa a celda de pagas |
| TEC-22 | §1.7 §7.6 | freeze, títulos de impresión, `fitToWidth=2` |
| TEC-23 | §2 (01) | DV, freeze e Instrucciones del mensual |
| TEC-24 | §4 (06) | `wrap_text` y alto en celdas combinadas |
| TEC-25 | §1.6 | formatos de hora, fecha y moneda |
| TEC-26 | §2 (02) §3 (03) | Tipo Extra y Horas Contratadas se usan |
| TEC-27 | §4 (06) | tendencia sobre los dos últimos trimestres |
| TEC-28 | §2 (BONUS-01) | DV de gravedad y prioridad |
| COM-01 | §2 (01) §5 | alertas del cuadrante: se construyen |
| COM-02 | §2 (02) §5 | FAQ del convenio: parámetro editable |
| COM-03 | §4 (04) §5 | el changelog v1.1 pasa a ser cierto |
| COM-04 | §4 (06) | error cacheado en el fichero que se firma |
| COM-05 | §5 §7.2 | base legal del hero |
| COM-06 | §4 (05) | una celda por mes → 53 semanas |
| COM-07 | §2 (02) | turno de noche en negativo |
| COM-08 | §6 §7.1 | reviews y testimonios: aparcado por John |
| COM-09 | §3 | 15 vs 8 personas: un solo modelo |
| COM-10 | §1.2 | color prometido sin formato condicional |
| COM-11 | §3 (03) | semáforo vs tabla de la misma hoja |
| COM-12 | §2 (01) | rejilla mensual muerta + 5ª semana |
| COM-13 | §3 (BONUS-02) §5 | días de apertura y picos de demanda |
| COM-14 | §2 (02) | «agrega por empleado» pasa a ser cierto |
| COM-15 | §6 | ancla de precio: aparcada por John |
| COM-16 | §4 (07) §5 | convenio y carnets en el directorio |
| COM-17 | §3 (03) | verde «EXCELENTE» sin datos |
| COM-18 | §1.3 | 50 filas de registro → 300 + aviso |
| COM-19 | §2 (02) | ET, fuerza mayor y tope de 80 h |
| COM-20 | §4 (05) §5 | cobertura mínima real |
| COM-21 | §4 (06) §5 | plan de desarrollo individual |
| COM-22 | §5 | `products-catalog.ts`: ratios inexistentes |
| COM-23 | §5 | 40 vs 30-60 EUR/mes unificado |
| COM-24 | §4 (05) | 30 días en celda, no en 30 fórmulas |
| COM-25 | §4 (07) | sección RGPD reescrita y el «cómo» |
| COM-26 | §4 (06) §7.5 | duplicar la ficha y volcar al histórico |

## 7-bis. Decisiones del orquestador sobre las dudas de §7 (2026-08-23)

1. **Testimonios (COM-08)**: se reescriben SOLO los dos que siguen describiendo funcionalidades
   inexistentes tras la v2.0 (Francisco Torres y Enrique Vidal), para que describan lo que el kit
   HACE (coste laboral con parámetros por convenio; dimensionamiento por servicio). `aggregateRating`,
   `reviews` y el resto de testimonios NO se tocan (aparcado por John; queda en el handoff).
2. **Sanción en la FAQ**: se cita con artículo — «infracción grave, art. 7.5 LISOS: 751 a 7.500 €
   por centro de trabajo» — y el integrador verifica el tramo vigente antes de publicar.
3. **04**: sí — 50 tareas (Contrat@/SEPE, copia básica a la RLT, modelo 145); «40+ tareas» se mantiene.
4. **BONUS-02**: sí — salario por defecto 1.500 €/mes en 14 pagas; el caso por defecto debe caer
   en ratio ~31 %.
5. **06**: sí — ficha en blanco + hoja «Ficha (ejemplo relleno)» + instrucción de duplicar.
6. **07**: sí — dos páginas A4 (`fitToWidth=2`), sin partir la Plantilla en bloques.
7. Las 277 líneas se aceptan: las fórmulas literales de §2/§4 son la spec, no relleno.
