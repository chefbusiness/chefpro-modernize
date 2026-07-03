# REPLICAR Y SUSTITUIR PICKAXE

> **Estado: VISIÓN REGISTRADA — fase final del plan maestro (Fase 9), arranca al terminar la migración Astro.**
> Decisión de John, 2026-07-03: "Pickaxe ha cumplido su función… pero a día de hoy me representa una limitante. Quiero una versión de AI Chef Pro que mire a los próximos cinco años."
> Este documento se itera ANTES de escribir código: primero madurar la idea y valorar la mejor implementación.

---

## 1. Por qué (catálogo de limitaciones VIVIDAS, con evidencia)

1. **Dependencia ciega en revenue**: el incidente 2026-05-18→27 — un deploy de Pickaxe rompió `/pricing` y el checkout Stripe **9 días sin avisar**; lo descubrimos por el email de un cliente. Cero control, cero observabilidad.
2. **Palancas de pricing acopladas** (sesión 2026-07-03): el "Your Rate" global precia los top-ups (€↔créditos) sin poder fijar el bonus como cifra independiente; los créditos comprados **no caducan** y no se pueden restringir a suscriptores; no hay grandfathering fino.
3. **5 workspaces separados por idioma** (ES/EN/IT/FR/DE): cada cambio (rate, límites, banners, copy) se repite ×5 a mano. Una app propia multi-idioma mata esta multiplicación.
4. **Sin API/webhooks/eventos hacia fuera**: no podemos automatizar (CRM, email lifecycle por comportamiento, analytics de producto, alertas de churn). El "Buy More credits" no dispara nada que podamos escuchar.
5. **Personalización limitada**: sanitiza `<script>` (los banners promo se hacen con hacks CSS `:target`), branding/UX encorsetados, SEO del subdominio app fuera de nuestro control.
6. **Techo funcional**: sin MCP, sin tool-use/actions propias, sin memoria de usuario controlada por nosotros, sin elegir modelo por agente ni router multi-modelo.

## 2. Qué construiríamos (north star)

**`app.aichef.pro` propia** (una sola app multi-idioma, 7 lenguas — adiós a los 5 workspaces):

- **Chat estilo ChatGPT** con biblioteca de 55+ agentes gastronómicos — los **prompts de sistema son nuestros** y se migran tal cual (son el alma del producto y ya existen).
- **Runtime de agentes**: tool-use/actions (function calling), **MCP**, APIs externas, webhooks, generación de imagen al final del flujo (patrón actual), export CSV/PDF/Word.
- **Créditos y planes propios**: medición = coste real × margen (ya entendemos el modelo de Pickaxe: consumo ~coste, precio con prima); Stripe directo — **ventaja enorme: las suscripciones YA viven en nuestro Stripe** (el checkout factura a nombre de John), no hay migración de billing desde un tercero.
- **Palancas que Pickaxe no da**: caducidad de bonus, top-ups solo-suscriptores, trials flexibles, grandfathering, precios por mercado.
- **Datos**: analytics de uso por agente/usuario, eventos → email lifecycle (Listmonk/Resend ya operativos), memoria de usuario propia.

## 3. Activos que ya tenemos (por qué es factible)

- Prompts de los 55+ agentes (exportables de Pickaxe) · base de usuarios/emails · **Stripe propio con las suscripciones activas** · experiencia probada en JWT + Netlify functions + Resend (33 productos digitales LIVE) · bridge.py/OpenRouter (router multi-modelo en producción) · skills insforge en el entorno (backend con auth/DB/storage/pagos si se valora) · el frontend público en Astro (Fase 0-8) ya separado de la app.

## 4. Decisiones a iterar (NO decididas — valorar en su momento)

| Tema | Opciones sobre la mesa |
|---|---|
| Hosting app | **Vercel** (preferencia inicial de John, amigable para apps IA) vs Netlify (unificar con lo existente) |
| Framework | Next.js + Vercel AI SDK vs alternativas; SDK de agentes (Claude Agent SDK) para el runtime |
| Modelos | Router multi-modelo (OpenRouter, como bridge.py) vs proveedor único; elegir modelo por agente según coste/calidad |
| Backend | Supabase / InsForge / propio sobre Netlify-Vercel functions — auth, DB, memoria, colas |
| Créditos | Réplica del modelo actual (coste real × prima) con las palancas nuevas de §2 |
| Migración usuarios | Export Pickaxe → import con reset de contraseña vs magic links; periodo de doble plataforma |

## 5. Fases (cuando arranque, post-Astro)

- **9.0 Discovery**: exportar e inventariar los prompts + mapear planes/usuarios/Stripe + spec funcional de paridad (qué hace hoy Pickaxe que NO podemos perder).
- **9.1 Prototipo**: 1 agente end-to-end (chat + créditos + 1 action) en el stack candidato.
- **9.2 MVP**: multi-agente + planes/créditos completos + i18n.
- **9.3 Beta paralela**: doble plataforma, usuarios voluntarios, comparar coste/calidad por agente.
- **9.4 Migración + cutover** de `app.aichef.pro` y variantes de idioma.
- **9.5 Apagar Pickaxe.**

## 6. Regla de oro mientras tanto

Hasta que esto arranque, **Pickaxe sigue siendo producción**: se mantiene, se monitoriza (pendiente: monitor pasivo del checkout con curl semanal) y NO se le añaden dependencias nuevas difíciles de replicar.
