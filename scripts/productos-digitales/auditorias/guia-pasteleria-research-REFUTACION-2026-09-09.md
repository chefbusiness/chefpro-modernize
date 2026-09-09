# REFUTACIÓN — «Cómo Montar una Pastelería»

**Fecha:** 2026-09-09/10 · **Objeto:** `guia-pasteleria-RESEARCH-2026-09-09.md` (1.003 líneas) y las seis lentes `L1`…`L6` del mismo directorio.
**Método:** tres lentes en un pase (rigor · negocio · producto), con verificación directa contra fuentes primarias (BOE consolidado en PDF, descargado con `curl` y extraído con `pypdf`), contra el repositorio, contra los PDF/DOCX de `astro-site/public/dl/` medidos con PyMuPDF y contra los xlsx del catálogo abiertos con openpyxl. **Se ha intentado TUMBAR la propuesta, no confirmarla.**

**Veredicto: CORREGIR ANTES.** 32 refutaciones: **8 altas · 16 medias · 8 bajas**. El núcleo aguanta —el hueco de entregables existe, la frontera con el kit está bien pensada y el bloque legal es el más verificable de los cuatro productos del ciclo—, pero **no se puede firmar la SPEC tal cual**: el argumento de credibilidad estrella se cae al recomputarlo, hay dos lecturas del RD 1021/2022 que se publican como categóricas y no lo son, un fichero que la guía va a citar contradice a la norma que la guía enseña, el presupuesto queda por debajo del único precedente medido para un paquete más grande, y falta justo el gate que habría evitado la línea rota que este research denuncia.

---

## Lo que SÍ he confirmado letra a letra (para que no se re-verifique)

**Repo:** `products-catalog.ts` **47** entradas · `payment-links.ts` **47** · `product-prices.ts` **47** · la **escalera de precios completa del §11.1 es exacta en sus 13 filas** (9/12×13/14×8/18/18,5/24/29×2/35×3/39/45×4/55×3/65×7/85/89) · `comingSoon` con **2** entradas y la descripción literal en `ProductosDigitales.tsx:942` y `ProductosDigitalesHubPage.astro:957` · «montar una pastelería» en el placeholder animado, `ProductosDigitalesHubPage.astro:2259` · `sinonimos-buscador.json` tiene **7** grupos y **ninguno** menciona pastelería, obrador ni montar · `robots.txt` con `Disallow: /guia-*-access` y `/guia-*-library` en los **5** bloques (líneas 35-36, 53-54, 71-72, 89-90, 107-108) · `use-cases-content.es.ts` con **51** bloques `productIds`, `guia-panaderia-obrador` con **0** apariciones, y el miswiring del panadero real en `:1153` (heladería, pizzería, chocolatería y bar sí llevan su propio kit, así que no es el patrón por defecto) · `documentos.py` **2.189** líneas, `repartir_puntos()` en `:1096`, commit **`3c1444d`**, y **0 de 4** guiones usan `puntos_por_epigrafe` · `censo-entregables.py` existe.

**Medido por mí:** los 10 PDF de `dl/guia-*/` — dark-kitchen 27p/7.023 · food-cost 95p/50.265 (**529 pal/pág**, confirma la calibración) · panadería **1p/55** · casual, japonés, mexicano, nikkei, peruano **1p/33** cada uno · gastronómico **10p/2.488**. Los DOCX de guía: 4.699 (panadería) · 2.917 · 5.813 · 4.195 · 6.317 · 4.763 · **2.395** (gastronómico). `business-plan-modelo.docx` de panadería **796 palabras / 0 tablas** — exacto.

**Kit y catálogo:** `kit-tareas-pasteleria` tiene **15** ficheros · todas las dimensiones citadas en §8.1 y §8.3 son exactas: Matriz Alérgenos **57×22**, Plan Semanal **56×11**, Producido vs Vendido **261×12**, Ficha de Encargo **51×4**, Registro **48×15**, Agenda **19×8**, Encargos de Hoy **24×7**, `kit-escandallos/05-pasteleria.xlsx` Instrucciones **66×2** / Tarta Chocolate **38×13** / Croissants **37×13** / Macarons **37×13** / Conversiones **37×3** / Mermas **25×4**, y los **4** perfiles (Jefe Pastelero · Pastelero · Ayudante · Dependiente Vitrina).

**Los 8 posts del §13.2 y sus 24 banners son exactos, banner a banner**, y las 8 cifras de menciones (258 · 110 · 72 · 90 · 55 · 45 · 40 · 18) coinciden al dígito.

**`plan-financiero-panaderia.xlsx`: 9 hojas, 737 fórmulas y CERO fórmulas prohibidas** (ni `INDIRECT`, ni `COUNTA`, ni `PMT`, ni `OFFSET`, ni `XLOOKUP`, ni `LET`, ni `LAMBDA`). El molde de `planes-v2_0` es construible tal cual y la corrección nº3 de L6 es correcta. Y `guia-panaderia-obrador/plan-financiero-3-anos.xlsx` es efectivamente **una sola hoja 25×5 con 21 fórmulas**.

**BOE, leído por mí en texto consolidado:** RD 1021/2022 (`BOE-A-2022-21681`, BOE núm. 305 de **21-dic-2022**) — art. **3** (25 % **o** 500 kg incluyendo consumidor final; zona de salud o ≤50 km; no a inscritos en RGSEAA; declaración responsable; 3.6 central+sucursales), art. **4.1 fila 9** («Productos de pastelería rellenos (salvo que sean estables a temperatura ambiente). Igual o inferior a 4 °C»), art. **9** (70 °C/2 s · 63 °C/20 s + consumo inmediato · ovoproducto; 9.3 ≤8 °C, 24 h y registro), art. **11** (menciones voluntarias, sólo en el establecimiento o sus sucursales, fraccionar/envasar no es elaborar) y art. **13** completo. **Todos exactos.** Ley 1/2025 (`BOE-A-2025-6597`, BOE núm. 80 de **02-abr-2025**) — D.F. vigésima literal, art. 6.4.c), 6.6, 6.7, art. 21 (2.000 / 60.000 / 500.000 € y las CCAA pueden incrementar) y art. 23 (6 meses / 1 año / 2 años). **Todos exactos. V-01 queda cerrada.**

---

## A — RIGOR

### A1 · ALTA — «La validación cruzada más fuerte del research» está construida sumando precios con IVA y sin IVA, el error que el propio documento denuncia dos líneas más abajo

**Afirmación literal (§4.3):** «🟢 **La validación cruzada más fuerte del research (PS-85 / §4.4 de L4):** la dotación tipo montada con **precios reales verificados** suma **≈29.683 €** de maquinaria, y coincide casi exactamente con el nivel «equipamiento medio **29.000 €**» que La Hostelera publica de forma **independiente**… **Dos fuentes independientes cuadrando es el mejor argumento de credibilidad que tiene este producto.**»

**Problema.** He recompuesto la tabla de `L4:384-398` línea a línea. La aritmética del subtotal es correcta (29.682,77 €), pero **es una suma de bases fiscales distintas**, y la propia L4 lo declara en su encabezado («Todos los importes **sin IVA salvo indicación**»):

| Línea | Importe | Base | id |
|---|---|---|---|
| UNOX XB693 Bakerlux | 3.354,12 € | **CON IVA** | PS-72 |
| SMEG ALFA420E1HDS | 2.513,41 € | **CON IVA** | PS-72 |
| Sammic BP-20 | 595,04 € | no declarada | PS-81 |
| Sammic DF-40 | 1.215,00 € | sin IVA | PS-79 |
| Irinox 4 bandejas | 10.037,00 € | + IVA | PS-78 |
| Docriluc VEPD-9-15-C ×2 | 4.568,20 € | sin IVA, **con −30 % de campaña** | PS-76 |
| Selmi One 12 kg | 7.400,00 € | + IVA, **«opcional según concepto»** | PS-82 |

Son **5.867,53 € con IVA + 23.815,24 € sin IVA**. Homogeneizado a la base de La Hostelera —que publica **con IVA**, según el propio PS-72— el subtotal real es **34.684 €**, un **+19,6 %** sobre los 29.000 €. La coincidencia desaparece. Y hay dos agravantes: **el 25 % del subtotal es una atemperadora de chocolate que la propia L4 marca como opcional** (sin ella son 22.283 €, un −23 % contra los 29.000 €), y **dos de las ocho líneas son la misma vitrina contada dos veces a precio de campaña con −30 %**, que caduca.

Tres párrafos más abajo el mismo §4.3 escribe: «⚠️ los precios **mezclan CON y SIN IVA según distribuidor**… **Cada línea del xlsx necesita columna "¿lleva IVA?" o el CAPEX saldrá un 21 % desviado.**» El research diagnostica la enfermedad y se muere de ella en su afirmación estrella.

**Gravedad: alta.** Es el argumento de credibilidad que el research se autoconcede, alimenta el «≈116.000 €» del mismo bloque, entra en el capítulo 04 y va camino de la landing.

