# Guía Food Cost + Ingeniería de Menú

**Escandallo, precios y rentabilidad de tu carta · España 2026**

*John Guerrero · AI Chef Pro · aichef.pro*

20 capítulos, 8 herramientas en Excel con fórmulas vivas y un bonus de 12 ejercicios resueltos para escandallar tu carta, ponerle precio y saber qué plato te da de comer y cuál te lo quita. No es una guía de apertura: está escrita para quien ya sirve todos los días. Todas las cifras que leerás salen de los libros de este mismo pack, así que el texto y las hojas de cálculo dicen lo mismo; cuando cambies un dato en el Excel, la lógica que explica este documento sigue siendo la tuya.

**Versión 1.0 · septiembre de 2026 · aichef.pro/guia-food-cost-ingenieria-menu**

---

## Índice

1. **Para Quién es Esta Guía (y Qué no Vas a Encontrar Aquí)** — nivel de partida, mapa de problema a capítulo y a herramienta, y el glosario de arranque.
2. **Las Cuatro Cifras que Gobiernan tu Carta** — food cost, margen de contribución, prime cost y ticket medio: cuál manda en cada decisión.
3. **IVA, Base Imponible y el Error que Invalida tu Food Cost** — la matriz de IVA por canal y tipo de producto, y por qué el porcentaje se calcula sobre la venta neta.
4. **El Coste Real de Compra: 4 %, 10 % y 21 % en el Mismo Albarán** — los tres tipos de IVA soportado, qué producto lleva cada uno y por qué el IVA de compra no es coste.
5. **Del Bruto al Neto: Merma, Rendimiento y el Test que Sustituye a la Tabla** — despiece, cocción y subproductos: cómo medir tu propia merma y cuánto cuesta de verdad el kilo limpio.
6. **La Ficha de Escandallo que Aguanta una Auditoría** — cantidad neta, merma, cantidad bruta, coste por ración y precio objetivo, línea a línea.
7. **Food Cost Teórico vs Real: Dónde se Escapa el Dinero** — el consumo real con stock inicial, compras y stock final, y las cuatro causas de la desviación.
8. **Prime Cost: la Métrica que Mide la Salud del Negocio** — producto más personal en una sola cifra, con el umbral español del 65 % y el del 55 % en barra.
9. **Cuatro Formas de Poner Precio a un Plato** — factor sobre el coste, margen objetivo en euros, precio de mercado y valor percibido.
10. **Psicología de Precios: lo Demostrado y lo que es Leyenda** — efecto señuelo, nombres descriptivos y formato del precio, cada uno con su estudio y su salvedad.
11. **Ingeniería de Menú I: Kasavana & Smith Bien Hecho** — popularidad por margen, el umbral del 70 % dividido por familia y qué se hace con cada cuadrante.
12. **Ingeniería de Menú II: lo que la Matriz Clásica no Ve** — Miller, Pavesic, Goal Value y LeBruto: tres variables y ningún método que las mida todas.
13. **Cuando los Métodos Discrepan: el Protocolo de Decisión** — leer las cuatro lecturas a la vez, entender la discrepancia y decidir entre reformular, resubir, rediseñar o retirar.
14. **Carta Corta, Menú de Precio Fijo, Buffet y Banquete** — cuando el precio ya está puesto y el margen lo decide el mix: menú del día, buffet, hotel y catering.
15. **Multicanal: Sala, Take Away y Delivery** — comisión, packaging, IVA por canal y precio techo: cuánto subir en cada canal y qué plato excluir.
16. **Beverage Cost: la Bodega Como Cuenta de Resultados Propia** — copa contra botella, barril, cócteles y el IVA por canal: la bodega tiene sus propios objetivos.
17. **Costeo por Lote en Obrador y Pastelería** — rendimiento de tanda, mano de obra por hora, packaging y escalado: por qué la ración no es la unidad.
18. **Cuando Sube el Proveedor: Protocolo de Re-escandallado** — disparadores, calendario, dónde mirar los precios y cómo subir sin perder al cliente.
19. **Caso Integral: una Carta Entera, de Principio a Fin** — la carta de ejemplo recorrida entera: ficha, matriz, precio, multicanal y plan de 90 días.
20. **Cuándo tu Excel se Queda Corto** — el criterio para saltar de la hoja de cálculo al software y a los agentes de IA, con la cuenta delante.

---

## 1. Para Quién es Esta Guía (y Qué no Vas a Encontrar Aquí)

### Qué damos por sabido y qué no

Esta guía arranca donde otras terminan: con la carta ya impresa, el local abierto y el food cost dando un número que no convence. No hay aquí ni una línea sobre licencias de actividad, obra, inversión inicial o plan de negocio. Quien busque eso necesita otro recurso; quien ya opera y quiere entender por qué su margen de contribución no cuadra, puede seguir leyendo.

Damos por sabido que el lector sabe lo que es una ficha técnica, que ha oído hablar de escandallo (costeo de recetas) y que entiende un porcentaje sobre ventas. Lo que no damos por sabido es el criterio: cuándo ese porcentaje es una señal de alarma, qué herramienta de análisis corresponde a cada síntoma y cómo se toma una decisión de carta con datos en la mano en lugar de con intuición. Eso es lo que aporta este documento.

El pack se divide en dos piezas con funciones distintas. El Kit de Escandallos contiene las plantillas por formato de negocio y el sistema de control diario: ahí viven las fichas, los rendimientos y el seguimiento de compras. Esta guía aporta el criterio de decisión y las ocho herramientas de análisis de carta. Quien tenga los dos materiales no duplica trabajo: cada uno resuelve una capa diferente del problema, y las referencias cruzadas entre ambos están señaladas a lo largo del texto para que el salto sea inmediato.

El hilo conductor de todos los capítulos es una carta de ejemplo que aparece en los ocho libros del pack. Se trata de un caso modelado, no de un cliente real ni de un negocio identificable: los datos son coherentes entre sí y están calibrados para que las herramientas muestren situaciones representativas, no ideales. Esa carta tiene 20 platos dados de alta, mueve 4.870 unidades vendidas al mes y genera 59.029 € de ventas netas en el periodo de referencia, con un food cost medio ponderado del 32,7 %. Esos números viven en la hoja «Datos» de matriz-multimetodo-carta.xlsx y son los mismos que el lector verá en cada análisis: si en algún momento la cifra del texto y la de la hoja no coinciden, la hoja manda.

El pack trabaja con un food cost objetivo del 30 % —alineado con la referencia de mercado que recoge el informe «CaixaBankLab × Fundación elBulli — Consumos y beneficios de un restaurante» (2026), que sitúa el rango sano entre el 25 % y el 35 % sobre venta— y con un objetivo de prime cost del 65 %, que es el parámetro activo en la hoja «Parámetros» de cuadro-de-mando-prime-cost.xlsx. Esos dos umbrales son el punto de partida de todos los ejercicios; el lector puede ajustarlos a su realidad, y el propio cuadro de mando está construido para absorber ese cambio sin romper ninguna fórmula.

Un apunte de vocabulario para lectores de Hispanoamérica, que es la única vez que aparecerá el paréntesis: a lo largo de la guía se escribe «escandallo» por «costeo de recetas», «coste» por «costo» y «carta» por «menú». Cuando el texto hable de un menú de precio fijo, lo llamará menú, porque ahí sí es la palabra correcta en cualquier variante del español. El resto del tiempo, carta es carta.

---

### Tu problema, su capítulo y su herramienta

La forma más rápida de entrar en esta guía no es por la página uno, sino por el síntoma. El food cost medio ponderado de la carta de ejemplo está en 32,7 %, dos puntos y siete décimas por encima del objetivo del 30 % que establece la hoja «Ficha» de ficha-escandallo-base.xlsx. Esa distancia puede tener orígenes muy distintos: un plato estrella con coste (costo) disparado, una familia de platos que arrastra el promedio hacia arriba, un precio de venta que no se ha revisado, o una combinación de los tres. Cada origen tiene su herramienta, y cada herramienta tiene su capítulo.

El cuadro siguiente organiza esa correspondencia: problema real en la primera columna, capítulo que lo trata en la segunda, archivo del pack que lo resuelve en la tercera. No es una tabla de contenidos; es un mapa de entrada para quien ya sabe dónde le duele y no quiere leer lo que no necesita.

Hay síntomas que esta guía no trata porque corresponden a otra capa del negocio. La estructura completa de costes de un restaurante, según el mismo informe «CaixaBankLab × Fundación elBulli — Consumos y beneficios de un restaurante» (2026), incluye personal en el rango del 30 % al 35 % sobre venta, alquiler entre el 5 % y el 10 %, y gastos generales con un ideal cercano al 17 %, lo que deja un EBITDA sano en la horquilla del 10 % al 13 %. El prime cost —producto más personal— es el primer indicador de que esa estructura está o no está en equilibrio, y por eso el cuadro de mando del pack lo vigila con el objetivo del 65 %. Pero el labor cost, el alquiler y los gastos generales quedan fuera del alcance de esta guía: aquí se trabaja la parte de producto y carta, que es donde el operador tiene margen de maniobra más inmediato y donde las decisiones de ingeniería de menú producen efecto en el siguiente ciclo de compras.

Lo que no se va a encontrar aquí, dicho sin rodeos: no hay negociación de proveedores paso a paso —ese material está en el bono del Kit de Escandallos y remitiremos a él cuando llegue el momento—, no hay análisis de rentabilidad por turno ni por canal de venta, y no hay ninguna proyección a doce meses construida sobre los datos de la carta de ejemplo. Las cifras que aparecen en el texto son las que están en las hojas; las cuentas las hace el lector con sus propios números, no con extrapolaciones de un caso modelado.

### Qué hace esta guía y qué hace el Kit de Escandallos

El punto de partida de este documento es una carta que ya se está sirviendo. No hay aquí ni un párrafo sobre licencias, obra, inversión inicial ni plan de negocio: quien necesite eso tiene que buscar otra herramienta. Lo que sí hay es un método para leer lo que esa carta está haciendo con el dinero y para tomar decisiones sobre ella con criterio, no con intuición.

La división del trabajo dentro del pack es precisa y conviene entenderla antes de abrir ningún archivo. El Kit de Escandallos aporta las plantillas por formato de negocio —restaurante de sala, barra, colectividades, delivery— y el sistema de control diario: fichas técnicas, hojas de mermas, registro de compras y cuadro de seguimiento de desviaciones. Esta guía aporta otra cosa: el criterio de decisión y las ocho herramientas de análisis de carta que permiten saber qué platos sostienen el negocio, cuáles lo lastran y qué palancas mover primero. Quien tenga los dos materiales no duplica trabajo: el Kit produce los datos y esta guía los interpreta.

El food cost objetivo con el que trabaja el pack es el 30 %, cifra que coincide con la media del sector hostelero español según el informe «CaixaBankLab × Fundación elBulli — Consumos y beneficios de un restaurante» (2026), que sitúa el rango sano entre el 25 % y el 35 % sobre venta. Ese mismo informe describe la estructura de costes de referencia de un restaurante español: producto en torno al 30 %, personal y servicio integrado entre el 30 % y el 35 %, alquiler entre el 5 % y el 10 %, y gastos generales entre el 13 % y el 20 % sobre venta, con un EBITDA sano resultante de entre el 10 % y el 13 %; por debajo del 10 % el negocio requiere reestructuración. Dentro de esa arquitectura, el prime cost —producto más personal— es el indicador que concentra la mayor parte de la gestión, y el objetivo con el que trabaja el cuadro de mando incluido en el pack es el 65 %, recogido en la hoja «Parámetros» de cuadro-de-mando-prime-cost.xlsx.

La carta de ejemplo que recorre todo el pack es un caso modelado, no un cliente real. Tiene 20 platos dados de alta, genera 4.870 unidades vendidas al mes y cierra el periodo con 59.029 € de ventas netas, con un food cost medio ponderado del 32,7 %. Esos números están en la hoja «Datos» de matriz-multimetodo-carta.xlsx y son los mismos en los ocho libros del pack: lo que cambia entre herramienta y herramienta es el ángulo desde el que se analiza esa carta, no los datos de partida. Trabajar siempre sobre el mismo caso permite comparar resultados entre métodos sin perder el hilo, y permite también que el lector vea con claridad qué decisión cambia cuando cambia un solo parámetro. La hoja «Inversión» de plan-financiero-3-anos.xlsx no forma parte de este pack: se menciona aquí solo para dejar claro que no está, porque es la herramienta de apertura y este documento empieza donde aquella termina.

La tabla de abajo recoge, para cada problema concreto que puede traer el lector, el capítulo que lo trata y la herramienta del pack que lo resuelve. Conviene leerla antes de seguir, porque marca el camino más corto según el punto de partida de cada uno.

---

### Cómo llamamos aquí a cada cosa

Este documento se escribe en español de España y usa los términos del oficio tal como se usan en sala y en cocina. Cuando un término tiene una forma distinta en Hispanoamérica, se indica la equivalencia la primera vez que aparece y después se usa siempre la forma española.

Escandallo (costeo de recetas) es la ficha que descompone un plato en ingredientes, cantidades brutas, mermas y coste (costo) unitario resultante. A partir de aquí, «escandallo» y «coste» son las formas que se usan en todo el documento. La carta (menú) es el conjunto de platos que el establecimiento ofrece a la venta; «menú» se reserva para el menú de precio fijo, que es un formato de venta distinto con su propia lógica de escandallo. «Plato» designa cualquier referencia de la carta, sea entrante, principal, postre o elaboración de barra.

Los anglicismos que se mantienen son los que el oficio ha adoptado sin sustituto claro: food cost, prime cost, labor cost, beverage cost, delivery, take away y packaging. No se usan «contribution margin», «menu engineering» ni otros términos en inglés que tienen traducción asentada en la hostelería española: se escribe «margen de contribución» e «ingeniería de menú» porque son las formas que aparecen en los convenios, en los informes sectoriales y en la formación profesional del sector.

El cuadro siguiente detalla qué libro del pack resuelve cada problema, con el nombre exacto del archivo y de la hoja donde empieza el trabajo.

**Tu problema, el capítulo que lo trata y la herramienta que lo resuelve**

| Si tu problema es… | Capítulo | Herramienta del pack |
|---|---|---|
| No sé si mi food cost está bien calculado | 3 y 4 | ficha-escandallo-base.xlsx |
| Compro mucho y no sé cuánto llega al plato | 5 | rendimiento-mermas-producto.xlsx |
| Tengo que rehacer la ficha de un plato | 6 | ficha-escandallo-base.xlsx |
| Mi food cost real no cuadra con el teórico | 7 | cuadro-de-mando-prime-cost.xlsx |
| Vendo mucho y no gano | 8 | cuadro-de-mando-prime-cost.xlsx |
| No sé qué precio ponerle a un plato nuevo | 9 y 10 | precio-objetivo-multi-metodo.xlsx |
| No sé qué plato quitar de la carta | 11, 12 y 13 | matriz-multimetodo-carta.xlsx |
| Quiero montar un menú de precio fijo | 14 | matriz-multimetodo-carta.xlsx |
| El delivery me deja menos de lo que parece | 15 | simulador-repricing-multicanal.xlsx |
| La bodega no sé si gana o pierde | 16 | carta-de-bebidas-beverage-cost.xlsx |
| Me han subido el proveedor y no sé qué tocar | 18 | precio-objetivo-multi-metodo.xlsx |
| Tengo el diagnóstico y no lo aplico | 19 y 20 | plan-accion-90-dias.xlsx |

*Los ocho libros comparten la misma carta de ejemplo, así que puedes saltar al capítulo que te interese sin perder el hilo de las cifras.*


---

## 2. Las Cuatro Cifras que Gobiernan tu Carta

### Food cost porcentual: qué mide y qué no mide

El food cost porcentual mide la proporción que el coste (costo) de materia prima representa sobre el precio de venta neto. Eso es todo lo que mide. No mide cuántos euros entran en caja, no mide si el equipo de cocina tarda veinte minutos en elaborar ese plato, y no mide si ese plato se vende diez veces al mes o doscientas. Confundir lo que mide con lo que decide es el error más caro que se comete al revisar una carta.

El rango sano para la restauración española se sitúa entre el 25 % y el 35 % sobre venta, con una media de mercado en torno al 30 % (CaixaBankLab × Fundación elBulli — Consumos y beneficios de un restaurante, 2026). Ese rango no es universal: según el formato, el punto de partida cambia. La restauración tradicional trabaja habitualmente entre el 28 % y el 32 %, el bar de tapas entre el 28 % y el 35 %, la pizzería entre el 25 % y el 30 %, la cafetería entre el 20 % y el 28 %, y el fine dining puede bajar al 20-25 % precisamente porque el ticket alto absorbe el coste fijo por cubierto (qamarero.com — Food cost restaurante: cómo calcularlo y optimizarlo, 2026). Ninguna de esas horquillas es un objetivo en sí misma: son referencias para saber si algo merece revisión.

La carta de ejemplo del pack cierra el mes con un food cost medio ponderado del 32,7 %, que está dentro del rango sano. Ese 32,7 % sale de la hoja «Datos» de matriz-multimetodo-carta.xlsx y se calcula sobre las 4.870 unidades vendidas en el mes, no sobre la media simple de los platos de la carta. La media simple da un número que no existe en la realidad del negocio: si un plato con food cost del 40 % se vende tres veces y otro con food cost del 28 % se vende cuatrocientas, el promedio aritmético de ambos porcentajes no describe nada que haya ocurrido en esa cocina. Solo la ponderación por unidades vendidas produce una cifra que se puede comparar con los 59.029 € de ventas netas del mes.

El porcentaje ordena la carta, ayuda a detectar platos con coste descontrolado y sirve de argumento en la negociación con proveedores. Pero no paga ninguna factura. Para eso hace falta la cifra siguiente.

### Margen de contribución: los euros que caen en la caja

El margen de contribución de un plato es lo que queda de su precio de venta una vez descontado el coste de materia prima. No es beneficio: todavía no ha pagado ni una hora de personal, ni el alquiler, ni la luz. Es el euro bruto que ese plato aporta para cubrir el resto de la estructura. Esa distinción importa cada vez que alguien propone retirar un plato porque «tiene un food cost alto».

La tesis que gobierna este capítulo es directa: el porcentaje ordena, el euro paga. Un plato con un food cost del 20 % que genera pocos euros por unidad puede ser peor negocio que uno con food cost alto que deja muchos euros por cubierto, siempre que se venda con suficiente frecuencia. El porcentaje bajo no compensa un margen de contribución raquítico multiplicado por pocas unidades.

En la carta de ejemplo, el margen de contribución medio ponderado es de 8,16 € por unidad vendida, calculado también sobre las 4.870 unidades del mes, en la misma hoja «Datos» de matriz-multimetodo-carta.xlsx. Multiplicar ese margen por las unidades vendidas no es una operación que haya que hacer aquí: los totales ya están en el libro. Lo que sí conviene fijar es el criterio: cuando se evalúa si un plato se mantiene o se retira de la carta, la variable que manda es el margen de contribución, no el food cost. Un plato que vende mucho y deja un margen de contribución sólido sostiene la cuenta aunque su porcentaje de coste supere la media. Retirarlo por el porcentaje, sin mirar los euros, es un error de diagnóstico.

El cuadro siguiente muestra el desglose mensual de la carta de ejemplo con ambas cifras por familia de platos.

### Prime cost: producto y personal en la misma línea

El prime cost suma el coste de materia prima y el labor cost, y los expresa juntos sobre ventas. Es la cifra que impide engañarse, porque recoge el trasvase más frecuente en cocina: bajar el food cost aumentando el trabajo de elaboración. Un restaurante que sustituye producto semielaborado por producto en bruto puede reducir su coste de materia prima varios puntos y ver cómo ese ahorro reaparece íntegro en la nómina, en horas extra o en la necesidad de un cocinero adicional. El food cost mejora en el papel; el prime cost no se mueve, o empeora.

La estructura de referencia para un restaurante español sitúa el coste de personal entre el 30 % y el 35 % sobre venta cuando el servicio está integrado, con un coste de producto en torno al 30 %, lo que coloca el prime cost en una banda que deja margen para el alquiler, los gastos generales y un EBITDA sano de entre el 10 % y el 13 % (CaixaBankLab × Fundación elBulli — Consumos y beneficios de un restaurante, 2026). Por debajo del 10 % de EBITDA, la estructura requiere revisión.

En el cuadro de mando del pack, la hoja «Mensual» de cuadro-de-mando-prime-cost.xlsx recoge el año completo: ventas netas de 1.232.200 €, coste de materia prima sobre ventas del 32,1 %, labor cost del 31,3 % y prime cost resultante del 63,4 %. El margen que queda tras ese prime cost es de 451.142 €, que es el punto de partida para cubrir alquiler, suministros, gastos generales y lo que finalmente quede como resultado de explotación. El cuadro de mando mensual con el detalle de cada partida aparece en la tabla de abajo.

La regla de uso de las tres cifras es la siguiente. Para decidir si un plato se retira o se mantiene en la carta, manda el margen de contribución: los euros por unidad vendida y el volumen de ventas de ese plato. Para negociar con proveedores o revisar mermas y porciones, manda el food cost: el porcentaje da el argumento y marca el objetivo de la negociación. Para saber si el negocio en su conjunto aguanta la estructura de costes que tiene, manda el prime cost: es la única cifra que pone producto y personal en la misma línea y hace visible el trasvase entre ambas partidas.

### Ticket medio y margen por cubierto

El porcentaje ordena; el euro paga. Esa es la tensión que atraviesa cualquier carta que lleve tiempo sin revisarse, y entenderla cambia el criterio con el que se toman las decisiones de precio.

Tomemos el caso de la carta de ejemplo del pack. El food cost medio ponderado es 32,7 % (hoja «Datos» de matriz-multimetodo-carta.xlsx), un número que, comparado con la referencia del sector, se sitúa en el extremo superior del rango sano de 25-35 % que recoge el informe «CaixaBankLab × Fundación elBulli — Consumos y beneficios de un restaurante» (2026). Alguien podría leer ese 32,7 % y concluir que la carta tiene un problema. La tabla de abajo demostrará que la lectura correcta es más matizada.

El margen de contribución medio ponderado de esa misma carta es 8,16 € por unidad vendida. Sobre 4.870 unidades al mes y 59.029 € de ventas netas, ese margen es el que financia todo lo que viene después: personal, alquiler, suministros y beneficio. Nótese que el margen de contribución no ha pagado todavía ninguna de esas partidas; es el punto de partida, no el resultado.

Ahora el caso límite que justifica la tesis. Un plato con food cost del 20 % sobre un precio de venta bajo puede dejar menos euros por cubierto que un plato con food cost del 34 % sobre un precio de venta alto. El porcentaje del primero es más «limpio» sobre el papel, pero el segundo aporta más margen absoluto a la caja cada vez que sale de la cocina. Si la decisión se toma mirando solo el porcentaje, se puede retirar precisamente el plato que más contribuye a cubrir los costes fijos.

El ticket medio sin IVA en el mes de partida del plan de 90 días es 27,4 (hoja «KPI de Seguimiento» de plan-accion-90-dias.xlsx) y el margen de contribución por cubierto en ese mismo momento es 18,1. Esos dos números se leen juntos: el primero dice cuánto ingresa el local por comensal; el segundo, cuánto queda disponible para cubrir estructura antes de que el cliente pague la cuenta y se marche.

El margen de contribución medio ponderado y el food cost medio ponderado de la carta se calculan siempre sobre las unidades realmente vendidas, no sobre la media simple de los platos que figuran en la carta. La media simple asigna el mismo peso a un plato que se vende tres veces al día que a uno que se vende tres veces al mes, y produce un número que no corresponde a ninguna realidad operativa. La hoja «Datos» de matriz-multimetodo-carta.xlsx aplica la ponderación por unidades: el resultado es el 32,7 % y los 8,16 € citados, y son los únicos que tienen sentido para tomar decisiones.

---

### Cuál manda en cada decisión

El prime cost es la cifra que impide el autoengaño más habitual en cocina: reducir el food cost aumentando la elaboración. Cuando se sustituye un producto semielaborado por materia prima en bruto, el coste de género baja, pero el tiempo de preparación sube y eso aparece en la nómina. El ahorro no desaparece; se desplaza de una línea a otra. El prime cost lo captura porque suma food cost y labor cost en un solo indicador.

En la carta de ejemplo, el coste de materia prima sobre ventas del año es 32,1 % y el labor cost es 31,3 %, lo que arroja un prime cost de 63,4 % (hoja «Mensual» de cuadro-de-mando-prime-cost.xlsx). Sobre unas ventas netas anuales de 1.232.200 €, el margen tras prime cost es 451.142 €. Ese margen tiene que cubrir el alquiler, los suministros, los gastos generales y dejar un EBITDA operativo. La estructura de referencia que publica «CaixaBankLab × Fundación elBulli — Consumos y beneficios de un restaurante» (2026) sitúa el producto en torno al 30 %, el personal entre 30 y 35 % y los gastos generales en un ideal próximo al 17 %, con un EBITDA sano resultante de entre 10 y 13 %; por debajo de ese umbral, el negocio requiere reestructuración. El cuadro siguiente permite leer mes a mes si el prime cost se mantiene en zona de control o si alguna de sus dos patas está derivando.

El rango de food cost varía según el formato. «qamarero.com — Food cost restaurante: cómo calcularlo y optimizarlo» (2026) recoge que el fine dining trabaja habitualmente entre 20 y 25 %, la restauración tradicional entre 28 y 32 %, el bar de tapas entre 28 y 35 %, la pizzería entre 25 y 30 % y la cafetería entre 20 y 28 %. Esos rangos son orientativos y dependen del ticket, del nivel de elaboración y del mix de ventas real, no de la carta impresa.

La regla de uso queda así:

- Para decidir si un plato se retira o se mantiene en carta, manda el margen de contribución: es el único indicador que mide lo que ese plato aporta en euros reales cada vez que se vende.
- Para ir a negociar con un proveedor, manda el food cost: es el porcentaje que refleja el peso de esa materia prima sobre la venta y el que justifica o no un volumen de compra mayor a cambio de un precio menor.
- Para saber si el negocio aguanta su estructura de costes, manda el prime cost: es la suma de las dos partidas controlables más grandes y el primer indicador que se deteriora cuando algo falla en cocina o en sala.

Ninguna de las tres cifras es prescindible, y ninguna sustituye a las otras dos.

**El cuadro de mando mensual: food cost, labor cost y prime cost (cuadro-de-mando-prime-cost.xlsx, hoja «Mensual»)**

| Mes | Ventas netas (€) | Food cost (%) | Labor cost (%) | Prime cost (%) | Objetivo (%) | Lectura |
|---|---|---|---|---|---|---|
| Enero | 89.600 € | 31,7 % | 33,5 % | 65,2 % | 65,0 % | Por encima del objetivo |
| Febrero | 84.100 € | 32,5 % | 35,6 % | 68,0 % | 65,0 % | Por encima del objetivo |
| Marzo | 95.200 € | 31,8 % | 32,5 % | 64,3 % | 65,0 % | En objetivo |
| Abril | 100.400 € | 31,6 % | 31,1 % | 62,7 % | 65,0 % | En objetivo |
| Mayo | 107.900 € | 31,7 % | 29,9 % | 61,6 % | 65,0 % | En objetivo |
| Junio | 110.700 € | 34,7 % | 30,4 % | 65,1 % | 65,0 % | Por encima del objetivo |
| Julio | 116.200 € | 32,4 % | 29,8 % | 62,3 % | 65,0 % | En objetivo |
| Agosto | 99.600 € | 35,2 % | 34,7 % | 69,9 % | 65,0 % | Por encima del objetivo |
| Septiembre | 105.500 € | 30,1 % | 30,3 % | 60,4 % | 65,0 % | En objetivo |
| Octubre | 102.700 € | 31,3 % | 30,4 % | 61,7 % | 65,0 % | En objetivo |
| Noviembre | 97.900 € | 30,6 % | 31,6 % | 62,2 % | 65,0 % | En objetivo |
| Diciembre | 122.400 € | 31,4 % | 28,1 % | 59,5 % | 65,0 % | En objetivo |
| TOTAL / MEDIA | 1.232.200 € | 32,1 % | 31,3 % | 63,4 % | 65,0 % | En objetivo |

*La última fila es el total del año y sus porcentajes son ponderados, no la media de los doce meses: un mes flojo pesa lo que factura, no una doceava parte.*

**Las tres familias de la carta de ejemplo (matriz-multimetodo-carta.xlsx, hoja «Datos»)**

| Familia | Platos | Uds vendidas | Mix sobre la carta (%) | MC medio ponderado (€) | Food cost medio ponderado (%) | Ventas netas del mes (€) |
|---|---|---|---|---|---|---|
| Entrantes | 7 | 1.730 | 35,5 % | 7,46 € | 30,7 % | 18.636 € |
| Principales | 9 | 2.020 | 41,5 % | 10,80 € | 35,6 % | 33.854 € |
| Postres | 4 | 1.120 | 23,0 % | 4,48 € | 23,2 % | 6.539 € |


---

## 3. IVA, Base Imponible y el Error que Invalida tu Food Cost

### Sobre qué número se calcula el food cost

El escandallo (costeo de recetas) trabaja siempre sobre la base imponible, nunca sobre el precio que el cliente ve en carta. La confusión nace de un gesto aparentemente inocente: dividir el coste de la ración entre el precio con IVA. El resultado es un food cost más bajo del real, y esa es la peor dirección posible del error, porque lleva a pensar que el plato rinde mejor de lo que rinde.

La ficha de la hoja «Ficha» de ficha-escandallo-base.xlsx lo muestra con precisión. El coste por ración del plato, sin IVA, es 5,67 €. El precio de venta sin IVA es 17,30 € y el precio de carta con IVA asciende a 19,03 €. El food cost real del plato, calculado sobre la base imponible, es 32,8 %. Si en lugar de dividir entre 17,30 € se divide entre 19,03 €, el porcentaje cae y la lectura se vuelve optimista sin que nada haya mejorado en la cocina.

Hay un segundo error que aparece con menos frecuencia pero que distorsiona igual: meter el IVA soportado de los ingredientes dentro del coste. Cuando el negocio está en régimen general de IVA, ese impuesto se deduce en la declaración periódica y no es un coste real de la ración. La hoja «Ficha» recoge el IVA soportado total de la ficha en 0,56 €, lo que elevaría el coste aparente a 6,23 €. Dividir esa cifra entre la base imponible del precio de venta da un food cost de 36,0 %, tres puntos y dos décimas por encima del real. Tres puntos en food cost no son un matiz: son decisiones de carta equivocadas, subidas de precio innecesarias o platos eliminados que en realidad sí eran rentables. El margen de contribución del plato con el precio de venta actual es 11,63 €, y ese dato solo es fiable si el coste y el precio de venta están ambos expresados sin IVA.

La regla es una sola: base imponible en el numerador, base imponible en el denominador.

### La matriz de IVA repercutido: tres canales por tres tipos de producto

El fundamento de la matriz está en la distinción que establece la Ley 37/1992, del Impuesto sobre el Valor Añadido, entre servicio de hostelería y entrega de bienes. Cuando hay servicio, el tipo reducido cubre todo el consumo, incluida la bebida alcohólica, porque lo que se presta es un servicio de restauración, no se vende un bien aislado. Así lo recoge el artículo 91, apartado Uno, número 2, número 2 de esa ley en su texto consolidado, con la última modificación introducida por la Ley 7/2024, en vigor desde el 22 de diciembre de 2024. En consecuencia, en sala tanto la comida como la bebida alcohólica tributan al 10 %, tal como figura en la hoja «Parámetros» de simulador-repricing-multicanal.xlsx.

Cuando no hay servicio de hostelería, la operación es una entrega de bienes y entran en juego las exclusiones del artículo 91. La comida elaborada entregada sin servicio tributa al 10 % como alimento ordinario, según el artículo 91, apartado Uno, número 1, número 1 de la misma ley, confirmado para el supuesto exacto de reparto a domicilio por la Dirección General de Tributos en la consulta vinculante V2254-22, de 26 de octubre de 2022. Sin embargo, las bebidas alcohólicas quedan excluidas del tipo reducido en ese canal y pasan al tipo general del 21 %, conforme a los artículos 90 y 91, apartado Uno, número 1, número 1 de la Ley 37/1992, como ratifica la misma consulta V2254-22. Los refrescos, zumos y gaseosas con azúcares o edulcorantes añadidos siguen el mismo camino: desde el 1 de enero de 2021 tributan al 21 %, por la redacción dada al artículo 91, apartado Uno, número 1, número 1 por la Ley 11/2020 de Presupuestos Generales del Estado para 2021, en su artículo 69. El tipo general del 21 % es el tipo residual que recoge el artículo 90 de la Ley 37/1992 para todo lo que no queda amparado por el artículo 91.

El ejemplo más claro de la consecuencia práctica es el botellín de cerveza: en la barra tributa al 10 % porque se presta un servicio; si el cliente se lo lleva o llega por delivery, tributa al 21 % porque es una entrega de bienes excluida del tipo reducido. No es una rareza ni un caso límite, es la consecuencia directa de la distinción entre canal de servicio y canal de entrega, y la tabla que aparece a continuación recoge los seis cruces resultantes con los tipos que ya están cargados en la hoja «Parámetros» de simulador-repricing-multicanal.xlsx.

La consecuencia operativa es inmediata: si la carta de delivery replica la de sala sin ajuste de precio de venta, el margen por canal no es el mismo, porque la base imponible sobre la que se calcula el food cost varía con el tipo aplicado. Esa divergencia se trabaja en el capítulo del multicanal con el simulador de repricing, pero el punto de partida es tener los tipos correctos en cada celda. Por eso los tipos de IVA están en celdas editables con nota en la hoja «Parámetros», y las fórmulas del libro los leen mediante INDEX y MATCH: si mañana una norma modifica un tipo, se cambia el valor en esa celda y el libro entero se recalcula sin tocar una sola fórmula.

### En sala va todo al tipo reducido, bebida alcohólica incluida

El error que más distorsiona el food cost no está en el escandallo (costeo de recetas): está antes, en el denominador. Cuando se divide el coste por ración entre el precio con IVA, el resultado es un porcentaje más bajo del real, y esa dirección del error es la peor posible porque hace creer que el margen aguanta cuando no aguanta. El food cost se calcula siempre sobre la base imponible, es decir, sobre el precio de venta sin IVA.

La ficha de la hoja «Ficha» de ficha-escandallo-base.xlsx lo muestra con números propios del pack. El coste por ración es 5,67 € y el precio de venta sin IVA es 17,30 €: el food cost real queda en 32,8 %. Si en lugar del precio sin IVA se usara el precio con IVA, que es 19,03 €, el porcentaje caería y daría una lectura artificialmente cómoda. La tabla de abajo recoge exactamente ese contraste para que no quede ninguna duda sobre qué celda es el denominador correcto.

