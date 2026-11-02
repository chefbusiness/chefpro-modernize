import { useState } from 'react';
import { useTranslation } from 'react-i18next';
import { Helmet } from 'react-helmet-async';
import { Link } from 'react-router-dom';
import jsPDF from 'jspdf';
import ModernHeader from '@/components/ModernHeader';
import ModernFooter from '@/components/ModernFooter';
import { Button } from '@/components/ui/button';
import { Badge } from '@/components/ui/badge';
import { useLanguage } from '@/hooks/useLanguage';
import { FileText, Copy, CheckCircle, RotateCcw, ArrowRight, Sparkles, FileDown } from 'lucide-react';
import HeroSocialProof from '@/components/HeroSocialProof';
import OtherFreeTools from '@/components/OtherFreeTools';
import PricingPlans from '@/components/PricingPlans';

const LANG_SLUGS: Record<string, string> = {
  es: '/generador-textos-carta-restaurante',
  en: '/en/restaurant-menu-copy-generator',
  fr: '/fr/generateur-textes-carte-restaurant',
  de: '/de/speisekarten-text-generator',
  it: '/it/generatore-testi-menu-ristorante',
  pt: '/pt/gerador-textos-cardapio-restaurante',
  nl: '/nl/menukaart-tekst-generator',
};

const HUB_SLUGS: Record<string, string> = {
  es: '/herramientas-gratuitas',
  en: '/en/free-tools-restaurants',
  fr: '/fr/outils-gratuits-restaurant',
  de: '/de/kostenlose-tools-restaurant',
  it: '/it/strumenti-gratuiti-ristorante',
  pt: '/pt/ferramentas-gratuitas-restaurante',
  nl: '/nl/gratis-tools-restaurant',
};

// ─── Template engine ────────────────────────────────────────────────────────

function strHash(str: string): number {
  let h = 0;
  for (let i = 0; i < str.length; i++) {
    h = (Math.imul(31, h) + str.charCodeAt(i)) | 0;
  }
  return Math.abs(h);
}

function pickFrom<T>(arr: T[], seed: number): T {
  return arr[seed % arr.length];
}

function parseIngredients(raw: string): string[] {
  return raw
    .split(/[,;\n]+/)
    .map(s => s.trim().toLowerCase())
    .filter(Boolean)
    .slice(0, 5);
}

// ─── Spanish templates ───────────────────────────────────────────────────────

const CLASICA_ES = [
  (name: string, ing1: string, ing2: string, styleAdj: string) =>
    `${capitalize(name)} elaborado con ${ing1} y ${ing2}, siguiendo una preparación ${styleAdj}. Textura equilibrada y sabor que no defrauda.`,
  (name: string, ing1: string, ing2: string, styleAdj: string) =>
    `Nuestra versión ${styleAdj} de ${name}: ${ing1} seleccionado y ${ing2} de primera calidad. Un clásico que habla por sí solo.`,
  (name: string, ing1: string, ing2: string, styleAdj: string) =>
    `${capitalize(name)} de elaboración ${styleAdj} con ${ing1} y ${ing2}. Ingredientes cuidados, resultado impecable.`,
  (name: string, ing1: string, _ing2: string, styleAdj: string) =>
    `Preparación ${styleAdj} de ${name} a base de ${ing1}. Equilibrio de sabores y presentación cuidada al detalle.`,
];

const EMOCIONAL_ES = [
  (name: string, ing1: string, sensory: string) =>
    `El primer bocado de este ${name} lo dice todo: ${ing1} ${sensory}, con ese sabor que te transporta a un buen momento.`,
  (name: string, ing1: string, sensory: string) =>
    `Hay platos que no necesitan explicación. Este ${name} con ${ing1} ${sensory} es uno de ellos. Cierra los ojos y disfruta.`,
  (name: string, ing1: string, sensory: string) =>
    `Sabores que cuentan historias. El ${ing1} ${sensory} de este ${name} crea el recuerdo que buscas en cada visita.`,
  (name: string, ing1: string, sensory: string) =>
    `Como debería ser siempre: ${name} con ${ing1} ${sensory} y ese punto exacto que lo convierte en imprescindible.`,
];

