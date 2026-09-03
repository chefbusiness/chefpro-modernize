# LENTE 5 — Auditoría de assets existentes y propuesta de herramientas nuevas
## Guía Food Cost + Ingeniería de Menú — research local, sin web

Fecha: 2026-09-03. Método: lectura directa con `openpyxl` (modo lectura, `data_only=False`, un fichero
cada vez, sin builds) de los xlsx vivos en `astro-site/public/dl/`, lectura completa del bono del kit,
de `kit-escandallos-v2-SPEC.md`, de `guias-v2-SPEC.md` §4.1/§4.2/§5, de `documentos.py` y de
`bono_guia.py`. Cero llamadas a bridge.py: este documento es research y propuesta, no contenido de
producto.

---

## 0. Resumen ejecutivo

El terreno de «coste de materia prima + precio de venta» está **muy cubierto** por dos productos que
ya existen y venden: el Kit de Escandallos Pro (12 €, 12 xlsx) y la Guía Restaurante Gastronómico
(85 €, cuyo `escandallo-maestro.xlsx` y `menu-engineering-matrix.xlsx` son, en su versión v2.0 actual,
herramientas serias con fórmulas correctas). Antes de proponer nada nuevo hubo que confirmar tres
cosas, y las tres cambian la propuesta:

1. **`menu-engineering-matrix.xlsx` YA hace clasificación por familias con umbral 70 %/N** — la
   herramienta de «análisis de carta por familias» que proponía el encargo como ejemplo **ya existe,
   byte a byte**, en columnas H/K/L del libro (§2). No se construye aparte.
2. El **bono de 30 días del kit** (`bono-guia-food-cost-30-dias.md`) es un plan táctico
   medir→escandallar→negociar→controlar con ingeniería de menú **básica** (una sola metodología,
   Kasavana-Smith simplificado) y negociación con proveedores **ya tratada a fondo** (7 tácticas +
   guion de llamada). La guía nueva no puede repetir ese contenido: tiene que **profundizar** donde el
   bono se queda en la superficie (multi-método, rendimiento medido, prime cost, multicanal, bodega) y
   **no tocar** la negociación de proveedores, que ya está bien resuelta (§3).
3. **Hallazgo con dinero detrás**: el bono del kit (línea 630) afirma que las bebidas alcohólicas de
   alta graduación llevan IVA del 21 % «en hostelería en España». Es **exactamente el error que John
   corrigió el 2026-08-31** en la guía gastronómica (commit `379fe79`, decisión RD-17, con la cita
   textual del art. 91.Uno.2.2 de la Ley del IVA ya escrita en `escandallo-maestro.xlsx!I31`): el 10 %
   se aplica también al alcohol **servido en sala**; el 21 % es sólo la venta para llevar. Si la guía
   nueva construye una carta de bebidas y copia el criterio del bono sin más, publica el mismo error
   que ya costó una regeneración completa de tres documentos. Ver §5 para el detalle y la cita exacta.

De los 10 ejemplos de herramientas que planteaba el encargo, **evalué las 10**: 7 se recomiendan
construir (con reutilización de motor explícita en cada una), 3 se descartan por duplicación alta con
lo que ya existe (§4).

---

## 1. Inventario exacto de lo que YA cubren nuestras herramientas

### 1.1 Kit de Escandallos Pro (12 €) — `astro-site/public/dl/kit-escandallos/`

