/**
 * Gastro Pro Prompts eBook — tienda internacional EN (3-oct-2026).
 * Ficha de datos de /en/digital-products/ai-prompts-for-restaurants: COPIA TRADUCIDA del texto que la
 * landing ES (components/pages/ProPromptsEbookPage.astro, sin ficha propia) lleva inline. La pinta
 * components/pages/ProPromptsEbookPageEn.astro, gemelo de esa plantilla (mismas secciones, clases,
 * imágenes y orden). SPEC: scripts/productos-digitales/pro-prompts-ebook-en/SPEC.md.
 *
 * La leen además, por regex, tres scripts:
 *  - sync-payment-links.py / gate-flujo-postpago.py: `slug` + `stripeEnvKey` (productId → env var).
 *  - sync-product-prices.py: `schema.price` (con la moneda USD de TIENDAS.en) → product-prices.ts.
 *  - tienda-gate.py: exige que exista una ficha productos-en/**\/<slug>.ts por producto EN vivo.
 * Por eso `slug:` es el primer campo y `schema: { … }` va a 2 espacios con su cierre `  },`.
 *
 * Reglas (TIENDA-INTERNACIONAL §3.5 y §6): sin «€», sin aggregateRating ni review; testimonios del
 * ES traducidos tal cual (nombres sin tilde, como en los kits EN) y marcados como edición española.
 */

export interface EbookEnCategory { icon: string; title: string; desc: string }
export interface EbookEnTestimonial { name: string; role: string; text: string; avatar: string }

