# L2 — SERP, demanda, vocabulario e intención: «Cómo Montar una Churrería-Chocolatería»

- **Producto:** guía «Cómo Montar» nº 51, tamaño L, 65 € orientativo. Hermana: `guia-chocolateria-obrador` (LIVE 19-sep).
- **Fecha de consulta de todos los datos:** 2026-10-03.
- **Método:** DataForSEO (`scripts/dataforseo.py vol` y `serp`, Google Ads search volume + SERP live desktop), GSC por MCP `gscServer` (`sc-domain:aichef.pro`, ventana 2026-07-05 → 2026-10-03 = 90 días), lectura de repo (`robots.txt`, `zona-app.ts`, hub, blog, CHS de la hermana).
- **Ids nuevos de esta lente:** `CUS-D*` = dato de demanda/sector medido hoy (no hay normativa aquí; la verificación legal es de otra lente).
- **Térmica:** `istats cpu temp` 46-52 °C durante toda la sesión; sin Playwright, sin builds, sin navegador. La regla de 65 °C queda también en la memoria del proyecto (`feedback_regla-termica-cpu-65-grados.md`, ya recogida).

## 0. Limitaciones declaradas (leer primero)

| Limitación | Efecto |
|---|---|
| El volumen de Google Ads agrupa variantes con y sin tilde: «churrería» = «churreria». | No se puede medir la grafía sin tilde por separado; la trampa de grafía aquí es otra (ver §1.3). |
| Google Ads redondea y agrupa: valores «10» = «entre 0 y 10-ish»; «None» = sin dato, **no** = cero. | Todo lo de 10 o menos se trata como «volumen despreciable», no como cifra. |
| El volumen de «churrería» (110.000 en ES) y «churros» (165.000) es de consumidor/local. | **No** es demanda de apertura. No entra en la conclusión de negocio. |
| Los SERP son de escritorio, ubicación nacional (España 2724) y México 2484 (solo 1 consulta). | La SERP móvil y local por provincia puede variar. El SERP de México para «como poner una churreria» devolvió resultados dominados por España (TripAdvisor.mx, Instagram, Facebook) y casi sin contenido mexicano de apertura: **señal débil, no concluyente**. |
| GSC: la propiedad no tiene consultas con «churr» ni «porra» en 90 días (filtro `contains`). La URL del post sí recibe impresiones, pero GSC anonimiza las consultas poco frecuentes. | Datos propios casi nulos: no hay base para afirmar posicionamiento por consulta. Ver §4. |
| No he verificado ninguna cifra de inversión, rentabilidad ni normativa de las páginas de la SERP: solo las cito como «lo que dice la SERP». | Nada de lo del §2 entra en el producto sin pasar por la lente de sector/normativa. |
| Franquicias (Chök, Maestro Churrero, KingChurro, Churro Planet, Pinocho, La Antigua Churrería, Desi…) citadas **solo por nombre**, como en la hermana. | Sin cifras de franquicia: no se verificaron contra la ficha oficial. |

## 1. Medición de demanda

### 1.1 España (2724, es) — búsquedas/mes, media de los últimos 12 meses según Google Ads, serie de los últimos 6 meses entre paréntesis

Fuente única: `dataforseo.py vol`, 2026-10-03 (ficheros de trabajo en el scratchpad de sesión). Los 4 del contexto no se repiten.

**Bloque A — apertura / montar (la intención del producto)**

| Keyword | Vol/mes | Comp | Últimos 6 meses | Lectura |
|---|---:|---|---|---|
| montar churreria | 50 | MEDIUM | 30,30,20,30,30,50 | orden de meses sin certificar |
| como montar una churreria | 30 | HIGH | 10,10,20,10,30,20 | ya medida en el contexto (30) |
| cuanto cuesta montar una churreria | 20 | LOW | 10×6 | |
| abrir una churreria | 10 | LOW | 10×6 | |
| como abrir una churreria | 10 | LOW | 10×6 | |
| poner una churreria | 10 | – | 0,10,0,10,10,0 | |
| negocio de churros | 10 | LOW | 10×6 | |
| rentabilidad churreria | 10 | LOW | 10×6 | |
| plan de negocio churreria | 10 | LOW | 10,0,0,10,10,0 | |
| licencia churreria | 10 | LOW | 10,10,10,10,0,0 | |
| trabajo churrero | 10 | LOW | | empleo, no apertura |
| montar una chocolateria | 10 | LOW | | la hermana: 5× menos que churrería |
| churreria rentable, churreria requisitos, churreria negocio, montar un negocio de churros, cuanto gana una churreria, churros caseros negocio, abrir chocolateria, obrador de churros, oferta empleo churrero | None | – | | sin dato en Google Ads |

**Suma del bloque A (todas las variantes de «montar/abrir/poner/negocio/rentabilidad/licencia/plan»): ≈ 190 búsquedas/mes en España** (suma aritmética de las filas con dato, más las 50 y 30 del contexto; no desduplicada: las variantes se solapan). Es demanda **minúscula y estable (orden de meses sin certificar)**.