const KM0_ES = [
  (name: string, ing1: string) =>
    `${capitalize(name)} elaborado con ${ing1} de productores de proximidad. Temporada respetada, kilómetro cero de verdad.`,
  (name: string, ing1: string) =>
    `Del campo a tu mesa: ${name} con ${ing1} de origen local y trazabilidad garantizada. Sabor genuino, territorio honesto.`,
  (name: string, ing1: string) =>
    `${capitalize(ing1)} de temporada para un ${name} que respeta el entorno. Producto cercano, sabor auténtico.`,
  (name: string, ing1: string) =>
    `${capitalize(name)} de km0: ${ing1} procedente de proveedores locales de confianza. Porque el mejor ingrediente es el más cercano.`,
];

const NOMBRE_ALT_ES = [
  (ing1: string, tipo: string) => `${capitalize(ing1)} ${tipo} del Chef`,
  (ing1: string, tipo: string) => `${capitalize(tipo)} de ${capitalize(ing1)}`,
  (ing1: string, tipo: string) => `${capitalize(ing1)} al Momento`,
  (ing1: string, tipo: string) => `${capitalize(tipo)} Fundente de ${capitalize(ing1)}`,
  (ing1: string, tipo: string) => `Selección de ${capitalize(ing1)} ${capitalize(tipo)}`,
];

const RAZON_ALT_ES = [
  'Un nombre más evocador que conecta con el ingrediente principal.',
  'Transmite artesanía y producto de calidad desde el primer vistazo.',
  'Más memorable y diferenciador en una carta con platos similares.',
  'Añade valor percibido y despierta la curiosidad del comensal.',
];

const STYLE_ADJ_ES: Record<number, string[]> = {
  0: ['tradicional', 'artesanal', 'de siempre', 'casera'],
  1: ['de vanguardia', 'de autor', 'innovadora', 'técnica'],
  2: ['informal', 'desenfadada', 'sin pretensiones', 'directa'],
  3: ['gourmet', 'de alta cocina', 'premium', 'exquisita'],
  4: ['familiar', 'reconfortante', 'generosa', 'de hogar'],
};

const SENSORY_ES = [
  'crujiente y dorado', 'cremoso y fundente', 'tostado y aromático',
  'suave y delicado', 'intenso y sabroso', 'jugoso y tierno',
  'ahumado y profundo', 'fresco y ligero',
];

// ─── English templates ───────────────────────────────────────────────────────

const CLASICA_EN = [
  (name: string, ing1: string, ing2: string, styleAdj: string) =>
    `${capitalize(name)} crafted with ${ing1} and ${ing2}, prepared in a ${styleAdj} style. Balanced flavors and a finish that never disappoints.`,
  (name: string, ing1: string, ing2: string, styleAdj: string) =>
    `Our ${styleAdj} take on ${name}: carefully selected ${ing1} and quality ${ing2}. A classic that speaks for itself.`,
  (name: string, ing1: string, _ing2: string, styleAdj: string) =>
    `${capitalize(name)} — ${styleAdj} preparation with premium ${ing1}. Precise technique, impeccable result.`,
];

const EMOCIONAL_EN = [
  (name: string, ing1: string, sensory: string) =>
    `One bite of this ${name} says it all: ${sensory} ${ing1} that takes you somewhere special. Comfort food at its finest.`,
  (name: string, ing1: string, sensory: string) =>
    `Some dishes need no introduction. This ${name} with ${sensory} ${ing1} is one of them. Just close your eyes and enjoy.`,
  (name: string, ing1: string, sensory: string) =>
    `Flavors that tell stories. The ${sensory} ${ing1} in this ${name} creates the memory your guests keep coming back for.`,
];

const KM0_EN = [
  (name: string, ing1: string) =>
    `${capitalize(name)} made with locally sourced ${ing1}. Seasonal, traceable, and genuinely km0.`,
  (name: string, ing1: string) =>
    `Farm to table: ${name} with ${ing1} from trusted local producers. Real flavor, honest territory.`,
  (name: string, ing1: string) =>
    `Seasonal ${ing1} for a ${name} that respects its surroundings. Local product, authentic taste.`,
];

const STYLE_ADJ_EN: Record<number, string[]> = {
  0: ['traditional', 'classic', 'time-honored', 'artisan'],
  1: ['avant-garde', 'signature', 'innovative', 'creative'],
  2: ['casual', 'relaxed', 'no-frills', 'laid-back'],
  3: ['gourmet', 'fine dining', 'premium', 'refined'],
  4: ['home-style', 'comforting', 'generous', 'family-inspired'],
};

const SENSORY_EN = [
  'crispy and golden', 'creamy and melt-in-your-mouth', 'smoky and aromatic',
  'light and delicate', 'bold and flavorful', 'juicy and tender',
  'fresh and bright', 'rich and indulgent',
];