**Fix.** Recomponer el subtotal en **una sola base** (recomiendo sin IVA, que es la que usa un CAPEX), sacar la línea marcada como opcional del subtotal comparable, fechar el descuento de la Docriluc, y publicar la comparación real: **≈28.700 € sin IVA frente a ≈23.970 € sin IVA de La Hostelera**, o la equivalente con IVA. Si tras homogeneizar la desviación sigue siendo del 20 %, **decirlo**: «dos fuentes independientes en el mismo orden de magnitud, con un 20 % de diferencia» sigue siendo un argumento honesto y es inatacable. Y aplicar ya la columna «¿lleva IVA?» a la tabla del research, no sólo al xlsx futuro.

---

### A2 · ALTA — «Los 500 kg incluyen el mostrador, así que puedes pasarte sin un solo B2B»: los dos umbrales de *marginal* son ALTERNATIVOS, y el art. 3 sólo se activa si hay suministro a otros minoristas

**Afirmación literal (§1.2 nº 2, repetida en PA-02, cap. 09 y en el libro 7):** «Los tres requisitos del art. 3 son **ACUMULATIVOS**: marginal (≤25 % anual **o** máx. 500 kg/semana, **incluyendo la venta a consumidor final**)… **el tope de 500 kg incluye el mostrador**, así que **una pastelería que despacha mucho puede pasarse sin haber hecho un solo B2B**» · libro 7: «**Control de Suministro B2B (25 % / 500 kg / 50 km)**… **semáforo de los tres umbrales acumulativos**».

**Problema.** Texto literal del art. 3.1 y 3.2 (verificado en `BOE-A-2022-21681-consolidado.pdf`):

> «1. Los establecimientos de comercio al por menor **sólo podrán suministrar** alimentos de producción propia y productos de origen animal **a establecimientos de comercio al por menor de distinta titularidad** si este suministro es marginal, localizado y restringido…
> 2. Una actividad se considerará marginal cuando: **a)** El suministro… **es inferior o igual al 25 %** del volumen anual…, **o b)** Supone una comercialización total de un máximo de 500 kg a la semana, incluyendo el suministro a consumidor final…»

Dos errores encadenados:

1. **El art. 3 no aplica a quien no suministra a otros minoristas.** Una pastelería con cero B2B nunca entra en el artículo: los 500 kg del mostrador son irrelevantes para ella. La frase «puede pasarse sin haber hecho un solo B2B» describe una trampa que no existe.
2. **a) y b) son alternativas, no umbrales acumulativos.** Basta cumplir **una** para ser marginal. Una pastelería que despacha 900 kg/semana y suministra el 10 % de su volumen anual a la tienda de al lado **sigue siendo marginal por la vía a)**, aunque supere de largo los 500 kg. El research vende el 500 kg como techo duro y ése es justo el sentido contrario del «o».

**Y el defecto baja al entregable.** El libro 7 titula la hoja «25 % / 500 kg / 50 km» y promete un «semáforo de los **tres** umbrales acumulativos». Esos tres no son los tres requisitos: 25 % y 500 kg son **las dos alternativas de UNO** de ellos (marginal), 50 km pertenece a **otro** (localizado, y sólo en el caso interautonómico), y **el tercero —restringido: no suministrar a inscritos en RGSEAA— no aparece en el título de la hoja**. Tal como está especificada, la hoja pondría en rojo a un negocio que la ley considera marginal y no comprobaría el requisito que más fácil se rompe.

**Gravedad: alta.** Es el capítulo 09, es el libro 7 y es el «error nº1 del nicho» que el producto promete corregir. Equivocarse aquí es perder la única autoridad que justifica el precio.

**Fix.** Reescribir PA-02 y §1.2 nº 2 con la estructura real: **tres condiciones acumulativas (marginal · localizado · restringido)**, y **dentro de "marginal", dos vías alternativas**. Añadir la puerta de entrada («esto sólo te aplica si suministras a otros minoristas de distinta titularidad»). Rehacer la hoja del libro 7 como un árbol: ¿suministras a otros minoristas? → no ⇒ no aplica; sí ⇒ tres semáforos (marginal por a) **o** por b) · localizado · restringido) **más** el recordatorio de la declaración responsable y del registro de destinatarios, cantidades y fechas del art. 3.5.

---

### A3 · ALTA — «La tarta de nata por encargo desde casa NO es legal» se publica como afirmación nacional y el art. 13 delega en las CCAA en cuatro puntos

**Afirmación literal (§2.4 nº 2, §1.2 nº 6, §15.2, FAQ 2, cap. 09 y pieza de blog nº 2):** «**la corrección más brutal del research: la tarta de nata por encargo desde casa NO es legal.** Las galletas decoradas y los bizcochos secos, sí. Ninguna de las páginas medidas lo dice» · «Prohíbe **congelar** (13.5.e), prohíbe **colectividades y eventos** (13.5.b)… **lista blanca** de producto (13.8)».

**Problema.** El art. 13 leído entero dice otra cosa. La lista blanca del 13.8 tiene **cinco** letras, y el research sólo publica cuatro:

> «**e)** Otros alimentos que **las autoridades competentes de las comunidades autónomas permitan en sus territorios**.»

Y de las cinco prohibiciones del 13.5 que el research enumera como absolutas, **tres llevan cláusula de escape autonómica**: 13.5.**a)** consumo in situ «salvo que la autoridad competente de la comunidad autónoma lo permita»; 13.5.**c)** suministro en el propio establecimiento, idéntica salvedad; 13.5.**d)** suministro a otros minoristas, «salvo que la autoridad competente… lo permita y establezca los requisitos necesarios». Sólo 13.5.b) (colectividades y eventos) es incondicional. Además, el 13.5.e) que el research cita como «prohibido congelar» continúa: «**Solo se podrán mantener en congelación las materias primas que se adquieran ya congeladas**» — un matiz operativo que cambia la compra de materia prima de un obrador doméstico.

Consecuencia: la afirmación estrella del producto —la que sostiene un capítulo, una respuesta de FAQ, una pieza de blog y el «mejor argumento de criterio»— es **una afirmación de alcance estatal sobre una materia que la propia norma remite a 17 reguladores**, y el research decide en la D6 cubrir **sólo 4 CCAA** «declaradas como ejemplos». No se puede afirmar «no es legal» en toda España desde un cuadro de cuatro comunidades.

**Gravedad: alta.** Es la afirmación más citada del research y la más expuesta: cualquier lector de una CCAA que haya ampliado la lista la refuta con su propio decreto, y el producto se vende precisamente por citar la norma con su artículo.

**Fix.** Publicar la lista blanca con **sus cinco letras**, incluida la 13.8.e). Reformular la afirmación así: «**Por defecto, el RD 1021/2022 sólo permite en vivienda repostería estable a temperatura ambiente: una tarta rellena de nata no entra en la lista del art. 13.8, salvo que tu comunidad autónoma la haya añadido por la vía de la letra e). Comprueba tu decreto autonómico — aquí está cómo.**» Añadir a la hoja «Ruta Doméstica» una **celda verde «¿tu CCAA amplía la lista del 13.8.e)?»** con enlace al registro autonómico, y marcar las tres prohibiciones condicionales del 13.5 como tales.

---

### A4 · ALTA — El fichero del kit que la guía va a CITAR contradice los dos artículos que la guía va a enseñar, y está en producto vendido

**Afirmación literal (§8.1 R4):** «`13-registro-temperaturas-recepcion.xlsx`: … **Vidas Útiles 28×4** (crema pastelera 48-72 h, nata montada 24 h, ganache 5-7 días) | **Prohibido rehacer.** La guía **cita el libro 13**… Lo que sí construye es la **hoja de decisión del huevo** (art. 9: 70 °C/2 s · 63 °C/20 s · ovoproducto)».

**Problema.** He abierto la hoja. Contenido literal, en producto que se vende hoy a 12 €:

| Elaboración | Conservación | Vida útil orientativa |
|---|---|---|
| Crema pastelera | 0 a 4 °C, tapada en contacto | **48 a 72 h** |
| Mousse o bavarois | 0 a 4 °C | **3 días** |
| Merengue italiano | 0 a 4 °C | **3 días** |
| **Tarta montada con nata** | 0 a 4 °C | 24 a 48 h — **«Vitrina a 2-6 °C»** |

Contra el texto literal que el research ya ha verificado:

- **Art. 9.3:** los alimentos elaborados conforme al 1.a) que **no sean estables a temperatura ambiente**, y los del apartado 2 (ovoproducto), «se conservarán a una temperatura igual o inferior a 8 °C y **se consumirán en un máximo de veinticuatro horas** a partir de su elaboración». Crema pastelera, mousse con huevo y merengue italiano caen todos ahí. **La hoja publica de 2 a 3 veces el tope legal.**
- **Art. 4.1 fila 9:** producto de pastelería relleno, **≤4 °C**. La nota de la hoja dice **«Vitrina a 2-6 °C»**, que admite hasta 6 °C.