**Bloque B — maquinaria y puesto (compra de equipo / formato móvil)**

| Keyword | Vol/mes | Comp | Últimos 6 meses |
|---|---:|---|---|
| puesto de churros | 880 | LOW | 880,590,720,1000,880,1000 |
| maquina de churros | 590 | HIGH | 480,480,320,480,390,590 |
| churreria ambulante | 480 | LOW | 480,320,260,320,320,480 |
| maquina churros | 320 | HIGH | 260,320,140,170,210,260 |
| churrera profesional | 260 | HIGH | 110,70,70,90,170,260 |
| churreria a domicilio | 170 | MEDIUM | 70,40,50,70,90,140 |
| dosificadora de churros | 70 | HIGH | |
| food truck churros | 70 | LOW | 30,50,50,40,70,70 |
| freidora para churros / freidora churros | 50 / 50 | HIGH | |
| carrito de churros | 40 | HIGH | |
| churros feria | 30 | LOW | |
| churros food truck | 20 | LOW | |
| aceite para freir churros | 20 | HIGH | 10,10,10,10,20,30 |
| maquina churros industrial / maquina de churros precio | 20 / 20 | HIGH | |
| churros industriales | 10 | HIGH | |

Competencia HIGH = hay anunciantes de maquinaria (compra); confirmado en la SERP de «maquina de churros» (§2).

**Bloque C — franquicia, curso, traspaso**

| Keyword | Vol/mes | Nota |
|---|---:|---|
| churreria franquicia | 70 | (contexto: «franquicia churreria» 70) |
| franquicia churros | 30 | |
| franquicias de churrerias | 20 | |
| curso de churrero | 40 | |
| traspaso churreria | 40 | 40,40,30,30,40,70 |
| churreria cafeteria / cafeteria churreria | 170 / 480 | mezcla local+apertura; ver §1.3 |

**Bloque D — consumidor / receta / producto (NO es la intención de la guía; sirve para captación lateral y vocabulario)**

| Keyword | Vol/mes | Nota |
|---|---:|---|
| churros | 165.000 | consumidor |
| churreria cerca de mi | 135.000 | consumidor, local pack |
| porras | 12.100 | |
| tejeringos | 8.100 | 6.600,4.400,4.400,5.400,6.600,8.100 |
| chocolate con churros | 5.400 | |
| receta churros | 3.600 | |
| churros sin gluten | 2.900 | serie 880…2.900, orden sin certificar |
| churreria madrid | 2.900 | |
| porras y churros | 1.600 | |
| churros caseros / masa de churros / churros y chocolate | 1.300 / 1.300 / 1.300 | |
| calentitos | 1.000 | |
| jeringos | 880 | |
| churros congelados | 720 | serie 320…590, orden sin certificar; toca el escenario (f) B2B congelado |
| churros a domicilio | 720 | 390,320,320,480,390,720 |
| churros rellenos | 590 | |
| churreria artesanal | 260 | |
| chocolate espeso | 140 | |
| churros precocinados / masa de churros congelada | 20 / 10 | |

**Estacionalidad medida (Google Ads, últimos 6 meses ≈ abril-septiembre 2026, orden cronológico inverso al de la API: primer valor = mes más reciente cerrado).** El helper imprime los 6 meses en el orden que devuelve la API; no tengo certificado el orden mes a mes. Lo que sí es robusto: «churros» oscila 135.000-201.000; «chocolate a la taza» 1.000-3.600 y «chocolate con churros» 1.600-4.400 entre valle y pico (estacionalidad marcada; mes del pico sin certificar). **Sin fuente del orden de meses**: no usar para el gráfico de estacionalidad hasta pedir `monthly_searches` con año/mes (el helper no los imprime).

### 1.2 LATAM y EE. UU. en español — `--pais` + `--idioma es` explícitos

Búsquedas/mes. «–» = None o 0. El volumen de «churrería» incluye la variante sin tilde.

