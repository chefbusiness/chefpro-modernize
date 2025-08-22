import { 
  ChefHat, 
  Cookie, 
  Coffee, 
  IceCream, 
  Wheat, 
  Salad, 
  Leaf, 
  Link,
  Globe,
  MessageSquare,
  Calculator,
  AlertTriangle,
  Heart,
  Scale,
  Users,
  Truck,
  Building,
  Utensils,
  Camera,
  Calendar,
  Search,
  PinIcon
} from 'lucide-react';

export interface App {
  id: string;
  name: string;
  description: string;
  preview: string;
  icon: any;
  category: string;
  slug: string;
}

export const creativityApps: App[] = [
  {
    id: 'cocina-creativa',
    name: 'Cocina Creativa',
    description: 'Genera platos únicos con historia',
    preview: 'Tartar de remolacha asada con gel de cítricos y flores comestibles...',
    icon: ChefHat,
    category: 'creativity',
    slug: 'cocina-creativa'
  },
  {
    id: 'pasteleria-creativa',
    name: 'Pastelería Creativa',
    description: 'Postres de autor paso a paso',
    preview: 'Soufflé de chocolate con pralinés de vainilla y coulis de frambuesa...',
    icon: Cookie,
    category: 'creativity',
    slug: 'pasteleria-creativa'
  },
  {
    id: 'chocolateria-creativa',
    name: 'Chocolatería Creativa',
    description: 'Bombones y chocolate de vanguardia',
    preview: 'Ganache infusionado con té matcha y cristales de sal rosa...',
    icon: Coffee,
    category: 'creativity',
    slug: 'chocolateria-creativa'
  },
  {
    id: 'heladeria-creativa',
    name: 'Heladería Creativa',
    description: 'Helados artesanales profesionales',
    preview: 'Sorbete de gin-tonic con notas cítricas y hierbas aromáticas...',
    icon: IceCream,
    category: 'creativity',
    slug: 'heladeria-creativa'
  },
  {
    id: 'panaderia-creativa',
    name: 'Panadería Creativa',
    description: 'Panes únicos y fermentaciones',
    preview: 'Pan de masa madre con semillas tostadas y miel de azahar...',
    icon: Wheat,
    category: 'creativity',
    slug: 'panaderia-creativa'
  },
  {
    id: 'fermentus',
    name: 'Fermentus Con AI+',
    description: 'Fermentación y conservas de autor',
    preview: 'Kimchi de remolacha con jengibre y chili coreano fermentado...',
    icon: Salad,
    category: 'creativity',
    slug: 'fermentus'
  },
  {
    id: 'vegchef',
    name: 'VegChef Plant-Based',
    description: 'Cocina vegetal de alto nivel',
    preview: 'Ceviche de king oyster con leche de tigre de coco y ajíes...',
    icon: Leaf,
    category: 'creativity',
    slug: 'vegchef'
  },
  {
    id: 'food-pairing',
    name: 'Food Pairing AI',
    description: 'Descubre maridajes científicos',
    preview: 'Chocolate + hinojo por compuestos fenólicos compartidos...',
    icon: Link,
    category: 'creativity',
    slug: 'food-pairing'
  }
];

