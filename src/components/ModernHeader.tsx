import { useState } from 'react';
import { Button } from '@/components/ui/button';
import { ChevronDown, Menu } from 'lucide-react';
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
                  {t('nav.aplicaciones')}
                </NavigationMenuTrigger>
                <NavigationMenuContent>
                  <div className="grid w-[600px] gap-3 p-4 md:grid-cols-3">
                    <div className="space-y-2">
                      <h4 className="font-medium leading-none text-accent">Creatividad</h4>
                      <div className="grid gap-1">
                        <NavigationMenuLink 
                          className="block text-sm text-muted-foreground hover:text-foreground transition-colors py-1"
                          href="#showcase-creatividad"
                        >
                          Cocina Creativa
                        </NavigationMenuLink>
                        <NavigationMenuLink 
                          className="block text-sm text-muted-foreground hover:text-foreground transition-colors py-1"
                          href="#showcase-creatividad"
                        >
                          Pastelería
                        </NavigationMenuLink>
                        <NavigationMenuLink 
                          className="block text-sm text-muted-foreground hover:text-foreground transition-colors py-1"
                          href="#showcase-creatividad"
                        >
                          Food Pairing
                        </NavigationMenuLink>
                      </div>
                    </div>
                    <div className="space-y-2">
                      <h4 className="font-medium leading-none text-accent">Recetarios</h4>
                      <div className="grid gap-1">
                        <NavigationMenuLink 
                          className="block text-sm text-muted-foreground hover:text-foreground transition-colors py-1"
                          href="#recetarios"
                        >
                          Europa (10)
                        </NavigationMenuLink>
                        <NavigationMenuLink 
                          className="block text-sm text-muted-foreground hover:text-foreground transition-colors py-1"
                          href="#recetarios"
                        >
                          Latinoamérica (11)
                        </NavigationMenuLink>
                        <NavigationMenuLink 
                          className="block text-sm text-muted-foreground hover:text-foreground transition-colors py-1"
                          href="#recetarios"
                        >
                          Asia (4)
                        </NavigationMenuLink>
                      </div>
                    </div>
                    <div className="space-y-2">
                      <h4 className="font-medium leading-none text-accent">Business</h4>
                      <div className="grid gap-1">
                        <NavigationMenuLink 
                          className="block text-sm text-muted-foreground hover:text-foreground transition-colors py-1"
                          href="#herramientas-business"
                        >
                          Mermas GenCal
                        </NavigationMenuLink>
                        <NavigationMenuLink 
                          className="block text-sm text-muted-foreground hover:text-foreground transition-colors py-1"
                          href="#herramientas-business"
                        >
                          ID Alérgenos
                        </NavigationMenuLink>
                        <NavigationMenuLink 
                          className="block text-sm text-muted-foreground hover:text-foreground transition-colors py-1"
                          href="#herramientas-business"
                        >
                          Mental Coach
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
              Login
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
              <SheetContent side="right" className="pr-0">
                <SheetHeader>
                  <SheetTitle>Menu</SheetTitle>
                </SheetHeader>
                <div className="my-4 h-[calc(100vh-8rem)] pb-10 pl-6">
                  <div className="flex flex-col space-y-3">
                    <a href="#inicio" className="font-medium">
                      {t('nav.inicio')}
                    </a>
                    <a href="#categorias-apps" className="font-medium">
                      Aplicaciones
                    </a>
                    <a href="#filtro-apps" className="font-medium">
                      Encuentra tu App
                    </a>
                    <a href="#showcase-creatividad" className="font-medium">
                      Creatividad
                    </a>
                    <a href="#recetarios" className="font-medium">
                      Recetarios
                    </a>
                    <a href="#herramientas-business" className="font-medium">
                      Herramientas
                    </a>
                    <a href="#pricing" className="font-medium">
                      Precios
                    </a>
                    <a href="https://blog.aichef.pro" target="_blank" rel="noopener noreferrer" className="font-medium">
                      {t('nav.blog')}
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