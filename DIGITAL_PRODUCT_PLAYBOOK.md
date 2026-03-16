# Digital Product Playbook — Sistema Replicable de Productos Digitales

> Flujo de trabajo completo para crear, vender y entregar productos digitales.
> Probado en producción con **Pro Prompts eBook** (aichef.pro/pro-prompts-ebook).

---

## Resumen del Stack

| Capa | Tecnología | Propósito |
|------|-----------|-----------|
| **Frontend** | React 18 + TypeScript + Vite | Landing page + Dashboard |
| **Estilos** | Tailwind CSS + shadcn/ui | UI premium, dark theme, gold accents |
| **Hosting** | Netlify (auto-deploy desde main) | CDN global, SSL, functions |
| **Pago** | Stripe Payment Links | Checkout hosted, sin backend propio |
| **Email** | Resend API | Emails transaccionales (magic link) |
| **Auth** | JWT (jsonwebtoken) | Tokens de 365 días, sin base de datos |
| **Almacenamiento** | localStorage | Persistencia de sesión en el navegador |

---

## Arquitectura del Sistema

```
┌─────────────────────────────────────────────────────────────┐
│                    LANDING PAGE                              │
│  /[producto]                                                │
│  Hero → Contenido → Autor → Bonos → CTA → FAQ → CTA Final │
│                         ↓                                    │
│              Botón "COMPRAR" → Stripe Payment Link           │
└─────────────────────────────────────────────────────────────┘
                          ↓
┌─────────────────────────────────────────────────────────────┐
│                 STRIPE CHECKOUT (hosted)                     │
│  Stripe cobra → redirige a success_url con session_id       │
└─────────────────────────────────────────────────────────────┘
                          ↓
┌─────────────────────────────────────────────────────────────┐
│              ACCESS GATE (/[producto]-access)                │
│  1. Recibe session_id o jwt en query params                 │
│  2. Llama a verify-purchase (Netlify Function)              │
│  3. verify-purchase:                                        │
│     - Consulta Stripe API → confirma pago                   │
│     - Genera JWT (365 días)                                 │
│     - Envía email con magic link via Resend                 │
│  4. Guarda JWT en localStorage                              │
│  5. Redirige al dashboard protegido                         │
└─────────────────────────────────────────────────────────────┘
                          ↓
┌─────────────────────────────────────────────────────────────┐
│           DASHBOARD PROTEGIDO (/[producto]-library)         │
│  ProtectedRoute verifica JWT en localStorage                │
│  - Contenido del producto (prompts, plantillas, etc.)       │
│  - Descargas (PDF, Excel, Word) via get-download-urls       │
│  - Cross-sell a otros productos / plataforma principal      │
└─────────────────────────────────────────────────────────────┘
                          ↓
┌─────────────────────────────────────────────────────────────┐
│              REENVÍO DE ACCESO (re-entry)                   │
│  Footer de landing: "¿Ya compraste? Reenviar acceso"        │
│  1. Usuario pone email                                      │
│  2. resend-access busca en Stripe si hay compra             │
│  3. Si existe: genera nuevo JWT + envía email               │
│  4. Si no existe: error 404                                 │
└─────────────────────────────────────────────────────────────┘
```

---

## Paso a Paso para Replicar

### FASE 1: Preparación (Día 1)

#### 1.1 Definir el producto
- **Nombre del producto**: ej. "Kit de Escandallos Pro"
- **Formato**: ebook, guía, plantillas, kit, diccionario, etc.
- **Precio**: definir precio de lanzamiento y precio final
- **Bonos**: 2-3 bonus que aumenten el valor percibido
- **Contenido descargable**: qué archivos recibirá el comprador (PDF, Excel, etc.)

#### 1.2 Crear el Stripe Payment Link
1. Ir a Stripe Dashboard → Payment Links
2. Crear producto con nombre, precio y descripción
3. Configurar `success_url`: `https://tudominio.com/[producto]-access?session_id={CHECKOUT_SESSION_ID}`
4. Copiar el link generado (ej. `https://buy.stripe.com/xxx`)
5. Guardar en Netlify env vars como `VITE_STRIPE_PAYMENT_LINK`

