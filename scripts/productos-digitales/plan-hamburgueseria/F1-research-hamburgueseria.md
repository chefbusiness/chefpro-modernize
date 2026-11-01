# Plan de Negocio: Hamburguesería Smash (ES) · F1 research (caso, normativa, demanda, jerga, riesgos y calculadora)

> Sesión Claude Code, 31-oct-2026 (F1 nocturna, decisiones delegadas). Una pasada. **Reutiliza** lo que ya está leído y no lo repite:
> el mapa de palabras clave (`F0-mapa-keywords-es-en.md`, **F0 §n**); la normativa leída en origen por la Pollería, la Taquería y el Sushi Bar
> (`../plan-polleria/F1-research-polleria.md` **POL §n**, `../plan-taqueria/F1-research-taqueria.md` **TAQ §n**,
> `../plan-sushi/F1-research-sushi.md` **SUS §n**, y la Pizzería, **PIZ §n**: IAE, Ley 12/2012, RD 126/2015, RD 1021/2022 arts. 3-11 en general,
> RD 1086/2020 art. 30, LIVA 91 y la regla del 21 % de la bebida para llevar, Ley 7/2022, Ley 1/2025, convenio, SMI, Veri\*factu, plataformas,
> registro de jornada, OCAS 4/2021 de Madrid, RD 919/2006 del gas); y el oficio del **Kit de Tareas Hamburguesería** LIVE (12 €,
> `dl/kit-tareas-hamburgueseria/`, `kit-tareas-v2_0/contenido_kit_tareas_hamburgueseria.py`, ficha `tareas/kit-tareas-hamburgueseria.ts`, **KT**:
> plancha, smash, freidora, línea de montaje, delivery, 70 °C en el centro, aceite filtrado por debajo de 40 °C) y del post propio
> `blog/es/smash-burger-receta-pro-tecnica-restaurante.md` (**BLOG**: 20 % de grasa, plancha a 220-250 °C, 90 s + 60 s).
> Hoy, leído en origen: **RD 1021/2022 arts. 1-7** (API de datos abiertos del BOE, consolidado), **Rgto. (CE) 853/2004** anexo I 1.13 y 1.15,
> art. 1.5 y anexo III secc. V caps. I-III (compilación oficial de la Junta de Castilla y León; EUR-Lex no responde desde el Mac), **Rgto. (UE)
> 2017/2158** arts. 1-4, anexo II y anexo IV (DOUE L 304 de 21-11-2017, copia del BOE), **Orden de 26 de enero de 1989** de aceites y grasas
> calentados (BOE-A-1989-2265, consolidado), **LIVA art. 91.Dos.1.1.º** (versiones vigentes el 8-10-2026 y el 1-12-2026: iguales en lo que se
> cita), el informe **Inf26008 de Madrid Salud** (2-feb-2026) y la ficha de la **AESAN** sobre *E. coli* (18-abr-2022). Precios, cartas,
> cadenas, equipo y salarios: un lector sonnet (38 llamadas; Makro y los mayoristas no publican precio: solo hay minorista). Etiquetas:
> **[medido]** = leído hoy en la página del vendedor o el documento · **✅** = norma leída hoy en origen · **✅ hermano** = leída por otra F1
> (se dice cuál) · **🟡** = snippet, marketplace o secundaria · **[criterio del plan]** = estimación del kit con el cálculo a la vista · ❌ = no
> encontrado.

## 0. Los 9 hallazgos que mandan

1. **La hamburguesa es el plato nº 1 del delivery y el smash es su formato de moda, pero el mercado crece despacio y las cadenas pierden.**
   Hamburguesa, el plato más pedido a domicilio por tercer año (Gastrómetro Just Eat 2025, vía The Objective, 9-dic-2025 🟡); hamburgueserías,
   **3.730 M€ en 2025 (+5,2 %), el 61 % de la comida rápida, con las aperturas a +0,8 %** (DBK vía ecosistemastartup, 30-sep-2026 [medido]);
   **Goiko vendió 109 M€ en 2025 (−11,2 %) y perdió 36,4 M€** (Alimarket [medido]); Vicio nació con el **90 % de la venta a domicilio** (El
   Español, 2022 🟡). El caso reparte **sala ≈ 54 %, para llevar ≈ 13 %, plataforma ≈ 33 %** (§3): unidad **comensal equivalente** (1 pedido =
   1,7 comensales) con la **rotación encendida** (fast casual: pedido en el mostrador y estancias de 30-40 min), como la Taquería y el Sushi Bar.
2. **La carne picada SÍ tiene norma dentro del restaurante.** El RD 1021/2022 se aplica a la restauración: su art. 2.2.a ✅ incluye en el
   «comercio al por menor» los «establecimientos de restauración y hostelería». **Carne picada ≤ 2 °C; preparados de carne ≤ 4 °C** (art. 4.1
   ✅). **Si picas en el local**: «El picado de la carne se efectuará a petición y a la vista del comprador. No obstante, el picado podrá
   realizarse con carácter previo, con arreglo a las necesidades del despacho diario, **no pudiendo conservarse de un día para otro**» (art. 7.2
   ✅), y cumples los caps. II y III de la secc. V del anexo III del Rgto. 853/2004 (art. 7.3 ✅): solo músculo esquelético con su grasa, **sin
   recortes ni desperdicios** (salvo cortes de músculos enteros), carne a ≤ 7 °C al picar, **picada dentro de los 6 días siguientes al
   sacrificio (15 si es vacuno deshuesado y envasado al vacío)** y a ≤ 2 °C nada más picarla (853 anexo III secc. V cap. II.1 y III.1-2 ✅).
   **La bola sin sal es carne picada** («menos de 1 % de sal», 853 anexo I 1.13 ✅); salada o aliñada antes de la plancha pasa a **preparado de
   carne** (1.15 ✅, ≤ 4 °C): el smash se sala en la plancha. **Si la compras picada** a la carnicería del barrio, ese suministro entre minoristas
   tiene que ser marginal, localizado y restringido, con declaración responsable del carnicero (RD 1021/2022 art. 3 ✅).
3. **«Dry aged burger»: no.** Madrid Salud, Inf26008 (2-feb-2026) [medido], ante una hamburguesería que servía bolas de carne madurada de un
   obrador central: «no podría elaborarse carne picada con carne madurada con periodos de maduración superior a los quince días»; y la
   Comunidad de Madrid: «**El empleo de carne picada procedente de carne madurada no es una práctica permitida** de acuerdo a la normativa
   comunitaria». La tendencia que vende la SERP es un incumplimiento: el plan lo dice y la checklist lo prohíbe.
4. **«Poco hecha» no está prohibido ni tiene temperatura legal; es una recomendación y una decisión de tu APPCC.** El RD 1086/2020 art. 30
   fija el mantenimiento en caliente (≥ 63 °C), el frío, el enfriado y el recalentado (≥ 74 °C 15 s), **no una temperatura de cocinado** (✅
   hermano TAQ §1.b). La AESAN (18-abr-2022) [medido] **recomienda** «una temperatura mayor o igual a 70 ºC durante al menos 2 minutos» y dice
   que las «hamburguesas u otros alimentos elaborados con carne picada… deben cocinarse completamente»; si la etiqueta del proveedor pide
   cocinarla, «no deberá emplearse para su consumo crudo». No hay obligación de aviso en carta (❌ ninguna encontrada). El KT ya fija 70 °C en
   el centro con sonda (`contenido_kit_tareas_hamburgueseria.py:433`). **Ventaja del formato**: la bola aplastada de 100 g en plancha a 220-250
   °C sale hecha (BLOG 🟡): el riesgo es de la gourmet gruesa «al punto» (variante C).
5. **Freidora: dos normas que el producto puede afirmar.** Rgto. (UE) 2017/2158 ✅: el restaurante aplica el **anexo II, parte A** (art. 2.2):
   patata con poco azúcar (pregunta al proveedor), **almacenada a más de 6 °C**; la fresca, en remojo de 30 min a 2 h en agua fría (o unos minutos
   en caliente) y enjuagada, mejor escaldada; **la congelada, con las instrucciones del fabricante**; aceites que frían más rápido o más frío,
   «**las temperaturas al freír serán inferiores a 175 °C**», espumar a menudo y **guía de colores a la vista** del personal. El A.3 también
   alcanza al **pan tostado** de bocadillos y sándwiches (tostar «hasta el color óptimo», guía expuesta). Sin muestreo (art. 4.6), pero hay que
   «aportar pruebas de la aplicación» de las medidas; una **franquicia** con suministro central añade la parte B (freidoras calibradas con
   temporizador, seguimiento de acrilamida). Nivel de referencia: patatas fritas listas para consumir, **500 µg/kg** (anexo IV). Y la **Orden
   de 26-1-1989, vigente** (BOE-A-1989-2265 ✅; sus arts. 7, 8, 10-12 los derogó el RD 176/2013): «**El contenido en componentes polares será
   inferior al 25 por 100**» (art. 6.3) en bares, cocinas de comida para llevar y establecimientos turísticos (art. 3); prohibido añadir
   sustancias al baño o reutilizar el aceite usado en alimentos (art. 9). No obliga a un medidor: el APPCC elige tiras, medidor (Testo 270,
   399-499 € 🟡) o cambio por frecuencia.