| Keyword | MX 2484 | CO 2170 | AR 2032 | CL 2152 | PE 2604 | US 2840 |
|---|---:|---:|---:|---:|---:|---:|
| churros | 49.500 | 9.900 | 18.100 | 9.900 | 8.100 | 201.000 |
| churreria / churrería | 8.100 | 170 | 8.100 | 320 | 170 | 6.600 |
| churreria cerca de mi | 6.600 | 50 | 6.600 | 170 | 90 | 720 |
| churros rellenos | 4.400 | 110 | 320 | 210 | 110 | 880 |
| como hacer churros | 1.900 | 720 | 1.900 | 880 | 320 | 1.000 |
| churrera | 1.600 | 210 | 2.400 | 880 | 140 | 590 |
| maquina de churros | 1.600 | 210 | 480 | 1.600 | 170 | 480 |
| maquina para churros | 880 | 110 | 110 | 590 | 50 | 260 |
| carrito de churros | 320 | 50 | 70 | 170 | 50 | 90 |
| puesto de churros | 260 | 10 | 90 | 10 | 10 | 50 |
| chocolate caliente | 5.400 | 1.000 | 1.600 | 5.400 | 1.900 | 2.900 |
| chocolate a la taza | 70 | 40 | 20 | 70 | 30 | 260 |
| churros y chocolate | 390 | 10 | 20 | 10 | 10 | 2.900 |
| negocio de churros | 50 | 10 | 10 | 10 | 10 | 10 |
| franquicia de churros | 50 | 10 | 20 | 10 | 10 | 10 |
| franquicia churros | 20 | 10 | 10 | 10 | 10 | – |
| curso de churros | 20 | 10 | 10 | 10 | 10 | 10 |
| como poner una churreria | 10 | – | 10 | – | – | 10 |
| poner una churreria | 10 | – | 10 | – | – | – |
| abrir una churreria | 10 | – | 10 | – | – | 10 |
| montar una churreria | – | – | 10 | – | – | 10 |
| cuanto cuesta poner una churreria | 10 | – | 10 | – | – | 10 |
| churreria ambulante | 10 | – | 10 | 10 | 10 | 10 |
| churreria chocolateria | 10 | 10 | 10 | 10 | 10 | 50 |
| rentabilidad churreria | 10 | – | 10 | – | – | – |

Lecturas honestas:
1. **«Poner/abrir/montar una churrería» no mide nada en ningún país de LATAM ni en EE. UU.** (≤ 10 en todos). Ni «poner» en México, que es el verbo natural allí. El producto no tiene demanda de búsqueda de apertura fuera de España.
2. **Sí hay demanda de equipamiento en México y Chile:** «maquina de churros» 1.600 y «churrera» 1.600 (MX), 1.600 y 880 (CL); competencia HIGH. Es intención de compra de maquinaria, no de guía.
3. **México es el mayor mercado de consumidor** después de EE. UU.: «churros» 49.500, «churros rellenos» 4.400 (aquí el relleno pesa más que en España: 590). Si en F3 se quiere un blog/landing de adaptación LATAM, el término es «churros rellenos» y «máquina de churros», no «montar».
4. **EE. UU. en español:** «churros y chocolate» 2.900 (5× España en proporción a su tamaño) y «churreria chocolateria» 50 (la mayor de todos los países; serie 20,50,40,10,70,170, orden de meses sin certificar). Demanda de consumidor, no de apertura.
5. «chocolate caliente» (5.400 MX y CL) **no** es lo mismo que «chocolate a la taza» (70): en LATAM se dice «chocolate caliente»; «a la taza» es casi inexistente (≤ 70). Dato clave de vocabulario (§5).
6. **No se midió US en inglés** («churro shop», «how to open a churro shop») porque queda fuera del alcance del encargo (guía en español); queda como hueco para una futura adaptación EN, conforme a la regla «duplicar y adaptar».

### 1.3 Trampas de grafía e intención

| Trampa | Resultado medido | Veredicto |
|---|---|---|
| «churreria»/«churrería» | Mismo volumen (Google lo agrupa) | no hay trampa de tilde |
| «tejeringos» 8.100 vs «jeringos» 880 vs «calentitos» 1.000 | Sinónimos regionales con volumen propio | se citan en primera mención |
| «montar churreria» (50) vs «montar una churreria» (50, contexto) | Misma magnitud sin «una» | tratar como un único racimo ≈ 100 |
| «cafeteria churreria» 480 vs «churreria cafeteria» 170 | Intención ambigua: local de desayunos (consumidor) o negocio | no se atribuye a apertura; la SERP de apertura relacionada («Traspaso de churreria ambulante», «maquinaria para montar una churrería») sí lo es |
| «porras» 12.100 | Intención de consumidor (receta/producto) | no apertura |
| Volumen de «churreria» 110.000 | SERP con local pack (3 bloques) y cero AI Overview | **consulta de consumidor; confirma que el volumen grande NO es de la guía** |

## 2. SERP directa — 9 consultas (8 en España, 1 en México)

Fuente: `dataforseo.py serp`, escritorio, 2026-10-03.

### 2.1 Tabla de bloques e intención