| # | Fichero | Hojas | Qué calcula | Inputs | Fórmula(s) clave | Qué le falta |
|---|---|---|---|---|---|---|
| 01 | `escandallo-estandar.xlsx` | Instrucciones, Escandallo, Conversiones, Mermas | Coste de UN plato a la carta, PVP sugerido y food cost real | Ingrediente/Ud. compra/Precio/Cantidad/Ud. uso/Merma | `G=VLOOKUP` factor conversión · `I=E/(1-H)` cant. bruta · `J=I*D/G` coste · `J33=J30/I32` PVP sugerido (coste/FC) | Sólo 1 plato; no cruza con popularidad de venta |
| 02 | `menu-degustacion.xlsx` | 9 pases + Resumen | Coste de un menú de 5-9 pases, FC único editado en Resumen | Igual que 01, ×9 pestañas | `Resumen!C14=SUM(C5:C13)`; cada pase lee `I27=Resumen!$C$16` | No clasifica pases por rentabilidad |
| 03 | `menu-del-dia.xlsx` | 3 platos + Resumen Menú + Rotación Semanal | Coste del menú del día y FC por día L-V | Primer/Segundo/Postre + extras fijos (pan/bebida/café) | `Rotación!K5=I5/J5` FC diario; media semana ponderada | No hay ingeniería de menú del día a día |
| 04 | `cocktails-bebidas.xlsx` | Formatos de Compra + 4 cócteles | Coste por cóctel con conversión botella→€/L | Formato cl, precio botella | `D5=C5*100/B5` €/L; FC objetivo 20-25 % | Sólo 4 cócteles, no hay carta de bodega completa |
| 05 | `pasteleria.xlsx` | 3 recetas por tanda | Coste por unidad repartiendo el coste de la tanda | Ingredientes de la tanda + Rendimiento (uds) | `J28=J26/I27` (coste tanda / rendimiento) | Rendimiento **fijo** (12/20/30); no hay escalado de lote |
| 06 | `catering.xlsx` | Cocktail por persona, Presupuesto, Checklist Evento, Presupuesto Cliente | Coste de catering por comensal + presupuesto de evento (comida+personal+menaje+transporte) | Comensales, coste/comensal, personal, menaje | `C29=MAX(C26+C27,C28)` PVP evento con mínimo de facturación | Sólo eventos tipo cocktail |
| 07 | `cafeteria-brunch.xlsx` | 4 platos (incl. Carrot Cake por tanda) | Igual que 01, FC objetivo 28 % | — | — | — |
| 08 | `food-truck.xlsx` | 3 platos + Punto de Equilibrio | Unidades/día para cubrir costes fijos | Costes fijos diarios, margen ponderado por mix de ventas | `B23=ROUNDUP(B12/B20,0)` | Sólo food truck; el punto de equilibrio no se generaliza a otros formatos |
| 09 | `control-mermas.xlsx` | Mermas Semanal, Evolución | **Desperdicio** (no merma de despiece) semanal por categoría, con semáforo y 12 semanas de tendencia | Compra total, desperdicio real por categoría | `G=F/E`; `I=IF(G<=C,"OK","ALERTA")` | Es agregado por categoría, no por plato ni por semana con causa raíz |
| 10 | `calculadora-pvp.xlsx` | Calculadora PVP | PVP sugerido por 9 tipos de negocio, incl. **Delivery con comisión de plataforma descontada antes del PVP** | Coste por ración, FC mín/máx por tipo, comisión | `G18=$C$4*E18/(1-F18)` PVP con comisión | Una sola fila por tipo de negocio; no aplica a TODA la carta a la vez |
| 11 | `dashboard-food-cost-mensual.xlsx` | Dashboard | Food cost real **mensual** = (stock inicial+compras−stock final)/ventas | 12 meses × stock inicial/compras/stock final/ventas | `H7=F7/G7`; `K7=IF(H7<=D4,"OK","ALERTA")` | Sólo mensual; no cruza con labor cost |
| BONUS | `mermas-inventario.xlsx` | Inventario, Ventas del periodo, Checklist Mermas | Consumo real vs **consumo teórico** (SUMPRODUCT de raciones vendidas × cantidad bruta por receta) | Stock inicial/compras/stock final por producto + raciones vendidas por plato | `F5=C5+D5-E5` consumo real; `G5=SUMPRODUCT(Ventas!C15,…)` teórico; `J5=H5*I5` valor del desvío | Por **ingrediente**, no da una lectura semanal de food cost global con causa raíz |

**Bono prometido** (`bono-guia-food-cost-30-dias.md`, 6.848 palabras): plan de 4 semanas
medir→escandallar→negociar→controlar. Detalle en §3.

### 1.2 Guía Restaurante Gastronómico (85 €) — `astro-site/public/dl/guia-restaurante-gastronomico/`

**`escandallo-maestro.xlsx`** (v2.0, ya con los fixes de `guias-v2-SPEC.md` §4.1 aplicados — verificado
celda a celda, no es el modelo viejo que describe la SPEC como defectuoso):

- Hoja `Ficha (plantilla)`: `D`=Cantidad NETA (ración) · `F`=Merma (%) · `G7='=IFERROR(IF(OR($D7="",$F7>=1),"",$D7/(1-$F7)),"")'` Cantidad BRUTA · `H7='=IFERROR(IF(OR($G7="",$E7=""),"",$G7*$E7),"")'` coste. Bloque de resumen: `H28=SUM(H7:H26)` coste total · `H29=H28/$F$4` coste por ración (raciones en `F4`, editable) · `H4=0,28` (número, formato `0%`) · `H30='=IFERROR(IF(OR($H$29="",$H$4="",$H$4=0),"",$H$29/$H$4),"")'` PVP sugerido sin IVA · `H31`=10 % IVA en celda · `H32=H30*(1+H31)` PVP con IVA · `H33`=celda verde para el PVP real de carta · `H34`=food cost real sobre ese precio.
- Una sola hoja `Ficha (plantilla)` pensada para **duplicar** (clic derecho → mover o copiar) por cada
  plato del menú degustación, más hoja `Resumen` que consolida con `INDIRECT("'"&$A6&"'!H28")` etc.
- **Esto es exactamente el motor que alimenta el escandallo por plato** de cualquier herramienta nueva
  que necesite un coste por ración: cualquier tool nueva puede citar `H29` de una ficha concreta.

**`menu-engineering-matrix.xlsx`** (v2.0, Kasavana & Smith **completo**, no la versión defectuosa que
describe la SPEC):

- Hoja `Menu Engineering`, filas 5-29, **12 platos de ejemplo ya precargados** (Tartar de vaca…
  Cítricos, hinojo y sorbete de yuzu).
- `H5` (Mix %, **dentro de la categoría/familia del plato**, no sobre el total):
  `=IFERROR(IF(OR($D5="",$C5=""),"",IF(SUMPRODUCT(--($C$5:$C$29=$C5),$D$5:$D$29)=0,"",$D5/SUMPRODUCT(--($C$5:$C$29=$C5),$D$5:$D$29))),"")`
