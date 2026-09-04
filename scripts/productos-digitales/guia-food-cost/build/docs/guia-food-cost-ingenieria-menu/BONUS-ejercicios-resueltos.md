# 12 Ejercicios Resueltos de Food Cost e Ingeniería de Menú

**Bonus del pack «Guía Food Cost + Ingeniería de Menú» · con los datos de las ocho herramientas Excel**

*John Guerrero · AI Chef Pro · aichef.pro*

Doce ejercicios con enunciado, resolución paso a paso y tabla, resueltos sobre la misma carta de ejemplo que usan las ocho herramientas Excel de este pack. No hay ninguna cifra inventada: cada número sale de una celda que puedes abrir y comprobar. Haz el ejercicio con tus datos al lado y en dos tardes tendrás tu carta escandallada, clasificada y con precio.

**Versión 1.0 · septiembre de 2026 · aichef.pro/guia-food-cost-ingenieria-menu**

---

## Índice

1. **Cantidad Bruta y Coste con Merma** — de la cantidad neta de la receta a la cantidad que hay que comprar, y de ahí al coste de la línea.
2. **Test de Rendimiento con Subproductos** — cuánto cuesta el kilo limpio cuando el recorte se aprovecha y cuánto cuando no.
3. **Food Cost Real de un Mes** — stock inicial más compras menos stock final, y el porcentaje sobre la venta neta.
4. **El Mismo Plato por los Cuatro Métodos** — factor, margen objetivo, mercado y valor percibido aplicados al mismo coste por ración.
5. **El IVA de una Bebida, Canal por Canal** — la misma botella en sala y para llevar: dos tipos y dos precios al cliente.
6. **Clasificar una Familia con Kasavana & Smith** — umbral de popularidad, margen medio ponderado y los cuatro cuadrantes, dentro de una familia.
7. **El Mismo Grupo en Miller y en Pavesic** — por qué dos modelos que miran los mismos platos llegan a conclusiones distintas.
8. **Goal Value de Dos Platos** — un índice por plato frente al objetivo de su familia, sin cuadrantes.
9. **Repricing en Delivery con Packaging y Techo** — comisión sobre el precio, envase por plato y el precio máximo que aguanta la aplicación.
10. **Copa o Botella** — el mismo vino servido de dos formas: qué cambia en el porcentaje y qué cambia en los euros.
11. **Prime Cost de un Mes y su Semáforo** — sumar producto y personal con la Seguridad Social dentro, y compararlo con el objetivo del formato.
12. **Menú de Precio Fijo: el Margen lo Decide el Mix** — el mismo menú al mismo precio con tres repartos de elección distintos.

---

## 1. Cantidad Bruta y Coste con Merma

### El enunciado y los datos

Tomamos la línea de solomillo de la hoja «Ficha» de ficha-escandallo-base.xlsx: una ración pide 0,22 de producto neto, con una merma del 12,0 % en la limpieza previa a cocina, y el proveedor factura el solomillo a 15,80 € por unidad, sin IVA. El ejercicio plantea dos preguntas que se repiten en cualquier escandallo (costeo de recetas): cuánto hay que comprar en bruto para que, tras descartar la merma, quede la cantidad neta que pide la receta, y cuánto cuesta esa línea dentro de la ficha.

La trampa está en el verbo con el que se habla de la merma: cuando se dice que una pieza «tiene un 12,0 % de merma», la tentación es multiplicar la cantidad neta directamente por ese porcentaje, como si la merma fuera un extra que se suma al final. No es así: es la parte de la pieza bruta que se pierde por el camino, y hay que comprar de más para compensarla, no sumarla a lo que ya se tiene. Esa diferencia separa un escandallo que refleja lo que de verdad ha pagado la cocina de otro que infravalora el coste (costo) del plato.

### La resolución, paso a paso

La fórmula es la misma para cualquier línea: la cantidad bruta es igual a la cantidad neta dividida entre uno menos la merma, expresada en tanto por uno. Aplicada al solomillo —cantidad neta 0,22, merma 12,0 %— esa división da la cantidad bruta a comprar, 0,25, la cifra que recoge la hoja «Ficha» de ficha-escandallo-base.xlsx y la tabla de abajo.

El coste de la línea no se calcula sobre la cantidad neta, que es lo que llega al plato, sino sobre la cantidad bruta, lo que realmente se ha comprado: cantidad bruta por precio por unidad sin IVA. Con 0,25 de cantidad bruta y 15,80 € por unidad, la línea de solomillo cuesta 3,95 € sin IVA, la cifra que cierra esa fila en la tabla siguiente.

Ahora el error que hay que desterrar: si en lugar de dividir se multiplica la cantidad neta por la merma —0,22 por 12,0 %— y ese resultado se toma como si fuera la cantidad bruta, la cifra sale muy por debajo de 0,25, y el coste de línea queda muy por debajo de los 3,95 € reales: la cocina compra de menos y anota un plato más barato de lo que en realidad cuesta producir. La línea del boniato, con merma del 18 %, llega a su cantidad bruta —0,22— por el mismo camino, y el coste total de la ficha, sin IVA, 5,67 €, sólo es correcto si cada línea se ha costeado en bruto y no en neto.

### Cómo se lee el resultado

Lo que separa el escandallo correcto del erróneo no es un matiz teórico: es pedir al proveedor la cantidad que hace falta, o quedarse corto en pleno servicio, y anotar un coste que existe de verdad frente a uno que sólo existe sobre el papel. La cifra que sale de la división —0,25 en el solomillo, 0,22 en el boniato— es la que hay que trasladar tal cual al pedido; comprar menos deja la partida corta, y pedir de más «por si acaso» no resuelve el problema, sólo lo esconde. El procedimiento no cambia de una línea a otra por mucho que cambien la merma o el precio: siempre es dividir la cantidad neta entre uno menos la merma y multiplicar el resultado por el precio, y es lo que sostiene el coste total de la ficha, sin IVA, en 5,67 €.

Ese coste total es también el número que se traslada de la ficha a la carta (menú) al fijar el precio de venta: si la cantidad bruta que lo alimenta está mal calculada en una sola línea, el precio de venta arrastra el mismo error desde el primer paso. Revisar la cantidad bruta de cada línea antes de cerrar la ficha es, de las tareas de este capítulo, la que menos tiempo exige y la que más protege el margen, ración a ración, cada vez que el plato sale de cocina.

**Las líneas de la ficha, con la cantidad bruta calculada**

| Ingrediente | Cantidad neta/ración | Merma (%) | Cantidad bruta a comprar | Precio/ud sin IVA (€) | Coste sin IVA (€) |
|---|---|---|---|---|---|
| Solomillo de cerdo ibérico | 0,22 | 12,0 % | 0,25 | 15,80 € | 3,95 € |
| Panceta ibérica (crujiente) | 0,03 | 5,0 % | 0,03 | 11,50 € | 0,36 € |
| Boniato | 0,18 | 18,0 % | 0,22 | 1,60 € | 0,35 € |
| Mantequilla | 0,01 | 0,0 % | 0,01 | 8,90 € | 0,13 € |
| Nata 35 % M.G. | 0,03 | 0,0 % | 0,03 | 3,40 € | 0,10 € |
| Cebolla | 0,04 | 12,0 % | 0,05 | 0,95 € | 0,04 € |
| Vino Pedro Ximénez (para la salsa) | 0,03 | 0,0 % | 0,03 | 9,80 € | 0,29 € |
| Caldo de carne | 0,06 | 0,0 % | 0,06 | 2,20 € | 0,13 € |
| Aceite de oliva virgen extra | 0,01 | 0,0 % | 0,01 | 7,20 € | 0,11 € |
| Brotes de rúcula | 0,01 | 10,0 % | 0,01 | 12,00 € | 0,13 € |
| Sal, pimienta, tomillo y pimentón (prorrateo) | 0,01 | 0,0 % | 0,01 | 6,00 € | 0,06 € |


---

## 2. Test de Rendimiento con Subproductos

### El enunciado y los datos

Partimos de una lubina entera comprada con su peso bruto ya pesado y su precio de compra por kilo conocido. Tras el despiece en cocina —quitar cabeza, espina y piel— queda un peso limpio, menor que el bruto, que es el que de verdad se sirve en el plato. De esa misma pieza sale además un recorte aprovechable: cabeza, espina y piel que no van directas al cubo de orgánico, sino que se separan, se pesan y se les asigna un valor de uso, es decir, lo que valen convertidas en fondo o en otra elaboración de aprovechamiento. Estos cuatro datos —peso bruto, precio de compra por kilo, peso limpio y valor de uso del subproducto— son el registro mínimo de cada pieza que se somete a esta prueba, y es lo que recoge, pieza a pieza, la hoja «Test de Rendimiento» de rendimiento-mermas-producto.xlsx. El objetivo no es saber cuánto pesa una lubina: es decidir, con esos cuatro datos, si compensa comprarla entera y trabajarla en casa o si sale mejor cuenta pedirla ya limpia al proveedor.

### La resolución, paso a paso

Primero se calcula el rendimiento: peso limpio dividido entre peso bruto. En esta lubina la operación da un 51,7 %, es decir, algo más de la mitad de lo que se compra se queda como carne aprovechable, y el resto son cabeza, espina, piel y recorte.

Segundo, el coste (costo) de compra: peso bruto multiplicado por el precio por kilo. Es el desembolso real que sale de caja por la pieza entera, antes de tocarla con el cuchillo.

Tercero, el coste neto por kilo limpio sin aprovechar el subproducto: el coste de compra dividido entre el peso limpio, sin restar nada. El resultado es 28,84 € el kilo, y es la cifra que hay que enfrentar al precio de venta del plato de lubina en la carta (menú), no al precio de compra por kilo que figura en la factura del proveedor.

