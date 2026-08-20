# Handoff — 2026-08-20 · Productos digitales: eBook Pro Prompts verificado + punto ciego del gate cerrado

> Sesión corta en el Mac (Fable, ultracode). Disparador: John avisa de una compra nueva del
> **eBook Gastro Pro Prompts** y pide revisarla **antes** de que el cliente escriba por WhatsApp,
> como pasó con el del Kit de Tareas Pastelería.
> **Estado del repo al cerrar:** `main` = `1b531de` (pusheado, limpio).
> ⚠️ **Hay otra sesión viva en el VPS** sobre este mismo repo, enfocada en **traducciones/i18n,
> blog DE/PT y SEO**. Empuja a `main` a menudo → **rebasar siempre antes de pushear** y no tocar
> `astro-site/src/content/blog/**`, `src/i18n/**` ni los locales.

## 1. El eBook está OK — el cliente puede descargar

Verificado eslabón por eslabón (no valía el gate; ver §2):

| Eslabón | Estado |
|---|---|
| Landing `/pro-prompts-ebook` | 200, con enlace `buy.stripe.com`, sin `#comprar` |
| Gate `/pro-prompts-library-access` | 200, island `client="only"` hidrata |
| Dashboard `/pro-prompts-library` | 200, island hidrata |
| `verify-purchase` | vivo (403 correcto con JWT falso) |
| `PDF_EBOOK_URL` → `/dl/pp-7e48…pdf` | 200 · `application/pdf` · 853.223 B == disco |
| `PDF_BONUS1_URL` → `/dl/b1-7e48…docx` | 200 · docx · 11.829 B == disco |
| `PDF_BONUS23_URL` → `/dl/b23-7e48…xlsx` | 200 · xlsx · 13.672 B == disco |
| Los 3 ficheros | en `astro-site/public/dl/` **y** trackeados en git |
| Cadena JWT | `AccessGate` escribe `pro-prompts-jwt` → `useAuth()` (mismo default) → `DownloadsSection` pide con Bearer → 3 botones |

Las 3 env vars están en el site `ee5802cf-…` con scope `functions`, que es el que necesitan.
Kit Pastelería re-verificado de paso: **11/11 verde**.

## 2. Bug del gate corregido (`1b531de`) — daba verde sin verificar nada

**`pro-prompts-ebook` es el ÚNICO de los 44 productos cuyas descargas no salen de
`PRODUCT_FILES`**: `netlify/functions/get-download-urls.ts:773-782` tiene una rama especial que
las lee de `PDF_EBOOK_URL` / `PDF_BONUS1_URL` / `PDF_BONUS23_URL`. El gate lo excluía de los
checks de ficheros y de tarjetas y lo imprimía como `files=0 cards=- dl_ok=- · 0 issues`: **verde
habiendo comprobado cero entregables de un producto que se vende.** Si esas env vars
desaparecieran del site, el dashboard mostraría «No disponible» en los 3 botones y el gate
seguiría en verde.

Ahora `gate-flujo-postpago.py`:
- resuelve las 3 env vars del site vía `netlify api getEnvVars`, las convierte a rutas `/dl/…` y
  las pasa por la **misma** maquinaria que el resto (disco + git + LIVE 200 con content-type
  binario y `Content-Length` == disco);
- cruza las 3 tarjetas fijas de `src/components/library/DownloadsSection.tsx` (`ebook`,
  `bonus1`, `bonus23`);
- en `--offline` no puede leerlas → lo dice con un **aviso** (canal `warns` nuevo, **no** cuenta
  como fallo), en vez de callárselo. El paso «offline → 0 fallos → merge» del workflow sigue OK;
- site/cuenta configurables con `AICP_SITE_ID` / `AICP_NETLIFY_ACCOUNT`.

**LIVE de referencia: 44 productos · 637 entregables · 0 fallos** (eran 634; +3 del eBook).
Test negativo apuntando al site de staging (sin esas env vars): falla con las 2 incidencias
correctas. `--offline`: 0 fallos · 1 aviso · exit 0.

