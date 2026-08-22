# Kit de Escandallos Pro — v2.0 (SPEC, 2026-08-22)

Origen: ronda 1 adversarial (`auditorias/kit-escandallos-R1.json`, 3 lentes opus, 90 hallazgos, 20 altas,
veredicto «no listo» ×3). Decisiones del orquestador: lo que sigue es lo que SE HACE; lo que no está
aquí se descarta con motivo en §6. Referencia de método y calidad: `kit-tareas-pasteleria-v2-SPEC.md`
y su post-proceso (`kit-pasteleria-v2_0-postprocess.py`: insertar filas/columnas sin romper merges,
DV ni fórmulas; idempotencia; `finalizar()`; `inject_cache.py` al final; verificación `data_only`).

Ficheros: `astro-site/public/dl/kit-escandallos/` (12 xlsx: 01-11 + BONUS-mermas-inventario) + el
bono nuevo. Se trabaja con **`--dry-run` sobre copias** hasta que la ronda 2 dé verde; la ejecución
real la hace el orquestador. Nada de builds locales ni Playwright; python en serie; `istats` entre
barridos.

Convención del kit (se mantiene): **food cost objetivo** = coste / PVP sin IVA → PVP = coste / FC.
Celdas editables en verde (`E8F5E9`); calculadas sin relleno. IVA y otros parámetros en celdas, no
en literales. Todas las divisiones con `IFERROR`. pycel soporta IFERROR, VLOOKUP, INDEX/MATCH,
ROUNDUP, SUMPRODUCT, MAX, TEXT (comprobado): lo nuevo debe cachear.

## 1. Motor común de los escandallos (01, 02, 03, 04, 05, 06, 07, 08) — `motor.py`

1.1 **Unidades con factor de conversión** (DOM-05/TEC-01/COM-04, alta). Columna nueva
«Factor» (oculta o estrecha, gris) entre «Ud. Uso» y «Merma»: `=IFERROR(VLOOKUP(C{r}&"→"&F{r},
Conversiones!$A:$B,2,FALSE),1)` sobre una hoja auxiliar `Conversiones` (kg→g 1000, kg→kg 1,
L→ml 1000, L→cl 100, L→L 1, docena→ud 12, ud→ud 1, manojo→ud 1…; incluir las parejas que
existan en los desplegables actuales). Coste = `=IFERROR(H{r}*D{r}/Factor{r},"")`. Cant. bruta
`=IFERROR(IF(E{r}="","",E{r}/(1-G{r})),"revisa merma")`. **Las 17 filas precargadas con C≠F se
corrigen** para que la cantidad esté en la unidad de uso (p. ej. gin 5 cl con C=L, F=cl → factor
100). Instrucciones: «Cantidad en la unidad de USO; el precio en la de COMPRA; el factor convierte».
1.2 **IVA en celda** (DOM-13/TEC-15): celda verde «Tipo de IVA (%)» = 10 % en cada hoja de
escandallo (y una global en 10-calculadora); `*1.10` → `*(1+$celda)`. Nota en Instrucciones (IGIC,
LATAM).
1.3 **Merma precargada por categoría** (DOM-14/TEC-10): hoja auxiliar `Mermas` (16 categorías →
mín / típica / máx; los valores típicos son los actuales de 01!Instrucciones; mín/máx razonables
por familia) y en las filas VACÍAS `G = IFERROR(VLOOKUP(B,Mermas!A:C,2,FALSE),"")` (sobrescribible).
Las filas precargadas conservan su valor escrito.
1.4 **Raciones y food cost real** (COM-18/DOM-18/COM-17): en el bloque final de cada escandallo,
filas nuevas: «Nº de raciones» (verde, 1), «COSTE POR RACIÓN» = total/raciones, «PVP actual en
carta (sin IVA)» (verde, vacía) y «FOOD COST REAL (%)» = IFERROR(coste ración / PVP actual, "")
con formato condicional rojo si > objetivo. El PVP sugerido pasa a calcularse sobre el coste por
ración.
1.5 **Filas libres** (TEC-12): 5 filas más por escandallo con la misma rejilla y el SUM ampliado.
1.6 **Protección de hoja sin contraseña** (DOM-27/TEC-25): `ws.protection.sheet = True`, con
las celdas verdes (relleno E8F5E9) y las columnas de entrada de ingredientes desbloqueadas
(`cell.protection = Protection(locked=False)`); instrucción «Revisar → Desproteger hoja» en
Instrucciones. Verificar con pycel que nada se rompe.
1.7 Ejemplos realistas (DOM-20/DOM-21/TEC-26/DOM-23): tostada de aguacate → coste ≈ 2,2 €, PVP ≈
9,5 € con IVA (1 rebanada, ½ aguacate, 1 huevo); microgreens por bandeja de 50 g (0,21 €/ración,
sin merma); colorante de macarons 2 g; categorías mal asignadas corregidas (lista en R1 DOM-23).
1.8 Instrucciones de cada fichero reescritas para describir EXACTAMENTE la hoja (columnas nuevas,
factor, IVA, raciones, protección).

