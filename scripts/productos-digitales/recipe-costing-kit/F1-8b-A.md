# Recipe Costing Kit — F1 · Research 8 bloques (parte A): compradores, huecos normativos, software, modelo de negocio y referentes

> Sesión Claude Code, **24-sep-2026** (subagente de F1). Amplía `F1-research-us-uk.md` (no lo repite) y alimenta
> `SPEC.md`. Cubre los bloques **1, 2 (solo huecos), 3, 5 y 6** del método de la memoria
> `feedback_research-previo-producto-nuevo`. Los bloques 4 (proveedores y formatos de compra) y 7 (documentación propia
> del mercado) van en la parte B.
>
> **Leyenda:** `[fuente: URL]` = dato leído en esa página · `[fuente secundaria]` = blog, resumen de buscador o
> agregador, no fuente primaria · `[medido DFS 24-sep]` = DataForSEO hoy (US 2840/en, UK 2826/en) · `[estimado]` =
> cálculo o criterio propio, con la cuenta a la vista · `[no medido]` = no se pudo medir y se dice.
>
> Restricción de la sesión: Mac con límite térmico (máximo medido 53 °C). Sin navegador, sin builds. Solo `curl` a
> APIs públicas (BLS QCEW, Nomis/ONS), WebSearch/WebFetch y DataForSEO.

---

## 0. Lo que cambia en la SPEC (resumen)

| # | Propuesta | Tipo | Bloque |
|---|---|---|---|
| C1 | **«Ventas netas» = sin impuesto Y sin service charge/propinas** en 10, 11, BONUS, PDF e Instrucciones. En UK el service charge discrecional va íntegro al personal (Tips Act) y queda fuera del IVA; si entra en las ventas, el GP % sale inflado | Solo texto | 2 |
| C2 | **06 Catering: valores por defecto US** (ratio 1:25 en recepción, camarero $25/h, jefe de sala $35/h, rentals $3,50/invitado, mínimo $1.000…) y rótulo «Service charge (%)» para el «margen servicios» del ES, con la nota DOL/IRS: un service charge **no es propina** | Valores + texto | 1, 2, 5 |
| C3 | **08 Food truck: costes diarios US** (commissary/parking $45 · seguros+permisos $25 · combustible/propano/generador $30 · personal $300 · amortización $50 · limpieza/agua $15 = **$465/día**) en lugar de los 300 € del ES | Valores | 2, 5 |
| C4 | **05 Pastelería en gramos** (compra en lb, receta en g): la pastelería estadounidense pesa en gramos y con porcentajes de panadero. El resto del kit, en lb/oz. Matiza D7 | Valores | 3 |
| C5 | **04 Bar: barril de cerveza** en `Conversions` y en el desplegable (`keg→fl oz` = 1.984, medio barril US; nota UK 50 L ≈ 88 pintas). Vino por copa: 5 fl oz (US) / 125-175-250 ml (UK). Nota sobre impuestos que paga el bar (Texas 6,7 %) | Fila de dato + desplegable (**requiere OK de John**: toca la lista literal de D7) | 1, 2 |
| C6 | **BONUS de inventario: instrucción para pegar el *product mix* del TPV** (nombre del plato + unidades vendidas) de Toast, Square, Clover, Lightspeed o Epos Now en `Sales for the Period` | Solo texto | 3 |
| C7 | **Prime cost: sin cambiar la estructura del 11.** Se explica en el PDF y en la FAQ con los datos de la NRA. La fila de mano de obra en el dashboard queda como propuesta para una v2.1, y la decide John | Texto ahora; estructura a decidir | 5 |
| C8 | **Landing: bloque honesto «Kit vs. software»** (meez $19/mes, Jelly £129/mes, MarginEdge $350/mes, R365 $469-749/mes…) y FAQ para los segmentos que el kit no nombra (private chef, meal prep, ghost kitchen, estudiantes) | Copy | 1, 3 |
| C9 | **PDF bonus: tabla de economía US/UK 2025-26** (márgenes NRA, cadenas cotizadas, inflación ERS/ONS, 30/30/30/10 con matiz) y «Further reading» con 3 manuales, sin afiliación | Texto PDF | 5, 6 |
| C10 | **Decisión de John: licencia** para consultores (¿pueden entregar copias a clientes?) y escuelas (¿licencia de aula?) | Decisión | 1 |

Detalle y fuentes en §1-§6. Ninguna propuesta añade hojas, columnas ni fórmulas salvo C5 (una fila de datos en
`Conversions` y un valor más en el desplegable, que es el crecimiento que la SPEC §0 ya admite) y C7, que queda aplazada.

---

## 1. Bloque 1 · Tipos de comprador

### 1.1 Tamaño de los segmentos

