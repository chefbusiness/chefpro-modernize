// astro-site/src/data/productos-en/guias/food-cost-menu-engineering-guide.ts
// TIENDA INTERNACIONAL EN — Food Cost + Menu Engineering Guide. COPIA TRADUCIDA Y ADAPTADA de la ficha ES
// astro-site/src/data/productos/guias/guia-food-cost-ingenieria-menu.ts (mismo tipo GuiaData, misma plantilla
// GuiaLandingPage con lang="en", mismo orden de campos). Primera guía de la tienda EN.
// SPEC: scripts/productos-digitales/guia-food-cost-en/SPEC.md (D1-D3, D5-D9, D13-D14).
//   · D1: nombre «Food Cost + Menu Engineering Guide» (titlePre + titleGold y schema.productName EXACTOS: ya
//     publicado como «Coming soon» en el hub EN). Slug/productId food-cost-menu-engineering-guide.
//   · D2: $59, pago único (propuesta; lo confirma John al crear el Payment Link). SIN anclas: sin priceOld,
//     descuento, «Total value» ni «Save $» (a4cc7a14: nada de precios tachados en la tienda EN).
//   · D3 (DataForSEO US, 15-oct): intención «how-to» del operador. Title con el nombre del producto primero y
//     «Menu Pricing» + «Food Cost %» detrás; meta con «menu pricing», «how to calculate food cost» y «menu
//     engineering»; FAQ con las PAA («7 menu pricing methods» → la guía usa 4 de precio + 4 de ingeniería, sin
//     inventar 7; «price out a menu»; «30/30/30 rule» → solo lo que la guía sostiene: estructura de costes y
//     prime cost, sin inventar el origen de la regla). Sin canibalizar el Food Cost Kit Pro (intención
//     «calculator / templates»): FAQ 1 y footer enlazan al kit, y el kit enlaza aquí.
//   · D7 (impuestos): «sales tax, VAT and GST by channel», nunca «VAT by channel» a secas. Hechos de los
//     capítulos 3-4 y 15-16 EN y de las hojas Instructions de los 8 xlsx (0 % por defecto; UK 20 % incluido;
//     AU 10 % GST incluido; CA GST/HST encima como en EE. UU.; impuesto de compra = coste en EE. UU. y fuera del
//     coste si estás registrado para VAT o GST/HST).
//   · Cifras SOLO de los entregables: PDF guía 94 págs. y bonus 31 págs. (PyMuPDF, 15-oct), 20 capítulos,
//     8 xlsx (SPEC §2), 20 platos de ejemplo + 5 filas libres en el calculador de precios y en la matriz,
//     12 meses en el cuadro de prime cost, 13 semanas en el plan, objetivos de prime cost 65 % / 55 %, regla
//     US del 60 % (Toast, citada en el cap. 8). El «>1.100 € + IVA» del software del ES NO se traslada (son
//     tarifas españolas): la razón 4 habla de cuota anual sin cifra.
//   · Sin testimonios (el ES no tiene: D3 del ES), sin aggregateRating ni review. La plantilla, fuera del ES,
//     no pinta los avatares con 5 estrellas del hero si no hay testimonios.
//   · Imágenes: las 6 del ES (guia-foodcost-*.jpg) y su OG, revisadas el 15-oct: ninguna lleva texto en
//     español. Sin galería de capturas reales (el ES tampoco la tiene).
//   · D13: el bonus de equivalencias es el COMÚN de la tienda EN (`equivalents-guide`, dl/en-shared/).
// DINERO: stripeEnvKey = VITE_STRIPE_PAYMENT_LINK_FOOD_COST_MENU_ENGINEERING_GUIDE (resuelto en el wrapper .astro).
import type { GuiaData } from '../../productos/guias/types';

