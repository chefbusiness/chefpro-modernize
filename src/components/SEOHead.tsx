import { Helmet } from 'react-helmet-async';
import { useTranslation } from 'react-i18next';
import { useLocation } from 'react-router-dom';

interface SEOHeadProps {
  title?: string;
  description?: string;
  keywords?: string;
  canonical?: string;
  ogImage?: string;
  ogType?: string;
  noindex?: boolean;
}

const SEOHead = ({ 
  title, 
  description, 
  keywords, 
  canonical, 
  ogImage = "/og-image.jpg",
  ogType = "website",
  noindex = false 
}: SEOHeadProps) => {
  const { t, i18n } = useTranslation();
  const location = useLocation();
  
  const currentLanguage = i18n.language;
  const siteUrl = import.meta.env.VITE_SITE_URL || "https://aichef.pro";
  
  // Use provided title or fallback to SEO default
  const pageTitle = title || t('seo.title');
  const pageDescription = description || t('seo.description');
  const pageKeywords = keywords || t('seo.keywords');
  
  // Generate hreflang URLs for all supported languages
  const languages = ['es', 'en', 'fr', 'de', 'it', 'pt', 'nl'];
  
  // Build canonical URL with current path
  const currentPath = location.pathname;
  const basePath = currentPath.replace(/^\/(es|en|fr|de|it|pt|nl)/, '') || '/';
  const canonicalUrl = canonical || `${siteUrl}${currentLanguage === 'es' ? basePath : `/${currentLanguage}${basePath}`}`.replace(/\/+/g, '/').replace(/\/$/, '') || siteUrl;
  
  // Map language codes to proper og:locale format
  const getOGLocale = (lang: string) => {
    const localeMap: Record<string, string> = {
      'es': 'es_ES',
      'en': 'en_US', 
      'fr': 'fr_FR',
      'de': 'de_DE',
      'it': 'it_IT',
      'pt': 'pt_PT',
      'nl': 'nl_NL'
    };
    return localeMap[lang] || 'es_ES';
  };
  
  return (
    <Helmet>
      {/* Basic Meta Tags */}
      <title>{pageTitle}</title>
      <meta name="description" content={pageDescription} />
      <meta name="keywords" content={pageKeywords} />
      <meta name="robots" content={noindex ? "noindex,nofollow" : "index,follow"} />
      <meta name="author" content="AI Chef Pro" />
      <meta name="viewport" content="width=device-width, initial-scale=1.0" />
      
      {/* Language and Canonical */}
      <html lang={currentLanguage} />
      <link rel="canonical" href={canonicalUrl} />
      
      {/* Hreflang for International SEO */}
      {languages.map(lang => {
        const langPath = lang === 'es' ? basePath : `/${lang}${basePath}`;
        const hrefLangUrl = `${siteUrl}${langPath}`.replace(/\/+/g, '/').replace(/\/$/, '') || siteUrl;
        return (
          <link 
            key={lang}
            rel="alternate" 
            hrefLang={lang} 
            href={hrefLangUrl} 
          />
        );
      })}
      <link rel="alternate" hrefLang="x-default" href={siteUrl} />
      
      {/* Open Graph */}
      <meta property="og:title" content={pageTitle} />
      <meta property="og:description" content={pageDescription} />
      <meta property="og:type" content={ogType} />
      <meta property="og:url" content={canonicalUrl} />
      <meta property="og:image" content={`${siteUrl}${ogImage}`} />
      <meta property="og:image:secure_url" content={`${siteUrl}${ogImage}`} />
      <meta property="og:image:alt" content={`${pageTitle} - AI Chef Pro`} />
      <meta property="og:image:width" content="1200" />
      <meta property="og:image:height" content="630" />
      <meta property="og:site_name" content="AI Chef Pro" />
      <meta property="og:locale" content={getOGLocale(currentLanguage)} />
      {languages.filter(lang => lang !== currentLanguage).map(lang => (
        <meta key={`og-locale-${lang}`} property="og:locale:alternate" content={getOGLocale(lang)} />
      ))}
      
      {/* Twitter Card */}
      <meta name="twitter:card" content="summary_large_image" />
      <meta name="twitter:site" content="@aichefpro" />
      <meta name="twitter:title" content={pageTitle} />
      <meta name="twitter:description" content={pageDescription} />
      <meta name="twitter:image" content={`${siteUrl}${ogImage}`} />
      <meta name="twitter:image:alt" content={`${pageTitle} - AI Chef Pro`} />
      
      {/* Additional SEO */}
      <meta name="theme-color" content="#f59e0b" />
      <meta name="msapplication-TileColor" content="#f59e0b" />
      
      {/* Enhanced Structured Data */}
      <script type="application/ld+json">
        {JSON.stringify([
          {
            "@context": "https://schema.org",
            "@type": "Organization",
            "name": "AI Chef Pro",
            "url": siteUrl,
            "logo": `${siteUrl}/logo-ai-chef-pro.svg`,
            "sameAs": [
              "https://twitter.com/aichefpro",
              "https://www.linkedin.com/company/aichefpro"
            ],
            "contactPoint": {
              "@type": "ContactPoint",
              "email": "info@aichef.pro",
              "telephone": "+34744717942",
              "contactType": "customer service"
            }
          },
          {
            "@context": "https://schema.org",
            "@type": "WebSite",
            "name": "AI Chef Pro",
            "url": siteUrl,
            "inLanguage": languages
          },
          {
            "@context": "https://schema.org",
            "@type": "WebApplication",
            "name": "AI Chef Pro",
            "description": pageDescription,
            "url": siteUrl,
            "applicationCategory": "BusinessApplication",
            "operatingSystem": "Web",
            "offers": {
              "@type": "Offer",
              "category": "SaaS",
              "priceCurrency": "EUR",
              "price": "0",
              "priceValidUntil": "2025-12-31"
            },
            "aggregateRating": {
              "@type": "AggregateRating",
              "ratingValue": "5.0",
              "ratingCount": "847"
            },
            "inLanguage": languages
          }
        ])}
      </script>
    </Helmet>
  );
};

export default SEOHead;