| Consulta | AI Overview | PAA | Vídeo | Local pack | Intención real | Quién rankea (top) |
|---|:--:|:--:|:--:|:--:|---|---|
| montar una churreria 2026 | **sí** | sí (9) | no | no | **apertura** | **aichef.pro/blog/ia-churrerias-guia-completa (posición 1)**; mrahosteleria.es; hostelmarkt.com; loomispay.com; lexpress-franchise.com; envanature.com; sillasmesas.es; rrhhdigital.com; churrofacil.com |
| como montar una churreria | **sí** | sí (9) | sí (1) | no | **apertura** | inblan.com; TikTok; maestrochurrero.com; forocoches (2014, 2009); ehosa.es (licencia ambulante, 2016); yimiglobal; scribd; montarchurreria.com |
| churreria | no | no | no | **sí (3)** | **consumidor/local** | TripAdvisor, Facebook, Instagram, Glovo, Uber Eats, turismo municipal |
| franquicia churreria | no | sí (9) | no | **sí (3)** | **franquicia** (informacional-comercial) | infofranquicias.com; franquicia.net; mundofranquicia; centraldefranquicias; start-franchising; kingchurro; Churros Factory |
| maquina de churros | no | sí (9) | sí (1) | no | **compra de maquinaria** (popular_products + Amazon) | Amazon, churrofacil.com, masterchurros.com, maquinaschurros.com, expomaquinaria.es, milanuncios |
| puesto de churros | no | sí (9) | no | **sí (12)** | **consumidor/local + mobiliario/remolque** | TripAdvisor, churrosur.com, maquinariachurros.es (remolques TM), remolquesmarchal.es |
| licencia churreria | **sí** | sí (9) | no | no | **apertura / legal** | milanuncios (churrofacil); tablón municipal Zaragoza; BOP Cáceres; noticia multa 1.500 € Zaragoza; tulicenciadeactividad.es (Málaga obligada a cerrar por no instalar campana) |
| chocolateria churreria | no | sí (9) | sí (1) | **sí (3)** | **consumidor/local** | chocolateria1902.com, San Ginés, Chocalte, Choco&Co, esmadrid.com |
| como poner una churreria (MX 2484) | **sí** | sí (9) | no | no | **apertura**, pero SERP mal localizada | TripAdvisor.mx, Instagram, Facebook, milanuncios, asest.es (plan de negocio ambulante) |

**Validación del filtro de intención (8 consultas España + 1 México):** LOCAL PACK presente y AI Overview ausente ⇒ consumidor (churreria, puesto de churros, chocolateria churreria, franquicia churreria). AI Overview presente y local pack ausente ⇒ apertura (montar, como montar, licencia, como poner MX). Regla cumplida en 9 de 9. «maquina de churros» no tiene ninguna de las dos señales y se clasifica por `popular_products` + Amazon.

### 2.2 Qué dice la SERP (citas de la SERP, no verificadas — `CUS-D1…D9`)

| Id | Dato (como lo publica la fuente) | Fuente y fecha del resultado | Estado |
|---|---|---|---|
| CUS-D1 | «Montar una churrería te va a costar, en España y en 2026, entre 12.000 € y 50.000 €» (nuestro propio post; rango típico local pequeño 25.000-40.000 €) | `https://aichef.pro/blog/ia-churrerias-guia-completa`, fecha de SERP 19-jul-2026; fichero `astro-site/src/content/blog/es/ia-churrerias-guia-completa.md:30,60` | **sin fuente propia verificada**: es una cifra del post, no se reutiliza en la guía sin pasar por la lente de sector |
| CUS-D2 | Maquinaria base de una churrería de barrio: 800-1.500 € (orientativo) | `https://mrahosteleria.es/churrerias-como-escoger-tus-maquinas-para-exito/`, 29-sep-2025 | **sin verificar**; comparar con precios de catálogo antes de usar |
| CUS-D3 | Dosificadora automática con variador y pedal: 2.250,00 € | `https://www.churrofacil.com/tienda/es/12-maquinarias-y-repuestos` (snippet SERP, 2026-10-03) | precio de catálogo del vendedor; **comprobar en la lente de sector** |
| CUS-D4 | Freidora churrera profesional a gas 14 L: 2.290,75 € | `https://www.multiserviciosvalles.com/churreras` (snippet SERP, 2026-10-03) | idem |
| CUS-D5 | King Churro: inversión 20.000-25.000 € (congelador, tostador, horno…) | `https://lexpress-franchise.com/es/articulos/como-abrir-una-churreria-top-10-de-marcas-en-espana/`, 9-ene-2026 | cifra de franquiciador vía medio; solo por nombre en la guía |
| CUS-D6 | Churro Planet: inversión desde 44.000 € (canon 5.000 € incluido, sin obra civil); Pinocho Churros Gourmet: 73.000 € inversión, 58.000 € aportación, 10 puntos de venta | `https://www.centraldefranquicias.es/franquicia/churro-planet/`; `https://www.start-franchising.com/es/franquicias/pinocho-churros-gourmet/` | idem; **no se citan cifras de franquicia con nombre sin ficha oficial** |
| CUS-D7 | Un local de churrería no necesita mucho espacio: 30-50 m² | `https://www.sillasmesas.es/blog/proyectos-hosteleria/como-montar-churreria/` | de un vendedor de mobiliario; contrastar con CHS-37a (75 m²) y CHS-37b (74 m²) de la hermana, que son **más grandes** porque son chocolatería-churrería con sala |
| CUS-D8 | Multa de 1.500 € a una churrería de Zaragoza (Miralbueno) por carecer de licencia de funcionamiento | `https://www.aragondigital.es/articulo/zaragoza/multan-1500-E-conocida-churreria-miralbueno-carecer-licencia-funcionamiento/20250603193544926082.am`, 3-jun-2025 | **noticia**, no norma; sirve de gancho, no de dato legal |
| CUS-D9 | Una churrería de Málaga, obligada a cerrar por no instalar campana extractora de humos | `https://tulicenciadeactividad.es/una-churreria-de-malaga-obligada-a-cerrar-por-no-instalar-campana-extractora-de-humos/` | **confirma que la fritura cambia la licencia** (hipótesis de la lente legal); el título es de una consultora de licencias, sin verificar contra norma |

