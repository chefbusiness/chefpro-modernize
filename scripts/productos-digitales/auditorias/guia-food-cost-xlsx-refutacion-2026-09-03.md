# Refutación de los 8 libros de Excel — «Guía Food Cost + Ingeniería de Menú» v1.0

> Fecha: 2026-09-03 · Ámbito: `scripts/productos-digitales/guia-food-cost/build/*.xlsx` (8 libros, 33 hojas,
> 3.579 fórmulas) · Método: dos lentes en un pase (TÉCNICA y DOMINIO), openpyxl (fórmulas y `data_only`),
> XML crudo del `xl/worksheets/*` para el cache, pycel para recalcular con inputs cambiados, y contraste
> contra `guia-food-cost-SPEC.md`, `guia-food-cost/datos_ejemplo.py` y `guias-v2_0/motor.py`.
>
> **VEREDICTO: CORREGIR.** 3 hallazgos de gravedad ALTA, 6 MEDIA, 7 BAJA.
> La capa técnica está limpia (cero funciones prohibidas, cero constantes económicas dentro de fórmulas,
> cero celdas verdes con fórmula, cero errores en cache, protección sin contraseña, formatos completos).
> Lo que falla es **el contenido de dominio del ejemplo y una fórmula académica mal implementada**.

---

## Resumen ejecutivo

| # | Gravedad | Libro | Qué se rompe |
|---|---|---|---|
| A1 | **alta** | matriz-multimetodo-carta | El «Goal Value» no es el de Hayes & Huffman: algebraicamente es Pavesic ×constante. Coincide con él en 20/20 platos y sus 2 celdas verdes son inertes |
| A2 | **alta** | precio-objetivo-multi-metodo | El «margen objetivo (€)» está sembrado como 2,20 × coste: el método B es el método A disfrazado y pide 47,36 € por el chuletón |
| A3 | **alta** | carta-de-bebidas ↔ cuadro-de-mando | El pack modela dos restaurantes: 43.657 €/mes de bebida en la bodega contra 21.992 €/mes de media en el cuadro (×1,98) |
| M1 | media | plan-accion-90-dias | Las 5 decisiones «salidas de la matriz» contradicen las 5 que sugiere la matriz; una retira el plato que el diagnóstico dice «no retirar» |
| M2 | media | carta-de-bebidas | 8 vinos donde la SPEC pide 30, 4 cócteles donde pide 8, y **cero filas libres** en las tres hojas de producto |
| M3 | media | ficha-escandallo-base | El cap. 04 se queda sin celdas que citar: no existe la tabla de IVA soportado 4/10/21 % ni el albarán de ejemplo, ni el aceite de oliva al 4 % (D4) |
| M4 | media | simulador-repricing-multicanal | 0 de 20 platos viables en delivery: el ejemplo del libro que enseña a repreciar no enseña ni un caso viable |
| M5 | media | cuadro-de-mando ↔ plan/matriz | «Food cost %» con dos bases distintas en el mismo pack (consumo total ÷ ventas totales vs coste de comida ÷ ventas de comida) |
| M6 | media | matriz-multimetodo-carta | El diagnóstico del caso insignia (Gambas al ajillo, MC alto con FC 44,5 %) cae en el cajón genérico |
| B1-B7 | baja | varios | Constante 100 en fórmula · 0 en vez de "" en familia vacía · ejemplo del plan sin fechas · coste crudo mal sembrado · 5 desajustes en los mapas JSON · 2 columnas sin validación · «excluir» aplicado a la sala |

---

## ALTA

### A1 · El «Goal Value» no es el de Hayes & Huffman y duplica a Pavesic

- **Libro:** `matriz-multimetodo-carta.xlsx`
- **Hoja:** `Goal Value`
- **Celdas:** `G5:G29` (Goal Value del plato), `K5:K29` (Goal Value objetivo), `E3` (rótulo de la fórmula), `D33`/`D34` (los dos parámetros verdes)

**Problema.** La fórmula implementada es

```
G5 = (1-$E5) * $D5 * $F5 * (1-($D$33+$D$34))
```

es decir `(1 − food cost %) × uds × PVP × (1 − (personal % + otros variables %))`. La de Hayes & Huffman
(1985) es `A × B × C × D` con **`D = 1 − (variable cost % + food cost %)`**: el food cost entra **dos veces**,
en A y en D, y eso es justamente lo que hace del Goal Value una lente distinta.

Al omitir el food cost del último factor, éste queda **constante para todos los platos** (`1 − 0,42 = 0,58`), y
como `(1 − FC) × PVP = margen de contribución`, la fórmula se reduce a

```
Goal Value = MC × uds × k     ·     Goal Value objetivo = (media del MC ponderado de la familia) × k
```

Los dos lados llevan la misma `k`, así que `G ≥ K` **⟺** `P ≥ Q` de la hoja `Datos`, que es exactamente el eje
vertical de Pavesic. No es una coincidencia de estos datos: es una identidad algebraica.

**Pruebas.**

