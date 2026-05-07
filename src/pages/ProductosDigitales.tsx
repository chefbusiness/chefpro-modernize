import { useEffect, useState } from 'react';
import { Helmet } from 'react-helmet-async';
import SaasDiscoveryBanner from '@/components/shared/SaasDiscoveryBanner';
import LogoBadge from '@/components/shared/LogoBadge';
import WhatsAppProductSupport from '@/components/shared/WhatsAppProductSupport';
import {
  ArrowRight, BookOpen, FileSpreadsheet, Star, Check, Clock,
  ShieldCheck, BarChart3, Utensils, GraduationCap, Users, Truck, Package, TrendingUp,
  ChefHat, Coffee, Building, Filter, Globe, ChevronDown, ClipboardList, Pizza, Beef, Warehouse, Croissant, Wine, Tent, IceCream, CakeSlice, UtensilsCrossed, Fish, Shell, Beer,
} from 'lucide-react';

// ── Tag definitions ──────────────────────────────────────────
const ALL_TAGS = [
  { id: 'all', label: 'Todos', icon: Filter },
  // Formato
  { id: 'excel', label: 'Excel' },
  { id: 'pdf', label: 'PDF / eBook' },
  { id: 'plantillas', label: 'Plantillas' },
  { id: 'guias', label: 'Guías How-To' },
  { id: 'manuales', label: 'Manuales' },
  // Temática
  { id: 'costes', label: 'Control de Costes' },
  { id: 'seguridad', label: 'Seguridad Alimentaria' },
  { id: 'ia', label: 'Inteligencia Artificial' },
  { id: 'gestion', label: 'Gestión' },
  // Concepto de negocio
  { id: 'restaurante', label: 'Restaurante' },
  { id: 'cafeteria', label: 'Cafetería' },
  { id: 'pizzeria', label: 'Pizzería' },
  { id: 'hamburgueseria', label: 'Hamburguesería' },
  { id: 'dark-kitchen', label: 'Dark Kitchen' },
  { id: 'pasteleria', label: 'Pastelería' },
  { id: 'bar', label: 'Bar / Cocktails' },
  { id: 'catering', label: 'Catering' },
  { id: 'hotel', label: 'Hotel' },
  { id: 'heladeria', label: 'Heladería' },
  { id: 'chocolateria', label: 'Chocolatería' },
  { id: 'chef-privado', label: 'Chef Privado' },
];

