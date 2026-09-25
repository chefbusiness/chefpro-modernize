// astro-site/src/data/productos-en/kits/restaurant-inventory-templates.ts
// TIENDA INTERNACIONAL EN — Restaurant Inventory Kit Pro. COPIA TRADUCIDA Y ADAPTADA de la ficha ES
// astro-site/src/data/productos/kits/kit-inventario.ts (mismo tipo, misma plantilla
// KitExcelLandingPage, mismo orden de campos). Patrón = el piloto food-cost-templates.ts.
// SPEC: scripts/productos-digitales/restaurant-inventory-kit/SPEC.md (§6 = esta landing).
//   · D2/D26: nombre «Restaurant Inventory Kit Pro»; title SEO y H1 = «Restaurant Inventory Kit Pro:
//     9 Restaurant Inventory Templates for Excel». H1 en Forma B como el ES (titlePost «: » +
//     titleSubtitle en bloque): el texto del H1 es exactamente el de D2.
//   · D5: títulos de las 9 plantillas = los de los xlsx EN (dl/restaurant-inventory-templates/).
//   · D3: $19, pago único. D4: priceOld 49 € → $59; cada bono 9 € → $19. Derivados: bonos $38 ·
//     total $97 · ahorro $40 · descuento 1 − 19/59 = 67,8 % → «-67%» (redondeo hacia abajo, como el piloto).
//   · Sin reviews ni aggregateRating en el JSON-LD. Testimonios: los 8 del ES traducidos tal cual
//     (nombres, negocios, cifras en EUR), con el subtítulo de la edición española (TIENDA §3.5).
//   · D11 (impuesto neutro 0 % editable), D12 (°F, FDA Food Code 2022), D13 (sin símbolo de moneda
//     en las plantillas), I2 («7 templates» con unidades, nunca 8), I3 (pastillas del piloto +
//     «Printable (US Letter)»), I4 (licencia = la del piloto: un negocio con todos sus locales).
//   · Software: sin cifra de precio de la competencia (D22 §6 «why»).
//   · ogImage: la OG del ES (og-kit-inventario.jpg); sus rótulos ya están en inglés.
// DINERO: stripeEnvKey = VITE_STRIPE_PAYMENT_LINK_RESTAURANT_INVENTORY_KIT (resuelto en el wrapper .astro).
import type { KitExcelData } from '../../productos/kits/types';

