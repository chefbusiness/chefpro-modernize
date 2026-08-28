# Kit Plan Financiero para Restaurantes — v2.0 (SPEC, 2026-08-23)

Origen: ronda 1 adversarial (`auditorias/kit-plan-financiero-R1.json`, 3 lentes opus — dominio financiero, técnica Excel, coherencia comercial; **90 hallazgos**, «no listo»
×3). Lo que sigue es lo que SE HACE; lo demás se descarta en §6 o se pregunta en §7; la evidencia está en el R1, citada aquí por id. Método y código de referencia:
`kit-inventario-v2-SPEC.md` y `kit-escandallos-v2-SPEC.md` con su paquete (motor + grupos, `main.py --dry-run / --solo`, respaldo previo, `inject_cache.py` al final,
verificación `data_only`, idempotencia por reconstrucción). Paquete nuevo `scripts/productos-digitales/kit-plan-financiero-v2_0/` (`motor.py`, `grupo_a.py`, `grupo_b.py`,
`grupo_c.py`, `main.py`); ejecución real solo con `KIT_PLAN_FINANCIERO_APPLY=1`.

Ficheros: `astro-site/public/dl/kit-plan-financiero/` — **los mismos 10 xlsx con los mismos nombres**: las 10 claves de descarga (`get-download-urls.ts:562-573`) viajan en
emails ya enviados. Se añaden hojas, columnas y filas; no se quita ningún entregable. Es el más caro de su familia (39 €) y **se vende para presentarlo a un banco**: el listón
es que el 07 se imprima y se entregue sin una sola celda en cero.

Convenciones: editables **verdes `E8F5E9`** y desbloqueadas, calculadas sin relleno; parámetros en celda, nunca literales dentro de la fórmula; `IFERROR` en toda división;
semáforo por formato condicional (verde `C6EFCE`, ámbar `FFEB9C`, rojo `FFC7CE`); DV con `showErrorMessage=True`; protección de hoja **sin contraseña**; bio anclada; «Versión
2.0 · agosto 2026»; metadata `title`/`subject` → `… · v2.0`; changelog 2.0 y `updateNote`; `inject_cache.py` al final; idempotencia; `--dry-run` por defecto. El A4 ya está
(`paperSize=9` en los 10): no se toca.

**pycel (1.0b30, medido hoy):** implementa `NPV`, `ROUNDUP`, `ROUND`, `MAX`, `MIN`, `ABS`, `AVERAGE`, `SUM`, `SUMIF`, `COUNTIF`, `INDEX`, `MATCH`, `IFERROR`, `TEXT` y el
operador `^`. **NO implementa `IRR`, `PMT` ni `COUNTA`** («Function IRR is not implemented. IRR is in the "Financial" group») y **`IFERROR` no lo atrapa**: la evaluación
revienta antes. Obligatorio: `COUNTA` → `COUNTIF(rango,"<>")`; `PMT`/`PAGO` → anualidad algebraica `importe*i/(1-(1+i)^-n)` (verificado: 100.000 € al 5 % en 60 meses → 1.887,12
€); `IRR` → fórmula en la celda **y caché aparte** (§1.8). Nada de builds locales ni Playwright; python en serie; `istats` entre barridos.

## 1. Motor común (`motor.py`) — los 10 ficheros

- **1.1 Gráficos: se construyen de verdad** (DOM-08/TEC-06/COM-03, altas). «Gráficos automáticos» se anuncia **seis veces** (hero, ContentGrid ×3, CTA, FAQ con JSON-LD y
  dashboard) más un testimonio, y hoy hay **0 charts en las 53 hojas de la v1.1 (56 en la v2.0)**. Con `openpyxl.chart` en **9 de los 10** (todos menos el BONUS-09): `01`/`01b`!Resumen `A10` `BarChart` de ingresos, gastos y EBITDA por año ·
  `02`!Break-Even `F4` `LineChart` de ingresos vs costes totales sobre el bloque auxiliar nuevo `A20:D31` · `03`!Alertas `F5` `LineChart` de saldo final + serie de umbral
  (columna `E` = `=$C$3`) · `04`!Resumen `F4` `BarChart` presupuesto vs real por categoría · `05`!'Resumen Anual' `A18` `BarChart` previsto vs real · `06`!Ratios `G16`
  `BarChart` tu valor vs objetivo (columnas numéricas nuevas de `Benchmarks`, §4) · `07`!Proyecciones `H3` `LineChart` de EBITDA y cash flow operativo 1-5 ·
  `BONUS-08`!Comparativa `B10` `BarChart` de EBITDA anual por escenario.
- **1.2 Formato condicional real** (TEC-18/COM-14): **0 reglas** en las 53 hojas de la v1.1 (56 en la v2.0) y tres Instrucciones prometen colores; hay emojis en texto negro, que en el A4 en blanco y
  negro de la Fase A no destacan. `semaforo(ws, rango, vocabulario)` con `containsText` en `03!Alertas!C6:D17`, `05!Ene..Dic!F6:F21`, `06!Ratios!E17:E25` y `07!Ratios!E4:E10`;
  regla `expression` `=$C6<$C$3` en `03!Alertas` y para el DSCR.
- **1.3 Guardas, parámetros en celda y protección** (TEC-11/TEC-15/TEC-25): `IFERROR` en las seis divisiones desnudas de `06!Ratios` (`C17`, `C19`, `C21`, `C22`, `C23`, `C24`)
  y en las tres de `02!Break-Even` (`C8` revienta con coste variable al 100 %, `C9` con 0 días de apertura, `C10` con ticket 0), con texto de ayuda en vez de `#¡DIV/0!`. Ningún
  parámetro que exista como input en otra hoja del libro va como literal en una fórmula. `ws.protection.sheet = True` sin contraseña en las 53 hojas de la v1.1 (56 en la v2.0) (hoy `protected=False` en
  todas), verdes con `Protection(locked=False)`, línea «Revisar → Desproteger hoja» y validación numérica ≥ 0 en importes y 0-1 en porcentajes.
