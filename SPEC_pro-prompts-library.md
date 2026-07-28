# SPEC: Pro Prompts Library — Página post-compra protegida
**Ruta pública:** `/pro-prompts-library-access?token=XXXX` (valida el token)
**Ruta de la library:** `/pro-prompts-library` (protegida, solo con sesión válida)
**Stack:** React + TypeScript + Vite + Tailwind CSS + Netlify Functions + Bun
**Repo:** github.com/chefbusiness/chefpro-modernize
**Deploy:** Netlify (auto-deploy desde main)

---

## Concepto del producto

Biblioteca de producto nativa donde el comprador accede a:
1. Sus descargas (PDF del eBook + bonos)
2. Todos los prompts organizados por categorías, navegables e interactivos, listos para copiar con un clic

El objetivo secundario: que el usuario visite esta página con frecuencia porque los prompts están aquí en formato interactivo, generando tráfico recurrente a aichef.pro y conversión natural hacia la suscripción de la plataforma.

---

## ARQUITECTURA DE SEGURIDAD COMPLETA

La ruta `/pro-prompts-library` es privada. Solo pueden acceder usuarios que hayan pagado.
El sistema funciona así:

### Flujo completo de acceso

```
1. Usuario paga en Stripe (Payment Link)
         ↓
2. Stripe redirige a: /pro-prompts-library-access?token={CHECKOUT_SESSION_ID}
         ↓
3. Componente AccessGate.tsx llama a Netlify Function: /.netlify/functions/verify-purchase
         ↓
4. Netlify Function verifica el CHECKOUT_SESSION_ID contra la API de Stripe
         ↓
5. Si el pago es válido:
   - Genera un JWT firmado con el email del comprador y expiración larga (1 año)
   - Guarda el email en KV store (Netlify Blobs o variable en memoria)
   - Devuelve el JWT al cliente
   - Cliente guarda el JWT en sessionStorage
   - Redirige automáticamente a /pro-prompts-library
         ↓
6. Si el pago NO es válido:
   - Redirige a /pro-prompts-ebook con mensaje de error
```

### Protección de la ruta /pro-prompts-library

El componente ProtectedRoute verifica en cada render que existe un JWT válido en sessionStorage.
Si no hay JWT válido, redirige automáticamente a /pro-prompts-ebook.

```
/pro-prompts-library
  → ProtectedRoute.tsx (middleware React)
      → verifica JWT en sessionStorage
      → si válido: renderiza ProPromptsLibrary
      → si inválido: redirect a /pro-prompts-ebook
```

### También: email con magic link

Adicionalmente al redirect automático de Stripe, la Netlify Function envía un email al comprador con su magic link personal. Así puede volver a la library en el futuro aunque haya cerrado el navegador.

El magic link contiene el mismo JWT:
`https://aichef.pro/pro-prompts-library-access?jwt=XXXXX`

---

## Estructura de archivos a crear

```
src/
  pages/
    ProPromptsLibrary.tsx          ← la library (protegida)
    AccessGate.tsx                 ← página de validación del token
  components/library/
    TopBar.tsx                     ← barra superior sticky
    DownloadsSection.tsx           ← tarjetas de descarga
    CompatibilityBanner.tsx
    PromptFilters.tsx              ← filtros de categoría
    PromptCategory.tsx             ← bloque de categoría
    PromptCard.tsx                 ← prompt individual con acordeón y botón copiar
    CtaToApp.tsx                   ← CTA final hacia aichef.pro
  components/shared/
    ProtectedRoute.tsx             ← middleware de protección de ruta
  hooks/
    useAuth.ts                     ← lógica de verificación del JWT

netlify/
  functions/
    verify-purchase.ts             ← Netlify Function principal
    send-access-email.ts           ← Netlify Function de email
```

Añadir rutas en el router principal:
```tsx
<Route path="/pro-prompts-library-access" element={<AccessGate />} />
<Route
  path="/pro-prompts-library"
  element={
    <ProtectedRoute>
      <ProPromptsLibrary />
    </ProtectedRoute>
  }
/>
```

---

## Variables de entorno

Añadir en `.env` local y en Netlify Dashboard > Environment Variables:
```
STRIPE_SECRET_KEY=sk_live_XXXXXXXX
JWT_SECRET=una_cadena_aleatoria_larga_y_segura_min_32_chars
RESEND_API_KEY=re_XXXXXXXX          (o el servicio de email que uses)
PDF_EBOOK_URL=https://...           (URL del PDF principal)
PDF_BONUS1_URL=https://...          (URL del Bonus 1)
PDF_BONUS23_URL=https://...         (URL del Bonus 2+3)
```

Estas variables NUNCA deben estar en el código fuente ni en el frontend (sin prefijo VITE_).

---

## Netlify Function: verify-purchase.ts

```typescript
// netlify/functions/verify-purchase.ts
// Recibe: { checkoutSessionId: string } o { jwt: string }
// Devuelve: { valid: boolean, jwt?: string, email?: string }

import Stripe from 'stripe';
import jwt from 'jsonwebtoken';

export const handler = async (event) => {
  const { checkoutSessionId, existingJwt } = JSON.parse(event.body || '{}');

  // Caso 1: verificar sesión de Stripe nueva
  if (checkoutSessionId) {
    const stripe = new Stripe(process.env.STRIPE_SECRET_KEY);
    const session = await stripe.checkout.sessions.retrieve(checkoutSessionId);

    if (session.payment_status === 'paid') {
      const token = jwt.sign(
        { email: session.customer_email, product: 'pro-prompts-ebook' },
        process.env.JWT_SECRET,
        { expiresIn: '365d' }
      );
      // Enviar email con magic link (llamada asíncrona)
      await sendAccessEmail(session.customer_email, token);
      return { statusCode: 200, body: JSON.stringify({ valid: true, jwt: token }) };
    }
    return { statusCode: 403, body: JSON.stringify({ valid: false }) };
  }

  // Caso 2: verificar JWT existente (para magic link en email)
  if (existingJwt) {
    try {
      jwt.verify(existingJwt, process.env.JWT_SECRET);
      return { statusCode: 200, body: JSON.stringify({ valid: true, jwt: existingJwt }) };
    } catch {
      return { statusCode: 403, body: JSON.stringify({ valid: false }) };
    }
  }

  return { statusCode: 400, body: JSON.stringify({ valid: false }) };
};
```

---

## Componente AccessGate.tsx

```
1. Lee el parámetro ?token= o ?jwt= de la URL
2. Muestra pantalla de carga: "Verificando tu compra..."
3. Llama a /.netlify/functions/verify-purchase
4. Si válido: guarda JWT en sessionStorage → redirige a /pro-prompts-library
5. Si inválido: muestra error y enlace de vuelta a /pro-prompts-ebook
```

Pantalla de carga con spinner y texto:
"Verificando tu compra... un momento por favor"

Pantalla de error:
"No hemos podido verificar tu acceso. Si acabas de comprar, revisa tu email para el enlace de acceso. ¿Problemas? Contáctanos en aichef.pro/contacto"

---

## Componente ProtectedRoute.tsx

