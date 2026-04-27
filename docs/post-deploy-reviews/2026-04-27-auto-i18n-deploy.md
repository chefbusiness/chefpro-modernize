# Auto-i18n + plataforma alemana — Deploy 2026-04-27

Registro completo del despliegue de auto-detección de idioma y routing a la plataforma alemana `deapp.aichef.pro`.

## Commits desplegados a `main`

| Commit | Cambio |
|---|---|
| `cd3a92f` | German platform routing — `getAppUrl()` mapea `de` → `deapp.aichef.pro` |
| `943ded6` | Preconnect/dns-prefetch para `deapp/frapp/itapp.aichef.pro` |
| `1a07ea9` | Edge Function `lang-redirect.ts` (auto-detección + redirect 302 desde `/`) |
| `ade578c` | Fix: cookie con idioma ≠ `es` también dispara redirect |

## Arquitectura de la auto-detección

### Lógica de prioridad (en orden)
1. **URL prefijada** (`/en`, `/de`, `/fr`, `/it`, `/pt`, `/nl`) — pasa transparente, no se toca
2. **Cookie `preferred-lang`** — usuario ya eligió manualmente, manda
3. **Header `Accept-Language`** — primer match con idioma soportado
4. **Geo-IP** del país (`context.geo.country.code` de Netlify)
5. **Default `en`** — para países no mapeados (NO español)

### Edge Function: `netlify/edge-functions/lang-redirect.ts`
- Solo se dispara en `path === "/"` (path exacto, no `/*`)
- Bots excluidos por regex en User-Agent: `bot|crawler|spider|googlebot|bingbot|baiduspider|yandex|duckduckbot|facebookexternalhit|twitterbot|linkedinbot|whatsapp|slackbot|telegrambot|applebot|chrome-lighthouse|ahrefsbot|semrushbot|mj12bot|petalbot`
- 302 (no 301) → Google no lo trata como canónico permanente
- Headers `Vary: Accept-Language, Cookie` y `Cache-Control: private, no-cache, no-store, must-revalidate`
- Escape hatch: `?nolang=1` salta toda la lógica
- Registrada en `netlify.toml` ANTES de `og-meta` para que se ejecute primero

### Mapeo país → idioma
| Idioma | Países |
|---|---|
| `es` | ES, MX, AR, CO, PE, CL, VE, UY, EC, BO, PY, CR, GT, HN, NI, PA, SV, DO, CU, PR |
| `en` | US, GB, CA, AU, NZ, IE, IN, ZA, SG, PH, MY, NG, KE |
| `fr` | FR, MC, LU, SN, CI |
| `de` | DE, AT, LI |
| `it` | IT, SM, VA |
| `pt` | PT, BR, AO, MZ, CV |
| `nl` | NL |

CH (Suiza) deliberadamente NO mapeada — es trilingüe (de/fr/it). Cae al fallback `en`. Si los datos GSC muestran tráfico CH significativo, considerar mapearlo a `de` (mayoritario en CH).

### Cookie persistente
Escrita por `src/hooks/useLanguage.ts:persistLangCookie()` en dos momentos:
1. Al aterrizar en una URL con prefijo de idioma (`/de/...`, `/en/...`)
2. Al cambiar de idioma vía selector

Formato: `preferred-lang=<lang>; path=/; max-age=31536000; SameSite=Lax`

## Auditoría confirmada en producción (2026-04-27)

### Rutas existentes (no roto)
12/12 rutas devuelven 200: `/pricing`, `/de`, `/en`, `/fr`, `/it`, `/pt`, `/nl`, `/productos-digitales`, `/kit-plan-financiero`, `/guia-dark-kitchen`, `/de/pricing`, `/de/productos-digitales`.

### Redirects por Accept-Language
| AL | Resultado |
|---|---|
| `es-ES` | 200 (queda en `/`) ✅ |
| `en-US` | 302 → `/en` ✅ |
| `de-DE` | 302 → `/de` ✅ |
| `fr-FR` | 302 → `/fr` ✅ |
| `it-IT` | 302 → `/it` ✅ |
| `pt-BR` | 302 → `/pt` ✅ |
| `nl-NL` | 302 → `/nl` ✅ |

