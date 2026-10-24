// astro-site/src/data/productos-en/planes/bbq-catering-business-plan.ts
// TIENDA INTERNACIONAL EN — BBQ Catering Business Plan Kit. DUPLICADO de mobile-bar-business-plan.ts (molde exacto: mismo
// tipo PlanNegocioData, misma plantilla PlanNegocioLandingPage con lang="en", mismo orden de campos) y del contenido de
// comida de catering-business-plan.ts, con el copy del BBQ caterer. Edición inglesa del ES astro-site/src/data/productos/
// planes/plan-negocio-parrillero-asador-eventos.ts (hreflang recíproco), cuyo contenido y cifras NO se reutilizan: el EN es
// otro concepto (SPEC D99).
// SPEC: scripts/productos-digitales/business-plans-en-6/SPEC-delta.md (§0 jerga, D96-D113) + las heredadas
//   business-plans-en-5 (D81-D95), -4 (D66-D80), -3 (D48-D65), -2 (D30-D47) y business-plans-en/SPEC.md (D1-D29).
//   · §0 / D96b: jerga US en las 3 capas (research §9). Title con el NOMBRE DEL PRODUCTO primero; H1 Forma B
//     `BBQ Catering ` + oro `Business Plan` + «Template for an Off-Site Barbecue Caterer with a Smoker Trailer: …»; meta
//     que abre con «BBQ business plan»; FAQ en la redacción del comprador (las 9 de research §9, incluidas «Can I sell
//     BBQ from my home without a license?» y «Is this plan for a BBQ food truck or restaurant?») y keywords de research
//     §9. «pitmaster» para la persona (nunca «grill master»), «BBQ caterer» para el negocio, «smoked meats»,
//     «commissary» (nunca «support kitchen»), «live pit on site» = extra de pago, «insulated food carriers / hot boxes»
//     (sin la marca Cambro), W-2 (nunca «freelance»). Sin «La Caja China» (marca) ni «lechón» (tilde): «whole hog /
//     pig roast». Los 6 H2 de research §9 NO caben como H2 (constantes de UI_PLAN, como en el mobile bar): sus keywords
//     van en las tarjetas (H3), las razones (H3), el subtítulo del grid y la FAQ.
//   · Canibalización con el Catering Business Plan Kit (D112): la landing diferencia por smoke, pitmaster, smoker trailer
//     y libras por invitado; FAQ «Should I buy this or the Catering Business Plan Kit?».
//   · D97: $39 SIN anclas (sin priceOld, «-x %», «Total value», «Save $», «launch price» ni valor de los bonos).
//   · D98: los 4 ficheros de dl/bbq-catering-business-plan/, dashboard BbqCateringBusinessPlanDashboard.tsx y
//     get-download-urls.ts (mismas claves que el ES y que el mobile bar) + la guía de equivalencias EN.
//   · Bonos sin precio y SOLO lo que existe en los ficheros: 1 = §9 del plan + fase 2 del checklist («Pits, Fire &
//     Permits»); 2 = tabla «US BBQ CATERING BENCHMARKS (sourced) AND KIT ESTIMATES» (D104) + los 5 umbrales del P&L;
//     3 = guía de equivalencias EN. Sin aggregateRating ni review.
//   · Legal (research §6, sin inventar): sin cocina de casa (Food Code 3-201.11(B); cottage food de TX excluye la carne),
//     commissary con acuerdo escrito, trailer que cocina en el evento = mobile food unit según el condado (TX 25 TAC
//     §228.221) → «ask your county», fuego → fire marshal (Class K, distancias, propano, burn bans) sin cifras de una
//     sola ciudad, temperaturas del Food Code en °F separadas de la de calidad (≈ 203 °F del brisket).
//   · FAQ «Does it work in the UK, Canada or Australia?» (estilo del mobile bar): VAT/GST editables en Assumptions,
//     lb con (kg) y °F con (°C) por REGLA_UNIDADES (D0), millas en la calculadora, nota UK del docx §9 (registro 28 días
//     antes, FHRS, 14 alérgenos, VAT 20 %, plan de fuego con council y recinto). ⚠️ Comprobar contra los ficheros F2.
//   · Testimonios (D26, como los otros planes EN): los 8 del ES (src/data/testimonials-plan-parrillero-asador-eventos)
//     traducidos con el subtítulo de la edición española y SIN ningún dato que no sea verdad en este kit: fuera «18
//     cortes», «manual de salmueras», «marco legal CCAA», «modelo(s) de contrato», «roadmap del food truck», «93
//     proveedores», la marca «Tienda Biomasa», «freelance», «Don» y todas las cifras (12 años, 30.000 EUR, 6 meses,
//     100.000 EUR, 10 minutos). Nombres con tilde en EXENTOS de tienda-gate.py.
//   · Imágenes: del ES del parrillero solo valen -2 (offset smoker en un evento: el hero), -6 (evento al aire libre) y
//     -hero (parrilla argentina = línea live-fire premium, nunca de hero). Fuera -1 («ASADOR»), -3 (restaurante), -4
//     («QUEBRACHO CHARCOAL MADRID 2026») y -5 («ASADO MADRID», food truck). Las 3 bbq-catering-*.jpg las GENERA EL
//     ORQUESTADOR con generate-images (F3-NOTAS §4): deben existir en public/lovable-uploads/ai-gallery/ antes del merge.
//     OG = recorte 1200×630 de bbq-catering-smoker-trailer-wedding.jpg (generada el 24-oct con generate-images).
// DINERO: stripeEnvKey = VITE_STRIPE_PAYMENT_LINK_BBQ_CATERING_BUSINESS_PLAN (resuelto en el wrapper .astro; sin la env
// var el CTA cae a '#comprar' hasta que John cree el Payment Link).
import type { PlanNegocioData, PlanNegocioFaq } from '../../productos/planes/types';