```tsx
const ProtectedRoute = ({ children }) => {
  const token = sessionStorage.getItem('pro-prompts-jwt');
  if (!token) return <Navigate to="/pro-prompts-ebook" replace />;
  try {
    // Verificación básica del JWT en cliente (solo estructura, sin firma)
    const payload = JSON.parse(atob(token.split('.')[1]));
    if (payload.exp < Date.now() / 1000) {
      sessionStorage.removeItem('pro-prompts-jwt');
      return <Navigate to="/pro-prompts-ebook" replace />;
    }
    return children;
  } catch {
    return <Navigate to="/pro-prompts-ebook" replace />;
  }
};
```

---

## Comportamiento general de la Library

- Página standalone: sin header/nav global ni footer global del sitio
- Barra superior sticky con logo AI Chef Pro y badge del producto
- Meta robots: noindex, nofollow — esta página NO aparece en Google
- Totalmente responsive, prioridad mobile
- Los prompts se abren en acordeón: un solo prompt abierto a la vez
- Botón "Copiar prompt": al hacer clic cambia a "¡Copiado!" durante 2 segundos (verde)
- Filtros de categoría en barra horizontal scrollable, filtro activo en amarillo

---

## BARRA SUPERIOR (sticky)

- Izquierda: logo "AI Chef Pro" → enlaza a aichef.pro
- Derecha: badge "PRO PROMPTS LIBRARY"

---

## SECCION 1 — HERO DE LA LIBRARY

**H1:** Tu Pro Prompts Library

**Subtítulo:**
Bienvenido. Aquí tienes todos tus prompts certificados para hostelería y restauración — para chefs, gerentes, pasteleros, bartenders y dueños de negocio. Copia, usa y domina la IA.

---

## SECCION 2 — DESCARGAS

Label: Tus descargas

3 tarjetas en grid (1 col mobile, 3 col desktop):

**Tarjeta 1 — Principal (borde amarillo)**
- Icono: libro
- Título: Pro Prompts eBook
- Descripción: El eBook completo en PDF con todos los prompts organizados por categorías.
- Botón primario amarillo: Descargar PDF → process.env variable PDF_EBOOK_URL (inyectada via API route o directamente si es pública con URL firmada de Stripe/S3)

**Tarjeta 2**
- Icono: globo
- Título: Bonus 1: Cocinas del Mundo
- Descripción: 50 prompts para las 25 cocinas internacionales de AI Chef Pro.
- Botón outline: Descargar → PDF_BONUS1_URL

**Tarjeta 3**
- Icono: rayo
- Título: Bonus 2 + 3
- Descripción: Guía de Prompt Engineering Gastronómico + Cheat Sheet imprimible.
- Botón outline: Descargar → PDF_BONUS23_URL

NOTA PARA CLAUDE CODE: las URLs de los PDFs vienen de variables de entorno del servidor,
no deben exponerse en el frontend directamente. Crear una Netlify Function get-download-urls.ts
que devuelva las URLs solo si el request incluye un JWT válido en el header Authorization.

---

## SECCION 3 — BANNER DE COMPATIBILIDAD

Texto: Compatible con:
Pills: AI Chef Pro (amarilla destacada) · ChatGPT · Claude · Perplexity · DeepSeek · Gemini · KIMI · Copilot

---

## SECCION 4 — BIBLIOTECA DE PROMPTS

**Título:** Prompts Certificados
**Badge:** 75 prompts · 9 perfiles

### Filtros de categoría (scrollable horizontal)

| data-filter | Label visible |
|-------------|---------------|
| all | Todos (activo por defecto) |
| cocina | Cocina |
| gestion | Gestión y Costes |
| pasteleria | Pastelería y Pan |
| catering | Catering |
| marketing | Marketing |
| alergenos | Alérgenos |
| food-pairing | Food Pairing |
| negocio | Negocio |
| liderazgo | Liderazgo |

Al hacer clic en un filtro, se muestran solo las categorías con ese data-cat.
Filtro activo con fondo amarillo y texto negro.

---

### Estructura de cada PromptCard

```
PromptCard
  ├── Cabecera clickeable (toggle acordeón)
  │     ├── Número: #01, #02...
  │     ├── Nombre del prompt
  │     └── Chevron (rota 180° cuando está abierto)
  └── Cuerpo (oculto por defecto)
        ├── Caja de texto del prompt
        │     └── Texto completo con placeholders en [MAYÚSCULAS]
        └── Fila de acciones
              ├── Botón "Copiar prompt" (amarillo → verde + "¡Copiado!" 2s)
              └── Texto compatibilidad (gris, pequeño, alineado derecha)
```

---

### CATEGORIA 1 — Cocina y Recetas Creativas
data-cat="cocina" · 10 prompts

**#01 — Receta de autor desde ingrediente principal**
Compatible con: AI Chef Pro · ChatGPT · Claude

Texto del prompt:
Actúa como chef ejecutivo con experiencia en cocina de autor contemporánea. Crea una receta de alta cocina usando [INGREDIENTE PRINCIPAL] como protagonista absoluto. El plato debe tener:
- Nombre creativo y evocador
- Historia del plato (2-3 frases)
- Ingredientes para 4 pax con cantidades exactas
- Elaboración paso a paso (técnicas profesionales)
- Emplatado y presentación
- Maridaje recomendado
- Nivel de dificultad: [BÁSICO/INTERMEDIO/AVANZADO]
Estilo gastronómico: [MEDITERRÁNEO/NÓRDICO/ASIÁTICO/FUSIÓN]

---

**#02 — Menú degustación de 7 pasos**
Compatible con: AI Chef Pro · ChatGPT · Claude

Texto del prompt:
Diseña un menú degustación de 7 pasos para un restaurante de [TIPO DE COCINA]. El menú debe:
- Seguir una narrativa gastronómica coherente de inicio a fin
- Incluir: snack bienvenida, 2 entrantes, pescado, carne, pre-postre y postre
- Respetar la progresión de sabores (de ligero a intenso)
- Cada plato con nombre, descripción y técnica principal
- Restricciones a evitar: [ALÉRGENOS/PREFERENCIAS]
- Precio objetivo por persona: [RANGO €]
- Temporada: [PRIMAVERA/VERANO/OTOÑO/INVIERNO]

---

**#03 — Reinterpretar un clásico con técnicas modernas**
Compatible con: AI Chef Pro · ChatGPT · Perplexity

Texto del prompt:
Toma el plato clásico [NOMBRE DEL PLATO] de la cocina [PAÍS/REGIÓN] y reinterpretalo con técnicas de cocina contemporánea. Mantén la esencia y los sabores reconocibles del original pero transforma:
- La textura de al menos 2 componentes
- La presentación al plato
- Incorpora al menos una técnica moderna (gelificación, esferificación, deshidratación, emulsión, etc.)
Explica qué conservas del original y qué transformas. Incluye receta completa.

---

**#04 — Receta de temporada con productos locales**
Compatible con: AI Chef Pro · ChatGPT · Claude

Texto del prompt:
Soy chef de un restaurante en [CIUDAD/REGIÓN] y quiero crear un plato que destaque los productos de temporada de [MES/ESTACIÓN]. Dame una receta que:
- Use mínimo 3 productos de temporada y proximidad de esa región
- Sea ejecutable en un servicio de restaurante (no exceda 15 min de mise en place por pase)
- Tenga un food cost por debajo del [X]% del precio de venta
- Precio de venta objetivo: [€]
- Número de comensales estimados por servicio: [N]

