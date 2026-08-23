# Kit Control de Inventario y Compras — v2.0 (SPEC, 2026-08-23)

Origen: ronda 1 adversarial (`auditorias/kit-inventario-R1.json`, 3 lentes opus — economato, técnica Excel, coherencia
comercial; **91 hallazgos**, «no listo» ×3). Lo que sigue es lo que SE HACE; lo demás se descarta en §6 o se pregunta en
§7; la evidencia de cada hallazgo está en el R1, citada aquí por id. Método y código de referencia:
`kit-escandallos-v2-SPEC.md` y su paquete (motor + grupos, `main.py --dry-run / --solo`, respaldo, `inject_cache.py` al
final, verificación `data_only`, idempotencia por reconstrucción). Paquete nuevo
`scripts/productos-digitales/kit-inventario-v2_0/` (`motor.py`, `grupo_a.py`, `grupo_b.py`, `grupo_c.py`, `main.py`);
ejecución real solo con `KIT_INVENTARIO_APPLY=1`.

Ficheros: `astro-site/public/dl/kit-inventario/` — **los mismos 9 xlsx con los mismos nombres**: las 9 claves de descarga
(`get-download-urls.ts:245-255`) viajan en emails ya enviados. Se añaden hojas, columnas y filas; no se quita ningún
entregable. Convenciones: celdas editables **verdes `E8F5E9`**, calculadas sin relleno; parámetros en celdas, nunca
literales en la fórmula; `IFERROR`/doble guarda en toda división y todo producto; semáforo por formato condicional (verde
`C6EFCE`, ámbar `FFEB9C`, rojo `FFC7CE`); DV con `showErrorMessage=True`. **pycel no implementa `COUNTA` ni `MODE`**
(medido el 2026-08-23: `UnknownFunction`); sí `SUMIF/SUMIFS/COUNTIF/COUNTIFS/LARGE/INDEX/MATCH/VLOOKUP/IFERROR/SUMPRODUCT/TODAY` → `COUNTIF(rango,"<>")` por `COUNTA` e `INDEX/MATCH` sobre una columna de `COUNTIF` por `MODE`. Nada de
builds locales ni Playwright; python en serie; `istats` entre barridos.

## 1. Motor común (`motor.py`) — los 9 ficheros

1.1 **Taxonomía y unidades únicas** (DOM-22/TEC-10/COM-19/DOM-02/TEC-01, altas): las 10 categorías de `07!'Coste por
Categoría'!A4:A13` (Cárnicos, Pescados, Lácteos, Verduras/Frutas, Secos/Granos, Congelados, Bebidas Alcohólicas, Bebidas
No Alcohólicas, Limpieza —incluye menaje y desechables—, Otros) y las unidades `kg, L, ud, docena, caja, bandeja, barril,
saco, rollo, paquete`, con DV **inline** (caben en los 255 caracteres de Excel) en `01!C/D`, `03!C/D`, `05!'Registro Diario Mermas'!C/E`, `06!'Control FIFO'!C`, `07!'Top 20'!C` y `BONUS-08!C/D`.
1.2 **Formato condicional real** (TEC-22/DOM-34, alta): `semaforo(ws, rango, vocabulario)` con `containsText` en `01!H`,
`04!M`, `05!'Dashboard Mermas'!D`, `06!L` y `07!'Dashboard KPIs'!E`; regla `expression` en `04!K` (temperatura) y
`07!'Top 20'!J` (variación > 5 %). Hoy hay 0 reglas en las 30 hojas: el «semáforo» es el emoji dentro del texto.
1.3 **IVA por categoría** (DOM-07/TEC-13/COM-16): 4 % Lácteos y Verduras/Frutas · 10 % Cárnicos, Pescados, Secos/Granos,
Congelados y Bebidas No Alcohólicas · 21 % Bebidas Alcohólicas, Limpieza y Otros; en `03!Listas`, nunca literal, con nota
«orientativo, edítalo: pan, harinas, legumbres y cereales al 4 %; refrescos azucarados, al 21 %».
1.4 **Ejemplos sembrados** (COM-27/DOM-34, alta): las **12 hojas esqueleto** dejan de estar en blanco (3-8 filas realistas
marcadas «(ejemplo)»): `02!Directorio Proveedores` y `!Condiciones Comerciales`, `03!Historial Pedidos`, `04!Control
Recepción` y `!Registro Incidencias`, `05!Plan de Acción`, `06!Mapa Almacén`, `07!Top 20 Productos`.
1.5 **Protección sin contraseña** (DOM-34): `ws.protection.sheet = True`, verdes con `Protection(locked=False)` y línea
«Revisar → Desproteger hoja (no tiene contraseña)».
1.6 **Toda pestaña citada existe** (DOM-08/TEC-05/COM-05, altas). SE CREAN por ser registros simples: `03!Proveedores` y
`07!Evolución Mensual`. NO se crean y se RETIRA la promesa: `03!Imprimible` (no es un registro: `Pedido Actual` ya lleva
`print_area` y `print_title_rows`) y `BONUS-09!Simulador` (exige diseño de escenarios) — fuera de `03!Instrucciones!A9`,
`BONUS-09!Instrucciones!A11` y `grid.templates[8].desc`. Se corrigen los nombres que no casan con `wb.sheetnames`
(`01!A20`, `02!A7/A9`, `03!A8`); gate en `main.py`: toda pestaña entrecomillada en Instrucciones tiene que existir.
1.7 **Formatos** (TEC-18/DOM-34): `#,##0.00 €` en toda columna de importe, también de entrada (`03!E9`, `05!F4`,
`07!B4:M13`, `02!D4:I13`, `BONUS-08!E5`); `dd/mm/yyyy` en fechas (`04!A`, `05!A`, `06!E/G/H`); `0` explícito en `06!K` para
que Excel no le propague formato de fecha; `0,0 %` en porcentajes.
1.8 **Doble guarda** (TEC-06): las guardas vigilan la cantidad e ignoran el precio, así que una línea sin precio vale
0,00 € y se suma como si fuera gratis → `=IF($D4="","",IF($F4="","⚠ falta coste",$D4*$F4))` en `03!G`, `05!G`, `BONUS-08!G`.
1.9 **Filas libres** (TEC-23): `01!Cocina` 5-44, `Barra`/`Almacén` 5-34; `03` 9-38; `04` 4-43; `05` 4-103; `06` se queda en
5-54; `BONUS-08` 5-84. Fórmula, DV y verde replicados; el TOTAL baja dos filas y su `SUM` cubre el rango completo.
1.10 **Instrucciones, bio y versión**: reescritas para describir lo que hay. Bio anclada (hoy no la lleva ninguno de los
9): «Diseñado por John Guerrero — chef y consultor gastronómico desde 2010, en cocina desde los 17 años ·
johnguerrero.es»; «Versión 2.0 · agosto 2026 · aichef.pro/kit-inventario · info@aichef.pro»; metadata `subject` →
`… · v2.0` (resto según `postprocess-transversal.py`).

