// astro-site/src/data/productos-en/kits/food-cost-templates.ts
// TIENDA INTERNACIONAL EN — Food Cost Kit Pro. COPIA TRADUCIDA Y ADAPTADA de la ficha ES
// astro-site/src/data/productos/kits/kit-escandallos.ts (mismo tipo, misma plantilla
// KitExcelLandingPage, mismo orden de campos). SPEC: scripts/productos-digitales/recipe-costing-kit/SPEC.md
//   · D2/D9 bis: nombre «Food Cost Kit Pro» (titlePre + titleGold y schema.productName EXACTOS) y
//     títulos de las 13 plantillas = los de los xlsx EN (dl/food-cost-templates/).
//   · D3: $19, pago único. D4: anclas como en ES, en USD (priceOld €49 → $59; bonos €27 → $39 y
//     €19 → $29, escalón $…9 por encima del cambio). Derivado: bonos $68 · total $127 ·
//     ahorro $40 · descuento 1 − 19/59 = 67,8 % → «-67%» (redondeo hacia abajo, como el ES: 75,5 % → «-75%»).
//   · Sin reviews ni aggregateRating en el JSON-LD. Testimonios: los del ES traducidos (John, 25-sep).
//   · D12 (benchmarks), D16 (solo Microsoft Excel), D18 (licencia), D15 (menu engineering solo
//     como paso básico de la guía).
//   · ogImage: la OG del ES (og-kit-escandallos.jpg) lleva texto en español incrustado; la EN es
//     og-food-cost-kit.jpg (Gemini, 1200×630, sin texto legible).
// DINERO: stripeEnvKey = VITE_STRIPE_PAYMENT_LINK_FOOD_COST_KIT (resuelto en el wrapper .astro).
import type { KitExcelData } from '../../productos/kits/types';