1. `Datos!P5` (MC ponderado) = 2.730,00 · 2.730 × 0,58 = **1.583,40** = `Goal Value!G5`, al céntimo.
2. La columna `Goal Value!L` («Lectura») coincide con `Pavesic!J` («Nivel de MC ponderado») en **20 de 20 platos**.
3. Recalculado con pycel tras subir `D33` de 0,32 a 0,60 y `D34` de 0,10 a 0,25 (del 42 % al 85 % de costes
   variables), **las 20 lecturas quedan idénticas**: cambia cada número y no cambia ni una clasificación. Las
   dos únicas celdas verdes de la hoja no pueden alterar su única salida.

**Daño.** La decisión D6 de la SPEC vende «cuatro métodos que miden dos de tres variables cada uno» y el pack
entrega tres lentes y una copia. La columna `Comparativa!H` («lecturas fuera de la mejor categoría») cuenta dos
veces la misma señal, inflando la discrepancia de todo plato con MC ponderado bajo (Torrija, Alcachofas, Sopa
de tomate, Lasaña, Fruta). Y el cap. 12 de la guía, que la SPEC obliga a escribir con «la fórmula completa» de
Hayes & Huffman citando estas celdas, atribuiría a esos autores una fórmula que no es la suya.

**Fix concreto.**

```
G5 = IFERROR(IF(OR($D5="",$E5="",$F5="",$D$33+$D$34+$E5>=1),"",
      (1-$E5)*$D5*$F5*(1-($D$33+$D$34+$E5))),"")
K5 = IFERROR(IF(OR($H5="",$I5="",$J5="",$D$33+$D$34+$J5>=1),"",
      (1-$J5)*$H5*$I5*(1-($D$33+$D$34+$J5))),"")
```

Actualizar `E3` a `Goal Value = (1 − food cost %) × uds × PVP × (1 − (personal % + otros variables % + food cost %))`
y añadir en `Instrucciones` la frase que explica por qué el food cost pesa dos veces (es lo que penaliza al plato
caro de producir y lo que separa a Goal Value de Pavesic). Regenerar, `inject_cache.py`, y **verificar que la
columna L ya NO coincide 20/20 con `Pavesic!J`** — con el fix, Gambas (FC 44,5 %) y Chuletón (45,3 %) deben
bajar por debajo del objetivo de su familia aunque su MC ponderado sea alto.

---

### A2 · El «margen objetivo (€)» es 2,20 × coste: el método B es el método A disfrazado

- **Libro:** `precio-objetivo-multi-metodo.xlsx`
- **Hoja:** `Por Plato`
- **Celdas:** `G9:G28` (Margen objetivo (€) — método B); secundariamente `H9:H28` e `I9:I28`
- **Origen:** `gen_precio-objetivo-multi-metodo.py:69` → `FACTOR_MARGEN = 2.2`

**Problema.** `G` está sembrada como `coste × 2,20` en los 20 platos (verificado: `G/D` = 2,200 en las 20 filas).
Un margen proporcional al coste **no es un margen objetivo: es un factor**. Consecuencia directa: la columna `N`
(«FC resultante con B») vale **31,2 % en los 20 platos** y la `M` («con A») 30,0 % en los 20. El libro promete en
`Instrucciones!A7` «el mismo plato con cuatro precios distintos y cuatro food cost distintos» y entrega dos
columnas que son la misma constante.

**Y el ejemplo enseña lo contrario de lo que dice el texto.** `Instrucciones!A14` justifica el reparto de métodos
con «coste por ración de 6 € o más, margen objetivo … el factor solo funciona en la banda intermedia: en el
chuletón dispara el precio». Pero el margen sembrado lo dispara igual:

| Plato | Coste | Método | PVP elegido (`Q`) | PVP actual (`V`) | Diferencia (`W`) | Semáforo (`U`) |
|---|---|---|---|---|---|---|
| Chuletón de vaca madurada | 14,80 € | B · Margen objetivo | **47,36 €** | 32,70 € | **+14,66 €** | Por encima del objetivo |
| Tataki de atún rojo | 9,60 € | B | 30,72 € | 22,40 € | +8,32 € | Por encima del objetivo |
| Lubina a la sal | 8,90 € | B | 28,48 € | 21,80 € | +6,68 € | Por encima del objetivo |
| Gambas al ajillo | 6,90 € | B | 22,08 € | 15,50 € | +6,58 € | Por encima del objetivo |

El libro propone subir el chuletón un 45 % y, aun así, marcarlo «Por encima del objetivo». Es el resultado que el
capítulo 09 usa para demostrar que el factor arruina los platos de coste alto — sólo que aquí lo produce el método
que se supone que lo arregla.

**Agravante.** `H` («precio de mercado de la zona») = `PVP actual × 1,03` y `I` («valor percibido») =
`PVP actual × 1,08`, en los 20 platos. Los cuatro métodos son, en el ejemplo, funciones deterministas de dos
únicos inputs (coste y PVP actual), así que el libro no puede enseñar ningún caso en que los métodos se separen
por razones de negocio.

