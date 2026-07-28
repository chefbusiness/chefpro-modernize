# HANDOFF — Email Campaigns AI Chef Pro (Listmonk + Resend)

**Fecha del handoff:** 2026-04-14, ~18:45
**Estado:** Campaña 01 (Kit de Escandallos Pro) enviándose en este momento.

---

## Contexto rápido

- **Stack:** Listmonk self-hosted en VPS Hostinger `http://46.202.175.14:32773/admin` + Resend como SMTP provider verificado en `contact.aichef.pro`.
- **Resend:** cuenta **Pro de pago** — **50.000 emails/mes** y **10 req/seg** de rate limit. (NO es Free. No volver a dar instrucciones conservadoras pensando en Free.)
- **Remitente por defecto:** `AI Chef Pro <info@contact.aichef.pro>`
- **Lista principal:** 3.216 suscriptores (profesionales de hostelería ES).
- **Es la primera campaña comercial desde hace meses** (MailerLite fue baneado). Subdominio `contact.aichef.pro` está frío — hay que calentar reputación sin disparar alarmas.

---

## Qué YA está hecho

### Archivos en este directorio (`chefpro-modernize/email-campaigns/`)
- `plantilla_maestra_aichefpro.html` — Plantilla reutilizable en Listmonk → Plantillas. Header negro con logo blanco real de AI Chef Pro, banda amarilla, catalog card, footer con unsubscribe + MessageURL.
- `campana_01_kit_escandallos.html` — Contenido de la campaña 01. Rediseñado tras 3 iteraciones (botón, badge Stripe, precio).
- `README_campana_01.md` — 3 opciones de asunto/preheader, pasos Listmonk, plan de warm-up.
- `HANDOFF.md` — este archivo.

### Commits en `chefpro-modernize` (rama `main`, ya pusheados a Netlify)
1. `a1f96bd` — `feat(email): campaña 01 Kit de Escandallos Pro + assets para Listmonk`
2. `aa720ec` — `fix(email): usar badge oficial Stripe powered-by-stripe.png en campaña 01`
3. `7954c14` — `fix(email): rediseñar precio + chip blanco bajo badge Stripe`

### Assets live en aichef.pro
Todos verificados con `curl` → 200 OK:
- `https://aichef.pro/og-kit-escandallos.jpg` (hero 1, 96KB, 1200×630)
- `https://aichef.pro/powered-by-stripe.png` (badge oficial, 17KB, 530×161, fondo blanco aplicado por el HTML)
- `https://aichef.pro/email-assets/aichef-pro-logo-white.png` (900×140, 23KB)
- `https://aichef.pro/email-assets/kit-escandallos-hero.jpg` (1088×608, 171KB)
- `https://aichef.pro/email-assets/money-back-30d.png` (240×240, 67KB)
- `https://aichef.pro/email-assets/john-guerrero.jpg` (160×160, 37KB)

(Los 5 PNGs sueltos de Visa/MC/Apple/Google/Stripe fueron eliminados en `aa720ec` — se usa el badge oficial `powered-by-stripe.png`.)

### Plantilla maestra y campaña 01 creadas en Listmonk
- Plantilla `AI Chef Pro — Maestra` en `/admin/campaigns/templates`.
- Campaña `01 · Kit de Escandallos Pro · 12€` creada y **enviándose en este momento** con asunto Opción A: `Kit de Escandallos Pro: 12€ esta semana (antes 49€)`.

---

## Qué pasó durante el primer envío (para contexto)

- Configuración inicial de Listmonk (Rendimiento): **Concurrencia 10 / Tasa 10 = ~100 msg/s**, masivamente por encima del límite de Resend.
- Resend devolvió `429 too many requests: You can only make 5 requests per second` a la mayoría de mensajes.
- Se pausó la campaña.
- Se corrigieron los ajustes (ver sección siguiente) y se reanudó.
- Al reanudar, Listmonk continuó desde donde se quedó (constraint único `campaign_subscriber`) — no hubo duplicados.

---

## PENDIENTE cuando retomemos

### 1. Verificar que la campaña terminó OK
- `/admin/campaigns` → campaña `01 · Kit de Escandallos Pro · 12€` → ver contador de **Vistas / Envíos / Clics / Rebotes**.
- Revisar `/admin/settings/logs` — no debería haber más `too many requests`.
- Anotar: % de aperturas, % de clics, rebotes duros, quejas.

### 2. Confirmar que los ajustes de rate limit se aplicaron
**Ajustes recomendados para Resend Pro (50k/mes, 10 req/s) — primera campaña:**

