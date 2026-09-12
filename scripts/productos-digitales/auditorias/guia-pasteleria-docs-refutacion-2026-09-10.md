# Refutación de los DOCUMENTOS — «Cómo Montar una Pastelería» (2026-09-10)

**Veredicto: CORREGIR ANTES.** 46 hallazgos confirmados: **11 altos, 25 medios, 10 bajos**.
Lente A (rigor legal y de cifras): 19 · Lente B (coherencia y no-solape): 14 · Lente C (calidad editorial): 13.

**Qué se ha leído entero:** `guia-pasteleria-obrador.md` (1.811 líneas, 55.874 palabras, 21 entradas de
capítulo, 43 tablas), `BONUS-12-decisiones-de-apertura.md` (690 líneas, 12 decisiones) y
`business-plan-modelo-pasteleria.md` (365 líneas), los **46 ficheros de la caché `txt/`**, el
`guion_guia_pasteleria_obrador.py` (**315 referencias `C()` resueltas una a una contra las celdas**), la
SPEC, la verificación legal del 10-sep con sus 13 prohibiciones, los ids `PA-*`/`PS-*` del research y las
celdas de los **8 xlsx** (openpyxl `data_only=True`, un fichero cada vez), más los tres PDF con PyMuPDF.

> **No se ha encontrado**: ninguna cifra de la lista negra del §5 (ni «11.729 pastelerías», ni «1,08 M€»,
> ni el rango inventado de 84.000-180.000 €, ni cifra puntual de cacao, ni el horno Salva a 1.499 €, ni
> franquicias como dato auditado, ni ticket medio «de pastelería», ni el reparto de canal del total
> alimentario — el cap. 2 lo desmiente expresamente); **PS-60 no existe ya en el JSON**; ningún carácter no
> latino; ninguna mención a las guías hermanas (**D19 se cumple**); ni una sola vez «artesana» por
> «artesanal»; «dulcería» sólo aparece para decir que no se usa; ninguna promesa de rentabilidad ni de
> tráfico; ningún «cumple la normativa» ni «100 % legal»; ningún «oficial» como nombre de perfil; ningún
> «RGSEAA obligatorio», ningún «carnet de manipulador» vivo, ningún «Verifactu 2026», ningún «conflicto
> 4 °C/8 °C»; el art. 3 va con su puerta de entrada y sus dos vías **alternativas**; el 13.8 con sus
> **cinco** letras y la e) valenciana; el 13.5 con la única incondicional; el 9.3 con las 24 h y el
> registro de hora; el DB-HS 3 **descartado** y el RITE con AE3/AE4 en su sitio; IAE 644.1 con su nota de
> fabricación; pan al 4 % con la Resolución de la DGT y el cruasán al 10 %; táper obligatorio por el
> RD 1055/2022; registro horario **sin** norma digital; Ley 1/2025 con la exención acotada al 6.4; libertad
> horaria con el matiz de «actividad principal»; y las cinco normas muertas, en el anexo.
> `solape.py` da **1 par en 46 bloques**: `puntos_por_epigrafe` (D33) **ha funcionado**.
>
> **Lo que falla es otra cosa: dos bugs de tubería que nadie miró (un regex de formato y un par de
> referencias de celda desplazadas una fila), cifras del mismo concepto calculadas de dos maneras en dos
> libros distintos, y tres afirmaciones que el propio pack desmiente en otra página.**

---

## 0. Salida de `solape.py` (umbral 0,55)

```
guia (21 caps):   cap 12 → 1 par (0,58) «Tres de esas treinta referencias están tomadas del Kit
                  de Escandallos, para que las cifras…»   ·   resto: 0
BONUS (12 caps):  TOTAL 0
business plan (6): TOTAL 0
TOTAL PACK: 1 par
```

El único par es una frase de frontera con el Kit de Escandallos que el cap. 12 escribe en sus dos bloques
(`cap12_b1` y `cap12_b2`). Es real y hay que podar una de las dos, pero no es el problema de este pack:
comparado con los **41 pares en 15 de 20 capítulos** del Manual del Chef Ejecutivo, `puntos_por_epigrafe`
ha hecho su trabajo y **la pasada de desduplicación no hace falta**.

---

## 1. Las dos causas raíz (explican 5 de los 11 hallazgos altos)

### Causa 1 · `documentos.py:722` — el nombre del producto dispara el formateador de porcentajes

```python
if es_fila_porcentual(fila[:2]):        # RX_ETIQUETA_PCT = r'\(\s*%\s*\)|\ben\s*%|\(porcentaje\)|%\s*$'
    for k in range(1, len(fila)):
        fila[k] = pct(v, 1) if abs(v) <= 1.5 else num(v, 1) + NARROW + '%'
```

La guarda que se añadió el 2026-08-29 para que una fila etiquetada «(%)» no se imprimiera con el formato de
su columna mira **las dos primeras celdas de la fila**. La referencia **T1 se llama «Tarta de chocolate
70 %»** y termina en `%`, así que **las tres filas del pack que la contienen se reformatean enteras como
porcentajes**. No hay ningún aviso, el gate `coherencia_cifras` queda verde y el defecto está vivo en el
PDF que se vende (verificado en la página 83).

### Causa 2 · el guion cita I52/I54 donde la hoja tiene I53/I55

`checklist-equipamiento-y-proveedores!Equipamiento` guarda en **I53** el «Plazo crítico de entrega
(semanas)» = **9** y en **I55** el «Margen del plazo crítico (semanas)» = **9**. El guion pide **I52** —que
es el **veredicto de la desviación**, un texto: «En línea con el CAPEX del libro 2»— y **I54** —que es la
**línea que marca el plazo**, otro texto: «Cámara de fermentación controlada (roll-in)»—. Como
`formatear()` devuelve `str(v)` cuando el valor no es numérico, **`verificar_guion.py` no falla** (la celda
existe y no está vacía) y los redactores recibieron dos etiquetas numéricas con texto dentro.

Barrido completo: **de las 315 referencias `C()` del guion, sólo estas 6 (3 pares, en los tres documentos)
resuelven a texto bajo un formato numérico**. Las otras 309 casan en tipo.

---

## 2. Lente A — RIGOR LEGAL Y DE CIFRAS

### A1 · ALTA · guía caps. 3, 12 y 17 · guion + `documentos.py:722`
> cap. 17: `| T1 | Tarta de chocolate 70 % | No | 4,0 % | 24,0 % | Vitrina refrigerada |`

En la tabla «Qué referencia puede viajar y cuál no», la **temperatura legal de conservación se imprime como
«4,0 %» y el plazo del art. 9.3 como «24,0 %»**. Son 4 °C y 24 horas: las dos cifras legales que el
capítulo entero sostiene. Las otras 29 filas salen bien; sólo la de la tarta de chocolate se rompe, y se
rompe por el `%` de su nombre (causa 1). Las otras dos apariciones:

| Dónde | Se imprime | Debe decir (celdas) |
|---|---|---|
| cap. 3, «Decisión de Surtido» | `35,2 % · 99,9 % · 120,0 % · 1,2 %` | `35,2 % · 1,00 € · 1,2 · 0,01 €` (D18/E18/F18/G18) |
| cap. 12, «Coste Hora y Mano de Obra» | `12,0 % · 45,0 % · 112,1 % · 115,2 % · 2,3 % · 35,2 %` | `12 · 45 · 1,12 € · 1,15 € · 2,27 € · 35,2 %` |
| cap. 17, «Decisión de Huevo y Temperatura» | `No · 4,0 % · 24,0 %` | `No · 4 · 24` |

**Fix (generador, es la única forma de cerrarlo):** en `documentos.py`, `es_fila_porcentual()` debe mirar
**sólo la primera celda** de la fila, o exigir que el `%` esté precedido de `)` / de «en» — el patrón
`%\s*$` sobre `fila[:2]` casa con cualquier producto cuyo nombre acabe en porcentaje. **Fix alternativo sin
tocar código:** renombrar la referencia en `datos_ejemplo.py` a **«Tarta de chocolate negro»** y regenerar
los 8 libros. *Ojo: el nombre «Tarta de chocolate 70 %» es uno de los tres que deben coincidir con
`kit-escandallos/05-pasteleria.xlsx` (§3 de la SPEC), así que si se renombra hay que renombrarlo también
allí o romper la coherencia con el kit.*

### A2 · ALTA · guía cap. 8, bonus 9 y business plan §6 · guion, 6 referencias
> cap. 8: «El plazo crítico de entrega de esta dotación **queda marcado en línea con el CAPEX del libro 2**
> de este mismo pack» · «el margen que te queda hasta la apertura prevista: **veinte semanas**»

