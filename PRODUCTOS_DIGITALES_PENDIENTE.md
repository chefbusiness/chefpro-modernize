# Productos digitales — PENDIENTE (nota de traspaso)

> **Estado: EN PAUSA por decisión de John (2026-08-08).** Esta línea de trabajo se
> retoma desde Claude Code en local. La sesión del VPS **no sigue** por aquí.
>
> Todo lo de abajo sale de una auditoría adversarial de 6 lentes con refutadores
> (2026-08-08). Cada cifra está medida contra el repo **y** contra producción
> viva, no deducida. Si algo se contradice con lo que veas, gana lo que midas hoy.

---

## 1. YA ARREGLADO Y EN PRODUCCIÓN — no lo rehagas

**`7e050c5` — Los 524 entregables daban 404 desde el 2026-07-19.**

El cutover de Fase 7 (`efa8bb7`) cambió el publish dir a `astro-site/dist` y
**16 entradas de `public/` nunca se movieron**. Durante 20 días, todo cliente que
compraba entraba a su dashboard, pulsaba descargar y recibía un 404.

Resuelto con `git mv public/<X> astro-site/public/<X>` (no copia: la SPA ya no se
construye). Verificado en producción tras el deploy: **42 de 42 productos con su
entregable vivo, 0 fallos**, más los 41 ficheros sueltos de la raíz de `/dl`.

Se movieron: `dl/` (524 ficheros, 8,8 MB), los **9 `og-*.jpg`** de las landings de
producto —las tarjetas de compartir salían sin imagen—, `ebook-mockup-bundle.png`
(referenciado por 4 páginas vivas), `email-assets/` (lo usan las plantillas de
`email-campaigns/`), `payment-logos/`, `images/`, `placeholder.svg`,
`ebook-cover.jpg`.

**NO se movieron `public/sitemap.xml` ni `public/sitemap.xsl`, y es deliberado:**
desde Fase 7 el sitemap lo genera Astro (`sitemap-index.xml`) y ese fichero ya no
es la fuente. Publicarlo crearía un `/sitemap.xml` rival con datos rancios.

⚠️ **La lección, para que no vuelva a pasar:** cualquier cosa que viva sólo en
`public/` de la raíz **no se publica**. Antes de dar por bueno un asset, `curl` a
producción. Un gate que compare `public/` contra `astro-site/public/` evitaría la
próxima; no está escrito.

---

## 2. PENDIENTE — el diagnóstico, para que no haya que repetir la auditoría

### 2.1 La línea NUNCA se ha internacionalizado, ni al inglés

44 productos / **133 páginas** (45 landings + 44 `-access` + 44 `-library`).
En el sitemap de producción: **45 URLs de producto en ES y CERO** en EN, IT, FR,
DE, PT y NL.

No hay maquinaria de idioma que reutilizar — pero tampoco deuda de un intento
anterior mal hecho. El primer producto no español paga el coste de la
infraestructura (rutas, hreflang, plantilla consciente del idioma).

### 2.2 Los entregables no son «traducibles»: son producto ESPAÑOL

Medido sobre `public/dl/` (hoy `astro-site/public/dl/`): **233.575 palabras**.

| Formato | Nº | Volumen |
|---|---|---|
| `.xlsx` | 454 | 1.301 hojas → 18.521 cadenas únicas / 95.532 palabras |
| `.docx` | 61 | 138.043 palabras |
| `.pdf` | 9 | — |

Y llevan **normativa española dentro**: «España» aparece 265 veces en 39 de los 61
docx, «APPCC» 96 veces en 30, «IVA» 85 en 14, «autónomo» 40 en 19.

**Esto parte la línea en dos:**

- **24 productos** (5 kits Excel + 19 `kit-tareas`): contenido mayoritariamente
  operativo → **sí se traduce**. Estimación: 3-5 semanas con QA.
- **18 productos** (10 planes de negocio + 8 guías): son los de mayor precio y los
  que llevan el marco legal y fiscal español → **no se traducen, se reescriben**
  con criterio legal italiano. Es otro proyecto, no una traducción.

### 2.3 La mitad de los entregables sólo existe como binario

`ls scripts/generate-*.py` → **22 generadores, 29.188 líneas**, ~25.794 cadenas
literales (~111k palabras). Cubren escandallos, appcc, gestión de personal,
inventario, plan financiero, 9 variantes de tareas y 7 guías.

Pero **de los 42 directorios de `/dl` faltan generadores para el resto**. Donde hay
generador, el italiano es «traducir literales y re-ejecutar»: limpio, repetible y
versionado. Donde no lo hay, toca editar `.xlsx`/`.docx` a mano o rescatar el
generador del repo hermano.

