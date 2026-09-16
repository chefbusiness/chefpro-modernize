/**
 * Banderas del selector de idioma como SVG en línea (compartido por
 * astro-site/src/components/Header.astro y src/components/ModernHeader.tsx).
 *
 * Por qué SVG y no emoji: Windows no trae glifos de bandera, así que en Chrome
 * o Edge sobre Windows 🇪🇸 se pinta como las letras «ES» sueltas. Un SVG se ve
 * igual en cualquier sistema y navegador.
 *
 * Diseño simplificado a propósito (se pintan a ~20×14 px): sin escudos ni
 * estrellas, que a ese tamaño son ruido. El contenedor recorta con `slice`,
 * así que todas ocupan la misma caja aunque sus proporciones reales difieran.
 *
 * `en` es la de EE. UU. por continuidad con el selector anterior.
 * Sin clases de Tailwind aquí: este fichero no entra en el scan de astro-site.
 */
export type FlagLang = 'es' | 'en' | 'fr' | 'de' | 'it' | 'pt' | 'nl';

const svg = (viewBox: string, body: string) =>
  `<svg xmlns="http://www.w3.org/2000/svg" viewBox="${viewBox}" width="100%" height="100%" preserveAspectRatio="xMidYMid slice" aria-hidden="true" focusable="false">${body}</svg>`;

const usStripes = Array.from({ length: 6 }, (_, i) => `<rect y="${300 + i * 600}" width="7410" height="300" fill="#fff"/>`).join('');

export const FLAG_SVG: Record<FlagLang, string> = {
  es: svg('0 0 750 500', '<rect width="750" height="500" fill="#AA151B"/><rect y="125" width="750" height="250" fill="#F1BF00"/>'),
  en: svg('0 0 7410 3900', `<rect width="7410" height="3900" fill="#B22234"/>${usStripes}<rect width="2964" height="2100" fill="#3C3B6E"/>`),
  fr: svg('0 0 900 600', '<rect width="300" height="600" fill="#0055A4"/><rect x="300" width="300" height="600" fill="#fff"/><rect x="600" width="300" height="600" fill="#EF4135"/>'),
  de: svg('0 0 500 300', '<rect width="500" height="100" fill="#000"/><rect y="100" width="500" height="100" fill="#DD0000"/><rect y="200" width="500" height="100" fill="#FFCE00"/>'),
  it: svg('0 0 900 600', '<rect width="300" height="600" fill="#009246"/><rect x="300" width="300" height="600" fill="#fff"/><rect x="600" width="300" height="600" fill="#CE2B37"/>'),
  pt: svg('0 0 600 400', '<rect width="240" height="400" fill="#006600"/><rect x="240" width="360" height="400" fill="#FF0000"/><circle cx="240" cy="200" r="80" fill="#FFCC00"/><rect x="205" y="160" width="70" height="80" rx="10" fill="#fff"/><rect x="215" y="170" width="50" height="60" rx="6" fill="#FF0000"/>'),
  nl: svg('0 0 900 600', '<rect width="900" height="200" fill="#AE1C28"/><rect y="200" width="900" height="200" fill="#fff"/><rect y="400" width="900" height="200" fill="#21468B"/>'),
};
