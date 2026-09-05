# Handoff — 2026-09-05 · los agentes se conectan con las cuentas del usuario (landing ×7 + post ×6)

**Estado: TODO CERRADO, desplegado y verificado en producción viva.** No hay nada a medias.
Commits `59b6da1d` (landing + home + nav), `25b33514` (los 6 posts), `96e1ae4d` (el pipeline)
y `b21670d6` (el gate de vigilancia). Rebasado sobre los 7 commits del Mac (línea A de planes
en v2.2) y build + gates repetidos sobre el árbol combinado antes de empujar.

---

## 1. Qué se anunciaba

John trajo tres mejoras aplicadas a **todos** los agentes de la plataforma:

1. **Razonamiento avanzado** — el agente piensa antes de responder. **El modelo NO se nombra en
   público** (decisión de John): se habla de la capacidad, no del motor, para no regalar el
   stack y para que el contenido no caduque al cambiar de modelo.
2. **Artefactos (Copilot)** — los agentes de chat crean y editan documentos, tablas,
   visualizaciones, componentes interactivos y ficheros HTML/CSS. **Las recetas y los
   escandallos quedan FUERA**: tienen acciones propias y se dice explícitamente.
3. **Conexión con plataformas externas vía Composio** — se invoca **hablando** dentro del chat
   («quiero enviar esta receta por correo vía Gmail»), no configurando. La autorización se pide
   la primera vez en la ventana oficial del servicio y dura hasta que caduca.

### Son 16 herramientas + Composio, no 17

El brief traía 17 líneas, pero **Composio no es una herramienta del chef: es el hub que gestiona
la autorización de las otras**. Contarlo dentro infla la cifra y confunde lo que se vende. Todo
el copy dice «16 herramientas» y nombra Composio aparte. Fuente canónica:
`astro-site/src/data/integraciones.ts`.

---

## 2. Lo construido

| Pieza | Dónde | Idiomas |
|---|---|---|
| Landing dedicada | `/integraciones` · `/en/integrations` · `/fr/integrations` · `/de/integrationen` · `/it/integrazioni` · `/pt/integracoes` · `/nl/integraties` | **7** |
| Sección de home | `components/IntegracionesShowcase.astro`, montada en los 7 `index.astro` | **7** |
| Enlace en navegación | `Header.astro` + `Footer.astro` + `ModernHeader.tsx` + `ModernFooter.tsx` | **7** |
| Post del blog | `agentes-ia-conectados-gmail-sheets-instagram` y hermanos | **6** (NL no tiene blog) |

**El markup de la landing vive UNA vez** (`components/IntegracionesPage.astro`) y el copy por
idioma en `src/data/integraciones-copy/`. Un arreglo de maquetación se hace una sola vez — que
es justo lo que no pasó con el hub de librerías y costó un enlace roto en el footer inglés.

### El enlace de nav hay que ponerlo en CUATRO ficheros

`Header.astro` y `Footer.astro` **no bastan**: las landings de marketing generadas en Fase 6
montan los gemelos de React `src/components/ModernHeader.tsx` y `ModernFooter.tsx`. Con sólo los
`.astro`, el enlace faltaría en media web. Las tablas de rutas están **duplicadas a propósito**
en los `.tsx` porque la SPA vive en otra raíz y no puede importar de `astro-site/`; si cambia un
slug hay que tocar los dos sitios (está comentado en ambos).

### Los logos

`components/BrandIcon.astro` — **13 SVG de Simple Icons (CC0) inline**, no `<img>`: cero
peticiones en una rejilla de 17, recoloreables y sin depender de un CDN de terceros.

- ⚠️ **Outlook, Canva, LinkedIn y Composio NO están en Simple Icons** — esas marcas pidieron
  que se retirasen. Van como **tesela con inicial y color oficial de marca**. Redibujarlas a
  ojo se ve peor que no ponerlas. Si algún día se quieren los reales: API de Composio (pide
  clave) o la página de brand assets de cada marca.
