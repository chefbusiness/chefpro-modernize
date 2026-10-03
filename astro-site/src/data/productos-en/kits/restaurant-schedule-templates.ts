// astro-site/src/data/productos-en/kits/restaurant-schedule-templates.ts
// TIENDA INTERNACIONAL EN — Restaurant Staff Scheduling Kit Pro. COPIA TRADUCIDA Y ADAPTADA de la ficha
// ES astro-site/src/data/productos/kits/kit-gestion-personal.ts (mismo tipo, misma plantilla
// KitExcelLandingPage, mismo orden de campos). Patrón = restaurant-inventory-templates.ts y
// haccp-templates.ts (ola 1).
// SPEC: scripts/productos-digitales/staff-kit/SPEC.md (§6 = esta landing).
//   · D2: nombre «Restaurant Staff Scheduling Kit Pro»; title SEO y H1 = «Restaurant Staff Scheduling
//     Kit Pro: Restaurant Schedule Template & Staff Rota for Excel». H1 en Forma B como los hermanos EN
//     (titlePost «: » + titleSubtitle en bloque): el texto del H1 es exactamente el de D2.
//   · D5: títulos de las 9 plantillas = los de los xlsx EN (§2.1, dl/restaurant-schedule-templates/).
//   · D3: $19, pago único. D4: priceOld 49 € → $59; cada bono 9 € → $19. Derivados: bonos $38 ·
//     total $97 · ahorro $40 · descuento 1 − 19/59 = 67,8 % → «-67%» (redondeo hacia abajo, como el piloto).
//   · Cifras y normativa SOLO de SPEC §3 (FLSA, Cal. Labor Code, 29 CFR 570, Fair Workweek, I-9, notas
//     UK). Lo que es criterio del kit (alerta de 10 h, presupuesto anual de horas extra, 14 días de PTO,
//     10 % de coste de empresa) se presenta como parámetro editable o estimación, nunca como ley. Sin
//     «compliant», «required by law» ni asesoría legal: los umbrales son celdas que el cliente ajusta.
//   · Sin reviews ni aggregateRating en el JSON-LD. Testimonios: los 8 del ES traducidos tal cual
//     (nombres, negocios y cifras de origen), con el subtítulo de la edición española (TIENDA §3.5).
//     Única adaptación: donde el ES habla de «límite legal», «normativa vigente» o «Inspección de
//     Trabajo» se precisa que es la española, para que no se lea como una promesa sobre la ley de EE. UU.
//   · Compatibilidad: SIN Google Sheets mientras no haya test real (SPEC §6 y §9: «Test real en Google
//     Sheets antes de afirmarlo en la FAQ»), y el resto de la landing coherente con eso (subtítulo de
//     compatApps, compatLabel y pastillas). El resto, como los kits EN hermanos (Excel, LibreOffice,
//     Numbers) + US Letter. Cuando el test pase: volver a añadir la pastilla «Google Sheets», el
//     subtítulo y la respuesta de la FAQ (y el aviso del dashboard RestaurantScheduleKitDashboard.tsx).
//   · Iconos: Banknote en lugar de Euro (tienda en USD, como Food Cost Kit Pro).
//   · Imágenes: la portada del ES (tareas-gestion-personal-hero.jpg) y su OG (og-kit-gestion-personal.jpg,
//     la misma foto) enseñan una APP de turnos en una tablet: engañan en un producto Excel → fuera.
//     Se queda el resto del set del ES (sin texto en español) y entra manual-manager-briefing.jpg (sin
//     texto) en su lugar. Revisión 3-oct: OG og-staff-scheduling-kit.jpg y 3 fotos propias staff-en-* (Gemini,
//     sin texto) sustituyen a la portada provisional y a -turnos/-oficina (rótulos de IA ilegibles).
// DINERO: stripeEnvKey = VITE_STRIPE_PAYMENT_LINK_STAFF_SCHEDULING_KIT (resuelto en el wrapper .astro).
import type { KitExcelData } from '../../productos/kits/types';