6. **La carne es el 60 % del coste de la burger y la PAA tiene respuesta de calculadora.** «¿Cuántas hamburguesas salen por 1 kg de carne?»
   (PAA, F0 §1): **10 bolas de 100 g = 5 dobles** (11 de 90 g); si picas pieza en el local, menos la limpieza. Bola de 80-100 g en el mercado
   (Trafic 80 g 🟡, Bolus 90 g 🟡, «doble de 95 g» 🟡, **Smash Hiro 100 g** [medido]). Doble con queso ≈ **2,89 €** de coste sobre 10,82 €
   sin IVA = **27 %**; simple 22 %; patatas 8 % (§2). **Sin precio profesional de carne picada** ❌ (minorista: «burger meat» Eroski 8,03 €/kg en
   oferta 🟡) → el caso usa **8,90 €/kg** [criterio del plan] y la calculadora lo pide. Teórico ponderado ≈ 24 % → **el caso usa 28 %** (puente
   en §2).
7. **Patata congelada en el caso; la fresca es decisión de marca, no de coste.** La fresca cuesta ≈ 0,18 € de producto por ración frente a
   0,28 € de la congelada, pero pelar, cortar, remojar y escaldar suma ≈ 0,30 € de mano de obra [criterio del plan; mídelo] y la obliga a las
   medidas de remojo de la acrilamida. La calculadora compara las dos («la fresca te compensa si pelar y cortar cuesta menos de X € por kg»).
8. **Precio y tamaño del mercado** (con IVA): Smash Hiro (Málaga, Glovo) **burger 11,50 € con bola de 100 g, menús 13,90-21,90 €, patatas 4,00 €,
   lata 2,50 €** [medido]; Smash Hiro Barcelona smash 13 €, menú 15 € (Time Out [medido]); Goiko smash con patatas 13,90-17,40 € 🟡. **Franquicias**:
   **La Pepita 250.000 €, 140 m², canon 30.000 €, 4,5 % + 1,5 %** (emprendedores.es [medido]); TGB 290.000-300.000 €, 120 m², canon 35.000 €,
   royalty 7 % 🟡; Steak Burger 200.000 €, 180 m² 🟡; Five Guys canon 45.000 € 🟡. La SERP da «60.000-80.000 € para un local pequeño (30-50 m²)»
   (🟡). **Caso: 36 plazas en 90 m², 104.350 € de inversión** (§3).
9. **Alérgenos e IVA cambian con el producto.** Pan brioche y potato bun: gluten, huevo y leche (sésamo en el de semillas, soja en algunos);
   queso: leche; salsas: huevo y mostaza; encurtidos: mostaza y sulfitos según la marca; rebozados (crispy chicken, aros): gluten, huevo y leche;
   batidos: leche (y gluten o frutos de cáscara de los toppings). **Dos freidoras** (patatas aparte de los rebozados) o ninguna promesa de
   «patatas sin gluten». IVA de compras: **el pan de hamburguesa no es «pan común»** (91.Dos.1.1.º a ✅): 10 %; quesos, huevos, patata fresca y
   verdura al 4 % (d, e, f ✅); **el aceite de girasol al 10 %** (solo «los aceites de oliva» van al 4 %, letra g ✅) → **`IVA_COMPRAS` 0,090**. Para
   llevar y a domicilio, la cerveza y los refrescos «con azúcares **o edulcorantes** añadidos» al 21 % (✅ hermano POL §0.9): **también los zero**.

## 1. Marco legal y fiscal (lo que el producto afirma)

| Tema | Regla para el plan | Fuente · estado |
|---|---|---|
| IAE | Hamburguesería con sala: **671.x** (por categoría) o **673** si es barra y mostrador sin comedor; si el delivery es la actividad principal, **677.9** (variante dark kitchen) | ✅ hermano TAQ §1, POL §1 |
| Apertura | Licencia o declaración responsable (agrupación 67 fuera del anexo de la Ley 12/2012); **consulta urbanística previa: uso, extracción a cubierta, potencia, aforo** | ✅ hermano TAQ §1 |
| Humos | Estatal: la cocina de un restaurante no es actividad potencialmente contaminadora (RD 100/2011, anexo del RD 1042/2017) → **manda la ordenanza**. Ejemplo, **Madrid** (OCAS 4/2021): conducto exclusivo a cubierta, 1 m sobre los edificios en 15 m (art. 12 y anexo I), limpieza ≥ 1 vez al año (art. 23.1.e); solo exime lo eléctrico ≤ 4 kW sin olores (art. 24), que **no** es una plancha con dos freidoras. Otras ciudades: «pide la ordenanza de tu ayuntamiento», sin cifra | ✅ hermano PIZ §0.5 y §1 |
| Gas | Plancha de gas: instalación por empresa habilitada, certificado y puesta en marcha de cada aparato; inspección o revisión cada 5 años | RD 919/2006 ✅ hermano TAQ §1 |
| Registro sanitario | Declaración responsable → registro autonómico; vender bolas a otros bares, solo marginal (art. 3) | ✅ hermano POL §1 · RD 1021/2022 art. 3 ✅ (hoy) |
| **Carne picada** | Hallazgo 2: **≤ 2 °C**; preparados de carne ≤ 4 °C; si picas, del día y nunca de un día para otro, materia prima sin recortes, carne ≤ 7 °C al picar, dentro de 6 días del sacrificio (15 al vacío); bola sin sal = picada | RD 1021/2022 arts. 2.2.a, 4.1, 7.2-7.3 ✅ (hoy) · Rgto. 853/2004 anexo I 1.13 y 1.15, anexo III secc. V caps. II-III ✅ (hoy, compilación CyL) |
| Carne madurada | Hallazgo 3: no se pica carne madurada más de 15 días | Inf26008 Madrid Salud ✅ (hoy) · 853 anexo III secc. V cap. III.2.b |
| Congelar bolas propias | Envasadas y etiquetadas con fecha de elaboración, congelación y caducidad (art. 5.3); equipo que llegue a ≤ −18 °C en el centro «siguiendo un descenso ininterrumpido» (5.4), no en un arcón de mantenimiento que no lo garantice (5.5); registro (5.6); nunca recongelar (5.9); descongelar en frío (5.8). ⚠️ Con picada del local, **confírmalo con tu inspector** (el art. 7.2 no deja guardarla «de un día para otro»): el caso compra y no congela | RD 1021/2022 art. 5 ✅ (hoy) · lectura conjunta con el 7.2 [criterio del plan] |
| **Cocción** | Hallazgo 4: **sin temperatura legal**; PCC del APPCC con sonda (70 °C ≥ 2 min, recomendación AESAN); mantener ≥ 63 °C y recalentar ≥ 74 °C 15 s | RD 1086/2020 art. 30 ✅ hermano TAQ §1.b · AESAN ✅ (hoy) |
| **Acrilamida** | Hallazgo 5: anexo II parte A (patatas y pan tostado); franquicia, parte B | Rgto. (UE) 2017/2158 arts. 2 y 4, anexos II y IV ✅ (hoy, DOUE original; enmiendas posteriores sin comprobar 🟡) |
| **Aceite de fritura** | Componentes polares **< 25 %**; sin aditivos al baño; el aceite usado no vuelve a la cadena alimentaria (gestor autorizado: KT) | Orden de 26-1-1989 arts. 3, 6.3 y 9 ✅ (hoy) |
| Comidas preparadas | Frías ≤ 4 °C (vida > 24 h) u ≤ 8 °C (< 24 h); calientes ≥ 63 °C; enfriado 60 → 10 °C en < 2 h; recalentado ≥ 74 °C 15 s (salsas cocinadas, pulled, chili) | RD 1086/2020 art. 30 ✅ hermano TAQ §1.b |
| Vegetal cortado | Lechuga, tomate y cebolla cortados ≤ 4 °C (punto 10 de la tabla) | RD 1021/2022 art. 4.1 ✅ (hoy) |
| Etiquetado | Sin envasar o envasado a petición: denominación y alérgenos (art. 4); burgers ya envueltas antes del pedido (vitrina, «grab and go») = art. 5 | RD 126/2015 arts. 4-5 ✅ hermano POL §0.4 |
| Alérgenos | Hallazgo 9; información escrita o de palabra con registro escrito y accesible; **en la plataforma, en la ficha de cada plato antes de pagar** | RD 126/2015 arts. 4.1.b y 6.5.a ✅ hermano TAQ §1 · venta a distancia, Rgto. 1169/2011 art. 14 🟡 (no releído) |
| «Sin gluten» | ≤ 20 mg/kg: no prometerlo con pan de trigo, freidora compartida con rebozados ni plancha común (pan sin gluten aparte es opción, sin prometer) | Reg. Ej. (UE) 828/2014 ✅ hermano |
| IVA de ventas | Comida en sala, para llevar y a domicilio al 10 %; **cerveza y refrescos con azúcares o edulcorantes que salen del local al 21 %**; el batido de leche no es «bebida refrescante» → 10 % [criterio del plan, 🟡: confírmalo con tu gestoría]; el menú para llevar se desglosa por componentes (🟡) | LIVA 91.Uno.1.1.º a y b ✅ hermano POL §0.9 |
| IVA de compras | Carne, pan, salsas, bacon, patata congelada, aceite de girasol, helado y bebida al 10 % (≈ 84 % de la compra de comida); queso, huevos, patata fresca, verdura y leche al 4 % (≈ 16 %) → **0,090**, solo comida (lección de la Pizzería) | LIVA 91.Dos.1.1.º a, d, e, f y g ✅ (hoy) · pesos [criterio del plan] · la frontera del «pan común», RD 308/2019 🟡 (no releído: mira la factura del panadero) |
| Envases y desperdicio | Envase de plástico de un solo uso cobrado aparte (Ley 7/2022 art. 55); lo no consumido en sala se lo lleva el cliente sin coste (Ley 1/2025 art. 8) | ✅ hermano TAQ §1 |
| Convenio, SMI, jornada, Veri\*factu | Hostelería provincial (el ALEH VI art. 4 nombra literalmente las «hamburgueserías»); SMI 1.221 €/mes × 14; cargas 33 %; registro de jornada (sin «digital obligatorio»); TPV con Veri\*factu | ✅ hermano TAQ §1 · 🟡 |
| LatAm (solo guía de equivalencias) | El marco es español: el plan lo dice y remite a la gestoría local; carne molida, aceite y acrilamida tienen norma propia en cada país (no se cubre) | — |

