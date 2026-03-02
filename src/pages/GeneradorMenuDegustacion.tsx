import { useState, KeyboardEvent, useRef } from 'react';
import { useTranslation } from 'react-i18next';
import { Helmet } from 'react-helmet-async';
import { Link } from 'react-router-dom';
import jsPDF from 'jspdf';
import ModernHeader from '@/components/ModernHeader';
import ModernFooter from '@/components/ModernFooter';
import { Button } from '@/components/ui/button';
import { Badge } from '@/components/ui/badge';
import { useLanguage } from '@/hooks/useLanguage';
import { Sparkles, RotateCcw, Copy, CheckCircle, ArrowRight, Printer, X, FileDown } from 'lucide-react';
import HeroSocialProof from '@/components/HeroSocialProof';
import OtherFreeTools from '@/components/OtherFreeTools';
import PricingPlans from '@/components/PricingPlans';

const LANG_SLUGS: Record<string, string> = {
  es: '/generador-menu-degustacion',
  en: '/en/tasting-menu-generator',
  fr: '/fr/generateur-menu-degustation',
  de: '/de/degustationsmenu-generator',
  it: '/it/generatore-menu-degustazione',
  pt: '/pt/gerador-menu-degustacao',
  nl: '/nl/proefmenu-generator',
};

const HUB_SLUGS: Record<string, string> = {
  es: '/herramientas-gratuitas',
  en: '/en/free-tools-restaurants',
  fr: '/fr/outils-gratuits-restaurant',
  de: '/de/kostenlose-tools-restaurant',
  it: '/it/strumenti-gratuiti-ristorante',
  pt: '/pt/ferramentas-gratuitas-restaurante',
  nl: '/nl/gratis-tools-restaurant',
};

// ─── Season ingredient suggestions ───────────────────────────────────────────

const SEASON_SUGGESTIONS: Record<string, Record<string, string[]>> = {
  es: {
    '0': ['espárrago', 'guisante', 'fresa', 'cordero lechal', 'alcachofa', 'cebolla tierna'],
    '1': ['tomate', 'pimiento rojo', 'bonito del norte', 'melocotón', 'berenjena', 'flor de calabacín'],
    '2': ['seta porcini', 'trufa negra', 'caza menor', 'manzana', 'castaña', 'lubina'],
    '3': ['cardo', 'bacalao', 'naranja sanguina', 'ostra', 'rabo de toro', 'berberecho'],
  },
  en: {
    '0': ['asparagus', 'peas', 'strawberry', 'spring lamb', 'artichoke', 'spring onion'],
    '1': ['tomato', 'red pepper', 'sea bream', 'peach', 'aubergine', 'courgette flower'],
    '2': ['porcini', 'black truffle', 'venison', 'apple', 'chestnut', 'sea bass'],
    '3': ['cardoon', 'salt cod', 'blood orange', 'oyster', 'oxtail', 'clam'],
  },
};

// ─── Hash helpers ─────────────────────────────────────────────────────────────

function strHash(str: string): number {
  let h = 0;
  for (let i = 0; i < str.length; i++) {
    h = (Math.imul(31, h) + str.charCodeAt(i)) | 0;
  }
  return Math.abs(h);
}

function pick<T>(arr: T[], seed: number): T {
  return arr[seed % arr.length];
}

function cap(s: string): string {
  return s.charAt(0).toUpperCase() + s.slice(1);
}

// ─── Course slot types ────────────────────────────────────────────────────────

type Slot = 'bocado' | 'frio' | 'caliente' | 'pescado' | 'carne' | 'caza' | 'quesos' | 'prepostre' | 'postre';

const SLOTS_BY_COUNT: Record<number, Slot[]> = {
  5: ['bocado', 'frio', 'pescado', 'carne', 'postre'],
  7: ['bocado', 'frio', 'caliente', 'pescado', 'carne', 'prepostre', 'postre'],
  10: ['bocado', 'bocado', 'frio', 'frio', 'caliente', 'pescado', 'carne', 'quesos', 'prepostre', 'postre'],
  12: ['bocado', 'bocado', 'bocado', 'frio', 'frio', 'caliente', 'pescado', 'caza', 'carne', 'quesos', 'prepostre', 'postre'],
};

// ─── Template data (ES + EN) ──────────────────────────────────────────────────

type Tpl = (a: string, b: string) => string;

const NOMBRES_ES: Record<Slot, Tpl[]> = {
  bocado: [
    (a) => `Bienvenida de ${a}`,
    (a) => `${cap(a)} en un mordisco`,
    (a) => `El primer gesto: ${a}`,
    (a) => `Preludio de ${a}`,
    (a) => `La apertura — ${a}`,
  ],
  frio: [
    (a) => `${cap(a)} en frío`,
    (a, b) => `Tartar de ${a} con ${b}`,
    (a) => `${cap(a)} marinado`,
    (a) => `El silencio de ${a}`,
    (a) => `Crudité de ${a}`,
  ],
  caliente: [
    (a) => `La calidez de ${a}`,
    (a) => `Crema de ${a}`,
    (a) => `${cap(a)} al vapor`,
    (a, b) => `${cap(a)} con ${b} tibio`,
    (a) => `Sopa de ${a}`,
  ],
  pescado: [
    (a) => `Del mar: ${a}`,
    (a) => `${cap(a)} y su esencia marina`,
    (a, b) => `${cap(a)} con ${b}`,
    (a) => `La travesía de ${a}`,
    (a) => `El litoral — ${a}`,
  ],
  carne: [
    (a) => `La tierra en ${a}`,
    (a) => `${cap(a)} al calor de la brasa`,
    (a) => `El reposo de ${a}`,
    (a) => `Del pasto al paladar: ${a}`,
    (a) => `Corazón de ${a}`,
  ],
  caza: [
    (a) => `El bosque en ${a}`,
    (a) => `Silvestre: ${a}`,
    (a) => `Del monte al plato — ${a}`,
    (a) => `La caza: ${a}`,
    (a, b) => `${cap(a)} y ${b}`,
  ],
  quesos: [
    (_a, b) => `El rebao y ${b}`,
    (a) => `Quesos con ${a} de temporada`,
    (a) => `La tabla — ${a}`,
    (a, b) => `${cap(a)} y queso con ${b}`,
    () => `Mundo lácteo: selección artesanal`,
  ],
  prepostre: [
    (a) => `El puente dulce — ${a}`,
    (a) => `${cap(a)} refrescante`,
    (a) => `La pausa de ${a}`,
    (a) => `Transición: ${a}`,
    (a) => `El limpiador — ${a}`,
  ],
  postre: [
    (a) => `El epílogo de ${a}`,
    (a) => `${cap(a)} dulce: el broche`,
    (a) => `La memoria de ${a}`,
    (a, b) => `${cap(a)} y ${b} en postre`,
    (a) => `El cierre — ${a}`,
  ],
};