- `K5` (margen medio **de su familia**, ponderado por unidades vendidas) y `L5` (**umbral de
  popularidad de su familia** = `$I$32/SUMPRODUCT(--($C$5:$C$29=$C5),--($D$5:$D$29>0))`, con
  `I32=0,7` — el clásico 70 %/N).
- `I5` clasifica **Star/Plowhorse/Puzzle/Dog** con `AND($H5>=$L5,$G5>=$K5)` etc.; `J5` da la acción
  recomendada por cuadrante.
- `D32` calcula qué umbral saldría si se midiera el mix sobre la carta ENTERA en vez de por familia
  (para que el usuario vea la diferencia).

**Conclusión de §1.2, importante para §4**: el ejemplo del encargo «análisis de carta por familias con
umbral 70 %/N» **ya está construido, y con fórmulas correctas verificadas**. No es una hipótesis de
research: es lo que hay hoy en el `dl/` vivo.

### 1.3 ChefBusiness (repo hermano) — no hay producto que auditar aquí

`ingenieria-de-menu.astro` y `reducir-food-cost-restaurante.astro`
(`/Users/johnguerrero/chefbusiness-astro/src/pages/`) son páginas de **consultoría** (landings de
`problemas.ts`, plantilla `ProblemaLayout`), no productos digitales: venden un diagnóstico de 21 días
desde 1.250 €, con CTAs a `consultoria-*`, no un Payment Link. `productos-landing.ts` de ChefBusiness
**ya lista `kitEscandallos`** (id `kit-escandallos`, con la «Guía rápida de Food Cost» de 29 € como
bono citado) — es la tarjeta que enlaza a la tienda única de aichef.pro, coherente con la decisión de
John del 2026-08-31 (tienda única en aichef.pro). No hay ningún producto de food cost/ingeniería de
menú duplicado en ChefBusiness que cree riesgo de canibalización cruzada entre marcas.

`src/components/tools/FoodCostCalculator.tsx` y `matriz-ingenieria-menu.astro` son **herramientas
gratuitas** (islands React, sin pago) para captación de leads de consultoría — otro medio (web
interactiva, no Excel) y otro objetivo (generar diagnóstico gratis → vender consultoría), no compiten
con el Excel de pago de aichef.pro.

---

## 2. Qué del bono de 30 días quedaría duplicado si la guía lo repite

`bono-guia-food-cost-30-dias.md` (6.848 palabras, `scripts/productos-digitales/kit-escandallos-v2_0/`)
cubre, con profundidad real (no un titular):

| Bloque del bono | Profundidad actual | Si la guía lo repite… |
|---|---|---|
| Semana 1 — Medir (fórmula food cost, inventario inicial/final, benchmarks por tipo de cocina) | Completa, con ejemplo numérico y rangos 20-35 % por segmento | **Duplicación directa** si se vuelve a explicar la fórmula base — la guía debe DAR POR SABIDO esto y citarlo, no reescribirlo |
| Semana 2 — Escandallar + ingeniería de menú BÁSICA | Escandallo por plato (ya cubierto por el kit) + **una sola metodología** de clasificación (Estrellas/Caballos/Puzzles/Perros, versión simplificada de Kasavana-Smith, sin fórmulas de umbral por familia) | Aquí es donde la guía nueva SÍ debe ir «más allá»: el bono no compara metodologías, no calcula MCI/CMI de Pavesic ni el cuadrante de Miller, y no separa por familia con umbral 70 %/N (eso lo hace el `menu-engineering-matrix.xlsx` de la guía gastronómica, no el bono) |
| Semana 3 — Negociar con proveedores | **7 tácticas completas** (comparar 3 ofertas, agrupar volumen, formatos de compra, temporada, sustitutos, condiciones de pago, revisión trimestral) + guion de llamada línea a línea + errores típicos | **Ya está bien resuelto y es largo.** La guía nueva NO debe volver a explicar cómo negociar con un proveedor de carne — si necesita tocar compras, debe ir a un nivel distinto (contratos indexados a precio de mercado, gestión de riesgo de volatilidad, condiciones de pago a escala de grupo), no repetir las mismas 7 tácticas |
| Semana 4 — Controlar (rutinas diarias/semanales/mensuales, alertas) | Completa, con dashboard mensual y 5 alertas tipificadas | Puede citarse como «la disciplina base ya la tienes en el bono»; la guía nueva no necesita repetir la ficha de merma diaria ni el dashboard mensual — puede REUTILIZAR esos ficheros por referencia |
| Caso práctico 35,36 %→31,8 % en 30 días | Caso compuesto con cifras coherentes, 4 palancas cuantificadas | La guía nueva necesita SU PROPIO caso, a 90 días y con las herramientas nuevas (multi-método, multicanal, prime cost) — no puede reciclar este caso porque las palancas son distintas |
| FAQ (6 preguntas: cadencia de medición, FC bajo, subidas de precio, IVA bebida, software, equipo) | Completa | La pregunta 4 (IVA bebida) **tiene un error** que la guía nueva no puede heredar — ver §5 |

