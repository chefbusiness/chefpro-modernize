# Revisión final adversarial — How to Open a Pastry Shop (EN) · guía + bonus «12 Opening Decisions» + plan modelo

> Sesión Claude Code, 17-oct-2026. Un solo revisor (Opus), sin web: cada hecho US se juzgó contra `F1-research-us.md`
> (incl. §16), las cifras contra DECISIONES §3-bis, `xlsx/CIFRAS-RECALCULADAS.md`, `xlsx/cifras_cambiadas.json` y la
> aritmética de las propias tablas; nombres de fichero y hoja contra `xlsx/config_en.py` y `xlsx/textos_en/*.json`.
> Correcciones hechas en `tandas/en/*.md`; `en/*.md` re-ensamblado con `ensamblar_md.py` (17/17 tandas `--final` OK,
> estructura idéntica al ES). Sin commits.

## Qué se comprobó y salió limpio

- **Hechos legales/fiscales/laborales US**: las 60+ citas distintas (secciones del Food Code, 21 CFR 1.226(c)/1.227/101.91/
  101.95, §403(a), 34 TAC §3.293, Reg. 1603, TB-ST-283/806, TSB-A-24(19)S, TIP 10A01-22, H&S §114380/§113948/§438.046(c),
  25 TAC §228.171/§229.176, FS #21/#43, HO 11, IMC 507/506, UL 710B, NFPA 96, ADA 904.4.1, SB 541, SB 54, SB 1383, AB 1200,
  AB 1826, 42 U.S.C. §1791, FDD Items 5-7/19/20/21, Form 8832) están en el research; topes cottage (CA $88,878/$177,756,
  TX $150,000, FL $250,000, NY sin tope), mínimos 2026 (CA $16.90, NY $17.00/$16.00, FL $14.00 «hasta el 29-sep» + aviso
  FloridaCommerce, TX $7.25), FICA/FUTA/SUTA CA, SBA 7(a)/Express/Microloan/504, envases EPS/PFAS, plazos FDACS/NY/CA:
  todos cuadran con su fuente y con la redacción segura que pedía el research.
- **Cifras del caso**: P&L, escenarios, punto muerto (155.6/148.9 tickets), tesorería ($62,115 → mínimo $61,346 mes 3 →
  $87,811; flujo $25,696), $227,916 = $167,916 + $60,000, nómina $7,731.34 × 12, tabla ×15/12, $15,080, picos, canales,
  CAPEX por bloque e ilustración del 8.25 % ($161,480 → $13,322 → $241,238): idénticas en guía, bonus y plan y
  recalculadas a mano (sumas de bloques, sueldo/hora, coste empresa/hora, DSCR, días ociosos, horas de campaña).
- **Producto**: los 8 libros y todas las hojas citadas entre comillas existen en el libro que se nombra (script de
  cruce: 0 discrepancias); índices = títulos de capítulo; ventas cruzadas solo Food Cost Kit Pro, HACCP Food Safety Kit
  Pro, Bakery Business Plan Kit, Food Cost + Menu Engineering Guide y Equivalents Guide; ningún Kit de Tareas, Hosply ni
  producto ES; ninguna marca ⟦ADAPT⟧.
- **Residuo español**: sin €, IVA, convenio, BOE, CCAA, m² (salvo entre paréntesis), °C sueltos ni ids PS-/PA-; todo
  dato español va declarado como ejemplo europeo/español (Matias/Mallorca, Hofmann/Barcelona, guía española del par
  5,000/7,200 sin moneda, traspasos).

## Hallazgos y cambios

