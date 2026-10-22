# PENDIENTE — Cutover de `enblog.aichef.pro` (acción de John)

> Decisión del 2026-10-22: los subdominios de blog se dan por muertos. Todo el
> contenido vive en `aichef.pro`. El diagnóstico en vivo de ese día cambió el
> plan de abajo: **no es el mismo hosting para los dos**.

## Dónde se sirve cada uno (medido el 2026-10-22)

| Host | DNS | Quién responde | Qué hacer |
|---|---|---|---|
| `blog.aichef.pro` | CNAME `aichefpro.netlify.app` | Netlify (`server: Netlify`, `x-nf-request-id`). El WordPress ya no está en el camino. | Nada de DNS ni de Hostinger. El arreglo está en este repo y se activa al desplegar. |
| `enblog.aichef.pro` | A `92.112.198.181`, `148.135.128.8` | WordPress en Hostinger (`platform: hostinger`, `server: hcdn`, `x-powered-by: PHP/8.3.35`, LiteSpeed). Canonical propio, HTTP 200. | Aplicar el `.htaccess` de abajo. El DNS a Netlify es el cierre, no el primer paso. |
| `aichef.pro` | A `75.2.60.5` (anycast de Netlify) y `www` CNAME al mismo site | Astro | Canónico. |
| `app.aichef.pro` | CNAME `cname.vercel-dns.com` | Vercel (Pickaxe) | No se toca. |

No hay otro proyecto Vercel en la cuenta con «aichef» en el nombre. El sitio de Netlify que ya tiene el alias `blog` es `aichefpro`.

## Qué es más simple y más seguro

**Para `enblog`, el `.htaccess` ahora. El CNAME a Netlify después.**

El `.htaccess` (`scripts/astro-migration/hostinger/enblog.htaccess`) corta los 200 hoy, sin pelearse con las A records. Hostinger ya demostró (cutover de `blog`, más abajo) que recrea las A si el subdominio sigue siendo el dominio principal de la instancia WordPress. El mapa de Netlify ya está en `astro-site/public/_redirects` y es el mismo: cuando el `.htaccess` lleve días en verde, se desvincula el WordPress y se apunta el CNAME. Hasta entonces las reglas de Netlify siguen inertes.

La alternativa del plugin Redirection es `scripts/astro-migration/hostinger/enblog-redirection.csv` (Import). Cubre cada URL censada una a una y no incluye un comodín, para no cerrar `/wp-admin`. El `.htaccess` es el completo: también tiene el comodín y deja el admin fuera a propósito.

Pasos en hPanel, en este orden:

1. Archivos del WordPress de `enblog` → `.htaccess` de la raíz. Pegar el fichero **encima** de `# BEGIN WordPress`. Dentro, WordPress lo borra al guardar enlaces permanentes.
2. No redirige `/wp-admin`, `/wp-login.php` ni `/wp-json`. Si se redirigen, no hay forma de quitar el fichero.
3. hPanel → caché / CDN → purgar `enblog.aichef.pro`. La hCDN estaba devolviendo 200 cacheados (`x-hcdn-cache-status: HIT`).
4. Comprobar, con barra final (WordPress hace 301 a la barra):
   ```bash
   curl -sI https://enblog.aichef.pro/best-ai-tools-for-chefs-2026/
   curl -sI https://enblog.aichef.pro/menu-engineering-software-complete-guide/
   curl -sI https://enblog.aichef.pro/ai-menu-engineering-for-chefs-in-london/
   curl -sI https://enblog.aichef.pro/
   ```
   Los dos primeros tienen que ir a `https://aichef.pro/en/blog/<mismo-slug>` (301) y esa URL tiene que dar 200. La guía de ciudad y la portada van a `https://aichef.pro/en/blog`.
5. Solo entonces, si se quiere apagar Hostinger: desvincular `enblog` de la instancia WP (aparcarla en su `*.hostingersite.com`), añadir `enblog.aichef.pro` como domain alias del site `aichefpro` en Netlify, y CNAME `enblog` → `aichefpro.netlify.app`. La trampa de las A records de abajo sigue vigente.

**Para `blog.aichef.pro` no hay paso de Hostinger.** Ya es alias de Netlify. Al desplegar este repo:

- `/{en,fr,de,it,pt,nl}/…` deja de caer en `/blog` (español). La edge function `legacy-blog-lang` manda al mismo post si existe y, si no, al índice de ese idioma. `_redirects` repite el índice por si la función no corre.
- Las guías de ciudad `ia-*-en-{ciudad}` dejan de ir a `/abrir-restaurante` (era un **404**) y van a `/abrir-restaurante/{ciudad}`, o al hub `/seo-restaurantes-por-ciudad` si la ciudad no está (Lima, Miami).
- La portada del subdominio, para un navegador, ya no hace 302 a `/en` del mismo host: `lang-redirect` solo actúa en `aichef.pro` y `www`.

