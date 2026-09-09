# LENTE 2 — SERP, demanda, vocabulario e intención

**Producto:** «Cómo Montar una Pastelería» (guía premium de apertura, producto nuevo nº 4 del ciclo; sería el nº 48 del catálogo).
**Fecha de la investigación:** 2026-09-09, madrugada del 2026-09-10 (CEST). Todas las consultas de API se lanzaron entre las 23:4x del 09-sep y las 00:2x del 10-sep.
**Autor:** lente L2 (research), sesión Claude Code.

---

## 0. Método y limitaciones DECLARADAS

### Método

| Paso | Herramienta | Alcance real |
|---|---|---|
| Volumen de búsqueda | `scripts/dataforseo.py vol` → DataForSEO Google Ads *search_volume/live* | **129 keywords** en España + **32 keywords × 6 mercados** (MX 2484, CO 2170, AR 2032, CL 2152, PE 2604, EE. UU. en español 2840) = **321 mediciones** |
| SERP orgánica en vivo | `scripts/dataforseo.py serp` → DataForSEO *serp/google/organic/live/advanced*, desktop, depth 20, PAA click depth 2 | **10 consultas** en España |
| Datos propios | MCP `gscServer`, propiedad `sc-domain:aichef.pro`, ventana **2026-06-11 → 2026-09-09** (90 días) | 9 consultas filtradas por *query* y por *page* |
| Nomenclatura y activos | lectura directa del repo | `src/data/products-catalog.ts`, `astro-site/src/pages/`, `astro-site/public/robots.txt`, hub ES y Astro |

Ficheros crudos de las consultas (temporales de sesión, no versionados):
`/private/tmp/claude-501/-Users-johnguerrero-chefpro-modernize/21c749d4-019e-47fd-bd62-733839f97842/scratchpad/vol_*.txt` y `serp_*.txt`.

### Lo que NO he podido verificar, y por qué

1. **El texto de los AI Overviews.** Cuatro de las diez SERP traen AI Overview, pero DataForSEO lo devuelve como `"asynchronous_ai_overview": true` con `"markdown": null` e `"items": null`. **Sé que el bloque existe y en qué consultas, pero no puedo citar su contenido ni sus fuentes citadas.** Para leerlo haría falta el endpoint asíncrono de AIO de DataForSEO (otro coste) o mirar la SERP a mano. Queda como tarea abierta.
2. **Las cifras de CAPEX de `lahostelera.com`** que el encargo trae heredadas (proyecto 5.000 €, obra media 81.000 €, equipamiento 46.000 €, marketing 5.000 €): **no las he abierto ni verificado en esta lente**. Las dejo marcadas **«sin fuente verificada por L2»**; si entran en el producto, tienen que pasar por la lente de datos (L3) con URL y fecha propias. No las repito como buenas.
3. **`mcp__gscServer__get_search_by_page_query` devolvió «No search data found» para `https://aichef.pro/guia-panaderia-obrador`**, cuando la misma propiedad y ventana consultadas con `get_advanced_search_analytics` (filtro `page contains`) sí devuelven 2 clics / 35 impresiones. **Es una discrepancia de la herramienta, no del dato** (probablemente filtro `equals` exacto frente a `contains`). He usado el camino `contains` en todo el informe. Anotarlo: fiarse del `get_search_by_page_query` habría hecho concluir «la landing hermana no existe en Google», que es falso.
4. **DataForSEO devuelve `None` (no `0`) para keywords sin datos en Google Ads.** `None` ≠ «cero búsquedas»: significa «Google Ads no sirve dato para esa cadena en ese mercado». En las tablas lo escribo `—`. No he convertido ninguna en cero.
5. **Google Ads agrupa por *close variants*.** Volúmenes idénticos entre variantes (ver §1.0) delatan agrupación, no coincidencia real.
6. **No he medido competencia** (autoridad de dominio, backlinks, antigüedad de los que rankean). Eso es la lente L1.
7. **Ventana GSC de 90 días con `data_state` por defecto** («all»): los últimos 2-3 días pueden moverse.

---

## 1. Demanda medida

> Fuente de toda esta sección: DataForSEO, endpoint `keywords_data/google_ads/search_volume/live`, vía `scripts/dataforseo.py`. Consultado el **2026-09-09/10**. Volumen = medias mensuales de Google Ads; `COMP` = competencia publicitaria (no dificultad SEO).

### 1.0 Primera trampa: los acentos NO son una variante de grafía; las PALABRAS sí

Medido en España el 2026-09-09:

| Par | Volumen | Lectura |
|---|---|---|
| `pastelería` / `pasteleria` | **110.000 / 110.000** | idénticos → Google Ads normaliza diacríticos |
| `repostería` / `reposteria` | **6.600 / 6.600** | idénticos |

**Conclusión:** la trampa del `chile crisp` / `chili crisp` **no se reproduce con tildes** en este nicho — poner o quitar el acento no cambia el dato. Pero **sí se reproduce con la elección de palabra y con las preposiciones**, y ahí sí hay factores grandes:

| Variante | Vol/mes (ES) | Factor |
|---|---|---|
| `obrador pasteleria` | **390** | — |
| `obrador de pasteleria` | **320** | ×0,82 |
| `maquinaria pasteleria` | **70** | — |
| `maquinaria de pasteleria` | **50** | ×0,71 |
| `maquinaria de pasteleria precio` | — (sin dato) | — |
| `pasteleria artesanal` | **480** | — |
| `pasteleria artesana` | **260** | ×0,54 |

`artesanal` vale casi el doble que `artesana`. Si el copy usa sólo una de las dos, deja la mitad fuera. **Recomendación: usar «artesanal» como forma principal y «artesana» como sinónimo en el cuerpo.**

### 1.1 España — el bloque de VOLUMEN ALTO (y por qué NO nos sirve casi nada)

