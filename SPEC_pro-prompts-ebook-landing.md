# SPEC: Landing Page — Pro Prompts eBook
**Ruta:** `/pro-prompts-ebook`
**Stack:** React + TypeScript + Vite + Tailwind CSS + Netlify + Bun
**Repo:** github.com/chefbusiness/chefpro-modernize
**Deploy:** Netlify (auto-deploy desde main)

---

## Contexto del producto

Producto digital de bajo coste (€9). Landing de venta standalone que convierte visitantes en compradores. Al completar el pago en Stripe, el usuario recibe un email automático con un magic link de acceso único hacia `/pro-prompts-library`. Nadie puede acceder a la library sin ese token único generado en el momento del pago.

**Headline oficial del producto (no modificar nunca):**
> "El único eBook de prompts de IA para el mundo de la gastronomía — Para chefs, gerentes, pasteleros, bartenders, chocolateros, dueños de restaurante y todos los profesionales del sector"

---

## Estructura de archivos a crear

```
src/
  pages/
    ProPromptsEbook.tsx
  components/ebook/
    HeroSection.tsx
    BookCover.tsx
    CategoriesGrid.tsx
    WhySection.tsx
    BonusSection.tsx
    BuyBox.tsx
    GuaranteeSection.tsx
    FaqAccordion.tsx
    CtaFinal.tsx
    StickyBar.tsx
```

Añadir ruta en el router principal:
```tsx
<Route path="/pro-prompts-ebook" element={<ProPromptsEbook />} />
```

---

## Variables de entorno

Añadir en `.env` local y en Netlify Environment Variables:
```
VITE_STRIPE_PAYMENT_LINK=https://buy.stripe.com/XXXXXXXX
```
Nunca hardcodear el link de Stripe en el código fuente.

---

## Comportamiento general

- Página completamente standalone: sin header/nav global ni footer global del sitio
- Sticky bar fija en la parte inferior en mobile con botón de compra siempre visible
- Todos los botones CTA apuntan a `import.meta.env.VITE_STRIPE_PAYMENT_LINK`
- Animaciones de entrada suaves al hacer scroll (Tailwind transitions o framer-motion)
- Mobile-first, totalmente responsive
- Meta robots: index, follow — esta página SI se indexa en Google
- OG tags completos para RRSS

---

## Diseño y estilos

Usar los tokens de Tailwind y fuentes ya existentes en el proyecto.
Paleta de referencia: fondo negro/dark, amarillo #FFD700 como color de acción y acento.

Si no existe en el config, añadir:
```js
// tailwind.config.ts
colors: {
  brand: {
    yellow: '#FFD700',
    dark: '#0a0a0a',
  }
}
```

---

## SECCION 1 — HERO

**Badge pill superior:**
🌍 El recurso #1 de prompts para el mundo de la hostelería y la restauración

**H1 (no modificar):**
El Único eBook de Prompts de IA para Hostelería que Realmente Necesitas

Las palabras "eBook de Prompts" en color amarillo/acento.

**Subtítulo:**
Para chefs, gerentes, pasteleros, bartenders, chocolateros, dueños de restaurante y todos los profesionales del sector. Desbloquea el potencial real de la IA en tu negocio.

**Checklist — 4 items con check en amarillo:**
- Acceso instantáneo al eBook completo
- Más de 300 prompts para toda la hostelería y restauración
- Compatible con ChatGPT, Claude, Perplexity, DeepSeek y más
- Actualizaciones gratuitas de por vida

**Caja de precio:**
- Precio tachado en gris: €97
- Precio real en amarillo grande: €9
- Pill badge: -90%
- Nota urgencia: Precio especial de lanzamiento. Sube pronto
- Botón CTA primario fondo amarillo texto negro: COMPRAR AHORA — €9
- Nota bajo el botón: Pago 100% seguro. Acceso inmediato por email

---

## SECCION 2 — PORTADA DEL EBOOK

Libro 3D generado con CSS puro (perspectiva, sombra lateral, borde). No imagen externa.

Contenido sobre el libro:
- Icono: chef
- Título: PRO PROMPTS · Hostelería y Restauración
- Subtítulo: 300+ Prompts para toda la hostelería
- Spine/borde lateral en amarillo
- Sombra oscura en la base

Debajo del libro: botón outline amarillo COMPRAR AHORA — €9 + nota de seguridad.

---

## SECCION 3 — QUE ENCONTRARAS EN EL EBOOK