**Fix concreto.** Sembrar `G` con un margen en euros **por familia**, tomado del MC medio ponderado que ya calcula
la matriz (`Datos!G40:G42`: Entrantes 7,46 €, Principales 10,80 €, Postres 4,48 €) redondeado a 6,50 / 10,50 / 4,20 €.
Con eso el chuletón sale a 25,30 € (FC 58,5 %, en rojo y con sentido: ese plato se vende por margen, no por
porcentaje) y la columna N deja de ser una constante. Para `H` e `I`, sembrar dispersión real por plato
(±5 a ±25 % según posicionamiento) en vez de dos factores únicos, y decirlo en `Instrucciones!A14`.

---

### A3 · La bodega y el cuadro de mando modelan dos restaurantes distintos

- **Libros:** `carta-de-bebidas-beverage-cost.xlsx` ↔ `cuadro-de-mando-prime-cost.xlsx` (y `matriz-multimetodo-carta.xlsx`)
- **Hojas/celdas:** `Resumen Bodega!B8` = 43.657,00 € · `Mensual!C5:C16` (18.000-26.200 €, suma `C17` = 263.900 €)
  · `Datos!I32` = 59.029,00 € · `Mensual!B17` = 616.000 €
- **Origen del dato:** `datos_ejemplo.py` → `CUADRO_MENSUAL` frente a `VINOS`/`CERVEZAS_REFRESCOS`/`DESTILADOS`/`COCTELES` y `PLATOS`

**Problema.** Los dos libros dicen ser el mismo restaurante modelado («La Encina», 70 plazas, 3.900 cubiertos/mes,
`datos_ejemplo.RESTAURANTE`) y no cuadran:

| Concepto | Bodega + matriz | Cuadro de mando | Factor |
|---|---|---|---|
| Ventas netas de **bebida** al mes | 43.657 € | 21.992 € (media; rango 18.000-26.200) | **×1,98** |
| Ventas netas de **comida** al mes | 59.029 € | 51.333 € (media; máximo 61.200 en diciembre) | ×1,15 |
| Ventas netas **totales** al mes | 102.686 € | 73.325 € | ×1,40 |
| Mix comida/bebida | 57 / **43 %** | 70 / **30 %** | — |

El 70/30 del cuadro es exactamente el que el propio libro cita como referencia en `Parámetros!A24`
(CaixaBankLab × elBulliFoundation); el 57/43 de la bodega lo contradice.

**El desempate señala al cuadro.** Los KPI sembrados del plan (`KPI de Seguimiento!B7` ticket medio 27,40 € y
`B8` MC por cubierto 18,10 €) cuadran con matriz + bodega sobre los 3.900 cubiertos (26,33 € y 18,43 €) y **no**
con el cuadro (18,80 €/cubierto). Como dato adicional que tampoco está conciliado: la matriz vende 4.870 platos
al mes para 3.900 cubiertos, o sea 1,25 platos por comensal en un restaurante de carta con entrantes, principales
y postres.

**Daño.** Los capítulos 02, 08, 16 y 19 citan celdas de los tres libros para el mismo restaurante. Un lector que
sume 59.029 + 43.657 y lo compare con los 64.000 € de enero del cuadro encuentra un agujero de 38.686 €, y el
producto se vende con la promesa de «una sola fuente de cifras» (SPEC §7-bis.7).

**Fix concreto.** Reescalar `CUADRO_MENSUAL` en `datos_ejemplo.py` conservando la estacionalidad: multiplicar la
columna de comida por 59.029 / 51.333 = 1,15 y la de bebida por 43.657 / 21.992 = 1,985, y subir en la misma
proporción compras, stocks y personal (para no romper los prime cost de 59-70 % que hoy dan bien). Alternativa
más barata: recortar `uds/mes` y `copas/mes` de la bodega a la mitad y subir un 15 % los meses del cuadro.
Después regenerar `cuadro-de-mando-prime-cost.xlsx` y revisar que `Mensual!R5:R17` siga marcando 4 meses por
encima del objetivo (hoy: enero, febrero, junio y agosto).

---

## MEDIA

### M1 · El plan contradice a la matriz en las 5 decisiones que dice haber sacado de ella

- **Libro:** `plan-accion-90-dias.xlsx` · **Hoja:** `Decisiones` · **Celdas:** `D5:D9` (y `K5:K9`, vacías)

| Plato | `Comparativa!J` (matriz) | `Decisiones!D` (plan) |
|---|---|---|
| Gambas al ajillo (E3) | Revisar | Resubir |
| Chuletón de vaca madurada (P5) | Rediseñar | **Mantener** (impacto 0 €) |
| Tabla de quesos (E5) | Rediseñar | **Retirar** |
| Lasaña de verduras (P8) | Revisar | Reformular |
| Fruta de temporada (D4) | Retirar | Rediseñar |

Cinco de cinco. La peor es la Tabla de quesos: `Comparativa!I9` dice literalmente **«MC alto con food cost pobre:
proteger el margen en euros, revisar precio, no retirar»** y el plan la retira, con la columna `Notas` (`K7`)
vacía. El chuletón, con las cuatro lecturas fuera de la mejor categoría (`Comparativa!H16` = 4), se «mantiene»
con impacto 0 €.

`Instrucciones!A20` cubre en abstracto que «aquí decide una persona», pero el ejemplo no justifica ni una sola
divergencia, y el cap. 19 recorre matriz → plan como un solo hilo.

