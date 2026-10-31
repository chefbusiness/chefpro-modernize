# Handoff 31-oct-2026 (noche, John dormido) · sesión Claude Code (Mac + VPS) — Sushi Bar ES+EN, 4 checklists EN y resync de los planes EN

John: «seguimos con el Plan Sushi Bar ES y EN, luego continúa con 4 traducciones más… por la mañana me das una lista de todos los
enlaces de pago… decide y elige, lidera tú». Todo queda en PR abiertos, verificados y a la espera de los Payment Links.

## 1. PR abiertos

| PR | Qué | Estado | Orden de fusión |
|---|---|---|---|
| **#191** | Conjuntos EN de planes regenerables tras #186 (`textos_es`/`censo_es` al día, `resync_es.py`, `comparar_sem.py`, `extraer_textos --fijar-clasificacion`) + **fila 34 de «12-Month Cash Flow» a 149,5 pt en 11 planes EN LIVE** (la nota de #186 se cortaba) | listo, sin link (es arreglo); el modo automático bloqueó el merge sin revisión → **revisarlo John** | 1.º |
| **#190** | Plan de Negocio: Sushi Bar (ES, 35 €, nº 58) | gates del preview verdes salvo el link | 2.º |
| **#192** | Sushi Restaurant Business Plan Kit (EN, $39), apilado sobre #190 | gates del preview: ver §2 | 3.º (tras #190) |
| **#189** | Lote de 4 checklists EN: Food Truck, Bakery, Seafood Restaurant ($15) y Fine Dining ($19) | gates del preview verdes salvo los links | cuando haya links |

Tras fusionar #191, la rama de #192 tiene los sha fijados de taco/rotisserie/pizza caducados: pasarle `resync_es.py` y `comparar_sem.py`
(solo afecta a sus scripts de regresión, no al producto).

## 2. Verificación

- **Sushi ES** (`scripts/productos-digitales/plan-sushi/`): 79 comensales × 20 € × 300 = 474.000 €; inversión 163.658 €; préstamo 131.000 € +
  55.000 € propios; neto 9,1 %; DSCR 2,52; holgura de caja 27,8 %. Anisakis por RD 1021/2022 (el RD 1420/2006 está derogado); arroz a
  temperatura ambiente solo vía RD 1086/2020 art. 30.5. Revisiones opus F2 (0 B · 1 M) y F3 (0 B · 2 M), arregladas. Preview #190:
  tienda verde, ES idénticas salvo las esperadas, postpago con los 7 fallos esperados sin link.
- **Sushi EN** (`business-plans-en-14/`): 115 covers × $32.50 × 310 = $1,158,625; total $385,156; SBA $256,000; neto 8.5 %; DSCR 3.59×.
  G1-G9 verde, regresión 22/22; revisiones opus F2 (0 B · 2 M) y F3 (0 B · 1 M), arregladas.
- **Kits EN** (`checklists-kit/{foodtruck,bakery,seafood,finedining}/`): los tres primeros son del **molde plano** de ChefBusiness (una hoja
  por libro, sin instrucciones, contadores ni protección) → ganchos `MOLDE == 'plano'` en el código común con regresión idéntica en los
  12 kits publicados; precio $15. Fine Dining es v2.0 (13 libros, 477 tareas), $19. Gates 8/8 (G5/G6 N/A en los planos), autotests
  14-19, revisión de contenido (0 B · 1 M seafood) y de Fine Dining (0 B · 2 M: ROP del pescado sous vide, recalentado/mantenimiento en
  caliente), todo arreglado; landings contrastadas con los volcados.

## 3. Payment Links que tiene que crear John (6)

Todos: pago único, impuesto automático *exclusive*, factura activada (como los anteriores). Al recibirlos, Claude pone la env (scope
builds), `sync-payment-links.py`, comprueba con `stripe … --live`, fusiona y pasa los gates LIVE.