### Bots respetados (NO redirigidos)
Googlebot, Bingbot, facebookexternalhit, Twitterbot, AhrefsBot, WhatsApp, LinkedInBot, Slackbot, Applebot → todos 200 en `/` con `Accept-Language: de-DE`. SEO indexado intacto.

### Cookie behavior
| Cookie | AL | Resultado |
|---|---|---|
| `de` | `en` | 302 → `/de` (cookie manda) ✅ |
| `fr` | `de` | 302 → `/fr` (cookie manda) ✅ |
| `es` | `de` | 200 (cookie es respeta) ✅ |
| `zz` (inválida) | `en` | 302 → `/en` (fallthrough a AL) ✅ |
| (sin cookie) | `en` | 302 → `/en` ✅ |

### Bundle JS de producción
Verificado que contiene: `deapp.aichef.pro`, `enapp.aichef.pro`, `frapp.aichef.pro`, `itapp.aichef.pro`, `app.aichef.pro`, `preferred-lang=`, mapeo `c==="de"?"https://deapp.aichef.pro"`.

## Gap conocido — Hreflang

NO hay tags `<link rel="alternate" hreflang="..."/>` en el `<head>` de las páginas. Esto NO bloqueó el deploy:
- El redirect es 302 (no 301) → Google no lo trata como redirección permanente
- `Vary: Accept-Language, Cookie` indica al CDN/Google que la URL responde con contenido distinto según headers
- `/`, `/en`, `/de`, etc. tienen URL canónica estable

Pero hreflang ayudaría a Google a entender la relación entre las versiones idiomáticas y mejorar la asignación de impresiones por país. **Decisión**: esperar 14 días y revisar Search Console antes de implementar. Si las impresiones se distribuyen mal, implementar.

## Routine de revisión T+14d

**ID**: `trig_01QJkegrTdV6ed3rj1bQuZnM`
**Ejecuta**: 2026-05-11T09:00:00Z (11:00 Europe/Madrid)
**Tipo**: One-time
**URL**: https://claude.ai/code/routines/trig_01QJkegrTdV6ed3rj1bQuZnM

### Plan del agente remoto
1. Verificar edge function vía curl (5 escenarios de Accept-Language + bot test)
2. Descargar bundle JS y verificar que contiene la lógica
3. `git log ade578c..HEAD` en archivos críticos (detección de reverts)
4. GSC vía MCP `gscServer` si está disponible (local-only stdio MCP, probablemente NO disponible en runtime remoto → degradación graceful)
5. Generar `docs/post-deploy-reviews/2026-05-11-auto-i18n-seo-review.md` y abrir PR
6. Escalación con label `urgent` si:
   - Googlebot recibe 302 en `/` (regex de bots fallaría)
   - Caída >15% impresiones en `/` para país ES
   - Caída global >10% impresiones aichef.pro

### Limitaciones conocidas del agente remoto
- `gscServer` MCP es stdio local (`/Users/johnguerrero/mcp-gsc/.venv/bin/python`) — NO accesible desde Anthropic Cloud. El agente lo intentará invocar y dejará nota si no responde.
- Conectores claude.ai disponibles: solo `Google-Drive` y `Canva` (no GSC ni GitHub App).
- GitHub: el agente usará el git checkout que la routine le da; PR creation depende de credenciales en runtime.

## Hipótesis del impacto esperado

- **Reducción del rebote internacional**: usuarios de US/DE/FR/IT que caían en página en español ahora aterrizan directos en su idioma
- **Mejor first-impression**: el CTA "Probar gratis" ahora apunta a `enapp/deapp/frapp/itapp.aichef.pro` (plataformas localizadas) en lugar del default español
- **Mejora en conversión free→paid**: hipótesis de John — usuarios entienden mejor el SaaS si lo ven en su idioma desde el primer click
- **Riesgo SEO controlado**: bots quedan en español canónico, redirect es 302+Vary, cada idioma sigue siendo indexable en su URL prefijada

## Cómo invocar la routine antes del T+14d (si es necesario)

```bash
# Listar todas las routines
RemoteTrigger action=list

# Ejecutar la review YA
RemoteTrigger action=run trigger_id=trig_01QJkegrTdV6ed3rj1bQuZnM

# Ver detalles
RemoteTrigger action=get trigger_id=trig_01QJkegrTdV6ed3rj1bQuZnM
```
