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
    image: 'https://assets.zyrosite.com/cdn-cgi/image/format=auto,w=328,h=222,fit=crop/AVLbeJ7l3JfrlNJr/ai-chef-pro---basic-apps-dWxb1bDVBVI55E7q.png',
    ctaText: 'Explorar Ingredientes',
    slug: 'sosa-ingredients'
  },
  {
    id: 'menu-plate-seo-featured',
    name: 'Menu Plate Local SEO',
    description: 'Optimiza cada plato para buscadores',
    testimonial: {
      text: 'Mis platos ahora aparecen en Google cuando la gente busca comida local. Las reservas han aumentado un 40%',
      author: 'Restaurante El Olivo',
      role: 'Propietario'
    },
    image: 'https://assets.zyrosite.com/cdn-cgi/image/format=auto,w=172,h=225,fit=crop/AVLbeJ7l3JfrlNJr/captura-de-pantalla-2024-08-29-a-las-11.58.02-AoPG8GrzGrFKWpoL.png',
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
    image: 'https://assets.zyrosite.com/cdn-cgi/image/format=auto,w=328,h=227,fit=crop/AVLbeJ7l3JfrlNJr/chef-diego-schattenhofer-aichef-ALpokN25zMuQ7oWJ.jpg',
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