/**
 * Programmatic SEO — Ciudades x Restaurantes
 *
 * Sub-proyecto pSEO Ciudades — sub-project arrancado 2026-05-01.
 * Validación deep research confirmó pivote: rol+ciudad descartado por intent mismatch.
 * Modificadores ganadores con intent comercial real:
 *   - abrir-restaurante (intent comercial alto, monetiza Guías €65-85)
 *   - licencia-restaurante (intent comercial alto, monetiza Pack APPCC + Guías)
 *   - software-gestion-restaurante (intent muy alto, monetiza SaaS suscripción)
 *   - escandallo-restaurante (intent medio, monetiza Kit Escandallos €12)
 *   - plan-negocio-restaurante (intent alto, monetiza Kit Plan Financiero €39)
 *
 * Data moat obligatorio por ciudad (anti-penalty Marzo 2026):
 *   coste apertura, regulación local, licencia/tiempos, salarios, barrios, ticket medio.
 */

export type PSeoModifier =
  | 'abrir-restaurante'
  | 'licencia-restaurante'
  | 'software-gestion-restaurante'
  | 'escandallo-restaurante'
  | 'plan-negocio-restaurante';

export type PSeoLang = 'es' | 'en' | 'fr' | 'de' | 'it' | 'pt' | 'nl';

export interface CitySalaries {
  jefeCocina: string;        // ej. "1.900-3.200 €/mes brutos"
  ayudante: string;
  camarero: string;
  source?: string;           // portal o estudio de referencia
}

export interface CityNeighborhood {
  name: string;
  ticketMedio: string;       // ej. "35-55 €"
  notes?: string;            // por qué es relevante para abrir
}

export interface CityRegulation {
  framework: string;         // ej. "APPCC (Reglamento CE 852/2004) + RD 3484/2000"
  licenseType: string;       // ej. "Licencia de Apertura clase III + actividad clasificada"
  tramitTime: string;        // ej. "3-9 meses según ayuntamiento"
  notes?: string;            // particularidades locales
}

export interface CityCostBreakdown {
  totalRange: string;        // ej. "€90.000 - €180.000"
  obra: string;              // ej. "€35.000 - €70.000"
  equipamiento: string;
  licencias: string;
  fianzaAlquiler: string;
  capitalCirculante: string;
  notes?: string;
}

export interface CityData {
  slug: string;              // url segment, ej. "madrid", "ciudad-de-mexico"
  displayName: string;       // ej. "Madrid", "Ciudad de México"
  country: string;           // ISO ej. "ES", "MX"
  countryName: string;       // ej. "España", "México"
  currency: string;          // ej. "€", "MXN"
  population: string;        // ej. "3.3M (área metropolitana 6.7M)"
  restaurantsCount?: string; // ej. "~12.500 establecimientos hostelería"
  cost: CityCostBreakdown;
  regulation: CityRegulation;
  salaries: CitySalaries;
  neighborhoods: CityNeighborhood[];  // 3-5 zonas relevantes
  marketNotes: string;       // 2-3 frases sobre tendencias locales
  sources?: string[];        // URLs de referencia para verificación
}

/**
 * Fase A — 15 ciudades de salida.
 * Datos iniciales: investigación pública (INE, ICEX, ProMexico, DANE, INDEC).
 * STATUS leyenda:
 *   - ✅ verified: datos completos verificados con fuentes
 *   - 🟡 partial: estructura lista, datos parciales, requiere refinamiento
 *   - 🔴 stub: solo placeholder, requiere investigación
 */