#### 1.3 Configurar Resend
1. Crear cuenta en resend.com
2. Verificar dominio (DNS records)
3. Generar API key
4. Guardar en Netlify env vars como `RESEND_API_KEY`

#### 1.4 Variables de entorno en Netlify
```
STRIPE_SECRET_KEY=sk_live_...
JWT_SECRET=<string-aleatorio-32+-caracteres>
RESEND_API_KEY=re_...
PDF_EBOOK_URL=<url-del-archivo-principal>
PDF_BONUS1_URL=<url-bonus-1>
PDF_BONUS23_URL=<url-bonus-2>
VITE_STRIPE_PAYMENT_LINK=https://buy.stripe.com/...
VITE_SITE_URL=https://tudominio.com
```

---

### FASE 2: Landing Page (Días 2-3)

#### 2.1 Estructura de componentes
Crear directorio: `src/components/[producto]/`

| # | Componente | Función | Prioridad |
|---|-----------|---------|-----------|
| 1 | **HeroSection** | Titular + subtítulo + precio + CTA principal | Alta |
| 2 | **BookCover** | Mockup visual del producto (3D, flat, etc.) | Alta |
| 3 | **CategoriesGrid** | Qué incluye el producto (categorías/módulos) | Alta |
| 4 | **WhySection** | 4 razones para comprar + compatibilidad | Alta |
| 5 | **AuthorSection** | Bio del autor + credenciales | Media |
| 6 | **BonusSection** | Bonus 1, 2, 3 con valor en € | Alta |
| 7 | **FreeToolsSection** | Herramientas gratuitas incluidas (si aplica) | Media |
| 8 | **BuyBox** | CTA secundario con precio + badges | Alta |
| 9 | **GuaranteeSection** | Garantía de devolución (30 días) | Alta |
| 10 | **FaqAccordion** | 5-7 preguntas frecuentes | Media |
| 11 | **CtaFinal** | CTA final con checklist resumen | Alta |
| 12 | **TryPlatformBanner** | Cross-sell a la plataforma principal | Media |
| 13 | **StickyBar** | CTA fijo en móvil (bottom bar) | Alta |
| 14 | **AlreadyBought** | Formulario de reenvío de acceso (footer) | Media |
| 15 | **PaymentBadges** | Badge de Stripe + métodos de pago | Baja |
| 16 | **FadeIn** | Wrapper de animación (IntersectionObserver) | Baja |

#### 2.2 Página orquestadora
Crear `src/pages/[Producto].tsx` que importa todos los componentes en orden:

```tsx
export default function MiProducto() {
  return (
    <div className="min-h-screen bg-[#0a0a0a]">
      <HeroSection />
      <BookCover />
      <CategoriesGrid />
      <WhySection />
      <AuthorSection />
      <BonusSection />
      <FreeToolsSection />
      <BuyBox />
      <GuaranteeSection />
      <FaqAccordion />
      <CtaFinal />
      <TryPlatformBanner />
      <footer>...</footer>
      <StickyBar />
    </div>
  );
}
```

#### 2.3 Elementos de confianza imprescindibles
- **Social proof**: avatar stack + estrellas (mínimo 4.5/5)
- **Autor con foto real**: nombre, bio corta, credenciales
- **Garantía**: 30 días, sin preguntas, 100% reembolso
- **Badges de pago**: Stripe + tarjetas + Apple Pay
- **Precio tachado**: siempre mostrar el "valor real" vs precio de lanzamiento
- **Badge de descuento**: `-XX%` visible junto al precio

---

### FASE 3: Backend / Functions (Día 3)

#### 3.1 verify-purchase.ts
```
netlify/functions/verify-purchase.ts
```
**Lógica**:
1. Si recibe `session_id` → consulta Stripe, verifica pago, genera JWT, envía email
2. Si recibe `jwt` → verifica firma, retorna token existente
3. JWT payload: `{ email, product: '[producto-id]' }`, expira en 365 días

