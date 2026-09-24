# Recipe Costing Kit Pro — Research de mercado EN en 8 bloques (F1 · 24-sep-2026 · sesión Claude Code)

> Consolidado para el OK de John. Es el mismo método de los productos españoles (memoria
> `feedback_research-previo-producto-nuevo`), adaptado a EE. UU. y Reino Unido.
>
> Detalle, con la fuente de cada dato o la marca `[estimado]` / `[no medido]`:
> - `F1-research-us-uk.md` → bloques 2 y 8, y glosario, impuestos, unidades, SERP y Sheets;
> - `F1-8b-A.md` → bloques 1, 2 (huecos), 3, 5 y 6;
> - `F1-8b-B.md` → bloques 4, 7 y 8 (huecos).

## Veredicto

**Ningún segmento necesita una plantilla nueva para lanzar.** El kit español ya cubre el núcleo de lo que enseñan
ProStart y Culinary Math en EE. UU. y City & Guilds en el Reino Unido: ficha de coste con AP/EP, Q-factor, plate cost
y drink cost, precio por food cost %, food cost por inventario y consumo teórico frente a real.

La adaptación de verdad está en cuatro cosas:
- **cómo compra el hostelero anglosajón**: por caja, saco o barril, y con catch weight;
- **qué cuenta como venta neta**: sin impuesto, sin service charge ni propinas;
- **los valores por defecto** del catering y del food truck;
- **el vocabulario**.

El precio de **$19** se mantiene.

## 1. Tipos de comprador

| Segmento | EE. UU. | Reino Unido | Plantillas que le sirven |
|---|---|---|---|
| Restaurante full-service | 266.611 | 37.300 con licencia | 01, 02, 03, 10, 11, BONUS |
| Limited-service / fast casual | 272.103 | 36.325 sin licencia + cafés | 01, 07, 10, 11 |
| Coffee shop / bakery | 88.925 (+4,4 %) | (incl. arriba) | 05, 07 |
| Bar / pub | 42.323 | 37.805 pubs | 04 |
| Food truck / street food | 13.123 con asalariados (+6 %) | [no medido] | 08 |
| Catering / eventos | 14.147 | 15.210 | 06 |
| Private chef, meal prep, ghost kitchen, estudiantes, consultores | [no medido] | [no medido] | 01, 10 (FAQ específica en la landing) |

Fuentes: BLS QCEW 4T-2025 y ONS/Nomis mar-2025. 7 de cada 10 restaurantes de EE. UU. tienen un solo local (NRA).

**Carencias reales detectadas:**
- bebidas de café;
- subrecetas enlazadas;
- mano de obra / prime cost;
- barril de cerveza.

Ninguna obliga a una hoja nueva. Se cubren con texto o con unidades.

## 2. Normativa que cambia el cálculo