export const worldCookbooks = {
  europa: [
    { name: 'Alemana', flag: '🇩🇪', preview: 'Sauerbraten con spätzle caseros y col lombarda...' },
    { name: 'Belga', flag: '🇧🇪', preview: 'Carbonada flamenca con cerveza trapense y pan tostado...' },
    { name: 'Británica', flag: '🇬🇧', preview: 'Fish and chips con masa crujiente y salsa tártara...' },
    { name: 'Española', flag: '🇪🇸', preview: 'Paella valenciana tradicional con azafrán de La Mancha...' },
    { name: 'Francesa', flag: '🇫🇷', preview: 'Coq au vin de Borgoña con hierbas de Provenza...' },
    { name: 'Griega', flag: '🇬🇷', preview: 'Moussaka auténtica con berenjenas y salsa bechamel...' },
    { name: 'Portuguesa', flag: '🇵🇹', preview: 'Bacalhau à Brás con patatas paja y aceitunas negras...' },
    { name: 'Países Bajos', flag: '🇳🇱', preview: 'Stamppot de col rizada con salchicha ahumada...' },
    { name: 'Suiza', flag: '🇨🇭', preview: 'Fondue de quesos alpinos con pan artesanal...' },
    { name: 'Turca', flag: '🇹🇷', preview: 'Kebab de cordero con yogur de hierbas y pilaf...' }
  ],
  latinoamerica: [
    { name: 'Argentina', flag: '🇦🇷', preview: 'Asado criollo con chimichurri y provoleta...' },
    { name: 'Brasileña', flag: '🇧🇷', preview: 'Feijoada completa con farofa y caipirinha...' },
    { name: 'Chilena', flag: '🇨🇱', preview: 'Curanto en olla con mariscos y papas chilotas...' },
    { name: 'Colombiana', flag: '🇨🇴', preview: 'Bandeja paisa con frijoles, chicharrón y arepa...' },
    { name: 'Dominicana', flag: '🇩🇴', preview: 'Mangu con cebollitas y queso frito dominicano...' },
    { name: 'Ecuatoriana', flag: '🇪🇨', preview: 'Ceviche mixto con leche de tigre y cancha...' },
    { name: 'Jamaicana', flag: '🇯🇲', preview: 'Jerk chicken con rice and peas caribeño...' },
    { name: 'Mexicana', flag: '🇲🇽', preview: 'Mole poblano tradicional con chocolate y chiles...' },
    { name: 'Paraguaya', flag: '🇵🇾', preview: 'Sopa paraguaya con queso fresco y cebolla...' },
    { name: 'Peruana', flag: '🇵🇪', preview: 'Lomo saltado con papas doradas y ají amarillo...' },
    { name: 'Venezolana', flag: '🇻🇪', preview: 'Pabellón criollo con caraotas negras y tajadas...' }
  ],
  asia: [
    { name: 'China', flag: '🇨🇳', preview: 'Pato laqueado pekinés con panqueques de cebolleta...' },
    { name: 'India', flag: '🇮🇳', preview: 'Butter chicken con naan casero y arroz basmati...' },
    { name: 'Japonesa', flag: '🇯🇵', preview: 'Ramen tonkotsu con chashu y huevo marinado...' },
    { name: 'Tailandesa', flag: '🇹🇭', preview: 'Pad thai auténtico con tamarindo y cacahuetes...' }
  ]
};

export const businessTools: App[] = [
  {
    id: 'chatgpt-4o',
    name: 'ChatGPT 4.1',
    description: 'Asistente general IA más avanzado',
    preview: 'Ayuda con dudas técnicas y planning de menús estacionales',
    icon: MessageSquare,
    category: 'business',
    slug: 'chatgpt-4o'
  },
  {
    id: 'mermas-gencal',
    name: 'Mermas GenCal',
    description: 'Optimiza rendimientos y reduce desperdicios',
    preview: 'Ahorra hasta 30% en costes de ingredientes con cálculos precisos',
    icon: Calculator,
    category: 'business',
    slug: 'mermas-gencal'
  },
  {
    id: 'id-alergenos',
    name: 'ID Alérgenos',
    description: 'Identifica alérgenos automáticamente',
    preview: 'Cumple normativas de seguridad alimentaria sin errores',
    icon: AlertTriangle,
    category: 'business',
    slug: 'id-alergenos'
  },
  {
    id: 'mental-coach',
    name: 'Mental Coach',
    description: 'Bienestar y liderazgo en la cocina',
    preview: 'Reduce estrés y mejora ambiente laboral del equipo',
    icon: Heart,
    category: 'business',
    slug: 'mental-coach'
  },
  {
    id: 'conversor-ing',
    name: 'Conversor Ing',
    description: 'Convierte medidas y pesos al instante',
    preview: 'Adapta recetas entre sistemas métricos sin errores',
    icon: Scale,
    category: 'business',
    slug: 'conversor-ing'
  },
  {
    id: 'calcula-pax',
    name: 'Calcula Pax',
    description: 'Ajusta cantidades según comensales',
    preview: 'Escala recetas con precisión matemática para cualquier evento',
    icon: Users,
    category: 'business',
    slug: 'calcula-pax'
  }
];