**Fix.** Alinear `DECISIONES_EJEMPLO` con la columna `J` de `Comparativa` salvo en una o dos filas deliberadas, y
en ésas escribir el motivo en `Notas`: p. ej. «la matriz decía rediseñar; se retira porque son 90 uds/mes y ocupa
cámara». Así el ejemplo enseña la excepción en vez de ignorar la regla.

### M2 · La bodega se dimensiona a los datos sembrados: 8 vinos, 4 cócteles y cero filas libres

- **Libro:** `carta-de-bebidas-beverage-cost.xlsx` · **Hojas:** `Vinos` (5-12), `Cervezas y Refrescos` (5-11),
  `Destilados y Cócteles` (5-9 y 33-36) · **Origen:** `gen_carta-de-bebidas-beverage-cost.py:325`
  `V_FIN = V_INI + len(D.VINOS) - 1` (idem 458 y 595)

La SPEC §2.2 pide «30 vinos» y «8 cócteles». Entrega 8 vinos, 7 cervezas/refrescos, 5 destilados y 4 cócteles, y
en las tres hojas la fila TOTAL va pegada al último dato: **no hay una sola fila libre**. Para dar de alta el
noveno vino hay que desproteger la hoja, insertar fila y extender a mano `J13`, `K13`, `Q13`, `R13`, `S13`, el
semáforo `T5:T12` y la validación de datos. Una carta de vinos real tiene 30-60 referencias: el libro que se
vende como «la bodega como cuenta de resultados propia» no admite la bodega del comprador.

`precio-objetivo-multi-metodo!Por Plato` (9-28, 20 sembrados) y `simulador!Carta` (5-24, 20 sembrados) tienen el
mismo problema. La matriz sí lo hace bien: 25 filas, 20 sembradas, y `Instrucciones!A16` lo anuncia.

**Fix.** Dimensionar por capacidad y no por datos: 30 vinos, 15 cervezas/refrescos, 12 destilados, 8 cócteles,
25 filas en precio-objetivo y en el simulador; las filas vacías ya con verde, validación, formato y fórmulas.
Los totales usan `IF(COUNT(...)=0,"",SUM(...))`, que aguanta filas vacías sin tocar nada. Anunciar en cada
`Instrucciones` cuántas filas hay libres, como hace la matriz.

### M3 · El capítulo 04 no tiene celdas que citar: falta la tabla de IVA soportado y el albarán

- **Libro:** `ficha-escandallo-base.xlsx` · **Hoja:** `Ficha` · **Celda de anclaje:** `G9` («IVA de compra (%)») y
  la validación de `G10:G29`

El cap. 04 se titula «El coste real de compra: 4 %, 10 % y 21 % en el mismo albarán» y la SPEC §4 le exige una
«tabla de un albarán de ejemplo» construida desde los xlsx (§7-bis.7: «el PDF cita celdas, no inventa»). En los
8 libros:

- Los tres tipos aparecen **sólo** en el *prompt* de la validación de `G10:G29` («Tipo de IVA soportado de la
  línea: 0,04 · 0,10 · 0,21»), que sólo se ve al seleccionar la celda y no se puede citar.
- No hay ninguna lista de **qué producto va a cada tipo** (`IVA_SOPORTADO` de `datos_ejemplo.py`), ni la mención
  del **aceite de oliva al 4 % desde el RDL 4/2024**, que es una decisión firmada (D4) y verificada contra el BOE.
- `ALBARAN_EJEMPLO` (7 líneas con 4/10/21 %) no está en ningún libro.

La validación de `G10:G29` es `decimal between 0 y 0,21`, así que acepta 0,07 o 0,15 sin avisar.

**Fix.** Añadir a `ficha-escandallo-base.xlsx` una hoja «Albarán e IVA soportado» con (a) las tres filas de
`IVA_SOPORTADO` — tipo en celda verde y nota con el artículo (91.Dos.1.1.º / 91.Uno.1.1.º / 90), incluyendo
explícitamente los aceites de oliva en el 4 % con la referencia al RDL 4/2024 — y (b) el albarán de 7 líneas con
base, tipo, cuota y total. Cambiar la validación de `G10:G29` a lista `0,04 / 0,10 / 0,21` y añadir el mapa de
celdas correspondiente al `mapa-ficha-escandallo-base.json`.

### M4 · El simulador no enseña ni un solo plato viable en delivery

- **Libro:** `simulador-repricing-multicanal.xlsx` · **Hojas:** `Resumen` (`B7` = 0, `C7` = 20) y `Carta`
  (`Y5:Y24`, 20 «No»)

Con los datos sembrados **0 de 20 platos son viables en delivery** y sólo 6 de 20 en take away. El libro que la
SPEC define como «cuánto subir en cada canal y qué platos excluir del delivery» entrega un ejemplo cuya respuesta
es «todo fuera», incluida la Tarta de queso (coste 1,30 €, PVP necesario 9,52 € contra un techo de 6,90 €).

La causa es el sembrado: `PRECIO_TECHO_APP` ≈ 1,2 × PVP de sala mientras el canal carga 30 % de comisión y
0,70 €/plato de envase con FC objetivo del 30 %. Recalculado con pycel bajando la comisión al 12 % y el envase a
0,40 €/pedido salen **7 viables** y los caros siguen dando «No», que es la lección que se busca.