- **1.4 Datos de ejemplo etiquetados y coherentes** (TEC-27/COM-19): `03!B5`=15.000, `06!Ratios!C6:C12` y `02!Datos!C6:C21` van tecleados sin marca, y el ejemplo del 02
  describe un negocio inviable según el propio kit (labor cost 41 %, prime cost ~71 %, «Peligro» en `06!Benchmarks`). Fila «VALORES DE EJEMPLO — sustitúyelos por los tuyos» en
  cada hoja de datos y recalibrado contra sus benchmarks (§7.5).
- **1.5 Base «sin IVA» declarada** (DOM-17): no se dice si ventas y ticket medio van con IVA —el error número uno del sector: con el 10 % de restauración el food cost sale ~3
  puntos bajo— y el 03 sí lo aclara, así que el kit es incoherente consigo mismo. «(sin IVA)» en cada etiqueta de ventas y ticket de 01, 01b, 02, 05, 06 y 07, más la línea
  «Todas las cifras van SIN IVA; en el 03 van CON IVA porque es caja».
- **1.6 Formatos, anchos y cabeceras** (TEC-20/TEC-29): `07!'Resumen Ejecutivo'!C5:C25` es la única hoja **sin celdas creadas y sin verde** (el analista lee «150000», no
  «150.000,00 €»): se crean con `E8F5E9`, `#,##0.00 €` en `C13:C15`/`C17`/`C18`, `#,##0` en `C8`/`C9`, fecha en `C10` y `freeze_panes='C5'`. Anchos: `07!Garantías` col. B a 45
  (hoy trunca «Aval SGR…») y `03!Alertas` col. B a 26.
- **1.7 Instrucciones, bio y versión** (DOM-28/COM-28/TEC-28): `01b!B9` («Año 1 con desglose mensual. Años 2-5 con desglose mensual.») → «Los cinco años van con desglose
  mensual (Ene-Dic) y total anual en la columna N»; `04!B13` nombra pestañas inexistentes («Obra civil», «Licencias y Permisos») → los nombres reales. Bio anclada, que **no la
  lleva ninguno de los 10**: «Diseñado por John Guerrero — chef y consultor gastronómico desde 2010, en cocina desde los 17 años · johnguerrero.es»; pie «Versión 2.0 · agosto
  2026 · aichef.pro/kit-plan-financiero · info@aichef.pro»; y `subject` → `… · v2.0` (hoy v1.1 en los 10).
- **1.8 Orden de construcción y caché de la TIR** (soporta DOM-03/TEC-03/COM-02). Orden en `main.py`: construir hojas → **insertar gráficos** → guardar → `inject_cache.py` →
  `cachear_irr()` → verificación `data_only`. Medido hoy: openpyxl 3.1.3 **conserva** los charts al recargar y guardar (siguen en `ws._charts` y en `xl/charts/chart1.xml`) e
  `inject_cache.py` también, porque reescribe el zip a mano sin `wb.save()`; aun así el gate los cuenta **después** del post-proceso. **La TIR es el punto ciego de la Fase A**:
  `07!Proyecciones!B21` es la única fórmula del kit sin caché (1 de 1.373) porque pycel no evalúa `IRR`, y en Vista previa de macOS o Google Sheets sale en blanco.
  `cachear_irr()` lee con `data_only` los flujos cacheados de `Proyecciones!B19:F19`, calcula por **Newton-Raphson** sobre `VAN(r)=Σ Fᵢ/(1+r)ⁱ` (semilla 0,1, 100 iteraciones,
  tolerancia 1e-10, bisección en [−0,99, 10] si la derivada se anula) e inyecta el `<v>` con el mecanismo de `inject_cache.py`. Caso trazado: −150.000 / 30.000 / 45.000 /
  60.000 / 70.000 → TIR **11,9592 %**, VAN al 8 % **15.440,05 €** (lo confirma pycel, que sí evalúa `NPV`) y payback **3,21 años**.

## 2. Grupo A — proyección y consolidados (01, 01b, 05) — `grupo_a.py`

- **Las tres «Resumen» que no consolidan nada** (DOM-04/DOM-05/TEC-04/TEC-05/COM-04, altas): 0 constantes sin fórmula **y sin relleno de input**, mientras las Instrucciones
  prometen que «consolida los 3/5 años» y «consolida los 12 meses»; el patrón correcto ya existe en el kit (`04!Resumen!B5="='Obra'!B15"`). **01**: `B5="='Año 1'!N10"`,
  `C5="='Año 2'!N10"`, `D5="='Año 3'!N10"`; fila 6 → `N19`; fila 7 → `N21`; `B8='=IFERROR($B7/$B5,"")'`. **01b**: igual hasta `F` (Año 5). **05!'Resumen Anual'**:
  `B5="='Ene'!B10"`, `B6="='Ene'!C10"`, `B7="='Ene'!B19"`, `B8="='Ene'!C19"`, `B9="='Ene'!B21"`, `B10="='Ene'!C21"`, arrastrado `C..M`, y `N5:N10 '=SUM(B5:M5)'` (hoy la columna
  TOTAL tampoco suma). Filas nuevas: desviación anual de ingresos (€ y %), de EBITDA (€) y food/labor/prime cost anuales desde `'Ene'!C13:C14`.
- **01/01b, columna de crecimiento** (DOM-27): solo `E5` (`G5` en 01b) tiene fórmula; `E6:E8` son 0 constantes en formato de porcentaje. Se replica
  `'=IFERROR(($D5-$B5)/$B5,"")'` en `E6:E7` y, para el margen (fila 8, que ya es porcentaje), `'=$D8-$B8'` etiquetado **p.p.**, no «crecimiento».
- **05, el semáforo que miente en dos direcciones** (DOM-12/TEC-09/TEC-10, ×12 pestañas): `F6:F21` usa `ABS()`, así que vender un 20 % **por encima** del presupuesto o gastar
  un 12 % **menos** en food cost se marcan «🔴 Alerta» igual que pasarse. Criterio con signo: ingresos y EBITDA (6-10 y 21)
  `'=IF($E6>=-0.05,"✅ OK",IF($E6>=-0.1,"⚠️ Atención","🔴 Alerta"))'`; gastos (13-19) `'=IF($E13<=0.05,…)'`. Y `E21='=IFERROR(($C21-$B21)/ABS($B21),"")'`: con EBITDA
  presupuestado negativo —lo normal en una apertura, el público del kit— hoy se invierte el signo y una mejora de 3.000 € sale en rojo.
