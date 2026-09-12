# LENTE 2 — SERP, demanda, vocabulario e intención

**Producto:** «Cómo Montar una Chocolatería» — guía premium de apertura, producto nuevo nº 5 del ciclo de sesiones alternadas; sería el **producto 49** del catálogo (hoy 48, contados en `src/data/products-catalog.ts` y `netlify/shared/payment-links.ts` el 2026-09-12).
**Fecha de la investigación:** **2026-09-12** (CEST). Todas las llamadas a DataForSEO y a GSC se lanzaron ese día.
**Autor:** lente L2 (research), sesión Claude Code.
**Alcance:** demanda, SERP, intención, vocabulario y conclusión de negocio. **No contiene contenido de producto**: ni capítulos, ni prosa vendible, ni cifras de CAPEX.

---

## 0. Método y limitaciones DECLARADAS

### Método

| Paso | Herramienta | Alcance real |
|---|---|---|
| Volumen de búsqueda | `/usr/bin/python3 scripts/dataforseo.py vol` → DataForSEO *keywords_data/google_ads/search_volume/live* | **115 keywords únicas en España** (5 tandas) + **16 keywords × 6 mercados** (MX 2484, CO 2170, AR 2032, CL 2152, PE 2604, EE. UU. en español 2840) = **211 mediciones**. De ellas, **más de 90 son keywords nuevas** que no estaban en las 25 del encargo |
| SERP orgánica en vivo | `scripts/dataforseo.py serp` → DataForSEO *serp/google/organic/live/advanced*, desktop, depth 20, PAA click depth 2 | **12 consultas en España** + **1 en México** (`dulceria`, para validar la trampa de vocabulario) |
| Datos propios | MCP `gscServer`, propiedad `sc-domain:aichef.pro`, ventana **2026-06-14 → 2026-09-12** (90 días, `data_state` por defecto) | 9 consultas: por *query* (chocolat / bombon / cacao / churr), por *page* (chocolat, chocolatero, kit-tareas-chocolateria, kit-tareas-, libreria-de-prompts-para-chocolat, aichef.pro/guia-) |
| Estado normativo del EUDR | WebSearch + WebFetch | 2 fuentes secundarias concordantes; **no abrí el texto primario del DOUE** (§7.3) |
| Nomenclatura y activos propios | lectura directa del repo | `src/pages/ProductosDigitales.tsx:958-960`, `astro-site/src/components/pages/ProductosDigitalesHubPage.astro:973-975`, `astro-site/public/robots.txt:35-36`, `astro-site/src/data/productos/guias/` |

Ficheros crudos (temporales de sesión, no versionados):
`/private/tmp/claude-501/-Users-johnguerrero-chefpro-modernize/b8385907-727b-45e2-b995-1140eaab1258/scratchpad/vol_*.txt` y `serp_*.txt`.

### Lo que NO he podido verificar, y por qué

1. **El texto de los AI Overviews.** Dos de las trece SERP traen AI Overview (`montar una chocolateria` y `precio del cacao`), pero DataForSEO lo devuelve como `"asynchronous_ai_overview": true` con `"markdown": null`, `"items": null` y `"references": null`. **Sé que el bloque existe y en qué consultas; no puedo citar su contenido ni qué fuentes cita.** Haría falta el endpoint asíncrono de AIO (coste extra) o mirar la SERP a mano. Es exactamente la misma limitación que declaró la L2 de Pastelería: **sigue abierta**.
2. **Las cifras de la crisis del cacao 2024-2026 (ICCO) y el efecto en el precio de las coberturas.** El encargo las trae como tema a cubrir. **No las he medido ni abierto en esta lente**: quedan **«sin fuente»** y son trabajo de la lente de datos (L3). Lo único que aporto aquí es la **demanda de búsqueda** de ese tema (§1.5), que sí está medida.
3. **Las cifras de CAPEX, precios de atemperadoras, vitrinas o cámaras de chocolate.** Igual: **«sin fuente»** en esta lente. Aquí sólo hay volúmenes de búsqueda de esas consultas, no precios.
4. **El error del «carnet de manipulador» de `plandenegocio.es`** que el encargo cita: he confirmado que la URL rankea (pos. 4 orgánica en `montar una chocolateria`, §2.4) pero **no he abierto la página para verificar la frase**. Es trabajo de L1 (competencia) y de L3 (normativa).
5. **DataForSEO devuelve `None` (no `0`) cuando Google Ads no sirve dato.** `None` ≠ «cero búsquedas». En las tablas lo escribo `—`. **No he convertido ni una sola en cero.** Hay dos casos distintos y los distingo: `—` (sin dato) y `0` (Google Ads devuelve cero explícito, p. ej. `plan de negocio chocolateria` en ES y en EE. UU.).
6. **No he medido competencia** (autoridad de dominio, backlinks, antigüedad de quien rankea). Eso es la lente L1. La columna `COMP` de las tablas es **competencia publicitaria de Google Ads, no dificultad SEO** — confundirlas es un error clásico.
7. **Ventana GSC de 90 días con `data_state` = «all»**: los últimos 2-3 días pueden moverse.
8. **No he medido el blog EN ni los blogs FR/DE/IT/PT.** Este producto es ES.

---

## 1. Demanda medida

> Fuente de toda esta sección: **DataForSEO, `keywords_data/google_ads/search_volume/live`, vía `scripts/dataforseo.py`, consultado el 2026-09-12**. Volumen = media mensual de Google Ads. La serie de 6 meses es la que devuelve el propio endpoint.

### 1.0 Primera trampa: la grafía SÍ mueve el dato aquí, y de dos maneras distintas

La L2 de Pastelería concluyó que **los acentos no son una variante de grafía** (`pastelería` = `pasteleria` = 110.000). **En chocolatería eso se cumple… salvo en la cola larga**, donde encontré un caso que rompe la regla. Medido el 2026-09-12, **las cuatro cadenas en la MISMA llamada** para descartar un artefacto de tanda:

| Par medido junto | Volumen | Lectura |
|---|---|---|
| `chocolateria artesanal` / `chocolatería artesanal` | **390 / 390** | idénticos → Google Ads normaliza diacríticos |
| `bomboneria artesanal` / `bombonería artesanal` | **10 / —** | **NO idénticos**: la forma acentuada devuelve *sin dato* |

**Conclusión operativa:** por encima de ~100 búsquedas/mes los diacríticos se normalizan y da igual cómo se escriba; **por debajo de ~50, la forma acentuada puede caer por debajo del umbral de Google Ads y devolver `—`**. Nunca concluir «esa variante no se busca» a partir de una cadena acentuada de cola larga: **medir siempre la forma sin tilde también**. (Esto explicaría, sin afirmarlo, parte de los `—` del encargo: `abrir una chocolateria` y `cuanto cuesta montar una chocolateria` no dan dato en ningún mercado de los 7 medidos.)

Y la trampa de PALABRA (la del `chile`/`chili crisp`) **sí se reproduce, y con factores grandes**:

| Variante | Vol/mes (ES) | Factor |
|---|---|---|
| `chocolateria artesanal` | **390** | — |
| `chocolateria artesana` | **—** (sin dato) | se cae del mapa |
| `chocolates artesanos` | **390** | ×1,00 |
| `cobertura de chocolate` / `chocolate de cobertura` | **2.400 / 2.400** | idénticos (Google Ads los agrupa) |
| `cacao precio` / `precio del cacao` | **1.300 / 1.300** | idénticos |
| `templado de chocolate` | **20** | — |
| `temperado de chocolate` | **10** | ×0,50 |
| `catas de chocolate` / `cata de chocolate` | **170 / 170** | idénticos |
| `obrador chocolate` | **10** | — |
| `obrador de chocolate` | (medido en la tanda 4 del encargo: **10**) | igual |

**Dos recomendaciones de copy que salen de aquí:**
- **«artesanal», nunca «artesana»** como forma principal (mismo patrón que en Pastelería: `artesanal` 480 vs `artesana` 260). En chocolate la diferencia es aún más brutal: 390 vs sin dato.
- **«templado» (20) por delante de «temperado» (10)** — el doble. El nombre anunciado en el hub dice «**Temperado**» (`ProductosDigitales.tsx:959`). Es la forma minoritaria. No es grave (son cifras ínfimas y el término técnico correcto es discutible en el gremio), pero **si hay que elegir una sola para los titulares, «templado»**.

