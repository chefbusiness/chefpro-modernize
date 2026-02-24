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