#### 3.2 get-download-urls.ts
```
netlify/functions/get-download-urls.ts
```
**Lógica**:
1. Recibe JWT en header `Authorization: Bearer {token}`
2. Verifica firma
3. Retorna URLs de descarga desde env vars

#### 3.3 resend-access.ts
```
netlify/functions/resend-access.ts
```
**Lógica**:
1. Recibe email en POST body
2. Busca en Stripe si hay sesión pagada con ese email
3. Si existe: genera JWT nuevo + envía email via Resend
4. Si no existe: retorna 404

#### 3.4 Template del email (Resend)
```html
<div style="background:#0a0a0a; padding:40px; text-align:center;">
  <h1 style="color:#FFD700;">Tu acceso a [Producto]</h1>
  <p style="color:#ccc;">Haz clic para acceder a tu contenido</p>
  <a href="https://tudominio.com/[producto]-access?jwt={TOKEN}"
     style="background:#FFD700; color:#000; padding:16px 32px; border-radius:8px;">
    Acceder Ahora
  </a>
  <p style="color:#888;">Guarda este email. Enlace válido por 12 meses.</p>
</div>
```

---

### FASE 4: Dashboard (Días 4-5)

#### 4.1 Estructura del dashboard
Crear directorio: `src/components/library/`

| Componente | Función |
|-----------|---------|
| **TopBar** | Header con logo + badge del producto |
| **FloatingGallery** | Background animado (opcional, premium feel) |
| **DownloadsSection** | Botones de descarga (PDF, Excel, Word) |
| **CompatibilityBanner** | Plataformas compatibles (si aplica) |
| **ContentGrid** | Grid principal del contenido (prompts, plantillas, etc.) |
| **ContentCard** | Tarjeta individual de cada item |
| **ContentModal** | Modal de detalle + copiar/descargar |
| **CtaToApp** | Cross-sell a la plataforma principal |

#### 4.2 Auth y protección
- **useAuth hook**: lee JWT de localStorage, decodifica payload, verifica expiración
- **ProtectedRoute**: wrapper que redirige a landing si no hay JWT válido
- **AccessGate page**: recibe session_id o jwt, llama a verify-purchase, guarda token

#### 4.3 Datos del producto
```typescript
// src/data/[producto].ts
interface Item {
  id: number;
  title: string;
  text: string;           // contenido completo
  compatible?: string[];  // plataformas compatibles (si aplica)
}

interface Category {
  id: string;
  title: string;
  itemCount: number;
  items: Item[];
}

export const categories: Category[] = [...]
```

---

### FASE 5: Rutas y Deploy (Día 5)

#### 5.1 Agregar rutas en App.tsx
```tsx
<Route path="/[producto]" element={<MiProductoLanding />} />
<Route path="/[producto]-access" element={<AccessGate />} />
<Route path="/[producto]-library" element={
  <ProtectedRoute><MiProductoDashboard /></ProtectedRoute>
} />
```

#### 5.2 SEO (Helmet)
```tsx
<Helmet>
  <title>[Título] | [Brand]</title>
  <meta name="description" content="[descripción 150 chars]" />
  <meta name="robots" content="index, follow" />
  <meta property="og:title" content="[título OG]" />
  <meta property="og:description" content="[descripción OG]" />
  <link rel="canonical" href="https://tudominio.com/[producto]" />
</Helmet>
```

#### 5.3 Checklist pre-deploy
- [ ] Stripe Payment Link creado y testeado
- [ ] Variables de entorno en Netlify
- [ ] Archivos descargables subidos (PDF, Excel, etc.)
- [ ] Email template con magic link correcto
- [ ] ProtectedRoute redirige correctamente
- [ ] StickyBar funciona en móvil
- [ ] Precio y descuento correctos
- [ ] Garantía de devolución visible
- [ ] Open Graph tags para compartir en redes
- [ ] Flujo completo probado: compra → email → magic link → dashboard

---

### FASE 6: Post-lanzamiento

