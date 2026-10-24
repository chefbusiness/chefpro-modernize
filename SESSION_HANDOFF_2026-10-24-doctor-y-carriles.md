# Handoff — 24-oct-2026 (sesión Claude Code, Mac) — /doctor y reparto de carriles entre sesiones

## ▶️ Para retomar (sesión nueva tras /clear)

- **Carriles desde hoy (John, 24-oct):** una sesión en **Cursor** lleva las landings comerciales, el SEO del sitio y los posts
  del blog. **Esta sesión (Claude Code, Mac en local)** lleva SOLO los **productos digitales** (`/productos-digitales`: hub,
  landings de producto, dashboards, entregables, pagos, correos) y su **traducción a otros idiomas, empezando por el inglés**.
  - No abrir trabajo de blog, SEO del sitio ni landings de marketing desde aquí.
  - Ficheros compartidos (`products-catalog.ts`, `Header`/`Footer` y sus gemelos React, `BaseLayout`, `llms.txt`): `git fetch`
    antes de tocarlos, commits pequeños y `git pull --rebase` antes de cada push.
- `origin/main` traía 13 PR del carril Cursor (#141-#155: glosario, comparativas, metadatos de agentes, 301 de `blog.aichef.pro`).
  Integrados al hacer este push; nada de este carril los toca.
- **Siguiente en este carril:** traducir al inglés el siguiente producto ES de la cola (tienda EN: 22 productos vivos; cola y
  huecos en `scripts/productos-digitales/CALENDARIO-V2-SEMANAL.md`, reglas en `scripts/productos-digitales/TIENDA-INTERNACIONAL.md`).
  Aparcado en ES: v2.1 de los 6 kits ES con las erratas de `checklists-kit/<v>/SPEC.md` §5/§6 (handoff del 18-oct).
- Routines de correo a vigilar con `RemoteTrigger list_runs` (lista completa en la memoria): la de hoy, 24-oct (Parrillero → 23-nov),
  y la de mañana, 25-oct (Mobile Bar EN → 24-nov).

## 1. /doctor (24-oct)

Ajustes de usuario, **fuera del repo** (copias en `~/.claude/settings.json.bak-doctor-2026-10-24` y `~/.claude.json.bak-doctor-2026-10-24`):

| Cambio | Dónde | Cómo deshacerlo |
|---|---|---|
| 21 skills apagadas: pack marketing (ai-seo, ch-seo-audit, cold-email, competitor-alternatives, copy-editing, pricing-strategy, programmatic-seo), pack SEO (seo-audit y 8 `seo-*`), impeccable, publish-blog, prune-posts, migrar-a-abacus, remotion-best-practices | `skillOverrides` en `~/.claude/settings.json` | quitar la clave |
| 10 agentes (`seo-*` ×6, `impeccable-*` ×4) | movidos a `~/.claude/agents-disabled/` | devolverlos a `~/.claude/agents/` |
| 19 MCP apagados **solo en este proyecto**: playwright, Canva, Gamma, Google Calendar/Docs/Drive/Sheets/Slides, Higgsfield, Hostinger, Meta Ads, Miselup, Opus Clip, Plane, Qonto, Trello, NOWPayments, Stripe, Claude Docs | `disabledMcpServers` del proyecto en `~/.claude.json` | `/mcp` → enable |
| Modelo por defecto de los subagentes que no indican modelo: sonnet | `env.CLAUDE_CODE_SUBAGENT_MODEL` | quitar la clave |
| Claude Code 2.1.306 → 2.1.310 | — | — |

- ⚠️ **NOWPayments y Stripe por MCP están apagados aquí.** En 30 días no hubo ni una llamada (los lanzamientos usan la CLI de
  Stripe `--live`, los scripts y las env vars). Si un lanzamiento los necesita: `/mcp` → enable.
- Siguen activos: gscServer, Gmail, Resend y claude-in-chrome.

En el repo (este commit):

- `CLAUDE.md`: fuera las cifras viejas (posts, URLs del sitemap) y el comando de build, que ya está en `netlify.toml`.
- Movidos tal cual, sin perder nada:
  - el método de «productos sin bridge» y el detalle de «Otros idiomas = DUPLICAR» → `.claude/skills/productos-digitales-aichef/SKILL.md`;
  - el gotcha de `faq.astro` → `astro-site/CLAUDE.md`.

## 2. Limpieza opcional (no hecha)

Hay 14 worktrees viejos en `.claude/worktrees/agent-*`:

- Los hubs DE/FR/IT/NL/PT del 24-sep ya están fusionados en el #96.
- Los spokes de Consultoría Gastro Pro son de mayo.
- `agent-a0b26e4cbb20410c2` (cripto, 6-sep) tiene 8 cambios sin commitear: hay que revisarlo antes de borrar nada.
