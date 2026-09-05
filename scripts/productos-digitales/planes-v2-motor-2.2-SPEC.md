# Motor de la familia Planes — parche 2.2 (2026-09-05) · consolidación de los 53 hallazgos de motor de los 4 correctores

Fuente: `$S/h-<pid>/fixer.json` (cafetería, tapas-bar, panadería, food-truck) y el resultado del workflow (motor_pendientes).
Versión de familia: `motor.VERSION = '2.2'` (VERSION_MES sigue 'septiembre 2026'). El representante bar-restaurante se regenera con
ella (hoy salió como 2.1; cambian números: payback, DSCR, base de imprevistos…).

## A. Cambios de MODELO (cambian números; con diseño decidido)

A1. **Payback del proyecto, antes de la deuda** (R-06 cafetería, REF-07-motor panadería, M-08 food-truck). Hoy 'Tesorería 12 meses'!B30
    «Inversión a recuperar» = necesidad TOTAL de caja (CAPEX + fondo + IVA recuperable, financiación incluida) y B31 la divide entre flujos
    DESPUÉS de intereses y principal: cuenta la deuda dos veces y sale «Más de 3 años» en 4 de 5. Nuevo: numerador = inversión SIN el IVA
    recuperable (CAPEX + fondo de maniobra = necesidad total − IVA soportado de la inversión); flujos = flujo neto de tesorería del año +
    intereses + devolución de principal de ese año (es decir, ANTES del servicio de la deuda), años 1-3 con la misma mecánica acumulada que
    hoy. Rótulos: «Inversión a recuperar (sin el IVA, que se recupera por el 303)», «Flujo de caja libre antes de la deuda, año N»,
    «Payback del proyecto (años), antes de la deuda»; nota: «Mide cuánto tarda el negocio en devolver la inversión con lo que genera antes
    de pagar al banco; si puedes pagar la cuota lo dice el DSCR de la hoja Financiación». Instrucciones!B30 (cifras de este plan) lee la
    misma celda. Si con 3 años no se recupera, sigue diciendo «Más de 3 años» pero en celda con formato General (ver B4).
A2. **CFADS después de impuestos** (R-20): 'Financiación'!B51:B53 y H27:H41 restan el Impuesto de Sociedades del P&L en el numerador.
    Etiqueta: «Flujo disponible para la deuda (después de impuestos)». Años 4-7 del cuadro (R-14): rotular G30:G33 «flujo del año 3
    mantenido» y que B54 «DSCR mínimo» siga midiendo todo el cuadro pero la nota lo declare.
A3. **IVA repercutido POR LÍNEA DE VENTA** (REF-04 panadería: pan común al 4 %, art. 91.Dos.1.1.º LIVA; sin mover la rejilla de Supuestos).
    Cada línea de ingreso del P&L lleva en la columna G su tipo de IVA repercutido (igual que las líneas de coste llevan el soportado):
    por defecto, líneas de comida → fórmula `='0. Supuestos'!$B$39`; líneas de bebida → la mezcla RD-17 actual
    `alc×((1−deliv)×B63+deliv×B40)+(1−alc)×B39` como fórmula. El contrato LINEAS_INGRESO admite un campo opcional `iva` (número o fórmula)
    que sustituye el defecto: la celda se pinta VERDE con nota si es literal. Los tres consumidores —'6. Tesorería'!B9:M9 (cobros con IVA),
    B16:M16 (IVA repercutido) y '0. Supuestos'!B9 (PVP equivalente)— pasan a usar `SUMPRODUCT(pesos_E, tipos_G)` de las líneas de ingreso en
    lugar de `pct_comida×B39 + pct_bebida×blend`. Para el bar los VALORES deben quedar idénticos (verificar 0 diferencias de valor por
    esta causa). C9: «Ticket sin IVA más el IVA medio ponderado de tus líneas de venta: X % (en sala todo va al 10 %; el alcohol por delivery
    y el pan común, si los tienes, mueven la media; aquí va redondeado)». Instrucciones línea 4: divisores 1,04 / 1,10 / 1,21 por tipo.
    Panadería (contenido, con fuente en su propio docx/a.py): separar o tipar la línea de pan común al 4 % y bollería/cafetería al 10 %; si el
    docx no da el reparto, la línea «pan, bollería…» lleva `iva` = fórmula ponderada con una celda verde «Pan común sobre la línea (%)» en
    la propia fila (columna H) y nota con la fuente.
