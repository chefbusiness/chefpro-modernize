import { useState } from 'react';
import { useForm } from 'react-hook-form';
import { zodResolver } from '@hookform/resolvers/zod';
import { z } from 'zod';
import { Helmet } from 'react-helmet-async';
import ModernHeader from '@/components/ModernHeader';
import ModernFooter from '@/components/ModernFooter';
import SEOHead from '@/components/SEOHead';
import AIImageGallery from '@/components/AIImageGallery';
import { Button } from '@/components/ui/button';
import { Card, CardContent, CardDescription, CardHeader, CardTitle, CardFooter } from '@/components/ui/card';
import { Badge } from '@/components/ui/badge';
import { Input } from '@/components/ui/input';
import { Textarea } from '@/components/ui/textarea';
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from '@/components/ui/select';
import { Form, FormControl, FormField, FormItem, FormLabel, FormMessage } from '@/components/ui/form';
import { Accordion, AccordionContent, AccordionItem, AccordionTrigger } from '@/components/ui/accordion';
import { useToast } from '@/hooks/use-toast';
import { Mic, Clock, Users, GraduationCap, Building2, CheckCircle2, Award, BookOpen, Headphones, FileText, Shield, Star, ChefHat, Utensils, Hotel, School, FlaskConical, Send, MapPin, Sparkles, Brain, Target } from 'lucide-react';

// Import training images
import formacionWorkshop from '@/assets/formacion-workshop.jpg';
import formacionConferencia from '@/assets/formacion-conferencia.jpg';
import formacionPractica from '@/assets/formacion-practica.jpg';
import formacionInhouse from '@/assets/formacion-inhouse.jpg';
import chefJohnGuerrero from '@/assets/chef-john-guerrero.png';

// Form validation schema
const contactFormSchema = z.object({
  nombre: z.string().min(2, 'El nombre debe tener al menos 2 caracteres').max(100),
  email: z.string().email('Email inválido').max(255),
  telefono: z.string().min(9, 'Teléfono inválido').max(20),
  organizacion: z.string().min(1, 'Selecciona un tipo de organización'),
  servicio: z.string().min(1, 'Selecciona un servicio de interés'),
  comentarios: z.string().max(1000).optional()
});
type ContactFormData = z.infer<typeof contactFormSchema>;