👉 **Primer paso recomendado:** auditar qué generadores existen en
`chefbusiness-astro` (2-3 h) y **priorizar para italiano los productos que sí
tienen generador**. Cambia el coste por un factor de dos.

### 2.4 Lo que NO hay que tocar (buena noticia)

**Stripe y el gate JWT son agnósticos al idioma.** Mismo Payment Link, mismo JWT,
las mismas 4 functions de `netlify/functions/`. La capa donde un error cuesta
dinero de verdad se reutiliza tal cual.

⚠️ Queda **una cosa por confirmar fuera del repo**: si **Stripe Tax** está
configurado para el IVA italiano. No se pudo medir sin acceso al panel de Stripe.

### 2.5 Bugs concretos, con fichero y línea

| Dónde | Qué pasa |
|---|---|
| `src/data/products-catalog.ts:1` | Declara `ProductLang = 'es'\|'en'\|'fr'\|'de'\|'it'\|'pt'\|'nl'`, pero `localize()` hace `entry.name[lang as 'es'\|'en'] ?? entry.name.es`. Los 25 productos sólo tienen `name`/`description` en es y en → **pedir 'it' devuelve español en silencio, y la `url` va sin prefijo de idioma**. Rompería la política de 3 banners por post en italiano: banner con nombre español apuntando a landing española. Falla sin ruido. ~2-3 h |
| `src/data/productos-digitales-config.ts` | 44 productos × 6 campos de email = **3.713 palabras en español**, sin parámetro de idioma. El HTML envolvente de `netlify/functions/` también. **El italiano paga y el único email que recibe —el del enlace mágico de acceso vitalicio— llega en español.** Es el punto de máxima fricción post-pago y causa típica de disputa en Stripe. ~1-2 días: añadir `lang` al payload del JWT y a las 3 functions, y convertir `PRODUCTS_CONFIG` en `Record<lang, campos>` con fallback |
| `astro-site/src/pages/*-library.astro` (44) | Montan el dashboard **sin prop `lang`**. `noindex` y excluidas del sitemap por `astro.config.mjs:54-55` (sufijos `-access`/`-library`). No son superficie SEO, pero sí interfaz que el cliente italiano vería en español |
| Un `.docx` sospechoso | La auditoría marcó uno que parece portada suelta o entregable vacío en un producto de 45-85 €. **Merece 10 minutos de comprobación abriéndolo** antes de replicar el patrón |

### 2.6 Sin blog italiano no hay canal que distribuya los banners

`astro-site/src/content/blog/` sólo tiene `es` (324 `.md`) y `en` (65). **0 posts
italianos.** Hoy la política de 3 banners produce 114 banners en 38 posts ES y 78
en 26 posts EN; en ES, **34 de los 114 (35 %) tiran de `kit-escandallos`**, y el
blog es el único canal de descubrimiento orgánico de los productos.

Aunque existieran landings italianas, no habría de dónde alimentarlas. El blog IT
es prerrequisito, no un extra.

---

## 3. Fuera de esta nota pero bloqueante para medir Italia

**`itapp.aichef.pro` no tiene la etiqueta de conversión.** `curl` a
`https://itapp.aichef.pro/ospite` (200, 114.207 bytes) → **0 apariciones de
`AW-17829651892`**. La española sí: `app.aichef.pro/invitado` → 9 apariciones de
`AW-17829651892`, 4 de `googletagmanager`, 31 de `gtag`.

Sin eso **no se registra ni una conversión del italiano**, y Google Ads no puede
pujar hacia algo que no mide. Es **tarea manual de John**, sin código: pegar en el
campo **Body** del workspace italiano de Pickaxe el mismo snippet documentado en
`GOOGLE_ADS_PICKAXE.md`. 30-45 min.

Recordatorio del gotcha ya documentado: en el alta **no existe página de
confirmación** (es un modal), y `?success=login` **no distingue registro de
login** — lo que sí lo distingue es que el modal de alta es el único con **dos
campos de contraseña**.

---

## 4. Orden sugerido cuando se retome

1. **Confirmar Stripe Tax / IVA italiano** en el panel. Si no está, nada de lo
   demás importa: no se puede cobrar bien en Italia.
2. **Auditar generadores en `chefbusiness-astro`** (2-3 h) → decide qué productos
   son baratos de traducir.
3. **Arreglar `products-catalog.ts`** (`localize` + prefijo de idioma en `url`).
   Es la pieza que rompería los banners en cuanto exista el blog italiano.
4. **Internacionalizar los emails transaccionales.** Cobrar en italiano y
   responder en español es lo que genera disputas.
5. **Un solo producto italiano de punta a punta** como piloto — de los que tienen
   generador— antes de escalar a los 24.
6. **Escribir el gate** `public/` vs `astro-site/public/` para que el fallo de la
   sección 1 no pueda repetirse.