Cuarto, el coste neto por kilo limpio aprovechando el subproducto: al coste de compra se le resta el valor de uso del recorte y el resultado se vuelve a dividir entre el peso limpio. Con esa resta, el coste neto baja a 27,63 € el kilo. La distancia entre los dos costes netos es lo que aporta el subproducto cuando alguien lo separa y le da salida en cocina antes de que caduque; cuando nadie lo hace, esa aportación se pierde en el cubo de basura orgánica.

### Cómo se lee el resultado

El dato que de verdad importa a la hora de fijar el precio de venta no es el precio de compra por kilo que aparece en la factura: es el coste neto por kilo limpio, porque refleja lo que cuesta de verdad cada kilo que llega al comensal. Comparado con el precio por kilo de la pieza entera, sin trabajar, el coste neto sin aprovechar el subproducto arrastra un sobrecoste de 12,73 € por kilo, y esa diferencia es lo que se paga por la parte de la lubina que termina en la basura orgánica en vez de en el plato: cuanto más bajo el rendimiento de una pieza, más carga ese sobrecoste sobre el kilo que sí se vende.

Puesta en el contexto del resto de pruebas de la misma hoja, esta lubina queda algo por debajo del rendimiento medio ponderado del conjunto, que es del 60,5 %: dentro del cuadro que sigue a este ejercicio hay piezas que aprovechan mejor su peso bruto y otras que aprovechan peor, y el criterio para decidir si una pieza compensa comprarla entera es esa comparación, no un número aislado. El mismo cuadro deja ver pruebas donde el subproducto pesa todavía más en la decisión: el ahorro por aprovechar las cabezas de la gamba, por ejemplo, es de 1,43 € por kilo, una cifra que en un producto de compra frecuente y precio alto tiene un recorrido acumulado distinto al de una pieza que sólo se trabaja de forma puntual. En conjunto, el valor de uso total de los subproductos de las diez pruebas del cuadro llega a 5,15 €, la prueba de que separar y dar salida al recorte no es un gesto simbólico: es una partida que se sigue con la misma disciplina que cualquier otro coste de la carta.

**Diez tests con su coste del kilo limpio, con y sin aprovechar el recorte**

| Producto | Peso bruto (kg) | Peso limpio (kg) | Subproductos (kg) | Valor de uso (€/kg) | Coste neto sin aprovechar (€/kg) | Coste neto aprovechando (€/kg) | Ahorro (€/kg) |
|---|---|---|---|---|---|---|---|
| Lubina entera (1,2 kg) | 1,20 | 0,62 | 0,30 | 2,50 € | 28,84 € | 27,63 € | 1,21 € |
| Merluza entera | 2,40 | 1,30 | 0,55 | 2,50 € | 21,78 € | 20,73 € | 1,06 € |
| Solomillo de vacuno (pieza) | 2,10 | 1,85 | 0,12 | 6,00 € | 30,08 € | 29,69 € | 0,39 € |
| Pollo de corral entero | 2,20 | 1,50 | 0,45 | 1,80 € | 7,92 € | 7,38 € | 0,54 € |
| Cordero (paletilla) | 1,60 | 1,35 | 0,00 | 0,00 € | 15,64 € | 15,64 € | 0,00 € |
| Tomate rosa | 5,00 | 4,40 | 0,00 | 0,00 € | 4,32 € | 4,32 € | 0,00 € |
| Alcachofa | 5,00 | 1,90 | 0,00 | 0,00 € | 7,63 € | 7,63 € | 0,00 € |
| Boniato | 5,00 | 4,10 | 0,00 | 0,00 € | 1,95 € | 1,95 € | 0,00 € |
| Mejillón (con concha) | 5,00 | 1,00 | 0,00 | 0,00 € | 13,00 € | 13,00 € | 0,00 € |
| Gamba blanca (entera) | 2,00 | 1,05 | 0,50 | 3,00 € | 45,71 € | 44,29 € | 1,43 € |


---

## 3. Food Cost Real de un Mes

### El enunciado y los datos

Un mes de carta se cierra con cuatro datos que hay que tener sobre la mesa antes de hablar de food cost: el inventario valorado al empezar el periodo (el stock inicial, el que queda tras el recuento físico del cierre anterior), las compras que han entrado por factura a lo largo del mes, el inventario valorado al terminar (el stock final, tras el recuento de ese mismo mes) y las ventas netas facturadas en esas mismas fechas, sin IVA y sin propinas. Ninguno de los cuatro sustituye a otro: comprar no es lo mismo que consumir.

La tabla siguiente recorre esa cuenta mes a mes. En enero, el consumo de materia prima cerró en 28.400 €, sobre unas ventas netas de 89.600 €, con un food cost de 31,7 %. Llevado a los doce meses del año, las compras acumuladas fueron 396.100 €, el consumo real acumulado 395.400 €, las ventas netas del año 1.232.200 € y el food cost del año 32,1 %, frente al food cost objetivo del cuadro de mando, fijado en 30 %. El ejercicio consiste en calcular el consumo real y compararlo con lo que dicen las compras solas.

### La resolución, paso a paso

La fórmula no cambia de un mes a otro: consumo es igual a stock inicial más compras menos stock final. Se aplica en tres movimientos.

- Se parte del inventario valorado con el que se cerró el mes anterior, que hace de stock inicial de este.
- Se suman las compras registradas en el periodo, tomadas de la factura de cada proveedor, nunca del albarán de reparto.
- Se resta el inventario valorado tras el recuento físico de cierre de este mes, el stock final.

Lo que queda de esa resta es el consumo real de materia prima del periodo, el que de verdad ha pasado por cocina y por barra. El food cost sale de dividir ese consumo entre las ventas netas del mismo periodo.

Aplicado a enero, la secuencia entrega el consumo de 28.400 € ya citado, y ese consumo entre las ventas netas de 89.600 € da el food cost de 31,7 %. La misma mecánica, sostenida los doce meses, deja el consumo real del año en 395.400 € sobre unas compras acumuladas de 396.100 €: dos cifras muy próximas, pero no la misma, y la diferencia entre ellas es justamente lo que ha cambiado de valor el almacén en ese tramo.

### Cómo se lee el resultado

El error habitual es dar por bueno el gasto en compras como si fuera el consumo, porque es el número que llega antes: la factura del proveedor está en cuanto se paga, y el consumo real solo aparece después del recuento físico. Ese atajo engaña siempre en la dirección en la que se haya movido el almacén.

Cuando el stock final acaba más alto que el inicial, con el almacén más lleno que al empezar, las compras superan al consumo real, porque parte de lo comprado todavía no ha salido del almacén. Tomar las compras como si fueran consumo infla el food cost: parece peor de lo que es, y puede llevar a tocar precios o raciones por un problema que en realidad es de inventario acumulado, no de coste (costo).

Cuando el stock final acaba más bajo que el inicial, con el almacén vaciándose, ocurre lo contrario: el consumo real supera a las compras, porque se ha gastado género ya pagado de meses anteriores. Ahí el atajo esconde el problema, porque el food cost calculado sobre compras sale mejor de lo que es, justo cuando el almacén se vacía por debajo.

El caso del año lo ilustra en pequeño: las compras, 396.100 €, quedan por encima del consumo real, 395.400 €, señal de que el almacén ha terminado el año algo más lleno de lo que empezó. Tanto el 31,7 % de enero como el 32,1 % del año quedan por encima del food cost objetivo del cuadro de mando, 30 %, con la cuenta hecha siempre sobre el consumo real y nunca sobre lo comprado: es la única forma de que la comparación con el objetivo signifique lo que dice que significa.

**Del stock al consumo, mes a mes**

| Mes | Stock inicial (€) | Compras (€) | Stock final (€) | Consumo (€) | Ventas netas (€) | Food cost (%) |
|---|---|---|---|---|---|---|
| Enero | 9.700 € | 28.100 € | 9.400 € | 28.400 € | 89.600 € | 31,7 % |
| Febrero | 9.400 € | 27.000 € | 9.100 € | 27.300 € | 84.100 € | 32,5 % |
| Marzo | 9.100 € | 30.700 € | 9.500 € | 30.300 € | 95.200 € | 31,8 % |
| Abril | 9.500 € | 31.400 € | 9.200 € | 31.700 € | 100.400 € | 31,6 % |
| Mayo | 9.200 € | 34.700 € | 9.700 € | 34.200 € | 107.900 € | 31,7 % |
| Junio | 9.700 € | 37.700 € | 9.000 € | 38.400 € | 110.700 € | 34,7 % |
| Julio | 9.000 € | 38.100 € | 9.400 € | 37.700 € | 116.200 € | 32,4 % |
| Agosto | 9.400 € | 34.400 € | 8.700 € | 35.100 € | 99.600 € | 35,2 % |
| Septiembre | 8.700 € | 32.600 € | 9.500 € | 31.800 € | 105.500 € | 30,1 % |
| Octubre | 9.500 € | 31.800 € | 9.200 € | 32.100 € | 102.700 € | 31,3 % |
| Noviembre | 9.200 € | 30.500 € | 9.700 € | 30.000 € | 97.900 € | 30,6 % |
| Diciembre | 9.700 € | 39.100 € | 10.400 € | 38.400 € | 122.400 € | 31,4 % |
| TOTAL / MEDIA |  | 396.100 € |  | 395.400 € | 1.232.200 € | 32,1 % |


---

## 4. El Mismo Plato por los Cuatro Métodos

### El enunciado y los datos

