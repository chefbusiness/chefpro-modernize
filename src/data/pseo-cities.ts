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

  // 🟡 partial — estructura completa, datos a refinar Fase A1.5
  barcelona: {
    slug: 'barcelona',
    displayName: 'Barcelona',
    country: 'ES',
    countryName: 'España',
    currency: '€',
    population: '1.6M (área metropolitana 4.9M)',
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
      jefeCocina: '€1.950 - €3.300/mes brutos',
      ayudante: '€1.400 - €1.750/mes brutos',
      camarero: '€1.350 - €1.850/mes brutos + propinas',
      source: 'Conveni Col·lectiu Hostaleria Catalunya',
    },
    neighborhoods: [
      { name: 'Eixample Dret', ticketMedio: '€40-90', notes: 'Premium y media-alta. Alquileres €45-85/m². Alta densidad turística + local.' },
      { name: 'Born / Ribera', ticketMedio: '€35-75', notes: 'Restringido por moratoria PEUAT. Si consigues licencia, ROI alto.' },
      { name: 'Gràcia', ticketMedio: '€25-50', notes: 'Auténtico local + foodies. Buenos alquileres, comunidad fiel.' },
      { name: 'Poblenou', ticketMedio: '€25-55', notes: 'Zona emergente post-22@. Tech workers + lofts. Alquiler 30% menos que centro.' },
      { name: 'Sant Antoni', ticketMedio: '€28-55', notes: 'Renovado tras mercado. Mix locals + turistas. Gastronomía catalana moderna.' },
    ],
    marketNotes: 'Barcelona tiene la moratoria PEUAT activa que restringe nuevas licencias en zonas saturadas — fundamental verificar antes de firmar contrato. Tendencias 2026: sostenibilidad, km 0 catalán, vermut moderno, brunch, cocina mediterránea fusión.',
  },

  // 🔴 stub — pendiente investigación detallada
  valencia: {
    slug: 'valencia', displayName: 'Valencia', country: 'ES', countryName: 'España', currency: '€',
    population: '800k (área metro 1.6M)',
    cost: { totalRange: '€80.000 - €200.000', obra: '€25.000 - €65.000', equipamiento: '€22.000 - €50.000', licencias: '€2.500 - €8.000', fianzaAlquiler: '€10.000 - €36.000', capitalCirculante: '€18.000 - €40.000' },
    regulation: { framework: 'APPCC + Ley Valenciana 14/2010 espectáculos + Ordenanza Municipal Valencia', licenseType: 'Declaración Responsable Ambiental (mayoría) o Licencia Ambiental', tramitTime: '1-2 meses DR — 4-8 meses LA' },
    salaries: { jefeCocina: '€1.700 - €2.700/mes', ayudante: '€1.250 - €1.550/mes', camarero: '€1.200 - €1.600/mes' },
    neighborhoods: [
      { name: 'Ruzafa', ticketMedio: '€25-50', notes: 'Hipster + foodie. Alta concentración locales modernos.' },
      { name: 'El Carmen / Ciutat Vella', ticketMedio: '€30-60', notes: 'Turístico + tradicional.' },
      { name: 'Cabanyal', ticketMedio: '€20-45', notes: 'Frente al mar, gentrificación reciente.' },
    ],
    marketNotes: 'Valencia con boom de aperturas post-COVID. Costes 30-40% menores que Madrid/Barcelona. Tendencias: arroz moderno, paella creativa, brunch mediterráneo.',
  },

  sevilla: {
    slug: 'sevilla', displayName: 'Sevilla', country: 'ES', countryName: 'España', currency: '€',
    population: '690k (área metro 1.5M)',
    cost: { totalRange: '€70.000 - €180.000', obra: '€22.000 - €58.000', equipamiento: '€20.000 - €45.000', licencias: '€2.500 - €7.500', fianzaAlquiler: '€8.000 - €30.000', capitalCirculante: '€15.000 - €38.000' },
    regulation: { framework: 'APPCC + Ley Andaluza 13/1999 espectáculos + Ordenanza Sevilla', licenseType: 'Declaración Responsable o Licencia Ambiental Unificada (autonomía andaluza)', tramitTime: '1-3 meses DR — 6-10 meses LAU' },
    salaries: { jefeCocina: '€1.600 - €2.500/mes', ayudante: '€1.200 - €1.500/mes', camarero: '€1.150 - €1.500/mes + propinas' },
    neighborhoods: [
      { name: 'Triana', ticketMedio: '€20-45', notes: 'Identitario sevillano. Alquileres moderados, alto flujo.' },
      { name: 'Alfalfa / Alameda', ticketMedio: '€25-50', notes: 'Centro turístico + nightlife.' },
      { name: 'Los Remedios', ticketMedio: '€30-60', notes: 'Residencial alto. Restaurantes familiares premium.' },
    ],
    marketNotes: 'Sevilla con fuerte componente turístico (~3M visitantes/año). Tapeo es eje. Costes muy bajos vs Madrid. Tendencias: tapas creativas, fusión andaluza-internacional.',
  },

  malaga: {
    slug: 'malaga', displayName: 'Málaga', country: 'ES', countryName: 'España', currency: '€',
    population: '580k (Costa del Sol >1.7M)',
    cost: { totalRange: '€80.000 - €220.000', obra: '€25.000 - €70.000', equipamiento: '€22.000 - €52.000', licencias: '€3.000 - €9.000', fianzaAlquiler: '€10.000 - €40.000', capitalCirculante: '€18.000 - €45.000' },
    regulation: { framework: 'APPCC + Ley Andaluza 13/1999 + Ordenanza Málaga', licenseType: 'Declaración Responsable / LAU', tramitTime: '1-3 meses DR — 6-10 meses LAU' },
    salaries: { jefeCocina: '€1.700 - €2.800/mes (premium temporada alta)', ayudante: '€1.250 - €1.600/mes', camarero: '€1.200 - €1.700/mes + propinas turísticas' },
    neighborhoods: [
      { name: 'Soho / Centro Histórico', ticketMedio: '€30-65', notes: 'Galerías + foodie. Pujante.' },
      { name: 'Pedregalejo / El Palo', ticketMedio: '€25-50', notes: 'Marisco + chiringuitos premium.' },
      { name: 'Marbella centro', ticketMedio: '€60-150', notes: 'Alta gama, target internacional.' },
    ],
    marketNotes: 'Málaga + Costa del Sol = mercado dual: residente local + turismo internacional alto poder adquisitivo. Boom inmobiliario impacta alquileres hostelería 2024-2026.',
  },

  bilbao: {
    slug: 'bilbao', displayName: 'Bilbao', country: 'ES', countryName: 'España', currency: '€',
    population: '345k (Bizkaia 1.1M)',
    cost: { totalRange: '€85.000 - €210.000', obra: '€28.000 - €68.000', equipamiento: '€24.000 - €55.000', licencias: '€3.500 - €10.000', fianzaAlquiler: '€10.000 - €38.000', capitalCirculante: '€18.000 - €42.000' },
    regulation: { framework: 'APPCC + Ley Vasca 4/1995 espectáculos + Ordenanza Bilbao', licenseType: 'Comunicación Previa o Licencia Actividad', tramitTime: '1-3 meses CP — 5-9 meses LA' },
    salaries: { jefeCocina: '€2.000 - €3.300/mes (mercado vasco premium)', ayudante: '€1.450 - €1.800/mes', camarero: '€1.400 - €1.900/mes' },
    neighborhoods: [
      { name: 'Casco Viejo', ticketMedio: '€25-55', notes: 'Pintxos + tradicional. Muy turístico.' },
      { name: 'Indautxu / Abando', ticketMedio: '€35-75', notes: 'Premium + residencial.' },
      { name: 'Bilbao La Vieja', ticketMedio: '€20-45', notes: 'Emergente, gentrificación.' },
    ],
    marketNotes: 'Bilbao referente gastronómico mundial (Asador Etxebarri, Guggenheim effect). Salarios 15-20% mayores que media española. Pintxo es identitario. Tendencias: alta cocina vasca de producto.',
  },

  zaragoza: {
    slug: 'zaragoza', displayName: 'Zaragoza', country: 'ES', countryName: 'España', currency: '€',
    population: '680k',
    cost: { totalRange: '€65.000 - €165.000', obra: '€20.000 - €52.000', equipamiento: '€18.000 - €42.000', licencias: '€2.500 - €7.500', fianzaAlquiler: '€7.000 - €28.000', capitalCirculante: '€14.000 - €35.000' },
    regulation: { framework: 'APPCC + Ley Aragonesa 11/2005 espectáculos + Ordenanza Zaragoza', licenseType: 'Comunicación Previa o Licencia Ambiental', tramitTime: '1-3 meses CP — 5-9 meses LA' },
    salaries: { jefeCocina: '€1.600 - €2.500/mes', ayudante: '€1.200 - €1.500/mes', camarero: '€1.150 - €1.550/mes' },
    neighborhoods: [
      { name: 'Casco Histórico', ticketMedio: '€25-50' },
      { name: 'Centro / Independencia', ticketMedio: '€30-60' },
      { name: 'Universidad', ticketMedio: '€18-35' },
    ],
    marketNotes: 'Zaragoza con costes 35-45% menores que Madrid. Mercado consolidado, baja rotación. Tendencias: tapa moderna, ternasco, productos km 0 aragoneses.',
  },

  'ciudad-de-mexico': {
    slug: 'ciudad-de-mexico', displayName: 'Ciudad de México', country: 'MX', countryName: 'México', currency: 'MXN',
    population: '9.2M (zona metropolitana 22M)',
    restaurantsCount: '~50.000 establecimientos formales + ~120.000 informales',
    cost: { totalRange: 'MXN $1.5M - $5M (≈USD $80k-$280k)', obra: 'MXN $400k - $1.5M', equipamiento: 'MXN $350k - $1.2M', licencias: 'MXN $80k - $250k', fianzaAlquiler: 'MXN $250k - $1M (3-6 meses)', capitalCirculante: 'MXN $400k - $1.2M' },
    regulation: { framework: 'NOM-251-SSA1-2009 (prácticas higiene alimentos) + NOM-093-SSA1-1994 + COFEPRIS + Reglamento Establecimientos Mercantiles CDMX', licenseType: 'Aviso de Funcionamiento COFEPRIS + Licencia Establecimiento Mercantil + Programa Interno Protección Civil', tramitTime: '2-6 meses (depende alcaldía y giro)' },
    salaries: { jefeCocina: 'MXN $25.000 - $55.000/mes brutos (premium Polanco/Roma puede llegar $80k)', ayudante: 'MXN $9.000 - $14.000/mes', camarero: 'MXN $8.000 - $13.000/mes + propinas (10-15%)' },
    neighborhoods: [
      { name: 'Polanco', ticketMedio: '$650-1.800 MXN', notes: 'Top gama. Alquileres premium. Target alto poder adquisitivo.' },
      { name: 'Roma Norte / Condesa', ticketMedio: '$350-900 MXN', notes: 'Foodie + millennials. Boom de aperturas autor.' },
      { name: 'Coyoacán / San Ángel', ticketMedio: '$300-700 MXN', notes: 'Tradicional con toque cultural.' },
      { name: 'Juárez / Cuauhtémoc', ticketMedio: '$300-800 MXN', notes: 'Renovación urbana. Mezcalerías + cocina autor.' },
    ],
    marketNotes: 'CDMX es el mercado gastronómico líder de LATAM. World\'s 50 Best ranking activo. Tendencias 2026: revalorización cocina mexicana de origen, mezcal, omakase mexicano, sostenibilidad. Mercado muy competitivo en zonas premium.',
  },

  guadalajara: {
    slug: 'guadalajara', displayName: 'Guadalajara', country: 'MX', countryName: 'México', currency: 'MXN',
    population: '1.5M (zona metropolitana 5M)',
    cost: { totalRange: 'MXN $900k - $3M', obra: 'MXN $250k - $900k', equipamiento: 'MXN $250k - $850k', licencias: 'MXN $50k - $180k', fianzaAlquiler: 'MXN $150k - $600k', capitalCirculante: 'MXN $250k - $700k' },
    regulation: { framework: 'NOM-251-SSA1-2009 + COFEPRIS + Reglamento Municipal Guadalajara', licenseType: 'Licencia Municipal Giro Restaurantero + Aviso COFEPRIS', tramitTime: '1-4 meses' },
    salaries: { jefeCocina: 'MXN $20.000 - $42.000/mes', ayudante: 'MXN $7.500 - $12.000/mes', camarero: 'MXN $7.000 - $11.000/mes + propinas' },
    neighborhoods: [
      { name: 'Providencia / Chapalita', ticketMedio: '$300-800 MXN', notes: 'Premium residencial.' },
      { name: 'Lafayette / Americana', ticketMedio: '$350-900 MXN', notes: 'Foodie + restaurantes de autor.' },
      { name: 'Centro Histórico', ticketMedio: '$200-500 MXN', notes: 'Tradicional + turístico.' },
    ],
    marketNotes: 'Guadalajara cuna del tequila y birria. Costes 30-40% menores que CDMX. Mercado en expansión, menos saturado. Tendencias: birria moderna, tequila pairings, cocina tapatía contemporánea.',
  },

  monterrey: {
    slug: 'monterrey', displayName: 'Monterrey', country: 'MX', countryName: 'México', currency: 'MXN',
    population: '1.1M (zona metropolitana 5.3M)',
    cost: { totalRange: 'MXN $1.2M - $4M', obra: 'MXN $300k - $1.1M', equipamiento: 'MXN $300k - $1M', licencias: 'MXN $60k - $200k', fianzaAlquiler: 'MXN $200k - $800k', capitalCirculante: 'MXN $300k - $900k' },
    regulation: { framework: 'NOM-251-SSA1-2009 + COFEPRIS + Reglamento Monterrey + NOM Nuevo León', licenseType: 'Licencia Municipal Restaurante + Aviso COFEPRIS', tramitTime: '1-4 meses (Monterrey ágil)' },
    salaries: { jefeCocina: 'MXN $24.000 - $48.000/mes (premium San Pedro hasta $70k)', ayudante: 'MXN $9.000 - $13.500/mes', camarero: 'MXN $8.500 - $12.500/mes + propinas' },
    neighborhoods: [
      { name: 'San Pedro Garza García', ticketMedio: '$500-1.500 MXN', notes: 'Municipio más rico LATAM. Alta gama.' },
      { name: 'Valle Oriente / Carretera Nacional', ticketMedio: '$400-1.000 MXN', notes: 'Corporativo + residencial alto.' },
      { name: 'Barrio Antiguo', ticketMedio: '$300-700 MXN', notes: 'Histórico renovado, foodie.' },
    ],
    marketNotes: 'Monterrey con poder adquisitivo más alto de México (PIB per cápita similar a España). Cabrito, machaca, cortes premium. Boom steakhouses alta gama y franquicias internacionales.',
  },

  queretaro: {
    slug: 'queretaro', displayName: 'Querétaro', country: 'MX', countryName: 'México', currency: 'MXN',
    population: '900k (zona metropolitana 1.6M)',
    cost: { totalRange: 'MXN $700k - $2.2M', obra: 'MXN $200k - $700k', equipamiento: 'MXN $200k - $600k', licencias: 'MXN $40k - $130k', fianzaAlquiler: 'MXN $100k - $400k', capitalCirculante: 'MXN $200k - $500k' },
    regulation: { framework: 'NOM-251 + COFEPRIS + Reglamento Querétaro', licenseType: 'Licencia Funcionamiento Municipal + Aviso COFEPRIS', tramitTime: '1-3 meses' },
    salaries: { jefeCocina: 'MXN $20.000 - $38.000/mes', ayudante: 'MXN $7.500 - $11.500/mes', camarero: 'MXN $7.000 - $10.500/mes + propinas' },
    neighborhoods: [
      { name: 'Centro Histórico (UNESCO)', ticketMedio: '$300-800 MXN', notes: 'Patrimonio + turismo cultural.' },
      { name: 'Juriquilla', ticketMedio: '$300-700 MXN', notes: 'Residencial alto, expats tech.' },
      { name: 'Milenio III / Antea', ticketMedio: '$250-600 MXN', notes: 'Comercial moderno.' },
    ],
    marketNotes: 'Querétaro ciudad de mayor crecimiento económico México (clúster aeroespacial + tech). Migración nacional alta, demanda creciente. Vinos Valle Tequisquiapan emergente. Costes muy competitivos.',
  },

  bogota: {
    slug: 'bogota', displayName: 'Bogotá', country: 'CO', countryName: 'Colombia', currency: 'COP',
    population: '8M (área metro 11M)',
    restaurantsCount: '~32.000 establecimientos formales',
    cost: { totalRange: 'COP $300M - $1.200M (≈USD $75k-$300k)', obra: 'COP $80M - $300M', equipamiento: 'COP $80M - $250M', licencias: 'COP $15M - $60M', fianzaAlquiler: 'COP $40M - $200M', capitalCirculante: 'COP $80M - $250M' },
    regulation: { framework: 'Resolución 2674 de 2013 INVIMA (BPM alimentos) + Decreto 3075/97 + Reglamento Distrital Bogotá', licenseType: 'Concepto Sanitario Favorable Secretaría Salud + Registro Mercantil Cámara Comercio + Concepto Bomberos + Sayco-Acinpro (música)', tramitTime: '2-5 meses (gestión paralela)' },
    salaries: { jefeCocina: 'COP $4.5M - $9M/mes brutos (premium Zona G/T hasta $14M)', ayudante: 'COP $1.5M - $2.4M/mes', camarero: 'COP $1.4M - $2.2M/mes + propinas (10%)' },
    neighborhoods: [
      { name: 'Zona G (Quinta Camacho)', ticketMedio: 'COP $80k-180k', notes: 'Gourmet by definition. Alta gama.' },
      { name: 'Zona T / Parque 93', ticketMedio: 'COP $60k-150k', notes: 'Comercial + nightlife premium.' },
      { name: 'Usaquén', ticketMedio: 'COP $50k-120k', notes: 'Histórico + mercado pulgas. Casual premium.' },
      { name: 'Chapinero Alto / La Macarena', ticketMedio: 'COP $40k-95k', notes: 'Foodie + autor. Alquileres más bajos.' },
    ],
    marketNotes: 'Bogotá con escena gastronómica explosiva (Leo, Mini-Mal, Sumá). World\'s 50 Best Latam crece. Tendencias 2026: cocina colombiana contemporánea, ingredientes endémicos amazónicos, mezcla africana-andina, sostenibilidad agropecuaria.',
  },

  medellin: {
    slug: 'medellin', displayName: 'Medellín', country: 'CO', countryName: 'Colombia', currency: 'COP',
    population: '2.5M (área metro 4M)',
    cost: { totalRange: 'COP $200M - $800M', obra: 'COP $50M - $200M', equipamiento: 'COP $60M - $180M', licencias: 'COP $10M - $40M', fianzaAlquiler: 'COP $25M - $130M', capitalCirculante: 'COP $55M - $170M' },
    regulation: { framework: 'Resolución 2674 INVIMA + Reglamento Medellín', licenseType: 'Concepto Sanitario + Registro Cámara Comercio Medellín + Concepto Bomberos', tramitTime: '2-4 meses' },
    salaries: { jefeCocina: 'COP $4M - $7.5M/mes', ayudante: 'COP $1.4M - $2.2M/mes', camarero: 'COP $1.3M - $2M/mes + propinas' },
    neighborhoods: [
      { name: 'El Poblado / Provenza', ticketMedio: 'COP $50k-130k', notes: 'Foodie boom + nómadas digitales. Mejor punto comercial Colombia.' },
      { name: 'Laureles', ticketMedio: 'COP $35k-85k', notes: 'Local + creciente internacional.' },
      { name: 'Envigado', ticketMedio: 'COP $30k-75k', notes: 'Tradicional paisa, residencial.' },
    ],
    marketNotes: 'Medellín capital nómada digital LATAM 2024-2026. Boom internacionalización gastronómica. Costes 25-35% menores que Bogotá. Tendencias: trucha, café de origen, arepas gourmet, cocina paisa moderna.',
  },

  'buenos-aires': {
    slug: 'buenos-aires', displayName: 'Buenos Aires', country: 'AR', countryName: 'Argentina', currency: 'ARS',
    population: '3.1M (área metro 15M)',
    cost: { totalRange: 'USD $50k - $200k (volátil ARS)', obra: 'USD $15k - $55k', equipamiento: 'USD $12k - $50k', licencias: 'USD $2k - $8k', fianzaAlquiler: 'USD $8k - $40k', capitalCirculante: 'USD $13k - $47k', notes: 'Cifras en USD por inflación ARS. Imports equipamiento muy castigados por aranceles + tipo cambio.' },
    regulation: { framework: 'Código Alimentario Argentino + Habilitación Comercial GCBA + Ley 11.317 manipuladores', licenseType: 'Habilitación Comercial GCBA rubro Restaurante + Inscripción AFIP + ANMAT manipuladores', tramitTime: '3-6 meses (Argentina notoria por demoras burocráticas)' },
    salaries: { jefeCocina: 'USD $800 - $2.000/mes (volátil ARS)', ayudante: 'USD $400 - $700/mes', camarero: 'USD $350 - $650/mes + propinas (10%)' },
    neighborhoods: [
      { name: 'Palermo Soho / Hollywood', ticketMedio: 'USD $25-60', notes: 'Foodie capital LATAM. Alta densidad restaurantes.' },
      { name: 'Recoleta', ticketMedio: 'USD $30-75', notes: 'Premium + turismo gastronómico.' },
      { name: 'San Telmo', ticketMedio: 'USD $20-45', notes: 'Histórico, parrilla, tango touristic.' },
      { name: 'Villa Crespo / Chacarita', ticketMedio: 'USD $18-40', notes: 'Emergente, alquileres más bajos.' },
    ],
    marketNotes: 'Buenos Aires con escena reconocida internacionalmente (Don Julio, El Preferido). Inflación + tipo cambio crean oportunidades para extranjeros con USD. Parrilla es identitaria pero crece neo-cocina argentina.',
  },

  santiago: {
    slug: 'santiago', displayName: 'Santiago', country: 'CL', countryName: 'Chile', currency: 'CLP',
    population: '5.6M (zona metropolitana 7.1M)',
    cost: { totalRange: 'CLP $80M - $260M (≈USD $85k-$280k)', obra: 'CLP $25M - $80M', equipamiento: 'CLP $20M - $60M', licencias: 'CLP $3M - $12M', fianzaAlquiler: 'CLP $12M - $55M', capitalCirculante: 'CLP $20M - $55M' },
    regulation: { framework: 'Reglamento Sanitario Alimentos DTO 977/96 + SEREMI Salud + Patente Municipal', licenseType: 'Resolución Sanitaria SEREMI Salud + Patente Comercial Municipal + Recepción Final DOM', tramitTime: '2-5 meses' },
    salaries: { jefeCocina: 'CLP $1.2M - $2.5M/mes brutos', ayudante: 'CLP $550k - $850k/mes', camarero: 'CLP $500k - $800k/mes + propinas (10%)' },
    neighborhoods: [
      { name: 'Vitacura / Las Condes', ticketMedio: 'CLP $25k-70k', notes: 'Premium residencial alto.' },
      { name: 'Providencia / Bellavista', ticketMedio: 'CLP $18k-50k', notes: 'Foodie + cultural.' },
      { name: 'Lastarria / Bellas Artes', ticketMedio: 'CLP $20k-55k', notes: 'Cultural-gastronómico, alta densidad.' },
      { name: 'Ñuñoa', ticketMedio: 'CLP $15k-40k', notes: 'Residencial creciente, costes moderados.' },
    ],
    marketNotes: 'Santiago con escena gastronómica madura, World\'s 50 Best activo (Boragó). Tendencias: cocina chilena contemporánea, productos endémicos (merkén, piñones, mariscos australes), wine pairings.',
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
