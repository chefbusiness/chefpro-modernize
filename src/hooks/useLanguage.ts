import { useState } from 'react';

export type Language = 'es' | 'en' | 'fr' | 'de' | 'it' | 'pt' | 'nl';

const translations = {
  es: {
    nav: {
      inicio: 'Inicio',
      plataformas: 'Plataformas', 
      servicios: 'Servicios',
      recursos: 'Recursos',
      contacto: 'Contacto',
      blog: 'Blog',
      login: 'Iniciar Sesión'
    },
    cta: {
      primary: 'PROBAR GRATIS AHORA',
      secondary: 'Prueba AI Chef Pro'
    },
    hero: {
      title: 'Transforma tu Gestión con AI Chef Pro',
      subtitle: '55+ Herramientas de IA Especializadas para Chefs. Desde Creatividad Culinaria hasta Marketing Digital.',
      description: 'Suite de Herramientas y Aplicaciones de Inteligencia Artificial, modelos entrenados para el uso cotidiano de Chefs, Cocineros y profesionales de la hostelería.',
      rating: 'Calificación: 5 estrellas'
    }
  },
  en: {
    nav: {
      inicio: 'Home',
      plataformas: 'Platforms',
      servicios: 'Services', 
      recursos: 'Resources',
      contacto: 'Contact',
      blog: 'Blog',
      login: 'Sign In'
    },
    cta: {
      primary: 'TRY FREE NOW',
      secondary: 'Try AI Chef Pro'
    },
    hero: {
      title: 'Transform your Management with AI Chef Pro',
      subtitle: '55+ Specialized AI Tools for Chefs. From Culinary Creativity to Digital Marketing.',
      description: 'Suite of AI Tools and Applications, models trained for daily use by Chefs, Cooks and hospitality professionals.',
      rating: 'Rating: 5 stars'
    }
  },
  fr: {
    nav: {
      inicio: 'Accueil',
      plataformas: 'Plateformes',
      servicios: 'Services',
      recursos: 'Ressources', 
      contacto: 'Contact',
      blog: 'Blog',
      login: 'Se connecter'
    },
    cta: {
      primary: 'ESSAYER GRATUITEMENT',
      secondary: 'Essayer AI Chef Pro'
    },
    hero: {
      title: 'Transformez votre Gestion avec AI Chef Pro',
      subtitle: '55+ Outils IA Spécialisés pour Chefs. De la Créativité Culinaire au Marketing Digital.',
      description: 'Suite d\'outils IA et applications, modèles entraînés pour l\'usage quotidien des Chefs, Cuisiniers et professionnels de l\'hôtellerie.',
      rating: 'Note: 5 étoiles'
    }
  },
  de: {
    nav: {
      inicio: 'Startseite',
      plataformas: 'Plattformen',
      servicios: 'Dienstleistungen',
      recursos: 'Ressourcen',
      contacto: 'Kontakt', 
      blog: 'Blog',
      login: 'Anmelden'
    },
    cta: {
      primary: 'JETZT KOSTENLOS TESTEN',
      secondary: 'AI Chef Pro testen'
    },
    hero: {
      title: 'Transformieren Sie Ihr Management mit AI Chef Pro',
      subtitle: '55+ Spezialisierte KI-Tools für Köche. Von Kulinarischer Kreativität bis Digital Marketing.',
      description: 'Suite von KI-Tools und Anwendungen, Modelle für den täglichen Gebrauch von Köchen und Gastronomiefachleuten.',
      rating: 'Bewertung: 5 Sterne'
    }
  },
  it: {
    nav: {
      inicio: 'Home',
      plataformas: 'Piattaforme',
      servicios: 'Servizi',
      recursos: 'Risorse',
      contacto: 'Contatto',
      blog: 'Blog', 
      login: 'Accedi'
    },
    cta: {
      primary: 'PROVA GRATIS ORA',
      secondary: 'Prova AI Chef Pro'
    },
    hero: {
      title: 'Trasforma la tua Gestione con AI Chef Pro',
      subtitle: '55+ Strumenti IA Specializzati per Chef. Dalla Creatività Culinaria al Marketing Digitale.',
      description: 'Suite di Strumenti IA e Applicazioni, modelli addestrati per l\'uso quotidiano di Chef, Cuochi e professionisti dell\'ospitalità.',
      rating: 'Valutazione: 5 stelle'
    }
  },
  pt: {
    nav: {
      inicio: 'Início',
      plataformas: 'Plataformas',
      servicios: 'Serviços',
      recursos: 'Recursos', 
      contacto: 'Contato',
      blog: 'Blog',
      login: 'Entrar'
    },
    cta: {
      primary: 'TESTAR GRÁTIS AGORA',
      secondary: 'Testar AI Chef Pro'
    },
    hero: {
      title: 'Transforme sua Gestão com AI Chef Pro',
      subtitle: '55+ Ferramentas IA Especializadas para Chefs. Da Criatividade Culinária ao Marketing Digital.',
      description: 'Suite de Ferramentas IA e Aplicações, modelos treinados para uso diário de Chefs, Cozinheiros e profissionais da hospitalidade.',
      rating: 'Avaliação: 5 estrelas'
    }
  },
  nl: {
    nav: {
      inicio: 'Home',
      plataformas: 'Platforms',
      servicios: 'Diensten',
      recursos: 'Bronnen',
      contacto: 'Contact',
      blog: 'Blog',
      login: 'Inloggen'
    },
    cta: {
      primary: 'PROBEER NU GRATIS',
      secondary: 'Probeer AI Chef Pro'
    },
    hero: {
      title: 'Transformeer uw Beheer met AI Chef Pro',
      subtitle: '55+ Gespecialiseerde AI-tools voor Chefs. Van Culinaire Creativiteit tot Digitale Marketing.',
      description: 'Suite van AI-tools en Toepassingen, modellen getraind voor dagelijks gebruik door Chefs, Koks en horeca-professionals.',
      rating: 'Beoordeling: 5 sterren'
    }
  }
};

export const useLanguage = () => {
  const [currentLanguage, setCurrentLanguage] = useState<Language>('es');
  
  const t = translations[currentLanguage];
  
  const changeLanguage = (lang: Language) => {
    setCurrentLanguage(lang);
  };

  const getAppUrl = (lang: Language) => {
    return lang === 'en' ? 'https://appen.aichef.pro' : 'https://app.aichef.pro';
  };
  
  return {
    currentLanguage,
    changeLanguage,
    t,
    getAppUrl
  };
};