---

**#05 — Receta plant-based de alta cocina**
Compatible con: AI Chef Pro · Claude · ChatGPT

Texto del prompt:
Diseña una receta plant-based (100% vegetal) de nivel gastronómico que pueda competir en carta con platos de proteína animal. El plato debe:
- Tener complejidad de sabores comparable a un plato de carne o pescado
- Usar técnicas que aporten umami (fermentación, Maillard, reducción, etc.)
- Ser visualmente impactante en el emplatado
- Ingrediente vegetal protagonista: [INGREDIENTE]
- Sin: [RESTRICCIONES ADICIONALES]
Incluye receta completa, técnicas y sugerencia de maridaje.

---

**#06 — Receta de aprovechamiento zero waste**
Compatible con: AI Chef Pro · ChatGPT · DeepSeek

Texto del prompt:
Tengo estos subproductos y mermas en mi cocina que normalmente se descartan: [LISTA DE SUBPRODUCTOS]. Crea una o varias recetas que los aprovechen íntegramente en platos de carta o tapas. Para cada receta indica:
- Nombre del plato
- Subproducto aprovechado y cómo se transforma
- Técnica aplicada
- Valor añadido al menú (narrativa de sostenibilidad)
- Precio de venta sugerido

---

**#07 — Receta de fermentación creativa**
Compatible con: AI Chef Pro · Claude · Perplexity

Texto del prompt:
Actúa como experto en fermentación gastronómica. Quiero fermentar [INGREDIENTE] para usarlo en [TIPO DE PLATO/CONTEXTO]. Dame:
- Técnica de fermentación más adecuada (koji, lactofermentación, garum, kombucha, miso, shoyu...)
- Proceso detallado paso a paso con tiempos y temperaturas
- Resultado esperado en sabor, textura y aroma
- Aplicaciones gastronómicas del fermento resultante (3 ideas de uso)
- Errores comunes a evitar
- Tiempo total hasta estar listo para usar

---

**#08 — Descripción literaria del plato para la carta**
Compatible con: AI Chef Pro · ChatGPT · Claude

Texto del prompt:
Escribe la descripción del plato [NOMBRE DEL PLATO] para la carta de un restaurante [TIPO]. Los ingredientes principales son: [LISTA]. La descripción debe:
- Tener entre 18 y 28 palabras (concisa pero evocadora)
- Apelar a los sentidos sin ser cursi
- Mencionar la técnica principal si añade valor
- Tono: [ELEGANTE/CASUAL/MODERNO/TRADICIONAL]
Dame 3 versiones alternativas para elegir.

---

**#09 — Escalado de receta para servicio masivo**
Compatible con: AI Chef Pro · ChatGPT · Gemini

Texto del prompt:
Tengo esta receta pensada para [N PORCIONES ORIGINAL]: [PEGAR RECETA]. Necesito escalarla para [N PORCIONES DESTINO]. Por favor:
- Escala todas las cantidades con precisión
- Advierte sobre ingredientes que NO escalan linealmente (levaduras, sal, especias, gelatinas)
- Ajusta tiempos de cocción si aplica
- Indica si algún proceso cambia al producir en ese volumen
- Sugiere adaptaciones para producción en cocina central si el volumen es superior a 50 porciones

---

**#10 — Receta fusión entre dos cocinas**
Compatible con: AI Chef Pro · Claude · ChatGPT

Texto del prompt:
Crea una receta de fusión entre la cocina [COCINA 1] y la cocina [COCINA 2] que sea coherente y no forzada. El plato debe respetar la esencia de ambas tradiciones culinarias. Indica:
- Qué elementos tomas de cada cocina (técnicas, ingredientes, filosofía)
- Por qué esta combinación tiene sentido gastronómico
- Receta completa con ingredientes y elaboración
- Nombre del plato que refleje la fusión
- Posibles puntos de conflicto cultural a tener en cuenta

---

### CATEGORIA 2 — Gestión, Costes y Mermas
data-cat="gestion" · 8 prompts

**#11 — Cálculo de food cost de una receta**
Compatible con: AI Chef Pro · ChatGPT · Gemini

Texto del prompt:
Calcula el food cost de esta receta para [N] porciones. Te proporciono los ingredientes y costes:
[LISTA: ingrediente - cantidad - precio por kg/unidad]
Por favor calcula:
- Coste total de materia prima
- Coste por porción
- Food cost % si el precio de venta es [€]
- Food cost % recomendado para este tipo de establecimiento: [TIPO]
- Si el food cost es elevado, sugiere 2-3 optimizaciones sin sacrificar calidad

---

**#12 — Análisis de mermas por ingrediente**
Compatible con: AI Chef Pro · ChatGPT · Claude

Texto del prompt:
Actúa como experto en gestión de costes gastronómicos. Para los siguientes ingredientes, dame el porcentaje de merma estándar por tipo de procesado y el peso neto aprovechable:
[LISTA DE INGREDIENTES]
Para cada uno indica:
- % merma en limpieza en crudo
- % merma tras cocción (si aplica)
- Rendimiento neto final por kg bruto
- Precio real por kg neto (si el bruto cuesta [€/kg])
- Consejos para reducir la merma en cocina

---

**#13 — Ingeniería de menú: rentabilidad por plato**
Compatible con: AI Chef Pro · Claude · ChatGPT

Texto del prompt:
Analiza la rentabilidad de estos platos de mi carta usando la matriz de ingeniería de menú (Boston Matrix):
[TABLA: plato - precio venta - food cost - unidades vendidas/semana]
Clasifica cada plato en: Estrella (alta rentabilidad, alta demanda), Vaca Lechera (alta rentabilidad, baja demanda), Interrogante (baja rentabilidad, alta demanda), Perro (baja rentabilidad, baja demanda).
Recomienda qué hacer con cada uno: mantener, rediseñar, eliminar o relanzar.

---

**#14 — Escandallo profesional completo**
Compatible con: AI Chef Pro · ChatGPT · Gemini

Texto del prompt:
Elabora el escandallo completo del plato [NOMBRE DEL PLATO]. Ingredientes y cantidades: [LISTA]. Precio de venta objetivo: [€]. Incluye:
- Tabla de escandallo con coste por ingrediente
- Coste total materia prima
- Coste de mano de obra estimado (tiempo elaboración: [MINUTOS] × coste/hora: [€])
- Costes indirectos estimados (energía, consumibles): [%]
- Margen bruto y neto
- Precio de venta mínimo para alcanzar el margen objetivo: [%]
- Recomendación de precio de carta

---

**#15 — Optimización de compras semanales**
Compatible con: AI Chef Pro · ChatGPT · Claude

Texto del prompt:
Ayúdame a optimizar el pedido semanal de mi restaurante. Datos:
- Menú de la semana: [DESCRIPCIÓN O LISTA DE PLATOS]
- Número de servicios estimados por día: [N]
- Días de la semana activos: [DÍAS]
- Ingredientes que ya tengo en stock: [LISTA]
Genera una lista de compras optimizada con cantidades exactas, considera mermas estándar, y agrupa por proveedor si es posible (carnicería, pescadería, frutería, almacén).

---

**#16 — Rediseño de plato para mejorar rentabilidad**
Compatible con: AI Chef Pro · Claude · ChatGPT