**Título:** ¿Qué Encontrarás en el eBook?
**Subtítulo:** Más de 300 prompts organizados en 12 categorías para toda la hostelería

**Grid de categorías (2 cols mobile, 3 tablet, 4 desktop):**

1. Cocina y Recetas — Para chefs y cocineros: recetas creativas, técnicas, fusión y cocinas del mundo
2. Gestión y Costes — Para gerentes y dueños: food cost, escandallos, rentabilidad y control de negocio
3. Pastelería y Panadería — Para pasteleros, panaderos y chocolateros: formulaciones, técnicas y creatividad
4. Sala, Bar y Bebidas — Para bartenders y sommeliers: coctelería, maridajes, carta de vinos y sala
5. Catering y Eventos — Propuestas, presupuestos, logística y menús para bodas, corporativos y banquetes
6. Food Pairing — Maridajes científicos, sustituciones de ingredientes y combinaciones inesperadas
7. Marketing del Negocio — RRSS, SEO local, reseñas, email marketing y posicionamiento de marca
8. Alérgenos y Seguridad — Gestión de alérgenos, etiquetado, protocolos APPCC y formación de equipo
9. Gestión de Negocio — Planes de negocio, franquicias, estrategia de precios y consultoría
10. Liderazgo y Equipos — Liderazgo, feedback, bienestar y gestión de brigada
11. Prompt Engineering — El framework para obtener respuestas perfectas de cualquier IA en hostelería
12. Plantillas Copy-Paste — Listas para usar en segundos para cualquier perfil del sector

Estilos de tarjeta: fondo dark semitransparente, borde gris sutil, hover con borde amarillo y transición suave.

---

## SECCION 4 — POR QUE ESTE EBOOK

**Título:** ¿Por Qué Este eBook?
**Subtítulo:** No es solo una lista de prompts. Es un sistema completo para dominar la IA en tu negocio de hostelería.

**4 tarjetas con icono grande sobre fondo amarillo:**

1. Para todo el sector, no solo la cocina
Da igual que seas chef, gerente, pastelero, bartender o dueño de restaurante. Cada prompt está diseñado para tu rol específico dentro del negocio.

2. Prompts Probados en AI Chef Pro
Cada prompt ha sido testeado en la plataforma para garantizar resultados consistentes y de calidad profesional en hostelería real.

3. Ahorra Horas de Trabajo
Deja de experimentar con la IA. Obtén resultados de calidad en segundos, ya sea para una receta, un presupuesto de catering o un post de Instagram.

4. Actualizaciones Gratuitas
A medida que AI Chef Pro crece con nuevas apps para toda la hostelería, el eBook se actualiza. Tú las recibes sin coste adicional.

**Banner de compatibilidad (strip full-width):**
Diseñado para AI Chef Pro. También funciona perfectamente con cualquier IA conversacional:
Pills: AI Chef Pro (amarillo destacada) · ChatGPT · Claude · Perplexity · DeepSeek · Gemini · KIMI · Copilot · + cualquier chatbot

---

## SECCION 5 — BONOS EXCLUSIVOS

**Título:** Bonos Exclusivos
**Subtítulo:** Además del eBook, recibirás estos bonos GRATIS valorados en €97

BONUS 1 — Mega Pack Cocinas del Mundo — Valor: €47
50 prompts adicionales exclusivos para las 25 cocinas internacionales de AI Chef Pro: francesa, japonesa, italiana, peruana, mexicana y más.

BONUS 2 — Guía de Prompt Engineering Gastronómico — Valor: €27
Aprende a crear tus propios prompts gastronómicos perfectos desde cero con el método AI Chef Pro.

BONUS 3 — Cheat Sheet Descargable — Valor: €23
Resumen rápido de los 30 mejores prompts para hostelería para tener siempre a mano en tu negocio.

**Caja de valor total:**
- Valor total tachado: €194
- Precio real grande amarillo: €9
- Texto: ¡Ahorra €185 HOY!

---

## SECCION 6 — CAJA DE COMPRA (id="comprar")

Caja centrada con borde amarillo:
- Precio: €97 tachado → €9 + pill -90%
- Nota: Precio especial de lanzamiento — 90% de descuento
- Botón: SI, QUIERO EL EBOOK — €9 → VITE_STRIPE_PAYMENT_LINK
- Nota seguridad: Pago 100% seguro. Acceso inmediato por email