El fundamento de que en sala todo el consumo tribute al 10 % —comida y bebida alcohólica por igual— está en el artículo 91.Uno.2.2.º de la Ley 37/1992, del Impuesto sobre el Valor Añadido (texto consolidado, última modificación introducida por la Ley 7/2024, en vigor desde el 22 de diciembre de 2024). Lo que se presta en un restaurante, una terraza o una barra es un servicio de hostelería, no una entrega de bienes. Esa calificación jurídica arrastra a todo el consumo al tipo reducido, sin excepción por tipo de producto: la copa de vino, el gin-tonic y la cerveza de barril van al 10 % exactamente igual que el plato principal, porque el objeto del contrato es el servicio, no la botella.

El margen de contribución del plato con el precio de venta actual es 11,63 €, calculado sobre la base imponible de 17,30 €. Ese es el dato que alimenta la ingeniería de menú: un margen calculado sobre el precio con IVA sería menor en términos absolutos y llevaría a decisiones de carta equivocadas.

### Sin servicio hay entrega de bienes: qué se va al tipo general

Cuando no hay servicio de hostelería, la operación cambia de naturaleza jurídica: es una entrega de bienes y las exclusiones del artículo 91.Uno.1.1.º de la Ley 37/1992 entran en juego. La comida elaborada para llevar o a domicilio sigue al 10 %, según confirma la Dirección General de Tributos en la consulta vinculante V2254-22 (DGT, 26 de octubre de 2022), emitida precisamente sobre el supuesto de una plataforma de reparto con repartidores subcontratados, que es el escenario exacto del delivery de restauración.

Lo que cambia de tipo son dos categorías concretas:

- Las bebidas alcohólicas quedan excluidas del tipo reducido en entrega de bienes y pasan al 21 %, tipo general del artículo 90 de la Ley 37/1992, según los artículos 90 y 91.Uno.1.1.º de esa misma norma, ratificados por la consulta V2254-22.
- Los refrescos, zumos y gaseosas con azúcares o edulcorantes añadidos tributan también al 21 % desde el 1 de enero de 2021, por la redacción dada al artículo 91.Uno.1.1.º por la Ley 11/2020 de Presupuestos Generales del Estado para 2021, en su artículo 69. Los zumos y refrescos sin azúcares ni edulcorantes añadidos no están afectados por esa exclusión.

El mismo botellín de cerveza que en la barra lleva un 10 % lleva un 21 % si el cliente lo recibe en casa: no es una rareza fiscal, es la consecuencia directa de que en un caso se presta un servicio y en el otro se entrega un bien. La hoja «Parámetros» de simulador-repricing-multicanal.xlsx recoge los tres canales y los tres tipos de producto en celdas editables con nota; las fórmulas del libro los leen mediante INDEX y MATCH, de modo que si mañana cambia cualquier tipo, basta con modificar la celda correspondiente y el libro entero se recalcula sin tocar una sola fórmula.

La consecuencia operativa es inmediata: si la carta de delivery es la misma que la de sala, el margen por canal no es el mismo, porque el IVA repercutido sobre alcohol y refrescos azucarados sube del 10 % al 21 % y eso afecta a la base imponible sobre la que se calcula el food cost. Cómo construir precios distintos por canal sin romper la percepción de valor es el problema que se trabaja en el capítulo del multicanal.

### El mismo plato con IVA y sin IVA: cuántos puntos de food cost te inventas

El food cost se calcula dividiendo el coste de la ración entre la base imponible, es decir, el precio de venta sin IVA. Dividirlo entre el precio con IVA produce un resultado más bajo del real, y esa es la peor dirección posible del error: te hace creer que el plato va mejor de lo que va.

Tomemos la ficha de la hoja «Ficha» de ficha-escandallo-base.xlsx. El coste por ración, sin IVA, es 5,67 €. El precio de venta sin IVA es 17,30 €. El food cost real del plato con ese precio de venta es 32,8 %. Hasta aquí, todo correcto. El error aparece cuando alguien coge el precio con IVA, 19,03 €, y lo usa como denominador sin quitarle el impuesto: el cociente baja y la ficha parece más saneada de lo que es. La diferencia no es cosmética; es la distancia entre una decisión fundamentada y una carta mal calibrada.

El segundo error, menos frecuente pero igual de grave, es meter el IVA soportado de los ingredientes dentro del coste de la ración. La hoja «Ficha» lo calcula de forma separada: el IVA soportado total de la ficha es 0,56 €, lo que llevaría el coste aparente a 6,23 €. Dividir ese importe entre la base imponible daría un food cost de 36,0 %, tres puntos y dos décimas por encima del real. El IVA soportado no es coste: es un crédito fiscal que se recupera en la liquidación periódica. Incluirlo en el escandallo (costeo de recetas) es contabilizar dos veces un importe que Hacienda te devuelve. El cuadro siguiente muestra ambos escenarios lado a lado para que la diferencia quede sin ambigüedad.

El margen de contribución del plato con el precio de venta actual es 11,63 €. Ese es el dato que alimenta la ingeniería de menú: si el denominador del food cost está inflado con IVA, el margen de contribución también queda distorsionado y la clasificación de los platos en la matriz de rentabilidad-popularidad pierde fiabilidad.

### Por qué el tipo vive en una celda y no dentro de la fórmula

La matriz fiscal de la restauración no es plana. En sala, todo el consumo tributa al tipo reducido del 10 %, alcohol incluido, porque la operación es una prestación de servicios de hostelería, no una entrega de bienes. Así lo establece la Ley 37/1992, del Impuesto sobre el Valor Añadido, art. 91.Uno.2.2.º, en su texto consolidado tras la Ley 7/2024, en vigor desde el 22 de diciembre de 2024. El servicio de hostelería envuelve toda la consumición: la copa de vino y la caña llevan el mismo tipo que el plato principal, 10 %, porque lo que se presta es un servicio, y la exclusión de las bebidas alcohólicas del tipo reducido solo opera cuando hay una entrega de bienes sin ese servicio.

Fuera de la sala, la lógica cambia de raíz. La comida elaborada entregada a domicilio o para llevar es una entrega de bienes y tributa como alimento ordinario al 10 %, según el art. 91.Uno.1.1.º de la misma ley, confirmado para el supuesto exacto de plataformas de reparto por la Dirección General de Tributos en la consulta vinculante V2254-22, de 26 de octubre de 2022. Pero en ese mismo canal, el botellín de cerveza que en la barra lleva un 10 % pasa a tributar al tipo general del 21 %, porque sin servicio de hostelería las bebidas alcohólicas quedan excluidas del tipo reducido, tal como recogen los arts. 90 y 91.Uno.1.1.º de la Ley 37/1992, refrendados por la misma consulta V2254-22. Lo mismo ocurre con los refrescos, zumos y gaseosas con azúcares o edulcorantes añadidos: desde el 1 de enero de 2021 tributan al 21 % en entrega de bienes, por la redacción dada al art. 91.Uno.1.1.º por la Ley 11/2020 de Presupuestos Generales del Estado para 2021, en su art. 69. El tipo general del 21 % es el tipo residual que recoge el art. 90 de la Ley 37/1992 para todo lo no comprendido en el art. 91.

La consecuencia operativa es directa: si la carta de delivery es la misma que la de sala, el margen por canal no es el mismo, porque el IVA repercutido sobre la bebida alcohólica y sobre el refresco azucarado sube once puntos al salir del local. Eso se trabaja en el capítulo del multicanal, donde se recalcula el precio de venta por canal para mantener el food cost objetivo. La tabla de abajo recoge los tipos por canal y por tipo de producto tal como están parametrizados en la hoja «Parámetros» de simulador-repricing-multicanal.xlsx: sala comida 10 %, sala bebida alcohólica 10 %, delivery comida 10 %, delivery refresco azucarado 21 %, delivery bebida alcohólica 21 %.

Esos valores viven en celdas editables con nota de fuente, y las fórmulas del libro los leen mediante INDEX y MATCH. Si mañana una modificación legislativa altera cualquiera de esos tipos, se cambia el valor en la celda correspondiente de la hoja «Parámetros» y el libro entero se recalcula sin tocar una sola fórmula. Escribir el tipo dentro de la fórmula, en cambio, obliga a rastrear cada cálculo que lo usa, y en un libro con escandallos, repricing y simulación de margen por canal, ese rastreo manual es la antesala del error silencioso.

**La matriz de IVA repercutido: canal por tipo de producto (simulador-repricing-multicanal.xlsx, hoja «Parámetros»)**

| Canal | Comida | Refresco o bebida azucarada | Bebida alcohólica |
|---|---|---|---|
| Sala | 10,0 % | 10,0 % | 10,0 % |
| Take away | 10,0 % | 21,0 % | 21,0 % |
| Delivery | 10,0 % | 21,0 % | 21,0 % |

*Las nueve casillas son editables y llevan su nota con el artículo que las sostiene. Si trabajas fuera de España, cambias las nueve y el resto del libro se recalcula solo.*

**El IVA soportado no es coste: qué pasa si lo metes dentro (ficha-escandallo-base.xlsx, hoja «Ficha»)**

| Concepto | Valor |
|---|---|
| IVA soportado total de la ficha (€) | 0,56 € |
| Coste con IVA soportado (solo tesorería) (€) | 6,23 € |
| Food cost si contases el IVA como coste (%) — NO se hace así | 36,0 % |

*El IVA de las compras se deduce en la declaración: es tesorería, no coste. Meterlo en el escandallo sube el food cost sin que nadie haya gastado un euro de más.*


---

## 4. El Coste Real de Compra: 4 %, 10 % y 21 % en el Mismo Albarán

### Los tres tipos que conviven en la misma caja de la compra

Cuando llega el albarán del proveedor, lo habitual es que no venga con un solo tipo de IVA soportado sino con tres conviviendo en el mismo documento. El aceite de oliva, los huevos y las harinas panificables tributan al 4 %; el resto de alimentos preparados, las bebidas sin alcohol y los productos de limpieza alimentaria van al 10 %; y el packaging, el menaje desechable o las bebidas alcohólicas compradas para llevar fuera de sala tributan al 21 %, según establece la Ley 37/1992, art. 90 (1992-12-29). Que los tres tipos aparezcan en el mismo pedido no es una anomalía: es la norma en cualquier cocina con una compra mínimamente diversificada.

El albarán de ejemplo de la hoja «Albarán e IVA soportado» de ficha-escandallo-base.xlsx lo ilustra con precisión: la base imponible total asciende a 768,40 €, la cuota de IVA total suma 84,41 € y el total con IVA que el proveedor cobra es 852,81 €. La diferencia entre la base y el total es exactamente lo que la Hacienda Pública devuelve o compensa en la liquidación periódica, siempre que el negocio esté en régimen general y pueda deducirse el IVA soportado. El cuadro siguiente desglosa esas líneas partida a partida.

La regla del escandallo (costeo de recetas) es una sola y no admite excepciones en condiciones normales: se trabaja siempre con el precio sin IVA. Si el negocio puede deducirse el IVA soportado, ese importe no es un coste real; meterlo en la ficha técnica equivale a contar el mismo gasto dos veces. La hoja «Ficha» de ficha-escandallo-base.xlsx lo demuestra con números propios: el coste por ración sin IVA es 5,67 €, el IVA soportado total de esa ficha suma 0,56 € y, si se cometiera el error de incluirlo, el coste aparente subiría a 6,23 €. El food cost correcto del plato es 32,8 %; el food cost erróneo contando el IVA como coste sube a 36,0 %. Esa diferencia de puntos porcentuales no es un matiz contable: es la distancia entre una decisión de precio bien calibrada y una mal calibrada.

Hay un caso en que esta regla se invierte y conviene conocerlo antes de configurar las fichas. Si el negocio no puede deducirse el IVA soportado, ese IVA sí se convierte en coste real y debe entrar en el escandallo. Determinar si esa situación aplica requiere revisar el régimen con la asesoría fiscal: no es una decisión que deba tomar el jefe de cocina ni el responsable de sala, y este capítulo no entra en los regímenes porque cada caso tiene condicionantes propios.

El packaging merece un párrafo específico porque genera confusión con frecuencia. Una caja de delivery, un vaso de cartón o una bolsa de papel no son alimentos: son envases o materiales auxiliares, y la Ley 37/1992, art. 90 los sitúa en el tipo general del 21 %. El hecho de que dentro de esa caja viaje un plato que tributa al 10 % no arrastra el envase al tipo reducido. Son dos líneas distintas en el albarán y dos tipos distintos en la ficha. Quien escandalla un plato de delivery y no separa el coste del packaging del coste del alimento está mezclando bases imponibles diferentes y distorsionando el food cost del plato.

---

### La lista cerrada del tipo superreducido

El tipo superreducido del 4 % no se aplica por categoría amplia ni por intuición: la Ley 37/1992, art. 91.Dos.1.1.º, letras a a g (1992-12-29, última incorporación RDL 4/2024, letra g, con efectos desde 2025-01-01), establece una lista cerrada. Lo que no está en ella y no está excluido por el art. 91.Uno.1.1.º va directamente al tipo reducido ordinario del 10 %. No hay zona gris ni interpretación favorable por analogía.

Los productos que integran esa lista cerrada son los siguientes:

- Pan común y masa de pan común congelada.
- Harinas panificables.
- Leche producida por cualquier especie animal: natural, certificada, pasterizada, concentrada, desnatada, esterilizada, UHT, evaporada y en polvo.
- Quesos.
- Huevos.
- Frutas, verduras, hortalizas, legumbres, tubérculos y cereales, que tienen su amparo en la letra f del mismo artículo.
- Aceites de oliva, incorporados por el RDL 4/2024 (art. 2) en la letra g, con efectos permanentes desde el 1 de enero de 2025, tras una rampa transitoria en 2024 que los situó al 5 % entre julio y septiembre y al 2 % entre octubre y diciembre de ese año.

Nada más. El aceite de girasol no está en la lista y tributa al 10 %. La carne, el pescado, el marisco, las conservas, los lácteos distintos de leche y queso, los zumos y los productos elaborados van al tipo reducido ordinario salvo que encajen en alguna de las letras anteriores por su composición principal, lo cual requiere criterio y, en caso de duda, consulta al proveedor sobre cómo lo declara él en su factura.

La incorporación del aceite de oliva es el cambio más relevante en la estructura del IVA soportado de una cocina española en los últimos años, y tiene consecuencia directa en las fichas: cualquier escandallo que incluya aceite de oliva y que se haya construido antes de que la norma entrara en vigor debe revisarse para asegurarse de que la columna de tipo impositivo refleja el 4 % y no el 10 % que se aplicaba con anterioridad. La tabla de abajo recoge la clasificación completa de compras habituales con su tipo correspondiente, extraída de la hoja «Albarán e IVA soportado» de ficha-escandallo-base.xlsx.

### Un albarán de ejemplo, línea a línea

Cuando llega un albarán del proveedor con partidas de distinta naturaleza, el primer trabajo es separar las bases imponibles antes de trasladar ningún número a la ficha de escandallo (costeo de recetas). El albarán del ejemplo que acompaña este tramo, reproducido en la tabla de abajo, suma una base imponible total de 768,40 €, una cuota de IVA total de 84,41 € y un total con IVA de 852,81 €. Esas tres cifras proceden de la hoja «Albarán e IVA soportado» de ficha-escandallo-base.xlsx, y el lector puede confrontarlas línea a línea con su propio albarán real.

El albarán mezcla tres tipos porque el proveedor sirve géneros de distinta naturaleza. Cada línea cae en uno de estos tramos:

- **4 %** — tipo superreducido, regulado en el artículo 91, apartado Dos, número 1, número 1, letras a a g de la Ley 37/1992 (última incorporación: RDL 4/2024, letra g, con efectos desde el 1 de enero de 2025). La lista es cerrada: pan común, harinas panificables, leche, quesos, huevos, frutas, verduras, hortalizas, legumbres, tubérculos, cereales y aceites de oliva. Cualquier alimento que no figure en esa enumeración y no esté excluido por el artículo 91, apartado Uno, número 1, número 1, va al tipo reducido ordinario. El aceite de oliva es la incorporación más reciente: tributa al 4 % desde el 1 de enero de 2025, tras una rampa transitoria en 2024, en virtud del RDL 4/2024 (art. 2), publicado el 27 de junio de 2024. La letra que lo recoge es la g; la letra f preexistente es la de frutas, verduras, hortalizas, legumbres, tubérculos y cereales.

- **10 %** — tipo reducido ordinario, también en el artículo 91 de la Ley 37/1992. Aquí caen la carne, el pescado, los mariscos, las conservas, el aceite de girasol y, en general, todos los alimentos que no están en la lista cerrada del 4 % ni excluidos de ella.

- **21 %** — tipo general, residual respecto al artículo 91, regulado en el artículo 90 de la misma Ley 37/1992. Aplica a las bebidas alcohólicas y refrescos azucarados fuera de sala, al menaje no alimentario y a todo lo no comprendido en el artículo 91.

El caso del packaging merece atención específica. La caja de delivery no es un alimento: es un envase de cartón o plástico destinado al transporte, y por eso tributa al 21 %, aunque el plato que va dentro lleve el tipo reducido. Lo mismo ocurre con los cubiertos de un solo uso, las bolsas de papel o los soportes de presentación que no forman parte del producto alimentario. Cuando el proveedor sirve en el mismo albarán género de cocina y material de packaging, el restaurador recibe un documento con los tres tipos en columnas distintas, y separar esas columnas antes de archivar es el único modo de cuadrar la contabilidad del IVA soportado sin errores.

### El IVA soportado es tesorería: dónde entra y dónde no

La regla del escandallo es una sola: se costea con el precio sin IVA. El IVA de compra se deduce en la liquidación periódica, de modo que no es un coste real para el negocio, sino un anticipo que la Hacienda Pública devuelve al compensarlo con el IVA repercutido. Meterlo en la ficha equivale a contarlo dos veces: una en la ficha y otra en el modelo de liquidación.

El efecto numérico es visible en la hoja «Ficha» de ficha-escandallo-base.xlsx. El coste por ración sin IVA es 5,67 €. El IVA soportado total que corresponde a esa ración asciende a 0,56 €, y si se suma al coste se obtiene un coste por ración con el IVA soportado dentro de 6,23 €. El food cost correcto del plato, calculado sobre la base imponible, es 32,8 %. Si en cambio se parte del 6,23 €, el food cost erróneo contando el IVA como coste sube a 36,0 %. Esa diferencia de puntos porcentuales no es un matiz técnico: altera la decisión de precio, el umbral de rentabilidad y cualquier comparativa entre platos de la carta.

Existe, sin embargo, un caso en que esta regla deja de ser válida: cuando el negocio no puede deducirse el IVA soportado, ese IVA sí se convierte en coste real y debe entrar en el escandallo. Las circunstancias que generan esa situación dependen del régimen fiscal aplicable y de la actividad concreta, y determinarlas es trabajo de la asesoría contable, no de la ficha técnica. Si hay cualquier duda sobre si el negocio puede o no deducir, la consulta con el asesor debe hacerse antes de configurar las fórmulas de la hoja «Ficha», porque cambiar el criterio a mitad del ejercicio obliga a recalcular todos los escandallos ya cerrados.

El cuadro siguiente, extraído de la hoja «Albarán e IVA soportado» de ficha-escandallo-base.xlsx, muestra el albarán completo con las tres columnas de IVA desglosadas y la base imponible de cada línea, de modo que el lector puede replicar la lectura con cualquier albarán de su proveedor habitual.

**Qué compra lleva cada tipo de IVA soportado (ficha-escandallo-base.xlsx, hoja «Albarán e IVA soportado»)**

| Tipo | Qué compra lleva este tipo |
|---|---|
| 4 % | Pan común, harinas panificables, leche, quesos, huevos, frutas, verduras, hortalizas, legumbres, tubérculos, cereales y aceites de oliva (art. 91.Dos.1.1.º; el aceite de oliva desde el 1-ene-2025 por el RDL 4/2024). |
| 10 % | Resto de alimentos y bebidas no alcohólicas sin azúcares añadidos: carnes, pescados, conservas, aceites de semillas, agua (art. 91.Uno.1.1.º). |
| 21 % | Bebidas alcohólicas; refrescos, zumos y gaseosas con azúcares o edulcorantes añadidos; y todo lo no alimentario: packaging, menaje, productos de limpieza (art. 90). |

**Un albarán con los tres tipos dentro, línea a línea (ficha-escandallo-base.xlsx, hoja «Albarán e IVA soportado»)**

| # | Producto | Cantidad | Unidad | Precio/ud sin IVA (€) | Base imponible (€) | Tipo (%) | Cuota de IVA (€) | Total con IVA (€) |
|---|---|---|---|---|---|---|---|---|
| 1 | Solomillo de cerdo ibérico | 12,0 | kg | 15,80 € | 189,60 € | 10 % | 18,96 € | 208,56 € |
| 2 | Tomate rosa | 20,0 | kg | 3,80 € | 76,00 € | 4 % | 3,04 € | 79,04 € |
| 3 | Aceite de oliva virgen extra | 25,0 | L | 7,20 € | 180,00 € | 4 % | 7,20 € | 187,20 € |
| 4 | Queso curado de oveja | 4,0 | kg | 18,50 € | 74,00 € | 4 % | 2,96 € | 76,96 € |
| 5 | Vino tinto crianza (botella) | 24,0 | ud | 6,10 € | 146,40 € | 21 % | 30,74 € | 177,14 € |
| 6 | Refresco de cola (lata) | 48,0 | ud | 0,55 € | 26,40 € | 21 % | 5,54 € | 31,94 € |
| 7 | Envases para llevar (caja) | 2,0 | ud | 38,00 € | 76,00 € | 21 % | 15,96 € | 91,96 € |
|  | TOTAL ALBARÁN |  |  |  | 768,40 € |  | 84,41 € | 852,81 € |

*La columna que entra en el escandallo es la base imponible. La cuota de IVA de este albarán se deduce en la declaración del trimestre.*


---

## 5. Del Bruto al Neto: Merma, Rendimiento y el Test que Sustituye a la Tabla

### Las tres mermas que no son la misma: despiece, cocción y desperdicio

La merma no es un porcentaje del sector que se copia de una tabla de internet y se aplica a todos los productos de la misma categoría. Es un dato de tu proveedor, de tu calibre de compra y de la manera en que tu equipo limpia. Dos cocinas que reciben la misma lubina entera del mismo puerto pueden obtener rendimientos distintos según el tamaño de los ejemplares, el cuchillo que usan y el criterio con el que retiran la piel. Eso significa que la tabla orientativa que acompaña este capítulo —la que encontrarás en la hoja «Mi Tabla de Mermas» de rendimiento-mermas-producto.xlsx— sólo sirve como punto de partida provisional mientras no tienes tu propia medición.

Conviene separar con precisión tres fenómenos que el oficio agrupa bajo la misma palabra. La merma de despiece es la que ocurre en frío, sobre la tabla, antes de que el producto entre en calor: espinas, piel, hojas externas, huesos, cáscaras. La merma de cocción es la pérdida de peso que sufre el producto ya limpio cuando se aplica calor: el agua que suelta una pieza de carne al horno, la reducción de un filete a la plancha, la contracción de un músculo al vapor. La merma por desperdicio es la que no debería existir y que sin embargo existe: el género que caduca, el que se corta mal y no se puede emplatat, el que se tira porque la mise en place fue excesiva. Las tres restan margen, pero se gestionan de forma distinta y se registran en momentos distintos.

El error más frecuente en el escandallo (costeo de recetas) es aplicar sólo la merma de despiece y olvidar la de cocción. Si el pollo de corral al horno pierde un 28,0 % de su peso durante la cocción —dato que recoge la hoja «Merma de Cocción» de rendimiento-mermas-producto.xlsx— y además tiene una merma de despiece propia del ave entera, quien sólo aplica uno de los dos números está costeando de menos. La pérdida media por cocción de las pruebas registradas en esa misma hoja es del 27,3 %, lo que indica que la cocción no es un ajuste menor: es una segunda merma de magnitud comparable a la del despiece en muchas categorías, y se aplica encima de la primera, no en lugar de ella.

---

### El protocolo del test de rendimiento, paso a paso

El test de rendimiento se hace con una báscula, el mismo día y con la pieza real que compras a tu proveedor habitual. No sirve pesar un calibre distinto ni usar un ejemplar de muestra: el número tiene que salir del género que entra en tu cocina.

El procedimiento tiene tres pesadas sobre la misma pieza:

- Se pesa el producto tal como llega del proveedor, sin limpiar. Ese es el peso bruto.
- Se limpia con el criterio habitual de la cocina y se pesa el producto limpio listo para cocinar. Ese es el peso neto.
- Se recoge por separado todo lo que tiene valor de uso —cabezas, espinas, recortes con carne, hojas externas aprovechables— y se pesa también. Ese es el peso del subproducto aprovechable.

Tres medidas de la misma pieza, el mismo día, anotadas en la hoja «Test de Rendimiento» de rendimiento-mermas-producto.xlsx. En los 10 productos medidos en esa hoja, el peso bruto total comprado fue de 31,50 kilos y el peso limpio total obtenido fue de 19,07 kilos, lo que arroja un rendimiento medio ponderado del 60,5 % y una merma media ponderada del 39,5 %. El coste total de compra de esos tests fue de 237,35 €.

De esos números sale el dato que va a la ficha técnica: el factor de corrección. Es el inverso del rendimiento, y su función es convertir la cantidad neta que necesitas para una ración en la cantidad bruta que debes comprar. Si la lubina entera rinde un 51,7 %, su factor de corrección es 1 dividido entre 0,517. Ese número —que la hoja calcula automáticamente— es el que multiplica el peso neto de la receta para obtener el peso de compra. Sin él, cada ficha técnica subestima la cantidad real que sale del almacén.

El coste neto por kilo limpio de la lubina sin aprovechar el subproducto es de 28,84 €, y el sobrecoste sobre el precio del kilo bruto es de 12,73 €. Esa diferencia es lo que desaparece del margen cuando el escandallo se hace sobre el precio de compra bruto en lugar de sobre el coste del kilo limpio. La alcachofa, con un rendimiento del 38,0 %, y el mejillón con concha, con un rendimiento del 20,0 %, ilustran en la tabla de abajo hasta qué punto el precio de compra y el coste real de uso pueden ser magnitudes muy alejadas entre sí.

---

### Qué pasa con el subproducto: cabezas, espinas y recortes

Aprovechar el subproducto reduce el coste neto del kilo limpio, pero sólo si el valor de uso que se le asigna es real. La condición es concreta: ese subproducto tiene que sustituir a algo que ibas a comprar. Si las cabezas de gamba se convierten en un fondo que reemplaza a un fondo envasado que de otro modo habrías pedido al proveedor, el ahorro es real y se puede cuantificar. Si ese fondo se hace porque «no se tira nada» pero luego no entra en ninguna receta o se acaba tirando igualmente, el valor de uso asignado es ficticio y el escandallo queda inflado.

En los tests recogidos en la hoja «Test de Rendimiento», el valor de uso total de los subproductos asciende a 5,15 €. No es una cifra despreciable dentro de un lote de 237,35 € de compra, pero tampoco cambia el coste de forma radical: lo que cambia es la precisión. La lubina aprovechada cuesta 27,63 € el kilo limpio frente a los 28,84 € sin aprovechar. El ahorro por aprovechar las cabezas de la gamba es de 1,43 €. Esos importes sólo son válidos si la cocina tiene una receta concreta que consume ese subproducto de forma sistemática y si el fondo o la preparación resultante sustituye efectivamente a una compra.

El criterio para registrar el valor de uso es el coste de lo que sustituye, no el precio de venta de un hipotético plato que podría hacerse con esos recortes. Si las espinas de lubina van a un fumet que reemplaza a un fumet comprado, el valor de uso es el precio de ese fumet comprado por la cantidad que se obtiene. Si no hay sustitución directa, el valor de uso es cero y el coste neto del kilo limpio se calcula sin descuento.

La hoja «Mi Tabla de Mermas» de rendimiento-mermas-producto.xlsx refleja el estado actual de la medición: 6 categorías ya tienen medición propia y 6 categorías aún usan la referencia orientativa. El objetivo no es tener todas las categorías medidas de una vez, sino ir sustituyendo la referencia por el dato propio cada vez que se hace un pedido relevante, hasta que la tabla de referencia quede como respaldo residual y no como fuente principal del escandallo.

### El coste del kilo limpio y el factor de corrección

La merma no es un porcentaje del sector: es el resultado de tu proveedor, de tu calibre de compra y de la mano de quien limpia. Dos cocinas que reciben la misma lubina entera el mismo martes pueden obtener rendimientos distintos porque una la filetea a máquina y la otra a cuchillo, porque una compra piezas de calibre superior y la otra trabaja con piezas más pequeñas, o simplemente porque el cocinero que hace el despiece lleva diez años haciéndolo y el de la otra casa lleva diez semanas. La tabla de mermas copiada de internet recoge una media de condiciones que no son las tuyas, y aplicarla en el escandallo (costeo de recetas) es aceptar un error de partida que se acumula en cada ficha.

El protocolo correcto exige tres medidas de la misma pieza, el mismo día. Se pesa el producto tal como llega del proveedor: ese es el peso bruto. Se limpia con el procedimiento habitual de la cocina, sin atajos ni esmero especial, porque lo que se mide es el proceso real, no el ideal. Se pesa el producto limpio listo para porcionar: ese es el peso neto aprovechable. Y se pesa por separado todo lo que se puede reutilizar —cabezas, espinas, pieles, recortes con valor de uso— porque ese subproducto tiene un coste asignado y modifica el cálculo final. Sin esas tres medidas no hay test; con dos de las tres se está estimando, no midiendo.

La hoja «Test de Rendimiento» de rendimiento-mermas-producto.xlsx recoge los resultados de 10 productos medidos con ese protocolo. El peso bruto total comprado en los tests fue de 31,50 kilos; el peso limpio obtenido, 19,07 kilos. El rendimiento medio ponderado de ese conjunto es 60,5 %, lo que equivale a una merma media ponderada de 39,5 %. El coste total de compra de los tests ascendió a 237,35 €, y el valor de uso asignado a los subproductos recuperados suma 5,15 €.

La lubina entera es el caso que mejor ilustra el salto entre precio de compra y coste real. Su rendimiento en el test es 51,7 %: de cada kilo que entra por la puerta de servicio, algo más de la mitad llega al plato. Sin aprovechar ningún subproducto, el coste neto por kilo limpio de la lubina asciende a 28,84 €. Aprovechando las cabezas y las espinas para un fondo que sustituye a algo que se iba a comprar, ese coste baja a 27,63 €. La diferencia entre el precio del kilo bruto y el coste neto del kilo limpio es de 12,73 €: ese es el sobrecoste que desaparece de la ficha cuando se trabaja con el precio de compra en lugar de con el coste real.

El número que viaja a la ficha técnica es el factor de corrección, que es el inverso del rendimiento. Si el rendimiento es 51,7 %, el factor de corrección es 1 dividido entre 0,517. Ese factor convierte la cantidad neta que pide la receta en la cantidad bruta que hay que comprar: si la ración necesita 180 gramos limpios, se multiplica por el factor y se obtiene los gramos que se pesan en el albarán. Sin ese paso, el escandallo subestima el coste de cada plato de forma sistemática.

La decisión de aprovechar el subproducto merece un criterio claro: las cabezas de gamba, las espinas de la lubina o las hojas exteriores de la alcachofa sólo compensan si el valor de uso que se les asigna es real. Valor de uso real significa que ese fondo, ese caldo o esa guarnición sustituye a algo que de otro modo se iba a comprar. Si el fondo de pescado se hace con las espinas pero la cocina también compra fumet envasado porque el volumen no alcanza, el ahorro es parcial y hay que calcularlo así. Las cabezas de gamba, por ejemplo, generan un ahorro de 1,43 € en el test: esa cifra sólo es válida si el bisque o el aceite que se elabora con ellas reemplaza una compra real, no si se hace porque «no se tira nada» y acaba en el cubo igualmente.

La merma de cocción es un número distinto y se aplica encima de la merma de despiece, nunca en su lugar. El pollo de corral al horno pierde 28,0 % de su peso durante la cocción, según la hoja «Merma de Cocción» de rendimiento-mermas-producto.xlsx; la pérdida media por cocción de las pruebas registradas en esa misma hoja es 27,3 %. Quien sólo aplica la merma de despiece está costeando el kilo limpio antes de que entre al horno, y quien sólo aplica la merma de cocción ignora lo que se perdió en la tabla de corte. Las dos mermas son independientes, se miden por separado y se encadenan en la ficha: primero se calcula cuánto hay que comprar para obtener el neto de la receta, y después se ajusta ese neto por la pérdida que introduce el calor.

### Tu tabla de mermas: cuándo puedes dejar de usar la referencia

Las tablas de mermas de cocina profesional que circulan en manuales y recursos formativos son orientativas por construcción. Los rangos que recogen son amplios precisamente porque agregan condiciones muy distintas —calibres, proveedores, técnicas, temperaturas de recepción— y ninguno de esos rangos lleva una fuente que permita saber en qué cocinas se midió ni con qué protocolo. Sirven para una estimación inicial cuando no se tiene ningún dato propio, y para nada más.

El cuadro siguiente muestra la tabla de mermas de la hoja «Mi Tabla de Mermas» de rendimiento-mermas-producto.xlsx con dos columnas diferenciadas: la referencia orientativa y la medición propia. En este momento, 6 categorías ya tienen medición propia y 6 categorías aún usan la referencia. Esa proporción es el estado actual, no el objetivo: cada categoría que pasa de la columna de referencia a la de medición propia reduce el margen de error del escandallo.

El criterio para priorizar qué se mide primero no es el volumen de compra en kilos, sino el impacto en el coste de la carta. La alcachofa tiene un rendimiento de 38,0 % en el test, y el mejillón con concha alcanza sólo 20,0 %: dos productos donde la diferencia entre usar la referencia y usar el dato propio puede mover el coste de la ración de forma relevante. Si esos dos productos aparecen en platos de alta rotación, medir antes que estimar no es un refinamiento técnico, es una decisión económica.

La frecuencia de revisión depende de cuánto varía el producto. Un vegetal de temporada cambia de calibre y de proveedor varias veces al año; un lomo de atún congelado de especificación fija puede mantenerse estable durante meses. La hoja «Mi Tabla de Mermas» tiene una columna de fecha de última medición precisamente para que la revisión sea un hábito de compra, no una tarea puntual: cuando cambia el proveedor o el calibre, el test se repite antes de actualizar la ficha, no después de detectar la desviación en el cierre del mes.

