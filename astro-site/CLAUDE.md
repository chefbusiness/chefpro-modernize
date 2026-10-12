# astro-site — medición, layout y widgets

> Movido literalmente desde el `CLAUDE.md` raíz el 2026-10-12 (/doctor) para no cargarlo en cada sesión. Los no negociables siguen resumidos en la raíz, sección «Detalle bajo demanda».

### Medición: Google Ads y consentimiento (desde 2026-08-03)

- **Hasta esta fecha el sitio no tenía NINGÚN tag** —ni analítica ni publicidad—.
  Ahora `AW-17829651892` con **Consent Mode v2** (denegado por defecto) y banner
  de cookies en los 7 idiomas: `astro-site/src/components/GoogleTag.astro` y
  `CookieConsent.astro`, montados en `BaseLayout.astro`. El bloque de
  consentimiento va **síncrono y ANTES** del loader async de gtag.js; invertirlo
  sembraría cookies publicitarias antes de leer el default denegado.
- **La decisión de consentimiento va en COOKIE sobre `.aichef.pro`, no en
  `localStorage`**, que está aislado por origen: lo aceptado en `aichef.pro` no
  se leería en `app.aichef.pro` y el visitante llegaría a Pickaxe como si no
  hubiera decidido nada, justo donde se mide la conversión.
- **La conversión se mide en Pickaxe, no aquí.** `app.aichef.pro` es Pickaxe
  whitelabeleado (sobre Vercel). El alta es un **modal**: NO existe «confirmation
  page» en el registro gratuito, así que el evento va en el campo **Body** del
  workspace. Y `?success=login` **no distingue registro de login** — lo que sí lo
  distingue es que el modal de alta es el único con **dos campos de contraseña**.
- No hace falta cross-domain linker: `aichef.pro` y `app.aichef.pro` comparten
  dominio registrable, así que `_gcl_aw` viaja sola.
- Docs: `GOOGLE_ADS_PICKAXE.md` (instalación) y `GOOGLE_ADS_GESTION.md` (gestión,
  qué NO tocar, y cómo montar un MCC para las otras marcas del grupo).
- ⚠️ **Antes de dar por buena cualquier campaña**: Objetivos → Conversiones →
  Resumen, y mirar el *Estado* de las acciones **principales**. La de aichef.pro
  llevaba tiempo optimizando hacia una **inactiva con 0,00 conversiones**.

### Analítica: DataFast en todo el sitio (desde 2026-09-20)

- `components/DataFast.astro`, montado en `BaseLayout.astro` **después** de `<GoogleTag />`
  (lee la cookie `aichef_consent` que ese componente publica). Panel: datafa.st, sitio
  `aichef.pro`, id `dfid_QU6VBDPW3GqyxYmZoQvw0`. miselup.pro lleva el snippet plano.
- **Modo HÍBRIDO, no el snippet plano de la guía**: el script estándar siembra dos cookies
  propias al cargar y el banner promete cookies de analítica solo tras «Aceptar». Sin
  decisión o rechazado carga `script.cookieless.js` (identificador diario, sin cookies);
  aceptado carga `script.js` (recurrentes y atribución multi-toque). La API mezcla los dos
  sin problema (flag `cookieless` por evento). La decisión se lee al cargar la página: quien
  acepta sigue cookieless hasta la siguiente navegación. `MODO` en el componente cambia a
  `cookies` o `cookieless` puro.
- Solo se activa bajo `aichef.pro`: previews y staging no ensucian el panel.
- **Se inyecta de inmediato desde el `<head>`, no en `DOMContentLoaded`**: la atribución de los
  Payment Links depende de que DataFast lea `?session_id=cs_…` en la página `-access` y lo envíe
  (XHR sin `keepalive`) ANTES de que `ProductAccessGate` navegue al dashboard tras verificar. El
  script espera al DOM por su cuenta para lo que lo necesita.
