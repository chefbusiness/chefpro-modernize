# Handoff — 2026-08-31 · banderas en Windows + los 322 posts que no vendían

**Estado: TODO CERRADO, desplegado y verificado en producción.** No hay nada a medias.
Commits `d493383` (banderas) y `e6d73b8` (banners). Cierre documental el 2026-09-03.

---

## 1. Las banderas no se veían en Windows — 1.023 páginas

**Reporte de John:** en la landing, las banderas de los países no se muestran en Chrome sobre
Windows; en el Mac sí.

**Causa:** no es CSS ni Chrome. **Windows no tiene los glifos**: Segoe UI Emoji no incluye los
pares de indicadores regionales (U+1F1E6–U+1F1FF), así que el navegador cae al fallback y pinta
las dos letras ISO — «DE», «BE», «GB», «ES». macOS funciona porque Apple Color Emoji sí las trae.

**Alcance real, medido sobre el `dist`: 1.023 de 1.312 páginas**, no sólo los recetarios. El
selector de idioma del menú móvil (`Header.astro`) está en casi todas, y también salían mal los
avisos de conversión («Alguien de Barcelona 🇪🇸» → «…Barcelona ES») y los strips de ciudades.

**Solución** — `astro-site/src/styles/global.css` + `tailwind.config.ts` + el woff2 en
`astro-site/public/fonts/` (con su `README.md` de atribución: Twemoji es CC-BY 4.0):

- Subconjunto de Twemoji de 78 KB, **37 codepoints en total**, declarado con `unicode-range`
  acotado a las banderas → **no puede afectar a ningún otro texto** y el navegador sólo lo
  descarga si la página pinta una bandera.
- `local('Apple Color Emoji'), local('Noto Color Emoji')` **delante** del `url()`: macOS/iOS y
  Android/Linux siguen usando su emoji nativo y no descargan nada. Sólo Windows cae al woff2.
  `Segoe UI Emoji` **no se lista a propósito**: existe en Windows pero no tiene los glifos, y
  casarlo dejaría la bandera sin pintar.
- Va el primero en la pila `sans` de Tailwind, de la que hereda todo el sitio.

**Cómo se verificó** (esto es reutilizable para cualquier bug dependiente del SO): se reprodujo
el entorno de Windows en el VPS lanzando Chromium con un `FONTCONFIG_FILE` que **rechaza
NotoColorEmoji**, y se midió A/B sobre la home real —

| | ancho del glifo | colores |
|---|---|---|
| producción de entonces | 64 px (**2 glifos** = las letras) | 1 |
| con el fix | 32 px (**1 glifo** = ligadura) | 11 |

Comprobadas además las 7 banderas del cajón de idioma en móvil, el hub de ciudades y la home
inglesa. Verificado en producción: el `@font-face` está en la CSS servida y
`/fonts/TwemojiCountryFlags.woff2` responde 200 con 78.292 bytes.

**Detalle conocido y aceptado:** en páginas donde las banderas sólo viven en el cajón de idioma
cerrado, el navegador no pide el font hasta que se abre (no descarga lo que no pinta) → un
parpadeo de letras de un *round trip* con `font-display: swap`. Aceptable.

---

## 2. El blog no vendía: 39 posts de 325 tenían banners

**Cómo salió:** revisando GSC del catálogo de productos digitales, a petición de John.

**El hallazgo de fondo:** arreglar la rotación de banners el 30-ago la dejó **en el generador**.
Un arreglo en el generador **no retroactúa sobre lo ya publicado**, así que el blog vivo seguía
con el reparto viejo — 19 productos de 44 y `kit-escandallos` en el 29,9 %. Y el agujero era
mayor que el reparto: **sólo 39 de 325 posts ES tenían banners; 286 no tenían ninguno.**

**Por qué no se podía usar el ensamblador:** `fase8c-libreria-assemble.py` **reconstruye el
cuerpo entero** desde el `.txt` de bridge; pasarlo sobre un post publicado lo pisa (ya se llevó
dos enlaces internos de `cocina-molecular` el 2026-08-01).

**Lo que se hizo** — `scripts/astro-migration/fase8e-banners-corpus.py` (dry-run por defecto,
`--lang es|en`, `--informe`, `--aplicar`). **Sólo inserta, y lo demuestra**: un gate quita del
resultado exactamente las cadenas insertadas y exige que el cuerpo vuelva a ser byte a byte el
original. Reutiliza `catalogo_productos()`, `rotar_productos()` y `banner()` **importando** el
ensamblador, para no duplicar su gate de recuento.

| | antes | ahora |
|---|---|---|
| Posts ES con 3 banners | 39 / 325 | **325 / 325** |
| Posts EN | 27 / 66 | **64 / 66** |
| Productos distintos vendidos | 19 / 44 | **44 / 44** |
| `kit-escandallos` | 29,9 % | **7,1 %** |
| Enlaces internos a las landings huérfanas | 3 y 7 | **24 y 24** |

**Dos trampas que costaron una iteración cada una:**

1. **Repartir por la longitud BRUTA coloca mal los banners.** Los bloques congelados de
   WordPress son hasta el 21 % del HTML, así que el «85 %» bruto puede caer detrás de todo el
   texto real. Se reparte por longitud **útil**, descontando esos tramos.