**Diez tests de rendimiento con su coste del kilo limpio (rendimiento-mermas-producto.xlsx, hoja «Test de Rendimiento»)**

| Producto | Peso bruto (kg) | Precio/kg bruto (€) | Peso limpio (kg) | Rendimiento (%) | Merma (%) | Factor de corrección | Coste neto sin aprovechar (€/kg) | Coste neto aprovechando (€/kg) |
|---|---|---|---|---|---|---|---|---|
| Lubina entera (1,2 kg) | 1,20 | 14,90 € | 0,62 | 51,7 % | 48,3 % | 1,94 | 28,84 € | 27,63 € |
| Merluza entera | 2,40 | 11,80 € | 1,30 | 54,2 % | 45,8 % | 1,85 | 21,78 € | 20,73 € |
| Solomillo de vacuno (pieza) | 2,10 | 26,50 € | 1,85 | 88,1 % | 11,9 % | 1,14 | 30,08 € | 29,69 € |
| Pollo de corral entero | 2,20 | 5,40 € | 1,50 | 68,2 % | 31,8 % | 1,47 | 7,92 € | 7,38 € |
| Cordero (paletilla) | 1,60 | 13,20 € | 1,35 | 84,4 % | 15,6 % | 1,19 | 15,64 € | 15,64 € |
| Tomate rosa | 5,00 | 3,80 € | 4,40 | 88,0 % | 12,0 % | 1,14 | 4,32 € | 4,32 € |
| Alcachofa | 5,00 | 2,90 € | 1,90 | 38,0 % | 62,0 % | 2,63 | 7,63 € | 7,63 € |
| Boniato | 5,00 | 1,60 € | 4,10 | 82,0 % | 18,0 % | 1,22 | 1,95 € | 1,95 € |
| Mejillón (con concha) | 5,00 | 2,60 € | 1,00 | 20,0 % | 80,0 % | 5,00 | 13,00 € | 13,00 € |
| Gamba blanca (entera) | 2,00 | 24,00 € | 1,05 | 52,5 % | 47,5 % | 1,90 | 45,71 € | 44,29 € |

**Tu tabla de mermas: referencia orientativa y medición propia (rendimiento-mermas-producto.xlsx, hoja «Mi Tabla de Mermas»)**

| Categoría | Referencia mínima (%) | Referencia máxima (%) | Tu merma medida (%) | Merma que usas (%) | De dónde sale el dato |
|---|---|---|---|---|---|
| Carnes (piezas con hueso/grasa) | 15,0 % | 30,0 % |  | 22,5 % | Referencia orientativa |
| Solomillo de vacuno (limpieza) | 10,0 % | 15,0 % | 11,9 % | 11,9 % | Tu medición |
| Pescado entero | 45,0 % | 55,0 % | 48,3 % | 48,3 % | Tu medición |
| Pescado en lomos/filetes | 5,0 % | 12,0 % |  | 8,5 % | Referencia orientativa |
| Verduras de hoja | 10,0 % | 15,0 % |  | 12,5 % | Referencia orientativa |
| Verduras y hortalizas (general) | 10,0 % | 25,0 % |  | 17,5 % | Referencia orientativa |
| Alcachofa | 55,0 % | 65,0 % | 62,0 % | 62,0 % | Tu medición |
| Mejillones, caracoles, callos | 80,0 % | 85,0 % | 80,0 % | 80,0 % | Tu medición |
| Marisco entero (gamba, cigala) | 45,0 % | 55,0 % | 47,5 % | 47,5 % | Tu medición |
| Fruta | 15,0 % | 30,0 % |  | 22,5 % | Referencia orientativa |
| Aves enteras | 28,0 % | 35,0 % | 31,8 % | 31,8 % | Tu medición |
| Quesos, embutidos (corteza/piel) | 3,0 % | 8,0 % |  | 5,5 % | Referencia orientativa |

*La columna «Merma que usas» toma tu medición en cuanto la escribes y, mientras no la tengas, se queda con la referencia. La última columna te dice siempre de dónde viene el número que está costeando tus platos.*


---

## 6. La Ficha de Escandallo que Aguanta una Auditoría

### Qué tiene que llevar una línea de escandallo para ser auditable

Una ficha de escandallo (costeo de recetas) que aguante una auditoría no es la que tiene más columnas, sino la que permite reconstruir cada decisión sin preguntar a quien la hizo. Para eso, cada línea de ingrediente necesita al menos seis campos: nombre del ingrediente tal como aparece en el albarán, cantidad neta por ración, porcentaje de merma, cantidad bruta a comprar, precio sin IVA y tipo de IVA de compra en su propia columna.

El motivo de separar el precio sin IVA del tipo impositivo no es burocrático. La ficha tiene que servir para dos cosas a la vez: costear la ración y conciliar el albarán cuando llegue la factura del proveedor. Si el precio que guardas ya lleva el IVA incorporado, el coste que calculas no es comparable con el que aparece en la cuenta de resultados, que trabaja siempre con bases imponibles. Y si el tipo de IVA está en su propia columna, cualquier cambio normativo —un ingrediente que pasa de un tipo a otro— se corrige en un solo campo sin tocar el precio ni la fórmula de coste.

El campo «raciones que salen de esta ficha» merece atención especial. La ficha del solomillo de cerdo ibérico con puré de boniato que acompaña esta guía tiene ese campo fijado en 1, lo que significa que todos los ingredientes están expresados por ración individual. Pero en cocina de producción es habitual escandalllar una elaboración entera —un fondo, una salsa base, un puré— y después dividir entre el número de raciones que rinde. Ese campo es el divisor. Costear a ojo la ración desde una elaboración de varios kilos introduce un redondeo que se acumula línea a línea y que al final del mes aparece como desviación inexplicable entre el coste teórico y el coste real. La ficha de la hoja «Ficha» de ficha-escandallo-base.xlsx resuelve esto: se introduce el coste total de la elaboración y el número de raciones, y la división la hace la hoja, no el cocinero de guardia.

Los campos obligatorios de cada línea, resumidos:

- Nombre del ingrediente exactamente como figura en el albarán del proveedor.
- Cantidad neta por ración, en kilogramos o litros, sin redondear.
- Porcentaje de merma, como número entre 0 y 1 o como porcentaje, según el criterio que se elija, pero siempre el mismo en toda la ficha.
- Cantidad bruta a comprar, calculada por fórmula, nunca a mano.
- Precio sin IVA por unidad de compra.
- Tipo de IVA de compra, en columna propia.
- Coste sin IVA de la línea, resultado de multiplicar la cantidad bruta por el precio sin IVA.

### La merma entra dividiendo, no multiplicando

El error más frecuente al construir una ficha es calcular la cantidad bruta sumando la merma a la cantidad neta. La lógica parece correcta: si necesito 0,22 kg limpios y la merma es del 12,0 %, añado el 12,0 % de 0,22 y compro un poco más. El problema es que ese cálculo aplica el porcentaje sobre el peso limpio, cuando la merma se produce sobre el peso bruto. El resultado siempre se queda corto, y la desviación crece con porcentajes de merma altos.

La fórmula correcta es: cantidad bruta = cantidad neta dividida entre uno menos la merma. Con los datos de la primera línea de la ficha, la cantidad neta es 0,22 kg y la merma es 12,0 %, es decir, 0,12 en decimal. La operación es 0,22 dividido entre 0,88, que da 0,25 kg. Ese 0,25 es la cantidad bruta que aparece en la hoja «Ficha» de ficha-escandallo-base.xlsx. Si se hubiera calculado sumando el 12,0 % de 0,22, el resultado habría sido 0,2464 kg, una diferencia que parece pequeña por ingrediente pero que se multiplica por cada línea, por cada servicio y por cada día del año.

La cantidad bruta del boniato en esa misma ficha es 0,22 kg, lo que indica que su merma es nula o despreciable en la elaboración concreta que se ha escandallado: el puré parte de boniato ya pelado y porcionado según el proceso de mise en place del establecimiento. Si el proceso cambia —si se compra con piel y se pela en cocina—, el porcentaje de merma sube y la cantidad bruta sube con él. La ficha no es un documento estático: cada vez que cambia el proveedor, el formato de compra o el proceso de limpieza, hay que revisar la columna de merma antes de revisar el precio.

Un criterio práctico para auditar esta columna: si el porcentaje de merma de una línea es cero y el ingrediente llega entero o sin procesar, hay que preguntar quién está asumiendo esa merma. O la absorbe el proveedor en el precio —lo que significa que el precio por kilogramo ya incorpora el coste del despiece— o la está absorbiendo la cuenta de resultados sin que nadie lo haya decidido.

### Del coste por ración al precio de venta objetivo

El resumen de la ficha es donde la información se convierte en decisión. El coste total de la ficha del solomillo de cerdo ibérico con puré de boniato, sin IVA, es 5,67 €. Como la ficha está construida para 1 ración, el coste por ración es también 5,67 €. A partir de ahí, la hoja aplica el food cost objetivo del 30 % fijado en la celda correspondiente de la hoja «Ficha» de ficha-escandallo-base.xlsx y calcula el precio de venta objetivo sin IVA: 18,90 €. Aplicando el tipo reducido del 10 % que corresponde al consumo en sala, el precio de venta objetivo con IVA queda en 20,79 €.

Hasta aquí, la ficha hace lo que hace cualquier escandallo. Lo que la convierte en una herramienta de decisión es la comparación con el precio actual en carta. El plato está en carta a 17,30 € sin IVA. Con ese precio, el food cost real sube al 32,8 % y el margen de contribución —la diferencia entre el precio de venta y el coste del plato— es de 11,63 €. La diferencia entre el precio objetivo y el precio actual es de 1,60 €, lo que equivale a una subida necesaria del 9,3 % sobre el precio actual.

Esos dos números —1,60 € y 9,3 %— son los que hay que llevar a la conversación sobre carta. La ficha no recomienda subir el precio de forma automática: recomienda que la decisión se tome con esos datos sobre la mesa, no a partir de la sensación de que «este plato no sale rentable». El cuadro siguiente, extraído de la hoja «Ficha» de ficha-escandallo-base.xlsx, muestra el resumen completo con todas las líneas.

Conviene aclarar el alcance de esta ficha respecto al resto del material del pack. La hoja «Ficha» de ficha-escandallo-base.xlsx es la base: sirve para construir el criterio, entender la lógica de la merma y leer el resumen de rentabilidad. El Kit de Escandallos incluye plantillas adaptadas a formatos de negocio con estructuras de carta distintas —degustación, menú de precio fijo, barra de tapas—, pero no son necesarias para trabajar con el criterio que desarrolla esta guía. Con la ficha base y el criterio claro, cualquier establecimiento puede auditar su carta plato a plato.

### Comparar el precio objetivo con el que hay hoy en la carta

El resumen de la ficha no termina en el coste por ración: termina en la decisión de precio. La hoja «Ficha» de ficha-escandallo-base.xlsx calcula el precio de venta objetivo a partir del food cost objetivo fijado en la cabecera, que en el ejemplo del solomillo de cerdo ibérico con puré de boniato es del 30 %. Con un coste por ración de 5,67 € sin IVA, el precio de venta objetivo sin IVA queda en 18,90 €, lo que al tipo reducido aplicable en sala representa 20,79 € con IVA. Ese es el precio que sostiene el margen que el negocio necesita.

El campo que convierte la ficha en una herramienta de gestión real es el precio de venta actual en carta, que en este caso es 17,30 € sin IVA. La diferencia entre ambos valores, 1,60 €, aparece calculada en la hoja «Ficha» junto con la subida necesaria expresada en porcentaje sobre el precio actual: 9,3 %. Esos dos datos son los que se llevan a la reunión de revisión de carta, no el coste a secas. El food cost real que genera el precio actual es 32,8 %, y el margen de contribución que deja cada ración vendida a ese precio es 11,63 €. Saber que el margen de contribución cae por debajo del objetivo no es suficiente para tomar una decisión; saber en cuánto hay que mover el precio, y expresarlo como porcentaje sobre el precio actual, es lo que permite evaluar si el mercado aguanta la subida o si hay que actuar por el lado del coste.

La ficha no prescribe la decisión: la informa. Puede que una subida del 9,3 % sea viable en temporada alta y no lo sea en un menú de mediodía de precio fijo. Puede que el plato sea un reclamo de carta y que el negocio decida sostener ese food cost de forma consciente, compensándolo con otros platos de mayor margen. Lo que no puede ocurrir es que esa decisión se tome sin conocer el número. El cuadro siguiente recoge el resumen completo, desde el coste por ración hasta la diferencia de precio, con todos los campos que acaban de describirse.

Para quien necesite adaptar esta estructura a formatos con varias raciones por elaboración, con escandallos de bebida o con fichas de semielaborados que entran como ingrediente en otras fichas, el Kit de Escandallos incluye plantillas específicas por tipo de negocio. Esta ficha base es suficiente para trabajar el criterio que desarrolla la guía; las plantillas del kit son complementarias y están pensadas para quien ya ha interiorizado la lógica de la ficha base.

---

### Errores que invalidan una ficha

El error más frecuente y más silencioso es calcular la cantidad bruta multiplicando la cantidad neta por el porcentaje de merma y sumando el resultado. Con una cantidad neta de 0,22 y una merma del 12,0 %, ese cálculo da una cantidad bruta inferior a la real. La fórmula correcta es dividir la cantidad neta entre uno menos la merma expresada en tanto por uno: 0,22 dividido entre 0,88 da 0,25, que es la cantidad bruta que aparece en la hoja «Ficha». La diferencia parece pequeña en una línea, pero se acumula en cada ingrediente y el coste total de la ficha queda subestimado de forma sistemática. La tabla de abajo muestra la línea del solomillo con los dos valores enfrentados para que la diferencia sea visible.

Guardar el precio sin IVA en la línea de ingrediente, y el tipo de IVA de compra en su propia columna, no es un capricho de formato: es lo que permite usar la misma ficha para costear y para conciliar el albarán del proveedor. Si el precio de compra se guarda con IVA incluido, el coste total de la ficha mezcla base imponible con impuesto y la comparación con el albarán exige un paso de conversión que introduce errores. Con el precio sin IVA en la línea y el tipo en columna separada, cualquier auditoría interna o externa puede reconstruir el importe bruto del albarán multiplicando por el coeficiente correspondiente, sin tocar la lógica del escandallo (costeo de recetas).

El campo «raciones que salen de esta ficha» resuelve otro problema habitual: el redondeo que aparece cuando se intenta costear directamente la ración a ojo. La práctica correcta es costear la elaboración completa y dividir entre el número de raciones que produce. En la ficha del ejemplo ese campo vale 1, porque la elaboración se calcula para una sola ración, pero en una salsa, un fondo o una masa que rinde varias unidades el campo puede valer cualquier número entero, y el coste por ración que calcula la hoja «Ficha» será siempre el resultado de dividir el coste total entre ese valor, sin redondeos intermedios.

Hay tres situaciones que invalidan una ficha aunque los cálculos sean correctos: que el precio de compra registrado no corresponda al proveedor actual, que la merma se haya estimado sin pesaje real, y que el campo de raciones no refleje el rendimiento real de la elaboración en cocina. Las tres tienen la misma solución: la ficha se revisa cada vez que cambia el precio de compra de un ingrediente relevante, y la merma se valida con una ficha de rendimiento firmada por el cocinero responsable. Una ficha sin fecha de última revisión y sin responsable asignado no aguanta una auditoría, aunque la fórmula de la cantidad bruta sea la correcta.

**Las líneas de la ficha, con la merma dentro (ficha-escandallo-base.xlsx, hoja «Ficha»)**

| # | Ingrediente | Unidad | Cantidad neta/ración | Precio/ud sin IVA (€) | Merma (%) | Cantidad bruta a comprar | Coste sin IVA (€) |
|---|---|---|---|---|---|---|---|
| 1 | Solomillo de cerdo ibérico | kg | 0,22 | 15,80 € | 12,0 % | 0,25 | 3,95 € |
| 2 | Panceta ibérica (crujiente) | kg | 0,03 | 11,50 € | 5,0 % | 0,03 | 0,36 € |
| 3 | Boniato | kg | 0,18 | 1,60 € | 18,0 % | 0,22 | 0,35 € |
| 4 | Mantequilla | kg | 0,01 | 8,90 € | 0,0 % | 0,01 | 0,13 € |
| 5 | Nata 35 % M.G. | L | 0,03 | 3,40 € | 0,0 % | 0,03 | 0,10 € |
| 6 | Cebolla | kg | 0,04 | 0,95 € | 12,0 % | 0,05 | 0,04 € |
| 7 | Vino Pedro Ximénez (para la salsa) | L | 0,03 | 9,80 € | 0,0 % | 0,03 | 0,29 € |
| 8 | Caldo de carne | L | 0,06 | 2,20 € | 0,0 % | 0,06 | 0,13 € |
| 9 | Aceite de oliva virgen extra | L | 0,01 | 7,20 € | 0,0 % | 0,01 | 0,11 € |
| 10 | Brotes de rúcula | kg | 0,01 | 12,00 € | 10,0 % | 0,01 | 0,13 € |
| 11 | Sal, pimienta, tomillo y pimentón (prorrateo) | kg | 0,01 | 6,00 € | 0,0 % | 0,01 | 0,06 € |

**El resumen de la ficha: del coste por ración al precio de carta (ficha-escandallo-base.xlsx, hoja «Ficha»)**

| Concepto | Valor |
|---|---|
| COSTE TOTAL DE LA FICHA, sin IVA (€) | 5,67 € |
| Coste por ración, sin IVA (€) | 5,67 € |
| PVP objetivo sin IVA (€) = coste por ración ÷ food cost objetivo | 18,90 € |
| Tipo de IVA de restauración (%) | 10,0 % |
| PVP objetivo CON IVA (€) — el que se imprime en la carta | 20,79 € |
| PVP ACTUAL en carta, sin IVA (€) | 17,30 € |
| PVP actual CON IVA (€) | 19,03 € |
| Food cost REAL con el PVP actual (%) | 32,8 % |
| Margen de contribución con el PVP actual (€) | 11,63 € |
| Diferencia entre el PVP objetivo y el actual (€) | 1,60 € |
| Subida necesaria sobre el PVP actual para llegar al objetivo (%) | 9,3 % |

*Las filas marcadas con «(%)» son porcentajes; el resto, euros. El precio objetivo sale de dividir el coste por ración entre el food cost objetivo, que es una celda editable y no un número dentro de la fórmula.*


---

## 7. Food Cost Teórico vs Real: Dónde se Escapa el Dinero

### Los dos food cost y por qué nunca coinciden del todo

El food cost teórico es lo que debería costar producir lo que se ha vendido, calculado plato a plato desde el escandallo (costeo de recetas). El food cost real es lo que el almacén ha consumido efectivamente durante el periodo, calculado desde el movimiento de stock. Que ambos difieran no es un error de la hoja de cálculo: es la norma, y la diferencia es el diagnóstico.

En la hoja «Datos» de matriz-multimetodo-carta.xlsx, el food cost teórico de la carta de ejemplo se sitúa en 32,7 %. El objetivo que aparece en la hoja «Ficha» de ficha-escandallo-base.xlsx es 30 %. El coste de materia prima sobre ventas del año que recoge la hoja «Mensual» de cuadro-de-mando-prime-cost.xlsx es 32,1 %, con unas ventas netas totales de 1.232.200 € y un consumo real de materia prima de 395.400 €. El objetivo del cuadro de mando, en la hoja «Parámetros» del mismo fichero, es también 30 %. Tres fuentes, tres números distintos, y los tres son correctos: miden cosas distintas. Según el informe «CaixaBankLab × Fundación elBulli — Consumos y beneficios de un restaurante» (2026), el food cost medio del sector hostelero español ronda el 30 % sobre venta, con un rango sano de 25 a 35 %. Estar en 32,1 % no es una alarma; estar en 32,1 % con tendencia ascendente sí lo es.

Las cuatro causas que explican la brecha entre teórico y real, ordenadas por frecuencia de aparición en cocina, son estas:

- **Porciones que no se ajustan a la ficha.** El escandallo dice 180 g de proteína; la balanza en el pase dice otra cosa. Un gramo de más por ración, multiplicado por el número de cubiertos del mes, mueve el food cost real por encima del teórico sin que nadie lo haya decidido.
- **Merma y caducidad.** Género que entra en el almacén y no llega al plato: recortes de limpieza superiores a los previstos en la ficha, producto que caduca antes de rotar, o merma de cocción no actualizada en el escandallo.
- **Invitaciones y consumo de personal.** Todo lo que sale de cocina sin generar venta. Si no se registra con un código de coste propio, el sistema lo contabiliza como consumo de materia prima y el food cost real sube sin explicación aparente.
- **Precios de compra que se han movido sin que nadie reescandallara.** El coste de un ingrediente sube, la ficha no se actualiza, y el teórico sigue calculándose con el precio antiguo. Para saber cuánto se ha movido el precio de origen, la referencia es la nota de prensa del IPC del INE y el sistema de precios origen-mayorista del Ministerio de Agricultura: ahí está el dato; aquí, el método para leerlo.

Lo que se vigila no es el valor absoluto de un mes, sino la tendencia. En enero, el food cost real fue 31,7 % sobre unas ventas netas de 89.600 €, con el objetivo fijado en 30 %. Una desviación estable alrededor de ese nivel, mes tras mes, indica que el escandallo o el objetivo necesitan revisión, pero no hay una fuga activa. Una desviación que crece cada mes señala que algo ha cambiado en la operativa o en los precios de compra y aún no se ha identificado.

---

### El consumo real: stock inicial, compras y stock final

El consumo real de materia prima de un periodo se calcula con una sola fórmula: stock inicial más compras menos stock final. El resultado es lo que la cocina ha consumido, independientemente de lo que se haya vendido. Sin ese inventario de cierre, el dato que se obtiene es el food cost de compras, que es una cifra distinta y engaña en cuanto el almacén sube o baja de nivel. Si en diciembre se compra más de lo habitual para cubrir el puente de enero, el food cost de compras de diciembre se dispara aunque la cocina haya funcionado con normalidad; el food cost real, calculado con el stock final, lo corrige.

En el cuadro de mando, las compras del año suman 396.100 € y el consumo real de materia prima es 395.400 €. La diferencia, que la hoja «Mensual» de cuadro-de-mando-prime-cost.xlsx recoge mes a mes, refleja exactamente ese ajuste de almacén: el stock no ha variado de forma significativa en el conjunto del año, pero en meses concretos la distancia entre ambas cifras puede ser relevante. La tabla que aparece a continuación muestra ese desglose mensual.

El protocolo más útil no es el inventario completo semanal, que en operativa real pocas cocinas sostienen. Lo que funciona es un inventario corto de las diez referencias que más peso tienen en el coste total: las proteínas principales, el marisco si lo hay, y cualquier ingrediente cuyo precio haya variado recientemente. Esas diez referencias suelen explicar la mayor parte de la desviación. Para quien quiera llevar el seguimiento diario con mayor granularidad, el dashboard del Kit de Escandallos incluye la plantilla de control con las columnas necesarias para registrar entrada, salida y stock en tiempo real, sin tener que construirla desde cero.

### Las cuatro causas de la desviación

El food cost real del periodo se obtiene con una sola fórmula: stock inicial más compras menos stock final. El resultado es el consumo real de materia prima. Sin ese inventario de cierre no hay food cost real; lo que se tiene es un food cost de compras, que es otra cosa y engaña cada vez que el almacén sube o baja de nivel. En la hoja «Mensual» del cuadro-de-mando-prime-cost.xlsx se ve la diferencia con claridad: las compras del año suman 396.100 € y el consumo real de materia prima es 395.400 €, sobre unas ventas netas de 1.232.200 €. Esos 700 € de diferencia reflejan la variación de stock entre el primer día del año y el último; si alguien hubiera usado las compras como proxy del consumo, el porcentaje habría salido ligeramente distorsionado. El coste de materia prima sobre ventas que arroja el cuadro de mando es 32,1 %, frente a un food cost objetivo del 30 % fijado en la hoja «Parámetros» del mismo libro. Esa brecha de 2,1 puntos no es un error de la hoja: es un diagnóstico que tiene causas concretas.

Según el informe de CaixaBankLab y la Fundación elBulli sobre consumos y beneficios de un restaurante (2026), el food cost medio del sector hostelero español se sitúa en torno al 30 % sobre venta, con un rango sano de entre el 25 % y el 35 %. Estar en 32,1 % no es una emergencia, pero sí exige saber por qué se está ahí y si la tendencia sube o baja.

Las causas de desviación entre el food cost teórico y el real se repiten en casi todos los establecimientos que asesoro, y siempre aparecen en el mismo orden de frecuencia:

- **Porciones que no se ajustan a la ficha.** Es la causa más habitual. El escandallo (costeo de recetas) fija un gramaje; la línea sirve otro. Cinco gramos de más por plato en una referencia de alto volumen mueven el food cost real varios décimas al mes sin que nadie lo note en el pase.
- **Merma y caducidad.** El género que entra en el almacén y no llega al plato tiene coste pero no genera venta. Una gestión de rotación deficiente o una compra sobredimensionada se traduce directamente en consumo real sin contrapartida en la cuenta de ventas.
- **Invitaciones y consumo de personal.** Toda salida de género sin ticket de venta es consumo real no cubierto por ingreso. Si no se registra con un sistema de invitaciones o de menú de empleados, el food cost absorbe ese coste sin que la hoja teórica lo contemple.
- **Precios de compra que se movieron sin que nadie reescandallara.** Cuando un proveedor actualiza tarifas y la ficha de escandallo no se toca, el food cost teórico de la carta queda desfasado. La matriz-multimetodo-carta.xlsx arroja un food cost teórico de la carta de ejemplo del 32,7 %; si los precios de compra han subido desde el último escandallo, ese 32,7 % ya es optimista. Para saber cuánto han variado los precios de origen, la referencia es la nota de prensa del IPC del INE y el sistema de precios origen-mayorista del Ministerio de Agricultura: ahí está el dato, no en la memoria del jefe de cocina.

Lo que se vigila no es el valor absoluto de un mes, sino la tendencia. Una desviación estable, mes tras mes en el mismo rango, indica que el negocio funciona con un food cost estructuralmente distinto al teórico y que hay que decidir si se corrige la operación o se ajusta el objetivo. Una desviación que crece es otra conversación: algo ha cambiado y hay que encontrarlo antes de que se consolide.

---

### El protocolo semanal que la mantiene bajo control

El inventario completo cada semana es inviable en la mayoría de cocinas con el personal que hay. Lo que funciona es el inventario corto: las diez referencias que más pesan en el coste total. En cualquier operación hay un grupo reducido de productos, normalmente proteínas y elaboraciones de alto valor, que concentran la mayor parte del consumo. Controlar esas diez referencias con rigor semanal da más información que un recuento exhaustivo hecho con prisa y errores.

El procedimiento es directo:

- Identificar las diez referencias de mayor peso en el consumo, usando como base la hoja «Mensual» del cuadro-de-mando-prime-cost.xlsx para ver qué partidas de compra son las más voluminosas.
- Contar el stock físico de esas referencias cada lunes antes del servicio, o el día de menor actividad de la semana.
- Registrar las compras recibidas entre ese conteo y el anterior.
- Calcular el consumo parcial: stock anterior más entradas menos stock actual.
- Comparar ese consumo parcial con las ventas de esas referencias en el mismo periodo, usando las unidades vendidas del TPV.

Si el consumo parcial de esas diez referencias se desvía de forma consistente respecto a lo que debería haberse consumido según la ficha-escandallo-base.xlsx, el problema está localizado antes de que se acumule un mes entero de pérdida. El food cost objetivo que recoge esa ficha es del 30 %; cualquier señal que aleje el consumo real de ese umbral de forma sostenida merece una revisión del gramaje en línea o de las condiciones de compra, no una explicación improvisada al cierre del mes.

Para quien quiera llevar el seguimiento día a día sin construir la herramienta desde cero, el dashboard del Kit de Escandallos incluye la plantilla de control con las fórmulas ya configuradas; el capítulo no la desarrolla aquí porque el material ya la trae lista para usar. La tabla que aparece a continuación muestra el recorrido completo del stock al consumo mes a mes, con los datos del cuadro-de-mando-prime-cost.xlsx, hoja «Mensual»: enero, con ventas netas de 89.600 € y un food cost real de 31,7 %, es el punto de partida para leer cómo evoluciona la desviación a lo largo del año.

**Del stock al consumo: el food cost real mes a mes (cuadro-de-mando-prime-cost.xlsx, hoja «Mensual»)**

| Mes | Ventas netas (€) | Stock inicial (€) | Compras (€) | Stock final (€) | Consumo (€) | Food cost (%) |
|---|---|---|---|---|---|---|
| Enero | 89.600 € | 9.700 € | 28.100 € | 9.400 € | 28.400 € | 31,7 % |
| Febrero | 84.100 € | 9.400 € | 27.000 € | 9.100 € | 27.300 € | 32,5 % |
| Marzo | 95.200 € | 9.100 € | 30.700 € | 9.500 € | 30.300 € | 31,8 % |
| Abril | 100.400 € | 9.500 € | 31.400 € | 9.200 € | 31.700 € | 31,6 % |
| Mayo | 107.900 € | 9.200 € | 34.700 € | 9.700 € | 34.200 € | 31,7 % |
| Junio | 110.700 € | 9.700 € | 37.700 € | 9.000 € | 38.400 € | 34,7 % |
| Julio | 116.200 € | 9.000 € | 38.100 € | 9.400 € | 37.700 € | 32,4 % |
| Agosto | 99.600 € | 9.400 € | 34.400 € | 8.700 € | 35.100 € | 35,2 % |
| Septiembre | 105.500 € | 8.700 € | 32.600 € | 9.500 € | 31.800 € | 30,1 % |
| Octubre | 102.700 € | 9.500 € | 31.800 € | 9.200 € | 32.100 € | 31,3 % |
| Noviembre | 97.900 € | 9.200 € | 30.500 € | 9.700 € | 30.000 € | 30,6 % |
| Diciembre | 122.400 € | 9.700 € | 39.100 € | 10.400 € | 38.400 € | 31,4 % |
| TOTAL / MEDIA | 1.232.200 € |  | 396.100 € |  | 395.400 € | 32,1 % |

*Compárense las columnas de compras y de consumo: cuando difieren, lo que ha cambiado es el almacén, y usar las compras como si fueran el consumo habría dado un food cost falso ese mes.*


---

## 8. Prime Cost: la Métrica que Mide la Salud del Negocio

### Qué suma el prime cost y por qué se miran juntos

El food cost y el coste (costo) de personal no son dos métricas independientes: son vasos comunicantes. Cuanto más se elabora dentro de la cocina —fondos propios, cortes desde la pieza entera, salsas madre en vez de bases industriales—, más baja el coste de producto y más suben las horas de mano de obra que hacen falta para sostenerlo. Comprar más elaborado hace lo contrario: sube el coste de producto y libera horas de cocina. Mirar solo el food cost premia la primera decisión y castiga la segunda sin ver lo que cuesta en la otra columna; mirar solo el coste de personal comete el error simétrico. El prime cost es la suma de las dos partidas sobre la venta neta, y es la única cifra que ve el efecto conjunto de cómo se produce la carta (menú).

Es también la cifra que descubre el caso que más engaña: un food cost que en la ficha de cada plato parece impecable mientras el coste de personal se ha ido desbocando sin que nadie lo cruce con el anterior. Un negocio puede escandallar cada receta con precisión y seguir perdiendo margen porque el cuadrante de sala y cocina lleva meses sin revisarse. El cuadro de mando de este pack está configurado para un negocio con servicio en mesa y compone, mes a mes, el coste de materia prima sobre ventas y el labor cost en la misma fila: en el año que recoge, el coste de producto queda en el 32,1 %, el labor cost en el 31,3 % y la suma —el prime cost— en el 63,4 %, con un margen tras prime cost de 451.142 €, el 36,6 % de la venta que queda para pagar alquiler, suministros y el resto de la estructura antes de hablar de beneficio. Dentro del mismo año hay recorrido: abril cierra en el 62,7 %, el mejor mes, y agosto en el 69,9 %, con una lectura que la propia hoja marca como «por encima del objetivo». La cifra global no dice en qué mes se ha torcido la cosa; el desglose mensual, sí.

### El umbral español: 30 % de producto y 30-35 % de personal

La estructura de costes de un negocio español con servicio integrado en mesa gira en torno al 30 % de producto y a un 30-35 % de personal sobre la venta neta (CaixaBankLab × Fundación elBulli — Consumos y beneficios de un restaurante, 2026). Sumadas, esas dos partidas dibujan el prime cost que este pack toma como referencia, y por eso el objetivo con servicio en mesa está fijado en el 65 % en una celda editable de la hoja «Parámetros» de cuadro-de-mando-prime-cost.xlsx, y no metido dentro de la fórmula: cada negocio puede moverlo si su estructura real se aparta de la referencia, sin tocar el cálculo que lo alimenta.

Ese 65 % solo funciona si el coste de personal que se compara con él se ha calculado con la misma vara. La Seguridad Social a cargo de la empresa se sitúa en el 33 % sobre bruto: en el año que recoge el cuadro de mando, los salarios brutos suman 277.600 € y los otros costes de personal 16.450 €, y una vez añadida esa Seguridad Social el coste de personal asciende a 385.658 €. Calcular el labor cost solo sobre nóminas brutas, sin la Seguridad Social a cargo de la empresa, es compararse con una vara que no es la suya: el resultado sale más bajo de lo real, y el prime cost que se deriva de ahí parece mejor de lo que sostiene el negocio.

Conviene no confundir este umbral con el que más circula en el sector: la referencia estadounidense sitúa el prime cost recomendable en un máximo del 60 %, por encima del cual resulta muy difícil ser rentable salvo con un volumen muy alto (Toast — How to Calculate Prime Cost, 2026), pero es una cifra pensada para otra estructura de personal, no para el español. La fotografía completa de la cuenta de explotación de un negocio español añade a esas dos partidas un 5-10 % de alquiler y un 13-20 % de gastos generales, con un EBITDA sano resultante del 10-13 % (CaixaBankLab × Fundación elBulli, 2026); por debajo de ese suelo, la lectura es que la estructura entera necesita revisarse, no solo la carta.

### Servicio en mesa o barra: dos objetivos distintos

