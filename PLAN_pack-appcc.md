# Pack de Plantillas APPCC — Product Plan

## Product Definition
- **Name**: Pack de Plantillas APPCC
- **Slug**: `pack-appcc`
- **Format**: kit (Excel templates + PDF guides)
- **Price**: €14 (launch) / ~~€29~~ (strikethrough)
- **Audience**: Todo restaurante, bar, cafetería, hotel, catering, obrador en España
- **Problem**: La normativa APPCC es obligatoria por ley (RD 1021/2022, Reglamento UE 1169/2011). Las inspecciones de Sanidad pueden cerrar tu negocio. La mayoría de establecimientos usan hojas fotocopiadas de hace 10 años o directamente no tienen nada. Crear los registros desde cero lleva semanas.
- **Tagline**: "Pasa la inspección de Sanidad con nota — todo lo que la ley te exige, listo para usar"

## Deliverables (15 plantillas + 2 bonus)

### Excel Templates (.xlsx) — 12 archivos
1. **Registro de Temperaturas Diario** — Cámaras frigoríficas, congeladores, exposición caliente/fría. Alertas automáticas si sale de rango.
2. **Registro de Temperaturas Recepción** — Control en recepción de mercancías con límites por tipo de producto.
3. **Plan de Limpieza y Desinfección** — Calendario semanal/mensual por zona (cocina, sala, baños, almacén). Checklist con responsable y firma.
4. **Registro de Limpieza Diaria** — Checklist diario por turno con verificación y firma.
5. **Checklist Recepción de Mercancías** — Verificación estado, temperatura, caducidad, etiquetado, lote, proveedor.
6. **Registro de Trazabilidad** — Entrada/salida de productos con lote, proveedor, fecha, cantidad.
7. **Control de Plagas** — Registro de actuaciones DDD (desinsectación, desratización, desinfección), plano de cebos, calendario revisiones.
8. **Matriz de Alérgenos** — Los 14 alérgenos obligatorios × platos de tu carta. Con desplegables Sí/No/Trazas y leyenda de iconos.
9. **Control de Aceite de Fritura** — Registro de cambios, test de acidez, temperatura máxima, tipo de aceite.
10. **Control de Agua** — Registros de potabilidad, análisis periódicos, tratamiento.
11. **Registro de Acciones Correctivas** — Incidencias, causa, medida adoptada, verificación, responsable, fecha cierre.
12. **Hoja de Análisis de Peligros HACCP** — Identificación de peligros por fase (recepción, almacenamiento, preparación, cocción, servicio), puntos críticos de control, límites, vigilancia, acciones correctivas.

### PDF Guides — 3 archivos
13. **Guía: Cómo Pasar una Inspección de Sanidad** (PDF ~30 pp) — Los 25 puntos que revisa el inspector, errores que causan sanción inmediata, cómo prepararte, qué documentos tener listos.
14. **Fichas de los 14 Alérgenos** (PDF) — Fichas imprimibles para cocina/sala con iconos, nombre, dónde se encuentran, síntomas. Formato A4 para pegar en cocina.
15. **Checklist de Higiene Personal** (PDF) — Cartel imprimible para vestuario + registro de formación en manipulación de alimentos.

### BONUS
- **Bonus 1**: Plantilla de Formación en Seguridad Alimentaria — Registro de formación del personal con fechas, contenido, certificados (valor percibido: €9)
- **Bonus 2**: Cartel "Protocolo de Actuación ante Alerta Alimentaria" — PDF imprimible A3 con el protocolo paso a paso ante intoxicación o alerta (valor percibido: €7)

## Content Outline

### Categorías para ContentGrid (landing page)
1. **Control de Temperaturas** (2 plantillas) — Registro diario + recepción
2. **Limpieza y Desinfección** (2 plantillas) — Plan + registro diario
3. **Recepción y Trazabilidad** (2 plantillas) — Checklist + registro lotes
4. **Alérgenos** (2 archivos) — Matriz Excel + fichas PDF
5. **Controles Especiales** (2 plantillas) — Aceite fritura + agua
6. **Gestión HACCP** (2 archivos) — Análisis peligros + acciones correctivas
7. **Control de Plagas** (1 plantilla) — Registro DDD
8. **Guía de Inspección** (1 PDF) — Los 25 puntos del inspector
9. **Bonus** (2 archivos) — Formación + protocolo alertas

## Landing Page Sections
- HeroSection (urgency: "obligatorio por ley")
- ProductCover (mockup 3D del pack con iconos de plantillas)
- CompatibleAppsMarquee (variant: "appcc" — Excel, Google Sheets, PDF, imprimir)
- ContentGrid (9 categorías arriba)
- TestimonialsMarquee (hosteleros que han pasado inspecciones)
- WhySection (4 razones: obligatorio, multas, tranquilidad, profesionalidad)
- AuthorSection (Chef John — 29 años + 15 consultoría)
- BonusSection (2 bonus)
- FreeToolsSection (shared)
- BuyBox
- GuaranteeSection (30 días)
- FaqAccordion (6-7 preguntas)
- CtaFinal
- TryPlatformBanner (shared)
- StickyBar (mobile)

## Dashboard Features
- 17 tarjetas de descarga (15 plantillas + 2 bonus) en grid
- Agrupadas por categoría con iconos
- Botón descarga directa por archivo
- Cross-sell banner → Kit de Escandallos + Pro Prompts
- Banner "Compatibles con Excel, Google Sheets, LibreOffice, Numbers + PDF imprimible"

## Pricing Strategy
- Launch: **€14**
- Strikethrough: ~~€29~~
- Badge: "52% dto. lanzamiento"
- Urgency: "Precio de lanzamiento por tiempo limitado"
- Anchor: "Menos de €1 por plantilla"

## Technical Setup

### Stripe
- Product: "Pack de Plantillas APPCC — AI Chef Pro"
- Price: €14.00 one-time
- Payment Link success_url: `https://aichef.pro/pack-appcc-access?session_id={CHECKOUT_SESSION_ID}`

### Environment Variables (Netlify)
- `VITE_STRIPE_PAYMENT_LINK_APPCC` — Payment Link URL (All scopes)
- `PACK_APPCC_URLS` — JSON object with download URLs (Functions scope)

### Routes (App.tsx)
- `/pack-appcc` → PackAppcc (landing)
- `/pack-appcc-access` → PackAppccAccessGate
- `/pack-appcc-library` → ProtectedRoute(storageKey="pack-appcc-jwt") + PackAppccDashboard

### Files
- Excel templates: `public/dl/pack-appcc/` (descriptive names) → copy to `public/dl/ap-XXXX.xlsx` (obfuscated)
- Landing components: `src/components/pack-appcc/`
- Dashboard: `src/pages/PackAppccDashboard.tsx`
- Access gate: `src/pages/PackAppccAccessGate.tsx`
- Testimonials: `src/data/testimonials-appcc.ts`

### Netlify Functions
- Reuse existing multi-product functions (verify-purchase, resend-access, get-download-urls)
- Add `'pack-appcc'` product config to PRODUCTS map in verify-purchase.ts
- Add `'pack-appcc'` handling in get-download-urls.ts (reads PACK_APPCC_URLS env var)
- Add `'pack-appcc'` email template in resend-access.ts

## SEO Keywords
Primary: "plantillas APPCC restaurante", "registros APPCC hostelería", "plantilla control temperaturas restaurante"
Secondary: "carta alérgenos obligatoria", "registro limpieza restaurante", "inspección sanidad restaurante"
Brand: "AI Chef Pro APPCC", "pack APPCC hostelería"
