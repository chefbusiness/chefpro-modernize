// astro-site/src/data/productos-en/tareas/bakery-checklist-templates.ts
// TIENDA INTERNACIONAL EN — Bakery Checklists Kit Pro. COPIA TRADUCIDA Y ADAPTADA de la ficha ES
// astro-site/src/data/productos/tareas/kit-tareas-panaderia.ts (mismo tipo KitTareasData, misma plantilla
// KitTareasLandingPage con lang="en", mismo orden de campos y de secciones), con las decisiones de sus hermanos EN
// (food-truck- y taco-shop-checklist-templates.ts los más cercanos). SPEC: scripts/productos-digitales/checklists-kit/
// bakery/SPEC.md (delta) + F2-NOTAS.md («lo que la F3 tiene que saber») + la del food truck (molde plano) + la base.
//   · D2: nombre «Bakery Checklists Kit Pro» (como el hermano LIVE Bakery Business Plan Kit); title SEO = H1 (Forma B):
//     «Bakery Checklists Kit Pro: Bread Bakery Opening, Production & Closing Checklist Templates for Excel». DataForSEO US
//     (31-oct): bakery opening checklist 30 (la cola con más volumen), bakery cleaning checklist / cleaning schedule /
//     production schedule 10; bread bakery 12.100. PAN, no pastelería: no pisa al Pastry Shop Checklists Kit Pro (tartas).
//   · D3/D4: $15 (molde plano), pago único. SIN precio tachado ni anclas (FTC 16 CFR 233.1, PR #117): sin priceOld,
//     discountBadge, bonusSaveLine, `value` en los bonos, aggregateRating ni review (el ES los lleva).
//   · MOLDE PLANO (F2-NOTAS): una hoja por libro, sin hoja de instrucciones, sin contador, sin N/A que descuente, sin
//     protección, sin línea de versión, sin firma ni iniciales, sin hoja de caja. NADA de eso se afirma aquí. Sí: columna
//     OK con desplegable ✓ / — / N/A y la fila en verde al marcar ✓ en 7 hojas (01-04, 06-08; el 05 lleva «Status» y el 09
//     va sin desplegable); el 01 trae la HORA de cada tarea del turno de madrugada (3:00 AM-2:30 PM); el 02 trae una
//     columna «Reading» para anotar pH, temperatura o volumen.
//   · Cifras SOLO de los 11 xlsx EN (revision/dump_en.txt, contrastadas el 31-oct): 135 tareas (01 25 = 7 + 7 + 5 + 6;
//     02 16; 03 18 = 6 + 5 + 7 de la tabla de horneado; 04 14; 05 13; 06 18 = 5 + 5 + 4 + 4; 07 16 = 8 + 8; 08 15), hoja
//     de producción diaria de 13 campos en 4 bloques, calendario de 12 meses (panes de temporada, eventos y pedidos,
//     mantenimiento, formación). °F solo los de los xlsx; °C solo en la FAQ UK (8 / 63 °C).
//   · Lo que el ES afirma y el kit EN no trae, fuera (SPEC §5): horno de CONVECCIÓN, «protocolos para recuperar masas que
//     pierden fuerza», «esponja», «gestión de cola en horas punta», «reporting con KPIs», «calibración de termómetros»
//     (solo básculas), San Juan, Reyes y las campañas españolas, ensaimadas, «acciones de marketing por estación» del
//     calendario (su columna E es Training), «cada categoría con sus tiempos y temperaturas» (la tabla trae 7 panes),
//     «Imprimible A4» (→ US Letter), la guía ES↔LatAm (→ Equivalents Guide) y la FAQ de Google Sheets (sin test real).
//   · Testimonios: los 8 del ES traducidos tal cual (nombres, roles y ciudades, sin marcas), con el subtítulo de la
//     edición española (TIENDA §3.5). Solo se pintan. Una frase que el kit EN contradice, cambiada (regla de John, 11-oct):
//     Fernando Delgado («Navidad, Reyes, Semana Santa» → «the holiday season, Easter»: el calendario EN no trae Reyes).
//     Avatares reasignados para que oficio y género cuadren: el maestro panadero lleva un avatar de chef con gorro
//     (chef-avatar-3, no el del chaleco de bar) y la oficial de obrador, la panadera de avatars-nicho (reutilizada).
//   · Imágenes: las 6 del ES, abiertas el 31-oct-2026: solo rótulos en inglés en los tarros («Poolish preferment»,
//     «Sourdough starter»), sin marcas ni texto en español → se quedan, con el reparto del ES. OG = el hero.
// DINERO: stripeEnvKey = VITE_STRIPE_PAYMENT_LINK_BAKERY_CHECKLISTS_KIT (resuelto en el wrapper .astro).
import type { KitTareasData } from '../../productos/tareas/types';