El pack recoge también un objetivo de prime cost para barra o autoservicio, del 55 %, frente al 65 % del servicio en mesa que está en vigor en este cuadro de mando. La diferencia no es un capricho de plantilla: en un formato de barra o autoservicio el coste de personal es estructuralmente menor, porque el servicio prescinde de buena parte de la sala, así que un mismo prime cost significa cosas muy distintas según el modelo de negocio. La misma fuente que fija el umbral español para el servicio integrado en mesa —entre el 30 % y el 35 % de personal sobre venta neta— sitúa el servicio parcial de autoservicio o barra en un 15-25 %, bastante más bajo (CaixaBankLab × Fundación elBulli, 2026). La referencia estadounidense recoge la misma lógica con otro corte: el 60-65 % para servicio completo y el 55-60 % para servicio rápido o QSR (Toast — How to Calculate Prime Cost, 2026). En los dos casos, lo que desplaza el listón es el modelo de servicio, no el criterio con el que se lee.

Leer el prime cost así es un ejercicio de diagnóstico: situarlo frente al umbral del formato del negocio y distinguir cuándo falla el producto y cuándo falla el personal. Cuando esa segunda lectura es la que falla —un labor cost que se sale de su rango mes tras mes—, el trabajo que sigue es de cuadrantes y de horas, y para eso está el Kit de Gestión de Personal de este mismo catálogo. Esta guía se queda en el diagnóstico; ese kit es el que entra a corregirlo.

### El coste de personal es el bruto más la Seguridad Social

El food cost y el coste de personal no se leen por separado: son vasos comunicantes. Cuando la cocina asume más elaboración propia —fondos, salsas madre, despiece en casa— el coste de producto baja, porque se paga materia prima en bruto y no el margen de quien ya la ha transformado, pero las horas de brigada suben, porque ese trabajo hay que hacerlo con alguien dentro. Comprar elaborado o semielaborado invierte el efecto: el food cost sube y las horas bajan. Mirar solo una de las dos partidas es ver la mitad de la decisión. El prime cost —su suma sobre la venta— es la única métrica que las ve juntas y la única que no premia trasladar coste de una columna a la otra sin que el negocio mejore de verdad.

La referencia española para un restaurante con servicio integrado en mesa sitúa el coste de producto en torno al 30 % de la venta y el de personal entre el 30 % y el 35 %, según CaixaBankLab y la Fundación elBulli en su estudio sobre consumos y beneficios del restaurante (2026). De esa suma sale el objetivo que trae el cuadro de mando para el tipo de negocio Servicio en mesa: 65 % de prime cost, cifra que vive en celda editable de la hoja «Parámetros» de cuadro-de-mando-prime-cost.xlsx y no dentro de ninguna fórmula, así que se ajusta el día que cambie el modelo de servicio o la política de personal del local.

La misma hoja trae dos objetivos, no uno:

- 65 % para el negocio con servicio en mesa, el que tiene activo el cuadro de mando.
- 55 % para el negocio que trabaja en barra o en autoservicio.

El segundo no es un umbral más generoso: es el reflejo de una estructura de personal distinta. Con menos servicio en mesa hay menos horas de sala por venta servida, y la propia CaixaBankLab sitúa el coste de personal de ese modelo entre el 15 % y el 25 % de la venta neta, frente al 30-35 % del servicio integrado. Un mismo prime cost del 65 % significa cosas muy distintas según de qué formato se hable.

Hay un matiz que decide si la comparación tiene sentido: el coste de personal que entra en el prime cost del cuadro de mando lleva la Seguridad Social a cargo de la empresa, fijada en el 33 % sobre el bruto en la hoja «Parámetros». La hoja «Mensual» separa las dos partidas del año —277.600 € de salarios brutos y 16.450 € de otros costes de personal— y las suma en un coste de personal con Seguridad Social de 385.658 €. Quien calcule su labor cost sobre nóminas brutas y lo compare contra un objetivo pensado para coste total de personal se está midiendo con una vara que no es la suya: el resultado sale artificialmente bajo, y el diagnóstico, optimista de más.

Conviene situar la referencia que más circula fuera de España: el sector estadounidense —con Toast, proveedor de sistemas de punto de venta, como fuente más citada— sitúa su prime cost objetivo en un 60 % máximo recomendado, por encima del cual es muy difícil ser rentable salvo con volumen muy alto, con un rango del 60-65 % para servicio completo y del 55-60 % para servicio rápido (2026). Es una referencia de otro mercado, con otra estructura de personal y otra fiscalidad laboral detrás.

### Leer el cuadro de mando: el mes bueno, el mes malo y el año

La hoja «Mensual» de cuadro-de-mando-prime-cost.xlsx pone, mes a mes y en la misma fila, el coste de producto sobre ventas y el labor cost, y de ahí calcula el prime cost de cada mes y el del año. Es la vista que delata el caso que más engaña: un food cost impecable conviviendo con un coste de personal desbocado, invisible si solo se mira la columna del producto. En el año que trae la plantilla, el coste de materia prima sobre ventas cierra en el 32,1 % y el labor cost en el 31,3 %, con un prime cost anual del 63,4 %, por debajo del objetivo del 65 % fijado para Servicio en mesa. El margen que queda tras cubrir esas dos partidas es de 451.142 €, el 36,6 % sobre ventas: lo disponible para alquiler, suministros y el resto de la estructura antes de llegar al resultado.

La misma hoja separa el mejor mes del peor. Abril cierra con un prime cost del 62,7 %, cómodamente dentro del objetivo; agosto lo dispara al 69,9 %, y la propia hoja lo marca como «Por encima del objetivo». Ese diferencial de más de siete puntos es la razón de leer el cuadro mes a mes y no solo el acumulado anual: un año en objetivo puede esconder un mes suelto donde algo se ha ido de madre —una plantilla sobredimensionada para la ocupación real, horas extra mal planificadas, un refuerzo de personal que no encontró la venta que lo justificara— y ese mes no se corrige mirando solo la cifra de diciembre.

Que agosto quede por encima del objetivo no significa que ese mes el negocio pierda dinero: significa que le ha quedado menos margen para pagar alquiler, suministros y el resto de la estructura fija que en un mes como abril. Es la lectura que separa el diagnóstico del alarmismo, y también el límite de esta guía: el prime cost dice cuándo el coste de personal se ha comido margen que debería quedar libre, pero no reorganiza cuadrantes ni redistribuye horas. Quien vea su labor cost fuera de sitio, mes tras mes, tiene ese trabajo en el Kit de Gestión de Personal, pensado para trabajar cuadrantes y horas con el detalle que este capítulo no cubre. Aquí el cuadro de mando se queda en poner el número correcto delante y decir si está donde debe.

**El objetivo de prime cost por tipo de negocio (cuadro-de-mando-prime-cost.xlsx, hoja «Parámetros»)**

| Tipo de negocio | Objetivo de prime cost (%) |
|---|---|
| Servicio en mesa | 65,0 % |
| Barra / autoservicio | 55,0 % |

*Las dos casillas son editables: si tu convenio, tu mix o tu formato piden otro umbral, se escribe ahí y el semáforo de los doce meses se recalcula contra el tuyo.*

**Producto y personal en la misma tabla, mes a mes (cuadro-de-mando-prime-cost.xlsx, hoja «Mensual»)**

| Mes | Coste de personal con SS (€) | Food cost (%) | Labor cost (%) | Prime cost (%) | Objetivo (%) | Margen tras prime cost (€) |
|---|---|---|---|---|---|---|
| Enero | 29.988 € | 31,7 % | 33,5 % | 65,2 % | 65,0 % | 31.212 € |
| Febrero | 29.918 € | 32,5 % | 35,6 % | 68,0 % | 65,0 % | 26.882 € |
| Marzo | 30.919 € | 31,8 % | 32,5 % | 64,3 % | 65,0 % | 33.981 € |
| Abril | 31.255 € | 31,6 % | 31,1 % | 62,7 % | 65,0 % | 37.445 € |
| Mayo | 32.256 € | 31,7 % | 29,9 % | 61,6 % | 65,0 % | 41.444 € |
| Junio | 33.656 € | 34,7 % | 30,4 % | 65,1 % | 65,0 % | 38.644 € |
| Julio | 34.657 € | 32,4 % | 29,8 % | 62,3 % | 65,0 % | 43.843 € |
| Agosto | 34.517 € | 35,2 % | 34,7 % | 69,9 % | 65,0 % | 29.983 € |
| Septiembre | 31.920 € | 30,1 % | 30,3 % | 60,4 % | 65,0 % | 41.780 € |
| Octubre | 31.255 € | 31,3 % | 30,4 % | 61,7 % | 65,0 % | 39.345 € |
| Noviembre | 30.919 € | 30,6 % | 31,6 % | 62,2 % | 65,0 % | 36.981 € |
| Diciembre | 34.398 € | 31,4 % | 28,1 % | 59,5 % | 65,0 % | 49.602 € |
| TOTAL / MEDIA | 385.658 € | 32,1 % | 31,3 % | 63,4 % | 65,0 % | 451.142 € |


---

## 9. Cuatro Formas de Poner Precio a un Plato

### Método A: factor sobre el coste, y dónde se rompe

El primero de los cuatro métodos parte del coste (costo) que arroja el escandallo (costeo de recetas) de cada plato y lo multiplica por un factor fijo, calculado para que el resultado deje el food cost objetivo que se haya marcado el negocio: en la carta (menú) de ejemplo, el 30 % que trae por defecto la hoja «Por Plato» de precio-objetivo-multi-metodo.xlsx, una celda que depende de la estructura de costes de cada negocio, no una regla fija que valga para cualquier carta. Es el método más conocido del oficio y funciona razonablemente bien mientras el coste de la ración se mantenga en un rango medio. El problema aparece en cuanto ese coste sube: el mismo factor que da un precio de venta (PVP) razonable en un plato barato, aplicado a un producto caro, dispara la cifra hasta un punto en el que ningún comensal la paga. La carta de ejemplo lo deja claro sin necesidad de más argumento: el chuletón, calculado por el método del factor, sale a un PVP de 49,33 €. No es una anécdota puesta a propósito; es lo que ocurre siempre que este método se aplica sin filtro a un producto de coste alto, y es la razón por la que ningún operador serio confía en un único método para toda la carta. El 30 % objetivo, dicho sea de paso, no es una cifra caprichosa: coincide con el food cost medio del sector hostelero español, en el entorno del 30 % sobre venta con un rango sano del 25 al 35 %, según CaixaBankLab y la Fundación elBulli en su informe «Consumos y beneficios de un restaurante» (2026). Pero un promedio sectorial sirve para calibrar el punto de partida, no para fijar el precio de cada plato uno a uno, y menos cuando el coste de la materia prima se dispara muy por encima del resto de la carta.

### Método B: margen objetivo en euros

El remedio para ese punto de rotura no está en cambiar el porcentaje, sino en cambiar la pregunta. En lugar de partir del coste y aplicar un factor, el método del margen objetivo en euros parte de cuánto quiere ganar el negocio por ración —una cifra fija, en euros, que no se mueve aunque se mueva el coste del producto— y deja que el porcentaje de food cost salga como consecuencia, aunque el resultado quede feo sobre el papel. Aplicado al mismo chuletón, este método devuelve un PVP de 25,30 €, muy por debajo del que arroja el factor, y es el que finalmente se elige para ese plato en la carta, tal como recoge la columna «Q» de la hoja «Por Plato». La consecuencia hay que aceptarla sin incomodidad: el food cost final del chuletón queda en el 58,5 %, muy por encima del 30 % objetivo del conjunto, y aun así el plato deja un margen de contribución sano en euros, que es al final lo que paga el alquiler y las nóminas, no el porcentaje que luce en la hoja. El PVP elegido, además, queda por debajo del precio actual en carta, 32,70 €, así que el ejercicio deja al operador la decisión de mantener el precio vigente o ajustarlo a la baja, una decisión que este capítulo no toma por él.

### Método C: precio de mercado de tu zona

Los métodos C y D cambian de naturaleza frente a los dos anteriores: no calculan un precio de venta, lo importan de fuera. El método C parte de lo que cobra la competencia directa de la zona por un plato equivalente y fija ahí el PVP; el D, que veremos más adelante en este capítulo, hace lo mismo desde otra referencia externa. En los dos casos la hoja deja de responder a «¿cuánto tengo que cobrar?» y pasa a responder a una pregunta distinta: dado ese precio, impuesto desde fuera, ¿qué food cost me queda, y puedo permitírmelo? Es un cambio de sentido en el cálculo, no un tercer camino hacia el mismo número, y conviene tenerlo claro antes de mirar la tabla siguiente.

La carta de ejemplo completa —20 platos con precio calculado— no reparte el trabajo entre un método ganador y tres residuales: usa el método A en 5 platos, el B en 6, el C en 4 y el D en 5, un reparto casi parejo entre los cuatro. 11 platos quedan dentro del food cost objetivo y 9 por encima, con un food cost del 36,7 % para el conjunto de la carta con los precios elegidos y un margen de contribución medio de 8,01 € por plato. Esa es la lectura correcta del cuadro siguiente: no hay que buscar cuál de los cuatro métodos «gana», sino entender que cada plato tira del método que mejor responde a su propia naturaleza —coste, posicionamiento o mercado— y que la carta entera es una cartera de esas cuatro decisiones, no una regla única aplicada plato a plato.

Las croquetas son el ejemplo que conviene mirar aparte, porque dicen algo distinto al del chuletón. El método del factor las sitúa en un PVP de 7,00 €; el precio actual en carta es de 8,60 €, 1,60 € por encima. Aquí el método no exige bajar nada: confirma que el precio vigente ya está por encima del suelo que marca el coste, así que la corrección, si la hay, va en otra dirección. No todos los platos de la carta necesitan tocarse; algunos sólo necesitan que alguien compruebe, escandallo en mano, que el precio que ya cobran sigue teniendo sentido.

### Método D: valor percibido

El factor sobre el coste multiplica sin preguntar qué plato tiene delante, y ahí está su problema: aplicado al chuletón de la carta de ejemplo, el precio que devuelve la hoja de precios es 49,33 €, una cifra que ningún comensal paga por una ración de carne, por generosa que sea la pieza. No es una anécdota del cálculo: es el argumento de este capítulo. Un factor fijo funciona bien cuando el coste de la materia prima es moderado y se comporta igual en toda la carta, pero en cuanto aparece un producto caro, el mismo multiplicador que cuadra las cuentas en un plato de pasta dispara el precio del chuletón hasta un número inservible.

El remedio no es cambiar el factor, es cambiar de método. El margen en euros parte de la pregunta contraria: en lugar de multiplicar el coste, se fija cuánto se quiere ganar por ración y se deja que el porcentaje salga de ahí, aunque el resultado quede feo en la hoja. Con el chuletón, ese camino devuelve un precio de venta de 25,30 €, que es también el precio elegido para la carta, y el food cost que resulta de aceptarlo sube al 58,5 %, muy por encima de cualquier objetivo razonable de conjunto. Compárese con el precio que el chuletón lleva hoy en carta, 32,70 €: ni el factor ni el margen en euros aciertan exactamente con lo que ya se cobra, y esa distancia es justo lo que hay que decidir plato a plato, no lo que hay que forzar a que cuadre.

El método D empuja la lógica un paso más allá. Los métodos C y D no calculan el precio de venta: lo imponen desde fuera, con la competencia, el posicionamiento de la casa o lo que el comensal está dispuesto a pagar por la experiencia, y sólo después dejan que la hoja diga qué food cost resulta de haber aceptado esa cifra. La pregunta deja de ser «cuánto cobro por este plato» y pasa a ser «puedo permitirme cobrar esto», que es una pregunta distinta y bastante más incómoda de responder. En el valor percibido, el precio no sale de ningún coste ni de ningún margen deseado: sale de lo que el plato representa para quien lo pide, y la hoja se limita a devolver el food cost que ese precio deja, para poder juzgar si es sostenible antes de imprimirlo en la carta.

### Qué método le toca a cada plato

La carta de ejemplo tiene 20 platos con precio calculado, y el reparto entre los cuatro métodos desmonta la idea de que exista uno ganador: 5 platos se resuelven por factor, 6 por margen en euros, 4 por precio de mercado y 5 por valor percibido. No hay una fórmula única para toda la carta, hay una cartera de métodos, y elegir cuál aplicar a cada plato es tan parte del oficio como calcular el coste de la ficha técnica. Del conjunto, 11 platos quedan dentro del food cost objetivo y 9 por encima, con un food cost global de la carta del 36,7 % y un margen de contribución medio de 8,01 € por plato: los números de la tabla no piden un único criterio, piden mirar plato por plato con el método que le corresponde.

Las croquetas son el caso que conviene mirar despacio, porque va en sentido contrario a todo lo anterior. El factor sobre el coste devuelve un precio de venta de 7,00 €, pero el precio actual en carta es 8,60 €, es decir, 1,60 € por encima. Aquí el método no está corrigiendo nada: está confirmando que el plato ya se cobra por encima de su suelo. Un plato puede estar perfectamente bien cobrado sin que el método que se usa para revisarlo lo diga con un número más alto; lo que hace el cálculo es marcar el mínimo defendible, no dictar el precio final. La tabla siguiente recoge los cuatro métodos aplicados a toda la carta, plato a plato, para que el criterio de elección quede a la vista antes de tocar un solo precio.

**Los cuatro métodos aplicados a la misma carta (precio-objetivo-multi-metodo.xlsx, hoja «Por Plato»)**

| Plato | Coste/ración (€) | Método elegido | A · PVP por factor (€) | B · PVP por margen (€) | PVP elegido sin IVA (€) | Food cost final (%) | Semáforo |
|---|---|---|---|---|---|---|---|
| Croquetas de jamón ibérico (6 ud) | 2,10 € | A · Factor sobre el coste | 7,00 € | 8,60 € | 7,00 € | 30,0 % | Dentro del objetivo |
| Ensalada de tomate rosa, ventresca y cebolleta | 3,60 € | A · Factor sobre el coste | 12,00 € | 10,10 € | 12,00 € | 30,0 % | Dentro del objetivo |
| Gambas al ajillo | 6,90 € | B · Margen objetivo | 23,00 € | 13,40 € | 13,40 € | 51,5 % | Por encima del objetivo |
| Huevos rotos con patatas y chistorra | 2,40 € | A · Factor sobre el coste | 8,00 € | 8,90 € | 8,00 € | 30,0 % | Dentro del objetivo |
| Tabla de quesos de la zona | 5,20 € | A · Factor sobre el coste | 17,33 € | 11,70 € | 17,33 € | 30,0 % | Dentro del objetivo |
| Alcachofas confitadas con jamón | 3,10 € | A · Factor sobre el coste | 10,33 € | 9,60 € | 10,33 € | 30,0 % | Dentro del objetivo |
| Sopa de tomate asado con albahaca | 1,20 € | D · Valor percibido | 4,00 € | 7,70 € | 7,56 € | 15,9 % | Dentro del objetivo |
| Solomillo de cerdo ibérico con puré de boniato | 5,67 € | C · Precio de mercado | 18,90 € | 16,17 € | 18,68 € | 30,4 % | Por encima del objetivo |
| Bacalao confitado al pil-pil | 7,40 € | B · Margen objetivo | 24,67 € | 17,90 € | 17,90 € | 41,3 % | Por encima del objetivo |
| Hamburguesa de vaca madurada con patatas | 4,30 € | C · Precio de mercado | 14,33 € | 14,80 € | 12,92 € | 33,3 % | Por encima del objetivo |
| Arroz meloso de secreto ibérico y setas | 6,20 € | B · Margen objetivo | 20,67 € | 16,70 € | 16,70 € | 37,1 % | Por encima del objetivo |
| Chuletón de vaca madurada (500 g) | 14,80 € | B · Margen objetivo | 49,33 € | 25,30 € | 25,30 € | 58,5 % | Por encima del objetivo |
| Lubina a la sal | 8,90 € | B · Margen objetivo | 29,67 € | 19,40 € | 19,40 € | 45,9 % | Por encima del objetivo |
| Pollo de corral asado con patatas | 3,70 € | C · Precio de mercado | 12,33 € | 14,20 € | 11,94 € | 31,0 % | Por encima del objetivo |
| Lasaña de verduras de temporada | 2,60 € | C · Precio de mercado | 8,67 € | 13,10 € | 10,49 € | 24,8 % | Dentro del objetivo |
| Tataki de atún rojo con sésamo | 9,60 € | B · Margen objetivo | 32,00 € | 20,10 € | 20,10 € | 47,8 % | Por encima del objetivo |
| Tarta de queso cremosa | 1,30 € | D · Valor percibido | 4,33 € | 5,50 € | 6,61 € | 19,7 % | Dentro del objetivo |
| Torrija caramelizada con helado | 1,10 € | D · Valor percibido | 3,67 € | 5,30 € | 5,83 € | 18,9 % | Dentro del objetivo |
| Coulant de chocolate | 1,60 € | D · Valor percibido | 5,33 € | 5,80 € | 7,13 € | 22,4 % | Dentro del objetivo |
| Fruta de temporada preparada | 1,40 € | D · Valor percibido | 4,67 € | 5,60 € | 4,73 € | 29,6 % | Dentro del objetivo |

*Las columnas A y B calculan siempre, aunque el plato use otro método: están ahí para que veas qué precio habría salido y decidas con las cuatro respuestas delante.*


---

## 10. Psicología de Precios: lo Demostrado y lo que es Leyenda

### El efecto señuelo: la opción que no quieres vender

Cuando una carta (menú) ofrece dos platos comparables en precio y en atractivo, el comensal duda. Basta introducir una tercera opción claramente peor que una de las dos en todo —más cara y sin argumento a su favor frente a la que quieres colocar— pero que no sea peor que la otra en ningún aspecto, para que la elección se incline hacia la opción dominante sobre ese señuelo. Es la dominancia asimétrica aplicada a una carta: el señuelo no está ahí para venderse, está ahí para que la opción vecina parezca la decisión razonable. De toda la psicología de precios que circula en el sector, este es el mecanismo con más respaldo experimental sostenido en el tiempo: el trabajo que lo confirma en la elección de menú se publicó en International Hospitality Review, de la editorial Emerald, y su conclusión es cualitativa —el efecto aparece de forma consistente cuando el señuelo está bien construido—, sin que convenga traducirlo a un porcentaje para tu carta.

Llevarlo a la práctica no exige inventar un plato nuevo: exige mirar la carta que ya tienes y preguntarte, plato a plato, si alguno funciona hoy como señuelo sin que lo hayas decidido tú. El criterio no es quitar el plato flojo: es colocarlo deliberadamente junto al plato que sí quieres que gane, de forma que la comparación quede resuelta antes de que el comensal termine de leer la página.

### Nombres descriptivos: el estudio y su letra pequeña

El nombre con el que describes un plato en la carta no es un detalle de estilo: es una palanca de venta con un estudio de campo detrás. Wansink, Painter y van Ittersum (2001), en la Cornell Hotel and Restaurant Administration Quarterly, midieron el efecto de sustituir un nombre genérico de plato por uno descriptivo —el mismo plato, la misma cocina, sólo cambió la etiqueta— y encontraron un 27 % de incremento de ventas frente al nombre genérico, además de una mejora en cómo el comensal valoraba el sabor y su actitud hacia el plato y el restaurante, sin que pagara ni un céntimo más. Aquí va la salvedad, y va en el mismo párrafo porque separarla sería darle al dato más autoridad de la que tiene: el autor principal de ese trabajo fue objeto de una investigación por mala praxis estadística en publicaciones posteriores, y no se ha localizado una replicación independiente de este estudio en concreto. El 27 % se usa como indicio de que el nombre importa, no como ley que puedas prometerle a nadie.

Lo que sí puedes hacer sin depender del número es aplicar el principio con criterio: un nombre que dice origen, técnica o textura le da al comensal una razón para elegir ese plato y no el de al lado, y esa razón funciona exista o no el 27 % detrás.

### El formato del precio: qué se midió y en qué moneda

Yang, Kimes y Sessarego (2009), en el Cornell Hospitality Report, estudiaron algo más concreto que quitar el símbolo del dinero: compararon precios escritos en numérico sin ningún signo frente a precios con el símbolo de la moneda o escritos en palabras, y encontraron un 8 % de gasto adicional medio —5,55 $ más por comensal— cuando el precio aparecía sin referencia monetaria explícita. La precisión importa: el estudio se hizo en dólares, con comensales estadounidenses, y lo que se midió no es el símbolo del dólar en sí, sino la ausencia de cualquier recordatorio de que ese número es dinero que vas a pagar. No hay forma honesta de trasladar esa cifra al euro ni de asumir que un comensal español reacciona igual ante una carta sin símbolos: el hallazgo se presenta como lo que es, una medición hecha en otro país y en otra moneda, y la decisión sobre tu propio formato de precio queda en tus manos.

Y conviene ser igual de explícito con lo que no tiene ese respaldo. Los precios acabados en nueve, la costumbre de colocar el plato que más interesa en la esquina superior derecha y las reglas sobre el recorrido que hace la vista al leer una carta se repiten en artículo tras artículo del sector, pero no se ha localizado un estudio citable que las sostenga: se enuncian aquí sin número y sin atribución, precisamente porque no la tienen.

El método D de la hoja de precios es, exactamente, la aplicación de todo esto: un precio que no sale de sumar coste (costo) más margen, sino que se impone desde cómo se percibe el plato dentro del conjunto de la carta. En tu pack, 5 platos usan ese método del valor percibido. La hoja te lo deja ver sin rodeos: si toda la carta se fijase a valor percibido, el total sube a 307,04 €; con los precios de venta que has elegido de verdad, el total de la carta se queda en 266,90 €, y el food cost del conjunto con esos precios elegidos queda en 36,7 %. Hasta dónde llevar la percepción y dónde frenarla lo decides tú, plato a plato, con esa misma hoja delante.

### Lo que circula sin estudio detrás

El efecto señuelo es, de toda la psicología de precios que circula en torno a la carta, lo único que tiene detrás un trabajo revisado por pares, publicado en International Hospitality Review, de la editorial Emerald: junto a las dos opciones reales entre las que quieres que el comensal elija se coloca una tercera, claramente peor que una de ellas —precio incluido— pero no peor que la otra: está ahí solo para inclinar la comparación. El comensal, que dudaba entre dos platos o dos menús de precio fijo, ve que uno de ellos gana con claridad al señuelo, y esa victoria relativa se traduce en preferencia por la opción que domina: es dominancia asimétrica, y explica por qué en una carta bien construida casi nunca sobra una opción intermedia, porque cada plato que aparece junto a otros dos suele cumplir una función de comparación, no sólo de venta directa.

Bajando un escalón en solidez está el estudio de los nombres descriptivos de plato: Wansink, Painter y van Ittersum (2001), en la Cornell Hotel and Restaurant Administration Quarterly, encontraron que sustituir el nombre genérico de un plato por uno descriptivo, evocando origen, textura o procedencia, elevaba las ventas un 27 % de incremento frente al nombre genérico, si bien su autor principal fue objeto después de una investigación por mala praxis estadística y no se ha localizado una replicación independiente de este estudio en concreto, de modo que el dato se toma como indicio y no como ley. Fue un ensayo de campo de seis semanas con 140 comensales reales que además registró mejor actitud hacia el plato y hacia el restaurante, y mejor valoración sensorial del sabor, 7,31 frente a 6,83 sobre 10, sin que el comensal pagara un céntimo más: el nombre no cambiaba lo que salía de cocina, cambiaba lo que el comensal decía haber probado.

Con el estudio del formato del precio la cautela es de otro tipo: Yang, Kimes y Sessarego (2009), en el Cornell Hospitality Report, midieron en el St. Andrew's Café del Culinary Institute of America, en Hyde Park, Nueva York, con resultado confirmado después por el Cornell Chronicle, que mostrar el precio en formato numérico sin símbolo de moneda, frente a mostrarlo con «$» o escrito en palabras, elevaba el gasto medio del comensal un 8 % de gasto adicional, 5,55 $ más por comensal. El estudio se hizo en dólares y con comensales estadounidenses, y lo que midieron de verdad no fue el símbolo, sino la ausencia de cualquier referencia monetaria explícita en la lectura del precio, así que trasladar la cifra al euro o suponer que el mismo salto se repite en una carta española sería estirar el dato más de lo que el propio estudio permite.

Y luego está todo lo que se repite sin que haya nada citable detrás. Tres afirmaciones aparecen en cualquier curso de ingeniería de menús sin un estudio al que remitirse ni un autor al que atribuirlas:

- los precios acabados en nueve venden más que el mismo precio redondeado;
- el plato que se quiere vender rinde mejor en la esquina superior derecha de la carta;
- la vista del comensal recorre la página siguiendo un patrón fijo que se puede explotar.

Ninguna de las tres cuenta con un experimento citable, y eso no significa que no funcionen: significa que, a diferencia de las tres anteriores, no hay ningún trabajo al que remitirse si alguien pregunta de dónde sale el consejo, así que aquí se quedan sin número y sin nombre propio.

### Cómo se aplica esto a una carta de verdad

Toda esta psicología deja de ser teoría en el momento en que decides el precio final de un plato, y ahí entra el método D de la hoja de precios: un precio que se impone desde la percepción del comensal, no desde el coste ni desde lo que cobra el vecino, y la propia hoja te devuelve el food cost que te queda al aplicarlo. En la hoja «Por Plato» de precio-objetivo-multi-metodo.xlsx conviven varios métodos, y el reparto ya dice algo por sí solo: 4 platos usan el método del precio de mercado y 5 el del valor percibido, que es justamente donde vive esta psicología. Si toda la carta se fijase a valor percibido, el precio conjunto subiría a 307,04 €; con los precios por los que finalmente has optado, el conjunto de la carta queda en 266,90 €, y el food cost del conjunto con esos precios elegidos se sitúa en el 36,7 %. Dos platos ilustran el rango entre un método y otro: las croquetas quedan en un precio de venta de 7,00 € sin IVA, y el chuletón en 25,30 € sin IVA, con el tipo de IVA de restauración en sala en el 10 %, el mismo para todo el consumo en sala, bebida alcohólica incluida. La tabla siguiente recoge, plato a plato, qué método se aplicó y qué margen queda al final; léela con esta psicología en la cabeza y se entiende por qué ni el precio de mercado ni el de percepción son «el correcto» en abstracto: cada uno responde a una pregunta distinta, y el método D sólo tiene sentido cuando el plato tiene detrás algo real que sostenga esa percepción.

**Cuando el precio viene de fuera: mercado y valor percibido (precio-objetivo-multi-metodo.xlsx, hoja «Por Plato»)**

| Plato | Coste/ración (€) | Precio de mercado de la zona (€) | Precio de valor percibido (€) | PVP elegido sin IVA (€) | PVP elegido con IVA (€) |
|---|---|---|---|---|---|
| Croquetas de jamón ibérico (6 ud) | 2,10 € | 9,12 € | 9,63 € | 7,00 € | 7,70 € |
| Ensalada de tomate rosa, ventresca y cebolleta | 3,60 € | 11,21 € | 12,63 € | 12,00 € | 13,20 € |
| Gambas al ajillo | 6,90 € | 17,36 € | 18,60 € | 13,40 € | 14,74 € |
| Huevos rotos con patatas y chistorra | 2,40 € | 9,21 € | 10,58 € | 8,00 € | 8,80 € |
| Tabla de quesos de la zona | 5,20 € | 15,64 € | 16,59 € | 17,33 € | 19,07 € |
| Alcachofas confitadas con jamón | 3,10 € | 10,14 € | 11,55 € | 10,33 € | 11,37 € |
| Sopa de tomate asado con albahaca | 1,20 € | 6,48 € | 7,56 € | 7,56 € | 8,32 € |
| Solomillo de cerdo ibérico con puré de boniato | 5,67 € | 18,68 € | 20,07 € | 18,68 € | 20,55 € |
| Bacalao confitado al pil-pil | 7,40 € | 21,39 € | 22,92 € | 17,90 € | 19,69 € |
| Hamburguesa de vaca madurada con patatas | 4,30 € | 12,92 € | 14,42 € | 12,92 € | 14,21 € |
| Arroz meloso de secreto ibérico y setas | 6,20 € | 17,38 € | 18,70 € | 16,70 € | 18,37 € |
| Chuletón de vaca madurada (500 g) | 14,80 € | 39,24 € | 40,88 € | 25,30 € | 27,83 € |
| Lubina a la sal | 8,90 € | 23,98 € | 25,72 € | 19,40 € | 21,34 € |
| Pollo de corral asado con patatas | 3,70 € | 11,94 € | 13,59 € | 11,94 € | 13,13 € |
| Lasaña de verduras de temporada | 2,60 € | 10,49 € | 11,97 € | 10,49 € | 11,54 € |
| Tataki de atún rojo con sésamo | 9,60 € | 25,76 € | 27,33 € | 20,10 € | 22,11 € |
| Tarta de queso cremosa | 1,30 € | 6,25 € | 6,61 € | 6,61 € | 7,27 € |
| Torrija caramelizada con helado | 1,10 € | 5,17 € | 5,83 € | 5,83 € | 6,41 € |
| Coulant de chocolate | 1,60 € | 6,70 € | 7,13 € | 7,13 € | 7,84 € |
| Fruta de temporada preparada | 1,40 € | 4,05 € | 4,73 € | 4,73 € | 5,20 € |

*El precio con IVA de la última columna es el que se imprime en la carta y el único que ve el cliente: es ahí donde operan los efectos de este capítulo, no en la base imponible con la que tú trabajas.*


---

## 11. Ingeniería de Menú I: Kasavana & Smith Bien Hecho

### Qué mide la matriz y qué deja fuera

La matriz que vas a usar en este capítulo compara cada plato en dos ejes: popularidad (unidades vendidas frente al resto de su familia) y margen de contribución en euros, no food cost en porcentaje. El modelo se atribuye a Kasavana y Smith (1982), «Menu Engineering: A Practical Guide to Menu Analysis», y su aportación fue cruzar esos dos ejes en un único cuadrante en lugar de mirarlos por separado. Cada plato de tu carta (menú) se compara con dos referencias, y las dos son de su propia familia: el umbral de popularidad y la media ponderada de margen de contribución. Nunca la media de la carta entera.

Ese matiz —comparar dentro de la familia, no contra el conjunto— separa una matriz útil de una que engaña. Si mezclas entrantes, principales y postres en un único cálculo, un principal caro y un postre barato nunca compiten en margen en igualdad de condiciones: en esta carta, el margen de contribución medio ponderado de los principales es 10,80 €, el de los entrantes 7,46 € y el de los postres 4,48 €, frente a un 8,16 € de media ponderada para el conjunto. Un postre que rinda por encima de su propia familia quedaría igualmente por debajo de esa media general sin haber hecho nada mal: el problema no sería el plato, sería la vara de medir.

La matriz trabaja además con promedios de un periodo de ventas, así que un cambio pequeño en la carta —quitar una referencia, ajustar una ración, mover un precio— puede desplazar a otro plato de cuadrante sin que su receta haya cambiado en nada. No es una etiqueta que se pega a un plato para siempre, sino una fotografía de este ciclo de ventas que conviene repetir cada vez que la carta se mueve de forma sensible.