### 1.1 España — el bloque de VOLUMEN ALTO, y por qué casi nada es nuestro

| Keyword | Vol/mes | COMP | Intención real (verificada en §2 donde hay SERP) |
|---|---|---|---|
| `churreria` | **110.000** | LOW | **Local puro** (consumidor buscando churrería cerca) |
| `chocolate valor` | **60.500** | LOW | **Marca / consumidor** |
| `chocolateria` | **9.900** | LOW | **Local + churros** — SERP con **12 bloques de local pack** (§2.2) |
| `praline` | **8.100** | LOW | Producto / definición / consumidor |
| `trufas de chocolate` | **6.600** | MEDIUM | **Recetas** |
| `chocolate con churros` | **5.400** | LOW | Local / consumidor |
| `escandallo` | **5.400** | LOW | **Transversal** — ya es nuestro terreno (Kit Escandallos, Guía Food Cost) |
| `appcc` | **4.400** | LOW | Transversal |
| `chocolate a la taza` | **4.400** (del encargo) | — | **RECETA** — SERP con bloque `recipes` (§2.6) |
| `chocolatina` | **2.900** | HIGH | Consumidor |
| `cobertura de chocolate` | **2.400** | HIGH | Compra de materia prima / recetas |
| `eudr` | **1.900** | MEDIUM | **Normativa — sí es nuestro terreno** (§1.5) |
| `valrhona` | **1.600** | HIGH | Marca / compra |
| `precio del cacao` | **1.300** | LOW | **Cotización — AI Overview, sin local pack** (§2.7) |
| `chocolate sin azucar` | **1.000** | HIGH | Consumidor |
| `bomboneria` | **880** (encargo) | LOW | **Local puro** — 12 bloques de local pack (§2.3) |
| `callebaut` | **880** | HIGH | Marca / compra |
| `licencia de apertura` | **720** | LOW | **Transversal de apertura — sí es nuestro** |

**Lectura:** de los ~18 términos por encima de 700 búsquedas/mes en este nicho, **sólo tres apuntan a nuestro comprador** (`escandallo`, `eudr`, `licencia de apertura`) y **los tres son transversales**: no son de chocolatería, son de apertura y gestión, y **dos de ellos ya los cubren productos nuestros**.

### 1.2 España — el núcleo semántico del producto (lo que de verdad describe la guía)

| Keyword | Vol/mes | COMP |
|---|---|---|
| `chocolateria artesanal` | **390** | HIGH |
| `chocolates artesanos` | **390** | HIGH |
| `bombones personalizados` | **390** | HIGH |
| `chocolate artesanal` | 390 (encargo) | — |
| `bean to bar` | 320 (encargo) | — |
| `taller de chocolate` | **210** | MEDIUM |
| `cata de chocolate` / `catas de chocolate` | **170 / 170** | HIGH |
| `chocolate ecologico` | **110** | HIGH |
| `chocolateria online` | **110** | HIGH |
| `moldes de bombones` | **70** | HIGH |
| `tienda de bombones` | **70** | MEDIUM |
| `proveedores de chocolate` | **30** | MEDIUM |
| `templado de chocolate` | **20** | LOW |
| `maquinaria para chocolate` | **20** | HIGH |
| `bean to bar españa` | **20** | MEDIUM |
| `obrador chocolate` | **10** | LOW |
| `camara de chocolate` | **10** | LOW |
| `atemperadora de chocolate precio` | **10** | — |
| `vitrina chocolate` | **10** | MEDIUM |
| `chocolateria boutique` | **10** | LOW |
| `chocolateria cafeteria` | **10** | LOW |
| `chocolate de autor` | **10** | HIGH |
| `bomboneria artesanal` | **10** | LOW |
| `tableta de chocolate artesanal` | **10** | MEDIUM |
| `bombones para eventos` | **10** | HIGH |
| `distribuidor de chocolate` | **10** | MEDIUM |
| `proveedores de cobertura de chocolate` | **10** | — |
| `venta de chocolate online` | **10** | HIGH |
| `tienda online de chocolate` | **10** | HIGH |
| `curso bomboneria` | **10** | HIGH |
| `franquicia valor precio` | **10** | LOW |
| **Sin dato (`—`)** | `obrador de bombones` · `obrador de chocolate artesanal` · `chocolateria artesana` · `fabrica de chocolate pequeña` · `taller de chocolate negocio` · `vender bombones online` · `vender chocolate desde casa` · `licencia chocolateria` · `registro sanitario chocolate` · `atemperadora precio` · `vitrina refrigerada chocolate` · `regalo corporativo chocolate` · `chocolate personalizado empresas` · `chocolate bean to bar españa` · `montar una chocolateria churreria` · `mercado del chocolate españa` · `vida util bombones` · `seguridad alimentaria chocolate` | | |

**Lectura dura:** el vocabulario propio del obrador de chocolate — atemperadora, cámara de chocolate, vitrina, proveedores de cobertura, obrador de bombones — **vive entre 10 y 0 búsquedas/mes en España**. Es exactamente el mismo perfil que tenía la Guía de Pastelería antes de venderse. **El producto describe un oficio que casi nadie teclea en Google.**

### 1.3 España — la intención de APERTURA: el bloque entero es humo estadístico

| Keyword | Vol/mes | COMP |
|---|---|---|
| `montar una cafeteria` (referencia) | **50** | LOW |
| `abrir una cafeteria` (referencia) | **30** | MEDIUM |
| `montar una panaderia` (referencia) | **30** | LOW |
| `montar una pasteleria` (referencia) | **20** | LOW |
| `montar chocolateria` | **10** | LOW |
| `negocio de chocolates` | **10** | LOW |
| `como montar una chocolateria` | 10 (encargo) | — |
| `montar una chocolateria` | 10 (encargo) | — |
| `estudio de mercado chocolate` | **10** | — |
| `consumo de chocolate en españa` | **10** | LOW |
| `plan de negocio chocolateria` | **0** (cero explícito) | — |
| `como abrir una chocolateria` | **—** | — |
| `abrir chocolateria` | **—** | — |
| `emprender con chocolate` | **—** | — |
| `rentabilidad chocolateria` | **—** | — |
| `chocolateria negocio rentable` | **—** | — |
| `cuanto cuesta abrir una chocolateria` | **—** | — |
| `inversion chocolateria` | **—** | — |
| `plan de empresa chocolateria` | **—** | — |

**Este es el dato más importante del informe para calibrar expectativas, y hay que leerlo con la referencia al lado:** `montar una pasteleria` son **20/mes** y `montar una panaderia` **30/mes** — y los dos productos hermanos (65 €) **ya están vendidos y publicados**. La demanda de apertura de chocolatería (10/mes) es **la mitad que la de pastelería**, que a su vez es despreciable. **Nadie ha decidido nunca lanzar estos productos por el volumen de la keyword de apertura, y no debe hacerse ahora tampoco.** El argumento de venta es otro (§6).

### 1.4 Estacionalidad: medida, no supuesta — y es la más extrema que he visto en el grupo

El endpoint devuelve la serie mensual. Dos hallazgos:

| Keyword | Media | Serie de los 6 meses devueltos | Factor pico/valle |
|---|---|---|---|
| `mona de pascua` / `monas de pascua` | **18.100** | `1.600 · 1.600 · 1.900 · 2.900 · 110.000 · 90.500` | **×69** |
| `churreria` | **110.000** | `110.000 · 74.000 · 60.500 · 74.000 · 74.000 · 90.500` | ×1,8 |
| `bombones san valentin` | **320** | `10 · 10 · 10 · 20 · 20 · 30` | la media (320) la hace un pico **fuera** de la ventana devuelta |
| `chocolateria` | 9.900 (encargo: `6.600→8.100` en 6 meses) | — | ×1,2 en la ventana medida |
| `trufas de chocolate` | **6.600** | `3.600 · 2.900 · 2.900 · 3.600 · 4.400 · 5.400` | ×1,9 y subiendo |
| `cobertura de chocolate` | **2.400** | `1.300 · 1.000 · 1.300 · 1.900 · 2.900 · 2.900` | ×2,9 y subiendo |

