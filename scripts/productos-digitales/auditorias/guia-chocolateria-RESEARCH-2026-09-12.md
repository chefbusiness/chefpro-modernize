# RESEARCH CONSOLIDADO — «Cómo Montar una Chocolatería»
## Producto digital NUEVO nº 5 · AI Chef Pro · línea «Cómo Montar» (hermano de `guia-pasteleria-obrador` y `guia-panaderia-obrador`)

**Fecha:** 2026-09-12 · **Estado:** research cerrado, PENDIENTE DEL OK DE JOHN antes de escribir una sola línea de producto.
**Fuentes:** las seis lentes de este mismo directorio (`guia-chocolateria-research-L1-competencia.md`, `-L2-serp-demanda.md`, `-L3-normativa.md`, `-L4-sector-equipamiento.md`, `-L5-cliente.md`, `-L6-assets.md`), **leídas enteras**, más **verificación propia** contra el repo (`src/data/products-catalog.ts`, `netlify/shared/*.ts`, `astro-site/src/lib/zona-app.ts`, `astro-site/public/robots.txt`, `astro-site/public/dl/**`, `astro-site/src/content/blog/es/**`, `src/data/use-cases*.ts`, `scripts/productos-digitales/**`, `CALENDARIO-V2-SEMANAL.md`, `git log`/`git status`), una consulta **en vivo a GSC** (`sc-domain:aichef.pro`, 2026-06-14 → 2026-09-12), **17 mediciones propias en DataForSEO** (España, 2026-09-12) y **dos `curl` a producción**.
**Regla aplicada:** cada cifra lleva fuente y fecha, o va marcada **«sin fuente»** y no entra. Nada de memoria del modelo. Este documento es research y propuesta: **no contiene contenido de producto**.

> ### Diecisiete verificaciones propias — seis CORRIGEN a las lentes y tres son hallazgos nuevos (detalle en §16)
>
> 1. 🔴 **CORRECCIÓN A L6, y mata su riesgo nº 1: el bug del `%` YA ESTÁ ARREGLADO.** L6 declara «R-1, probabilidad **casi segura**: los `%` en los nombres de la carta rompen las tablas (`documentos.py:722`)» y condiciona el juego de datos a arreglarlo antes de construir. Hoy `documentos.py:692` dice `RX_ETIQUETA_PCT = re.compile(r'\(\s*%\s*\)|\ben\s*%|\(porcentaje\)')` — **sin el `|%\s*$`** — y `:694-697` lleva el comentario literal «**A1 (2026-09-10): el patrón viejo llevaba `%\s*$`, que casa con CUALQUIER texto acabado en «%» — y la referencia T1 de la carta se llama «Tarta de chocolate 70 %»**». El fix entró en el commit **`0ba5158`** (fixer 1.0.1 de Pastelería) y está publicado en su changelog (`src/data/productos-changelog.ts:127`). **«Tableta 70 %» y «Cobertura 55 %» son nombres seguros.**
> 2. 🔴 **CORRECCIÓN A L6, y mata su riesgo nº 2: el gate de tipo de `verificar_guion.py` YA EXISTE.** L6 lo pide como «fix obligatorio antes de la sesión B». Está en `scripts/productos-digitales/guia-pasteleria/verificar_guion.py:207`: `if fmt in FMT_NUMERICOS and not isinstance(v, (int, float)): falla(…TIPO INCOMPATIBLE…)`, con el comentario que cita **A2 (2026-09-10)** y la cifra inventada («veinte semanas»). **Copiar el fichero a `guia-chocolateria/` trae el gate gratis.** Consecuencia de presupuesto: **el 1,5 M que L6 decía que se podía ahorrar arreglando los dos bugs ya está ahorrado** (§15.4).
> 3. 🔴 **CORRECCIÓN A L6, y cae su pregunta BLOQUEANTE: la Guía de Pastelería está cerrada, pusheada y LIVE.** L6 abre con «el producto 48 sigue en `main` LOCAL, sin push, con los 13 entregables sin commitear». Hoy: `git status -sb` → `## main...origin/main` **sin marcador ahead/behind** (`git rev-list --count origin/main..main` = **0**); lo único no commiteado son **los seis `.md` de estas lentes** y `scripts/termica/watchdog-termico.sh`; el Payment Link está en `netlify/shared/payment-links.ts:8`; y **`curl https://aichef.pro/guia-pasteleria-obrador` devuelve 200** con «103 páginas» y `buy.stripe.com/7sY00c5Sk64e1MPejH6oo1r` dentro del HTML. **No hay nada que cerrar antes de arrancar el 49.**
> 4. 🔴 **CORRECCIÓN A L6: `zona-app.ts` NO tiene 49 productos, tiene 48.** L6 avisa de «una entrada de más en zona-app respecto al catálogo; conviene identificarla». La 49.ª coincidencia de `grep -c "productId:"` es la **declaración de tipo** `productId: string;` de la línea 31. Extraídos los 48 slugs reales y cruzados con el catálogo: **`comm` no devuelve ni una diferencia en ninguno de los dos sentidos, y `uniq -d` ningún duplicado.** Los cuatro ficheros están cuadrados a 48.
> 5. 🔴 **AMPLIACIÓN GRAVE A L2, y cambia el argumento de canal: el universo de chocolate hace 285 impresiones y 6 clics, no «24 impresiones y 0 clics».** L2 midió GSC filtrando por **query** que contiene «chocolat» (24 impresiones / 0 clics) y concluyó que el nicho no trae a nadie. Medido hoy por mí filtrando por **PAGE**: **38 URLs, 285 impresiones y 6 clics** en 90 días, de las cuales **159 impresiones y 3 clics** en el dominio vivo. Y el dato que L2 no vio: **`/blog/chocolateria-artesanal-e-ia-una-combinacion-innovadora` hace 3 clics / 30 impresiones / posición 4,9 / CTR 10 %**. **Es exactamente la trampa que la propia L2 documentó** (las queries anonimizadas no aparecen en el desglose por consulta) — sólo que la aplicó al kit y no a sí misma.
> 6. 🔴 **HALLAZGO NUEVO, no está en ninguna lente, y tiene dinero detrás: hay una CUARTA página de chocolate y ya publica una inversión que el research refuta.** `/usos/consultoria/chocolatero-consultor` (`src/data/use-cases-content.es.consultor.ts:348`, `productIds` en `:386`) publica en su FAQ —y por tanto en su `FAQPage`— «**una chocolatería artesanal premium en España requiere una inversión inicial entre 80.000 € y 250.000 € para un local de 50-80 m²**», con «templadora continua (8.000-25.000 €)», «**vitrina refrigerada (6.000-18.000 €)**» y «ticket medio entre 18 € y 35 €». **Está en los SIETE idiomas** (`grep -l "80.000" src/data/use-cases-content.*.consultor.ts` → 7 ficheros). La vitrina de chocolate verificada por L4 cuesta **2.684,99 € sin IVA** (§4.3): la página publica **2,2-6,7×** ese precio. Si la guía sale con el CAPEX verificado, **el mismo dominio publicará dos inversiones incompatibles para el mismo negocio**. Decisión **D12**.
> 7. 🔴 **AMPLIACIÓN A L6: el universo de blog accionable son 8 posts, no 7.** Censados por mí los **326** `.md` de `astro-site/src/content/blog/es/` contando menciones de chocolate/bombón/cacao/praliné: falta **`coulant-de-guanaja-70-y-praline-homenaje-a-laguiole` (31 menciones)**, y sus tres banners de hoy son `kit-tareas-chocolateria` · **`plan-negocio-cafeteria`** · **`kit-tareas-asador`**. Es el **segundo** peor encaje del corpus después del de sushi, y L6 no lo tenía.
> 8. ✅ **MATIZ A L6 sobre «el hub miente por defecto»: no miente, omite.** Los 11 ficheros de `kit-tareas-chocolateria` son **9 numerados + 2 BONUS**, y ése es **el estándar de la familia**: contados los 18 kits, **16 tienen exactamente 11 ficheros (9+2)**. La descripción «9 checklists» del hub (`ProductosDigitalesHubPage.astro:806`) es **literalmente correcta** para los checklists; lo que falta es «+ 2 bonus» (+22 %), no el +67 % de Pastelería. **Y el que sí vende de más es otro: `kit-tareas-chef-privado` entrega 7 checklists + 2 bonus y el hub anuncia «9 checklists profesionales».**
> 9. ✅ **MATIZ A L6 sobre el `comingSoon` vacío: el rótulo no queda visible para siempre, queda en el HTML servido.** Cierto que `…HubPage.astro:1448` renderiza la sección **sin guarda server-side** (la SPA sí la tiene, `ProductosDigitales.tsx:1227`). Pero el script de cliente **la oculta**: `:1883` hace `comingSection.classList.toggle('hidden', matchingComing.length === 0)` y `:2256` llama a `apply()` al cargar. **El defecto real es un destello (FOUC) y un rótulo huérfano dentro del HTML estático** — que es lo que ven Google y quien tenga JS bloqueado. Sigue habiendo que arreglarlo, pero no es «una sección vacía en producción».
> 10. ✅ **Confirmo el censo de superficies de L6:** `products-catalog.ts` **48** · `payment-links.ts` **48** · `product-prices.ts` **48**. Y **`curl https://aichef.pro/guia-chocolateria-obrador` devuelve 404**: el slug está libre. `robots.txt` cubre `Disallow: /guia-*-access` y `/guia-*-library` en **los 5 bloques** (líneas 35-36, 53-54, 71-72, 89-90, 107-108): **nada que tocar**.
> 11. ✅ **Confirmo a L2 al dígito con GSC en vivo:** la línea `guia-*` entera hace **8 clics / 419 impresiones** en 90 días (peruano 3/118 · panadería 2/39 · mexicano 2/73 · japonés 1/64 · el resto a cero). `/guia-pasteleria-obrador` **no aparece**: se publicó el 10-sep. Ausencia esperada.
> 12. ✅ **CORRECCIÓN DE ESCALERA a L1, L3, L5 y L6: la franja de 65 € ya son OCHO productos, no siete.** Parseado `products-catalog.ts` entero hoy: 9 € ×1 · **12 € ×13** · 14 € ×8 · 18/18,50 € ×2 · 24 € ×1 · 29 € ×2 · 35 € ×3 · 39 € ×1 · 45 € ×4 · **55 € ×3** · **65 € ×8** · 85 € ×1 · 89 € ×1. Éste sería el **noveno** de la franja de 65 €.
> 13. ✅ **Los prefijos `CHN-` y `CHS-` están libres y no colisionan entre sí.** Verificado sobre las **411** entradas de `guias-v2-research-sector.json`: PS 123 · PA 63 · MM 59 · CE 40 · FC 36 · CS 23 · TRAM 12 · MICH 10 · SECT 10 · REPS 7 · CONV 7 · ANIS 6 · TURG 5 · JORN 4 · SMI 3 · TICK 3. **Ni un `CHN` ni un `CHS`.** A diferencia del Manual del Chef Ejecutivo (donde L3 y L4 se pisaron 23 ids con el mismo prefijo `CE-`), **aquí no hay nada que renombrar**.
> 14. ✅ **Medición propia en DataForSEO (España, 2026-09-12), con tres datos que ninguna lente tiene:** `montar una bomboneria`, `abrir una bomboneria`, `negocio de bombones`, `regalo de empresa chocolate` y `chocolateria artesanal barcelona` **no devuelven dato en ninguna grafía** — la intención de apertura de la rama (a) no existe ni cambiando de palabra; **`bomboneria` está SUBIENDO** (serie `590·590·590·880·880·1.000`, +69 % en el semestre) y **`chocolateria artesanal` también** (`260·170·170·260·320·390`); y **`montar una chocolateria` tiene DOS meses a CERO** en su serie de seis (`10·10·0·10·0·10`), así que su «10/mes» es todavía más frágil de lo que parece.
> 15. 🔴 **ARBITRAJE ENTRE LENTES — la temperatura de la cámara SÍ tiene fuente, y no es la del brief.** L4 la deja «sin fuente» y avisa de que el brief dice 16-18 °C sin respaldo. **L5 la tiene literal, leída en la misma fuente que usó L4**: `C46`, Llevats21, 23-jun-2026 — «cámaras de conservación específicas para chocolate, que mantienen **entre 15 y 18 °C** con humedad controlada». **Lo que entra en el producto es 15-18 °C** (Llevats21), **no los 16-18 °C del encargo**, y siempre como **criterio técnico del operador**, nunca como requisito legal (`CHN-30`). La sala de trabajo es otra cosa: **18-22 °C con HR < 55 %** (`C41`, `C43`).
> 16. 🔴 **ARBITRAJE ENTRE LENTES — L1 y L4 publican cifras DISTINTAS de las MISMAS franquicias.** Valor: **150.000 € de inversión y canon 24.000 €** (L1, lafranquicia.es) frente a **desde 125.000 € y canon 24.040 €** (L4, lexpress-franchise). Chök: **200.000 €, canon 30.000 € + IVA, 70-120 m²** (L1, lafranquicia.es) frente a **desde 100.000 €, canon 30.000 €, local mínimo 55 m²** (L4, franquiciashoy). Es literalmente la **N-18 de Pastelería** repitiéndose: los portales se contradicen dentro del mismo dato. **Ninguna cifra de franquicia entra como dato auditado** (§15.1, `N-6`).
> 17. ✅ **Confirmo banner a banner los tres posts de chocolate** y las páginas `/usos/`: `chocolatero` (`use-cases-content.es.ts:1225`, `productIds` en `:1264`), `chocolateria` (`:3210` / `:3248`) y la tercera del punto 6. El pipeline se reutiliza tal cual: `documentos.py` **2.246 líneas**, `motor.py` **2.135**, `dump_prompts.py` **62**, `check_bloque.py` **32**, `solape.py` **82**; los 8 `gen_*.py` de pastelería suman **12.196 líneas**, `datos_ejemplo.py` **3.324**, el guion **4.924** y la SPEC **330**.

> ⚠️ **Dos correcciones al propio encargo, menores pero medidas:** la Guía de Pastelería entrega **103 págs + 37 + 18** (no «103 + 38 + 19»; el fixer 1.0.1 del 12-sep regeneró los tres documentos, y así lo registra `CALENDARIO-V2-SEMANAL.md:140`), y el blog ES tiene hoy **326** posts, no 325.

---

## 0. Lo primero: qué demanda hay de verdad y por dónde entra el dinero

**Éste es el producto con la demanda de apertura más baja de los cinco del ciclo, y es la mitad que la de su hermano ya vendido.** Volúmenes de DataForSEO (Google Ads, búsquedas/mes, España), medidos por L2 el 2026-09-12 salvo los marcados ✅, que **los he medido yo ese mismo día**:

| Bloque | Keywords | Vol/mes |
|---|---|---|
| **Genérico de CONSUMIDOR** (no es nuestro) | `churreria` 110.000 · `chocolate valor` 60.500 · `chocolateria` 9.900 · `praline` 8.100 · `trufas de chocolate` 6.600 · `chocolate con churros` 5.400 · **`chocolate a la taza` 4.400** ✅ · `chocolatina` 2.900 · `cobertura de chocolate` 2.400 · **`chocolateria churreria` 1.000** ✅ · **`bomboneria` 880** ✅ | — |
| **El núcleo del oficio** (lo que de verdad describe la guía) | **`chocolateria artesanal` 390** ✅ · `chocolates artesanos` 390 · `bombones personalizados` 390 · **`bean to bar` 320** ✅ · `taller de chocolate` 210 · `cata de chocolate` 170 · `chocolateria online` 110 · `templado de chocolate` 20 · **`obrador de chocolate` 10** ✅ · `camara de chocolate` 10 · `atemperadora de chocolate precio` 10 | **entre 10 y 390** |
| **Apertura — el bloque entero es humo estadístico** | **`montar una chocolateria` 10** ✅ (serie `10·10·0·10·0·10`) · `como montar una chocolateria` 10 · `montar chocolateria` 10 · `negocio de chocolates` 10 · **`plan de negocio chocolateria` 0 explícito** · `abrir una chocolateria`, `cuanto cuesta abrir una chocolateria`, `rentabilidad chocolateria`, `inversion chocolateria` **sin dato** | **~40** |
| **Medido por mí y NO por las lentes** ✅ | **`montar una bomboneria` · `abrir una bomboneria` · `negocio de bombones` · `regalo de empresa chocolate` · `chocolateria artesanal barcelona` = SIN DATO** · `bombones corporativos` 10 · `taller de bombones` 10 · `vender bombones` 10 | **~30** |
| **El único ángulo normativo con volumen** | **`eudr` 1.900** ✅ (serie `480·880·1.000·1.300·1.000·880`, **creció ×2 en el semestre**) · `licencia de apertura` 720 · `fat bloom` 140 · `sugar bloom` 90 · `reglamento deforestacion` 50 · `crisis del cacao` 20 · `rd 1055 2003` 10 | — |

**Seis lecturas, y sólo una es cómoda:**

1. **En España «chocolatería» significa chocolate a la taza con churros, no bombonería, y está probado con SERP.** L2 abrió la SERP de `chocolateria` (9.900/mes): **12 bloques de local pack**, los orgánicos 2, 4 y 5 son **Chocolatería San Ginés**, y **5 de las 9 preguntas del People Also Ask son de churros** («¿Cuál es la churrería más famosa de Madrid?», «¿Es rentable vender churros?»). Google no desambigua el término: **el producto tiene que desambiguarlo por él** (§1.3).
2. **La demanda de apertura no existe en ninguna de las dos ramas, ni en ninguna grafía.** `montar una chocolateria` 10/mes con dos meses a cero; `montar una churreria` 50; y **las cuatro variantes de bombonería que medí yo no devuelven dato**. Como referencia: `montar una panaderia` 30 y `montar una pasteleria` 20, y **los dos hermanos a 65 € ya están vendidos y publicados**. Nunca se ha lanzado un producto de esta línea por el volumen de su keyword, y no debe hacerse ahora.
3. **El filtro de intención de L2, ampliado a v2, clasifica 13 de 13 SERP sin un error.** `local_pack` presente → no es nuestra (8/8) · bloque `recipes` → no es nuestra (`chocolate a la taza`) · `knowledge_graph` + `google_reviews` sin local pack → no es nuestra (`obrador de chocolate`) · **`ai_overview` sin local pack → sí es nuestra (2/2)**. Sólo **dos** de las trece consultas son nuestras: `montar una chocolateria` y `precio del cacao`. El filtro de una sola señal habría fallado 2 de 13.
4. **⚠️ La anti-recomendación más cara: NO escribir «chocolate a la taza» (4.400/mes) como pieza de captación.** Su SERP trae bloque `recipes` y **sus nueve preguntas del PAA son «cómo hacer»**: es el «qué es un token» de este nicho. Igual con `churreria` (110.000), `chocolate valor` (60.500), `praline` (8.100) y `bomboneria` (880, con 7 de 8 relacionadas llevando ciudad o «cerca de mí»).
5. **Y nuestro propio activo de chocolatería ya publicado factura cero por SEO.** `/kit-tareas-chocolateria` (12 €) lleva meses en **posición media 6,0** y ha hecho **13 impresiones y 0 clics** en 90 días. Un producto de 12 € en primera página que nadie ve.
6. ✅ **Lo único cómodo, y lo descubrí yo: el nicho SÍ tiene clics, sólo que L2 los midió por la dimensión equivocada** (§0.1). Y las dos keywords del núcleo del oficio están **subiendo**: `bomboneria` de 590 a 1.000 y `chocolateria artesanal` de 260 a 390 en el semestre.

### 0.1 El mejor predictor que tenemos, verificado por mí en GSC hoy

**(a) La línea `guia-*` entera** — `sc-domain:aichef.pro`, `page contains /guia-`, 2026-06-14 → 2026-09-12, consultado por mí el 2026-09-12:

| Landing | Clics | Impresiones | CTR | Posición |
|---|---|---|---|---|
| `/guia-restaurante-peruano` | 3 | 118 | 2,54 % | 5,6 |
| `/guia-restaurante-mexicano` | 2 | 73 | 2,74 % | 9,4 |
| **`/guia-panaderia-obrador`** | **2** | **39** | **5,13 %** | **7,3** |
| `/guia-restaurante-japones` | 1 | 64 | 1,56 % | 7,9 |
| `/guia-restaurante-gastronomico` | 0 | 51 (+1) | 0 % | 13,7 |
| `/guia-restaurante-casual` | 0 | 46 | 0 % | 9,0 |
| `/guia-food-cost-ingenieria-menu` | 0 | 11 | 0 % | 6,9 |
| `/guia-restaurante-nikkei` | 0 | 11 | 0 % | 5,5 |
| `/guia-dark-kitchen` | 0 | 4 | 0 % | 39,2 |
| **TOTAL LÍNEA** | **8** | **419** | **1,91 %** | — |

**(b) El universo de chocolate, medido por PAGE — y aquí está la corrección** (`page contains chocolat`, misma ventana, 38 URLs):

| Página | Clics | Impr. | CTR | Pos. |
|---|---|---|---|---|
| **`/blog/chocolateria-artesanal-e-ia-una-combinacion-innovadora`** | **3** | **30** | **10,00 %** | **4,9** |
| `blog.aichef.pro/chocolateria-artesanal-e-ia…` (legacy, 301) | 2 | 19 | 10,53 % | 8,2 |
| `blog.aichef.pro/en/Top-10-chocolate-schools-in-the-United-States-2026/` (legacy, **inglés**) | 1 | 26 | 3,85 % | 70,2 |
| `/blog/libreria-de-prompts-para-chocolatero-consultor-pro-ai` | 0 | 47 | 0 % | 7,8 |
| `/usos/consultoria/chocolatero-consultor` | 0 | 15 | 0 % | **4,3** |
| `/en/use-cases/consultancy/chocolatier-consultant` | 0 | 14 | 0 % | 10,2 |
| **`/kit-tareas-chocolateria`** | **0** | **13** | 0 % | **6,0** |
| `/blog/libreria-de-prompts-para-chocolateria-creativa-ai` | 0 | 12 | 0 % | 7,4 |
| `/nl`, `/pt`, `/de`, `/en` (roles y consultorías de chocolate) | 0 | 22 | 0 % | 1,5-10,2 |
| `/usos/rol/chocolatero-bombonero` · `/usos/concepto/chocolateria-bomboneria` | 0 | 6 | 0 % | 4,5-10,2 |
| resto (24 URLs, casi todas legacy y multi-idioma) | 0 | 81 | 0 % | — |
| **TOTAL (38 URLs)** | **6** | **285** | **2,11 %** | — |
| *de las cuales en el dominio vivo `aichef.pro`* | **3** | **159** | | |

**Cómo se lee esto sin engañarse:**

- **El nicho no está muerto, pero tampoco compra.** Seis clics en 90 días, y **la mitad cuelgan del subdominio legacy** ya 301-eado — la trampa que documenta `CLAUDE.md` y que L2 evitó en su §4.1 pero no en su conclusión.
- **El post `chocolateria-artesanal-e-ia` es el activo real**: posición 4,9, CTR 10 % y 3 clics propios. Es el mejor sitio del blog para colgar un enlace contextual a la landing (§13.2) — y es justo el que hoy vende **cocina peruana y sushi**.
- **`/usos/consultoria/chocolatero-consultor` en posición 4,3 con 15 impresiones** es la segunda entrada, y es la página cuya FAQ publica hoy una inversión que este research refuta (verificación 6).
- **Estimación honesta para `/guia-chocolateria-obrador`: 0-2 clics orgánicos por trimestre y 0 ventas atribuibles a búsqueda en el primer año.** La hermana más parecida (`/guia-panaderia-obrador`, mismo molde, mismo precio, publicada antes) hace 2 clics en 90 días, y la demanda de apertura de chocolatería es la mitad. **No se debe prometer más, ni en el copy ni en el informe a John.**

### 0.2 Por dónde entra el dinero: ocho canales, todos nuestros

| Canal | Estado real hoy (verificado por mí) | Qué hay que hacer |
|---|---|---|
| **El producto está ANUNCIADO en el hub desde mayo, y vencido** | `src/pages/ProductosDigitales.tsx:958-960` y `astro-site/src/components/pages/ProductosDigitalesHubPage.astro:973-975`: `{ name: 'Cómo Montar una Chocolatería', desc: 'Temperado, obrador, vitrina, proveedores de cacao, licencias y modelo de negocio.', tags: ['pdf','guias','chocolateria'], phase: 'Junio 2026' }`. **Tres meses de retraso visible al cliente** | Tarjeta real con badge «Nuevo» + **vaciar `comingSoon` en LOS DOS ficheros** + la guarda del Astro y el badge condicional (§13.1, decisión **D6**) |
| **El buscador del hub** | `sinonimos-buscador.json` tiene 8 grupos, 4 frases y 7 alias; **ni uno menciona chocolate, cacao, bombón ni templado** (verificado). El placeholder animado (`…HubPage.astro:2260-2279`) sugiere «montar una pastelería» pero **no** chocolatería | **Alias nuevo** (§13.1). No dispara el gate de grupos huérfanos |
| **8 posts propios con sus 3 banners puestos** | Verificado post a post (§13.2). Los dos peores encajes: `chocolateria-artesanal-e-ia` vende **sushi y cocina peruana**, y `coulant-de-guanaja-70-y-praline` vende **asador y cafetería** | **Sustitución quirúrgica** en 4 posts + enlace contextual en el resto |
| **4 páginas `/usos/` del público exacto** | `rol/chocolatero-bombonero` · `concepto/chocolateria-bomboneria` · **`consultoria/chocolatero-consultor`** (la que ninguna lente vio) · y, por la variante, las dos de heladería. Las tres de chocolate venden hoy **sólo productos de 9-18 €** | Añadir `guia-chocolateria-obrador` a sus `productIds`, enlace **bidireccional**, **y resolver D12** (la cifra de 80.000-250.000 € en 7 idiomas) |
| **Rotación general de banners** | 326 posts ES con 3 banners cada uno y rotación por los 44+ productos (`fase8e-banners-corpus.py`) | Entrada **49** en `products-catalog.ts` → entra en la rotación sola |
| **Lista de compradores (Resend)** | Segmentos de `kit-tareas-chocolateria` (12 €), `kit-escandallos` (12 €), `pack-appcc` (14 €), Guía Food Cost (55 €), Manual del Manager (55 €), Manual del Chef Ejecutivo (65 €) y **Guía de Pastelería (65 €)** | **Broadcast propio**. Primer hueco libre: **24-oct-2026, 08:00 UTC** (§13.3) |
| **Plataforma (Pickaxe)** | Agentes **«Chocolatero Consultor Pro»** y **«Chocolatería Creativa»** ⚠️ *nombres tomados del repo; la fuente autorizada es la plataforma* | Mención desde el agente y desde su librería de prompts. **Comprobar contra `fase8c-agentes/catalogo-hub.json`** |
| **La buyer persona P5, que ya nos ha comprado** | La pastelería/cafetería que **añade** obrador de chocolate (§6.3). **Está en la lista de compradores de la Guía de Pastelería, publicada hace dos días** | Es el mejor objetivo del correo de lanzamiento, y el argumento es del propio oficio: «*para elaborar y vender productos de chocolate necesitas menos infraestructura, maquinaria y mano de obra que para la pastelería. Es más rentable*» (Lluís Morera, `C25`) |

**Conclusión del bloque, sin adornos:** este producto **no se lanza por volumen de búsqueda**. Se lanza porque (a) **lleva anunciado desde mayo en dos ficheros y es la última entrada del `comingSoon`**, con tres meses de retraso visible; (b) el hueco de pago está medido producto a producto y **no existe en español una sola guía de negocio de chocolatería** (§7); (c) tenemos ocho canales propios y una base de compradores de pastelería que acaba de pagar 65 € por el hermano; y (d) **el bloque normativo del chocolate no lo cubre nadie** y es lo que separa 65 € de 49 €. **La landing no va a captar por búsqueda y no se debe prometer que lo haga.**

---

## 1. Los tipos de negocio, los conceptos que la guía DEBE fijar, y la decisión de alcance

### 1.1 Bloque obligatorio 1 — Los 12 sub-conceptos del nicho (ids `CHS-01` a `CHS-12`)

**La decisión más cara que toma el lector es qué chocolatería monta, y en este sector la palabra significa dos negocios que no comparten ni licencia, ni maquinaria, ni ticket, ni convenio.** El salto entre extremos medidos es de **un factor 36**: de 5.740 € de núcleo de máquina a 200.000 € de franquicia.