El ejercicio toma un plato de coste (costo) alto: el chuletón, la pieza que en cualquier carta (menú) concentra el mayor gasto en materia prima por ración. La hoja «Por Plato» de precio-objetivo-multi-metodo.xlsx recoge, para este plato, su coste por ración —el que ya sale del escandallo (costeo de recetas) que el lector tiene cargado en el resto del pack—, el food cost objetivo fijado para toda la carta, un margen objetivo en euros que protege el beneficio absoluto de esta pieza en concreto, y dos referencias que no salen de ningún cálculo interno: el precio de mercado, lo que el chuletón puede sostener frente a lo que cobra la competencia directa, y el precio de valor percibido, el techo que el comensal está dispuesto a pagar por esa pieza en ese local. El food cost objetivo de la carta es del 30 %, el mismo porcentaje que se aplica al resto de los platos de la hoja, desde las croquetas hasta este chuletón. Con esos cuatro puntos de partida la hoja resuelve el mismo plato por cuatro caminos distintos, y lo que cada uno de ellos devuelve es lo que se compara en el cuadro siguiente.

### La resolución, paso a paso

Las cuatro vías parten del mismo coste y llegan a cuatro precios de venta distintos:

- Precio por factor: el coste se divide entre el food cost objetivo. Con un food cost objetivo del 30 %, el precio de venta del chuletón por esta vía sube hasta 49,33 €.
- Precio por margen: al coste se le suma el margen objetivo en euros. Por este camino, el precio de venta del chuletón queda en 25,30 €, y es este precio —no el del factor— el que la hoja marca como el elegido para la carta.
- Precio de mercado: se toma el precio que ya sostiene la competencia directa y, con ese dato como entrada, se calcula el food cost que resultaría de vender a esa cifra.
- Precio de valor percibido: misma lógica, tomando como entrada el techo que el comensal está dispuesto a pagar por esa pieza en ese local.

Con el precio elegido de 25,30 €, el food cost final del chuletón queda en el 58,5 %: muy por encima del 30 % objetivo y también del precio que este plato lleva hoy en carta, 32,70 €. Con las croquetas, plato de coste bajo, el mismo ejercicio da otro resultado: el precio de venta por factor es de 7,00 €, cercano al 8,60 € que ya llevan hoy en carta, de modo que ahí el factor no abre ninguna brecha con lo que el negocio ya cobra.

### Cómo se lee el resultado

El precio por factor no sirve para el chuletón, y eso no es un fallo de la hoja: es el límite del propio método. El factor multiplica el coste por una constante fija, pensada para que el food cost salga igual en todos los platos de la carta, y esa igualdad sólo tiene sentido comercial en el tramo de coste medio y bajo, donde el resultado cae dentro de lo que el comensal ya paga por costumbre. En un plato de coste alto como el chuletón, la misma constante empuja el precio muy por encima de lo que el precio de mercado y el precio de valor percibido están dispuestos a sostener, y ahí es donde el precio por margen recupera el control: fija el beneficio en euros y deja que el food cost se mueva, incluso hasta ese 58,5 % que en cualquier otro plato pediría revisión inmediata. No es que el chuletón sea un mal plato: es que en los platos de coste alto el food cost deja de ser el indicador que manda, y pasa a mandar el margen de contribución en euros que deja cada ración. Comparar el chuletón con las croquetas ayuda a fijar la idea: en un plato de coste bajo, el precio por factor y el precio por margen tienden a converger, y por eso ahí sí funciona el atajo del método del factor; en un plato de coste alto, el mismo atajo deja de sostenerse, y hay que resolver el precio por la vía del margen, contrastado siempre contra lo que el precio de mercado y el precio de valor percibido están dispuestos a aceptar.

**Los cuatro métodos sobre la misma carta**

| Plato | Coste/ración (€) | A · PVP por factor (€) | B · PVP por margen (€) | FC con el precio de mercado (%) | FC con el valor percibido (%) | PVP elegido sin IVA (€) |
|---|---|---|---|---|---|---|
| Croquetas de jamón ibérico (6 ud) | 2,10 € | 7,00 € | 8,60 € | 23,0 % | 21,8 % | 7,00 € |
| Ensalada de tomate rosa, ventresca y cebolleta | 3,60 € | 12,00 € | 10,10 € | 32,1 % | 28,5 % | 12,00 € |
| Gambas al ajillo | 6,90 € | 23,00 € | 13,40 € | 39,7 % | 37,1 % | 13,40 € |
| Huevos rotos con patatas y chistorra | 2,40 € | 8,00 € | 8,90 € | 26,1 % | 22,7 % | 8,00 € |
| Tabla de quesos de la zona | 5,20 € | 17,33 € | 11,70 € | 33,2 % | 31,3 % | 17,33 € |
| Alcachofas confitadas con jamón | 3,10 € | 10,33 € | 9,60 € | 30,6 % | 26,8 % | 10,33 € |
| Sopa de tomate asado con albahaca | 1,20 € | 4,00 € | 7,70 € | 18,5 % | 15,9 % | 7,56 € |
| Solomillo de cerdo ibérico con puré de boniato | 5,67 € | 18,90 € | 16,17 € | 30,4 % | 28,3 % | 18,68 € |
| Bacalao confitado al pil-pil | 7,40 € | 24,67 € | 17,90 € | 34,6 % | 32,3 % | 17,90 € |
| Hamburguesa de vaca madurada con patatas | 4,30 € | 14,33 € | 14,80 € | 33,3 % | 29,8 % | 12,92 € |
| Arroz meloso de secreto ibérico y setas | 6,20 € | 20,67 € | 16,70 € | 35,7 % | 33,2 % | 16,70 € |
| Chuletón de vaca madurada (500 g) | 14,80 € | 49,33 € | 25,30 € | 37,7 % | 36,2 % | 25,30 € |
| Lubina a la sal | 8,90 € | 29,67 € | 19,40 € | 37,1 % | 34,6 % | 19,40 € |
| Pollo de corral asado con patatas | 3,70 € | 12,33 € | 14,20 € | 31,0 % | 27,2 % | 11,94 € |
| Lasaña de verduras de temporada | 2,60 € | 8,67 € | 13,10 € | 24,8 % | 21,7 % | 10,49 € |
| Tataki de atún rojo con sésamo | 9,60 € | 32,00 € | 20,10 € | 37,3 % | 35,1 % | 20,10 € |
| Tarta de queso cremosa | 1,30 € | 4,33 € | 5,50 € | 20,8 % | 19,7 % | 6,61 € |
| Torrija caramelizada con helado | 1,10 € | 3,67 € | 5,30 € | 21,3 % | 18,9 % | 5,83 € |
| Coulant de chocolate | 1,60 € | 5,33 € | 5,80 € | 23,9 % | 22,4 % | 7,13 € |
| Fruta de temporada preparada | 1,40 € | 4,67 € | 5,60 € | 34,6 % | 29,6 % | 4,73 € |


---

## 5. El IVA de una Bebida, Canal por Canal

### El enunciado y los datos

El tinto de la casa que la hoja «Vinos» de carta-de-bebidas-beverage-cost.xlsx recoge tiene un precio de venta sin IVA de 13,60 € cuando se sirve en sala. El ejercicio plantea dos preguntas sobre esa misma botella: cuánto paga el cliente que se sienta a la mesa y cuánto paga el cliente que se la lleva cerrada, sin abrir, para beberla en su casa. El coste (costo) de compra de la botella, también sin IVA, es 3,90 €, y ese dato no se mueve entre un canal y otro: lo único que cambia es el tipo de IVA que se le repercute al cliente, según haya o no servicio de hostelería de por medio. La carta (menú) no distingue precios por canal —el vino tiene un único precio de venta sin IVA— y es justo ahí donde conviene mirar con lupa lo que ocurre después, cuando ese precio se convierte en dos importes finales distintos.

### La resolución, paso a paso

En sala hay servicio de hostelería: el camarero descorcha, sirve y retira la copa, así que la operación completa —venta más servicio— tributa al tipo reducido del 10 %, alcohol incluido, porque no es una entrega de bienes sino una prestación de servicios de hostelería (Ley 37/1992, art. 91.Uno.2.2.º, texto consolidado tras la última modificación por Ley 7/2024, en vigor desde el 22 de diciembre de 2024). Aplicado a los 13,60 € de la botella, el resultado es el precio de venta con IVA en sala: 14,96 €.

Sin ese servicio —botella cerrada, cliente que se la lleva— la operación deja de ser una prestación de servicios y pasa a ser una entrega de bienes, y ahí la bebida alcohólica queda excluida del tipo reducido y cae en el tipo general del 21 % (Ley 37/1992, arts. 90 y 91.Uno.1.1.º, con el criterio de la Dirección General de Tributos en su consulta V2254-22). El mismo precio de venta sin IVA, los mismos 13,60 €, da entonces un resultado distinto: 16,46 € con IVA para llevar. La matriz fiscal no distingue sólo por canal, sino por producto: los refrescos con azúcares o edulcorantes añadidos siguen el mismo camino fuera de sala y tributan también al 21 % desde el 1 de enero de 2021 (Ley 37/1992, art. 91.Uno.1.1.º, en la redacción que le dio la Ley 11/2020 de Presupuestos Generales del Estado para 2021, en su artículo 69), mientras que la comida para llevar se queda en el 10 %. La exclusión apunta al alcohol y al azúcar añadido, no al hecho de salir del local con la bolsa en la mano.

### Cómo se lee el resultado