## 2. Grupo A (motor + 01, 02, 03, 07) — `grupo_a.py`
- **02 menú degustación** (DOM-16/TEC-17/COM-14/TEC-09): pestañas «6. Pase»…«9. Pase» vacías con
  la rejilla completa; Resumen ampliado a 9 referencias con `IF(pase vacío,"",…)`; un ÚNICO food
  cost objetivo editable en Resumen que alimenta el de cada pase (`='Resumen'!$C$12`).
- **03 menú del día** (TEC-16/COM-15/DOM-17): hoja «Rotación Semanal» L-V × (primero, segundo,
  postre) con celdas que referencian el coste de cada escandallo (desplegable de platos o
  referencia directa), coste medio y food cost por día.
- **07 cafetería/brunch** (DOM-08/TEC-23/COM-12): pestaña «Carrot Cake» (por raciones: §1.4).

## 3. Grupo B (04, 05, 06, 08) — `grupo_b.py`
- **04 cócteles** (DOM-06/COM-23/DOM-22/DOM-24/COM-33/TEC-30/COM-29): cantidades en cl con factor
  (§1.1); columna «Formato de compra (cl)» (70 cl destilados, 75 vino) y precio/L calculado o nota
  clara; rótulos «plato» → «cóctel / bebida»; «Coste elaboración» → «Merma y hielo (%)» 5 %; UN solo
  rango de food cost de bar (20-25 %) en landing, Instrucciones y celdas; nombres de pestaña citados
  correctamente.
- **05 pastelería** (DOM-04/TEC-05/COM-01/TEC-20/COM-13): fila «Rendimiento (uds)» (12/20/30),
  «COSTE POR UNIDAD», «PVP POR UNIDAD» (sin y con IVA); mermas 12 % chocolate de cobertura y 8 %
  harinas/horneado como dice la landing; colorante 2 g.
- **06 catering** (DOM-12/TEC-08/COM-05/DOM-19/TEC-21/TEC-07/COM-19/TEC-24/COM-16): pestaña
  «Cocktail 50 pax» → «Cocktail (por persona)» con aviso en A2; Presupuesto con «Food Cost
  objetivo (%)» y `C17=C14/C16` (convención del kit); bloque de personal explícito (camareros =
  ROUNDUP(pax/22,0), horas, €/hora, jefe de sala) y menaje con «€/comensal» en celda verde; hojas
  nuevas «Checklist Evento» (timings, personal, menaje, transporte, montaje, alérgenos, permisos —
  con desplegable ✓/—/N/A y contador como en los kits de tareas) y «Presupuesto Cliente» (solo
  concepto, pax, PVP/persona con IVA, total).
- **08 food truck** (DOM-07/TEC-06/COM-03): hoja «Punto de Equilibrio»: costes fijos diarios
  editables (plaza, seguro, combustible/generador, personal, amortización, tasas), margen de
  contribución medio de las 3 hojas, «UNIDADES/DÍA para cubrir costes» = ROUNDUP(CF/margen,0) y
  facturación mínima.

## 4. Grupo C (09, 10, 11, BONUS) — `grupo_c.py`
- **09 control de mermas** (DOM-02/TEC-04/COM-22/DOM-09/TEC-03/COM-08/DOM-10/TEC-22/COM-20/COM-09/
  DOM-26): columna B pasa a «Desperdicio objetivo (% s/compra)» con benchmarks por familia (secos
  /congelados 2-3 %, carne/pescado 3-5 %, verdura/fruta 5-8 %, bebidas 1-2 %); columnas «Mín / Típica
  / Máx» de desperdicio; semáforo con formato condicional (OK verde C6EFCE / ALERTA rojo FFC7CE)
  sobre Estado y escala sobre Merma real; hoja «Evolución» de 12 semanas (o meses) alimentada por
  el TOTAL con un LineChart construido con openpyxl (`Reference` + `set_categories`); Instrucciones
  coherentes. La referencia de mermas de despiece se queda en el escandallo (hoja `Mermas`).