| Keyword | Vol/mes | COMP | Intención real (§2) |
|---|---|---|---|
| pastelería / pasteleria | **110.000** | LOW | Local / navegacional |
| confiteria | **9.900** | LOW | **Local puro** (12 resultados de local pack) |
| obrador | **9.900** | LOW | **Local + definición** (RAE en pos. 5) |
| chocolateria | **9.900** | LOW | Local |
| repostería / reposteria | **6.600** | LOW | Mixta (recetas + local) |
| carnet manipulador de alimentos | **6.600** | HIGH | Formación (transversal, no de apertura) |
| bolleria | **4.400** | LOW | Producto / recetas |
| dulceria | **3.600** | LOW | Local (y en LATAM, otra cosa: §1.3) |
| cafeteria pasteleria | **2.900** | LOW | **Local** — pero su PAA tiene oro (§2.3) |
| pasteleria sin gluten | **2.400** | LOW | **Consumidor comprando tarta** — cero valor |
| panaderia pasteleria | **1.900** | LOW | Local |
| pastelero | **1.900** | LOW | Empleo / definición |
| abatidor de temperatura | **1.900** | HIGH | Compra de maquinaria |
| tartas personalizadas | **2.900** | HIGH | Consumidor |
| viennoiserie | **1.000** | LOW | Definición / técnica |
| croissanteria | **1.000** | LOW | Marca / local |
| cursos de reposteria | **880** | HIGH | Formación |
| pasteleria vegana | **880** | LOW | Consumidor |
| pasteleria artesanal | **480** | LOW | Local (§2.6) |
| pasteleria a domicilio | **480** | HIGH | Consumidor |
| obrador pasteleria | **390** | LOW | Local + empleo |
| pasteleria online | **390** | HIGH | Consumidor |
| tienda de tartas | **390** | LOW | Consumidor |
| obrador de pasteleria | **320** | LOW | Local + empleo (ya medido el 09-sep) |

**Lectura dura: todo lo que pasa de 300 búsquedas/mes en este nicho lo teclea alguien que quiere COMPRAR UN PASTEL, no alguien que quiere abrir una pastelería.** Esa es la conclusión central de la lente.

### 1.2 España — el bloque de INTENCIÓN DE APERTURA (nuestro comprador)

| Keyword | Vol/mes | COMP |
|---|---|---|
| obrador compartido | **50** | LOW |
| franquicias de pasteleria | **40** | MEDIUM |
| franquicia pasteleria *(medido el 09-sep, dato heredado)* | **40** | — |
| montar una panaderia | **40** | LOW |
| requisitos para montar un obrador en casa | **30** | LOW |
| requisitos obrador pasteleria | **30** | LOW |
| traspaso pasteleria | **30** | LOW |
| montar una pasteleria *(dato heredado 09-sep)* | **20** | — |
| montar una pasteleria en casa | **20** | HIGH |
| vender reposteria desde casa españa | **20** | LOW |
| vender tartas desde casa | **20** | LOW |
| como montar una panaderia | **20** | MEDIUM |
| cuanto cuesta montar una panaderia | **20** | LOW |
| obrador de tartas | **20** | MEDIUM |
| iva pasteleria | **20** | LOW |
| **como montar una pasteleria** *(dato heredado 09-sep)* | **10** | HIGH |
| cuanto cuesta montar una pasteleria | **10** | LOW |
| presupuesto para montar una pasteleria | **10** | — |
| coste montar pasteleria | **10** | — |
| como montar un obrador · montar un obrador | **10** cada una | LOW |
| requisitos para abrir un obrador | **10** | — |
| como montar una cafeteria pasteleria | **10** | LOW |
| que se necesita para montar una pasteleria | **10** | HIGH |
| como poner una pasteleria | **10** | — |
| negocio de pasteleria · negocio de reposteria · negocio de postres | **10** cada una | LOW/MEDIUM |
| como montar una reposteria | **10** | — |
| montar una confiteria | **10** | — |
| montar una chocolateria | **10** | LOW |
| appcc pasteleria · convenio colectivo pasteleria · normativa obrador pasteleria | **10** cada una | LOW |
| rentabilidad de una pasteleria · plan de negocio pasteleria pdf | **10** cada una | LOW |
| local para pasteleria · diseño de pasteleria | **10** cada una | LOW |
| maquinaria pasteleria segunda mano · horno para pasteleria precio | **10** cada una | HIGH |
| estudio de mercado pasteleria | **0** | — |

**Sin dato en España (`—`, no cero):** `montar una reposteria`, `abrir una reposteria`, `abrir una confiteria`, `obrador de pan y pasteleria`, `cuanto cuesta un obrador`, `cuanto cuesta montar un obrador`, `licencia obrador`, `registro sanitario obrador`, `registro sanitario pasteleria`, `escandallo pasteleria`, `alergenos pasteleria`, `etiquetado alergenos pasteleria`, `epigrafe iae pasteleria`, `plan appcc obrador`, `licencia de apertura pasteleria`, `como abrir una pasteleria en españa`, `requisitos para abrir una pasteleria en españa`, `obrador de pasteleria en casa`, `obrador en casa legal`, `venta de reposteria casera legislacion`, `curso para montar una pasteleria`, `pastelero autonomo`, `montar obrador de pasteleria`, `inversion pasteleria`, `margen de beneficio pasteleria`, `como poner precio a mis tartas`, `cuanto cobrar por una tarta`, `abrir un obrador`, `escuela de pasteleria`, `laboratorio de pasteleria`, `mesa refrigerada pasteleria`, `pasteleria takeaway`, `cocina compartida alquiler`.

> ⚠️ **Que `escandallo pasteleria`, `alergenos pasteleria` o `registro sanitario obrador` no tengan dato no significa que el capítulo sobre ellos sobre.** Significa que nadie lo busca con ESA cadena — el comprador ya llega al producto por otra vía y esos capítulos son valor de entrega, no de captación. Es exactamente el criterio de John para las librerías de prompts.

**Suma de todo el clúster de intención de apertura de pastelería en España: ~330 búsquedas/mes**, repartidas en ~35 cadenas distintas de las cuales 25 están en 10/mes. Comparación útil: una sola keyword de consumidor, `pasteleria sin gluten`, vale 2.400 — **siete veces todo nuestro clúster junto**.

### 1.3 LATAM + EE. UU. en español — 32 keywords × 6 mercados

Volúmenes en búsquedas/mes. `—` = sin dato en Google Ads.

