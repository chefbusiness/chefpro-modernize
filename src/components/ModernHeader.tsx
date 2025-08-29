import { useState } from 'react';
import { Button } from '@/components/ui/button';
import { ChevronDown, Menu, Home, Briefcase, GraduationCap, Palette, Globe2, Settings, Globe, Check } from 'lucide-react';
import { useLanguage, type Language } from '@/hooks/useLanguage';
import {
  NavigationMenu,
  NavigationMenuContent,
  NavigationMenuItem,
  NavigationMenuLink,
  NavigationMenuList,
  NavigationMenuTrigger,
} from '@/components/ui/navigation-menu';
import {
  DropdownMenu,
  DropdownMenuContent,
  DropdownMenuItem,
  DropdownMenuTrigger,
} from '@/components/ui/dropdown-menu';
import {
  Sheet,
  SheetContent,
  SheetHeader,
  SheetTitle,
  SheetTrigger,
} from '@/components/ui/sheet';
import { ScrollArea } from '@/components/ui/scroll-area';
import { Separator } from '@/components/ui/separator';

const languages: { code: Language; name: string; flag: string }[] = [
  { code: 'es', name: 'Español', flag: '🇪🇸' },
  { code: 'en', name: 'English', flag: '🇺🇸' },
  { code: 'fr', name: 'Français', flag: '🇫🇷' },
  { code: 'de', name: 'Deutsch', flag: '🇩🇪' },
  { code: 'it', name: 'Italiano', flag: '🇮🇹' },
  { code: 'pt', name: 'Português', flag: '🇵🇹' },
  { code: 'nl', name: 'Nederlands', flag: '🇳🇱' },
];

