import { useTranslation } from 'react-i18next';
import { useEffect } from 'react';
import { useParams, useNavigate } from 'react-router-dom';

export type Language = 'es' | 'en' | 'fr' | 'de' | 'it' | 'pt' | 'nl';

// Pages with language-native slugs (not just a lang prefix + same slug)
// Each entry maps a language code to its URL slug for that page
const LANGUAGE_NATIVE_PAGES: Array<Record<Language, string>> = [
  {
    es: 'herramientas-ia-para-restaurantes',
    en: 'ai-tools-for-restaurants',
    fr: 'outils-ia-restaurant',
    de: 'ki-tools-restaurant',
    it: 'strumenti-ia-ristorante',
    pt: 'ferramentas-ia-restaurante',
    nl: 'ai-tools-restaurant',
  },
  {
    es: 'reducir-costes-restaurante-ia',
    en: 'reduce-restaurant-costs-ai',
    fr: 'reduire-couts-restaurant-ia',
    de: 'restaurantkosten-senken-ki',
    it: 'ridurre-costi-ristorante-ia',
    pt: 'reduzir-custos-restaurante-ia',
    nl: 'restaurantkosten-verlagen-ai',
  },
  {
    es: 'carta-menu-restaurante-ia',
    en: 'restaurant-menu-ai',
    fr: 'carte-menu-restaurant-ia',
    de: 'speisekarte-restaurant-ki',
    it: 'menu-ristorante-ia',
    pt: 'cardapio-restaurante-ia',
    nl: 'restaurantmenu-ai',
  },
  {
    es: 'marketing-restaurante-ia',
    en: 'restaurant-marketing-ai',
    fr: 'marketing-restaurant-ia',
    de: 'restaurant-marketing-ki',
    it: 'marketing-ristorante-ia',
    pt: 'marketing-restaurante-ia-pt',
    nl: 'restaurant-marketing-ai-nl',
  },
  {
    es: 'chatgpt-para-restaurantes',
    en: 'chatgpt-for-restaurants',
    fr: 'chatgpt-pour-restaurants',
    de: 'chatgpt-fuer-restaurants',
    it: 'chatgpt-per-ristoranti',
    pt: 'chatgpt-para-restaurantes',
    nl: 'chatgpt-voor-restaurants',
  },
  {
    es: 'herramientas-gratuitas',
    en: 'free-tools-restaurants',
    fr: 'outils-gratuits-restaurant',
    de: 'kostenlose-tools-restaurant',
    it: 'strumenti-gratuiti-ristorante',
    pt: 'ferramentas-gratuitas-restaurante',
    nl: 'gratis-tools-restaurant',
  },
  {
    es: 'calculadora-food-cost-restaurante',
    en: 'food-cost-calculator-restaurant',
    fr: 'calculateur-food-cost-restaurant',
    de: 'food-cost-rechner-restaurant',
    it: 'calcolatore-food-cost-ristorante',
    pt: 'calculadora-food-cost-restaurante',
    nl: 'food-cost-calculator-restaurant',
  },
  {
    es: 'simulador-rentabilidad-restaurante',
    en: 'restaurant-profit-simulator',
    fr: 'simulateur-rentabilite-restaurant',
    de: 'rentabilitaet-simulator-restaurant',
    it: 'simulatore-redditivita-ristorante',
    pt: 'simulador-rentabilidade-restaurante',
    nl: 'winstgevendheid-simulator-restaurant',
  },
  {
    es: 'test-digitalizacion-restaurante',
    en: 'restaurant-digitalization-test',
    fr: 'test-digitalisation-restaurant',
    de: 'digitalisierungstest-restaurant',
    it: 'test-digitalizzazione-ristorante',
    pt: 'teste-digitalizacao-restaurante',
    nl: 'digitaliseringstest-restaurant',
  },
  {
    es: 'detector-alergenos-restaurante',
    en: 'restaurant-allergen-detector',
    fr: 'detecteur-allergenes-restaurant',
    de: 'allergen-detektor-restaurant',
    it: 'rilevatore-allergeni-ristorante',
    pt: 'detector-alergenos-restaurante',
    nl: 'allergenen-detector-restaurant',
  },
  {
    es: 'calculadora-brigada-restaurante',
    en: 'restaurant-brigade-calculator',
    fr: 'calculateur-brigade-restaurant',
    de: 'brigaden-rechner-restaurant',
    it: 'calcolatore-brigata-ristorante',
    pt: 'calculadora-brigada-restaurante',
    nl: 'brigade-calculator-restaurant',
  },
  {
    es: 'calendario-contenidos-restaurante',
    en: 'restaurant-content-calendar',
    fr: 'calendrier-contenu-restaurant',
    de: 'content-kalender-restaurant',
    it: 'calendario-contenuti-ristorante',
    pt: 'calendario-conteudo-restaurante',
    nl: 'content-kalender-restaurant',
  },
  {
    es: 'generador-textos-carta-restaurante',
    en: 'restaurant-menu-copy-generator',
    fr: 'generateur-textes-carte-restaurant',
    de: 'speisekarten-text-generator',
    it: 'generatore-testi-menu-ristorante',
    pt: 'gerador-textos-cardapio-restaurante',
    nl: 'menukaart-tekst-generator',
  },
  {
    es: 'generador-menu-degustacion',
    en: 'tasting-menu-generator',
    fr: 'generateur-menu-degustation',
    de: 'degustationsmenu-generator',
    it: 'generatore-menu-degustazione',
    pt: 'gerador-menu-degustacao',
    nl: 'proefmenu-generator',
  },
];