const data: KitExcelData = {
  slug: 'restaurant-schedule-templates',
  stripeEnvKey: 'VITE_STRIPE_PAYMENT_LINK_STAFF_SCHEDULING_KIT',

  seo: {
    title: 'Restaurant Staff Scheduling Kit Pro: Restaurant Schedule Template & Staff Rota for Excel',
    description:
      '9 Excel templates to schedule restaurant staff: weekly & monthly schedule with clopening and minor-hour alerts, FLSA overtime tracker, labor cost %, PTO. One-time $19.',
    keywords:
      'restaurant schedule template, restaurant staff schedule template, restaurant employee schedule template, staff rota template, rota template, shift schedule template excel, server schedule template, restaurant overtime tracker, restaurant labor cost calculator, labor cost percentage restaurant, new hire onboarding checklist restaurant, pto planner template, employee directory template, AI Chef Pro',
    ogImage: 'https://aichef.pro/og-staff-scheduling-kit.jpg',
  },

  schema: {
    productName: 'Restaurant Staff Scheduling Kit Pro',
    productDescription:
      '9 Excel templates with automatic formulas to schedule restaurant staff and manage overtime, labor cost, onboarding, PTO, performance reviews and an employee directory.',
    price: '19.00',
    priceValidUntil: '2026-12-31',
    // FAQPage schema: versiones CORTAS de las FAQ on-page (mismo patrón que el ES y los hermanos EN).
    faqs: [
      {
        q: 'Is there a free template for creating a schedule in Google Sheets?',
        a: "Yes, you'll find free weekly schedule templates for Google Sheets online. This kit is a set of 9 Excel workbooks built for restaurants: the schedule knows your shift codes and times and flags long shifts, clopenings, weeks over 40 hours and minors' shifts.",
      },
      {
        q: 'How do I create a schedule template?',
        a: 'Set up each shift once with a code, a start time and an end time, then type the codes into the weekly grid. The Restaurant Schedule Template works out the hours, the rest between shifts and the alerts.',
      },
      {
        q: 'Is it a time clock?',
        a: "No. It doesn't record clock-ins: it's for planning shifts, tracking overtime, controlling labor cost, onboarding and managing your team. It works alongside your POS or time-clock app.",
      },
      {
        q: 'Do the formulas calculate overtime automatically?',
        a: 'Yes. Hours over 40 in the workweek count as overtime at 1.5× (the FLSA rule), both editable, with an optional daily threshold for states such as California (8 hours).',
      },
      {
        q: 'How is it different from scheduling software?',
        a: 'Scheduling apps are a monthly subscription, usually per location. This kit is $19, a one-time payment with no subscription. There is no mobile app and no POS or time-clock integration.',
      },
      {
        q: 'Does it work in the UK?',
        a: 'Yes. The limits are editable cells: set 11 hours of rest between shifts, keep an eye on the 48-hour average week and enter 5.6 weeks of paid holiday.',
      },
      {
        q: 'What currency will I pay in?',
        a: 'The price is $19 USD. At checkout, Stripe can show the amount in your local currency. The templates have no currency symbol: you type amounts in your own currency.',
      },
      {
        q: 'Is there a money-back guarantee?',
        a: 'Yes. A full 30-day guarantee, 100% refund with no questions asked.',
      },
    ],
    breadcrumbName: 'Restaurant Staff Scheduling Kit Pro',
  },

  images: {
    // hero bg (6) — el set del ES salvo su portada (app de turnos en una tablet), sustituida por
    // manual-manager-briefing.jpg. gridGallery omitido: cae en `gallery`, como en el ES.
    gallery: [
      '/lovable-uploads/ai-gallery/staff-en-schedule-board.jpg',
      '/lovable-uploads/ai-gallery/staff-en-preshift.jpg',
      '/lovable-uploads/ai-gallery/tareas-gestion-personal-cocina.jpg',
      '/lovable-uploads/ai-gallery/tareas-gestion-personal-equipo.jpg',
      '/lovable-uploads/ai-gallery/staff-en-office-schedule.jpg',
      '/lovable-uploads/ai-gallery/tareas-gestion-personal-servicio.jpg',
    ],
    whyBg: '/lovable-uploads/ai-gallery/staff-en-office-schedule.jpg',
    buyBoxBg: '/lovable-uploads/ai-gallery/staff-en-schedule-board.jpg',
    ctaBg: '/lovable-uploads/ai-gallery/manual-manager-briefing.jpg',
  },

  hero: {
    badgeTone: 'gold',
    badge: 'FLSA overtime, clopening and minor-hour alerts built in',
    // D2: titlePre + titleGold = «Restaurant Staff Scheduling Kit Pro»; Forma B como los hermanos EN.
    titlePre: 'Restaurant Staff Scheduling ',
    titleGold: 'Kit Pro',
    titlePost: ': ',
    titleSubtitle: 'Restaurant Schedule Template & Staff Rota for Excel',
    description:
      '9 Excel templates with automatic formulas to manage shifts, overtime, labor cost, onboarding, PTO and performance reviews for your restaurant team. Schedule like a pro.',
    checkItems: [
      'Weekly and monthly schedule with alerts for long shifts, clopenings and minors',
      'Overtime tracker on the FLSA 40-hour week, with automatic cost',
      'Labor cost ratio with a traffic light: green, yellow, red',
      'Complete onboarding: hiring paperwork, training, equipment',
      'PTO, performance reviews and an employee directory',
    ],
    ctaLabel: 'BUY NOW — $19',
  },

  compatApps: {
    titleHtml: 'Print, Delegate and <span class="text-[#FFD700]">Control</span>',
    subtitleHtml:
      'Excel templates set up to print on US Letter. Compatible with Excel, LibreOffice and Numbers',
  },

  grid: {
    countGold: '9',
    headingRest: ' Staff Management Templates',
    subtitle:
      'Every template comes with automatic formulas and is built for how restaurants really work. Adjust it to your business and start scheduling.',
    // fourCols omitido → md:grid-cols-3 (9 tarjetas, como el ES)
    templates: [
      { icon: 'CalendarDays', title: 'Restaurant Schedule Template: Weekly & Monthly Staff Rota', desc: 'Weekly and monthly schedule with the alerts that matter: less than 10 hours between shifts (the "clopening" rule of Fair Workweek laws), shifts over 10 hours, weeks over 40 hours, days off, and minors\' shifts (under 16: no work after 7 PM, 9 PM from June 1 to Labor Day, 29 CFR 570.35; 16-17: state law). You set shift codes and times once.' },
      { icon: 'Clock', title: 'Overtime Tracker & Time Log (FLSA 40-Hour Week)', desc: 'Time log per employee with overtime by workweek: hours over 40 at 1.5× (both editable), plus an optional daily threshold for states such as California. Unapproved overtime still counts, because it still has to be paid, and an annual overtime budget per person shows who is close to it.' },
      { icon: 'Banknote', title: 'Restaurant Labor Cost Calculator (Payroll & Labor %)', desc: 'Labor cost-to-sales ratio with a traffic light by type of restaurant (fast casual, casual dining, fine dining, catering...). Payroll by pay period (weekly, biweekly, semimonthly or monthly), employer taxes as an editable estimate, and a staffing forecast per service.' },
      { icon: 'UserPlus', title: 'New Hire Onboarding Checklist', desc: '50 tasks in five blocks: hiring paperwork, required training, equipment and access, on-the-job training, and the introductory period. Each one with its deadline in days from the hire date, such as Form I-9 Section 1 by the first day of work.' },
      { icon: 'Palmtree', title: 'PTO & Vacation Planner', desc: 'Annual calendar by week with a real PTO balance. Requests, approvals, minimum coverage by position and a high-season warning. The entitlement is an editable cell: there is no federal paid vacation requirement in the US.' },
      { icon: 'Star', title: 'Employee Performance Review Form', desc: '10 key competencies for restaurants, scored 1-5. Quarterly history, goals for each period and an individual development plan.' },
      { icon: 'Users', title: 'Employee Directory & Expiry Tracker', desc: 'Complete staff database: position, employment type, FLSA status, pay type, only the last 4 digits of the SSN, contract end dates, food handler card and alcohol server certificate expiry alerts, and a flag for staff under 18.' },
      { icon: 'Megaphone', title: 'BONUS: Shift Handover Log (Manager Log Book)', desc: 'Handover between shifts: incidents, VIP reservations, pending tasks, low stock, absences and staff changes, a CASH COUNT against the POS Z report with the over/short, and TEMPERATURES at handover in °F, each unit with its min and max.' },
      { icon: 'Calculator', title: 'BONUS: Restaurant Staffing Calculator', desc: 'Works out how many people you need from covers per service, covers per employee, days open and demand peaks.' },
    ],
  },

  why: {
    headingPre: 'Why This ',
    headingGold: 'Kit',
    headingPost: '?',
    subtitle:
      "These aren't generic HR templates. They're tools designed by a chef who has worked in kitchens since the age of 17 and has been a restaurant consultant since 2010.",
    reasons: [
      { icon: 'Utensils', title: 'Built for Restaurants, Not Generic HR', desc: 'Designed for restaurants, hotels and catering: split shifts, doubles, services, back of house and front of house, extra shifts on the weekend. Not generic HR templates.' },
      { icon: 'Calculator', title: 'Real Formulas', desc: 'Labor cost, overtime by workweek, covers per employee and a staffing forecast per service, all calculated automatically. Not theory: numbers.' },
      { icon: 'ShieldCheck', title: 'Labor Rules, With the Exact Citation', desc: 'Each legal alert cites its rule: overtime after 40 hours in a workweek (FLSA, 29 U.S.C. 207), rest between shifts from Fair Workweek laws (10 hours in Oregon and Seattle, 11 for fast food in New York City) and hour limits for minors under 16 (29 CFR 570.35). The 10 h long-shift alert and the 80 h overtime budget are kit defaults you can change. Every threshold is an editable cell, because state and city rules vary. A planning tool, not legal advice.' },
      { icon: 'RefreshCw', title: 'Scheduling Apps Charge Every Month, Per Location. This Is $19, Once', desc: 'The same planning tools as a scheduling subscription, in Excel, for a one-time payment. No subscription and no per-user fees.' },
    ],
    // Pastillas del ES (orden incluido) sin Google Sheets hasta el test real (SPEC §6, §9); «A4» → US Letter.
    compatLabel: 'Compatible with:',
    compatPills: [
      { label: 'Microsoft Excel', highlight: true },
      { label: 'LibreOffice' },
      { label: 'Ready to print on US Letter' },
      { label: 'Apple Numbers' },
    ],
  },

  authorBio:
    'CEO of AI Chef Pro and founder of ChefBusiness Group. In kitchens since the age of 17 and a restaurant consultant since 2010. A specialist in managing restaurant and hotel teams, he has designed staff scheduling systems for hundreds of restaurants.',
  // authorBadges omitido → ui.authorBadgesDefault de i18n/tienda/en.json

  bonus: {
    headingPre: 'Exclusive ',
    headingGold: 'Bonuses',
    subtitle:
      'Besides the 7 core templates, you get these extra resources — worth $38',
    items: [
      {
        icon: 'Megaphone',
        label: 'BONUS 1',
        title: 'Shift Handover Log (Manager Log Book)',
        value: '$19',
        desc: 'The template that makes sure no shift starts blind. Incidents, VIP reservations, pending tasks, low stock, staff absences, a cash count (opening float, cash counted and cash sales from the POS Z report) and temperatures at handover, the exact moment food safety changes hands.',
        image: '/lovable-uploads/ai-gallery/tareas-gestion-personal-equipo.jpg',
      },
      {
        icon: 'Calculator',
        label: 'BONUS 2',
        title: 'Restaurant Staffing Calculator',
        value: '$19',
        desc: 'Works out how many people you need from your covers per service, days open, covers per employee and demand peaks. Stop being overstaffed or understaffed.',
        image: '/lovable-uploads/ai-gallery/staff-en-office-schedule.jpg',
      },
    ],
  },

  buyBox: {
    ctaLabel: 'YES, I WANT THE SCHEDULING KIT — $19',
  },

  guarantee: {
    // headingPre por defecto = ui.guaranteeHeadingPreDefault («Satisfaction Guarantee »).
    text:
      "If the templates don't help you manage your restaurant team better, we'll refund 100% of your money. No questions, no hassle.",
    stats: [
      { number: '30', label: 'Day guarantee' },
      { number: '100%', label: 'Money back' },
      { number: '0', label: 'Awkward questions' },
    ],
  },

  // FAQ on-page (acordeón): People Also Ask de la SPEC §6 + las 6 del ES adaptadas (registro horario →
  // «Is it a time clock?», horas extra FLSA/CA, cualquier restaurante, vs software, varios locales con la
  // licencia de la tienda EN, garantía) + UK + moneda y suscripción (como los hermanos EN).
  faqs: [
    {
      q: 'Is there a free template for creating a schedule in Google Sheets?',
      a: "Yes. You'll find free weekly schedule templates for Google Sheets online, and they're fine for a simple grid of names and days. This kit is something else: 9 Excel (.xlsx) workbooks built for restaurants. The schedule knows your shift codes and times, adds up the hours and flags long shifts, less than 10 hours between shifts, weeks over 40 hours and shifts for minors, and it comes with the overtime, labor cost, onboarding and PTO templates around it, for a one-time $19.",
    },
    {
      q: 'How do I create a schedule template?',
      a: 'Set up your shifts once and reuse them every week. In the Shifts tab of the Restaurant Schedule Template, each shift has a code, a start time and an end time (AM from 7 AM to 3 PM, PM from 3 to 11 PM, SP for a split shift, DBL for a double...). Then you type the codes into the weekly grid, and the sheet works out the hours, the rest between shifts and the alerts. Change a shift\'s times in the Shifts tab and the schedule updates.',
    },
    {
      q: 'How do I make a schedule in a spreadsheet?',
      a: 'Put your team in rows and the days of the week in columns, use a short code for each shift and keep the start and end times in a separate table, so the sheet can add up hours per person and per week. Then add the checks: hours over 40 (overtime), rest between a closing and an opening shift, and days off. The Restaurant Schedule Template comes set up exactly that way, with a weekly and a monthly view.',
    },
    {
      q: 'Is it a time clock?',
      a: "No. This kit doesn't record clock-ins: for that you need your POS or a time-clock app. It's for PLANNING shifts, tracking overtime, controlling labor cost, onboarding and managing your team. You can type the clock-in and clock-out times from your time clock into the Overtime Tracker, and it works out the overtime and what it costs. Keep those records: under the FLSA, payroll records are kept for 3 years and time cards for 2 (29 CFR 516.5-516.6).",
    },
    {
      q: 'Do the formulas calculate overtime automatically?',
      a: "Yes. The Overtime Tracker adds up each person's hours by workweek and counts everything over 40 as overtime at 1.5× the regular rate, the FLSA rule. Both numbers are editable cells, and there is an optional daily threshold for states with daily overtime (California: over 8 hours in a day). Overtime that wasn't approved still counts, because it still has to be paid. If you take a tip credit, remember that overtime is calculated on the full minimum wage, not on the cash wage.",
    },
    {
      q: 'Does it work for any type of restaurant?',
      a: "Yes. The templates are built for foodservice in general: casual dining, fine dining, fast casual, hotel restaurants, catering, cafés, bars and ghost kitchens, from one location to a group. The labor cost traffic light has its own target for each of 10 concepts, so a fine-dining restaurant isn't judged against a quick-service benchmark.",
    },
    {
      q: 'How is it different from scheduling software?',
      a: 'Scheduling and HR apps are a monthly subscription, usually per location. This kit is $19, a one-time payment with no subscription, and you can customize 100% of it. What it is not: there is no mobile app for your staff, no shift-swap requests or notifications, and no POS or time-clock integration.',
    },
    {
      q: 'Can I use it for several locations or with my clients?',
      a: "Yes. One purchase covers one business with all of its locations, which makes it a good fit for restaurant groups and multi-unit operators. If you are a consultant, you can use the templates with your clients, but you can't hand them copies: each business buys its own.",
    },
    {
      q: 'Does it work in the UK?',
      a: 'Yes. The limits live in editable cells, so you set the UK figures once: call it your rota, set the minimum rest between shifts to 11 hours, keep an eye on the 48-hour average week and enter 39 calendar days (5.6 weeks of paid holiday) in the PTO planner. The UK has no legal overtime premium, so set the multiplier to what your contracts say, and put your own employer cost in its cell (employer National Insurance is 15% above £5,000 a year, plus a 3% pension contribution).',
    },
    {
      q: 'What currency will I pay in?',
      a: 'The price is $19 USD, a one-time payment. At checkout, Stripe can show the amount in your local currency (for example GBP, EUR, CAD or AUD) and converts it for you. The templates themselves have no currency symbol: you type amounts in your own currency.',
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
    heading: 'Stop Improvising How You Manage Your Team',
    subtitle:
      "9 professional templates to manage your staff for less than one hour of a labor consultant's time.",
    // D4: los valores de los bonos repiten los de bonus.items.
    items: [
      'Weekly and monthly schedule with clopening, overtime and minor-hour alerts',
      'Overtime tracker with automatic cost',
      'Monthly labor cost ratio with a traffic light',
      'New hire onboarding: 50 tasks, each with its deadline',
      'PTO planning with minimum coverage',
      'Performance reviews: 10 competencies, scored 1-5',
      'Employee directory with expiry dates and certificates',
      'BONUS: Shift Handover Log ($19)',
      'BONUS: Restaurant Staffing Calculator ($19)',
    ],
    ctaLabel: 'YES, I WANT THE SCHEDULING KIT — $19',
  },

  // Testimonios: traducción fiel de los 8 del ES (decisión de John, 25-sep-2026). Son del Kit Gestión de
  // Personal y Turnos, la edición española de este kit: por eso conservan sus nombres, negocios y cifras
  // (12 h de descanso, convenio, Madrid), y el subtítulo lo dice. Solo se pintan: NO alimentan el JSON-LD.
  testimonials: {
    subtitle:
      'General managers, HR directors and owners who already manage their teams with Kit Gestión de Personal y Turnos, the Spanish edition of this kit',
    items: [
      { name: 'David Ruiz', role: 'General Manager, casual restaurant (45 covers)', text: 'The shift schedule has changed my life. I used to do it by hand and there were always mistakes with rest periods. Now the alerts for the 12 hours of rest between shifts and for the hours each person is contracted for warn me automatically.', avatar: '/avatars/avatar-1.jpg' },
      { name: 'Carmen Delgado', role: 'HR Director, hospitality group (6 restaurants)', text: 'The onboarding template is amazing. 50 organized tasks: paperwork, HACCP, workplace safety, training, access. Onboarding time dropped from 2 weeks to 4 days in every unit.', avatar: '/avatars/avatar-2.jpg' },
      { name: 'Francisco Torres', role: 'Owner, 2 restaurants in Madrid', text: "I close the month and in five minutes I know my labor cost: the employer's social security contribution and the overtime premium in my collective agreement are cells I edit myself, and the traffic light uses the threshold for MY type of business, not a generic 30%.", avatar: '/avatars/avatar-3.jpg' },
      { name: 'Lucía Navarro', role: 'Head Chef, Mediterranean restaurant', text: "The overtime tracker is exactly what I needed. It calculates the cost automatically under our collective agreement and warns me when a cook is close to Spain's legal limit. We've avoided 3 fines.", avatar: '/avatars/avatar-4.jpg' },
      { name: 'Alberto Méndez', role: 'Director of Operations, restaurant chain', text: 'Vacation planning with minimum coverage by position is great. No more Augusts with 3 cooks when we need 6. We plan from January with the full picture.', avatar: '/avatars/avatar-5.jpg' },
      { name: 'Marta Jiménez', role: 'Labor consultant specializing in hospitality', text: "I recommend it to all my clients. The templates follow current Spanish labor rules: rest periods, maximum working hours, vacation. It's the best way to prevent fines from Spain's Labor Inspectorate.", avatar: '/avatars/avatar-6.jpg' },
      { name: 'Roberto Sánchez', role: 'Executive Chef, 5-star hotel (120 employees)', text: 'The performance review with 10 competencies scored 1-5 has made our quarterly reviews professional. The history shows how each team member is really progressing.', avatar: '/avatars/avatar-7.jpg' },
      { name: 'Enrique Vidal', role: 'General Manager, fine-dining restaurant (2 stars)', text: "The staffing calculator was an eye-opener. With the covers of our PEAK day, it told us that service needs 2 extra people, and that we didn't need to add permanent staff. The covers-per-employee ratio explains everything.", avatar: '/avatars/avatar-8.jpg' },
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

  // Etiqueta corta (el ES también abrevia: «KIT GESTIÓN PERSONAL»): el nombre completo no cabe en la barra móvil.
  stickyLabel: 'STAFF SCHEDULING KIT PRO — $19',
  // stickyVariant omitido → default 'v2', como el ES.

  footerLinks: [
    { href: '/en', label: 'aichef.pro' },
    { href: '/en/digital-products', label: 'Digital Products' },
    { href: '/en/digital-products/food-cost-templates', label: 'Food Cost Kit Pro' },
    { href: '/en/digital-products/restaurant-inventory-templates', label: 'Restaurant Inventory Kit Pro' },
    { href: '/en/digital-products/haccp-templates', label: 'HACCP Food Safety Kit Pro' },
    { href: '/en/digital-products/restaurant-financial-plan-templates', label: 'Restaurant Financial Plan Kit Pro' },
    { href: '/en/digital-products/ai-prompts-for-restaurants', label: 'Gastro Pro Prompts eBook' },
    { href: 'mailto:info@aichef.pro', label: 'Contact' },
  ],
  updateNote: 'Version 2.0 · October 2026',

  alreadyBought: {
    product: 'restaurant-schedule-templates',
    label: 'Already bought the kit? Get back into your dashboard',
  },
};

export default data;