const DESCRIPCIONES_ES: Record<Slot, Tpl[]> = {
  bocado: [
    (a) => `Un solo bocado que concentra la esencia de ${a}. Temperatura controlada, sabor que abre el apetito y prepara el paladar para el viaje.`,
    (a) => `${cap(a)} transformado en una pieza delicada que anuncia el concepto del menú y despierta la curiosidad del comensal.`,
    (a) => `Una sola cucharada basta: ${a} concentrado, textura sorprendente y el aroma que lo invade todo. Bienvenidos al viaje.`,
    (a) => `El saludo de la casa. ${cap(a)} en su estado más puro — mínima intervención, máxima honestidad. El primer mensaje.`,
    (a, b) => `Miniatura donde ${a} y ${b} protagonizan un momento de sorpresa. Elaborado con técnica precisa, ligero e intrigante.`,
  ],
  frio: [
    (a) => `${cap(a)} servido en su temperatura óptima, con un dressing que realza su pureza. Sin fuego, sin prisa: solo producto y técnica de frío.`,
    (a) => `${cap(a)} marinado 24 horas y cortado al momento. Un plato que habla del tiempo, la paciencia y el respeto por el producto.`,
    (a, b) => `Contraste donde ${a} frío dialoga con ${b}. Acidez equilibrada, textura cruda que revela matices que el calor ocultaría.`,
    (a) => `Carpaccio de ${a} con aceite de primera cosecha y flor de sal. La simplicidad como declaración de principios gastronómicos.`,
    (a) => `Tartar de ${a} con vinagreta de temporada. La textura cruda del producto revela matices que el calor ocultaría.`,
  ],
  caliente: [
    (a) => `Consomé de ${a} trabajado durante horas hasta la transparencia perfecta. Un caldo que limpia, calienta y emociona.`,
    (a) => `${cap(a)} cocinado a baja temperatura con sus propios jugos. La caramelización exterior contrasta con la ternura interior.`,
    (a) => `Crema aterciopelada de ${a} con un toque de aceite especiado. Textura sedosa que envuelve el paladar y prepara los pases siguientes.`,
    (a) => `${cap(a)} al vapor durante el tiempo justo: la clorofila viva, el sabor puro y la textura entre el crujiente y lo tierno.`,
    (a, b) => `Estofado ligero de ${a} con ${b}. Un plato que reconforta sin pesar, que abraza sin agotar.`,
  ],
  pescado: [
    (a) => `${cap(a)} con punto de cocción exacto — carne nacarada que cede al primer contacto, caldo de sus propias espinas y hierbas de litoral.`,
    (a) => `El mar en su esplendor. ${cap(a)} a la plancha sobre fuego vivo: piel crujiente y jugosidad interior preservada al milímetro.`,
    (a, b) => `Ceviche de ${a} con leche de tigre y ${b}. La acidez equilibra la grasa natural del pescado con elegancia.`,
    (a) => `${cap(a)} confitado en aceite de oliva virgen a 65°C durante 12 minutos. Textura mantecosa, sabor del Mediterráneo en estado puro.`,
    (a, b) => `Suquet de ${a} con ${b} confitado y un aire de azafrán. La tradición marinera reinterpretada sin perder su alma.`,
  ],
  carne: [
    (a) => `${cap(a)} madurado y cocinado a 55°C durante 48 horas. Un mordisco que concentra semanas de paciencia y el mejor sabor de la tierra.`,
    (a) => `Pieza de ${a} glaseada en su propio jugo reducido, con guarnición de temporada. Se deshace sin esfuerzo, umami que persiste.`,
    (a) => `${cap(a)} a la brasa de carbón de encina. La costra caramelizada guarda un interior rosado, tierno y lleno del sabor del producto.`,
    (a, b) => `Guiso de ${a} cocinado lentamente con ${b}. Un plato que necesita horas y recompensa cada minuto de espera.`,
    (a) => `${cap(a)} en dos servicios: el medallón en cocción perfecta y un caldo de sus huesos tostados servido en pequeña taza.`,
  ],
  caza: [
    (a) => `${cap(a)} de caza mayor, madurado y cocinado a fuego lento con hierbas silvestres. El sabor del monte en una pieza de intensidad memorable.`,
    (a, b) => `El salvaje de temporada: ${a} con salsa de bayas del bosque y ${b}. Profundidad de sabor inigualable, el monte en el plato.`,
    (a) => `${cap(a)} escabechado con vinagre de jerez envejecido. La acidez domestica la potencia de la caza, creando un equilibrio sorprendente.`,
    (a, b) => `Taco de ${a} bridado y confitado, servido sobre ${b} y salsa de civet. La técnica francesa al servicio del producto ibérico.`,
  ],
  quesos: [
    (a) => `Selección artesanal: un fresco de cabra, un semicurado de oveja y uno curado de vaca en cueva. Acompañados de ${a} para equilibrar.`,
    (a, b) => `Tosta de queso azul con ${a} caramelizado y ${b}. La grasa del queso encuentra en el dulce el contrapunto perfecto.`,
    (a) => `Queso artesanal de proximidad con láminas de ${a} y miel de flores. Minimalismo que deja hablar al producto sin interferencias.`,
    (a, b) => `${cap(a)} gelificado sobre queso curado de vaca con ${b}. Un bocado que une dulce y salado en equilibrio de texturas.`,
  ],
  prepostre: [
    (a) => `${cap(a)} en granizado ligero que limpia el paladar de la carne y lo prepara para lo dulce. Acidez justa, temperatura contrastante.`,
    (a) => `Sorbete de ${a} con unas gotas de licor artesanal. Frescor que actúa como bisagra entre el mundo salado y el postre.`,
    (a) => `${cap(a)} en textura mousse ligera, con un shot de infusión de hierbas. El prepostre que siempre hace dudar si pedir más.`,
    (a, b) => `Crema helada de ${a} sobre mermelada de ${b}. La suavidad del frío, el contraste del ácido: preparación que revitaliza.`,
  ],
  postre: [
    (a) => `${cap(a)} en múltiples texturas: gelificado, en polvo y en helado artesanal. Un postre que agota las posibilidades del ingrediente con elegancia.`,
    (a) => `Coulant de chocolate negro con corazón de ${a} caliente. La temperatura, la textura y la sorpresa en un solo momento memorable.`,
    (a, b) => `Milhojas de ${a} con crema Diplomática y ${b}. El clásico reinterpretado, ligero y sin renuncia a la satisfacción.`,
    (a) => `Bizcocho de ${a} cocinado al vapor, servido con helado de leche cruda y caramelo salado. La infancia revisitada desde la técnica.`,
    (a) => `Tarta de ${a} con base de galleta tostada y glaseado espejo. La perfección técnica al servicio del placer más sencillo.`,
  ],
};

const NOMBRES_EN: Record<Slot, Tpl[]> = {
  bocado: [
    (a) => `Welcome bite — ${a}`,
    (a) => `${cap(a)} in one bite`,
    (a) => `The opening: ${a}`,
    (a) => `Prelude of ${a}`,
    (a) => `First impression — ${a}`,
  ],
  frio: [
    (a) => `${cap(a)} cold`,
    (a, b) => `Tartare of ${a} with ${b}`,
    (a) => `${cap(a)} marinated`,
    (a) => `The silence of ${a}`,
    (a) => `Raw ${a}`,
  ],
  caliente: [
    (a) => `The warmth of ${a}`,
    (a) => `${cap(a)} cream`,
    (a) => `Steamed ${a}`,
    (a, b) => `${cap(a)} with warm ${b}`,
    (a) => `${cap(a)} broth`,
  ],
  pescado: [
    (a) => `From the sea: ${a}`,
    (a) => `${cap(a)} and the ocean`,
    (a, b) => `${cap(a)} with ${b}`,
    (a) => `The voyage of ${a}`,
    (a) => `Coastal — ${a}`,
  ],
  carne: [
    (a) => `The earth in ${a}`,
    (a) => `${cap(a)} over the embers`,
    (a) => `The rest of ${a}`,
    (a) => `From pasture to palate: ${a}`,
    (a) => `Heart of ${a}`,
  ],
  caza: [
    (a) => `The forest in ${a}`,
    (a) => `Wild: ${a}`,
    (a) => `From the woods — ${a}`,
    (a) => `Game: ${a}`,
    (a, b) => `${cap(a)} and ${b}`,
  ],
  quesos: [
    (_a, b) => `Cheese and ${b}`,
    (a) => `Selection with ${a}`,
    (a) => `The board — ${a}`,
    (a, b) => `${cap(a)} and aged cheese with ${b}`,
    () => `Artisan cheese selection`,
  ],
  prepostre: [
    (a) => `The sweet bridge — ${a}`,
    (a) => `Refreshing ${a}`,
    (a) => `The pause of ${a}`,
    (a) => `Transition: ${a}`,
    (a) => `The palate cleanser — ${a}`,
  ],
  postre: [
    (a) => `The epilogue of ${a}`,
    (a) => `Sweet ${a}: the finale`,
    (a) => `The memory of ${a}`,
    (a, b) => `${cap(a)} and ${b} dessert`,
    (a) => `The closing — ${a}`,
  ],
};

