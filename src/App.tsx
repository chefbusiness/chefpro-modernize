import { Toaster } from "@/components/ui/toaster";
import { Toaster as Sonner } from "@/components/ui/sonner";
import { TooltipProvider } from "@/components/ui/tooltip";
import { QueryClient, QueryClientProvider } from "@tanstack/react-query";
import { HelmetProvider } from 'react-helmet-async';
import { BrowserRouter, Routes, Route } from "react-router-dom";
import CookieBanner from "@/components/CookieBanner";
import Index from "./pages/Index";
import MentoriaOnline from "./pages/MentoriaOnline";
import FormacionPresencial from "./pages/FormacionPresencial";
import Legal from "./pages/Legal";
import Cookies from "./pages/Cookies";
import Privacy from "./pages/Privacy";
import Terms from "./pages/Terms";
import NotFound from "./pages/NotFound";
import HerramientasIARestaurantes from "./pages/HerramientasIARestaurantes";
import ReducirCostesRestaurante from "./pages/ReducirCostesRestaurante";
import MenuRestaurante from "./pages/MenuRestaurante";
import MarketingRestaurante from "./pages/MarketingRestaurante";
import ChatGPTRestaurantes from "./pages/ChatGPTRestaurantes";
import SoftwareGestionCocina from "./pages/SoftwareGestionCocina";
import RecetasIARestaurantes from "./pages/RecetasIARestaurantes";
import EscandallosRestaurante from "./pages/EscandallosRestaurante";
import HerramientasGratuitas from "./pages/HerramientasGratuitas";
import CalculadoraFoodCost from "./pages/CalculadoraFoodCost";
import SimuladorRentabilidad from "./pages/SimuladorRentabilidad";
import TestDigitalizacion from "./pages/TestDigitalizacion";
import DetectorAlergenos from "./pages/DetectorAlergenos";
import CalculadoraBrigada from "./pages/CalculadoraBrigada";
import './i18n/config';

const queryClient = new QueryClient();

