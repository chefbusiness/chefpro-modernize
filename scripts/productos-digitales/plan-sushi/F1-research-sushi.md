# Plan de Negocio: Sushi Bar (ES) · F1 research (caso, normativa, demanda, jerga, riesgos y calculadora)

> Sesión Claude Code, 31-oct-2026 (F1 nocturna, decisiones delegadas). Una pasada. **Reutiliza** lo que ya está leído y no lo repite:
> el mapa de palabras clave (`F0-mapa-keywords-es-en.md`, **F0 §n**); la normativa leída en origen por la Pollería y la Taquería
> (`../plan-polleria/F1-research-polleria.md` **POL §n**, `../plan-taqueria/F1-research-taqueria.md` **TAQ §n**: IAE, Ley 12/2012, RD
> 126/2015, RD 1021/2022 arts. 3-11, LIVA 91, Ley 7/2022, Ley 1/2025, convenio, SMI, Veri\*factu, plataformas); el anisakis corregido el
> 29-ago (`../auditorias/anisakis-rd1021-correccion-2026-08-29.json` y `guias-v2-research-sector.json` ANIS-01…06, **ANIS**); y el oficio del
> **Kit de Tareas Sushi Bar** LIVE (14 €, `dl/kit-tareas-sushi-bar/`, auditorías `kit-tareas-sushi-bar-R1.json` y
> `kit-tareas-cb-v2-contenido-kit-tareas-sushi-bar.json`, **KT**: pH del shari, registro de congelación, vitrina, alérgenos, temporadas) y
> de la **Guía Restaurante Japonés** (65 €, `dl/guia-restaurante-japones/`, **GJ**: modelos, equipo, brigada, proveedores, escandallos).
> Hoy, leído en origen: **RD 1086/2020 art. 30** entero y la tabla del art. 4.1 del RD 1021/2022 (lector sonnet, texto consolidado del BOE),
> **LIVA art. 91.Dos.1.1.º** (consolidado del BOE, Mac). Precios, equipo, salarios, cartas y franquicias: un lector sonnet (44 llamadas; Makro
> y comercios con JS solo dan snippet). Etiquetas: **[medido]** = leído hoy en la página del vendedor o el documento · **✅** = norma leída
> hoy en origen · **✅ hermano** = leída por otra F1 (se dice cuál) · **🟡** = snippet, marketplace o secundaria · **[criterio del plan]** =
> estimación del kit con el cálculo a la vista · ❌ = no encontrado.

## 0. Los 9 hallazgos que mandan

1. **El sushi bar vende piezas en tres canales, y el delivery pesa.** El maki es el **segundo plato más pedido del delivery en España**, tras
   la hamburguesa (Gastrómetro Just Eat 2025, vía The Objective, 9-dic-2025 🟡). El caso reparte **sala ≈ 62 %, para llevar ≈ 12 %,
   plataforma ≈ 26 %** (§3) y por eso la unidad del motor es el **comensal equivalente** (un pedido = 1,6 comensales), con la rotación
   encendida: la barra y las mesas sí rotan (como la Taquería, no como la Pollería).
2. **Anisakis: la norma vigente es el RD 1021/2022, art. 8.** El **RD 1420/2006 está derogado desde el 22-dic-2022** (ANIS-01 ✅ hermano):
   el encargo lo citaba y el gate lo prohíbe. Art. 8.1: pescado para consumo en crudo **congelado a ≤ −20 °C en la totalidad del producto ≥ 24
   h, o ≤ −35 °C ≥ 15 h** (también puede venir hecho de una etapa anterior si está documentado); art. 8.2: **informar al consumidor** (carta o
   cartel) de que se ha congelado o de que procede de acuicultura libre de anisakis; Rgto. (CE) 853/2004, anexo III, secc. VIII, cap. III.D
   (redacción del Rgto. (UE) 1276/2011) y su excepción de acuicultura **acreditada por escrito** (ANIS-03/04/05 ✅ hermano, KT DOM-15).
   **En la UE el atún salvaje NO está exento** (en EE. UU. sí: US delta §6) → atún ultracongelado con documento o congelación propia.
3. **El shari a temperatura ambiente no lo ampara ninguna norma española de forma expresa.** RD 1086/2020 art. 30.2 ✅: las comidas
   preparadas «se servirán para su consumo cuanto antes, a menos que se refrigeren, congelen o se mantengan a una temperatura superior o
   igual a 63 °C»; la única salida es el **30.5** ✅: el operador «podrá establecer temperaturas de conservación diferentes de las
   establecidas en el apartado 3, siempre que demuestre a la autoridad competente que estas temperaturas están basadas en evidencias
   científicas». Ni «arroz», ni «pH», ni «vinagre» aparecen en el RD 1086/2020 ni en el RD 1021/2022 ✅ (barrido del texto). → El plan lo dice
   así: **shari a temperatura ambiente solo con el APPCC validado** (pH medido por lote ≤ 4,6, Codex CXC 23-1979, = KT; muchas autoridades de
   EE. UU. piden < 4,2: apunta a 4,2-4,3 para tener margen [criterio del plan]; tiempo máximo fijado por el APPCC) **y comunicado a sanidad**;
   si no, refrigerado. Nadie en la SERP lo cuenta; la Guía Japonés da «20-25 °C, máx. 4 h» sin norma (GJ §6: no se copia).
4. **El salmón paga la carta; el atún, el langostino y la merma la encarecen.** Salmón noruego de acuicultura entero ≈ 11,95 €/kg minorista
   (El Corte Inglés vía agregador 🟡), en origen NOK 70-88/kg ≈ 6-7,5 €/kg (abr-may 2026 🟡); lomo o filete congelado Makro **20,7-21,8
   €/kg** (METRO Chef y Leroy 🟡). **Rendimiento del entero a lomo limpio: 50-60 %** (🟡, dos blogs de gestión; sin fuente técnica ❌). Atún
   aleta amarilla de importación 14,70-26,82 USD/kg (Tridge 🟡); saku ultracongelado sin precio en España ❌. **El escandallo teórico de una
   carta con 60 % de salmón sale en ≈ 20-22 %** (§2); con merma de vitrina, recortes y comidas del personal, **el caso usa 29 %** (GJ da
   30-35 % para un japonés completo con pescado premium).
