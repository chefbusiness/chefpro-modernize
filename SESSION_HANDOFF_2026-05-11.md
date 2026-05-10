# SESSION HANDOFF — 2026-05-11 noche → próxima sesión

## TL;DR
Sprint paridad CB↔AICP avanza: **Bloque B Línea A CERRADO 5/5 LIVE 100%** + **Bloque C Línea B Gastro Móvil 2/5 LIVE**. Mañana arrancamos con **Paellero €45** (réplica clónica del template Parrillero).

**HEAD git**: `ed68a86` pusheado a `origin/main`. Working tree limpio salvo untracked previos a la sesión (`.playwright-mcp/`, `SPEC_*.md`, `audit-en-pilot/`, etc. — no tocar).

---

## 🎯 Tarea inmediata al retomar

**Producto siguiente del Bloque C Línea B: Paellero / Paella para Eventos €45**

Mensaje sugerido para arrancar mañana:
> Continuamos sprint paridad CB↔AICP. Lee la memoria. Arrancamos con **Paellero / Paella para Eventos €45** — réplica clónica del template Parrillero ya rodado (Bloque C Línea B 3/5). Assets ya inspeccionados, comando en el handoff.

---

## Estado actual del sprint paridad

### Bloque A — Kits Tareas (€12-€14) — CERRADO 6/6 LIVE 100% ✅
Sushi Bar, Asador, Marisquería, Tapas Bar, Food Truck, Panadería.

### Bloque B — Planes Negocio Línea A (€29-€35) — CERRADO 5/5 LIVE 100% ✅
| # | Producto | Precio | Status |
|---|---|---|---|
| 1 | Bar-Restaurante | €35 | ✅ LIVE |
| 2 | Tapas Bar / Gastrobar | €35 | ✅ LIVE |
| 3 | Cafetería / Brunch | €29 | ✅ LIVE |
| 4 | Panadería / Obrador | €35 | ✅ LIVE |
| 5 | Food Truck | €29 | ✅ LIVE |

### Bloque C — Planes Negocio Línea B Gastro Móvil (€45-€55) — 2/5 LIVE
| # | Producto | Precio | Status |
|---|---|---|---|
| 1 | Coctelería de Eventos / Barra Móvil | €55 | ✅ LIVE (template canónico) |
| 2 | Parrillero / Asador para Eventos | €45 | ✅ LIVE |
| **3** | **Paellero / Paella para Eventos** | **€45** | ⏳ **Siguiente** |
| 4 | Chef Privado Showcooking | €45 | ⏳ Pendiente |
| 5 | Catering Temático Eventos | €45 | ⏳ Pendiente |

---

## 📋 Paellero — assets ya inspeccionados, listos para portar

- **Slug**: `plan-negocio-paellero-eventos`
- **Precio**: €45 (igual que Parrillero)
- **Entregables**: 11 (7 docx + 4 xlsx)
- **Gallery**: 7 imágenes (usar primeras 6 en el grid)
- **Hero**: `plan-negocio-paellero-eventos-hero.jpg`
- **Diferenciales únicos**:
  - 88 proveedores reales (DO Valencia + Calasparra)
  - Equipamiento Garcima / Vaello / Pordamsa
  - Manual técnico del fuego + socarrat
  - Modelo híbrido B2C (bodas, comuniones, fiestas del pueblo, cumpleaños) + B2B (wedding planners, agencias, hoteles 4-5*, ayuntamientos, empresas team-building)

### Paths CB → AICP

**Deliverables** (`chefbusiness-astro/public/dl/plan-negocio-paellero-eventos/` → `chefpro-modernize/public/dl/plan-negocio-paellero-eventos/`):
```
10-experiencias-tematicas-paellero.docx
calculadora-pricing-eventos-paellero.xlsx
carta-12-paellas-arroces.docx
catalogo-equipamiento-utensilios-menaje-paellero.docx
checklist-apertura-paellero-eventos.xlsx
guia-tipos-paellero-roadmap-food-truck.docx
manual-tecnico-paellero-profesional.docx
modelos-contrato-paellero-eventos.docx
plan-de-negocio-paellero-eventos.docx
plan-financiero-paellero-eventos.xlsx
plantilla-proveedores-paellero-eventos.xlsx
```

**Gallery** (`chefbusiness-astro/public/images/gallery/plan-paellero-eventos/` → `chefpro-modernize/public/lovable-uploads/ai-gallery/plan-paellero-eventos-{1..6}.jpg`):
```
01-paella-valenciana-finca-boda.jpg     → plan-paellero-eventos-1.jpg
02-paella-marisco-corporate.jpg          → plan-paellero-eventos-2.jpg
03-show-cooking-paella-restaurante.jpg   → plan-paellero-eventos-3.jpg
04-equipamiento-paelleras-detalle.jpg    → plan-paellero-eventos-4.jpg
05-food-truck-paellero-arroceria.jpg     → plan-paellero-eventos-5.jpg
06-arroces-emplatados-editorial.jpg      → plan-paellero-eventos-6.jpg
(skip 07-fiesta-pueblo-paella-popular.jpg)
```

