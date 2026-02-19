import { useTranslation } from 'react-i18next';
import { useEffect } from 'react';
import { useParams, useNavigate } from 'react-router-dom';

export type Language = 'es' | 'en' | 'fr' | 'de' | 'it' | 'pt' | 'nl';

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
    
    // Update URL to reflect language change
    const currentPath = window.location.pathname;
    const isHomePage = currentPath === '/' || currentPath.match(/^\/[a-z]{2}$/);
    
    if (isHomePage) {
      if (newLang === 'es') {
        navigate('/', { replace: true });
      } else {
        navigate(`/${newLang}`, { replace: true });
      }
    } else {
      // Handle language switching for specific pages
      let newPath = '';
      
      // Remove current language prefix if exists
      const pathWithoutLang = currentPath.replace(/^\/[a-z]{2}/, '');
      const cleanPath = pathWithoutLang || '/';
      
      if (newLang === 'es') {
        // For Spanish, no language prefix needed
        newPath = cleanPath === '/' ? '/' : cleanPath;
      } else {
        // For other languages, add language prefix
        newPath = `/${newLang}${cleanPath}`;
      }
      
      navigate(newPath, { replace: true });
    }
  };

  const getAppUrl = (language?: Language) => {
    const targetLang = language || i18n.language as Language;
    if (targetLang === 'en') return 'https://enapp.aichef.pro';
    if (targetLang === 'it') return 'https://itapp.aichef.pro';
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