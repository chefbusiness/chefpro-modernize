import { Button } from '@/components/ui/button';
import { Input } from '@/components/ui/input';
import { Separator } from '@/components/ui/separator';
import { Facebook, Instagram, Twitter, Youtube, Music } from 'lucide-react';
import { useLanguage } from '@/hooks/useLanguage';
import logoAiChefPro from '@/assets/logo-ai-chef-pro.svg';

const AI_TOOLS_SLUGS: Record<string, string> = {
  es: 'herramientas-ia-para-restaurantes',
  en: 'en/ai-tools-for-restaurants',
  fr: 'fr/outils-ia-restaurant',
  de: 'de/ki-tools-restaurant',
  it: 'it/strumenti-ia-ristorante',
  pt: 'pt/ferramentas-ia-restaurante',
  nl: 'nl/ai-tools-restaurant',
};

const COSTES_SLUGS: Record<string, string> = {
  es: 'reducir-costes-restaurante-ia',
  en: 'en/reduce-restaurant-costs-ai',
  fr: 'fr/reduire-couts-restaurant-ia',
  de: 'de/restaurantkosten-senken-ki',
  it: 'it/ridurre-costi-ristorante-ia',
  pt: 'pt/reduzir-custos-restaurante-ia',
  nl: 'nl/restaurantkosten-verlagen-ai',
};

const MENU_SLUGS: Record<string, string> = {
  es: 'carta-menu-restaurante-ia',
  en: 'en/restaurant-menu-ai',
  fr: 'fr/carte-menu-restaurant-ia',
  de: 'de/speisekarte-restaurant-ki',
  it: 'it/menu-ristorante-ia',
  pt: 'pt/cardapio-restaurante-ia',
  nl: 'nl/restaurantmenu-ai',
};

const MARKETING_SLUGS: Record<string, string> = {
  es: 'marketing-restaurante-ia',
  en: 'en/restaurant-marketing-ai',
  fr: 'fr/marketing-restaurant-ia',
  de: 'de/restaurant-marketing-ki',
  it: 'it/marketing-ristorante-ia',
  pt: 'pt/marketing-restaurante-ia-pt',
  nl: 'nl/restaurant-marketing-ai-nl',
};

const CHATGPT_SLUGS: Record<string, string> = {
  es: 'chatgpt-para-restaurantes',
  en: 'en/chatgpt-for-restaurants',
  fr: 'fr/chatgpt-pour-restaurants',
  de: 'de/chatgpt-fuer-restaurants',
  it: 'it/chatgpt-per-ristoranti',
  pt: 'pt/chatgpt-para-restaurantes',
  nl: 'nl/chatgpt-voor-restaurants',
};

const RECETAS_SLUGS: Record<string, string> = {
  es: 'recetas-ia-restaurantes',
  en: 'ai-recipes-for-restaurants',
  fr: 'fr/recettes-ia-restaurants',
  de: 'de/ki-rezepte-restaurants',
  it: 'it/ricette-ia-ristoranti',
  pt: 'pt/receitas-ia-restaurantes',
  nl: 'nl/ai-recepten-restaurants',
};

const SOFTWARE_GESTION_SLUGS: Record<string, string> = {
  es: 'software-gestion-cocina-ia',
  en: 'en/kitchen-management-software-ai',
  fr: 'fr/logiciel-gestion-cuisine-ia',
  de: 'de/kuechenverwaltung-ki',
  it: 'it/software-gestione-cucina-ia',
  pt: 'pt/software-gestao-cozinha-ia',
  nl: 'nl/keuken-software-ai',
};

const ESCANDALLOS_SLUGS: Record<string, string> = {
  es: 'escandallos-restaurante-ia',
  en: 'en/food-cost-calculator-restaurant-ai',
  fr: 'fr/calcul-food-cost-restaurant-ia',
  de: 'de/food-cost-rechner-restaurant-ki',
  it: 'it/food-cost-ristorante-ia',
  pt: 'pt/escandallo-restaurante-ia',
  nl: 'nl/food-cost-berekening-restaurant-ai',
};

const MENTORIA_SLUGS: Record<string, string> = {
  es: 'mentoria-online',
  en: 'en/mentoria-online',
  fr: 'fr/mentoria-online',
  de: 'de/mentoria-online',
  it: 'it/mentoria-online',
  pt: 'pt/mentoria-online',
  nl: 'nl/mentoria-online',
};