// ── Live products ────────────────────────────────────────────
const products = [
  {
    name: 'Mega Pack Tareas Recurrentes — 13 Kits',
    slug: '/mega-pack-tareas',
    price: '€89',
    originalPrice: '€180',
    discount: '-50%',
    description: 'Los 13 kits de tareas recurrentes en un solo pack: restaurante, cafetería, pizzería, bar, hotel, catering, heladería, chocolatería y más. 151 plantillas Excel.',
    features: [
      '13 kits completos de tareas recurrentes',
      '151 plantillas Excel editables',
      'Apertura/cierre negocio + caja incluidos',
      'Ahorra más del 45% vs compra individual',
    ],
    icon: Package,
    image: '/lovable-uploads/ai-gallery/tareas-gestion-personal-hero.jpg',
    badge: '🎁 Mega Pack',
    badgeColor: 'bg-emerald-500 text-white ring-1 ring-emerald-300/50',
    tags: ['excel', 'plantillas', 'bundle', 'restaurante', 'cafeteria', 'pizzeria', 'hamburgueseria', 'dark-kitchen', 'pasteleria', 'bar', 'catering', 'hotel', 'heladeria', 'chocolateria', 'chef-privado'],
    featured: true,
  },
  {
    name: 'Kit de Escandallos Pro',
    slug: '/kit-escandallos',
    price: '€12',
    originalPrice: '€49',
    discount: '-75%',
    description: '11 plantillas Excel con fórmulas automáticas, mermas precargadas y calculadora de PVP. Controla tu food cost.',
    features: [
      '11 plantillas Excel profesionales',
      'Mermas estándar precargadas',
      'Calculadora PVP para 9 establecimientos',
      'Dashboard Food Cost mensual',
    ],
    icon: FileSpreadsheet,
    image: '/kit-escandallos-hero.jpg',
    badge: '🔥 Más Vendido',
    badgeColor: 'bg-orange-500 text-white ring-1 ring-orange-300/50',
    tags: ['excel', 'plantillas', 'costes', 'restaurante', 'cafeteria', 'pizzeria', 'hamburgueseria', 'dark-kitchen', 'pasteleria', 'bar', 'catering', 'hotel', 'heladeria', 'chocolateria'],
  },
  {
    name: 'Pack Plantillas APPCC',
    slug: '/pack-appcc',
    price: '€14',
    originalPrice: '€29',
    discount: '-52%',
    description: '17 plantillas de seguridad alimentaria: temperaturas, limpieza, alérgenos, HACCP, trazabilidad. Obligatorio por ley.',
    features: [
      '17 plantillas con alertas automáticas',
      'Matriz de los 14 alérgenos obligatorios',
      'Análisis de Peligros HACCP pre-rellenado',
      'Guía de inspección de Sanidad',
    ],
    icon: ShieldCheck,
    image: '/lovable-uploads/ai-gallery/appcc-inspector-sanidad.jpeg',
    badge: '🔥 Más Vendido',
    badgeColor: 'bg-orange-500 text-white ring-1 ring-orange-300/50',
    tags: ['excel', 'plantillas', 'seguridad', 'restaurante', 'cafeteria', 'pizzeria', 'hamburgueseria', 'dark-kitchen', 'pasteleria', 'bar', 'catering', 'hotel', 'heladeria', 'chocolateria'],
  },
  {
    name: 'Kit Control de Inventario y Compras',
    slug: '/kit-inventario',
    price: '€14',
    originalPrice: '€49',
    discount: '-71%',
    description: '9 plantillas Excel con formulas automaticas: inventario diario, fichas proveedores, pedidos de compra, recepcion mercancias, control mermas, FIFO, analisis costes y 2 bonus.',
    features: [
      'Par levels con alertas de reposicion',
      'Comparativa precios entre proveedores',
      'Control mermas con dashboard',
      'FIFO y caducidades con semaforo',
    ],
    icon: Package,
    image: '/lovable-uploads/ai-gallery/inventario-hero.jpg',
    badge: '🔥 Más Vendido',
    badgeColor: 'bg-orange-500 text-white ring-1 ring-orange-300/50',
    tags: ['excel', 'plantillas', 'gestion', 'restaurante', 'cafeteria', 'pizzeria', 'hamburgueseria', 'dark-kitchen', 'pasteleria', 'bar', 'catering', 'hotel', 'heladeria', 'chocolateria'],
  },
  {
    name: 'Cómo Montar un Restaurante Gastronómico',
    slug: '/guia-restaurante-gastronomico',
    price: '€85',
    originalPrice: '€220',
    discount: '-61%',
    description: 'Guía premium 80+ páginas: 22 capítulos, plan financiero, diseño cocina y sala, brigada, bodega, Michelin, Sol Repsol. 10 plantillas Excel + 8 checklists + business plan + manual de sala.',
    features: [
      'PDF + DOCX: 22 capítulos, 80+ páginas',
      '10 plantillas Excel con fórmulas',
      '8 checklists de apertura completos',
      'Business plan modelo para bancos',
    ],
    icon: Star,
    image: '/lovable-uploads/ai-gallery/guia-dk-cocina.jpg',
    badge: 'Premium',
    badgeColor: 'bg-amber-500/20 text-amber-400',
    tags: ['pdf', 'guias', 'restaurante'],
  },
  {
    name: 'Cómo Montar un Restaurante Casual',
    slug: '/guia-restaurante-casual',
    price: '€65',
    originalPrice: '€180',
    discount: '-64%',
    description: 'Guía premium 60+ páginas: 20 capítulos, plan financiero, diseño cocina y sala, delivery, terraza, menú del día. 9 plantillas Excel + 6 checklists + business plan + manual de operaciones.',
    features: [
      'PDF + DOCX: 20 capítulos, 60+ páginas',
      '9 plantillas Excel con fórmulas',
      '6 checklists de apertura completos',
      'Business plan modelo para bancos',
    ],
    icon: UtensilsCrossed,
    image: '/lovable-uploads/ai-gallery/guia-casual-hero.jpg',
    badge: 'Nuevo',
    badgeColor: 'bg-green-500/20 text-green-400',
    tags: ['pdf', 'guias', 'restaurante'],
  },
  {
    name: 'Cómo Montar un Restaurante Mexicano',
    slug: '/guia-restaurante-mexicano',
    price: '€65',
    originalPrice: '€180',
    discount: '-64%',
    description: 'Guía premium 60+ páginas: 20 capítulos, proveedores mexicanos en España, barra de tequilas y mezcales, escandallos de 15 recetas. 9 plantillas Excel + 6 checklists + business plan + manual de operaciones.',
    features: [
      'PDF + DOCX: 20 capítulos, 60+ páginas',
      '9 plantillas Excel con fórmulas',
      '6 checklists de apertura completos',
      'Escandallos de 15 recetas mexicanas',
    ],
    icon: Utensils,
    image: '/lovable-uploads/ai-gallery/guia-mexicano-hero.jpg',
    badge: 'Nuevo',
    badgeColor: 'bg-green-500/20 text-green-400',
    tags: ['pdf', 'guias', 'restaurante'],
  },
  {
    name: 'Cómo Montar un Restaurante Peruano',
    slug: '/guia-restaurante-peruano',
    price: '€65',
    originalPrice: '€180',
    discount: '-64%',
    description: 'Guía premium 60+ páginas: 20 capítulos, cevichería, cocina Nikkei, barra de piscos, proveedores peruanos en España. 9 plantillas Excel + 6 checklists + business plan + manual de operaciones.',
    features: [
      'PDF + DOCX: 20 capítulos, 60+ páginas',
      '9 plantillas Excel con fórmulas',
      '6 checklists de apertura completos',
      'Escandallos de 15 recetas peruanas',
    ],
    icon: Utensils,
    image: '/lovable-uploads/ai-gallery/guia-peruano-hero.jpg',
    badge: 'Nuevo',
    badgeColor: 'bg-green-500/20 text-green-400',
    tags: ['pdf', 'guias', 'restaurante'],
  },
  {
    name: 'Cómo Montar un Restaurante Japonés',
    slug: '/guia-restaurante-japones',
    price: '€65',
    originalPrice: '€180',
    discount: '-64%',
    description: 'Guía premium 60+ páginas: 20 capítulos, sushi-ya, ramen-ya, izakaya, omakase, robatayaki. Pescado sashimi-grade, normativa anisakis, barra de sake y whisky japonés. 9 plantillas Excel + 6 checklists + business plan + manual de operaciones.',
    features: [
      'PDF + DOCX: 20 capítulos, 60+ páginas',
      '9 plantillas Excel con fórmulas',
      '6 checklists (incluye APPCC anisakis)',
      'Escandallos de 15 recetas japonesas',
    ],
    icon: Utensils,
    image: '/lovable-uploads/ai-gallery/guia-restaurante-japones-hero.jpg',
    badge: 'Nuevo',
    badgeColor: 'bg-green-500/20 text-green-400',
    tags: ['pdf', 'guias', 'restaurante'],
  },
  {
    name: 'Cómo Montar un Restaurante Nikkei',
    slug: '/guia-restaurante-nikkei',
    price: '€65',
    originalPrice: '€180',
    discount: '-64%',
    description: 'Guía premium 60+ páginas: fusión peruano-japonesa. Tiraditos, ceviches nikkei, causas, makis acevichados, anticuchos, chaufa, omakase nikkei. Barra de pisco + sake. Proveedores de ají peruano y pescado sashimi-grade. 9 plantillas Excel + 6 checklists + business plan + manual de operaciones.',
    features: [
      'PDF + DOCX: 20 capítulos, 60+ páginas',
      '9 plantillas Excel con fórmulas',
      '6 checklists (APPCC anisakis + leche de tigre)',
      'Escandallos de 15 recetas nikkei',
    ],
    icon: Utensils,
    image: '/lovable-uploads/ai-gallery/guia-restaurante-nikkei-hero.jpg',
    badge: 'Nuevo',
    badgeColor: 'bg-green-500/20 text-green-400',
    tags: ['pdf', 'guias', 'restaurante'],
  },
  {
    name: 'Cómo Montar una Dark Kitchen',
    slug: '/guia-dark-kitchen',
    price: '€24',
    originalPrice: '€90',
    discount: '-73%',
    description: 'Guía completa PDF + DOCX editable: 12 capítulos, requisitos legales, plan financiero, diseño de cocina, tecnología, marketing. 3 checklists Excel + calculadora de viabilidad.',
    features: [
      'PDF editorial + DOCX editable',
      '12 capítulos de la idea al lanzamiento',
      '3 checklists Excel + calculadora',
      'Requisitos legales España 2026',
    ],
    icon: Building,
    image: '/lovable-uploads/ai-gallery/guia-dk-hero.jpg',
    badge: 'Nuevo',
    badgeColor: 'bg-purple-500/20 text-purple-400',
    tags: ['pdf', 'guias', 'dark-kitchen'],
  },
  {
    name: 'Gastro Pro Prompts eBook',
    slug: '/pro-prompts-ebook',
    price: '€9',
    originalPrice: '€50',
    discount: '-90%',
    description: '300+ prompts de IA específicos para hostelería: cocina creativa, pastelería, catering, gestión, marketing y más.',
    features: [
      'eBook PDF + Dashboard exclusivo',
      '300+ prompts organizados por categoría',
      'Compatible con ChatGPT, Claude, Gemini',
      'Actualizaciones de por vida',
    ],
    icon: BookOpen,
    image: '/ebook-mockup-bundle.webp',
    badge: 'Bestseller',
    badgeColor: 'bg-[#FFD700]/20 text-[#FFD700]',
    tags: ['pdf', 'ia'],
  },
  {
    name: 'Kit Gestion de Personal y Turnos',
    slug: '/kit-gestion-personal',
    price: '€14',
    originalPrice: '€49',
    discount: '-71%',
    description: '9 plantillas Excel con formulas automaticas: cuadrante turnos, horas extra, coste laboral, onboarding, vacaciones, evaluacion de desempeno y directorio de plantilla.',
    features: [
      'Cuadrante turnos con alertas legales',
      'Control horas extra automatico',
      'Ratio coste laboral con semaforo',
      'Onboarding, vacaciones y evaluacion',
    ],
    icon: Users,
    image: '/lovable-uploads/ai-gallery/tareas-gestion-personal-hero.jpg',
    badge: 'Nuevo',
    badgeColor: 'bg-purple-500/20 text-purple-400',
    tags: ['excel', 'plantillas', 'gestion', 'restaurante', 'cafeteria', 'pizzeria', 'hamburgueseria', 'dark-kitchen', 'pasteleria', 'bar', 'catering', 'hotel', 'heladeria', 'chocolateria'],
  },
  {
    name: 'Kit Plan Financiero para Restaurantes',
    slug: '/kit-plan-financiero',
    price: '€39',
    originalPrice: '€190',
    discount: '-79%',
    description: '10 plantillas Excel con fórmulas encadenadas: plan financiero a 3 y 5 años, punto de equilibrio, cash flow, CAPEX, P&L mensual, ratios financieros e informe de viabilidad para bancos.',
    features: [
      'Plan previsional a 3 y 5 años',
      'Break-even con 3 escenarios',
      'Cash flow con alertas de liquidez',
      'Informe viabilidad listo para bancos',
    ],
    icon: TrendingUp,
    image: '/lovable-uploads/ai-gallery/plan-financiero-hero.jpg',
    badge: 'Nuevo',
    badgeColor: 'bg-purple-500/20 text-purple-400',
    tags: ['excel', 'plantillas', 'costes', 'restaurante', 'cafeteria', 'pizzeria', 'hamburgueseria', 'dark-kitchen', 'pasteleria', 'bar', 'catering', 'hotel', 'heladeria', 'chocolateria'],
  },
  {
    name: 'Tareas Recurrentes: Restaurante Casual',
    slug: '/kit-tareas',
    price: '€14',
    originalPrice: '€49',
    discount: '-71%',
    description: '9 checklists operativos pre-rellenados: apertura, cierre, partidas, manager, perfiles, eventos. Imprime, delega y firma.',
    features: [
      'Apertura y cierre por área',
      'Tareas por perfil profesional',
      'Checklist diario/semanal del manager',
      'Eventos y festivos incluidos',
    ],
    icon: ClipboardList,
    image: '/lovable-uploads/ai-gallery/tareas-restaurante-hero.jpg',
    badge: 'Nuevo',
    badgeColor: 'bg-purple-500/20 text-purple-400',
    tags: ['excel', 'plantillas', 'gestion', 'restaurante'],
  },
  {
    name: 'Tareas Recurrentes: Cafetería / Brunch',
    slug: '/kit-tareas-cafeteria',
    price: '€12',
    originalPrice: '€39',
    discount: '-69%',
    description: '463 tareas + inventarios con fórmulas: apertura/cierre, barista, vitrina pastelería, brunch, terraza. Imprime, delega y firma.',
    features: [
      'Inventario diario de barra con alertas',
      'Tareas específicas de barista',
      'Control de vitrina y pastelería',
      'Brunch dominical y eventos',
    ],
    icon: Coffee,
    image: '/lovable-uploads/ai-gallery/tareas-cafeteria-hero.jpg',
    badge: 'Nuevo',
    badgeColor: 'bg-purple-500/20 text-purple-400',
    tags: ['excel', 'plantillas', 'gestion', 'cafeteria'],
  },
  {
    name: 'Tareas Recurrentes: Pizzería',
    slug: '/kit-tareas-pizzeria',
    price: '€12',
    originalPrice: '€39',
    discount: '-69%',
    description: '330 tareas + inventario: horno de leña/piedra, masa napolitana, línea de montaje, delivery. Imprime, delega y firma.',
    features: [
      'Control de horno y temperatura',
      'Línea de montaje pizza',
      'Gestión de delivery y packaging',
      'Masa: fermentación y estirado',
    ],
    icon: Pizza,
    image: '/lovable-uploads/ai-gallery/tareas-pizzeria-hero.jpg',
    badge: 'Nuevo',
    badgeColor: 'bg-purple-500/20 text-purple-400',
    tags: ['excel', 'plantillas', 'gestion', 'pizzeria'],
  },
  {
    name: 'Tareas Recurrentes: Hamburguesería',
    slug: '/kit-tareas-hamburgueseria',
    price: '€12',
    originalPrice: '€39',
    discount: '-69%',
    description: '302 tareas pre-rellenadas: plancha/grill, smash burgers, freidora, línea de montaje, delivery y packaging. Imprime, delega y firma.',
    features: [
      'Control de plancha y punto de carne',
      'Smash burger y técnica de grill',
      'Freidora: test polares, filtrado, temperatura',
      'Delivery y packaging burger',
    ],
    icon: Beef,
    image: '/lovable-uploads/ai-gallery/tareas-burger-hero.jpg',
    badge: 'Nuevo',
    badgeColor: 'bg-purple-500/20 text-purple-400',
    tags: ['excel', 'plantillas', 'gestion', 'hamburgueseria'],
  },
  {
    name: 'Tareas Recurrentes: Dark Kitchen',
    slug: '/kit-tareas-dark-kitchen',
    price: '€12',
    originalPrice: '€39',
    discount: '-69%',
    description: '293 tareas pre-rellenadas: estaciones produccion multi-marca, empaquetado, plataformas (Glovo, Uber Eats, Just Eat), riders y expedicion. Imprime, delega y firma.',
    features: [
      'Multi-marca / ghost kitchen',
      'Gestion de tablets y plataformas',
      'Packaging diferenciado por marca',
      'Coordinacion de riders y expedicion',
    ],
    icon: Warehouse,
    image: '/lovable-uploads/ai-gallery/tareas-dk-hero.jpg',
    badge: 'Nuevo',
    badgeColor: 'bg-purple-500/20 text-purple-400',
    tags: ['excel', 'plantillas', 'gestion', 'dark-kitchen'],
  },
  {
    name: 'Tareas Recurrentes: Pastelería / Obrador',
    slug: '/kit-tareas-pasteleria',
    price: '€12',
    originalPrice: '€39',
    discount: '-69%',
    description: '9 checklists operativos pre-rellenados para pastelería y obrador: producción de masas, fermentación, cremas, decoración, vitrina, perfiles y eventos. Imprime, delega y firma.',
    features: [
      'Producción artesanal completa',
      'Masas, fermentación, cremas, decoración',
      'Eventos: Navidad, Reyes, San Valentín',
      'Perfiles: jefe pastelero, oficial, ayudante',
    ],
    icon: Croissant,
    image: '/lovable-uploads/ai-gallery/tareas-pasteleria-hero.jpg',
    badge: 'Nuevo',
    badgeColor: 'bg-purple-500/20 text-purple-400',
    tags: ['excel', 'plantillas', 'gestion', 'pasteleria'],
  },
  {
    name: 'Tareas Recurrentes: Bar / Cocktails',
    slug: '/kit-tareas-bar',
    price: '€12',
    originalPrice: '€39',
    discount: '-69%',
    description: '9 checklists operativos pre-rellenados para bar y cocktail bar: coctelería, barra, cerveza de grifo, vinos por copa, terraza, inventario y eventos. Imprime, delega y firma.',
    features: [
      'Coctelería clásica y contemporánea',
      'Cerveza de grifo, vinos, café',
      'Eventos: Nochevieja, Halloween, catas',
      'Perfiles: head bartender, barback',
    ],
    icon: Wine,
    image: '/lovable-uploads/ai-gallery/tareas-bar-hero.jpg',
    badge: 'Nuevo',
    badgeColor: 'bg-purple-500/20 text-purple-400',
    tags: ['excel', 'plantillas', 'gestion', 'bar'],
  },
  {
    name: 'Tareas Recurrentes: Catering / Eventos',
    slug: '/kit-tareas-catering',
    price: '€12',
    originalPrice: '€39',
    discount: '-69%',
    description: '9 checklists operativos pre-rellenados para empresas de catering: producción off-site, transporte, montaje, servicio, desmontaje y post-evento. Bodas, corporativos, cocktails.',
    features: [
      'Producción off-site y empaquetado',
      'Transporte y cadena de frío',
      'Bodas, corporativos, cocktails, outdoor',
      'Perfiles: chef evento, maître, camarero',
    ],
    icon: Tent,
    image: '/lovable-uploads/ai-gallery/tareas-catering-hero.jpg',
    badge: 'Nuevo',
    badgeColor: 'bg-purple-500/20 text-purple-400',
    tags: ['excel', 'plantillas', 'gestion', 'catering'],
  },
  {
    name: 'Tareas Recurrentes: Hotel Completo',
    slug: '/kit-tareas-hotel',
    price: '€18,50',
    originalPrice: '€95',
    discount: '-81%',
    description: '46 checklists operativos en 15 plantillas para 11 departamentos: F&B, recepción, housekeeping, piscina, terraza, mantenimiento, administración y spa.',
    features: [
      'F&B: 6 outlets completos',
      'Recepción, housekeeping, spa',
      'Piscina, terraza, mantenimiento',
      'Administración y revenue',
    ],
    icon: Building,
    image: '/lovable-uploads/ai-gallery/tareas-hotel-hero.jpg',
    badge: 'Nuevo',
    badgeColor: 'bg-purple-500/20 text-purple-400',
    tags: ['excel', 'plantillas', 'gestion', 'hotel'],
  },
  {
    name: 'Tareas Recurrentes: Heladería Artesanal',
    slug: '/kit-tareas-heladeria',
    price: '€12',
    originalPrice: '€39',
    discount: '-69%',
    description: '9 checklists operativos pre-rellenados para heladería artesanal: producción (pasteurización, mantecación), servicio, gestión y temporada.',
    features: [
      'Producción: pasteurización y mantecación',
      'Vitrina, toppings y servicio mostrador',
      'Perfiles: heladero, dependiente, encargado',
      'Temporada alta/baja + catering eventos',
    ],
    icon: IceCream,
    image: '/lovable-uploads/ai-gallery/tareas-heladeria-hero.jpg',
    badge: 'Nuevo',
    badgeColor: 'bg-purple-500/20 text-purple-400',
    tags: ['excel', 'plantillas', 'gestion', 'heladeria'],
  },
  {
    name: 'Tareas Recurrentes: Chocolatería / Obrador',
    slug: '/kit-tareas-chocolateria',
    price: '€12',
    originalPrice: '€39',
    discount: '-69%',
    description: '9 checklists operativos pre-rellenados para chocolatería artesanal: producción (templado, moldeado, bombones), vitrina, servicio, gestión y temporada.',
    features: [
      'Producción: templado, moldeado y bombones',
      'Vitrina, packaging y servicio mostrador',
      'Perfiles: chocolatero, dependiente, encargado',
      'Temporada: Navidad, San Valentín, Pascua',
    ],
    icon: CakeSlice,
    image: '/lovable-uploads/ai-gallery/tareas-chocolateria-hero.jpg',
    badge: 'Nuevo',
    badgeColor: 'bg-purple-500/20 text-purple-400',
    tags: ['excel', 'plantillas', 'gestion', 'chocolateria'],
  },
  {
    name: 'Tareas Recurrentes: Restaurante Creativo / De Autor',
    slug: '/kit-tareas-restaurante-creativo',
    price: '€12',
    originalPrice: '€39',
    discount: '-69%',
    description: '11 checklists operativos pre-rellenados para restaurante creativo y de autor: I+D, menu degustacion, brigada creativa, sumiller, eventos, fotografia y storytelling.',
    features: [
      'I+D: fichas tecnicas, pruebas, costes',
      'Mise en place degustacion y timing de pases',
      'Sumiller: bodega, maridajes, catas',
      'Chef\'s table, showcookings, prensa',
    ],
    icon: ChefHat,
    image: '/lovable-uploads/ai-gallery/tareas-restaurante-creativo-hero.jpg',
    badge: 'Nuevo',
    badgeColor: 'bg-purple-500/20 text-purple-400',
    tags: ['excel', 'plantillas', 'gestion', 'restaurante'],
  },
  {
    name: 'Tareas Recurrentes: Chef Privado / Personal Chef',
    slug: '/kit-tareas-chef-privado',
    price: '€18',
    originalPrice: '€85',
    discount: '-79%',
    description: '9 checklists profesionales para chef privado: ficha de cliente con alergias, equipo y transporte, APPCC móvil, servicio completo, fidelización y administración del autónomo.',
    features: [
      'Ficha de cliente: alergias, preferencias, cocina',
      'Equipo portátil, transporte frío, vehículo',
      'APPCC móvil: temperaturas y alérgenos',
      'Servicio: pre, durante y post + limpieza',
    ],
    icon: UtensilsCrossed,
    image: '/lovable-uploads/ai-gallery/tareas-chef-privado-hero.jpg',
    badge: 'Nuevo',
    badgeColor: 'bg-purple-500/20 text-purple-400',
    tags: ['excel', 'plantillas', 'gestion', 'chef-privado'],
  },
  {
    name: 'Tareas Recurrentes: Sushi Bar',
    slug: '/kit-tareas-sushi-bar',
    price: '€14',
    originalPrice: '€69',
    discount: '-80%',
    description: '11 checklists operativos para sushi bar con protocolo anisakis APPCC obligatorio (RD 1420/2006), control de pH del arroz, vitrina neta case, perfiles itamae y omakase.',
    features: [
      'Anisakis APPCC: -20 ºC / 7 días por lote',
      'Arroz sushi con control de pH (≤4.6)',
      'Vitrina neta case (2-4 ºC) + rotación FIFO',
      'Perfiles itamae, ayudante, sala, delivery',
    ],
    icon: Fish,
    image: '/lovable-uploads/ai-gallery/tareas-sushi-bar-hero.jpg',
    badge: 'Nuevo',
    badgeColor: 'bg-purple-500/20 text-purple-400',
    tags: ['excel', 'plantillas', 'gestion', 'sushi-bar', 'japones'],
  },
  {
    name: 'Tareas Recurrentes: Asador / Parrilla y Josper',
    slug: '/kit-tareas-asador',
    price: '€14',
    originalPrice: '€69',
    discount: '-80%',
    description: '11 checklists operativos para asador con horno Josper: encendido y mantenimiento de brasas, maduración dry-age y despiece, temperaturas por corte, pescados y verduras a la brasa.',
    features: [
      'Protocolo Josper: encendido, zonas de calor, carbón',
      'Maduración dry-age con fichas por pieza',
      'Temperaturas internas por corte y punto de cocción',
      'Perfiles parrillero, ayudante, cocina, sala',
    ],
    icon: Beef,
    image: '/lovable-uploads/ai-gallery/tareas-asador-hero.jpg',
    badge: 'Nuevo',
    badgeColor: 'bg-purple-500/20 text-purple-400',
    tags: ['excel', 'plantillas', 'gestion', 'asador', 'parrilla', 'josper'],
  },
  {
    name: 'Tareas Recurrentes: Marisquería con Vivero y APPCC',
    slug: '/kit-tareas-marisqueria',
    price: '€14',
    originalPrice: '€69',
    discount: '-80%',
    description: '11 checklists operativos para marisquería: control del vivero (oxígeno, salinidad, temperatura), expositor de hielo, trazabilidad APPCC y alérgenos de crustáceos y moluscos, lonjas y temporadas de pesca de España.',
    features: [
      'Vivero: oxígeno, salinidad, temperatura, mortalidad',
      'Trazabilidad APPCC y alérgenos UE 1379/2013',
      'Expositor de hielo y rotación FIFO',
      'Temporadas de pesca y vedas oficiales España',
    ],
    icon: Shell,
    image: '/lovable-uploads/ai-gallery/tareas-marisqueria-hero.jpg',
    badge: 'Nuevo',
    badgeColor: 'bg-purple-500/20 text-purple-400',
    tags: ['excel', 'plantillas', 'gestion', 'marisqueria', 'pescado', 'marisco'],
  },
  {
    name: 'Tareas Recurrentes: Tapas Bar / Gastrobar',
    slug: '/kit-tareas-tapas-bar',
    price: '€14',
    originalPrice: '€69',
    discount: '-80%',
    description: '11 checklists operativos para tapas bar y gastrobar: barra de pinchos y tapas frías, cocina de raciones (plancha, freidora, guisos), cerveza grifo, vinos por copa, vermut, terraza y rotación de carta estacional.',
    features: [
      'Barra de pinchos y tapas frías con rotación',
      'Cocina de raciones: plancha, freidora, guisos',
      'Cerveza grifo, vinos por copa y vermut',
      'Terraza, eventos y carta estacional',
    ],
    icon: Beer,
    image: '/lovable-uploads/ai-gallery/tareas-bar-hero.jpg',
    badge: 'Nuevo',
    badgeColor: 'bg-purple-500/20 text-purple-400',
    tags: ['excel', 'plantillas', 'gestion', 'tapas', 'gastrobar', 'bar'],
  },
];

