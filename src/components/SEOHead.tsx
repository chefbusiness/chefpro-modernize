import { Helmet } from 'react-helmet-async';
import { useTranslation } from 'react-i18next';

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
  
  const currentLanguage = i18n.language;
  const siteUrl = "https://aichef.pro";
  
  // Use provided title or fallback to SEO default
  const pageTitle = title || t('seo.title');
  const pageDescription = description || t('seo.description');
  const pageKeywords = keywords || t('seo.keywords');
  
  // Generate hreflang URLs for all supported languages
  const languages = ['es', 'en', 'fr', 'de', 'it', 'pt', 'nl'];
  const canonicalUrl = canonical || `${siteUrl}/${currentLanguage === 'es' ? '' : currentLanguage}`;
  
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
      {languages.map(lang => (
        <link 
          key={lang}
          rel="alternate" 
          hrefLang={lang} 
          href={`${siteUrl}${lang === 'es' ? '' : `/${lang}`}`} 
        />
      ))}
      <link rel="alternate" hrefLang="x-default" href={siteUrl} />
      
      {/* Open Graph */}
      <meta property="og:title" content={pageTitle} />
      <meta property="og:description" content={pageDescription} />
      <meta property="og:type" content={ogType} />
      <meta property="og:url" content={canonicalUrl} />
      <meta property="og:image" content={`${siteUrl}${ogImage}`} />
      <meta property="og:site_name" content="AI Chef Pro" />
      <meta property="og:locale" content={currentLanguage === 'es' ? 'es_ES' : `${currentLanguage}_${currentLanguage.toUpperCase()}`} />
      
      {/* Twitter Card */}
      <meta name="twitter:card" content="summary_large_image" />
      <meta name="twitter:title" content={pageTitle} />
      <meta name="twitter:description" content={pageDescription} />
      <meta name="twitter:image" content={`${siteUrl}${ogImage}`} />
      
      {/* Additional SEO */}
      <meta name="theme-color" content="#f59e0b" />
      <meta name="msapplication-TileColor" content="#f59e0b" />
      
      {/* Structured Data */}
      <script type="application/ld+json">
        {JSON.stringify({
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
        })}
      </script>
    </Helmet>
  );
};

export default SEOHead;