| # | Producto Stripe | Precio | Redirección | Env |
|---|---|---|---|---|
| 1 | Plan de Negocio Sushi Bar - AI Chef Pro | 35,00 EUR | `https://aichef.pro/plan-negocio-sushi-bar-access?session_id={CHECKOUT_SESSION_ID}` | `VITE_STRIPE_PAYMENT_LINK_PLAN_SUSHI_BAR` |
| 2 | Sushi Restaurant Business Plan Kit - AI Chef Pro | 39.00 USD | `https://aichef.pro/en/digital-products/sushi-restaurant-business-plan/access?session_id={CHECKOUT_SESSION_ID}` | `VITE_STRIPE_PAYMENT_LINK_SUSHI_RESTAURANT_BUSINESS_PLAN` |
| 3 | Food Truck Checklists Kit Pro | 15.00 USD | `https://aichef.pro/en/digital-products/food-truck-checklist-templates/access?session_id={CHECKOUT_SESSION_ID}` | `VITE_STRIPE_PAYMENT_LINK_FOOD_TRUCK_CHECKLISTS_KIT` |
| 4 | Bakery Checklists Kit Pro | 15.00 USD | `https://aichef.pro/en/digital-products/bakery-checklist-templates/access?session_id={CHECKOUT_SESSION_ID}` | `VITE_STRIPE_PAYMENT_LINK_BAKERY_CHECKLISTS_KIT` |
| 5 | Seafood Restaurant Checklists Kit Pro | 15.00 USD | `https://aichef.pro/en/digital-products/seafood-restaurant-checklist-templates/access?session_id={CHECKOUT_SESSION_ID}` | `VITE_STRIPE_PAYMENT_LINK_SEAFOOD_RESTAURANT_CHECKLISTS_KIT` |
| 6 | Fine Dining Checklists Kit Pro | 19.00 USD | `https://aichef.pro/en/digital-products/fine-dining-checklist-templates/access?session_id={CHECKOUT_SESSION_ID}` | `VITE_STRIPE_PAYMENT_LINK_FINE_DINING_CHECKLISTS_KIT` |

Descripciones (un párrafo, ≤ 260 caracteres): las de 1 y 2 están en `PAYMENT_LINKS_PENDIENTES_JOHN.md` de sus ramas (249 y 244); las de los
kits, en el resumen de la mañana (229-246 caracteres; las de §0 de cada `F3-NOTAS.md` pasaban de 260).

## 4. Correos (al publicar)

ES: Sushi Bar **28-dic 08:00Z** (routine). EN, cola de 5 días a las 14:00Z tras el Taco Shop Checklists (25-mar-2027): Sushi Restaurant
30-mar · Food Truck 4-abr · Bakery 9-abr · Seafood 14-abr · Fine Dining 19-abr (borradores + routines a ≤ 30 días). Los HTML están
preparados en `scripts/productos-digitales/emails/` de cada rama.

## 5. Deuda anotada

- ES LIVE de molde plano (Food Truck, Panadería, Marisquería, Tapas Bar): textos sin tildes; la landing ES del Food Truck promete arqueo de
  caja y vitrina que los ficheros no traen (y la de Panadería, horno de convección, KPI, calibración…). Para su próxima versión.
- Sushi EN: el desplegable `Fish Yield!B18` arranca en «I freeze in-house» (el plan compra el pescado tratado); no cambia cifras.
- Gates EN de pizza, burger, cafe y ghost en rojo por deriva (G4) desde antes.
- Kits ES Sushi Bar, Asador y Chef Privado: molde v1.1 (otro gancho si se traducen).

## 6. Térmica

Toda la noche entre 42 y 56 °C con 2-4 agentes (API) y todo el cálculo en el VPS; vigilante en bucle. `knowledgeconstructiond` congelado
desde el 30-oct (`pkill -CONT knowledgeconstructiond` para reanudarlo).

## 7. Mañana del 31-oct (sesión Claude Code): los seis LIVE

John creó los 6 Payment Links y pidió «fusiona los 4». Hecho:

- **Links** comprobados con `stripe … --live` (nombre, importe, pago único, *exclusive*, factura, redirección) y sus 6 envs en Netlify
  (builds); `payment-links.ts` regenerado en cada rama. Detalle en `PAYMENT_LINKS_PENDIENTES_JOHN.md`.