El coste de compra de la botella es idéntico en los dos canales: 3,90 €, sin IVA, la sirva o no la sirva el camarero. Lo único que se mueve es el tipo que se repercute al cliente, y ese movimiento trae una consecuencia que suele pasar desapercibida en la carta: si decides mantener el mismo precio final al público en sala y para llevar —por comodidad, por no manejar dos etiquetas en la misma botella— la parte de ese precio que corresponde a IVA repercutido crece en el canal para llevar, porque el tipo pasó del 10 % al 21 %, y la base imponible que efectivamente te queda a ti como ingreso se reduce en la misma proporción. El coste de compra no ha subido ni un céntimo y, sin embargo, el margen sobre esa venta cae, sólo por el canal que ha elegido el cliente. De ahí que convenga fijar el precio para llevar sobre el precio sin IVA de la carta y aplicarle el tipo que le corresponde a ese canal, en vez de arrastrar un único precio final entre los dos: es lo que evita que la diferencia de tipo se coma el margen sin que nadie lo haya decidido.

**La misma botella, dos canales y dos tipos de IVA**

| Vino | PVP botella sin IVA (€) | IVA en sala (%) | PVP con IVA en sala (€) | IVA para llevar (%) | PVP con IVA para llevar (€) |
|---|---|---|---|---|---|
| Tinto de la casa (Tempranillo joven) | 13,60 € | 10 % | 14,96 € | 21 % | 16,46 € |
| Crianza Rioja | 19,10 € | 10 % | 21,01 € | 21 % | 23,11 € |
| Ribera del Duero roble | 21,80 € | 10 % | 23,98 € | 21 % | 26,38 € |
| Verdejo Rueda | 14,50 € | 10 % | 15,95 € | 21 % | 17,54 € |
| Albariño Rías Baixas | 22,70 € | 10 % | 24,97 € | 21 % | 27,47 € |
| Cava brut nature | 18,20 € | 10 % | 20,02 € | 21 % | 22,02 € |
| Rosado Navarra | 12,70 € | 10 % | 13,97 € | 21 % | 15,37 € |
| Vino dulce Pedro Ximénez | 27,30 € | 10 % | 30,03 € | 21 % | 33,03 € |


---

## 6. Clasificar una Familia con Kasavana & Smith

### El enunciado y los datos

Antes de fiarnos de la etiqueta que la matriz coloca junto a cada plato, conviene hacerla a mano una vez, con una sola familia, para ver de dónde sale cada palabra. Tomamos la familia de entrantes tal y como está recogida en la hoja «Datos» de matriz-multimetodo-carta.xlsx: 7 platos, 1.730 unidades vendidas en el periodo que cubre el análisis y un margen de contribución medio ponderado de 7,46 € por unidad. Son los tres datos de partida y no hace falta ninguno más para reproducir el criterio del modelo.

El modelo detrás del ejercicio es el de Kasavana y Smith (1982): cruza cuánto pesa cada plato dentro de las ventas de su propia familia frente a cuánto margen deja, y de esa doble comparación sale una de cuatro etiquetas. Lo que falta para cerrar el cálculo plato a plato —las unidades vendidas y el margen de cada uno por separado, ya no los de la familia entera— es justo lo que recoge el cuadro que sigue a este texto, con el umbral de la familia al lado de cada fila.

### La resolución, paso a paso

Con los tres datos de la familia se reconstruye el procedimiento completo en cuatro pasos, los mismos que aplica la matriz a cada familia de la carta (menú):

- El mix de cada plato es su peso dentro de la familia: las unidades que vende ese plato en concreto sobre las 1.730 unidades que suman entre todos los entrantes. Es una proporción interna a la familia, no a la carta completa, y por eso el mismo número de ventas pesa distinto según en qué familia caiga el plato.
- El umbral de popularidad de la familia sale de aplicar el factor del 70 % —el mismo que rige toda la matriz, guardado también en la hoja «Datos»— a la cuota que le tocaría a cada plato si las unidades se repartieran a partes iguales entre los 7 platos de la familia: ese 70 % multiplicado por uno entre el número de platos. Un plato con un mix por encima de ese umbral cuenta como popular dentro de su familia; por debajo, no.
- El margen de contribución de cada plato se compara con el margen medio ponderado de la familia, esos 7,46 € por unidad. Por encima de la media, el plato deja más margen que el conjunto de los entrantes; por debajo, deja menos.
- La etiqueta sale de cruzar las dos comparaciones, no de mirarlas por separado: popularidad alta con margen alto es un Star; popularidad alta con margen bajo, un Plowhorse; popularidad baja con margen alto, un Puzzle; y popularidad baja con margen bajo, un Dog.

Aplicado a la carta completa —no ya solo a los entrantes—, el resultado que arroja la hoja «Kasavana-Smith» de matriz-multimetodo-carta.xlsx es de 6 platos Star, 6 Plowhorse, 5 Puzzle y 3 Dog. Es la misma lógica que acabamos de aplicar a mano en la familia de entrantes, repetida familia por familia hasta agotar la carta entera; el cuadro siguiente recoge el detalle plato a plato, con el mix, el margen y el umbral de cada uno junto a su etiqueta.

### Cómo se lee el resultado

La etiqueta de un plato no es una propiedad suya en solitario: depende del conjunto de platos con los que comparte familia en el momento de calcularla. El umbral se construye sobre el número de platos de la familia y el mix de cada uno se mide sobre el total de unidades de esa misma familia, así que retirar un plato de la carta —o añadir uno nuevo— cambia los dos denominadores a la vez. Los platos que quedan no han vendido ni una unidad más ni una menos, pero su mix se recalcula sobre un total distinto y el margen medio ponderado de la familia también se desplaza, de modo que un plato que hoy queda justo por encima del umbral puede caer por debajo la próxima vez que se revise la carta, sin que nada en su propia venta haya cambiado. Por eso conviene repetir este cálculo cada vez que se toca la composición de una familia, y no solo cuando cambia el precio de venta o el coste (costo) de un plato concreto: quitar de una familia el plato con peor etiqueta no siempre mejora a los demás, porque puede desplazar el umbral o la media hacia un punto que perjudique a otro plato que hasta entonces estaba a salvo.

**La clasificación plato a plato, con el umbral de su familia al lado**

| Plato | Familia | Uds | Mix en su familia (%) | Umbral (%) | MC (€) | Clasificación |
|---|---|---|---|---|---|---|
| Croquetas de jamón ibérico (6 ud) | Entrantes | 420 | 24,3 % | 10,0 % | 6,50 € | Plowhorse |
| Ensalada de tomate rosa, ventresca y cebolleta | Entrantes | 310 | 17,9 % | 10,0 % | 8,20 € | Star |
| Gambas al ajillo | Entrantes | 260 | 15,0 % | 10,0 % | 8,60 € | Star |
| Huevos rotos con patatas y chistorra | Entrantes | 380 | 22,0 % | 10,0 % | 7,40 € | Plowhorse |
| Tabla de quesos de la zona | Entrantes | 90 | 5,2 % | 10,0 % | 8,40 € | Puzzle |
| Alcachofas confitadas con jamón | Entrantes | 120 | 6,9 % | 10,0 % | 7,80 € | Puzzle |
| Sopa de tomate asado con albahaca | Entrantes | 150 | 8,7 % | 10,0 % | 6,00 € | Dog |
| Solomillo de cerdo ibérico con puré de boniato | Principales | 340 | 16,8 % | 7,8 % | 11,63 € | Star |
| Bacalao confitado al pil-pil | Principales | 190 | 9,4 % | 7,8 % | 11,70 € | Star |
| Hamburguesa de vaca madurada con patatas | Principales | 460 | 22,8 % | 7,8 % | 9,30 € | Plowhorse |
| Arroz meloso de secreto ibérico y setas | Principales | 270 | 13,4 % | 7,8 % | 10,20 € | Plowhorse |
| Chuletón de vaca madurada (500 g) | Principales | 110 | 5,4 % | 7,8 % | 17,90 € | Puzzle |
| Lubina a la sal | Principales | 80 | 4,0 % | 7,8 % | 12,90 € | Puzzle |
| Pollo de corral asado con patatas | Principales | 300 | 14,9 % | 7,8 % | 9,00 € | Plowhorse |
| Lasaña de verduras de temporada | Principales | 140 | 6,9 % | 7,8 % | 8,80 € | Dog |
| Tataki de atún rojo con sésamo | Principales | 130 | 6,4 % | 7,8 % | 12,80 € | Puzzle |
| Tarta de queso cremosa | Postres | 520 | 46,4 % | 17,5 % | 4,60 € | Star |
| Torrija caramelizada con helado | Postres | 210 | 18,8 % | 17,5 % | 4,40 € | Plowhorse |
| Coulant de chocolate | Postres | 330 | 29,5 % | 17,5 % | 4,60 € | Star |
| Fruta de temporada preparada | Postres | 60 | 5,4 % | 17,5 % | 3,10 € | Dog |


---

## 7. El Mismo Grupo en Miller y en Pavesic

### El enunciado y los datos

El ejercicio parte de un grupo de platos de la carta (menú), con tres datos ya cerrados en su escandallo (costeo de recetas): food cost porcentual, margen de contribución por unidad y unidades vendidas en el periodo. Son los mismos datos que ya has manejado por separado en la matriz de Miller y en la de Pavesic; aquí se cruzan plato a plato, para ver qué pasa cuando dos modelos que parten del mismo coste (costo) y del mismo precio de venta le ponen al mismo plato una etiqueta distinta. Lo que cambia es el segundo eje: el peso de cada plato en el total de unidades vendidas, o el margen de contribución que deja multiplicado por esas unidades. Ese margen ponderado por volumen es el dato que separa a un modelo del otro, y conviene tenerlo presente antes de mirar la tabla de abajo, con Miller y Pavesic uno junto al otro sobre la misma carta.