Texto del prompt:
Este plato tiene un food cost demasiado alto: [DESCRIPCIÓN DEL PLATO] con food cost actual del [%]. Mi objetivo es bajarlo al [%] sin que el cliente perciba pérdida de valor. Propón:
- Sustitución o reducción de ingredientes de alto coste
- Técnicas que aporten percepción de valor sin incrementar coste
- Rediseño del emplatado que justifique el precio
- Nueva propuesta de precio de carta si hay mejora de valor percibido

---

**#17 — Control de inventario y rotación**
Compatible con: AI Chef Pro · ChatGPT · Gemini

Texto del prompt:
Tengo los siguientes ingredientes en mi cámara con estas fechas de caducidad/consumo preferente: [LISTA CON FECHAS]. Necesito:
- Orden de prioridad de uso por urgencia
- Sugerencias de platos del día o especiales que los aprovechen
- Técnicas de conservación para extender vida útil de los más críticos
- Alerta de lo que se perderá si no actúo en 24/48h
- Propuesta de mise en place que minimice pérdidas esta semana

---

**#18 — Precio de carta basado en mercado**
Compatible con: AI Chef Pro · ChatGPT · Claude

Texto del prompt:
Ayúdame a fijar el precio de carta para [NOMBRE DEL PLATO]. El coste de materia prima es [€] por porción. Mi restaurante es de tipo [TIPO] en [CIUDAD], ticket medio actual [€]. Considera:
- Benchmark con precios de mercado de ese tipo de establecimiento
- Elasticidad de precio para ese perfil de comensal
- Estrategia de pricing: líder en precio, precio premium, precio justo
- El precio que maximiza margen sin sacrificar volumen de ventas
- Si conviene presentarlo como precio redondo o con céntimos (psicología del precio)

---

### CATEGORIA 3 — Catering y Eventos
data-cat="catering" · 8 prompts

**#19 — Propuesta de menú para boda**
Compatible con: AI Chef Pro · ChatGPT · Claude

Texto del prompt:
Diseña una propuesta de menú para una boda de [N] invitados:
- Perfil de los novios/invitados: [DESCRIPCIÓN]
- Presupuesto por persona: [€]
- Restricciones dietéticas confirmadas: [LISTA]
- Época del año: [MES]
- Espacio: [INTERIOR/EXTERIOR/FINCA/HOTEL]
- Formato: [SERVICIO A LA MESA/BUFFET/ESTACIONES/COCTELERÍA]
Incluye: cóctel de bienvenida, menú completo con opciones, carta de bebidas sugerida y estimación de personal necesario.

---

**#20 — Presupuesto de catering corporativo**
Compatible con: AI Chef Pro · ChatGPT · Claude

Texto del prompt:
Elabora un presupuesto detallado para un evento corporativo:
- Número de personas: [N]
- Formato: [COFFEE BREAK/ALMUERZO/CENA DE GALA/COCKTAIL]
- Duración: [HORAS]
- Ubicación: [LOCAL PROPIO/SEDE CLIENTE/ESPACIO EXTERNO]
- Presupuesto máximo: [€]
Desglosa: coste de alimentos, bebidas, personal, logística, alquiler de material y margen comercial. Incluye condiciones de pago y política de cancelación.

---

**#21 — Planning operativo de producción para evento**
Compatible con: AI Chef Pro · Claude · ChatGPT

Texto del prompt:
Crea el planning operativo de producción para este evento: [DESCRIPCIÓN]. Fecha: [FECHA]. Menú: [DESCRIPCIÓN]. Personal disponible: [N personas]. Organiza:
- Timeline de producción (desde 3 días antes hasta el servicio)
- Asignación de tareas por persona
- Lista de mise en place por día
- Checklist de carga/transporte si aplica
- Plan B para las elaboraciones más críticas

---

**#22 — Menú para evento con restricciones múltiples**
Compatible con: AI Chef Pro · ChatGPT · Claude

Texto del prompt:
Diseña un menú para un evento de [N] personas donde coexisten estas restricciones dietéticas: [LISTA DETALLADA: X veganos, Y celíacos, Z sin lactosa, etc.]. El reto: que no haya menús especiales segregados. Propón un menú unificado que funcione para todos sin que nadie sienta que tiene una versión inferior.

---

**#23 — Estaciones gastronómicas para cocktail**
Compatible con: AI Chef Pro · ChatGPT · Claude

Texto del prompt:
Diseña [N] estaciones gastronómicas temáticas para un cóctel de [N] personas durante [HORAS]. Cada estación debe tener:
- Nombre y concepto temático
- 4-6 elaboraciones (mix frío/caliente)
- 1 elemento espectacular o interactivo para atraer a los invitados
- Tiempo de montaje y necesidades de personal por estación
Tema global del evento: [TEMA]. Presupuesto total: [€]

---

**#24 — Email de propuesta comercial para cliente**
Compatible con: AI Chef Pro · Claude · ChatGPT

Texto del prompt:
Redacta un email de propuesta comercial para un cliente potencial de catering. Evento: [TIPO]. El email debe:
- Ser profesional pero cálido, no robótico
- Resumir nuestra propuesta de valor diferencial
- Mencionar brevemente el menú sugerido: [DESCRIPCIÓN]
- Precio por persona: [€]
- Llamada a la acción clara para concertar reunión o degustación
- Longitud: máximo 200 palabras
Firmado por: [NOMBRE/CARGO]

---

**#25 — Cálculo de cantidades para buffet**
Compatible con: AI Chef Pro · ChatGPT · Gemini

Texto del prompt:
Calcula las cantidades exactas de alimentos para un buffet de [N] personas durante [HORAS]. Perfil: [CORPORATIVO/FAMILIAR/GALA/CASUAL]. Menú del buffet: [DESCRIPCIÓN]. Ten en cuenta:
- Ratios estándar por persona por categoría
- Factor de consumo según perfil de invitados y hora del día
- Excedente de seguridad recomendado
- Orden de colocación en buffet para optimizar consumo

---

**#26 — Menú de temporada para catering premium**
Compatible con: AI Chef Pro · Claude · ChatGPT

Texto del prompt:
Diseña un menú de catering premium para la temporada de [TEMPORADA/MESES] que destaque productos de km 0 y máxima calidad. Nivel: gourmet/alta gama. El menú debe ser una declaración gastronómica, no solo un servicio de comida. Incluye storytelling de los ingredientes principales y sugiere cómo comunicarlo a los clientes.

---

### CATEGORIA 4 — Marketing del Negocio
data-cat="marketing" · 8 prompts

**#27 — Post de Instagram para plato de carta**
Compatible con: AI Chef Pro · ChatGPT · Claude

Texto del prompt:
Escribe un post de Instagram para presentar el plato [NOMBRE] del restaurante [NOMBRE]. Ingredientes principales: [LISTA]. El post debe:
- Empezar con un gancho potente en la primera línea
- Contar la historia o concepto detrás del plato
- Incluir una llamada a la acción natural
- Finalizar con 15-20 hashtags relevantes
- Tono: [ELEGANTE/CERCANO/APASIONADO/INFORMATIVO]
- Longitud: 150-200 palabras de texto + hashtags

---