### El umbral de popularidad: por qué es el 70 % dividido entre los platos de la familia

El umbral sale de una cuenta sencilla. Si una familia tiene N platos y las ventas se repartieran de forma perfectamente plana, cada uno se llevaría una N-ésima parte de las unidades vendidas por esa familia. El umbral de esta matriz es el 70 % de esa parte proporcional, no el 100 %: exigir la parte completa dejaría fuera a la mitad de una carta sana. Ese factor está en celda, no fijo en el cálculo, así que quien quiera ser más estricto con lo que llama «popular» puede subirlo sin tocar nada más de la hoja. Con las 20 referencias de esta carta y las 4.870 unidades mensuales que mueve en conjunto, cada familia parte de su propio reparto plano, y es sobre ese reparto —nunca sobre el total de la carta— donde se aplica el 70 %.

Con las dos referencias fijadas, cada plato cae en uno de los cuatro cuadrantes clásicos. En esta carta hay 6 platos Star, que suman 1.950 unidades (el 40,0 % de todo lo vendido) y 14.865 € de margen total; 6 Plowhorse con 16.198 € entre todos; 5 Puzzle con 6.357 €, y 3 Dog con 350 unidades y 2.318 €. La tabla de abajo desglosa cada plato dentro de su familia, y el cuadro siguiente pesa lo que representa cada cuadrante sobre el total.

El orden de intervención no es el mismo para los cuatro, y equivocarlo sale caro. Sobre un Star se toca poco y con cuidado: es un caballo de batalla, y una subida de precio brusca puede tirar por tierra justo lo que lo hace popular. Un Puzzle —margen alto, pocas unidades— pide rediseño antes que precio: cambiar su posición en la carta o el modo de presentarlo suele mover más unidades que subirle el precio de golpe. Retirar un plato es la última palanca, nunca la primera, porque hasta un Dog puede sostener a otros del ticket: quien lo pide puede ser quien luego encarga la botella de vino o el postre que sí deja margen, una lectura conjunta que la matriz no ve por diseño.

### Por familia, siempre: un postre no compite con un principal

La matriz de Kasavana y Smith (1982), presentada en «Menu Engineering: A Practical Guide to Menu Analysis», cruza dos ejes: la popularidad de cada plato, medida en unidades vendidas, y su margen de contribución en euros, lo que le queda a cada plato tras descontar lo que cuesta prepararlo. Cada plato se compara con un umbral de unidades y con la media ponderada de margen, y ese cruce solo tiene sentido dentro de su propia familia de la carta: entrantes contra entrantes, principales contra principales, postres contra postres. Mezclarlos en una sola tabla es el error que inutiliza el método, junto con el de comparar el margen de cada plato contra la media simple de toda la carta en vez de contra la media ponderada de su propia familia.

La carta de referencia de este capítulo tiene 20 platos con ventas y suma 4.870 unidades vendidas al mes, con un margen de contribución medio ponderado de 8,16 € para el conjunto. Pero ese 8,16 € esconde tres mundos distintos: los entrantes rondan un margen ponderado de 7,46 €, los principales suben hasta 10,80 € y los postres se quedan en 4,48 €. Un principal caro y un postre barato no van a competir nunca en margen por una razón que nada tiene que ver con lo bien diseñado que esté cada uno: comparado contra la media de toda la carta, el postre sale mal clasificado siempre, solo por pertenecer a una familia con un margen medio más bajo.

El umbral de popularidad se construye igual de sencillo: si una familia tiene N platos, repartir las unidades a partes iguales daría a cada uno una N-ésima parte de las ventas de esa familia. El umbral es el 70 % de esa parte proporcional, y ese 70 % está en una celda propia de la hoja de cálculo, no escrito a fuego en el método: quien quiera exigir más a sus platos cambia ese número y la clasificación se recalcula sola.

### Los cuatro cuadrantes y lo que significan de verdad

Cruzar popularidad y margen por encima o por debajo del umbral deja cuatro cuadrantes, y se mantienen con su nombre original —Star, Plowhorse, Puzzle, Dog— porque son los que el lector va a encontrar en cualquier material sobre el tema:

- Star: vende mucho y deja mucho margen. En esta carta son 6 platos que suman 1.950 unidades, el 40,0 % de todo lo que se vende, y aportan 14.865 € de margen de contribución.
- Plowhorse, el caballo de batalla: vende mucho pero con poco margen. Son 6 platos que, entre todos, aportan 16.198 €.
- Puzzle: deja buen margen pero se vende poco. Son 5 platos con 6.357 € de aportación conjunta.
- Dog: no vende ni deja margen. Son 3 platos, 350 unidades entre todos, 2.318 € de margen total.

El orden de intervención va por riesgo, no por orden alfabético de cuadrante. Sobre un Plowhorse se sube el precio con cuidado, en pasos pequeños: es el plato que más gente pide y un salto brusco se nota. Sobre un Puzzle se rediseña antes de tocar el precio: se cambia el nombre en la carta, se reubica en la página o se prueba junto a un plato que arrastre más pedidos. Retirar es la última palanca, no la primera: un Dog puede estar sosteniendo a otros platos del ticket medio, completando un menú de precio fijo o cerrando una mesa de grupo que sin esa opción se habría ido a otro sitio. Quitarlo sin mirar ese efecto puede llevarse por delante ventas que nunca aparecerán en su propia fila de la matriz.

La propia matriz reconoce su límite: trabaja con promedios, así que un cambio pequeño en la carta —un plato nuevo, una subida de precio en otro, un cambio de temporada— puede mover un plato de cuadrante sin que haya cambiado nada en su receta. El cuadro siguiente, con la carta clasificada plato a plato dentro de su familia, y la tabla de abajo, con el peso de cada cuadrante, son una fotografía de este momento, no una etiqueta permanente.

### Qué se hace con cada uno, en orden de riesgo

Kasavana y Smith (1982), en «Menu Engineering: A Practical Guide to Menu Analysis», plantean el modelo seminal de la ingeniería de menú sobre dos ejes: la popularidad de cada plato, en unidades vendidas, y el margen de contribución en euros, precio de venta menos coste de materia prima. Cada plato se compara con dos referencias: un umbral de popularidad y la media ponderada de margen de SU familia. La hoja «Kasavana-Smith» de matriz-multimetodo-carta.xlsx hace esa comparación por plato, con el desglose en la hoja «Datos» del mismo libro.

El umbral no sale de una media histórica, sale de un reparto igualitario: si una familia tiene N platos, repartir la venta a partes iguales daría a cada uno una N-ésima parte; el umbral se fija en el 70 % de esa parte (factor del umbral de popularidad: 70 %), y ese porcentaje vive en una celda de la hoja «Datos», así que quien quiera exigir más sólo tiene que subirlo. Con las 4.870 unidades vendidas al mes entre los 20 platos con ventas de la carta, el corte se calcula familia por familia, nunca sobre el total.

Aplicar la matriz a la carta entera —mezclando entrantes, principales y postres en una sola nube de puntos— es el error que la vuelve inservible: el margen de contribución medio ponderado de los principales (10,80 €) y el de los postres (4,48 €) no compiten en la misma liga, así que un postre bien vendido y bien diseñado saldría siempre por debajo del umbral de margen sólo por estar al lado de un principal, sin que eso diga nada de su rentabilidad real. Por eso cada familia se lee contra su propia media —los entrantes contra la suya (7,46 €), los principales contra la suya (10,80 €) y los postres contra la suya (4,48 €)—; la media de 8,16 € de toda la carta sirve de fotografía de conjunto, nunca de corte para un plato concreto.

Con las cuatro etiquetas puestas —Star, alto en popularidad y en margen, Plowhorse, el caballo de batalla, mucha venta y margen corto, Puzzle, el rompecabezas, buen margen y poca venta, y Dog, bajo en las dos métricas—, el orden en que se interviene es de menor a mayor riesgo.

- Star primero, y con cuidado: son los 6 platos que ya cumplen las dos condiciones, mueven 1.950 unidades al mes —el 40,0 % de toda la venta de la carta— y aportan 14.865 € de margen, el bloque mayor de los cuatro cuadrantes. El trabajo es de vigilancia: si se toca el precio, se sube poco y se mide la reacción antes de repetir.
- Plowhorse después: populares, pero con el margen por debajo del umbral de su familia. Son 6 platos que ya aportan 16.198 €; aquí se sube precio, se revisa la ficha técnica para recortar coste sin que se note en el plato, o las dos cosas a la vez, vigilando que la venta no baje del umbral que lo clasificó aquí.
- Puzzle se rediseña, no se retoca: son 5 platos con buen margen —6.357 € entre todos— y venta corta, así que el trabajo no es de precio: es de nombre, de foto, de ubicación en la página o de sugerencia del servicio de sala, para sumar las unidades que faltan sin tocar el margen.
- Dog es la última intervención, y no la automática: antes de retirar un plato conviene comprobar si sostiene el ticket de lo que se pide a su lado, o si su presencia sigue cumpliendo una función aunque venda poco. Los 3 Dog de este ejemplo mueven 350 unidades entre los tres y aportan 2.318 € de margen; el cuadro siguiente reparte lo que pone cada cuadrante sobre el total de la carta.

Conviene no perder de vista la reserva que los propios autores del modelo dejaron por escrito: la matriz trabaja con promedios de un periodo de venta, así que un cambio pequeño en el mix —un plato de temporada que entra o sale, o una promoción puntual— puede desplazar un plato de cuadrante de un mes al siguiente. No es una etiqueta que se pega una vez y se olvida: es una fotografía que hay que repetir.

**La carta clasificada plato a plato, dentro de su familia (matriz-multimetodo-carta.xlsx, hoja «Kasavana-Smith»)**

| Plato | Familia | Uds | Mix en su familia (%) | Umbral (%) | Popularidad | MC del plato (€) | MC medio de su familia (€) | Clasificación |
|---|---|---|---|---|---|---|---|---|
| Croquetas de jamón ibérico (6 ud) | Entrantes | 420 | 24,3 % | 10,0 % | Alta | 6,50 € | 7,46 € | Plowhorse |
| Ensalada de tomate rosa, ventresca y cebolleta | Entrantes | 310 | 17,9 % | 10,0 % | Alta | 8,20 € | 7,46 € | Star |
| Gambas al ajillo | Entrantes | 260 | 15,0 % | 10,0 % | Alta | 8,60 € | 7,46 € | Star |
| Huevos rotos con patatas y chistorra | Entrantes | 380 | 22,0 % | 10,0 % | Alta | 7,40 € | 7,46 € | Plowhorse |
| Tabla de quesos de la zona | Entrantes | 90 | 5,2 % | 10,0 % | Baja | 8,40 € | 7,46 € | Puzzle |
| Alcachofas confitadas con jamón | Entrantes | 120 | 6,9 % | 10,0 % | Baja | 7,80 € | 7,46 € | Puzzle |
| Sopa de tomate asado con albahaca | Entrantes | 150 | 8,7 % | 10,0 % | Baja | 6,00 € | 7,46 € | Dog |
| Solomillo de cerdo ibérico con puré de boniato | Principales | 340 | 16,8 % | 7,8 % | Alta | 11,63 € | 10,80 € | Star |
| Bacalao confitado al pil-pil | Principales | 190 | 9,4 % | 7,8 % | Alta | 11,70 € | 10,80 € | Star |
| Hamburguesa de vaca madurada con patatas | Principales | 460 | 22,8 % | 7,8 % | Alta | 9,30 € | 10,80 € | Plowhorse |
| Arroz meloso de secreto ibérico y setas | Principales | 270 | 13,4 % | 7,8 % | Alta | 10,20 € | 10,80 € | Plowhorse |
| Chuletón de vaca madurada (500 g) | Principales | 110 | 5,4 % | 7,8 % | Baja | 17,90 € | 10,80 € | Puzzle |
| Lubina a la sal | Principales | 80 | 4,0 % | 7,8 % | Baja | 12,90 € | 10,80 € | Puzzle |
| Pollo de corral asado con patatas | Principales | 300 | 14,9 % | 7,8 % | Alta | 9,00 € | 10,80 € | Plowhorse |
| Lasaña de verduras de temporada | Principales | 140 | 6,9 % | 7,8 % | Baja | 8,80 € | 10,80 € | Dog |
| Tataki de atún rojo con sésamo | Principales | 130 | 6,4 % | 7,8 % | Baja | 12,80 € | 10,80 € | Puzzle |
| Tarta de queso cremosa | Postres | 520 | 46,4 % | 17,5 % | Alta | 4,60 € | 4,48 € | Star |
| Torrija caramelizada con helado | Postres | 210 | 18,8 % | 17,5 % | Alta | 4,40 € | 4,48 € | Plowhorse |
| Coulant de chocolate | Postres | 330 | 29,5 % | 17,5 % | Alta | 4,60 € | 4,48 € | Star |
| Fruta de temporada preparada | Postres | 60 | 5,4 % | 17,5 % | Baja | 3,10 € | 4,48 € | Dog |

**Cuánto pesa cada cuadrante (matriz-multimetodo-carta.xlsx, hoja «Kasavana-Smith»)**

| Clasificación | Platos | Uds vendidas | % de las uds de la carta | MC total aportado (€) |
|---|---|---|---|---|
| Star | 6 | 1.950 | 40,0 % | 14.865 € |
| Plowhorse | 6 | 2.040 | 41,9 % | 16.198 € |
| Puzzle | 5 | 530 | 10,9 % | 6.357 € |
| Dog | 3 | 350 | 7,2 % | 2.318 € |

*Mírese la última columna antes de tocar nada: hay cuadrantes con pocos platos que sostienen una parte grande del margen del mes.*


---

## 12. Ingeniería de Menú II: lo que la Matriz Clásica no Ve

### Miller: popularidad contra food cost porcentual

La matriz clásica cruza dos variables, popularidad y margen de contribución, y con ellas basta para leer cualquier carta (menú) en un primer vistazo. Pero hay una tercera variable que esa lectura no incorpora, el food cost porcentual, y ningún modelo mide las tres a la vez: cada uno elige dos de las tres —popularidad, food cost porcentual y margen en euros— y deja fuera la que no necesita. Por eso, aplicados sobre la misma carta, los distintos modelos no siempre coronan al mismo plato como ganador. Esa discrepancia no es un error de cálculo: es información, y leerla bien es el hilo que recorre este capítulo.

Miller (1980) es el modelo del que compra bien. Cruza popularidad con food cost porcentual y premia al plato que vende mucho con un food cost bajo, sin mirar cuántos euros deja cada unidad vendida. En la carta de referencia, el grupo Winner reúne 8 platos que concentran 2.940 unidades vendidas —el 60,4 % de todo lo que sale de cocina— con un food cost medio ponderado del 26,9 %, por debajo del 32,7 % de la carta completa. El grupo Loser, con 5 platos, sube hasta el 40,7 %; el Marginal queda en medio, con 7 platos. El riesgo de esta lectura es también su virtud: puede coronar como Winner un plato que compra barato y vende mucho, aunque el margen que deja en euros sea escaso. Miller no lo ve, porque no es la variable que mide.

### Pavesic: food cost porcentual contra margen ponderado por unidades

Pavesic (1983) corrige esa ceguera. En vez de mirar sólo el porcentaje, pondera el margen de contribución por las unidades vendidas de cada plato, de modo que un plato de margen alto que casi nadie pide deja de parecer estupendo en cuanto se multiplica por su volumen real. En la misma carta, el grupo Prime —7 platos— aporta un margen de contribución ponderado total de 21.408 €; el Problem, con 6 platos, se queda en 7.830 €; entre ambos quedan el Standard, con 3 platos, y el Sleeper, con 4. La tabla siguiente reparte esos euros plato a plato.

Hayes y Huffman (1985), en «Menu Analysis: A Better Way», publicado en la Cornell Hotel and Restaurant Administration Quarterly, plantean una salida que ya no es una matriz de cuadrantes: el Goal Value Analysis reduce food cost, precio de venta, popularidad y costes variables a un único índice por plato, y su crítica al enfoque de cuadrantes es precisamente que se apoya en promedios de toda la carta en vez de en el objetivo de cada plato. Con un coste (costo) de personal sobre ventas del 32 % y otros costes variables del 10 % —los dos porcentajes que alimentan el índice y que en el libro viven en celdas editables—, 9 platos de la carta quedan por encima del objetivo de su propia familia y 11 por debajo. El índice no tiene unidades ni se expresa en euros: sólo se puede leer contra el objetivo de su propia familia, nunca en absoluto ni comparado con platos de otra familia.

LeBruto, Quain y Ashley (1995), en «Menu Engineering: A Model Including Labor», publicado en la FIU Hospitality Review, añaden el coste de mano de obra al modelo de Kasavana y Smith y parten sus cuatro cuadrantes en ocho. Su frase clave es la que ordena todo el capítulo: los operadores ingresan dinero, no porcentajes.

### Goal Value: un índice por plato en lugar de cuadrantes

Popularidad, food cost porcentual y margen en euros son las tres variables que deciden si un plato conviene, y cada modelo elige dos y deja la tercera fuera. Por eso Miller, Pavesic y Goal Value pueden clasificar el mismo plato de tres formas distintas sin equivocarse, y la discrepancia es información que la matriz clásica sola no da.

Miller (1980) planteó el primer modelo matricial que cruza food cost y mix de ventas, antecesor de la matriz de Kasavana y Smith: premia el food cost bajo con volumen, y puede coronar ganador a un plato de mucha rotación aunque deje pocos euros de margen. En tu carta marca 8 Winner —2.940 unidades vendidas, el 60,4 % del total, food cost medio ponderado 26,9 %—, 7 Marginal y 5 Loser, estos con food cost medio ponderado del 40,7 %.

Pavesic (1983) corrige ese punto ciego: sustituye el margen de contribución individual por el ponderado por unidades vendidas, así que un plato de margen alto y poca venta deja de parecer estupendo. En tu carta marca 7 Prime, con 21.408 € de margen ponderado conjunto; 3 Standard, 4 Sleeper y 6 Problem, estos con 7.830 € de margen ponderado conjunto.

El Goal Value no es una tercera matriz: es la alternativa de quienes vieron el problema en el propio formato de cuadrantes. Hayes y Huffman (1985), «Menu Analysis: A Better Way», en la Cornell Hotel and Restaurant Administration Quarterly, criticaron que Miller y Pavesic reparten los platos contra un promedio de carta que se mueve con cada plato que entra o sale. Su alternativa: un índice único por plato que combina food cost, precio de venta, popularidad y costes variables, sin cuadrante ni promedio. En tu carta usa un coste de personal del 32 % sobre ventas y otros costes variables del 10 %, y compara cada plato con el objetivo de su familia: 9 platos por encima y 11 por debajo, sobre un food cost medio ponderado de carta del 32,7 %.

Ese índice no lleva unidades: ni precio en euros ni porcentaje absoluto, así que compararlo entre familias —un guiso contra un pescado— no dice nada; solo vale leído contra el objetivo de su propia familia, que es lo que hace el cuadro siguiente, plato a plato.

### LeBruto: qué pasa cuando entra el coste de mano de obra

LeBruto, Quain y Ashley (1995), «Menu Engineering: A Model Including Labor», en la FIU Hospitality Review, añadieron a la matriz de Kasavana y Smith lo que ni Miller, ni Pavesic ni el Goal Value habían metido: el coste de mano de obra de cada plato. No es una hoja nueva, sino una lectura añadida sobre la misma matriz: cada plato se clasifica también como de coste laboral alto o bajo, y esa capa parte los cuatro cuadrantes clásicos en ocho, hasta los 8 cuadrantes de la matriz ampliada frente a los 4 originales.

Su frase ordena el capítulo: los operadores ingresan dinero, no porcentajes. Un plato de food cost bajo y mucho trabajo de cocina detrás puede costarte en mano de obra lo que ahorras en materia prima, y la matriz clásica no lo muestra porque solo mira dos variables a la vez. No sustituye al Goal Value ni al margen ponderado de Pavesic: exige sumar esa pregunta a cualquiera de los tres, antes de fijar el precio de venta o de empujar un plato desde sala. Es lo que separa el food cost porcentual del margen en euros que entra en caja, y lo que convierte a Miller, Pavesic y Goal Value en tres ángulos del mismo problema, no en respuestas que compiten entre sí.

### Las tres variables y por qué ningún método las mide todas

Popularidad, food cost porcentual y margen de contribución en euros son las tres variables que definen la rentabilidad real de un plato, y ningún modelo las mira a la vez: cada uno se queda con dos y deja fuera la tercera. Por eso, cuando dos matrices aplicadas a la misma carta clasifican el mismo plato en grupos distintos, no hay ningún error de cálculo detrás, sino una pregunta distinta. La discrepancia no es ruido que resolver a favor de una sola tabla: es información, y leerla bien exige saber qué variable ha dejado fuera cada método.

Miller (1980) es el modelo de quien compra bien. Cruza popularidad y food cost porcentual, y premia con la etiqueta de Winner al plato que combina alta demanda con un coste de materia prima bajo, dejando fuera precisamente cuántos euros de margen produce cada unidad servida. Fue el primer modelo matricial que cruzó food cost y mix de producto, antecesor directo de la matriz clásica de Kasavana y Smith. Aplicado a esta carta, y como muestra la tabla siguiente, los ocho platos Winner reúnen 2.940 unidades vendidas —el 60,4 % de todo lo que sale de cocina— con un food cost medio ponderado del 26,9 %. Ahí está su punto ciego: compra barato y vende mucho, pero puede dejar pocos euros por comensal si el precio de venta se quedó corto. Los cinco Loser cargan un food cost medio ponderado del 40,7 %, y entre ambos quedan los siete Marginal.

Pavesic (1983) corrige ese punto ciego: sustituye el margen de contribución individual por el ponderado por las unidades vendidas, de modo que un plato de margen alto que casi nadie pide deja de parecer estupendo en cuanto se multiplica por su volumen real. En esta carta, los siete platos Prime aportan entre todos 21.408 € de margen ponderado, frente a los 7.830 € que suman los seis Problem: la distancia entre un plato que sostiene la caja y otro que solo luce bien en la ficha técnica. Entre ambos quedan tres Standard y cuatro Sleeper, un matiz que Miller no ve porque nunca cruza volumen y margen.

Hayes y Huffman (1985), en «Menu Analysis: A Better Way», publicado en la Cornell Hotel and Restaurant Administration Quarterly, propusieron una salida que no es una matriz: el Goal Value Analysis condensa food cost, precio de venta, popularidad y costes variables en un único índice por plato, y critican el enfoque de cuadrantes por apoyarse en promedios de toda la carta que diluyen lo que le pasa a cada referencia. Aquí el índice se calcula con un coste de personal del 32 % sobre ventas y otros costes variables del 10 % sobre ventas, editables en la hoja de cálculo; con ellos, nueve platos quedan por encima del objetivo de su familia y once por debajo. El Goal Value no lleva euros ni porcentaje propio: es un índice que solo tiene sentido comparado con el objetivo de su misma familia, nunca en absoluto ni frente al de otra.

LeBruto, Quain y Ashley (1995), en «Menu Engineering: A Model Including Labor», publicado en la FIU Hospitality Review, no proponen otra hoja de cálculo: proponen una lectura distinta de la misma matriz. Incorporan el coste de mano de obra al modelo de Kasavana y Smith y parten cada uno de los cuatro cuadrantes clásicos en dos, según el plato cargue mucho o poco coste laboral, hasta llegar a ocho cuadrantes en lugar de los cuatro originales. Su frase resume el capítulo entero: los operadores ingresan dinero, no porcentajes. Resta importancia al food cost porcentual aislado frente al margen que un plato deja de verdad, y esa es la idea que ordena el paso de una tabla a la siguiente: cada método mira una parte distinta de la misma carta, y ninguno sustituye a los otros tres.

**Miller: cuánto pesa cada grupo (matriz-multimetodo-carta.xlsx, hoja «Miller»)**

| Clasificación | Platos | Uds vendidas | % de las uds de la carta | Food cost medio ponderado del grupo (%) |
|---|---|---|---|---|
| Winner | 8 | 2.940 | 60,4 % | 26,9 % |
| Marginal | 7 | 1.460 | 30,0 % | 32,0 % |
| Loser | 5 | 470 | 9,7 % | 40,7 % |

**Pavesic: cuánto margen ponderado aporta cada grupo (matriz-multimetodo-carta.xlsx, hoja «Pavesic»)**

| Clasificación | Platos | Uds vendidas | % de las uds de la carta | MC ponderado total del grupo (€) |
|---|---|---|---|---|
| Prime | 7 | 2.730 | 56,1 % | 21.408 € |
| Standard | 3 | 860 | 17,7 % | 6.508 € |
| Sleeper | 4 | 620 | 12,7 % | 3.992 € |
| Problem | 6 | 660 | 13,6 % | 7.830 € |

**Goal Value plato a plato, contra el objetivo de su familia (matriz-multimetodo-carta.xlsx, hoja «Goal Value»)**

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

*El Goal Value es un ÍNDICE, no un importe: sólo tiene sentido comparado con el objetivo de su propia familia, que es la columna de al lado.*


---

## 13. Cuando los Métodos Discrepan: el Protocolo de Decisión

### Coincidencia no es confianza: qué significa que los cuatro coincidan

De los 20 platos con ventas en la carta (menú), sólo 3 alcanzan las cuatro lecturas en la mejor categoría a la vez, y otros 3 no tienen ninguna lectura fuera de su franja esperada: el 15,0 % de la carta. Leer esos platos como «los que ya están bien» y dejar de mirarlos sería exactamente el error que evita este capítulo, porque la coincidencia dice que los modelos están de acuerdo entre sí, no que el plato esté sano. Los cuatro métodos parten del mismo escandallo (costeo de recetas), del mismo precio de venta y del mismo historial de ventas de la carta; si ese dato de entrada arrastra un sesgo, una ración mal pesada, una promoción puntual que disparó las unidades un mes concreto, el sesgo viaja a los cuatro resultados por igual, y coinciden en el error con la misma limpieza con la que coincidirían en el acierto.

Al nombrar los cuatro modelos basta con los apellidos de quienes los desarrollaron, sin repetir aquí lo que ya se explicó al presentarlos: Kasavana y Smith, con la matriz que cruza popularidad y margen de contribución en cuadrantes; Miller; Pavesic; y Hayes y Huffman, cuyo Goal Value abandona la matriz de cuadrantes y resume esas mismas dos variables en un único índice numérico por plato. Ninguno de los cuatro es más «correcto» que los otros: son cuatro formas de proyectar la misma realidad sobre ejes distintos, y el valor de tenerlos juntos no está en promediarlos ni en quedarse con el que más convenza, sino en usar el punto donde se separan como señal.

Ese punto de partida común tiene una referencia concreta en esta carta: el margen de contribución medio ponderado es de 8,16 €. Es la vara con la que cada modelo mide si un plato «deja» lo suficiente, y aun partiendo del mismo número, cada uno lo combina con la popularidad o con el food cost de una manera distinta; ahí empieza la discrepancia, no en el dato, sino en cómo se lee después. Hay una quinta lectura que conviene tener presente aunque no sea una de las cuatro que ordena este capítulo: LeBruto, Quain y Ashley (1995) incorporaron el coste (costo) de mano de obra al modelo de Kasavana y Smith y ampliaron su matriz original de 4 cuadrantes a 8, clasificando además cada plato según si su coste laboral es alto o bajo. Los propios autores lo resumen con una frase que conviene tener presente al leer cualquiera de estas lecturas: «los operadores ingresan dinero, no porcentajes». Es el mismo criterio que sostiene los dos patrones siguientes.

### Los patrones de discrepancia más frecuentes

De los 20 platos, 12 tienen tres o cuatro lecturas fuera de su franja esperada: dentro de ese grupo, 4 tienen tres lecturas fuera y 8 las cuatro. En el otro extremo, 4 platos tienen una única lectura fuera y 1 tiene dos lecturas fuera, el 5,0 % de la carta. La discrepancia, en esta carta, no es la excepción: es mayoría, y por eso conviene saber leerla en vez de tratarla como ruido de los modelos.

Tres patrones se repiten con más frecuencia que ningún otro:

- Margen alto con food cost porcentual pobre: es un plato de producto caro que, aun así, deja dinero real por comensal servido. El error habitual es mirar sólo el porcentaje, ver que sale alto, y sentenciar el plato como problemático. La decisión casi nunca es retirarlo: se revisa el precio de venta o el tamaño de la ración, porque el margen de contribución ya ha demostrado que el cliente está dispuesto a pagarlo.
- Food cost porcentual excelente con margen bajo: vende mucho y deja poco por unidad. El sitio de ese plato no está en la cuenta de resultados, sino en el ticket, en lo que arrastra a pedir alrededor y en el volumen que sostiene la sala. Se decide si se mantiene como gancho comercial o si se ajusta el precio para que ese food cost tan favorable empiece a traducirse en margen de contribución real.
- Popularidad baja en todos los modelos: antes de retirar el plato se comprueba si el problema está en el plato mismo o en su descripción y en su sitio dentro de la carta. Un plato correcto mal colocado, con un nombre que no vende o pegado a un competidor directo más barato en la misma página, puede leer como un fracaso sin serlo.

La regla que ordena estos tres patrones es sencilla de enunciar y fácil de saltarse: no se tocan más de dos o tres platos a la vez. Cada cambio de precio o de ración mueve el mix de ventas de toda la carta y, con él, los umbrales de todos los demás platos: lo que hoy queda por encima de la media de margen puede quedar por debajo en cuanto cambie qué se vende más. Después de cada tanda se vuelve a medir con los cuatro modelos; no se asume que el ajuste funcionó porque la intuición lo sugiera. El cuadro siguiente recoge, plato a plato, dónde coincide cada lectura y dónde se separa.

### Las cuatro erres: reformular, resubir, rediseñar, retirar

Cuando los cuatro métodos —el original de Kasavana y Smith, la reformulación de Miller, la de Pavesic y el Goal Value de Hayes y Huffman— coinciden en la lectura de un plato, conviene no leer esa coincidencia como una validación. Los cuatro parten de los mismos datos de entrada: las mismas ventas, el mismo coste de la ficha técnica y el mismo precio de la carta. Si ese dato de origen está mal cargado, los cuatro modelos lo heredan por igual, y cuatro lecturas de acuerdo sobre un error siguen siendo un error. Lo que aporta información de verdad es el punto exacto en el que los métodos dejan de coincidir: ahí cada uno mira una variable distinta de la misma cuenta.

De los 20 platos con ventas en la carta, 3 reciben la lectura más favorable en los cuatro métodos a la vez y otros 3 no tienen ninguna lectura fuera de esa categoría, un 15,0 % de la carta. 4 platos tienen una sola lectura fuera, 1 tiene dos lecturas fuera —el 5,0 % de la carta— y 12 tienen tres o cuatro lecturas fuera de la mejor categoría: de ellos, 4 tienen tres lecturas fuera y 8 tienen las cuatro fuera. Son esos 12 los que exigen mirar la tabla de abajo plato por plato, no de un vistazo, porque ahí es donde aparecen tres patrones que se repiten con más frecuencia que el resto.

El primero es el margen alto con food cost porcentual pobre: un plato de producto caro —pescado, marisco, una pieza de carne noble— que deja un margen de contribución sólido en euros aunque su porcentaje de coste sobre el precio de venta sea alto porque el producto de base también lo es. Ese plato no se retira: se reformula la ración o se resube el precio, porque el problema no está en si conviene venderlo sino en cuánto se está cobrando por venderlo.

El segundo patrón es el inverso: food cost porcentual excelente con margen de contribución bajo. Vende mucho y deja poco por unidad. Ahí el sitio del plato no es la cuenta de resultados, es el ticket: empuja el número de comensales o arrastra venta de otros platos, y lo que corresponde es decidir, con criterio, si se mantiene como gancho de la carta. La incorporación del coste de mano de obra al modelo de Kasavana y Smith, publicada por LeBruto, Quain y Ashley (1995), amplía la matriz original de 4 cuadrantes a 8 para separar estos dos casos, y sus autores lo resumen con una frase que conviene tener presente al leer cualquier porcentaje: «los operadores ingresan dinero, no porcentajes».

El tercer patrón es la popularidad baja en los cuatro modelos a la vez. Antes de retirar el plato, hay que comprobar si el problema es el plato o es su descripción y su sitio en la carta: un nombre que no cuenta nada, una posición perdida en una página larga o una fotografía ausente bastan para hundir la venta de algo que, contado de otra forma, funciona. Rediseñar —cambiar el texto, la posición, la fotografía— va antes que retirar, y sólo cuando el rediseño ya se ha probado y la venta sigue sin moverse tiene sentido sacar el plato de la carta.

### El orden de intervención y cuántos platos se tocan a la vez

Las cuatro erres no son un algoritmo cerrado: son un orden de intervención, del cambio más ligero al más drástico, y quien decide dónde parar es quien conoce a su cliente, no la matriz. Reformular —tocar receta o ración— y resubir —tocar precio— son los movimientos más baratos y los más fáciles de revertir si no funcionan. Rediseñar —tocar cómo se cuenta y dónde se coloca el plato— exige más trabajo pero sigue sin sacar nada de la carta. Retirar es el único movimiento que no se puede deshacer sin reescribir la ficha técnica y volver a fotografiar: va el último, reservado a los platos del tercer patrón que ya han pasado por el rediseño sin moverse.

La regla operativa que sostiene todo el capítulo es no tocar más de dos o tres platos a la vez. Cada cambio de precio, de ración o de posición mueve el mix de ventas de la carta entera, y ese mix es el dato de entrada del que dependen los cuatro métodos: el margen de contribución medio ponderado de la carta, hoy en 8,16 €, se recalcula con cada intervención, y con él se mueven los umbrales de popularidad y de food cost del resto de platos, no sólo del que se ha tocado. Intervenir en bloque sobre media carta de golpe invalida la siguiente lectura antes de haberla hecho.

Después de cada tanda de dos o tres platos toca volver a pasar los cuatro métodos y comprobar, otra vez, dónde discrepan. El modelo seminal de la matriz de popularidad y margen de contribución y el Goal Value Analysis de Hayes y Huffman, que resume cada plato en un índice numérico único en lugar de situarlo en una matriz de cuadrantes, sirven aquí para lo mismo que en la primera lectura: confirmar si el cambio ha movido al plato de categoría o si ha desplazado el problema a otro sitio de la carta.

**Las cuatro lecturas del mismo plato, una al lado de otra (matriz-multimetodo-carta.xlsx, hoja «Comparativa»)**