### La resolución, paso a paso

Los dos caminos parten del mismo par de datos —food cost porcentual y margen de contribución— pero cruzan un segundo eje distinto. Miller (1980) enfrenta el food cost porcentual con la popularidad de cada plato, su peso en el total de unidades vendidas; alta o baja popularidad, food cost alto o bajo, cuatro cuadrantes. Sobre este grupo reparte 8 Winner —popularidad alta y food cost bajo— y 5 Loser —popularidad baja y food cost alto—, con un food cost medio ponderado de los Winner del 26,9 %. En términos cualitativos, Miller es el primer modelo matricial que cruza el food cost con el mix de producto, antecedente directo de la matriz de Kasavana y Smith que ya has trabajado en el resto de este pack.

Pavesic (1983) toma el mismo food cost porcentual pero cambia el segundo eje: en vez de la popularidad, entra el margen de contribución ponderado por las unidades vendidas de cada plato, no el margen unitario de una ración suelta. Sustituir el margen individual por el ponderado es, en términos cualitativos, la corrección que Pavesic le hace a Miller: dos platos con la misma popularidad pueden dejar euros distintos en caja según cuánto valga cada unidad vendida, matiz que desaparece si sólo se cuentan raciones. Con ese eje nuevo el reparto cambia: 7 platos Prime —food cost bajo y margen ponderado alto— y 6 Problem —food cost alto y margen ponderado bajo—, con un margen de contribución ponderado total de los Prime de 21.408 €.

Puestos los dos repartos uno junto al otro, sólo 3 platos mantienen la mejor etiqueta en las cuatro lecturas a la vez —Winner en Miller y Prime en Pavesic, sin fisuras—. En el otro extremo hay 12 platos donde tres o cuatro lecturas no coinciden: uno puede salir Winner por popularidad y Problem por margen ponderado, o Loser por vender poco y Prime porque cada unidad deja un margen alto. En esos 12 cambia la etiqueta según el modelo, y son los que merecen una segunda lectura antes de tocar el precio de venta o retirar un plato de la carta.

### Cómo se lee el resultado

Que Miller y Pavesic no coincidan en un plato no es un error de cálculo: es el aviso de que ese plato tiene un food cost porcentual que no se corresponde con los euros que realmente deja en caja. El food cost porcentual es una proporción sobre el precio de venta y por sí solo no dice nada del volumen que se mueve detrás; el margen de contribución ponderado sí lo dice, porque multiplica lo que deja cada unidad por cuántas se venden. Un plato con food cost porcentual discreto puede parecer, a ojo, sano, y aun así aportar poco margen ponderado si apenas se pide; y uno con food cost porcentual más alto puede sostener buena parte del margen de contribución total de la carta si se vende mucho, aunque su porcentaje solo lo señale como sospechoso.

La decisión no está en elegir un modelo y descartar el otro, sino en usar la discrepancia como filtro: cuando coinciden, el plato no pide ninguna acción urgente; cuando discrepan, toca mirar el precio de venta, el coste y el volumen de ese plato antes de tocarlo, porque el porcentaje solo —sin saber cuántas unidades salen y cuánto margen de contribución dejan— puede llevar a subir un precio que ya funciona o a mantener uno que está lastrando la cuenta.

**Miller y Pavesic sobre el mismo plato, uno al lado del otro**

| Plato | Familia | Miller | Pavesic | Lecturas fuera | Diagnóstico |
|---|---|---|---|---|---|
| Croquetas de jamón ibérico (6 ud) | Entrantes | Winner | Prime | 1 | Popular con margen bajo: subir precio o bajar coste. |
| Ensalada de tomate rosa, ventresca y cebolleta | Entrantes | Winner | Prime | 0 | Las cuatro lecturas coinciden en lo mejor: mantener, destacar en carta y proteger receta y proveedor. |
| Gambas al ajillo | Entrantes | Marginal | Standard | 3 | MC alto con food cost pobre: proteger el margen en euros, revisar precio, no retirar. |
| Huevos rotos con patatas y chistorra | Entrantes | Winner | Prime | 1 | Popular con margen bajo: subir precio o bajar coste. |
| Tabla de quesos de la zona | Entrantes | Loser | Problem | 4 | MC alto con food cost pobre: proteger el margen en euros, revisar precio, no retirar. |
| Alcachofas confitadas con jamón | Entrantes | Marginal | Sleeper | 4 | Food cost sano pero aporta poco margen al total: dale visibilidad antes de retirarlo. |
| Sopa de tomate asado con albahaca | Entrantes | Marginal | Sleeper | 4 | Food cost sano pero aporta poco margen al total: dale visibilidad antes de retirarlo. |
| Solomillo de cerdo ibérico con puré de boniato | Principales | Winner | Prime | 0 | Las cuatro lecturas coinciden en lo mejor: mantener, destacar en carta y proteger receta y proveedor. |
| Bacalao confitado al pil-pil | Principales | Marginal | Problem | 3 | MC alto con food cost pobre: proteger el margen en euros, revisar precio, no retirar. |
| Hamburguesa de vaca madurada con patatas | Principales | Winner | Prime | 1 | Popular con margen bajo: subir precio o bajar coste. |
| Arroz meloso de secreto ibérico y setas | Principales | Marginal | Standard | 3 | Las lecturas discrepan: cada método mide dos de las tres variables (popularidad, margen en euros y food cost). Decide con la que más te duela este mes. |
| Chuletón de vaca madurada (500 g) | Principales | Loser | Problem | 4 | MC alto con food cost pobre: proteger el margen en euros, revisar precio, no retirar. |
| Lubina a la sal | Principales | Loser | Problem | 4 | MC alto con food cost pobre: proteger el margen en euros, revisar precio, no retirar. |
| Pollo de corral asado con patatas | Principales | Winner | Prime | 1 | Popular con margen bajo: subir precio o bajar coste. |
| Lasaña de verduras de temporada | Principales | Marginal | Sleeper | 4 | Food cost sano pero aporta poco margen al total: dale visibilidad antes de retirarlo. |
| Tataki de atún rojo con sésamo | Principales | Loser | Problem | 4 | MC alto con food cost pobre: proteger el margen en euros, revisar precio, no retirar. |
| Tarta de queso cremosa | Postres | Winner | Prime | 0 | Las cuatro lecturas coinciden en lo mejor: mantener, destacar en carta y proteger receta y proveedor. |
| Torrija caramelizada con helado | Postres | Winner | Sleeper | 3 | Popular con margen bajo: subir precio o bajar coste. |
| Coulant de chocolate | Postres | Marginal | Standard | 2 | MC alto con food cost pobre: proteger el margen en euros, revisar precio, no retirar. |
| Fruta de temporada preparada | Postres | Loser | Problem | 4 | Poco pedido, food cost alto y aporta poco margen al total: candidato a retirar o a reformular de raíz. |


---

## 8. Goal Value de Dos Platos

### El enunciado y los datos

El ejercicio toma dos platos de una misma familia de la carta (menú) y les aplica el índice de Hayes y Huffman (1985), el modelo que en el oficio se conoce como Goal Value. Cada plato aporta tres datos propios: su food cost porcentual, su precio de venta sin IVA y las unidades vendidas en el periodo analizado; esos tres números, plato a plato, son los que recoge la tabla siguiente. A ese dato individual se suman dos porcentajes que no cambian de un plato a otro porque describen la estructura de coste (costo) de todo el negocio, no de la receta concreta: el coste de personal sobre ventas, fijado en el 32 % para este ejercicio, y el resto de costes variables sobre ventas —suministros, mantenimiento, comisiones de cobro y similares—, fijado en el 10 %. Estas dos cifras entran igual en el cálculo de cualquier plato de la carta; lo que distingue a un plato de otro es su propio food cost, su propio precio de venta y su propio volumen. Con esos cinco datos —los tres del plato y los dos de la casa— el índice queda listo para calcularse sin necesitar ningún dato externo de mercado ni de competencia.

### La resolución, paso a paso

El cálculo se repite igual para cada plato de la familia, y antes de tocar un solo plato hace falta fijar el objetivo del grupo:

- Primero se calcula el objetivo de la familia: la media ponderada del food cost de todos los platos de esa categoría, ponderando cada uno por su peso en las unidades vendidas del grupo. La lógica es la misma que da el food cost medio ponderado de toda la carta —32,7 %, según la hoja «Datos» de matriz-multimetodo-carta.xlsx—, sólo que aplicada al grupo y no al conjunto del negocio: un plato que vende mucho pesa más en esa media que uno que apenas sale de cocina, esté su food cost donde esté.
- Con el objetivo de la familia ya fijado, cada plato suma a su food cost individual el coste de personal y los otros costes variables —el 32 % y el 10 % de la casa— para obtener el peso conjunto de los tres costes variables sobre su precio de venta sin IVA.
- Ese peso conjunto se contrasta contra el mismo cálculo hecho con el objetivo de la familia en lugar del food cost del plato, y el resultado de ese contraste, ajustado por el volumen vendido del plato dentro de su grupo, es el índice: un número único que sustituye a la vieja matriz de cuadrantes —estrellas, vacas, puzles y perros— por una sola cifra ordenable, plato a plato, familia a familia.

El procedimiento no cambia de una familia a otra: lo único que varía es el objetivo, porque cada familia se pondera con sus propios platos y sus propias ventas.

### Cómo se lee el resultado