`Resumen!A11` lo reconoce con honestidad, pero además contradice al plan: `Decisiones!B10:B11` retira **dos**
platos del delivery citando este mismo simulador, no veinte.

**Fix.** Subir `PRECIO_TECHO_APP` a 1,35-1,45 × PVP de sala (que es el diferencial real de las apps) y/o poner
`SIMULADOR_DEFECTO['fc_objetivo_delivery']` en 0,35. Objetivo: ~8-12 viables, con «Chuletón», «Lubina»,
«Tataki», «Bacalao» y «Tabla de quesos» en «No». Después alinear las decisiones del plan con el resultado.

### M5 · «Food cost %» tiene dos bases distintas dentro del mismo pack

- **Libros:** `cuadro-de-mando-prime-cost.xlsx` (`Mensual!I5:I17`) ↔ `plan-accion-90-dias.xlsx`
  (`KPI de Seguimiento!K5`) y `matriz-multimetodo-carta.xlsx` (`Datos!H32`)

`Mensual!I5` = `consumo de materia prima ÷ ventas netas TOTALES` (comida + bebida), bajo el rótulo «Food cost (%)»
→ 31,7 % en enero, 32,09 % en el año. `Datos!H32` = `coste de comida ÷ ventas de comida` → 32,68 %. Y la nota
`KPI!K5` define el KPI como «Coste de producto sobre ventas netas **de comida**». Tres celdas, dos definiciones,
un solo nombre. Los caps. 02, 07 y 08 citarían las dos.

**Fix.** Renombrar `Mensual!I4` a «Coste de materia prima sobre ventas totales (%)» —que es lo que calcula y lo
que necesita el prime cost— y añadir en `Instrucciones` la frase que lo distingue del food cost de comida de la
matriz. O, si se prefiere mantener el nombre, separar consumo de comida y de bebida en dos columnas verdes y
calcular los dos porcentajes.

### M6 · El diagnóstico del caso insignia (Gambas al ajillo) cae en el cajón genérico

- **Libro:** `matriz-multimetodo-carta.xlsx` · **Hoja:** `Comparativa` · **Celdas:** `I5:I29` (rama
  `AND(OR($D5="Puzzle",$D5="Star"),OR($E5="Loser",$F5="Problem"))`)

Gambas al ajillo es el ejemplo canónico de «MC alto con food cost pobre»: FC 44,5 % contra el 30,7 % medio de su
familia, y MC 8,60 € contra 7,46 €. La rama que emite ese texto exige que Miller sea «Loser» **o** Pavesic
«Problem», y Gambas es Star + **Marginal** + **Standard** → `I7` acaba en «Las lecturas discrepan: … decide con
la que más te duela este mes». El plato que la SPEC (D6, cap. 13) usa para explicar el protocolo de decisión no
recibe el diagnóstico que lo explica.

**Fix.** Sustituir esa condición por una comparación directa de las dos variables, que es lo que describe el
mensaje:

```
IF(AND('Datos'!$G5>='Datos'!$N5,'Datos'!$H5>'Datos'!$O5),
   "MC alto con food cost pobre: proteger el margen en euros, revisar precio, no retirar", …)
```

Comprobar después que la reciben Gambas (E3), Chuletón (P5), Tabla de quesos (E5), Lubina (P6), Tataki (P9) y
Bacalao (P2), y que la columna `J` de esos platos no queda en «Revisar».

---

## BAJA