- **Fusiones** (squash): #191 `6a927b25` → #190 `664c6038` → #192 `07e7513a` → #189 `8b02f1e7`.
  - #192 chocaba con el squash de #190 en 6 ficheros (hub EN, `tienda.ts`, `products-catalog.ts`, `tienda-gate.py`, `llms.txt`,
    PAYMENT_LINKS): main traía exactamente la rama ES final y #192 ya la contenía + el EN → versión de #192. Comprobado: la fusión solo
    añadía el parche de #191 byte a byte.
  - #192 tras #191: `resync_es.py` ya conoce `business-plans-en-14` (CONJUNTOS + 4 bloques de sha). Re-extracción con la clasificación
    publicada (recoge «plantilla 02 del Kit» de la F3 del ES en `SUSC F3!E14`; el EN de esa celda no cita el kit español) y 6 sha
    re-medidos. VPS: `bp14 verificar` OK; regresión de los 13 conjuntos 49 IGUAL + 3 xlsx parcheados en #186 IGUAL-SEM; el Sushi EN
    regenerado: 3 xlsx IGUAL-SEM (0 difs) y docx IGUAL.
  - #189 tras #192: hub EN con los 4 kits arriba (Fine Dining 1 → Food Truck 4), luego Sushi Restaurant y Taco Shop Checklists (59
    tarjetas, sin duplicados); `llms.txt` ES 58 · EN 39; mapas regenerados (98 productos).
- **LIVE**: postpago 0 fallos y 0 avisos (98 productos, 1.206 entregables); robots verde; tienda-gate verde en los previews de #192 y #189;
  landings 200 con el link en las 4 posiciones; sitemap + `llms.txt`; GSC reenviado; cripto 200 ×6.
- **Correos**: ver §4 y `CALENDARIO-V2-SEMANAL.md` (entrada del 31-oct). ES 28-dic (routine `trig_01Jm6Rwvrkm6y7jihtxjfCzS`, 29-nov) · EN
  30-mar → 19-abr-2027 (un routine, `trig_01SUhZPtzFnR44opoYmqs4VL`, 21-mar-2027). Pruebas a John ×6. **Siguiente hueco: ES 2-ene-2027 ·
  EN 24-abr-2027.**
- **Pendiente de John**: purgar también los QA cripto de hoy (`qa-sushibar`, `qa-sushi-en`, `qa-foodtruck-en`, `qa-bakery-en`,
  `qa-seafood-en`, `qa-finedining-en`) con el resto de la lista del handoff del 30-oct §4.
- Térmica: un pico de 61 °C tras los gates LIVE; pausa hasta 54 °C antes de seguir.

## 8. Cierre de sesión (31-oct, sesión Claude Code)

- **Estado**: `main` limpio y sincronizado con `origin/main`; producción con los 6 productos nuevos (98 en el registro). Worktrees de
  esta sesión borrados en el Mac y en el VPS; las ramas remotas de #189-#192 siguen en GitHub (se pueden borrar sin pérdida). Los
  worktrees `.claude/worktrees/agent-*` (hub-de, hub-fr, hub-it, hub-nl, hub-pt…) son de otras sesiones: no tocarlos.
- **Térmica**: cierre a 43 °C. El vigilante (`scripts/termica/watchdog-termico.sh`) sigue en bucle; `photoanalysisd`, `mediaanalysisd`
  y `knowledgeconstructiond` siguen congelados (`pkill -CONT <nombre>` para reanudarlos).
- **Pendiente de John**: (1) purgar los pedidos cripto QA sin pagar —los 6 de hoy (§7) + los 15 del handoff del Taco Shop §4— con
  `crypto-report.py --purge-unpaid-before` (la CLI devuelve 401; necesita `ADMIN_PASSWORD`); (2) `CUTOVER_ENBLOG_PENDIENTE.md`.
- **A vigilar**: el 29-nov-2026 (15:07Z) corre el routine del correo ES del Sushi Bar y el 21-mar-2027 el de los 5 EN; comprobar su
  `list_runs` y que los borradores pasen a programados.
- **Siguiente sesión**: Hamburguesería Smash (ES, y luego su EN) → Kit de Tareas Pollería («Próximos»). Alternativa rápida: traducir
  al inglés alguno de los 18 productos ES que siguen sin gemelo EN (los kits de tareas son lo más corto). Antes de traducir un kit ES
  de molde plano o v1.1, mirar la deuda de §5.
- **Siguiente hueco de correo**: ES 2-ene-2027 · EN 24-abr-2027.