- **05, media tabla vacía bajo su encabezado** (TEC-26): Margen EBITDA % y las tres de «RATIOS AUTOMÁTICOS» solo tienen Presupuesto y Real: `D`, `E` y `F` no existen.
  `D22='=$C22-$B22'` con formato `0,0 %`, `E22` con el texto «p.p.» y `F22` con semáforo por puntos porcentuales; ídem 25-27, ×12.

## 3. Grupo B — tesorería, equilibrio e inversión (02, 03, 04) — `grupo_b.py`

- **03, el encadenado roto del saldo** (DOM-01/TEC-01/COM-01, alta): `C5:M5` leen la fila **22** («Otros pagos», dentro de TOTAL PAGOS) en vez de la **25** («SALDO FINAL»):
  once meses de tesorería erróneos y once alertas rojas falsas **ya cacheadas en el fichero que se descarga**. Es de origen (`git show 7e050c5:`) y la Fase A no lo vio porque
  la fórmula es sintácticamente válida. En la numeración nueva, `C5='=B29'` … `M5='=L29'`. Caso trazado: saldo 15.000, cobros 40.000, pagos 35.000 en enero → febrero abre en
  20.000.
- **03, hoja nueva `Parámetros`: el desfase y el IVA dejan de ser palabras** (DOM-10/DOM-23/TEC-17/COM-09/COM-15, altas). Verdes: % de ventas con tarjeta, días de abono
  (D+1/D+2), plazo de pago a proveedores, IVA repercutido (10 %), soportado de compras (10 %) y de gastos (21 %), y estacionalidad por mes. Mapa nuevo de `Flujo Mensual`:
  **12** VENTAS DEL MES `=SUM(B7:B11)` · **13** Pendiente de abono de tarjeta `'=IF($B12="","",$B12*Parámetros!$C$4*Parámetros!$C$5/30)'` · **14** TOTAL COBROS DE CAJA
  (`B14='=B12-B13'`, `C14='=C12-C13+B13'`) · **16** Pago a proveedores (`C16='=C33*(1-p/30)+B33*p/30'`) · **17** Nóminas (neto) · **18** Pago de Seguridad Social (mes anterior)
  (`C18='=B34'`) · 19-22 alquiler, suministros, marketing, gestoría · **23** Cuota de préstamo (nota: cópiala del cuadro del 07) · **24** Retenciones IRPF (mod. 111) · **25**
  Liquidación de IVA · **26** Otros pagos · **27** TOTAL PAGOS `=SUM(B16:B26)` · **28** FLUJO NETO `=B14-B27` · **29** SALDO FINAL `=B5+B28`. Bloque gris `31:34` «datos base,
  no son caja» (compras del mes, SS devengada) y `36:37` (IVA repercutido `'=IF($B12="","",$B12-$B12/(1+Parámetros!$C$7))'` y soportado). La fila 25 calcula **solo en el
  calendario AEAT**: `E25='=MAX(0,SUM($B$36:$D$36)-SUM($B$37:$D$37))'` (abril liquida el 1T), `H25` el 2T, `K25` el 3T; `B25` queda verde para el 4T anterior con la nota «mod.
  303: 1-20 de abril, julio y octubre; 1-30 de enero»; el resto, `=""`. Así `Instrucciones!B8` pasa a ser cierta.
- **02, Escenarios desconectado de Datos** (DOM-13/TEC-08/COM-20): `C7:E7` repiten 19.000 € como constantes y `C10` lleva el `26` dentro de la fórmula, mientras `Break-Even` sí
  lee de `Datos`: dos verdades distintas en el mismo fichero. `C7:E7 '=Datos!$C$14'` y `C10='=C4*C5*Datos!$C$21'` (ídem `D10`/`E10`); la fila 6 se renombra «% Coste variable
  (food + comisiones; NO incluye personal fijo)» con remisión al 08.
- **02, el EBITDA que resta la cuota del préstamo** (TEC-23/DOM-24): `Datos!C12` (cuota, 800 €) está dentro de `C14='=SUM(C6:C13)'`, así que la fila «EBITDA» de `Escenarios` va
  después del servicio de deuda y luego se compara con los benchmarks de EBITDA del 06 y del 07. La cuota pasa a fila propia `C15`, `C14` suma `C6:C11`+`C13`, y `Break-Even`
  gana **dos** resultados: break-even operativo (EBITDA = 0) y break-even de caja (con la cuota). `Datos!B7` unifica su etiqueta contradictoria («bruto» vs la nota «incluye SS
  empresa», 30-33 % sobre 12.000 €) en «Coste total de personal fijo (salario bruto + SS empresa)», nota «≈ bruto × 1,32».
- **02, redondeo del umbral y ticket necesario** (DOM-25/TEC-16/COM-27): `C10` vale 51,10 y el formato `#,##0` muestra «51»; 51 × 22 € × 26 días = 29.172 €, **por debajo** del
  break-even de 29.230,77 €. `C10='=IFERROR(ROUNDUP($C9/Datos!$C$20,0),"Indica el ticket medio")'`, `C11='=IFERROR(ROUNDUP($C8/Datos!$C$20,0),"—")'`. Fila nueva «Ticket medio
  necesario (€)» `'=IFERROR($C9/cubiertos_previstos,"")'` con su input verde: la ficha promete calcularlo y hoy el ticket es un dato de entrada.