La primera frase no significa nada: el redactor recibió como valor de «Plazo crítico de entrega, en
semanas» el texto **«En línea con el CAPEX del libro 2»** (causa 2) y lo cosió a la prosa. La segunda es
peor: recibió como «Margen de ese plazo crítico hasta la apertura, en semanas» el texto **«Cámara de
fermentación controlada (roll-in)»** y, al no poder usarlo, **se inventó «veinte semanas»**. La celda real
dice **9**. Es la única cifra fabricada que he encontrado en los tres documentos, y está en un producto de
65 € que promete que cada número sale de una celda.

**Fix (guion), 6 sitios:** `!Equipamiento!I52` → **`!Equipamiento!I53`** y `!Equipamiento!I54` →
**`!Equipamiento!I55`** (líneas 1841, 3155, 3156, 3841, 4519, 4520 de
`guion_guia_pasteleria_obrador.py`).
**Fix (texto, cap. 8):** «El plazo crítico de entrega de esta dotación es de **nueve semanas**, y lo marca
la cámara de fermentación controlada: es la primera que hay que pedir aunque sea la última que instales.» ·
«Lo que sí puedo darte aquí es el margen que te queda hasta la apertura prevista: **nueve semanas**.»
**Fix (gate):** `verificar_guion.py` debe abortar cuando una referencia con formato `eur*`/`pct*`/`num*`
resuelva a un valor no numérico. Hoy sólo comprueba que exista y no esté vacía, y por eso pasó en verde.

### A3 · ALTA · guía caps. 1, 4 y 19 contra business plan §1 · `calculadora-capex` vs `plan-financiero`
> guía: «una inversión total, con el fondo de maniobra dentro, de **228.049 €**» · «el desembolso total con
> IVA […] llega a **261.960 €**»
> business plan: «El fondo de maniobra añade **62.115 €**, y la suma de los dos da la inversión total:
> **227.916 €**. La necesidad total de caja al arranque sube hasta **261.826 €**»

**Los dos documentos del mismo pack publican dos inversiones totales distintas para el mismo caso.** El
fondo de maniobra son 4 meses de costes fijos, y cada libro usa los suyos:
`calculadora-capex!IVA y Tesorería!B13` = **62.248,84** (4 × 15.562,25) y
`plan-financiero!Inversión Inicial!B16` = **62.115,26** (4 × 15.528,82, el fijo mensual del año 2 del P&L).
Arrastra también la aportación propia: **201.960 €** en el capex contra **201.826 €** en el business plan.
Son 134 € de diferencia; el problema no es el importe, es que **el documento que se le enseña al banco no
dice lo mismo que el capítulo que lo explica**, y el primero que abra los dos xlsx lo ve.

**Fix (xlsx, no de texto):** el fondo de maniobra tiene que calcularse en **un solo sitio**. Lo natural es
que `calculadora-capex` lo tome de los costes fijos mensuales del año de crucero del plan financiero
(copia declarada, como el resto del pack) y que las dos hojas publiquen **62.115 €**, **227.916 €**,
**261.826 €** y **201.826 €**. Después hay que regenerar el guion y los bloques afectados (cap. 1, cap. 4,
cap. 19 y business plan §1).

### A4 · ALTA · guía cap. 4 · `txt/cap04_b1.txt`
> «Para el caso modelado, **el fondo de maniobra asciende a 15.562 €**, y ese importe está pensado para
> cubrir 4 meses de gastos fijos»

**15.562 € es el coste fijo de UN mes**, no el fondo. El fondo son **62.249 €**, y así lo dice la tabla de
CAPEX que va **dos párrafos más abajo en el mismo capítulo** («Fondo de maniobra | 62.249 €») y la de la
línea a línea («Colchón de tesorería | 62.249 €»). Además, un fondo de 15.562 € haría que la inversión
total del cap. 1 (228.049 = 165.800 + 62.249) no cuadrara. El lector cuenta 15.562 × 4 = 62.248 y descubre
solo el error, que es la peor forma de descubrirlo.

**Fix:** «Para el caso modelado, el fondo de maniobra asciende a 62.249 €: son 4 meses de gastos fijos
—alquiler, nóminas, suministros— a razón de 15.562 € al mes, sin necesidad de haber facturado un euro.»

### A5 · ALTA · guía cap. 19 (pie de tabla) y business plan §5 (×2) · guion + `business-plan/cap05_b1.txt`
> guía cap. 18 (**correcto**): «el equilibrio contable exige 155,6 tickets diarios, y el de caja exige 148,9»
> guía cap. 19, pie de la tabla de deuda: «Por eso **el punto de equilibrio de caja está por encima del contable**.»
> business plan §5: «El equilibrio contable […] **pide menos tickets al día que el equilibrio de caja**» ·
> «**hace falta vender más para que la caja aguante** que para que el papel diga que se gana dinero» ·
> «Es también la cifra que explica **por qué el equilibrio de caja pide más tickets que el equilibrio contable**»

`plan-financiero!Punto de Equilibrio` es tajante: contable **155,65** tickets/día, caja **148,87**. **La
caja pide MENOS**, porque la amortización que se quita (16.090 €) pesa más que el principal que se suma
(7.979 €). El cap. 18 lo escribe bien y hasta lo explica; los otros tres sitios dicen lo contrario, y el
business plan lo convierte en el argumento de su epígrafe. Un analista de riesgos de banco lo desmonta
restando dos filas.

**Fix (cap. 19, pie de la tabla «El servicio de la deuda año a año»):** «Sólo los intereses son gasto de la
cuenta de resultados; el principal devuelto sale de la caja y no aparece en el resultado. **En este caso el
equilibrio de caja queda por debajo del contable, porque la amortización que se descuenta pesa más que el
principal que se añade.**»
**Fix (business plan §5), tres frases:** «El equilibrio contable —el punto en el que el resultado deja de
ser negativo— **pide más tickets al día que el equilibrio de caja: 155,6 frente a 148,9**. El equilibrio de
caja, que es el que de verdad importa mientras hay un préstamo abierto, exige 148,9 tickets al día.» ·
«La diferencia entre los dos no es un error de cálculo: **el contable carga la amortización, que no se paga,
y el de caja carga la devolución de principal, que sí; en este plan la primera pesa más que la segunda**.» ·
«Es también la cifra que explica **por qué el equilibrio de caja no coincide con el contable**: esa cuota
sale de caja, mes tras mes, gane o no gane el negocio ese mes concreto.»

### A6 · ALTA · guía cap. 19 · `txt/cap19_b2.txt` — afirmación normativa falsa
> «La segunda obligación es la de ofrecer al menos una referencia de bebida en envase reutilizable […]
> Y aquí sí conviene decirlo sin rodeos: **esa fecha ya ha llegado y la obligación ya es exigible**, así que
> no es un «para cuando abras» sino un «para cuando factures».»

Falso. El art. 9.4.a).1.º del RD 1055/2022 fija **el 1 de enero de 2027** para los establecimientos de
**menos de 120 m²** (PA-30c, literal verificado). El caso son 90 m², y **hoy es 10 de septiembre de 2026**.
Lo que ya está en vigor desde 2025 son los tramos de 300 m² en adelante, que no le tocan a una pastelería.
El propio **anexo del libro lo desmiente dos veces**: «para una superficie comercial inferior a 120 metros
cuadrados […] la obligación pasa de futura a presente **el 1 de enero de 2027**» y la fila «Bebida en
envase reutilizable por debajo del umbral de superficie | **01-01-2027**». Es exactamente el tipo de
afirmación que la lista negra del §5 persigue, y encima contradice al propio documento.

**Fix:** «Y aquí conviene la fecha exacta: **para una superficie de menos de 120 m² esa obligación empieza
el 1 de enero de 2027**, así que hoy todavía no te aplica —pero llega antes de tu primer aniversario, y el
proveedor de bebida hay que elegirlo sabiéndolo.»

### A7 · ALTA · guía cap. 12 · `txt/cap12_b2.txt` — la regla central del pack se apoya en una equivalencia falsa
> «la misma fuente sitúa también el margen bruto objetivo de una pastelería artesanal en **una banda sobre
> coste** (Pastelería Para Todos, 2026), **coherente con el objetivo que este libro te pide trabajar**.»