---

## SECCION 7 — GARANTIA

- Icono central: escudo en círculo con fondo amarillo semitransparente
- Título: Garantía de Satisfacción 100%
- Texto: Si el eBook no supera tus expectativas, te devolvemos el 100% de tu dinero. Sin preguntas, sin complicaciones.

3 estadísticas en fila:
- 30 / Días de garantía
- 100% / Reembolso garantizado
- 0 / Preguntas incómodas

---

## SECCION 8 — FAQ (acordeón)

Un solo ítem abierto a la vez. Chevron rota 180° al abrir.

P: ¿Cómo recibo el acceso después del pago?
R: Inmediatamente después del pago recibirás un email con tu enlace de acceso personal y único a la Pro Prompts Library, donde encontrarás el eBook descargable y todos los bonos. El enlace es personal e intransferible.

P: ¿Funciona solo con AI Chef Pro o con otras IAs?
R: Los prompts están optimizados para AI Chef Pro pero funcionan perfectamente con ChatGPT, Claude, Perplexity, DeepSeek, Gemini, KIMI y cualquier IA conversacional.

P: ¿Qué formato tiene el eBook?
R: PDF de alta calidad, compatible con todos los dispositivos: móvil, tablet y ordenador.

P: ¿Recibiré actualizaciones?
R: Sí. Todas las actualizaciones futuras son gratuitas. A medida que AI Chef Pro lance nuevas apps, el eBook se actualiza y tú las recibes automáticamente.

P: ¿Cómo funciona la garantía?
R: Tienes 30 días completos para probarlo. Si no estás satisfecho por cualquier motivo, te devolvemos el 100% sin hacer ninguna pregunta.

P: ¿Necesito experiencia previa con IA?
R: Para nada. Los prompts están listos para copiar y pegar. Resultados profesionales desde el primer día, independientemente de tu nivel.

---

## SECCION 9 — CTA FINAL

**Título:** Es Hora de Dominar la IA en tu Negocio
**Texto:** No dejes pasar esta oportunidad. Únete a miles de profesionales de la hostelería y restauración que ya están obteniendo resultados con IA.

Checklist completa en la caja final:
- eBook completo con 300+ prompts para toda la hostelería
- BONUS 1: Mega Pack Cocinas del Mundo (€47)
- BONUS 2: Guía Prompt Engineering Gastronómico (€27)
- BONUS 3: Cheat Sheet Descargable (€23)
- Actualizaciones gratuitas de por vida
- Garantía de devolución 30 días

Botón: SI, QUIERO EL EBOOK — €9 → VITE_STRIPE_PAYMENT_LINK
Nota: Pago 100% seguro. Acceso inmediato por email

---

## STICKY BAR — solo mobile (md:hidden)

Fija en la parte inferior de pantalla:
OBTENER EL EBOOK — €9    [COMPRAR AHORA]
Botón → VITE_STRIPE_PAYMENT_LINK

---

## FOOTER MINIMO

Sin header/footer global del sitio:
© 2026 AI Chef Pro · Todos los derechos reservados
Links: aichef.pro · Contacto · Precios

---

## SEO / HEAD META

```html
<title>Pro Prompts eBook — El único eBook de prompts de IA para hostelería | AI Chef Pro</title>
<meta name="description" content="300+ prompts de IA para chefs, gerentes, pasteleros, bartenders y dueños de restaurante. Compatible con ChatGPT, Claude y AI Chef Pro. Solo €9." />
<meta name="robots" content="index, follow" />
<meta property="og:title" content="Pro Prompts eBook — AI Chef Pro" />
<meta property="og:description" content="El único eBook de prompts de IA para el mundo de la gastronomía. €9." />
<meta property="og:url" content="https://aichef.pro/pro-prompts-ebook" />
```

---

## NOTAS FINALES PARA CLAUDE CODE

- VITE_STRIPE_PAYMENT_LINK es variable de entorno. Añadirla también en Netlify Dashboard > Environment Variables
- La URL de redirect post-pago se configura en Stripe Dashboard. Debe apuntar a: https://aichef.pro/pro-prompts-library-access?token={CHECKOUT_SESSION_ID}
- Esta página NO incluye header/nav ni footer global del sitio
- Respetar todos los tokens de Tailwind y fuentes ya instalados en el proyecto
- Ver SPEC_pro-prompts-library.md para la arquitectura de seguridad completa del acceso post-pago