**#28 — Contenido SEO local para blog de restaurante**
Compatible con: AI Chef Pro · Claude · ChatGPT

Texto del prompt:
Escribe un artículo de blog SEO-optimizado para el restaurante [NOMBRE] en [CIUDAD]. Keyword objetivo: [PLATO/TIPO DE COCINA] en [CIUDAD]. Incluye:
- H1 optimizado con keyword
- Introducción con keyword natural en primeros 100 palabras
- Descripción de la experiencia con contenido de valor real
- Sección por qué visitarnos con diferenciadores
- Información práctica (horarios, dirección, reservas)
- Meta description de 155 caracteres
Longitud: 600-800 palabras. Tono natural, no sobreoptimizado.

---

**#29 — Respuesta profesional a reseña negativa**
Compatible con: AI Chef Pro · Claude · ChatGPT

Texto del prompt:
Un cliente ha dejado esta reseña negativa: [PEGAR RESEÑA]. Redacta una respuesta pública que:
- Agradezca el feedback sin ser condescendiente
- Reconozca el problema si es legítimo
- Explique brevemente qué se hará al respecto
- Invite al cliente a una segunda oportunidad
- No sea defensiva ni agresiva
Máximo 100-120 palabras. Firmado por: [NOMBRE/CARGO]

---

**#30 — Plan de contenido mensual para RRSS**
Compatible con: AI Chef Pro · ChatGPT · Claude

Texto del prompt:
Crea un plan de contenido para redes sociales del mes de [MES] para el restaurante [NOMBRE/TIPO]. Frecuencia: [N posts/semana]. Redes: [Instagram/Facebook/TikTok]. Incluye para cada publicación:
- Día y hora de publicación
- Formato (foto/reel/story/carrusel)
- Tema y concepto del contenido
- Copy resumido o idea principal
- Hashtags sugeridos
Ratio recomendado: 70% valor, 20% comunidad, 10% venta.

---

**#31 — Email marketing para base de clientes**
Compatible con: AI Chef Pro · Claude · ChatGPT

Texto del prompt:
Redacta un email de marketing para nuestra base de clientes. Objetivo: [ANUNCIAR NUEVA CARTA/EVENTO/OFERTA/REAPERTURA]. El email debe:
- Asunto irresistible (máx. 50 caracteres)
- Preheader complementario
- Cuerpo cálido y personal (no corporativo)
- Un único CTA claro
- Sin lenguaje de spam
- Posdata con toque humano
Tono: como si lo escribiera el chef/propietario personalmente. Máximo 200 palabras.

---

**#32 — Script para Reel o TikTok gastronómico**
Compatible con: AI Chef Pro · ChatGPT · Claude

Texto del prompt:
Crea el script completo para un Reel/TikTok de [DURACIÓN: 30/45/60 segundos] mostrando [PLATO/TÉCNICA/RECETA/DETRÁS DE CÁMARAS]. El script incluye:
- Gancho visual para los primeros 2 segundos
- Estructura de escenas con descripción visual
- Texto en pantalla (subtítulos/overlays)
- Música recomendada (tipo/mood)
- CTA final
El objetivo es [VIRALIZARSE/EDUCAR/VENDER/CONSTRUIR MARCA].

---

**#33 — Storytelling del chef para bio profesional**
Compatible con: AI Chef Pro · Claude · ChatGPT

Texto del prompt:
Escribe la bio profesional de [NOMBRE] para web, prensa y RRSS. Datos: [TRAYECTORIA, FORMACIÓN, RESTAURANTES, FILOSOFÍA, LOGROS]. Dame:
- Versión larga (300 palabras) para web y prensa
- Versión corta (80 palabras) para RRSS
- Versión ultra corta (1 frase de impacto) para presentaciones
- Tono: [ELEGANTE/CERCANO/ÉPICO]
Que transmita autenticidad, no un CV frío.

---

**#34 — Propuesta de colaboración con influencer**
Compatible con: AI Chef Pro · Claude · ChatGPT

Texto del prompt:
Redacta un mensaje de colaboración para un influencer gastronómico con [N] seguidores en [PLATAFORMA]. Nuestro restaurante: [NOMBRE Y DESCRIPCIÓN BREVE]. La propuesta: [DESCRIPCIÓN]. El mensaje debe:
- Ser personalizado (mencionar algo específico de su perfil)
- Ser directo sobre lo que proponemos
- Explicar el beneficio mutuo
- No sonar genérico
- Incluir un CTA concreto
Máximo 120 palabras.

---

### CATEGORIA 5 — Pastelería, Panadería y Chocolatería
data-cat="pasteleria" · 7 prompts

**#35 — Postre de restaurante contemporáneo**
Compatible con: AI Chef Pro · ChatGPT · Claude

Texto del prompt:
Diseña un postre de restaurante de alta cocina que sea visualmente impactante y técnicamente ejecutable en servicio. Debe incluir al menos 3 componentes con diferentes texturas (crujiente, cremoso, gelificado). Ingrediente o concepto protagonista: [INGREDIENTE/CONCEPTO]. Restricciones: [ALÉRGENOS A EVITAR]. Incluye: nombre del postre, historia del plato, receta completa, técnicas específicas y descripción del emplatado.

---

**#36 — Formulación de ganache de chocolate**
Compatible con: AI Chef Pro · ChatGPT · Claude

Texto del prompt:
Formula una ganache de chocolate con las siguientes características:
- Tipo de chocolate: [NEGRO XX%/LECHE/BLANCO/RUBIO]
- Aplicación: [RELLENO DE BOMBÓN/TRUFA/COBERTURA/TARTA/HELADO]
- Textura final deseada: [FIRME/BLANDA/FLUIDA/PARA MOLDEAR]
- Ingredientes adicionales a incorporar: [LISTA]
Dame: ratio chocolate/nata, temperatura de trabajo, proceso detallado, tiempo de cristalización y consejos de conservación.

---

**#37 — Pan artesanal con masa madre**
Compatible con: AI Chef Pro · Claude · Perplexity

Texto del prompt:
Crea una receta de pan artesanal con masa madre con estas especificaciones:
- Tipo de harina: [TIPO Y FUERZA]
- Hidratación deseada: [%]
- Incorporaciones: [SEMILLAS/FRUTOS SECOS/ACEITUNAS/ESPECIAS/NINGUNA]
- Formato final: [HOGAZA/BARRA/ROLLS/CHAPATA]
- Horneado en: [HORNO DOMÉSTICO/HORNO DE PANADERÍA/COCOTTE]
Incluye: fórmula de la masa madre, proceso completo con tiempos de fermentación, temperatura de cocción y trucos para corteza perfecta.

---

**#38 — Formulación de helado artesanal**
Compatible con: AI Chef Pro · ChatGPT · Claude

Texto del prompt:
Formula un helado artesanal con las siguientes características:
- Sabor principal: [SABOR]
- Tipo: [CREMOSO/SORBETE/SEMIFRÍO/GRANIZADO]
- Restricciones: [SIN LACTOSA/VEGANO/SIN AZÚCAR/CONVENCIONAL]
- Uso: [RESTAURANTE/HELADERÍA/VENTA AL PÚBLICO]
Proporciona: fórmula completa con porcentajes, índice de dulzor y congelación, proceso de elaboración, temperatura de servicio y sugerencia de maridaje o presentación.

