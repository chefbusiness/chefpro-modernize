# SESSION HANDOFF — 2026-07-28/29 (cierre de 8B.6 + auditoría del mapa 301)

> Doc canónico: `PLAN_MAESTRO_MIGRACION_ASTRO_2026.md` §8 (entrada 2026-07-28/29).
> Runbook abierto: `CUTOVER_ENBLOG_PENDIENTE.md`. Sesión trabajada desde el **VPS**.

## ✅ Qué quedó HECHO y VERIFICADO

1. **Fase 8B.6 — el blog EN entra en `aichef.pro/en/blog`** (`621e2e2`)
   - 39 de los 89 posts de `enblog.aichef.pro`; las **50 guías de ciudad NO se migran**
     (0 clics, plantilla por ciudad = doorway pages; mismo criterio Tier D del ES).
   - `lib/blog.ts` pasa a estar **indexado por idioma** y todas las URLs salen de helpers
     (`postPath`/`categoryPath`/`listPagePath`/`blogBase`) — única fuente de verdad.
   - Segmentos nativos en inglés (`/en/blog/category|page/…`), copy nativo (no traducido),
     CTA a `enapp.aichef.pro`, imágenes en `/blog-assets/en/`, `locales={[lang]}` para no
     declarar pares ES↔EN que no existen.
   - Build limpio 1.216 páginas · 43 URLs EN en el sitemap con lastmod real.

2. **Navegación EN arreglada** (`80758c2`, `1a52543`)
   - Header/Footer/Hero mandaban al blog **español**; ahora `blogHubHref(lang)`.
   - Barra de anuncios EN → `/en/blog/best-ai-tools-for-chefs-2026` + copy nuevo en
     `en.json` (compartido con la SPA → cambiados los dos sitios que la pintan).
   - **El árbol EN ya no contiene ningún enlace al blog ES.**

3. **🐛 EL HALLAZGO DE LA SESIÓN — 24 familias de URL hacían 301 a un 404** (`7674af5`, `542721c`)
   - Causa: **el WordPress sirve las archives de categoría en la RAÍZ** (base de categoría
     vacía) y caían en la genérica `/:slug → /blog/:slug`, que las trata como posts.
   - Auditando el censo completo aparecieron 16 familias más: las **7 páginas del WP**,
     los **sitemaps hijos**, `robots.txt`, `favicon.ico`, archives de año, `/amp`,
     `/wp-login.php`, `/wp-admin`, `/xmlrpc.php`.
   - Arreglado en los **dos mapas y los dos generadores**, con destinos con sentido
     (`/about`→`/sobre-nosotros`, `/contact`→`/contacto`, sitemaps→`sitemap-index.xml`).
   - Verificado live: las 16 del ES hacen 301 → 200.

4. **Gate permanente: `scripts/astro-migration/fase8b-auditar-301.py --sitio es|en`**
   - Simula el motor de Netlify contra el censo del export, sigue cadenas y exige que el
     destino exista en el `dist`. **ES 508/508 · EN 189/189 · 0 rotos · 0 cadenas.**
   - Complemento contra red para después del DNS: `fase8b6-gate-301-en.py` (7/7).

5. **Respaldo** — el export del WordPress inglés existía en **una sola copia** (VPS).
   Subido al repo privado `chefbusiness/aichef-blog` → `enblog-export-2026-07-28/`
   (texto: 89 posts + páginas + taxonomías; medios fuera por convención, con el estado
   documentado en su README).

## ⚠️ Gotchas nuevos (ya en CLAUDE.md)

- **La genérica `/:slug` se traga TODO lo que llegue con un solo segmento**, no sólo los
  posts. Cada familia de un segmento que no sea un post necesita regla propia ANTES.
  Correr `fase8b-auditar-301.py` siempre que se toque `_redirects`.
- En Header/Footer/Hero el hub es **`blogHubHref(lang)`, nunca `blogBase(lang)`**:
  `/fr/blog`, `/de/blog`… no existen y serían un 404 en 5 idiomas.
- Las categorías se resuelven **con idioma** (`getCategory(slug, lang)`): `ai-chef-pro`
  existe en ES y en EN.

## ⏳ PENDIENTE DE JOHN (confirmado el 2026-07-29: "las ejecutaré más tarde o mañana")