**PS-55** dice literalmente «margen bruto objetivo […] **65-70 % sobre coste**» y **PS-56** dice «food cost
[…] **por debajo del 30-35 % del PVP**». **No son la misma regla dicha dos veces**: 65-70 % *sobre coste*
es un margen comercial que equivale a un food cost del **59-61 %**, no del 30-35 %. El libro trabaja con
32 % de food cost ⇒ **68 % sobre PVP**. Afirmar que la banda «sobre coste» es «coherente» con ese 68 % es
falso por un factor de casi dos, y es justamente la frase con la que el capítulo cierra su tesis. La hoja
`carta!Parámetros!A24` arrastra el mismo problema: cita «PS-55 + PS-56» para sostener «30-35 % de food cost
= 65-70 % de margen bruto», que sólo se deduce de PS-56.

**Fix:** «Y ya que estamos con la regla del sector: la misma fuente da un food cost objetivo del **30-35 %
del precio de venta**, que es exactamente el 32 % con el que trabaja este libro. Cuidado con las fuentes que
publican «65-70 % de margen» sin decir sobre qué: **sobre precio de venta** equivale a ese 30-35 % de food
cost, pero **sobre coste** sería otra cosa y mucho más floja. Antes de comparar tu margen con el de nadie,
pregunta sobre qué base está calculado.»
**Fix (xlsx):** la nota de `carta!Parámetros!A24` debe citar **sólo PS-56** para la equivalencia, y PS-55
con el aviso «declarado sobre coste por la fuente».

### A8 · ALTA · guía caps. 2 y 15 · `estacionalidad-y-picos.xlsx`
> cap. 2: «**Enero | 1,18 | 31.683 € | 9,8 %**» · cap. 15: «**Reyes | 5 | 31.500 € | 9,8 %**»

Las dos tablas se publican en el mismo libro y **las dos declaran el mismo 9,8 % del año**. Si Reyes son
31.500 € en cinco días y enero entero son 31.683 €, **los otros 26 días de enero facturan 183 €**, siete
euros al día, en una pastelería que hace 1.074 € en un día medio. El modelo no se sostiene: el «producto
estrella» de Reyes son 420 roscones/día a 15 € sin IVA (2.100 en cinco días), mientras el mix de la carta
asigna al roscón un 1,2 % de 142.800 piezas al año = **1.714 unidades en todo el ejercicio**. La misma
incoherencia, más pequeña, en Todos los Santos (1.560 buñuelos en 3 días contra 1.428/año) y Semana Santa
(1.920 torrijas en 8 días contra 1.856/año). Y de ahí sale, ya en prosa, «un día de Reyes factura 5,9 veces
lo que factura un día normal», que compara la venta de **una sola referencia** contra la venta **total** de
un día medio.

**Fix (xlsx, `Calendario de 6 Picos`):** bajar `K6` (uds/día en campaña de Reyes) de **420** a un valor
compatible con el mix de la carta y con las 2.856 piezas/día de la hoja de capacidad —**160 uds/día**
(800 roscones en la campaña, el 47 % de las 1.714 del año) deja Reyes en 12.000 € y en el **3,7 % del año**,
que sí cabe dentro del 9,8 % de enero. Alternativa igual de válida: subir el mix del roscón en la carta.
Lo que no puede quedarse es la foto actual. Después hay que regenerar cap. 2, cap. 15, bonus 5, bonus 9 y
business plan §2, y revisar la frase «5,9 veces lo que factura un día normal».

### A9 · MEDIA · guía cap. 17 · `txt/cap17_b1.txt`
> «el peso del suministro a otras tiendas sobre el total de las ventas es del 5 %, **muy lejos del techo del
> 25 % del volumen anual** que marca la primera vía»

El 25 % del art. 3.2.a) se mide sobre el **volumen anual de alimentos comercializados** —así lo escribe
bien el cap. 9—, y aquí se compara contra un **5 % del mix en euros**. No es lo mismo: el B2B vende más
barato por kilo, así que un 5 % en euros puede ser un 8 % en volumen. La hoja `checklist-legal!Suministro a
Otros Minoristas` lo calcula bien, en kilos: **4,1 %**. El capítulo publica el número equivocado para el
umbral que analiza.

**Fix:** «el peso del suministro a otras tiendas es del 5 % de las ventas en euros y del **4,1 % en kilos**
—que es la magnitud que mide el artículo—, muy lejos del techo del 25 % del volumen anual que marca la
primera vía. Ojo con la unidad: el 25 % es de volumen, no de facturación, y el B2B siempre pesa más en
kilos que en euros.»

### A10 · MEDIA · guía cap. 12 · `txt/cap12_b2.txt`
> «ese food cost te va a salir muy por debajo de lo que pide la regla del sector para una pastelería
> artesanal, que fija el objetivo de coste de ingredientes **por debajo de un porcentaje sobre el precio de
> venta** (Pastelería Para Todos, 2026)»

Un párrafo que anuncia una regla y no la dice. La cifra existe, es citable y **ya está escrita dos párrafos
antes en el mismo capítulo** («el food cost objetivo es del 32 %») y en la hoja («La regla del sector es
30-35 %», `Mix y Ticket Medio!I46`). El hueco no protege de nada y deja la frase coja.

**Fix:** «…que fija el objetivo de coste de ingredientes **entre el 30 % y el 35 % del precio de venta**
(Pastelería Para Todos, 2026).»

### A11 · MEDIA · bonus, decisión 6 · `BONUS…/cap06_b1.txt`
> «El art. 9.3 del RD 1021/2022 […] fija un máximo de **24 horas de vida útil**»

D11 y la propia hoja lo prohíben con todas las letras: `carta!Parámetros!G30` dice «**No es una vida útil:
es un plazo legal**», y el libro 4 devuelve las dos salidas por separado justamente para que no se
confundan. Llamarlo «vida útil» invita al lector a poner 24 h en su APPCC como vida útil declarada de todo
lo relleno, que es lo contrario de lo que el pack construye.

**Fix:** «fija un **plazo legal de consumo de 24 horas desde la elaboración** —que no es la vida útil, que
la declaras tú en tu APPCC—, con un techo de temperatura de 8 °C que baja a 4 °C cuando concurre esa fila»

### A12 · MEDIA · bonus, decisión 3 · `BONUS…/cap03_b1.txt`
> «si alguna de tus tartas por encargo lleva licor por encima del **1,2 % en volumen** —el umbral a partir
> del cual hay que declarar el grado alcohólico en producto no envasado—, esa declaración es obligatoria
> conforme al RD 126/2015»

El art. 4.1.d) del RD 126/2015 dice, literal (PA-21): «El grado alcohólico **en las bebidas** con una
graduación superior en volumen al 1,2 por 100». **Es una obligación sobre bebidas, no sobre tartas.**
Extenderla a un producto sólido es una inferencia que la verificación legal no respalda, y la regla de la
casa es que lo NO VERIFICADO no se afirma con artículo delante.

**Fix:** «Y si alguna de tus tartas por encargo lleva licor, el alcohol es un ingrediente que va declarado
como cualquier otro; **el umbral del 1,2 % en volumen del art. 4.1.d) del RD 126/2015 obliga a declarar el
grado alcohólico en las BEBIDAS, no en la pastelería**, así que no lo apliques por analogía sin
preguntar.»

### A13 · MEDIA · guía cap. 21 (anexo) · `txt/cap21_b1.txt`
> prosa: «El RD 3484/2000 […] está **derogado por el mismo RD 1021/2022**, de 2022.»
> tabla: «RD 3484/2000 | Comidas preparadas | **DEROGADO; lo sustituye el art. 30 del RD 1086/2020**»

El anexo da dos versiones distintas del mismo hecho, y **ninguna de las dos está en la verificación legal
del 10-sep**, que no abrió la disposición derogatoria del RD 3484/2000. Lo mismo, más suave, con «el
RD 1420/2006 […] su contenido quedó absorbido por el RD 1021/2022»: la derogación está fuera de duda, pero
la norma que lo sustituye no se verificó. En un anexo cuyo valor es la trazabilidad, atribuir mal una
derogación es el peor sitio para fallar.

**Fix (prosa):** «El RD 3484/2000, sobre normas de higiene de comidas preparadas y temperaturas, **está
derogado**. Lo que regula hoy la materia en un comercio minorista es el RD 1021/2022, y en la zona de
degustación, el art. 30 del RD 1086/2020.» **Fix (tabla):** «DEROGADO; la materia la regulan hoy el
RD 1021/2022 y el art. 30 del RD 1086/2020». Y en el bullet del RD 1420/2006, sustituir «su contenido quedó
absorbido por el RD 1021/2022» por «está derogado; la congelación preventiva del parásito se rige hoy por
el RD 1021/2022».