- **Ventas netas** = sin impuesto **y** sin service charge ni propinas.
  - UK: la Employment (Allocation of Tips) Act 2023 obliga a repartir el 100 % entre el personal, y el service charge discrecional queda fuera del VAT (VAT Notice 709/1).
  - US: el service charge obligatorio no es propina (DOL Fact Sheet #15) y puede tributar.
  - Afecta a los textos del 10, el 11, el BONUS y el PDF.
- **Salarios mínimos 2026**: federal $7,25; estados de $11 a $18,40; comida rápida en California $20; UK NLW £12,71 + 15 % de cotización del empleador. Alimentan el catering y el food truck.
- **Impuestos, alérgenos, calorías y medidas de bar**: ya estaban en `F1-research-us-uk.md` §3 y §7.

## 3. Herramientas del sector (en lugar de «equipamiento»)

- **TPV**: Toast, Square, Clover, Lightspeed; en UK, Epos Now. Todos exportan el *product mix* en CSV → instrucción para pegar plato + unidades vendidas en el BONUS («Sales for the Period», columnas A-B). Solo texto.
- **Software de costes**: meez $19/mes, Jelly £129/mes, MarginEdge $350/mes, R365 $469-749/mes. La landing lleva una comparativa **honesta**: el kit no sustituye un SaaS; es la alternativa de pago único para quien aún no lo necesita.
- **Básculas**: la cocina salada pesa en oz (báscula de 5 lb × 1 oz); **la pastelería pesa en gramos** → el 05 compra en lb y formula en g.

## 4. Proveedores y formatos de compra

- **Distribuidores**: Sysco, US Foods, PFG, Gordon Food Service, Restaurant Depot, Chef's Warehouse, Costco Business Center; en UK, Brakes, Bidfood, Booker, JJ Foodservice y Costco.
- **En factura se compra por caja, saco o barril.** Un `case` genérico no sirve: no hay un único factor que valga igual para 4 galones, 36 libras o 180 huevos. Por eso el desplegable pierde `case` y gana formatos con el contenido en el nombre, cada uno con su fuente (USDA, TTB 27 CFR, distribuidores):
  - EE. UU.: `15 dz case`, `30 dz case`, `50 lb bag`, `40 lb case`, `36x1 lb case`, `4x1 gal case`, `12x750 ml case`, `24x12 fl oz case`, `1/2 bbl keg` y `1/6 bbl keg`;
  - UK: `16 kg sack`, `40x250 g case`, `50 L keg`, más `imp pt`.
  - Total: 33 unidades en 241 caracteres, dentro del límite de 255 de Excel.
- **`Conversions`**: ≈ 224 claves generadas por regla, solo entre unidades de la misma dimensión y con factores NIST. Cero duplicados, cero peso↔volumen.
- **Instrucciones 01-08, bloque «From invoice to price per unit»**:
  - notación pack/size y catch weight;
  - lata #10 (96-117 oz netas, USDA);
  - el aceite de freidora va al Q-factor;
  - los precios, sin el impuesto recuperable;
  - pesar los secos (una taza contra una compra en `lb` da «?»).

## 5. Modelo de negocio (valores por defecto y bono PDF)

- **NRA**: beneficio antes de impuestos FSR 2,8 % / LSR 4,0 %; mano de obra 36,5 % / 31,7 %; prime cost LSR 65 %.
- **Cadenas cotizadas**: Chipotle 29,6 %, Shake Shack 28,5 %, Darden 30,6 %, Texas Roadhouse 36,4 % (4T). Las de Darden y Texas Roadhouse se confirman antes de publicarlas.
- **Inflación**: USDA ERS ago-2026 (vacuno +9,8 %, huevos −30,8 %); ONS restaurantes 4,1 %. Regla 30/30/30/10 con su matiz.
- **06 catering** (EE. UU.):
  - 1 camarero cada 25 invitados en recepción; tabla completa en Instrucciones;
  - camarero $25/h y jefe de sala $35/h (OEWS $17 + 7,65 % FICA, o tarifa de agencia);
  - rentals $3,50 por invitado y mínimo $1.000;
  - «margen servicios» → **Service charge (%)** 20 %;
  - propuesta al cliente: «Prices exclude sales tax… the service charge is not a gratuity».
  - Casi todo es `[estimado]`, con el ancla indicada.
- **08 food truck**: $465/día (commissary, permisos y seguro, propano, 2 personas con cargas, amortización y limpieza), con la cuenta de cada línea `[estimado]`.

## 6. Referentes (storytelling, sin afiliación)

Chipotle y las cadenas cotizadas como referencia pública de food cost. Libros de texto: *Culinary Math*, *Math for the
Professional Kitchen*, *Food and Beverage Cost Control* (Dopson & Hayes, 8.ª ed.), que van a «Further reading» del PDF.
ProStart, ACF y City & Guilds como temario que el kit cubre.

## 7. Documentación propia del mercado EN

| Candidato | Veredicto |
|---|---|
| Ficha de coste AP/EP, Q-factor, plate/drink cost, precio por FC %, FC por inventario, consumo teórico | **Ya cubierto** |
| GP % (UK) | Ya en D8 de la SPEC |
| Pour cost por categoría, vino por copa (5 fl oz US; 125/175/250 ml UK), barril | **Adaptación** del 04: unidades de barril y dos filas de ejemplo (vino 750 ml, barril 1/6 bbl) en filas ya existentes |
| Yield test, pérdida en cocción, escalado, subrecetas | **Texto** en Instrucciones |
| Periodo semanal en el dashboard | Rótulo «Period (month or week)» en el 11 |
| Par levels · prime cost · menu engineering | **Fuera de alcance**: son del Kit de Inventario, el Plan Financiero y la Guía Food Cost |
| Hoja *Yield Test* · hoja *Ingredient Price List* (lo que venden Someka y Excel Highway) | **Hojas NUEVAS**: decide John. Recomendación: no en la v1 EN; si se hacen, en ES y EN a la vez |
| Fila de mano de obra / prime cost en el 11 | Cambio de estructura: se propone para una v2.1 conjunta ES+EN; decide John |

Tres volúmenes que engañan: «prime cost» (4.400/mes) es Amazon Prime; «standard pour» (14.800) es un bar de Dallas;
«sub recipe» (720) son bocadillos.

## 8. Precio

**$19 se mantiene.** La SERP de hoy tiene packs de Etsy a $7,99-12,30, Someka a $29,95 y Excel Highway a $39; estos
dos últimos traen base de ingredientes. Subir a $24 solo tendría sentido con esas hojas nuevas y con reseñas en inglés.

## Decisiones que necesita John

1. **OK a este research** y a la adaptación resultante (sin hojas nuevas).
2. **Hojas nuevas *Yield Test* e *Ingredient Price List***: no en la v1 (recomendado) / sí, en ES y EN a la vez.
3. **Licencia de uso**: ¿un consultor puede entregar copias a sus clientes? ¿Hay licencia de aula para escuelas?