### 2.3 Guion de PAA para la FAQ de compra (sumando las 9 SERP; repetidas = señal fuerte)

**Preguntas que aparecen en ≥ 3 SERP (núcleo de la FAQ):**
1. ¿Cuánto dinero necesito / cuánto vale / cuánto cuesta montar una churrería? (montar 2026, como montar, licencia, franquicia, MX)
2. ¿Es rentable vender churros / un negocio de churros? (5 de 9 SERP)
3. ¿Qué se necesita / qué necesito para poner una churrería? (4 de 9)
4. ¿Cuántos churros salen de 1 kilo de harina? (**7 de 9 SERP**, la más repetida: pregunta de escandallo; candidata a tabla de rendimiento)
5. ¿Cuánto gana un churrero / cuánto dinero se gana con una churrería? (4 de 9)
6. ¿Cuánto cuesta una franquicia de churros? (4 de 9)
7. ¿Cuánto suele valer una docena de churros? / ¿cuánto vale 1 kg de churros? / ¿cuántos churros son 5 euros? (precio de venta: el lector busca el ticket)
8. ¿Cuánto vale una máquina de hacer churros? / ¿cuánto cuesta una máquina para hacer churros?

**Una vez cada una (cola larga útil):** ¿Cómo empezar un negocio de churros? · ¿Qué nombre puedo poner a mi negocio de churros? · ¿Qué vende una churrería? · ¿Cómo hacer churros profesionales? · ¿Cuál es la mejor harina para hacer churros? · ¿Cuáles son las mejores franquicias de churrerías en España? · ¿Cómo se les dice a los churros en España? · ¿Qué es más sano, churros o porras? · ¿Qué dos tipos de churros hay? · ¿Cuál es la churrería más famosa de Madrid? (consumidor; ignorar).
**México (SERP 9):** ¿Qué franquicia puedo poner con 50/100/200 mil pesos? — **pregunta de capital en pesos**: la FAQ «¿sirve fuera de España?» la absorbe sin cifrar en pesos.

**Qué NO está en el PAA y la guía sí debe cubrir (huecos frente a la competencia de la SERP):** extracción de humos y licencia por fritura (el único indicio en SERP es la noticia de Málaga y la de Zaragoza), aceite de fritura (compuestos polares), alérgenos, convenio, estacionalidad. **Ninguna página del top 10 de «montar una churrería 2026» los trata como bloque propio en su snippet**; sin verificar el cuerpo de cada página (no abierto por límite térmico/alcance). Hueco de diferenciación probable, **no confirmado**.

## 3. Quién compite por la intención «montar una churrería» (y de qué tipo son)

| Tipo | Ejemplos (SERP 1 y 2) | Lectura para la guía |
|---|---|---|
| Vendedores de maquinaria/mobiliario con blog | mrahosteleria.es, sillasmesas.es, tiendaiglesias.com, cocimia.com, inblan.com, churrofacil.com, maquinaschurros.com, mimobiliariohosteleria.es | La competencia SEO es **vendedor que quiere vender máquinas**; su guía es de equipamiento. La guía de pago se diferencia por: números reales, licencia, PRL, calidad del aceite, plan financiero |
| Medios de franquicia | emprendedores.es, lexpress-franchise.com, infofranquicias.com | Cubre «franquicia vs independiente» solo comercialmente |
| Gestorías/licencias | declaracion-responsable.com, tulicenciadeactividad.es, ehosa.es | Cubren licencia, no el modelo económico |
| Foros/UGC | forocoches (2009, 2014), reddit r/askspain (`https://www.reddit.com/r/askspain/comments/1t8hfsr/`), Facebook, TikTok | Demanda real de un emprendedor sin información fiable |
| **Propio** | **aichef.pro/blog/ia-churrerias-guia-completa: posición 1 en «montar una churreria 2026»** | Ya tenemos la primera posición en una consulta de apertura de volumen bajo. **El blog es el canal de captación natural** (§6) |

## 4. Datos propios en GSC (`sc-domain:aichef.pro`, 2026-07-05 → 2026-10-03)