export default function ModernHeader() {
  const { currentLanguage, changeLanguage, t, getAppUrl } = useLanguage();
  const [mobileMenuOpen, setMobileMenuOpen] = useState(false);

  const currentLang = languages.find(lang => lang.code === currentLanguage);

  const handleCTAClick = () => {
    window.open(getAppUrl(currentLanguage) + '/pricing', '_blank');
  };

  const handleLoginClick = () => {
    window.open(getAppUrl(currentLanguage), '_blank');
  };

  return (
    <header className="sticky top-0 z-50 w-full border-b bg-background/95 backdrop-blur supports-[backdrop-filter]:bg-background/60">
      <div className="container flex h-14 max-w-screen-2xl items-center">
        <div className="mr-4 flex">
          <a className="mr-6 flex items-center space-x-2" href="/">
            <img 
              src="https://assets.zyrosite.com/AVLbeJ7l3JfrlNJr/logo-ai-chef-pro-24-m2Wp64Vqqwso1ZQN.svg" 
              alt="AI Chef Pro Logo" 
              className="h-8 w-auto"
            />
          </a>
          <NavigationMenu className="hidden md:flex">
            <NavigationMenuList>
              <NavigationMenuItem>
                <NavigationMenuLink 
                  className="transition-colors hover:text-foreground/80 text-foreground/60 px-3 py-2"
                  href="#inicio"
                >
                  {t('nav.inicio')}
                </NavigationMenuLink>
              </NavigationMenuItem>
              
              <NavigationMenuItem>
                <NavigationMenuTrigger className="transition-colors hover:text-foreground/80 text-foreground/60">
                  {t('nav.servicios')}
                </NavigationMenuTrigger>
                <NavigationMenuContent>
                  <div className="grid w-[400px] gap-3 p-4 md:grid-cols-1">
                    <div className="space-y-2">
                      <h4 className="font-medium leading-none text-accent">{t('nav.servicios')}</h4>
                      <div className="grid gap-1">
                        <NavigationMenuLink 
                          className="block text-sm text-muted-foreground hover:text-foreground transition-colors py-1"
                          href={currentLanguage === 'es' ? '/mentoria-online' : `/${currentLanguage}/mentoria-online`}
                        >
                          {t('nav.mentoria_online')}
                        </NavigationMenuLink>
                      </div>
                    </div>
                  </div>
                </NavigationMenuContent>
              </NavigationMenuItem>
              
              <NavigationMenuItem>
                <NavigationMenuTrigger className="transition-colors hover:text-foreground/80 text-foreground/60">
                  {t('nav.aplicaciones')}
                </NavigationMenuTrigger>
                <NavigationMenuContent>
                  <div className="grid w-[600px] gap-3 p-4 md:grid-cols-3">
                    <div className="space-y-2">
                      <h4 className="font-medium leading-none text-accent">{t('categories_labels.creatividad')}</h4>
                      <div className="grid gap-1">
                        <NavigationMenuLink 
                          className="block text-sm text-muted-foreground hover:text-foreground transition-colors py-1"
                          href="#showcase-creatividad"
                        >
                          {t('nav.creatividad')}
                        </NavigationMenuLink>
                        <NavigationMenuLink 
                          className="block text-sm text-muted-foreground hover:text-foreground transition-colors py-1"
                          href="#showcase-creatividad"
                        >
                          {t('apps.creativity.pasteleria_creativa.name')}
                        </NavigationMenuLink>
                        <NavigationMenuLink 
                          className="block text-sm text-muted-foreground hover:text-foreground transition-colors py-1"
                          href="#showcase-creatividad"
                        >
                          {t('apps.creativity.food_pairing.name')}
                        </NavigationMenuLink>
                      </div>
                    </div>
                    <div className="space-y-2">
                      <h4 className="font-medium leading-none text-accent">{t('categories_labels.recetarios')}</h4>
                      <div className="grid gap-1">
                        <NavigationMenuLink 
                          className="block text-sm text-muted-foreground hover:text-foreground transition-colors py-1"
                          href="#recetarios"
                        >
                          {t('categories.world_cookbooks.europa.name')} ({t('categories.world_cookbooks.europa.count').replace(/\D/g, '')})
                        </NavigationMenuLink>
                        <NavigationMenuLink 
                          className="block text-sm text-muted-foreground hover:text-foreground transition-colors py-1"
                          href="#recetarios"
                        >
                          {t('categories.world_cookbooks.latinoamerica.name')} ({t('categories.world_cookbooks.latinoamerica.count').replace(/\D/g, '')})
                        </NavigationMenuLink>
                        <NavigationMenuLink 
                          className="block text-sm text-muted-foreground hover:text-foreground transition-colors py-1"
                          href="#recetarios"
                        >
                          {t('categories.world_cookbooks.asia.name')} ({t('categories.world_cookbooks.asia.count').replace(/\D/g, '')})
                        </NavigationMenuLink>
                      </div>
                    </div>
                    <div className="space-y-2">
                      <h4 className="font-medium leading-none text-accent">{t('showcase.business_title')}</h4>
                      <div className="grid gap-1">
                        <NavigationMenuLink 
                          className="block text-sm text-muted-foreground hover:text-foreground transition-colors py-1"
                          href="#herramientas-business"
                        >
                          {t('apps.business.mermas_gencal.name')}
                        </NavigationMenuLink>
                        <NavigationMenuLink 
                          className="block text-sm text-muted-foreground hover:text-foreground transition-colors py-1"
                          href="#herramientas-business"
                        >
                          {t('apps.business.id_alergenos.name')}
                        </NavigationMenuLink>
                        <NavigationMenuLink 
                          className="block text-sm text-muted-foreground hover:text-foreground transition-colors py-1"
                          href="#herramientas-business"
                        >
                          {t('apps.business.mental_coach.name')}
                        </NavigationMenuLink>
                      </div>
                    </div>
                  </div>
                </NavigationMenuContent>
              </NavigationMenuItem>
              
              <NavigationMenuItem>
                <NavigationMenuLink 
                  className="transition-colors hover:text-foreground/80 text-foreground/60 px-3 py-2"
                  href="#pricing"
                >
                  {t('nav.precios')}
                </NavigationMenuLink>
              </NavigationMenuItem>
              
              <NavigationMenuItem>
                <NavigationMenuLink 
                  className="transition-colors hover:text-foreground/80 text-foreground/60 px-3 py-2"
                  href="https://blog.aichef.pro"
                  target="_blank"
                  rel="noopener noreferrer"
                >
                  {t('nav.blog')}
                </NavigationMenuLink>
              </NavigationMenuItem>
            </NavigationMenuList>
          </NavigationMenu>
        </div>
        <div className="flex flex-1 items-center justify-between space-x-2 md:justify-end">
          <div className="w-full flex-1 md:w-auto md:flex-none">
            {/* Search would go here if needed */}
          </div>
          <nav className="flex items-center gap-2">
            <DropdownMenu>
              <DropdownMenuTrigger asChild>
                <Button variant="ghost" size="sm" className="h-8 px-2">
                  {currentLang?.name}
                  <ChevronDown className="h-4 w-4" />
                </Button>
              </DropdownMenuTrigger>
              <DropdownMenuContent 
                align="end" 
                className="bg-popover border border-border shadow-lg z-[100] min-w-[100px]"
              >
                {languages.map((lang) => (
                  <DropdownMenuItem
                    key={lang.code}
                    onClick={() => changeLanguage(lang.code)}
                    className="hover:bg-accent hover:text-accent-foreground cursor-pointer focus:bg-accent focus:text-accent-foreground"
                  >
                    {lang.name}
                  </DropdownMenuItem>
                ))}
              </DropdownMenuContent>
            </DropdownMenu>
            
            <Button 
              variant="ghost" 
              size="sm" 
              onClick={handleLoginClick}
              className="hidden md:inline-flex"
            >
              {t('nav.login')}
            </Button>
            
            <Button 
              size="sm" 
              onClick={handleCTAClick}
              className="bg-primary text-primary-foreground hover:bg-primary/90 hidden md:inline-flex"
            >
              {t('cta.primary')}
            </Button>

            <Sheet open={mobileMenuOpen} onOpenChange={setMobileMenuOpen}>
              <SheetTrigger asChild>
                <Button variant="ghost" size="sm" className="md:hidden">
                  <Menu className="h-5 w-5" />
                </Button>
              </SheetTrigger>
              <SheetContent 
                side="right" 
                className="p-0 w-full sm:max-w-sm bg-card/95 backdrop-blur-lg border-l rounded-l-2xl"
              >
                {/* Header */}
                <div className="sticky top-0 z-10 bg-card/95 backdrop-blur-sm border-b px-6 py-4">
                  <div className="flex items-center gap-3">
                    <img 
                      src="https://assets.zyrosite.com/AVLbeJ7l3JfrlNJr/logo-ai-chef-pro-24-m2Wp64Vqqwso1ZQN.svg" 
                      alt="AI Chef Pro" 
                      className="h-8 w-8" 
                    />
                    <span className="font-bold text-lg">AI Chef Pro</span>
                  </div>
                </div>

                {/* Scrollable Content */}
                <ScrollArea className="flex-1" style={{ height: 'calc(100vh - 140px)' }}>
                  <nav className="p-6 space-y-6">
                    {/* Main Navigation */}
                    <div className="space-y-1">
                      <a
                        href="#inicio"
                        onClick={() => setMobileMenuOpen(false)}
                        className="flex items-center gap-3 px-3 py-3 text-base font-medium rounded-lg hover:bg-accent/50 focus:bg-accent/50 transition-colors touch-manipulation"
                      >
                        <Home className="h-5 w-5 text-muted-foreground" />
                        {t('nav.inicio')}
                      </a>
                      <a
                        href={currentLanguage === 'es' ? '/servicios' : `/${currentLanguage}/servicios`}
                        onClick={() => setMobileMenuOpen(false)}
                        className="flex items-center gap-3 px-3 py-3 text-base font-medium rounded-lg hover:bg-accent/50 focus:bg-accent/50 transition-colors touch-manipulation"
                      >
                        <Briefcase className="h-5 w-5 text-muted-foreground" />
                        {t('nav.servicios')}
                      </a>
                      <a
                        href={currentLanguage === 'es' ? '/mentoria-online' : `/${currentLanguage}/mentoria-online`}
                        onClick={() => setMobileMenuOpen(false)}
                        className="flex items-center gap-3 px-3 py-3 text-base font-medium rounded-lg hover:bg-accent/50 focus:bg-accent/50 transition-colors touch-manipulation"
                      >
                        <GraduationCap className="h-5 w-5 text-muted-foreground" />
                        {t('nav.mentoria_online')}
                      </a>
                      <a
                        href="#pricing"
                        onClick={() => setMobileMenuOpen(false)}
                        className="flex items-center gap-3 px-3 py-3 text-base font-medium rounded-lg hover:bg-accent/50 focus:bg-accent/50 transition-colors touch-manipulation"
                      >
                        <Settings className="h-5 w-5 text-muted-foreground" />
                        {t('nav.precios')}
                      </a>
                      <a
                        href="https://blog.aichef.pro"
                        target="_blank"
                        rel="noopener noreferrer"
                        onClick={() => setMobileMenuOpen(false)}
                        className="flex items-center gap-3 px-3 py-3 text-base font-medium rounded-lg hover:bg-accent/50 focus:bg-accent/50 transition-colors touch-manipulation"
                      >
                        <Globe2 className="h-5 w-5 text-muted-foreground" />
                        {t('nav.blog')}
                      </a>
                    </div>

                    <Separator />

                    {/* Applications Section */}
                    <div className="space-y-3">
                      <h3 className="text-xs font-semibold text-muted-foreground uppercase tracking-wider px-3">
                        {t('nav.aplicaciones')}
                      </h3>
                      <div className="space-y-1">
                        <a
                          href="#showcase-creatividad"
                          onClick={() => setMobileMenuOpen(false)}
                          className="flex items-center gap-3 px-3 py-3 text-sm font-medium rounded-lg hover:bg-accent/50 focus:bg-accent/50 transition-colors touch-manipulation"
                        >
                          <Palette className="h-4 w-4 text-muted-foreground" />
                          {t('nav.creatividad')}
                        </a>
                        <a
                          href="#recetarios"
                          onClick={() => setMobileMenuOpen(false)}
                          className="flex items-center gap-3 px-3 py-3 text-sm font-medium rounded-lg hover:bg-accent/50 focus:bg-accent/50 transition-colors touch-manipulation"
                        >
                          <Globe2 className="h-4 w-4 text-muted-foreground" />
                          {t('nav.recetarios')}
                        </a>
                        <a
                          href="#herramientas-business"
                          onClick={() => setMobileMenuOpen(false)}
                          className="flex items-center gap-3 px-3 py-3 text-sm font-medium rounded-lg hover:bg-accent/50 focus:bg-accent/50 transition-colors touch-manipulation"
                        >
                          <Settings className="h-4 w-4 text-muted-foreground" />
                          {t('nav.herramientas')}
                        </a>
                        <a
                          href="#filtro-apps"
                          onClick={() => setMobileMenuOpen(false)}
                          className="flex items-center gap-3 px-3 py-3 text-sm font-medium rounded-lg hover:bg-accent/50 focus:bg-accent/50 transition-colors touch-manipulation"
                        >
                          <Settings className="h-4 w-4 text-muted-foreground" />
                          {t('finder.title_prefix')} {t('finder.title_highlight')}
                        </a>
                      </div>
                    </div>

                    <Separator />

                    {/* Language Selector */}
                    <div className="space-y-3">
                      <h3 className="text-xs font-semibold text-muted-foreground uppercase tracking-wider px-3">
                        Idioma / Language
                      </h3>
                      <DropdownMenu>
                        <DropdownMenuTrigger asChild>
                          <Button variant="ghost" className="w-full justify-start gap-3 px-3 py-3 h-auto">
                            <Globe className="h-4 w-4" />
                            <span className="flex items-center gap-2">
                              <span className="text-lg">{languages.find(lang => lang.code === currentLanguage)?.flag}</span>
                              {languages.find(lang => lang.code === currentLanguage)?.name}
                            </span>
                            <ChevronDown className="ml-auto h-4 w-4" />
                          </Button>
                        </DropdownMenuTrigger>
                        <DropdownMenuContent align="start" className="w-56">
                          {languages.map((language) => (
                            <DropdownMenuItem
                              key={language.code}
                              onClick={() => {
                                changeLanguage(language.code);
                                setMobileMenuOpen(false);
                              }}
                              className="flex items-center gap-3 py-2"
                            >
                              <span className="text-lg">{language.flag}</span>
                              {language.name}
                              {currentLanguage === language.code && (
                                <Check className="ml-auto h-4 w-4" />
                              )}
                            </DropdownMenuItem>
                          ))}
                        </DropdownMenuContent>
                      </DropdownMenu>
                    </div>
                  </nav>
                </ScrollArea>

                {/* Sticky Footer */}
                <div className="sticky bottom-0 bg-card/95 backdrop-blur-sm border-t p-6" style={{ paddingBottom: 'max(24px, env(safe-area-inset-bottom))' }}>
                  <div className="flex gap-3">
                    <Button variant="outline" size="lg" onClick={handleLoginClick} className="flex-1 h-12">
                      {t('nav.login')}
                    </Button>
                    <Button size="lg" onClick={handleCTAClick} className="flex-1 h-12">
                      {t('cta.primary')}
                    </Button>
                  </div>
                </div>
              </SheetContent>
            </Sheet>
          </nav>
        </div>
      </div>
    </header>
  );
}