# AI Chef Pro — Lead Magnet Apps 2026
## Propuestas + Guía de Desarrollo para Claude Code

> **Documento:** Especificaciones técnicas y estratégicas para el desarrollo de 8 aplicaciones gratuitas estilo lead magnet integradas en la Landing Page 2026 de aichef.pro  
> **Fecha:** Febrero 2026  
> **Destinatario:** Claude Code — Agente de desarrollo Landing Page AI Chef Pro v2026  
> **Stack recomendado:** React + Tailwind CSS (integrado en la landing existente) o HTML/CSS/JS vanilla si la landing es estática

---

## ÍNDICE

1. [Contexto del Proyecto](#contexto-del-proyecto)
2. [Instrucciones Globales para Claude Code](#instrucciones-globales-para-claude-code)
3. [App 01 — FoodCost Calculator](#app-01--foodcost-calculator)
4. [App 02 — Alérgenos Checker](#app-02--alergenos-checker)
5. [App 03 — Gastro Content Calendar](#app-03--gastro-content-calendar)
6. [App 04 — Menu Profit Simulator](#app-04--menu-profit-simulator)
7. [App 05 — MenuCopy AI](#app-05--menucopy-ai)
8. [App 06 — Digital Chef Score](#app-06--digital-chef-score)
9. [App 07 — Brigade Calculator](#app-07--brigade-calculator)
10. [App 08 — Tasting Menu Generator](#app-08--tasting-menu-generator)
11. [Integración en la Landing Page](#integracion-en-la-landing-page)
12. [Estrategia de CTA y Conversión](#estrategia-de-cta-y-conversion)
13. [Tabla Resumen](#tabla-resumen)

---

## CONTEXTO DEL PROYECTO

**AI Chef Pro** (aichef.pro) es una suite de inteligencia artificial para chefs, cocineros, gerentes y dueños de restaurantes. La plataforma ofrece 55+ aplicaciones especializadas en 7 idiomas.

**Planes de pago actuales** (únicos a promocionar):
- **25€/mes** — Premium Pro
- **50€/mes** — Premium Plus
- **95€/mes** — Plan Profesional
- **950€/año** — Plan Anual (equivale a descuento significativo)

**Página de precios oficial:** https://app.aichef.pro/pricing

**Objetivo de estas 8 apps:** Actuar como lead magnets en el footer y secciones estratégicas de la Landing 2026, captando la atención del usuario final (chef, gerente, dueño) mediante herramientas gratuitas de valor inmediato, para convertirlos en suscriptores de pago.

---

## INSTRUCCIONES GLOBALES PARA CLAUDE CODE

### Principios de desarrollo

```
PRIORIDAD 1: Cada app debe funcionar de forma completamente autónoma (sin backend)
PRIORIDAD 2: Resultados instantáneos — el usuario no debe esperar más de 2 segundos
PRIORIDAD 3: Diseño mobile-first, limpio, profesional y coherente con la identidad de aichef.pro
PRIORIDAD 4: CTA visible post-resultado, que dirija a app.aichef.pro/pricing
PRIORIDAD 5: Sin cookies, sin registro previo, sin fricción de entrada
```

### Stack técnico recomendado

```
- Framework: React con Tailwind CSS (si la landing usa ese stack)
- Alternativa: HTML5 + CSS3 + Vanilla JS (si la landing es estática)
- IA calls: Anthropic API (claude-sonnet-4-6) para las apps que generen texto con IA
- Sin localStorage ni sessionStorage (no soportado en el entorno Claude.ai)
- Estado: useState de React o variables JS en memoria
- Iconos: lucide-react o SVG inline
```

### Estructura de componente estándar para cada app

```jsx
// Estructura base recomendada para cada lead magnet
const AppLeadMagnet = () => {
  // 1. Estado inicial (inputs del usuario)
  // 2. Estado de resultado (output calculado o generado)
  // 3. Estado de loading (si hay llamada a API)
  // 4. Función de cálculo o llamada a Anthropic API
  // 5. Sección de INPUT — formulario simple
  // 6. Sección de RESULTADO — tarjeta con el output
  // 7. Sección de CTA — botón hacia app.aichef.pro/pricing
}
```

### Paleta de colores AI Chef Pro (usar consistentemente)

```css
--color-primary: #1a1a2e;       /* Navy oscuro — fondos principales */
--color-accent: #e94560;        /* Rojo coral — CTAs y acentos */
--color-secondary: #16213e;     /* Azul oscuro — cards */
--color-light: #f5f5f5;         /* Gris claro — fondos de sección */
--color-text: #333333;          /* Texto principal */
--color-success: #27ae60;       /* Verde — resultados positivos */
--color-warning: #f39c12;       /* Naranja — alertas */
--color-danger: #e74c3c;        /* Rojo — resultados críticos */
```

### Llamadas a la API de Anthropic (para apps con IA generativa)

```javascript
// Patrón estándar para llamadas a Anthropic API desde las apps
const callAnthropicAPI = async (prompt) => {
  const response = await fetch("https://api.anthropic.com/v1/messages", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      model: "claude-sonnet-4-6",
      max_tokens: 1000,
      messages: [{ role: "user", content: prompt }]
    })
  });
  const data = await response.json();
  return data.content[0].text;
};
```

---

## APP 01 — FoodCost Calculator

### Nombre completo
**FoodCost Calculator by AI Chef Pro**

### Descripción funcional
Calculadora de coste de plato por ración. El usuario introduce ingredientes con cantidad y precio de compra unitario. La app calcula food cost por ración, precio de venta recomendado (basado en porcentaje objetivo configurable) y margen bruto.

### Por qué convierte
El food cost es el dolor número uno del propietario de restaurante. Ver el resultado en segundos genera un "aha moment" inmediato que conecta emocionalmente con la propuesta de valor de AI Chef Pro.

### Tipo de app
**Calculadora pura — sin IA generativa, sin API calls**

### Inputs del usuario

| Campo | Tipo | Descripción |
|-------|------|-------------|
| Nombre del plato | Text input | Ej: "Lubina a la sal con verduras" |
| Ingredientes (nombre) | Text input repetible | Filas dinámicas de ingredientes |
| Cantidad usada | Number input | En gramos, ml o unidades |
| Precio de compra | Number input | Precio por kg, litro o unidad |
| % Food Cost objetivo | Range slider | Default: 30% — rango: 20%-45% |

### Lógica de cálculo

```javascript
// Coste de cada ingrediente por ración
const costePorIngrediente = (cantidad, precioCompra, unidad) => {
  // si unidad es kg: precio / 1000 * cantidad_en_gramos
  // si unidad es litro: precio / 1000 * cantidad_en_ml
  // si unidad es unidad: precio * cantidad
  return costeCalculado;
};

// Food cost total del plato
const foodCostTotal = ingredientes.reduce((sum, ing) => sum + ing.coste, 0);

// Precio de venta recomendado
const precioVentaRecomendado = foodCostTotal / (porcentajeFoodCost / 100);

// Margen bruto
const margenBruto = precioVentaRecomendado - foodCostTotal;
const margenPorcentaje = ((margenBruto / precioVentaRecomendado) * 100).toFixed(1);
```

### Output / Resultado

```
┌─────────────────────────────────────────┐
│  ANÁLISIS DE FOOD COST                  │
│  Lubina a la sal con verduras           │
├─────────────────────────────────────────┤
│  Coste de ingredientes: €4,82           │
│  Food Cost real: 28,3%  ✅              │
│  Precio de venta recomendado: €17,00   │
│  Margen bruto: €12,18 (71,7%)          │
├─────────────────────────────────────────┤
│  [Descarga el análisis completo en PDF] │
└─────────────────────────────────────────┘
```

**Semáforo visual:**
- Verde (✅): Food cost < 30%
- Naranja (⚠️): Food cost 30%-38%
- Rojo (🚨): Food cost > 38%

### CTA post-resultado
> 💡 *¿Quieres calcular toda tu carta, optimizar mermas y generar fichas técnicas automáticamente? **Empieza con AI Chef Pro →** [app.aichef.pro/pricing]*

### Notas de desarrollo para Claude Code

```
- Añadir botón "+" para agregar ingredientes dinámicamente (máximo 20)
- Permitir seleccionar unidad de medida por ingrediente (g, ml, ud)
- Slider de food cost objetivo con actualización en tiempo real
- Botón de reset completo
- Versión mobile: inputs apilados verticalmente
- NO requiere API call — todo es cálculo local
```

---

## APP 02 — Alérgenos Checker

### Nombre completo
**Alérgenos Checker by AI Chef Pro**

### Descripción funcional
El usuario pega o escribe la lista de ingredientes de un plato. La app detecta automáticamente los 14 alérgenos de declaración obligatoria según el Reglamento UE 1169/2011 y genera un informe visual con iconos, advertencias y texto listo para incluir en la carta.

### Por qué convierte
Cumplimiento legal = urgencia real y consecuencias económicas/legales. Cualquier restaurante en España necesita esto. Resuelve un problema de compliance inmediato.

### Tipo de app
**Detección por base de datos local + lógica de matching — sin API call obligatoria**  
*(Opcional: llamada a API para análisis de ingredientes complejos o términos ambiguos)*

### Los 14 alérgenos (base de datos interna)

```javascript
const ALERGENOS = {
  gluten: {
    nombre: "Gluten (cereales)",
    icono: "🌾",
    keywords: ["trigo", "harina", "centeno", "cebada", "avena", "espelta", 
               "kamut", "pan", "pasta", "sémola", "couscous", "bulgur",
               "cerveza", "salsa de soja", "panko", "miga de pan"]
  },
  crustaceos: {
    nombre: "Crustáceos",
    icono: "🦐",
    keywords: ["langosta", "bogavante", "cangrejo", "gamba", "langostino",
               "nécora", "percebe", "cigala", "centollo", "camarón"]
  },
  huevo: {
    nombre: "Huevo",
    icono: "🥚",
    keywords: ["huevo", "yema", "clara", "mayonesa", "merengue", 
               "tortilla", "lactonesa", "alioli", "hollandaise"]
  },
  pescado: {
    nombre: "Pescado",
    icono: "🐟",
    keywords: ["bacalao", "salmón", "atún", "lubina", "merluza", "dorada",
               "sardina", "anchoa", "boquerón", "pescado", "rodaballo",
               "salsa worcestershire", "pasta de anchoa"]
  },
  cacahuetes: {
    nombre: "Cacahuetes",
    icono: "🥜",
    keywords: ["cacahuete", "maní", "arachis", "groundnut"]
  },
  soja: {
    nombre: "Soja",
    icono: "🫘",
    keywords: ["soja", "tofu", "tempeh", "miso", "edamame", 
               "salsa de soja", "tamari", "leche de soja"]
  },
  lacteos: {
    nombre: "Lácteos (leche)",
    icono: "🥛",
    keywords: ["leche", "nata", "mantequilla", "queso", "yogur", 
               "crema", "ghee", "lactosa", "suero", "caseína",
               "mozzarella", "parmesano", "brie", "camembert"]
  },
  frutosSecos: {
    nombre: "Frutos de cáscara",
    icono: "🌰",
    keywords: ["almendra", "avellana", "nuez", "anacardo", "pistacho",
               "macadamia", "nuez de brasil", "pecana", "piñón",
               "pasta de almendra", "praline", "mazapán", "tahini"]
  },
  apio: {
    nombre: "Apio",
    icono: "🌿",
    keywords: ["apio", "celery", "apio nabo", "sal de apio"]
  },
  mostaza: {
    nombre: "Mostaza",
    icono: "🟡",
    keywords: ["mostaza", "semilla de mostaza", "harina de mostaza",
               "mostaza de dijon", "mostaza inglesa"]
  },
  sesamo: {
    nombre: "Sésamo",
    icono: "⚪",
    keywords: ["sésamo", "ajonjolí", "tahini", "aceite de sésamo",
               "pasta de sésamo", "semilla de sésamo"]
  },
  sulfitos: {
    nombre: "Dióxido de azufre y sulfitos",
    icono: "🍷",
    keywords: ["vino", "vinagre de vino", "fruta seca", "orejones",
               "pasas", "conservante e220", "e221", "e222", "e223",
               "e224", "sulfito", "dióxido de azufre", "mostaza seca"]
  },
  moluscos: {
    nombre: "Moluscos",
    icono: "🐙",
    keywords: ["almeja", "mejillón", "ostra", "calamar", "pulpo",
               "sepia", "berberecho", "navaja", "chipirón", "vieira",
               "caracol", "caracola"]
  },
  altramuces: {
    nombre: "Altramuces",
    icono: "🫛",
    keywords: ["altramuz", "lupino", "lupin", "harina de altramuz"]
  }
};
```

### Lógica de detección

```javascript
const detectarAlergenos = (textoIngredientes) => {
  const textoNormalizado = textoIngredientes.toLowerCase()
    .normalize("NFD").replace(/[\u0300-\u036f]/g, ""); // eliminar acentos
  
  const alergenosDetectados = [];
  
  Object.entries(ALERGENOS).forEach(([key, alergeno]) => {
    const encontrado = alergeno.keywords.some(keyword => 
      textoNormalizado.includes(keyword.toLowerCase()
        .normalize("NFD").replace(/[\u0300-\u036f]/g, ""))
    );
    if (encontrado) alergenosDetectados.push({ ...alergeno, key });
  });
  
  return alergenosDetectados;
};
```

### Output / Resultado

```
┌──────────────────────────────────────────────┐
│  ANÁLISIS DE ALÉRGENOS                       │
│  Tartar de lubina con alioli y pan de centeno│
├──────────────────────────────────────────────┤
│  ⚠️ CONTIENE 4 ALÉRGENOS DETECTADOS:        │
│                                              │
│  🐟 Pescado     🥚 Huevo                     │
│  🌾 Gluten      🧄 Apio (posible)            │
├──────────────────────────────────────────────┤
│  TEXTO PARA TU CARTA:                        │
│  "Contiene: pescado, huevo, gluten.          │
│  Puede contener trazas de otros alérgenos.  │
│  Consulte con nuestro personal."            │
│                                              │
│  [Copiar texto] [Descargar informe]          │
└──────────────────────────────────────────────┘
```

### CTA post-resultado
> 🔎 *¿Quieres gestionar los alérgenos de toda tu carta de forma automática y cumplir con la normativa EU 1169/2011? **Prueba ID Alérgenos en AI Chef Pro →** [app.aichef.pro/pricing]*

### Notas de desarrollo para Claude Code

```
- Textarea grande para pegar lista de ingredientes
- Detección en tiempo real mientras el usuario escribe (debounce 500ms)
- Iconos visuales grandes para cada alérgeno (accesibilidad)
- Botón "Copiar texto para carta" con confirmación visual
- Advertencia legal pequeña: "Esta herramienta es orientativa. 
  Consulta siempre con un especialista en seguridad alimentaria."
- Color coding: Rojo = detectado con certeza / Naranja = posible
```

---

## APP 03 — Gastro Content Calendar

### Nombre completo
**Gastro Content Calendar by AI Chef Pro**

### Descripción funcional
El usuario selecciona tipo de restaurante, redes sociales donde tiene presencia y el mes. La app genera un calendario editorial de 30 días con ideas de posts específicas, hashtags recomendados y fechas gastronómicas y festivas relevantes.

### Tipo de app
**IA generativa — requiere llamada a Anthropic API**

### Inputs del usuario

| Campo | Tipo | Opciones |
|-------|------|---------|
| Tipo de establecimiento | Select | Restaurante tradicional / Gastrobar / Pastelería / Pizzería / Food Truck / Catering / Bar de tapas |
| Redes activas | Multi-checkbox | Instagram / Facebook / TikTok / Pinterest / LinkedIn |
| Mes a planificar | Select | Enero — Diciembre |
| Frecuencia de publicación | Select | Diaria / 3 veces/semana / Semanal |
| Idioma | Select | Español / English |

### Prompt para Anthropic API

```javascript
const generateCalendarPrompt = (inputs) => `
Eres un experto en marketing gastronómico y community management para restaurantes en España.

Genera un calendario de contenidos editorial para ${inputs.mes} para un/a ${inputs.tipoRestaurante}.
Frecuencia: ${inputs.frecuencia}.
Redes sociales: ${inputs.redes.join(", ")}.

Para cada publicación incluye:
- Día del mes
- Red social objetivo
- Tipo de contenido (foto, video, reel, story, carrusel)
- Idea concreta del post (2-3 líneas)
- 5 hashtags específicos y relevantes
- Fecha gastronómica o festiva si aplica ese día

Incluye fechas clave de ${inputs.mes} como: festivos nacionales españoles, días internacionales gastronómicos, tendencias del sector.

Responde SOLO en JSON con esta estructura:
{
  "mes": "${inputs.mes}",
  "publicaciones": [
    {
      "dia": 1,
      "red": "Instagram",
      "tipo": "Reel",
      "idea": "...",
      "hashtags": ["#hash1", "#hash2", "#hash3", "#hash4", "#hash5"],
      "fechaEspecial": "Día Mundial del Chocolate"
    }
  ]
}
`;
```

### Output / Resultado
Calendario visual en formato de tabla/grid con color coding por red social y tipo de contenido.

### CTA post-resultado
> 📱 *¿Quieres generar contenido completo listo para publicar con IA para cada post de tu restaurante? **Descubre InstaFlow AI Pro y Gastro Calendar →** [app.aichef.pro/pricing]*

### Notas de desarrollo para Claude Code

```
- Loading spinner mientras genera el calendario (2-5 segundos)
- Renderizar el resultado como grid calendario visual (7 columnas = días de semana)
- Color coding por red social: morado=Instagram, azul=Facebook, negro=TikTok
- Botón "Regenerar" para obtener nueva versión
- Opción de exportar a formato texto simple
- Mobile: mostrar como lista cronológica en lugar de grid
```

---

## APP 04 — Menu Profit Simulator

### Nombre completo
**Menu Profit Simulator by AI Chef Pro**

### Descripción funcional
El usuario introduce datos clave de su negocio: ticket medio, cubiertos/servicio, número de servicios semanales y porcentajes de costes estimados. La app genera un diagnóstico de rentabilidad con semáforo visual, KPIs clave y 3 recomendaciones accionables.

### Tipo de app
**Calculadora financiera + recomendaciones estáticas — sin API call**

### Inputs del usuario

| Campo | Tipo | Ejemplo |
|-------|------|---------|
| Ticket medio por comensal | Number (€) | 28 |
| Cubiertos por servicio | Number | 45 |
| Servicios por semana | Number | 12 |
| % Food Cost estimado | Range slider | 32% |
| % Coste de personal | Range slider | 38% |
| % Gastos fijos (alquiler, suministros) | Range slider | 18% |

### Lógica de cálculo

```javascript
const calcularRentabilidad = (inputs) => {
  const ventasSemanales = inputs.ticketMedio * inputs.cubiertos * inputs.servicios;
  const ventasMensuales = ventasSemanales * 4.33;
  const ventasAnuales = ventasMensuales * 12;

  const costeFoodMensual = ventasMensuales * (inputs.foodCost / 100);
  const costePersonalMensual = ventasMensuales * (inputs.personal / 100);
  const gastosFijosMensual = ventasMensuales * (inputs.gastosFijos / 100);

  const totalCostes = costeFoodMensual + costePersonalMensual + gastosFijosMensual;
  const beneficioMensual = ventasMensuales - totalCostes;
  const margenNeto = ((beneficioMensual / ventasMensuales) * 100).toFixed(1);

  // Prime Cost (food + personal) — indicador clave de hostelería
  const primeCost = inputs.foodCost + inputs.personal;

  return {
    ventasMensuales,
    ventasAnuales,
    beneficioMensual,
    margenNeto,
    primeCost,
    zona: margenNeto > 15 ? "beneficio" : margenNeto > 5 ? "equilibrio" : "peligro"
  };
};
```

### Output / Resultado

```
┌──────────────────────────────────────────────┐
│  DIAGNÓSTICO DE RENTABILIDAD                 │
├──────────────────────────────────────────────┤
│  📊 VENTAS ESTIMADAS                         │
│  Mensual: €43.524  │  Anual: €522.288        │
├──────────────────────────────────────────────┤
│  💰 RESULTADO NETO MENSUAL                   │
│  €5.228  │  Margen: 12% ⚠️ ZONA EQUILIBRIO  │
├──────────────────────────────────────────────┤
│  🔑 PRIME COST: 70% (Óptimo: <65%)          │
│  Food Cost: 32% | Personal: 38%              │
├──────────────────────────────────────────────┤
│  💡 3 ACCIONES INMEDIATAS:                   │
│  1. Reducir food cost 2% = +€870/mes        │
│  2. Añadir 1 servicio/semana = +€1.890/mes  │
│  3. Subir ticket medio 2€ = +€1.170/mes     │
└──────────────────────────────────────────────┘
```

**Zonas de resultado:**
- 🟢 **BENEFICIO** — Margen neto > 15% — "Tu restaurante está en buena salud financiera"
- 🟡 **EQUILIBRIO** — Margen 5%-15% — "Tienes margen de mejora. Actúa ahora"
- 🔴 **ZONA DE PELIGRO** — Margen < 5% — "Tu negocio necesita optimización urgente"

### CTA post-resultado
> 💰 *¿Quieres un análisis completo de cada plato de tu carta para maximizar la rentabilidad? **Prueba AI Chef Pro y transforma los números de tu restaurante →** [app.aichef.pro/pricing]*

### Notas de desarrollo para Claude Code

```
- Sliders interactivos con actualización de resultado en tiempo real
- Gráfico de dona (donut chart) mostrando distribución de costes
- Tooltips explicativos sobre Prime Cost y KPIs hosteleros
- Sección de "¿Qué pasaría si...?" — sliders de simulación de mejora
- Formulario de captura de email ANTES de mostrar el resultado completo
  (mostrar preview parcial para incentivar el email)
```

---

## APP 05 — MenuCopy AI

### Nombre completo
**MenuCopy AI by AI Chef Pro**

### Descripción funcional
El usuario introduce nombre del plato e ingredientes principales. La app genera 3 versiones de descripción para la carta: clásica, emocional y km0/producto local. Incluye sugerencia de nombre alternativo si el original es genérico.

### Tipo de app
**IA generativa — requiere llamada a Anthropic API**

### Inputs del usuario

| Campo | Tipo | Ejemplo |
|-------|------|---------|
| Nombre actual del plato | Text | "Croquetas de jamón" |
| Ingredientes principales | Textarea | "Jamón ibérico, bechamel, pan rallado" |
| Estilo del restaurante | Select | Tradicional / Vanguardista / Informal / Gourmet / Familiar |
| Idioma de la carta | Select | Español / Inglés / Catalán / Euskera |
| Precio del plato (opcional) | Number | 9.50 |

### Prompt para Anthropic API

```javascript
const generateMenuCopyPrompt = (inputs) => `
Eres un copywriter especializado en gastronomía y cartas de restaurante en España.

Plato: "${inputs.nombre}"
Ingredientes: "${inputs.ingredientes}"
Estilo del restaurante: ${inputs.estilo}
Idioma: ${inputs.idioma}
${inputs.precio ? `Precio: ${inputs.precio}€` : ""}

Genera:

1. DESCRIPCIÓN CLÁSICA (25-35 palabras): Formal, elegante, focalizada en ingredientes y técnica.

2. DESCRIPCIÓN EMOCIONAL (25-35 palabras): Evoca sensaciones, memorias, experiencias. Usa lenguaje sensorial.

3. DESCRIPCIÓN KM0/LOCAL (25-35 palabras): Destaca origen del producto, temporada, productor local si es relevante.

4. NOMBRE ALTERNATIVO SUGERIDO: Si el nombre original es genérico, propón uno más atractivo y memorable.

Responde SOLO en JSON:
{
  "clasica": "...",
  "emocional": "...",
  "km0": "...",
  "nombreAlternativo": "...",
  "razonNombre": "..."
}
`;
```

### Output / Resultado

```
┌──────────────────────────────────────────────┐
│  DESCRIPCIONES PARA TU CARTA                 │
│  Croquetas de jamón                          │
├──────────────────────────────────────────────┤
│  📋 CLÁSICA                                  │
│  "Croquetas artesanales elaboradas con       │
│  bechamel cremosa y jamón ibérico de         │
│  bellota, con rebozado crujiente dorado      │
│  al punto."                      [Copiar]   │
├──────────────────────────────────────────────┤
│  ❤️ EMOCIONAL                                │
│  "Como las de siempre, pero mejor.           │
│  Crujientes por fuera, fundentes por         │
│  dentro, con el aroma inconfundible del      │
│  mejor jamón."                   [Copiar]   │
├──────────────────────────────────────────────┤
│  🌱 KM0 / PRODUCTO LOCAL                    │
│  "Elaboradas con jamón ibérico de            │
│  Extremadura DO y leche fresca local.        │
│  Receta tradicional, ingredientes            │
│  de proximidad."                 [Copiar]   │
├──────────────────────────────────────────────┤
│  ✨ NOMBRE ALTERNATIVO SUGERIDO:             │
│  "Croquetas de Ibérico Fundente"             │
└──────────────────────────────────────────────┘
```

### CTA post-resultado
> ✍️ *¿Quieres generar toda tu carta optimizada para Local SEO y posicionamiento en Google? **Descubre Menu Plate Local SEO en AI Chef Pro →** [app.aichef.pro/pricing]*

### Notas de desarrollo para Claude Code

```
- Botón "Copiar" individual en cada descripción con feedback visual ("¡Copiado!")
- Contador de caracteres en cada descripción
- Botón "Regenerar solo esta versión" para cada tipo
- Opción "Generar otro plato" para resetear sin perder el resultado actual
- Loading state con mensaje animado: "Creando descripciones...✍️"
```

---

## APP 06 — Digital Chef Score

### Nombre completo
**Digital Chef Score by AI Chef Pro**

### Descripción funcional
Quiz de 10 preguntas sobre gestión operativa, presencia digital, control de costes y uso de tecnología. Al finalizar genera un informe con puntuación 0-100, diagnóstico por área y plan de acción personalizado con las herramientas de AI Chef Pro más relevantes según las respuestas.

### Tipo de app
**Quiz con lógica de scoring — sin API call — lógica de recomendación estática**

### Preguntas del quiz

```javascript
const PREGUNTAS = [
  {
    id: 1,
    area: "tecnologia",
    pregunta: "¿Utilizas alguna herramienta digital para gestionar tu carta o recetas?",
    opciones: [
      { texto: "No, todo en papel o memoria", puntos: 0 },
      { texto: "Solo Excel o Word", puntos: 3 },
      { texto: "Software básico de gestión", puntos: 7 },
      { texto: "Plataformas digitales especializadas", puntos: 10 }
    ]
  },
  {
    id: 2,
    area: "costes",
    pregunta: "¿Conoces el food cost exacto de cada plato de tu carta?",
    opciones: [
      { texto: "No lo calculo", puntos: 0 },
      { texto: "Tengo una idea aproximada", puntos: 3 },
      { texto: "Lo calculo manualmente para algunos platos", puntos: 6 },
      { texto: "Tengo un sistema de control riguroso", puntos: 10 }
    ]
  },
  {
    id: 3,
    area: "digital",
    pregunta: "¿Con qué frecuencia publicas contenido en redes sociales?",
    opciones: [
      { texto: "Casi nunca o nunca", puntos: 0 },
      { texto: "Esporádicamente (1-2 veces al mes)", puntos: 3 },
      { texto: "Regularmente (1-2 veces por semana)", puntos: 7 },
      { texto: "Tengo un calendario editorial y publico diario", puntos: 10 }
    ]
  },
  {
    id: 4,
    area: "operaciones",
    pregunta: "¿Cómo gestionas los alérgenos en tu establecimiento?",
    opciones: [
      { texto: "No tengo un sistema formal", puntos: 0 },
      { texto: "Informo verbalmente al cliente", puntos: 3 },
      { texto: "Tengo información en carta pero sin sistema digital", puntos: 6 },
      { texto: "Sistema completo digitalizado y actualizado", puntos: 10 }
    ]
  },
  {
    id: 5,
    area: "creatividad",
    pregunta: "¿Con qué frecuencia renuevas o actualizas tu carta?",
    opciones: [
      { texto: "Raramente o nunca", puntos: 0 },
      { texto: "Una vez al año", puntos: 4 },
      { texto: "Por temporadas (4 veces al año)", puntos: 7 },
      { texto: "Mensualmente con elementos de temporada", puntos: 10 }
    ]
  },
  {
    id: 6,
    area: "costes",
    pregunta: "¿Llevas un control riguroso de mermas y desperdicios?",
    opciones: [
      { texto: "No mido las mermas", puntos: 0 },
      { texto: "Tengo una idea general", puntos: 3 },
      { texto: "Registro algunas mermas clave", puntos: 6 },
      { texto: "Sistema completo de control de mermas", puntos: 10 }
    ]
  },
  {
    id: 7,
    area: "digital",
    pregunta: "¿Tu restaurante aparece en los primeros resultados de Google Maps cuando alguien busca en tu zona?",
    opciones: [
      { texto: "No lo sé / no creo", puntos: 0 },
      { texto: "A veces aparezco", puntos: 4 },
      { texto: "Sí, aparezco regularmente", puntos: 7 },
      { texto: "Sí, y trabajo activamente el SEO local", puntos: 10 }
    ]
  },
  {
    id: 8,
    area: "equipo",
    pregunta: "¿Cómo gestionas la formación y bienestar de tu equipo de cocina?",
    opciones: [
      { texto: "No tengo un sistema formal", puntos: 0 },
      { texto: "Formación básica de entrada", puntos: 3 },
      { texto: "Formación periódica en técnicas", puntos: 7 },
      { texto: "Programa completo incluyendo bienestar y motivación", puntos: 10 }
    ]
  },
  {
    id: 9,
    area: "tecnologia",
    pregunta: "¿Utilizas inteligencia artificial en algún proceso de tu negocio?",
    opciones: [
      { texto: "No, nunca lo he probado", puntos: 0 },
      { texto: "He probado ChatGPT ocasionalmente", puntos: 4 },
      { texto: "Uso IA regularmente para algunas tareas", puntos: 7 },
      { texto: "La IA está integrada en mis procesos clave", puntos: 10 }
    ]
  },
  {
    id: 10,
    area: "rentabilidad",
    pregunta: "¿Conoces el margen neto de beneficio de tu restaurante?",
    opciones: [
      { texto: "No lo calculo", puntos: 0 },
      { texto: "Tengo una idea aproximada", puntos: 3 },
      { texto: "Lo reviso mensualmente", puntos: 7 },
      { texto: "Tengo KPIs detallados y los reviso semanalmente", puntos: 10 }
    ]
  }
];
```

### Lógica de scoring y recomendación

```javascript
const calcularScore = (respuestas) => {
  const total = respuestas.reduce((sum, r) => sum + r.puntos, 0);
  const scoreTotal = total; // máximo 100

  const scoresPorArea = {
    tecnologia: calcularScoreArea(respuestas, "tecnologia"),
    costes: calcularScoreArea(respuestas, "costes"),
    digital: calcularScoreArea(respuestas, "digital"),
    operaciones: calcularScoreArea(respuestas, "operaciones"),
    equipo: calcularScoreArea(respuestas, "equipo"),
  };

  const nivel = scoreTotal >= 75 ? "avanzado" 
              : scoreTotal >= 45 ? "intermedio" 
              : "principiante";

  const planRecomendado = scoreTotal >= 75 ? "95€/mes" 
                        : scoreTotal >= 45 ? "50€/mes" 
                        : "25€/mes";

  return { scoreTotal, scoresPorArea, nivel, planRecomendado };
};
```

### Output / Resultado

```
┌──────────────────────────────────────────────┐
│  TU DIGITAL CHEF SCORE                       │
│                                              │
│           ⬤ 58/100                          │
│        NIVEL: INTERMEDIO                     │
├──────────────────────────────────────────────┤
│  DIAGNÓSTICO POR ÁREA:                       │
│  💻 Tecnología    ████░░ 60%                 │
│  💰 Control costes ███░░░ 40%               │
│  📱 Presencia digital ██░░░░ 30%            │
│  🔧 Operaciones   ████░░ 70%               │
│  👥 Equipo        ████░░ 60%               │
├──────────────────────────────────────────────┤
│  📋 PLAN DE ACCIÓN PERSONALIZADO:            │
│  1. Prioridad inmediata: Control de food     │
│     cost → Mermas GenCal + FoodCost Calc    │
│  2. Área de mejora: Presencia digital        │
│     → InstaFlow AI + Menu Plate SEO         │
│  3. Plan recomendado para ti: 50€/mes       │
├──────────────────────────────────────────────┤
│  [VER MI PLAN RECOMENDADO EN AI CHEF PRO →] │
└──────────────────────────────────────────────┘
```

### CTA post-resultado
CTA dinámico según nivel:
- **Principiante:** *"Tu restaurante tiene un enorme potencial de mejora. AI Chef Pro puede transformar tu negocio en 30 días →"*
- **Intermedio:** *"Estás en el camino correcto. Da el salto definitivo con AI Chef Pro y supera a tu competencia →"*
- **Avanzado:** *"Eres un profesional de alto nivel. AI Chef Pro te da las herramientas para llegar más lejos →"*

### Notas de desarrollo para Claude Code

```
- Progress bar durante el quiz (Pregunta X de 10)
- Animación de transición entre preguntas
- Gráfico radar (spider chart) mostrando las 5 áreas
- El resultado enlaza directamente al plan recomendado en app.aichef.pro/pricing
- Formulario de captura de email para "recibir el informe completo por correo"
- Barra animada circular para el score final (efecto contador)
```

---

## APP 07 — Brigade Calculator

### Nombre completo
**Brigade Calculator by AI Chef Pro**

### Descripción funcional
Calculadora de estructura óptima de brigada de cocina. El usuario introduce capacidad del restaurante, tipo de servicio y número de servicios semanales. La app calcula el número óptimo de personas por partida, coste de personal estimado y ratio coste/ventas.

### Tipo de app
**Calculadora con tablas de referencia — sin API call**

### Inputs del usuario

| Campo | Tipo | Opciones/Ejemplo |
|-------|------|-----------------|
| Cubiertos por servicio | Number | 65 |
| Tipo de cocina | Select | À la carte / Menú del día / Buffet / Banquetes / Mixto |
| Número de servicios/semana | Number | 14 |
| Ticket medio (€) | Number | 35 |
| Salario medio mensual cocinero (€) | Number | 1.800 |
| Horas de servicio por turno | Number | 5 |

### Lógica de cálculo

```javascript
// Ratios estándar del sector hostelero español
const RATIOS_BRIGADA = {
  alaCarteLujo:     { cubiertosXCocinero: 8,  partidas: ["frio", "caliente", "postres", "entremetier"] },
  alaCarte:         { cubiertosXCocinero: 12, partidas: ["frio", "caliente", "postres"] },
  menuDelDia:       { cubiertosXCocinero: 20, partidas: ["caliente", "frio"] },
  buffet:           { cubiertosXCocinero: 30, partidas: ["produccion", "repaso"] },
  banquetes:        { cubiertosXCocinero: 40, partidas: ["produccion", "emplatado"] },
};

const calcularBrigada = (inputs) => {
  const ratio = RATIOS_BRIGADA[inputs.tipoCocina];
  const cocinerosNecesarios = Math.ceil(inputs.cubiertos / ratio.cubiertosXCocinero);
  
  // Añadir jefe de cocina si brigada > 4 personas
  const jefesCocina = cocinerosNecesarios > 4 ? 1 : 0;
  const totalBrigada = cocinerosNecesarios + jefesCocina;
  
  const costeMensualBrigada = totalBrigada * inputs.salarioMedio * 1.35; // +35% SS
  
  const ventasMensuales = inputs.cubiertos * inputs.ticket * inputs.servicios * 4.33;
  const ratioPersonalVentas = ((costeMensualBrigada / ventasMensuales) * 100).toFixed(1);
  
  return {
    cocinerosNecesarios,
    jefesCocina,
    totalBrigada,
    costeMensualBrigada,
    ratioPersonalVentas,
    zona: ratioPersonalVentas < 35 ? "optimo" : ratioPersonalVentas < 42 ? "aceptable" : "alto"
  };
};
```

### Output / Resultado

```
┌──────────────────────────────────────────────┐
│  ESTRUCTURA DE BRIGADA ÓPTIMA                │
├──────────────────────────────────────────────┤
│  👨‍🍳 COMPOSICIÓN RECOMENDADA:               │
│  • 1 Jefe de Cocina                          │
│  • 2 Cocineros partida caliente              │
│  • 1 Cocinero partida fría                   │
│  • 1 Ayudante / Plongeur                     │
│  TOTAL: 5 personas                           │
├──────────────────────────────────────────────┤
│  💰 IMPACTO ECONÓMICO:                       │
│  Coste mensual brigada: €12.150 (con SS)     │
│  Ratio personal/ventas: 37% ⚠️               │
│  Óptimo sector: <35%                         │
├──────────────────────────────────────────────┤
│  💡 RECOMENDACIÓN:                           │
│  "Estás ligeramente por encima del ratio     │
│  óptimo. Considera optimizar turnos o        │
│  incrementar el ticket medio."               │
└──────────────────────────────────────────────┘
```

### CTA post-resultado
> 👥 *¿Quieres optimizar la gestión de tu equipo con herramientas de IA específicas para cocinas profesionales? **Prueba Mental Coach y las apps de gestión de AI Chef Pro →** [app.aichef.pro/pricing]*

### Notas de desarrollo para Claude Code

```
- Organigrama visual de la brigada generado dinámicamente
- Tooltip explicando cada puesto y sus funciones
- Comparativa: "Tu situación actual vs. brigada óptima" si usuario 
  introduce sus datos actuales
- Benchmark del sector: "El restaurante medio en España tiene un ratio 
  de personal del 38%"
```

---

## APP 08 — Tasting Menu Generator

### Nombre completo
**Tasting Menu Generator by AI Chef Pro**

### Descripción funcional
El usuario selecciona ingredientes estrella de temporada, número de pases y estilo de cocina. La app genera en segundos una propuesta de menú degustación completo con nombre de cada pase, descripción y técnica culinaria sugerida.

### Tipo de app
**IA generativa — requiere llamada a Anthropic API**

### Inputs del usuario

| Campo | Tipo | Ejemplo |
|-------|------|---------|
| Ingredientes estrella (3-5) | Tags input | Trufa negra, remolacha, lubina, naranja sanguina |
| Número de pases | Select | 5 / 7 / 10 / 12 pases |
| Estilo culinario | Select | Vanguardista / Tradicional / Fusión / Plant-based / Mediterráneo |
| Temporada | Select | Primavera / Verano / Otoño / Invierno |
| Nombre del restaurante (opcional) | Text | "El Jardín de Neptuno" |

### Prompt para Anthropic API

```javascript
const generateTastingMenuPrompt = (inputs) => `
Eres un chef ejecutivo con experiencia en alta cocina y menús degustación.

Diseña un menú degustación de ${inputs.pases} pases con las siguientes características:
- Ingredientes estrella: ${inputs.ingredientes.join(", ")}
- Estilo: ${inputs.estilo}
- Temporada: ${inputs.temporada}
${inputs.restaurante ? `- Para el restaurante: ${inputs.restaurante}` : ""}

Para cada pase genera:
- Número y nombre del pase (evocador y poético)
- Descripción del plato (30-40 palabras, sensorial y técnica)
- Técnica culinaria principal utilizada
- Maridaje sugerido (vino o bebida)

La progresión debe seguir la lógica clásica: snacks → fríos → calientes → pescado → carne → pre-postre → postre (adapta según número de pases).

Responde SOLO en JSON:
{
  "nombreMenu": "...",
  "descripcionConcepto": "...",
  "pases": [
    {
      "numero": 1,
      "nombre": "...",
      "descripcion": "...",
      "tecnica": "...",
      "maridaje": "..."
    }
  ]
}
`;
```

### Output / Resultado
Menú degustación formateado visualmente como una carta elegante, con tipografía serif, cada pase en una card individual.

### CTA post-resultado
> 🍽️ *¿Quieres generar recetas completas con historia, ingredientes precisos e instrucciones paso a paso para cada uno de estos pases? **Descubre Cocina Creativa AI y toda la suite de AI Chef Pro →** [app.aichef.pro/pricing]*

### Notas de desarrollo para Claude Code

```
- Tags input para ingredientes (máximo 5, con autocompletado de ingredientes de temporada)
- Loading con mensaje: "Tu menú degustación está tomando forma...🍽️"
- Resultado formateado como carta de restaurante elegante (fondo oscuro, tipografía serif)
- Botón "Generar otro concepto" (regenerar sin cambiar inputs)
- Opción de imprimir / descargar como PDF
- Animación de aparición de cada pase en cascada
```

---

## INTEGRACIÓN EN LA LANDING PAGE

### Estructura recomendada en la Landing 2026

```
HEADER
  └─ Hero Section (propuesta de valor principal)
  
SECTION 1 — Herramientas de la suite (overview)

SECTION 2 — LEAD MAGNET APPS (sección destacada)
  └─ Título: "Prueba el poder de AI Chef Pro. Gratis, ahora mismo."
  └─ Subtítulo: "8 herramientas profesionales sin registro. Sin tarjeta de crédito."
  └─ Grid 2x4 con cards de cada app (icono + nombre + CTA rápido)
  └─ Al hacer clic → Modal o sección expandida con la app
  
SECTION 3 — Planes y precios

FOOTER
  └─ Links rápidos a las 8 apps
```

### Implementación de las apps en la landing

**Opción A — Modal (recomendada para mobile)**
```jsx
// Al hacer clic en la card de la app, se abre un modal fullscreen
const AppModal = ({ app, isOpen, onClose }) => (
  <div className="fixed inset-0 bg-black/80 z-50 flex items-center justify-center p-4">
    <div className="bg-white rounded-2xl max-w-2xl w-full max-h-[90vh] overflow-y-auto p-6">
      <button onClick={onClose} className="float-right text-2xl">×</button>
      <app.Component />
    </div>
  </div>
);
```

**Opción B — Sección expandible (recomendada para desktop)**
```jsx
// Accordion: al hacer clic en la card, se expande la app inline
```

### Cards de presentación de las 8 apps

```jsx
const LEAD_MAGNET_APPS = [
  { id: 1, icono: "🧮", nombre: "FoodCost Calculator", tagline: "Calcula el coste de cualquier plato en segundos", color: "#27ae60" },
  { id: 2, icono: "🔍", nombre: "Alérgenos Checker", tagline: "Detecta los 14 alérgenos obligatorios al instante", color: "#e74c3c" },
  { id: 3, icono: "📅", nombre: "Gastro Content Calendar", tagline: "30 días de contenido para tus redes en 1 clic", color: "#9b59b6" },
  { id: 4, icono: "💰", nombre: "Menu Profit Simulator", tagline: "Conoce la rentabilidad real de tu restaurante", color: "#f39c12" },
  { id: 5, icono: "✍️", nombre: "MenuCopy AI", tagline: "Descripciones irresistibles para tu carta", color: "#3498db" },
  { id: 6, icono: "📊", nombre: "Digital Chef Score", tagline: "¿Cuán digitalizado está tu restaurante?", color: "#1abc9c" },
  { id: 7, icono: "👨‍🍳", nombre: "Brigade Calculator", tagline: "La brigada óptima para tu volumen de trabajo", color: "#e67e22" },
  { id: 8, icono: "🍽️", nombre: "Tasting Menu Generator", tagline: "Un menú degustación completo generado por IA", color: "#8e44ad" },
];
```

---

## ESTRATEGIA DE CTA Y CONVERSIÓN

### Flujo de conversión por cada app

```
Usuario ve la Landing →
  Prueba una app gratuita →
    Obtiene resultado de valor →
      Ve CTA específico relacionado con su dolor →
        Hace clic en "Ver mi plan en AI Chef Pro" →
          Llega a app.aichef.pro/pricing →
            Se suscribe al plan recomendado
```

### Prioridad de despliegue (orden recomendado)

```
FASE 1 (lanzamiento inmediato):
  1. FoodCost Calculator ← mayor impacto, sin API
  2. Menu Profit Simulator ← decisores económicos
  3. Digital Chef Score ← precalifica y recomienda plan

FASE 2 (2 semanas después):
  4. Alérgenos Checker ← urgencia legal
  5. MenuCopy AI ← demostración de IA generativa
  6. Brigade Calculator ← dueños y gerentes

FASE 3 (1 mes después):
  7. Gastro Content Calendar ← visibilidad digital
  8. Tasting Menu Generator ← wow factor creativo
```

### Links de destino en CTAs

```
Todos los CTAs principales → https://app.aichef.pro/pricing
Link de contacto → https://aichef.pro/contacto
Página de inicio → https://aichef.pro/
Blog → https://blog.aichef.pro/
Roadmap → https://blog.aichef.pro/roadmap/
```

---

## TABLA RESUMEN

| # | App | Tipo | API Necesaria | Público Primario | Conversión Estimada |
|---|-----|------|--------------|-----------------|-------------------|
| 1 | FoodCost Calculator | Calculadora | ❌ No | Dueños / Gerentes | ⭐⭐⭐⭐⭐ |
| 2 | Alérgenos Checker | Detección BD | ❌ No | Chefs / Gerentes | ⭐⭐⭐⭐⭐ |
| 3 | Gastro Content Calendar | IA Generativa | ✅ Sí | Community Mgr / Dueños | ⭐⭐⭐⭐ |
| 4 | Menu Profit Simulator | Calculadora | ❌ No | Dueños / Inversores | ⭐⭐⭐⭐⭐ |
| 5 | MenuCopy AI | IA Generativa | ✅ Sí | Chefs / Dueños | ⭐⭐⭐⭐ |
| 6 | Digital Chef Score | Quiz/Scoring | ❌ No | Todos | ⭐⭐⭐⭐⭐ |
| 7 | Brigade Calculator | Calculadora | ❌ No | Dueños / Jefes Cocina | ⭐⭐⭐⭐ |
| 8 | Tasting Menu Generator | IA Generativa | ✅ Sí | Chefs Creativos | ⭐⭐⭐⭐ |

---

*Documento generado para el proyecto AI Chef Pro — Landing Page v2026*  
*© 2026 AI Chef Pro — aichef.pro*