const data: KitExcelData = {
  slug: 'restaurant-inventory-templates',
  stripeEnvKey: 'VITE_STRIPE_PAYMENT_LINK_RESTAURANT_INVENTORY_KIT',

  seo: {
    title: 'Restaurant Inventory Kit Pro: 9 Restaurant Inventory Templates for Excel',
    description:
      '9 restaurant inventory templates for Excel: par sheet, vendor price comparison, purchase orders, receiving log in °F, food waste log, FIFO and food cost KPIs. One-time $19.',
    keywords:
      'restaurant inventory templates, restaurant inventory template, restaurant inventory spreadsheet, restaurant inventory sheet, kitchen inventory template, food inventory template, bar inventory template, par sheet restaurant, receiving log template, food waste log template, fifo labels, restaurant order guide template, stock take template, AI Chef Pro',
    ogImage: 'https://aichef.pro/og-kit-inventario.jpg',
  },

  schema: {
    productName: 'Restaurant Inventory Kit Pro',
    productDescription:
      '9 restaurant inventory templates for Excel with automatic formulas to control inventory, vendors, purchase orders, receiving, food waste, FIFO and purchasing costs.',
    price: '19.00',
    priceValidUntil: '2026-12-31',
    // FAQPage schema: versiones CORTAS de las FAQ on-page (mismo patrón que el ES y el piloto).
    faqs: [
      {
        q: 'Does it work for any type of restaurant?',
        a: 'Yes. The 10 categories are preloaded for foodservice: meat & poultry, seafood, dairy & eggs, produce, dry goods, frozen, alcoholic beverages, non-alcoholic beverages, paper & cleaning and other.',
      },
      {
        q: 'Are the templates connected to each other?',
        a: 'They are nine separate files that speak the same language: the same 10 categories in all 9 templates and the same units in the 7 that list products. The Order Qty column tells you how much to reorder, and the vendor drop-down on the purchase order comes from the Vendors tab of that same file, which you fill in once.',
      },
      {
        q: 'Does it meet HACCP requirements?',
        a: 'They help you keep the receiving and traceability records your HACCP or food safety plan calls for; they do not replace the plan or an advisor. They include receiving temperatures in °F, FIFO/FEFO traceability and use-by tracking with color alerts.',
      },
      {
        q: 'Is there a free Excel template for restaurant inventory?',
        a: 'You will find free single inventory sheets online. This kit is a set of 9 templates that share the same categories, units and sample data — inventory with par levels, vendors, purchase orders, receiving, waste, FIFO and cost KPIs — for a one-time $19.',
      },
      {
        q: 'How do I make an inventory list for a restaurant?',
        a: 'List every item you buy by storage area, with its category, purchase unit, par level and price per unit, and count on-hand at the same time every week. The Kitchen & Bar Inventory Sheet comes set up that way with 50 sample items.',
      },
      {
        q: 'What is the best inventory system for restaurants: Excel or software?',
        a: 'Software pays off when you need POS integration, barcode scanning or several people counting at once. To count, reorder, receive, track waste and see your food cost without a monthly fee, a well-built Excel kit does the job.',
      },
      {
        q: 'Does Excel have an inventory template?',
        a: "Excel's template gallery has generic inventory lists, but they are not built for foodservice: no par levels by storage area, no receiving temperatures, no use-by vs best-by and no food cost.",
      },
      {
        q: 'Does it work in Google Sheets?',
        a: 'Yes. You can import the .xlsx files straight into Google Sheets and the formulas carry over. They also work with LibreOffice Calc and Apple Numbers.',
      },
      {
        q: 'How do I set par levels?',
        a: 'Par level = daily usage × (vendor lead time + days of safety stock). The Reorder Point Calculator works it out per item, and its sample data matches the par levels of the inventory sheet.',
      },
      {
        q: 'How does it handle sales tax and VAT?',
        a: 'The purchase order has a tax rate per category, 0% by default and editable: in the US, food bought for resale is usually exempt with a resale certificate; in the UK, type 0, 5 or 20% VAT. Check with your accountant.',
      },
      {
        q: 'Which temperatures does the receiving log use?',
        a: 'Degrees Fahrenheit, with the FDA Food Code 2022 limits for 15 product families: cold TCS food at 41 °F or below, hot food at 135 °F or above, shell eggs and live shellfish at 45 °F or below, and frozen food received frozen.',
      },
      {
        q: 'How is it different from inventory software?',
        a: 'Inventory software is a monthly subscription. This kit is $19, a one-time payment with no subscription, and you can customize everything. There is no app, no POS integration and no barcode scanning.',
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
        a: 'Yes. A full 30-day guarantee, 100% refund with no questions asked.',
      },
    ],
    breadcrumbName: 'Restaurant Inventory Kit Pro',
  },

  images: {
    // hero bg (6) — las MISMAS del ES (gridGallery omitido: cae en `gallery`, como en el ES)
    gallery: [
      '/lovable-uploads/ai-gallery/inventario-hero.jpg',
      '/lovable-uploads/ai-gallery/inventario-almacen.jpg',
      '/lovable-uploads/ai-gallery/inventario-recepcion.jpg',
      '/lovable-uploads/ai-gallery/inventario-proveedores.jpg',
      '/lovable-uploads/ai-gallery/inventario-cocina.jpg',
      '/lovable-uploads/ai-gallery/inventario-analisis.jpg',
    ],
    whyBg: '/lovable-uploads/ai-gallery/inventario-almacen.jpg',
    buyBoxBg: '/lovable-uploads/ai-gallery/inventario-almacen.jpg',
    ctaBg: '/lovable-uploads/ai-gallery/inventario-hero.jpg',
  },

  hero: {
    badgeTone: 'red',
    badge: 'Uncounted waste eats 3-5% of your purchases, from what we see auditing kitchens: counting it is the first step to getting it back',
    // D2/D26: titlePre + titleGold = «Restaurant Inventory Kit Pro»; Forma B como el ES.
    titlePre: 'Restaurant Inventory ',
    titleGold: 'Kit Pro',
    titlePost: ': ',
    titleSubtitle: '9 Restaurant Inventory Templates for Excel',
    description:
      '9 Excel templates with automatic formulas to manage inventory, vendors, purchase orders, receiving, food waste, FIFO and purchasing cost analysis. Stop losing money.',
    checkItems: [
      'Daily inventory with par levels and automatic reorder alerts',
      'Vendor list with price comparison across up to 5 vendors',
      '9 templates that speak the same language: the same 10 categories in all of them and the same units in the 7 that list products',
      'Receiving log with temperature (°F) and date checks',
      'Waste by category with a dashboard and an action plan',
    ],
    ctaLabel: 'BUY NOW — $19',
  },

  compatApps: {
    titleHtml: 'Print, Delegate and <span class="text-[#FFD700]">Control</span>',
    subtitleHtml:
      'Excel templates optimized to print on US Letter. Compatible with Excel, Google Sheets, LibreOffice and Numbers',
  },

  grid: {
    countGold: '9',
    headingRest: ' Restaurant Inventory Templates',
    subtitle:
      'Every template comes with automatic formulas and is built for how restaurants really work. Adjust it to your business and start controlling.',
    // fourCols omitido → grid-cols-2 md:grid-cols-3 (9 tarjetas, como el ES)
    templates: [
      { icon: 'Package', title: 'Kitchen & Bar Inventory Sheet with Par Levels', desc: 'Inventory by storage area (kitchen, bar, storeroom) with par levels, automatic reorder alerts and inventory valuation. A red/yellow/green traffic light, and an Order Qty column that tells you how much to reorder.' },
      { icon: 'Users', title: 'Vendor List, Price Comparison & Scorecard', desc: 'Full vendor directory, price comparison across up to 5 vendors per item (it shows the cheapest and flags expired quotes), a 5-criteria scorecard with an A/B/C/D grade, and vendor terms.' },
      { icon: 'ShoppingCart', title: 'Purchase Order Template & Order Log', desc: 'Enter your items and the purchase order does the math: tax rate per line (by item or by category, 0% by default and editable), subtotals, tax, total and a breakdown by rate, ready to send to your vendor. It warns you if you are below the vendor\'s order minimum. The Order Qty column of the inventory sheet tells you what to put here.' },
      { icon: 'ClipboardCheck', title: 'Receiving Log (Temperatures & Credit Requests)', desc: 'Check every delivery: quantity, quality, temperature in °F and dates. The sheet looks up the FDA Food Code limit for 15 product families and returns ACCEPT or REJECT on its own; shortages and rejections go to a discrepancy log with the credit memo you are owed.' },
      { icon: 'Trash2', title: 'Food Waste Log & Action Plan', desc: 'Daily log with 10 standard reasons (past use-by date, overproduction, butchery trim loss, cold chain failure, unexplained variance…). Automatic cost, analysis by category, a monthly dashboard and an action plan. Target: under 3% of purchases.' },
      { icon: 'RotateCcw', title: 'FIFO & Expiration Date Tracker', desc: 'FIFO/FEFO rotation with a 5-status traffic light. It tells a use-by date (discard) from a past best-by date (check it first), which is what stops you from throwing out a perfectly good can. Includes a storage map with 11 areas and their temperatures in °F.' },
      { icon: 'BarChart3', title: 'Purchasing Cost Analysis & Food Cost KPIs', desc: 'Spend by category, monthly trend, top 20 items, price-change alerts (>5%) and a KPI dashboard: food cost % and cost per cover.' },
      { icon: 'Clock', title: 'BONUS: Month-End Inventory Count', desc: 'A simplified one-page count for your full month-end inventory. It works out inventory value and the variance against last month automatically.' },
      { icon: 'Calculator', title: 'BONUS: Reorder Point & Order Quantity Calculator', desc: 'Works out when to reorder each item from daily usage, vendor lead time and safety stock, with the economic order quantity (EOQ).' },
    ],
  },

  why: {
    headingPre: 'Why This ',
    headingGold: 'Kit',
    headingPost: '?',
    subtitle:
      "These aren't generic warehouse templates. They're tools designed by a chef who has worked in kitchens since the age of 17 and has been a restaurant consultant since 2010.",
    reasons: [
      { icon: 'Utensils', title: 'Built for Restaurants', desc: 'The 10 standard foodservice categories preloaded in all 9 templates, with a drop-down: meat & poultry, seafood, dairy & eggs, produce, dry goods, frozen, alcoholic beverages, non-alcoholic beverages, paper & cleaning and other. Not generic warehouse templates.' },
      { icon: 'Calculator', title: 'Formulas That Save Money', desc: 'Par levels with alerts, automatic waste cost, price differences between vendors and spend by category. Food cost on usage and cost per cover, in the KPI dashboard. The numbers work for you.' },
      { icon: 'ShieldCheck', title: 'Records for Your HACCP Plan', desc: 'Helps you keep the receiving and traceability records your HACCP or food safety plan asks for: receiving temperatures, FIFO/FEFO traceability, use-by tracking and a storage map. It does not replace the plan or an advisor.' },
      { icon: 'RefreshCw', title: 'Inventory Software Is a Monthly Subscription. This Kit Is $19, Once', desc: 'To control inventory, vendors and waste without paying a subscription, this is enough: in Excel, for a one-time payment and with no per-user fees. Ready for 100 inventory items, 100 waste lines a month, 50 FIFO lots and 30 order lines; add more by unprotecting the sheet (there is no password).' },
    ],
    // Pastillas del piloto + «Printable (US Letter)» (SPEC D22, I3).
    compatLabel: 'Compatible with any spreadsheet software:',
    compatPills: [
      { label: 'Microsoft Excel', highlight: true },
      { label: 'Google Sheets' },
      { label: 'LibreOffice Calc' },
      { label: 'Apple Numbers' },
      { label: 'WPS Office' },
      { label: 'Printable (US Letter)' },
    ],
  },

  // Bio y chips del piloto EN (SPEC §6): bio anclada, sin sumar cifras.
  authorBio:
    'CEO of AI Chef Pro and founder of ChefBusiness Group. In kitchens since the age of 17 and a restaurant consultant since 2010. He has designed cost-control systems for hundreds of restaurants.',
  // authorBadges omitido → ui.authorBadgesDefault de i18n/tienda/en.json

  bonus: {
    headingPre: 'Exclusive ',
    headingGold: 'Bonuses',
    subtitle:
      'Besides the 7 core templates, you get these extra resources — worth $38',
    items: [
      {
        icon: 'Clock',
        label: 'BONUS 1',
        title: 'Month-End Inventory Count',
        value: '$19',
        desc: 'A simplified one-page count for your full month-end inventory. It works out inventory value and flags significant variances against last month. Optimized for printing.',
        image: '/lovable-uploads/ai-gallery/inventario-almacen.jpg',
      },
      {
        icon: 'Calculator',
        label: 'BONUS 2',
        title: 'Reorder Point & Order Quantity Calculator',
        value: '$19',
        desc: 'Enter daily usage, lead time and safety stock — it calculates the reorder point and the economic order quantity (EOQ) automatically.',
        image: '/lovable-uploads/ai-gallery/inventario-analisis.jpg',
      },
    ],
  },

  buyBox: {
    ctaLabel: 'YES, I WANT THE INVENTORY KIT — $19',
  },

  guarantee: {
    // headingPre por defecto = ui.guaranteeHeadingPreDefault («Satisfaction Guarantee »).
    text:
      "If the templates don't help you cut waste and control your restaurant's purchasing better, we'll refund 100% of your money. No questions, no hassle.",
    stats: [
      { number: '30', label: 'Day guarantee' },
      { number: '100%', label: 'Money back' },
      { number: '0', label: 'Awkward questions' },
    ],
  },

  // FAQ on-page (acordeón): las 6 del ES traducidas (licencia = D18 del piloto, I4) + semillas del
  // People Also Ask de la SPEC §6 + impuesto (D11), temperaturas (D12) y moneda.
  faqs: [
    {
      q: 'Does it work for any type of restaurant?',
      a: "Yes. The 10 categories are preloaded for foodservice in general: meat & poultry, seafood, dairy & eggs, produce, dry goods, frozen, alcoholic beverages, non-alcoholic beverages, paper & cleaning and other. Just ignore the ones that don't apply to your business.",
    },
    {
      q: 'Are the templates connected to each other?',
      a: "They are nine separate files, on purpose: they don't link to each other, because a linked workbook breaks as soon as you move a file to another folder and you would see #REF!. What they do share is the language: the same 10 categories in all 9 templates and the same units in the 7 that list products (the receiving log also sorts items by food safety family, because the temperature limit is set by the FDA Food Code, not by your purchasing category, and it includes the bridge between the two lists). In the inventory sheet, the Order Qty column tells you how much to reorder when on-hand drops below the par level, and the vendor drop-down on the purchase order comes from the Vendors tab of the purchase order file itself, which you fill in once. The sample data is the same in all nine: the same items, the same prices and the same six sample vendors.",
    },
    {
      q: 'Does it meet HACCP requirements?',
      a: 'They help you keep the receiving and traceability records your HACCP or food safety plan calls for; they do not replace the plan or an advisor. The receiving log checks temperatures by product family against the FDA Food Code 2022 limits, and the FIFO tracker manages use-by and best-by dates with color alerts — useful for your records and inspections.',
    },
    {
      q: 'Is there a free Excel template for restaurant inventory?',
      a: 'You will find free single inventory sheets online, and they are fine for a one-off count. This kit is a set of 9 templates that share the same categories, units and sample data: inventory with par levels, vendors, purchase orders, receiving, food waste, FIFO and food cost KPIs, plus two bonuses, for a one-time $19.',
    },
    {
      q: 'How do I make an inventory list for a restaurant?',
      a: 'List every item you buy by storage area (kitchen, bar, storeroom), with its category, purchase unit, par level and price per unit. Count on-hand at the same time every week, and the sheet tells you what is running low, how much to order and what your inventory is worth. The Kitchen & Bar Inventory Sheet comes with 50 sample items in that structure: replace them with yours.',
    },
    {
      q: 'What is the best inventory system for restaurants: Excel or software?',
      a: 'Software pays off when you need POS integration, barcode scanning or several people counting at once. If what you need is to count, reorder, receive deliveries, track waste and see your food cost without a monthly fee, a well-built Excel kit does the job. Many restaurants start in Excel and move to software once their process works.',
    },
    {
      q: 'Does Excel have an inventory template?',
      a: "Excel's template gallery has generic inventory lists, but they are not built for foodservice: no par levels by storage area, no receiving temperatures, no use-by vs best-by dates and no food cost. This kit is built for restaurants and bars.",
    },
    {
      q: 'Does it work in Google Sheets?',
      a: 'Yes. You can import the .xlsx files straight into Google Sheets and the formulas carry over. They also work with LibreOffice Calc and Apple Numbers. Editable cells are green; everything else is protected so you can\'t delete a formula by accident.',
    },
    {
      q: 'How do I set par levels?',
      a: 'Par level is what you use between two deliveries plus a safety cushion: daily usage × (vendor lead time + days of safety stock). Par max is the most you want on the shelf. The Reorder Point Calculator (bonus 2) works it out per item from daily usage, lead time and safety stock, and its sample data matches the par levels of the inventory sheet.',
    },
    {
      q: 'How does it handle sales tax and VAT?',
      a: 'The purchase order has a tax rate per category, 0% by default and editable. In the US, food you buy for resale is usually exempt with a resale certificate (0%), while supplies carry your local sales tax; in the UK, type 0, 5 or 20% VAT. The breakdown by rate is editable too, so you type the rates you actually pay — check with your accountant. The cost analysis works on amounts before tax.',
    },
    {
      q: 'Which temperatures does the receiving log use?',
      a: 'Degrees Fahrenheit, with the FDA Food Code 2022 limits for 15 product families: cold TCS food at 41 °F or below, hot food at 135 °F or above, shell eggs, milk and live shellfish at 45 °F or below, and frozen food received frozen. In the UK, follow your Safer Food Better Business limits (chilled food legally at 8 °C or below, 5 °C recommended).',
    },
    {
      q: 'How is it different from inventory software?',
      a: 'Inventory software is a monthly subscription, usually per location. This kit is $19, a one-time payment with no subscription, and you can customize 100% of it. What it is not: there is no app, no POS integration, no barcode scanning and no automatic price updates.',
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
      a: "Yes. A full 30-day guarantee. If you're not happy, we'll refund 100% with no questions asked.",
    },
  ],

  cta: {
    heading: 'Stop Losing Money on Waste and Blind Purchasing',
    subtitle:
      '9 professional templates to control your inventory for less than a single day of waste costs you.',
    // D4: los valores de los bonos repiten los de bonus.items.
    items: [
      'Daily inventory with par levels and reorder alerts',
      'Vendor list with price comparison',
      'Purchase orders with tax per line and an order-minimum alert',
      'Receiving log with temperature checks in °F',
      'Food waste log with a dashboard and an action plan',
      'FIFO and expiration dates with a color traffic light',
      'Cost analysis with KPIs: food cost % and cost per cover',
      'BONUS: Month-End Inventory Count ($19)',
      'BONUS: Reorder Point & Order Quantity Calculator ($19)',
    ],
    ctaLabel: 'YES, I WANT THE INVENTORY KIT — $19',
  },

  // Testimonios: traducción fiel de los 8 del ES (decisión de John, 25-sep-2026). Son del Kit de
  // Inventario, la edición española de este kit: por eso conservan sus nombres, negocios y euros,
  // y el subtítulo lo dice. Solo se pintan: NO alimentan el JSON-LD.
  testimonials: {
    subtitle:
      'Head chefs, managers and directors of operations who already control their inventory with Kit de Inventario, the Spanish edition of this kit',
    items: [
      { name: 'Miguel Fernandez', role: 'Head Chef, casual restaurant (60 covers)', text: 'Tracking waste was an eye-opener. We found out we were losing EUR 400 a month on badly stored vegetables alone. In 3 months we cut waste by 60%. The template paid for itself on day one.', avatar: '/avatars/avatar-1.jpg' },
      { name: 'Laura Martinez', role: 'Director of Operations, group of 4 restaurants', text: "The vendor comparison saved us more than EUR 2,000 in the first quarter. Having 5 vendors' prices in one table with a price-change traffic light is a game changer when you negotiate.", avatar: '/avatars/avatar-2.jpg' },
      { name: 'Carlos Ramos', role: 'Owner, gastrobar in Barcelona', text: 'We used to order by eye. With the purchase order template and the reorder points, we no longer run out on a Friday night or throw food away on Monday.', avatar: '/avatars/avatar-3.jpg' },
      { name: 'Patricia Vega', role: 'Storeroom Manager, 4-star hotel (180 rooms)', text: 'The receiving log has saved us from 3 temperature incidents in the last month. Now everything is on record: vendor, quantity, temperature, expiration date.', avatar: '/avatars/avatar-4.jpg' },
      { name: 'Andres Lopez', role: 'Executive Chef, event catering', text: 'The color-coded FIFO is brilliant. My cooks get it at a glance from the color, without doing the date math. Our losses from expired product dropped by 80%.', avatar: '/avatars/avatar-5.jpg' },
      { name: 'Elena Ruiz', role: 'Restaurant consultant, 12+ years', text: "I use it with all my clients. It's the most complete kit I've seen in Spanish: from daily inventory to cost analysis with a dashboard. It professionalizes management from day one.", avatar: '/avatars/avatar-6.jpg' },
      { name: 'Jorge Navarro', role: 'Manager, artisan pizzeria (2 locations)', text: "The reorder point calculator changed our lives. We know exactly when to order each ingredient based on our daily usage and the vendor's lead time.", avatar: '/avatars/avatar-7.jpg' },
      { name: 'Diego Serrano', role: 'Purchasing Director, restaurant chain', text: 'The cost analysis by category gives me the full picture: what percentage we spend on meat, seafood, produce, dry goods. Now I negotiate with real data, not gut feelings.', avatar: '/avatars/avatar-8.jpg' },
    ],
  },

  pricing: {
    priceOld: '$59',
    price: '$19',
    discountBadge: '-67%',
    heroNote: 'Special launch price. Going up soon',
    buyBoxNote: 'Special launch price — 67% off',
    bonusTotalLabel: 'Total value of the complete kit: $97 — 7 templates ($59) + 2 bonuses ($38)',
    bonusSaveLine: 'Save $40 TODAY!',
  },

  stickyLabel: 'RESTAURANT INVENTORY KIT PRO — $19',
  // stickyVariant omitido → default 'v2', como el ES.

  footerLinks: [
    { href: '/en', label: 'aichef.pro' },
    { href: '/en/digital-products', label: 'Digital Products' },
    { href: '/en/digital-products/food-cost-templates', label: 'Food Cost Kit Pro' },
    { href: 'mailto:info@aichef.pro', label: 'Contact' },
  ],
  updateNote: 'Version 2.0 · September 2026',

  alreadyBought: {
    product: 'restaurant-inventory-templates',
    label: 'Already bought the kit? Get back into your dashboard',
  },
};

export default data;