**Cómo evitar la duplicación, en una frase**: el bono es **táctico y semanal** (una persona, cuatro
semanas, disciplina de medición); la guía nueva tiene que ser **estratégica y de método** (varias
metodologías de clasificación de carta, precios por multicanal, prime cost, bodega, rendimiento
medido) — el plan de 90 días de la guía (§4, herramienta 7) debe explicitar esta diferencia de nivel
en su primer párrafo para que no lea como «el mismo bono, más largo».

---

## 3. Propuesta razonada de herramientas Excel nuevas

Evalué los 10 ejemplos del encargo uno a uno. **3 se descartan** por duplicar mecanismos que ya
existen y verificé con fórmulas exactas; **7 se recomiendan**, cada una con su reutilización de motor
explícita.

### 3.1 Descartadas (con motivo verificado)

| Ejemplo del encargo | Motivo del descarte | Evidencia |
|---|---|---|
| Análisis de carta por familias con umbral 70 %/N | **Ya existe, idéntico**, en `menu-engineering-matrix.xlsx!Menu Engineering` columnas H (mix % por familia), K (margen medio de familia) y L (`=$I$32/SUMPRODUCT(...)`, el 70 %/N literal) | Fórmulas citadas en §1.2 |
| Food cost teórico vs real semanal con análisis de desviaciones | El mecanismo (teórico vía SUMPRODUCT de recetas × ventas, vs real vía stock) **ya está en 3 sitios**: `BONUS-mermas-inventario.xlsx!Inventario+Ventas del periodo` (por ingrediente), `09-control-mermas.xlsx!Mermas Semanal+Evolución` (semanal, con gráfico de 12 semanas), `11-dashboard-food-cost-mensual.xlsx!Dashboard` (mensual). Construir un cuarto no aporta salvo una columna «causa raíz» que puede añadirse a `BONUS-mermas-inventario.xlsx!Inventario` sin crear fichero nuevo | Fórmulas citadas en §1.1 |
| Pastelería por lote | Duplica `05-pasteleria.xlsx` (3 recetas con `Rendimiento (uds)` → `COSTE POR UNIDAD`). Lo único que le falta de verdad —un multiplicador de escalado de lote (12→200 uds)— es una mejora del fichero existente, no un producto nuevo | Fórmulas citadas en §1.1 |

### 3.2 Recomendadas (6.5 → redondeo a 7, todas con reutilización explícita)

#### 3.2.1 `matriz-multimetodo-carta.xlsx` — el diferenciador principal

- **Hojas**: `Datos` (Plato/Categoría/Uds vendidas/Coste/PVP — un único input compartido) ·
  `Kasavana-Smith` (importa la MISMA hoja `Menu Engineering` de `menu-engineering-matrix.xlsx`, con sus
  fórmulas H-M ya construidas) · `Miller` (cuadrante Food Cost % vs popularidad) · `Pavesic` (índices
  ponderados MCI/CMI) · `Comparativa` (una fila por plato, las 3 clasificaciones lado a lado + columna
  «coinciden en las 3 / discrepan»).
- **Inputs**: los mismos 5 campos de `menu-engineering-matrix.xlsx!A5:F29` (nada nuevo que pedir al
  cliente).
- **Fórmulas clave**: Miller — `FC% = Coste/PVP`, clasificación por `FC%` vs FC% medio ponderado de la
  carta (o familia) cruzado con el mismo umbral de popularidad; Pavesic — `MCI = FC%_plato/FC%_medio`,
  `CMI = CM_plato/CM_medio`, «Prime» si `MCI<=1` y `CMI>=1`; Comparativa —
  `=IF(AND(KS=Miller,Miller=Pavesic),"Coinciden en las 3","Discrepan — revisar a mano")`.
- **Qué decisión permite tomar**: cuando las 3 metodologías coinciden en marcar un plato como problema,
  es señal de alta confianza para reformular/retirar sin más análisis; cuando discrepan (típico de un
  plato caro con margen absoluto alto pero FC % pobre — un marisco premium), es la señal de que hace
  falta juicio cualitativo, no una fórmula más.
- **Reutiliza**: la hoja `Menu Engineering` completa de `menu-engineering-matrix.xlsx` (columnas A-M,
  fórmulas H/I/J/K/L/M) como hoja «Kasavana-Smith» del libro nuevo, sin reescribir nada de eso.

#### 3.2.2 `simulador-repricing-multicanal.xlsx`

- **Hojas**: `Carta` (Plato, coste por ración) · `Multicanal` (PVP sala / PVP take-away / PVP delivery
  por plataforma, con su comisión propia y su IVA correcto) · `Resumen` (cuánto sube el precio medio en
  cada canal, y qué platos quedan con FC % inviable en delivery).
- **Inputs**: coste por ración (enlazable a `escandallo-maestro!H29` o a cualquier `xlsx` del kit),
  comisión de cada plataforma (celda verde), coste de packaging.
- **Fórmulas clave**: `PVP_canal = coste/(FC_objetivo×(1−comisión))` — **la misma fórmula que ya usa
  `10-calculadora-pvp.xlsx!Calculadora PVP!G18`** para la fila «Delivery» del kit, aplicada por FILA de
  plato en vez de una sola fila por tipo de negocio; IVA por celda con la regla `=IF(canal="alcohol para
  llevar",0.21,0.10)` (§5).