### A14 · MEDIA · guía cap. 8 y tablas de dotación · `checklist-equipamiento` + `calculadora-capex`
> «Una batidora amasadora planetaria **Sammic BP-20** de veinte litros arranca desde 595,04 €
> (Batidora amasadora planetaria **BE-20** Sammic — HostelShopping, 2026)»

El modelo y su fuente no coinciden **en la misma frase**. El id PS-81 tiene el mismo defecto: `dato` dice
BP-20 y `fuente_titulo` dice BE-20. La gama de planetarias de Sammic es **BE-**; «BP-20» no existe. El
número de modelo viaja además a la columna «Modelo» de la tabla de dotación del cap. 8 y a la línea del
CAPEX del cap. 4, así que el lector que vaya a pedir presupuesto con ese código no encuentra la máquina.

**Fix (xlsx `checklist-equipamiento!Equipamiento`, columna Modelo, y prosa del cap. 8):** **BE-20** en los
tres sitios. Y corregir `dato` de PS-81 en `guias-v2-research-sector.json`.

### A15 · MEDIA · guía cap. 6 · `txt/cap06_b1.txt`
> «el coste total de la vía de traspaso es de 144.250 €, frente a los 237.700 € que sale la vía de obra
> nueva […] La diferencia entre las dos vías […] es de -93.450 €»

El lector no puede reconstruir ninguno de los dos números con lo que el capítulo le da. Le dan 43.000 € de
traspaso y 1.250 €/mes de renta: 43.000 + 1.250 × 60 = 118.000, no 143.000. **Faltan los 25.000 € de
«inversión de adecuación» que la hoja carga al traspaso** y, sobre todo, falta el supuesto que produce los
93.450 € de diferencia: la hoja carga a la obra nueva **el CAPEX comparable entero (160.900 €, con todo el
equipamiento dentro)** y al traspaso sólo 25.000 €, es decir, **da por hecho que el traspaso viene con el
obrador montado**. Es un supuesto razonable y está en la nota del xlsx, pero **no está en el libro**, y sin
él el veredicto «Sale mejor el TRASPASO» es una cifra sin hipótesis, que es justo lo que el cap. 4 denuncia.

**Fix:** añadir tras «…con una renta mensual de 1.250 €»: «A ese precio hay que sumarle **25.000 € de
adecuación** —pintura, rótulo, vitrina y la máquina que falte—, y el supuesto que de verdad manda en la
comparación: **el traspaso se contabiliza con el obrador ya montado, mientras que la obra nueva carga el
equipamiento entero (160.900 €)**. Si el local que traspasas viene vacío, esta cuenta cambia de signo:
compruébalo antes de darle la razón a la hoja.»

### A16 · MEDIA · guía cap. 12 · guion (tabla «De dónde sale el coste hora de obrador»)
> `| Horas anuales de contrato | 1.780,00 |` · `| Horas productivas sobre la jornada | 0,85 |` ·
> `| Horas productivas del obrador al año | 3.782,50 | calculado |`

1.780 × 0,85 = **1.513**, no 3.782,50. Falta la fila que cierra la cadena: **las 2,5 jornadas equivalentes
de obrador** (Jefe 1,0 + Pastelero 1,0 + Ayudante 0,5), que es lo que multiplica. La tabla se llama «De
dónde sale el coste hora de obrador, parámetro a parámetro» y es el único sitio donde el lector puede
comprobar los 17,94 €; tal como está, la comprobación falla.

**Fix (guion):** añadir la fila `carta-de-apertura-y-escandallo.xlsx!Parámetros!B9` («TOTAL OBRADOR» = 2,5
jornadas) y la fila `!F9` (coste de empresa anual del obrador = 67.850 €) delante de las horas productivas.
Con esas dos, la cadena 2,5 × 1.780 × 0,85 = 3.782,5 y 67.850 / 3.782,5 = 17,94 € se sigue sin salir de la
tabla.

### A17 · MEDIA · guía cap. 5 · `txt/cap05_b1.txt`
> «El segundo número que hay que llevar apuntado es el caudal de la campana extractora, que en el caso
> modelado **es de 1.360**.»

Sin unidad. Son **1.360 m³/h** (`capacidad!Parámetros!B21`), y el propio párrafo dice que es «el número que
hay que llevar apuntado» a la visita del local. Un caudal sin unidad no sirve para nada delante de un
instalador.

**Fix:** «…que en el caso modelado es de **1.360 m³/h**.»

### A18 · MEDIA · `estacionalidad-y-picos!Peso sobre el Año` (columna de incremental)
> cap. 15: «la facturación incremental —41.163 €— es la que se habría perdido si el negocio hubiera vendido
> a ritmo normal esos mismos días»

Con esa definición, Reyes tendría que descontar 5 días a 1.074 € (5.370 €) y quedarse en 26.130 €; la hoja
da **31.500 €, exactamente igual que el total**, es decir, base cero. San Valentín, en cambio, sí descuenta
—pero una base de 181 €/día, no de 1.074 €—. Las dos lecturas conviven en la misma tabla del capítulo, y
la prosa presenta la incremental como el número con el que se decide el refuerzo.

**Fix:** o se recalcula la incremental de todas las campañas sobre la venta del día medio del año
(1.073,99 €), o el pie de la tabla dice qué base usa: «la incremental descuenta **la venta del producto
estrella fuera de campaña** (`J` del Calendario), no la venta total de un día medio: en Reyes ese producto
no se vende el resto del año, y por eso su incremental coincide con su total».

### A19 · BAJA · bonus, decisión 12 · `BONUS…/cap12_b1.txt`
> «Vender producto con defecto […] con dos exclusiones: no aplica a frutas y hortalizas ni a conservas
> abombadas, **y en ningún caso puede dificultar la lectura de la información obligatoria del etiquetado**»

La coletilla final no está en el literal verificado del art. 17 (PA-20), que se limita a las dos
exclusiones. Puede estar en el articulado completo, pero la verificación no la recoge y aquí se escribe con
la norma delante.

**Fix:** cortar en «…ni a conservas abombadas (RD 1021/2022, art. 17, texto consolidado; comprobado el 10 de
septiembre de 2026)».

---

## 3. Lente B — COHERENCIA Y NO-SOLAPE

### B1 · ALTA · guía, los 21 capítulos · guion + `carta-de-apertura-y-escandallo`
La SPEC vende la **hoja de decisión de huevo** como el diferencial que «no existe en ningún producto del
catálogo ni de la competencia» (§2.2 libro 4), el objetivo del cap. 12 es «Qué vendes, a cuánto, y **con qué
vía legal de huevo**», y PA-14 está verificado a nivel A con sus tres vías literales. Pues bien:

- **«ovoproducto» aparece 0 veces en los 21 capítulos.** «huevo crudo», 0. «70 °C», 0. «art. 9.1», 0.
- «huevo» sale **6 veces**, y ninguna explica nada: dos son punteros («la hoja de decisión de huevo y
  temperatura de este pack»), una es el título de una tabla y tres están en el anexo hablando de una norma
  derogada.
- La única tabla que imprime esa hoja (cap. 17) **omite justamente la columna D, «Vía legal del huevo»**, y
  también «Cuál manda» y «Vida útil declarada por ti» — las tres columnas que D11 exige como salidas
  separadas. Se quedan las dos que ya se explican en otros capítulos.
- El bonus sí lo menciona (decisión 11, tabla de recuentos), pero el libro de 104 páginas no.

Resultado: **el comprador abre el xlsx y encuentra una hoja que el libro no le ha enseñado a usar**, y el
capítulo que más se vendió en la SPEC no cumple su objetivo.

**Fix (texto, cap. 12 o cap. 10, un epígrafe nuevo de ~350 palabras):** «**Las tres vías del huevo, y por
qué decides una por elaboración.** Con huevo crudo sólo hay tres caminos, y el art. 9 del RD 1021/2022 no
deja más (comprobado el 10 de septiembre de 2026): **70 °C durante 2 segundos en el centro del producto**,
o cualquier combinación de efecto equivalente (art. 9.1.a); **63 °C durante 20 segundos con consumo
inmediato** (art. 9.1.b), que es la vía de la tortilla y del huevo frito y **no la tuya**; o **sustituir el
huevo crudo por ovoproducto** de establecimiento autorizado (art. 9.2). Todo lo que no pase por una de las
tres no se hace con huevo crudo. Y la vía que elijas arrastra consecuencias: lo elaborado por la vía de los
70 °C **que no sea estable a temperatura ambiente**, y todo lo hecho con ovoproducto, se conserva a 8 °C o
menos y se consume en **24 horas** desde su elaboración, **con registro de fecha y hora** (art. 9.3). Si
además es producto de pastelería relleno, le aplica también la fila 9 del art. 4.1 —4 °C o menos— y manda
el más bajo de los dos. Por eso el libro 4 devuelve dos salidas separadas y no una: el **plazo legal**, que
lo fija el art. 9.3, y la **vida útil que declaras tú**, que la fijas en tu APPCC y que el real decreto no
establece.»
**Fix (guion, tabla del cap. 17):** añadir la columna `D` («Vía legal del huevo») y la `J` («Cuál manda»),
o al menos la `D`, que es la que da nombre a la hoja.