// FAQ: la misma lista en el acordeón y en el FAQPage (patrón de los planes EN, 13-oct).
const FAQS: { q: string; a: string }[] = [
  {
    q: 'Do I need the Food Cost Kit Pro if I buy this guide?',
    a: "No, but they work together. The Food Cost Kit Pro is 13 Excel templates to cost recipes for different types of venue; this guide is the method and the decision: what price to charge, which method to use and what to do with each dish. The guide includes its own recipe cost card and yield test, so you can work without the kit. If you have both, only those two basic tools overlap (the kit also has a recipe cost card and a yield test) and everything else is different.",
  },
  {
    q: 'What are the 7 menu pricing methods?',
    a: "Lists of \"7 methods\" change from one source to the next, so this guide doesn't sell you a number. It works with four pricing methods: cost factor (food cost % markup), target contribution margin in dollars, local market price and perceived value, and it shows when each one fits and why the cost factor breaks on high-cost dishes. Then it checks the whole menu with four menu engineering methods: Kasavana & Smith, Miller, Pavesic and Goal Value.",
  },
  {
    q: 'How do I price out a menu?',
    a: 'Start with a recipe cost card for every dish: the plate cost comes from the as-purchased quantity, with trim loss included. Choose the pricing method that fits each dish (cost factor, target margin, market price or perceived value) and check the food cost % on the pre-tax price. Then look at the menu as a whole with menu engineering, popularity against contribution margin within each category, and adjust takeout and delivery prices for commission and packaging. The guide walks a 20-dish example menu through every step, and the Menu Pricing Calculator puts the four methods side by side.',
  },
  {
    q: 'How do I calculate food cost percentage?',
    a: 'For a dish, food cost % = plate cost ÷ menu price before tax. For a period, use what you actually used: beginning inventory + purchases − ending inventory, divided by net food sales. The guide covers both, theoretical food cost from your cost cards and actual food cost from your inventory, and the four causes of the gap between them.',
  },
  {
    q: 'What is the 30/30/30 rule for restaurants?',
    a: "It's a rule of thumb about keeping your biggest costs near 30% of sales, and sources define it in different ways, so the guide doesn't build on it. What it uses is the cost structure behind the idea: product around 30% of net sales and labor between 30% and 35% for full service, read together as prime cost. The prime cost dashboard ships with a 65% target for full service and 55% for counter service, both in editable cells, and the guide sets them next to the widely quoted US rule of thumb of 60% at most.",
  },
  {
    q: 'Does it work in the UK, Canada or Australia?',
    a: "Yes. It's the US edition, with notes for the UK, Canada and Australia wherever the rules differ. Every workbook keeps its tax rate in editable cells, 0% by default because US menu prices are pre-tax: enter 20% for UK VAT or 10% for Australian GST to see the printed price including tax; in Canada you price before GST/HST, as in the US. The guide explains when the tax on your purchases is a cost (in the US, or if you're not registered) and when you reclaim it (registered for VAT or GST/HST), and gives GP %, the figure UK kitchens use, next to food cost %. Weights are in lb and oz, and bottles stay in milliliters (750 ml), as on the label. Every English edition also includes the US · UK · Canada · Australia Equivalents Guide, a bonus with the local terms, taxes, food safety and staff rules side by side.",
  },
  {
    q: 'How does sales tax affect food cost?',
    a: 'More than it seems. Food cost % is calculated on net sales, before tax, never on what the guest pays. In the US sales tax is added on the bill, so the menu price is already net; in the UK and Australia the printed price includes VAT or GST, so you take it out first (UK: printed price ÷ 1.20). On the cost side, sales tax you pay on supplies in the US is a cost, while a business registered for VAT or GST/HST reclaims it, so it stays out of the plate cost. Get it wrong and your food cost moves by several points, and you end up repricing the wrong dish.',
  },
  {
    q: 'Do drinks carry a different tax rate than food?',
    a: 'It depends on the country and the channel. In the UK, food and drink consumed on the premises, alcohol included, pay the same 20% standard rate, while takeaway splits hot food at 20% from most cold food at zero (soft drinks, confectionery and crisps excluded). In the US the rate depends on your state and city, and some add a meals tax. That is why the beverage and multichannel workbooks carry a tax matrix of nine cells, by channel and product type, all at 0% by default.',
  },
  {
    q: 'How do I calculate food cost for a dish sold through third-party delivery?',
    a: 'Add the packaging for each order to the plate cost and divide by what you actually take in: the price minus the platform commission. The multichannel simulator does it for every dish, tells you the pre-tax price you would need to hit your target and whether that price fits under the ceiling price your market accepts.',
  },
  {
    q: 'Why is the beverage cost target different from food cost?',
    a: "Because the cost structure is nothing alike: there's no butchering trim loss, you decide the unit of sale (by the glass or by the bottle) and turnover is different. The guide gives target ranges by category with their source and puts them in editable cells of the beverage workbook, so you compare your bar with the right reference and not with a generic number.",
  },
  {
    q: 'How often should I re-cost a recipe?',
    a: 'Not on a blind calendar but on triggers: a supplier price change, a change of season or pack size, a change of recipe or portion, plus a periodic review of the whole menu. Chapter 18 sets the protocol and shows where to look for prices, so you see increases coming instead of finding out from the invoice.',
  },
  {
    q: 'Is Kasavana & Smith the only valid menu engineering method?',
    a: "It's the most cited, not the only one, and on its own it falls short: it crosses popularity with contribution margin and ignores food cost %. The guide does it properly and adds Miller, Pavesic and Goal Value (Hayes & Huffman) on the same menu, with a sheet that flags where they disagree. That's usually where the decisions that matter are.",
  },
  {
    q: 'What is prime cost, and why does it matter more than food cost alone?',
    a: "It's product cost plus labor cost, including employer payroll taxes and benefits, over net sales. It matters because those are the two lines your operation actually moves, and because a great food cost can be propped up by extra prep hours that eat the margin. The dashboard shows them together month by month, with the target for your type of business in an editable cell.",
  },
  {
    q: 'Which programs do the Excel tools work with?',
    a: "Microsoft Excel, Google Sheets, LibreOffice and Apple Numbers. The workbooks are built on purpose without functions that break compatibility between programs, and they keep their calculated values saved inside the file, so they also display correctly on a phone and in viewers that don't recalculate.",
  },
  {
    q: 'What currency will I pay in?',
    a: 'The price is $59 USD, a one-time payment. At checkout, Stripe can show the amount in your local currency (for example GBP, EUR, CAD or AUD) and converts it for you. The workbooks have no currency symbol: you type amounts in your own currency.',
  },
  {
    q: 'Is it a subscription? Are future updates included?',
    a: 'No subscription: you pay once and get lifetime access to the online dashboard. When we improve a tool or update the guide, you download the new version at no extra cost, and the dashboard shows the change history of every version.',
  },
  {
    q: 'Is there a money-back guarantee?',
    a: "Yes. A full 30-day guarantee. If the guide doesn't meet your expectations, we'll refund 100% with no questions asked.",
  },
];

