import { useLocation } from "react-router-dom";
import { useEffect } from "react";
import SEOHead from "@/components/SEOHead";
import { useTranslation } from "react-i18next";

const NotFound = () => {
  const location = useLocation();
  const { t } = useTranslation();

  useEffect(() => {
    console.error(
      "404 Error: User attempted to access non-existent route:",
      location.pathname
    );
  }, [location.pathname]);

  return (
    <>
      <SEOHead 
        title="404 - Página no encontrada | AI Chef Pro"
        description="Lo sentimos, la página que buscas no existe. Regresa al inicio de AI Chef Pro."
        noindex={true}
      />
      <div className="min-h-screen flex items-center justify-center bg-background">
        <div className="text-center">
          <h1 className="text-4xl font-bold mb-4 text-foreground">404</h1>
          <p className="text-xl text-muted-foreground mb-4">Oops! Página no encontrada</p>
          <a href="/" className="text-primary hover:text-primary/80 underline">
            Volver al Inicio
          </a>
        </div>
      </div>
    </>
  );
};

export default NotFound;