const DESCRIPCIONES_EN: Record<Slot, Tpl[]> = {
  bocado: [
    (a) => `A single bite concentrating the essence of ${a}. Controlled temperature, flavor that opens the appetite and prepares the palate for the journey.`,
    (a) => `${cap(a)} transformed into a delicate piece announcing the menu's concept, awakening the guest's curiosity before the experience begins.`,
    (a) => `One spoonful is enough: concentrated ${a}, a surprising texture and an aroma that fills everything. Welcome to the journey.`,
    (a) => `The house greeting. ${cap(a)} in its purest state — minimal intervention, maximum honesty. The first message of the kitchen.`,
    (a, b) => `A miniature where ${a} and ${b} share a moment of surprise. Precise technique, light and intriguing.`,
  ],
  frio: [
    (a) => `${cap(a)} served at its optimal temperature, with a dressing that enhances its purity. No fire, no rush: product and cold technique only.`,
    (a) => `${cap(a)} marinated for 24 hours and carved at the moment. A dish that speaks of time, patience and respect for the product.`,
    (a, b) => `Contrast where cold ${a} dialogues with ${b}. Balanced acidity, raw texture revealing nuances that heat would conceal.`,
    (a) => `${cap(a)} carpaccio with first-harvest olive oil and sea salt. Simplicity as a gastronomic statement of principles.`,
    (a) => `${cap(a)} tartare with seasonal vinaigrette. The raw texture of the product reveals nuances that heat would otherwise conceal.`,
  ],
  caliente: [
    (a) => `${cap(a)} consommé worked for hours until crystal clear. A broth that cleanses, warms and moves you.`,
    (a) => `${cap(a)} cooked at low temperature in its own juices. The caramelized exterior contrasts with the tender interior.`,
    (a) => `Velvety ${a} cream with a touch of spiced oil. Silky texture that envelops the palate and prepares for the following courses.`,
    (a) => `${cap(a)} steamed for exactly the right time: the chlorophyll alive, pure flavor and texture between crisp and tender.`,
    (a, b) => `Light stew of ${a} with ${b}. A dish that comforts without weighing, that embraces without exhausting.`,
  ],
  pescado: [
    (a) => `${cap(a)} with precise cooking — pearlescent flesh yielding at first contact, broth from its own bones and coastal herbs alongside.`,
    (a) => `The sea at its best. ${cap(a)} on a live flame: crispy skin and internal juiciness preserved to the millimeter.`,
    (a, b) => `${cap(a)} ceviche with tiger's milk and ${b}. The acidity balances the fish's natural fat with elegance.`,
    (a) => `${cap(a)} confit in virgin olive oil at 65°C for 12 minutes. Buttery texture, pure Mediterranean flavor.`,
    (a, b) => `${cap(a)} and ${b} suquet with saffron air. Maritime tradition reinterpreted without losing its soul.`,
  ],
  carne: [
    (a) => `${cap(a)} aged and cooked at 55°C for 48 hours. A bite concentrating weeks of patience and the finest land flavors.`,
    (a) => `${cap(a)} glazed in its own reduced jus with seasonal garnish. Falls apart effortlessly, umami that lingers.`,
    (a) => `${cap(a)} over oak charcoal embers. The caramelized crust guards a pink, tender, flavor-packed interior.`,
    (a, b) => `Slow-cooked ${a} with ${b}. A dish requiring hours, rewarding every minute of waiting.`,
    (a) => `${cap(a)} in two services: the perfect medallion and a broth from its roasted bones served in a small cup.`,
  ],
  caza: [
    (a) => `${cap(a)} aged and slow-cooked with wild herbs. The mountain flavor concentrated in a piece of unforgettable intensity.`,
    (a, b) => `The seasonal wild: ${a} with forest berry sauce and ${b}. Unmatched depth of flavor — the mountain on your plate.`,
    (a) => `${cap(a)} escabeche with aged sherry vinegar. The acidity tames the game's power, creating a surprising balance.`,
    (a, b) => `Braised ${a} confit, served over ${b} and civet sauce. French technique in service of Iberian product.`,
  ],
  quesos: [
    (a) => `Artisan selection: fresh goat, semi-cured sheep and cave-aged cow. Accompanied by ${a} to balance.`,
    (a, b) => `Toast of blue cheese with caramelized ${a} and ${b}. The fat of the cheese finds in the sweet its perfect counterpoint.`,
    (a) => `Local artisan cheese with slices of ${a} and wildflower honey. Minimalism that lets the product speak.`,
    (a, b) => `${cap(a)} gel over aged cow cheese with ${b}. A bite uniting sweet and savory in balance.`,
  ],
  prepostre: [
    (a) => `${cap(a)} granita that cleanses the palate of meat flavors and prepares for the sweet. Perfect acidity, contrasting temperature.`,
    (a) => `${cap(a)} sorbet with drops of artisan liqueur. Freshness acting as a bridge between savory and dessert.`,
    (a) => `${cap(a)} light mousse texture, with a shot of herb infusion. The pre-dessert that always makes you want more.`,
    (a, b) => `${cap(a)} ice cream over ${b} jam. The softness of cold, the contrast of acidity: a preparation that revitalizes.`,
  ],
  postre: [
    (a) => `${cap(a)} in multiple textures: jellied, powdered and artisan ice cream. A dessert exhausting the ingredient's possibilities with elegance.`,
    (a) => `Dark chocolate fondant with a hot ${a} heart. Temperature, texture and surprise in one unforgettable moment.`,
    (a, b) => `${cap(a)} mille-feuille with Diplomat cream and ${b}. The classic reinterpreted, light without sacrificing satisfaction.`,
    (a) => `Steamed ${a} sponge, served with raw milk ice cream and salted caramel. Childhood revisited through technique.`,
    (a) => `${cap(a)} tart with toasted shortbread base and mirror glaze. Technical perfection in service of the simplest pleasure.`,
  ],
};

const TECNICAS: Record<Slot, string[]> = {
  bocado: ['Esferificación básica', 'Mousse en cucharilla', 'Crujiente al horno', 'Tartaleta fina', 'Shot frío y caliente'],
  frio: ['Marinado en sal y azúcar', 'Vacío a baja temperatura', 'Carpaccio a máquina', 'Curado en casa', 'Tartar a cuchillo'],
  caliente: ['Cocción al vacío (sous vide)', 'Brasa a alta temperatura', 'Vapor suave', 'Reducción de fondo', 'Estofado lento'],
  pescado: ['Confitado en aceite 65°C', 'Plancha con piel', 'Ceviche con leche de tigre', 'Escabeche ligero', 'A la sal entera'],
  carne: ['Maduración en seco', 'Sous vide 48h + brasa final', 'Glaseado con fondo', 'Estofado a baja temperatura', 'Brasa de madera de frutal'],
  caza: ['Civet tradicional', 'Escabechado artesanal', 'Confitado en grasa de pato', 'Estofado con hierbas', 'Braseado con vino tinto'],
  quesos: ['Selección y maduración in situ', 'Marmelada artesanal', 'Gel de miel con especias', 'Lámina crujiente de fruta'],
  prepostre: ['Granizado en Pacojet', 'Sorbete sin azúcar añadido', 'Mousse con gelatina neutra', 'Esferificación con zumo'],
  postre: ['Glaseado espejo', 'Cocción en sifón', 'Helado mantecado artesanal', 'Coulant al minuto', 'Confit en aceite de oliva'],
};

