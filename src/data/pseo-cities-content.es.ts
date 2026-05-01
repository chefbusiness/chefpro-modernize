/**
 * Contenido de los 5 modificadores pSEO Ciudades (ES).
 *
 * Cada modificador es una plantilla con secciones únicas que se combinan con CityData
 * para generar páginas únicas por ciudad sin caer en duplicate content.
 *
 * IMPORTANTE: La página final inserta datos específicos por ciudad (cost, regulation,
 * salaries, neighborhoods) en cada sección — esto es el data moat anti-penalty 2026.
 */

import type { PSeoModifier } from './pseo-cities';

export interface PSeoModifierContent {
  modifier: PSeoModifier;
  // SEO meta (templates con {city} y {country} reemplazables)
  metaTitle: string;        // ej. "Cómo Abrir un Restaurante en {city}: Guía 2026 Costes y Licencia"
  metaDescription: string;
  keywords: string;
  // H1 + hero
  h1Template: string;       // ej. "Cómo Abrir un Restaurante en {city}"
  heroSubtitle: string;
  heroBadge: string;
  // Intro section
  introTitle: string;
  introBody: string;        // texto largo (puede contener {city} y {country})
  // Sections del cuerpo
  sections: PSeoSectionTemplate[];
  // CTA primario al producto del catálogo
  primaryProductSlug: string;       // ej. "guia-restaurante-gastronomico"
  primaryProductLabel: string;
  primaryCtaTitle: string;
  primaryCtaBody: string;
  // CTA secundario al SaaS
  saasCtaTitle: string;
  saasCtaBody: string;
  // FAQ por modificador (preguntas comunes, respuesta puede usar {city})
  faqs: { q: string; a: string }[];
  // Schema.org service name
  schemaServiceName: string;
  schemaServiceCategory: string;
}

export interface PSeoSectionTemplate {
  type: 'cost-breakdown' | 'regulation-detail' | 'salaries-table' | 'neighborhoods-grid'
       | 'workflow-steps' | 'product-cross-sell' | 'market-notes' | 'comparison-other-cities';
  title: string;            // título de la sección
  intro?: string;           // párrafo de intro
}