// ── Cifras del caso US — confirmado con F2-NOTAS §8 (24-oct) (business-plans-en-6/F2-NOTAS.md §8 y cifras_caso.json) ────────────
// La F2 no había cerrado el caso al escribir esta ficha (24-oct): son los valores de research §8 / SPEC D100 (B4 150 ·
// B6 75 · B5 $38, CAPEX ≈ $83,300 con la contingencia de D102, préstamo semilla $98,000 sin calibrar). Se sustituyen
// AQUÍ, en un solo sitio, por los de cifras_caso.json; si la calibración D15 sube B4, cambian eventos, ventas, neto,
// equilibrio, necesidad y préstamo. Los ejemplos salen de «3 Example Quotes» de la calculadora (±10 % de $22/$35/$52).
const CASO = {
  eventos: '150', // B4 — confirmado con F2-NOTAS §8 (24-oct)
  invitados: '75', // B6 — confirmado con F2-NOTAS §8 (24-oct)
  precio: '$38.00', // B5 — confirmado con F2-NOTAS §8 (24-oct)
  ventas: '$427,500', // ventas_a1 = B4 × B5 × B6 — confirmado con F2-NOTAS §8 (24-oct)
  inversion: '$83,300', // total de Startup Costs (contingencia 10 % × filas 7, 8, 11, 12 y 15 = $4,500) — confirmado con F2-NOTAS §8 (24-oct)
  circulante: '$52,371', // necesidad − inversión — confirmado con F2-NOTAS §8 (24-oct)
  necesidad: '$135,671', // total cash needed — confirmado con F2-NOTAS §8 (24-oct)
  propios: '$35,000', // B30 — confirmado con F2-NOTAS §8 (24-oct)
  prestamo: '$101,000', // B31 (CALIBRAR, regla D85) — confirmado con F2-NOTAS §8 (24-oct)
  neto: '$29,816', // beneficio neto año 1 — confirmado con F2-NOTAS §8 (24-oct)
  netoPct: '7.0%', // — confirmado con F2-NOTAS §8 (24-oct)
  equilibrio: '128', // eventos/año de equilibrio — confirmado con F2-NOTAS §8 (24-oct)
  dscr: '2.43×', // DSCR mínimo — confirmado con F2-NOTAS §8 (24-oct)
  marketing: '$10,000', // fijo de marketing (research §8) — confirmado con F2-NOTAS §8 (24-oct)
  seguros: '$6,000', // B27 — confirmado con F2-NOTAS §8 (24-oct)
  pesEventos: '113', // Scenarios pesimista — confirmado con F2-NOTAS §8 (24-oct)
  pesPrecio: '$34.20', // — confirmado con F2-NOTAS §8 (24-oct)
  pesInvitados: '68', // — confirmado con F2-NOTAS §8 (24-oct)
  ejDropoff: '$22.50', // «3 Example Quotes»: corporate drop-off 40 inv. — confirmado con F2-NOTAS §8 (24-oct)
  ejGraduacion: '$34.50', // graduation party staffed buffet 70 inv. — confirmado con F2-NOTAS §8 (24-oct)
  ejBoda: '$54.00', // wedding 130 inv. full-service + live pit on site — confirmado con F2-NOTAS §8 (24-oct)
  livePit: '$650', // fee por defecto del live pit on site (D105) — confirmado con F2-NOTAS §8 (24-oct)
  cortes: '13', // cortes de «Meat Yield & Smoke Schedule» (D106) — confirmado con F2-NOTAS §8 (24-oct)
  menuStyles: '10', // menu styles del docx §2 (D99) — confirmado con F2-NOTAS §8 (24-oct)
  formulas: '700', // «more than N» fórmulas del libro (el del catering pasa de 700) — confirmado con F2-NOTAS §8 (24-oct)
};