// maridajes[estiloIdx]
const MARIDAJES: Record<Slot, string[][]> = {
  bocado: [
    ['Cava Brut Nature', 'Champagne Blanc de Blancs', 'Manzanilla en rama', 'Vermut artesanal'],
    ['Manzanilla de Sanlúcar', 'Cava Brut reserva', 'Sidra natural', 'Vermut rojo de barrica'],
    ['Sake Junmai-daiginjo', 'Riesling Kabinett', 'Txakoli fresco', 'Kir royal'],
    ['Agua con gas y cítricos', 'Kombucha de jengibre', 'Kéfir de agua', 'Zumo de manzana artesanal'],
    ['Txakoli fresco', 'Albariño joven', 'Cava rosado', 'Manzanilla pasada'],
  ],
  frio: [
    ['Albariño de Rías Baixas', 'Godello con crianza', 'Chardonnay sin roble', 'Fino en rama'],
    ['Verdejo de Rueda', 'Albariño clásico', 'Txakoli', 'Ribeiro blanco'],
    ['Grüner Veltliner', 'Muscadet Sèvre et Maine', 'Soave Classico', 'Picpoul de Pinet'],
    ['Vinho Verde monovarietal', 'Pinot Gris de Alsacia', 'Gavi di Gavi', 'Agua de mar filtrada'],
    ['Premier Cru Chablis', 'Vermentino de Cerdeña', 'Manzanilla de Sanlúcar', 'Palomino de Jerez'],
  ],
  caliente: [
    ['Viura con barrica', 'Blanco de Borgoña', 'Sake Junmai', 'Sidra natural vasca'],
    ['Rioja blanco fermentado en barrica', 'Chardonnay de Borgoña', 'Manzanilla pasada', 'Fino de Jerez'],
    ['Sake Daiginjo', 'Riesling Spätlese', 'Viognier del Ródano', 'Chenin Blanc de Loire'],
    ['Kombucha de hierbas', 'Infusión fría de flor de saúco', 'Agua de coco natural', 'Kvass casero'],
    ['Vermentino di Gallura', 'Fiano di Avellino', 'Greco di Tufo', 'Greco di Tufo'],
  ],
  pescado: [
    ['Rías Baixas Albariño', 'Premier Cru Chablis', 'Manzanilla de Sanlúcar', 'Palomino de Jerez'],
    ['Verdejo de Rueda', 'Albariño Rias Baixas', 'Blanco de Rueda', 'Txakoli'],
    ['Pinot Gris de Alsacia', 'White Burgundy', 'Assyrtiko de Santorini', 'Rías Baixas'],
    ['Vinho Verde', 'Muscadet', 'Picpoul de Pinet', 'Soave Classico'],
    ['Vermentino di Sardegna', 'Fiano di Avellino', 'Assyrtiko de Santorini', 'Greco di Tufo'],
  ],
  carne: [
    ['Ribera del Duero Reserva', 'Priorat viejo', 'Rioja Gran Reserva', 'Barolo'],
    ['Rioja Gran Reserva', 'Ribera del Duero Roble', 'Tempranillo de Toro', 'Garnacha vieja'],
    ['Syrah del Ródano', 'Malbec de Mendoza', 'Cabernet de Napa', 'Shiraz de Barossa'],
    ['Malbec sin sulfitos', 'Grenache Noir biodinámico', 'Pinotage sudafricano', 'Garnacha vieja sin sulfitos'],
    ['Primitivo di Manduria', 'Negroamaro de Puglia', 'Nerello Mascalese del Etna', 'Aglianico del Vulture'],
  ],
  caza: [
    ['Garnacha vieja de Aragón', 'Pinot Noir de Borgoña', 'Monastrell de Jumilla', 'Mencía de Bierzo'],
    ['Rioja Reserva antiguo', 'Garnacha de Campo de Borja', 'Toro crianza', 'Valdepeñas Reserva'],
    ['Syrah del Ródano Norte', 'Nebbiolo de Langhe', 'Sangiovese di Romagna', 'Xinomavro de Naoussa'],
    ['Pinot Noir de Alsacia', 'Gamay de Morgon', 'Lambrusco secco', 'Zweigelt austríaco'],
    ['Negroamaro', 'Primitivo di Manduria', 'Cannonau di Sardegna', 'Nero d\'Avola'],
  ],
  quesos: [
    ['Amontillado de Jerez', 'Riesling Spätlese', 'Oporto Tawny 10 años', 'Cava Brut con azúcar'],
    ['Oloroso seco de Jerez', 'Moscatel de Málaga', 'Oporto Ruby', 'Sidra de pera envejecida'],
    ['Sake Nigori', 'Vino de miel escandinavo', 'Trappist beer', 'Kombucha fermentada añeja'],
    ['Kombucha de flores', 'Zumo de uva natural', 'Kéfir de agua con miel', 'Cerveza de trigo artesana'],
    ['Marsala Superiore', 'Malvasia delle Lipari', 'Zibibbo di Pantelleria', 'Moscato d\'Asti'],
  ],
  prepostre: [
    ['Cava rosado Brut', 'Champagne rosé', 'Riesling Trockenbeerenauslese', 'Agua con gas'],
    ['Sidra de manzana natural', 'Cava rosado', 'Agua de rosas artesanal', 'Moscatel seco'],
    ['Plum wine japonés', 'Umeshu ligero', 'Sake Nigori', 'Kombucha de hibisco'],
    ['Zumo de fruta de temporada', 'Kombucha de frutos rojos', 'Agua de coco', 'Infusión fría de hierbas'],
    ['Limoncello artesano diluido', 'Vino de naranja de Sicilia', 'Malvasia seco', 'Moscato Secco'],
  ],
  postre: [
    ['Moscatel de Alejandría', 'Sauternes', 'Oporto LBV', 'PX de Montilla-Moriles'],
    ['Moscatel de Valencia', 'Pedro Ximénez', 'Oporto Vintage', 'Málaga dulce'],
    ['Sake Nigori dulce', 'Baijiu suave', 'Icewine canadiense', 'Tokaji Aszú 5 puttonyos'],
    ['Zumo de fruta tropical', 'Kombucha de vainilla', 'Cacao de origen cálido', 'Horchata artesanal'],
    ['Passito di Pantelleria', 'Vin Santo Toscano', 'Marsala Fine', 'Moscato d\'Asti'],
  ],
};

// ─── Menu name & concept generators ──────────────────────────────────────────

const ESTILOS_ES = ['Vanguardista', 'Tradicional', 'Fusión', 'Plant-based', 'Mediterráneo'];
const ESTILOS_EN = ['Avant-garde', 'Traditional', 'Fusion', 'Plant-based', 'Mediterranean'];
const TEMPORADAS_ES = ['Primavera', 'Verano', 'Otoño', 'Invierno'];
const TEMPORADAS_EN = ['Spring', 'Summer', 'Autumn', 'Winter'];

const MENU_NAME_PREFIXES_ES = [
  'Raíces', 'Diálogo', 'Memoria', 'Silencio', 'Estaciones', 'Terroir', 'Travesía', 'Génesis',
];
const MENU_NAME_PREFIXES_EN = [
  'Roots', 'Dialogue', 'Memory', 'Silence', 'Seasons', 'Terroir', 'Journey', 'Genesis',
];

const CONCEPTS_ES = [
  (ings: string[], estilo: string, temp: string) =>
    `Un viaje de ${ings.length} ingredientes estrella a través del ${estilo.toLowerCase()} más honesto. La ${temp.toLowerCase()} como guía, el producto como protagonista.`,
  (ings: string[], estilo: string, temp: string) =>
    `${estilo} gastronómico que celebra los mejores productos de la ${temp.toLowerCase()}. Cada pase es una conversación entre el chef y el comensal.`,
  (ings: string[], estilo: string, temp: string) =>
    `La esencia de la ${temp.toLowerCase()} concentrada en cada pase. Técnica ${estilo.toLowerCase()}, ingredientes de primera: ${ings.slice(0, 3).join(', ')}.`,
  (ings: string[], estilo: string) =>
    `Una propuesta ${estilo.toLowerCase()} que teje ${ings.length} ingredientes estrella en un relato de sabores coherente y emocionante.`,
];

