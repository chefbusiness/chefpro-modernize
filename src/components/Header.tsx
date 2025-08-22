import { useState } from 'react';
import { Button } from '@/components/ui/button';
import { ChevronDown, Menu, X, Globe } from 'lucide-react';
import { useLanguage, type Language } from '@/hooks/useLanguage';
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
import logoImage from '@/assets/chef-pro-logo.png';

const languages: { code: Language; name: string; flag: string }[] = [
  { code: 'es', name: 'Español', flag: '🇪🇸' },
  { code: 'en', name: 'English', flag: '🇺🇸' },
  { code: 'fr', name: 'Français', flag: '🇫🇷' },
  { code: 'de', name: 'Deutsch', flag: '🇩🇪' },
  { code: 'it', name: 'Italiano', flag: '🇮🇹' },
  { code: 'pt', name: 'Português', flag: '🇵🇹' },
  { code: 'nl', name: 'Nederlands', flag: '🇳🇱' },
];

const Header = () => {
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
      <div className="container flex h-16 items-center justify-between">
        {/* Logo */}
        <div className="flex items-center space-x-2">
          <img src={logoImage} alt="AI Chef Pro" className="h-10 w-10" />
          <span className="text-xl font-bold text-chef-dark">AI Chef Pro</span>
        </div>

        {/* Desktop Navigation */}
        <nav className="hidden md:flex items-center space-x-8">
          <a href="#inicio" className="text-sm font-medium hover:text-chef-gold transition-colors">
            {t.nav.inicio}
          </a>
          <a href="#plataformas" className="text-sm font-medium hover:text-chef-gold transition-colors">
            {t.nav.plataformas}
          </a>
          <a href="#servicios" className="text-sm font-medium hover:text-chef-gold transition-colors">
            {t.nav.servicios}
          </a>
          <a href="#recursos" className="text-sm font-medium hover:text-chef-gold transition-colors">
            {t.nav.recursos}
          </a>
          <a 
            href="https://blog.aichef.pro" 
            target="_blank" 
            rel="noopener noreferrer"
            className="text-sm font-medium hover:text-chef-gold transition-colors"
          >
            {t.nav.blog}
          </a>
          <a href="#contacto" className="text-sm font-medium hover:text-chef-gold transition-colors">
            {t.nav.contacto}
          </a>
        </nav>

        {/* Desktop Actions */}
        <div className="hidden md:flex items-center space-x-4">
          {/* Language Selector */}
          <DropdownMenu>
            <DropdownMenuTrigger asChild>
              <Button variant="outline" size="sm" className="gap-2">
                <Globe className="h-4 w-4" />
                {currentLang?.flag} {currentLang?.name}
                <ChevronDown className="h-4 w-4" />
              </Button>
            </DropdownMenuTrigger>
            <DropdownMenuContent align="end">
              {languages.map((lang) => (
                <DropdownMenuItem
                  key={lang.code}
                  onClick={() => changeLanguage(lang.code)}
                  className="gap-2"
                >
                  {lang.flag} {lang.name}
                </DropdownMenuItem>
              ))}
            </DropdownMenuContent>
          </DropdownMenu>

          <Button 
            variant="outline" 
            onClick={handleLoginClick}
            className="text-sm"
          >
            {t.nav.login}
          </Button>
          
          <Button 
            onClick={handleCTAClick}
            className="chef-cta-button text-sm font-bold animate-glow-pulse"
          >
            {t.cta.primary}
          </Button>
        </div>

        {/* Mobile Menu */}
        <Sheet open={mobileMenuOpen} onOpenChange={setMobileMenuOpen}>
          <SheetTrigger asChild className="md:hidden">
            <Button variant="outline" size="sm">
              <Menu className="h-4 w-4" />
            </Button>
          </SheetTrigger>
          <SheetContent side="right">
            <SheetHeader>
              <SheetTitle className="text-left">AI Chef Pro</SheetTitle>
            </SheetHeader>
            <div className="mt-8 space-y-4">
              <a 
                href="#inicio" 
                className="block py-2 text-sm font-medium hover:text-chef-gold transition-colors"
                onClick={() => setMobileMenuOpen(false)}
              >
                {t.nav.inicio}
              </a>
              <a 
                href="#plataformas" 
                className="block py-2 text-sm font-medium hover:text-chef-gold transition-colors"
                onClick={() => setMobileMenuOpen(false)}
              >
                {t.nav.plataformas}
              </a>
              <a 
                href="#servicios" 
                className="block py-2 text-sm font-medium hover:text-chef-gold transition-colors"
                onClick={() => setMobileMenuOpen(false)}
              >
                {t.nav.servicios}
              </a>
              <a 
                href="#recursos" 
                className="block py-2 text-sm font-medium hover:text-chef-gold transition-colors"
                onClick={() => setMobileMenuOpen(false)}
              >
                {t.nav.recursos}
              </a>
              <a 
                href="https://blog.aichef.pro" 
                target="_blank" 
                rel="noopener noreferrer"
                className="block py-2 text-sm font-medium hover:text-chef-gold transition-colors"
                onClick={() => setMobileMenuOpen(false)}
              >
                {t.nav.blog}
              </a>
              <a 
                href="#contacto" 
                className="block py-2 text-sm font-medium hover:text-chef-gold transition-colors"
                onClick={() => setMobileMenuOpen(false)}
              >
                {t.nav.contacto}
              </a>
              
              <div className="pt-4 space-y-3">
                {/* Mobile Language Selector */}
                <DropdownMenu>
                  <DropdownMenuTrigger asChild>
                    <Button variant="outline" className="w-full justify-between">
                      <span className="flex items-center gap-2">
                        <Globe className="h-4 w-4" />
                        {currentLang?.flag} {currentLang?.name}
                      </span>
                      <ChevronDown className="h-4 w-4" />
                    </Button>
                  </DropdownMenuTrigger>
                  <DropdownMenuContent className="w-full">
                    {languages.map((lang) => (
                      <DropdownMenuItem
                        key={lang.code}
                        onClick={() => changeLanguage(lang.code)}
                        className="gap-2"
                      >
                        {lang.flag} {lang.name}
                      </DropdownMenuItem>
                    ))}
                  </DropdownMenuContent>
                </DropdownMenu>

                <Button 
                  variant="outline" 
                  onClick={handleLoginClick}
                  className="w-full"
                >
                  {t.nav.login}
                </Button>
                
                <Button 
                  onClick={handleCTAClick}
                  className="w-full chef-cta-button animate-glow-pulse"
                >
                  {t.cta.primary}
                </Button>
              </div>
            </div>
          </SheetContent>
        </Sheet>
      </div>
    </header>
  );
};

export default Header;