export const businessConcepts: App[] = [
  {
    id: 'catering-ai',
    name: 'Catering AI+',
    description: 'Especialízate en catering profesional',
    preview: 'Menús para eventos con logística y costes optimizados',
    icon: Utensils,
    category: 'concepts',
    slug: 'catering-ai'
  },
  {
    id: 'burger-pro-ai',
    name: 'Burger Pro AI+',
    description: 'Perfecciona tu hamburguesería',
    preview: 'Recetas gourmet y técnicas de cocción para burgers premium',
    icon: ChefHat,
    category: 'concepts',
    slug: 'burger-pro-ai'
  },
  {
    id: 'food-truck-ai',
    name: 'Food Truck AI+',
    description: 'Optimiza tu food truck',
    preview: 'Menús móviles rentables con ingredientes versátiles',
    icon: Truck,
    category: 'concepts',
    slug: 'food-truck-ai'
  },
  {
    id: 'bar-lounge-ai',
    name: 'Bar & Lounge AI+',
    description: 'Cocktails y tapas de autor',
    preview: 'Combinaciones únicas de bebidas y maridajes perfectos',
    icon: Coffee,
    category: 'concepts',
    slug: 'bar-lounge-ai'
  },
  {
    id: 'casual-restaurants-ai',
    name: 'Casual Restaurants AI+',
    description: 'Gestión integral de restaurante',
    preview: 'Desde el menú hasta la experiencia del cliente',
    icon: Building,
    category: 'concepts',
    slug: 'casual-restaurants-ai'
  }
];

export const marketingTools: App[] = [
  {
    id: 'menu-plate-seo',
    name: 'Menu Plate Local SEO',
    description: 'Optimiza cada plato para buscadores',
    preview: 'Tus platos aparecen en Google cuando buscan comida local',
    icon: Search,
    category: 'marketing',
    slug: 'menu-plate-seo'
  },
  {
    id: 'gastro-calendar',
    name: 'Gastro Calendar',
    description: 'Planifica contenido gastronómico',
    preview: 'Calendario editorial con tendencias y fechas clave',
    icon: Calendar,
    category: 'marketing',
    slug: 'gastro-calendar'
  },
  {
    id: 'instaflow-ai',
    name: 'InstaFlow AI Pro',
    description: 'Contenido para Instagram automatizado',
    preview: 'Posts, stories y reels que enamoran a tu audiencia',
    icon: Camera,
    category: 'marketing',
    slug: 'instaflow-ai'
  },
  {
    id: 'pinterai-content',
    name: 'PinterAI Content Pro',
    description: 'Domina Pinterest gastronómico',
    preview: 'Pins virales con recetas que generan tráfico real',
    icon: PinIcon,
    category: 'marketing',
    slug: 'pinterai-content'
  }
];

export const gastroKnowledge: App[] = [
  {
    id: 'gastro-lexicum',
    name: 'Gastro Lexicum',
    description: 'Accede al saber culinario universal',
    preview: 'Enciclopedia gastronómica con técnicas y términos profesionales',
    icon: Globe,
    category: 'knowledge',
    slug: 'gastro-lexicum'
  }
];

export const allApps = [
  ...creativityApps,
  ...businessTools,
  ...businessConcepts,
  ...marketingTools,
  ...gastroKnowledge
];

export const appCategories = [
  {
    id: 'creativity',
    name: 'Creatividad Culinaria',
    description: 'Innova sin límites con IA',
    icon: ChefHat,
    count: creativityApps.length,
    apps: creativityApps
  },
  {
    id: 'worldCookbooks',
    name: 'Recetarios Mundiales',
    description: 'Domina la cocina global',
    icon: Globe,
    count: 25, // Europa (10) + Latinoamérica (11) + Asia (4)
    apps: []
  },
  {
    id: 'knowledge',
    name: 'Gastro Conocimiento',
    description: 'Accede al saber culinario',
    icon: Globe,
    count: gastroKnowledge.length,
    apps: gastroKnowledge
  },
  {
    id: 'business',
    name: 'Herramientas & Utilities',
    description: 'Optimiza tu operación diaria',
    icon: Calculator,
    count: businessTools.length,
    apps: businessTools
  },
  {
    id: 'concepts',
    name: 'Conceptos de Negocio',
    description: 'Especialízate en tu nicho',
    icon: Building,
    count: businessConcepts.length,
    apps: businessConcepts
  },
  {
    id: 'marketing',
    name: 'Marketing & Contenido',
    description: 'Potencia tu presencia digital',
    icon: Camera,
    count: marketingTools.length,
    apps: marketingTools
  }
];