La hoja lleva descargo («ORIENTATIVAS… la vida útil la fijas tú y debe constar en tu plan de APPCC»), pero el art. 9.3 es un tope, no una recomendación, y la flexibilidad por evidencias científicas del art. 4 no alcanza al plazo del art. 9.3.

**Y la guía nueva lo agrava en vez de corregirlo:** el capítulo 10 y el libro 4 enseñan el art. 9 y el art. 4.1 fila 9 como la prueba de criterio del producto, y la regla R4 manda **remitir al lector a ese mismo fichero**. El comprador de los dos productos leería 24 h en la guía de 65 € y 72 h en la hoja de 12 € del mismo autor.

Es exactamente el patrón que la refutación del Manual del Chef Ejecutivo cazó hace cuatro días con el anisakis (`kit-tareas-sushi-bar/03` y `kit-tareas-marisqueria/03`, −20 °C/7 días donde la ley son 24 h), y que el §15.2 de este research cita como lección — sin comprobar si su propio kit de referencia tiene el mismo defecto.

**Gravedad: alta.** Seguridad alimentaria en producto vendido, en la categoría exacta del producto nuevo, y en el fichero que la guía convierte en cross-sell.

**Fix.** (1) Corregir `13-registro-temperaturas-recepcion.xlsx`: las elaboraciones con huevo bajo art. 9.3 a **24 h** con nota «RD 1021/2022 art. 9.3», y la vitrina a **≤4 °C** con nota «art. 4.1, fila 9». (2) Hasta que esté corregido, **la regla R4 no puede remitir a esa hoja**: la guía construye su propia tabla de vidas útiles legales o no la construye. (3) Añadir al §14.4 del research un bloque «defectos heredados» con este caso, como se hizo con el anisakis.

---

### A5 · MEDIA — «El conflicto 4 °C vs 8 °C… no está resuelto en ningún sitio en español»: no hay conflicto, son dos techos y manda el más bajo

**Afirmación literal (§2.4 nº 4, §1.2 nº 4, libro 4):** «**Las tres vías del huevo** y **la resolución del conflicto 4 °C / 8 °C**: es la decisión técnica que toma un pastelero cada día y **no está resuelta en ningún sitio en español**» · «el art. 9.3 exige ≤8 °C a lo elaborado con huevo: **en una tarta de crema mandan los 4 °C**».

**Problema.** El art. 4.1 fila 9 fija un máximo de 4 °C para el producto relleno; el art. 9.3 fija un máximo de 8 °C para lo elaborado con huevo. **Los dos son techos**, así que cuando concurren se aplica el más estricto por aritmética elemental, no por interpretación. No hay antinomia que resolver ni laguna doctrinal. Vender «la resolución de un conflicto que nadie ha resuelto» sobre dos límites superiores compatibles invita a que el primer técnico de seguridad alimentaria que lea la landing responda en una línea — y el research ya sabe lo caro que sale eso (es el reproche que hace a `qamarero.com` y a `emprendedores.es`).

Lo que **sí** es criterio y el research no destaca: del art. 9.3 lo que aprieta de verdad no es la temperatura, son las **24 horas** de vida útil y la obligación de **registrar fecha y hora de elaboración**. Eso sí cambia la operativa de un obrador y sí lo dice poca gente.

**Gravedad: media.** El argumento sobrevive intacto reformulado, y reformulado es mejor.

**Fix.** Sustituir por: «El art. 4.1 fila 9 y el art. 9.3 son dos topes distintos; **a una tarta de crema le aplican los dos y manda el más bajo, 4 °C**. Y el art. 9.3 añade lo que casi nadie cuenta: **24 horas de vida útil y registro de fecha y hora de elaboración**.» Y en el libro 4, que la hoja devuelva las dos salidas por separado (temperatura y plazo), citando cada una a su artículo.

---

### A6 · MEDIA — «El único "Cómo Montar" que entrega lo que promete es `guia-dark-kitchen`»: promete «+40 páginas» y entrega 27

**Afirmación literal (§16, verificación 1, repetida en §0.2 y §15.3):** «**El único «Cómo Montar» que entrega lo que promete es `guia-dark-kitchen` (24 €, 27 págs / 7.023 palabras).**»

**Problema.** `astro-site/src/data/productos/guias/guia-dark-kitchen.ts:34` publica: «Guía completa PDF + DOCX editable (12 capítulos, **+40 páginas**)». Medido por mí con PyMuPDF: **27 páginas**. Entrega el **67 %** de lo prometido — mucho mejor que el resto de la línea, pero no «lo que promete».

Y hay confirmación interna: `scripts/productos-digitales/CALENDARIO-V2-SEMANAL.md:201` programa **«S10 · 2 – 8 nov | guia-dark-kitchen (+ documentos +40 págs)»**. El propio calendario del proyecto sabe que dark-kitchen debe páginas. La verificación nº 1 —presentada como la corrección grave a L6, la que sostiene D2 y D3— contiene una afirmación que el calendario del repo refuta.

**Gravedad: media.** No cambia el sentido de la conclusión (la línea está rota), pero es la única excepción que el research declara y no resiste un `grep`. Si entra en una decisión de John presentada como «lo verificado», es un precedente malo.

**Fix.** «Ninguna guía de la línea entrega lo prometido. La menos lejos es `guia-dark-kitchen`: **27 páginas de las "+40" que anuncia (67 %)**; el resto va del 4 % al 17 %.»

---

### A7 · MEDIA — El PDF de 1 página no es un producto vacío: es una portada deliberada que remite al DOCX, y eso cambia el diagnóstico y el coste de D2

**Afirmación literal (§16 verificación 1 y §15.3 R1):** «`guia-panaderia-obrador` **1 pág / 55 palabras**… **6 de los 8 productos de la franja 65-85 € están vacíos**» · «**La línea de 65 € entrega un 5-13 % de lo que promete**».

**Problema.** He extraído el texto de esa única página. Dice, literalmente:

> «Cómo Montar una Panadería con Obrador · Guía Premium España 2026 — Modelo Artesanal con Masa Madre · **Para la guía completa en formato editable, descarga el archivo DOCX: guia-panaderia-obrador.docx** · 20 capítulos · 70+ páginas · Recetario · Plan financiero · 9 plantillas Excel + 6 checklists + Business Plan + Manual Obrador · AI Chef Pro · aichef.pro»

No es un PDF roto ni un producto vacío: es una **portada-puntero por diseño**. El entregable real es el DOCX, y ahí hay **4.699 palabras** (≈9 páginas a la calibración medida), no 55. El defecto sigue siendo grave —9 páginas contra «70+»— pero es **de longitud, no de existencia**, y eso mueve dos decisiones:

- **D2** («arreglar antes **retrasa el lanzamiento meses**, porque son 6 productos») está costeada sobre la hipótesis de escribir seis guías desde cero. Si hay 2.900-6.300 palabras ya escritas por producto, el trabajo es de **ampliación**, que es lo que el calendario ya presupuesta a 1,5-1,8 M por guía en S4-S9 (21-sep → 1-nov). El research cita ese calendario en la misma D2 sin conciliarlo con su propia estimación de «meses».
- **La conclusión de portada** («6 de 8 vacíos») describe mal el estado a quien tiene que decidir.

Añadido: la franja 65-85 € son 8 productos, pero uno es el **Manual del Chef Ejecutivo (96 págs, correcto)**. La frase honesta es «**7 de los 8 productos de la franja quedan por debajo de lo que anuncian; el octavo, el Manual del Chef Ejecutivo, cumple**».

**Gravedad: media.**

**Fix.** Reescribir la verificación 1 con las tres cifras que importan por producto: **páginas prometidas en la landing · palabras del DOCX · páginas del PDF**, y decir que el PDF es una portada por diseño. Recostear D2 sobre «ampliar 6 DOCX existentes», que es lo que el calendario ya tiene planificado.

---

### A8 · MEDIA — Dos keywords se clasifican por intención sin haber medido su SERP, que es el error que el propio research prohíbe

**Afirmación literal (§0):** en el bloque «Genérico de CONSUMIDOR (no es nuestro)» figura **`chocolateria` 9.900**; y entre «Las cuatro con intención pura» figura **`requisitos obrador pasteleria` 30**.

**Problema.** La tabla «Resumen de bloques SERP» de `L2:262-274` tiene **11 filas**, y:

- **`chocolateria` viene marcada «*(no medida)*»** en todas sus columnas (AIO, PAA, local pack, vídeo) y clasificada «Local ❌» sin ninguna medición.
- **`requisitos obrador pasteleria` no está en la tabla**: L2 nunca abrió su SERP. La síntesis la promueve a «intención pura» y la suma al clúster de captación.

El §0.2 del research y la memoria del proyecto dicen exactamente lo contrario de lo que aquí se hace: «**El volumen sin SERP engaña**… Correr siempre `serp` antes de decidir el enfoque, no sólo `vol`». Y en el caso de `chocolateria` importa el doble: **«Cómo Montar una Chocolatería · Junio 2026» es la OTRA tarjeta de `comingSoon`** (`ProductosDigitales.tsx:943`), así que descartar su SERP sin medirla prejuzga el research del producto siguiente.

