# SESSION HANDOFF — 2026-05-14 → próxima sesión

## TL;DR
**Día 2 de productos nuevos post-paridad**. Cierra **Guía Panadería con Obrador €65 LIVE 100%** (Stripe inyectado, OG correcta, accesible en producción) + **fix crítico de testimonios** (coherencia avatar↔género↔nicho). **Pastelería €65** con research completo listo, pendiente arranque de producción mañana.

**HEAD git al cierre**: `967dd97` pusheado a `origin/main`. Tag respaldo: `producto-panaderia-live-fix-testimonios-2026-05-14`.

---

## 🎯 Tarea inmediata al retomar mañana

**Producto a producir: Cómo Montar una Pastelería €65**

Mensaje sugerido para arrancar mañana:
> Lee la memoria. Continuamos con la Guía Pastelería €65. El research completo está en `SESSION_HANDOFF_2026-05-14.md`. Confirma que sigues OK con €65 + 19 entregables y arrancamos directamente con el script de generación de entregables (mismo patrón Panadería).

---

## Estado al cierre 2026-05-14

### Productos NUEVOS post-paridad — progreso

| # | Producto | Fecha prevista | Status |
|---|---|---|---|
| 1 | Cómo Montar una Panadería con Obrador | Mayo 2026 | ✅ **LIVE 100%** (€65) |
| 2 | **Cómo Montar una Pastelería** | **Mayo 2026** | ⏳ **Research listo, arranque pendiente** |
| 3 | Cómo Montar una Chocolatería | Junio 2026 | ⏳ Pendiente |
| 4 | Manual del Chef Ejecutivo | Junio 2026 | ⏳ Pendiente |
| 5 | Manual del Manager de Restaurante | Julio 2026 | ⏳ Pendiente |
| 6 | Guía Food Cost + Ingeniería de Menú | Julio 2026 | ⏳ Pendiente |

### Lo cerrado hoy

1. **Sprint paridad CB→AICP 16/16 LIVE** — handoff `1477afb` (de la sesión 2026-05-13 que cerró al despertar 2026-05-14 AM).
2. **Guía Panadería con Obrador €65 LIVE** — `fc86944` (código) + `8bf2a18` (rebuild trigger Stripe). 19 entregables + 6 imágenes Nano Banana 2 + 14 archivos React + 4 configs cableados. Eliminado de "Coming Soon".
3. **Fix crítico testimonios Panadería** — `967dd97`. 8 testimonios con coherencia perfecta nombre↔género↔atuendo nicho. Avatar nuevo mujer panadera generado ($0.07).
4. **3 reglas operativas nuevas** guardadas en memoria (ver MEMORY.md):
   - Research previo obligatorio para producto nuevo
   - Fuente de verdad LIVE vs plan (no confundir carpeta plan con estado real)
   - Coherencia avatar↔género↔nicho en testimonios

### Costes Nano Banana 2 del día: **$0.47**

---

## 📚 RESEARCH COMPLETO PASTELERÍA — listo para usar mañana

> Este research ya está hecho. NO reinvestigar. Solo retomar y arrancar producción cuando John dé OK al precio €65.

### 1. Sub-conceptos del nicho

| Modelo | Inversión | Notas |
|---|---|---|
| **Pastelería tradicional con obrador + tienda** | €120-200K | Modelo de referencia para la guía. Bollería + repostería + tartas por encargo |
| **Pastelería de autor / boutique** (Oriol Balaguer, Hofmann) | €150-280K | Premium, ticket alto, marca personal |
| **Pastelería de eventos / B2B bodas** | €100-180K + logística | Foco bodas + comuniones + corporate. Tarta 4-7€/pax |
| **Pastelería-cafetería / salón de té** | €150-250K | Cross-sell consumo in situ |
| **Micropastelería en casa (RD 102/2022)** | €15-40K | Entry low cost, online + encargo |

**Decisión Guía**: modelo principal = tradicional con obrador + tienda, capítulo dedicado a B2B bodas (la gran diferencia frente a Panadería).

### 2. Diferencia esencial Pastelería vs Panadería (ya LIVE)