// ── Coming soon products ────────────────────────────────────
const comingSoon = [
  { icon: Utensils, name: 'Cómo Montar una Panadería/Obrador', desc: 'Guía completa con presupuesto, planos tipo, trámites por CCAA, equipamiento y proveedores.', tags: ['pdf', 'guias', 'pasteleria'], phase: 'Mayo 2026' },
  { icon: Utensils, name: 'Cómo Montar una Pastelería', desc: 'Guía paso a paso: obrador, vitrina, maquinaria, proveedores, licencias y lanzamiento.', tags: ['pdf', 'guias', 'pasteleria'], phase: 'Mayo 2026' },
  { icon: Utensils, name: 'Cómo Montar una Chocolatería', desc: 'Temperado, obrador, vitrina, proveedores de cacao, licencias y modelo de negocio.', tags: ['pdf', 'guias', 'chocolateria'], phase: 'Junio 2026' },
  { icon: ChefHat, name: 'Manual del Chef Ejecutivo', desc: 'Responsabilidades, KPIs, protocolos, checklists y evaluación de equipo de cocina.', tags: ['pdf', 'manuales', 'gestion', 'restaurante'], phase: 'Junio 2026' },
  { icon: Coffee, name: 'Manual del Manager de Restaurante', desc: 'Guía completa del gerente: operaciones, personas, finanzas, servicio y liderazgo.', tags: ['pdf', 'manuales', 'gestion', 'restaurante'], phase: 'Julio 2026' },
  { icon: GraduationCap, name: 'Guía Food Cost + Ingeniería de Menú', desc: 'Metodología completa + matriz BCG + 30 ejemplos + pricing psychology + plantillas.', tags: ['pdf', 'costes', 'restaurante'], phase: 'Julio 2026' },
];