- **Proxy por dominio propio (contra bloqueadores) NO activado.** Antes de activarlo hay
  que demostrar que el proxy de Netlify reenvía la IP real: en modo cookieless el
  identificador sale de la IP, y sin ella todos los visitantes del día se funden en uno.
- Gate: `python3 scripts/astro-migration/datafast-gate.py [--base <preview>]` — cargador
  exactamente una vez en 17 páginas de muestra + los dos scripts descargables. Correrlo al
  tocar `BaseLayout`.
- **Pickaxe (los 7 subdominios `app`, `enapp`, `frapp`, `deapp`, `itapp`, `ptapp`, `nlapp`) también lo
  llevan desde el 20-sep**: snippet autocontenido (misma lógica híbrida leyendo la cookie `aichef_consent`)
  pegado en `Settings → Deploy → Workspace Level Custom code → Header` de cada workspace, con
  `data-domain="aichef.pro"` para que caigan en el mismo panel. Al pegar por automatización: el editor es
  CodeMirror 6 en un mundo aislado (no hay `cmView`), se inserta con un `paste` sintético sobre `.cm-content`
  enfocado, y **el clic en «Save Settings» tiene que ir unos segundos DESPUÉS del pegado y verificarse
  recargando** (4 guardados inmediatos se perdieron sin aviso). `ctrl+End` no mueve el cursor en ese
  editor: el snippet quedó al principio del Header, que funciona igual. Sus suscripciones NO se atribuyen
  por visitante (Pickaxe devuelve a `?success=login`, sin `session_id`); aparecen como ingresos de Stripe
  sin canal. Atribución de Payment Links (productos): ya cumplida por el flujo `-access?session_id=`.

### El widget de WhatsApp lo pinta el LAYOUT, no cada página (2026-09-03)

John lo cazó a ojo: estaba en las home y en poco más. Medido sobre el `dist`:
**655 de 1.312 páginas**. Faltaba en el **blog entero** (ES + EN), `/precios`,
`/contacto`, el hub de librerías, los legales y los **44 gates de acceso** — o
sea, justo donde llega el tráfico de SEO. No fallaba nada: cada página lo
montaba **a mano** y a nadie se le ocurrió que faltase.

Ahora lo pinta `BaseLayout.astro` para todo el sitio. Lo que hay que saber antes
de tocarlo es que **existen TRES implementaciones del mismo botón** y por eso el
riesgo al centralizarlo no era la falta, era el **duplicado**:

| Implementación | Dónde | Por qué es distinta |
|---|---|---|
| `components/WhatsAppFloatingButton.astro` | **global, en `BaseLayout`** | `aria-label` del i18n (7 idiomas), `bottom-6` |
| `<a>` inline en las 7 plantillas de landing | 45 landings de producto | mensaje **prerellenado** de soporte + `bottom-20` en móvil para no quedar debajo de su barra sticky |
| `WhatsAppProductSupport` (React) | 44 dashboards `-library` | va dentro de un island `client:only`, **no está en el HTML** |

Esas 89 páginas pasan **`whatsapp={false}`** a `BaseLayout` o saldrían **dos
botones superpuestos**, con doble animación y sin un solo aviso en el build.
La plantilla de `fase5-generate-zona-app.py` ya lo emite (los `-library` son
generados: editar el generador, no el fichero).

**Y el banner de cookies lo tapaba.** Es `fixed bottom-0` a lo ancho con
z-index 100, así que en la primera visita se comía el botón de la esquina — en
todo el sitio, no sólo donde acababa de aparecer. `CookieConsent.astro` publica
su **altura real** en `--aichef-cookie-h` (medida, no un número fijo: ~90 px en
escritorio, ~190 px en móvil, y cambia con el idioma), marca `<html>` con
`aichef-cookies-abierto` mientras se ve, y `global.css` aparta **todos** los
flotantes de WhatsApp con `margin-bottom`. Se desplaza en vez de reescribir
`bottom` porque las tres variantes tienen anclajes distintos y un desplazamiento
relativo respeta el de cada una.