**Citas literales leídas hoy (para el Word y el checklist)**

| Norma | Literal | Fuente |
|---|---|---|
| RD 1021/2022 art. 2.2.a | «…así como establecimientos de restauración y hostelería.» (dentro de la definición de «Establecimiento de comercio al por menor») | [BOE-A-2022-21681](https://www.boe.es/buscar/act.php?id=BOE-A-2022-21681) ✅ |
| Ídem, art. 4.1 (tabla) | «4. Preparados de carne. Igual o inferior a 4 °C. 5. Carne picada. Igual o inferior a 2 °C.» | ✅ |
| Ídem, art. 7.2 | «El picado de la carne se efectuará a petición y a la vista del comprador. No obstante, el picado podrá realizarse con carácter previo, con arreglo a las necesidades del despacho diario, no pudiendo conservarse de un día para otro.» | ✅ |
| Ídem, art. 7.3 | «Los establecimientos de comercio al por menor que elaboren carne picada y preparados de carne, lo harán de acuerdo con lo establecido en los capítulos II y III de la sección V del anexo III del Reglamento (CE) n.º 853/2004…» | ✅ |
| Rgto. 853/2004 anexo I 1.13 | «"Carne picada": la carne deshuesada que ha sido sometida a una operación de picado en trozos y que contiene menos de 1% de sal.» | compilación Junta de Castilla y León ✅ |
| Ídem, anexo III secc. V cap. III.2.b-c | «…cuando se trate de carne de vacuno deshuesada y envasada al vacío, dentro de los 15 días siguientes al sacrificio» · «…refrigerarse a una temperatura interna no superior a 2°C en el caso de la carne picada, y de 4°C en el caso de los preparados de carne» | ✅ |
| Rgto. (UE) 2017/2158 anexo II parte A.1 | «las temperaturas al freír serán inferiores a 175 °C y, en cualquier caso, lo más bajas posible, teniendo en cuenta los requisitos en materia de seguridad alimentaria» · «las patatas deberán almacenarse a una temperatura superior a 6 °C» | [DOUE L 304/24](https://www.boe.es/doue/2017/304/L00024-00044.pdf) ✅ |
| Orden de 26-1-1989, norma art. 6.3 | «El contenido en componentes polares será inferior al 25 por 100…» | [BOE-A-1989-2265](https://www.boe.es/buscar/act.php?id=BOE-A-1989-2265) ✅ |
| AESAN, *Toxiinfección por Escherichia coli* (18-4-2022) | «…el cocinado completo y homogéneo del alimento, a una temperatura mayor o igual a 70 ºC durante al menos 2 minutos, destruirá a la bacteria» | aesan.gob.es ✅ (recomendación, no norma) |
| LIVA 91.Dos.1.1.º a y g | «a) El pan común…» · «g) Los aceites de oliva.» | [BOE-A-1992-28740](https://www.boe.es/buscar/act.php?id=BOE-A-1992-28740) ✅ |

## 2. Benchmarks España

| Dato | Valor | Fuente |
|---|---|---|
| Mercado | Hamburgueserías 3.730 M€ en 2025, +5,2 %, 61 % de la comida rápida; aperturas +0,8 %. McDonald's, KFC, Domino's, Telepizza y Burger King suman ≈ 3.000 locales y ≈ 75 % del valor | DBK vía ecosistemastartup.com, 30-sep-2026 [medido] |
| Delivery | Hamburguesa, 1.º plato a domicilio por 3.er año (antes que maki y durum) · Vicio: 90 % de la venta a domicilio en 2020 · comida rápida: 16 % delivery (2019, antiguo) | Just Eat vía The Objective 🟡 · El Español 🟡 · okdiario 🟡 |
| Tendencia smash | Street Smash Burgers (Lisboa 2024, 35 locales) abre en Fuencarral 114, Madrid (fin de sep-2026) · Harlem Smash Burger (2023, 5 locales, busca franquiciados, inversión no comunicada) · Bemba Burger, 8-oct-2026: «no paran de abrir nuevos locales» · encuesta Uber Eats: 30 % prefiere smash (may-2024) | Alimarket [medido] · lexpress-franchise [medido] · SERP 🟡 · 🟡 sin URL |
| Precios de carta (con IVA) | **Smash Hiro Málaga**: burger 11,50 € (1 o 2 bolas de 100 g), carne y queso 10,50 €, resto 12,50-18,90 €, menús 13,90-21,90 €, patatas 4,00 €, lata 2,50 €, agua 2,00 € · **Smash Hiro Barcelona**: smash 13 €, menú 15 € · Smash Hiro (SERP): 10-14 €, postres 3,50-6,50 € · **Goiko**: smash con patatas 13,90-17,40 €, bebidas 2,40-3,90 €, menú 17,60-19,60 € · Trafic Burger (Murcia): smash de 80 g con cheddar 6,00 € · Smash Burger House (Barcelona): 14 € «algo caras» | Glovo [medido] · Time Out [medido] · SERP 🟡 · fastfoodsmenu y Just Eat 🟡 · Uber Eats 🟡 · TripAdvisor 🟡 |
| Ticket medio publicado | ❌ (ni Macarfi ni TheFork ni prensa) | — |
| Cadenas | **Goiko** 109 M€ (2025, −11,2 %), pérdidas 36,4 M€, ≈ 117 locales en 2024, Capza con el 98 % · **Vicio** ≈ 20 M€ en 2022, previsión > 40 M€ en 2023, Lisboa en dic-2025 · Five Guys 43-44 restaurantes · Burger King > 1.000 | Alimarket [medido] · Forbes [medido] · 🟡 · 🟡 |
| Franquicias | **La Pepita Burger Bar** 250.000 €, canon 30.000 €, 4,5 % + 1,5 %, ≥ 140 m², 5 propios + 18 franquiciados · TGB 290.000-300.000 €, canon 35.000 € + IVA, royalty 7 %, ≥ 120 m², > 70 locales · Steak Burger 200.000 €, canon 25.000 €, 5 % + 2 %, ≥ 180 m² · Five Guys canon 45.000 €, 5 % + 4 %, 20 años · Burger King ≈ 600.000 €, canon 60.000 € · La Birra Bar ≈ 500.000 €/local | emprendedores.es [medido] · lexpress-franchise y asest 🟡 · 🟡 · 🟡 · 🟡 · ecosistemastartup [medido] |
| Carne picada de vacuno | Minorista: «burger meat» Eroski 8,03 €/kg (en oferta) · profesional (Makro, Transgourmet, mayorista) ❌ → **caso 8,90 €/kg sin IVA**, blend de aguja, falda y pecho con ≈ 20 % de grasa (BLOG) [criterio del plan] | Eroski 🟡 |
| Pan, queso, patata, aceite | Brioche minorista 0,94 €/ud (2 × 1,88 €) → **caso 0,50 €** · potato bun ❌ · cheddar en lonchas minorista 8,75-23 €/kg → **caso 8,00 €/kg** · patata congelada minorista 1,76 €/kg (Eroski 2,5 kg), McCain 3,85 €/kg, lineal 2,10 €/kg (Circana, mar-2024) → **caso 1,50 €/kg** · patata fresca profesional ❌ → **0,60 €/kg** · girasol alto oleico minorista 2,25 €/l → **caso 1,80 €/l** en garrafa · bacon y salsas ❌ → 9,00 y 4,00 €/kg | finditapp 🟡 · Alimarket 🟡 · [criterio del plan] |
| Oficio | Bola de 80-100 g (Smash Hiro 100 g [medido]) · ≈ 20 % de grasa · plancha 220-250 °C · 90 s el primer lado y 60 s el segundo | BLOG 🟡 · KT |
| Equipo (sin IVA) | Plancha a gas de 80 cm 771 € (Francia, gama dudosa), 600 mm 1.399 € (tarifa), eléctrica de 80 cm 1.240,83 € · freidora eléctrica 2 × 8 l 268,45 € (gama ligera) · smasher de acero 34,99 € con IVA · medidor de polares Testo 270 399-499 € · campana 1,5-2 m 543-813 €, armario 400 l 899 €, mesa refrigerada 1.177-1.948 € · plancha de 100 cm, saladette de 1,5 m y tostador de cinta ❌ | hellopro, hosteleria10 (PDF) 🟡 · hitech2business 🟡 · Weber 🟡 · Infoagro 🟡 · ✅ hermano TAQ §2 |
| Salarios | Cocinero de cadena 22.000-25.000 €/año (Bilbao, Palencia) · cocinero 16-30 h de Hamburguesa Nostra 6.000-8.000 €/año · ayudante de hamburguesería gourmet 16.000-18.000 €/año (fijo discontinuo) · encargado y camarero ❌ | InfoJobs 🟡 |
| Alquiler | 12-20 €/m²/mes de media · los anuncios de Madrid con humos son traspasos (Malasaña 80.000 €; Sol 11.000 €/mes + 150.000 €): no sirven de referencia | ✅ hermano TAQ §2 · 🟡 |
| Plataformas | Glovo 15-35 % + IVA, Uber Eats 30 % + IVA, Just Eat 13-35 % | ✅ hermano 🟡 (PIZ §2, TAQ §2) |

**Escandallos del caso** (sin IVA; bola de 100 g a 8,90 €/kg + 3 % de merma de bolas al cierre; pan 0,50 €; 2 lonchas de 20 g de queso
por bola; salsa, encurtido, cebolla, mantequilla del pan y papel ≈ 0,20 € + 0,02 € por bola; patata congelada 150 g a 1,50 €/kg + aceite) [criterio del plan]:

| Producto | Coste | PVP sin IVA (con IVA) | Coste % |
|---|---|---|---|
| Smash simple con queso (1 × 100 g) | 1,80 € | 8,09 € (8,90 €) | **22 %** |
| Smash doble con queso (2 × 100 g) | 2,89 € | 10,82 € (11,90 €) | **27 %** |
| Doble con bacon (+ 30 g) | 3,16 € | 11,73 € (12,90 €) | 27 % |
| Triple (3 × 100 g) | 3,99 € | 13,18 € (14,50 €) | 30 % |
| Patatas congeladas (150 g) | 0,28 € | 3,55 € (3,90 €) | **8 %** |
| Patatas frescas cortadas en casa (200 g brutos, 75 % útil) | 0,18 € + ≈ 0,30 € de mano de obra | 3,55 € (3,90 €) | 5 % (14 % con la mano de obra) |
| Patatas con queso y bacon | 0,92 € | 5,91 € (6,50 €) | 16 % |
| Menú doble + patatas + refresco (15,90 €): parte de comida | 3,17 € | 12,28 € | 26 % |
| El mismo menú en plataforma (18,30 €, +15 %) | 3,17 € + bebida 0,45 + cajas y bolsa 0,60 | 16,64 € | margen tras el 30 % ≈ **7,40 €** (sala ≈ 10,80 €; para llevar ≈ 10,40 €) |
| **Teórico ponderado de la comida** (burgers ≈ 70 %, patatas ≈ 20 %, postres y otros ≈ 10 %, con el descuento del menú) | | | **≈ 23-24 %** |

**Del 24 % teórico al 28 % del caso** (puente que el Word explica y la calculadora deja medir): bolas, pan y salsas tirados al cierre +1,5 ·
comidas del personal, invitaciones, errores y reclamaciones de plataforma +1,5 · promociones de plataforma (2 × 1, primera compra) +1 =
**≈ 28 %**. Cada 1 €/kg que sube la carne pone ≈ 0,21 € en la doble (≈ 2 puntos de food cost).

## 3. Caso España 2.2 (comensales equivalentes × ticket × días; motor de planes)

**Semilla**: la rejilla de la **Taquería LIVE** con la rotación encendida, confirmada: la sala rota (pedido en el mostrador, estancias de
30-40 min) y la unidad es el comensal con equivalentes de llevar y domicilio. **Propuesta**: partir del **Sushi Bar LIVE**
(`dl/plan-negocio-sushi-bar/`), que es esa misma rejilla (semilla Taquería) ya con Mes 1 = enero, pagas 7/12, la línea partida de bebida con
`pct`, `IVA_COMPRAS` de solo comida y `VOCABULARIO_SIN_TILDES`: menos que reescribir. La Pollería no sirve (rotación apagada, unidad
«pedido»). Que el arquitecto lo decida con el dry-run de control (= SUS-camino §1).

**Variantes** [criterio del plan]:

| Variante | Local | Plazas | Mezcla | Lectura |
|---|---|---|---|---|
| A · Smash solo a domicilio (dark kitchen) | 40-60 m² | 0 | 100 % fuera | El origen de Vicio (90 % delivery); 677.9; remite a la **Guía Dark Kitchen**. Solo en el Word |
| **B · Hamburguesería smash fast casual con sala, para llevar y plataforma (ELEGIDA)** | **90 m²** | **36** (6 en barra de ventana) | **sala ≈ 54 %, para llevar ≈ 13 %, plataforma ≈ 33 %** | Pedido en el mostrador, sin servicio de mesa, carta corta |
| C · Hamburguesería gourmet con servicio de mesa (bola de 180 g al punto, cervezas) | 120-150 m² | 60-80 | sala | Ticket 25-30 €, el tamaño de La Pepita y TGB; el riesgo del «poco hecho» (hallazgo 4). Word |
| D · Carrito, puesto o food truck de smash | — | — | calle y eventos | Remite al **Plan Food Truck** (y a la búsqueda mexicana de «carrito», F0 §1) |
| E · Franquicia (La Pepita, TGB, Five Guys) | 120-180 m² | | | Cifras de §2 frente a la marca propia. Word y FAQ |

**Local tipo (B)**: barrio con vida de noche o zona universitaria en una ciudad de 150.000-500.000 habitantes (o un barrio de Madrid,
Barcelona, Valencia); **90 m² ya de restauración con salida de humos a cubierta posible** (el filtro del local), sin traspaso; **cocina a la
vista** con plancha (fry-top) de acero a gas de 100 cm, tostador de pan, **dos freidoras** (patatas aparte de los rebozados), línea de montaje
refrigerada con cajones para las bolas; **mostrador de pedidos con pantalla de turnos** (un runner lleva la bandeja); sala de 30 plazas + 6 en
barra de ventana; zona de empaquetado y recogida de riders junto a la puerta. **Carta corta** (≈ 14 referencias): 6 smash (simple, doble,
triple, bacon, «oklahoma» con cebolla, la de la casa), crispy chicken, vegetal; patatas clásicas y cargadas; tres salsas; tres batidos,
refrescos, cerveza de tirador, agua; dos postres. **Menú** doble + patatas + bebida 15,90 €. **Horario**: martes a domingo 13:00-16:30 y
20:00-24:00 (viernes y sábado hasta las 00:30), plataforma en los dos servicios; cierra los lunes y 10 días en la segunda quincena de enero.

**Derivación** (media del año; 1 pedido para llevar o de plataforma = **1,7 comensales equivalentes**) [criterio del plan]:

| Día | Sala (comensales) | Para llevar (pedidos) | Plataforma (pedidos) | Comensales equivalentes |
|---|---|---|---|---|
| Martes y miércoles (× 2) | 34 | 5 | 11 | 61 |
| Jueves | 42 | 6 | 13 | 74 |
| Viernes | 66 | 9 | 22 | 119 |
| Sábado | 80 | 10 | 24 | 138 |
| Domingo | 60 | 10 | 22 | 114 |
| **Semana (6 días)** | 316 → **52,7/día** (1,46 por plaza) | 45 → 7,5/día | 103 → 17,2/día | **568 → ≈ 95/día** (2,6 por plaza con todo) |

**Ticket** (con IVA → sin IVA): comensal de sala (burger 11,40 € + patatas 2,90 € + bebida 3,00 € + extra 0,90 € − descuento del menú 1,20 €) =
17,00 € → **15,45 €** · pedido para llevar (≈ 2 menús, no siempre completos) 28,00 € → 25,45 € → **14,97 € por comensal equivalente** · pedido de
plataforma (precio +15 %) 32,20 € → 29,27 € → **17,22 €**. Venta diaria (52,7 × 15,45 + 7,5 × 25,45 + 17,2 × 29,27) ≈ 1.507 € ÷ 94,6 = 15,93 € →
el caso usa **16,00 €**. Reparto: **sala 54 %, para llevar 13 %, plataforma 33 %**.

| Clave del motor | Rótulo hamburguesería | Valor | Fuente |
|---|---|---|---|
| `cubiertos_dia` | Comensales al día (sala + equivalentes de llevar y domicilio: 1 pedido = 1,7) | **95** (sábado 138; martes 61) | tabla |
| `ticket_medio` · `dias_apertura` | € por comensal sin IVA · días | **16,00 €** · **300** (365 − 52 lunes − 10 de enero − 3 sueltos) | arriba |
| Ventas a régimen | | **95 × 16,00 × 300 = 456.000 €** · sala ≈ 246.000 · llevar ≈ 58.000 · plataforma ≈ 152.000 | |
| `crec_a2` / `crec_a3` | | 6 % / 4 % | = Taquería y Sushi Bar |
| Líneas (2) | Comida (burgers, patatas, postres) / Bebida (refrescos, cerveza, batidos, agua) | **84 % / 16 %** (sala ≈ 19 % de bebida; fuera ≈ 12 %) | [criterio del plan] |
| Bebida que sale del local al 21 % | Línea partida del motor (sexto campo): refrescos con azúcares o edulcorantes y cerveza, fuera del local | ≈ 4,5 % de las ventas → **`pct` 0,28** de la bebida | LIVA ✅ hermano |
| `coste_comida` · `coste_bebida` | | **28 %** (puente de §2) · **25 %** (lata ≈ 19 %, tercio ≈ 22 %, batido ≈ 18 %, con el descuento del menú) | §2 |
| `pct_consumibles` | Cajas de burger, cucuruchos de patatas, tarrinas de salsa, bolsas, precinto, papel, servilletas, guantes | **3,0 %** (≈ 1,10 € por pedido y 0,20 € por comensal de sala) | [criterio del plan] |
| `pct_delivery` / comisión | | **0,33 / 0,30** (9,9 % de las ventas) | §2 ✅ hermano |
| TPV · varios | | 0,8 % · 2 % | molde |
| `alquiler_mes` · fianza · renta previa | | **1.500 €** (90 m² × ≈ 16,7 €/m²; 3,9 %) · 2 · 2 | [criterio del plan] |
| `suministros_mes` · `seguros_ano` | Gas de la plancha, freidoras eléctricas, extracción potente, frío, clima | **1.150 €** · **1.500 €** | [criterio del plan] |
| Financiación | | propios **55.000 €** + préstamo **≈ 127.000 € (CALIBRAR en F2)** · 6 %, 7 años, 1 de carencia · fondo 3 meses · vidas 10/10 | = Sushi Bar |
| `aforo` · `ROTACION` | | **36** · techo **3,5** (comida, cena y estancias de 30-40 min); referencia: incluye los pedidos; la de tu sala ronda 1,5 | [criterio del plan] |
| Rampa · cobro/pago · pagas | | 0,75 en 4 · 2 / 30 · 7 y 12 | = familia |
| `IVA_COMPRAS` · Mes 1 | | **0,090** · **enero** | §1 · = familia |

**Plantilla** (7 filas; 14 pagas; todos ≥ SMI a prorrata) [criterio del plan]: titular — gerente y **jefe/a de plancha** (compra de la carne,
blend y proveedores, carta, APPCC, plataformas) 1,00 × **2.000** · cocinero/a de plancha (smash, tiempos y punto) 1,00 × **1.500** · cocinero/a
de montaje y freidora (línea, patatas, salsas, bolas, mise en place) 1,00 × 1.400 · encargado/a de mostrador y pedidos (caja, pantalla,
plataformas, empaquetado, alérgenos) 1,00 × 1.450 · auxiliar de sala y empaquetado (runner, recogida, friegue) 0,75 × 1.350 · refuerzo de
viernes a domingo (segunda plancha o empaquetado) 0,50 × 1.350 · suplencias 0,10 × 1.400 → **5,35 jornadas, 8.178 €/mes → 114.485 € brutos + 33 % =
152.265 €/año (33,4 %)**. **Cobertura**: servicio 7,5 h × 3,5 personas + producción 2,5 h × 1,5 (bolas, salsas, cortar verdura, reponer) =
30,0 h × 300 = 9.000 h frente a 5,35 × 40 × 46 = 9.844 → **≈ 109 %**; ⚠️ el viernes y el sábado por la noche hacen falta 6 (dos en plancha,
uno en montaje y freidora, uno en mostrador, uno empaquetando y un runner): el cuadrante anual no lo ve (= TAQ §7).

**Inversión** (18 filas, sin IVA; O obra, M maquinaria y mobiliario, N no amortizable) [criterio del plan salvo lo medido]:

| # | Partida | € | Tipo |
|---|---|---|---|
| 1 | Proyecto técnico de actividad y de extracción, y dirección de obra | 3.500 | O |
| 2 | Obra, rótulo y fachada (mostrador de pedidos, cocina a la vista, aseos —uno adaptado—, suelo antideslizante) | 26.000 | O |
| 3 | Conducto exclusivo de extracción hasta cubierta (plancha y freidoras: mucha grasa) | 6.000 | O |
| 4 | Instalación eléctrica (freidoras trifásicas), cuadro y boletín | 4.500 | O |
| 5 | Fontanería, separador de grasas, climatización e instalación de gas por empresa habilitada | 8.500 | O |
| 6 | **Plancha (fry-top) de acero a gas de 100 cm y tostador de pan** | 4.000 | M (80 cm 771-1.399 € 🟡; 100 cm ❌) |
| 7 | **Dos freidoras eléctricas de 2 × 10 l** (patatas aparte de los rebozados) y mantenedor de patatas | 3.500 | M (2 × 8 l de gama ligera 268,45 € 🟡) |
| 8 | Campana extractora de 3 m con motor y filtros | 2.200 | M (1,5-2 m 543-813 € ✅ hermano) |
| 9 | Mesa refrigerada de preparación (línea de montaje) y bajo plancha refrigerado para las bolas | 3.800 | M (1.177-1.948 € la mesa ✅ hermano) |
| 10 | Frío: armario de carne (≤ 2 °C), armarios de cocina, congelador de patatas y nevera de bebidas | 5.000 | M |
| 11 | Barra: batidora de batidos, arcón de helado, tirador de cerveza (si no lo cede la cervecera) y botellero | 2.500 | M |
| 12 | Lavavajillas, fregaderos, lavamanos de accionamiento no manual, inox | 5.500 | M |
| 13 | Utillaje: smashers, espátulas y raspadores, básculas de porcionado, sondas, **medidor de compuestos polares**, GN, dispensadores de salsa, etiquetadora | 2.000 | M (smasher 34,99 € 🟡, Testo 270 399-499 € 🟡) |
| 14 | Mobiliario de sala y barra (36 plazas) y mostrador | 8.000 | M |
| 15 | TPV con Veri\*factu, pantalla de turnos, datáfono, impresora de comandas e integrador de plataformas | 3.500 | M |
| 16 | Constitución de la SL, licencia, tasas, registro sanitario y APPCC | 3.000 | N |
| 17 | Marca, web, fotos y vídeo de lanzamiento (el smash se vende en vídeo) | 5.000 | N |
| 18 | Stock inicial (carne, pan, patatas, aceite, salsas, envases de delivery, bebida) | 3.000 | N |
| | **Total** (O 48.500 · M 40.000 · N 11.000) + imprevistos del 10 % sobre la obra 4.850 | **104.350** | |

**Fijos** (9 filas, €/año) = **14.400**: gestoría 2.400 · mantenimiento (**limpieza de campana y conducto ≥ 1 vez al año**, plancha y gas,
freidoras, frío) 2.000 · marketing (redes con vídeo, fotos, Google, promociones de plataforma, **Día de la Hamburguesa** del 28 de mayo 🟡) 4.500 ·
software, TPV, integrador de plataformas, teléfono e internet 1.800 · limpieza, lavandería, EPI y análisis 1.500 · gestión de residuos y del
**aceite usado por gestor autorizado** 600 · DDD 450 · SGAE y AGEDI-AIE 500 · PRL, vigilancia de la salud y formación (manipulador, alérgenos,
quemaduras) 650.

**Cuenta a mano, a régimen** (F2 recalcula con rampa y estacionalidad):

| Concepto | € | % ventas |
|---|---|---|
| Ventas | 456.000 | 100 |
| Variables: mercancía 27,52 (0,84 × 28 + 0,16 × 25) + consumibles 3,0 + plataforma 9,9 + TPV 0,8 + varios 2 | | 43,2 |
| Contribución | 258.900 | 56,8 |
| Personal | 152.265 | 33,4 |
| Alquiler | 18.000 | 3,9 |
| Suministros + seguros + fijos (13.800 + 1.500 + 14.400) | 29.700 | 6,5 |
| **EBITDA** | **≈ 58.950** | **12,9** |
| Amortización (5.335 + 4.000) ≈ 9.335 · intereses ≈ 7.620 | | |
| BAI | ≈ 42.000 | 9,2 |
| **Neto** (IS 15 %) | **≈ 35.700** | **≈ 7,8** |

**Necesidad ≈ 182.000 €**: inversión 104.350 + fianza 3.000 + renta previa 3.000 + IVA soportado ≈ 21.600 + fondo de 3 meses ≈ 50.000 (fijos de
caja ≈ 16.660 €/mes) → 55.000 + ≈ 127.000. Cuota tras la carencia ≈ 25.800 €/año → **DSCR ≈ 2,0**. **Equilibrio de caja** (fijos de caja +
intereses ≈ 207.600 ÷ 0,568) ≈ 365.600 € = **76 comensales/día**, holgura ≈ **20 %**; contable ≈ 79,6, ≈ 16 %. El neto del año 3 sube con el
6 % y el 4 % de crecimiento (la F2 lo mide). **Honesto**: cada punto de food cost ≈ 3.800 € de EBITDA; si la carne sube un 20 % (≈ 55 % de la
compra de comida), ≈ −11.800 €; pasar 10 puntos de plataforma a recogida propia ahorra ≈ 13.700 € de comisión; un local que se vaya al 45 % de
plataforma (el modelo Vicio) pierde ≈ 16.400 € más. **Palancas F2** (= SUS §3): holgura A1 < 15 % → 65.000 € propios; DSCR < 1,25 → 8 años;
neto del año 3 > 12 % → 90 comensales; < 7 % → ticket 16,50 €.

**Estacionalidad** (Mes 1 = enero; suma 1,000) [criterio del plan; ❌ sin fuente de reparto mensual]: **ene .072** (cierre de 10 días y cuesta
de enero) · feb .080 · mar .085 · abr .086 · **may .089** (buen tiempo, fin de curso, Día de la Hamburguesa) · jun .088 · jul .086 · **ago .076**
(ciudad vacía y calor: cae el delivery) · sep .085 · oct .087 (vuelta, fútbol, Halloween) · nov .082 · dic .084. Pico/valle 1,24. **Variante
costa** (Word): julio y agosto suben. **Escenarios**: pesimista **80 · 15,25 · 295** (≈ 359.900 €, en el equilibrio de caja: EBITDA ≈ 4.400 €) ·
optimista **110 · 16,75 · 305** (≈ 562.000 €). **Umbrales**: `r_mb` **0,52** (caso 56,8 %) · `r_cogs` **0,30** · personal ≤ 38 % · alquiler ≤ 10 %
· neto ≥ 5 %. Rotación: caso 2,64, equilibrio ≈ 2,1, techo 3,5.

**Referencias de Instrucciones** (cada una con fuente): hamburguesa, 1.º plato del delivery (Just Eat 🟡) · smash 11,50-13 € y menú 13,90-15 €
(Smash Hiro [medido]) · bola de 80-100 g (§2) · 10 bolas de 100 g por kilo (cálculo de la calculadora) · comisión de plataforma 30 % + IVA (✅
hermano) · IVA 10 % la comida, 21 % el alcohol y los refrescos con azúcares o edulcorantes para llevar, 4 % el queso, el huevo y la patata fresca
en la compra (LIVA ✅) · carne picada ≤ 2 °C y, si la picas, del día (RD 1021/2022 arts. 4.1 y 7.2 ✅) · freír por debajo de 175 °C (Rgto.
2017/2158 ✅) · polares < 25 % (Orden de 1989 ✅) · SMI 1.221 € (✅ hermano).

**Checklist de apertura: tareas que el research obliga a meter** (el resto, del molde): F1 · alta en el 671.x o 673 (677.9 si manda el
delivery); consulta urbanística con extracción a cubierta, potencia y aforo; **decidir antes de firmar: carne comprada picada o picada en el
local** (arts. 3 y 7 del RD 1021/2022) y **patata congelada o fresca** (dimensiona cocina, plantilla y acrilamida). F2 · licencia; conducto
exclusivo y campana (plancha + freidoras); gas por empresa habilitada (RD 919/2006) o potencia para una plancha eléctrica; separador de grasas.
F3 · registro sanitario; APPCC con **carne picada ≤ 2 °C** (bola sin sal; salada antes, preparado ≤ 4 °C), si picas: del día y nunca de un día
para otro, músculo sin recortes, ≤ 6 días del sacrificio (15 al vacío) y **nada de carne madurada**; **PCC de cocción con sonda** (70 °C, criterio
AESAN, sin prometer «al punto»); utensilios de crudo separados; congelación de bolas solo con equipo de −18 °C ininterrumpido, envasadas,
etiquetadas y consultado el inspector; **acrilamida** (patata a más de 6 °C, remojo o escaldado si es fresca, < 175 °C, guía de colores de patatas
y pan a la vista); **aceite** (polares < 25 % con tiras o medidor, registro de cambios, gestor autorizado); matriz de 14 alérgenos (pan: gluten
y sésamo; salsas: huevo y mostaza; queso; sulfitos de encurtidos; rebozados) y la misma ficha en cada plataforma; «sin gluten» no prometido.
F4 · contratos y registro de jornada; manipulador; PRL de quemaduras de plancha y freidora; cuadrante de viernes y sábado. F5 · IVA 10/21 % (los
refrescos zero también al 21 % para llevar); envase de plástico cobrado; plataformas con techo del 35 %; **dos proveedores de carne** con ficha
técnica (blend, % de grasa, fecha de sacrificio o envasado) y uno de pan; precio del menú por canal. F6 · pesar 10 bolas, medir la merma de
cocción y las raciones de patata por kilo y llevarlo a la calculadora; polares y cambios de aceite; limpieza de campana y conducto; calibrar
la sonda.

## 4. Demanda, SERP y canibalización

- **Volúmenes**: F0 §1-§2 (DataForSEO, 31-oct). Intención de montar ≈ 420/mes en España (con «franquicia hamburguesería» 210) y ≈ 600 en México
  («negocio de hamburguesas» 320); el consumidor busca muchísimo (smash burger 49.500 ES, 18.100 MX; hamburguesería 22.200 ES, 9.900 AR). El
  producto vive del catálogo y de la venta cruzada, como toda la familia.
- **SERP «como montar una hamburgueseria»** (ES): F0 §1. Páginas de software y de modelos con cifras sin fuente («en torno a 80.000 €»,
  «60.000-80.000 € para 30-50 m²»), Reddit argentino, grupo de Facebook y un curso mexicano. **Nadie cuenta el art. 7 del RD 1021/2022, la carne
  madurada, la acrilamida a 175 °C ni el coste por bola y por canal.** «Hamburguesería smash» es SERP local de cartas y reseñas.
- **Nombre y SEO de la landing**: H1 y `schema.productName` **«Plan de Negocio: Hamburguesería Smash»** (= tarjeta del hub) · slug
  **`plan-negocio-hamburgueseria`** (F0 §3) · `titleSubtitle` «Cómo montar una hamburguesería de smash burgers con sala, para llevar y a
  domicilio» · `seo.keywords`: plan de negocio hamburguesería, cómo montar una hamburguesería, montar una hamburguesería smash, cuánto cuesta
  montar una hamburguesería, negocio de hamburguesas, hamburguesería smash, smash burger, hamburguesas a domicilio, carne para smash burger,
  AI Chef Pro. «Franquicia» solo en la FAQ (no es un plan de franquicia).
- **Canibalización** (medido con `git grep`; **ninguna ficha lleva keywords de montar una hamburguesería: no hay que quitar nada**):
  **Kit de Tareas Hamburguesería** (12 €; complemento operativo: el plan remite a sus hojas de plancha, freidora y montaje; `footerLinks` +1 en
  `tareas/kit-tareas-hamburgueseria.ts:399`); use case `hamburgueseria` de `src/data/use-cases-content.es.ts:2436` (`productIds` en la l. 2474:
  +`plan-negocio-hamburgueseria`; comprobar la tarjeta en el `dist` de `/usos/`); **Guía Dark Kitchen** (variante A; keywords sin roce; enlace
  opcional); **Kit de Escandallos** (su plantilla de food truck y su test de rendimiento usan una smash: complemento, no se toca); **Guía
  Restaurante Casual** (casual dining sin hamburguesa en keywords: sin roce); **Plan Food Truck** (variante D). La **tarjeta «Próximos»** de
  `ProductosDigitalesHubPage.astro:1152` se quita al publicar. EN: el gemelo operativo `burger-joint-checklist-templates` ya existe.

## 5. Jerga y equivalencias (glosario de los redactores y de la guía de equivalencias)

| España | Uso en el producto | LatAm / EN |
|---|---|---|
| **smash** (bola aplastada en la plancha), **bola** (la porción cruda), **smasher** (la prensa), **costra** | glosar la primera vez | igual; AR y UY «medallón» para la carne de la hamburguesa; EN «patty», «puck» |
| **plancha** · **fry-top** (plancha de acero de cocina profesional) | equipo | MX también «comal» o «plancha»; EN «flat-top», «griddle» |
| **carne picada** · **blend** (mezcla de cortes) | materia prima | **carne molida** (MX, CO, PE, CL); AR «carne picada»; EN «ground beef», «chuck blend» |
| **pan brioche** · **pan de patata** (potato bun) | pan | **pan de papa** (AR 12.100, CL 5.400 búsquedas) |
| **patatas fritas** | guarnición | **papas fritas**; MX **«papas a la francesa»** (33.100); EN «fries» |
| **batido** | bebida | **malteada** (MX, CO, PE); «milkshake» (CL, AR); EN «shake» |
| **bacon** · **queso americano** o cheddar · **pepinillo** · **kétchup** | ingredientes | tocino (MX), tocineta (CO), panceta (AR) · «queso amarillo» (MX) · pickles (AR) · cátsup (MX) |
| **refresco** | bebida | gaseosa (AR, CO, PE), bebida (CL) |
| para llevar · a domicilio · plataforma | canales | AR «take away»; AR, CL y PE «delivery»; CO **«domicilios»** |
| línea de montaje · runner · rider | operativa | = |

**Guía de equivalencias**: `terminos.json` ya tiene «patata» (papa), «carne picada», «panceta, bacon», «refrescos», «para llevar», «a
domicilio» y «plancha» (comprobado). **Falta «batido»** (solo está «batidora»), que cambia en ≥ 5 de 21 países (malteada en MX y buena parte de
Centroamérica, CO, EC, PE; milkshake en CL y AR; volúmenes de F0 §1 como apoyo) → **proponer 1 término nuevo** (`batido`, patrón
`\bbatidos?\b` para no cazar «batidora» ni «abatidor»), si el tope de 0,05 M (= POL) lo admite; si no, ejemplo en la FAQ.

## 6. Errores frecuentes, riesgos y FAQ de la landing

**Errores** (cada uno con su sitio en el Word y el checklist): (1) **Picar hoy para mañana** o guardar la picada del local de un día para otro
(art. 7.2). (2) **«Dry aged burger»** con carne madurada más de 15 días (Inf26008). (3) Bolas saladas en la cámara a 4 °C creyendo que son
picada (son preparado; y la picada va a ≤ 2 °C). (4) **Prometer el «al punto»** sin sonda ni APPCC, o servir poco hecha una carne cuyo
proveedor pide cocinarla. (5) **Freír a 180-190 °C** y cambiar el aceite «cuando huele» (< 175 °C y polares < 25 %). (6) Una sola freidora para
patatas y rebozados y luego «patatas sin gluten». (7) **Plataforma sin techo**: 30 % + IVA + cajas; la burger viaja bien, las patatas no
(cucurucho ventilado, freír al último). (8) **Precio del menú sin escandallo por canal**: en plataforma el margen cae ≈ 30 % (§2). (9) Carta
larga (12 burgers, 6 salsas) con merma de pan y toppings. (10) Un solo proveedor de carne y sin ficha técnica del blend. (11) Cobrar al 10 % la
cerveza o el refresco zero para llevar. (12) Copiar la inversión de una franquicia de 140-180 m² para un local de 90 m². (13) Abrir sin cuadrante
de viernes y sábado: la plancha es el cuello de botella.

**FAQ de la landing** (de las PAA; cifras del Excel en la F3): 1. **¿Cuánto cuesta montar una hamburguesería?** (≈ 104.000 € de inversión y
≈ 182.000 € con el colchón; franquicias de 200.000 a 300.000 €) · 2. **¿Es rentable el negocio de hamburguesas?** (neto ≈ 8 % a régimen;
equilibrio ≈ 76 comensales/día; el tamaño no garantiza nada: Goiko perdió 36 M€ en 2025) · 3. **¿Cuántas hamburguesas salen por 1 kg de
carne?** (10 bolas de 100 g, 5 dobles; la calculadora con tus gramos y tu merma) · 4. **¿Qué carne uso para una smash?** (blend de vacuno con ≈
20 % de grasa, picado del día; nada de madurada de más de 15 días) · 5. **¿Puedo servir la hamburguesa poco hecha?** (no hay temperatura
legal ni prohibición; la AESAN recomienda 70 °C 2 min y tu APPCC decide; la smash sale hecha) · 6. **¿Qué dice la ley de la freidora?**
(acrilamida: < 175 °C; aceite: polares < 25 %) · 7. **¿Qué licencias necesito?** · 8. **¿Cuánto se lleva Glovo o Uber Eats?** (30 % + IVA:
escandallo por canal) · 9. **¿Me sirve en México, Argentina, Colombia…?** (guía de equivalencias; el marco legal es el español) · 10. **¿Y una
franquicia?** (cifras de §2 frente al caso). Con el carrito o el food truck de smash → Plan Food Truck.

## 7. Sin verificar, preguntas abiertas y notas

- ❌ / 🟡: precio profesional de carne picada, brioche, potato bun, queso, patata fresca, aceite en garrafa, bacon y salsas (solo minorista);
  plancha de 100 cm, saladette, tostador de cinta y campana de 3 m; ticket medio de hamburguesería; salario de encargado; peso real del
  delivery en una hamburguesería con sala; número de hamburgueserías en España; reparto mensual de ventas; merma de cocción de la bola en
  plancha; litros de aceite y raciones por cambio. **Todo «estimación del kit, editable»** en Excel, calculadora, Word y landing; la calculadora
  pide pesar bolas y medir polares.
- **Fuentes a cotejar en la F3** (no cambian lo que se afirma): el Rgto. 853/2004 se leyó en una compilación oficial de 2008 (EUR-Lex no
  responde desde el Mac); los plazos de 6 y 15 días los confirma Madrid Salud en 2026 ✅ · el Rgto. 2017/2158, en su DOUE original · el art. 14
  del Rgto. 1169/2011 (alérgenos antes de pagar en la venta a distancia), el IVA del batido y el desglose del menú para llevar: 🟡 · la API del
  BOE ya trae el art. 91 con vigencia 1-12-2026: igual en lo citado, releer antes de publicar (= TAQ §1).
- **Para el motor (reportar, no arreglar)**: el comensal equivalente (1 pedido = 1,7) va en la nota de `cubiertos_dia`; los refrescos zero para
  llevar entran en el `pct` 0,28 de la línea partida; el aceite de girasol al 10 % solo afecta a `IVA_COMPRAS`.
- **Fuera de esta pareja (para una tanda de arreglos sin correo)**: (a) el **Kit de Tareas Hamburguesería vale 12 €**, no 14 €
  (`netlify/shared/product-prices.ts:55`, ficha l. 28); (b) su ficha promete «punto de carne (rare a well done)»
  (`tareas/kit-tareas-hamburgueseria.ts:55` y `:280`) mientras su contenido fija 70 °C en el centro (`contenido_kit_tareas_hamburgueseria.py:433`):
  la landing contradice al kit; (c) su tabla de congelación «Patties y carne picada cruda: 3-4 meses» (`…hamburgueseria.py:605`) no avisa del
  art. 7.2 cuando la picada es del local.
- **Decisiones** (las firma el arquitecto en `F1-camino.md` §2): nombre «Plan de Negocio: Hamburguesería Smash» · slug
  `plan-negocio-hamburgueseria` · unidad `comensal` con rotación encendida · semilla Sushi Bar (o Taquería) · caso B · coste de comida 28 % con su
  puente · Mes 1 = enero · **35 €** (= Taquería, Pollería, Sushi Bar: mismo formato y entregables; el Kit de Tareas de 12 € queda al lado).

## 8. Propuesta de la calculadora: «Carne, Patatas y Escandallo por Canal»

`calculadora-carne-patatas-escandallo-hamburgueseria.xlsx` (≤ 4 hojas; A4, protegida sin contraseña, verdes desbloqueadas; constantes grises
«1.000 g por kg» y «60 min por h»; helpers de `../plan-polleria/calculadora_pol_es.py`, = SUS-camino §4):

| Hoja | Entradas (verdes) | Cálculo |
|---|---|---|
| `Carne` | 3 columnas + 1 libre: **blend comprado picado** (8,90 €/kg, útil 100 %) · **pieza para picar en el local** (aguja o falda, 7,50 €/kg, limpieza 90 %, **sin fuente: mídelo**; minutos de limpiar y picar por kg 6 y €/h del cocinero) · **bolas compradas porcionadas** (€ por bola) · % de grasa (informativo, 20 %) · gramos por bola (100) · merma de bolas al cierre 3 % · merma de cocción en plancha (sin fuente: pesa 10 bolas antes y después) · desplegable «¿picas en el local?» (informativo) | **coste por kg útil** = precio ÷ útil ÷ (1 − merma) · **bolas por kilo** = 1.000 × (1 − merma) ÷ g (**la PAA: 10 de 100 g**) · coste por bola, por smash simple, doble y triple · gramos servidos · **«picar en el local te compensa mientras limpiarlo cueste menos de X € por kg»** · aviso fijo: picada ≤ 2 °C, del día si la picas, sin madurada (RD 1021/2022 arts. 4.1 y 7.2) |
| `Patatas` | **congelada** (1,50 €/kg, 150 g por ración, absorción 5 %) · **fresca** (0,60 €/kg, útil 75 %, absorción 10 %, minutos de pelar, cortar y remojar por kg, €/h) · aceite: litros por cuba 10, cubas 2, €/l 1,80, **raciones por cambio** (las que aguante con polares < 25 %, mídelo) y relleno diario % · raciones al día (comensales × 0,8) | coste por ración de cada patata con y sin mano de obra · **coste de aceite por ración** · kg de patata al día y litros de aceite al mes · **«la fresca te compensa si pelar y cortar cuesta menos de X € por kg»** · nota fija: < 175 °C y remojo o escaldado de la fresca (Rgto. 2017/2158) |
| `Escandallo` | IVA 10 % · objetivo de food cost 28 % · 14 productos (smash simple, doble, triple, bacon, oklahoma, la de la casa, crispy chicken, vegetal, patatas clásicas y cargadas, batido, postre, menú doble + patatas + bebida, pedido tipo de plataforma) con bolas, pan, lonchas, otros ingredientes € y ración de patata (de las dos hojas anteriores) · PVP con IVA de sala · caja y bolsa por canal (llevar 0,45 €, plataforma 0,60 €) · recargo de plataforma 15 % · comisión 30 % | coste, PVP sin IVA, food cost % con semáforo, PVP sugerido · **margen € por canal** (sala, para llevar, plataforma) y ranking · aviso fijo: las patatas viajan mal. Por defecto: doble ≈ 27 %, simple ≈ 22 %, patatas ≈ 8 %, ponderado ≈ 24 % (puente al 28 % del plan en Instrucciones) |
| `Instrucciones` | — | pesar 10 bolas y 10 raciones de patata; medir la merma de cocción y los polares; carne picada (arts. 4.1, 7.2 y 7.3 del RD 1021/2022; nada de madurada, Inf26008); cocción (sin temperatura legal; 70 °C AESAN; el APPCC decide); acrilamida y aceite; IVA; «estimación del kit, editable»; versión 1.0; bio |

**Gate `--autotest`** (VPS; = SUS-camino §4): pycel y caché ± 0,01 frente a `calcular()` con 3 juegos · coste útil = precio ÷ útil ÷ (1 − m) ·
bolas por kg = 1.000 × (1 − m) ÷ g · margen plataforma < para llevar < sala en el menú · doble por defecto en 24-30 % · A4, protección, 0 fórmulas
sin caché, 0 números tecleados en fórmulas (salvo 0/1) · DV · docProps · barrido y no latinos 0 · `parche_xml_xlsx.py --check`. `EXPUESTOS` →
`cifras --calc`: `COSTE_KG_UTIL_BLEND`, `COSTE_KG_UTIL_PIEZA`, `BOLAS_KG`, `COSTE_DOBLE`, `FC_DOBLE`, `FC_SIMPLE`, `COSTE_RACION_PATATA_CONG`,
`COSTE_RACION_PATATA_FRESCA`, `ACEITE_RACION`, `MARGEN_SALA_MENU`, `MARGEN_PLATAFORMA_MENU`.

## Fuentes

Leídas hoy: BOE-A-2022-21681 (RD 1021/2022, arts. 1-7, API de datos abiertos), Rgto. (CE) 853/2004 (anexo I, art. 1.5 y anexo III secc. V;
compilación de saludcastillayleon.es), DOUE L 304 de 21-11-2017 (Rgto. (UE) 2017/2158, copia en boe.es/doue), BOE-A-1989-2265 (Orden de
26-1-1989, consolidada), BOE-A-1992-28740 (LIVA art. 91, versiones del 8-10-2026 y del 1-12-2026), madrid.es (Madrid Salud, Inf26008,
2-feb-2026), aesan.gob.es (*Toxiinfección por Escherichia coli*, 18-4-2022, y su página de consejos) · glovoapp.com (Smash Hiro Málaga) ·
timeout.es (Smash Hiro Barcelona) · emprendedores.es (La Pepita) · lexpress-franchise.com (Harlem Smash Burger) · alimarket.es (Goiko,
Street Smash Burgers) · ecosistemastartup.com (DBK) · forbes.es (Vicio) · DataForSEO (F0). Snippets 🟡: fastfoodsmenu.com y just-eat.es
(Goiko), Uber Eats (Trafic Burger), tripadvisor, solomeat, bolusburger.com, asest.es, theobjective.com (Just Eat), elespanol.com (Vicio),
okdiario.com, supermercado.eroski.es, finditapp.es, hellopro.fr, hosteleria10.com (PDF), hitech2business.com, weber.com, infoagro.com,
infojobs.net, indomio.es, bizalia.com. Hermanos: POL, TAQ, SUS, PIZ, KT, BLOG (rutas en la cabecera).