// FAQ on-page Y FAQPage (un solo array: lo que ve el visitante es lo que declara el schema).
const FAQS: PlanNegocioFaq[] = [
  {
    q: 'What should a BBQ catering business plan include?',
    a: 'The sections lenders and investors expect: executive summary, concept and value proposition, market analysis, competitive analysis, marketing plan, operations plan, management and staffing, financial plan, legal requirements and permits, and conclusions with an action plan. This kit gives you those 10 sections already written in Word for an off-site BBQ caterer, plus the Excel financial projections that back them up, a pricing calculator that turns pounds of meat per guest into a quote, with a smoke schedule and a shopping list, and a 68-task startup checklist.',
  },
  {
    q: 'Is it a generic template or built for BBQ catering?',
    a: 'Built for a full-service, off-site BBQ caterer: the pitmaster smokes brisket, pulled pork, ribs, chicken and sausage in the commissary yard, holds them hot in insulated food carriers and hot boxes, and serves a staffed buffet with a carving station. The smoker trailer goes to the event for weddings and premium jobs, as a paid "live pit on site" add-on; corporate drop-off lunches fill the weekdays, and a live-fire premium line covers Argentine asado, Santa Maria tri-tip and whole hog. Event staff on W-2 payroll, a used cargo van and no alcohol sales of its own. Nothing to strip out from a restaurant template.',
  },
  {
    q: 'How much does it cost to start a BBQ catering business?',
    a: `It depends mostly on the smoker and the van. A lean start — a used smoker, holding gear and drop-off only — can come in around $25,000 to $35,000 (a kit estimate). The kit's example buys new: ${CASO.inversion} in startup costs plus ${CASO.circulante} of working capital, for ${CASO.necesidad} in total cash needed. The Startup Costs sheet lists every line — a new 500-gallon-class smoker trailer ($20,000) and its upfit, a live-fire rig, commissary storage, a used cargo van ($18,000) and its upfit, LLC and legal, first-year permits and certifications, plan review or trailer inspection, catering software, smallwares and pit tools, opening inventory, website, launch and a first bridal show, and holding and service equipment — plus the commissary deposit, rent before opening and a contingency. Your own pickup tows the trailer; if you need one, a used pickup rated to tow at least 5,000 lb (2,270 kg), checked against the loaded trailer weight, is a kit estimate of $25,000 to $40,000. Replace each line with your own quotes.`,
  },
  {
    q: 'How profitable is a BBQ business?',
    a: `It can be, but margins are thin: ItsaCheckmate reports an average net margin of 7-8% for caterers, and Galley Solutions puts food cost at 28-35% of the menu price. In the kit's example — ${CASO.eventos} events a year with ${CASO.invitados} guests at ${CASO.precio} per guest (excl. sales tax; staffing and service charge included) — year-1 sales are ${CASO.ventas} and net income is ${CASO.neto} (${CASO.netoPct}), after paying the owner as pitmaster, with a break-even of ${CASO.equilibrio} events a year. That's a full-time operator with a pit cook and a ${CASO.marketing} marketing budget, not a typical first year. In the pessimistic scenario — ${CASO.pesEventos} events at ${CASO.pesPrecio} per guest and ${CASO.pesInvitados} guests — the cash runs out in year 1, and the plan says so. Build your first year on your own bookings, not on the example.`,
  },
  {
    q: 'How to charge for catering BBQ?',
    a: `Per guest, by package, starting from your costs. The pricing calculator multiplies your guests by the ounces of cooked meat per guest, splits them by your meat mix, turns them into raw pounds with each cut's yield and prices them at the raw cost per pound you type (it ships blank, so there are no invented meat prices); then it adds sides, bread and sauces, disposables, wood, pitmasters and servers with payroll taxes, rentals and mileage, applies your target margin and shows the price per guest and its all-in equivalent per pound of cooked meat. On top go the event fee, the live pit on site fee (a flat ${CASO.livePit} by default), the service charge, the sales tax and a 50% nonrefundable deposit. As a market reference, published BBQ catering prices run from about $15-$30 per person for drop-off to $25-$50 for a staffed buffet and $40-$75 or more for full service (kit estimate). The calculator's three example quotes: a corporate drop-off for 40 guests at about ${CASO.ejDropoff} per guest, a graduation party buffet for 70 at about ${CASO.ejGraduacion} and a wedding for 130 with the pit on site at about ${CASO.ejBoda}.`,
  },
  {
    q: 'How much barbecue per person for catering?',
    a: `BBQ caterers usually plan one-third to one-half pound of cooked meat per guest; the kit uses 6 oz (170 g) for drop-off and 8 oz (227 g) for a full-service buffet or live-fire, and you can change both. Smoking shrinks the meat: brisket and pork butt yield about 50% of their raw weight, so half a pound cooked is about a pound raw. The Meat Yield & Smoke Schedule holds the yield, pit temperature, cook, rest and hold time of ${CASO.cortes} cuts, and the Shopping List by Guest Count turns your guest count — and 40, 80, 150 and 300 guests — into raw pounds per cut, packers, butts and racks, sides, rolls, sauce and wood.`,
  },
  {
    q: 'Can I sell BBQ from my home without a license?',
    a: "No. Under the FDA Food Code, which most states adopt, food prepared in a private home can't be used in a food business (section 3-201.11), and cottage food laws, which let you sell some shelf-stable foods made at home, leave meat out — Texas, for example, excludes meat, meat products and poultry. To cater BBQ you need a permitted kitchen: your own licensed commercial kitchen or a commissary under a written agreement, plus the permits of your county health department. That's why the plan smokes at a commissary and why the commissary agreement is one of the first tasks in the checklist. Rules vary by state and county, so check with your local health department before you spend.",
  },
  {
    q: 'Do I need a commissary kitchen for BBQ catering?',
    a: "In most places, yes. Caterers prepare food in a permitted facility, and a shared commissary under a written agreement is the usual route when you don't own a kitchen; the example smokes in the commissary yard and rents prep time and trailer parking there. If your smoker trailer cooks at the event, your county may treat it as a mobile food unit tied to a central preparation facility — Texas rules say so — with its own permit, hand sink and water; ask your county before you sell a live pit on site, and if it isn't permitted, smoke at the commissary and hold hot. The fire marshal may have a say too: a Class K extinguisher next to a wood or charcoal pit, clearances from tents and other vendors, propane limits and burn bans. Check with your county health department and your fire marshal.",
  },
  {
    q: 'What smoker do I need to start a BBQ catering business?',
    a: 'For catering volume, most operators use an offset (stick burner) or reverse-flow smoker, or a pellet smoker, built on a trailer in the 250- to 500-gallon class. New smoker trailers from US makers list at roughly $8,500 to $20,400 before shipping. The kit\'s example budgets a new 500-gallon-class offset or reverse-flow smoker trailer at $20,000 plus $3,500 of upfit (warming cabinet, storage boxes, lights, and a hand sink and water tanks if your county requires them), and a $4,500 live-fire rig for the premium line: a Santa Maria grill, an Argentine parrilla and asado crosses. Check what your fire marshal and your county require before you buy.',
  },
  {
    q: 'What are the four types of BBQ?',
    a: `The four classic American styles are Texas (beef brisket with salt and pepper over post oak), Kansas City (a sweet tomato-and-molasses sauce and burnt ends), Memphis (dry-rubbed pork ribs) and Carolina (whole hog or pulled pork with a vinegar or mustard sauce). The plan builds its menu on ${CASO.menuStyles} styles: those four plus Santa Maria tri-tip, Argentine asado, Brazilian churrasco, a pig roast, a live-fire "fire show" with tomahawk steaks and a corporate boxed lunch, so you can sell what your market asks for.`,
  },
  {
    q: 'What food safety rules apply to smoked meats?',
    a: "The FDA Food Code minimums, which the kit keeps apart from quality targets: 145 °F for 15 seconds for intact cuts; 155 °F for 17 seconds for ground meat, sausage and meat that has been injected or tenderized (an injected brisket or pork butt counts); 165 °F for poultry; hot holding at 135 °F or above; cooling from 135 °F to 70 °F within 2 hours and to 41 °F within a total of 6 hours; and reheating to 165 °F. A brisket pulled at around 203 °F is a quality target, not a safety rule, and the Meat Yield & Smoke Schedule shows the two in separate columns. Meat has to come from USDA- or state-inspected sources: custom-exempt meat, whole hogs included, can't be sold.",
  },
  {
    q: 'What insurance do I need for BBQ catering?',
    a: `Usually general liability (venues often ask for a certificate of insurance naming them as additional insured), commercial auto that covers the van and the smoker trailer you tow, workers' compensation once you hire, and inland marine coverage for the smoker and your gear on the road; liquor liability only if your staff serve the client's alcohol. Insureon puts a small caterer at about $45 a month for general liability, $96 for a business owner's policy, $82 for workers' comp and $204 for commercial auto. The example budgets ${CASO.seguros} a year for insurance; ask an agent who insures caterers for your own quotes.`,
  },
  {
    q: 'Should I buy this or the Catering Business Plan Kit?',
    a: "Buy this one if smoke is your product: a pitmaster, a smoker trailer, an overnight cook, pounds of meat per guest, smoker yield and the fire rules around a wood or charcoal pit. The Catering Business Plan Kit is written for a general event caterer — plated service, chef-attended stations and a refrigerated van — and its calculator works from food cost per guest. Both share the same lender-ready format and the same Excel engine, driven by events per year, price per guest and guests per event.",
  },
  {
    q: 'Is there a plan for a paella caterer?',
    a: "Yes. If you'd rather cook giant paellas live in front of the guests than smoke meats, our Paella Catering Business Plan Kit is written for that: paella pans and 3-ring propane burners at the event, sofrito, stock and seafood prepped at a commissary, cooked rice as a TCS food, propane rules and a pricing calculator that turns your guest count into pans, rice and a price per guest, with a pan sizing table and a shopping list by guest count.",
  },
  {
    q: 'Is this plan for a BBQ food truck or restaurant?',
    a: "No. It's built for an off-site BBQ caterer with no storefront, which sells events, not plates to walk-up customers. If you're opening a BBQ food truck, our Food Truck Business Plan Kit fits better; for a BBQ restaurant, start from the Restaurant Business Plan Kit. The Excel workbook takes any numbers you type, but the written plan describes a BBQ catering company, so you'd rewrite more of the text.",
  },
  {
    q: 'Can I present this plan to a lender or investors?',
    a: `Yes. It follows the format lenders usually ask for: a written plan, a 3-year P&L, break-even, three scenarios, a 12-month cash flow, sources and uses of funds and a loan schedule with the debt service coverage ratio (DSCR), checked against 1.25×, a common lender target. The loan schedule and the DSCR cover your main loan, the one you enter in the assumptions; the financing sheet also lists an SBA Microloan, investors or partners and local grants as sources of funds, without amortizing them. In the example, the owner puts in ${CASO.propios} and borrows ${CASO.prestamo} at 10% over 7 years — more than the SBA Microloan cap of $50,000, so it's a bank or SBA 7(a) loan — with a minimum DSCR of about ${CASO.dscr}. It's a lender-ready format, not a guarantee of approval, and a planning tool, not financial, tax or legal advice.`,
  },
  {
    q: 'Can I change the numbers in the Excel model?',
    a: `Yes. The green cells are the ones you type — events per year, price per guest, guests per event, the split between BBQ packages and add-ons, meat and disposables cost, the corporate marketplace share, commissary rent, wages and any startup cost line — and more than ${CASO.formulas} linked formulas recalculate the rest. The 50% client deposit isn't modeled, which keeps the cash flow on the cautious side. To change a calculated cell, use Review → Unprotect Sheet (there is no password). The workbook and the calculator each include an Instructions tab.`,
  },
  {
    q: 'Does it work in the UK, Canada or Australia?',
    a: "Yes, with UK notes. Tax rates and wages are editable cells: enter 20% VAT, Canadian GST/HST plus any PST, or 10% Australian GST, the tax you reclaim on purchases, and your own minimum wage and employer costs. UK and Australian prices include tax, so type your price per guest without it. The calculator works in pounds, ounces and gallons (1 lb = 0.454 kg; 1 gallon = 3.8 liters), shows every temperature in °F with °C alongside, and counts miles, so type kilometers and your cost per km instead. The plan's UK notes cover registering with your council at least 28 days before trading, the food hygiene rating, the 14 allergens, 20% VAT on event catering and agreeing a fire plan with the council and the venue. In Canada and Australia, check your provincial or state food premises and fire rules with your local authority before you sell a live pit on site. Every English edition also includes the US · UK · Canada · Australia Equivalents Guide, a bonus with the local terms, taxes, food safety and staff rules side by side.",
  },
  {
    q: 'What currency will I pay in?',
    a: 'The price is $39 USD, a one-time payment. At checkout, Stripe can show the amount in your local currency (for example GBP, EUR, CAD or AUD) and converts it for you. The Excel cells have no currency symbol, so you type amounts in your own currency; the example in the Word plan is in US dollars.',
  },
  {
    q: 'Is it a subscription? Are future updates included?',
    a: 'No subscription: you pay once and get lifetime access to the online dashboard. When we improve the plan or the workbooks, you get the new version at no extra cost — just download the files again.',
  },
  {
    q: 'Can I use it with my clients or for more than one business?',
    a: "One purchase covers one business, however many events it caters. If you're a consultant or an investor, you can use the files with the projects you advise, but you can't hand them copies: each business buys its own.",
  },
  {
    q: 'Is there a money-back guarantee?',
    a: "Yes. A full 30-day guarantee. If the plan doesn't meet your expectations, we'll refund 100% with no questions asked.",
  },
];