| Consulta | Resultado |
|---|---|
| Páginas con «churrer» en la URL | `https://aichef.pro/blog/ia-churrerias-guia-completa`: **4 clics, 133 impresiones, CTR 3,01 %, posición media 4,9**. El resto (`blog.aichef.pro/<idioma>/…`): 0 clics, ≤ 8 impresiones cada una: URLs legacy WordPress (gu, hi, is, mr, sq, ta, es): **posiciones de URL legacy, no leer como suelo** (regla del `CLAUDE.md`). |
| Consultas con «churr» (filtro `contains`, 90 días, query+page) | **sin datos**: ni una fila. GSC anonimiza consultas poco frecuentes: el único texto que devolvió la API para la URL es «cuánto presupuesto necesito» (1 impresión, posición 5,0). |
| Consultas con «porra» | sin datos |
| Consultas con «chocolate» | 5 filas, todas de otras páginas: `chocolate ia` y `chocolate para ia` → `/blog/chocolateria-artesanal-e-ia-una-combinacion-innovadora` (9 y 13 impresiones, 0 clics). Nada de «chocolate a la taza». |
| Páginas con «chocolateria-obrador» en la URL | **sin datos**: la landing `/guia-chocolateria-obrador` no aparece en 90 días (recién publicada el 19-sep; además, el `noindex` de las 88 páginas de zona app). |

Lectura: **hay ~133 impresiones/90 días en el post, con 4 clics**, es decir ≈ 1,5 impresiones/día. No hay demanda propia que cuantificar más allá de eso. No inventar «posiciona por X».

## 5. Vocabulario ES vs LATAM (lista de equivalencias para la PRIMERA mención de cada documento)

La columna «volumen» es de §1; las equivalencias son **uso coloquial conocido**, medido solo donde hay cifra. **Sin fuente lingüística:** el reparto geográfico exacto de cada sinónimo no está medido por esta lente; la regla es: es-ES manda, LATAM en paréntesis una sola vez.

| Concepto | Término base (es-ES) | Equivalencias (primera mención) | Volumen que lo avala |
|---|---|---|---|
| El producto frito en tira | churro | porra (el churro grueso en es-ES; **12.100/mes**), tejeringo (**8.100**), calentito (**1.000**), jeringo (**880**); en LATAM «churro» sin distinción | tejeringos 8.100 ES vs 12.100 porras |
| El local | churrería-chocolatería | churrería; «chocolatería» solo no basta en ES (la hermana: «chocolatería churrería» 1.000) | churrería 110.000 ES; MX 8.100; AR 8.100; US 6.600 |
| La bebida | chocolate a la taza | chocolate espeso (140 ES), **chocolate caliente** (MX 5.400, CL 5.400, PE 1.900, CO 1.000, AR 1.600, US 2.900: es el término LATAM) | «a la taza» MX 70, CL 70, CO 40, AR 20, PE 30 → casi inexistente fuera de España |
| La máquina | churrera | máquina de churros (MX 1.600, CL 1.600), dosificadora (ES 70), manga (sin cifra medida), freidora para churros (ES 50) | churrera ES 2.900, MX 1.600, AR 2.400, CL 880 |
| La masa | masa de churros | (sin variante medida) | ES 1.300 |
| El taller | obrador | taller / cocina de producción | **sin fuente** (término de la hermana) |
| Costes por plato | escandallo | costeo (LATAM) | **sin fuente en esta lente**; término ya fijado en la hermana |
| Abrir el negocio | montar / abrir | **poner** (México: «poner una churrería»: 10/mes en MX, 0 en la mayoría) | todos ≤ 10 |
| El formato móvil | churrería ambulante / puesto | carrito (MX 320, CL 170), caseta, remolque, food truck (ES 70) | puesto de churros ES 880, MX 260 |
| El pago por unidades | docena de churros / 1 kg | (precio de venta por peso en ES: «churros por peso»; en MX: «por orden») | **sin fuente medida**: usar solo «por peso» y «por unidad» |

Regla de redacción para el pipeline: la guía lleva «churro» como término único (con «porra» como churro grueso); **«tejeringo», «calentito» y «jeringo» solo en la primera mención** del documento y no vuelven; en LATAM **«chocolate caliente» se menciona como equivalente de «chocolate a la taza» una sola vez**.

## 6. Conclusión de negocio honesta

### 6.1 Tráfico SEO alcanzable (honesto)