### B2 · ALTA · business plan §1 · `business-plan/cap01_b1.txt`
> «El resultado neto de los tres años y el margen neto de ese año de crucero **están calculados, partida a
> partida, en el cuadro de la previsión financiera** que acompaña a este resumen» ·
> «sitúa en un rango porcentual la rentabilidad neta […]; **no repetimos esa cifra**» ·
> «Cuándo llega este negocio al punto de equilibrio y con cuánta holgura lo hace es un dato que también
> vive en esa misma sección financiera del pack: **no una frase que se pueda resumir sin verla**»

**Tres párrafos seguidos del RESUMEN EJECUTIVO que se niegan a dar el resultado neto, el margen y el punto
de equilibrio.** Es el documento «en el formato que pide un banco» y el epígrafe se llama «El proyecto en
una página»: son exactamente las tres cifras que un analista lee antes de pasar de página. Las tres existen
y están calculadas (27.836 €, 8,6 %, 148,9 tickets/día, 22,9 % de holgura). La instrucción de no repetir
cifras entre bloques se ha aplicado al único sitio donde repetirlas es obligatorio.

**Fix:** «La previsión a tres años cierra el año de crucero con **322.198 € de ingresos**, un **resultado
neto de 27.836 €** y un **margen neto del 8,6 %**; el año uno, todavía en rampa, cierra en **5.447 €**. El
negocio cubre su equilibrio de caja con **148,9 tickets al día** y el plan prevé 183, una **holgura del
22,9 %**. El cuadro de la previsión financiera desglosa cómo se llega hasta ahí, partida a partida.» ·
«El gerente de Pastelerías Pomar sitúa la rentabilidad neta de una pastelería que va bien **entre el 8 % y
el 12 %**: el 8,6 % de este plan cae en el tramo bajo de esa banda, que es donde tiene que caer un caso
conservador.» · borrar el tercer párrafo, que ya está dicho en el primero.

### B3 · ALTA · bonus 9 y business plan §6 · `BONUS…/cap09_b1.txt`, `business-plan/cap06_b1.txt`
> bonus 9: «Dentro de esos doce hitos, el que más veces desplaza la fecha final **no suele ser la obra ni el
> papeleo: es el plazo de entrega del equipamiento**»
> business plan §6: «su plazo de entrega es el que **gobierna la fecha real de apertura, no la obra ni el
> papeleo**»

Las dos frases contradicen la tabla que **el propio bonus 9 imprime tres párrafos más abajo**: «H6 · Pedido
y entrega del equipamiento · **Holgura 1,0 · ¿Ruta crítica? No**», y el pie que la remata: «El único hito
con holgura del caso modelado es el pedido de equipamiento, porque va en paralelo a la obra: **todos los
demás son ruta crítica**». Es decir, en este caso la obra y el papeleo sí gobiernan y el equipamiento es lo
único que no. El origen es el mismo bug de la causa 2: los dos redactores recibieron «Cámara de
fermentación controlada (roll-in)» como valor de «Margen del plazo crítico, en semanas» y construyeron una
tesis sobre un texto.

**Fix (bonus 9):** «Dentro de esos doce hitos, la obra y el trámite de actividad son los que mandan: son
ruta crítica y cualquier día que se muevan mueve la apertura. **El equipamiento es el único hito con
holgura —un mes— y sólo porque se pide en paralelo a la obra**; el plazo más largo de las líneas críticas
son **nueve semanas** y lo marca la cámara de fermentación controlada, así que se pide en cuanto está el
proyecto, no cuando termina el tabique. Si esperas, se convierte en ruta crítica él también.»
**Fix (business plan §6):** «De todo el listado, el elemento con el plazo más largo es la cámara de
fermentación controlada, el roll-in: **nueve semanas**, y es la primera que hay que encargar. **En este
cronograma no gobierna la apertura —es el único hito con holgura— precisamente porque se pide en paralelo a
la obra**; el día que se pida tarde, pasa a gobernarla.»

### B4 · MEDIA · bonus, decisión 7 · `BONUS…/cap07_b1.txt`
> criterio: «¿qué le pasa al punto muerto si quito ese canal? **Si el punto muerto baja al quitarlo, el
> canal está restando** […] y sostenerlo **no compensa** el volumen que trae.»
> celda: «con todos los canales activos —23.337,56 €— y sin el de suministro a otras tiendas —23.018,22 €—.
> **Como el punto muerto sube al meter el canal**, este caso concreto queda en el filo […] **de ahí sale la
> recomendación de la opción B**»

La decisión aplica su propio criterio, obtiene el veredicto «resta» y recomienda lo contrario sin decir por
qué. Y unas líneas antes ya había escrito la regla al revés: «Esa recomendación cambia si el punto muerto
sin el canal resulta más alto que con él —entonces el canal aporta de verdad». Aquí es más bajo.

**Fix:** «Como el punto muerto sube al meter el canal —de 23.018 € a 23.338 € al mes—, **por el criterio de
arriba este canal resta: te obliga a facturar 320 € más cada mes para llegar al mismo cero**. Que la
recomendación siga siendo la opción B, y no la A, es por lo segundo que mide esta decisión y no por el
punto muerto: **el B2B llena horas muertas de obrador que ya estás pagando**, y con tope puesto ese uso de
capacidad compensa los 320 €. El día que el canal crezca sin tope, la cuenta cambia de signo.»

### B5 · MEDIA · guía cap. 15 · guion (dos tablas del mismo capítulo)
> tabla 2: «Reyes […] **Personas de refuerzo necesarias | 4**» · «San Valentín […] **1**» · «Todos los Santos […] **1**»
> tabla 3: «Reyes | **Personas de refuerzo | 3**» · «San Valentín | **0**» · «Todos los Santos | **2**»

**Tres de las seis campañas dan dos números distintos en dos tablas separadas por cuatro párrafos**, y la
prosa no dice ni una palabra. El xlsx sí lo explica: la hoja «Refuerzo y Tesorería» tiene una columna
«**¿Cubre el refuerzo?**» (No / No / Sí…) y una nota por campaña —«El refuerzo sale a CERO personas y CERO
euros a propósito: la persona que hace falta ya está en la plantilla base»—. El guion imprime las dos
cifras y **deja fuera precisamente la columna que las reconcilia**.

**Fix (guion, tabla «Lo que cuesta cada campaña y lo que inmoviliza»):** añadir las columnas `G`
(«Personas necesarias») y `H` («¿Cubre el refuerzo?») de `estacionalidad-y-picos!Refuerzo y Tesorería`, y
cambiar el pie por: «Las personas de refuerzo son las que **contratas**; las necesarias son las que pediría
el déficit. Cuando no coinciden es una decisión: en San Valentín se cubre con la plantilla base y en Reyes
se acepta quedarse una persona corto y compensar adelantando producción.»

### B6 · MEDIA · guía, índice y cuerpo · `documentos.py` / guion — incumple D28
> portada: «**Veinte capítulos**, un anexo normativo fechado…»
> índice: «**21.** Anexo normativo, actualizado a 10 de septiembre de 2026 — **Anexo normativo, actualizado
> a 10 de septiembre de 2026**»
> cuerpo: «## **21.** Anexo normativo, actualizado a 10 de septiembre de 2026»

D28 es explícita: el anexo «va como entrada 21 de `CAPITULOS` para que el pipeline lo escriba, pero **no se
numera como capítulo** en el índice ni en la landing». Va numerado en los dos sitios, y encima **su resumen
de índice repite el título literal** porque el guion no le puso `resumen_indice`. La portada dice veinte y
el índice cuenta veintiuno: es lo primero que ve el comprador.