- **Qué decisión permite tomar**: cuánto subir el precio en cada canal sin perder margen tras comisión,
  y qué platos excluir de delivery porque no aguantan la comisión (FC % > 40 % neto).
- **Reutiliza**: fórmula de `10-calculadora-pvp.xlsx` (kit, fila Delivery) escalada a TODA la carta a
  la vez, que es justo lo que el kit no hace (una sola fila, no un libro).

#### 3.2.3 `precio-objetivo-multi-metodo.xlsx`

- **Hojas**: `Por plato`, 4 columnas de PVP: **Factor** (coste/FC — reutiliza literalmente
  `escandallo-maestro!H30` y `10-calculadora-pvp!G9:G18`), **Margen objetivo en €** (`PVP = coste +
  CM_objetivo€`, para proteger el beneficio absoluto en platos caros con % de food cost naturalmente
  alto, como marisco o trufa), **Mercado** (rango de precios de competencia introducido a mano, PVP =
  percentil elegido), **Valor percibido** (multiplicador sobre el factor, con tabla de ajuste por
  atributos: temporada/escasez/storytelling, +X % editable).
- **Qué decisión permite tomar**: qué método usar según el tipo de plato — factor para volumen y bajo
  coste, margen en € para proteger el beneficio absoluto en platos caros, mercado para anclar contra lo
  que ya paga el cliente de la zona, valor para cobrar más por producto con historia sin que el % de
  food cost lo penalice en la matriz del punto 3.2.1.
- **Reutiliza**: el panel «Factor» es literalmente la fórmula de `escandallo-maestro!H30` y de
  `10-calculadora-pvp.xlsx`; los otros 3 paneles son el aporte nuevo.

#### 3.2.4 `rendimiento-mermas-producto.xlsx`

- **Hojas**: `Test de Rendimiento` (fecha, producto, proveedor/lote, peso bruto AP, peso limpio EP tras
  despiece/limpieza/cocción, subproductos aprovechables con su propio valor, merma real % resultante) ·
  `Mi Tabla de Mermas` (media de N tests por producto, con formato idéntico a la hoja `Mermas` del kit
  para poder pegarse ahí directamente).
- **Fórmulas clave**: `Merma real % = 1 − (Peso limpio / Peso bruto)`; coste neto descontando
  subproductos aprovechados: `Coste neto/kg = (Precio×Peso bruto − Valor subproductos) / Peso limpio`.
- **Qué decisión permite tomar**: sustituir la merma GENÉRICA por categoría (p. ej. «Pescado 35 %», que
  usan TODOS los ficheros del kit vía `VLOOKUP` en la hoja `Mermas`) por la merma REAL medida con el
  proveedor y el cuchillo de ESE restaurante, que puede diferir varios puntos porcentuales y cambiar la
  decisión de precio; y decidir si merece la pena aprovechar subproductos (fondo con espinas, tartar de
  recortes) para bajar el coste neto real.
- **Reutiliza**: la convención matemática de merma `D/(1-F)` de `escandallo-maestro.xlsx` (aplicada en
  sentido inverso: de test a %, no de % a cantidad bruta) y el formato exacto de la hoja `Mermas` del
  kit-escandallos (`Categoría/Mínima/Típica/Máxima`) para que el resultado se pueda copiar sin
  reformatear.

#### 3.2.5 `plan-accion-90-dias.xlsx`

- **Hojas**: `Decisiones` (una fila por plato, importando Clasificación + Acción recomendada de
  3.2.1, con responsable, semana objetivo y estado ✓/en curso/pendiente) · `Calendario 90 días`
  (bloques de 12 semanas: semanas 1-2 diagnóstico y test de rendimiento, 3-6 repricing y reformulación
  con la matriz, 7-10 negociación estructural, 11-12 revisión y nuevo ciclo) · `KPI de seguimiento`
  (food cost %, prime cost %, margen medio por familia, lectura trimestral con semáforo).
- **Qué decisión permite tomar**: da un ORDEN de ejecución a las salidas de las otras 6 herramientas —
  es la pieza que convierte un PDF de análisis en algo que se ejecuta con fecha y responsable, en vez
  de quedarse leído.
- **Reutiliza**: el patrón ✓/—/N/A + contador de `06-catering.xlsx!Checklist Evento` (kit) y el patrón
  de Gantt de `cronograma-apertura-gantt.xlsx` (familia de guías, grupo B). **No reutiliza ni repite**
  el plan semanal de 4 semanas del bono: es trimestral, de nivel de carta y contrato, no de disciplina
  diaria — diferencia que el propio fichero debe declarar en su primera hoja para no leer como «el
  mismo bono, estirado» (§2).

#### 3.2.6 `cuadro-de-mando-prime-cost.xlsx`

- **Hojas**: `Mensual`, 12 filas: Food cost % (misma fórmula que `11-dashboard-food-cost-mensual.xlsx!
  Dashboard!H7`), Labor cost % (bruto + SS / ventas, misma convención al 33 % en celda que
  `plantilla-turnos-brigada.xlsx` §4.4 de `guias-v2-SPEC.md`/kit-gestión-personal), Prime Cost % = suma
  de ambos, semáforo vs objetivo.