**Gravedad: media.**

**Fix.** Marcar las dos como «sin SERP medida» en la tabla del §0 y no usarlas en ninguna conclusión de intención. Medir las dos SERP antes de cerrar la SPEC — son dos llamadas a `scripts/dataforseo.py serp` y cuestan minutos.

---

### A9 · MEDIA — El filtro «local pack + sin AI Overview = no es nuestra» tiene un contraejemplo dentro de su propia tabla, y el research lo desobedece cuatro secciones después

**Afirmación literal (§0, lectura 2):** «**L2 descubrió y validó un filtro barato en 10 SERP: LOCAL PACK presente + AI OVERVIEW ausente = la consulta NO es nuestra.** … Es el clasificador más barato para cualquier keyword nueva del nicho.»

**Problema.** En la misma tabla de L2, **`franquicias de pasteleria` (40/mes) tiene local pack (9) y NO tiene AI Overview**, y L2 la clasifica «**Comercial apertura**». Es decir: una consulta de intención de apertura que el filtro mandaría descartar. Y el propio research la convierte cuatro secciones después en la **pieza de captación nº 4** del §13.4 («Franquicia de pastelería vs marca propia»).

Además, «validado en 10 SERP» describe mal lo hecho: la regla se **deriva** de esas mismas 10 observaciones, sin ninguna consulta reservada para comprobarla. Con n=10, una excepción declarada y cero validación fuera de muestra, es una **heurística útil**, no un clasificador validado.

**Gravedad: media.** Un filtro presentado como validado se usará para descartar keywords sin abrir la SERP — que es la práctica que este research existe para evitar.

**Fix.** Degradar la frase a: «**heurística observada en 10 SERP, con una excepción conocida (`franquicias de pasteleria`): el local pack sin AI Overview es señal de consulta local, no prueba.** Ante la duda, abrir la SERP.» Y en el §13.4, decir por qué la pieza 4 se escribe pese a caer del lado «no nuestro» del filtro (es contenido de decisión para quien ya nos lee, como el propio research reconoce).

---

### A10 · MEDIA — «Las cuatro con intención pura» son cinco, y las cuatro con AI Overview son otras cuatro

**Afirmación literal (§0):** fila «Las cuatro con intención pura | `obrador compartido` **50** · `requisitos para montar un obrador en casa` **30** · `requisitos obrador pasteleria` **30** · `montar una pasteleria en casa` **20** · `vender reposteria desde casa españa` **20** | **~150**».

**Problema.** La fila etiquetada «las cuatro» enumera **cinco** keywords. Y dos líneas más abajo, la lectura 2 nombra «**las cuatro únicas SERP con AI Overview**» y lista **otras cuatro**: `requisitos para montar un obrador en casa`, `montar una pasteleria en casa`, `vender reposteria desde casa españa` y `obrador compartido` — es decir, el conjunto de cinco menos `requisitos obrador pasteleria`, que es justamente la que no tiene SERP medida (A8). El «~150» sí suma bien las cinco.

Y el §13.4 usa un tercer conjunto: «~**120**/mes agregado (30+30+20+20+20)», cinco sumandos que no coinciden con los cinco de la fila (falta el 50 de `obrador compartido` y sobra un 20 sin identificar).

**Gravedad: media.** Es el bloque de demanda, va al brief del guion y a la justificación de las piezas de blog. Tres recuentos distintos del mismo clúster en un documento cuya tesis es que los demás no cuentan bien.

**Fix.** Una sola tabla del clúster de apertura con una fila por keyword, su volumen, si su SERP está medida y si tiene AIO; y que todos los agregados del documento se calculen de ahí.

---

### A11 · MEDIA — PS-58 y PS-60 implican márgenes del 71 % y del 80 %, incompatibles entre sí y con la «regla única» PS-55/56 que el research declara

**Afirmación literal (§3.1):** «**PS-55/56 — Regla de margen (UNA sola, dos lecturas)**: margen bruto **65-70 %** ⇔ food cost **<30-35 %**» · «**PS-58** — fijos de **5.000 €/mes** ⇒ facturación **~7.200 €/mes**» · «**PS-60** — pequeña **5.000 → 7.000 €** · mediana **8.000 → 10.000 €** · grande **12.000 → 15.000 €**».

**Problema.** El punto muerto es fijos ÷ margen. Despejando el margen que cada cifra implica:

| id | Fijos | Facturación de equilibrio | Margen implícito |
|---|---|---|---|
| PS-58 | 5.000 € | 7.200 € | **69,4 %** ✓ dentro de PS-55/56 |
| PS-60 pequeña | 5.000 € | 7.000 € | **71,4 %** ✗ |
| PS-60 mediana | 8.000 € | 10.000 € | **80,0 %** ✗✗ |
| PS-60 grande | 12.000 € | 15.000 € | **80,0 %** ✗✗ |

**PS-60 no es coherente ni consigo mismo ni con la regla de margen que el research acaba de declarar única.** Con el 65-70 % de PS-55/56, unos fijos de 8.000 € necesitan **11.400-12.300 €** de facturación, no 10.000. El research marca PS-60 como «escenario editable, nunca benchmark» por no citar fuente primaria, pero **no ve la incoherencia aritmética**, y los tres ids (PS-58, PS-60, PS-55/56) entran juntos al capítulo 18 y al libro 5.

**Gravedad: media.** Si el guion redacta el capítulo 18 con PS-58 y PS-60 en la misma página, publica dos reglas de margen que se contradicen — el mismo error de método que el §15.2 prohíbe («Presentar "margen 65-70 %" y "food cost <30-35 %" como dos reglas»).

**Fix.** Retirar PS-60 de las cifras citables y dejarlo como lo que es: tres pares (fijos, facturación) publicados por un tercero **cuyo margen implícito es del 71-80 %, incompatible con el 65-70 % del sector**. El capítulo 18 calcula el punto muerto con la regla única y muestra PS-58 como el único par publicado que cuadra.

---

### A12 · MEDIA — «Un obrador artesano factura 84.000-180.000 €/año» son cifras de PUNTO MUERTO, no de facturación, y con ellas se tumba N-2

**Afirmación literal (§15.1, N-2):** «🚨 «**Facturación media anual por pastelería: 1,08 millones de euros**»… **La más peligrosa del research.** Contradice a PS-48/57/60 por un factor de **6 a 12** (**un obrador artesano factura 84.000-180.000 €/año**).»

**Problema.** El rango «84.000-180.000 €/año» no está en ninguna fuente: sale de multiplicar por 12 las dos cifras de equilibrio del §3.1 — PS-58 (7.200 × 12 = 86.400) y PS-60 grande (15.000 × 12 = 180.000). Y el factor «6 a 12» lo confirma: 1.080.000/180.000 = 6,0 y 1.080.000/86.400 = 12,5.

Son **umbrales de beneficio cero**, no facturación media. Presentarlos como «lo que factura un obrador artesano» convierte el suelo en el techo: un negocio que facture exactamente 86.400 € no gana nada, y el propio research afirma que la rentabilidad neta «yendo bien» es del 8-12 % (PS-48), lo que exige facturar bastante por encima del punto muerto.

Además, las cifras que el propio research trae del sector apuntan mucho más arriba: Levaduramadre **49,3 M€ / 167 tiendas ≈ 295.000 € por tienda** y Manolo Bakes **33,5 M€ / >50 locales ≈ 670.000 €**. N-2 se rechaza correctamente por no tener fuente primaria; el argumento aritmético con el que se refuerza es el que falla.

**Gravedad: media.** N-2 va al `cifras_ignorar` del guion, y su justificación se copiará al capítulo 18 y a la landing.

**Fix.** Dejar N-2 rechazada por lo que la tumba de verdad —blog sin fuente primaria, contenido de granja de IA— y borrar el rango inventado. Si se quiere un contraste, usar los datos con nombre que sí hay: «Levaduramadre declara 49,3 M€ en 167 tiendas (≈295.000 €/tienda) y Manolo Bakes 33,5 M€ en más de 50 locales».

---

### A13 · BAJA — El «5-13 % de lo que promete» no se recompone con ninguna de las mediciones publicadas

**Afirmación literal (§15.3, R1):** «🔴 **La línea de 65 € entrega un 5-13 % de lo que promete**».

**Problema.** Con las cifras del propio research y la calibración de 529 pal/pág:

- Por PDF: panadería 55 pal contra ~37.000 = **0,15 %**; gastronómico 2.488 contra ~62.900 = **4,0 %**. Rango 0,15-4 %.
- Por DOCX (que es el entregable real, ver A7): gastronómico 2.395/119 págs = **3,8 %**; nikkei 6.317/70 págs = **17,1 %**. Rango 3,8-17,1 %.

Ni uno ni otro da 5-13 %.

**Gravedad: baja**, pero es una cifra de portada en un riesgo marcado en rojo.

**Fix.** «Las seis guías de la línea entregan entre el **4 % y el 17 %** de las páginas que anuncian (medido sobre el DOCX, que es el entregable real).»