---

**#39 — Tarta de celebración: diseño y receta**
Compatible con: AI Chef Pro · ChatGPT · Claude

Texto del prompt:
Diseña una tarta de celebración para [OCASIÓN] para [N] personas. Estilo visual: [ELEGANTE/MODERNO/RÚSTICO/TEMÁTICO]. Sabores deseados: [LISTA]. Restricciones: [ALÉRGENOS]. Proporciona:
- Concepto visual detallado (capas, colores, decoración)
- Receta completa de bizcocho, crema y cobertura
- Estructura de capas y montaje
- Técnicas de decoración
- Timeline de producción (qué hacer cada día)

---

**#40 — Tabla de temperaturas de templado de chocolate**
Compatible con: AI Chef Pro · ChatGPT · Gemini

Texto del prompt:
Necesito la guía completa de templado de chocolate para trabajo profesional. Para cada tipo de chocolate (negro, con leche, blanco, rubio/caramel) dame:
- Temperatura de fusión
- Temperatura de enfriamiento (1ª bajada)
- Temperatura de trabajo (subida final)
- Señales visuales para saber si está bien templado
- Errores comunes y cómo corregirlos
- Método alternativo de templado por siembra y por tablado
Formato: tabla comparativa + notas de proceso.

---

**#41 — Colección de petit fours para restaurante**
Compatible con: AI Chef Pro · Claude · ChatGPT

Texto del prompt:
Diseña una colección de 6 petit fours para el final de la comida en un restaurante de [TIPO/ESTILO]. La colección debe:
- Tener coherencia visual y de concepto entre las 6 piezas
- Combinar técnicas: gelificación, chocolate, crujiente, cremoso
- Ser ejecutable en producción diaria para [N] servicios
- Temporada: [ESTACIÓN]
- Sin: [ALÉRGENOS]
Para cada pieza: nombre, descripción, receta resumida y técnica principal.

---

### CATEGORIA 6 — Food Pairing
data-cat="food-pairing" · 8 prompts

**#42 — Maridaje molecular entre dos ingredientes**
Compatible con: AI Chef Pro · Claude · Perplexity

Texto del prompt:
Analiza la compatibilidad molecular entre [INGREDIENTE 1] y [INGREDIENTE 2] basándote en sus compuestos aromáticos compartidos. Dime:
- Compuestos aromáticos que comparten
- Nivel de compatibilidad (alta/media/baja) y por qué
- Cómo potenciar esa combinación en cocina (técnicas recomendadas)
- 3 ideas concretas de platos o preparaciones que aprovechen ese maridaje
- Ingrediente puente que puede unir ambos si la compatibilidad es baja

---

**#43 — Sustituto perfecto para un ingrediente**
Compatible con: AI Chef Pro · ChatGPT · Claude

Texto del prompt:
Necesito un sustituto para [INGREDIENTE ORIGINAL] en esta receta: [DESCRIPCIÓN BREVE]. El motivo es: [ALERGIA/NO DISPONIBLE/PRECIO/TEMPORADA]. El sustituto debe:
- Mantener el perfil de sabor lo más similar posible
- Funcionar con la misma técnica de cocción
- Estar disponible en [REGIÓN/TEMPORADA]
Dame las 3 mejores opciones ordenadas por similitud, con ajustes de cantidad y cualquier modificación necesaria en la técnica.

---

**#44 — Maridaje vino y plato**
Compatible con: AI Chef Pro · ChatGPT · Claude

Texto del prompt:
Recomienda el maridaje de vino ideal para este plato: [DESCRIPCIÓN DEL PLATO]. Considera:
- Intensidad del plato y equilibrio vino/comida
- Región vinícola preferida si aplica: [REGIÓN O "cualquiera"]
- Presupuesto por botella: [€]
- Servicio: [RESTAURANTE/CENA EN CASA/EVENTO]
Dame: 3 opciones (una segura, una interesante, una sorprendente), con varietal, DO o región, y explicación de por qué funciona ese maridaje.

---

**#45 — Combinaciones inesperadas con base científica**
Compatible con: AI Chef Pro · Claude · Perplexity

Texto del prompt:
Propón 5 combinaciones de ingredientes inesperadas o contraintuitivas que estén justificadas por food pairing científico. Para cada combinación:
- Los dos (o más) ingredientes
- Por qué funciona (compuestos compartidos o contraste equilibrado)
- Una aplicación gastronómica concreta
- Nivel de sorpresa para el comensal (del 1 al 5)
Ingrediente o perfil de cocina de referencia: [INGREDIENTE O ESTILO]

---

**#46 — Perfil sensorial de un plato**
Compatible con: AI Chef Pro · ChatGPT · Claude

Texto del prompt:
Analiza el perfil sensorial completo de este plato: [DESCRIPCIÓN]. Evalúa:
- Sabores predominantes y secundarios (dulce, salado, ácido, amargo, umami, picante)
- Texturas presentes y su contraste
- Aromas principales y cómo evolucionan
- Temperatura y contraste térmico
- Equilibrio general: ¿qué sobresale? ¿qué falta?
- Recomendaciones para mejorar el balance sensorial
Formato: análisis detallado + tabla resumen.

---

**#47 — Menú monoproducto**
Compatible con: AI Chef Pro · Claude · ChatGPT

Texto del prompt:
Diseña un menú degustación de 5 pasos donde el protagonista absoluto de todos los platos sea [INGREDIENTE]. El reto: que cada plato muestre una faceta completamente diferente del mismo ingrediente (crudo, cocido, fermentado, deshidratado, en salsa, etc.). Incluye: nombre de cada plato, técnica aplicada al ingrediente protagonista y cómo evoluciona la experiencia de principio a fin.

---

**#48 — Adaptación de receta a restricción dietética**
Compatible con: AI Chef Pro · ChatGPT · Claude

Texto del prompt:
Adapta esta receta: [PEGAR RECETA] para que sea apta para [VEGANO/CELÍACO/SIN LACTOSA/SIN FRUTOS SECOS/DIABÉTICO]. La adaptación debe:
- Mantener el espíritu y los sabores del plato original
- Indicar cada sustitución con su equivalencia exacta
- Advertir si algún cambio afecta significativamente a la textura o sabor
- Verificar que el resultado final cumple completamente con la restricción
- Si hay pérdida de calidad, proponer compensaciones

---

**#49 — Contraste de texturas en un plato**
Compatible con: AI Chef Pro · Claude · ChatGPT

Texto del prompt:
Quiero añadir contraste de texturas a este plato que actualmente es demasiado uniforme: [DESCRIPCIÓN DEL PLATO]. Propón:
- 3 elementos crujientes que encajen con el perfil de sabor
- 2 elementos cremosos o gelificados como contrapunto
- 1 elemento que aporte temperatura contrastante si es apropiado
Para cada propuesta: ingrediente, técnica de elaboración y cómo incorporarlo al emplatado sin que rompa la coherencia del plato.

---

### CATEGORIA 7 — Alérgenos y Seguridad Alimentaria
data-cat="alergenos" · 6 prompts

**#50 — Análisis de alérgenos en una receta**
Compatible con: AI Chef Pro · ChatGPT · Claude