const PRODUCTS_PER_PAGE = 12;

export default function ProductosDigitales() {
  const [activeTag, setActiveTag] = useState('all');
  const [visibleCount, setVisibleCount] = useState(PRODUCTS_PER_PAGE);

  const filteredProducts = activeTag === 'all'
    ? products
    : products.filter((p) => p.tags.includes(activeTag));

  const filteredComingSoon = activeTag === 'all'
    ? comingSoon
    : comingSoon.filter((p) => p.tags.includes(activeTag));

  useEffect(() => {
    setVisibleCount(PRODUCTS_PER_PAGE);
  }, [activeTag]);

  const visibleProducts = filteredProducts.slice(0, visibleCount);
  const hasMoreProducts = visibleCount < filteredProducts.length;

  return (
    <>
      <Helmet>
        <title>Productos Digitales para Hostelería — Plantillas, Guías, Prompts IA | AI Chef Pro</title>
        <meta name="description" content="eBooks, plantillas Excel, prompts de IA, guías APPCC y herramientas digitales para chefs, gerentes y dueños de restaurante. Recursos profesionales desde €9." />
        <meta name="robots" content="index, follow" />
        <meta name="keywords" content="productos digitales hostelería, prompts IA restaurante, plantilla escandallo excel, plantillas APPCC restaurante, ebook hostelería, herramientas digitales restaurante, food cost excel, seguridad alimentaria hostelería, AI Chef Pro" />
        <link rel="canonical" href="https://aichef.pro/productos-digitales" />

        {/* Open Graph */}
        <meta property="og:title" content="Productos Digitales para Hostelería — AI Chef Pro" />
        <meta property="og:description" content="Plantillas Excel, guías profesionales y prompts de IA para profesionales de hostelería. Desde €9." />
        <meta property="og:url" content="https://aichef.pro/productos-digitales" />
        <meta property="og:type" content="website" />
        <meta property="og:site_name" content="AI Chef Pro" />
        <meta property="og:locale" content="es_ES" />
        <meta property="og:image" content="https://aichef.pro/og-productos-digitales.jpg" />
        <meta property="og:image:width" content="1200" />
        <meta property="og:image:height" content="630" />

        {/* Twitter Card */}
        <meta name="twitter:card" content="summary_large_image" />
        <meta name="twitter:title" content="Productos Digitales para Hostelería — AI Chef Pro" />
        <meta name="twitter:description" content="Plantillas Excel, guías y prompts de IA para profesionales de hostelería." />
        <meta name="twitter:image" content="https://aichef.pro/og-productos-digitales.jpg" />

        {/* CollectionPage Schema */}
        <script type="application/ld+json">{JSON.stringify({
          "@context": "https://schema.org",
          "@type": "CollectionPage",
          "name": "Productos Digitales para Hostelería — AI Chef Pro",
          "description": "Plantillas Excel, guías APPCC, prompts de IA y herramientas digitales para chefs, gerentes y dueños de restaurante.",
          "url": "https://aichef.pro/productos-digitales",
          "publisher": {
            "@type": "Organization",
            "name": "AI Chef Pro",
            "url": "https://aichef.pro"
          },
          "mainEntity": {
            "@type": "ItemList",
            "itemListElement": [
              { "@type": "ListItem", "position": 1, "url": "https://aichef.pro/mega-pack-tareas", "name": "Mega Pack Tareas Recurrentes — 13 Kits" },
              { "@type": "ListItem", "position": 2, "url": "https://aichef.pro/kit-escandallos", "name": "Kit de Escandallos Pro" },
              { "@type": "ListItem", "position": 3, "url": "https://aichef.pro/pack-appcc", "name": "Pack Plantillas APPCC" },
              { "@type": "ListItem", "position": 4, "url": "https://aichef.pro/kit-inventario", "name": "Kit Control de Inventario y Compras" },
              { "@type": "ListItem", "position": 5, "url": "https://aichef.pro/guia-restaurante-gastronomico", "name": "Cómo Montar un Restaurante Gastronómico" },
              { "@type": "ListItem", "position": 6, "url": "https://aichef.pro/pro-prompts-ebook", "name": "Gastro Pro Prompts eBook" },
              { "@type": "ListItem", "position": 7, "url": "https://aichef.pro/kit-plan-financiero", "name": "Kit Plan Financiero para Restaurantes" },
              { "@type": "ListItem", "position": 8, "url": "https://aichef.pro/kit-gestion-personal", "name": "Kit Gestión de Personal y Turnos" },
              { "@type": "ListItem", "position": 9, "url": "https://aichef.pro/kit-tareas", "name": "Tareas Recurrentes: Restaurante Casual" },
              { "@type": "ListItem", "position": 10, "url": "https://aichef.pro/kit-tareas-hotel", "name": "Tareas Recurrentes: Hotel Completo" }
            ]
          }
        })}</script>

        {/* FAQPage Schema */}
        <script type="application/ld+json">{JSON.stringify({
          "@context": "https://schema.org",
          "@type": "FAQPage",
          "mainEntity": [
            { "@type": "Question", "name": "?Qu? formato tienen los productos digitales?", "acceptedAnswer": { "@type": "Answer", "text": "La mayor?a son plantillas en formato Excel (.xlsx) compatibles con Microsoft Excel, Google Sheets, LibreOffice y Apple Numbers. Tambi?n incluimos gu?as y fichas en formato PDF." }},
            { "@type": "Question", "name": "?C?mo recibo los productos despu?s de comprar?", "acceptedAnswer": { "@type": "Answer", "text": "El acceso es inmediato. Tras el pago con Stripe, te redirigimos a tu dashboard privado donde puedes descargar todos los archivos." }},
            { "@type": "Question", "name": "?Puedo comprar desde fuera de Espa?a?", "acceptedAnswer": { "@type": "Answer", "text": "S?. Puedes comprar desde cualquier parte del mundo con tarjeta, Apple Pay o Google Pay. Los productos est?n en espa?ol." }},
            { "@type": "Question", "name": "?Hay garant?a de devoluci?n?", "acceptedAnswer": { "@type": "Answer", "text": "30 d?as de garant?a completa en todos los productos. Si no est?s satisfecho, te devolvemos el 100% sin preguntas." }},
            { "@type": "Question", "name": "?Las plantillas incluyen f?rmulas autom?ticas?", "acceptedAnswer": { "@type": "Answer", "text": "S?. Todas las plantillas Excel vienen con f?rmulas precargadas que calculan autom?ticamente food cost, PVP sugerido, alertas de temperatura y control de mermas." }},
            { "@type": "Question", "name": "?Incluyen actualizaciones futuras?", "acceptedAnswer": { "@type": "Answer", "text": "S?. Todos los productos incluyen acceso de por vida al dashboard online con actualizaciones sin coste adicional." }},
            { "@type": "Question", "name": "?Puedo usar las plantillas en varios restaurantes?", "acceptedAnswer": { "@type": "Answer", "text": "S?. La licencia es personal ? puedes usar las plantillas en todos los establecimientos que gestiones." }},
            { "@type": "Question", "name": "?Qu? m?todos de pago aceptan?", "acceptedAnswer": { "@type": "Answer", "text": "Procesamos pagos con Stripe. Aceptamos tarjeta de cr?dito/d?bito (Visa, Mastercard, Amex), Apple Pay, Google Pay y Link." }}
          ]
        })}</script>

        {/* BreadcrumbList Schema */}
        <script type="application/ld+json">{JSON.stringify({
          "@context": "https://schema.org",
          "@type": "BreadcrumbList",
          "itemListElement": [
            { "@type": "ListItem", "position": 1, "name": "AI Chef Pro", "item": "https://aichef.pro" },
            { "@type": "ListItem", "position": 2, "name": "Productos Digitales", "item": "https://aichef.pro/productos-digitales" }
          ]
        })}</script>
      </Helmet>

      <div className="min-h-screen bg-[#0a0a0a]">
        <SaasDiscoveryBanner />
        {/* Hero */}
        <section className="relative px-4 pt-6 pb-12 md:pt-8 md:pb-16 overflow-hidden">
          <div className="absolute inset-0" style={{
            background: 'radial-gradient(ellipse 80% 60% at 50% -10%, rgba(255,215,0,0.08) 0%, transparent 70%)',
          }} />

          <div className="relative max-w-4xl mx-auto text-center z-10">
            <LogoBadge />
            <span className="inline-block mt-4 mb-6 px-4 py-1.5 rounded-full bg-[#FFD700]/10 border border-[#FFD700]/30 text-[#FFD700] text-sm font-medium">
              {products.length} productos disponibles · {comingSoon.length} próximamente
            </span>

            <h1 className="text-3xl md:text-5xl lg:text-6xl font-extrabold text-white leading-tight mb-6">
              Tienda de Productos <span className="text-[#FFD700]">Digitales</span> para la Hostelería de Hoy
            </h1>

            <p className="text-lg md:text-xl text-gray-300 max-w-3xl mx-auto leading-relaxed">
              eBooks, plantillas Excel, guías de seguridad alimentaria y prompts de IA diseñados por y para profesionales de la hostelería. Descarga inmediata, acceso de por vida.
            </p>
          </div>
        </section>

        {/* Tag Filter */}
        <section className="px-4 pb-8">
          <div className="max-w-6xl mx-auto">
            <div className="flex flex-wrap justify-center gap-2">
              {ALL_TAGS.map((tag) => {
                const isActive = activeTag === tag.id;
                return (
                  <button
                    key={tag.id}
                    onClick={() => setActiveTag(tag.id)}
                    className={`px-4 py-2 rounded-full text-sm font-medium transition-all duration-200 ${
                      isActive
                        ? 'bg-[#FFD700] text-black'
                        : 'bg-white/5 text-gray-400 border border-white/10 hover:border-[#FFD700]/30 hover:text-white'
                    }`}
                  >
                    {tag.icon && <tag.icon className="w-3.5 h-3.5 inline mr-1.5 -mt-0.5" />}
                    {tag.label}
                  </button>
                );
              })}
            </div>
          </div>
        </section>

        {/* Products Grid — 3 columns */}
        {filteredProducts.length > 0 && (
          <section className="px-4 pb-16 md:pb-24">
            <div className="max-w-6xl mx-auto grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
              {visibleProducts.map((product) => {
                const Icon = product.icon;
                return (
                  <a
                    key={product.slug}
                    href={product.slug}
                    className={`group relative bg-white/[0.03] rounded-2xl overflow-hidden hover:bg-white/[0.05] transition-all duration-300 flex flex-col ${(product as any).featured ? 'border-2 border-emerald-500/50 hover:border-emerald-400/70 ring-1 ring-emerald-500/20' : 'border border-white/10 hover:border-[#FFD700]/30'}`}
                  >
                    {/* Badge */}
                    <div className="absolute top-3 right-3 z-10">
                      <span className={`px-3 py-1 rounded-full text-xs font-bold shadow-lg shadow-black/40 backdrop-blur-sm ${product.badgeColor}`}>
                        {product.badge}
                      </span>
                    </div>

                    {/* Image */}
                    <div className="relative h-40 overflow-hidden bg-gradient-to-b from-white/[0.05] to-transparent">
                      <img
                        src={product.image}
                        alt={product.name}
                        className="w-full h-full object-cover opacity-80 group-hover:opacity-100 group-hover:scale-105 transition-all duration-500"
                        loading="lazy"
                      />
                      <div className="absolute inset-0 bg-gradient-to-t from-[#0a0a0a] via-transparent to-transparent" />
                    </div>

                    {/* Content */}
                    <div className="p-5 flex flex-col flex-1">
                      <div className="flex items-center gap-2.5 mb-2">
                        <div className="w-9 h-9 rounded-xl bg-[#FFD700]/10 flex items-center justify-center flex-shrink-0">
                          <Icon className="w-4.5 h-4.5 text-[#FFD700]" />
                        </div>
                        <h2 className="text-lg md:text-base lg:text-lg font-bold text-white group-hover:text-[#FFD700] transition-colors leading-tight">
                          {product.name}
                        </h2>
                      </div>

                      <p className="text-gray-400 text-sm leading-relaxed mb-4">
                        {product.description}
                      </p>

                      {/* Features */}
                      <ul className="space-y-1.5 mb-5 flex-1">
                        {product.features.map((feature) => (
                          <li key={feature} className="flex items-start gap-2 text-xs text-gray-300">
                            <Check className="w-3.5 h-3.5 text-[#FFD700] flex-shrink-0 mt-0.5" />
                            <span>{feature}</span>
                          </li>
                        ))}
                      </ul>

                      {/* Tags */}
                      <div className="flex flex-wrap gap-1.5 mb-4">
                        {product.tags.map((tagId) => {
                          const tag = ALL_TAGS.find((t) => t.id === tagId);
                          return tag ? (
                            <span key={tagId} className="px-2 py-0.5 rounded-full bg-white/5 text-gray-500 text-[10px] font-medium">
                              {tag.label}
                            </span>
                          ) : null;
                        })}
                      </div>

                      {/* Price + CTA */}
                      <div className="flex items-center justify-between mt-auto pt-4 border-t border-white/5">
                        <div className="flex items-center gap-2">
                          <span className="text-2xl font-extrabold text-[#FFD700]">{product.price}</span>
                          <span className="text-sm text-gray-500 line-through">{product.originalPrice}</span>
                          <span className="px-2 py-0.5 rounded-full bg-[#FFD700]/20 text-[#FFD700] text-[10px] font-bold">
                            {product.discount}
                          </span>
                        </div>
                        <div className="flex items-center gap-1 text-[#FFD700] text-xs font-medium group-hover:gap-2 transition-all">
                          Ver
                          <ArrowRight className="w-3.5 h-3.5" />
                        </div>
                      </div>
                    </div>
                  </a>
                );
              })}
            </div>

            {/* Cargar más */}
            {hasMoreProducts && (
              <div className="max-w-6xl mx-auto mt-10 flex flex-col items-center gap-3">
                <button
                  onClick={() => setVisibleCount((c) => c + PRODUCTS_PER_PAGE)}
                  className="px-8 py-3 rounded-full bg-[#FFD700]/10 border border-[#FFD700]/30 text-[#FFD700] text-sm font-semibold hover:bg-[#FFD700]/20 hover:border-[#FFD700]/60 transition-all duration-200"
                >
                  Cargar más productos ({filteredProducts.length - visibleCount} restantes)
                </button>
                <p className="text-xs text-gray-500">
                  Mostrando {visibleProducts.length} de {filteredProducts.length}
                </p>
              </div>
            )}
          </section>
        )}

        {/* Coming Soon */}
        {filteredComingSoon.length > 0 && (
          <section className="px-4 pb-16 md:pb-24">
            <div className="max-w-6xl mx-auto">
              <div className="text-center mb-8">
                <span className="inline-block mb-4 px-4 py-1.5 rounded-full bg-white/5 border border-white/10 text-gray-400 text-sm font-medium">
                  <Clock className="w-4 h-4 inline mr-2" />
                  En Desarrollo
                </span>
                <h2 className="text-2xl md:text-3xl font-bold text-white mb-2">
                  Próximos <span className="text-[#FFD700]">Productos</span>
                </h2>
                <p className="text-gray-500 text-sm max-w-2xl mx-auto">
                  Mismo estándar de calidad: acceso inmediato, actualizaciones de por vida y garantía de 30 días.
                </p>
              </div>

              <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-4">
                {filteredComingSoon.map((item) => {
                  const Icon = item.icon;
                  return (
                    <div
                      key={item.name}
                      className="bg-white/[0.02] border border-white/[0.06] rounded-xl p-4 opacity-70 hover:opacity-90 transition-opacity"
                    >
                      <div className="flex items-start gap-3 mb-3">
                        <div className="w-8 h-8 rounded-lg bg-white/5 flex items-center justify-center flex-shrink-0">
                          <Icon className="w-4 h-4 text-gray-400" />
                        </div>
                        <div className="flex-1 min-w-0">
                          <h3 className="text-sm font-semibold text-white leading-tight mb-1">{item.name}</h3>
                          <p className="text-[11px] text-gray-500 leading-relaxed">{item.desc}</p>
                        </div>
                      </div>
                      <div className="flex items-center justify-between">
                        <div className="flex flex-wrap gap-1">
                          {item.tags.slice(0, 2).map((tagId) => {
                            const tag = ALL_TAGS.find((t) => t.id === tagId);
                            return tag ? (
                              <span key={tagId} className="px-1.5 py-0.5 rounded-full bg-white/5 text-gray-600 text-[9px] font-medium">
                                {tag.label}
                              </span>
                            ) : null;
                          })}
                        </div>
                        <span className="text-[10px] px-2 py-0.5 rounded-full bg-white/5 text-gray-500 font-medium">
                          {item.phase}
                        </span>
                      </div>
                    </div>
                  );
                })}
              </div>
            </div>
          </section>
        )}

        {/* No results */}
        {filteredProducts.length === 0 && filteredComingSoon.length === 0 && (
          <section className="px-4 pb-16 md:pb-24">
            <div className="max-w-3xl mx-auto text-center py-12">
              <p className="text-gray-400 text-lg mb-4">No hay productos en esta categoría todavía.</p>
              <button
                onClick={() => setActiveTag('all')}
                className="px-6 py-2 rounded-full bg-[#FFD700]/10 text-[#FFD700] text-sm font-medium hover:bg-[#FFD700]/20 transition-colors"
              >
                Ver todos los productos
              </button>
            </div>
          </section>
        )}

        {/* Trust section */}
        <section className="px-4 pb-16 md:pb-24">
          <div className="max-w-3xl mx-auto text-center">
            <div className="flex items-center justify-center gap-1 mb-3">
              {Array.from({ length: 5 }).map((_, i) => (
                <Star key={i} className="h-5 w-5 fill-[#FFD700] text-[#FFD700]" />
              ))}
            </div>
            <p className="text-gray-400 text-sm mb-6">
              Valoración media de 4.9/5 por profesionales de hostelería
            </p>
            <div className="flex flex-wrap items-center justify-center gap-6 text-sm text-gray-500">
              <span className="flex items-center gap-2">
                <Check className="w-4 h-4 text-[#FFD700]" />
                Garantía 30 días
              </span>
              <span className="flex items-center gap-2">
                <Check className="w-4 h-4 text-[#FFD700]" />
                Acceso inmediato
              </span>
              <span className="flex items-center gap-2">
                <Check className="w-4 h-4 text-[#FFD700]" />
                Actualizaciones gratis
              </span>
              <span className="flex items-center gap-2">
                <Check className="w-4 h-4 text-[#FFD700]" />
                Pago seguro con Stripe
              </span>
            </div>
          </div>
        </section>

        {/* Worldwide availability */}
        <section className="px-4 pb-16 md:pb-24">
          <div className="max-w-4xl mx-auto">
            <div className="bg-white/[0.03] border border-white/10 rounded-2xl p-8 md:p-10 text-center">
              <div className="w-16 h-16 rounded-full bg-[#FFD700]/10 flex items-center justify-center mx-auto mb-5">
                <Globe className="w-8 h-8 text-[#FFD700]" />
              </div>
              <h2 className="text-xl md:text-2xl font-bold text-white mb-3">
                Compra desde <span className="text-[#FFD700]">Cualquier Parte del Mundo</span>
              </h2>
              <p className="text-gray-400 text-sm md:text-base leading-relaxed max-w-2xl mx-auto mb-6">
                Nuestros productos digitales están diseñados para el mercado de hostelería en español.
                Acceso inmediato tras la compra — sin importar dónde estés.
              </p>
              <div className="flex flex-wrap justify-center gap-3 text-sm text-gray-500">
                {['Espa\u00f1a', 'M\u00e9xico', 'Colombia', 'Argentina', 'Chile', 'Per\u00fa', 'Ecuador', 'EE.UU.', 'Alemania', 'Francia'].map((country) => (
                  <span key={country} className="px-3 py-1.5 rounded-full bg-white/5 border border-white/[0.06]">
                    {country}
                  </span>
                ))}
                <span className="px-3 py-1.5 rounded-full bg-[#FFD700]/10 border border-[#FFD700]/20 text-[#FFD700] font-medium">
                  + todo el mundo
                </span>
              </div>
            </div>
          </div>
        </section>

        {/* FAQ Section */}
        <section className="px-4 pb-16 md:pb-24">
          <div className="max-w-3xl mx-auto">
            <h2 className="text-2xl md:text-3xl font-bold text-white text-center mb-10">
              Preguntas <span className="text-[#FFD700]">Frecuentes</span>
            </h2>
            <div className="space-y-3">
              {[
                { q: '\u00bfQu\u00e9 formato tienen los productos digitales?', a: 'La mayor\u00eda son plantillas en formato Excel (.xlsx) compatibles con Microsoft Excel, Google Sheets, LibreOffice y Apple Numbers. Tambi\u00e9n incluimos gu\u00edas y fichas en formato PDF listas para imprimir. Todos los archivos se descargan desde tu dashboard privado.' },
                { q: '\u00bfC\u00f3mo recibo los productos despu\u00e9s de comprar?', a: 'El acceso es inmediato. Tras el pago con Stripe, te redirigimos a tu dashboard privado donde puedes descargar todos los archivos. Adem\u00e1s, recibir\u00e1s un email con un enlace m\u00e1gico para acceder siempre que quieras.' },
                { q: '\u00bfPuedo comprar desde fuera de Espa\u00f1a?', a: 'S\u00ed. Los productos est\u00e1n en espa\u00f1ol y dise\u00f1ados pensando en normativa espa\u00f1ola y europea, pero el contenido es aplicable a cualquier pa\u00eds hispanohablante. Puedes comprar desde cualquier parte del mundo con tarjeta, Apple Pay o Google Pay.' },
                { q: '\u00bfLas plantillas incluyen f\u00f3rmulas autom\u00e1ticas?', a: 'S\u00ed. Todas las plantillas Excel vienen con f\u00f3rmulas precargadas que calculan autom\u00e1ticamente: food cost, PVP sugerido, alertas de temperatura, control de mermas. Solo introduces tus datos y el Excel hace el resto.' },
                { q: '\u00bfHay garant\u00eda de devoluci\u00f3n?', a: '30 d\u00edas de garant\u00eda completa en todos los productos. Si no est\u00e1s satisfecho, te devolvemos el 100% sin preguntas. Contacta a info@aichef.pro.' },
                { q: '\u00bfIncluyen actualizaciones futuras?', a: 'S\u00ed. Todos los productos incluyen acceso de por vida al dashboard online. Cuando a\u00f1adamos nuevas plantillas, mejoras o actualicemos por cambios normativos, las recibir\u00e1s sin coste adicional.' },
                { q: '\u00bfPuedo usar las plantillas en varios restaurantes?', a: 'S\u00ed. La licencia es personal — puedes usar las plantillas en todos los establecimientos que gestiones. Ideal para consultores, grupos de restauraci\u00f3n y gerentes multi-unidad.' },
                { q: '\u00bfQu\u00e9 m\u00e9todos de pago aceptan?', a: 'Procesamos pagos con Stripe, la plataforma de pagos m\u00e1s segura del mundo. Aceptamos tarjeta de cr\u00e9dito/d\u00e9bito (Visa, Mastercard, Amex), Apple Pay, Google Pay y Link (pago r\u00e1pido de Stripe).' },
              ].map((faq, i) => (
                <details key={i} className="group bg-white/[0.03] border border-white/10 rounded-xl overflow-hidden">
                  <summary className="flex items-center justify-between p-5 cursor-pointer list-none">
                    <span className="text-white font-medium pr-4 text-sm md:text-base">{faq.q}</span>
                    <ChevronDown className="w-5 h-5 text-[#FFD700] flex-shrink-0 transition-transform duration-300 group-open:rotate-180" />
                  </summary>
                  <p className="px-5 pb-5 text-gray-400 text-sm leading-relaxed">{faq.a}</p>
                </details>
              ))}
            </div>
          </div>
        </section>

        {/* pSEO Cities cross-link */}
        <section className="px-4 pb-16 md:pb-24 border-t border-white/5 pt-12">
          <div className="max-w-5xl mx-auto">
            <div className="text-center mb-8">
              <span className="inline-block px-4 py-1.5 rounded-full bg-[#FFD700]/10 border border-[#FFD700]/30 text-[#FFD700] text-xs font-medium mb-3">
                Recursos por ciudad
              </span>
              <h2 className="text-2xl md:text-3xl font-bold text-white mb-3">
                Lleva tu Plan a la <span className="text-[#FFD700]">Ciudad Donde Vas a Abrir</span>
              </h2>
              <p className="text-gray-400 max-w-2xl mx-auto">
                Combina nuestros kits y guías con datos verificados por ciudad: costes reales, licencias específicas, salarios sectoriales y los mejores barrios.
              </p>
            </div>
            <div className="flex flex-wrap justify-center gap-2 mb-6">
              {[
                { slug: 'madrid', label: 'Madrid' },
                { slug: 'barcelona', label: 'Barcelona' },
                { slug: 'valencia', label: 'Valencia' },
                { slug: 'ciudad-de-mexico', label: 'CDMX' },
                { slug: 'monterrey', label: 'Monterrey' },
                { slug: 'bogota', label: 'Bogotá' },
                { slug: 'medellin', label: 'Medellín' },
                { slug: 'buenos-aires', label: 'Buenos Aires' },
                { slug: 'santiago', label: 'Santiago' },
              ].map((c) => (
                <a
                  key={c.slug}
                  href={`/abrir-restaurante/${c.slug}`}
                  className="px-4 py-2 rounded-full bg-white/5 hover:bg-[#FFD700]/15 hover:text-[#FFD700] text-gray-300 text-sm font-medium transition-colors border border-white/10"
                >
                  Abrir restaurante en {c.label}
                </a>
              ))}
            </div>
            <div className="text-center">
              <a
                href="/seo-restaurantes-por-ciudad"
                className="inline-flex items-center gap-2 px-6 py-3 rounded-full bg-[#FFD700] text-black font-semibold hover:bg-[#FFD700]/90 transition-colors"
              >
                Ver las 15 ciudades + 5 recursos →
              </a>
            </div>
          </div>
        </section>

        {/* SEO content block */}
        <section className="px-4 pb-16 md:pb-24 border-t border-white/5 pt-12">
          <div className="max-w-3xl mx-auto">
            <h2 className="text-xl md:text-2xl font-bold text-white mb-4 text-center">
              Recursos Digitales Profesionales para <span className="text-[#FFD700]">Hostelería</span>
            </h2>
            <div className="text-gray-400 text-sm leading-relaxed space-y-4">
              <p>
                AI Chef Pro ofrece una colección de productos digitales diseñados específicamente para profesionales de hostelería y restauración. Desde prompts de inteligencia artificial optimizados para ChatGPT, Claude, Gemini y Perplexity, hasta plantillas de escandallos en Excel y registros de seguridad alimentaria APPCC obligatorios por ley.
              </p>
              <p>
                Cada producto ha sido creado por profesionales con más de 29 años de experiencia en alta hostelería y 15 años en consultoría gastronómica. No son recursos genéricos: son herramientas específicas para chefs ejecutivos, jefes de cocina, gerentes de restaurante, pasteleros, bartenders, directores de catering y dueños de establecimientos de hostelería.
              </p>
              <p>
                Todos nuestros productos incluyen acceso inmediato tras la compra, actualizaciones gratuitas de por vida, 8 herramientas profesionales gratuitas y garantía de devolución de 30 días. Pago seguro procesado por Stripe.
              </p>
            </div>
          </div>
        </section>

        {/* Footer */}
        <footer className="py-8 px-4 border-t border-white/10">
          <div className="max-w-4xl mx-auto text-center">
            <p className="text-gray-500 text-sm mb-2">
              © 2026 AI Chef Pro · Todos los derechos reservados
            </p>
            <div className="flex flex-wrap items-center justify-center gap-2 md:gap-4 text-sm">
              <a href="https://aichef.pro" className="text-gray-500 hover:text-[#FFD700] transition-colors">aichef.pro</a>
              <span className="text-gray-700 hidden md:inline">·</span>
              <a href="/pro-prompts-ebook" className="text-gray-500 hover:text-[#FFD700] transition-colors">Pro Prompts eBook</a>
              <span className="text-gray-700 hidden md:inline">·</span>
              <a href="/kit-escandallos" className="text-gray-500 hover:text-[#FFD700] transition-colors">Kit Escandallos</a>
              <span className="text-gray-700 hidden md:inline">·</span>
              <a href="/pack-appcc" className="text-gray-500 hover:text-[#FFD700] transition-colors">Pack APPCC</a>
              <span className="text-gray-700 hidden md:inline">·</span>
              <a href="mailto:info@aichef.pro" className="text-gray-500 hover:text-[#FFD700] transition-colors">Contacto</a>
            </div>
          </div>
        </footer>
        <WhatsAppProductSupport />
      </div>
    </>
  );
}