const CONCEPTS_EN = [
  (ings: string[], style: string, season: string) =>
    `A journey through ${ings.length} star ingredients in the most honest ${style.toLowerCase()} spirit. ${season} as guide, product as protagonist.`,
  (ings: string[], style: string, season: string) =>
    `${style} gastronomy celebrating the finest ${season.toLowerCase()} produce. Each course is a conversation between chef and guest.`,
  (ings: string[], style: string, season: string) =>
    `The essence of ${season.toLowerCase()} concentrated in every course. ${style} technique, finest ingredients: ${ings.slice(0, 3).join(', ')}.`,
  (ings: string[], style: string) =>
    `A ${style.toLowerCase()} proposal weaving ${ings.length} star ingredients into a coherent, moving flavour narrative.`,
];

// ─── Core generation ──────────────────────────────────────────────────────────

export interface CourseResult {
  numero: number;
  nombre: string;
  descripcion: string;
  tecnica: string;
  maridaje: string;
}

export interface MenuResult {
  nombreMenu: string;
  descripcionConcepto: string;
  pases: CourseResult[];
}

function generateMenu(
  ingredientes: string[],
  numPases: number,
  estiloIdx: number,
  temporadaIdx: number,
  restaurante: string,
  lang: string,
): MenuResult {
  if (ingredientes.length === 0) ingredientes = ['ingrediente'];
  const seed = strHash(ingredientes.join(',') + numPases + estiloIdx + temporadaIdx + restaurante + lang);
  const isEN = lang === 'en';

  const NOMBRES = isEN ? NOMBRES_EN : NOMBRES_ES;
  const DESCRIPCIONES = isEN ? DESCRIPCIONES_EN : DESCRIPCIONES_ES;
  const ESTILOS = isEN ? ESTILOS_EN : ESTILOS_ES;
  const TEMPORADAS = isEN ? TEMPORADAS_EN : TEMPORADAS_ES;
  const PREFIXES = isEN ? MENU_NAME_PREFIXES_EN : MENU_NAME_PREFIXES_ES;
  const CONCEPTS = isEN ? CONCEPTS_EN : CONCEPTS_ES;

  const slots = SLOTS_BY_COUNT[numPases] || SLOTS_BY_COUNT[7];

  const pases: CourseResult[] = slots.map((slot, i) => {
    const ing = ingredientes[i % ingredientes.length];
    const ing2 = ingredientes[(i + 1) % ingredientes.length] || ing;
    const s = seed + i * 13;

    return {
      numero: i + 1,
      nombre: pick(NOMBRES[slot], s)(ing, ing2),
      descripcion: pick(DESCRIPCIONES[slot], s + 3)(ing, ing2),
      tecnica: pick(TECNICAS[slot], s + 7),
      maridaje: pick(MARIDAJES[slot][estiloIdx] || MARIDAJES[slot][0], s + 11),
    };
  });

  const estilo = ESTILOS[estiloIdx] || ESTILOS[0];
  const temporada = TEMPORADAS[temporadaIdx] || TEMPORADAS[0];
  const prefix = pick(PREFIXES, seed + 99);
  const suffix = restaurante ? ` · ${restaurante}` : '';
  const nombreMenu = isEN
    ? `${prefix} — ${estilo} Tasting Menu${suffix}`
    : `${prefix} — Menú Degustación ${estilo}${suffix}`;

  const conceptFn = pick(CONCEPTS, seed + 77) as (...args: unknown[]) => string;
  const descripcionConcepto = conceptFn(ingredientes, estilo, temporada);

  return { nombreMenu, descripcionConcepto, pases };
}

// ─── Component ────────────────────────────────────────────────────────────────