---

### A14 · BAJA — La regla de los 30 días no está en el art. 20 del TRLGDCU

**Afirmación literal (§11.2):** «**Sin `priceOld` ni `discountBadge`** (decisión D2 de la familia: producto nuevo, sin «precio anterior de 30 días» que sostenga un tachado — **art. 20 TRLGDCU / RDL 24/2021**).»

**Problema.** Verificado en el texto consolidado de la **Ley 7/1996, de Ordenación del Comercio Minorista** (`BOE-A-1996-1072`), **art. 20 «Constancia de la reducción de precios»**: «Se entenderá por precio anterior **el menor que hubiese sido aplicado sobre productos idénticos en los treinta días precedentes**». El RDL 24/2021 es la norma que introdujo esa redacción **en la Ley 7/1996**, no en el TRLGDCU, cuyo art. 20 regula la información necesaria en la oferta comercial.

**Gravedad: baja** — la decisión es correcta, la norma citada no. Pero es un producto que se vende por citar bien las normas y esta cita viaja a la SPEC y de ahí a la familia.

**Fix.** «art. 20 de la Ley 7/1996 de Ordenación del Comercio Minorista, en la redacción dada por el RDL 24/2021».

---

### A15 · BAJA — La exención de los 1.300 m² de la Ley 1/2025 sólo alcanza al apartado 4 del art. 6

**Afirmación literal (§15.2 y cap. 19):** «"La **Ley 1/2025** te obliga a un plan de prevención" — **no** si eres microempresa o ≤1.300 m²» · «**por qué tu pastelería está exenta del plan**».

**Problema.** El art. 6.4.c) literal empieza: «**Quedan exceptuadas de las obligaciones del presente apartado cuatro** las actividades de transformación, comercio minorista…». La exención por superficie alcanza **sólo al apartado 4** (plan de aplicación y promoción de convenios de donación). Siguen obligando al que no sea microempresa: el **6.2** (aplicar el art. 19 de la Ley 7/2022), el **6.3** (nulidad de cláusulas que impidan donar) y el **6.5** (no dejar alimentos no aptos deliberadamente). Sólo el **6.6** (microempresas) exime del artículo entero.

**Gravedad: baja** (la conclusión sobre el plan es correcta), pero es el matiz que justifica el precio, y es el mismo hallazgo A11 de la refutación del Manual del Chef Ejecutivo, repetido cuatro días después.

**Fix.** «Estás exento **del plan de prevención (art. 6.4)** si tu superficie no pasa de 1.300 m²; si además eres microempresa, quedas fuera de todo el art. 6. Lo que sigue obligándote en los dos casos es el 6.2, el 6.3 y el 6.5.»

---

## B — NEGOCIO

### B1 · ALTA — D12 (adelantar el correo al 19 o 24 de septiembre) es incompatible con D14 (dos sesiones) y con el calendario publicado

**Afirmación literal (D12, y §13.3):** «**Adelantarlo**, con el precedente literal de la D28 del Chef Ejecutivo… Si se repite, la pastelería saldría el **19-sep** o el **24-sep** y todo lo demás corre un hueco.» · (D14) «**¿Se parte la construcción en DOS sesiones?** **Sí.** 12-16 M no caben en una semana… **Su coste: Alarga el lanzamiento una semana.**»

**Problema.** Las dos decisiones no pueden ser verdad a la vez, y el calendario lo demuestra:

| Semana | Ya asignada a | Presupuesto |
|---|---|---|
| **S3 · 14-20 sep** | plan-negocio-food-truck · kit-tareas-sushi-bar | 1,5 M |
| **S4 · 21-27 sep** | guia-restaurante-casual (+ documentos) | 1,5 M |
| **S5 · 28 sep-4 oct** | guia-restaurante-mexicano | 1,5 M |

(`CALENDARIO-V2-SEMANAL.md:196-198`.) Un correo el **19-sep** exige el producto LIVE ese lunes, es decir, terminar A2+B1+B2+C **dentro de S3**, que está ocupada y presupuestada a 1,5 M frente a los 12-16 M del producto. El **24-sep** cae en S4, igual. Y la regla de la propia hoja (`:208`) — «**Las semanas con producto nuevo van INTERCALADAS: cuando toque una, la v2.0 de esa semana se salta**» — significa que dos sesiones de pastelería **no alargan el lanzamiento una semana: consumen dos semanas del programa y desplazan dos entregas de v2.0**, con efecto en cascada sobre S4-S17.

Además, el coste declarado en D14 («alarga el lanzamiento una semana») subestima: entre dos sesiones de producto va, por la regla de alternancia, una sesión impar de v2.0. Dos sesiones de producto son **tres semanas naturales como mínimo**, lo que sitúa el LIVE a primeros de octubre — coherente con el hueco de Resend del **14-oct** que el propio §13.3 identifica, e incoherente con D12.

**Gravedad: alta.** Es el tipo de decisión que, tomada mal, deja un producto a medias en la tercera sesión — precedente vivo: la Guía Gastronómica v2.0, «a medio camino», con tres documentos sin publicar.

**Fix.** Retirar D12 o reescribirla con su coste real. La recomendación defendible es: **mantener el hueco del 14-oct**, ocupar S3 con A2+B1 (saltando su v2.0), S5 con B2+C, y dejar S4 intacta. Y corregir el coste de D14: «dos semanas del programa de v2.0, no una».

---

### B2 · ALTA — El presupuesto queda por debajo del único precedente medido, para un paquete objetivamente mayor

**Afirmación literal (§15.4):** «**TOTAL 12,0-16,0 M**… **Este producto es el más caro de la serie por entregables** —10 libros frente a los 7 del Chef, y **tres sin molde previo**— aunque **mi estimación queda ligeramente por debajo de la de L6 (13,5-17,5 M) porque el pipeline ya no necesita arreglos**.»

**Problema.** El único dato medido de un producto de esta forma es el Manual del Chef Ejecutivo, y desmiente la estimación:

| | Chef Ejecutivo (**medido**) | Pastelería (**estimado**) |
|---|---|---|
| xlsx | **7** | **10** (3 sin molde previo) |
| Documento principal | 96 págs / 52.203 pal | 78-86 págs |
| Bonus | 34 págs / 15.762 pal | 28-32 págs **+ business plan** |
| Redactores | **56** bloques, **7,7 M** | «~44» bloques, **5,5-7,0 M** |
| Research | **2,1 M** | 1,5-2,0 M |
| Resto (xlsx + landing + gates) | **≈7,2 M** (17 − 2,1 − 7,7) | **3,5-5,0 M** (B1 2,5-3,5 + C 1,0-1,5) |
| **Total** | **≈17 M** | **12-16 M** |

Fuentes: `SESSION_HANDOFF_2026-09-06-manual-chef-ejecutivo.md:15` y `:21`; `CALENDARIO-V2-SEMANAL.md:130` («Coste ≈ 17 M tokens de subagentes»).

**Se propone hacer más con menos.** El bloque de xlsx —el que crece de 7 a 10 con tres moldes nuevos— se estima en **la mitad** de lo que costó el equivalente más pequeño. Y la justificación («el pipeline ya no necesita arreglos») cubre una parte pequeña: el arreglo de `repartir_puntos()` ya está commiteado (`3c1444d`), pero eso no explica un ahorro de 2-3 M en construcción de libros.

Y la escala, dicha en voz alta: el programa completo de v2.0 de **17 semanas** (S1 a S17, hasta el 27-dic) suma **≈24,5 M** de presupuesto. **Este producto solo se llevaría entre la mitad y los dos tercios de todo ese programa.**

**Gravedad: alta.** Es la decisión que más le cuesta a John si se toma mal, y la que su regla del 29-ago existe para proteger.

**Fix.** Poner tres escenarios con su coste y su calendario **antes** de arrancar, no a mitad: **(a)** alcance completo, 16-19 M realistas, dos o tres sesiones; **(b)** alcance recortado que sí quepa en dos — **8 libros** fundiendo `mix-de-canales` dentro de `plan-financiero` y `cronograma-gantt` dentro de `checklist-legal`, y el bonus 2 a 8 decisiones en vez de 12: ≈10-12 M; **(c)** aplazarlo y ocupar el ciclo con un producto más barato. Y corregir el «~44 redactores» a la baremación real (ver C7).

---

### B3 · ALTA — El «hueco limpio entre 49 € y 357 € que no ocupa nadie» lo ocupa un producto de 147 € que L1 sí declara, y el suelo de 49 € es una oferta que caducó el 13-sep-2026

**Afirmación literal (§7.2 H2 y §11.2 argumento 4):** «**Hay un agujero de precio limpio entre 49 € y 357 €, y nadie lo ocupa**… **Entre 49 € y 357 € sólo hay técnica y plantillas sueltas.**» · «**El hueco de mercado está entre 49 € y 357 € y no lo ocupa nadie.** A 65 € somos **1,33×** el software de plan de negocio (49 €)».