- ⚠️ **Notion, TikTok y X son negros (#000000)** y desaparecerían sobre el fondo del modo
  oscuro: llevan color alterno declarado en `DARK`.

### La animación

Marquesina infinita en **CSS puro, sin una línea de JS**: la lista se pinta dos veces y se
desplaza el 50 %, así el reinicio no se ve (el duplicado lleva `aria-hidden`). Se para al pasar
el ratón. **Respeta `prefers-reduced-motion`**: con la preferencia activada la cinta se queda
quieta y se recorre con scroll horizontal.

### SEO

Schemas de la landing: `WebPage` + `BreadcrumbList` + `ItemList`(16) + `FAQPage`, enlazados por
`@id`. **NO se emite `SoftwareApplication`**: `BaseLayout` ya publica el global del SaaS con sus
`offers` y precios reales, y emitir otro dejaba **dos nodos «AI Chef Pro» en la misma página**,
siendo el mío el pobre. Canonical y hreflang correctos en los 7 con `x-default` al español, sin
el bug del prefijo duplicado (`basePath` va sin idioma y además se pasa el mapa `alternates`
completo, así que `urlFor()` nunca llega a componerlo).

---

## 3. Tres modos de fallo NUEVOS del pipeline de traducción, cada uno con su gate

Todos vistos este día, y los tres pasaban desapercibidos con los controles que había.

| Fallo | Qué pasó | Gate que lo caza |
|---|---|---|
| **El alemán rompe el JSON** | Cierra comillas con `„ … “` y emite el cierre como comilla **RECTA** (U+0022), que termina la cadena. Falló con **los dos motores** aun pidiéndoselo expresamente | `repara_comillas()`: escapa las comillas sueltas dentro de los valores. Se repara, no se pide por favor |
| **Sobraba contenido, no faltaba** | El francés devolvió el artículo **TRES veces** (3.241 palabras y 13 encabezados donde el español tiene 1.293 y 5) y **pasaba todos los controles**, porque sólo miraban que no faltara nada | Gates acotados **por arriba**: nº de H2 igual al español, palabras en [0,6×, 1,5×] y sin párrafos repetidos literalmente |
| **La estructura no se conserva** | Traducir el artículo entero y confiar en que respete los 5 encabezados no funciona: el alemán volvió con 6, luego con 4; el portugués con 6. Oscilaba entre reintentos | **Traducir POR SECCIONES** (`trocea()`): cada pieza lleva 0 o 1 encabezados, así que fundir o inventar una sección es imposible por construcción |

### El tratamiento al lector cambia por idioma y hay que IMPONERLO y VERIFICARLO

Medido sobre `src/i18n/locales/*.json` (ocurrencias en el sitio ya publicado):

**es tú (306) · fr vous (405) · de Sie (1009) · it tu (307) · pt você (233) · nl u (452)**

El español original tutea, así que **todo idioma formal necesita que se le diga expresamente**:
la primera pasada del francés vino con «tu/tes» y había que tirarla; el alemán igual. La
instrucción no basta —el modelo la ignora a veces—, así que `revisar_tratamiento()` **cuenta los
marcadores sobre el resultado** y rechaza la traducción si gana el contrario. Cazó también el
portugués.

### Y una de motor

**DeepSeek se atascó 40 minutos sin devolver nada** en el post donde **Sonnet resolvió el
artículo entero en cinco**. Es el patrón ya documentado (prompt con tabla de cifras a medida).
El primer motor tiene ahora **timeout corto (420 s)** y se cae a `anthropic/claude-sonnet-4.6`.
Para el alemán, que falló con DeepSeek en **todos** los intentos de la sesión, se fue directo a
Sonnet.

---

## 4. Dos errores que habrían salido publicados

1. **«Está disponible para todos los usuarios, incluido el plan gratuito».** Lo escribió el
   modelo y **es falso: en la web ya no hay plan gratuito** (el Miembro son 10 €/mes desde la
   fase 11). Corregido en el español **antes** de traducir, así que no se propagó a ningún
   idioma. Regla: **revisar siempre las cifras de plan que invente el modelo.**
2. **Composio llamado «el estándar».** Es una capa/plataforma, no un estándar — y además se
   contradecía con la propia FAQ de la página, que dice «la capa». Corregido en los 7.

Y una **FAQ duplicada entre landing y post** («¿Qué es Composio?» con la misma respuesta en dos
`FAQPage` del mismo dominio): la del post se reformuló a «¿Tengo que crear una cuenta en
Composio?», que además responde algo útil.

---

## 5. Decisiones de alcance

- **El neerlandés NO lleva post.** `/nl/blog` no existe (`hasBlog('nl')` es falso) y sería un
  404. Ve la novedad en su home y en su landing, que sí están en NL.
- **Los banners de producto van sólo en ES y EN.** `src/data/products-catalog.ts` sólo tiene
  nombre y descripción en esos idiomas y las landings de producto tampoco existen en los otros;
  medido: los 49 posts de los blogs FR/DE/IT/PT tienen **cero** banners. Uno en francés mandaría
  al lector a un checkout en español.
- **El post enlaza a la landing** con URL absoluta (convención del repo: 2.278 usos frente a 28
  relativos). El post es el anuncio; la landing, la referencia permanente.
- `translations:` recíproco **ES↔EN** en el post — es el mismo contenido adaptado. Va en el
  ensamblador, no a mano: reensamblar el post lo borraba.

---

## 6. El gate de vigilancia llevaba desviado desde antes, y no lo sabíamos

Al desplegar, `fase7-vigilancia.py` cantó **1206 URLs != 1197**. `_F8_EXTRA` es una lista **a
mano** de las URLs nativas fuera del blog, con un comentario que pide mantenerla al día, y las 7
landings nuevas no estaban. Culpa de esta sesión.

**Pero salieron 9 de diferencia, no 7.** Reconstruido el cálculo sobre `c825e95f` —el commit
anterior a este trabajo— daba **1187 esperadas frente a 1189 servidas**: el gate ya venía
desviado en 2. Las culpables: **`/productos-digitales` y `/seo-restaurantes-por-ciudad`**, dos
páginas públicas, en el sitemap y enlazadas desde el header español, que nunca se declararon.

Declaradas las nueve. **Una alarma que no cuadra deja de avisar de lo que importa**, y ésta
llevaba tiempo roja por un motivo que nadie miraba.

---

## 7. Estado al cerrar — verificado en producción viva

- **13/13 URLs en HTTP 200** (7 landings + 6 posts).
- **Los 7 homes** sirven la sección y enlazan a su landing, 4 enlaces cada uno (nav escritorio,
  nav móvil, footer y CTA de la sección).
- Las 3 imágenes del post + la OG de la landing, en 200.
- **Sitemap: 1.206 URLs** (antes 1.189), con las 13 nuevas. **Reenviado a Search Console** el
  2026-09-05 a las 19:26.
- Gates: **WhatsApp verde** (1 botón por página, sin duplicados) · **robots verde** (ninguna URL
  pública bloqueada) · **H1 único** · **FAQ duplicadas** sin marcar ninguno de los nuevos ·
  **`fase7-vigilancia.py` todo verde**.
- `blog-lastmod.json` regenerado (446 entradas).

### Lo único que queda pendiente

1. **Los 4 logos en tesela** (Outlook, Canva, LinkedIn, Composio). Si se quieren los reales:
   clave de la API de Composio, o bajarlos de las brand assets de cada marca.
2. **Mirar en GSC dentro de 2-3 semanas** si las 7 landings entran en el índice.
3. **Tarea aparte abierta por John: «herramientas» → «agentes»** en todas las landings y
   metadatos. **Medido y con riesgo casi nulo**: en 90 días sólo 3 queries y ~10 clics dependen
   de esa palabra (`ai chef tools` 8, `free ai tools for restaurants` 1, `free tools` 1) y las
   **77 menciones de `marketing-heads/*.ts` no rankean para nada**. El tráfico del sitio es marca
   (`ai chef pro` 393, `ai chef` 273) y long-tail de glosario. Plan: empezar por los
   title/description, después los locales i18n, y **NO tocar los slugs de URL** (obligarían a
   301 en 7 idiomas a cambio de nada). Ver memoria `herramientas-vs-agentes`.

---

## 8. Piezas del pipeline

| Fichero | Para qué |
|---|---|
| `scripts/astro-migration/fase12-integraciones.py` | Genera las 7 landings y las claves i18n de la home desde el mismo copy |
| `scripts/astro-migration/fase12-traducir-copy.py` | Traduce el copy de la landing (con los gates de estructura, alfabeto, tratamiento y el reparador de comillas) |
| `scripts/astro-migration/fase12-post-traducir.py` | Traduce el post **por secciones**; `--solo-meta` rehace los metadatos sin retraducir el cuerpo |
| `scripts/astro-migration/fase12-post-assemble.py` | Monta el `.md`: frontmatter + FAQ + banners + imágenes intercaladas |
| `scripts/astro-migration/fase12-post-brief.txt` | El brief con el que se escribió el español |
| `scripts/astro-migration/fase12-copy/`, `fase12-post-copy/`, `fase12-post-cuerpo/` | El copy fuente y sus traducciones |