| | Panadería | Pastelería |
|---|---|---|
| Producto core | Pan + bollería básica | Repostería + tartas + bombonería + bollería fina |
| Cadena B2B | Horeca (hoteles, restaurantes) | **Bodas, eventos, comuniones (estacional fuerte)** |
| Food cost | 18-22% | **22-28%** (chocolate, mantequilla, frutos secos premium) |
| Margen personal | 28-32% | **30-36%** (mano de obra más cualificada) |
| Equipamiento killer | Horno piso/rotativo + masa madre | **Abatidor de temperatura** (CRÍTICO) + atemperadora chocolate |
| Casos referencia | Levaduramadre, Panic, Crustó, Hofmann (panadería) | Hofmann (pastelería), Oriol Balaguer, Escribà, Bubó, Lluc Crusellas |

### 3. Regulación España 2026 (igual que Panadería + 3 específicos)

- **APPCC con temperaturas críticas** (crema pastelera 75°C, abatimiento <10°C en 90 min, cadena frío crema fresca/nata)
- **Cumplimiento cadena de frío reforzada** (nata, huevo crudo en mousses, lácteos)
- **RD 102/2022 micropastelería en casa** (opción entry para emprendedoras desde domicilio)
- Resto igual: RGSEAA, licencia clasificada salida humos, APPCC, IAE 644.1, manipulador, Verifactu 2027, control horario digital 2026

### 4. Equipamiento crítico (diferencia de Panadería)

| Equipo | Rango precio 2026 | Nota |
|---|---|---|
| **Horno de convección 6-10 bandejas con humidificador** | €4.500-12.000 | Unox, Mychef, Romag |
| **Abatidor de temperatura ⭐CRÍTICO** | €4.000-9.000 | Killer del nicho — sin esto no hay pastelería seria |
| **Batidora planetaria 20-60L** | €2.500-7.500 | Ferneto BTF/BTI, Kenwood, Hobart |
| **Atemperadora de chocolate** | €3.500-9.000 | Valrhona / Callebaut compatible |
| **Cámara fermentación croissant/hojaldre** | €5.000-12.000 | Igual que panadería |
| **Pasteurizador (si helados)** | €4.000-9.000 | Opcional |
| **Cámaras refrigeradas + congelador** | €5.000-11.000 | Doble: positiva semifríos + negativa congelados |
| **Vitrina expositora refrigerada pastelería** | €5.000-12.000 | Más alta calidad que panadería |
| **Robot pastelero pro** | €1.500-4.000 | Apoyo |

### 5. Proveedores reales 2026

- **Maquinaria**: Dispan, Coolvi, Romag, Unox, Mychef, Ferneto, La Casa del Chef
- **Chocolate pro**: Valrhona, Callebaut, Cacao Barry
- **Ingredientes técnicos**: Sosa Ingredients (líder gel/glaseado/gelificantes pro), Italfeed
- **Congelados pro**: Bridor (croissant + brioche), Pastryking
- **Decoración**: PME, Wilton, Decora
- **Frutos secos**: Damasc, Frusan, Borges

### 6. Modelo de negocio (Pastelería 70-90 m²)

- Ticket medio mostrador: **€5,80-9,00** (más alto que panadería)
- Tickets/día: 80-160 + B2B encargos
- Facturación anual: **€340-520K** (mostrador) + **€60-180K** (B2B bodas/eventos)
- Tarta boda: **€4-7/pax** (50 pax → €250-350; 150 pax → €750-1.050)
- Food cost: 22-28%
- Margen bruto: 45-58%
- Personal: 30-36% facturación
- Break-even: 9-15 meses
- **Estacionalidad**: picos Navidad (turrón + roscón Reyes) + Pascua (monas) + mayo-junio (comuniones) + verano-otoño (bodas)

### 7. Casos éxito de referencia