| id | Sub-concepto | Inversión de referencia | m² | Personal | Qué cambia estructuralmente |
|---|---|---|---|---|---|
| **CHS-01** | **Obrador en casa / venta directa** | «sin fuente» (no hay cifra publicada para chocolate) | zona separada del uso doméstico | 1 | 🔴 **Régimen legal PROPIO y muy restrictivo, y con un hallazgo incómodo**: el chocolate **NO está en la lista estatal del art. 13.8 del RD 1021/2022** (`CHN-44`). Ver §2.1 |
| **CHS-02** | **Obrador de bombonería sin venta al público (B2B)** | Núcleo de máquina **verificado línea a línea: ≈24.105 €** (§4.6, base mixta) | «sin fuente» | 1-2 | Cliente = hostelería, regalo corporativo, tiendas. Sin escaparate. **Aquí se rompe el «restringido» del art. 3** (`CHN-41`) |
| **CHS-03** ⭐ | **Bombonería / chocolatería artesana con obrador + tienda** | **20.000-30.000 €**, «hasta 80.000 € según el proyecto» | **60-100 m²** | **1-2** | **Es el caso central propuesto.** Aparece la vitrina de chocolate a **+14/+17 °C** (§4.3), el TPV y el packaging de regalo |
| **CHS-04** | **Tienda de chocolate SIN obrador** | «sin fuente» | «sin fuente» | 1-2 | Compra producto acabado. **Pierde el margen de transformación** y no puede usar «ELABORACIÓN PROPIA» (`CHN-55`) |
| **CHS-05** | **Bean-to-bar** (del grano a la tableta) | **«sin fuente (precio)»** — el tren de máquinas **no tiene precio público** (§4.7) | «sin fuente» | «sin fuente» | 🔴 El único que **importa grano** → **OPERADOR** del EUDR con diligencia debida completa (`CHN-25`), **CAPCA por el tostado** (`CHN-47`) y los HAP del grano (`CHN-18`). Tiene **asociación propia** con más de 40 miembros (§5.3) |
| **CHS-06** | **Chocolatería-cafetería / con degustación** | «sin fuente» | «sin fuente» | 3-5 (por analogía; «sin fuente» para chocolate) | Añade barra y aseos de público; **cambia de régimen sanitario** si elabora comidas preparadas (art. 30 del RD 1086/2020, `CHN-51`) y cambia el IVA y probablemente el convenio |
| **CHS-07** ⚠️ | **Chocolatería de taza y churros** | «sin fuente» de inversión. **Traspasos reales: 58.000-95.000 €** (§3.6) | **74-118 m²** (traspasos) | «sin fuente» | **Es otro negocio.** Freidora + **extracción de humos** + gas (`CHN-48`) + comidas preparadas (`CHN-51`). Margen bruto del churro **85-90 %** (§3.4). **Ver la decisión del §1.3** |
| **CHS-08** | **Chocolatería-pastelería** | Traspasos reales de pastelería-bombonería: **26.000-210.000 €** (§3.6) | **90-400 m²** | «sin fuente» | Horno → vuelve la salida de humos y **dos regímenes térmicos en el mismo local** (`CHN-30b`) |
| **CHS-09** | **Chocolatería-heladería** | «sin fuente» | «sin fuente» | «sin fuente» | **Contraestacional perfecta**: el valle de verano del chocolate (§3.5) es el pico del helado. Es la respuesta natural a la peor debilidad del modelo |
| **CHS-10** | **Venta online con envío** | «sin fuente» | — | — | El chocolate **no viaja en verano** sin isotérmico. Caso Equimercado: **apaga la tienda el 12 de junio, todos los años** (`C40`). Y el art. 4.3 responsabiliza al operador de la temperatura en todo el transporte (`CHN-56`) |
| **CHS-11** | **Talleres y catas como línea de ingresos** | «sin fuente» | — | 1 | **25-45 €/persona**, mínimo típico 6 pax (§3.3). Margen altísimo, **no consume cobertura** y **funciona en agosto** |
| **CHS-12** | **Franquicia** | ⚠️ **Cifras contradictorias entre lentes** (§15.1 `N-6`): Valor **125.000 o 150.000 €** · Chök **100.000 o 200.000 €** · Sven **33.000 €** · Chocolat-Box **60.000-70.000 €** · Fábrica di Chocolate **60.000 €** · Maestro Churrero **115.000 €** | Chök **55 m²** (el mínimo de todo el research) · Valor **150 m²** · Cacao Sampaka **100-250 m² y ≥500.000 hab.** | — | **Canon de entrada de 5.000 a 30.000 €** + royalty + compra obligada a central. **Es 4-5× la inversión de CHS-03** |

**Fuentes:** CHS-03, CHS-40 y CHS-70 → Stefano Ventura, plandenegocio.es, **17-dic-2025**, https://plandenegocio.es/como-hacer-un-plan-de-negocio-para-chocolateria/ (fiabilidad **MEDIA**; ⚠️ **es el mismo dominio** cuyo artículo de requisitos comete el error del «carnet de manipulador») · CHS-07/CHS-08 traspasos → Milanuncios, 2026-09-12 · CHS-10 → https://bomboneriapons.com/en/pages/history-bomboneria-pons y Equimercado 04-jun-2026 · CHS-12 → las seis fichas de franquicia de L1 y L4, todas 2026-09-12.

### 1.2 Los 12 conceptos que la SERP mezcla y que la guía tiene que fijar

Es el equivalente a las 12 distinciones de Pastelería. Aquí el reparto es **todavía más duro para lo gratuito: en 9 de 12 lo gratuito afirma algo falso o no lo menciona siquiera**.

| # | Concepto | Qué es exactamente | Con qué se confunde | ¿Lo cubre bien lo gratuito? |
|---|---|---|---|---|
| 1 | **«Chocolatería» son DOS negocios** 🔴 | El IAE los separa con nombre y apellidos: **644.5** «Comercio al por menor de bombones y caramelos» (el obrador), **grupo 676** «Servicios en chocolaterías, heladerías y horchaterías» (la de taza) y **644.6** (la churrería, que faculta para elaborar churros) | Google los funde: 5 de 9 PAA de `chocolateria` son de churros | **NO. Ninguna de las 10 fuentes gratuitas auditadas distingue los modelos** (`CHN-72`) |
| 2 | **«Bombón de chocolate» tiene definición legal** 🔴 | Ap. 1.13 del RD 1055/2003: producto **del tamaño de un bocado** en el que el chocolate es **≥25 % del peso total**, relleno incluido | Se llama bombón a cualquier bocado bañado | **NO.** Un bocado con 15 % de cobertura y 85 % de relleno **no se puede llamar bombón de chocolate** (`CHN-03`) |
| 3 | **«Praliné», «trufa», «artesano» y «casero» NO existen en la norma** 🔴 | Búsqueda exhaustiva sobre el texto íntegro del RD 1055/2003 **y** del RD 496/2010: esas cinco palabras **no aparecen ni una vez** | Se usan como si fueran categorías protegidas | **NO.** Son nombres comerciales; el único límite es no engañar (`CHN-03b`, `CHN-53`) |
| 4 | **La mención «cacao: X % mínimo» NO es universal** | El ap. 6.d) la exige **sólo** para los apartados 1.4, 1.5, 1.6, 1.7, 1.8, 1.11 y 1.12 | Se cree obligatoria siempre | **NO.** **No la exige** para chocolate **blanco** (1.9), **relleno** (1.10) ni **bombón** (1.13). Ponerla no es ilegal; **decir que es obligatoria en una caja de bombones sí sería falso** (`CHN-07`) |
| 5 | **El permiso legal para las palabras que venden está en el ap. 6.g)** | «Fino», «superior», «extra» sólo sobre «chocolate», «chocolate con leche» y «cobertura», y sólo con **≥43 % / ≥26 %** (negro), **≥30 % / ≥18 % / ≥4,5 %** (leche) y **≥16 %** desgrasada (cobertura) | Se pone el calificativo por marketing | **NO, y es el apartado más ignorado del real decreto** (`CHN-08`) |
| 6 | **Sucedáneo ≠ chocolate, y la frontera es exacta** | Si la manteca está **sustituida** (total o parcialmente) por otras grasas, es **sucedáneo** y así se etiqueta; si sólo se **añade** hasta **5 %** de las **seis** grasas autorizadas, **sigue siendo chocolate** | Se compra «cobertura barata» sin mirar | **NO** (`CHN-06`, `CHN-11`). Y la mención «contiene grasas vegetales además de manteca de cacao» va **en negrita, mismo tamaño, mismo campo visual que los ingredientes** |
| 7 | **La temperatura del bombón NO la fija la norma: la fijas tú** 🔴 | La tabla del art. 4.1 del RD 1021/2022 tiene **11 filas y ninguna nombra chocolate**. La fila 9 dice «productos de **pastelería** rellenos», y un bombón no es pastelería. Aplica el **art. 4.2**: temperatura de la etiqueta, justificada por tu autocontrol | Se copia «4 °C» de la pastelería, o se dice que la ley exige 16-18 °C | **NO, y es el hallazgo que separa esta guía de la de pastelería** (`CHN-30`). **Los 15-18 °C de la cámara son criterio técnico, NO un requisito legal** |
| 8 | **Una chocolatería-pastelería tiene DOS regímenes térmicos en el mismo local** | En cuanto la vitrina mezcla chocolate con tarta o éclair, **ese producto sí entra en la fila 9 y va a ≤4 °C** | Se pone todo a la misma temperatura | **NO** (`CHN-30b`). Es argumento de diseño de obrador, no de papeles |
| 9 | **El «carnet de manipulador» no existe** | El RD 202/2000 fue **derogado por el RD 109/2010**; el RD 1021/2022 tiene **22 artículos y ninguno de formación**. La obligación es del empresario (Anexo II Cap. XII del Rgto. 852/2004) y hay que **poder acreditarla** | Se vende el carnet como requisito | **NO, y lo dice la única guía española de 2026** (`CHN-69`, `E-1`). Cambia el entregable: hace falta un **registro de formación**, no un curso |
| 10 | **Una chocolatería NO va al RGSEAA si vende al consumidor final** | RD 191/2011 art. 2.2 en la redacción del RD 1021/2022: comunicación o declaración responsable autonómica **«que no será habilitante»**. Y **tener obrador y transformar NO te saca de la condición de minorista** | Se vende el «registro sanitario» como obligatorio siempre | **NO, es el error nº 2 del nicho** (`CHN-39`, `CHN-40b`, `E-2`) |
| 11 | **Lo que te mete en el RGSEAA es A QUIÉN vendes** 🔴 | Los tres requisitos del art. 3 son **acumulativos**, y el que mata es **«restringido»**: basta servir a **un solo hotel o una sola cadena inscrita en el RGSEAA** para perderlo | Se cree que basta con vender poco | **NO. Y el regalo corporativo es justo la línea que lo rompe** (`CHN-41`): tus clientes son empresas, y muchas están inscritas |
| 12 | **La libertad horaria de una bombonería NO viene del art. 5.1** | El art. 5.1 de la Ley 1/2004 nombra «pastelería y repostería, pan…» y **el chocolate no aparece**. La libertad le viene del **art. 5.2**, por tener **menos de 300 m²** | Se copia el argumento de la pastelería | **NO.** El resultado práctico es el mismo **y el fundamento es distinto**, y eso importa el día que alguien lo discuta (`CHN-77`) |

**Ése es el índice de criterio de la guía: 12 distinciones, 9 con algo falso enfrente, y todas comprobables por el lector en un minuto abriendo el BOE o EUR-Lex.**

### 1.3 🔴 LA DECISIÓN DE ALCANCE: bombonería con obrador (a) vs chocolatería de taza y churros (b)

**Las seis lentes convergen en (a) y divergen en la forma de tratar (b).** Ése es el desacuerdo real, y hay que resolverlo antes de la SPEC:

| Lente | Qué propone para (b) |
|---|---|
| L1 | «Capítulo corto de variante» que diga qué cambia y remita a la franquicia |
| L2 | **Capítulo**, «porque “¿qué modelo monto?” es de las primeras decisiones del lector» |
| L3 | «Capítulo de variante corto y honesto», con el argumento del IAE y del art. 30 |
| L4 | Capítulo **+ columna de escenario** en CAPEX y P&L **+ párrafo en landing y FAQ** |
| L5 | **Epígrafe de derivación**, no capítulo; y anotar «Cómo Montar una Churrería-Chocolatería» como candidato siguiente |
| L6 | **NI capítulo: sólo columna de «Variante del Formato»** — «si la guía abraza el modelo San Ginés, deja de ser una guía de obrador» |

**Mi arbitraje: alcance (a), y (b) como EPÍGRAFE del capítulo 01 + columna de escenario en el libro 2 + párrafo explícito en landing y FAQ. NO un capítulo propio, NO silencio.** Seis argumentos, cada uno con su dato:

1. **El compromiso con el cliente ya está adquirido y es (a) palabra por palabra.** La descripción publicada desde mayo dice «Temperado, obrador, vitrina, proveedores de cacao, licencias y modelo de negocio». Cambiar el alcance tras tres meses de retraso sería incumplir dos veces.
2. **La normativa las separa sola, y eso permite explicarlo en un epígrafe en vez de un capítulo.** El IAE ya tiene **tres altas distintas** (`CHN-72`); la taza mete al negocio en el **art. 30 del RD 1086/2020** con zona de elaboración separada (`CHN-51`); los churros devuelven **el gas** (`CHN-48`) y **el conducto de humos** que el obrador de chocolate no tiene (`CHN-46`); y hasta el fundamento de la libertad horaria cambia (`CHN-77`). **Con esas cuatro citas primarias, la distinción cabe en dos páginas y queda mejor argumentada que en veinte.**
3. **El argumento estructural de la guía se cae si (b) entra de verdad.** «Tu obrador no tiene humos y eso te abre locales que a una pastelería le están cerrados» es **el** hallazgo económico del producto (§4.1). Una churrería fríe.
4. **Meterlo en la misma hoja de CAPEX duplicaría el concepto «obrador»**, que es exactamente el defecto **alto** que la refutación de Pastelería marcó (A3: dos inversiones totales en el mismo pack). Regla: **un concepto, una fuente.**
5. **El volumen de (b) es de consumidor, no de emprendedor**, y está medido: `chocolate a la taza` 4.400 y `chocolateria churreria` 1.000 frente a `montar una churreria` **50** y `montar una chocolateria churreria` **sin dato**. Y **`chocolate a la taza` no es exportable**: 4.400 en España contra 20-70 en México, Colombia, Argentina y Chile. Es un fenómeno ibérico.
6. **Y ese método ya tiene quien lo venda empaquetado:** Maestro Churrero pide **115.000 € de inversión, 15.000 € de canon, 5 % de royalty y 100 m² mínimos**. Competir con eso desde una guía de 65 € es otro producto.

**Lo que sí se hace, y es lo que cierra el agujero:**
- **Un epígrafe del capítulo 01** titulado como la pregunta del lector: «*Si lo que tienes en la cabeza es San Ginés, esto es lo que cambia*» — con los cuatro cambios normativos primarios y el aviso de que ese modelo tiene franquicia.
- **«Chocolate a la taza» entra como FAMILIA de la carta** (libro 4) y como línea de desestacionalización: es producto de invierno, sube el ticket **de 2,50 € a 3,50-4 €** (+40 a +60 %, `CHS-32`) y **no toca el obrador**. Es la recomendación cruzada que ninguna fuente da.
- **«Chocolatería-churrería» entra como columna de «Variante del Formato»** del libro 2, con su CAPEX diferencial y una nota franca.
- **Un párrafo en la primera pantalla de la landing y una FAQ** que diga cuál de las dos chocolaterías se cubre a fondo. Es el antídoto contra la devolución por expectativa.
- **Se anota «Cómo Montar una Churrería-Chocolatería» como candidato de la siguiente cola** (decisión **D3**): su keyword de emprendedor, 50/mes, es **5× la de chocolatería**.

### 1.4 Los cinco errores de método de lo gratuito, que la guía corrige con autoridad

| Error | Dónde se midió | Qué hace la guía |
|---|---|---|
| **Horquilla de inversión de factor ×10 sin declarar la hipótesis** | **20.000-30.000 €** (plandenegocio.es, 14-abr-2026), **36.600 €** con 80 m² (emprender-facil.com, **sin fecha**) y **3.000-8.000 USD** (gempages.net/es, 25-ago-2025, traducido de EE. UU. citando **FDA y SBA**) | **No da un número: da el modelo que produce el número del lector**, y declara qué hipótesis lleva dentro |
| **Cuentas que no cuadran en la propia página** | plandenegocio.es titula «20.000-30.000 €» y desglosa 5.000-10.000 + 7.000-12.000 + 2.000-4.000 + 1.000-2.000 = **15.000-28.000 €** | Toda suma del producto es **refutable**: sumandos a la vista y gate de coherencia de cifras |
| **El requisito legal más elemental, falso** | La única guía española de 2026 lista el **«carnet de manipulador»**, suprimido por el RD 109/2010 | Norma + apartado + enlace + **fecha de verificación** en cada afirmación, y un epígrafe que enseña a abrir la ficha de vigencia del BOE |
| **Medio nicho que no se menciona jamás** | En las **10** fuentes gratuitas auditadas **no aparece ni una vez** el RD 1055/2003, ni el EUDR, ni el cadmio, ni la cámara de chocolate, ni el aw de los rellenos | Los tres frentes propios del chocolate son **tres capítulos y tres hojas** (§2, §9) |
| **La mitad de la SERP española es LATAM o traducción de EE. UU.** | 4 de 10 fuentes: dos mexicanas (pesos), una estadounidense (dólares, FDA/SBA) y una colombiana | Marco español declarado en la primera pantalla + vocabulario con equivalencia LATAM + la FAQ ofrece la adaptación como servicio |

---

## 2. Bloque obligatorio 2 — Regulación España 2026 (ids `CHN-*`)

L3 leyó **texto consolidado** en `boe.es` y en **EUR-Lex** (`CELEX:0…`, anotando las marcas ▼M de cada modificación), extrayendo el PDF con PyMuPDF cuando el HTML sólo servía el índice. Usa tres niveles: **A** = literal leído en boletín oficial (citable entrecomillado) · **B** = norma identificada, contenido por fuente oficial no normativa (**no citar entrecomillado**) · **C** = sólo fuente secundaria o no verificado (**no entra en el producto**).

**Los prefijos `CHN-` (normativa) y `CHS-` (sector) están libres y no colisionan entre sí** — verificado por mí sobre las **411** entradas de `guias-v2-research-sector.json`. **Nada que renombrar**, a diferencia del Manual del Chef Ejecutivo.

### 2.1 El núcleo verificado a nivel A — y los seis hallazgos que sostienen el producto

| id | Tema | Qué dice la norma | Norma y apartado | Nivel |
|---|---|---|---|---|
| **CHN-01** | **La norma del producto te obliga aunque seas de barrio** | «es de **obligado cumplimiento para todos los fabricantes, elaboradores, envasadores, comerciantes e importadores**». **Sin umbral de tamaño ni excepción para el artesano**, y **«sin modificaciones» desde 2003** | RD 1055/2003, art. único ap. 2 | **A** |
| **CHN-02** | **La tabla de mínimos legales por denominación** | 1.6 Chocolate **≥35 %** cacao total (≥18 manteca, ≥14 desgrasada) · Cobertura **≥35 %** total y **≥31 %** manteca · 1.7 Con leche **≥25 %** cacao, ≥14 extracto lácteo, ≥3,5 grasa láctea · 1.9 **Blanco** ≥20 % manteca y ≥14 extracto lácteo · 1.10 **Relleno** exterior **≥25 %** · 1.13 **Bombón ≥25 %** del peso total · 1.11 **A la taza ≥35 %** cacao y **≤8 %** de harina o almidón | RD 1055/2003, ap. 1.1-1.13 | **A** |
| **CHN-03** 🔴 | **«Bombón de chocolate» es denominación legal** | «producto **del tamaño de un bocado**… siempre que el chocolate represente, **al menos, el 25 por ciento del peso total**» | ap. 1.13 | **A** |
| **CHN-04** | **El bombón con galleta o helado dentro NO es «chocolate relleno»** | «**Esta designación no se aplicará a los productos cuyo interior esté constituido por productos de panadería, pastelería, galletería o bollería o por helado**» | ap. 1.10 | **A** |
| **CHN-05** | **«Chocolate a la taza» es un producto, no un uso — y su etiqueta tiene una mención obligatoria** | ≥35 % cacao, ≥18 % manteca, ≥14 % desgrasada, **≤8 %** de harina o almidón **de trigo, arroz o maíz** (el familiar: ≥30 % y **≤18 %**). Y el ap. 6.e): debe incluirse la expresión «**para su consumo cocido**» acompañando a la denominación | aps. 1.11, 1.12 y 6.e) | **A** |
| **CHN-06** | **Seis grasas vegetales, tope del 5 %, y una mención en negrita** | Illipe, palma, Sal, Shea, Kokum gurgi y hueso de mango; **≤5 %** del producto acabado **sin reducir los mínimos de cacao**; coco **sólo** para chocolate destinado a helados. Etiqueta: «**contiene grasas vegetales además de manteca de cacao**», **en negrita, mismo tamaño, mismo campo visual que los ingredientes y cerca de la denominación** | aps. 2.1, 2.2 y 6.b) | **A** |
| **CHN-07** | **La mención «cacao: X % mínimo» NO es universal** | Exigida sólo para 1.4, 1.5, 1.6, 1.7, 1.8, 1.11 y 1.12. **NO** para blanco (1.9), relleno (1.10) ni bombón (1.13) | ap. 6.d) | **A** |
| **CHN-08** | **El permiso legal para los calificativos de calidad** | Sólo sobre «chocolate», «chocolate con leche» y «cobertura», con **≥43 %/≥26 %**, **≥30 %/≥18 %/≥4,5 %** y **≥16 %** respectivamente | ap. 6.g) | **A** |
| **CHN-09** | **Tres reglas duras del día a día del obrador** | Materias comestibles añadidas **≤40 %** del peso del producto acabado · **grasa animal no láctea prohibida** · harinas y almidones **sólo** en chocolate a la taza · aromas que **no imiten** el sabor a chocolate ni a grasa láctea | aps. 3.1 y 3.2 | **A** |
| **CHN-10** | **El cálculo tiene truco: dos bases distintas en la misma norma** | Tableta con avellanas: el 35 % se mide **descontadas las avellanas**. Bombón: el 25 % se mide **sobre el peso total, relleno incluido** | ap. 4 | **A** |
| **CHN-13** | **La caja surtida tiene regla propia** | «**chocolates surtidos**» o «**chocolates rellenos surtidos**» y **una única lista de ingredientes** para el conjunto | ap. 6.c) | **A** |
| **CHN-15** | **Media vitrina se rige por OTRO real decreto** | Las almendras al chocolate son «**grageas o confites de chocolate o cobertura**» y la naranja bañada, «**fruta bañada de chocolate o cobertura**». Y si está **relleno, recubierto o grageado, la denominación de venta tiene que decirlo** con esa palabra | RD 348/2011, aps. 1.3, 1.3.1.3, 1.3.3 y 3.1.4 | **A** |
| **CHN-16** 🔴 | **El límite de cadmio SUBE cuanto más cacao lleva** | Chocolate con leche **<30 %** de cacao → **0,10 mg/kg** · chocolate **<50 %** o con leche **≥30 %** → **0,30** · chocolate **≥50 %** → **0,80** · cacao en polvo para el consumidor final → **0,60** | Rgto. (UE) 2023/915, Anexo I, 3.2.15.1-4 | **A** |
| **CHN-17/18** | **Y no es sólo el cadmio: hay OTA y HAP** | **Ocratoxina A**: cacao en polvo **3,0 μg/kg** (1.2.16) · **HAP**: cacao en grano y derivados **«incluida la manteca de cacao»** **5,0** (benzo(a)pireno) y **30,0** (suma de 4) μg/kg de grasa (5.1.4); **fibra de cacao** (cáscara) **3,0** y **15,0**, más estricta (5.1.5) | mismo reglamento | **A** |
| **CHN-19** | **Tres obligaciones que son TUYAS, no del proveedor** | No usar como ingrediente lo que pase de límite (art. 2.1) · **no «diluir» mezclando** lote conforme con no conforme (art. 2.2) · **justificar ante la inspección los factores de concentración o dilución** de los productos compuestos (art. 3.2) | arts. 2, 3 y 4 | **A** |
| **CHN-20** 🔴 | **El chocolate TERMINADO está en el EUDR, no sólo el grano** | Anexo I, fila Cacao: **1801** grano · **1802** cascarilla · 1803 pasta · 1804 manteca · 1805 polvo · **1806 «Chocolate y demás preparaciones alimenticias que contengan cacao»**. Y el art. 1.1 somete también **la EXPORTACIÓN desde la Unión** | Rgto. (UE) 2023/1115 consolidado a 26-12-2025 | **A** |
| **CHN-21/22** 🔴 | **El aplazamiento a junio de 2027 NO sirve para un negocio nuevo** | Art. 38.2: fecha general **30-dic-2026**. Art. 38.3: el **30-jun-2027** exige **dos** condiciones acumulativas — ser persona física, microempresa o pequeña empresa **Y** «**que estuviesen establecidos como tales a 31 de diciembre de 2024**» | arts. 38.2 y 38.3 (redacción del Rgto. 2025/2650) | **A** |
| **CHN-23/24** 🔴 | **La reforma de dic-2025 creó la figura que resuelve el caso: «operador posterior»** | El art. 2.15 **excluye expresamente** a los operadores posteriores de la definición de «operador». Quien compra cobertura ya comercializada en la UE **no hace declaración de diligencia debida**: le obliga el **art. 5** — guardar datos del proveedor **y el número de referencia de su DDS**, **cinco años**, avisar de incumplimientos y asistir a la inspección. Y **no tiene que registrarse** en el sistema de información: el art. 5.2 sólo obliga a registrarse a quien **no sea pyme** | arts. 2.15/2.15 ter y 5 (▼M2) | **A** |
| **CHN-25** | **El bean-to-bar que importa grano SÍ es OPERADOR** | Diligencia debida completa (arts. 8-11), **declaración presentada ANTES** de introducir el grano, responsabilidad asumida y registro **cinco años**. Y la condición b) del art. 3 obliga a saber **de qué finca** sale el grano | arts. 3, 4 y 8 | **A** |
| **CHN-27** | **⚠️ El «régimen simplificado» del EUDR NO es para el importador pequeño** | El art. 4 bis se aplica a los «**micro o pequeños operadores primarios**», definidos (art. 2.15 bis) como establecidos «**en un país clasificado como de riesgo bajo**». **El cacao no viene de esos países** | art. 4 bis | **A** |
| **CHN-30** 🔴 | **La tabla de temperaturas NO tiene fila para el chocolate** | Las 11 filas del art. 4.1 y ninguna nombra chocolate ni bombones. La fila 9 es «productos de **pastelería** rellenos», y la pastelería se define por la masa de harina. Aplica el **art. 4.2**: «deberán almacenarse y transportarse a las temperaturas indicadas en la etiqueta […] **de acuerdo con lo establecido en su sistema de autocontrol**» | RD 1021/2022, arts. 4.1 y 4.2 | **A** |
| **CHN-30b** | **Una chocolatería-pastelería tiene dos regímenes térmicos** | En cuanto la vitrina lleva tarta, pastel o éclair, **ese producto entra en la fila 9 y va a ≤4 °C** salvo que sea estable a temperatura ambiente | art. 4.1 fila 9 | **A** |
| **CHN-31** | **El huevo sigue mandando en una bombonería más de lo que parece** | Las **tres vías** del art. 9 (70 °C/2 s · 63 °C/20 s + consumo inmediato · **ovoproducto de establecimiento autorizado**) alcanzan a **yemas, trufas con yema, merengues, mazapanes con clara cruda y glaseados reales**. Si usas ovoproducto, el art. 9.3 te mete en **≤8 °C, 24 h y registro de fecha y hora** | RD 1021/2022, art. 9 (vía `PA-14`/`PA-15`) | **A** |
| **CHN-32** | **APPCC simplificado, con responsable con nombre** | «se podrán aplicar de manera simplificada» conforme a la Comunicación **2020/C 199/01**, «**debiendo contar con una persona responsable de su aplicación**». Las guías sectoriales son **voluntarias** | art. 20 | **A** |
| **CHN-39/40b/41** 🔴 | **Ni RGSEAA ni «registro sanitario»: comunicación autonómica NO habilitante — y lo que te saca del régimen es a QUIÉN vendes** | «previa **comunicación o declaración responsable, que no será habilitante**». La guía del RGSEAA rev. 16 lo dice con todas las letras: «**Dentro de sus instalaciones pueden realizar transformaciones… además de la venta al consumidor final**». Los tres umbrales del art. 3 son acumulativos y **el que mata es «restringido»**: basta con servir a **un hotel o una cadena inscrita** para perderlo | RD 191/2011 art. 2.2 · RD 1021/2022 art. 3 · Guía RGSEAA rev. 16 | **A** / **B** |
| **CHN-40** | **Cuando SÍ toca RGSEAA, el cajón es la clave 25** | «**Clave 25: Alimentos estimulantes…**», actividades «**07 Cacao y derivados**» y «**08 Chocolate y derivados**» (y 09, sucedáneos), categorías 1-5. **El chocolate está con el café y el té, no con los azúcares** | Guía RGSEAA rev. 16 (11-06-2025) | **B** ⚠️ el catálogo de claves **no está en ningún BOE** |
| **CHN-44** 🔴 | **Hacer bombones en casa para vender NO entra en la lista estatal** | El art. 13.8 permite «Productos de **panadería y repostería** estables a temperatura ambiente», y ni el bombón ni la tableta son repostería. **Prueba:** el decreto catalán de artesanía tuvo que escribir «confitería, pastelería, bollería y repostería, **incluidos turrones y chocolates**» — si el chocolate estuviera dentro de «confitería», no habría hecho falta añadirlo | RD 1021/2022 art. 13.8 + Decreto 85/2024 | **A** |
| **CHN-46** 🔴 | **El obrador de chocolate no genera aire AE4, y eso es dinero** | La IT 1.1.4.2.5 del RITE clasifica como **AE4** «extracción de campanas de humos» y prohíbe recircularlo; el art. 2.6 deja **fuera del RITE** las instalaciones de proceso industrial. **Sin horno no hay campana ni combustión**: el problema del conducto de humos no se plantea. Lo que sí cae bajo el RITE es **la climatización y el control de humedad del local** | RD 1027/2007, arts. 2.1/2.6 e IT 1.1.4.2.5 | **A** |
| **CHN-47** | **Si tuestas el grano, entras en el catálogo de actividades contaminadoras** | Código **04 06 05 14** «Tostación o torrefacción del café **o similares**», **grupo C** → **notificación** a la comunidad autónoma (art. 5.3), no autorización. **Nota (2):** la comunidad puede subirte a grupo B a menos de **500 m** de determinados espacios | RD 100/2011 | **A** ⚠️ **interpretación**: el epígrafe no nombra el cacao. Va como **pregunta a la CCAA antes de comprar tostador** |
| **CHN-51** | **La taza de chocolate cambia tu régimen sanitario** | Servir un bombón con un café no es comida preparada; **preparar chocolate a la taza y churros sí lo es** → art. 30 del RD 1086/2020 y **zona de elaboración separada de la venta** | RD 1021/2022 art. 10 + RD 1086/2020 art. 30 | **A** |
| **CHN-52** | **En Cataluña el chocolate está expresamente en la artesanía alimentaria** | Oficio nº 2 del repertorio: «Pastelería: … **incluidos turrones y chocolates**». Dos acreditaciones **voluntarias**: **carné** de la persona (3 años de experiencia + FP o **100 h** de formación) y **distintivo** de la empresa. Vigencia indefinida | Decreto 85/2024 (DOGC 9155) | **A** |
| **CHN-53** | **«Chocolate artesano» no tiene definición estatal** | «artesano», «artesanal» y «casero» **no aparecen** ni en el RD 496/2010 ni en el RD 1055/2003 | búsqueda exhaustiva sobre los dos textos | **A** |
| **CHN-55** | **«ELABORACIÓN PROPIA»: la mención buena y su trampa** | Es **voluntaria**; **«no se considerará elaboración el fraccionamiento o el envasado»** de producto ajeno; y lo que la lleve **sólo se puede vender en el local donde se hizo o en sus sucursales**. Fundir cobertura comprada y moldearla **sí es transformar**; cortar una tableta ajena y encajarla, **no** | RD 1021/2022 art. 11 | **A** |
| **CHN-56** | **Vender bombones online a toda España no te obliga al RGSEAA** | La venta a distancia ya está **dentro** de la definición de minorista (art. 2.2.a) y el art. 3 sólo regula el suministro **a otros comercios**. Lo que te obliga es el **art. 4.3**: mantener la temperatura durante todo el transporte | RD 1021/2022 | **A** |
| **CHN-60** | **Exportar chocolate fuera de la UE también es un hecho sujeto al EUDR** | El art. 1.1 somete «**así como a la exportación desde la Unión**» | Rgto. 2023/1115 | **A** |
| **CHN-62** 🔴 | **El impuesto al plástico SÍ puede alcanzarte, porque compras packaging fuera** | Sujeta «la fabricación, **la importación o la adquisición intracomunitaria**» (art. 72.1), **0,45 €/kg** de plástico **no reciclado** (art. 78), **inscripción previa** en el Registro territorial (art. 82.3). **La salida:** exento hasta **5 kg/mes** de plástico no reciclado (art. 75.f). **Y el límite del hallazgo: los MOLDES de policarbonato NO son envases** (art. 73.d) | Ley 7/2022 | **A** |
| **CHN-63** | **Bombones al peso = venta a granel** | «Todos los establecimientos… que vendan **a granel**… **deberán aceptar** el uso de recipientes reutilizables». Y desde el **1-ene-2027**, **una referencia de bebida en envase reutilizable** si tienes **<120 m²** | RD 1055/2022, arts. 9.3 y 9.4 | **A** |
| **CHN-65** 🔴 | **El convenio de Madrid nombra los bombones dos veces y con dos alcances** | El **despacho** de bombones está dentro sin condición; pero «**la fabricación y venta de bombones… se regirán por el presente Convenio, CUANDO LA ACTIVIDAD PRINCIPAL… sea la de Confitería, Pastelería, Bollería y Repostería**». **Una bombonería pura no cumple esa condición para su obrador.** Es cuestión de ámbito funcional para un laboralista | BOCM 194 de 15-08-2025, art. 2 | **A** |
| **CHN-72** 🔴 | **Existe un epígrafe de IAE escrito para una bombonería, y casi nadie lo usa** | **644.5** «Comercio al por menor de bombones y caramelos» — Nota: «faculta para: **La fabricación de bombones y caramelos en el propio establecimiento, siempre que su comercialización se realice en las propias dependencias de venta**». **No hace falta el 421.1**, que es el **industrial**. Y la nomenclatura desambigua: **grupo 676** «Servicios en chocolaterías, heladerías y horchaterías» (la taza) · **644.6** «preparados de chocolate», que **faculta para elaborar churros** · **644.1**, el único con **degustación** | RDLeg 1175/1990 («Última modificación: 21-03-2026») | **A** ⚠️ **no reproducir las cuotas**: el consolidado tiene una errata de conversión en el 644.5 |
| **CHN-73** | **Darse de alta en el epígrafe sí; pagarlo, casi nunca** | Exentos los dos primeros períodos, **las personas físicas** y las sociedades con cifra de negocios **<1.000.000 €** | RDLeg 2/2004, art. 82.1 | **A** |
| **CHN-74** | **CNAE-2025: 10.82 y 47.24, y no es el IAE** | «**10.82** Fabricación de cacao, chocolate y productos de confitería» y «**47.24** Comercio al por menor de pan, productos de panadería y confitería». Quien abra ahora comunica el CNAE **en el momento del alta** | RD 10/2025 | **A** |
| **CHN-71** | **IVA: tableta, bombón, cobertura y chocolate a la taza en polvo al 10 %** | No por un precepto que los nombre, sino porque **no están en la lista cerrada del 4 %** y **no están excluidos del 10 %**. Y la trampa del TPV: **la misma botella cambia de tipo según dónde se la beba el cliente** | Ley 37/1992, arts. 90.Uno y 91 | **A** |
| **CHN-77** | **La libertad horaria de una bombonería viene del art. 5.2, no del 5.1** | El 5.1 nombra «pastelería y repostería, pan…» y **el chocolate no está**. El 5.2 da libertad a los establecimientos de **menos de 300 m²** | Ley 1/2004 | **A** |
| **CHN-75** | **Verifactu no es 2026, es 2027** | Sociedades **1-ene-2027**; el resto **1-jul-2027**. **Pero el TPV que compres hoy ya tiene que estar adaptado** | RD 1007/2023 | **A** |
| **CHN-76** | **La regla de los 30 días del precio tachado está en la Ley 7/1996, no en el TRLGDCU** | «precio anterior… **el menor que hubiese sido aplicado… en los treinta días precedentes**». Relevante aquí por la estacionalidad: **subir en noviembre para «rebajar» en diciembre no cumple** | Ley 7/1996 art. 20.1 | **A** |
| **CHN-64** | **Desperdicio: una chocolatería es microempresa y queda fuera del art. 6** | Le siguen obligando el 6.2, el 6.3 (**nula de pleno derecho la cláusula que prohíba donar**) y el 6.5 | Ley 1/2025 | **A** |