**Tres lecciones:**
1. **La media miente en un negocio estacional.** `mona de pascua` tiene media 18.100 y valle 1.600: quien planifique tesorería con la media se arruina. El producto tiene que enseñar el perfil, no el promedio — y **la estacionalidad de la chocolatería es medible, no una opinión**.
2. **`bombones san valentin` (320 de media, 10-30 en la ventana devuelta) demuestra el caso inverso**: una media alta sostenida por un pico que ni siquiera aparece en los 6 meses que devuelve la API. **Nunca citar una media de estos términos sin la serie.**
3. `trufas de chocolate` y `cobertura de chocolate` están **subiendo mes a mes** en la ventana medida (marzo→agosto): es la rampa hacia el otoño-Navidad. Confirma con dato propio el argumento de la campaña.

### 1.5 El ángulo normativo: el ÚNICO con volumen real y sin dueño

| Keyword | Vol/mes | COMP | Nota |
|---|---|---|---|
| `eudr` | **1.900** | MEDIUM | Serie: `480 · 880 · 1.000 · 1.300 · 1.000 · 880` — **creció ×2 en el semestre** |
| `licencia de apertura` | **720** | LOW | Serie `170 · 260 · 320 · 480 · 480 · 590` — subiendo |
| `fat bloom` | **140** | LOW | Defecto técnico del chocolate |
| `sugar bloom` | **90** | LOW | Idem |
| `registro sanitario alimentos` | **90** | LOW | |
| `reglamento deforestacion` | **50** | LOW | Hermana en español de `eudr` |
| `etiquetado chocolate` | **40** | LOW | |
| `rd 1055 2003` | **10** | LOW | El RD del cacao y el chocolate |
| `cadmio en el chocolate` | **10** | LOW | |
| `conservacion del chocolate` | **10** | LOW | |
| `crisis del cacao` | **20** | LOW | |
| `real decreto chocolate` · `manipulador de alimentos chocolate` | **—** | — | |

**Estado real del EUDR a 2026-09-12** (verificado, ver §7.3 para la limitación): el Reglamento (UE) 2023/1115 **incluye el cacao** entre sus siete materias primas y **ha sido aplazado por segunda vez**. El **Reglamento (UE) 2025/2650, de 19 de diciembre de 2025**, retrasa la aplicación al **30 de diciembre de 2026 para grandes y medianas empresas** y al **30 de junio de 2027 para micro y pequeñas empresas** como operadores.
Fuentes consultadas el **2026-09-12**: <https://www.taric.es/noticias/2026-01-02-retraso-en-aplicacion-de-reglamento-eudr-hasta-el-30-12-2026/> y <https://actualidad.aidimme.es/2025/12/18/la-ue-aprueba-un-nuevo-aplazamiento-del-reglamento-eudr-por-un-ano-alivia-la-gestion-y-otorga-a-las-pyme-6-meses-mas-de-gracia/>.

**Por qué esto importa a esta lente:** `eudr` es la **única keyword de 4 cifras del nicho cuya intención es informativa-profesional y no local ni de consumidor** (1.900/mes, creciendo, competencia publicitaria MEDIUM). Es el mejor candidato a pieza de captación que ha salido de toda la medición (§6.2). Y **la fecha importa**: una chocolatería que abra en 2026 cae en el tramo de micro/pequeña empresa → **30 de junio de 2027**. Publicar «entra en vigor en 2025» sería un error caro.

---

## 2. SERP directa: qué es «chocolatería» para el buscador español

> Fuente: **DataForSEO `serp/google/organic/live/advanced`, desktop, depth 20, PAA click depth 2, España (2724) / español**, consultado el **2026-09-12**. México (2484) en la última fila.

### 2.1 Tabla de bloques — y la validación del filtro de intención

| Consulta | AI Overview | Local pack | Otros bloques | Veredicto |
|---|---|---|---|---|
| `chocolateria` | no | **12** | compare_sites, PAA, images | **NO es nuestra** |
| `bomboneria` | no | **12** | knowledge_graph, compare_sites, PAA | **NO es nuestra** |
| `chocolateria artesanal` | no | **12** | compare_sites, popular_products (7), PAA | **NO es nuestra** |
| `chocolateria churreria` | no | **12** | compare_sites, video, PAA | **NO es nuestra** |
| `chocolate artesanal` | no | **9** | popular_products (6), google_reviews (2), video | **NO es nuestra** |
| `bean to bar` | no | **6** | knowledge_graph, PAA | **NO es nuestra** |
| `taller de chocolate` | no | **3** | compare_sites, PAA | **NO es nuestra** |
| `bombones artesanales` | no | **2** | popular_products (8), images (2) | **NO es nuestra** |
| `obrador de chocolate` | no | 0 | **knowledge_graph + google_reviews** | **NO es nuestra** (ficha de negocio local sin local pack) |
| `chocolate a la taza` | no | 0 | **recipes**, popular_products (3), video, knowledge_graph | **NO es nuestra** (receta) |
| **`montar una chocolateria`** | **SÍ** | **0** | video, PAA, related | **SÍ es nuestra** |
| **`precio del cacao`** | **SÍ** | **0** | images (2), PAA, related | **SÍ es nuestra** |
| `dulceria` (México) | no | 3 | PAA | NO es nuestra (§3.2) |

**El filtro heredado de Pastelería se valida 13/13**, pero hay que **ampliarlo con dos señales más**, porque dos consultas sin local pack tampoco son nuestras:

> **Filtro de intención v2 (validado sobre 13 SERP el 2026-09-12):**
> `local_pack` presente **→ no es nuestra** (8/8 casos).
> `recipes` presente **→ no es nuestra** (receta de consumidor: `chocolate a la taza`).
> `knowledge_graph` + `google_reviews` sin local pack **→ no es nuestra** (Google ya resolvió la consulta como un negocio concreto: `obrador de chocolate`).
> `ai_overview` presente **sin** local pack **→ sí es nuestra** (2/2 casos).
>
> El filtro de una sola señal (sólo local pack) habría clasificado mal 2 de 13 consultas. **Con la versión v2, cero errores.**

### 2.2 La pregunta decisiva: `chocolateria` en España es **chocolate a la taza con churros**, no bombonería

La SERP de `chocolateria` (9.900/mes) no deja lugar a dudas. **Los orgánicos 2, 4 y 5 son Chocolatería San Ginés** (la de los churros de Madrid) y el resto son tiendas y locales. Pero la prueba definitiva es el **People Also Ask**: de las 9 preguntas que devuelve Google, **5 son de churros**:

```
? ¿Qué es una chocolatería?
? ¿Cuáles son las 10 mejores marcas de chocolate?
? ¿Quién es el mejor chocolatero de España?
? ¿Cuál es la churrería más famosa de Madrid?      ← churros
? ¿Cuáles son las 10 mejores churrerías de España? ← churros
? ¿Cuántos churros son 5 euros?                    ← churros
? ¿Cuántos churros se recomienda por persona?      ← churros
? ¿Es rentable vender churros?                     ← churros
? ¿Cuántas calorías tienen 2 churros?              ← churros
```

**Google, al oír «chocolatería» en España, entiende «sitio donde te tomas un chocolate con churros».** Y el volumen lo respalda: `churreria` **110.000/mes**, `chocolate con churros` **5.400/mes**, `chocolateria churreria` 1.000/mes — frente a `bomboneria` 880 y `chocolateria artesanal` 390. **El modelo (b) es entre 10 y 100 veces más buscado que el (a).**

La SERP de `chocolateria churreria` lo confirma: 12 bloques de local pack, y su PAA es íntegramente de churros y de Madrid (`¿Cuánto cuestan los churros en San Ginés?`). El único dato de negocio que asoma en todo el bloque es **`¿Es rentable vender churros?`**, que aparece en el PAA de `chocolateria`.

### 2.3 `bomboneria` (880/mes) es tienda de barrio, no oficio