**⚠️ El primer intento usaba `transform` y salió a producción temblando.** John
lo vio en el móvil: el botón se movía unos píxeles arriba y abajo en cada gesto
de scroll. Dos causas sumadas, y las dos enseñan algo:

- **Un `transform` sobre un `position: fixed` lo promociona a capa compuesta** y
  el móvil deja de pintarlo con el scroll asíncrono: va a la zaga del viewport.
  `margin-bottom` consigue el mismo desplazamiento —en un elemento posicionado
  `bottom` se mide al borde del MARGEN— sin tocar la capa.
- **Y estaba aplicado siempre**, con `transition`, aunque no hubiera banner: cada
  micro-reflow se convertía en una animación de 0,25 s. Ahora la regla vive bajo
  `html.aichef-cookies-abierto`, sin transición, y el publicador de la altura
  **ignora los cambios de menos de 4 px** (los que provoca la barra de
  direcciones del móvil al contraerse). Sin banner, el botón no recibe ni una
  propiedad: `transform: none`, `transition-duration: 0s`.

Regla que queda: **para apartar un `fixed` de otro elemento, margen antes que
`transform`**, y no dejar puesta una propiedad de composición cuando la
condición que la justifica (aquí, un banner que se ve 5 segundos) ya no se da.
Verificado con 12 reflows de ±1 px simulados: cero movimientos del botón.

**Gate: `python3 scripts/astro-migration/whatsapp-gate.py`** — exige exactamente
1 botón flotante por página del `dist` y que las únicas 44 sin él sean los
dashboards. Correrlo al tocar el layout, las landings o la zona app. Probado
contra 4 defectos inyectados a mano: los caza los 4 (uno de ellos sólo tras
arreglar que `fr.html` se leía como española — con `build.format: 'file'` la
portada de cada idioma **no** es `fr/index.html`).

### Tarjeta lateral de Miselup en landing + dashboard de cada producto (19-sep-2026, PR #82)

John pidió su snippet (HTML/CSS/JS) «en la landing pública y en la página privada de dashboard de cada
producto». Vive en `components/MiselupSideCard.astro` y **la monta `BaseLayout.astro` solo**, con el
registro `PRODUCTOS_ZONA_APP` (`lib/zona-app.ts`): si la ruta actual es un `landingPath` → tarjeta con
`utm_content=landing`; si es un `libraryPath` → `utm_content=dashboard`; en cualquier otra página, nada.
Un producto nuevo la hereda al entrar en el registro. `miselup={true|false}` en `BaseLayout` fuerza.

- **`style` y `script` van `is:inline` dentro del componente**: BaseLayout lo importa en las ~1.300
  páginas y los `<style>/<script>` normales de Astro se recogen por IMPORT, no por render (misma trampa
  que `CryptoPayButton`). Sin `is:inline` el CSS/JS se colaría en todo el sitio.
- **Sin `transform` sobre el `position: fixed`** (regla del 3-sep tras el temblor del botón de WhatsApp):
  centrado con `top/bottom: 0` + márgenes auto + `height: fit-content`, y el repliegue es un `right`
  negativo animado. El corte móvil es **767 px** (el `md` del sitio), no los 640 del snippet: entre 641 y
  767 se abría sola en modo escritorio sobre la barra sticky de compra.
- No se auto-abre en el dashboard (tapaba la rejilla de descargas) ni con menos de 560 px de alto;
  `.ms-body` queda `visibility: hidden` al replegarse (si no, el ✕ y el CTA eran paradas de tabulación
  fuera de pantalla). Snippet de John intacto en lo visual; mejoras documentadas en la cabecera.
- **Gate: `python3 scripts/astro-migration/miselup-gate.py [--base <preview>]`** — 96 páginas con la
  tarjeta exactamente una vez (por `utm_content` de su colocación) y 13 páginas ajenas con CERO firma
  del componente. Mide la FIRMA (`id="miselup-card"`, `miselupCardDismissed`, el CTA), **no la palabra
  «miselup»**: 25 posts del blog la llevan en el bloque congelado «CHEFBUSINESS GROUP».