2. **Una línea en blanco dentro de un `<div>` corta el bloque HTML de Markdown** y el resto se
   escaparía como texto plano. De ahí la guarda de **balance 0 de contenedores** en el punto de
   inserción, que es además la red contra cualquier bloque congelado que no conozcamos.

**Gates, todos verdes:** `fase8b-gate` 3.558 checks / 0 fallos · `fase8c-h1-unico` 0 ·
`fase8c-restos-wordpress` 0 · `robots-gate` verde · `fase8c-libreria-en-gate --todos` 26 posts /
0 errores · **0 `<aside>` escapados** en todo el `dist`. Spot-check en producción sobre los tres
moldes ES y un post EN: 3 banners y 0 escapados en los cinco.

---

## 3. Lo que dice GSC del catálogo (90 días, al 2026-08-30)

Base técnica **correcta**: 44/44 landings sin `noindex`, 44/44 en el sitemap de producción,
las 44 sirven 200 y el `robots-gate` está verde (no se ha repetido lo de agosto).

- **96 clics y 2.977 impresiones. CTR 3,22 %.** Cinco landings se llevan el **70 %** de las
  impresiones y el **80 %** de los clics (`kit-escandallos`, `kit-plan-financiero`, `pack-appcc`,
  `kit-tareas`, `pro-prompts-ebook`). **21 landings tienen impresiones y cero clics.**
- **⚠️ Trampa de medición:** el corte de `row_limit: 500` hacía parecer que **26** landings no
  tenían ninguna impresión. Consultando **por familia** hasta `has_more: false`, las mudas
  reales son **5**. No dar por muerta una URL sin esa comprobación.
- De esas 5: `plan-negocio-bar-restaurante` y `plan-negocio-parrillero-asador-eventos` están en
  **«URL is unknown to Google · last crawled: Never»** pese a existir desde el 19-jul y estar en
  el sitemap; `plan-negocio-paellero-eventos` está *crawled, currently not indexed*;
  `kit-tareas-sushi-bar` y `plan-negocio-food-truck` sí están indexadas, sólo son recientes.
  No hay bloqueo técnico: era **orfandad de enlaces internos** (tenían 3 y 7; ahora 24 y 24).
- **Las queries dicen que el camino NO es rankear las landings.** Llegan por «plantilla
  escandallo», «escandallo excel», «control de mermas formato excel **gratis**» — intención de
  descarga gratuita, en posiciones 15-85. Ahí no se gana. Encaja con el criterio de John: el
  catálogo vende **dentro de los contenidos**, y por eso el pase de banners es la palanca.

---

## 4. Qué queda abierto

**De John:**
- **Solicitar indexación manual en GSC** de `plan-negocio-bar-restaurante` y
  `plan-negocio-parrillero-asador-eventos`. Con 24 enlaces internos cada una el rastreo llegará
  solo, pero pedirlo ahorra semanas.
- Sigue pendiente el **cutover de `enblog.aichef.pro`** (`CUTOVER_ENBLOG_PENDIENTE.md`), sin
  relación con esta sesión.

**Para la próxima sesión (nada bloqueante):**
- **2 posts EN sin banners, a propósito:** `ai-restaurant-management-software` y
  `ai-food-cost-calculator-reduce-costs`. Son un **cuarto molde** que no estaba documentado —
  el cuerpo entero envuelto en `<div class="hero">` / `<header class="post-header">`, sin un
  solo punto de inserción a nivel superior. La guarda de contenedores los rechazó bien; meterlos
  a la fuerza rompería el HTML. Van a mano.
- La relevancia temática del pase fue del **23 %** (66 de 285 posts ES con producto fijado por
  tema; el resto salió de la rotación determinista). El mapa `TEMATICO` del script se puede
  enriquecer si se quiere subir esa proporción.
- **Blog PT tanda 5**: sigue construida y verificada, bloqueada por las imágenes
  (`SESSION_HANDOFF_2026-08-30-blog-pt-tanda5.md`). No se tocó.

- **⚠️ Los banners ingleses llevan a landings en español.** No es algo que introdujera esta
  sesión —los 27 posts EN que ya tenían banners hacían exactamente lo mismo— pero ahora son 64
  y conviene decidirlo: el copy del banner sí es inglés (`banner(..., lang='en')` saca nombre y
  descripción del campo `en` del catálogo), pero la URL de destino es el slug español
  (`/kit-escandallos`) y **no existe ninguna landing de producto bajo `/en/`**. O se localizan
  las landings, o se asume el salto de idioma en la conversión. Decisión de John.
- **Los roadmaps de DE/PT/FR/IT/NL siguen siendo válidos tal cual**: dicen «productos digitales
  ES-only → sin banners», y esta sesión sólo tocó ES e EN, así que esa decisión no cambia.

**Coordinación:** durante la sesión, la instancia de Claude Code que lleva Stripe/pagos en local
empujó 4 veces (webhook de Stripe activado, guía gastronómica, pasarela cripto). Se rebaseó sin
conflictos porque tocábamos ficheros distintos. **Si esa instancia va a escribir en
`astro-site/`, sincronizar antes de cada tanda.**
