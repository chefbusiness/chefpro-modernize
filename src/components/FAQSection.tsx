import {
  Accordion,
  AccordionContent,
  AccordionItem,
  AccordionTrigger,
} from '@/components/ui/accordion';

const FAQSection = () => {
  const faqs = [
    {
      question: '¿Qué es AI Chef Pro y cómo puede beneficiarme como chef o profesional de la gastronomía?',
      answer: 'AI Chef Pro es una Suite de Herramientas y Aplicaciones de Inteligencia Artificial, modelos entrenados para el uso cotidiano de Chefs, Cocineros y profesionales de la hostelería. Ofrece herramientas que impulsan tu creatividad, mejoran tu gestión y amplían tus conocimientos culinarios. Como líder en cualquier campo de la cocina o la gastronomía, podrás explorar nuevas combinaciones de sabores, optimizar tus procesos y mantenerte al día con las últimas tendencias gastronómicas. AI Chef Pro te permite enfocarte en tu pasión culinaria mientras la IA te asiste en tareas repetitivas, te ayuda a resolver escenarios y te inspira con nuevas ideas.'
    },
    {
      question: '¿Qué herramientas específicas ofrece AI Chef Pro para mi gestión profesional?',
      answer: 'AI Chef Pro ofrece una variedad de herramientas centradas en tu crecimiento como chef: Catering AI+ para planificar eventos, Food Pairing AI para descubrir combinaciones innovadoras, Mermas GenCal para optimizar el uso de ingredientes, ID Alérgenos para garantizar la seguridad alimentaria, Mental Coach para tu bienestar profesional, y otras más. Además, incluye generadores de recetas temáticos, semanalmente el sistema libera una nueva app dentro de la suite que responde a una solución.'
    },
    {
      question: '¿Cuáles son los planes de suscripción disponibles y sus precios?',
      answer: 'Ofrecemos planes adaptados a diferentes etapas de tu carrera como chef: Miembro (Gratis) para explorar funcionalidades básicas, Pro (10€/mes) ideal para chefs individuales, Premium (15€/mes) para uso frecuente y mayor creatividad, Premium Pro (25€/mes) para chefs en roles de liderazgo, y Premium Plus (50€/mes) con uso ilimitado para chefs ejecutivos. Cada plan está diseñado para apoyar tu crecimiento profesional y adaptarse a tus necesidades cambiantes como chef.'
    },
    {
      question: '¿Qué nivel de experiencia tecnológica necesito para usar AI Chef Pro?',
      answer: 'AI Chef Pro está diseñado pensando en chefs y profesionales de todos los niveles tecnológicos. La interfaz es intuitiva y fácil de usar, accesible desde ordenadores y dispositivos móviles para que puedas utilizarlo en la cocina o donde lo necesites. El sistema aprende de tus preferencias, ofreciendo sugerencias cada vez más relevantes. No necesitas ser un experto en tecnología; si puedes usar un smartphone, podrás aprovechar AI Chef Pro al máximo.'
    },
    {
      question: '¿Cómo protege AI Chef Pro mis recetas y datos personales?',
      answer: 'Entendemos que tus recetas son tu propiedad intelectual más valiosa. En AI Chef Pro, utilizamos tecnologías de encriptación avanzadas para proteger toda tu información. Tus recetas y datos personales se mantienen estrictamente confidenciales y nunca se comparten. Ofrecemos opciones de respaldo regulares para garantizar que nunca pierdas tu trabajo. Tu creatividad y privacidad están seguras con nosotros.'
    },
    {
      question: '¿Puedo probar AI Chef Pro antes de suscribirme?',
      answer: '¡Absolutamente! Ofrecemos un plan Miembro gratuito que te permite explorar las funcionalidades básicas de AI Chef Pro sin compromiso. Es una excelente manera de descubrir cómo la plataforma puede potenciar tu creatividad y eficiencia como chef. Cuando estés listo para acceder a más funciones y llevar tu cocina al siguiente nivel, puedes actualizar fácilmente a uno de nuestros planes de pago.'
    }
  ];

  return (
    <section id="faq" className="py-20 bg-background">
      <div className="container mx-auto px-4">
        <div className="max-w-4xl mx-auto">
          <div className="text-center mb-16 animate-fade-in-up">
            <h2 className="text-3xl md:text-4xl font-bold text-chef-dark mb-6">
              Preguntas Frecuentes
            </h2>
            <p className="text-lg text-chef-gray">
              Resolvemos las dudas más comunes sobre AI Chef Pro
            </p>
          </div>

          <div className="animate-scale-in">
            <Accordion type="single" collapsible className="w-full space-y-4">
              {faqs.map((faq, index) => (
                <AccordionItem 
                  key={index} 
                  value={`item-${index}`}
                  className="chef-card border-0 px-6"
                >
                  <AccordionTrigger className="text-left font-semibold text-chef-dark hover:text-chef-gold transition-colors [&>svg]:text-chef-gold">
                    {faq.question}
                  </AccordionTrigger>
                  <AccordionContent className="text-chef-gray leading-relaxed pt-4">
                    {faq.answer}
                  </AccordionContent>
                </AccordionItem>
              ))}
            </Accordion>
          </div>
        </div>
      </div>
    </section>
  );
};

export default FAQSection;