const data: PlanNegocioData = {
  slug: 'bbq-catering-business-plan',
  stripeEnvKey: 'VITE_STRIPE_PAYMENT_LINK_BBQ_CATERING_BUSINESS_PLAN',

  seo: {
    title: 'BBQ Catering Business Plan Kit: Word Template + Excel Financial Projections + Pricing Calculator | AI Chef Pro',
    description:
      'BBQ business plan template for a smoked-meat catering company: Word plan, 3-year Excel projections, per-guest pricing calculator and startup checklist.',
    keywords:
      'bbq catering business plan, bbq business plan, bbq business plan template, barbecue catering business plan, how to start a bbq catering business, bbq catering prices, smoker trailer, AI Chef Pro',
    ogImage: 'https://aichef.pro/og-bbq-catering-business-plan.jpg',
  },

  schema: {
    productName: 'BBQ Catering Business Plan Kit',
    productDescription:
      'BBQ catering business plan template kit for an off-site barbecue caterer with a smoker trailer: a 10-section business plan in Word, an Excel financial model with 9 sheets (assumptions, startup costs, 3-year P&L, break-even, scenarios, staffing, 12-month cash flow, financing with a loan schedule and DSCR, and instructions), a pricing calculator from pounds of meat per guest to quote with a meat yield and smoke schedule and a shopping list by guest count, and a 68-task startup checklist in 6 phases. Set up for the US, with notes for the UK.',
    price: '39.00',
    priceValidUntil: '2026-12-31',
    faqs: FAQS,
    breadcrumbName: 'BBQ Catering Business Plan Kit',
  },

  images: {
    // hero bg (6) — el offset smoker en un evento (ES -2) abre; las 3 bbq-catering-* las genera el orquestador
    // (F3-NOTAS §4); -6 (evento al aire libre) y el hero ES (parrilla argentina = línea live-fire premium) cierran.
    gallery: [
      '/lovable-uploads/ai-gallery/plan-parrillero-asador-eventos-2.jpg',
      '/lovable-uploads/ai-gallery/bbq-catering-smoker-trailer-wedding.jpg',
      '/lovable-uploads/ai-gallery/bbq-catering-brisket-carving-station.jpg',
      '/lovable-uploads/ai-gallery/bbq-catering-drop-off-corporate.jpg',
      '/lovable-uploads/ai-gallery/plan-parrillero-asador-eventos-6.jpg',
      '/lovable-uploads/ai-gallery/plan-parrillero-asador-eventos-hero.jpg',
    ],
    // strip del ContentGrid (6): el mismo set en otro orden, como el mobile bar.
    gridGallery: [
      '/lovable-uploads/ai-gallery/bbq-catering-brisket-carving-station.jpg',
      '/lovable-uploads/ai-gallery/plan-parrillero-asador-eventos-6.jpg',
      '/lovable-uploads/ai-gallery/bbq-catering-drop-off-corporate.jpg',
      '/lovable-uploads/ai-gallery/plan-parrillero-asador-eventos-2.jpg',
      '/lovable-uploads/ai-gallery/plan-parrillero-asador-eventos-hero.jpg',
      '/lovable-uploads/ai-gallery/bbq-catering-smoker-trailer-wedding.jpg',
    ],
    whyBg: '/lovable-uploads/ai-gallery/plan-parrillero-asador-eventos-6.jpg',
    buyBoxBg: '/lovable-uploads/ai-gallery/plan-parrillero-asador-eventos-2.jpg',
    ctaBg: '/lovable-uploads/ai-gallery/plan-parrillero-asador-eventos-2.jpg',
  },

  hero: {
    badge: 'Lender-ready BBQ catering business plan: Word + Excel + pricing calculator',
    titlePre: 'BBQ Catering ',
    titleGold: 'Business Plan',
    titleSubtitle:
      'Template for an Off-Site Barbecue Caterer with a Smoker Trailer: Word Plan + Excel Financial Projections + Pricing Calculator + Startup Checklist',
    description:
      'Everything you need to plan, price and pitch an off-site BBQ catering company that smokes at a commissary and brings the pit to the event when the client pays for it: a 10-section business plan in Word, already written for the format lenders expect; an Excel model that recalculates your startup costs, 3-year P&L, break-even in events per year, 12-month cash flow and loan payments from your own numbers; a pricing calculator that turns pounds of meat per guest into a quote, with a smoke schedule and a shopping list; and a 68-task checklist that takes you from your LLC, your commissary agreement and the fire marshal to your first 90 days of events. Set up for the US, with notes for the UK.',
    checkItems: [
      '10-section BBQ catering business plan in Word, ready to edit',
      'Excel financial projections: 3-year P&L, break-even in events per year and 12-month cash flow',
      'Pricing calculator: pounds of meat per guest to quote, smoke schedule and shopping list',
      'Startup checklist: 68 tasks in 6 phases, from your LLC to your first 90 days',
      'Instant access + lifetime updates',
    ],
    ctaLabel: 'GET THE BUSINESS PLAN — $39',
  },

  compatSubtitle: 'Microsoft Excel and Word files, set up to print on US Letter paper',

  grid: {
    subtitle:
      "What's inside your BBQ Business Plan Kit for catering: 9 building blocks to test whether your BBQ catering business works on paper before you buy a smoker trailer, price every event by the pound and present the plan to a lender or an investor.",
    templates: [
      { icon: 'FileText', title: 'BBQ Catering Business Plan (Word, 10 Sections)', desc: `A complete plan already written for an off-site BBQ caterer that smokes in the commissary yard and holds hot in insulated carriers: executive summary, concept and value proposition with ${CASO.menuStyles} menu styles (Texas, Carolina, Kansas City, Memphis, Santa Maria, Argentine asado and more), market analysis, competitive analysis, marketing plan (The Knot, WeddingWire, Zola, ezCater, bridal shows and tastings), operations plan (the overnight cook, hot holding and the phases of an event), management and staffing, financial plan, legal requirements, permits and fire rules, and conclusions with an action plan. Its figures are the ones in the example Excel model.` },
      { icon: 'FileSpreadsheet', title: 'BBQ Catering Financial Projections (Excel, 9 Sheets)', desc: `Is a BBQ business profitable? Assumptions, startup costs, 3-year P&L, break-even, scenarios, staffing, 12-month cash flow, financing and instructions. More than ${CASO.formulas} linked formulas: change events per year, price per guest or guests per event and the whole workbook recalculates.` },
      { icon: 'Calculator', title: 'BBQ Catering Pricing Calculator (Pounds of Meat per Guest to Quote)', desc: 'BBQ catering prices from your own costs. Three packages — drop-off, full-service BBQ buffet with a carving station and live-fire premium — plus a live pit on site switch with its flat fee; guests and guest minimum, ounces of cooked meat per guest, your meat mix, the raw price per pound you pay (you type it), sides, bread and sauces, disposables, wood or charcoal, pitmasters and servers with wages and payroll taxes, rentals, mileage, event fee, target margin, service charge, sales tax, a 50% nonrefundable deposit and cancellation tiers. Out come raw pounds and pieces per cut and the total cooked pounds, the price per guest and its all-in equivalent per pound of cooked meat, the total, the deposit, the balance and the margin it really leaves. Three example quotes: a corporate drop-off, a graduation party buffet and a wedding with the pit on site.' },
      { icon: 'Thermometer', title: 'Meat Yield & Smoke Schedule + Shopping List by Guest Count', desc: `Your BBQ catering menu in pounds: ${CASO.cortes} cuts, from packer brisket and pork butt to ribs, chicken, sausage, tri-tip, picanha and whole hog, each with raw weight per piece, pit temperature in °F (°C), the quality target and the FDA Food Code minimum in separate columns, cook, rest and hold times, yield (brisket and pork butt about 50%) and a "start the pit by" time worked back from serving time. The shopping list scales your guest count — and 40, 80, 150 and 300 guests — into raw pounds per cut, packers, butts and racks, pans of sides, rolls, sauce, wood or charcoal, butcher paper and foil, hotel pans, hot boxes, pitmasters and servers.` },
      { icon: 'Coins', title: 'BBQ Catering Startup Costs, Line by Line', desc: 'How much does it cost to start a BBQ catering business? A new 500-gallon-class smoker trailer and its upfit (warming cabinet, storage boxes, and a hand sink and water tanks if your county requires them), a live-fire rig (Santa Maria grill, Argentine parrilla, asado crosses), commissary storage, a used cargo van and its upfit, LLC and legal, first-year permits and certifications, plan review or trailer inspection, catering software, smallwares and pit tools, opening inventory, website, launch and your first bridal show, and holding and service equipment — insulated carriers, hot boxes, chafing dishes and a carving board — each with a reference price you replace with your quotes, plus the commissary deposit, rent before opening, a contingency and working capital. Your own pickup tows the trailer.' },
      { icon: 'TrendingUp', title: 'Break-Even in Events per Year + 3 Scenarios', desc: 'How many events a year you need at your price per guest (excl. sales tax) and guest count to cover every cost, and the cash break-even with loan payments in and depreciation out, with a sensitivity table and a plain-English reading of the result. Plus pessimistic, base and optimistic scenarios side by side, each with its own estimated cash balance — honest about what a slow first year does to your cash.' },
      { icon: 'Users', title: 'Staffing & Event Labor (4 Roles)', desc: 'Owner / Pitmaster & Sales, a pit cook who watches the overnight cook, hourly W-2 event staff (servers, buffet attendants, carvers) and a part-time prep cook who drives the van, with gross pay, employer payroll taxes and the real cost of each role. The sheet checks the event hours you need (hours per event × people per event × events) against the hours you hire, and flags any pay below the minimum wage for the hours worked.' },
      { icon: 'ShieldCheck', title: 'Startup Checklist (68 Tasks, 6 Phases)', desc: "Business setup (LLC, EIN, seller's permit, business license, your catering contract with a 50% deposit and cancellation tiers, a HACCP-based food safety plan), pits, fire and permits (a written commissary agreement, your county on whether smoking at the event makes the trailer a mobile food unit, the fire marshal, the trailer at the DMV, commercial auto and inland marine), equipment, staff (W-2, never 1099; ServSafe Manager and food handler cards), marketing (The Knot, WeddingWire, Zola, ezCater, Thumbtack, Google Business Profile, bridal shows and a launch tasting) and your first 90 days." },
      { icon: 'Banknote', title: 'Financing Plan', desc: "Owner equity and your loan (bank or SBA 7(a)) with its amortization schedule and the debt service coverage ratio (DSCR) year by year against a 1.25× target, plus an SBA Microloan, investors or partners and local grants as other sources of funds, and a warning if your sources don't cover the cash you need." },
    ],
  },

  // Testimonios: traducción de los 8 del ES (D26), del Plan de Negocio Parrillero y Asador para Eventos, la edición
  // española. Sin ningún dato que no sea verdad en este kit (ver cabecera). Solo se pintan: NO alimentan el JSON-LD.
  testimonials: {
    subtitle:
      'Pitmasters and live-fire cooks who planned their event business with the Spanish edition of this plan',
    items: [
      { name: 'Mariano Rodríguez', role: 'Argentine asado pitmaster, Madrid, Spain', text: 'After years working for someone else at the grill, this plan gave me the roadmap to go out on my own. The menu styles and the pricing calculator are what I use most now.', avatar: '/avatars/avatar-1.jpg' },
      { name: 'Lucía Sanz', role: 'Live-fire cook for weddings, Barcelona, Spain', text: 'The smoke schedule and yield table alone is worth the whole plan. My weddings were more consistent from the very first season.', avatar: '/avatars/avatar-2.jpg' },
      { name: 'Tomás García', role: 'Spit-roast cook at a rural venue, Toledo, Spain', text: 'I thought I knew everything about lamb on the asado cross, but the legal section and the permits checklist put all the paperwork for my first wedding with a planner in order.', avatar: '/avatars/avatar-3.jpg' },
      { name: 'Diego López', role: 'BBQ pitmaster for corporate events, Madrid, Spain', text: 'Following the startup costs line by line kept my investment under control, and I started with corporate events sooner than I expected.', avatar: '/avatars/avatar-4.jpg' },
      { name: 'Andrés Camacho', role: 'Colombian live-fire cook, Madrid, Spain', text: 'It covers what no other plan did for me: Latin American live-fire asado next to smoked meats. A real difference at weddings with Latin American families.', avatar: '/avatars/avatar-5.jpg' },
      { name: 'Federico Aguirre', role: 'Uruguayan asado cook, Costa del Sol, Spain', text: 'The startup checklist saved me months: permits, insurance and equipment in order, so I knew what to do every week before my first event.', avatar: '/avatars/avatar-6.jpg' },
      { name: 'Marcos Pérez', role: 'Young BBQ catering entrepreneur, Valencia, Spain', text: 'I am in my second year, and the realistic financial plan is what anchors every decision I make.', avatar: '/avatars/avatar-7.jpg' },
      { name: 'Sandra Vera', role: 'Latin American grill cook for events, Bilbao, Spain', text: 'The pricing calculator is pure gold. I used to price each event by gut feeling; now I build the quote, see my margin and send it.', avatar: '/avatars/avatar-8.jpg' },
    ],
  },

  why: {
    subtitle:
      'Not another generic template: a BBQ catering plan written for the format lenders expect, with a financial model and a pricing calculator that recalculate from your own numbers.',
    reasons: [
      { icon: 'Flame', title: 'Built for an Off-Site BBQ Caterer', desc: 'A pitmaster who smokes in the commissary yard; brisket, pulled pork, ribs, chicken and sausage held hot in insulated carriers and hot boxes; a staffed buffet with a carving station; the smoker trailer at the event only when the client pays for a live pit on site; corporate drop-off on weekdays and a live-fire premium line (Argentine asado, Santa Maria tri-tip, whole hog). Nothing to strip out from a restaurant or a general catering template.' },
      { icon: 'ShieldCheck', title: 'Can You Start a BBQ Business From Home? The Legal Route', desc: "Food prepared in a private home can't be used under the FDA Food Code, and cottage food laws such as Texas's leave meat out. The plan works from a commissary under a written agreement, explains when a trailer that cooks at the event becomes a mobile food unit (ask your county) and what the fire marshal checks around a wood or charcoal pit, and keeps the Food Code temperatures for smoked meats apart from quality targets." },
      { icon: 'Calculator', title: 'BBQ Catering Prices per Guest, Drop-Off vs. Full-Service', desc: 'What to charge per person, drop-off vs. full-service: the calculator turns ounces of meat per guest, your meat mix and raw prices, yield, wood, staff hours and mileage into a price per guest and its all-in equivalent per pound of cooked meat, adds the live pit fee, the service charge, the sales tax and a 50% nonrefundable deposit, and shows the margin it leaves. Three example quotes: a corporate drop-off, a graduation party buffet and a wedding with the pit on site.' },
      { icon: 'BarChart3', title: 'Honest Numbers, Calculated', desc: `The example: ${CASO.eventos} events a year with ${CASO.invitados} guests at ${CASO.precio} per guest (excl. sales tax; staffing and service charge included), ${CASO.ventas} in year-1 sales and ${CASO.equilibrio} events a year to break even — a full-time operator with a pit cook and a marketing budget, not a typical first year. The pessimistic scenario runs out of cash, and the plan says so. Replace the numbers with yours.` },
    ],
    compatLabel: 'Works with:',
    compatPills: [
      { label: 'Microsoft Excel (.xlsx)', highlight: true },
      { label: 'Microsoft Word (.docx)' },
      { label: 'US Letter size' },
    ],
  },

  authorBio:
    'CEO of AI Chef Pro and founder of ChefBusiness Group. In kitchens since the age of 17 and a restaurant consultant since 2010, he has advised pitmasters, live-fire cooks and event caterers on launching and growing BBQ catering services, combining hands-on operations with financial planning.',
  // authorBadges omitido → default del diccionario EN ['Restaurant consultant since 2010', 'In professional kitchens since 17'].

  bonus: {
    subtitle:
      'Besides the business plan, the financial model, the pricing calculator and the startup checklist, you get these extra resources, drawn from the plan and the workbook themselves',
    items: [
      {
        icon: 'Map',
        label: 'BONUS 1',
        title: 'BBQ Catering Permits, Fire Rules & Food Safety Guide (US + UK Notes)',
        desc: "Section 9 of the plan plus Phase 2 of the checklist: why there's no legal way to sell BBQ from your home kitchen, the written commissary agreement, when a smoker trailer that cooks at the event becomes a mobile food unit, what the fire marshal checks (Class K extinguisher, clearances, propane, burn bans), the Food Code temperatures for smoked meats (an injected brisket is non-intact: 155 °F), cooling and reheating, approved sources for meat and whole hogs, insurance that covers the trailer, the COI venues ask for, W-2 staff and sales tax on catering — with notes for the UK. No state forms included: requirements vary by state, county and city.",
        image: '/lovable-uploads/ai-gallery/plan-parrillero-asador-eventos-6.jpg',
      },
      {
        icon: 'BarChart3',
        label: 'BONUS 2',
        title: 'US BBQ Catering Benchmarks (Sourced)',
        desc: 'The reference table inside the workbook: price per guest by package, guest minimums, pounds of meat per guest, smoker yield, food cost, wages for cooks and servers, smoker trailer prices, wood per cook, marketplace commission, deposits, shared kitchen rates, insurance and net margin, each with its source or marked "kit estimate" when there isn\'t one — plus five OK / REVIEW checks on your P&L against editable thresholds.',
        image: '/lovable-uploads/ai-gallery/plan-parrillero-asador-eventos-hero.jpg',
      },
      {
        icon: 'Globe',
        label: 'BONUS 3',
        title: 'US · UK · Canada · Australia Equivalents Guide',
        desc: 'Bonus: terms, taxes, food safety, staff rules, alcohol and units for using this kit in the US, UK, Canada and Australia.',
        image: '/lovable-uploads/ai-gallery/en-equivalents-guide.jpg',
      },
    ],
  },

  buyBox: {
    ctaLabel: 'YES, I WANT THE PLAN — $39',
  },

  guarantee: {
    text:
      "If the business plan doesn't live up to your expectations, we'll refund 100% of your money. No questions, no hassle.",
    stats: [
      { number: '30', label: 'Day guarantee' },
      { number: '100%', label: 'Money back' },
      { number: '0', label: 'Awkward questions' },
    ],
  },

  faqs: FAQS,

  cta: {
    headingPre: "It's Time to Launch Your ",
    headingGold: 'BBQ Catering Business',
    subtitle:
      'Plan it before you buy the smoker trailer: the written plan, the numbers behind it, a price for every quote by the pound and the permits list, for a one-time payment.',
    items: [
      '10-section BBQ catering business plan in Word',
      'Excel financial projections with a 3-year P&L',
      'Startup costs line by line and total cash needed',
      'Break-even in events per year, with a sensitivity table',
      'Pricing calculator: from pounds of meat per guest to a quote',
      'Meat yield & smoke schedule and a shopping list by guest count',
      'Startup checklist: 68 tasks in 6 phases',
      'BONUS: BBQ Catering Permits, Fire Rules & Food Safety Guide (included in the plan)',
      'BONUS: US BBQ Catering Benchmarks',
      'BONUS: US · UK · Canada · Australia Equivalents Guide',
    ],
    ctaLabel: 'YES, I WANT THE PLAN — $39',
  },

  pricing: {
    price: '$39',
    heroNote: 'One-time payment · lifetime access · updates included',
    buyBoxNote: 'One-time payment · lifetime access · updates included',
  },

  stickyLabel: 'BBQ CATERING BUSINESS PLAN — $39',

  // Salientes: los gemelos más cercanos (Catering de eventos, Food Truck), Catering Checklists (operación de eventos),
  // Food Cost (coste por invitado), HACCP (cocción, mantenimiento en caliente y enfriado), Staff Scheduling (personal por
  // evento), Financial Plan + los otros planes EN.
  footerLinks: [
    { href: '/en', label: 'aichef.pro' },
    { href: '/en/digital-products', label: 'Digital Products' },
    { href: '/en/digital-products/catering-business-plan', label: 'Catering Business Plan Kit' },
    { href: '/en/digital-products/paella-catering-business-plan', label: 'Paella Catering Business Plan Kit' },
    { href: '/en/digital-products/food-truck-business-plan', label: 'Food Truck Business Plan Kit' },
    { href: '/en/digital-products/catering-checklist-templates', label: 'Catering Checklists Kit Pro' },
    { href: '/en/digital-products/food-cost-templates', label: 'Food Cost Kit Pro' },
    { href: '/en/digital-products/haccp-templates', label: 'HACCP Food Safety Kit Pro' },
    { href: '/en/digital-products/restaurant-schedule-templates', label: 'Restaurant Staff Scheduling Kit Pro' },
    { href: '/en/digital-products/restaurant-financial-plan-templates', label: 'Restaurant Financial Plan Kit Pro' },
    { href: '/en/digital-products/restaurant-business-plan', label: 'Restaurant Business Plan Kit' },
    { href: '/en/digital-products/mobile-bar-business-plan', label: 'Mobile Bar Business Plan Kit' },
    { href: '/en/digital-products/bar-business-plan', label: 'Bar Business Plan Kit' },
    { href: '/en/digital-products/bakery-business-plan', label: 'Bakery Business Plan Kit' },
    { href: '/en/digital-products/coffee-shop-business-plan', label: 'Coffee Shop Business Plan Kit' },
    { href: 'mailto:info@aichef.pro', label: 'Contact' },
  ],
  updateNote: 'Version 2.2 · October 2026',

  alreadyBought: {
    product: 'bbq-catering-business-plan',
    label: 'Already bought the plan? Get back into your dashboard',
  },
};

export default data;
