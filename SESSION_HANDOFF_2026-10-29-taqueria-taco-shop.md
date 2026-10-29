# Handoff 29-oct-2026 · sesión Claude Code (Mac + VPS) — Taquería ES + Taco Shop EN, LOS DOS LIVE

## 1. Qué salió
- **Plan de Negocio: Taquería** (ES, 35 €, nº 56) — https://aichef.pro/plan-negocio-taqueria · PR #181 → `add4451c`.
  5 entregables en `dl/plan-negocio-taqueria/`: plan financiero (motor 2.2, semilla Pizzería LIVE, Mes 1 = enero), Word de 10
  secciones, checklist de 80 tareas, calculadora del trompo y escandallo (4 hojas), guía de equivalencias (censo 56).
- **Taco Shop Business Plan Kit** (EN, $39) — https://aichef.pro/en/digital-products/taco-shop-business-plan · PR #182 → `bf18ff72`.
  4 entregables en `dl/taco-shop-business-plan/` (Letter) + bonus común de equivalencias. Conjunto `taq` en `business-plans-en-12/`.
- Docs: `scripts/productos-digitales/plan-taqueria/` (F1-research, F1-camino, F2-NOTAS, REVISION-FINAL) y
  `scripts/productos-digitales/business-plans-en-12/` (F1-research-us-delta, F2-NOTAS, REVISION-FINAL).

## 2. Verificación LIVE
Postpago `--only` ×2: 0 fallos · tienda, robots, hub, Miselup 112/112 verdes · cripto 200 ×2 · sitemap con las dos URLs y reenviado a
GSC · `fase6-gate`: 3 falsos positivos de siempre (umbrales del sitemap y `hreflang`).

## 3. Pendientes
- **John**: purgar los pedidos QA de cripto `qa-taqueria@aichef.pro` y `qa-tacoshop@aichef.pro` (`crypto-report?purge_unpaid_before=`,
  con `ADMIN_PASSWORD`).
- Correos: ES 18-dic (routine `trig_01TEKYVQu3egcewC5fss64zM`, 18-nov) · EN 15-mar-2027 (routine `trig_01RLdVGQKRp4dUy9W8scMmit`,
  14-feb-2027): comprobar sus `list_runs`.
- Deuda menor: `Inversión!D37` sin separador de miles (fórmula del motor común, también en la Pizzería); citas del Word ES (Ley 18/2022,
  Reg. 1169/2011 art. 14, ET 1.1) correctas pero no anotadas en el research §1; `nombre-gate.py` no mira fichas EN (`productos-en/`).
- Commit de merge `e4fe8c26` en la rama ES salió sin el trailer `Via:` (merge por defecto); no se reescribe.

## 4. Carril Cursor (landings + SEO + blog)
Enlazar desde el blog: posts ES de cocina mexicana, tacos al pastor (`tacos-al-pastor-autenticos-receta-mexicana.md`), restaurante
mexicano y apertura de negocio → `/plan-negocio-taqueria`; `productIds` de `restaurante-mexicano` en `src/data/use-cases-content.es.ts`;
posts EN de Mexican restaurant / food truck → `/en/digital-products/taco-shop-business-plan`. La Guía Restaurante Mexicano ya no lleva
«abrir taqueria» en sus keywords y enlaza al plan.

## 5. Siguiente
**Pollería / Asador de Pollos** (prioridad 2 de la cola): UN plan de negocio + guía con todas las corrientes (peruano, venezolano, asador
español, rôtisserie) ES + EN; mapa de keywords listo en `scripts/productos-digitales/plan-polleria/F0-mapa-keywords-es-en.md`. Después
Taco Shop Checklist Templates EN ($19), Sushi Bar y Hamburguesería Smash.

## 6. Segunda pareja del día (29-oct, tarde-noche · sesión Claude Code): Pollería ES + Rotisserie Chicken EN, LOS DOS LIVE
- **Plan de Negocio: Pollería y Asador de Pollos** (ES, 35 €, nº 57) — https://aichef.pro/plan-negocio-polleria · PR #183 → `6fb676c2`.
  Docs: `scripts/productos-digitales/plan-polleria/` (F0, F1-research, F1-camino, F2-NOTAS, REVISION-FINAL).
- **Rotisserie Chicken Restaurant Business Plan Kit** (EN, $39) — https://aichef.pro/en/digital-products/rotisserie-chicken-restaurant-business-plan
  · PR #184 → `26e618f8`. Docs: `scripts/productos-digitales/business-plans-en-13/`.
- LIVE verde (postpago 0 fallos ×2, tienda, Miselup 114/114, cripto 200 ×2, sitemap + GSC). Correos ES 23-dic (`trig_016kaq4TEPPAhirwMdwYaAKv`)
  · EN 20-mar-2027 (`trig_01Vjtwyj3hKpar5kL2DRRwSk`).
- **John**: purgar también los pedidos QA `qa-polleria@aichef.pro` y `qa-rotisserie@aichef.pro`.
- **Deuda nueva**: checklist de la Taquería LIVE, F6 (`plan-taqueria/datos_checklist.py:289`), cita solo «ITC-ICG 08» en el control del gas
  cada 5 años (la otra mención dice «ITC-ICG 07 e ITC-ICG 08»): arreglo menor sin correo en una tanda de arreglos.
- **Lecciones**: (1) la rama EN apilada nace de la ES antes de los arreglos de la F3 ES → fusionar la ES en la EN antes de pasar gates;
  (2) los nombres traducidos de las tarjetas de los hubs no llevan la palabra española (`tienda-gate --base` la caza como resto);
  (3) contrastar SIEMPRE la landing EN con los entregables antes de abrir el PR (8 correcciones en el Taco y 8 en el Rotisserie).
- **Carril Cursor**: enlazar desde el blog (posts de pollo a la brasa, cocina peruana, asador, comida para llevar) → `/plan-negocio-polleria`;
  posts EN de Peruvian chicken / rotisserie → el kit EN; caso de uso `restaurante-peruano` (`src/data/use-cases-content.es.ts:3690`).