export const PSEO_CITIES: Record<string, CityData> = {
  // ✅ verified
  madrid: {
    slug: 'madrid',
    displayName: 'Madrid',
    country: 'ES',
    countryName: 'España',
    currency: '€',
    population: '3.3M (área metropolitana 6.7M)',
    restaurantsCount: '~28.000 establecimientos de hostelería (Madrid capital + área metro)',
    cost: {
      totalRange: '€110.000 - €280.000',
      obra: '€35.000 - €90.000 (según estado del local)',
      equipamiento: '€25.000 - €60.000 (cocina + sala)',
      licencias: '€3.500 - €12.000 (proyecto + tasas + ICIO)',
      fianzaAlquiler: '€18.000 - €60.000 (3-6 meses fianza zonas centro)',
      capitalCirculante: '€20.000 - €50.000 (3-6 meses operación)',
      notes: 'Coste muy variable según barrio. Centro/Salamanca multiplica obra y alquiler. Zonas emergentes (Tetuán, Carabanchel) reducen 30-40%.',
    },
    regulation: {
      framework: 'APPCC (Reglamento CE 852/2004) + RD 3484/2000 manipuladores + Ordenanza Municipal Madrid Protección contra Incendios',
      licenseType: 'Declaración Responsable o Licencia de Actividad (Ord. Madrid 2014). Restaurantes: clase III actividad recreativa de hostelería.',
      tramitTime: '15 días hábiles Declaración Responsable (apertura inmediata) — 3-9 meses Licencia clásica si proyecto complejo o local sin actividad previa similar',
      notes: 'Madrid permite Declaración Responsable para mayoría de restaurantes desde 2014. Reduce drásticamente tiempos vs municipios pequeños. ICIO ~4% del PEM.',
    },
    salaries: {
      jefeCocina: '€1.900 - €3.200/mes brutos (12 pagas) — sector Hostelería Madrid Convenio',
      ayudante: '€1.350 - €1.700/mes brutos',
      camarero: '€1.300 - €1.800/mes brutos + propinas',
      source: 'Convenio Hostelería Madrid 2025 + Indeed/Glassdoor Madrid',
    },
    neighborhoods: [
      { name: 'Salamanca / Recoletos', ticketMedio: '€55-120', notes: 'Alta gama, target ejecutivos y gastronómicos. Alquileres €40-80/m². Mejor ROI con concepto premium.' },
      { name: 'Chueca / Justicia', ticketMedio: '€35-65', notes: 'Gastrobar y casual creativo. Público joven con poder adquisitivo, alta rotación.' },
      { name: 'Malasaña / Conde Duque', ticketMedio: '€28-50', notes: 'Casual, bistronomic, brunch. Tendencias millennials/foodies.' },
      { name: 'Lavapiés / La Latina', ticketMedio: '€20-40', notes: 'Tapas tradicionales + cocinas del mundo. Alquiler más asequible.' },
      { name: 'Tetuán / Cuatro Caminos', ticketMedio: '€18-35', notes: 'Zona emergente. Alquileres 40% menos que centro. Gentrificación gastronómica activa.' },
    ],
    marketNotes: 'Madrid lidera España en aperturas y cierres de hostelería (~3.000 aperturas/año). Tendencias 2026: bistronomic, cocina latinoamericana premium (peruana, mexicana de autor), conceptos sostenibles, dark kitchens en perímetro. Concentración alta de restaurantes Michelin (~25 estrellas).',
    sources: [
      'Hostelería de España — Anuario',
      'Ayuntamiento de Madrid — Ordenanza ALAR',
      'Convenio Colectivo Hostelería Madrid 2024-2026',
    ],
  },

  barcelona: {
    slug: 'barcelona',
    displayName: 'Barcelona',
    country: 'ES',
    countryName: 'España',
    currency: '€',
    population: '1.6M (área metropolitana 4.9M)',
    restaurantsCount: '~17.000 establecimientos hostelería (Barcelona ciudad + área metro)',
    cost: {
      totalRange: '€100.000 - €260.000',
      obra: '€32.000 - €85.000',
      equipamiento: '€25.000 - €60.000',
      licencias: '€4.000 - €15.000 (Barcelona más estricta que Madrid)',
      fianzaAlquiler: '€16.000 - €55.000',
      capitalCirculante: '€20.000 - €50.000',
      notes: 'Eixample y Born muy caros. Poblenou y Sants opciones emergentes.',
    },
    regulation: {
      framework: 'APPCC (CE 852/2004) + Ordenança Municipal d\'Activitats Barcelona + Llei Catalana 16/2015 simplificació activitats',
      licenseType: 'Comunicació Prèvia (régimen general restauración) o Llicència Ambiental segons aforament',
      tramitTime: '1-3 meses Comunicació Prèvia — 6-12 meses si Llicència Ambiental',
      notes: 'Barcelona aplica moratoria de licencias en Ciutat Vella desde 2017 — limita aperturas en zonas saturadas. Verificar PEUAT antes de comprometer alquiler.',
    },
    salaries: {
      jefeCocina: '€1.950 - €3.300/mes brutos (12 pagas) — Eixample / Born premium hasta €4.200',
      ayudante: '€1.400 - €1.750/mes brutos',
      camarero: '€1.350 - €1.850/mes brutos + propinas',
      source: 'Conveni Col·lectiu Hostaleria Catalunya 2024-2026 + Indeed/InfoJobs Barcelona',
    },
    neighborhoods: [
      { name: 'Eixample Dret', ticketMedio: '€40-90', notes: 'Premium y media-alta. Alquileres €45-85/m². Alta densidad turística + local.' },
      { name: 'Born / Ribera', ticketMedio: '€35-75', notes: 'Restringido por moratoria PEUAT. Si consigues licencia, ROI alto.' },
      { name: 'Gràcia', ticketMedio: '€25-50', notes: 'Auténtico local + foodies. Buenos alquileres, comunidad fiel.' },
      { name: 'Poblenou', ticketMedio: '€25-55', notes: 'Zona emergente post-22@. Tech workers + lofts. Alquiler 30% menos que centro.' },
      { name: 'Sant Antoni', ticketMedio: '€28-55', notes: 'Renovado tras mercado. Mix locals + turistas. Gastronomía catalana moderna.' },
    ],
    marketNotes: 'Barcelona tiene la moratoria PEUAT activa que restringe nuevas licencias en zonas saturadas — fundamental verificar antes de firmar contrato. Escena gastronómica en consolidación post-elBulli: Disfrutar (#1 World 50 Best 2024), Cinc Sentits, Suculent. Tendencias 2026: sostenibilidad, km 0 catalán (Empordà), vermut moderno, brunch mediterráneo, cocina mediterránea fusión, vinos naturales Penedès.',
    sources: [
      'Departament de Salut Generalitat de Catalunya',
      'Ajuntament de Barcelona — PEUAT 2024',
      'Conveni Col·lectiu d\'Hostaleria de Catalunya',
    ],
  },

  valencia: {
    slug: 'valencia', displayName: 'Valencia', country: 'ES', countryName: 'España', currency: '€',
    population: '800k (área metro 1.6M)',
    restaurantsCount: '~7.500 establecimientos hostelería (Valencia capital + área metro)',
    cost: {
      totalRange: '€80.000 - €200.000',
      obra: '€25.000 - €65.000',
      equipamiento: '€22.000 - €50.000',
      licencias: '€2.500 - €8.000',
      fianzaAlquiler: '€10.000 - €36.000',
      capitalCirculante: '€18.000 - €40.000',
      notes: 'Valencia tiene costes 30-40% menores que Madrid/Barcelona. Ruzafa y centro encarecen alquiler; Cabanyal y barrios marítimos ofrecen mejor ratio €/m². ICIO Valencia ~3.5% del PEM.',
    },
    regulation: {
      framework: 'APPCC (CE 852/2004) + Ley Valenciana 14/2010 espectáculos + Ordenanza Reguladora Obras Edificación + Ord. Convivencia Valencia',
      licenseType: 'Declaración Responsable Ambiental (régimen general restauración hasta 500 m²) o Licencia Ambiental',
      tramitTime: '1-2 meses DR — 4-8 meses LA si proyecto técnico complejo',
      notes: 'Valencia simplificó trámites en 2018 con DR Ambiental. Verificar si la zona tiene Plan Especial (Ciutat Vella tiene moratoria parcial nocturna). Inspección sanitaria post-apertura obligatoria primeros 3 meses.',
    },
    salaries: {
      jefeCocina: '€1.700 - €2.700/mes brutos (12 pagas)',
      ayudante: '€1.250 - €1.550/mes brutos',
      camarero: '€1.200 - €1.600/mes brutos + propinas',
      source: 'Convenio Hostelería Valencia 2024-2026 + Indeed/InfoJobs Valencia',
    },
    neighborhoods: [
      { name: 'Ruzafa', ticketMedio: '€25-50', notes: 'Hipster + foodie. Alta concentración locales modernos. Alquileres €25-45/m².' },
      { name: 'El Carmen / Ciutat Vella', ticketMedio: '€30-60', notes: 'Turístico + tradicional. Verificar restricciones por moratoria nocturna.' },
      { name: 'Cabanyal', ticketMedio: '€20-45', notes: 'Frente al mar, gentrificación reciente. Mejor coste de entrada de Valencia capital.' },
      { name: 'Eixample / Gran Vía Marqués del Turia', ticketMedio: '€35-70', notes: 'Premium residencial. Target ejecutivos y familias alto poder.' },
    ],
    marketNotes: 'Valencia con boom de aperturas post-COVID — World Design Capital 2022 + Capital Verde 2024 atrajeron turismo gastronómico. Costes 30-40% menores que Madrid/Barcelona. Tendencias 2026: arroz moderno (no solo paella), cocina mediterránea km 0, vermutería, brunch healthy mediterráneo.',
    sources: [
      'Conselleria Sanitat Universal Generalitat Valenciana',
      'Ayuntamiento de Valencia — Ordenanza Municipal',
      'Convenio Colectivo Hostelería Valencia 2024-2026',
    ],
  },

  sevilla: {
    slug: 'sevilla', displayName: 'Sevilla', country: 'ES', countryName: 'España', currency: '€',
    population: '690k (área metro 1.5M)',
    restaurantsCount: '~6.200 establecimientos hostelería (Sevilla capital + área metro)',
    cost: {
      totalRange: '€70.000 - €180.000',
      obra: '€22.000 - €58.000',
      equipamiento: '€20.000 - €45.000',
      licencias: '€2.500 - €7.500',
      fianzaAlquiler: '€8.000 - €30.000',
      capitalCirculante: '€15.000 - €38.000',
      notes: 'Sevilla con costes 35-45% menores que Madrid. Centro histórico (Santa Cruz, Alfalfa) tiene normativa restrictiva por patrimonio UNESCO — encarece licencia y obra. Triana y Nervión ofrecen mejor ratio inversión/flujo.',
    },
    regulation: {
      framework: 'APPCC (CE 852/2004) + Ley Andaluza 13/1999 espectáculos + Decreto 78/2002 catálogo establecimientos + Ordenanza Sevilla',
      licenseType: 'Declaración Responsable o Licencia Ambiental Unificada Andaluza (LAU) según aforo y actividad',
      tramitTime: '1-3 meses DR — 6-10 meses LAU si aforo >50 personas o local sin actividad previa similar',
      notes: 'Centro histórico exige informe favorable Comisión Patrimonio. Veladores (terrazas) requieren autorización municipal aparte con tasas anuales. Inspección sanitaria Junta Andalucía obligatoria pre-apertura.',
    },
    salaries: {
      jefeCocina: '€1.600 - €2.500/mes brutos',
      ayudante: '€1.200 - €1.500/mes brutos',
      camarero: '€1.150 - €1.500/mes brutos + propinas',
      source: 'Convenio Hostelería Sevilla 2024-2026 + portales empleo locales',
    },
    neighborhoods: [
      { name: 'Triana', ticketMedio: '€20-45', notes: 'Identitario sevillano. Alquileres moderados (€18-30/m²), alto flujo turismo + local.' },
      { name: 'Alfalfa / Alameda', ticketMedio: '€25-50', notes: 'Centro turístico + nightlife. Densidad alta, competencia feroz.' },
      { name: 'Los Remedios', ticketMedio: '€30-60', notes: 'Residencial alto. Restaurantes familiares premium, baja rotación clientela.' },
      { name: 'Nervión', ticketMedio: '€22-45', notes: 'Comercial + residencial medio. Buen ratio precio/visibilidad.' },
    ],
    marketNotes: 'Sevilla con fuerte componente turístico (~3M visitantes/año, 9M pernoctaciones). Tapeo identitario. Costes muy bajos vs Madrid. Tendencias 2026: tapas creativas, fusión andaluza-internacional, vermut moderno, slow food km 0 sevillano. Ojo con saturación Centro: rotación de cierres alta.',
    sources: [
      'Junta de Andalucía — Sanidad Alimentaria',
      'Ayuntamiento de Sevilla — Ordenanza Municipal',
      'Convenio Colectivo Hostelería Sevilla',
    ],
  },

  malaga: {
    slug: 'malaga', displayName: 'Málaga', country: 'ES', countryName: 'España', currency: '€',
    population: '580k (Costa del Sol >1.7M)',
    restaurantsCount: '~9.500 establecimientos hostelería (Málaga capital + Costa del Sol)',
    cost: {
      totalRange: '€80.000 - €220.000',
      obra: '€25.000 - €70.000',
      equipamiento: '€22.000 - €52.000',
      licencias: '€3.000 - €9.000',
      fianzaAlquiler: '€10.000 - €40.000',
      capitalCirculante: '€18.000 - €45.000',
      notes: 'Boom inmobiliario 2024-2026 disparó alquileres en Málaga capital (Soho, Centro) +25-40%. Marbella y Puerto Banús requieren inversión Premium (€200k+). Pueblos blancos interior reducen 50% vs costa.',
    },
    regulation: {
      framework: 'APPCC (CE 852/2004) + Ley Andaluza 13/1999 espectáculos + Decreto 78/2002 + Ordenanzas Málaga / Marbella según municipio',
      licenseType: 'Declaración Responsable o Licencia Ambiental Unificada Andaluza (LAU)',
      tramitTime: '1-3 meses DR — 6-10 meses LAU. Marbella tiende a tiempos más largos por revisión patrimonial costa.',
      notes: 'Costa del Sol exige cumplimiento normativa playa si tu local da a primera línea (Ley Costas + chiringuitos). Marbella aplica criterios estrictos en zonas turísticas premium. Verifica cédula urbanística antes de comprometer alquiler.',
    },
    salaries: {
      jefeCocina: '€1.700 - €2.800/mes brutos (premium temporada alta hasta €3.500)',
      ayudante: '€1.250 - €1.600/mes brutos',
      camarero: '€1.200 - €1.700/mes brutos + propinas turísticas (especialmente Marbella)',
      source: 'Convenio Hostelería Málaga 2024-2026 + portales empleo Costa del Sol',
    },
    neighborhoods: [
      { name: 'Soho / Centro Histórico', ticketMedio: '€30-65', notes: 'Galerías Pompidou + foodie. Pujante. Alquileres €30-55/m².' },
      { name: 'Pedregalejo / El Palo', ticketMedio: '€25-50', notes: 'Marisco + chiringuitos premium. Identitario malagueño.' },
      { name: 'Marbella centro', ticketMedio: '€60-150', notes: 'Alta gama, target internacional. Inversión y operación 2x sobre Málaga capital.' },
      { name: 'La Malagueta / Limonar', ticketMedio: '€35-80', notes: 'Premium residencial costa. Familias clase alta + turismo nacional.' },
    ],
    marketNotes: 'Málaga + Costa del Sol = mercado dual: residente local + turismo internacional alto poder adquisitivo. Málaga capital lidera en captación nómadas digitales internacionales 2024-2026 (top 3 Europa). Tendencias: gastronomía de mar mediterránea creativa, brunch, fusión andaluza-asiática, healthy bowls.',
    sources: [
      'Junta de Andalucía — Sanidad Alimentaria',
      'Ayuntamiento de Málaga + Marbella — Ordenanzas',
      'Convenio Colectivo Hostelería Málaga',
    ],
  },

  bilbao: {
    slug: 'bilbao', displayName: 'Bilbao', country: 'ES', countryName: 'España', currency: '€',
    population: '345k (Bizkaia 1.1M)',
    restaurantsCount: '~3.800 establecimientos hostelería (Bilbao + Bizkaia ~7.500)',
    cost: {
      totalRange: '€85.000 - €210.000',
      obra: '€28.000 - €68.000',
      equipamiento: '€24.000 - €55.000',
      licencias: '€3.500 - €10.000',
      fianzaAlquiler: '€10.000 - €38.000',
      capitalCirculante: '€18.000 - €42.000',
      notes: 'Bilbao mantiene costes operativos altos por nivel salarial vasco (15-20% sobre media española). Casco Viejo y Abando son zonas premium con alquileres €30-55/m². Bilbao La Vieja y zona Olabeaga ofrecen oportunidad emergente con alquiler 30-40% menor.',
    },
    regulation: {
      framework: 'APPCC (CE 852/2004) + Ley Vasca 4/1995 espectáculos + Decreto 17/2019 turismo + Ordenanza Bilbao + Reglamento Sanitario Euskadi',
      licenseType: 'Comunicación Previa Actividad (régimen general restauración) o Licencia Actividad Calificada según aforo y actividades complementarias',
      tramitTime: '1-3 meses CP — 5-9 meses LA. Patrimonio Casco Viejo añade 1-2 meses por informes.',
      notes: 'Euskadi tiene normativa propia muy estricta de manipulador de alimentos (formación sectorial obligatoria). Casco Viejo requiere informes patrimonio. Música en directo exige licencia ampliada y aislamiento acústico documentado.',
    },
    salaries: {
      jefeCocina: '€2.000 - €3.300/mes brutos (mercado vasco premium, Michelin hasta €4.500)',
      ayudante: '€1.450 - €1.800/mes brutos',
      camarero: '€1.400 - €1.900/mes brutos + propinas',
      source: 'Convenio Hostelería Bizkaia 2024-2026 + Lanbide observatorio empleo',
    },
    neighborhoods: [
      { name: 'Casco Viejo', ticketMedio: '€25-55', notes: 'Pintxos + tradicional. Muy turístico, alta competencia. Las 7 Calles concentran flujo.' },
      { name: 'Indautxu / Abando', ticketMedio: '€35-75', notes: 'Premium + residencial. Profesionales y ejecutivos. Mejor ticket medio Bilbao.' },
      { name: 'Bilbao La Vieja / San Francisco', ticketMedio: '€20-45', notes: 'Emergente, gentrificación, escena foodie joven. Alquileres más asequibles.' },
      { name: 'Deusto', ticketMedio: '€22-48', notes: 'Residencial universitario + familias. Restaurantes de barrio fieles.' },
    ],
    marketNotes: 'Bilbao referente gastronómico mundial (Asador Etxebarri #1 Best 50, Mina, Mugaritz cercano). Guggenheim effect mantiene flujo turístico premium constante. Salarios 15-20% mayores que media española. Pintxo es identitario y barrera de entrada (calidad muy alta del estándar local). Tendencias 2026: alta cocina vasca de producto km 0, txakoli pairings, txuleta de vaca vieja, conservas premium.',
    sources: [
      'Departamento Salud Gobierno Vasco',
      'Ayuntamiento de Bilbao — Ordenanza Municipal',
      'Convenio Colectivo Hostelería Bizkaia',
    ],
  },

  zaragoza: {
    slug: 'zaragoza', displayName: 'Zaragoza', country: 'ES', countryName: 'España', currency: '€',
    population: '680k (área metropolitana 770k)',
    restaurantsCount: '~3.500 establecimientos hostelería en Zaragoza ciudad',
    cost: {
      totalRange: '€65.000 - €165.000',
      obra: '€20.000 - €52.000',
      equipamiento: '€18.000 - €42.000',
      licencias: '€2.500 - €7.500',
      fianzaAlquiler: '€7.000 - €28.000',
      capitalCirculante: '€14.000 - €35.000',
      notes: 'Zaragoza tiene los costes más competitivos de las grandes ciudades españolas (35-45% menos que Madrid). Centro / Independencia premium; Casco Histórico moderado; Actur/Universidad económicos. Operación financiera más alcanzable para primer proyecto.',
    },
    regulation: {
      framework: 'APPCC (CE 852/2004) + Ley Aragonesa 11/2005 espectáculos + Ordenanza Municipal Zaragoza Actividades + Decreto Aragón sanidad alimentaria',
      licenseType: 'Comunicación Previa Actividad o Licencia Ambiental Calificada según aforo / actividades complementarias',
      tramitTime: '1-3 meses CP — 5-9 meses LA. Zaragoza administrativamente ágil dentro de la media nacional.',
      notes: 'Zaragoza permite Comunicación Previa para mayoría restaurantes desde 2014. Casco Histórico requiere informe patrimonio cuando hay obra estructural. ICIO ~3.5% PEM. Inspección DGA Salud Pública pre-apertura obligatoria.',
    },
    salaries: {
      jefeCocina: '€1.600 - €2.500/mes brutos',
      ayudante: '€1.200 - €1.500/mes brutos',
      camarero: '€1.150 - €1.550/mes brutos + propinas',
      source: 'Convenio Hostelería Zaragoza 2024-2026 + INAEM observatorio',
    },
    neighborhoods: [
      { name: 'Casco Histórico / El Tubo', ticketMedio: '€25-50', notes: 'Centro tapas tradicional zaragozano. Alto flujo turístico + local fines de semana.' },
      { name: 'Centro / Independencia', ticketMedio: '€30-60', notes: 'Premium financiero. Comercial alta, ejecutivos. Mejor ticket medio Zaragoza.' },
      { name: 'Universidad / Romareda', ticketMedio: '€18-35', notes: 'Estudiantes + residencial joven. Volumen alto, ticket bajo. Casual y fast-casual rentables.' },
      { name: 'Actur / Parque Goya', ticketMedio: '€20-40', notes: 'Residencial moderno expansión norte. Familias. Alquileres bajos.' },
    ],
    marketNotes: 'Zaragoza con costes 35-45% menores que Madrid y mercado consolidado de baja rotación (clientela fiel multigeneracional). Población estable pero economía industrial sólida (Opel/PSA, logística). Tendencias 2026: tapa moderna evolución del tradicional Tubo, ternasco aragonés contemporáneo, vino DO Cariñena/Calatayud, productos km 0 aragoneses (jamón Teruel, aceite Bajo Aragón).',
    sources: [
      'Departamento Sanidad Gobierno de Aragón',
      'Ayuntamiento de Zaragoza — Ordenanza Municipal Actividades',
      'Convenio Colectivo Hostelería Zaragoza',
    ],
  },

  'ciudad-de-mexico': {
    slug: 'ciudad-de-mexico', displayName: 'Ciudad de México', country: 'MX', countryName: 'México', currency: 'MXN',
    population: '9.2M (zona metropolitana 22M)',
    restaurantsCount: '~50.000 establecimientos formales + ~120.000 informales (CANIRAC + INEGI)',
    cost: {
      totalRange: 'MXN $1.5M - $5M (≈USD $80k-$280k)',
      obra: 'MXN $400k - $1.5M',
      equipamiento: 'MXN $350k - $1.2M',
      licencias: 'MXN $80k - $250k',
      fianzaAlquiler: 'MXN $250k - $1M (3-6 meses garantía)',
      capitalCirculante: 'MXN $400k - $1.2M',
      notes: 'CDMX tiene altísima variabilidad por alcaldía. Polanco / Lomas / Santa Fe 2-3x más caros que Iztapalapa o Coyoacán. Roma Norte / Condesa duplicó alquileres 2020-2026 por boom nómada digital. Considera Programa Interno de Protección Civil (DRO) ~MXN $80-200k aparte.',
    },
    regulation: {
      framework: 'NOM-251-SSA1-2009 (prácticas higiene alimentos) + NOM-093-SSA1-1994 + COFEPRIS Federal + Reglamento Establecimientos Mercantiles CDMX + Ley Protección Civil',
      licenseType: 'Aviso de Funcionamiento COFEPRIS + Licencia Establecimiento Mercantil con/sin venta alcohol + Programa Interno Protección Civil (PIPC) + Constancia de Uso de Suelo + Visto Bueno Bomberos',
      tramitTime: '2-6 meses (depende alcaldía y giro de bebidas alcohólicas — alcohol añade 2-3 meses)',
      notes: 'CDMX exige Director Responsable de Obra (DRO) corresponsable para PIPC. Venta alcohol requiere licencia específica con horarios restringidos. Alcaldías con normativa propia: Cuauhtémoc y Miguel Hidalgo más estrictas, Tlalpan y Xochimilco más ágiles.',
    },
    salaries: {
      jefeCocina: 'MXN $25.000 - $55.000/mes brutos (premium Polanco / Roma hasta $80k, Pujol/Quintonil $100k+)',
      ayudante: 'MXN $9.000 - $14.000/mes brutos',
      camarero: 'MXN $8.000 - $13.000/mes brutos + propinas (10-15% del consumo)',
      source: 'CANIRAC observatorio + OCC Mundial + Indeed México',
    },
    neighborhoods: [
      { name: 'Polanco', ticketMedio: '$650-1.800 MXN', notes: 'Top gama. Alquileres premium ($800-1.500/m²). Target alto poder adquisitivo + corporativo.' },
      { name: 'Roma Norte / Condesa', ticketMedio: '$350-900 MXN', notes: 'Foodie capital LATAM + millennials + nómadas digitales. Boom aperturas autor 2020-2026.' },
      { name: 'Coyoacán / San Ángel', ticketMedio: '$300-700 MXN', notes: 'Tradicional con toque cultural-bohemio. Familias + turismo cultural.' },
      { name: 'Juárez / Cuauhtémoc', ticketMedio: '$300-800 MXN', notes: 'Renovación urbana. Mezcalerías + cocina autor emergente. Mejor ratio precio/visibilidad centro.' },
      { name: 'Santa Fe', ticketMedio: '$400-1.200 MXN', notes: 'Corporativo lunes-viernes. Comida ejecutiva + cenas premium. Riesgo: vacío fines de semana.' },
    ],
    marketNotes: 'CDMX es el mercado gastronómico líder de LATAM con 6 restaurantes en World\'s 50 Best Latam (Pujol, Quintonil, Sud777, Rosetta, Máximo, Em). Tendencias 2026: revalorización cocina mexicana de origen y producto endémico (huitlacoche, chinicuiles, hormigas chicatanas), mezcal y destilados nativos, omakase mexicano, fonda gourmet, sostenibilidad agrícola tradicional. Mercado muy competitivo en zonas premium — diferencial creativo es vital.',
    sources: [
      'CANIRAC — Cámara Nacional Industria de Restaurantes',
      'COFEPRIS — Comisión Federal Protección Riesgos Sanitarios',
      'Reglamento Establecimientos Mercantiles CDMX',
    ],
  },

  guadalajara: {
    slug: 'guadalajara', displayName: 'Guadalajara', country: 'MX', countryName: 'México', currency: 'MXN',
    population: '1.5M (zona metropolitana 5M, segunda más grande México)',
    restaurantsCount: '~18.000 establecimientos formales (zona metro Guadalajara)',
    cost: {
      totalRange: 'MXN $900k - $3M (≈USD $50k-$170k)',
      obra: 'MXN $250k - $900k',
      equipamiento: 'MXN $250k - $850k',
      licencias: 'MXN $50k - $180k',
      fianzaAlquiler: 'MXN $150k - $600k',
      capitalCirculante: 'MXN $250k - $700k',
      notes: 'Guadalajara con costes 30-40% menores que CDMX. Lafayette / Americana se encareció rápido 2022-2026 por boom foodie. Centro Histórico aprovecha alquileres moderados pero exige normativa patrimonial. Tlaquepaque / Tonalá ofrecen zona turística con costes bajos.',
    },
    regulation: {
      framework: 'NOM-251-SSA1-2009 + COFEPRIS Federal + Reglamento Municipal Guadalajara + Reglamento Estatal Jalisco protección civil',
      licenseType: 'Licencia Municipal de Giro Restaurantero + Aviso de Funcionamiento COFEPRIS + Programa Interno de Protección Civil + Visto Bueno Bomberos',
      tramitTime: '1-4 meses (Guadalajara administrativamente más ágil que CDMX)',
      notes: 'Centro Histórico requiere informes INAH si edificio histórico. Bebidas alcohólicas requieren licencia adicional con horarios. Tlaquepaque y Zapopan tienen reglamentos municipales propios distintos a Guadalajara capital.',
    },
    salaries: {
      jefeCocina: 'MXN $20.000 - $42.000/mes brutos (premium Andares / Puerta de Hierro hasta $60k)',
      ayudante: 'MXN $7.500 - $12.000/mes brutos',
      camarero: 'MXN $7.000 - $11.000/mes brutos + propinas',
      source: 'CANIRAC Jalisco + OCC Mundial Guadalajara',
    },
    neighborhoods: [
      { name: 'Providencia / Chapalita', ticketMedio: '$300-800 MXN', notes: 'Premium residencial. Familias clase alta tapatía. Restaurantes consolidados con clientela fiel.' },
      { name: 'Lafayette / Americana', ticketMedio: '$350-900 MXN', notes: 'Foodie + restaurantes de autor. Boom aperturas premium 2022-2026. Distrito gastronómico oficial.' },
      { name: 'Centro Histórico', ticketMedio: '$200-500 MXN', notes: 'Tradicional + turístico. Alquileres moderados pero normativa patrimonio.' },
      { name: 'Andares / Puerta de Hierro (Zapopan)', ticketMedio: '$500-1.300 MXN', notes: 'Zona corporate premium. Target ejecutivos + alto poder adquisitivo. Comparable Polanco CDMX.' },
    ],
    marketNotes: 'Guadalajara cuna del tequila y birria, capital cultural de Occidente. Costes 30-40% menores que CDMX y mercado menos saturado. Tendencias 2026: birria moderna (caldo + taco), tequila pairings, cocina tapatía contemporánea, mezcal jalisciense, omakase y fine dining elevando la ciudad gastronómica. Andares concentra concepto premium nuevo.',
    sources: [
      'CANIRAC Jalisco',
      'COFEPRIS — Aviso Funcionamiento',
      'Reglamento Municipal Guadalajara — Establecimientos Mercantiles',
    ],
  },

  monterrey: {
    slug: 'monterrey', displayName: 'Monterrey', country: 'MX', countryName: 'México', currency: 'MXN',
    population: '1.1M (zona metropolitana 5.3M, tercera más grande México)',
    restaurantsCount: '~16.500 establecimientos formales (zona metro Monterrey)',
    cost: {
      totalRange: 'MXN $1.2M - $4M (≈USD $65k-$220k)',
      obra: 'MXN $300k - $1.1M',
      equipamiento: 'MXN $300k - $1M',
      licencias: 'MXN $60k - $200k',
      fianzaAlquiler: 'MXN $200k - $800k',
      capitalCirculante: 'MXN $300k - $900k',
      notes: 'San Pedro Garza García (municipio más rico LATAM por ingreso per cápita) duplica costes de Monterrey capital. Carretera Nacional y Valle Oriente premium. Centro Monterrey y Barrio Antiguo más asequibles. Construcción cara por cumplir normas sismicidad.',
    },
    regulation: {
      framework: 'NOM-251-SSA1-2009 + COFEPRIS Federal + Reglamento Estatal Nuevo León + Reglamento Municipal Monterrey + Protección Civil Estatal',
      licenseType: 'Licencia de Funcionamiento Municipal Restaurante + Aviso COFEPRIS + Dictamen de Uso de Suelo + Visto Bueno Bomberos + Programa Interno Protección Civil',
      tramitTime: '1-4 meses (Monterrey y San Pedro administrativamente ágiles, mejor ranking México)',
      notes: 'San Pedro tiene reglamento propio más estricto (estética urbanística, terraza requiere proyecto arquitectónico). Garza García y Apodaca regulan industrial pesado — verifica zonificación. Permiso bebidas alcohólicas estatal con horarios.',
    },
    salaries: {
      jefeCocina: 'MXN $24.000 - $48.000/mes brutos (premium San Pedro hasta $70k, Pangea / Koli hasta $90k)',
      ayudante: 'MXN $9.000 - $13.500/mes brutos',
      camarero: 'MXN $8.500 - $12.500/mes brutos + propinas',
      source: 'CANIRAC Nuevo León + OCC Mundial Monterrey + Indeed',
    },
    neighborhoods: [
      { name: 'San Pedro Garza García', ticketMedio: '$500-1.500 MXN', notes: 'Municipio más rico LATAM. Alta gama corporate + familiar premium. Operación financiera demanda capital alto.' },
      { name: 'Valle Oriente / Carretera Nacional', ticketMedio: '$400-1.000 MXN', notes: 'Corporativo + residencial alto. Comida ejecutiva + cenas premium. Plazas comerciales premium.' },
      { name: 'Barrio Antiguo', ticketMedio: '$300-700 MXN', notes: 'Histórico renovado, foodie + nightlife. Mejor zona aperturas autor + emergente Monterrey.' },
      { name: 'Centro Monterrey / Macroplaza', ticketMedio: '$250-600 MXN', notes: 'Tradicional + corporativo gobierno. Volumen comida lunes-viernes.' },
    ],
    marketNotes: 'Monterrey con poder adquisitivo más alto de México (PIB per cápita similar a España, más alto que cualquier otra ciudad LATAM). Cabrito, machaca, cortes premium identitarios. Boom steakhouses alta gama (Sonora Grill Prime, Cabrera 7) y franquicias internacionales. Pangea y Koli en World\'s 50 Best Latam 2024-2026. Tendencias: parrilla norteña fine dining, mezcal y destilados artesanales, fusión texmex contemporánea, omakase regio.',
    sources: [
      'CANIRAC Nuevo León',
      'COFEPRIS — Aviso Funcionamiento',
      'Reglamento Municipal Monterrey + San Pedro',
    ],
  },

  queretaro: {
    slug: 'queretaro', displayName: 'Querétaro', country: 'MX', countryName: 'México', currency: 'MXN',
    population: '900k (zona metropolitana 1.6M, ciudad mayor crecimiento México)',
    restaurantsCount: '~5.500 establecimientos formales (zona metro Querétaro)',
    cost: {
      totalRange: 'MXN $700k - $2.2M (≈USD $40k-$120k)',
      obra: 'MXN $200k - $700k',
      equipamiento: 'MXN $200k - $600k',
      licencias: 'MXN $40k - $130k',
      fianzaAlquiler: 'MXN $100k - $400k',
      capitalCirculante: 'MXN $200k - $500k',
      notes: 'Querétaro tiene los costes más competitivos de las grandes ciudades mexicanas. Centro Histórico (UNESCO) requiere normativa patrimonio que encarece obra ~20%. Juriquilla (alta gama) y El Refugio (residencial premium) más caros. Antea / Plaza Real comerciales con buen ROI.',
    },
    regulation: {
      framework: 'NOM-251-SSA1-2009 + COFEPRIS + Reglamento Municipal Querétaro + Reglamento Centro Histórico (zona UNESCO patrimonio mundial)',
      licenseType: 'Licencia de Funcionamiento Municipal + Aviso COFEPRIS + Dictamen Uso de Suelo + Visto Bueno Bomberos + (si Centro Histórico) Visto Bueno INAH',
      tramitTime: '1-3 meses (Querétaro entre los más ágiles de México por digitalización trámites)',
      notes: 'Centro Histórico exige aprobación INAH para fachadas, rótulos, terrazas — añade 1-2 meses pero protege singularidad del local. Bebidas alcohólicas requieren licencia adicional. Zonas industriales (El Marqués, Bernardo Quintana) más fáciles trámite pero menos flujo cliente.',
    },
    salaries: {
      jefeCocina: 'MXN $20.000 - $38.000/mes brutos',
      ayudante: 'MXN $7.500 - $11.500/mes brutos',
      camarero: 'MXN $7.000 - $10.500/mes brutos + propinas',
      source: 'CANIRAC Querétaro + OCC Mundial + portales empleo regionales',
    },
    neighborhoods: [
      { name: 'Centro Histórico (UNESCO)', ticketMedio: '$300-800 MXN', notes: 'Patrimonio Humanidad + turismo cultural intenso. Encanto único pero normativa restrictiva.' },
      { name: 'Juriquilla', ticketMedio: '$300-700 MXN', notes: 'Residencial alto + expats tech (Intel, BlackBerry, Samsung). Familias jóvenes alto poder.' },
      { name: 'Milenio III / Antea', ticketMedio: '$250-600 MXN', notes: 'Comercial moderno + plazas. Concepto familiar y casual rentables.' },
      { name: 'El Refugio / La Vista', ticketMedio: '$400-1.000 MXN', notes: 'Residencial premium emergente. Target ejecutivos y empresarios.' },
    ],
    marketNotes: 'Querétaro es la ciudad de mayor crecimiento económico de México (clúster aeroespacial + tech + automotriz). Migración nacional alta (CDMX, Monterrey expats), demanda creciente. Vinos Valle Tequisquiapan / Bernal emergentes. Costes muy competitivos. Tendencias 2026: cocina queretana con producto local (xoconostle, queso Tequisquiapan), enoturismo gastronómico, fine dining de mercado, conceptos familiares premium.',
    sources: [
      'CANIRAC Querétaro',
      'COFEPRIS — Aviso Funcionamiento',
      'Reglamento Municipal Querétaro + INAH Centro Histórico',
    ],
  },

  bogota: {
    slug: 'bogota', displayName: 'Bogotá', country: 'CO', countryName: 'Colombia', currency: 'COP',
    population: '8M (área metro 11M, ciudad más grande Colombia)',
    restaurantsCount: '~32.000 establecimientos formales (Cámara Comercio Bogotá)',
    cost: {
      totalRange: 'COP $300M - $1.200M (≈USD $75k-$300k)',
      obra: 'COP $80M - $300M',
      equipamiento: 'COP $80M - $250M',
      licencias: 'COP $15M - $60M',
      fianzaAlquiler: 'COP $40M - $200M (4-6 meses garantía + arrendador exige codeudor o póliza)',
      capitalCirculante: 'COP $80M - $250M',
      notes: 'Bogotá tiene gran disparidad por zona. Zona G y Zona T duplican costes vs Chapinero Alto o La Candelaria. Importación equipamiento castigada por aranceles + IVA 19%. Considera Sayco-Acinpro (derechos autor música) ~COP $300k-1M/año aparte.',
    },
    regulation: {
      framework: 'Resolución 2674 de 2013 INVIMA (BPM alimentos) + Decreto 3075/97 + Ley 9 de 1979 sanitaria + Reglamento Distrital Bogotá + Plan de Ordenamiento Territorial (POT) por uso de suelo',
      licenseType: 'Concepto Sanitario Favorable Secretaría Distrital Salud + Registro Mercantil Cámara Comercio Bogotá + Concepto Técnico Bomberos + Sayco-Acinpro (música ambiental/vivo) + Uso de Suelo conforme POT',
      tramitTime: '2-5 meses (gestión paralela ahorra 1-2 meses; Bogotá digitalizó VUE - Ventanilla Única Empresarial)',
      notes: 'Bogotá exige verificación uso de suelo previo a firma alquiler — zonas residenciales NO permiten venta alcohol. Concepto Bomberos requiere proyecto contra incendios firmado por ingeniero. POT 2024 reformuló zonificación: zonas Mixto Urbano (M1-M4) son ideales restaurante. Inspección sanitaria semestral.',
    },
    salaries: {
      jefeCocina: 'COP $4.5M - $9M/mes brutos (premium Zona G/T hasta $14M, Leo/Mini-Mal $18M+)',
      ayudante: 'COP $1.5M - $2.4M/mes brutos',
      camarero: 'COP $1.4M - $2.2M/mes brutos + propinas (10% sugerida ley)',
      source: 'ACODRES + Computrabajo Colombia + Ministerio Trabajo Colombia',
    },
    neighborhoods: [
      { name: 'Zona G (Quinta Camacho)', ticketMedio: 'COP $80k-180k', notes: 'Gourmet by definition (G = Gourmet). Alta gama, target ejecutivos + fine dining. Alquileres premium.' },
      { name: 'Zona T / Parque 93', ticketMedio: 'COP $60k-150k', notes: 'Comercial + nightlife premium. Mix retail + restaurantes + clubs. Alto flujo viernes-sábado.' },
      { name: 'Usaquén', ticketMedio: 'COP $50k-120k', notes: 'Histórico + mercado pulgas dominical. Casual premium familiar.' },
      { name: 'Chapinero Alto / La Macarena', ticketMedio: 'COP $40k-95k', notes: 'Foodie + autor + bohemio. Mejor zona aperturas creativas. Alquileres más bajos vs Zona G.' },
      { name: 'Salitre / Park Way', ticketMedio: 'COP $45k-100k', notes: 'Residencial alto. Familias clase alta. Restaurantes consolidados con clientela fiel.' },
    ],
    marketNotes: 'Bogotá con escena gastronómica explosiva: Leo (Leonor Espinosa) #1 World\'s 50 Best Latin 2022, Mini-Mal, Sumá, El Chato consolidados. Tendencias 2026: cocina colombiana contemporánea con ingredientes endémicos amazónicos (asaí, copoazú, hormigas culonas), café especial origen Quindío/Huila, fusión afro-andina del Pacífico, sostenibilidad agropecuaria con campesinado. Mercado en plena expansión, lugar para concepto autor diferencial.',
    sources: [
      'INVIMA — Resolución 2674/2013',
      'Cámara de Comercio de Bogotá',
      'Secretaría Distrital de Salud Bogotá',
      'ACODRES — Asociación Colombiana de la Industria Gastronómica',
    ],
  },

  medellin: {
    slug: 'medellin', displayName: 'Medellín', country: 'CO', countryName: 'Colombia', currency: 'COP',
    population: '2.5M (área metropolitana 4M)',
    restaurantsCount: '~14.000 establecimientos formales (Cámara Comercio Medellín + Aburrá)',
    cost: {
      totalRange: 'COP $200M - $800M (≈USD $50k-$200k)',
      obra: 'COP $50M - $200M',
      equipamiento: 'COP $60M - $180M',
      licencias: 'COP $10M - $40M',
      fianzaAlquiler: 'COP $25M - $130M',
      capitalCirculante: 'COP $55M - $170M',
      notes: 'Medellín con costes 25-35% menores que Bogotá. El Poblado (Provenza, Manila) duplicó alquileres 2020-2026 por boom nómada digital. Laureles y Envigado mantienen mejor ratio inversión/flujo. Sabaneta y Itagüí emergentes como zonas residenciales premium.',
    },
    regulation: {
      framework: 'Resolución 2674 de 2013 INVIMA + Decreto 3075/97 + Acuerdo Municipal Medellín + POT Medellín 2024',
      licenseType: 'Concepto Sanitario Favorable Secretaría Salud Medellín + Registro Mercantil Cámara Comercio Medellín + Concepto Bomberos + Sayco-Acinpro + Uso de Suelo conforme POT',
      tramitTime: '2-4 meses (Medellín mejoró ranking digitalización trámites Colombia)',
      notes: 'Medellín exige Plan de Cumplimiento Ambiental para zonas mixtas. El Poblado tiene normativa específica horario nocturno (cierre extendido viernes-sábado). Provenza con saturación: nuevas aperturas en zona específica requieren estudio de viabilidad previo. Inspección semestral.',
    },
    salaries: {
      jefeCocina: 'COP $4M - $7.5M/mes brutos (premium El Poblado hasta $11M)',
      ayudante: 'COP $1.4M - $2.2M/mes brutos',
      camarero: 'COP $1.3M - $2M/mes brutos + propinas (10% sugerida)',
      source: 'ACODRES Antioquia + Computrabajo Medellín + Cámara Comercio Aburrá',
    },
    neighborhoods: [
      { name: 'El Poblado / Provenza', ticketMedio: 'COP $50k-130k', notes: 'Foodie boom + nómadas digitales. Mejor punto comercial Colombia, alta competencia. Alquileres premium.' },
      { name: 'Laureles', ticketMedio: 'COP $35k-85k', notes: 'Local + creciente internacional. Mejor ratio precio/flujo. Familias y profesionales jóvenes.' },
      { name: 'Envigado', ticketMedio: 'COP $30k-75k', notes: 'Tradicional paisa, residencial alto. Restaurantes familiares premium con clientela fiel.' },
      { name: 'Manila / La Strada', ticketMedio: 'COP $45k-110k', notes: 'Subzona El Poblado emergente. Aperturas autor + concepto. Alquileres altos pero crecientes.' },
    ],
    marketNotes: 'Medellín capital nómada digital LATAM 2024-2026 (~30k extranjeros residiendo). Boom internacionalización gastronómica. Costes 25-35% menores que Bogotá. Tendencias 2026: trucha andina, café de origen Antioquia, arepas gourmet con masas alternativas, cocina paisa moderna (frijolada deconstructiva), cocina del Pacífico afrocolombiana, mercado coctelería autor con destilados nativos (viche, aguardiente).',
    sources: [
      'INVIMA — Resolución 2674/2013',
      'Cámara de Comercio Medellín para Antioquia',
      'Secretaría de Salud Medellín',
      'ACODRES Antioquia',
    ],
  },

  'buenos-aires': {
    slug: 'buenos-aires', displayName: 'Buenos Aires', country: 'AR', countryName: 'Argentina', currency: 'ARS',
    population: '3.1M Capital Federal (área metro 15M, mayor LATAM)',
    restaurantsCount: '~25.000 establecimientos formales CABA + GBA (AHRCC)',
    cost: {
      totalRange: 'USD $50k - $200k (volátil ARS — usar referencia USD por inflación)',
      obra: 'USD $15k - $55k',
      equipamiento: 'USD $12k - $50k',
      licencias: 'USD $2k - $8k',
      fianzaAlquiler: 'USD $8k - $40k',
      capitalCirculante: 'USD $13k - $47k',
      notes: 'Cifras en USD por inflación ARS persistente. Imports equipamiento muy castigados por aranceles + brecha cambiaria + IVA 21%. Recoleta y Palermo top alquileres; Villa Crespo, Chacarita, Almagro emergentes con costes 40-50% menores. Considera CUIT, AFIP categorización inicial.',
    },
    regulation: {
      framework: 'Código Alimentario Argentino (CAA Ley 18.284) + Habilitación Comercial GCBA + Ley 11.317 manipulación alimentos + Código Edificación CABA + Ley Higiene Alimentaria CABA',
      licenseType: 'Habilitación Comercial GCBA Rubro Restaurante / Bar / Confitería + Inscripción AFIP (monotributo o responsable inscripto) + Curso Manipulador Alimentos ANMAT + Plan Manejo Residuos + Habilitación Bomberos',
      tramitTime: '3-6 meses (Argentina notoria por demoras burocráticas; gestionarla con escribano o gestor agiliza)',
      notes: 'CABA exige Plano Conforme firmado por arquitecto matriculado para habilitación. Régimen impositivo argentino complejo: monotributo (hasta facturación específica) o responsable inscripto (IVA 21% + Ganancias). Brecha cambiaria oficial vs paralelo afecta importaciones.',
    },
    salaries: {
      jefeCocina: 'USD $800 - $2.000/mes (volátil ARS — referencia paralelo a abril 2026)',
      ayudante: 'USD $400 - $700/mes',
      camarero: 'USD $350 - $650/mes + propinas (10% sugerida)',
      source: 'AHRCC Asociación Hoteles Restaurantes Confiterías + Computrabajo Argentina + UTHGRA convenio',
    },
    neighborhoods: [
      { name: 'Palermo Soho / Hollywood', ticketMedio: 'USD $25-60', notes: 'Foodie capital LATAM. Alta densidad restaurantes (densidad real "barrio gastronómico"). Alquileres premium.' },
      { name: 'Recoleta', ticketMedio: 'USD $30-75', notes: 'Premium + turismo gastronómico. Familias clase alta + visitante internacional. Estilo clásico.' },
      { name: 'San Telmo', ticketMedio: 'USD $20-45', notes: 'Histórico, parrilla, tango touristic. Alto flujo turístico fines de semana (Feria San Telmo).' },
      { name: 'Villa Crespo / Chacarita', ticketMedio: 'USD $18-40', notes: 'Emergente, alquileres 40-50% más bajos. Mejor zona aperturas autor con presupuesto ajustado.' },
      { name: 'Puerto Madero', ticketMedio: 'USD $40-90', notes: 'Corporativo + turismo premium. Comida ejecutiva y cenas alta gama. Vista río.' },
    ],
    marketNotes: 'Buenos Aires con escena reconocida internacionalmente: Don Julio (#1 Best 50 Latin), El Preferido, Mishiguene, Tegui. Inflación + brecha cambiaria crean oportunidades para extranjeros con dólares (poder adquisitivo 3-5x sobre local). Parrilla y carne argentina identitarias pero crece neo-cocina argentina con producto local. Tendencias 2026: parrilla autor con cortes alternativos, vino Mendoza/Patagonia pairings, cocina judía-argentina (Mishiguene), bodegones modernos.',
    sources: [
      'AHRCC — Asociación de Hoteles, Restaurantes, Confiterías y Cafés',
      'Código Alimentario Argentino — ANMAT',
      'GCBA — Habilitación Comercial CABA',
      'UTHGRA — Convenio Hostelería Argentina',
    ],
  },

  santiago: {
    slug: 'santiago', displayName: 'Santiago', country: 'CL', countryName: 'Chile', currency: 'CLP',
    population: '5.6M (zona metropolitana 7.1M, ~40% población Chile)',
    restaurantsCount: '~22.000 establecimientos formales (ACHIGA + INE Chile)',
    cost: {
      totalRange: 'CLP $80M - $260M (≈USD $85k-$280k)',
      obra: 'CLP $25M - $80M',
      equipamiento: 'CLP $20M - $60M',
      licencias: 'CLP $3M - $12M',
      fianzaAlquiler: 'CLP $12M - $55M (3-6 meses garantía estándar Chile)',
      capitalCirculante: 'CLP $20M - $55M',
      notes: 'Santiago tiene costes operativos moderados-altos para LATAM (Chile país más caro región). Vitacura / Las Condes premium duplican costes vs Ñuñoa o Providencia interior. Lastarria/Bellas Artes con alto flujo turístico cultural a precio razonable. Importación equipamiento moderada (Chile economía abierta, IVA 19%).',
    },
    regulation: {
      framework: 'Reglamento Sanitario de Alimentos DTO 977/96 + Código Sanitario + SEREMI Salud Metropolitana + Ley General Urbanismo y Construcciones + Ordenanza Local Patente',
      licenseType: 'Resolución Sanitaria SEREMI Salud (Autorización Sanitaria) + Patente Comercial Municipal + Recepción Final DOM (Dirección Obras Municipales) + Patente Alcoholes (si aplica) + Inicio Actividades SII',
      tramitTime: '2-5 meses (Chile ágil dentro de LATAM, digitalización buena)',
      notes: 'Resolución Sanitaria es el cuello de botella: requiere croquis instalaciones firmado, fichas técnicas equipos, capacitación BPM personal. Patente Alcoholes restringida (limitación por densidad zona). Vitacura / Las Condes con normativa propia más estricta que centro Santiago. Inspección sanitaria semestral.',
    },
    salaries: {
      jefeCocina: 'CLP $1.2M - $2.5M/mes brutos (premium Vitacura / Las Condes hasta $3.8M, Boragó $5M+)',
      ayudante: 'CLP $550k - $850k/mes brutos',
      camarero: 'CLP $500k - $800k/mes brutos + propinas (10% legal sugerida)',
      source: 'ACHIGA Asociación Chilena Gastronomía + Trabajando.com + Mintur Chile',
    },
    neighborhoods: [
      { name: 'Vitacura / Las Condes', ticketMedio: 'CLP $25k-70k', notes: 'Premium residencial alto. Comparable Polanco CDMX o Recoleta Madrid. Familias clase alta + corporativo.' },
      { name: 'Providencia / Bellavista', ticketMedio: 'CLP $18k-50k', notes: 'Foodie + cultural + nightlife. Alta densidad restaurantes. Mix turismo + local.' },
      { name: 'Lastarria / Bellas Artes', ticketMedio: 'CLP $20k-55k', notes: 'Cultural-gastronómico (Centro Cultural GAM, Bellas Artes). Alta densidad, ticket medio.' },
      { name: 'Ñuñoa', ticketMedio: 'CLP $15k-40k', notes: 'Residencial creciente, costes moderados. Mejor ratio para concepto local fiel.' },
      { name: 'Barrio Italia', ticketMedio: 'CLP $22k-55k', notes: 'Distrito gastronómico-diseño emergente. Aperturas autor + gastronomía + decoración.' },
    ],
    marketNotes: 'Santiago con escena gastronómica madura: Boragó (Rodolfo Guzmán) #2 Best 50 Latin, Karai, 99, Ambrosía, Demencia. Chile país más caro LATAM pero también con poder adquisitivo más alto (clase media consolidada). Tendencias 2026: cocina chilena contemporánea con productos endémicos (merkén, piñones araucanos, locos, machas, mariscos australes Chiloé), wine pairings DO Maipo/Casablanca/Colchagua, fermentos pre-hispánicos (chicha mapuche), sostenibilidad pesca artesanal.',
    sources: [
      'SEREMI Salud Metropolitana — Reglamento Sanitario',
      'Servicio Impuestos Internos (SII)',
      'ACHIGA — Asociación Chilena de Gastronomía',
      'Sernatur — turismo gastronómico Chile',
    ],
  },
};

export const PSEO_CITY_SLUGS = Object.keys(PSEO_CITIES);
export const PSEO_MODIFIERS: PSeoModifier[] = [
  'abrir-restaurante',
  'licencia-restaurante',
  'software-gestion-restaurante',
  'escandallo-restaurante',
  'plan-negocio-restaurante',
];