1. **`enblog.aichef.pro` → alias en Netlify + DNS.** Sin esto el mapa 301 del blog inglés
   está escrito pero inerte. **Ojo a la trampa de 8B.5**: si el subdominio es el dominio
   principal nativo de su instancia WP, el panel de Hostinger **recrea las A records** solo;
   hay que desvincularlo y aparcar el WP en su `*.hostingersite.com`. Todo en
   `CUTOVER_ENBLOG_PENDIENTE.md`.
2. **Search Console** (sólo UI, la API no expone esos botones): solicitar indexación de las
   archives de categoría y 3-4 posts prioritarios; dar de baja los **5 sitemaps muertos** de
   `blog.aichef.pro` (y los 4 de `enblog` tras su cutover).

## 📊 Estado real medido en GSC (no impresiones, datos)

- **El blog migrado funciona y sube**: `aichef.pro/blog/` hizo **76 clics y 7.428
  impresiones en 7 días** (22→28 jul), con tendencia clara al alza (4→21 clics/día,
  811→1.510 impresiones/día) y posición media 8,8. El viejo subdominio promediaba ~629
  impresiones/día en 90 días: **en impresiones ya se está por encima**, en clics todavía no
  (CTR ~1% a posición 8,8 → margen evidente en titles/metas).
- **Lo que estaba roto casi no tenía tráfico**: las 24 familias sumaban ~61 impresiones y
  4 clics en 90 días sobre 56.582 del subdominio, y GSC las da como "URL desconocida,
  nunca rastreada". El bug era real; su impacto medible, ridículo. **No hay nada que
  revalidar** en el informe de indexación.
- **Dato para decidir ruta**: el **74% de los clics del subdominio viejo (1.539 de 2.087 en
  90 días) venía de las traducciones automáticas de GTranslate**, que hoy hacen 301 al hub
  ES. Por idiomas soportados por el producto: **it 140 · pt 112 · fr 111 clics**. El resto
  son fa (251), ka, bs, bg, uk, ru, ko… sin producto ni monetización detrás.

## 🧭 Rutas posibles para la próxima sesión

| Ruta | Por qué sí | Coste | Evidencia |
|---|---|---|---|
| **A. Cerrar 8B.6** | Desbloquea apagar el WP inglés y recupera los 301 del subdominio | 15 min de John + verificación | gate listo, 7/7 esperado |
| **B. CTR del blog** | 7.428 impresiones/semana a posición 8,8 con CTR 1%: es la ganancia más barata que hay | 1 sesión | striking distance ya en §5 del plan |
| **C. 8C — páginas por agente (~70)** | Son las páginas que **monetizan**, absorben las 25 librerías de prompts con 301 y dan esqueleto de enlazado interno | varias sesiones | plan maestro §4 |
| **D. 8C fase 2 — escáner de riesgo de imagen** | Media hecha (1.003 imágenes escaneadas en fase 1) y es riesgo legal/marca, no SEO | corta | `fase8c-escanear-caras.py` |
| **E. 8B.7 — blog en it/pt/fr** | 363 clics/90d demostrados que hoy se tiran al hub; la infraestructura multi-idioma ya está construida | alta (contenido) | tabla GTranslate de arriba |
| **F. Fase 9 — sustituir Pickaxe** | El salto de producto, no de SEO | proyecto | `REPLICAR_Y_SUSTITUIR_PICKAXE.md` |

**Recomendación**: **D** primero (es riesgo abierto y está a medias, sale barato), luego **C**
como línea principal —las páginas de agente monetizan y de paso arreglan el enlazado interno,
que es justo lo que le falta a lo que ya está publicado—, con **B** como relleno de sesiones
cortas. **E** después de C, cuando el dominio tenga más autoridad. **A** en cuanto John pueda.

## Commits de la sesión

`621e2e2` 8B.6 blog EN · `4f7e1c7` escáner de imagen 8C · `3e03e2f` package-lock ·
`80758c2` navegación EN · `57ae612` mapa 301 EN · `b2e289f` docs 8B.6 ·
`1a52543` barra de anuncios EN · `7674af5` archives de categoría 301→404 ·
`23659b0` runbook del cutover · `542721c` auditoría completa del mapa 301 ·
`772ed0d` paso GSC del runbook