## 2. Grupo A — inventario y proveedores (01, 02, BONUS-08) — `grupo_a.py`

- **01, las 50 filas precargadas** (DOM-01/DOM-02/DOM-14, TEC-01/TEC-25, COM-02/COM-31, altas): se reescriben `Cocina!B5:F24`,
  `Barra!B5:F19` y `Almacén!B5:F19` con categoría, unidad, **precio de referencia** (HORECA, orientativo, sin fecha en el
  texto) y par level / par max **por producto** — hoy categoría y unidad se asignan por rotación cíclica y los 50 par
  levels son 5/15. Carnes y pescados en kg (pollo 6,50 par 8/20 · solomillo 32,00 par 3/8 · salmón 14,00 · gambas 18,00),
  hortalizas y fruta en kg salvo lechuga en ud, aceites y vinagres en L, secos en kg, huevos en **docena**, lácteos en L o
  kg, cerveza de grifo en **barril de 30 L** (55,00 par 2/6), vinos en **ud (botella 75 cl)** —no «copa»—, refrescos, agua
  y tónica en ud, hielo en saco, consumibles y químicos en rollo/caja/L, y **«Coca-Cola» → «Refresco de cola»** (COM-31).
  Nota en la fila 3: «Datos de ejemplo; precios orientativos, edítalos».
- **01, valoración y resumen** (DOM-09/TEC-03/COM-14, altas; DOM-33/TEC-21): columna nueva **J «Precio/ud (€)» verde**
  (Valor→K, Proveedor→L, Notas→M) con `K5='=IFERROR(IF(OR($G5="",$J5=""),"",$G5*$J5),"")'`, y `A Pedir` arrancando ya en
  ámbar: `I5='=IF($G5="","",IF($G5<$E5*1.5,MAX(0,$F5-$G5),0))'`. `Resumen Dashboard`: `A4:A6` = Cocina/Barra/Almacén con
  `B4='=COUNTIF(Cocina!$H$5:$H$44,"*BAJO*")'`, `C4='=COUNTIF(…,"*PEDIR*")'` y `D4='=SUM(Cocina!$K$5:$K$44)'` (Barra y
  Almacén sobre `5:34`), fila 7 TOTAL, y bloque `A9:C20` por categoría con
  `B10='=SUMIF(Cocina!$C$5:$C$44,$A10,Cocina!$K$5:$K$44)+SUMIF(Barra!…)+SUMIF(Almacén!…)'`, `C10='=IFERROR($B10/$B$20,"")'`
  y `B20` = VALOR TOTAL DEL STOCK.
