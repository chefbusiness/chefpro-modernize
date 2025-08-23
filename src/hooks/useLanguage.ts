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
      // For other pages, we'll handle this when we create them
      window.location.href = newLang === 'es' ? '/' : `/${newLang}`;
    }
  };

  const getAppUrl = (language?: Language) => {
    const targetLang = language || i18n.language as Language;
    return targetLang === 'en' ? 'https://appen.aichef.pro' : 'https://app.aichef.pro';
  };

  const getCurrentLanguage = (): Language => {
    return i18n.language as Language;
  };
  
  return {
    currentLanguage: getCurrentLanguage(),
    changeLanguage,
    t,
    getAppUrl
  };
};