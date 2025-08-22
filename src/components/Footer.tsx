import { Button } from '@/components/ui/button';
import { Input } from '@/components/ui/input';
import { Facebook, Instagram, Twitter, Youtube, Music } from 'lucide-react';
import { useLanguage } from '@/hooks/useLanguage';
import logoImage from '@/assets/chef-pro-logo.png';

const Footer = () => {
  const { getAppUrl, currentLanguage } = useLanguage();

  const handleNewsletterSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    // Newsletter subscription logic would go here
  };

  return (
    <footer id="contacto" className="bg-chef-dark text-white">
      <div className="container mx-auto px-4">
        {/* Main Footer Content */}
        <div className="py-16">
          <div className="grid md:grid-cols-2 lg:grid-cols-4 gap-8">
            {/* Brand Section */}
            <div className="lg:col-span-2 space-y-6">
              <div className="flex items-center space-x-3">
                <img src={logoImage} alt="AI Chef Pro" className="h-12 w-12" />
                <h3 className="text-2xl font-bold text-chef-gold">AI Chef Pro</h3>
              </div>
              
              <div className="space-y-4">
                <h4 className="text-xl font-bold text-chef-gold">
                  Inteligencia Artificial para el Chef de Hoy
                </h4>
                <p className="text-gray-300 leading-relaxed">
                  Desarrolla tu potencial profesional con el uso y el apoyo de la inteligencia artificial en tu día a día.
                </p>
                <p className="text-sm text-gray-400">
                  Suite de Herramientas y Aplicaciones de Inteligencia Artificial modeladas para Chefs, Cocineros y profesionales de la hostelería.
                </p>
              </div>

              {/* Newsletter */}
              <div className="space-y-4">
                <h4 className="font-bold text-chef-gold">BOLETÍN IA PARA CHEFS PRO</h4>
                <form onSubmit={handleNewsletterSubmit} className="flex gap-2">
                  <Input
                    type="email"
                    placeholder="Ingresa tu correo electrónico"
                    className="flex-1 bg-white/10 border-white/20 text-white placeholder:text-gray-400"
                  />
                  <Button 
                    type="submit"
                    className="chef-cta-button px-6"
                  >
                    Suscribirme
                  </Button>
                </form>
              </div>
            </div>

            {/* Navigation Links */}
            <div className="space-y-6">
              <h4 className="text-lg font-bold text-chef-gold">Navegación</h4>
              <ul className="space-y-3">
                <li>
                  <a href="#inicio" className="text-gray-300 hover:text-chef-gold transition-colors">
                    Inicio
                  </a>
                </li>
                <li>
                  <a href="#plataformas" className="text-gray-300 hover:text-chef-gold transition-colors">
                    Plataformas
                  </a>
                </li>
                <li>
                  <a href="#servicios" className="text-gray-300 hover:text-chef-gold transition-colors">
                    Servicios
                  </a>
                </li>
                <li>
                  <a href="#recursos" className="text-gray-300 hover:text-chef-gold transition-colors">
                    Recursos
                  </a>
                </li>
                <li>
                  <a 
                    href="https://blog.aichef.pro" 
                    target="_blank" 
                    rel="noopener noreferrer"
                    className="text-gray-300 hover:text-chef-gold transition-colors"
                  >
                    Blog
                  </a>
                </li>
                <li>
                  <a 
                    href="https://aichef.pro/herramientas-gratuitas" 
                    target="_blank"
                    rel="noopener noreferrer"
                    className="text-gray-300 hover:text-chef-gold transition-colors"
                  >
                    Herramientas Gratuitas con AI 🪄
                  </a>
                </li>
              </ul>
            </div>

            {/* Contact & Social */}
            <div className="space-y-6">
              <h4 className="text-lg font-bold text-chef-gold">Contacto</h4>
              <div className="space-y-3">
                <p className="text-gray-300">
                  <a href="mailto:info@aichef.pro" className="hover:text-chef-gold transition-colors">
                    info@aichef.pro
                  </a>
                </p>
                <p className="text-gray-300">
                  <a href="tel:+34744717942" className="hover:text-chef-gold transition-colors">
                    +34 744 717 942
                  </a>
                </p>
              </div>

              {/* Action Buttons */}
              <div className="space-y-3">
                <Button 
                  onClick={() => window.open(getAppUrl(currentLanguage) + '/pricing', '_blank')}
                  className="w-full chef-cta-button"
                >
                  Planes y Precios
                </Button>
                <Button 
                  variant="outline" 
                  onClick={() => window.open(getAppUrl(currentLanguage) + '/pricing', '_blank')}
                  className="w-full border-chef-gold text-chef-gold hover:bg-chef-gold hover:text-chef-dark"
                >
                  Probar Gratis
                </Button>
              </div>

              {/* Social Media */}
              <div>
                <h5 className="font-semibold text-chef-gold mb-3">Síguenos</h5>
                <div className="flex space-x-4">
                  <a 
                    href="https://www.facebook.com/profile.php?id=61565177312061" 
                    target="_blank" 
                    rel="noopener noreferrer"
                    className="text-gray-300 hover:text-chef-gold transition-colors"
                  >
                    <Facebook className="h-5 w-5" />
                  </a>
                  <a 
                    href="https://www.instagram.com/aichefpro" 
                    target="_blank" 
                    rel="noopener noreferrer"
                    className="text-gray-300 hover:text-chef-gold transition-colors"
                  >
                    <Instagram className="h-5 w-5" />
                  </a>
                  <a 
                    href="https://x.com/aichefpro" 
                    target="_blank" 
                    rel="noopener noreferrer"
                    className="text-gray-300 hover:text-chef-gold transition-colors"
                  >
                    <Twitter className="h-5 w-5" />
                  </a>
                  <a 
                    href="https://tiktok.com/aichefpro" 
                    target="_blank" 
                    rel="noopener noreferrer"
                    className="text-gray-300 hover:text-chef-gold transition-colors"
                  >
                    <Music className="h-5 w-5" />
                  </a>
                  <a 
                    href="https://youtube.com/playlist?list=PLkevVb6pg5bs3b2hlwI8-2wW7juXV-eFj&si=eGAgpRRE0h6zfH1S" 
                    target="_blank" 
                    rel="noopener noreferrer"
                    className="text-gray-300 hover:text-chef-gold transition-colors"
                  >
                    <Youtube className="h-5 w-5" />
                  </a>
                </div>
              </div>
            </div>
          </div>
        </div>

        {/* Bottom Footer */}
        <div className="border-t border-gray-700 py-8">
          <div className="flex flex-col md:flex-row justify-between items-center space-y-4 md:space-y-0">
            <div className="text-gray-400 text-sm">
              © 2024. All rights reserved.
            </div>
            
            <div className="flex flex-col md:flex-row items-center space-y-2 md:space-y-0 md:space-x-6 text-sm">
              <a 
                href="https://chefbusiness.co/" 
                target="_blank" 
                rel="noopener noreferrer"
                className="text-gray-400 hover:text-chef-gold transition-colors"
              >
                Chefbusiness Consultoría Gastronómica
              </a>
              <a 
                href="https://gastroseo.com/" 
                target="_blank" 
                rel="noopener noreferrer"
                className="text-gray-400 hover:text-chef-gold transition-colors"
              >
                GastroSEO
              </a>
            </div>
          </div>
        </div>
      </div>
    </footer>
  );
};

export default Footer;