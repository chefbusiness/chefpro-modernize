// astro-site/src/data/productos-en/planes/paella-catering-business-plan.ts
// TIENDA INTERNACIONAL EN — Paella Catering Business Plan Kit. DUPLICADO de bbq-catering-business-plan.ts (molde exacto: mismo
// tipo PlanNegocioData, misma plantilla PlanNegocioLandingPage con lang="en", mismo orden de campos), con el copy del live
// paella caterer. Edición inglesa del ES astro-site/src/data/productos/planes/plan-negocio-paellero-eventos.ts (hreflang
// recíproco), cuyo contenido y cifras NO se reutilizan: el EN es otro concepto (SPEC D117).
// SPEC: scripts/productos-digitales/business-plans-en-7/SPEC-delta.md (§0 jerga, D114-D132) + las heredadas
//   business-plans-en-6 (D96-D113), -5 (D81-D95), -4 (D66-D80), -3 (D48-D65), -2 (D30-D47) y business-plans-en/SPEC.md (D1-D29).
//   · §0 / D114b: jerga US en las 3 capas (research §9). Title con el NOMBRE DEL PRODUCTO primero (patrón BBQ y mobile bar);
//     H1 Forma B `Paella Catering ` + oro `Business Plan` + «Template to Start a Live Paella & Spanish Catering Company: …»;
//     meta de research §9 («Paella catering business plan template for a live-cooking Spanish caterer…»); FAQ en la
//     redacción del comprador (las 9 de research §9) y keywords que captan «paella catering», «paella caterer», «spanish
//     catering» y «paella party». «paella chef» para la persona (nunca «paellero» ni «chef» suelto), «paella caterer» para
//     el negocio, «paella pan» (nunca «paellera»), «3-ring propane burner», «live paella», «backyard paella party»,
//     «commissary», «insulated food carriers» (sin la marca Cambro), W-2 (nunca «freelance»). Sin tildes en los préstamos
//     (detector de español): «fideua», «Serrano ham», «Spanish tortilla». Nada de «DO» aplicado al plato (deuda ES, D131).
//     Los 6 H2 de research §9 NO caben como H2 (constantes de UI_PLAN, como en el BBQ): sus keywords van en las tarjetas
//     (H3), las razones (H3), el subtítulo del grid y la FAQ.
//   · Vocabulario vetado (rule 5 de John + RX_PAEL_NO de inventario §7): ni smoker, pitmaster, brisket, pulled pork, ribs,
//     bark, smoke ring ni live pit; ni lo heredado del bar y del catering (plated, stations salvo «live paella station»,
//     refrigerated van, induction, pasta, bartender, cocktails, freelance). El nombre «BBQ Catering Business Plan Kit» solo
//     sale como producto hermano en la FAQ de canibalización y en el pie.
//   · Canibalización con Catering y BBQ (D114b): la landing diferencia por paella cocinada en vivo, paelleras y quemadores,
//     arroz por invitado; FAQ «Should I buy this or the Catering Business Plan Kit?».
//   · D115: $39 SIN anclas (sin priceOld, «-x %», «Total value», «Save $», «launch price» ni valor de los bonos).
//   · D116: los 4 ficheros de dl/paella-catering-business-plan/, dashboard PaellaCateringBusinessPlanDashboard.tsx y
//     get-download-urls.ts (mismas claves que el ES y que el BBQ) + la guía de equivalencias EN.
//   · Bonos sin precio y SOLO lo que existe en los ficheros: 1 = §9 del plan + fase 2 del checklist («Propane & Permits»);
//     2 = tabla «US PAELLA CATERING BENCHMARKS (sourced) AND KIT ESTIMATES» (D122) + los 5 umbrales del P&L; 3 = guía de
//     equivalencias EN. Sin aggregateRating ni review.
//   · Legal (research §6, sin inventar): sin cocina de casa (Food Code 3-201.11; el cottage food no cubre alimentos TCS),
//     commissary con acuerdo escrito, cocinar en el evento según el condado (limited food preparation de San Diego County
//     como ejemplo → «ask your county»), propano y carpa → «check with your fire marshal» sin cifras de un solo estado (los
//     20 ft de Virginia NO salen), arroz cocido = TCS (≥ 135 °F o TPHC 4 h con procedimiento escrito), 165 / 145 / 155 °F,
//     shellstock tags 90 días, sangría sin alcohol o con el vino del cliente y sin venderlo (corkage fuera del modelo).
//   · FAQ «Does it work in the UK, Canada or Australia?» (estilo BBQ): VAT/GST editables, lb (kg), °F (°C) y pulgadas (cm)
//     por REGLA_UNIDADES, nota UK del docx §9 (D126 108: registro 28 días antes, FHRS, VAT 20 %, gas con council y recinto,
//     14 alérgenos con moluscos, apio y sulfitos; en EE. UU. los moluscos no son alérgeno mayor). ⚠️ Comprobar contra F2.
//   · Testimonios (D26, como los otros planes EN): los 8 del ES (src/data/testimonials-plan-paellero-eventos) traducidos con
//     el subtítulo de la edición española y SIN ningún dato que no sea verdad en este kit: fuera «fiestas del pueblo»,
//     «modelo(s) de contrato B2B/B2C», «manual técnico», «12 paellas», «88 proveedores DO Valencia», «catálogo con SKU de
//     Garcima» (marca), «anexo legal CCAA», «10 experiencias», «Don» y todas las cifras (25 años, 4 planners, 2 meses,
//     95.000 EUR, 3 meses, 40 %, 10 minutos). Nombres con tilde en EXENTOS de tienda-gate.py.
//   · Imágenes: del ES del paellero valen -hero (paella en vivo en una boda al aire libre: el hero), -2 (paella de marisco
//     en un evento de empresa en una azotea), -4 (paelleras, quemador de 3 aros y azafrán) y -6 (estilos de paella). Fuera
//     -1 (cartel «PAELLA VALENCIANA D.O.»: texto y deuda DO), -3 (restaurante, no es nuestro comprador) y -5 (food truck con
//     rótulos en español y precios en €). Las 3 paella-catering-*.jpg las GENERA EL ORQUESTADOR con generate-images
//     (F3-NOTAS §4): deben existir en public/lovable-uploads/ai-gallery/ antes del merge. OG = recorte 1200×630 de
//     paella-catering-seafood-paella-wedding.jpg (las 3 generadas el 24-oct con generate-images).
// DINERO: stripeEnvKey = VITE_STRIPE_PAYMENT_LINK_PAELLA_CATERING_BUSINESS_PLAN (resuelto en el wrapper .astro; sin la env
// var el CTA cae a '#comprar' hasta que John cree el Payment Link).
import type { PlanNegocioData, PlanNegocioFaq } from '../../productos/planes/types';