A4. **Cobertura de horas sobreescribible** (M-02, REF-06, MOT-03): clave opcional de contenido `COBERTURA = {'horas_dia', 'personas_franja',
    'horas_produccion', 'personas_produccion', 'nota_horas', 'nota_personas'}` (defectos 13, 2, 0, 0 y las notas actuales). Horas necesarias
    = horas_dia×personas_franja×días + horas_produccion×personas_produccion×días. Aplicar: tapas-bar 9,5 h × 2 (su docx: 12-16 h y
    19-00:30 h); panadería tienda 13 h × 1,7 + obrador 3,5 h × 1 (J5 e Instrucciones: producción 4:00-5:00); food-truck 12 h × 1 (docx:
    «diez y doce horas de jornada efectiva»). Notas sin «barra/cocina y sala» cuando el molde no los tenga.
A5. **Techo de rotación y frase de referencia sobreescribibles** (REF-01 panadería, M-07 food-truck, MOT-02 tapas-bar): clave opcional
    `ROTACION = {'activa': bool, 'max': float, 'nota_max': str, 'referencia': str}`. `activa=False` suprime el bloque ('Punto Equilibrio'
    A25:E26 y '0. Supuestos' A50:C50 quedan vacíos, sin CF colgando) — panadería y food-truck lo apagan (el driver es la transacción de
    mostrador, no el cubierto sentado; el propio libro lo dice en C51). `referencia` sustituye el texto fijo de C50 («El documento de este
    plan pide un MÍNIMO de 1,8…»): tapas-bar pone la suya («1,8 servicios por cubierto en almuerzo y 1,5 en cena, párrafo 27 del docx»).
    Verificación: 0 celdas rojas en PE!B26:D26 de panadería y food-truck.
A6. **Rótulos de filas canónicas y de ratios** (M-05, M-09): `INVERSION`/`FIJOS` admiten tupla de 3 `(importe|None, nota, rotulo_nuevo)`
    conservando la posición; `ratio()` toma el rótulo de la tupla de UMBRALES cuando venga. Food-truck: «Aparcamiento y base del vehículo»
    y «Aparcamiento / Ventas».
A7. **IVA soportado de la inversión** (REF-14): el SUMIF de 'Inversión Inicial' cubre EXACTAMENTE el mismo rango que el SUM del subtotal
    (última fila real del bloque, incluida la fila calculada de imprevistos). Gate propio: rango SUMIF == rango SUM.
A8. **Imprevistos y base de obra** (REF-06, REF-19): la base de los imprevistos son las partidas clasificadas como 'obra' por AMORT_DEFECTO
    (proyecto técnico, obra civil, eléctrica, fontanería, extracciones, decoración, rotulación), no el bloque entero; la nota lo dice tal
    cual. Los imprevistos de obra CAPITALIZAN (entran en la base 'obra' de la amortización). La enumeración de D37 («no amortizable: …») se
    genera desde las filas que realmente quedan fuera.

## B. Arreglos de CALIDAD (no cambian el caso base o lo cambian sólo en texto/formato)

B1. Guardas de libro vacío (R-08, REF-15): '0. Supuestos'!B12 = IF(COUNT(B11)=0,"",1-B11); mismo patrón en 'PyG'!E11, Personal!B22 y
    Financiación!B23. Y la demo 13 marca también «100,0 %» y notas TEXT() que imprimen número sin input.
