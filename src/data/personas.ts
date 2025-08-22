import { allApps } from './apps';

export type PersonaType = 'chef-ejecutivo' | 'panaderia' | 'food-truck' | 'estudiante' | 'restaurante' | 'reposteria';

export interface Persona {
  id: PersonaType;
  name: string;
  description: string;
  emoji: string;
  recommendedApps: string[]; // App IDs
}

export const personas: Persona[] = [
  {
    id: 'chef-ejecutivo',
    name: 'Soy Chef Ejecutivo',
    description: 'Lidero equipos y diseño menús estratégicos',
    emoji: '👨‍🍳',
    recommendedApps: ['mental-coach', 'gastro-lexicum', 'catering-ai', 'menu-plate-seo']
  },
  {
    id: 'panaderia',
    name: 'Tengo una Panadería',
    description: 'Especialista en panes y productos horneados',
    emoji: '🥖',
    recommendedApps: ['panaderia-creativa', 'mermas-gencal', 'calcula-pax', 'instaflow-ai']
  },
  {
    id: 'food-truck',
    name: 'Dirijo un Food Truck',
    description: 'Cocina móvil con menús optimizados',
    emoji: '🚚',
    recommendedApps: ['food-truck-ai', 'cocina-creativa', 'id-alergenos', 'gastro-calendar']
  },
  {
    id: 'estudiante',
    name: 'Soy Estudiante de Gastronomía',
    description: 'Aprendiendo técnicas y expandiendo conocimiento',
    emoji: '🎓',
    recommendedApps: ['gastro-lexicum', 'cocina-creativa', 'mental-coach', 'conversor-ing']
  },
  {
    id: 'restaurante',
    name: 'Tengo un Restaurante',
    description: 'Gestiono un establecimiento gastronómico',
    emoji: '🏪',
    recommendedApps: ['casual-restaurants-ai', 'food-pairing', 'mermas-gencal', 'menu-plate-seo']
  },
  {
    id: 'reposteria',
    name: 'Me especializo en Repostería',
    description: 'Maestro en postres y dulces de autor',
    emoji: '🧁',
    recommendedApps: ['pasteleria-creativa', 'chocolateria-creativa', 'heladeria-creativa', 'pinterai-content']
  }
];

export const getRecommendedApps = (personaId: PersonaType) => {
  const persona = personas.find(p => p.id === personaId);
  if (!persona) return [];
  
  return persona.recommendedApps
    .map(appId => allApps.find(app => app.id === appId))
    .filter(Boolean);
};