- **04, base imponible, IVA y amortización** (DOM-15/COM-13): las cinco hojas tienen `Partida | Presupuesto | Real | Desviación % | Notas` y el libro no menciona el IVA ni una
  vez, mientras la landing promete «totales con y sin IVA» — y el desembolso real es un 21 % mayor que el presupuesto que se enseña, con recuperación diferida. Cabecera nueva
  `Partida · Base (€) · IVA % · IVA (€) · Total con IVA (€) · Real (€) · Desviación % · Coef. amortización · Dotación anual (€) · Notas`, con `D5='=IF($B5="","",$B5*$C5)'`,
  `E5='=IF($B5="","",$B5+$D5)'`, `G5='=IFERROR(($F5-$B5)/$B5,"")'` e `I5='=IF(OR($B5="",$H5=""),"",$B5*$H5)'`; coeficiente por hoja (obra 3 %, equipamiento de cocina 12 %,
  mobiliario 10 %, tecnología 25 %, licencias 0 % = gasto del ejercicio). `Resumen` gana «Inversión (base)», «IVA soportado a recuperar», «Desembolso total» y «Dotación anual a
  la amortización», de donde sale la fila `Amortización` del 07.
- **04, hoja nueva `Otros conceptos de apertura`** (DOM-16): las 46 líneas actuales no recogen traspaso, fianza y primeras rentas, constitución/notaría/registro, stock inicial,
  nóminas y formación pre-apertura, marketing de lanzamiento, imprevistos (5-10 %) ni **fondo de maniobra 3-6 meses** — y el kit sabe que falta (`BONUS-09!C15`, sin celda donde
  ponerlo). `Licencias!A13` «Seguros (año 1)» es OPEX y duplica `02!Datos!B8`: se mueve aquí como gasto anticipado no amortizable.

## 4. Grupo C — informe bancario, ratios y bonus (06, 07, BONUS-08, BONUS-09) — `grupo_c.py`

- **07, el P&L que no calcula ni una línea** (DOM-02/TEC-02/COM-18, altas): TOTAL GASTOS, EBITDA, BAI, IS, BENEFICIO NETO y CASH FLOW OPERATIVO son 0 constantes **sin relleno
  verde**, así que se leen como resultados y se presentan al banco en cero; el libro entero tiene 3 fórmulas. `B8:F8 '=SUM(B5:B7)'`; `B9 '=$B4-$B8'`; `B12 '=$B9-$B10-$B11'`;
  `B13 '=IF($B12>0,$B12*$C$31,0)'`; `B14 '=$B12-$B13'`; `B16 '=$B14+$B10'`; verde solo en `B4:F7`, `B10:F11` y parámetros. **`C31` «Tipo impositivo (%)» en celda** (DOM-19):
  hoy el 25 % va clavado en la etiqueta cuando el destinatario típico es una entidad de nueva creación (15 % los dos primeros ejercicios con base positiva, art. 29.1 LIS) y
  puede no ser una SL — el propio `BONUS-09!C5` contempla autónomo y cooperativa (§7.6).
- **07, TIR, VAN y payback** (DOM-03/TEC-03/COM-02, altas): `IRR`/`NPV` operan sobre `B19:F19`, donde solo existe `B19=-150000`; los flujos viven en la fila 16, que no se
  referencia jamás, y el payback es una celda verde vacía. Fila **19** «Flujo de caja del proyecto»: `B19="=-'Resumen Ejecutivo'!$C$13"` y `C19:F19 '=C16'`…; fila **20** «Flujo
  acumulado»: `B20='=B19'`, `C20='=$B20+C19'`… `C25` **«Tasa de descuento (%)» verde** al 8 % (un banco pregunta qué tasa se ha usado). `B21='=IFERROR(IRR($B$19:$F$19),"—")'`
  (caché por §1.8); `B22='=IFERROR(NPV($C$25,$C$19:$F$19)+$B$19,"—")'`; payback por fórmula, medida y evaluable por pycel:
  `B23='=IFERROR(IF($F$20<0,"No se recupera en 5 años",COUNTIF($B$20:$F$20,"<0")-1+(-INDEX($B$20:$F$20,COUNTIF($B$20:$F$20,"<0")))/INDEX($B$19:$F$19,COUNTIF($B$20:$F$20,"<0")+1)),"—")'`.
  Se borra el texto muerto de `B20` («→ Ver fila Cash Flow Operativo arriba»).
- **07, hoja nueva `Financiación`** (DOM-14): falta el cuadro de amortización, la pieza que un banco mira después del EBITDA, y sin él el DSCR > 1,25× que el propio informe
  exige no se puede calcular sin salirse del kit. Verdes: importe, tipo nominal, plazo en años y carencia. Cuadro por año 1-5 con **anualidad algebraica** (`PAGO`/`PMT`
  prohibido, pycel no lo implementa): cuota `'=IF($C$4=0,0,$C$4*$C$5/(1-(1+$C$5)^(-$C$6)))'`, intereses = capital pendiente × tipo, capital = cuota − intereses, capital
  pendiente. Los intereses alimentan `Proyecciones!B11:F11`; la cuota, el DSCR y la fila 23 del 03.
- **07, los siete ratios vacíos** (DOM-11/TEC-19/COM-17): `Ratios!C4:C10` no tiene ni celdas creadas —solo etiquetas y la referencia bancaria—, y ahí está el DSCR, que es el
  número que decide la operación. Bloque nuevo «Datos de balance y deuda» (activo y pasivo corriente, fondos propios, deuda viva) y: endeudamiento `=deuda/(deuda+FFPP)`; DSCR
  `'=IFERROR(Proyecciones!$B$16/Financiación!$D$5,"—")'`; liquidez `=AC/PC`; margen EBITDA `'=IFERROR(Proyecciones!$B$9/Proyecciones!$B$4,"—")'`; ROI
  `=Proyecciones!B14/inversión`; FFPP/Inversión; Deuda/EBITDA. Columna **E «Estado»** con semáforo contra la columna D, que ya está escrita.
- **07, la inversión ficticia de 150.000 €** (DOM-21/COM-16): precargada en una celda verde bajo un epígrafe de «indicadores», sin relación con el resumen ejecutivo (`C13`
  vacía) ni con el CAPEX, en un documento que se imprime y se entrega. `B19` pasa a `"=-'Resumen Ejecutivo'!$C$13"` y el 150.000 sobrevive solo como texto de ejemplo. Regla de
  familia: en un fichero que se entrega a un tercero, ningún dato de ejemplo queda precargado con aspecto de dato real.