**Problema.** Dos cosas, las dos en la propia L1:

1. **L1 lo escribió con el matiz y la síntesis lo borró.** `L1:152`: «Entre **49 € y 357 €** sólo hay técnica **(147 €)** y plantillas sueltas sin precio público». El «Pack Técnico Completo» de Pastelería Para Todos son **147 €** (`L1:58`, checkout `pay.hotmart.com/M106768436M`, consultado 2026-09-09) y está **dentro del hueco**. La H2 lo lista en su propia escala ordenada tres líneas antes de declarar que nadie lo ocupa.
2. **El ancla de 49 € tiene fecha de caducidad y ya venció.** `L1:56`: plandenegocio.es, «**49 €** (antes tachado **147 €**; oferta declarada «**válida hasta 13-sep-2026**»)». El producto se lanzaría en octubre. A partir del 14-sep el precio de referencia del competidor es **147 €**, y entonces el argumento «somos 1,33× el software de plan de negocio» desaparece: pasamos a ser **0,44×**, lo cual es mejor argumento comercial pero **otro argumento**. Ironía menor: el research prohíbe el `priceOld` propio por la regla de los 30 días y usa el precio promocional de un competidor como suelo de mercado.

Y una corrección de encuadre: `L1:206` declara ese software como «**el suelo**» y detalla que trae «business plan + presupuesto a 5 años + **2 escenarios** + **DSCR** + licencia de por vida». Es un competidor directo del **libro 5**, no un producto de otra categoría.

**Gravedad: alta.** Es el argumento nº 4 de los seis que sostienen el precio de 65 €, y es el que se copia literal a la landing.

**Fix.** Reescribir H2 y el argumento 4: «**Entre 49 € y 357 € hay un único producto, un pack de técnica pastelera de 147 € sin nada de gestión. No hay ningún producto documental de apertura en esa franja.**» Y **re-consultar el precio de plandenegocio.es antes de escribir el copy** (la oferta vencía el 13-sep): si ha vuelto a 147 €, el argumento se reescribe entero y mejora.

---

### B4 · MEDIA — La plantilla del juego de datos hace inviables los costes fijos que el propio research publica

**Afirmación literal (§9.1 y §3.1):** «Plantilla | **Jefe pastelero · 1 oficial · 1 ayudante · 2 dependientes (1 a tiempo parcial)**» · «**PS-61** — Desglose de fijos mensuales: alquiler 1.200-3.000 · suministros 600-1.200 · **personal 2-5 empleados 2.000-6.000** · seguros y gestoría 300-700 · marketing 200-500 · reposición 1.000-2.000 → **5.000-12.000 €/mes**».

**Problema.** «La Clara» son 4,5 jornadas completas. Con las tablas del convenio de Madrid que el propio research verifica (PA-33: **15 pagas**, grupos 1.733,88 / 1.427,89 / 1.376,91 / 1.249,42 / 1.192,42 €/mes):

- Jefe pastelero 1.427,89 × 15 = 21.418 € · oficial 1.376,91 × 15 = 20.654 € · ayudante 1.249,42 × 15 = 18.741 € · dependiente 1.192,42 × 15 = 17.886 € · dependiente a media jornada = 8.943 €
- **Bruto anual ≈ 87.642 €**; con SS a cargo de la empresa (~32 %) ≈ **115.700 €/año ≈ 9.640 €/mes**

**Sólo el personal se come el 80 % del techo (12.000 €) de TODO el rango de fijos de PS-61, cuya línea de personal para 2-5 empleados es de 2.000-6.000 €.** Sumando alquiler, suministros, gestoría, marketing y reposición, los fijos reales de La Clara rondan **13.000-14.000 €/mes**, fuera del rango publicado; y su punto muerto al 67,5 % de margen sale en **≈19.500 €/mes ≈ 234.000 €/año**, que no cabe en ninguno de los escenarios de PS-60 (máximo 15.000 €/mes) ni en el rango «84.000-180.000 €/año» con el que se refuta N-2 (ver A12).

**Gravedad: media.** El juego de datos único es la columna vertebral: los 10 libros, el guion y los dos bonus beben de él. Si el caso modelo no cuadra con los benchmarks que el mismo producto publica, cualquier lector con una calculadora lo ve.

**Fix.** Elegir una de dos, y declararlo: **(a)** bajar «La Clara» a 3-3,5 jornadas (jefe + ayudante + 1,5 dependientes), que sí cabe en PS-61 y sigue casando con los 4 perfiles del kit; o **(b)** mantener las 4,5 jornadas y **retirar PS-61 y PS-60 de las cifras citables**, sustituyéndolos por el desglose que produce el propio libro 10 con el convenio en celda verde. En cualquier caso, el capítulo 13 debe mostrar el salto bruto → coste empresa: es el dato que más sorprende al lector y el research ya lo tiene.

---

### B5 · MEDIA — Cuatro de los diez libros dependen de datos que viven en el kit de 12 €, y no se dice qué ve el comprador que no lo tiene

**Afirmación literal (§8.1, regla transversal):** «*cero fórmulas entre libros y cero duplicación de tabla operativa; cuando la guía necesita un dato que vive en el kit, lleva una **celda verde** con la nota «**cópialo de tu `10-plan-produccion-semanal.xlsx`**».*»

**Problema.** La regla resuelve bien la canibalización, pero crea un problema comercial que el research no aborda: **el comprador de la guía de 65 € que no tiene el kit de 12 € se encuentra celdas verdes que le piden un fichero que no posee.** Afecta al menos a los libros 3 (capacidad vs demanda del pico), 4 (referencias precargadas del `12-control-alergenos-vitrina`), 6 (encargos) y 10 (perfiles). Y el research vende expresamente el producto **a quien AÚN no ha abierto** (persona B, FAQ 4), es decir, a quien por definición **no tiene datos históricos de producción** que copiar de ninguna parte.

Peor: la landing promete «los diez Excel que hacen tus números» (§12.2) y enumerarlos uno a uno como argumento de venta (§7.3). Un libro cuya celda de entrada remite a otro producto no «hace tus números».

**Gravedad: media.** Es una fuente clásica de devolución y contradice la promesa de la primera pantalla.

**Fix.** Que **cada celda verde de este tipo traiga un valor por defecto propio y declarado como supuesto**, con la nota «si ya tienes el Kit de Tareas Pastelería, sustitúyelo por tu dato real de `10-plan-produccion-semanal.xlsx`». Ninguna celda de entrada puede quedar vacía por depender de otro producto. Y verificarlo con un gate: **cero celdas verdes sin valor por defecto** en los 10 libros.

---

### B6 · MEDIA — El nombre doble se aprueba en D18 citando en la misma página la regla que lo prohíbe, y sin gate

**Afirmación literal (§12.1 y D18):** «⚠️ **Y un aviso de nomenclatura que ya costó dinero en este repo:** el nombre del enlace debe coincidir con el de la página de destino… o repetimos el defecto de «Biblioteca de Prompts» → `/libreria-de-prompts`.» · (D18) «**Los dos**… Su coste: **Dos nombres para lo mismo exige cuidado** en el hub y en el footer.»

**Problema.** El research identifica el defecto, lo documenta con su precedente, y a continuación recomienda la configuración que lo produce: **H1 «Cómo Montar una Pastelería» + nombre de catálogo «Guía Pastelería con Obrador»**. Esos dos nombres viajarían simultáneamente a: la tarjeta del hub (dos ficheros), el `products-catalog.ts` que alimenta los banners de los 325 posts, el `footerLinks` de cuatro fichas de producto, el asunto del broadcast de Resend y el `emailBody` post-pago. La mitigación propuesta es «cuidado», que es exactamente lo que falló con «Biblioteca de Prompts».

**Gravedad: media.**

**Fix.** Elegir **un** nombre visible. Recomiendo **«Cómo Montar una Pastelería»** en todo lo que ve el usuario —es la promesa publicada desde mayo y lo que el buscador del hub sugiere— y usar «con obrador» sólo como subtítulo, no como nombre alternativo. Si John prefiere los dos, entonces D18 necesita un **gate**, no cuidado: un script que compruebe que el `name` del catálogo, el `<h1>` de la landing, el texto del banner y el asunto del correo coinciden.

---

### B7 · BAJA — El estado de la cola de Resend que el research dice haber verificado ya está desactualizado en el propio calendario

**Afirmación literal (§13.3):** «| 9-oct | Food truck 2.2 | **BORRADOR** (Resend no admite > 30 días vista) |»

**Problema.** `CALENDARIO-V2-SEMANAL.md:130-131` ya recoge: «✅ **PROGRAMADO el 10-sep** (`POST /broadcasts/{id}/send` con `scheduled_at`, aprobado por John…)». El research declara honestamente en §16 que «**No consulté Resend**: el hueco del 14-oct es una previsión sobre lo documentado en el calendario, no un hueco confirmado» — pero la tabla del §13.3 lo presenta como «verificada por mí».

**Gravedad: baja.** No cambia la conclusión (el 14-oct sigue libre), pero una tabla marcada como verificada que ya no coincide con el fichero del que sale es la clase de dato que se arrastra.

