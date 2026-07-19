# SESSION HANDOFF — 2026-07-20 (madrugada, cierre del sprint nocturno)

> Sesión continua desde 2026-07-19. Doc canónico: `PLAN_MAESTRO_MIGRACION_ASTRO_2026.md` §8
> (entrada 2026-07-19/20). Memoria: `session-2026-07-19-fase8b-port-blog.md`.

## ✅ Qué quedó HECHO y VERIFICADO en esta sesión

1. **🚀 CUTOVER 8B.5 EJECUTADO** — blog.aichef.pro → 301 a aichef.pro/blog
   - Causa raíz DNS: `blog` era dominio principal NATIVO de la instancia WP (apaño manual
     Hostinger 2024). John lo desvinculó; WP aparcado en `darkgrey-dugong-825343.hostingersite.com`
     (backup vivo, no tocar).
   - CNAME live + SSL emitido + batería 301 7/7 verde + 3 checks 301/TLS añadidos a
     `fase7-vigilancia.py`.
   - ⚠️ **NO cancelar Hostinger hasta ~2026-07-24** (margen rollback). Claude da la señal si la
     vigilancia sigue limpia.

2. **Refresh Tier A: slices A4-A8 = 50 posts → total 78/134 (58%)**
   - Commits: `9f0266b` (A4) · `f587191` (A5) · `66d5bde` (A6) · `7d0bf14` (A7) · `b9e5650` (A8).
   - Receta consolidada (Workflow por slice): productor opus (WebSearch SERP → brief →
     bridge.py 16k tokens → fase8b-refresh-assemble.py) + QA adversarial opus por post →
     verificación Fable (greps prohibidas + **regen blog-lastmod.json** + fase8b-gate + push +
     vigía deploy + spot-check títulos live).
   - QA cazó >100 issues: agentes inventados (catálogo canónico = `src/lib/linkify-use-case.tsx`),
     "catalán" como 7º idioma (es NEERLANDÉS), editor de fotos inexistente, IAE 671.5→672,
     EFSA recaracterizado, RD 315/2025 verificado real (BOE-A-2025-7659).

3. **F8 — /precios en 7 idiomas** (`450d4bb`)
   - Nuevas: `/fr/tarifs` `/de/preise` `/it/prezzi` `/pt/precos` `/nl/prijzen` (workflow 5 prod +
     5 QA nativos). hreflang ×8 verificado en las 7 páginas. Header "Precios" → página dedicada
     (antes ancla `/#pricing`); Footer con mapa de 7 rutas.

4. **F8 — páginas fantasma del llms.txt** (`43225ff`): `/contacto` `/sobre-nosotros` `/faq` en
   200 (E-E-A-T: bio John 29/15, estándares editoriales, FAQPage schema, WhatsApp ya público).

5. **Sitemap 696 → 1.073 URLs** con lastmod real; reenviado a GSC (sc-domain:aichef.pro).
   Gates actualizados: `_F8_EXTRA` (vigilancia) y `f8_extra` (fase6-gate) = 10 rutas F8.

6. **Fix de cierre** (`2b6786b`): 9 imágenes generadas por productores de A3/A4 estaban en disco
   pero SIN commitear → 404 live. Auditoría refs↔disco↔tracking ejecutada (script inline).
   Micro: 2ª imagen de `que-significa-abocar-en-cocina` (estándar ≥2 cumplido).

## ⚠️ Reglas/gotchas nuevos de esta sesión

- **Commits de slices DEBEN incluir `astro-site/public/blog-assets/`** — los productores generan
  imágenes nuevas; el `git add` quirúrgico de content/ las deja fuera (bug cazado al cierre).
- zsh: JAMÁS `for path in ...` (pisa $PATH). · `grep -c` en HTML minificado = 1 línea (usar
  python `.count()`). · El QA de slices debe verificar agentes contra `linkify-use-case.tsx`.
- Tras CADA refresh: regenerar `astro-site/src/lib/blog-lastmod.json` (el assembler NO lo toca).

## 📌 PRÓXIMO (en orden)

1. **Decisión John**: 301 de ~13 posts Tier A duplicados de pilares refrescados
   (branding-gastronomico-con-ia, gestion-de-franquicias-gastronomicas-con-ia,
   como-usar-ai-chef-pro-catering, tecnologia-de-seguridad-alimentaria, 10-herramientas,
   generador-de-menus-con-ia, puede-chatgpt-disenar-menu, puede-la-ia-reemplazar-transforma,
   fotografia-culinaria-mejorada, automatizacion-inteligente-en-hosteleria,
   ia-en-artes-culinarias, la-ia-en-la-alta-cocina, intro/introduccion-a-ai-chef-pro).
   Consolida autoridad pero elimina URLs con historial → **solo con OK explícito**.
2. **Slices A9+**: ~27 posts Tier A únicos restantes (misma receta; script de A8 reutilizable
   cambiando POSTS: `.claude/.../workflows/scripts/fase8b-refresh-a8-*.js`).
3. **~2026-07-24**: señal para cancelar Hostinger/WP si vigilancia limpia → cierra task #21.
4. **8B.6 Blog EN nativo** (/en/blog; semillas del export enblog) → luego FR/DE/IT/PT/NL (#22).
5. **F8 auditoría general** (#24) + los 27 posts LATAM congelados como calendario editorial.
6. Vigilancia GSC hasta ~2026-08-16 (cobertura, 404, compras post-pago) — re-armar cron 9:23
   en sesión nueva si caducó.

## Estado de tareas (tablero)

- #20 in_progress (78/134) · #21 in_progress (cutover hecho; falta señal cancelación ~24 jul) ·
- #22 pending · #24 pending · #18/#19/#23 completed.
