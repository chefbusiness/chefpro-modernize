export interface NotificationCity {
  city: string;
  country: string;
  flag: string;
}

export interface NotificationPlan {
  name: string;
  price: string;
  currency: string;
}

export const notificationCities: Record<string, NotificationCity[]> = {
  es: [
    { city: "Madrid", country: "España", flag: "🇪🇸" },
    { city: "Barcelona", country: "España", flag: "🇪🇸" },
    { city: "Sevilla", country: "España", flag: "🇪🇸" },
    { city: "Valencia", country: "España", flag: "🇪🇸" },
    { city: "Bilbao", country: "España", flag: "🇪🇸" },
    { city: "Zaragoza", country: "España", flag: "🇪🇸" },
    { city: "Málaga", country: "España", flag: "🇪🇸" },
    { city: "Murcia", country: "España", flag: "🇪🇸" },
    { city: "Las Palmas", country: "España", flag: "🇪🇸" },
    { city: "Palma", country: "España", flag: "🇪🇸" },
    { city: "Bogotá", country: "Colombia", flag: "🇨🇴" },
    { city: "Medellín", country: "Colombia", flag: "🇨🇴" },
    { city: "Cartagena", country: "Colombia", flag: "🇨🇴" },
    { city: "Lima", country: "Perú", flag: "🇵🇪" },
    { city: "Arequipa", country: "Perú", flag: "🇵🇪" },
    { city: "Ciudad de México", country: "México", flag: "🇲🇽" },
    { city: "Guadalajara", country: "México", flag: "🇲🇽" },
    { city: "Monterrey", country: "México", flag: "🇲🇽" },
    { city: "Buenos Aires", country: "Argentina", flag: "🇦🇷" },
    { city: "Santiago", country: "Chile", flag: "🇨🇱" },
    { city: "Quito", country: "Ecuador", flag: "🇪🇨" },
    { city: "Caracas", country: "Venezuela", flag: "🇻🇪" }
  ],
  en: [
    { city: "New York", country: "USA", flag: "🇺🇸" },
    { city: "Los Angeles", country: "USA", flag: "🇺🇸" },
    { city: "Chicago", country: "USA", flag: "🇺🇸" },
    { city: "Miami", country: "USA", flag: "🇺🇸" },
    { city: "San Francisco", country: "USA", flag: "🇺🇸" },
    { city: "London", country: "UK", flag: "🇬🇧" },
    { city: "Manchester", country: "UK", flag: "🇬🇧" },
    { city: "Birmingham", country: "UK", flag: "🇬🇧" },
    { city: "Toronto", country: "Canada", flag: "🇨🇦" },
    { city: "Vancouver", country: "Canada", flag: "🇨🇦" },
    { city: "Sydney", country: "Australia", flag: "🇦🇺" },
    { city: "Melbourne", country: "Australia", flag: "🇦🇺" },
    { city: "Dublin", country: "Ireland", flag: "🇮🇪" }
  ],
  fr: [
    { city: "Paris", country: "France", flag: "🇫🇷" },
    { city: "Lyon", country: "France", flag: "🇫🇷" },
    { city: "Marseille", country: "France", flag: "🇫🇷" },
    { city: "Toulouse", country: "France", flag: "🇫🇷" },
    { city: "Nice", country: "France", flag: "🇫🇷" },
    { city: "Strasbourg", country: "France", flag: "🇫🇷" },
    { city: "Bordeaux", country: "France", flag: "🇫🇷" },
    { city: "Montréal", country: "Canada", flag: "🇨🇦" },
    { city: "Québec", country: "Canada", flag: "🇨🇦" },
    { city: "Bruxelles", country: "Belgique", flag: "🇧🇪" },
    { city: "Genève", country: "Suisse", flag: "🇨🇭" }
  ],
  de: [
    { city: "Berlin", country: "Deutschland", flag: "🇩🇪" },
    { city: "München", country: "Deutschland", flag: "🇩🇪" },
    { city: "Hamburg", country: "Deutschland", flag: "🇩🇪" },
    { city: "Köln", country: "Deutschland", flag: "🇩🇪" },
    { city: "Frankfurt", country: "Deutschland", flag: "🇩🇪" },
    { city: "Stuttgart", country: "Deutschland", flag: "🇩🇪" },
    { city: "Düsseldorf", country: "Deutschland", flag: "🇩🇪" },
    { city: "Wien", country: "Österreich", flag: "🇦🇹" },
    { city: "Salzburg", country: "Österreich", flag: "🇦🇹" },
    { city: "Zürich", country: "Schweiz", flag: "🇨🇭" }
  ],
  it: [
    { city: "Roma", country: "Italia", flag: "🇮🇹" },
    { city: "Milano", country: "Italia", flag: "🇮🇹" },
    { city: "Napoli", country: "Italia", flag: "🇮🇹" },
    { city: "Torino", country: "Italia", flag: "🇮🇹" },
    { city: "Firenze", country: "Italia", flag: "🇮🇹" },
    { city: "Bologna", country: "Italia", flag: "🇮🇹" },
    { city: "Venezia", country: "Italia", flag: "🇮🇹" },
    { city: "Palermo", country: "Italia", flag: "🇮🇹" }
  ],
  pt: [
    { city: "Lisboa", country: "Portugal", flag: "🇵🇹" },
    { city: "Porto", country: "Portugal", flag: "🇵🇹" },
    { city: "Coimbra", country: "Portugal", flag: "🇵🇹" },
    { city: "São Paulo", country: "Brasil", flag: "🇧🇷" },
    { city: "Rio de Janeiro", country: "Brasil", flag: "🇧🇷" },
    { city: "Brasília", country: "Brasil", flag: "🇧🇷" },
    { city: "Salvador", country: "Brasil", flag: "🇧🇷" },
    { city: "Recife", country: "Brasil", flag: "🇧🇷" }
  ],
  nl: [
    { city: "Amsterdam", country: "Nederland", flag: "🇳🇱" },
    { city: "Rotterdam", country: "Nederland", flag: "🇳🇱" },
    { city: "Den Haag", country: "Nederland", flag: "🇳🇱" },
    { city: "Utrecht", country: "Nederland", flag: "🇳🇱" },
    { city: "Eindhoven", country: "Nederland", flag: "🇳🇱" },
    { city: "Groningen", country: "Nederland", flag: "🇳🇱" },
    { city: "Antwerpen", country: "België", flag: "🇧🇪" },
    { city: "Gent", country: "België", flag: "🇧🇪" }
  ]
};