| # | Libro · hoja · celda | Problema | Fix |
|---|---|---|---|
| B1 | matriz · `Menú Precio Fijo` · `B41:D41` | `=B40*100` teclea el número de menús servidos dentro de la fórmula; para 2.400 menús/mes hay que rehacerla a mano | Celda verde «Menús servidos al mes» junto a `C22` y referencia absoluta `$C$24` |
| B2 | matriz · `Datos` · `F43` (y `C43:E43`) | La familia «Menú», sin platos, muestra «0,0 %» de mix y 0 platos mientras `G43`/`H43` sí devuelven `""`. La regla de la familia es «sin dato = "" nunca 0» | `=IFERROR(IF(OR($D$32=0,$E43=0),"",$E43/$D$32),"")`, y lo mismo en `C43`/`D43`/`E43` |
| B3 | plan · `Decisiones` `G5:G14` y `Calendario 90 Días` `D5:E30` | El ejemplo no trae **ni una fecha** (ni responsables en el calendario) mientras `Decisiones!E3` dice «sin responsable y sin fecha, no es una decisión: es una opinión» e `Instrucciones!A6` lo repite | Celda verde «Fecha de inicio del plan» y derivar `=$fecha+7*($A5-1)` en las 13 semanas; sembrar responsables en el calendario |
| B4 | rendimiento-mermas · `Merma de Cocción` · `I6` (y `I8`, `I10` vacías) | El coste/kg crudo del solomillo se siembra a 15,80 €, el precio bruto de albarán, cuando la nota `M6` de la propia hoja pide usar el «Coste neto €/kg limpio APROVECHANDO» (la ficha le aplica 12 % de merma → 17,95 €/kg). Y 3 de 5 filas del ejemplo se quedan sin `I`, así que `J` y `K` salen en blanco | Sembrar `I` con el coste ya limpio y rellenar las 5 filas |
| B5 | `mapa-simulador-…json` (`Resumen`) y `mapa-precio-objetivo-…json` (`Por Plato`) | 5 desajustes: la cabecera declarada «Food cost efectivo medio al PVP de sala (%)» no es la del libro («… (media simple, %)»), y las «tablas» de las filas 40-44 y 47-50 declaran cabeceras («Método», «Facturación (€)», «Platos») que no existen: son bloques etiqueta-valor sin fila de cabecera. Un capítulo que copie el mapa imprimiría rótulos que no están en el xlsx | Copiar las cabeceras literales del libro y mover esos dos bloques de `tablas` a `celdas` |
| B6 | simulador · `Carta` · `D5:D24` y `F5:F24` | «PVP en sala, sin IVA» y «Precio techo del mercado» son las dos únicas columnas verdes numéricas del libro sin validación (`C` y `G` sí la tienen) | `dv_numerica(ws, …, minimo=0)` con su prompt, como en `C` |
| B7 | simulador · `Carta` · `K5:K24` | La columna «¿Viable?» aplica a la **sala** el precio techo de la app y marca «No: excluir o reformular» a 7 platos del comedor (gambas, tabla de quesos, bacalao, arroz, chuletón, lubina, tataki). `Resumen!A12` lo matiza, pero el rótulo dice «excluir» | Texto distinto para el canal de sala («No llega al objetivo al precio que acepta el mercado») o techo propio por canal |

---

## Lo que se intentó tumbar y aguantó

Estas comprobaciones se hicieron esperando encontrar fallos y **no los hay**:

1. **Cache tras `inject_cache`.** 3.579 fórmulas en los 8 libros; **todas** llevan su elemento `<v>` en el XML
   (comprobado sobre `xl/worksheets/*.xml`, no sólo con `data_only`). Las 514 que `openpyxl` devuelve como `None`
   son filas sin datos cuyo resultado cacheado es la cadena vacía — el «sin dato = ""» de la familia, no un cache
   perdido. **Cero cachés con error** (`#DIV/0!`, `#N/A`, `#REF!`, `#VALUE!`).
2. **Funciones prohibidas: 0.** Ni `INDIRECT`, ni `COUNTA`, ni `PMT`, ni `OFFSET`, ni `XLOOKUP`, ni `LET`, ni
   `LAMBDA`, ni matrices dinámicas (`FILTER`, `SORT`, `UNIQUE`, `SEQUENCE`). El repertorio usado es
   `SUM/SUMIF/SUMPRODUCT/COUNTIF/COUNT/INDEX/MATCH/IF/IFERROR/ISNUMBER/AVERAGE/MIN/MAX/ROUND/AND/OR`.
3. **Constantes económicas dentro de fórmulas: 0.** El barrido de literales sólo devuelve `0`, `1` y `2`
   (estructurales), `100` (conversión cl→L, documentada en `Destilados y Cócteles!B30`, y el multiplicador de
   B1), `12` (meses del año) y `3`/`4` (recuentos de `Comparativa!C40`). Ningún 0,10 / 0,21 / 0,04 / 0,30 / 0,33 /
   0,70 vive dentro de una fórmula: todos están en celda verde con nota y se referencian con `$` absolutos.
4. **Celdas verdes con fórmula: 0**, en los 8 libros. Y **0 celdas verdes bloqueadas** / **0 no verdes
   desbloqueadas**: el bloqueo casa con el relleno al 100 %.
5. **Protección:** las 33 hojas protegidas y **ninguna con contraseña**.
6. **Semáforos numéricos con `ISNUMBER`:** todos los bloques de formato condicional sobre números lo llevan
   (`=AND(ISNUMBER($T5),ISNUMBER($E$15),$T5>$E$15)` y equivalentes); los de texto usan `cellIs equal` sobre el
   vocabulario, que es el patrón de `motor.semaforo_texto`.
7. **`IFERROR(...,"")` en todo cociente** y guardas `IF(OR(...="", ...=0),"")` antes de dividir. No se encontró
   ninguna división sin protección.
8. **Formatos:** 0 celdas numéricas con formato `General` en todo el pack. `#,##0.00 €`, `0.0%`, `0.000` y
   `#,##0` aplicados de forma consistente. A4 (`paperSize 9`), `fitToWidth=1`, Instrucciones en vertical y hojas
   de datos apaisadas — igual que `menu-engineering-matrix.xlsx` y `escandallo-maestro.xlsx` de la familia.
9. **Hoja «Instrucciones» primera en los 8 libros**, con A1 título, A2 «AI Chef Pro · aichef.pro — Guía Food Cost
   + Ingeniería de Menú», pasos numerados (7-8 según libro), «Celdas verdes = campos editables», la nota de IVA
   que corresponde, la nota de desproteger, la bio anclada de John Guerrero y la línea de versión **exacta**:
   `Versión 1.0 · septiembre 2026 · aichef.pro/guia-food-cost-ingenieria-menu · info@aichef.pro`. Ninguno usa la
   línea 2.0 del motor. Metadata correcta en los 8 (`creator='AI Chef Pro'`, `subject='Guía Food Cost +
   Ingeniería de Menú · Versión 1.0 · septiembre 2026'`).