export default function ModernFooter() {
  const { getAppUrl, currentLanguage, t } = useLanguage();

  const handleNewsletterSubmit = (e: React.FormEvent) => {
    e.preventDefault();
  };

  const legalHref = (slug: string) =>
    currentLanguage === 'es' ? `/${slug}` : `/${currentLanguage}/${slug}`;

  const START_YEAR = 2024;
  const currentYear = new Date().getFullYear();
  const yearText = START_YEAR === currentYear ? `${currentYear}` : `${START_YEAR} - ${currentYear}`;

  const lang = currentLanguage;

  return (
    <footer className="border-t bg-background">
      <div className="container py-14">

        {/* Top section: Brand + Newsletter */}
        <div className="grid grid-cols-1 gap-8 lg:grid-cols-3 mb-12">
          {/* Brand */}
          <div>
            <div className="flex items-center space-x-2">
              <img
                src={logoAiChefPro}
                alt="AI Chef Pro Logo"
                className="h-8 w-auto"
              />
            </div>
            <p
              className="mt-4 text-sm text-muted-foreground max-w-md"
              dangerouslySetInnerHTML={{ __html: t('footer.brand_desc') }}
            />
            <p className="mt-2 text-xs text-muted-foreground">
              {t('footer.suite_desc')}
            </p>
          </div>

          {/* Newsletter */}
          <div className="lg:col-span-2">
            <h4 className="text-sm font-semibold">{t('footer.newsletter_title')}</h4>
            <form onSubmit={handleNewsletterSubmit} className="mt-3 flex max-w-md gap-2">
              <Input
                type="email"
                placeholder={t('footer.newsletter_placeholder')}
                className="flex-1"
              />
              <Button type="submit" size="sm">
                {t('footer.newsletter_button')}
              </Button>
            </form>
          </div>
        </div>

        {/* Links section: 5 columns */}
        <div className="grid grid-cols-2 gap-8 md:grid-cols-3 lg:grid-cols-5">

          {/* Col 1 – IA PARA RESTAURANTES */}
          <div>
            <h4 className="text-sm font-semibold uppercase tracking-wide mb-4">
              {t('footer.section_ia')}
            </h4>
            <ul className="space-y-3 text-sm">
              <li>
                <a
                  href={`/${AI_TOOLS_SLUGS[lang] || AI_TOOLS_SLUGS.es}`}
                  className="text-primary hover:text-primary/80 transition-colors font-medium"
                >
                  {t('footer.nav_ai_tools')}
                </a>
              </li>
              <li>
                <a
                  href={`/${COSTES_SLUGS[lang] || COSTES_SLUGS.es}`}
                  className="text-red-600 hover:text-red-500 transition-colors font-medium"
                >
                  {t('footer.nav_costs')}
                </a>
              </li>
              <li>
                <a
                  href={`/${MENU_SLUGS[lang] || MENU_SLUGS.es}`}
                  className="text-emerald-600 hover:text-emerald-500 transition-colors font-medium"
                >
                  {t('footer.nav_menu')}
                </a>
              </li>
              <li>
                <a
                  href={`/${MARKETING_SLUGS[lang] || MARKETING_SLUGS.es}`}
                  className="text-violet-600 hover:text-violet-500 transition-colors font-medium"
                >
                  {t('footer.nav_marketing')}
                </a>
              </li>
              <li>
                <a
                  href={`/${CHATGPT_SLUGS[lang] || CHATGPT_SLUGS.es}`}
                  className="text-indigo-600 hover:text-indigo-500 transition-colors font-medium"
                >
                  {t('footer.nav_chatgpt')}
                </a>
              </li>
              <li>
                <a
                  href={`/${SOFTWARE_GESTION_SLUGS[lang] || SOFTWARE_GESTION_SLUGS.es}`}
                  className="text-emerald-600 hover:text-emerald-500 transition-colors font-medium"
                >
                  {t('footer.nav_software_gestion')}
                </a>
              </li>
              <li>
                <a
                  href={`/${RECETAS_SLUGS[lang] || RECETAS_SLUGS.es}`}
                  className="text-amber-600 hover:text-amber-500 transition-colors font-medium"
                >
                  {t('footer.nav_recetas')}
                </a>
              </li>
              <li>
                <a
                  href={`/${ESCANDALLOS_SLUGS[lang] || ESCANDALLOS_SLUGS.es}`}
                  className="text-rose-600 hover:text-rose-500 transition-colors font-medium"
                >
                  {t('footer.nav_escandallos')}
                </a>
              </li>
            </ul>
          </div>

          {/* Col 2 – FORMACIÓN */}
          <div>
            <h4 className="text-sm font-semibold uppercase tracking-wide mb-4">
              {t('footer.section_formacion')}
            </h4>
            <ul className="space-y-3 text-sm">
              <li>
                <a
                  href={`/${MENTORIA_SLUGS[lang] || MENTORIA_SLUGS.es}`}
                  className="text-muted-foreground hover:text-foreground transition-colors"
                >
                  {t('footer.mentoria_online')}
                </a>
              </li>
              <li>
                <a
                  href="/formacion-presencial"
                  className="text-muted-foreground hover:text-foreground transition-colors"
                >
                  {t('footer.formacion_presencial')}
                </a>
              </li>
              <li>
                <a
                  href={getAppUrl(lang) + '/pricing'}
                  target="_blank"
                  rel="noopener noreferrer"
                  className="text-muted-foreground hover:text-foreground transition-colors"
                >
                  {t('footer.planes_precios')}
                </a>
              </li>
            </ul>
          </div>

          {/* Col 3 – RECURSOS */}
          <div>
            <h4 className="text-sm font-semibold uppercase tracking-wide mb-4">
              {t('footer.section_recursos')}
            </h4>
            <ul className="space-y-3 text-sm">
              <li>
                <a
                  href={currentLanguage === 'en' ? 'https://enblog.aichef.pro/' : 'https://blog.aichef.pro'}
                  target="_blank"
                  rel="noopener noreferrer"
                  className="text-muted-foreground hover:text-foreground transition-colors"
                >
                  {t('footer.blog_main')}
                </a>
              </li>
              <li>
                <a
                  href="https://blog.aichef.pro/tutoriales/"
                  target="_blank"
                  rel="noopener noreferrer"
                  className="text-muted-foreground hover:text-foreground transition-colors"
                >
                  {t('footer.tutoriales')}
                </a>
              </li>
              <li>
                <a
                  href="https://blog.aichef.pro/libreria-de-prompts/"
                  target="_blank"
                  rel="noopener noreferrer"
                  className="text-muted-foreground hover:text-foreground transition-colors"
                >
                  {t('footer.prompts_library')}
                </a>
              </li>
              <li>
                <a
                  href="https://blog.aichef.pro/recetario-pro-ai/"
                  target="_blank"
                  rel="noopener noreferrer"
                  className="text-muted-foreground hover:text-foreground transition-colors"
                >
                  {t('footer.recetario')}
                </a>
              </li>
              <li>
                <a
                  href="https://blog.aichef.pro/glosario-y-lexico-ai/"
                  target="_blank"
                  rel="noopener noreferrer"
                  className="text-muted-foreground hover:text-foreground transition-colors"
                >
                  {t('footer.glosario_ia')}
                </a>
              </li>
              <li>
                <a
                  href="https://blog.aichef.pro/glosario-y-lexico-cientifico-culinario/"
                  target="_blank"
                  rel="noopener noreferrer"
                  className="text-muted-foreground hover:text-foreground transition-colors"
                >
                  {t('footer.glosario_culinario')}
                </a>
              </li>
              <li>
                <a
                  href="https://blog.aichef.pro/roadmap/"
                  target="_blank"
                  rel="noopener noreferrer"
                  className="text-muted-foreground hover:text-foreground transition-colors"
                >
                  {t('footer.roadmap')}
                </a>
              </li>
            </ul>
          </div>

          {/* Col 4 – HERRAMIENTAS */}
          <div>
            <h4 className="text-sm font-semibold uppercase tracking-wide mb-4">
              {t('footer.section_herramientas')}
            </h4>
            <ul className="space-y-3 text-sm">
              <li>
                <a
                  href={getAppUrl(lang)}
                  target="_blank"
                  rel="noopener noreferrer"
                  className="text-muted-foreground hover:text-foreground transition-colors"
                >
                  {t('footer.app_tools')}
                </a>
              </li>
              <li>
                <a
                  href="/herramientas-gratuitas"
                  className="text-muted-foreground hover:text-foreground transition-colors"
                >
                  {t('footer.free_tools_hub')}
                </a>
              </li>
              <li>
                <a
                  href={`/${AI_TOOLS_SLUGS[lang] || AI_TOOLS_SLUGS.es}`}
                  className="text-muted-foreground hover:text-foreground transition-colors"
                >
                  {t('footer.nav_ai_tools')}
                </a>
              </li>
              <li>
                <a
                  href={getAppUrl(lang)}
                  target="_blank"
                  rel="noopener noreferrer"
                  className="text-muted-foreground hover:text-foreground transition-colors"
                >
                  {t('footer.app_login')}
                </a>
              </li>
            </ul>
          </div>

          {/* Col 5 – EMPRESA */}
          <div>
            <h4 className="text-sm font-semibold uppercase tracking-wide mb-4">
              {t('footer.section_empresa')}
            </h4>
            <ul className="space-y-3 text-sm">
              <li>
                <a
                  href="https://chefbusiness.co/"
                  target="_blank"
                  rel="noopener noreferrer"
                  className="text-muted-foreground hover:text-foreground transition-colors"
                >
                  ChefBusiness.co
                </a>
              </li>
              <li>
                <a
                  href="https://gastroseo.com/"
                  target="_blank"
                  rel="noopener noreferrer"
                  className="text-muted-foreground hover:text-foreground transition-colors"
                >
                  GastroSEO.com
                </a>
              </li>
              <li>
                <a
                  href="https://gastrolocal.pro/"
                  target="_blank"
                  rel="noopener noreferrer"
                  className="text-muted-foreground hover:text-foreground transition-colors"
                >
                  GastroLocal.pro
                </a>
              </li>
              <li>
                <a
                  href="https://hosply.pro/"
                  target="_blank"
                  rel="noopener noreferrer"
                  className="text-muted-foreground hover:text-foreground transition-colors"
                >
                  Hosply.pro
                </a>
              </li>
              <li>
                <a
                  href="mailto:info@aichef.pro"
                  className="text-muted-foreground hover:text-foreground transition-colors"
                >
                  info@aichef.pro
                </a>
              </li>
              <li>
                <a
                  href="tel:+34744717942"
                  className="text-muted-foreground hover:text-foreground transition-colors"
                >
                  +34 744 717 942
                </a>
              </li>
            </ul>
          </div>
        </div>

        <Separator className="my-8" />

        {/* Payment methods */}
        <div className="mb-6">
          <p className="text-xs text-muted-foreground mb-3">{t('footer.payment_methods')}</p>
          <div className="flex flex-wrap items-center gap-2">
            {/* Visa */}
            <div className="flex items-center justify-center h-8 px-2 rounded border border-border bg-white dark:bg-slate-800">
              <svg viewBox="0 0 48 32" className="h-5 w-auto" aria-label="Visa">
                <rect width="48" height="32" rx="4" fill="white"/>
                <text x="24" y="22" textAnchor="middle" fontFamily="Arial,sans-serif" fontWeight="bold" fontSize="14" fill="#1A1F71" letterSpacing="1">VISA</text>
              </svg>
            </div>
            {/* Mastercard */}
            <div className="flex items-center justify-center h-8 px-2 rounded border border-border bg-white dark:bg-slate-800">
              <svg viewBox="0 0 48 32" className="h-5 w-auto" aria-label="Mastercard">
                <rect width="48" height="32" rx="4" fill="white"/>
                <circle cx="19" cy="16" r="9" fill="#EB001B"/>
                <circle cx="29" cy="16" r="9" fill="#F79E1B"/>
                <path d="M24 9.27a9 9 0 0 1 0 13.46A9 9 0 0 1 24 9.27z" fill="#FF5F00"/>
              </svg>
            </div>
            {/* American Express */}
            <div className="flex items-center justify-center h-8 px-2 rounded border border-border bg-white dark:bg-slate-800">
              <svg viewBox="0 0 48 32" className="h-5 w-auto" aria-label="American Express">
                <rect width="48" height="32" rx="4" fill="#2E77BC"/>
                <text x="24" y="20" textAnchor="middle" fontFamily="Arial,sans-serif" fontWeight="bold" fontSize="7" fill="white" letterSpacing="0.5">AMERICAN</text>
                <text x="24" y="27" textAnchor="middle" fontFamily="Arial,sans-serif" fontWeight="bold" fontSize="7" fill="white" letterSpacing="0.5">EXPRESS</text>
              </svg>
            </div>
            {/* Google Pay */}
            <div className="flex items-center justify-center h-8 px-2 rounded border border-border bg-white dark:bg-slate-800">
              <svg viewBox="0 0 64 32" className="h-5 w-auto" aria-label="Google Pay">
                <rect width="64" height="32" rx="4" fill="white"/>
                <text x="32" y="21" textAnchor="middle" fontFamily="Arial,sans-serif" fontSize="11" fill="#3C4043" fontWeight="500">
                  <tspan fill="#4285F4">G</tspan>
                  <tspan fill="#3C4043">Pay</tspan>
                </text>
              </svg>
            </div>
            {/* Apple Pay */}
            <div className="flex items-center justify-center h-8 px-2 rounded border border-border bg-white dark:bg-slate-800">
              <svg viewBox="0 0 64 32" className="h-5 w-auto" aria-label="Apple Pay">
                <rect width="64" height="32" rx="4" fill="white"/>
                <text x="32" y="21" textAnchor="middle" fontFamily="-apple-system,Arial,sans-serif" fontSize="11" fill="#000000" fontWeight="500"> Pay</text>
                <text x="18" y="21" textAnchor="middle" fontFamily="-apple-system,Arial,sans-serif" fontSize="13" fill="#000000"></text>
              </svg>
            </div>
            {/* Stripe badge */}
            <div className="flex items-center justify-center h-8 px-2 rounded border border-border bg-white dark:bg-slate-800">
              <svg viewBox="0 0 48 32" className="h-5 w-auto" aria-label="Stripe">
                <rect width="48" height="32" rx="4" fill="white"/>
                <text x="24" y="21" textAnchor="middle" fontFamily="Arial,sans-serif" fontWeight="bold" fontSize="12" fill="#635BFF">stripe</text>
              </svg>
            </div>
          </div>
        </div>

        {/* Bottom bar: copyright + legal + social */}
        <div className="flex flex-col items-center justify-between gap-4 md:flex-row">
          <div className="flex flex-wrap items-center justify-center md:justify-start gap-x-4 gap-y-2 text-center text-sm text-muted-foreground md:text-left">
            <span>© {yearText}. All rights reserved.</span>
            <a href={legalHref('legales')} className="hover:text-foreground transition-colors">{t('footer.legal')}</a>
            <a href={legalHref('privacidad')} className="hover:text-foreground transition-colors">{t('footer.privacy')}</a>
            <a href={legalHref('terminos')} className="hover:text-foreground transition-colors">{t('footer.terms')}</a>
            <a href={legalHref('cookies')} className="hover:text-foreground transition-colors">{t('footer.cookies')}</a>
          </div>

          <div className="flex items-center space-x-3">
            <a
              href="https://www.facebook.com/profile.php?id=61565177312061"
              target="_blank"
              rel="noopener noreferrer"
              className="text-muted-foreground hover:text-foreground transition-colors"
              aria-label="Facebook"
            >
              <Facebook className="h-4 w-4" />
            </a>
            <a
              href="https://www.instagram.com/aichefpro"
              target="_blank"
              rel="noopener noreferrer"
              className="text-muted-foreground hover:text-foreground transition-colors"
              aria-label="Instagram"
            >
              <Instagram className="h-4 w-4" />
            </a>
            <a
              href="https://x.com/aichefpro"
              target="_blank"
              rel="noopener noreferrer"
              className="text-muted-foreground hover:text-foreground transition-colors"
              aria-label="X / Twitter"
            >
              <Twitter className="h-4 w-4" />
            </a>
            <a
              href="https://tiktok.com/aichefpro"
              target="_blank"
              rel="noopener noreferrer"
              className="text-muted-foreground hover:text-foreground transition-colors"
              aria-label="TikTok"
            >
              <Music className="h-4 w-4" />
            </a>
            <a
              href="https://youtube.com/playlist?list=PLkevVb6pg5bs3b2hlwI8-2wW7juXV-eFj&si=eGAgpRRE0h6zfH1S"
              target="_blank"
              rel="noopener noreferrer"
              className="text-muted-foreground hover:text-foreground transition-colors"
              aria-label="YouTube"
            >
              <Youtube className="h-4 w-4" />
            </a>
          </div>
        </div>

      </div>
    </footer>
  );
}