- **02 fichas de proveedor** (DOM-15/DOM-16/DOM-17, TEC-07/TEC-16, COM-18/COM-29): `Directorio Proveedores!A3:S3` gana CIF/NIF, Nº RGSEAA,
  contacto de incidencias, día de pedido, día de reparto, plazo de entrega, condiciones de pago, Homologado (S/N), fecha de
  homologación y de última revisión, con **una fila de ejemplo por tipo** (carnes, pescados, frutas y verduras, secos,
  bebidas, limpieza). `Comparativa Precios` gana formato de venta, contenido (kg/L/ud), fecha de cotización y vigencia +
  bloque oculto `P4:T13` de precio normalizado `=IFERROR(F4/$E4,"")` sobre el que corren
  `K4='=IF(COUNT($P4:$T4)=0,"",MIN($P4:$T4))'`, `L4='=IFERROR(INDEX($F$3:$J$3,MATCH($K4,$P4:$T4,0)),"")'` y
  `M4='=IFERROR((MAX($P4:$T4)-$K4)/$K4,"")'`; `F3:J3` traen el nombre del directorio, no «Prov. 1…5». `Evaluación
  Proveedores`: `H3`→«PUNTUACIÓN MEDIA (1-5)», `H4='=IF(COUNT($C4:$G4)<3,"",AVERAGE($C4:$G4))'` e `I4` con la nota
  A/B/C/D; `Instrucciones!A9` con los cinco criterios reales.
- **BONUS-08** (DOM-32/TEC-24/COM-28): columnas `Compras del mes`, `Consumo ='=IF(OR($F5="",$H5=""),"",$H5+$I5-$F5)'`,
  `Variación (ud) ='=IF(OR($F5="",$H5=""),"",$F5-$H5)'` y `% Variación ='=IF(OR($H5="",$H5=0),"",$F5/$H5-1)'`; `G5` con
  doble guarda (§1.8).

## 3. Grupo B — compras, recepción y mermas (03, 04, 05) — `grupo_b.py`

- **03 pedidos** (DOM-07/DOM-18/DOM-19, TEC-13/TEC-19/TEC-20, COM-16/COM-17/COM-30): cabecera `# · Producto · Categoría (DV) · Unidad · Cantidad ·
  Precio/ud (€) · Subtotal (€) · IVA % · Total (€)`, con `H9='=IF($B9="","",IFERROR(VLOOKUP($C9,Listas!$A$2:$B$11,2,FALSE),10))'` y **DV `4,10,21` encima** para sobrescribirlo, e `I9='=IF(OR($E9="",$F9=""),"",$E9*$F9*(1+$H9/100))'`.
  Totales bajo la columna «Total»: `H40` BASE `=SUM($G$9:$G$38)`, `H41` CUOTA `=SUM($I$9:$I$38)-$H$40`, `H42` TOTAL; y
  desglose por tipo en `A45:D48` (`B46='=SUMIF($H$9:$H$38,$A46,$G$9:$G$38)'`, `C46='=IFERROR($B46*$A46/100,"")'`,
  `D46='=$B46+$C46'`). Etiquetas `A3:A6` combinadas `A:B` con el dato en `C` (la columna A mide 5 y hoy imprime «Prove»),
  bloque emisor verde en `F3:G6` (establecimiento, CIF, dirección de entrega, contacto), `freeze_panes='A9'` y
  `print_title_rows='$8:$8'`. Hojas nuevas `Proveedores` (20 filas, 6 de ejemplo; alimenta la DV de `C3` y el `VLOOKUP` que
  trae teléfono y pedido mínimo) y `Listas` (categoría→IVA). `Historial Pedidos` pasa a 40 filas con la primera enlazada al
  pedido en curso (`E4` = `='Pedido Actual'!$H$40`, `F4` = `=…$H$41`, `G4` = `=…$H$42`), DV de Estado y nota de flujo.