| Plato | Familia | Kasavana & Smith | Miller | Pavesic | Goal Value | Lecturas fuera | Decisión sugerida |
|---|---|---|---|---|---|---|---|
| Croquetas de jamón ibérico (6 ud) | Entrantes | Plowhorse | Winner | Prime | Por encima del objetivo | 1 | Resubir |
| Ensalada de tomate rosa, ventresca y cebolleta | Entrantes | Star | Winner | Prime | Por encima del objetivo | 0 | Mantener |
| Gambas al ajillo | Entrantes | Star | Marginal | Standard | Por debajo del objetivo | 3 | Revisar |
| Huevos rotos con patatas y chistorra | Entrantes | Plowhorse | Winner | Prime | Por encima del objetivo | 1 | Resubir |
| Tabla de quesos de la zona | Entrantes | Puzzle | Loser | Problem | Por debajo del objetivo | 4 | Rediseñar |
| Alcachofas confitadas con jamón | Entrantes | Puzzle | Marginal | Sleeper | Por debajo del objetivo | 4 | Rediseñar |
| Sopa de tomate asado con albahaca | Entrantes | Dog | Marginal | Sleeper | Por debajo del objetivo | 4 | Revisar |
| Solomillo de cerdo ibérico con puré de boniato | Principales | Star | Winner | Prime | Por encima del objetivo | 0 | Mantener |
| Bacalao confitado al pil-pil | Principales | Star | Marginal | Problem | Por debajo del objetivo | 3 | Reformular |
| Hamburguesa de vaca madurada con patatas | Principales | Plowhorse | Winner | Prime | Por encima del objetivo | 1 | Resubir |
| Arroz meloso de secreto ibérico y setas | Principales | Plowhorse | Marginal | Standard | Por encima del objetivo | 3 | Resubir |
| Chuletón de vaca madurada (500 g) | Principales | Puzzle | Loser | Problem | Por debajo del objetivo | 4 | Rediseñar |
| Lubina a la sal | Principales | Puzzle | Loser | Problem | Por debajo del objetivo | 4 | Rediseñar |
| Pollo de corral asado con patatas | Principales | Plowhorse | Winner | Prime | Por encima del objetivo | 1 | Resubir |
| Lasaña de verduras de temporada | Principales | Dog | Marginal | Sleeper | Por debajo del objetivo | 4 | Revisar |
| Tataki de atún rojo con sésamo | Principales | Puzzle | Loser | Problem | Por debajo del objetivo | 4 | Rediseñar |
| Tarta de queso cremosa | Postres | Star | Winner | Prime | Por encima del objetivo | 0 | Mantener |
| Torrija caramelizada con helado | Postres | Plowhorse | Winner | Sleeper | Por debajo del objetivo | 3 | Resubir |
| Coulant de chocolate | Postres | Star | Marginal | Standard | Por encima del objetivo | 2 | Revisar |
| Fruta de temporada preparada | Postres | Dog | Loser | Problem | Por debajo del objetivo | 4 | Retirar |

**Cuántos platos discrepan, y cuánto (matriz-multimetodo-carta.xlsx, hoja «Comparativa»)**

| Lecturas fuera de la mejor categoría | Platos | % de la carta |
|---|---|---|
| 0 | 3 | 15,0 % |
| 1 | 4 | 20,0 % |
| 2 | 1 | 5,0 % |
| 3 | 4 | 20,0 % |
| 4 | 8 | 40,0 % |

*La columna de la izquierda no es una nota: es el número de modelos que sacan al plato de su mejor categoría. Cuanto más arriba, más de acuerdo están los cuatro en que ahí hay algo que revisar.*


---

## 14. Carta Corta, Menú de Precio Fijo, Buffet y Banquete

### Tamaño de carta: qué se gana al podar y qué se pierde

Podar la carta (menú) no es una cuestión estética: es logística de cocina. Cada plato dado de alta arrastra su propio stock, su propia merma cuando no rota como se esperaba, y una línea más que la brigada tiene que dominar en el pase. Menos referencias concentra la compra en menos proveedores, así que el volumen por línea sube y con él el poder de negociación con cada uno. Menos platos significa también menos producto abierto en cámara y menos ración que acaba en la basura al cierre porque nadie la pidió. La carta de ejemplo de esta guía tiene 20 platos dados de alta, y esa cifra no es una recomendación: es sólo el punto de partida de los ejemplos siguientes.

Lo que se pierde al recortar es cobertura. Cada plato que desaparece deja fuera al comensal que sólo venía por él, a la alergia que sólo cubría esa opción o al grupo que necesitaba una alternativa vegetariana o sin gluten para cerrar la mesa completa. También se pierde margen frente a la estacionalidad, porque una carta corta tiene menos hueco para rotar producto de temporada sin sacar algo fijo. La decisión no tiene un número óptimo: se toma plato a plato, mirando qué venta arrastra cada referencia y qué stock exige mantenerla viva, apoyándose en los datos que ya maneja el lector.

### Menú de precio fijo: el margen lo decide el mix

En un menú de precio fijo el ingreso está cerrado antes de que se siente el primer comensal: el precio de venta al público, con el impuesto sobre el valor añadido de la restauración en sala al tipo reducido del 10 %, es de 14,50 €, lo que deja 13,18 € sin ese impuesto por cada menú servido. Ese ingreso no se mueve aunque cambie por completo lo que la gente pide, así que el resultado del mes depende enteramente del mix. Gestionar un menú de precio fijo es, en la práctica, gestionar ese reparto.

El cuadro siguiente lo demuestra con el mismo menú, el mismo precio y el mismo volumen de servicio —100 menús al mes—, variando sólo lo que la gente elige. Con el mix base el coste (costo) medio del menú es de 5,63 €, con un food cost del 42,7 % y un margen de contribución de 7,55 € por menú que, multiplicado por el volumen del mes, deja 754,93 €. Basta con que el comensal se decante más por las opciones caras del escenario A para que el coste medio suba a 5,93 €, el food cost a 45,0 % y el margen del mes baje a 725,18 €; y basta con que el mix se incline hacia el escenario B, con más opciones económicas, para que el coste medio baje a 5,35 €, el food cost a 40,6 % y el margen del mes suba a 782,93 €. Mismo menú, mismo precio, mismos 100 comensales, tres resultados distintos: la diferencia entera está en lo que se pide, no en lo que se cobra.

La palanca real no es subir el precio del menú. Si el plato más caro es también el más pedido, lo que se cambia es su sitio en la pizarra o en la carta del día, o se refuerza el atractivo de la alternativa más barata para desplazar demanda hacia el escenario B. Y hay un coste que muchos escandallos (costeo de recetas) de menú del día olvidan: el pan, el café y la bebida incluida no forman parte del precio de ningún plato del mix y, sin embargo, hay que servirlos siempre; en esta carta de ejemplo ese coste fijo por menú es de 0,55 € y, sobre un ticket de 14,50 €, pesa lo bastante como para no tratarlo como un detalle menor.

Fuera de la carta a la carta, el mismo principio cambia de forma. En buffet, banquete y hotel no se cuesta por ración emplatada sino por comensal servido, y el dato que gobierna esa cuenta es el consumo medido por cabeza, que no viene en ningún libro: hay que medirlo en la propia casa, servicio a servicio. Como referencia de contraste internacional —no como benchmark español, porque no hay un dato local equivalente en el research— el food cost habitual en hotel F&B y buffet se mueve entre el 28 % y el 40 % sobre venta (Cucinovo — Food Cost % by Restaurant Type, 2026). En catering y eventos el mix no se observa después de servir: se pacta en la propuesta que firma el cliente, así que el trabajo de ingeniería de menú tiene que hacerse antes de esa firma, no después del servicio.

### Los dos escenarios de mix y qué hacer con ellos

En un menú de precio fijo el ingreso ya está cerrado antes de que se siente el primer comensal: 14,50 € con el IVA de restauración en sala, el mismo tipo reducido del 10 % que se aplica a todo el consumo servido en mesa, bebida alcohólica incluida, y 13,18 € una vez descontado ese impuesto. Lo que no está cerrado es el coste, porque depende de qué elige la gente en cada curso. Gestionar un menú de precio fijo es, en la práctica, gestionar ese reparto: el mix.

La tabla de abajo lo demuestra con el mismo menú, el mismo precio y el mismo volumen de servicio —100 menús al mes— repartido en tres escenarios. Con el mix base, el coste medio es de 5,63 €, el food cost del 42,7 % y el margen de contribución de 7,55 € por menú, 754,93 € al mes. En el escenario A, con el comensal inclinado hacia lo más caro, el coste sube a 5,93 €, el food cost al 45,0 % y el margen baja a 7,25 €, 725,18 € al mes. En el escenario B, volcado hacia lo económico, el coste baja a 5,35 €, el food cost al 40,6 % y el margen sube a 7,83 €, 782,93 € al mes. Precio, IVA y comensales son idénticos: sólo cambia lo que se pide, y basta para mover el mes entero.

Ahí está la palanca real: si el plato más caro del menú resulta también el más pedido, no se toca el precio del menú, se cambia su sitio en la pizarra o se refuerza la alternativa que compite con él, para acercar el reparto al escenario B. El food cost objetivo de este menú es del 30 %, por debajo del 28-32 % que qamarero.com (2026) atribuye a la restauración tradicional, así que la desviación hacia el escenario A pesa doble. Y hay un coste que muchos escandallos de menú del día pasan por alto: pan, café y bebida incluida suman 0,55 € de coste fijo por menú, antes de que el comensal elija nada. En un ticket de 13,18 € sin impuestos, ese descuento previo pesa mucho más que en una carta de ticket alto, y conviene restarlo del PVP antes de calcular el margen de cada opción, no después.

### Buffet, banquete y hotel: el mismo problema con otra escala

En buffet, banquete y F&B de hotel el problema es el mismo —ingreso cerrado, resultado dependiente de lo que se consume— pero cambia la unidad de coste: no se cuesta por ración emplatada, porque no hay ración fija, sino por comensal servido. El dato que gobierna esa cuenta es el consumo medio por cabeza, y no sale de ningún libro ni de ninguna plantilla: se mide en la propia casa, servicio a servicio, porque cada oferta y cada perfil de cliente consume distinto. Cucinovo, en su informe Food Cost % by Restaurant Type (2026), sitúa el food cost del F&B de hotel y del buffet entre el 28 y el 40 % sobre venta; es un dato estadounidense, sin equivalente español localizado, así que sirve como contraste internacional y orden de magnitud, nunca como el número que hay que alcanzar en una casa concreta.

En catering y eventos el mix no se gestiona durante el servicio: se pacta en la propuesta que se firma con el cliente, con el menú, las cantidades y las opciones cerradas semanas antes de que se ponga un plato en la mesa. Por eso el trabajo de ingeniería de este formato se hace antes de firmar y no después de servir: en la propuesta se decide qué entra en cada opción, a qué coste y qué margen deja, porque una vez firmado el presupuesto ya no queda margen de maniobra para corregir el reparto con la pizarra ni con ningún otro gesto de sala.

### Catering y eventos: el mix se pacta antes

En catering y eventos el ingreso no solo está cerrado como en el menú de precio fijo: está firmado semanas o meses antes de que se sirva un solo plato. El comensal no elige en la mesa; elige, si elige algo, en un formulario de opciones que el cliente reenvía al organizador con los días de antelación que marque el contrato. Eso desplaza todo el trabajo de ingeniería al momento de redactar la propuesta: ahí es donde se decide qué opciones entran en el menú del evento, cuántas alternativas de plato principal se ofrecen y qué acompaña a cada una, porque una vez el cliente firma y confirma el número de comensales ya no queda margen para corregir el mix moviendo un plato de sitio en la carta o mejorando la alternativa que le compite dentro del propio menú, como sí ocurre en el día a día del menú de precio fijo. La corrección, aquí, o se hace antes de firmar, o no se hace.

Eso obliga a costear cada opción del evento con su escandallo propio antes de mandar el presupuesto, no después de aceptarlo, y a modelar de antemano al menos dos o tres repartos plausibles del mix (uno cómodo, uno realista y uno exigente) para comprobar que el precio por comensal aguanta el peor de los tres, no solo el que más conviene. Un presupuesto que solo se ha probado contra el reparto más favorable es un presupuesto que puede perder margen en cuanto los invitados elijan de forma distinta a la prevista.

Conviene además separar, en el cálculo, lo que escala con cada comensal de lo que no escala. El coste por cabeza cubre la comida y la bebida servida; el personal de sala y cocina, el alquiler de menaje, mantelería o carpa y la logística de transporte no crecen en la misma proporción que el número de invitados, y mezclarlo todo en una única cifra por comensal esconde en qué partida se está perdiendo margen cuando el evento es pequeño.

En la práctica, esto se traduce en unas pocas decisiones que conviene tomar siempre en la misma fase, antes de que el evento se acepte:

- Cerrar el catálogo de opciones del evento, con su coste real ya calculado, antes de que el comercial se siente a negociar con el cliente.
- Fijar en el propio contrato el plazo y la forma en que se confirma el desglose de comensales por opción, porque ese desglose es el mix real del evento.
- Exigir una garantía mínima de comensales facturados, de forma que un aforo final más bajo no traslade el mismo coste fijo a menos cabezas.
- Revisar, al cerrar el evento, el margen con el mix que finalmente se confirmó y no solo con el que se presupuestó, para que la siguiente propuesta parta de un dato real.

La lógica es la misma que gobierna cualquier menú de precio fijo: el resultado depende de qué elige la gente, no del precio que se cobra. En catering y eventos, sin embargo, toda esa ingeniería tiene que estar terminada antes de que el cliente firme, porque después de la firma ya no queda ninguna palanca que mover.

**Las opciones del menú y los tres repartos de mix (matriz-multimetodo-carta.xlsx, hoja «Menú Precio Fijo»)**

| Curso | Opción | Coste por ración (€) | Mix base (%) | Mix escenario A (%) | Mix escenario B (%) |
|---|---|---|---|---|---|
| Primeros | Ensalada de la huerta | 1,10 € | 40 % | 25 % | 35 % |
| Primeros | Crema de calabaza | 1,05 € | 25 % | 20 % | 45 % |
| Primeros | Pasta al pesto | 1,60 € | 35 % | 55 % | 20 % |
| Segundos | Pollo asado con patatas | 2,80 € | 45 % | 30 % | 60 % |
| Segundos | Merluza a la romana | 3,90 € | 30 % | 45 % | 15 % |
| Segundos | Albóndigas de ternera | 3,20 € | 25 % | 25 % | 25 % |
| Postres | Flan casero | 0,50 € | 55 % | 40 % | 70 % |
| Postres | Fruta del tiempo | 0,70 € | 45 % | 60 % | 30 % |

*Los tres repartos suman el 100 % dentro de cada curso; lo único que cambia entre escenarios es qué opción se lleva la gente.*

**El coste medio de cada curso según el mix (matriz-multimetodo-carta.xlsx, hoja «Menú Precio Fijo»)**

| Curso | Coste medio base (€) | Coste medio A (€) | Coste medio B (€) |
|---|---|---|---|
| Primeros | 1,26 € | 1,37 € | 1,18 € |
| Segundos | 3,23 € | 3,39 € | 3,06 € |
| Postres | 0,59 € | 0,62 € | 0,56 € |

**El mismo menú, el mismo precio, tres resultados (matriz-multimetodo-carta.xlsx, hoja «Menú Precio Fijo»)**

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

## 15. Multicanal: Sala, Take Away y Delivery

### Tres canales, tres cuentas de resultados

La carta (menú) no cambia de canal a canal, pero la cuenta de resultados sí. La comisión de la plataforma no se resta del margen como un coste (costo) fijo por plato: se aplica sobre el precio de venta, y por eso escala con él. Un mismo plato al mismo precio tiene un food cost efectivo distinto en sala, en take away y en delivery, y ese es el número que hay que mirar, no el de la carta de sala.

El food cost objetivo es del 30 % en sala y en take away, y sube al 40 % en delivery para absorber la comisión de la plataforma, parametrizada en el 30 % sobre el precio de venta. La hoja «Resumen» de simulador-repricing-multicanal.xlsx recoge el food cost efectivo medio: 31,4 % en sala, 38,2 % en take away y 54,6 % en delivery. Dieciséis platos son viables en sala, sólo doce en delivery, y ocho hay que excluirlos o reformularlos. El margen mensual pasa de 43.635 € en sala a 30.050 € en delivery: -13.585 € que sólo se ven en el cuadro siguiente.

Las croquetas lo ilustran: mismo plato, mismo precio, food cost del 24,4 % en sala frente al 46,5 % en delivery. Para volver al 40 % objetivo, la hoja despeja el precio de venta sin IVA que necesita en la aplicación —10,00 €— y lo compara con el precio techo de ese plato ahí: 11,60 €. La aplicación tiene su propio mercado; un precio por encima de la competencia no se vende aunque los números cuadren, así que el simulador no da un precio, da un precio necesario frente al techo. Por debajo, sube el precio y el ajuste está resuelto; por encima, el plato se saca de la carta de esa aplicación o se reformula en un formato que viaje mejor y pese menos en el coste de envase por ración: no se sube el precio de un plato que ese mercado ya no va a pagar, se cambia de plato.

En Hispanoamérica, las nueve casillas de la matriz fiscal y de comisión son editables: no hay que aceptar los porcentajes de España. La hoja cita como referencia a Rappi y DiDi en México, y a PedidosYa en Argentina, Uruguay y Panamá; cada operador negocia su condición con cada local, y la casilla se sustituye por el dato real del contrato.

### La comisión no es el único coste: packaging y platos por pedido

El envase no se paga por plato, sino por pedido: su coste por plato es una división —packaging por pedido entre platos del pedido medio— y esa cifra vive en una sola celda de la hoja «Parámetros» de simulador-repricing-multicanal.xlsx. En take away el packaging por pedido es 1,75 €; en delivery también, pero el pedido medio lleva 2,5 platos, así que el packaging por plato baja a 0,70 €. Mover los platos por pedido —un pedido familiar reparte mejor el envase que uno de un solo plato— mueve esa celda, y con ella el food cost efectivo de toda la carta en delivery, sin tocar un precio.

La comisión que usa el simulador, el 30 % sobre el precio de venta, hay que tratarla como orden de magnitud, no como tarifa cerrada: ninguna plataforma publica un tarifario oficial, y todas dependen de la zona, del plan contratado y de quién hace el reparto. Glovo cobra entre el 15 % y el 35 % más IVA según zona y demanda —hasta el 35 % si reparte ella misma—, con cuota mensual en torno a 39 € y un 2-5 % adicional de marketing (fuente: qamarero.com, «Cuánto cobra Glovo a los restaurantes», 2026); el resto sigue el mismo patrón por planes —Uber Eats del 15 % al 30 %, Just Eat del 13 % al 35 % más 0,30 € por pedido, Deliveroo del 25 % al 30 % más una cuota tecnológica de 50 € al mes— (fuente: qamarero.com, «Comisiones delivery: cuánto cobran realmente las plataformas», 2026). Y el porcentaje nominal no es todo el coste: encima hay packaging que tasa la propia plataforma —1,35-2,15 € por pedido—, descuentos promocionales del 20-30 % exigidos para dar visibilidad, y penalizaciones de hasta 2 puntos más (misma fuente).

Un tercer factor no toca el food cost pero sí el precio que ve el cliente: el IVA. En sala todo tributa al tipo reducido, alcohol incluido, por el servicio de hostelería; sin ese servicio —take away y delivery— la comida es entrega de bienes y tributa al 10 %, como alimento ordinario, y el alcohol sale del tipo reducido para pasar al 21 % (Ley 37/1992, arts. 90 y 91.Uno.1.1.º; DGT, consulta vinculante V2254-22, de 26 de octubre de 2022). A ese mismo 21 % tributan, desde el 1 de enero de 2021, los refrescos, zumos y gaseosas con azúcares o edulcorantes añadidos (Ley 37/1992, art. 91.Uno.1.1.º, en la redacción de la Ley 11/2020 de Presupuestos Generales del Estado). La propia DGT, resolviendo precisamente sobre una plataforma de reparto a domicilio con repartidores subcontratados, confirma el reparto: comida al 10 %, alcohol o refrescos azucarados al 21 % (consulta V2254-22). Al leer el precio techo de la aplicación conviene recordarlo: no tributa igual la ración de croquetas que la cerveza que la acompaña.

### El IVA cambia con el canal y con el producto

El IVA no tributa igual en los tres canales, y dentro de cada canal tampoco tributa igual todo lo que hay en el pedido. En sala, todo lo que sirves —también la copa de vino o la cerveza— tributa al tipo reducido de la restauración, sin distinguir plato de bebida. Take away y delivery dejan de ser un servicio y pasan a ser una entrega de bienes: la comida elaborada que sale sin servicio de hostelería tributa como alimento ordinario, al 10 % (Ley 37/1992, art. 91.Uno.1.1.º, y DGT, consulta vinculante V2254-22, 2022-10-26). La bebida alcohólica pasa al 21 % en cuanto sale sin servicio (Ley 37/1992, arts. 90 y 91.Uno.1.1.º, y DGT V2254-22), igual que los refrescos, zumos y gaseosas con azúcares o edulcorantes añadidos desde el 1 de enero de 2021 (Ley 37/1992, art. 91.Uno.1.1.º, redacción dada por la Ley 11/2020 de PGE 2021, art. 69); la DGT lo confirmó en el caso exacto de una plataforma de reparto a domicilio, con los dos tipos a la vez —10 % comida, 21 % alcohol y refrescos azucarados o edulcorados— (V2254-22, 2022-10-26). Un mismo pedido de delivery puede llevar los dos tipos a la vez: hay que aplicarlos plato a plato y bebida a bebida, nunca como un tipo único para todo el pedido.

### El precio techo: hasta dónde te deja subir la aplicación

La comisión no es un coste fijo que se resta del margen: se aplica sobre el precio de venta y escala con él. Un mismo plato, al mismo precio, tiene un food cost efectivo distinto según el canal, y ese es el número que hay que vigilar, no el de la sala: 31,4 % en sala —pegado al objetivo del 30 %—, 38,2 % en take away —mismo objetivo— y 54,6 % en delivery, donde el objetivo se relaja al 40 % para dejarle hueco a una comisión que, en la plantilla, es del 30 % sobre el pedido.

El packaging se mira por plato, no por pedido: el envase se paga por pedido —1,75 € en take away, otros 1,75 € en delivery— y su coste por plato depende de cuántos platos lleve el pedido medio. Con 2,5 platos por pedido en delivery, esos 1,75 € bajan a 0,70 € por plato: un plato suelto carga el envase entero; varios comensales lo diluyen.

Con la comisión escalando sobre el precio y el packaging por plato, llega el límite real: la aplicación tiene su propio mercado, y un precio por encima de la competencia no se vende aunque los números cuadren. La hoja no da un precio: da el precio necesario para el food cost objetivo del canal y lo compara con el precio techo de esa carta en esa aplicación. En las croquetas, el food cost pasa del 24,4 % en sala al 46,5 % en delivery al mismo precio; el objetivo pide un PVP sin IVA de 10,00 €, y el techo está en 11,60 €. De los 16 platos viables en sala sólo 12 lo son en delivery; los otros 8 no llegan al objetivo sin pasarse de techo, y la decisión es sacarlos de esa aplicación o reformularlos para que viajen mejor, no forzar el precio. Resultado: 43.635 € de margen mensual en sala frente a 30.050 € en delivery, 13.585 € menos.

Las comisiones son orden de magnitud, no tarifario oficial —ninguna plataforma publica tarifa cerrada— y dependen de la zona, del plan y de quién reparte:

- Glovo: 15-35 % más IVA según zona y demanda (35 % si reparte la propia Glovo), cuota de unos 39 € al mes y marketing adicional del 2-5 % (qamarero.com — «Cuánto cobra Glovo a los restaurantes», 2026).
- Uber Eats: 30, 25 o 15-20 % según básico, plus o premium.
- Just Eat: 13 % de escaparate, o 25-35 % si reparte, más 0,30 € por pedido.
- Deliveroo: 30 % en estándar o 25 % en el reducido —desde 500 pedidos al mes—, más 50 € al mes de fee tecnológico.

Estas tres últimas, y los costes que siguen, vienen de qamarero.com — «Comisiones delivery: cuánto cobran realmente las plataformas» (2026): fuera del porcentaje nominal quedan 1,35-2,15 € de packaging por pedido, descuentos del 20-30 % para ganar visibilidad, y hasta 2 puntos más de comisión como penalización por rendimiento.

Si trabajas en Hispanoamérica, tanto la matriz fiscal de nueve casillas como las comisiones son editables en la plantilla; ahí cambian los operadores de referencia, con Rappi y DiDi en México y PedidosYa en Argentina, Uruguay y Panamá.

### Qué platos no deberían estar en delivery

La comisión de la aplicación no se resta del margen como si fuera un coste (costo) fijo por plato: se aplica sobre el precio de venta, así que escala con él, y un mismo plato con el mismo precio en la carta (menú) tiene un food cost efectivo distinto en cada canal. Ese es el número que hay que vigilar, no el de la sala. De ahí que el food cost objetivo sea propio de cada canal —30 % en sala, 30 % en take away y 40 % en delivery— frente al efectivo que arroja hoy la carta completa: 31,4 %, 38,2 % y 54,6 %.

El envase es la otra pieza mal calculada con frecuencia: el take away y el delivery pagan el packaging por PEDIDO, no por plato —1,75 € en los dos canales—, así que su coste por plato depende de cuántos platos lleve el pedido medio. En delivery son 2,5, y de ahí sale el packaging por plato ya resuelto en la hoja: 0,70 €, una celda, no una estimación a ojo.

Con la comisión sobre el precio y el packaging repartido por plato, el cálculo da el precio necesario para llegar al food cost objetivo del canal, y lo compara con el precio techo: el que tolera el mercado de la propia aplicación antes de que el plato deje de venderse aunque las cuentas cuadren. Las croquetas necesitan 10,00 € sin IVA para bajar del 40 % en delivery —frente al 24,4 % de sala—, y el techo está en 11,60 €: hay recorrido. Cuando el precio necesario supera el techo, no se sube el precio a la fuerza: se saca el plato de esa aplicación o se reformula en un formato que viaje mejor. De los 16 platos viables en sala, delivery sólo sostiene 12; los otros 8 hay que excluirlos o reformularlos, y son la diferencia entre los 43.635 € de sala y los 30.050 € de delivery: -13.585 € de margen mensual, con la misma cocina detrás.

Las comisiones no son un tarifario cerrado. Glovo cobra el 15-35 % más IVA según zona y demanda —hasta el 35 % si gestiona el reparto—, con cuota mensual de unos 39 € y marketing adicional del 2-5 % (qamarero.com, «Cuánto cobra Glovo a los restaurantes», 2026). Uber Eats va del 15 % al 30 % según el plan; Just Eat cobra un 13 % de escaparate o un 25-35 % con reparto propio, más 0,30 € por pedido; Deliveroo cobra un 30 % estándar, 25 % desde 500 pedidos al mes, más 50 € mensuales de fee tecnológico (qamarero.com, «Comisiones delivery: cuánto cobran realmente las plataformas», 2026). Son horquillas de fuente sectorial, no tarifa oficial: dependen de zona, plan y de quién reparte, y hay costes fuera del porcentaje nominal —1,35-2,15 € de packaging por pedido, descuentos de visibilidad del 20-30 % y hasta dos puntos de penalización por rendimiento, según la misma fuente.

El alcohol y los refrescos azucarados son, además, candidatos claros a salir del reparto por una razón fiscal. En sala todo tributa al tipo reducido, alcohol incluido; fuera de sala, la comida entregada sin servicio de hostelería es entrega de bienes y sigue al 10 % (Ley 37/1992, art. 91.Uno.1.1.º, y DGT, consulta V2254-22, 2022), pero el alcohol pasa al 21 % (Ley 37/1992, arts. 90 y 91.Uno.1.1.º, y DGT V2254-22, 2022), igual que los refrescos con azúcares o edulcorantes añadidos desde 2021 (Ley 37/1992, art. 91.Uno.1.1.º, redacción de la Ley 11/2020 de Presupuestos Generales del Estado). La propia DGT lo confirma para el supuesto exacto de una plataforma de reparto a domicilio: 10 % comida, 21 % alcohol y refrescos azucarados (DGT, consulta V2254-22, 2022). Cargar esa subida sobre una comisión que ya pesa sobre el precio suele bastar para dejar esas bebidas fuera del pedido.

### Vender fuera de España: qué casillas se cambian

La matriz fiscal y las comisiones de plataforma no vienen bloqueadas al caso español: son nueve casillas editables, pensadas para que el lector que opera en Hispanoamérica sustituya el tipo de IVA local y la horquilla de comisión de su operador sin tocar ninguna fórmula. La estructura del cálculo no cambia de un mercado a otro; lo que cambia es el contenido de esas nueve celdas.

Como referencia de qué operadores rellenar, se citan a modo de ejemplo Rappi y DiDi en México, y PedidosYa en Argentina, Uruguay y Panamá: son los que el lector encontrará facturando en su carta si opera en esos países, y cada uno negocia o publica su propia horquilla de comisión, que conviene introducir antes de fiar ningún precio necesario que salga de ella.

**Los parámetros de cada canal (simulador-repricing-multicanal.xlsx, hoja «Parámetros»)**

| Canal | Packaging (€/pedido) | Platos por pedido | Comisión de la plataforma (%) | Food cost objetivo (%) | Packaging por plato (€) |
|---|---|---|---|---|---|
| Sala | 0,00 € | 1,0 | 0 % | 30 % | 0,00 € |
| Take away | 1,75 € | 2,5 | 0 % | 30 % | 0,70 € |
| Delivery | 1,75 € | 2,5 | 30 % | 40 % | 0,70 € |

*Las seis columnas son editables: son el contrato que hayas firmado tú, no un estándar del sector.*

**Comisiones de las plataformas: orden de magnitud, no tarifario (simulador-repricing-multicanal.xlsx, hoja «Parámetros»)**

| Plataforma | Comisión y cuotas de referencia |
|---|---|
| Glovo | 15-35 % + IVA según zona y si la plataforma reparte; cuota mensual aprox. 39 € |
| Uber Eats | 30 % / 25 % / 15-20 % + IVA según plan |
| Just Eat | 13 % + IVA solo marketing (reparto propio) · 25-35 % + IVA servicio completo · 0,30 €/pedido |
| Deliveroo | 30 % + IVA estándar · 25 % + IVA a partir de 500 pedidos/mes · cuota tecnológica 50 €/mes |

*Estas horquillas son de referencia sectorial y cambian por zona, por plan contratado y según quién haga el reparto. El número que hay que escribir en la casilla es el de tu contrato.*

**Los tres canales, comparados (simulador-repricing-multicanal.xlsx, hoja «Resumen»)**

| Canal | Platos viables | Platos a excluir o reformular | Food cost efectivo medio (%) | Food cost objetivo (%) | PVP medio necesario (€) | Margen mensual total (€) |
|---|---|---|---|---|---|---|
| Sala | 16 | 4 | 31,4 % | 30,0 % | 15,51 € | 43.635 € |
| Take away | 12 | 8 | 38,2 % | 30,0 % | 17,85 € | 49.597 € |
| Delivery | 12 | 8 | 54,6 % | 40,0 % | 19,12 € | 30.050 € |


---

## 16. Beverage Cost: la Bodega Como Cuenta de Resultados Propia

### Por qué la bebida no se mide con la vara de la comida

El dato de partida sorprende a quien gestiona la carta (menú) como una sola partida: en «Consumos y beneficios de un restaurante», de CaixaBankLab y Fundación elBulli (2026), el coste (costo) de producto pesa un 34,5 % sobre los ingresos de bebida y solo un 28 % sobre los de comida, con un mix de ingresos del 70 % comida y el 30 % restante en bodega. Léase como matiz, no como regla general —depende del mix de cada bodega—, y por eso aquí cada categoría se trata por separado, no como un food cost único. Las referencias de mercado tampoco fijan un número cerrado: getbackbar.com y purimax.com (2026) mueven el beverage cost entre el 15 % y el 28 % según el tipo de bebida, media 20 %; ya en España, qamarero.com (2026) sitúa las bebidas estándar entre el 15 % y el 25 %, con un caso en el 27,5 % mensual. Son horquillas de fiabilidad media, así que el objetivo por categoría queda como casilla propia y editable: 30 % en vinos, 22 % en cervezas y refrescos, 20 % en destilados y cócteles. Contra esos tres objetivos se lee el mes de bodega: 43.657 € de ventas, 11.503,96 € de coste, un beverage cost ponderado del 26,4 % y un margen de contribución de 32.153,04 €, con los vinos pesando un 41,6 % de esas ventas y cervezas y refrescos otro 35,6 %. Hay además una frontera que la comida no comparte: el IVA cambia según el canal. La misma botella tributa al 10 % en sala, como servicio de hostelería y con el alcohol incluido (art. 91.Uno.2.2.º de la Ley 37/1992), y al 21 % cuando el cliente se la lleva sin servicio, porque entonces la entrega queda fuera del tipo reducido (arts. 90 y 91.Uno.1.1.º de la Ley 37/1992 y consulta V2254-22 de la Dirección General de Tributos). Las columnas de precio con IVA de la hoja resuelven los dos casos solas.

### Vino: la copa cambia la ecuación de la botella

El vino explica mejor que nadie cómo la unidad de venta cambia el resultado. Vender por copa mejora el porcentaje frente a la botella entera —el tinto de la casa cuesta 0,78 € la copa y deja 2,22 € de margen, con un beverage cost del 26,0 % en copa frente al 28,7 % en botella—, pero ese porcentaje solo se sostiene si el número de copas por botella se respeta: con 530 botellas y 2.540 copas al mes, esa relación es el dato que vigilar, porque en cuanto se desvía, el beverage cost sube sin que nadie lo note hasta cerrar el mes, y la merma no aparece en ninguna factura. El conjunto de vinos cierra con un beverage cost ponderado del 30,2 %, prácticamente sobre el objetivo del 30 %.

La cerveza de barril juega otro partido: se compra en litros y se vende en centilitros, y entre uno y otro hay una merma de espuma en el tiro y de limpieza de líneas que ningún escandallo (costeo de recetas) recoge por sí solo. Con 6.360 servicios de cerveza y refrescos al mes y un beverage cost ponderado del 25,4 % frente al objetivo del 22 %, esa merma ya tiene nombre propio en el resumen. El cóctel se cuesta como una ficha de escandallo en miniatura, ingrediente a ingrediente, y la mezcla —hielo que se funde, fruta que se descarta, el chorro que sobra al servir— suele pesar más en el coste final de lo que el camarero cree al montar la copa; los combinados quedan en el 21,6 % y los cócteles en el 19,7 %, los dos por debajo del objetivo del 20 % de la categoría.