#### 6.1 Verificaciones
- [ ] Compra de prueba (€9 → refund)
- [ ] Email llega correctamente (revisar Resend dashboard)
- [ ] Magic link funciona
- [ ] Descargas funcionan
- [ ] Reenvío de acceso funciona
- [ ] Mobile responsive OK

#### 6.2 Métricas a seguir
- **Stripe**: ventas, ingresos, refunds
- **Resend**: emails enviados, tasa de apertura
- **Analytics**: visitas landing, tasa de conversión, scroll depth
- **Dashboard**: accesos, descargas

---

## Dependencias NPM Requeridas

```json
{
  "stripe": "^20.x",
  "jsonwebtoken": "^9.x",
  "@types/jsonwebtoken": "^9.x",
  "react-helmet-async": "^1.x",
  "lucide-react": "latest",
  "tailwindcss": "latest"
}
```

---

## Estructura de Archivos (Template)

```
src/
├── pages/
│   ├── [Producto]Landing.tsx          # Orquestador de landing
│   ├── [Producto]Dashboard.tsx        # Orquestador de dashboard
│   └── AccessGate.tsx                 # Gate de verificación (reutilizable)
├── components/
│   ├── [producto]/                    # Componentes de landing
│   │   ├── HeroSection.tsx
│   │   ├── BookCover.tsx
│   │   ├── CategoriesGrid.tsx
│   │   ├── WhySection.tsx
│   │   ├── AuthorSection.tsx
│   │   ├── BonusSection.tsx
│   │   ├── BuyBox.tsx
│   │   ├── GuaranteeSection.tsx
│   │   ├── FaqAccordion.tsx
│   │   ├── CtaFinal.tsx
│   │   ├── StickyBar.tsx
│   │   ├── AlreadyBought.tsx
│   │   ├── PaymentBadges.tsx
│   │   └── FadeIn.tsx
│   ├── library/                       # Componentes de dashboard
│   │   ├── TopBar.tsx
│   │   ├── DownloadsSection.tsx
│   │   ├── ContentGrid.tsx
│   │   ├── ContentCard.tsx
│   │   ├── ContentModal.tsx
│   │   └── CtaToApp.tsx
│   └── shared/
│       └── ProtectedRoute.tsx         # Reutilizable entre productos
├── hooks/
│   └── useAuth.ts                     # Reutilizable entre productos
├── data/
│   └── [producto].ts                  # Datos del contenido
netlify/
└── functions/
    ├── verify-purchase.ts             # Reutilizable (parametrizar producto)
    ├── get-download-urls.ts           # Reutilizable (parametrizar URLs)
    └── resend-access.ts               # Reutilizable (parametrizar producto)
```

---

## Tiempos Estimados por Fase

| Fase | Descripción | Con este playbook |
|------|-------------|-------------------|
| 1 | Preparación (Stripe, Resend, env vars) | 1-2 horas |
| 2 | Landing page (componentes) | 3-5 horas |
| 3 | Backend functions | 1-2 horas (copiar + adaptar) |
| 4 | Dashboard | 2-4 horas |
| 5 | Rutas, SEO, deploy | 1 hora |
| 6 | Testing y ajustes | 1-2 horas |
| **Total** | **Producto completo** | **~1-2 días** |

> Nota: el primer producto (Pro Prompts eBook) tomó ~3 sesiones de trabajo.
> Los siguientes deberían tomar significativamente menos al reutilizar componentes.

---

## Componentes 100% Reutilizables (sin cambios)

- `FadeIn.tsx` — animación de entrada
- `PaymentBadges.tsx` — badge de Stripe
- `ProtectedRoute.tsx` — protección de rutas
- `useAuth.ts` — hook de autenticación
- `AccessGate.tsx` — gate de verificación (parametrizar URLs)
- `GuaranteeSection.tsx` — garantía 30 días (solo cambiar textos)

---

*Playbook creado el 16 de marzo de 2026*
*Basado en el sistema de Pro Prompts eBook — AI Chef Pro*