const NOMBRE_ALT_EN = [
  (ing1: string, tipo: string) => `Chef's ${capitalize(ing1)} ${capitalize(tipo)}`,
  (ing1: string, tipo: string) => `${capitalize(tipo)} of ${capitalize(ing1)}`,
  (ing1: string, tipo: string) => `Pan-${capitalize(ing1)} ${capitalize(tipo)}`,
  (ing1: string, tipo: string) => `House ${capitalize(tipo)} with ${capitalize(ing1)}`,
];

// ─── Helpers ─────────────────────────────────────────────────────────────────

function capitalize(s: string): string {
  return s.charAt(0).toUpperCase() + s.slice(1);
}

function extractDishType(name: string): string {
  const common = [
    'croquetas', 'ensalada', 'sopa', 'crema', 'pasta', 'arroz', 'paella',
    'filete', 'lomo', 'pechuga', 'lubina', 'salmón', 'bacalao', 'pulpo',
    'tarta', 'coulant', 'brownie', 'flan', 'tiramisú',
    'burger', 'sandwich', 'bocadillo', 'pizza', 'risotto',
  ];
  const lower = name.toLowerCase();
  return common.find(w => lower.includes(w)) || lower.split(' ')[0];
}

// ─── Core generation function ─────────────────────────────────────────────────

interface MenuCopyResult {
  clasica: string;
  emocional: string;
  km0: string;
  nombreAlternativo: string;
  razonNombre: string;
}

function generateMenuCopy(
  nombre: string,
  ingredientes: string,
  estiloIdx: number,
  idiomaIdx: number
): MenuCopyResult {
  const seed = strHash(nombre + ingredientes + estiloIdx + idiomaIdx);
  const ings = parseIngredients(ingredientes);
  const ing1 = ings[0] || nombre.toLowerCase();
  const ing2 = ings[1] || ings[0] || 'ingredientes seleccionados';
  const tipo = extractDishType(nombre);

  if (idiomaIdx === 1) {
    // English
    const styleAdj = pickFrom(STYLE_ADJ_EN[estiloIdx] || STYLE_ADJ_EN[0], seed);
    const sensory = pickFrom(SENSORY_EN, seed + 7);
    return {
      clasica: pickFrom(CLASICA_EN, seed + 1)(nombre.toLowerCase(), ing1, ing2, styleAdj),
      emocional: pickFrom(EMOCIONAL_EN, seed + 2)(nombre.toLowerCase(), ing1, sensory),
      km0: pickFrom(KM0_EN, seed + 3)(nombre.toLowerCase(), ing1),
      nombreAlternativo: pickFrom(NOMBRE_ALT_EN, seed + 4)(ing1, tipo),
      razonNombre: 'A more evocative name that highlights the main ingredient and adds perceived value.',
    };
  }

  // Spanish (default — also used for Catalán/Euskera with note)
  const styleAdj = pickFrom(STYLE_ADJ_ES[estiloIdx] || STYLE_ADJ_ES[0], seed);
  const sensory = pickFrom(SENSORY_ES, seed + 7);
  return {
    clasica: pickFrom(CLASICA_ES, seed + 1)(nombre.toLowerCase(), ing1, ing2, styleAdj),
    emocional: pickFrom(EMOCIONAL_ES, seed + 2)(nombre.toLowerCase(), ing1, sensory),
    km0: pickFrom(KM0_ES, seed + 3)(nombre.toLowerCase(), ing1),
    nombreAlternativo: pickFrom(NOMBRE_ALT_ES, seed + 4)(ing1, tipo),
    razonNombre: pickFrom(RAZON_ALT_ES, seed + 5),
  };
}

// ─── Component ────────────────────────────────────────────────────────────────