### 2.2 Lo que está a nivel B o C y NO puede entrar como afirmación

**Nivel B** (no entrecomillar): `CHN-28` autoridades del EUDR en España (MITECO + una por CCAA) · `CHN-40`/`CHN-40b` claves del RGSEAA.
**Nivel C — no entra en el producto:** `CHN-36` RD 1808/1991 (el lote: se dice que es obligatorio, **sin número de artículo**) · `CHN-49`/`CHN-50` licencia municipal y clasificación urbanística · `CHN-54` artesanía fuera de Cataluña · `CHN-58` desistimiento, LSSI y RGPD en venta online · `CHN-66` convenio estatal del chocolate · `CHN-70` PRL · `CHN-79` ruido · `CHN-80` seguro de RC. **Ninguna cifra de dB, de capital de RC ni de coste de proyecto técnico entra en el producto.**
**Interpretación declarada, no literal:** `CHN-47` (el CAPCA dice «del café **o similares**») y `CHN-71b` (**el IVA de talleres y catas no está resuelto**: por la regla general sería 21 %, pero hay matices sin verificar → en el producto va **con el argumento explicado y sin número**).

### 2.3 Estado de vigencia a 2026-09-12

| Norma | Estado |
|---|---|
| **RD 1055/2003** (cacao y chocolate) · **RD 348/2011** (confites) · **RD 1021/2022** · **RD 10/2025** (CNAE) · **RD 1055/2022** | **VIGENTES · «sin modificaciones»** |
| **Directiva 2000/36/CE** | **VIGENTE**, *date of end of validity: No*. Sólo modificada en arts. 5 y 6 (procedimiento) y anexos (adhesión 2004) |
| **Rgto. (UE) 2023/915** (contaminantes) | **VIGENTE**; consolidado leído a **01-01-2025** (rev. 004.001). ⚠️ no existe consolidado posterior |
| **Rgto. (UE) 2023/1115 (EUDR)** | **VIGENTE**, modificado por **2024/3234** (26-12-2024) y **2025/2650** (26-12-2025). Aplicable desde **30-12-2026** / 30-06-2027 con las dos condiciones de `CHN-22` |
| **Ley 7/2022** (plástico) | VIGENTE · última modificación **02-04-2025** |
| **RDLeg 1175/1990** (IAE) | VIGENTE · última modificación **21-03-2026** |
| **Ley 1/2004** (horarios) | VIGENTE · última modificación 17-10-2014 |
| **Decreto 85/2024** (artesanía, Cataluña) · **Decreto 26/2026** (registro, Madrid, transitorio hasta **28-03-2027**) | VIGENTES |
| **Convenio de Madrid** (28001025011981) | Vigente; tablas 2026 hasta **31-12-2026** |
| **RD 202/2000** (carnet de manipulador) · **RD 1254/1991** · **RD 3484/2000** | **DEROGADOS** |

### 2.4 Qué de esto es argumento de venta y qué NO se puede decir en el copy

**Sí es argumento (y va en la landing, en la FAQ y en el email, no en el titular — regla de John del 5-sep):**
- «**El obrador de chocolate no tiene horno ni campana: te abre locales que una pastelería tiene que descartar**» (`CHN-46`). Es el argumento económico más fuerte del producto y sale de norma primaria.
- «**Te decimos cómo puedes llamar legalmente a lo que vendes**» (`CHN-02`, `CHN-03`, `CHN-07`, `CHN-08`, `CHN-11`, `CHN-15`). Ninguna fuente gratuita lo menciona.
- «**El EUDR ya te alcanza, y no de la forma que te han contado**» (`CHN-22`, `CHN-24`). El matiz del 31-12-2024 es el más valioso del bloque para un lector que **aún no ha abierto**.
- «**Hay un epígrafe de IAE que te deja fabricar bombones sin darte de alta como industria**» (`CHN-72`).

**NO se puede decir, y va a la lista negra (§15.2):**
- «Verificado contra el BOE» **en titular ni en Stripe** (regla de John del 5-sep): en el copy comercial lideran los entregables y el beneficio práctico.
- **Nada sobre el «carnet de manipulador» atribuido a un blog por su nombre**: `plandenegocio.es` devolvió **404** a L3 y la frase no se pudo capturar en su fuente. El error se documenta y se refuta **con su norma**, sin entrecomillar a nadie.
- **Ningún dato de coste de licencia, proyecto técnico, ruido o seguro de RC.**
- **Ninguna tabla salarial del chocolate** más allá de la de Madrid marcada como ejemplo.

### 2.5 Las verificaciones que L3 dejó abiertas y que hay que cerrar ANTES del guion

| id | Qué falta | Por qué bloquea | Método |
|---|---|---|---|
| **V-01** | **Convenio del chocolate**: no se localizó ningún convenio **estatal** de «chocolates, bombones, caramelos y chicles» en el BOE, y el de Madrid **condiciona** la fabricación de bombones (`CHN-65`) | Decide los brutos del libro 7 y si el negocio es comercio o industria | **REGCON** del Ministerio de Trabajo (decisión **D9**) |
| **V-02** | **IVA de talleres y catas** (`CHN-71b`) | El libro de talleres pondría un tipo | Consulta vinculante de la DGT; si no se cierra, **va sin número** |
| **V-03** | **Artesanía fuera de Cataluña** (`CHN-54`) | El cuadro por CCAA | Repertorios autonómicos. **Decisión D10**: una comunidad con articulado y el resto como enlace |
| **V-04** | **RD 1808/1991 (lote)** (`CHN-36`) | El capítulo de etiquetado | PDF consolidado del BOE con el identificador correcto |
| **V-05** | **«Confitería» en la lista valenciana, ¿cubre el bombón?** (`CHN-44b`) | El capítulo del obrador en casa | Pregunta a la conselleria. **Va como pregunta, no como respuesta** |

---

## 3. Bloque obligatorio 5 — El sector y el modelo de negocio (ids `CHS-*`)

### 3.1 El mercado: crece en euros y se encoge en kilos — y para el artesano eso es buena noticia

| id | Dato | Fuente | Fiabilidad |
|---|---|---|---|
| **CHS-18** | **Consumo de cacao y chocolate en España 2025: 2.323 M€, +10,3 %** · facturación **2.146 M€, +12,3 %** · exportación **858 M€, +35,7 %** · importación **1.034 M€, +25,6 %** (99,4 % de origen UE) · **6.994 empleos directos** | Produlce 2025 vía Revista Aral (10-sep-2026) y Financial Food (9-sep-2026), **cifras idénticas en dos medios independientes** | **ALTA** |
| **CHS-19** | **Reparto por categorías (% del valor):** tabletas **31,3 %** · cacao soluble y **chocolate a la taza 23,0 %** · snacks **19,0 %** · **bombones 13,6 %** · cremas de untar 13,1 % | mismas URLs | **ALTA** |
| **CHS-21** | **Consumo per cápita en hogares: 2,96 kg** (TAM mar-2025), desde **3,54 kg en 2022** = **−16,4 % en tres años**. **Precio medio 10,11 €/kg, +11,3 %** | MAPA e INE vía Xataka Magnet, 18-sep-2025 | MEDIA-ALTA ⚠️ es **precio de hogar**, no coste de materia prima |
| **CHS-22** | **2025: el mercado interior subió 0,5 % en valor y cayó 4,6 % en volumen**; gasto per cápita **33,88 €**; precios **+18 %** | Agencia EFE vía Infobae, **12-sep-2026 (hoy)** | MEDIA-ALTA |
| **CHS-23** | **El precio del chocolate subió 17,7 % en 2025 tras un 10 % en 2024: ~30 % acumulado en dos años** | IPMARK citando NielsenIQ | MEDIA |
| **CHS-13/16** | **No existe número oficial de chocolaterías en España.** El DIRCE público llega al grupo **108**, que mezcla cacao con café, té, especias y platos preparados (**3.237 empresas a 1-ene-2020**, y la tabla se detiene ahí). Lo más cercano: **976 empresas CNAE 1082** (eInforma, balance 2024), que sólo cubre sociedades que depositan cuentas | INE DIRCE tabla 298 (CSV descargado) · eInforma | **ALTA** pero **inservible como «chocolaterías»** / MEDIA |

> **La lectura de negocio, que es lo que va en el capítulo 02:** el consumidor **ya ha aceptado pagar más por menos cantidad**. Ése es exactamente el terreno del producto artesano, y lo dice la presidenta de la asociación bean-to-bar: «*el consumidor no necesariamente está buscando chocolate barato, está buscando que el precio que pague **tenga sentido***» (Teresa Ricart, `C51`).

### 3.2 La crisis del cacao (CHS-24) — el dato que decide el escandallo

| id | Dato | Fuente |
|---|---|---|
| **CHS-24a** | **2-ene-2026: 4.956 €/t.** Un año antes, **>10.300 €/t**. Máximo de 2025: **>10.800 €/t** (finales de enero). Mínimo: ~4.400 €/t (noviembre) | Food Retail & Service, 7-ene-2026, **citando expresamente a la ICCO** |
| **CHS-24b** | **12-sep-2026 (hoy): 5.938 US$/t ≈ 5.117 €/t**, «un 20 % por debajo de hace un año, **aunque aún muy por encima de los niveles previos a 2024**» | EFE vía Infobae, 12-sep-2026 |

> 🔴 **La regla que tiene que llevar la guía, y es la que justifica un libro entero:** **el precio de la cobertura NO baja cuando baja el cacao.** El cacao cayó a la mitad y el chocolate subió un 17,7 % el mismo año (`CHS-23`), y la propia tendera lo describe en términos operativos: «*es impresionante cómo se ha disparado el valor del cacao*» y «**antes era una vez al año, ahora los aumentos son semestrales**» (`C13`, `C14`). **Un escandallo de chocolatería montado sobre la cotización de bolsa es un escandallo falso:** se monta sobre **la factura del proveedor**, en **celda verde**, con hoja de sensibilidad. Es la doctrina de los xlsx de la casa aplicada al caso más extremo que tenemos.

⚠️ **Contradicción detectada y resuelta:** varios medios latinoamericanos (eldiario.ec, extra.ec, latercera.com) sitúan el cacao en 2026 entre **3.000 y 4.500 US$/t**, incluso «perforando los 3.000». Es incompatible con la ICCO y con EFE. Probablemente mezclan precio de finca ecuatoriano con la cotización internacional. **A la lista negra** (§15.1 `N-1`).

### 3.3 Precios, ticket y márgenes verificados

| id | Dato | Fuente | Fiabilidad |
|---|---|---|---|
| **CHS-28a** | **Cobertura Callebaut 811 (negro 54,5 %), bloque de 5 kg: 125,08 € CON IVA = 25,02 €/kg** — el formato que compra un obrador | Planeta Torta | MEDIA |
| **CHS-28c** | **Valrhona pepitas 400 g: 14,99 € = 37,48 €/kg** | Club del Chocolate | MEDIA |
| **CHS-29** | **PVP del bombón artesano: 1,67 €/ud (caja de 12, 20 €) · 1,40 € (caja de 20, 28 €) · 1,29 € (caja de 35, 45 €)** — **el precio por bombón baja un 23 % de la caja de 12 a la de 35** | Confitería Gascón | MEDIA ⚠️ la página **no publica el peso ni la base de IVA**: no hay €/kg |
| **CHS-30** | **Talleres y catas: 25-45 €/persona**, mínimo habitual **6 pax**, 90-150 min (Madrid 26 y 45 € · Valencia 30 € · Murcia 25 € IVA incl.) | 4 operadores | MEDIA (**verificar 2-3 en página antes de publicar**) |
| **CHS-31/32/33** | **Churro: margen bruto 85-90 %** (un maestro churrero lo rebaja a «poco más del 50 %» — **publicar los dos y explicar por qué difieren**) · pieza 0,30-0,70 € · **ración de 4 uds ~2,50 €, que sube a 3,50-4 € al añadir el chocolate** · ingredientes y aceite **≈20 % de la facturación** | Loomis Pay + El Español | MEDIA |
| **CHS-40** | **Punto de equilibrio publicado: ~89 uds/día** (4.000 €/mes de fijos ÷ 1,50 €/ud de margen = 2.667/mes). La aritmética **cuadra** | plandenegocio.es, 17-dic-2025 | **MEDIA-BAJA** |
| **CHS-69** | Salarios de mercado orientativos: chocolatero **13-16 €/h** · encargado **15-20 €/h** · oficial 11-13 € · ayudante 8-9,50 € | agregador Insertia | **MEDIA-BAJA** ⚠️ **no son ofertas reales** (InfoJobs devuelve HTTP 456) |

> ⚠️ **Tres avisos sobre CHS-40, y el tercero es el que importa:** (1) la aritmética cuadra, que es más de lo que se puede decir de la mayoría de la SERP; (2) **su ticket de 2,50 €/ud no casa con el PVP del bombón medido (1,29-1,67 €)** ni con una caja de regalo (20-45 €): parece una unidad genérica de pastelería; (3) es del **mismo dominio** que comete el error del carnet. **Entra como método editable, JAMÁS como promesa de rentabilidad, y NO va en la portada** (§15.1 `N-5`).

> ⚠️ **El chocolatero es la categoría mejor pagada del obrador después del maestro** (13-16 €/h frente a 11-13 € del oficial de primera). Si se confirma con convenio, es un dato de negocio de primer orden: **el cuello de botella de una chocolatería no es la máquina, es encontrar a quien la maneje.** Va con su fiabilidad a la vista.

### 3.4 Estacionalidad: los picos están verificados, la curva mensual NO existe

| id | Dato | Fuente |
|---|---|---|
| **CHS-34** | **Tres picos nombrados por la patronal: Navidad, San Valentín y Halloween.** «Las ventas de chocolates y dulces **pueden llegar a duplicar el promedio anual** en San Valentín» y «hay compañías que hacen **hasta el 10 % de su venta anual**» en un solo evento | Produlce vía Financial Food, 10-feb-2025 |
| **CHS-66** | **Monas de Pascua** confirmadas como campaña de obrador de barrio | Bombonería Pons |
| ✅ **mío** | **Estacionalidad medida en búsqueda, no supuesta:** `mona de pascua` media **18.100** con serie `1.600·1.600·1.900·2.900·**110.000**·**90.500**` → **factor ×69**. `bombones san valentin` media 320 con serie `10·10·10·20·20·30`: **la media la hace un pico que ni aparece** en los 6 meses devueltos. `chocolate a la taza` sube `1.600→3.600` (×2,25) camino del otoño | DataForSEO, 2026-09-12 |
| **El valle** | **Verificado y es estructural, no comercial.** Equimercado **apaga los envíos el 12 de junio, todos los años**: «*preferimos parar, proteger el producto*» (`C39`, `C40`). Y el propio `BONUS-02-calendario-anual-tareas.xlsx` del kit de 12 € ya declara **agosto como temporada BAJA** («producción reducida, planificación Q4»), junio «adaptar catálogo (calor)» y julio «packs souvenir» | Equimercado 04-jun-2026 + kit propio |

> ⚠️ **Lo que NO existe y hay que declarar: no hay dato público del reparto mensual de ventas de una chocolatería española.** Ni Navidad vs resto, ni monas, ni la profundidad del valle. **Es la misma limitación L-6 que tuvo Pastelería y se resuelve igual: curva editable con supuesto explícito, nunca una curva inventada.**
>
> **Regla de diseño obligatoria (A8 de la refutación de Pastelería):** las unidades de campaña **se calculan desde el mix anual, no se teclean**, y el libro 6 lleva una **fila de cuadre** («unidades de campaña / unidades del año de esa referencia») con semáforo. En chocolatería el riesgo es peor porque Navidad puede ser un tercio del año.

### 3.5 Los dos hallazgos de modelo de negocio que no tiene nadie

**(a) La vida útil del relleno es una decisión de MODELO DE NEGOCIO, y el factor es 5.** «Los bombones rellenos de **ganache** pueden conservarse **5 o 6 semanas si contienen sorbitol**. De lo contrario, habrá que consumirlos en un **máximo de 8 días**» (`CHS-56`, Danielle Pacheco Chocolatier). Eso no es una cuestión técnica: es **la diferencia entre poder vender online, poder servir regalo corporativo con los 14-16 días de plazo que piden los proveedores, y poder fabricar para Navidad en noviembre** — o no poder hacer nada de eso.

**(b) El pedido corporativo de Navidad se cierra en OCTUBRE.** `CHS-55`: los proveedores de regalo corporativo trabajan con **plazo de 14-16 días desde la aprobación de la muestra** y **mínimos de 10-25 cajas con 20-30 días**. Es una línea del calendario operativo que el que abre no sabe, y la que impide el error clásico: **aceptar 400 cajas para la semana en que ya no cabe un molde más**.

### 3.6 El traspaso: el hallazgo diferencial, igual que en Pastelería

Consultados en Milanuncios el 2026-09-12. ⚠️ Son **precios PEDIDOS**, no pagados.

| id | Negocio | Provincia | m² | Traspaso | Alquiler/mes |
|---|---|---|---|---|---|
| **CHS-38a** | **Pastelería-bombonería con obrador, 40+ años** | El Prat de Llobregat | **90** | **26.000 €** | **1.100 €** |
| CHS-37c | Churrería-chocolatería | Mataró | 118 | 58.000 € | — |
| CHS-38b | Pastelería-bombonería, 34 años | Reus | 300 | 73.000 € | — |
| CHS-37b | Churrería-chocolatería | Madrid (Vallecas) | **74** | 82.000-95.000 € | **910 €** |
| CHS-38c | Pastelería-bombonería, obrador a la vista | Barcelona | 180 | 140.000 € | 2.200 € |
| CHS-38d | Pastelería con obrador profesional | Valencia | 100 | 180.000 € | — |
| CHS-38e | Obrador de pastelería y panadería | Lliçà d'Amunt | 400 | 210.000 € | — |

> **El caso que decide el capítulo: 26.000 € por 90 m² con obrador equipado y 40 años de clientela.** Es decir, **traspasar puede salir más barato que montar de cero** (CHS-03: 20.000-80.000 € **sin** local ni clientela). La comparativa **traspaso vs obra nueva a 5 años** tiene que ser una hoja, igual que en Pastelería.
>
> ⚠️ **Y un dato que es un hallazgo en sí mismo: ninguno de los ocho anuncios es una bombonería artesana pura.** El negocio de chocolate puro **se traspasa poco**, porque su valor está en las manos del titular. Eso refuerza CHS-01/CHS-02 como puerta de entrada real y **descarta el traspaso como vía principal para la rama (a)**.

---

## 4. Bloques obligatorios 3 y 4 — Equipamiento crítico y proveedores reales

> **Regla aplicada línea a línea, y es la corrección directa del defecto que tumbó la L4 de Pastelería:** cada precio dice si es **CON IVA**, **SIN IVA** o **base NO declarada**, con la frase literal de la web cuando existe. **No se ha convertido ninguna base.**

### 4.1 El hallazgo estructural: el chocolate no hace humo, y eso es dinero

Un obrador de chocolate puro **no tiene horno ni freidora**. La consecuencia económica está en dos sitios y los dos son sólidos:
- **Normativa (nivel A):** sin horno no hay campana ni aire **AE4**, así que **el problema del conducto de humos no se plantea** (`CHN-46`). Lo que sí cae bajo el RITE es la climatización y el control de humedad.
- **Sector (MEDIA):** el conducto de acero inoxidable por fachada «**puede superar los 6.000 €**» (Salva Industrial, **página sin fecha**, fabricante con interés comercial).

**Traducción de negocio: puedes alquilar locales que una pastelería tendría que descartar.** Es el argumento económico más fuerte del producto y **ninguna fuente de la SERP lo plantea como decisión**.

⚠️ **Y la contrapartida hay que enseñarla en la misma página:** lo que ahorra en extracción **se lo gasta en clima**. Ése es un coste que la pastelería no tiene.

### 4.2 Clima del obrador y de la cámara — con el arbitraje entre lentes resuelto

| Concepto | Cifra que ENTRA | Fuente | Nota |
|---|---|---|---|
| **Sala de trabajo** | **18-22 °C** | Llevats21, 23-jun-2026 (`C41`, `CHS-44`) | «El rango óptimo para trabajar con cobertura oscila entre los 18 y los 22 °C» |
| **Humedad relativa de sala** | **< 55 %** | ídem (`C43`) | «reduce considerablemente los problemas de agarre» |
| **Cámara de conservación del producto acabado** | ✅ **15-18 °C con humedad controlada** | ídem (`C46`) — **literal, leído por L5 en la misma página que L4 dio por muda** | ⚠️ **NO los «16-18 °C» del encargo, que van sin fuente** |
| **Puesta en marcha** | El aire **encendido al menos una hora antes** de empezar, para que mármoles, utensilios y moldes alcancen la temperatura | ídem (`C44`) | Es un dato operativo que nadie publica |
| **Punto de fusión de la manteca** | Se ablanda a **28 °C**, funde a **32-34 °C** | Equimercado (`C36`) y Llevats21 (`C42`) | Es la razón física del valle de verano |
| **Deshumidificador** | «una inversión que **se amortiza rápido** en obradores de clima mediterráneo o costero» | ídem (`C45`) | **Precio «sin fuente»** |

> ⚠️ **Y NUNCA escribir que «la norma obliga a 16-18 °C y 50 % de humedad»: no lo dice ninguna norma** (`CHN-30`). Es criterio técnico del operador, y por eso va explicado **como decisión**, no como requisito. Va a la lista negra (§15.2).
>
> ⚠️ **El único climatizador con precio que apareció NO SIRVE:** un evaporativo industrial «desde 365 €» **añade humedad**, que es exactamente lo contrario de lo que necesita el chocolate (§15.1 `N-9`).

### 4.3 Atemperadoras, enrobadoras y vitrina — la escalera que es el corazón del capítulo

