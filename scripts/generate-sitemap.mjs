import fs from 'fs';
import path from 'path';

const SITE_URL = 'https://aichef.pro';
const LANGUAGES = ['es', 'en', 'fr', 'de', 'it', 'pt', 'nl'];
const DEFAULT_LANG = 'es';

// Get current date in ISO format
const getCurrentDate = () => {
  return new Date().toISOString().split('T')[0];
};

// Generate hreflang links for a URL
const generateHreflangs = (path = '') => {
  return LANGUAGES.map(lang => {
    const href = lang === DEFAULT_LANG 
      ? `${SITE_URL}${path}` 
      : `${SITE_URL}/${lang}${path}`;
    
    return `    <xhtml:link rel="alternate" hreflang="${lang}" href="${href}" />`;
  }).join('\n') + '\n    <xhtml:link rel="alternate" hreflang="x-default" href="' + SITE_URL + path + '" />';
};

// Define pages to include in sitemap
const pages = [
  { path: '', priority: '1.0', changefreq: 'weekly' },
  { path: '/services', priority: '0.8', changefreq: 'weekly' },
  { path: '/mentoria-online', priority: '0.8', changefreq: 'monthly' },
  { path: '/legal', priority: '0.3', changefreq: 'yearly' },
  { path: '/privacy', priority: '0.3', changefreq: 'yearly' },
  { path: '/terms', priority: '0.3', changefreq: 'yearly' },
  { path: '/cookies', priority: '0.3', changefreq: 'yearly' }
];

// Generate sitemap XML
const generateSitemap = () => {
  const currentDate = getCurrentDate();
  
  let sitemap = `<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">`;

  // Generate URLs for each language and page combination
  LANGUAGES.forEach(lang => {
    const isDefault = lang === DEFAULT_LANG;
    const langPrefix = isDefault ? '' : `/${lang}`;
    
    pages.forEach(page => {
      const url = `${SITE_URL}${langPrefix}${page.path}`;
      const priority = isDefault && page.path === '' ? page.priority : 
                     (isDefault ? page.priority : (parseFloat(page.priority) * 0.9).toFixed(1));
      
      sitemap += `
  <url>
    <loc>${url}</loc>
    <lastmod>${currentDate}</lastmod>
    <changefreq>${page.changefreq}</changefreq>
    <priority>${priority}</priority>
${generateHreflangs(page.path)}
  </url>`;
    });
  });

  sitemap += `
</urlset>`;

  return sitemap;
};

// Write sitemap to public directory
const writeSitemap = () => {
  const sitemapContent = generateSitemap();
  const publicDir = path.join(process.cwd(), 'public');
  
  // Ensure public directory exists
  if (!fs.existsSync(publicDir)) {
    fs.mkdirSync(publicDir, { recursive: true });
  }
  
  // Write sitemap
  fs.writeFileSync(path.join(publicDir, 'sitemap.xml'), sitemapContent);
  console.log('✅ Sitemap generated successfully at public/sitemap.xml');
};

// Execute if run directly
if (import.meta.url === `file://${process.argv[1]}`) {
  writeSitemap();
}

export { generateSitemap, writeSitemap };