El índice no tiene unidades: no es un porcentaje, ni un importe, ni una nota sobre diez. Es un número relativo, y sólo dice algo comparado con el objetivo de su propia familia; no se compara entre familias ni contra el food cost medio de toda la carta. Un plato de entrantes y un plato de postres pueden tener índices parecidos sin que eso signifique nada, porque cada familia se pesa consigo misma: tiene su propio precio de venta, su propio volumen y su propio food cost de referencia.

Lo único que el índice dice, plato a plato, es si ese plato está por encima o por debajo del objetivo que se ha marcado su propia familia. Aplicado a toda la carta de este ejercicio, el resultado deja 9 platos por encima del objetivo de su familia y 11 por debajo, según la hoja «Goal Value» de matriz-multimetodo-carta.xlsx. Ese reparto —9 y 11— no dice todavía qué familia concreta empuja el desequilibrio ni qué plato conviene revisar primero: para eso sirve la tabla siguiente, que cruza cada plato con el objetivo de los suyos y permite localizar, familia por familia, dónde hay margen que recuperar sin tocar el precio de venta y dónde el problema es de volumen y no de coste.

**El índice de cada plato frente al objetivo de su familia**

| Plato | PVP sin IVA (€) | Food cost (%) | Goal Value del plato | Goal Value objetivo de su familia | Lectura |
|---|---|---|---|---|---|
| Croquetas de jamón ibérico (6 ud) | 8,60 € | 24,4 % | 916,77 | 503,30 | Por encima del objetivo |
| Ensalada de tomate rosa, ventresca y cebolleta | 11,80 € | 30,5 % | 698,83 | 503,30 | Por encima del objetivo |
| Gambas al ajillo | 15,50 € | 44,5 % | 301,50 | 503,30 | Por debajo del objetivo |
| Huevos rotos con patatas y chistorra | 9,80 € | 24,5 % | 942,31 | 503,30 | Por encima del objetivo |
| Tabla de quesos de la zona | 13,60 € | 38,2 % | 149,42 | 503,30 | Por debajo del objetivo |
| Alcachofas confitadas con jamón | 10,90 € | 28,4 % | 276,68 | 503,30 | Por debajo del objetivo |
| Sopa de tomate asado con albahaca | 7,20 € | 16,7 % | 372,00 | 503,30 | Por debajo del objetivo |
| Solomillo de cerdo ibérico con puré de boniato | 17,30 € | 32,8 % | 997,46 | 543,03 | Por encima del objetivo |
| Bacalao confitado al pil-pil | 19,10 € | 38,7 % | 428,07 | 543,03 | Por debajo del objetivo |
| Hamburguesa de vaca madurada con patatas | 13,60 € | 31,6 % | 1.128,64 | 543,03 | Por encima del objetivo |
| Arroz meloso de secreto ibérico y setas | 16,40 € | 37,8 % | 556,17 | 543,03 | Por encima del objetivo |
| Chuletón de vaca madurada (500 g) | 32,70 € | 45,3 % | 250,85 | 543,03 | Por debajo del objetivo |
| Lubina a la sal | 21,80 € | 40,8 % | 177,24 | 543,03 | Por debajo del objetivo |
| Pollo de corral asado con patatas | 12,70 € | 29,1 % | 779,39 | 543,03 | Por encima del objetivo |
| Lasaña de verduras de temporada | 11,40 € | 22,8 % | 433,58 | 543,03 | Por debajo del objetivo |
| Tataki de atún rojo con sésamo | 22,40 € | 42,9 % | 251,98 | 543,03 | Por debajo del objetivo |
| Tarta de queso cremosa | 5,90 € | 22,0 % | 860,31 | 436,37 | Por encima del objetivo |
| Torrija caramelizada con helado | 5,50 € | 20,0 % | 351,12 | 436,37 | Por debajo del objetivo |
| Coulant de chocolate | 6,20 € | 25,8 % | 488,70 | 436,37 | Por encima del objetivo |
| Fruta de temporada preparada | 4,50 € | 31,1 % | 50,01 | 436,37 | Por debajo del objetivo |

*El Goal Value es un índice sin unidades: no es un importe, aunque la hoja lo muestre con dos decimales.*


---

## 9. Repricing en Delivery con Packaging y Techo

### El enunciado y los datos

El ejercicio parte de un plato con el escandallo (costeo de recetas) ya resuelto: las croquetas. El canal de reparto añade al coste (costo) por ración dos variables que la sala no conoce —la comisión de la plataforma y el envase, o packaging, del pedido— y fija además un precio techo: el límite por encima del cual el cliente deja de pedir el plato en la aplicación. Estos son los datos de partida:

- Coste por ración de las croquetas: 2,10 €.
- Precio de venta en sala, sin IVA: 8,60 €.
- Comisión del canal: 30 %.
- Envase por pedido: 1,75 €, con 2,5 platos de media por pedido.
- Envase por plato: 0,70 €.
- Precio techo en delivery: 11,60 €.

La comisión del 30 % del ejercicio encaja dentro del rango que manejan las plataformas en España, entre el 15 % y el 35 % más IVA, según la zona, el plan contratado y quién asume el reparto (qamarero.com — Cuánto cobra Glovo a los restaurantes, 2026). Y rara vez es el único coste: el envase puede moverse por su cuenta entre 1,35 € y 2,15 € por pedido, algunas plataformas piden descuentos de visibilidad de entre el 20 % y el 30 %, y las penalizaciones por rendimiento suman hasta 2 puntos más de comisión (qamarero.com — Comisiones delivery: cuánto cobran realmente las plataformas, 2026), extras que casi nunca están a la vista al firmar el contrato.

### La resolución, paso a paso

El primer paso suma el coste por ración de las croquetas y el envase que le corresponde a cada plato: de ahí sale el coste efectivo, la cifra real que hay que cubrir cuando el pedido sale por la puerta con su envase puesto, no sólo con la elaboración terminada.

El segundo paso comprueba qué pasa si en delivery se cobra el mismo precio que en sala. El food cost efectivo es el coste efectivo dividido entre el precio de venta multiplicado por uno menos la comisión, es decir, entre lo que de verdad le queda al restaurante del precio una vez descontado el porcentaje que se lleva la plataforma. Con el precio de sala sin tocar, la hoja «Carta» de simulador-repricing-multicanal.xlsx sitúa ese food cost efectivo de las croquetas en el 46,5 %, muy por encima del food cost objetivo del canal, que es del 40 %: ahí queda a la vista que el precio de sala no sirve para el canal de reparto sin repasarlo antes.

El tercer paso invierte la fórmula anterior: en vez de partir del precio para llegar al food cost, se parte del food cost objetivo para llegar al precio. El precio necesario es el coste efectivo dividido entre el producto del food cost objetivo por uno menos la comisión. Aplicada a las croquetas, esa cuenta fija el precio necesario en 10,00 €: el precio mínimo con el que, descontada la comisión del 30 %, el food cost del plato en delivery vuelve a caer en el 40 % que se persigue.

### Cómo se lee el resultado

El último paso ya no es de cálculo, es de decisión: comparar el precio necesario con el precio techo. En las croquetas, 10,00 € de precio necesario frente a 11,60 € de techo deja margen de sobra, así que el plato entra en el canal de reparto sin forzar el precio hasta el límite que tolera el cliente y se queda en la carta (menú) de delivery con ese precio recalculado.

El mismo criterio se repite plato por plato, y el cuadro siguiente recoge —tal como resume la hoja «Resumen» de simulador-repricing-multicanal.xlsx— el resultado aplicado a toda la carta: 12 platos viables en delivery frente a 8 que hay que excluir o reformular. Cuando el precio necesario supera el precio techo, la respuesta no es subir el precio hasta el límite y esperar que aguante: eso sólo traslada el problema al cliente, que deja de pedir el plato. La salida real pasa por sacar el plato del canal de reparto —dejarlo sólo para la sala, donde el food cost sí funciona— o por reformularlo: bajar el coste por ración, ajustar la ración o cambiar algún ingrediente hasta que el precio necesario vuelva a caber bajo el techo. Y conviene repetir el cálculo cada vez que cambien las condiciones con la plataforma, porque la comisión y los costes que se le suman se mueven con la zona, el plan y la campaña del momento.

**La carta en el canal de reparto: precio necesario contra precio techo**

