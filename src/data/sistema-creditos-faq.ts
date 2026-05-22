// Content for the "Sistema de créditos" FAQ landing page.
// Available in the 7 languages the platform supports: es, en, fr, de, it, pt, nl.
// German uses the formal "Sie" form to match the rest of the German site.

export type FaqLang = 'es' | 'en' | 'fr' | 'de' | 'it' | 'pt' | 'nl';

export interface CreditFaqItem {
  /** Question text. */
  q: string;
  /** Answer, split into one or more paragraphs. */
  a: string[];
}

export interface CreditFaqContent {
  badge: string;
  h1: string;
  intro: string;
  breadcrumb: string;
  faqs: CreditFaqItem[];
  supportTitle: string;
  supportText: string;
  /** CTA label; "{email}" is replaced with the support email at render time. */
  supportCta: string;
  seoTitle: string;
  seoDescription: string;
  seoKeywords: string;
}

export const SUPPORT_EMAIL = 'info@aichef.pro';

export const CREDIT_FAQ_CONTENT: Record<FaqLang, CreditFaqContent> = {
  es: {
    badge: 'Nuevo sistema de créditos',
    h1: 'Preguntas Frecuentes sobre el Nuevo Sistema de Créditos de AI Chef Pro',
    intro:
      'Estamos migrando del sistema de medición por usos a un sistema de créditos, el estándar que ya adopta la industria de la IA. Aquí resolvemos las dudas más frecuentes sobre cómo funciona esta actualización y qué significa para ti.',
    breadcrumb: 'Sistema de Créditos',
    faqs: [
      {
        q: '¿Qué es el sistema de créditos y por qué lo habéis adoptado?',
        a: [
          'El sistema de créditos es el modelo estándar que utilizan actualmente los principales proveedores de inteligencia artificial del mundo. Consiste en asignar a cada usuario una cantidad de créditos que se consumen en función del uso que se hace de los modelos de IA disponibles en la plataforma.',
          'Hemos adoptado este sistema porque es el único que nos permite ofrecerte acceso nativo a los modelos de frontera más avanzados del mercado —como DeepSeek 4, Gemini 3.5 Flash, Opus 4.7 o GPT-5.5— directamente dentro de AI Chef Pro, sin salir de la plataforma ni depender de integraciones externas.',
        ],
      },
      {
        q: '¿Qué ha cambiado respecto al sistema anterior?',
        a: [
          'Hasta ahora, AI Chef Pro funcionaba con un sistema de uso por defecto, sin distinción según el modelo o la intensidad del uso. Con el nuevo sistema de créditos, el consumo se ajusta al uso real que haces de la plataforma y al tipo de modelo que utilizas en cada momento. Esto nos permite ser más justos, más transparentes y, sobre todo, ofrecerte acceso a herramientas mucho más potentes.',
        ],
      },
      {
        q: '¿Cuándo entra en vigor el nuevo sistema de créditos?',
        a: [
          'Estamos implementando el nuevo sistema de créditos de forma progresiva en la plataforma. Te informaremos por correo electrónico y desde el panel de la plataforma a medida que se aplique a tu cuenta, para que tengas toda la información antes de cualquier cambio. Mientras tanto, puedes seguir utilizando AI Chef Pro con total normalidad.',
        ],
      },
      {
        q: '¿Cómo se consumen los créditos?',
        a: [
          'Cada interacción con los agentes de la plataforma consume una cantidad de créditos que varía según el modelo utilizado y la extensión de la conversación. Los modelos más avanzados y las sesiones más largas o con mayor volumen de contexto consumirán más créditos que las interacciones simples. En tu panel de usuario podrás ver en todo momento tu saldo disponible y tu historial de consumo.',
        ],
      },
      {
        q: '¿Cuántos créditos incluye mi plan actual?',
        a: [
          'Cada plan de AI Chef Pro incluye una cantidad de créditos mensuales. Puedes consultar los créditos asignados a tu plan actual directamente en tu perfil de usuario dentro de la plataforma. Si tienes dudas sobre qué plan se adapta mejor a tu nivel de uso, nuestro equipo estará encantado de orientarte.',
        ],
      },
      {
        q: 'Tenía un número de usos al mes en mi plan. ¿A cuántos créditos equivalen?',
        a: [
          'Cada plan se ha convertido a una asignación equivalente de créditos, pensada para que puedas mantener —como mínimo— el mismo nivel de uso que tenías hasta ahora. Puedes consultar los créditos exactos asignados a tu plan directamente en tu perfil de usuario dentro de la plataforma.',
        ],
      },
      {
        q: '¿Qué ocurre si se me acaban los créditos?',
        a: [
          'Si agotas tus créditos antes de que se renueven, podrás adquirir créditos adicionales de forma sencilla desde tu panel de usuario, sin necesidad de cambiar de plan. También puedes optar por actualizar tu suscripción si tu uso habitual supera los créditos incluidos en tu plan actual.',
        ],
      },
      {
        q: '¿Este cambio encarece mi plan? ¿Tengo que hacer algo?',
        a: [
          'No. El precio de tu suscripción no cambia con la adopción del sistema de créditos, y no necesitas hacer nada: la conversión a créditos se aplica de forma automática. El sistema de créditos solo cambia la forma de medir el consumo, no la cuota que pagas. Si en el futuro actualizamos los planes, te lo comunicaremos siempre con antelación.',
        ],
      },
      {
        q: '¿Los créditos caducan?',
        a: [
          'Los créditos incluidos en tu plan mensual se renuevan con cada ciclo de facturación. Los créditos adicionales adquiridos de forma independiente tienen su propia fecha de validez, que se indicará claramente en el momento de la compra.',
        ],
      },
      {
        q: '¿Todos los agentes de la plataforma consumen créditos de la misma manera?',
        a: [
          'No. El consumo depende del modelo de IA que utiliza cada agente y de la complejidad de la sesión. Los agentes basados en modelos de frontera de última generación tendrán un consumo mayor que los agentes con modelos más ligeros. En cada agente encontrarás información clara sobre su consumo estimado por sesión.',
        ],
      },
      {
        q: '¿Vais a añadir más modelos próximamente?',
        a: [
          'Sí. La integración del sistema de créditos es precisamente lo que nos permite activar nuevos modelos de forma progresiva y nativa dentro de la plataforma. En los próximos días iremos incorporando nuevas opciones y te avisaremos por correo electrónico y desde el panel de la plataforma en cuanto estén disponibles.',
        ],
      },
      {
        q: '¿Este cambio afecta a la calidad o al funcionamiento de los agentes especializados?',
        a: [
          'En absoluto. Todos los agentes especializados de AI Chef Pro —Cocina Creativa, Chef Ejecutivo, Catering AI+, Conceptos de Negocio y el resto— siguen funcionando exactamente igual, y en muchos casos mejor, gracias al reentrenamiento y las mejoras incluidas en la versión 2.1. El sistema de créditos únicamente regula el acceso a los modelos, no la calidad ni la especialización de los agentes.',
        ],
      },
      {
        q: 'Tengo más dudas, ¿con quién puedo hablar?',
        a: [
          `Puedes escribirnos a ${SUPPORT_EMAIL} o contactarnos a través del chat dentro de la plataforma. Nuestro equipo está disponible para ayudarte a entender el nuevo sistema y asegurarse de que sigas sacando el máximo partido a AI Chef Pro.`,
        ],
      },
    ],
    supportTitle: '¿Sigues con dudas?',
    supportText:
      'Nuestro equipo está disponible para ayudarte a entender el nuevo sistema y a sacar el máximo partido a AI Chef Pro.',
    supportCta: 'Escríbenos a {email}',
    seoTitle: 'Preguntas Frecuentes — Sistema de Créditos | AI Chef Pro',
    seoDescription:
      'Resolvemos tus dudas sobre el nuevo sistema de créditos de AI Chef Pro: qué es, cómo se consumen los créditos, qué incluye tu plan y cómo te da acceso a los modelos de IA más avanzados.',
    seoKeywords:
      'sistema de créditos, AI Chef Pro, créditos IA, modelos de IA, planes, preguntas frecuentes',
  },

  en: {
    badge: 'New credit system',
    h1: 'Frequently Asked Questions About the New AI Chef Pro Credit System',
    intro:
      "We're migrating from a usage-based metering system to a credit system — the standard the AI industry has already adopted. Here we answer the most common questions about how this update works and what it means for you.",
    breadcrumb: 'Credit System',
    faqs: [
      {
        q: 'What is the credit system and why have you adopted it?',
        a: [
          "The credit system is the standard model currently used by the world's leading artificial intelligence providers. It assigns each user an amount of credits that are consumed based on how the AI models available on the platform are used.",
          "We've adopted this system because it's the only one that lets us give you native access to the most advanced frontier models on the market — such as DeepSeek 4, Gemini 3.5 Flash, Opus 4.7 or GPT-5.5 — directly inside AI Chef Pro, without leaving the platform or relying on external integrations.",
        ],
      },
      {
        q: 'What has changed compared to the previous system?',
        a: [
          'Until now, AI Chef Pro worked with a default usage system, with no distinction based on the model or the intensity of use. With the new credit system, consumption adjusts to the actual use you make of the platform and the type of model you use at any given moment. This lets us be fairer, more transparent and, above all, offer you access to far more powerful tools.',
        ],
      },
      {
        q: 'When does the new credit system take effect?',
        a: [
          'We are rolling out the new credit system progressively across the platform. We will notify you by email and from the platform panel as it is applied to your account, so you have all the information before any change. In the meantime, you can keep using AI Chef Pro as normal.',
        ],
      },
      {
        q: 'How are credits consumed?',
        a: [
          'Every interaction with the platform’s agents consumes an amount of credits that varies depending on the model used and the length of the conversation. More advanced models and longer sessions, or sessions with a larger volume of context, will consume more credits than simple interactions. In your user panel you can see your available balance and your consumption history at all times.',
        ],
      },
      {
        q: 'How many credits does my current plan include?',
        a: [
          "Every AI Chef Pro plan includes a monthly amount of credits. You can check the credits assigned to your current plan directly in your user profile within the platform. If you're unsure which plan best suits your level of use, our team will be glad to advise you.",
        ],
      },
      {
        q: 'My plan had a number of uses per month. How many credits do they equal?',
        a: [
          'Each plan has been converted to an equivalent allocation of credits, designed so that you can maintain — at least — the same level of use you had until now. You can check the exact credits assigned to your plan directly in your user profile within the platform.',
        ],
      },
      {
        q: 'What happens if I run out of credits?',
        a: [
          'If you use up your credits before they renew, you can easily purchase additional credits from your user panel, without needing to change your plan. You can also choose to upgrade your subscription if your regular usage exceeds the credits included in your current plan.',
        ],
      },
      {
        q: 'Does this change make my plan more expensive? Do I need to do anything?',
        a: [
          'No. The price of your subscription does not change with the adoption of the credit system, and you do not need to do anything: the conversion to credits is applied automatically. The credit system only changes the way consumption is measured, not the fee you pay. If we update the plans in the future, we will always let you know in advance.',
        ],
      },
      {
        q: 'Do credits expire?',
        a: [
          'The credits included in your monthly plan renew with each billing cycle. Additional credits purchased separately have their own validity date, which will be clearly indicated at the time of purchase.',
        ],
      },
      {
        q: "Do all the platform's agents consume credits in the same way?",
        a: [
          "No. Consumption depends on the AI model each agent uses and the complexity of the session. Agents based on the latest-generation frontier models will consume more than agents with lighter models. On each agent you'll find clear information about its estimated consumption per session.",
        ],
      },
      {
        q: 'Are you going to add more models soon?',
        a: [
          "Yes. The integration of the credit system is precisely what allows us to activate new models progressively and natively within the platform. Over the coming days we'll be adding new options, and we'll notify you by email and from the platform panel as soon as they're available.",
        ],
      },
      {
        q: 'Does this change affect the quality or functioning of the specialized agents?',
        a: [
          "Not at all. All of AI Chef Pro's specialized agents — Avant-garde Cuisine, Executive Chef, Catering AI+, Business Concepts and the rest — keep working exactly the same, and in many cases better, thanks to the retraining and improvements included in version 2.1. The credit system only governs access to the models, not the quality or specialization of the agents.",
        ],
      },
      {
        q: 'I have more questions — who can I talk to?',
        a: [
          `You can email us at ${SUPPORT_EMAIL} or contact us through the chat inside the platform. Our team is available to help you understand the new system and make sure you keep getting the most out of AI Chef Pro.`,
        ],
      },
    ],
    supportTitle: 'Still have questions?',
    supportText:
      'Our team is available to help you understand the new system and get the most out of AI Chef Pro.',
    supportCta: 'Email us at {email}',
    seoTitle: 'FAQ — Credit System | AI Chef Pro',
    seoDescription:
      "We answer your questions about AI Chef Pro's new credit system: what it is, how credits are consumed, what your plan includes, and how it gives you access to the most advanced AI models.",
    seoKeywords:
      'credit system, AI Chef Pro, AI credits, AI models, plans, FAQ',
  },

  fr: {
    badge: 'Nouveau système de crédits',
    h1: "Questions Fréquentes sur le Nouveau Système de Crédits d'AI Chef Pro",
    intro:
      "Nous migrons d'un système de mesure par utilisations vers un système de crédits, le standard déjà adopté par l'industrie de l'IA. Vous trouverez ici les réponses aux questions les plus fréquentes sur le fonctionnement de cette mise à jour et ce qu'elle signifie pour vous.",
    breadcrumb: 'Système de crédits',
    faqs: [
      {
        q: "Qu'est-ce que le système de crédits et pourquoi l'avez-vous adopté ?",
        a: [
          "Le système de crédits est le modèle standard utilisé actuellement par les principaux fournisseurs d'intelligence artificielle du monde. Il consiste à attribuer à chaque utilisateur une quantité de crédits qui sont consommés en fonction de l'usage fait des modèles d'IA disponibles sur la plateforme.",
          "Nous avons adopté ce système car c'est le seul qui nous permet de vous offrir un accès natif aux modèles de frontière les plus avancés du marché — comme DeepSeek 4, Gemini 3.5 Flash, Opus 4.7 ou GPT-5.5 — directement au sein d'AI Chef Pro, sans quitter la plateforme ni dépendre d'intégrations externes.",
        ],
      },
      {
        q: 'Qu’est-ce qui a changé par rapport au système précédent ?',
        a: [
          "Jusqu'à présent, AI Chef Pro fonctionnait avec un système d'utilisation par défaut, sans distinction selon le modèle ou l'intensité de l'usage. Avec le nouveau système de crédits, la consommation s'ajuste à l'usage réel que vous faites de la plateforme et au type de modèle que vous utilisez à chaque moment. Cela nous permet d'être plus justes, plus transparents et, surtout, de vous offrir l'accès à des outils bien plus puissants.",
        ],
      },
      {
        q: 'Quand le nouveau système de crédits entre-t-il en vigueur ?',
        a: [
          "Nous mettons en place le nouveau système de crédits de façon progressive sur la plateforme. Nous vous informerons par e-mail et depuis le panneau de la plateforme au fur et à mesure de son application à votre compte, afin que vous disposiez de toutes les informations avant tout changement. Entre-temps, vous pouvez continuer à utiliser AI Chef Pro normalement.",
        ],
      },
      {
        q: 'Comment les crédits sont-ils consommés ?',
        a: [
          "Chaque interaction avec les agents de la plateforme consomme une quantité de crédits qui varie selon le modèle utilisé et la longueur de la conversation. Les modèles les plus avancés et les sessions les plus longues ou comportant un plus grand volume de contexte consommeront plus de crédits que les interactions simples. Dans votre panneau utilisateur, vous pourrez voir à tout moment votre solde disponible et votre historique de consommation.",
        ],
      },
      {
        q: 'Combien de crédits inclut mon forfait actuel ?',
        a: [
          "Chaque forfait d'AI Chef Pro inclut une quantité de crédits mensuels. Vous pouvez consulter les crédits attribués à votre forfait actuel directement dans votre profil utilisateur au sein de la plateforme. Si vous avez des doutes sur le forfait le mieux adapté à votre niveau d'usage, notre équipe se fera un plaisir de vous orienter.",
        ],
      },
      {
        q: "Mon forfait incluait un nombre d'utilisations par mois. À combien de crédits cela correspond-il ?",
        a: [
          "Chaque forfait a été converti en une allocation équivalente de crédits, conçue pour que vous puissiez conserver — au minimum — le même niveau d'usage que vous aviez jusqu'à présent. Vous pouvez consulter les crédits exacts attribués à votre forfait directement dans votre profil utilisateur au sein de la plateforme.",
        ],
      },
      {
        q: 'Que se passe-t-il si je suis à court de crédits ?',
        a: [
          "Si vous épuisez vos crédits avant leur renouvellement, vous pourrez acquérir des crédits supplémentaires facilement depuis votre panneau utilisateur, sans avoir besoin de changer de forfait. Vous pouvez également choisir de mettre à niveau votre abonnement si votre usage habituel dépasse les crédits inclus dans votre forfait actuel.",
        ],
      },
      {
        q: 'Ce changement rend-il mon forfait plus cher ? Dois-je faire quelque chose ?',
        a: [
          "Non. Le prix de votre abonnement ne change pas avec l'adoption du système de crédits, et vous n'avez rien à faire : la conversion en crédits s'applique automatiquement. Le système de crédits modifie uniquement la façon de mesurer la consommation, pas le montant que vous payez. Si nous mettons à jour les forfaits à l'avenir, nous vous en informerons toujours à l'avance.",
        ],
      },
      {
        q: 'Les crédits expirent-ils ?',
        a: [
          "Les crédits inclus dans votre forfait mensuel se renouvellent à chaque cycle de facturation. Les crédits supplémentaires acquis séparément ont leur propre date de validité, qui sera clairement indiquée au moment de l'achat.",
        ],
      },
      {
        q: 'Tous les agents de la plateforme consomment-ils des crédits de la même manière ?',
        a: [
          "Non. La consommation dépend du modèle d'IA utilisé par chaque agent et de la complexité de la session. Les agents basés sur les modèles de frontière de dernière génération auront une consommation plus élevée que les agents utilisant des modèles plus légers. Sur chaque agent, vous trouverez des informations claires sur sa consommation estimée par session.",
        ],
      },
      {
        q: "Allez-vous ajouter d'autres modèles prochainement ?",
        a: [
          "Oui. L'intégration du système de crédits est précisément ce qui nous permet d'activer de nouveaux modèles de façon progressive et native au sein de la plateforme. Dans les prochains jours, nous incorporerons de nouvelles options et nous vous préviendrons par e-mail et depuis le panneau de la plateforme dès qu'elles seront disponibles.",
        ],
      },
      {
        q: 'Ce changement affecte-t-il la qualité ou le fonctionnement des agents spécialisés ?',
        a: [
          "Absolument pas. Tous les agents spécialisés d'AI Chef Pro — Cuisine Créative, Chef Exécutif, Traiteur IA+, Concepts d'Affaires et les autres — continuent de fonctionner exactement de la même manière, et dans bien des cas mieux, grâce au réentraînement et aux améliorations incluses dans la version 2.1. Le système de crédits régule uniquement l'accès aux modèles, pas la qualité ni la spécialisation des agents.",
        ],
      },
      {
        q: "J'ai d'autres questions, à qui puis-je m'adresser ?",
        a: [
          `Vous pouvez nous écrire à ${SUPPORT_EMAIL} ou nous contacter via le chat au sein de la plateforme. Notre équipe est disponible pour vous aider à comprendre le nouveau système et à vous assurer que vous continuez à tirer le meilleur parti d'AI Chef Pro.`,
        ],
      },
    ],
    supportTitle: 'Vous avez encore des questions ?',
    supportText:
      "Notre équipe est disponible pour vous aider à comprendre le nouveau système et à tirer le meilleur parti d'AI Chef Pro.",
    supportCta: 'Écrivez-nous à {email}',
    seoTitle: 'FAQ — Système de Crédits | AI Chef Pro',
    seoDescription:
      "Nous répondons à vos questions sur le nouveau système de crédits d'AI Chef Pro : ce que c'est, comment les crédits sont consommés, ce qu'inclut votre forfait et comment il vous donne accès aux modèles d'IA les plus avancés.",
    seoKeywords:
      "système de crédits, AI Chef Pro, crédits IA, modèles d'IA, forfaits, questions fréquentes",
  },

  de: {
    badge: 'Neues Kreditsystem',
    h1: 'Häufige Fragen zum Neuen Kreditsystem von AI Chef Pro',
    intro:
      'Wir wechseln von einem nutzungsbasierten Messsystem zu einem Kreditsystem – dem Standard, den die KI-Branche bereits übernommen hat. Hier beantworten wir die häufigsten Fragen dazu, wie dieses Update funktioniert und was es für Sie bedeutet.',
    breadcrumb: 'Kreditsystem',
    faqs: [
      {
        q: 'Was ist das Kreditsystem und warum haben Sie es eingeführt?',
        a: [
          'Das Kreditsystem ist das Standardmodell, das derzeit von den weltweit führenden Anbietern künstlicher Intelligenz verwendet wird. Dabei wird jedem Nutzer eine Menge an Credits zugewiesen, die je nach Nutzung der auf der Plattform verfügbaren KI-Modelle verbraucht werden.',
          'Wir haben dieses System eingeführt, weil es das einzige ist, das es uns ermöglicht, Ihnen nativen Zugang zu den fortschrittlichsten Frontier-Modellen des Marktes zu bieten – wie DeepSeek 4, Gemini 3.5 Flash, Opus 4.7 oder GPT-5.5 – direkt innerhalb von AI Chef Pro, ohne die Plattform zu verlassen oder von externen Integrationen abhängig zu sein.',
        ],
      },
      {
        q: 'Was hat sich gegenüber dem bisherigen System geändert?',
        a: [
          'Bisher funktionierte AI Chef Pro mit einem Standard-Nutzungssystem, ohne Unterscheidung nach Modell oder Nutzungsintensität. Mit dem neuen Kreditsystem passt sich der Verbrauch an Ihre tatsächliche Nutzung der Plattform und an die Art des Modells an, das Sie jeweils verwenden. So können wir fairer und transparenter sein und Ihnen vor allem Zugang zu deutlich leistungsstärkeren Werkzeugen bieten.',
        ],
      },
      {
        q: 'Wann tritt das neue Kreditsystem in Kraft?',
        a: [
          'Wir führen das neue Kreditsystem schrittweise auf der Plattform ein. Wir informieren Sie per E-Mail und über das Plattform-Panel, sobald es auf Ihr Konto angewendet wird, damit Ihnen vor jeder Änderung alle Informationen vorliegen. In der Zwischenzeit können Sie AI Chef Pro ganz normal weiter nutzen.',
        ],
      },
      {
        q: 'Wie werden Credits verbraucht?',
        a: [
          'Jede Interaktion mit den Agenten der Plattform verbraucht eine Menge an Credits, die je nach verwendetem Modell und Länge der Konversation variiert. Fortschrittlichere Modelle und längere Sitzungen oder Sitzungen mit größerem Kontextvolumen verbrauchen mehr Credits als einfache Interaktionen. In Ihrem Nutzerbereich können Sie jederzeit Ihr verfügbares Guthaben und Ihren Verbrauchsverlauf einsehen.',
        ],
      },
      {
        q: 'Wie viele Credits enthält mein aktueller Tarif?',
        a: [
          'Jeder Tarif von AI Chef Pro enthält eine monatliche Menge an Credits. Sie können die Ihrem aktuellen Tarif zugewiesenen Credits direkt in Ihrem Nutzerprofil innerhalb der Plattform einsehen. Wenn Sie sich nicht sicher sind, welcher Tarif am besten zu Ihrem Nutzungsverhalten passt, berät Sie unser Team gerne.',
        ],
      },
      {
        q: 'Mein Tarif enthielt eine Anzahl an Nutzungen pro Monat. Wie vielen Credits entspricht das?',
        a: [
          'Jeder Tarif wurde in eine entsprechende Menge an Credits umgewandelt, die so bemessen ist, dass Sie mindestens das gleiche Nutzungsniveau wie bisher beibehalten können. Sie können die genaue Anzahl der Ihrem Tarif zugewiesenen Credits direkt in Ihrem Nutzerprofil innerhalb der Plattform einsehen.',
        ],
      },
      {
        q: 'Was passiert, wenn meine Credits aufgebraucht sind?',
        a: [
          'Wenn Sie Ihre Credits vor der Erneuerung aufbrauchen, können Sie ganz einfach zusätzliche Credits über Ihren Nutzerbereich erwerben, ohne den Tarif wechseln zu müssen. Sie können auch Ihr Abonnement upgraden, wenn Ihre übliche Nutzung die in Ihrem aktuellen Tarif enthaltenen Credits übersteigt.',
        ],
      },
      {
        q: 'Wird mein Tarif durch diese Änderung teurer? Muss ich etwas tun?',
        a: [
          'Nein. Der Preis Ihres Abonnements ändert sich durch die Einführung des Kreditsystems nicht, und Sie müssen nichts tun: Die Umwandlung in Credits erfolgt automatisch. Das Kreditsystem ändert lediglich die Art, wie der Verbrauch gemessen wird, nicht den Betrag, den Sie zahlen. Sollten wir die Tarife in Zukunft aktualisieren, informieren wir Sie stets im Voraus.',
        ],
      },
      {
        q: 'Verfallen Credits?',
        a: [
          'Die in Ihrem Monatstarif enthaltenen Credits werden mit jedem Abrechnungszyklus erneuert. Separat erworbene zusätzliche Credits haben ihr eigenes Gültigkeitsdatum, das beim Kauf klar angegeben wird.',
        ],
      },
      {
        q: 'Verbrauchen alle Agenten der Plattform Credits auf die gleiche Weise?',
        a: [
          'Nein. Der Verbrauch hängt vom KI-Modell ab, das jeder Agent verwendet, sowie von der Komplexität der Sitzung. Agenten, die auf Frontier-Modellen der neuesten Generation basieren, haben einen höheren Verbrauch als Agenten mit leichteren Modellen. Bei jedem Agenten finden Sie klare Informationen zum geschätzten Verbrauch pro Sitzung.',
        ],
      },
      {
        q: 'Werden Sie demnächst weitere Modelle hinzufügen?',
        a: [
          'Ja. Die Integration des Kreditsystems ist genau das, was es uns ermöglicht, neue Modelle schrittweise und nativ innerhalb der Plattform zu aktivieren. In den kommenden Tagen werden wir neue Optionen hinzufügen und Sie per E-Mail sowie über das Plattform-Panel benachrichtigen, sobald sie verfügbar sind.',
        ],
      },
      {
        q: 'Wirkt sich diese Änderung auf die Qualität oder Funktionsweise der spezialisierten Agenten aus?',
        a: [
          'Überhaupt nicht. Alle spezialisierten Agenten von AI Chef Pro – Cuisine Créative, Executive Chef, Catering AI+, Geschäftskonzepte und die übrigen – funktionieren weiterhin genau gleich und in vielen Fällen sogar besser, dank des Neutrainings und der Verbesserungen in Version 2.1. Das Kreditsystem regelt ausschließlich den Zugang zu den Modellen, nicht die Qualität oder Spezialisierung der Agenten.',
        ],
      },
      {
        q: 'Ich habe weitere Fragen – an wen kann ich mich wenden?',
        a: [
          `Sie können uns an ${SUPPORT_EMAIL} schreiben oder uns über den Chat innerhalb der Plattform kontaktieren. Unser Team steht Ihnen zur Verfügung, um Ihnen das neue System zu erklären und sicherzustellen, dass Sie weiterhin das Beste aus AI Chef Pro herausholen.`,
        ],
      },
    ],
    supportTitle: 'Haben Sie noch Fragen?',
    supportText:
      'Unser Team hilft Ihnen gerne, das neue System zu verstehen und das Beste aus AI Chef Pro herauszuholen.',
    supportCta: 'Schreiben Sie uns an {email}',
    seoTitle: 'FAQ — Kreditsystem | AI Chef Pro',
    seoDescription:
      'Wir beantworten Ihre Fragen zum neuen Kreditsystem von AI Chef Pro: was es ist, wie Credits verbraucht werden, was Ihr Tarif enthält und wie es Ihnen Zugang zu den fortschrittlichsten KI-Modellen verschafft.',
    seoKeywords:
      'Kreditsystem, AI Chef Pro, KI-Credits, KI-Modelle, Tarife, häufige Fragen',
  },

  it: {
    badge: 'Nuovo sistema di crediti',
    h1: 'Domande Frequenti sul Nuovo Sistema di Crediti di AI Chef Pro',
    intro:
      "Stiamo migrando da un sistema di misurazione per utilizzi a un sistema di crediti, lo standard già adottato dall'industria dell'IA. Qui rispondiamo alle domande più frequenti su come funziona questo aggiornamento e cosa significa per te.",
    breadcrumb: 'Sistema di crediti',
    faqs: [
      {
        q: "Cos'è il sistema di crediti e perché lo avete adottato?",
        a: [
          "Il sistema di crediti è il modello standard attualmente utilizzato dai principali fornitori di intelligenza artificiale del mondo. Consiste nell'assegnare a ogni utente una quantità di crediti che vengono consumati in base all'uso che si fa dei modelli di IA disponibili sulla piattaforma.",
          "Abbiamo adottato questo sistema perché è l'unico che ci consente di offrirti accesso nativo ai modelli di frontiera più avanzati del mercato — come DeepSeek 4, Gemini 3.5 Flash, Opus 4.7 o GPT-5.5 — direttamente all'interno di AI Chef Pro, senza uscire dalla piattaforma né dipendere da integrazioni esterne.",
        ],
      },
      {
        q: 'Cosa è cambiato rispetto al sistema precedente?',
        a: [
          "Finora, AI Chef Pro funzionava con un sistema di utilizzo predefinito, senza distinzione in base al modello o all'intensità dell'uso. Con il nuovo sistema di crediti, il consumo si adatta all'uso reale che fai della piattaforma e al tipo di modello che utilizzi in ogni momento. Questo ci permette di essere più equi, più trasparenti e, soprattutto, di offrirti accesso a strumenti molto più potenti.",
        ],
      },
      {
        q: 'Quando entra in vigore il nuovo sistema di crediti?',
        a: [
          "Stiamo implementando il nuovo sistema di crediti in modo progressivo sulla piattaforma. Ti informeremo via e-mail e dal pannello della piattaforma man mano che verrà applicato al tuo account, affinché tu abbia tutte le informazioni prima di qualsiasi cambiamento. Nel frattempo, puoi continuare a utilizzare AI Chef Pro in tutta normalità.",
        ],
      },
      {
        q: 'Come si consumano i crediti?',
        a: [
          'Ogni interazione con gli agenti della piattaforma consuma una quantità di crediti che varia in base al modello utilizzato e alla lunghezza della conversazione. I modelli più avanzati e le sessioni più lunghe o con un maggior volume di contesto consumeranno più crediti rispetto alle interazioni semplici. Nel tuo pannello utente potrai vedere in qualsiasi momento il tuo saldo disponibile e lo storico dei consumi.',
        ],
      },
      {
        q: 'Quanti crediti include il mio piano attuale?',
        a: [
          'Ogni piano di AI Chef Pro include una quantità di crediti mensili. Puoi consultare i crediti assegnati al tuo piano attuale direttamente nel tuo profilo utente all’interno della piattaforma. Se hai dubbi su quale piano si adatti meglio al tuo livello di utilizzo, il nostro team sarà lieto di orientarti.',
        ],
      },
      {
        q: 'Il mio piano includeva un numero di utilizzi al mese. A quanti crediti corrispondono?',
        a: [
          "Ogni piano è stato convertito in un'assegnazione equivalente di crediti, pensata affinché tu possa mantenere — come minimo — lo stesso livello di utilizzo che avevi finora. Puoi consultare i crediti esatti assegnati al tuo piano direttamente nel tuo profilo utente all'interno della piattaforma.",
        ],
      },
      {
        q: 'Cosa succede se finisco i crediti?',
        a: [
          'Se esaurisci i crediti prima del loro rinnovo, potrai acquistare crediti aggiuntivi in modo semplice dal tuo pannello utente, senza bisogno di cambiare piano. Puoi anche scegliere di aggiornare il tuo abbonamento se il tuo utilizzo abituale supera i crediti inclusi nel tuo piano attuale.',
        ],
      },
      {
        q: 'Questo cambiamento rende il mio piano più costoso? Devo fare qualcosa?',
        a: [
          'No. Il prezzo del tuo abbonamento non cambia con l’adozione del sistema di crediti e non devi fare nulla: la conversione in crediti viene applicata automaticamente. Il sistema di crediti modifica unicamente il modo di misurare il consumo, non la quota che paghi. Se in futuro aggiorneremo i piani, te lo comunicheremo sempre in anticipo.',
        ],
      },
      {
        q: 'I crediti scadono?',
        a: [
          "I crediti inclusi nel tuo piano mensile si rinnovano a ogni ciclo di fatturazione. I crediti aggiuntivi acquistati separatamente hanno una propria data di validità, che verrà indicata chiaramente al momento dell'acquisto.",
        ],
      },
      {
        q: 'Tutti gli agenti della piattaforma consumano crediti allo stesso modo?',
        a: [
          'No. Il consumo dipende dal modello di IA utilizzato da ciascun agente e dalla complessità della sessione. Gli agenti basati sui modelli di frontiera di ultima generazione avranno un consumo maggiore rispetto agli agenti con modelli più leggeri. Su ogni agente troverai informazioni chiare sul suo consumo stimato per sessione.',
        ],
      },
      {
        q: 'Aggiungerete altri modelli prossimamente?',
        a: [
          "Sì. L'integrazione del sistema di crediti è proprio ciò che ci permette di attivare nuovi modelli in modo progressivo e nativo all'interno della piattaforma. Nei prossimi giorni incorporeremo nuove opzioni e ti avviseremo via e-mail e dal pannello della piattaforma non appena saranno disponibili.",
        ],
      },
      {
        q: 'Questo cambiamento influisce sulla qualità o sul funzionamento degli agenti specializzati?',
        a: [
          'Assolutamente no. Tutti gli agenti specializzati di AI Chef Pro — Cucina Creativa, Chef Esecutivo, Catering AI+, Concetti di Business e gli altri — continuano a funzionare esattamente allo stesso modo, e in molti casi meglio, grazie al riaddestramento e ai miglioramenti inclusi nella versione 2.1. Il sistema di crediti regola unicamente l’accesso ai modelli, non la qualità né la specializzazione degli agenti.',
        ],
      },
      {
        q: 'Ho altri dubbi, con chi posso parlare?',
        a: [
          `Puoi scriverci a ${SUPPORT_EMAIL} o contattarci tramite la chat all'interno della piattaforma. Il nostro team è disponibile ad aiutarti a comprendere il nuovo sistema e ad assicurarsi che tu continui a ottenere il massimo da AI Chef Pro.`,
        ],
      },
    ],
    supportTitle: 'Hai ancora dei dubbi?',
    supportText:
      'Il nostro team è disponibile ad aiutarti a comprendere il nuovo sistema e a ottenere il massimo da AI Chef Pro.',
    supportCta: 'Scrivici a {email}',
    seoTitle: 'FAQ — Sistema di Crediti | AI Chef Pro',
    seoDescription:
      "Rispondiamo alle tue domande sul nuovo sistema di crediti di AI Chef Pro: cos'è, come si consumano i crediti, cosa include il tuo piano e come ti dà accesso ai modelli di IA più avanzati.",
    seoKeywords:
      'sistema di crediti, AI Chef Pro, crediti IA, modelli di IA, piani, domande frequenti',
  },

  pt: {
    badge: 'Novo sistema de créditos',
    h1: 'Perguntas Frequentes sobre o Novo Sistema de Créditos da AI Chef Pro',
    intro:
      'Estamos a migrar de um sistema de medição por utilizações para um sistema de créditos, o padrão já adotado pela indústria da IA. Aqui respondemos às dúvidas mais frequentes sobre como funciona esta atualização e o que significa para si.',
    breadcrumb: 'Sistema de créditos',
    faqs: [
      {
        q: 'O que é o sistema de créditos e porque é que o adotaram?',
        a: [
          'O sistema de créditos é o modelo padrão atualmente utilizado pelos principais fornecedores de inteligência artificial do mundo. Consiste em atribuir a cada utilizador uma quantidade de créditos que são consumidos em função da utilização que se faz dos modelos de IA disponíveis na plataforma.',
          'Adotámos este sistema porque é o único que nos permite oferecer-lhe acesso nativo aos modelos de fronteira mais avançados do mercado — como o DeepSeek 4, o Gemini 3.5 Flash, o Opus 4.7 ou o GPT-5.5 — diretamente dentro da AI Chef Pro, sem sair da plataforma nem depender de integrações externas.',
        ],
      },
      {
        q: 'O que mudou em relação ao sistema anterior?',
        a: [
          'Até agora, a AI Chef Pro funcionava com um sistema de utilização por defeito, sem distinção consoante o modelo ou a intensidade da utilização. Com o novo sistema de créditos, o consumo ajusta-se à utilização real que faz da plataforma e ao tipo de modelo que utiliza em cada momento. Isto permite-nos ser mais justos, mais transparentes e, sobretudo, oferecer-lhe acesso a ferramentas muito mais potentes.',
        ],
      },
      {
        q: 'Quando entra em vigor o novo sistema de créditos?',
        a: [
          'Estamos a implementar o novo sistema de créditos de forma progressiva na plataforma. Iremos informá-lo por correio eletrónico e a partir do painel da plataforma à medida que for aplicado à sua conta, para que tenha toda a informação antes de qualquer alteração. Entretanto, pode continuar a utilizar a AI Chef Pro com total normalidade.',
        ],
      },
      {
        q: 'Como se consomem os créditos?',
        a: [
          'Cada interação com os agentes da plataforma consome uma quantidade de créditos que varia consoante o modelo utilizado e a extensão da conversa. Os modelos mais avançados e as sessões mais longas ou com maior volume de contexto consomem mais créditos do que as interações simples. No seu painel de utilizador poderá ver a qualquer momento o seu saldo disponível e o seu histórico de consumo.',
        ],
      },
      {
        q: 'Quantos créditos inclui o meu plano atual?',
        a: [
          'Cada plano da AI Chef Pro inclui uma quantidade de créditos mensais. Pode consultar os créditos atribuídos ao seu plano atual diretamente no seu perfil de utilizador dentro da plataforma. Se tiver dúvidas sobre qual o plano que melhor se adapta ao seu nível de utilização, a nossa equipa terá todo o gosto em orientá-lo.',
        ],
      },
      {
        q: 'O meu plano incluía um número de utilizações por mês. A quantos créditos correspondem?',
        a: [
          'Cada plano foi convertido numa atribuição equivalente de créditos, pensada para que possa manter — no mínimo — o mesmo nível de utilização que tinha até agora. Pode consultar os créditos exatos atribuídos ao seu plano diretamente no seu perfil de utilizador dentro da plataforma.',
        ],
      },
      {
        q: 'O que acontece se os meus créditos acabarem?',
        a: [
          'Se esgotar os seus créditos antes de serem renovados, poderá adquirir créditos adicionais de forma simples a partir do seu painel de utilizador, sem necessidade de mudar de plano. Também pode optar por atualizar a sua subscrição se a sua utilização habitual ultrapassar os créditos incluídos no seu plano atual.',
        ],
      },
      {
        q: 'Esta alteração torna o meu plano mais caro? Tenho de fazer alguma coisa?',
        a: [
          'Não. O preço da sua subscrição não muda com a adoção do sistema de créditos e não precisa de fazer nada: a conversão para créditos é aplicada de forma automática. O sistema de créditos altera unicamente a forma de medir o consumo, não a mensalidade que paga. Se no futuro atualizarmos os planos, iremos comunicá-lo sempre com antecedência.',
        ],
      },
      {
        q: 'Os créditos caducam?',
        a: [
          'Os créditos incluídos no seu plano mensal renovam-se a cada ciclo de faturação. Os créditos adicionais adquiridos de forma independente têm a sua própria data de validade, que será claramente indicada no momento da compra.',
        ],
      },
      {
        q: 'Todos os agentes da plataforma consomem créditos da mesma forma?',
        a: [
          'Não. O consumo depende do modelo de IA que cada agente utiliza e da complexidade da sessão. Os agentes baseados em modelos de fronteira de última geração terão um consumo maior do que os agentes com modelos mais leves. Em cada agente encontrará informação clara sobre o seu consumo estimado por sessão.',
        ],
      },
      {
        q: 'Vão acrescentar mais modelos em breve?',
        a: [
          'Sim. A integração do sistema de créditos é precisamente o que nos permite ativar novos modelos de forma progressiva e nativa dentro da plataforma. Nos próximos dias iremos incorporar novas opções e iremos avisá-lo por correio eletrónico e a partir do painel da plataforma assim que estiverem disponíveis.',
        ],
      },
      {
        q: 'Esta alteração afeta a qualidade ou o funcionamento dos agentes especializados?',
        a: [
          'De forma alguma. Todos os agentes especializados da AI Chef Pro — Cozinha de Vanguarda, Chef Executivo, Catering AI+, Conceitos de Negócio e os restantes — continuam a funcionar exatamente da mesma forma e, em muitos casos, melhor, graças ao retreino e às melhorias incluídas na versão 2.1. O sistema de créditos regula unicamente o acesso aos modelos, não a qualidade nem a especialização dos agentes.',
        ],
      },
      {
        q: 'Tenho mais dúvidas, com quem posso falar?',
        a: [
          `Pode escrever-nos para ${SUPPORT_EMAIL} ou contactar-nos através do chat dentro da plataforma. A nossa equipa está disponível para o ajudar a compreender o novo sistema e a garantir que continua a tirar o máximo partido da AI Chef Pro.`,
        ],
      },
    ],
    supportTitle: 'Ainda tem dúvidas?',
    supportText:
      'A nossa equipa está disponível para o ajudar a compreender o novo sistema e a tirar o máximo partido da AI Chef Pro.',
    supportCta: 'Escreva-nos para {email}',
    seoTitle: 'FAQ — Sistema de Créditos | AI Chef Pro',
    seoDescription:
      'Respondemos às suas perguntas sobre o novo sistema de créditos da AI Chef Pro: o que é, como se consomem os créditos, o que inclui o seu plano e como lhe dá acesso aos modelos de IA mais avançados.',
    seoKeywords:
      'sistema de créditos, AI Chef Pro, créditos IA, modelos de IA, planos, perguntas frequentes',
  },

  nl: {
    badge: 'Nieuw creditsysteem',
    h1: 'Veelgestelde Vragen over het Nieuwe Creditsysteem van AI Chef Pro',
    intro:
      'We stappen over van een systeem dat het gebruik meet naar een creditsysteem — de standaard die de AI-industrie inmiddels heeft omarmd. Hier beantwoorden we de meest gestelde vragen over hoe deze update werkt en wat die voor jou betekent.',
    breadcrumb: 'Creditsysteem',
    faqs: [
      {
        q: 'Wat is het creditsysteem en waarom hebben jullie het ingevoerd?',
        a: [
          'Het creditsysteem is het standaardmodel dat momenteel wordt gebruikt door de belangrijkste aanbieders van kunstmatige intelligentie ter wereld. Het houdt in dat aan elke gebruiker een hoeveelheid credits wordt toegekend die worden verbruikt op basis van het gebruik van de AI-modellen die op het platform beschikbaar zijn.',
          'We hebben dit systeem ingevoerd omdat het het enige is waarmee we je native toegang kunnen bieden tot de meest geavanceerde frontier-modellen op de markt — zoals DeepSeek 4, Gemini 3.5 Flash, Opus 4.7 of GPT-5.5 — rechtstreeks binnen AI Chef Pro, zonder het platform te verlaten of afhankelijk te zijn van externe integraties.',
        ],
      },
      {
        q: 'Wat is er veranderd ten opzichte van het vorige systeem?',
        a: [
          'Tot nu toe werkte AI Chef Pro met een standaard gebruikssysteem, zonder onderscheid op basis van het model of de gebruiksintensiteit. Met het nieuwe creditsysteem past het verbruik zich aan op het werkelijke gebruik dat je van het platform maakt en op het type model dat je op elk moment gebruikt. Zo kunnen we eerlijker en transparanter zijn en, bovenal, je toegang bieden tot veel krachtigere tools.',
        ],
      },
      {
        q: 'Wanneer treedt het nieuwe creditsysteem in werking?',
        a: [
          'We voeren het nieuwe creditsysteem geleidelijk in op het platform. We brengen je per e-mail en via het platformpaneel op de hoogte zodra het op je account wordt toegepast, zodat je over alle informatie beschikt vóór elke wijziging. In de tussentijd kun je AI Chef Pro gewoon blijven gebruiken.',
        ],
      },
      {
        q: 'Hoe worden credits verbruikt?',
        a: [
          'Elke interactie met de agents van het platform verbruikt een hoeveelheid credits die varieert afhankelijk van het gebruikte model en de lengte van het gesprek. Geavanceerdere modellen en langere sessies of sessies met een groter contextvolume verbruiken meer credits dan eenvoudige interacties. In je gebruikerspaneel kun je op elk moment je beschikbare saldo en je verbruiksgeschiedenis bekijken.',
        ],
      },
      {
        q: 'Hoeveel credits bevat mijn huidige abonnement?',
        a: [
          'Elk abonnement van AI Chef Pro bevat een maandelijkse hoeveelheid credits. Je kunt de credits die aan je huidige abonnement zijn toegekend rechtstreeks raadplegen in je gebruikersprofiel binnen het platform. Twijfel je welk abonnement het beste bij je gebruiksniveau past, dan adviseert ons team je graag.',
        ],
      },
      {
        q: 'Mijn abonnement bevatte een aantal gebruiken per maand. Met hoeveel credits komt dat overeen?',
        a: [
          'Elk abonnement is omgezet naar een gelijkwaardige hoeveelheid credits, zo bepaald dat je minstens hetzelfde gebruiksniveau kunt behouden als voorheen. Je kunt de exacte credits die aan je abonnement zijn toegekend rechtstreeks raadplegen in je gebruikersprofiel binnen het platform.',
        ],
      },
      {
        q: 'Wat gebeurt er als mijn credits op zijn?',
        a: [
          'Als je je credits opmaakt voordat ze worden vernieuwd, kun je eenvoudig extra credits aanschaffen via je gebruikerspaneel, zonder van abonnement te hoeven veranderen. Je kunt er ook voor kiezen je abonnement te upgraden als je gebruikelijke gebruik de credits in je huidige abonnement overschrijdt.',
        ],
      },
      {
        q: 'Wordt mijn abonnement door deze wijziging duurder? Moet ik iets doen?',
        a: [
          'Nee. De prijs van je abonnement verandert niet door de invoering van het creditsysteem, en je hoeft niets te doen: de omzetting naar credits gebeurt automatisch. Het creditsysteem verandert alleen de manier waarop het verbruik wordt gemeten, niet het bedrag dat je betaalt. Mochten we de abonnementen in de toekomst aanpassen, dan laten we je dat altijd vooraf weten.',
        ],
      },
      {
        q: 'Verlopen credits?',
        a: [
          'De credits die in je maandabonnement zijn inbegrepen, worden bij elke factureringscyclus vernieuwd. Apart aangeschafte extra credits hebben hun eigen geldigheidsdatum, die duidelijk wordt aangegeven op het moment van aankoop.',
        ],
      },
      {
        q: 'Verbruiken alle agents van het platform credits op dezelfde manier?',
        a: [
          'Nee. Het verbruik hangt af van het AI-model dat elke agent gebruikt en van de complexiteit van de sessie. Agents die gebaseerd zijn op de nieuwste generatie frontier-modellen hebben een hoger verbruik dan agents met lichtere modellen. Bij elke agent vind je duidelijke informatie over het geschatte verbruik per sessie.',
        ],
      },
      {
        q: 'Gaan jullie binnenkort meer modellen toevoegen?',
        a: [
          'Ja. De integratie van het creditsysteem is juist wat ons in staat stelt om nieuwe modellen geleidelijk en native binnen het platform te activeren. In de komende dagen voegen we nieuwe opties toe en brengen we je per e-mail en via het platformpaneel op de hoogte zodra ze beschikbaar zijn.',
        ],
      },
      {
        q: 'Heeft deze wijziging invloed op de kwaliteit of werking van de gespecialiseerde agents?',
        a: [
          'Absoluut niet. Alle gespecialiseerde agents van AI Chef Pro — Avant-garde Cuisine, Executive Chef, Catering AI+, Bedrijfsconcepten en de rest — blijven exact hetzelfde werken, en in veel gevallen beter, dankzij de hertraining en verbeteringen in versie 2.1. Het creditsysteem regelt uitsluitend de toegang tot de modellen, niet de kwaliteit of de specialisatie van de agents.',
        ],
      },
      {
        q: 'Ik heb meer vragen — met wie kan ik praten?',
        a: [
          `Je kunt ons mailen op ${SUPPORT_EMAIL} of contact met ons opnemen via de chat binnen het platform. Ons team staat klaar om je te helpen het nieuwe systeem te begrijpen en ervoor te zorgen dat je het maximale uit AI Chef Pro blijft halen.`,
        ],
      },
    ],
    supportTitle: 'Nog vragen?',
    supportText:
      'Ons team staat klaar om je te helpen het nieuwe systeem te begrijpen en het maximale uit AI Chef Pro te halen.',
    supportCta: 'Mail ons op {email}',
    seoTitle: 'FAQ — Creditsysteem | AI Chef Pro',
    seoDescription:
      'We beantwoorden je vragen over het nieuwe creditsysteem van AI Chef Pro: wat het is, hoe credits worden verbruikt, wat je abonnement bevat en hoe het je toegang geeft tot de meest geavanceerde AI-modellen.',
    seoKeywords:
      'creditsysteem, AI Chef Pro, AI-credits, AI-modellen, abonnementen, veelgestelde vragen',
  },
};