**EE. UU.: establecimientos privados con asalariados, 4.º trimestre de 2025** (BLS QCEW, `area_fips=US000`,
`own_code=5`, descargado hoy de la API abierta) [fuente: https://data.bls.gov/cew/data/api/2025/4/industry/{NAICS}.csv].
QCEW **no cuenta los negocios sin asalariados** (el food truck de un autónomo, el private chef, el consultor): esos
segmentos salen infrarrepresentados.

| NAICS | Segmento | Establecimientos | Empleo (dic-2025) | Var. interanual de establecimientos |
|---|---|---|---|---|
| 722 | Total food services & drinking places | **728.580** | 12.156.414 | +1,2 % |
| 722511 | Full-service restaurants | **266.611** | 5.315.016 | +0,2 % |
| 722513 | Limited-service (QSR + fast casual) | **272.103** | 4.578.945 | +1,4 % |
| 722515 | Snack & nonalcoholic beverage bars (coffee shops, juice, donuts, helados) | **88.925** | 990.840 | **+4,4 %** |
| 722410 | Drinking places (bares) | **42.323** | 405.344 | −1,0 % |
| 722330 | Mobile food services (food trucks, carts) | **13.123** | 43.358 | **+6,0 %** |
| 722320 | Caterers | **14.147** | 181.919 | +1,4 % |
| 722310 | Food service contractors (colectividades) | 26.112 | 567.079 | +1,1 % |
| 722514 | Cafeterias & buffets | 5.236 | 73.913 | +0,5 % |
| 311811 | Retail bakeries | 9.814 | 110.506 | +2,4 % |

- **7 de cada 10 restaurantes son de un solo local y 9 de cada 10 tienen menos de 50 empleados**
  [fuente: https://restaurant.org/research-and-media/research/industry-statistics/national-statistics/]. Es el perfil
  del comprador de un kit de $19: independiente y pequeño.
- La NRA prevé **$1,55 billones** de ventas de restauración y 15,8 millones de empleos en 2026
  [fuente: https://restaurant.org/research-and-media/media/press-releases/persistent-cost-increases-and-enduring-demand-will-shape-the-restaurant-industry-in-2026/ — cifra del resumen de buscador sobre la nota de prensa].
- Food trucks sin asalariados: **10.099** negocios en 2020 (Nonemployer Statistics, NAICS 722330) [fuente secundaria,
  resumen de buscador; el API del Census pide ahora clave y no se pudo leer el dato de 2023].

**Reino Unido: empresas y locales registrados en VAT o PAYE a marzo de 2025** (IDBR de la ONS). Empresas: ONS
`ah1864.xlsx`, publicado el 24-jun-2026
[fuente: https://www.ons.gov.uk/businessindustryandtrade/business/activitysizeandlocation/adhocs/3495foodservicesbyemploymentsizeuk2023to2025].
Locales y las clases 56.21/56.30: Nomis, datasets `NM_141_1` y `NM_142_1`, 2025 [fuente: https://www.nomisweb.co.uk/api/v01/dataset/NM_141_1.data.csv].

| SIC 2007 | Segmento | Empresas | Locales (sites) | % micro (0-9 empl.) |
|---|---|---|---|---|
| 56101 | Licensed restaurants | **31.615** | **37.300** | 59,8 % |
| 56102 | Unlicensed restaurants & cafés | **28.170** | **36.325** | 78,8 % |
| 56103 | Take-away food shops & **mobile food stands** (street food incluido, no separable) | **45.355** | **48.165** | 91,3 % |
| 56210 | Event catering | 10.055 | 15.210 | [no medido] |
| 56290 | Other food service (contract catering) | 3.930 | 16.185 | [no medido] |
| 56301 | Licensed clubs | 6.180 | 6.430 | [no medido] |
| 56302 | Public houses & bars | **29.940** | **37.805** | [no medido] |

- BBPA: **44.650 pubs** en 2025 [fuente secundaria: resumen de buscador que cita a la BBPA]. La diferencia con los
  37.805 locales de la ONS se explica porque el IDBR solo cuenta negocios registrados en VAT/PAYE y porque la
  clasificación por SIC es distinta [estimado].
- **Canadá:** 80.157 negocios de full-service (IBISWorld, de pago) [fuente secundaria]. **Australia:** 89.000 negocios de
  cafés, restaurantes y comida para llevar en junio de 2025 (ABS CABEE, citado por Tourism Research Australia)
  [fuente secundaria: https://www.tra.gov.au/en/economic-analysis/tourism-businesses-in-australia]. No hay desglose
  por segmento **[no medido]**.

### 1.2 Demanda por segmento [medido DFS 24-sep]

| US | Vol. | UK | Vol. |
|---|---|---|---|
| ghost kitchen | 33.100 ⚠️ serie con un pico de 165.000: intención de noticias o consumidor [estimado] | tronc (reparto de propinas) | 2.400 |
| prime cost | 4.400 ⚠️ **la SERP es de Amazon Prime** (medido hoy); la real es «restaurant prime cost» = 260 | stock take | 2.400 |
| restaurant profit margin | 1.000 | nory (SaaS) | 2.900 |
| catering price per person | 390 | restaurant gp | 390 |
| coffee shop profit margin | 390 | menu pricing | 390 |
| culinary math | 320 | service charge restaurant | 390 |
| private chef pricing · meal prep pricing | 260 · 260 | kitchen cut (SaaS) | 320 |
| restaurant prime cost | 260 | food gp calculator | 260 |
| liquor inventory spreadsheet · bar inventory spreadsheet | 210 · 90 | stock take sheet | 70 |
| restaurant food cost | 210 | cafe profit margin | 50 |
| food truck profit margin | 170 | catering price per head | 20 |
| bakery profit margin | 90 | recipe costing · dish costing | 10 · 10 |
| food and beverage cost control | 70 | wet gp · drinks gp | sin dato |
| how to price catering | 40 | | |
| actual vs theoretical food cost · food cost variance · theoretical food cost | 30 · 20 · 10 | | |
| food truck break even · catering staffing ratio · recipe costing class | sin dato | | |

Lectura: los segmentos con demanda propia medible son **catering** (precio por persona), **cafetería**, **private
chef**, **meal prep** y **bar** (inventario de licores). La jerga de control («theoretical food cost», «variance») casi no
se busca: se usa en el cuerpo de la landing, no en el `title`.

### 1.3 Qué plantillas le sirven a cada segmento y qué echaría en falta

| Segmento | Tamaño (§1.1) | Le sirven | Echaría en falta (y qué hacer) |
|---|---|---|---|
| **Restaurante independiente full-service** (UK: licensed restaurant / gastropub) | US 266.611 · UK 37.300 locales | 01, 02, 03, 09, 10, 11, BONUS, PDF | **Subrecetas enlazadas** (fondos, salsas): el 01 las trata como ingrediente con precio por litro. Instrucciones: «cost the sub-recipe in its own card and use its cost per unit». **Menu engineering**: no está (D15). **Mano de obra / prime cost**: C7 |
| **Fast casual / QSR** | US 272.103 (con cadenas) | 01, 10 (fila fast casual), 11, BONUS | **Envases por plato**: las cadenas lo cuentan como «food *and paper*» (Chipotle, Shake Shack, §5.3). El Q-factor del 01 ya lo recoge: el rótulo debe nombrarlo («seasonings, oil, garnish, **packaging**», glosario §1.1 del research). Combos y modificadores: fuera de alcance |
| **Café / coffee shop, bakery** (UK: café) | US 88.925 + 9.814 · UK 36.325 locales (junto con restaurantes sin licencia) | 07, 05, 10, 09 | **Bebidas de café** (espresso, leche, vaso, tapa): el 07 escandalla comida y el 04 es de coctelería. Se puede usar el 04 con ml/fl oz; una hoja de «latte» sería una receta de ejemplo nueva y se propondría a John. **Precio mayorista** de panadería: fuera de alcance |
| **Bar / pub** (UK: wet-led pub) | US 42.323 · UK 37.805 locales | 04, 10 (fila bar), 11, BONUS | **Barril de cerveza** (C5). **Vino por copa**: el 04 trae la botella de 750 ml; hay que documentar la copa de 5 fl oz (US) y la de 125/175/250 ml (UK). **Inventario de barra por botella o décimas**: fuera de alcance (Bar Inventory Kit). **«Wet GP» / «dry GP»**: solo vocabulario, en las Instrucciones UK |
| **Food truck / street food** | US 13.123 con asalariados (+6 %) + ≈10.000 sin ellos · UK dentro de 56103 | **08** (break-even), 01, 10, 09 | **Cuota de feria o evento como % de ventas** **[no medido]**: el 08 solo tiene costes fijos diarios; se documenta en Instrucciones cómo sumarla. Costes diarios US: C3 |
| **Catering / eventos** | US 14.147 · UK 15.210 locales | **06**, 01, 04, 10 | **Service charge y gratuity** (C2). **Personal por horas con mínimo de 4 h** (práctica de las agencias, §5.5) y **paquete de barra por invitado y hora**: la hora ya es una celda; el paquete de barra se calcula con el 04 |
| **Ghost kitchen / marcas virtuales** | [no medido] | 01, 10 (fila delivery con comisión), 11 | Envase por pedido (Q-factor) y varias marcas en una cocina (una copia del 11 por marca). Nada estructural |
| **Private chef** | OEWS: 1.100 «Cooks, private household» con nómina, mediana $23,05/h [fuente: https://www.bls.gov/news.release/ocwage.t01.htm]; la mayoría son autónomos y no aparecen [estimado]. ACF tiene certificación propia (PCEC) [fuente: https://www.acfchefs.org/ACF/Certify/Levels/PCEC/default.aspx] | 02 (menú degustación), 06 (presupuesto por invitado), 01 | **Honorarios** (compra a cargo del cliente + fee de servicio): el 06 lo resuelve con el FC objetivo y el margen de servicios. Va a la FAQ de la landing, sin cambios de estructura |
| **Meal prep** | [no medido] | 01 (raciones y lotes), 10, 09 | Envase y etiqueta (Q-factor); información nutricional: fuera de alcance |
| **Estudiantes y escuelas** | **ProStart: más de 234.000 alumnos en 2.275 centros** de los 50 estados [fuente: https://chooserestaurants.org/programs/prostart/]. El currículo FRMCA incluye hacer la *recipe cost card* de una receta estandarizada y calcular food cost % y markup [fuente secundaria: resumen de buscador sobre materiales ProStart]. UK: el **Level 3 Diploma in Professional Cookery (City & Guilds 7133)** incluye «cost proposed recipes and work out gross profit» [fuente secundaria: resumen de buscador sobre el handbook 7133] | 01 (mismo método AP→EP→yield % que *Culinary Math*, §6), 04, 05, 10 | Nada estructural. **Licencia de aula** (C10). Cursos universitarios de *culinary arts* (CIP 12.0503) **[no medido]** |
| **Consultores** | [no medido] | Todo el kit como entregable al cliente | **Licencia** (C10). Hoy la landing ES no dice si el comprador puede entregar copias a sus clientes |

**Conclusión:** ningún segmento necesita una plantilla nueva para que el kit le sirva. Lo que falta es **texto**
(Instrucciones, FAQ y landing) y **valores de mercado** en 04, 05, 06 y 08. Las cuatro carencias reales (bebidas de
café, subrecetas enlazadas, mano de obra/prime cost y barril) se proponen a John como cambio y no se hacen por defecto.

---

## 2. Bloque 2 · Huecos normativos que afectan al cálculo del precio

### 2.1 Propinas y service charge

| Tema | EE. UU. | Reino Unido | Efecto en el kit |
|---|---|---|---|
| ¿Es propina? | **Un cargo obligatorio no es propina**: «A compulsory charge for service, for example, 15 percent of the bill, is not considered a tip under the FLSA» [fuente: https://www.dol.gov/agencies/whd/fact-sheets/15-tipped-employees-flsa]. Para la IRS, la «auto-gratuity» es *service charge* y, si se reparte, salario (Rev. Rul. 2012-18, vigente desde 2014) [fuente secundaria: https://www.pillsburylaw.com/a/web/260/260.pdf] | Tips Act: el empleador **reparte el 100 %** de propinas, gratificaciones y service charges, tanto obligatorios como discrecionales, sin deducciones salvo impuestos, antes de fin del mes siguiente; política escrita y derecho del trabajador a pedir su registro; en vigor desde el **1-oct-2024** [fuente: https://www.legislation.gov.uk/uksi/2024/831/made · https://assets.publishing.service.gov.uk/media/66a76a35ab418ab055592e86/statutory-code-of-practice-on-fair-and-transparent-distribution-of-tips.pdf]. Hay un **borrador de código revisado** publicado [fuente: https://assets.publishing.service.gov.uk/media/6a3d49dfda47783d87723b48/draft-revised-code-of-practice-on-fair-and-transparent-distribution-of-tips.pdf] (contenido no leído) | C1: el service charge **no** es venta de comida a efectos de food cost ni de GP |
| IVA / sales tax | Un service charge obligatorio de catering **tributa en sales tax** en Nueva York salvo que figure aparte como gratuity y se entregue íntegro al personal [fuente: https://www.nystax.gov/pubs_and_bulls/tg_bulletins/st/caterers_and_catering_services.htm (resumen de buscador)]. Otros estados: **[no medido]** | «If you make a service charge, it's standard-rated. But if the customer freely gives a tip above your total charge, no VAT is due on the tip» (§2.3) [fuente: https://www.gov.uk/guidance/catering-takeaway-food-and-vat-notice-7091, actualizada el 8-jun-2026] | 06 `Client Proposal`: «Prices exclude sales tax. A service charge of X % applies (not a gratuity)» |
| Nivel habitual | Service charge de catering **18-22 %** (rango 18-24 %) [fuente secundaria: resumen de buscador sobre blogs de catering de Seattle y Cvent]. Propina media en Toast: **19,3 %** en full-service y **15,8 %** en quick-service (1T-2026) [fuente secundaria: https://pos.toasttab.com/blog/data/restaurant-tipping-trends, resumen de buscador] | Service charge discrecional **12,5 %** habitual; 15 % cada vez más frecuente en Londres [fuente secundaria: resumen de buscador sobre startups.co.uk, visitlondon.com y otros] | Solo texto en las Instrucciones del 06 y del 10 |
| Precio anunciado | FTC: la norma de *junk fees* (mayo de 2025) solo alcanza a entradas de espectáculos y alojamiento de corta estancia **[no verificado en esta sesión]**. California (SB 478) obliga a incluir en el precio los cargos obligatorios **[no verificado en esta sesión]** | DMCC Act (desde el **6-abr-2025**): los cargos **obligatorios** deben ir en el precio de cabecera; los opcionales no [fuente secundaria: https://www.taylorwessing.com/en/insights-and-events/insights/2025/04/dmcca-drip-pricing] | Refuerza C1 y D6: en UK, lo que se imprime es el precio con IVA y sin service charge discrecional |
| Tip credit (salario de sala) | Federal: salario en efectivo **$2,13/h** + tip credit máximo $5,12 ($7,25 − $2,13); pool obligatorio con cocina **solo si no se aplica tip credit** [fuente: DOL FS#15, arriba]. Tabla estatal a 1-jul-2026: CA y WA sin tip credit (pagan el mínimo completo); TX y GA $2,13; FL $10,98; IL $9,00; NJ $6,05; MA $6,75; DC $10,30 [fuente: https://www.dol.gov/agencies/whd/state/minimum-wage/tipped] | No hay tip credit: el NLW se paga completo | Los costes de personal por defecto del 06 y del 08 usan salario completo, no el cash wage de sala |
| Reparto UK | — | El «tronc» (2.400 búsquedas/mes, §1.2) tiene su guía de NIC y PAYE en el folleto E24 de HMRC, actualizado el 18-jul-2025 [fuente: https://www.gov.uk/government/publications/e24-tips-gratuities-service-charges-and-troncs]. El detalle de la exención de NIC no se leyó (§8 del folleto) | Fuera del kit: es nómina |

### 2.2 Impuestos sobre el alcohol que tocan el pour cost

| Mercado | Qué hay | ¿Cambia la fórmula del 04? |
|---|---|---|
| EE. UU. (federal) | Excise sobre destilados: **$13,50 por proof gallon** (tipo general; $2,70 los primeros 100.000 del productor nacional) [fuente secundaria, resumen de buscador que cita https://www.ttb.gov/taxes/tax-audit/tax-and-fee-rates] | **No**: va dentro del precio de la botella |
| EE. UU. («control states») | **17 jurisdicciones** venden los destilados al por mayor a través de una agencia estatal [fuente secundaria: resumen de buscador sobre https://www.nabca.org/control-systems] | No: la tarifa estatal es el precio de compra. Sí explica por qué el precio de ejemplo es orientativo (research §9.1) |
| EE. UU. (impuestos que paga el bar sobre sus ventas) | **Texas:** *Mixed Beverage Gross Receipts Tax* **6,7 %** de los ingresos por bebidas servidas, **a cargo del titular del permiso**, más el *Mixed Beverage Sales Tax* **8,25 %**, que sí puede cobrarse al cliente [fuente secundaria: resumen de buscador sobre https://comptroller.texas.gov/taxes/mixed-beverage/receipts.php]. Otros estados o ciudades con impuestos parecidos: **[no medido]** | **Sí, en las Instrucciones del 04 (texto):** «If you pay a tax on your drink sales (e.g., Texas 6.7 % gross receipts), deduct it from the price before reading your pour cost» |
| Reino Unido | Alcohol Duty por graduación desde ago-2023, con **Draught Relief** para el barril. Actualización por RPI del **3,66 % el 1-feb-2026** [fuente secundaria: resumen de buscador sobre https://commonslibrary.parliament.uk/research-briefings/cbp-9765/] | No: la duty va en la factura del mayorista. Nota: «re-cost your drinks after each February duty change» |

### 2.3 Salarios mínimos 2026 (alimentan el personal del 06 y del 08)

| Mercado | Mínimo 2026 | Fuente |
|---|---|---|
| EE. UU. federal | **$7,25/h** | [fuente: https://www.dol.gov/agencies/whd/minimum-wage/state, actualizada el 1-jul-2026] |
| Estados (selección) | **DC $18,40** · **WA $17,13** · NY $17,00 (NYC, LI, Westchester) / $16,00 · CT $16,94 · **CA $16,90** · NJ $15,92 · OR $15,55 · CO $15,16 · AZ $15,15 · IL $15,00 · MA $15,00 · FL $14,00 · MI $13,73 · NV $12,00 · OH $11,00 · TX, PA y GA: el federal ($7,25) | ídem |
| California, comida rápida | **$20/h** en cadenas de 60 o más locales sin servicio de mesa, desde el 1-abr-2024; sigue vigente en 2026 [fuente secundaria: resumen de buscador sobre https://dir.ca.gov/dlse/minimum_wage.htm y otras] | |
| Cargas del empleador US | Seguridad Social **6,2 %** + Medicare **1,45 %** = **7,65 %** (base de SS 2026: $184.500) [fuente: https://www.irs.gov/taxtopics/tc751]. FUTA/SUTA y workers' comp: **[no medido]** | |
| Salarios de mercado US (OEWS, mayo de 2025, mediana por hora) | Chefs & head cooks **$30,03** · supervisores de F&B $21,19 · cooks, restaurant **$17,98** · food servers, nonrestaurant **$17,00** · waiters & waitresses $16,94 (incluye propinas) · bartenders $16,51 · fast food & counter **$15,00** · dishwashers $16,73 | [fuente: https://www.bls.gov/news.release/ocwage.t01.htm] |
| Reino Unido (desde el 1-abr-2026) | **NLW (21+) £12,71** (antes £12,21) · 18-20 años £10,85 · menores de 18 y aprendices £8,00 | [fuente: https://www.gov.uk/national-minimum-wage-rates] |
| Cargas del empleador UK 2026/27 | NIC del empleador **15 %** por encima de **£5.000 al año**; Employment Allowance **£10.500** | [fuente: https://www.gov.uk/guidance/rates-and-thresholds-for-employers-2026-to-2027] |
| Canadá | Federal **$18,15 desde el 1-abr-2026**, solo para sectores de competencia federal; la hostelería se rige por el mínimo de cada provincia **[no medido]** | [fuente secundaria: resumen de buscador sobre https://www.canada.ca/en/employment-social-development/news/2026/03/government-of-canada-raises-the-federal-minimum-wage.html] |
| Australia | Subida de los salarios de convenio del **4,75 %** desde el 1-jul-2026; el NMW, en **$26,44/h** según un resumen, pero otro habla de un 6 %: **contradictorio, verificar en fairwork.gov.au** (la página no respondió) | [fuente secundaria] |

---

## 3. Bloque 3 · Herramientas y software del sector (sustituye a «equipamiento»)

### 3.1 TPV y qué exportan (lo que puede aceptar el BONUS)

La hoja ES `Ventas del periodo` pide, por plato, **nombre (col. A) y raciones vendidas (col. B)**, y debajo las cantidades
brutas por ingrediente (comprobado hoy con openpyxl en `BONUS-mermas-inventario.xlsx`). Esas dos columnas son
exactamente lo que da el *product mix* de cualquier TPV:

| TPV | Informe | Exporta | Fuente |
|---|---|---|---|
| **Toast** (US) | Reports → Menus → **Product mix** (vista «Items»): nombre del artículo, **unidades vendidas**, ventas brutas y netas, descuentos, *waste count*… | **CSV o Excel** | [fuente: https://support.toasttab.com/en/article/Product-Mix-PMIX-Report-Overview (resumen de buscador)] |
| **Square** (US/UK/CA/AU) | Reports → **Item sales** / Custom Item report | **CSV o Excel** | [fuente: https://squareup.com/help/us/en/article/8363-view-item-category-and-modifiers-sales-reports (resumen de buscador)] |
| **Clover** (US) | **Item Sales report** | Exportable | [fuente: https://www.clover.com/en-US/help/run-or-request-the-item-sales-report (resumen de buscador)] |
| **Lightspeed Restaurant K-Series** (US/UK/CA/AU) | **Product Mix report** | **CSV/XLSX** | [fuente: https://k-series-support.lightspeedhq.com/hc/en-us/articles/4403156004763-Product-Mix-Report (resumen de buscador)] |
| **Epos Now** (UK) | **Sales by Product report** | **CSV, Excel, Word** (desde ordenador) | [fuente: https://support.eposnow.com/s/article/Sales-by-Product-Report?language=en_US (resumen de buscador)] |

Precios de TPV (contexto de la landing): Toast Starter **$0** (con comisión por transacción más alta) y Point of Sale
**$69/mes** [fuente secundaria: resumen de buscador sobre https://pos.toasttab.com/blog/on-the-line/how-much-does-a-restaurant-pos-system-cost];
Square for Restaurants tiene plan **Free**, Plus y Premium; en la página solo se leyeron los complementos de KDS/Kiosk
($20-50 por dispositivo) [fuente: https://squareup.com/us/en/point-of-sale/restaurants/pricing].

**→ C6 (solo texto):** en `Instructions` del BONUS: «Export your POS product mix (Toast *Product mix*, Square *Item sales*,
Clover *Item Sales*, Lightspeed *Product Mix*, Epos Now *Sales by Product*) and paste **item name + quantity sold** into
columns A-B of *Sales for the Period*». Sin importador ni macros: pegar dos columnas funciona igual en Excel y en Sheets.
El límite de filas de platos del ES se mantiene (regla de copia) y se dice en las Instrucciones.

### 3.2 Software de costes e inventario

| Producto | Mercado | Precio | Qué hace / qué exporta | Fuente |
|---|---|---|---|---|
| **meez** | US | Starter **$19/mes** (anual; $24 mensual) · Pro $89 · Premium $179 | Recetas y costes; **exporta costes de receta e ingrediente a CSV** e **importa costes de ingredientes desde una hoja de cálculo** | Precio: research §5.1 · [fuente: https://intercom.help/getmeez/en/articles/6014933-exporting-recipe-costs-or-ingredient-costs · https://intercom.help/getmeez/en/articles/4606257-importing-ingredient-costs-via-a-spreadsheet] (resúmenes de buscador) |
| **MarginEdge** | US | **$350/mes por local** | Facturas, inventario y costes; *PMIX mapping* (ventas del TPV → consumo teórico); exporta la lista de recetas a CSV/PDF | Precio: research §5.1 · [fuente: https://help.marginedge.com/hc/en-us/articles/360015333193-How-do-I-complete-PMIX-Mapping] |
| **xtraCHEF by Toast** | **Solo US** | Plan gratuito de facturas; costes de receta solo en planes de pago, **$149-299/mes + $1.049 de alta** según terceros (Toast no publica precio) | Facturas → costes | [fuente secundaria: resumen de buscador sobre dishcost.com, Capterra y Softabase] |
| **Restaurant365** | US | **$469-499 (Essential) / $689-749 (Professional) por local y mes**, sin precio público | ERP: contabilidad, inventario, recetas | [fuente secundaria: resumen de buscador sobre Capterra y otras] |
| **Galley** | US | [no medido] (su página de precios da 404) | Recetas; **exporta CSV con costes** | [fuente: https://support.galleysolutions.com/how-do-i-export-my-recipes (resumen de buscador)] |
| **Apicbase** | UE/UK/US | Presupuesto a medida; terceros citan desde **$149-249/mes** | Recetas, inventario, compras | [fuente secundaria] |
| **Jelly** | UK | **£129/mes por local** + alta + pasarela TPV desde £15/mes | Coste de recetas y menú, facturas, stock, pedidos | [fuente: https://www.getjelly.co.uk/pricing] |
| **Nory** | UK/IE | **£250-500+/mes** | Operaciones con IA (personal, inventario) | [fuente secundaria] |
| **Kitchen CUT** | UK | [no medido] (terceros dan cifras contradictorias) | F&B engine: recetas, compras, stock | [fuente secundaria] |

### 3.3 Cómo se pesa en una cocina de EE. UU.

- **Cocina salada:** la báscula de porciones clásica es de **esfera, 5 lb × 1 oz** (Edlund SR-5) o 5 lb × ½ oz / 2,2 kg ×
  20 g (Taylor); las digitales **cambian entre lb/oz y kg/g** [fuente: listados de producto en
  https://www.amazon.com/Edlund-SR-5-OP-Portion-Control-Capacity/dp/B003X848Z4 y
  https://www.hubert.com/product/88929/ (resúmenes de buscador)]. Porciones de línea en **oz**.
- **Pastelería:** se pesa, y en gramos, con **porcentaje de panadero**. En el ICE, pesar es la primera lección de Culinary
  y de Pastry & Baking [fuente secundaria: resumen de buscador sobre https://www.ice.edu/blog/baking-measurements y
  https://www.americastestkitchen.com/how_tos/5739-bakers-percentages-explained]. Recordatorio: fl oz (volumen) ≠ oz
  (peso) (ya en el research §4.2).
- **→ C4:** el 05 lleva los ejemplos con **unidad de receta en g** y compra en lb (la pareja `lb→g` ya está en
  `Conversions`). El resto del kit, en lb/oz como fija D7.

### 3.4 Dónde encaja un kit Excel de $19 (argumento honesto para la landing, C8)

| El comprador… | Kit de $19 | SaaS ($19-750 al mes por local) |
|---|---|---|
| Quiere saber hoy lo que le cuesta un plato y a cuánto venderlo | ✓ (01-08 + 10) | ✓ |
| Tiene 1 local, poco volumen o está abriendo (7 de cada 10 son de un solo local, §1.1) | ✓ pago único | Cuota mensual con alta y permanencia (R365, xtraCHEF, Jelly) |
| Hace un trabajo puntual: presupuesto de catering, plan de food truck, menú degustación | ✓ (06, 08, 02) | Sobra |
| Estudia o enseña costes | ✓ mismo método que los manuales (§6) | Licencias de empresa |
| Necesita facturas escaneadas, precios vivos del proveedor e integración con el TPV | ✗ **decirlo** | ✓ (es lo que venden) |
| Quiere validar sus números antes de contratar software | ✓. meez importa costes de ingrediente desde una hoja de cálculo (§3.2), así que la lista del kit se reaprovecha [estimado: verificar el formato antes de afirmarlo en la landing] | — |

Frase propuesta: *«No invoice scanning, no POS integration, no monthly fee. Eleven spreadsheets that do the math
software charges $19-$750 a month for — and that you keep.»* La cifra del rango sale de §3.2 (meez Starter y R365
Professional). **No** decir «replaces MarginEdge/R365».

---

## 4. Bloque 5 · Modelo de negocio (valores por defecto del 06, 08 y del PDF)

### 4.1 Economía del restaurante

| Métrica | EE. UU. | Reino Unido |
|---|---|---|
| **Beneficio antes de impuestos (mediana)** | **Full-service 2,8 %** · **limited-service 4,0 %** de las ventas (datos de 2024, *Restaurant Operations Data Abstract* 2025, más de 900 operadores) [fuente: https://restaurant.org/research-and-media/media/press-releases/new-resource-from-national-restaurant-association-provides-insights-into-operational-realities/, 20-ago-2025] | [no medido] (sin fuente pública; la NRA británica no existe como tal) |
| **Mano de obra con cargas (mediana)** | **FSR 36,5 %** (rentables 34,2 %; con pérdidas 42,9 %) · **LSR 31,7 %** (30,0 % / 34,1 %) [fuente: https://restaurant.org/research-and-media/research/restaurant-economic-insights/analysis-commentary/elevated-labor-costs-had-a-significant-impact-on-restaurant-profitability-in-2024/, 8-oct-2025] | [no medido] |
| **Prime cost** | LSR: **65 centavos por dólar** de ventas (mediana) [fuente: NRA, nota de prensa citada]. FSR: food & bev 28-35 % (research §2.1) + mano de obra 36,5 % ≈ **65-70 %** [estimado] | Alarma > 70 % (research §2.2) |
| **Food cost** | Research §2 | **GP %** en research §2.2 |
| **Regla 30/30/30(/10)** | 30 % comida, 30 % personal, 30 % gastos generales y 10 % de beneficio. Sale en el PAA de US y UK (research §6.3), pero **no cuadra con los datos**: el beneficio real mediano es del 2,8-4 %. Una fuente la actualiza a ≈ 33 % comida, 34 % personal, 27 % resto y 4-6 % de tecnología [fuente secundaria: resumen de buscador sobre https://www.directorders.com/blog/30-30-30-rule-for-restaurants] | Igual. El PAA UK pregunta por la «30/30/30/10» |
| **Ticket medio** | QSR $8-14 · fast casual $10-18 · casual $15-35 · fine dining $50-150+ por persona, antes de impuestos y propina [fuente secundaria: consenso de blogs, resumen de buscador; **sin fuente primaria**] | [no medido] |

**Cadenas cotizadas: food cost público** (sirve para el relato: «even the big chains live at 28-36 %»):

| Cadena (segmento) | Métrica | Dato | Fuente |
|---|---|---|---|
| Chipotle (fast casual) | Food, beverage & packaging / ingresos | 29,6 % (2025) | research §2.1 |
| Shake Shack (fast casual, hamburguesas) | Food & paper / ventas | **28,5 % en el año fiscal 2025** (28,2 % en 2024); 4T-2025: 28,7 % | [fuente: https://www.sec.gov/Archives/edgar/data/1620533/000162053326000013/shak-20260226_exhibit991.htm] |
| Darden (casual: Olive Garden, LongHorn…) | Food & beverage / ventas | **30,6 % en el año fiscal 2026** (cierre 31-may-2026); 30,3 % en el FY2025 | [fuente: https://www.sec.gov/Archives/edgar/data/940944/000094094426000016/exhibit991-q4fy26.htm] (porcentajes calculados por el lector de la página a partir de los importes: comprobar antes de publicarlos) |
| Texas Roadhouse (casual, steakhouse) | Food & beverage / ventas de restaurante | **36,4 % en el 4T-2025** (33,5 % en el 4T-2024); año 2025 ≈ 35,1 % (calculado) | [fuente: https://investor.texasroadhouse.com/news/news-details/2026/Texas-Roadhouse-Inc--Announces-Fourth-Quarter-2025-Results/default.aspx]. Buen ejemplo de **inflación del vacuno** (§4.2) |

### 4.2 Inflación de alimentos 2025-2026

| Serie | Dato | Fuente |
|---|---|---|
| **USDA ERS, previsión de agosto de 2026** (publicada el 25-ago-2026) | 2026: todos los alimentos **+3,0 %** (2,4-3,5) · en casa +2,5 % · **fuera de casa +3,6 %** (3,2-3,9). 2025 real: +2,9 / +2,3 / +3,8 %. Por categorías, 2026: **vacuno +9,8 %** · **huevos −30,8 %** · verdura fresca +5,9 % · azúcar y dulces +7,1 % · grasas y aceites a la baja. 2027: +2,4 % (fuera de casa +2,7 %) | [fuente: https://www.ers.usda.gov/data-products/food-price-outlook/summary-findings] |
| **ONS, IPC de agosto de 2026** (publicado el 16-sep-2026) | IPC 3,1 % · IPCH 3,3 % · **alimentos y bebidas no alcohólicas 1,3 %** · **restaurantes y hoteles 4,1 %** | [fuente: https://www.ons.gov.uk/economy/inflationandpriceindices/bulletins/consumerpriceinflation/august2026] |

Uso: la semana 3 del PDF («Negociar») y la semana 4 («Controlar») citan el vacuno (+9,8 %) y los huevos (−30,8 %) como
ejemplo de por qué **re-escandallar cada trimestre**: los platos de vacuno pierden margen y los de huevo ganan. Cuadra
con los precios BLS del research §9.1 (ground beef $6,32 → $6,92/lb; huevos $3,59 → $2,27/docena).

### 4.3 Food truck: costes diarios por defecto para el 08 (C3)

El ES tiene seis líneas de coste diario (300 €). Propuesta US, con la cuenta a la vista (22 días de servicio al mes y
260 al año) [estimado]:

| Línea ES → EN | Rango fuente | Valor US/día | Cuenta |
|---|---|---|---|
| Plaza/canon → **Commissary & parking** | Commissary $500-1.500/mes (full service), $300-800 compartido; parking $100-400/mes si va aparte [fuente secundaria: https://mobilefoodmath.com/guides/food-truck-commissary-costs, actualizada el 5-ago-2026] | **$45** | $1.000 ÷ 22 [estimado] |
| Seguros, licencias y tasas → **Insurance, permits & licenses** | Seguro: $2.500-8.400 al año según coberturas; Insureon: RC general $42/mes y auto comercial $170/mes de media [fuente secundaria: resumen de buscador sobre Insureon, MoneyGeek y mobilefoodmath]. Permisos: $500-3.000 al año; Boston > $17.000 [fuente secundaria] | **$25** | ($5.000 + $1.500) ÷ 260 [estimado] |
| Combustible/generador → **Fuel, propane & generator** | Generador y propano: $300-700/mes; propano ≈ $3/galón de media en 2026 [fuente secundaria: resumen de buscador sobre streetlegal.io] | **$30** | $500 ÷ 22 = $23 + desplazamientos [estimado] |
| Personal (2 × jornada) → **Staff (2 people)** | OEWS: cooks, restaurant $17,98 · fast food $15,00 (§2.3); FICA 7,65 % | **$300** | 2 × 8 h × $17 × 1,0765 = $293 [estimado] |
| Amortización → **Truck depreciation** | Camión equipado $50.000-175.000 [fuente secundaria: resumen de buscador] | **$50** | $90.000 ÷ 7 años ÷ 260 días [estimado] |
| Limpieza → **Cleaning, water & waste** | Agua y residuos $5-25 por visita si no van con el commissary [fuente secundaria: mobilefoodmath] | **$15** | [estimado] |
| **Total** | | **$465/día** | frente a 300 € en el ES |

Nota para las Instrucciones del 08: el salario mínimo va de **$7,25 a $18,40** según el estado, y las cadenas de comida
rápida de California pagan $20 (§2.3). Las ferias cobran cuota fija o un % de ventas **[no medido]**. UK: street van con
NLW £12,71 + NIC 15 %.

### 4.4 Catering: valores por defecto para el `Event Quote` del 06 (C2)

| Línea ES | Valor ES | Propuesta US | Base |
|---|---|---|---|
| Ratio camareros | 1/22 pax (cóctel) | **1 server / 25 guests** (recepción con pase) | Referencias del sector: **plated 1:10-12 · buffet 1:20 · cóctel con pase 1:25 · barra 1 bartender/50** (60-80 si solo cerveza y vino) [fuente secundaria: resumen de buscador sobre breakroomapp.com, premierstaff.com y otras]. La tabla va a las Instrucciones |
| Horas × €/h camarero | 5 h × 16 €/h | **5 h × $25/h** | Suelo W-2: OEWS *food servers, nonrestaurant* $17,00 × 1,0765 = $18,30; agencia: **$30/h con mínimo de 4 h** [fuente secundaria: resumen de buscador]. $25 = punto intermedio redondeado [estimado] |
| Jefe de sala | 6 h × 22 €/h | **6 h × $35/h** (captain) | Misma proporción que el ES (22/16 × $25 = $34,4) [estimado]. Suelo W-2: OEWS supervisores $21,19 × 1,0765 = $22,81 |
| Menaje | 1,20 €/pax | **Rentals $3,50/guest** | Vajilla y cubertería básicas desde ≈ $3/persona; copas $0,50-1 cada una [fuente secundaria: resumen de buscador sobre WeddingWire, eventslv.com y otras] + 1 copa [estimado] |
| Transporte · montaje | 150 € · 200 € | **$150 · $200** | [estimado] (sin fuente; valores que el usuario sustituye) |
| FC comida · margen servicios | 35 % · 20 % | 35 % (catering 28-35 %, D12) · **«Service charge (%)» 20 %** | Service charge US 18-22 % (§2.1) |
| Mínimo de facturación | 600 € | **$1.000** | [estimado] |
| IVA | 10 % | D6 (0 % por defecto) | En las Instrucciones: el service charge puede tributar (NY, §2.1) |
| `Client Proposal!A15` | «Precios con IVA incluido» | «Prices exclude sales tax. A X % service charge applies; it is not a gratuity» | DOL FS#15, Rev. Rul. 2012-18 |
| `Event Checklist` | «Registro sanitario y carnés de manipulador» | «Food handler cards / Certified Food Protection Manager on site» (ya en SPEC §2.5) + **«Staffing ratio confirmed (plated 1:10-12 · buffet 1:20 · passed 1:25)»** en sustitución de una fila, no añadida | — |

UK (solo en Instrucciones): personal de agencia en Londres **£18-24/h** (4 h mínimo, más VAT) [fuente secundaria:
resumen de buscador sobre thehospitalitycompany.co.uk y murphyseventhire.co.uk]; NLW £12,71 + NIC 15 % (§2.3);
catering standard-rated al 20 %.

---

## 5. Bloque 6 · Referentes

Para el relato de la landing y el apartado «Further reading» del PDF. **Nunca como aval**: ni logos ni «as taught at the
CIA». En la landing, fórmula genérica: *«Uses the standard AP → EP → yield % method taught in culinary schools»*. Los
títulos concretos, solo en el PDF.

### 5.1 Manuales y formación

| Referente | Qué es | Uso | Fuente |
|---|---|---|---|
| ***Culinary Math*, 4.ª ed.** — Linda Blocker y Julia Hill (ex profesoras del CIA), Wiley | Manual de referencia: yield % (cap. 7), coste de la porción comestible (cap. 10), **costeo de recetas (cap. 11)**, conversión métrica ↔ US. Trae un «Food Cost Form» | El 01 usa **la misma fórmula** (research §1.1). «culinary math» = 320 búsquedas/mes en US [medido DFS 24-sep] | [fuente: https://www.wiley.com/en-us/Culinary+Math,+4th+Edition-p-9781119195580 (resumen de buscador)] |
| ***Math for the Professional Kitchen*** — The Culinary Institute of America; Laura Dreesen, Michael Nothnagel y Susan Wysocki. Wiley, 2011 | Escalado, conversiones, costeo, precio de carta, rendimientos | Further reading | [fuente: https://www.wiley.com/en-us/Math+for+the+Professional+Kitchen,+1st+Edition-p-9781118692486R150 (resumen de buscador)] |
| ***Food and Beverage Cost Control*, 8.ª ed.** — David K. Hayes y Lea R. Dopson. Wiley, **agosto de 2026** (ISBN 978-1-394-36595-1). 7.ª ed. de 2019 | Texto universitario de control de costes: compras, producción, análisis de ventas, planificación del beneficio. La 8.ª añade un apartado sobre *off-premise* | Further reading. «food and beverage cost control» = 70/mes [medido DFS 24-sep] | [fuente: https://www.wiley.com/en-us/food-and-beverage-cost-control-7th-edition-p-9781394365951] |
| **ProStart (NRAEF)** | Programa de bachillerato en 2 niveles (currículo FRMCA): más de 234.000 alumnos en 2.275 centros | Segmento comprador (§1.3). En la landing, **no** nombrarlo | [fuente: https://chooserestaurants.org/programs/prostart/] |
| **ACF — Certified Executive Chef** | Pide conocimientos de *cost control management* y *beverage management* | Relato: los costes forman parte de la certificación del chef | [fuente secundaria: resumen de buscador sobre https://www.acfchefs.org/ACF/Certify/Levels/CEC/] |
| **City & Guilds 7133 (UK)** | Level 3 Diploma in Professional Cookery: «cost proposed recipes and work out gross profit» | Relato UK: GP % | [fuente secundaria: resumen de buscador sobre el handbook 7133] |

### 5.2 Voces y marcas que el comprador reconoce

| Referente | Por qué lo conoce el comprador | Uso | Fuente |
|---|---|---|---|
| **National Restaurant Association** | La patronal. Publica el *State of the Industry* y el *Operations Data Abstract* | Datos del PDF (§4.1) | Enlaces en §4.1 |
| **David Scott Peters** | «Restaurant coach»; libro *Restaurant Prosperity Formula: What Successful Restaurateurs Do* y pódcast homónimo. Predica el prime cost y el food cost teórico | Solo como contexto. **No citar** su cifra de marketing («−23 %») | [fuente: https://www.simonandschuster.com/books/Restaurant-Prosperity-Formula/David-Scott-Peters/9781642250398 (resumen de buscador)] |
| **RestaurantOwner.com** | Plantillas Excel de pago («Menu & Recipe Cost Spreadsheet Template»); aparece en la SERP | Competidor (research §5.1), no referente | SERP [medido DFS 24-sep] |
| **meez, MarginEdge, Toast, Jelly (UK)** | Sus blogs dominan las SERP informativas | Comparativa honesta (§3.4), sin enlazarlos | §3.2 |
| **Chipotle, Shake Shack, Darden, Texas Roadhouse** | Cadenas conocidas con food cost público | Tabla del PDF (§4.1): «the big chains run 28-36 %» | §4.1 |
| **Proveedores UK con calculadora de GP** (Brakes, Bidfood, Unilever Food Solutions, Total Foodservice) | Copan la SERP de «gp calculator» (5.400/mes UK) | Contexto de la FAQ UK | research §6.2 |

No se han verificado en esta sesión (no usar sin comprobar): fundadores concretos de meez o RestaurantOwner, y medios
británicos del sector.

---

## 6. Límites de este informe

- US por segmento: QCEW no ve a los negocios sin asalariados; el dato de 2023 de Nonemployer Statistics se quedó sin
  medir (el API del Census pide clave desde hoy).
- Los costes de food truck y catering son **secundarios**: blogs del sector, sin encuesta primaria. Por eso cada valor
  por defecto lleva `[estimado]` y la cuenta, y las Instrucciones dicen «replace with your own quotes».
- Las cifras de Darden y Texas Roadhouse del año completo las calculó el lector de la página: verificar en F2 si se
  publican en el PDF.
- Canadá y Australia: solo recuentos agregados y salario mínimo; el de Australia es contradictorio.
- No verificados en esta sesión: la norma de *junk fees* de la FTC, California SB 478 y la exención de NIC del tronc.

### Log

- **2026-09-24 (sesión Claude Code, subagente de F1-8b-A):** BLS QCEW (4T-2025, 10 NAICS por CSV abierto), ONS
  `ah1864.xlsx` + Nomis `NM_141_1`/`NM_142_1` (5 SIC), BLS OEWS mayo de 2025, DOL (salario mínimo estatal y de
  propinas, FS#15), gov.uk (NLW, NIC, VAT Notice 709/1, E24), IRS (FICA), USDA ERS (ago-2026), ONS IPC (ago-2026), SEC y
  notas de resultados (Shake Shack, Darden, Texas Roadhouse), NRA. DataForSEO: 2 consultas de volumen (24 keywords US
  y 20 UK) y 1 SERP («prime cost», que resultó ser de Amazon Prime). Revisada la hoja `Ventas del periodo` del BONUS ES
  con openpyxl, solo lectura. Temperatura máxima: 53 °C.
