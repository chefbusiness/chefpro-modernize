# SPEC — How to Open a Pastry Shop (EN) · producto 15 de la tienda EN

> Sesión Claude Code, 16/17-oct-2026. Duplicado de la **Guía «Cómo Montar una Pastelería»** (ES, 65 €, v1.0.1 sep-2026,
> `guia-pasteleria-obrador`) para la tienda EN. Tamaño **L** (≤ 10 M tokens). Segunda guía en inglés: reutiliza el método
> y la mecánica de la Food Cost EN (`../guia-food-cost-en/SPEC.md`, `F1-census.md`): `GuiaLandingPage` con `lang`,
> registro en 5 fuentes, dashboard EN gemelo, render con `documentos.maquetar()`.
> Insumos de F1: `F1-census.md` (anatomía ES: el **94 %** del texto depende de España) y `F1-research-us.md` (hechos US
> con fuente: la ÚNICA fuente de datos legales, laborales, fiscales y de mercado que pueden usar los traductores).
> Reglas heredadas que no se repiten aquí: `TIENDA-INTERNACIONAL.md` §1 y §6, `GLOSARIO-JERGA-ES-EN.md`,
> `../guia-food-cost-en/SPEC.md` D6-D10.

## 1. Decisiones

| # | Tema | Decisión |
|---|---|---|
| D1 | Nombre y URL | **«How to Open a Pastry Shop»** (ya publicado como «Coming soon» en el hub EN: no se cambia). «Bakery» va como **descriptor** (title, H1, meta; D3), que es lo que busca EE. UU. Slug y productId `how-to-open-a-pastry-shop` → `/en/digital-products/how-to-open-a-pastry-shop` (+ `/access`, `/library`). Familia nueva en `tienda.ts`: `guia-pasteleria-obrador` (es + en) |
| D2 | Precio | **$69** (ES 65 €; la Food Cost pasó de 55 € a $59). Payment Link en **USD** (el primero de la Food Cost salió en EUR: avisar a John) |
| D3 | SEO | Ver §6 (sale de `F1-research-us.md` §15). Keywords: how to open a bakery 720 · how to start a bakery business 480 · bakery startup costs · how much does it cost to open a bakery · cottage food license · bakery permits · pastry shop business. PAA |
| D4 | Documentos | Se traducen y readaptan los **tres `.md` ensamblados** del ES (`../guia-pasteleria/build/docs/`): guía (57.623 palabras, 20 caps. + anexo), bonus «12 decisiones» (16.744) y business plan modelo (8.059). Render con `render_en.py` (A4, mismo maquetado). Salidas en `astro-site/public/dl/how-to-open-a-pastry-shop/`: `how-to-open-a-pastry-shop.docx/.pdf`, `BONUS-12-opening-decisions.docx/.pdf`, `sample-business-plan-pastry-shop.docx` (como el ES, solo docx) |
| D5 | Portada | Subtítulo «**Production kitchen, permits and numbers: the complete opening playbook · US edition 2026**» (con notas UK, Canada y Australia). Versión: «**Version 1.0 · October 2026 · aichef.pro/en/digital-products/how-to-open-a-pastry-shop**». Bonus: «**12 Opening Decisions, Solved**». Plan: «**Sample Business Plan for a Pastry Shop**» |
| D6 | **El caso «La Clara»** | Caso MODELADO (ya lo es en ES: «no es un benchmark»). **Cifras idénticas: € → $ 1:1, cifra intacta** (1.427,89 € → $1,427.89), como la Food Cost. Se **traslada a «a mid-size city in Texas»**: es el estado donde el caso encaja sin recalcular (salario mínimo federal de $7.25, al que superan todos los sueldos del ejemplo; cottage food amplio) y cuya tradición panadera hispana casa con los productos de temporada del caso (rosca de Reyes el 6 de enero, polvorones, buñuelos, primeras comuniones, Día de Muertos). Concepto EN: «**a European-style pastry shop with Spanish and Mexican holiday specialties**». Donde el caso quede por debajo del mercado US (sueldos, precios), el texto lo dice con el dato US de `F1-research-us.md` al lado y le pide al lector sus cifras. Nunca se presenta una cifra del caso como dato del sector. Formato US: 1,234.56 · 30% · October 15, 2026 |
| D7 | Impuestos | **Precio de carta sin impuesto** (US). xlsx: cada celda «PVP con IVA» tecleada recibe el **PVP sin IVA del ES con todos los decimales** (= ES ÷ (1+IVA)) y cada tipo de IVA pasa a **0 %** → todo valor derivado «sin IVA» queda idéntico al ES. Texto: las cifras «sin IVA» se quedan; las «con IVA» pasan a la cifra pre-tax (lista en `DECISIONES-TANDAS.md` §3). **Sales tax** de la comida de pastelería por estado: solo lo que diga el research (§10). El sales tax pagado en equipo y obra **es coste** en EE. UU. (no se recupera): el lector pone su tipo en la columna de impuesto del CAPEX (0 % por defecto). Las hojas de recuperación del IVA soportado («IVA y Tesorería», tesorería con IVA repercutido/soportado/modelo 303) pasan a «**VAT/GST & Cash (UK, Canada, Australia)**»: fórmulas intactas, sirven a quien recupera el impuesto (UK VAT, CA GST/HST, AU GST); en EE. UU. se dejan a 0 %. Fuera: tipos 4/10/21 %, modelo 303, Verifactu, Impuesto de Sociedades, autónomos (una línea genérica «talk to a CPA» como mucho) |
| D8 | Unidades | Superficies **m² → sq ft** (× 10.7639) en texto y xlsx, y **€/m² → $/sq ft** (÷ 10.7639): los totales no cambian. **°C → °F**. Caudal **m³/h → CFM** (÷ 1.69901). **Pesos de receta en GRAMOS** (la pastelería profesional US pesa en gramos; precedente Food Cost D8) y **precio de compra en $/kg** en los xlsx; en el texto, el $/lb entre paréntesis en los ingredientes clave (× 0.453592). Envases de compra en lb en el texto («50 lb bag»). kW se queda. «Potencia contratada» → servicio eléctrico (amperios/voltaje) según el research |
| D9 | Terminología | Glosario §13 de `F1-research-us.md` + `GLOSARIO-JERGA-ES-EN.md` + Food Cost D9. Fijos: obrador → **production kitchen** (bakehouse) · despacho/vitrina → **front counter / display case** · bollería → **viennoiserie / breakfast pastries** · pastelería individual → **individual pastries** · tartas y entremets → **cakes and entremets** · encargo → **custom order** · señal → **deposit** · abatidor → **blast chiller** · cámara de fermentación controlada → **retarder-proofer** · escandallo → **recipe costing / cost card** · merma → **waste / trim loss** · ticket medio → **average ticket** · CAPEX → **startup costs (CAPEX)** · punto de equilibrio → **break-even** · traspaso → **taking over an existing business (key money)** |
| D10 | Referencias españolas | Leyes, BOE/RD, CCAA, ayuntamientos, convenio, estadísticas e ids `PS-*`/`PA-*` **no se traducen**: se sustituyen por el hecho US equivalente de `F1-research-us.md` (con su fuente) o se generalizan o quitan. **Nunca se inventa una fuente, un artículo, una tasa ni una cifra US.** Las «cuatro comunidades de ejemplo» → **California, Texas, New York, Florida**. El glosario «España e Hispanoamérica» del cap. 1 → glosario **US · UK · Canada · Australia** (de la Equivalents Guide). Lo que el traductor no pueda resolver: `⟦ADAPT: motivo⟧` (el gate falla con `--final`) |
| D11 | Ficheros y pestañas | Mapa cerrado §2. En el texto EN, ficheros con su nombre EN y pestañas entre comillas dobles rectas («the "Batch Costing" sheet») |
| D12 | Laboral | En EE. UU. no hay convenio. La tabla de 6 grupos pasa a **tabla de sueldos por puesto** (6 filas, claves traducidas IGUAL en los tres libros: las usan `MATCH`/`INDEX`). Para que el coste anual no cambie: «pagas» **15 → 12** y el bruto mensual **× 15/12** con todos los decimales (anual idéntico). El 33 % de SS pasa a «**Payroll taxes, workers' comp and benefits**» (mismo 33 %; el texto explica sus partes US con el research y que sin seguro médico baja). SMI → «**Minimum wage (monthly, full-time)**» = federal/Texas $7.25 × 2,080 h ÷ 12 = **$1,256.67** con 12 pagas; el veredicto sigue siendo «la tabla supera el mínimo». El texto da el sueldo hora del ejemplo (anual ÷ 2,080), lo compara con BLS y con los mínimos de CA, NY y FL (donde el ejemplo sería ilegal: dilo) y pide al lector sus sueldos. 1.780 h/año = «annual hours actually worked (after paid time off and holidays)». Perfiles (nombres de `PERFILES_KIT`): §5 de `DECISIONES-TANDAS.md` |
| D13 | Seis picos | (El research proponía «Pi Day & St. Patrick's Day» para el pico de marzo; se descarta: Mother's Day pesa $38 bn según NRF y mover el mes no cambia ninguna cifra.) Mismas seis campañas, mismas cifras y mismos días; nombres US-Texas: 1 **Día de Reyes — Rosca de Reyes** (Jan 2-6) · 2 **Valentine's Day** (Feb 13-14) · 3 **Mother's Day** (Día de las Madres May 10 + US Mother's Day, 2nd Sunday of May) — su mes pasa de 3 a **5** (la columna «Mes» no la usa ninguna fórmula: cero efecto numérico) · 4 **Easter (Holy Week)** · 5 **First Communions and graduations** (mid-April to mid-June) · 6 **All Saints' Day and Día de los Muertos** (Oct 30-Nov 1). Thanksgiving y Christmas: se mencionan como picos US que el ejemplo recoge en la estacionalidad mensual (nov 1,08 · dic 1,24), no como campaña |
| D14 | Carta | Las 30 referencias conservan ingredientes, gramos, minutos, costes y precios (pre-tax, D7); cambian solo los nombres (tabla §4 de `DECISIONES-TANDAS.md`). Las tres copias del kit (B1, PI3, T1) se citan como copia del **Food Cost Kit Pro** (`05-bakery-cake-pricing.xlsx`, hojas "Croissants", "Macarons", "Chocolate Cake"), donde están en unidades US |
| D15 | Libros de ley española | `checklist-legal-y-licencias.xlsx` → **`permits-and-licenses-checklist.xlsx`**: misma estructura y mismo nº de filas (30 trámites F1-F6, árboles, ruta doméstica, registro de formación, cronograma), contenido US del research §1-§3: el árbol de registro sanitario → «Which Permit Do I Need?» (retail food establishment / wholesale + FDA registration / cottage food); «Suministro a Otros Minoristas» → «Selling Wholesale»; «Ruta Doméstica» → «Cottage Food Route»; «Registro de Formación» → «Training Log» (CFPM, food handler cards). Fechas `mm/dd/yyyy`. En `opening-menu-and-recipe-costing.xlsx`, «Decisión de Huevo y Temperatura» (art. 9 RD 1021/2022) → «**Egg & TCS Decision**» (FDA Food Code: TCS frente a no TCS, ≤ 41 °F, marcado de fecha de 7 días si se guarda > 24 h, consumer advisory si hay huevo crudo): mismas fórmulas, se reescriben sus literales con los hechos del research §3 |
| D16 | Equipo y proveedores | Filas de marca y modelo: se mantiene la marca si se vende en EE. UU. (research §11) y se cambia por un equivalente US verificado si no; **el precio de la celda es el del caso** y se rotula «example price»; el texto da los rangos US del research. Los 9 proveedores → proveedores US por categoría (distribuidor generalista, distribuidor de pastelería, chocolate, packaging…) con URL verificada |
| D17 | Ventas cruzadas | `Kit de Escandallos` → **Food Cost Kit Pro** (`/en/digital-products/food-cost-templates`). `Kit de Tareas Pastelería` (sin gemelo EN) → se quita la mención o se generaliza («your daily task checklists»); donde hable de registros de temperatura o limpieza → **HACCP Food Safety Kit Pro** (`/en/digital-products/haccp-templates`). Hosply.pro → fuera. Nuevo: **Bakery Business Plan Kit** (`/en/digital-products/bakery-business-plan`, $39) para quien quiere el plan para el banco. Ninguna mención a un producto ES |
| D18 | Bonus comunes | La guía ES de equivalencias **no** se traduce: va el bonus común `equivalents-guide` (`dl/en-shared/…docx`) como en los otros 14 |
| D19 | Landing y app | Como Food Cost D14: ficha EN `productos-en/guias/how-to-open-a-pastry-shop.ts` (copia de la ES), páginas landing/access/library, dashboard EN gemelo, registro en 5 fuentes + admin, `usd: 69`, `omitGlobalApp`, sin reseñas ni rating, `CryptoPayButton lang="en"` en las 3 puertas, FAQ con las PAA + «Does it work in the UK, Canada or Australia?» + equivalents. La tarjeta «Coming soon» del hub EN pasa a viva (y se corrige su descripción, que dice «Chocolate kitchen»). Enlaces recíprocos con Bakery Business Plan, Food Cost Kit Pro, HACCP Kit y Food Cost Guide |
| D20 | Correo EN | Hueco EN **4-dic 14:00Z** (handoff 15-oct); borrador + routine como el Mobile Bar y la Food Cost |

## 2. Mapa de ficheros y pestañas (cerrado)

| ES | EN | Pestañas EN (en orden) |
|---|---|---|
| calculadora-capex-pasteleria.xlsx | **startup-cost-calculator.xlsx** | Instructions · Settings · Startup Costs by Block · Format Variant · Takeover vs New Build · VAT-GST & Cash · Summary |
| capacidad-obrador-y-local.xlsx | **kitchen-capacity-and-site.xlsx** | Instructions · Settings · Zones and Square Feet · Capacity by Equipment · Bottleneck · Site Visit Checklist |
| carta-de-apertura-y-escandallo.xlsx | **opening-menu-and-recipe-costing.xlsx** | Instructions · Settings · Batch Costing · Labor Cost per Hour · Egg & TCS Decision · Mix and Average Ticket · Menu Decision |
| checklist-equipamiento-y-proveedores.xlsx | **equipment-and-suppliers-checklist.xlsx** | Instructions · Equipment · Format Variant · Suppliers · Counter |
| checklist-legal-y-licencias.xlsx | **permits-and-licenses-checklist.xlsx** | Instructions · Permits Checklist (P1-P6) · Which Permit Do I Need · Selling Wholesale · Cottage Food Route · Training Log · Timeline and Critical Path |
| estacionalidad-y-picos.xlsx | **seasonal-peaks-planner.xlsx** | Instructions · Settings · 6-Peak Calendar · Share of the Year · Peak Capacity vs Demand · Extra Staff and Cash |
| plan-financiero-3-anos-pasteleria.xlsx | **3-year-financial-plan.xlsx** | Instructions · 0. Assumptions · Startup Investment · 3-Year P&L · Break-Even · Scenarios · Staff · 12-Month Cash Flow · Financing · Channels and Break-Even |
| plantilla-turnos-y-coste-personal.xlsx | **staff-schedule-and-labor-cost.xlsx** | Instructions · Settings · Weekly Schedule · Hours and Cost · Hiring Plan |
| guia-pasteleria-obrador.docx/.pdf | **how-to-open-a-pastry-shop.docx/.pdf** | — |
| BONUS-12-decisiones-de-apertura.docx/.pdf | **BONUS-12-opening-decisions.docx/.pdf** | — |
| business-plan-modelo-pasteleria.docx | **sample-business-plan-pastry-shop.docx** | — |
| 05-pasteleria.xlsx (Kit de Escandallos ES; solo se cita) | **05-bakery-cake-pricing.xlsx** (Food Cost Kit Pro EN) | Croissants · Macarons · Chocolate Cake |

Ficheros ES citados sin EN (`ORFANOS` en `split_md.py`): `05-pasteleria` (→ texto «Food Cost Kit Pro, 05-bakery-cake-pricing.xlsx»), `BONUS-02-calendario-anual-tareas`, los `kit-tareas-pasteleria/*.xlsx` (D17).

## 3. Plan por fases (gate + commit + push al cerrar cada una)

- **F1 (Mac)** — `F1-census.md`, `F1-research-us.md`, esta SPEC, `DECISIONES-TANDAS.md` sembrado, utillaje (`split_md.py`,
  `gate_md_en.py`, `ensamblar_md.py`, `render_en.py`, `xlsx/censo_textos.py` → `xlsx/textos_es.json`). Cierra con el
  gate corrido sobre una tanda de prueba.
- **F2** — (a) traducción y readaptación de las tandas §4, de 2 en 2 en el Mac (API); (b) xlsx EN: textos por libro
  (`xlsx/textos_en/<libro>.json`) + `xlsx/config_en.py` (D7, D8, D12, D13) + `aplicar_en.py` + `inject_cache.py` +
  `gate_xlsx_en.py` **en el VPS**; (c) ensamblado + render + gates de documento **en el VPS**; (d) UNA revisión Opus final.
- **F3** — landing con `lang`, páginas, dashboard, registro, precio, gates LIVE, Payment Link de John, correo, llms.txt,
  sitemap, GSC, handoff.

## 4. Tandas (entrada `tandas/es/<T>.md` → salida `tandas/en/<T>.md`)

| Tanda | Contenido | Palabras | Modelo |
|---|---|---|---|
| T01 | portada + índice + cap. 1 (variantes, glosario US/UK/CA/AU) | 4.090 | opus |
| T02 | cap. 2 (cliente y plaza: datos US) + cap. 3 (carta: nombres §4, D7) | 5.358 | opus |
| T03 | cap. 4 (CAPEX: D7 sales tax, marcas) + cap. 5 (local: sq ft) | 4.764 | opus |
| T04 | cap. 6 (antes de firmar: lease, zoning, hood) + cap. 7 (obrador por dentro) | 5.375 | opus |
| T05 | cap. 8 (maquinaria: marcas, precios) + cap. 9 (licencias: 4 estados) | 5.599 | opus |
| T06 | cap. 10 (food safety, alérgenos, formación) + cap. 11 (proveedores US) | 4.946 | opus |
| T07 | cap. 12 (escandallo y precios) | 3.515 | sonnet |
| T08 | cap. 13 (equipo: D12) + cap. 14 (turnos de madrugada: FLSA, menores) | 4.356 | opus |
| T09 | cap. 15 (seis picos: D13) + cap. 16 (encargos: comuniones y graduaciones) | 5.332 | opus |
| T10 | cap. 17 (canales: wholesale, envío) + cap. 18 (plan financiero) | 5.685 | opus |
| T11 | cap. 19 (financiación, sales tax, envases, tesorería) | 3.237 | opus |
| T12 | cap. 20 + anexo normativo (→ «Regulatory Appendix (US), updated October 2026») + sobre el autor | 5.366 | opus |
| B01 | bonus: portada + índice + dec. 1-4 | 5.665 | opus |
| B02 | bonus: dec. 5-8 | 5.453 | opus |
| B03 | bonus: dec. 9-12 + sobre el autor | 5.626 | opus |
| P01 | plan: portada + índice + §1-4 | 4.705 | opus |
| P02 | plan: §5-6 + sobre el autor | 3.354 | opus |

## 5. Brief para cada traductor (el orquestador lo pega con su tanda)

**Lees** (y nada más): tu entrada `tandas/es/<T>.md`; esta SPEC (§1, §2, §5); `DECISIONES-TANDAS.md` (entero:
nombres fijados por todos); `F1-research-us.md` (las secciones que te indique el orquestador); y
`../business-plans-en/BRIEF-TRADUCTORES.md` §0 («Idioma y tono», «Reglas duras»). Si choca con esta SPEC, manda la SPEC.

**Escribes** `tandas/en/<T>.md`: el mismo Markdown con **estructura idéntica** (mismo nº y nivel de encabezados, mismas
tablas con las mismas filas y columnas, mismas listas, negritas y cursivas en su sitio). Encabezados en Title Case.
Tú a tú («you»), inglés de EE. UU. natural de alguien que ha llevado un obrador; no traducción literal. Readaptar es
**cambiar el contenido español por su equivalente US dentro de la misma forma**: la tabla de cuatro comunidades pasa a
ser la de cuatro estados, la lista de trámites españoles la de trámites US, con el mismo número de filas e ítems.

**Cifras**: las del caso, idénticas (D6) salvo las «con IVA» (D7) y las magnitudes con unidad (D8). Cifras US nuevas:
solo de `F1-research-us.md`, con la fuente citada como la cita el ES (nombre del organismo y año; sin URL larga en el
cuerpo salvo en el anexo). Lo que no puedas resolver: `⟦ADAPT: motivo⟧`.

**Al terminar**: añade a `DECISIONES-TANDAS.md` §9 (bajo tu tanda) 3-8 decisiones que las demás deban conocer (nombres
nuevos, cifras convertidas, términos). Valida: `istats cpu temp | head -1` y
`python3 scripts/productos-digitales/guia-pasteleria-en/gate_md_en.py --tanda <T>` hasta `OK`. Responde solo con:
fichero escrito, resultado del gate, nº de marcas `⟦ADAPT⟧` y las decisiones añadidas. Sin commits; no toques nada fuera
de tu salida y de tu bloque en `DECISIONES-TANDAS.md`.

## 6. SEO de la landing

- **Title** (58): `How to Open a Pastry Shop: US Bakery Guide + 8 Excel Tools`
- **Meta** (152): `Open a bakery with its own pastry kitchen: permits by state, cottage food, startup costs, equipment, staff and a 3-year plan. 8 Excel tools + 2 bonuses.`
- **H1**: «How to Open a Pastry Shop» + descriptor «The step-by-step guide to opening a bakery with its own production
  kitchen in the US: permits, startup costs, equipment, team, peak seasons and your first 90 days.»
- Cabezas: how to open a bakery 720 (MED) · how to start a bakery business 480 (MED) · opening a bakery 1,000 · pastry shop
  business 1,300 · cottage food law 6,600 / license 4,400 (puerta de entrada: FAQ) · home bakery license 590 · how much
  does it cost to open a bakery 260 · bakery permits 260. Las dos SERP de cabeza llevan AI Overview: cada sección de la
  landing abre con una frase citable; ángulo diferencial = caso numérico completo + 8 Excel + ruta legal por estado; contestar
  «home bakery → storefront». Mencionar Texas y Florida (búsquedas relacionadas por estado).
- FAQ (PAA, research §12.3) + «Does this work in the UK, Canada or Australia?» (research §14).