5. **«¿Cuántos sushis salen con 1 kilo de arroz?» (PAA) tiene respuesta de calculadora**: ≈ 20 g de shari por nigiri (Directo al Paladar
   🟡) y × 2,2 de crudo a cocido (Just One Cookbook 🟡) + ≈ 10 % de sushi-zu (KT DOM-22) → **1 kg de arroz crudo ≈ 2,4 kg de shari ≈ 120
   nigiris** [criterio del plan]; el arroz para sushi cuesta **1,81-1,85 €/kg sin IVA** en Makro (METRO Chef y DACSA, 5 kg 🟡) y el japonés
   2,50-8,10 €/kg (🟡 / [medido] Japonshop). El arroz es barato: el coste está en el pescado y en la mano del itamae.
6. **El itamae es la contratación difícil (y la que sostiene la carta).** Ofertas de sushiman: **12.000-22.000 € brutos/año** (InfoJobs,
   Paracuellos 🟡), 20.000 € (EURES, Fuerteventura 🟡), «desde 2.500 €/mes» en un omakase de Ibiza (🟡); GJ: itamae 3.000-4.500 €/mes en un
   japonés premium. Caso: **titular-itamae a 2.200 €** y sushiman a 1.650 € (§3); las ofertas de 12.000 € son media jornada o bajo convenio
   y no sirven de coste.
7. **La inversión de mercado va de un quiosco a un restaurante**: Sushimore **39.950 € + obra, 38 m²**; Miss Sushi **desde 200.000 €, 120 m²**;
   Sibuya Urban Sushi Bar **300.000 €, 180 m²**, canon 30.000 €, royalty 4 % + 1 % (emprendedores.es [medido]); la SERP da «50.000-160.000 €»
   para un sushi bar (🟡). **Caso: 36 plazas en 95 m², 103.350 € de inversión** (§3), la franja baja de un local con barra.
8. **IVA: comida al 10 %; arroz, verdura, aguacate, huevo y queso se compran al 4 %.** LIVA 91.Dos.1.1.º ✅ (hoy): «d) Los quesos. e) Los
   huevos. f) Las frutas, verduras, hortalizas, legumbres, tubérculos y **cereales**, que tengan la condición de productos naturales…» → el
   arroz para sushi va al 4 %; pescado, algas, salsas y surimi al 10 % → **`IVA_COMPRAS` 0,087** (§1). La cerveza, el sake y los refrescos
   azucarados que salen del local, al 21 % (✅ hermano POL §0.9).
9. **Los alérgenos del sushi no caben en «pescado y soja».** Pescado, crustáceos (langostino, ebi), moluscos (pulpo, vieira), soja **y trigo
   de la soja**, sésamo, huevo (tamago, mayonesa japonesa del spicy), leche (queso crema), gluten (tempura, panko y **surimi**, que suele
   llevar almidón de trigo y clara de huevo 🟡 según etiqueta), **mostaza en algunas pastas de wasabi** (son rábano picante teñido —S&B 31 %
   de rábano y 4,5 % de wasabi— y la AESAN alertó en 2020 de mostaza no declarada en snacks de wasabi 🟡: leer la etiqueta de la marca) y
   sulfitos (vino, algunos encurtidos). KT ya corrigió la lista de 4 que omitía el pescado (KT DOM-07).

## 1. Marco legal y fiscal (lo que el producto afirma)

| Tema | Regla para el plan | Fuente · estado |
|---|---|---|
| IAE | Sushi bar con sala: **671.x** (restaurante, por categoría) o 673.2; la venta para llevar la faculta la nota común de 671-673; si el para llevar fuera la actividad principal, 677.9 (variante dark kitchen) | ✅ hermano POL §1 (agrupación 67 leída el 29-oct) |
| Apertura | Licencia o declaración responsable (agrupación 67 fuera del anexo de la Ley 12/2012); consulta urbanística previa: uso, **extracción** (freidora de tempura y plancha), aforo | ✅ hermano TAQ §1, POL §1 |
| Humos | Cocina eléctrica (inducción, freidora, plancha de gyozas) → campana con filtros y conducto exclusivo a cubierta; sin leña ni carbón en el caso (la robata de binchotan es variante: filtro de partículas, OCAS 4/2021 de Madrid art. 23 como ejemplo) | ✅ hermano POL §1, PIZ §1 · GJ §9 |
| Registro sanitario | Declaración responsable → registro autonómico; venta a otros bares solo marginal (RD 1021/2022 art. 3) | ✅ hermano POL §1 |
| **Anisakis** | Hallazgo 2. Registro por lote (especie, origen, fecha y hora de entrada y salida del congelador, temperatura), documento del proveedor si llega congelado o si es acuicultura exenta; **información al consumidor en carta o cartel** (art. 8.2) | RD 1021/2022 art. 8.1-8.2 · Rgto. 853/2004 anexo III secc. VIII cap. III.D (Rgto. 1276/2011) ✅ hermano ANIS · KT DOM-14/15 |
| Pescado fresco en cámara y vitrina | **0-4 °C** (tabla del art. 4.1, punto 7: productos de la pesca frescos y crustáceos y moluscos cocidos); congelado ≤ −18 °C (el −20 °C es el del anisakis, no el del congelador general, KT DOM-02); descongelación en cámara | RD 1021/2022 art. 4.1 ✅ (hoy) |
| **Shari** | Hallazgo 3: refrigerar, mantener ≥ 63 °C o temperatura distinta **validada** (art. 30.5) con pH por lote y tiempo máximo en el APPCC | RD 1086/2020 art. 30.2 y 30.5 ✅ (hoy, BOE-A-2020-15872) · Codex CXC 23-1979 (KT) |
| Comidas preparadas | Frías ≤ 4 °C (vida > 24 h) u ≤ 8 °C (< 24 h); calientes ≥ 63 °C; enfriado 60 → 10 °C en < 2 h; recalentado ≥ 74 °C 15 s (gyoza, karaage, ramen si lo hay) | RD 1086/2020 art. 30.3-30.7 ✅ (hoy) |
| Histamina | Atún, caballa, pez limón y bonito: cadena de frío desde la recepción; criterio de histamina del Rgto. (CE) 2073/2005 para el operador que comercializa (en el restaurante, APPCC de recepción) | 🟡 (no releído hoy) |
| Etiquetado | Sin envasar o envasado a petición: denominación y alérgenos (art. 4). **Bandejas de combinado ya cerradas en vitrina o para recoger antes del pedido = art. 5**: ingredientes, alérgenos resaltados, peso, fecha y conservación | RD 126/2015 arts. 4-5 ✅ hermano POL §0.4 |
| Alérgenos | Hallazgo 9; información escrita o de palabra con registro escrito y accesible | RD 126/2015 arts. 4.1.b y 6.5.a ✅ hermano TAQ §1 |
| «Sin gluten» | ≤ 20 mg/kg: no prometerlo con soja de trigo, tempura y freidora compartida (tamari sin gluten es opción, sin prometer) | Reg. Ej. (UE) 828/2014 ✅ hermano |
| IVA de ventas | Comida en sala, para llevar y a domicilio al 10 %; **cerveza, sake, vino y refrescos azucarados que salen del local al 21 %** (91.Uno.1.1.º a y b) | LIVA ✅ hermano POL §0.9 |
| IVA de compras | Pescado, marisco, algas, salsas, surimi, gyozas y bebida sin alcohol al 10 % (≈ 79 % de la compra de comida); arroz, verdura, aguacate, fruta, huevo y queso crema al 4 % (≈ 21 %) → **0,087**, solo comida (lección de la Pizzería) | LIVA 91.Dos.1.1.º d, e y f ✅ (hoy) · pesos [criterio del plan] |
| Envases y desperdicio | Envase de plástico de un solo uso cobrado aparte (Ley 7/2022 art. 55); lo no consumido en sala se lo lleva el cliente sin coste (Ley 1/2025 art. 8) | ✅ hermano TAQ §1 |
| Convenio, SMI, jornada, Veri\*factu | Hostelería provincial; SMI 1.221 €/mes × 14; cargas 33 %; registro de jornada (sin «digital obligatorio»); TPV con Veri\*factu | ✅ hermano TAQ §1 · 🟡 |
| LatAm (solo guía de equivalencias) | El marco es español: el plan lo dice y remite a la gestoría local; anisakis y pescado crudo tienen norma propia en cada país (no se cubre) | — |