export default function GeneradorMenuDegustacion() {
  const { t, i18n } = useTranslation();
  const { currentLanguage, getAppUrl } = useLanguage();
  const siteUrl = import.meta.env.VITE_SITE_URL || 'https://aichef.pro';
  const slug = LANG_SLUGS[currentLanguage] || LANG_SLUGS.es;
  const canonicalUrl = `${siteUrl}${slug}`;
  const lang = i18n.language?.split('-')[0] || 'es';
  const isEN = lang === 'en';

  const seo = t('toolDegustacion.seo', { returnObjects: true }) as Record<string, string>;
  const hero = t('toolDegustacion.hero', { returnObjects: true }) as Record<string, string>;
  const tool = t('toolDegustacion.tool', { returnObjects: true }) as Record<string, unknown>;
  const faqItems = t('toolDegustacion.faq', { returnObjects: true }) as Array<{ q: string; a: string }>;
  const ctaSection = t('toolDegustacion.cta_section', { returnObjects: true }) as Record<string, string>;

  const faqSchema = Array.isArray(faqItems) && faqItems.length > 0
    ? {
        '@context': 'https://schema.org',
        '@type': 'FAQPage',
        mainEntity: faqItems.map(f => ({
          '@type': 'Question',
          name: f.q,
          acceptedAnswer: { '@type': 'Answer', text: f.a },
        })),
      }
    : null;

  const estilos: string[] = Array.isArray(tool?.estilos) ? (tool.estilos as string[]) : [];
  const temporadas: string[] = Array.isArray(tool?.temporadas) ? (tool.temporadas as string[]) : [];
  const paseOptions: number[] = [5, 7, 10, 12];
  const rl = (tool?.result_labels || {}) as Record<string, string>;

  // Form state
  const [tags, setTags] = useState<string[]>([]);
  const [tagInput, setTagInput] = useState('');
  const [numPases, setNumPases] = useState(7);
  const [estiloIdx, setEstiloIdx] = useState(0);
  const [temporadaIdx, setTemporadaIdx] = useState(2); // Otoño default
  const [restaurante, setRestaurante] = useState('');
  const [result, setResult] = useState<MenuResult | null>(null);
  const [isGenerating, setIsGenerating] = useState(false);
  const [copied, setCopied] = useState(false);
  const tagInputRef = useRef<HTMLInputElement>(null);

  const hubSlug = HUB_SLUGS[lang] || HUB_SLUGS.es;
  const isValid = tags.length > 0;

  const seasonSuggestions = (SEASON_SUGGESTIONS[isEN ? 'en' : 'es']?.[temporadaIdx] || []) as string[];

  const addTag = (val: string) => {
    const clean = val.trim().toLowerCase();
    if (clean && !tags.includes(clean) && tags.length < 5) {
      setTags(prev => [...prev, clean]);
    }
    setTagInput('');
  };

  const removeTag = (i: number) => {
    setTags(prev => prev.filter((_, idx) => idx !== i));
  };

  const handleKeyDown = (e: KeyboardEvent<HTMLInputElement>) => {
    if (e.key === 'Enter' || e.key === ',') {
      e.preventDefault();
      if (tagInput.trim()) addTag(tagInput);
    } else if (e.key === 'Backspace' && !tagInput && tags.length > 0) {
      removeTag(tags.length - 1);
    }
  };

  const handleGenerate = () => {
    if (!isValid) return;
    setIsGenerating(true);
    setTimeout(() => {
      setResult(generateMenu(tags, numPases, estiloIdx, temporadaIdx, restaurante.trim(), lang));
      setIsGenerating(false);
    }, 900);
  };

  const handleRegenerate = () => {
    if (!isValid) return;
    setIsGenerating(true);
    setTimeout(() => {
      setResult(generateMenu(tags, numPases, estiloIdx, temporadaIdx, restaurante.trim() + Math.random(), lang));
      setIsGenerating(false);
    }, 700);
  };

  const handleReset = () => {
    setTags([]);
    setTagInput('');
    setNumPases(7);
    setEstiloIdx(0);
    setTemporadaIdx(2);
    setRestaurante('');
    setResult(null);
  };

  const handleCopyMenu = () => {
    if (!result) return;
    const text = [
      result.nombreMenu,
      '',
      result.descripcionConcepto,
      '',
      ...result.pases.map(p =>
        `${p.numero}. ${p.nombre}\n${p.descripcion}\nTécnica: ${p.tecnica}\nMaridaje: ${p.maridaje}`
      ),
    ].join('\n');
    navigator.clipboard.writeText(text).then(() => {
      setCopied(true);
      setTimeout(() => setCopied(false), 2000);
    });
  };

  const handlePrint = () => window.print();

  const downloadPDF = () => {
    if (!result) return;

    const t_pdf = (key: string) => (tool?.[key] as string) || '';
    const today = new Date().toLocaleDateString(lang, { year: 'numeric', month: '2-digit', day: '2-digit' });

    const doc = new jsPDF({ unit: 'mm', format: 'a4' });
    const W = 210;
    const MARGIN = 18;
    const CONTENT_W = W - MARGIN * 2;
    let y = 0;

    const checkPage = (needed: number) => {
      if (y + needed > 270) {
        doc.addPage();
        y = 18;
      }
    };

    // ── Header bar (dark indigo) ──────────────────────────────────────────────
    doc.setFillColor(49, 46, 129); // indigo-900
    doc.rect(0, 0, W, 22, 'F');
    doc.setFontSize(9);
    doc.setTextColor(199, 210, 254); // indigo-200
    doc.text('AI Chef Pro — aichef.pro', MARGIN, 9);
    doc.setFontSize(8);
    doc.setTextColor(165, 180, 252); // indigo-300
    doc.text(t_pdf('pdf_date_label') + ': ' + today, MARGIN, 16);
    // Restaurant name on right if provided
    if (restaurante.trim()) {
      doc.setFontSize(9);
      doc.setTextColor(224, 231, 255);
      doc.text(restaurante.trim(), W - MARGIN, 13, { align: 'right' });
    }

    y = 32;

    // ── Menu name ────────────────────────────────────────────────────────────
    doc.setFontSize(20);
    doc.setTextColor(31, 41, 55); // gray-800
    const nameLines = doc.splitTextToSize(result.nombreMenu, CONTENT_W);
    doc.text(nameLines, W / 2, y, { align: 'center' });
    y += nameLines.length * 9 + 4;

    // Sub-info line: N pases · Estilo · Temporada
    const estilosArr = (tool?.estilos as string[]) || [];
    const temporadasArr = (tool?.temporadas as string[]) || [];
    const estiloName = estilosArr[estiloIdx] || '';
    const temporadaName = temporadasArr[temporadaIdx] || '';
    const subInfo = `${numPases} ${t_pdf('pdf_label_courses')}  ·  ${estiloName}  ·  ${temporadaName}`;
    doc.setFontSize(9);
    doc.setTextColor(99, 102, 241); // indigo-500
    doc.text(subInfo, W / 2, y, { align: 'center' });
    y += 8;

    // Divider
    doc.setDrawColor(199, 210, 254);
    doc.setLineWidth(0.4);
    doc.line(MARGIN, y, W - MARGIN, y);
    y += 8;

    // ── Concept description ──────────────────────────────────────────────────
    doc.setFontSize(9.5);
    doc.setTextColor(75, 85, 99); // gray-600
    const conceptLines = doc.splitTextToSize(result.descripcionConcepto, CONTENT_W);
    doc.text(conceptLines, MARGIN, y);
    y += conceptLines.length * 5.5 + 6;

    // ── Star ingredients ────────────────────────────────────────────────────
    if (tags.length > 0) {
      doc.setFontSize(8);
      doc.setTextColor(99, 102, 241);
      doc.text(t_pdf('pdf_label_ingredientes') + ':', MARGIN, y);
      y += 5;
      doc.setFontSize(8.5);
      doc.setTextColor(55, 65, 81);
      doc.text(tags.join('  ·  '), MARGIN + 2, y);
      y += 6;
    }

    // Divider
    doc.setDrawColor(199, 210, 254);
    doc.line(MARGIN, y, W - MARGIN, y);
    y += 8;

    // ── Courses ─────────────────────────────────────────────────────────────
    for (const pase of result.pases) {
      checkPage(40);

      // Course number circle (simulated as bold prefix)
      doc.setFontSize(9);
      doc.setTextColor(99, 102, 241);
      doc.text(`${pase.numero}.`, MARGIN, y);

      // Course name
      doc.setFontSize(12);
      doc.setTextColor(17, 24, 39); // gray-900
      const nameW = CONTENT_W - 8;
      const courseNameLines = doc.splitTextToSize(pase.nombre, nameW);
      doc.text(courseNameLines, MARGIN + 8, y);
      y += courseNameLines.length * 6 + 2;

      // Description
      doc.setFontSize(8.5);
      doc.setTextColor(75, 85, 99);
      const descLines = doc.splitTextToSize(pase.descripcion, CONTENT_W - 4);
      checkPage(descLines.length * 4.8 + 10);
      doc.text(descLines, MARGIN + 4, y);
      y += descLines.length * 4.8 + 3;

      // Técnica + Maridaje on same line
      doc.setFontSize(7.5);
      doc.setTextColor(107, 114, 128); // gray-500
      const tecLabel = (rl.tecnica || 'Técnica') + ': ';
      const marLabel = '  ·  ' + (rl.maridaje || 'Maridaje') + ': ';
      const tecLine = tecLabel + pase.tecnica + marLabel + pase.maridaje;
      const tecLines = doc.splitTextToSize(tecLine, CONTENT_W - 4);
      doc.text(tecLines, MARGIN + 4, y);
      y += tecLines.length * 4.5 + 6;

      // Light separator between courses
      doc.setDrawColor(229, 231, 235); // gray-200
      doc.setLineWidth(0.2);
      doc.line(MARGIN + 8, y, W - MARGIN - 8, y);
      y += 5;
    }

    // ── Footer ───────────────────────────────────────────────────────────────
    checkPage(16);
    y += 4;
    doc.setDrawColor(199, 210, 254);
    doc.setLineWidth(0.4);
    doc.line(MARGIN, y, W - MARGIN, y);
    y += 6;
    doc.setFontSize(7.5);
    doc.setTextColor(156, 163, 175); // gray-400
    doc.text(t_pdf('pdf_generated_by'), MARGIN, y);

    const date = new Date().toISOString().slice(0, 10);
    doc.save(`${t_pdf('pdf_filename')}-${date}.pdf`);
  };

  return (
    <div className="min-h-screen bg-white flex flex-col">
      <Helmet>
        <html lang={lang} />
        <title>{seo?.title || 'Generador Menú Degustación | AI Chef Pro'}</title>
        <meta name="description" content={seo?.description || ''} />
        {seo?.keywords && <meta name="keywords" content={seo.keywords} />}
        <link rel="canonical" href={canonicalUrl} />
        {Object.entries(LANG_SLUGS).map(([l, s]) => (
          <link key={l} rel="alternate" hrefLang={l} href={`${siteUrl}${s}`} />
        ))}
        {faqSchema && (
          <script type="application/ld+json">{JSON.stringify(faqSchema)}</script>
        )}
      </Helmet>

      <ModernHeader />

      <main className="flex-1">
        {/* ── Hero ── */}
        <section className="bg-gradient-to-b from-indigo-50 to-white py-16 px-4">
          <div className="max-w-3xl mx-auto text-center">
            <HeroSocialProof />
            <Badge className="bg-indigo-100 text-indigo-700 border-0 mb-4 px-3 py-1">
              {hero?.badge || 'Gratis — Sin registro'}
            </Badge>
            <h1 className="text-4xl md:text-5xl font-bold text-gray-900 mb-4 leading-tight">
              {hero?.h1 || 'Generador de Menú Degustación con IA'}
            </h1>
            <p className="text-lg text-gray-600 mb-8 max-w-2xl mx-auto">
              {hero?.subtitle || 'Selecciona tus ingredientes estrella y obtén al instante un menú degustación completo con nombre poético, descripción sensorial, técnica y maridaje.'}
            </p>
            <div className="flex flex-col sm:flex-row gap-3 justify-center">
              <Button
                className="bg-indigo-600 hover:bg-indigo-700 text-white px-6 py-3"
                onClick={() => document.getElementById('tool-section')?.scrollIntoView({ behavior: 'smooth' })}
              >
                <Sparkles className="w-4 h-4 mr-2" />
                {hero?.cta_tool || 'Crear mi menú degustación'}
              </Button>
              <Button variant="outline" className="border-indigo-600 text-indigo-600 hover:bg-indigo-50 px-6 py-3" asChild>
                <a href={getAppUrl()} target="_blank" rel="noopener noreferrer">
                  {hero?.cta_premium || 'Plan Premium →'}
                </a>
              </Button>
            </div>
          </div>
        </section>

        {/* ── Tool ── */}
        <section id="tool-section" className="py-16 px-4 bg-white">
          <div className="max-w-2xl mx-auto">
            <div className="bg-white border border-gray-200 rounded-2xl shadow-sm p-8">
              <div className="flex items-center gap-3 mb-8">
                <div className="w-10 h-10 rounded-xl bg-indigo-100 flex items-center justify-center">
                  <Sparkles className="w-5 h-5 text-indigo-600" />
                </div>
                <h2 className="text-xl font-bold text-gray-900">
                  {(tool?.title as string) || 'Diseña tu Menú Degustación'}
                </h2>
              </div>

              {/* Tags input — ingredientes */}
              <div className="mb-5">
                <label className="block text-sm font-semibold text-gray-700 mb-2">
                  {(tool?.ingredientes_label as string) || 'Ingredientes estrella (hasta 5)'} <span className="text-red-500">*</span>
                </label>
                <div
                  className="flex flex-wrap gap-2 border border-gray-300 rounded-lg px-3 py-2.5 focus-within:ring-2 focus-within:ring-indigo-500 focus-within:border-transparent cursor-text min-h-[52px]"
                  onClick={() => tagInputRef.current?.focus()}
                >
                  {tags.map((tag, i) => (
                    <span key={i} className="inline-flex items-center gap-1 bg-indigo-100 text-indigo-700 text-sm rounded-full px-3 py-1">
                      {tag}
                      <button onClick={() => removeTag(i)} className="text-indigo-400 hover:text-indigo-600 transition-colors">
                        <X className="w-3 h-3" />
                      </button>
                    </span>
                  ))}
                  {tags.length < 5 && (
                    <input
                      ref={tagInputRef}
                      type="text"
                      value={tagInput}
                      onChange={e => setTagInput(e.target.value)}
                      onKeyDown={handleKeyDown}
                      onBlur={() => { if (tagInput.trim()) addTag(tagInput); }}
                      placeholder={tags.length === 0 ? ((tool?.ingredientes_placeholder as string) || 'Ej: trufa negra') : ''}
                      className="flex-1 min-w-24 outline-none text-gray-900 text-sm bg-transparent"
                    />
                  )}
                </div>
                <p className="text-xs text-gray-500 mt-1">
                  {(tool?.ingredientes_hint as string) || 'Pulsa Enter o coma para añadir. Máximo 5.'}
                </p>

                {/* Season suggestions */}
                {tags.length < 5 && seasonSuggestions.length > 0 && (
                  <div className="mt-2 flex flex-wrap gap-1.5">
                    {seasonSuggestions
                      .filter(s => !tags.includes(s))
                      .map((s, i) => (
                        <button
                          key={i}
                          onClick={() => addTag(s)}
                          className="text-xs bg-gray-100 hover:bg-indigo-100 hover:text-indigo-700 text-gray-600 rounded-full px-2.5 py-1 transition-colors"
                        >
                          + {s}
                        </button>
                      ))}
                  </div>
                )}
              </div>

              {/* Número de pases */}
              <div className="mb-5">
                <label className="block text-sm font-semibold text-gray-700 mb-2">
                  {(tool?.pases_label as string) || 'Número de pases'}
                </label>
                <div className="grid grid-cols-4 gap-2">
                  {paseOptions.map(n => (
                    <button
                      key={n}
                      onClick={() => setNumPases(n)}
                      className={`py-2.5 rounded-lg text-sm font-semibold border transition-colors ${
                        numPases === n
                          ? 'bg-indigo-600 text-white border-indigo-600'
                          : 'bg-white text-gray-700 border-gray-300 hover:border-indigo-400 hover:text-indigo-600'
                      }`}
                    >
                      {n} {isEN ? 'courses' : 'pases'}
                    </button>
                  ))}
                </div>
              </div>

              {/* Estilo + Temporada */}
              <div className="grid grid-cols-1 sm:grid-cols-2 gap-5 mb-5">
                <div>
                  <label className="block text-sm font-semibold text-gray-700 mb-2">
                    {(tool?.estilo_label as string) || 'Estilo culinario'}
                  </label>
                  <select
                    value={estiloIdx}
                    onChange={e => setEstiloIdx(Number(e.target.value))}
                    className="w-full border border-gray-300 rounded-lg px-4 py-3 text-gray-900 bg-white focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:border-transparent"
                  >
                    {estilos.map((e, i) => (
                      <option key={i} value={i}>{e}</option>
                    ))}
                  </select>
                </div>
                <div>
                  <label className="block text-sm font-semibold text-gray-700 mb-2">
                    {(tool?.temporada_label as string) || 'Temporada'}
                  </label>
                  <select
                    value={temporadaIdx}
                    onChange={e => setTemporadaIdx(Number(e.target.value))}
                    className="w-full border border-gray-300 rounded-lg px-4 py-3 text-gray-900 bg-white focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:border-transparent"
                  >
                    {temporadas.map((t, i) => (
                      <option key={i} value={i}>{t}</option>
                    ))}
                  </select>
                </div>
              </div>

              {/* Nombre restaurante */}
              <div className="mb-6">
                <label className="block text-sm font-semibold text-gray-700 mb-2">
                  {(tool?.restaurante_label as string) || 'Nombre del restaurante (opcional)'}
                </label>
                <input
                  type="text"
                  value={restaurante}
                  onChange={e => setRestaurante(e.target.value)}
                  placeholder={(tool?.restaurante_placeholder as string) || 'Ej: El Jardín de Neptuno'}
                  className="w-full border border-gray-300 rounded-lg px-4 py-3 text-gray-900 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:border-transparent"
                />
              </div>

              <Button
                className="w-full bg-indigo-600 hover:bg-indigo-700 text-white py-3 text-base font-semibold"
                onClick={handleGenerate}
                disabled={!isValid || isGenerating}
              >
                {isGenerating ? (
                  <span className="flex items-center justify-center gap-2">
                    <span className="animate-spin rounded-full h-4 w-4 border-b-2 border-white" />
                    {(tool?.generating as string) || 'Tu menú está tomando forma...'}
                  </span>
                ) : (
                  <span className="flex items-center justify-center gap-2">
                    <Sparkles className="w-4 h-4" />
                    {(tool?.generate_btn as string) || 'Crear mi menú degustación'}
                  </span>
                )}
              </Button>
            </div>

            {/* ── Results ── */}
            {result && !isGenerating && (
              <div className="mt-8">
                {/* Action bar */}
                <div className="flex items-center justify-between mb-4 flex-wrap gap-2">
                  <h3 className="text-lg font-bold text-gray-900">{rl.menu_title || 'Menú Degustación'}</h3>
                  <div className="flex items-center gap-2">
                    <button
                      onClick={handleCopyMenu}
                      className="flex items-center gap-1.5 text-sm text-gray-600 hover:text-indigo-600 transition-colors px-3 py-1.5 border border-gray-200 rounded-lg"
                    >
                      {copied ? <CheckCircle className="w-4 h-4 text-green-600" /> : <Copy className="w-4 h-4" />}
                      <span className={copied ? 'text-green-600' : ''}>{copied ? (rl.copied || '¡Copiado!') : (rl.copy_menu || 'Copiar menú')}</span>
                    </button>
                    <button
                      onClick={handlePrint}
                      className="flex items-center gap-1.5 text-sm text-gray-600 hover:text-indigo-600 transition-colors px-3 py-1.5 border border-gray-200 rounded-lg print:hidden"
                    >
                      <Printer className="w-4 h-4" />
                      <span>{isEN ? 'Print' : 'Imprimir'}</span>
                    </button>
                    <button
                      onClick={downloadPDF}
                      className="flex items-center gap-1.5 text-sm text-white bg-indigo-600 hover:bg-indigo-700 transition-colors px-3 py-1.5 rounded-lg font-medium print:hidden"
                    >
                      <FileDown className="w-4 h-4" />
                      <span>{(tool?.pdf_download as string) || 'Descargar PDF Carta'}</span>
                    </button>
                    <button
                      onClick={handleRegenerate}
                      className="flex items-center gap-1.5 text-sm text-gray-600 hover:text-indigo-600 transition-colors px-3 py-1.5 border border-gray-200 rounded-lg"
                    >
                      <Sparkles className="w-4 h-4" />
                      <span>{rl.regenerate || 'Otro concepto'}</span>
                    </button>
                    <button
                      onClick={handleReset}
                      className="flex items-center gap-1.5 text-sm text-gray-500 hover:text-indigo-600 transition-colors"
                    >
                      <RotateCcw className="w-4 h-4" />
                      <span>{rl.reset || 'Nuevo menú'}</span>
                    </button>
                  </div>
                </div>

                {/* Elegant dark menu card */}
                <div className="bg-gray-950 rounded-2xl overflow-hidden shadow-2xl print:shadow-none">
                  {/* Header */}
                  <div className="px-8 py-10 text-center border-b border-gray-800">
                    <p className="text-indigo-400 text-xs font-semibold uppercase tracking-[0.3em] mb-3">
                      {isEN ? `${numPases} courses` : `${numPases} pases`}
                    </p>
                    <h2 className="text-2xl md:text-3xl font-serif font-bold text-white mb-3 leading-tight">
                      {result.nombreMenu}
                    </h2>
                    <p className="text-gray-400 text-sm leading-relaxed max-w-lg mx-auto">
                      {result.descripcionConcepto}
                    </p>
                    {tags.length > 0 && (
                      <div className="flex flex-wrap justify-center gap-2 mt-4">
                        {tags.map((t, i) => (
                          <span key={i} className="text-xs bg-indigo-900/60 text-indigo-300 rounded-full px-3 py-1">
                            {t}
                          </span>
                        ))}
                      </div>
                    )}
                  </div>

                  {/* Courses */}
                  <div className="divide-y divide-gray-800/60">
                    {result.pases.map((pase) => (
                      <div key={pase.numero} className="px-8 py-6 hover:bg-gray-900/40 transition-colors">
                        <div className="flex items-start gap-4">
                          <span className="shrink-0 w-8 h-8 rounded-full bg-indigo-900/60 border border-indigo-700/50 flex items-center justify-center text-indigo-400 text-xs font-bold">
                            {pase.numero}
                          </span>
                          <div className="flex-1 min-w-0">
                            <h3 className="text-white font-serif font-semibold text-lg mb-1.5 leading-snug">
                              {pase.nombre}
                            </h3>
                            <p className="text-gray-400 text-sm leading-relaxed mb-3">
                              {pase.descripcion}
                            </p>
                            <div className="flex flex-wrap gap-x-6 gap-y-1">
                              <span className="text-xs text-gray-600">
                                <span className="text-gray-500 font-medium">{rl.tecnica || 'Técnica'}:</span>{' '}
                                <span className="text-gray-400">{pase.tecnica}</span>
                              </span>
                              <span className="text-xs text-gray-600">
                                <span className="text-gray-500 font-medium">{rl.maridaje || 'Maridaje'}:</span>{' '}
                                <span className="text-indigo-400">{pase.maridaje}</span>
                              </span>
                            </div>
                          </div>
                        </div>
                      </div>
                    ))}
                  </div>

                  {/* Footer */}
                  <div className="px-8 py-5 border-t border-gray-800 text-center">
                    <p className="text-gray-600 text-xs tracking-widest uppercase">
                      AI Chef Pro — aichef.pro
                    </p>
                  </div>
                </div>

                {/* CTA post-result */}
                <div className="bg-indigo-600 rounded-xl p-6 text-white text-center mt-6">
                  <p className="font-semibold mb-1">{rl.cta_title || '¿Quieres generar las recetas completas de cada pase?'}</p>
                  <p className="text-indigo-100 text-sm mb-4">
                    {rl.cta_subtitle || 'Con AI Chef Pro creas fichas técnicas, escandallos y recetas paso a paso para tu menú degustación.'}
                  </p>
                  <Button className="bg-white text-indigo-600 hover:bg-indigo-50 font-semibold" asChild>
                    <a href={getAppUrl()} target="_blank" rel="noopener noreferrer">
                      {rl.cta_btn || 'Ver Cocina Creativa AI →'}
                    </a>
                  </Button>
                </div>
              </div>
            )}
          </div>
        </section>

        <PricingPlans toolKey="toolDegustacion" />

        {/* ── FAQ ── */}
        {Array.isArray(faqItems) && faqItems.length > 0 && (
          <section className="py-16 px-4 bg-gray-50">
            <div className="max-w-2xl mx-auto">
              <h2 className="text-2xl font-bold text-gray-900 text-center mb-8">
                {(tool?.faq_title as string) || 'Preguntas frecuentes'}
              </h2>
              <div className="space-y-4">
                {faqItems.map((item, i) => (
                  <div key={i} className="bg-white rounded-xl p-6 border border-gray-200">
                    <p className="font-semibold text-gray-900 mb-2">{item.q}</p>
                    <p className="text-gray-600 text-sm leading-relaxed">{item.a}</p>
                  </div>
                ))}
              </div>
            </div>
          </section>
        )}

        <OtherFreeTools excludeIndex={7} />

        {/* ── Footer CTA ── */}
        <section className="py-16 px-4 bg-white border-t border-gray-100">
          <div className="max-w-2xl mx-auto text-center">
            <h2 className="text-2xl font-bold text-gray-900 mb-3">
              {ctaSection?.title || '¿Listo para crear tu próximo menú degustación?'}
            </h2>
            <p className="text-gray-600 mb-8">
              {ctaSection?.subtitle || 'Genera propuestas en segundos y adapta el resultado a la identidad de tu restaurante.'}
            </p>
            <div className="flex flex-col sm:flex-row gap-3 justify-center">
              <Button
                className="bg-indigo-600 hover:bg-indigo-700 text-white px-6 py-3"
                onClick={() => document.getElementById('tool-section')?.scrollIntoView({ behavior: 'smooth' })}
              >
                {ctaSection?.cta_primary || 'Crear menú degustación gratis'}
              </Button>
              <Button variant="outline" className="border-gray-300 text-gray-700 hover:bg-gray-50 px-6 py-3" asChild>
                <Link to={hubSlug}>
                  <ArrowRight className="w-4 h-4 mr-2" />
                  {ctaSection?.cta_secondary || 'Ver todas las herramientas'}
                </Link>
              </Button>
            </div>
          </div>
        </section>
      </main>

      <ModernFooter />
    </div>
  );
}