| Pieza | Demanda (ES) | Competencia SERP | Alcanzable |
|---|---|---|---|
| Landing `/guia-churreria-chocolateria` por «montar una churrería» | 50 + 30 + 20 + 10 ≈ 110-190/mes (todas las variantes de apertura, no desduplicadas) | SERP dominada por vendedores de maquinaria; **ya tenemos la posición 1 con el post** | **Máximo: decenas de visitas/mes** con tasa de conversión de producto digital 65 € incierta. **La landing no es un canal SEO**; «montar una churrería» no llega a 100 búsquedas ni sumando todas las variantes. Confirmado con la regla de John (19-sep): volumen cero no descalifica; el veto es canibalizar |
| Todo el nicho de apertura en LATAM y EE. UU. (es) | ≤ 10/mes por país | — | **cero**. No hay captación SEO fuera de España |
| Maquinaria (puesto, churrera, máquina) | ES 2.900+590+880+480+320 ≈ 5.000/mes; MX 1.600+1.600+880; CL 1.600+880 | HIGH, vendedores + Amazon | Competir contra tiendas de maquinaria **no es viable** ni coherente; no se escribe contenido de ese nicho salvo como puente |
| Churrería-chocolatería consumidor | 110.000+ | local pack | **no es nuestra audiencia** |

**La venta de la guía no entra por SEO.** Entra por los canales propios (hub, lista de compradores, blog, plataforma), como en los productos anteriores. Hay 133 impresiones/90 días en el post.

### 6.2 Piezas de captación de blog con demanda real (nombre + slug + volumen + SERP)

| # | Pieza propuesta | Slug propuesto | Keyword principal | Vol ES | SERP | Veredicto |
|---|---|---|---|---:|---|---|
| 1 | **Ampliar** el post existente (no crear uno nuevo): cuánto cuesta + licencia por fritura + PAA | `ia-churrerias-guia-completa` (ya existe) | montar una churrería (50) + cuánto cuesta (20) | 110-190 | AI Overview + PAA; posición 1 | **Sí, y es una ampliación, no un post nuevo**: canibalizaría si se crea otro. Comparar encabezados primero (regla del `CLAUDE.md`) |
| 2 | Puesto/carrito/churrería ambulante: licencia y requisitos | `churreria-ambulante-licencia` | churrería ambulante (480) + puesto de churros (880) | 1.360 | **local pack en «puesto de churros»**: mezcla consumidor; la primera está dominada por TripAdvisor | Solo si la lente legal confirma contenido propio; frontera con `plan-negocio-food-truck` y `kit-tareas-food-truck` (enlazar, no duplicar) |
| 3 | Cuántos churros salen de 1 kg de harina (escandallo) | `cuantos-churros-salen-de-1-kg-de-harina` | PAA en 7/9 SERP | **sin volumen medido** (es PAA, no keyword medida) | PAA | **Probar con `vol`** antes de decidir; candidato a captación con CTA a `kit-escandallos` |
| 4 | Franquicia de churrería vs independiente | `franquicia-churreria-vs-independiente` | franquicia churreria (70) + franquicia churros (30) | 120 | medios de franquicia, local pack | Bajo; solo como enlace saliente de la guía |
| 5 | Churros congelados / B2B (escenario f) | `churros-congelados-negocio` | churros congelados (720) | 720 | sin SERP medida | **Sin SERP: no decidir**; medir antes |
| 6 | Porras vs churros (diferencia) | `diferencia-porras-churros` | porras (12.100) + tejeringos (8.100) | 20.200 | **sin SERP medida**; consumidor | **Alta demanda, intención de consumidor**: puerta de entrada de tráfico al sitio, pero no a la guía. Medir SERP antes; es contenido de glosario (mediana 1.285 palabras) |

**Lo que NO se recomienda:** posts «churros» (165.000) o «churrería cerca de mí» (135.000): consumidor + local pack, cero conversión posible a una guía de 65 €.

### 6.3 Nombre y slug

Comprobado en repo (2026-10-03): `astro-site/src/pages/` no tiene `churr*`; `_redirects` sin coincidencias; `zona-app.ts` no tiene ninguno de los tres slugs; `robots.txt` bloquea `/guia-*-access` y `/guia-*-library` (y sus homónimos por familia), **no** `/guia-churreria-chocolateria` ni `/guia-churreria` ni `/guia-como-montar-churreria` (ninguno acaba en `-access`/`-library`). El único slug con riesgo sería uno que acabe en `-library` o `-access`.

| Opción | Coherencia con hermanas | Con el hub | Riesgo | Veredicto |
|---|---|---|---|---|
| **`guia-churreria-chocolateria`** | Mismo patrón `guia-<nicho>[-obrador]`: hermanas `guia-chocolateria-obrador`, `guia-pasteleria-obrador`, `guia-panaderia-obrador`. Solo falta el sufijo `-obrador` | Coincide con el nombre del hub («Cómo Montar una Churrería-Chocolatería», `ProductosDigitalesHubPage.astro:1015`) | Ninguno de robots/URLs/redirects; la keyword «churreria chocolateria» tiene 1.900 (y «chocolateria churreria» 1.000) | **RECOMENDADA** |
| `guia-churreria-chocolateria-obrador` | Idéntico patrón a las 3 hermanas con obrador | Alarga el slug; el obrador de masa es un elemento más, no la oferta | Solo longitud | Alternativa válida si el equipo prefiere simetría estricta |
| `guia-churreria` | Más corto | **Pierde «chocolatería»**: la frontera con la hermana (D1) es justamente que la chocolatería de taza va aquí | **Confunde con la hermana**: «chocolatería» es el término que desambigua | No |
| `guia-como-montar-churreria` | No sigue el patrón de las guías (`guia-<nicho>`) | Idéntico al «Cómo Montar», pero ninguna otra guía lo repite en el slug | Slug largo | No |