- **Qué decisión permite tomar**: la métrica que de verdad usan los grupos de restauración para medir
  salud operativa (food cost y labor cost juntos) — hoy NINGÚN fichero del catálogo cruza los dos; un
  food cost «bueno» aislado puede esconder un labor cost descontrolado.
- **Reutiliza**: fórmula de food cost real de `11-dashboard-food-cost-mensual.xlsx!Dashboard!H7` y la
  convención de SS al 33 % en celda verde de `plantilla-turnos-brigada`/`kit-gestion-personal`.
- **Hueco pendiente, no inventado**: los rangos de referencia de Prime Cost por segmento (el ~55-60 %
  que se cita habitualmente en gestión hotelera para full-service) son una cifra de sector que
  necesita fuente con URL y fecha antes de publicarse — no está verificada en este research (que fue
  local, sin web) y se marca «research pendiente», tal como exige la regla de datos del encargo.

#### 3.2.7 `carta-de-bebidas-beverage-cost.xlsx`

- **Hojas**: `Vinos` / `Cervezas y NA` / `Destilados y Cócteles` (producto, formato de compra, precio
  botella, PVP copa/unidad, beverage cost %, margen) · `Resumen Bodega` (beverage cost medio ponderado
  vs objetivo, mismo rango 20-25 % de bar que ya usa el kit).
- **IVA — casilla explícita, no un supuesto**: «10 % si se sirve en sala (consumo en el acto, art.
  91.Uno.2.2 LIVA) / 21 % si es venta para llevar», reproduciendo LITERALMENTE la nota que ya está
  escrita en `escandallo-maestro.xlsx!I31` y evitando el error del bono del kit (§5).
- **Qué decisión permite tomar**: gestionar la carta de bebidas como una cuenta de resultados propia
  (hoy sólo hay 4 cócteles sueltos en el kit), y aplicar el IVA correcto por canal en vez de un 21 %
  fijo que ya se demostró incorrecto para el consumo en sala.
- **Reutiliza**: el patrón «Formatos de Compra» (botella→precio/L) de `04-cocktails-bebidas.xlsx` del
  kit, y el rango de food cost de bar (20-25 %) ya validado en `10-calculadora-pvp.xlsx`.

---

## 4. Qué de `documentos.py` y `bono_guia.py` se puede reutilizar tal cual

### 4.1 `documentos.py` (`scripts/productos-digitales/guias-v2_0/documentos.py`, 90 KB)

**No está acoplado a la familia de 8 guías más allá de una convención de directorios.** Es un motor
genérico parametrizado por un módulo `guion_<pid>.py` con tres símbolos: `GUIA` (dict con
título/subtítulo/cabecera/pie/gates), `CAPITULOS` (lista de dicts con epígrafes, cifras a citar y
tablas a construir) y `BONUS` (lista de documentos bonus con su propio `CAPITULOS`).

**Reutilizable sin tocar una línea** (verificado leyendo cada función, §"FUNC DEFS" del fichero):

- `wb()`/`celda()`/`eur()`/`pct()`/`num()`/`formatear()`/`resolver_cifras()`/`construir_tabla()` — el
  motor de lectura de xlsx a texto/tabla de Markdown. `celda(xlsx_dir, 'fichero.xlsx!Hoja!C27')`
  funciona con **cualquier** `xlsx_dir`; para la guía nueva sería
  `astro-site/public/dl/<pid-nuevo>/`, apuntando a los 7 xlsx propuestos en §3.
- `guard_no_latinos()`, la familia `erratas_*` (fechas caducas, degeneración, truncamiento, léxico),
  `reparar_erratas()` — genéricos, sin ninguna referencia a las 8 guías.
- `bridge()` — wrapper de `bridge.py` con reintentos a menor `--max-tokens` si vuelve vacío; genérico.
- `prompt_bloque()`/`trocear()`/`generar_capitulo()` — arman el prompt de cada bloque de capítulo a
  partir de `cap` (dict) y `guia` (dict); no leen nada específico de las 8 guías salvo lo que se les
  pase.
- `sanear()`/`sanear_bloques()`/`restos_no_winansi()`/`parsear()`/`construir_docx()`/`construir_pdf()`/
  `maquetar()` — el pipeline Markdown→DOCX+PDF completo, con `PageBreak` por capítulo, portada, índice
  y metadata; genérico dado un `md_text` y un `meta` dict.
- `valores_admitidos()`/`coherencia_cifras()`/`gates()` — la batería de gates (páginas, palabras,
  paridad PDF↔DOCX, tablas ancladas, no latinos, WinAnsi, fechas caducas, coherencia de cifras,
  metadata); genérica dado un `cfg` que sale de `guia['gates']`.
- `construir_documento()` — orquesta un documento entero (capítulos → .md → .docx/.pdf → gates);
  genérica.
- `main()` — CLI `--producto <pid>` ya funciona para cualquier `pid` con su `guion_<pid>.py`.

**Lo único que hay que parametrizar** (cero cambios de código, sólo ficheros nuevos):

1. Escribir `guion_guia_food_cost_ingenieria_menu.py` (o el pid que decida el orquestador) con `GUIA` +
   `CAPITULOS` (el guion cerrado del §5.2 de `guias-v2-SPEC.md`: título, epígrafes, cifras con su `ref`
   a celda de los 7 xlsx nuevos, tablas con su rango) + `BONUS`.