// Returns the slug map for the current path if it matches a native-slug page, else null
function detectNativePage(currentPath: string): Record<Language, string> | null {
  for (const slugMap of LANGUAGE_NATIVE_PAGES) {
    for (const [lang, slug] of Object.entries(slugMap)) {
      const expected = lang === 'es' ? `/${slug}` : `/${lang}/${slug}`;
      if (currentPath === expected) return slugMap as Record<Language, string>;
    }
  }
  return null;
}

export const useLanguage = () => {
  const { i18n, t } = useTranslation();
  const { lang } = useParams<{ lang?: string }>();
  const navigate = useNavigate();

  useEffect(() => {
    // If URL has language parameter, change i18n language
    if (lang && ['es', 'en', 'fr', 'de', 'it', 'pt', 'nl'].includes(lang)) {
      if (i18n.language !== lang) {
        i18n.changeLanguage(lang);
      }
    } else if (lang) {
      // If invalid language in URL, redirect to Spanish (default)
      navigate('/', { replace: true });
    }
  }, [lang, i18n, navigate]);

  const changeLanguage = (newLang: Language) => {
    i18n.changeLanguage(newLang);

    const currentPath = window.location.pathname;
    const isHomePage = currentPath === '/' || currentPath.match(/^\/[a-z]{2}$/);

    // Check if this page uses language-native slugs (e.g. landing pages)
    const nativePage = detectNativePage(currentPath);
    if (nativePage) {
      const targetSlug = nativePage[newLang];
      const newPath = newLang === 'es' ? `/${targetSlug}` : `/${newLang}/${targetSlug}`;
      navigate(newPath, { replace: true });
      return;
    }

    if (isHomePage) {
      if (newLang === 'es') {
        navigate('/', { replace: true });
      } else {
        navigate(`/${newLang}`, { replace: true });
      }
    } else {
      // Handle language switching for pages with shared slug (e.g. /mentoria-online)
      const pathWithoutLang = currentPath.replace(/^\/[a-z]{2}\//, '/');
      const cleanPath = pathWithoutLang || '/';

      const newPath = newLang === 'es' ? cleanPath : `/${newLang}${cleanPath}`;
      navigate(newPath, { replace: true });
    }
  };

  const getAppUrl = (language?: Language) => {
    const targetLang = language || i18n.language as Language;
    if (targetLang === 'en') return 'https://enapp.aichef.pro';
    if (targetLang === 'it') return 'https://itapp.aichef.pro';
    if (targetLang === 'fr') return 'https://frapp.aichef.pro';
    return 'https://app.aichef.pro';
  };

  const getCurrentLanguage = (): Language => {
    const currentLang = i18n.language;
    // Normalize language codes (es-ES -> es, en-US -> en, etc.)
    const simpleLang = currentLang.split('-')[0];
    return (['es', 'en', 'fr', 'de', 'it', 'pt', 'nl'].includes(simpleLang) 
      ? simpleLang 
      : 'es') as Language;
  };
  
  return {
    currentLanguage: getCurrentLanguage(),
    changeLanguage,
    t,
    getAppUrl
  };
};