// ── Cifras del caso US — confirmado con F2-NOTAS §8 (24-oct) (business-plans-en-7/F2-NOTAS.md y cifras_caso.json) ─────
// Valores del libro final (aplicar_en --idempotencia, D15 en verde sin calibrar: B4 135 · B6 58 · B5 $40, préstamo de
// punto fijo $64,000). Los ejemplos salen de «3 Example Quotes» de la calculadora (±10 % de $22 / $34 / $52).
const CASO = {
  eventos: '135', // B4 — confirmado con F2-NOTAS §8 (24-oct)
  invitados: '58', // B6 — confirmado con F2-NOTAS §8 (24-oct)
  precio: '$40.00', // B5 — confirmado con F2-NOTAS §8 (24-oct)
  ventas: '$313,200', // ventas_a1 = B4 × B5 × B6 — confirmado con F2-NOTAS §8 (24-oct)
  inversion: '$49,480', // capex: $44,700 + fianza $1,100 + 1 mes previo $1,100 + contingencia 10 % × filas 7, 8, 11, 12 y 15 = $2,580 — confirmado con F2-NOTAS §8 (24-oct)
  circulante: '$39,486', // fondo_maniobra — confirmado con F2-NOTAS §8 (24-oct)
  necesidad: '$88,966', // inversion_total = capex + fondo de maniobra — confirmado con F2-NOTAS §8 (24-oct)
  propios: '$25,000', // B30 — confirmado con F2-NOTAS §8 (24-oct)
  prestamo: '$64,000', // B31 de punto fijo (SBA 7(a), no cabe en el Microloan) — confirmado con F2-NOTAS §8 (24-oct)
  neto: '$20,319', // resultado_neto_a1 (D&A $5,734) — confirmado con F2-NOTAS §8 (24-oct)
  netoPct: '6.5%', // margen_neto_a1 — confirmado con F2-NOTAS §8 (24-oct)
  equilibrio: '116', // equilibrio_eventos (115.83 contable; 117 de caja; holgura 15.8 %) — confirmado con F2-NOTAS §8 (24-oct)
  dscr: '2.47×', // dscr_min — confirmado con F2-NOTAS §8 (24-oct)
  marketing: '$8,000', // marketing_anual — confirmado con F2-NOTAS §8 (24-oct)
  seguros: '$5,500', // B27 — confirmado con F2-NOTAS §8 (24-oct)
  pesEventos: '101', // Scenarios pesimista (caja −$10,040: se agota) — confirmado con F2-NOTAS §8 (24-oct)
  pesPrecio: '$36.00', // — confirmado con F2-NOTAS §8 (24-oct)
  pesInvitados: '52', // — confirmado con F2-NOTAS §8 (24-oct)
  ejDropoff: '$22.50', // «3 Example Quotes»: corporate drop-off 30 inv. — confirmado con F2-NOTAS §8 (24-oct)
  ejFiesta: '$32.00', // backyard paella party 45 inv. — confirmado con F2-NOTAS §8 (24-oct)
  ejBoda: '$53.00', // wedding 110 inv. with tapas hour and staff — confirmado con F2-NOTAS §8 (24-oct)
  arrozOz: '3.25', // oz de arroz crudo por invitado por defecto (D123) — confirmado con F2-NOTAS §8 (24-oct)
  menuStyles: '8', // menu styles (D117, docx §2, calculadora) — confirmado con F2-NOTAS §8 (24-oct)
  formulas: '700', // «more than N»: el libro tiene 722 fórmulas — confirmado con F2-NOTAS §8 (24-oct)
};