- **10 calculadora PVP** (DOM-11/TEC-18/COM-11): fila «Delivery» (FC objetivo 18-22 % + columna
  «Comisión plataforma (%)» que se descuenta antes del PVP); columna «Multiplicador» =
  1/AVERAGE(mín,máx); IVA global en celda; Instrucciones alineadas.
- **11 dashboard food cost** (DOM-03/TEC-14/COM-10/TEC-13/COM-24/TEC-27/COM-27): columnas «Stock
  inicial (€)» y «Stock final (€)»; food cost = IFERROR((ini+compras−fin)/ventas,""); rótulos
  «sin IVA»; columna «Estado» OK/ALERTA + formato condicional rojo; serie objetivo
  `=IF(D7=0,"",$C$4)`; gráfico regenerado con openpyxl (categorías como texto, eje abajo); rótulo
  del input sin cortar; Instrucciones con la fórmula del consumo.
- **BONUS inventario** (DOM-15/TEC-19/COM-31/COM-32/DOM-25/TEC-28): pestaña «Ventas del periodo»
  (plato × raciones vendidas × cantidad/ración por ingrediente) y «Consumo teórico» calculado con
  SUMPRODUCT; «Precio unitario (€)» y «Valor de la diferencia (€)»; guarda de vacío en Diferencia;
  registro con 90 filas y rotulado «Registro de incidencias (mes)».

## 5. Bono prometido, landing, dashboard, changelog — `integracion` (sonnet)
- **BONUS 1 «Guía: Controla tu Food Cost en 30 Días»** (DOM-01/TEC-02/COM-02): se PRODUCE. Texto
  con `bridge.py` (orquestador), maquetado a DOCX (python-docx) y PDF (reportlab, como las guías)
  → `/dl/kit-escandallos/BONUS-guia-food-cost-30-dias.pdf` (+ `.docx`), clave `bonus-guia` en
  `PRODUCT_FILES['kit-escandallos']`, tarjeta en `TEMPLATES` del dashboard, mega pack no aplica.
  Estructura: plan semana a semana (4 semanas: medir → escandallar → negociar → controlar),
  tácticas de negociación con proveedores, checklist semanal, caso práctico con cifras coherentes
  con el kit (food cost 32 % → 27 %). Sin precios fechados. Bio anclada.
- Landing `astro-site/src/data/productos/kits/kit-escandallos.ts` (y `src/components/kit-escandallos/*`
  de la SPA si siguen vivos): textos alineados con lo que HAY (9 pases, rotación semanal, carrot
  cake, delivery, mermas mín/típica/máx, semáforo, gráfico de evolución, checklist + presupuesto
  cliente, punto de equilibrio, food cost real, «Cada plantilla de escandallo…», un solo gráfico en
  singular); ancla de valor coherente (COM-21: valor total = plantillas + bonos); dashboard «Tus 12
  plantillas + 2 bonus» (COM-26); **NO tocar** `aggregateRating`/`review`/`priceOld`/`discountBadge`
  (COM-06/COM-07/COM-28: aparcado por John).
- Changelog: entrada **2.0** (2026-08-22) en `productos-changelog.ts` con lo construido (textos al
  cliente, sin cifras que haya que sincronizar), `updateNote` → «Producto actualizado · Versión 2.0
  · agosto 2026», línea de versión de los xlsx → «Versión 2.0 · agosto 2026 · aichef.pro/kit-escandallos».
- Gates: `censo-entregables.py --only <carpeta> --fail` (0 defectos), `gate-flujo-postpago.py
  --offline --only kit-escandallos`, `inject_cache.py` al final, verificación `data_only`,
  contadores y fórmulas nuevas evaluadas con pycel cambiando inputs.

## 6. Descartado con motivo
- COM-06/COM-07/COM-28 (reseñas, ancla de precio, «#1»): decisión aparcada por John (2026-08-22).
- TEC-29 (zona de foto pequeña): cosmético, se amplía la fila si es trivial; no bloquea.
- DOM-27 con contraseña: sin contraseña (el cliente debe poder desproteger).
