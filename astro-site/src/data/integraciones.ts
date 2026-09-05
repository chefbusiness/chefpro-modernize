// Catálogo de plataformas conectables desde el chat de los agentes (vía Composio).
//
// FUENTE: brief de John (2026-09-05) con la actualización mayor de los agentes.
// Son 16 PLATAFORMAS + Composio, que no es una plataforma más sino el hub que
// gestiona la autorización de todas. Ojo al contarlas en el copy: decir «17
// plataformas» mete a Composio en el saco de las herramientas del usuario, y no
// lo es. En los textos se dice «16 herramientas» y Composio se nombra aparte.
//
// El `icon` es la clave de BrandIcon.astro. El `name` es marca registrada y NO se
// traduce en ningún idioma. Lo único traducible es la etiqueta de la categoría y
// la frase de ejemplo, que viven en los locales i18n (integraciones.*).

export type IntegracionCategoria =
  | 'comunicacion'
  | 'documentos'
  | 'organizacion'
  | 'contenido'
  | 'redes';

export interface Integracion {
  /** Clave de icono en BrandIcon.astro */
  icon: string;
  /** Marca registrada — nunca se traduce */
  name: string;
  categoria: IntegracionCategoria;
  /** Clave i18n de la frase de ejemplo: integraciones.ejemplos.<key> */
  key: string;
}

export const INTEGRACIONES: Integracion[] = [
  { icon: 'gmail', name: 'Gmail', categoria: 'comunicacion', key: 'gmail' },
  { icon: 'outlook', name: 'Outlook', categoria: 'comunicacion', key: 'outlook' },

  { icon: 'googlesheets', name: 'Google Sheets', categoria: 'documentos', key: 'sheets' },
  { icon: 'googledocs', name: 'Google Docs', categoria: 'documentos', key: 'docs' },
  { icon: 'googledrive', name: 'Google Drive', categoria: 'documentos', key: 'drive' },

  { icon: 'googlecalendar', name: 'Google Calendar', categoria: 'organizacion', key: 'calendar' },
  { icon: 'notion', name: 'Notion', categoria: 'organizacion', key: 'notion' },
  { icon: 'google', name: 'Google Super', categoria: 'organizacion', key: 'googlesuper' },

  { icon: 'canva', name: 'Canva', categoria: 'contenido', key: 'canva' },
  { icon: 'wordpress', name: 'WordPress', categoria: 'contenido', key: 'wordpress' },

  { icon: 'instagram', name: 'Instagram', categoria: 'redes', key: 'instagram' },
  { icon: 'facebook', name: 'Facebook', categoria: 'redes', key: 'facebook' },
  { icon: 'linkedin', name: 'LinkedIn', categoria: 'redes', key: 'linkedin' },
  { icon: 'x', name: 'X (Twitter)', categoria: 'redes', key: 'x' },
  { icon: 'tiktok', name: 'TikTok', categoria: 'redes', key: 'tiktok' },
  { icon: 'reddit', name: 'Reddit', categoria: 'redes', key: 'reddit' },
];

/** Número de herramientas del usuario. Composio NO cuenta: es el hub. */
export const TOTAL_INTEGRACIONES = INTEGRACIONES.length; // 16

export const CATEGORIAS: IntegracionCategoria[] = [
  'comunicacion',
  'documentos',
  'organizacion',
  'contenido',
  'redes',
];

export const porCategoria = (c: IntegracionCategoria): Integracion[] =>
  INTEGRACIONES.filter((i) => i.categoria === c);

/** Rutas nativas de la landing por idioma (se usan en Header, Footer y home). */
export const INTEGRACIONES_PATHS: Record<string, string> = {
  es: '/integraciones',
  en: '/en/integrations',
  fr: '/fr/integrations',
  de: '/de/integrationen',
  it: '/it/integrazioni',
  pt: '/pt/integracoes',
  nl: '/nl/integraties',
};

export const integracionesHref = (lang: string): string =>
  INTEGRACIONES_PATHS[lang] ?? INTEGRACIONES_PATHS.es;
