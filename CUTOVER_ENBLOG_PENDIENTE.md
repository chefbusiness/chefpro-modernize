# PENDIENTE — Cutover de `enblog.aichef.pro` (acción de John)

> Estado a 2026-07-28. El blog EN ya está **live** en https://aichef.pro/en/blog (39 posts).
> Falta **sólo** apuntar el subdominio: hasta entonces el WordPress inglés sigue sirviendo
> las mismas piezas y hay contenido duplicado entre las dos propiedades.
> Mismo procedimiento que el cutover ES (8B.5, 2026-07-19), **con la trampa que nos costó aquella vez**.

## Qué está hecho y qué no

| | Estado |
|---|---|
| 39 posts EN en Astro, con imágenes, sitemap y hreflang | ✅ live |
| Navegación EN (header, footer, hero, barra de anuncios) apuntando al blog EN | ✅ live |
| Mapa 301 completo de `enblog.aichef.pro` en `astro-site/public/_redirects` | ✅ escrito, **inerte** |
| `enblog.aichef.pro` como alias del site en Netlify + DNS | ❌ **pendiente (tú)** |
| Apagar el WordPress inglés | ❌ no hasta que la batería dé 7/7 y el backup esté a salvo |

Las reglas son *host-scoped*: mientras el DNS apunte a Hostinger no se ejecuta ninguna,
así que el bloque es inofensivo. No hay prisa técnica; la única penalización de esperar
es el duplicado EN mientras tanto.

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

**Antes de tocar el DNS de `enblog`, comprueba si está en la misma situación**: si es el
dominio principal de su instancia WP, primero desvincúlalo y aparca el WP en su
`*.hostingersite.com`. Si no lo haces, verás A records reapareciendo solas y perderás la
tarde.

## Pasos

1. Netlify → site `aichefpro` → **Domain management** → añadir `enblog.aichef.pro` como
   *domain alias*.
2. DNS: `enblog` → **CNAME** → `aichefpro.netlify.app` (quitando las A records que
   apunten a Hostinger; ver la trampa de arriba).
3. Esperar propagación + certificado (en 8B.5 fueron minutos).
4. Batería de verificación:
   ```bash
   python3 scripts/astro-migration/fase8b-auditar-301.py --sitio en  # offline, 189/189
   python3 scripts/astro-migration/fase8b6-gate-301-en.py            # contra la red, 7/7
   ```
   El primero simula el motor de Netlify contra el censo completo del WordPress
   inglés (posts, páginas, categorías, tags, infraestructura) y exige que el
   destino final exista en el `dist`; se puede correr ya, sin DNS. El segundo va
   contra la red y sólo pasa después del cutover.
   Comprueba portada, post migrado, guía de ciudad no migrada, archive de categoría,
   feed, medios y catch-all: que cada uno haga **301** y que el destino responda **200**.
   *Antes* del cutover este gate da 0/7 con "sigue sirviendo el WP" — es lo normal.
5. Sólo con 7/7: dar por cerrada la Fase 8B.6 y planificar el apagado del WordPress inglés.

## Antes de apagar/cancelar nada

- El export completo del WP inglés está en el **VPS**, no en GitHub:
  `/root/aichef-blog-media/enblog-export/` (89 posts + páginas + taxonomías +
  **169 MB / 193 ficheros de medios**). Si ese VPS desaparece, desaparece el backup.
- Mismo criterio que con el WordPress español: **no se cancela el hosting hasta tener
  el backup en un sitio duradero** y la batería 301 en verde con margen de rollback.

## Rollback

Deshacer el CNAME y devolver el subdominio a Hostinger. El WordPress inglés no se toca
hasta el final justamente para que el rollback sea volver a apuntar el DNS.