Mapa completo: `scripts/astro-migration/legacy-subdominios-301.csv`.
Candidatos a recrear (comparativas sin post nativo en FR/DE/IT/PT/NL): `scripts/astro-migration/legacy-subdominios-huerfanos.csv`.

## Qué está hecho y qué no (histórico, 2026-07-28)

El blog EN ya estaba live en https://aichef.pro/en/blog. Faltaba apuntar `enblog`.
El procedimiento de DNS es el mismo que el cutover ES (8B.5, 2026-07-19), **con la trampa que costó aquella vez**. El `.htaccess` de arriba no sustituye ese cuidado: lo aplaza hasta que los 301 ya estén sirviendo.

| | Estado a 2026-10-22 |
|---|---|
| Posts EN en Astro, con imágenes, sitemap y hreflang | ✅ live (el censo REST de enblog sigue en 89; 39 con slug idéntico en `/en/blog`, 50 guías de ciudad al índice) |
| Mapa 301 de `enblog.aichef.pro` en `astro-site/public/_redirects` | ✅ escrito, **inerte hasta el CNAME** |
| El mismo mapa en `.htaccess` para Hostinger | ✅ en el repo, **pendiente de pegarlo** |
| `enblog.aichef.pro` como alias del site en Netlify + DNS | ❌ no hacerlo antes del `.htaccess` y de desvincular el WP |
| `blog.aichef.pro` | ✅ ya es alias de Netlify desde 8B.5 |

## La trampa de la vez anterior (esto es lo que costó dinero en 8B.5)

`blog.aichef.pro` **era el dominio principal nativo de la instancia de WordPress**
(un apaño manual de Hostinger de hace ~2 años). Consecuencia: **el panel de Hostinger
recreaba las A records** cada vez que se intentaba dejar el CNAME hacia Netlify, y el
cutover se quedó atascado sin causa aparente.

Se resolvió así:

1. **Desvincular el subdominio de la instancia WP** y aparcar el WordPress en su dominio
   nativo de Hostinger (`darkgrey-dugong-825343.hostingersite.com`), que quedó como
   backup vivo y navegable.
2. Sólo entonces el CNAME `blog` → `aichefpro.netlify.app` se quedó quieto.
3. Netlify emitió el certificado SSL en minutos, sin tocar nada más.

**Antes de tocar el DNS de `enblog`, hay que hacer lo mismo**: si es el dominio
principal de su instancia WP, primero desvincularlo y aparcar el WP en su
`*.hostingersite.com`. Si no, las A records reaparecen.

## Pasos de DNS — solo después del .htaccess

1. Netlify → site `aichefpro` → **Domain management** → añadir `enblog.aichef.pro` como
   *domain alias*.
2. DNS: `enblog` → **CNAME** → `aichefpro.netlify.app` (quitando las A records que
   apunten a Hostinger; ver la trampa de arriba).
3. Esperar propagación + certificado (en 8B.5 fueron minutos).
4. Batería de verificación:
   ```bash
   python3 scripts/astro-migration/fase8b-auditar-301.py --sitio en  # offline, necesita el export del VPS y un dist
   python3 scripts/astro-migration/fase8b6-gate-301-en.py            # contra la red, 7/7
   ```
   El primero simula el motor de Netlify contra el censo completo del WordPress
   inglés (posts, páginas, categorías, tags, infraestructura) y exige que el
   destino final exista en el `dist`; se puede correr ya, sin DNS, si el export
   sigue en el VPS (`/root/aichef-blog-media/enblog-export/`). El segundo va
   contra la red y sólo pasa después del cutover.
5. Search Console, cuando el gate esté en verde:
   - reenviar `https://aichef.pro/sitemap-index.xml`;
   - **borrar a mano** los sitemaps de `enblog.aichef.pro` que sigan dados de alta
     (`sitemap_index.xml`, `post-sitemap.xml`, `page-sitemap.xml`, `category-sitemap.xml`).
     El sitemap de producción (`sitemap-0.xml`, 1.279 URLs el 2026-10-22) no cita
     ni `blog.` ni `enblog.`.

## Antes de apagar/cancelar nada

- El export completo del WP inglés está en el **VPS**, no en GitHub:
  `/root/aichef-blog-media/enblog-export/` (89 posts + páginas + taxonomías +
  **169 MB / 193 ficheros de medios**). Si ese VPS desaparece, desaparece el backup.
- Mismo criterio que con el WordPress español: **no se cancela el hosting hasta tener
  el backup en un sitio duradero** y la batería 301 en verde con margen de rollback.

## Rollback

Quitar el bloque pegado en el `.htaccess` (el admin sigue abierto) y purgar la hCDN.
Si ya se cambió el DNS: deshacer el CNAME y devolver el subdominio a Hostinger.
El WordPress inglés no se toca hasta el final justamente para que el rollback sea
volver a apuntar el DNS.
