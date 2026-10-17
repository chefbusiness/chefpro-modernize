# Handoff — 17-oct-2026 (sesión Claude Code) — Restaurant Checklists Kit Pro (EN, $19), producto 16 de la tienda EN

## 0. Estado: LISTO a falta del Payment Link · PR #133 (draft) · rama `feat/restaurant-checklists-en`
- Edición EN del `kit-tareas` ES v2.0: 9 plantillas + 2 bonus xlsx + bonus común de equivalencias (`dl/en-shared/`).
  `/en/digital-products/restaurant-checklist-templates` (+ `/access`, `/library`). Carpeta `scripts/productos-digitales/checklists-kit/`.
- Elegido con DataForSEO US (17-oct): clúster de checklists ~1.300/mes (opening 260 · cleaning 260 · kitchen 210 · checklist(s) 140 · closing 90…)
  + UK kitchen cleaning checklist 260. Ojo: «taco truck business plan» 9.900 = mismas cifras que «food truck business plan» (agrupación de Google Ads).
- Gates contra el preview `deploy-preview-133--aichefpro.netlify.app`: `tienda-gate` verde · `--es-identico` 48/49 + `/kit-tareas` (solo hreflang, esperado) ·
  `gate-flujo-postpago --only` 12/12 descargas, cripto OK; los 3 fallos = falta el Payment Link (env + `payment-links.ts` + botón `#comprar`) ·
  aviso webhook 501 = esperado en preview. F2 (VPS): G1-G8 verdes, autotest 16/16, `censo-entregables` 0, `gate-no-latinos` 0.
- Revisión adversarial (opus): 0 bloqueantes · 4 MAYOR + 15 menor aplicados (ronda 1 de 2); v2.1 anotada en `checklists-kit/revision/REVISION-F2.md`
  (server checkout / tip-out / paid-outs, recalentado 165 °F sin fila propia).

## 1. Cierre (cuando John cree el link)
1. Stripe (John): nombre «Restaurant Checklists Kit Pro» · $19.00 USD · impuesto automático (`tax_behavior` exclusive, como los kits EN) ·
   redirección `https://aichef.pro/en/digital-products/restaurant-checklist-templates/access?session_id={CHECKOUT_SESSION_ID}` · descripción (245):
   «Nine Excel checklist templates and three bonuses for US restaurants: kitchen, FOH and bar opening and closing, station and manager checklists,
   side work by role, cleaning schedule, holiday prep and cash drawer. One-time payment, lifetime access.»
2. Comprobar el link con la CLI de Stripe (`--live`), env `VITE_STRIPE_PAYMENT_LINK_RESTAURANT_CHECKLISTS_KIT` (scope builds), `sync-payment-links.py`, commit.
3. Sacar #133 de draft y merge (el modo automático bloquea `gh pr merge`: Shift+Tab). `vivo: true` ya va en la rama: no fusionar sin link.
4. LIVE: `gate-flujo-postpago --only restaurant-checklist-templates`, `tienda-gate --base https://aichef.pro`, `robots-gate --live`, acceso por admin,
   sitemap en GSC. Gate completo (67 productos) en el VPS.
5. Correo EN: plantilla `emails/broadcast-restaurant-checklists-lanzamiento-en.html`; siguiente hueco EN **9-dic 14:00Z** → borrador + routine
   (programable desde el 9-nov). Test real en Google Sheets antes de afirmarlo (hoy la landing no lo promete).
6. Limpieza: `git worktree remove` en el Mac (scratchpad `wt-checklists`) y en el VPS (`/root/wt-checklists`).

## 2. Lecciones
- El VPS estuvo caído ~1 h (sin ping; reinicio del lado de Hostinger): la F1 siguió en el Mac porque es API-bound; la F2 esperó y corrió allí.
- Dos picos térmicos (63 y 66 °C) los causó el Chrome del Mac, no el trabajo: pausa con bucle de `istats` hasta < 60 °C.
- `KitTareasLandingPage` ya acepta `lang`: los ~20 hermanos verticales EN reutilizan plantilla, `checklists-kit/` (mapas por vertical) y el
  comparador sin build `scripts/astro-migration/es-identico-local/` (requiere `ASTRO_NM`).

Consumo ≈ 2,1 M tokens de subagentes (S, techo 2,5 M) en ~2 h. CPU del Mac 46-66 °C (picos del Chrome del Mac); xlsx y gates pesados en el VPS.