| Marca | Ciudad | Hecho diferencial |
|---|---|---|
| **Hofmann** | BCN | Mejor Croissant Artesano Mantequilla 2010. 750 croissants/día solo en local Born = 22.000/mes |
| **Oriol Balaguer (La Duquesita)** | Madrid + BCN | Mejor Confitería Madrid. 5 locales BCN + 3 Madrid. Panettone de referencia |
| **Christian Escribà** | BCN | Pastelería de autor desde 1906 |
| **Bubó (Carles Mampel)** | BCN | Vanguardia, premios internacionales |
| **Lluc Crusellas** | BCN | Campeón Mundial Pastelería 2022 |
| **Ricardo Vélez (Moulin Chocolat)** | Madrid | Repostería francesa tradicional |
| **Espai Sucre** | BCN | Pastelería gastronómica + escuela |

### 8. Documentación específica del nicho (19 entregables propuestos)

**Específicos pastelería** (sin equivalente en Panadería):
1. **Recetario maestro pastelería** — 15 recetas técnicas con gramajes y procesos: croissant Hofmann + hojaldre + milhojas + ópera + Sacher + tarta Tatín + mousse chocolate + tres chocolates + fraisier + tartaleta limón + tartaleta frutas + roscón Reyes + panettone + Mona Pascua + brazo gitano
2. **Calculadora escandallos por tarta + porción** (Excel con Sacher, ópera, red velvet, etc.)
3. **Plan eventos B2B bodas + comuniones** (Excel): pricing 4-7€/pax + extras + transporte + montaje + cronograma día evento
4. **APPCC pastelería con temperaturas críticas** (abatimiento crema 75→10°C en 90min, cadena frío)
5. **Calendario estacional anual** (Navidad → Reyes → San Valentín → Pascua → comuniones → bodas → vuelta cole → Todos Santos huesos de santo)
6. **Calculadora coste energético** (horno convección + abatidor + cámaras → +25-35% más caro que panadería)
7. **Plan de carta 30 referencias** (rotación + estacionales + clásicos + autor)
8. **Checklist abatidor de temperatura + cadena frío** (el distintivo killer)
9. **Plantilla contrato B2B bodas** (incluye anulación + cambio diseño + transporte + montaje + horario entrega)
10. **Calculadora margen por línea** (mostrador vs encargo vs B2B bodas)

**Reutilizables del template Casual/Panadería** (con datos adaptados a pastelería):
- Plan financiero 3 años, CAPEX, P&L escenarios, cash flow, Gantt, turnos brigada, escandallo maestro, business plan modelo, manual operaciones, 6 checklists.

### Precio sugerido: **€65** alineado con Panadería + Casual

Mismo ticket, mismo nivel de profundidad. NO subimos a €75 para cross-sell natural con Panadería.

---

## 🛠️ Plan paso a paso para mañana (workflow probado)

1. **Confirmación user** del precio €65 + 19 entregables (debería ser inmediata).
2. **Crear carpeta destino**: `public/dl/guia-pasteleria/`
3. **Generar DOCX maestro** con script `/tmp/gen_guia_pasteleria_docx.py` (20 cap específicos pastelería, ~30K chars). Patrón: `gen_guia_panaderia_docx.py` adaptado.
4. **Generar 9 plantillas Excel + 6 checklists** con `/tmp/gen_guia_pasteleria_excels.py` + `gen_guia_pasteleria_checklists.py`. Patrón Panadería adaptado.
5. **Generar PDF placeholder** (1 página redirigiendo al DOCX, igual que Panadería).
6. **Generar 6 imágenes Nano Banana 2** con `/tmp/gen_imagenes_pasteleria.py` (1 hero 16:9 + 5 gallery 1:1). **Importante**: prompts coherentes con nicho pastelería (vitrina con tartas, atemperadora chocolate, pastelero con uniforme blanco, milhojas, croissant Hofmann-style, ambiente pastelería boutique). Coste $0.40.
7. **Crear 14 archivos React** `src/components/guia-pasteleria/` (10 components) + `src/pages/GuiaPasteleria*.tsx` (3 pages) + `src/data/testimonials-guia-pasteleria.ts`. Patrón Panadería con adaptaciones.
8. **APLICAR REGLA TESTIMONIOS desde el primer momento**: 8 testimonios con coherencia género nombre ↔ género avatar ↔ atuendo del nicho pastelero. Mapping orientativo:
   - 4 mujeres + 4 hombres balance
   - Probablemente generar 1-2 avatares nuevos pastelero/pastelera con Nano Banana 2 ($0.07-0.14)
   - Avatar-4 (mujer chef gorro) y avatar-8 (chef maduro) son los más cercanos al nicho de los existentes
