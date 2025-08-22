import { useState } from 'react';
import { Button } from '@/components/ui/button';
import { ChevronDown, Menu } from 'lucide-react';
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

const languages: { code: Language; name: string }[] = [
  { code: 'es', name: 'ES' },
  { code: 'en', name: 'EN' },
  { code: 'fr', name: 'FR' },
  { code: 'de', name: 'DE' },
  { code: 'it', name: 'IT' },
  { code: 'pt', name: 'PT' },
  { code: 'nl', name: 'NL' },
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
            <div className="h-6 w-6 rounded bg-primary" />
            <span className="font-bold">AI Chef Pro</span>
          </a>
          <nav className="hidden md:flex items-center gap-6 text-sm">
            <a
              className="transition-colors hover:text-foreground/80 text-foreground/60"
              href="#docs"
            >
              {t.nav.inicio}
            </a>
            <a
              className="transition-colors hover:text-foreground/80 text-foreground/60"
              href="#components"
            >
              Herramientas
            </a>
            <a
              className="transition-colors hover:text-foreground/80 text-foreground/60"
              href="#pricing"
            >
              Precios
            </a>
            <a
              className="transition-colors hover:text-foreground/80 text-foreground/60"
              href="https://blog.aichef.pro"
              target="_blank"
            >
              {t.nav.blog}
            </a>
          </nav>
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
              Login
            </Button>
            
            <Button 
              size="sm" 
              onClick={handleCTAClick}
              className="bg-primary text-primary-foreground hover:bg-primary/90 hidden md:inline-flex"
            >
              {t.cta.primary}
            </Button>

            <Sheet open={mobileMenuOpen} onOpenChange={setMobileMenuOpen}>
              <SheetTrigger asChild>
                <Button variant="ghost" size="sm" className="md:hidden">
                  <Menu className="h-5 w-5" />
                </Button>
              </SheetTrigger>
              <SheetContent side="right" className="pr-0">
                <SheetHeader>
                  <SheetTitle>Menu</SheetTitle>
                </SheetHeader>
                <div className="my-4 h-[calc(100vh-8rem)] pb-10 pl-6">
                  <div className="flex flex-col space-y-3">
                    <a href="#docs" className="font-medium">
                      {t.nav.inicio}
                    </a>
                    <a href="#components" className="font-medium">
                      Herramientas
                    </a>
                    <a href="#pricing" className="font-medium">
                      Precios
                    </a>
                    <a href="https://blog.aichef.pro" target="_blank" className="font-medium">
                      {t.nav.blog}
                    </a>
                  </div>
                  <div className="mt-6 space-y-3">
                    <DropdownMenu>
                      <DropdownMenuTrigger asChild>
                        <Button variant="outline" className="w-full justify-between">
                          <span>
                            {currentLang?.name}
                          </span>
                          <ChevronDown className="h-4 w-4" />
                        </Button>
                      </DropdownMenuTrigger>
                      <DropdownMenuContent className="w-full bg-popover border border-border shadow-lg z-[100]">
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
                      variant="outline" 
                      onClick={handleLoginClick}
                      className="w-full justify-start"
                    >
                      Login
                    </Button>
                    <Button 
                      onClick={handleCTAClick}
                      className="w-full justify-start"
                    >
                      {t.cta.primary}
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