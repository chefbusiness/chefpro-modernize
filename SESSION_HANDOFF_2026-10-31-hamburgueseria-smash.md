# Handoff 31-oct-2026 (noche) · sesión Claude Code (Mac + VPS) — Hamburguesería Smash ES + Burger Restaurant EN

Continúa `SESSION_HANDOFF_2026-10-31-noche-sushi-y-lote-checklists.md` (§8 = cierre anterior). John: «dale, seguimos con la
Hamburguesería Smash». Los dos productos están construidos, revisados y en PR; **faltan los dos Payment Links de John**.

## 1. PR abiertos (borrador)

| PR | Qué | Rama | Orden |
|---|---|---|---|
| **#195** | Plan de Negocio: Hamburguesería Smash (ES, 35 €, nº 59) | `feat/plan-negocio-hamburgueseria` | 1.º |
| **#196** | Burger Restaurant Business Plan Kit (EN, $39), apilado sobre #195 | `feat/burger-restaurant-business-plan-en` | 2.º (tras #195) |

Con squash, #196 chocará con el squash de #195 en los ficheros compartidos (lección del Sushi): `git merge origin/main` en la rama EN y
quedarse la versión de la rama EN, comprobando que solo añade lo de main. `main` ya trae #193 (medición de compra en `-access`) y #194
(GA4): las dos ramas los tienen fusionados (`2982fa78`, `95e227e1`).

## 2. Payment Links que tiene que crear John

Fichas completas en `PAYMENT_LINKS_PENDIENTES_JOHN.md` de cada rama.
- ES: «Plan de Negocio: Hamburguesería Smash - AI Chef Pro», 35,00 EUR, éxito → `/plan-negocio-hamburgueseria-access?session_id={CHECKOUT_SESSION_ID}`,
  env `VITE_STRIPE_PAYMENT_LINK_PLAN_HAMBURGUESERIA`, descripción de 259 caracteres.
- EN: «Burger Restaurant Business Plan Kit - AI Chef Pro», 39.00 USD, éxito → `/en/digital-products/burger-restaurant-business-plan/access?session_id={CHECKOUT_SESSION_ID}`,
  env `VITE_STRIPE_PAYMENT_LINK_BURGER_RESTAURANT_BUSINESS_PLAN`, descripción de 234 caracteres.
Al recibirlos: `stripe payment_links list --live` + line_items, env (scope builds), `sync-payment-links.py` en cada rama, preview, merge
#195 → #196, gates LIVE (`gate-flujo-postpago.py`, `robots-gate.py --live`, landings 200 con el link ×4, sitemap + llms, GSC, cripto 200
con `qa-hamburgueseria` / `qa-burger-en`), correos.

## 3. Verificación

- **ES** (`scripts/productos-digitales/plan-hamburgueseria/`): semilla = Sushi Bar LIVE (dry-run 0 diferencias). 95 comensales
  equivalentes × 16,00 € × 300 = 456.000 €; neto 10,2 / 11,4 / 10,7 %; inversión 162.144 €; necesidad 184.057 € (55.000 € + 130.000 €);
  DSCR 2,64; equilibrio contable 76, caja 73 (holgura 30,9 %). Calculadora `Carne` · `Patatas` · `Escandallo` · `Instrucciones` (autotest
  644). Revisiones: F2 opus 0 B · 4 M · 10 m; lector legal (853/2004: picar dentro de 6 días del sacrificio, 15 solo vacuno deshuesado al
  vacío; batido «confírmalo con tu gestoría»); F3 opus 0 B · 3 M · 9 m. Preview #195: postpago solo los 3 ✗ del link; tienda-gate 51/56
  ES idénticas + las 5 esperadas (4 `footerLinks` y la landing nueva).
- **EN** (`business-plans-en-15/`, conjunto `bur`): 195 covers × $16.50 × 360 = $1,158,300; neto 7.6 / 9.3 / 10.3 %; inversión $382,704
  ($130,000 + SBA $253,000); DSCR 3.37×; `Break-Even!B25` = 5. G1-G9 verde; regresión de 14 conjuntos 53 IGUAL + 3 IGUAL-SEM. Revisiones:
  F2 opus 0 B · 3 M · 5 m; F3 sonnet 0 B · 2 M · 5 m (23 FAQ).

## 4. Correos (al publicar)

ES **2-ene-2027 08:00Z** (`emails/broadcast-plan-negocio-hamburgueseria-lanzamiento-es.html`; borrador + routine ≥ 3-dic-2026). EN
**24-abr-2027 14:00Z** (`broadcast-burger-restaurant-business-plan-lanzamiento-en.html` + `.subject.txt`; routine ≥ 25-mar-2027).
Siguiente hueco tras estos: ES 7-ene-2027 · EN 29-abr-2027.

## 5. Deuda anotada

- **Kit de Tareas Hamburguesería (LIVE)** contradice al plan en la fritura: 175-180 °C (`01-apertura-cierre.xlsx` `Apertura Cocina!B16`,
  `02-partidas-cocina.xlsx` `Freidora!B7`) frente a < 175 °C (acrilamida), y cambiar el aceite «si está oscuro o huele» (`Freidora!B19`)
  frente a polares < 25 %. Además su tabla de congelación no avisa del art. 7.2 (picada del local, del día) y los hubs dicen 302 tareas
  frente a 346. Tanda de arreglos sin correo (y revisar el gemelo Burger Joint Checklists EN).
- `nombre-gate.py`: `ai-prompts-for-restaurants` (EN) roto también en main.
- La de antes sigue: `SESSION_HANDOFF_2026-10-31-noche-sushi-y-lote-checklists.md` §5.

## 6. Gasto y térmica

≈ 4,4 M tokens de subagentes para la pareja (F1 ≈ 0,8 · ES F2+F3 ≈ 2,0 · EN F2+F3 ≈ 1,5), dentro del techo de 5 M. Imágenes: 10
generaciones Nano Banana (≈ 0,70 $). Mac entre 38 y 50 °C todo el tiempo; todo el cálculo en el VPS (`/root/wt-smash`, `/root/wt-burger-en`).