const App = () => (
  <QueryClientProvider client={queryClient}>
    <HelmetProvider>
      <TooltipProvider>
        <Toaster />
        <Sonner />
        <BrowserRouter>
          <Routes>
            <Route path="/" element={<Index />} />
            <Route path="/:lang" element={<Index />} />
            
            {/* Spanish routes */}
            <Route path="/mentoria-online" element={<MentoriaOnline />} />
            <Route path="/formacion-presencial" element={<FormacionPresencial />} />
            <Route path="/legales" element={<Legal />} />
            <Route path="/cookies" element={<Cookies />} />
            <Route path="/privacidad" element={<Privacy />} />
            <Route path="/terminos" element={<Terms />} />
            
            {/* Multi-language routes */}
            <Route path="/:lang/mentoria-online" element={<MentoriaOnline />} />
            <Route path="/es/formacion-presencial" element={<FormacionPresencial />} />
            <Route path="/:lang/legales" element={<Legal />} />
            <Route path="/:lang/cookies" element={<Cookies />} />
            <Route path="/:lang/privacidad" element={<Privacy />} />
            <Route path="/:lang/terminos" element={<Terms />} />
            
            {/* Landing pages SEO — todos los idiomas */}
            <Route path="/herramientas-ia-para-restaurantes" element={<HerramientasIARestaurantes />} />
            <Route path="/en/ai-tools-for-restaurants" element={<HerramientasIARestaurantes />} />
            <Route path="/fr/outils-ia-restaurant" element={<HerramientasIARestaurantes />} />
            <Route path="/de/ki-tools-restaurant" element={<HerramientasIARestaurantes />} />
            <Route path="/it/strumenti-ia-ristorante" element={<HerramientasIARestaurantes />} />
            <Route path="/pt/ferramentas-ia-restaurante" element={<HerramientasIARestaurantes />} />
            <Route path="/nl/ai-tools-restaurant" element={<HerramientasIARestaurantes />} />

            {/* Landing costes restaurante — todos los idiomas */}
            <Route path="/reducir-costes-restaurante-ia" element={<ReducirCostesRestaurante />} />
            <Route path="/en/reduce-restaurant-costs-ai" element={<ReducirCostesRestaurante />} />
            <Route path="/fr/reduire-couts-restaurant-ia" element={<ReducirCostesRestaurante />} />
            <Route path="/de/restaurantkosten-senken-ki" element={<ReducirCostesRestaurante />} />
            <Route path="/it/ridurre-costi-ristorante-ia" element={<ReducirCostesRestaurante />} />
            <Route path="/pt/reduzir-custos-restaurante-ia" element={<ReducirCostesRestaurante />} />
            <Route path="/nl/restaurantkosten-verlagen-ai" element={<ReducirCostesRestaurante />} />

            {/* Landing menu restaurante — todos los idiomas */}
            <Route path="/carta-menu-restaurante-ia" element={<MenuRestaurante />} />
            <Route path="/en/restaurant-menu-ai" element={<MenuRestaurante />} />
            <Route path="/fr/carte-menu-restaurant-ia" element={<MenuRestaurante />} />
            <Route path="/de/speisekarte-restaurant-ki" element={<MenuRestaurante />} />
            <Route path="/it/menu-ristorante-ia" element={<MenuRestaurante />} />
            <Route path="/pt/cardapio-restaurante-ia" element={<MenuRestaurante />} />
            <Route path="/nl/restaurantmenu-ai" element={<MenuRestaurante />} />

            {/* Landing marketing restaurante — todos los idiomas */}
            <Route path="/marketing-restaurante-ia" element={<MarketingRestaurante />} />
            <Route path="/en/restaurant-marketing-ai" element={<MarketingRestaurante />} />
            <Route path="/fr/marketing-restaurant-ia" element={<MarketingRestaurante />} />
            <Route path="/de/restaurant-marketing-ki" element={<MarketingRestaurante />} />
            <Route path="/it/marketing-ristorante-ia" element={<MarketingRestaurante />} />
            <Route path="/pt/marketing-restaurante-ia-pt" element={<MarketingRestaurante />} />
            <Route path="/nl/restaurant-marketing-ai-nl" element={<MarketingRestaurante />} />

            <Route path="/chatgpt-para-restaurantes" element={<ChatGPTRestaurantes />} />
            <Route path="/en/chatgpt-for-restaurants" element={<ChatGPTRestaurantes />} />
            <Route path="/fr/chatgpt-pour-restaurants" element={<ChatGPTRestaurantes />} />
            <Route path="/de/chatgpt-fuer-restaurants" element={<ChatGPTRestaurantes />} />
            <Route path="/it/chatgpt-per-ristoranti" element={<ChatGPTRestaurantes />} />
            <Route path="/pt/chatgpt-para-restaurantes" element={<ChatGPTRestaurantes />} />
            <Route path="/nl/chatgpt-voor-restaurants" element={<ChatGPTRestaurantes />} />

            {/* Landing software gestión cocina — todos los idiomas */}
            <Route path="/software-gestion-cocina-ia" element={<SoftwareGestionCocina />} />
            <Route path="/en/kitchen-management-software-ai" element={<SoftwareGestionCocina />} />
            <Route path="/fr/logiciel-gestion-cuisine-ia" element={<SoftwareGestionCocina />} />
            <Route path="/de/kuechenverwaltung-ki" element={<SoftwareGestionCocina />} />
            <Route path="/it/software-gestione-cucina-ia" element={<SoftwareGestionCocina />} />
            <Route path="/pt/software-gestao-cozinha-ia" element={<SoftwareGestionCocina />} />
            <Route path="/nl/keuken-software-ai" element={<SoftwareGestionCocina />} />

            {/* Landing recetas IA restaurantes — todos los idiomas */}
            <Route path="/recetas-ia-restaurantes" element={<RecetasIARestaurantes />} />
            <Route path="/en/ai-recipes-for-restaurants" element={<RecetasIARestaurantes />} />
            <Route path="/fr/recettes-ia-restaurants" element={<RecetasIARestaurantes />} />
            <Route path="/de/ki-rezepte-restaurants" element={<RecetasIARestaurantes />} />
            <Route path="/it/ricette-ia-ristoranti" element={<RecetasIARestaurantes />} />
            <Route path="/pt/receitas-ia-restaurantes" element={<RecetasIARestaurantes />} />
            <Route path="/nl/ai-recepten-restaurants" element={<RecetasIARestaurantes />} />

            {/* Landing escandallos restaurante IA — todos los idiomas */}
            <Route path="/escandallos-restaurante-ia" element={<EscandallosRestaurante />} />
            <Route path="/en/food-cost-calculator-restaurant-ai" element={<EscandallosRestaurante />} />
            <Route path="/fr/calcul-food-cost-restaurant-ia" element={<EscandallosRestaurante />} />
            <Route path="/de/food-cost-rechner-restaurant-ki" element={<EscandallosRestaurante />} />
            <Route path="/it/food-cost-ristorante-ia" element={<EscandallosRestaurante />} />
            <Route path="/pt/escandallo-restaurante-ia" element={<EscandallosRestaurante />} />
            <Route path="/nl/food-cost-berekening-restaurant-ai" element={<EscandallosRestaurante />} />

            {/* Hub Herramientas Gratuitas — todos los idiomas */}
            <Route path="/herramientas-gratuitas" element={<HerramientasGratuitas />} />
            <Route path="/en/free-tools-restaurants" element={<HerramientasGratuitas />} />
            <Route path="/fr/outils-gratuits-restaurant" element={<HerramientasGratuitas />} />
            <Route path="/de/kostenlose-tools-restaurant" element={<HerramientasGratuitas />} />
            <Route path="/it/strumenti-gratuiti-ristorante" element={<HerramientasGratuitas />} />
            <Route path="/pt/ferramentas-gratuitas-restaurante" element={<HerramientasGratuitas />} />
            <Route path="/nl/gratis-tools-restaurant" element={<HerramientasGratuitas />} />

            {/* Calculadora Food Cost — todos los idiomas */}
            <Route path="/calculadora-food-cost-restaurante" element={<CalculadoraFoodCost />} />
            <Route path="/en/food-cost-calculator-restaurant" element={<CalculadoraFoodCost />} />
            <Route path="/fr/calculateur-food-cost-restaurant" element={<CalculadoraFoodCost />} />
            <Route path="/de/food-cost-rechner-restaurant" element={<CalculadoraFoodCost />} />
            <Route path="/it/calcolatore-food-cost-ristorante" element={<CalculadoraFoodCost />} />
            <Route path="/pt/calculadora-food-cost-restaurante" element={<CalculadoraFoodCost />} />
            <Route path="/nl/food-cost-calculator-restaurant" element={<CalculadoraFoodCost />} />

            {/* Simulador Rentabilidad — todos los idiomas */}
            <Route path="/simulador-rentabilidad-restaurante" element={<SimuladorRentabilidad />} />
            <Route path="/en/restaurant-profit-simulator" element={<SimuladorRentabilidad />} />
            <Route path="/fr/simulateur-rentabilite-restaurant" element={<SimuladorRentabilidad />} />
            <Route path="/de/rentabilitaet-simulator-restaurant" element={<SimuladorRentabilidad />} />
            <Route path="/it/simulatore-redditivita-ristorante" element={<SimuladorRentabilidad />} />
            <Route path="/pt/simulador-rentabilidade-restaurante" element={<SimuladorRentabilidad />} />
            <Route path="/nl/winstgevendheid-simulator-restaurant" element={<SimuladorRentabilidad />} />

            {/* Test Digitalización — todos los idiomas */}
            <Route path="/test-digitalizacion-restaurante" element={<TestDigitalizacion />} />
            <Route path="/en/restaurant-digitalization-test" element={<TestDigitalizacion />} />
            <Route path="/fr/test-digitalisation-restaurant" element={<TestDigitalizacion />} />
            <Route path="/de/digitalisierungstest-restaurant" element={<TestDigitalizacion />} />
            <Route path="/it/test-digitalizzazione-ristorante" element={<TestDigitalizacion />} />
            <Route path="/pt/teste-digitalizacao-restaurante" element={<TestDigitalizacion />} />
            <Route path="/nl/digitaliseringstest-restaurant" element={<TestDigitalizacion />} />

            {/* Detector Alérgenos — todos los idiomas */}
            <Route path="/detector-alergenos-restaurante" element={<DetectorAlergenos />} />
            <Route path="/en/restaurant-allergen-detector" element={<DetectorAlergenos />} />
            <Route path="/fr/detecteur-allergenes-restaurant" element={<DetectorAlergenos />} />
            <Route path="/de/allergen-detektor-restaurant" element={<DetectorAlergenos />} />
            <Route path="/it/rilevatore-allergeni-ristorante" element={<DetectorAlergenos />} />
            <Route path="/pt/detector-alergenos-restaurante" element={<DetectorAlergenos />} />
            <Route path="/nl/allergenen-detector-restaurant" element={<DetectorAlergenos />} />

            {/* Calculadora Brigada — todos los idiomas */}
            <Route path="/calculadora-brigada-restaurante" element={<CalculadoraBrigada />} />
            <Route path="/en/restaurant-brigade-calculator" element={<CalculadoraBrigada />} />
            <Route path="/fr/calculateur-brigade-restaurant" element={<CalculadoraBrigada />} />
            <Route path="/de/brigaden-rechner-restaurant" element={<CalculadoraBrigada />} />
            <Route path="/it/calcolatore-brigata-ristorante" element={<CalculadoraBrigada />} />
            <Route path="/pt/calculadora-brigada-restaurante" element={<CalculadoraBrigada />} />
            <Route path="/nl/brigade-calculator-restaurant" element={<CalculadoraBrigada />} />

            {/* ADD ALL CUSTOM ROUTES ABOVE THE CATCH-ALL "*" ROUTE */}
            <Route path="*" element={<NotFound />} />
          </Routes>
          <CookieBanner />
        </BrowserRouter>
      </TooltipProvider>
    </HelmetProvider>
  </QueryClientProvider>
);

export default App;