10. **Caracteres no latinos: 0** en las 33 hojas. Sin erratas detectables, sin dobles espacios, sin vocabulario
    LATAM colado (ni «costo», ni «platillo», ni «mesero»); «solo» sin tilde es la forma vigente.
11. **Matriz de IVA 3×3 (D4) correcta y realmente cableada.** Sala 10/10/10, take away y delivery 10/21/21, con
    las notas de los arts. 91.Uno.2.2.º y 91.Uno.1.1.º y la exclusión desde 1-ene-2021. Probado con pycel:
    cambiando `Parámetros!D6` a 0,21 el PVP con IVA del vino en sala pasa de 3,30 a 3,63 €, y bajando `C7` a 0,10
    el refresco para llevar pasa de 2,783 a 2,53 €. `INDEX/MATCH` sobre la matriz en los tres libros que la
    llevan; ningún `IF` binario. La clasificación de las bebidas es fina y correcta: cerveza sin alcohol, agua y
    zumo natural van a la columna «Comida» (10 % para llevar) y el refresco de cola al 21 %.
12. **Los tipos de IVA soportado de la ficha son correctos uno a uno**: aceite de oliva 4 %, boniato, cebolla y
    rúcula 4 %; mantequilla, nata, caldo y especias 10 % (no están en la lista del 4 %); vino PX 21 %.
13. **Prime cost con el umbral español (D5)**: 65 % servicio en mesa / 55 % barra, los dos en celda verde, con la
    fuente CaixaBankLab × elBulliFoundation y el 60 % de Toast citado sólo como contraste de EE. UU. El semáforo
    marca 4 meses por encima (enero, febrero, junio, agosto) y la fila TOTAL es media **ponderada**, no media de
    porcentajes. SS 33 % desde `Parámetros!B20`. Gráfico de líneas con 2 series.
14. **Pavesic con MC ponderado (D6)**: eje `MC × uds` contra la media de la familia — correcto. Miller con FC %
    contra el FC medio ponderado de la familia — correcto. Kasavana & Smith con umbral `0,7 ÷ N` por familia
    (`Datos!M5` = 0,7/7 = 10 %) y MC contra el **medio ponderado** de la familia — correcto.
15. **Clasificaciones razonables sobre la carta de ejemplo**: Tarta de queso = Star ✓; Fruta de temporada = Dog /
    Loser / Problem ✓; Gambas y Chuletón muestran la discrepancia MC alto vs FC % pobre ✓ (Gambas Star pero
    Miller Marginal; Chuletón Puzzle/Loser/Problem con `H=4`). La Tabla de quesos sale **Puzzle**, no Dog: es lo
    correcto por el método (mix 5,2 % bajo el umbral del 10 %, pero MC 8,40 € sobre la media de 7,46 €).
16. **Menú de precio fijo**: los tres cursos suman 100 % en los tres escenarios y hay formato condicional que se
    pone en rojo si un curso no suma 1 (`=AND(ISNUMBER(B27),ROUND(B27,4)<>1)`). El FC del menú (42,7 %) queda por
    encima del objetivo y `A44` lo explica en vez de esconderlo.
17. **Doble contabilidad de la bodega, evitada a propósito**: el Gin tonic aparece en las dos tablas de
    `Destilados y Cócteles` (como combinado y desglosado), y la columna `G32` «¿Suma al total de la bodega?» lo
    marca «No» para que `J37` no lo cuente dos veces. `B41`/`B42` lo explican, incluida la advertencia sobre el
    cava usado como ingrediente del spritz.
18. **Beverage cost por copa coherente**: tinto de la casa 26,0 %, crianza 29,8 %, PX 35,9 % por copa; total
    vinos 30,2 % contra un objetivo del 30 % → semáforo en rojo, que es lo que debe pasar. Copas por botella
    derivadas de `formato ÷ servicio` (75/15 = 5; el PX de 50 cl a 6,25 cl = 8).
19. **Prueba de dos inputs por libro, recalculada con pycel** (verificación obligatoria nº 2):