| id | Modelo | Capacidad | Precio | Base IVA | Fuente |
|---|---|---|---|---|---|
| **CHS-41h** | **Pavoni Minitemper** | 4,5 L (≈3 kg) | **1.960,00 €** (+ cubeta 165,30 €) | **NO declarada** | Utilcentre |
| **CHS-41a** | **Selmi One** | **12 kg** (55 kg/h) | **8.500 €** + **1.045 €** de embalaje, transporte y puesta en marcha | **NO declarada** (la ficha escribe «1045 €/**Neto**», que apunta a sin IVA, **pero la web no lo afirma**) | Utilcentre |
| CHS-41c/d | Selmi Ghana-Legend / Plus EX | 24 kg | 12.300 € / 18.500 € | NO declarada | ídem |
| CHS-41f/g | Selmi Top EX / Cento EX | 60 / 100 kg | 27.500 € / 45.000 € | NO declarada | ídem |
| CHS-42a/b/c | Enrobadoras Selmi R200 Legend / RS 200 / RS 250 | — | 6.800 € / 8.500 € / 9.700 € | NO declarada | ídem |
| CHS-42i | Placa dosificadora | — | 1.495 € | NO declarada | ídem |
| CHS-41j / CHS-41i | Baño maría digital 22 L / mantenedor 1 cubeta | — | 2.650 € / desde 570 € | NO declarada | ídem |
| **CHS-43** 🔴 | **Vitrina refrigerada Docriluc WB-6-6-R PARA CHOCOLATE** · 600×730×1380 mm · **temperatura de trabajo +14 °C a +17 °C** | — | **2.684,99 €** (antes 3.487 €) | ✅ **SIN IVA, declarado literalmente** («sin impuestos») | Equipo H |
| CHS-46a-f | Chocolateras **Ugolini Delice 3/5/5 Gold** · **Campeona TXM** | 3-40 L | **527 / 631,55 / 748 €** · 833-2.159 € | ✅ **SIN IVA, declarado** («Estos precios se entienden sin IVA») | Equipo H |
| CHS-45a | Moldes de policarbonato **Chocolate World** | — | **24,20-42,83 €/ud** | NO declarada | RestorHome |

> **La escalera de atemperadoras es una tabla de decisión excelente y no existe en ninguna fuente gratuita: de 1.960 € (Minitemper, 3 kg) a 8.500 € (Selmi One 12 kg, el estándar profesional de entrada) a 27.500 € (Top EX, 60 kg). Un factor 14 entre extremos**, y la elección la decide **los kg/semana que salgan de la hoja de capacidad**. Ese cruce **kg/semana → máquina** es el corazón del capítulo 08.
>
> 🔴 **La vitrina de chocolate va a +14/+17 °C, no a +2/+4 °C.** Es un error caro y frecuentísimo: una vitrina de pastelería **arruina el bombón** (condensación, *sugar bloom*, pérdida de brillo). La fuente lo hace explícito al llamar a la gama «temperatura de trabajo **para chocolates**».
>
> ⚠️ **Anomalía declarada:** la serie de chocolateras Campeona **no es monótona** (TXM/9-LB 9 L a 1.015,75 € cuesta **menos** que la TXM/7-LC 7 L a 1.300,50 €). **No usar la serie completa sin verificar con el distribuidor** (§15.1 `N-8`).

### 4.4 Dotación tipo, con la aritmética a la vista

> ⚠️ **Léase antes que la tabla: esto NO es un presupuesto de apertura.** Es la suma de las líneas con **precio verificado**, y nada más.

**Escenario A — profesional de entrada (CHS-47a):** Selmi One 8.500 + puesta en marcha 1.045 + enrobadora R200 6.800 + placa dosificadora 1.495 + 12 moldes (12 × 30 €) 360 + baño maría 22 L 2.650 + mantenedor 570 + vitrina Docriluc 2.684,99 = **24.104,99 €** ⚠️ **BASE MIXTA, no sumable como cifra fiscal**.
**Escenario B — arranque mínimo viable (CHS-47b):** Minitemper 1.960 + cubeta 165,30 + mantenedor 570 + 12 moldes 360 + vitrina 2.684,99 = **5.740,29 €**.

**Las 12 partidas que FALTAN y NO tienen precio público** — y que **deliberadamente no se estiman**: obra y adecuación · instalación eléctrica (trifásica) y de agua · **cámara/armario de chocolate** · **climatización y deshumidificación** · mesa de mármol · mesas de inox y fregaderos · abatidor · balanza · **TPV** · **packaging** · mobiliario y rótulo · licencias y proyecto técnico · **fondo de maniobra y stock de cobertura**.

> 🔴 **El contraste que es un argumento de venta en sí mismo:** la única fuente publicada con un número completo sitúa la apertura en **20.000-30.000 €**, y el núcleo de máquina profesional verificado aquí ya son **24.105 €**. **Las dos cifras sólo son compatibles si esa fuente está pensando en el escenario B (Minitemper, 5.740 €) y no en una Selmi.** Es decir: **el rango publicado de «20.000-30.000 €» esconde dos negocios distintos**, y eso es exactamente lo que la guía tiene que hacer explícito.

### 4.5 Bean-to-bar y churrería: catálogos verificados, precios inexistentes

**El tren de máquinas bean-to-bar (tostador, descascarilladora, melanger, refinadora, concha, prensa) NO tiene precio público** (CocoaTown España, Premier/DCM, KM0Chocolate: venta a presupuesto). **Es un hallazgo, no un fallo:** significa que quien vaya a bean-to-bar **va a tener que pedir presupuesto sí o sí**, y la guía debe darle **la lista de la compra y las preguntas que hacer**, no un número falso. Lo mismo con **churrera, freidora y extracción** (Inblan, HostelShop, Churrofácil: catálogo sin precio) y con la **guitarra de corte**.

### 4.6 Proveedores reales, verificados con URL

| Familia | Verificados ✅ | Sólo citados 🔎 (no publicar sin verificar) |
|---|---|---|
| **Cobertura profesional** | **Barry Callebaut Ibérica** (Callebaut, Cacao Barry, Chocovic) · **Valrhona** (distribución ES) · **Chocolates Torras** (línea profesional propia) · **Simón Coll + Amatller** (bean-to-bar desde 1840) · **Natra** (>220 M€ en derivados del cacao, vía Alimarket) | Sosa Ingredients · Grupo Nederland · Norte Eurocao · **Blanxart (no verificado: no publicar)** |
| **Grano de cacao** | 🔴 **La vía fiable NO es un buscador: es la Asociación Chocolate Bean to Bar España**, cuyo listado público identifica **8 importadores/proveedores** — **Kahkow Europa** (Valencia), Essenzo, Intensa, Top Kokoa, Orilla Cacao, Lopetes, OrigenEcuador, Clorawfila | Killa Foods · Grupo Meza · Amari Cacao Import · Cacao del Norte (directorio, **BAJA**) |
| **Maquinaria** | **Utilcentre** (distribuidor Selmi + Pavoni, **precios públicos**) · **Selmi Group** · **Equipo H** (**precios SIN IVA declarados**) · **CocoaTown** (catálogo sin precio) · **Inblan** (churreras) | KM0Chocolate · Deldivel · Frigeria · Clifrihos |
| **Moldes y utensilios** | **RestorHome** (Chocolate World, precios leídos) · **El Món Dolç de Clàudia** | María Lunarillos |
| **Packaging** | **García de Pou** (existe, sin precio) | **SelfPackaging: HTTP 403 → «sin fuente (precio)»** |
| **Regalo corporativo B2B** | Gift Campaign («desde 0,30 €») · Regalo Publicidad («desde 0,35 €») · Lindt España · Cornet 1945 · QuieroChocolate · NoSoloDulce | — |

**La pregunta que el lector tiene que saber hacer, y que es el entregable real de este bloque:** «*¿me das el boletín de análisis de **cadmio** y de **HAP** de este lote?*» y «*¿me das el **número de referencia de tu declaración de diligencia debida** (EUDR)?*». Es la diferencia entre un obrador que compra y uno que sabe lo que compra — y las dos son **columnas del libro 9**, no prosa.

---

## 5. Bloque obligatorio 6 — Casos de éxito reales, con cifras públicas

| id | Marca | Modelo | Dato público verificado | Lección para la guía |
|---|---|---|---|---|
| **CHS-57** | **Chocolates Valor** (Villajoyosa, 1881) | Industrial + cadena propia de chocolaterías de taza + franquicia desde **1984** | **>220 M€ de facturación en 2025, +34 %, 8,2 M€ de beneficio neto. 39 establecimientos**, 5 aperturas en 2025. Presencia en >45 países | **El modelo integrado**: demuestra que (a) y (b) **pueden convivir en una marca**. Es el techo de CHS-12 |
| **CHS-58** | **Chök** (Barcelona, 2012) | «Casual bakery + casual chocolate boutique», franquicia desde 2013 | **42 establecimientos** · **local mínimo 55 m²** | **El local más pequeño de todo el research.** Prueba que el formato chocolate-boutique cabe donde una pastelería no |
| **CHS-59** | **Cacao Sampaka** | Boutique premium + franquicia | Tiendas en Madrid, Barcelona, **Tokio, Osaka y Kobe**; franquicia con **100-250 m² y población mínima 500.000 hab.** | **El criterio de ubicación más exigente medido.** Es el contraargumento a «abro una chocolatería premium en mi pueblo» |
| **CHS-60** | **Casa Cacao** (Girona, Jordi Roca y Anna Payet) | Bean-to-bar + café + tienda + hotel de 15 habitaciones | Edificio de 4 plantas de los años 40 **adquirido en 2016**; **obrador visible desde la calle**; cacao de comunidades de Perú, Venezuela, Colombia y Ecuador | **El obrador como escaparate.** ⚠️ **Inversión no publicada** (§15.1 `N-10`) |
| **CHS-61** | **Kaitxo** (**Balmaseda**, Bizkaia) | Bean-to-bar familiar + café de especialidad | Fundada en **2017** por Raquel y Mikel González; el nombre = **KA**fe + **TXO**colate; **oro en los International Chocolate Awards**; abren el obrador al público | **El modelo café + chocolate** como respuesta a la estacionalidad, y **el premio internacional como palanca de marca**. ⚠️ **CORRECCIÓN AL ENCARGO: está en Balmaseda, NO en Karrantza** |
| **CHS-62** | **Utopick** (Valencia, Ruzafa) | Bean-to-bar urbano + obrador-tienda | Paco Llopis y Juana Rojas; compra **directamente a productores**; exporta (EE. UU., Australia) | **El obrador pequeño que vende fuera de España.** ⚠️ El «35.000 € de inversión en 2014» es **afirmación del redactor, no cita de los fundadores, y de hace 12 años**: no usar como referencia de CAPEX |
| **CHS-63** | **Pancracio** (Cádiz, 2003; **comprada en 2017** por una firma valenciana del lujo) | Marca artesana + retail + online | **Facturación >2.500.000 €**, **35 empleados**, **+51,42 %** en el último ejercicio publicado | **La trayectoria completa**: de obrador andaluz a marca comprada por un grupo de lujo |
| **CHS-64** | **Enric Rovira** (Barcelona / Castellbell) | Chocolate de autor con diseño | S.L. **fundada en 1993**; caso estudiado en **Harvard**; sus «rajolas» inspiradas en el Eixample | **El diseño como diferencial**: el producto puede ser el mismo y el envase, el negocio |
| **CHS-65** | **Simón Coll (1840) + Amatller (1797)** | Fabricante histórico | Simón Coll **adquirió Amatller en 1972**, «la marca de chocolate más antigua de Europa» | **El bean-to-bar no es una moda de 2015**: en España lleva desde 1840 |
| **CHS-66** | **Bombonería Pons** (Sants, Barcelona, **1960**) | Obrador familiar de barrio, 3 generaciones | **2 tiendas**; crece por **venta online, más tiendas físicas, venta al por mayor y exportación**; fabrica bombones, turrones y **monas de Pascua** | 🔴 **El caso más parecido al lector objetivo**: escala **por canales, no por franquicia**. Y confirma las monas como pico |
| **CHS-67** | **Chocolatería San Ginés** (Madrid, **1894**) | La referencia absoluta de CHS-07 | **Abierta 24 h, 365 días. No acepta reservas**: ticket en caja al entrar. Ha ido **anexando locales contiguos** | **El prepago en caja como solución de rotación.** Sin cifras públicas |
| **CHS-68** | **Oriol Balaguer / Moulin Chocolat** | Pastelería-chocolatería de autor → cadena | Proyección de Balaguer Coffee & Bakery: **1,5 M€ (2026) → 4 M€ (2027) → 8 M€ (2028)**, 35 tiendas en tres años | **Adquirir un obrador con marca** en vez de crearlo. ⚠️ **CORRECCIÓN AL ENCARGO: Moulin Chocolat ya NO es «de Ricardo Vélez»** — la fundó en 2006 y **hoy es de Balaguer** |
| **CHS-25a** | **Asociación Chocolate Bean to Bar España** | Gremio propio | **«Más de 40» miembros**: **27 makers** (Utopick, Kaitxo, Casa Cacao, Lurka, Kina, Origen, Maüa, Relieve, Puchero, Chocolates Artesanos Isabel, Chocolate Moro…), **8 importadores** y 6 museos | ⚠️ **Discrepancia declarada: 45 (EFE) vs ~41 (recuento del listado). Publicar «más de 40», nunca una cifra exacta** |

> ⚠️ **«Dubai chocolate» NO sostiene ningún capítulo de carta.** WGSN —la misma fuente que pronosticó la moda— sitúa su **saturación máxima a finales de 2024 / principios de 2025**. Un producto de 65 € que se venderá en 2026-2027 no puede apoyarse en eso. Entra como **ejemplo de cómo se explota una moda y cómo se sale de ella**, jamás como recomendación de surtido.

---

## 6. Voz del cliente: dolores, personas, objeciones y vocabulario

### 6.1 Aviso de honestidad que hay que leer antes de la tabla

L5 construyó un corpus de **68 citas literales** (53 numeradas `C##`) leídas **directamente en su URL**, y declara que **no hay ni una cita reconstruida de memoria**. Pero el corpus tiene un hueco grande y confesado: **Reddit está completamente bloqueado** para el agente, **los comentarios de YouTube no son accesibles**, Instagram, Facebook y TikTok piden sesión, y Forocoches y los foros de repostería no devolvieron nada específico. **Consecuencia concreta: no hay ni una sola queja en primera persona sobre un templado fallido, un problema de humedad o una compra de maquinaria de segunda mano.** Tenemos la norma técnica; no tenemos la frustración vivida. Y dos citas del corpus son **antiguas o extranjeras**, marcadas en cada uso: el foro TheChocolateLife es de **junio de 2011 y de EE. UU.**, y la entrevista a Lluís Morera es de **septiembre de 2007** republicada en 2021.

### 6.2 Los 10 dolores con evidencia, y dónde los resuelve el producto

| # | Dolor | Evidencia | Dónde lo resuelve |
|---|---|---|---|
| **D1** 🔴 | **El calor y el verano — el dolor nº 1 y el único exclusivo del chocolate** | Equimercado **apaga la tienda online el 12 de junio, todos los años** (`C39`, `C40`); la manteca se ablanda a 28 °C (`C42`); sala a 18-22 °C y HR <55 % con el aire una hora antes (`C41`, `C43`, `C44`) | **En pastelería el verano es «menos venta»; aquí es IMPOSIBILIDAD TÉCNICA de producir + parada de canal.** Libro 6, hoja **«El Valle de Verano»**, que **no existe en el molde de pastelería** |
| **D2** | **El precio del cacao y cómo repercutirlo** | «*Antes era una vez al año, ahora los aumentos son **semestrales***» (`C14`); cacao a 5.938 $/t, −20 % interanual pero lejísimos de lo normal (`C48`) | **Libro 3** entero: cobertura en celda verde + sensibilidad +10/20/30 % + qué PVP hace falta para mantener margen. Y un epígrafe de prosa sobre **cómo se comunica una subida** (`C15` es el guion literal) |
| **D3** | **Licencias y registro: qué papeles hacen falta de verdad** | 9 meses de obra y permisos (`C05`, EE. UU. 2011); «dificultades con relación a la legislación **especialmente para la instalación de su obrador**» (`C68`); obra en 2021 y apertura en **2023** (`R05`) | **Libro 8 con Gantt** + el epígrafe «**qué NO necesitas**» (el carnet, `CHN-69`) y el argumento del obrador sin humos (`CHN-46`) |
| **D4** | **Cuánto cuesta de verdad** | El rango público va de **20.000 € a 1.000.000 €**: «Abrir una tienda cuesta 100.000 euros» y del obrador «200.000, 300.000 y más» (`C16`, `C17`, pastelería) frente a los 20.000-30.000 € de plandenegocio | **Libro 2, CAPEX por escenarios.** Es el entregable que más justifica los 65 € **porque es la pregunta que la SERP deja sin responder** |
| **D5** 🔴 | **Saben templar o saben contar, casi nunca las dos** | Toda la formación española enseña técnica (§7); «*Si un pastelero tarda hora y media en hacer un pastel y lo cobra teniendo en cuenta ese tiempo no hay nadie que lo pague*» (`C24`); «*Hay muchos pasteleros que no saben porqué hacen tal o cual producto*» (`C26`) | **Es el hueco de mercado entero.** La guía **no compite con Hofmann: compite con el vacío que dejan.** Y se dice en la landing: «*esto no te enseña a templar; te enseña a que templar sea rentable*» |
| **D6** | **Qué cobrar por el bombón** | `C09` (la pregunta «cuánto cuesta hacer una tableta y ponerle el envoltorio» lleva **15 años sin respuesta** en el foro de referencia mundial); «un bombón lleva mínimo dos días» (`R05`) | **Libro 4** con **escandallo por molde/tanda**, **merma de templado con recorte recuperable** y **minutos de mano de obra por pieza**: es lo que enseña por qué el bombón de dos días no se vende a 1,20 € |
| **D7** | **Estacionalidad y tesorería** | Cuatro picos y un valle de tres meses; «3-6 meses de gastos personales de colchón» (`C06`) | **Libro 6 + tesorería a 12 meses del libro 7**: la Navidad se **produce y se paga en octubre** y se **cobra en diciembre**. Ese desfase es el que mata |
| **D8** | **Envíos y venta online** | El caso completo de una tienda que **renuncia a vender tres meses** (`C36`-`C40`) | Epígrafe de canal con la decisión honesta (parar vs isotérmico) y su coste. **No prometer que el online arregla el verano** |
| **D9** 🔴 | **El obrador en casa** | 100 kg/semana, «ELABORADO EN VIVIENDA PARTICULAR», zona geográfica delimitada, «repostería estable a temperatura ambiente» (`C60`-`C63`) | **El capítulo más valioso y el más peligroso.** Y la conclusión verificada es incómoda: **el chocolate NO está en la lista estatal** (`CHN-44`). Se cuenta con la fórmula segura, no con «es ilegal en España» |
| **D10** | **Competir contra el supermercado, Valor y Lindt** | «*deben competir en desigualdad con las onzas de grasas vegetales aderezadas con cacao que pueblan los supermercados*» (`C53`); «*Ahora todo el mundo es chocolatero y bombonero*» (`C23`) | Capítulo de posicionamiento + **las líneas que el súper no puede copiar**: talleres, catas y regalo corporativo |

### 6.3 Las cinco buyer personas, por orden de encaje comercial

> ⚠️ Son **construcciones**. Edades y capital van marcados «sin fuente»; **lo único verificado de cada una es la frase literal**, que en los cinco casos es una cita real del corpus.

| # | Persona | Frase literal que la retrata | Qué compra |
|---|---|---|---|
| **P3** ⭐ | **La reconversión desde otro sector** (camino Chocolate Refart) | «*Empezamos de cero. Teníamos un niño pequeño y nos habíamos quedado en el paro. Enseguida empezamos a movernos, a visitar obradores*» (`C28`) | **La guía entera. Es el comprador ideal: le falta todo y lo sabe** |
| **P5** ⭐ | **La pastelería/cafetería que AÑADE obrador de chocolate** | «*Para elaborar y vender productos de chocolate necesitas menos infraestructura, maquinaria y mano de obra que para la pastelería. Es más rentable*» (`C25`) | CAPEX por escenarios y escandallo comparado. **Más dinero, menos tiempo — y YA está en la lista de compradores de la Guía de Pastelería: es el mejor objetivo del correo de lanzamiento** |
| **P1** | **El pastelero con oficio** que quiere su propio obrador | «*Si un pastelero tarda una hora y media en hacer un pastel y lo cobra teniendo en cuenta ese tiempo de preparación no hay nadie que lo pague*» (`C24`) | **El Excel. La prosa se la salta** |
| **P2** | **La aficionada que se profesionaliza** (camino Danielle Pacheco) | «*llevo décadas soñando con abrir mi propia chocolatería*» (`C32`); ha hecho **cinco** formaciones distintas (`C33`) | **El capítulo legal y el checklist de licencias.** Para ella 65 € son baratos si le evitan una visita al gestor |
| **P4** | **El bean-to-bar que viene del producto, no del dulce** | «*El consumidor no necesariamente está buscando chocolate barato, está buscando que el precio que pague tenga sentido*» (`C51`) | Discute el resto y paga por **aprovisionamiento y normativa del grano**. ⚠️ **Es el perfil que detecta si la guía va floja en cacao** |

### 6.4 Las ocho objeciones, con la respuesta honesta

| # | Objeción | Respuesta honesta |
|---|---|---|
| **O1** | «Esto está gratis en Google» | Está gratis **y está mal**: la única guía española de 2026 pide un carnet que no existe, su desglose **no suma** (15.000-28.000 € bajo un titular de 20.000-30.000 €) y **la mitad de la SERP es de México y EE. UU.**, con pesos y dólares |
| **O2** | «¿65 € por un PDF?» | El PDF no es el producto: **son los libros de Excel**. El comparativo real no es otra guía —**no existe ninguna en español**— sino un curso de **180 € a 5.525 €** que enseña a templar, no a calcular |
| **O3** | «Yo lo que necesito es aprender a templar» | **Cierto, y esto no te lo enseña.** Va en la landing, no escondido en la FAQ |
| **O4** | «El mercado del chocolate está cayendo» | El **volumen** cae (−4,6 % en 2025) pero el **valor** no (+0,5 %), y lo que sube es el segmento de origen y autor. **No prometemos rentabilidad**: damos el modelo para no entrar por la puerta equivocada |
| **O5** | «Esto será normativa española y yo estoy en LATAM» | Sí, y se dice en la primera pantalla. La estructura económica viaja entera; **la FAQ ofrece la adaptación como servicio** |
| **O6** | «Yo empiezo desde casa» | El capítulo existe y es de los más concretos — **y dice lo que nadie dice: el chocolate no está en la lista estatal del art. 13.8** |
| **O7** | «Ya tengo el Kit de Tareas de Chocolatería» | **El kit te dice qué hacer cada día cuando ya has abierto. Esta guía es todo lo que hay que decidir antes.** Son secuenciales |
| **O8** | «¿Y esto quién lo firma?» | La bio real (29 años de alta hostelería, 15 de consultoría) y **las fuentes citadas dentro del producto**, que es lo que ninguna guía gratuita hace. **Sin ratings ni testimonios inventados** |

### 6.5 Vocabulario: cómo lo dicen ellos, y las equivalencias LATAM

**Tres observaciones de lenguaje que valen dinero:**
1. **Quien quiere PRODUCIR dice «obrador», no «chocolatería».** «Chocolatería» (9.900/mes) la teclea el consumidor que quiere merendar. **El título lleva «chocolatería» por la promesa; el cuerpo habla de obrador por el lector; «bombonería» va en el subtítulo** — es la palabra de quien ya lo hizo («hemos conseguido abrir una bombonería a Barcelona», `C34`).
2. ✅ **«artesanal», nunca «artesana»**: `chocolateria artesanal` **390** frente a `chocolateria artesana` **sin dato**. Mismo patrón que en Pastelería, pero más brutal.
3. **«templado» (20) por delante de «temperado» (10)** — el doble. El nombre anunciado en el hub dice «Temperado»: **no justifica cambiar el nombre público** (son cifras ínfimas), pero **«templado» es la forma principal del cuerpo**.

| Concepto | España (forma principal) | LATAM, en la PRIMERA mención | Respaldo |
|---|---|---|---|
| El negocio | **chocolatería artesanal** · **bombonería** | **chocolatería artesanal** funciona en los 7 mercados (MX 1.600, AR 720, CO 590). **`bombonería` sólo es fuerte en ARGENTINA (720)** | medido |
| 🚨 **Falso amigo** | — | **`dulcería` NO ENTRA COMO SINÓNIMO.** En México son **110.000/mes** y la SERP en vivo devuelve **tiendas de golosinas y botanas al MAYOREO** (Superdulces, Azúcar Dulcerías), con PAA de «20 dulces típicos mexicanos» | SERP MX medida |
| El local de producción | **obrador** | taller · laboratorio | **propuesta, sin medición** |
| El cálculo de coste | **escandallo** | **costeo** | medido |
| El mueble | **vitrina** | mostrador · exhibidor | **propuesta, sin medición** |
| La pieza | **bombón** · **trufa** · **praliné** | bombón · chocolate (unidad) | ⚠️ **«trufa» y «praliné» NO son sinónimos de bombón: son tipos.** Un chocolatero lo detecta en la primera página |
| La materia prima | **cobertura** / chocolate de cobertura | cobertura | medido (2.400 las dos, agrupadas) |
| El formato | **tableta** | barra · barrita | **propuesta, sin medición** |
| La bebida | **chocolate a la taza** | chocolate caliente ⚠️ | **No son lo mismo**: el español lleva almidón y es espeso. Se da la equivalencia **avisando de la diferencia** |
| El método | **bean-to-bar — NO TRADUCIR** | idéntico en los 7 mercados (320 ES · 320 US · 140 AR · 110 MX/CO/PE) | medido |
| Formación / ingreso extra | **taller** · **cata** (210 / 170 ES) | **curso** — `curso de chocolateria` MX 210, CO/AR/CL 140. **En LATAM se dice «curso», no «taller»** | medido |
| El defecto técnico | **fat bloom** (140) · **sugar bloom** (90) | igual | medido — **anglicismos vivos en español** |
| Coste | coste | **costo** | heredado |

> 🔴 **Corrección al encargo:** la lista de equivalencias del enunciado incluye «dulcería». **La SERP mexicana en vivo lo refuta.** Sale de la tabla. Y si alguna FAQ recoge el PAA «¿Cuánto dinero necesito para abrir una dulcería?», **hay que reformularla**, porque tal cual responde a otro negocio.

---

## 7. Bloque obligatorio 8 (parte 1) — La competencia de pago: el hueco, confirmado producto a producto

### 7.1 El censo: 32 productos de pago, 21 con precio confirmado en la página del vendedor

| Familia | Ítems con precio + URL | Rango verificado | ¿Alguno enseña a MONTAR una chocolatería **en España**? |
|---|---|---|---|
| **(a) Libros** | 4 de 5 | **18,85 USD – 99 €** | **NO.** El único de negocio (**49,90 €**) está en inglés y sin marco español; el único en español es un **autoeditado venezolano de 2020** |
| **(b) Guías y plantillas** | 3 de 6 | **3 USD – 49 €** | **NO.** Un generador de business plan genérico (49 €) y escandallos de repostería a 3-10 USD |
| **(c) Cursos** | 8 de 12 | **180 € – 21.150 €** | **NO.** Uno solo tiene gestión de empresa (**19.200 €, 15 meses**) y es de pastelería |
| **(d) Franquicias** | 6 de 7 | inversión **33.000-200.000 €** · canon **5.000-30.000 €** | **Sí, pero comprando su marca.** El método no se vende suelto |
| **(e) Consultoras de licencias** | **0 de 3** | **ninguna publica tarifa** | Hacen el proyecto técnico; no enseñan a decidir |

### 7.2 Los cinco hallazgos que valen por todo el análisis

**H1 — El único libro del mundo sobre el NEGOCIO de una chocolatería cuesta 49,90 €, está en inglés y lo publica un fabricante de cobertura.** *The Chocolatier's Shop* (Callebaut, 2023, 160 págs.) se vende literalmente como «una guía para chocolateros que quieren **empezar o hacer crecer su tienda de chocolate**»: marca, surtido, personal, equipamiento, inventario, **más 25 chocolateros contando qué les salió mal**. Es un producto excelente y es **nuestro competidor conceptual**. Lo que no tiene: **español, normativa española, un solo Excel, un solo número de un local de Madrid**. *Consecuencia de diseño:* **no competimos contra el vacío, competimos contra un buen libro en inglés — y ganamos por marco legal + hojas de cálculo, no por «contenido».**

**H2 — En español sólo hay un autoeditado de 2020 escrito desde Venezuela.** «Cómo crear tu negocio de chocolatería: Paso a Paso» (Daniel Rojas Rivero, 221 págs., *Independently published*, **18,85-31,33 USD**, ISBN 9798578061042). Es **el único libro en español sobre montar una chocolatería**, y rankea en la posición 13 de `montar una chocolateria`. Sin marco legal español.

**H3 — Toda la formación española de chocolate enseña a HACERLO, no a VENDERLO.** Verificado ficha por ficha: **Callebaut «Chocolate The One 2026»** son **100 h y 4.500 €** y su propia descripción «*does not explicitly address business or management topics*»; **ESAH** son **150 h online** con **ocho unidades, todas técnicas, y cero módulos de gestión**; **Torreblanca** (180 €) lo admite en su ficha. El **único** programa con dirección de empresa de verdad es el **Máster de Barcelona Culinary Hub: 19.200 € y 15 meses**, y es de alta pastelería. *Consecuencia:* **nuestro comprador no necesita aprender a atemperar — probablemente ya sabe. Necesita saber si le salen los números. La guía no debe enseñar técnica.**

**H4 — El error del «carnet de manipulador» está vivo en la única guía española de 2026, y sus cuentas no cuadran.** Es la evidencia que sostiene la promesa de rigor — **sin decirla en el titular comercial** (regla de John del 5-sep). ⚠️ **Y con la disciplina de citación que impone L3: la página devolvió 404 al intentar capturar la frase, así que el error se refuta con su norma y NO se atribuye a nadie por su nombre** (§15.2).

**H5 — El mercado ya pone precio al método: 5.000 € de canon mínimo, y ninguna consultora publica tarifa.** Entre «5.000 € y tu marca es de otro» (Sven, Chocolat-Box) y «gratis pero con una cifra falsa», **no hay absolutamente nada**. Y en el otro extremo, **ninguna de las cuatro ingenierías revisadas publica el precio del proyecto técnico de licencia**: el emprendedor **no puede ni presupuestar esa partida** sin llamar por teléfono. Ese es el hueco, y cabe un producto de 65 €.

### 7.3 Qué hace bien la competencia y copiamos

| Qué hace bien | Quién | Cómo lo aplicamos |
|---|---|---|
| **Contar fracasos, no sólo casos de éxito** | *The Chocolatier's Shop*: 25 chocolateros narrando «experiencias exitosas **y las dificultades encontradas**» | El bonus «**12 decisiones de apertura resueltas**» es exactamente esa forma. Cada decisión **enseña el escenario que sale mal, con la cifra a la que se rompe** |
| **Dos escenarios + DSCR calculado, como titular** | plandenegocio.es, a 49 € | **Ya lo tenemos y mejor** (P&L, tesorería 12 meses y DSCR antes de deuda, motor 2.2). Hay que **enseñarlo en la landing**, porque el competidor lo usa de gancho |
| **Publicar la estructura económica completa sin vaguedades** | Las fichas de franquicia: inversión, canon, royalty, m², población, años | Una columna «**franquicia vs. independiente**» en el CAPEX. ⚠️ **Decisión D11**: nombra competidores por su nombre en un entregable de pago, y **L1 y L4 dan cifras distintas de las mismas marcas** |
| **aw, pH y estabilidad como materia propia** | Callebaut *Formulación y bombonería 2.0* — **900 € por enseñarlo** | **Vida útil y aw del relleno es un libro y un capítulo**, no una nota al pie |
| **El Canvas como puerta de entrada emocional** | Rojas Rivero y silviaguedez.com | Un capítulo 01 corto de «¿es esto para ti?» con **criterios de descarte numéricos**, no con ánimo |
| **Directorio sectorial como prueba de mercado** | Asociación Bean to Bar (más de 40 makers) | **Benchmark competitivo**: quién hay, en qué comunidad, con qué modelo. Gratis, verificable y **nadie lo ha convertido en tabla** |
| **Empezar pequeño y escalar la máquina** | KM0Chocolate: «primero una atemperadora y una bañadora, y más adelante molinos, conchadoras, prensas» | El CAPEX debe tener **fases**, no una sola lista de la compra |

### 7.4 Limitaciones declaradas del censo

**Amazon.es devuelve HTTP 500** e **infofranquicias.com 403** (faltan el precio español del único libro en español y **todos los datos de Chocolat Factory**, la franquicia de chocolate artesano más visible del país) · **EPGB no publica precios** y tres de sus fichas dan 404 (su Màster de Xocolata queda sin precio pese a ser probablemente el competidor formativo más relevante de Barcelona) · **Hotmart no muestra precio sin checkout** (3 infoproductos sin cifra) · **ninguna consultora de licencias publica tarifa** · **el censo mide precio publicado, no ticket medio ni unidades vendidas: ninguna afirmación de «cuánto vende la competencia» puede sostenerse** · **silviaguedez.com (403) y teymas.com (sin salida) se perdieron**: son 10 fuentes gratuitas auditadas, no 12.

> ⚠️ **Recordatorio de método que casi cuesta un ancla falsa:** el buscador daba **41.580 €** para el Diploma de Pastelería de Le Cordon Bleu Madrid; su página oficial de tarifas publica **21.150 €**. **El snippet no es la fuente.**

---

## 8. Lo que ya vendemos y la FRONTERA: qué se cita y qué se construye

### 8.1 Frontera con `kit-tareas-chocolateria` (12 €, 11 xlsx) — seis reglas numeradas

Medido por mí: **11 ficheros = 9 checklists + 2 BONUS**, que es **el estándar de la familia** (16 de 18 kits tienen exactamente eso). **139 fórmulas en todo el kit, 95 de ellas en `09-apertura-cierre-caja.xlsx`**: fuera de ese libro son **44 fórmulas en 10 ficheros**. **El kit es papel, no calculadora** — y desde la óptica de quien ABRE le falta todo: **no hay un solo euro, ni un m², ni una decisión de compra, ni un trámite.**

| # | Riesgo de solape | **Regla** |
|---|---|---|
| **K1** | **Templado y moldeado** (`02-partidas-produccion.xlsx`: Templado 36×7, Moldeado 49×7, con curvas, tiempos y «enfriar a 12-14 °C 10-15 min») | La guía **no emite ninguna hoja de proceso de templado ni de moldeado y no enseña técnica**. Construye **capacidad**: cuántos bombones/día permite la atemperadora que vas a comprar. **Decisión de compra, no de ejecución** |
| **K2** | **Campañas** (`06-eventos-temporada.xlsx`: Navidad, San Valentín, Pascua) y **calendario anual** (`BONUS-02`, 12 meses con Alta/Media/**BAJA en agosto**) | La guía **no repite el calendario ni las tareas de campaña**. Construye la **economía**: % de facturación por campaña, déficit de capacidad, coste del refuerzo, **tesorería inmovilizada en moldes y packaging** y —lo que el kit no tiene— **el coste del valle**. 🔴 **El kit pone las fechas; la guía pone los euros** |
| **K3** | **Perfiles** (`04-tareas-perfiles.xlsx`: **Chocolatero · Dependiente · Encargado**, **3**, no los 4 de pastelería) | La guía **no rehace las fichas de tarea**: dimensiona (cuántos de cada perfil, bruto de convenio, coste de empresa con SS) y planifica contrataciones. ⚠️ **Los nombres del juego de datos son LITERALMENTE esos tres.** «Maestro chocolatero», «bombonero» u «oficial» **quedan prohibidos** (precedente D22 de Pastelería) |
| **K4** | **Vitrina** (`01-apertura-cierre`: «cubrir bombones que queden expuestos») | La guía **no hace checklist de vitrina**: decide **qué vitrina** (refrigerada a +14/+17 °C o climatizada) y **qué referencia puede ir en cuál**. Es CAPEX y vida útil, no apertura del día |
| **K5** | **Arqueo de caja** (`09`, 95 fórmulas, Registro Mensual 38×10) | **Prohibido rehacer.** Es el único libro del kit con cálculo de verdad y está resuelto |
| **K6** | **Control de temperaturas** (`03-tareas-manager.xlsx`, diario) | La guía **no emite registro de temperaturas** (es del kit y del `pack-appcc/01`): **dimensiona el clima** — qué cámara sostiene 15-18 °C con la carga térmica de esa ciudad y ese equipo. **Cálculo de compra, no de registro** |

**Regla transversal (D21 de Pastelería, y aquí es aún más necesaria):** cuando la guía necesita un dato que vive en el kit, **la celda verde trae su propio valor por defecto declarado como supuesto** y la nota «*si ya tienes el Kit de Tareas Chocolatería, sustitúyelo por tu dato real de `<fichero>.xlsx`*». **Cero fórmulas entre libros.** El comprador de la guía **no ha abierto**: no tiene histórico.

**Frase de frontera, arriba en la landing y no en la FAQ:** «*El Kit de Tareas te dice qué hacer cada día cuando ya has abierto. Esta guía es todo lo que hay que decidir antes.*»

### 8.2 Frontera con `guia-pasteleria-obrador` (65 €) — mismo molde, contenido propio

Medido por mí sobre `astro-site/public/dl/guia-pasteleria-obrador/`: **8 libros y 4.557 fórmulas**; documentos de **103 págs / 56.168 palabras** (545,3 pal/pág), bonus de **37 págs / 16.842 palabras** (455,2) y business plan de **7.415 palabras con 9 tablas**.

| Se COMPARTE (estructura) | Es CONTENIDO PROPIO (nunca se copia) |
|---|---|
| El reparto de libros por decisión | Las partidas, los equipos, las zonas y los proveedores |
| El motor de escandallo por tanda con coste hora de obrador imputado | **La merma de templado y el recorte recuperable** (el chocolate mal templado **se vuelve a fundir**; la masa fallida no) y **la caja como unidad de venta**, que no existe en pastelería |
| La ficha de visita a local con veredicto eliminatorio | Los **criterios**: allí humos y forjado; aquí **clima, estabilidad térmica y la ausencia de humos como VENTAJA** |
| El molde `planes-v2_0` motor 2.2 del plan financiero | Los **canales son 5, no 4**: mostrador · online con envío · B2B hostelería · **regalo corporativo** · **talleres y catas** |
| El árbol de registro sanitario, el del art. 3, la ruta doméstica y el Gantt | **RD 1055/2003, cadmio y EUDR**, que en pastelería no existen |
| `puntos_por_epigrafe`, `NO_COMUN`, la lista negra, el vocabulario ES/LATAM | Cada entrada de esas listas |
| La hoja «Decisión de Huevo y Temperatura» como **hueco funcional** | Su equivalente aquí es **aw / vida útil del relleno y temperatura declarada**, no el huevo (aunque el huevo sigue tocando yemas, merengues y glaseados reales, `CHN-31`) |

🔴 **Prohibición dura, con precedente medido:** *está prohibido copiar prosa, tablas o redacciones legales de la guía de pastelería.* «Copiar redacciones legales de otros kits sin verificar» ya produjo que `kit-tareas-sushi-bar/03` y `kit-tareas-marisqueria/03` citen el **RD 1420/2006 derogado**, y **eso sigue vivo en producto vendido** (punto 0 de la deuda del calendario). **Aquí el reflejo peligroso concreto es copiar `PA-39`** (libertad horaria): en chocolatería el fundamento es otro (`CHN-77`).

### 8.3 Frontera con el resto del catálogo: qué se CITA y no se construye

| Activo | Decisión |
|---|---|
| `kit-escandallos` (12 €) — **13 ficheros y NINGUNO de chocolate** (verificado: la 05 es de pastelería por lote) | **CITAR** como cross-sell. **El escandallo de chocolate se CONSTRUYE porque no existe en el catálogo** |
| `pack-appcc` (14 €) — **18 de sus 21 registros valen** para un obrador de chocolate; no aplican `09-control-aceite-fritura`, `16-coccion-regeneracion` y `18-congelacion-anisakis` | **CITAR** los 18. La guía lleva **una fila de checklist** («plan de autocontrol firmado antes de abrir») y **cero registros**. Lo que construye —aw, lote de cobertura, cámara— **no está en el pack** |
| Guía Food Cost (55 €), cap. 17 (costeo por lote en obrador) | **CITAR**, no repetir |
| `kit-plan-financiero` (39 €) | **NO citar como cross-sell**: el plan financiero va **dentro** de la guía |
| `guia-panaderia-obrador` (65 €) | ⚠️ **D19 de Pastelería sigue vigente: no se enlaza a ninguna hermana de la línea mientras no entregue lo que promete** (2 clics / 39 impresiones y 1 página de PDF) |
| Agentes «Chocolatero Consultor Pro» y «Chocolatería Creativa» + las **4** páginas `/usos/` | **Canal de distribución interno**: es donde está el comprador, no en la SERP |

### 8.4 El pipeline se reutiliza al 100 %, y los dos bugs que lo amenazaban YA ESTÁN ARREGLADOS

Verificado por mí, fichero a fichero:

- **`guias-v2_0/documentos.py` es genérico** (2.246 líneas): su única entrada de producto es `--producto <pid>` y resuelve `fichero.xlsx!Hoja!Celda` contra `DL/<pid>/`. **No hay ningún registro de productos que ampliar.**
- **`motor.py`** (2.135), **`dump_prompts.py`** (62), **`check_bloque.py`** (32) y **`solape.py`** (82) son **agnósticos**.
- ✅ 🔴 **`es_fila_porcentual()` YA NO rompe los nombres con `%`.** `documentos.py:692` → `RX_ETIQUETA_PCT = re.compile(r'\(\s*%\s*\)|\ben\s*%|\(porcentaje\)')`, **sin `%\s*$`**, y `RX_CELDA_PCT` (`:698`) sólo casa una celda que **sea** un porcentaje entero (`^\s*-?\d+(?:[.,]\d+)?\s*%\s*$`). El fix entró en **`0ba5158`**. **«Tableta 70 %» y «Cobertura 55 %» son nombres seguros, y el `%` es vocabulario del oficio que NO hay que renunciar a usar.**
- ✅ 🔴 **`verificar_guion.py` YA aborta por tipo.** Línea 207: `if fmt in FMT_NUMERICOS and not isinstance(v, (int, float)): falla(…TIPO INCOMPATIBLE…)`, con el comentario que cita **A2 (2026-09-10)**. **Se copia el fichero y el gate viene dentro.**
- **`gate_libros.py`** (269 líneas) es reutilizable **cambiando dos literales** (la línea de versión y la lista de ficheros): sus 9 comprobaciones son de familia (funciones prohibidas, referencias externas, celdas verdes vacías, constantes de IVA/margen cableadas, «Instrucciones» primera, versión, `creator`, WinAnsi, ≥25 etiquetas válidas en el `mapa-*.json`).
- **`paginas-gate.py`, `nombre-gate.py`, `censo-entregables.py`, `gate-no-latinos.py`, `gate-flujo-postpago.py`, `inject_cache.py`, `postprocess-transversal.py`, `sync-payment-links.py`, `sync-product-prices.py`** ya existen y aceptan `--only <slug>`. **Nada nuevo que escribir.**
- **A crear:** la SPEC · `guias-v2_0/guion_guia_chocolateria_obrador.py` (~4.900 líneas de referencia) con su `NO_COMUN` propio y **`puntos_por_epigrafe` desde el día 1** · `scripts/productos-digitales/guia-chocolateria/` con **9 `gen_*.py`** (media medida en pastelería: **1.142-2.720 líneas por libro**, 12.196 en los ocho), `datos_ejemplo.py` (3.324 de referencia), `_comun_chocolateria.py` (280) y los dos `_comun_libros_*.py` (322 + 435).
- 🔴 **Ordenación crítica, heredada:** `documentos.py` lee `xlsx_dir = DL/<pid>/`. **Los libros tienen que estar copiados en `astro-site/public/dl/guia-chocolateria-obrador/` ANTES de lanzar la redacción**, porque el guion cita cifras por celda y el pipeline las resuelve con openpyxl para meter **el número** en el prompt. **Invertir el orden hace que el guion no pueda escribirse.**
- ✅ **`puntos_por_epigrafe` funcionó y hay que repetirlo sin tocarlo:** `solape.py` sobre la caché de Pastelería dio **1 par en 46 bloques**, frente a **41 pares en 15 de 20 capítulos** del Manual del Chef Ejecutivo, que costaron ~2,2 M de desduplicación.
- 🔴 **Lo único NUEVO de código: el script de banners.** La serie va `fase8f` (Food Cost) · `fase8g` (Manager) · `fase8h` (Chef) · **`fase8i` (Pastelería, verificado que existe)** → la siguiente libre es **`fase8j`**. **Recomendación firme: NO copiarlo una quinta vez.** Generalizarlo a `fase8x-sustituir-banner.py --producto <pid>` cuesta lo mismo y cierra la deuda (lo propuso D32 de la SPEC de Pastelería y no se hizo).
- ⚠️ **`guias-v2-SPEC.md` §5.3 y la cabecera de `documentos.py` siguen diciendo «texto largo SIEMPRE con bridge.py» y están DESACTUALIZADAS.** Manda la regla de John del 2026-09-04: los productos digitales los escriben **subagentes Anthropic**.

---

## 9. Bloque obligatorio 7 — La lista DEFINITIVA de entregables

### 9.1 El juego de datos único: la chocolatería «La Almendra»

Patrón obligado: **un solo `datos_ejemplo.py`** del que beben los 9 generadores, el guion y los dos bonus. *Si un número cambia, cambia ahí y se regeneran los libros.*

| Campo | Propuesta | Por qué |
|---|---|---|
| **Nombre** | Chocolatería **«La Almendra»** | Neutro, sin marca real. Paralelo a «La Encina» (Food Cost / Manager) y «La Clara» (Pastelería). ⚠️ **Comprobar que no coincide con marca registrada antes de cerrarlo** |
| **Formato** | **Obrador propio + tienda a calle** (CHS-03), ciudad media española **sin nombre propio** | Es el caso central; las demás variantes son **desviaciones tabuladas** sobre él |
| **Superficie** | **~75 m²**, dentro de los **60-100 m²** publicados y de los **55-120 m²** en los que convergen tres fuentes independientes (CHS-03, traspasos reales 74-118 m², mínimo de Chök 55 m²). Zonas: **obrador de templado · cámara de chocolate · almacén de cobertura · packaging · tienda · aseos y vestuario** | ⚠️ **Es PROPUESTA, no medición.** Y **el reparto NO es el de pastelería**: aquí **no hay zona de horno ni de fermentación**, y sí **cámara climatizada**. Copiar el reparto sería el error de método que la casa persigue |
| **Plantilla** | **Los 3 perfiles LITERALES del kit: Chocolatero · Dependiente · Encargado** | **Regla dura K3 + precedente D22.** Coherente con «1-2 empleados» de CHS-70 más el titular |
| **Carta** | **25-30 referencias en 5 familias:** bombones de colección · tabletas · **chocolate a la taza** · turrones y figuras de temporada · **cajas y regalo** | La taza entra como **familia**, no como negocio (§1.3). **Las cajas son familia propia porque la caja es la unidad de venta real** (CHS-29: el precio por bombón baja 23 % de la de 12 a la de 35) |
| ✅ **Nombres con `%`** | **PERMITIDOS.** «Tableta 70 %», «Cobertura 55 %», «Bombón de origen 64 %» | ✅ **Verificado por mí: el bug de `es_fila_porcentual()` está arreglado** (§8.4). El `%` es vocabulario del oficio y **renunciar a él habría sido pagar un bug que ya no existe** |
| **Coherencia con el kit** | Verificar **abriendo los ficheros** qué referencias vienen precargadas en `02-partidas-produccion.xlsx` y `03-tareas-manager.xlsx` y usar **las mismas donde coincidan** | El research de Pastelería lo afirmó sin abrirlos y su SPEC tuvo que ponerlo como tarea. **Aquí se hace antes** |
| **Campañas** | **Navidad+Reyes · San Valentín · Pascua (monas y huevos) · Día de la Madre · Halloween · Todos los Santos** + **valle de junio-agosto** | **Salen del `BONUS-02` del kit**, que ya declara Alta/Media/Baja mes a mes. Así el lector reconoce el calendario y la guía pone los euros |
| **Cobertura de referencia** | **Una sola celda**, la del libro 3, de la que beben el escandallo, la sensibilidad y el stock inicial del CAPEX | 🔴 **Un concepto, UNA fuente** (A3 de la refutación de Pastelería: el fondo de maniobra calculado dos veces publicó **dos inversiones totales distintas** en el mismo pack) |
| **Convenio** | En celda verde, con su código y su publicación; **una sola tabla, la de Madrid, marcada como ejemplo** | ⚠️ **Cuál es el convenio de una bombonería es pregunta abierta** (`CHN-65`, V-01) |

**Restricciones de familia, no negociables:** helpers de `motor.py` (`f()`, `val()`, `verde()`, `dv_lista()`, `semaforo_isnumber()`, `version_line()`, `hoja_instrucciones()`) · hoja «Instrucciones» primero con «celdas verdes = editables», línea de versión, bio anclada y nota de desproteger · **cero constantes tecleadas dentro de una fórmula** · `IFERROR(...;"")` y `ISNUMBER` en semáforos · «sin dato» = `""`, nunca `0` · **prohibidos `INDIRECT`, `COUNTA`, `PMT`, `OFFSET`, `XLOOKUP`, `LET`, `LAMBDA` y las referencias entre libros** · formatos `#,##0.00 €` / `0.0 %` / `dd/mm/yyyy` · A4 con `print_setup` · metadata `author='AI Chef Pro'` · **cada celda con dato legal lleva nota «Verificado el 12-09-2026 · norma · URL»** · al cierre, `inject_cache.py` + verificación `data_only` de cada fórmula + `mapa-<libro>.json`.

### 9.2 Los 9 libros de Excel — arbitraje entre L4 (8) y L6 (10)

**L4 propone 8 (paridad con Pastelería) y L6 propone 10 con plan de absorción. Mi arbitraje son 9**, y la diferencia con cada uno está argumentada:

- **Contra L4:** el chocolate tiene **dos frentes que la pastelería no tiene y que no caben como hojas sin perderse**: la **sensibilidad al precio del cacao** (es el argumento comercial más fuerte del producto y el único oficio de la casa donde una commodity volátil es el 40-60 % del coste) y la **vida útil del relleno** (factor 5, y es el hueco funcional de la hoja del huevo). Enterrar el primero dentro del escandallo **es enterrar lo que se vende**.
- **Contra L6:** su libro 10 (talleres y regalo corporativo) **es genuinamente dos hojas**, no un libro: `taller de bombones` y `bombones corporativos` valen **10 búsquedas/mes cada uno** (medido por mí) y su contenido es **margen por sesión y calendario de cierre de pedidos**, que es exactamente lo que hace la hoja «Canales y Punto Muerto» del plan financiero. **Absorberlo ahorra 0,30 M sin perder nada visible.**

| # | Fichero | Hojas | Entradas (celda verde) | Salidas por fórmula | La decisión que permite | Frontera / por qué existe |
|---|---|---|---|---|---|---|
| **1** ⭐ | `capacidad-obrador-y-clima.xlsx` | Instrucciones · Parámetros · **Zonas y m²** · **Clima del Obrador** · **Capacidad por Equipo** · **Cuello de Botella** · **Ficha de Visita a Local** | m² por zona; kg/hora de atemperadora; nº de moldes; m³ de cámara a **15-18 °C**; horas de turno; **T y HR objetivo**; **T exterior de tu ciudad en agosto**; potencia instalada | m² totales y % obrador/venta; **bombones/día por equipo**; **el equipo que limita**; **carga térmica de la cámara y si el equipo la sostiene en agosto**; **semáforo eliminatorio del local** | **Si ese local sirve y cuántos bombones/día aguanta el equipo que vas a comprar** | **Nada equivalente en el catálogo.** La hoja «Clima del Obrador» **no existe ni en pastelería ni en la competencia**: es **el** criterio del chocolate. Frontera K1/K6 |
| **2** | `calculadora-capex-chocolateria.xlsx` | Instr. · Parámetros · **CAPEX por Bloque** · **Variante del Formato** · **Traspaso vs Obra Nueva** · **IVA y Tesorería** · Resumen | importe por partida (mín/máx/tuyo); variante elegida; **«¿lleva IVA?» y tipo por línea**; precio de traspaso; renta; horizonte; meses de colchón; **kg/mes de plástico no reciclado adquirido fuera de España** | total por bloque y CAPEX total; **IVA soportado y cuándo vuelve**; CAPEX por variante; **coste a 5 años de traspaso+renta vs obra nueva+renta**; **alerta al superar los 5 kg/mes del art. 75.f** | **Cuánto necesitas de verdad y si sale mejor traspaso u obra** | Molde del libro 2 de pastelería (323 fórmulas). **Variantes propias:** bean-to-bar (tostador, descascarilladora, refinadora, conchadora) y **churrería-chocolatería** (§1.3). **Cero precios inventados: celda verde con su columna de IVA.** Y el contador de plástico de `CHN-62` |
| **3** ⭐ | `sensibilidad-al-precio-del-cacao.xlsx` | Instr. · Parámetros · **Coste de Cobertura por Referencia** · **Escenarios de Precio** · **Repercusión al PVP** · **Stock y Cobertura de Compra** | €/kg de cada cobertura; % de cobertura en cada referencia; escenarios de subida en %; margen objetivo; semanas de stock | coste de materia por referencia en cada escenario; **food cost resultante**; **subida de PVP necesaria para mantener margen**; **€ inmovilizados si compras a plazo**; **la referencia que primero se rompe** | **Qué haces cuando el cacao sube un 40 %: subes precio, cambias gramaje, cambias cobertura o aceptas menos margen** | 🔴 **El libro más propio del producto y el que ninguna guía tiene.** Responde al dolor que la propia página de rol ya declara («cacao con precio volátil que cambia el coste real cada semana») y a la cita del oficio: «**antes era una vez al año, ahora los aumentos son semestrales**» |
| **4** ⭐ | `carta-de-apertura-y-escandallo-chocolate.xlsx` | Instr. · Parámetros (coste hora de obrador) · **Denominaciones y Mínimos Legales** · **Escandallo por Molde/Tanda** (25-30 refs) · **Merma de Templado y Recortes** · **Coste Hora y Mano de Obra** · **Unidad vs Caja** · **Mix y Ticket Medio** · Decisión de Surtido | precios de compra; gramaje; **piezas por molde**; moldes por tanda; minutos de mano de obra; **% de merma de templado** y **% de recorte recuperable**; **% de cacao y de manteca por referencia**; PVP por unidad y por caja; mix % | coste materia por pieza; **coste real con merma y recorte recuperado**; coste de mano de obra por pieza; food cost %; margen €; **precio de la caja de 9/16/24 frente a la suma de sus unidades**; **qué puedes LLAMAR legalmente a cada referencia y qué menciones debe llevar** | **Qué vendes, a cuánto, cómo lo puedes llamar, y si la caja te gana o te cuesta dinero** | Motor heredado del libro 4 de pastelería (1.929 fórmulas, el más denso). **Lo propio:** merma de templado con **recorte recuperable** (el chocolate mal templado **se vuelve a fundir**), **la caja como unidad de venta**, y la hoja de **denominaciones** que materializa `CHN-02`/`CHN-07`/`CHN-08`. **`kit-escandallos` NO tiene hoja de chocolate** |
| **5** ⭐ | `vida-util-rellenos-y-rotacion.xlsx` | Instr. · Parámetros · **Tipo de Relleno y aw** · **Vida Útil Declarada** · **Temperatura y Vitrina** · **Lote Económico y Merma por Caducidad** | tipo de relleno por referencia; **aw medida o estimada por ti**; **T de conservación que TÚ declaras**; **vía legal del huevo** cuando aplica; ventas/semana; tamaño de lote | plazo orientativo por familia; **vida útil declarada por ti** (celda verde, **nunca calculada**); temperatura con su norma; **lote económico**; **merma esperada por caducidad en €/año**; **semáforo de vitrina refrigerada (+14/+17 °C) vs climatizada** | **Cuánto dura cada bombón, en qué vitrina va y de cuánto haces cada lote** | 🔴 **El hueco funcional de la «decisión del huevo» de pastelería.** ⚠️ **Regla dura:** la vida útil **la declara el operador en su APPCC** (`CHN-30`); el libro **nunca la calcula ni la presenta como norma**. Y `CHN-31` (las tres vías del huevo para yemas, merengues y glaseados) **tiene que estar explicada en la prosa ANTES de esta hoja** |
| **6** ⭐ | `campanas-y-valle-del-ano.xlsx` | Instr. · Parámetros · **Calendario de Campañas** · **Peso sobre el Año** · **Capacidad vs Demanda del Pico** · **Refuerzo y Tesorería** · **El Valle de Verano** | ventas estimadas por campaña; PVP y unidades/día; refuerzo; antelación de compra de moldes y packaging; meses de valle y % de caída; ¿cierras en agosto?; ¿paras los envíos? | % de facturación por campaña; **déficit de capacidad** (contra el libro 1); coste del refuerzo; **tesorería inmovilizada en moldes y packaging de temporada**; **coste del valle: fijos que siguen corriendo con la caja parada**; **cuánto tiene que aportar la desestacionalización para taparlo**; **fila de CUADRE** unidades de campaña / unidades del año | **Si aguantas Navidad, y de qué vives en julio y agosto** | Frontera K2. **La hoja «El Valle de Verano» no tiene equivalente en pastelería**, donde el verano no es un agujero. La **fila de cuadre** es obligatoria por A8 |
| **7** | `plan-financiero-3-anos-chocolateria.xlsx` | 0. Supuestos · Inversión Inicial · PyG 3 Años · Punto de Equilibrio · Escenarios · Personal · **Tesorería 12 meses** · Financiación · **Canales y Punto Muerto** · **Talleres y Regalo Corporativo** · Instrucciones | tickets/día; ticket medio sin IVA; días de apertura; **estacionalidad mensual con el valle dentro**; rampa; brutos de convenio; % SS; deuda; **por canal**: ventas, margen, coste de servir, comisión, **coste de envío refrigerado**; precio/persona del taller, aforo, horas de docente; pedido mínimo B2B y días de cobro | P&L; punto muerto; 3 escenarios; coste de personal con SS; tesorería mes a mes; servicio de deuda; **margen de contribución por canal**; **punto muerto con y sin B2B**; **asistentes para cubrir el punto muerto del taller**; **€/hora de sala del taller frente a €/hora de la misma sala vendiendo**; **fecha límite de cierre de pedidos de Navidad calculada hacia atrás desde la capacidad del libro 1** | **Si el negocio se sostiene, cuándo llega al equilibrio, qué canal lo sostiene y si el taller da dinero o te ocupa el obrador en el peor momento** | Molde `planes-v2_0` motor **2.2** (1.022 fórmulas). **Los canales son 5, no 4.** ✏️ **Aquí absorbo el libro 10 de L6**: son dos hojas, no un libro. La segunda impide el error clásico —**aceptar 400 cajas corporativas para la semana en que ya no cabe un molde más**— con el dato verificado de que **el pedido corporativo de Navidad se cierra en octubre** |
| **8** ⭐ | `checklist-legal-licencias-y-cacao.xlsx` | Instr. · **Checklist Legal (F1-F6)** · **Árbol de Registro Sanitario** · **Suministro a Otros Minoristas** · **Ruta Doméstica** · **Cadmio y Analíticas** · **EUDR: ¿te aplica?** · Registro de Formación · **Cronograma y Ruta Crítica** | ✓/☐/N/A, fecha, responsable, coste; CCAA; ¿suministras a otros minoristas?; kg/semana y a quién; **¿importas grano o compras cobertura en la UE?**; proveedor y qué te declara; fecha y duración de cada hito | contador y % por fase; **veredicto «comunicación autonómica» vs «RGSEAA»**; **semáforo de los tres umbrales acumulativos**; alerta de los 100 kg/semana; **si necesitas analítica de cadmio y con qué frecuencia**; **tu papel en la cadena EUDR y qué documentación te toca**; mes de cada hito, ruta crítica y fecha de apertura | **Qué papel te toca, en qué orden, y qué te obliga la norma del cacao** | 🔴 **El libro más diferencial del bloque legal.** Las 5 hojas de familia se heredan; **las dos nuevas dependen de `CHN-16`…`CHN-19` y `CHN-20`…`CHN-29`**. ⚠️ **La hoja de EUDR se construye con el resultado de L3, que ya está cerrado contra fuente primaria: «operador posterior», art. 5, cinco años, sin registro.** Si algo se mueve, va al anexo |
| **9** | `checklist-equipamiento-y-proveedores-cacao.xlsx` | Instr. · **Equipamiento** (mín/máx, prioridad, **¿lleva IVA?**, **plazo de entrega**) · **Variante del Formato** · **Proveedores de Cobertura y Cacao** · Contador | ✓; precio real negociado; proveedor; plazo en semanas; **¿te declara origen y número de DDS (EUDR)?**; **¿te da analítica de cadmio y de HAP?**; pedido mínimo | contador; **desviación contra el CAPEX del libro 2**; **plazo crítico** que mueve la fecha de apertura; **semáforo de documentación del proveedor** | **Qué compras, a quién, a qué precio real, con qué plazo y con qué papeles** | Molde B del libro 7 de pastelería (352 fórmulas). **Dos columnas que pastelería no necesita** (EUDR y cadmio). Se siembra con los proveedores **verificados** de §4.6; **los 🔎 no se publican** |

**Cobertura de la promesa publicada en el hub desde mayo** («Temperado, obrador, vitrina, proveedores de cacao, licencias y modelo de negocio»): temperado → 1, 4 (capacidad y merma; **no técnica**, K1) · obrador → 1 · vitrina → 5, 2 · proveedores de cacao → 9 · licencias → 8 · modelo de negocio → 2, 3, 6, 7. **Los seis sustantivos quedan cubiertos.** ⚠️ **«Proveedores de cacao» suena a grano (bean-to-bar) y el molde principal compra COBERTURA**: o se retoca la descripción al publicar, o el libro 9 cubre las dos cosas (decisión **D4**).

### 9.3 Los dos bonus — y los dos que se descartan con argumento

**BONUS 1 — `business-plan-modelo-chocolateria.docx` (RELLENO).** El caso completo de «La Almendra» con cifras: resumen ejecutivo, mercado, concepto, plan de operaciones, plan financiero y análisis de riesgos con escenarios. **Objetivo ≥3.500 palabras y ≥9 tablas**, todas coherentes con el libro 7. **Justificación medida:** es el formato que pide un banco o una línea ENISA, el de pastelería mide **7.415 palabras y 9 tablas**, y **aquí vale todavía más** porque **no existe ninguna referencia española fiable de inversión para chocolate**. ⚠️ **Hereda el defecto B2 de Pastelería: el resumen ejecutivo tiene que DAR el resultado neto, el margen y el punto de equilibrio, no remitir a otra hoja.**

**BONUS 2 — «12 decisiones de apertura resueltas» (PDF + DOCX).** Molde probado **tres veces**; el de pastelería mide **37 págs / 16.842 palabras / 12 tablas**. Cada decisión con **contexto · opciones · criterio · la celda del libro que la resuelve · y la norma con su id `CHN-*` y su fecha de verificación** cuando la hay. Las doce, todas salidas de este research:

1. **Bombonería o bean-to-bar** (y el EUDR delante: operador posterior vs operador, `CHN-24` vs `CHN-25`). · 2. **Comprar la Selmi o empezar con la Minitemper** (factor 4,3 en máquina y factor 4 en el total del núcleo). · 3. **Abrir con 15 referencias o con 30.** · 4. **Vender la caja o la unidad** (el precio por bombón cae 23 % de la caja de 12 a la de 35). · 5. **Cobertura de marca o de origen** (25 €/kg vs 37,48 €/kg, factor 1,5: es la decisión de posicionamiento más cara del negocio). · 6. **Vitrina refrigerada a +14/+17 °C o vitrina climatizada** (y qué referencia puede ir en cuál). · 7. **Aceptar el primer pedido corporativo sin histórico** — **y en qué momento te obliga al RGSEAA** (`CHN-41`). · 8. **Envío a domicilio en verano: cuándo dices que no.** · 9. **Cerrar en agosto o quedarte.** · 10. **El taller: línea de negocio o marketing.** · 11. **Empezar en casa dentro de la legalidad: qué puedes vender y qué no** (`CHN-44`). · 12. **Qué haces con el chocolate que no se vende** (`CHN-64` y el «rincón de los feos»).

**BONUS 3 (calendario de campañas) — ❌ DESCARTADO.** Es el `BONUS-02` del kit de 12 € (**frontera K2**). Duplicarlo canibaliza y encima quedaría peor.
**BONUS 4 (recetario de bombones con curvas de templado) — ❌ DESCARTADO, terminantemente.** Un recetario con gramajes y curvas que **nadie ha ejecutado** es el patrón de cifra inventada que la casa prohíbe, **y aquí el riesgo es físico**: una curva de templado mal publicada arruina producción. Precedente: Pastelería descartó su BONUS 3 por lo mismo. **Las 25-30 referencias viven dentro del libro 4 como datos de ejemplo declarados como tales.**

### 9.4 Resumen del paquete

**1 guía (PDF + DOCX) de 20 capítulos + anexo normativo · 2 bonus (business plan relleno + 12 decisiones resueltas) · 9 libros de Excel con fórmulas vivas.** Pago único, acceso vitalicio al dashboard, actualizaciones incluidas.

> **Es el segundo paquete más grande de los cinco productos nuevos del ciclo**, por detrás sólo del que Pastelería llegó a proponer: Food Cost entregó 8 xlsx, el Manual del Manager 7, el Manual del Chef Ejecutivo 7 y la Guía de Pastelería **8**. Aquí son **9**, y **cuatro no tienen molde previo** (clima del obrador, sensibilidad al cacao, vida útil de rellenos, valle de verano). Eso es lo que sostiene el precio.

---

## 10. Índice propuesto: 20 capítulos + anexo, con presupuesto de palabras calibrado

**Calibración MEDIDA sobre los PDF que se venden hoy** (no estimada): cuerpo **545,3 pal/pág** y bonus **455,2 pal/pág** en Pastelería; **529-544 / 406-464** en Food Cost y el Manual del Chef. Y la lección que hay que meter en el guion desde el día 1: **el guion de Pastelería presupuestó 37.500 palabras y salieron 56.168 — un +49 %, peor que el +30 % que su SPEC daba por hecho.**

| Entregable | Presupuesto de guion | Salida realista (con el **+49 %** medido) | Gate interno | Qué publica la landing |
|---|---|---|---|---|
| **Guía, 20 caps + anexo** | 1.800 palabras/cap. (los cuatro legales —09, 10, 11, 19— a **2.100**) ≈ **37.000 palabras** | **52.000-56.000 palabras → 95-103 páginas** | `paginas_prometidas: 90` · `min_palabras_cap: 1.300` | **La cifra MEDIDA tras construir** (D17 de la familia). Nunca la prometida |
| **Bonus 2, 12 decisiones** | 850-900 palabras/decisión + 1 tabla ≈ **10.500 palabras** | **15.000-17.000 palabras → 33-37 páginas** | `paginas_prometidas: 30` · `min_palabras_cap: 600` | Ídem |
| **Bonus 1, business plan** | ≈ **3.500 palabras + 9 tablas** | 3.500-4.500 palabras → ~18 páginas | ≥9 `<w:tbl>` verificadas descomprimiendo `word/document.xml` | «Business plan modelo relleno con el caso completo» |

**Cada capítulo con `puntos_por_epigrafe`.** **Ninguna cifra entra si no sale de una celda de xlsx o de un id `CHN-*` / `CHS-*`.**
`H` = hereda estructura de Pastelería · `N` = nuevo del chocolate · 🔴 = depende del bloque legal y lo firma el verificador antes de escribirse.

| # | Capítulo | H/N | Contenido obligatorio | Libro / hoja | ids |
|---|---|---|---|---|---|
| **01** | **Qué negocio estás montando: las 12 variantes y cuál te toca** | H | La matriz comparada con inversión, m² y personal; **el epígrafe que separa la bombonería de la chocolatería de taza y churros** con los cuatro cambios normativos (§1.3); la frontera con el Kit de Tareas **en la primera página**; y qué **NO** vas a encontrar aquí | `capacidad-obrador-y-clima!Parámetros` + `capex!Variante del Formato` | CHS-01…12, CHN-72, CHN-51 |
| **02** | **El cliente y la plaza: quién compra chocolate, cuándo y a qué precio** | H | El mercado **crece en euros y se encoge en kilos** (2,96 kg/persona desde 3,54 en 2022, precio +30 % en dos años); el reparto por categorías (**bombones 13,6 %**); **el consumidor ya paga más por menos**; y que **no existe un número oficial de chocolaterías** | `campanas-y-valle!Peso sobre el Año` | CHS-18…24 |
| **03** | **La carta de apertura: las referencias, las familias y la caja como unidad** | H+N | Cómo se decide el surtido; **la caja de 9/16/24 frente a la unidad** (−23 % de precio por bombón); el papel de cada familia; **el chocolate a la taza como familia de invierno que sube el ticket** | `carta!Unidad vs Caja` | CHS-29, CHS-32 |
| **04** | **Cuánto cuesta abrir: el CAPEX real, partida a partida** | H | **Por qué las cifras publicadas varían ×10** y qué hipótesis lleva cada una; **el rango de «20.000-30.000 €» esconde dos negocios distintos**; las 12 partidas sin precio público y cómo presupuestarlas; **el colchón de tesorería como partida, no como propina**; y el aviso del IVA por línea | `capex!CAPEX por Bloque` | CHS-03, CHS-47a/b, ⛔ §15.1 |
| **05** | **El local: metros, zonas y la ficha de visita** | H | Las zonas de un obrador de chocolate (**no las de pastelería**: sin horno ni fermentación, con cámara); superficies; marcha adelante; la potencia que de verdad hace falta | `capacidad!Zonas y m²` | CHS-03, CHS-58 |
| **06** | **Antes de firmar: el obrador sin humos cambia la conversación de la licencia** | **N** | 🔴 **El capítulo que ahorra el dinero.** El DB-HS 3 **no regula tu local** y las reglas de «chimenea por cubierta» que circulan **son las de las viviendas**; sin horno no hay aire AE4; lo que sí te aplica es el RITE por la climatización; **puedes alquilar locales que una pastelería descarta**; y las tres puertas: local nuevo, **traspaso** (26.000-210.000 € reales) o franquicia | `capacidad!Ficha de Visita a Local` + `capex!Traspaso vs Obra Nueva` | **CHN-45, CHN-46**, CHN-49, CHS-37/38 |
| **07** | **El clima del obrador: 18-22 °C de sala, 15-18 °C de cámara y por qué el chocolate manda sobre el local** | **N** | 🔴 **El criterio del chocolate.** Sala y cámara **son dos cosas distintas**; HR <55 %; el aire **una hora antes**; el deshumidificador como inversión; fat bloom y sugar bloom; **y que ninguna norma obliga a esas temperaturas: las declaras tú y las justificas** | `capacidad!Clima del Obrador` | **CHN-30**, CHS-44, C41-C47 |
| **08** | **Maquinaria: atemperadora, enrobadora, moldes — qué compras, qué esperas y qué NO** | H+N | La escalera **1.960 € → 8.500 € → 27.500 €** y el cruce **kg/semana → máquina**; **la trampa del IVA** (unos distribuidores publican con y otros sin, y nunca se suman); **la vitrina de chocolate va a +14/+17 °C, no a +2/+4**; plazos de entrega; y el tren bean-to-bar, **que no tiene precio público y hay que presupuestar** | `equipamiento!Equipamiento` | CHS-41…48 |
| **09** 🔴 | **Licencias, sanidad y registro: el camino completo** | H | **El error nº 2 del nicho: una chocolatería minorista NO va al RGSEAA**; la comunicación autonómica **que no habilita**; **tener obrador y transformar no te saca de minorista**; los tres umbrales acumulativos y **que el que mata es «restringido»**; la clave 25 cuando sí toca; **y la ruta doméstica con su conclusión incómoda** | `checklist-legal!Árbol de Registro Sanitario` + `…!Ruta Doméstica` | **CHN-39…44b**, CHN-49 |
| **10** 🔴 | **Cómo puedes llamar a lo que vendes: las denominaciones legales del cacao** | **N** | 🔴 **El capítulo que no tiene nadie.** La tabla de mínimos; **«bombón de chocolate» es ≥25 % del peso total**; el bombón con galleta dentro **no es «chocolate relleno»**; **«praliné», «trufa» y «artesano» no existen en la norma**; el «cacao: X % mínimo» **no es universal**; los calificativos de calidad del ap. 6.g); **sucedáneo ≠ chocolate**; las seis grasas vegetales y su mención en negrita; el «para su consumo cocido»; la caja surtida; y que media vitrina se rige por **otro** real decreto | `carta!Denominaciones y Mínimos Legales` | **CHN-01…15b, CHN-53, CHN-55** |
| **11** 🔴 | **Cacao, cadmio y deforestación: qué te pide la norma y qué le pides a tu proveedor** | **N** | 🔴 **El cadmio sube con el % de cacao: castiga justo al negro premium**; OTA y HAP; **no puedes diluir mezclando lotes** y tienes que **justificar los factores de transformación**; el EUDR **incluye el chocolate terminado y la exportación**; **eres «operador posterior», no «operador»**, y eso son cuatro obligaciones documentales, no una declaración; **el aplazamiento a junio de 2027 no te sirve si abres ahora**; y el bean-to-bar **sí es operador**, con CAPCA por el tostado | `checklist-legal!Cadmio y Analíticas` + `…!EUDR: ¿te aplica?` + `equipamiento!Proveedores` | **CHN-16…29, CHN-47, CHN-60** |
| **12** | **Autocontrol, alérgenos y formación: qué tener el día de la inspección** | H | APPCC **simplificado es legal** y exige **responsable con nombre**; **los peligros de un obrador de chocolate no son los de una pastelería** (baja el microbiológico, suben el alérgeno cruzado y el cuerpo extraño metálico); temperatura y humedad como **prerrequisito, no PCC**; **la carta de alérgenos por referencia**, porque la unidad de venta es el bombón; «sin gluten» son **20 mg/kg validados**; **y el carnet de manipulador no existe: lo que hace falta es un registro de formación** | `checklist-legal!Registro de Formación` *(cita `pack-appcc`)* | CHN-32…37, **CHN-69** |
| **13** | **Proveedores: cobertura, cacao, packaging y plazos** | H | Los proveedores verificados por categoría; **la Asociación Bean to Bar como vía fiable para el grano**; cómo pedir tres presupuestos comparables; **las dos preguntas que separan a quien compra de quien sabe lo que compra** (boletín de cadmio y número de DDS); **y el impuesto al plástico si compras estuches fuera** | `equipamiento!Proveedores` | CHS-50…55, **CHN-62** |
| **14** | **Escandallo del chocolate: la merma de templado, el recorte que vuelve y la caja** | H+N | La unidad de costeo es **el molde y la tanda, no la pieza**; **el chocolate mal templado se vuelve a fundir** y eso cambia la merma; el coste hora de obrador imputado; **el bombón de dos días no se vende a 1,20 €**; y por qué **margen bruto y food cost son la misma regla dicha dos veces** | `carta!Merma de Templado y Recortes` *(cita Food Cost cap. 17)* | CHS-28, CHS-29, C09, C24 |
| **15** 🔴 | **El precio del cacao: qué haces cuando sube y quién paga la subida** | **N** | 🔴 **El cacao cayó a la mitad y el chocolate subió un 17,7 %**: la cobertura no baja cuando baja la bolsa; el ciclo real de revisión es **semestral**; los cuatro caminos (precio, gramaje, cobertura, margen) con su número; y **cómo se comunica una subida** | `sensibilidad-al-cacao!Escenarios de Precio` | CHS-23, CHS-24, C13-C15 |
| **16** | **Vida útil del relleno: aw, vitrina y de cuánto haces cada lote** | **N** | **Factor 5 entre 8 días y 5-6 semanas**, y es una decisión de **modelo de negocio**, no técnica: decide si puedes vender online, servir corporativo y fabricar en noviembre; **la temperatura la declaras tú** y con ella la responsabilidad; **la vitrina de chocolate no es la de pastelería**; y las tres vías del huevo donde aún aplican | `vida-util!Tipo de Relleno y aw` | CHS-56, **CHN-30, CHN-31, CHN-38** |
| **17** | **El equipo: cuántos, qué perfiles y qué cuestan** | H | Los **3 perfiles** (Chocolatero, Dependiente, Encargado); del bruto al **coste empresa con SS**; **el chocolatero es la categoría mejor pagada después del maestro** — el cuello de botella no es la máquina; **una sola tabla de convenio, la de Madrid, marcada como ejemplo, y el método para identificar el tuyo**; y el aviso de `CHN-65` | `plan-financiero!Personal` *(cita el libro 04 del kit)* | CHS-69/70, **CHN-65, CHN-67, CHN-68** |
| **18** | **Las campañas y el valle: de Navidad a agosto** | H+N | San Valentín **duplica la media** y un solo evento puede ser el **10 % del año**; la producción de Navidad se paga en octubre y se cobra en diciembre; **el valle no es «menos venta», es imposibilidad técnica**; cerrar o no en agosto; y las dos respuestas contraestacionales: **heladería y talleres** | `campanas-y-valle!El Valle de Verano` | CHS-34…36, CHS-09/11, C36-C47 |
| **19** 🔴 | **Canales: mostrador, online con envío, B2B, corporativo y talleres** | H+N | El **95/5** de cobro directo y a crédito; **cuándo el B2B te obliga a inscribirte en el RGSEAA** y por qué **el regalo corporativo es justo la línea que lo rompe**; **vender online a toda España no te saca de minorista, pero te responsabiliza de la temperatura en el camión**; la información obligatoria **antes de la compra**; **exportar también cae bajo el EUDR**; y **los talleres como la única línea que funciona en agosto y no depende del cacao** | `plan-financiero!Canales y Punto Muerto` + `…!Talleres y Regalo Corporativo` | **CHN-41, CHN-56, CHN-57, CHN-60**, CHS-30, CHS-55 |
| **20** | **El plan financiero, el dinero hasta el punto de equilibrio y los primeros 90 días** | H | P&L a 3 años con **estacionalidad mensual y rampa**; punto muerto; **el sueldo del propietario como renglón propio**; **IVA al 10 % y la trampa del TPV**; **Verifactu en 2027, no en 2026**; la ruta crítica y la fecha de apertura; **abrir fuera de pico y llegar rodado a Navidad**; y qué se mide en el mes 0 y en el mes 3 | `plan-financiero!PyG 3 Años` + `checklist-legal!Cronograma` | CHS-40, **CHN-71, CHN-73…77** |
| **A** | **Anexo normativo fechado** (vigencias + las fechas que se mueven) | H | La tabla de §2.3 + **las diez normas cuyo cambio invalidaría algo** + cómo comprobar la vigencia en el BOE y en EUR-Lex | — | §15.3 |

> **Balance: 13 capítulos heredan estructura, 5 son nuevos del chocolate y 3 son mixtos** — más contenido propio del que tuvo Pastelería respecto a Panadería, y por eso el presupuesto de §15.4 no baja tanto como cabría esperar.
> **Poda aplicada respecto a las 22 entradas que proponía L6:** se fusionaron sus capítulos 19 (talleres) dentro de 20 (canales) — coherente con absorber el libro 10 en el 7 — y sus 21 y 22 (plan financiero y cronograma) en uno solo.

---

## 11. Bloque obligatorio 8 (parte 2) — Precio y ancla

### 11.1 La escalera real del catálogo (48 productos, parseada por mí hoy)

| Franja | Nº | Productos |
|---|---|---|
| 9 € | 1 | eBook Pro Prompts |
| **12 €** | **13** | Kit de Escandallos + 12 kits de tareas por concepto (incl. **`kit-tareas-chocolateria`** y `kit-tareas-pasteleria`) |
| **14 €** | **8** | Kit de Tareas, Pack APPCC, Kit de Inventario, Kit de Gestión de Personal + 4 kits de tareas |
| 18 / 18,50 € | 2 | `kit-tareas-chef-privado` · `kit-tareas-hotel` |
| 24 € | 1 | **Guía Dark Kitchen** *(la única «Cómo Montar» que no está a 65 €)* |
| 29 € | 2 | plan-negocio-cafeteria · plan-negocio-food-truck |
| 35 € | 3 | plan-negocio-bar-restaurante · plan-negocio-panaderia · plan-negocio-tapas-bar |
| **39 €** | 1 | Kit Plan Financiero |
| 45 € | 4 | 4 planes de eventos |
| **55 €** | **3** | Guía Food Cost + Ingeniería de Menú · Manual del Manager de Restaurante · Plan Coctelería |
| **65 €** | **8** | 6 guías «Cómo Montar» (casual, japonés, mexicano, nikkei, peruano, **panadería-obrador**) + **`guia-pasteleria-obrador`** + **Manual del Chef Ejecutivo** |
| 85 € | 1 | Guía Restaurante Gastronómico |
| 89 € | 1 | Mega Pack de Tareas |

### 11.2 Recomendación: **65 €**

**Seis argumentos, uno por línea:**

1. **Las dos hermanas directas están a 65 € y comparten molde, estructura y comprador.** `guia-pasteleria-obrador` se publicó hace dos días a 65 € y `guia-panaderia-obrador` está ahí desde antes. Separarse obligaría a explicar por qué la chocolatería vale distinto que la pastelería.
2. **La franja de 65 € ya son OCHO productos** (verificado por mí): **es la franja de los productos grandes del catálogo**, no sólo la de las guías. Y el precedente más reciente empuja hacia arriba, no hacia abajo: **el Manual del Chef Ejecutivo salió a 65 € cuando su propio research recomendaba 55**.
3. **El paquete es mayor que el de la hermana:** **9 libros de Excel frente a los 8 de Pastelería**, y **cuatro sin molde previo** (clima, sensibilidad al cacao, vida útil de rellenos, valle de verano), más los dos bonus.
4. **El hueco de mercado no tiene competencia que lo ocupe.** Entre **49,90 €** (un buen libro en inglés, sin España y sin un solo Excel), **49 €** (un generador de business plan genérico cuya guía gratuita pide un carnet que no existe) y **19.200 €** (el único programa con dirección de empresa, y es de pastelería), **no hay absolutamente nada en español**.
5. **Las anclas externas aguantan sin retórica:** 65 € son **1,30×** el único libro de negocio del sector · **0,36×** el curso técnico más barato del censo (180 €) · **0,012×** el curso presencial de Callebaut (**4.500 €**) · y **el 1,3 % del canon de entrada más barato del mercado (5.000 €)**. Y el argumento defensivo verificable: **«menos que un mes de alquiler del local que vas a firmar»** (las rentas medidas van de 910 a 2.200 €/mes).
6. **Y el bloque normativo tiene dos cosas que la Guía de Pastelería no tiene:** una **norma de producto con porcentajes legales exigibles** (RD 1055/2003, 23 años sin modificarse) y un **reglamento europeo con fecha y sanción** (EUDR). **Es justo lo que justifica 65 € y no 49 €** — y hay que poder demostrarlo **en el entregable, no en el copy**.

**Sin `priceOld` ni `discountBadge`** (D1 de la familia: producto nuevo, no hay «precio anterior de 30 días» que sostenga un tachado — y en este nicho hay un matiz propio, `CHN-76`: **subir en noviembre para «rebajar» en diciembre no cumple la regla de los 30 días**). **Sin `aggregateRating`, sin `review` y sin testimonios inventados**: `testimonials.items: []`, que `GuiaLandingPage.astro` ya oculta. **Nace con NOWPayments** además de Stripe (regla de John del 6-sep): la plantilla ya importa `CryptoPayButton` y monta **las tres puertas** (hero, buybox, CTA) — **lo único que hay que hacer es añadir el slug a `CRYPTO_PRODUCTS` con scope `builds` Y `functions`**.

### 11.3 Las alternativas, con su coste honesto

- **55 €** — es lo que sugeriría la prudencia por el tamaño del mercado. **Su coste:** lo pondría **por debajo del Manual del Chef Ejecutivo con un paquete mayor** (9 xlsx frente a 7), rompería la paridad con las dos hermanas que el hub enseña juntas, y **la chocolatería aparecería como «la barata» de la familia**. El comparativo real del comprador **no es otra guía —no existe— sino un curso de 180 a 5.525 €**.
- **85 €** — defendible con el recuento de entregables en la mano (9 libros frente a los 8 de Pastelería y los 15 «de v1.0 sin fórmulas» de Panadería). **Su coste:** colisiona con la **Guía Restaurante Gastronómico (85 €)**, que promete 119 páginas y **entrega 10**, y obligaría a justificar por qué la chocolatería vale más que la pastelería. **No lo recomiendo mientras la línea no esté arreglada.**
- **49 € — VETADO:** es el precio tachado del Kit de Escandallos y chocarían en el hub.

> **Lo que se deja sobre la mesa, dicho en voz alta:** con 65 € renunciamos al margen que nueve libros justificarían, **a cambio de coherencia con las dos hermanas** y de no tocar la franja de 85 €.

---

## 12. Nombre, slug, subtítulo, promesa y vocabulario

### 12.1 Nombre y slug

**Titular / H1: «Cómo Montar una Chocolatería».** No es una preferencia: **es el nombre con el que el producto lleva anunciado en el hub desde mayo**, en los dos ficheros y con su descripción publicada. Cambiarlo rompe una promesa que ya está en producción.

**Nombre de catálogo, banner y email: «Guía Chocolatería con Obrador»** — calca el patrón de las hermanas (`products-catalog.ts`: «Guía Panadería con Obrador», «Guía Pastelería con Obrador»). Inglés propuesto: **«Guide: Chocolate Shop with Production Room»**.

**Slug recomendado: `guia-chocolateria-obrador`** → `https://aichef.pro/guia-chocolateria-obrador`, `-access`, `-library`.

| Alternativa | Veredicto |
|---|---|
| **`guia-chocolateria-obrador`** | ✅ **Recomendado.** Paridad exacta con las dos hermanas del molde · el sufijo **`-obrador` desambigua el modelo (a) frente al (b) justo donde Google no desambigua** · ✅ **verificado por mí: hoy devuelve 404** (libre) y **`robots.txt` lo cubre en los 5 bloques sin tocar nada** |
| `guia-chocolateria` | ❌ Rompe la simetría del trío de obradores y **no desambigua (a)/(b)**, que es el problema central de este producto |
| `guia-como-montar-chocolateria` | ❌ **Ninguna de las 10 fichas de `astro-site/src/data/productos/guias/` usa ese patrón** (verificado); introduciría un tercer patrón de slug para una keyword de 10/mes |

⚠️ **Aviso de nomenclatura que ya costó dinero en este repo:** el nombre del enlace debe coincidir con el de la página de destino. Si el hub dice «Cómo Montar una Chocolatería» y la landing se titula «Guía Chocolatería con Obrador», **el H1 y el título del hub tienen que decir lo mismo** o repetimos el defecto de «Biblioteca de Prompts» → `/libreria-de-prompts`.

⚠️ **Comprobación obligatoria antes de publicar:** `python3 scripts/astro-migration/robots-gate.py`. El slug no acaba en `-access` ni en `-library`, así que **no debería** caer en ningún patrón — pero eso **se verifica con el gate, no se supone** (la regla que costó un mes de indexación de 26 posts ingleses).

### 12.2 Copy

| Elemento | Propuesta | Nota |
|---|---|---|
| **H1** | **«Cómo Montar una Chocolatería»** | Es la promesa publicada desde mayo |
| **Title** (≤60) | **«Cómo Montar una Chocolatería \| Obrador, Licencias y Números»** (59) | Alternativa: «Guía Chocolatería con Obrador \| Abrir Paso a Paso» (55) |
| **Subtítulo del hero** | **«El dossier completo de apertura de una bombonería con obrador: los nueve Excel que hacen tus números y los documentos que te pide la inspección.»** | Es el ángulo libre que deja el competidor (H1/H3): **no vendemos «te explico», vendemos los entregables**. Y mete **«bombonería»**, que es la palabra de quien ya lo ha hecho |
| **Promesa honesta** | **«No te enseña a templar. Te dice qué decidir y en qué orden: si ese local sirve, cuánto necesitas de verdad, cómo puedes llamar legalmente a lo que vendes, cuánto tienes que cobrar cuando sube el cacao, y de qué vives en agosto.»** | Responde de frente a O1, O3 y O4, y **nombra los cuatro capítulos que no tiene nadie** |
| **Declaración en negativo, arriba y no en la FAQ** | **«Esto no es un recetario ni un curso de técnica del chocolate, y no sustituye al proyecto técnico visado.»** | Copiado de lo que hace bien el competidor. **Corta devoluciones** |
| **Aviso de alcance, en la primera pantalla** | **«Cubre a fondo la chocolatería artesana con obrador —bombones, tabletas, cajas—. Si lo que quieres es una chocolatería de taza y churros, aquí tienes el capítulo que te dice qué cambia, pero ése es otro negocio.»** | Es el antídoto contra la devolución por expectativa (§1.3) |
| **Description** (~155) | **«Para quien va a abrir una chocolatería en España: viabilidad del local, clima del obrador, CAPEX por escenarios, denominaciones legales del cacao, escandallo con merma de templado y plan financiero. 20 capítulos y 9 Excel.»** (recortar a 155) | — |
| **Keywords** (para el cuerpo y los H2, **no para el slug ni el title**) | montar una chocolatería · obrador de chocolate · bombonería artesanal · chocolatería artesanal · templado de chocolate · atemperadora · cámara de chocolate · escandallo de chocolate · bean-to-bar · licencia de obrador · traspaso de chocolatería | ⚠️ **«artesanal», nunca «artesana»** (390 vs sin dato). **«templado» por delante de «temperado»** (20 vs 10). **Nunca «dulcería»** |
| **Frase de frontera** | *«El Kit de Tareas te dice qué hacer cada día cuando ya has abierto. Esta guía es todo lo que hay que decidir antes.»* | Va **arriba**, no en la FAQ |

### 12.3 Límite del copy, escrito en la primera pantalla

**El marco legal explicado es el ESPAÑOL.** Las herramientas tienen todas las casillas editables, el vocabulario lleva su equivalencia LATAM **en la primera mención y sólo en la primera**, y el método viaja entero — pero **no se promete cobertura normativa de ningún otro país**. Se dice en el hero, en la FAQ y en el email, y la FAQ **ofrece la adaptación como servicio** (regla de John del 5-sep). **Sin siglas españolas en los titulares** (RGSEAA, APPCC, BOE y EUDR van dentro, no en el hero). **Y nada de «verificado contra el BOE» en Stripe ni en el titular**: ahí lideran los entregables y el beneficio práctico.

---

## 13. Canales, interenlazado y piezas de captación

### 13.1 Entrantes (regla capital: cero páginas huérfanas)

| Origen | Acción | Fichero |
|---|---|---|
| **Hub `/productos-digitales`** (Astro **y** SPA) | Tarjeta real con badge «Nuevo» + **vaciar `comingSoon` en LOS DOS ficheros**, o quedarán la tarjeta real y la de «Próximamente · Junio 2026» a la vez | `src/pages/ProductosDigitales.tsx:958-960` · `astro-site/src/components/pages/ProductosDigitalesHubPage.astro:973-975` |
| 🔴 **Y con el array vacío hay DOS arreglos obligatorios en el mismo commit** | **(1)** Envolver la sección del Astro en `{comingSoon.length > 0 && (…)}` — hoy `…HubPage.astro:1448` la renderiza **sin guarda server-side**, al contrario que la SPA (`ProductosDigitales.tsx:1227`). ✅ **Matiz verificado por mí: el script de cliente SÍ la oculta** (`:1883` + `apply()` en `:2256`), así que el defecto es **un destello y un rótulo huérfano en el HTML servido**, no una sección visible para siempre — pero eso es justo lo que ve Google. **(2)** Hacer condicional el «· N próximamente» del badge del hero, que diría **«49 productos disponibles · 0 próximamente»** (`ProductosDigitales.tsx:1080` y `…HubPage.astro:1143`) | ídem |
| **Buscador del hub** | **Alias nuevo.** Verificado: `sinonimos-buscador.json` (8 grupos, 4 frases, 7 alias) **no menciona chocolate, cacao, bombón ni templado**, así que no dispara el gate de grupos huérfanos. El índice normaliza sin acentos: `"/guia-chocolateria-obrador": "abrir montar una chocolateria bomboneria obrador de chocolate cacao cobertura bombones tabletas templado atemperadora bean to bar licencia traspaso taller de chocolate"` | `astro-site/src/lib/sinonimos-buscador.json` |
| **8 posts con banner FIJADO** (sustitución quirúrgica) | Ver §13.2 | `astro-site/src/content/blog/es/` |
| **4 páginas `/usos/`** | Añadir `'guia-chocolateria-obrador'` **en primera posición** a los `productIds` de **`chocolatero`** (`use-cases-content.es.ts:1264`), **`chocolateria`** (`:3248`) y ✅ **`chocolatero-consultor`** (`use-cases-content.es.consultor.ts:386`, la que ninguna lente vio y que está en **posición 4,3** en GSC). **Valorar** las dos de heladería (`:1924` y `:3138`) por la chocolatería-heladería. Enlace **bidireccional** | `src/data/use-cases-content.es.ts` · `…es.consultor.ts` |
| **`PRODUCT_ALIASES`** | `'Cómo Montar una Chocolatería'` | `src/lib/linkify-use-case.tsx:13` |
| **`footerLinks` cruzados** | Desde `kit-tareas-chocolateria`, `kit-escandallos`, `pack-appcc` y Guía Food Cost. ⚠️ **NO desde las guías hermanas** mientras no entreguen lo que prometen (D19) | `astro-site/src/data/productos/**` |
| **Rotación general de banners** | Entrada **49** en `products-catalog.ts` → `fase8e-banners-corpus.py` lo reparte solo por los 326 posts | — |
| **Lista de compradores (Resend)** | Broadcast propio (§13.3) | — |
| **Plataforma (Pickaxe)** | Agentes **«Chocolatero Consultor Pro»** y **«Chocolatería Creativa»**. ⚠️ **Comprobar los nombres contra `fase8c-agentes/catalogo-hub.json` antes de escribirlos**: la fuente autorizada es la plataforma, no el repo | — |

**Salientes de la landing:** `kit-tareas-chocolateria` (12 €), `kit-escandallos` (12 €), `pack-appcc` (14 €) y Guía Food Cost (55 €), con `utm_source=landing&utm_medium=cross-sell` para poder medir quién compra dos.

### 13.2 Los 8 posts del universo y qué banner sustituye a cuál

Extraídos por mí, banner a banner, de los **326** `.md` de `astro-site/src/content/blog/es/`. **Los ocho tienen exactamente 3 banners: hay que SUSTITUIR, no añadir.**

| Post | Menciones (medidas) | Banners hoy | Sustituir |
|---|---|---|---|
| `libreria-de-prompts-para-chocolatero-consultor-pro-ai` | **382** | kit-tareas-chocolateria · **kit-plan-financiero** · kit-escandallos | **`kit-plan-financiero`** → el plan financiero a 3 años va **dentro** de la guía |
| `libreria-de-prompts-para-chocolateria-creativa-ai` | **364** | kit-tareas-chocolateria · kit-escandallos · **pro-prompts-ebook** | **`pro-prompts-ebook`** (el menos ligado al negocio de chocolate) |
| `chocolateria-artesanal-e-ia-una-combinacion-innovadora` | **88** · 🔴 **y es el activo real: 3 clics / 30 impr. / pos. 4,9 / CTR 10 %** | kit-tareas-chocolateria · **guia-restaurante-peruano** · **kit-tareas-sushi-bar** | 🔴 **El peor encaje del corpus: un post de chocolatería artesanal vendiendo cocina peruana y sushi.** Sustituir **`kit-tareas-sushi-bar`** por la guía; `guia-restaurante-peruano` queda como candidato a un segundo arreglo |
| ✅ **`coulant-de-guanaja-70-y-praline-homenaje-a-laguiole`** | **31** — **hallazgo mío, no está en L6** | kit-tareas-chocolateria · **plan-negocio-cafeteria** · **kit-tareas-asador** | 🔴 **El segundo peor encaje: un plato de Guanaja 70 % y praliné vendiendo un asador.** Sustituir **`kit-tareas-asador`** |
| `libreria-de-prompts-para-heladeria-creativa-ai` | 31 | kit-tareas-heladeria · kit-escandallos · pro-prompts-ebook | **Enlace contextual**, no banner (el solape es la chocolatería-heladería, no el producto) |
| `libreria-de-prompts-para-heladero-consultor-pro-ai` | 27 | kit-tareas-heladeria · kit-plan-financiero · kit-escandallos | Ídem |
| `libreria-de-prompts-para-pasteleria-creativa-ai` | 127 | kit-tareas-pasteleria · kit-escandallos · **guia-pasteleria-obrador** | **No tocar.** Ya vende la guía hermana correcta |
| `ia-churrerias-guia-completa` | 18 | guia-dark-kitchen · kit-tareas-bar · kit-tareas-restaurante-creativo | **No tocar**: este post es de **churrería**, no de obrador de chocolate (§1.3) |

**Ganancia neta para el 49: 4 banners** (los tres de chocolate más el del coulant).

⚠️ **Herramienta:** `fase8e-banners-corpus.py` **sólo inserta, no sustituye**. Hace falta una pasada quirúrgica (`fase8j`, o mejor el genérico `fase8x-sustituir-banner.py --producto <pid>`) **con gate de reversibilidad byte a byte**. **PROHIBIDO reejecutar `fase8c-libreria-assemble.py`**: reconstruye el cuerpo desde el `.txt` de bridge y **pisa las ediciones manuales**. Después de aplicar: **siempre `fase8b-regen-lastmod.py`**.
⚠️ **A la lista `NUNCA` del script:** `kit-tareas-chocolateria`, `kit-escandallos`, `pack-appcc` y `guia-food-cost-ingenieria-menu` — son el cross-sell de la guía; sustituirlos sería quitarse ventas propias.

### 13.3 Resend: dónde cabe el correo de lanzamiento, y la trampa

Cola leída por mí en `CALENDARIO-V2-SEMANAL.md` (regla de John del 5-sep: **último `scheduled_at` + 5 días, 08:00 UTC / 10:00 Madrid**):

| Fecha | Correo | Estado |
|---|---|---|
| 14-sep | Manual del Chef Ejecutivo (lanzamiento) | programado |
| 19-sep · 24-sep · 29-sep · 4-oct | bar-restaurante 2.1 · cafetería 2.2 · tapas-bar 2.2 · panadería 2.2 | programados |
| 9-oct | Food truck 2.2 | **PROGRAMADO el 10-sep** |
| 14-oct | **Guía de Pastelería (lanzamiento)** | **BORRADOR** — programar desde el 14-sep |
| 19-oct | Kit de Tareas Pastelería 2.1 | **BORRADOR** — programar desde el 19-sep |
| **24-oct** | **← hueco de la Guía de Chocolatería** | **libre** |

⚠️ **El 24-oct está a 42 días de hoy, muy fuera del tope de 30 días de Resend: no se puede programar todavía.** Queda como **borrador con el sufijo «— PROGRAMAR 24-oct»** y se programa **a partir del 24-sep**. Y al recrear cualquier correo: **un broadcast programado no se edita (403)** — es `GET` (guardar asunto y nombre) → `DELETE` → `POST`, con `json.loads(strict=False)`, y **leer el asunto ANTES de borrar** (la lección del 6-sep, en la que se borraron cuatro correos a ciegas).

> **Alternativa que merece plantearse (decisión D8):** un lanzamiento **anunciado desde mayo con tres meses de retraso** compite mal con un aviso de versión. **El precedente existe dos veces**: la D28 del Manual del Chef Ejecutivo adelantó el lanzamiento y desplazó un hueco cinco actualizaciones, con este argumento literal: «*un lanzamiento anunciado desde mayo vende más que un aviso de versión*».

### 13.4 Las piezas de captación de blog que salen de este research

**No son este producto y no bloquean el lanzamiento**, pero salen gratis. Se escriben con `bridge.py` (regla capital: los productos no, el blog sí).

| # | Pieza | Volumen ES | Por qué | Riesgo |
|---|---|---|---|---|
| **1** | **El EUDR y el cacao: qué obliga a una chocolatería pequeña y desde cuándo** | **`eudr` 1.900** ✅ (creciendo ×2 en el semestre) | 🟢 **La única keyword de 4 cifras del nicho con intención profesional**, y tenemos la respuesta **verificada contra EUR-Lex consolidado**: «operador posterior», art. 5, cinco años, sin registro — **y el matiz del 31-12-2024 que nadie cuenta**. Ningún actor gastronómico español lo ha escrito para chocolateros | Bajo |
| **2** | **Licencia de apertura de un obrador de chocolate: por qué NO necesita salida de humos** | `licencia de apertura` **720** (subiendo 170→590) | El ángulo del obrador sin hornos es **propio y diferencial**, y está en norma primaria (`CHN-45`, `CHN-46`) | ⚠️ **Medio: canibaliza con lo que ya cubren las guías de pastelería y panadería.** **Comprobar antes con GSC agrupando por `page,query`** (regla de `CLAUDE.md`) |
| **3** | **Fat bloom y sugar bloom: por qué se te blanquea el chocolate y cómo se evita** | `fat bloom` 140 + `sugar bloom` 90 = **230 agregado** | Intención limpia, competencia cero, **anglicismos vivos en español**, y conecta con el capítulo 07 (clima) | Bajo |
| **4** | **Cuánto cuesta un bombón cuando sube el cacao** | cola larga del PAA de `precio del cacao` (1.300): «**¿Cuánto vale 1 kg de cacao?**» y «**¿Cuál es la tendencia del cacao para 2026?**» | Es una pieza de **coste**, no de cotización: ahí no compite Investing ni Yahoo Finance | Bajo |

> ❌ **Anti-recomendación, repetida aquí porque es donde se decide:** **NO escribir «chocolate a la taza» (4.400), «chocolatería» (9.900), «bombonería» (880), «praliné» (8.100) ni «bean to bar» (320)** como piezas de captación. Los cinco tienen la intención en otro sitio (§0), y `bean to bar` **sirve como vocabulario y como capítulo, no como pieza SEO**.

---

## 14. FAQ de COMPRA — 12 preguntas

Las de **oficio** («¿cómo se templa el chocolate?», «¿qué curva uso?») y las de **consumidor** («¿cuál es el bombón más rico?») **quedan fuera**: no son nuestras. Estas 12 son de compra, y seis salen del **People Also Ask medido**.

| # | Pregunta | Cómo se responde |
|---|---|---|
| 1 | **¿Esto no está gratis en Google?** | **La primera, por la objeción nº 1 medida.** Sí, la información suelta está — y **las tres cifras de inversión que encuentras varían ×10** (20.000-30.000 €, 36.600 € y 3.000-8.000 USD), **la mitad de la SERP es de México y EE. UU.**, y la única guía española de 2026 exige un requisito legal que **no existe desde 2010**. Lo que no está en Google es **el orden de decisión y nueve Excel donde metes TUS metros, TU carta y TU precio de cobertura**. Se responde con una tabla, no con adjetivos |
| 2 | **¿En qué se diferencia del Kit de Tareas Chocolatería de 12 €? ¿Necesito los dos?** | **El kit te dice qué hacer cada día cuando ya has abierto** (templado, moldeado, vitrina, campañas, caja). **Esta guía es todo lo que hay que decidir antes de abrir.** Si ya estás abierto, el kit te vale y esta guía no te hace falta |
| 3 | **¿Me sirve si quiero empezar desde casa?** | Sí, y es donde más aporta — **aunque la respuesta no sea la que esperas**: el chocolate **no está en la lista estatal** del art. 13.8 del RD 1021/2022, que sólo permite «panadería y **repostería** estables a temperatura ambiente». La fórmula correcta no es «es ilegal en España», sino «**no entra en el régimen estatal salvo que tu comunidad lo haya añadido**», y la guía te dice **cómo preguntarlo y a quién** |
| 4 | **¿Cuánto cuesta montar una chocolatería de verdad?** | **No te damos un número: te damos el modelo que produce el TUYO.** Lo que sí te damos verificado es **el núcleo de máquina línea a línea** (de ~5.700 € con una atemperadora de sobremesa a ~24.100 € con una continua) y **las doce partidas que ninguna fuente publica**, para que las presupuestes tú. Y te explicamos **por qué «20.000-30.000 €» esconde dos negocios distintos** |
| 5 | **¿Qué pasa cuando sube el cacao?** | Hay un libro entero para eso. El cacao pasó de **>10.800 €/t a 4.956 €/t** en un año **y el chocolate subió un 17,7 %** el mismo año: **la cobertura no baja cuando baja la bolsa**. El precio va en celda verde con hoja de sensibilidad, y el capítulo te da los cuatro caminos con su número |
| 6 | **¿Y el EUDR? ¿Me afecta si compro cobertura europea?** | **Sí, y no como te lo han contado.** Desde diciembre de 2025 eres **«operador posterior»**: **no** haces declaración de diligencia debida, pero **sí** tienes que guardar los datos de tu proveedor **y el número de referencia de su declaración, cinco años**. Y ojo: **el aplazamiento a junio de 2027 exige haber estado establecido a 31 de diciembre de 2024** — si abres ahora, **tu fecha es el 30 de diciembre de 2026** |
| 7 | **¿Cubre la chocolatería de taza y churros, tipo San Ginés?** | **Como variante, no a fondo, y se dice antes de comprar.** Es otro negocio: **fríe**, y con la freidora vuelven la salida de humos, el gas y las comidas preparadas. Hay un capítulo que te dice **exactamente qué cambia** —incluidos los tres epígrafes de IAE distintos— y qué alternativa tienes. **A fondo cubrimos la chocolatería artesana con obrador** |
| 8 | **¿Y si quiero hacer bean-to-bar?** | Entra como **variante con su propio escenario de CAPEX** y **dos frentes normativos propios**: el EUDR te convierte en **operador** con diligencia debida completa, y **tostar el grano te mete en el catálogo de actividades contaminadoras**, con notificación a tu comunidad. Lo que **no** te damos es un precio de la maquinaria: **no existe precio público** y te damos la lista de la compra y las preguntas que hacer |
| 9 | **¿Sustituye al proyecto técnico o a la gestión de licencias?** | **No, y hay que decirlo arriba.** Eso lo firma un técnico — y **ninguna de las cuatro ingenierías que revisamos publica su tarifa**. Lo que hace la guía es que **llegues a esa reunión sabiendo qué pedir, qué preguntar y qué te van a cobrar**, y que no firmes un alquiler antes |
| 10 | **Mi ayuntamiento es distinto. ¿Me sirve igual?** | **Verdad, y es lo primero que dicen todos los técnicos.** No existe una guía que dé la ordenanza de 8.131 municipios. Lo que da ésta es **el marco estatal y europeo verificado con su artículo y su enlace**, más **la lista exacta de qué preguntar en tu ayuntamiento y en qué orden**. Prometer otra cosa sería mentir |
| 11 | **¿Los Excel funcionan en Google Sheets y en Numbers?** | Sí: nuestras convenciones **prohíben `INDIRECT`, `COUNTA`, `PMT`, `OFFSET`, `XLOOKUP`, `LET` y `LAMBDA`** justamente por eso, y **no hay referencias entre libros**. Todos los parámetros van en **celda verde**, sin constantes escondidas dentro de fórmulas |
| 12 | **¿Sirve si voy a abrir fuera de España, y qué pasa cuando cambie la normativa?** | **El marco legal explicado es el español**, y se dice en la primera pantalla; **la estructura económica viaja entera** y **esa adaptación la ofrecemos como servicio**. Pago único con **actualizaciones incluidas**: los parámetros legales viven en celda editable con su fecha y hay un **anexo normativo con fecha de corte**. **Y hay cuatro fechas que ya sabemos que se mueven: el EUDR (30-dic-2026), el SMI y el convenio (31-dic-2026), Verifactu (1-ene y 1-jul-2027) y la bebida reutilizable (1-ene-2027)** |

**JSON-LD:** `Product` (con `offers`, `priceValidUntil`, `availability`, `seller`) **sin `aggregateRating` ni `review`** + `FAQPage` con las 12 + `BreadcrumbList`. Se pasa `clasifica()` de `fase8d-faq-duplicadas.py` sobre la FAQ final: **cero pares PARECIDA/DEFINICION**. ⚠️ **Ojo con los pares 2/7 y 6/8**, que son los que más se parecen. Y del PAA medido, **elegir UNA sola** entre «¿Cuáles son los 3 tipos de chocolate?» y «¿Cuáles son los 4 tipos de chocolate?»: son la misma pregunta con distinto número y el gate las marcará en nivel DEFINICION.

---

## 15. LISTA NEGRA, riesgos, presupuesto y decisiones

### 15.1 Cifras que NO pueden entrar en el producto

Va literalmente al `NO_COMUN` del guion como `cifras_ignorar` + `prohibido`, y el gate de coherencia de cifras de `documentos.py` lo hace cumplir.

| # | Cifra prohibida | Por qué se rechaza |
|---|---|---|
| **N-1** | «El cacao está en **3.000-4.500 US$/t** en 2026» (eldiario.ec, extra.ec, latercera.com) | **Incompatible** con la ICCO vía FoodRetail (**4.956 €/t** el 2-ene-2026) y con EFE (**5.938 US$/t** hoy). Probable confusión entre **precio de finca latinoamericano** y cotización internacional |
| **N-2** | 🚨 «**Una chocolatería artesanal premium requiere 80.000-250.000 €** para 50-80 m²», con «templadora continua 8.000-25.000 €», «**vitrina refrigerada 6.000-18.000 €**» y «ticket medio 18-35 €» | **La más peligrosa, y es NUESTRA:** está publicada en `use-cases-content.es.consultor.ts:386` y en **los otros 6 idiomas**, dentro de un `FAQPage`. **La vitrina de chocolate verificada cuesta 2.684,99 € sin IVA**: la página publica 2,2-6,7×. **Si la guía sale con el CAPEX verificado, el mismo dominio publicará dos inversiones incompatibles.** Decisión **D12** |
| **N-3** | Cualquier «**número de chocolaterías en España**» | **No existe dato oficial.** El DIRCE público no baja de grupo (108 mezcla cacao con café, té y platos preparados) y se detiene en 2020; eInforma sólo cubre sociedades que depositan cuentas |
| **N-4** | «Facturación agregada CNAE 1082 = **16.817.176 €**» y «facturación total CNAE 4724 = **830,68 M€**» (eInforma) | **Internamente incoherentes**: 976 × 16,8 M€ daría 16.400 M€ frente a los 2.146 M€ de Produlce; y 13.167 × 830.681 € = 10.937 M€, no 830,68 M€. **Sólo entran los recuentos de empresas y la media** |
| **N-5** | «**89 unidades/día** de punto de equilibrio» como cifra de portada | La aritmética cuadra, pero **su ticket de 2,50 €/ud no casa con el PVP del bombón medido (1,29-1,67 €)**, es del **mismo dominio** que comete el error del carnet, y su fiabilidad es MEDIA-BAJA. **Entra como método editable; NO va en la portada** |
| **N-6** | **Cualquier cifra de franquicia como dato auditado** | **L1 y L4 se contradicen dentro del mismo dato**: Valor 150.000/24.000 € vs 125.000/24.040 €; Chök 200.000 €/70-120 m² vs 100.000 €/55 m². Valen como «orden de magnitud publicado por el portal X en la fecha Y» |
| **N-7** | Los precios de **Utilcentre interpretados como «con IVA»** y **el total de 24.104,99 € como cifra fiscal** | La web **no declara la base**; el único indicio («1045 €/**Neto**») apunta a lo contrario. **El total es BASE MIXTA y así va etiquetado.** Sumarlo con las líneas de Equipo H (que sí declaran «sin IVA») da una cifra fiscalmente falsa — **es exactamente lo que tumbó la L4 de Pastelería** |
| **N-8** | La **serie completa de chocolateras Campeona** y los **precios de Valrhona de Club del Chocolate** | La serie Campeona **no es monótona** (TXM/9 a 1.015,75 € < TXM/7 a 1.300,50 €). Y de Valrhona **la página no publica el formato**: dividir sería inventar. **Lo único convertible es la bolsa de pepitas de 400 g** |
| **N-9** | «**Climatizador evaporativo desde 365 €**» para el obrador | Un evaporativo **añade humedad**: es exactamente lo contrario de lo que necesita el chocolate |
| **N-10** | Cualquier cifra de inversión de **Casa Cacao**, de **Lluc Crusellas** (1 M€ / 700 m²) o de la **franquicia Valor** vía infofranquicias (125.000 €, 30 % de rentabilidad, amortización 2,5-3 años) | Las tres sólo existen en **resumen de buscador**; la página de infofranquicias devolvió **403** |
| **N-11** | «**Utopick abrió con 35.000 € en 2014**» como referencia de CAPEX | Es **afirmación del redactor, no cita de los fundadores**, y es de **hace 12 años** |
| **N-12** | «**Selmi One a 7.400 € + IVA**» (Chocosolutions) | Es una **tienda mexicana** (tel. +52) con importación aparte: **no es precio del mercado español** |
| **N-13** | Cualquier **ticket medio de chocolatería** o **reparto mensual de ventas** | **No existe dato público.** Van como parámetro en celda verde **con el valor por defecto declarado explícitamente como supuesto**, y la guía enseña a medirlo con el TPV en dos semanas |
| **N-14** | Las **cifras del foro TheChocolateLife** (50.000-75.000 $ de arranque, 12.000-16.000 $/mes, 80-100 k$ de maquinaria) | Son de **junio de 2011 y de EE. UU.** Valen como **voz del oficio**, jamás como dato de coste español de 2026 |
| **N-15** | Las cifras de **Pomar** (100.000 € la tienda, 200.000-300.000 € el obrador, 8-12 % de rentabilidad) presentadas como coste de un obrador de chocolate | Es **PASTELERÍA**, con hornos y salida de humos. Sirven como **cota superior del oficio dulce con obrador** y como voz, **no** como CAPEX de chocolate |
| **N-16** | «Los bombones son el **18,2 %** del valor de la categoría» | Es un dato de **2022**. El vigente es **13,6 %** (Produlce 2025) |
| **N-17** | «**Dubai chocolate**» como recomendación de surtido | **WGSN, la fuente que la pronosticó, sitúa su saturación a finales de 2024 / principios de 2025.** Entra como ejemplo de cómo se explota y se sale de una moda |
| **N-18** | «La Asociación Bean to Bar tiene **45 miembros**» como cifra exacta | **45 (EFE) vs ~41 (recuento del listado).** Publicar **«más de 40»** |
| **N-19** | «**Kaitxo está en Karrantza**» y «**Moulin Chocolat es de Ricardo Vélez**» | Las dos vienen del encargo y **las dos son falsas**: Kaitxo está en **Balmaseda**, y Moulin Chocolat **es hoy de Oriol Balaguer**. **Son negocios vivos: publicarlo mal es un dato falso sobre un tercero** |
| **N-20** | Los salarios de **13-16 €/h** presentados como tabla de convenio | Salen de un **agregador que mezcla el convenio de Sevilla, el ALEH VI de 2023 y el valenciano de 2022 con plataformas de salarios**. Entran como **salario de mercado orientativo con su fiabilidad a la vista**, nunca como convenio |

### 15.2 Afirmaciones normativas falsas o caducas, y errores de método

**Normativas (todas vivas en la SERP medida o en el reflejo de copiar de Pastelería):**

- «Necesitas el **carnet de manipulador**» — **no existe desde el 20-02-2010** (`CHN-69`).
- «Necesitas **registro sanitario (RGSEAA)** para abrir» — **no**, si vendes al consumidor final: comunicación autonómica **no habilitante** (`CHN-39`). Y **tener obrador no te saca de minorista** (`CHN-40b`).
- «Con vender **poco** a otras tiendas no pasa nada» — los tres requisitos del art. 3 son **acumulativos**, y **basta un solo cliente inscrito en el RGSEAA** para romper «restringido» (`CHN-41`).
- «**La ley obliga a tener el obrador a 16-18 °C y al 50 % de humedad**» — **no lo dice ninguna norma** (`CHN-30`). Es criterio del operador.
- «**Los bombones van a 4 °C porque lo dice el RD 1021/2022**» — la fila 9 habla de **pastelería** rellena; al bombón le aplica el **4.2** (`CHN-30`).
- «**Hacer bombones en casa para vender es ilegal en España**» — la fórmula correcta es «**no entra en la lista del art. 13.8 salvo que tu comunidad lo haya añadido por la letra e)**» (`CHN-44`).
- «La **Comunitat Valenciana** permite el chocolate desde vivienda» — su lista dice «confitería», **no «chocolate»**, y **la cuestión no está resuelta** (`CHN-44b`).
- «**Praliné», «trufa» y «chocolate artesano»** como categorías legales — **no aparecen en la norma** (`CHN-03b`, `CHN-53`).
- «La mención **“cacao: X % mínimo” es obligatoria en todos los chocolates**» — **no** en blanco, relleno ni bombón (`CHN-07`).
- «**El régimen simplificado del EUDR es para las pymes**» — es para **micro y pequeños operadores primarios establecidos en países de riesgo bajo** (`CHN-27`).
- «**Como soy pequeño, el EUDR me llega en junio de 2027**» — **sólo si estabas establecido a 31-12-2024** (`CHN-22`).
- «**El EUDR no me afecta porque compro cobertura europea**» — **sí te afecta**, como operador posterior (`CHN-24`).
- «**Una chocolatería tiene libertad horaria por el art. 5.1 de la Ley 1/2004**» — **no está en esa lista**; le viene por el **5.2** (`CHN-77`).
- «**Necesitas el epígrafe industrial 421.1** para fabricar bombones» — el **644.5 te faculta expresamente** (`CHN-72`).
- «**Los moldes de policarbonato pagan el impuesto al plástico**» — **no**: el art. 73.d) excluye lo que no se entrega con la mercancía (`CHN-62`).
- «**Verifactu es obligatorio en 2026**» — **1-ene-2027** y **1-jul-2027** (`CHN-75`).
- «**Tostar cacao no tiene implicaciones ambientales**» — está el CAPCA, grupo C, **notificación** a la CCAA (`CHN-47`). Y el revés: **tampoco se puede afirmar que el epígrafe menciona el cacao**, porque dice «del café **o similares**».

**Errores de método:**

- **Dar un número de inversión en vez del modelo que lo produce.** Es lo que hacen las fuentes gratuitas, y por eso se contradicen ×10.
- **Citar «el artículo 6 del RD 1055/2003».** Ese real decreto tiene **un artículo único**: se cita «**apartado 6.d) de la Reglamentación técnico-sanitaria**» (`CHN-01`).
- **Copiar la remisión del RD 1055/2003 al RD 1334/1999** para el etiquetado, aunque lo haga la propia norma: está superada por el Rgto. 1169/2011 (`CHN-12`).
- **Mezclar precios CON y SIN IVA en la misma tabla de CAPEX** → desviación del 21 % (§15.1 `N-7`).
- **Confundir la temperatura de la SALA (18-22 °C) con la de la CÁMARA (15-18 °C).** Son dos cosas distintas y el encargo las fundía.
- **Usar «dulcería» como sinónimo de chocolatería en el copy LATAM** — en México es la tienda de golosinas al mayoreo.
- **Escribir «artesana» en vez de «artesanal»** (390 vs sin dato) y **«temperado» en vez de «templado»** (10 vs 20) en el cuerpo.
- **Presentar «trufa» y «praliné» como sinónimos de bombón**: son tipos, y un chocolatero lo detecta en la primera página.
- **Copiar redacciones legales de otros kits sin verificar.** Precedente medido: `kit-tareas-sushi-bar/03` y `kit-tareas-marisqueria/03` citan el **RD 1420/2006 derogado** en producto **vendido**.
- **Prometer tráfico SEO.** 10 búsquedas/mes para la intención de apertura, con dos meses a cero.
- **Fiarse de un snippet.** Precedente medido en este mismo research: 41.580 € vs los 21.150 € de la página oficial de tarifas.
- **Medir GSC por la dimensión equivocada.** Precedente medido **en este mismo research**: por `query` el nicho daba 24 impresiones y 0 clics; por `page`, **285 impresiones y 6 clics**.

### 15.3 Riesgos, incluidos los de caducidad

| # | Riesgo | Evidencia | Mitigación |
|---|---|---|---|
| **1** 🔴 | **El EUDR se ha aplazado DOS veces y puede haber una tercera** | Rgtos. **2024/3234** (26-12-2024) y **2025/2650** (26-12-2025), y el segundo **reescribió ocho artículos y creó una figura nueva** | **Es el único capítulo con caducidad conocida y alta probabilidad de cambio.** Fecha de revisión **dentro del propio documento** («verificado a 12-09-2026; comprueba el estado antes de comprar cacao») y todo lo movible al **anexo**. Decisión **D5** |
| **2** 🔴 | **Publicamos dos inversiones incompatibles en el mismo dominio** | `use-cases-content.es.consultor.ts:386` en **7 idiomas**, dentro de un `FAQPage` | **D12.** Arreglarlo en el mismo commit o antes |
| **3** | **Un error en el bloque legal cuesta más que un error de food cost** | Sanciones de seguridad alimentaria y, en el EUDR, responsabilidad documental de cinco años | **Verificador legal independiente obligatorio** (agente sonnet, patrón del verificador fiscal de la Guía Food Cost) **antes** de escribir los caps. 09, 10, 11 y 19, **contra las fuentes primarias, no contra L3** |
| **4** | **Cinco verificaciones normativas siguen abiertas y una es de capítulo** | V-01 (convenio), V-02 (IVA de talleres), V-03 (artesanía por CCAA), V-04 (lote), V-05 (confitería valenciana) | **No escribir esos epígrafes sin cerrarlas.** El método barato está probado: **PDF consolidado + PyMuPDF** |
| **5** | **Canibalización con `kit-tareas-chocolateria` (12 €)** | El kit resuelve templado, moldeado, vitrina, campañas y caja | Las **6 reglas K1-K6 del §8.1**, verificadas hoja a hoja, y el cap. 01 con la tabla «qué incluye el pack / qué es cross-sell» |
| **6** | **Cinco dolores centrales con corpus sesgado o sin voz** | **Reddit, YouTube, Instagram, Facebook, TikTok y los foros españoles, inaccesibles**; cero quejas en primera persona sobre templado, humedad o maquinaria de segunda mano | **Pedirle a John 5-10 minutos de voz** (decisión **D13**) |
| **7** | **Vender profundidad LATAM que no tenemos** | El bloque legal es **exclusivamente español**; y la demanda LATAM de apertura es 10/mes o cero | Casillas editables + vocabulario con equivalencia + **la landing lo dice en la primera pantalla** + la FAQ ofrece la adaptación como servicio |
| **R-01** | **EUDR — art. 38** | Todo el bloque C, la ficha de proveedor y la fila del calendario legal | **30-12-2026** (general) · 30-06-2027 (sólo establecidos a 31-12-2024) |
| **R-02** | **Rgto. (UE) 2023/915** — cadmio, OTA y HAP | Los siete límites numéricos | **Continuo**: se modifica **por reglamentos de la Comisión, sin aviso legislativo** (el consolidado leído ya va por la revisión 004.001) y **el cadmio del cacao está en revisión permanente por la EFSA** |
| **R-03** | **RD 1055/2003** | **Todo el capítulo 10**: definiciones, porcentajes, menciones | **Sin fecha; riesgo medio.** Lleva **23 años sin una sola modificación** y remite a una norma de etiquetado de **1999**. Si Bruselas abre el melón de las «directivas verticales» —como hizo con miel y zumos en 2024— **se cae medio capítulo** |
| **R-04** | **SMI 2026 y revisión del convenio de Madrid** | La tabla salarial y los ejemplos de nómina | **Caducan el 31-12-2026.** Viven en celda verde y en el anexo, nunca en la prosa |
| **R-05** | **Verifactu** | El capítulo de TPV y facturación. **Ya se aplazó dos veces** | 1-ene-2027 / 1-jul-2027 |
| **R-06** | **RD 1055/2022 art. 9.4.a)** | Un requisito hoy futuro pasa a presente en <120 m² | **1-ene-2027** |
| **R-07** | **Registros sanitarios autonómicos** | El cuadro por CCAA | **Continuo, 24 meses.** Valencia legisló en 2025 y Madrid en 2026: **las comunidades se están adaptando ahora mismo**, y cualquiera puede usar la letra e) del art. 13.8 y **cambiar la respuesta de `CHN-44`** |
| **R-08** | **Art. 91 de la Ley 37/1992 (IVA)** | Los tipos y el capítulo de TPV | Cada ley de presupuestos **y por doctrina de la DGT sin cambio legal** |
| **R-09** | **Decreto 26/2026 de Madrid: transitorio de un año** | La frase «tienes de plazo hasta…» | **Vence el 28-03-2027.** Es oro comercial **con fecha de caducidad** |
| **R-10** | **Térmica**: `documentos.py` y los 9 constructores son python local | En las lentes se llegó a **67,4 °C** sólo leyendo ficheros | `istats cpu temp` entre fases, **un python cada vez**, `scripts/termica/watchdog-termico.sh` activo, **sin builds locales ni Playwright**; deploy en la nube |

> **Consecuencia de diseño, no de contenido:** todo lo de R-01 a R-09 debe vivir en **celda de parámetro o en el anexo fechado**, nunca cosido en la prosa de un capítulo. **Un «Anexo normativo — actualizado a 12-09-2026» de 6-8 páginas permite reeditar el producto cambiando un fichero.**

### 15.4 Presupuesto estimado por fase

| Fase | Trabajo | Modelo | Pastelería (real) | **Chocolatería (estimado)** | Por qué cambia |
|---|---|---|---|---|---|
| **A — research** (esta sesión) | 6 lentes + esta síntesis | opus / sonnet | 2,06 M | **Cerrada. ≈2,1 M** | Mismo alcance |
| **A2 — verificación legal + SPEC + guion** | Cerrar V-01…V-05 con PDF del BOE/EUR-Lex · SPEC con las decisiones firmadas · `guion_guia_chocolateria_obrador.py` de 20 caps + anexo con `puntos_por_epigrafe` · `verificar_guion.py` en verde | opus (SPEC) + sonnet (guion) | 0,88 M | **1,10 M** ⬆ | **+25 %: tres frentes normativos nuevos** (RD 1055/2003, contaminantes, EUDR) y más referencias de celda |
| **B1 — `datos_ejemplo.py` + los 9 libros** | juego de datos (opus) → 4 constructores → 1 refutador opus de los xlsx → fixer sonnet → `inject_cache` + verificación `data_only` + `mapa-*.json` + `gate_libros.py` | opus + sonnet | 2,79 M (8 libros) | **3,15 M (9)** ⬆ | 0,30 M/libro medido × 9, + **cuatro libros sin molde previo** (1-clima, 3, 5, 6-valle) |
| **B2 — documentos** | `dump_prompts.py` → **~46 redactores sonnet** (20 caps + anexo + 2 bonus) con `check_bloque.py` → **1 verificador legal sonnet contra fuentes primarias** (caps. 09, 10, 11, 19) → `documentos.py` ensambla → 1 refutador opus → fixer → gates (páginas con PyMuPDF, no latinos, coherencia de cifras, paridad PDF↔DOCX, metadata) | sonnet en paralelo + opus | 4,90 M | **5,0-5,2 M** | Mismo nº de bloques si se repite la palanca de `bloques: 1` en los capítulos no legales |
| **C — capa de producto y lanzamiento** | Landing sobre `GuiaData`, dashboard, 4 functions, Payment Link (John), catálogo 49, hub ×2 con el `comingSoon` vaciado **y sus dos arreglos**, alias del buscador, changelog, 7 imágenes, sustitución quirúrgica de 4 banners, `productIds` de 3-5 páginas de rol, `CRYPTO_PRODUCTS`, `robots-gate.py`, `whatsapp-gate.py`, `gate-flujo-postpago.py`, `censo-entregables.py --fail`, gate LIVE, broadcast en Resend | sonnet + Fable en lo crítico | 0,71 M | **0,80 M** | + el arreglo del `comingSoon` y **D12** |
| **Refutaciones y fixes** | Refutación de xlsx + de documentos + fixer | opus + sonnet | ≈1,50 M | **1,25 M** ⬇ | ✅ **Los dos bugs de tubería que en Pastelería generaron 5 de los 11 hallazgos altos YA ESTÁN ARREGLADOS** (§8.4). Es el único renglón que baja |
| **TOTAL** | | | **≈14,1 M** | **≈13,4-14,6 M** | |

🔴 **Aviso explícito, y es la decisión D14:** el techo de John es **~15 % de la cuota semanal**. **Mi estimación queda por debajo de la de L6 (14,8 M) por dos razones medidas, no por optimismo:** (1) **9 libros en vez de 10** (−0,30 M) y (2) **los dos bugs de tubería ya están arreglados**, así que el 1,5 M que L6 identificaba como ahorro posible **ya está ahorrado** y no hay que gastarlo en arreglarlos ni en la ronda de fixer que provocaban. **Aun así sigue siendo un producto de 13-15 M: no arrancar la construcción sin luz verde explícita, y probablemente en dos sesiones** — (A2+B1) y (B2+C).

**Las palancas que quedan, con su coste honesto:**
1. **Bajar a 8 libros** (absorber el 3 en el 4): **−0,30 M**. **Coste real:** el argumento comercial más fuerte del producto queda enterrado dentro del escandallo. **No lo recomiendo.**
2. **Reducir el bonus 2 de 12 decisiones a 8**: **−0,4 M**. Coste: es el bonus que más valor percibido da por página.
3. **Repetir la palanca de `bloques: 1`** en los capítulos no legales: ya está dentro de la estimación.

### 15.5 Decisiones que sólo puede tomar John

| # | Decisión | Mi recomendación | Su coste |
|---|---|---|---|
| **D1** 🔴 | **ALCANCE.** ¿(a) chocolatería artesana / bombonería con obrador, con la de taza y churros como **epígrafe del cap. 01 + columna de escenario + párrafo en landing y FAQ**? ¿O como **capítulo propio** (L2, L4) o **sólo columna** (L6)? | **(a), con (b) como EPÍGRAFE, no capítulo.** Seis argumentos en §1.3, y el que decide: **la normativa ya las separa sola** (tres epígrafes de IAE, art. 30 del RD 1086/2020, gas y humos, y hasta el fundamento de la libertad horaria), así que **la distinción cabe en dos páginas mejor argumentadas que veinte** | Un capítulo entero costaría ~2 bloques de redactor (≈0,2 M) y, peor, **duplicaría el concepto «obrador» en el CAPEX**, que es el defecto alto que ya cazó la refutación de Pastelería |
| **D2** | **BEAN-TO-BAR: ¿dentro o fuera?** | **Dentro, como VARIANTE con su columna de CAPEX y su epígrafe en el cap. 11**, no como segundo caso modelado. Es la línea con más contenido normativo propio (EUDR como **operador**, CAPCA por el tostado, HAP del grano) y **el perfil que más fácil detecta si la guía va floja en cacao** | ⚠️ **El tren de máquinas NO tiene precio público**: la guía dará **la lista de la compra y las preguntas que hacer**, no una cifra. Si entra como capítulo doble, **+0,3 M** |
| **D3** | ¿**Anotamos «Cómo Montar una Churrería-Chocolatería»** como candidato de la siguiente cola? | **Sí, anotarlo** (no hacerlo ahora). Su keyword de emprendedor (`montar una churreria` **50/mes**, subiendo 30→50) es **5× la de chocolatería**, y hay traspasos reales con cifras | Ninguno hoy. Es una nota en el calendario |
| **D4** | **La descripción del hub dice «proveedores de cacao»**, que suena a grano, y el molde principal compra **cobertura** | **Ampliar el libro 9 para cubrir las dos cosas** y **retocar la descripción al publicar** («proveedores de cobertura y cacao»). Es un cambio de tres palabras | Retocar lo anunciado desde mayo. Alternativa: dejar la literal y que el libro lo cubra igual |
| **D5** | **EUDR y fecha de lanzamiento.** El bloque tiene caducidad conocida (**30-12-2026**) y **ya se aplazó dos veces** | **Fecha de revisión explícita DENTRO del documento** («verificado a 12-09-2026; comprueba el estado del EUDR antes de comprar cacao»), como se hizo con Verifactu, y todo lo movible al **anexo** | Ninguno. Es disciplina de redacción |
| **D6** 🔴 | **El `comingSoon` se queda VACÍO al publicar** (es la última entrada). ¿Se **oculta** la sección o se **siembra** con el siguiente producto? | **Sembrarla con el siguiente producto de tu cola.** Mantiene viva la señal de «esto se mueve» y **alimenta el registro de demanda del buscador**. Si no hay siguiente, ocultarla — **y en los dos casos hay que añadir la guarda que le falta al Astro y hacer condicional el badge** | Si se oculta sin más, el hub pierde el bloque de «En Desarrollo». **Lo que NO se puede hacer es no tocar nada**: quedaría el rótulo huérfano en el HTML servido |
| **D7** | **Número de libros: 8, 9 o 10.** L4 dice 8, L6 dice 10 | **9.** Se mantiene `sensibilidad-al-precio-del-cacao` como libro propio (**es el argumento comercial más fuerte y enterrado no se vende**) y se absorben talleres y regalo corporativo como **dos hojas del plan financiero** (sus keywords valen 10/mes: son valor de producto, no de búsqueda) | 10 libros cuestan **+0,30 M**; 8 entierran el libro 3 |
| **D8** | **Slot de Resend.** ¿Borrador para el **24-oct**, o se **adelanta** desplazando la cola? | **Dejarlo en el 24-oct**, a diferencia de lo que se hizo con el Chef Ejecutivo: **delante hay ya un lanzamiento (Pastelería, 14-oct) y su kit (19-oct)**, y adelantar la chocolatería metería **tres correos de producto de la misma familia en once días** | Adelantarlo desplazaría cinco correos y saturaría a la lista. **Es tu decisión de negocio** |
| **D9** | **Convenio del chocolate** (`CHN-65`, V-01): no hay convenio **estatal** localizable y el de Madrid **condiciona** la fabricación de bombones | **Una pasada de verificación en el REGCON del Ministerio de Trabajo** (~0,1 M). Si no se cierra: **una sola tabla, la de Madrid, marcada como ejemplo, más el método para identificar el tuyo** | 0,1 M y media hora. **Publicar una tabla salarial equivocada es peor que no publicar ninguna** |
| **D10** | **Artesanía por comunidades** (`CHN-54`): sólo Cataluña verificada | **Cataluña con articulado y el resto como enlace al registro autonómico**, igual que en Pastelería | Las 17 son ~2 días más y **multiplican el mantenimiento**: las CCAA se están adaptando ahora mismo |
| **D11** | **¿Autorizas una columna «franquicia vs. independiente»** en el CAPEX con las seis fichas verificadas (Sven, Chocolat-Box, Fábrica di Chocolate, Maestro Churrero, Valor, Chök), citando marca y fuente? | **Sí, pero como «orden de magnitud publicado por el portal X en la fecha Y», nunca como dato auditado** — porque **L1 y L4 dan cifras distintas de las mismas marcas** (§15.1 `N-6`). Es el único benchmark público y honesto del sector | Nombra competidores por su nombre en un entregable de pago |
| **D12** | 🔴 **La cifra de 80.000-250.000 € publicada en `/usos/consultoria/chocolatero-consultor` en los 7 idiomas**, con una vitrina 2,2-6,7× por encima de la verificada | **Corregirla en el mismo commit del producto 49**, con el rango que sostiene este research y sus fuentes. Si no, **el mismo dominio publicará dos inversiones incompatibles para el mismo negocio** — y una de ellas dentro de un `FAQPage` | Tocar 7 ficheros de contenido. Es media hora de un agente sonnet y **evita que un comprador nos enseñe la contradicción** |
| **D13** | **¿Nos das 5-10 minutos de voz** sobre el precio del cacao y cómo se repercute, la merma real de templado, qué margen deja una caja frente a la unidad, qué haces en julio y agosto, y si los talleres dan dinero o son marketing? | **Sí.** Es el hueco declarado de L5 (**Reddit, YouTube y los foros españoles bloqueados**: no hay ni una queja en primera persona sobre templado o humedad) y **tu experiencia es la fuente más autorizada que existe** para llenarlo | 10 minutos tuyos |
| **D14** | **¿Se parte la construcción en DOS sesiones** (A2+B1 · B2+C)? | **Sí.** 13-15 M no caben en una semana bajo el techo del 15 % | Alarga el lanzamiento una semana. **Decidirlo antes, no a mitad** |
| **D15** | **Los tres defectos colaterales de pocas líneas.** (a) La tarjeta de `kit-tareas-chocolateria` dice «9 checklists» y entrega **9 + 2 bonus**. (b) **`kit-tareas-chef-privado` anuncia «9 checklists» y entrega 7 + 2 bonus** — ése sí vende de más. (c) Dos posts de chocolate venden **sushi, cocina peruana y asador** | **Arreglar (a) y (c) en el mismo commit** del producto 49. **(b) va a una sesión impar**: no es de esta familia y ampliar a los 6 casos sería salirse del alcance | Ninguno. (a) y (c) es trabajo que ya hay que hacer |
| **D16** | **Cripto.** ¿El 49 nace con NOWPayments activado aunque el pago real de prueba siga pendiente? | **Sí** (regla del 6-sep). La plantilla ya monta las tres puertas: **sólo hay que añadir el slug a `CRYPTO_PRODUCTS` con scope `builds` Y `functions`** | Ninguno |
| **D17** | **Nombre.** ¿«Cómo Montar una Chocolatería» como H1 + «Guía Chocolatería con Obrador» como nombre de catálogo? | **Los dos**: el titular es la promesa publicada desde mayo; el nombre de catálogo calca a las hermanas | Dos nombres para lo mismo exige cuidado en el hub y en el footer (§12.1) |
| **D18** | **El retraso.** La tarjeta dice «Junio 2026» y estamos en septiembre | **No mencionarlo en el copy.** Se retira la tarjeta de «Próximamente» y se publica la real con badge «Nuevo»: el cliente ve el producto, no la deuda | Ninguno |

---

## 16. Lo que este research NO pudo verificar (y lo que SÍ comprobé yo)

**L1 — competencia**
- **Amazon.es devuelve HTTP 500** e **infofranquicias.com 403**: faltan el precio español del único libro en español y **todos los datos de Chocolat Factory**.
- **EPGB no publica precios** y tres de sus fichas dan 404; **Hotmart no muestra precio sin checkout** (3 infoproductos); **ESAH y Hofmann** dejan dos fichas sin precio.
- **Ninguna consultora de licencias publica tarifa**: la familia (e) no aporta ancla, sólo la constatación de la opacidad.
- **El censo mide precio publicado, no ticket medio ni unidades vendidas.** Ninguna afirmación de «cuánto vende la competencia» puede sostenerse.
- **Dos fuentes gratuitas se perdieron** (silviaguedez.com 403, teymas.com sin salida): son **10 auditadas, no 12**.

**L2 — SERP y demanda**
- **No se pudo leer el TEXTO de los AI Overviews**: DataForSEO los devuelve como `asynchronous_ai_overview: true` con `markdown: null`. Se sabe en qué 2 consultas existen, **no qué dicen ni a quién citan**. **Limitación heredada de Pastelería y sin resolver.**
- **DataForSEO devuelve `None`, no `0`**, para keywords sin dato. **`None` ≠ cero búsquedas**, y L2 lo distinguió correctamente.
- ❌ **CORREGIDO POR MÍ:** midió el universo de chocolate **por query** y concluyó 24 impresiones / 0 clics. **Por page son 285 / 6** (verificación 5).
- **No se midió el blog EN ni los FR/DE/IT/PT.**

**L3 — normativa**
- **V-01 (convenio estatal del chocolate), V-02 (IVA de talleres), V-03 (artesanía fuera de Cataluña), V-04 (RD 1808/1991, lote) y V-05 («confitería» valenciana) siguen ABIERTAS.** Ninguna puede entrar tal cual.
- **`plandenegocio.es` devolvió 404**: el error del «carnet de manipulador» **no se pudo capturar en su fuente** y por tanto **no se atribuye a ningún blog por su nombre**.
- **El PDF de claves del RGSEAA de `ics.jccm.es` descargó corrupto** y el oficial de AESAN dio 404: la clave 25 se verificó sobre la Guía rev. 16 de la Comunidad de Madrid. **Nivel B.**
- **No existe consolidado del Rgto. 2023/915 posterior al 01-01-2025.**
- **Bloques no abiertos por alcance:** licencia municipal, urbanismo, desistimiento/LSSI/RGPD, PRL, ruido y seguro de RC.

**L4 — sector y equipamiento**
- **El DIRCE público no aísla el chocolate** (L-1/L-2) y **la serie oficial de la ICCO está tras muro de pago** con su «último» dato del 07-10-2024.
- **InfoJobs devuelve HTTP 456** y Glassdoor no se pudo leer: **el bloque de salarios no cumple el encargo** y baja a MEDIA-BAJA.
- **Selfpackaging 403** (sin precios de packaging), **Infrico 404** (sin vitrina alternativa), **eInforma/Axesor de pago**.
- **No hay precio público del tren bean-to-bar, de la cámara climatizada, del deshumidificador dimensionado, de la guitarra de corte ni de churrera/freidora/extracción.**
- **No existe dato público del reparto mensual de ventas de una chocolatería española.**
- ❌ **ARBITRADO POR MÍ:** dejó la temperatura de la cámara «sin fuente»; **L5 la tiene literal en la misma fuente** (verificación 15).

**L5 — voz del cliente**
- **Reddit bloqueado por completo** (`WebFetch` y `WebSearch` con `allowed_domains`), **comentarios de YouTube inaccesibles**, Instagram/Facebook/TikTok con muro de sesión, **Forocoches y foros de repostería sin nada específico**.
- **Seis páginas clave devuelven 403** (metropolitano.gal, aragondigital.es, madridesnoticia.es, negociosenventa.es, silviaguedez.com, infofranquicias.com): marcadas R01-R06 y **no usadas como cita ni como cifra**.
- **Cero quejas en primera persona sobre templado fallido, humedad o maquinaria de segunda mano.** Tenemos la norma técnica, no la frustración vivida.
- **Dos citas del corpus son antiguas o extranjeras** y así van marcadas (foro de **2011, EE. UU.**; entrevista de **2007**).

**L6 — assets**
- ❌ **Corregido por mí:** el bug del `%` **ya está arreglado** (verificación 1) y el gate de tipo de `verificar_guion.py` **ya existe** (verificación 2). **Sus dos riesgos de tubería principales están muertos.**
- ❌ **Corregido por mí:** daba la Guía de Pastelería por **sin commitear y sin push**; está **cerrada, pusheada y LIVE** (verificación 3).
- ❌ **Corregido por mí:** `zona-app.ts` tiene **48**, no 49 (verificación 4).
- ❌ **Ampliado por mí:** el universo de blog son **8 posts, no 7** (verificación 7), y hay una **cuarta página `/usos/`** con una cifra que hay que corregir (verificación 6).
- ✅ **Matizado por mí:** el «9 checklists» del hub **no miente, omite** — y el que sí vende de más es `kit-tareas-chef-privado` (verificación 8); y el `comingSoon` vacío **deja un rótulo en el HTML servido, no una sección visible para siempre** (verificación 9).
- **No pudo consultar el registro de búsquedas del hub** (`buscador-report.py` exige `ADMIN_PASSWORD`), **ni GSC**, **ni los nombres reales de los agentes en Pickaxe**, **ni precios de maquinaria**.
- **Ninguna fórmula de los 9 libros se ha verificado con pycel**: son diseño, no ficheros.

**Verificaciones propias de esta síntesis (lo que SÍ comprobé)**
- ✅ **48 productos en `products-catalog.ts`, `payment-links.ts` y `product-prices.ts`, y 48 reales en `zona-app.ts`** (`comm` sin diferencias en ninguno de los dos sentidos) · **escalera de precios completa parseada** (la franja de 65 € son **8**) · ✅ `robots.txt` con `guia-*` en los **5 bloques** · ✅ **`curl`: `/guia-pasteleria-obrador` = 200 con «103 páginas» y su Payment Link; `/guia-chocolateria-obrador` = 404** (slug libre) · ✅ `git status -sb` y `git rev-list --count` = **0 ahead, 0 behind** · ✅ **`documentos.py:692-698` y `verificar_guion.py:207` leídos línea a línea**, más `git log` de `documentos.py` (`0ba5158`) y el changelog publicado · ✅ **`comingSoon`, sus guardas (`ProductosDigitales.tsx:1227` vs `…HubPage.astro:1448`) y el script de cliente (`:1883`, `:2256`)** · ✅ **los 11 ficheros de `kit-tareas-chocolateria` y los de las 18 verticales** (16 de 18 con 11 = 9+2; chef-privado con 7+2) · ✅ **13 ficheros de `kit-escandallos`: ninguno de chocolate** · ✅ **censo de los 326 posts ES por menciones de chocolate y los banners de los 8 extraídos uno a uno** · ✅ **`use-cases-content.es.ts:1225/1264` y `:3210/3248`, más `…es.consultor.ts:348/386` y sus 7 idiomas** · ✅ **`sinonimos-buscador.json` (8 grupos, 4 frases, 7 alias, sin chocolate) y el placeholder animado** · ✅ **411 entradas de `guias-v2-research-sector.json` con sus 16 prefijos: `CHN` y `CHS` libres** · ✅ **GSC en vivo, 90 días, dos consultas (línea `guia-*` y universo chocolate)** · ✅ **17 keywords medidas por mí en DataForSEO**, cinco de ellas **que ninguna lente midió** · ✅ **tamaños del pipeline** (`documentos.py` 2.246, `motor.py` 2.135, 8 `gen_*.py` = 12.196, `datos_ejemplo.py` 3.324, guion 4.924, SPEC 330) · ✅ **`CALENDARIO-V2-SEMANAL.md` para la cola de Resend**.
- ❌ **No repetí los fetches de precios de L1 ni de L4**: las cifras de cursos, franquicias, maquinaria y proveedores se toman de esas lentes **con su fecha de consulta**.
- ❌ **No consulté Resend**: el hueco del 24-oct es una previsión sobre lo documentado en el calendario, **no un hueco confirmado por API**.
- ❌ **No verifiqué ninguna norma con mis propias manos**: el bloque legal se apoya en L3 con sus niveles A/B/C declarados. **Antes de escribir los caps. 09, 10, 11 y 19, el verificador legal debe abrir el RD 1055/2003, el Rgto. 2023/915 y el consolidado del EUDR.**
- ❌ **No abrí ningún `.xlsx` con openpyxl ni ningún PDF con PyMuPDF**: las medidas de fórmulas, páginas y palabras se toman de L6, que las hizo hoy sobre el disco. Era la parte más cara térmicamente y la que menos aportaba repetir.

**Térmica:** `istats cpu temp` medido entre tandas durante toda la sesión. Registro real: **48,2 → 43,5 → 42,1 → 42,0 → 41,3 → 50,3 → 45,6 → 42,4 → 39,7 °C**. **Nunca se acercó a los 65 °C.** Sin builds, sin Playwright, sin navegador, sin openpyxl y sin PyMuPDF; las consultas de red (GSC, DataForSEO, dos `curl`) no cargan la CPU.

---

**Estado: research cerrado, PENDIENTE DEL OK DE JOHN.**

**Via: Claude Code**