| Keyword | ES 2724 | MX 2484 | CO 2170 | AR 2032 | CL 2152 | PE 2604 | US-es 2840 |
|---|---|---|---|---|---|---|---|
| pasteleria | 110.000 | **135.000** | 8.100 | 14.800 | 22.200 | 14.800 | 22.200 |
| dulceria | 3.600 | **110.000** | 3.600 | 1.000 | 880 | 880 | **14.800** |
| reposteria | 6.600 | **22.200** | 5.400 | 9.900 | 6.600 | 4.400 | 4.400 |
| pasteleria artesanal | 480 | 480 | 140 | 720 | 90 | 260 | 480 |
| horno para pasteleria | *(70 «horno de»)* | 390 | 170 | 170 | 70 | 110 | 30 |
| negocio de postres | 10 | 260 | 50 | 10 | *(n/d en top)* | 30 | 20 |
| vitrina para pasteleria | *(50 «vitrina de»)* | 110 | 50 | 20 | 50 | 20 | 10 |
| franquicia de pasteleria | *(40 «franquicias de»)* | 90 | 10 | 10 | *(n/d)* | *(n/d)* | *(n/d)* |
| negocio de reposteria | 10 | 90 | 20 | 30 | 20 | 30 | 10 |
| taller de pasteleria | 40 | 30 | 20 | 70 | 40 | 70 | 10 |
| negocio de pasteleria | 10 | 40 | 10 | 10 | 10 | 20 | 10 |
| maquinaria para pasteleria | *(70 «maquinaria pasteleria»)* | 20 | 10 | 20 | 70 | 20 | 10 |
| **como montar una pasteleria** | **10** | **10** | **10** | **10** | **10** | **10** | **10** |
| montar una pasteleria | 20 | 10 | 10 | 10 | 10 | 10 | — |
| abrir una pasteleria | 10 | 10 | 10 | 10 | 10 | 10 | — |
| como abrir una pasteleria | 10 | 10 | **0** | 10 | 10 | 10 | 10 |
| cuanto cuesta poner una pasteleria | — | 10 | 10 | 10 | 10 | 10 | 10 |
| como poner una pasteleria | 10 | 10 | 10 | 10 | 10 | 10 | 10 |
| plan de negocio pasteleria | *(10 «…pdf»)* | 10 | 10 | 10 | 10 | 10 | 10 |
| plan de negocios de una pasteleria | — | 10 | 10 | 10 | 10 | 10 | 10 |
| como montar una dulceria | — | 10 | 10 | 10 | *(n/d)* | 10 | *(n/d)* |
| obrador de pasteleria | 320 | 10 | 10 | 10 | 10 | *(n/d)* | 10 |
| rentabilidad de una pasteleria | 10 | 10 | **0** | **0** | 10 | *(n/d)* | *(n/d)* |
| cuanto gana una pasteleria | *(10, heredado)* | 10 | 10 | 10 | *(n/d)* | *(n/d)* | 10 |
| vender postres desde casa | *(20 «vender tartas…»)* | 10 | 10 | 10 | *(n/d)* | *(n/d)* | 10 |
| requisitos para abrir una pasteleria | *(10, heredado)* | 10 | **0** | 10 | *(n/d)* | *(n/d)* | *(n/d)* |
| como iniciar un negocio de reposteria | — | 10 | 10 | 10 | *(n/d)* | *(n/d)* | *(n/d)* |
| cuanto cobrar por un pastel | — | 10 | 10 | 10 | *(n/d)* | *(n/d)* | *(n/d)* |
| pasteles por encargo | *(210 «tartas por encargo»)* | 10 | 10 | 10 | *(n/d)* | *(n/d)* | *(n/d)* |
| licencia para abrir una pasteleria | — | — | — | — | — | — | — |
| costeo de pasteles | — | — | — | — | — | — | — |
| como sacar el costo de un pastel | — | — | — | — | — | — | — |

**Tres hallazgos de LATAM:**

1. **El patrón es idéntico en los siete mercados: genéricos gigantes, apertura en 10.** No hay un solo mercado hispanohablante donde «cómo montar una pastelería» y sus variantes pasen de 10/mes. **La demanda de apertura de pastelería en español, sumando España + México + Colombia + Argentina + Chile + Perú + EE. UU., no llega a 500 búsquedas/mes**, y está atomizada en decenas de cadenas de 10.
2. **`dulceria` en México vale 110.000 y en EE. UU. en español 14.800** — órdenes de magnitud sobre España (3.600). Pero **en México «dulcería» no es una pastelería**: es la tienda de golosinas/piñatas y el mostrador de dulces del cine. **Es un falso amigo comercial: usar «dulcería» como sinónimo de pastelería en el copy de LATAM sería un error de vocabulario, no un acierto de volumen.** (Ver §4.)
3. **`costeo de pasteles` y `como sacar el costo de un pastel` no devuelven dato en NINGÚN mercado**, incluidos MX/CO/PE donde «costeo» es la palabra nativa. Es un recordatorio de que el vocabulario LATAM correcto sirve para que el texto se entienda, **no** para captar tráfico que no existe.

---

## 2. Análisis SERP — 10 consultas en vivo (España, desktop, 2026-09-09/10)

> Fuente: DataForSEO `serp/google/organic/live/advanced`, depth 20, `people_also_ask_click_depth: 2`, `location_code: 2724`, `language_code: es`.

### 2.1 `confiteria` (9.900/mes) — **descartada: local pack puro**
Bloques: `local_pack ×12`, `compare_sites`, `people_also_ask`, `organic ×20`, `related_searches ×2`. **Sin AI Overview.**
Rankean: `grupconfiteria.com`, `confiteriasanantonio.es`, `rocambolesc.com`, TripAdvisor, `confiteriaochoa.com` (Sevilla), `confiteriasolla.com` (Pontevedra), Instagram y Facebook de confiterías locales.
PAA: «¿Qué es una confitería?», «¿Qué son los productos de confitería?», «¿Hay alguna confitería en San Antonio?», «¿Cuáles son algunas pastelerías famosas en España?», «¿Cuáles son las 10 mejores pastelerías del mundo?».
**Veredicto: 9.900 búsquedas/mes de gente buscando una confitería CERCA. Cero valor para el producto.** Este es el caso «qué es un token = criptomonedas» de este nicho.