**Fix (guion):** dar al anexo `'resumen_indice': 'qué norma sigue vigente y desde cuándo, las cuatro fechas
que ya sabemos que se mueven, las cinco normas muertas que la SERP sigue citando y cómo comprobar la ficha
de vigencia del BOE en un minuto'`. **Fix (`documentos.py` o guion):** marcar la entrada con una clave del
tipo `'sin_numerar': True` para que el índice y el `<h2>` impriman «Anexo normativo · actualizado a 10 de
septiembre de 2026» sin ordinal. Si no da tiempo a tocar código, el mínimo es el `resumen_indice`.

### B7 · MEDIA · los tres documentos · §6 de la SPEC
La SPEC manda «equivalencia en la **PRIMERA** mención; luego, el término de España», y el propio cap. 1 se
lo promete al lector: «a partir de ahí se usa siempre la forma española». Medido:

| Glosa | guía | bonus | b. plan | total |
|---|---|---|---|---|
| obrador (taller o laboratorio) | 21 | 8 | 6 | **35** |
| pastelería (repostería) | 13 | 6 | 4 | **23** |
| vitrina (exhibidor) | 11 | 4 | 5 | **20** |
| encargo/encargos (pedido/pedidos) | 10 | 5 | 4 | **19** |
| tarta/tartas (pastel o torta) | 7 | 5 | 4 | **16** |
| coste/costes (costo/costos) | 5 | 3 | 4 | **12** |
| escandallo (costeo) | 6 | 2 | 2 | **10** |
| **TOTAL** | **73** | **33** | **29** | **135** |

Ciento treinta y cinco paréntesis después de la primera mención, en un documento que anuncia que no los va
a poner. Cansa la lectura y hace que el texto suene a traducción automática.

**Fix (mecánico, seguro):** dejar la primera aparición de cada glosa en el cap. 1 de la guía, en la
decisión 1 del bonus y en el §1 del business plan, y **sustituir todas las demás por el término a secas**.
Es un `replace` por documento sobre los `.txt`, con la única precaución de no tocar el párrafo del
glosario del cap. 1 ni la tabla de vocabulario.

### B8 · MEDIA · guía cap. 11 · `txt/cap11_b1.txt` — incumple D29
> «el directorio de proveedores de hostelería del grupo, **Hosply**, es el sitio donde continuar esa
> búsqueda.»

D29 pide que Hosply.pro se enlace **con UTM** desde el cap. 11, y por eso se verificó su TLS el 10-sep. Lo
que hay es el nombre de la marca sin dominio, sin URL y sin UTM: en un PDF, «Hosply» no lleva a ninguna
parte y no se puede medir. Las nueve URL de los proveedores externos sí están completas en la tabla de al
lado, así que el único enlace del grupo es el que falta.

**Fix:** «…el directorio de proveedores de hostelería del grupo, **Hosply**
(`https://hosply.pro/?utm_source=guia-pasteleria&utm_medium=libro&utm_content=cap11`), es el sitio donde
continuar esa búsqueda.»

### B9 · MEDIA · business plan §4 · `business-plan/cap04_b1.txt`
> «El Dependiente Vitrina que abre la persiana el día de la apertura **se suma justo entonces, no antes** […]
> El Ayudante y el segundo Dependiente Vitrina **llegan después**, cuando el volumen de venta ya sostiene
> esas horas. **Por eso el primer año no cuesta lo mismo que el de crucero**»

El P&L que va cuatro epígrafes más abajo dice «Personal (nóminas y Seguridad Social) | **92.776 € | 92.776 €
| 92.776 €**»: el año uno cuesta **exactamente lo mismo** que el de crucero. Y el propio párrafo se
desmiente en su última frase: «se paga la plantilla completa antes de que la plantilla completa esté
generando el ritmo de venta». Un banco que compare el relato con la tabla ve que el plan de contratación
escalonado no está modelado.

**Fix:** «No toda la plantilla hace falta desde el primer día, pero **este plan la presupuesta entera desde
el mes uno a propósito**: es el supuesto conservador, y por eso el coste de personal es el mismo en los tres
años del cuadro. Si escalonas las altas —el Ayudante y el segundo Dependiente Vitrina cuando el volumen los
sostenga— el año uno mejora, y ese margen se queda como colchón en vez de como previsión.»

### B10 · MEDIA · bonus, decisión 4 · `BONUS…/cap04_b1.txt`
> «la variante de punto caliente sale a **22.456 € de inversión**, frente a los 66.980 € del caso base con
> obrador»

Son 22.456 € **de equipamiento**, no de inversión: la columna es «Inversión de referencia de esa variante»
de la hoja de variantes del **libro 7**, que «no incluye obra, licencias ni fondo de maniobra». La
inversión de apertura de esa misma variante está publicada en el cap. 1 de la guía y son **85.997 €**. Un
lector que lea los dos documentos ve la misma variante a dos precios que se diferencian por cuatro.

**Fix:** «la variante de punto caliente pide **22.456 € de equipamiento**, frente a los 66.980 € del caso
base con obrador — y **85.997 € de inversión de apertura completa**, con obra y licencias dentro, contra
los 165.800 € del caso base.»

### B11 · MEDIA · guía cap. 1 contra su propia tabla y contra el bonus 10 · `txt/cap01_b1.txt`
> «De las que sí tienen rango, y **siempre en cualitativo** porque son estimaciones de terceros sin desglose
> verificable línea a línea: el obrador en casa […] maneja un mínimo viable modesto y un arranque económico
> que crece bastante…»

Tres líneas después, **la tabla del mismo capítulo publica los números** («Obrador en casa | Publicado
mínimo 3.000 € | Publicado máximo 30.000 €», y así ocho filas), y el **bonus 10 los da en prosa**: «una
inversión de referencia de tres mil a cinco mil euros para el mínimo viable […] y de cinco mil a ocho mil
[…] frente a treinta mil euros o más». La política editorial que el capítulo anuncia no la cumple ni él
mismo. Y la perífrasis («modesto», «crece bastante») deja al lector sin dato y sin criterio.

**Fix:** «De las que sí tienen rango, y siempre **con la etiqueta de lo que son —estimaciones de terceros
sin desglose verificable línea a línea, no presupuestos—**: el obrador en casa con venta directa, según
«Cómo montar un negocio de pastelería: guía 2026 — Pastelería Para Todos» (2026-07-12), se mueve entre
**3.000 € y 30.000 €** según se monte con lo mínimo o con equipamiento profesional completo;…»

### B12 · MEDIA · guía cap. 18 y business plan §5 · guion (tabla del P&L)
Dos defectos en la misma tabla, la que más se mira del pack:

1. **La fila «Personal (nóminas y Seguridad Social)» es la única sin porcentaje** en la columna «Parte de
   las ventas del año 2». Todas las demás lo llevan. El número existe —**28,8 %**— y el business plan lo
   publica en prosa. Es justo la partida que los dos capítulos declaran «la más pesada».
2. **Las filas «IVA soportado de los costes variables» y «…de los costes fijos» van entre TOTAL COSTES
   FIJOS y RESULTADO ANTES DE IMPUESTOS**, y no participan en la resta (219.095 − 186.346 = 32.749). Un
   lector que las sume obtiene otro resultado. En una cuenta que declara «todas las cifras van sin IVA»,
   esas dos líneas no pintan nada ahí.

**Fix (guion):** rellenar la celda de porcentaje de la fila de personal con
`plan-financiero!PyG 3 Años` (o calcularla) y **mover las dos filas de IVA soportado detrás del resultado**,
bajo un rótulo «Memoria de IVA (no afecta al resultado)», como ya hace la hoja de tesorería.

### B13 · MEDIA · business plan §5 · guion (tabla de tesorería)
> `| Compras y coste de ventas (IVA incluido) | **-0 €** | -5.686 € | …`

El mes 1 factura 17.536 € y compra **cero**. Además el importe se imprime como «**-0 €**», con signo, que
es un artefacto de formato. En el documento que va al banco, un primer mes que vende sin comprar es lo
primero que un analista rodea con boli.

**Fix (xlsx `plan-financiero!Tesorería 12 meses`):** las compras del mes 1 no pueden ser cero — el pedido
de arranque está en el CAPEX («Packaging inicial», 2.500 €) pero la materia prima del primer mes no. Si el
supuesto es que se paga a 30 días, hay que decirlo en el pie: «Las compras del mes 1 salen a cero porque el
supuesto es pago a 30 días: la primera factura de materia prima se paga en el mes 2.» Y arreglar el
formato para que imprima «0 €», no «-0 €».

### B14 · BAJA · guía cap. 1 · `txt/cap01_b1.txt`
> «Y una advertencia más: **aquí no se usa «dulcería» como sinónimo de pastelería en ningún momento**,
> porque en México «dulcería» es la tienda de golosinas»