const data: KitTareasData = {
  slug: 'bakery-checklist-templates',
  stripeEnvKey: 'VITE_STRIPE_PAYMENT_LINK_BAKERY_CHECKLISTS_KIT',

  seo: {
    title: 'Bakery Checklists Kit Pro: Bread Bakery Opening, Production & Closing Checklist Templates for Excel',
    description:
      '11 Excel files with 135 bakery tasks already written: overnight bake shift, sourdough starter, ovens, display & labels, manager, roles. One-time $15.',
    keywords:
      'bakery checklist, bakery opening checklist, bakery closing checklist, bakery opening and closing checklist, bakery cleaning checklist, bakery cleaning schedule, bakery production schedule, bakery daily checklist, bread bakery checklist, sourdough bakery checklist, sourdough starter checklist, bakery manager checklist, AI Chef Pro',
    // OG = el hero de la ficha (como los hermanos EN): el og-kit-tareas-panaderia.jpg del ES lleva texto en español y €.
    ogImage: 'https://aichef.pro/lovable-uploads/ai-gallery/use-case-panadero-hero.jpg',
  },

  schema: {
    productName: 'Bakery Checklists Kit Pro',
    productDescription:
      '9 templates + 3 bonuses (12 files): Excel checklists for bread bakeries with 135 tasks already written: opening and closing on the overnight bake shift, the sourdough starter and fermentation, deck and rack ovens with a bake table in °F, the display case and counter with labels and allergens, the manager, duties by role, weekly and monthly cleaning and maintenance, seasons and holidays, a daily production sheet and an annual calendar.',
    price: '15.00',
    priceValidUntil: '2026-12-31',
    // FAQPage schema: versiones CORTAS de las FAQ on-page. Sin reviews ni aggregateRating (D3).
    faqs: [
      {
        q: 'What should be on a bakery opening checklist?',
        a: 'The overnight bake shift in order: ovens and proofer on, sourdough starters checked (activity, pH, temperature), ingredients scaled, base doughs mixed with the water temperature adjusted for the season, the bakehouse at 72–79 °F, then bulk fermentation, dividing and shaping, final proof, scoring, baking with steam and cooling on racks; and the shop opening: the bread display, allergen labels, TCS items cold or hot, the POS and starting bank, and display cases sanitized.',
      },
      {
        q: 'What goes on a bakery closing checklist?',
        a: 'The starter fed for tomorrow, the mixer, workbench and utensils cleaned and sanitized, the ovens off and clean (gas ovens serviced by a licensed technician), day-old bread counted for donation, breadcrumbs or croutons, the register closed out with the cash count and over/short, and the flour order for tomorrow.',
      },
      {
        q: 'Does it include a sourdough starter checklist?',
        a: 'Yes. The starter checklist covers the daily 1:1:1 feeding, pH before use (3.8–4.2), starter temperature (75–82 °F), the float test, a backup in the refrigerator and a reminder to log feeding date, pH, temperature and activity, with a Reading column for your figures.',
      },
      {
        q: 'Is there a free bakery checklist template in Excel or PDF?',
        a: 'Yes, you will find free checklist templates online. This kit is 11 Excel workbooks with 135 bread bakery tasks already written, a bake table and process temperatures in °F, and a ✓ / — / N/A drop-down. Print it on US Letter or save it as a PDF from Excel.',
      },
      {
        q: 'Does it work in the UK, Canada or Australia?',
        a: 'Yes, with a few edits: in the UK, cold holding at 8 °C, hot holding at 63 °C and 14 allergens; in Canada and Australia, your local holding temperatures and allergen list. Every English edition includes the US · UK · Canada · Australia Equivalents Guide.',
      },
      {
        q: 'Is there a money-back guarantee?',
        a: 'Yes. A full 30-day guarantee, 100% refund with no questions asked.',
      },
    ],
    breadcrumbName: 'Bakery Checklists Kit Pro',
  },

  images: {
    // hero bg (6) y strip del ContentGrid: las 6 fotos del ES (sin texto en español, sin marcas). Mismo reparto que el ES.
    gallery: [
      '/lovable-uploads/ai-gallery/use-case-panadero-hero.jpg',
      '/lovable-uploads/ai-gallery/use-case-panadero-fermentacion.jpg',
      '/lovable-uploads/ai-gallery/use-case-panadero-masa.jpg',
      '/lovable-uploads/ai-gallery/use-case-panadero-horneado.jpg',
      '/lovable-uploads/ai-gallery/use-case-panadero-panes.jpg',
      '/lovable-uploads/ai-gallery/use-case-panadero-team.jpg',
    ],
    whyBg: '/lovable-uploads/ai-gallery/use-case-panadero-team.jpg',
    buyBoxBg: '/lovable-uploads/ai-gallery/use-case-panadero-panes.jpg',
    ctaBg: '/lovable-uploads/ai-gallery/use-case-panadero-hero.jpg',
  },

  hero: {
    badge: 'Checklist apps charge every month; this is $15, once',
    // D2: titlePre + titleGold = «Bakery Checklists Kit Pro»; Forma B como los hermanos EN.
    titlePre: 'Bakery Checklists ',
    titleGold: 'Kit Pro',
    titlePost: ': ',
    subtitleLine: 'Bread Bakery Opening, Production & Closing Checklist Templates for Excel',
    description:
      '9 templates + 3 bonuses (12 files) with 135 bread bakery tasks already written in Excel: the overnight bake shift from 3:00 AM, the sourdough starter and preferments, deck and rack ovens, the display case and labels, the manager, roles, cleaning and seasons. Print it, hand it to your team and check it off.',
    checkItems: [
      'Opening and closing on the overnight bake shift, task by task from 3:00 AM to 2:30 PM',
      'Sourdough starter checklist: 1:1:1 feeding, pH 3.8–4.2, starter at 75–82 °F, float test, poolish and biga',
      'Deck and rack ovens with a bake table in °F: baguette, rustic loaf, ciabatta, whole wheat, croissant, brioche, sourdough',
      'Display case and counter: labels and the 9 major allergens, FIFO, gluten-free and organic only when you can back them',
      'A manager checklist, duties for 4 roles (head baker, baker, bakery assistant, counter staff) and weekly and monthly upkeep',
      'Bonuses: a daily production sheet and a 12-month US calendar of seasonal breads, holiday orders, maintenance and training',
    ],
    ctaLabel: 'BUY NOW — $15',
  },

  // Etiqueta corta (el ES también abrevia: «KIT TAREAS PANADERÍA — €12»).
  stickyLabel: 'BAKERY CHECKLISTS KIT PRO — $15',

  grid: {
    countGold: '9',
    headingRest: ' Bread Bakery Checklist Templates + 3 Bonuses (12 files)',
    subtitle:
      '135 bread bakery tasks already written and sorted by shift, area and role. Adjust them to your breads, print and delegate.',
    templates: [
      {
        icon: 'Sunrise',
        title: 'Bakery Opening & Closing Checklist: Overnight Bake Shift, Production & Shop',
        desc: 'The overnight bake shift (3:00–5:00 AM: ovens and proofer on, starters checked, scaling, mixing, the bakehouse at 72–79 °F), fermentation and baking (5:00–8:00 AM: bulk, shaping, final proof, scoring, steam, cooling), the shop opening (8:00–9:00 AM: the display, allergen labels, the POS) and the close: the starter fed, ovens off, day-old bread counted, the register closed out. 25 tasks, each with a time and who does it.',
      },
      {
        icon: 'Wheat',
        title: 'Sourdough Starter & Fermentation Checklist: Starter, Bulk, Retard & Preferments',
        desc: 'The natural starter (1:1:1 feeding, pH 3.8–4.2, 75–82 °F, float test, a backup in the refrigerator, the log), fermentation checks (dough at 75–79 °F after mixing, bulk time by bakehouse temperature, windowpane test, cold retard at 37–41 °F, final proof and the poke test) and yeast and preferments (fresh yeast at 36–39 °F, poolish and biga the night before). 16 checks with a Reading column.',
      },
      {
        icon: 'Flame',
        title: 'Bakery Oven Checklist: Deck & Rack Ovens, Steam and Bake Times',
        desc: 'Deck oven (preheat 45–60 minutes, the deck checked with an infrared thermometer at 430–500 °F, steam on loading, the damper opened after 10 minutes), rack oven (preheat, loading, time, temperature and steam programmed, even rotation, cleaning) and a bake table for 7 breads, from baguette at 465–480 °F with steam to brioche at 355–375 °F. 18 checks.',
      },
      {
        icon: 'Store',
        title: 'Bakery Display & Counter Checklist: Bread Case, Labels & Customer Service',
        desc: 'The display by type with FIFO rotation, labels with name, ingredients, net weight and allergens for everything bagged on site (FDA Food Code 3-602.11), a legal-for-trade scale if you sell by weight, meat empanadas and cream-filled items held cold or hot, gluten-free and organic only when you can back them, allergen questions, special orders and the close: day-old bread, cleaning and the register. 14 tasks.',
      },
      {
        icon: 'Users',
        title: 'Bakery Manager Checklist: Production Planning, Flour Orders, Waste & Food Cost',
        desc: 'Daily production planned from sales and orders, quality checks, recipes adjusted by season, new products, the flour order and ingredient stock, waste under 8% (the kit\'s target), flour quality (protein, ash, falling number, absorption), weekly food cost against a 28–35% benchmark, prices against flour and energy costs, the overnight shift schedule, training and social media. 13 tasks with frequency and priority.',
      },
      {
        icon: 'UserCog',
        title: 'Bakery Duties by Role: Head Baker, Baker, Bakery Assistant & Counter Staff',
        desc: 'Clear tasks for 4 roles: the head baker (starter and preferments, mixing, shaping and baking, quality, the day\'s production), the baker (scaling, mixing, shaping, the ovens, pastries), the bakery assistant (pans and baskets, scoring under supervision, packing and labels, cleaning) and the counter staff (display, customers, orders, the register).',
      },
      {
        icon: 'ClipboardList',
        title: 'Bakery Weekly & Monthly Checklists: Deep Cleaning, Maintenance & Inventory',
        desc: 'Weekly: the mixer, divider, ovens and proofer deep cleaned, the precision scale calibrated, flour, seed, yeast and butter inventory, use-by dates, the starter backup and waste. Monthly: oven maintenance (gas ovens by a licensed technician), the mixer, a review of your temperature, cleaning and allergen logs, food cost by product, flour suppliers, training, prices and pest control by a licensed operator.',
      },
      {
        icon: 'Gift',
        title: 'Bakery Seasonal & Holiday Checklist: Seasonal Breads, Holiday Orders & Specialties',
        desc: 'Breads by season (winter rye and walnut, spring herbs and olives, summer focaccia and ciabatta, fall pumpkin and chestnut), the key sales events (the holiday season with stollen, panettone and dinner rolls, Easter hot cross buns, Valentine\'s Day, Halloween, World Bread Day on Oct 16 and Thanksgiving pre-orders) and the trends: sourdough, gluten-free, organic and specialty grains. 15 tasks.',
      },
      {
        icon: 'FileSpreadsheet',
        title: 'Blank Bakery Checklist Template (Editable)',
        desc: 'A blank checklist with the kit\'s columns (area, task, assigned to, frequency, OK and notes) to build lists for your exact bakery: specialty breads, gluten-free, organic, pastries or savory items.',
      },
      {
        icon: 'Calendar',
        title: 'BONUS: Bakery Daily Production Sheet (Pre-Shift Briefing)',
        desc: '13 fields to start the day: today\'s production (basic breads, specialty breads, pastries, special orders), the starter and preferments (pH, temperature, activity; poolish yes / no; yeast stock), ovens and equipment, and the team, low-stock alerts and notes.',
      },
      {
        icon: 'CalendarDays',
        title: 'BONUS: Bakery Annual Calendar: Seasonal Breads, Orders, Maintenance & Training (US)',
        desc: '12 months for a US bread bakery: the seasonal breads, the events and orders (Super Bowl, Mardi Gras king cakes, St. Patrick\'s soda bread, Easter and Passover, Mother\'s Day, July 4 buns, Rosh Hashanah challah, World Bread Day, Thanksgiving rolls and the holidays), the maintenance and the training for each month.',
      },
    ],
  },

  why: {
    headingPre: 'Why This ',
    headingGold: 'Kit',
    headingPost: '?',
    subtitle:
      "These aren't generic templates. They're checklists designed by a chef who has worked in kitchens since the age of 17 and has been a hospitality consultant since 2010, set up for a US bread bakery under the FDA Food Code.",
    reasons: [
      {
        icon: 'Sunrise',
        title: 'Built for the Overnight Bake Shift',
        desc: 'Not restaurant templates with the name changed. Checklists for the real operation of a bakehouse from 3:00 AM: ovens on, the day\'s doughs, the first bake and the bread on the shelves before the shop opens.',
      },
      {
        icon: 'Wheat',
        title: 'Sourdough Starter and Preferments',
        desc: 'The starter fed 1:1:1, pH 3.8–4.2 and 75–82 °F, the float test and a backup in the refrigerator; dough temperature, bulk, retard and the poke test; poolish and biga the night before. The same bread every day.',
      },
      {
        icon: 'Flame',
        title: 'Deck and Rack Ovens, Down to the Detail',
        desc: 'Preheating, steam and loading for each oven, the deck oven\'s damper, and a bake table in °F for 7 breads, from baguette to brioche. Fewer batches lost to avoidable mistakes.',
      },
      {
        icon: 'RefreshCw',
        title: 'Checklist Apps Charge Every Month. This Is $15, Once',
        desc: 'The same kind of task lists bakeries run in premium checklist apps, in Excel, for a one-time payment. No subscription.',
      },
    ],
    // Pastillas de los hermanos EN: sin Google Sheets hasta el test real (SPEC base §6, §9); «A4» → US Letter.
    compatLabel: 'Compatible with:',
    compatPills: [
      { label: 'Microsoft Excel', highlight: true },
      { label: 'LibreOffice' },
      { label: 'Ready to print on US Letter' },
      { label: 'Apple Numbers' },
    ],
  },

  authorBio:
    'CEO of AI Chef Pro and founder of ChefBusiness Group. In kitchens since the age of 17 and a hospitality consultant since 2010. He has advised artisan bakeries, bakehouses and bakery chains on running their operations professionally: the overnight bake shift, sourdough starters and preferments, the ovens and the busy seasons of the year.',
  // authorBadges omitido → ui.authorBadgesDefault de i18n/tienda/en.json

  bonus: {
    headingPre: 'Exclusive ',
    headingGold: 'Bonuses',
    subtitle: 'Besides the 9 templates, you get these extra resources',
    items: [
      {
        icon: 'Calendar',
        label: 'BONUS 1',
        title: 'Bakery Daily Production Sheet',
        desc: "Today's breads, specialty breads, pastries and special orders; the starter's pH, temperature and activity, the poolish and the yeast stock; the ovens and the mixer; and the team, low-stock alerts and notes. One sheet to start every bake without surprises.",
        image: '/lovable-uploads/ai-gallery/use-case-panadero-team.jpg',
      },
      {
        icon: 'CalendarDays',
        label: 'BONUS 2',
        title: 'Bakery Annual Calendar (US)',
        desc: '12 months of seasonal breads, US events and orders (from Super Bowl and Mardi Gras king cakes to Rosh Hashanah challah, Thanksgiving rolls and the holidays), the maintenance and the team training for each month.',
        image: '/lovable-uploads/ai-gallery/use-case-panadero-horneado.jpg',
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
    ctaLabel: 'YES, I WANT THE BAKERY CHECKLISTS KIT — $15',
  },

  guarantee: {
    text: "If the checklists don't help you run your bakery more professionally, from the overnight bake shift and your starter to the ovens and the shop, we'll refund 100% of your money. No questions, no hassle.",
    stats: [
      { number: '30', label: 'Day guarantee' },
      { number: '100%', label: 'Money back' },
      { number: '0', label: 'Awkward questions' },
    ],
  },

  // FAQ on-page (acordeón): intención US medida (bakery opening / closing checklist, cleaning schedule, production
  // schedule, sourdough starter log) arriba + las 7 del ES adaptadas (masa madre, turno de madrugada, hornos —sin
  // convección—, bollería y panes especiales, garantía; Google Sheets fuera hasta el test real; la de Latinoamérica →
  // UK/CA/AU) + horneado, etiquetas y alérgenos, cottage food, pan frente a pastelería, plantilla gratis, cómo se marca,
  // apps, varias tiendas, caja, moneda y suscripción.
  faqs: [
    {
      q: 'What should be on a bakery opening checklist?',
      a: 'The overnight bake shift first, in the order it happens. From 3:00 AM: the proofer and the deck or rack oven on, the sourdough starters checked (activity, pH, temperature), the day\'s ingredients scaled, the base doughs mixed (baguette, rustic loaf, ciabatta) with the mixing water temperature set for the season, the bakehouse checked at 72–79 °F and the specialty doughs started. From 5:00 AM: bulk fermentation, dividing, scaling and shaping, the final proof in bannetons, scoring, baking with steam for the first 10 minutes and cooling on racks. From 8:00 AM, the shop: the bread display and pastry case, allergen labels on everything bagged or boxed, meat empanadas and cream-filled items held at 41 °F or below or 135 °F or above, the POS and starting bank, and the display cases cleaned and sanitized. The "Opening & Closing" checklist has those 19 opening tasks already written, each with a time and who does it.',
    },
    {
      q: 'What goes on a bakery closing checklist?',
      a: "In production: the starter fed for tomorrow, the mixer, workbench and utensils cleaned and sanitized (checked with test strips), and the ovens off and clean, with gas ovens serviced by a licensed technician as your local code requires (if you smell gas: light nothing, get out and call from outside). In the shop: day-old bread counted and sent to donation, breadcrumbs or croutons, and the register closed out with the cash count and over/short against the POS Z report. Then the flour and ingredient order for tomorrow. The kit has those 6 closing tasks already written, and the display checklist adds the shop's own close.",
    },
    {
      q: 'What should a bakery cleaning schedule include?',
      a: 'Daily cleaning goes in the closing checklist. On top of that, the kit schedules a weekly deep clean of the ovens (ash and grease) and of the mixer, divider and proofer, sanitized at label strength and checked with test strips, plus the scale calibration, the inventory and the use-by dates; and monthly upkeep: preventive oven maintenance (burners, gaskets, thermostats; gas ovens by a licensed technician), mixer maintenance (belts, gears, lubrication), a review of your temperature, cleaning and allergen logs, and pest control by a licensed operator with the service report on file while the team checks traps and signs in the flour storage.',
    },
    {
      q: 'Does it include a daily production sheet?',
      a: 'Yes, as a bonus. The daily production sheet has 13 fields in 4 blocks: today\'s production (baguettes and loaves, specialty breads, pastries and confirmed special orders), the starter and preferments (pH, temperature and activity; poolish made the night before, yes or no; fresh and dry yeast stock), ovens and equipment (deck oven, rack oven and mixer status) and the team on shift, low-stock alerts and notes. The manager checklist adds planning the day\'s production from sales and orders.',
    },
    {
      q: 'Does it cover the sourdough starter and preferments?',
      a: 'Yes. The starter checklist covers the daily 1:1:1 feeding (starter, flour, water) at the same time every day, pH before use (ideal 3.8–4.2), starter temperature (75–82 °F), the float test at peak activity, a backup in the refrigerator fed weekly and a log of feeding date, pH, temperature and activity. Then the fermentation checks (dough at 75–79 °F after mixing, bulk time by bakehouse temperature, the windowpane test, a cold retard at 37–41 °F for 12–72 hours if you use one, a final proof of +80–100% and the poke test) and yeast and preferments: fresh yeast at 36–39 °F, dry yeast airtight, poolish (1:1 flour and water plus yeast, 12–16 hours) and biga (50–60% hydration) made the night before. There is a column to write down each reading.',
    },
    {
      q: 'How does it handle the overnight bake shift?',
      a: 'The opening checklist runs task by task from 3:00 AM: the ovens and proofer on, the starters checked, scaling and mixing, then fermentation and baking from 5:00 AM and the shop opening from 8:00 AM, with the closing tasks in the early afternoon (the last at 2:30 PM). Every task has a time and who does it (baker, bakery assistant, counter staff or manager), and the manager checklist plans the overnight shift schedule every week. Change the times to fit your own schedule.',
    },
    {
      q: 'Does it cover different types of ovens?',
      a: 'Deck and rack ovens. For the deck oven: preheating 45–60 minutes before loading, the deck temperature checked with an infrared thermometer (430–500 °F, by bread), steam on loading for the first 8–10 minutes, the damper opened after 10 minutes to dry the crust, rotating loaves if needed and brushing the deck at close. For the rack oven: preheating per the manufacturer (15–30 minutes), loading racks with evenly spaced pans, programming time, temperature and steam, checking the rack rotates evenly and cleaning the oven and pans. If you bake in a convection oven, add its steps to the blank template.',
    },
    {
      q: 'What baking temperatures does it use?',
      a: 'A bake table in °F for 7 breads, set as a starting point for your oven: baguette at 465–480 °F with steam for 18–22 minutes, rustic loaf at 445–465 °F with steam for 35–45 minutes, ciabatta at 445 °F with steam for 20–25 minutes, whole wheat at 430–445 °F for 30–40 minutes, croissant at 375–390 °F without steam for 15–18 minutes, brioche at 355–375 °F for 20–25 minutes and sourdough at 445–465 °F with steam for 40–50 minutes, by size. Adjust them to your oven and your recipes.',
    },
    {
      q: 'Does it cover pastries and specialty breads?',
      a: 'Yes, alongside the everyday bread: croissants, pain au chocolat, danishes and brioche, savory items such as empanadas and filled breads, seasonal breads (rye and walnut in winter, focaccia in summer, pumpkin and chestnut in fall, stollen and panettone for the holidays) and specialty lines such as spelt, kamut, buckwheat and whole rye, gluten-free and organic. It is a bread bakery kit: if you mostly make cakes and pastries to order, the Pastry Shop Checklists Kit Pro is the one built for that.',
    },
    {
      q: 'Does it cover labels, allergens and gluten-free?',
      a: 'Yes. Everything bagged or boxed on site gets a label with the name, ingredients, net weight and the major allergens (FDA Food Code 3-602.11); unwrapped bread gets a written allergen notice where your state has adopted the 2022 FDA Food Code (3-602.12(C)). The 9 major US allergens are listed for the counter, mainly wheat, milk, eggs, soy, sesame, tree nuts and peanuts in a bakery. Call an item gluten-free only if you can back it (under 20 ppm gluten, 21 CFR 101.91) with strict separation in a bakery that uses wheat flour, and organic only with certified flour under USDA Organic rules. If you sell by weight, the scale must be legal-for-trade (NTEP).',
    },
    {
      q: 'Is it for a home bakery under cottage food laws?',
      a: 'No. It is set up for a bakery with a health permit (a food establishment) with a bakehouse, ovens and a shop. Many tasks, such as TCS items held at 41 °F or 135 °F, labels for items bagged on site and a licensed pest control operator, assume that. If you bake at home under your state\'s cottage food law, its rules on what you can sell and how you label it come first.',
    },
    {
      q: 'Is there a free bakery checklist template in Excel or PDF?',
      a: 'Yes, you will find free checklist templates online, and a blank one is fine to get started. This kit is something else: 11 Excel workbooks with 135 bread bakery tasks already written and sorted by shift, area and role, a sourdough starter checklist, a bake table and process temperatures in °F, and a ✓ / — / N/A drop-down on the checklists. Print it on US Letter, or save any sheet as a PDF from Excel.',
    },
    {
      q: 'Are the tasks already filled in for a bakery?',
      a: "Yes. Every checklist comes with the real tasks of a bread bakery already written. You'll want to make it yours: every cell can be edited, so adjust tasks, times and temperatures to your bakery, delete the ones that don't apply and add your own. The blank template has the same columns for anything extra.",
    },
    {
      q: 'How do you check off the tasks?',
      a: 'Each checklist has columns for the area or dough type, the task, who does it, when (a time on the opening and closing list, a frequency or the moment of the shift in the others), OK and notes; the starter checklist adds a column for the reading. In 7 of the checklists the OK column has a ✓ / — / N/A drop-down, and the row turns green when you pick ✓; the manager checklist has a status column you fill in yourself. Print the list and hand it to the team, or keep it open on a tablet in the bakehouse.',
    },
    {
      q: 'How is it different from checklist apps?',
      a: "Checklist apps charge a monthly fee per location and need connected tablets or phones. This kit gives you the same kind of task lists in Excel for $15, a one-time payment. What it is not: there are no reminders, photos or notifications on your team's phones.",
    },
    {
      q: 'Can I use it for several bakeries or with my clients?',
      a: "Yes. One purchase covers one business with all of its locations, which makes it a good fit for bakery chains. If you are a consultant, you can use the checklists with your clients, but you can't hand them copies: each business buys its own.",
    },
    {
      q: 'Does it include a cash drawer count?',
      a: "The register close-out is part of the day: the closing, display and duties checklists have you count the cash and note any over/short against the POS Z report. This kit has no separate cash count sheet by bill and coin; if you want one that works out the starting bank and the over/short for you, the Restaurant Checklists Kit Pro includes it.",
    },
    {
      q: 'Does it work in the UK, Canada or Australia?',
      a: "Yes, with a few edits, all in cells you can change. The kit is set up for the US: temperatures in °F, the FDA Food Code (41 °F cold holding and 135 °F hot holding for TCS items such as meat empanadas and cream fillings) and the 9 major allergens. In the UK, the legal limits are 8 °C for cold holding and 63 °C for hot holding, allergen information covers 14 allergens, and plain bread and most cold bakery items sold to take away are zero-rated for VAT, while hot takeaway food is not. In Canada and Australia, check your provincial or state food safety rules and allergen list and type them into the tasks. Every English edition also includes the US · UK · Canada · Australia Equivalents Guide, a bonus with the local terms, taxes, food safety, staff rules and units side by side.",
    },
    {
      q: 'What currency will I pay in?',
      a: 'The price is $15 USD, a one-time payment. At checkout, Stripe can show the amount in your local currency (for example GBP, EUR, CAD or AUD) and converts it for you.',
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
    heading: 'Your Bakery, Organized from the 3:00 AM Bake to the Close — in 11 Excel Files',
    subtitle:
      '9 templates + 3 bonuses (12 files) for the critical areas of your bakery: the overnight bake shift, the starter, the ovens, the display case, roles and seasons. For a one-time $15.',
    items: [
      'Opening and closing on the overnight bake shift, task by task with times',
      'Sourdough starter checklist, fermentation checks, poolish and biga',
      'Deck and rack ovens with a bake table in °F for 7 breads',
      'Display case and counter: labels, allergens, FIFO and special orders',
      'Tasks by role: head baker, baker, bakery assistant, counter staff',
      'Seasonal breads and holiday orders, from Easter to Thanksgiving',
      'BONUS: Bakery Daily Production Sheet',
      'BONUS: Bakery Annual Calendar (US)',
      'BONUS: US · UK · Canada · Australia Equivalents Guide',
    ],
    ctaLabel: 'YES, I WANT THE BAKERY CHECKLISTS KIT — $15',
  },

  // Testimonios: traducción fiel de los 8 del ES (decisión de John, 25-sep-2026). Son del Kit de Tareas Recurrentes:
  // Panadería / Obrador, la edición española de este kit: por eso conservan sus nombres, roles y ciudades, y el
  // subtítulo lo dice. Sin marcas. Solo se pintan: NO alimentan el JSON-LD. Una frase cambiada y dos avatares
  // reasignados (ver cabecera).
  testimonials: {
    subtitle:
      'Head bakers, bakers and bakery consultants who already run their production with Kit de Tareas Recurrentes: Panadería / Obrador, the Spanish edition of this kit',
    items: [
      {
        name: 'Alejandro Ruiz',
        role: 'Head Baker, Madrid',
        text: 'The overnight shift checklists are essential. Ovens on, the day\'s doughs, fermentation… the whole team follows the same routine from 3:00 AM, and we start production without chaos.',
        avatar: '/avatars/chef-avatar-3.jpg',
      },
      {
        name: 'María López',
        role: 'Bakery Owner, Barcelona',
        text: 'Tracking our starters and preferments saved us. Now every feeding is logged with its pH and temperature, and the poolish and biga go on the list every night. No more lost batches.',
        avatar: '/avatars/avatar-2.jpg',
      },
      {
        name: 'Carlos Méndez',
        role: 'Director, bakery chain (4 bakeries)',
        text: 'We rolled it out in 4 bakeries. Ovens, fermentation and production are now consistent in every shop. The same bread wherever you buy it.',
        avatar: '/avatars/avatar-3.jpg',
      },
      {
        name: 'Laura Fernández',
        role: 'Manager, artisan bakery',
        text: 'The duties by role make it clear who does what: head baker, baker, assistant, counter staff. The daily production sheet saves us time and mistakes on every bake.',
        avatar: '/avatars/avatar-4.jpg',
      },
      {
        name: 'David Torres',
        role: 'Bakery Consultant',
        text: "For bakeries it's the most complete kit out there. Sourdough, ovens, the display case, the overnight shift… it covers it all, with no gaps in the operation.",
        avatar: '/avatars/avatar-5.jpg',
      },
      {
        name: 'Ana García',
        role: 'Baker',
        text: 'The ovens and baking checklist is really detailed. Deck oven, rack oven, steam, times, temperatures… I know exactly what to do with every bake and every kind of bread.',
        avatar: '/lovable-uploads/avatars-nicho/avatar-panadera-celiaca.jpg',
      },
      {
        name: 'Pedro Gutiérrez',
        role: 'Production Manager, bakery',
        text: 'The weekly and monthly tasks, cleaning the ovens, checking our flours and calibrating the scales, keep us ready for any health inspection.',
        avatar: '/avatars/avatar-7.jpg',
      },
      {
        name: 'Fernando Delgado',
        role: 'Head Baker, premium bakery',
        text: 'The annual calendar with seasonal breads and special occasions helps us plan the holiday season, Easter and all our seasonal production with no surprises.',
        avatar: '/avatars/avatar-8.jpg',
      },
    ],
  },

  pricing: {
    price: '$15',
    heroNote: 'One-time payment · lifetime access · updates included',
    buyBoxNote: 'One-time payment · lifetime access · updates included',
    // D4: obligatorio en KitTareasPricing; sin «valor total» ni ahorro (FTC).
    bonusTotalLabel: 'Everything included: 9 templates + 3 bonuses',
  },

  footerLinks: [
    { href: '/en', label: 'aichef.pro' },
    { href: '/en/digital-products', label: 'Digital Products' },
    { href: '/en/digital-products/restaurant-checklist-templates', label: 'Restaurant Checklists Kit Pro' },
    { href: '/en/digital-products/bar-checklist-templates', label: 'Bar Checklists Kit Pro' },
    { href: '/en/digital-products/coffee-shop-checklist-templates', label: 'Coffee Shop Checklists Kit Pro' },
    { href: '/en/digital-products/catering-checklist-templates', label: 'Catering Checklists Kit Pro' },
    { href: '/en/digital-products/pizza-shop-checklist-templates', label: 'Pizza Shop Checklists Kit Pro' },
    { href: '/en/digital-products/burger-joint-checklist-templates', label: 'Burger Joint Checklists Kit Pro' },
    { href: '/en/digital-products/ghost-kitchen-checklist-templates', label: 'Ghost Kitchen Checklists Kit Pro' },
    { href: '/en/digital-products/ice-cream-shop-checklist-templates', label: 'Ice Cream Shop Checklists Kit Pro' },
    { href: '/en/digital-products/chocolate-shop-checklist-templates', label: 'Chocolate Shop Checklists Kit Pro' },
    { href: '/en/digital-products/pastry-shop-checklist-templates', label: 'Pastry Shop Checklists Kit Pro' },
    { href: '/en/digital-products/hotel-checklist-templates', label: 'Hotel Checklists Kit Pro' },
    { href: '/en/digital-products/taco-shop-checklist-templates', label: 'Taco Shop Checklists Kit Pro' },
    { href: '/en/digital-products/food-truck-checklist-templates', label: 'Food Truck Checklists Kit Pro' },
    { href: '/en/digital-products/seafood-restaurant-checklist-templates', label: 'Seafood Restaurant Checklists Kit Pro' },
    { href: '/en/digital-products/bakery-business-plan', label: 'Bakery Business Plan Kit' },
    { href: '/en/digital-products/food-cost-templates', label: 'Food Cost Kit Pro' },
    { href: '/en/digital-products/haccp-templates', label: 'HACCP Food Safety Kit Pro' },
    { href: '/en/digital-products/restaurant-inventory-templates', label: 'Restaurant Inventory Kit Pro' },
    { href: '/en/digital-products/restaurant-schedule-templates', label: 'Restaurant Staff Scheduling Kit Pro' },
    { href: '/en/digital-products/restaurant-financial-plan-templates', label: 'Restaurant Financial Plan Kit Pro' },
    { href: '/en/digital-products/ai-prompts-for-restaurants', label: 'Gastro Pro Prompts eBook' },
    { href: 'mailto:info@aichef.pro', label: 'Contact' },
  ],

  // La versión de los xlsx (docProps subject «Bakery Checklists Kit Pro · v1.1»; el ES es v1.1). Los ficheros no llevan
  // línea de versión dentro (molde plano): esto solo fecha la edición.
  updateNote: 'Version 1.1 · October 2026',

  alreadyBought: {
    product: 'bakery-checklist-templates',
    label: 'Already bought the kit? Get back into your dashboard',
  },
};

export default data;