12 bloques de local pack; relacionadas: `Bombonería Madrid · Bombonería Barcelona · Bomboneria cerca de mi · Bombonería Sevilla · Bombonería Pons · Bombonería pons horario · Bombonería Zaragoza · Mejores bombones Barcelona` — **siete de las ocho llevan ciudad o «cerca de mí»**. Su PAA es 100 % de consumidor (`¿Cuál es el bombón más rico?`, `¿Cuáles son los 5 chocolates más caros del mundo?`), con **una sola excepción aprovechable**: `¿Cuánto cuesta un kilo de bombones artesanales?` — que es una pregunta de **precio de venta**, y ésa sí interesa al que va a abrir.

### 2.4 `montar una chocolateria`: la única SERP de apertura, y está vacía de guías españolas serias

10 búsquedas/mes, pero es **la única con AI Overview y sin local pack**. Top 14 orgánico (consultado 2026-09-12):

| # | Resultado | Lectura |
|---|---|---|
| 1 | «7 cosas que necesita para abrir una chocolatería» — <https://maxima.com/es/blogs/maxima/todo-lo-necesario-para-abrir-una-chocolateria-en/> | **Fabricante de maquinaria** vendiendo equipo |
| 2 | «Franquicias Chocolaterías Valor» — <https://www.valor.es/franquicias/> | **Franquicia** — y es el modelo (b), chocolate a la taza |
| 3 | «3 razones por las que abrir una chocolateria es…» | contenido de marca |
| 4 | «Cómo abrir una chocolatería en España: requisitos» (plandenegocio.es) | **la única española de apertura** — el encargo señala que pide «carnet de manipulador», error clásico (**no verificado por L2**, §0.4) |
| 5 | «5 Tips para Abrir una Chocolatería Exitosa» | LATAM |
| 6-9 | contenido de marca / LATAM | |
| 10 | «How to start a chocolate business» | **en inglés** |
| 13 | «Cómo crear tu negocio de chocolatería: Paso a Paso **eBook**» | **hay alguien vendiendo un producto digital de esto** — competencia directa, para L1 |

**Las relacionadas delatan hacia dónde tira Google:** `Franquicia chocolatería · Franquicia chocolates valor precio · Valor chocolate · Chocolatería valor dénia · Valor chocolateria burgos · Chocolatería Valor Madrid Postigo…` — **7 de 8 son la franquicia Valor**. Es decir: **incluso en la consulta de apertura, Google entiende que quien quiere «montar una chocolatería» quiere abrir una Valor**, no un obrador de bombones.

**El PAA es el guion de FAQ más valioso de toda la medición**, y es mayoritariamente LATAM:
```
? ¿Cuánto dinero necesito para abrir una dulcería?     ← LATAM (§3.2)
? ¿Cuál es el chocolate que más se vende?
? ¿Qué porcentaje se le gana al dulce?                 ← MARGEN: pregunta de negocio real
? ¿Qué se necesita para hacer chocolatinas?
? ¿Cómo hacer chocolates artesanales?
? ¿Cuál es la materia prima del chocolate?
? ¿Cuáles son los 4 tipos de chocolate?
? ¿Cómo se hace un chocolate paso a paso?
? ¿Cuál es el circuito productivo del chocolate?
```
**Siete de las nueve son de PRODUCCIÓN, no de negocio.** Sólo `¿Qué porcentaje se le gana al dulce?` y `¿Cuánto dinero necesito…?` son del comprador de la guía. **Mensaje para el guion: quien busca esto en Google todavía no sabe que lo suyo es un problema de negocio; cree que es un problema de recetas.** Eso condiciona el copy de la landing, no el contenido del producto.

### 2.5 `bean to bar` (320/mes): comunidad y afición, con 6 bloques de local pack