| Severidad | Doc · capítulo | Qué estaba mal | Qué se cambió |
|---|---|---|---|
| MAYOR | Guía cap. 18 (T10) · Plan §5 (P02) · Plan §1 (P01) | La «holgura del 22.9 % sobre el equilibrio de caja» se leía como «lo que puede caer tu facturación antes de perder caja» («si la caída se acerca a ese 22.9 %…»). Es previstos ÷ equilibrio − 1 (183 ÷ 148.9): medida sobre el equilibrio. La caída que aguanta la venta es 1 − 148.9 ÷ 183 = **18.6 %**. Un lector creería que aguanta un 23 % de caída | Texto reescrito en los tres sitios: 22.9 % sobre el equilibrio (183 vs 148.9) y «puede caer ≈ 18.6 %… si la caída se acerca al 19 %». Errata ES anotada |
| MAYOR (libro, pendiente) | 3-year-financial-plan.xlsx, "Break-Even" | La nota de «Cushion above CASH break-even (%)» (`textos_en/plan-financiero-3-anos-pasteleria.json` clave 329) repite el error: «How far you can fall below plan…» | **Orquestador**: p. ej. «How far the plan sits above CASH break-even. The drop in sales it can absorb is smaller: 1 − 1/(1 + this %), about 18.6% in the case. The minimum required is in "0. Assumptions".» |
| MENOR | Guía cap. 1 (texto y tabla) · Bonus dec. 1 (tabla) | «Lo que se come en tus mesas generalmente tributa» sin la salvedad de Texas (el estado del caso): allí lo dispara el plato o los cubiertos del vendedor (34 TAC §3.293), no la mesa | Añadida la salvedad de Texas en las 3 frases |
| MENOR | Plan §6 (P02) | «(in most other states, the day you add tables)»: generalización a 47 estados sin fuente | → «in California, New York and Florida, generally the day you add tables» |
| MENOR | Guía cap. 6 (T04) | La independencia del ducto (regla IMC del **Type I**) se extendía a cualquier cocina: «your production kitchen needs its own exhaust duct, separate from the rest of the building» | Acotado a Type I; con Type II, «ask the building department what your adopted code allows» |
| MENOR | Guía cap. 5 (T03) | Las siete zonas «son lo que tus planos necesitan para aprobarse» (el propio texto dice que ningún código US las enumera) | → «they're the answers the plan reviewer will look for» |
| MENOR | Guía cap. 13 (T08) | Workers' comp: «Texas is the exception» (el research solo dice «casi todos» + TX opcional) | → «the best-known exception» |
| MENOR | Guía cap. 6 (T04) | Consejo atribuido a «a pastry chef with nearly fifty employees» sin declarar que es la fuente española | → «Matias, who runs a family pastry business in Spain… (you'll meet him in chapter 13)» |
| MENOR | Guía cap. 7 (T04) · Bonus dec. 2 | Nombres de equipo de la tabla "Capacity by Equipment" que no existen en esa hoja: «Automatic dough sheeter, up to 16 in wide», «Walk-in cooler, 8 m³ (about 283 cu ft)» | → «Dough sheeter, up to 16 in wide» y «Walk-in cooler, about 283 cu ft (8 m³)» (literales del libro) |
| MENOR | Guía cap. 8 (T05) | «A 20-qt planetary mixer is in at $595.04» frente a la tabla («20 L (about 21 qt)») | → «A 20-liter (about 21-qt) planetary mixer… below the cheapest 20-qt one» |
| MENOR (libro, pendiente) | startup-cost-calculator.xlsx, "Startup Costs by Block" | La partida se llama «Planetary mixer, 20 qt» (`textos_en/calculadora-capex-pasteleria.json` clave 162), mientras el cap. 4 y los otros dos libros dicen «Planetary mixer, 20 L (about 21 qt)»; además 20 qt es falso (cubeta de 20 L) | **Orquestador**: cambiar la clave 162 a «Planetary mixer, 20 L (about 21 qt)» (y PENDIENTES-XLSX T04, que aún propone «20 qt») |
| MENOR | Plan §6 (P02) | «Of the whole list, the longest lead time is the… retarder-proofer's: nine weeks»: la lista trae el horno de pisos (opcional) a 12 semanas | → «Of the lines you're actually ordering…». Errata ES anotada |
| MENOR | Bonus dec. 12 (B03) | «all 15 are TCS food» (la propia tabla da 13 rellenos no estables; la condición TCS la decide pH/aw) · «goes in the bin» (UK) | → «the model treats all 15 as TCS food…» · «goes in the trash» |
| MENOR | Anexo (T12) | Remisiones de capítulo erróneas: Food Code «people and labels» Ch. 2 (es el 3) · 21 CFR 1.227 Ch. 16 (es el 15) · sales tax CA/TX Ch. 2 (son 1 y 3) · §403(a) sin el 19 · «The Florida figure in chapters 1 and 13» (el cap. 1 no da cifra de FL) | Corregidas; FL → «chapter 13, bonus decision 8 and the sample plan» |
| MENOR | Bonus portada (B01) · Plan portada y §1 (P01) | «Every number comes from a cell you can open» / «Every figure comes from the eight Excel tools»: falso desde que se añadieron BLS, NRF, CBRE, Toast, Zenind, USDA… | Acotado a «every number about the case…; outside figures name their source» |
| MENOR (estilo) | Guía caps. 2, 7, 13 · Plan §2 y §4 | Calco «cruising speed» (velocidad de crucero), 6 veces, frente al «steady-state year» fijado | → «steady-state year» / «the year adds up to the steady-state year's sales» |

**Recuento**: BLOQUEANTE 0 · MAYOR 2 (1 corregido en texto, 1 en el libro → orquestador) · MENOR 14 (13 corregidos, 1 en
el libro → orquestador). Tandas tocadas: T01 T02 T03 T04 T05 T08 T10 T12 B01 B03 P01 P02 (gate `--final` OK en las 17).

## Lo que no se tocó, y por qué

- **Docx/PDF ya renderizados** en `astro-site/public/dl/how-to-open-a-pastry-shop/` son anteriores a estos cambios:
  hay que re-renderizar (`render_en.py`, VPS) los tres documentos.
- **«1.5 % de las ventas» de servir + cobrar + comisión (cap. 17)**: es la definición del libro (68 % de la regla única −
  66.5 % de contribución); con los márgenes brutos por canal de la propia tabla (67.2 % ponderado) el coste de servir
  pesa ≈ 0.7 %. Es diseño del modelo y está igual en ES: no lo cambio; decidir si se reformula en libro y texto.
- **Fondo de maniobra «cuatro meses de costes fijos (rent, payroll, utilities) a $15,529/mes»** (cap. 4): $15,529 =
  costes fijos del P&L ÷ 12, amortización e intereses incluidos. Conservador y de libro; el paréntesis simplifica.
- **California, horas extra diarias (> 8 h/día)**: afectaría al turno de 8 h del caso en CA, pero no está en el research
  (§5 solo trae FLSA semanal y pausas de CA). El cap. 14 ya remite a las reglas estatales; si se quiere la frase,
  verificarla y añadirla a §16 antes.
- **BizBuySell / BizQuest** (cap. 6) no están en el research: son portales reales de compraventa de negocios, sin
  contenido normativo; se dejan.
- **Bio del autor**: idéntica a la Food Cost EN (decisión T12); no verificable aquí.
- **Florida $14.00**: el research no confirma la subida a $15.00 del 30-sep-2026; el texto ya lo dice y remite a
  FloridaCommerce (conviene verificarlo antes de publicar y, si se confirma, poner $15.00 en caps. 13, bonus 8 y plan).
- **«campaign»** se mantiene aunque el glosario §13.1 lo desaconseja: lo fijan SPEC D13 y las hojas del libro.
- Avisos del gate aceptados: ratio de palabras de P02 (1.31), menciones de Spain/Spanish (ejemplos europeos declarados).