const data = {
  slug: 'ai-prompts-for-restaurants',
  stripeEnvKey: 'VITE_STRIPE_PAYMENT_LINK_AI_PROMPTS_FOR_RESTAURANTS',
  productName: 'Gastro Pro Prompts eBook',

  seo: {
    title: 'Gastro Pro Prompts eBook: 300 AI Prompts for Restaurants & Hospitality | AI Chef Pro',
    description:
      '300+ AI prompts for chefs, restaurant managers, pastry chefs, bartenders and restaurant owners. Works with ChatGPT, Claude and AI Chef Pro. Just $14.',
    keywords:
      'AI prompts for restaurants, ChatGPT prompts for restaurants, AI prompts for chefs, restaurant AI, AI for hospitality, chef prompts eBook, ChatGPT for professional kitchens, AI prompts for pastry chefs, catering AI prompts, AI Chef Pro',
    ogImage: 'https://aichef.pro/tienda-en/ai-prompts-for-restaurants/ebook-mockup-bundle-en.jpg',
  },

  schema: {
    productName: 'Gastro Pro Prompts eBook — 300+ AI prompts for restaurants and hospitality',
    productDescription:
      'eBook with 300+ AI prompts built for restaurants and hospitality: creative cooking, pastry, catering, management, leadership, marketing and more.',
    price: '14.00',
    priceValidUntil: '2026-12-31',
    breadcrumbName: 'Gastro Pro Prompts eBook',
  },

  pricing: {
    priceOld: '$59',
    price: '$14',
    discountBadge: '-76%',
    heroNote: 'Special launch price. Going up soon',
    buyBoxNote: 'Special launch price — 76% off',
    bonusSaveLine: 'Save $45 TODAY!',
  },

  mockup: {
    webp: '/tienda-en/ai-prompts-for-restaurants/ebook-mockup-bundle-en.webp',
    png: '/tienda-en/ai-prompts-for-restaurants/ebook-mockup-bundle-en-sm.png',
    alt: 'Gastro Pro Prompts — eBook, tablet and phone with 300+ AI prompts for restaurants and hospitality',
  },

  checkItems: [
    'PDF eBook + a private dashboard with 76 more copy-ready prompts',
    '300+ prompts for every corner of hospitality',
    '8 free professional tools included',
    'Works with ChatGPT, Claude, Perplexity, DeepSeek and more',
    'Free lifetime updates',
  ],

  categories: [
    { icon: 'ChefHat', title: 'Cooking & Recipes', desc: 'More than 40 prompts for chefs and cooks: create original recipes with the ingredients you have, adapt dishes to the season, explore fine-dining techniques and the fusion of world cuisines. Includes prompts for professional plating and presentation.' },
    { icon: 'Calculator', title: 'Management & Costs', desc: "Essential prompts for managers and owners: work out food cost in seconds, generate recipe cost cards automatically, analyze profitability dish by dish and optimize purchasing with your vendors. Turn AI into your kitchen's financial controller." },
    { icon: 'Cake', title: 'Pastry & Bakery', desc: "A section for pastry chefs, bakers and chocolatiers: formulas with baker's percentages, fermentation techniques, flavor combinations and recipe adaptations for food intolerances. Build seasonal menus in minutes." },
    { icon: 'Wine', title: 'Front of House, Bar & Drinks', desc: 'For bartenders and sommeliers: create signature cocktails, design dish-by-dish pairings, write wine descriptions for your list and sharpen front-of-house service. Includes beverage trend and menu-writing prompts.' },
    { icon: 'CalendarDays', title: 'Catering & Events', desc: 'Write tailored proposals and detailed per-guest quotes, plan logistics and design menus for weddings, corporate events and banquets. Every prompt is built to impress the client and close the event.' },
    { icon: 'Beaker', title: 'Food Pairing', desc: 'Discover science-based ingredient combinations: pairings by aroma compounds, smart substitutions when an ingredient runs out and unexpected combinations that surprise your guests. Creativity backed by science.' },
    { icon: 'Megaphone', title: 'Restaurant Marketing', desc: 'Prompts to create social media content, optimize your local SEO on Google, respond to reviews professionally, build email marketing campaigns and position your brand. An AI community manager, built in.' },
    { icon: 'ShieldCheck', title: 'Allergens & Food Safety', desc: 'Generate complete allergen spec sheets, labeling that follows the rules where you operate, up-to-date HACCP procedures and training plans for your team. Stay compliant without spending hours on paperwork.' },
    { icon: 'Briefcase', title: 'Business Management', desc: 'From business plans for new concepts to pricing strategies and franchise feasibility studies. Includes consulting prompts that help you make strategic decisions based on data, not gut feeling.' },
    { icon: 'Users', title: 'Leadership & Teams', desc: 'Prompts to sharpen your kitchen leadership: performance reviews, training plans, onboarding procedures for new hires and communication techniques for your brigade. Manage people, not just plates.' },
    { icon: 'Cpu', title: 'Bonus: Prompt Engineering Guide', desc: 'Learn to write your own prompts with the 5-element method: Role, Context, Task, Parameters and Format. Includes before-and-after examples for every area of hospitality.' },
    { icon: 'ClipboardList', title: 'Bonus: Templates + Cheat Sheet', desc: 'Fill-in-the-blank prompt templates and a one-page cheat sheet of the 20 best prompts, in a spreadsheet you can reuse every day.' },
  ] as EbookEnCategory[],

  testimonials: {
    subtitle:
      'Hospitality professionals who already use the prompts every day, from the Spanish edition of this eBook',
    items: [
      { name: 'Carlos Martinez', role: 'Executive Chef, El Olivo restaurant', text: "I've been in kitchens for 20 years and never thought AI would save me this much time. The creative recipe prompts have given me ideas that would have taken me weeks of R&D on my own.", avatar: '/avatars/chef-avatar-1.jpg' },
      { name: 'Laura Sanchez', role: 'Manager, LB restaurant group', text: 'The management and cost prompts are pure gold. Within a week I had food cost under control across 3 restaurants with the templates the AI generates.', avatar: '/avatars/avatar-2.jpg' },
      { name: 'Miguel Angel Torres', role: 'Owner, La Esquina gastrobar', text: "I bought the eBook expecting generic prompts. I was completely wrong: they're built for hospitality and they work from day one.", avatar: '/avatars/avatar-3.jpg' },
      { name: 'Ana Belen Ruiz', role: 'Pastry chef, Dulce Ana bakery', text: "The pastry section is incredible. I've created 15 new recipes for the season with the combination and technique prompts. My customers love them.", avatar: '/avatars/avatar-4.jpg' },
      { name: 'Javier Moreno', role: 'Catering Director, EventosPro', text: 'The catering prompts help me put together tailored proposals in minutes. Each event quote used to take me half a day.', avatar: '/avatars/avatar-5.jpg' },
      { name: 'Sofia Herrera', role: 'Bartender, The Cocktail Lab', text: "I use the mixology prompts to create seasonal cocktails and pairings. The AI suggests combinations I'd never have thought of.", avatar: '/avatars/avatar-6.jpg' },
      { name: 'Roberto Garcia', role: 'Restaurant Consultant', text: "I recommend the eBook to all my clients. It's the fastest way for a restaurant to start using AI without any technical training.", avatar: '/avatars/chef-avatar-3.jpg' },
      { name: 'Andres Lopez', role: 'Head Chef, Hotel Grand Palace', text: 'The allergen and food safety prompts have saved me hours of paperwork. Now I generate complete spec sheets in seconds.', avatar: '/avatars/avatar-8.jpg' },
      { name: 'Diego Fernandez', role: 'Owner, El Mexicano food truck', text: "With the marketing prompt I built the whole month's social media plan in 20 minutes. Before, I didn't even know where to start with Instagram.", avatar: '/avatars/avatar-7.jpg' },
      { name: 'Marcos Navarro', role: 'HR Director, CN restaurant group', text: 'The leadership and team prompts help me prepare performance reviews, training plans and onboarding procedures. An essential tool.', avatar: '/avatars/avatar-1.jpg' },
    ] as EbookEnTestimonial[],
  },

  reasons: [
    { icon: 'Globe', title: 'For the Whole Industry, Not Just the Kitchen', desc: "Whether you're a chef, manager, pastry chef, bartender or restaurant owner, every prompt is designed for your specific role in the business." },
    { icon: 'FlaskConical', title: 'Built Around AI Chef Pro', desc: 'Every prompt is written around the agents on AI Chef Pro, so you get consistent, professional-grade results in real hospitality settings.' },
    { icon: 'Clock', title: 'Save Hours of Work', desc: "Stop experimenting with AI. Get quality results in seconds, whether it's a recipe, a catering quote or an Instagram post." },
    { icon: 'RefreshCw', title: 'Pay Once, Yours Forever', desc: 'No subscriptions or recurring payments. Your private dashboard keeps growing with new prompts and categories. Every future improvement is yours at no extra cost.' },
  ],

  author: {
    bio: 'CEO of AI Chef Pro and founder of ChefBusiness Group. In professional kitchens since 17 and a restaurant consultant since 2010. He combines his industry experience with applied artificial intelligence to help hundreds of professionals transform their food businesses.',
    badges: ['CEO, AI Chef Pro', 'Founder of ChefBusiness', 'In professional kitchens since 17'],
  },

  bonuses: [
    { icon: 'BookOpen', label: 'BONUS 1', title: 'Restaurant Prompt Engineering Guide', value: '$29', desc: 'Learn to write your own perfect hospitality prompts from scratch with the AI Chef Pro method. An editable Word document you can customize.', image: '/lovable-uploads/ai-gallery/focaccia-jardin-alta-hidratacion-aichefpro.jpeg' },
    { icon: 'FileText', label: 'BONUS 2', title: 'Templates + Cheat Sheet', value: '$25', desc: 'A spreadsheet with ready-to-use templates and a quick summary of the best hospitality prompts.', image: '/lovable-uploads/ai-gallery/hogaza-masa-madre-oreja-perfecta-aichefpro.jpeg' },
  ],

  guarantee: {
    text: "If the eBook doesn't exceed your expectations, we'll refund 100% of your money. No questions, no hassle.",
    stats: [
      { number: '30', label: 'Day guarantee' },
      { number: '100%', label: 'Money back' },
      { number: '0', label: 'Awkward questions' },
    ],
  },

  // On-page FAQ (acordeón) y FAQPage: las 6 del ES traducidas. En el ES la respuesta 1 del acordeón
  // lleva una frase más que la del schema; se conserva la misma diferencia (`aSchema`).
  faqs: [
    { q: 'How do I get access after paying?', a: "Right after payment you'll receive an email with your personal, unique access link to the Pro Prompts Library, where you'll find the downloadable eBook and all the bonuses. The link is personal and non-transferable.", aSchema: "Right after payment you'll receive an email with your personal, unique access link to the Pro Prompts Library, where you'll find the downloadable eBook and all the bonuses." },
    { q: 'Does it only work with AI Chef Pro, or with other AIs too?', a: 'The prompts are optimized for AI Chef Pro but work perfectly with ChatGPT, Claude, Perplexity, DeepSeek, Gemini, KIMI and any conversational AI.' },
    { q: 'What format is the eBook?', a: 'A high-quality PDF that works on every device: phone, tablet and computer.' },
    { q: 'Will I get updates?', a: 'Yes. All future updates are free. As AI Chef Pro launches new AI agents, the eBook is updated and you get the new version automatically.' },
    { q: 'How does the guarantee work?', a: "You have a full 30 days to try it. If you're not satisfied for any reason, we'll refund 100%, no questions asked." },
    { q: 'Do I need any prior experience with AI?', a: 'Not at all. The prompts are ready to copy and paste. Professional results from day one, whatever your level.' },
  ] as { q: string; a: string; aSchema?: string }[],

  ctaItems: [
    'Complete eBook with 300+ prompts for every corner of hospitality',
    'BONUS 1: Restaurant Prompt Engineering Guide ($29)',
    'BONUS 2: Downloadable Templates + Cheat Sheet ($25)',
    'Pay once: lifetime access to the online dashboard',
    'Ongoing updates with new prompts at no extra cost',
    '30-day money-back guarantee',
  ],

  stickyLabel: 'GET THE EBOOK — $14',

  // Pie: el ES enlaza a /kit-escandallos; aquí, a su gemelo EN.
  footerLinks: [
    { href: '/en', label: 'aichef.pro' },
    { href: '/en/digital-products/food-cost-templates', label: 'Food Cost Kit Pro' },
    { href: 'mailto:info@aichef.pro', label: 'Contact' },
  ],

  alreadyBought: {
    product: 'ai-prompts-for-restaurants',
    label: 'Already bought the eBook? Get back into your dashboard',
  },
};

export default data;