const data: KitExcelData = {
  slug: 'food-cost-templates',
  stripeEnvKey: 'VITE_STRIPE_PAYMENT_LINK_FOOD_COST_KIT',

  seo: {
    title: 'Food Cost Kit Pro: 13 Food Cost Templates for Excel | AI Chef Pro',
    description:
      '13 food cost templates for Excel: recipe cost cards, plate cost and pour cost calculators, menu pricing for 10 venue types, yield test and price tracker. One-time $19.',
    keywords:
      'food cost templates, food cost template, recipe costing template, menu costing template, food cost spreadsheet, food cost calculator excel, food cost excel template, plate cost calculator, pour cost calculator, menu pricing calculator, recipe cost card, food cost percentage, yield test, AI Chef Pro',
    ogImage: 'https://aichef.pro/og-food-cost-kit.jpg',
  },

  schema: {
    productName: 'Food Cost Kit Pro',
    productDescription:
      '13 food cost templates for Excel with automatic formulas, preloaded trim-loss rates and a menu pricing calculator. For chefs, managers and restaurant owners.',
    price: '19.00',
    priceValidUntil: '2026-12-31',
    // FAQPage schema: versiones CORTAS de las FAQ on-page (mismo patrón que el ES).
    faqs: [
      {
        q: 'Do I need advanced Excel skills to use the templates?',
        a: 'No. Everything is already set up: formulas, trim-loss rates and drop-downs. You only enter your ingredients, quantities and prices, and everything is calculated automatically.',
      },
      {
        q: 'Does it work in Google Sheets?',
        a: 'Yes. You can import the .xlsx files straight into Google Sheets and every formula carries over. They also work with LibreOffice Calc and Apple Numbers.',
      },
      {
        q: 'Is 30% a typical food cost?',
        a: 'It is a common rule of thumb, but the right target depends on the venue: fine dining 30-35%, casual dining 28-32%, fast casual 27-32%, cafés 25-30%, catering and food trucks 28-35%, bakeries 25-35% and bars 18-24% (pour cost).',
      },
      {
        q: 'How do I calculate food cost for a recipe?',
        a: 'Food cost % = cost per portion ÷ pre-tax menu price. Suggested menu price = cost per portion ÷ target food cost %. The recipe cost card does both automatically, including trim loss and a Q-factor.',
      },
      {
        q: 'What is the difference between AP and EP (yield)?',
        a: 'AP (as purchased) is what you buy; EP (edible portion) is what is left after trimming. Yield % = 100% − trim loss %. The kit preloads typical trim loss for 21 ingredient categories, and the Yield Test measures your own.',
      },
      {
        q: 'Can I use ounces and pounds — or grams?',
        a: 'Both. The examples use US customary units (lb, oz, fl oz), and the unit drop-down also has kg, g, L, ml and cl. The bakery template weighs in grams, the way pastry kitchens formulate. Buy in one unit and use another: the Conversions tab does the math, and it never mixes weight and volume.',
      },
      {
        q: 'Does it handle case prices and catch weight?',
        a: 'Yes. Enter the price exactly as it appears on the invoice (a 50 lb bag, a 36 x 1 lb case, a 15-dozen case of eggs, a keg) and the Conversions tab turns it into the unit you use in the recipe. Catch-weight items go in lb or kg.',
      },
      {
        q: 'How does it handle sales tax and VAT?',
        a: 'Every cost card has one Tax rate cell, 0% by default because US menu prices are pre-tax. Enter 20% for UK VAT or 10% for Australian GST to see the price including tax. Food cost is always calculated on the pre-tax price.',
      },
      {
        q: 'How do I calculate GP %?',
        a: 'GP % = (menu price ex VAT − cost per portion) ÷ menu price ex VAT. It is the mirror image of food cost %: a 30% food cost is a 70% GP. Every cost card shows gross profit per portion and target GP %.',
      },
      {
        q: 'What do the Yield Test and the Ingredient Price Tracker add?',
        a: 'The Yield Test turns the weighing of a whole cut or a cooked dish into the real trim loss for your cost card. The Price Tracker keeps your supplier prices in one sheet and flags any ingredient that goes up. It does not update the cost cards on its own: you paste the new price with Paste Special → Values.',
      },
      {
        q: 'What is not included?',
        a: 'It is a set of Excel templates, not software: no app, no POS or supplier integration, no automatic price updates and no labor costing. Menu engineering appears only as a basic step in the 30-day guide.',
      },
      {
        q: 'What currency will I pay in?',
        a: 'The price is $19 USD. At checkout, Stripe can show the amount in your local currency. The templates have no currency symbol: you type prices in your own currency.',
      },
      {
        q: 'Can I use it for several locations or with my clients?',
        a: 'One purchase covers one business with all its locations. You can use the templates with your clients, but you can\'t hand them copies: each business buys its own. Culinary schools can ask for a classroom license at info@aichef.pro.',
      },
      {
        q: 'Is it a subscription? Are future updates included?',
        a: 'No subscription: you pay once and get lifetime access to the online dashboard. When we add templates or improvements, you get them at no extra cost.',
      },
      {
        q: 'Is there a money-back guarantee?',
        a: 'Yes. A full 30-day guarantee. If the templates do not help you control your food cost, we refund 100% with no questions asked.',
      },
    ],
    breadcrumbName: 'Food Cost Kit Pro',
  },

  images: {
    // hero bg (6) — las MISMAS del ES
    gallery: [
      '/lovable-uploads/ai-gallery/tataki-presa-iberica-chimichurri.jpeg',
      '/lovable-uploads/ai-gallery/tartaleta-de-yuzu-y-merengue.jpeg',
      '/lovable-uploads/ai-gallery/cocktail-green-margarita.jpeg',
      '/lovable-uploads/ai-gallery/croqueta-jamon.jpeg',
      '/lovable-uploads/ai-gallery/croissant-bicolor-de-mantequilla-aichefpro.jpeg',
      '/lovable-uploads/ai-gallery/huevo-baja-temperatura-trufa.jpeg',
    ],
    // ContentGrid strip (6) — las MISMAS del ES
    gridGallery: [
      '/lovable-uploads/ai-gallery/croqueta-jamon.jpeg',
      '/lovable-uploads/ai-gallery/cocktail-garibaldi-fermentado.jpeg',
      '/lovable-uploads/ai-gallery/milhojas-vertical-de-vainilla-con-frambuesas-aichefpro-2.jpeg',
      '/lovable-uploads/ai-gallery/carpaccio-gambas.jpeg',
      '/lovable-uploads/ai-gallery/torrija-caramelizada-con-helado.jpeg',
      '/lovable-uploads/ai-gallery/cocktail-tepache-pina-asada.jpeg',
    ],
    whyBg: '/lovable-uploads/ai-gallery/cochinillo-asado.jpeg',
    buyBoxBg: '/lovable-uploads/ai-gallery/gambas-al-ajillo.jpeg',
    ctaBg: '/lovable-uploads/ai-gallery/falso-risotto-semillas-plancton.jpeg',
  },

  hero: {
    badgeTone: 'gold',
    badge: 'The #1 food cost kit for professional hospitality',
    // D2: titlePre + titleGold = «Food Cost Kit Pro» EXACTO; la cifra va en titlePost.
    titlePre: '',
    titleGold: 'Food Cost Kit Pro',
    titlePost: ': 13 Excel Templates to Control Your Food Cost',
    description:
      '13 food cost templates for Excel with automatic formulas, preloaded trim-loss rates and a menu pricing calculator. Work out the real cost of every dish and control the costs of your restaurant, bakery, bar, catering business or food truck from day one.',
    checkItems: [
      '13 professional Excel templates with automatic formulas',
      'Preloaded industry trim-loss (yield) rates',
      'Menu pricing calculator for 10 venue types',
      'Food cost percentage tracker with a trend chart',
      "ACTUAL food cost: type the price you charge today and the sheet flags it in red if you're over target",
      'Space for a photo of the dish on every recipe cost card',
    ],
    ctaLabel: 'BUY NOW — $19',
  },

  compatApps: {
    titleHtml: 'Works With the <span class="text-[#FFD700]">Tools</span> You Already Use',
    subtitleHtml:
      'Works best with <a href="/en" class="text-[#FFD700] hover:underline">AI Chef Pro</a>. Compatible with Excel, Google Sheets, PDF and more',
  },

  grid: {
    countGold: '13',
    headingRest: ' Professional Food Cost Templates',
    subtitle:
      'Every recipe cost card has the columns that matter — ingredient, category, purchase unit, price per unit, quantity, recipe unit, conversion factor, trim loss %, AP quantity and cost — with automatic formulas, preloaded trim-loss rates, a space for the dish photo and a print-ready US Letter layout.',
    fourCols: true,
    templates: [
      { icon: 'UtensilsCrossed', title: 'Recipe Cost Card & Plate Cost Calculator', desc: "The most complete template for à la carte dishes. Enter ingredients, quantities and purchase prices — the formulas work out the trim loss, the real cost per portion, food cost % and the suggested menu price from your target margin. And the other way round: type the price already on your menu and the sheet returns your ACTUAL food cost, in red if it's over target. Includes a space for a photo of the plated dish." },
      { icon: 'ChefHat', title: 'Tasting Menu Costing', desc: 'Built for tasting menus of 5 to 9 courses, with a cost card for each course. The summary sheet adds up the whole menu, works out the overall food cost and suggests the price per guest. Made for fine dining and premium experiences.' },
      { icon: 'ClipboardList', title: 'Prix Fixe & Set Menu Costing', desc: "Complete structure: starter, main, dessert and extras (bread & butter, plus a drink and coffee if they're included). Works out the full cost of the menu and the price you need to keep your margin. Includes a weekly rotation to plan 5 different menus and compare their costs." },
      { icon: 'Wine', title: 'Pour Cost Calculator (Cocktails & Drinks)', desc: 'Pour cost for 4 cocktails with standard US pours in fl oz, cost per ingredient and cost per drink. Set up for a bar pour cost target of 18-24%. The Bottle Sizes tab turns the bottle price on your invoice (750 ml, 1 L, 1.75 L) into a price per liter. Garnish and ice are costed line by line, and a spillage allowance covers over-pouring.' },
      { icon: 'CakeSlice', title: 'Bakery & Cake Pricing Calculator', desc: 'A pastry template weighed in grams, the way bakeries formulate, with pastry trim losses and yield per batch — how many units each recipe makes, with cost and price per unit. Comes with a chocolate cake, butter croissants and raspberry macarons, bought the way bakeries buy: 50 lb bags and cases of butter and eggs.' },
      { icon: 'PartyPopper', title: 'Catering Pricing Calculator & Quote', desc: 'The only template that puts food + staff + transport + rentals into one quote per guest. Set your target food cost and your markup on services, and get the price per guest instantly. Includes an event checklist and a client-ready proposal that keeps your costs and margin out of sight.' },
      { icon: 'Coffee', title: 'Café & Brunch Menu Costing', desc: 'Cost cards built for cafés, with a target food cost of 25-30%. Real examples: avocado toast, açaí bowl, eggs Benedict and carrot cake. Each recipe with its real cost broken down, so you can see which items make you money and which eat into it.' },
      { icon: 'Truck', title: 'Food Truck Menu Pricing & Break-Even', desc: 'Built for street food: fast recipes, speed of service and high margins. Includes a double smash burger, loaded fries and a pulled pork sandwich with their real cost per unit. Works out your daily break-even: how many units you need to sell to cover the day\'s fixed costs.' },
      { icon: 'TrendingDown', title: 'Food Waste Log', desc: 'Weekly log of real waste in 16 product families (meat, fish, fruit, dairy…), with a minimum, typical and maximum target for each one. The traffic light shows OK or ALERT as soon as waste goes over target. Includes a 12-week waste trend chart.' },
      { icon: 'Calculator', title: 'Menu Pricing Calculator', desc: 'Enter the cost of any dish and get the recommended menu price for 10 venue types: fine dining, casual dining, fast casual, café, catering, food truck, hotel F&B, pastry & bakery, bar & cocktails and delivery. Each with its industry target food cost range, and delivery with the platform commission taken off first.' },
      { icon: 'BarChart3', title: 'Food Cost Percentage Tracker', desc: 'Track your food cost over 12 consecutive periods (months or weeks). Enter beginning inventory, purchases, ending inventory and net sales: food cost comes from what you USED, not from what you bought — a big delivery at month-end no longer skews the number. Includes an annual trend chart and alerts when food cost goes over your limit.' },
      { icon: 'Scale', title: 'Yield Test (Butcher & Cooking Loss)', desc: "Weigh a whole cut and what's left after trimming it (butcher yield), or a dish before and after cooking (cooking loss), and the sheet gives you the real trim loss for your recipe cost card, with the value of the by-products already credited. It also works out the cost per usable lb, the portions per cut and a cost factor to pass on a supplier price change without repeating the test. Comes with template 01's whole beef tenderloin and template 08's smash burger as examples." },
      { icon: 'Banknote', title: 'Ingredient Price Tracker', desc: "Every ingredient from the kit's templates in one sheet, with supplier, pack size and price per lb, liter or each. Enter the price from your latest invoice and the sheet compares it with the previous one: ingredients that go up by more than your threshold (5% by default) turn red. It doesn't update the cost cards on its own: you copy the new price into each one with Paste Special → Values." },
    ],
  },

  why: {
    headingPre: 'Why This ',
    headingGold: 'Kit',
    headingPost: '?',
    subtitle:
      "These aren't generic templates. They're recipe cost cards designed by a chef who has worked in kitchens since the age of 17 and has been a restaurant consultant since 2010.",
    reasons: [
      { icon: 'Calculator', title: 'Real Formulas, Not Fixed Values', desc: 'Change an ingredient and everything recalculates: cost, trim loss, food cost % and suggested menu price. No manual errors.' },
      { icon: 'FileSpreadsheet', title: 'For Every Kind of Venue', desc: 'Restaurant, catering, bakery, bar, food truck, café. Each template adapted to how that business really works.' },
      { icon: 'TrendingDown', title: 'Preloaded Trim-Loss Rates', desc: '21 ingredient categories with the typical industry trim loss. Editable, so you can match your own kitchen.' },
      { icon: 'RefreshCw', title: 'Pay Once, Yours Forever', desc: 'No subscription. Lifetime access to the dashboard with every template. New templates at no extra cost.' },
    ],
    // Réplica del ES (John, 25-sep): mismas cinco píldoras de compatibilidad.
    compatLabel: 'Compatible with any spreadsheet software:',
    compatPills: [
      { label: 'Microsoft Excel', highlight: true },
      { label: 'Google Sheets' },
      { label: 'LibreOffice Calc' },
      { label: 'Apple Numbers' },
      { label: 'WPS Office' },
    ],
  },

  // Bio anclada (sin sumar cifras): traducción literal de la del ES.
  authorBio:
    'CEO of AI Chef Pro and founder of ChefBusiness Group. In kitchens since the age of 17 and a restaurant consultant since 2010. He has designed cost-control systems for hundreds of restaurants.',
  // authorBadges omitido → ui.authorBadgesDefault de i18n/tienda/en.json

  bonus: {
    headingPre: 'Exclusive ',
    headingGold: 'Bonuses',
    subtitle:
      'On top of the 13 templates, you get these extra resources — worth $68',
    items: [
      {
        icon: 'BookOpen',
        label: 'BONUS 1',
        title: 'Guide: How to Reduce Food Cost in 30 Days',
        value: '$39',
        desc: 'A week-by-week action plan to bring your food cost down: how to read an invoice, supplier negotiation tactics, a weekly checklist, a basic menu-engineering step and a worked case study built from real consulting work. 23-page PDF.',
        image: '/lovable-uploads/ai-gallery/focaccia-jardin-alta-hidratacion-aichefpro.jpeg',
      },
      {
        icon: 'FileSpreadsheet',
        label: 'BONUS 2',
        title: 'Actual vs Theoretical Food Cost (Inventory & Waste)',
        value: '$29',
        desc: 'Excel template with an incident log for waste (with reasons and corrective actions) and inventory control that compares actual usage with the theoretical usage from what you sold.',
        image: '/lovable-uploads/ai-gallery/hogaza-masa-madre-oreja-perfecta-aichefpro.jpeg',
      },
    ],
  },

  buyBox: {
    ctaLabel: 'YES, I WANT THE KIT — $19',
  },

  guarantee: {
    // headingPre por defecto = ui.guaranteeHeadingPreDefault («Satisfaction Guarantee »).
    text:
      "If the templates don't help you control your food cost, we'll refund 100% of your money. No questions, no hassle.",
    stats: [
      { number: '30', label: 'Day guarantee' },
      { number: '100%', label: 'Money back' },
      { number: '0', label: 'Awkward questions' },
    ],
  },

  // FAQ on-page (acordeón): guion del People Also Ask (research §6.3) + moneda, licencia (D18),
  // precios por caja, qué no incluye y Google Sheets como en el ES (John, 25-sep).
  faqs: [
    {
      q: 'Do I need advanced Excel skills to use the templates?',
      a: 'No. The templates come fully set up: formulas, trim-loss rates and drop-downs. You only enter your ingredients, quantities and prices, and everything is calculated automatically. Editable cells are green; everything else is protected so you can\'t delete a formula by accident.',
    },
    {
      q: 'Does it work in Google Sheets?',
      a: 'Yes. You can import the .xlsx files straight into Google Sheets and every formula carries over. They also work with LibreOffice Calc and Apple Numbers.',
    },
    {
      q: 'Is 30% a typical food cost?',
      a: 'It is a common rule of thumb, but the right target depends on the venue: fine dining 30-35%, casual dining 28-32%, fast casual 27-32%, cafés 25-30%, catering and food trucks 28-35%, hotel F&B 30-35%, pastry & bakery 25-35% and bars 18-24% (pour cost). The Menu Pricing Calculator comes with these ranges preloaded for 10 venue types.',
    },
    {
      q: 'How do I calculate food cost for a recipe?',
      a: 'Food cost % = cost per portion ÷ pre-tax menu price. The cost per portion is the sum of each ingredient (as-purchased quantity × price per unit, after trim loss) plus a Q-factor for seasonings, oil and small losses you don\'t cost line by line, all divided by the number of portions. Suggested menu price = cost per portion ÷ target food cost %. The recipe cost card does all of it automatically.',
    },
    {
      q: 'What is the difference between AP and EP (yield)?',
      a: 'AP (as purchased) is what you buy; EP (edible portion) is what is left after trimming. Yield % = 100% − trim loss %. The kit preloads the typical trim loss for 21 ingredient categories, with minimum and maximum, and you can adjust them. When you want your own number, the Yield Test (template 12) measures it from a real cut.',
    },
    {
      q: 'Can I use ounces and pounds — or grams?',
      a: 'Both. The examples use US customary units (lb, oz, fl oz), and the unit drop-down also has kg, g, L, ml and cl. The bakery template weighs in grams, the way pastry kitchens formulate. Buy in one unit and use another: the Conversions tab does the math, and it never mixes weight and volume.',
    },
    {
      q: 'Does it handle case prices and catch weight?',
      a: 'Yes. Enter the price exactly as it appears on the invoice — a 50 lb bag of flour, a 36 x 1 lb case of butter, a 15-dozen case of eggs, a 1/6 bbl keg — and the Conversions tab turns it into the unit you use in the recipe. Catch-weight items (priced by the actual weight) go in lb or kg. The drop-down has 13 common case and keg formats; for a case that isn\'t on the list, enter the price per lb or each (case price ÷ contents).',
    },
    {
      q: 'How does it handle sales tax and VAT?',
      a: 'Every cost card has one Tax rate cell, 0% by default: in the US menu prices are shown before sales tax. In the UK enter 20% VAT to see the menu price including VAT; in Australia, 10% GST. Food cost and GP are always calculated on the pre-tax price, and net sales exclude tax, service charges and tips.',
    },
    {
      q: 'How do I calculate GP %?',
      a: 'GP % = (menu price ex VAT − cost per portion) ÷ menu price ex VAT. It is the mirror image of food cost %: a 30% food cost is a 70% GP. Every recipe cost card shows gross profit per portion and target GP % at the suggested price, and your actual food cost from the price on your menu (actual GP % = 100% − that figure).',
    },
    {
      q: 'What do the Yield Test and the Ingredient Price Tracker add?',
      a: 'The Yield Test (template 12) turns the weighing of a whole cut (butcher yield) or a cooked dish (cooking loss) into the real trim loss you enter on your cost card, instead of the standard one. The Ingredient Price Tracker (template 13) keeps your supplier prices in one sheet, works out the price per lb, liter or each and flags any ingredient that goes up by more than your threshold. It doesn\'t update the cost cards on its own, because each template is a separate file: you paste the new price into the cost card with Paste Special → Values.',
    },
    {
      q: 'What is not included?',
      a: 'It is a set of Excel templates, not software: there is no app, no POS or supplier integration, no automatic price updates, no barcode inventory and no labor costing. The templates are separate files, so a new price is copied into each cost card by hand. Menu engineering appears only as a basic step in the 30-day guide.',
    },
    {
      q: 'What currency will I pay in?',
      a: 'The price is $19 USD, a one-time payment. At checkout, Stripe can show the amount in your local currency (for example GBP, EUR, CAD or AUD) and converts it for you. The templates themselves have no currency symbol: you type prices in your own currency.',
    },
    {
      q: 'Can I use it for several locations or with my clients?',
      a: 'One purchase covers one business, with all of its locations. If you are a consultant, you can use the templates with your clients, but you can\'t hand them copies: each business buys its own. Culinary schools and training centers can ask for a classroom license at info@aichef.pro.',
    },
    {
      q: 'Is it a subscription? Are future updates included?',
      a: 'No subscription: you pay once and get lifetime access to the online dashboard. When we add new templates or improvements, you get them at no extra cost — just download the files again.',
    },
    {
      q: 'Is there a money-back guarantee?',
      a: "Yes. A full 30-day guarantee. If the templates don't help you control your food cost, we'll refund 100% with no questions asked.",
    },
  ],

  cta: {
    heading: 'Stop Losing Money on Your Food Cost',
    subtitle:
      '13 professional templates for a one-time $19 — about what a single month of recipe costing software costs. Start controlling your costs today.',
    // D4: los valores de los bonos repiten los de bonus.items.
    items: [
      '13 professional Excel templates with automatic formulas',
      'Preloaded industry trim-loss rates (21 categories)',
      'Menu pricing calculator for 10 venue types',
      'Food cost percentage tracker with a trend chart',
      "ACTUAL food cost: type the price you charge today and the sheet flags it in red if you're over target",
      'BONUS: "How to Reduce Food Cost in 30 Days" guide ($39)',
      'BONUS: Actual vs Theoretical Food Cost (Inventory & Waste) ($29)',
      'Pay once — lifetime access to the online dashboard',
      '30-day money-back guarantee',
    ],
    ctaLabel: 'YES, I WANT THE KIT — $19',
  },

  // Testimonios: traducción fiel de los del ES (decisión de John, 25-sep-2026). Son del Kit de
  // Escandallos Pro, la edición española de este kit: por eso conservan sus nombres, negocios,
  // centilitros y euros, y el subtítulo lo dice. Solo se pintan: NO alimentan el JSON-LD.
  testimonials: {
    subtitle:
      'Hospitality professionals who already keep their food cost under control with Kit de Escandallos Pro, the Spanish edition of this kit',
    items: [
      { name: 'Alejandro Ruiz', role: 'Head Chef, Restaurante Alma', text: 'I used to cost my recipes in a notebook. With these templates I know the food cost of every dish down to the cent. I brought it down from 35% to 28% in two months.', avatar: '/avatars/chef-avatar-1.jpg' },
      { name: 'María José Pérez', role: 'Director of Operations, Grupo MJP', text: 'I run 4 restaurants, and these templates let me standardize recipe costing across all of them. The monthly dashboard is what I use most — I can see the trend at a glance.', avatar: '/avatars/avatar-2.jpg' },
      { name: 'Tomás Herrero', role: 'Owner, Tapería El Rincón', text: 'Nobody taught me recipe costing in culinary school. With the kit I just enter ingredients and prices, and the spreadsheet tells me exactly what to charge for each dish.', avatar: '/avatars/avatar-3.jpg' },
      { name: 'Lucía Fernández', role: 'Pastry Chef, Obrador La Dulce', text: 'The bakery template accounts for the waste on every ingredient. I found out I was losing 12% of my chocolate because I wasn\'t accounting for tempering loss properly.', avatar: '/avatars/avatar-4.jpg' },
      { name: 'Fernando Navarro', role: 'Catering Director, Banquetes FN', text: 'The catering template with per-guest pricing has changed my life. I now put together professional quotes in 10 minutes. It used to take me the whole morning.', avatar: '/avatars/avatar-5.jpg' },
      { name: 'Elena Molina', role: 'Bartender, Cóctel & Co', text: 'The cocktail template with measures in cl is perfect. I worked out that my premium gin and tonic has a pour cost of 16% — much better than I thought.', avatar: '/avatars/avatar-6.jpg' },
      { name: 'Antonio Delgado', role: 'Restaurant Consultant', text: 'I use the kit with all my consulting clients. It\'s the most practical tool I\'ve found for teaching cost control. I recommend it to everyone in the industry.', avatar: '/avatars/chef-avatar-5.jpg' },
      { name: 'Gonzalo Romero', role: 'Manager, Cafetería Central', text: 'The café template helped me discover that my avocado toast had a food cost of 42%. I adjusted the recipe and now it\'s at 27%. The kit pays for itself.', avatar: '/avatars/avatar-8.jpg' },
      { name: 'Pablo Soto', role: 'Owner, Food Truck Street Bites', text: 'With the food truck costing template I worked out that my best-selling smash burger was leaving me only 1.20 euros of margin. I reworked the recipe and now it\'s 2.80 euros. Information is power.', avatar: '/avatars/avatar-7.jpg' },
      { name: 'Sergio Vega', role: 'Purchasing Manager, Hotel Panorama', text: 'Tracking waste helped me negotiate better with suppliers. When I show them real waste data by category, I get better prices. An essential tool.', avatar: '/avatars/avatar-1.jpg' },
    ],
  },

  pricing: {
    priceOld: '$59',
    price: '$19',
    discountBadge: '-67%',
    heroNote: 'Special launch price. Going up soon',
    buyBoxNote: 'Special launch price — 67% off',
    bonusTotalLabel: 'Total value of the complete kit: $127 — 13 templates ($59) + 2 bonuses ($68)',
    bonusSaveLine: 'Save $40 TODAY!',
  },

  stickyLabel: 'FOOD COST KIT PRO — $19',
  stickyVariant: 'v1',

  footerLinks: [
    { href: '/en', label: 'aichef.pro' },
    { href: '/en/digital-products', label: 'Digital Products' },
    { href: '/en/food-cost-calculator-restaurant', label: 'Food Cost Calculator for Restaurants' },
    { href: '/en/food-cost-calculator-restaurant-ai', label: 'Restaurant Food Cost with AI' },
    { href: 'mailto:info@aichef.pro', label: 'Contact' },
  ],
  updateNote: 'Version 2.1 · September 2026',

  alreadyBought: {
    product: 'food-cost-templates',
    label: 'Already bought the kit? Get back into your dashboard',
  },
};

export default data;