**Fix.** Actualizar la fila a «9-oct · Food truck 2.2 · **programado el 10-sep**» y mantener el 14-oct como **previsión**, con la nota de que hay que confirmarlo en Resend a partir del 14-sep.

---

## C — PRODUCTO

### C1 · ALTA — Nada ata `paginas_prometidas` al número que publica la landing, y ése es exactamente el mecanismo que produjo la línea rota

**Afirmación literal (§10 y §8.4):** «Gate interno: `paginas_prometidas: 70` · `min_palabras_cap: 1.300` | Qué publica la landing: **La cifra MEDIDA tras construir** (decisión D17 de la familia). Nunca la prometida» · «`GUIA['gates']` acepta `paginas_prometidas`… **Cero cambios de código.**»

**Problema.** El gate existe y funciona —lo he verificado: `documentos.py:1997` evalúa `'paginas': doc_pdf.page_count >= cfg['paginas_prometidas']`—, pero **no está conectado con la promesa que ve el comprador**, y eso ya ha fallado en producción:

| Fuente | Dice |
|---|---|
| `guion_guia_restaurante_gastronomico.py:70` | `'paginas_prometidas': 80` |
| `astro-site/src/data/productos/guias/guia-restaurante-gastronomico.ts:13,23,25,151` | «22 capítulos, **119 páginas**» |
| PDF servido en `dl/`, medido por mí | **10 páginas** |

Tres números distintos en tres ficheros que nadie compara. Y `censo-entregables.py` —el gate de catálogo— **no mira páginas** (cero coincidencias de `page_count` o `páginas`). Es decir: **el defecto que el research dedica su verificación nº 1 a denunciar no lo causó la falta de un gate de construcción, sino la falta de un gate que ate el fichero de datos de la landing con el PDF servido.** El research propone repetir el mismo montaje (`paginas_prometidas: 70`, salida real 78-86, landing con «la cifra medida») **sin proponer ese gate**.

**Gravedad: alta.** Es la única garantía barata de no repetir el problema, y el producto nuevo nace precisamente vendiéndose como «el primero de la línea que entrega lo que promete».

**Fix.** Añadir a la fase C un gate de **cuatro líneas** que, para cada producto con PDF en `dl/`, extraiga con PyMuPDF el `page_count` real, extraiga con un regex el número de páginas anunciado en `astro-site/src/data/productos/**/*.ts` y **aborte si el anunciado supera al real**. Correrlo sobre los 9 productos actuales antes de publicar el 48 (dará 7 fallos, que es el mapa exacto del trabajo de D2) y dejarlo en la batería junto a `robots-gate.py` y `whatsapp-gate.py`.

---

### C2 · MEDIA — La hoja «Ruta Doméstica» pone el contador en el límite que casi nadie alcanza y omite el que de verdad ata

**Afirmación literal (§9.2, libro 7):** «**Ruta Doméstica (lista blanca + contador de 100 kg/semana)**… kg elaborados en vivienda… **alerta al superar 100 kg/semana**».

**Problema.** El art. 13.9 completo dice: «El volumen total de alimentos preparados **deberá ser proporcional al tamaño de las instalaciones** de manera que se garanticen unas prácticas correctas de higiene alimentaria **y en ningún caso** podrán superar los 100 kilogramos semanales, lo cual se demostrará documentalmente.»

Son **dos** límites, y el que ata a una cocina doméstica real es el primero. 100 kg/semana son ~14 kg/día: una repostera con un horno doméstico y 4 m² útiles no llega ni de lejos, así que **el contador estaría siempre en verde mientras el requisito que sí puede incumplir —la proporcionalidad— no se comprueba en ninguna parte**. Además, la hoja no recoge la tercera obligación del mismo apartado: **demostrarlo documentalmente**, que es lo que pide un inspector.

Y la lista blanca de la hoja hereda el problema de A3: le falta la letra e) del 13.8.

**Gravedad: media.** Es la hoja que sirve a la buyer persona A, la del segmento con más búsqueda del nicho.

**Fix.** Tres entradas en celda verde (m² útiles dedicados · kg/semana · ¿registro documental sí/no?) y tres salidas: semáforo de los 100 kg, **semáforo de proporcionalidad** (kg por m² útil, con el umbral declarado como criterio propio y no como norma) y **aviso de "demostrable documentalmente"** con la lista de lo que hay que guardar. Más la celda de la letra e) autonómica.

---

### C3 · MEDIA — V-03, declarado bloqueante de capítulo, ya está resuelto: el texto está en el MISMO PDF que L3 descargó, y verificado en este directorio hace cuatro días

**Afirmación literal (§2.5 y riesgo 5):** «**V-03** | **Art. 30 del RD 1086/2020** (comidas preparadas) | 🔴 **ABIERTA.** Es la puerta de toda la variante pastelería-cafetería. **No escribir ese capítulo sin leerlo**» · (D4) «La **pastelería-cafetería** abre un frente entero (art. 30 del RD 1086/2020…) y **puede añadir 1,5-2 M de tokens**».

**Problema.** El art. 30 del RD 1086/2020, en su redacción vigente, **está dentro de `BOE-A-2022-21681-consolidado.pdf`** —el mismo fichero que L3 descargó y extrajo con `pypdf` para obtener los artículos 3, 4, 9 y 13—, porque es la D.F. del RD 1021/2022 la que le da su redacción actual («Doce. El artículo 30 queda redactado del siguiente modo…»). Lo he extraído en dos minutos, con sus 11 apartados: mantenimiento en caliente **≥63 °C** (30.2), refrigeradas **≤4 °C** si vida útil >24 h y **≤8 °C** si <24 h (30.3), congeladas **≤−18 °C** (30.4), temperaturas alternativas con evidencias científicas (30.5), **60 → 10 °C en menos de 2 h** (30.6), recalentado **≥74 °C durante ≥15 s** con equivalencias admitidas (30.7), y comidas testigo (30.8-30.11, umbral de encargos «**de más de 40 personas**», ≥100 g, ≥7 días, ≤4 °C o ≤−18 °C).

Y hay una segunda fuente en casa: **`manual-chef-ejecutivo-research-REFUTACION-2026-09-06.md`, hallazgo A3**, ya cita ese artículo literal y completo, verificado contra el BOE hace cuatro días, en este mismo directorio.

**Gravedad: media.** No es un error de contenido, es trabajo que se está reservando dos veces y una decisión (D4) costeada sobre una incertidumbre que no existe.

**Fix.** Cerrar V-03 con el texto ya extraído, meterlo como `PA-16b` a nivel A, y **recostear D4**: la variante pastelería-cafetería no abre un frente normativo nuevo, hereda un artículo ya verificado. Lo que sí queda abierto de esa variante es el convenio y el IVA (V-02), no el art. 30.

---

### C4 · MEDIA — La FAQ 10 justifica la lista de fórmulas prohibidas con una razón falsa que el comprador refuta en treinta segundos

**Afirmación literal (FAQ 10):** «**¿Los Excel funcionan en Google Sheets y en Numbers?** Sí: nuestras convenciones **prohíben `INDIRECT`, `COUNTA`, `PMT`, `OFFSET`, `XLOOKUP`, `LET` y `LAMBDA` justamente por eso**, y no hay referencias entre libros.»

**Problema.** La causalidad es falsa y es comprobable en un minuto: **Google Sheets implementa `INDIRECT`, `COUNTA`, `PMT`, `OFFSET`, `XLOOKUP`, `LET` y `LAMBDA`** — las siete. Numbers implementa `INDIRECT`, `COUNTA`, `PMT` y `OFFSET`, y no `XLOOKUP`/`LET`/`LAMBDA`. Es decir, de las siete funciones prohibidas, **cuatro no dan ningún problema en ninguna de las dos plataformas**. La razón real de la lista es interna (estabilidad del recalculado, `inject_cache.py`, volatilidad y legibilidad de las fórmulas), y es una razón perfectamente vendible.

Poner una afirmación técnica falsa en una FAQ pública de un producto que se vende por rigor es el peor sitio posible para ponerla.

**Gravedad: media.**

**Fix.** «Sí. No usamos fórmulas volátiles ni funciones que dependan del motor de cálculo, y no hay referencias entre libros: lo que ves en Excel se recalcula igual en Google Sheets y en Numbers. Todos los parámetros van en **celda verde**, sin constantes escondidas dentro de las fórmulas.» La lista concreta de funciones va en la SPEC interna, no en la FAQ.

---

### C5 · MEDIA — El juego de datos son 110 m² y toda la validación económica que lo respalda es de 90 m²

**Afirmación literal (§9.1 y §4.3):** «Superficie | **~110 m²**: obrador ~55 · despacho ~25 · cámara/almacén ~15 · aseos y vestuario ~15» · «Con obra media (**81.000 €**) y proyecto (5.000 €) el total ronda **116.000 €**, dentro del rango de PS-05».