Es una regla editorial interna del taller contada al lector. La información útil (que en México «dulcería»
es otra cosa) cabe sin hablar del propio documento.

**Fix:** «Y un falso amigo que conviene tener fichado: en México **«dulcería» no es una pastelería, es la
tienda de golosinas**, así que si buscas proveedores o competencia con esa palabra vas a encontrar otro
negocio.»

---

## 4. Lente C — CALIDAD EDITORIAL

### C1 · MEDIA · PDF de la guía (p. 103) y del bonus (p. 37)
Los dos PDF tienen **una página en blanco antes de «Sobre el autor»**: sólo cabecera y pie (100 y 108
caracteres). En el `.md` se ve la causa: `---`, dos líneas en blanco, `---` (líneas 1800-1803 de la guía,
679-682 del bonus, 354-357 del business plan). Es una sección vacía que el ensamblador emite entre el
último capítulo y el cierre.

**Fix (`documentos.py`):** no emitir el separador de cierre cuando el bloque anterior ya terminó con uno.
Mientras tanto se puede borrar a mano el `---` sobrante de los tres `.md`, pero volverá en el siguiente
ensamblado.

### C2 · MEDIA · bonus 3 y business plan §3 · guion (tabla «Cómo queda la carta»)
> `| Margen ponderado medio de la carta (€) | **0** |  |`

El valor real es **0,0357 €** (`carta!Decisión de Surtido!E42`) y además cae en la columna «Referencias»,
no en la de euros: la fila 42 de la hoja tiene el número en `E`, que en las tres filas anteriores es el
recuento. Imprimir «0» como margen medio de la carta, justo debajo de tres filas que suman 1,07 €,
contradice la cifra que los dos documentos acaban de dar.

**Fix (guion):** en las dos tablas, acotar `'filas': (39, 41)` —las tres del recuento— y mover el margen
medio al pie: «El margen ponderado medio por referencia de la carta es de **0,04 €**; el de las cien piezas
vendidas con este mix, de **1,07 €**.»

### C3 · MEDIA · guía cap. 19 · `txt/cap19_b2.txt`
> «no cuenta como «precio anterior» a efectos de la regla de los treinta días **de la que hablamos más
> adelante en este mismo capítulo**»

No se habla de ella más adelante. El cap. 19 tiene cinco epígrafes y ninguno trata la regla de los 30 días;
en toda la guía sólo aparece una vez más, como fila de la tabla de vigencias del anexo. El reenvío deja al
lector buscando cuatro páginas.

**Fix:** «…no cuenta como «precio anterior» a efectos de la regla de los treinta días —**el art. 20.1 de la
Ley 7/1996, en la redacción del RD-ley 24/2021, que obliga a enseñar junto al precio rebajado el más bajo
que hayas aplicado en los treinta días anteriores, y que deja fuera expresamente lo que rebajes para no
tirar producto próximo a caducar** (comprobado el 10 de septiembre de 2026).»

### C4 · MEDIA · los tres documentos
Muletillas medidas sobre 55.874 palabras de la guía: «**de verdad**» 47 · «**conviene**» 46 · «**y aquí**»
23 · «**antes de firmar**» 24 · «**casi nadie**» 15 (de las cuales «casi nadie te cuenta/explica/dice» 7) ·
«el error más…» 5. En el bonus, sobre 16.549 palabras: «de verdad» 17, «conviene» 15, «la recomendación» 11.
Una cada 1.100 palabras de «de verdad» y la fórmula «esto es lo que casi nadie te cuenta» siete veces
convierten la voz en una plantilla.

**Fix:** pasada de poda con presupuesto: dejar «de verdad» en un máximo de 15 apariciones en la guía y 5 en
el bonus, «conviene» en 15 y 5, y **reescribir las 7 apariciones de «casi nadie te cuenta/explica»** dejando
como mucho dos. No hay sustitución mecánica: es una pasada de sonnet por bloque con la instrucción de
suprimir, no de reformular.

### C5 · MEDIA · guía cap. 7 · `txt/cap07_b1.txt`
Cinco «**ºC**» (indicador ordinal masculino, U+00BA) contra cuatro «**°C**» (signo de grado, U+00B0) **en el
mismo capítulo**: «+85 ºC a −40 ºC», «−18 ºC», «4 ºC o menos», «−18 ºC o menos» frente a los «4 °C» del
resto del libro. Las dos pasan el saneado WinAnsi, así que ningún gate lo ve, pero en pantalla se nota.

**Fix:** reemplazar las 5 ocurrencias de `ºC` por `°C` en `cap07_b1.txt`.

### C6 · BAJA · business plan §5 · `business-plan/cap05_b1.txt`
> «sitúa unos costes fijos de 5.000 € al mes con **una facturación de equilibrio de 7200 €/mes de
> facturación de equilibrio**»

Frase duplicada y, de paso, el único millar del pack sin separador («7200» en vez de «7.200»).

**Fix:** «sitúa unos costes fijos de 5.000 € al mes con una facturación de equilibrio de unos 7.200 € al
mes».

### C7 · BAJA · bonus 10 · `BONUS…/cap10_b1.txt`
> «el ejemplo usa 12 metros útiles con **un criterio propio de proporcionalidad de 8** y una referencia de
> 5,0 kilos por metro cuadrado útil y semana»

«De 8» de qué. Es el umbral de kilos por metro cuadrado útil y semana que la casa se pone; sin unidad, la
frase no se entiende.

**Fix:** «…con un criterio propio de proporcionalidad de **8 kilos por metro cuadrado útil y semana** —que
es de la casa, no de la norma— y un resultado de 5,0, holgadamente por debajo».

### C8 · BAJA · bonus 11 · `BONUS…/cap11_b1.txt`
> «quince van a vitrina refrigerada y quince a vitrina de ambiente, **y de esas, quince referencias quedan
> con un plazo legal de veinticuatro horas**»

El antecedente de «de esas» son las quince de ambiente, que son precisamente las que **no** tienen plazo.
Son las otras quince.

**Fix:** «quince van a vitrina refrigerada y quince a vitrina de ambiente, y **son esas quince refrigeradas
las que quedan** con un plazo legal de veinticuatro horas».

### C9 · BAJA · guía cap. 21 · `txt/cap21_b1.txt`
> «Van cinco, **con el año en que dejaron de tener validez** y con la norma que ocupó su lugar»

De las cinco, sólo el RD 202/2000 trae su año («derogado desde 2010»). De las otras cuatro se da el año de
la norma sucesora, no el de la derogación. La lista incumple lo que acaba de prometer.

**Fix:** o se añaden los años («RD 1254/1991 … derogado con efectos de **22 de diciembre de 2022**», que ya
está en la tabla de vigencias) o se cambia el anuncio por «Van cinco, con la norma que ocupó su lugar».

### C10 · BAJA · guía cap. 21 · `txt/cap21_b1.txt` + guion
Epígrafe «**Las cuatro fechas** que ya sabemos que se mueven» y, debajo, una tabla con **siete filas** (las
cuatro más las dos de accesibilidad y el desdoble de Verifactu).

**Fix:** titular el epígrafe «Las fechas que ya sabemos que se mueven» y abrirlo con «Son cuatro bloques y
siete fechas», o dejar la tabla en cuatro filas agrupando Verifactu y sacando accesibilidad.

### C11 · BAJA · bonus 1 · `BONUS…/cap01_b1.txt`
> «Si tu local vale **30 euros el metro cuadrado**, el obrador te cuesta 30 euros el metro cuadrado igual
> que la vitrina»

Cifra inventada para el ejemplo, y contradice el caso: el alquiler de La Clara son 14.400 €/año sobre 90 m²,
es decir **13,3 €/m² y mes**. En un pack donde todo sale de una celda, un número redondo suelto desentona.

**Fix:** «Si tu local vale **los 13,3 euros por metro cuadrado y mes del caso de este pack**, el obrador te
cuesta 13,3 euros el metro cuadrado igual que la vitrina».

### C12 · BAJA · guía cap. 8 · `txt/cap08_b1.txt`
> «**el gerente de una conocida pastelería española** lo resume con una frase…»

Es la misma fuente que el cap. 4 nombra («Matías Pomar, dueño de una pastelería en España») y que el cap. 13
identifica del todo («Pastelerías Pomar, en Mallorca, fundada en 1902»). Anonimizarla en el cap. 8 debilita
la cita sin ganar nada.

**Fix:** «Matías Pomar, de Pastelerías Pomar, lo resume con una frase…»