export default function GeneradorTextosCarta() {
  const { t, i18n } = useTranslation();
  const { currentLanguage, getAppUrl } = useLanguage();
  const siteUrl = import.meta.env.VITE_SITE_URL || 'https://aichef.pro';
  const slug = LANG_SLUGS[currentLanguage] || LANG_SLUGS.es;
  const canonicalUrl = `${siteUrl}${slug}`;

  const seo = t('toolMenuCopy.seo', { returnObjects: true }) as any;
  const hero = t('toolMenuCopy.hero', { returnObjects: true }) as any;
  const tool = t('toolMenuCopy.tool', { returnObjects: true }) as any;
  const faqItems: Array<{ q: string; a: string }> = t('toolMenuCopy.faq', { returnObjects: true }) as any;
  const ctaSection = t('toolMenuCopy.cta_section', { returnObjects: true }) as any;

  const faqSchema = Array.isArray(faqItems) && faqItems.length > 0
    ? {
        '@context': 'https://schema.org',
        '@type': 'FAQPage',
        mainEntity: faqItems.map(f => ({
          '@type': 'Question',
          name: f.q,
          acceptedAnswer: { '@type': 'Answer', text: f.a },
        })),
      }
    : null;

  const estilos: string[] = Array.isArray(tool?.estilos) ? tool.estilos : [];
  const idiomas: string[] = Array.isArray(tool?.idiomas) ? tool.idiomas : [];
  const resultLabels = tool?.result_labels || {};

  // Form state
  const [nombre, setNombre] = useState('');
  const [ingredientes, setIngredientes] = useState('');
  const [estiloIdx, setEstiloIdx] = useState(0);
  const [idiomaIdx, setIdiomaIdx] = useState(0);
  const [precio, setPrecio] = useState('');

  // Results state
  const [result, setResult] = useState<MenuCopyResult | null>(null);
  const [isGenerating, setIsGenerating] = useState(false);
  const [copiedKey, setCopiedKey] = useState<string | null>(null);

  const handleGenerate = () => {
    if (!nombre.trim() || !ingredientes.trim()) return;
    setIsGenerating(true);
    setTimeout(() => {
      setResult(generateMenuCopy(nombre.trim(), ingredientes.trim(), estiloIdx, idiomaIdx));
      setIsGenerating(false);
    }, 800);
  };

  const handleCopy = (text: string, key: string) => {
    navigator.clipboard.writeText(text).then(() => {
      setCopiedKey(key);
      setTimeout(() => setCopiedKey(null), 2000);
    });
  };

  const downloadPDF = () => {
    if (!result) return;

    const rl = resultLabels as Record<string, string>;
    const T = (key: string) => rl?.[key] || key;
    const today = new Date().toLocaleDateString(currentLanguage, { year: 'numeric', month: '2-digit', day: '2-digit' });
    const estiloName = estilos[estiloIdx] || '';

    const doc = new jsPDF({ unit: 'mm', format: 'a4' });
    const W = 210;
    const MARGIN = 18;
    const CW = W - MARGIN * 2;
    let y = 0;

    const checkPage = (needed: number) => {
      if (y + needed > 270) { doc.addPage(); y = 18; }
    };

    // Header
    doc.setFillColor(37, 99, 235); // blue-600
    doc.rect(0, 0, W, 22, 'F');
    doc.setFontSize(9);
    doc.setTextColor(219, 234, 254); // blue-100
    doc.text('AI Chef Pro — ' + T('pdf_title'), MARGIN, 9);
    doc.setFontSize(8);
    doc.setTextColor(147, 197, 253); // blue-300
    doc.text(T('pdf_date_label') + ': ' + today, MARGIN, 16);

    y = 32;

    // Dish name
    doc.setFontSize(22);
    doc.setTextColor(17, 24, 39); // gray-900
    const nameLines = doc.splitTextToSize(nombre.toUpperCase(), CW);
    doc.text(nameLines, MARGIN, y);
    y += nameLines.length * 10 + 2;

    // Ingredients + style
    doc.setFontSize(9);
    doc.setTextColor(107, 114, 128); // gray-500
    doc.text(T('pdf_ingredients_label') + ': ' + ingredientes, MARGIN, y);
    y += 5.5;
    if (estiloName) {
      doc.text(T('pdf_style_label') + ': ' + estiloName, MARGIN, y);
      y += 5.5;
    }

    // Divider
    doc.setDrawColor(191, 219, 254); // blue-200
    doc.setLineWidth(0.4);
    doc.line(MARGIN, y + 2, W - MARGIN, y + 2);
    y += 10;

    // Helper to render a description section
    const renderSection = (emoji: string, label: string, text: string, borderR: number, borderG: number, borderB: number) => {
      checkPage(35);
      // Left color bar
      doc.setFillColor(borderR, borderG, borderB);
      doc.rect(MARGIN, y - 1, 3, 18, 'F');
      // Label
      doc.setFontSize(8);
      doc.setTextColor(borderR, borderG, borderB);
      doc.text(`${emoji}  ${label.toUpperCase()}`, MARGIN + 6, y + 4);
      y += 8;
      // Text
      doc.setFontSize(10);
      doc.setTextColor(55, 65, 81); // gray-700
      const lines = doc.splitTextToSize(text, CW - 8);
      checkPage(lines.length * 5.5 + 8);
      doc.text(lines, MARGIN + 6, y);
      y += lines.length * 5.5 + 8;
    };

    renderSection('📋', T('clasica'),   result.clasica,   37, 99, 235);   // blue
    renderSection('❤️', T('emocional'), result.emocional, 244, 63, 94);   // rose
    renderSection('🌱', T('km0'),       result.km0,       22, 163, 74);   // green

    // Divider
    doc.setDrawColor(191, 219, 254);
    doc.line(MARGIN, y, W - MARGIN, y);
    y += 8;

    // Alternative name section
    checkPage(30);
    doc.setFontSize(8);
    doc.setTextColor(99, 102, 241); // indigo
    doc.text('✨  ' + T('pdf_alt_name_label').toUpperCase(), MARGIN, y);
    y += 6;
    doc.setFontSize(14);
    doc.setTextColor(17, 24, 39);
    doc.text(`"${result.nombreAlternativo}"`, MARGIN, y);
    y += 7;
    doc.setFontSize(9);
    doc.setTextColor(107, 114, 128);
    const razonLines = doc.splitTextToSize(T('pdf_alt_reason_label') + ': ' + result.razonNombre, CW);
    doc.text(razonLines, MARGIN, y);
    y += razonLines.length * 5 + 10;

    // Footer
    doc.setDrawColor(191, 219, 254);
    doc.setLineWidth(0.4);
    doc.line(MARGIN, y, W - MARGIN, y);
    y += 5;
    doc.setFontSize(7.5);
    doc.setTextColor(156, 163, 175);
    doc.text(T('pdf_generated_by'), MARGIN, y);

    const date = new Date().toISOString().slice(0, 10);
    doc.save(`${T('pdf_filename')}-${date}.pdf`);
  };

  const handleReset = () => {
    setNombre('');
    setIngredientes('');
    setEstiloIdx(0);
    setIdiomaIdx(0);
    setPrecio('');
    setResult(null);
  };

  const showCatalanNote = idiomaIdx === 2 || idiomaIdx === 3;
  const isValid = nombre.trim().length > 0 && ingredientes.trim().length > 0;

  const lang = i18n.language || 'es';
  const hubSlug = HUB_SLUGS[lang] || HUB_SLUGS.es;

  return (
    <div className="min-h-screen bg-white flex flex-col">
      <Helmet>
        <html lang={lang} />
        <title>{seo?.title || 'Generador de Textos para Carta de Restaurante | AI Chef Pro'}</title>
        <meta name="description" content={seo?.description || ''} />
        {seo?.keywords && <meta name="keywords" content={seo.keywords} />}
        <link rel="canonical" href={canonicalUrl} />
        {Object.entries(LANG_SLUGS).map(([l, s]) => (
          <link
            key={l}
            rel="alternate"
            hrefLang={l}
            href={`${siteUrl}${s}`}
          />
        ))}
        {faqSchema && (
          <script type="application/ld+json">{JSON.stringify(faqSchema)}</script>
        )}
      </Helmet>

      <ModernHeader />

      <main className="flex-1">
        {/* ── Hero ── */}
        <section className="bg-gradient-to-b from-blue-50 to-white py-16 px-4">
          <div className="max-w-3xl mx-auto text-center">
            <HeroSocialProof />
            <Badge className="bg-blue-100 text-blue-700 border-0 mb-4 px-3 py-1">
              {hero?.badge || 'Gratis — Sin registro'}
            </Badge>

            <h1 className="text-4xl md:text-5xl font-bold text-gray-900 mb-4 leading-tight">
              {hero?.h1 || 'Generador de Textos para tu Carta'}
            </h1>
            <p className="text-lg text-gray-600 mb-8 max-w-2xl mx-auto">
              {hero?.subtitle || 'Introduce el nombre del plato e ingredientes y obtén 3 descripciones listas para tu carta: clásica, emocional y km0.'}
            </p>

            <div className="flex flex-col sm:flex-row gap-3 justify-center">
              <Button
                className="bg-blue-600 hover:bg-blue-700 text-white px-6 py-3"
                onClick={() => document.getElementById('tool-section')?.scrollIntoView({ behavior: 'smooth' })}
              >
                <FileText className="w-4 h-4 mr-2" />
                {hero?.cta_tool || 'Generar textos para mi carta'}
              </Button>
              <Button variant="outline" className="border-blue-600 text-blue-600 hover:bg-blue-50 px-6 py-3" asChild>
                <a href={getAppUrl()} target="_blank" rel="noopener noreferrer">
                  {hero?.cta_premium || 'Ver Plan Premium →'}
                </a>
              </Button>
            </div>
          </div>
        </section>

        {/* ── Tool ── */}
        <section id="tool-section" className="py-16 px-4 bg-white">
          <div className="max-w-2xl mx-auto">
            <div className="bg-white border border-gray-200 rounded-2xl shadow-sm p-8">
              <div className="flex items-center gap-3 mb-8">
                <div className="w-10 h-10 rounded-xl bg-blue-100 flex items-center justify-center">
                  <Sparkles className="w-5 h-5 text-blue-600" />
                </div>
                <h2 className="text-xl font-bold text-gray-900">
                  {tool?.title || 'Generador de Textos para Carta'}
                </h2>
              </div>

              {/* Nombre del plato */}
              <div className="mb-5">
                <label className="block text-sm font-semibold text-gray-700 mb-2">
                  {tool?.nombre_label || 'Nombre actual del plato'} <span className="text-red-500">*</span>
                </label>
                <input
                  type="text"
                  value={nombre}
                  onChange={e => setNombre(e.target.value)}
                  placeholder={tool?.nombre_placeholder || 'Ej: Croquetas de jamón'}
                  className="w-full border border-gray-300 rounded-lg px-4 py-3 text-gray-900 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent"
                />
              </div>

              {/* Ingredientes */}
              <div className="mb-5">
                <label className="block text-sm font-semibold text-gray-700 mb-2">
                  {tool?.ingredientes_label || 'Ingredientes principales'} <span className="text-red-500">*</span>
                </label>
                <textarea
                  value={ingredientes}
                  onChange={e => setIngredientes(e.target.value)}
                  placeholder={tool?.ingredientes_placeholder || 'Ej: jamón ibérico, bechamel, pan rallado'}
                  rows={3}
                  className="w-full border border-gray-300 rounded-lg px-4 py-3 text-gray-900 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent resize-none"
                />
                <p className="text-xs text-gray-500 mt-1">
                  {tool?.ingredientes_hint || 'Separa los ingredientes por comas'}
                </p>
              </div>

              {/* Estilo + Idioma */}
              <div className="grid grid-cols-1 sm:grid-cols-2 gap-5 mb-5">
                <div>
                  <label className="block text-sm font-semibold text-gray-700 mb-2">
                    {tool?.estilo_label || 'Estilo del restaurante'}
                  </label>
                  <select
                    value={estiloIdx}
                    onChange={e => setEstiloIdx(Number(e.target.value))}
                    className="w-full border border-gray-300 rounded-lg px-4 py-3 text-gray-900 bg-white focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent"
                  >
                    {estilos.map((e: string, i: number) => (
                      <option key={i} value={i}>{e}</option>
                    ))}
                  </select>
                </div>
                <div>
                  <label className="block text-sm font-semibold text-gray-700 mb-2">
                    {tool?.idioma_label || 'Idioma de la carta'}
                  </label>
                  <select
                    value={idiomaIdx}
                    onChange={e => setIdiomaIdx(Number(e.target.value))}
                    className="w-full border border-gray-300 rounded-lg px-4 py-3 text-gray-900 bg-white focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent"
                  >
                    {idiomas.map((idioma: string, i: number) => (
                      <option key={i} value={i}>{idioma}</option>
                    ))}
                  </select>
                </div>
              </div>

              {/* Precio (opcional) */}
              <div className="mb-6">
                <label className="block text-sm font-semibold text-gray-700 mb-2">
                  {tool?.precio_label || 'Precio del plato (opcional)'}
                </label>
                <div className="relative">
                  <span className="absolute left-4 top-1/2 -translate-y-1/2 text-gray-500">€</span>
                  <input
                    type="number"
                    value={precio}
                    onChange={e => setPrecio(e.target.value)}
                    placeholder="9.50"
                    min="0"
                    step="0.50"
                    className="w-full border border-gray-300 rounded-lg pl-8 pr-4 py-3 text-gray-900 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent"
                  />
                </div>
              </div>

              {showCatalanNote && (
                <div className="bg-amber-50 border border-amber-200 rounded-lg px-4 py-3 mb-5 text-sm text-amber-800">
                  {tool?.catalan_note || 'El texto se genera en español. Puedes adaptarlo al catalán o euskera manualmente.'}
                </div>
              )}

              <Button
                className="w-full bg-blue-600 hover:bg-blue-700 text-white py-3 text-base font-semibold"
                onClick={handleGenerate}
                disabled={!isValid || isGenerating}
              >
                {isGenerating ? (
                  <span className="flex items-center justify-center gap-2">
                    <span className="animate-spin rounded-full h-4 w-4 border-b-2 border-white" />
                    {tool?.generating || 'Creando descripciones…'}
                  </span>
                ) : (
                  <span className="flex items-center justify-center gap-2">
                    <Sparkles className="w-4 h-4" />
                    {tool?.generate_btn || 'Generar textos para mi carta'}
                  </span>
                )}
              </Button>
            </div>

            {/* ── Results ── */}
            {result && (
              <div className="mt-8 space-y-4">
                <div className="flex items-center justify-between">
                  <h3 className="text-lg font-bold text-gray-900">
                    {resultLabels?.title || 'Descripciones para tu carta'} —{' '}
                    <span className="text-blue-600 font-semibold">{nombre}</span>
                  </h3>
                  <div className="flex items-center gap-2">
                    <button
                      onClick={downloadPDF}
                      className="flex items-center gap-1.5 text-sm text-white bg-blue-600 hover:bg-blue-700 transition-colors px-3 py-1.5 rounded-lg font-medium"
                    >
                      <FileDown className="w-4 h-4" />
                      {(resultLabels as Record<string, string>)?.pdf_download || 'Descargar PDF'}
                    </button>
                    <button
                      onClick={handleReset}
                      className="flex items-center gap-1 text-sm text-gray-500 hover:text-blue-600 transition-colors"
                    >
                      <RotateCcw className="w-4 h-4" />
                      {resultLabels?.reset || 'Nuevo plato'}
                    </button>
                  </div>
                </div>

                {/* Clásica */}
                <ResultCard
                  emoji="📋"
                  label={resultLabels?.clasica || 'Clásica'}
                  text={result.clasica}
                  colorClass="border-l-blue-400"
                  onCopy={() => handleCopy(result.clasica, 'clasica')}
                  copied={copiedKey === 'clasica'}
                  copyLabel={resultLabels?.copy || 'Copiar'}
                  copiedLabel={resultLabels?.copied || '¡Copiado!'}
                />

                {/* Emocional */}
                <ResultCard
                  emoji="❤️"
                  label={resultLabels?.emocional || 'Emocional'}
                  text={result.emocional}
                  colorClass="border-l-rose-400"
                  onCopy={() => handleCopy(result.emocional, 'emocional')}
                  copied={copiedKey === 'emocional'}
                  copyLabel={resultLabels?.copy || 'Copiar'}
                  copiedLabel={resultLabels?.copied || '¡Copiado!'}
                />

                {/* KM0 */}
                <ResultCard
                  emoji="🌱"
                  label={resultLabels?.km0 || 'KM0 / Producto local'}
                  text={result.km0}
                  colorClass="border-l-green-400"
                  onCopy={() => handleCopy(result.km0, 'km0')}
                  copied={copiedKey === 'km0'}
                  copyLabel={resultLabels?.copy || 'Copiar'}
                  copiedLabel={resultLabels?.copied || '¡Copiado!'}
                />

                {/* Nombre alternativo */}
                <div className="bg-gradient-to-r from-blue-50 to-indigo-50 border border-blue-200 rounded-xl p-5">
                  <div className="flex items-start justify-between gap-4">
                    <div>
                      <p className="text-xs font-semibold text-blue-600 uppercase tracking-wider mb-1">
                        ✨ {resultLabels?.nombre_alt || 'Nombre alternativo sugerido'}
                      </p>
                      <p className="text-xl font-bold text-gray-900 mb-1">
                        "{result.nombreAlternativo}"
                      </p>
                      <p className="text-sm text-gray-600">{result.razonNombre}</p>
                    </div>
                    <button
                      onClick={() => handleCopy(result.nombreAlternativo, 'nombre')}
                      className="shrink-0 flex items-center gap-1.5 text-sm text-blue-600 hover:text-blue-700 transition-colors"
                    >
                      {copiedKey === 'nombre' ? (
                        <><CheckCircle className="w-4 h-4 text-green-600" /><span className="text-green-600">{resultLabels?.copied || '¡Copiado!'}</span></>
                      ) : (
                        <><Copy className="w-4 h-4" /><span>{resultLabels?.copy || 'Copiar'}</span></>
                      )}
                    </button>
                  </div>
                </div>

                {/* CTA post-result */}
                <div className="bg-blue-600 rounded-xl p-6 text-white text-center">
                  <p className="font-semibold mb-1">{resultLabels?.cta_title || '¿Quieres generar toda tu carta optimizada para SEO?'}</p>
                  <p className="text-blue-100 text-sm mb-4">
                    {resultLabels?.cta_subtitle || 'Descubre Menu Plate Local SEO en AI Chef Pro'}
                  </p>
                  <Button className="bg-white text-blue-600 hover:bg-blue-50 font-semibold" asChild>
                    <a href={getAppUrl()} target="_blank" rel="noopener noreferrer">
                      {resultLabels?.cta_btn || 'Ver todas las funcionalidades →'}
                    </a>
                  </Button>
                </div>
              </div>
            )}
          </div>
        </section>

        <PricingPlans toolKey="toolMenuCopy" />

        {/* ── FAQ ── */}
        {Array.isArray(faqItems) && faqItems.length > 0 && (
          <section className="py-16 px-4 bg-gray-50">
            <div className="max-w-2xl mx-auto">
              <h2 className="text-2xl font-bold text-gray-900 text-center mb-8">
                {tool?.faq_title || 'Preguntas frecuentes'}
              </h2>
              <div className="space-y-4">
                {faqItems.map((item, i) => (
                  <div key={i} className="bg-white rounded-xl p-6 border border-gray-200">
                    <p className="font-semibold text-gray-900 mb-2">{item.q}</p>
                    <p className="text-gray-600 text-sm leading-relaxed">{item.a}</p>
                  </div>
                ))}
              </div>
            </div>
          </section>
        )}

        <OtherFreeTools excludeIndex={4} />

        {/* ── Footer CTA ── */}
        <section className="py-16 px-4 bg-white border-t border-gray-100">
          <div className="max-w-2xl mx-auto text-center">
            <h2 className="text-2xl font-bold text-gray-900 mb-3">
              {ctaSection?.title || '¿Listo para mejorar la carta de tu restaurante?'}
            </h2>
            <p className="text-gray-600 mb-8">
              {ctaSection?.subtitle || 'Genera textos profesionales para cada plato y eleva la percepción de tu restaurante.'}
            </p>
            <div className="flex flex-col sm:flex-row gap-3 justify-center">
              <Button
                className="bg-blue-600 hover:bg-blue-700 text-white px-6 py-3"
                onClick={() => document.getElementById('tool-section')?.scrollIntoView({ behavior: 'smooth' })}
              >
                {ctaSection?.cta_primary || 'Generar textos gratis'}
              </Button>
              <Button variant="outline" className="border-gray-300 text-gray-700 hover:bg-gray-50 px-6 py-3" asChild>
                <Link to={hubSlug}>
                  <ArrowRight className="w-4 h-4 mr-2" />
                  {ctaSection?.cta_secondary || 'Ver todas las herramientas'}
                </Link>
              </Button>
            </div>
          </div>
        </section>
      </main>

      <ModernFooter />
    </div>
  );
}