Rankea la **Asociación Chocolate Bean to Bar España** (posiciones 2 y 7, con Instagram), obradores concretos (Bean To Bar Lleida, Chocolate Moro, Clo Raw Fila), un **artículo de definición de Gastronosfera del 26-mar-2026** (<https://www.gastronosfera.com/tendencias/chocolate-bean-bar-que-es-y-en-que-consiste>) y **100x100chef vendiendo formación** (<https://100x100chef.com/shop/es/246-chocolateria-bean-to-bar>). Relacionadas: `Bean to bar Barcelona · madrid · Valencia · España · extremadura` — **geográficas**. Su PAA es de consumidor puro (`¿Cuál es el chocolate número 1?`).

**Veredicto:** `bean to bar` es un **nicho con identidad y asociación propia** pero su búsqueda es de consumidor y de localización, no de apertura. **Como capítulo/variante del producto tiene sentido (hay gremio, hay asociación, hay vocabulario); como pieza de captación SEO, no.**

### 2.6 `chocolate a la taza` (4.400/mes): es una RECETA, no un negocio

Bloque `recipes` en la SERP. Top 7: recetasdecocina.elmundo.es, tienda.lacasa.es, chocolateslasuperlativa.es, **valor.es**, Simón Coll, Torras, un blog de recetas. Relacionadas: `Receta chocolate a la taza Valor · Como hacer chocolate a la taza espeso · Chocolate a la taza mercadona · Chocolate a la taza sin maicena · Chocolate a la taza Thermomix`. PAA: nueve preguntas y **las nueve son «cómo hacer»**.

**Veredicto:** 4.400 búsquedas/mes de **ama de casa con una tableta y un cazo**. Escribir una pieza de captación aquí produciría tráfico cero-cualificado. **Es el `qué es un token` de este nicho: el volumen está, la intención no.** Descartada como captación.

### 2.7 `precio del cacao` (1.300/mes): AI Overview, sin local pack — y la SERP es FINANCIERA

Top 8: Investing (futuros CCZ6), Expansion.com, IG, Yahoo Finance (CC=F), Datos Históricos. **Es una SERP de trading de materias primas, no de chocolatería.** PAA: `¿Qué precio tiene el cacao hoy?`, `¿Cuánto vale 1 kg de cacao?`, **`¿Cuál es la tendencia del cacao para 2026?`**, `¿Cuántos quintales de cacao son una tonelada?`.

**Veredicto matizado:** pasa el filtro v2 (AIO sin local pack) pero **el competidor es Investing y Yahoo Finance con datos en tiempo real**, y nosotros no publicamos cotizaciones. **No se puede competir por la keyword genérica.** Lo que sí es viable es la **cola larga de la pregunta del PAA**: `¿Cuánto vale 1 kg de cacao?` traducida a «**cuánto te cuesta un bombón cuando el cacao sube**», que es una pieza de coste, no de cotización. Ahí no hay nadie. (Y `¿Cuál es la tendencia del cacao para 2026?` es literalmente el guion de esa pieza.)

### 2.8 Guion de FAQ consolidado (People Also Ask de las 12 SERP españolas)

Preguntas **útiles para el comprador de la guía**, extraídas de los PAA medidos el 2026-09-12 (descarto las ~70 de consumidor tipo «¿cuál es el chocolate más rico?»):

| Pregunta (literal de Google) | De qué SERP sale | Para qué sirve |
|---|---|---|
| **¿Qué es una chocolatería?** | `chocolateria` | Define el alcance del producto en la primera página |
| **¿Es rentable vender churros?** | `chocolateria` | La pregunta del modelo (b) |
| **¿Cuánto cuesta un kilo de bombones artesanales?** | `bomboneria`, `bombones artesanales` | **Precio de venta** — núcleo del escandallo |
| **¿Qué porcentaje se le gana al dulce?** | `montar una chocolateria` | **Margen** — núcleo del escandallo |
| **¿Cuánto dinero necesito para abrir una dulcería?** | `montar una chocolateria` | **CAPEX** (con la advertencia de vocabulario §3.2) |
| **¿Qué tan rentable es un negocio de chocolates?** | `chocolateria artesanal` | Rentabilidad |
| **¿Cuánto cuesta un curso de chocolatería?** | `taller de chocolate` | **Línea de ingresos por talleres** — precio de mercado |
| **¿Qué tipo de chocolate se usa para los churros?** | `chocolateria churreria` | Materia prima del modelo (b) |
| **¿Cuál es la tendencia del cacao para 2026?** | `precio del cacao` | Crisis del cacao |
| **¿Cuánto vale 1 kg de cacao?** | `precio del cacao` + encargo | Coste de materia prima |
| **¿Cuáles son los 4 tipos de chocolate?** / **¿Cuáles son los 3 tipos de chocolate?** | `montar una chocolateria`, `bean to bar`, `taller de chocolate` | Aparece en **tres** SERP distintas: es la definición que Google espera |
| **¿Qué es el chocolate artesanal?** | `chocolate artesanal` | Definición legal (enlaza con el RD 1055/2003) |

⚠️ **Aviso de duplicación de FAQ**: `¿Cuáles son los 3 tipos de chocolate?` y `¿Cuáles son los 4 tipos de chocolate?` son **la misma pregunta con distinto número**, recogidas de SERP distintas. Es exactamente el caso que caza `fase8d-faq-duplicadas.py` (nivel DEFINICION). **Elegir una sola** — si el producto lleva `FAQPage`, las dos juntas producirían dos *rich results* redundantes.

---

## 3. LATAM y EE. UU. en español

> Fuente: DataForSEO, mismas keywords, `--pais <loc> --idioma es`, consultado el **2026-09-12**. `—` = sin dato, `0` = cero explícito.

### 3.1 Tabla por país (búsquedas/mes)

| Keyword | **ES** 2724 | **MX** 2484 | **CO** 2170 | **AR** 2032 | **CL** 2152 | **PE** 2604 | **US-es** 2840 |
|---|---|---|---|---|---|---|---|
| `dulceria` | 3.600¹ | **110.000** | **3.600** | 1.000 | 880 | 880 | **14.800** |
| `chocolateria` | 9.900¹ | 5.400 | 1.600 | **9.900** | 6.600 | 5.400 | 2.400 |
| `chocolateria artesanal` | 390 | **1.600** | 590 | 720 | 480 | 390 | 320 |
| `tienda de chocolate` | 320¹ | 390 | 140 | 90 | 480 | 140 | 480 |
| `curso de chocolateria` | 30¹ | **210** | 140 | 140 | 140 | 50 | 10 |
| `bean to bar` | 320¹ | 110 | 110 | 140 | 50 | 110 | 320 |
| `bomboneria` | 880¹ | 90 | 30 | **720** | 20 | 20 | 90 |
| `taller de chocolate` | 210 | 110 | 20 | 10 | 40 | 30 | 30 |
| `bombones artesanales` | 260¹ | 50 | 20 | **260** | 70 | 30 | 20 |
| `chocolate a la taza` | **4.400**¹ | 70 | 40 | 20 | 70 | 30 | 260 |
| `negocio de chocolates` | 10 | 10 | 10 | 10 | 10 | 10 | 10 |
| `como montar una chocolateria` | 10¹ | 10 | 10 | 10 | 10 | **0** | **0** |
| `montar una chocolateria` | 10¹ | 10 | 10 | **0** | 10 | **0** | **0** |
| `plan de negocio chocolateria` | **0** | 10 | 10 | 10 | 10 | 10 | **0** |
| `abrir una chocolateria` | — | — | — | — | — | — | — |
| `cuanto cuesta montar una chocolateria` | — | — | — | — | — | — | — |

¹ Dato de España que viene del encargo (medido el 2026-09-12 según el enunciado), no remedido por mí salvo donde indico lo contrario. `dulceria` en ES: valor tomado de la L2 de Pastelería (§1.1 de aquel informe, 2026-09-09) — **no lo he remedido**, marcado como dato heredado.

### 3.2 ⚠️ LA TRAMPA DE VOCABULARIO MÁS CARA DEL INFORME: «dulcería» NO es chocolatería

`dulceria` es el término de mayor volumen de toda la tabla LATAM (**110.000/mes en México**, 14.800 en EE. UU. en español) y **el PAA de `montar una chocolateria` en España pregunta literalmente «¿Cuánto dinero necesito para abrir una dulcería?»**. Es tentador usarlo como equivalencia LATAM de «chocolatería». **Sería un error grave.**

Lo verifiqué con una SERP en vivo en México (2484) el 2026-09-12. Top 10 orgánico:
```
 1. Superdulces - Dulcería en línea en México
 2. Azúcar Dulcerías - Dulces y botanas al MAYOREO. Todo para ...
 3. El Castillo del Dulce
 4. El Mundo de los Dulces
 5. Compra Dulces Online | Variedad de Caramelos, Chocolates ...
 7. Dulces Las Delicias
 9. Dulcería | Galletas, Chocolates, Gomitas y Caramelos
10. Dulces y Botanas
```
Y su PAA: `¿Cuáles son 20 dulces típicos mexicanos?` · `¿Cuáles son los 10 dulces más vendidos en México?` · `¿Cuál es la dulcería más barata en Monterrey?` · `¿Qué dulces son económicos pero ricos?`

**Una «dulcería» mexicana es una tienda de golosinas y botanas al mayoreo** —caramelos, gomitas, piñatas— **no un obrador de bombones**. Compartir la palabra con el chocolate es coincidencia de categoría, no equivalencia.

**Corroboración independiente:** la L2 de Pastelería ya midió `dulceria` por países el 2026-09-09 (`guia-pasteleria-research-L2-serp-demanda.md:144`) y obtuvo **exactamente las mismas cifras** que yo el 12-sep (MX 110.000 · CO 3.600 · AR 1.000 · CL 880 · PE 880 · US 14.800). Dos mediciones independientes con tres días de diferencia coinciden dígito a dígito: el dato es sólido. Lo que aquel informe no hizo —y sí he hecho aquí— es **abrir la SERP mexicana para ver qué vende una dulcería**.

> **Regla para la tabla de equivalencias del producto: `dulcería` NO entra como sinónimo de chocolatería/bombonería. Si se menciona, es para ACLARAR que en México designa otra cosa.**
> Y si alguna FAQ recoge la pregunta del PAA «¿Cuánto dinero necesito para abrir una dulcería?», **hay que reformularla**, porque tal cual responde a otro negocio.

### 3.3 Otras lecturas de la tabla LATAM

- **Argentina es el mercado hispanohablante donde nuestro modelo (a) está más vivo**: `bomboneria` **720** (frente a 90 en México y 30 en Colombia) y `bombones artesanales` **260**, empatado con España. La bombonería es una categoría real allí.
- **México es el mercado de la FORMACIÓN**: `curso de chocolateria` **210**, el más alto de los siete mercados, y `chocolateria artesanal` **1.600**, cuatro veces España. Vende cursos, no aperturas.
- **`chocolate a la taza` es un españolismo**: 4.400 en España contra 70 en México, 40 en Colombia, 20 en Argentina. **En EE. UU. en español sube a 260**, casi seguro por población de origen español/mexicano buscando el producto. **Confirma que el modelo (b) —chocolate a la taza con churros— es un fenómeno IBÉRICO** y no exportable al comprador hispanoamericano.
- **La intención de apertura es igual de nula en los siete mercados**: `montar una chocolateria` está en 10 o en 0 en todos, `abrir una chocolateria` y `cuanto cuesta montar una chocolateria` **no devuelven dato en ninguno de los siete**. No hay un mercado de rescate.
- **`bean to bar` es el término más homogéneo de la tabla** (320 ES · 320 US · 140 AR · 110 MX/CO/PE · 50 CL): es **vocabulario internacional**, no se traduce, y funciona igual en los siete mercados.

---

## 4. Datos propios (Google Search Console)

> Fuente: MCP `gscServer`, propiedad `sc-domain:aichef.pro`, **2026-06-14 → 2026-09-12** (90 días), `search_type` WEB. Consultado el 2026-09-12.

### 4.1 Consultas con «chocolat» — 24 impresiones, 0 clics, en 90 días

| Query | Página | Clics | Impr. | Pos. |
|---|---|---|---|---|
| `chocolatier school` | blog.aichef.pro/en/Top-10-chocolate-schools-in-the-United-States-2026/ | 0 | 6 | 87,3 |
| `chocolate ia` | aichef.pro/blog/chocolateria-artesanal-e-ia-una-combinacion-innovadora | 0 | 4 | **7,2** |
| `chocolate schools` | blog.aichef.pro/en/Top-10-chocolate-schools… | 0 | 4 | 96,0 |
| `ecole chocolat` | blog.aichef.pro/en/Top-10-chocolate-schools… | 0 | 4 | 62,2 |
| `chocolatier schools` | blog.aichef.pro/en/Top-10-chocolate-schools… | 0 | 3 | 43,0 |
| `chocolate school` | blog.aichef.pro/en/Top-10-chocolate-schools… | 0 | 2 | 85,5 |
| `chocolateiro` | aichef.pro/pt/casos-uso/consultoria/chocolateiro-consultor | 0 | 1 | 8,0 |
| **TOTAL** | | **0** | **24** | |

**Consultas con `bombon`: sin datos. Con `cacao`: sin datos. Con `churr`: sin datos.** Cero impresiones en 90 días para las tres.

Dos observaciones:
1. **19 de las 24 impresiones (79 %) son de un post INGLÉS del subdominio legacy `blog.aichef.pro`** sobre escuelas de chocolate en EE. UU., en posiciones 43-96. **Es exactamente la trampa que documenta `CLAUDE.md`**: leer «hay histórico de chocolate» sin mirar de qué URL cuelga llevaría a creer que existe un suelo. No lo hay: ese subdominio está 301-eado y el post no es ni español ni de apertura.
2. `chocolate ia` en **posición 7,2** con 4 impresiones y 0 clics: el post `chocolateria-artesanal-e-ia-una-combinacion-innovadora` rankea bien para una consulta que nadie busca.

### 4.2 Páginas propias del nicho

| Página | Clics | Impr. | Pos. |
|---|---|---|---|
| `/blog/libreria-de-prompts-para-chocolatero-consultor-pro-ai` | 0 | **47** | 7,8 |
| `/blog/libreria-de-prompts-para-chocolateria-creativa-ai` | 0 | 12 | 7,4 |
| `/kit-tareas-chocolateria` (12 €, v2.x, 11 xlsx) | **0** | **13** | **6,0** |
| `/blog/chocolateria-artesanal-e-ia-una-combinacion-innovadora` | 0 | 4 | 7,2 |
| `/pt/casos-uso/consultoria/chocolateiro-consultor` | 0 | 1 | 8,0 |
| `/usos/rol/chocolatero-bombonero` | **sin datos** | **sin datos** | — |
| (legacy `blog.aichef.pro/**` de librerías chocolate, 5 URLs) | 0 | 23 | 5,6-21,5 |

**El dato que manda:** `/kit-tareas-chocolateria` lleva meses publicado, está en **posición media 6,0**, y ha conseguido **13 impresiones y CERO clics en 90 días**. Un producto de 12 € en primera página que nadie ve. **Es el predictor más directo que existe de lo que hará una landing de chocolatería: el SEO de este nicho no trae compradores.**

⚠️ **Trampa de la herramienta, cazada en esta lente:** consultar `kit-tareas-chocolateria` con `dimensions=page,query` devuelve **«No search analytics data found»**; con `dimensions=page` devuelve **13 impresiones**. La diferencia son las *queries anonimizadas* de Google, que no aparecen en el desglose por consulta. **Ausencia en una consulta con dimensión `query` NO es ausencia de datos.** Es hermana de la trampa nº 3 del L2 de Pastelería (`get_search_by_page_query` vs `contains`). Fiarme del primer resultado me habría hecho escribir «la landing hermana no existe en Google», que es falso.

### 4.3 La línea `guia-*` entera: el predictor de facturación por SEO

| Página | Clics | Impr. | CTR | Pos. |
|---|---|---|---|---|
| `/guia-restaurante-peruano` | 3 | 118 | 2,54 % | 5,6 |
| `/guia-restaurante-mexicano` | 2 | 73 | 2,74 % | 9,4 |
| **`/guia-panaderia-obrador`** | **2** | **39** | **5,13 %** | **7,3** |
| `/guia-restaurante-japones` | 1 | 64 | 1,56 % | 7,9 |
| `/guia-restaurante-gastronomico` | 0 | 51+1 | 0 % | 13,7 |
| `/guia-restaurante-casual` | 0 | 46 | 0 % | 9,0 |
| `/guia-food-cost-ingenieria-menu` | 0 | 11 | 0 % | 6,9 |
| `/guia-restaurante-nikkei` | 0 | 11 | 0 % | 5,5 |
| `/guia-dark-kitchen` | 0 | 4 | 0 % | 39,2 |
| (legacy blog) | 0 | 1 | 0 % | 9,0 |
| **TOTAL LÍNEA** | **8** | **419** | **1,91 %** | — |

**8 clics en 90 días para las 10 landings de guías juntas.** (La L2 de Pastelería midió 7/386 el 09-sep; tres días después son 8/419: la línea crece a razón de ~1 clic cada tres días **para todo el conjunto**.)

⚠️ **`/guia-pasteleria-obrador` no aparece**: se publicó el 2026-09-10, hace dos días. **Ausencia esperada, no un fallo** — Google aún no la ha indexado. No confundirlo con «no funciona».

**Predicción honesta para `guia-chocolateria`, basada en la hermana directa:** `/guia-panaderia-obrador` (mismo molde, mismo precio, publicada antes) hace **2 clics / 39 impresiones / 90 días**. Como la demanda de apertura de chocolatería es **la mitad** que la de panadería (`montar una chocolateria` 10 vs `montar una panaderia` 30), **el escenario razonable para la nueva landing es 0-2 clics orgánicos cada 90 días**. Es decir: **cero ventas por SEO**, y hay que decirlo así.

---

## 5. Vocabulario: España vs LATAM, para la primera mención

Tabla de equivalencias construida sobre (a) los volúmenes medidos por país en §3.1, (b) el vocabulario que aparece en los títulos y descripciones de los orgánicos de las 13 SERP, y (c) las búsquedas relacionadas. **Donde no tengo medición que respalde una equivalencia, lo digo.**

| Concepto | **España (forma principal)** | LATAM / equivalencia para la primera mención | Evidencia |
|---|---|---|---|
| El negocio (modelo a) | **chocolatería artesanal** · bombonería | **chocolatería artesanal** funciona igual en los 7 mercados (MX 1.600, AR 720, CO 590, CL 480, PE 390, US 320). **`bombonería` sólo es fuerte en ARGENTINA (720)**; en MX/CO/CL/PE está entre 90 y 20 | §3.1 |
| ⚠️ Falso amigo | — | **`dulcería` NO vale**: en México (110.000/mes) es tienda de golosinas y botanas al mayoreo | §3.2, SERP MX |
| El negocio (modelo b) | **chocolatería (de taza) y churrería** | **No exportable**: `chocolate a la taza` 4.400 en ES vs 20-70 en LATAM | §3.3 |
| El local de producción | **obrador** (`obrador chocolate` 10; `obrador` 9.900 en el L2 de Pastelería) | **taller** · **laboratorio** (uso profesional) — **sin medición propia de estas dos formas en LATAM: propuesta, no dato** | parcial |
| El cálculo de coste | **escandallo** (5.400/mes ES; `escandallo de costes` 590) | **costeo** (`costeo de recetas` 10 en ES) | §1.5, §1 |
| El mueble de venta | **vitrina** (`vitrina chocolate` 10) | mostrador · exhibidor — **sin medición: propuesta** | parcial |
| La pieza | **bombón** · **trufa** (`trufas de chocolate` 6.600) · **praliné** (`praline` 8.100) | chocolatina (2.900 ES, registro más coloquial) | §1.1 |
| La materia prima | **cobertura** / **chocolate de cobertura** (2.400 las dos, agrupadas por Google) | igual | §1.0 |
| El formato | **tableta** (`tableta de chocolate artesanal` 10) | barra — **sin medición: propuesta** | parcial |
| La bebida | **chocolate a la taza** (4.400) | chocolate caliente · chocolate de mesa (MX) — **sin medición: propuesta** | parcial |
| El método | **bean-to-bar** — **NO TRADUCIR**: 320 ES, 320 US, 140 AR, 110 MX/CO/PE, 50 CL | idéntico en los 7 mercados; hay Asociación Bean to Bar España | §3.3, §2.5 |
| La técnica | **templado** (20) por delante de **temperado** (10) | — | §1.0 |
| Formación / ingreso extra | **taller de chocolate** (210 ES) · **cata de chocolate** (170) | **curso de chocolatería**: MX 210, CO/AR/CL 140, PE 50 — **en LATAM se dice «curso», no «taller»** (`taller de chocolate` cae a 10-40 allí) | §3.1 |
| El defecto técnico | **fat bloom** (140) · **sugar bloom** (90) — **anglicismos vivos en español** | igual | §1.5 |

**Nota de aplicación de la regla de John (5-sep):** la equivalencia va en la **primera mención de cada documento y sólo en la primera**. De la tabla de arriba, **las que están respaldadas por medición** son: chocolatería artesanal, bombonería (con el matiz argentino), escandallo/costeo, bombón/trufa/praliné/chocolatina, cobertura, bean-to-bar, templado/temperado, taller/curso. **Las que son propuesta sin medir** (obrador/taller/laboratorio, vitrina/mostrador/exhibidor, tableta/barra, chocolate a la taza/caliente/de mesa) **deberían validarlas L4 o L5 antes de congelarlas en la SPEC**, o marcarse como decisión editorial y no como dato.

---

## 6. Conclusión de negocio

### 6.1 Cuánto tráfico puede aportar el SEO: entre cero y dos clics por trimestre

Los tres números que lo cierran, los tres medidos:

1. **La demanda de apertura no existe**: `montar una chocolateria` 10/mes, `plan de negocio chocolateria` **0**, y `abrir una chocolateria` / `cuanto cuesta montar una chocolateria` **sin dato en los 7 mercados medidos**. Es la mitad de `montar una panaderia` (30) y la mitad de `montar una pasteleria` (20).
2. **Nuestro activo de chocolatería ya publicado factura cero por SEO**: `/kit-tareas-chocolateria`, posición 6,0, **13 impresiones y 0 clics en 90 días**.
3. **La línea entera de guías hace 8 clics / 419 impresiones en 90 días**, y la hermana más parecida (`/guia-panaderia-obrador`) hace **2 clics**.

**Conclusión: la landing `guia-chocolateria` no venderá por SEO. No se debe prometer tráfico, y no se debe justificar el producto con él.** La venta entra —como en los cuatro productos anteriores— por **canales propios**: el hub `/productos-digitales`, la lista de compradores de Resend (el broadcast de lanzamiento con cola de 5 días), los banners de producto dentro de los 325 posts del blog ES (`fase8e-banners-corpus.py` ya reparte 3 por post entre los 44 productos; con 49 el reparto baja al ~2 % por producto), la plataforma Pickaxe (agentes «Chocolatero Consultor Pro» y «Chocolatería Creativa») y la página de rol `/usos/rol/chocolatero-bombonero`.

**Y hay un argumento de canal que ninguna cifra de SEO recoge:** el producto lleva **anunciado en el hub como «Próximamente · Junio 2026» desde mayo** (`src/pages/ProductosDigitales.tsx:959` y `ProductosDigitalesHubPage.astro:974`), con la descripción literal «Temperado, obrador, vitrina, proveedores de cacao, licencias y modelo de negocio». Va con **tres meses de retraso visible al cliente**. Ese anuncio es, hoy, el mejor activo de captación del producto — y también una deuda.

⚠️ **Consecuencia técnica para quien implemente:** al publicarlo, el array `comingSoon` se queda **VACÍO en los dos ficheros**. Ambos renderizan una sección «Próximamente» condicionada a `filteredComingSoon`; hay que comprobar que con array vacío **no se pinta una sección huérfana con cabecera y sin tarjetas**, en la SPA **y** en el Astro (son dos implementaciones paralelas y el bug tendría que cazarse dos veces).

### 6.2 Piezas de CAPTACIÓN del blog que SÍ tienen demanda — sólo dos sobreviven al filtro

De las 115 keywords medidas en España, **sólo dos** pasan el filtro de intención v2 (§2.1) **y** tienen volumen ≥ 100:

| # | Pieza propuesta | Keyword ancla | Vol/mes | Bloques SERP | Por qué |
|---|---|---|---|---|---|
| **1** | **El EUDR y el cacao: qué obliga a una chocolatería pequeña y desde cuándo** | `eudr` | **1.900** (creciendo ×2 en 6 meses) | AIO no medido; **MEDIUM comp**; hermana `reglamento deforestacion` 50 | **La única keyword de 4 cifras del nicho con intención profesional.** Fechas verificadas (§1.5): 30-dic-2026 grandes/medianas, **30-jun-2027 micro/pequeñas**. Ningún actor gastronómico español lo ha escrito para chocolateros |
| **2** | **Licencia de apertura de un obrador de chocolate: por qué NO necesita salida de humos** | `licencia de apertura` | **720** (subiendo: 170→590) | LOW comp | Transversal a todo el grupo, **y el ángulo del obrador sin hornos es propio y diferencial**. Ojo: **canibaliza** con lo que ya cubren las guías de pastelería y panadería → hay que **comprobar antes con GSC agrupando por `page,query`** (regla de `CLAUDE.md`) |

**Candidatas de segundo orden** (volumen bajo pero intención limpia y cero competencia): `fat bloom` (140) + `sugar bloom` (90) fundidas en una sola pieza sobre defectos del templado; `¿Cuánto vale 1 kg de cacao?` / `¿Cuál es la tendencia del cacao para 2026?` reformulada como **coste por bombón cuando sube el cacao** (§2.7); `¿Cuánto cuesta un curso de chocolatería?` como pieza de **precio de los talleres** (`taller de chocolate` 210 ES, `curso de chocolateria` 210 MX).

**Explícitamente DESCARTADAS pese al volumen** (y por qué, porque alguien las propondrá):

| Keyword | Vol/mes | Por qué NO |
|---|---|---|
| `churreria` | **110.000** | Local puro. Nadie que teclee eso quiere abrir nada |
| `chocolate valor` | **60.500** | Marca ajena |
| `chocolateria` | **9.900** | 12 bloques de local pack + PAA de churros (§2.2) |
| `praline` / `trufas de chocolate` | 8.100 / 6.600 | Recetas y consumidor |
| **`chocolate a la taza`** | **4.400** | **Bloque `recipes`, PAA 9/9 de «cómo hacer»** (§2.6). Es el `qué es un token` de este nicho |
| `precio del cacao` | 1.300 | Compite con Investing y Yahoo Finance con datos en vivo (§2.7). Sólo la cola larga |
| `bomboneria` | 880 | 12 local packs, relacionadas 7/8 con ciudad (§2.3) |
| **`bean to bar`** | **320** | 6 local packs + PAA de consumidor. **Sirve como vocabulario y como capítulo, no como pieza SEO** (§2.5) |

### 6.3 La decisión que el encargo pide argumentar: (a) bombonería con obrador vs (b) chocolate a la taza y churros

**Lo que dice la evidencia, sin adornos:**

| | **(a) Chocolatería artesana / bombonería con obrador** | **(b) Chocolatería de taza y churros** |
|---|---|---|
| Volumen del término que lo nombra | `chocolateria artesanal` **390** · `bomboneria` **880** | `churreria` **110.000** · `chocolate con churros` **5.400** · `chocolateria churreria` **1.000** |
| Lo que Google entiende por «chocolatería» en ES | minoritario | **mayoritario: 5 de 9 PAA son de churros** (§2.2) |
| Adónde lleva la consulta de apertura | 4 de 14 orgánicos | **7 de 8 relacionadas son la franquicia Valor** (§2.4) |
| Exportable a LATAM | **sí** (chocolatería artesanal fuerte en los 7 mercados) | **no** (chocolate a la taza: 4.400 ES vs 20-70 LATAM) |
| Coherencia con la descripción ya anunciada al cliente | **total** («temperado, obrador, vitrina, proveedores de cacao») | ninguna |
| Coherencia con el molde de la familia (obrador, capacidad, escandallo, turnos) | **total** | parcial: (b) es hostelería de barra, más cerca de `kit-tareas-cafeteria` |
| Activos propios que ya lo cubren | agentes Chocolatero Consultor Pro / Chocolatería Creativa, rol chocolatero-bombonero, kit-tareas-chocolateria (partidas: **templado, moldeado, bombones**) | `ia-churrerias-guia-completa` (18 menciones), `kit-tareas-cafeteria` |

**Mi recomendación argumentada: producto (a), con (b) como CAPÍTULO DE VARIANTE, no como producto aparte y no fuera.**

Razones, por orden de peso:
1. **El compromiso ya está adquirido.** La descripción anunciada desde mayo es (a) palabra por palabra. Cambiar el alcance a (b) después de tres meses de retraso sería incumplir dos veces.
2. **(b) no es un producto de obrador, es un producto de barra.** Su molde natural no es `guia-pasteleria-obrador` (capacidad de obrador, escandallo por lote, coste hora de obrador) sino el de una cafetería. Meterlo entero en el molde de la familia lo deformaría.
3. **Pero ignorar (b) sería un error de mercado**, y lo dice el dato más contundente del informe: **el modelo (b) es 10-100× más buscado**, tiene franquicias vivas (Valor) y su pregunta de negocio —`¿Es rentable vender churros?`— aparece en el PAA de la propia consulta `chocolateria`. Un comprador español que busque «montar una chocolatería» puede perfectamente querer eso.
4. **Por eso: un capítulo de variante que (i) distinga los dos modelos en la página 1 —lo cual además resuelve la ambigüedad que Google no resuelve—, (ii) dé el CAPEX y el P&L diferenciales del modelo de taza y churros, y (iii) diga honestamente cuándo conviene cada uno.** Ese capítulo es, encima, **el gancho de diferenciación frente a las cinco guías gratuitas que rankean**, ninguna de las cuales distingue los modelos.
5. **Producto aparte: no.** `montar una churreria` son 50/mes y `montar una chocolateria churreria` no da dato. No hay mercado para dos SKUs.

**Decisión que le corresponde a John, no a esta lente:** si el capítulo de variante entra como **un capítulo** (coherente con los 20+anexo del molde) o como **bonus separado** (como las «12 decisiones de apertura» de Pastelería). L2 recomienda **capítulo**, porque la decisión «¿qué modelo de chocolatería monto?» es de las primeras que toma el lector y un bonus se lee al final.

### 6.4 Nombre y slug recomendados

**Nombre público: «Cómo Montar una Chocolatería»** — sin cambios. Es el que lleva anunciado desde mayo en los dos ficheros del hub; cambiarlo ahora rompería la continuidad con lo prometido y con la familia («Cómo Montar una Pastelería», «Cómo Montar una Panadería»).

**Slug recomendado: `guia-chocolateria-obrador`.**

| Opción | A favor | En contra | Veredicto |
|---|---|---|---|
| **`guia-chocolateria-obrador`** | **Paridad exacta** con `guia-pasteleria-obrador` y `guia-panaderia-obrador`, que son los dos hermanos directos del molde · el sufijo `-obrador` **desambigua el modelo (a) frente al (b)** justo donde Google no desambigua · entra en `Disallow: /guia-*-access` / `-library` sin rozar nada (`robots.txt:35-36`): **ninguna URL del blog empieza por `/guia-`** | dos palabras más largo | **RECOMENDADO** |
| `guia-chocolateria` | más corto, coincide con `guia-dark-kitchen`, `guia-food-cost-ingenieria-menu` | **rompe la simetría del trío de obradores** · no desambigua (a)/(b), que es el problema central de este producto | descartado |
| `guia-como-montar-chocolateria` | literal respecto al nombre público | **ninguna landing del catálogo usa ese patrón** (se comprobó: los 10 ficheros de `astro-site/src/data/productos/guias/`); introduciría un tercer patrón de slug | descartado |

⚠️ **Comprobación obligatoria antes de publicar** (regla de `CLAUDE.md` que ya costó 26 posts ingleses): `python3 scripts/astro-migration/robots-gate.py`. `guia-chocolateria-obrador` no acaba en `-access` ni en `-library`, así que **no debería** caer en ningún patrón — pero eso se verifica con el gate, no se supone.

---

## 7. Avisos, contradicciones y preguntas abiertas

### 7.1 Contradicciones con el contexto del encargo

1. **`chocolateria` 9.900/mes «casi seguro consumidor/local»** — el encargo lo sospechaba; **queda CONFIRMADO con evidencia**: 12 bloques de local pack y 5 de 9 preguntas del PAA sobre churros (§2.2). Ya no es sospecha.
2. **El encargo propone `dulcería` en la lista de vocabulario LATAM** («chocolatería/bombonería/dulcería»). **La medición lo refuta**: en México designa una tienda de golosinas al mayoreo (§3.2). **Hay que sacarlo de la tabla de equivalencias.**
3. **El encargo dice que la línea `guia-*` sumaba «7 clics / 386 impresiones en 90 días»** (dato del 09-sep). **Remedido el 12-sep: 8 clics / 419 impresiones.** No es una corrección, es la deriva de tres días; lo anoto para que nadie crea que hay dos fuentes en conflicto.
4. **El nombre anunciado usa «Temperado»** y `templado` se busca el doble (20 vs 10). Cifras ínfimas: **no justifica cambiar el nombre público**, pero sí usar «templado» como forma principal en el cuerpo.

### 7.2 Riesgos detectados

- **Canibalización con `guia-pasteleria-obrador` y `guia-panaderia-obrador`.** Los tres comparten molde y buena parte del aparato (capacidad de obrador, escandallo, turnos, licencias). **Antes de escribir la landing hay que correr el chequeo de dos consultas que manda `CLAUDE.md`**: `ls` de landings con el término en el slug + GSC agrupando por `page,query`. Con 39 impresiones en `guia-panaderia-obrador`, el riesgo real es bajo, pero el chequeo cuesta dos comandos.
- **La sección «Próximamente» del hub se queda vacía en dos ficheros** (§6.1). Riesgo de sección huérfana con cabecera y sin contenido, sin error de build.
- **El eBook «Cómo crear tu negocio de chocolatería: Paso a Paso»** rankea en posición 13 de `montar una chocolateria` (§2.4): **hay competencia directa vendiendo un producto digital de esto**. Es trabajo de L1, pero lo señalo porque cambia el análisis competitivo.
- **Duplicación de FAQ ya identificable en el guion**: `¿Cuáles son los 3 tipos de chocolate?` vs `¿Cuáles son los 4 tipos de chocolate?` (§2.8). Si se recogen las dos del PAA, `fase8d-faq-duplicadas.py` las marcará.
- **La demanda de este nicho es la más baja de los cinco productos del ciclo.** Es un producto de catálogo y de compromiso, no de mercado. Si el criterio fuera el volumen, no se haría — igual que pasó con las librerías de prompts, y aquella decisión fue correcta.

### 7.3 Fuentes bloqueadas o no verificadas

- **AI Overview**: DataForSEO devuelve `asynchronous_ai_overview: true` con `markdown: null`. **Contenido inaccesible** con el endpoint actual, en las 2 SERP donde aparece. Limitación heredada de la L2 de Pastelería, sin resolver.
- **EUDR**: verificado con **dos fuentes secundarias concordantes** (taric.es y aidimme.es, consultadas el 2026-09-12), que citan el **Reglamento (UE) 2025/2650** y la referencia DOUE `OJ:L_202502650`. **No abrí EUR-Lex ni el DOUE directamente.** Antes de que una fecha del EUDR entre en el producto, **L3 tiene que confirmarla contra el texto primario**.
- **Cifras de la crisis del cacao (ICCO), CAPEX, precios de atemperadora/vitrina/cámara**: **«sin fuente»** en esta lente, no medidas. No las repito como buenas.
- **El error del «carnet de manipulador» de plandenegocio.es**: la URL rankea (verificado), **la frase no la he abierto** (§0.4).
- **Equivalencias LATAM de obrador/vitrina/tableta/chocolate de mesa**: **propuesta editorial sin medición**, marcadas como tales en §5.

---

*Fin del informe L2. Ninguna cifra de este documento procede de la memoria del modelo: todas salen de DataForSEO (2026-09-12), de GSC (`sc-domain:aichef.pro`, 2026-06-14 → 2026-09-12), del propio repositorio con fichero:línea, o de las dos URLs citadas en §1.5.*
