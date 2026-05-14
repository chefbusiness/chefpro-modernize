import avatar1 from '@/assets/avatars/avatar-1.jpg'; // hombre, chaleco sommelier/bar
import avatar2 from '@/assets/avatars/avatar-2.jpg'; // mujer, chaqueta chef blanca
import avatar3 from '@/assets/avatars/avatar-3.jpg'; // hombre, camisa + tirantes (bistró)
import avatar4 from '@/assets/avatars/avatar-4.jpg'; // mujer, gorro chef blanco (panadera)
import avatar6 from '@/assets/avatars/avatar-6.jpg'; // mujer, vestido elegante (asesora)
import avatar7 from '@/assets/avatars/avatar-7.jpg'; // hombre, gorro panadero marrón + delantal — PANADERO PERFECTO
import avatar8 from '@/assets/avatars/avatar-8.jpg'; // hombre, chef maduro chaqueta blanca

// Avatar específico del nicho panadería generado para Elena Solís
const avatarPanaderaCeliaca = '/lovable-uploads/avatars-nicho/avatar-panadera-celiaca.jpg';

export const guiaPanaderiaObradorTestimonials = [
  {
    name: 'Marta Vidal',
    role: 'Panadera artesana, primera apertura en Madrid',
    text: 'La parte de licencia clasificada con salida de humos me ahorró meses de retraso. Verifiqué la viabilidad antes de firmar el alquiler como dice el manual y descarté dos locales que me habrían costado una fortuna en cambios.',
    avatar: avatar4, // M, gorro chef blanco — coherente panadera
  },
  {
    name: 'Javier Marca',
    role: 'Maestro panadero con obrador propio, Barcelona',
    text: 'Llevo 12 años haciendo pan y aún así el plan de fermentación 24-72h y la calculadora de masa madre me dieron criterios técnicos que no había sistematizado. Lo recomiendo a cualquiera que se quiera profesionalizar.',
    avatar: avatar7, // H, gorro panadero marrón — PANADERO PERFECTO
  },
  {
    name: 'Carmen Iglesias',
    role: 'Emprendedora, abriendo panadería-bistró en Bilbao',
    text: 'El business plan modelo me lo aceptó el banco prácticamente sin cambios. Conseguí la financiación de 130.000€ en 18 días. Vale 10 veces el precio de la guía solo por eso.',
    avatar: avatar2, // M, chaqueta chef — coherente bistró
  },
  {
    name: 'Daniel Romero',
    role: 'Antiguo chef pastelero reconvertido a panadero',
    text: 'El recetario maestro con baguette tradition, hogaza T80 masa madre, croissant clásico y panettone es muy técnico. Las hidrataciones, los plegados, los tiempos. Información de obrador real, no de blog.',
    avatar: avatar8, // H, chef maduro chaqueta blanca — pastelero/chef
  },
  {
    name: 'Lucía Bermúdez',
    role: 'Asesora financiera especializada hostelería',
    text: 'El P&L mensual con 3 escenarios + cash flow 24 meses + calculadora CAPEX es lo más completo que he visto a este precio. Lo doy a todos mis clientes que quieren entrar en panadería.',
    avatar: avatar6, // M, vestido elegante — coherente asesora (perfil externo)
  },
  {
    name: 'Pedro Estévez',
    role: 'Inversor con 3 locales de gastrobar buscando diversificar',
    text: 'El capítulo de modelos de negocio (tradicional vs despacho vs bistró vs boutique) me ayudó a decidir el modelo correcto para mi ubicación. Cada uno tiene márgenes muy distintos y el análisis es preciso.',
    avatar: avatar1, // H, chaleco — coherente inversor con gastrobar
  },
  {
    name: 'Elena Solís',
    role: 'Panadera celíaca, especialidad sin gluten',
    text: 'El protocolo de alérgenos cruzados con separación física es exactamente lo que necesitaba para certificarme FACE. Me aclaró por qué tantas panaderías cometen errores graves al ofrecer sin gluten.',
    avatar: avatarPanaderaCeliaca, // M, gorro chef + delantal + harina + obrador — específico nicho
  },
  {
    name: 'Roberto Casas',
    role: 'Gestor laboral hostelería',
    text: 'El control horario digital 2026 con plus nocturnidad para turnos de madrugada está bien resuelto en la plantilla de turnos. Cumplimiento legal + rentabilidad. Mis clientes panaderos lo agradecen.',
    avatar: avatar3, // H, camisa + tirantes — profesional formal sin nicho
  },
];