> Gotcha del `--only`: el filtro es **igualdad exacta** de `productId`.
> `--only pro-prompts` devuelve 0 productos; es `--only pro-prompts-ebook`.

## 3. 🔴 La causa real de «no tengo ningún enlace» (aplica a TODOS los productos)

**No hay webhook de Stripe.** `verify-purchase.ts` llama a `sendAccessEmail()` **sólo cuando el
cliente aterriza en la página `-access` con `?session_id=…`** después de pagar. Si cerró la
pestaña de Stripe al ver «pago completado», o si el Payment Link no tiene bien configurada la URL
de confirmación, **no se envía nada y no queda rastro**: pagó y para el sistema no ha pasado nada.

Es exactamente lo que le ocurrió al cliente del Kit Pastelería del 16-ago, y le puede volver a
pasar a cualquiera mientras no haya webhook. Ya estaba anotado como pendiente en el handoff del
18-ago §5; ahora está confirmado como **la** explicación por defecto.

### Cómo devolverle el acceso a un cliente (3 vías)

1. **`https://aichef.pro/admin/generar-acceso`** (verificada LIVE: 200 + island hidrata) —
   contraseña = env var `ADMIN_PASSWORD` del site. Email + desplegable de los 44 productos +
   casilla «enviar email» (marcada por defecto). Devuelve el magic link en pantalla con botón de
   copiar, para pegarlo por WhatsApp. **JWT de 365 días** (`admin-generate-access.ts:84`).
2. **Autoservicio del cliente**: formulario «¿Ya compraste…?» al pie de cada landing
   (`data-ab-form`) → `resend-access` busca su compra en Stripe y le reenvía el enlace.
   Verificado vivo en `/pro-prompts-ebook` y `/kit-tareas-pasteleria`.
3. **CLI** si Netlify se cayera: `node scripts/generate-access-link.mjs <email> <product-id>`
   (necesita `JWT_SECRET` en un `.env` local; **no está** en el repo).

⚠️ **Ojo con los tres homónimos del desplegable**: `Kit Tareas Pastelería` ≠ `Kit Tareas
Panadería / Obrador` ≠ `Guía Panadería con Obrador`. Equivocarse acuña el JWT del producto que no
es y el cliente abre un dashboard ajeno.

## 4. Pendiente / decisiones de John

1. **Stripe: la URL de confirmación de los 44 Payment Links.** Es la pieza que decide si el
   cliente llega solo al gate, y **no está en el repo** sino en el panel de Stripe. El CLI del Mac
   (`/usr/local/bin/stripe`) está logueado en la cuenta de **Miselup**,
   no en la de AI Chef Pro → desde aquí no se alcanza. Con
   `stripe login --project-name aichefpro` se pueden revisar los 44 de una tacada y sacar las
   sesiones de los dos clientes (16-ago pastelería y el del eBook) para confirmar qué compró cada
   uno.
2. **Webhook de Stripe** (§3): mata la clase entera de incidencias.
3. **Seguridad — `resend-access` no valida QUÉ compró.** Encuentra cualquier sesión pagada de ese
   email y acuña el JWT del producto que le pidan: quien compre el eBook de 9 € puede pedirse el
   enlace de la guía de 85 €. Mismo hueco en `verify-purchase` (no cruza la sesión con el
   producto). No es urgente, pero está abierto.
4. Sigue pendiente todo lo del handoff del 18-ago: **Kit Pastelería v2.0** (4 plantillas nuevas,
   SPEC + workflow listos), JSON-LD de reseñas, ancla de precio €39/−69 %, barrido de la bio.

## 5. Memoria actualizada

- `reference_entrega-postpago-y-recuperar-acceso.md` — **nuevo**: el porqué del cliente sin enlace
  + las 3 vías de recuperación + los dos avisos (homónimos, `resend-access` sin validar producto).
- `reference_gates-productos-digitales-e-inject-cache.md` — añadida la rama de env vars del eBook
  y el nuevo baseline 44/637.