La lectura de conjunto está en la fila de abajo del resumen: cada categoría tiene su objetivo editable en la hoja «Parámetros» de carta-de-bebidas-beverage-cost.xlsx, y el libro calcula que 646,38 € de margen se recuperarían si cada una alcanzase el suyo. Ese número, y no el porcentaje ponderado de toda la bodega, es el que marca por dónde empezar.

### Cerveza de barril y refrescos: el coste por servicio

Conviene abrir con el dato que rompe el tópico. El informe de CaixaBankLab y la Fundación elBulli sobre consumos y beneficios del restaurante medio español (2026), sobre un mix del 70 % de facturación en comida y el 30 % en bebida, da un 28 % de coste sobre las ventas de comida frente a un 34,5 % sobre las de bebida: la bodega pesa, proporcionalmente, más sobre sus propios ingresos que la comida sobre los suyos, lo contrario de lo que suele darse por hecho. No es regla universal, es un matiz que depende del mix de tu bodega y de cuánta copa se sirve.

Ahí entra la decisión copa contra botella. Vender por copa mejora el porcentaje: en el tinto de la casa, la copa cuesta 0,78 € y deja un margen de 2,22 €, con un beverage cost del 26,0 % frente al 28,7 % de la botella entera. Lo que sostiene esa mejora es el número de copas que salen de cada botella, y también lo que se escapa de la vista: con 530 botellas vendidas al mes y 2.540 copas, esa relación confirma si el escanciado se ajusta a lo previsto. Sirve un poco de más en cada copa y el beverage cost real se dispara sin que ningún ticket lo delante.

El barril tiene su propia trampa: se compra por litros y se vende por centilitros, y entre ambas unidades se cuela la espuma de un tiraje mal regulado y la limpieza de líneas, que consume producto sin generar ticket. Por eso el objetivo de cervezas y refrescos se fija aparte, en el 22 %, con 6.360 servicios vendidos al mes sosteniendo un beverage cost ponderado del 25,4 % y un peso del 35,6 % sobre las ventas de la bodega, dentro de la horquilla del 20 % al 26 % que el agregado sectorial de getbackbar.com y purimax.com (2026) da para la cerveza de barril, sin desglose español por tipo de bebida.

El IVA por canal también entra en esta cuenta: la misma botella tributa distinto según cómo sale del local. En sala, con servicio de hostelería, el consumo completo va al 10 %, alcohol incluido, porque es servicio y no entrega de bienes; sin ese servicio, la bebida alcohólica queda fuera del tipo reducido y pasa al 21 %. Las columnas de precio con IVA de la hoja resuelven solas esa distinción, según el canal.

### Destilados y cócteles: cuando el coste está en la mezcla

Un cóctel se cuesta igual que cualquier plato de la carta: es una ficha de escandallo en miniatura, ingrediente a ingrediente, con su merma y su ratio de venta. La mezcla suele pesar más de lo que el equipo cree, porque un licor de autor, un amargo de importación o una guarnición trabajada empujan el coste por encima de lo que sugiere la botella base. Los destilados puros se mueven en un beverage cost ponderado del 21,6 % y los cócteles montados en el 19,7 %, ambos por debajo del objetivo del 20 % y dentro de la horquilla del 15 % al 22 % que la misma fuente de getbackbar.com y purimax.com (2026) da para espirituosos y cócteles.

La lectura de conjunto queda en el resumen de la bodega. Sobre unas ventas totales de 43.657 € y un coste de 11.503,96 €, el beverage cost ponderado de toda la bodega se sitúa en el 26,4 %, con un margen de contribución de 32.153,04 €. Cada categoría conserva su propio objetivo, editable en la hoja, y el margen que se recuperaría si vinos, cervezas y refrescos, y destilados y cócteles llegasen cada uno al suyo asciende a 646,38 €. Ese número es el orden de prioridades: con el 30,2 % de los vinos y el 20,9 % de destilados y cócteles ya cerca de su objetivo, la categoría que más margen deja sobre la mesa es cervezas y refrescos, con su 25,4 % frente al 22 % marcado en los parámetros; ahí conviene mirar primero el tiraje, la limpieza de líneas y el tamaño de cada ración servida.

### El resumen de la bodega y el margen que estás dejando en la mesa

El primer dato va contra lo que se da por sentado: la bebida no siempre deja mejor margen que la comida. Según el informe «Consumos y beneficios de un restaurante» de CaixaBankLab y la Fundación elBulli (2026), el restaurante medio español destina el 28 % de sus ingresos de comida a comprarla, y el 34,5 % de sus ingresos de bebida a comprarla, sobre un mix de ingresos del 70 % comida y el 30 % bebida: proporcionalmente, la bodega pesa más sobre sí misma que la cocina sobre sí misma. Es un matiz, no una regla fija: depende de qué compone tu carta de vinos y licores. Por eso la bodega necesita su propio cuadro de mando, separado del food cost general.

La primera decisión que mueve la aguja es copa contra botella. Vender por copa mejora el porcentaje, pero el margen sólo se sostiene si el número real de copas por botella coincide con el calculado. Con 530 botellas de vino vendidas al mes y 2.540 copas en el mismo periodo, el tinto de la casa deja un coste por copa de 0,78 € y un margen de 2,22 €, con un beverage cost del 28,7 % en botella que baja al 26,0 % por copa. Si el servicio escancia de más, ese 26,0 % sube sin que nadie lo note hasta que el resumen lo enseña.

El barril tiene su propia trampa: se compra en litros y se vende en centilitros, con espuma que no se cobra y líneas que hay que limpiar entre medias. Con 6.360 servicios de cerveza y refrescos vendidos al mes, el objetivo de la categoría es del 22 % y el ponderado real se queda en el 25,4 %; esa diferencia es la merma que el cálculo del barril tiene que absorber. Como referencia de mercado, no como cifra española, el agregado sectorial de getbackbar.com y purimax.com (2026) sitúa el beverage cost objetivo entre el 20 % y el 26 % en barril, entre el 24 % y el 28 % en botella o lata, y entre el 15 % y el 22 % en espirituosos y cócteles, con una media general del 20 %. En España, qamarero.com (2026) da una horquilla del 15 % al 25 % para bebidas estándar, con un caso concreto del 27,5 % mensual; fuentes de fiabilidad media, para contrastar, nunca como objetivo cerrado.

El cóctel se cuesta como una ficha de escandallo en miniatura: cada licor, jarabe, fruta y hielo entran en la cuenta, y la mezcla suele pesar más de lo que parece a primera vista. El objetivo de destilados y cócteles es del 20 %; el ponderado de los combinados queda en el 21,6 % y el de los cócteles trabajados en el 19,7 %, cifras que conviene leer por separado porque el combinado sencillo y el cóctel de autor no se comportan igual.

El resumen de bodega junta las tres categorías: los vinos pesan el 41,6 % de las ventas con un ponderado del 30,2 % sobre un objetivo del 30 %; cervezas y refrescos pesan el 35,6 % con un ponderado del 25,4 % sobre un objetivo del 22 %; destilados y cócteles cierran con un ponderado del 20,9 % sobre un objetivo del 20 %. Sobre unas ventas de 43.657 € y un coste de 11.503,96 €, el beverage cost ponderado del conjunto es del 26,4 % y el margen de contribución total llega a 32.153,04 €. El libro calcula cuánto se recuperaría si cada categoría llegase a su propio objetivo: 646,38 €, el orden de prioridades para la próxima carta de vinos y la próxima compra de barril.

Falta el IVA, que también distingue canal dentro de la bodega. La misma botella tributa al tipo reducido del 10 %, alcohol incluido, cuando se sirve en sala, por ser un servicio de hostelería y no una entrega de bienes (Ley 37/1992, art. 91.Uno.2.2.º); si el cliente se la lleva sin consumirla, la operación pasa a entrega de bienes, la bebida alcohólica queda excluida del tipo reducido y tributa al tipo general del 21 % (Ley 37/1992, arts. 90 y 91.Uno.1.1.º, con criterio de la Dirección General de Tributos). Las columnas de precio con IVA de la hoja ya resuelven las dos situaciones: sólo hay que mirar la del canal por el que sale la botella.

**La bodega por categorías, con su objetivo al lado (carta-de-bebidas-beverage-cost.xlsx, hoja «Resumen Bodega»)**

| Categoría | Ventas del mes (€) | Coste del mes (€) | Beverage cost ponderado (%) | Objetivo (%) | Margen de contribución (€) | Peso sobre las ventas de bodega (%) |
|---|---|---|---|---|---|---|
| Vinos | 18.151 € | 5.473,90 € | 30,2 % | 30,0 % | 12.677,10 € | 41,6 % |
| Cervezas y refrescos | 15.554 € | 3.947,20 € | 25,4 % | 22,0 % | 11.606,80 € | 35,6 % |
| Destilados y cócteles | 9.952 € | 2.082,86 € | 20,9 % | 20,0 % | 7.869,14 € | 22,8 % |
| TOTAL BODEGA | 43.657 € | 11.503,96 € | 26,4 % |  | 32.153,04 € | 100,0 % |

*Los objetivos por categoría son celdas editables sembradas con las referencias del sector: no son un estándar, son un punto de partida para que escribas el tuyo.*

**Vinos: la misma botella por botella y por copa (carta-de-bebidas-beverage-cost.xlsx, hoja «Vinos»)**

| Vino | Compra de la botella sin IVA (€) | Copas por botella | PVP botella sin IVA (€) | PVP copa sin IVA (€) | Coste por copa (€) | Beverage cost botella (%) | Beverage cost copa (%) |
|---|---|---|---|---|---|---|---|
| Tinto de la casa (Tempranillo joven) | 3,90 € | 5,0 | 13,60 € | 3,00 € | 0,78 € | 28,7 % | 26,0 % |
| Crianza Rioja | 6,10 € | 5,0 | 19,10 € | 4,10 € | 1,22 € | 31,9 % | 29,8 % |
| Ribera del Duero roble | 7,40 € | 5,0 | 21,80 € | 4,50 € | 1,48 € | 33,9 % | 32,9 % |
| Verdejo Rueda | 4,20 € | 5,0 | 14,50 € | 3,20 € | 0,84 € | 29,0 % | 26,2 % |
| Albariño Rías Baixas | 7,90 € | 5,0 | 22,70 € | 4,80 € | 1,58 € | 34,8 % | 32,9 % |
| Cava brut nature | 5,60 € | 5,0 | 18,20 € | 3,90 € | 1,12 € | 30,8 % | 28,7 % |
| Rosado Navarra | 3,70 € | 5,0 | 12,70 € | 2,90 € | 0,74 € | 29,1 % | 25,5 % |
| Vino dulce Pedro Ximénez | 11,50 € | 8,0 | 27,30 € | 4,00 € | 1,44 € | 42,1 % | 35,9 % |

**Cervezas y refrescos: del formato de compra al servicio (carta-de-bebidas-beverage-cost.xlsx, hoja «Cervezas y Refrescos»)**

| Referencia | Formato de compra | Precio de compra sin IVA (€) | Servicios por unidad | Coste por servicio (€) | PVP en sala sin IVA (€) | Beverage cost (%) |
|---|---|---|---|---|---|---|
| Cerveza de barril (30 L) | barril | 78,00 € | 120,0 | 0,65 € | 2,30 € | 28,3 % |
| Cerveza de barril (30 L) | barril | 78,00 € | 60,0 | 1,30 € | 4,10 € | 31,7 % |
| Cerveza tercio (33 cl) | botella | 0,62 € | 1,0 | 0,62 € | 2,50 € | 24,8 % |
| Cerveza sin alcohol (33 cl) | botella | 0,58 € | 1,0 | 0,58 € | 2,40 € | 24,2 % |
| Refresco de cola (lata 33 cl) | lata | 0,55 € | 1,0 | 0,55 € | 2,30 € | 23,9 % |
| Agua mineral (50 cl) | botella | 0,28 € | 1,0 | 0,28 € | 1,80 € | 15,6 % |
| Zumo de naranja natural | kg naranjas | 1,40 € | 4,0 | 0,35 € | 3,20 € | 10,9 % |


---

## 17. Costeo por Lote en Obrador y Pastelería

### La unidad de costeo es la tanda, no la pieza

En un obrador no se escandalla la pieza suelta: se escandalla la hornada, la cuba de fermentación o el lote completo, y el coste (costo) de cada pieza sale de dividir ese total entre las unidades BUENAS que efectivamente salen, no entre las que la fórmula prometía sobre el papel. Es el mismo principio del rendimiento de despiece del capítulo 5, trasladado del cuchillo al horno: se pesa la masa cargada y se cuentan las piezas que superan el control de calidad al salir. Toda tanda tiene un rendimiento propio —piezas rotas, deformadas, quemadas en el borde del horno o fermentadas de más— y ese rendimiento de tanda convierte un coste de fórmula en un coste real por unidad vendible.

La merma no es un solo número: hay merma de fermentación, cuando la masa pierde volumen o se pasa antes de entrar al horno, y merma de cocción, cuando el producto pierde peso y, con las piezas descartadas, también unidades enteras. El libro de rendimiento resuelve esto pesando antes y después de cada fase, y ya trae registradas 5 pruebas de cocción con ese método. El rendimiento medio ponderado de esas cinco pruebas es del 72,7 %, con una pérdida media por cocción del 27,3 % —y la palabra «ponderado» importa, porque no todos los productos pierden igual: el solomillo a la plancha se deja un 22,0 %, el pollo de corral al horno un 28,0 % (con el kilo ya cocinado costando 7,50 €) y las verduras asadas hasta un 31,0 %, como se ve en el cuadro siguiente. Son pruebas de cocina, no de obrador, pero el método es el que hay que aplicar a la bollería y a la pastelería: báscula antes de meter la bandeja, báscula al sacarla y contaje de piezas aptas frente a piezas de fórmula. Sin esa prueba propia por producto, cualquier coste de tanda es una suposición optimista.

En cuanto el producto se vende envasado —caja, film, bolsa con etiqueta de alérgenos y fecha de consumo preferente—, el packaging deja de ser un gasto de pedido y pasa a ser coste por pieza: cada unidad que sale de la tanda carga su propio envase y su propia etiqueta, dentro del escandallo (costeo de recetas) de la pieza, nunca en una partida aparte de «suministros».

### Mano de obra por hora dentro del coste del lote

En una pieza de bollería o de pastelería el coste de las manos suele pesar más que el coste de la harina, la mantequilla o el relleno, y por eso el escandallo que sólo mira el ingrediente da un precio ruinoso: le falta la parte más cara de la pieza. El cálculo correcto reparte el tiempo real de la tanda —amasado, formado, fermentación vigilada, horneado, enfriado y envasado— entre las piezas buenas que salen de ella, igual que ya se reparte el coste de la materia prima. El dato de coste por hora de cada puesto de trabajo lo pone la propia empresa, con su convenio y sus cargas sociales: no hay una cifra universal que sirva para todos los obradores. Como referencia de cuánto puede llegar a pesar la plantilla sobre la venta, el coste de personal se mueve entre el 30 % y el 35 % de la venta neta en un servicio integrado en mesa, y entre el 15 % y el 25 % en un servicio parcial de autoservicio o barra (CaixaBankLab × Fundación elBulli, 2026); un obrador con venta de mostrador suele acercarse más a esa segunda horquilla, aunque cada negocio tiene que medir la suya.

El escalado de la tanda es donde este coste se convierte en palanca: doblar la fórmula no dobla el tiempo de amasado ni el de vigilancia de la fermentación, y tampoco dobla la merma, así que el coste de mano de obra por pieza baja según crece el tamaño del lote, hasta que la capacidad del horno, de la cámara o de la mesa de trabajo pone el techo. Encontrar ese punto óptimo es decidir cuánta plantilla y cuánto tiempo hacen falta para el volumen que de verdad se vende, no para el que cabe en el horno.

Para poner precio a la pieza ya costeada, este formato encaja mejor con el método del margen objetivo que con un simple multiplicador sobre coste: se fija primero cuánto tiene que dejar cada pieza y se calcula el precio de venta desde ahí. De los 6 platos que ya usan este método en el pack, entre los distintos formatos de carta (menú), el margen de contribución medio es de 8,01 €, con un food cost conjunto del 36,7 %; el cuadro siguiente muestra cómo se llega a esa cifra. Quien quiera la plantilla de costeo por lote ya montada la tiene lista en el Kit de Escandallos: aquí queda el método.

### Packaging y etiquetado: el coste que no está en la receta

En obrador no se escandalla la ración: se escandalla la tanda entera, y el coste de cada pieza sale de dividir ese total entre las piezas buenas que llegan al mostrador, nunca entre las que la fórmula prometía sobre el papel. Es el mismo principio que el rendimiento de despiece del capítulo 5, trasladado del cuchillo al horno y a la cámara de fermentación: primero se pesa lo que entra, después se cuenta lo que de verdad se puede vender, y sólo con ese segundo número se calcula el coste.

Aquí, además, la mano de obra pesa en el escandallo como no siempre pesa en cocina de plato. Una pieza de bollería puede llevar más euros de manos —amasado, boleado, laminado, formado, decorado— que de harina, mantequilla o relleno, y un escandallo que sólo mira el ingrediente da un precio ruinoso. En el conjunto del negocio, el coste de personal sobre la venta neta se mueve entre el 30-35 % en el servicio integrado en mesa y el 15-25 % en el servicio parcial —autoservicio o barra— (CaixaBankLab × Fundación elBulli — Consumos y beneficios de un restaurante, 2026); en obrador ese peso no se diluye en el ticket medio de una sala, se concentra pieza a pieza, y por eso el minutaje de cada fórmula tiene que figurar en la ficha con el mismo rigor que el gramaje.

La merma de cocción y la de fermentación son la otra mitad del rendimiento de tanda, y se miden igual: pesando antes y después. El libro de rendimiento recoge esa lógica con cinco pruebas de cocción registradas, con un rendimiento medio ponderado del 72,7 % —pérdida media del 27,3 %— que va desde el 22,0 % del solomillo a la plancha hasta el 31,0 % de las verduras asadas, pasando por el 28,0 % del pollo de corral al horno, con un coste ya cocinado de 7,50 € el kilo. Son pruebas de cocina, no de obrador, y aquí sólo ilustran el método: cada fórmula, cada horno y cada obrador tienen su propio rendimiento, que hay que registrar con la báscula propia. La merma de fermentación se pesa igual —lo que se pierde de humedad en el primer y el segundo levado, y lo que se vuelve a perder dentro del horno— y entra en el coste de la tanda como la merma de cocción.

Y en cuanto la pieza sale envasada —film, bolsa, caja individual, con la etiqueta de alérgenos y la fecha de consumo preferente—, el packaging deja de ser un gasto del pedido de compra y pasa a ser coste de la pieza: se compra por lote grande, se reparte por unidad, y esa unidad se suma en la ficha antes de fijar el precio de venta, no después.

### Escalar una fórmula sin escalar el error

Doblar una fórmula parece aritmética simple —el doble de harina, el doble de mantequilla, el doble de piezas—, pero el tiempo de manos no se dobla igual: amasar dos kilos no lleva el doble de minutos que amasar uno, y una hornada de más piezas reparte el mismo tiempo de horno, fermentación y formado entre más unidades. Por eso el coste por pieza baja con el tamaño de tanda, hasta que un límite físico —la capacidad del horno, el espacio de la cámara, las bandejas que entran en un carro— obliga a partir en dos hornadas, y ahí se acaba el ahorro. Ese límite lo decide el horno y la cámara propios, nunca los de un libro.

La merma tampoco escala en línea recta: una tanda grande suele sostener mejor la temperatura y fermentar de forma más uniforme que una prueba pequeña, así que el rendimiento a escala real de producción no coincide con el de la prueba hecha para montar el escandallo sobre el papel, y es el primero el que hay que registrar para que el coste unitario no se quede corto frente a lo que marca la báscula cada mañana.

Para poner precio a cada pieza, el método que encaja con este formato es el del margen objetivo: en vez de partir del coste y sumarle un porcentaje, se parte del margen de contribución que necesita esa pieza para sostener la tanda y el negocio, y desde ahí se despeja el precio de venta. El libro aplica ese método a seis platos, con un margen de contribución medio de 8,01 € por plato y un food cost del conjunto de la carta del 36,7 %; son platos de sala, no piezas de obrador, pero el cuadro siguiente ilustra el mismo mecanismo que se aplica pieza a pieza en costeo por tanda: se parte del margen que necesita el negocio, no de la costumbre del oficio.

Para el negocio que quiera la plantilla de costeo por lote ya montada —con la báscula de la tanda, el minutaje y el packaging enlazados en una sola ficha— está en el Kit de Escandallos; lo que queda aquí es el método, que es lo necesario para adaptar cualquier plantilla al obrador propio.

**Lo que pierde el producto en el horno y en la plancha (rendimiento-mermas-producto.xlsx, hoja «Merma de Cocción»)**

| Elaboración | Técnica | Peso crudo (kg) | Peso cocinado (kg) | Pérdida por cocción (%) | Factor de cocción | Coste/kg crudo (€) | Coste/kg cocinado (€) |
|---|---|---|---|---|---|---|---|
| Solomillo de cerdo a la plancha | Plancha | 0,25 | 0,20 | 22,0 % | 1,28 | 17,95 € | 23,01 € |
| Pollo de corral al horno | Horno | 1,50 | 1,08 | 28,0 % | 1,39 | 5,40 € | 7,50 € |
| Bacalao confitado | Confitado | 0,20 | 0,18 | 12,0 % | 1,14 | 14,90 € | 16,93 € |
| Secreto ibérico a la brasa | Brasa | 0,30 | 0,22 | 26,0 % | 1,35 | 16,50 € | 22,30 € |
| Verduras asadas | Horno | 1,00 | 0,69 | 31,0 % | 1,45 | 2,20 € | 3,19 € |

*El factor de cocción se multiplica por el coste del producto crudo: es lo que convierte el precio del albarán en el coste de lo que sale del horno.*

**Poner precio por margen objetivo, que es el método del obrador (precio-objetivo-multi-metodo.xlsx, hoja «Por Plato»)**

| Plato | Coste/ración (€) | Margen objetivo (€) | B · PVP por margen (€) | FC resultante con B (%) |
|---|---|---|---|---|
| Croquetas de jamón ibérico (6 ud) | 2,10 € | 6,50 € | 8,60 € | 24,4 % |
| Ensalada de tomate rosa, ventresca y cebolleta | 3,60 € | 6,50 € | 10,10 € | 35,6 % |
| Gambas al ajillo | 6,90 € | 6,50 € | 13,40 € | 51,5 % |
| Huevos rotos con patatas y chistorra | 2,40 € | 6,50 € | 8,90 € | 27,0 % |
| Tabla de quesos de la zona | 5,20 € | 6,50 € | 11,70 € | 44,4 % |
| Alcachofas confitadas con jamón | 3,10 € | 6,50 € | 9,60 € | 32,3 % |
| Sopa de tomate asado con albahaca | 1,20 € | 6,50 € | 7,70 € | 15,6 % |
| Solomillo de cerdo ibérico con puré de boniato | 5,67 € | 10,50 € | 16,17 € | 35,1 % |
| Bacalao confitado al pil-pil | 7,40 € | 10,50 € | 17,90 € | 41,3 % |
| Hamburguesa de vaca madurada con patatas | 4,30 € | 10,50 € | 14,80 € | 29,1 % |
| Arroz meloso de secreto ibérico y setas | 6,20 € | 10,50 € | 16,70 € | 37,1 % |
| Chuletón de vaca madurada (500 g) | 14,80 € | 10,50 € | 25,30 € | 58,5 % |
| Lubina a la sal | 8,90 € | 10,50 € | 19,40 € | 45,9 % |
| Pollo de corral asado con patatas | 3,70 € | 10,50 € | 14,20 € | 26,1 % |
| Lasaña de verduras de temporada | 2,60 € | 10,50 € | 13,10 € | 19,8 % |
| Tataki de atún rojo con sésamo | 9,60 € | 10,50 € | 20,10 € | 47,8 % |
| Tarta de queso cremosa | 1,30 € | 4,20 € | 5,50 € | 23,6 % |
| Torrija caramelizada con helado | 1,10 € | 4,20 € | 5,30 € | 20,8 % |
| Coulant de chocolate | 1,60 € | 4,20 € | 5,80 € | 27,6 % |
| Fruta de temporada preparada | 1,40 € | 4,20 € | 5,60 € | 25,0 % |


---

## 18. Cuando Sube el Proveedor: Protocolo de Re-escandallado

### Los cuatro disparadores de un re-escandallado

El re-escandallado no depende de la memoria de nadie: hay cuatro situaciones que lo activan, y conviene tenerlas escritas en algún sitio visible de cocina.

- Una subida de proveedor por encima del umbral que tú mismo fijes sobre el coste (costo) de esa referencia; por debajo de ese umbral se deja pasar sin tocar nada.
- Un cambio de formato o de calibre del producto que compras, aunque el precio por unidad de compra no se mueva: el coste real por ración sí lo hace, y ahí se esconde el desajuste que nadie ve en la factura.
- Un cambio de receta, venga de cocina o de un ajuste del proveedor en la composición del producto.
- El vencimiento del calendario, aunque no haya pasado nada de lo anterior: revisar por fecha es la red que atrapa lo que los otros tres disparadores no ven venir.

Ninguno de los cuatro obliga a revisar la carta (menú) entera. Aplica la regla del 80/20: se revisan las referencias que más pesan en el consumo del mes —las que más kilos o litros mueven, no las que más veces aparecen escritas— y los platos que más se venden, porque amplifican cualquier error de coste antes que ningún otro. De los 20 platos con precio calculado en la tabla de referencia del pack, 11 quedan dentro del objetivo y 9 por encima; el 80/20 dice que esos 9 son el primer sitio donde mirar, y que los otros 11 pueden esperar al siguiente repaso.

Para saber si una subida cruza tu umbral, hay dos sitios donde consultar antes de fiarte de la sensación que deja una factura suelta. Para el comportamiento general de los alimentos, el Instituto Nacional de Estadística publica periódicamente su nota de prensa del Índice de Precios de Consumo, con el desglose propio de la rúbrica de alimentos y bebidas no alcohólicas: se consulta para distinguir si lo que sube es un movimiento generalizado del mercado o algo propio de ese proveedor. Para el fresco, el Ministerio de Agricultura, Pesca y Alimentación mantiene, dentro de su Observatorio de la Cadena Alimentaria, un sistema de precios origen-mayorista con seguimiento sobre 34 productos frescos vía Mercasa (MAPA — Observatorio de la Cadena Alimentaria, sistema de precios origen-mayorista, 2026): ahí se pregunta en qué eslabón de la cadena nace la subida, y si el precio de origen ya la refleja o si el margen se añade más adelante. Ninguno de los dos dice cuánto hay que subir la carta; los dos dicen si la subida es real y en qué punto de la cadena se ha producido.

### El calendario: qué se revisa cada mes y qué cada trimestre

El repaso mensual se ocupa de lo urgente: las referencias que dispararon el umbral ese mes, los platos con la desviación más señalada en la tabla de precio objetivo, y el seguimiento de las decisiones de negociación en marcha. El plan a 90 días recoge 2 decisiones de negociación registradas, con un impacto estimado de 300 €, dentro de un impacto total estimado del plan de 2.360 € (la hoja «Decisiones» de plan-accion-90-dias.xlsx); revisarlas cada mes es comprobar si el proveedor cumplió lo pactado, no reabrir la negociación entera cada vez.

El repaso trimestral es donde se mide la carta completa contra el objetivo, plato por plato. La diferencia total con los precios de venta actuales, -13,54 €, y la subida media sobre el precio de venta actual, -5,1 %, de la tabla de precio objetivo, dan la fotografía completa de los 20 platos, no sólo la de los que ya sabías que estaban descolgados.

Cómo se traslada la subida: no se sube toda la carta el mismo día ni el mismo porcentaje. Se sube donde el mercado deja —un plato de entrada admite un movimiento que el plato ancla de la carta no admite igual— y se aprovecha el cambio de carta o de temporada para que el nuevo precio llegue dentro de «la carta nueva» y no como «la subida». Se revisan primero los platos cuya subida es pequeña en euros aunque sea grande en porcentaje: son los que menos protesta generan en sala, así que es donde conviene actuar primero. La ficha de referencia del pack, por ejemplo, necesita una subida del 9,3 % para llegar a su precio de venta objetivo, con una diferencia de apenas 1,60 € entre el objetivo y el actual (la hoja «Ficha» de ficha-escandallo-base.xlsx): en euros es un ajuste pequeño, y es justo el tipo de plato que se sube primero y sin que se note en sala. Las croquetas, en la tabla de precio objetivo, aparecen en cambio con una diferencia de -1,60 € frente a su precio de venta actual: el signo contrario avisa de que no todos los ajustes van en la misma dirección, y es la tabla la que lo dice, nunca la intuición del cocinero.

Después de mover cualquier precio, la matriz de rentabilidad de la carta deja de valer hasta que se vuelve a medir: cambiar precios cambia el mix de ventas, así que sacar conclusiones sobre qué plato retirar o potenciar con datos de antes de la subida es medir con la regla que ya no corresponde. Se espera al cierre siguiente, se recalcula la matriz entera, y sólo entonces se decide qué plato se queda, cuál se retoca otra vez y cuál sale de la carta.

### Dónde mirar el precio de la materia prima

Hay cuatro momentos que obligan a re-escandallar, y ninguno depende de la memoria:

- una subida del proveedor por encima del umbral que tú mismo hayas fijado como línea roja;
- un cambio de formato o de calibre en el género que compras, aunque la referencia parezca la misma;
- un cambio en la receta, por sustitución de ingrediente o por ajuste de ración;
- el vencimiento del calendario de revisión, aunque en apariencia no haya pasado nada.

Este último es el que más se salta: si el proveedor no avisa, se asume que todo sigue igual, y ahí es donde el escandallo (costeo de recetas) se desvía en silencio.

Cuando toca revisar, no se abre la carta (menú) entera: se aplica la regla del 80/20, repasando primero las referencias que más pesan en el consumo del mes —no las que más aparecen en la carta, sino las que más kilos o litros mueves— y los platos más vendidos, porque arrastran el resultado aunque su desviación individual sea pequeña. El cuadro que sigue a este texto, con los platos que tienen precio recalculado en este ciclo, es ese recorte: no la carta completa, sino la parte que concentra el impacto. Son 20 platos; de ellos, 11 quedan dentro del objetivo y 9 por encima, con una diferencia conjunta frente a los precios de venta actuales de -13,54 € y una subida media del -5,1 % sobre el precio de venta actual del conjunto revisado: la fotografía del bloque completo, que sirve para decidir por dónde entrar primero.

Antes de descolgar el teléfono hay dos sitios donde mirar si la subida responde al mercado o solo a que el proveedor puede. El primero es la nota de prensa del Índice de Precios de Consumo del Instituto Nacional de Estadística, en su rúbrica de Alimentos y bebidas no alcohólicas: recoge el comportamiento general de la cesta de alimentación, mes a mes, y sirve para contrastar si la subida de un proveedor va en línea con el sector o se sale de lo razonable. El segundo, para el género fresco, es el sistema de precios origen-mayorista del Ministerio de Agricultura, Pesca y Alimentación, con seguimiento a 34 productos frescos a través de Mercasa (MAPA — Observatorio de la Cadena Alimentaria, sistema de precios origen-mayorista, 2026): compara el precio de origen con el del mercado mayorista y pregunta si el margen de cada eslabón se ha ensanchado. Ninguno de los dos se cita aquí por lo que marque hoy —eso cambia cada semana—, sino como el sitio al que volver cuando llegue la próxima subida.

### Cómo se sube un precio sin que se note en la caja

Subir toda la carta a la vez, y al mismo porcentaje, es la manera más rápida de que el cliente lo note. La subida se reparte: se sube donde el mercado lo permite —los platos sin referencia clara de precio en la cabeza del cliente— y se aprovecha un cambio de carta o de temporada para rediseñar la ficha o la guarnición, de modo que el precio nuevo no se lea como una subida desnuda. La ficha de escandallo de este capítulo es el ejemplo: la subida necesaria calculada es del 9,3 %, que en euros son solo 1,60 € de diferencia entre el precio de venta objetivo y el actual. Es el tipo de ajuste que conviene revisar primero: pequeño en euros, así que el cliente apenas lo nota; grande en porcentaje, así que corrige el margen de verdad. La misma magnitud aparece desde el otro lado en el cuadro de por plato: la diferencia de las croquetas con su precio de venta actual es de -1,60 €, el reverso exacto del mismo ajuste.

No todos los ajustes salen de subir el precio en carta. Parte de las decisiones del plan de acción a 90 días son de negociación con el proveedor, no de precio de venta: hay 2 decisiones de este tipo registradas, con un impacto estimado de 300 € sobre un impacto total de 2.360 € para el conjunto del plan. Cuándo sentarse a negociar y con qué dato en la mano ya está desarrollado en el bono del Kit de Escandallos que tienes en el mismo pack; aquí basta con tener claro que subir el precio de venta y negociar el coste (costo) de la materia prima son palancas distintas, y conviene mirar las dos antes de decidir cuál tocar primero.

Y una advertencia que no se puede saltar: en cuanto se toca un precio, se mueve el mix de ventas. El plato que antes se pedía mucho porque salía barato al lado de los de la misma página puede perder peso, y otro que apenas se pedía puede ganarlo. Por eso, después de aplicar cualquier subida hay que dejar pasar tiempo antes de volver a medir —no dar por buena ninguna conclusión sobre un plato con los datos de antes del cambio—, porque la matriz que decide qué se promociona y qué se retira de la carta se construye con ventas reales, y esas tardan en asentarse tras un precio nuevo.

**Qué plato hay que tocar y cuánto (precio-objetivo-multi-metodo.xlsx, hoja «Por Plato»)**