- El `-library` sin JWT redirige a la landing: el dashboard se verifica por HTML (gate), no a ojo.

### Integraciones / conectores (Fase 12, 2026-09-05)

Los agentes ganaron razonamiento avanzado, **artefactos** (Copilot) y **conexión con
plataformas externas vía Composio**. Se construyó `/integraciones` en los 7 idiomas,
una sección en las 7 portadas, el enlace en la navegación y el post del blog en los
6 idiomas con blog. Piezas: `fase12-integraciones.py` (genera las 7 landings desde
`fase12-copy/*.json`), `fase12-traducir-copy.py`, `fase12-post-*.py`,
`components/IntegracionesPage.astro`, `IntegracionesShowcase.astro`, `BrandIcon.astro`
y `data/integraciones.ts`.

- **Son 16 plataformas + Composio, no 17.** Composio no es una herramienta del
  usuario: es el hub que gestiona la autorización de las otras. Contarlo dentro
  infla la cifra y confunde lo que se vende.
- **Un enlace de navegación nuevo hay que ponerlo en CUATRO ficheros.**
  `Header.astro` y `Footer.astro` **no bastan**: las landings de marketing generadas
  (Fase 6) montan los gemelos de React `src/components/ModernHeader.tsx` y
  `ModernFooter.tsx`. Con sólo los `.astro`, el enlace falta en media web.
- **Outlook, Canva, LinkedIn y Composio NO están en Simple Icons** (retirados a
  petición de las marcas) y la API de Composio pide clave. Se pintan como tesela con
  la inicial y el color oficial. **Notion, TikTok y X son negros**: sin color alterno
  desaparecen en modo oscuro.
- **El tratamiento al lector cambia por idioma y hay que imponerlo.** Medido sobre
  `src/i18n/locales/*.json`: **es tú · fr vous · de Sie · it tu · pt você · nl u**.
  La primera traducción francesa vino tuteando. El pipeline lleva la instrucción
  **y un gate que la verifica sobre el resultado**, porque el modelo la ignora a veces.

**Tres modos de fallo del traductor, cada uno con su gate (todos vistos ese día):**

| Fallo | Qué pasó | Gate |
|---|---|---|
| El alemán rompe el JSON | Cierra comillas con `„ … "` y emite el cierre como comilla RECTA, que termina la cadena. Falló con los DOS motores aun pidiéndoselo | `repara_comillas()`: escapa las comillas sueltas dentro de los valores |
| Sobra contenido, no falta | El francés devolvió el artículo **tres veces** y pasaba todo, porque los gates sólo miraban que no faltara nada | Nº de H2 **igual** al español, palabras en [0,6×, 1,5×], sin párrafos repetidos |
| DeepSeek se atasca | 40 minutos sin devolver nada donde Sonnet resolvió el artículo en cinco | Timeout corto (420 s) en el primer motor y caída a `anthropic/claude-sonnet-4.6` |

- **Los banners de producto van sólo en ES y EN.** `products-catalog.ts` sólo tiene
  nombre y descripción en esos idiomas, y los 49 posts de los blogs FR/DE/IT/PT
  tienen **cero** banners. Un banner en francés manda a un checkout en español.
- **`bridge.py` escribió el post ES con `--model anthropic/claude-sonnet-4.6`**, no
  con DeepSeek: el brief lleva una tabla de 16 filas con ejemplos a medida y es
  justo el tipo de prompt donde el motor de razonamiento se cuelga.
- ⚠️ **Revisar SIEMPRE las cifras de plan que invente el modelo.** El borrador del
  post decía «incluido el plan gratuito» y **en la web ya no hay plan gratuito**
  (el Miembro son 10 €/mes). Habría salido publicado.