B2. Personal!A2 por fórmula (R-11, REF-16): ="Convenio Hostelería — "&TEXT(B21,"0")&" pagas + SS "&TEXT(B20*100,"0")&" %" (sin "0,0%"
    dependiente de locale).
B3. 'Escenarios' fila 25 (R-13): NO cambiar el método; rotular «Saldo de caja al cierre del año 1 (realista: tesorería mensual;
    pesimista y optimista: estimado)» y nota.
B4. Celdas de TEXTO con formato numérico (R-15, R-19): al cerrar cada libro, toda celda cuyo valor sea str pasa a number_format 'General'
    (todas las hojas). Extender gate_formatos para detectarlo.
B5. Validación «Sí,No» sólo sobre filas editables (R-18): recortar la sqref a las filas desbloqueadas.
B6. TILDES (M-01, R-10, REF-21): añadir vehículo, móvil, máquina, práctica, física, menú, categoría, tráfico, urbanístico, rótulo,
    fórmula, número, único, público, básico, económico, técnico, análisis, más… (revisar que no rompa homógrafos: solo pares seguros).
    Falso positivo MOT-04: «cuanto/Cuánto» son ambas válidas: excluir ese par de la heurística de convivencia.
B7. «CRECIMIENTO DE LA PLANTILLA (coste escalonado, RD-10)» (M-04, REF-02-motor, MOT-01, NUEVO-CAF-01): quitar «, RD-10».
B8. «Renta de los 1 meses» (PLURAL-01, NUEVO-CAF-02, REF-23): IF(B54=1,"Renta del mes de obra y licencias…","Renta de los N meses…").
B9. Liquidación trimestral (REF-09): sin rojo en negativo (es «a compensar»); rojo sólo si el pago del 303 supera el saldo del mes.
B10. Guarda del cross-sell (R-05, CROSS-SELL-01): `cross_sell_sin_precios()` sólo actúa sobre líneas de catálogo REALES (celda que
    empieza por Kit/Guía/Pack/eBook/Plan o contiene aichef.pro/productos); el informe lista cada celda modificada.
B11. RX_EURO_FUERTE (M-06): conocer «ventas», «derechos», «eventos», «día» en rótulos de euros.
B12. 'Punto Equilibrio'!A33 (R-23): rotular la tabla «Cubiertos/día necesarios: ticket (columnas) × coste variable por cubierto (filas)».
B13. Tesorería fila de compras (R-24): nota O11 «Con 30 días de pago, la compra de diciembre se paga en enero: la columna Año recoge 11
     mensualidades».
B14. Doble guarda IF(B9="","",IF(B9="","",… (REF-22, REF-18): no volver a envolver una fórmula que ya lleva la guarda.
B15. DEMO-2119 (panadería): la demostración §2.11.9 mira el primer año CON devolución de principal (carencia + 1), no siempre B47.

## C. Verificación exigida (la hace el implementador y la repite el orquestador)
- Dry-run de los CINCO (bar + 4 hermanos) EN SERIE con cerrojo y `istats`: exit 0, «gates medibles a 0: 13/13», idempotencia 0,
  blancos_contaminados 0; food-truck debe llegar a 13/13 (B6).
- Bar: diff celda a celda contra el LIVE (`$S/rd17/diff_live_dry.py <carpeta>`): TODA celda cambiada atribuida a un ítem A/B de esta lista
  (A3 debe dejar los valores de cobros/IVA/PVP IDÉNTICOS; A1/A2/A7/A8 cambian valores: anotar antes/después).
- Panadería: N16 < 30.690 € por A3; PE!B26:D26 sin rojo por A5; Personal!B24 ≥ 1 por A4. Food-truck: cobertura ≥ 98 % por A4.
- Informe JSON con: ítems hechos (con línea de código), ítems no hechos (motivo), celdas cambiadas del bar por ítem, cifras nuevas de los 5
  (payback, DSCR mínimo, saldo mínimo, IVA repercutido año 1, necesidad de caja).