- **04 recepción** (DOM-03/DOM-04/DOM-05/DOM-20/DOM-21, TEC-04/TEC-17, COM-04/COM-06/COM-08; cuatro altas): es el único libro con **0 fórmulas** y sus
  `Instrucciones!A9` afirman que las temperaturas fuera de rango se marcan solas en rojo. `Verificación Temperaturas!A3:D16`
  pasa a tabla NUMÉRICA (`Familia · Tª ideal · Tª máx. aceptable (°C) · Base normativa`) desdoblada: canal y despiece de
  ungulados ≤ 7 · despojos ≤ 3 · aves y lagomorfos ≤ 4 · preparados de carne ≤ 4 · carne picada ≤ 2 (Reg. (CE) 853/2004,
  Anexo III, Secc. I/II/V) · pescado fresco 0-2 °C en hielo fundente (Secc. VIII) · congelados ≤ −18 (tolerancia breve −15
  en transporte) · comidas preparadas refrigeradas ≤ 4 °C, u ≤ 8 °C si duran menos de 24 h (RD 3484/2000, art. 6) · lácteos
  y refrigerados ≤ 8 °C o lo que indique la etiqueta · frutas y verduras ≤ 12 · huevos «temperatura ambiente constante, sin
  cambios bruscos; no refrigerar antes de la venta» → `N/A` (Reg. (CE) 589/2008). `Control Recepción` gana `Nº albarán/factura`, `Nº de lote`, `Familia` (DV contra `'Verificación Temperaturas'!$A$4:$A$16`), `Diferencia`, `Receptor` y
  `Firma`, y tres columnas calculadas: `I4='=IF(OR($G4="",$H4=""),"",$H4-$G4)'`,
  `L4='=IF($E4="","",IFERROR(VLOOKUP($E4,'Verificación Temperaturas'!$A$4:$C$16,3,FALSE),""))'` y
  `M4='=IF(OR($K4="",$E4=""),"",IF($L4="N/A","N/A",IF($K4<=$L4,"✓ CONFORME","✗ RECHAZAR")))'`, con CF rojo sobre `K4:K43`
  (`=AND($K4<>"",$M4="✗ RECHAZAR")`) y sobre `M`. `Registro Incidencias` gana `Nº albarán`, `Importe reclamado (€)`,
  `Abono recibido (€)`, DV de estado, 3 filas de ejemplo y fila de totales.
- **05 mermas** (DOM-11/DOM-23, TEC-09, COM-10/COM-12; altas): `Análisis por Categoría!A4:A13` pasa a las 10 canónicas con
  `B4='=COUNTIF('Registro Diario Mermas'!$C$4:$C$103,$A4)'`, `C4='=SUMIF('Registro Diario Mermas'!$C$4:$C$103,$A4,'Registro Diario Mermas'!$G$4:$G$103)'`, `D4='=IFERROR($C4/$C$14,"")'`, columna verde «Coste mes anterior (€)» y
  `Tendencia`, más bloque auxiliar `H4:I10` de `COUNTIF` por motivo (pycel no soporta `MODE`). `Dashboard Mermas`:
  `B4` = `='Registro Diario Mermas'!$G$105`, celda verde **`B10` «Compras del mes (€, sin IVA)»** —sin ella el «< 3 % sobre
  compras» que el propio kit fija como objetivo es incalculable—, `B5='=IFERROR($B$4/$B$10,"")'`,
  `B6='=COUNTIF('Registro Diario Mermas'!$B$4:$B$103,"<>")'`, `B7` y `B8` con INDEX/MATCH sobre el máximo del análisis y
  sobre el bloque de motivos, y `C4` pasa del absoluto «< 500 €» a `=IFERROR($B$10*0.03,"")`. `Plan de Acción` deja de ser
  un título suelto: `Prioridad · Categoría · Problema detectado · Causa raíz · Acción correctora · Responsable · Fecha
  límite · Coste mensual evitado (€) · Estado y seguimiento`, DV en Prioridad y Estado, **5 filas precargadas**
  (sobreproducción, etiquetado FIFO, rotura en cámara, corte con merma excesiva, pedido por encima del consumo) y total.

## 4. Grupo C — caducidades, costes y punto de pedido (06, 07, BONUS-09) — `grupo_c.py`

- **06 FIFO** (DOM-13/DOM-24/DOM-25/DOM-26/DOM-27/DOM-28, TEC-11/TEC-12, COM-09/COM-15/COM-26; dos altas): `Control FIFO!A4:T4` gana `Tipo de fecha` (DV
  {Caducidad, Consumo preferente}), `Fecha de apertura`, `Vida útil tras abrir (días)`, `Fecha límite efectiva`, `Días en
  almacén`, `Cantidad`, `Unidad`, `Precio/ud (€)` y `Valor en riesgo (€)`, con
  `J5='=IF($H5="",$G5,IF($I5="",$G5,MIN($G5,$H5+$I5)))'`, `K5='=IF($J5="","",$J5-TODAY())'`,
  `M5='=IF($E5="","",TODAY()-$E5)'` (da uso a «Fecha Entrada», hoy ausente de las 100 fórmulas),
  `Q5='=IF(OR($N5="",$P5=""),"",$N5*$P5)'` y **semáforo de cuatro estados** `L5='=IF($K5="","",IF($K5<0,IF($F5="Consumo preferente","⚠ REVISAR (consumo preferente)","⛔ CADUCADO — RETIRAR"),IF($K5<=2,"🔴 URGENTE",IF($K5<=7,"🟡 PRÓXIMO","🟢 OK"))))'`. `Alertas Caducidad` deja de ser una instrucción de trabajo manual: autofiltro en `A4:T54` + contadores por
  estado (`COUNTIF`) con su valor en riesgo (`SUMIF`) y protocolo en cuatro líneas — **caducado = retirada obligatoria y
  registro de merma, nunca uso**; urgente = servicio de hoy; próximo = priorizar; consumo preferente vencido = revisión
  organoléptica. `Mapa Almacén!A4:E12` se precarga con 9 zonas separando crudo de elaborados (crudos 0-4 · pescado 0-2 en
  hielo · elaborados y lácteos 0-4 · verduras 4-8 · congelador ≤ −18 · descongelación identificada 0-4 · economato seco
  «lugar fresco y seco, < 25 °C, HR < 60 %, a ≥ 10 cm del suelo y separado de la pared» · bodega 12-16 · residuos) y
  alimenta la DV de `Zona`. Instrucciones: el criterio operativo es **FEFO**; FIFO es el de colocación.
