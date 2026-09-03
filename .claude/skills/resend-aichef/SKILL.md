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