**Problema.** Los 81.000 € son «obra civil sobre local de referencia de **90 m²**» a 900 €/m² (PS-85a/b/c, caso de La Hostelera). Aplicados a los 110 m² de «La Clara» son **99.000 €**, y el total del escenario sube a **≈134.000 €** — no 116.000, y ya no «por debajo de los 137.000 € del escenario de equipamiento alto», sino prácticamente encima de él. El libro 2 y el capítulo 04 heredarían la incoherencia: parámetros de 110 m² y cifras validadas sobre 90.

Además el propio §9.1 marca la superficie como «⚠️ **Es PROPUESTA, no medición**», así que no hay ningún coste en alinearla.

**Gravedad: media.**

**Fix.** O bien fijar «La Clara» en **90 m²** (obrador 45 · despacho 22 · cámara 12 · aseos 11), que hace que todo el bloque PS-85 case sin retoques y que el escenario de referencia sea el mismo que la fuente; o bien mantener 110 m² y **recalcular el §4.3 entero** a esa superficie, diciendo que se sale del caso publicado. La primera es más barata y más honesta.

---

### C6 · MEDIA — El libro 4 devuelve «vida útil» por fórmula, y la norma sólo la fija en un caso

**Afirmación literal (§9.2, libro 4):** «Salidas por fórmula: … **temperatura de conservación y vida útil resultantes de la vía elegida**».

**Problema.** De las tres vías del art. 9, **sólo una produce un plazo legal**: el art. 9.3 impone 24 h a lo elaborado por la vía 1.a) que no sea estable a temperatura ambiente y a lo elaborado con ovoproducto (apartado 2). Para todo lo demás —un bizcocho, una ganache, un hojaldre— **la vida útil la fija el operador con su estudio, y debe constar en su plan de APPCC**; no se deriva de la vía del huevo. Una hoja que devuelva «vida útil» como salida calculada para las 30 referencias estaría emitiendo, con apariencia de fórmula, un dato que la norma atribuye al operador — y el catálogo ya tiene un precedente de ese dato mal puesto (A4).

**Gravedad: media.** Es la hoja que el research llama «el corazón técnico-legal de una pastelería».

**Fix.** Dos salidas distintas y etiquetadas: **«Plazo legal (art. 9.3)»**, que devuelve 24 h o «no aplica» según la vía; y **«Vida útil declarada por ti»**, celda verde, con la nota «la fijas tú y debe constar en tu plan de APPCC — el RD no la establece». Y la temperatura, siempre como el mínimo entre el art. 4.1 fila 9 y el art. 9.3, citando el artículo que manda en cada caso.

---

### C7 · BAJA — «~44 redactores (20 caps × 2 bloques + 2 bonus)» son 42 por su propia aritmética, y el precedente medido fueron 56

**Afirmación literal (§15.4, fase B2):** «`dump_prompts.py` → **~44 redactores sonnet (20 caps × 2 bloques + 2 bonus)**».

**Problema.** 20 × 2 + 2 = **42**. Y el paréntesis subestima el trabajo: el bonus 2 son **12 decisiones** de 800-900 palabras cada una, que no caben en un bloque; el bonus 1 es un business plan con ≥8 tablas. El precedente medido para un paquete de tamaño equivalente —Manual del Chef Ejecutivo, 96 págs + 34 de bonus— fueron **56 bloques por 56 redactores, 7,7 M tokens** (`SESSION_HANDOFF_2026-09-06-manual-chef-ejecutivo.md:21`).

**Gravedad: baja** en sí misma, pero es uno de los sumandos de B2.

**Fix.** «20 caps × 2 bloques + 12 bloques del bonus 2 + 1-2 del bonus 1 = **53-54 redactores**», y ajustar la estimación de B2 al ratio medido (7,7 M / 56 bloques ≈ 0,14 M por bloque ⇒ **≈7,4-7,6 M**).

---

### C8 · BAJA — «Coincide exactamente con los 4 perfiles del kit»: son 5 personas y un nombre que el kit no usa

**Afirmación literal (§9.1):** «Plantilla | Jefe pastelero · **1 oficial** · 1 ayudante · 2 dependientes (1 a tiempo parcial) | **Coincide exactamente con los 4 perfiles del `04-tareas-perfiles.xlsx`** del kit → **el cross-sell es literal**.»

**Problema.** Abierto el fichero, las cuatro hojas se llaman **Jefe Pastelero · Pastelero · Ayudante · Dependiente Vitrina**. «Oficial» no aparece en ninguna. Si el argumento es que el cross-sell es *literal*, el nombre tiene que serlo: el lector que abra el kit buscando la ficha del «oficial» no la encuentra.

**Gravedad: baja.**

**Fix.** Llamarlo **«Pastelero»** en el juego de datos, en el libro 10 y en el capítulo 13. Y matizar la frase: «cubre los 4 perfiles del kit, con dos personas en el perfil de Dependiente Vitrina».

---

### C9 · BAJA — PA-03 vende el «central + sucursales» como palanca de crecimiento y omite la obligación que va pegada

**Afirmación literal (§1.2 nº 3 y PA-03):** «El art. 3.6 exceptúa el flujo del establecimiento central a sus sucursales de misma titularidad: **no se considera suministro entre minoristas**… **Es una palanca de crecimiento que casi ninguna fuente explica.**»

**Problema.** El art. 3.6 literal: «se considerarán una única unidad comercial, **pero se inscribirán en el registro de las comunidades autónomas de manera independiente**». La segunda mitad —cada sucursal con su inscripción— es la obligación operativa que acompaña a la ventaja, y es justo lo que necesita saber quien está decidiendo abrir un segundo despacho. La síntesis publica la ventaja sin el deber.

**Gravedad: baja**, pero es un capítulo (09) que se vende por completar lo que otros dejan a medias.

**Fix.** «Central y sucursales de la misma titularidad son **una sola unidad comercial** y el suministro entre ellas **no cuenta como B2B** — pero **cada sucursal se inscribe por separado en el registro autonómico**.»

---

### C10 · BAJA — La «pasada quirúrgica del estilo `fase8h`» es un script nuevo por producto, no una herramienta existente

**Afirmación literal (§13.2):** «⚠️ **Herramienta:** `fase8e-banners-corpus.py` **sólo inserta, no sustituye**. Para cambiar un banner ya publicado hace falta **una pasada quirúrgica del estilo `fase8h`** (la que se usó con el Manual del Chef Ejecutivo), **con gate de reversibilidad byte a byte**.»

**Problema.** En `scripts/astro-migration/` hay **un script por producto**: `fase8f-guia-food-cost-blog.py`, `fase8g-manual-manager-blog.py`, `fase8h-manual-chef-blog.py`. No existe una herramienta genérica de sustitución. La fase C tendría que **escribir un `fase8i-guia-pasteleria-blog.py`** con su propio gate de reversibilidad, y eso no está desglosado en el presupuesto de C (1,0-1,5 M) ni listado entre lo «a crear» del §8.4, que sí enumera la SPEC, el guion, los 10 `gen_*.py`, `datos_ejemplo.py` y `verificar_guion.py`.

**Gravedad: baja.**

**Fix.** Añadir `fase8i-guia-pasteleria-blog.py` a la lista de piezas a crear del §8.4. Y considerar lo evidente: **cuatro productos seguidos han necesitado el mismo script con el nombre cambiado**. Generalizarlo a `fase8x-sustituir-banner.py --producto <pid> --posts <lista>` cuesta lo mismo que copiarlo una quinta vez y cierra la deuda.

---

## Resumen para decidir

**Lo que hay que arreglar antes de firmar la SPEC (bloqueantes):** A1 (recomputar la validación cruzada en una sola base de IVA) · A2 (art. 3: alternativas, no acumulativas, y rehacer la hoja del libro 7) · A3 (la lista blanca del 13.8 tiene cinco letras) · A4 (corregir `kit-tareas-pasteleria/13` o no citarlo) · B2 (tres escenarios de alcance y presupuesto, con el precedente de 17 M delante) · B3 (re-consultar el precio del competidor y reescribir el argumento del hueco) · C1 (el gate que ata la landing con el PDF).

**Lo que hay que decidir con John, y no está bien planteado hoy:** **D12 no puede coexistir con D14** (B1) — hay que llevarle una sola opción de calendario, con las semanas de v2.0 que se desplazan escritas. Y **D4 es más barata de lo que dice** (C3): el art. 30 ya está verificado.

**Lo que ha resistido la refutación y sostiene el producto:** el bloque normativo del RD 1021/2022 y de la Ley 1/2025 es **exacto en todo lo que he podido contrastar contra el BOE consolidado**; la frontera R1-R6 con el kit es el reparto más limpio del catálogo; el molde de `planes-v2_0` para el libro 5 es construible tal cual (cero fórmulas prohibidas en 737); el censo de banners, las dimensiones de los xlsx, la escalera de precios y los recuentos del repo son exactos; y el diagnóstico de fondo —la línea de 65 € no entrega lo que promete— es cierto, aunque haya que reformularlo (A6, A7, A13).

---

**Via: Claude Code**
