# Handoff 28-oct-2026 — Cafetería Móvil para Eventos (ES) + Coffee Cart Business Plan Kit (EN) · sesión Claude Code

> Sesión Claude Code (Mac + VPS). Los dos productos LIVE el mismo día. Siguiente: Plan de Negocio Taquería ES + Taco Shop EN.

## 1. Qué salió

| | ES | EN |
|---|---|---|
| Producto | Plan de Negocio: Cafetería Móvil para Eventos (nº 55, 45 €) | Coffee Cart Business Plan Kit ($39) |
| Slug | `plan-negocio-cafeteria-movil-eventos` | `coffee-cart-business-plan` (`/en/digital-products/…`) |
| PR / merge | #177 → `176b10d0` | #178 (apilado) → `13734218` |
| Payment Link | `plink_1UVeuY4CcdRGidmEKFfsfmBH` · `buy.stripe.com/eVqcMY80seAKfDF7Vj6oo28` | `plink_1UVf3T4CcdRGidmEpptCpIzi` · `buy.stripe.com/4gMbIU1C42S21MP8Zn6oo29` |
| Env de Netlify | `VITE_STRIPE_PAYMENT_LINK_PLAN_CAFETERIA_MOVIL` | `VITE_STRIPE_PAYMENT_LINK_COFFEE_CART_BUSINESS_PLAN` |
| Entregables | plan financiero xlsx, Word (7.235 palabras), checklist 80 tareas, calculadora de presupuesto por evento, modelo de contrato, guía de equivalencias | Word, projections xlsx, pricing calculator, 68-task checklist, service agreement template |
| Docs | `scripts/productos-digitales/plan-cafeteria-movil/` | `scripts/productos-digitales/business-plans-en-11/` |
| Correo | 13-dic 08:00Z · borrador `54186da9` · routine `trig_01DfJRFTEchp9u5wvki9gQVj` (13-nov) | 10-mar-2027 14:00Z · borrador `bd617950` · routine `trig_019sy8y23xamjrAcohMyZzfH` (9-feb) |

Links comprobados con la CLI de Stripe `--live`: importe, `one_time`, `tax_behavior=exclusive`, factura activada, redirección a su `/access`,
descripción en prosa (257 y 247 caracteres).

## 2. Verificación LIVE (desde el VPS, `main` = `13734218`)

- `gate-flujo-postpago.py` completo: **87 productos · 1114 entregables · 0 fallos**; `--only` de cada slug: 0 fallos.
- `tienda-gate --base https://aichef.pro`, `robots-gate --live`, `hub-gate` (Cafetería primera, «Nuevo»), `miselup-gate` 110/110: verdes.
- `nombre-gate`: ✅ el slug nuevo (los 46 «rotos» del recorrido completo son deuda antigua; el gate se usa con `--only`).
- `fase6-gate https://aichef.pro`: 3 fallos de 2283, **falsos positivos de umbrales viejos** (recuento del sitemap de julio; `hreflang`
  contado en todo el HTML, cuando la portada tiene sus 8 `<link rel="alternate">` correctos). Conviene actualizar el gate.
- Cripto: `crypto-checkout` 200 ×2 → **pedidos QA por purgar** (`qa-cafemovil@aichef.pro`, `qa-coffeecart@aichef.pro`; John, con `ADMIN_PASSWORD`).
- Sitemap reenviado en GSC (`sc-domain:aichef.pro`); las dos URLs ya están en `sitemap-0.xml` y en `llms.txt` / `llms-full.txt`
  (el recuento del hub ES en `llms.txt` pasa de 51 a 55).

## 3. Deuda que queda anotada

- **Motor 2.2, IVA en la fila de tasas** (`grupo_a.py:2544-2547` aplica el 21 % a la fila de tasas de la PyG; ~63 €/año en este caso;
  nota F35 reescrita). Afecta a la familia: tanda aparte.
- **Fórmulas de más de 255 caracteres** en `Inversión!D28`/`D33` (familia entera del motor).
- **m16 `inject_cache` EN** (común), sin tocar.
- `fase6-gate`: umbrales del sitemap y recuento de `hreflang` (ver §2).

## 4. Carril Cursor (landings + SEO + blog)

Enlazar desde el blog a los dos productos nuevos: posts ES de cafetería, café de especialidad, catering y bodas →
`/plan-negocio-cafeteria-movil-eventos`; posts EN de coffee shop, catering y food truck → `/en/digital-products/coffee-cart-business-plan`.

## 5. Siguiente (cola decidida con John al cierre)

1. **Plan de Negocio Taquería ES (35 €)** + **Taco Shop Business Plan Kit EN ($39)**: rama `feat/plan-negocio-taqueria` creada desde
   `13734218` (worktree `scratchpad/wt-taqueria`). Gemelo de construcción: Pizzería Napolitana (línea A 2.2); reutilizar la research del
   Kit Taquería (`kit-tareas-taqueria/01-research-taqueria-mexicana.md`). Taquería = concepto monoproducto (como pizzería, arepería,
   hamburguesería); la Guía Restaurante Mexicano es el concepto amplio.
2. Taco Shop Checklist Templates EN ($19), desde el Kit Taquería v2.0.
3. **Asador de Pollos**: UN plan de negocio + guía de creación con todas las corrientes (peruana, venezolana, española, francesa) ES + EN,
   y el kit de tareas suelto (= tarjeta anunciada «Tareas Recurrentes: Pollería y Pollo a la Brasa»).
4. Plan Sushi Bar ES + EN (idea nº 50 del plan maestro).
5. Hamburguesería Smash.

Plan maestro actualizado: `/Users/johnguerrero/productos-digitales/Catalogo_…RoadmapExpansion.xlsx` (columna «Estado 28-oct-2026» en
hojas 4 y 6, hoja 8 nueva con LIVE ES 55 · LIVE EN 32 · cola de 76; copia `….BACKUP-2026-10-28.xlsx`).