| Plato | Coste por ración (€) | PVP en sala sin IVA (€) | Food cost en delivery (%) | PVP necesario (€) | Precio techo (€) | ¿Viable? |
|---|---|---|---|---|---|---|
| Croquetas de jamón ibérico (6 ud) | 2,10 € | 8,60 € | 46,5 % | 10,00 € | 11,60 € | Sí |
| Ensalada de tomate rosa, ventresca y cebolleta | 3,60 € | 11,80 € | 52,1 % | 15,36 € | 15,90 € | Sí |
| Gambas al ajillo | 6,90 € | 15,50 € | 70,0 % | 27,14 € | 20,90 € | No: excluir o reformular |
| Huevos rotos con patatas y chistorra | 2,40 € | 9,80 € | 45,2 % | 11,07 € | 13,20 € | Sí |
| Tabla de quesos de la zona | 5,20 € | 13,60 € | 62,0 % | 21,07 € | 18,40 € | No: excluir o reformular |
| Alcachofas confitadas con jamón | 3,10 € | 10,90 € | 49,8 % | 13,57 € | 14,70 € | Sí |
| Sopa de tomate asado con albahaca | 1,20 € | 7,20 € | 37,7 % | 6,79 € | 9,70 € | Sí |
| Solomillo de cerdo ibérico con puré de boniato | 5,67 € | 17,30 € | 52,6 % | 22,75 € | 23,40 € | Sí |
| Bacalao confitado al pil-pil | 7,40 € | 19,10 € | 60,6 % | 28,93 € | 25,80 € | No: excluir o reformular |
| Hamburguesa de vaca madurada con patatas | 4,30 € | 13,60 € | 52,5 % | 17,86 € | 18,40 € | Sí |
| Arroz meloso de secreto ibérico y setas | 6,20 € | 16,40 € | 60,1 % | 24,64 € | 22,10 € | No: excluir o reformular |
| Chuletón de vaca madurada (500 g) | 14,80 € | 32,70 € | 67,7 % | 55,36 € | 44,10 € | No: excluir o reformular |
| Lubina a la sal | 8,90 € | 21,80 € | 62,9 % | 34,29 € | 29,40 € | No: excluir o reformular |
| Pollo de corral asado con patatas | 3,70 € | 12,70 € | 49,5 % | 15,71 € | 17,10 € | Sí |
| Lasaña de verduras de temporada | 2,60 € | 11,40 € | 41,4 % | 11,79 € | 15,40 € | Sí |
| Tataki de atún rojo con sésamo | 9,60 € | 22,40 € | 65,7 % | 36,79 € | 30,20 € | No: excluir o reformular |
| Tarta de queso cremosa | 1,30 € | 5,90 € | 48,4 % | 7,14 € | 8,00 € | Sí |
| Torrija caramelizada con helado | 1,10 € | 5,50 € | 46,8 % | 6,43 € | 7,40 € | Sí |
| Coulant de chocolate | 1,60 € | 6,20 € | 53,0 % | 8,21 € | 8,40 € | Sí |
| Fruta de temporada preparada | 1,40 € | 4,50 € | 66,7 % | 7,50 € | 6,10 € | No: excluir o reformular |


---

## 10. Copa o Botella

### El enunciado y los datos

Abrir un vino por copas es una decisión que se toma con la calculadora delante, no por intuición de sala. El caso es el tinto de la casa: una botella de formato estándar, servida por copa además de por botella entera, con un precio de compra sin IVA de 3,90 €. El establecimiento tiene fijado un precio de venta para la botella y otro, distinto, para la copa suelta: de esa diferencia entre lo que cuesta y lo que se cobra sale el margen y, con él, el beverage cost de cada formato. Las cifras que recoge la hoja «Vinos» de carta-de-bebidas-beverage-cost.xlsx para este vino son las siguientes: la botella rinde 5,0 copas, el coste (costo) por copa es de 0,78 €, el margen por botella es de 9,70 € y el margen por copa de 2,22 €. El beverage cost de la botella entera es del 28,7 %, el de la copa del 26,0 %, y el objetivo fijado para los vinos de la carta (menú) es del 30 %. El promedio ponderado de todos los vinos, con el peso real de ventas de cada referencia, se queda en el 30,2 %, ligeramente por encima del objetivo, sin ser una desviación que exija revisar la carta entera.

### La resolución, paso a paso

El primer paso es partir la botella en las copas que realmente se sirven: 5,0 por cada unidad de compra. El coste por copa resulta de dividir el precio de compra entre esas copas, y por eso 3,90 € repartidos entre 5,0 copas dan los 0,78 € que recoge la ficha. A partir de ahí el resto es leer, no calcular: el margen por botella —9,70 €— y el margen por copa —2,22 €— salen de restar el coste al precio de venta correspondiente, uno para la botella completa y otro para la copa suelta, y los dos ya están resueltos en la plantilla. El beverage cost hace el mismo recorrido en forma de porcentaje: el coste sobre el precio de venta da el 28,7 % de la botella y el 26,0 % de la copa. Esa diferencia es el efecto de vender la misma materia prima en una ración con mejor precio por mililitro: la copa suelta soporta mejor su propio coste que la botella cerrada. Puesto en el contexto de toda la carta de vinos, el 30,2 % ponderado frente al objetivo del 30 % dice que, aunque esta referencia mejora al abrirse por copas, el conjunto sigue necesitando la misma disciplina de compra y de escandallo (costeo de recetas) que cualquier otra familia de la carta.

### Cómo se lee el resultado

El porcentaje mejora con la copa: pasar del 28,7 % al 26,0 % de beverage cost es una ganancia de eficiencia sobre el papel. Pero el margen en euros por botella abierta —los 9,70 € que en teoría genera cada unidad— sólo se materializa si las 5,0 copas encuentran comprador antes de que el vino se oxide o cambie de carta. Servir de más, dejar una copa sin cobrar en una invitación de cortesía o tirar el resto de una botella que ya lleva varios días abierta se come esa diferencia sin que ninguna hoja lo registre: el Excel sigue mostrando un beverage cost del 26,0 % en la copa mientras la botella real, la que de verdad se destapó en cocina, rinde menos margen del que promete la ficha. Por eso el criterio de sala no es sólo mirar el porcentaje de la copa contra la botella, sino vigilar cuántas copas de cada botella abierta llegan a servirse de verdad. Como referencia de mercado —no como cifra española, porque procede de un agregado sectorial de Estados Unidos sin desglose por tipo de bebida— conviene tener presente el rango que maneja el agregado sectorial de getbackbar.com y purimax.com (2026): el beverage cost objetivo se mueve entre el 15 y el 22 % en espirituosos y cócteles, entre el 20 y el 26 % en cerveza de barril, entre el 24 y el 28 % en cerveza de botella o lata, y entre el 18 y el 24 %, con una media del 20 %, como objetivo general sobre la venta de la bebida. El tinto de la casa, con su 26,0 % en copa, se mueve dentro de esa misma franja, aunque el dato que manda a la hora de fijar precio en la propia carta sigue siendo el objetivo interno del 30 % para vinos, no la media de otra categoría de bebida.

**Botella y copa del mismo vino, con su margen y su porcentaje**

| Vino | PVP botella sin IVA (€) | PVP copa sin IVA (€) | Copas por botella | Coste por copa (€) | Margen por botella (€) | Margen por copa (€) | BC botella (%) | BC copa (%) |
|---|---|---|---|---|---|---|---|---|
| Tinto de la casa (Tempranillo joven) | 13,60 € | 3,00 € | 5,0 | 0,78 € | 9,70 € | 2,22 € | 28,7 % | 26,0 % |
| Crianza Rioja | 19,10 € | 4,10 € | 5,0 | 1,22 € | 13,00 € | 2,88 € | 31,9 % | 29,8 % |
| Ribera del Duero roble | 21,80 € | 4,50 € | 5,0 | 1,48 € | 14,40 € | 3,02 € | 33,9 % | 32,9 % |
| Verdejo Rueda | 14,50 € | 3,20 € | 5,0 | 0,84 € | 10,30 € | 2,36 € | 29,0 % | 26,2 % |
| Albariño Rías Baixas | 22,70 € | 4,80 € | 5,0 | 1,58 € | 14,80 € | 3,22 € | 34,8 % | 32,9 % |
| Cava brut nature | 18,20 € | 3,90 € | 5,0 | 1,12 € | 12,60 € | 2,78 € | 30,8 % | 28,7 % |
| Rosado Navarra | 12,70 € | 2,90 € | 5,0 | 0,74 € | 9,00 € | 2,16 € | 29,1 % | 25,5 % |
| Vino dulce Pedro Ximénez | 27,30 € | 4,00 € | 8,0 | 1,44 € | 15,80 € | 2,56 € | 42,1 % | 35,9 % |


---

## 11. Prime Cost de un Mes y su Semáforo

### El enunciado y los datos

El ejercicio parte de un mes cerrado: ventas netas del periodo, consumo de materia prima, salarios brutos y otros costes de personal, la parte que no pasa por nómina pero sí forma parte de mantener la plantilla. A los brutos hay que sumarles el porcentaje de Seguridad Social a cargo de la empresa, fijado en el cuadro de mando en el 33 %. Falta un tercer dato antes de calcular nada: el objetivo de prime cost del formato, que no es el mismo con servicio en mesa (65 %) que en barra o autoservicio (55 %); son dos listones distintos, no una variación menor del mismo número.

El mes es agosto, con ventas netas de 99.600 €. El resto de partidas —consumo de materia prima, salarios brutos, otros costes de personal— ya están volcadas en la hoja «Mensual» de cuadro-de-mando-prime-cost.xlsx, y de ellas sale el coste (costo) de personal completo del mes, con la Seguridad Social ya incluida: 34.517 €. Con ventas netas, coste de personal y el objetivo del formato como vara de medir, el ejercicio ya tiene lo que necesita.

### La resolución, paso a paso

La resolución sigue el orden de la propia hoja. Primero se compone el coste de personal: los brutos, multiplicados por uno más la Seguridad Social —el 33 % ya citado—, más los otros costes de personal. Esa suma, nunca el bruto de la nómina a solas, es la que se compara con la venta: dejar fuera la Seguridad Social por descuido no cambia lo que paga la empresa, pero sí falsea el semáforo. Para agosto, esa composición da 34.517 €.

Con el coste de personal cerrado, el segundo paso es dividir cada partida entre las ventas netas del mes. El food cost sale de poner el consumo de materia prima sobre esas ventas netas: 35,2 % en agosto. El labor cost sale de poner el coste de personal completo —los 34.517 € recién compuestos— sobre la misma base: 34,7 %. Al estar medidos sobre la misma venta neta, se suman sin ajuste alguno: el prime cost es food cost más labor cost, 35,2 % más 34,7 %, que la hoja resuelve en 69,9 %. Por definición, el prime cost es esas dos líneas juntas sobre la venta neta del mismo periodo.

### Cómo se lee el resultado