- **06, el RevPASH que no es RevPASH** (DOM-07/TEC-13/COM-07, alta): `C22='=C6/(C11*C12)'` divide por **metros cuadrados** y la etiqueta se delata escribiendo «€/m²/hora»;
  luego se compara con «> 8 € casual dining», que es un umbral **por plaza y hora**, así que el ejemplo da 2,95 € y el usuario concluye que va tres veces por debajo del sector.
  Input nuevo «Nº de plazas (aforo)», `C22='=IFERROR($C6/($C11*$C13),"—")'` con etiqueta «RevPASH (€/plaza/hora)» y fila aparte «Ventas por m² de sala» con su benchmark.
- **06, el GOP que depende de la interpretación** (DOM-18/TEC-14/COM-32): `C9` «Gastos operativos totales» no define qué incluye y en USALI el GOP va antes de rentas y cargas
  de propiedad: dos usuarios con el mismo negocio obtienen GOP separados por 10-15 puntos. `C9` pasa a **calculado** `'=IFERROR($C7+$C8+$C16,"")'` (materia prima + personal +
  otros, con `C16` como input nuevo), se separan `C14` alquiler y `C15` amortización, y se añade fila **EBITDA %** `'=IFERROR(($C6-$C9-$C14-$C15)/$C6,"—")'` contra su propio
  benchmark, con guarda visible ante un valor incoherente.
- **06, una sola fuente de umbrales** (DOM-29/TEC-12/COM-29/DOM-22): el food cost vale 32 % en Instrucciones y en la columna de referencia y 33 % en la fórmula y en
  `Benchmarks`; el labor cost acepta hasta 31 % en `E18` frente al «Peligro > 30 %» de `Benchmarks!E5`; el prime cost, 66 % contra 65 %. `Benchmarks` gana **columnas
  numéricas** `F` («óptimo hasta») y `G` («peligro desde»), y `E17:E25` las leen
  (`'=IF($C17<Benchmarks!$F$4,"✅ Excelente",IF($C17<=Benchmarks!$G$4,"⚠️ Aceptable","🔴 Alto"))'`); `Instrucciones!B12:B15` se reescriben con esos números, que además alimentan
  el gráfico de §1.1. Se añade el semáforo que falta en las filas 21-24, donde el ejemplo situaba al restaurante en «Peligro» de su propio benchmark (coste por cubierto /
  ticket = 85 % frente al «> 70 %» de `Benchmarks!E11`) sin que nada lo señalara.
- **BONUS-08, doble contabilización del personal** (DOM-06/COM-08, altas): `C11` toma como «costes fijos mensuales» los mismos 19.000 € que en el 02 **ya incluyen 12.000 € de
  nóminas**, y encima aplica un labor cost del 28 % sobre ventas: el escenario BASE —el que se enseña a un inversor— sale con **−5.272 €/mes y −63.264 €/año** mientras el 02,
  con el mismo ticket, da EBITDA positivo. `A11` → «Costes fijos mensuales **SIN personal** (alquiler, suministros, seguros, gestoría, cuota de préstamo)», con nota: «si copias
  los costes fijos del 02, resta antes las nóminas».
- **BONUS-08, escenarios recalibrados y homogéneos con el 02** (TEC-21/TEC-22/COM-26): dos de los tres salen en pérdidas en un fichero que sus Instrucciones proponen para
  «negociar con inversores o socios». Base común con el 02 (ticket 22 €, **55 cubiertos**, 26 días) y fijos sin personal 9.500 / 9.800 / 9.200 → EBITDA base ≈ 3.100 €/mes
  (**~10 % sobre ventas**); el pesimista sigue negativo a propósito. Y la «ocupación» que anuncian landing, dashboard e `Instrucciones!B7` no existe —la variable es «Cubiertos
  / día»—: se cambia la palabra en las cuatro superficies.
- **BONUS-09, la fase que falta y el contador honesto** (DOM-20/DOM-26/TEC-24/COM-30): la checklist financiera pre-apertura no tiene **ni una** tarea de alta laboral
  (inscripción de la empresa en la SS y CCC, alta en RETA del promotor, comunicación de apertura del centro de trabajo, contratos según el convenio provincial de hostelería,
  alta de trabajadores previa al inicio, registro de jornada y calendario de nóminas/mod. 111), todas con sanción directa e impacto de caja el primer mes, mientras la fase 6
  detalla la «política de propinas». Fase 7 «Personal y obligaciones laborales» con 6 tareas → **54** (§7.4). Contador honesto: `C55='=COUNTIF($A$5:$A$64,"<>")'` (`COUNTA`
  prohibido) y `C59='=IFERROR(COUNTIF($F$5:$F$64,"Completada")/$C$55,0)'` en vez del 48 escrito a mano; DV de lista sobre `F5:F64` con `showErrorMessage=True` y CF por estado,
  para que «completado» o «COMPLETADA » dejen de congelar el avance en 0 %.

## 5. Integración — landing, dashboard, changelog, emails, gates (`integracion`, sonnet)

- **Superficies**: la fuente que sirve producción es `astro-site/src/data/productos/kits/kit-plan-financiero.ts`; los gemelos de la SPA (`src/components/kit-plan-financiero/*`,
  `src/pages/KitPlanFinanciero.tsx`, `src/pages/KitPlanFinancieroDashboard.tsx`) reciben **los mismos cambios**, o vuelven a divergir.
- **«Fórmulas encadenadas» entre plantillas** (DOM-09/TEC-07/COM-10, alta): diez libros aislados, **cero `externalLink`** en los diez paquetes OOXML, y la FAQ describe tres
  encadenados concretos que no existen. Se reescribe como en kit-inventario: «**coherentes entre sí**: mismas líneas de ingreso y gasto, mismos ratios y la misma base sin IVA
  en las 10 plantillas; dentro de cada libro las fórmulas sí están encadenadas (mensual → total anual → resumen)» — `faqs[3].a:242`, `why.reasons[1].desc:167` y el hub
  `ProductosDigitales.tsx:320`. En cada `Instrucciones`, línea «de dónde sacar este dato» (04!Resumen → 07!Proyecciones!B10; Financiación → 03!fila 23): el encadenado realista
  entre libros sueltos.