### 2.2 `obrador` (9.900/mes) — **descartada, pero con un regalo**
Bloques: `local_pack ×12`, `organic ×19`, `images`, `people_also_ask`, `related_searches ×2`. Sin AIO.
Rankean: `lobrador.es` (franquicia de panadería), **Wikipedia** (pos. 2), obradores locales de Madrid/Ciudad Real/Jerez, y **el DLE de la RAE en pos. 5**.
PAA: «¿Qué es un obrador?», «¿Qué es un obrador en España?», «¿Qué hace un obrador?», «¿Cuál es un sinónimo de obrador?», «¿Cómo se dice obrador en inglés?».
**El regalo — definición del DLE (https://dle.rae.es/obrador, consultado 2026-09-09):** «*Taller artesanal, especialmente el de confitería y repostería.* **Sin.: confitería, dulcería.**» Es la fuente autorizada para la nota de vocabulario del producto y zanja la equivalencia obrador↔taller.
**Veredicto: intención mixta local+definición. No es una keyword de apertura.**

### 2.3 `cafeteria pasteleria` (2.900/mes) — **descartada como keyword, PERO su PAA vale oro**
Bloques: `local_pack ×3`, `hotels_pack`, `organic ×19`, `people_also_ask`, `images ×2`. Sin AIO.
Rankean: TripAdvisor, `bilbaoturismo.net`, `saborea-madrid.com`, Expansión («Las 10 mejores cafeterías-pastelerías de Madrid»), Facebook. **Turismo y guías de consumidor, 100 %.**
PAA: **«¿Cuánto cuesta montar una cafetería pastelería?»** ← la ÚNICA pregunta de apertura en toda la SERP, seguida de «¿Cuáles son los 3 tipos de repostería?», «¿Quién es el mejor pastelero de España?», «¿Cuál es la tarta de queso más premiada de España?».
**Veredicto: no se puede rankear ni se debe intentar. Pero Google confirma que la variante «pastelería-cafetería» es una pregunta de coste real → capítulo del producto, no keyword.**

### 2.4 `pasteleria sin gluten` (2.400/mes) — **descartada, y conviene decirlo alto**
Bloques: `local_pack ×12`, `compare_sites`, `organic ×20`, `images ×2`. Sin AIO. **Sin PAA.**
Rankean: `helmacakes.com` (Barcelona), `sanalocura.es`, `nicolina.es` (Madrid), `leonthebaker.com`, `pastelerialaorientalsingluten.com`, `bakeryzerozero.com`, Instagram `@dulcesfree`, `lactosa.org` («Las 10 mejores pastelerías sin gluten en España»).
**Veredicto: 2.400 búsquedas/mes de CELÍACOS COMPRANDO TARTA.** Si alguien mira la hoja de volúmenes sin la SERP, propondrá un post «Pastelería sin gluten» pensando que capta emprendedores. Captaría consumidores que no compran una guía de 65 €. **Es la trampa más cara de este research.**

### 2.5 `franquicias de pasteleria` (40/mes) — **intención comercial real, competencia de directorios**
Bloques: `organic ×20`, `local_pack ×9`, `people_also_ask`, `related_searches ×2`. Sin AIO.
Rankean: `emprendedores.es` («8 franquicias de panaderías y pastelería», 30-oct-2024), `mundofranquicia.com`, `franquiciator.es`, `franquiciashoy.es`, `franquicias.es`, `100franquicias.com`. **Directorios verticales de franquicia con años de autoridad.**
PAA: «¿Cuánto dinero se necesita para abrir una pastelería?», «¿Cuáles son las 10 franquicias más rentables?», «¿Qué franquicias puedo montar por menos de 15.000 euros?», «¿Qué negocio montar con 7.000 euros?».
Dato de la propia SERP (`franquicias.es`, consultado 2026-09-09): «*La inversión de estas franquicias de Pastelería está en torno a los 20.000 euros*». **Cifra de tercero, útil como contraste en el capítulo de modelos de negocio; verificar en L3 antes de usarla.**
**Veredicto: intención de apertura confirmada, pero es un mercado de directorios. No competir; sí cubrir «franquicia vs. marca propia» como capítulo.**

### 2.6 `pasteleria artesanal` (480/mes) — **descartada: local**
Bloques: `local_pack ×12`, `organic ×18`, `images ×2`, `people_also_ask`, `related_searches ×2`. Sin AIO.
PAA: «¿Qué es la pastelería artesanal?», «¿Cuáles son los 7 tipos de pastelería?», «¿Cuál es la diferencia entre repostería y pastelería?», «¿Cuánto gana una pastelera al mes?», «¿Cuál es el salario de un pastelero?».
**Veredicto: local + definición + empleo. El PAA «diferencia entre repostería y pastelería» sí es material de glosario y de la nota de vocabulario.**

---

### 2.7 `requisitos para montar un obrador en casa` (30/mes) — 🟢 **LA MEJOR SERP DEL NICHO**
Bloques: **`ai_overview`**, `organic ×17`, `people_also_ask`, `video`, `related_searches ×2`.
Rankean, por orden:
1. `manipulador-alimentos.net/vender-comida-hecha-en-casa/` — «¿Es legal vender comida hecha en casa? Requisitos en 2026» (13-jul-2026)
2. **`pasteleriaparatodos.com/montar-obrador-pasteleria-casa/`** — «Montar un Obrador de Pastelería en Casa: Guía Paso a Paso» (18-jun-2025)
3. `ayudatpymes.com/gestron/montar-pasterleria-online/` — «Cómo montar una pastelería online desde casa | Requisitos»
4. `madridlicencias.com/blog/puedo-montar-mi-negocio-de-elaboracion-de-tartas-o-comidas-preparadas-en-casa/`
5. `dianaverdu.com/tipo-obrador-montar-espana/` — «¿Qué tipo de obrador puedes montar en España?» (03-jun-2025) → **taxonomía de tipos de obrador, incluida «obrador en casa (con licencia sanitaria)»**
6. `asyfal.com/blog/puedo-montar-un-negocio-alimentacion-desde-casa`
7. `certicalia.com/blog/requisitos-para-abrir-un-obrador-pasteleria` (24-nov-2025) — «requisitos, licencias, certificados y **costes aproximados**»
8. `blogsaverroes.juntadeandalucia.es/agroalimentaria/vender-comida-casera-andalucia/` (31-jul-2025) — **fuente institucional autonómica**
9. `escueladeobradores.com/formacion-abre-tu-obrador-plan-y-normativas/` — **formación de pago competidora**

PAA (**el guion de la FAQ**): «¿Es legal vender comida en casa?» · «¿Es legal vender comida desde casa?» · «¿Qué requisitos necesito para vender comida desde mi casa?» · «¿Qué necesito para vender comida desde casa?» · **«¿Cuál es la multa por vender comida sin permiso en España?»** · «¿Qué tipo de comida puedo vender en mi casa?» · «¿Cómo puedo empezar a vender conservas caseras?» · «¿Cuál es la comida más rentable para vender?».
Relacionadas: `Puedo montar un obrador en casa` · `Montar una pastelería en casa` · `Vender tartas desde casa` · `Requisitos para vender comida desde casa en españa` · `Licencia para vender comida hecha en casa` · `Vender repostería desde casa España` · **`Multa por vender comida sin permiso`**.

**Veredicto: 30 búsquedas/mes, pero es la SERP con la intención más pura y más monetizable del nicho.** El miedo legal («¿es legal?», «¿cuál es la multa?») es lo que mueve a esta persona. **Y es exactamente el perfil que compra una guía de apertura.**

### 2.8 `montar una pasteleria en casa` (20/mes) — 🟢 **la hermana, mismo veredicto**
Bloques: **`ai_overview`**, `video`, `people_also_ask`, `organic ×16`, `related_searches ×2`.
Rankean: **`pasteleriaparatodos.com/obrador-en-casa/`** en pos. 1 — «Monta tu obrador de pastelería en casa, legalízalo y hazlo rentable. **7 módulos, plantillas reales y soporte directo. Tamara Viñas · Le Cordon Bleu Madrid**» ← **producto de pago directamente competidor, en la posición 1**. Luego `aprende.com`, `blog.cib.education`, `monouso.es`, `agendapastelera.com`, `packento.com`, `dianaverdu.com/como-abrir-obrador/` (31-jul-2023), Reddit r/AskBaking, `asyfal.com`.
PAA: «¿Es posible abrir un negocio de pastelería en casa?» · «¿Es legal vender tartas caseras en España?» · «¿Qué se necesita para iniciar una pastelería?» · **«¿Es rentable abrir una pastelería?»** · «¿Cuál es el postre más rentable para vender?» · «¿Qué dulces dejan buena ganancia?» · «¿Cuáles son los 10 postres más vendidos?» · «¿Qué postres están en tendencia?».
Relacionadas: `Vender repostería desde casa España` · `Vender tartas desde casa` · `Montar un obrador en casa` · `Como montar una pastelería` · `Como abrir una pasteleria en españa` · **`Montar una pastelería es rentable`** · `Puedo vender pasteles desde casa` · `Postres para emprender desde casa`.

### 2.9 `vender reposteria desde casa españa` (20/mes) — 🟢 **misma familia, confirma el clúster**
Bloques: **`ai_overview`**, `organic ×18`, `people_also_ask`, `video`, `related_searches ×2`.
Pos. 1: `manipulador-alimentos.net` de nuevo. Pos. 2: `ayudatpymes.com` — «*sí, es totalmente legal montar y vender pasteles desde casa en España, pero no es un "ahorro de trámites", sino un cambio en la naturaleza de los…*». Pos. 3: `pasteleriaparatodos.com/obrador-en-casa/` (otra vez el producto de pago).
PAA: «¿Es legal vender tartas caseras en España?» · «¿Qué necesito para vender postres desde casa?» · «¿Es posible abrir un negocio de pastelería en casa?» · «¿Puedo vender comida desde casa en España?» · «¿Cuánto cuesta poner un foodtruck?» · «¿Qué negocios de comida puedo empezar desde casa?».

### 2.10 `obrador compartido` (50/mes) — 🟢 **el hueco más limpio: cero competencia comercial**
Bloques: **`ai_overview`**, `organic ×19`, `related_searches ×2`. **Sin PAA.**
Rankean, y esto es lo interesante: `naviaporcia.com` (grupo de acción local), `bcnagraria.diba.cat` (**Diputació de Barcelona**), `cooccio.com` (obrador compartido de Barcelona), `leaderoriente.es` (PEPAC 2023-2027), Instagram `@massa`, `thenewbarcelonapost.com` (14-mar-2025), `puebloingenio.org`, **`acsa.gencat.cat/es/seguretat_alimentaria/obradors-compartits/`** (Agència Catalana de Seguretat Alimentària).
**Veredicto: 50/mes con SERP 100 % institucional y asociativa. No hay una sola pieza comercial explicando el obrador compartido como VÍA DE ENTRADA para abrir una pastelería con inversión mínima.** `cooccio.com` lo vende como servicio («mínima inversión», «inicio inmediato»), pero no como guía. **Es el hueco editorial más claro que ha salido de esta lente.**

### Resumen de bloques SERP

| Consulta | Vol/mes | AIO | PAA | Local pack | Vídeo | Intención | ¿Nuestra? |
|---|---|---|---|---|---|---|---|
| confiteria | 9.900 | no | sí | **12** | no | Local | ❌ |
| obrador | 9.900 | no | sí | **12** | no | Local + definición | ❌ |
| chocolateria | 9.900 | *(no medida)* | — | — | — | Local | ❌ |
| cafeteria pasteleria | 2.900 | no | sí | 3 + hotels | no | Local/turismo | ❌ (PAA sí) |
| pasteleria sin gluten | 2.400 | no | **no** | **12** | no | Consumidor | ❌❌ |
| pasteleria artesanal | 480 | no | sí | **12** | no | Local + empleo | ❌ |
| obrador compartido | 50 | **sí** | no | no | no | **Informacional B2B** | ✅✅ |
| franquicias de pasteleria | 40 | no | sí | 9 | no | **Comercial apertura** | ⚠️ directorios |
| requisitos … obrador en casa | 30 | **sí** | sí | no | sí | **Apertura + miedo legal** | ✅✅✅ |
| montar una pasteleria en casa | 20 | **sí** | sí | no | sí | **Apertura** | ✅✅✅ |
| vender reposteria desde casa españa | 20 | **sí** | sí | no | sí | **Apertura** | ✅✅ |

**Patrón limpio y accionable: la presencia de LOCAL PACK y la ausencia de AI OVERVIEW marcan las consultas que NO son nuestras. Las cuatro consultas con AI Overview son exactamente las cuatro de intención de apertura.** Es el filtro más barato para clasificar cualquier keyword nueva de este nicho.

---

## 3. Datos propios — Google Search Console

> Fuente: MCP `gscServer`, propiedad `sc-domain:aichef.pro`, ventana **2026-06-11 → 2026-09-09** (90 días), search_type WEB. Consultado el 2026-09-09/10.

### 3.1 Contexto del sitio

| País | Clics | Impresiones | CTR | Posición media |
|---|---|---|---|---|
| España | 581 | 41.825 | 1,39 % | 22,7 |
| México | 495 | 38.830 | 1,27 % | 9,7 |
| India | 316 | 5.739 | 5,51 % | 11,5 |
| EE. UU. | 225 | 31.325 | 0,72 % | 13,3 |
| Colombia | 223 | 13.813 | 1,61 % | 9,1 |
| Argentina | 195 | 17.742 | 1,10 % | 9,0 |
| Perú | 168 | 12.612 | 1,33 % | 8,6 |
| Italia | 148 | 8.362 | 1,77 % | 11,1 |
| Chile | 142 | 9.845 | 1,44 % | 8,7 |
| Francia | 121 | 5.925 | 2,04 % | 16,2 |

El sitio recibe tráfico real. La pregunta es cuánto de él es de pastelería.

### 3.2 Consultas con `pastel*` — 90 días

| Consulta | Página | Clics | Impr. | Pos. |
|---|---|---|---|---|
| os agentes da pastelaria | `/pt/casos-uso/consultoria/confeiteiro-consultor` | 0 | 23 | 5,5 |
| os agentes da pastelaria | `/pt/casos-uso/consultoria/padeiro-consultor` | 0 | 2 | 18,0 |
| pastelería | `/usos/rol/repostero-pastelero` | 0 | 1 | **2,0** |
| pastelería congelada monoporción | `/blog/libreria-de-prompts-para-pasteleria-creativa-ai` | 0 | 1 | 15,0 |
| sauce pour pastel | `/fr/blog/sauces-meres` | 0 | 1 | 4,0 |

### 3.3 Consultas con `reposter*` — 90 días

| Consulta | Página | Clics | Impr. | Pos. |
|---|---|---|---|---|
| la repostería | `/blog/ia-para-panaderias` | 0 | 1 | 4,0 |
| la repostería | `/usos/rol/repostero-pastelero` | 0 | 1 | **1,0** |
| universidad de reposteria | `blog.aichef.pro/top-10-escuelas-pasteleria-profesional-estados-unidos-2026/` | 0 | 1 | 8,0 |

### 3.4 `obrador`, `tarta` — 90 días

**Cero filas. Ninguna. `obrador` no ha generado una sola impresión en 90 días; `tarta` tampoco.**

### 3.5 `chocolate` — 90 días

| Consulta | Página | Clics | Impr. | Pos. |
|---|---|---|---|---|
| chocolate ia | `/blog/chocolateria-artesanal-e-ia-una-combinacion-innovadora` | 0 | 4 | 7,2 |
| chocolate schools | `blog.aichef.pro/en/Top-10-chocolate-schools…` | 0 | 4 | 96,0 |
| chocolate school | *(la misma legacy)* | 0 | 2 | 85,5 |
| chocolateiro | `/pt/casos-uso/consultoria/chocolateiro-consultor` | 0 | 1 | 8,0 |

### 3.6 El total, dicho sin adornos

**El universo pastelería/repostería/obrador/tarta/chocolate de aichef.pro suma ~47 impresiones y CERO clics en 90 días**, y de esas 47 **la mitad son portuguesas** (`os agentes da pastelaria`, 25). En español, las consultas de este universo que llegan a aichef.pro caben en cinco filas y suman **5 impresiones**.

**Y hay algo peor que el volumen bajo: las posiciones son buenísimas y no traen nada.** `/usos/rol/repostero-pastelero` rankea en **posición 1,0** para «la repostería» y en **2,0** para «pastelería», con **1 impresión cada una**. Estar el primero de Google en este nicho no vale nada porque nadie teclea eso.

⚠️ **Trampa del histórico legacy, confirmada aquí:** dos de las filas (`universidad de reposteria`, `chocolate school[s]`) cuelgan de `blog.aichef.pro`, el subdominio ya 301-eado. Son historia, no suelo desde el que arrancar.

### 3.7 Las landings propias más parecidas — el mejor predictor que tenemos

**Familia `kit-tareas-*` (14 verticales, 12 € cada uno), 90 días:**

| Landing | Clics | Impr. | Pos. |
|---|---|---|---|
| `/kit-tareas` (hub) | 8 | 351 | 7,0 |
| `/kit-tareas-hotel` | 1 | 119 | 9,2 |
| `/kit-tareas-cafeteria` | 3 | 46 | 11,2 |
| `/kit-tareas-restaurante-creativo` | 0 | 42 | 14,2 |
| `/kit-tareas-dark-kitchen` | 1 | 38 | 9,4 |
| `/kit-tareas-asador` · `/kit-tareas-hamburgueseria` | 0 | 34 c/u | 9,3 / 12,3 |
| `/kit-tareas-chef-privado` | 1 | 32 | 7,9 |
| `/kit-tareas-food-truck` | 1 | 31 | 10,4 |
| `/kit-tareas-heladeria` | 1 | 30 | 9,6 |
| `/kit-tareas-catering` | 1 | 26 | 10,6 |
| `/kit-tareas-pizzeria` | 0 | 25 | 5,9 |
| `/kit-tareas-tapas-bar` | 0 | 17 | 6,0 |
| `/kit-tareas-panaderia` | 2 | 16 | 13,6 |
| `/kit-tareas-chocolateria` | 0 | 12 | 6,4 |
| **`/kit-tareas-pasteleria`** | **0** | **8** | **4,6** |
| `/kit-tareas-bar` | 0 | 7 | 7,4 |
| `/kit-tareas-marisqueria` | 0 | 4 | 5,5 |
| `/kit-tareas-sushi-bar` | 0 | 1 | 5,0 |
| **Total familia** | **19** | **873** | — |

**`/kit-tareas-pasteleria`: posición media 4,6 — casi la mejor de toda la familia — y 8 impresiones, 0 clics en 90 días.** Es la demostración más limpia de que aquí el problema no es rankear, es que no hay a quién.

**Familia `guia-*` (las «Cómo Montar», 65 €), 90 días, sólo URLs de `aichef.pro`:**

| Landing | Clics | Impr. | Pos. |
|---|---|---|---|
| `/guia-restaurante-peruano` | 2 | 114 | 5,7 |
| `/guia-restaurante-mexicano` | 2 | 66 | 9,6 |
| `/guia-restaurante-japones` | 1 | 53 | 7,4 |
| `/guia-restaurante-gastronomico` | 0 | 50 (+1 con UTM) | 13,6 |
| `/guia-restaurante-casual` | 0 | 46 | 9,0 |
| **`/guia-panaderia-obrador`** | **2** | **35** | **7,4** |
| `/guia-restaurante-nikkei` | 0 | 10 | 5,7 |
| `/guia-food-cost-ingenieria-menu` | 0 | 7 | 6,9 |
| `/guia-dark-kitchen` | 0 | 4 | 39,2 |
| **Total línea** | **7** | **386** | — |

**`/guia-panaderia-obrador` — la hermana exacta del producto que se va a construir — lleva 2 clics y 35 impresiones en 90 días.** Y al pedir el desglose por consulta, **GSC devuelve cero filas**: las 35 impresiones vienen de consultas por debajo del umbral de anonimización, o sea que **ni una sola keyword identificable manda tráfico a esa landing**.

**Toda la línea de guías de 65 € junta: 7 clics en 90 días. Eso es lo que el SEO aporta hoy a la línea de producto más cara del catálogo.**

---

## 4. Vocabulario: España ↔ LATAM

Equivalencias para la **primera mención** (regla de la casa: español de España como base, equivalencia LATAM entre paréntesis la primera vez y luego el término de España).

| Concepto | España (principal) | LATAM (equivalencia primera mención) | Nota / fuente |
|---|---|---|---|
| El oficio y la tienda | **pastelería** | **repostería** (MX/CO/PE/AR); **pastelería** también se usa | `pasteleria` gana en los 7 mercados (§1.3); `reposteria` es fuerte en MX (22.200) y AR (9.900) |
| Sinónimo culto/regional | **confitería** | **confitería** (AR/UY, muy vivo) | DLE: sinónimo de obrador |
| ⚠️ Falso amigo | — | **dulcería** ≠ pastelería | En MX (110.000) y US-es (14.800) «dulcería» es tienda de golosinas / mostrador de dulces del cine. **NO usarlo como sinónimo.** DLE lo da como sinónimo de obrador en España, pero el uso mexicano manda en México |
| El espacio de producción | **obrador** | **taller** · **laboratorio** (AR/UY/CL) · **planta de producción** | DLE `obrador`: «*Taller artesanal, especialmente el de confitería y repostería*» — https://dle.rae.es/obrador (2026-09-09). En España `obrador` tiene 9.900/mes; en MX/CO/AR/CL/PE `obrador de pasteleria` cae a 10/mes → **fuera de España la palabra apenas se usa** |
| Coste unitario de receta | **escandallo** | **costeo** · **costeo de recetas** | `escandallo pasteleria` sin dato en ES; `costeo de pasteles` sin dato en ningún mercado (§1.3) |
| Mueble de exposición | **vitrina** · **mostrador** | **exhibidor** · **vitrina exhibidora** | `vitrina de pasteleria` 50 (ES), `vitrina para pasteleria` 110 (MX) → **la preposición cambia por mercado**: «de» en España, «para» en LATAM |
| Pedido de cliente | **encargo** | **pedido** · **orden** (MX) | `tartas por encargo` 210 (ES); `pasteles por encargo` 10 (MX) |
| Producto | **tarta** | **pastel** (MX) · **torta** (AR/CO/CL/PE/UY) | ⚠️ **triple divergencia**: `tarta` en España, `pastel` en México, `torta` en el Cono Sur y los Andes (en México «torta» es un bocadillo). Es la palabra más peligrosa del producto |
| Bollería | **bollería** (4.400/mes ES) | **panadería dulce** · **facturas** (AR) · **pan dulce** (MX/CL) | `viennoiserie` 1.000/mes en ES: término técnico ya asentado en el sector profesional español |
| Maquinaria | **maquinaria** | **maquinaria** · **equipo** · **equipamiento** | `maquinaria pasteleria` 70 vs `maquinaria de pasteleria` 50 (ES); `maquinaria para pasteleria` es la forma de MX/CO/AR/CL/PE |
| Oficio de la persona | **pastelero/a** (1.900/mes ES) | **repostero/a** · **pastelero/a** | La página propia se llama `/usos/rol/repostero-pastelero` y cubre las dos |
| Modelo sin local propio | **obrador compartido** (50/mes ES) | **cocina compartida** · **cocina colaborativa** | `cocina compartida alquiler` sin dato en ES. SERP institucional (ACSA, Diputació de Barcelona) |
| Forma «artesanal» | **artesanal** (480) | **artesanal** | ⚠️ `artesana` sólo 260: usar **artesanal** como forma principal |

**Regla operativa para el producto:** España como base normativa y léxica, con la equivalencia entre paréntesis en la primera mención de cada término de la tabla. **La excepción es «dulcería»: no se usa como sinónimo en ningún idioma del producto**, porque en el mercado más grande de LATAM significa otra cosa.

---

## 5. Conclusión de negocio

### 5.1 Cuánto tráfico puede aportar el SEO: prácticamente nada, y ahora está medido

Tres mediciones independientes apuntan al mismo sitio:

1. **La demanda no existe.** Todo el clúster de intención de apertura de pastelería en España suma **~330 búsquedas/mes** repartidas en ~35 cadenas, 25 de ellas en 10/mes. Sumando los siete mercados hispanohablantes medidos, **no se llega a 500/mes**. La keyword que da nombre al producto, `como montar una pasteleria`, vale **10/mes en los siete mercados**.
2. **Lo que sí tiene volumen no es nuestro.** `pastelería` 110.000, `confitería` 9.900, `obrador` 9.900, `pastelería sin gluten` 2.400: las cuatro SERP están dominadas por **local pack de 12 resultados** y negocios locales. Es gente comprando una tarta.
3. **Los activos propios ya lo demuestran.** `/kit-tareas-pasteleria` está en **posición 4,6** y lleva **0 clics en 90 días**. `/guia-panaderia-obrador` —la hermana exacta— lleva **2 clics**, y GSC no puede nombrar ni una sola consulta que la traiga. **Toda la línea de guías de 65 € junta: 7 clics en 90 días.**

**Estimación honesta para la landing del producto: entre 0 y 5 clics/mes de SEO en el primer año, con 0-2 ventas atribuibles a búsqueda orgánica.** No se debe prometer más, ni construir el producto con esa expectativa. Es exactamente el mismo veredicto que dieron los tres productos anteriores del ciclo, y ahora está cuantificado con las landings ya publicadas en vez de por analogía.

### 5.2 Por qué la venta entra igualmente — y por dónde

- **El hub `/productos-digitales`** lleva anunciando el producto desde mayo. Literal, en `astro-site/src/components/pages/ProductosDigitalesHubPage.astro:957` y `src/pages/ProductosDigitales.tsx:942`: `{ name: 'Cómo Montar una Pastelería', desc: 'Guía paso a paso: obrador, vitrina, maquinaria, proveedores, licencias y lanzamiento.', phase: 'Mayo 2026' }`. **Hay una expectativa creada con cuatro meses de retraso visible.**
- **La lista de compradores en Resend**, con la regla de un broadcast por producto nuevo (cola de 5 días). Es el canal que ha vendido los tres anteriores.
- **La plataforma**: los agentes «Pastelero Consultor Pro», «Pastelería Creativa» y «Hotel Pastry & Bakery Pro» tienen usuarios que ya pagan y que son exactamente el público.
- **Los banners de producto en el corpus del blog**: 325 posts ES con 3 banners cada uno y rotación por todo el catálogo. Un producto nuevo entra automáticamente en esa rotación.
- **Venta cruzada con el hermano `guia-panaderia-obrador`** (65 €) y con `kit-tareas-pasteleria` (12 €), que comparten comprador.

### 5.3 Las piezas de CAPTACIÓN de blog que SÍ tienen demanda

Cuatro, y las cuatro salen del mismo clúster: **el obrador en casa y el miedo legal.** Son las únicas SERP del nicho sin local pack, con AI Overview y con PAA de apertura.

| # | Pieza propuesta | Keywords y volumen ES | Por qué |
|---|---|---|---|
| **1** | **El obrador compartido: cómo abrir una pastelería sin montar obrador propio** | `obrador compartido` **50**; `cocina compartida alquiler` sin dato | **El hueco más limpio.** SERP 100 % institucional (ACSA/Gencat, Diputació de Barcelona, grupos LEADER). **Cero piezas comerciales.** Y encaja como capítulo del producto (vía de entrada con CAPEX mínimo) |
| **2** | **¿Es legal vender repostería desde casa en España? Requisitos, licencia y multas** | `requisitos para montar un obrador en casa` **30** + `requisitos obrador pasteleria` **30** + `montar una pasteleria en casa` **20** + `vender reposteria desde casa españa` **20** + `vender tartas desde casa` **20** ≈ **120/mes agregado** | El clúster mejor definido. PAA listo: «¿Es legal…?», «¿Cuál es la multa por vender comida sin permiso en España?», «¿Qué requisitos necesito…?». ⚠️ Compite con **`pasteleriaparatodos.com` (Tamara Viñas), que vende una formación de pago y ocupa la pos. 1**, y con `escueladeobradores.com`. No es un hueco vacío: es un hueco disputado por productos, no por medios |
| **3** | **Cuánto cuesta montar una pastelería en España: desglose real** | `cuanto cuesta montar una pasteleria` **10** + `presupuesto para montar una pasteleria` **10** + `coste montar pasteleria` **10** + PAA de `cafeteria pasteleria` («¿Cuánto cuesta montar una cafetería pastelería?») y de `franquicias de pasteleria` («¿Cuánto dinero se necesita para abrir una pastelería?») | Volumen ridículo, **pero es la pregunta que Google inyecta como PAA en SERP de 2.900 y 40/mes**. Captación baja, conversión altísima: quien busca esto compra |
| **4** | **Franquicia de pastelería vs. marca propia: qué te dan y qué te quitan** | `franquicias de pasteleria` **40** + `franquicia pasteleria` **40** | Intención comercial confirmada. ⚠️ **SERP de directorios verticales con años de autoridad** (`mundofranquicia`, `franquicias.es`, `100franquicias`). Rankear es improbable; el valor es de **contenido de decisión** para quien ya nos lee |

**Y una anti-recomendación, que es el hallazgo más caro de esta lente:**
> ❌ **NO escribir «Pastelería sin gluten» (2.400/mes) ni «Cafetería pastelería» (2.900/mes) ni «Confitería» (9.900/mes) como piezas de captación.** Los tres volúmenes son de consumidor comprando producto, con SERP de 12 resultados de local pack. Quien mire la hoja de volúmenes sin abrir la SERP los propondrá, y traerían visitas que jamás compran una guía de 65 €.

### 5.4 Nombre y slug recomendados

**Slug: `guia-pasteleria-obrador`.**

| Opción | A favor | En contra | Veredicto |
|---|---|---|---|
| **`guia-pasteleria-obrador`** | Calca exactamente el patrón del hermano `guia-panaderia-obrador`, verificado en `src/data/products-catalog.ts:247` y en `astro-site/src/pages/guia-panaderia-obrador.astro`. Incluye «obrador», que en España tiene 9.900/mes de reconocimiento de marca-categoría y es la palabra que usa el propio anuncio del hub. Robots ya cubierto: `Disallow: /guia-*-access` y `/guia-*-library` (`astro-site/public/robots.txt:35-36`) — **los gates `guia-pasteleria-obrador-access` y `-library` quedan protegidos sin tocar el fichero** | Ninguno detectado | ✅ **Recomendado** |
| `guia-pasteleria` | Más corto | **Rompe el paralelismo con el hermano** y pierde «obrador», que es lo que distingue este producto de un curso de repostería. Además el catálogo tiene `kit-tareas-pasteleria`: dos slugs casi homónimos de productos distintos invitan al error que ya costó el enlace roto del hub de librerías | ❌ |
| `guia-como-montar-pasteleria` | Contiene la keyword literal del nombre anunciado | La keyword vale **10/mes**: no compra nada. Rompe el patrón de los 9 slugs `guia-*` existentes, todos `guia-<tipo de negocio>`. Y es el más largo de la línea | ❌ |

**Nombre comercial: «Guía Pastelería con Obrador».**
Calca la ficha del hermano en `src/data/products-catalog.ts:251` — `name: { es: 'Guía Panadería con Obrador', en: 'Guide: Bakery with Production Room' }`. Inglés propuesto: **«Guide: Pastry Shop with Production Room»** (coherente con la traducción ya establecida de «obrador»).

⚠️ **Pero el hub anuncia «Cómo Montar una Pastelería» desde mayo.** Recomendación: **mantener «Cómo Montar una Pastelería» como titular de la landing y del H1** (es la promesa hecha, y es la línea entera: «guías Cómo Montar»), y usar **«Guía Pastelería con Obrador»** como `name` del catálogo, del banner y del email — que es donde tiene que coincidir con el hermano. Al publicar, **la entrada «Próximamente · Mayo 2026» del hub hay que sustituirla por el producto real en LOS DOS ficheros** (`src/pages/ProductosDigitales.tsx:942` y `ProductosDigitalesHubPage.astro:957`), o el hub seguirá anunciando como futuro algo que ya está a la venta.

**Precio sugerido: 65 €**, alineado con `guia-panaderia-obrador` y con las 7 guías de restaurante. No hay nada en esta lente que justifique separarse de la escalera. *(La decisión de precio no es de L2; se apunta por coherencia.)*

---

## 6. Preguntas abiertas para John

1. El hub anuncia «Cómo Montar una Pastelería» desde mayo. **¿Titular «Cómo Montar una Pastelería» + nombre de catálogo «Guía Pastelería con Obrador»** (mi recomendación), o unificamos los dos en uno solo?
2. **¿Cubrimos «obrador en casa» y «obrador compartido» como capítulos del producto?** Son las dos únicas SERP con intención pura del nicho y las dos vías de entrada con CAPEX bajo, pero se salen del molde «obrador propio + tienda» del hermano de panadería.
3. `pasteleriaparatodos.com` (Tamara Viñas, Le Cordon Bleu Madrid) **vende una formación de pago de 7 módulos con plantillas y soporte**, y ocupa la posición 1 de «montar una pasteleria en casa». ¿Se le entra de frente en la pieza de captación nº 2, o se elige el hueco limpio del obrador compartido (nº 1)?
4. **¿Sigue en pie que la pieza de captación NO se mide por tráfico?** Con 30-50 búsquedas/mes, ninguna de las cuatro va a mover el contador; su valor es alimentar al comprador que ya está dentro.
5. **¿Extiendo la lente al AI Overview?** Cuatro SERP lo tienen y DataForSEO no me devolvió el texto: hace falta el endpoint asíncrono (coste extra) o mirarlo a mano. Es lo único de este encargo que queda a medias.
6. **La palabra «tarta».** En México es «pastel» y en el Cono Sur «torta». Si el producto se lee en toda la hispanofonía, ¿nota de equivalencia en la primera mención, o glosario al final?