**Citas literales leídas hoy (para el Word y el checklist)**

| Norma | Literal | Fuente |
|---|---|---|
| RD 1086/2020 art. 30.2 | «Las comidas preparadas se elaborarán con la menor antelación posible a su consumo, se servirán para su consumo cuanto antes, a menos que se refrigeren, congelen o se mantengan a una temperatura superior o igual a 63 °C.» | [BOE-A-2020-15872](https://www.boe.es/buscar/act.php?id=BOE-A-2020-15872) ✅ |
| Ídem, 30.5 | «El operador que produzca las comidas preparadas podrá establecer temperaturas de conservación diferentes de las establecidas en el apartado 3, siempre que demuestre a la autoridad competente que estas temperaturas están basadas en evidencias científicas y que se garantice la seguridad de los productos.» | ✅ |
| RD 1021/2022 art. 8.2 | «…deberán informar a las personas consumidoras de que dichos productos han sido congelados o, en su caso, que proceden de sistemas de acuicultura que garantizan que están libres de anisakis, mediante los procedimientos que estimen apropiados, entre otros, mediante carteles o cartas-menú.» | [BOE-A-2022-21681](https://www.boe.es/buscar/act.php?id=BOE-A-2022-21681) ✅ hermano (29-ago) |
| LIVA 91.Dos.1.1.º f | «Las frutas, verduras, hortalizas, legumbres, tubérculos y cereales, que tengan la condición de productos naturales de acuerdo con el Código Alimentario y las disposiciones dictadas para su desarrollo.» | [BOE-A-1992-28740](https://www.boe.es/buscar/act.php?id=BOE-A-1992-28740) ✅ |

## 2. Benchmarks España

| Dato | Valor | Fuente |
|---|---|---|
| Demanda de delivery | Maki, 2.º plato más pedido del delivery (tras la hamburguesa, antes del durum) | Gastrómetro Just Eat 2025 vía The Objective, 9-dic-2025 🟡 |
| Nº de restaurantes japoneses | Sin fuente fiable ❌ (un blog comercial da cifras que no cuadran: no se usa). GJ dice «+2.400 (2025)» sin fuente: **no se copia** | 🟡 / ❌ |
| Precios de carta (con IVA) | **Sibuya León** (cadena): nigiri 2,60 € la pieza (anguila 2,90 €), Nigiri Lovers 10 pzs 22,60 €, uramaki 9,60-12,60 € el rollo, flamed 13,90-14,90 €, combinados de 24 pzs 24,90-30,60 €, 28 pzs 36,60 €, 52 pzs 65,90 € · **Kioto (Valencia)**: nigiri 2,50 € la pieza, uramaki 5,90-6,50 € las 4 pzs · **Ichiwaka**: nigiri 2 pzs 5,20-6,50 €, **menú del día 13,95 €** | conmenu.com [medido] · 🟡 · 🟡 |
| Buffet libre (variante) | Valencia: < 20 € de lunes a jueves, 28,50 € el fin de semana (may-2026) · Barcelona (parrilla y sushi): 16,90 € mediodía, 26,90 € cenas | El Español · Barcelona Secreta 🟡 |
| Omakase, kaiten | Sin precio de menú ❌; GJ: omakase 80-180 € de ticket, barra de 8-12 plazas | GJ §3 |
| Franquicias | Sibuya 300.000 € (Asest: desde 350.000), canon 30.000 €, 4 % + 1 %, 180 m², 15 propios + 25 franquiciados (79 operativos en 2025 según JustRetail 🟡) · **Miss Sushi** desde 200.000 €, canon 29.000 €, 5 % + 300 €/mes, 120 m² · **Sushimore** 39.950 € + obra, 3 % + 2 %, 38 m² (stand 23 m²), 21 locales · Makitake desde 30.000 € · Sushicatessen desde 37.000 € · Igua Sushi Art 67.300 € + obra (🟡) | emprendedores.es [medido] · 🟡 |
| Arroz para sushi (sin IVA) | METRO Chef 5 kg **1,81 €/kg** · DACSA «sinzu» 5 kg **1,85 €/kg** · Sushima 20 kg 2,50 €/kg · japonés Haruka 8,10 €/kg · Koshihikari 1 kg 3,49 € | Makro 🟡 · Okidoki 🟡 · Japonshop [medido] |
| Salmón | Noruego entero de acuicultura ASC **11,95 €/kg** (minorista) · origen NOK 70-88/kg (≈ 6-7,5 €/kg) · **lomos o filete congelado 20,7-21,8 €/kg** (Makro METRO Chef 5 × 150 g; Leroy 1-2 kg) · Mercamadrid: sin precio de salmón publicado ❌ | 🟡 (agregador, Undercurrent, pulse.bot, Makro) |
| Atún | Aleta amarilla fresco de importación **14,70-26,82 USD/kg** (2024, entero) · saku ultracongelado (−60 °C) 114,95 €/kg en una tienda alemana (no es referencia de hostelería) · atún rojo de acuicultura, ebi, langostino de tempura, surimi, masago: ❌ | Tridge 🟡 · honest-catch 🟡 |
| Nori, vinagre, wasabi | Nori Gold 100 hojas **25,95 € = 0,26 €/hoja** (minorista; 10 hojas 0,59-0,77 €/hoja) · vinagre de arroz 500 ml 6,05-7,99 € (12-16 €/l minorista) · wasabi en pasta 43 g 2,25-2,35 € | Oriental Market 🟡 · Japonshop [medido] |
| Rendimientos | Salmón entero → lomo limpio para sushi **50-60 %** · atún lomo → saku ❌ (US: 45-65 %, fuentes que se contradicen) · shari **≈ 20 g por nigiri** · crudo → cocido **× 2,2** · sushi-zu ≈ 10 % del arroz cocido | beancount.io y modelosdeplandenegocios 🟡 · Directo al Paladar 🟡 · Just One Cookbook 🟡 · KT DOM-22 |
| Equipo (sin IVA) | Vitrina de sushi Polar 6 GN 1/3 **999 €** · arroceras Buffalo 4,2 l 99 € y 8 l **483,50 €**, Hendi con calentador 5,4 l 258,05 €, Eutron 18 l 335 € · abatidor de 5 bandejas 1.189 € (Chefook, sin −35 °C) y Edenox AM-05 (+3/−18 °C) 5.395 € PVP · GJ: congelador certificado −20 °C 3.000-5.500 €, vitrina de barra 4.500-9.000 €, set de cuchillos 1.500-4.500 € · robot de sushi en España ❌ (US: Suzumo de segunda mano 13.600 USD) | hosteleria10 (PDF) 🟡 · chefook 🟡 · GJ §9 |
| Salarios | Sushiman 12.000-22.000 €/año (InfoJobs) · 20.000 € (EURES) · omakase Ibiza desde 2.500 €/mes · Jooble 2.802 €/mes (dudoso) · GJ: itamae 3.000-4.500 €/mes, sushi chef 2.200-2.800 € (premium) | 🟡 · GJ §12 |
| Plataformas · alquiler | Glovo 15-35 % + IVA, Uber Eats 30 % + IVA, Just Eat 13-35 % · alquiler 12-20 €/m²/mes | ✅ hermano 🟡 (PIZ §2, TAQ §2) |

**Escandallos del caso** (sin IVA; neta 15 g por nigiri [criterio del plan: «pesa 10 lonchas»], salmón entero a 9,50 €/kg con 55 % de lomo y
15 % de recorte reaprovechado en tartar y maki → **13,57 €/kg útil**, 14,28 €/kg con un 5 % de merma de vitrina; shari ≈ 1,2 €/kg; nori 0,26
€/hoja) [criterio del plan]:

| Producto | Coste | PVP sin IVA (con IVA) | Coste % |
|---|---|---|---|
| Nigiri de salmón (2) | 0,53 € | 4,73 € (5,20 €) | **11 %** |
| Nigiri de atún aleta amarilla (2), saku a 26 €/kg con 90 % de corte | 0,97 € | 5,45 € (6,00 €) | 18 % |
| Uramaki California (8): 120 g de shari, ½ nori, surimi, aguacate, pepino, masago | 0,80 € | 8,73 € (9,60 €) | 9 % |
| Uramaki de langostino en tempura (8) | ≈ 1,65 € | 10,45 € (11,50 €) | 16 % |
| Sashimi de salmón (5 cortes de 15 g) | 1,12 € | 6,82 € (7,50 €) | 16 % |
| Poke de salmón (100 g, arroz, aguacate, edamame, mango, salsa) | ≈ 2,40 € | 11,73 € (12,90 €) | 20 % |
| Combinado de 24 piezas (delivery), con su caja | ≈ 4,20 € | 26,36 € (29,00 €) | 16 % (+ caja 0,90 €) |
| Gyozas (6) | ≈ 1,10 € | 6,36 € (7,00 €) | 17 % |
| **Teórico ponderado de la carta** (60 % salmón; atún, langostino, anguila y gyozas el resto) | | | **≈ 20-22 %** |

**Del 21 % teórico al 29 % del caso** (puente que el Word explica y la calculadora deja medir): merma de pescado no vendido y recorte no
reaprovechado +4 · shari, nori y salsas tirados al cierre +1 · comidas del personal, invitaciones y errores de pedido +2 · menú del día de
mediodía con margen bajo +1 = **≈ 29 %**. Con lomo comprado limpio (≈ 23,7 €/kg útil) el nigiri de salmón sube del 11 al 17 %: la
calculadora compara entero frente a lomo.

## 3. Caso España 2.2 (comensales equivalentes × ticket × días; motor de planes)

**Variantes** [criterio del plan]:

| Variante | Local | Plazas | Mezcla | Lectura |
|---|---|---|---|---|
| A · Sushi para llevar y a domicilio (dark kitchen o mostrador) | 40-60 m² | 0-6 | 100 % fuera | El formato Sushimore (39.950 € + obra); 677.9; techo de plataforma alto. Solo en el Word |
| **B · Sushi bar de barrio con barra y mesas (ELEGIDA)** | **95 m²** | **36** (8 en barra) | **sala ≈ 62 %, para llevar ≈ 12 %, plataforma ≈ 26 %** | Itamae a la vista, carta corta, menú del día a mediodía |
| C · Barra omakase (10-12 plazas) | 60-80 m² | 10-12 | 100 % sala, reserva | Ticket 80-150 € (GJ): otro negocio; Word |
| D · Kaiten o buffet libre | 150-250 m² | 80-120 | sala | Precio cerrado 17-28,50 € (🟡): volumen y merma propios; Word |
| E · Nikkei · F · japonés completo (ramen, izakaya, robata) | | | | Remiten a la **Guía Restaurante Nikkei** y a la **Guía Restaurante Japonés** |

**Local tipo (B)**: barrio con vida de noche en una ciudad de 150.000-500.000 habitantes (o un barrio de Madrid, Barcelona, Valencia); 95 m²
ya de restauración, sin traspaso; **barra de sushi a la vista con vitrina refrigerada de neta** (8 taburetes), sala de 28 plazas, cocina
eléctrica (arroceras, inducción, freidora de tempura, plancha de gyozas), cuarto frío con armario de pescado a 0-2 °C y **armario congelador
de −20 °C con registrador** (anisakis); zona de empaquetado de pedidos junto a la puerta. **Carta corta** (≈ 35 referencias): nigiri,
sashimi, hosomaki, uramaki, temaki, combinados de 12-24-36 piezas, poke, gyozas, edamame, sopa de miso, mochi; cerveza japonesa, sake, vino,
refrescos, té. **Menú del día** a mediodía de martes a viernes (13,95 € con bebida). **Horario**: martes a domingo 13:00-16:00 y 20:00-23:30
(plataforma en los dos servicios); cierra los lunes y 10 días en agosto (la ciudad se vacía).

**Derivación** (media del año; 1 pedido para llevar o de plataforma = **1,6 comensales equivalentes**) [criterio del plan]:

| Día | Sala (comensales) | Para llevar (pedidos) | Plataforma (pedidos) | Comensales equivalentes |
|---|---|---|---|---|
| Martes y miércoles (× 2) | 30 | 5 | 9 | 52 |
| Jueves | 40 | 6 | 11 | 67 |
| Viernes | 58 | 9 | 18 | 101 |
| Sábado | 66 | 10 | 20 | 114 |
| Domingo | 46 | 10 | 18 | 91 |
| **Semana (6 días)** | 270 → **45/día** (1,25 por plaza) | 45 → 7,5/día | 85 → 14,2/día | **478 → ≈ 79/día** (2,2 por plaza con todo) |

**Ticket** (con IVA → sin IVA): comensal de sala = 30 % menú del día 14,90 € + 70 % cena o fin de semana 28,60 € (≈ 22 € de comida y 6,60 €
de bebida) = 24,50 € → **22,26 €** · pedido para llevar (combinado de 24 + extra) 27,00 € → 24,55 € → **15,34 € por comensal equivalente** ·
pedido de plataforma (precio +15 %) 32,50 € → 29,55 € → **18,47 €**. Venta diaria (45 × 22,26 + 7,5 × 24,55 + 14,2 × 29,55) ≈ 1.605 € ÷ 79,7 =
20,14 € → el caso usa **20,00 €**. Reparto: **sala 62 %, para llevar 12 %, plataforma 26 %**.

| Clave del motor | Rótulo sushi bar | Valor | Fuente |
|---|---|---|---|
| `cubiertos_dia` | Comensales al día (sala + equivalentes de llevar y domicilio: 1 pedido = 1,6) | **79** (sábado 114; martes 52) | tabla |
| `ticket_medio` · `dias_apertura` | € por comensal sin IVA · días | **20,00 €** · **300** (365 − 52 lunes − 10 de agosto − 3 sueltos) | arriba |
| Ventas a régimen | | **79 × 20,00 × 300 = 474.000 €** · sala ≈ 296.000 · llevar ≈ 54.000 · plataforma ≈ 124.000 | |
| `crec_a2` / `crec_a3` | | 6 % / 4 % | = Taquería |
| Líneas (2) | Comida (sushi, poke, cocina caliente, postres) / Bebida (cerveza, sake, vino, refrescos, agua, té) | **85 % / 15 %** (sala ≈ 22 % de bebida; fuera ≈ 4 %) | [criterio del plan] |
| Bebida que sale del local al 21 % | Línea partida del motor (sexto campo) | ≈ 1,05 % de las ventas → **`pct` 0,07** de la bebida | LIVA ✅ hermano |
| `coste_comida` · `coste_bebida` | | **29 %** (puente de §2) · **28 %** | §2 |
| `pct_consumibles` | Cajas de sushi, tarrinas de soja, palillos, bolsas, servilletas, toallitas | **3,0 %** (≈ 0,90-1,20 € por pedido; GJ 1,20-2,80 €) | [criterio del plan] |
| `pct_delivery` / comisión | | **0,25 / 0,30** (7,5 % de las ventas) | §2 ✅ hermano |
| TPV · varios | | 0,8 % · 2 % | molde |
| `alquiler_mes` · fianza · renta previa | | **1.600 €** (95 m² × ≈ 17 €/m²; 4,1 %) · 2 · 2 | [criterio del plan] |
| `suministros_mes` · `seguros_ano` | Cocina eléctrica, frío intensivo (pescado, congelador de −20 °C), extracción, clima | **1.100 €** · **1.800 €** (RC con pescado crudo) | [criterio del plan] |
| Financiación | | propios **55.000 €** + préstamo **≈ 128.000 € (CALIBRAR en F2)** · 6 %, 7 años, 1 de carencia · fondo 3 meses · vidas 10/10 | = Taquería |
| `aforo` · `ROTACION` | | **36** · techo **3,0** (comida + cena + segundo turno del sábado); referencia: incluye los pedidos; la de tu sala ronda 1,25 | [criterio del plan] |
| Rampa · cobro/pago · pagas | | 0,75 en 4 · 2 / 30 · 7 y 12 | = Taquería |
| `IVA_COMPRAS` · Mes 1 | | **0,087** · **enero** | §1 · = familia |

**Plantilla** (7 filas; 14 pagas; todos ≥ SMI a prorrata) [criterio del plan]: titular — **itamae** y gerente (compra y corte del pescado,
carta, proveedores, APPCC del anisakis) 1,00 × **2.200** · **sushiman/sushiwoman** (shari, rolls, combinados de plataforma) 1,00 × **1.650** ·
cocinero/a de cocina caliente y arroz (gyozas, tempura, miso, arroceras, office) 1,00 × 1.400 · encargado/a de sala y pedidos (plataformas,
alérgenos, caja) 1,00 × 1.500 · camarero/a de cenas 0,75 × 1.350 · refuerzo de viernes a domingo (sala y empaquetado) 0,50 × 1.350 ·
suplencias 0,10 × 1.400 → **5,35 jornadas, 8.578 €/mes → 120.092 € brutos + 33 % = 159.722 €/año (33,7 %)**. **Cobertura**: servicio 6,5 h ×
3,5 personas + producción 3,0 h × 2,0 (arroz, corte y limpieza del pescado, salsas) = 28,75 h × 300 = 8.625 h frente a 5,35 × 40 × 46 = 9.844 →
**≈ 114 %**; ⚠️ el viernes y el sábado por la noche hacen falta 6 (dos en barra, uno en caliente, dos en sala, uno empaquetando): el cuadrante
anual no lo ve (= TAQ §7).

**Inversión** (18 filas, sin IVA; O obra, M maquinaria y mobiliario, N no amortizable) [criterio del plan salvo lo medido]:

| # | Partida | € | Tipo |
|---|---|---|---|
| 1 | Proyecto técnico de actividad y de extracción, y dirección de obra | 3.500 | O |
| 2 | Obra, rótulo y fachada (barra de sushi de obra a la vista, aseos, suelo, cuarto frío) | 28.000 | O |
| 3 | Conducto exclusivo de extracción hasta cubierta | 5.000 | O |
| 4 | Instalación eléctrica (cocina eléctrica), cuadro y boletín | 4.500 | O |
| 5 | Fontanería, separador de grasas y climatización | 7.500 | O |
| 6 | **Vitrina refrigerada de sushi (neta) para la barra** | 2.500 | M (999 € la de 6 GN 1/3 🟡; GJ 4.500-9.000 la premium) |
| 7 | Arroceras industriales (2), mantenedor y hangiri | 1.500 | M (483,50 € la de 8 l 🟡) |
| 8 | **Armario congelador de −20 °C con registrador (anisakis) y arcón** | 2.000 | M (GJ 3.000-5.500 la cámara; abatidor de −35 °C = variante) |
| 9 | Cocina caliente: inducción, freidora de tempura y plancha | 3.500 | M |
| 10 | Campana extractora con motor y filtros | 1.500 | M |
| 11 | Frío: armario de pescado (0-2 °C), armarios de cocina, mesa refrigerada y nevera de bebida y sake | 7.500 | M |
| 12 | Lavavajillas, fregaderos, lavamanos de accionamiento no manual, inox | 5.500 | M |
| 13 | Utillaje: cuchillos japoneses (yanagiba, deba), tablas por colores, sondas, básculas, **pH-metro**, etiquetadora (art. 5 RD 126/2015), vajilla | 3.500 | M |
| 14 | Mobiliario de sala y barra (36 plazas) | 9.000 | M |
| 15 | TPV con Veri\*factu, datáfono, impresora de comandas y tablets de plataformas | 2.500 | M |
| 16 | Constitución de la SL, licencia, tasas, registro sanitario y APPCC | 3.000 | N |
| 17 | Marca, web, fotos y lanzamiento | 4.500 | N |
| 18 | Stock inicial (pescado, arroz, algas, salsas, cajas de delivery, bebida) | 3.500 | N |
| | **Total** (O 48.500 · M 39.000 · N 11.000) + imprevistos del 10 % sobre la obra 4.850 | **103.350** | |

**Fijos** (9 filas, €/año) = **13.850**: gestoría 2.400 · mantenimiento (frío, congelador de −20 °C, campana, calibración del pH-metro) 1.800 ·
marketing (redes, fotos, Google, promociones de plataforma, **San Valentín y Nochevieja**) 4.000 · software, TPV, teléfono e internet 1.800 ·
limpieza, lavandería, EPI y análisis 1.500 · gestión de residuos y del aceite de tempura 600 · DDD 450 · SGAE y AGEDI-AIE 500 · PRL,
vigilancia de la salud y formación (manipulador de pescado crudo y alérgenos) 800.

**Cuenta a mano, a régimen** (F2 recalcula con rampa y estacionalidad):

| Concepto | € | % ventas |
|---|---|---|
| Ventas | 474.000 | 100 |
| Variables: mercancía 28,85 (0,85 × 29 + 0,15 × 28) + consumibles 3,0 + plataforma 7,5 + TPV 0,8 + varios 2 | | 42,2 |
| Contribución | 274.200 | 57,8 |
| Personal | 159.722 | 33,7 |
| Alquiler | 19.200 | 4,1 |
| Suministros + seguros + fijos | 28.850 | 6,1 |
| **EBITDA** | **≈ 66.400** | **14,0** |
| Amortización ≈ 9.240 · intereses ≈ 7.700 | | |
| **Neto** (IS 15 %) | **≈ 42.000** | **≈ 8,9** |

**Necesidad ≈ 182.000 €**: inversión 103.350 + fianza 3.200 + renta previa 3.200 + IVA soportado ≈ 20.400 + fondo de 3 meses ≈ 52.000 (fijos de
caja ≈ 17.300 €/mes) → 55.000 + ≈ 128.000. Cuota tras la carencia ≈ 26.000 €/año → **DSCR ≈ 2,5**. **Equilibrio de caja** (fijos de caja +
intereses ≈ 215.500 ÷ 0,578) ≈ 372.800 € = **62 comensales/día**, holgura ≈ **27 %**; contable ≈ 65, ≈ 22 %. **Honesto**: cada punto de food
cost ≈ 4.000 € de EBITDA; si el salmón sube un 20 % (≈ 35 % de la compra de comida), ≈ −8.200 €; pasar 10 puntos de plataforma a recogida
propia ahorra ≈ 14.000 € de comisión. **Palancas F2** (= TAQ §3): holgura A1 < 15 % → 65.000 € propios; DSCR < 1,25 → 8 años; neto > 12 % → 74
comensales; < 7 % → ticket 21,00 €.

**Estacionalidad** (Mes 1 = enero; suma 1,000) [criterio del plan; ❌ sin fuente de reparto mensual]: ene .082 · feb .086 (San Valentín) ·
mar .086 · abr .084 · may .086 · jun .084 · jul .080 · **ago .066** (cierre de 10 días y ciudad vacía) · sep .082 · oct .086 · nov .086 · **dic
.092** (bandejas de Nochebuena y Nochevieja). Pico/valle 1,39. **Variante costa** (Word): agosto sube. **Escenarios**: pesimista **68 · 19,00 ·
295** (≈ 381.000 €) · optimista **90 · 21,00 · 305** (≈ 576.000 €). **Umbrales**: `r_mb` **0,52** (caso 57,8 %) · `r_cogs` **0,31** · personal ≤
38 % · alquiler ≤ 10 % · neto ≥ 5 %.

**Referencias de Instrucciones** (cada una con fuente): maki, 2.º plato del delivery (Just Eat 🟡) · nigiri 2,50-2,60 € la pieza, combinado de
24 piezas 24,90-30,60 €, menú del día 13,95 € (§2) · salmón: lomo limpio 50-60 % del entero (🟡) · arroz para sushi 1,81-1,85 €/kg (Makro
🟡) · comisión de plataforma 30 % + IVA (✅ hermano) · IVA 10 % la comida, 21 % el alcohol y los refrescos azucarados para llevar, 4 % el arroz
en la compra (LIVA ✅) · anisakis −20 °C 24 h o −35 °C 15 h e información al consumidor (RD 1021/2022 art. 8 ✅ hermano) · shari: art. 30.5
del RD 1086/2020 (✅) · SMI 1.221 € (✅ hermano).

**Checklist de apertura: tareas que el research obliga a meter** (el resto, del molde): F1 · alta en el 671.x (677.9 si el para llevar
manda); consulta urbanística con extracción y aforo; decidir el formato (barra y mesas, para llevar, omakase) antes de firmar. F2 · licencia;
conducto y campana; cuarto frío y potencia eléctrica para cocina eléctrica. F3 · registro sanitario; **APPCC con PCC de anisakis** (registro
por lote, documento del proveedor, acuicultura acreditada por escrito, congelador que llegue a −20 °C en la totalidad), **cartel o carta con la
información del art. 8.2**, pescado a 0-4 °C y descongelación en cámara, **validación del shari** (pH por lote, tiempo máximo, comunicación a
sanidad, art. 30.5) o shari refrigerado, histamina en la recepción del atún, matriz de 14 alérgenos (con pescado, mostaza del wasabi y
trigo de la soja), etiqueta completa de las bandejas cerradas antes del pedido (art. 5 RD 126/2015). F4 · contratos y registro de jornada;
**itamae y sushiman contratados antes de la obra**; formación de manipulador de pescado crudo; cuadrante de viernes y sábado; PRL de cortes.
F5 · IVA 10/21 %; envase de plástico cobrado; plataformas con techo del 25 %; **dos proveedores de pescado** y uno de arroz con ficha técnica;
temporadas (bonito del norte jun-oct, atún rojo de almadraba abr-jun, KT DOM-09). F6 · medir rendimiento del salmón y gramos de shari y
llevarlos a la calculadora; revisión del frío y del congelador; calibración del pH-metro.

## 4. Demanda, SERP y canibalización

- **Volúmenes**: F0 §1-§2 (DataForSEO, 31-oct). Intención de montar ≈ 100/mes en España (con «franquicia sushi» 90) y ≈ 120 en México
  («negocio de sushi» 70); el consumidor busca muchísimo (sushi 301.000 ES, 368.000 MX; poke 74.000; sushi bar 8.100). El producto vive del
  catálogo y de la venta cruzada, como toda la familia.
- **SERP «montar restaurante de sushi»** (ES): F0 §1. Páginas de modelos con cifras sin fuente («50.000-160.000 €», «230.000-790.000 $»),
  franquicias, vídeos y Reddit mexicano. **Nadie cuenta el art. 30.5 del shari, ni el art. 8.2 del anisakis, ni el coste por pieza.**
- **Nombre y SEO de la landing**: H1 y `schema.productName` **«Plan de Negocio: Sushi Bar»** · `titleSubtitle` «Cómo montar un sushi bar o
  restaurante de sushi con barra, para llevar y a domicilio» · `seo.keywords`: plan de negocio sushi bar, cómo montar un sushi bar, montar
  restaurante de sushi, negocio de sushi, cuánto cuesta abrir un sushi bar, sushi a domicilio, sushiman, itamae, anisakis, AI Chef Pro.
- **Canibalización**: Guía Restaurante Japonés (lleva «abrir sushi bar» en sus keywords → **se quita** y enlaza al plan, como la Guía
  Mexicana con la Taquería); Guía Restaurante Nikkei (variante E, sin tocar sus keywords); Kit de Tareas Sushi Bar (complemento: el plan
  remite a sus hojas de pH, congelación y vitrina; enlace en los dos sentidos); Plan Food Truck (sushi en un remolque: fuera).

## 5. Jerga y equivalencias (glosario de los redactores y de la guía de equivalencias)

| España | Uso en el producto | LatAm / EN |
|---|---|---|
| **itamae** (jefe de barra), **sushiman / sushiwoman** | glosar la primera vez; «sushiman» es el término de México, Colombia y Argentina (F0) | US «sushi chef» (itamae = jerga de oficio) |
| **neta** (lo que va sobre el arroz) · **shari** (arroz avinagrado) · **sushi-zu** · **saku** (bloque limpio de pescado) · **hangiri** | glosados en el Word y la calculadora | = |
| nigiri, sashimi, **hosomaki** (fino), **uramaki** (arroz por fuera), temaki, futomaki, combinado | carta | US «roll», «inside-out roll», «hand roll» |
| vitrina de neta (o de sushi) | equipo | US «sushi case» |
| para llevar · a domicilio · plataforma | canales | AR «take away», CL «delivery» |
| pescado «apto para sushi» | **nunca «sashimi grade» como garantía**: no es categoría legal (US delta §6) | |
| omakase · kaiten · buffet libre | variantes | AR «sushi libre», CL «tenedor libre» |

**Guía de equivalencias**: términos ES que cambian en ≥ 5 de 21 países con fuente → solo si los hay (sushiman sí cambia de uso, pero no es
término de España): por defecto ejemplos en la FAQ, sin términos nuevos en `terminos.json` (tope 0,05 M, = POL).

## 6. Errores frecuentes, riesgos y FAQ de la landing

**Errores** (cada uno con su sitio en el Word y el checklist): (1) **Abrir sin itamae** o con uno solo: sin él no hay carta, y si falta, no
abre la barra. (2) **Citar el RD 1420/2006** o creer que el salmón «fresco» se puede servir sin papeles: el de acuicultura necesita el
documento; el salvaje y el atún, congelación. (3) **Congelador que marca −18 °C** usado para el anisakis (−20 °C en la totalidad, KT DOM-02).
(4) **Shari a temperatura ambiente sin validar** (art. 30.5) ni registro de pH. (5) **Plataforma sin techo**: 30 % + IVA + caja; el combinado
viaja bien, la tempura no. (6) Carta larga (60 platos) con merma de neta en vitrina. (7) **Precio del combinado sin escandallo por canal**: en
plataforma el margen cae a la mitad. (8) Un solo proveedor de pescado. (9) Alérgenos incompletos (pescado, mostaza del wasabi, trigo de la
soja y del surimi). (10) Bandejas cerradas en vitrina sin etiqueta del art. 5. (11) Cobrar al 10 % la cerveza para llevar. (12) Prometer «sin
gluten». (13) Copiar cifras de franquicia (180 m², 300.000 €) para un local de 95 m².

**FAQ de la landing** (de las PAA; cifras del Excel en la F3): 1. **¿Cuánto cuesta montar un sushi bar?** (≈ 103.000 € de inversión y ≈
182.000 € con el colchón; franquicias de 39.950 € a 300.000 €) · 2. **¿Es rentable un negocio de sushi?** (neto ≈ 9 % a régimen; equilibrio ≈
62 comensales/día) · 3. **¿Cuántos sushis salen con 1 kilo de arroz?** (≈ 120 nigiris por kilo de arroz crudo; la calculadora con tus
gramos) · 4. **¿Cuánto gana un sushiman?** (ofertas de 12.000-22.000 €/año; el caso, 1.650 €/mes en 14 pagas) · 5. **¿Qué dice la ley del
anisakis?** (RD 1021/2022 art. 8) · 6. **¿Puedo tener el arroz a temperatura ambiente?** (art. 30.5, APPCC validado) · 7. **¿Qué licencias
necesito?** · 8. **¿Me sirve en México, Argentina, Chile…?** (guía de equivalencias; el marco legal es el español) · 9. **¿Y una franquicia?**
(cifras de §2 frente al caso).

## 7. Sin verificar, preguntas abiertas y notas

- ❌ / 🟡: precio profesional de salmón fresco (Makro con JS, Mercamadrid sin publicar), saku de atún en España, ebi, langostino, surimi,
  masago, queso crema, aguacate y soja en garrafa; rendimiento del atún a saku; gramos de shari por uramaki (fuente US 80-90 g; el caso usa 120
  g, [criterio del plan]); peso de la neta; precio de robot de sushi, abatidor de −35 °C y mantenedor de arroz; número de restaurantes
  japoneses; ticket medio del delivery de sushi; omakase y kaiten con precio; Sushi Pop y Sushi Artist; reparto mensual de ventas.
  **Todo «estimación del kit, editable»** en Excel, calculadora, Word y landing; la calculadora pide medir neta y shari.
- **Para el motor (reportar, no arreglar)**: el comensal equivalente de plataforma (1,6 por pedido) va en la nota de `cubiertos_dia`; el
  arroz al 4 % solo afecta a `IVA_COMPRAS`.
- **Decisiones** (firmadas en `F1-camino.md` §2): nombre «Plan de Negocio: Sushi Bar» · slug `plan-negocio-sushi-bar` · unidad `comensal`
  con rotación encendida · caso B · coste de comida 29 % con su puente · Mes 1 = enero · **35 €** (= Pizzería, Taquería, Pollería: mismo
  formato y entregables; el Kit de Tareas de 14 € y la Guía de 65 € quedan a los lados).

## 8. Propuesta de la calculadora: «Pescado, Arroz y Escandallo por Pieza y Canal»

`calculadora-pescado-arroz-escandallo-sushi-bar.xlsx` (≤ 4 hojas: `Pescado` · `Arroz` · `Escandallo` · `Instrucciones`): rendimiento y coste
por gramo útil de salmón entero, lomo comprado y atún (merma de vitrina y recorte reaprovechado); shari por kilo de arroz crudo y piezas por kilo
(la PAA); coste por pieza y por rollo; margen por canal (sala, para llevar, plataforma con comisión, recargo y caja). Diseño en `F1-camino.md` §4.

## Fuentes

Leídas hoy: BOE-A-2020-15872 (RD 1086/2020, art. 30), BOE-A-2022-21681 (RD 1021/2022, art. 4.1), BOE-A-1992-28740 (LIVA, art. 91) ·
emprendedores.es (Sibuya, Miss Sushi, Sushimore) · conmenu.com (Sibuya León) · japonshop.com · DataForSEO (F0). Snippets 🟡: catalogos.makro.es y
tienda.makro.es (arroz, salmón), okidokiasianmarket.com, orientalmarket.es, finditapp.es, undercurrentnews.com, pulse.bot, dir.tridge.com,
hosteleria10.com (PDF), chefook.com, infojobs.net, es.jooble.org, theobjective.com (Just Eat), kantar.com, volteretarestaurante.com,
covermanager.com, elespanol.com, barcelonasecreta.com, directoalpaladar.com, justonecookbook.com, beancount.io, modelosdeplandenegocios.com,
ilfattoalimentare.it, aesan.gob.es (alerta wasabi 2020). Hermanos: POL, TAQ, PIZ, ANIS, KT, GJ (rutas en la cabecera).