9. **Wire 4 configs**:
   - `src/data/productos-digitales-config.ts` (entrada con 19 file paths)
   - `src/App.tsx` (3 rutas: landing + access + library ProtectedRoute)
   - `netlify/edge-functions/og-meta.ts` (entrada SEO)
   - `src/pages/ProductosDigitales.tsx` (card LIVE + ELIMINAR de "Coming Soon" Mayo 2026)
10. **Build local** (`npm run build`) → verde
11. **Stage selectivo** (NO `git add -A`)
12. **Commit + push** a `origin/main`
13. **Paquete Stripe a John**:
    - Nombre: `Cómo Montar una Pastelería — Guía Completa España 2026`
    - Precio: `65 EUR`
    - Descripción ≤260 chars (verificar con `python3 -c "print(len('...'))"`)
    - Confirmation URL: `https://aichef.pro/guia-pasteleria-access?session_id={CHECKOUT_SESSION_ID}`
    - Env var: `VITE_STRIPE_PAYMENT_LINK_GUIA_PASTELERIA`
14. **Cuando John pase Stripe link**: commit vacío `chore: trigger Netlify rebuild` + push → LIVE en producción ~2-3 min.

**Tiempo estimado total**: 60-90 min desde arranque hasta paquete Stripe.

---

## ⚠️ Reglas no negociables (memoria viva, leer al arrancar)

1. **Descripciones Stripe ≤260 caracteres ESTRICTO**, párrafo en prosa, sin bullets.
2. **Stage selectivo** — nunca `git add -A`. Arrastra untracked previos (`.playwright-mcp/`, `SPEC_*.md`, `audit-en-pilot/`, `logos-*.png`, `fix_translations_fase2.py`, `email-campaigns/HANDOFF.md`).
3. **No tocar archivos untracked existentes** en raíz (son del user).
4. **Reuso de assets cuando posible** ($0). Para nuevos productos NUEVOS generamos imágenes con Nano Banana 2 ($0.40 por producto + opcional $0.07-0.14 avatares nicho).
5. **No testing manual con tarjeta de prueba**. John crea Stripe + carga env; yo escribo código + commit + trigger rebuild.
6. **Netlify env scope: VITE_* = "Builds only"** (AWS Lambda 4 KB env limit).
7. **🚨 Coherencia testimonios obligatoria** desde el primer commit (regla nueva guardada hoy).
8. **Research previo obligatorio** para producto NUEVO — 8 bloques + esperar OK del user antes de codificar (regla nueva guardada hoy).

---

## Recent git log

```
967dd97 fix(testimonios): coherencia avatar↔género↔nicho en Guía Panadería €65
8bf2a18 chore: trigger Netlify rebuild to inject VITE_STRIPE_PAYMENT_LINK_GUIA_PANADERIA_OBRADOR env var
fc86944 feat(productos): NEW Cómo Montar una Panadería con Obrador €65 — Guía Premium 1er producto investigado desde cero post-sprint paridad
1477afb docs: session handoff 2026-05-13 — Sprint paridad CB→AICP CERRADO 16/16 LIVE 100%
be2e7a6 chore: force fresh Netlify build
```

## Tag git de respaldo
`producto-panaderia-live-fix-testimonios-2026-05-14` apuntando a `967dd97`.

## Memorias relevantes para retomar
- `reference_plan-productos-digitales-2026.md` — plan maestro 6 productos nuevos + 9 ejes
- `feedback_research-previo-producto-nuevo.md` — checklist research obligatorio
- `feedback_testimonios-coherencia-avatar-genero-nicho.md` — regla testimonios
- `feedback_fuente-verdad-productos-live-vs-plan.md` — no confundir plan con estado
- `session-2026-05-14-panaderia-live-fix-avatares-y-pasteleria-pendiente.md` — log de la sesión de hoy