### C13 · BAJA · pie de página de los tres PDF
El pie imprime «AI Chef Pro · Cómo Montar una Pastelería | Página N | **Versión 1.0 · aichef.pro/guia-pasteleria-obrador**»
mientras la portada y el cierre llevan «Versión 1.0 · **septiembre de 2026** · aichef.pro/guia-pasteleria-obrador».
El pie es lo único que sobrevive a una fotocopia suelta y es donde más falta hace la fecha de edición.

**Fix (`documentos.py`, plantilla del pie):** «Versión 1.0 · septiembre de 2026 · aichef.pro/guia-pasteleria-obrador».

---

## 5. Lo que se comprobó y salió limpio

- **Gates de `documentos.py`:** los 23 en verde. 104 páginas contra 70 prometidas (guía), 38 contra 25
  (bonus), 19 contra 8 (business plan) — **`paginas-gate.py` pasaría con margen**. 0 no latinos en md/pdf/docx,
  0 fechas caducas, 0 fugas de taller, 0 citas en sintaxis de celda, 0 truncamientos, 0 erratas, 0 entidades
  HTML, 0 asteriscos impresos, paridad PDF↔DOCX al 0,88 %, A4 en las 104 páginas, `author='AI Chef Pro'`.
- **Solape:** 1 par en 46 bloques (§0). D33 funciona.
- **315 referencias `C()` resueltas contra celda:** 309 casan en tipo y en valor; las 6 malas son el par
  I52/I54 de A2. Ninguna referencia rota, ninguna celda vacía, ningún id de `sector` inexistente.
- **Cifras verificadas contra celda, una a una:** 90 m² / 45 · 22 · 12 · 11 y sus siete zonas · 476 y 480
  piezas/día y la holgura de 4 · 1.920 / 1.543 / 480 / 1.244 / 1.036 / 3.072 / 3.080 / 4.800 / 8.533 / 11.582 ·
  408 minutos productivos · 34 y 62 kW · 18 ítems y 8 eliminatorios de la ficha de visita · 165.800 /
  228.049 / 33.911 / 261.960 / 81.000 / 54.296 / 12.684 / 7.920 / 2.400 / 2.500 / 5.000 · 160.900 y el 17,4 %
  contra los 137.000 € de La Hostelera · 66.980 / 86.501 / 18.165 / 104.666 / 60.480 · las 22 líneas de
  dotación con sus precios y plazos · 38.600 € de media de los quince traspasos (sumados a mano) · 143.000 /
  232.900 / 144.250 / 237.700 / −93.450 · 30 referencias con su food cost, margen, mix y veredicto (27/1/2) ·
  1,0711 € de margen medio y el reparto 1,0279 / 0,012 / 0,0312 · 2,4557 € de PVP medio, 6,3848 y 5,8688 € de
  ticket, 2,6 piezas · 17,55 % y 20,33 % de food cost · 8,79 % de IVA medio · 375,60 € y 542,62 € de las
  treinta tandas · 63,3 % de mano de obra · 67.850 € y 17,94 €/h · los 6 grupos del convenio al céntimo y los
  cinco perfiles (21.418 / 20.654 / 8.943 / 9.371 ×2 = 69.756 → 92.776 con el 33 %) · 7.731,34 €/mes ·
  140 h y las 3,5 jornadas · 322.198 € y los doce coeficientes que suman 12,00 · 1.074 €/día · 2.856 y 1.656
  piezas de Reyes, 47,4 h · 3.795,51 € de refuerzo y 7.281,67 € inmovilizados · 45.108 € y 30.673 € del canal
  de encargos · 2,25 días de cobro y 66,5 % de contribución · 219.095 / 186.346 / 32.749 / 27.836 / 5.447 y el
  8,6 % · 155,6 y 148,9 tickets y el 22,9 % · 60.000 € al 6,2 %, 936,57 €, 3.671,10 € y la cobertura 3,37 ·
  59.622 € de saldo mínimo · 30 trámites y 8 autonómicos · 5 personas formadas, 240 €, 800 €, 120 €, 730 días ·
  15 referencias de vitrina refrigerada · 13 líneas sin proveedor · 2.700 € de pedido mínimo · 9 proveedores
  con URL · 11 hitos de ruta crítica y 8,5 meses. **Todas casan.**
- **Bloque legal, contrastado id a id con la verificación del 10-sep:** PA-01 y la comunicación no
  habilitante · PA-01b y la venta a distancia dentro de la definición de minorista · PA-02/02b/02c/02d con
  la puerta de entrada, las dos vías alternativas, los 50 km condicionados y la declaración responsable ·
  PA-03 con la obligación de inscribir cada sucursal · PA-03b con las tres condiciones del esquema · PA-04
  con el Decreto 26/2026, el 28-03-2026 y el transitorio al 28-03-2027 · PA-07 con el DB-HS 3 **descartado**
  y PA-07b con AE3/AE4 y el conducto propio · PA-10 con el APPCC simplificado y la persona responsable ·
  PA-11 con el RD 202/2000 derogado por el RD 109/2010 y el Cap. XII del 852/2004 · PA-12 con la fila 9 ·
  PA-13 con el descenso ininterrumpido, las tres fechas de etiqueta y la prohibición de recongelar · PA-15
  con los dos topes y las 24 h con registro de hora · PA-17 con «ELABORACIÓN PROPIA» voluntaria y el
  fraccionar-no-es-elaborar · PA-18 con el táper obligatorio del RD 1055/2022 · PA-20 con el rincón de los
  feos · PA-21 con los alérgenos de palabra y su registro escrito, el cartel por sección y el castellano ·
  PA-23 con los 20 mg/kg y la certificación como voluntaria · PA-27/27b con el envío nacional y el envasador
  de la caja · PA-28 con la información antes de la compra y la excepción de la fecha · PA-29/29b/29c/29d con
  las cinco letras, la e) valenciana, la única prohibición incondicional, los tres límites del 13.9 y
  «Elaborado en vivienda particular» · PA-30/30b con los envases de servicio y **la obligación en el
  proveedor, no en el pastelero** · PA-31/31b con la exención acotada al 6.4 y el 02-04-2026 · PA-32 con los
  17.094 € **sin decir «14 pagas»** · PA-33 con las 15 pagas y los 17.886,30 € por encima del SMI · PA-34 con
  el registro de jornada **sin norma digital** y el aviso de «proyecto en tramitación» · PA-36/36b/36c/36d con
  la lista cerrada del 4 %, el pan del RD 308/2019 al 4 % por la Resolución de la DGT y el 21 % de la bebida
  para llevar · PA-37 con 1-ene-2027 / 1-jul-2027 y el plazo del fabricante sin fecha derivada · PA-39 con la
  libertad horaria y el matiz de actividad principal · PA-44 con el art. 20 de la Ley 7/1996. **Ninguna de las
  13 prohibiciones del §12 de la verificación aparece violada, salvo la de A6**, que no está en esa lista sino
  en el calendario del propio anexo.
- **Frontera con el kit (R1-R6):** el plan de producción semanal se cita por nombre y no se rehace (R1) ·
  la ficha y el registro de encargos se remiten al `11-control-encargos.xlsx` (R2) · la matriz de vitrina se
  deja al kit y sólo se construye la de obrador (R3) · las temperaturas y vidas útiles se remiten y lo que se
  construye es la hoja de huevo (R4) · el calendario de picos se remite y la guía pone los euros (R5) · las
  fichas de perfil se remiten y la guía construye el dimensionado (R6). **Los seis se cumplen**, y la frase de
  frontera («el Kit de Tareas te dice qué hacer cada día cuando ya has abierto; esta guía es todo lo que hay
  que decidir antes») está en el cap. 1, arriba y no en la FAQ.
- **Los tres perfiles y los nombres del kit:** Jefe Pastelero · Pastelero · Ayudante · Dependiente Vitrina A y
  B, literales, en los tres documentos y en los cuatro xlsx que los usan. **«Oficial» no aparece nunca** como
  nombre de perfil (sólo dentro de la denominación literal del convenio, «oficial 1.ª de producción», que es
  cita).
- **Títulos:** ninguno lleva raya «—» ni cifra con separador de miles; Title Case español correcto en los 21
  del índice y en los 12 del bonus.

---

*Refutación escrita el 2026-09-10 leyendo los tres documentos enteros, los 46 bloques de la caché, el guion
resuelto contra las celdas, los 8 libros con `data_only` y los tres PDF. Temperatura de CPU vigilada antes de
cada python (máximo 55,4 °C), un intérprete cada vez, sin builds.*

Via: Claude Code