- **Gráficos**: con §1.1 las seis afirmaciones pasan a ser ciertas en 9 de los 10. `grid.subtitle:143` deja de decir «cada plantilla incluye… graficos profesionales» y nombra
  dónde están.
- **COM-11, el email dice 9 y el producto son 10**: `verify-purchase.ts:200`, `resend-access.ts:200` y `productos-digitales-config.ts:877/880` → «las 10 plantillas financieras
  (8 + 2 bonus)». Es la peor superficie para descontar una unidad: el comprador acaba de pagar y está contando. **`get-download-urls.ts` no se toca.**
- **COM-21, el JSON-LD no coincide con la FAQ visible**: el `FAQPage` declara 4 de las 6 preguntas, recortadas. Se genera desde el **mismo array `faqs`** del acordeón, tras
  corregir la respuesta del encadenado (COM-10) y la del banco.
- **COM-25 y COM-31, la respuesta del banco**: `faqs[2].a:238` garantiza la decisión de un tercero, remata con «Lo hemos validado con asesores financieros» y dice «proyecciones
  a 3 anos» cuando el 07 proyecta a 5. Nueva redacción: «Te da la estructura que piden las entidades — resumen ejecutivo, proyecciones a 5 años, ratios de solvencia, TIR, VAN y
  payback — pero la aprobación depende de tu proyecto»; se retira la validación no nominal (§7.2).
- **COM-23, «anos» → «años»** en 6 sitios (`hero.badge:115`, `faqs[2].a:238`, testimonios `:276`/`:277`/`:278`, `schema.reviews[0].body:63`), incluido el badge rojo del hero; y
  barrido de acentos: `grep -nE '\b(anos|formulas|graficos|automatico|semaforo|desviacion)\b' src/components/kit-plan-financiero/`.
- **COM-22, el changelog**: `productos-changelog.ts:281-296` titula la v1.1 «Revisión completa de los 10 ficheros» cuando los tres cambios son A4, versión y metadatos — y esa
  «revisión completa» dejó vivos un informe bancario que no calcula nada y tres resúmenes en cero. Se retitula «Formato de impresión (A4), metadatos y versión en los 10
  ficheros» y se añade la entrada **2.0** en lenguaje de cliente, con una línea por cálculo corregido; `updateNote:309` → v2.0.
- **Fichas que pasan a ser ciertas sin tocarse**: `:149` (desfase, IVA trimestral y estacionalidad, COM-15), `:150` (totales con y sin IVA, COM-13) y `:148` (ticket medio
  necesario, COM-27) quedan respaldadas por §3.
- **Gates**: `censo-entregables.py --only kit-plan-financiero --fail --quiet` (0 defectos) · `gate-flujo-postpago.py --offline --only kit-plan-financiero` (10/10) · **gate de
  gráficos** `len(ws._charts) >= 1` en los 9 ficheros de §1.1, **después del post-proceso y de `inject_cache`** · `inject_cache.py` + `cachear_irr()` al final, con
  `fallos_pycel` = 0 salvo la propia `IRR`, que debe quedar cacheada por el segundo paso · verificación `data_only` (ninguna celda de resultado en `None`) · idempotencia
  (segunda pasada = 0 cambios) · prueba con pycel: `03!'Flujo Mensual'!C5` debe seguir al saldo final de enero y toda fórmula de estado debe cambiar con un dato fuera de
  límite.

## 6. Descartado con motivo

- **COM-05** (ancla de 190 € nunca cobrada, «-79 %», «Ahorra 151 EUR HOY», «Sube pronto») y **COM-12** (el mismo recuadro muestra «-79 %» y «72 % de descuento» a cuatro
  centímetros): tocan el **ancla de precio, aparcada por John**. No se ejecutan en la v2.0; COM-05 sube a §7.1.
- **COM-06** (`aggregateRating` 4,9/8, `schema.reviews`, 8 testimonios ficticios): aparcado por John. Sube a §7.2: dos de los ocho describen funciones que hoy no existen y la
  v2.0 las hace existir, lo que reduce —no elimina— el problema.
- **Enlaces externos entre libros** (lectura literal de DOM-09/TEC-07/COM-10, y la opción (a) de DOM-09 de fusionar el kit en 2-3 libros): no. Un `.xlsx` movido de carpeta
  rompe la referencia y el cliente ve `#REF!`; y fusionar invalidaría las 10 claves de descarga ya enviadas por email.
- **DOM-14 como «plantilla 07b nueva»**: no; el cuadro va como hoja `Financiación` **dentro del 07**. **DOM-16 como «borrar Seguros (año 1)»**: no se borra, se mueve a
  `Otros conceptos de apertura` marcado como gasto anticipado no amortizable, para que quien ya lo tenía presupuestado no lo pierda.

## 7. Dudas para el orquestador

- **7.1 DUDA DESTACADA — ancla de 190 € (COM-05).** Salió a 19 € y subió a 39 € el mismo día (`153ccc1` y `7196f1c`, 2026-04-05); los 190 € se inventaron en ese segundo commit
  y llevan 4,5 meses vivos con «-79 %» y «Ahorra 151 EUR HOY». El art. 20 de la Ley 7/1996 tras la Directiva Ómnibus (RDL 24/2021) exige que el precio anterior anunciado sea
  **el más bajo aplicado en los 30 días previos**, que aquí fue 19 €. *Recomiendo retirarlo*: quitar tachado, badge y «Sube pronto» de las 5 superficies, o sustituirlo por un
  ancla documentada (suma de los precios individuales ya publicados de cada plantilla). El riesgo de práctica comercial engañosa no compensa un número inventado.
- **7.2 DUDA DESTACADA — testimonios que citan funcionalidades inexistentes (COM-06).** Tres de los ocho se refutan abriendo el fichero: «Lo presente tal cual, con los
  graficos» (`:276`), «TIR, VAN, payback period — todo calculado automaticamente» (`:283`) y «ven 3 meses antes cuando van a tener tension de tesoreria» (`:281`). La v2.0 hace
  ciertas las tres funciones, pero quedan la cifra «me aprobaron 120.000 EUR en 2 semanas» y el `aggregateRating` 4,9/8 en `Product` sin reseñas reales — *review self-serving*,
  que Google prohíbe desde 2019 con riesgo de acción manual sobre **todo el dominio**. *Recomiendo*, sin tocar la marquee: eliminar del JSON-LD `aggregateRating` y el array
  `review`, y borrar los 120.000 €.