2. Poblar `astro-site/public/dl/<pid-nuevo>/` con los 7 xlsx de §3.2 — es la única fuente de cifras
   que `celda()`/`construir_tabla()` pueden leer (§7-bis.7 de la SPEC: una sola fuente de cifras, el
   propio producto).
3. `RESEARCH` (`auditorias/guias-v2-research-sector.json`) es una constante de módulo compartida por
   las 8 guías; para la guía nueva basta con **añadir entradas nuevas con su `id`** a ese mismo JSON
   (research de Prime Cost por segmento, si se consigue fuente — §3.2.6) en vez de tocar código.

Conclusión: `documentos.py` es la pieza de más apalancamiento de todo este research — se reutiliza
al 100 % con un módulo `guion_<pid>.py` nuevo y una carpeta de xlsx nueva, cero cambios de código.

### 4.2 `bono_guia.py` (`scripts/productos-digitales/kit-escandallos-v2_0/bono_guia.py`, 21 KB)

Es el **predecesor** del patrón que `documentos.py` generalizó — la propia SPEC de guías lo dice
explícitamente (`guias-v2-SPEC.md` §5.3.4: «Maquetado con el patrón de
`kit-escandallos-v2_0/bono_guia.py`»). Mismas funciones (`sanear()`, `parsear()`, `construir_docx()`,
`construir_pdf()`), pero **más simple y menos capaz**: sin `PageBreak` real entre capítulos (usa
`Spacer(1,6)`), sin portada ni índice automáticos, sin la batería de gates de `documentos.py`.

**Cuándo usar cuál**: para el cuerpo de la guía nueva y para bonus que necesiten gates completos
(páginas, coherencia de cifras, paridad DOCX↔PDF), usar `documentos.py` end-to-end como se describe en
§4.1. `bono_guia.py` sólo tiene sentido si se quiere producir un bonus **ligero, standalone**, sin
pasar por el aparato `guion_<pid>.py`/`GUIA` — es decir, un CLI de dos argumentos
(`bono_guia.py <entrada.md> <salida_pdf> [<salida_docx>]`) para un documento suelto que no necesita
capítulos con cifras citadas de xlsx ni gates de coherencia. Para esta guía, con 7 herramientas nuevas
cuyas cifras SÍ hay que citar en el texto (§7-bis.7), la recomendación es **`documentos.py`, no
`bono_guia.py`**.

---

## 5. Hallazgo verificado: el IVA de la bebida alcohólica — el bono del kit tiene el error que ya se corrigió en la guía gastronómica

**El error, con cita exacta**:

`scripts/productos-digitales/kit-escandallos-v2_0/bono-guia-food-cost-30-dias.md:630`:
> «En hostelería en España, las bebidas alcohólicas de alta graduación llevan IVA del 21 %, así que
> conviene separarlas para no distorsionar los cálculos.»

**La corrección ya hecha, con cita exacta**, en `astro-site/public/dl/guia-restaurante-gastronomico/
escandallo-maestro.xlsx`, celda `Ficha (plantilla)!I31` (idéntica en `menu-engineering-matrix.xlsx!
Menu Engineering!G33`):
> «10 % en restauración, INCLUIDA la bebida alcohólica servida en sala: el art. 91.Uno.2.2 de la Ley
> del IVA grava a ese tipo los servicios de hostelería y «el suministro de comidas y bebidas para
> consumir en el acto», y no excluye el alcohol. Cámbialo aquí y se recalcula todo el libro.»

**Fuente y fecha de la decisión**: commit `379fe79` (2026-08-31), orden de John «corrige a 10 % en
sala y rehaz los xlsx», con la referencia legal citada en el propio commit (art. 91.Uno.2.2 de la Ley
del IVA). Efecto medido en ese commit: 131 celdas cambiadas en 3 ficheros de la guía gastronómica
(`budget-bodega`, `cash-flow-break-even`, más las notas de `escandallo-maestro` y
`menu-engineering-matrix`), food cost de bebida de 36,2 % a 32,9 %, margen medio de bodega de 63,8 % a
67,1 %.

**Por qué importa para este encargo**: el bono del kit **no formaba parte** de ese commit (es un
producto distinto, `kit-escandallos`, no `guia-restaurante-gastronomico`) y sigue publicando el 21 %
en producción hoy. Si la guía nueva construye la herramienta 3.2.7 (`carta-de-bebidas-beverage-cost.
xlsx`) o cualquier contenido que toque IVA de bebida, y se apoya en el bono del kit como referencia sin
verificar, **reproduce el mismo error que ya obligó a regenerar 3 documentos completos el 31 de
agosto**. La regla correcta, ya escrita y verificada en el código vivo: **10 % si se consume en el
acto (en sala), 21 % sólo si es venta para llevar**.

**Recomendación operativa** (fuera del alcance de esta LENTE, pero vale la pena decirlo): el bono del
kit-escandallos (`bono-guia-food-cost-30-dias.md:630` y su `.pdf`/`.docx` publicados en
`/dl/kit-escandallos/BONUS-guia-food-cost-30-dias.pdf`) tiene un dato incorrecto en producción HOY, en
un producto que ya vende. Corregirlo es una tarea aparte, con su propio dry-run/gate, no parte de esta
guía nueva — pero el orquestador debería saberlo antes de la siguiente sesión sobre kit-escandallos.