- **07 costes** (DOM-10/DOM-29/DOM-30/DOM-31, TEC-08, COM-11/COM-23; dos altas): `Coste por Categoría` → `O4='=IFERROR($N4/$N$14,"")'` y
  cabeceras «(€, sin IVA)». Hoja nueva **`Evolución Mensual`**: 12 filas con `B` = `='Coste por Categoría'!B$14`, `C` =
  variación mes a mes y `D` = acumulado. `Top 20 Productos` gana `Precio anterior (€)` y `Precio actual (€)`,
  `F='=IF($E4="","",$E4*12)'`, `G='=IFERROR($E4/$E$24,"")'`, `J='=IF(OR($H4="",$I4=""),"",$I4/$H4-1)'` con CF > 5 %, 8 filas
  de ejemplo y bloque «Top 5 por gasto» en `L4:M8` con `L4='=IFERROR(INDEX($B$4:$B$23,MATCH(LARGE($E$4:$E$23,1),$E$4:$E$23,0)),"")'` (el `k` va literal por fila). `Dashboard KPIs`: **entradas verdes** `B12:B17` (ventas del periodo sin
  IVA, cubiertos servidos, existencias inicial y final, compras del periodo anterior, ticket medio) y KPIs reales:
  `B6` = `='Coste por Categoría'!$N$14`, `B4='=IFERROR(($B$14+$B$6-$B$15)/$B$12,"")'` (food cost sobre **consumo**, no sobre
  compras), `B5='=IFERROR(($B$14+$B$6-$B$15-'Coste por Categoría'!$N$12-'Coste por Categoría'!$N$13)/$B$13,"")'` (el
  coste por cubierto excluye Limpieza y Otros), `B7='=IFERROR($B$6/$B$16-1,"")'`, `B9` con INDEX/MATCH sobre la variación
  del Top 20 y `C5='=IFERROR($B$17*0.30,"")'` en vez del absoluto «< 4,50 €», que solo vale para un ticket de 15 €.
  Instrucciones: «todos los importes van SIN IVA (base imponible)».
- **BONUS-09 punto de pedido** (DOM-06/DOM-12, TEC-02/TEC-14/TEC-15, COM-01; tres altas): `Parámetros` gana celdas verdes numéricas `D4`
  (coste de pedido, 3 €) y `D5` (% de almacenamiento anual, 0,25) — hoy el `2` y el `0.5` van hardcodeados en las 30
  fórmulas. `Calculadora!A3:N3` pasa a `# · Producto · Categoría · Consumo diario · Lead time (días) · Cobertura de
  seguridad (días) · Stock de seguridad (ud) · Punto de pedido · Precio/ud (€) · Vida útil (días) · EOQ teórica · Cantidad
  a pedir sugerida · Frecuencia de pedido (días) · Proveedor`, con `G4='=IF(OR($D4="",$F4=""),"",$D4*$F4)'` y
  `H4='=IF(OR($D4="",$E4=""),"",$D4*$E4+$G4)'`: el stock de seguridad queda **en unidades con la ayuda «días × consumo
  diario»** y `Parámetros!A10` describe ya la columna F. EOQ parametrizada y **capada dos veces**:
  `K4='=IF(OR($D4="",$D4<=0,$I4=""),"",ROUND(SQRT(2*$D4*365*Parámetros!$D$4/($I4*Parámetros!$D$5)),0))'`,
  `L4='=IF($K4="","",MIN($K4,ROUND($D4*$J4*0.7,0)))'` y `M4='=IF(OR($D4="",$D4<=0,$L4=""),"",ROUND($L4/$D4,0))'`. 8 filas de
  ejemplo coherentes con el 01; el «Simulador» se retira (§1.6).

## 5. Integración — landing, dashboard, changelog, emails, gates (`integracion`, sonnet)