Texto del prompt:
Analiza los alérgenos presentes en esta receta: [PEGAR RECETA COMPLETA CON INGREDIENTES]. Identifica:
- Alérgenos de declaración obligatoria presentes (los 14 de la normativa europea)
- Ingredientes que pueden contener alérgenos ocultos o trazas
- Riesgo de contaminación cruzada según las técnicas usadas
- Sustitutos posibles para eliminar cada alérgeno identificado
- Cómo comunicarlo correctamente en la carta

---

**#51 — Protocolo de atención a cliente con alergia**
Compatible con: AI Chef Pro · Claude · ChatGPT

Texto del prompt:
Crea un protocolo de atención para cuando un cliente informa de una alergia o intolerancia alimentaria en sala. El protocolo debe cubrir:
- Cómo recibir la información del cliente (preguntas clave a hacer)
- Proceso de comunicación entre sala y cocina
- Verificación antes de servir el plato
- Qué hacer si hay duda sobre contaminación cruzada
- Cómo documentar el incidente
Formato: checklist paso a paso que pueda imprimirse y colocarse en cocina y sala.

---

**#52 — Ficha técnica con declaración de alérgenos**
Compatible con: AI Chef Pro · ChatGPT · Gemini

Texto del prompt:
Crea la ficha técnica completa del plato [NOMBRE] con declaración de alérgenos para uso interno y/o carta. Ingredientes: [LISTA COMPLETA]. Incluye:
- Tabla de alérgenos (los 14 de la normativa europea) con presencia confirmada/posibles trazas/ausente
- Instrucciones de elaboración para minimizar contaminación cruzada
- Formato apto para imprimir y colocar en cocina
- Versión resumida para incluir en carta o app de pedidos

---

**#53 — Menú completo apto para celíacos**
Compatible con: AI Chef Pro · Claude · ChatGPT

Texto del prompt:
Diseña un menú completo de [NÚMERO DE PLATOS] que sea 100% apto para celíacos (sin gluten en ingredientes y sin contaminación cruzada). El menú es para [TIPO DE ESTABLECIMIENTO]. Debe:
- Ser gastronómicamente atractivo, no una versión reducida
- Especificar qué harinas alternativas usar en cada preparación
- Indicar el protocolo de cocina para evitar contaminación cruzada
- Incluir postres sin gluten que no parezcan un compromiso

---

**#54 — Etiquetado de producto artesanal para venta**
Compatible con: AI Chef Pro · ChatGPT · Claude

Texto del prompt:
Necesito el etiquetado correcto para vender este producto artesanal: [DESCRIPCIÓN DEL PRODUCTO]. Se venderá en [TIENDA PROPIA/MERCADO/ONLINE/TERCEROS]. La normativa aplicable es europea (UE 1169/2011). Proporciona:
- Lista de ingredientes en orden descendente de peso
- Alérgenos en negrita o resaltados
- Información nutricional por 100g y por porción
- Vida útil recomendada y condiciones de conservación
- Información del productor que debe aparecer
- Advertencias obligatorias si aplica

---

**#55 — Plan de formación APPCC para equipo**
Compatible con: AI Chef Pro · Claude · ChatGPT

Texto del prompt:
Crea un plan de formación básica en APPCC (Análisis de Peligros y Puntos de Control Crítico) para el equipo de [TIPO DE ESTABLECIMIENTO] con [N] personas. El plan debe incluir:
- Conceptos fundamentales de seguridad alimentaria (resumen ejecutivo)
- Los puntos de control crítico más relevantes para ese tipo de negocio
- Tabla de temperaturas de seguridad para conservación y cocción
- Checklist diaria de control de higiene y temperatura
- Formato de sesión formativa de 45 minutos para el equipo

---

### CATEGORIA 8 — Gestión de Negocio
data-cat="negocio" · 7 prompts

**#56 — Plan de negocio para restaurante**
Compatible con: AI Chef Pro · Claude · ChatGPT

Texto del prompt:
Ayúdame a estructurar el plan de negocio para [TIPO DE RESTAURANTE/CONCEPTO] en [CIUDAD]. Datos del proyecto: [DESCRIPCIÓN BREVE]. El plan debe cubrir:
- Análisis de mercado y competencia local
- Propuesta de valor diferencial
- Modelo de negocio y fuentes de ingresos
- Estructura de costes fijos y variables
- Proyección de ingresos a 12 meses (con escenario conservador y optimista)
- Inversión inicial estimada y punto de equilibrio
- Estrategia de marketing de lanzamiento

---

**#57 — Descripción de concepto para franquicia**
Compatible con: AI Chef Pro · ChatGPT · Claude

Texto del prompt:
Redacta la descripción de concepto para presentar [NOMBRE DEL RESTAURANTE/CADENA] como franquicia potencial. El documento debe incluir:
- Historia y filosofía de la marca (origen y evolución)
- Propuesta de valor para el franquiciado
- Descripción del modelo operativo replicable
- Ventajas competitivas del concepto
- Perfil ideal del franquiciado
- Resumen de inversión y retorno estimado
Tono: documento ejecutivo profesional de 2 páginas.

---

**#58 — Manual de operaciones básico**
Compatible con: AI Chef Pro · Claude · ChatGPT

Texto del prompt:
Crea el índice y los primeros apartados del manual de operaciones para [TIPO DE NEGOCIO GASTRONÓMICO]. El manual debe cubrir:
- Estándares de servicio y protocolo de atención al cliente
- Procedimientos de apertura y cierre
- Gestión de reservas e incidencias
- Estándares de higiene y seguridad alimentaria
- Protocolo de formación de nuevo personal
Formato: documento estructurado que pueda entregarse al personal en su primer día.

---

**#59 — Análisis DAFO del negocio**
Compatible con: AI Chef Pro · ChatGPT · Claude

Texto del prompt:
Realiza un análisis DAFO completo para [TIPO DE NEGOCIO GASTRONÓMICO] en [CIUDAD/CONTEXTO]. Datos del negocio: [DESCRIPCIÓN]. Incluye:
- Debilidades internas a trabajar
- Amenazas externas a monitorizar
- Fortalezas a potenciar en la comunicación
- Oportunidades del mercado a aprovechar
Para cada punto: al menos 4 ítems con descripción y nivel de impacto (alto/medio/bajo). Añade las 3 acciones más urgentes que derivan del análisis.

---

**#60 — Job description para puesto clave**
Compatible con: AI Chef Pro · Claude · ChatGPT

Texto del prompt:
Redacta la descripción de puesto para [NOMBRE DEL PUESTO: chef ejecutivo/jefe de sala/pastelero/bartender/gerente] en [TIPO DE ESTABLECIMIENTO]. Incluye:
- Misión del puesto en el equipo
- Responsabilidades principales (8-10 puntos)
- Requisitos de experiencia y formación
- Competencias clave (técnicas y personales)
- Condiciones del puesto (jornada, tipo de contrato si aplica)
- Descripción de la cultura del equipo para atraer al perfil adecuado

---

**#61 — Estrategia de precios para nueva carta**
Compatible con: AI Chef Pro · ChatGPT · Claude

