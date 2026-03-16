# Kit de Escandallos Pro — Product Plan

## Product Definition

| Campo | Valor |
|-------|-------|
| **Nombre** | Kit de Escandallos Pro |
| **Slug** | `kit-escandallos` |
| **Formato** | Kit (plantillas Excel + guía PDF + dashboard) |
| **Audiencia** | Chefs, gerentes, dueños de restaurante, jefes de cocina, responsables de catering |
| **Problema** | Los profesionales pierden horas creando escandallos a mano, sin fórmulas fiables ni control real de food cost y mermas |
| **Precio lanzamiento** | €12 (badge: -75%) |
| **Precio "real"** | €49 |
| **Autor** | Chef John Guerrero |
| **Brand** | AI Chef Pro |
| **Dominio** | aichef.pro |
| **URL Landing** | aichef.pro/kit-escandallos |
| **URL Dashboard** | aichef.pro/kit-escandallos-library |

---

## Deliverables — Producto Principal

### 11 Plantillas Excel (.xlsx)

Cada plantilla incluye:
- Pestaña "Instrucciones" con guía paso a paso
- Fórmulas automáticas reales (no valores estáticos)
- Datos de ejemplo con ingredientes reales
- Mermas estándar precargadas por categoría de ingrediente
- Cálculo automático de Food Cost % y PVP sugerido
- Formato profesional (colores AI Chef Pro, listo para imprimir)
- Paneles congelados (header fijo al hacer scroll)
- Validación de datos (dropdowns para unidades de medida)

| # | Plantilla | Descripción | Ingredientes ejemplo |
|---|-----------|-------------|---------------------|
| 1 | **Escandallo Estándar (Plato a la Carta)** | El escandallo clásico para cualquier plato | Solomillo, salsa Pedro Ximénez, guarnición |
| 2 | **Escandallo Menú Degustación** | Multi-plato con coste por comensal | 5 pases: aperitivo, entrante, pescado, carne, postre |
| 3 | **Escandallo Menú del Día** | Primer plato + segundo + postre + bebida | Ensalada, pollo al horno, flan casero, agua/vino |
| 4 | **Escandallo Cocktails y Bebidas** | Para bar y mixología, con medidas en cl/ml | Gin Tonic premium, Mojito, Margarita, Spritz |
| 5 | **Escandallo Pastelería** | Mermas específicas de repostería, rendimiento por molde | Tarta de chocolate, croissants, macarons |
| 6 | **Escandallo Catering por Persona** | Coste por comensal × número de invitados | Catering cocktail 50 pax, banquete 100 pax |
| 7 | **Escandallo Cafetería/Brunch** | Desayunos, brunch, meriendas | Tostada aguacate, açaí bowl, eggs benedict |
| 8 | **Escandallo Food Truck** | Simplificado, con foco en velocidad y margen | Smash burger, loaded fries, pulled pork |
| 9 | **Control de Mermas por Categoría** | Registro semanal/mensual de mermas reales vs estándar | 15 categorías precargadas con merma típica |
| 10 | **Calculadora de PVP** | Introduce coste → obtén PVP por tipo de establecimiento | 6 tipos: fine dining, casual, fast casual, catering, café, food truck |
| 11 | **Dashboard Food Cost Mensual** | Resumen mensual: costes, ventas, food cost %, tendencia | Gráfico de barras con fórmulas, comparativa 12 meses |

### Estructura de columnas estándar por escandallo:

| Columna | Descripción | Tipo |
|---------|-------------|------|
| A | Ingrediente | Texto |
| B | Categoría | Dropdown (carne, pescado, verdura, etc.) |
| C | Unidad de compra | Dropdown (kg, L, ud, docena, etc.) |
| D | Precio por unidad de compra (€) | Número |
| E | Cantidad necesaria | Número |
| F | Unidad de uso | Dropdown |
| G | Merma (%) | Número (precargado por categoría) |
| H | Cantidad neta (tras merma) | Fórmula: =E×(1+G) |
| I | Coste neto (€) | Fórmula: =H×D (ajustado por unidad) |

**Filas finales:**
- **Coste total de ingredientes**: =SUMA(columna I)
- **Coste de elaboración** (% configurable, default 10%): fórmula
- **Coste total del plato**: ingredientes + elaboración
- **Food Cost objetivo** (%): input del usuario
- **PVP sugerido (sin IVA)**: =Coste total / Food Cost %
- **PVP con IVA** (10% hostelería España): =PVP × 1.10
- **Margen bruto** (€): =PVP - Coste total
- **Margen bruto** (%): fórmula

---

## Bonuses

### Bonus 1: "Guía: Controla tu Food Cost en 30 Días" (PDF)
**Valor percibido: €27**

Contenido:
1. Qué es el food cost y por qué es el KPI más importante
2. Cómo calcular tu food cost actual (fórmula + ejemplo)
3. Los 5 errores más comunes que disparan el food cost
4. Tabla de food cost objetivo por tipo de establecimiento
5. Plan de acción de 30 días (semana a semana)
6. Cómo reducir mermas sin afectar la calidad
7. Negociación con proveedores: 7 tácticas probadas
8. Checklist semanal de control de costes
9. Cómo usar las plantillas del Kit para el seguimiento
10. Caso práctico: restaurante que bajó su food cost del 38% al 28%