- **Interconexión** (COM-03, alta): son 9 ficheros separados y las referencias externas se rompen al descargar. Se reescriben
  las cinco afirmaciones — `kit-inventario.ts:114` (`hero.checkItems[2]`), `:137` (`grid.templates[2].desc`), `:73`
  (`schema.faqs[1].a`, indexable), `:221` (`faqs[1].a`), `:248` (`cta.items[2]`) y `KitInventarioDashboard.tsx:17` — a
  «**coherentes entre sí: mismas categorías, unidades y familias en las 9 plantillas**; la columna “A Pedir” te dice cuánto
  reponer y el desplegable de proveedores sale de tu propio directorio».
- **APPCC** (COM-07, alta): `schema.faqs[2].a:77` y `faqs[2].a:225` pasan del «Sí» taxativo a «te ayudan a **documentar los
  registros de recepción y trazabilidad que pide tu plan APPCC; no sustituyen al plan ni a un asesor**», con enlace a
  `/pack-appcc`; mismo matiz en `why.reasons[2].desc:156`.
- Resto: `seo.description:30`, `schema.productDescription:39` y `hero.description:110` («9 plantillas con fórmulas
  automáticas») quedan **ciertos** al dotar de fórmulas al 04 (COM-06); `why.reasons[0].desc:154`, `faqs[0].a:217` y
  `schema.faqs[0].a:69` enumeran las **10** categorías canónicas (hoy 8, COM-19); `grid.templates[2].desc` sin «formato
  imprimible» como pestaña; `:140` «rotación FIFO/FEFO»; `:143` sin «Simulador»; `why.reasons[3]:157` unifica con
  `faqs[3].a:229` en **50-100 EUR/mes** y cambia «las mismas funciones que los SaaS» por una afirmación de suficiencia
  (COM-22, §7.6). Dashboard `KitInventarioDashboard.tsx:15-23` y gemelos de la SPA en `src/components/kit-inventario/*`:
  los mismos cambios.
- Changelog `productos-changelog.ts:265-280`: `version`/`updated` → **2.0** (2026-08-23); la entrada 1.1 se retitula
  «Mejoras de formato e impresión (A4) en los 9 ficheros» (COM-24) y se añade la 2.0 en lenguaje de cliente;
  `kit-inventario.ts:295` `updateNote` → «Producto actualizado · Versión 2.0 · agosto 2026».
- **Emails y claves: no se tocan** — `verify-purchase.ts:133-139` y `resend-access.ts:133-139` («9 plantillas de control de
  inventario») siguen siendo ciertos y `get-download-urls.ts:245-255` queda intacto.
- Gates: `censo-entregables.py --only kit-inventario --fail --quiet` (0 defectos), `gate-flujo-postpago.py --offline --only
  kit-inventario` (9/9), `inject_cache.py` al final, verificación `data_only`, idempotencia (segunda pasada = 0 cambios) y
  pycel cambiando inputs: toda fórmula de estado debe cambiar con un dato fuera de límite.

## 6. Descartado con motivo

- **COM-13** (`aggregateRating` 4,9/8, `schema.reviews`, 8 testimonios): aparcado por John (2026-08-22). La v2.0 vuelve
  ciertos los dos testimonios que hoy describen funciones inexistentes (punto de pedido y alertas de temperatura).
- **COM-20** (bonos «valorados en 18 EUR» frente a «valor total 49 EUR / ahorra 35») y **COM-21** (`priceOld`,
  `discountBadge`, «Sube pronto» frente a `priceValidUntil`): tocan el **ancla de precio**, aparcada por John. COM-20 se
  cerraría quitando «— valorados en 18 EUR» de `bonus.subtitle:177`, sin tocar el ancla.
- **TEC-23 como `ListObject`**: no; rangos ampliados con fórmula, DV y verde replicados (§1.9). **DOM-08/COM-05 en su
  versión «crear las tres pestañas»**: solo las dos que son registros simples (§1.6). **Enlaces externos entre libros**
  (lectura literal de COM-03): no; un `.xlsx` movido de carpeta rompe la referencia y el cliente ve `#REF!`.

## 7. Dudas para el orquestador