// ─── Result Card subcomponent ─────────────────────────────────────────────────

function ResultCard({
  emoji,
  label,
  text,
  colorClass,
  onCopy,
  copied,
  copyLabel,
  copiedLabel,
}: {
  emoji: string;
  label: string;
  text: string;
  colorClass: string;
  onCopy: () => void;
  copied: boolean;
  copyLabel: string;
  copiedLabel: string;
}) {
  return (
    <div className={`bg-white border border-gray-200 border-l-4 ${colorClass} rounded-xl p-5`}>
      <div className="flex items-start justify-between gap-4">
        <div className="flex-1">
          <p className="text-xs font-semibold text-gray-500 uppercase tracking-wider mb-2">
            {emoji} {label}
          </p>
          <p className="text-gray-800 leading-relaxed">"{text}"</p>
          <p className="text-xs text-gray-400 mt-2">{text.length} {text.length === 1 ? 'carácter' : 'caracteres'}</p>
        </div>
        <button
          onClick={onCopy}
          className="shrink-0 flex items-center gap-1.5 text-sm transition-colors mt-1"
          style={{ color: copied ? '#16a34a' : '#2563eb' }}
        >
          {copied ? (
            <><CheckCircle className="w-4 h-4" /><span>{copiedLabel}</span></>
          ) : (
            <><Copy className="w-4 h-4" /><span>{copyLabel}</span></>
          )}
        </button>
      </div>
    </div>
  );
}
