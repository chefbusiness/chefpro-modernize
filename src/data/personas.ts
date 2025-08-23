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
    name: 'chef-ejecutivo',
    description: 'chef-ejecutivo',
    emoji: '👨‍🍳',
    recommendedApps: ['mental-coach', 'gastro-lexicum', 'catering-ai', 'menu-plate-seo']
  },
  {
    id: 'panaderia',
    name: 'panaderia',
    description: 'panaderia',
    emoji: '🥖',
    recommendedApps: ['panaderia-creativa', 'mermas-gencal', 'calcula-pax', 'instaflow-ai']
  },
  {
    id: 'food-truck',
    name: 'food-truck',
    description: 'food-truck',
    emoji: '🚚',
    recommendedApps: ['food-truck-ai', 'cocina-creativa', 'id-alergenos', 'gastro-calendar']
  },
  {
    id: 'estudiante',
    name: 'estudiante',
    description: 'estudiante',
    emoji: '🎓',
    recommendedApps: ['gastro-lexicum', 'cocina-creativa', 'mental-coach', 'conversor-ing']
  },
  {
    id: 'restaurante',
    name: 'restaurante',
    description: 'restaurante',
    emoji: '🏪',
    recommendedApps: ['casual-restaurants-ai', 'food-pairing', 'mermas-gencal', 'menu-plate-seo']
  },
  {
    id: 'reposteria',
    name: 'reposteria',
    description: 'reposteria',
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