- **7.3 Badge del hero sin fuente (COM-24).** «El 60% de los restaurantes cierra en los primeros 3 años por falta de planificación financiera»: ni la cifra ni la atribución
  causal están respaldadas, y la regla capital del proyecto prohíbe inventar cifras. *Recomiendo* reformular sin número —«la mayoría de los cierres tempranos se explican por
  una planificación financiera inexistente»— salvo que aportes fuente y año.
- **7.4 BONUS-09: de 48 a 54 tareas.** La fase 7 laboral obliga a actualizar el «48» en `Instrucciones!B7`, `Checklist!A1`, `grid.templates[9].desc:155`,
  `bonus.items[1].desc:204`, el dashboard `:24` y el título del fichero. *Recomiendo sí*: son obligaciones con sanción, y sin ellas la checklist está incompleta justo en lo que
  más caja mueve el primer mes.
- **7.5 Datos de ejemplo: ¿recalibrar o vaciar?** El 02, el 06 y el BONUS-08 se entregan con un ejemplo que el propio kit calificaría de inviable. *Recomiendo recalibrar y
  etiquetar*, no vaciar: un fichero en blanco no enseña a usarlo, pero un ejemplo sin marca acaba presentado al banco.
- **7.6 Tipo del Impuesto de Sociedades por defecto.** `C31` sale a celda con nota, pero hay que elegir el valor precargado. *Recomiendo 25 %* (tipo general) con la nota de que
  una entidad de nueva creación tributa al 15 % los dos primeros ejercicios con base positiva y que un autónomo tributa por IRPF: precargar el 15 % daría por supuesta una forma
  jurídica que el propio `BONUS-09!C5` deja abierta.

## 7-bis. Decisiones del orquestador ya tomadas (no se reabren al construir)

1. **Mismos 10 ficheros, mismos nombres**; ni fusionar libros ni crear un 07b.
2. **03**: saldo inicial encadenado al final del mes anterior; IVA trimestral **calculado** (tipos en parámetros, calendario AEAT); SS al mes siguiente; tarjeta D+1/D+2;
   proveedores con plazo en celda.
3. **07**: P&L con fórmulas; flujos correctos (año 0 + años 1-5); VAN con tasa en celda; TIR cacheada por Newton porque **pycel no evalúa `IRR`**; payback por fórmula; DSCR
   contra la cuota.
4. **Resúmenes de 01, 01b y 05**: consolidan por **referencia**; ninguna constante 0.
5. **06**: RevPASH = ingresos / (plazas × horas de servicio), con benchmark coherente.
6. **BONUS-08**: sin doble contabilización; los costes fijos excluyen nóminas mientras el labor cost esté activo, con nota y base común con el 02.
7. **Gráficos**: de verdad (§1.1), antes de `inject_cache`, y el gate los cuenta tras el post-proceso.
8. **«Fórmulas encadenadas entre plantillas»** → «coherentes entre sí»; dentro de cada libro sí se encadena.
9. **`aggregateRating`, reseñas, testimonios y ancla de 190 €**: no se tocan (John); las dos primeras suben a §7.
10. **TIR/VAN/payback del proyecto (flujo libre sin deuda); el préstamo se mide con el DSCR** (2026-08-29, a raíz de RX-06). El año 0 es la inversión TOTAL,
   así que los años 1-5 tienen que ser flujo **libre del proyecto** = EBITDA − IS calculado SIN intereses (= EBIT×(1−t)+amortización), en fila propia y visible
   de `07!Proyecciones` («Flujo libre del proyecto (sin deuda)», fila 17), que es la que alimenta `B22:G22`. Se descarta la convención del inversor (flujo
   apalancado contra fondos propios) porque lo que pide un analista de riesgos es si el negocio se sostiene solo. Los indicadores se renombran («TIR del
   proyecto (sin apalancamiento)», «VAN del proyecto», «Payback del proyecto (años)») y la hoja lo dice bajo la tabla. La capacidad de devolver el préstamo la
   mide el **DSCR** de `07!Ratios`, que sí lee el servicio de deuda del año.

## 8. Mapa id → sección (90/90)

