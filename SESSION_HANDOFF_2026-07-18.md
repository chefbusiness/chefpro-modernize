# SESSION HANDOFF — 2026-07-18

**Sesión: migración Astro, Fase 1 slice 3 — home ×7 idiomas CERRADO con gates verdes.**

---

## 1. Qué se cerró hoy ✅

- **Home en los 7 idiomas** en staging (commits `272db46` + `3abfbca`): 6 páginas nuevas `astro-site/src/pages/{en,fr,de,it,pt,nl}/index.astro` reutilizando los 22 componentes con prop `lang`; title/meta desde `pages.index.seo_*` de cada JSON (mismas claves que la SPA vía `SEOHead`).
- **Auditoría adversarial i18n de los 23 componentes vs la SPA** (los .astro solo se habían revisado renderizando ES): salió casi limpia — el port de slice 2 ya usaba estructuras por idioma (`LMap` + `pick()`). 1 fix aplicado: el menú móvil usaba las etiquetas largas del desktop; la SPA tiene etiquetas cortas propias en móvil → `roleItemsMobile`/`conceptItemsMobile` verbatim de ModernHeader.tsx 581-585/599-604 (77 labels byte-parity, slugs intactos).
- **HEAD = `3abfbca`** (más el commit de docs de esta sesión).

## 2. Gates verificados (curl UA Googlebot, staging)

200+noindex ×7 · `<html lang>` ×7 · **title/meta description == `seo_*` del JSON byte-exactos** (en/fr/de/it/pt/nl; ES mantiene el hardcode aprobado en slices 1-2) · canonical `/{lang}` · hreflang×8 · 2 JSON-LD **localizados** (faq.q1 nativo dentro del FAQPage, verificado en/de/nl) · 5 textos nativos de secciones distintas server-side ×7 · bytes visibles: es 23.032 / en 19.376 / fr 24.073 / de 21.188 / it 20.781 / pt 21.216 / nl 20.515.

## 3. Gotcha técnico NUEVO (importante para TODAS las páginas futuras)

**`build: { format: 'file' }` en `astro-site/astro.config.mjs`.** Con el default (`directory`), `en/index.astro` genera `en/index.html` y Netlify responde **301 `/en` → `/en/`** — rompe la paridad D6 (la SPA y el sitemap usan URLs SIN barra). Con `file` se genera `en.html`, `/en` responde 200 y `/en/` normaliza 301 → `/en`. Cualquier página anidada futura (`/mentoria-online`, spokes, pSEO) depende de este ajuste, ya aplicado.

## 4. Hallazgo de alcance — /precios NO existe (corrige el plan)

`/precios`, `/sobre` y `/servicios` **no existen en la SPA**: 0 rutas en `App.tsx`, 0 entradas en el sitemap; "Precios" del header enlaza al ancla `/#pricing` de la home. La Fase 1 los listaba por error. **Fase 1 restante real**: `/mentoria-online` (×idiomas, ruta `/:lang/mentoria-online`) y `/formacion-presencial` (solo ES + alias `/es/formacion-presencial`). Crear `/precios` sería URL/copy nuevo → decisión de producto, Fase 8 como muy pronto.

Anomalía menor anotada: `es.json` → `pages.index.seo_description` dice "marketing gastronomico" **sin tilde** (erosión previa); el hardcode ES de `index.astro` la lleva. Resolver junto a la auditoría de acentos pendiente (`feedback_acentos_tildes.md`).

## 5. Método (replicable) + térmica

Workflow de **8 agentes en secuencia estricta**: 1 sonnet (creación mecánica de las 6 páginas) + 6 lotes Opus (auditoría adversarial i18n con evidencia fichero:línea en ambos lados y obligación de auto-refutar) + 1 fixer Opus (verifica antes de aplicar). Guardián istats en background (umbral 63 °C): **CPU 42-50 °C toda la sesión, cero alertas**. Builds solo en nube (Netlify auto-deploy); verificación por curl.

## 6. Próxima sesión — arranque directo

1. **`/mentoria-online` ×7 idiomas**: portar `src/pages/MentoriaOnline.tsx` a Astro (mismo método que la home: port → auditoría adversarial → fixer → gates). Verificar qué variantes de idioma están en el sitemap antes de crear páginas.
2. **`/formacion-presencial`** (ES + alias `/es/formacion-presencial` — ojo: NO tiene variantes en otros idiomas en la SPA).
3. Después: resto Fase 1 (legales/cookies/privacidad/terminos/sistema-creditos ×idiomas si están en sitemap) → Fase 2 use cases (gate anti-huérfanas + interenlazado).

**Directiva vigente**: ejecución AUTÓNOMA slice a slice (la SPA es la spec, gates los verifico yo); parar solo en producto/copy nuevo, dinero (Fases 4-5) y cutover (Fase 7). Regla térmica: istats siempre, secuencial, builds SOLO nube, sin Playwright.

## Mensaje para retomar

> Claude, retomamos la migración Astro de aichef.pro. Lee `PLAN_MAESTRO_MIGRACION_ASTRO_2026.md` (§8) y `SESSION_HANDOFF_2026-07-18.md`. Slice 3 (home ×7) cerrado y verificado; arranca directo con `/mentoria-online` ×7 idiomas en staging (site `dc777725-7e95-4336-876e-a5a9b568fe75`).