const data: GuiaData = {
  slug: 'food-cost-menu-engineering-guide',
  stripeEnvKey: 'VITE_STRIPE_PAYMENT_LINK_FOOD_COST_MENU_ENGINEERING_GUIDE',

  seo: {
    title: 'Food Cost + Menu Engineering Guide: Menu Pricing & Food Cost % | AI Chef Pro',
    description:
      'Menu pricing, how to calculate food cost and menu engineering, step by step: a 95-page guide, 8 Excel workbooks with live formulas and 12 solved exercises. $59.',
    keywords:
      'menu pricing, restaurant menu pricing, how to calculate food cost, food cost percentage, menu engineering, menu engineering matrix, plate cost, recipe costing, recipe cost card, prime cost restaurant, beverage cost, pour cost, kasavana smith, food cost guide, AI Chef Pro',
    ogImage: 'https://aichef.pro/og-guia-food-cost-ingenieria-menu.jpg',
  },

  showCompatibleApps: true,

  hero: {
    badge: 'For operators already open: price your menu and decide every dish with numbers, not gut feel',
    titlePre: 'Food Cost + ',
    titleGold: 'Menu Engineering Guide',
    subtitleLine: 'Recipe costing, menu pricing and menu profitability — with sales tax handled right and third-party delivery in the math',
    description:
      'The Food Cost Kit Pro tells you what each dish costs. This guide tells you what to do with that number: what to rework, reprice, redesign or remove, dish by dish, with the math in front of you.',
    checkItems: [
      'Complete guide in PDF + editable DOCX (20 chapters, 95 pages)',
      '8 Excel tools with live formulas: recipe cost card, yield and trim loss, menu pricing, menu engineering matrix, third-party delivery, beverage cost, prime cost and a 90-day plan',
      'Four menu engineering methods on the same menu, and a sheet that shows where they disagree',
      'Sales tax, VAT and GST by channel (dine-in, takeout and delivery) built into the math, for the US, UK, Canada and Australia',
      'Bonus: 12 solved exercises, step by step (32 pages)',
    ],
    ctaLabel: 'BUY THE GUIDE — $59',
    avatarAltPrefix: 'Professional',
  },

  pricing: {
    price: '$59',
    heroNote: 'One-time payment · lifetime access · updates included',
    buyBoxNote: 'One-time payment · lifetime access · updates included',
    bonusTotalLabel:
      'Included in the price: the guide, the 8 Excel tools and both bonuses: the solved exercises and the US · UK · Canada · Australia Equivalents Guide',
  },

  images: {
    gallery: [
      '/lovable-uploads/ai-gallery/guia-foodcost-hero.jpg',
      '/lovable-uploads/ai-gallery/guia-foodcost-carta.jpg',
      '/lovable-uploads/ai-gallery/guia-foodcost-cocina.jpg',
      '/lovable-uploads/ai-gallery/guia-foodcost-bodega.jpg',
      '/lovable-uploads/ai-gallery/guia-foodcost-delivery.jpg',
      '/lovable-uploads/ai-gallery/guia-foodcost-equipo.jpg',
    ],
    whyBg: '/lovable-uploads/ai-gallery/guia-foodcost-cocina.jpg',
    buyBoxBg: '/lovable-uploads/ai-gallery/guia-foodcost-hero.jpg',
    ctaBg: '/lovable-uploads/ai-gallery/guia-foodcost-carta.jpg',
  },

  grid: {
    countGold: '20',
    headingRest: ' Chapters + 8 Excel Tools + 12 Solved Exercises',
    subtitle:
      'Method, not theory. Every chapter leans on one of the eight Excel tools in the pack, and its tables come from the cells of those files, not from made-up examples. Written by a chef and restaurant consultant who has been pricing real menus since 2010.',
    // Títulos = los H2 de la guía EN (scripts/productos-digitales/guia-food-cost-en/en/food-cost-menu-engineering-guide.md).
    chapters: [
      { icon: 'Users', num: '01', title: 'Who This Guide Is For (and What You Will Not Find Here)', desc: 'Where we assume you start, a map from problem to chapter to tool, and the starter glossary of terms the rest of the guide uses.' },
      { icon: 'BarChart3', num: '02', title: 'The Four Numbers That Run Your Menu', desc: 'Food cost %, contribution margin in dollars, prime cost and average check. Which one rules each decision, and why looking at only one misleads you.' },
      { icon: 'Scale', num: '03', title: 'Sales Tax, VAT and the Error That Breaks Your Food Cost %', desc: 'The tax matrix by channel and product type, why the percentage is always calculated on net sales, and one dish read with and without tax.' },
      { icon: 'Banknote', num: '04', title: 'The Real Purchase Cost: What Actually Belongs on the Invoice Line', desc: 'How tax shows up on a supplier invoice, which lines carry it and why tax you reclaim as a registered business is not a cost.' },
      { icon: 'TrendingDown', num: '05', title: 'From AP to EP: Trim Loss, Yield and the Test That Replaces the Chart', desc: 'Butchering, cooking and byproducts: how to run a yield test and what a clean pound really costs you.' },
      { icon: 'FileSpreadsheet', num: '06', title: 'The Recipe Cost Card That Survives an Audit', desc: 'Edible quantity, trim loss, as-purchased quantity, plate cost and target price, line by line. What a card needs so nobody can argue with it.' },
      { icon: 'Search', num: '07', title: 'Theoretical vs. Actual Food Cost: Where the Money Leaks', desc: 'Actual usage from beginning inventory, purchases and ending inventory; the four causes of variance and a short count of the ten items that weigh most in your cost.' },
      { icon: 'Target', num: '08', title: 'Prime Cost: The Metric That Measures the Health of the Business', desc: 'Product and labor in one number, with the 65% full-service target and 55% for counter service. A "good" food cost can hide a broken labor cost.' },
      { icon: 'Calculator', num: '09', title: 'Four Ways to Price a Dish', desc: 'Cost factor, target dollar margin, market price and perceived value. When to use each one, and why the factor breaks on high-cost dishes.' },
      { icon: 'Sparkles', num: '10', title: 'Pricing Psychology: What Is Proven and What Is Myth', desc: 'The decoy effect, descriptive names and price formatting, each with its study and its caveat, and what circulates in the trade with no evidence behind it.' },
      { icon: 'LayoutGrid', num: '11', title: 'Menu Engineering I: Kasavana & Smith Done Right', desc: 'The classic menu engineering matrix done properly: the 70% popularity rule split by category, contribution margin and what to do with each quadrant.' },
      { icon: 'PieChart', num: '12', title: "Menu Engineering II: What the Classic Matrix Can't See", desc: 'Miller, Pavesic with weighted margin and the Goal Value of Hayes & Huffman with its full formula. Three readings the 2×2 matrix does not give you.' },
      { icon: 'Shuffle', num: '13', title: 'When the Methods Disagree: The Decision Protocol', desc: 'What each method really measures, how to read the comparison sheet, and the decision tree: rework, reprice, redesign or remove.' },
      { icon: 'UtensilsCrossed', num: '14', title: 'Short Menus, Prix Fixe, Buffets and Banquets', desc: 'Menu size and pruning; on a prix fixe the mix decides the margin. With its own section for hotel, buffet, banquet and catering.' },
      { icon: 'Truck', num: '15', title: 'Multichannel: Dine-In, Takeout and Third-Party Delivery', desc: 'Platform commission, packaging per order, tax by channel and the price ceiling. How much to raise in each channel and which dishes should not be on the app.' },
      { icon: 'Wine', num: '16', title: 'Beverage Cost: The Bar as a P&L of Its Own', desc: 'Glass versus bottle, draft, spirits and cocktails. Targets by category and tax by channel: the bar has its own numbers.' },
      { icon: 'Croissant', num: '17', title: 'Batch Costing for Commissary Kitchens and Pastry', desc: 'Batch yield, labor per hour, packaging and scaling. The full method, and why the portion is not the unit.' },
      { icon: 'RefreshCw', num: '18', title: 'When Your Supplier Raises Prices: The Re-Costing Protocol', desc: 'Triggers and review calendar, where to look for prices and how to raise yours without losing the guest.' },
      { icon: 'ClipboardList', num: '19', title: 'The Full Case: One Entire Menu, Start to Finish', desc: "The pack's example menu walked through cost card, matrix, pricing, multichannel and the 90-day plan. Labeled as a modeled case." },
      { icon: 'Cpu', num: '20', title: 'When Your Spreadsheet Falls Short', desc: 'The criteria for jumping from the spreadsheet to software, and from software to AI agents, with what each jump gains and what it costs.' },
    ],
  },

  // Sin una sola venta en inglés y sin testimonios en el ES: la plantilla oculta la sección y, fuera del ES,
  // también la prueba social del hero.
  testimonials: {
    titleGold: '',
    subtitle: '',
    items: [],
  },

  why: {
    titlePre: 'Why This ',
    titleGold: 'Guide',
    reasons: [
      { icon: 'Scale', title: 'Sales Tax, VAT and GST Inside the Math', desc: 'Food cost is calculated on net sales, and the tax changes by country and channel: added on the bill in the US and Canada, included in the printed price in the UK and Australia, different for dine-in, takeout and delivery. Here it lives in editable cells, not hidden inside a formula.' },
      { icon: 'Shuffle', title: 'Four Methods, Not One', desc: "Kasavana & Smith, Miller, Pavesic and Goal Value on the same menu, with a sheet that shows where they disagree and why. Each method measures two of three variables: the interesting part isn't when they agree, it's when they don't." },
      { icon: 'FileSpreadsheet', title: 'Eight Excel Tools With Live Formulas', desc: 'Not PDFs to fill in by hand: you enter your numbers and they calculate. Compatible with Excel, Google Sheets and Numbers, in US units, with tax rates, commissions and targets in editable cells so they also work in the UK, Canada and Australia.' },
      { icon: 'Wallet', title: 'Pay Once Instead of a Monthly Fee', desc: 'Recipe-costing software is a subscription you pay every year, per location. This guide is a one-time payment with lifetime access, and its last chapter shows when the jump to software is actually worth it.' },
    ],
  },

  author: {
    bio: 'CEO of AI Chef Pro and founder of ChefBusiness Group. In kitchens since the age of 17 and a restaurant consultant since 2010. He has advised on the opening of more than 200 venues, including Michelin-starred restaurants and Repsol Sun winners in Spain and Europe.',
    badge3: '200+ openings',
  },

  bonus: {
    subtitle:
      'On top of the PDF + DOCX guide, you get 8 Excel tools with live formulas and two bonuses: the solved exercises and the US · UK · Canada · Australia Equivalents Guide',
    layout: 'single',
    items: [
      { icon: 'FileSpreadsheet', label: 'TOOL 1', title: 'Recipe Cost Card', value: 'Included in the pack', desc: 'Ingredient lines with trim loss, the as-purchased quantity calculated for you, plate cost and target menu price before and with tax, plus an "Invoice & Tax Check" sheet. The starting point for everything else.', image: '/lovable-uploads/ai-gallery/guia-foodcost-hero.jpg' },
      { icon: 'Scale', label: 'TOOL 2', title: 'Yield and Trim Loss', value: 'Included in the pack', desc: 'A yield test with usable byproducts, a cooking loss test and your own trim loss table of measured values next to the reference ones, with the net cost per clean pound.', image: '/lovable-uploads/ai-gallery/guia-foodcost-cocina.jpg' },
      { icon: 'Calculator', label: 'TOOL 3', title: 'Menu Pricing Calculator', value: 'Included in the pack', desc: 'Twenty example dishes priced with the four methods side by side, the price kept by the method you choose and a traffic light on the resulting food cost.', image: '/lovable-uploads/ai-gallery/guia-foodcost-carta.jpg' },
      { icon: 'PieChart', label: 'TOOL 4', title: 'Menu Engineering Matrix', value: 'Included in the pack', desc: 'Up to 25 dishes classified by Kasavana & Smith, Miller, Pavesic and Goal Value, with a comparison sheet that flags where they disagree and what to do, plus a prix fixe menu sheet.', image: '/lovable-uploads/ai-gallery/guia-foodcost-carta.jpg' },
      { icon: 'Truck', label: 'TOOL 5', title: 'Multichannel Repricing Simulator', value: 'Included in the pack', desc: "Effective food cost by channel with commission and packaging, the price you need to hit your target and a flag when that price won't fit under the ceiling your market accepts.", image: '/lovable-uploads/ai-gallery/guia-foodcost-delivery.jpg' },
      { icon: 'Wine', label: 'TOOL 6', title: 'Beverage Menu and Beverage Cost', value: 'Included in the pack', desc: 'Wine by the glass and by the bottle, draft and bottled beer, soft drinks, spirits and cocktails with their ingredients. Cost, margin and weighted beverage cost by category.', image: '/lovable-uploads/ai-gallery/guia-foodcost-bodega.jpg' },
      { icon: 'Target', label: 'TOOL 7', title: 'Prime Cost Dashboard', value: 'Included in the pack', desc: 'Twelve months of food cost and labor cost with employer payroll taxes and benefits, monthly prime cost, a traffic light against your target and a trend chart.', image: '/lovable-uploads/ai-gallery/guia-foodcost-equipo.jpg' },
      { icon: 'CalendarRange', label: 'TOOL 8', title: '90-Day Action Plan', value: 'Included in the pack', desc: 'Decisions with an owner, a date and an estimated impact, a 13-week calendar and tracking KPIs compared with month 0.', image: '/lovable-uploads/ai-gallery/guia-foodcost-equipo.jpg' },
      { icon: 'GraduationCap', label: 'BONUS 1', title: '12 Solved Food Cost and Menu Engineering Exercises', value: 'Included in the pack', desc: 'Twelve cases with the problem, the data, a step-by-step solution, a table and what the result means: trim loss, tax by channel, the four pricing methods, disagreements between matrices, delivery, glass versus bottle and prime cost.', image: '/lovable-uploads/ai-gallery/guia-foodcost-hero.jpg' },
      { icon: 'Globe', label: 'BONUS 2', title: 'US · UK · Canada · Australia Equivalents Guide', value: 'Included in the pack', desc: 'Bonus: terms, taxes, food safety, staff rules, alcohol and units for using this guide in the US, UK, Canada and Australia.', image: '/lovable-uploads/ai-gallery/en-equivalents-guide.jpg' },
    ],
  },

  buyBox: {
    ctaLabel: 'YES, I WANT THE GUIDE — $59',
  },

  guarantee: {
    text: "If the guide doesn't help you price your menu and decide each dish with confidence, we'll refund 100% of your money. No questions, no hassle. You have 30 days to decide.",
  },

  faqs: FAQS,

  cta: {
    heading: 'Stop Pricing Your Menu by Gut Feel',
    subtitle: 'The method, the tools and the exercises to decide your menu with the numbers in front of you.',
    items: [
      'Complete guide in PDF + DOCX (20 chapters, 95 pages)',
      '8 Excel tools with live formulas',
      'Four menu engineering methods and the sheet that shows where they disagree',
      'Dine-in, takeout and third-party delivery simulator with tax and commissions',
      'Prime cost dashboard and a 90-day action plan',
      'Bonus: 12 solved exercises (32 pages)',
      'BONUS: US · UK · Canada · Australia Equivalents Guide',
    ],
    ctaLabel: 'YES, I WANT THE GUIDE — $59',
  },

  stickyLabel: 'FOOD COST + MENU ENGINEERING GUIDE — $59',

  footerLinks: [
    { label: 'aichef.pro', href: '/en' },
    { label: 'Digital Products', href: '/en/digital-products' },
    { label: 'Food Cost Kit Pro', href: '/en/digital-products/food-cost-templates' },
    { label: 'Restaurant Staff Scheduling Kit Pro', href: '/en/digital-products/restaurant-schedule-templates' },
    { label: 'Restaurant Inventory Kit Pro', href: '/en/digital-products/restaurant-inventory-templates' },
    { label: 'Restaurant Financial Plan Kit Pro', href: '/en/digital-products/restaurant-financial-plan-templates' },
    { label: 'Restaurant Business Plan Kit', href: '/en/digital-products/restaurant-business-plan' },
    { label: 'How to Open a Pastry Shop', href: '/en/digital-products/how-to-open-a-pastry-shop' },
    { label: 'Food Cost Calculator for Restaurants', href: '/en/food-cost-calculator-restaurant' },
    { label: 'Contact', href: 'mailto:info@aichef.pro' },
  ],

  updateNote: 'Version 1.0 · October 2026',

  alreadyBought: {
    product: 'food-cost-menu-engineering-guide',
    label: 'Already bought the guide? Get back into your dashboard',
  },

  schema: {
    productName: 'Food Cost + Menu Engineering Guide',
    productDescription:
      'A 20-chapter guide to cost recipes, price your menu and decide what to do with each dish in a restaurant that is already open: sales tax, VAT and GST by channel, measured trim loss, four menu engineering methods, third-party delivery, beverage cost and prime cost. Includes 8 Excel tools with live formulas and 12 solved exercises.',
    price: '59.00',
    priceValidUntil: '2026-12-31',
    faqs: FAQS,
    breadcrumb: [
      { name: 'AI Chef Pro', item: 'https://aichef.pro/en' },
      { name: 'Digital Products', item: 'https://aichef.pro/en/digital-products' },
      { name: 'Food Cost + Menu Engineering Guide', item: 'https://aichef.pro/en/digital-products/food-cost-menu-engineering-guide' },
    ],
  },
};

export default data;