**Hero** (`chefbusiness-astro/public/images/productos/plan-negocio-paellero-eventos-hero.jpg` → `chefpro-modernize/public/lovable-uploads/ai-gallery/plan-paellero-eventos-hero.jpg`)

**OG** (copia del hero → `chefpro-modernize/public/og-plan-negocio-paellero-eventos.jpg`)

---

## Workflow probado (rodado en Coctelería + Parrillero, sin errores)

1. **Inspect astro source completo** (1209 líneas máximo): `Read` líneas 1-120 + `grep -n "price-old\|BONUS\|Valor:"` para extraer precio tachado + 2 bonuses
2. **Copy assets** con bash one-liner + `set -e`
3. **Build 11 components React** (FadeIn re-export + Hero + ContentGrid + WhySection + AuthorSection + BonusSection + BuyBox + GuaranteeSection + FaqAccordion + CtaFinal + StickyBar) — usar Parrillero como base, cambiar Stripe env var + slug + copy específico paellero
4. **Build testimonials data file** con los 8 testimonios del .astro CB
5. **Build 3 pages** (Landing + AccessGate + Dashboard con 11 entregables TEMPLATES)
6. **Wire 4 configs**:
   - `src/data/productos-digitales-config.ts` — entry con 11 file paths
   - `src/App.tsx` — 3 imports + 3 rutas
   - `netlify/edge-functions/og-meta.ts` — entry SEO
   - `src/pages/ProductosDigitales.tsx` — hub card con tags
7. **Build local** (`npm run build`) → verde
8. **Stage selectivo** (NO `git add -A` — arrastra untracked previos):
   ```bash
   git reset HEAD > /dev/null 2>&1
   git add public/dl/plan-negocio-paellero-eventos/ \
     public/lovable-uploads/ai-gallery/plan-paellero-eventos-*.jpg \
     public/og-plan-negocio-paellero-eventos.jpg \
     src/components/plan-negocio-paellero-eventos/ \
     src/data/testimonials-plan-paellero-eventos.ts \
     src/data/productos-digitales-config.ts \
     src/pages/PlanNegocioPaelleroEventos*.tsx \
     src/pages/ProductosDigitales.tsx \
     src/App.tsx \
     netlify/edge-functions/og-meta.ts
   ```
9. **Commit + push** a `origin/main`
10. **Entrega a John**: Stripe link template (nombre + precio + descripción ≤260 chars verificada + confirmation URL `https://aichef.pro/plan-negocio-paellero-eventos-access?session_id={CHECKOUT_SESSION_ID}` + env var `VITE_STRIPE_PAYMENT_LINK_PLAN_PAELLERO`)
11. **Cuando John pase Stripe link**: commit vacío `chore: trigger Netlify rebuild` + push → LIVE en producción ~2-3 min

Tiempo estimado: **30-40 min** desde inspect hasta entrega del paquete Stripe a John.

---

## ⚠️ Reglas no negociables

1. **Descripciones Stripe ≤260 caracteres ESTRICTO**, párrafo en prosa, sin bullets ni guiones. Verificar SIEMPRE con `python3 -c "print(len('...'))"` antes de pasar a John. (Memoria: `feedback_stripe-descripcion-formato.md` actualizada)
2. **Stage selectivo** — nunca `git add -A`. Arrastra `.playwright-mcp/`, `audit-en-pilot/`, `SPEC_*.md`, `logos-*.png`, `fix_translations_fase2.py` que son archivos previos a la sesión.
3. **No tocar archivos untracked existentes** (`?? .claude/`, `?? .playwright-mcp/`, `?? audit-en-pilot/`, etc.) — son del usuario.
4. **Reuso 100% de assets desde CB** → coste $0 (no generar imágenes nuevas con Nano Banana).
5. **No testing manual con tarjeta de prueba** — John apaga ordenador después de cada producto. Yo entrego código + paquete Stripe; John crea Payment Link + carga env var en Netlify; yo gatillo rebuild.

---

## Recent git log

```
ed68a86 chore: trigger Netlify rebuild to inject Plan Parrillero / Asador Stripe env var
ae9eae2 feat(productos): port Plan de Negocio Parrillero / Asador para Eventos (€45) — Bloque C 2/5
235cb8f chore: trigger Netlify rebuild to inject Plan Coctelería de Eventos Stripe env var
034862a feat(productos): port Plan de Negocio Coctelería de Eventos / Barra Móvil (€55) — abre Bloque C Línea B Gastro Móvil
8ab3511 chore: trigger Netlify rebuild to inject Plan Food Truck Stripe env var
2ffcac6 feat(productos): port Plan de Negocio Food Truck (€29) from chefbusiness.co — CIERRA Bloque B Línea A 5/5
```

Detalle completo en memoria: `session-2026-05-11-bloque-b-cerrado-bloque-c-2de5.md` (índice ya actualizado).