export const notificationPlans: Record<string, NotificationPlan[]> = {
  es: [
    { name: "Premium", price: "15", currency: "€" },
    { name: "Premium Plus", price: "50", currency: "€" },
    { name: "Premium Pro", price: "25", currency: "€" },
    { name: "Pro", price: "10", currency: "€" }
  ],
  en: [
    { name: "Premium", price: "18", currency: "$" },
    { name: "Premium Plus", price: "60", currency: "$" },
    { name: "Premium Pro", price: "30", currency: "$" },
    { name: "Pro", price: "12", currency: "$" }
  ],
  fr: [
    { name: "Premium", price: "15", currency: "€" },
    { name: "Premium Plus", price: "50", currency: "€" },
    { name: "Premium Pro", price: "25", currency: "€" },
    { name: "Pro", price: "10", currency: "€" }
  ],
  de: [
    { name: "Premium", price: "15", currency: "€" },
    { name: "Premium Plus", price: "50", currency: "€" },
    { name: "Premium Pro", price: "25", currency: "€" },
    { name: "Pro", price: "10", currency: "€" }
  ],
  it: [
    { name: "Premium", price: "15", currency: "€" },
    { name: "Premium Plus", price: "50", currency: "€" },
    { name: "Premium Pro", price: "25", currency: "€" },
    { name: "Pro", price: "10", currency: "€" }
  ],
  pt: [
    { name: "Premium", price: "15", currency: "€" },
    { name: "Premium Plus", price: "50", currency: "€" },
    { name: "Premium Pro", price: "25", currency: "€" },
    { name: "Pro", price: "10", currency: "€" }
  ],
  nl: [
    { name: "Premium", price: "15", currency: "€" },
    { name: "Premium Plus", price: "50", currency: "€" },
    { name: "Premium Pro", price: "25", currency: "€" },
    { name: "Pro", price: "10", currency: "€" }
  ]
};

export const getRandomNotification = (language: string) => {
  const cities = notificationCities[language] || notificationCities.es;
  const plans = notificationPlans[language] || notificationPlans.es;
  
  const randomCity = cities[Math.floor(Math.random() * cities.length)];
  const randomPlan = plans[Math.floor(Math.random() * plans.length)];
  const randomMinutes = Math.floor(Math.random() * 45) + 5; // 5-49 minutes
  
  return {
    city: randomCity,
    plan: randomPlan,
    minutesAgo: randomMinutes
  };
};