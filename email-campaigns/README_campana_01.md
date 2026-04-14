# Campaña 01 — Kit de Escandallos Pro

Primera campaña comercial desde `contact.aichef.pro` (Resend + Listmonk self-hosted).

## ⚠️ PASO 0 — DEPLOY OBLIGATORIO antes de enviar

Esta campaña usa 9 imágenes nuevas ubicadas en `chefpro-modernize/public/email-assets/`. **Tienes que deployar Netlify antes de crear la campaña en Listmonk**, porque si no, las imágenes devuelven 404 y el email se ve roto.

```bash
cd /Users/johnguerrero/chefpro-modernize
git add public/email-assets/ email-campaigns/
git commit -m "Email assets: campaña 01 Kit de Escandallos Pro"
git push
```

Espera ~2 min al build de Netlify y verifica con:

```bash
curl -sI https://aichef.pro/email-assets/aichef-pro-logo-white.png | head -1
```

Debe devolver `HTTP/2 200`.

---

## Archivos

- `plantilla_maestra_aichefpro.html` — Plantilla reutilizable. Se pega UNA vez en **Listmonk → Campañas → Plantillas → Nueva**.
- `campana_01_kit_escandallos.html` — Contenido del email. Se pega en **Listmonk → Campañas → Nueva → pestaña Contenido** en formato **"HTML de origen"** (Raw HTML).

---

## 3 opciones de asunto + preheader

Ordenadas por probabilidad de apertura (primera campaña desde subdominio frío, lista ~3.2k, hostelería ES). Recomendada: **Opción A**.

### ⭐ Opción A — Directa, sin humo (recomendada)
- **Asunto:** `Kit de Escandallos Pro: 12€ esta semana (antes 49€)`
- **Preheader:** `11 plantillas Excel con fórmulas, mermas y calculadora de PVP. Garantía de 30 días.`
- *Por qué:* primera campaña desde subdominio nuevo. Claridad > creatividad. Precio + descuento justifican la apertura y evitan filtros "promo vacía".

### Opción B — Dolor concreto
- **Asunto:** `¿Sabes cuál es el margen real de tu plato estrella?`
- **Preheader:** `11 plantillas Excel para escandallar sin errores. Hoy por 12€ (antes 49€).`

### Opción C — Autoridad / curiosidad
- **Asunto:** `Escandallar a ojo te cuesta dinero (te lo demostramos con Excel)`
- **Preheader:** `Kit de 11 plantillas con mermas precargadas y calculadora de PVP. 12€.`

---

## Pasos en Listmonk

1. **Plantilla maestra** (una sola vez):
   - `http://46.202.175.14:32773/admin/campaigns/templates` → **+ Nueva**.
   - Nombre: `AI Chef Pro — Maestra`.
   - Tipo: `Plantilla de campaña`.
   - Pegar `plantilla_maestra_aichefpro.html` íntegro → Guardar.

2. **Crear campaña**:
   - **Campañas → + Nueva**.
   - Nombre: `01 · Kit de Escandallos Pro · 12€`.
   - Asunto: Opción A.
   - Lista: la principal (3.216 suscriptores).
   - Remitente: `AI Chef Pro <info@contact.aichef.pro>`.
   - Plantilla: `AI Chef Pro — Maestra`.
   - Pestaña **Contenido** → formato **`HTML de origen`** → pegar `campana_01_kit_escandallos.html` íntegro.
   - Guardar como **borrador**.

3. **QA antes de enviar**:
   - Vista previa de Listmonk → comprobar que la plantilla envuelve al contenido y todas las imágenes cargan.
   - Enviar prueba a tu propio email → abrir en Gmail web + Gmail móvil + Outlook web.
   - Verificar: CTA → `aichef.pro/kit-escandallos` · Bridge → `aichef.pro/calculadora-food-cost-restaurante` · Catálogo → `aichef.pro/productos-digitales`.
   - `{{ UnsubscribeURL }}` tiene que renderizar como URL real.

4. **Warm-up del subdominio** (muy importante — primera campaña desde `contact.aichef.pro`):
   - NO envíes los 3.216 de golpe. Trocea:
     - **Día 1:** 500 contactos más recientes (últimos 90 días, más engagement).
     - **Día 2:** 800 siguientes.
     - **Día 3:** resto.
   - Monitoriza bounce rate y quejas en el dashboard de Resend antes de cada tanda. Si bounce > 5%, para y revisa.

---

## URLs de la campaña (QA)

Todas con dominio nativo `aichef.pro` y HTTPS.

### Links
| URL | Uso |
|---|---|
| `https://aichef.pro/kit-escandallos` | CTA principal |
| `https://aichef.pro/productos-digitales` | Catálogo (plantilla + bridge) |
| `https://aichef.pro/calculadora-food-cost-restaurante` | Puente freemium |
| `https://aichef.pro` | Footer |

### Imágenes
Todas servidas desde `https://aichef.pro/email-assets/` salvo la hero, que vive en la raíz.

| Archivo | Uso | Peso | Dimensiones |
|---|---|---|---|
| `/og-kit-escandallos.jpg` | Hero 1 (banner producto) | 96 KB | 1200×630 |
| `/email-assets/aichef-pro-logo-white.png` | Logo header + footer | 23 KB | 900×140 |
| `/email-assets/kit-escandallos-hero.jpg` | Imagen secundaria in-content | 171 KB | 1088×608 |
| `/email-assets/visa.png` | Badge pago | 9 KB | 280×176 |
| `/email-assets/mastercard.png` | Badge pago | 7 KB | 280×176 |
| `/email-assets/apple-pay.png` | Badge pago | 7 KB | 280×176 |
| `/email-assets/google-pay.png` | Badge pago | 8 KB | 280×176 |
| `/email-assets/stripe.png` | Badge pago | 6 KB | 280×176 |
| `/email-assets/money-back-30d.png` | Garantía 30 días | 67 KB | 240×240 |
| `/email-assets/john-guerrero.jpg` | Foto autor (sign-off) | 37 KB | 160×160 |

Todas las imágenes < 200 KB. Total del email: ~431 KB.

## Cambios respecto a la primera versión

- ✅ **Botón CTA arreglado.** Ya no se ve deformado: patrón "bulletproof button" (tabla + `<a>` inline-block con padding fijo), fuente 17px/line-height 20px, padding 16×34.
- ✅ **Badges de pago.** Fila con Visa, Mastercard, Apple Pay, Google Pay y Stripe en PNG, sobre fondo blanco dentro de la caja CTA negra para que destaquen.
- ✅ **Garantía 30 días.** Caja propia con badge visual y copy explícito de cómo solicitar la devolución.
- ✅ **Herramientas gratuitas.** Bridge amarillo menciona la Calculadora de Food Cost gratis + link al catálogo con "decenas de herramientas gratis más".
- ✅ **Foto del autor.** Firma con foto circular de John Guerrero.
- ✅ **Segunda imagen del producto.** `kit-escandallos-hero.jpg` optimizada (250 KB → 171 KB) como refuerzo visual antes de la sección "Qué incluye".
- ✅ **Logo real en header y footer** (wordmark blanco, PNG 900×140) en vez del texto.
