---
name: resend-aichef
description: Valores LOCALES de AI Chef Pro para operar Resend (broadcasts, segmentos, remitente, dónde vive la credencial). Complementa la skill agnóstica del grupo `resend-operaciones-grupo`. Usar SIEMPRE que haya que enviar o programar un mailing de aichef.pro, dar de alta contactos o comprobar deliverability.
---

# Resend — valores de AI Chef Pro (skill local)

La cuenta de Resend es **una para todo el grupo** (ver `~/.claude/skills/resend-operaciones-grupo`).
Aquí solo lo concreto de esta marca.

## Credencial (no pedirla a John: ya existe en local)

Orden de resolución que usa `scripts/productos-digitales/emails/resend-broadcast.py`:

1. `RESEND_API_KEY` en el entorno.
2. `~/.config/resend/claude-code-local.key` (si alguna sesión la creó).
3. **`~/michelin-leads/.env` → `RESEND_API_KEY`** (la key de AI Chef que usan las sesiones de
   prospección; acceso completo verificado el 2026-09-04: dominios, segmentos y broadcasts).

También valen `~/chefbusiness-prospecting/.env` (`MISELUP_RESEND_API_KEY`) y
`~/timlup-pro/web/.env.local` (`RESEND_API_KEY`): misma cuenta. **Nunca imprimir ni commitear.**

## HTTP: curl, no urllib

El `python3` de este Mac falla el handshake TLS (`CERTIFICATE_VERIFY_FAILED`). Toda llamada a
`api.resend.com` va por `curl` (el script ya lo hace así).

## Valores de la marca

| Parámetro | Valor |
|---|---|
| Segmento «AI Chef Pro ES» | `b2c581bd-81db-4ded-a174-2b339f7d3cc3` |
| Segmento «AI Chef Pro EN» | `d06ed053-4327-4bec-9e3b-25a9ee9f6704` |
| From (marketing) | `AI Chef Pro <hola@news.aichef.pro>` (dominio `news.aichef.pro` verificado) |
| Reply-To | `info@aichef.pro` |
| Baja en el cuerpo | `{{{RESEND_UNSUBSCRIBE_URL}}}` (obligatorio en todo broadcast) |
| Estética | negro `#111111` + dorado `#FFD700`; nada de marrón/naranja (orden de John 2026-08-24) |
| Plantillas vivas | `scripts/productos-digitales/emails/*.html` |

## Programar un broadcast (API, sin panel)

```
python3 scripts/productos-digitales/emails/resend-broadcast.py \
  --html scripts/productos-digitales/emails/<fichero>.html \
  --subject "…" --name "…" \
  --scheduled-at 2026-09-04T08:00:00Z        # UTC; Madrid en verano = UTC+2
  [--test john@chefbusiness.co]              # prueba transaccional antes
  [--dry-run]
```

`POST /broadcasts` admite `segment_id`, `send: true` y `scheduled_at` (ISO 8601 o «in 1 hour»).
El script aborta si quedan tokens `__PAGINAS__`, si falta el bloque de baja, si algún enlace o
imagen `https://aichef.pro/…` no responde 200, o si la hora está en el pasado.

## Antes de cada envío

Revisar deliverability en resend.com/emails (bounces < 4 %, spam < 0,08 %) — memoria
`reference_resend` del proyecto de prospección.

## Cola de correos de producto (regla de John, 2026-09-05)

Por **cada producto actualizado de versión o creado** se programa un broadcast individual; la cola lleva **5 días entre
correos**. Procedimiento:

1. Hueco: `curl -s -H "Authorization: Bearer $KEY" https://api.resend.com/broadcasts` → el `scheduled_at` más tardío
   (o el último `sent_at`) **+ 5 días a las 08:00Z**. Nunca dos el mismo día. Ejemplo: Manual del Manager el 7-sep → Plan
   Bar-Restaurante 2.1 el 12-sep → siguiente el 17-sep…
2. HTML individual en `scripts/productos-digitales/emails/broadcast-<pid>-v<version>-es.html` (actualización: copiar
   `broadcast-kits-tareas-v2-es.html`; lanzamiento: `broadcast-manual-manager-lanzamiento-es.html`). Qué trae la versión
   sale del changelog del producto (`src/data/productos-changelog.ts`), en lenguaje de cliente; CTA a la landing con UTM
   `utm_source=email&utm_medium=broadcast&utm_content=<pid>-v<version>`; párrafo «¿Ya lo compraste?» con la página
   `-access`; bloque de baja `{{{RESEND_UNSUBSCRIBE_URL}}}`.
3. `resend-broadcast.py --html … --subject … --name "Actualización <producto> <versión> (ES)" --test john@chefbusiness.co`
   y, acto seguido, el mismo comando con `--scheduled-at <slot>`. El script bloquea si un enlace no responde 200.
4. Anotar el slot en el handoff de la sesión y en `CALENDARIO-V2-SEMANAL.md`.
