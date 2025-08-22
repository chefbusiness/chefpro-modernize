import { Button } from '@/components/ui/button';
import { Input } from '@/components/ui/input';
import { Separator } from '@/components/ui/separator';
import { Facebook, Instagram, Twitter, Youtube, Music } from 'lucide-react';
import { useLanguage } from '@/hooks/useLanguage';

export default function ModernFooter() {
  const { getAppUrl, currentLanguage } = useLanguage();

  const handleNewsletterSubmit = (e: React.FormEvent) => {
    e.preventDefault();
  };

  return (
    <footer className="border-t bg-background">
      <div className="container py-14">
        <div className="grid grid-cols-1 gap-8 lg:grid-cols-4">
          {/* Brand Column */}
          <div className="lg:col-span-2">
            <div className="flex items-center space-x-2">
              <img 
                src="/src/assets/logo-ai-chef-pro.svg" 
                alt="AI Chef Pro Logo" 
                className="h-8 w-auto"
              />
            </div>
            <p className="mt-4 text-sm text-muted-foreground max-w-md">
              <strong>Inteligencia Artificial para el Chef de Hoy.</strong> 
              Desarrolla tu potencial profesional con el uso y el apoyo de la 
              inteligencia artificial en tu día a día.
            </p>
            <p className="mt-2 text-xs text-muted-foreground">
              Suite de Herramientas y Aplicaciones de Inteligencia Artificial 
              modeladas para Chefs, Cocineros y profesionales de la hostelería.
            </p>

            {/* Newsletter */}
            <div className="mt-6">
              <h4 className="text-sm font-semibold">BOLETÍN IA PARA CHEFS PRO</h4>
              <form onSubmit={handleNewsletterSubmit} className="mt-3 flex max-w-md gap-2">
                <Input
                  type="email"
                  placeholder="Ingresa tu correo electrónico"
                  className="flex-1"
                />
                <Button type="submit" size="sm">
                  Suscribirme
                </Button>
              </form>
            </div>
          </div>

          {/* Links Column */}
          <div>
            <h4 className="text-sm font-semibold">Navegación</h4>
            <ul className="mt-4 space-y-3 text-sm">
              <li>
                <a href="#inicio" className="text-muted-foreground hover:text-foreground transition-colors">
                  Inicio
                </a>
              </li>
              <li>
                <a href="#herramientas" className="text-muted-foreground hover:text-foreground transition-colors">
                  Herramientas
                </a>
              </li>
              <li>
                <a href="#pricing" className="text-muted-foreground hover:text-foreground transition-colors">
                  Precios
                </a>
              </li>
              <li>
                <a 
                  href="https://blog.aichef.pro" 
                  target="_blank" 
                  rel="noopener noreferrer"
                  className="text-muted-foreground hover:text-foreground transition-colors"
                >
                  Blog
                </a>
              </li>
              <li>
                <a 
                  href="https://aichef.pro/herramientas-gratuitas" 
                  target="_blank"
                  rel="noopener noreferrer"
                  className="text-muted-foreground hover:text-foreground transition-colors"
                >
                  Herramientas Gratuitas 🪄
                </a>
              </li>
            </ul>
          </div>

          {/* Contact Column */}
          <div>
            <h4 className="text-sm font-semibold">Contacto</h4>
            <ul className="mt-4 space-y-3 text-sm">
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

            {/* Action Buttons */}
            <div className="mt-6 space-y-2">
              <Button 
                onClick={() => window.open(getAppUrl(currentLanguage) + '/pricing', '_blank')}
                className="w-full text-sm"
                size="sm"
              >
                Planes y Precios
              </Button>
              <Button 
                variant="outline" 
                onClick={() => window.open(getAppUrl(currentLanguage) + '/pricing', '_blank')}
                className="w-full text-sm"
                size="sm"
              >
                Probar Gratis
              </Button>
            </div>

            {/* Social Media */}
            <div className="mt-6">
              <h5 className="text-sm font-semibold mb-3">Síguenos</h5>
              <div className="flex space-x-3">
                <a 
                  href="https://www.facebook.com/profile.php?id=61565177312061" 
                  target="_blank" 
                  rel="noopener noreferrer"
                  className="text-muted-foreground hover:text-foreground transition-colors"
                >
                  <Facebook className="h-4 w-4" />
                </a>
                <a 
                  href="https://www.instagram.com/aichefpro" 
                  target="_blank" 
                  rel="noopener noreferrer"
                  className="text-muted-foreground hover:text-foreground transition-colors"
                >
                  <Instagram className="h-4 w-4" />
                </a>
                <a 
                  href="https://x.com/aichefpro" 
                  target="_blank" 
                  rel="noopener noreferrer"
                  className="text-muted-foreground hover:text-foreground transition-colors"
                >
                  <Twitter className="h-4 w-4" />
                </a>
                <a 
                  href="https://tiktok.com/aichefpro" 
                  target="_blank" 
                  rel="noopener noreferrer"
                  className="text-muted-foreground hover:text-foreground transition-colors"
                >
                  <Music className="h-4 w-4" />
                </a>
                <a 
                  href="https://youtube.com/playlist?list=PLkevVb6pg5bs3b2hlwI8-2wW7juXV-eFj&si=eGAgpRRE0h6zfH1S" 
                  target="_blank" 
                  rel="noopener noreferrer"
                  className="text-muted-foreground hover:text-foreground transition-colors"
                >
                  <Youtube className="h-4 w-4" />
                </a>
              </div>
            </div>
          </div>
        </div>

        <Separator className="my-8" />
        
        <div className="flex flex-col items-center justify-between gap-4 md:flex-row">
          <div className="text-center text-sm text-muted-foreground md:text-left">
            © 2024. All rights reserved.
          </div>
          
          <div className="flex items-center gap-4 text-sm">
            <a 
              href="https://chefbusiness.co/" 
              target="_blank" 
              rel="noopener noreferrer"
              className="text-muted-foreground hover:text-foreground transition-colors"
            >
              Chefbusiness Consultoría Gastronómica
            </a>
            <a 
              href="https://gastroseo.com/" 
              target="_blank" 
              rel="noopener noreferrer"
              className="text-muted-foreground hover:text-foreground transition-colors"
            >
              GastroSEO
            </a>
          </div>
        </div>
      </div>
    </footer>
  );
}