7.1 **Top 20 del 07:** ¿hoja «Registro de Compras» línea a línea sobre la que corra el `LARGE/INDEX/MATCH`, o el propio
`Top 20` como tabla de entrada con el ranking ordenando sobre ella? *Recomiendo lo segundo*: evita una hoja más.
7.2 **Hoja `Proveedores` del 03:** ¿visible (20 filas, con teléfono y pedido mínimo) o rango oculto solo para la DV?
*Recomiendo visible*: es lo que hace útil el desplegable y el `VLOOKUP` de la cabecera del pedido.
7.3 **Taxonomía canónica:** ¿confirmas las **10** de 07 y reescribir la enumeración de 8 de la landing? *Recomiendo sí*:
separar bebidas alcohólicas de no alcohólicas es lo que permite el IVA por defecto del 03.
7.4 **«Simulador» del BONUS-09:** ¿retiramos la promesa o construimos un bloque de tres escenarios? *Recomiendo retirarla*:
con `Parámetros` ya editable, probar escenarios es cambiar dos celdas.
7.5 **Licencia (COM-25):** `faqs[4].a` dice «licencia personal» y a la vez «ideal para consultores», y ningún xlsx lleva
cláusula de uso. ¿Añadimos la línea al pie de las 9 Instrucciones y reescribimos la FAQ abriendo la licencia profesional
(`info@aichef.pro`)? *Recomiendo sí*: hoy se está regalando la reventa.
7.6 **Cifras sin fuente (COM-32 y COM-22):** ni el badge del hero («3.000-5.000 EUR/año en mermas evitables») ni el coste del
software citan ninguna. ¿Aportas la fuente o reformulamos? *Recomiendo* unificar en «50-100 EUR/mes» y dejar el badge como
dato propio («en los establecimientos que hemos auditado»).

## 8. Mapa id → sección (91/91)

| id | dónde | qué |
|---|---|---|
| DOM-01 | §2 (01 filas) | categorías reales por producto |
| DOM-02 | §2 (01 filas) | unidades reales de compra |
| DOM-03 | §3 (04) | Instrucciones A9 pasa a ser cierta |
| DOM-04 | §3 (04) | lote y albarán en recepción |
| DOM-05 | §3 (04) | umbrales legales por familia |
| DOM-06 | §4 (BONUS-09) | EOQ capada por vida útil |
| DOM-07 | §3 (03) | IVA por línea con DV |
| DOM-08 | §1.7 | 2 pestañas se crean, 2 promesas se retiran |
| DOM-09 | §2 (01 valoración) | precio/ud, valor y resumen |
| DOM-10 | §4 (07) | entradas de ventas y cubiertos |
| DOM-11 | §3 (05) | SUMIF en análisis y dashboard |
| DOM-12 | §4 (BONUS-09) | seguridad en unidades desde días |
| DOM-13 | §4 (06) | cuarto estado CADUCADO |
| DOM-14 | §2 (01 filas) | par levels por producto |
| DOM-15 | §2 (02) | INDEX/MATCH del mejor proveedor |
| DOM-16 | §2 (02) | formato, contenido y fecha de cotización |
| DOM-17 | §2 (02) | CIF, RGSEAA y homologación |
| DOM-18 | §3 (03) | historial real y cuota de IVA |
| DOM-19 | §3 (03) | hoja Proveedores + bloque emisor |
| DOM-20 | §3 (04) | diferencia pedido vs recibido |
| DOM-21 | §3 (04) | familia + VLOOKUP de umbral |
| DOM-22 | §1.1 | taxonomía única |
| DOM-23 | §3 (05) | celda de compras del mes |
| DOM-24 | §4 (06) | FEFO explicado y días en almacén |
| DOM-25 | §4 (06) | cantidad y valor en riesgo |
| DOM-26 | §4 (06) | tipo de fecha con DV |
| DOM-27 | §4 (06) | autofiltro y contadores |
| DOM-28 | §4 (06) | mapa de almacén precargado |
| DOM-29 | §4 (07) | precio anterior y variación |
| DOM-30 | §4 (07) | aviso «sin IVA» |
| DOM-31 | §4 (07) | % del total y objetivo relativo |
| DOM-32 | §2 (BONUS-08) | consumo del mes |
| DOM-33 | §2 (01 valoración) | A Pedir arranca en ámbar |
| DOM-34 | §1.3/1.5/1.6/1.8 | CF, ejemplos, protección, moneda |
| TEC-01 | §2 (01 filas) | rotación cíclica corregida |
| TEC-02 | §4 (BONUS-09) | EOQ parametrizada |
| TEC-03 | §2 (01 valoración) | valoración de stock viva |
| TEC-04 | §3 (04) | fórmulas y CF en el 04 |
| TEC-05 | §1.7 | pestañas citadas existen |
| TEC-06 | §1.9 | doble guarda cantidad/precio |
| TEC-07 | §2 (02) | MIN con guarda de vacío |
| TEC-08 | §4 (07) | hojas del 07 con fórmulas |
| TEC-09 | §3 (05) | DV de categoría + agregación |
| TEC-10 | §1.1 | una sola taxonomía con DV |
| TEC-11 | §4 (06) | semáforo de cuatro niveles |
| TEC-12 | §4 (06) | cantidad + alertas reales |
| TEC-13 | §3 (03) | DV 4/10/21 |
| TEC-14 | §4 (BONUS-09) | unidades del stock de seguridad |
| TEC-15 | §4 (BONUS-09) | guarda de consumo 0 |
| TEC-16 | §2 (02) | media, guarda y columna Nota |
| TEC-17 | §3 (04) | ✓ cantidad calculada + lote |
| TEC-18 | §1.8 | formatos de moneda y fecha |
| TEC-19 | §3 (03) | cabecera legible + freeze/print |
| TEC-20 | §3 (03) | totales en la columna correcta |
| TEC-21 | §2 (01 valoración) | ámbar propone reposición |
| TEC-22 | §1.3 | formato condicional real |
| TEC-23 | §1.10 §6 | filas libres y SUM ampliado; sin ListObject |
| TEC-24 | §2 (BONUS-08) | guarda de la variación |
| TEC-25 | §2 (01 filas) | par levels plausibles |
| COM-01 | §4 (BONUS-09) | EOQ con precio y coste de posesión |
| COM-02 | §2 (01 filas) | 50 filas reasignadas |
| COM-03 | §5 §6 | copy reescrito; sin enlaces externos |
| COM-04 | §3 (04) | afirmación falsa dentro del xlsx |
| COM-05 | §1.7 | pestañas prometidas |
| COM-06 | §3 (04) §5 | «9 con fórmulas» pasa a ser cierto |
| COM-07 | §5 | APPCC matizado |
| COM-08 | §3 (04) | tabla de temperaturas legal |
| COM-09 | §4 (06) | protocolo de caducado |
| COM-10 | §3 (05) | Plan de Acción con estructura |
| COM-11 | §4 (07) | dashboards con fórmulas |
| COM-12 | §3 (05) | agregación de mermas |
| COM-13 | §6 | reseñas y testimonios: aparcado por John |
| COM-14 | §2 (01 valoración) | valoración de stock |
| COM-15 | §4 (06) | mapa de almacén |
| COM-16 | §3 (03) | IVA del pedido |
| COM-17 | §3 (03) | dropdown de proveedores |
| COM-18 | §2 (02) | mejor proveedor + directorio |
| COM-19 | §1.1 §5 | tres taxonomías → una |
| COM-20 | §6 | aritmética de bonos: ancla aparcada |
| COM-21 | §6 | ancla de precio: aparcada |
| COM-22 | §5 §7.6 | cifra unificada y suficiencia |
| COM-23 | §4 (07) | definición de los KPI |
| COM-24 | §5 | changelog retitulado |
| COM-25 | §7.5 | licencia: decisión de John |
| COM-26 | §4 (06) | FIFO/FEFO |
| COM-27 | §1.5 | 12 hojas esqueleto |
| COM-28 | §2 (BONUS-08) | variación del bonus |
| COM-29 | §2 (02) | evaluación de proveedores |
| COM-30 | §3 (03) | datos del emisor |
| COM-31 | §2 (01 filas) | «Coca-Cola» → «Refresco de cola» |
| COM-32 | §7.6 | fuente del badge: decisión de John |