---

## 6. Riesgos de canibalización y posicionamiento

### 6.1 El riesgo real

El Kit de Escandallos Pro (12 €) y la Guía nueva (línea «Guías técnicas Premium», previsiblemente
55-85 € por el rango ya establecido en la familia de guías) compiten por la MISMA intención de búsqueda
(«escandallo», «food cost», «ingeniería de menú» — ver banco de keywords del contexto común) y el mismo
comprador (quien gestiona una carta). Sin una frontera clara, el cliente que ya tiene el kit no ve
motivo para pagar 5-7× más por «lo mismo, con más páginas».

### 6.2 Cómo se evita — la frontera es de MÉTODO, no de tamaño

| | Kit de Escandallos Pro (12 €) | Guía Food Cost + Ingeniería de Menú (nueva) |
|---|---|---|
| Qué es | **Plantillas** para escandallar: coste por plato, PVP sugerido, control de mermas por categoría, dashboard mensual | **Método + análisis + decisión**: cómo clasificar la carta con 3 metodologías cruzadas, cómo fijar precio por 4 métodos distintos, cómo medir el rendimiento real de tu proveedor, cómo leer el prime cost, cómo repricing multicanal, cómo llevar bodega como P&L |
| Nº de metodologías de clasificación de carta | 0 (no clasifica, sólo costea) | 3 (Kasavana-Smith + Miller + Pavesic, comparadas) |
| Precio de venta | 1 fórmula (coste/FC), por tipo de negocio | 4 métodos (factor/margen€/mercado/valor), por plato |
| Merma | Tabla de referencia por categoría (genérica, 21 categorías) | Protocolo de TEST de rendimiento con TU proveedor (medido, no de tabla) |
| Bebidas | 4 cócteles sueltos | Carta de bodega completa como P&L, con el IVA correcto |
| Horizonte | Semanal/mensual (disciplina) | Trimestral (decisiones de carta y contrato) |
| Bono incluido | 30 días, táctico, con negociación de proveedores a fondo | 90 días, estratégico, ejecuta las decisiones de la matriz — NO repite negociación de proveedores |

### 6.3 Cross-sell explícito, en las dos direcciones

- **Desde el kit hacia la guía**: en el bono de 30 días (§5, Semana 2, «Ingeniería de menú básica»),
  añadir una nota — «esta clasificación usa una sola metodología; si quieres cruzarla con Miller y
  Pavesic y ver dónde discrepan, o fijar precio por 4 métodos en vez de uno, es lo que trae la Guía
  Food Cost + Ingeniería de Menú» — con enlace a la landing nueva. Es una edición de 2-3 frases sobre
  un fichero que ya existe, no una reescritura.
- **Desde la guía hacia el kit**: en el capítulo de escandallo de la guía nueva, cuando se necesite el
  coste por ración de un plato concreto para alimentar la matriz multi-método o el simulador
  multicanal, remitir explícitamente al Kit de Escandallos Pro («si aún no tienes cada plato
  escandallado, hazlo primero con el Kit de Escandallos Pro — 11 plantillas por formato de negocio,
  12 €») en vez de reconstruir un escandallo genérico dentro de la guía. Esto además resuelve un
  problema práctico: la guía nueva no necesita una hoja de escandallo por plato propia (evitando
  duplicar 01-08 del kit) — puede asumir que el coste por ración ya existe (del kit o de
  `escandallo-maestro.xlsx` si el cliente tiene también la guía gastronómica) y arrancar desde ahí.
- **Landing**: banner cruzado en ambas landings (`kit-escandallos.ts` y la landing nueva), con el
  patrón ya establecido de banners de producto del blog (`utm_source=landing&utm_medium=cross-sell`),
  para poder medir cuánta gente compra los dos.

---

## Huecos de este research (no medibles sin web ni sin decisión de John)

- Precio final de la guía nueva: no está en el alcance de esta LENTE (research de assets, no de
  pricing) y depende de la decisión de John sobre la línea «Guías técnicas Premium».
- Rangos de Prime Cost por segmento (full-service/casual/QSR) para `cuadro-de-mando-prime-cost.xlsx`
  (§3.2.6): sin fuente verificada en este research local — pendiente de un paso de research con
  WebSearch/WebFetch antes de escribir el capítulo correspondiente, tal como exige §7-bis.21 de
  `guias-v2-SPEC.md` («sin fuente, no entra»).
- No se ha verificado en pycel ninguna fórmula de las 7 herramientas propuestas (son propuestas de
  diseño, no ficheros construidos) — la verificación pycel es tarea de la fase de construcción, no de
  esta auditoría.
- No se ha auditado si `products-catalog.ts` (raíz del repo, 44 productos) necesita una entrada nueva
  para la guía — se confirma que HOY no existe (`grep -in "food-cost"` sin resultados de producto), lo
  cual es la fuente de verdad correcta, pero añadir la entrada es tarea de integración, no de esta
  LENTE.