| Panel | Campo | Valor |
|---|---|---|
| **Configuraciones → Rendimiento** | Concurrencia | `2` |
| | Tasa de envío | `4` |
| | Tamaño del lote | `1000` |
| | Umbral de errores | `100` |
| | Habilitar límite de corrimiento de ventana | **ON** |
| | Mensajes máximos / duración | `400 / 60s` |
| **Configuraciones → Mensajeros (SMTP)** | Conexiones máximas | `2` |
| | Reintentos | `3` |
| | Tiempo máximo de espera | `5s` |

Efectivo: 2 × 4 = **8 msg/seg** (bajo el límite de 10/s de Resend Pro). 3.216 subs → ~7 min.

### 3. Rebotes — Listmonk ↔ Resend
**Estado actual:** `Configuraciones → Rebotes → Activar el procesamiento de rebotes` está **OFF**. Resend ya suprime bounces internamente, así que la reputación con Resend está cubierta, pero Listmonk no sabe qué suscriptores botaron y los seguirá enviando.

**Dos opciones para decidir cuando retomemos:**

- **Opción A (minimal):** Tras cada campaña, descargar de Resend Dashboard los `bounced`/`complained`, exportar a CSV y subirlo a Listmonk como `Lista de bloqueo`. Suficiente si enviamos 1 campaña/semana.

- **Opción B (automática):** Crear función Netlify en `chefpro-modernize` en `netlify/functions/resend-bounce-relay.ts` que:
    1. Recibe webhook de Resend (eventos `email.bounced`, `email.complained`).
    2. Traduce el payload al formato que espera `POST /webhooks/bounce` de Listmonk.
    3. Llama a Listmonk con header `Authorization: token <usuario>:<api_token>`.
  - Pasos previos en Listmonk: crear usuario tipo `API` (ej. `resend-bounces`) con rol que tenga `campaigns:manage` + `subscribers:manage`. Guardar el token que Listmonk muestra UNA vez.
  - Configurar webhook en Resend → Dashboard → Webhooks apuntando a `https://aichef.pro/.netlify/functions/resend-bounce-relay`.
  - ~40 líneas TypeScript, deployable en 1 commit.

**Mi recomendación:** Opción B si el plan es mandar >1 campaña/semana o hacer drips. Opción A si es puntual.

### 4. Roadmap de campañas futuras
- **Semana siguiente:** campaña 02. Candidatos más fuertes del catálogo de 27 productos digitales: Pack APPCC, Kit Plan Financiero, Kit Inventario, Kit Gestión de Personal, alguna de las Guías de cocinas del mundo (nikkei/japonés/peruano/mexicano).
- Reutilizar `plantilla_maestra_aichefpro.html` tal cual. Solo cambia el contenido (`campana_02_*.html`).
- Mantener la estructura: hero → dolor → imagen secundaria → bullets → CTA con precio stack + badge Stripe → garantía 30d → bridge herramienta gratis → firma autor.

### 5. Warm-up del subdominio (info para futuras decisiones)
- En la campaña 01 se envió a **los 3.216 de golpe** porque el usuario decidió no trocear.
- Si esta campaña tiene bounce rate < 3% y complaint rate < 0.1%, el subdominio está warm y podemos seguir mandando en tandas completas.
- Si hay más quejas, aplicar segmentación por engagement reciente (últimos 90 días) las siguientes 2-3 campañas.

---

## Comandos útiles para retomar

```bash
# Ver estado del git
cd /Users/johnguerrero/chefpro-modernize
git log --oneline -5

# Ver los 3 archivos de la campaña
ls -la email-campaigns/

# Verificar que los assets siguen vivos
for img in og-kit-escandallos.jpg powered-by-stripe.png email-assets/aichef-pro-logo-white.png email-assets/kit-escandallos-hero.jpg email-assets/money-back-30d.png email-assets/john-guerrero.jpg; do
  printf "%-50s " "$img"
  curl -so /dev/null -w "%{http_code}\n" "https://aichef.pro/$img"
done

# Abrir Listmonk
open "http://46.202.175.14:32773/admin/campaigns"
```

---

## Mensaje para retomar esta tarea

> Claude, retomamos la tarea del email marketing con Listmonk + Resend. El contexto completo está en `/Users/johnguerrero/chefpro-modernize/email-campaigns/HANDOFF.md`. Léelo primero entero y luego dime cómo quedaron las métricas de la campaña 01 (Kit de Escandallos Pro) — te paso capturas del panel de Listmonk. A partir de ahí, decidimos si avanzamos con la Opción B (función Netlify para bounces) o pasamos directamente a la campaña 02.
