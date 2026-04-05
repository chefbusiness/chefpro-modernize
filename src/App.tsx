import { useEffect } from 'react';
import { Toaster } from "@/components/ui/toaster";
import { Toaster as Sonner } from "@/components/ui/sonner";
import { TooltipProvider } from "@/components/ui/tooltip";
import { QueryClient, QueryClientProvider } from "@tanstack/react-query";
import { HelmetProvider } from 'react-helmet-async';
import { BrowserRouter, Routes, Route, useLocation } from "react-router-dom";

function ScrollToTop() {
  const { pathname } = useLocation();
  useEffect(() => { window.scrollTo(0, 0); }, [pathname]);
  return null;
}
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
import CalendarioContenidos from "./pages/CalendarioContenidos";
import GeneradorTextosCarta from "./pages/GeneradorTextosCarta";
import GeneradorMenuDegustacion from "./pages/GeneradorMenuDegustacion";
import ProPromptsEbook from "./pages/ProPromptsEbook";
import ProPromptsLibrary from "./pages/ProPromptsLibrary";
import KitEscandallos from "./pages/KitEscandallos";
import ProductosDigitales from "./pages/ProductosDigitales";
import AccessGate from "./pages/AccessGate";
import KitEscandallosAccessGate from "./pages/KitEscandallosAccessGate";
import KitEscandallosDashboard from "./pages/KitEscandallosDashboard";
import PackAppcc from "./pages/PackAppcc";
import PackAppccAccessGate from "./pages/PackAppccAccessGate";
import PackAppccDashboard from "./pages/PackAppccDashboard";
import KitTareas from "./pages/KitTareas";
import KitTareasAccessGate from "./pages/KitTareasAccessGate";
import KitTareasDashboard from "./pages/KitTareasDashboard";
import KitTareasCafeteria from "./pages/KitTareasCafeteria";
import KitTareasCafeteriaAccessGate from "./pages/KitTareasCafeteriaAccessGate";
import KitTareasCafeteriaDashboard from "./pages/KitTareasCafeteriaDashboard";
import KitTareasPizzeria from "./pages/KitTareasPizzeria";
import KitTareasPizzeriaAccessGate from "./pages/KitTareasPizzeriaAccessGate";
import KitTareasPizzeriaDashboard from "./pages/KitTareasPizzeriaDashboard";
import KitTareasHamburgueseria from "./pages/KitTareasHamburgueseria";
import KitTareasHamburguseriaAccessGate from "./pages/KitTareasHamburguseriaAccessGate";
import KitTareasHamburgueseriaDashboard from "./pages/KitTareasHamburgueseriaDashboard";
import KitTareasDarkKitchen from "./pages/KitTareasDarkKitchen";
import KitTareasDarkKitchenAccessGate from "./pages/KitTareasDarkKitchenAccessGate";
import KitTareasDarkKitchenDashboard from "./pages/KitTareasDarkKitchenDashboard";
import KitTareasPasteleria from "./pages/KitTareasPasteleria";
import KitTareasPasteleriaAccessGate from "./pages/KitTareasPasteleriaAccessGate";
import KitTareasPasteleriaDashboard from "./pages/KitTareasPasteleriaDashboard";
import KitTareasBar from "./pages/KitTareasBar";
import KitTareasBarAccessGate from "./pages/KitTareasBarAccessGate";
import KitTareasBarDashboard from "./pages/KitTareasBarDashboard";
import KitTareasCatering from "./pages/KitTareasCatering";
import KitTareasCateringAccessGate from "./pages/KitTareasCateringAccessGate";
import KitTareasCateringDashboard from "./pages/KitTareasCateringDashboard";
import KitTareasHotel from "./pages/KitTareasHotel";
import KitTareasHotelAccessGate from "./pages/KitTareasHotelAccessGate";
import KitTareasHotelDashboard from "./pages/KitTareasHotelDashboard";
import KitTareasHeladeria from "./pages/KitTareasHeladeria";
import KitTareasHeladeriaAccessGate from "./pages/KitTareasHeladeriaAccessGate";
import KitTareasHeladeriaDashboard from "./pages/KitTareasHeladeriaDashboard";
import KitTareasChocolateria from "./pages/KitTareasChocolateria";
import KitTareasChocolateriaAccessGate from "./pages/KitTareasChocolateriaAccessGate";
import KitTareasChocolateriaDashboard from "./pages/KitTareasChocolateriaDashboard";
import KitTareasRestauranteCreativo from "./pages/KitTareasRestauranteCreativo";
import KitTareasRestauranteCreativoAccessGate from "./pages/KitTareasRestauranteCreativoAccessGate";
import KitTareasRestauranteCreativoDashboard from "./pages/KitTareasRestauranteCreativoDashboard";
import KitTareasChefPrivado from "./pages/KitTareasChefPrivado";
import KitTareasChefPrivadoAccessGate from "./pages/KitTareasChefPrivadoAccessGate";
import KitTareasChefPrivadoDashboard from "./pages/KitTareasChefPrivadoDashboard";
import KitGestionPersonal from "./pages/KitGestionPersonal";
import KitGestionPersonalAccessGate from "./pages/KitGestionPersonalAccessGate";
import KitGestionPersonalDashboard from "./pages/KitGestionPersonalDashboard";
import KitInventario from "./pages/KitInventario";
import KitInventarioAccessGate from "./pages/KitInventarioAccessGate";
import KitInventarioDashboard from "./pages/KitInventarioDashboard";
import KitPlanFinanciero from "./pages/KitPlanFinanciero";
import KitPlanFinancieroAccessGate from "./pages/KitPlanFinancieroAccessGate";
import KitPlanFinancieroDashboard from "./pages/KitPlanFinancieroDashboard";
import MegaPackTareas from "./pages/MegaPackTareas";
import MegaPackTareasAccessGate from "./pages/MegaPackTareasAccessGate";
import MegaPackTareasDashboard from "./pages/MegaPackTareasDashboard";
import ProtectedRoute from "./components/shared/ProtectedRoute";
import './i18n/config';

