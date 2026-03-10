export interface Prompt {
  id: number;
  title: string;
  compatible: string[];
  text: string;
}

export interface Category {
  id: string;
  title: string;
  promptCount: number;
  prompts: Prompt[];
}

export const categories: Category[] = [
  {
    id: "cocina",
    title: "Cocina y Recetas Creativas",
    promptCount: 10,
    prompts: [
      {
        id: 1,
        title: "Receta de autor desde ingrediente principal",
        compatible: ["AI Chef Pro", "ChatGPT", "Claude"],
        text: "Actúa como chef ejecutivo con experiencia en cocina de autor contemporánea. Crea una receta de alta cocina usando [INGREDIENTE PRINCIPAL] como protagonista absoluto. El plato debe tener:\n- Nombre creativo y evocador\n- Historia del plato (2-3 frases)\n- Ingredientes para 4 pax con cantidades exactas\n- Elaboración paso a paso (técnicas profesionales)\n- Emplatado y presentación\n- Maridaje recomendado\n- Nivel de dificultad: [BÁSICO/INTERMEDIO/AVANZADO]\nEstilo gastronómico: [MEDITERRÁNEO/NÓRDICO/ASIÁTICO/FUSIÓN]"
      },
      {
        id: 2,
        title: "Menú degustación de 7 pasos",
        compatible: ["AI Chef Pro", "ChatGPT", "Claude"],
        text: "Diseña un menú degustación de 7 pasos para un restaurante de [TIPO DE COCINA]. El menú debe:\n- Seguir una narrativa gastronómica coherente de inicio a fin\n- Incluir: snack bienvenida, 2 entrantes, pescado, carne, pre-postre y postre\n- Respetar la progresión de sabores (de ligero a intenso)\n- Cada plato con nombre, descripción y técnica principal\n- Restricciones a evitar: [ALÉRGENOS/PREFERENCIAS]\n- Precio objetivo por persona: [RANGO €]\n- Temporada: [PRIMAVERA/VERANO/OTOÑO/INVIERNO]"
      },
      {
        id: 3,
        title: "Reinterpretar un clásico con técnicas modernas",
        compatible: ["AI Chef Pro", "ChatGPT", "Perplexity"],
        text: "Toma el plato clásico [NOMBRE DEL PLATO] de la cocina [PAÍS/REGIÓN] y reinterpretalo con técnicas de cocina contemporánea. Mantén la esencia y los sabores reconocibles del original pero transforma:\n- La textura de al menos 2 componentes\n- La presentación al plato\n- Incorpora al menos una técnica moderna (gelificación, esferificación, deshidratación, emulsión, etc.)\nExplica qué conservas del original y qué transformas. Incluye receta completa."
      },
      {
        id: 4,
        title: "Receta de temporada con productos locales",
        compatible: ["AI Chef Pro", "ChatGPT", "Claude"],
        text: "Soy chef de un restaurante en [CIUDAD/REGIÓN] y quiero crear un plato que destaque los productos de temporada de [MES/ESTACIÓN]. Dame una receta que:\n- Use mínimo 3 productos de temporada y proximidad de esa región\n- Sea ejecutable en un servicio de restaurante (no exceda 15 min de mise en place por pase)\n- Tenga un food cost por debajo del [X]% del precio de venta\n- Precio de venta objetivo: [€]\n- Número de comensales estimados por servicio: [N]"
      },
      {
        id: 5,
        title: "Receta plant-based de alta cocina",
        compatible: ["AI Chef Pro", "Claude", "ChatGPT"],
        text: "Diseña una receta plant-based (100% vegetal) de nivel gastronómico que pueda competir en carta con platos de proteína animal. El plato debe:\n- Tener complejidad de sabores comparable a un plato de carne o pescado\n- Usar técnicas que aporten umami (fermentación, Maillard, reducción, etc.)\n- Ser visualmente impactante en el emplatado\n- Ingrediente vegetal protagonista: [INGREDIENTE]\n- Sin: [RESTRICCIONES ADICIONALES]\nIncluye receta completa, técnicas y sugerencia de maridaje."
      },
      {
        id: 6,
        title: "Receta de aprovechamiento zero waste",
        compatible: ["AI Chef Pro", "ChatGPT", "DeepSeek"],
        text: "Tengo estos subproductos y mermas en mi cocina que normalmente se descartan: [LISTA DE SUBPRODUCTOS]. Crea una o varias recetas que los aprovechen íntegramente en platos de carta o tapas. Para cada receta indica:\n- Nombre del plato\n- Subproducto aprovechado y cómo se transforma\n- Técnica aplicada\n- Valor añadido al menú (narrativa de sostenibilidad)\n- Precio de venta sugerido"
      },
      {
        id: 7,
        title: "Receta de fermentación creativa",
        compatible: ["AI Chef Pro", "Claude", "Perplexity"],
        text: "Actúa como experto en fermentación gastronómica. Quiero fermentar [INGREDIENTE] para usarlo en [TIPO DE PLATO/CONTEXTO]. Dame:\n- Técnica de fermentación más adecuada (koji, lactofermentación, garum, kombucha, miso, shoyu...)\n- Proceso detallado paso a paso con tiempos y temperaturas\n- Resultado esperado en sabor, textura y aroma\n- Aplicaciones gastronómicas del fermento resultante (3 ideas de uso)\n- Errores comunes a evitar\n- Tiempo total hasta estar listo para usar"
      },
      {
        id: 8,
        title: "Descripción literaria del plato para la carta",
        compatible: ["AI Chef Pro", "ChatGPT", "Claude"],
        text: "Escribe la descripción del plato [NOMBRE DEL PLATO] para la carta de un restaurante [TIPO]. Los ingredientes principales son: [LISTA]. La descripción debe:\n- Tener entre 18 y 28 palabras (concisa pero evocadora)\n- Apelar a los sentidos sin ser cursi\n- Mencionar la técnica principal si añade valor\n- Tono: [ELEGANTE/CASUAL/MODERNO/TRADICIONAL]\nDame 3 versiones alternativas para elegir."
      },
      {
        id: 9,
        title: "Escalado de receta para servicio masivo",
        compatible: ["AI Chef Pro", "ChatGPT", "Gemini"],
        text: "Tengo esta receta pensada para [N PORCIONES ORIGINAL]: [PEGAR RECETA]. Necesito escalarla para [N PORCIONES DESTINO]. Por favor:\n- Escala todas las cantidades con precisión\n- Advierte sobre ingredientes que NO escalan linealmente (levaduras, sal, especias, gelatinas)\n- Ajusta tiempos de cocción si aplica\n- Indica si algún proceso cambia al producir en ese volumen\n- Sugiere adaptaciones para producción en cocina central si el volumen es superior a 50 porciones"
      },
      {
        id: 10,
        title: "Receta fusión entre dos cocinas",
        compatible: ["AI Chef Pro", "Claude", "ChatGPT"],
        text: "Crea una receta de fusión entre la cocina [COCINA 1] y la cocina [COCINA 2] que sea coherente y no forzada. El plato debe respetar la esencia de ambas tradiciones culinarias. Indica:\n- Qué elementos tomas de cada cocina (técnicas, ingredientes, filosofía)\n- Por qué esta combinación tiene sentido gastronómico\n- Receta completa con ingredientes y elaboración\n- Nombre del plato que refleje la fusión\n- Posibles puntos de conflicto cultural a tener en cuenta"
      }
    ]
  },
  {
    id: "gestion",
    title: "Gestión, Costes y Mermas",
    promptCount: 8,
    prompts: [
      {
        id: 11,
        title: "Cálculo de food cost de una receta",
        compatible: ["AI Chef Pro", "ChatGPT", "Gemini"],
        text: "Calcula el food cost de esta receta para [N] porciones. Te proporciono los ingredientes y costes:\n[LISTA: ingrediente - cantidad - precio por kg/unidad]\nPor favor calcula:\n- Coste total de materia prima\n- Coste por porción\n- Food cost % si el precio de venta es [€]\n- Food cost % recomendado para este tipo de establecimiento: [TIPO]\n- Si el food cost es elevado, sugiere 2-3 optimizaciones sin sacrificar calidad"
      },
      {
        id: 12,
        title: "Análisis de mermas por ingrediente",
        compatible: ["AI Chef Pro", "ChatGPT", "Claude"],
        text: "Actúa como experto en gestión de costes gastronómicos. Para los siguientes ingredientes, dame el porcentaje de merma estándar por tipo de procesado y el peso neto aprovechable:\n[LISTA DE INGREDIENTES]\nPara cada uno indica:\n- % merma en limpieza en crudo\n- % merma tras cocción (si aplica)\n- Rendimiento neto final por kg bruto\n- Precio real por kg neto (si el bruto cuesta [€/kg])\n- Consejos para reducir la merma en cocina"
      },
      {
        id: 13,
        title: "Ingeniería de menú: rentabilidad por plato",
        compatible: ["AI Chef Pro", "Claude", "ChatGPT"],
        text: "Analiza la rentabilidad de estos platos de mi carta usando la matriz de ingeniería de menú (Boston Matrix):\n[TABLA: plato - precio venta - food cost - unidades vendidas/semana]\nClasifica cada plato en: Estrella (alta rentabilidad, alta demanda), Vaca Lechera (alta rentabilidad, baja demanda), Interrogante (baja rentabilidad, alta demanda), Perro (baja rentabilidad, baja demanda).\nRecomienda qué hacer con cada uno: mantener, rediseñar, eliminar o relanzar."
      },
      {
        id: 14,
        title: "Escandallo profesional completo",
        compatible: ["AI Chef Pro", "ChatGPT", "Gemini"],
        text: "Elabora el escandallo completo del plato [NOMBRE DEL PLATO]. Ingredientes y cantidades: [LISTA]. Precio de venta objetivo: [€]. Incluye:\n- Tabla de escandallo con coste por ingrediente\n- Coste total materia prima\n- Coste de mano de obra estimado (tiempo elaboración: [MINUTOS] × coste/hora: [€])\n- Costes indirectos estimados (energía, consumibles): [%]\n- Margen bruto y neto\n- Precio de venta mínimo para alcanzar el margen objetivo: [%]\n- Recomendación de precio de carta"
      },
      {
        id: 15,
        title: "Optimización de compras semanales",
        compatible: ["AI Chef Pro", "ChatGPT", "Claude"],
        text: "Ayúdame a optimizar el pedido semanal de mi restaurante. Datos:\n- Menú de la semana: [DESCRIPCIÓN O LISTA DE PLATOS]\n- Número de servicios estimados por día: [N]\n- Días de la semana activos: [DÍAS]\n- Ingredientes que ya tengo en stock: [LISTA]\nGenera una lista de compras optimizada con cantidades exactas, considera mermas estándar, y agrupa por proveedor si es posible (carnicería, pescadería, frutería, almacén)."
      },
      {
        id: 16,
        title: "Rediseño de plato para mejorar rentabilidad",
        compatible: ["AI Chef Pro", "Claude", "ChatGPT"],
        text: "Este plato tiene un food cost demasiado alto: [DESCRIPCIÓN DEL PLATO] con food cost actual del [%]. Mi objetivo es bajarlo al [%] sin que el cliente perciba pérdida de valor. Propón:\n- Sustitución o reducción de ingredientes de alto coste\n- Técnicas que aporten percepción de valor sin incrementar coste\n- Rediseño del emplatado que justifique el precio\n- Nueva propuesta de precio de carta si hay mejora de valor percibido"
      },
      {
        id: 17,
        title: "Control de inventario y rotación",
        compatible: ["AI Chef Pro", "ChatGPT", "Gemini"],
        text: "Tengo los siguientes ingredientes en mi cámara con estas fechas de caducidad/consumo preferente: [LISTA CON FECHAS]. Necesito:\n- Orden de prioridad de uso por urgencia\n- Sugerencias de platos del día o especiales que los aprovechen\n- Técnicas de conservación para extender vida útil de los más críticos\n- Alerta de lo que se perderá si no actúo en 24/48h\n- Propuesta de mise en place que minimice pérdidas esta semana"
      },
      {
        id: 18,
        title: "Precio de carta basado en mercado",
        compatible: ["AI Chef Pro", "ChatGPT", "Claude"],
        text: "Ayúdame a fijar el precio de carta para [NOMBRE DEL PLATO]. El coste de materia prima es [€] por porción. Mi restaurante es de tipo [TIPO] en [CIUDAD], ticket medio actual [€]. Considera:\n- Benchmark con precios de mercado de ese tipo de establecimiento\n- Elasticidad de precio para ese perfil de comensal\n- Estrategia de pricing: líder en precio, precio premium, precio justo\n- El precio que maximiza margen sin sacrificar volumen de ventas\n- Si conviene presentarlo como precio redondo o con céntimos (psicología del precio)"
      }
    ]
  },
  {
    id: "catering",
    title: "Catering y Eventos",
    promptCount: 8,
    prompts: [
      {
        id: 19,
        title: "Propuesta de menú para boda",
        compatible: ["AI Chef Pro", "ChatGPT", "Claude"],
        text: "Diseña una propuesta de menú para una boda de [N] invitados:\n- Perfil de los novios/invitados: [DESCRIPCIÓN]\n- Presupuesto por persona: [€]\n- Restricciones dietéticas confirmadas: [LISTA]\n- Época del año: [MES]\n- Espacio: [INTERIOR/EXTERIOR/FINCA/HOTEL]\n- Formato: [SERVICIO A LA MESA/BUFFET/ESTACIONES/COCTELERÍA]\nIncluye: cóctel de bienvenida, menú completo con opciones, carta de bebidas sugerida y estimación de personal necesario."
      },
      {
        id: 20,
        title: "Presupuesto de catering corporativo",
        compatible: ["AI Chef Pro", "ChatGPT", "Claude"],
        text: "Elabora un presupuesto detallado para un evento corporativo:\n- Número de personas: [N]\n- Formato: [COFFEE BREAK/ALMUERZO/CENA DE GALA/COCKTAIL]\n- Duración: [HORAS]\n- Ubicación: [LOCAL PROPIO/SEDE CLIENTE/ESPACIO EXTERNO]\n- Presupuesto máximo: [€]\nDesglosa: coste de alimentos, bebidas, personal, logística, alquiler de material y margen comercial. Incluye condiciones de pago y política de cancelación."
      },
      {
        id: 21,
        title: "Planning operativo de producción para evento",
        compatible: ["AI Chef Pro", "Claude", "ChatGPT"],
        text: "Crea el planning operativo de producción para este evento: [DESCRIPCIÓN]. Fecha: [FECHA]. Menú: [DESCRIPCIÓN]. Personal disponible: [N personas]. Organiza:\n- Timeline de producción (desde 3 días antes hasta el servicio)\n- Asignación de tareas por persona\n- Lista de mise en place por día\n- Checklist de carga/transporte si aplica\n- Plan B para las elaboraciones más críticas"
      },
      {
        id: 22,
        title: "Menú para evento con restricciones múltiples",
        compatible: ["AI Chef Pro", "ChatGPT", "Claude"],
        text: "Diseña un menú para un evento de [N] personas donde coexisten estas restricciones dietéticas: [LISTA DETALLADA: X veganos, Y celíacos, Z sin lactosa, etc.]. El reto: que no haya menús especiales segregados. Propón un menú unificado que funcione para todos sin que nadie sienta que tiene una versión inferior."
      },
      {
        id: 23,
        title: "Estaciones gastronómicas para cocktail",
        compatible: ["AI Chef Pro", "ChatGPT", "Claude"],
        text: "Diseña [N] estaciones gastronómicas temáticas para un cóctel de [N] personas durante [HORAS]. Cada estación debe tener:\n- Nombre y concepto temático\n- 4-6 elaboraciones (mix frío/caliente)\n- 1 elemento espectacular o interactivo para atraer a los invitados\n- Tiempo de montaje y necesidades de personal por estación\nTema global del evento: [TEMA]. Presupuesto total: [€]"
      },
      {
        id: 24,
        title: "Email de propuesta comercial para cliente",
        compatible: ["AI Chef Pro", "Claude", "ChatGPT"],
        text: "Redacta un email de propuesta comercial para un cliente potencial de catering. Evento: [TIPO]. El email debe:\n- Ser profesional pero cálido, no robótico\n- Resumir nuestra propuesta de valor diferencial\n- Mencionar brevemente el menú sugerido: [DESCRIPCIÓN]\n- Precio por persona: [€]\n- Llamada a la acción clara para concertar reunión o degustación\n- Longitud: máximo 200 palabras\nFirmado por: [NOMBRE/CARGO]"
      },
      {
        id: 25,
        title: "Cálculo de cantidades para buffet",
        compatible: ["AI Chef Pro", "ChatGPT", "Gemini"],
        text: "Calcula las cantidades exactas de alimentos para un buffet de [N] personas durante [HORAS]. Perfil: [CORPORATIVO/FAMILIAR/GALA/CASUAL]. Menú del buffet: [DESCRIPCIÓN]. Ten en cuenta:\n- Ratios estándar por persona por categoría\n- Factor de consumo según perfil de invitados y hora del día\n- Excedente de seguridad recomendado\n- Orden de colocación en buffet para optimizar consumo"
      },
      {
        id: 26,
        title: "Menú de temporada para catering premium",
        compatible: ["AI Chef Pro", "Claude", "ChatGPT"],
        text: "Diseña un menú de catering premium para la temporada de [TEMPORADA/MESES] que destaque productos de km 0 y máxima calidad. Nivel: gourmet/alta gama. El menú debe ser una declaración gastronómica, no solo un servicio de comida. Incluye storytelling de los ingredientes principales y sugiere cómo comunicarlo a los clientes."
      }
    ]
  },
  {
    id: "marketing",
    title: "Marketing del Negocio",
    promptCount: 8,
    prompts: [
      {
        id: 27,
        title: "Post de Instagram para plato de carta",
        compatible: ["AI Chef Pro", "ChatGPT", "Claude"],
        text: "Escribe un post de Instagram para presentar el plato [NOMBRE] del restaurante [NOMBRE]. Ingredientes principales: [LISTA]. El post debe:\n- Empezar con un gancho potente en la primera línea\n- Contar la historia o concepto detrás del plato\n- Incluir una llamada a la acción natural\n- Finalizar con 15-20 hashtags relevantes\n- Tono: [ELEGANTE/CERCANO/APASIONADO/INFORMATIVO]\n- Longitud: 150-200 palabras de texto + hashtags"
      },
      {
        id: 28,
        title: "Contenido SEO local para blog de restaurante",
        compatible: ["AI Chef Pro", "Claude", "ChatGPT"],
        text: "Escribe un artículo de blog SEO-optimizado para el restaurante [NOMBRE] en [CIUDAD]. Keyword objetivo: [PLATO/TIPO DE COCINA] en [CIUDAD]. Incluye:\n- H1 optimizado con keyword\n- Introducción con keyword natural en primeros 100 palabras\n- Descripción de la experiencia con contenido de valor real\n- Sección por qué visitarnos con diferenciadores\n- Información práctica (horarios, dirección, reservas)\n- Meta description de 155 caracteres\nLongitud: 600-800 palabras. Tono natural, no sobreoptimizado."
      },
      {
        id: 29,
        title: "Respuesta profesional a reseña negativa",
        compatible: ["AI Chef Pro", "Claude", "ChatGPT"],
        text: "Un cliente ha dejado esta reseña negativa: [PEGAR RESEÑA]. Redacta una respuesta pública que:\n- Agradezca el feedback sin ser condescendiente\n- Reconozca el problema si es legítimo\n- Explique brevemente qué se hará al respecto\n- Invite al cliente a una segunda oportunidad\n- No sea defensiva ni agresiva\nMáximo 100-120 palabras. Firmado por: [NOMBRE/CARGO]"
      },
      {
        id: 30,
        title: "Plan de contenido mensual para RRSS",
        compatible: ["AI Chef Pro", "ChatGPT", "Claude"],
        text: "Crea un plan de contenido para redes sociales del mes de [MES] para el restaurante [NOMBRE/TIPO]. Frecuencia: [N posts/semana]. Redes: [Instagram/Facebook/TikTok]. Incluye para cada publicación:\n- Día y hora de publicación\n- Formato (foto/reel/story/carrusel)\n- Tema y concepto del contenido\n- Copy resumido o idea principal\n- Hashtags sugeridos\nRatio recomendado: 70% valor, 20% comunidad, 10% venta."
      },
      {
        id: 31,
        title: "Email marketing para base de clientes",
        compatible: ["AI Chef Pro", "Claude", "ChatGPT"],
        text: "Redacta un email de marketing para nuestra base de clientes. Objetivo: [ANUNCIAR NUEVA CARTA/EVENTO/OFERTA/REAPERTURA]. El email debe:\n- Asunto irresistible (máx. 50 caracteres)\n- Preheader complementario\n- Cuerpo cálido y personal (no corporativo)\n- Un único CTA claro\n- Sin lenguaje de spam\n- Posdata con toque humano\nTono: como si lo escribiera el chef/propietario personalmente. Máximo 200 palabras."
      },
      {
        id: 32,
        title: "Script para Reel o TikTok gastronómico",
        compatible: ["AI Chef Pro", "ChatGPT", "Claude"],
        text: "Crea el script completo para un Reel/TikTok de [DURACIÓN: 30/45/60 segundos] mostrando [PLATO/TÉCNICA/RECETA/DETRÁS DE CÁMARAS]. El script incluye:\n- Gancho visual para los primeros 2 segundos\n- Estructura de escenas con descripción visual\n- Texto en pantalla (subtítulos/overlays)\n- Música recomendada (tipo/mood)\n- CTA final\nEl objetivo es [VIRALIZARSE/EDUCAR/VENDER/CONSTRUIR MARCA]."
      },
      {
        id: 33,
        title: "Storytelling del chef para bio profesional",
        compatible: ["AI Chef Pro", "Claude", "ChatGPT"],
        text: "Escribe la bio profesional de [NOMBRE] para web, prensa y RRSS. Datos: [TRAYECTORIA, FORMACIÓN, RESTAURANTES, FILOSOFÍA, LOGROS]. Dame:\n- Versión larga (300 palabras) para web y prensa\n- Versión corta (80 palabras) para RRSS\n- Versión ultra corta (1 frase de impacto) para presentaciones\n- Tono: [ELEGANTE/CERCANO/ÉPICO]\nQue transmita autenticidad, no un CV frío."
      },
      {
        id: 34,
        title: "Propuesta de colaboración con influencer",
        compatible: ["AI Chef Pro", "Claude", "ChatGPT"],
        text: "Redacta un mensaje de colaboración para un influencer gastronómico con [N] seguidores en [PLATAFORMA]. Nuestro restaurante: [NOMBRE Y DESCRIPCIÓN BREVE]. La propuesta: [DESCRIPCIÓN]. El mensaje debe:\n- Ser personalizado (mencionar algo específico de su perfil)\n- Ser directo sobre lo que proponemos\n- Explicar el beneficio mutuo\n- No sonar genérico\n- Incluir un CTA concreto\nMáximo 120 palabras."
      }
    ]
  },
  {
    id: "pasteleria",
    title: "Pastelería, Panadería y Chocolatería",
    promptCount: 7,
    prompts: [
      {
        id: 35,
        title: "Postre de restaurante contemporáneo",
        compatible: ["AI Chef Pro", "ChatGPT", "Claude"],
        text: "Diseña un postre de restaurante de alta cocina que sea visualmente impactante y técnicamente ejecutable en servicio. Debe incluir al menos 3 componentes con diferentes texturas (crujiente, cremoso, gelificado). Ingrediente o concepto protagonista: [INGREDIENTE/CONCEPTO]. Restricciones: [ALÉRGENOS A EVITAR]. Incluye: nombre del postre, historia del plato, receta completa, técnicas específicas y descripción del emplatado."
      },
      {
        id: 36,
        title: "Formulación de ganache de chocolate",
        compatible: ["AI Chef Pro", "ChatGPT", "Claude"],
        text: "Formula una ganache de chocolate con las siguientes características:\n- Tipo de chocolate: [NEGRO XX%/LECHE/BLANCO/RUBIO]\n- Aplicación: [RELLENO DE BOMBÓN/TRUFA/COBERTURA/TARTA/HELADO]\n- Textura final deseada: [FIRME/BLANDA/FLUIDA/PARA MOLDEAR]\n- Ingredientes adicionales a incorporar: [LISTA]\nDame: ratio chocolate/nata, temperatura de trabajo, proceso detallado, tiempo de cristalización y consejos de conservación."
      },
      {
        id: 37,
        title: "Pan artesanal con masa madre",
        compatible: ["AI Chef Pro", "Claude", "Perplexity"],
        text: "Crea una receta de pan artesanal con masa madre con estas especificaciones:\n- Tipo de harina: [TIPO Y FUERZA]\n- Hidratación deseada: [%]\n- Incorporaciones: [SEMILLAS/FRUTOS SECOS/ACEITUNAS/ESPECIAS/NINGUNA]\n- Formato final: [HOGAZA/BARRA/ROLLS/CHAPATA]\n- Horneado en: [HORNO DOMÉSTICO/HORNO DE PANADERÍA/COCOTTE]\nIncluye: fórmula de la masa madre, proceso completo con tiempos de fermentación, temperatura de cocción y trucos para corteza perfecta."
      },
      {
        id: 38,
        title: "Formulación de helado artesanal",
        compatible: ["AI Chef Pro", "ChatGPT", "Claude"],
        text: "Formula un helado artesanal con las siguientes características:\n- Sabor principal: [SABOR]\n- Tipo: [CREMOSO/SORBETE/SEMIFRÍO/GRANIZADO]\n- Restricciones: [SIN LACTOSA/VEGANO/SIN AZÚCAR/CONVENCIONAL]\n- Uso: [RESTAURANTE/HELADERÍA/VENTA AL PÚBLICO]\nProporciona: fórmula completa con porcentajes, índice de dulzor y congelación, proceso de elaboración, temperatura de servicio y sugerencia de maridaje o presentación."
      },
      {
        id: 39,
        title: "Tarta de celebración: diseño y receta",
        compatible: ["AI Chef Pro", "ChatGPT", "Claude"],
        text: "Diseña una tarta de celebración para [OCASIÓN] para [N] personas. Estilo visual: [ELEGANTE/MODERNO/RÚSTICO/TEMÁTICO]. Sabores deseados: [LISTA]. Restricciones: [ALÉRGENOS]. Proporciona:\n- Concepto visual detallado (capas, colores, decoración)\n- Receta completa de bizcocho, crema y cobertura\n- Estructura de capas y montaje\n- Técnicas de decoración\n- Timeline de producción (qué hacer cada día)"
      },
      {
        id: 40,
        title: "Tabla de temperaturas de templado de chocolate",
        compatible: ["AI Chef Pro", "ChatGPT", "Gemini"],
        text: "Necesito la guía completa de templado de chocolate para trabajo profesional. Para cada tipo de chocolate (negro, con leche, blanco, rubio/caramel) dame:\n- Temperatura de fusión\n- Temperatura de enfriamiento (1ª bajada)\n- Temperatura de trabajo (subida final)\n- Señales visuales para saber si está bien templado\n- Errores comunes y cómo corregirlos\n- Método alternativo de templado por siembra y por tablado\nFormato: tabla comparativa + notas de proceso."
      },
      {
        id: 41,
        title: "Colección de petit fours para restaurante",
        compatible: ["AI Chef Pro", "Claude", "ChatGPT"],
        text: "Diseña una colección de 6 petit fours para el final de la comida en un restaurante de [TIPO/ESTILO]. La colección debe:\n- Tener coherencia visual y de concepto entre las 6 piezas\n- Combinar técnicas: gelificación, chocolate, crujiente, cremoso\n- Ser ejecutable en producción diaria para [N] servicios\n- Temporada: [ESTACIÓN]\n- Sin: [ALÉRGENOS]\nPara cada pieza: nombre, descripción, receta resumida y técnica principal."
      }
    ]
  },
  {
    id: "food-pairing",
    title: "Food Pairing",
    promptCount: 8,
    prompts: [
      {
        id: 42,
        title: "Maridaje molecular entre dos ingredientes",
        compatible: ["AI Chef Pro", "Claude", "Perplexity"],
        text: "Analiza la compatibilidad molecular entre [INGREDIENTE 1] y [INGREDIENTE 2] basándote en sus compuestos aromáticos compartidos. Dime:\n- Compuestos aromáticos que comparten\n- Nivel de compatibilidad (alta/media/baja) y por qué\n- Cómo potenciar esa combinación en cocina (técnicas recomendadas)\n- 3 ideas concretas de platos o preparaciones que aprovechen ese maridaje\n- Ingrediente puente que puede unir ambos si la compatibilidad es baja"
      },
      {
        id: 43,
        title: "Sustituto perfecto para un ingrediente",
        compatible: ["AI Chef Pro", "ChatGPT", "Claude"],
        text: "Necesito un sustituto para [INGREDIENTE ORIGINAL] en esta receta: [DESCRIPCIÓN BREVE]. El motivo es: [ALERGIA/NO DISPONIBLE/PRECIO/TEMPORADA]. El sustituto debe:\n- Mantener el perfil de sabor lo más similar posible\n- Funcionar con la misma técnica de cocción\n- Estar disponible en [REGIÓN/TEMPORADA]\nDame las 3 mejores opciones ordenadas por similitud, con ajustes de cantidad y cualquier modificación necesaria en la técnica."
      },
      {
        id: 44,
        title: "Maridaje vino y plato",
        compatible: ["AI Chef Pro", "ChatGPT", "Claude"],
        text: "Recomienda el maridaje de vino ideal para este plato: [DESCRIPCIÓN DEL PLATO]. Considera:\n- Intensidad del plato y equilibrio vino/comida\n- Región vinícola preferida si aplica: [REGIÓN O \"cualquiera\"]\n- Presupuesto por botella: [€]\n- Servicio: [RESTAURANTE/CENA EN CASA/EVENTO]\nDame: 3 opciones (una segura, una interesante, una sorprendente), con varietal, DO o región, y explicación de por qué funciona ese maridaje."
      },
      {
        id: 45,
        title: "Combinaciones inesperadas con base científica",
        compatible: ["AI Chef Pro", "Claude", "Perplexity"],
        text: "Propón 5 combinaciones de ingredientes inesperadas o contraintuitivas que estén justificadas por food pairing científico. Para cada combinación:\n- Los dos (o más) ingredientes\n- Por qué funciona (compuestos compartidos o contraste equilibrado)\n- Una aplicación gastronómica concreta\n- Nivel de sorpresa para el comensal (del 1 al 5)\nIngrediente o perfil de cocina de referencia: [INGREDIENTE O ESTILO]"
      },
      {
        id: 46,
        title: "Perfil sensorial de un plato",
        compatible: ["AI Chef Pro", "ChatGPT", "Claude"],
        text: "Analiza el perfil sensorial completo de este plato: [DESCRIPCIÓN]. Evalúa:\n- Sabores predominantes y secundarios (dulce, salado, ácido, amargo, umami, picante)\n- Texturas presentes y su contraste\n- Aromas principales y cómo evolucionan\n- Temperatura y contraste térmico\n- Equilibrio general: ¿qué sobresale? ¿qué falta?\n- Recomendaciones para mejorar el balance sensorial\nFormato: análisis detallado + tabla resumen."
      },
      {
        id: 47,
        title: "Menú monoproducto",
        compatible: ["AI Chef Pro", "Claude", "ChatGPT"],
        text: "Diseña un menú degustación de 5 pasos donde el protagonista absoluto de todos los platos sea [INGREDIENTE]. El reto: que cada plato muestre una faceta completamente diferente del mismo ingrediente (crudo, cocido, fermentado, deshidratado, en salsa, etc.). Incluye: nombre de cada plato, técnica aplicada al ingrediente protagonista y cómo evoluciona la experiencia de principio a fin."
      },
      {
        id: 48,
        title: "Adaptación de receta a restricción dietética",
        compatible: ["AI Chef Pro", "ChatGPT", "Claude"],
        text: "Adapta esta receta: [PEGAR RECETA] para que sea apta para [VEGANO/CELÍACO/SIN LACTOSA/SIN FRUTOS SECOS/DIABÉTICO]. La adaptación debe:\n- Mantener el espíritu y los sabores del plato original\n- Indicar cada sustitución con su equivalencia exacta\n- Advertir si algún cambio afecta significativamente a la textura o sabor\n- Verificar que el resultado final cumple completamente con la restricción\n- Si hay pérdida de calidad, proponer compensaciones"
      },
      {
        id: 49,
        title: "Contraste de texturas en un plato",
        compatible: ["AI Chef Pro", "Claude", "ChatGPT"],
        text: "Quiero añadir contraste de texturas a este plato que actualmente es demasiado uniforme: [DESCRIPCIÓN DEL PLATO]. Propón:\n- 3 elementos crujientes que encajen con el perfil de sabor\n- 2 elementos cremosos o gelificados como contrapunto\n- 1 elemento que aporte temperatura contrastante si es apropiado\nPara cada propuesta: ingrediente, técnica de elaboración y cómo incorporarlo al emplatado sin que rompa la coherencia del plato."
      }
    ]
  },
  {
    id: "alergenos",
    title: "Alérgenos y Seguridad Alimentaria",
    promptCount: 6,
    prompts: [
      {
        id: 50,
        title: "Análisis de alérgenos en una receta",
        compatible: ["AI Chef Pro", "ChatGPT", "Claude"],
        text: "Analiza los alérgenos presentes en esta receta: [PEGAR RECETA COMPLETA CON INGREDIENTES]. Identifica:\n- Alérgenos de declaración obligatoria presentes (los 14 de la normativa europea)\n- Ingredientes que pueden contener alérgenos ocultos o trazas\n- Riesgo de contaminación cruzada según las técnicas usadas\n- Sustitutos posibles para eliminar cada alérgeno identificado\n- Cómo comunicarlo correctamente en la carta"
      },
      {
        id: 51,
        title: "Protocolo de atención a cliente con alergia",
        compatible: ["AI Chef Pro", "Claude", "ChatGPT"],
        text: "Crea un protocolo de atención para cuando un cliente informa de una alergia o intolerancia alimentaria en sala. El protocolo debe cubrir:\n- Cómo recibir la información del cliente (preguntas clave a hacer)\n- Proceso de comunicación entre sala y cocina\n- Verificación antes de servir el plato\n- Qué hacer si hay duda sobre contaminación cruzada\n- Cómo documentar el incidente\nFormato: checklist paso a paso que pueda imprimirse y colocarse en cocina y sala."
      },
      {
        id: 52,
        title: "Ficha técnica con declaración de alérgenos",
        compatible: ["AI Chef Pro", "ChatGPT", "Gemini"],
        text: "Crea la ficha técnica completa del plato [NOMBRE] con declaración de alérgenos para uso interno y/o carta. Ingredientes: [LISTA COMPLETA]. Incluye:\n- Tabla de alérgenos (los 14 de la normativa europea) con presencia confirmada/posibles trazas/ausente\n- Instrucciones de elaboración para minimizar contaminación cruzada\n- Formato apto para imprimir y colocar en cocina\n- Versión resumida para incluir en carta o app de pedidos"
      },
      {
        id: 53,
        title: "Menú completo apto para celíacos",
        compatible: ["AI Chef Pro", "Claude", "ChatGPT"],
        text: "Diseña un menú completo de [NÚMERO DE PLATOS] que sea 100% apto para celíacos (sin gluten en ingredientes y sin contaminación cruzada). El menú es para [TIPO DE ESTABLECIMIENTO]. Debe:\n- Ser gastronómicamente atractivo, no una versión reducida\n- Especificar qué harinas alternativas usar en cada preparación\n- Indicar el protocolo de cocina para evitar contaminación cruzada\n- Incluir postres sin gluten que no parezcan un compromiso"
      },
      {
        id: 54,
        title: "Etiquetado de producto artesanal para venta",
        compatible: ["AI Chef Pro", "ChatGPT", "Claude"],
        text: "Necesito el etiquetado correcto para vender este producto artesanal: [DESCRIPCIÓN DEL PRODUCTO]. Se venderá en [TIENDA PROPIA/MERCADO/ONLINE/TERCEROS]. La normativa aplicable es europea (UE 1169/2011). Proporciona:\n- Lista de ingredientes en orden descendente de peso\n- Alérgenos en negrita o resaltados\n- Información nutricional por 100g y por porción\n- Vida útil recomendada y condiciones de conservación\n- Información del productor que debe aparecer\n- Advertencias obligatorias si aplica"
      },
      {
        id: 55,
        title: "Plan de formación APPCC para equipo",
        compatible: ["AI Chef Pro", "Claude", "ChatGPT"],
        text: "Crea un plan de formación básica en APPCC (Análisis de Peligros y Puntos de Control Crítico) para el equipo de [TIPO DE ESTABLECIMIENTO] con [N] personas. El plan debe incluir:\n- Conceptos fundamentales de seguridad alimentaria (resumen ejecutivo)\n- Los puntos de control crítico más relevantes para ese tipo de negocio\n- Tabla de temperaturas de seguridad para conservación y cocción\n- Checklist diaria de control de higiene y temperatura\n- Formato de sesión formativa de 45 minutos para el equipo"
      }
    ]
  },
  {
    id: "negocio",
    title: "Gestión de Negocio",
    promptCount: 7,
    prompts: [
      {
        id: 56,
        title: "Plan de negocio para restaurante",
        compatible: ["AI Chef Pro", "Claude", "ChatGPT"],
        text: "Ayúdame a estructurar el plan de negocio para [TIPO DE RESTAURANTE/CONCEPTO] en [CIUDAD]. Datos del proyecto: [DESCRIPCIÓN BREVE]. El plan debe cubrir:\n- Análisis de mercado y competencia local\n- Propuesta de valor diferencial\n- Modelo de negocio y fuentes de ingresos\n- Estructura de costes fijos y variables\n- Proyección de ingresos a 12 meses (con escenario conservador y optimista)\n- Inversión inicial estimada y punto de equilibrio\n- Estrategia de marketing de lanzamiento"
      },
      {
        id: 57,
        title: "Descripción de concepto para franquicia",
        compatible: ["AI Chef Pro", "ChatGPT", "Claude"],
        text: "Redacta la descripción de concepto para presentar [NOMBRE DEL RESTAURANTE/CADENA] como franquicia potencial. El documento debe incluir:\n- Historia y filosofía de la marca (origen y evolución)\n- Propuesta de valor para el franquiciado\n- Descripción del modelo operativo replicable\n- Ventajas competitivas del concepto\n- Perfil ideal del franquiciado\n- Resumen de inversión y retorno estimado\nTono: documento ejecutivo profesional de 2 páginas."
      },
      {
        id: 58,
        title: "Manual de operaciones básico",
        compatible: ["AI Chef Pro", "Claude", "ChatGPT"],
        text: "Crea el índice y los primeros apartados del manual de operaciones para [TIPO DE NEGOCIO GASTRONÓMICO]. El manual debe cubrir:\n- Estándares de servicio y protocolo de atención al cliente\n- Procedimientos de apertura y cierre\n- Gestión de reservas e incidencias\n- Estándares de higiene y seguridad alimentaria\n- Protocolo de formación de nuevo personal\nFormato: documento estructurado que pueda entregarse al personal en su primer día."
      },
      {
        id: 59,
        title: "Análisis DAFO del negocio",
        compatible: ["AI Chef Pro", "ChatGPT", "Claude"],
        text: "Realiza un análisis DAFO completo para [TIPO DE NEGOCIO GASTRONÓMICO] en [CIUDAD/CONTEXTO]. Datos del negocio: [DESCRIPCIÓN]. Incluye:\n- Debilidades internas a trabajar\n- Amenazas externas a monitorizar\n- Fortalezas a potenciar en la comunicación\n- Oportunidades del mercado a aprovechar\nPara cada punto: al menos 4 ítems con descripción y nivel de impacto (alto/medio/bajo). Añade las 3 acciones más urgentes que derivan del análisis."
      },
      {
        id: 60,
        title: "Job description para puesto clave",
        compatible: ["AI Chef Pro", "Claude", "ChatGPT"],
        text: "Redacta la descripción de puesto para [NOMBRE DEL PUESTO: chef ejecutivo/jefe de sala/pastelero/bartender/gerente] en [TIPO DE ESTABLECIMIENTO]. Incluye:\n- Misión del puesto en el equipo\n- Responsabilidades principales (8-10 puntos)\n- Requisitos de experiencia y formación\n- Competencias clave (técnicas y personales)\n- Condiciones del puesto (jornada, tipo de contrato si aplica)\n- Descripción de la cultura del equipo para atraer al perfil adecuado"
      },
      {
        id: 61,
        title: "Estrategia de precios para nueva carta",
        compatible: ["AI Chef Pro", "ChatGPT", "Claude"],
        text: "Ayúdame a definir la estrategia de precios para la nueva carta de [TIPO DE RESTAURANTE]. Datos del negocio: ticket medio actual [€], coste fijo mensual [€], número de cubiertos por servicio [N], servicios por semana [N]. Propón:\n- Rango de precios por categoría (entrantes, principales, postres, bebidas)\n- Estrategia de pricing psicológico (números pares/impares, anclaje)\n- Estructura de márgenes objetivo por categoría\n- Cómo comunicar la subida de precios si es necesaria"
      },
      {
        id: 62,
        title: "Propuesta de consultoría gastronómica",
        compatible: ["AI Chef Pro", "Claude", "ChatGPT"],
        text: "Redacta una propuesta de consultoría gastronómica para el cliente [TIPO DE NEGOCIO]. El cliente tiene este problema o necesidad: [DESCRIPCIÓN]. La propuesta debe incluir:\n- Diagnóstico inicial del problema\n- Metodología de trabajo propuesta\n- Fases del proyecto con entregables por fase\n- Equipo y perfil del consultor\n- Inversión y forma de pago\n- Resultados esperados y métricas de éxito\nTono: profesional y orientado a resultados, no academicista."
      }
    ]
  },
  {
    id: "liderazgo",
    title: "Liderazgo, Equipos y Bienestar",
    promptCount: 6,
    prompts: [
      {
        id: 63,
        title: "Gestión del estrés en servicio de alta presión",
        compatible: ["AI Chef Pro", "Claude", "ChatGPT"],
        text: "Actúa como coach especializado en bienestar para profesionales de la hostelería. Tengo este problema de estrés en mi equipo/en mí mismo: [DESCRIPCIÓN DE LA SITUACIÓN]. Necesito:\n- Técnicas de gestión del estrés aplicables DURANTE el servicio (no solo después)\n- Una rutina de 5 minutos pre-servicio para centrar al equipo\n- Señales de alerta tempranas de burnout en cocina\n- Cómo comunicar al equipo que hay un problema sin generar más tensión\n- 3 cambios en la dinámica de trabajo que pueden reducir la presión crónica"
      },
      {
        id: 64,
        title: "Feedback constructivo para el equipo",
        compatible: ["AI Chef Pro", "Claude", "ChatGPT"],
        text: "Necesito dar feedback sobre un problema de rendimiento o actitud a [PERFIL: cocinero/jefe de partida/camarero/pastelero]. La situación es: [DESCRIPCIÓN OBJETIVA DEL PROBLEMA]. El empleado lleva [TIEMPO] en el equipo. Ayúdame a:\n- Estructurar la conversación (modelo SBI: Situación-Comportamiento-Impacto)\n- Las frases exactas para abrir la conversación sin generar defensividad\n- Cómo escuchar activamente su perspectiva\n- Cómo acordar un plan de mejora concreto y medible\n- Qué decir si la conversación se pone tensa"
      },
      {
        id: 65,
        title: "Rutina de mindfulness pre-servicio",
        compatible: ["AI Chef Pro", "Claude", "ChatGPT"],
        text: "Diseña una rutina de mindfulness de 8-10 minutos específica para el equipo de cocina antes de un servicio intenso. La rutina debe:\n- Ser práctica, no esotérica (adaptada a profesionales escépticos)\n- Aplicarse en el propio espacio de trabajo, sin cambiar de ropa ni de lugar\n- Incluir técnicas de respiración, enfoque mental y activación física suave\n- Terminar con un ritual de equipo que genere cohesión\n- Tener un guion que el jefe de cocina pueda leer en voz alta"
      },
      {
        id: 66,
        title: "Reunión post-servicio efectiva",
        compatible: ["AI Chef Pro", "Claude", "ChatGPT"],
        text: "Crea el esquema de una reunión post-servicio de 15 minutos para el equipo de [TIPO DE ESTABLECIMIENTO]. El servicio de hoy tuvo: [DESCRIPCIÓN: incidencias, momentos positivos, etc.]. La reunión debe:\n- Empezar por lo que salió bien (refuerzo positivo)\n- Abordar los problemas con enfoque en soluciones, no en culpas\n- Generar 1-2 acciones concretas para el próximo servicio\n- Cerrar con algo que deje al equipo con energía positiva\n- Durar máximo 15 minutos (guion con tiempos)"
      },
      {
        id: 67,
        title: "Plan de desarrollo profesional para empleado",
        compatible: ["AI Chef Pro", "Claude", "ChatGPT"],
        text: "Crea un plan de desarrollo profesional a 6 meses para [PERFIL DEL EMPLEADO: cocinero de X años de experiencia, especialidad en Y]. El empleado quiere crecer hacia: [OBJETIVO PROFESIONAL]. El plan debe incluir:\n- Evaluación de competencias actuales vs. requeridas para el objetivo\n- Formaciones específicas recomendadas (cursos, talleres, stages)\n- Responsabilidades progresivas dentro del equipo\n- Hitos de evaluación cada 2 meses\n- Cómo involucrar al empleado en el proceso para que lo sienta suyo"
      },
      {
        id: 68,
        title: "Resolución de conflicto en brigada",
        compatible: ["AI Chef Pro", "Claude", "ChatGPT"],
        text: "Tengo un conflicto entre dos miembros de mi equipo: [DESCRIPCIÓN OBJETIVA DE LA SITUACIÓN, sin nombres]. El conflicto está afectando a: [CÓMO AFECTA AL SERVICIO/AMBIENTE]. Como jefe de cocina o gerente, ayúdame a:\n- Entender las posibles causas raíz del conflicto\n- Cómo abordar la conversación por separado con cada parte\n- Cómo facilitar una conversación conjunta si es necesario\n- Qué límites y reglas de equipo establecer para evitar recurrencia\n- Cuándo es el momento de escalar el problema a RRHH"
      }
    ]
  }
];
