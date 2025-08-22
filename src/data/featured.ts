export interface FeaturedApp {
  id: string;
  name: string;
  description: string;
  testimonial: {
    text: string;
    author: string;
    role: string;
  };
  image: string;
  ctaText: string;
  slug: string;
}

export const featuredApps: FeaturedApp[] = [
  {
    id: 'sosa-ingredients',
    name: 'Sosa Ingredients Agent',
    description: 'Trabaja con ingredientes de vanguardia',
    testimonial: {
      text: 'Me ayuda a seleccionar los mejores productos Sosa para mis creaciones de alta cocina',
      author: 'Chef M. García',
      role: 'Chef Ejecutivo, Restaurante Michelin'
    },
    image: '/lovable-uploads/69dc47f9-78f7-4d07-9be2-86a312f39d0d.png',
    ctaText: 'Explorar Ingredientes',
    slug: 'sosa-ingredients'
  },
  {
    id: 'menu-plate-seo-featured',
    name: 'MenuDish Local SEO',
    description: 'Optimiza cada plato para buscadores',
    testimonial: {
      text: 'Mis platos ahora aparecen en Google cuando la gente busca comida local. Las reservas han aumentado un 40%',
      author: 'Restaurante El Olivo',
      role: 'Propietario'
    },
    image: '/lovable-uploads/f48cf594-86e2-4b91-8c3e-a84ee90031ff.png',
    ctaText: 'Optimizar Mi Menú',
    slug: 'menu-plate-seo'
  },
  {
    id: 'fermentus-featured',
    name: 'Fermentus Con AI+',
    description: 'Fermentación y conservas de autor',
    testimonial: {
      text: 'Revolucionó mi comprensión de la fermentación. Ahora creo sabores únicos que mis clientes adoran',
      author: 'Chef Ana Rodrigo',
      role: 'Especialista en Fermentación'
    },
    image: '/lovable-uploads/63181b9a-0605-4608-b9ce-f331d980d4b6.png',
    ctaText: 'Dominar Fermentación',
    slug: 'fermentus'
  },
  {
    id: 'mental-coach-featured',
    name: 'Mental Coach',
    description: 'Bienestar y liderazgo en la cocina',
    testimonial: {
      text: 'Mi equipo está más motivado y el ambiente en la cocina es completamente diferente. Menos estrés, más creatividad',
      author: 'Chef Roberto Silva',
      role: 'Chef Ejecutivo'
    },
    image: 'https://assets.zyrosite.com/cdn-cgi/image/format=auto,w=328,h=222,fit=crop/AVLbeJ7l3JfrlNJr/ai-chef-pro---basic-apps-dWxb1bDVBVI55E7q.png',
    ctaText: 'Mejorar Liderazgo',
    slug: 'mental-coach'
  }
];