export const PSEO_CONTENT_ES: Record<PSeoModifier, PSeoModifierContent> = {
  'abrir-restaurante': {
    modifier: 'abrir-restaurante',
    metaTitle: 'Cómo Abrir un Restaurante en {city} en 2026: Coste, Licencias y Pasos Completos',
    metaDescription: 'Guía actualizada 2026 para abrir un restaurante en {city}: inversión real ({totalRange}), licencias específicas, salarios sector y mejores barrios. Plantillas profesionales incluidas.',
    keywords: 'abrir restaurante {city}, montar restaurante {city}, cómo abrir un restaurante en {city}, coste abrir restaurante {city}, licencia restaurante {city}',
    h1Template: 'Cómo Abrir un Restaurante en {city} (2026): Guía Completa con Costes Reales',
    heroSubtitle: 'Inversión real, licencias paso a paso, salarios del sector y los mejores barrios para tu concepto. Datos verificados y plantillas profesionales para reducir 6 meses de planificación a 1.',
    heroBadge: 'Guía 2026 Verificada',
    introTitle: 'Lo Que Realmente Cuesta Abrir un Restaurante en {city}',
    introBody: 'Abrir un restaurante en {city} es uno de los negocios más rentables — y más arriesgados — del sector hostelero {country}. El 60% de los restaurantes que cierran el primer año lo hacen por una mala planificación financiera o por desconocer la regulación local. Esta guía te da los números reales de inversión, los trámites concretos del Ayuntamiento de {city} y la información sectorial que ningún portal genérico te ofrece. Al final, encontrarás las plantillas profesionales que han usado más de 1.500 restauradores hispanohablantes para validar su proyecto antes de comprometer un euro.',
    sections: [
      {
        type: 'cost-breakdown',
        title: 'Inversión Total Real para Abrir un Restaurante en {city}',
        intro: 'Cifras de mercado verificadas {country} 2026. Rango refleja diferencias por barrio, tamaño del local y nivel de acabados.',
      },
      {
        type: 'regulation-detail',
        title: 'Licencias y Marco Regulatorio Específico de {city}',
        intro: 'Trámites obligatorios sector hostelería {country} con tiempos reales del Ayuntamiento de {city}.',
      },
      {
        type: 'salaries-table',
        title: 'Salarios del Sector Hostelero en {city}',
        intro: 'Convenios y mercado real {city} 2026. Cifras brutas mensuales — calcula seguridad social aparte (~30% adicional).',
      },
      {
        type: 'neighborhoods-grid',
        title: 'Mejores Barrios para Abrir un Restaurante en {city}',
        intro: 'Análisis de zonas con ticket medio, perfil de cliente y consideraciones de alquiler.',
      },
      {
        type: 'workflow-steps',
        title: 'Plan de Trabajo: De la Idea a la Apertura en {city}',
        intro: 'Cronograma realista de 6-12 meses para abrir un restaurante con todas las garantías.',
      },
      {
        type: 'market-notes',
        title: 'Tendencias del Mercado Gastronómico en {city}',
      },
      {
        type: 'product-cross-sell',
        title: 'Plantillas Profesionales que Acortan el Proceso',
      },
      {
        type: 'comparison-other-cities',
        title: 'Compara con Otras Ciudades',
      },
    ],
    primaryProductSlug: 'guia-restaurante-gastronomico',
    primaryProductLabel: 'Guía Completa Cómo Montar un Restaurante (€85)',
    primaryCtaTitle: 'Ahorra 6 Meses de Planificación con la Guía Profesional',
    primaryCtaBody: 'La guía completa Cómo Montar un Restaurante incluye 20+ entregables: plan de negocio editable, escandallos por categoría, plan de inversión CAPEX, P&L mensual, plantillas APPCC, marco regulatorio España + LATAM. Todo lo que necesitas para abrir tu restaurante en {city} con cifras reales y procesos validados por consultores con 15+ años de experiencia.',
    saasCtaTitle: 'O Empieza Gratis con AI Chef Pro',
    saasCtaBody: 'Suscripción mensual con todas las herramientas IA para escandallar, generar cartas, controlar APPCC, calcular brigadas y +30 apps específicas para restauración. Prueba gratis sin tarjeta.',
    faqs: [
      {
        q: '¿Cuánto cuesta realmente abrir un restaurante en {city}?',
        a: 'La inversión total en {city} oscila entre {totalRange}, dependiendo del barrio elegido, tamaño del local (50-150 m²), estado de la obra previa y nivel de acabados. Esta cifra incluye obra, equipamiento, licencias, fianza + 3-6 meses de capital circulante. NO incluye el alquiler en sí ni el sueldo del propietario el primer año.',
      },
      {
        q: '¿Cuánto tarda el trámite de licencia en {city}?',
        a: '{licenseTramitText}',
      },
      {
        q: '¿Cuál es el barrio más rentable para abrir un restaurante en {city}?',
        a: 'No existe un barrio universal: depende del concepto. Zonas premium ({premiumNeighborhood}) maximizan ticket medio pero exigen alquileres altos y conceptos diferenciados. Zonas emergentes ({emergingNeighborhood}) reducen el coste de entrada 30-40% pero requieren más esfuerzo de marketing. La regla: tu barrio ideal es donde se concentra tu cliente objetivo, no donde tú quisieras vivir.',
      },
      {
        q: '¿Qué salario mensual debo presupuestar para un jefe de cocina en {city}?',
        a: 'En {city}, el rango es {jefeCocinaSalary}. Suma ~30% adicional de cuotas patronales/seguridad social. Para conceptos premium o estrellas Michelin, los rangos pueden duplicarse. Considera también equity o bonos por objetivos para retener talento, especialmente en {city} donde la rotación del sector es alta.',
      },
      {
        q: '¿Necesito permiso especial si voy a vender alcohol o tener música en directo?',
        a: 'Sí. La licencia base de restaurante NO cubre venta principal de alcohol (bar, pub, discoteca tienen otras categorías) ni espectáculos en directo (música ambiental envasada sí, instrumentos en vivo no). En {city} requerirás trámites adicionales con Sayco/SGAE y permiso ampliado de actividad. Considera estos costes desde el principio.',
      },
    ],
    schemaServiceName: 'Consultoría para Apertura de Restaurante en {city}',
    schemaServiceCategory: 'Restaurant Opening Consultation',
  },

  'licencia-restaurante': {
    modifier: 'licencia-restaurante',
    metaTitle: 'Licencia para Abrir un Restaurante en {city} 2026: Trámites, Tiempos y Coste Real',
    metaDescription: 'Todo sobre la licencia de restaurante en {city}: tipo de licencia, organismos involucrados, documentación exigida, tiempos reales y coste total. Marco regulatorio {country} actualizado.',
    keywords: 'licencia restaurante {city}, licencia apertura restaurante {city}, permisos restaurante {city}, sanidad restaurante {city}, declaración responsable restaurante {city}',
    h1Template: 'Licencia para Abrir un Restaurante en {city}: Guía Trámites 2026',
    heroSubtitle: 'Tipo de licencia exacta, organismos a visitar, documentación obligatoria, tiempos reales y coste total. Evita los errores que retrasan 6 meses una apertura.',
    heroBadge: 'Marco Regulatorio 2026',
    introTitle: 'Tipo de Licencia que Necesitas en {city}',
    introBody: 'La pregunta más cara que te puedes hacer al abrir un restaurante en {city} es "¿qué licencia necesito?", porque elegir el régimen incorrecto puede retrasar tu apertura 4-9 meses, o peor, paralizarla con sanciones. {country} y específicamente {city} tienen normativa propia que se superpone a la europea/federal. Esta guía detalla exactamente qué tramitar, en qué orden, en qué organismo y con qué documentación.',
    sections: [
      {
        type: 'regulation-detail',
        title: 'Marco Regulatorio Aplicable en {city}',
        intro: 'Normativa europea/federal + autonómica/estatal + local que afecta a tu restaurante en {city}.',
      },
      {
        type: 'workflow-steps',
        title: 'Trámites Paso a Paso (Orden Obligatorio)',
      },
      {
        type: 'cost-breakdown',
        title: 'Coste Total de Licencias y Trámites en {city}',
      },
      {
        type: 'product-cross-sell',
        title: 'Plantillas APPCC y Documentación Sanitaria Lista para tu Apertura',
      },
    ],
    primaryProductSlug: 'pack-appcc',
    primaryProductLabel: 'Pack Completo APPCC (€14)',
    primaryCtaTitle: 'Pasa Sanidad a la Primera con el Pack APPCC',
    primaryCtaBody: 'El Pack APPCC contiene los 12 documentos que tu inspector va a pedir: planes de limpieza, control plagas, mantenimiento, recepción, almacenamiento, manipulador, trazabilidad, agua, residuos, formación, alérgenos y registros diarios. Editables en Word/Excel, listos para personalizar con tu razón social y abrir en {city} sin contratiempos.',
    saasCtaTitle: 'Automatiza el Día a Día APPCC',
    saasCtaBody: 'Con la suscripción AI Chef Pro tienes registros APPCC digitales, alertas de temperatura, generación automática de informes mensuales y trazabilidad completa. Pasa de papel a digital y reduce 80% del trabajo administrativo.',
    faqs: [
      {
        q: '¿Cuál es el tiempo real para conseguir la licencia de restaurante en {city}?',
        a: '{licenseTramitText}. Si tu local cambia de uso (de oficina a restaurante, por ejemplo), añade 2-4 meses adicionales por proyecto técnico y obras de adecuación. La prisa empuja a saltarse pasos — cada error retrasa más de lo que ahorra.',
      },
      {
        q: '¿Necesito un técnico colegiado para la documentación?',
        a: 'Sí, el proyecto técnico que entregas en {city} debe ir firmado por arquitecto, ingeniero o aparejador colegiado. Su honorario suele oscilar entre €1.500-€5.000 según complejidad del local. Es coste obligatorio, considéralo desde tu plan financiero inicial.',
      },
      {
        q: '¿Qué pasa si abro sin licencia?',
        a: 'En {city} las inspecciones municipales son frecuentes en zonas hosteleras. Las multas por funcionar sin licencia van de €600 (caso leve) hasta €60.000+ (reincidencia/sanidad), más cierre cautelar inmediato y pérdida de toda inversión hasta regularizar. Los seguros tampoco cubren incidentes en establecimientos sin licencia. No vale la pena el riesgo.',
      },
      {
        q: '¿Necesito Pack APPCC desde el día 1?',
        a: 'Sí. La inspección sanitaria previa a la apertura en {city} verifica que dispones del Plan APPCC documentado, el plan de limpieza, el de plagas y los registros formación-manipuladores. Sin estos documentos no se otorga el visto bueno sanitario, y por tanto no abre tu restaurante. El Pack APPCC contiene los 12 docs imprescindibles editables.',
      },
    ],
    schemaServiceName: 'Asesoría Licencia de Restaurante en {city}',
    schemaServiceCategory: 'Restaurant License Consulting',
  },

  'software-gestion-restaurante': {
    modifier: 'software-gestion-restaurante',
    metaTitle: 'Software de Gestión para Restaurantes en {city}: Comparativa, Precio y Mejor Opción 2026',
    metaDescription: 'Análisis del mejor software de gestión de restaurantes para {city}: TPV, escandallos, APPCC, inventario, IA. Precios, integraciones y por qué AI Chef Pro lidera en {country}.',
    keywords: 'software restaurante {city}, software gestión restaurante {city}, programa restaurante {city}, software TPV {city}, app gestión restaurante {city}',
    h1Template: 'Software de Gestión para Restaurantes en {city}: Mejor Opción 2026',
    heroSubtitle: 'Comparativa real de plataformas adaptadas a la regulación de {country}: APPCC digital, escandallos, IA generativa para cartas, control de inventario y gestión de personal. Prueba gratis sin tarjeta.',
    heroBadge: 'Comparativa Verificada 2026',
    introTitle: 'Por Qué tu Restaurante en {city} Necesita Software Especializado',
    introBody: 'El restaurante medio en {city} pierde entre 8 y 15 horas semanales en tareas administrativas que podrían automatizarse: escandallar platos cuando suben los precios, generar partes APPCC, calcular turnos, hacer pedidos al proveedor, actualizar la carta, responder reseñas. AI Chef Pro es la primera plataforma de IA específica para hostelería en {country} con +30 herramientas integradas. Esta página compara las opciones disponibles para un restaurante en {city} y por qué AI Chef Pro está liderando la adopción.',
    sections: [
      {
        type: 'workflow-steps',
        title: 'Funcionalidades Críticas para un Restaurante en {city}',
        intro: 'Características que tu software DEBE tener para cumplir regulación {country} y operar eficientemente.',
      },
      {
        type: 'cost-breakdown',
        title: 'Coste Mensual de Software Restaurante en {city}',
      },
      {
        type: 'salaries-table',
        title: 'Cuánto Ahorra el Software al Equipo de Cocina y Sala',
      },
      {
        type: 'product-cross-sell',
        title: 'Plantillas Excel Compatibles con Cualquier Software',
      },
    ],
    primaryProductSlug: 'saas-trial',
    primaryProductLabel: 'Prueba Gratis AI Chef Pro',
    primaryCtaTitle: 'Empieza Gratis con AI Chef Pro Hoy',
    primaryCtaBody: 'AI Chef Pro es el SaaS que reúne en una sola plataforma escandallos automáticos, APPCC digital, generación de cartas con IA, control de inventario, gestión de personal, calendario de contenidos y +25 apps específicas para restauración. Sin tarjeta de crédito. Sin permanencia. Adaptado a la regulación de {country}.',
    saasCtaTitle: 'Suscripción Profesional AI Chef Pro',
    saasCtaBody: 'Suscripción mensual con acceso ilimitado a todas las herramientas IA, generación de cartas, escandallos masivos, APPCC digital, integración con tu TPV. Soporte en español + atención WhatsApp.',
    faqs: [
      {
        q: '¿Qué software de gestión es mejor para un restaurante en {city}?',
        a: 'Depende del tamaño y complejidad. Para gestión integral con IA (escandallos, cartas, APPCC, RRHH, marketing) — AI Chef Pro lidera en {country} por adaptación a normativa local y equipo en español. Para solo TPV (cobro mesa) — Revel, Ágora, TPV Profesional. La tendencia 2026 es plataforma única en lugar de 5 software desconectados.',
      },
      {
        q: '¿Cuánto cuesta el software de gestión para un restaurante mediano en {city}?',
        a: 'TPV: €30-90/mes por terminal. Software de gestión integral: €40-150/mes según funcionalidades. Suscripción AI Chef Pro incluye +30 herramientas IA específicas hostelería desde €19/mes y escala según uso. Compara TCO (coste total propiedad) — soluciones aparentemente baratas requieren 4-5 plataformas integradas.',
      },
      {
        q: '¿AI Chef Pro funciona con mi TPV actual?',
        a: 'AI Chef Pro es plataforma de IA y gestión, no reemplaza TPV. Se integra como capa superior con cualquier TPV vía export CSV/Excel/PDF. Generamos escandallos, cartas, APPCC y partes que después cargas en tu TPV. Filosofía: complementamos lo que ya usas, no obligamos a cambiar.',
      },
    ],
    schemaServiceName: 'Software Gestión Restaurantes en {city}',
    schemaServiceCategory: 'Restaurant Management Software',
  },

  'escandallo-restaurante': {
    modifier: 'escandallo-restaurante',
    metaTitle: 'Escandallo de Restaurante en {city}: Cómo Calcular Costes y Precio Real 2026',
    metaDescription: 'Aprende a hacer escandallos en {city} con precios reales del mercado {country}. Plantilla profesional Excel + calculadora IA. Aumenta margen 8-15 puntos.',
    keywords: 'escandallo restaurante {city}, escandallo platos {city}, food cost {city}, calcular precio plato {city}, plantilla escandallo restaurante',
    h1Template: 'Escandallo de Restaurante en {city}: Calcula Costes Reales y Margen 2026',
    heroSubtitle: 'Plantilla profesional Excel + calculadora IA para escandallar tus platos con precios actualizados de proveedores en {country}. Aumenta margen 8-15 puntos sin tocar el ticket.',
    heroBadge: 'Plantilla Profesional 2026',
    introTitle: 'Por Qué el Escandallo es la Diferencia Entre Beneficio y Pérdida',
    introBody: 'En {city}, los precios de proveedor suben de media un 6-9% anual. Los restaurantes que NO escandallan al menos cada 6 meses pierden 5-12 puntos de margen sin darse cuenta. Esta guía te enseña a escandallar profesionalmente — con la metodología real (no la del Excel del cuñado) — y te da las plantillas que usan los consultores de hostelería con 15+ años de experiencia.',
    sections: [
      {
        type: 'workflow-steps',
        title: 'Metodología Profesional de Escandallo Aplicada en {city}',
      },
      {
        type: 'cost-breakdown',
        title: 'Estructura de Costes Tipo en un Restaurante de {city}',
      },
      {
        type: 'product-cross-sell',
        title: 'Kit Profesional de Escandallos Excel + IA',
      },
    ],
    primaryProductSlug: 'kit-escandallos',
    primaryProductLabel: 'Kit de Escandallos Pro (€12)',
    primaryCtaTitle: 'Escandalla Profesionalmente con el Kit Pro',
    primaryCtaBody: 'El Kit de Escandallos Pro contiene: plantilla Excel maestra con fórmulas profesionales, calculadora de food cost por plato, base de datos editable de ingredientes con conversiones, plantilla de menú engineering (estrellas/perros/caballos/plows) y vídeo-tutorial de uso. Aumenta el margen de tu restaurante en {city} sin subir un céntimo en carta.',
    saasCtaTitle: 'O Escandalla con IA en AI Chef Pro',
    saasCtaBody: 'La app Escandallos IA de AI Chef Pro escandalla cualquier plato a partir del nombre y los ingredientes. Genera CSV importable a tu Kit de Escandallos. Suscripción mensual con uso ilimitado.',
    faqs: [
      {
        q: '¿Con qué frecuencia debo escandallar en {city}?',
        a: 'Mínimo cada 6 meses. Ideal cada 3 meses si trabajas con producto fresco/temporada. En {city}, donde la inflación alimentaria 2024-2026 ha sido especialmente alta en proteína y aceites, escandallar trimestralmente es la diferencia entre perder o ganar dinero. La automatización con AI Chef Pro permite re-escandallar masivo en minutos.',
      },
      {
        q: '¿Cuál es el food cost objetivo para un restaurante en {city}?',
        a: '28-32% para restaurante medio (servicio mesa). 25-28% para casual rápido. 33-38% para alta gama (más merma, producto premium). Por debajo del 25% suele indicar plato infravalorado (no estás aprovechando el margen). Por encima del 38%, plato sobreprecio o pérdida segura.',
      },
      {
        q: '¿El Kit de Escandallos sirve para mi restaurante en {city}?',
        a: 'Sí — está diseñado para hispanohablantes y soporta cualquier moneda y unidades. La metodología es internacional, los precios los introduces tú según tus proveedores en {city}. Más de 1.500 restauradores en {country} y otros países hispanohablantes lo han implementado.',
      },
    ],
    schemaServiceName: 'Escandallo Profesional Restaurante {city}',
    schemaServiceCategory: 'Restaurant Cost Calculation',
  },

  'plan-negocio-restaurante': {
    modifier: 'plan-negocio-restaurante',
    metaTitle: 'Plan de Negocio para Restaurante en {city} 2026: Plantilla Excel y Cifras Reales',
    metaDescription: 'Plantilla de plan de negocio para restaurante en {city} con cifras reales del mercado {country}: P&L, inversión, break-even, ratios bancarios. Lista para banco/inversor.',
    keywords: 'plan de negocio restaurante {city}, business plan restaurante {city}, plan empresarial restaurante {city}, plantilla plan negocio hostelería',
    h1Template: 'Plan de Negocio para Restaurante en {city} (2026): Plantilla y Cifras Reales',
    heroSubtitle: 'Plantilla Excel profesional con P&L mensual, inversión CAPEX, break-even, ratios bancarios y cash flow. Cifras de mercado {country} validadas. Lista para presentar a banco o inversor.',
    heroBadge: 'Plantilla Bancaria 2026',
    introTitle: 'El Plan de Negocio que tu Banco Quiere Ver',
    introBody: 'En {city}, los bancos rechazan el 70% de las solicitudes de financiación hostelera por planes de negocio mal estructurados o con cifras sin fundamento. Esta guía te muestra cómo construir un plan de negocio bancable para tu restaurante: las cifras que el comité de riesgos espera ver, el formato de los estados financieros previsionales y los ratios mínimos de viabilidad. Plantilla Excel profesional incluida.',
    sections: [
      {
        type: 'cost-breakdown',
        title: 'Inversión Inicial Realista para Restaurante en {city}',
      },
      {
        type: 'workflow-steps',
        title: 'Estructura del Plan de Negocio Bancable',
      },
      {
        type: 'salaries-table',
        title: 'Costes de Personal en el P&L Previsional ({city})',
      },
      {
        type: 'market-notes',
        title: 'Análisis de Mercado y Competencia en {city}',
      },
      {
        type: 'product-cross-sell',
        title: 'Kit Plan Financiero Profesional',
      },
    ],
    primaryProductSlug: 'kit-plan-financiero',
    primaryProductLabel: 'Kit Plan Financiero (€39)',
    primaryCtaTitle: 'Plan de Negocio Listo en 4 Horas con el Kit Profesional',
    primaryCtaBody: 'El Kit Plan Financiero contiene: plan financiero previsional 5 años, calculadora punto equilibrio, cash flow forecast, presupuesto inversión CAPEX, P&L mensual real vs presupuesto, dashboard ratios financieros, informe viabilidad bancos, simulador escenarios y checklist pre-apertura. Las plantillas profesionales para tu restaurante en {city} listas para personalizar.',
    saasCtaTitle: 'O Apóyate en AI Chef Pro para Cifras de Mercado',
    saasCtaBody: 'Con la suscripción AI Chef Pro accedes a apps que generan automáticamente referencias de costes, ratios sectoriales y proyecciones para tu plan de negocio. Útil tanto para arrancar como para revisión anual de viabilidad.',
    faqs: [
      {
        q: '¿Qué cifras incluye un plan de negocio bancable para restaurante en {city}?',
        a: 'Inversión inicial detallada (CAPEX), proyección P&L mensual a 36 meses, cash flow operativo, ratios de viabilidad (margen bruto, EBITDA, payback, TIR), análisis sensibilidad y plan de contingencia. El banco quiere ver cifras realistas del mercado {country} — no proyecciones optimistas sin fundamento.',
      },
      {
        q: '¿Cuánto financiación puedo conseguir en {city} para abrir un restaurante?',
        a: 'Generalmente 60-70% de inversión total con aval personal. ICO Pyme y líneas hostelería ofrecen condiciones específicas en {country}. Necesitas aportar 30-40% capital propio + buen plan de negocio. Empresas con experiencia previa logran condiciones mejores que primer proyecto.',
      },
      {
        q: '¿Qué break-even es realista en un restaurante de {city}?',
        a: 'Depende del concepto y barrio. Casual mesa de 80 plazas en {city}: break-even mensual aprox 65-75% ocupación con ticket €25-35. Premium 50 plazas: 55-65% ocupación con ticket €60-90. Si tu plan no llega al break-even al mes 9-12 con ratios sectoriales, replantea concepto antes de comprometer financiación.',
      },
    ],
    schemaServiceName: 'Plan de Negocio Restaurante {city}',
    schemaServiceCategory: 'Restaurant Business Planning',
  },
};

/**
 * Helper para reemplazar tokens {city}, {country}, {totalRange}, etc. en strings
 */
import type { CityData } from './pseo-cities';

export function fillTemplate(template: string, city: CityData): string {
  const premiumNeighborhood = city.neighborhoods[0]?.name ?? '';
  const emergingNeighborhood = city.neighborhoods[city.neighborhoods.length - 1]?.name ?? '';
  const licenseTramitText = `${city.regulation.licenseType}. Tiempo real: ${city.regulation.tramitTime}. ${city.regulation.notes ?? ''}`;

  return template
    .replace(/\{city\}/g, city.displayName)
    .replace(/\{country\}/g, city.countryName)
    .replace(/\{currency\}/g, city.currency)
    .replace(/\{totalRange\}/g, city.cost.totalRange)
    .replace(/\{premiumNeighborhood\}/g, premiumNeighborhood)
    .replace(/\{emergingNeighborhood\}/g, emergingNeighborhood)
    .replace(/\{jefeCocinaSalary\}/g, city.salaries.jefeCocina)
    .replace(/\{licenseTramitText\}/g, licenseTramitText);
}