| Plato | Coste/ración (€) | PVP actual sin IVA (€) | PVP elegido sin IVA (€) | Diferencia (€) | Semáforo vs objetivo |
|---|---|---|---|---|---|
| Croquetas de jamón ibérico (6 ud) | 2,10 € | 8,60 € | 7,00 € | -1,60 € | Dentro del objetivo |
| Ensalada de tomate rosa, ventresca y cebolleta | 3,60 € | 11,80 € | 12,00 € | 0,20 € | Dentro del objetivo |
| Gambas al ajillo | 6,90 € | 15,50 € | 13,40 € | -2,10 € | Por encima del objetivo |
| Huevos rotos con patatas y chistorra | 2,40 € | 9,80 € | 8,00 € | -1,80 € | Dentro del objetivo |
| Tabla de quesos de la zona | 5,20 € | 13,60 € | 17,33 € | 3,73 € | Dentro del objetivo |
| Alcachofas confitadas con jamón | 3,10 € | 10,90 € | 10,33 € | -0,57 € | Dentro del objetivo |
| Sopa de tomate asado con albahaca | 1,20 € | 7,20 € | 7,56 € | 0,36 € | Dentro del objetivo |
| Solomillo de cerdo ibérico con puré de boniato | 5,67 € | 17,30 € | 18,68 € | 1,38 € | Por encima del objetivo |
| Bacalao confitado al pil-pil | 7,40 € | 19,10 € | 17,90 € | -1,20 € | Por encima del objetivo |
| Hamburguesa de vaca madurada con patatas | 4,30 € | 13,60 € | 12,92 € | -0,68 € | Por encima del objetivo |
| Arroz meloso de secreto ibérico y setas | 6,20 € | 16,40 € | 16,70 € | 0,30 € | Por encima del objetivo |
| Chuletón de vaca madurada (500 g) | 14,80 € | 32,70 € | 25,30 € | -7,40 € | Por encima del objetivo |
| Lubina a la sal | 8,90 € | 21,80 € | 19,40 € | -2,40 € | Por encima del objetivo |
| Pollo de corral asado con patatas | 3,70 € | 12,70 € | 11,94 € | -0,76 € | Por encima del objetivo |
| Lasaña de verduras de temporada | 2,60 € | 11,40 € | 10,49 € | -0,91 € | Dentro del objetivo |
| Tataki de atún rojo con sésamo | 9,60 € | 22,40 € | 20,10 € | -2,30 € | Por encima del objetivo |
| Tarta de queso cremosa | 1,30 € | 5,90 € | 6,61 € | 0,71 € | Dentro del objetivo |
| Torrija caramelizada con helado | 1,10 € | 5,50 € | 5,83 € | 0,33 € | Dentro del objetivo |
| Coulant de chocolate | 1,60 € | 6,20 € | 7,13 € | 0,93 € | Dentro del objetivo |
| Fruta de temporada preparada | 1,40 € | 4,50 € | 4,73 € | 0,23 € | Dentro del objetivo |

*La columna de la diferencia es la que ordena el trabajo: se empieza por los platos cuya corrección es mayor en euros y se vende mucho, no por los que tienen el porcentaje más feo.*

**Las decisiones del plan, por tipo (plan-accion-90-dias.xlsx, hoja «Decisiones»)**

| Decisión | Decisiones | Impacto estimado (€/mes) | Impacto conseguido (€/mes) |
|---|---|---|---|
| Reformular | 1 | 900,00 € | 0,00 € |
| Resubir | 1 | 210,00 € | 0,00 € |
| Rediseñar | 2 | 400,00 € | 0,00 € |
| Retirar | 3 | 290,00 € | 0,00 € |
| Revisar | 2 | 300,00 € | 0,00 € |
| Negociar | 1 | 260,00 € | 0,00 € |


---

## 19. Caso Integral: una Carta Entera, de Principio a Fin

### El punto de partida: qué había sobre la mesa

Antes de entrar en el detalle, conviene dejarlo dicho sin rodeos: lo que sigue es un caso modelado, construido enteramente sobre las plantillas del pack para que el lector vea el flujo completo encadenado antes de aplicarlo a su propia carta (menú). No corresponde a un restaurante real ni a un negocio identificable; los datos que aparecen a partir de aquí, y en las tablas que acompañan este capítulo, son los que arroja el propio ejercicio.

La carta de partida tenía 20 platos dados de alta, con 4.870 unidades vendidas al mes y unas ventas netas de 59.029 € en ese mismo periodo. El food cost medio ponderado de esa carta era del 32,7 %, con un margen de contribución medio ponderado de 8,16 € por ración. Para situar esa cifra: el food cost medio del sector hostelero español, entendido como el consumo de producto sobre la venta, se mueve en un rango sano del 25 al 35 % sobre venta, con una media de mercado en torno al 30 % (CaixaBankLab × Fundación elBulli — Consumos y beneficios de un restaurante, 2026). El 32,7 % de partida quedaba, por tanto, dentro de ese rango pero en su mitad alta, con recorrido de mejora sin necesitar una reestructuración de la carta.

Ese food cost no vive solo: convive con el personal, el alquiler y los gastos generales dentro de la cuenta de explotación, y el EBITDA sano de referencia para ese conjunto se sitúa en el 10-13 % sobre venta (misma fuente). El caso no toca esas otras partidas —quedan fuera del alcance de este capítulo—, pero conviene tenerlas presentes porque son el marco en el que se lee cualquier decisión sobre precios.

Con ese punto de partida sobre la mesa, el recorrido por las herramientas del pack empieza donde tiene que empezar: en la ficha técnica de cada plato.

### Paso 1: escandallar y medir la merma

El primer plato que se llevó a la ficha de escandallo (costeo de recetas), en ficha-escandallo-base.xlsx, dio un coste (costo) por ración de 5,67 €. Con ese coste, la herramienta propuso un precio de venta objetivo, sin IVA, de 18,90 €, calculado para sostener el margen de contribución que la carta necesita. La decisión en este paso no fue aceptar el coste tal cual: fue revisar, ración a ración, si ese coste recogía la merma real del producto o si se había quedado en el peso de compra.

Ahí entró la segunda herramienta. Los tests de rendimiento sobre las materias primas de la carta, recogidos en rendimiento-mermas-producto.xlsx, dieron un rendimiento medio ponderado del 60,5 %, es decir, que una parte considerable de cada kilo comprado se pierde entre limpieza, desperdicio de corte y merma de cocción antes de llegar al plato. La decisión que se tomó con ese dato fue trasladar el rendimiento medido a la ficha de cada producto, en lugar de dejar el coste calculado sobre el peso bruto de la factura del proveedor: es la diferencia entre un escandallo que parece cuadrar en el papel y uno que cuadra en cocina, plato a plato. Con el rendimiento ya incorporado, el coste por ración dejó de ser una estimación optimista y pasó a ser el número real con el que trabajar en los pasos siguientes: la clasificación de la carta y, después, el precio.

### Paso 2: clasificar la carta con los cuatro métodos

Con los costes reales ya en la ficha, la matriz multimétodo cruzó los 20 platos de la carta por las cuatro lecturas clásicas de la ingeniería de menú. El resultado, recogido en matriz-multimetodo-carta.xlsx: solo 3 platos coincidían en la mejor categoría en las cuatro lecturas a la vez, y 12 tenían tres o cuatro lecturas discrepantes entre sí. En la lectura de Kasavana-Smith, la más usada como referencia rápida, la carta dejaba 6 platos Star y 3 Dog.

Esos 12 platos discrepantes son el motivo de ser de este paso, porque es ahí donde fiarse de una sola lectura induce a error. Hay platos que un método clasifica como estrella por su volumen de venta y que otro método degrada a la categoría más débil en cuanto se mira el margen que dejan por ración: la decisión, en esos casos, fue mantenerlos en carta pero revisar el precio antes de tocar nada más, porque el volumen ya está ganado y lo que falla es el margen. Hay otros en el extremo contrario, con un margen de contribución alto pero una venta tan escasa que ningún método los premia: ahí la decisión fue de visibilidad, no de precio —reubicarlos en la carta, en la explicación de sala o en la sugerencia del camarero, para que el margen que ya tienen encuentre más comensales—. Y hay un tercer grupo, el más incómodo, donde ni el margen ni el volumen acompañan y las cuatro lecturas apuntan en la misma dirección poco favorable: con esos no cabe ambigüedad, y son los primeros candidatos a salir de la carta o a rediseñarse desde la ficha técnica, no desde el precio. La clasificación no sustituye la decisión; la que hace falta es la que toma quien lleva la carta, plato a plato, con las cuatro lecturas delante y no con una sola.

### Paso 3: poner precio plato a plato

Antes de entrar en cifras, una aclaración necesaria: lo que sigue es un caso modelado, construido sobre las plantillas del pack para que el lector vea el flujo completo antes de aplicarlo a su propia carta. No es un cliente real ni un negocio identificable.

La carta de ejemplo tiene 20 platos dados de alta, que mueven 4.870 unidades al mes y 59.029 € de ventas netas, con un food cost medio ponderado del 32,7 % y un margen de contribución medio ponderado de 8,16 € por plato. Antes de tocar un solo precio de venta conviene mirar cada plato con los cuatro métodos a la vez, no con uno solo.

Con la lectura combinada, 3 platos coinciden en la mejor categoría en las cuatro clasificaciones y se mantienen tal cual: los cuatro métodos coinciden en que ya están donde deben estar. El caso interesante son los otros 12, con tres o cuatro lecturas fuera de su categoría ideal. Ahí la decisión no sale de promediar los cuatro resultados, sino de mirar plato por plato el margen de contribución y el coste individual junto a la rotación real. Donde el problema es un coste alto sostenido por buena rotación, la decisión fue revisar el escandallo —ración, proveedor o técnica— antes que tocar el precio de venta. Donde la rotación es floja con margen correcto, la decisión fue de colocación: cambiar de sitio en la carta o de nombre, no de coste. Y donde coinciden coste alto y rotación floja, el plato se marcó para salida o rediseño completo, porque ningún ajuste de precio arregla esa combinación por sí solo. La lectura aparte de Kasavana-Smith, la más clásica de las cuatro, sitúa 6 platos como Star y 3 como Dog, y ya adelanta buena parte de ese reparto.

Con la clasificación cerrada, toca poner precio de venta objetivo. El escandallo de ejemplo tiene un coste por ración de 5,67 € —aplicado el rendimiento medio ponderado de los tests, que en el conjunto de los productos analizados se queda en el 60,5 %— y un precio de venta objetivo, sin IVA, de 18,90 €. Repetido plato a plato, deja 11 platos de los 20 dentro del objetivo tras aplicar el nuevo precio. El food cost del conjunto de la carta con esos precios queda en el 36,7 %, y la diferencia total frente a los precios de venta actuales es de -13,54 €: la carta, sumada, pide subir más de lo que baja en ningún plato suelto.

### Paso 4: revisar el delivery y decidir exclusiones

La misma carta, servida por una aplicación de reparto, no es la misma carta. La comisión que retiene cada plataforma se suma al coste de producto y al packaging, así que el food cost efectivo de ese canal no es comparable en directo con el de la sala. Del total de 20 platos, 12 resultan viables en delivery y 8 quedan para excluir de la aplicación o para reformular. El criterio es comparar, plato a plato, el food cost efectivo contra el precio techo que el canal permite sin dejar de ganar dinero con ese pedido.

Los platos que salen de la aplicación son los que, con su coste actual y el peso añadido de comisión y envase, no llegan a ese precio techo por mucho que se suba el precio de venta. Los que suben de precio son los que sí tienen recorrido: su food cost efectivo entra en un margen manejable en cuanto se ajusta el precio del canal, sin tocar la receta ni el escandallo. El resultado agregado deja un food cost efectivo medio en delivery del 54,6 %, frente a un margen mensual total en sala de 43.635 €. La diferencia de margen del delivery frente a la sala es de -13.585 €: el canal aporta volumen y visibilidad, pero con esta carta no iguala a la sala en rentabilidad.

### Paso 5: convertir el diagnóstico en decisiones con fecha

El food cost medio del sector hostelero español se mueve en un rango sano de entre el 25 % y el 35 % sobre venta, con una media de mercado del 30 %, según CaixaBankLab y la Fundación elBulli en su informe «Consumos y beneficios de un restaurante» (2026). La misma fuente sitúa la estructura de costes de referencia de un restaurante español en torno al 30 % de producto, un 30-35 % de personal con el servicio integrado, un 5-10 % de alquiler y un 13-20 % de gastos generales —idealmente el 17 %—, con un EBITDA sano del 10-13 %; por debajo del 10 % pide reestructuración. El prime cost del año de la carta de ejemplo es del 63,4 %, por debajo del objetivo del 65 % fijado en su cuadro de mando: hay margen de maniobra, pero no tanto como para relajar el seguimiento.

Todo lo anterior —clasificación, precio de venta y delivery— desemboca en 10 decisiones registradas en el plan, cada una con responsable, semana de ejecución e impacto estimado. Ese impacto estimado suma 2.360 € en el conjunto de las 10 decisiones y 28.320 € proyectado a doce meses: cifras que hay que leer como una estimación calculada a la fecha del plan, no como un resultado ya conseguido. El plan fija quién hace qué y para cuándo; no certifica el resultado.

La lectura del trimestre, con esas diez decisiones en marcha, mueve el food cost del mes 0 desde el 33,1 % hasta un objetivo de 29,8 % en el mes 3; el prime cost, del 66,8 % al 63,8 %; y los platos en carta, de 20 a 18. Conviene leer estos tres indicadores como lo que son en el libro: un objetivo de ejemplo para enseñar cómo se sigue un plan trimestre a trimestre, no una promesa de lo que le va a pasar al lector con su propia carta. Lo replicable es el mecanismo: decisión con fecha, responsable e impacto estimado, y una hoja de seguimiento que compara cada mes contra el punto de partida.

### Qué salió de todo esto

Todo lo recorrido pertenece al caso modelado que se construye sobre las plantillas del pack: no es un restaurante real ni un negocio identificable, sino la misma carta (menú) trabajada de principio a fin con las ocho herramientas, para que el lector vea el conjunto antes de aplicarlo a la suya.

La carta de partida reúne veinte platos dados de alta, con 4.870 unidades vendidas al mes y unas ventas netas de 59.029 €; sobre ese volumen, el food cost medio ponderado de la carta queda en 32,7 % y el margen de contribución medio ponderado, en 8,16 € por plato — dentro del margen que la referencia sectorial marca como sano: el food cost medio del sector hostelero español se sitúa en el 30 % sobre venta, con un rango sano de 25-35 % (CaixaBankLab × Fundación elBulli — Consumos y beneficios de un restaurante, 2026). El escandallo (costeo de recetas) de la ficha que abre el caso deja un coste (costo) por ración de 5,67 € y un precio de venta objetivo, sin IVA, de 18,90 €, sostenido por un rendimiento medio ponderado del 60,5 % en el test de rendimiento del mismo producto.

La clasificación multimétodo es donde más se nota el criterio, porque el desacuerdo entre lecturas es la norma y no la excepción: de los veinte platos, sólo tres coinciden en la mejor categoría bajo las cuatro lecturas a la vez, y doce se quedan con tres o cuatro lecturas fuera de esa coincidencia. Con esos doce la decisión dependió de la rotación de cada plato:

- Discrepancia sobre un plato de alta rotación: se mantuvo el precio de venta y se vigiló el volumen, porque perder ventas por corregir una sola lectura sale más caro que convivir con el desacuerdo entre métodos.
- Discrepancia sobre un plato de baja rotación: se revisó la receta o se retiró, porque ahí no hay volumen que compense un food cost fuera de sitio.

La carta cerró con seis platos Star y tres Dog bajo Kasavana-Smith, y esos tres Dog concentraron buena parte de las decisiones del paso siguiente. Con el precio puesto plato por plato, once de los veinte quedaron dentro del objetivo marcado; el conjunto de la carta con esos precios elegidos deja un food cost del 36,7 % y una diferencia total de -13,54 € frente a los precios de venta actuales, la brecha entre lo que se cobra hoy y lo que la herramienta recomienda cobrar.

En el canal de reparto la carta se reparte de otra manera: doce platos son viables en la aplicación y ocho quedan para excluir o reformular, con un food cost efectivo medio en delivery del 54,6 %. La lógica es siempre la misma: cada plato lleva delante su food cost efectivo —el que ya incorpora el descuento del canal y el empaquetado— comparado con su precio techo; por debajo del techo sube de precio y sigue en la aplicación, y por encima sale, porque subirlo lo dejaría fuera de precio para el canal. El margen mensual total en sala es de 43.635 €, y la diferencia de margen del delivery frente a la sala es de -13.585 €.

La bodega, aparte, deja un beverage cost ponderado del 26,4 % y un margen de contribución total de 32.153,04 €. Y el año, tomado en conjunto, cierra con un prime cost del 63,4 %, por debajo del objetivo en vigor del 65 % que marca el cuadro de mando durante todo el caso. Para leerlo dentro de la cuenta de explotación completa, la referencia sectorial sitúa la estructura de costes de un restaurante español en 30 % de producto, 30-35 % de personal con el servicio integrado, 5-10 % de alquiler y 13-20 % de gastos generales —con el 17 % como cifra ideal—, de donde resulta un EBITDA sano del 10-13 %, con reestructuración recomendada por debajo del 10 % (CaixaBankLab × Fundación elBulli — Consumos y beneficios de un restaurante, 2026).

Todo eso desemboca en el plan de acción a 90 días: diez decisiones registradas, cada una con su responsable, su semana de ejecución y su impacto estimado en el cuadro siguiente. Conviene leerlo con esa palabra por delante, estimado: el impacto total son 2.360 € y, llevado a doce meses, 28.320 €, y la columna de conseguido del mismo cuadro se queda en cero a propósito, porque el trabajo todavía no se ha ejecutado. Es la lectura del plan en la fecha en que se cierra, no un resultado ya cobrado.

Los indicadores del trimestre, en el cuadro que sigue, muestran el punto de partida y el objetivo con el que se construyó el caso: el food cost pasa del 33,1 % en el mes cero al 29,8 % en el mes tres, el prime cost del 66,8 % al 63,8 %, y la carta se reduce de veinte a dieciocho platos. Esas cifras del mes tres son el objetivo de ejemplo con el que se cerró este caso modelado, no lo que le va a pasar al lector: lo suyo lo dirá su propia carta, trabajada con las mismas ocho herramientas.

**La carta de ejemplo entera, plato a plato (matriz-multimetodo-carta.xlsx, hoja «Datos»)**

| Plato | Familia | Uds vendidas | Coste por ración (€) | PVP sin IVA (€) | MC (€) | Food cost (%) | PVP con IVA en sala (€) |
|---|---|---|---|---|---|---|---|
| Croquetas de jamón ibérico (6 ud) | Entrantes | 420 | 2,10 € | 8,60 € | 6,50 € | 24,4 % | 9,46 € |
| Ensalada de tomate rosa, ventresca y cebolleta | Entrantes | 310 | 3,60 € | 11,80 € | 8,20 € | 30,5 % | 12,98 € |
| Gambas al ajillo | Entrantes | 260 | 6,90 € | 15,50 € | 8,60 € | 44,5 % | 17,05 € |
| Huevos rotos con patatas y chistorra | Entrantes | 380 | 2,40 € | 9,80 € | 7,40 € | 24,5 % | 10,78 € |
| Tabla de quesos de la zona | Entrantes | 90 | 5,20 € | 13,60 € | 8,40 € | 38,2 % | 14,96 € |
| Alcachofas confitadas con jamón | Entrantes | 120 | 3,10 € | 10,90 € | 7,80 € | 28,4 % | 11,99 € |
| Sopa de tomate asado con albahaca | Entrantes | 150 | 1,20 € | 7,20 € | 6,00 € | 16,7 % | 7,92 € |
| Solomillo de cerdo ibérico con puré de boniato | Principales | 340 | 5,67 € | 17,30 € | 11,63 € | 32,8 % | 19,03 € |
| Bacalao confitado al pil-pil | Principales | 190 | 7,40 € | 19,10 € | 11,70 € | 38,7 % | 21,01 € |
| Hamburguesa de vaca madurada con patatas | Principales | 460 | 4,30 € | 13,60 € | 9,30 € | 31,6 % | 14,96 € |
| Arroz meloso de secreto ibérico y setas | Principales | 270 | 6,20 € | 16,40 € | 10,20 € | 37,8 % | 18,04 € |
| Chuletón de vaca madurada (500 g) | Principales | 110 | 14,80 € | 32,70 € | 17,90 € | 45,3 % | 35,97 € |
| Lubina a la sal | Principales | 80 | 8,90 € | 21,80 € | 12,90 € | 40,8 % | 23,98 € |
| Pollo de corral asado con patatas | Principales | 300 | 3,70 € | 12,70 € | 9,00 € | 29,1 % | 13,97 € |
| Lasaña de verduras de temporada | Principales | 140 | 2,60 € | 11,40 € | 8,80 € | 22,8 % | 12,54 € |
| Tataki de atún rojo con sésamo | Principales | 130 | 9,60 € | 22,40 € | 12,80 € | 42,9 % | 24,64 € |
| Tarta de queso cremosa | Postres | 520 | 1,30 € | 5,90 € | 4,60 € | 22,0 % | 6,49 € |
| Torrija caramelizada con helado | Postres | 210 | 1,10 € | 5,50 € | 4,40 € | 20,0 % | 6,05 € |
| Coulant de chocolate | Postres | 330 | 1,60 € | 6,20 € | 4,60 € | 25,8 % | 6,82 € |
| Fruta de temporada preparada | Postres | 60 | 1,40 € | 4,50 € | 3,10 € | 31,1 % | 4,95 € |

*Es la misma carta que aparece en la ficha, en la matriz, en la hoja de precios y en el simulador multicanal: todo lo que se lee en esta guía sale de estas líneas.*

**La misma carta en el canal de reparto (simulador-repricing-multicanal.xlsx, hoja «Carta»)**

| Plato | Coste por ración (€) | PVP en sala sin IVA (€) | Food cost en delivery (%) | PVP necesario en delivery (€) | Precio techo (€) | ¿Viable? |
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

**Las decisiones, con responsable y fecha (plan-accion-90-dias.xlsx, hoja «Decisiones»)**

| Plato o área | Herramienta de origen | Decisión | Semana | Estado | Impacto estimado (€/mes) |
|---|---|---|---|---|---|
| Gambas al ajillo (E3) | Matriz multi-método | Revisar | 2 | Pendiente | 180,00 € |
| Chuletón de vaca madurada (P5) | Matriz multi-método | Rediseñar | 1 | Pendiente | 260,00 € |
| Tabla de quesos (E5) | Matriz multi-método | Rediseñar | 4 | Pendiente | 140,00 € |
| Lasaña de verduras (P8) | Matriz multi-método | Revisar | 3 | Pendiente | 120,00 € |
| Fruta de temporada (D4) | Matriz multi-método | Retirar | 3 | Pendiente | 60,00 € |
| Lubina a la sal (P6) en delivery | Simulador multicanal | Retirar | 2 | Pendiente | 90,00 € |
| Chuletón (P5) en delivery | Simulador multicanal | Retirar | 2 | Pendiente | 140,00 € |
| Pescado entero: cambiar a lomos | Test de rendimiento | Negociar | 5 | Pendiente | 260,00 € |
| Copa de crianza: PVP | Carta de bebidas | Resubir | 2 | Pendiente | 210,00 € |
| Cuadrante de sala en meses bajos | Cuadro de mando prime cost | Reformular | 6 | Pendiente | 900,00 € |

**Los indicadores del trimestre (plan-accion-90-dias.xlsx, hoja «KPI de Seguimiento»)**

| KPI | Mes 0 | Mes 3 | Variación mes 3 vs mes 0 | Lectura |
|---|---|---|---|---|
| Food cost (%) | 33,1 % | 29,8 % | -3,3 % | Mejora |
| Prime cost (%) | 66,8 % | 63,8 % | -3,0 % | Mejora |
| Ticket medio sin IVA (€) | 27,4 | 29,1 | 1,7 | Mejora |
| Margen de contribución por cubierto (€) | 18,1 | 20,2 | 2,1 | Mejora |
| Platos en carta (n.º) | 20,0 | 18,0 | -2,0 | Mejora |

*Las cifras del mes 3 son el objetivo con el que se sembró el libro para que veas cómo se lee la tabla, no una previsión de resultados.*


---

## 20. Cuándo tu Excel se Queda Corto

### Las cuatro señales de que la hoja se te ha quedado pequeña

Hay un momento en el que la hoja de cálculo deja de ser la herramienta y pasa a ser el cuello de botella. La primera señal es abrir un segundo local: cada punto de venta trae su propio proveedor, su propia carta (menú) y su propio ritmo de compra, y sostener eso en pestañas duplicadas de la misma hoja multiplica el trabajo sin multiplicar el control, hasta que nadie sabe cuál copia manda. La segunda es que el precio de coste (costo) de tus proveedores cambie a diario: el pescado, el marisco y buena parte de la fruta y la verdura entran en la cocina con un precio distinto cada mañana, y actualizar a mano cada escandallo (costeo de recetas) que usa esa materia prima es una tarea que nadie sostiene más de unas semanas. La tercera es el inventario: cuando el almacén ya no cabe en un recuento visual de fin de semana —varias familias de producto, varios proveedores, mermas que anotar plato a plato— llevarlo a mano deja de ser control y pasa a ser estimación. La cuarta es que más de una persona toque la misma hoja: sin un registro de quién cambió qué y cuándo, la hoja deja de ser fiable y se convierte en un archivo que hay que auditar antes de creérselo.

### Qué te da un software que la hoja no te da

Un software de gestión de escandallos y carta resuelve justo eso. Primero, la entrada de precios: el proveedor manda el albarán y el precio de coste se actualiza solo, así que cada ficha refleja el coste del día en que se sirvió el plato, no el de la última revisión manual. Segundo, el recálculo: cambia el precio de un proveedor y el margen de cada plato de la carta que lo usa se recalcula sin abrir un solo documento; la ventaja frente a la hoja no es que el cálculo sea más exacto, es que ocurre sin que nadie tenga que acordarse. Tercero, la trazabilidad: queda registro de quién cambió cada precio y cuándo, así que un margen que se mueve tiene respuesta, no sospecha entre turnos.

Y aquí la frase que ordena la decisión: esta guía te da el criterio, el software te da la automatización. Un software de este tipo cuesta del orden de 1.100 € al año por local, IVA aparte, así que el salto tiene sentido cuando el tiempo que ahorra vale más que esa cifra, no antes.

Quedarte en la hoja tampoco es gratis de mantener. El plan de 90 días de este pack fija 26 hitos en su calendario, con responsable y fecha cada uno; hoy, recién arrancado, los 26 siguen pendientes y el avance marca un 0 %, porque lo mueven las personas, no la plantilla. El mismo plan registra 10 decisiones con un objetivo de cierre del 80 % a los noventa días: su impacto estimado es de 2.360 €, con una proyección a doce meses —tal como la recoge el propio plan— de 28.320 €. De ellas, 5 salen de la matriz multi-método (760 € de impacto) y 2 del simulador multicanal; el cuadro siguiente reparte el resto por herramienta, y la tabla de arriba, por bloque de trabajo.

### Qué te da un agente de inteligencia artificial

Un agente de inteligencia artificial no calcula el margen por ti —para eso está el escandallo y, si el volumen lo justifica, el software— pero acelera el trabajo que rodea a la carta. Redacta la ficha de un plato a partir de sus ingredientes y su elaboración en el tiempo que tardarías en dictarla. Propone reformulaciones cuando un ingrediente sube de precio o deja de estar disponible, con la misma lógica de sustitución que ya aplicas tú, solo que en segundos y sobre toda la carta: en una carta de ejemplo con 20 platos dados de alta, revisar uno a uno qué sustituir deja de ocupar una tarde y pasa a resolverse en una consulta. Y lee la carta en lenguaje natural: le describes lo que tienes montado y te devuelve dónde hay un desequilibrio de precios, un nombre que no vende o un plato que nadie toca desde hace meses.

Lo que no hace es sustituir el criterio de este libro: lo aplica más rápido. Qué plato subir, cuál retirar y a qué precio anclar la carta son decisiones que ya conoces de capítulos anteriores; el agente ejecuta esa lógica sin que tengas que repetirla cada vez a mano.

Ahí entra AI Chef Pro, la plataforma con la que trabajamos en este libro: agentes de inteligencia artificial pensados para quien gestiona un restaurante y necesita redactar, reformular y leer su carta sin abrir una hoja nueva cada vez. No es un requisito para aprovechar esta guía —el pack funciona entero con lápiz, calculadora y las plantillas que ya tienes— ni una promesa de resultado: es una herramienta más, para quien decida que le conviene.

### La cuenta: cuánto cuesta cada salto

Hay cuatro señales que indican que la hoja de cálculo se ha quedado corta, y casi siempre llegan juntas. La primera es tener más de un local: cada apertura nueva duplica el archivo, y con dos o tres locales nadie está seguro de cuál es la versión buena. La segunda son los precios de proveedor que cambian a diario —pescado, marisco, producto de temporada—, porque un escandallo (costeo de recetas) que hay que actualizar a mano todas las mañanas deja de actualizarse en cuanto llega la primera semana de mucho trabajo. La tercera es un inventario que ya no se puede llevar a mano: cuando el número de referencias supera lo que una persona puede contar y valorar en una tarde, el dato deja de ser fiable el mismo día en que se escribe. Y la cuarta es tener a más de una persona tocando la misma hoja a la vez, que es justo donde aparecen dos versiones distintas del mismo plato con dos costes (costos) distintos y nadie sabe cuál mandó al final.

Un software de gestión de escandallos y carta (menú) resuelve tres cosas que una hoja de cálculo no resuelve bien haga lo que haga quien la lleve: los precios entran solos desde el albarán, sin que nadie los teclee ni los copie de un documento a otro; el escandallo se recalcula en el instante en que cambia el coste de un ingrediente, sin que haya que abrir ni tocar ningún archivo; y queda trazabilidad de quién cambió cada cifra y cuándo, algo que una hoja compartida por correo nunca da. Ninguna de las tres cosas es magia: son automatismos que sustituyen tareas mecánicas, no decisiones.

Un agente de inteligencia artificial aporta otra capa distinta. Redacta la ficha técnica de un plato a partir de los datos que le des, propone reformulaciones cuando un ingrediente se dispara de precio y lee la carta entera en lenguaje natural para señalar qué platos conviene revisar primero. Nada de eso sustituye al criterio que trae este libro: lo aplica más rápido, sobre más platos, sin que tengas que releer ficha por ficha.

Esta guía te da el criterio; el software te da la automatización. Un software de gestión de escandallos y carta cuesta del orden de 1.100 € al año por local, IVA aparte, así que el salto se hace cuando el tiempo que ahorra vale más que esa cifra —y esa cuenta la hace cada negocio con sus propios números, no un libro.

### El orden correcto: criterio primero, automatización después

Quedarse en Excel también tiene coste, aunque no llegue factura al mes. El plan de acción a 90 días de este pack registra 26 hitos en su calendario, con 26 todavía pendientes de cerrar —un avance del 0 % en el momento en que abres el archivo, tal y como muestra la hoja «Calendario 90 Días» de plan-accion-90-dias.xlsx—, porque el calendario empieza en blanco el primer día. Cada hito tiene responsable y fecha; si nadie los cierra, ni la hoja ni el software que compres después van a valer nada, porque la herramienta no toma la decisión por ti: se limita a registrarla.

La hoja «Decisiones» de plan-accion-90-dias.xlsx guarda 10 decisiones ya registradas, con un objetivo de cierre a 90 días del 80 % y un impacto total estimado de 2.360 €, que a doce meses el propio libro traduce en 28.320 €. De esas diez decisiones, 5 salen de la matriz multi-método, con un impacto estimado de 760 €, y otras 2 salen del simulador multicanal: dos orígenes distintos de la misma disciplina, porque primero se prueba la decisión con un método —la matriz, el simulador— y sólo después se ejecuta. La carta de ejemplo que acompaña la matriz, en la hoja «Datos» de matriz-multimetodo-carta.xlsx, tiene 20 platos dados de alta: los justos para ver el patrón sin que el volumen tape el criterio.

Ese orden —primero el método, después la herramienta que lo automatiza— es el que sostiene todo lo anterior. Ninguna plataforma decide por ti qué reformular ni qué precio de venta poner: eso lo decide la matriz, el simulador y el criterio que ya has trabajado en las páginas anteriores. AI Chef Pro es una plataforma con agentes de inteligencia artificial pensada para quien gestiona restauración y quiere aplicar ese mismo criterio con menos trabajo manual —redactar fichas, proponer reformulaciones, leer la carta completa—, pero no promete resultados por sí sola ni hace falta para sacarle partido a esta guía: el plan de 90 días funciona igual con o sin ella. La cuenta final la cierras tú: si el tiempo que gastas manteniendo la hoja pesa más que lo que cuesta automatizarla, ese es el momento del salto, ni antes ni después.

**El avance del plan por bloque de trabajo (plan-accion-90-dias.xlsx, hoja «Calendario 90 Días»)**

| Bloque | Hitos | Hechos | Avance (%) |
|---|---|---|---|
| Medir | 4 | 0 | 0 % |
| Escandallar y clasificar | 4 | 0 | 0 % |
| Aplicar decisiones | 8 | 0 | 0 % |
| Medir el efecto | 8 | 0 | 0 % |
| Revisión | 2 | 0 | 0 % |

*El libro se entrega con todo a cero: el avance lo escribe quien hace el trabajo, y eso es exactamente lo que ningún software hace por ti.*

**De qué herramienta sale cada decisión (plan-accion-90-dias.xlsx, hoja «Decisiones»)**

| Herramienta de origen | Decisiones | Impacto estimado (€/mes) | Impacto conseguido (€/mes) |
|---|---|---|---|
| Ficha de escandallo | 0 | 0,00 € | 0,00 € |
| Test de rendimiento | 1 | 260,00 € | 0,00 € |
| Precio objetivo | 0 | 0,00 € | 0,00 € |
| Matriz multi-método | 5 | 760,00 € | 0,00 € |
| Simulador multicanal | 2 | 230,00 € | 0,00 € |
| Carta de bebidas | 1 | 210,00 € | 0,00 € |
| Cuadro de mando prime cost | 1 | 900,00 € | 0,00 € |


---


---

## Sobre el autor y condiciones de uso

John Guerrero es CEO de AI Chef Pro y fundador de ChefBusiness Group. En cocina desde los 17 años y consultor gastronómico desde 2010, ha asesorado la apertura de más de 200 establecimientos, incluidos restaurantes con Estrella MICHELIN y Soles Repsol en España y Europa. Más sobre su trabajo en johnguerrero.es.

**Versión 1.0 · septiembre de 2026 · aichef.pro/guia-food-cost-ingenieria-menu · info@aichef.pro**

*Esta guía es un documento de trabajo profesional, no un dictamen fiscal, jurídico ni contable. Los tipos de IVA que se citan son los vigentes en España al cierre de esta edición y están recogidos en celdas editables de las hojas de cálculo precisamente porque cambian: si cambia el tipo, se cambia la celda y todo el libro se recalcula. Los costes, precios de venta, márgenes y porcentajes son valores de ejemplo tomados de las ocho plantillas Excel que acompañan a este pack y sirven para que los sustituyas por los tuyos: ninguno es una previsión de tus resultados ni una recomendación de precio. La calificación fiscal de una operación concreta —qué es servicio de hostelería y qué es entrega de bienes, qué tipo lleva un producto determinado— depende de los hechos de esa operación. Antes de cambiar la carta, el precio de un plato o el tipo con el que facturas, contrasta con tu asesoría.*