### Bonus 2: "Checklist de Control de Mermas + Inventario" (Excel)
**Valor percibido: €19**

2 pestañas:
- **Checklist de mermas**: registro diario/semanal por categoría, con comparativa vs merma estándar
- **Plantilla de inventario**: stock inicial, compras, stock final, consumo teórico vs real, diferencia

---

## Landing Page — Secciones

| # | Componente | Incluir | Notas |
|---|-----------|---------|-------|
| 1 | HeroSection | Sí | Titular enfocado en "ahorra horas" y "controla tu food cost" |
| 2 | ProductCover | Sí | Mockup de laptop con Excel abierto (o 3D de las plantillas) |
| 3 | ContentGrid | Sí | Las 11 plantillas en grid con icono + nombre |
| 4 | WhySection | Sí | 4 razones: fórmulas reales, todos los formatos, mermas precargadas, paga una vez |
| 5 | AuthorSection | Sí | Reutilizar foto y bio del Chef John |
| 6 | BonusSection | Sí | Los 2 bonuses con valor en € |
| 7 | FreeToolsSection | No | No aplica para este producto |
| 8 | BuyBox | Sí | CTA con precio €12 / ~~€49~~ |
| 9 | GuaranteeSection | Sí | 30 días, 100% reembolso |
| 10 | FaqAccordion | Sí | 6 FAQs específicas |
| 11 | CtaFinal | Sí | Checklist resumen + CTA final |
| 12 | TryPlatformBanner | Sí | Cross-sell a aichef.pro |
| 13 | StickyBar | Sí | Mobile CTA |
| 14 | AlreadyBought | Sí | Reenvío de acceso |

### FAQs propuestas:
1. **¿Necesito Excel avanzado?** — No, las plantillas vienen con todo configurado. Solo introduces tus datos.
2. **¿Funciona con Google Sheets?** — Sí, puedes importar los .xlsx a Google Sheets y las fórmulas se mantienen.
3. **¿Los datos de merma son fiables?** — Sí, son los estándares de la industria usados en hostelería profesional y consultoría.
4. **¿Puedo personalizar las plantillas?** — Totalmente. Añade ingredientes, cambia precios, ajusta mermas a tu realidad.
5. **¿Incluye actualizaciones?** — Sí, acceso de por vida al dashboard. Nuevas plantillas sin coste adicional.
6. **¿Hay garantía?** — 30 días de garantía. Si no te convence, te devolvemos el 100%.

---

## Dashboard — Funcionalidades

El comprador accede a un dashboard protegido con:

1. **Zona de descargas**: botones para descargar cada uno de los 11 Excel + PDF de la guía + Excel del bonus
2. **Vista previa**: preview de cada plantilla (nombre, descripción, qué incluye)
3. **Tabla de mermas**: referencia rápida con mermas estándar por categoría (consultable sin descargar)
4. **Tabla de food cost**: referencia de food cost objetivo por tipo de establecimiento
5. **Cross-sell**: banner a Pro Prompts eBook y a AI Chef Pro

---

## Pricing Strategy

```
Precio "real":           €49
Precio de lanzamiento:   €12
Badge de descuento:      -75%
Urgencia:                "Precio especial de lanzamiento. Sube pronto"
Propuesta de valor:      "11 plantillas profesionales por menos de lo que cuesta un menú del día"
```

---

## Technical Setup

### Stripe
- Crear producto "Kit de Escandallos Pro" en Stripe Dashboard
- Precio: €12 (pago único)
- Success URL: `https://aichef.pro/kit-escandallos-access?session_id={CHECKOUT_SESSION_ID}`
- Guardar link como `VITE_STRIPE_PAYMENT_LINK_ESCANDALLOS`

### Variables de entorno (Netlify)
```
VITE_STRIPE_PAYMENT_LINK_ESCANDALLOS=https://buy.stripe.com/xxx
EXCEL_KIT_ESCANDALLOS_URL=<url-del-zip-con-todos-los-excel>
PDF_FOOD_COST_GUIDE_URL=<url-de-la-guia-pdf>
EXCEL_MERMAS_INVENTARIO_URL=<url-del-bonus-excel>
```

### Rutas (App.tsx)
```tsx
<Route path="/kit-escandallos" element={<KitEscandallos />} />
<Route path="/kit-escandallos-access" element={<AccessGate />} />
<Route path="/kit-escandallos-library" element={
  <ProtectedRoute><KitEscandallosLibrary /></ProtectedRoute>
} />
```

### Functions
Reutilizar las existentes (verify-purchase, get-download-urls, resend-access) añadiendo soporte multi-producto con el campo `product` del JWT.

---

## Orden de Ejecución

1. ✅ Plan (este documento)
2. ⬜ Generar los 11 Excel + 1 Excel bonus con Python/openpyxl
3. ⬜ Generar contenido de la guía PDF (bonus 1)
4. ⬜ Crear componentes de landing page
5. ⬜ Crear dashboard
6. ⬜ Actualizar functions para multi-producto
7. ⬜ Añadir rutas
8. ⬜ Configurar Stripe
9. ⬜ Deploy y test

---

*Plan creado: 16 de marzo de 2026*