## 7-bis. Decisiones del orquestador sobre las dudas de §7 (2026-08-23, antes de construir)

1. **Top 20 del 07**: como recomienda §7.1 — el propio «Top 20» es la tabla de entrada (columnas
   verdes producto/categoría/importe) y el ranking (`LARGE`/`INDEX`/`MATCH`) ordena sobre ella. Sin
   hoja nueva.
2. **Hoja `Proveedores` del 03**: VISIBLE, 20 filas, con teléfono y pedido mínimo; alimenta el
   desplegable y el `VLOOKUP` de la cabecera.
3. **Taxonomía canónica**: las 10 categorías de `07!'Coste por Categoría'` en todo el kit; se
   reescribe la enumeración de 8 de la landing (las 3 ubicaciones citadas).
4. **«Simulador» del BONUS-09**: se RETIRA la promesa (Instrucciones y landing); `Parámetros`
   editable ya lo cubre.
5. **Licencia (COM-25)**: la FAQ se reescribe SOLO para quitar la contradicción, sin cambiar
   condiciones comerciales: «Licencia personal para tu negocio (todos tus locales). ¿Eres consultor
   y quieres usarlo con clientes? Escríbenos a info@aichef.pro». NO se añade cláusula nueva a los
   xlsx: los términos de licencia son decisión de John (queda en el handoff).
6. **Cifras sin fuente (COM-32/COM-22)**: se unifica el coste del software en «50-100 €/mes»; el
   badge del hero se reformula como estimación propia sin cifra absoluta inventada: «Las mermas sin
   control se comen un 3-5 % de tus compras: contarlas es el primer paso para recuperarlas» (rango
   estándar del sector, coherente con el 05). Nada de fuentes fantasma.