Texto del prompt:
Ayúdame a definir la estrategia de precios para la nueva carta de [TIPO DE RESTAURANTE]. Datos del negocio: ticket medio actual [€], coste fijo mensual [€], número de cubiertos por servicio [N], servicios por semana [N]. Propón:
- Rango de precios por categoría (entrantes, principales, postres, bebidas)
- Estrategia de pricing psicológico (números pares/impares, anclaje)
- Estructura de márgenes objetivo por categoría
- Cómo comunicar la subida de precios si es necesaria

---

**#62 — Propuesta de consultoría gastronómica**
Compatible con: AI Chef Pro · Claude · ChatGPT

Texto del prompt:
Redacta una propuesta de consultoría gastronómica para el cliente [TIPO DE NEGOCIO]. El cliente tiene este problema o necesidad: [DESCRIPCIÓN]. La propuesta debe incluir:
- Diagnóstico inicial del problema
- Metodología de trabajo propuesta
- Fases del proyecto con entregables por fase
- Equipo y perfil del consultor
- Inversión y forma de pago
- Resultados esperados y métricas de éxito
Tono: profesional y orientado a resultados, no academicista.

---

### CATEGORIA 9 — Liderazgo, Equipos y Bienestar
data-cat="liderazgo" · 6 prompts

**#63 — Gestión del estrés en servicio de alta presión**
Compatible con: AI Chef Pro · Claude · ChatGPT

Texto del prompt:
Actúa como coach especializado en bienestar para profesionales de la hostelería. Tengo este problema de estrés en mi equipo/en mí mismo: [DESCRIPCIÓN DE LA SITUACIÓN]. Necesito:
- Técnicas de gestión del estrés aplicables DURANTE el servicio (no solo después)
- Una rutina de 5 minutos pre-servicio para centrar al equipo
- Señales de alerta tempranas de burnout en cocina
- Cómo comunicar al equipo que hay un problema sin generar más tensión
- 3 cambios en la dinámica de trabajo que pueden reducir la presión crónica

---

**#64 — Feedback constructivo para el equipo**
Compatible con: AI Chef Pro · Claude · ChatGPT

Texto del prompt:
Necesito dar feedback sobre un problema de rendimiento o actitud a [PERFIL: cocinero/jefe de partida/camarero/pastelero]. La situación es: [DESCRIPCIÓN OBJETIVA DEL PROBLEMA]. El empleado lleva [TIEMPO] en el equipo. Ayúdame a:
- Estructurar la conversación (modelo SBI: Situación-Comportamiento-Impacto)
- Las frases exactas para abrir la conversación sin generar defensividad
- Cómo escuchar activamente su perspectiva
- Cómo acordar un plan de mejora concreto y medible
- Qué decir si la conversación se pone tensa

---

**#65 — Rutina de mindfulness pre-servicio**
Compatible con: AI Chef Pro · Claude · ChatGPT

Texto del prompt:
Diseña una rutina de mindfulness de 8-10 minutos específica para el equipo de cocina antes de un servicio intenso. La rutina debe:
- Ser práctica, no esotérica (adaptada a profesionales escépticos)
- Aplicarse en el propio espacio de trabajo, sin cambiar de ropa ni de lugar
- Incluir técnicas de respiración, enfoque mental y activación física suave
- Terminar con un ritual de equipo que genere cohesión
- Tener un guion que el jefe de cocina pueda leer en voz alta

---

**#66 — Reunión post-servicio efectiva**
Compatible con: AI Chef Pro · Claude · ChatGPT

Texto del prompt:
Crea el esquema de una reunión post-servicio de 15 minutos para el equipo de [TIPO DE ESTABLECIMIENTO]. El servicio de hoy tuvo: [DESCRIPCIÓN: incidencias, momentos positivos, etc.]. La reunión debe:
- Empezar por lo que salió bien (refuerzo positivo)
- Abordar los problemas con enfoque en soluciones, no en culpas
- Generar 1-2 acciones concretas para el próximo servicio
- Cerrar con algo que deje al equipo con energía positiva
- Durar máximo 15 minutos (guion con tiempos)

---

**#67 — Plan de desarrollo profesional para empleado**
Compatible con: AI Chef Pro · Claude · ChatGPT

Texto del prompt:
Crea un plan de desarrollo profesional a 6 meses para [PERFIL DEL EMPLEADO: cocinero de X años de experiencia, especialidad en Y]. El empleado quiere crecer hacia: [OBJETIVO PROFESIONAL]. El plan debe incluir:
- Evaluación de competencias actuales vs. requeridas para el objetivo
- Formaciones específicas recomendadas (cursos, talleres, stages)
- Responsabilidades progresivas dentro del equipo
- Hitos de evaluación cada 2 meses
- Cómo involucrar al empleado en el proceso para que lo sienta suyo

---

**#68 — Resolución de conflicto en brigada**
Compatible con: AI Chef Pro · Claude · ChatGPT

Texto del prompt:
Tengo un conflicto entre dos miembros de mi equipo: [DESCRIPCIÓN OBJETIVA DE LA SITUACIÓN, sin nombres]. El conflicto está afectando a: [CÓMO AFECTA AL SERVICIO/AMBIENTE]. Como jefe de cocina o gerente, ayúdame a:
- Entender las posibles causas raíz del conflicto
- Cómo abordar la conversación por separado con cada parte
- Cómo facilitar una conversación conjunta si es necesario
- Qué límites y reglas de equipo establecer para evitar recurrencia
- Cuándo es el momento de escalar el problema a RRHH

---

## SECCION 5 — CTA HACIA AI CHEF PRO

**Título:** ¿Quieres usar estos prompts con las 55+ apps de AI Chef Pro?
**Texto:** La suite completa para toda la hostelería: chefs, gerentes, pasteleros, bartenders y dueños de negocio. Food Pairing AI, Mermas GenCal, Catering AI+ y mucho más.
**Botón:** Descubrir AI Chef Pro → https://aichef.pro

---

## FOOTER MINIMO

Sin header/footer global. Solo:
© 2026 AI Chef Pro · Pro Prompts Library · Todos los derechos reservados
Links: aichef.pro · Contacto

---

## RESUMEN DE SEGURIDAD — Lo que garantiza acceso privado real

1. La ruta /pro-prompts-library está protegida por ProtectedRoute.tsx
2. Sin JWT válido en sessionStorage → redirect automático a /pro-prompts-ebook
3. El JWT solo se genera en la Netlify Function tras verificar el pago real con Stripe API
4. Las URLs de descarga de PDFs se sirven también via Netlify Function con verificación de JWT
5. Meta robots noindex, nofollow — Google no indexa la página
6. El usuario recibe además un email con su magic link personal para acceso futuro

---

## NOTAS FINALES PARA CLAUDE CODE

- Variables de entorno del servidor (sin prefijo VITE_): STRIPE_SECRET_KEY, JWT_SECRET, RESEND_API_KEY, PDF_EBOOK_URL, PDF_BONUS1_URL, PDF_BONUS23_URL
- Variables de entorno del cliente (con prefijo VITE_): solo VITE_STRIPE_PAYMENT_LINK (en la landing)
- La library NUNCA recibe variables de entorno del servidor directamente — todo pasa por Netlify Functions
- Esta página NO incluye header/nav global ni footer global del sitio
- Respetar todos los tokens de Tailwind y fuentes ya instalados en el proyecto
- Los prompts se pueden ampliar iterativamente añadiendo nuevos PromptCard sin cambiar la arquitectura