| id | dónde | qué |
|---|---|---|
| DOM-01 | §3 (03) | saldo inicial encadena con el saldo final |
| DOM-02 | §4 (07) | P&L del informe bancario con fórmulas |
| DOM-03 | §4 (07) §1.8 | TIR, VAN y payback reales |
| DOM-04 | §2 (01/01b) | Resumen consolida por referencia |
| DOM-05 | §2 (05) | Resumen Anual consolida los 12 meses |
| DOM-06 | §4 (BONUS-08) | fin de la doble contabilización del personal |
| DOM-07 | §4 (06) | RevPASH por plaza, no por m² |
| DOM-08 | §1.1 | los gráficos se construyen |
| DOM-09 | §5 §6 | «encadenadas» → «coherentes entre sí» |
| DOM-10 | §3 (03) | IVA trimestral calculado |
| DOM-11 | §4 (07) | los siete ratios de solvencia se calculan |
| DOM-12 | §2 (05) | semáforo con signo y EBITDA negativo |
| DOM-13 | §3 (02) | Escenarios lee de Datos |
| DOM-14 | §4 (07) §6 | hoja Financiación con cuadro francés |
| DOM-15 | §3 (04) | base, IVA y coeficiente de amortización |
| DOM-16 | §3 (04) §6 | hoja «Otros conceptos de apertura» |
| DOM-17 | §1.5 | base sin IVA declarada |
| DOM-18 | §4 (06) | GOP con alcance definido |
| DOM-19 | §4 (07) §7.6 | tipo impositivo en celda |
| DOM-20 | §4 (BONUS-09) | fase 7 de obligaciones laborales |
| DOM-21 | §4 (07) | inversión enlazada al resumen ejecutivo |
| DOM-22 | §4 (06) | semáforo en las filas 21-24 |
| DOM-23 | §3 (03) | desfase, SS, IRPF y estacionalidad |
| DOM-24 | §3 (02) | etiqueta única del coste de personal |
| DOM-25 | §3 (02) | cubiertos redondeados hacia arriba |
| DOM-26 | §4 (BONUS-09) | DV de estado y contador honesto |
| DOM-27 | §2 (01/01b) | columna de crecimiento completa |
| DOM-28 | §1.7 | instrucciones sin frases a medias |
| DOM-29 | §4 (06) | umbral único de food cost |
| TEC-01 | §3 (03) | C5:M5 apuntan a la fila del saldo final |
| TEC-02 | §4 (07) | 30 celdas de P&L con fórmula |
| TEC-03 | §4 (07) §1.8 | flujos, TIR con caché y payback |
| TEC-04 | §2 (05) | 78 constantes → referencias |
| TEC-05 | §2 (01/01b) | Resumen de los dos previsionales |
| TEC-06 | §1.1 | 0 charts → 8 charts en 9 ficheros |
| TEC-07 | §5 §6 | sin enlaces externos; copy reescrito |
| TEC-08 | §3 (02) | 26 y 19.000 dejan de ir literales |
| TEC-09 | §2 (05) | ABS() fuera del semáforo de ingresos |
| TEC-10 | §2 (05) | desviación de EBITDA sobre ABS |
| TEC-11 | §1.3 | IFERROR en las seis divisiones del 06 |
| TEC-12 | §4 (06) | umbrales alineados a Benchmarks |
| TEC-13 | §4 (06) | RevPASH con input de plazas |
| TEC-14 | §4 (06) | gastos operativos calculados |
| TEC-15 | §1.3 §3 (02) | guardas en las tres fórmulas centrales |
| TEC-16 | §3 (02) | ROUNDUP en el umbral de cubiertos |
| TEC-17 | §3 (03) | la línea de liquidación de IVA calcula |
| TEC-18 | §1.2 | formato condicional real |
| TEC-19 | §4 (07) | columna Valor con celdas y fórmulas |
| TEC-20 | §1.6 §4 (07) | Resumen Ejecutivo con formato y verde |
| TEC-21 | §4 (BONUS-08) | supuestos homogéneos con el 02 |
| TEC-22 | §4 (BONUS-08) | escenario base viable |
| TEC-23 | §3 (02) | la cuota sale del EBITDA |
| TEC-24 | §4 (BONUS-09) | denominador del % sin el 48 fijo |
| TEC-25 | §1.3 | protección sin contraseña y DV |
| TEC-26 | §2 (05) | columnas D/E/F de ratios y margen |
| TEC-27 | §1.4 | datos de ejemplo etiquetados |
| TEC-28 | §1.7 | instrucciones que nombran bien las pestañas |
| TEC-29 | §1.6 | anchos de columna que no truncan |
| COM-01 | §3 (03) | encadenado del saldo + gate de familia |
| COM-02 | §4 (07) | TIR/VAN/payback antes de prometerlos |
| COM-03 | §1.1 | gráficos en 6 superficies, ahora ciertos |
| COM-04 | §2 (01/01b, 05) | las tres consolidaciones muertas |
| COM-05 | §6 §7.1 | ancla de 190 €: aparcada, duda destacada |
| COM-06 | §6 §7.2 | reseñas y testimonios: aparcado, duda destacada |
| COM-07 | §4 (06) | RevPASH vs su benchmark |
| COM-08 | §4 (BONUS-08) | costes fijos sin personal |
| COM-09 | §3 (03) | promesa del IVA cumplida |
| COM-10 | §5 §6 | FAQ del encadenado reescrita |
| COM-11 | §5 | los emails dicen 10 plantillas |
| COM-12 | §6 | −79 % vs 72 %: ligado al ancla |
| COM-13 | §3 (04) | totales con y sin IVA en el CAPEX |
| COM-14 | §1.2 | la alerta es roja de verdad |
| COM-15 | §3 (03) §5 | estacionalidad y desfase existen |
| COM-16 | §4 (07) | los 150.000 € dejan de ser ficticios |
| COM-17 | §4 (07) | hoja Ratios con DSCR calculado |
| COM-18 | §4 (07) | las seis filas del P&L |
| COM-19 | §1.4 | ejemplo del 02 recalibrado y marcado |
| COM-20 | §3 (02) | Escenarios conectado a Datos |
| COM-21 | §5 | FAQPage generado desde el mismo array |
| COM-22 | §5 | changelog retitulado + entrada 2.0 |
| COM-23 | §5 | «anos» → «años» y barrido de acentos |
| COM-24 | §5 §7.3 | badge del 60 %: decisión de John |
| COM-25 | §5 | la FAQ del banco deja de garantizar |
| COM-26 | §4 (BONUS-08) | «ocupación» → «cubiertos/día» |
| COM-27 | §3 (02) | fila «Ticket medio necesario» |
| COM-28 | §1.7 | instrucción del 01b sin sentido |
| COM-29 | §4 (06) | una sola fuente de umbrales |
| COM-30 | §4 (BONUS-09) | contador honesto de tareas |
| COM-31 | §5 | proyecciones a 5 años, no a 3 |
| COM-32 | §4 (06) | GOP con alcance USALI |

## 7-bis. Decisiones del orquestador sobre las dudas de §7 (2026-08-23)

1. **7.1 ancla 190 € y 7.2 rating/reviews/testimonios**: NO se tocan en la v2.0 — son decisión de
   John (aparcadas por él), pero suben al handoff como AVISO LEGAL destacado (Directiva Ómnibus /
   art. 20 Ley 7/1996; riesgo de acción manual de Google por review self-serving). La v2.0 sí hace
   CIERTAS las tres funcionalidades que los testimonios citan.
2. **7.3**: sí — badge reformulado sin cifra sin fuente.
3. **7.4**: sí — BONUS-09 a 54 tareas con la fase laboral; actualizar el «48» en las 6 superficies.
4. **7.5**: recalibrar los datos de ejemplo y etiquetarlos «ejemplo orientativo — edítalo».
5. **7.6**: IS 25 % por defecto en celda, con nota del 15 % de nueva creación e IRPF si es autónomo.
