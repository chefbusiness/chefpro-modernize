# Handoff — 24-oct-2026 (sesión Claude Code, Mac + VPS) — Ice Cream Shop Checklists Kit Pro (EN, $19)

## ▶️ Para retomar (sesión nueva tras /clear)

- **Estado:** producto LISTO a falta del Payment Link. PR **#156** (draft), rama `feat/ice-cream-shop-checklists-en`
  (worktree del Mac en el scratchpad de la sesión `wt-icecream`; en el VPS `/root/wt-icecream`). Preview:
  https://deploy-preview-156--aichefpro.netlify.app/en/digital-products/ice-cream-shop-checklist-templates
- **Carriles:** este producto es del carril Mac (productos). Los banners del blog EN NO se han tocado (carril Cursor): candidatos
  para esa sesión `prompt-library-creative-ice-cream` (el mejor), `prompt-library-gelato-consulting` y `prompt-library-creative-pastry`.
- Detalle técnico: `scripts/productos-digitales/checklists-kit/icecream/{SPEC,F2-NOTAS,F3-NOTAS}.md` y `revision/REVISION-F2.md`.

## 1. Lo que tiene que hacer John: el Payment Link (Stripe, USD)

- **Ice Cream Shop Checklists Kit Pro** · **$19.00 USD**, pago único, impuesto automático (precio *exclusive*, como los kits EN).
- Redirección: `https://aichef.pro/en/digital-products/ice-cream-shop-checklist-templates/access?session_id={CHECKOUT_SESSION_ID}`
- Descripción (prosa, sin comillas al final):
  Nine Excel checklist templates and three bonuses for ice cream shops: opening and closing, pasteurizing and batch freezing, manager and role duties, cleaning and maintenance, peak season and ice cream catering, cash drawer. One-time payment, lifetime access.

## 2. Cierre (Claude, con el link)

Comprobar el link con la CLI (`stripe payment_links list --live`: USD 1900, `exclusive`, redirección) → `netlify api createEnvVars`
`VITE_STRIPE_PAYMENT_LINK_ICE_CREAM_SHOP_CHECKLISTS_KIT` (scope `builds`, context `all`) → `sync-payment-links.py` en la rama →
sacar de draft y fusionar (**el modo automático bloquea `gh pr merge`: Shift+Tab**) → LIVE: `gate-flujo-postpago --only
ice-cream-shop-checklist-templates`, `tienda-gate --base https://aichef.pro`, `robots-gate --live`, gate completo en el VPS, sitemap en
GSC → correo EN (`emails/broadcast-ice-cream-shop-checklists-lanzamiento-en.*`, ya escrito) en el hueco **24-ene 14:00Z**: borrador
en Resend + routine el 25-dic (Resend no programa a > 30 días).

## 3. Hecho hoy

- F1 (SPEC delta + mapas), traducción de 403 cadenas (sonnet), F2 en el VPS (11 xlsx, Letter, °F; gates VERDE 8/0, autotest 19/19,
  0 celdas cortadas nuevas, sha256 Mac = VPS), F3 (landing, access, library, registro, hub EN, llms 23 productos, sitemap, correo),
  UNA revisión adversarial (1 B · 6 M · 14 m) y UNA ronda de arreglos, todo aplicado. ≈ 1,8 M tokens de subagentes. Mac 38-48 °C.
- 🔴 **Errata de seguridad en el ES LIVE corregida** (`kit-tareas-heladeria` 02 «Pasteurización» B13-B14: grasas y yemas se añadían
  DESPUÉS de pasteurizar) + mantecadora «nunca en vacío» (05 B6) + cilindro (02 B24, 05 B13). Parche a nivel de XML de celda: estilos,
  DV, CF y caché idénticos; versión sin cambiar; también en `scripts/generate-tareas-heladeria.py`.
- `tienda-gate.py`: lee robots.txt por grupos (desde el #143 del carril Cursor varios User-agent comparten reglas y daba un falso
  rojo; `robots-gate --live` estaba verde). Alias «Tasks: Pizzeria» → landing EN viva. Fotos con texto ajeno fuera de la landing EN.
- Previews: `gate-flujo-postpago --base` 12/12 entregables 200 y solo fallos de Payment Link; `tienda-gate --base --es-identico`
  48/49 ES idénticas + la esperada.

## 4. Pendiente fuera de este producto

- **Deuda del circuito:** desde `adf52a52` (18-oct, mínimos del inventario ES a número) el dry-run de cafetería, pizzería,
  hamburguesería y ghost kitchen EN sale ROJO (G4 «valor fijado»: el ES trae `2` y `VALORES_EN` espera `'2'`). Lo publicado no cambia;
  hay que adaptar `VALORES_EN` en esos 4 `mapas_<v>.py` antes de volver a regenerarlos.
- Siguiente EN por demanda con gemelo ES v2: chocolatería y pastelería (checklists, molde base); las guías L esperan a sus v2 ES.