**Recomendación: slug `guia-churreria-chocolateria`** (landing) con rutas hijas `guia-churreria-chocolateria-access` y `guia-churreria-chocolateria-library`, cubiertas ya por `/guia-*-access` y `/guia-*-library`. Nombre público: **«Cómo Montar una Churrería-Chocolatería»**, exactamente como está en el hub, para no mover URL ni tarjeta. Sin siglas españolas en el titular (cumple la regla del 5-sep).

### 6.4 Coherencia con la hermana (frontera ya decidida, D1/D3)

- **Hay solapamiento de demanda real y es útil:** «churreria chocolateria» 1.900 y «chocolateria churreria» 1.000 (ES) son consultas de consumidor mixtas, pero el contexto indica que **«montar una churrería» es 5× «montar una chocolatería»** (50 contra 10, repetido aquí; el contexto lo traía de la hermana). Esa es la razón de negocio de que exista un producto aparte: la demanda de apertura de la churrería es mayor que la de la chocolatería boutique, pero ambas diminutas.
- **Venta cruzada en las dos direcciones:** la guía de la churrería-chocolatería enlaza a `guia-chocolateria-obrador` (bombonería, templado, obrador de chocolate fino) y la hermana ya trata «la chocolatería de taza y churros: por qué es OTRO negocio» (epígrafe cap. 01). La relación debe ser **«si lo tuyo es chocolate fino y bombones, la hermana; si es churro frito + chocolate a la taza, esta»**.
- **No contradecir:** la hermana solo cifra la chocolatera (527 € sin IVA, CHS-46a); esta guía **cifra todo el montaje de la churrería** (fritura, dosificadora, extracción de humos, aceite). Los datos sobre traspasos reales CHS-37a (75 m²) y CHS-37b (74 m², traspaso 82.000-95.000 €, alquiler 910 €/mes) y el margen del churro CHS-31 (85-90 % bruto frente a «un poco más del 50 %» de un maestro churrero; **hay que publicar los dos números y explicar la diferencia**, como indica el propio CHS-31) **se reutilizan por id**, no se re-verifican. Atención: son los **mismos datos con los que la hermana ya dijo «otro negocio»**.
- **Fronteras con LIVE (no canibalizar):** `plan-negocio-food-truck` / `kit-tareas-food-truck` (formato c), `plan-negocio-cafeteria` / `kit-tareas-cafeteria` (formato e), `kit-escandallos`, `pack-appcc`, Guía Food Cost, y el post ES `ia-churrerias-guia-completa` (**ya posición 1**). **El post debe enlazar a la guía y la guía al post**, y **no se crea un segundo post de «montar una churrería»**.

### 6.5 Decisiones que esta lente deja abiertas

| # | Decisión | Recomendación |
|---|---|---|
| 1 | Slug y nombre | `guia-churreria-chocolateria`; nombre del hub sin cambios |
| 2 | Caso central a cifrar | Formato (a) local fijo con obrador de masa y sala; es el único con demanda de apertura medible («montar una churrería» se refiere a local y a puesto; la SERP lo trata como «local fijo o food truck», AI Overview de «como montar una churreria»). Puesto/feria (c) y churro añadido a cafetería (e) como **variantes** con remisión a los kits LIVE; franquicia (d) como **comparativa sin cifras de marcas**; obrador B2B (f) como **apéndice o fuera** hasta medir «churros congelados» (720) |
| 3 | Qué piezas de blog crear | Solo **ampliar** el post existente; medir SERP de «porras vs churros» y «cuántos churros salen de 1 kg de harina» antes de crear nada |
| 4 | LATAM | No hay demanda de apertura; adaptar por «FAQ ¿sirve fuera de España?», no por captación. El material medido (máquina de churros 1.600 MX/CL) es compra de equipo |
| 5 | Medir estacionalidad con meses explícitos | Pedir `monthly_searches` con año/mes (el helper solo imprime valores); no usar el orden actual |
| 6 | SERP de «porras vs churros» y «churros congelados» | No medidas aquí: hacerlo antes de decidir blog de captación |

### 6.6 Resumen de reglas aplicadas

- Cada dato: URL + fecha (2026-10-03) o id reutilizado (CHS-31, CHS-37a, CHS-37b, CHS-46a); ids nuevos `CUS-D1…D9`.
- Nada de memoria del modelo: cifras de volumen salen de `dataforseo.py`; el vocabulario marcado «sin fuente» está marcado.
- No he escrito ni modificado ningún fichero del repo salvo este informe. Sin commits.