const queryClient = new QueryClient();

const App = () => (
  <QueryClientProvider client={queryClient}>
    <HelmetProvider>
      <TooltipProvider>
        <Toaster />
        <Sonner />
        <BrowserRouter>
          <ScrollToTop />
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
            <Route path="/en/ai-food-cost-calculator" element={<CalculadoraFoodCost />} />
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

            {/* Calendario de Contenidos — todos los idiomas */}
            <Route path="/calendario-contenidos-restaurante" element={<CalendarioContenidos />} />
            <Route path="/en/restaurant-content-calendar" element={<CalendarioContenidos />} />
            <Route path="/fr/calendrier-contenu-restaurant" element={<CalendarioContenidos />} />
            <Route path="/de/content-kalender-restaurant" element={<CalendarioContenidos />} />
            <Route path="/it/calendario-contenuti-ristorante" element={<CalendarioContenidos />} />
            <Route path="/pt/calendario-conteudo-restaurante" element={<CalendarioContenidos />} />
            <Route path="/nl/content-kalender-restaurant" element={<CalendarioContenidos />} />

            {/* Generador Textos Carta — todos los idiomas */}
            <Route path="/generador-textos-carta-restaurante" element={<GeneradorTextosCarta />} />
            <Route path="/en/restaurant-menu-copy-generator" element={<GeneradorTextosCarta />} />
            <Route path="/fr/generateur-textes-carte-restaurant" element={<GeneradorTextosCarta />} />
            <Route path="/de/speisekarten-text-generator" element={<GeneradorTextosCarta />} />
            <Route path="/it/generatore-testi-menu-ristorante" element={<GeneradorTextosCarta />} />
            <Route path="/pt/gerador-textos-cardapio-restaurante" element={<GeneradorTextosCarta />} />
            <Route path="/nl/menukaart-tekst-generator" element={<GeneradorTextosCarta />} />

            {/* Generador Menú Degustación — todos los idiomas */}
            <Route path="/generador-menu-degustacion" element={<GeneradorMenuDegustacion />} />
            <Route path="/en/tasting-menu-generator" element={<GeneradorMenuDegustacion />} />
            <Route path="/fr/generateur-menu-degustation" element={<GeneradorMenuDegustacion />} />
            <Route path="/de/degustationsmenu-generator" element={<GeneradorMenuDegustacion />} />
            <Route path="/it/generatore-menu-degustazione" element={<GeneradorMenuDegustacion />} />
            <Route path="/pt/gerador-menu-degustacao" element={<GeneradorMenuDegustacion />} />
            <Route path="/nl/proefmenu-generator" element={<GeneradorMenuDegustacion />} />

            {/* Productos Digitales Hub */}
            <Route path="/productos-digitales" element={<ProductosDigitales />} />

            {/* Kit de Escandallos Pro */}
            <Route path="/kit-escandallos" element={<KitEscandallos />} />
            <Route path="/kit-escandallos-access" element={<KitEscandallosAccessGate />} />
            <Route
              path="/kit-escandallos-library"
              element={
                <ProtectedRoute storageKey="kit-escandallos-jwt" redirectTo="/kit-escandallos">
                  <KitEscandallosDashboard />
                </ProtectedRoute>
              }
            />

            {/* Pack de Plantillas APPCC */}
            <Route path="/pack-appcc" element={<PackAppcc />} />
            <Route path="/pack-appcc-access" element={<PackAppccAccessGate />} />
            <Route
              path="/pack-appcc-library"
              element={
                <ProtectedRoute storageKey="pack-appcc-jwt" redirectTo="/pack-appcc">
                  <PackAppccDashboard />
                </ProtectedRoute>
              }
            />

            {/* Kit de Tareas Recurrentes */}
            <Route path="/kit-tareas" element={<KitTareas />} />
            <Route path="/kit-tareas-access" element={<KitTareasAccessGate />} />
            <Route
              path="/kit-tareas-library"
              element={
                <ProtectedRoute storageKey="kit-tareas-jwt" redirectTo="/kit-tareas">
                  <KitTareasDashboard />
                </ProtectedRoute>
              }
            />

            {/* Kit de Tareas Recurrentes: Cafetería / Brunch */}
            <Route path="/kit-tareas-cafeteria" element={<KitTareasCafeteria />} />
            <Route path="/kit-tareas-cafeteria-access" element={<KitTareasCafeteriaAccessGate />} />
            <Route
              path="/kit-tareas-cafeteria-library"
              element={
                <ProtectedRoute storageKey="kit-tareas-cafeteria-jwt" redirectTo="/kit-tareas-cafeteria">
                  <KitTareasCafeteriaDashboard />
                </ProtectedRoute>
              }
            />

            {/* Kit de Tareas Recurrentes: Pizzería */}
            <Route path="/kit-tareas-pizzeria" element={<KitTareasPizzeria />} />
            <Route path="/kit-tareas-pizzeria-access" element={<KitTareasPizzeriaAccessGate />} />
            <Route
              path="/kit-tareas-pizzeria-library"
              element={
                <ProtectedRoute storageKey="kit-tareas-pizzeria-jwt" redirectTo="/kit-tareas-pizzeria">
                  <KitTareasPizzeriaDashboard />
                </ProtectedRoute>
              }
            />

            {/* Kit de Tareas Recurrentes: Hamburguesería */}
            <Route path="/kit-tareas-hamburgueseria" element={<KitTareasHamburgueseria />} />
            <Route path="/kit-tareas-hamburgueseria-access" element={<KitTareasHamburguseriaAccessGate />} />
            <Route
              path="/kit-tareas-hamburgueseria-library"
              element={
                <ProtectedRoute storageKey="kit-tareas-hamburgueseria-jwt" redirectTo="/kit-tareas-hamburgueseria">
                  <KitTareasHamburgueseriaDashboard />
                </ProtectedRoute>
              }
            />

            {/* Kit de Tareas Recurrentes: Dark Kitchen */}
            <Route path="/kit-tareas-dark-kitchen" element={<KitTareasDarkKitchen />} />
            <Route path="/kit-tareas-dark-kitchen-access" element={<KitTareasDarkKitchenAccessGate />} />
            <Route
              path="/kit-tareas-dark-kitchen-library"
              element={
                <ProtectedRoute storageKey="kit-tareas-dark-kitchen-jwt" redirectTo="/kit-tareas-dark-kitchen">
                  <KitTareasDarkKitchenDashboard />
                </ProtectedRoute>
              }
            />

            {/* Kit Tareas Pastelería */}
            <Route path="/kit-tareas-pasteleria" element={<KitTareasPasteleria />} />
            <Route path="/kit-tareas-pasteleria-access" element={<KitTareasPasteleriaAccessGate />} />
            <Route
              path="/kit-tareas-pasteleria-library"
              element={
                <ProtectedRoute storageKey="kit-tareas-pasteleria-jwt" redirectTo="/kit-tareas-pasteleria">
                  <KitTareasPasteleriaDashboard />
                </ProtectedRoute>
              }
            />

            {/* Kit Tareas Bar */}
            <Route path="/kit-tareas-bar" element={<KitTareasBar />} />
            <Route path="/kit-tareas-bar-access" element={<KitTareasBarAccessGate />} />
            <Route
              path="/kit-tareas-bar-library"
              element={
                <ProtectedRoute storageKey="kit-tareas-bar-jwt" redirectTo="/kit-tareas-bar">
                  <KitTareasBarDashboard />
                </ProtectedRoute>
              }
            />

            {/* Kit Tareas Catering */}
            <Route path="/kit-tareas-catering" element={<KitTareasCatering />} />
            <Route path="/kit-tareas-catering-access" element={<KitTareasCateringAccessGate />} />
            <Route
              path="/kit-tareas-catering-library"
              element={
                <ProtectedRoute storageKey="kit-tareas-catering-jwt" redirectTo="/kit-tareas-catering">
                  <KitTareasCateringDashboard />
                </ProtectedRoute>
              }
            />

            {/* Kit Tareas Hotel */}
            <Route path="/kit-tareas-hotel" element={<KitTareasHotel />} />
            <Route path="/kit-tareas-hotel-completo-access" element={<KitTareasHotelAccessGate />} />
            <Route
              path="/kit-tareas-hotel-library"
              element={
                <ProtectedRoute storageKey="kit-tareas-hotel-jwt" redirectTo="/kit-tareas-hotel">
                  <KitTareasHotelDashboard />
                </ProtectedRoute>
              }
            />

            {/* Kit Tareas Heladería */}
            <Route path="/kit-tareas-heladeria" element={<KitTareasHeladeria />} />
            <Route path="/kit-tareas-heladeria-access" element={<KitTareasHeladeriaAccessGate />} />
            <Route
              path="/kit-tareas-heladeria-library"
              element={
                <ProtectedRoute storageKey="kit-tareas-heladeria-jwt" redirectTo="/kit-tareas-heladeria">
                  <KitTareasHeladeriaDashboard />
                </ProtectedRoute>
              }
            />

            {/* Kit Tareas Chocolatería */}
            <Route path="/kit-tareas-chocolateria" element={<KitTareasChocolateria />} />
            <Route path="/kit-tareas-chocolateria-access" element={<KitTareasChocolateriaAccessGate />} />
            <Route
              path="/kit-tareas-chocolateria-library"
              element={
                <ProtectedRoute storageKey="kit-tareas-chocolateria-jwt" redirectTo="/kit-tareas-chocolateria">
                  <KitTareasChocolateriaDashboard />
                </ProtectedRoute>
              }
            />

            {/* Kit Tareas Restaurante Creativo */}
            <Route path="/kit-tareas-restaurante-creativo" element={<KitTareasRestauranteCreativo />} />
            <Route path="/kit-tareas-restaurante-creativo-access" element={<KitTareasRestauranteCreativoAccessGate />} />
            <Route
              path="/kit-tareas-restaurante-creativo-library"
              element={
                <ProtectedRoute storageKey="kit-tareas-restaurante-creativo-jwt" redirectTo="/kit-tareas-restaurante-creativo">
                  <KitTareasRestauranteCreativoDashboard />
                </ProtectedRoute>
              }
            />

            {/* Kit Tareas Chef Privado */}
            <Route path="/kit-tareas-chef-privado" element={<KitTareasChefPrivado />} />
            <Route path="/kit-tareas-chef-privado-access" element={<KitTareasChefPrivadoAccessGate />} />
            <Route
              path="/kit-tareas-chef-privado-library"
              element={
                <ProtectedRoute storageKey="kit-tareas-chef-privado-jwt" redirectTo="/kit-tareas-chef-privado">
                  <KitTareasChefPrivadoDashboard />
                </ProtectedRoute>
              }
            />

            {/* Kit Gestion de Personal y Turnos */}
            <Route path="/kit-gestion-personal" element={<KitGestionPersonal />} />
            <Route path="/kit-gestion-personal-access" element={<KitGestionPersonalAccessGate />} />
            <Route
              path="/kit-gestion-personal-library"
              element={
                <ProtectedRoute storageKey="kit-gestion-personal-jwt" redirectTo="/kit-gestion-personal">
                  <KitGestionPersonalDashboard />
                </ProtectedRoute>
              }
            />

            {/* Kit Control de Inventario y Compras */}
            <Route path="/kit-inventario" element={<KitInventario />} />
            <Route path="/kit-inventario-access" element={<KitInventarioAccessGate />} />
            <Route
              path="/kit-inventario-library"
              element={
                <ProtectedRoute storageKey="kit-inventario-jwt" redirectTo="/kit-inventario">
                  <KitInventarioDashboard />
                </ProtectedRoute>
              }
            />

            {/* Mega Pack Tareas Recurrentes */}
            <Route path="/mega-pack-tareas" element={<MegaPackTareas />} />
            <Route path="/mega-pack-tareas-access" element={<MegaPackTareasAccessGate />} />
            <Route
              path="/mega-pack-tareas-library"
              element={
                <ProtectedRoute storageKey="mega-pack-tareas-jwt" redirectTo="/mega-pack-tareas">
                  <MegaPackTareasDashboard />
                </ProtectedRoute>
              }
            />

            {/* Kit Plan Financiero para Restaurantes */}
            <Route path="/kit-plan-financiero" element={<KitPlanFinanciero />} />
            <Route path="/kit-plan-financiero-access" element={<KitPlanFinancieroAccessGate />} />
            <Route
              path="/kit-plan-financiero-library"
              element={
                <ProtectedRoute storageKey="kit-plan-financiero-jwt" redirectTo="/kit-plan-financiero">
                  <KitPlanFinancieroDashboard />
                </ProtectedRoute>
              }
            />

            {/* Pro Prompts eBook & Library */}
            <Route path="/pro-prompts-ebook" element={<ProPromptsEbook />} />
            <Route path="/pro-prompts-library-access" element={<AccessGate />} />
            <Route
              path="/pro-prompts-library"
              element={
                <ProtectedRoute>
                  <ProPromptsLibrary />
                </ProtectedRoute>
              }
            />

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