// FAQ on-page Y FAQPage (un solo array: lo que ve el visitante es lo que declara el schema).
const FAQS: PlanNegocioFaq[] = [
  {
    q: 'What should a paella catering business plan include?',
    a: 'The sections lenders and investors expect: executive summary, concept and value proposition, market analysis, competitive analysis, marketing plan, operations plan, management and staffing, financial plan, legal requirements and permits, and conclusions with an action plan. This kit gives you those 10 sections already written in Word for a live paella caterer, plus the Excel financial projections that back them up, a pricing calculator that turns your guest count into paella pans, rice and a price per guest, with a pan sizing table and a shopping list, and a 68-task startup checklist.',
  },
  {
    q: 'Is it a generic template or built for paella catering?',
    a: 'Built for a live paella caterer: the paella chef cooks giant paellas in front of the guests, in 26- to 36-inch (65-90 cm) paella pans over 3-ring propane burners, served with salad and bread, while the sofrito, the stock, the vegetables and the cleaned seafood are prepped the day before at a commissary. Backyard paella parties, weddings and rehearsal dinners, corporate events and a premium seafood-and-tapas line, plus drop-off paella for corporate lunches on weekdays. Event staff on W-2 payroll, a used cargo van and no alcohol sales of its own. Nothing to strip out from a restaurant template.',
  },
  {
    q: 'How much does it cost to start a paella catering business?',
    a: `It depends mostly on the van and on how many pans and burners you start with. A lean start — a few pans and burners, a vehicle you already own and drop-off or small backyard parties only — can come in around $12,000 to $20,000 (a kit estimate). The kit's example buys a fuller setup: ${CASO.inversion} in startup costs plus ${CASO.circulante} of working capital, for ${CASO.necesidad} in total cash needed. The Startup Costs sheet lists every line — paella burners and stands ($2,500), eight paella pans from 26 to 36 inches ($1,800), a propane and fire-safety kit ($900), commissary prep and storage fit-out, a used cargo van ($18,000) and its upfit with shelving and upright cylinder racks, LLC and legal, first-year permits and certifications, a fire or event permit and propane setup inspection if required, catering software, smallwares and paella tools, opening inventory, website, launch and a first bridal show, and the event setup: a canopy for the cooking station, tables, a handwashing station, coolers, chafing dishes and insulated food carriers — plus the commissary deposit, rent before opening and a contingency. Replace each line with your own quotes.`,
  },
  {
    q: 'How much should I charge per person for paella catering?',
    a: `Per guest, by package, starting from your costs. The pricing calculator takes your package (drop-off paella delivered hot, a live paella party cooked on site with salad and bread, or full-service live paella with a paella chef and staff for weddings and corporate events), your paella style, your guest count and guest minimum, and a tapas hour if you add one. It works out the pans for the pan size you pick, the pounds of rice, the gallons of stock and the propane, prices the ingredients at the cost you type (per pound, saffron per gram; it ships blank, so there are no invented seafood or saffron prices; until you fill them in, it uses a kit estimate of food cost per guest for each style and says so), adds salad and bread, disposables, paella chefs and servers with payroll taxes, applies your target margin and shows the price per guest. On top go the service charge, the sales tax and a 50% deposit (US caterers usually ask for 25-50%). As a market reference, published prices from US paella caterers run from about $12 to $31 per person for live-cooked paella with salad and bread, around $45 for lobster paella and $44 to $65 for a full Spanish menu with staff. The calculator's three example quotes: a corporate drop-off for 30 guests at about ${CASO.ejDropoff} per guest, a backyard paella party for 45 at about ${CASO.ejFiesta} and a wedding for 110 with a tapas hour and staff at about ${CASO.ejBoda}.`,
  },
  {
    q: 'How many people does a 36-inch paella pan serve?',
    a: 'About 40 guests as a main course, in the kit\'s planning table. Some retailers list a 36-inch (90 cm) pan as serving 40 to 50; the kit plans 40 to leave room for big appetites, 30 for a 32-inch (80 cm) pan and 18 for a 26-inch (65 cm) pan. The Paella Yield & Pan Sizing sheet covers pans from 18 to 40 inches, each with guests served, uncooked rice, stock and burner rings, all marked as kit estimates you can change, and the calculator turns your guest count into the number of pans of the size you pick. As a rule of thumb, one paella chef handles about three pans at once.',
  },
  {
    q: 'How much rice per person for paella for a crowd?',
    a: `Most paella cooks plan 3 to 3.5 oz (about 85-100 g) of uncooked rice per guest for a main course; the calculator uses ${CASO.arrozOz} oz, and you can change it. For 100 guests that's roughly 20 lb (9 kg) of uncooked rice. The sheet works out the stock per pan too: 1.2 quarts per pound of rice (2.5 liters per kg) by default, and up to 1.45 quarts (3 liters per kg) for bomba, which absorbs more. The Shopping List by Guest Count turns your guest count — and 40, 80, 150 and 300 guests — into pans and burners for the size you pick, pounds of rice and of each ingredient, gallons of stock, saffron in grams, lemons, bread, salad and aioli, propane cylinders, plates and flatware, ice for the seafood and the staff you need.`,
  },
  {
    q: 'Can I cook paella at home and sell it?',
    a: "No. Under the FDA Food Code, which most states adopt, food prepared in a private home can't be used in a food business (section 3-201.11), and cottage food laws, which let you sell some shelf-stable foods made at home, don't cover foods like cooked rice, chicken and seafood that need time and temperature control for safety. To cater paella you need a permitted kitchen: your own licensed commercial kitchen or a commissary under a written agreement, where you prep the sofrito, the stock and the seafood, plus the permits of your county health department. That's why the plan works from a commissary and why the commissary agreement is one of the first tasks in the checklist. Rules vary by state and county, so check with your local health department before you spend.",
  },
  {
    q: 'Do I need a permit to cook paella at an event?',
    a: "Usually, yes, and the rules for cooking on site vary by county. Under the FDA Food Code, a catering operation that serves food directly to guests is a food establishment, and many counties expect the food to be prepared in your permitted kitchen. Some allow limited cooking at the event: San Diego County, California, for example, lets caterers do limited food preparation at a private catered event, with the prep done at the commissary, a handwashing station on site and the cooking area kept apart from the guests. Ask your county whether cooking the rice in front of the guests fits its limits. The fire marshal may have a say too: keep the propane cooking station outdoors or under its own canopy, away from the guest tent, with the cylinders outside any tent and an extinguisher at hand, and watch for burn bans. A public event open to everyone is usually a temporary food establishment, with its own permit. Check with your county health department and your fire marshal.",
  },
  {
    q: 'What food safety rules apply to paella at events?',
    a: "Cooked rice is a time/temperature control for safety (TCS) food: Bacillus cereus, a common cause of outbreaks linked to rice held without enough heat, survives cooking, so paella has to be held at 135 °F (57 °C) or above, or served under time as a public health control — up to 4 hours with a written procedure, the time marked and anything left thrown away. The kit also uses the FDA Food Code minimum for each ingredient: 165 °F for chicken, 145 °F for 15 seconds for fish and seafood, and 155 °F for 17 seconds for raw Mexican-style chorizo (cured Spanish chorizo is ready to eat). Leftovers aren't cooled for reuse. Mussels and clams must come from approved sources and stay in their tagged container, and the shellstock tags are kept for 90 days. The plan's HACCP-based food safety plan and the checklist cover all of it.",
  },
  {
    q: 'Can I serve sangria at my paella events?',
    a: "Not as something you sell, unless you hold the right liquor license. In the plan, sangria is a non-alcoholic add-on, or the client buys the wine and your staff mix and pour it without charging for the alcohol. Some paella caterers charge a corkage fee, but in some states that can count as an alcohol sale, so the kit leaves it out of the model. If your staff serve the client's alcohol, add liquor liability coverage. Alcohol rules vary by state, so check yours.",
  },
  {
    q: 'Is a paella catering business profitable?',
    a: `It can be, but margins are thin: ItsaCheckmate reports an average net margin of 7-8% for caterers, and Galley Solutions puts food cost at 28-35% of the menu price. In the kit's example — ${CASO.eventos} events a year with ${CASO.invitados} guests at ${CASO.precio} per guest (excl. sales tax; staffing and service charge included) — year-1 sales are ${CASO.ventas} and net income is ${CASO.neto} (${CASO.netoPct}), after paying the owner as paella chef, with a break-even of ${CASO.equilibrio} events a year. That's a full-time owner-operator with a second paella chef on weekends, not a typical first year, and the price per guest includes the paella chef that some caterers charge separately. In the pessimistic scenario — ${CASO.pesEventos} events at ${CASO.pesPrecio} per guest and ${CASO.pesInvitados} guests — the cash runs out in year 1, and the plan says so. Build your first year on your own bookings, not on the example.`,
  },
  {
    q: 'What equipment do I need to start a paella catering business?',
    a: 'Paella pans in several sizes, 3-ring propane paella burners with legs or stands, 20-lb propane cylinders with regulators and hoses, fire extinguishers, and a vehicle that carries it all safely. The kit\'s example budgets $2,500 for paella burners and stands, $1,800 for eight pans (two 36-inch, three 32-inch and three 26-inch), $900 for a propane and fire-safety kit, a used cargo van ($18,000) with $3,000 of upfit — shelving, upright cylinder racks, tie-downs and a wrap — and $3,000 for the event setup: a canopy for the cooking station, tables, a handwashing station, coolers, chafing dishes and insulated food carriers. Gas is the base; a wood fire only where your fire marshal allows it. Check what your fire marshal and your county require before you buy.',
  },
  {
    q: 'What insurance do I need for paella catering?',
    a: `Usually general liability (venues often ask for a certificate of insurance naming them as additional insured) — check that the policy doesn't exclude open-flame cooking at events — commercial auto for the van, workers' compensation once you hire, and inland marine coverage for your pans, burners and gear on the road; liquor liability only if your staff serve the client's alcohol. Insureon puts a small caterer at about $45 a month for general liability, $96 for a business owner's policy, $82 for workers' comp and $204 for commercial auto. The example budgets ${CASO.seguros} a year for insurance; ask an agent who insures caterers for your own quotes.`,
  },
  {
    q: 'Should I buy this or the Catering Business Plan Kit?',
    a: "Buy this one if paella cooked live is your product: paella pans and 3-ring propane burners, a paella chef, rice per guest and pan sizing, the fire marshal and the propane setup, and the food safety rules for cooked rice and shellfish. The Catering Business Plan Kit is written for a general event caterer with a broad menu, and its calculator works from food cost per guest; the BBQ Catering Business Plan Kit is for smoked meats. All three share the same lender-ready format and the same Excel engine, driven by events per year, price per guest and guests per event.",
  },
  {
    q: 'Is this plan for a paella food truck or restaurant?',
    a: "No. It's built for a paella caterer with no storefront, which sells events, not plates over a counter. If you're opening a paella food truck, our Food Truck Business Plan Kit fits better; for a Spanish restaurant or a tapas bar, start from the Restaurant Business Plan Kit or the Bar Business Plan Kit. The Excel workbook takes any numbers you type, but the written plan describes a paella catering company, so you'd rewrite more of the text.",
  },
  {
    q: 'Can I present this plan to a lender or investors?',
    a: `Yes. It follows the format lenders usually ask for: a written plan, a 3-year P&L, break-even, three scenarios, a 12-month cash flow, sources and uses of funds and a loan schedule with the debt service coverage ratio (DSCR), checked against 1.25×, a common lender target. The loan schedule and the DSCR cover your main loan, the one you enter in the assumptions; the financing sheet also lists an SBA Microloan, investors or partners and local grants as sources of funds, without amortizing them. In the example, the owner puts in ${CASO.propios} and borrows ${CASO.prestamo} at 10% over 7 years — more than the SBA Microloan cap of $50,000, so it's a bank or SBA 7(a) loan — with a minimum DSCR of about ${CASO.dscr}. It's a lender-ready format, not a guarantee of approval, and a planning tool, not financial, tax or legal advice.`,
  },
  {
    q: 'Can I change the numbers in the Excel model?',
    a: `Yes. The green cells are the ones you type — events per year, price per guest, guests per event, the split between paella packages and add-ons, food and disposables cost, the corporate marketplace share, commissary rent, wages and any startup cost line — and more than ${CASO.formulas} linked formulas recalculate the rest. Client deposits aren't modeled, which keeps the cash flow on the cautious side. To change a calculated cell, use Review → Unprotect Sheet (there is no password). The workbook and the calculator each include an Instructions tab.`,
  },
  {
    q: 'Does it work in the UK, Canada or Australia?',
    a: "Yes, with UK notes. Tax rates and wages are editable cells: enter 20% VAT, Canadian GST/HST plus any PST, or 10% Australian GST, the tax you reclaim on purchases, and your own minimum wage and employer costs. UK and Australian prices include tax, so type your price per guest without it. The calculator works in pounds, ounces and gallons, with kilograms and liters alongside on the pan sizing sheet (1 lb = 0.454 kg; 1 gallon = 3.8 liters), degrees Fahrenheit with Celsius, pan sizes in inches with centimeters, saffron in grams and miles for travel. The plan's UK notes cover registering with your council at least 28 days before trading, the food hygiene rating, 20% VAT on event catering, agreeing the gas setup with the council and the venue, and the 14 allergens — which, unlike the 9 major allergens in the US, include molluscs such as mussels, clams and squid, plus celery and sulphites, all of which can turn up in a paella. In Canada and Australia, check your provincial or state food premises and fire rules with your local authority before you cook on site. Every English edition also includes the US · UK · Canada · Australia Equivalents Guide, a bonus with the local terms, taxes, food safety and staff rules side by side.",
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
  slug: 'paella-catering-business-plan',
  stripeEnvKey: 'VITE_STRIPE_PAYMENT_LINK_PAELLA_CATERING_BUSINESS_PLAN',

  seo: {
    title: 'Paella Catering Business Plan Kit: Word Template + Excel Financial Projections + Pricing Calculator | AI Chef Pro',
    description:
      'Paella catering business plan template for a live-cooking Spanish caterer: Word plan, 3-year Excel projections, pricing calculator and checklist.',
    keywords:
      'paella catering business plan, paella business plan, how to start a paella catering business, spanish catering business plan, paella catering prices, paella caterer, paella party, AI Chef Pro',
    ogImage: 'https://aichef.pro/og-paella-catering-business-plan.jpg',
  },

  schema: {
    productName: 'Paella Catering Business Plan Kit',
    productDescription:
      'Paella catering business plan template kit for a live paella and Spanish catering company: a 10-section business plan in Word, an Excel financial model with 9 sheets (assumptions, startup costs, 3-year P&L, break-even, scenarios, staffing, 12-month cash flow, financing with a loan schedule and DSCR, and instructions), a pricing calculator from paella pans, rice and price per guest to quote with a paella yield and pan sizing table and a shopping list by guest count, and a 68-task startup checklist in 6 phases. Set up for the US, with notes for the UK.',
    price: '39.00',
    priceValidUntil: '2026-12-31',
    faqs: FAQS,
    breadcrumbName: 'Paella Catering Business Plan Kit',
  },

  images: {
    // hero bg (6) — la paella en vivo en una boda al aire libre (ES -hero) abre; las 3 paella-catering-* las genera el
    // orquestador (F3-NOTAS §4); -2 (paella de marisco en un evento de empresa) y -6 (estilos de paella) cierran.
    gallery: [
      '/lovable-uploads/ai-gallery/plan-paellero-eventos-hero.jpg',
      '/lovable-uploads/ai-gallery/paella-catering-seafood-paella-wedding.jpg',
      '/lovable-uploads/ai-gallery/paella-catering-backyard-party-tapas.jpg',
      '/lovable-uploads/ai-gallery/paella-catering-van-pans-burners.jpg',
      '/lovable-uploads/ai-gallery/plan-paellero-eventos-2.jpg',
      '/lovable-uploads/ai-gallery/plan-paellero-eventos-6.jpg',
    ],
    // strip del ContentGrid (6): -4 (paelleras y quemador) entra en lugar del hero; el resto, en otro orden.
    gridGallery: [
      '/lovable-uploads/ai-gallery/paella-catering-backyard-party-tapas.jpg',
      '/lovable-uploads/ai-gallery/plan-paellero-eventos-4.jpg',
      '/lovable-uploads/ai-gallery/paella-catering-van-pans-burners.jpg',
      '/lovable-uploads/ai-gallery/plan-paellero-eventos-2.jpg',
      '/lovable-uploads/ai-gallery/plan-paellero-eventos-6.jpg',
      '/lovable-uploads/ai-gallery/paella-catering-seafood-paella-wedding.jpg',
    ],
    whyBg: '/lovable-uploads/ai-gallery/plan-paellero-eventos-2.jpg',
    buyBoxBg: '/lovable-uploads/ai-gallery/plan-paellero-eventos-hero.jpg',
    ctaBg: '/lovable-uploads/ai-gallery/plan-paellero-eventos-hero.jpg',
  },

  hero: {
    badge: 'Lender-ready paella catering business plan: Word + Excel + pricing calculator',
    titlePre: 'Paella Catering ',
    titleGold: 'Business Plan',
    titleSubtitle:
      'Template to Start a Live Paella & Spanish Catering Company: Word Plan + Excel Financial Projections + Pricing Calculator + Startup Checklist',
    description:
      'Everything you need to plan, price and pitch a paella caterer that cooks giant paellas live in front of the guests: a 10-section business plan in Word, already written for the format lenders expect; an Excel model that recalculates your startup costs, 3-year P&L, break-even in events per year, 12-month cash flow and loan payments from your own numbers; a pricing calculator that turns your guest count into paella pans, rice, propane and a price per guest, with a pan sizing table and a shopping list; and a 68-task checklist that takes you from your LLC, your commissary agreement and the fire marshal to your first 90 days of events. Set up for the US, with notes for the UK.',
    checkItems: [
      '10-section paella catering business plan in Word, ready to edit',
      'Excel financial projections: 3-year P&L, break-even in events per year and 12-month cash flow',
      'Pricing calculator: pans, rice and price per guest to quote, with pan sizing and a shopping list',
      'Startup checklist: 68 tasks in 6 phases, from your LLC to your first 90 days',
      'Instant access + lifetime updates',
    ],
    ctaLabel: 'GET THE BUSINESS PLAN — $39',
  },

  compatSubtitle: 'Microsoft Excel and Word files, set up to print on US Letter paper',

  grid: {
    subtitle:
      "What's inside your Paella Catering Business Plan Kit: 9 building blocks to test whether your paella catering business works on paper before you buy pans and burners, price every paella party per guest and present the plan to a lender or an investor.",
    templates: [
      { icon: 'FileText', title: 'Paella Catering Business Plan (Word, 10 Sections)', desc: `A complete plan already written for a live paella caterer that preps at a commissary and cooks in front of the guests: executive summary, concept and value proposition with ${CASO.menuStyles} menu styles (seafood, chicken & seafood, chicken & chorizo, Valencian, farm vegetable, paella negra, lobster & seafood and an easy-eat peeled seafood paella) and the events you'll sell, market analysis, competitive analysis, marketing plan (The Knot, WeddingWire, Zola, ezCater, bridal shows and tastings), operations plan (the day before at the commissary, then arrival, setup, cooking, service and breakdown at the event), management and staffing, financial plan, legal requirements, permits and propane rules, and conclusions with an action plan. Its figures are the ones in the example Excel model.` },
      { icon: 'FileSpreadsheet', title: 'Paella Catering Financial Projections (Excel, 9 Sheets)', desc: `Is a paella catering business profitable? Assumptions, startup costs, 3-year P&L, break-even, scenarios, staffing, 12-month cash flow, financing and instructions. More than ${CASO.formulas} linked formulas: change events per year, price per guest or guests per event and the whole workbook recalculates.` },
      { icon: 'Calculator', title: 'Paella Catering Pricing Calculator (Pans, Rice and Price per Guest to Quote)', desc: 'Paella catering prices from your own costs. Three packages — drop-off paella delivered hot, a live paella party cooked on site with salad and bread, and full-service live paella with a paella chef and staff — plus your paella style and a tapas hour switch with its cost per guest; guests and guest minimum, ounces of uncooked rice per guest, pan size, the price you pay for each ingredient (per pound, saffron per gram; you type it), salad and bread, disposables, propane, paella chefs and servers with wages and payroll taxes, target margin, service charge, sales tax, a 50% deposit and cancellation tiers. Out come the pans for the size you pick, the people you need, pounds of rice, gallons of stock, propane and 20-lb cylinders, the price per guest, the total, the deposit, the balance and the margin it really leaves. Three example quotes: a corporate drop-off, a backyard paella party and a wedding with a tapas hour.' },
      { icon: 'Thermometer', title: 'Paella Yield & Pan Sizing + Shopping List by Guest Count', desc: `Paella for a crowd: pan sizes, rice per guest and staff for 50, 100 or 200 guests, or any count you type. Pans from 18 to 40 inches (46-100 cm), each with guests served, uncooked rice, stock and burner rings; ${CASO.menuStyles} paella styles with ounces per guest of every ingredient, the FDA Food Code minimum in its own column (165 °F for chicken, 145 °F for seafood), hot holding at 135 °F or a written 4-hour time procedure, and the typical allergens of each style to verify with your recipe and suppliers. The shopping list scales your guest count — and 40, 80, 150 and 300 guests — into pans and burners for the size you pick, pounds of rice and of each ingredient, gallons of stock, saffron in grams, bread, salad and aioli, propane cylinders, plates and flatware, ice for the seafood and the staff you need.` },
      { icon: 'Coins', title: 'Paella Catering Startup Costs, Line by Line', desc: 'How much does it cost to start a paella catering business? Paella burners and stands, eight paella pans from 26 to 36 inches, a propane and fire-safety kit, commissary prep and storage fit-out, a used cargo van and its upfit (shelving, upright cylinder racks, tie-downs and a wrap), LLC and legal, first-year permits and certifications, a fire or event permit and propane setup inspection if required, catering software, smallwares and paella tools, opening inventory, website, launch and your first bridal show, and the event setup — a canopy for the cooking station, tables, a handwashing station, coolers, chafing dishes and insulated food carriers — each with a reference price you replace with your quotes, plus the commissary deposit, rent before opening, a contingency and working capital.' },
      { icon: 'TrendingUp', title: 'Break-Even in Events per Year + 3 Scenarios', desc: 'How many events a year you need at your price per guest (excl. sales tax) and guest count to cover every cost, and the cash break-even with loan payments in and depreciation out, with a sensitivity table and a plain-English reading of the result. Plus pessimistic, base and optimistic scenarios side by side, each with its own estimated cash balance — honest about what a slow first year does to your cash.' },
      { icon: 'Users', title: 'Staffing & Event Labor (4 Roles)', desc: 'Owner / Paella Chef & Sales, a part-time lead cook who works as second paella chef, hourly W-2 event staff (servers and buffet attendants) and a part-time prep cook who drives the van, with gross pay, employer payroll taxes and the real cost of each role. The sheet checks the event hours you need (hours per event × people per event × events) against the hours you hire, and flags any pay below the minimum wage for the hours worked.' },
      { icon: 'ShieldCheck', title: 'Startup Checklist (68 Tasks, 6 Phases)', desc: "Business setup (LLC, EIN, seller's permit, business license, your loan application, your catering contract with a 25-50% deposit, cancellation tiers and a plan B for wind and rain, a HACCP-based food safety plan with cooked rice as a TCS food and ServSafe Manager), propane and permits (a written commissary agreement, your county on cooking at the event, the fire marshal on the propane station and the canopy, the van with cylinders upright and secured, insurance that does not exclude open flame), equipment (pans and 3-ring burners tested ring by ring, the propane kit and a refill account, insulated carriers, approved seafood sources and shellstock tags kept 90 days, a full test cook), staff (W-2, never 1099; food handler cards; propane and fire safety training), marketing (The Knot, WeddingWire, Zola, ezCater, Thumbtack, Google Business Profile, bridal shows and a launch tasting) and your first 90 days." },
      { icon: 'Banknote', title: 'Financing Plan', desc: "Owner equity and your loan (bank or SBA 7(a)) with its amortization schedule and the debt service coverage ratio (DSCR) year by year against a 1.25× target, plus an SBA Microloan, investors or partners and local grants as other sources of funds, and a warning if your sources don't cover the cash you need." },
    ],
  },

  // Testimonios: traducción de los 8 del ES (D26), del Plan de Negocio Paellero para Eventos, la edición española. Sin
  // ningún dato que no sea verdad en este kit (ver cabecera). Solo se pintan: NO alimentan el JSON-LD.
  testimonials: {
    subtitle:
      'Paella chefs and rice cooks who planned their event business with the Spanish edition of this plan',
    items: [
      { name: 'Vicent Pellicer', role: 'Valencian rice cook, Sueca, Spain', text: 'I cooked paella at local celebrations for years and never had a business plan to move up to premium weddings. This kit gave me the whole picture, and the pricing calculator is what won over the wedding planners I work with now.', avatar: '/avatars/avatar-1.jpg' },
      { name: 'Carmen Soler', role: 'Paella chef for weddings at rural venues, Toledo, Spain', text: 'The pan sizing and yield table is pure gold: I printed it and keep it laminated in the van. My weddings were more consistent from the very first season.', avatar: '/avatars/avatar-2.jpg' },
      { name: 'Antonio Rivas', role: 'Seafood paella chef for private events, Murcia, Spain', text: 'For years I made seafood paella at private events with no brand behind me. The business plan and its marketing section positioned me as a premium option with the wedding planners in my area.', avatar: '/avatars/avatar-3.jpg' },
      { name: 'Marc Esteve', role: 'Young rice-dish entrepreneur, Valencia, Spain', text: 'I am in my second year, and the startup checklist saved me months: equipment, permits and insurance in order, so I knew what to do every week before my first event.', avatar: '/avatars/avatar-4.jpg' },
      { name: 'Sara Romero', role: 'Corporate paella chef, Madrid, Spain', text: 'I cook paella live for companies on rooftop terraces, and following the startup costs line by line kept my initial investment under control. The pricing calculator is the tool I use most.', avatar: '/avatars/avatar-5.jpg' },
      { name: 'Joan Beltrán', role: 'Traditional wood-fire paella cook, Castellón, Spain', text: 'I am old school with a wood fire and thought I did not need a plan, but the legal section and the permits checklist put the paperwork for my first wedding with a planner in order.', avatar: '/avatars/avatar-6.jpg' },
      { name: 'Laura Martín', role: 'Premium wedding paella chef, eastern Spain', text: 'The menu styles and the three packages gave me a catalog I can actually sell: now I sell an experience, not just a menu.', avatar: '/avatars/avatar-7.jpg' },
      { name: 'Diego Montes', role: 'Fideua and paella cook, Alicante, Spain', text: 'The pricing calculator changed how I quote. I used to price each event by gut feeling; now I enter the guests, see the pans, the rice and my margin, and send the quote.', avatar: '/avatars/avatar-8.jpg' },
    ],
  },

  why: {
    subtitle:
      'Not another generic template: a paella catering plan written for the format lenders expect, with a financial model and a pricing calculator that recalculate from your own numbers.',
    reasons: [
      { icon: 'Flame', title: 'Built for a Live Paella Caterer', desc: 'A paella chef who cooks giant paellas in front of the guests over 3-ring propane burners; sofrito, stock, vegetables and cleaned seafood prepped the day before at a commissary; salad and bread, a tapas hour and a buffet with attendants for weddings; drop-off paella for corporate lunches on weekdays and a premium seafood-and-tapas line. Nothing to strip out from a restaurant or a general catering template.' },
      { icon: 'ShieldCheck', title: 'Cooking Paella at Events: Commissary, Propane and Food Safety Rules', desc: "Food prepared in a private home can't be used under the FDA Food Code. The plan works from a commissary under a written agreement, explains how counties treat cooking at a catered event (ask yours) and what the fire marshal checks around a propane cooking station and its canopy, and keeps cooked rice where the Food Code wants it: hot at 135 °F or above, or on a written 4-hour time procedure, with the shellstock tags of your mussels and clams kept for 90 days." },
      { icon: 'Calculator', title: 'Paella Catering Prices: What to Charge per Person', desc: 'Drop-off, backyard paella party or full service: the calculator turns your guests, your paella style, ounces of rice per guest, ingredient prices, propane, staff hours and a tapas hour into pans, rice, stock and propane, a price per guest and a quote with the service charge, the sales tax and a 50% deposit, and shows the margin it leaves. Three example quotes: a corporate drop-off, a backyard paella party and a wedding with a tapas hour.' },
      { icon: 'BarChart3', title: 'Honest Numbers, Calculated', desc: `The example: ${CASO.eventos} events a year with ${CASO.invitados} guests at ${CASO.precio} per guest (excl. sales tax; staffing and service charge included), ${CASO.ventas} in year-1 sales and ${CASO.equilibrio} events a year to break even — a full-time owner-operator with a second paella chef on weekends, not a typical first year. The pessimistic scenario runs out of cash, and the plan says so. Replace the numbers with yours.` },
    ],
    compatLabel: 'Works with:',
    compatPills: [
      { label: 'Microsoft Excel (.xlsx)', highlight: true },
      { label: 'Microsoft Word (.docx)' },
      { label: 'US Letter size' },
    ],
  },

  authorBio:
    'CEO of AI Chef Pro and founder of ChefBusiness Group. In kitchens since the age of 17 and a restaurant consultant since 2010, he has advised paella and rice cooks and event caterers on launching and growing live paella services for weddings and events, combining hands-on operations with financial planning.',
  // authorBadges omitido → default del diccionario EN ['Restaurant consultant since 2010', 'In professional kitchens since 17'].

  bonus: {
    subtitle:
      'Besides the business plan, the financial model, the pricing calculator and the startup checklist, you get these extra resources, drawn from the plan and the workbook themselves',
    items: [
      {
        icon: 'Map',
        label: 'BONUS 1',
        title: 'Paella Catering Permits, Propane & Food Safety Guide (US + UK Notes)',
        desc: "Section 9 of the plan plus Phase 2 of the checklist: why there's no legal way to sell paella from your home kitchen, the written commissary agreement, how counties treat cooking at a catered event (limited food preparation in California, for example), what the fire marshal checks around the propane cooking station, the canopy and the cylinders, cooked rice as a TCS food (hot holding at 135 °F or a written 4-hour time procedure), the Food Code temperatures for chicken, seafood and chorizo, approved sources and shellstock tags for mussels and clams, sangria without selling alcohol, insurance that doesn't exclude open flame, the COI venues ask for, W-2 staff and sales tax on catering — with notes for the UK. No state forms included: requirements vary by state, county and city.",
        image: '/lovable-uploads/ai-gallery/plan-paellero-eventos-2.jpg',
      },
      {
        icon: 'BarChart3',
        label: 'BONUS 2',
        title: 'US Paella Catering Benchmarks (Sourced)',
        desc: 'The reference table inside the workbook: price per person for live paella and for a full Spanish menu with staff, guest minimums, rice per guest, guests per paella pan, pans and burners, food cost, the paella chef and attendant fees some caterers charge separately, wages for cooks and servers, marketplace commission, shared kitchen rates, propane and disposables per event, insurance and net margin, each with its source or marked "kit estimate" when there isn\'t one — plus five OK / REVIEW checks on your P&L against editable thresholds.',
        image: '/lovable-uploads/ai-gallery/plan-paellero-eventos-4.jpg',
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
    headingGold: 'Paella Catering Business',
    subtitle:
      'Plan it before you buy the pans and burners: the written plan, the numbers behind it, a price per guest for every quote and the permits list, for a one-time payment.',
    items: [
      '10-section paella catering business plan in Word',
      'Excel financial projections with a 3-year P&L',
      'Startup costs line by line and total cash needed',
      'Break-even in events per year, with a sensitivity table',
      'Pricing calculator: from pans and rice per guest to a quote',
      'Paella yield & pan sizing and a shopping list by guest count',
      'Startup checklist: 68 tasks in 6 phases',
      'BONUS: Paella Catering Permits, Propane & Food Safety Guide (included in the plan)',
      'BONUS: US Paella Catering Benchmarks',
      'BONUS: US · UK · Canada · Australia Equivalents Guide',
    ],
    ctaLabel: 'YES, I WANT THE PLAN — $39',
  },

  pricing: {
    price: '$39',
    heroNote: 'One-time payment · lifetime access · updates included',
    buyBoxNote: 'One-time payment · lifetime access · updates included',
  },

  stickyLabel: 'PAELLA CATERING BUSINESS PLAN — $39',

  // Salientes: los gemelos más cercanos (Catering de eventos, BBQ Catering, Food Truck), Catering Checklists (operación de
  // eventos), Food Cost (coste por invitado), HACCP (arroz cocido, mantenimiento en caliente), Staff Scheduling (personal
  // por evento), Financial Plan + los otros planes EN.
  footerLinks: [
    { href: '/en', label: 'aichef.pro' },
    { href: '/en/digital-products', label: 'Digital Products' },
    { href: '/en/digital-products/catering-business-plan', label: 'Catering Business Plan Kit' },
    { href: '/en/digital-products/bbq-catering-business-plan', label: 'BBQ Catering Business Plan Kit' },
    { href: '/en/digital-products/pizza-shop-business-plan', label: 'Pizza Shop Business Plan Kit' },
    { href: '/en/digital-products/ice-cream-shop-business-plan', label: 'Ice Cream Shop Business Plan Kit' },
    { href: '/en/digital-products/wedding-venue-business-plan', label: 'Wedding Venue Business Plan Kit' },
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
    product: 'paella-catering-business-plan',
    label: 'Already bought the plan? Get back into your dashboard',
  },
};

export default data;
