# Handoff — 18-oct-2026 (sesión Claude Code, noche delegada) — 5 kits de checklists EN + post pilar food truck

## 0. Estado: 6 productos LISTOS a falta del Payment Link + 1 post en borrador

John (17-oct, 23:30): «continúa con todos los productos que puedas… en la mañana configuramos y creamos los enlaces de Stripe».
Todos son hermanos verticales del **Restaurant Checklists Kit Pro** (LIVE 17-oct, #133), con el mismo circuito
`scripts/productos-digitales/checklists-kit/` (`--kit <vertical>`, memoria de traducción entre kits).

| PR | Producto (EN, $19) | Slug | Env del Payment Link | Estado |
|---|---|---|---|---|
| #134 | Bar Checklists Kit Pro | `bar-checklist-templates` | `VITE_STRIPE_PAYMENT_LINK_BAR_CHECKLISTS_KIT` | preview verde, revisión aplicada |
| #135 | Coffee Shop Checklists Kit Pro | `coffee-shop-checklist-templates` | `VITE_STRIPE_PAYMENT_LINK_COFFEE_SHOP_CHECKLISTS_KIT` | preview verde, revisión aplicada |
| #137 | Catering Checklists Kit Pro | `catering-checklist-templates` | `VITE_STRIPE_PAYMENT_LINK_CATERING_CHECKLISTS_KIT` | preview verde, revisión aplicada |
| #138 | Pizza Shop Checklists Kit Pro | `pizza-shop-checklist-templates` | `VITE_STRIPE_PAYMENT_LINK_PIZZA_SHOP_CHECKLISTS_KIT` | preview verde, revisión aplicada |
| #139 | Burger Joint Checklists Kit Pro | `burger-joint-checklist-templates` | `VITE_STRIPE_PAYMENT_LINK_BURGER_JOINT_CHECKLISTS_KIT` | preview verde, revisión aplicada |
| #140 | Ghost Kitchen Checklists Kit Pro | `ghost-kitchen-checklist-templates` | `VITE_STRIPE_PAYMENT_LINK_GHOST_KITCHEN_CHECKLISTS_KIT` | revisión en curso al escribir esto |
| #136 | Post EN «How to Start a Food Truck Business» | `/en/blog/how-to-start-a-food-truck-business` | — | borrador, gates verdes, auditado |

**Los PR de producto van APILADOS** (cada uno contiene a los anteriores; base `main` para tener preview).
**Orden de fusión obligatorio: #134 → #135 → #137 → #138 → #139 → #140.** El #136 (blog) es independiente.

## 1. Lo que tiene que hacer John: 6 Payment Links (Stripe, USD)

Común a los seis: **$19.00 USD**, pago único, impuesto automático (precio *exclusive*, como los kits EN), redirección
`https://aichef.pro/en/digital-products/<slug>/access?session_id={CHECKOUT_SESSION_ID}`.

| Producto | Descripción para Stripe (prosa, ≤ 260) |
|---|---|
| Bar Checklists Kit Pro | Nine Excel checklist templates and three bonuses for bars: bar opening and closing, cocktail, beer and wine stations, bar manager and bartender duties, cleaning and inventory, events, venue close-out and cash drawer. One-time payment, lifetime access. |
| Coffee Shop Checklists Kit Pro | Nine Excel checklist templates and three bonuses for coffee shops: espresso bar opening and closing, barista and pastry case stations, shift lead and daily duties, cleaning and inventory, holiday season and cash drawer. One-time payment, lifetime access. |
| Catering Checklists Kit Pro | Nine Excel checklist templates and three bonuses for caterers: commissary prep, event chef and service checklists, load-in and load-out, cleaning, event calendar and per-event billing with deposit and balance due. One-time payment, lifetime access. |
| Pizza Shop Checklists Kit Pro | Nine Excel checklist templates and three bonuses for pizza shops: oven, make line and apps stations, pizza maker and delivery driver duties, opening and closing, cleaning and inventory, game nights and cash drawer. One-time payment, lifetime access. |
| Ghost Kitchen Checklists Kit Pro | Nine Excel checklist templates and three bonuses for ghost kitchens: hot, cold and packing stations, multi-brand cook, packer and app manager duties, site opening and closing, cleaning and inventory, rush nights and cash. One-time payment, lifetime access. |
| Burger Joint Checklists Kit Pro | Nine Excel checklist templates and three bonuses for burger joints: grill, make line and fry stations, grill and fry cook duties, opening and closing, cleaning and inventory, Burger Week and cash drawer. One-time payment, lifetime access. |

Ojo al copiar: sin comillas «» al final (en el Restaurant Checklists se coló un «»» en Stripe; quitarlo en el panel).

## 2. Cierre (Claude, con los links)

Por cada link, en el orden de fusión: comprobarlo con la CLI (`stripe payment_links list --live`: USD 1900, `exclusive`,
redirección) → `netlify api createEnvVars` (scope `builds`, context `all`) → `sync-payment-links.py` en la rama del
último PR → sacar de draft y fusionar en orden (**el modo automático bloquea `gh pr merge`: Shift+Tab**) → LIVE:
`gate-flujo-postpago --only <slug>` ×5, `tienda-gate --base https://aichef.pro`, `robots-gate --live`, gate completo
en el VPS, GSC sitemap → correos EN en la cola de 5 días (siguiente hueco **14-dic 14:00Z**; Resend no programa a > 30 días:
borrador + routine como el del Restaurant Checklists, `trig_01GWsawxCZ8CbSBZ387HsMqo`).

## 3. Pendientes y decisiones para John
- 🔴 **OpenRouter: la key da 401 «User not found»** (Mac y VPS). bridge.py inoperativo → el post #136 se redactó con el
  fallback de la regla 5 (subagente + auditoría). Renovar/revisar la cuenta.
- **Testimonios retirados SOLO en EN** por citar cadenas reales: «PizzaExpress» (#138), «Burger Factory» (#139), «CloudEats» y «GhostBurger» (#140; el de Laura Serrano se queda con solo la frase de las apps cambiada). En #139
  queda un «Sergio Ramos» (homónimo del futbolista): decide John.
- **Erratas del ES** encontradas al duplicar (para su próxima versión, no tocadas): CF de cabeceras del catering que pinta 32
  encabezados, orden de apertura/cierre en varios 08, mínimos del inventario de cafetería guardados como texto (el semáforo
  siempre pide), tareas largas de la pizzería sin ajuste de texto. Detalle en `checklists-kit/<vertical>/SPEC.md` §6.

## 4. Lecciones
- El circuito generalizado reduce cada hermano a ≈ 1,2-1,9 M tokens y ~2 h de pared; la memoria de traducción hereda
  entre el 5 % (catering) y el 45 % (hamburguesería) de las cadenas.
- Cada revisión adversarial cazó algo que los gates no ven (promos de alcohol ilegales, 3-501.19 mal dicho, leche abierta,
  horno solo napolitano). Sus lecciones se pasan al siguiente hermano desde la F1: la pizzería y la hamburguesería salieron
  con menos mayores.
- Gate nuevo `TERMINOS_PROHIBIDOS` por kit: caza restos del kit de origen (Head chef en una cafetería, etc.).
- Ramas apiladas con base `main` para tener deploy preview; cada F1 nueva se crea desde la rama anterior y se le fusionan
  los arreglos de la revisión del hermano (un conflicto en `gates_en.py::_cita_mal`, resuelto a mano).
- Térmica: CPU del Mac 44-56 °C toda la noche, con DOS agentes como tope; todo el openpyxl e `inject_cache` en el VPS.

Consumo de la noche ≈ 7-8 M tokens de subagentes (5 kits S + post).