| Libro | Inputs cambiados | Salidas y dirección |
|---|---|---|
| ficha-escandallo-base | solomillo 15,80 → 22,00 €/kg; merma 12 → 25 % | bruta 0,250 → 0,293 · coste ficha 5,67 → 8,17 € · PVP objetivo 18,90 → 27,25 € · FC real 32,8 → 47,3 % · subida necesaria 9,3 → 57,5 % ✔ |
| rendimiento-mermas | lubina limpio 0,62 → 0,40 kg; merma medida de verduras de hoja | rendimiento 51,7 → 33,3 % · coste neto 27,63 → 42,82 €/kg · «Merma que usas» 12,5 → 22,0 % y el origen cambia a «Tu medición» ✔ |
| precio-objetivo | FC objetivo global 30 → 25 %; Gambas de método B a C | PVP por factor 7,00 → 8,40 € · Gambas PVP elegido 22,08 → 15,96 € y FC final 31,3 → 43,2 % ✔ |
| matriz-multimetodo | Tabla de quesos 90 → 900 uds; Gambas coste 6,90 → 3,20 € | Tabla de quesos Puzzle → **Star** · Gambas → Star/Winner/Prime con `H=0` y decisión «Mantener» · FC ponderado 32,68 → 32,18 % ✔ |
| simulador-multicanal | comisión delivery 30 → 12 %; packaging 1,75 → 0,40 €/pedido | viables en delivery 0 → **7** · FC delivery croquetas 46,5 → 29,9 % · margen mensual 24.249 → 35.969 € ✔ |
| carta-de-bebidas | copa 15 → 10 cl; objetivo vinos 30 → 35 %; `D6` 10 → 21 % | copas/botella 5 → 7,5 · coste copa 0,78 → 0,52 € · BC copa 26,0 → 17,3 % · PVP copa con IVA 3,30 → 3,63 € ✔ |
| cuadro-de-mando | tipo → «Barra / autoservicio»; SS 33 → 40 % | objetivo 65 → 55 % · coste de personal enero 21.382 → 22.460 € · prime cost 65,1 → 66,8 % · diciembre y el TOTAL pasan a «Por encima del objetivo» ✔ |
| plan-accion-90-dias | 2 decisiones a «Hecha»; 1 hito a «Sí» | cerradas 0 → 2 · % cerradas 0 → 20 % · impacto conseguido 0 → 430 € · avance del calendario 0 → 3,8 % ✔ |
| matriz · Goal Value | personal 32 → 60 %; otros 10 → 25 % | **las 20 lecturas NO cambian** ✗ → hallazgo A1 |

20. **Recuento de celdas verdes por hoja** (verificación obligatoria nº 5):

| Libro | Celdas verdes por hoja | Total |
|---|---|---|
| ficha-escandallo-base | Instrucciones 1 · Ficha 146 | 147 |
| rendimiento-mermas-producto | Instrucciones 1 · Test de Rendimiento 90 · Merma de Cocción 60 · Mi Tabla de Mermas 90 | 241 |
| precio-objetivo-multi-metodo | Instrucciones 1 · Por Plato 182 | 183 |
| matriz-multimetodo-carta | Instrucciones 1 · Datos 127 · K-S 0 · Miller 0 · Pavesic 0 · Goal Value 2 · Comparativa 0 · Menú Precio Fijo 76 | 206 |
| simulador-repricing-multicanal | Instrucciones 1 · Parámetros 21 · Carta 120 · Resumen 0 | 142 |
| carta-de-bebidas-beverage-cost | Instrucciones 1 · Parámetros 12 · Vinos 72 · Cervezas y Refrescos 63 · Destilados y Cócteles 124 · Resumen Bodega 0 | 272 |
| cuadro-de-mando-prime-cost | Instrucciones 1 · Parámetros 5 · Mensual 96 | 102 |
| plan-accion-90-dias | Instrucciones 1 · Decisiones 181 · Calendario 90 Días 182 · KPI de Seguimiento 56 | 420 |

(La celda verde de cada `Instrucciones` es la muestra de color junto a «Celdas verdes = campos editables»; las
hojas derivadas —K-S, Miller, Pavesic, Comparativa, los dos Resumen— tienen 0 a propósito: no se teclea nada en
ellas.)

21. **Mapas de celdas**: 983 celdas y 45 tablas declaradas en los 8 JSON. Todas las coordenadas existen y ninguna
    apunta a una celda vacía ni a una fórmula sin cache. Los 5 desajustes encontrados son de rótulo (B5).
22. **Los 8 generadores escriben sólo en `guia-food-cost/build/`**, importan `datos_ejemplo` y fijan
    `motor.CTX['producto'] = 'guia-food-cost-ingenieria-menu'` sin usar `motor.version_line()`. Ninguno toca
    `astro-site/public/dl/**` ni ficheros de otro libro.
23. **Coherencia de la carta entre libros** (lo que la SPEC §2.2 exige de forma explícita): los 20 platos, con su
    familia, coste, PVP y uds, son idénticos en `matriz!Datos`, `precio-objetivo!Por Plato` y `simulador!Carta`;
    el coste de P1 es `coste_ficha()` = **5,67 €** en los tres y `ficha!E33` lo devuelve al céntimo.

---

## Qué falta antes de dar el pack por bueno

1. Corregir A1 (fórmula de Goal Value) y volver a comprobar que su lectura ya no coincide 20/20 con Pavesic.
2. Corregir A2 (sembrado del margen objetivo) y comprobar que la columna `N` deja de ser constante.
3. Conciliar A3 en `datos_ejemplo.py` y regenerar el cuadro y el plan.
4. M1 a M6 antes de escribir los capítulos 02, 04, 08, 09, 12, 13, 15 y 19, que citan justo esas celdas.
5. Tras cada regeneración: `inject_cache.py` + verificación `data_only` + `postprocess-transversal.py --dry-run`
   + `gate-no-latinos.py`, y repetir la prueba de dos inputs de la tabla del punto 19.

*Refutación realizada el 2026-09-03 · Vía: Claude Code*