// Service color configurations
const serviceColors = {
  conferencia: {
    gradient: 'from-amber-500/10 to-orange-500/10',
    iconBg: 'bg-amber-500/20',
    iconColor: 'text-amber-600',
    border: 'border-amber-500/30',
    price: 'text-amber-600'
  },
  workshop: {
    gradient: 'from-emerald-500/10 to-teal-500/10',
    iconBg: 'bg-emerald-500/20',
    iconColor: 'text-emerald-600',
    border: 'border-emerald-500/30',
    price: 'text-emerald-600'
  },
  'programa-completo': {
    gradient: 'from-blue-500/10 to-indigo-500/10',
    iconBg: 'bg-blue-500/20',
    iconColor: 'text-blue-600',
    border: 'border-blue-500/30',
    price: 'text-blue-600'
  },
  institucional: {
    gradient: 'from-purple-500/10 to-violet-500/10',
    iconBg: 'bg-purple-500/20',
    iconColor: 'text-purple-600',
    border: 'border-purple-500/30',
    price: 'text-purple-600'
  },
  consultoria: {
    gradient: 'from-pink-500/10 to-rose-500/10',
    iconBg: 'bg-pink-500/20',
    iconColor: 'text-pink-600',
    border: 'border-pink-500/30',
    price: 'text-pink-600'
  }
};
const FormacionPresencial = () => {
  const {
    toast
  } = useToast();
  const [isSubmitting, setIsSubmitting] = useState(false);
  const form = useForm<ContactFormData>({
    resolver: zodResolver(contactFormSchema),
    defaultValues: {
      nombre: '',
      email: '',
      telefono: '',
      organizacion: '',
      servicio: '',
      comentarios: ''
    }
  });
  const onSubmit = async (data: ContactFormData) => {
    setIsSubmitting(true);

    // Simulate form submission
    await new Promise(resolve => setTimeout(resolve, 1000));
    console.log('Form submitted:', data);
    toast({
      title: "¡Propuesta Solicitada!",
      description: "Nos pondremos en contacto contigo en menos de 24 horas."
    });
    form.reset();
    setIsSubmitting(false);
  };
  const scrollToForm = () => {
    document.getElementById('contacto-formacion')?.scrollIntoView({
      behavior: 'smooth'
    });
  };

  // Structured data schemas
  const breadcrumbSchema = {
    "@context": "https://schema.org",
    "@type": "BreadcrumbList",
    "itemListElement": [{
      "@type": "ListItem",
      "position": 1,
      "name": "Inicio",
      "item": "https://aichef.pro"
    }, {
      "@type": "ListItem",
      "position": 2,
      "name": "Servicios",
      "item": "https://aichef.pro/servicios"
    }, {
      "@type": "ListItem",
      "position": 3,
      "name": "Formación Presencial",
      "item": "https://aichef.pro/formacion-presencial"
    }]
  };
  const serviceSchema = {
    "@context": "https://schema.org",
    "@type": "EducationalOrganization",
    "name": "AI Chef Pro Academy",
    "description": "Formación presencial especializada en Inteligencia Artificial aplicada a la gastronomía profesional",
    "url": "https://aichef.pro/formacion-presencial",
    "provider": {
      "@type": "Organization",
      "name": "AI Chef Pro",
      "url": "https://aichef.pro"
    },
    "hasOfferCatalog": {
      "@type": "OfferCatalog",
      "name": "Servicios de Formación Presencial",
      "itemListElement": [{
        "@type": "Offer",
        "itemOffered": {
          "@type": "Course",
          "name": "Conferencia Magistral",
          "description": "La Revolución de la IA en la Cocina Profesional"
        },
        "price": "990",
        "priceCurrency": "EUR"
      }, {
        "@type": "Offer",
        "itemOffered": {
          "@type": "Course",
          "name": "Workshop Intensivo",
          "description": "Domina la IA en tu Cocina"
        },
        "price": "1490",
        "priceCurrency": "EUR"
      }, {
        "@type": "Offer",
        "itemOffered": {
          "@type": "Course",
          "name": "Programa Formativo Completo",
          "description": "Transformación Digital de tu Cocina con IA"
        },
        "price": "2490",
        "priceCurrency": "EUR"
      }, {
        "@type": "Offer",
        "itemOffered": {
          "@type": "Course",
          "name": "Programa Institucional",
          "description": "IA en la Educación Gastronómica"
        },
        "price": "4990",
        "priceCurrency": "EUR"
      }, {
        "@type": "Offer",
        "itemOffered": {
          "@type": "Course",
          "name": "Consultoría Estratégica In-House",
          "description": "Transformación Digital Total"
        },
        "priceSpecification": {
          "@type": "PriceSpecification",
          "minPrice": "4990",
          "priceCurrency": "EUR"
        }
      }]
    }
  };
  const services = [{
    id: 'conferencia',
    icon: Mic,
    name: 'Conferencia Magistral',
    subtitle: '"La Revolución de la IA en la Cocina Profesional"',
    duration: '90-120 minutos',
    attendees: 'Hasta 200 personas',
    price: '990€',
    idealFor: 'Eventos, congresos, jornadas de asociaciones, inauguraciones de curso',
    includes: ['Material digital para asistentes', 'Código de prueba AI Chef Pro (7 días)', 'Certificado de asistencia personalizado'],
    content: ['Estado actual de la IA en gastronomía mundial', 'Demostración en vivo de herramientas AI Chef Pro', 'Casos de éxito y ROI demostrable', 'El futuro inmediato: tendencias 2025-2030', 'Sesión de preguntas y networking']
  }, {
    id: 'workshop',
    icon: Users,
    name: 'Workshop Intensivo',
    subtitle: '"Domina la IA en tu Cocina"',
    duration: '4 horas',
    attendees: '12-25 personas',
    price: '1.490€',
    idealFor: 'Equipos de cocina, estudiantes avanzados, mandos intermedios',
    includes: ['Licencia AI Chef Pro Premium (1 mes) por asistente', 'Manual de implementación digital', 'Biblioteca de prompts optimizados', 'Soporte post-formación (15 días)'],
    content: ['Fundamentos de IA generativa para gastronomía', 'Práctica guiada con AI Chef Pro', 'Aplicación a casos reales del establecimiento', 'Plan de implementación personalizado']
  }, {
    id: 'programa-completo',
    icon: GraduationCap,
    name: 'Programa Formativo Completo',
    subtitle: '"Transformación Digital de tu Cocina con IA"',
    duration: '8 horas (jornada completa)',
    attendees: '10-20 personas',
    price: '2.490€',
    popular: true,
    idealFor: 'Equipos completos de restaurantes, brigadas de cocina',
    includes: ['Licencia AI Chef Pro Premium Plus (2 meses) por asistente', 'Manual de implementación completo (físico + digital)', 'Biblioteca completa de prompts profesionales', 'Sesión de seguimiento online (1h) a los 30 días', 'Certificado profesional AI Chef Pro Academy', 'Soporte prioritario (30 días)'],
    content: ['Fundamentos de IA generativa y aplicaciones', 'Masterclass: Creatividad culinaria con IA', 'Gestión operativa con IA (Mermas, Alérgenos)', 'Marketing gastronómico con IA', 'Bienestar del equipo: Mental Coach AI']
  }, {
    id: 'institucional',
    icon: School,
    name: 'Programa Institucional',
    subtitle: '"IA en la Educación Gastronómica"',
    duration: '16-24 horas (2-3 días)',
    attendees: 'Hasta 30 personas por sesión',
    price: '4.990€',
    idealFor: 'Escuelas de cocina, facultades gastronómicas, centros FP, universidades',
    includes: ['Licencias institucionales AI Chef Pro (curso académico)', 'Material didáctico adaptado al nivel formativo', 'Guía para profesores/instructores', 'Sistema de evaluación y rúbricas', 'Certificación acreditada AI Chef Pro Academy', 'Posibilidad de bonificación FUNDAE'],
    content: ['Módulo 1: Fundamentos de IA (4h)', 'Módulo 2: Creatividad y recetas con IA (4h)', 'Módulo 3: Gestión operativa y costes (4h)', 'Módulo 4: Marketing digital gastronómico (4h)', 'Módulo 5 (opcional): Proyecto final (4h)']
  }, {
    id: 'consultoria',
    icon: Building2,
    name: 'Consultoría Estratégica In-House',
    subtitle: '"Transformación Digital Total"',
    duration: '2-5 días (proyecto a medida)',
    attendees: 'Toda la organización',
    price: 'Desde 4.990€',
    idealFor: 'Grupos de restauración, hoteles, cocinas centrales, empresas de catering',
    includes: ['Licencias corporativas AI Chef Pro', 'Informe de diagnóstico detallado', 'Plan de transformación digital documentado', 'Formación presencial personalizada', 'Soporte prioritario durante implementación', 'Sesiones de seguimiento trimestrales (primer año)'],
    content: ['Diagnóstico inicial de procesos', 'Plan de transformación personalizado', 'Formación del equipo por roles', 'Implementación guiada de herramientas', 'Seguimiento y optimización continua']
  }];
  const targetAudience = [{
    icon: School,
    name: 'Escuelas de Cocina',
    description: 'Facultades gastronómicas, FP y universidades',
    need: 'Actualizar curriculum con competencias digitales y IA',
    color: 'purple'
  }, {
    icon: Utensils,
    name: 'Grupos de Restauración',
    description: 'Cadenas, franquicias y holdings gastronómicos',
    need: 'Estandarización, eficiencia operativa, reducción de costes',
    color: 'blue'
  }, {
    icon: ChefHat,
    name: 'Asociaciones Profesionales',
    description: 'Federaciones de hostelería, colegios de chefs',
    need: 'Formación continua para asociados, eventos de valor',
    color: 'amber'
  }, {
    icon: FlaskConical,
    name: 'Centros de I+D',
    description: 'Laboratorios alimentarios, innovación gastronómica',
    need: 'Integración de IA en procesos de investigación',
    color: 'emerald'
  }, {
    icon: Hotel,
    name: 'Hoteles y Resorts',
    description: 'Departamentos F&B, cocinas centrales',
    need: 'Optimización de operaciones a escala',
    color: 'pink'
  }];
  const benefits = [{
    icon: CheckCircle2,
    title: 'Aprendizaje Práctico Real',
    description: 'Trabaja directamente con las herramientas en tu propia cocina',
    color: 'emerald'
  }, {
    icon: Award,
    title: 'Adaptación a Tu Realidad',
    description: 'Contenido personalizado según tu tipo de establecimiento',
    color: 'amber'
  }, {
    icon: Clock,
    title: 'Implementación Inmediata',
    description: 'Empieza a aplicar lo aprendido el mismo día',
    color: 'blue'
  }, {
    icon: Users,
    title: 'Formación del Equipo Completo',
    description: 'Toda tu brigada alineada en el uso de IA',
    color: 'purple'
  }, {
    icon: Headphones,
    title: 'Seguimiento Garantizado',
    description: 'No te quedas solo después de la formación',
    color: 'pink'
  }];
  const valueItems = [{
    icon: Star,
    text: 'Acceso a AI Chef Pro (55+ herramientas de IA gastronómica)',
    color: 'amber'
  }, {
    icon: BookOpen,
    text: 'Material formativo físico y digital',
    color: 'blue'
  }, {
    icon: FileText,
    text: 'Biblioteca de prompts profesionales',
    color: 'emerald'
  }, {
    icon: Award,
    text: 'Certificación oficial AI Chef Pro Academy',
    color: 'purple'
  }, {
    icon: Headphones,
    text: 'Soporte post-formación incluido',
    color: 'pink'
  }, {
    icon: Shield,
    text: 'Posibilidad de bonificación FUNDAE',
    color: 'teal'
  }];
  const faqs = [{
    question: '¿Dónde se imparten las formaciones?',
    answer: 'Me desplazo a tus instalaciones. Toda España peninsular, Baleares, Canarias y otros países bajo consulta. Los gastos de desplazamiento y alojamiento se presupuestan según ubicación.'
  }, {
    question: '¿Se puede bonificar por FUNDAE?',
    answer: 'Sí, gestionamos la bonificación según el tipo de empresa y formación. Consulta con nosotros para conocer las opciones disponibles para tu organización.'
  }, {
    question: '¿Qué necesitamos para la formación?',
    answer: 'Un espacio con proyector/pantalla y conexión a internet. Los asistentes necesitan dispositivo (móvil, tablet o portátil) para las prácticas.'
  }, {
    question: '¿Cuánto tiempo de antelación necesitáis?',
    answer: 'Recomendamos un mínimo de 2-3 semanas para preparar contenido personalizado y garantizar disponibilidad.'
  }, {
    question: '¿Qué dispositivos necesitan los asistentes?',
    answer: 'Cualquier dispositivo con conexión a internet: smartphone, tablet o portátil. AI Chef Pro funciona en cualquier navegador moderno.'
  }, {
    question: '¿IVA incluido en los precios?',
    answer: 'Los precios indicados no incluyen IVA (21%). Se aplicará según la normativa vigente.'
  }];
  const organizationTypes = ['Escuela de Cocina / Centro Formativo', 'Restaurante / Grupo de Restauración', 'Hotel / Resort', 'Asociación Profesional', 'Jornadas Gastronómicas', 'Congreso Gastronómico', 'Centro de I+D Alimentario', 'Empresa de Catering', 'Otro'];
  const trainingImages = [{
    src: formacionWorkshop,
    alt: 'Workshop intensivo de IA para chefs profesionales',
    caption: 'Workshop Intensivo'
  }, {
    src: formacionConferencia,
    alt: 'Conferencia magistral AI Chef Pro',
    caption: 'Conferencia Magistral'
  }, {
    src: formacionPractica,
    alt: 'Sesión práctica de IA en cocina profesional',
    caption: 'Formación Práctica'
  }, {
    src: formacionInhouse,
    alt: 'Consultoría in-house en restaurante',
    caption: 'Consultoría In-House'
  }];
  const getColorClasses = (color: string) => {
    const colors: Record<string, {
      bg: string;
      iconBg: string;
      text: string;
      border: string;
    }> = {
      emerald: {
        bg: 'bg-emerald-50',
        iconBg: 'bg-emerald-500/20',
        text: 'text-emerald-600',
        border: 'border-emerald-500/30'
      },
      amber: {
        bg: 'bg-amber-50',
        iconBg: 'bg-amber-500/20',
        text: 'text-amber-600',
        border: 'border-amber-500/30'
      },
      blue: {
        bg: 'bg-blue-50',
        iconBg: 'bg-blue-500/20',
        text: 'text-blue-600',
        border: 'border-blue-500/30'
      },
      purple: {
        bg: 'bg-purple-50',
        iconBg: 'bg-purple-500/20',
        text: 'text-purple-600',
        border: 'border-purple-500/30'
      },
      pink: {
        bg: 'bg-pink-50',
        iconBg: 'bg-pink-500/20',
        text: 'text-pink-600',
        border: 'border-pink-500/30'
      },
      teal: {
        bg: 'bg-teal-50',
        iconBg: 'bg-teal-500/20',
        text: 'text-teal-600',
        border: 'border-teal-500/30'
      }
    };
    return colors[color] || colors.amber;
  };
  return <div className="min-h-screen bg-background overflow-x-hidden">
      <SEOHead title="Formación Presencial IA para Restaurantes | AI Chef Pro Academy" description="Workshops, conferencias y programas in-house de IA para hostelería. Chef John Guerrero lleva las 55+ herramientas de AI Chef Pro directamente a tu cocina." keywords="formación IA restaurantes, curso inteligencia artificial hostelería, workshop IA cocina profesional, consultoría IA restaurantes, formación presencial IA gastronomía" />
      
      <Helmet>
        <script type="application/ld+json">
          {JSON.stringify(breadcrumbSchema)}
        </script>
        <script type="application/ld+json">
          {JSON.stringify(serviceSchema)}
        </script>
      </Helmet>

      <ModernHeader />

      {/* Hero Section - With warm gradient and image */}
      <section className="relative py-12 sm:py-16 md:py-24 overflow-hidden">
        <div className="absolute inset-0 bg-gradient-to-br from-amber-50 via-background to-orange-50" />
        <div className="absolute inset-0 bg-[radial-gradient(ellipse_at_top_right,_var(--tw-gradient-stops))] from-amber-100/40 via-transparent to-transparent" />
        
        <div className="container relative px-4 sm:px-6">
          <div className="grid lg:grid-cols-2 gap-8 lg:gap-12 items-center">
            <div className="text-center lg:text-left max-w-full">
              <Badge className="mb-4 px-3 sm:px-4 py-2 bg-amber-100 text-amber-800 border-amber-300 max-w-full flex-wrap">
                <GraduationCap className="h-4 w-4 mr-2 flex-shrink-0" />
                <span className="text-xs sm:text-sm">AI Chef Pro Academy - Formación Presencial</span>
              </Badge>
              
              <h1 className="text-3xl sm:text-4xl md:text-5xl lg:text-6xl font-bold tracking-tight mb-6 leading-tight text-balance break-words">
                Llevo la Revolución de la IA{' '}
                <span className="block sm:inline bg-gradient-to-r from-amber-600 to-orange-600 bg-clip-text text-transparent">
                  Directamente a Tu Negocio
                </span>
              </h1>
              
              <p className="text-lg sm:text-xl md:text-2xl text-muted-foreground mb-8">
                Formación presencial especializada en Inteligencia Artificial aplicada a la gastronomía profesional. 
                Workshops, conferencias y programas in-house para escuelas de cocina, grupos de restauración y equipos de hostelería.
              </p>
              
              <div className="flex flex-col sm:flex-row gap-3 sm:gap-4 justify-center lg:justify-start mb-8 sm:mb-12">
                <Button size="lg" onClick={scrollToForm} className="w-full sm:w-auto text-base sm:text-lg px-4 sm:px-8 bg-gradient-to-r from-amber-500 to-orange-500 hover:from-amber-600 hover:to-orange-600 text-white whitespace-normal">
                  <Send className="mr-2 h-5 w-5 flex-shrink-0" />
                  <span className="sm:hidden">Solicitar Propuesta</span>
                  <span className="hidden sm:inline">Solicitar Propuesta Personalizada</span>
                </Button>
                <Button size="lg" variant="outline" onClick={() => document.getElementById('servicios')?.scrollIntoView({
                behavior: 'smooth'
              })} className="w-full sm:w-auto border-amber-500/50 hover:bg-amber-50">
                  Ver Servicios y Precios
                </Button>
              </div>
              
              {/* Stats with color - Responsive */}
              <div className="grid grid-cols-2 md:grid-cols-4 gap-2 sm:gap-4">
                <div className="bg-amber-100/80 rounded-xl p-3 sm:p-4 text-center border border-amber-200 min-w-0">
                  <div className="text-2xl sm:text-3xl font-bold text-amber-700">55+</div>
                  <div className="text-xs sm:text-sm text-amber-600">Herramientas IA</div>
                </div>
                <div className="bg-emerald-100/80 rounded-xl p-3 sm:p-4 text-center border border-emerald-200 min-w-0">
                  <div className="text-2xl sm:text-3xl font-bold text-emerald-700">100%</div>
                  <div className="text-xs sm:text-sm text-emerald-600">IA Gastronómica</div>
                </div>
                <div className="bg-blue-100/80 rounded-xl p-3 sm:p-4 text-center border border-blue-200 min-w-0">
                  <div className="text-2xl sm:text-3xl font-bold text-blue-700">Único</div>
                  <div className="text-xs sm:text-sm text-blue-600">en España</div>
                </div>
                <div className="bg-purple-100/80 rounded-xl p-3 sm:p-4 text-center border border-purple-200 min-w-0">
                  <div className="text-2xl sm:text-3xl font-bold text-purple-700">ROI</div>
                  <div className="text-xs sm:text-sm text-purple-600">Inmediato</div>
                </div>
              </div>
            </div>
            
            {/* Hero Image */}
            <div className="hidden lg:block">
              <div className="relative">
                <div className="absolute -inset-4 bg-gradient-to-r from-amber-400/20 to-orange-400/20 rounded-3xl blur-2xl" />
                <img src={formacionConferencia} alt="Conferencia AI Chef Pro" className="relative rounded-2xl shadow-2xl border-4 border-white/50" />
                <div className="absolute -bottom-4 -right-4 bg-white rounded-xl shadow-lg p-4 border border-amber-100">
                  <div className="flex items-center gap-3">
                    <div className="w-12 h-12 rounded-full bg-gradient-to-br from-amber-400 to-orange-500 flex items-center justify-center">
                      <Brain className="h-6 w-6 text-white" />
                    </div>
                    <div>
                      <div className="font-bold text-slate-900">55+ Apps IA</div>
                      <div className="text-sm text-slate-500">Especializadas</div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* Por qué Formación Presencial */}
      <section className="py-16 bg-gradient-to-b from-amber-50/50 to-background">
        <div className="container">
          <div className="text-center mb-12">
            <Badge className="mb-4 bg-emerald-100 text-emerald-800 border-emerald-300">
              <Target className="h-3 w-3 mr-1" />
              Ventajas Únicas
            </Badge>
            <h2 className="text-3xl md:text-4xl font-bold mb-4">¿Por Qué Formación Presencial?</h2>
            <p className="text-lg text-muted-foreground max-w-2xl mx-auto">
              La formación presencial ofrece ventajas únicas que marcan la diferencia en la implementación de IA
            </p>
          </div>
          
          <div className="grid md:grid-cols-2 lg:grid-cols-5 gap-6">
            {benefits.map((benefit, index) => {
            const colors = getColorClasses(benefit.color);
            return <Card key={index} className={`text-center hover:shadow-lg transition-all hover:-translate-y-1 border-t-4 ${colors.border}`}>
                  <CardHeader>
                    <div className={`mx-auto w-14 h-14 rounded-xl ${colors.iconBg} flex items-center justify-center mb-2`}>
                      <benefit.icon className={`h-7 w-7 ${colors.text}`} />
                    </div>
                    <CardTitle className="text-lg">{benefit.title}</CardTitle>
                  </CardHeader>
                  <CardContent>
                    <p className="text-sm text-muted-foreground">{benefit.description}</p>
                  </CardContent>
                </Card>;
          })}
          </div>
        </div>
      </section>

      {/* Galería de Imágenes Gastronómicas (AIImageGallery) */}
      <AIImageGallery />

      {/* Formación en Acción - Mini Gallery */}
      <section className="py-16 bg-gradient-to-b from-slate-900 to-slate-800">
        <div className="container">
          <div className="text-center mb-12">
            <Badge className="mb-4 bg-amber-500/20 text-amber-400 border-amber-500/30">
              <Sparkles className="h-3 w-3 mr-1" />
              Formación en Acción
            </Badge>
            <h2 className="text-3xl md:text-4xl font-bold mb-4 text-white">
              Así Son Nuestras Formaciones
            </h2>
            <p className="text-lg text-slate-300 max-w-2xl mx-auto">
              Workshops prácticos, conferencias inspiradoras y consultoría personalizada en tu propia cocina
            </p>
          </div>
          
          <div className="grid grid-cols-2 md:grid-cols-4 gap-4 max-w-5xl mx-auto">
            {trainingImages.map((image, index) => <div key={index} className="group relative overflow-hidden rounded-xl">
                <img src={image.src} alt={image.alt} className="w-full aspect-[4/3] object-cover transition-transform duration-500 group-hover:scale-110" />
                <div className="absolute inset-0 bg-gradient-to-t from-black/80 via-black/20 to-transparent" />
                <div className="absolute bottom-0 left-0 right-0 p-4">
                  <p className="text-white font-semibold text-sm md:text-base">{image.caption}</p>
                </div>
              </div>)}
          </div>
        </div>
      </section>

      {/* Quién Soy */}
      <section className="py-16 bg-gradient-to-b from-background to-amber-50/30">
        <div className="container">
          <div className="max-w-4xl mx-auto">
            <Card className="overflow-hidden border-0 shadow-xl">
              <div className="grid md:grid-cols-3 gap-0">
                <div className="bg-gradient-to-br from-amber-400 via-orange-500 to-amber-600 p-8 flex items-center justify-center relative overflow-hidden">
                  <div className="absolute inset-0 bg-[url('data:image/svg+xml,...')] opacity-10" />
                  <div className="text-center relative z-10">
                    <div className="w-32 h-32 rounded-full mx-auto mb-4 overflow-hidden border-4 border-white/30 shadow-xl">
                      <img src={chefJohnGuerrero} alt="Chef John Guerrero - Especialista en IA Gastronómica" className="w-full h-full object-cover" />
                    </div>
                    <h3 className="text-xl font-bold text-white">Chef John Guerrero</h3>
                    <p className="text-sm text-amber-100">Desarrollador de AI Chef Pro</p>
                  </div>
                </div>
                <div className="md:col-span-2 p-8 bg-white">
                  <Badge className="mb-4 bg-amber-100 text-amber-800 border-amber-300">Sobre el Formador</Badge>
                  <h2 className="text-2xl font-bold mb-4">Especialista en IA Aplicada a la Gastronomía</h2>
                  <p className="text-muted-foreground mb-6">
                    Con más de 15 años de experiencia en consultoría gastronómica, he ayudado a cientos de restaurantes 
                    a optimizar sus operaciones y potenciar su creatividad. Como desarrollador de AI Chef Pro y su suite 
                    de 55+ herramientas de IA especializadas, pongo a tu disposición los conocimientos y tecnologías que 
                    están transformando la industria gastronómica.
                  </p>
                  <div className="flex flex-wrap gap-2">
                    <Badge className="bg-amber-100 text-amber-700">55+ Herramientas Propias</Badge>
                    <Badge className="bg-blue-100 text-blue-700">+15 Años Experiencia</Badge>
                    <Badge className="bg-purple-100 text-purple-700">Único en España</Badge>
                    <Badge className="bg-emerald-100 text-emerald-700">Consultoría Gastronómica</Badge>
                  </div>
                </div>
              </div>
            </Card>
          </div>
        </div>
      </section>

      {/* Servicios */}
      <section id="servicios" className="py-16 bg-gradient-to-b from-amber-50/30 to-slate-50">
        <div className="container">
          <div className="text-center mb-12">
            <Badge className="mb-4 bg-blue-100 text-blue-800 border-blue-300">5 Packs Disponibles</Badge>
            <h2 className="text-3xl md:text-4xl font-bold mb-4">Nuestros Servicios de Formación</h2>
            <p className="text-lg text-muted-foreground max-w-2xl mx-auto">
              Desde conferencias magistrales hasta programas de transformación digital completos
            </p>
          </div>
          
          <div className="grid lg:grid-cols-2 xl:grid-cols-3 gap-6">
            {services.map(service => {
            const colors = serviceColors[service.id as keyof typeof serviceColors];
            return <Card key={service.id} className={`relative overflow-hidden hover:shadow-xl transition-all hover:-translate-y-1 bg-gradient-to-br ${colors.gradient} ${service.popular ? 'ring-2 ring-blue-500' : ''}`}>
                  {service.popular && <div className="absolute top-0 right-0">
                      <Badge className="rounded-none rounded-bl-lg bg-blue-500 text-white">
                        Más Solicitado
                      </Badge>
                    </div>}
                  
                  <CardHeader>
                    <div className="flex items-start gap-4">
                      <div className={`w-14 h-14 rounded-xl ${colors.iconBg} flex items-center justify-center shrink-0`}>
                        <service.icon className={`h-7 w-7 ${colors.iconColor}`} />
                      </div>
                      <div>
                        <CardTitle className="text-xl">{service.name}</CardTitle>
                        <CardDescription className="text-sm italic">{service.subtitle}</CardDescription>
                      </div>
                    </div>
                  </CardHeader>
                  
                  <CardContent className="space-y-4">
                    <div className="flex flex-wrap gap-2 text-sm">
                      <Badge variant="outline" className={`flex items-center gap-1 ${colors.border}`}>
                        <Clock className="h-3 w-3" />
                        {service.duration}
                      </Badge>
                      <Badge variant="outline" className={`flex items-center gap-1 ${colors.border}`}>
                        <Users className="h-3 w-3" />
                        {service.attendees}
                      </Badge>
                    </div>
                    
                    <div className={`text-3xl font-bold ${colors.price}`}>{service.price}</div>
                    
                    <div>
                      <p className="text-sm font-medium mb-1">Ideal para:</p>
                      <p className="text-sm text-muted-foreground">{service.idealFor}</p>
                    </div>
                    
                    <div>
                      <p className="text-sm font-medium mb-2">Incluye:</p>
                      <ul className="space-y-1">
                        {service.includes.slice(0, 4).map((item, idx) => <li key={idx} className="text-sm text-muted-foreground flex items-start gap-2">
                            <CheckCircle2 className={`h-4 w-4 ${colors.iconColor} shrink-0 mt-0.5`} />
                            {item}
                          </li>)}
                        {service.includes.length > 4 && <li className="text-sm text-muted-foreground">
                            +{service.includes.length - 4} más...
                          </li>}
                      </ul>
                    </div>
                  </CardContent>
                  
                  <CardFooter>
                    <Button onClick={scrollToForm} className={`w-full bg-gradient-to-r ${colors.gradient.replace('/10', '')} hover:opacity-90`}>
                      Solicitar Propuesta
                    </Button>
                  </CardFooter>
                </Card>;
          })}
          </div>
          
          <p className="text-center text-sm text-muted-foreground mt-8">
            * Precios base para España peninsular. IVA no incluido. Gastos de desplazamiento según ubicación.
          </p>
        </div>
      </section>

      {/* Para Quién */}
      <section className="py-16 bg-gradient-to-b from-slate-50 to-purple-50/30">
        <div className="container">
          <div className="text-center mb-12">
            <Badge className="mb-4 bg-purple-100 text-purple-800 border-purple-300">
              <Users className="h-3 w-3 mr-1" />
              Audiencia
            </Badge>
            <h2 className="text-3xl md:text-4xl font-bold mb-4">¿Para Quién es Esta Formación?</h2>
            <p className="text-lg text-muted-foreground max-w-2xl mx-auto">
              Servicios adaptados a las necesidades específicas de cada tipo de organización
            </p>
          </div>
          
          <div className="grid md:grid-cols-2 lg:grid-cols-5 gap-6">
            {targetAudience.map((audience, index) => {
            const colors = getColorClasses(audience.color);
            return <Card key={index} className={`text-center hover:shadow-lg transition-all hover:-translate-y-1 group border-b-4 ${colors.border}`}>
                  <CardHeader>
                    <div className={`mx-auto w-16 h-16 rounded-2xl ${colors.iconBg} flex items-center justify-center mb-2 group-hover:scale-110 transition-transform`}>
                      <audience.icon className={`h-8 w-8 ${colors.text}`} />
                    </div>
                    <CardTitle className="text-lg">{audience.name}</CardTitle>
                    <CardDescription>{audience.description}</CardDescription>
                  </CardHeader>
                  <CardContent>
                    <p className="text-sm text-muted-foreground">{audience.need}</p>
                  </CardContent>
                </Card>;
          })}
          </div>
        </div>
      </section>

      {/* Qué Incluye */}
      <section className="py-16 bg-gradient-to-r from-amber-50/50 via-background to-orange-50/50">
        <div className="container">
          <div className="text-center mb-12">
            <Badge className="mb-4 bg-teal-100 text-teal-800 border-teal-300">¿Listo para Transformar tu Negocio de Hostelería con la Inteligencia Artificial?<Star className="h-3 w-3 mr-1" />
              Valor Incluido
            </Badge>
            <h2 className="text-3xl md:text-4xl font-bold mb-4">Qué Incluyen Nuestras Formaciones</h2>
            <p className="text-lg text-muted-foreground max-w-2xl mx-auto">
              Valor añadido en cada servicio para garantizar el éxito de la implementación
            </p>
          </div>
          
          <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-6 max-w-4xl mx-auto">
            {valueItems.map((item, index) => {
            const colors = getColorClasses(item.color);
            return <div key={index} className={`flex items-center gap-4 p-5 bg-white rounded-xl border shadow-sm hover:shadow-md transition-shadow ${colors.border}`}>
                  <div className={`w-12 h-12 rounded-xl ${colors.iconBg} flex items-center justify-center shrink-0`}>
                    <item.icon className={`h-6 w-6 ${colors.text}`} />
                  </div>
                  <p className="text-sm font-medium">{item.text}</p>
                </div>;
          })}
          </div>
        </div>
      </section>

      {/* Comparativa de Valor */}
      <section className="py-16 bg-white">
        <div className="container">
          <div className="text-center mb-12">
            <Badge className="mb-4 bg-amber-100 text-amber-800 border-amber-300">
              <Award className="h-3 w-3 mr-1" />
              Comparativa
            </Badge>
            <h2 className="text-3xl md:text-4xl font-bold mb-4">¿Por Qué AI Chef Pro Academy?</h2>
            <p className="text-lg text-muted-foreground max-w-2xl mx-auto">
              La única formación presencial en España 100% especializada en IA gastronómica
            </p>
          </div>
          
          <div className="max-w-4xl mx-auto">
            <Card className="overflow-hidden border-2 border-amber-200">
              <div className="overflow-x-auto">
                <table className="w-full">
                  <thead className="bg-gradient-to-r from-amber-100 to-orange-100">
                    <tr>
                      <th className="text-left p-4 font-medium">Aspecto</th>
                      <th className="text-center p-4 font-medium text-amber-700">AI Chef Pro Academy</th>
                      <th className="text-center p-4 font-medium text-muted-foreground">Competidores</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr className="border-t">
                      <td className="p-4">Herramientas Incluidas</td>
                      <td className="p-4 text-center font-medium text-amber-700">55+ apps propias</td>
                      <td className="p-4 text-center text-muted-foreground">Herramientas genéricas</td>
                    </tr>
                    <tr className="border-t bg-amber-50/30">
                      <td className="p-4">Especialización</td>
                      <td className="p-4 text-center font-medium text-amber-700">100% IA gastronómica</td>
                      <td className="p-4 text-center text-muted-foreground">IA genérica o parcial</td>
                    </tr>
                    <tr className="border-t">
                      <td className="p-4">Aplicación</td>
                      <td className="p-4 text-center font-medium text-amber-700">Mismo día</td>
                      <td className="p-4 text-center text-muted-foreground">Semanas/meses</td>
                    </tr>
                    <tr className="border-t bg-amber-50/30">
                      <td className="p-4">Enfoque</td>
                      <td className="p-4 text-center font-medium text-amber-700">Práctico hands-on</td>
                      <td className="p-4 text-center text-muted-foreground">Teórico general</td>
                    </tr>
                  </tbody>
                </table>
              </div>
            </Card>
          </div>
        </div>
      </section>

      {/* FAQ */}
      <section className="py-16 bg-gradient-to-b from-slate-50 to-background">
        <div className="container">
          <div className="max-w-3xl mx-auto">
            <div className="text-center mb-12">
              <Badge className="mb-4 bg-blue-100 text-blue-800 border-blue-300">FAQ</Badge>
              <h2 className="text-3xl md:text-4xl font-bold mb-4">Preguntas Frecuentes</h2>
              <p className="text-lg text-muted-foreground">
                Todo lo que necesitas saber antes de contratar tu formación
              </p>
            </div>
            
            <Accordion type="single" collapsible className="w-full">
              {faqs.map((faq, index) => <AccordionItem key={index} value={`item-${index}`} className="border rounded-lg mb-2 px-4">
                  <AccordionTrigger className="text-left hover:no-underline">{faq.question}</AccordionTrigger>
                  <AccordionContent className="text-muted-foreground">
                    {faq.answer}
                  </AccordionContent>
                </AccordionItem>)}
            </Accordion>
          </div>
        </div>
      </section>

      {/* Formulario de Contacto */}
      <section id="contacto-formacion" className="py-16 bg-gradient-to-br from-amber-50 via-background to-orange-50">
        <div className="container">
          <div className="max-w-2xl mx-auto">
            <div className="text-center mb-12">
              <Badge className="mb-4 bg-emerald-100 text-emerald-800 border-emerald-300">Sin Compromiso</Badge>
              <h2 className="text-3xl md:text-4xl font-bold mb-4">
                ¿Listo para Transformar tu Cocina con IA?
              </h2>
              <p className="text-lg text-muted-foreground">
                Solicita una propuesta personalizada y te contactaremos en menos de 24 horas
              </p>
            </div>
            
            <Card className="border-2 border-amber-200 shadow-xl">
              <CardHeader className="bg-gradient-to-r from-amber-50 to-orange-50">
                <CardTitle className="flex items-center gap-2">
                  <Send className="h-5 w-5 text-amber-600" />
                  Solicitar Propuesta Personalizada
                </CardTitle>
                <CardDescription>
                  Cuéntanos sobre tu organización y te prepararemos una propuesta a medida
                </CardDescription>
              </CardHeader>
              <CardContent className="pt-6">
                <Form {...form}>
                  <form onSubmit={form.handleSubmit(onSubmit)} className="space-y-6">
                    <div className="grid md:grid-cols-2 gap-4">
                      <FormField control={form.control} name="nombre" render={({
                      field
                    }) => <FormItem>
                            <FormLabel>Nombre completo *</FormLabel>
                            <FormControl>
                              <Input placeholder="Tu nombre" {...field} />
                            </FormControl>
                            <FormMessage />
                          </FormItem>} />
                      
                      <FormField control={form.control} name="email" render={({
                      field
                    }) => <FormItem>
                            <FormLabel>Email *</FormLabel>
                            <FormControl>
                              <Input type="email" placeholder="tu@email.com" {...field} />
                            </FormControl>
                            <FormMessage />
                          </FormItem>} />
                    </div>
                    
                    <FormField control={form.control} name="telefono" render={({
                    field
                  }) => <FormItem>
                          <FormLabel>Teléfono *</FormLabel>
                          <FormControl>
                            <Input type="tel" placeholder="+34 600 000 000" {...field} />
                          </FormControl>
                          <FormMessage />
                        </FormItem>} />
                    
                    <div className="grid md:grid-cols-2 gap-4">
                      <FormField control={form.control} name="organizacion" render={({
                      field
                    }) => <FormItem>
                            <FormLabel>Tipo de organización *</FormLabel>
                            <Select onValueChange={field.onChange} defaultValue={field.value}>
                              <FormControl>
                                <SelectTrigger>
                                  <SelectValue placeholder="Selecciona..." />
                                </SelectTrigger>
                              </FormControl>
                              <SelectContent>
                                {organizationTypes.map(type => <SelectItem key={type} value={type}>{type}</SelectItem>)}
                              </SelectContent>
                            </Select>
                            <FormMessage />
                          </FormItem>} />
                      
                      <FormField control={form.control} name="servicio" render={({
                      field
                    }) => <FormItem>
                            <FormLabel>Servicio de interés *</FormLabel>
                            <Select onValueChange={field.onChange} defaultValue={field.value}>
                              <FormControl>
                                <SelectTrigger>
                                  <SelectValue placeholder="Selecciona..." />
                                </SelectTrigger>
                              </FormControl>
                              <SelectContent>
                                {services.map(service => <SelectItem key={service.id} value={service.name}>{service.name}</SelectItem>)}
                              </SelectContent>
                            </Select>
                            <FormMessage />
                          </FormItem>} />
                    </div>
                    
                    <FormField control={form.control} name="comentarios" render={({
                    field
                  }) => <FormItem>
                          <FormLabel>Comentarios adicionales</FormLabel>
                          <FormControl>
                            <Textarea placeholder="Cuéntanos sobre tu organización, número de asistentes, fechas preferidas, necesidades específicas..." className="min-h-[120px]" {...field} />
                          </FormControl>
                          <FormMessage />
                        </FormItem>} />
                    
                    <Button type="submit" size="lg" className="w-full bg-gradient-to-r from-amber-500 to-orange-500 hover:from-amber-600 hover:to-orange-600 text-white text-lg" disabled={isSubmitting}>
                      {isSubmitting ? <>Enviando...</> : <>
                          <Send className="mr-2 h-5 w-5" />
                          Enviar Solicitud de Propuesta
                        </>}
                    </Button>
                    
                    <p className="text-xs text-center text-muted-foreground">
                      Al enviar este formulario, aceptas nuestra política de privacidad. 
                      Nos pondremos en contacto contigo en menos de 24 horas laborables.
                    </p>
                  </form>
                </Form>
              </CardContent>
            </Card>
          </div>
        </div>
      </section>

      {/* CTA Final */}
      <section className="py-20 bg-gradient-to-br from-slate-900 via-slate-800 to-slate-900 relative overflow-hidden">
        <div className="absolute inset-0 bg-[url('data:image/svg+xml,...')] opacity-5" />
        <div className="absolute top-0 left-0 w-96 h-96 bg-amber-500/10 rounded-full blur-3xl" />
        <div className="absolute bottom-0 right-0 w-96 h-96 bg-orange-500/10 rounded-full blur-3xl" />
        
        <div className="container relative">
          <div className="max-w-3xl mx-auto text-center">
            <Badge className="mb-6 bg-amber-500/20 text-amber-400 border-amber-500/30">
              <Sparkles className="h-3 w-3 mr-1" />
              Da el Primer Paso
            </Badge>
            <h2 className="text-3xl md:text-4xl lg:text-5xl font-bold mb-6 text-white">
              La IA No Espera.{' '}
              <span className="bg-gradient-to-r from-amber-400 to-orange-400 bg-clip-text text-transparent">
                ¿Y Tú?
              </span>
            </h2>
            <p className="text-xl text-slate-300 mb-8">
              Solicita tu propuesta personalizada hoy y lleva la revolución de la IA directamente a tu cocina, restaurante u otro negocio de hostelería
            </p>
            <div className="flex flex-col sm:flex-row gap-4 justify-center">
              <Button size="lg" onClick={scrollToForm} className="text-lg px-8 bg-gradient-to-r from-amber-500 to-orange-500 hover:from-amber-600 hover:to-orange-600 text-white">
                <Send className="mr-2 h-5 w-5" />
                Solicitar Propuesta Ahora
              </Button>
              <Button size="lg" variant="outline" className="text-lg px-8 border-amber-500/50 text-amber-400 hover:bg-amber-500/10" onClick={() => window.location.href = 'mailto:info@aichef.pro'}>
                <MapPin className="mr-2 h-5 w-5" />
                info@aichef.pro
              </Button>
            </div>
          </div>
        </div>
      </section>

      <ModernFooter />
    </div>;
};
export default FormacionPresencial;