El 69,9 % de agosto se lee contra el objetivo del formato, no contra una cifra abstracta. Con servicio en mesa el objetivo es 65 %, así que agosto queda por encima del objetivo, tal como marca la propia hoja. Conviene mirar también el acumulado: el prime cost del año está en 63,4 %, dentro de rango, lo que sitúa el problema de agosto como algo puntual y no como una deriva de todo el ejercicio.

Ese mismo 69,9 % significaría otra cosa en barra o autoservicio, porque el objetivo de ese formato no es 65 % sino 55 %, un listón más exigente para las mismas dos partidas. La razón no es que la barra cueste menos en abstracto, sino que reparte su gasto de otra manera. Según «CaixaBankLab × Fundación elBulli — Consumos y beneficios de un restaurante» (2026), el coste de personal sobre la venta neta se sitúa en el 30-35 % con servicio integrado en mesa, y en el 15-25 % con servicio parcial, como autoservicio o barra: la plantilla para llevar el plato a la mesa, cobrar y recoger no es la de un mostrador donde buena parte del recorrido lo hace el cliente. En la misma línea, «Toast — How to Calculate Prime Cost» (2026) sitúa el prime cost esperado en 60-65 % para servicio completo y en 55-60 % para servicio rápido o QSR: el techo baja porque baja el peso del personal, no porque el food cost tenga que apretarse más.

Por eso un prime cost de 69,9 % en sala y ese mismo 69,9 % en barra no piden la misma corrección. En sala, con un labor cost de 34,7 % ya dentro de rango, el margen de mejora está en el food cost: mermas, rendimientos y el escandallo (costeo de recetas) de cada plato, antes de tocar la plantilla. En barra, con un objetivo de personal mucho más bajo, ese mismo 34,7 % ya estaría fuera de rango por sí solo, y la corrección miraría primero los turnos y el dimensionamiento del equipo. Leer el semáforo sin fijarse en el formato lleva, casi siempre, a corregir la partida que no toca.

**Los doce meses con su prime cost y su lectura**

| Mes | Coste de personal con SS (€) | Food cost (%) | Labor cost (%) | Prime cost (%) | Objetivo (%) | Lectura |
|---|---|---|---|---|---|---|
| Enero | 29.988 € | 31,7 % | 33,5 % | 65,2 % | 65,0 % | Por encima del objetivo |
| Febrero | 29.918 € | 32,5 % | 35,6 % | 68,0 % | 65,0 % | Por encima del objetivo |
| Marzo | 30.919 € | 31,8 % | 32,5 % | 64,3 % | 65,0 % | En objetivo |
| Abril | 31.255 € | 31,6 % | 31,1 % | 62,7 % | 65,0 % | En objetivo |
| Mayo | 32.256 € | 31,7 % | 29,9 % | 61,6 % | 65,0 % | En objetivo |
| Junio | 33.656 € | 34,7 % | 30,4 % | 65,1 % | 65,0 % | Por encima del objetivo |
| Julio | 34.657 € | 32,4 % | 29,8 % | 62,3 % | 65,0 % | En objetivo |
| Agosto | 34.517 € | 35,2 % | 34,7 % | 69,9 % | 65,0 % | Por encima del objetivo |
| Septiembre | 31.920 € | 30,1 % | 30,3 % | 60,4 % | 65,0 % | En objetivo |
| Octubre | 31.255 € | 31,3 % | 30,4 % | 61,7 % | 65,0 % | En objetivo |
| Noviembre | 30.919 € | 30,6 % | 31,6 % | 62,2 % | 65,0 % | En objetivo |
| Diciembre | 34.398 € | 31,4 % | 28,1 % | 59,5 % | 65,0 % | En objetivo |
| TOTAL / MEDIA | 385.658 € | 32,1 % | 31,3 % | 63,4 % | 65,0 % | En objetivo |


---

## 12. Menú de Precio Fijo: el Margen lo Decide el Mix

### El enunciado y los datos

El ejercicio parte de un menú de precio fijo con un precio de venta único que agrupa varios cursos, cada uno con dos o tres opciones donde elegir. El precio de venta al público con IVA es 14,50 €, y como todo el consumo en sala tributa al tipo reducido de IVA de restauración —el 10 %, bebida alcohólica incluida—, la base imponible del menú queda en 13,18 €. A ese precio se le suman unos costes (costos) fijos por menú de 0,55 €, la parte de mise en place y de estructura que no cambia se pida lo que se pida. El pack cierra el mes con 100 menús servidos, la cifra sobre la que se proyecta el resultado.

Cada curso lleva su propio escandallo (costeo de recetas), y lo que decide cuánto cuesta el curso no es el coste de un plato suelto, sino el peso de cada opción en lo que de verdad se pide: el mix. El ejercicio compara tres repartos de ese mix con el mismo precio de venta y los mismos costes: uno base, el observado en sala, y dos escenarios que mueven la demanda dentro del propio menú —el A, hacia las opciones de coste más alto; el B, hacia las más económicas—. Ese es el dato de partida: un precio, unos costes fijos y tres mix distintos para las mismas opciones.

### La resolución, paso a paso

El primer paso ya queda resuelto en el propio enunciado: la base imponible sale de descontar el tipo de IVA de restauración al precio de venta con IVA, y son esos 13,18 € los que sirven de referencia para todo lo que viene después, nunca los 14,50 € que paga el comensal en caja.

El segundo paso es el coste medio de cada curso, que se calcula sumando el coste de cada opción multiplicado por su peso en el mix: si una opción se pide más veces, pesa más en la media; si casi nadie la elige, apenas mueve el número aunque sea la más cara. Se repite curso a curso, una vez por cada uno de los tres repartos.

El tercer paso suma los costes medios de todos los cursos y añade los costes fijos por menú, y da el coste total del menú en cada escenario: 5,63 € con el mix base, 5,93 € en el escenario A y 5,35 € en el escenario B. Tres costes de menú distintos para el mismo precio de venta, sólo porque cambia lo que se pide.

Con ese coste total se despejan los dos últimos datos: el food cost, que es el coste total sobre la base imponible, y el margen por menú, que es la base imponible menos el coste total. El mix base deja un food cost del 42,7 % y un margen de 7,55 € por menú; el escenario A sube el food cost hasta el 45,0 %; el escenario B lo baja hasta el 40,6 %. El último paso multiplica ese margen por los 100 menús servidos al mes y da el margen del mes de cada reparto, tal como recoge el cuadro siguiente: 754,93 € con el mix base, 725,18 € en el escenario A y 782,93 € en el escenario B.

### Cómo se lee el resultado

El precio de venta no se mueve en ningún momento de este ejercicio: los 14,50 € con IVA son los mismos en el mix base y en los dos escenarios, y aun así el margen del mes cambia de forma notable entre el reparto más caro de servir y el más barato. Eso es lo que demuestra un menú cerrado: el resultado no lo decide el precio impreso, lo decide lo que el comensal acaba eligiendo dentro de las opciones que se le ofrecen.

Dicho de otro modo, el food cost de este menú no es un número que se calcule una vez y se olvide: es una media que se recalcula cada vez que cambia el mix, y ese mix se mueve con decisiones al alcance de la cocina y de la sala —el orden de las opciones en cada curso, cómo se describen, cuáles se recomiendan en la mesa—, no con subir el precio de venta. Por eso el ejercicio no busca un margen aceptable en abstracto: busca la distancia entre el escenario A y el B con el mismo precio, porque esa distancia es la palanca que hay que trabajar antes de plantearse tocar el menú.

**El mismo menú y el mismo precio, tres resultados según el mix**

| Concepto | Mix base | Escenario A | Escenario B |
|---|---|---|---|
| Coste medio de los primeros (€) | 1,26 € | 1,37 € | 1,18 € |
| Coste medio de los segundos (€) | 3,23 € | 3,39 € | 3,06 € |
| Coste medio de los postres (€) | 0,59 € | 0,62 € | 0,56 € |
| Costes fijos por menú (€) | 0,55 € | 0,55 € | 0,55 € |
| Coste medio total del menú (€) | 5,63 € | 5,93 € | 5,35 € |
| Food cost del menú (%) | 42,7 % | 45,0 % | 40,6 % |
| Margen de contribución por menú (€) | 7,55 € | 7,25 € | 7,83 € |
| Margen sobre los menús servidos al mes (€) | 754,93 € | 725,18 € | 782,93 € |


---


---

## Sobre el autor y condiciones de uso

John Guerrero es CEO de AI Chef Pro y fundador de ChefBusiness Group. En cocina desde los 17 años y consultor gastronómico desde 2010, ha asesorado la apertura de más de 200 establecimientos, incluidos restaurantes con Estrella MICHELIN y Soles Repsol en España y Europa. Más sobre su trabajo en johnguerrero.es.

**Versión 1.0 · septiembre de 2026 · aichef.pro/guia-food-cost-ingenieria-menu · info@aichef.pro**

*Esta guía es un documento de trabajo profesional, no un dictamen fiscal, jurídico ni contable. Los tipos de IVA que se citan son los vigentes en España al cierre de esta edición y están recogidos en celdas editables de las hojas de cálculo precisamente porque cambian: si cambia el tipo, se cambia la celda y todo el libro se recalcula. Los costes, precios de venta, márgenes y porcentajes son valores de ejemplo tomados de las ocho plantillas Excel que acompañan a este pack y sirven para que los sustituyas por los tuyos: ninguno es una previsión de tus resultados ni una recomendación de precio. La calificación fiscal de una operación concreta —qué es servicio de hostelería y qué es entrega de bienes, qué tipo lleva un producto determinado— depende de los hechos de esa operación. Antes de cambiar la carta, el precio de un plato o el tipo con el que facturas, contrasta con tu asesoría.*
