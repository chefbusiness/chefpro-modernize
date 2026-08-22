// Portugués content for use-case spokes.
// Each entry mirrors the structure of USE_CASES_CONTENT_ES.
// Missing entries fall back to ES at runtime via makeContent() in use-cases.ts.
//
// Generado el 2026-08-15 con scripts/astro-migration/fase10-traducir-spokes.py
// (bridge.py ~deepseek/deepseek-v4-flash-latest, --strict-lang) y el glosario
// de la PLATAFORMA viva fase10-glosario-pt.json. Los agentes sin versión
// pt se preservan verbatim a propósito (decisión de catálogo pendiente,
// ver CATALOGO_ITALIANO_PENDIENTE.md — aplica a los 5 idiomas).
//
// NO editar a mano campo a campo: productIds, galleryImages, features[].icon,
// seo.ogImage y testimonialAuthor se preservan verbatim desde el ES y el
// validador del script lo comprueba. Regenerar PISA ediciones manuales.

import type { UseCaseContent } from './use-cases';

export const USE_CASES_CONTENT_PT: Record<string, UseCaseContent> = {
  "propietario-restaurante": {
    "h1": "IA para Proprietários de Restaurante",
    "heroSubtitle": "Tome melhores decisões, recupere horas administrativas e aumente a rentabilidade do seu restaurante com uma suite de agentes de IA especializados em hotelaria.",
    "heroTagline": "O seu sócio digital para gerir o negócio com dados",
    "badge": "Para proprietários e donos de restaurante",
    "painsTitle": "O Que um Proprietário de Restaurante Não Pode Deixar de Resolver",
    "pains": [
      "Margem estreita: custa saber que pratos rendem e quais sangram rentabilidade sem uma análise precisa.",
      "Tempo escasso para rever custos, escandallos, fornecedores e comunicação com a equipa.",
      "Decisões de menu, preços e promoções tomadas mais por intuição do que por dados.",
      "Equipas rotativas: formar, supervisionar e gerir turnos consome horas todas as semanas.",
      "Reporting financeiro ao gestor ou a investidores que requer documentos limpos e consolidados.",
      "Marketing e comunicação constantes (redes, web, email) que distraem do negócio em si."
    ],
    "featuresTitle": "Como o AI Chef Pro Ajuda um Proprietário",
    "features": [
      {
        "icon": "BriefcaseBusiness",
        "title": "Gerente Restaurante Pro",
        "description": "Agente especializado para apoiar o proprietário em operações diárias, decisões de equipa e reporting ao investidor."
      },
      {
        "icon": "FileText",
        "title": "Plano financeiro profissional",
        "description": "Kit Plan Financiero: cash flow, ponto de equilíbrio, P&L mensal e dashboard de rácios. Modelos prontos para investidores e bancos."
      },
      {
        "icon": "Calculator",
        "title": "Fichas técnicas profissionais",
        "description": "Culinária Criativa entrega receita + ficha técnica inicial CSV com preços de referência; o Kit de Escandallos Pro gere-o com os seus preços reais."
      },
      {
        "icon": "ShieldCheck",
        "title": "APPCC e segurança alimentar",
        "description": "Pack APPCC com 19 registos prontos para inspeção, registos desde o telemóvel e folhas prontas a imprimir em A4."
      },
      {
        "icon": "Users",
        "title": "Gestão de pessoal e turnos",
        "description": "Kit Gestión de Personal: quadros de horários, controlo de horas, rácios de produtividade e onboarding de novos colaboradores."
      },
      {
        "icon": "Sparkles",
        "title": "MenuDish Local SEO + BlogPost SEO Gen+",
        "description": "Suite de marketing e SEO local: descrições de prato, blog e campanhas com IA para captar tráfego orgânico."
      },
      {
        "icon": "Search",
        "title": "Keyword Discovery AI+",
        "description": "Investigação de palavras-chave gastronómicas locais para posicionar o seu restaurante no Google sem pagar agência."
      },
      {
        "icon": "BarChart3",
        "title": "Refeição do Pessoal",
        "description": "Gerador de menus de staff que poupa custos mantendo motivada a equipa de cozinha e sala."
      },
      {
        "icon": "MessageSquare",
        "title": "Coach Mental",
        "description": "Coaching psicológico para profissionais de hotelaria: gestão do stress, equilíbrio trabalho-vida e direção de equipas em setores de alta pressão."
      }
    ],
    "workflowTitle": "Um Dia Real de um Proprietário com AI Chef Pro",
    "workflow": [
      "08:30 · Café e dashboard — abre o Kit Plan Financiero e revê os rácios do dia anterior. Deteta que o food cost subiu para 33 % por mermas em peixe.",
      "09:30 · Gerente Restaurante Pro — pede análise da causa ao agente e obtém 3 ações concretas para esta semana.",
      "10:30 · MenuDish Local SEO — atualiza a descrição dos 4 pratos top no Google Business e no site com palavras-chave que o Keyword Discovery AI+ detetou.",
      "12:30 · Serviço de meio-dia — supervisiona a sala apoiado na checklist do Kit de Tareas Restaurante Casual.",
      "15:30 · Reunião com gestor — exporta P&L mensal, dashboard de rácios e escala de pessoal em PDF diretamente do Kit Plan Financiero. Reunião concluída em 30 minutos.",
      "17:00 · Culinária Criativa — pede ideias para o menu da estação que vem. O agente entrega 8 pratos com receita e escandallo CSV.",
      "18:30 · Decisão de equipa — usa Coach Mental para preparar a conversa difícil com um colaborador-chave. Leva estrutura e argumentos para a reunião.",
      "21:00 · Encerramento — o gerente envia-lhe o relatório automático do dia por WhatsApp. Vai para casa sem papelada pendente."
    ],
    "productsTitle": "Modelos e Kits Descarregáveis para Proprietários",
    "productIds": [
      "kit-plan-financiero",
      "kit-escandallos",
      "pack-appcc",
      "kit-gestion-personal",
      "kit-inventario",
      "pro-prompts-ebook"
    ],
    "testimonialQuote": "Antes passava 6 horas por semana apenas a fechar contas entre Excel e guardanapos. Com AI Chef Pro fecho-o numa hora com dashboards profissionais. Recuperei o controlo financeiro dos meus dois locais e a margem subiu 3 pontos no primeiro trimestre.",
    "testimonialAuthor": "Carlos Méndez",
    "testimonialRole": "Proprietário, grupo de bistrôs mediterrânicos (2 locais)",
    "faqTitle": "Perguntas Frequentes de Proprietários",
    "faqs": [
      {
        "q": "Que tamanho de restaurante encaixa com AI Chef Pro?",
        "a": "Desde um único local familiar até grupos com mais de 10 restaurantes. Os modelos escalam ao volume e os planos ajustam-se ao uso real. Há clientes com 1 local e outros com 25 unidades ativas."
      },
      {
        "q": "Preciso de conhecimentos técnicos?",
        "a": "Não. Se sabe usar WhatsApp e Excel a nível básico, já sabe usar AI Chef Pro. O onboarding começa com o agente «Quem Sou Eu?», que em 2 minutos adapta o sistema a si, ao seu negócio e à sua zona geográfica. Há vídeos curtos de onboarding e suporte direto por WhatsApp."
      },
      {
        "q": "Substitui o meu gestor ou consultor?",
        "a": "Não, mas facilita-lhes muito a vida. O seu gestor recebe documentos limpos e você chega às reuniões com dados consolidados. A maioria das gestoras acaba por recomendar AI Chef Pro a outros clientes."
      },
      {
        "q": "Quanto tempo demoro a ver resultados?",
        "a": "A maioria dos proprietários reporta entre 4 e 6 horas semanais recuperadas na primeira semana de uso. O impacto na margem costuma estar entre 2 e 5 pontos percentuais em 60-90 dias, graças ao redesenho de pratos com food cost alto e ao controlo de mermas."
      },
      {
        "q": "Como me ajuda com o marketing e o SEO local?",
        "a": "A suite Conteúdos e Redes Sociais inclui MenuDish Local SEO (descrições de prato otimizadas), BlogPost SEO Gen+ (posts para captar tráfego orgânico) e Keyword Discovery AI+ (palavras-chave gastronómicas locais). Reduz gastos em agências de marketing e capta reservas diretas."
      },
      {
        "q": "Há descontos para grupos com vários locais?",
        "a": "Sim. A partir de 5 unidades ativas há planos empresa com onboarding personalizado e dashboards consolidados por grupo."
      }
    ],
    "ctaTitle": "Gira o seu restaurante com dados, não com intuição.",
    "ctaSubtitle": "Comece com o onboarding de 2 minutos. Plano Membro por 10 € por mês com 10.000 créditos para usar todos os agentes.",
    "seo": {
      "title": "IA para Proprietários de Restaurante: Plano Financeiro, Fichas Técnicas, SEO | AI Chef Pro",
      "description": "Suite de IA para proprietários de restaurante: agentes especializados, plano financeiro, fichas técnicas profissionais, APPCC, marketing e SEO local. Comece hoje.",
      "keywords": "IA proprietário restaurante, dono restaurante IA, software gestão restaurante proprietários, plano financeiro restaurante IA, fichas técnicas restaurante, marketing restaurante IA, SEO local restaurante, agente IA hotelaria, proprietário restaurante Espanha",
      "ogImage": "https://aichef.pro/og/use-cases/propietario-restaurante.jpg"
    },
    "personalizationTitle": "Personalizado ao Seu Negócio desde o Minuto Um",
    "personalizationBody": "AI Chef Pro arranca com o agente «Quem Sou Eu?», um onboarding conversacional de 2 minutos em que lhe conta que tipo de restaurante tem, em que cidade, quantos locais, qual o ticket médio que gere e como trabalha. A partir desse momento, cada agente —desde o Plano Financeiro até ao SEO local— responde adaptado ao seu contexto: preços de mercado da sua zona, normativa do seu país e escala real da sua operação. Não é um formulário: é uma conversa curta que torna cada ferramenta verdadeiramente útil para o seu negócio.",
    "appsTitle": "Os Agentes IA que Vai Usar como Proprietário",
    "apps": [
      {
        "name": "Gerente Restaurante Pro",
        "category": "Gastro Profile Pro",
        "description": "Assistente operativo e financeiro para apoiá-lo em decisões de equipa, reporting e operações diárias."
      },
      {
        "name": "Restaurantes Casuais AI+",
        "category": "Conceitos de Negócio",
        "description": "Especialista em bistrôs, gastrobares, tapas e mediterrâneo: o espetro casual completo com base profissional."
      },
      {
        "name": "MenuDish Local SEO",
        "category": "Conteúdos e Redes Sociais",
        "description": "Descrições de prato otimizadas para SEO local no Google Business e web."
      },
      {
        "name": "BlogPost SEO Gen+",
        "category": "Conteúdos e Redes Sociais",
        "description": "Posts de blogue que captam tráfego orgânico local para o seu restaurante."
      },
      {
        "name": "Keyword Discovery AI+",
        "category": "Conteúdos e Redes Sociais",
        "description": "Investigação de palavras-chave gastronómicas locais por zona postal."
      },
      {
        "name": "Culinária Criativa",
        "category": "Criatividade Culinária",
        "description": "Desenvolvimento de pratos profissionais com receita + ficha técnica inicial CSV (preços de referência) pronto para o Kit de Escandallos Pro."
      },
      {
        "name": "Mermas Genéricas",
        "category": "Ferramentas e Utilitários",
        "description": "Dados precisos de mermas e rendimentos por ingrediente, essenciais para a ficha técnica realista."
      },
      {
        "name": "ID Alergénios",
        "category": "Ferramentas e Utilitários",
        "description": "Identificação automática de alergénios por receita e prato, pronta para regulamentação."
      },
      {
        "name": "Refeição do Pessoal",
        "category": "Gastro Profile Pro",
        "description": "Gerador de menus de staff que poupa custos mantendo motivada a equipa."
      },
      {
        "name": "Coach Mental",
        "category": "Ferramentas e Utilitários",
        "description": "Coaching psicológico para profissionais de hotelaria: stress, equipas e decisões difíceis."
      },
      {
        "name": "Gastro Calendar",
        "category": "Conteúdos e Redes Sociais",
        "description": "Calendário gastronómico com datas-chave, ideias e hashtags para redes e blog."
      },
      {
        "name": "InstaFlow AI Pro + Gerador de Pins Pinterest",
        "category": "Conteúdos e Redes Sociais",
        "description": "Conteúdo viral para Instagram e Pinterest sem agência."
      }
    ],
    "metrics": [
      {
        "value": "+3 pp",
        "label": "margem em 60-90 dias"
      },
      {
        "value": "−6 h",
        "label": "semanais em gestão"
      },
      {
        "value": "×2",
        "label": "reservas diretas via SEO local"
      },
      {
        "value": "12+",
        "label": "agentes de IA para o seu papel"
      }
    ],
    "beforeAfter": {
      "beforeTitle": "Sem AI Chef Pro",
      "beforeItems": [
        "6 horas semanais a fechar contas em Excel, guardanapos e notas de fornecedores",
        "Decisões de menu e pricing por intuição, não por análise de food cost real",
        "Reporting ao gestor com ficheiros dispersos em Word, Excel e email",
        "Marketing improvisado ou externalizado a preços elevados sem saber o que funciona",
        "Stress constante e quebra em feriados por não largar o controlo"
      ],
      "afterTitle": "Com AI Chef Pro",
      "afterItems": [
        "1 hora semanal a fechar dashboards profissionais com KPIs claros",
        "Decisões de menu e pricing com ficha técnica profissional e análise de margem",
        "Reporting ao gestor em PDF diretamente do Kit Plan Financiero",
        "SEO local automatizado e suite de marketing IA reduzindo gastos em agências",
        "Tranquilidade: a equipa envia-lhe relatórios automáticos por WhatsApp"
      ]
    },
    "galleryTitle": "O Dia a Dia de um Proprietário, em Imagens",
    "gallerySubtitle": "O que vai poder gerir com AI Chef Pro: dashboards financeiros, decisões operativas, equipa, sala e reporting.",
    "galleryImages": [
      "/lovable-uploads/ai-gallery/use-case-propietario-restaurante-hero.jpg",
      "/lovable-uploads/ai-gallery/use-case-propietario-restaurante-tablet.jpg",
      "/lovable-uploads/ai-gallery/use-case-propietario-restaurante-meeting.jpg",
      "/lovable-uploads/ai-gallery/use-case-propietario-restaurante-numbers.jpg",
      "/lovable-uploads/ai-gallery/use-case-propietario-restaurante-team.jpg",
      "/lovable-uploads/ai-gallery/use-case-propietario-restaurante-dining.jpg"
    ]
  },
  "gerente-restaurante": {
    "h1": "IA para Gerentes e Gestores de Restaurante",
    "heroSubtitle": "Otimize operações diárias, controle custos e recupere horas de trabalho administrativo com uma suite de agentes de IA pensados para o dia a dia do gerente de restaurante.",
    "heroTagline": "Mais controlo operativo, menos folhas soltas",
    "badge": "Para gerentes e gestores",
    "painsTitle": "O Que um Gerente de Restaurante Não Pode Deixar de Resolver",
    "pains": [
      "Fechar turnos todas as semanas respeitando o acordo, jornada legal e descansos sem desvios nem sobrecustos",
      "Controlar mermas, inventário e compras com fornecedores diferentes que mudam de preço todas as semanas",
      "Manter o APPCC em dia e preparar inspeções sem stress nem acumulação de papelada",
      "Reportar ao proprietário com dados consolidados e dashboards profissionais, não em Excel improvisados",
      "Coordenar a equipa de cozinha e sala com comunicação clara e formação rápida do novo pessoal",
      "Gerir a operação dos picos de serviço sem perder qualidade nem descuidar a sala"
    ],
    "featuresTitle": "Como o AI Chef Pro Ajuda um Gerente",
    "features": [
      {
        "icon": "BriefcaseBusiness",
        "title": "Gerente Restaurante Pro",
        "description": "Agente especializado para apoiá-lo em decisões operativas, gestão da equipa e reporting ao proprietário."
      },
      {
        "icon": "Calendar",
        "title": "Quadrantes e controlo de turnos",
        "description": "Kit Gestión de Personal: quadrantes em minutos respeitando o acordo, controlo de horas, rácios de produtividade."
      },
      {
        "icon": "Package",
        "title": "Inventário e controlo de compras",
        "description": "Kit Inventario: modelos Excel prontos, alertas de stock mínimo, comparação de fornecedores e mermas."
      },
      {
        "icon": "ShieldCheck",
        "title": "APPCC e rastreabilidade",
        "description": "Pack APPCC com 19 registos, alertas de temperatura a partir do telemóvel e folhas prontas para inspeção."
      },
      {
        "icon": "BarChart3",
        "title": "KPIs e reporting ao proprietário",
        "description": "Rácios de cozinha e sala, produtividade, ticket médio. Dashboards exportáveis para PDF diretamente a partir do Excel."
      },
      {
        "icon": "CheckSquare",
        "title": "Tarefas recorrentes por turno",
        "description": "Modelos prontos por conceito: abertura, fecho, partida e serviço num único kit por tipo de negócio."
      },
      {
        "icon": "Users",
        "title": "Refeição do Pessoal",
        "description": "Gerador de menus de staff que poupa custo mantendo a equipa motivada e bem alimentada."
      },
      {
        "icon": "MessageSquare",
        "title": "Coach Mental",
        "description": "Coaching psicológico para gerir conversas difíceis, stress e motivação da equipa."
      },
      {
        "icon": "ShieldCheck",
        "title": "ID Alergénios",
        "description": "Identificação automática de alergénios por prato, pronta para regulamentação e para a sala."
      }
    ],
    "workflowTitle": "Um Dia Real de um Gerente com AI Chef Pro",
    "workflow": [
      "08:30 · Abertura — imprime a checklist do turno a partir do Kit de Tareas e revê o inventário em 10 minutos.",
      "09:30 · Gerente Restaurante Pro — o agente resume-lhe as incidências do dia anterior e as ações pendentes.",
      "10:30 · Kit Inventario — valida pedidos a fornecedores com comparação de preços e alertas de stock mínimo.",
      "12:30 · Serviço de meio-dia — a equipa regista mermas e temperaturas a partir do telemóvel com o Pack APPCC.",
      "15:30 · Quadrante da próxima semana — abre o Kit Gestión de Personal e fecha o quadrante em 20 minutos respeitando o acordo.",
      "17:00 · Refeição do Pessoal — gera o menu do staff da próxima semana com ingredientes que já tem na câmara.",
      "19:00 · Conversa difícil — usa o Coach Mental para preparar a conversa com um cozinheiro que chega atrasado repetidamente.",
      "23:30 · Fecho — gera o relatório diário com rácios e envia-o ao proprietário por WhatsApp com um toque."
    ],
    "productsTitle": "Modelos e Kits Descarregáveis para Gerentes",
    "productIds": [
      "kit-gestion-personal",
      "kit-inventario",
      "pack-appcc",
      "kit-tareas",
      "kit-escandallos",
      "kit-plan-financiero"
    ],
    "testimonialQuote": "Antes passava 8 horas por semana só a fechar turnos e pedidos a fornecedores. Agora fecho isso em 2 horas com o Kit Gestión de Personal e o Kit Inventario. O AI Chef Pro devolveu-me tempo para estar na sala com a equipa, que é onde um gerente deve estar.",
    "testimonialAuthor": "Marta Ruiz",
    "testimonialRole": "Gerente, restaurante casual de 80 lugares",
    "faqTitle": "Perguntas Frequentes de Gerentes",
    "faqs": [
      {
        "q": "Funciona se eu gerir 1 local ou se tiver vários?",
        "a": "Em ambos os casos. Os modelos escalam com o volume e pode consolidar o reporting de vários locais num único dashboard. Há clientes com 1 local e outros com mais de 10 unidades ativas."
      },
      {
        "q": "Substitui o software de reservas ou o TPV?",
        "a": "Não, complementa. O Cover Manager ou o The Fork gerem reservas e o TPV gere vendas; o AI Chef Pro gere custos, pessoal, APPCC, inventário e operação interna. Os dados são perfeitamente compatíveis via Excel."
      },
      {
        "q": "A equipa precisa de formação?",
        "a": "Mínima. Os modelos e os agentes estão em espanhol e tudo arranca com o agente «Quem Sou Eu?», que adapta o sistema a si em 2 minutos. A curva real da equipa é de 1-2 dias com o onboarding em vídeo e suporte por WhatsApp."
      },
      {
        "q": "Posso exportar os dados para o meu gestor ou o proprietário?",
        "a": "Sim. Tudo se exporta para Excel e PDF em formato profissional. As gestoras recebem documentação limpa e os proprietários recebem dashboards com KPIs claros diretamente no WhatsApp."
      },
      {
        "q": "Como me ajuda com conversas difíceis da equipa?",
        "a": "O Coach Mental é um agente de coaching psicológico para profissionais de hotelaria que o ajuda a estruturar conversas difíceis (despedimentos, atrasos, conflitos entre cozinha e sala) com argumentos e estrutura clara antes da reunião."
      },
      {
        "q": "Existem modelos específicos por conceito de negócio?",
        "a": "Sim. Existem Kits de Tarefas específicos para casual, cafetaria, pizzaria, hamburgueria, dark kitchen, pastelaria, bar, catering, hotel, gelataria, chocolataria, restaurante criativo e chef privado. Cada um com modelos adaptados à operação real."
      }
    ],
    "ctaTitle": "Leve a operação do seu restaurante para o próximo nível.",
    "ctaSubtitle": "Comece com o onboarding de 2 minutos. Plano Membro por 10 € por mês com 10.000 créditos para usar todos os agentes.",
    "seo": {
      "title": "IA para Gerentes e Gestores de Restaurante: Turnos, APPCC e Reporting | AI Chef Pro",
      "description": "Suite de IA para gestores de restaurante: quadrantes, inventário, APPCC, KPIs e reporting ao proprietário com agentes especializados em hotelaria. Comece hoje.",
      "keywords": "IA gerente restaurante, gestor restaurante IA, software gestor restaurante, gestão operativa restaurante IA, quadrantes turnos restaurante, APPCC gestor, KPIs restaurante, agente IA hotelaria, gerente restaurante Espanha",
      "ogImage": "https://aichef.pro/og/use-cases/gerente-restaurante.jpg"
    },
    "personalizationTitle": "Personalizado ao Seu Restaurante desde o Minuto Um",
    "personalizationBody": "O AI Chef Pro arranca com o agente «Quem Sou Eu?», um onboarding conversacional de 2 minutos em que lhe conta que tipo de restaurante gere, em que cidade, quantos comensais atende e como trabalha. A partir desse momento, cada agente —desde os quadrantes até ao reporting— responde adaptado ao seu contexto: convenção do país, escala da sua equipa, picos de serviço reais. Não é um formulário: é uma conversa curta que torna a suite verdadeiramente útil para o seu dia a dia como gerente.",
    "appsTitle": "Os Agentes de IA que Vai Usar como Gerente",
    "apps": [
      {
        "name": "Gerente Restaurante Pro",
        "category": "Gastro Profile Pro",
        "description": "Agente principal: decisões operativas, gestão da equipa e reporting ao proprietário."
      },
      {
        "name": "Restaurantes Casuais AI+",
        "category": "Conceitos de Negócio",
        "description": "Especialista em bistrôs, gastrobares, tapas e mediterrâneo: o espetro casual completo."
      },
      {
        "name": "Refeição do Pessoal",
        "category": "Gastro Profile Pro",
        "description": "Gerador de menus de staff que poupa custo e motiva a equipa."
      },
      {
        "name": "Mermas Genéricas",
        "category": "Ferramentas e Utilitários",
        "description": "Dados precisos de mermas e rendimentos por ingrediente, essenciais para controlo de cozinha."
      },
      {
        "name": "ID Alergénios",
        "category": "Ferramentas e Utilitários",
        "description": "Identificação automática de alergénios por receita e prato."
      },
      {
        "name": "Conversor Ing",
        "category": "Ferramentas e Utilitários",
        "description": "Conversor de pesos e medidas para cozinha profissional."
      },
      {
        "name": "Calcula Pax",
        "category": "Ferramentas e Utilitários",
        "description": "Calculadora de porções que escala receitas para qualquer número de comensais."
      },
      {
        "name": "Coach Mental",
        "category": "Ferramentas e Utilitários",
        "description": "Coaching psicológico para profissionais de hotelaria: stress, conversas difíceis e motivação da equipa."
      },
      {
        "name": "MenuDish Local SEO",
        "category": "Conteúdos e Redes Sociais",
        "description": "Descrições de prato otimizadas para SEO local no Google e no site do restaurante."
      },
      {
        "name": "Gastro Calendar",
        "category": "Conteúdos e Redes Sociais",
        "description": "Calendário gastronómico com datas-chave, ideias e hashtags para redes e blog."
      },
      {
        "name": "Culinária Criativa",
        "category": "Criatividade Culinária",
        "description": "Desenvolvimento de pratos profissionais com receita + escandallo CSV para carregar no Kit de Escandallos Pro."
      }
    ],
    "metrics": [
      {
        "value": "−75 %",
        "label": "tempo em quadrantes e pedidos"
      },
      {
        "value": "×4",
        "label": "velocidade de reporting ao proprietário"
      },
      {
        "value": "−40 %",
        "label": "mermas após controlo sistemático"
      },
      {
        "value": "11+",
        "label": "agentes de IA para o seu cargo"
      }
    ],
    "beforeAfter": {
      "beforeTitle": "Sem AI Chef Pro",
      "beforeItems": [
        "8 horas semanais a fechar turnos em Excel manual e notas de fornecedores",
        "APPCC em papel impresso que se perde ou chega incompleto à inspeção",
        "Reporting ao proprietário em ficheiros dispersos por email sem estrutura",
        "Mermas registadas a olho, sem rastreabilidade real nem alertas",
        "Refeição do pessoal improvisada que dispara custo sem que ninguém note"
      ],
      "afterTitle": "Com AI Chef Pro",
      "afterItems": [
        "2 horas semanais a fechar quadrantes com modelo profissional respeitando o acordo",
        "APPCC a partir do telemóvel com registos, temperaturas e alertas pronto para inspeção",
        "Reporting ao proprietário em PDF direto do Kit Plan Financiero, com dashboards claros",
        "Controlo sistemático de mermas com dados precisos e alertas de stock",
        "Refeição do pessoal gerada com IA respeitando custo objetivo e motivação da equipa"
      ]
    },
    "galleryTitle": "O Dia a Dia de um Gerente, em Imagens",
    "gallerySubtitle": "O que vai coordenar com o AI Chef Pro: planeamento de turnos, gestão de cozinha e sala, inventário, serviço e reporting.",
    "galleryImages": [
      "/lovable-uploads/ai-gallery/use-case-gerente-restaurante-hero.jpg",
      "/lovable-uploads/ai-gallery/use-case-gerente-restaurante-shifts.jpg",
      "/lovable-uploads/ai-gallery/use-case-gerente-restaurante-kitchen.jpg",
      "/lovable-uploads/ai-gallery/use-case-gerente-restaurante-inventory.jpg",
      "/lovable-uploads/ai-gallery/use-case-gerente-restaurante-service.jpg",
      "/lovable-uploads/ai-gallery/use-case-gerente-restaurante-reporting.jpg"
    ]
  },
  "director-operaciones-grupo": {
    "h1": "IA para Diretores de Operações de Grupos de Restauração",
    "heroSubtitle": "Padronize processos, consolide relatórios e multiplique a produtividade operacional em grupos multi-local com uma suíte de agentes de IA especializados em restauração.",
    "heroTagline": "Mesmo padrão em todos os locais, dados consolidados num clique",
    "badge": "Para diretores de operações de grupos",
    "painsTitle": "O Que um Diretor de Operações Multi-Local Não Pode Deixar de Resolver",
    "pains": [
      "Manter o mesmo padrão de qualidade, processos e experiência em todos os locais do grupo",
      "Consolidar KPIs financeiros, operacionais e de equipa para comparar desempenho entre unidades",
      "Replicar manuais operacionais, formação e onboarding sem perder qualidade quando a rede cresce",
      "Detetar a tempo os locais com desvios de food cost, pessoal ou produtividade antes de que comprometam a margem",
      "Coordenar os gerentes de cada local com comunicação clara e relatórios consistentes",
      "Escalar o grupo abrindo novas unidades sem ter de reinventar a roda em cada abertura"
    ],
    "featuresTitle": "Como a AI Chef Pro Ajuda um Diretor de Operações",
    "features": [
      {
        "icon": "Building2",
        "title": "Padronização multi-local",
        "description": "Manuais, checklists e procedimentos uniformes que são replicados para todas as unidades do grupo com um clique."
      },
      {
        "icon": "BarChart3",
        "title": "Dashboards consolidados",
        "description": "Kit Plan Financiero: compare food cost, produtividade, mermas e ticket médio entre todos os seus restaurantes numa única vista."
      },
      {
        "icon": "ChefHat",
        "title": "Chef Executivo Pro",
        "description": "Agente que padroniza receitas e fichas técnicas para que o mesmo prato saia igual em 1, 5 ou 25 cozinhas."
      },
      {
        "icon": "BriefcaseBusiness",
        "title": "Gerente Restaurante Pro",
        "description": "Assistente para cada gerente local que reporta ao diretor de operações com dados consolidados."
      },
      {
        "icon": "BookOpen",
        "title": "Manuais operacionais com IA",
        "description": "Onboarding, formação de equipas e procedimentos sempre atualizados a partir de um único repositório central."
      },
      {
        "icon": "ShieldCheck",
        "title": "APPCC corporativo unificado",
        "description": "Um único sistema documental para todas as unidades do grupo: rastreabilidade e temperaturas centralizadas."
      },
      {
        "icon": "TrendingDown",
        "title": "Auditoria de custos por local",
        "description": "Mermas Genéricas e Kit de Escandallos Pro detetam desvios de food cost antes de que fiquem fora de controlo."
      },
      {
        "icon": "Users",
        "title": "Escalas e estrutura de equipa",
        "description": "Kit Gestión de Personal: mesma estrutura de turnos, rácios e produtividade em todas as unidades."
      },
      {
        "icon": "Search",
        "title": "Sonar Deep Research",
        "description": "Pesquisa aprofundada de tendências, concorrentes e mercados para decisões estratégicas de expansão."
      }
    ],
    "workflowTitle": "Um Dia Real de um Diretor de Operações com AI Chef Pro",
    "workflow": [
      "08:30 · Café e Kit Plan Financiero — abre o dashboard consolidado dos 7 locais do grupo e deteta que o local 4 tem food cost de 33 % (+3 pp face ao objetivo).",
      "09:30 · Gerente Restaurante Pro — pede ao agente uma análise automatizada da causa por local. Identifica problema em mermas de peixe.",
      "10:30 · Videochamada com a gerente do local 4 apoiada em dados reais do Kit Plan Financiero, não em intuição.",
      "12:00 · Chef Executivo Pro — atualiza o procedimento de manipulação de peixe e é replicado às 7 cozinhas como nova versão do manual.",
      "15:30 · Escalas consolidadas — revê o Kit Gestión de Personal com rácios de produtividade de todos os locais e assina o onboarding da nova gerente do local 8.",
      "17:00 · Sonar Deep Research — investiga o mercado para a próxima abertura noutra cidade: análise de zonas, ticket médio e concorrência.",
      "19:00 · Reunião com o comité — exporta KPIs do trimestre em PDF diretamente do Kit Plan Financiero. Reunião fechada em 45 minutos.",
      "21:30 · Encerramento — os 7 gerentes enviam-lhe o relatório automático do dia por WhatsApp. Vai para casa com visão completa do grupo."
    ],
    "productsTitle": "Modelos e Kits Descarregáveis para Grupos de Restauração",
    "productIds": [
      "kit-plan-financiero",
      "kit-escandallos",
      "pack-appcc",
      "kit-gestion-personal",
      "kit-inventario",
      "kit-tareas"
    ],
    "testimonialQuote": "Gerimos 7 locais e antes cada um funcionava de forma diferente: Excel diferentes, manuais diferentes, APPCC diferentes. Com AI Chef Pro temos o mesmo padrão em todos e relatórios consolidados numa única vista. Detetar o local com problemas passou de demorar 2 semanas para demorar 1 dia.",
    "testimonialAuthor": "Javier Ortega",
    "testimonialRole": "Diretor de Operações, grupo de restauração com 7 locais",
    "faqTitle": "Perguntas Frequentes de Diretores de Operações",
    "faqs": [
      {
        "q": "Quantos locais suporta a AI Chef Pro?",
        "a": "Sem limite real. Há clientes com 1 local e outros com mais de 25 unidades ativas. Os planos empresa escalam por utilizações e desbloqueiam dashboards consolidados, onboarding personalizado e suporte prioritário."
      },
      {
        "q": "Integra-se com o nosso ERP ou sistema contabilístico?",
        "a": "Os modelos exportam para Excel, PDF e CSV em formatos compatíveis com a maioria dos ERPs e sistemas contabilísticos. A sua equipa financeira recebe documentação pronta a integrar."
      },
      {
        "q": "Permite perfis e permissões por local?",
        "a": "Sim. Pode dar acesso por gerente local, por diretor regional ou de forma consolidada ao diretor de operações. Cada nível vê apenas os dados que lhe correspondem."
      },
      {
        "q": "Como se garante o mesmo padrão em todas as unidades?",
        "a": "Chef Executivo Pro padroniza receitas e fichas técnicas; o Pack APPCC unifica a rastreabilidade; o Kit de Escandallos Pro mantém os mesmos cálculos em todos os locais. Os manuais são replicados com um clique e atualizados a partir de um único ponto."
      },
      {
        "q": "Há descontos para grupos com vários locais?",
        "a": "Sim. A partir de 5 unidades ativas há planos empresa com onboarding personalizado, dashboards consolidados, formação da equipa central e suporte prioritário."
      },
      {
        "q": "Serve para abrir novas localizações mais rapidamente?",
        "a": "Sim. É um dos casos de uso mais recorrentes: as guias Cómo Montar… (dark kitchen, restaurante gastronómico, casual, mexicano, japonês, peruano, nikkei) são roadmaps profissionais que aceleram as aberturas com plano financeiro, business plan e manuais replicáveis."
      }
    ],
    "ctaTitle": "Padronize o seu grupo. Mesmo padrão em todos os locais.",
    "ctaSubtitle": "Fale connosco para um onboarding personalizado para o seu grupo ou comece com o plano Membro: 10 € por mês com 10.000 créditos.",
    "seo": {
      "title": "IA para Diretores de Operações de Grupos de Restauração | AI Chef Pro",
      "description": "Suíte de IA para grupos de restauração multi-local: dashboards consolidados, padronização de receitas, APPCC corporativo, manuais replicáveis e plano financeiro por unidade.",
      "keywords": "IA grupo restauração, software multi-local restaurantes, diretor operações restaurantes IA, padronizar processos restaurante, dashboards consolidados restaurante, escalar grupo restauração, multi-local IA restauração",
      "ogImage": "https://aichef.pro/og/use-cases/director-operaciones-grupo.jpg"
    },
    "personalizationTitle": "Personalizado para o Seu Grupo desde o Minuto Um",
    "personalizationBody": "AI Chef Pro arranca com o agente «Quem Sou Eu?», um onboarding conversacional de 2 minutos em que lhe conta quantos locais gere, que conceitos opera (casual, gastronómico, dark kitchen, hotel), em que países e como trabalha a sua organização. A partir desse momento, cada agente —desde o Plan Financiero até aos manuais operativos— responde adaptado à escala e estrutura real do grupo. Não é um formulário: é uma conversa curta que torna a suíte verdadeiramente útil para diretores de operações multi-local.",
    "appsTitle": "Os Agentes IA que Vai Usar como Diretor de Operações",
    "apps": [
      {
        "name": "Chef Executivo Pro",
        "category": "Gastro Profile Pro",
        "description": "Padronização de receitas, fichas técnicas e manuais replicáveis a todas as unidades do grupo."
      },
      {
        "name": "Gerente Restaurante Pro",
        "category": "Gastro Profile Pro",
        "description": "Assistente para cada gerente local com relatórios consolidados para a direção."
      },
      {
        "name": "Restaurantes Casuais AI+",
        "category": "Conceitos de Negócio",
        "description": "Especialista em bistrôs, gastrobares e casual: o espectro mais comum em grupos multi-local."
      },
      {
        "name": "Burger Pro AI+",
        "category": "Conceitos de Negócio",
        "description": "Para grupos com marcas de hamburgueria gourmet ou fast casual."
      },
      {
        "name": "Catering AI+",
        "category": "Conceitos de Negócio",
        "description": "Para grupos com divisão de catering e eventos corporativos."
      },
      {
        "name": "Sonar Deep Research",
        "category": "Modelos IA + LLM",
        "description": "Pesquisa aprofundada de tendências, concorrentes e mercados para decisões estratégicas."
      },
      {
        "name": "Mermas Genéricas",
        "category": "Ferramentas e Utilitários",
        "description": "Dados precisos de mermas e rendimentos por ingrediente, essenciais para auditoria multi-local."
      },
      {
        "name": "ID Alergénios",
        "category": "Ferramentas e Utilitários",
        "description": "Identificação automática de alergénios por receita, unificada em todas as unidades."
      },
      {
        "name": "BlogPost SEO Gen+",
        "category": "Conteúdos e Redes Sociais",
        "description": "Posts de blog para captar tráfego orgânico para cada unidade do grupo."
      },
      {
        "name": "Keyword Discovery AI+",
        "category": "Conteúdos e Redes Sociais",
        "description": "Pesquisa de palavras-chave por zona postal de cada local."
      },
      {
        "name": "GastroIMG Gen+",
        "category": "Gastro Conhecimento",
        "description": "Fotografia gastronómica com IA unificada para toda a marca do grupo."
      }
    ],
    "metrics": [
      {
        "value": "−14 d",
        "label": "detetar local com desvios"
      },
      {
        "value": "×7",
        "label": "velocidade do reporting consolidado"
      },
      {
        "value": "+3 pp",
        "label": "margem após padronização"
      },
      {
        "value": "11+",
        "label": "agentes para multi-local"
      }
    ],
    "beforeAfter": {
      "beforeTitle": "Sem AI Chef Pro",
      "beforeItems": [
        "7 locais com 7 Excel diferentes, manuais heterogéneos e APPCC inconsistente",
        "Detetar um local com desvios demora 2 semanas porque não há relatórios consolidados",
        "Onboarding de novo gerente em 1 mês com materiais improvisados de cada unidade",
        "Relatórios para o comité com ficheiros dispersos e sem dashboards profissionais",
        "Decisões de expansão por intuição, sem análise de mercado aprofundada"
      ],
      "afterTitle": "Com AI Chef Pro",
      "afterItems": [
        "Mesmo padrão replicado nas 7 unidades: receitas, manuais e APPCC unificados",
        "Detetar local com desvios em 1 dia com dashboard consolidado do Kit Plan Financiero",
        "Onboarding de novo gerente em 1 semana com manuais e formação replicáveis",
        "Relatórios para o comité em PDF direto do Kit Plan Financiero com KPIs consolidados",
        "Decisões de expansão apoiadas em Sonar Deep Research e nas guias Cómo Montar… profissionais"
      ]
    },
    "galleryTitle": "O Dia a Dia de um Diretor de Operações, em Imagens",
    "gallerySubtitle": "O que vai coordenar com AI Chef Pro: dashboards multi-local, reuniões de estratégia, auditorias às unidades, manuais corporativos e onboarding de gerentes.",
    "galleryImages": [
      "/lovable-uploads/ai-gallery/use-case-director-operaciones-hero.jpg",
      "/lovable-uploads/ai-gallery/use-case-director-operaciones-multilocal.jpg",
      "/lovable-uploads/ai-gallery/use-case-director-operaciones-meeting.jpg",
      "/lovable-uploads/ai-gallery/use-case-director-operaciones-audit.jpg",
      "/lovable-uploads/ai-gallery/use-case-director-operaciones-strategy.jpg",
      "/lovable-uploads/ai-gallery/use-case-director-operaciones-handover.jpg"
    ]
  },
  "chef-ejecutivo": {
    "h1": "IA para Chef Executivo e Chef Corporativo",
    "heroSubtitle": "Crie receitas padronizadas, escandallos precisos e manuais replicáveis para 1, 5 ou 25 cozinhas. Uma suite de agentes de IA gastronómica desenhados para um dos papéis mais exigentes da cozinha profissional.",
    "heroTagline": "A sua equipa criativa e operativa, escalada à velocidade de uma conversa",
    "badge": "Para chefs executivos e corporativos",
    "painsTitle": "O Que um Chef Executivo Não Pode Deixar de Resolver",
    "pains": [
      "Padronizar receitas em cozinhas dispersas geograficamente sem que cada local as interprete à sua maneira",
      "Fechar escandallos precisos para cada ficha técnica com produto da época cujo preço muda todas as semanas",
      "Renovar a carta a cada 6-12 semanas sem que a equipa se afogue em papelada",
      "Manter manuais de cozinha e onboarding atualizados quando há rotação constante de pessoal",
      "Inovar no menu sazonal sem perder o food cost objetivo nem a margem real",
      "Reportar à direção com KPIs claros: rentabilidade por prato, produtividade da brigada e mermas"
    ],
    "featuresTitle": "Como o AI Chef Pro Ajuda um Chef Executivo",
    "features": [
      {
        "icon": "ChefHat",
        "title": "Chef Executivo Pro",
        "description": "Agente de IA especializado no papel: padronização multi-local, fichas técnicas, manuais de cozinha e decisões de carta baseadas em dados reais."
      },
      {
        "icon": "Sparkles",
        "title": "Culinária Criativa + Food Pairing AI",
        "description": "Chuva de ideias de pratos por época, ingrediente ou técnica, com combinações apoiadas em base científica. A Culinária Criativa entrega ainda a receita detalhada e um escandallo inicial com preços de referência de mercado, descarregável em CSV."
      },
      {
        "icon": "Calculator",
        "title": "Escandallos profissionais",
        "description": "Carrega o CSV de Culinária Criativa no Kit de Escandallos Pro e substitui os preços de referência pelos dos seus fornecedores reais. Custo por porção, food cost %, margem e preço sugerido instantaneamente. Recalcula automaticamente quando muda uma gramagem ou um custo."
      },
      {
        "icon": "BookOpen",
        "title": "Fichas técnicas profissionais",
        "description": "Receita, procedimento, alergénios, empratamento e storytelling num único documento. Pronto para enviar a todas as cozinhas do grupo."
      },
      {
        "icon": "Layers",
        "title": "Padronização multi-local",
        "description": "Mesmo prato, mesma qualidade e mesmo custo em 1, 5 ou 25 unidades. Manuais replicáveis e totalmente rastreáveis."
      },
      {
        "icon": "Beaker",
        "title": "Fermentus Con AI+ e técnicas avançadas",
        "description": "Koji, kombuchas, shoyus, garums e lactofermentos: I&D gastronómico com respaldo profissional."
      },
      {
        "icon": "ShieldCheck",
        "title": "ID Alergénios e Mermas Genéricas",
        "description": "Deteção automática de alergénios por prato e dados precisos de mermas e rendimentos por ingrediente."
      },
      {
        "icon": "Search",
        "title": "Sonar Deep Research",
        "description": "Investigação gastronómica profunda: tendências, técnicas emergentes, produtores e produtos da época."
      },
      {
        "icon": "Image",
        "title": "GastroIMG Gen+",
        "description": "Fotografia gastronómica gerada com IA para fichas técnicas, comunicação interna e notas de imprensa."
      }
    ],
    "workflowTitle": "Um Dia Real de um Chef Executivo com AI Chef Pro",
    "workflow": [
      "Manhã, 09:00 · Culinária Criativa — chuva de ideias de 12 pratos para o menu de outono a partir de produto da época local. O agente entrega-lhe receita detalhada e um escandallo inicial com preços de referência de mercado, descarregável em CSV.",
      "Manhã, 10:30 · Kit de Escandallos Pro — carrega os 12 CSV de Culinária Criativa, substitui os preços de referência pelos dos seus fornecedores reais e descarta 4 pratos que não encaixam no seu food cost objetivo (28 %).",
      "Meio-dia, 12:00 · Food Pairing AI — trabalha o maridagem dos 8 finalistas e valida harmonias inesperadas.",
      "Tarde, 15:00 · ID Alergénios — gera a ficha de alergénios por prato, pronta para regulamentação e para a sala.",
      "Tarde, 16:30 · Chef Executivo Pro — redige a ficha técnica completa com procedimento, gramagens, empratamento e storytelling.",
      "Tarde, 18:00 · GastroIMG Gen+ — gera as fotos de cada prato para o manual interno e a nota de imprensa.",
      "Tarde, 18:30 · Replica o manual às 5 cozinhas do grupo. O que um processo tradicional fecha em 15-30 dias, você fecha em 1-3 jornadas consoante o tamanho da carta."
    ],
    "productsTitle": "Modelos e Kits Descarregáveis para Chefs Executivos",
    "productIds": [
      "kit-escandallos",
      "pack-appcc",
      "pro-prompts-ebook",
      "kit-plan-financiero",
      "kit-inventario",
      "kit-gestion-personal"
    ],
    "testimonialQuote": "Antes demorava entre 15 e 20 dias a fechar uma carta nova entre chuva de ideias, testes, escandallos, fichas técnicas e comunicação interna. Com AI Chef Pro faço-o em 2 ou 3 dias, consoante o tamanho da carta e se é reengenharia completa ou parcial. A diferença não é só de tempo: a equipa recebe documentação profissional e replicável, não apontamentos manuscritos.",
    "testimonialAuthor": "Diego Saavedra",
    "testimonialRole": "Chef Executivo, grupo de 5 restaurantes mediterrânicos",
    "faqTitle": "Perguntas Frequentes de Chefs Executivos",
    "faqs": [
      {
        "q": "Os agentes de IA do AI Chef Pro entendem cozinha profissional ou são chatbots generalistas?",
        "a": "São agentes especializados. Culinária Criativa, Food Pairing AI, Fermentus Con AI+ e Chef Executivo Pro estão treinados com conhecimento gastronómico profissional: técnicas, escandallo real, rentabilidade, gramagens e cortes. Não são ChatGPT genérico: são ferramentas desenhadas para alguém que já sabe cozinhar."
      },
      {
        "q": "Posso carregar o meu receituário existente?",
        "a": "Sim. O Kit de Escandallos Pro permite carregar o seu receituário e aplicar escandallo automatizado em minutos. Também pode pedir ao agente Chef Executivo Pro que gere fichas técnicas a partir de descrições livres."
      },
      {
        "q": "Serve para cozinha gastronómica avançada ou apenas para cozinha casual?",
        "a": "Para todo o espetro. Há agentes específicos: Culinária Criativa para cozinha de autor, Pastelaria Criativa, Fermentus para vanguarda, VegChef para plant-based, além de mais de 25 receituários por país. Casos reais em Michelin e Repsol Soles e em grupos casuais de até 25 unidades."
      },
      {
        "q": "Como é que o sistema se adapta à minha forma de trabalhar?",
        "a": "Começa com o agente «Quem Sou Eu?», um onboarding conversacional de 2 minutos no qual lhe conta quem é, onde trabalha, o seu tipo de cozinha e a que escala. A partir desse momento, todos os agentes adaptam-se ao seu contexto: preços locais, regulamentação do seu país, cozinha do território e escala da sua operação."
      },
      {
        "q": "Há algo específico para grupos multi-local e cadeias de restauração?",
        "a": "Sim. O agente Chef Executivo Pro está pensado para a padronização: mesma ficha técnica, mesmo escandallo e mesmos manuais replicados em todas as unidades. Combinado com o Kit Plan Financiero, pode consolidar o reporting de KPIs por unidade e por grupo."
      },
      {
        "q": "Há uma biblioteca de prompts específicos para chefs?",
        "a": "Sim. O Pro Prompts eBook inclui mais de 300 prompts testados para criatividade, escandallo, fichas técnicas, formação, comunicação interna e operativa de cozinha, organizados por situação de utilização."
      },
      {
        "q": "Quanto tempo demora a pagar-se a subscrição?",
        "a": "A maioria dos chefs executivos reporta retorno na primeira carta nova. Uma mudança de menu tradicional ocupa entre 15 e 30 dias entre chuva de ideias, testes, escandallos, fichas técnicas e comunicação interna. Com AI Chef Pro e um bom fluxo em Excel ou Google Workspace, esse mesmo processo passa a entre 1 e 3 dias consoante o tamanho da carta e se é reengenharia total ou parcial. Com 4-6 mudanças de carta por ano, recupera entre 60 e 120 jornadas de trabalho."
      }
    ],
    "ctaTitle": "Crie, escandalle e replique receitas à velocidade de uma conversa.",
    "ctaSubtitle": "Comece com o onboarding de 2 minutos. Plano Membro por 10 € por mês com 10.000 créditos para usar todos os agentes.",
    "seo": {
      "title": "IA para Chef Executivo: Receitas, Escandallos e Manuais | AI Chef Pro",
      "description": "Suite de IA para chef executivo e corporativo: agente Chef Executivo Pro, escandallos automáticos, fichas técnicas e manuais replicáveis multi-local. Comece hoje.",
      "keywords": "IA chef executivo, chef executivo IA, software chef corporativo, agente IA gastronómico, escandallos automáticos, fichas técnicas restaurante, receitas padronizadas multi-local, manuais de cozinha IA, food pairing IA, IA para grupos de restauração, chef executivo Espanha",
      "ogImage": "https://aichef.pro/og/use-cases/chef-ejecutivo.jpg"
    },
    "personalizationTitle": "Personalizado para Si desde o Primeiro Minuto",
    "personalizationBody": "O AI Chef Pro arranca com um onboarding conversacional de 2 minutos —o agente «Quem Sou Eu?»— no qual lhe conta quem é, onde trabalha, que tipo de cozinha lidera e a que escala opera. A partir desse momento, cada agente —desde os escandallos até à criatividade— responde adaptado ao seu contexto: a sua cozinha local, a sua regulamentação, os seus preços de mercado e o tamanho da sua brigada. Não é um formulário: é uma conversa curta que dá sentido a tudo o que vem a seguir.",
    "appsTitle": "Os Agentes de IA que Vai Usar como Chef Executivo",
    "apps": [
      {
        "name": "Chef Executivo Pro",
        "category": "Gastro Profile Pro",
        "description": "Agente principal: padronização multi-local, fichas técnicas e decisões de carta."
      },
      {
        "name": "Culinária Criativa",
        "category": "Criatividade Culinária",
        "description": "Desenvolvimento de pratos profissionais com receita detalhada e escandallo inicial descarregável em CSV (preços de referência de mercado), pronto para carregar no Kit de Escandallos Pro."
      },
      {
        "name": "Food Pairing AI",
        "category": "Criatividade Culinária",
        "description": "Combinações de ingredientes e maridagens com base científica."
      },
      {
        "name": "Fermentus Con AI+",
        "category": "Criatividade Culinária",
        "description": "Fermentação criativa: koji, kombucha, shoyu, miso, garum e lactofermentos."
      },
      {
        "name": "Mermas Genéricas",
        "category": "Ferramentas e Utilitários",
        "description": "Dados precisos de mermas e rendimentos por ingrediente. Essencial para escandallo realista."
      },
      {
        "name": "Calcula Pax",
        "category": "Ferramentas e Utilitários",
        "description": "Calculadora de porções que escala receitas para qualquer número de comensais."
      },
      {
        "name": "ID Alergénios",
        "category": "Ferramentas e Utilitários",
        "description": "Identificação automática de alergénios potenciais por receita e por prato."
      },
      {
        "name": "Pastelaria Criativa",
        "category": "Criatividade Culinária",
        "description": "Sobremesas de restaurante criativas com técnica de pastelaria profissional."
      },
      {
        "name": "Sosa Ingredients",
        "category": "Fornecedores Gastro",
        "description": "Assistente de seleção e técnica com o catálogo profissional da Sosa."
      },
      {
        "name": "tSpoonLab Agent",
        "category": "Fornecedores Gastro",
        "description": "Assistente do catálogo tSpoonLab para técnicas e aplicações avançadas."
      },
      {
        "name": "Sonar Deep Research",
        "category": "Modelos IA + LLM",
        "description": "Investigação profunda: tendências, produtores e técnicas emergentes."
      },
      {
        "name": "GastroIMG Gen+",
        "category": "Gastro Conhecimento",
        "description": "Fotografia gastronómica gerada com IA para fichas técnicas e imprensa."
      },
      {
        "name": "Léxico Gastronómico",
        "category": "Gastro Conhecimento",
        "description": "Tutor com definições de técnicas, processos, aditivos e ciência gastronómica."
      }
    ],
    "metrics": [
      {
        "value": "−90 %",
        "label": "tempo a fechar carta nova"
      },
      {
        "value": "×10",
        "label": "velocidade de fichas técnicas"
      },
      {
        "value": "+4 pp",
        "label": "margem por melhor escandallo"
      },
      {
        "value": "13+",
        "label": "agentes de IA para o seu papel"
      }
    ],
    "beforeAfter": {
      "beforeTitle": "Sem AI Chef Pro",
      "beforeItems": [
        "Fecho de uma carta nova: entre 15 e 30 dias, dependendo da padronização do processo",
        "Receituário em folhas soltas, documentos Word desordenados e notas manuscritas",
        "Cada local interpreta a receita à sua maneira e o resultado varia",
        "Escandallo manual com calculadora: muda uma gramagem e reescreve tudo",
        "Manuais e onboarding desatualizados constantemente"
      ],
      "afterTitle": "Com AI Chef Pro",
      "afterItems": [
        "Fecho de uma carta nova: entre 1 e 3 dias consoante o tamanho e se é reengenharia total ou parcial",
        "Receituário centralizado com escandallo, alergénios, técnica e storytelling",
        "Mesmo prato, mesma qualidade e mesmo custo em 1, 5 ou 25 cozinhas",
        "Escandallo profissional que recalcula instantaneamente com qualquer mudança",
        "Manuais atualizados com um clique e onboarding pronto para novos chefs"
      ]
    },
    "appUrlPath": "/agents/chef-ejecutivo-pro",
    "galleryTitle": "O Dia a Dia de um Chef Executivo, em Imagens",
    "gallerySubtitle": "O que vai poder gerir com AI Chef Pro: brigada, fichas técnicas, criatividade, escandallos e comunicação interna.",
    "galleryImages": [
      "/lovable-uploads/ai-gallery/use-case-chef-ejecutivo-hero.jpg",
      "/lovable-uploads/ai-gallery/use-case-chef-ejecutivo-recipes.jpg",
      "/lovable-uploads/ai-gallery/use-case-chef-ejecutivo-brigade.jpg",
      "/lovable-uploads/ai-gallery/use-case-chef-ejecutivo-creativity.jpg",
      "/lovable-uploads/ai-gallery/use-case-chef-ejecutivo-tasting.jpg",
      "/lovable-uploads/ai-gallery/use-case-chef-ejecutivo-meeting.jpg"
    ]
  },
  "chef-cocina": {
    "h1": "IA para Chef de Cozinha e Chefe de Cozinha",
    "heroSubtitle": "Gira cozinhas, fichas técnicas, mise en place e formação da equipa com uma suite de agentes de IA pensados para o dia a dia do chefe de cozinha profissional.",
    "heroTagline": "Mais cozinha, menos papelada",
    "badge": "Para chefs de cozinha e chefes de cozinha",
    "painsTitle": "O Que um Chefe de Cozinha Não Pode Deixar de Resolver",
    "pains": [
      "Calcular o food cost preciso de cada prato e da ementa completa com produto que muda de preço todas as semanas",
      "Coordenar mise en place e cozinhas sem falhas nos picos de serviço",
      "Manter o APPCC em dia sem que a papelada roube tempo à cozinha",
      "Formar e supervisionar a equipa em técnicas e procedimentos padronizados com rotação frequente",
      "Renovar a ementa a cada estação mantendo margem e respeitando o produto local",
      "Comunicar com a sala, a direção e os fornecedores com documentação profissional, não com apontamentos num caderno"
    ],
    "featuresTitle": "Como a AI Chef Pro Ajuda um Chefe de Cozinha",
    "features": [
      {
        "icon": "ChefHat",
        "title": "Chef Executivo Pro",
        "description": "Agente especializado para o apoiar na padronização de receitas, fichas técnicas e manuais de cozinha."
      },
      {
        "icon": "Sparkles",
        "title": "Culinária Criativa + Food Pairing AI",
        "description": "Brainstorming para novos pratos com base profissional. A Culinária Criativa entrega receita + ficha técnica CSV com preços de referência, pronta para o Kit de Escandallos Pro."
      },
      {
        "icon": "Calculator",
        "title": "Fichas técnicas profissionais",
        "description": "Kit de Escandallos Pro: carrega o CSV da Culinária Criativa, substitui os preços pelos reais e obtém custo, food cost % e margem instantaneamente."
      },
      {
        "icon": "BookOpen",
        "title": "Fichas técnicas profissionais",
        "description": "Receita, procedimento, alergénios, empratamento e storytelling num único documento pronto a imprimir."
      },
      {
        "icon": "CheckSquare",
        "title": "Tarefas e mise en place",
        "description": "Kit de Tareas com modelos específicos por conceito: abertura, encerramento, cozinhas e serviço."
      },
      {
        "icon": "ShieldCheck",
        "title": "APPCC e rastreabilidade",
        "description": "Pack APPCC com 19 registos: temperaturas, quebras, alergénios e rastreabilidade a partir do telemóvel da equipa."
      },
      {
        "icon": "Beaker",
        "title": "Fermentus Con AI+",
        "description": "I&D gastronómico: koji, kombuchas, shoyus, garums e lactofermentações com suporte profissional."
      },
      {
        "icon": "GraduationCap",
        "title": "Pro Prompts eBook",
        "description": "Mais de 300 prompts testados para criatividade, fichas técnicas, formação e operação de cozinha."
      },
      {
        "icon": "ShieldCheck",
        "title": "ID Alergénios e Mermas Genéricas",
        "description": "Deteção automática de alergénios por prato e dados precisos de quebras e rendimentos por ingrediente."
      }
    ],
    "workflowTitle": "Um Dia Real de um Chefe de Cozinha com a AI Chef Pro",
    "workflow": [
      "08:00 · Abertura — imprime a mise en place do dia a partir do Kit de Tareas e valida encomendas a fornecedores com o Kit Inventario.",
      "09:00 · Culinária Criativa — desenvolve um prato fora da ementa para o fim de semana com produto que chegou a bom preço. Recebe receita + ficha técnica CSV.",
      "10:30 · Kit de Escandallos Pro — carrega o CSV, aplica os seus preços reais e valida que o food cost fecha nos 28 %.",
      "12:30 · Serviço — a equipa regista quebras e temperaturas a partir do telemóvel com o Pack APPCC. Você está na cozinha, não no escritório.",
      "15:30 · Briefing curto com a brigada para rever o prato do dia e ajustar a mise.",
      "17:00 · Pro Prompts eBook — pede ao agente para gerar o guião da formação de um novo cozinheiro que entra amanhã.",
      "19:30 · Serviço noturno — coordena os serviços com a equipa apoiado nas fichas técnicas centralizadas.",
      "23:30 · Encerramento — assina o APPCC do dia, gera o relatório e este vai para o WhatsApp do proprietário em 10 minutos."
    ],
    "productsTitle": "Modelos e Kits Descarregáveis para Chefes de Cozinha",
    "productIds": [
      "kit-escandallos",
      "pack-appcc",
      "kit-tareas",
      "pro-prompts-ebook",
      "kit-inventario",
      "kit-gestion-personal"
    ],
    "testimonialQuote": "O Kit de Escandallos Pro e o Pack APPCC tiraram-me 5 horas de papelada por semana. Mas o que mais uso é a Culinária Criativa para pratos fora da ementa do fim de semana: numa manhã fecho receita, ficha técnica e custos. Antes era uma semana inteira.",
    "testimonialAuthor": "Lucía Romero",
    "testimonialRole": "Chefe de Cozinha, restaurante mediterrânico de 70 lugares",
    "faqTitle": "Perguntas Frequentes de Chefes de Cozinha",
    "faqs": [
      {
        "q": "Tenho de ser especialista em Excel?",
        "a": "Não. Os modelos do Kit de Escandallos Pro e do Pack APPCC têm fórmulas pré-carregadas, só tem de introduzir dados. Há um vídeo tutorial de 5 minutos para começar."
      },
      {
        "q": "Funciona se a nossa ementa mudar todos os meses ou em cada estação?",
        "a": "É o caso ideal. A Culinária Criativa gera pratos novos com ficha técnica em CSV, carrega-a no Kit de Escandallos Pro com os seus preços e exporta as fichas técnicas. O que era uma semana de trabalho passa a ser um dia."
      },
      {
        "q": "A IA entende termos profissionais de cozinha?",
        "a": "Sim. A Culinária Criativa, o Food Pairing AI, a Fermentus Con AI+ e os livros de receitas por país (italiana, mexicana, japonesa, peruana, etc.) são treinados com conhecimento gastronómico profissional: técnicas, fichas técnicas, gramagens, cortes, empratamento e storytelling. Não é um ChatGPT genérico."
      },
      {
        "q": "Como é que se adapta à minha cozinha específica?",
        "a": "Começa com o agente «Quem Sou Eu?», um onboarding conversacional de 2 minutos onde nos conta que tipo de cozinha lidera, onde trabalha e a que escala. A partir desse momento, todos os agentes respondem adaptados ao seu contexto real."
      },
      {
        "q": "Posso descarregar tudo em Excel e PDF?",
        "a": "Sim. Toda a documentação é exportável e editável: fichas técnicas, APPCC, mise en place e formação da equipa."
      },
      {
        "q": "Serve para cozinhas com técnicas avançadas (fermentos, esferificações, cozeduras longas)?",
        "a": "Sim. A Fermentus Con AI+ cobre fermentação de vanguarda (koji, kombucha, shoyu, miso, garum, lactofermentações) e a Culinária Criativa entende técnicas como sous vide, esferificações, gelificações e cozeduras longas controladas."
      }
    ],
    "ctaTitle": "Mais cozinha, menos papelada. Recupere horas para o que importa.",
    "ctaSubtitle": "Comece com o onboarding de 2 minutos. Plano Membro por 10 € por mês com 10.000 créditos para usar todos os agentes.",
    "seo": {
      "title": "IA para Chef de Cozinha e Chefe de Cozinha: Fichas Técnicas e APPCC | AI Chef Pro",
      "description": "Suite de IA para chefes de cozinha profissional: agentes especializados, fichas técnicas, mise en place e APPCC com suporte gastronómico real. Comece hoje.",
      "keywords": "IA chef cozinha, chefe de cozinha software, IA chefe de cozinha, fichas técnicas cozinha, APPCC cozinha, mise en place IA, agente IA gastronómico, chefe cozinha Portugal",
      "ogImage": "https://aichef.pro/og/use-cases/chef-cocina.jpg"
    },
    "personalizationTitle": "Personalizado à Sua Cozinha desde o Primeiro Minuto",
    "personalizationBody": "A AI Chef Pro arranca com o agente «Quem Sou Eu?», um onboarding conversacional de 2 minutos em que nos conta que tipo de cozinha lidera, em que cidade, que tipo de ementa gere e a que escala opera. A partir desse momento, cada agente — desde as fichas técnicas até à criatividade — responde adaptado ao seu contexto: produto local, legislação do seu país, dimensão da sua brigada e orçamento real. Não é um formulário: é uma conversa curta que torna a suite verdadeiramente útil para o seu dia a dia na cozinha.",
    "appsTitle": "Os Agentes de IA que Vai Usar como Chefe de Cozinha",
    "apps": [
      {
        "name": "Chef Executivo Pro",
        "category": "Gastro Profile Pro",
        "description": "Padronização de receitas, fichas técnicas e manuais de cozinha."
      },
      {
        "name": "Culinária Criativa",
        "category": "Criatividade Culinária",
        "description": "Desenvolvimento de pratos profissionais com receita + ficha técnica CSV pronta para o Kit de Escandallos Pro."
      },
      {
        "name": "Food Pairing AI",
        "category": "Criatividade Culinária",
        "description": "Combinações de ingredientes e harmonizações com base científica."
      },
      {
        "name": "Fermentus Con AI+",
        "category": "Criatividade Culinária",
        "description": "I&D gastronómico: fermentação criativa de koji, kombucha, shoyu, miso e garum."
      },
      {
        "name": "Pastelaria Criativa",
        "category": "Criatividade Culinária",
        "description": "Sobremesas de restaurante criativas com técnica de pastelaria profissional."
      },
      {
        "name": "Mermas Genéricas",
        "category": "Ferramentas e Utilitários",
        "description": "Dados precisos de quebras e rendimentos por ingrediente."
      },
      {
        "name": "Calcula Pax",
        "category": "Ferramentas e Utilitários",
        "description": "Calculadora de porções que adapta receitas a qualquer número de comensais."
      },
      {
        "name": "Conversor Ing",
        "category": "Ferramentas e Utilitários",
        "description": "Conversor de pesos e medidas para cozinha profissional."
      },
      {
        "name": "ID Alergénios",
        "category": "Ferramentas e Utilitários",
        "description": "Identificação automática de alergénios por receita e prato."
      },
      {
        "name": "Refeição do Pessoal",
        "category": "Gastro Profile Pro",
        "description": "Gerador de menus de staff que poupa custos e motiva a equipa."
      },
      {
        "name": "Sosa Ingredients",
        "category": "Fornecedores Gastro",
        "description": "Assistente com o catálogo profissional da Sosa para técnicas avançadas."
      },
      {
        "name": "tSpoonLab Agent",
        "category": "Fornecedores Gastro",
        "description": "Assistente do catálogo tSpoonLab para aplicações técnicas."
      },
      {
        "name": "Léxico Gastronómico",
        "category": "Gastro Conhecimento",
        "description": "Tutor com definições de técnicas, processos e ciência gastronómica."
      }
    ],
    "metrics": [
      {
        "value": "−5 h",
        "label": "semanais em papelada"
      },
      {
        "value": "×7",
        "label": "velocidade de fecho de nova ementa"
      },
      {
        "value": "+3 pp",
        "label": "margem após ficha técnica real"
      },
      {
        "value": "13+",
        "label": "agentes de IA para a sua cozinha"
      }
    ],
    "beforeAfter": {
      "beforeTitle": "Sem AI Chef Pro",
      "beforeItems": [
        "Livro de receitas em caderno e folhas soltas, versões diferentes consoante o cozinheiro",
        "Ficha técnica manual com calculadora sempre que um preço muda",
        "APPCC em papel impresso que se acumula e ninguém revê",
        "Renovar a ementa demora entre 15 e 30 dias entre chuva de ideias, fichas técnicas e documentos",
        "Formação da equipa improvisada sempre que entra alguém novo"
      ],
      "afterTitle": "Com AI Chef Pro",
      "afterItems": [
        "Livro de receitas centralizado com ficha técnica, alergénios, técnica e storytelling",
        "Ficha técnica automática que recalcula instantaneamente com qualquer alteração de preço",
        "APPCC a partir do telemóvel com registos e alertas, pronto para inspeção",
        "Renove a ementa em 1-3 dias com Culinária Criativa + Kit de Escandallos Pro",
        "Manuais de formação replicáveis com o guião do Pro Prompts eBook"
      ]
    },
    "galleryTitle": "O Dia a Dia de um Chefe de Cozinha, em Imagens",
    "gallerySubtitle": "O que vai coordenar com a AI Chef Pro: brigada, mise en place, fichas técnicas, serviço, armazém e formação da equipa.",
    "galleryImages": [
      "/lovable-uploads/ai-gallery/use-case-chef-cocina-hero.jpg",
      "/lovable-uploads/ai-gallery/use-case-chef-cocina-recipes.jpg",
      "/lovable-uploads/ai-gallery/use-case-chef-cocina-team.jpg",
      "/lovable-uploads/ai-gallery/use-case-chef-cocina-mise.jpg",
      "/lovable-uploads/ai-gallery/use-case-chef-cocina-pass.jpg",
      "/lovable-uploads/ai-gallery/use-case-chef-cocina-storage.jpg"
    ]
  },
  "sous-chef": {
    "h1": "IA para Sous Chef",
    "heroSubtitle": "Organize partidas, gere o mise en place, supervisione a equipa e liberte horas administrativas com uma suite de agentes de IA pensados para o sous chef em cozinha profissional.",
    "heroTagline": "O braço direito do chefe de cozinha, com sistema",
    "badge": "Para sous chefs",
    "painsTitle": "O Que um Sous Chef Não Pode Deixar de Resolver",
    "pains": [
      "Coordenar partidas e mise en place com precisão quando o ritmo não espera",
      "Cobrir o chefe de cozinha quando não está sem que baixe a qualidade nem a operativa",
      "Formar e supervisionar a equipa de cozinha com critérios consistentes",
      "Manter a rastreabilidade APPCC em dia sem que se acumule a papelada",
      "Ter acesso rápido a fichas técnicas atualizadas durante o serviço",
      "Validar escandallos quando entram ingredientes novos ou muda um fornecedor"
    ],
    "featuresTitle": "Como o AI Chef Pro Ajuda um Sous Chef",
    "features": [
      {
        "icon": "CheckSquare",
        "title": "Mise en place e tarefas por partida",
        "description": "Kit de Tareas com listas estruturadas por turno e por partida, prontas para imprimir todas as manhãs."
      },
      {
        "icon": "BookOpen",
        "title": "Fichas técnicas sempre atualizadas",
        "description": "Acesso rápido a partir do telemóvel a receita, procedimento, empratamento e alergénios de cada prato durante o serviço."
      },
      {
        "icon": "ShieldCheck",
        "title": "APPCC a partir do telemóvel",
        "description": "Pack APPCC com registos, alertas de temperatura e exportação para PDF. A equipa regista a partir do telemóvel sem papelada."
      },
      {
        "icon": "Calculator",
        "title": "Escandallos rápidos",
        "description": "Culinária Criativa entrega receita + escandallo CSV; o Kit de Escandallos Pro gere-o com os seus preços reais e valida margem no instante."
      },
      {
        "icon": "GraduationCap",
        "title": "Formação da equipa",
        "description": "Pro Prompts eBook + Chef Executivo Pro geram manuais e onboarding prontos para novos cozinheiros."
      },
      {
        "icon": "Sparkles",
        "title": "Culinária Criativa",
        "description": "Chat de IA gastronómico para resolver dúvidas técnicas, propor pratos fora da carta e validar técnicas em tempo real."
      },
      {
        "icon": "Users",
        "title": "Refeição do Pessoal",
        "description": "Gerador de menus de staff que aproveita o produto que já tem na câmara e motiva a equipa."
      },
      {
        "icon": "ShieldCheck",
        "title": "ID Alergénios e Mermas Genéricas",
        "description": "Deteção automática de alergénios e dados precisos de mermas para passe e partida."
      }
    ],
    "workflowTitle": "Um Dia Real de um Sous Chef com AI Chef Pro",
    "workflow": [
      "07:30 · Abertura — abre o Kit de Tareas e revê o mise en place do dia. Assina o inventário crítico com o Kit Inventario.",
      "08:30 · Briefing breve com a brigada — repassa os passes do dia com fichas técnicas centralizadas em mãos.",
      "12:00 · Serviço de meio-dia — supervisiona partidas, a equipa regista mermas e temperaturas a partir do telemóvel com o Pack APPCC.",
      "15:30 · Culinária Criativa — o chefe de cozinha pede-lhe um prato fora da carta para o sábado. Gera prato + escandallo CSV em 20 minutos.",
      "16:00 · Kit de Escandallos Pro — carrega o CSV com os seus preços reais, valida que o food cost bate aos 28 % e exporta a ficha técnica.",
      "17:30 · Refeição do Pessoal — prepara o menu do staff da próxima semana respeitando o custo objetivo e o stock da câmara.",
      "20:00 · Serviço de noite — coordena passes com a brigada, gere as dúvidas com a Culinária Criativa quando o cozinheiro júnior precisa de confirmar técnica.",
      "23:30 · Encerramento — assina APPCC, deixa o mise en place do dia seguinte pronto e relatório enviado ao chefe de cozinha."
    ],
    "productsTitle": "Modelos e Kits Descarregáveis para Sous Chefs",
    "productIds": [
      "kit-tareas",
      "kit-escandallos",
      "pack-appcc",
      "pro-prompts-ebook",
      "kit-inventario",
      "kit-gestion-personal"
    ],
    "testimonialQuote": "Ser sous chef é estar em mil sítios ao mesmo tempo. As listas de mise en place do Kit de Tareas e os registos APPCC a partir do telemóvel organizaram-me o caos. Quando o chefe de cozinha não está, tudo continua a funcionar porque os procedimentos estão documentados.",
    "testimonialAuthor": "Nicolás Vega",
    "testimonialRole": "Sous Chef, restaurante de 100 lugares",
    "faqTitle": "Perguntas Frequentes de Sous Chefs",
    "faqs": [
      {
        "q": "Os modelos adaptam-se ao estilo da minha cozinha?",
        "a": "Sim. Existem Kits de Tareas específicos por conceito (casual, gastronómico, dark kitchen, hotel, pizzaria, hamburgueria, pastelaria, bar, catering, gelataria, chocolataria, restaurante criativo, chef privado) e todos podem ser personalizados ao estilo da sua cozinha."
      },
      {
        "q": "Funciona a partir do telemóvel para registos da equipa?",
        "a": "Sim. Os registos APPCC, mermas, temperaturas e check de tarefas são feitos a partir do telemóvel do staff sem instalar nada. No final do dia exporta-se para PDF para o chefe de cozinha ou o proprietário."
      },
      {
        "q": "É complicado de usar para a equipa?",
        "a": "Não. A equipa só preenche caixas ou marca check. A curva real é de 1 dia. Há vídeo de onboarding de 5 minutos."
      },
      {
        "q": "Serve se não for eu quem decide as ferramentas na cozinha?",
        "a": "Pode começar com o plano Membro (10 € por mês, 10.000 créditos) para as suas próprias listas e propostas. Quando tiver 1-2 semanas a usá-lo, proponha ao chefe de cozinha com dados concretos: tempo poupado, escandallos validados, mise organizado."
      },
      {
        "q": "Como me ajuda nos picos de serviço?",
        "a": "As fichas técnicas centralizadas dão-lhe acesso rápido a partir do telemóvel durante o passe. Se surgir uma dúvida técnica, a Culinária Criativa responde em segundos. O Coach Mental também ajuda a gerir o stress em cozinhas de alta pressão."
      },
      {
        "q": "Há algo específico para ascensão a chefe de cozinha?",
        "a": "Sim. Pro Prompts eBook (300+ prompts profissionais), Chef Executivo Pro (padronização multi-local) e Léxico Gastronómico (referência de técnica) são ferramentas-chave para crescer para o próximo nível."
      }
    ],
    "ctaTitle": "Organize a sua cozinha sem papéis soltos.",
    "ctaSubtitle": "Comece com o onboarding de 2 minutos. Plano Membro por 10 € por mês com 10.000 créditos para usar todos os agentes.",
    "seo": {
      "title": "IA para Sous Chef: Mise en Place, Fichas Técnicas e APPCC | AI Chef Pro",
      "description": "Suite de IA para sous chef em cozinha profissional: mise en place, fichas técnicas centralizadas, escandallos, APPCC a partir do telemóvel e formação da equipa. Comece hoje.",
      "keywords": "IA sous chef, software sous chef, mise en place cozinha IA, APPCC sous chef, fichas técnicas cozinha, formação brigada cozinha, sous chef Espanha",
      "ogImage": "https://aichef.pro/og/use-cases/sous-chef.jpg"
    },
    "personalizationTitle": "Personalizado à Sua Cozinha desde o Minuto Um",
    "personalizationBody": "AI Chef Pro arranca com o agente «Quem Sou Eu?», um onboarding conversacional de 2 minutos em que lhe conta que tipo de cozinha tem, em que cidade, que carta gere e a que escala. A partir desse momento, cada agente —desde o mise en place até aos escandallos— responde adaptado ao seu contexto: tipo de serviço, tamanho da brigada e operativa real. Não é um formulário: é uma conversa curta que torna a suite verdadeiramente útil para o ritmo de partida.",
    "appsTitle": "Os Agentes de IA que Vai Usar como Sous Chef",
    "apps": [
      {
        "name": "Chef Executivo Pro",
        "category": "Gastro Profile Pro",
        "description": "Padronização de receitas, fichas técnicas e manuais de cozinha centralizados."
      },
      {
        "name": "Culinária Criativa",
        "category": "Criatividade Culinária",
        "description": "Desenvolvimento de pratos profissionais com receita + escandallo CSV pronto para o Kit de Escandallos Pro."
      },
      {
        "name": "Food Pairing AI",
        "category": "Criatividade Culinária",
        "description": "Combinações de ingredientes e harmonizações com base científica."
      },
      {
        "name": "Pastelaria Criativa",
        "category": "Criatividade Culinária",
        "description": "Sobremesas de restaurante criativas com técnica de pastelaria profissional."
      },
      {
        "name": "Calcula Pax",
        "category": "Ferramentas e Utilitários",
        "description": "Calculadora de porções que escala receitas para qualquer número de comensais."
      },
      {
        "name": "Conversor Ing",
        "category": "Ferramentas e Utilitários",
        "description": "Conversor de pesos e medidas para cozinha profissional."
      },
      {
        "name": "Mermas Genéricas",
        "category": "Ferramentas e Utilitários",
        "description": "Dados precisos de mermas e rendimentos por ingrediente."
      },
      {
        "name": "ID Alergénios",
        "category": "Ferramentas e Utilitários",
        "description": "Identificação automática de alergénios por receita e prato."
      },
      {
        "name": "Refeição do Pessoal",
        "category": "Gastro Profile Pro",
        "description": "Gerador de menus de staff com produto que já tem na câmara."
      },
      {
        "name": "Coach Mental",
        "category": "Ferramentas e Utilitários",
        "description": "Coaching psicológico para gerir stress e conversas difíceis em cozinha."
      },
      {
        "name": "Léxico Gastronómico",
        "category": "Conhecimento Gastronómico",
        "description": "Tutor com definições de técnicas, processos e ciência gastronómica."
      }
    ],
    "metrics": [
      {
        "value": "×3",
        "label": "velocidade mise en place"
      },
      {
        "value": "−4 h",
        "label": "semanais em papelada"
      },
      {
        "value": "mesmo",
        "label": "padrão quando o chefe não está"
      },
      {
        "value": "11+",
        "label": "agentes para o seu papel"
      }
    ],
    "beforeAfter": {
      "beforeTitle": "Sem AI Chef Pro",
      "beforeItems": [
        "Mise en place ditada todas as manhãs à equipa, diferente todos os dias",
        "APPCC em papel impresso que se acumula no final da semana",
        "Fichas técnicas no caderno do chefe de cozinha, inacessíveis durante o serviço",
        "Quando o chefe de cozinha não está, a qualidade e a operativa baixam",
        "Formação de novos cozinheiros improvisada e inconsistente"
      ],
      "afterTitle": "Com AI Chef Pro",
      "afterItems": [
        "Mise en place imprimível todos os dias com o Kit de Tareas estruturado por partida",
        "APPCC a partir do telemóvel com registos, alertas e exportação para PDF no encerramento",
        "Fichas técnicas centralizadas acessíveis a partir do telemóvel durante o serviço",
        "Procedimentos documentados — o padrão mantém-se mesmo que a equipa mude",
        "Formação replicável com guião do Pro Prompts eBook e manuais do Chef Executivo Pro"
      ]
    },
    "galleryTitle": "O Dia a Dia de um Sous Chef, em Imagens",
    "gallerySubtitle": "O que vai coordenar com AI Chef Pro: mise en place, preparação, supervisão da equipa, serviço em linha e rastreabilidade.",
    "galleryImages": [
      "/lovable-uploads/ai-gallery/use-case-sous-chef-hero.jpg",
      "/lovable-uploads/ai-gallery/use-case-sous-chef-prep.jpg",
      "/lovable-uploads/ai-gallery/use-case-sous-chef-cooking.jpg",
      "/lovable-uploads/ai-gallery/use-case-sous-chef-supervise.jpg",
      "/lovable-uploads/ai-gallery/use-case-sous-chef-clipboard.jpg",
      "/lovable-uploads/ai-gallery/use-case-sous-chef-station.jpg"
    ]
  },
  "chef-catering": {
    "h1": "IA para Chef de Catering",
    "heroSubtitle": "Desenha menus de evento, escandala por serviço e planeia produção à escala com uma suite de agentes de IA pensados para catering profissional e chefs de eventos.",
    "heroTagline": "Produção à escala sem perder margem nem qualidade",
    "badge": "Para chefs de catering e eventos",
    "painsTitle": "O Que um Chef de Catering Não Pode Deixar de Resolver",
    "pains": [
      "Escandalar menus com variabilidade alta de convidados (50, 200, 500) quando os preços dos ingredientes mudam todas as semanas",
      "Planificar produção, mise en place e compras em grande escala sem desvios",
      "Coordenar logística, transporte e montagem nas instalações do cliente respeitando tempos e temperaturas",
      "Manter APPCC e rastreabilidade fora do local fixo, em instalações externas e veículos refrigerados",
      "Desenhar menus criativos por tipo de evento (casamento, corporativo, cocktail, gala) sem reinventar cada vez",
      "Comunicar com a equipa de produção, transporte e serviço com documentação clara"
    ],
    "featuresTitle": "Como o AI Chef Pro Ajuda um Chef de Catering",
    "features": [
      {
        "icon": "PartyPopper",
        "title": "Catering AI+",
        "description": "Agente especializado em catering e eventos gastronómicos: casamentos, corporativos, cocktails e galas com conhecimento profissional."
      },
      {
        "icon": "Sparkles",
        "title": "Culinária Criativa + Food Pairing AI",
        "description": "Chuva de ideias para menus de evento. A Culinária Criativa entrega receita + escandalo CSV pronto para o Kit de Escandallos Pro."
      },
      {
        "icon": "Calculator",
        "title": "Escandalos por evento",
        "description": "Kit de Escandallos Pro: carregas o CSV com os teus preços reais, ajustas o número de convidados e obténs custo, food cost % e margem instantaneamente."
      },
      {
        "icon": "Layers",
        "title": "Calcula Pax",
        "description": "Calculadora de porções que escala receitas para 50, 200, 500 ou 1000 comensais em segundos."
      },
      {
        "icon": "CheckSquare",
        "title": "Kit de Tareas Catering",
        "description": "Modelos específicos para produção, transporte, montagem, serviço e desmontagem nas instalações do cliente."
      },
      {
        "icon": "ShieldCheck",
        "title": "APPCC fora do local",
        "description": "Pack APPCC com modelos adaptados a produto que viaja: rastreabilidade, temperatura em transporte e registos em instalações externas."
      },
      {
        "icon": "Image",
        "title": "GastroIMG Gen+",
        "description": "Fotografia gastronómica com IA para apresentações a clientes, propostas de evento e notas de imprensa."
      },
      {
        "icon": "ShieldCheck",
        "title": "ID Alergénios",
        "description": "Identificação automática de alergénios crítica para eventos com muitos convidados de perfis alimentares distintos."
      },
      {
        "icon": "BookOpen",
        "title": "Sosa Ingredients",
        "description": "Assistente para seleção de ingredientes técnicos do catálogo Sosa, especialmente útil em cocktails e sobremesas."
      }
    ],
    "workflowTitle": "Um Dia Real de um Chef de Catering com AI Chef Pro",
    "workflow": [
      "08:30 · Catering AI+ — o agente ajuda-te a fechar a proposta de menu para um casamento de 180 convidados segundo o briefing do cliente.",
      "09:30 · Culinária Criativa — desenvolves os 12 pratos do menu com receita detalhada e escandalo CSV com preços de referência.",
      "10:30 · Calcula Pax + Kit de Escandallos Pro — escalas para 180 comensais, carregas o CSV com os teus preços reais e validas a margem objetivo.",
      "12:00 · Validação com cliente — exportas a proposta com fichas técnicas e fotografia gastronómica do GastroIMG Gen+.",
      "14:00 · Kit de Tareas Catering — planificas produção, transporte, montagem, serviço e desmontagem do evento de sábado.",
      "16:00 · APPCC fora do local — preparas registos de temperatura em transporte e rastreabilidade em instalações externas com o Pack APPCC.",
      "18:00 · ID Alergénios — geras a ficha de alergénios por prato pronta para a sala e para os convidados com restrições.",
      "19:30 · Briefing à equipa — montas o briefing de serviço com a equipa de cozinha e sala do evento, tudo a partir de uma única fonte."
    ],
    "productsTitle": "Modelos e Kits Descarregáveis para Chefs de Catering",
    "productIds": [
      "kit-tareas-catering",
      "kit-escandallos",
      "pack-appcc",
      "kit-plan-financiero",
      "pro-prompts-ebook",
      "kit-inventario"
    ],
    "testimonialQuote": "Os escandalos por evento poupam-me horas. Fecho um menu de 200 convidados com margem validada em 30 minutos. Antes era metade da tarde com calculadora e guardanapos. E ter o APPCC adaptado a evento fora do local tirou-nos uma dor de cabeça enorme com clientes corporativos.",
    "testimonialAuthor": "Andrea Costa",
    "testimonialRole": "Chef de Catering, especialista em eventos corporativos e casamentos",
    "faqTitle": "Perguntas Frequentes de Chefs de Catering",
    "faqs": [
      {
        "q": "Serve para qualquer tamanho de catering?",
        "a": "Sim. Desde caterings boutique de 50 convidados por mês até empresas com mais de 1000 serviços por mês e eventos de 2000 comensais."
      },
      {
        "q": "Permite gerir a variabilidade de convidados?",
        "a": "Sim. O Calcula Pax escala receitas para qualquer número de comensais e o Kit de Escandallos Pro recalcula custo, food cost e margem automaticamente."
      },
      {
        "q": "Cobre APPCC fora do local fixo?",
        "a": "Sim. O Pack APPCC tem modelos específicos para produto que viaja em mochila, mota, furgoneta refrigerada ou cozinha central, incluindo rastreabilidade em instalações externas."
      },
      {
        "q": "Há modelos específicos de catering?",
        "a": "Sim. O Kit de Tareas Catering inclui listas detalhadas de produção, transporte, montagem em instalações, serviço e desmontagem, além de protocolos de coordenação com cozinha central."
      },
      {
        "q": "Como se adapta ao meu tipo de catering?",
        "a": "Começas com o agente «Quem Sou Eu?», um onboarding de 2 minutos em que contas que tipo de eventos fazes (casamentos, corporativos, cocktails, galas), tamanho médio, cidade e operativa. Tudo se adapta ao teu contexto."
      },
      {
        "q": "Serve para desenhar menus inovadores?",
        "a": "Sim. Catering AI+ + Culinária Criativa + Food Pairing AI + Fermentus Con AI+ trabalham em conjunto para desenhar menus criativos com base profissional, não receitas copiadas da internet."
      }
    ],
    "ctaTitle": "Desenha, escandala e produz eventos sem papéis soltos.",
    "ctaSubtitle": "Começa com o onboarding de 2 minutos. Plano Membro por 10 € por mês com 10.000 créditos para usar todos os agentes.",
    "seo": {
      "title": "IA para Chef de Catering: Menus, Escandalos e APPCC de Evento | AI Chef Pro",
      "description": "Suite de IA para chef de catering: Catering AI+, Culinária Criativa, Calcula Pax, escandalos por evento, APPCC fora de local e planeamento de produção à escala. Começa hoje.",
      "keywords": "IA chef catering, chef catering software, escandalos catering IA, software catering eventos, APPCC catering, menu casamento IA, gestão evento gastronómico IA, chef catering Espanha",
      "ogImage": "https://aichef.pro/og/use-cases/chef-catering.jpg"
    },
    "personalizationTitle": "Personalizado ao Teu Tipo de Catering desde o Minuto Um",
    "personalizationBody": "O AI Chef Pro arranca com o agente «Quem Sou Eu?», um onboarding conversacional de 2 minutos em que contas que tipo de eventos desenhas (casamentos, corporativos, cocktails, galas), tamanho médio, cidade e forma de trabalhar. A partir desse momento, cada agente —desde o Catering AI+ até aos escandalos— responde adaptado ao teu contexto: tipos de serviço, escala da tua cozinha central e operativa real. Não é um formulário: é uma conversa curta que torna a suite verdadeiramente útil para o teu dia a dia como chef de catering.",
    "appsTitle": "Os Agentes de IA que Vais Usar como Chef de Catering",
    "apps": [
      {
        "name": "Catering AI+",
        "category": "Conceitos de Negócio",
        "description": "Agente principal: casamentos, corporativos, cocktails e galas com conhecimento profissional."
      },
      {
        "name": "Culinária Criativa",
        "category": "Criatividade Culinária",
        "description": "Desenvolvimento de pratos profissionais com receita + escandalo CSV pronto para o Kit de Escandallos Pro."
      },
      {
        "name": "Food Pairing AI",
        "category": "Criatividade Culinária",
        "description": "Combinações de ingredientes e harmonizações com base científica."
      },
      {
        "name": "Pastelaria Criativa",
        "category": "Criatividade Culinária",
        "description": "Sobremesas de evento com técnica profissional, ideais para banquetes e galas."
      },
      {
        "name": "Fermentus Con AI+",
        "category": "Criatividade Culinária",
        "description": "Para canapés vanguardistas com fermentos, garums e técnicas inovadoras."
      },
      {
        "name": "Calcula Pax",
        "category": "Ferramentas e Utilitários",
        "description": "Calculadora de porções que escala receitas para 50, 200 ou 500 comensais."
      },
      {
        "name": "ID Alergénios",
        "category": "Ferramentas e Utilitários",
        "description": "Identificação automática de alergénios por prato, crítico para eventos grandes."
      },
      {
        "name": "Mermas Genéricas",
        "category": "Ferramentas e Utilitários",
        "description": "Dados precisos de mermas e rendimentos para produção à escala."
      },
      {
        "name": "Conversor Ing",
        "category": "Ferramentas e Utilitários",
        "description": "Conversor de pesos e medidas profissional para produção industrial."
      },
      {
        "name": "Sosa Ingredients",
        "category": "Fornecedores Gastro",
        "description": "Assistente para ingredientes técnicos do catálogo Sosa."
      },
      {
        "name": "GastroIMG Gen+",
        "category": "Conhecimento Gastro",
        "description": "Fotografia gastronómica com IA para propostas a clientes e notas de imprensa."
      }
    ],
    "metrics": [
      {
        "value": "×10",
        "label": "velocidade fecho menu evento"
      },
      {
        "value": "+5 pp",
        "label": "margem após escandalo real"
      },
      {
        "value": "−50 %",
        "label": "tempo em planeamento logístico"
      },
      {
        "value": "11+",
        "label": "agentes para o teu catering"
      }
    ],
    "beforeAfter": {
      "beforeTitle": "Sem AI Chef Pro",
      "beforeItems": [
        "Fechar menu de evento com cliente: metade da tarde com calculadora e guardanapos",
        "APPCC fora do local improvisado, sem rastreabilidade real em transporte",
        "Produção para 200 convidados sem escala precisa, mermas altas",
        "Propostas a clientes com modelos Word e fotos de stock",
        "Briefing à equipa em folhas soltas que se perdem"
      ],
      "afterTitle": "Com AI Chef Pro",
      "afterItems": [
        "Fechar menu com margem validada em 30 minutos com Catering AI+ e Kit de Escandallos Pro",
        "APPCC adaptado a produto que viaja com registos a partir do telemóvel e rastreabilidade por evento",
        "Produção escalada com Calcula Pax, mermas controladas com Mermas Genéricas",
        "Propostas comerciais com fotos GastroIMG Gen+ e fichas técnicas profissionais",
        "Briefing centralizado e replicável para produção, transporte, montagem e serviço"
      ]
    },
    "galleryTitle": "O Dia a Dia de um Chef de Catering, em Imagens",
    "gallerySubtitle": "O que vais coordenar com AI Chef Pro: design de menu, produção à escala, logística, montagem em instalações externas, serviço e rastreabilidade.",
    "galleryImages": [
      "/lovable-uploads/ai-gallery/use-case-chef-catering-hero.jpg",
      "/lovable-uploads/ai-gallery/use-case-chef-catering-production.jpg",
      "/lovable-uploads/ai-gallery/use-case-chef-catering-loading.jpg",
      "/lovable-uploads/ai-gallery/use-case-chef-catering-event.jpg",
      "/lovable-uploads/ai-gallery/use-case-chef-catering-tasting.jpg",
      "/lovable-uploads/ai-gallery/use-case-chef-catering-temp.jpg"
    ]
  },
  "propietario-catering": {
    "h1": "IA para Proprietários de Empresa de Catering",
    "heroSubtitle": "Controle a rentabilidade por evento, escale a produção, gere equipas eventuais e faça crescer a sua empresa de catering com uma suite de agentes de IA especializados em hotelaria.",
    "heroTagline": "Crescimento controlado, margem real, eventos sem caos",
    "badge": "Para proprietários de empresa de catering",
    "painsTitle": "O Que um Proprietário de Catering Não Pode Deixar de Resolver",
    "pains": [
      "Gerir margens com variabilidade alta entre eventos: um casamento, um cocktail corporativo e um coffee break têm rentabilidades muito distintas",
      "Escalar produção sem perder qualidade nem controlo de custos quando chegam picos de casamentos ou época de eventos",
      "Coordenar equipas eventuais e quadro fixo com escalas, contratos por evento e custos laborais claros",
      "Reporting financeiro a investidores ou sócios com dados consolidados, não Excel improvisados",
      "Captar clientes corporativos com propostas profissionais que fechem contratos de maior ticket",
      "Decidir que eventos aceitar e quais rejeitar com dados de margem real, não por sensação"
    ],
    "featuresTitle": "Como AI Chef Pro Ajuda um Proprietário de Catering",
    "features": [
      {
        "icon": "PartyPopper",
        "title": "Catering AI+",
        "description": "Agente especializado em eventos gastronómicos: casamentos, corporativos, cocktails e galas com conhecimento profissional."
      },
      {
        "icon": "FileText",
        "title": "Kit Plan Financiero",
        "description": "Cash flow, P&L mensal, dashboard de rácios e rentabilidade por evento e por cliente. Modelos profissionais adaptados a catering."
      },
      {
        "icon": "Calculator",
        "title": "Fichas técnicas por evento",
        "description": "Culinária Criativa entrega receita + ficha técnica CSV; Kit de Escandallos Pro gere-a com os seus preços reais e margem objetivo."
      },
      {
        "icon": "Users",
        "title": "Kit Gestión de Personal",
        "description": "Escalas para pessoal fixo e eventual, contratos por evento, controlo de horas e custos laborais por serviço."
      },
      {
        "icon": "ShieldCheck",
        "title": "APPCC e certificações",
        "description": "Pack APPCC com modelos adaptados a catering: rastreabilidade, transporte e registos prontos para inspeção e clientes corporativos."
      },
      {
        "icon": "Sparkles",
        "title": "BlogPost SEO Gen+ + MenuDish Local SEO",
        "description": "Suite SEO para captar clientes corporativos com tráfego orgânico e melhor posicionamento."
      },
      {
        "icon": "Image",
        "title": "GastroIMG Gen+",
        "description": "Fotografia gastronómica com IA para propostas a clientes, apresentações e galeria web."
      },
      {
        "icon": "BarChart3",
        "title": "Dashboard de operações",
        "description": "KPIs financeiros consolidados, rácio de ocupação, rentabilidade por linha de negócio (casamentos, corporativos, cocktails)."
      },
      {
        "icon": "Search",
        "title": "Sonar Deep Research",
        "description": "Investigação profunda de mercado, concorrentes e tendências para decisões estratégicas de crescimento."
      }
    ],
    "workflowTitle": "Um Dia Real de um Proprietário de Catering com AI Chef Pro",
    "workflow": [
      "08:30 · Kit Plan Financiero — abre o dashboard e deteta que um evento do fim de semana tem margem de 18 %, abaixo do objetivo (28 %).",
      "09:30 · Kit de Escandallos Pro — analisa a ficha técnica de custos do evento e ajusta o menu ou o preço antes de fechar o contrato.",
      "11:00 · Catering AI+ — fecha proposta para empresa cliente com apresentação gerada com IA e validada com o agente.",
      "12:30 · GastroIMG Gen+ — gera as fotografias dos pratos do menu proposto para incluir na apresentação.",
      "14:00 · Reunião com cliente corporativo — apresenta proposta fechada em 1 hora em vez dos 3 dias tradicionais.",
      "16:30 · Kit Plan Financiero — valida o previsional do trimestre, exporta para PDF para reunião com sócios.",
      "18:00 · Kit Gestión de Personal — revê a escala do fim de semana com pessoal fixo e eventual, assina contratos por evento.",
      "20:00 · BlogPost SEO Gen+ — publica um post sobre o último grande evento corporativo para captar novos clientes organicamente."
    ],
    "productsTitle": "Modelos e Kits Descarregáveis para Empresas de Catering",
    "productIds": [
      "kit-plan-financiero",
      "kit-escandallos",
      "pack-appcc",
      "kit-tareas-catering",
      "kit-gestion-personal",
      "kit-inventario"
    ],
    "testimonialQuote": "AI Chef Pro deu-me controlo financeiro real. Sei exatamente em que eventos ganho dinheiro e em quais não, e isso permitiu-me dizer não a clientes que não eram rentáveis. No primeiro trimestre subimos 4 pontos de margem sem tocar nos preços. Apenas ajustando menus e rejeitando eventos maus.",
    "testimonialAuthor": "Roberto Iglesias",
    "testimonialRole": "Proprietário, empresa de catering corporativo (2M€ faturação anual)",
    "faqTitle": "Perguntas Frequentes de Proprietários de Catering",
    "faqs": [
      {
        "q": "Serve para catering boutique com menos de 5 funcionários?",
        "a": "Sim. É ideal para boutique porque consolida operativa, finanças, marketing e propostas a clientes numa só ferramenta. O cliente típico começa com 1 plano pessoal e cresce para empresa."
      },
      {
        "q": "E para empresas grandes com 50+ funcionários eventuais?",
        "a": "Também. O Kit Gestión de Personal escala para equipas grandes com escalas, contratos por evento e consolidação de custos laborais. Há clientes com 100+ serviços por mês."
      },
      {
        "q": "Integra-se com o meu software contabilístico ou ERP?",
        "a": "Exporta Excel, PDF e CSV compatíveis com a maioria dos ERPs e gestorias. A sua equipa financeira recebe documentação pronta a integrar."
      },
      {
        "q": "Há plano empresa para catering grande?",
        "a": "Sim. A partir de certa faturação há planos empresa com onboarding personalizado, dashboards consolidados, formação da equipa central e suporte prioritário."
      },
      {
        "q": "Como me ajuda a captar clientes corporativos?",
        "a": "BlogPost SEO Gen+ e MenuDish Local SEO captam tráfego orgânico para o seu site; Catering AI+ ajuda a redigir propostas profissionais; GastroIMG Gen+ gera fotografias para apresentações; Keyword Discovery AI+ encontra as pesquisas reais de empresas na sua zona."
      },
      {
        "q": "É seguro confiar o plano financeiro a uma IA?",
        "a": "Sim. O Kit Plan Financiero é um modelo Excel profissional com fórmulas pré-carregadas, não IA. Você insere os dados reais e a ferramenta calcula. Os agentes IA só são usados para apoiar em decisões, redação de propostas e análise, não em cálculo financeiro crítico."
      }
    ],
    "ctaTitle": "Faça crescer o seu catering com margem real, não intuição.",
    "ctaSubtitle": "Comece com o onboarding de 2 minutos. Plano Membro por 10 € por mês com 10.000 créditos para usar todos os agentes.",
    "seo": {
      "title": "IA para Proprietários de Empresa de Catering: Rentabilidade e Plano Financeiro | AI Chef Pro",
      "description": "Suite de IA para empresas de catering: rentabilidade por evento, produção em escala, equipas eventuais, plano financeiro e captação de clientes corporativos. Comece hoje.",
      "keywords": "IA empresa catering, proprietário catering IA, software catering, gestão empresa catering, plano financeiro catering, rentabilidade catering, captação clientes corporativos catering, escalar empresa catering, proprietário catering Espanha",
      "ogImage": "https://aichef.pro/og/use-cases/propietario-catering.jpg"
    },
    "personalizationTitle": "Personalizado para a Sua Empresa desde o Minuto Um",
    "personalizationBody": "AI Chef Pro arranca com o agente «Quem Sou Eu?», um onboarding conversacional de 2 minutos em que lhe conta que tipo de catering opera (casamentos, corporativos, cocktails, galas), tamanho médio de evento, cidade e volume anual. A partir desse momento, cada agente —desde Catering AI+ até ao Plano Financeiro— responde adaptado ao seu contexto: tipos de serviço, escala real e mercado-alvo. Não é um formulário: é uma conversa curta que torna a suite verdadeiramente útil para a sua empresa.",
    "appsTitle": "Os Agentes IA que Vai Usar como Proprietário de Catering",
    "apps": [
      {
        "name": "Catering AI+",
        "category": "Conceitos de Negócio",
        "description": "Agente principal: casamentos, corporativos, cocktails e galas com conhecimento profissional."
      },
      {
        "name": "Gerente Restaurante Pro",
        "category": "Gastro Profile Pro",
        "description": "Assistente operativo e financeiro para apoiá-lo em decisões e reporting a sócios."
      },
      {
        "name": "Culinária Criativa",
        "category": "Criatividade Culinária",
        "description": "Desenvolvimento de menus de evento com receita + ficha técnica CSV pronta para o Kit de Escandallos Pro."
      },
      {
        "name": "Pastelaria Criativa",
        "category": "Criatividade Culinária",
        "description": "Sobremesas de evento e banquete com técnica profissional."
      },
      {
        "name": "Calcula Pax",
        "category": "Ferramentas e Utilitários",
        "description": "Calculadora de porções que escala receitas para 50, 200 ou 500 comensais."
      },
      {
        "name": "ID Alergénios",
        "category": "Ferramentas e Utilitários",
        "description": "Identificação automática de alergénios por receita, crítica para eventos grandes."
      },
      {
        "name": "BlogPost SEO Gen+",
        "category": "Conteúdos e Redes Sociais",
        "description": "Posts de blog para captar tráfego orgânico para o seu site de catering."
      },
      {
        "name": "MenuDish Local SEO",
        "category": "Conteúdos e Redes Sociais",
        "description": "Descrições SEO para melhorar o posicionamento web do seu catering."
      },
      {
        "name": "Keyword Discovery AI+",
        "category": "Conteúdos e Redes Sociais",
        "description": "Investigação de palavras-chave para captar empresas que procuram catering na sua zona."
      },
      {
        "name": "GastroIMG Gen+",
        "category": "Gastro Conhecimento",
        "description": "Fotografia gastronómica para propostas a clientes e apresentações comerciais."
      },
      {
        "name": "Sonar Deep Research",
        "category": "Modelos IA + LLM",
        "description": "Investigação de mercado, concorrentes e tendências do setor de eventos."
      },
      {
        "name": "Coach Mental",
        "category": "Ferramentas e Utilitários",
        "description": "Coaching para gestão de stress, decisões difíceis e conversas com sócios ou equipa."
      }
    ],
    "metrics": [
      {
        "value": "+4 pp",
        "label": "margem no primeiro trimestre"
      },
      {
        "value": "×3",
        "label": "velocidade de fecho de propostas"
      },
      {
        "value": "−40 %",
        "label": "tempo em reporting financeiro"
      },
      {
        "value": "12+",
        "label": "agentes para a sua empresa"
      }
    ],
    "beforeAfter": {
      "beforeTitle": "Sem AI Chef Pro",
      "beforeItems": [
        "Não saber qual dos 50 eventos do mês é realmente rentável",
        "Fechar propostas a clientes corporativos em 3 dias com modelos Word",
        "Escalas de pessoal eventual em Excel manual sem controlo de custos",
        "APPCC dispar entre eventos, problema com clientes corporativos exigentes",
        "Marketing improvisado ou externalizado a preço alto sem captar leads orgânicos"
      ],
      "afterTitle": "Com AI Chef Pro",
      "afterItems": [
        "Rentabilidade por evento e por cliente clara, decisões de aceitar/rejeitar com dados",
        "Fechar propostas em 1 hora com Catering AI+ + GastroIMG Gen+ + apresentação profissional",
        "Escalas com Kit Gestión de Personal: controlo de horas e custos consolidados",
        "APPCC unificado e profissional, pronto para qualquer inspeção ou cliente corporativo",
        "Suite SEO a captar leads orgânicos sem gasto em agências"
      ]
    },
    "galleryTitle": "O Dia a Dia de um Proprietário de Catering, em Imagens",
    "gallerySubtitle": "O que vai coordenar com AI Chef Pro: pricing, propostas a clientes, eventos em grande escala, equipas, armazém logístico e reporting financeiro.",
    "galleryImages": [
      "/lovable-uploads/ai-gallery/use-case-propietario-catering-hero.jpg",
      "/lovable-uploads/ai-gallery/use-case-propietario-catering-event.jpg",
      "/lovable-uploads/ai-gallery/use-case-propietario-catering-pricing.jpg",
      "/lovable-uploads/ai-gallery/use-case-propietario-catering-team.jpg",
      "/lovable-uploads/ai-gallery/use-case-propietario-catering-storage.jpg",
      "/lovable-uploads/ai-gallery/use-case-propietario-catering-presentation.jpg"
    ]
  },
  "bartender-coctelero": {
    "h1": "IA para Bartender e Cocteleiro",
    "heroSubtitle": "Desenhe cartas de cocktails com custo de receita profissional, custo por bebida com custo real e técnica, e crie drinks de autor com storytelling e harmonização com uma suite de agentes de IA gastronómica especializados em coctelaria.",
    "heroTagline": "Coctelaria com margem real e técnica de autor",
    "badge": "Para bartenders, cocteleiros e mixólogos",
    "painsTitle": "O Que um Bartender Não Pode Deixar de Resolver",
    "pains": [
      "Calcular custos de cocktails complexos com muitos ingredientes (espirituosos, cordiais, infusões, garnishes) sem perder horas com a calculadora",
      "Renovar a carta a cada temporada com bebidas novas mantendo margem e um food cost coerente com o resto da barra",
      "Padronizar receitas na barra para que qualquer empregado de mesa replique a bebida com o mesmo equilíbrio de cada vez",
      "Controlar mermas na barra: quebra de cristalaria, sobre-pour, evaporação, garnishes que se desperdiçam",
      "Storytelling: cada cocktail precisa de um nome, uma história e uma harmonização que justifique o ticket alto",
      "Diferenciar-se em zona concorrida com coctelaria de autor, branding visual e redes sociais ativas"
    ],
    "featuresTitle": "Como AI Chef Pro Ajuda um Bartender",
    "features": [
      {
        "icon": "Wine",
        "title": "Bar & Lounge AI+",
        "description": "Agente especializado em coctelaria profissional, vinotecas, bares de copos e bebidas espirituosas com técnica avançada."
      },
      {
        "icon": "Sparkles",
        "title": "Food Pairing AI",
        "description": "Combinações inesperadas para cocktails de autor com base científica e harmonizações com cozinha."
      },
      {
        "icon": "Calculator",
        "title": "Custos por bebida",
        "description": "Bar & Lounge AI+ entrega receita + custo de receita CSV com técnica; Kit de Escandallos Pro gere-o com custo real por bebida, food cost % e preço sugerido."
      },
      {
        "icon": "BookOpen",
        "title": "Fichas técnicas de cocktail",
        "description": "Receita, técnica, garnish, glassware, harmonização e storytelling num único documento pronto para a equipa."
      },
      {
        "icon": "CheckSquare",
        "title": "Kit de Tareas Bar",
        "description": "Modelos: mise de barra, preparação de cordiais e infusões, procedimentos por turno, fecho de caixa, controlo de stock."
      },
      {
        "icon": "ShieldCheck",
        "title": "Pack APPCC bar",
        "description": "Rastreabilidade de gelo, garnishes frescos, infusões caseiras e temperaturas críticas."
      },
      {
        "icon": "Calendar",
        "title": "Gastro Calendar",
        "description": "Planeamento de carta sazonal: cocktails de verão, quentes de inverno, cartas temáticas para São Valentim, Natal e eventos."
      },
      {
        "icon": "Image",
        "title": "GastroIMG Gen+ + InstaFlow AI Pro",
        "description": "Fotografia de cocktails com IA de referência + conteúdo para Instagram com calendário editorial profissional."
      },
      {
        "icon": "BarChart3",
        "title": "KPIs de barra",
        "description": "Ticket médio, rotação de bebidas, margem por categoria (clássicos, signature, vinhos, cervejas)."
      }
    ],
    "workflowTitle": "Um Dia Real de um Bartender com AI Chef Pro",
    "workflow": [
      "11:00 · Abertura — checklist Kit de Tareas Bar: mise de garnishes frescos, preparação de cordiais caseiros, carregar gelo, revisão de stock.",
      "12:00 · Bar & Lounge AI+ — desenvolve um novo signature para a carta de verão (gin com shrub de morangos e manjericão). Culinária Criativa entrega receita + custo de receita CSV.",
      "13:00 · Food Pairing AI — valida a harmonização com um prato da cozinha e afina a técnica.",
      "14:00 · Kit de Escandallos Pro — carrega o CSV com os seus preços reais de espirituoso premium e ingredientes, valida margem por bebida e food cost %.",
      "17:00 · Serviço — a equipa replica a bebida com a ficha técnica (receita, técnica, garnish, glassware, storytelling).",
      "19:00 · Gastro Calendar — atualiza o calendário editorial do Instagram com o lançamento do novo signature.",
      "20:00 · GastroIMG Gen+ + InstaFlow AI Pro — gera a imagem de referência da bebida e os posts para o lançamento.",
      "02:00 · Encerramento — limpeza profunda, APPCC assinado, controlo de mermas e stock final."
    ],
    "productsTitle": "Modelos e Kits Recomendados para Coctelaria",
    "productIds": [
      "kit-tareas-bar",
      "kit-escandallos",
      "pack-appcc",
      "kit-inventario",
      "kit-gestion-personal",
      "pro-prompts-ebook"
    ],
    "testimonialQuote": "AI Chef Pro mudou a minha forma de fechar cartas de cocktails. Antes era uma semana de guardanapos e calculadora; agora é um dia com custo de receita profissional, ficha técnica com storytelling e harmonização validada, pronta para a minha equipa replicar. Subimos a margem 5 pontos e triplicámos o engagement no Instagram com GastroIMG.",
    "testimonialAuthor": "Hugo Vázquez",
    "testimonialRole": "Bartender, cocktail bar de autor",
    "faqTitle": "Perguntas Frequentes de Bartenders",
    "faqs": [
      {
        "q": "Serve para coctelaria clássica, de autor ou casual?",
        "a": "Para as três. Bar & Lounge AI+ entende desde clássicos do IBA até vanguarda: shrubs, infusões, fermentados, espumas, fumados controlados, técnica avançada de barra."
      },
      {
        "q": "Cobre vinhos e cervejas além de coctelaria?",
        "a": "Sim. O agente cobre todo o espectro de barra: cocktails, vinhos, cervejas, bebidas espirituosas, sem álcool e harmonizações."
      },
      {
        "q": "Permite criar cartas de bebidas com storytelling e técnica?",
        "a": "Sim. As fichas incluem receita, técnica, garnish, glassware, história e harmonização prontos para a sala. Ideal para subir o ticket médio justificando o preço."
      },
      {
        "q": "Gera conteúdo visual para Instagram e carta?",
        "a": "Sim. GastroIMG Gen+ gera imagens de referência profissionais de cada bebida para Instagram, web e carta; InstaFlow AI Pro programa conteúdo com calendário editorial. Lembre-se de que a imagem IA é de referência visual: a foto definitiva é feita por si com o seu cocktail empratado real."
      },
      {
        "q": "Como me ajuda com a sazonalidade da carta?",
        "a": "Gastro Calendar planifica as cartas sazonais (verão, outono, Natal, São Valentim) com antecedência. O Kit Plan Financiero projeta o cash flow sazonal realista para que chegue com stock e caixa a cada pico."
      }
    ],
    "ctaTitle": "A sua coctelaria com margem real e técnica de autor.",
    "ctaSubtitle": "Comece com o onboarding de 2 minutos. Plano Membro por 10 € por mês com 10.000 créditos para usar todos os agentes.",
    "seo": {
      "title": "IA para Bartender e Cocteleiro: Cartas, Custos de Receita e Storytelling | AI Chef Pro",
      "description": "Suite de IA para bartenders profissionais: Bar & Lounge AI+, Food Pairing AI, custos por bebida, fichas técnicas com storytelling e branding visual. Comece hoje.",
      "keywords": "IA bartender, IA cocteleiro, software coctelaria, custos de cocktail, food pairing IA, carta cocktails IA, mixólogo IA, signature cocktail",
      "ogImage": "https://aichef.pro/og/use-cases/bartender-coctelero.jpg"
    },
    "personalizationTitle": "Personalizado para a Sua Barra desde o Minuto Um",
    "personalizationBody": "AI Chef Pro arranca com o agente «Quem Sou Eu?», um onboarding conversacional de 2 minutos no qual lhe conta que tipo de barra opera (cocktail bar de autor, vinoteca, bar de hotel, lounge, restaurante com coctelaria), tamanho da equipa, cidade e estilo de carta. Cada agente —desde Bar & Lounge AI+ até Gastro Calendar— responde adaptado ao seu produto, mercado e operativa real.",
    "appsTitle": "Os Agentes IA que Vai Usar na Sua Barra",
    "apps": [
      {
        "name": "Bar & Lounge AI+",
        "category": "Criatividade Culinária",
        "description": "Agente especializado em coctelaria profissional, vinhos, cervejas e bebidas espirituosas com técnica avançada."
      },
      {
        "name": "Food Pairing AI",
        "category": "Criatividade Culinária",
        "description": "Combinações inesperadas com base científica e harmonizações cocktail + prato."
      },
      {
        "name": "Culinária Criativa",
        "category": "Criatividade Culinária",
        "description": "Desenvolvimento de bebidas signature com receita + custo de receita CSV."
      },
      {
        "name": "Sosa Ingredients",
        "category": "Fornecedores Gastro",
        "description": "Catálogo Sosa para texturas avançadas, gelificantes e técnicas de barra de autor."
      },
      {
        "name": "tSpoonLab Agent",
        "category": "Fornecedores Gastro",
        "description": "Assistente do catálogo tSpoonLab para aplicações avançadas de mixologia."
      },
      {
        "name": "Mermas Genéricas",
        "category": "Ferramentas e Utilitários",
        "description": "Dados de mermas na barra: quebra, sobre-pour, evaporação, garnishes desperdiçados."
      },
      {
        "name": "ID Alergénios",
        "category": "Ferramentas e Utilitários",
        "description": "Identificação automática de alergénios por bebida: sulfitos, laticínios, frutos secos, glúten."
      },
      {
        "name": "GastroIMG Gen+",
        "category": "Gastro Conhecimento",
        "description": "Fotografia gastronómica IA de referência para web, redes e carta de cocktails."
      },
      {
        "name": "InstaFlow AI Pro",
        "category": "Conteúdos e Redes Sociais",
        "description": "Instagram com calendário editorial profissional para coctelaria de autor."
      },
      {
        "name": "MenuDish Local SEO",
        "category": "Conteúdos e Redes Sociais",
        "description": "Captar clientes locais que procuram \"cocktail bar perto\" no Google e Maps."
      },
      {
        "name": "Gastro Calendar",
        "category": "Conteúdos e Redes Sociais",
        "description": "Planeamento de carta sazonal: verão, inverno, São Valentim, Natal."
      },
      {
        "name": "Gerador de Pins Pinterest",
        "category": "Conteúdos e Redes Sociais",
        "description": "Pinterest captura tráfego orgânico estável para cocktails com storytelling."
      }
    ],
    "metrics": [
      {
        "value": "+5 pp",
        "label": "margem após calcular custos da carta"
      },
      {
        "value": "×3",
        "label": "engagement Instagram com GastroIMG"
      },
      {
        "value": "−1 dia",
        "label": "fecho de carta de temporada (de 7 a 1)"
      },
      {
        "value": "12+",
        "label": "agentes para a sua barra"
      }
    ],
    "beforeAfter": {
      "beforeTitle": "Sem AI Chef Pro",
      "beforeItems": [
        "Cartas fechadas em uma semana de guardanapos e calculadora",
        "Custos de receita sem food cost real por bebida, signatures em perdas sem saber",
        "Fichas técnicas inexistentes: cada empregado de mesa replica como pode",
        "Mermas na barra sem rastreabilidade real",
        "Instagram improvisado com fotos do telemóvel sem continuidade"
      ],
      "afterTitle": "Com AI Chef Pro",
      "afterItems": [
        "Carta de temporada fechada em um dia com custo de receita profissional e storytelling",
        "Food cost real por bebida, signatures com margem validada",
        "Fichas técnicas com receita, técnica, garnish, glassware, harmonização e storytelling",
        "Mermas controladas com Mermas Genéricas e modelos específicos de barra",
        "Instagram com calendário editorial profissional e GastroIMG Gen+"
      ]
    },
    "galleryTitle": "Como Funciona uma Barra de Autor",
    "gallerySubtitle": "O que vai coordenar com AI Chef Pro: barra, cocktails, técnica, mise, ingredientes e equipamento. Imagens geradas com IA como referência visual do conceito.",
    "galleryImages": [
      "/lovable-uploads/ai-gallery/use-case-bartender-hero.jpg",
      "/lovable-uploads/ai-gallery/use-case-bartender-cocktails.jpg",
      "/lovable-uploads/ai-gallery/use-case-bartender-technique.jpg",
      "/lovable-uploads/ai-gallery/use-case-bartender-mise.jpg",
      "/lovable-uploads/ai-gallery/use-case-bartender-ingredients.jpg",
      "/lovable-uploads/ai-gallery/use-case-bartender-team.jpg"
    ]
  },
  "pizzero": {
    "h1": "IA para Pizzaiolo e Pizzaiolo",
    "heroSubtitle": "Otimize massas e fermentações, escandalle por pizza com custo real, controle técnica de forno e operação com uma suite de agentes de IA gastronómica especializados em cozinha italiana profissional.",
    "heroTagline": "Pizza com técnica autêntica e margem real",
    "badge": "Para pizzaiolos, pizzaioli e proprietários de pizzaria",
    "painsTitle": "O Que um Pizzaiolo Não Pode Deixar de Resolver",
    "pains": [
      "Padronizar massa, hidratação e fermentação em cada turno com critério técnico (napolitana, romana, in pala, americana)",
      "Escandallar pizzas com muitas variantes de toppings e manter food cost coerente entre todas as opções da carta",
      "Mermas na massa (sobrefermentação, formação falhada), mozzarella (humidade, evaporação) e molhos",
      "Manter qualidade consistente no forno (lenha, elétrico, gás) com picos altos de procura aos fins de semana",
      "Diferenciar-se em zona competitiva com pizzas de autor, farinhas premium e storytelling visual",
      "Captar pedidos de delivery com margem enquanto se gere o espaço com serviço de sala"
    ],
    "featuresTitle": "Como o AI Chef Pro Ajuda um Pizzaiolo",
    "features": [
      {
        "icon": "Pizza",
        "title": "Cozinha Italiana",
        "description": "Agente especializado em cozinha italiana profissional: massas (napolitana, romana, in pala, americana), molhos, toppings e técnica de forno."
      },
      {
        "icon": "Beaker",
        "title": "Fermentus Con AI+",
        "description": "Para massas mãe, pré-fermentos (biga, poolish), hidratações altas e fermentações longas controladas em frio."
      },
      {
        "icon": "Calculator",
        "title": "Escandallos por pizza",
        "description": "Cozinha Italiana entrega receita + escandallo CSV; Kit de Escandallos Pro gere com custo real por pizza, food cost % e preço sugerido."
      },
      {
        "icon": "CheckSquare",
        "title": "Kit de Tareas Pizzería",
        "description": "Modelos: mise de massa, preparação de molhos, mise de toppings, serviço de sala, delivery, encerramento e limpeza de forno."
      },
      {
        "icon": "ShieldCheck",
        "title": "Pack APPCC pizzaria",
        "description": "Rastreabilidade de farinhas, massa mãe, mozzarella, molhos e temperaturas críticas em forno e câmara."
      },
      {
        "icon": "Calendar",
        "title": "Gastro Calendar",
        "description": "Planeamento de carta sazonal: pizzas de verão com tomate fresco, outono com cogumelos e trufa, especiais para São Valentim e eventos."
      },
      {
        "icon": "Image",
        "title": "GastroIMG Gen+ + InstaFlow AI Pro",
        "description": "Fotografia gastronómica IA de referência + Instagram com calendário editorial: a pizzaria vive do impacto visual."
      },
      {
        "icon": "BarChart3",
        "title": "MenuDish Local SEO",
        "description": "Captar clientes locais que procuram \"pizzaria perto\" no Google e Maps com descrições otimizadas."
      },
      {
        "icon": "Sparkles",
        "title": "Mermas Genéricas",
        "description": "Dados precisos de mermas por processo (massa, mozzarella, recortes, delivery) integrados no escandallo."
      }
    ],
    "workflowTitle": "Um Dia Real de um Pizzaiolo com AI Chef Pro",
    "workflow": [
      "08:00 · Abertura — checklist Kit de Tareas Pizzería: refresco de massa mãe ou biga, preparação de molho de tomate San Marzano, fermentação controlada de bolas de massa.",
      "10:00 · Cozinha Italiana — desenvolve uma nova pizza sazonal (abóbora assada, gorgonzola, mel e noz) com critério técnico. Culinária Criativa entrega receita + escandallo CSV.",
      "11:00 · Fermentus Con AI+ — ajusta hidratação para 70 % e tempos de fermentação em frio de 48 horas para a massa napolitana.",
      "12:00 · Kit de Escandallos Pro — carrega o CSV com os seus preços reais de farinha caputo, mozzarella di bufala e toppings, valida margem e food cost %.",
      "13:00 · Serviço de almoço — a equipa replica com modelos de mise e preparação, picos coordenados.",
      "17:00 · Pausa entre serviços — Gastro Calendar planifica a carta de outono e eventos.",
      "19:00 · GastroIMG Gen+ + InstaFlow AI Pro — gera a imagem de referência da nova pizza e os posts para Instagram.",
      "23:00 · Encerramento — limpeza profunda do forno, APPCC assinado, preparação de massa para amanhã."
    ],
    "productsTitle": "Modelos e Kits Recomendados para Pizzaria",
    "productIds": [
      "kit-tareas-pizzeria",
      "kit-escandallos",
      "pack-appcc",
      "kit-inventario",
      "kit-gestion-personal",
      "pro-prompts-ebook"
    ],
    "testimonialQuote": "Fizemos escandallo pizza a pizza e descobrimos que 4 estavam com prejuízo apesar de venderem bem. Redesenhámo-las com Cozinha Italiana simplificando toppings sem perder identidade e subimos a margem 4 pontos sem tocar no preço. Fermentus mudou-nos a massa: hidratação 70 %, fermentação 48 horas, alveolado perfeito.",
    "testimonialAuthor": "Giovanni Russo",
    "testimonialRole": "Pizzaiolo e proprietário, pizzaria napolitana",
    "faqTitle": "Perguntas Frequentes de Pizzaiolos",
    "faqs": [
      {
        "q": "Serve para pizza napolitana, romana, in pala ou americana?",
        "a": "Para as quatro. Cozinha Italiana e Fermentus cobrem todo o espetro de massas (alveolado, hidratação, fermentações), técnicas de cozedura (lenha, elétrico, gás) e estilos italianos e americanos."
      },
      {
        "q": "Cobre técnica de massa mãe e pré-fermentos?",
        "a": "Sim. Fermentus Con AI+ entende biga, poolish, massa mãe líquida e sólida, hidratações altas e fermentações controladas em frio. Raciocina como pizzaiolo profissional, não receitas de YouTube."
      },
      {
        "q": "Cobre delivery além do espaço físico?",
        "a": "Sim. O Kit de Tareas Pizzería inclui modelos específicos para delivery: temperaturas, embalagem que mantém a cozedura, mermas de transporte e procedimentos de pickup."
      },
      {
        "q": "Gera conteúdo visual para Instagram, Glovo e Uber Eats?",
        "a": "Sim. GastroIMG Gen+ gera imagens de referência profissionais para Instagram, plataformas de delivery e carta; melhor foto = mais cliques e melhor ranking. Lembre-se que a imagem IA é de referência visual: a foto definitiva é feita por si com a sua pizza acabada de sair do forno."
      },
      {
        "q": "Como me ajuda com sazonalidade e eventos?",
        "a": "Gastro Calendar planifica as cartas sazonais (verão, outono com cogumelos e trufa, especiais para São Valentim, Páscoa, Natal). O Kit Plan Financiero projeta o cash flow sazonal realista para que chegue com stock e caixa a cada pico."
      }
    ],
    "ctaTitle": "A sua pizzaria com margem real e técnica autêntica.",
    "ctaSubtitle": "Comece com o onboarding de 2 minutos. Plano Membro por 10 € por mês com 10.000 créditos para usar todos os agentes.",
    "seo": {
      "title": "IA para Pizzaiolo e Pizzaiolo: Massas, Escandallos e Técnica Italiana | AI Chef Pro",
      "description": "Suite de IA para pizzaiolos profissionais: Cozinha Italiana, Fermentus para massas e biga, escandallos por pizza, modelos e técnica autêntica. Comece hoje.",
      "keywords": "IA pizzaiolo, IA pizzaiolo, software pizzaria, escandallos pizza, massa mãe pizza, biga poolish pizza, técnica napolitana, pizza romana IA",
      "ogImage": "https://aichef.pro/og/use-cases/pizzero.jpg"
    },
    "personalizationTitle": "Personalizado à Sua Pizzaria desde o Minuto Um",
    "personalizationBody": "O AI Chef Pro arranca com o agente «Quem Sou Eu?», um onboarding conversacional de 2 minutos em que lhe conta que tipo de pizzaria opera (napolitana autêntica, romana al taglio, americana, mista com cozinha italiana, dark kitchen para delivery), tamanho da equipa, cidade e tipo de forno. Cada agente —desde Cozinha Italiana até Gastro Calendar— responde adaptado ao seu produto, mercado e operação real.",
    "appsTitle": "Os Agentes IA que Vai Usar na Sua Pizzaria",
    "apps": [
      {
        "name": "Cozinha Italiana",
        "category": "Criatividade Culinária",
        "description": "Agente especializado em cozinha italiana profissional: massas, molhos, toppings, técnica de forno."
      },
      {
        "name": "Fermentus Con AI+",
        "category": "Criatividade Culinária",
        "description": "Massas mãe, biga, poolish, hidratações altas, fermentações longas controladas."
      },
      {
        "name": "Culinária Criativa",
        "category": "Criatividade Culinária",
        "description": "Desenvolvimento de pizzas signature com receita + escandallo CSV."
      },
      {
        "name": "Sosa Ingredients",
        "category": "Fornecedores Gastro",
        "description": "Catálogo Sosa para farinhas técnicas, melhoradores e combinações avançadas."
      },
      {
        "name": "Mermas Genéricas",
        "category": "Ferramentas e Utilitários",
        "description": "Mermas em massa, mozzarella, molho, recortes e delivery integradas no escandallo."
      },
      {
        "name": "ID Alergénios",
        "category": "Ferramentas e Utilitários",
        "description": "Identificação automática de alergénios por pizza: glúten, laticínios, frutos secos, ovo."
      },
      {
        "name": "GastroIMG Gen+",
        "category": "Gastro Conhecimento",
        "description": "Fotografia gastronómica IA de referência para Glovo, Uber Eats, web e redes sociais."
      },
      {
        "name": "InstaFlow AI Pro",
        "category": "Conteúdos e Redes Sociais",
        "description": "Instagram com calendário editorial profissional para pizzaria de autor."
      },
      {
        "name": "MenuDish Local SEO",
        "category": "Conteúdos e Redes Sociais",
        "description": "Captar clientes locais que procuram \"pizzaria perto\" no Google e Maps."
      },
      {
        "name": "Gastro Calendar",
        "category": "Conteúdos e Redes Sociais",
        "description": "Planeamento de carta sazonal: verão, outono, São Valentim, Natal."
      },
      {
        "name": "Gerador de Pins Pinterest",
        "category": "Conteúdos e Redes Sociais",
        "description": "Pinterest captura tráfego orgânico estável para pizzas com storytelling."
      },
      {
        "name": "BlogPost SEO Gen+",
        "category": "Conteúdos e Redes Sociais",
        "description": "Artigos SEO sobre técnica italiana, massas e harmonizações para captar tráfego."
      }
    ],
    "metrics": [
      {
        "value": "+4 pp",
        "label": "margem após escandallar pizzas"
      },
      {
        "value": "×3",
        "label": "engagement Instagram com GastroIMG"
      },
      {
        "value": "−25 %",
        "label": "mermas em massa e mozzarella"
      },
      {
        "value": "12+",
        "label": "agentes para a sua pizzaria"
      }
    ],
    "beforeAfter": {
      "beforeTitle": "Sem AI Chef Pro",
      "beforeItems": [
        "Massa improvisada por turno: alveolado inconsistente e crocância desigual",
        "Escandallos sem food cost real, pizzas com prejuízo sem saber",
        "Mermas em massa, mozzarella e molho sem rastreabilidade",
        "Instagram improvisado e plataformas de delivery com fotos do telemóvel",
        "APPCC em papel impresso espalhado pela pizzaria"
      ],
      "afterTitle": "Com AI Chef Pro",
      "afterItems": [
        "Massa com critério técnico: hidratação, fermentação e cozedura consistentes",
        "Escandallo profissional por pizza com margem validada e food cost %",
        "Mermas controladas com Mermas Genéricas e modelos específicos",
        "GastroIMG Gen+ + InstaFlow + MenuDish Local SEO captam clientes locais e delivery",
        "APPCC a partir do telemóvel com registos prontos para inspeção"
      ]
    },
    "galleryTitle": "Como Funciona uma Pizzaria Autêntica",
    "gallerySubtitle": "O que vai coordenar com AI Chef Pro: massa, forno, técnica, ingredientes, pizzas e equipa. Imagens geradas com IA como referência visual do conceito.",
    "galleryImages": [
      "/lovable-uploads/ai-gallery/use-case-pizzero-hero.jpg",
      "/lovable-uploads/ai-gallery/use-case-pizzero-masa.jpg",
      "/lovable-uploads/ai-gallery/use-case-pizzero-horno.jpg",
      "/lovable-uploads/ai-gallery/use-case-pizzero-pizza.jpg",
      "/lovable-uploads/ai-gallery/use-case-pizzero-ingredients.jpg",
      "/lovable-uploads/ai-gallery/use-case-pizzero-team.jpg"
    ]
  },
  "panadero": {
    "h1": "IA para Padeiro Artesanal",
    "heroSubtitle": "Otimize massa mãe e pré-fermentos, calcule o custo por peça com custo hora de oficina, controle fermentações longas e a operação com uma suite de agentes de IA gastronómica especializados em padaria artesanal.",
    "heroTagline": "Padaria artesanal com técnica e margem real",
    "badge": "Para padeiros artesanais e oficinas",
    "painsTitle": "O Que um Padeiro Artesanal Não Pode Deixar de Resolver",
    "pains": [
      "Padronizar massa mãe, pré-fermentos (biga, poolish), hidratações e processos de fermentação longos em cada turno",
      "Calcular custo por peça com custo real incluindo horas de oficina (refresco, amassadura, modelagem, cozedura consomem tempo)",
      "Quebras em massas, pré-fermentos, sobras de modelagem e cozedura falhada",
      "Produção ajustada à procura diária sem sobreprodução nem rutura de stock antes do encerramento",
      "Diferenciar-se em zona concorrida com farinhas premium, cereais antigos e branding artesanal",
      "Captar encomendas de restauração local (restaurantes, cafetarias) com margem enquanto se gere a venda direta"
    ],
    "featuresTitle": "Como AI Chef Pro Ajuda um Padeiro",
    "features": [
      {
        "icon": "Wheat",
        "title": "Padaria Criativa",
        "description": "Agente especializado em padaria artesanal profissional: massas mãe, hidratações altas, técnica de modelagem e cozedura em forno de sola."
      },
      {
        "icon": "Beaker",
        "title": "Fermentus Con AI+",
        "description": "Para massas mãe líquidas e sólidas, pré-fermentos (biga, poolish), fermentações longas controladas em frio e técnica avançada."
      },
      {
        "icon": "Cake",
        "title": "Pastelaria Criativa",
        "description": "Para oficinas que combinam padaria com pastelaria e confeitaria: brioche, croissants, ensaimadas e pastelaria artesanal."
      },
      {
        "icon": "Calculator",
        "title": "Fichas de custo por peça com custo hora de oficina",
        "description": "Culinária Criativa entrega receita + ficha de custo CSV; Kit de Escandallos Pro gere com custo hora de oficina integrado na margem real por pão, baguete ou brioche."
      },
      {
        "icon": "CheckSquare",
        "title": "Kit de Tareas Obrador",
        "description": "Modelos: refresco de massa mãe, pré-fermentos, amassaduras, fermentações, modelagem, cozedura, montra e conservação."
      },
      {
        "icon": "ShieldCheck",
        "title": "Pack APPCC padaria",
        "description": "Rastreabilidade de farinhas, massa mãe, pré-fermentos, conservação e temperaturas críticas em câmara de fermentação."
      },
      {
        "icon": "Calendar",
        "title": "Gastro Calendar",
        "description": "Planeamento sazonal com datas-chave: Páscoa (bolos de Páscoa, folar), Natal (Bolo Rei, panetone), São João, eventos locais."
      },
      {
        "icon": "Image",
        "title": "GastroIMG Gen+ + Gerador de Pins Pinterest",
        "description": "Fotografia gastronómica IA de referência + Pinterest, onde a padaria artesanal captura tráfego orgânico estável."
      },
      {
        "icon": "BarChart3",
        "title": "MenuDish Local SEO",
        "description": "Captar clientes locais que procuram \"padaria artesanal perto\" no Google e Maps."
      }
    ],
    "workflowTitle": "Um Dia Real de um Padeiro com AI Chef Pro",
    "workflow": [
      "04:00 · Abertura — checklist Kit de Tareas Obrador: refresco da massa mãe, controlo das fermentações da noite, ligar o forno de sola.",
      "05:30 · Modelagem e cozedura — modelagem de pães, baguetes e brioche com modelos específicos, controlo de quebras de sobras.",
      "08:00 · Reposição da montra — primeira fornada pronta para venda direta e encomendas para restauração local.",
      "10:00 · Padaria Criativa — desenvolve um novo pão de cereais antigos com massa mãe líquida. Culinária Criativa entrega receita + ficha de custo CSV.",
      "11:00 · Fermentus Con AI+ — ajusta a hidratação a 80% e fermentação em frio de 24 horas para o novo pão.",
      "12:00 · Kit de Escandallos Pro — carrega o CSV com os seus preços reais de farinha biológica e custo hora de oficina, valida a margem.",
      "15:00 · GastroIMG Gen+ + Gerador de Pins Pinterest — gera a imagem de referência do novo pão e os pins para captar tráfego orgânico.",
      "20:00 · Encerramento — limpeza, APPCC assinado, preparação das massas para fermentação noturna."
    ],
    "productsTitle": "Modelos e Kits Recomendados para Padaria",
    "productIds": [
      "kit-tareas-pasteleria",
      "kit-escandallos",
      "pack-appcc",
      "kit-inventario",
      "kit-gestion-personal",
      "pro-prompts-ebook"
    ],
    "testimonialQuote": "Passámos de folhas soltas a sistema. Sabemos exatamente que peça rende e qual não, incluindo o custo hora de oficina. A quebra caiu 30% em 3 meses e descobrimos que dois pães históricos não eram rentáveis sem custo hora — redesenhámo-los simplificando o processo sem perder qualidade e subimos a margem 5 pontos.",
    "testimonialAuthor": "Ana Iglesias",
    "testimonialRole": "Padeira artesanal, oficina própria",
    "faqTitle": "Perguntas Frequentes de Padeiros",
    "faqs": [
      {
        "q": "Cobre técnica de massa mãe profissional?",
        "a": "Sim. Padaria Criativa e Fermentus raciocinam como padeiro profissional: refrescos com percentagem de inóculo, hidratações por tipo de pão, fermentações controladas em frio 24-48 horas, equilíbrio de estirpes. Não receitas do YouTube."
      },
      {
        "q": "Serve para oficina artesanal pequena ou industrial?",
        "a": "Para ambos. Os modelos escalam desde oficina familiar de 2 pessoas até produção industrial. A metodologia é a mesma: receita → ficha de custo CSV com custo hora de oficina → margem real."
      },
      {
        "q": "Cobre pastelaria e confeitaria além de padaria?",
        "a": "Sim. Pastelaria Criativa complementa o catálogo se fizer brioche, croissants, ensaimadas, pastelaria de Páscoa ou bolachas. Fermentus Con AI+ cobre a parte fermentada com técnica profissional."
      },
      {
        "q": "Gera conteúdo visual para montra, Instagram e Pinterest?",
        "a": "Sim. GastroIMG Gen+ gera imagens de referência profissionais do pão para montra, web e redes; Gerador de Pins Pinterest captura tráfego orgânico estável que a padaria artesanal aproveita muito. Lembre-se de que a imagem IA é de referência visual: a foto final é feita por si com o seu pão acabado de cozer."
      },
      {
        "q": "Como me ajuda com a sazonalidade e eventos?",
        "a": "Gastro Calendar planeia as épocas-chave (Páscoa com bolos de Páscoa e folar, Natal com Bolo Rei e panetone, São João, eventos locais) com antecedência. O Kit Plan Financiero projeta o cash flow sazonal realista."
      }
    ],
    "ctaTitle": "A sua padaria artesanal com margem clara e técnica profissional.",
    "ctaSubtitle": "Comece com o onboarding de 2 minutos. Plano Membro por 10 € por mês com 10.000 créditos para usar todos os agentes.",
    "seo": {
      "title": "IA para Padeiro Artesanal: Massa Mãe, Fichas de Custo e Técnica Profissional | AI Chef Pro",
      "description": "Suite de IA para padeiros artesanais: Padaria Criativa, Fermentus Con AI+ para massa mãe, fichas de custo por peça com custo hora de oficina. Comece hoje.",
      "keywords": "IA padeiro, padaria artesanal IA, massa mãe IA, software padaria, fichas de custo padaria, fermentus, biga poolish, padeiro profissional",
      "ogImage": "https://aichef.pro/og/use-cases/panadero.jpg"
    },
    "personalizationTitle": "Personalizado para a Sua Oficina desde o Minuto Um",
    "personalizationBody": "AI Chef Pro arranca com o agente «Quem Sou Eu?», um onboarding conversacional de 2 minutos em que conta que tipo de padaria opera (artesanal com massa mãe, padaria tradicional, oficina com pastelaria, padaria com cafetaria, padaria biológica), tamanho da equipa, cidade e especialidade. Cada agente —desde Padaria Criativa até Gastro Calendar— responde adaptado ao seu produto, mercado e operação real.",
    "appsTitle": "Os Agentes IA que Vai Usar na Sua Padaria",
    "apps": [
      {
        "name": "Padaria Criativa",
        "category": "Criatividade Culinária",
        "description": "Agente especializado em padaria artesanal profissional, massas mãe, hidratações e técnica."
      },
      {
        "name": "Fermentus Con AI+",
        "category": "Criatividade Culinária",
        "description": "Massas mãe, biga, poolish, hidratações altas e fermentações longas controladas."
      },
      {
        "name": "Pastelaria Criativa",
        "category": "Criatividade Culinária",
        "description": "Brioche, croissants, ensaimadas e pastelaria artesanal complementar."
      },
      {
        "name": "Culinária Criativa",
        "category": "Criatividade Culinária",
        "description": "Desenvolvimento de pães de autor com receita + ficha de custo CSV."
      },
      {
        "name": "Sosa Ingredients",
        "category": "Fornecedores Gastro",
        "description": "Catálogo Sosa: farinhas técnicas, melhoradores, sementes e cereais antigos."
      },
      {
        "name": "Mermas Genéricas",
        "category": "Ferramentas e Utilitários",
        "description": "Quebras em massa, pré-fermentos, sobras de modelagem e cozedura."
      },
      {
        "name": "ID Alergénios",
        "category": "Ferramentas e Utilitários",
        "description": "Identificação automática de alergénios por peça: glúten, lacticínios, frutos secos, ovo."
      },
      {
        "name": "GastroIMG Gen+",
        "category": "Conhecimento Gastro",
        "description": "Fotografia gastronómica IA de referência para montra, web e redes sociais."
      },
      {
        "name": "Gerador de Pins Pinterest",
        "category": "Conteúdos e Redes Sociais",
        "description": "O Pinterest captura tráfego orgânico estável para padaria artesanal."
      },
      {
        "name": "InstaFlow AI Pro",
        "category": "Conteúdos e Redes Sociais",
        "description": "Instagram com calendário editorial profissional para padaria de autor."
      },
      {
        "name": "MenuDish Local SEO",
        "category": "Conteúdos e Redes Sociais",
        "description": "Captar clientes locais que procuram \"padaria artesanal perto\" no Google e Maps."
      },
      {
        "name": "Gastro Calendar",
        "category": "Conteúdos e Redes Sociais",
        "description": "Planeamento sazonal: Páscoa, Natal, São João, eventos locais."
      }
    ],
    "metrics": [
      {
        "value": "+5 pp",
        "label": "margem após calcular custo por peça"
      },
      {
        "value": "−30 %",
        "label": "quebras na oficina e na cozedura"
      },
      {
        "value": "×2",
        "label": "tráfego orgânico via Pinterest"
      },
      {
        "value": "12+",
        "label": "agentes para a sua padaria"
      }
    ],
    "beforeAfter": {
      "beforeTitle": "Sem AI Chef Pro",
      "beforeItems": [
        "Massa mãe improvisada, fermentações inconsistentes turno a turno",
        "Fichas de custo sem custo hora de oficina, pães complexos com prejuízo sem saber",
        "Quebras em massas, pré-fermentos e cozedura sem rastreabilidade",
        "Montra e redes sociais improvisadas com fotos do telemóvel",
        "APPCC em papel impresso espalhado pela oficina"
      ],
      "afterTitle": "Com AI Chef Pro",
      "afterItems": [
        "Massa mãe com critério técnico: refrescos, hidratações e fermentações consistentes",
        "Ficha de custo profissional por peça com custo hora de oficina integrado",
        "Quebras controladas com Mermas Genéricas e modelos específicos",
        "Gerador de Pins Pinterest + InstaFlow + GastroIMG Gen+ captam tráfego estável",
        "APPCC a partir do telemóvel com registos prontos para inspeção"
      ]
    },
    "galleryTitle": "Como Funciona uma Padaria Artesanal",
    "gallerySubtitle": "O que vai coordenar com AI Chef Pro: montra, massa mãe, fermentação, pães, cozedura e equipa. Imagens geradas com IA como referência visual do conceito.",
    "galleryImages": [
      "/lovable-uploads/ai-gallery/use-case-panadero-hero.jpg",
      "/lovable-uploads/ai-gallery/use-case-panadero-masa.jpg",
      "/lovable-uploads/ai-gallery/use-case-panadero-fermentacion.jpg",
      "/lovable-uploads/ai-gallery/use-case-panadero-panes.jpg",
      "/lovable-uploads/ai-gallery/use-case-panadero-horneado.jpg",
      "/lovable-uploads/ai-gallery/use-case-panadero-team.jpg"
    ]
  },
  "chocolatero": {
    "h1": "IA para Chocolateiro e Bomboneiro",
    "heroSubtitle": "Desenha bombons, tabletes e coberturas com escandallo profissional, técnica de temperagem e planeamento sazonal com uma suite de agentes de IA especializados em chocolataria artesanal de autor.",
    "heroTagline": "Chocolataria com técnica autêntica e margem real",
    "badge": "Para chocolateiros, bomboneiros e mestres chocolateiros",
    "painsTitle": "O Que um Chocolateiro Não Pode Deixar de Resolver",
    "pains": [
      "Cacau com preço volátil que muda o custo real todas as semanas sem avisar e obriga a recalcular escandallos constantemente",
      "Técnica de temperagem exigente: cristalização em forma V, curvas precisas conforme cobertura, brilho e snap consistentes",
      "Mermas em obrador (temperagem falhada, recortes, moldes mal cuajados, abatimento) que sangram rentabilidade sem controlo",
      "Sazonalidade extrema: Natal, São Valentim, Páscoa e Bolo Rei concentram uma alta percentagem da faturação anual",
      "Diferenciar-se em zona concorrida com bombons de autor, packaging premium e storytelling visual de marca",
      "Captar pedidos corporativos, casamentos e eventos com margem enquanto se gere a produção diária"
    ],
    "featuresTitle": "Como AI Chef Pro Ajuda um Chocolateiro",
    "features": [
      {
        "icon": "Cookie",
        "title": "Chocolataria Criativa",
        "description": "Agente especializado em chocolataria profissional: bombons, ganaches, pralinés, tabletes, coberturas, técnica de temperagem e curvas de cristalização."
      },
      {
        "icon": "Cake",
        "title": "Pastelaria Criativa",
        "description": "Para sobremesas com chocolate, petiscos, brownies, mousses e combinações avançadas chocolate + pastelaria."
      },
      {
        "icon": "Calculator",
        "title": "Escandallos por peça com custo hora obrador",
        "description": "Culinária Criativa entrega receita + escandallo CSV; Kit de Escandallos Pro gere-o com custo hora obrador integrado em margem real por bombom e por caixa."
      },
      {
        "icon": "Beaker",
        "title": "Sosa Ingredients",
        "description": "Assistente do catálogo Sosa para coberturas técnicas, pastas concentradas, frutos secos e aromas profissionais."
      },
      {
        "icon": "CheckSquare",
        "title": "Kit de Tareas Chocolatería",
        "description": "Modelos: temperagem, moldagem, ganaches, montagem, packaging, controlo de temperaturas em câmara."
      },
      {
        "icon": "ShieldCheck",
        "title": "Pack APPCC chocolataria",
        "description": "Rastreabilidade de cacau, lacticínios, frutos secos, álcoois e conservação profissional com curvas documentadas."
      },
      {
        "icon": "Calendar",
        "title": "Gastro Calendar",
        "description": "Planeamento sazonal com datas-chave: Natal, São Valentim, Páscoa, Bolo Rei, Dia da Mãe. Calendário editorial."
      },
      {
        "icon": "Image",
        "title": "GastroIMG Gen+ + Gerador de Pins Pinterest",
        "description": "Fotografia de autor IA de referência + Pinterest, onde a chocolataria premium captura tráfego orgânico estável."
      },
      {
        "icon": "Sparkles",
        "title": "Mermas Genéricas",
        "description": "Dados precisos de mermas por processo (temperagem, moldagem, recortes, exposição) integrados em escandallo."
      }
    ],
    "workflowTitle": "Um Dia Real de um Chocolateiro com AI Chef Pro",
    "workflow": [
      "07:00 · Abertura — checklist Kit de Tareas Chocolatería: revisão de câmara, pré-cristalização de cobertura, preparação de moldes de policarbonato.",
      "08:30 · Chocolataria Criativa — desenvolve um novo bombom signature com praliné de avelã caramelizada e sal Maldon. Culinária Criativa entrega receita + escandallo CSV.",
      "09:30 · Sosa Ingredients — seleciona cobertura técnica com percentagem de cacau adequada, manteiga de cacau adicional e sal de qualidade.",
      "10:00 · Kit de Escandallos Pro — carrega o CSV com os seus preços reais de cacau e custo hora obrador integrado, valida margem por bombom e por caixa de 9 peças.",
      "11:00 · Produção do dia — temperagem em mármore, moldagem, ganache, enchimento, abatimento e desmoldagem.",
      "14:00 · Reposição — preparação de caixas oferta profissionais, etiquetagem e controlo de mermas.",
      "16:00 · Gastro Calendar — prepara o planeamento de Natal com caixas corporativas (antecedência de 8 semanas).",
      "18:00 · GastroIMG Gen+ + Gerador de Pins Pinterest — gera imagem de referência do novo signature e pins otimizados para Pinterest.",
      "20:00 · Encerramento — limpeza profunda, APPCC assinado, planeamento de misturas a abater."
    ],
    "productsTitle": "Modelos e Kits Recomendados para Chocolataria",
    "productIds": [
      "kit-tareas-chocolateria",
      "kit-escandallos",
      "pack-appcc",
      "kit-inventario",
      "kit-gestion-personal",
      "pro-prompts-ebook"
    ],
    "testimonialQuote": "Produzir 12 000 bombons para o Natal sem sistema era caos. Com Chocolataria Criativa para design, Sosa Ingredients para cobertura técnica, Kit de Escandallos Pro para margem real com cacau atualizado e Gastro Calendar para planeamento sazonal, salvámos a época e subimos a margem 7 pontos. As caixas corporativas fecham-se numa chamada com proposta profissional.",
    "testimonialAuthor": "Mónica Salazar",
    "testimonialRole": "Mestra chocolateira e proprietária",
    "faqTitle": "Perguntas Frequentes de Chocolateiros",
    "faqs": [
      {
        "q": "Cobre técnica de temperagem profissional e curvas de cristalização?",
        "a": "Sim. Chocolataria Criativa raciocina como chocolateiro profissional: temperagem de cobertura por curvas (45-27-31 °C para cobertura negra), técnica de tabling em mármore, semeação, micro-ondas com manteiga de cacau adicional. Não receitas do YouTube."
      },
      {
        "q": "Serve para chocolataria artesanal pequena, atelier de autor ou bombonaria com produção em escala?",
        "a": "Para as três. Os modelos escalam desde obrador familiar até produção para vários pontos de venda ou caixas corporativas com centenas de unidades."
      },
      {
        "q": "Como gerimos o preço volátil do cacau?",
        "a": "Kit de Escandallos Pro recalcula instantaneamente a margem real quando atualiza o preço da cobertura. Mermas Genéricas adiciona o custo de mermas por processo. A margem reflete sempre o custo atual."
      },
      {
        "q": "Gera conteúdo para montra, redes e packaging?",
        "a": "Sim. GastroIMG Gen+ gera imagens de referência profissionais de cada bombom para montra, web e redes; Gerador de Pins Pinterest + InstaFlow AI Pro programam conteúdo visual; MenuDish Local SEO captura clientes locais. Lembre-se de que a imagem IA é de referência visual: a foto definitiva é feita por si com o seu bombom empratado real."
      },
      {
        "q": "Como me ajuda com a sazonalidade forte?",
        "a": "Gastro Calendar planifica as épocas-chave (Natal, São Valentim, Páscoa, Bolo Rei, Dia da Mãe) com antecedência de 8-12 semanas. O Kit Plan Financiero projeta o cash flow sazonal realista para que chegue com produção e caixa a cada pico."
      }
    ],
    "ctaTitle": "A sua chocolataria com margem clara e técnica de autor.",
    "ctaSubtitle": "Comece com o onboarding de 2 minutos. Plano Membro por 10 € por mês com 10.000 créditos para usar todos os agentes.",
    "seo": {
      "title": "IA para Chocolateiro e Bomboneiro: Temperagem, Escandallos e Sazonalidade | AI Chef Pro",
      "description": "Suite de IA para chocolateiros profissionais: Chocolataria Criativa, escandallos por peça com custo hora obrador, planeamento sazonal e APPCC. Comece hoje.",
      "keywords": "IA chocolateiro, IA bomboneiro, software chocolataria, escandallos bombom, chocolataria artesanal IA, técnica temperagem, curvas cristalização, mestre chocolateiro",
      "ogImage": "https://aichef.pro/og/use-cases/chocolatero.jpg"
    },
    "personalizationTitle": "Personalizado ao Seu Atelier desde o Primeiro Minuto",
    "personalizationBody": "AI Chef Pro arranca com o agente «Quem Sou Eu?», um onboarding conversacional de 2 minutos em que lhe conta que tipo de chocolataria opera (atelier de autor, bombonaria com produção em escala, chocolataria com cafeteria, obrador para venda a hotelaria, chocolataria com experiências e degustações), tamanho da equipa, cidade e especialidade. Cada agente —desde Chocolataria Criativa até Gastro Calendar— responde adaptado ao seu produto, mercado e operativa real.",
    "appsTitle": "Os Agentes IA que Vai Usar no Seu Atelier",
    "apps": [
      {
        "name": "Chocolataria Criativa",
        "category": "Criatividade Culinária",
        "description": "Agente especializado em chocolataria profissional: bombons, ganaches, pralinés, tabletes e técnica de temperagem."
      },
      {
        "name": "Pastelaria Criativa",
        "category": "Criatividade Culinária",
        "description": "Sobremesas com chocolate, petiscos, brownies, mousses e combinações avançadas."
      },
      {
        "name": "Culinária Criativa",
        "category": "Criatividade Culinária",
        "description": "Desenvolvimento de bombons signature com receita + escandallo CSV."
      },
      {
        "name": "Sosa Ingredients",
        "category": "Fornecedores Gastro",
        "description": "Catálogo Sosa: coberturas técnicas, pastas concentradas, frutos secos e aromas profissionais."
      },
      {
        "name": "tSpoonLab Agent",
        "category": "Fornecedores Gastro",
        "description": "Assistente do catálogo tSpoonLab para aplicações avançadas de chocolataria."
      },
      {
        "name": "Mermas Genéricas",
        "category": "Ferramentas e Utilitários",
        "description": "Mermas em temperagem, moldagem, recortes e exposição integradas em escandallo."
      },
      {
        "name": "ID Alergénios",
        "category": "Ferramentas e Utilitários",
        "description": "Identificação automática de alergénios por bombom: lacticínios, frutos secos, glúten, álcoois."
      },
      {
        "name": "GastroIMG Gen+",
        "category": "Conhecimento Gastro",
        "description": "Fotografia de autor IA de referência para montra, web, packaging e redes."
      },
      {
        "name": "Gerador de Pins Pinterest",
        "category": "Conteúdos e Redes Sociais",
        "description": "Pinterest captura tráfego orgânico estável para chocolataria premium."
      },
      {
        "name": "InstaFlow AI Pro",
        "category": "Conteúdos e Redes Sociais",
        "description": "Instagram com calendário editorial para chocolataria de autor."
      },
      {
        "name": "MenuDish Local SEO",
        "category": "Conteúdos e Redes Sociais",
        "description": "Captar clientes locais que procuram \"chocolataria artesanal perto\" no Google e Maps."
      },
      {
        "name": "Gastro Calendar",
        "category": "Conteúdos e Redes Sociais",
        "description": "Planeamento sazonal: Natal, São Valentim, Páscoa, Bolo Rei, Dia da Mãe."
      }
    ],
    "metrics": [
      {
        "value": "+7 pp",
        "label": "margem após escandallar bombons"
      },
      {
        "value": "−35 %",
        "label": "mermas em obrador e montra"
      },
      {
        "value": "×2",
        "label": "pedidos corporativos Natal"
      },
      {
        "value": "12+",
        "label": "agentes para o seu atelier"
      }
    ],
    "beforeAfter": {
      "beforeTitle": "Sem AI Chef Pro",
      "beforeItems": [
        "Temperagem improvisada: brilho e snap inconsistentes peça a peça",
        "Cacau volátil que desequilibra os preços sem recalcular em tempo real",
        "Mermas em temperagem, moldagem e montra sem rastreabilidade real",
        "Produção sazonal reativa: chega tarde ao Natal e perde pedidos corporativos",
        "APPCC em papel impresso disperso pelo atelier"
      ],
      "afterTitle": "Com AI Chef Pro",
      "afterItems": [
        "Temperagem por curvas com critério técnico, brilho e snap consistentes",
        "Escandallo profissional por bombom com cacau atualizável e custo hora integrado",
        "Mermas controladas com Mermas Genéricas e modelos específicos",
        "Gerador de Pins Pinterest + InstaFlow + GastroIMG Gen+ captam tráfego estável e pedidos",
        "APPCC desde o telemóvel com registos prontos para inspeção"
      ]
    },
    "galleryTitle": "Como Funciona um Atelier de Chocolataria",
    "gallerySubtitle": "O que vai coordenar com AI Chef Pro: temperagem, moldagem, bombons, ganache e equipamento. Imagens geradas com IA como referência visual do conceito.",
    "galleryImages": [
      "/lovable-uploads/ai-gallery/use-case-chocolatero-hero.jpg",
      "/lovable-uploads/ai-gallery/use-case-chocolatero-temperado.jpg",
      "/lovable-uploads/ai-gallery/use-case-chocolatero-bombones.jpg",
      "/lovable-uploads/ai-gallery/use-case-chocolatero-moldeado.jpg",
      "/lovable-uploads/ai-gallery/use-case-chocolatero-ganache.jpg",
      "/lovable-uploads/ai-gallery/use-case-chocolatero-team.jpg"
    ]
  },
  "chef-privado-personal": {
    "h1": "IA para Chef Privado e Personal Chef",
    "heroSubtitle": "Desenha menus personalizados para clientes únicos, calcule o custo real de cada jantar privado, planifica mise en casas particulares e capta branding profissional com uma suite de agentes de IA gastronómica especializados em chef privado e serviço em casas particulares.",
    "heroTagline": "Serviço privado com margem real e técnica de autor",
    "badge": "Para chefs privados, personal chefs e catering íntimo",
    "painsTitle": "O Que um Chef Privado Não Pode Deixar de Resolver",
    "pains": [
      "Desenhar menus totalmente personalizados por cliente: alergias, intolerâncias, preferências, dieta, ocasião e estética do empratado",
      "Calcular o custo de cada jantar privado com custo real (compra do dia, ingredientes premium) e preço personalizado",
      "Planificar mise em casas particulares com cozinhas não profissionais (sem equipamento, espaço limitado, fogões desconhecidos)",
      "Padronizar fichas técnicas para que o cliente possa repetir o menu ou preservar a receita como recordação",
      "Diferenciar-se em zona concorrida com storytelling pessoal, branding visual de autor e captação por redes",
      "Captar clientes premium recorrentes (famílias VIP, executivos, celebridades) com propostas profissionais e personalizadas"
    ],
    "featuresTitle": "Como AI Chef Pro Ajuda um Chef Privado",
    "features": [
      {
        "icon": "ChefHat",
        "title": "Chef Privado Pro",
        "description": "Agente especializado do catálogo Gastro Profile Pro: raciocina como personal chef profissional com experiência em casas particulares e eventos íntimos."
      },
      {
        "icon": "Sparkles",
        "title": "Culinária Criativa",
        "description": "Para desenvolvimento de menus personalizados com técnica avançada: empratados de autor, fusões controladas, sobremesas de assinatura."
      },
      {
        "icon": "Wine",
        "title": "Food Pairing AI",
        "description": "Maridagens personalizadas com a adega do cliente ou propostas de vinhos para cada prato do menu privado."
      },
      {
        "icon": "Calculator",
        "title": "Calcula Pax + Cálculo de Custos",
        "description": "Calcula Pax escala receitas para 2, 6, 12 comensais; Kit de Escandallos Pro gere-o com custo real por jantar privado e preço personalizado."
      },
      {
        "icon": "CheckSquare",
        "title": "Kit de Tareas Chef Privado",
        "description": "Modelos: pré-visita à cozinha do cliente, lista de compras, mise transportável, plano de serviço, limpeza, fatura."
      },
      {
        "icon": "ShieldCheck",
        "title": "ID Alergénios",
        "description": "Identificação automática de alergénios por cliente: crítico quando trabalha com famílias com intolerâncias específicas."
      },
      {
        "icon": "Calendar",
        "title": "Gastro Calendar",
        "description": "Planeamento de menus sazonais e para datas especiais: Natal, Dia dos Namorados, aniversários, aniversários."
      },
      {
        "icon": "Image",
        "title": "GastroIMG Gen+ + InstaFlow AI Pro",
        "description": "Fotografia premium IA de referência + Instagram para captar novos clientes e construir reputação de autor."
      },
      {
        "icon": "BookOpen",
        "title": "Ficha técnica + fatura",
        "description": "Modelo profissional para entregar ao cliente: ficha técnica do menu com receita + storytelling + fatura clara."
      }
    ],
    "workflowTitle": "Um Dia Real de um Chef Privado com AI Chef Pro",
    "workflow": [
      "07:00 · Pré-visita — checklist Kit de Tareas Chef Privado: revisão da cozinha do cliente (equipamentos, espaço, alergias e preferências confirmadas).",
      "08:00 · Chef Privado Pro — desenvolve o menu personalizado para jantar íntimo de 6 pax com alergia a frutos secos. Culinária Criativa entrega receita + escandallos CSV.",
      "09:00 · Calcula Pax — escala as receitas de 6 para 8 comensais (cliente adicionou dois convidados). Kit de Escandallos Pro recalcula custo e proposta.",
      "10:00 · Lista de compras — vai ao mercado com a lista priorizada: produto do dia, ingredientes premium específicos.",
      "14:00 · Chegada a casa do cliente — montagem de mise em cozinha particular seguindo o plano transportável, organização do espaço.",
      "17:00 · Serviço de jantar — execução do menu com técnica profissional adaptada à cozinha do cliente, empratado em porcelana fina.",
      "21:00 · Fecho com cliente — entrega de ficha técnica do menu com storytelling + fatura profissional + foto de referência do menu.",
      "23:00 · Pós-jantar — InstaFlow AI Pro: post de Instagram com a imagem de referência do menu (sem caras do cliente) para construir reputação."
    ],
    "productsTitle": "Modelos e Kits Recomendados para Chef Privado",
    "productIds": [
      "kit-tareas-chef-privado",
      "kit-escandallos",
      "pack-appcc",
      "pro-prompts-ebook",
      "kit-inventario"
    ],
    "testimonialQuote": "Chef Privado Pro mudou a minha proposta comercial. Agora cada cliente recebe um menu personalizado com cálculo de custos profissional e storytelling, e a captação por Instagram com GastroIMG Gen+ multiplicou-se. Fecho propostas numa chamada porque entrego ficha técnica + fatura no mesmo dia. Aumentámos o ticket médio em 35% por jantar.",
    "testimonialAuthor": "Andrea Gómez",
    "testimonialRole": "Chef privada freelance, Madrid + costa",
    "faqTitle": "Perguntas Frequentes de Chefs Privados",
    "faqs": [
      {
        "q": "Serve para chef privado freelance, agência de personal chef ou catering íntimo?",
        "a": "Para os três. Chef Privado Pro raciocina como personal chef profissional, serve tanto para freelance que desenha a sua proposta como para agências com vários chefs."
      },
      {
        "q": "Como gere alergias e dietas especiais por cliente?",
        "a": "ID Alergénios identifica automaticamente alergénios por receita. Chef Privado Pro raciocina em chave de personalização: dietas keto, vegan, sem glúten, baixa em sódio, FODMAP, gravidez. Cada cliente recebe um menu adaptado real."
      },
      {
        "q": "Como escala receitas para diferentes números de comensais?",
        "a": "Calcula Pax escala as receitas para 2, 6, 12 ou qualquer número de comensais sem perder precisão. Kit de Escandallos Pro recalcula o custo por pessoa e a proposta económica ao cliente."
      },
      {
        "q": "Gera conteúdo visual para Instagram e reputação de autor?",
        "a": "Sim. GastroIMG Gen+ gera imagens de referência profissionais do menu (sem mostrar o cliente) para Instagram, web e portefólio. Lembre-se que a imagem IA é de referência visual: a foto definitiva é feita por si com o seu prato empratado real em cada jantar."
      },
      {
        "q": "Como me ajuda com a captação de clientes recorrentes?",
        "a": "GastroIMG Gen+ + InstaFlow AI Pro constroem conteúdo visual constante; MenuDish Local SEO capta clientes locais que procuram \"chef privado em [cidade]\"; Gastro Calendar ajuda a propor menus sazonais (Natal íntimo, Dia dos Namorados, aniversários) para fidelizar."
      }
    ],
    "ctaTitle": "O seu serviço de chef privado com margem real e proposta de autor.",
    "ctaSubtitle": "Comece com o onboarding de 2 minutos. Plano Membro por 10 € por mês com 10.000 créditos para usar todos os agentes.",
    "seo": {
      "title": "IA para Chef Privado e Personal Chef: Menus, Cálculo de Custos e Serviço | AI Chef Pro",
      "description": "Suite de IA para chefs privados profissionais: Chef Privado Pro, cálculos de custos por jantar, menus personalizados, branding e captação. Comece hoje.",
      "keywords": "IA chef privado, IA personal chef, software chef privado, cálculo de custos jantar privado, chef privado madrid, personal chef freelance",
      "ogImage": "https://aichef.pro/og/use-cases/chef-privado.jpg"
    },
    "personalizationTitle": "Personalizado ao Seu Serviço de Chef Privado desde o Minuto Um",
    "personalizationBody": "AI Chef Pro arranca com o agente «Quem Sou Eu?», um onboarding conversacional de 2 minutos no qual conta que tipo de serviço opera (chef privado freelance, agência com vários chefs, catering íntimo de casamentos e eventos privados, chef de iates), tipo de clientela (famílias VIP, executivos, celebridades), cidade e especialidade. Cada agente — desde Chef Privado Pro até Gastro Calendar — responde adaptado à sua proposta e operativa real.",
    "appsTitle": "Os Agentes IA que Vai Usar como Chef Privado",
    "apps": [
      {
        "name": "Chef Privado Pro",
        "category": "Gastro Profile Pro",
        "description": "Agente especializado do catálogo Gastro Profile Pro: raciocina como personal chef profissional."
      },
      {
        "name": "Culinária Criativa",
        "category": "Criatividade Culinária",
        "description": "Desenvolvimento de menus personalizados com técnica avançada e receita + cálculo de custos CSV."
      },
      {
        "name": "Food Pairing AI",
        "category": "Criatividade Culinária",
        "description": "Maridagens personalizadas com a adega do cliente ou propostas de vinhos."
      },
      {
        "name": "Calcula Pax",
        "category": "Ferramentas e Utilitários",
        "description": "Escalamento de receitas para diferentes números de comensais."
      },
      {
        "name": "ID Alergénios",
        "category": "Ferramentas e Utilitários",
        "description": "Identificação automática de alergénios por cliente e receita."
      },
      {
        "name": "Conversor Ing",
        "category": "Ferramentas e Utilitários",
        "description": "Conversor de pesos e medidas, crítico ao trabalhar com cozinhas não profissionais."
      },
      {
        "name": "Mermas Genéricas",
        "category": "Ferramentas e Utilitários",
        "description": "Mermas em compra do dia e produto premium."
      },
      {
        "name": "GastroIMG Gen+",
        "category": "Conhecimento Gastronómico",
        "description": "Fotografia premium IA de referência para Instagram, portefólio e captação."
      },
      {
        "name": "InstaFlow AI Pro",
        "category": "Conteúdos e Redes Sociais",
        "description": "Instagram com calendário editorial profissional para captar clientes recorrentes."
      },
      {
        "name": "MenuDish Local SEO",
        "category": "Conteúdos e Redes Sociais",
        "description": "Captar clientes locais que procuram \"chef privado em [cidade]\" no Google e Maps."
      },
      {
        "name": "Gastro Calendar",
        "category": "Conteúdos e Redes Sociais",
        "description": "Menus sazonais: Natal íntimo, Dia dos Namorados, aniversários, aniversários."
      },
      {
        "name": "Bar & Lounge AI+",
        "category": "Conceitos de Negócio",
        "description": "Para coquetelaria personalizada em jantares privados."
      }
    ],
    "metrics": [
      {
        "value": "+35 %",
        "label": "ticket médio por jantar privado"
      },
      {
        "value": "×3",
        "label": "captação de clientes via Instagram"
      },
      {
        "value": "×5",
        "label": "velocidade de propostas comerciais"
      },
      {
        "value": "12+",
        "label": "agentes para o seu serviço privado"
      }
    ],
    "beforeAfter": {
      "beforeTitle": "Sem AI Chef Pro",
      "beforeItems": [
        "Menus personalizados à mão: uma semana por proposta",
        "Cálculos de custos sem custo real, propostas comerciais com margem incerta",
        "Pré-visita e mise em casa improvisada todas as vezes",
        "Captação por boca a boca, sem Instagram constante",
        "Sem ficha técnica para entregar ao cliente como recordação"
      ],
      "afterTitle": "Com AI Chef Pro",
      "afterItems": [
        "Menu personalizado em uma hora com Chef Privado Pro",
        "Cálculo de custos profissional por jantar com margem validada",
        "Pré-visita e mise com modelo transportável Kit de Tareas",
        "Captação constante com GastroIMG Gen+ + InstaFlow AI Pro",
        "Ficha técnica do menu + fatura entregue no mesmo dia"
      ]
    },
    "galleryTitle": "Como Funciona o Serviço de Chef Privado",
    "gallerySubtitle": "O que vai coordenar com AI Chef Pro: mise, prato empratado, mesa posta, despensa e serviço. Imagens geradas com IA como referência visual do conceito.",
    "galleryImages": [
      "/lovable-uploads/ai-gallery/use-case-chef-privado-hero.jpg",
      "/lovable-uploads/ai-gallery/use-case-chef-privado-mise.jpg",
      "/lovable-uploads/ai-gallery/use-case-chef-privado-plato.jpg",
      "/lovable-uploads/ai-gallery/use-case-chef-privado-mesa.jpg",
      "/lovable-uploads/ai-gallery/use-case-chef-privado-despensa.jpg",
      "/lovable-uploads/ai-gallery/use-case-chef-privado-team.jpg"
    ]
  },
  "fb-manager-hotel": {
    "h1": "IA para F&B Manager de Hotel",
    "heroSubtitle": "Coordene restaurantes, banquetes, room service, breakfast buffet e bares de hotel com escandallo cruzado, modelos operativos profissionais e branding integrado com uma suite de agentes de IA gastronómica especializados em gestão integral F&B hoteleira.",
    "heroTagline": "F&B hoteleiro com margem real e operativa profissional",
    "badge": "Para F&B Managers, Diretores de Alimentos e Bebidas",
    "painsTitle": "O Que um F&B Manager Não Pode Deixar de Resolver",
    "pains": [
      "Coordenar vários outlets simultâneos (restaurante principal, room service, breakfast buffet, bar da piscina, banquetes, cafetaria)",
      "Escandallar carta cruzada entre outlets mantendo coerência de food cost e margem integrada",
      "Mermas Genéricas elevadas no breakfast buffet (oferta abundante com consumo variável) e em banquetes (volume alto, complexidade logística)",
      "Padronizar procedimentos por turno com equipas rotativas e três serviços diários",
      "Diferenciar-se num hotel concorrido com experiência gastronómica integral, branding visual e storytelling de hospitalidade",
      "Captar eventos corporativos, casamentos e banquetes premium com propostas profissionais e margem validada"
    ],
    "featuresTitle": "Como o AI Chef Pro Ajuda um F&B Manager",
    "features": [
      {
        "icon": "Hotel",
        "title": "Gerente Restaurante Pro",
        "description": "Agente especializado do catálogo Gastro Profile Pro adaptado à gestão F&B hoteleira multi-outlet."
      },
      {
        "icon": "PartyPopper",
        "title": "Catering AI+",
        "description": "Aconselhamento profissional para banquetes, casamentos e eventos corporativos do hotel."
      },
      {
        "icon": "Sparkles",
        "title": "Culinária Criativa",
        "description": "Para desenvolvimento de cartas integradas: restaurante principal, breakfast buffet, room service e bar da piscina com coerência."
      },
      {
        "icon": "Wine",
        "title": "Bar & Lounge AI+",
        "description": "Para a cocktailaria do bar da piscina, lobby bar e harmonizações do restaurante principal."
      },
      {
        "icon": "Calculator",
        "title": "Escandallos cruzados",
        "description": "Culinária Criativa entrega receita + escandallo CSV; Kit de Escandallos Pro gere-o com custo cruzado entre outlets e margem integrada."
      },
      {
        "icon": "CheckSquare",
        "title": "Kit de Tareas Hotel Completo",
        "description": "Modelos para 5 outlets: restaurante, breakfast, room service, bar, banquetes com procedimentos por turno."
      },
      {
        "icon": "ShieldCheck",
        "title": "Pack APPCC hoteleiro",
        "description": "Rastreabilidade de buffet, banquetes, room service e bar com temperaturas críticas e conservação."
      },
      {
        "icon": "Calendar",
        "title": "Gastro Calendar",
        "description": "Planeamento de eventos corporativos, casamentos, épocas (verão/inverno), Natal, São Valentim, conferências."
      },
      {
        "icon": "Image",
        "title": "GastroIMG Gen+ + InstaFlow AI Pro",
        "description": "Fotografia premium IA de referência + Instagram para todos os outlets do hotel com coerência de marca."
      }
    ],
    "workflowTitle": "Um Dia Real de um F&B Manager com AI Chef Pro",
    "workflow": [
      "06:00 · Abertura do breakfast — checklist Kit de Tareas Hotel: preparação do buffet, controlo de chafing dishes, temperaturas, mise da estação de ovos.",
      "09:00 · Coordenação com a cozinha principal — Culinária Criativa atualiza a carta de almoço com produto da época. Receita + escandallo CSV.",
      "10:00 · Catering AI+ — desenvolve a proposta de menu para casamento de 120 pax com três tempos. Calcula Pax escala as receitas, Kit de Escandallos Pro valida custo e margem.",
      "12:00 · Serviço de almoço no restaurante principal + room service — coordenação cruzada entre outlets.",
      "14:00 · Bar & Lounge AI+ — desenvolve a nova carta de cocktails para o bar da piscina na época de verão.",
      "17:00 · Banquete corporativo de 80 pax — execução com modelo específico do Kit de Tareas.",
      "20:00 · GastroIMG Gen+ + InstaFlow AI Pro — gera imagens de referência para os quatro outlets e os posts coerentes para o Instagram do hotel.",
      "23:00 · Encerramento — limpeza profunda multi-outlet, APPCC assinado, planeamento do breakfast e serviços do dia seguinte."
    ],
    "productsTitle": "Modelos e Kits Recomendados para F&B Manager",
    "productIds": [
      "kit-tareas-hotel",
      "kit-escandallos",
      "pack-appcc",
      "kit-inventario",
      "kit-gestion-personal",
      "pro-prompts-ebook"
    ],
    "testimonialQuote": "Gerir cinco outlets sem sistema era caos. Gerente Restaurante Pro + Catering AI+ coordenam-nos carta cruzada, banquetes e room service com escandallo integrado. O planeamento de casamentos de 120 pax que antes era uma semana agora é um dia com proposta profissional. Subimos a margem 5 pontos cruzando outlets e fechámos eventos premium com muito mais velocidade.",
    "testimonialAuthor": "Roberto Castaño",
    "testimonialRole": "Diretor de F&B, hotel 5 estrelas",
    "faqTitle": "Perguntas Frequentes de F&B Managers",
    "faqs": [
      {
        "q": "Serve para hotel boutique, hotel de cadeia, all-inclusive ou hotel de luxo?",
        "a": "Para os quatro. Gerente Restaurante Pro + Catering AI+ + Bar & Lounge AI+ cobrem desde hotel boutique com um restaurante até hotel 5 estrelas com 5+ outlets, all-inclusive com buffet massivo ou resort de férias."
      },
      {
        "q": "Como coordeno a carta cruzada entre outlets?",
        "a": "Culinária Criativa raciocina com coerência entre outlets: produto do menu principal aproveitado no breakfast, no room service e em banquetes, otimizando food cost integrado e reduzindo mermas cruzadas."
      },
      {
        "q": "Como escalo escandallos para banquetes de 50, 100 ou 300 pax?",
        "a": "Calcula Pax escala as receitas sem perder precisão; Kit de Escandallos Pro recalcula o custo por pax e a proposta económica ao cliente corporativo ou de casamentos."
      },
      {
        "q": "Gera conteúdo visual coerente para o Instagram do hotel?",
        "a": "Sim. GastroIMG Gen+ gera imagens de referência profissionais para os quatro outlets com coerência de marca; InstaFlow AI Pro programa o Instagram. Lembre-se de que a imagem IA é de referência visual: a foto definitiva é feita por si com o seu prato empratado real."
      },
      {
        "q": "Como me ajuda com eventos corporativos e épocas?",
        "a": "Gastro Calendar planeia eventos corporativos, casamentos, conferências, épocas (verão/inverno), Natal e São Valentim com menus específicos por outlet e calendário editorial coordenado."
      }
    ],
    "ctaTitle": "O seu F&B hoteleiro com margem integrada e operativa profissional.",
    "ctaSubtitle": "Comece com o onboarding de 2 minutos. Plano Membro por 10 € por mês com 10.000 créditos para usar todos os agentes.",
    "seo": {
      "title": "IA para F&B Manager de Hotel: Multi-outlet, Banquetes e Escandallos | AI Chef Pro",
      "description": "Suite de IA para F&B Managers de hotel: Gerente Pro, Catering AI+, escandallos cruzados, branding multi-outlet e APPCC integrado. Comece hoje.",
      "keywords": "IA F&B manager, IA hotel F&B, software hotel restaurante, escandallos hotel, banquetes hotel IA, breakfast buffet hotel",
      "ogImage": "https://aichef.pro/og/use-cases/fb-manager-hotel.jpg"
    },
    "personalizationTitle": "Personalizado para o Seu Hotel desde o Primeiro Minuto",
    "personalizationBody": "O AI Chef Pro arranca com o agente «Quem Sou Eu?», um onboarding conversacional de 2 minutos em que lhe conta que tipo de hotel opera (boutique, cadeia, 5 estrelas, all-inclusive, resort de férias), número de outlets F&B, dimensão da equipa e especialidade. Cada agente —desde Gerente Restaurante Pro até Catering AI+— responde adaptado ao seu hotel real.",
    "appsTitle": "Os Agentes IA que Vai Usar como F&B Manager",
    "apps": [
      {
        "name": "Gerente Restaurante Pro",
        "category": "Gastro Profile Pro",
        "description": "Agente especializado adaptado à gestão F&B hoteleira multi-outlet."
      },
      {
        "name": "Catering AI+",
        "category": "Conceitos de Negócio",
        "description": "Banquetes, casamentos e eventos corporativos do hotel com propostas profissionais."
      },
      {
        "name": "Culinária Criativa",
        "category": "Criatividade Culinária",
        "description": "Cartas integradas com coerência entre outlets e receita + escandallo CSV."
      },
      {
        "name": "Bar & Lounge AI+",
        "category": "Conceitos de Negócio",
        "description": "Para cocktailaria do bar da piscina, lobby bar e harmonizações do restaurante principal."
      },
      {
        "name": "Restaurantes Casuais AI+",
        "category": "Conceitos de Negócio",
        "description": "Para o restaurante casual e a cafetaria do hotel."
      },
      {
        "name": "Calcula Pax",
        "category": "Ferramentas e Utilitários",
        "description": "Escalamento de receitas para banquetes de 50, 100, 300 ou 500 pax."
      },
      {
        "name": "Mermas Genéricas",
        "category": "Ferramentas e Utilitários",
        "description": "Mermas no breakfast buffet, banquetes e room service."
      },
      {
        "name": "ID Alergénios",
        "category": "Ferramentas e Utilitários",
        "description": "Identificação automática para clientes com alergias em banquetes."
      },
      {
        "name": "GastroIMG Gen+",
        "category": "Gastro Conhecimento",
        "description": "Fotografia premium IA de referência com coerência de marca para todos os outlets."
      },
      {
        "name": "InstaFlow AI Pro",
        "category": "Conteúdos e Redes Sociais",
        "description": "Instagram com calendário editorial coordenado para todos os outlets."
      },
      {
        "name": "MenuDish Local SEO",
        "category": "Conteúdos e Redes Sociais",
        "description": "Captar clientes locais que procuram \"restaurante hotel\" no Google e Maps."
      },
      {
        "name": "Gastro Calendar",
        "category": "Conteúdos e Redes Sociais",
        "description": "Eventos corporativos, casamentos, conferências, Natal, São Valentim, épocas."
      }
    ],
    "metrics": [
      {
        "value": "+5 pp",
        "label": "margem após escandallar cruzado"
      },
      {
        "value": "×7",
        "label": "velocidade de propostas de banquete"
      },
      {
        "value": "−25 %",
        "label": "mermas no breakfast buffet"
      },
      {
        "value": "12+",
        "label": "agentes para o seu F&B"
      }
    ],
    "beforeAfter": {
      "beforeTitle": "Sem AI Chef Pro",
      "beforeItems": [
        "Outlets coordenados manualmente, food cost cruzado sem rastreabilidade",
        "Banquetes escandallados à mão: uma semana por casamento",
        "Mermas no breakfast buffet sem controlo real",
        "Branding visual disperso entre outlets sem coerência",
        "APPCC em papel impresso disperso pelos outlets"
      ],
      "afterTitle": "Com AI Chef Pro",
      "afterItems": [
        "Outlets coordenados com escandallo cruzado e food cost integrado",
        "Banquetes escandallados em um dia com proposta profissional",
        "Mermas controladas com Mermas Genéricas no breakfast e banquetes",
        "Branding coerente com GastroIMG Gen+ + InstaFlow AI Pro",
        "APPCC a partir do telemóvel multi-outlet com registos prontos para inspeção"
      ]
    },
    "galleryTitle": "Como Funciona o F&B de um Hotel",
    "gallerySubtitle": "O que vai coordenar com AI Chef Pro: restaurante, banquetes, breakfast, room service e bar da piscina. Imagens geradas com IA como referência visual do conceito.",
    "galleryImages": [
      "/lovable-uploads/ai-gallery/use-case-fb-manager-hero.jpg",
      "/lovable-uploads/ai-gallery/use-case-fb-manager-banquet.jpg",
      "/lovable-uploads/ai-gallery/use-case-fb-manager-breakfast.jpg",
      "/lovable-uploads/ai-gallery/use-case-fb-manager-roomservice.jpg",
      "/lovable-uploads/ai-gallery/use-case-fb-manager-bar.jpg",
      "/lovable-uploads/ai-gallery/use-case-fb-manager-team.jpg"
    ]
  },
  "maitre-jefe-sala": {
    "h1": "IA para Maître e Chefe de Sala",
    "heroSubtitle": "Coordene o serviço de sala com técnica profissional, gerencie reservas premium e harmonizações, lidere a equipa e capture branding fine dining com uma suite de agentes de IA gastronómica especializados em sala e serviço de alto nível.",
    "heroTagline": "Sala com técnica profissional e experiência memorável",
    "badge": "Para maîtres, chefes de sala e diretores de serviço",
    "painsTitle": "O Que um Maître Não Pode Deixar de Resolver",
    "pains": [
      "Coordenar o serviço de sala com sequência perfeita de passes, gueridon, decantação e serviço profissional turno a turno",
      "Gerir reservas premium com planeamento de mesas, alergias, ocasiões especiais e preferências de cliente recorrente",
      "Liderar a equipa de sala com formação constante em harmonizações, cutelaria, descrição de pratos e storytelling",
      "Coordenar com a cozinha passe a passe com timing perfeito e comunicação fluida em picos de serviço",
      "Diferenciar-se em restaurante competitivo com experiência memorável, branding visual fine dining e captação de clientes recorrentes",
      "Captar eventos privados e jantares corporativos com propostas profissionais de serviço e harmonização"
    ],
    "featuresTitle": "Como o AI Chef Pro Ajuda um Maître",
    "features": [
      {
        "icon": "Crown",
        "title": "Gerente Restaurante Pro",
        "description": "Agente especializado adaptado à gestão de sala fine dining: sequência de serviço, gueridon, decantação, formação de equipa."
      },
      {
        "icon": "Wine",
        "title": "Bar & Lounge AI+",
        "description": "Para gestão profissional da adega, decantações, recomendações de vinho e coquetelaria profissional."
      },
      {
        "icon": "Sparkles",
        "title": "Food Pairing AI",
        "description": "Harmonizações com base científica para cada prato do menu, fundamentação profissional para a equipa de sala."
      },
      {
        "icon": "Calculator",
        "title": "Calcula Pax + Mise",
        "description": "Calcula Pax para banquetes, modelos de mise de mesa, gueridon, sequência de passes."
      },
      {
        "icon": "CheckSquare",
        "title": "Kit de Tareas Restaurante",
        "description": "Modelos: pré-serviço (mise), turno de serviço (passes), pós-serviço (fecho, limpeza), formação de equipa."
      },
      {
        "icon": "ShieldCheck",
        "title": "Pack APPCC sala",
        "description": "Rastreabilidade da adega, conservação de vinhos, decantações e temperaturas de serviço."
      },
      {
        "icon": "Calendar",
        "title": "Gastro Calendar",
        "description": "Reservas premium, eventos privados, jantares corporativos, Natal, São Valentim, aniversários."
      },
      {
        "icon": "Image",
        "title": "GastroIMG Gen+ + InstaFlow AI Pro",
        "description": "Fotografia elegante IA de referência + Instagram com storytelling de serviço e harmonizações para captar clientes premium."
      },
      {
        "icon": "BookOpen",
        "title": "Storytelling de menu",
        "description": "Geração de descrições de pratos e harmonizações para a equipa de sala recitar com profissionalismo perante o cliente."
      }
    ],
    "workflowTitle": "Um Dia Real de um Maître com AI Chef Pro",
    "workflow": [
      "15:00 · Abertura — checklist Kit de Tareas: revisão das reservas do dia, mise de mesas, polimento de cristalaria e cutelaria, controlo da adega.",
      "16:00 · Briefing à equipa — explicação dos novos pratos do dia com storytelling gerado e harmonizações validadas com Food Pairing AI.",
      "17:00 · Coordenação com a cozinha — verificação de alterações na carta, alergias confirmadas, mise de passes.",
      "18:30 · Receção das primeiras reservas — atendimento profissional, serviço de aperitivos, descrição da carta.",
      "20:00 · Serviço de jantar — coordenação passe a passe com a cozinha, decantações profissionais, gueridon na mesa quando aplicável.",
      "22:00 · Jantares corporativos privados — atenção dedicada a evento de 12 pax com menu de degustação e harmonizações.",
      "00:00 · Encerramento — fecho, despedida da equipa, GastroIMG Gen+ gera imagem de referência do menu de degustação + InstaFlow programa o post.",
      "01:00 · Briefing de encerramento — feedback da equipa, anotação de comentários de clientes, planeamento do dia seguinte."
    ],
    "productsTitle": "Modelos e Kits Recomendados para Maître",
    "productIds": [
      "kit-tareas",
      "kit-escandallos",
      "pack-appcc",
      "kit-gestion-personal",
      "pro-prompts-ebook",
      "kit-inventario"
    ],
    "testimonialQuote": "Gerente Restaurante Pro + Bar & Lounge AI+ + Food Pairing AI elevaram completamente o nível da equipa de sala. O briefing diário com storytelling gerado de cada prato e harmonização validada cientificamente é agora profissional. Os clientes notam a diferença: subimos o ticket médio 20 % e o rácio de recorrentes premium cresceu 40 % em seis meses.",
    "testimonialAuthor": "Sofía Vega",
    "testimonialRole": "Maître e Chefe de Sala, restaurante fine dining",
    "faqTitle": "Perguntas Frequentes de Maîtres",
    "faqs": [
      {
        "q": "Serve para fine dining, restaurante de autor, gastronómico Michelin ou restaurante premium?",
        "a": "Para os quatro. Gerente Restaurante Pro + Bar & Lounge AI+ cobrem desde restaurante premium até gastronómico Michelin com serviço impecável, gueridon, decantação profissional e storytelling."
      },
      {
        "q": "Como gerir reservas premium e clientes recorrentes?",
        "a": "O Gerente Restaurante Pro raciocina com critério profissional de sala: planeamento de mesas por preferência, anotação de alergias e ocasiões, captação de clientes recorrentes com menus personalizados."
      },
      {
        "q": "Como treino a equipa de sala com harmonizações e storytelling?",
        "a": "O Food Pairing AI fundamenta cada harmonização com base científica que a equipa pode comunicar ao cliente; o Bar & Lounge AI+ aprofunda em adega, decantação e técnicas. O briefing diário é agora profissional."
      },
      {
        "q": "Gera conteúdo visual elegante para Instagram?",
        "a": "Sim. O GastroIMG Gen+ gera imagens elegantes de referência do menu e mesa posta para Instagram, web e captação de clientes premium. Lembre-se que a imagem IA é de referência visual: a foto definitiva é feita por si com a sua mesa real."
      },
      {
        "q": "Como me ajuda com eventos privados e jantares corporativos?",
        "a": "O Gastro Calendar planeia eventos privados, jantares corporativos, Natal, São Valentim, aniversários com menus de degustação e propostas de serviço dedicado."
      }
    ],
    "ctaTitle": "A sua sala com técnica profissional e experiência memorável.",
    "ctaSubtitle": "Comece com o onboarding de 2 minutos. Plano Membro por 10 € por mês com 10.000 créditos para usar todos os agentes.",
    "seo": {
      "title": "IA para Maître e Chefe de Sala: Serviço, Harmonizações e Storytelling | AI Chef Pro",
      "description": "Suite de IA para maîtres profissionais: Gerente Pro, Bar & Lounge AI+, Food Pairing AI, formação de equipa e captação premium. Comece hoje.",
      "keywords": "IA maître, IA chefe de sala, software maître, fine dining sala, gueridon decantação IA, formação equipa sala",
      "ogImage": "https://aichef.pro/og/use-cases/maitre-jefe-sala.jpg"
    },
    "personalizationTitle": "Personalizado à Sua Sala desde o Minuto Um",
    "personalizationBody": "O AI Chef Pro arranca com o agente «Quem Sou Eu?», um onboarding conversacional de 2 minutos em que conta que tipo de sala dirige (fine dining, restaurante de autor, gastronómico Michelin/Repsol, restaurante premium com adega), tamanho da equipa, cidade e especialidade. Cada agente responde adaptado à sua sala e operativa real.",
    "appsTitle": "Os Agentes IA que Vai Usar como Maître",
    "apps": [
      {
        "name": "Gerente Restaurante Pro",
        "category": "Gastro Profile Pro",
        "description": "Agente especializado adaptado à gestão de sala fine dining."
      },
      {
        "name": "Bar & Lounge AI+",
        "category": "Conceitos de Negócio",
        "description": "Gestão de adega, decantações, recomendações de vinho e coquetelaria profissional."
      },
      {
        "name": "Food Pairing AI",
        "category": "Criatividade Culinária",
        "description": "Harmonizações com base científica para cada prato do menu."
      },
      {
        "name": "Culinária Criativa",
        "category": "Criatividade Culinária",
        "description": "Storytelling e descrições de pratos para a equipa de sala."
      },
      {
        "name": "Calcula Pax",
        "category": "Ferramentas e Utilitários",
        "description": "Escalamento de receitas para eventos privados e jantares corporativos."
      },
      {
        "name": "ID Alergénios",
        "category": "Ferramentas e Utilitários",
        "description": "Identificação automática de alergénios para comunicar ao cliente."
      },
      {
        "name": "Coach Mental",
        "category": "Ferramentas e Utilitários",
        "description": "Coaching para liderança de equipa de sala e gestão do stress em picos de serviço."
      },
      {
        "name": "GastroIMG Gen+",
        "category": "Gastro Conhecimento",
        "description": "Fotografia elegante IA de referência para Instagram, web e captação premium."
      },
      {
        "name": "InstaFlow AI Pro",
        "category": "Conteúdos e Redes Sociais",
        "description": "Instagram com calendário editorial elegante para fine dining."
      },
      {
        "name": "MenuDish Local SEO",
        "category": "Conteúdos e Redes Sociais",
        "description": "Captar clientes premium que procuram fine dining no Google e Maps."
      },
      {
        "name": "Gastro Calendar",
        "category": "Conteúdos e Redes Sociais",
        "description": "Eventos privados, jantares corporativos, Natal, São Valentim, aniversários."
      },
      {
        "name": "Refeição do Pessoal",
        "category": "Gastro Profile Pro",
        "description": "Gerador de menus de staff antes do serviço."
      }
    ],
    "metrics": [
      {
        "value": "+20 %",
        "label": "ticket médio fine dining"
      },
      {
        "value": "×1.4",
        "label": "rácio de clientes recorrentes"
      },
      {
        "value": "×2",
        "label": "velocidade de propostas de eventos"
      },
      {
        "value": "12+",
        "label": "agentes para a sua sala"
      }
    ],
    "beforeAfter": {
      "beforeTitle": "Sem AI Chef Pro",
      "beforeItems": [
        "Briefing à equipa improvisado, storytelling de prato sem rigor",
        "Harmonizações recomendadas sem base científica fundamentada",
        "Reservas premium sem planeamento com preferências e alergias",
        "Eventos privados fechados à mão, proposta lenta",
        "Instagram improvisado sem storytelling de serviço"
      ],
      "afterTitle": "Com AI Chef Pro",
      "afterItems": [
        "Briefing diário profissional com storytelling e harmonizações",
        "Harmonizações com base científica do Food Pairing AI",
        "Reservas premium com planeamento profissional e captação recorrente",
        "Eventos privados fechados em um dia com proposta de serviço",
        "Instagram elegante com GastroIMG Gen+ + InstaFlow AI Pro"
      ]
    },
    "galleryTitle": "Como Funciona a Sala de um Fine Dining",
    "gallerySubtitle": "O que vai coordenar com AI Chef Pro: mise de mesa, decantação, gueridon, serviço e equipa. Imagens geradas com IA como referência visual do conceito.",
    "galleryImages": [
      "/lovable-uploads/ai-gallery/use-case-maitre-hero.jpg",
      "/lovable-uploads/ai-gallery/use-case-maitre-mesa.jpg",
      "/lovable-uploads/ai-gallery/use-case-maitre-pour.jpg",
      "/lovable-uploads/ai-gallery/use-case-maitre-servicio.jpg",
      "/lovable-uploads/ai-gallery/use-case-maitre-gueridon.jpg",
      "/lovable-uploads/ai-gallery/use-case-maitre-team.jpg"
    ]
  },
  "sommelier": {
    "h1": "IA para Sommelier",
    "heroSubtitle": "Desenha cartas de vinhos com critério profissional, valida harmonizações com base científica, gere a adega com rastreabilidade e capta branding wine-driven com uma suite de agentes de IA gastronómica especializados em sommelaria profissional.",
    "heroTagline": "Adega com critério profissional e harmonizações científicas",
    "badge": "Para sommeliers, head sommeliers e diretores de adega",
    "painsTitle": "O Que um Sommelier Não Pode Deixar de Resolver",
    "pains": [
      "Desenhar carta de vinhos com critério: equilíbrio de regiões, castas, preços, copos e verticais por adega",
      "Validar harmonizações com base científica para cada prato do menu de degustação e carta que muda por estação",
      "Gerir adega com rastreabilidade: rotação, condições de cellar, pedidos, quebras por desarrolhamento falhado",
      "Padronizar o storytelling de cada vinho para que a equipa de sala o comunique com profissionalismo ao cliente",
      "Diferenciar-se num restaurante com muita concorrência com adega curada, desarrolhamento profissional e experiência wine-driven",
      "Captar clientes premium com provas, eventos de adega e harmonizações especiais com margem alta"
    ],
    "featuresTitle": "Como o AI Chef Pro Ajuda um Sommelier",
    "features": [
      {
        "icon": "Wine",
        "title": "Bar & Lounge AI+",
        "description": "Agente especializado em sommelaria profissional: adega, castas, regiões, técnica de desarrolhamento e serviço do vinho."
      },
      {
        "icon": "Sparkles",
        "title": "Food Pairing AI",
        "description": "Harmonizações com base científica para cada prato e vinho: análise de acidez, taninos, estrutura, intensidade e harmonia."
      },
      {
        "icon": "BookOpen",
        "title": "Culinária Criativa + Storytelling",
        "description": "Storytelling de cada vinho para a equipa de sala: adega, terroir, casta, vinificação, notas de prova."
      },
      {
        "icon": "Calculator",
        "title": "Custeio de adega",
        "description": "Custo real por copo, food cost do vinho por serviço, quebras por desarrolhamento e propostas de carta com margem validada."
      },
      {
        "icon": "CheckSquare",
        "title": "Kit de Tareas Bodega",
        "description": "Modelos: controlo de cellar (humidade, temperatura), rotação, desarrolhamento do dia, formação de equipa."
      },
      {
        "icon": "ShieldCheck",
        "title": "Pack APPCC adega",
        "description": "Rastreabilidade de vinhos, conservação, desarrolhamento falhado e temperaturas de serviço por tipo."
      },
      {
        "icon": "Calendar",
        "title": "Gastro Calendar",
        "description": "Provas e eventos de adega: harmonizações com menu de degustação, lançamentos, feiras de vinhos, Natal, eventos privados."
      },
      {
        "icon": "Image",
        "title": "GastroIMG Gen+ + InstaFlow AI Pro",
        "description": "Fotografia wine-driven IA de referência + Instagram com storytelling de adega para captar clientes premium."
      },
      {
        "icon": "BarChart3",
        "title": "Mermas Genéricas",
        "description": "Dados precisos de quebras em desarrolhamento falhado, copo partido e vinho na mesa."
      }
    ],
    "workflowTitle": "Um Dia Real de um Sommelier com AI Chef Pro",
    "workflow": [
      "11:00 · Abertura — checklist Kit de Tareas Bodega: controlo de cellar (12-14 °C, 70 % humidade), revisão de pedidos, rotação de vinhos do dia.",
      "12:00 · Bar & Lounge AI+ — atualiza a carta com duas referências novas (Borgonha tinto e Riesling alemão). Receita + storytelling gerado.",
      "13:00 · Food Pairing AI — valida a harmonização do novo Riesling com um prato de peixe fermentado do menu de degustação. Análise de acidez e harmonia.",
      "14:00 · Kit de Escandallos Pro — calcula o custo das duas referências novas com margem real por copo e por garrafa, valida o preço sugerido.",
      "15:00 · Briefing à equipa — explicação das duas referências novas com storytelling e harmonizações validadas.",
      "17:00 · Prova privada para cliente VIP — seleção de cinco vinhos com harmonizações ad hoc, desarrolhamento profissional, decanting quando aplica.",
      "20:00 · Serviço de jantar — coordenação com maître e cozinha, recomendações por mesa, guéridon quando aplica.",
      "23:00 · Encerramento — atualização de stock, GastroIMG Gen+ gera imagem de referência do novo Borgonha + InstaFlow programa o post."
    ],
    "productsTitle": "Modelos e Kits Recomendados para Sommelier",
    "productIds": [
      "kit-tareas-bar",
      "kit-escandallos",
      "pack-appcc",
      "kit-inventario",
      "pro-prompts-ebook",
      "kit-gestion-personal"
    ],
    "testimonialQuote": "Bar & Lounge AI+ + Food Pairing AI mudaram a minha proposta. Cada harmonização do menu de degustação tem agora base científica documentada que a equipa de sala comunica ao cliente com profissionalismo. A gestão de adega com custeio por copo aumentou-nos a margem de vinhos em 6 pontos. As provas privadas para VIPs fecham-se numa chamada com proposta profissional.",
    "testimonialAuthor": "Eduardo Lara",
    "testimonialRole": "Head Sommelier, restaurante com 1 estrela Michelin",
    "faqTitle": "Perguntas Frequentes de Sommeliers",
    "faqs": [
      {
        "q": "Serve para sommelier de fine dining, restaurante gastronómico, garrafeira ou hotel?",
        "a": "Para os quatro. O Bar & Lounge AI+ cobre desde sommelier de restaurante premium até head sommelier de gastronómico Michelin, garrafeira com adega curada ou hotel com multi-outlet."
      },
      {
        "q": "Como é que me ajuda com harmonizações científicas?",
        "a": "O Food Pairing AI raciocina com base científica: análise de acidez, taninos, estrutura, intensidade, harmonia e contraste. Fundamenta cada harmonização para que a equipa de sala a comunique com profissionalismo."
      },
      {
        "q": "Como é que faço o custeio e a margem por copo?",
        "a": "O Kit de Escandallos Pro recalcula a margem por copo e por garrafa quando atualiza preços de adega. As Mermas Genéricas acrescentam o custo de desarrolhamento falhado e quebras em serviço."
      },
      {
        "q": "Gera conteúdo visual wine-driven para Instagram?",
        "a": "Sim. O GastroIMG Gen+ gera imagens de referência profissionais de copos, decanting e adega para Instagram, web e captação de clientes premium. Lembre-se de que a imagem IA é de referência visual: a foto definitiva é feita por si com o seu copo real."
      },
      {
        "q": "Como é que me ajuda com provas privadas e eventos de adega?",
        "a": "O Gastro Calendar planifica provas privadas, eventos de adega, feiras de vinhos, lançamentos por estação e harmonizações com menus de degustação."
      }
    ],
    "ctaTitle": "A sua adega com critério profissional e harmonizações científicas.",
    "ctaSubtitle": "Começa com o onboarding de 2 minutos. Plano Membro por 10 € por mês com 10.000 créditos para usar todos os agentes.",
    "seo": {
      "title": "IA para Sommelier: Adega, Harmonizações e Provas Profissionais | AI Chef Pro",
      "description": "Suite de IA para sommeliers profissionais: Bar & Lounge AI+, Food Pairing AI, custeio por copo, provas privadas e branding wine-driven. Comece hoje.",
      "keywords": "IA sommelier, software sommelier, harmonizações IA, gestão de adega IA, custeio de vinhos, head sommelier, prova privada IA",
      "ogImage": "https://aichef.pro/og/use-cases/sommelier.jpg"
    },
    "personalizationTitle": "Personalizado para a Sua Adega desde o Primeiro Minuto",
    "personalizationBody": "O AI Chef Pro arranca com o agente «Quem Sou Eu?», um onboarding conversacional de 2 minutos em que lhe conta que tipo de sommelier é (head sommelier de fine dining, sommelier freelance, diretor de garrafeira, sommelier de hotel, formador), tamanho da adega, cidade e especialidade. Cada agente responde adaptado à sua adega e operação real.",
    "appsTitle": "Os Agentes de IA que Vai Usar como Sommelier",
    "apps": [
      {
        "name": "Bar & Lounge AI+",
        "category": "Conceitos de Negócio",
        "description": "Agente especializado em sommelaria profissional: adega, castas, regiões, técnica."
      },
      {
        "name": "Food Pairing AI",
        "category": "Criatividade Culinária",
        "description": "Harmonizações com base científica: acidez, taninos, estrutura, intensidade e harmonia."
      },
      {
        "name": "Culinária Criativa",
        "category": "Criatividade Culinária",
        "description": "Storytelling de cada vinho: terroir, vinificação, notas de prova para a equipa de sala."
      },
      {
        "name": "Mermas Genéricas",
        "category": "Ferramentas e Utilitários",
        "description": "Quebras em desarrolhamento falhado, copo partido e vinho na mesa integradas no custeio."
      },
      {
        "name": "ID Alergénios",
        "category": "Ferramentas e Utilitários",
        "description": "Identificação de sulfitos em vinhos para clientes com sensibilidade."
      },
      {
        "name": "Léxico Gastronómico",
        "category": "Gastro Conhecimento",
        "description": "Tutor de definições técnicas: enologia, vinificação, terroir, denominações."
      },
      {
        "name": "GastroIMG Gen+",
        "category": "Gastro Conhecimento",
        "description": "Fotografia wine-driven IA de referência para Instagram, web e eventos."
      },
      {
        "name": "InstaFlow AI Pro",
        "category": "Conteúdos e Redes Sociais",
        "description": "Instagram com calendário editorial wine-driven para captar clientes premium."
      },
      {
        "name": "MenuDish Local SEO",
        "category": "Conteúdos e Redes Sociais",
        "description": "Captar clientes que procuram garrafeira, prova ou sommelier no Google e Maps."
      },
      {
        "name": "Gastro Calendar",
        "category": "Conteúdos e Redes Sociais",
        "description": "Provas privadas, feiras de vinhos, lançamentos, Natal, eventos de adega."
      },
      {
        "name": "BlogPost SEO Gen+",
        "category": "Conteúdos e Redes Sociais",
        "description": "Artigos SEO sobre harmonizações, castas e adegas para captar tráfego orgânico."
      },
      {
        "name": "Sonar Deep Research",
        "category": "Modelos IA + LLM",
        "description": "Research profundo sobre adegas emergentes, terroirs, colheitas e tendências."
      }
    ],
    "metrics": [
      {
        "value": "+6 pp",
        "label": "margem após custeio da adega"
      },
      {
        "value": "×2",
        "label": "velocidade de propostas de prova"
      },
      {
        "value": "×3",
        "label": "engagement Instagram wine-driven"
      },
      {
        "value": "12+",
        "label": "agentes para a sua adega"
      }
    ],
    "beforeAfter": {
      "beforeTitle": "Sem AI Chef Pro",
      "beforeItems": [
        "Harmonizações recomendadas sem base científica documentada",
        "Carta de vinhos sem custeio por copo e margem real",
        "Adega gerida em folhas de cálculo, sem rastreabilidade nem rotação clara",
        "Storytelling de vinho improvisado, equipa de sala sem formação constante",
        "Provas privadas fechadas à mão, proposta lenta"
      ],
      "afterTitle": "Com AI Chef Pro",
      "afterItems": [
        "Harmonizações com base científica do Food Pairing AI",
        "Custeio por copo com margem validada em tempo real",
        "Adega com rastreabilidade APPCC e rotação documentada",
        "Briefing diário à equipa com storytelling e harmonizações",
        "Provas privadas fechadas num dia com proposta wine-driven"
      ]
    },
    "galleryTitle": "Como Funciona a Adega de um Sommelier",
    "gallerySubtitle": "O que vai coordenar com AI Chef Pro: cellar, decanting, copo, prova e equipa. Imagens geradas com IA como referência visual do conceito.",
    "galleryImages": [
      "/lovable-uploads/ai-gallery/use-case-sommelier-hero.jpg",
      "/lovable-uploads/ai-gallery/use-case-sommelier-decanting.jpg",
      "/lovable-uploads/ai-gallery/use-case-sommelier-copa.jpg",
      "/lovable-uploads/ai-gallery/use-case-sommelier-cellar.jpg",
      "/lovable-uploads/ai-gallery/use-case-sommelier-tasting.jpg",
      "/lovable-uploads/ai-gallery/use-case-sommelier-team.jpg"
    ]
  },
  "maestro-asador": {
    "h1": "IA para Mestre Grelhador e Parrilheiro",
    "heroSubtitle": "Domine técnica de brasas, desmancha e dry-aged com escandallo profissional por corte, planeie produção de proteínas e capture branding fire-driven com uma suite de agentes de IA gastronómica especializados em cozinha ao fogo profissional.",
    "heroTagline": "Brasas com técnica autêntica e margem real",
    "badge": "Para mestres grelhadores, parrilheiros e grillmasters",
    "painsTitle": "O Que um Mestre Grelhador Não Pode Deixar de Resolver",
    "pains": [
      "Padronizar ponto de cozedura e técnica de brasas turno a turno (carvão vegetal, lenha, marmoreio, temperatura interna)",
      "Desmancha rigorosa com custo por quilo e rendimento por corte (chuletão, picanha, T-bone, lombo)",
      "Gestão de dry-aged com câmara, humidade, temperatura, rotação e merma semanal documentada",
      "Coordenar grelha com cozinha principal em picos de serviço sem perder qualidade nem timing",
      "Storytelling de fornecedores pecuários, raça, alimentação e maturação para sala",
      "Formar equipa de parrilheiros juniores com critério técnico e consistência no ponto de cozedura"
    ],
    "featuresTitle": "Como AI Chef Pro Ajuda um Mestre Grelhador",
    "features": [
      {
        "icon": "Flame",
        "title": "Culinária Criativa",
        "description": "Para desenvolvimento técnico de cortes signature, marinadas, molhos e guarnições de grelhador."
      },
      {
        "icon": "UtensilsCrossed",
        "title": "Cozinha Argentina + Brasileira",
        "description": "Receituários especializados: grelha, chimichurri, picanha, churrasco, técnica autêntica."
      },
      {
        "icon": "Calculator",
        "title": "Escandallos por corte com dry-aged",
        "description": "Receita + escandallo CSV com merma de dry-aged integrada e custo hora de grelha. Margem real por corte."
      },
      {
        "icon": "BarChart3",
        "title": "Mermas Genéricas",
        "description": "Dados por processo: desmancha, dry-aging semanal, trimming, merma de cozedura."
      },
      {
        "icon": "CheckSquare",
        "title": "Kit de Tareas Restaurante Casual",
        "description": "Modelos: acendimento de brasas, desmancha, controlo de câmara dry-aged, mise, encerramento."
      },
      {
        "icon": "ShieldCheck",
        "title": "Pack APPCC grelhador",
        "description": "Rastreabilidade de carne, dry-aging, temperatura interna e conservação."
      },
      {
        "icon": "Wine",
        "title": "Bar & Lounge AI+",
        "description": "Harmonizações com tintos potentes para os novos cortes signature."
      },
      {
        "icon": "Calendar",
        "title": "Gastro Calendar",
        "description": "Dia do Pai, Natal, eventos corporativos e lançamentos por temporada."
      },
      {
        "icon": "Image",
        "title": "GastroIMG Gen+ + InstaFlow AI Pro",
        "description": "Fotografia premium IA de referência + Instagram com storytelling de fornecedor pecuário."
      }
    ],
    "workflowTitle": "Um Dia Real de um Mestre Grelhador com AI Chef Pro",
    "workflow": [
      "09:00 · Abertura — checklist Kit de Tareas: acendimento controlado de brasas (3 horas para chegar ao ponto), controlo câmara dry-aged.",
      "11:00 · Culinária Criativa + Cozinha Argentina — desenvolve um novo corte signature de chuletão galego dry-aged 60 dias com sal Maldon fumada e chimichurri. Receita + escandallo CSV.",
      "12:00 · Kit de Escandallos Pro — carrega o CSV com os seus preços reais de carne e merma de dry-aged, valida margem real por corte.",
      "13:00 · Serviço meio-dia — grelha a pleno com cortes premium, mise de chimichurri e guarnições.",
      "17:00 · Briefing à equipa — formação de parrilheiros juniores com critério técnico de ponto de cozedura.",
      "20:00 · Serviço jantar — picos coordenados, grelha com vários cortes simultâneos.",
      "22:00 · GastroIMG Gen+ + InstaFlow AI Pro — gera a imagem de referência do novo chuletão e os posts para Instagram.",
      "00:00 · Encerramento — limpeza profunda de grelhas, APPCC assinado, controlo de câmara dry-aged."
    ],
    "productsTitle": "Modelos e Kits Recomendados para Mestre Grelhador",
    "productIds": [
      "kit-tareas",
      "kit-escandallos",
      "pack-appcc",
      "kit-inventario",
      "kit-gestion-personal",
      "pro-prompts-ebook"
    ],
    "testimonialQuote": "Cozinha Argentina + Culinária Criativa subiram o meu nível. A minha equipa replica agora o ponto de cozedura com critério técnico documentado, os escandallos de cortes premium refletem a merma do dry-aged e subimos margem 5 pontos. O planeamento do Dia do Pai com Gastro Calendar triplicou a nossa faturação.",
    "testimonialAuthor": "Pedro Aguirre",
    "testimonialRole": "Mestre grelhador, grelhador premium com dry-aged",
    "faqTitle": "Perguntas Frequentes de Mestres Grelhadores",
    "faqs": [
      {
        "q": "Serve para grelha argentina, churrascaria, grelhador premium ou steakhouse?",
        "a": "Para os quatro. Cozinha Argentina + Cozinha Brasileira + Culinária Criativa cobrem desde grelha tradicional até steakhouse com dry-aged."
      },
      {
        "q": "Cobre dry-aged e gestão de câmara?",
        "a": "Sim. Raciocina como mestre grelhador profissional: condições de câmara, tempos por corte, controlo de merma semanal e rotação."
      },
      {
        "q": "Como gero o custo volátil da carne?",
        "a": "Kit de Escandallos Pro recalcula a margem instantaneamente. Mermas Genéricas adiciona o custo de mermas por dry-aging, desmancha e trimming."
      },
      {
        "q": "Gera conteúdo visual para Instagram?",
        "a": "Sim. GastroIMG Gen+ gera imagens de referência profissionais de cortes e brasas. Lembre-se que a imagem IA é de referência visual: a foto definitiva é feita por si com o seu corte real."
      },
      {
        "q": "Como me ajuda com eventos corporativos?",
        "a": "Gastro Calendar planeia Dia do Pai, Natal, eventos corporativos e lançamentos de cortes por temporada."
      }
    ],
    "ctaTitle": "A sua grelha com técnica de fogo e margem real.",
    "ctaSubtitle": "Comece com o onboarding de 2 minutos. Plano Membro por 10 € por mês com 10.000 créditos para usar todos os agentes.",
    "seo": {
      "title": "IA para Mestre Grelhador e Parrilheiro: Cortes, Brasas e Dry-Aged | AI Chef Pro",
      "description": "Suite de IA para mestres grelhadores: Cozinha Argentina + Brasileira, escandallos por corte, dry-aged, branding e APPCC. Comece hoje.",
      "keywords": "IA mestre grelhador, IA parrilheiro, software grelhador, escandallos chuletão, dry-aged, técnica de brasas, grelha argentina IA",
      "ogImage": "https://aichef.pro/og/use-cases/maestro-asador-parrillero.jpg"
    },
    "personalizationTitle": "Personalizado à Sua Grelha desde o Minuto Um",
    "personalizationBody": "AI Chef Pro arranca com o agente «Quem Sou Eu?», um onboarding de 2 minutos em que lhe conta que tipo de grelha dirige (grelha argentina, churrascaria brasileira, steakhouse premium com dry-aged, grelhador casual de bairro), tamanho da equipa, cidade e especialidade. Cada agente responde adaptado à sua grelha e operacional real.",
    "appsTitle": "Os Agentes IA que Vai Usar como Mestre Grelhador",
    "apps": [
      {
        "name": "Culinária Criativa",
        "category": "Criatividade Culinária",
        "description": "Desenvolvimento de cortes signature com técnica de brasas e guarnições."
      },
      {
        "name": "Cozinha Argentina",
        "category": "Receituários da América Latina",
        "description": "Asado, chimichurri, molejas e técnica de grelha autêntica."
      },
      {
        "name": "Cozinha Brasileira",
        "category": "Receituários da América Latina",
        "description": "Picanha, churrasco, farofa e técnica de churrascaria."
      },
      {
        "name": "Food Pairing AI",
        "category": "Criatividade Culinária",
        "description": "Harmonizações com tintos potentes e coquetelaria de carácter."
      },
      {
        "name": "Bar & Lounge AI+",
        "category": "Conceitos de Negócio",
        "description": "Para barra do grelhador com vinhos tintos premium."
      },
      {
        "name": "Mermas Genéricas",
        "category": "Ferramentas e Utilitários",
        "description": "Mermas em desmancha, dry-aging, trimming e cozedura."
      },
      {
        "name": "ID Alergénios",
        "category": "Ferramentas e Utilitários",
        "description": "Identificação automática por corte e guarnição."
      },
      {
        "name": "GastroIMG Gen+",
        "category": "Gastro Conhecimento",
        "description": "Fotografia premium IA de referência para Instagram, web e carta."
      },
      {
        "name": "InstaFlow AI Pro",
        "category": "Conteúdos e Redes Sociais",
        "description": "Instagram com calendário editorial fire-driven."
      },
      {
        "name": "MenuDish Local SEO",
        "category": "Conteúdos e Redes Sociais",
        "description": "Captar clientes que procuram \"grelhador perto\" no Google e Maps."
      },
      {
        "name": "Gastro Calendar",
        "category": "Conteúdos e Redes Sociais",
        "description": "Dia do Pai, Natal, eventos corporativos."
      },
      {
        "name": "Coach Mental",
        "category": "Ferramentas e Utilitários",
        "description": "Coaching para liderança de equipa e picos de serviço."
      }
    ],
    "metrics": [
      {
        "value": "+5 pp",
        "label": "margem após escandallar cortes"
      },
      {
        "value": "×3",
        "label": "faturação no Dia do Pai"
      },
      {
        "value": "−15 %",
        "label": "mermas em desmancha e dry-aging"
      },
      {
        "value": "12+",
        "label": "agentes para a sua grelha"
      }
    ],
    "beforeAfter": {
      "beforeTitle": "Sem AI Chef Pro",
      "beforeItems": [
        "Ponto de cozedura improvisado entre parrilheiros",
        "Escandallos sem merma do dry-aged",
        "Câmara dry-aged sem rastreabilidade",
        "Briefing improvisado, formação variável",
        "Instagram sem storytelling de fornecedor pecuário"
      ],
      "afterTitle": "Com AI Chef Pro",
      "afterItems": [
        "Ponto de cozedura consistente com critério técnico",
        "Escandallo profissional com merma de dry-aged integrada",
        "Câmara com rastreabilidade APPCC documentada",
        "Briefing diário profissional, formação constante",
        "GastroIMG Gen+ + storytelling de fornecedor pecuário"
      ]
    },
    "galleryTitle": "Como Funciona a Grelha de um Mestre Grelhador",
    "gallerySubtitle": "O que vai coordenar com AI Chef Pro: brasas, desmancha, cortes, chimichurri e equipa. Imagens geradas com IA como referência visual do conceito.",
    "galleryImages": [
      "/lovable-uploads/ai-gallery/use-case-maestro-asador-hero.jpg",
      "/lovable-uploads/ai-gallery/use-case-maestro-asador-tongs.jpg",
      "/lovable-uploads/ai-gallery/use-case-maestro-asador-cuts.jpg",
      "/lovable-uploads/ai-gallery/use-case-maestro-asador-fire.jpg",
      "/lovable-uploads/ai-gallery/use-case-maestro-asador-chimichurri.jpg",
      "/lovable-uploads/ai-gallery/use-case-maestro-asador-team.jpg"
    ]
  },
  "maestro-heladero": {
    "h1": "IA para Mestre Geladeiro e Gelatiere",
    "heroSubtitle": "Domine o equilíbrio técnico de bases, escandallo por sabor com custo real, planeie produção sazonal e capture branding artesanal com uma suite de agentes de IA gastronómica especializados em gelataria profissional.",
    "heroTagline": "Gelado com técnica autêntica e margem real",
    "badge": "Para mestres geladeiros, gelatieri e artesãos do gelado",
    "painsTitle": "O Que um Mestre Geladeiro Não Pode Deixar de Resolver",
    "pains": [
      "Equilíbrio técnico exigente: equilíbrio de açúcares (sacarose, dextrose, açúcar invertido), sólidos totais e gorduras para textura ótima",
      "Mermas na mantecadora, abatimento e vitrina com produto sensível à temperatura",
      "Sazonalidade extrema: época alta verão, vale invernal que rentabilizar com tartes geladas e semifrios",
      "Padronizar produção de bases (branca, amarela, fruta, sorbet) turno a turno com critério técnico",
      "Diferenciar-se em zona concorrida com sabores próprios, ingredientes premium (Sosa, Pistácio di Bronte) e branding visual",
      "Formar a equipa em técnica profissional de equilíbrio e cristalização"
    ],
    "featuresTitle": "Como AI Chef Pro Ajuda um Mestre Geladeiro",
    "features": [
      {
        "icon": "IceCream",
        "title": "Gelataria Criativa",
        "description": "Agente especializado em gelataria artesanal profissional: bases branca, amarela, fruta, sorbets, equilíbrio técnico de açúcares."
      },
      {
        "icon": "Cake",
        "title": "Pastelaria Criativa",
        "description": "Para tartes geladas, semifrios, sobremesas de colher que rentabilizam o vale invernal."
      },
      {
        "icon": "Sparkles",
        "title": "Culinária Criativa",
        "description": "Para desenvolvimento de sabores signature, fusões controladas e apresentações de autor."
      },
      {
        "icon": "Calculator",
        "title": "Escandallos por sabor",
        "description": "Gelataria Criativa entrega receita + escandallo CSV com equilíbrio técnico; Kit de Escandallos Pro gere-o com margem real por kg, por bola e por cone."
      },
      {
        "icon": "Beaker",
        "title": "Sosa Ingredients",
        "description": "Catálogo Sosa para texturas profissionais, neutros, estabilizantes e pastas concentradas."
      },
      {
        "icon": "CheckSquare",
        "title": "Kit de Tareas Heladería",
        "description": "Modelos: preparação da mantecadora, abatimento, reposição da vitrina, controlo de temperaturas, rotação."
      },
      {
        "icon": "ShieldCheck",
        "title": "Pack APPCC gelataria",
        "description": "Rastreabilidade de leite, fruta fresca, frutos secos e temperaturas críticas."
      },
      {
        "icon": "Calendar",
        "title": "Gastro Calendar",
        "description": "Dia da Mãe, primavera, verão, São Valentim, tartes geladas Natal."
      },
      {
        "icon": "Image",
        "title": "GastroIMG Gen+ + InstaFlow AI Pro",
        "description": "Fotografia artesanal IA de referência + Instagram para captar clientes locais."
      }
    ],
    "workflowTitle": "Um Dia Real de um Mestre Geladeiro com AI Chef Pro",
    "workflow": [
      "07:00 · Abertura — checklist Kit de Tareas: revisão da câmara, abatimento de misturas preparadas na véspera.",
      "08:30 · Gelataria Criativa — desenvolve um novo sabor signature de pistácio di Bronte com sal Maldon. Culinária Criativa entrega receita + escandallo CSV.",
      "09:30 · Sosa Ingredients — seleciona pasta concentrada e neutro adequados.",
      "10:00 · Kit de Escandallos Pro — carrega CSV com os seus preços reais de pistácio premium e leite, valida margem por bola e por kg.",
      "11:00 · Produção do dia — passa misturas pela mantecadora, abate a -18 °C.",
      "13:30 · Reposição da vitrina com etiquetas e controlo de mermas de exposição.",
      "16:00 · Pastelaria Criativa — desenvolve uma tarte gelada para o Dia da Mãe com semifrio de pistácio.",
      "18:00 · GastroIMG Gen+ + InstaFlow AI Pro — gera imagem de referência do novo sabor + posts."
    ],
    "productsTitle": "Modelos e Kits Recomendados para Mestre Geladeiro",
    "productIds": [
      "kit-tareas-heladeria",
      "kit-escandallos",
      "pack-appcc",
      "kit-inventario",
      "kit-gestion-personal",
      "pro-prompts-ebook"
    ],
    "testimonialQuote": "Gelataria Criativa mudou-nos a cozinha. Equilibrámos açúcares e sólidos com critério técnico, os escandallos por bola com pistácio premium refletem margem real. Pastelaria Criativa abriu-nos as tartes geladas que rentabilizam o inverno. Subimos 5 pontos.",
    "testimonialAuthor": "Federico Riva",
    "testimonialRole": "Mestre gelatiere, gelataria artesanal premium",
    "faqTitle": "Perguntas Frequentes de Mestres Geladeiros",
    "faqs": [
      {
        "q": "Serve para gelataria italiana, gelataria artesanal ou cadeia com vários pontos?",
        "a": "Para as três. Gelataria Criativa raciocina como mestre geladeiro profissional com equilíbrio técnico documentado."
      },
      {
        "q": "Cobre equilíbrio de açúcares, sólidos e gorduras?",
        "a": "Sim. Gelataria Criativa raciocina como geladeiro profissional: equilíbrio com sacarose, dextrose, açúcar invertido, sólidos totais e gorduras conforme norma técnica."
      },
      {
        "q": "Como me ajuda com a sazonalidade?",
        "a": "Pastelaria Criativa abre tartes geladas e semifrios para o vale invernal; Gastro Calendar planeia picos (Dia da Mãe, verão)."
      },
      {
        "q": "Gera conteúdo visual para Instagram?",
        "a": "Sim. GastroIMG Gen+ gera imagens de referência para vitrina e redes. Lembre-se de que a imagem IA é de referência visual: a foto definitiva é feita por si com a sua cuba e empratamento real."
      },
      {
        "q": "Como gero mermas na mantecadora e vitrina?",
        "a": "Mermas Genéricas entrega dados por processo (mantecadora, abatimento, exposição). Integram-se ao escandallo do Kit de Escandallos Pro."
      }
    ],
    "ctaTitle": "O seu gelado com técnica autêntica e margem real.",
    "ctaSubtitle": "Comece com o onboarding de 2 minutos. Plano Membro por 10 € por mês com 10.000 créditos.",
    "seo": {
      "title": "IA para Mestre Geladeiro e Gelatiere: Bases, Escandallos e Sazonalidade | AI Chef Pro",
      "description": "Suite de IA para mestres geladeiros: Gelataria Criativa, equilíbrio técnico, escandallos por sabor, branding e APPCC. Comece hoje.",
      "keywords": "IA mestre geladeiro, IA gelatiere, software gelataria, escandallos gelado, equilíbrio técnico gelado, mantecadora IA",
      "ogImage": "https://aichef.pro/og/use-cases/maestro-heladero.jpg"
    },
    "personalizationTitle": "Personalizado à Sua Gelataria desde o Minuto Um",
    "personalizationBody": "AI Chef Pro arranca com o agente «Quem Sou Eu?», um onboarding de 2 minutos em que você conta que tipo de gelataria opera (gelataria italiana, gelataria artesanal espanhola, gelataria com obrador), tamanho da equipa, cidade e especialidade.",
    "appsTitle": "Os Agentes de IA que Vai Usar como Mestre Geladeiro",
    "apps": [
      {
        "name": "Gelataria Criativa",
        "category": "Criatividade Culinária",
        "description": "Agente especializado em gelataria artesanal com equilíbrio técnico."
      },
      {
        "name": "Pastelaria Criativa",
        "category": "Criatividade Culinária",
        "description": "Tartes geladas, semifrios, sobremesas de colher para vale invernal."
      },
      {
        "name": "Culinária Criativa",
        "category": "Criatividade Culinária",
        "description": "Desenvolvimento de sabores signature com receita + escandallo CSV."
      },
      {
        "name": "Sosa Ingredients",
        "category": "Fornecedores Gastro",
        "description": "Neutros, estabilizantes, pastas concentradas e texturas profissionais."
      },
      {
        "name": "Mermas Genéricas",
        "category": "Ferramentas e Utilitários",
        "description": "Mermas na mantecadora, abatimento e vitrina."
      },
      {
        "name": "ID Alergénios",
        "category": "Ferramentas e Utilitários",
        "description": "Identificação automática por sabor: laticínios, frutos secos, glúten."
      },
      {
        "name": "GastroIMG Gen+",
        "category": "Conhecimento Gastro",
        "description": "Fotografia artesanal IA de referência para vitrina, web e redes."
      },
      {
        "name": "InstaFlow AI Pro",
        "category": "Conteúdos e Redes Sociais",
        "description": "Instagram com calendário editorial para gelataria de autor."
      },
      {
        "name": "MenuDish Local SEO",
        "category": "Conteúdos e Redes Sociais",
        "description": "Captar clientes que procuram \"gelataria perto de mim\"."
      },
      {
        "name": "Gastro Calendar",
        "category": "Conteúdos e Redes Sociais",
        "description": "Dia da Mãe, verão, São Valentim, tartes geladas Natal."
      },
      {
        "name": "Gerador de Pins Pinterest",
        "category": "Conteúdos e Redes Sociais",
        "description": "Pinterest captura tráfego orgânico para tartes geladas."
      },
      {
        "name": "Refeição do Pessoal",
        "category": "Gastro Profile Pro",
        "description": "Gerador de menus de staff para o obrador."
      }
    ],
    "metrics": [
      {
        "value": "+5 pp",
        "label": "margem após escandallar sabores"
      },
      {
        "value": "−40 %",
        "label": "mermas em obrador e vitrina"
      },
      {
        "value": "×3",
        "label": "engagement Instagram"
      },
      {
        "value": "12+",
        "label": "agentes para o seu obrador"
      }
    ],
    "beforeAfter": {
      "beforeTitle": "Sem AI Chef Pro",
      "beforeItems": [
        "Bases improvisadas, equilíbrio inconsistente turno a turno",
        "Escandallos sem equilíbrio técnico documentado",
        "Mermas sem rastreabilidade por processo",
        "Sazonalidade reativa em vale invernal",
        "Vitrina e redes sociais improvisadas"
      ],
      "afterTitle": "Com AI Chef Pro",
      "afterItems": [
        "Bases com equilíbrio técnico documentado",
        "Escandallos profissionais por bola e por kg",
        "Mermas controladas com Mermas Genéricas",
        "Tartes geladas e semifrios rentabilizam o inverno",
        "GastroIMG Gen+ + InstaFlow + Gerador de Pins Pinterest"
      ]
    },
    "galleryTitle": "Como Funciona o Obrador de um Mestre Geladeiro",
    "gallerySubtitle": "O que vai coordenar com AI Chef Pro: mantecadora, bases, espátula, fruta e equipa. Imagens geradas com IA como referência visual do conceito.",
    "galleryImages": [
      "/lovable-uploads/ai-gallery/use-case-maestro-heladero-hero.jpg",
      "/lovable-uploads/ai-gallery/use-case-maestro-heladero-mantecadora.jpg",
      "/lovable-uploads/ai-gallery/use-case-maestro-heladero-bases.jpg",
      "/lovable-uploads/ai-gallery/use-case-maestro-heladero-spatula.jpg",
      "/lovable-uploads/ai-gallery/use-case-maestro-heladero-fruta.jpg",
      "/lovable-uploads/ai-gallery/use-case-maestro-heladero-team.jpg"
    ]
  },
  "repostero-pastelero": {
    "h1": "IA para Confeiteiro e Pasteleiro",
    "heroSubtitle": "Domine técnica de pastelaria profissional, custo de produção por peça com custo hora de oficina, planeie produção sazonal e capture branding artesanal com uma suite de agentes de IA gastronómica especializados em confeitaria e pastelaria de autor.",
    "heroTagline": "Pastelaria com técnica autêntica e margem real",
    "badge": "Para confeiteiros, pasteleiros e chefs pâtissiers",
    "painsTitle": "O Que um Confeiteiro Não Pode Deixar de Resolver",
    "pains": [
      "Técnica avançada exigente: massa folhada, massas brisée e sablée, biscuits, ganaches, glaceados, mousses com equilíbrio preciso",
      "Perdas altas na oficina (modelagem, cozedura, decoração) que sangram rentabilidade sem controlo",
      "Padronizar peças signature turno a turno com consistência profissional",
      "Sazonalidade muito forte: Bolo Rei, Páscoa, Dia dos Namorados, Natal concentram uma alta percentagem do ano",
      "Diferenciar-se com confeitaria de autor, apresentação premium e storytelling de técnica francesa ou moderna",
      "Captar pedidos de tartes à medida, eventos privados e casamentos com margem enquanto se gere a pastelaria diária"
    ],
    "featuresTitle": "Como AI Chef Pro Ajuda um Confeiteiro",
    "features": [
      {
        "icon": "Cake",
        "title": "Pastelaria Criativa",
        "description": "Agente especializado em pastelaria profissional, sobremesas de restaurante, tartes à medida e pastelaria com técnica avançada."
      },
      {
        "icon": "Cookie",
        "title": "Chocolataria Criativa",
        "description": "Para combinações avançadas pastelaria + chocolate: ganaches, cremoso, glaceados."
      },
      {
        "icon": "Sparkles",
        "title": "Culinária Criativa",
        "description": "Para desenvolvimento de sobremesas signature e combinações de sabores com critério técnico."
      },
      {
        "icon": "Calculator",
        "title": "Custos de produção com custo hora de oficina",
        "description": "Pastelaria Criativa entrega receita + custo de produção CSV; Kit de Escandallos Pro gere-o com custo hora de oficina integrado em margem real por peça."
      },
      {
        "icon": "Beaker",
        "title": "Sosa Ingredients",
        "description": "Catálogo Sosa para texturas, gelificantes, neutros e técnica avançada."
      },
      {
        "icon": "CheckSquare",
        "title": "Kit de Tareas Pastelería",
        "description": "Modelos: preparação de massa, produção, modelagem, cozedura, decoração, montra, conservação."
      },
      {
        "icon": "ShieldCheck",
        "title": "Pack APPCC pastelaria",
        "description": "Rastreabilidade de ovo, cremes, frutos secos e conservação profissional."
      },
      {
        "icon": "Calendar",
        "title": "Gastro Calendar",
        "description": "Bolo Rei, Dia dos Namorados, Páscoa, Natal, comunhões, Dia da Mãe."
      },
      {
        "icon": "Image",
        "title": "GastroIMG Gen+ + Gerador de Pins Pinterest",
        "description": "Fotografia artesanal IA de referência + Pinterest, onde a pastelaria captura tráfego orgânico estável."
      }
    ],
    "workflowTitle": "Um Dia Real de um Confeiteiro com AI Chef Pro",
    "workflow": [
      "06:00 · Abertura — checklist Kit de Tareas Pastelería: refresco de massa mãe, batido de bolos, preparação de cremes.",
      "08:00 · Pastelaria Criativa — desenvolve uma nova sobremesa para o Dia dos Namorados. Culinária Criativa entrega receita + custo de produção CSV.",
      "09:00 · Kit de Escandallos Pro — carrega o CSV com os seus preços reais e custo hora de oficina, valida margem por peça.",
      "11:00 · Produção do dia — modelagem, cozedura, decoração com modelos específicos.",
      "14:00 · Reposição da montra com etiquetas e preços.",
      "16:00 · Gastro Calendar — prepara o planeamento do Bolo Rei com 8 semanas de antecedência.",
      "18:00 · GastroIMG Gen+ + Gerador de Pins Pinterest — gera imagem de referência da nova sobremesa + pins.",
      "20:00 · Encerramento — limpeza profunda, APPCC assinado, planeamento do dia seguinte."
    ],
    "productsTitle": "Modelos e Kits Recomendados para Confeiteiro",
    "productIds": [
      "kit-tareas-pasteleria",
      "kit-escandallos",
      "pack-appcc",
      "kit-inventario",
      "kit-gestion-personal",
      "pro-prompts-ebook"
    ],
    "testimonialQuote": "Pastelaria Criativa + Sosa Ingredients mudaram a minha proposta. As minhas sobremesas signature têm agora técnica documentada que a minha equipa replica com consistência, os custos de produção com custo hora de oficina deram-me 6 pontos a mais de margem e os pedidos de tartes à medida fecham-se numa chamada com proposta profissional.",
    "testimonialAuthor": "Eva Mata",
    "testimonialRole": "Chef pâtissière, pastelaria de autor",
    "faqTitle": "Perguntas Frequentes de Confeiteiros",
    "faqs": [
      {
        "q": "Serve para confeiteiro de restaurante, pasteleiro artesanal ou chef pâtissier de hotel?",
        "a": "Para os três. Pastelaria Criativa cobre desde pastelaria artesanal até alta confeitaria de restaurante com técnica francesa avançada."
      },
      {
        "q": "Cobre técnica avançada (massa folhada, mousses, glaceados)?",
        "a": "Sim. Pastelaria Criativa raciocina como chef pâtissier profissional: massa folhada invertida, massas trabalhadas com técnica, mousses com equilíbrio, glaceados com cobertura técnica."
      },
      {
        "q": "Cobre confeitaria + chocolataria?",
        "a": "Sim. Chocolataria Criativa complementa com bombons, ganaches, pralinés e técnica de temperagem para peças combinadas."
      },
      {
        "q": "Gera conteúdo visual para montra e redes?",
        "a": "Sim. GastroIMG Gen+ gera imagens de referência profissionais; Gerador de Pins Pinterest captura tráfego orgânico estável. Lembre-se de que a imagem IA é de referência visual: a foto definitiva é feita por si com a sua peça real."
      },
      {
        "q": "Como me ajuda com eventos e épocas?",
        "a": "Gastro Calendar planeia as épocas-chave (Bolo Rei, Dia dos Namorados, Páscoa, Natal, comunhões) com antecedência."
      }
    ],
    "ctaTitle": "A sua confeitaria com técnica de autor e margem real.",
    "ctaSubtitle": "Comece com o onboarding de 2 minutos. Plano Membro por 10 € por mês com 10.000 créditos.",
    "seo": {
      "title": "IA para Confeiteiro e Pasteleiro: Técnica, Custos de Produção e Sazonalidade | AI Chef Pro",
      "description": "Suite de IA para confeiteiros profissionais: Pastelaria Criativa, custos de produção com custo hora de oficina, planeamento sazonal e branding. Comece hoje.",
      "keywords": "IA confeiteiro, IA pasteleiro, IA chef pâtissier, software pastelaria, custos de produção pastelaria, técnica francesa, confeitaria de autor",
      "ogImage": "https://aichef.pro/og/use-cases/repostero-pastelero.jpg"
    },
    "personalizationTitle": "Personalizado à Sua Confeitaria desde o Minuto Um",
    "personalizationBody": "AI Chef Pro arranca com o agente «Quem Sou Eu?», um onboarding de 2 minutos em que lhe conta que tipo de confeitaria trabalha (chef pâtissier de restaurante, pasteleiro artesanal, confeiteiro de hotel, confeitaria para eventos), tamanho da equipa, cidade e especialidade.",
    "appsTitle": "Os Agentes IA que Vai Usar como Confeiteiro",
    "apps": [
      {
        "name": "Pastelaria Criativa",
        "category": "Criatividade Culinária",
        "description": "Agente especializado em pastelaria profissional com técnica avançada."
      },
      {
        "name": "Chocolataria Criativa",
        "category": "Criatividade Culinária",
        "description": "Para bombons, ganaches e combinações avançadas."
      },
      {
        "name": "Culinária Criativa",
        "category": "Criatividade Culinária",
        "description": "Desenvolvimento de sobremesas signature com receita + custo de produção CSV."
      },
      {
        "name": "Padaria Criativa",
        "category": "Criatividade Culinária",
        "description": "Para brioche, croissants, ensaimadas e pastelaria complementar."
      },
      {
        "name": "Sosa Ingredients",
        "category": "Fornecedores Gastro",
        "description": "Catálogo Sosa para texturas, gelificantes e técnica avançada."
      },
      {
        "name": "tSpoonLab Agent",
        "category": "Fornecedores Gastro",
        "description": "Assistente do catálogo tSpoonLab para aplicações avançadas."
      },
      {
        "name": "Mermas Genéricas",
        "category": "Ferramentas e Utilitários",
        "description": "Perdas na oficina, modelagem, cozedura e montra."
      },
      {
        "name": "ID Alergénios",
        "category": "Ferramentas e Utilitários",
        "description": "Identificação automática por peça: glúten, laticínios, frutos secos, ovo."
      },
      {
        "name": "GastroIMG Gen+",
        "category": "Gastro Conhecimento",
        "description": "Fotografia artesanal IA de referência para montra, web e redes."
      },
      {
        "name": "InstaFlow AI Pro",
        "category": "Conteúdos e Redes Sociais",
        "description": "Instagram com calendário editorial para confeitaria de autor."
      },
      {
        "name": "Gerador de Pins Pinterest",
        "category": "Conteúdos e Redes Sociais",
        "description": "Pinterest captura tráfego orgânico estável para tartes e sobremesas."
      },
      {
        "name": "Gastro Calendar",
        "category": "Conteúdos e Redes Sociais",
        "description": "Bolo Rei, Dia dos Namorados, Páscoa, Natal, Dia da Mãe."
      }
    ],
    "metrics": [
      {
        "value": "+6 pp",
        "label": "margem após custear as peças"
      },
      {
        "value": "−30 %",
        "label": "perdas na oficina"
      },
      {
        "value": "×2",
        "label": "tráfego orgânico via Pinterest"
      },
      {
        "value": "12+",
        "label": "agentes para a sua oficina"
      }
    ],
    "beforeAfter": {
      "beforeTitle": "Sem AI Chef Pro",
      "beforeItems": [
        "Técnica improvisada, sobremesas signature inconsistentes",
        "Custos de produção sem custo hora de oficina",
        "Perdas na oficina sem rastreabilidade real",
        "Montra e redes improvisadas com fotos do telemóvel",
        "Sazonalidade reativa, chega tarde ao Bolo Rei"
      ],
      "afterTitle": "Com AI Chef Pro",
      "afterItems": [
        "Técnica documentada, sobremesas signature consistentes",
        "Custo de produção profissional com custo hora de oficina integrado",
        "Perdas controladas com Mermas Genéricas",
        "GastroIMG Gen+ + Gerador de Pins Pinterest captam tráfego estável",
        "Bolo Rei e épocas planeadas com 8 semanas de antecedência"
      ]
    },
    "galleryTitle": "Como Funciona a Oficina de um Confeiteiro",
    "gallerySubtitle": "O que vai coordenar com AI Chef Pro: piping, tartes, mise, montra e equipa. Imagens geradas com IA como referência visual do conceito.",
    "galleryImages": [
      "/lovable-uploads/ai-gallery/use-case-repostero-hero.jpg",
      "/lovable-uploads/ai-gallery/use-case-repostero-decoration.jpg",
      "/lovable-uploads/ai-gallery/use-case-repostero-tartas.jpg",
      "/lovable-uploads/ai-gallery/use-case-repostero-mise.jpg",
      "/lovable-uploads/ai-gallery/use-case-repostero-vitrina.jpg",
      "/lovable-uploads/ai-gallery/use-case-repostero-team.jpg"
    ]
  },
  "restaurante-casual": {
    "h1": "IA para Restaurante Casual",
    "heroSubtitle": "Otimize a operação diária, controle o food cost e recupere horas de papelada no seu restaurante casual com uma suite de agentes de IA especializados em restauração.",
    "heroTagline": "O restaurante casual moderno precisa de IA",
    "badge": "Para restaurantes casuais e bistrôs",
    "painsTitle": "O Que um Restaurante Casual Não Pode Deixar de Resolver",
    "pains": [
      "Margem estreita que exige controlo milimétrico de custos e mermas na cozinha",
      "Rotatividade alta de equipa: formar e supervisionar novos cozinheiros e empregados de mesa consome horas todas as semanas",
      "Carta ampla com muitos pratos para fazer escandallos quando os preços dos fornecedores mudam",
      "APPCC e regulamentação sempre em dia sem que a papelada roube tempo à sala",
      "Captar clientes numa zona competitiva: SEO local, redes e avaliações são chave",
      "Coordenar cozinha, sala e delivery nos picos de serviço sem falhas"
    ],
    "featuresTitle": "Como o AI Chef Pro Ajuda num Restaurante Casual",
    "features": [
      {
        "icon": "UtensilsCrossed",
        "title": "Restaurantes Casuais AI+",
        "description": "Agente especializado em bistrôs, gastrobares, tapas e mediterrâneo: o espetro casual completo com base profissional."
      },
      {
        "icon": "Calculator",
        "title": "Escandallos profissionais",
        "description": "Culinária Criativa entrega receita + escandallo CSV; Kit de Escandallos Pro gere com os seus preços reais e margem objetivo."
      },
      {
        "icon": "CheckSquare",
        "title": "Kit de Tareas Restaurante Casual",
        "description": "Modelos prontos: abertura, encerramento, partidas de cozinha, sala, delivery e eventos."
      },
      {
        "icon": "ShieldCheck",
        "title": "APPCC e rastreabilidade",
        "description": "Pack APPCC com 19 registos, registos a partir do telemóvel, alertas e folhas prontas a imprimir em A4 para a inspeção."
      },
      {
        "icon": "Users",
        "title": "Kit Gestión de Personal",
        "description": "Quadrantes em minutos respeitando convenção, descansos, controlo de horas e rácios de produtividade."
      },
      {
        "icon": "Sparkles",
        "title": "MenuDish Local SEO + BlogPost SEO Gen+",
        "description": "Suite de SEO local para captar clientes organicamente sem pagar agência."
      },
      {
        "icon": "BarChart3",
        "title": "Kit Plan Financiero",
        "description": "Dashboard de rácios, food cost, produtividade e ticket médio. Relatório ao proprietário em PDF."
      },
      {
        "icon": "Image",
        "title": "GastroIMG Gen+ + InstaFlow AI Pro",
        "description": "Fotografia gastronómica IA para site e redes, conteúdo para Instagram com calendário editorial."
      },
      {
        "icon": "Search",
        "title": "Keyword Discovery AI+",
        "description": "Investigação de palavras-chave gastronómicas locais por zona postal para posicionamento real."
      }
    ],
    "workflowTitle": "Um Dia Real num Restaurante Casual com AI Chef Pro",
    "workflow": [
      "08:30 · Abertura — checklist do Kit de Tareas Restaurante Casual e controlo de inventário em 10 minutos.",
      "10:00 · Restaurantes Casuais AI+ — pede ao agente sugestões de prato do dia com produto que tem na câmara.",
      "10:30 · Culinária Criativa + Kit de Escandallos Pro — faz o escandallo do prato do dia com os seus preços e valida a margem.",
      "12:30 · Serviço de meio-dia — cozinha, sala e delivery coordenados com modelos. Mermas registadas a partir do telemóvel com APPCC.",
      "15:30 · Kit Plan Financiero — revê KPIs do dia anterior e deteta que o food cost de segunda subiu para 32 %, identifica a causa.",
      "17:00 · MenuDish Local SEO — atualiza as descrições dos 6 pratos top no Google Business e no site.",
      "18:00 · Kit Inventario — valida pedidos a fornecedores com comparação de preços e alertas de stock mínimo.",
      "23:30 · Encerramento — APPCC assinado, relatório diário ao proprietário em PDF direto a partir do Kit Plan Financiero."
    ],
    "productsTitle": "Modelos e Kits Descarregáveis para Restaurante Casual",
    "productIds": [
      "kit-tareas",
      "kit-escandallos",
      "pack-appcc",
      "kit-gestion-personal",
      "kit-inventario",
      "kit-plan-financiero"
    ],
    "testimonialQuote": "Temos 80 lugares e alta rotatividade de pessoal. O Kit de Tareas Restaurante Casual e o Pack APPCC organizaram toda a nossa operação. Vamos como um relógio suíço e o food cost baixou 3 pontos no primeiro trimestre só por fazer escandallos corretamente.",
    "testimonialAuthor": "Sandra López",
    "testimonialRole": "Gerente, restaurante casual mediterrâneo de 80 lugares",
    "faqTitle": "Perguntas Frequentes de Restaurantes Casuais",
    "faqs": [
      {
        "q": "Funciona para restaurantes de 30, 80 ou 150 lugares?",
        "a": "Sim. Os modelos escalam ao volume e os planos adaptam-se ao uso real. Há clientes desde 30 lugares até cadeias de 25 unidades."
      },
      {
        "q": "Cobre delivery além de sala?",
        "a": "Sim. O Kit de Tareas Restaurante Casual inclui modelos específicos para gestão de delivery, mermas associadas e coordenação com plataformas como Glovo, Uber Eats e Just Eat."
      },
      {
        "q": "Substitui o meu TPV ou software de reservas?",
        "a": "Não, complementa. O Cover Manager ou o The Fork gerem reservas e o TPV gere vendas; o AI Chef Pro gere custos, pessoal, APPCC, inventário e SEO local. Os dados são compatíveis via Excel."
      },
      {
        "q": "Quanto tempo demora a equipa a aprender?",
        "a": "Curva real de 1-2 dias. Há vídeo de onboarding de 5 minutos, suporte por WhatsApp e tudo arranca com o agente «Quem Sou Eu?» que adapta o sistema ao seu restaurante em 2 minutos."
      },
      {
        "q": "Como me ajuda com SEO local e captação?",
        "a": "Suite de Conteúdos e Redes Sociais: MenuDish Local SEO (descrições de prato), BlogPost SEO Gen+ (posts de blogue), Keyword Discovery AI+ (palavras-chave por zona postal), InstaFlow AI Pro (Instagram) e Gerador de Pins Pinterest."
      },
      {
        "q": "Há agente específico para o meu tipo de restaurante casual?",
        "a": "Sim. Restaurantes Casuais AI+ cobre bistrôs, gastrobares, tapas, mediterrâneo, mesões, braseria casual. Para conceitos mais específicos há Burger Pro AI+, Food Truck AI+ e agentes por país (mexicana, peruana, japonesa, etc.)."
      }
    ],
    "ctaTitle": "Ponha ordem no seu restaurante casual.",
    "ctaSubtitle": "Comece com o onboarding de 2 minutos. Plano Membro por 10 € por mês com 10.000 créditos para usar todos os agentes.",
    "seo": {
      "title": "IA para Restaurante Casual: Operação, Escandallos e SEO Local | AI Chef Pro",
      "description": "Suite de IA para restaurantes casuais e bistrôs: agentes especializados, escandallos, APPCC, quadrantes, SEO local e marketing com base profissional. Começa hoje.",
      "keywords": "IA restaurante casual, software restaurante casual, gestão bistrô IA, escandallos casual, APPCC restaurante casual, marketing restaurante casual IA, SEO local restaurante, restaurante casual Espanha",
      "ogImage": "https://aichef.pro/og/use-cases/restaurante-casual.jpg"
    },
    "personalizationTitle": "Personalizado para o Seu Restaurante desde o Minuto Um",
    "personalizationBody": "O AI Chef Pro arranca com o agente «Quem Sou Eu?», um onboarding conversacional de 2 minutos em que lhe conta que tipo de casual gere (mediterrâneo, bistrô, gastrobar, mesão, tapas), número de lugares, cidade e forma de trabalhar. A partir desse momento, cada agente —desde Restaurantes Casuais AI+ até MenuDish Local SEO— responde adaptado ao seu contexto: ticket médio da sua zona, regulamentação e operação real.",
    "appsTitle": "Os Agentes de IA que Vai Usar no Seu Restaurante Casual",
    "apps": [
      {
        "name": "Restaurantes Casuais AI+",
        "category": "Conceitos de Negócio",
        "description": "Agente principal: bistrôs, gastrobares, tapas e mediterrâneo com base profissional."
      },
      {
        "name": "Gerente Restaurante Pro",
        "category": "Gastro Profile Pro",
        "description": "Assistente operativo e relatório ao proprietário."
      },
      {
        "name": "Culinária Criativa",
        "category": "Criatividade Culinária",
        "description": "Desenvolvimento de pratos profissionais com receita + escandallo CSV."
      },
      {
        "name": "Mermas Genéricas",
        "category": "Ferramentas e Utilitários",
        "description": "Dados precisos de mermas e rendimentos para controlo de cozinha."
      },
      {
        "name": "ID Alergénios",
        "category": "Ferramentas e Utilitários",
        "description": "Identificação automática de alergénios por receita e prato."
      },
      {
        "name": "Refeição do Pessoal",
        "category": "Gastro Profile Pro",
        "description": "Gerador de menus de staff com produto que já tem na câmara."
      },
      {
        "name": "MenuDish Local SEO",
        "category": "Conteúdos e Redes Sociais",
        "description": "Descrições de prato otimizadas para SEO local."
      },
      {
        "name": "BlogPost SEO Gen+",
        "category": "Conteúdos e Redes Sociais",
        "description": "Posts de blogue para captar tráfego orgânico local."
      },
      {
        "name": "Keyword Discovery AI+",
        "category": "Conteúdos e Redes Sociais",
        "description": "Palavras-chave por zona postal."
      },
      {
        "name": "InstaFlow AI Pro",
        "category": "Conteúdos e Redes Sociais",
        "description": "Conteúdo viral para Instagram com calendário editorial."
      },
      {
        "name": "GastroIMG Gen+",
        "category": "Gastro Conhecimento",
        "description": "Fotografia gastronómica IA para site e redes sociais."
      },
      {
        "name": "Coach Mental",
        "category": "Ferramentas e Utilitários",
        "description": "Coaching para gestão de stress em alta pressão e conversas difíceis."
      }
    ],
    "metrics": [
      {
        "value": "−3 pp",
        "label": "food cost no primeiro trimestre"
      },
      {
        "value": "×2",
        "label": "reservas via SEO local"
      },
      {
        "value": "−6 h",
        "label": "semanais em gestão"
      },
      {
        "value": "12+",
        "label": "agentes para o seu restaurante"
      }
    ],
    "beforeAfter": {
      "beforeTitle": "Sem AI Chef Pro",
      "beforeItems": [
        "Operação em folhas soltas com cada partida a funcionar à sua maneira",
        "APPCC em papel impresso que se perde antes da inspeção",
        "Quadrantes em Excel manual preenchidos durante horas",
        "Marketing improvisado sem captação orgânica de clientes",
        "Food cost a olho, sem saber que prato sangra rentabilidade"
      ],
      "afterTitle": "Com AI Chef Pro",
      "afterItems": [
        "Kit de Tareas com modelos estruturados por turno e partida",
        "APPCC a partir do telemóvel com registos, alertas e exportação para PDF",
        "Quadrantes em minutos com o Kit Gestión de Personal respeitando convenção",
        "Suite de SEO local a captar reservas orgânicas sem gasto em agências",
        "Food cost por prato calculado ao detalhe com escandallo profissional"
      ]
    },
    "galleryTitle": "Como Funciona um Restaurante Casual Moderno",
    "gallerySubtitle": "O que vai coordenar com o AI Chef Pro: sala, cozinha aberta, esplanada, prato do dia, equipa e bar.",
    "galleryImages": [
      "/lovable-uploads/ai-gallery/use-case-casual-hero.jpg",
      "/lovable-uploads/ai-gallery/use-case-casual-kitchen.jpg",
      "/lovable-uploads/ai-gallery/use-case-casual-terrace.jpg",
      "/lovable-uploads/ai-gallery/use-case-casual-dish.jpg",
      "/lovable-uploads/ai-gallery/use-case-casual-team.jpg",
      "/lovable-uploads/ai-gallery/use-case-casual-bar.jpg"
    ]
  },
  "cafeteria-brunch": {
    "h1": "IA para Cafetaria e Brunch",
    "heroSubtitle": "Otimize pequenos-almoços, brunch, café de especialidade e pastelaria com uma suite de agentes de IA pensados para coffee shops, locais de brunch e cafetarias modernas.",
    "heroTagline": "Coffee shop moderno com operação moderna",
    "badge": "Para cafetarias de especialidade e brunch",
    "painsTitle": "O Que um Coffee Shop ou Local de Brunch Não Pode Deixar de Resolver",
    "pains": [
      "Carta curta mas rotação altíssima nas horas de pico da manhã e do meio-dia",
      "Margem muito apertada em café de especialidade e pastelaria com custo de leite e cacau volátil",
      "Equipa jovem e rotativa que precisa de formação rápida em barra e serviço",
      "Branding e redes sociais (Instagram, Pinterest) são a principal alavanca de captação",
      "Diferenciar-se numa zona concorrida com pricing premium mas acessível",
      "Gerir o fluxo de brunch aos fins de semana sem colapsar a operação durante a semana"
    ],
    "featuresTitle": "Como o AI Chef Pro Ajuda numa Cafetaria de Brunch",
    "features": [
      {
        "icon": "Coffee",
        "title": "Restaurantes Casuais AI+",
        "description": "Agente com conhecimento de coffee shops, brunch e cafetaria de especialidade: cartas, pricing e operação."
      },
      {
        "icon": "Calculator",
        "title": "Escandallos de café, brunch e pastelaria",
        "description": "Culinária Criativa entrega receita + escandallo CSV; Kit de Escandallos Pro gere-o com os seus preços reais."
      },
      {
        "icon": "Sparkles",
        "title": "Pastelaria Criativa + Padaria Criativa",
        "description": "Receitas profissionais para pastelaria, brioche, croissants, bolos e padaria artesanal."
      },
      {
        "icon": "CheckSquare",
        "title": "Kit de Tareas Cafetería",
        "description": "Modelos específicos: abertura, encerramento, barra, cozinha ligeira, brunch, serviço e limpeza."
      },
      {
        "icon": "ShieldCheck",
        "title": "APPCC simplificado",
        "description": "Pack APPCC com registos mínimos mas completos para cafetaria: leite, conservação, lavagem, temperaturas."
      },
      {
        "icon": "Image",
        "title": "GastroIMG Gen+ + InstaFlow AI Pro",
        "description": "Fotografia gastronómica IA + conteúdo Instagram com captions, calendário editorial e planeamento."
      },
      {
        "icon": "Search",
        "title": "Gerador de Pins Pinterest",
        "description": "O Pinterest é chave para coffee shops: pins de brunch, café latte art e pastelaria para captar tráfego orgânico."
      },
      {
        "icon": "BarChart3",
        "title": "KPIs e ticket médio",
        "description": "Kit Plan Financiero: taxa de ocupação, ticket médio, produtividade e upselling de brunch e café."
      },
      {
        "icon": "Search",
        "title": "Keyword Discovery AI+",
        "description": "Palavras-chave gastronómicas locais para «brunch [o seu bairro]», «café especialidade perto» e semelhantes."
      }
    ],
    "workflowTitle": "Um Dia Real numa Cafetaria de Brunch com AI Chef Pro",
    "workflow": [
      "07:00 · Abertura — checklist do Kit de Tareas Cafetería: barra ligada, café moído, leite frio, vitrine pronta.",
      "08:00 · Serviço da manhã — pequenos-almoços e café de especialidade com fluxo coordenado entre barra e cozinha ligeira.",
      "11:00 · Culinária Criativa — desenvolve um novo brunch para sábado: tostas com burrata, gravlax e ovos. Recebe escandallo CSV.",
      "11:30 · Kit de Escandallos Pro — carrega o CSV com preços reais e valida a margem objetivo (32 %).",
      "13:00 · Serviço do meio-dia — brunch em marcha, equipa coordenada com modelos específicos.",
      "16:00 · GastroIMG Gen+ + Gerador de Pins Pinterest — gera fotografias do novo brunch e pins otimizados para Pinterest.",
      "17:30 · InstaFlow AI Pro — programa publicações de Instagram para a próxima semana com calendário editorial.",
      "19:30 · Encerramento — limpeza profunda, APPCC assinado, planeamento da pastelaria para o dia seguinte."
    ],
    "productsTitle": "Modelos e Kits Descarregáveis para Cafetarias",
    "productIds": [
      "kit-tareas-cafeteria",
      "kit-escandallos",
      "pack-appcc",
      "kit-gestion-personal",
      "kit-inventario",
      "pro-prompts-ebook"
    ],
    "testimonialQuote": "Temos brunch aos fins de semana e café de especialidade durante a semana. O Kit de Tareas Cafetería e a geração de conteúdo para Instagram devolveram-me as tardes. O Gerador de Pins Pinterest foi uma descoberta: trouxe-nos tráfego orgânico que nunca tinha visto.",
    "testimonialAuthor": "Marcos Rivera",
    "testimonialRole": "Proprietário, coffee shop de especialidade e brunch",
    "faqTitle": "Perguntas Frequentes de Coffee Shops",
    "faqs": [
      {
        "q": "Serve para café de especialidade ou apenas cafetaria casual?",
        "a": "Serve para ambos. Há modelos adaptáveis tanto para coffee shops de especialidade (V60, espresso de origem, latte art) como para cafetarias casuais e brunch."
      },
      {
        "q": "Funciona para locais com cozinha muito ligeira?",
        "a": "Sim. O Kit de Tareas Cafetería tem modelos específicos para cozinha ligeira, brunch e barra, sem assumir que tem brigada completa."
      },
      {
        "q": "Gera conteúdo otimizado para Instagram e Pinterest?",
        "a": "Sim. O InstaFlow AI Pro e o Gerador de Pins Pinterest são agentes específicos para esses canais. O Pinterest funciona muito bem para brunch e café com tráfego orgânico estável."
      },
      {
        "q": "Cobre delivery e horários alargados?",
        "a": "Sim. Os modelos são adaptáveis a horário, delivery, take-away e catering ligeiro (coffee break corporativo)."
      },
      {
        "q": "Como otimiza o SEO local para o meu coffee shop?",
        "a": "MenuDish Local SEO + BlogPost SEO Gen+ + Keyword Discovery AI+ trabalham juntos para captar pesquisas locais como «brunch em [a sua zona]» ou «melhor café de especialidade perto»."
      }
    ],
    "ctaTitle": "A sua cafetaria com operação afinada e captação orgânica.",
    "ctaSubtitle": "Comece com o onboarding de 2 minutos. Plano Membro por 10 € por mês com 10.000 créditos para usar todos os agentes.",
    "seo": {
      "title": "IA para Cafetaria e Brunch: Operação, Pinterest e SEO Local | AI Chef Pro",
      "description": "Suite de IA para coffee shops e locais de brunch: agentes especializados, escandallos, APPCC, conteúdo para Instagram e Pinterest, SEO local. Comece hoje.",
      "keywords": "IA cafetaria, brunch software, IA coffee shop, gestão cafetaria especialidade, escandallos café, marketing cafetaria IA, Pinterest brunch, SEO local cafetaria, coffee shop Portugal",
      "ogImage": "https://aichef.pro/og/use-cases/cafeteria-brunch.jpg"
    },
    "personalizationTitle": "Personalizado para o Seu Coffee Shop desde o Primeiro Minuto",
    "personalizationBody": "O AI Chef Pro arranca com o agente «Quem Sou Eu?», um onboarding conversacional de 2 minutos em que lhe conta que tipo de cafetaria gere (especialidade, brunch, casual), cidade e forma de trabalhar. A partir desse momento, cada agente — desde Pastelaria Criativa até Gerador de Pins Pinterest — responde adaptado ao seu contexto: ticket médio da sua zona, perfil de cliente e operação real.",
    "appsTitle": "Os Agentes de IA que Vai Usar na Sua Cafetaria",
    "apps": [
      {
        "name": "Restaurantes Casuais AI+",
        "category": "Conceitos de Negócio",
        "description": "Agente principal: coffee shops, brunch e cafetaria com base profissional."
      },
      {
        "name": "Pastelaria Criativa",
        "category": "Criatividade Culinária",
        "description": "Receitas profissionais para pastelaria de cafetaria: brioche, croissants, bolos, tartes."
      },
      {
        "name": "Padaria Criativa",
        "category": "Criatividade Culinária",
        "description": "Para coffee shops que cozem o seu próprio pão e pastelaria com massa mãe."
      },
      {
        "name": "Culinária Criativa",
        "category": "Criatividade Culinária",
        "description": "Desenvolvimento de pratos de brunch com receita + escandallo CSV."
      },
      {
        "name": "ID Alergénios",
        "category": "Ferramentas e Utilitários",
        "description": "Identificação automática de alergénios por receita."
      },
      {
        "name": "Refeição do Pessoal",
        "category": "Gastro Profile Pro",
        "description": "Gerador de menus de staff que motivam a equipa."
      },
      {
        "name": "MenuDish Local SEO",
        "category": "Conteúdos e Redes Sociais",
        "description": "Descrições SEO local para melhorar posicionamento."
      },
      {
        "name": "BlogPost SEO Gen+",
        "category": "Conteúdos e Redes Sociais",
        "description": "Publicações de blog para captar tráfego orgânico para o coffee shop."
      },
      {
        "name": "Keyword Discovery AI+",
        "category": "Conteúdos e Redes Sociais",
        "description": "Palavras-chave por zona postal: brunch, café especialidade, etc."
      },
      {
        "name": "InstaFlow AI Pro",
        "category": "Conteúdos e Redes Sociais",
        "description": "Conteúdo viral Instagram com calendário editorial."
      },
      {
        "name": "Gerador de Pins Pinterest",
        "category": "Conteúdos e Redes Sociais",
        "description": "Pins otimizados para Pinterest: brunch, café, pastelaria."
      },
      {
        "name": "GastroIMG Gen+",
        "category": "Gastro Conhecimento",
        "description": "Fotografia gastronómica IA para web, redes e carta."
      }
    ],
    "metrics": [
      {
        "value": "×3",
        "label": "tráfego orgânico via Pinterest"
      },
      {
        "value": "+ €1,80",
        "label": "ticket médio por upselling"
      },
      {
        "value": "−4 h",
        "label": "semanais em gestão de redes"
      },
      {
        "value": "12+",
        "label": "agentes para a sua cafetaria"
      }
    ],
    "beforeAfter": {
      "beforeTitle": "Sem AI Chef Pro",
      "beforeItems": [
        "Operação de barra e cozinha ligeira improvisada em cada turno",
        "Escandallos a olho em café e pastelaria com margem incerta",
        "Instagram caótico sem calendário editorial nem continuidade",
        "Sem presença no Pinterest, perdendo o tráfego orgânico que mais converte para brunch",
        "APPCC em caderno que se esquece na inspeção"
      ],
      "afterTitle": "Com AI Chef Pro",
      "afterItems": [
        "Kit de Tareas Cafetería com modelos específicos por turno e secção",
        "Escandallo profissional em cada bebida e prato com margem real",
        "InstaFlow AI Pro com calendário editorial e captions otimizadas",
        "Gerador de Pins Pinterest a captar tráfego orgânico estável e de alta conversão",
        "APPCC a partir do telemóvel com registos prontos para inspeção"
      ]
    },
    "galleryTitle": "Como Funciona uma Cafetaria de Brunch Moderna",
    "gallerySubtitle": "O que vai coordenar com AI Chef Pro: especialidade e brunch, barista, pastelaria, equipa de turno e conteúdo para redes sociais.",
    "galleryImages": [
      "/lovable-uploads/ai-gallery/use-case-cafeteria-hero.jpg",
      "/lovable-uploads/ai-gallery/use-case-cafeteria-brunch.jpg",
      "/lovable-uploads/ai-gallery/use-case-cafeteria-barista.jpg",
      "/lovable-uploads/ai-gallery/use-case-cafeteria-pastry.jpg",
      "/lovable-uploads/ai-gallery/use-case-cafeteria-team.jpg",
      "/lovable-uploads/ai-gallery/use-case-cafeteria-instagram.jpg"
    ]
  },
  "pizzeria": {
    "h1": "IA para Pizzaria",
    "heroSubtitle": "Estandardiza massa mãe, calcula escandallos por pizza, controla delivery e multi-marca com uma suite de agentes de IA especializados em pizzaria profissional, pizza napolitana, romana e americana.",
    "heroTagline": "Pizza com margem real, técnica com sistema",
    "badge": "Para pizzarias e pizzaioli",
    "painsTitle": "O Que uma Pizzaria Não Pode Deixar de Resolver",
    "pains": [
      "Margem muito ajustada em pizza com controlo milimétrico de gramagem em massa, molho, queijo e toppings",
      "Mermas em massa mãe, mozzarella e molhos que sangram rentabilidade sem controlo",
      "Picos de procura em delivery (12:30-14:30, 20:30-22:30) sem margem para erros",
      "Carta ampla de pizzas com escandallo individualizado por variante",
      "Estandardizar massa e técnica em cozinhas onde roda a equipa de pizzaioli",
      "Captar clientes locais com SEO e redes para reduzir dependência de plataformas de delivery"
    ],
    "featuresTitle": "Como AI Chef Pro Ajuda numa Pizzaria",
    "features": [
      {
        "icon": "Pizza",
        "title": "Cozinha Italiana",
        "description": "Agente especializado em cozinha italiana profissional, massas, molhos e técnica de pizzaria napolitana, romana e americana."
      },
      {
        "icon": "Beaker",
        "title": "Fermentus Con AI+",
        "description": "Para massas mãe, fermentações longas, hidratações altas e técnica de panificação aplicada a pizza profissional."
      },
      {
        "icon": "Calculator",
        "title": "Escandallos por pizza",
        "description": "Culinária Criativa entrega receita + escandallo CSV; Kit de Escandallos Pro gere-o com os seus preços reais e margem objetivo por variante."
      },
      {
        "icon": "CheckSquare",
        "title": "Kit de Tareas Pizzería",
        "description": "Modelos: hidratação de massa, preparação de molhos, mise de toppings, serviço no local e delivery."
      },
      {
        "icon": "ShieldCheck",
        "title": "Pack APPCC",
        "description": "Modelos adaptados a pizzaria: temperaturas de forno, conservação de massa mãe, rastreabilidade para delivery."
      },
      {
        "icon": "Truck",
        "title": "Burger Pro AI+ + Food Truck AI+",
        "description": "Se opera dark kitchen multi-marca, também agentes complementares para delivery especializado."
      },
      {
        "icon": "Sparkles",
        "title": "MenuDish Local SEO + InstaFlow AI Pro",
        "description": "Posicionamento local no Google e conteúdo viral para Instagram com calendário editorial."
      },
      {
        "icon": "Image",
        "title": "GastroIMG Gen+",
        "description": "Fotografia gastronómica IA para Glovo, Uber Eats, Just Eat e web do restaurante."
      },
      {
        "icon": "Users",
        "title": "Kit Gestión de Personal",
        "description": "Escalas para pizzaioli, sala e delivery com turnos rotativos e picos de serviço."
      }
    ],
    "workflowTitle": "Um Dia Real numa Pizzaria com AI Chef Pro",
    "workflow": [
      "08:00 · Abertura — checklist Kit de Tareas Pizzería: hidratação de massa mãe, preparação de molho de tomate, mise de toppings.",
      "10:00 · Cozinha Italiana + Fermentus Con AI+ — desenvolve uma nova pizza de época com massa de hidratação 75 % e fermentação 48 h.",
      "11:00 · Kit de Escandallos Pro — escandala a nova pizza com os seus preços reais (farinha, mozzarella, prosciutto) e valida margem de 32%.",
      "12:30 · Serviço meio-dia — pizzaiolo no forno, sala cheia, delivery ativo com modelos específicos.",
      "15:30 · Inventário — valida pedidos de farinha italiana, mozzarella di bufala e conservas com o Kit Inventario.",
      "17:00 · MenuDish Local SEO — atualiza as descrições das pizzas top no Google Business e na web.",
      "20:00 · Serviço noite — pico de delivery, pizzaiolo ao forno coordenado com sala e motoristas.",
      "23:30 · Encerramento — limpeza, APPCC assinado, relatório do dia ao proprietário."
    ],
    "productsTitle": "Modelos e Kits Descarregáveis para Pizzaria",
    "productIds": [
      "kit-tareas-pizzeria",
      "kit-escandallos",
      "pack-appcc",
      "kit-inventario",
      "kit-gestion-personal",
      "pro-prompts-ebook"
    ],
    "testimonialQuote": "Fizemos escandallo pizza a pizza com o Kit de Escandallos Pro e descobrimos que 4 variantes estavam em perdas porque pesava demasiado mozzarella. Ajustámos gramagem e preço. A margem do local subiu 4 pontos em 2 meses sem tocar na qualidade.",
    "testimonialAuthor": "Giovanni Russo",
    "testimonialRole": "Pizzaiolo e proprietário, pizzaria napolitana",
    "faqTitle": "Perguntas Frequentes de Pizzarias",
    "faqs": [
      {
        "q": "Serve para pizza napolitana, romana, americana ou detroit?",
        "a": "Para todas. Cozinha Italiana e Fermentus Con AI+ cobrem o espetro completo de massas, hidratações, fermentações e técnicas de cada estilo."
      },
      {
        "q": "Cobre delivery além de local?",
        "a": "Sim. O Kit de Tareas Pizzería inclui modelos específicos de delivery com tempos, mermas associadas e coordenação com plataformas (Glovo, Uber Eats, Just Eat)."
      },
      {
        "q": "Funciona para 1 local ou cadeia de pizzarias?",
        "a": "Ambos. Há clientes com 1 local e outros com mais de 12 unidades ativas. Para grupos, Chef Executivo Pro estandardiza receitas e manuais."
      },
      {
        "q": "Gera ideias de promoções para dias fracos?",
        "a": "Sim. Gastro Calendar + InstaFlow AI Pro geram combos, ofertas, calendário editorial e campanhas sazonais com criatividade profissional."
      },
      {
        "q": "Como me ajuda com massa mãe profissional?",
        "a": "Fermentus Con AI+ é referência em fermentação: hidratações, prefermentos (poolish, biga, tang zhong), refrescos de massa mãe e técnicas de fermentação controlada."
      }
    ],
    "ctaTitle": "Pizza com margem real, não intuição.",
    "ctaSubtitle": "Comece com o onboarding de 2 minutos. Plano Membro por 10 € por mês com 10.000 créditos para usar todos os agentes.",
    "seo": {
      "title": "IA para Pizzaria: Massa Mãe, Escandallos por Pizza e Delivery | AI Chef Pro",
      "description": "Suite de IA para pizzarias profissionais: Cozinha Italiana, Fermentus para massas, escandallos por pizza, modelos pizza-shop e SEO local. Comece hoje.",
      "keywords": "IA pizzaria, escandallos pizza, software pizzaria, massa mãe pizza IA, pizza napolitana IA, pizza romana IA, gestão pizzaria delivery, pizzaria Espanha",
      "ogImage": "https://aichef.pro/og/use-cases/pizzeria.jpg"
    },
    "personalizationTitle": "Personalizado para a Sua Pizzaria desde o Minuto Um",
    "personalizationBody": "AI Chef Pro arranca com o agente «Quem Sou Eu?», um onboarding conversacional de 2 minutos em que lhe conta que tipo de pizzaria opera (napolitana, romana, americana, detroit, alla pala), número de lugares, cidade e operativa. A partir desse momento, cada agente —desde Cozinha Italiana até MenuDish Local SEO— responde adaptado ao seu estilo de massa, plataformas de delivery e mercado local.",
    "appsTitle": "Os Agentes de IA que Vai Usar na Sua Pizzaria",
    "apps": [
      {
        "name": "Cozinha Italiana",
        "category": "Receituários por país",
        "description": "Agente especializado em cozinha italiana profissional com base de pizzaria napolitana e romana."
      },
      {
        "name": "Fermentus Con AI+",
        "category": "Criatividade Culinária",
        "description": "Massa mãe, hidratações altas e fermentações longas com apoio profissional."
      },
      {
        "name": "Culinária Criativa",
        "category": "Criatividade Culinária",
        "description": "Desenvolvimento de pizzas criativas com receita + escandallo CSV."
      },
      {
        "name": "Restaurantes Casuais AI+",
        "category": "Conceitos de Negócio",
        "description": "Para coordenar o resto do menu casual da pizzaria (entradas, sobremesas)."
      },
      {
        "name": "Mermas Genéricas",
        "category": "Ferramentas e Utilitários",
        "description": "Dados precisos de mermas em massa, mozzarella e toppings."
      },
      {
        "name": "ID Alergénios",
        "category": "Ferramentas e Utilitários",
        "description": "Identificação automática de alergénios por pizza e prato."
      },
      {
        "name": "MenuDish Local SEO",
        "category": "Conteúdos e Redes Sociais",
        "description": "Descrições SEO local para melhorar posicionamento web e delivery."
      },
      {
        "name": "BlogPost SEO Gen+",
        "category": "Conteúdos e Redes Sociais",
        "description": "Posts de blogue para captar tráfego orgânico local."
      },
      {
        "name": "Keyword Discovery AI+",
        "category": "Conteúdos e Redes Sociais",
        "description": "Palavras-chave por zona postal: «pizza napolitana [o teu bairro]»."
      },
      {
        "name": "InstaFlow AI Pro",
        "category": "Conteúdos e Redes Sociais",
        "description": "Conteúdo viral Instagram com fotos de pizza e calendário editorial."
      },
      {
        "name": "GastroIMG Gen+",
        "category": "Conhecimento Gastronómico",
        "description": "Fotografia gastronómica IA para web e plataformas de delivery."
      }
    ],
    "metrics": [
      {
        "value": "+4 pp",
        "label": "margem após escandallar pizza a pizza"
      },
      {
        "value": "×2",
        "label": "tráfego delivery via SEO local"
      },
      {
        "value": "−25 %",
        "label": "mermas com controlo sistemático"
      },
      {
        "value": "11+",
        "label": "agentes para a sua pizzaria"
      }
    ],
    "beforeAfter": {
      "beforeTitle": "Sem AI Chef Pro",
      "beforeItems": [
        "Massa mãe e técnica dispersos em caderno do pizzaiolo principal",
        "Escandallos a olho, gramagens que variam entre pizzaioli",
        "Mermas de mozzarella e massa sem controlo real",
        "Posicionamento fraco em delivery por descrições genéricas",
        "Operativa de delivery improvisada em horas de pico"
      ],
      "afterTitle": "Com AI Chef Pro",
      "afterItems": [
        "Cozinha Italiana + Fermentus Con AI+ documentam massa e técnica replicável",
        "Escandallo profissional por pizza com margem validada",
        "Mermas controladas com Mermas Genéricas e modelos específicos",
        "SEO local otimizado com MenuDish Local SEO + Keyword Discovery",
        "Kit de Tareas Pizzería com modelos para delivery, local e picos"
      ]
    },
    "galleryTitle": "Como Funciona uma Pizzaria Profissional",
    "gallerySubtitle": "O que vai coordenar com AI Chef Pro: forno, massa mãe, pizza ao detalhe, preparação de toppings, equipa e delivery.",
    "galleryImages": [
      "/lovable-uploads/ai-gallery/use-case-pizzeria-hero.jpg",
      "/lovable-uploads/ai-gallery/use-case-pizzeria-oven.jpg",
      "/lovable-uploads/ai-gallery/use-case-pizzeria-dough.jpg",
      "/lovable-uploads/ai-gallery/use-case-pizzeria-pizza.jpg",
      "/lovable-uploads/ai-gallery/use-case-pizzeria-toppings.jpg",
      "/lovable-uploads/ai-gallery/use-case-pizzeria-delivery.jpg"
    ]
  },
  "hamburgueseria": {
    "h1": "IA para Hamburguesaria",
    "heroSubtitle": "Custo por burger, controlo do custo de carne e pão, gestão de delivery e multi-marca com uma suite de agentes de IA especializados em smash burger gourmet, fast casual e dark kitchen de burger.",
    "heroTagline": "Burger com margem real, não intuição",
    "badge": "Para hamburguesarias e burger shops",
    "painsTitle": "O Que uma Hamburguesaria Não Pode Deixar de Resolver",
    "pains": [
      "Carne e pão: insumos-chave com custo volátil que muda todas as semanas",
      "Mermas na confeção de carne, montagem e embalagem para delivery",
      "Delivery com altíssima rotação e picos brutais em horas específicas",
      "Carta ampla com muitas variantes de burger (clássica, gourmet, smash, plant-based)",
      "Diferenciar-se num mercado saturado de burger shops com SEO local e redes",
      "Padronizar técnica de chapa e montagem quando a equipa roda"
    ],
    "featuresTitle": "Como o AI Chef Pro Ajuda numa Hamburguesaria",
    "features": [
      {
        "icon": "Beef",
        "title": "Burger Pro AI+",
        "description": "Agente especializado em hamburguesarias: gourmet, smash, fast food, plant-based, artesanal e temáticas."
      },
      {
        "icon": "Calculator",
        "title": "Custos por burger",
        "description": "Culinária Criativa entrega receita + ficha técnica CSV; Kit de Escandallos Pro gere com os seus preços reais (carne, pão, queijo, toppings, molhos)."
      },
      {
        "icon": "CheckSquare",
        "title": "Kit de Tareas Hamburguesería",
        "description": "Modelos: preparação de molhos, mise de toppings, chapa, montagem, serviço e delivery."
      },
      {
        "icon": "ShieldCheck",
        "title": "Pack APPCC + ID Alergénios",
        "description": "Rastreabilidade da carne, controlo de confeção, temperatura e alergénios por burger."
      },
      {
        "icon": "Truck",
        "title": "Gestão multi-plataforma delivery",
        "description": "Plano financeiro com cálculo de margem após comissões de Glovo, Uber Eats e Just Eat por marca virtual."
      },
      {
        "icon": "Leaf",
        "title": "VegChef Plant-Based",
        "description": "Para burgers vegetais com técnica nutricional: Beyond Meat, Heura, alternativas plant-based de qualidade."
      },
      {
        "icon": "Sparkles",
        "title": "MenuDish Local SEO + InstaFlow AI Pro",
        "description": "Posicionamento local no Google e conteúdo viral para Instagram, onde as burger shops mais vendem."
      },
      {
        "icon": "Image",
        "title": "GastroIMG Gen+",
        "description": "Fotografia gastronómica IA crítica para Glovo, Uber Eats e Just Eat: melhor foto = mais cliques e melhor ranking."
      },
      {
        "icon": "Users",
        "title": "Kit Gestión de Personal",
        "description": "Quadrantes para chapa, montagem, sala e delivery com turnos rotativos."
      }
    ],
    "workflowTitle": "Um Dia Real numa Hamburguesaria com AI Chef Pro",
    "workflow": [
      "11:00 · Abertura — checklist Kit de Tareas Hamburguesería: preparação de molhos caseiros, mise de toppings, chapa pronta.",
      "12:00 · Burger Pro AI+ — desenvolve uma nova burger gourmet com queijo de cabra e compota de cebola. Culinária Criativa entrega receita + ficha técnica CSV.",
      "12:30 · Kit de Escandallos Pro — carrega o CSV com os seus preços reais e valida margem a 31% após comissão Glovo (29%).",
      "13:00 · Serviço de meio-dia — chapa ativa, montagem coordenada, delivery a sair, sala cheia.",
      "16:00 · MenuDish Local SEO + GastroIMG Gen+ — atualiza a nova burger nas plataformas com foto profissional e descrição otimizada.",
      "17:30 · Inventário — valida pedidos de carne (fornecedor local), pão brioche e queijo premium.",
      "20:00 · Serviço noturno — pico de delivery, montagem em cadeia, chapa no máximo.",
      "23:30 · Encerramento — limpeza, APPCC assinado, relatório do dia e mermas registadas."
    ],
    "productsTitle": "Modelos e Kits Descarregáveis para Hamburguesaria",
    "productIds": [
      "kit-tareas-hamburgueseria",
      "kit-escandallos",
      "pack-appcc",
      "kit-inventario",
      "kit-gestion-personal",
      "pro-prompts-ebook"
    ],
    "testimonialQuote": "Reduzimos o food cost de 36% para 31% em 60 dias com custos precisos e controlo sistemático de mermas. O investimento em AI Chef Pro pagou-se numa semana só com isso. A foto IA para Glovo subiu o nosso ranking do 8.º para o 3.º lugar.",
    "testimonialAuthor": "Pablo Hernández",
    "testimonialRole": "Proprietário, hamburguesaria gourmet com 2 marcas em delivery",
    "faqTitle": "Perguntas Frequentes de Hamburguesarias",
    "faqs": [
      {
        "q": "Funciona para hamburguesaria gourmet, smash ou casual?",
        "a": "Para todas. Burger Pro AI+ cobre o espetro completo: gourmet, smash burger, fast food, plant-based e temáticas."
      },
      {
        "q": "Cobre delivery além do local?",
        "a": "Sim. Modelos específicos com mermas de delivery, embalagem com marca, coordenação com plataformas e cálculo de margem após comissões."
      },
      {
        "q": "Há controlo específico de carne e rastreabilidade?",
        "a": "Sim. Pack APPCC com rastreabilidade da carne, controlo de confeção no ponto, temperatura interna e conservação."
      },
      {
        "q": "Gera ideias de combos e promoções?",
        "a": "Sim. Gastro Calendar + InstaFlow + Pro Prompts eBook geram combos, ofertas para dias fracos, calendário editorial e campanhas com IA."
      },
      {
        "q": "Serve para abrir uma marca virtual de burger em dark kitchen?",
        "a": "Sim. Burger Pro AI+ + Restaurantes Casuais AI+ + Food Truck AI+ são combináveis para multi-marca virtual. Há caso real em /usos/conceito/dark-kitchen."
      }
    ],
    "ctaTitle": "Burger com margem real, não intuição.",
    "ctaSubtitle": "Comece com o onboarding de 2 minutos. Plano Membro por 10 € por mês com 10.000 créditos para usar todos os agentes.",
    "seo": {
      "title": "IA para Hamburguesaria: Custos, Smash Burger e Delivery | AI Chef Pro",
      "description": "Suite de IA para hamburguesarias profissionais: Burger Pro AI+, custos por burger, modelos burger-shop, APPCC e delivery multi-plataforma. Comece hoje.",
      "keywords": "IA hamburguesaria, custos burger, software hamburguesaria, smash burger IA, gestão burger delivery, hamburguesaria gourmet IA, hamburguesaria Espanha",
      "ogImage": "https://aichef.pro/og/use-cases/hamburgueseria.jpg"
    },
    "personalizationTitle": "Personalizado para a Sua Hamburguesaria desde o Primeiro Minuto",
    "personalizationBody": "O AI Chef Pro arranca com o agente «Quem Sou Eu?», um onboarding conversacional de 2 minutos em que lhe conta que tipo de hamburguesaria opera (gourmet, smash, fast casual, plant-based), número de lugares, cidade, plataformas de delivery e comissões. Cada agente — desde Burger Pro AI+ até ao Kit de Escandallos Pro — responde adaptado ao seu estilo e mercado real.",
    "appsTitle": "Os Agentes de IA que Vai Usar na Sua Hamburguesaria",
    "apps": [
      {
        "name": "Burger Pro AI+",
        "category": "Conceitos de Negócio",
        "description": "Agente especializado em hamburguesarias: gourmet, smash, fast food, plant-based."
      },
      {
        "name": "Culinária Criativa",
        "category": "Criatividade Culinária",
        "description": "Desenvolvimento de burgers profissionais com receita + ficha técnica CSV."
      },
      {
        "name": "VegChef Plant-Based",
        "category": "Criatividade Culinária",
        "description": "Para burgers vegetais com técnica nutricional profissional."
      },
      {
        "name": "Food Truck AI+",
        "category": "Conceitos de Negócio",
        "description": "Para conceitos móveis e dark kitchen multi-marca de burger."
      },
      {
        "name": "Mermas Genéricas",
        "category": "Ferramentas e Utilitários",
        "description": "Dados precisos de mermas na confeção de carne e montagem."
      },
      {
        "name": "ID Alergénios",
        "category": "Ferramentas e Utilitários",
        "description": "Identificação automática de alergénios por burger e molho."
      },
      {
        "name": "MenuDish Local SEO",
        "category": "Conteúdos e Redes Sociais",
        "description": "Descrições SEO local para Glovo, Uber Eats e web."
      },
      {
        "name": "BlogPost SEO Gen+",
        "category": "Conteúdos e Redes Sociais",
        "description": "Posts de blogue para captar pesquisas locais de burger."
      },
      {
        "name": "Keyword Discovery AI+",
        "category": "Conteúdos e Redes Sociais",
        "description": "Palavras-chave por zona postal: «smash burger [o seu bairro]»."
      },
      {
        "name": "InstaFlow AI Pro",
        "category": "Conteúdos e Redes Sociais",
        "description": "Conteúdo viral Instagram para hamburguesarias."
      },
      {
        "name": "GastroIMG Gen+",
        "category": "Conhecimento Gastronómico",
        "description": "Fotografia gastronómica IA para plataformas de delivery."
      }
    ],
    "metrics": [
      {
        "value": "−5 pp",
        "label": "food cost em 60 dias"
      },
      {
        "value": "+5",
        "label": "posições no ranking Glovo"
      },
      {
        "value": "×3",
        "label": "velocidade de lançamento de nova burger"
      },
      {
        "value": "11+",
        "label": "agentes para a sua burger shop"
      }
    ],
    "beforeAfter": {
      "beforeTitle": "Sem AI Chef Pro",
      "beforeItems": [
        "Custos a olho com gramagem variável entre cozinheiros",
        "Food cost a 36% por mermas e montagem sem controlo",
        "Fotos no Glovo e Uber Eats de baixa qualidade, ranking baixo",
        "Mermas de carne e montagem sem rastreabilidade",
        "Operação de delivery improvisada em horas de pico"
      ],
      "afterTitle": "Com AI Chef Pro",
      "afterItems": [
        "Burger Pro AI+ + Culinária Criativa documentam técnica replicável",
        "Food cost a 31% com ficha técnica profissional e mermas controladas",
        "Fotos profissionais com GastroIMG Gen+ a subir ranking nas plataformas",
        "Pack APPCC com rastreabilidade de carne e mermas registadas",
        "Kit de Tareas Hamburguesería com modelos para delivery e local"
      ]
    },
    "galleryTitle": "Como Funciona uma Hamburguesaria Moderna",
    "gallerySubtitle": "O que vai coordenar com AI Chef Pro: chapa, smash burger, montagem, preparação, equipa e delivery.",
    "galleryImages": [
      "/lovable-uploads/ai-gallery/use-case-hamburgueseria-hero.jpg",
      "/lovable-uploads/ai-gallery/use-case-hamburgueseria-grill.jpg",
      "/lovable-uploads/ai-gallery/use-case-hamburgueseria-burger.jpg",
      "/lovable-uploads/ai-gallery/use-case-hamburgueseria-prep.jpg",
      "/lovable-uploads/ai-gallery/use-case-hamburgueseria-team.jpg",
      "/lovable-uploads/ai-gallery/use-case-hamburgueseria-delivery.jpg"
    ]
  },
  "dark-kitchen": {
    "h1": "IA para Dark Kitchen e Cozinhas Virtuais",
    "heroSubtitle": "Escala 1, 4 ou 10 marcas virtuais na mesma cozinha. Controla o food cost por marca e por plataforma, melhora o seu posicionamento nos agentes de IA de delivery e multiplica os tickets sem contratar mais sala.",
    "heroTagline": "Cozinha sem sala, margem com sistema",
    "badge": "Dark Kitchen e Ghost Kitchen",
    "painsTitle": "O Que um Operador de Dark Kitchen Não Pode Deixar de Resolver",
    "pains": [
      "Várias marcas na mesma cozinha, cada uma com o seu custo de receita próprio e com custos de matéria-prima que mudam todas as semanas",
      "Margem pressionada por comissões da Glovo, Uber Eats e Just Eat (entre 25 % e 35 % do ticket)",
      "Picos brutais no delivery, das 12:30 às 14:30 e das 20:30 às 22:30, sem margem para erros operativos",
      "Sem contacto físico com o cliente: a marca, as fotos e o copy da ficha são tudo o que tem",
      "Posicionamento nas plataformas que muda constantemente: se perder posições, os pedidos caem a pique",
      "Difícil saber que marca e que prato estão realmente a render quando tudo se mistura na mesma cozinha"
    ],
    "featuresTitle": "Como o AI Chef Pro Ajuda uma Dark Kitchen",
    "features": [
      {
        "icon": "Layers",
        "title": "Custos de receita multi-marca: Culinária Criativa → Kit de Escandallos Pro",
        "description": "A Culinária Criativa gera o prato e o custo de receita inicial em CSV com preços de referência de mercado. Carrega-o no Kit de Escandallos Pro, substitui os preços pelos dos seus fornecedores e obtém custo real e margem por marca, por prato e por plataforma."
      },
      {
        "icon": "Smartphone",
        "title": "Burger Pro AI+, Food Truck AI+ e Restaurantes Casuais AI+",
        "description": "Três agentes especializados que cobrem os conceitos virtuais mais rentáveis em delivery: hamburgueria, fast food, casual e bistrô."
      },
      {
        "icon": "Truck",
        "title": "Cálculo de margem real após comissão",
        "description": "O plano financeiro do AI Chef Pro desconta automaticamente as comissões de cada plataforma e mostra-lhe a margem real por marca e por canal."
      },
      {
        "icon": "TrendingUp",
        "title": "MenuDish Local SEO + BlogPost SEO Gen+",
        "description": "Suite de SEO para que as suas marcas subam no Google local e capte tráfego orgânico, além do que chega pelos agentes de IA."
      },
      {
        "icon": "Search",
        "title": "Keyword Discovery AI+",
        "description": "Investigação de palavras-chave gastronómicas locais para nomear marcas, pratos e cartas que se posicionem melhor."
      },
      {
        "icon": "Image",
        "title": "GastroIMG Gen+",
        "description": "Fotografia gastronómica gerada com IA para as fichas de plataforma. Melhor foto = mais cliques e melhor posicionamento."
      },
      {
        "icon": "Sparkles",
        "title": "Culinária Criativa + Cozinha Italiana, Mexicana, Japonesa…",
        "description": "Mais de 25 receituários de IA por país para criar marcas virtuais temáticas com base profissional, não receitas copiadas do Google."
      },
      {
        "icon": "ShieldCheck",
        "title": "APPCC + ID Alergénios para delivery",
        "description": "Rastreabilidade, temperatura e alergénios pensados para produto que viaja em mochila ou em mota."
      },
      {
        "icon": "BarChart3",
        "title": "Dashboard multi-marca e multi-plataforma",
        "description": "KPIs por marca, ticket médio, comissão, posição no ranking e produtividade. Tudo consolidado numa única vista."
      }
    ],
    "workflowTitle": "Um Dia Real numa Dark Kitchen com AI Chef Pro",
    "workflow": [
      "08:30 · Revê o dashboard do dia anterior: a marca A vai à frente, a marca C caiu 12 % no posicionamento. É preciso agir.",
      "09:00 · Keyword Discovery AI+ — investiga o que os utilizadores da sua zona postal procuram e deteta uma palavra-chave que falta na marca C.",
      "09:30 · MenuDish Local SEO — atualiza as descrições dos 6 pratos top da marca C com essa palavra-chave.",
      "10:00 · Culinária Criativa — chuva de ideias para um prato estrela na marca A, aproveitando que um fornecedor lhe deu bom preço. O mesmo agente devolve-lhe a receita completa e um custo de receita inicial com preços de referência de mercado, descarregável em CSV.",
      "10:30 · Kit de Escandallos Pro — carrega o CSV da Culinária Criativa, substitui os preços de referência pelos dos seus fornecedores negociados e valida a margem após comissão na Glovo (29 %) e na Uber Eats (25 %).",
      "11:00 · GastroIMG Gen+ — gera a fotografia do prato novo e carrega-a nas plataformas.",
      "12:30 · Serviço em delivery, com 4 marcas a operar na mesma cozinha apoiadas pelos modelos de tarefas Dark Kitchen.",
      "16:00 · APPCC assinado, perdas registadas por marca e mise en place do jantar pronto.",
      "23:30 · Encerramento: relatório automático por marca enviado para o WhatsApp do proprietário."
    ],
    "productsTitle": "Modelos, Kits e Guias Descarregáveis para Dark Kitchen",
    "productIds": [
      "guia-dark-kitchen",
      "kit-tareas-dark-kitchen",
      "kit-escandallos",
      "pack-appcc",
      "kit-plan-financiero",
      "kit-inventario"
    ],
    "testimonialQuote": "Operamos 4 marcas virtuais numa cozinha. Sem custos de receita por marca e por plataforma, estávamos a perder margem sem saber onde. O AI Chef Pro resolveu-nos isso numa semana: detetámos que uma marca tinha um food cost de 41 % na Glovo. Redesenhámo-la e subimos 7 pontos de margem sem tocar no preço.",
    "testimonialAuthor": "Iván Domínguez",
    "testimonialRole": "Operador, dark kitchen com 4 marcas virtuais",
    "faqTitle": "Perguntas Frequentes de Operadores de Dark Kitchen",
    "faqs": [
      {
        "q": "Funciona para 1 marca ou para várias na mesma cozinha?",
        "a": "Para ambas. Está pensado de raiz para multi-marca: custo de receita independente por marca, KPIs separados e listas de tarefas que coordenam a produção de várias marcas na mesma produção."
      },
      {
        "q": "Cobre as comissões das plataformas (Glovo, Uber Eats e Just Eat)?",
        "a": "Sim. O cálculo de margem real desconta automaticamente a comissão de cada plataforma, assim sabe o que ganha em cada pedido por canal e pode decidir melhor a sua política de preços."
      },
      {
        "q": "Existe um guia passo a passo para abrir uma dark kitchen?",
        "a": "Sim, o Guía Cómo Montar una Dark Kitchen (24 €): 12 capítulos com requisitos legais, plano financeiro, design de cozinha, tecnologia, marketing e plataformas, além de 3 checklists em Excel e uma calculadora."
      },
      {
        "q": "Serve para escalar para várias localizações de dark kitchen?",
        "a": "Sim. A padronização multi-local do agente Chef Executivo Pro e os dashboards consolidados estão pensados para grupos com várias unidades virtuais."
      },
      {
        "q": "Como me ajuda a melhorar o posicionamento nos agentes de IA de delivery?",
        "a": "Com três alavancas: GastroIMG Gen+ para fotos de melhor qualidade (que aumentam o CTR), MenuDish Local SEO para descrições que convertem e Keyword Discovery AI+ para detetar o que os utilizadores da sua zona postal procuram."
      },
      {
        "q": "O sistema adapta-se ao meu país e às minhas plataformas?",
        "a": "Sim. Começa com o agente «Quem Sou Eu?» num onboarding de 2 minutos onde lhe conta onde opera, que plataformas usa e que comissões tem negociadas. Todo o resto adapta-se ao seu contexto."
      },
      {
        "q": "E o SEO local? Compensa para uma dark kitchen?",
        "a": "Sim, muito. Uma dark kitchen vive da descoberta online: se além do tráfego dos agentes de IA captar pesquisas locais no Google (por exemplo, «hambúrguer delivery [o seu bairro]»), baixa a sua dependência das comissões e soma margem direta. A suite de SEO do AI Chef Pro está pensada exatamente para isso."
      }
    ],
    "ctaTitle": "A sua dark kitchen, com margem real e dados por marca.",
    "ctaSubtitle": "Comece com o onboarding de 2 minutos. Plano Membro por 10 € por mês com 10.000 créditos para usar todos os agentes.",
    "seo": {
      "title": "IA para Dark Kitchen e Cozinhas Virtuais: Custos de Receita e SEO | AI Chef Pro",
      "description": "Suite de IA para dark kitchen e ghost kitchen: custos de receita multi-marca, margem após comissão da Glovo e Uber Eats, SEO local, APPCC e guia para abrir a sua cozinha virtual.",
      "keywords": "IA dark kitchen, dark kitchen software, ghost kitchen, cozinha virtual, custos de receita multi-marca, abrir dark kitchen, gestão delivery IA, posicionamento Glovo Uber Eats, software cozinha fantasma, marca virtual delivery, dark kitchen Espanha, SEO local restaurante delivery",
      "ogImage": "https://aichef.pro/og/use-cases/dark-kitchen.jpg"
    },
    "personalizationTitle": "Personalizado às Suas Marcas, à Sua Zona e às Suas Plataformas",
    "personalizationBody": "O AI Chef Pro arranca com o agente «Quem Sou Eu?», um onboarding conversacional de 2 minutos. Conta-lhe que marcas opera, em que cidade e zona postal, que plataformas utiliza (Glovo, Uber Eats, Just Eat) e que comissões tem negociadas. A partir desse momento, os custos de receita são calculados com a sua comissão real, as recomendações de SEO local apontam para o seu bairro e os KPIs são consolidados por marca e por canal tal como você precisa. Não é um formulário: é uma conversa curta que converte cada agente numa ferramenta feita à sua medida.",
    "appsTitle": "Os Agentes de IA que Vai Usar na Sua Dark Kitchen",
    "apps": [
      {
        "name": "Burger Pro AI+",
        "category": "Conceitos de Negócio",
        "description": "Especialista em hamburguerias virtuais: gourmet, fast food, smash burger e plant-based."
      },
      {
        "name": "Food Truck AI+",
        "category": "Conceitos de Negócio",
        "description": "Conceitos móveis e virtuais de comida rápida com margem ajustada."
      },
      {
        "name": "Restaurantes Casuais AI+",
        "category": "Conceitos de Negócio",
        "description": "Bistrôs, gastrobares, tapas e mediterrâneo virtual: todo o espetro casual."
      },
      {
        "name": "Cozinha Italiana, Mexicana, Japonesa, Tailandesa…",
        "category": "Receituários por país",
        "description": "Mais de 25 receituários de IA para criar marcas virtuais temáticas com base profissional. Cada receita chega com custo de receita inicial em CSV pronto para o Kit de Escandallos Pro."
      },
      {
        "name": "Mermas Genéricas",
        "category": "Ferramentas e Utilitários",
        "description": "Dados precisos de perdas e rendimentos. Crítico para um custo de receita realista em delivery."
      },
      {
        "name": "ID Alergénios",
        "category": "Ferramentas e Utilitários",
        "description": "Identificação automática de alergénios por receita. Obrigatório para vender em delivery de forma legal."
      },
      {
        "name": "MenuDish Local SEO",
        "category": "Conteúdos e Redes Sociais",
        "description": "Descrições otimizadas para SEO por prato, prontas para o blog e para as plataformas."
      },
      {
        "name": "BlogPost SEO Gen+",
        "category": "Conteúdos e Redes Sociais",
        "description": "Posts de blog que captam tráfego orgânico local para as suas marcas virtuais."
      },
      {
        "name": "Keyword Discovery AI+",
        "category": "Conteúdos e Redes Sociais",
        "description": "Investigação de palavras-chave gastronómicas por zona postal."
      },
      {
        "name": "GastroIMG Gen+",
        "category": "Gastro Conhecimento",
        "description": "Fotografia gastronómica com IA para fichas de plataforma: melhor foto, melhor posicionamento."
      },
      {
        "name": "Gerente Restaurante Pro",
        "category": "Gastro Profile Pro",
        "description": "Assistente operativo para coordenar as marcas, as equipas e os fornecedores."
      },
      {
        "name": "InstaFlow AI Pro + Gerador de Pins Pinterest",
        "category": "Conteúdos e Redes Sociais",
        "description": "Conteúdo viral para captar audiência para além das plataformas de delivery."
      }
    ],
    "metrics": [
      {
        "value": "+7 pp",
        "label": "margem após custear por marca"
      },
      {
        "value": "×4",
        "label": "marcas virtuais numa cozinha"
      },
      {
        "value": "−35 %",
        "label": "tempo em gestão multi-marca"
      },
      {
        "value": "12+",
        "label": "agentes de IA para dark kitchen"
      }
    ],
    "beforeAfter": {
      "beforeTitle": "Sem AI Chef Pro",
      "beforeItems": [
        "Custo de receita manual em Excel com margem «média» entre marcas",
        "Comissões de plataformas subtraídas a olho, sem saber que canal compensa mais",
        "Fotos de plataforma de qualidade média e posicionamento errático",
        "Descrições genéricas que não captam SEO local",
        "KPIs misturados: impossível saber que marca rende realmente",
        "Operativa em folhas soltas e erros em horas de pico"
      ],
      "afterTitle": "Com AI Chef Pro",
      "afterItems": [
        "Custo de receita independente por marca e por plataforma, com margem real no instante",
        "Cálculo automático após comissão por canal e decisões de preço com dados",
        "Fotografias profissionais com GastroIMG Gen+ e posicionamento mais estável",
        "Descrições e blog otimizados para o SEO local da sua zona postal",
        "Dashboard multi-marca com KPIs separados por marca e por canal",
        "Listas de tarefas Dark Kitchen específicas para coordenar produção multi-marca"
      ]
    },
    "galleryTitle": "Como Funciona uma Dark Kitchen Moderna",
    "gallerySubtitle": "Produção multi-marca, packaging com marca por marca virtual, ecrãs com pedidos da Glovo, Uber Eats e JustEat, riders no pickup e tudo o que envolve uma operativa 100% delivery.",
    "galleryImages": [
      "/lovable-uploads/ai-gallery/use-case-dark-kitchen-hero.jpg",
      "/lovable-uploads/ai-gallery/use-case-dark-kitchen-cooking.jpg",
      "/lovable-uploads/ai-gallery/use-case-dark-kitchen-packaging.jpg",
      "/lovable-uploads/ai-gallery/use-case-dark-kitchen-orders.jpg",
      "/lovable-uploads/ai-gallery/use-case-dark-kitchen-pickup.jpg",
      "/lovable-uploads/ai-gallery/use-case-dark-kitchen-app.jpg"
    ]
  },
  "pasteleria-obrador": {
    "h1": "IA para Pastelaria e Obrador",
    "heroSubtitle": "Custo por peça com custo de hora de obrador, planeia produção sazonal e capta branding profissional com uma suite de agentes de IA especializados em pastelaria artesanal.",
    "heroTagline": "Pastelaria com margem real e sem papéis",
    "badge": "Para pastelarias e obradores artesanais",
    "painsTitle": "O Que uma Pastelaria Não Pode Deixar de Resolver",
    "pains": [
      "Fichas técnicas complexas com massas mãe, prefermentos e elaborações longas que requerem horas de obrador",
      "Quebras elevadas em obrador (modelagem, cozedura, decoração) que sangram rentabilidade sem controlo",
      "Rastreabilidade APPCC com produtos sensíveis: ovo, lacticínios, cremes, frutos secos",
      "Sazonalidade muito forte: Bolo Rei, Dia dos Namorados, Páscoa, Natal, comunhões",
      "Diferenciar-se em zona competitiva: branding visual, vitrina e redes sociais são chave",
      "Captar pedidos de tartes personalizadas com margem enquanto se gere a pastelaria diária"
    ],
    "featuresTitle": "Como AI Chef Pro Ajuda na Pastelaria",
    "features": [
      {
        "icon": "Cake",
        "title": "Pastelaria Criativa",
        "description": "Agente especializado em pastelaria profissional, sobremesas de restaurante, tartes personalizadas e pastelaria com técnica avançada."
      },
      {
        "icon": "Cookie",
        "title": "Chocolataria Criativa",
        "description": "Para obradores que combinam pastelaria com chocolataria: bombons, ganaches, coberturas e combinações."
      },
      {
        "icon": "Wheat",
        "title": "Padaria Criativa",
        "description": "Para obradores que fazem a sua própria pastelaria com massa mãe, brioche, croissants e padaria artesanal."
      },
      {
        "icon": "Beaker",
        "title": "Fermentus Con AI+",
        "description": "Massas mãe profissionais, fermentações controladas e processos de padaria de vanguarda."
      },
      {
        "icon": "Calculator",
        "title": "Fichas técnicas com custo de hora de obrador",
        "description": "Culinária Criativa entrega receita + ficha técnica CSV; Kit de Escandallos Pro gere-a com custo de hora de obrador integrado em margem real por peça."
      },
      {
        "icon": "CheckSquare",
        "title": "Kit de Tareas Pastelería",
        "description": "Modelos: preparação de massa mãe, produção, modelagem, cozedura, vitrina, conservação."
      },
      {
        "icon": "ShieldCheck",
        "title": "Pack APPCC pastelaria",
        "description": "Rastreabilidade de ovo, cremes com lacticínios, frutos secos e conservação profissional."
      },
      {
        "icon": "Calendar",
        "title": "Gastro Calendar",
        "description": "Planeamento sazonal com datas-chave: Bolo Rei, Dia dos Namorados, Páscoa, Natal. Calendário editorial para vitrina."
      },
      {
        "icon": "Image",
        "title": "GastroIMG Gen+ + Gerador de Pins Pinterest",
        "description": "Fotografia gastronómica IA + Pinterest, onde as pastelarias captam mais tráfego orgânico estável."
      }
    ],
    "workflowTitle": "Um Dia Real numa Pastelaria com AI Chef Pro",
    "workflow": [
      "06:00 · Abertura — checklist Kit de Tareas Pastelería: refresco de massa mãe, batido de bolos, preparação de cremes.",
      "08:00 · Pastelaria Criativa — desenvolve uma nova sobremesa para o Dia dos Namorados. Culinária Criativa entrega receita + ficha técnica CSV.",
      "09:00 · Kit de Escandallos Pro — carregas o CSV com os seus preços reais e custo de hora de obrador integrado, valida a margem.",
      "11:00 · Produção do dia — modelagem e cozedura com modelos específicos, quebras registadas com APPCC.",
      "14:00 · Reposição de vitrina com etiquetas e preços, controlo de quebras de exposição.",
      "16:00 · Gastro Calendar — prepara o planeamento de produção de Bolo Rei (Natal).",
      "18:00 · GastroIMG Gen+ + Gerador de Pins Pinterest — gera fotografias e pins da nova sobremesa para captar tráfego.",
      "20:00 · Encerramento — limpeza profunda, APPCC assinado, planeamento do dia seguinte."
    ],
    "productsTitle": "Modelos e Kits Descarregáveis para Pastelaria",
    "productIds": [
      "kit-tareas-pasteleria",
      "kit-escandallos",
      "pack-appcc",
      "kit-inventario",
      "kit-gestion-personal",
      "pro-prompts-ebook"
    ],
    "testimonialQuote": "Os custos por peça com custo de hora de obrador abriram-me os olhos. Descobri que algumas elaborações complexas não eram rentáveis apesar de se venderem bem. Redesenhámo-las com Pastelaria Criativa simplificando o processo sem perder qualidade e subimos a margem 6 pontos.",
    "testimonialAuthor": "Eva Mata",
    "testimonialRole": "Proprietária, pastelaria artesanal com obrador próprio",
    "faqTitle": "Perguntas Frequentes de Pastelarias",
    "faqs": [
      {
        "q": "Serve para obrador artesanal pequeno ou grande?",
        "a": "Para ambos. Os modelos escalam desde obrador familiar de 2 pessoas até produção industrial. Há clientes com um e com seis pasteleiros."
      },
      {
        "q": "Cobre padaria além de pastelaria?",
        "a": "Sim. Padaria Criativa + Fermentus Con AI+ cobrem padaria artesanal e massa mãe profissional para obradores mistos."
      },
      {
        "q": "Há controlo de custo de hora de obrador?",
        "a": "Sim. Custo de hora de obrador integrado na ficha técnica do Kit de Escandallos Pro: uma elaboração complexa com 3 horas de trabalho por peça tem o seu custo real refletido."
      },
      {
        "q": "Gera conteúdo para vitrina e redes?",
        "a": "Sim. GastroIMG Gen+ para fotos de vitrina + Gerador de Pins Pinterest + InstaFlow AI Pro + MenuDish Local SEO para captar clientes locais."
      },
      {
        "q": "Como me ajuda com a sazonalidade?",
        "a": "Gastro Calendar planeia as épocas-chave (Bolo Rei, Dia dos Namorados, Páscoa, Natal, comunhões) com antecedência e plano financeiro adaptado a picos de produção."
      }
    ],
    "ctaTitle": "O seu obrador com margem clara e branding profissional.",
    "ctaSubtitle": "Começa com o onboarding de 2 minutos. Plano Membro por 10 € por mês com 10.000 créditos para usar todos os agentes.",
    "seo": {
      "title": "IA para Pastelaria e Obrador: Fichas Técnicas, Sazonalidade e Branding | AI Chef Pro",
      "description": "Suite de IA para pastelarias artesanais: Pastelaria Criativa, fichas técnicas por peça com custo de hora de obrador, APPCC, planeamento sazonal e branding. Começa hoje.",
      "keywords": "IA pastelaria, software obrador, fichas técnicas pastelaria, pastelaria artesanal IA, massa mãe pastelaria, Bolo Rei Natal, pastelaria Espanha",
      "ogImage": "https://aichef.pro/og/use-cases/pasteleria-obrador.jpg"
    },
    "personalizationTitle": "Personalizado ao Seu Obrador desde o Minuto Um",
    "personalizationBody": "AI Chef Pro arranca com o agente «Quem Sou Eu?», um onboarding conversacional de 2 minutos em que lhe conta que tipo de pastelaria opera (artesanal, industrial, pastelaria de restaurante, obrador misto), tamanho da equipa, cidade e especialidade. Cada agente —desde Pastelaria Criativa até Gastro Calendar— responde adaptado ao seu produto, mercado e operativa real.",
    "appsTitle": "Os Agentes IA que Vai Usar na Sua Pastelaria",
    "apps": [
      {
        "name": "Pastelaria Criativa",
        "category": "Criatividade Culinária",
        "description": "Agente especializado em pastelaria profissional, sobremesas e tartes com técnica avançada."
      },
      {
        "name": "Chocolataria Criativa",
        "category": "Criatividade Culinária",
        "description": "Para bombons, ganaches e combinações de chocolate."
      },
      {
        "name": "Padaria Criativa",
        "category": "Criatividade Culinária",
        "description": "Para massa mãe, brioche, croissants e padaria artesanal."
      },
      {
        "name": "Fermentus Con AI+",
        "category": "Criatividade Culinária",
        "description": "Fermentações, prefermentos e técnicas avançadas de padaria."
      },
      {
        "name": "Culinária Criativa",
        "category": "Criatividade Culinária",
        "description": "Desenvolvimento de sobremesas com receita + ficha técnica CSV."
      },
      {
        "name": "Sosa Ingredients",
        "category": "Fornecedores Gastro",
        "description": "Assistente do catálogo Sosa para texturas e técnica avançada."
      },
      {
        "name": "tSpoonLab Agent",
        "category": "Fornecedores Gastro",
        "description": "Assistente do catálogo tSpoonLab para aplicações avançadas."
      },
      {
        "name": "Mermas Genéricas",
        "category": "Ferramentas e Utilitários",
        "description": "Dados precisos de quebras em obrador (modelagem, cozedura, vitrina)."
      },
      {
        "name": "ID Alergénios",
        "category": "Ferramentas e Utilitários",
        "description": "Identificação automática de alergénios por peça, crítico em pastelaria."
      },
      {
        "name": "GastroIMG Gen+",
        "category": "Conhecimento Gastro",
        "description": "Fotografia gastronómica IA para vitrina, web e redes."
      },
      {
        "name": "Gerador de Pins Pinterest",
        "category": "Conteúdos e Redes Sociais",
        "description": "Pinterest é o canal com mais tráfego orgânico estável para pastelaria."
      },
      {
        "name": "Gastro Calendar",
        "category": "Conteúdos e Redes Sociais",
        "description": "Planeamento sazonal: Bolo Rei, Dia dos Namorados, Páscoa, Natal."
      }
    ],
    "metrics": [
      {
        "value": "+6 pp",
        "label": "margem após custeio de peças"
      },
      {
        "value": "×2",
        "label": "tráfego orgânico via Pinterest"
      },
      {
        "value": "−30 %",
        "label": "quebras em obrador"
      },
      {
        "value": "12+",
        "label": "agentes para o seu obrador"
      }
    ],
    "beforeAfter": {
      "beforeTitle": "Sem AI Chef Pro",
      "beforeItems": [
        "Fichas técnicas sem custo de hora de obrador, elaborações longas em perdas sem saber",
        "Quebras em obrador e vitrina sem rastreabilidade real",
        "Vitrina e redes sociais improvisadas sem continuidade",
        "Produção sazonal reativa, sem antecedência nem planeamento",
        "APPCC em papel impresso disperso pelo obrador"
      ],
      "afterTitle": "Com AI Chef Pro",
      "afterItems": [
        "Ficha técnica profissional por peça com custo de hora de obrador integrado",
        "Quebras controladas com Mermas Genéricas e modelos específicos",
        "Gerador de Pins Pinterest + InstaFlow + GastroIMG Gen+ captam tráfego estável",
        "Gastro Calendar planeia épocas-chave com antecedência",
        "APPCC desde o telemóvel com registos prontos para inspeção"
      ]
    },
    "galleryTitle": "Como Funciona uma Pastelaria Artesanal",
    "gallerySubtitle": "O que vais coordenar com AI Chef Pro: vitrina, obrador, exposição de peças, decoração, tartes e equipa.",
    "galleryImages": [
      "/lovable-uploads/ai-gallery/use-case-pasteleria-hero.jpg",
      "/lovable-uploads/ai-gallery/use-case-pasteleria-obrador.jpg",
      "/lovable-uploads/ai-gallery/use-case-pasteleria-display.jpg",
      "/lovable-uploads/ai-gallery/use-case-pasteleria-piping.jpg",
      "/lovable-uploads/ai-gallery/use-case-pasteleria-cakes.jpg",
      "/lovable-uploads/ai-gallery/use-case-pasteleria-team.jpg"
    ]
  },
  "bar-cocktails": {
    "h1": "IA para Bar e Coctelaria",
    "heroSubtitle": "Desenhe cartas de cocktails de autor, calcule o custo de cada trago com os seus preços reais e capture branding profissional com uma suite de agentes de IA pensados para bartenders, cocteleiros e proprietários de bar.",
    "heroTagline": "A sua barra com margem real, coctelaria com técnica",
    "badge": "Para bares de cocktails e coctelarias",
    "painsTitle": "O Que um Bar de Cocktails Não Pode Deixar de Resolver",
    "pains": [
      "Calcular o custo de cocktails complexos com muitos ingredientes, infusões e técnicas",
      "Perdas e quebra de cristalaria na barra que sangram rentabilidade sem controlo",
      "Cartas de drinks que mudam sazonalmente com I&D contínuo",
      "Margem muito apertada em bebidas spirit com custo de alcoóis premium volátil",
      "Diferenciar-se em zona competitiva com storytelling e branding visual de cocktails",
      "Gerir coctelaria de autor combinada com cervejaria, vinhos e carta de tapas"
    ],
    "featuresTitle": "Como AI Chef Pro Ajuda num Bar de Cocktails",
    "features": [
      {
        "icon": "Wine",
        "title": "Bar & Lounge AI+",
        "description": "Agente especializado em pubs, coctelaria, vinotecas, bares desportivos e bares de copos com conhecimento profissional."
      },
      {
        "icon": "Sparkles",
        "title": "Food Pairing AI",
        "description": "Combinações inesperadas para cocktails de autor com base científica e maridagem com tapas."
      },
      {
        "icon": "Beaker",
        "title": "Fermentus Con AI+",
        "description": "Fermentações para cocktails avançados: kombuchas como base, infusões, lactofermentos cítricos."
      },
      {
        "icon": "Calculator",
        "title": "Custos por drink",
        "description": "Culinária Criativa entrega receita + ficha de custos CSV; Kit de Escandallos Pro gere-o com os seus preços reais e margem profissional por cocktail."
      },
      {
        "icon": "BookOpen",
        "title": "Cartas de cocktail com storytelling",
        "description": "Design de carta e rotação sazonal com storytelling profissional para sala e imprensa."
      },
      {
        "icon": "CheckSquare",
        "title": "Kit de Tareas Bar",
        "description": "Modelos: preparação de sumos, xaropes, garnishes, infusões, mise de barra, serviço e limpeza profunda."
      },
      {
        "icon": "ShieldCheck",
        "title": "Pack APPCC Bar",
        "description": "Rastreabilidade específica: sumos frescos, cremes, conservação de garnishes, lavagem de cristalaria."
      },
      {
        "icon": "Image",
        "title": "GastroIMG Gen+ + InstaFlow AI Pro",
        "description": "Fotografia de cocktails com IA + conteúdo para Instagram com calendário editorial profissional."
      },
      {
        "icon": "BookOpen",
        "title": "Sosa Ingredients + tSpoonLab Agent",
        "description": "Assistentes para seleção de ingredientes técnicos premium muito usados em coctelaria de autor."
      }
    ],
    "workflowTitle": "Um Dia Real num Bar de Cocktails com AI Chef Pro",
    "workflow": [
      "11:00 · Abertura — checklist Kit de Tareas Bar: preparação de sumos, xaropes, infusões e garnishes.",
      "14:00 · Bar & Lounge AI+ + Food Pairing AI — desenvolve um novo cocktail para a carta de primavera com maridagem em mente.",
      "15:00 · Culinária Criativa entrega receita + ficha de custos CSV; Kit de Escandallos Pro gere-o com os seus preços reais (gin premium, xaropes, garnish).",
      "16:00 · Teste do cocktail com a equipa, ajustes finais de equilíbrio e proporções.",
      "17:00 · Pro Prompts eBook + BlogPost SEO Gen+ — redige storytelling para a nova carta e nota para sala.",
      "18:00 · GastroIMG Gen+ + InstaFlow AI Pro — gera a fotografia e posts de Instagram para o lançamento.",
      "20:00 · Serviço noite — barra coordenada, custos validados, cocktails a serem servidos com precisão.",
      "02:30 · Encerramento — limpeza profunda, APPCC assinado, relatório de drinks do dia."
    ],
    "productsTitle": "Modelos e Kits Descarregáveis para Bar e Coctelaria",
    "productIds": [
      "kit-tareas-bar",
      "kit-escandallos",
      "pack-appcc",
      "kit-inventario",
      "kit-gestion-personal",
      "pro-prompts-ebook"
    ],
    "testimonialQuote": "Ter cada cocktail com custo calculado e a carta pronta numa manhã mudou a minha forma de trabalhar. Antes era com calculadora, guardanapo e muita intuição. Agora com Bar & Lounge AI+ e o Kit de Escandallos Pro tiro uma carta nova com margem validada em 2 horas.",
    "testimonialAuthor": "Hugo Vázquez",
    "testimonialRole": "Bartender e proprietário, cocktail bar de autor",
    "faqTitle": "Perguntas Frequentes de Bartenders e Cocteleiros",
    "faqs": [
      {
        "q": "Serve para coctelaria de autor ou casual?",
        "a": "Para ambas. Bar & Lounge AI+ + Food Pairing AI cobrem desde cocktails clássicos a coctelaria de vanguarda com técnica profissional."
      },
      {
        "q": "Cobre cervejaria e vinhos além de coctelaria?",
        "a": "Sim. Bar & Lounge AI+ cobre todo o espectro de barra: cervejarias, vinotecas, bares de copos, pubs tradicionais e bares desportivos."
      },
      {
        "q": "Gera ideias de drinks novos com técnica?",
        "a": "Sim. Bar & Lounge AI+ + Culinária Criativa + Food Pairing AI + Fermentus Con AI+ trabalham em conjunto para criar cocktails com base profissional."
      },
      {
        "q": "Funciona para bar de hotel ou local independente?",
        "a": "Ambos. O bar lobby de hotel gere-se a partir do caso /usos/concepto/hotel-completo-fb; bar independente a partir daqui."
      },
      {
        "q": "Como me ajuda com o branding visual dos meus cocktails?",
        "a": "GastroIMG Gen+ gera fotografias profissionais de cada drink para Instagram, web e carta. InstaFlow AI Pro programa o conteúdo com calendário editorial."
      }
    ],
    "ctaTitle": "Coctelaria com margem real e branding profissional.",
    "ctaSubtitle": "Comece com o onboarding de 2 minutos. Plano Membro por 10 € por mês com 10.000 créditos para usar todos os agentes.",
    "seo": {
      "title": "IA para Bar e Coctelaria: Cocktails de Autor, Custos e Branding | AI Chef Pro",
      "description": "Suite de IA para bares e coctelaria profissional: Bar & Lounge AI+, Food Pairing AI, custos por cocktail, cartas, APPCC e branding visual. Comece hoje.",
      "keywords": "IA bar coctelaria, custos cocktail, software bar, IA bartender, IA cocteleiro, cocktail bar IA, bar autor Espanha, gestão coctelaria IA",
      "ogImage": "https://aichef.pro/og/use-cases/bar-cocktails.jpg"
    },
    "personalizationTitle": "Personalizado ao Seu Bar desde o Minuto Um",
    "personalizationBody": "AI Chef Pro arranca com o agente «Quem Sou Eu?», um onboarding conversacional de 2 minutos no qual lhe conta que tipo de bar gere (cocktail bar, vinoteca, cervejaria, pub, bar de copos), cidade e carta. Cada agente —desde Bar & Lounge AI+ até ao Kit de Escandallos Pro— responde adaptado ao seu estilo de barra e mercado.",
    "appsTitle": "Os Agentes IA que Vai Usar no Seu Bar",
    "apps": [
      {
        "name": "Bar & Lounge AI+",
        "category": "Conceitos de Negócio",
        "description": "Agente principal: pubs, coctelaria, vinotecas, bares desportivos, bares de copos."
      },
      {
        "name": "Culinária Criativa",
        "category": "Criatividade Culinária",
        "description": "Desenvolvimento de cocktails com receita + ficha de custos CSV."
      },
      {
        "name": "Food Pairing AI",
        "category": "Criatividade Culinária",
        "description": "Combinações científicas para cocktails de autor e maridagem com tapas."
      },
      {
        "name": "Fermentus Con AI+",
        "category": "Criatividade Culinária",
        "description": "Fermentações para coctelaria avançada: kombuchas, infusões, lactofermentos."
      },
      {
        "name": "Restaurantes Casuais AI+",
        "category": "Conceitos de Negócio",
        "description": "Para bares com carta de tapas e cozinha ligeira além de coctelaria."
      },
      {
        "name": "Sosa Ingredients",
        "category": "Fornecedores Gastro",
        "description": "Assistente para ingredientes técnicos do catálogo Sosa."
      },
      {
        "name": "tSpoonLab Agent",
        "category": "Fornecedores Gastro",
        "description": "Assistente do catálogo tSpoonLab para coctelaria técnica."
      },
      {
        "name": "ID Alergénios",
        "category": "Ferramentas e Utilitários",
        "description": "Identificação automática de alergénios em cocktails e tapas."
      },
      {
        "name": "Mermas Genéricas",
        "category": "Ferramentas e Utilitários",
        "description": "Dados precisos de perdas em sumos, garnishes e cristalaria."
      },
      {
        "name": "GastroIMG Gen+",
        "category": "Gastro Conhecimento",
        "description": "Fotografia gastronómica IA para cocktails: web, redes e carta."
      },
      {
        "name": "InstaFlow AI Pro",
        "category": "Conteúdos e Redes Sociais",
        "description": "Conteúdo viral Instagram para coctelaria com calendário editorial."
      },
      {
        "name": "Pro Prompts eBook",
        "category": "Gastro Conhecimento",
        "description": "300+ prompts para storytelling de cocktails, comunicação com imprensa e formação."
      }
    ],
    "metrics": [
      {
        "value": "×4",
        "label": "velocidade de fecho da carta de cocktails"
      },
      {
        "value": "+5 pp",
        "label": "margem após custo profissional"
      },
      {
        "value": "×3",
        "label": "engagement Instagram com GastroIMG"
      },
      {
        "value": "12+",
        "label": "agentes para o seu bar"
      }
    ],
    "beforeAfter": {
      "beforeTitle": "Sem AI Chef Pro",
      "beforeItems": [
        "Cocktails com custo calculado com calculadora e guardanapo",
        "Cartas de drinks sem storytelling profissional para sala",
        "Perdas na barra e cristalaria sem rastreabilidade",
        "Branding visual improvisado no Instagram com fotos do telemóvel",
        "Sem acesso sistemático a tendências de coctelaria internacional"
      ],
      "afterTitle": "Com AI Chef Pro",
      "afterItems": [
        "Bar & Lounge AI+ + Culinária Criativa + Kit de Escandallos Pro fecham cartas em 2 horas",
        "Storytelling profissional para cada cocktail pronto para sala e imprensa",
        "Perdas controladas com Mermas Genéricas e modelos específicos",
        "GastroIMG Gen+ + InstaFlow geram fotos profissionais e posts virais",
        "Sonar Deep Research traz tendências e referências internacionais"
      ]
    },
    "galleryTitle": "Como Funciona um Bar de Cocktails Profissional",
    "gallerySubtitle": "O que vai coordenar com AI Chef Pro: barra principal, técnica de shaker, cocktail final, preparação de garnishes, técnica de pour e serviço.",
    "galleryImages": [
      "/lovable-uploads/ai-gallery/use-case-bar-hero.jpg",
      "/lovable-uploads/ai-gallery/use-case-bar-shaker.jpg",
      "/lovable-uploads/ai-gallery/use-case-bar-cocktail.jpg",
      "/lovable-uploads/ai-gallery/use-case-bar-prep.jpg",
      "/lovable-uploads/ai-gallery/use-case-bar-pour.jpg",
      "/lovable-uploads/ai-gallery/use-case-bar-team.jpg"
    ]
  },
  "catering-eventos": {
    "h1": "IA para Catering e Eventos",
    "heroSubtitle": "Escandallo por evento, planifica produção à escala, gere logística e APPCC fora do local com uma suite de agentes de IA especializados em catering profissional, casamentos, corporativos e cocktails.",
    "heroTagline": "Eventos com margem, sem caos",
    "badge": "Para empresas de catering e eventos",
    "painsTitle": "O Que um Catering Não Pode Deixar de Resolver",
    "pains": [
      "Escandallar menus com variabilidade alta de convidados (50, 200, 500) quando os preços mudam todas as semanas",
      "Planificar produção e mise en place à escala a partir de cozinha central",
      "Coordenar logística, transporte refrigerado e montagem na sede do cliente",
      "Manter APPCC e rastreabilidade fora do local fixo, em sedes alheias e veículos",
      "Captar clientes corporativos com propostas profissionais que fechem contratos de maior ticket",
      "Gerir simultaneamente vários eventos do fim de semana sem desvios"
    ],
    "featuresTitle": "Como AI Chef Pro Ajuda em Catering e Eventos",
    "features": [
      {
        "icon": "PartyPopper",
        "title": "Catering AI+",
        "description": "Agente especializado em catering e eventos gastronómicos: casamentos, corporativos, cocktails e galas com conhecimento profissional."
      },
      {
        "icon": "Sparkles",
        "title": "Culinária Criativa + Food Pairing AI",
        "description": "Chuva de ideias para menus de evento. Culinária Criativa entrega receita + escandallo CSV pronto para o Kit de Escandallos Pro."
      },
      {
        "icon": "Calculator",
        "title": "Escandallos por evento",
        "description": "Kit de Escandallos Pro: carrega o CSV com os seus preços reais, ajusta o número de convidados e obtém margem instantaneamente."
      },
      {
        "icon": "Layers",
        "title": "Calcula Pax",
        "description": "Calculadora de porções que escala receitas para 50, 200, 500 ou 1000 comensais em segundos."
      },
      {
        "icon": "CheckSquare",
        "title": "Kit de Tareas Catering",
        "description": "Modelos: produção central, transporte refrigerado, montagem em sede, serviço e desmontagem."
      },
      {
        "icon": "ShieldCheck",
        "title": "Pack APPCC fora do local",
        "description": "Rastreabilidade em transporte, sede alheia e serviço externo com registos a partir do telemóvel."
      },
      {
        "icon": "Image",
        "title": "GastroIMG Gen+",
        "description": "Fotografia gastronómica IA para propostas a clientes corporativos e galeria de eventos."
      },
      {
        "icon": "ShieldCheck",
        "title": "ID Alergénios",
        "description": "Identificação automática crítica para eventos com perfis alimentares variados."
      },
      {
        "icon": "Search",
        "title": "BlogPost SEO Gen+ + Keyword Discovery AI+",
        "description": "Captação orgânica de empresas que procuram catering na sua zona."
      }
    ],
    "workflowTitle": "Um Dia Real numa Empresa de Catering com AI Chef Pro",
    "workflow": [
      "08:30 · Catering AI+ — o agente ajuda-o a fechar o menu proposto para um casamento de 180 convidados segundo briefing do cliente.",
      "09:30 · Culinária Criativa — desenvolve os 12 pratos do menu com receita e escandallo CSV com preços de referência.",
      "10:30 · Calcula Pax + Kit de Escandallos Pro — escala para 180 comensais, carrega o CSV com os seus preços reais e valida margem.",
      "12:00 · GastroIMG Gen+ — gera fotografias dos pratos para incluir na apresentação ao cliente.",
      "14:00 · Reunião com cliente — proposta fechada com apresentação profissional em vez dos modelos Word de antes.",
      "16:00 · Kit de Tareas Catering — planifica produção central, transporte, montagem e serviço do evento de sábado.",
      "18:00 · Pack APPCC — prepara registos de temperatura para transporte e rastreabilidade em sede alheia.",
      "20:00 · Brief à equipa — monta brief de produção, transporte, montagem e serviço a partir de uma única fonte."
    ],
    "productsTitle": "Modelos e Kits Descarregáveis para Catering",
    "productIds": [
      "kit-tareas-catering",
      "kit-escandallos",
      "pack-appcc",
      "kit-plan-financiero",
      "kit-inventario",
      "pro-prompts-ebook"
    ],
    "testimonialQuote": "Fechamos eventos em um terço do tempo. Os escandallos por evento ajustam ao detalhe por número de convidados, as plantillas de logística são ouro e as propostas com fotografia profissional fecham contratos corporativos que antes nos escapavam. Margem +5 pontos no primeiro trimestre só por melhor escandallo.",
    "testimonialAuthor": "Sara Pérez",
    "testimonialRole": "Empresa de catering corporativo e casamentos (200 eventos por ano)",
    "faqTitle": "Perguntas Frequentes de Empresas de Catering",
    "faqs": [
      {
        "q": "Serve para catering boutique ou grande?",
        "a": "Para ambos. Desde caterings boutique de 50 convidados por mês até empresas com mais de 1000 serviços por mês e eventos de 2000 comensais."
      },
      {
        "q": "Cobre casamentos, corporativos e cocktails?",
        "a": "Sim. Catering AI+ e o Kit de Tareas Catering têm modelos específicos para os três formatos e para galas/eventos especiais."
      },
      {
        "q": "Há APPCC específico fora do local fixo?",
        "a": "Sim. O Pack APPCC tem modelos adaptados a produto que viaja em mochila, moto, carrinha refrigerada ou cozinha central, incluindo rastreabilidade em sede alheia."
      },
      {
        "q": "Gera propostas comerciais para empresas?",
        "a": "Sim. Catering AI+ + GastroIMG Gen+ + Pro Prompts eBook permitem redigir propostas profissionais com fotografia gastronómica e storytelling."
      },
      {
        "q": "Como me ajuda a captar clientes corporativos?",
        "a": "BlogPost SEO Gen+ + Keyword Discovery AI+ + MenuDish Local SEO trabalham em conjunto para captar empresas que procuram catering na sua zona via pesquisas orgânicas no Google."
      }
    ],
    "ctaTitle": "Catering com margem real e sem caos.",
    "ctaSubtitle": "Começa com o onboarding de 2 minutos. Plano Membro por 10 € por mês com 10.000 créditos para usar todos os agentes.",
    "seo": {
      "title": "IA para Catering e Eventos: Casamentos, Corporativos e Cocktails | AI Chef Pro",
      "description": "Suite de IA para empresas de catering profissional: Catering AI+, escandallos por evento, produção à escala, APPCC fora do local e propostas comerciais. Comece hoje.",
      "keywords": "IA catering, software catering, escandallos eventos, gestão catering IA, catering casamentos IA, catering corporativo IA, eventos gastronómicos software, catering Espanha",
      "ogImage": "https://aichef.pro/og/use-cases/catering-eventos.jpg"
    },
    "personalizationTitle": "Personalizado ao Seu Catering desde o Minuto Um",
    "personalizationBody": "AI Chef Pro arranca com o agente «Quem Sou Eu?», um onboarding conversacional de 2 minutos em que lhe conta que tipo de catering opera (casamentos, corporativos, cocktails, galas), tamanho médio, cidade e volume anual. Cada agente —desde Catering AI+ até ao Kit Plan Financiero— responde adaptado ao seu tipo de evento, escala e mercado real.",
    "appsTitle": "Os Agentes IA que Vai Usar no Seu Catering",
    "apps": [
      {
        "name": "Catering AI+",
        "category": "Conceitos de Negócio",
        "description": "Agente principal: casamentos, corporativos, cocktails e galas com base profissional."
      },
      {
        "name": "Culinária Criativa",
        "category": "Criatividade Culinária",
        "description": "Desenvolvimento de menus de evento com receita + escandallo CSV."
      },
      {
        "name": "Food Pairing AI",
        "category": "Criatividade Culinária",
        "description": "Combinações de ingredientes e harmonizações para cocktails e canapés."
      },
      {
        "name": "Pastelaria Criativa",
        "category": "Criatividade Culinária",
        "description": "Sobremesas de evento e banquete com técnica profissional."
      },
      {
        "name": "Fermentus Con AI+",
        "category": "Criatividade Culinária",
        "description": "Para canapés vanguardistas com fermentos e técnicas inovadoras."
      },
      {
        "name": "Calcula Pax",
        "category": "Ferramentas e Utilitários",
        "description": "Calculadora de porções que escala receitas para 50, 200 ou 500 comensais."
      },
      {
        "name": "ID Alergénios",
        "category": "Ferramentas e Utilitários",
        "description": "Identificação de alergénios crítica em eventos com muitos convidados."
      },
      {
        "name": "Mermas Genéricas",
        "category": "Ferramentas e Utilitários",
        "description": "Dados precisos para produção à escala industrial."
      },
      {
        "name": "BlogPost SEO Gen+",
        "category": "Conteúdos e Redes Sociais",
        "description": "Posts de blog para captar empresas via pesquisas orgânicas."
      },
      {
        "name": "MenuDish Local SEO",
        "category": "Conteúdos e Redes Sociais",
        "description": "Descrições SEO para melhorar o posicionamento do site do catering."
      },
      {
        "name": "GastroIMG Gen+",
        "category": "Conhecimento Gastro",
        "description": "Fotografia gastronómica IA para propostas e galeria web."
      },
      {
        "name": "Sosa Ingredients",
        "category": "Fornecedores Gastro",
        "description": "Para ingredientes técnicos em cocktails e canapés."
      }
    ],
    "metrics": [
      {
        "value": "×3",
        "label": "velocidade de fecho de propostas"
      },
      {
        "value": "+5 pp",
        "label": "margem após escandallo real"
      },
      {
        "value": "−50 %",
        "label": "tempo em logística"
      },
      {
        "value": "11+",
        "label": "agentes para o seu catering"
      }
    ],
    "beforeAfter": {
      "beforeTitle": "Sem AI Chef Pro",
      "beforeItems": [
        "Fechar menu com cliente: meia tarde com calculadora",
        "Produção para 200 convidados sem escalonamento preciso",
        "APPCC fora do local improvisado",
        "Propostas com modelos Word e fotos de stock",
        "Brief à equipa em folhas soltas"
      ],
      "afterTitle": "Com AI Chef Pro",
      "afterItems": [
        "Fechar menu em 30 minutos com margem validada",
        "Produção escalada com Calcula Pax e Mermas Genéricas",
        "APPCC com rastreabilidade em transporte e sede alheia",
        "Propostas com GastroIMG Gen+ e storytelling profissional",
        "Brief centralizado com Kit de Tareas Catering"
      ]
    },
    "galleryTitle": "Como Funciona um Catering Profissional",
    "gallerySubtitle": "O que vai coordenar com AI Chef Pro: produção central, eventos elegantes, canapés, cocktails corporativos, montagem e serviço.",
    "galleryImages": [
      "/lovable-uploads/ai-gallery/use-case-catering-eventos-hero.jpg",
      "/lovable-uploads/ai-gallery/use-case-catering-eventos-canapes.jpg",
      "/lovable-uploads/ai-gallery/use-case-catering-eventos-corporate.jpg",
      "/lovable-uploads/ai-gallery/use-case-catering-eventos-cocktail.jpg",
      "/lovable-uploads/ai-gallery/use-case-catering-eventos-setup.jpg",
      "/lovable-uploads/ai-gallery/use-case-catering-eventos-banquet.jpg"
    ]
  },
  "hotel-completo": {
    "h1": "IA para Hotel Completo (F&B + Housekeeping)",
    "heroSubtitle": "Gere pequenos-almoços, restaurante, room service, banquetes, bar e housekeeping com uma suite de agentes de IA pensados para F&B Managers e direções de hotel.",
    "heroTagline": "Toda a operativa de hotel coordenada num único sistema",
    "badge": "Para F&B Managers de hotel",
    "painsTitle": "O Que um F&B Manager de Hotel Não Pode Deixar de Resolver",
    "pains": [
      "Coordenar múltiplos pontos de venda ao mesmo tempo: pequeno-almoço buffet, restaurante à la carte, bar lobby, room service e banquetes",
      "Gerir equipas grandes com turnos rotativos 24/7 respeitando o acordo coletivo e descansos",
      "Manter APPCC distribuído por várias áreas de cozinha com consolidação ao F&B Director",
      "Reporting consolidado ao diretor do hotel e ao corporate com KPIs por linha de F&B",
      "Desenhar cartas sazonais para vários outlets sem que a equipa se afogue em papelada",
      "Gerir banquetes de casamentos e eventos corporativos conciliados com o F&B regular"
    ],
    "featuresTitle": "Como o AI Chef Pro Ajuda num Hotel Completo",
    "features": [
      {
        "icon": "Hotel",
        "title": "Kit de Tareas Hotel",
        "description": "Modelos específicos para pequeno-almoço buffet, restaurante, bar lobby, room service, banquetes e housekeeping num único sistema documental."
      },
      {
        "icon": "ChefHat",
        "title": "Chef Executivo Pro",
        "description": "Padronização de receitas e fichas técnicas em todos os outlets do hotel. Mesmo prato, mesma qualidade em restaurante, room service e banquete."
      },
      {
        "icon": "Calculator",
        "title": "Custos de receita por ponto de venda",
        "description": "Culinária Criativa entrega receita + custo de receita CSV; Kit de Escandallos Pro gere-o com os seus preços reais separando margem por outlet."
      },
      {
        "icon": "PartyPopper",
        "title": "Catering AI+",
        "description": "Para design e produção de banquetes de casamento, corporativos e eventos especiais do hotel."
      },
      {
        "icon": "Wine",
        "title": "Bar & Lounge AI+",
        "description": "Para coquetelaria do bar lobby, vinhos de restaurante e bebidas espirituosas com custo de receita profissional."
      },
      {
        "icon": "Users",
        "title": "Kit Gestión de Personal",
        "description": "Quadrantes para equipas grandes 24/7 com turnos rotativos respeitando o acordo coletivo do país. Refeição do Pessoal incluída."
      },
      {
        "icon": "ShieldCheck",
        "title": "Pack APPCC corporativo",
        "description": "APPCC distribuído por área de cozinha mas consolidado num único dashboard para o F&B Director."
      },
      {
        "icon": "BarChart3",
        "title": "Kit Plan Financiero",
        "description": "Dashboard com KPIs por ponto de venda: pequeno-almoço, restaurante, bar, room service, banquetes. Rácios de ocupação e produtividade."
      },
      {
        "icon": "BriefcaseBusiness",
        "title": "Gerente Restaurante Pro",
        "description": "Para os managers de cada outlet com reporting consolidado para o F&B Manager do hotel."
      }
    ],
    "workflowTitle": "Um Dia Real de um F&B Manager de Hotel com AI Chef Pro",
    "workflow": [
      "07:00 · Abertura do pequeno-almoço — a equipa arranca o buffet com a checklist do Kit de Tareas Hotel; você revê o dashboard de ocupação do hotel e ajusta a mise.",
      "09:30 · Catering AI+ — prepara o banquete de casamento do próximo sábado: menu, custo de receita e produção para 220 convidados.",
      "11:00 · Chef Executivo Pro — atualiza a ficha técnica do novo prato do restaurante e replica-se ao room service e ao menu de banquete com a mesma padronização.",
      "13:00 · Serviço de meio-dia — restaurante à la carte + bar lobby + room service ativos. A equipa coordena com modelos específicos de cada outlet.",
      "15:30 · Kit Plan Financiero — exporta KPIs por outlet do trimestre para reunião com a direção do hotel.",
      "17:00 · Bar & Lounge AI+ — desenha a nova carta de cocktails para o bar lobby com custo de receita profissional.",
      "19:30 · Quadrante da próxima semana — Kit Gestión de Personal com turnos rotativos respeitando o acordo coletivo, controlo de horas e refeição do pessoal gerada.",
      "23:00 · APPCC consolidado — registos dos 6 pontos de venda assinados e exportados, relatório ao F&B Director e ao corporate enviado em PDF."
    ],
    "productsTitle": "Modelos e Kits Descarregáveis para Hotéis",
    "productIds": [
      "kit-tareas-hotel",
      "kit-escandallos",
      "pack-appcc",
      "kit-gestion-personal",
      "kit-inventario",
      "kit-plan-financiero"
    ],
    "testimonialQuote": "Coordenar 6 pontos de venda de F&B num hotel de 200 quartos era um pesadelo constante. AI Chef Pro ordenou-nos tudo. O Kit de Tareas Hotel é ouro e o reporting ao diretor do hotel é agora automático em PDF. Subimos o RevPASH do restaurante 12 % em 4 meses só por ter melhor controlo.",
    "testimonialAuthor": "Cristina Núñez",
    "testimonialRole": "F&B Manager, hotel 4 estrelas com 200 quartos",
    "faqTitle": "Perguntas Frequentes de F&B Managers",
    "faqs": [
      {
        "q": "Funciona para hotel boutique ou grande cadeia?",
        "a": "Ambos. Os modelos escalam desde hotéis de 30 quartos até cadeias com centenas de propriedades. Há onboarding empresa para cadeias grandes."
      },
      {
        "q": "Cobre housekeeping além de F&B?",
        "a": "Sim. O Kit de Tareas Hotel inclui modelos específicos de housekeeping além dos 5 pontos de venda de F&B."
      },
      {
        "q": "Integra-se com o nosso PMS ou Opera?",
        "a": "Exporta Excel, PDF e CSV compatíveis com a maioria dos PMS e sistemas hoteleiros. Os dados podem ser integrados manualmente no fecho de cada turno ou jornada."
      },
      {
        "q": "Há plano empresa para cadeias hoteleiras?",
        "a": "Sim. A partir de certo número de propriedades há planos empresa com onboarding personalizado, dashboards consolidados por cadeia e suporte prioritário."
      },
      {
        "q": "Como gere os banquetes e eventos especiais?",
        "a": "Catering AI+ está integrado com o Kit Tareas Hotel para que os banquetes (casamentos, corporativos) conciliem com o F&B regular sem colidir produção nem equipa."
      },
      {
        "q": "E o controlo de custos por outlet?",
        "a": "O Kit Plan Financiero permite analisar food cost, produtividade e margem separadamente para pequeno-almoço, restaurante, bar lobby, room service e banquetes. Isso dá uma visão real de que outlet rende e qual não."
      }
    ],
    "ctaTitle": "O seu F&B de hotel coordenado e sem caos.",
    "ctaSubtitle": "Fale connosco para um onboarding personalizado ou comece com o plano Membro: 10 € por mês com 10.000 créditos.",
    "seo": {
      "title": "IA para Hotel Completo (F&B + Housekeeping): Restaurante, Bar, Banquetes | AI Chef Pro",
      "description": "Suite de IA para F&B Managers de hotel: pequeno-almoço buffet, restaurante, bar lobby, room service, banquetes e housekeeping com agentes especializados. Comece hoje.",
      "keywords": "IA hotel F&B, F&B Manager IA, software F&B hotel, gestão hotel IA, room service IA, banquete hotel IA, housekeeping software, hotel restaurant management IA, F&B Espanha",
      "ogImage": "https://aichef.pro/og/use-cases/hotel-completo.jpg"
    },
    "personalizationTitle": "Personalizado ao Seu Hotel desde o Minuto Um",
    "personalizationBody": "AI Chef Pro arranca com o agente «Quem Sou Eu?», um onboarding conversacional de 2 minutos em que lhe conta que tipo de hotel gere (boutique, 4 estrelas, grande cadeia, tudo incluído), número de quartos, que outlets de F&B opera e a que escala. A partir desse momento, cada agente —desde Chef Executivo Pro até ao Plano Financeiro— responde adaptado à realidade do seu hotel: tipo de hóspede, taxa de ocupação e operativa real. Não é um formulário: é uma conversa curta que torna a suite verdadeiramente útil para um F&B Manager de hotel.",
    "appsTitle": "Os Agentes IA que Vai Usar como F&B Manager",
    "apps": [
      {
        "name": "Chef Executivo Pro",
        "category": "Gastro Profile Pro",
        "description": "Padronização de receitas e fichas técnicas em todos os outlets do hotel."
      },
      {
        "name": "Gerente Restaurante Pro",
        "category": "Gastro Profile Pro",
        "description": "Assistente para os managers de cada outlet com reporting consolidado ao F&B Manager."
      },
      {
        "name": "Catering AI+",
        "category": "Conceitos de Negócio",
        "description": "Para banquetes de casamento, eventos corporativos e galas do hotel."
      },
      {
        "name": "Bar & Lounge AI+",
        "category": "Conceitos de Negócio",
        "description": "Para coquetelaria do bar lobby, vinhos de restaurante e bebidas espirituosas."
      },
      {
        "name": "Restaurantes Casuais AI+",
        "category": "Conceitos de Negócio",
        "description": "Para o restaurante à la carte do hotel e opções casuais do room service."
      },
      {
        "name": "Culinária Criativa",
        "category": "Criatividade Culinária",
        "description": "Desenvolvimento de pratos para todos os outlets com receita + custo de receita CSV."
      },
      {
        "name": "Pastelaria Criativa",
        "category": "Criatividade Culinária",
        "description": "Sobremesas de hotel: pequeno-almoço buffet, restaurante, room service e banquetes."
      },
      {
        "name": "Refeição do Pessoal",
        "category": "Gastro Profile Pro",
        "description": "Gerador de menus de staff para equipas grandes 24/7."
      },
      {
        "name": "ID Alergénios",
        "category": "Ferramentas e Utilitários",
        "description": "Identificação automática de alergénios por receita, crítica em hotéis internacionais."
      },
      {
        "name": "Mermas Genéricas",
        "category": "Ferramentas e Utilitários",
        "description": "Dados precisos de mermas e rendimentos para controlo multi-outlet."
      },
      {
        "name": "GastroIMG Gen+",
        "category": "Gastro Conhecimento",
        "description": "Fotografia gastronómica para web do hotel, menu de room service e banquetes."
      }
    ],
    "metrics": [
      {
        "value": "+12 %",
        "label": "RevPASH em 4 meses"
      },
      {
        "value": "6",
        "label": "pontos de venda coordenados"
      },
      {
        "value": "×5",
        "label": "velocidade de reporting ao diretor"
      },
      {
        "value": "11+",
        "label": "agentes para o seu hotel"
      }
    ],
    "beforeAfter": {
      "beforeTitle": "Sem AI Chef Pro",
      "beforeItems": [
        "6 outlets de F&B com 6 sistemas distintos: pequeno-almoço, restaurante, bar, room service, banquetes e housekeeping inconexos",
        "APPCC em papel impresso disperso em cada cozinha do hotel, problema em inspeções",
        "Banquetes de casamento colidem com produção do restaurante regular e room service",
        "Reporting ao F&B Director e ao corporate com arquivos dispersos e sem estrutura",
        "Quadrantes 24/7 quadrados em Excel manual com 50+ funcionários"
      ],
      "afterTitle": "Com AI Chef Pro",
      "afterItems": [
        "Kit de Tareas Hotel com modelos específicos por outlet, tudo coordenado num único sistema",
        "APPCC consolidado em dashboard: registos desde o telemóvel, pronto para inspeção e para corporate",
        "Banquetes integrados com Catering AI+ que respeita produção do F&B regular",
        "Reporting ao diretor e corporate em PDF direto desde o Kit Plan Financiero",
        "Quadrantes com Kit Gestión de Personal: turnos 24/7 respeitando o acordo coletivo sem desalinhamentos"
      ]
    },
    "galleryTitle": "Como Funciona o F&B de um Hotel Completo",
    "gallerySubtitle": "O que vai coordenar com AI Chef Pro: restaurante, pequeno-almoço buffet, banquete, bar lobby, room service e briefing F&B com cozinha.",
    "galleryImages": [
      "/lovable-uploads/ai-gallery/use-case-hotel-completo-hero.jpg",
      "/lovable-uploads/ai-gallery/use-case-hotel-completo-breakfast.jpg",
      "/lovable-uploads/ai-gallery/use-case-hotel-completo-banquet.jpg",
      "/lovable-uploads/ai-gallery/use-case-hotel-completo-bar.jpg",
      "/lovable-uploads/ai-gallery/use-case-hotel-completo-roomservice.jpg",
      "/lovable-uploads/ai-gallery/use-case-hotel-completo-fbteam.jpg"
    ]
  },
  "heladeria": {
    "h1": "IA para Gelataria Artesanal",
    "heroSubtitle": "Custo de receita por sabor com custo real de leite, fruta e frutos secos, planeie produção sazonal e capture branding profissional com uma suite de agentes de IA especializados em gelataria artesanal.",
    "heroTagline": "Gelado com margem real e sem papelada",
    "badge": "Para gelatarias artesanais",
    "painsTitle": "O Que uma Gelataria Artesanal Não Pode Deixar de Resolver",
    "pains": [
      "Custos de receita complexos com leite, nata, frutas frescas, frutos secos e pastas profissionais que requerem cálculo por kg e por bola",
      "Quebras elevadas no obrador (mantecadora, abatimento) e na montra (exposição prolongada, rotação) sem controlo real",
      "Rastreabilidade APPCC com produtos sensíveis: leite, ovo em algumas bases, frutos secos com alergénios e temperaturas críticas",
      "Sazonalidade extrema: época alta de maio a setembro, período de baixa invernal que é preciso rentabilizar com tartes e sobremesas",
      "Diferenciar-se em zona concorrida com sabores próprios, branding visual de montra, embalagem e redes sociais",
      "Captar pedidos de tartes geladas e sobremesas à medida com margem enquanto se gere o dia a dia de serviço"
    ],
    "featuresTitle": "Como AI Chef Pro Ajuda na Gelataria Artesanal",
    "features": [
      {
        "icon": "IceCream",
        "title": "Gelataria Criativa",
        "description": "Agente especializado em gelataria artesanal: bases branca, amarela, fruta, sorbets, equilíbrio de açúcares, sólidos e gorduras para textura ótima."
      },
      {
        "icon": "Cake",
        "title": "Pastelaria Criativa",
        "description": "Para tartes geladas, semifrios, sobremesas de colher e combinações gelado + pão-de-ló que abrem o ticket médio no período de baixa invernal."
      },
      {
        "icon": "Cookie",
        "title": "Chocolataria Criativa",
        "description": "Para coberturas, bombons gelados, pralinés e combinações avançadas gelado + chocolate."
      },
      {
        "icon": "Calculator",
        "title": "Custos de receita por sabor",
        "description": "Gelataria Criativa entrega receita + ficha de custo CSV com equilíbrio técnico (açúcares, sólidos, gorduras); Kit de Escandallos Pro gere-o com margem real por kg, por bola e por cone."
      },
      {
        "icon": "CheckSquare",
        "title": "Kit de Tareas Heladería",
        "description": "Modelos: preparação da mantecadora, abatimento, reposição de montra, controlo de temperaturas, rotação de sabores, encerramento."
      },
      {
        "icon": "ShieldCheck",
        "title": "Pack APPCC gelataria",
        "description": "Rastreabilidade de leite, fruta fresca, frutos secos com alergénios e temperaturas críticas em câmara, mantecadora e montra."
      },
      {
        "icon": "Calendar",
        "title": "Gastro Calendar",
        "description": "Planeamento sazonal com picos-chave: Dia da Mãe, primavera, verão, São Valentim e tartes geladas de Natal. Calendário editorial para montra."
      },
      {
        "icon": "Image",
        "title": "GastroIMG Gen+ + InstaFlow AI Pro",
        "description": "Fotografia gastronómica IA + conteúdo para Instagram: a gelataria artesanal vive do impacto visual de cubas e cones."
      },
      {
        "icon": "BarChart3",
        "title": "Sosa Ingredients",
        "description": "Assistente do catálogo Sosa para texturas profissionais, neutros, estabilizantes e pastas concentradas de gelataria."
      }
    ],
    "workflowTitle": "Um Dia Real numa Gelataria Artesanal com AI Chef Pro",
    "workflow": [
      "07:00 · Abertura — checklist Kit de Tareas Heladería: revisão de câmara, abatimento de misturas preparadas na véspera, preparação da mantecadora.",
      "08:30 · Gelataria Criativa — desenvolve um novo sabor de época (frutos vermelhos com balsâmico). Culinária Criativa entrega receita + ficha de custo CSV com equilíbrio técnico.",
      "09:30 · Kit de Escandallos Pro — carrega o CSV com os seus preços reais de fruta de época e leite local, valida margem por kg e por bola.",
      "11:00 · Produção do dia — passa misturas pela mantecadora, abate a -18 °C, etiqueta com APPCC.",
      "13:30 · Reposição de montra com etiquetas profissionais, controlo de quebras de exposição por sabor.",
      "16:00 · Pastelaria Criativa — desenvolve uma tarte gelada para o Dia da Mãe com semifrio de pistáchio, base de pão-de-ló e cobertura. Ficha de custo CSV pronta.",
      "18:00 · GastroIMG Gen+ + InstaFlow AI Pro — gera a imagem de referência do novo sabor e os posts de Instagram para o lançamento.",
      "21:00 · Encerramento — limpeza profunda, APPCC assinado, planeamento de misturas a abater esta noite para amanhã."
    ],
    "productsTitle": "Modelos e Kits Descarregáveis para Gelataria",
    "productIds": [
      "kit-tareas-heladeria",
      "kit-escandallos",
      "pack-appcc",
      "kit-inventario",
      "kit-gestion-personal",
      "pro-prompts-ebook"
    ],
    "testimonialQuote": "Passámos de folhas soltas a sistema. Com a Gelataria Criativa equilibramos açúcares e sólidos com critério técnico, e o Kit de Escandallos Pro confirma-me a margem real por bola e por kg com os preços atuais de fruta. A quebra caiu 40 % em 3 meses e descobrimos que dois sabores históricos não eram rentáveis.",
    "testimonialAuthor": "Laura Costa",
    "testimonialRole": "Proprietária, gelataria artesanal com obrador próprio",
    "faqTitle": "Perguntas Frequentes de Gelatarias",
    "faqs": [
      {
        "q": "Serve para gelataria pequena, gelataria italiana ou cadeia?",
        "a": "Para as três. Os modelos escalam desde gelataria familiar de um único ponto até cadeia com vários locais e obrador centralizado. A metodologia é a mesma: receita equilibrada → ficha de custo CSV → margem real."
      },
      {
        "q": "Cobre o equilíbrio técnico de bases (açúcares, sólidos, gorduras)?",
        "a": "Sim. A Gelataria Criativa raciocina como geladeiro profissional: equilíbrio de açúcares com sacarose, dextrose e açúcar invertido; sólidos totais e gorduras segundo norma técnica; equilíbrio para evitar cristalização e manter cremosidade."
      },
      {
        "q": "Como gerimos a sazonalidade forte da gelataria?",
        "a": "O Gastro Calendar planeia com antecedência os picos (Dia da Mãe, verão, São Valentim, Natal de tartes geladas) e o período de baixa invernal com tartes, semifrios e sobremesas de colher para manter o ticket médio. O Kit Plan Financiero projeta o cash flow sazonal realista."
      },
      {
        "q": "Há controlo de quebras no obrador e na montra?",
        "a": "Sim. As Mermas Genéricas entrega dados por processo (mantecadora, abatimento, exposição prolongada na montra, rotação de sabores). Integram-se no custo de receita do Kit de Escandallos Pro para que o custo real reflita as quebras, não apenas o ingrediente bruto."
      },
      {
        "q": "Gera conteúdo para montra, redes e Google Maps?",
        "a": "Sim. O GastroIMG Gen+ gera imagens de referência profissionais de cada sabor para montra, web e redes; o InstaFlow AI Pro programa Instagram com calendário editorial; o MenuDish Local SEO captura clientes locais que procuram \"gelataria perto de mim\". Lembre-se de que a imagem IA é de referência visual: a foto definitiva é feita por si com a sua cuba e empratamento real."
      }
    ],
    "ctaTitle": "A sua gelataria com margem clara e branding profissional.",
    "ctaSubtitle": "Comece com o onboarding de 2 minutos. Plano Membro por 10 € por mês com 10.000 créditos para usar todos os agentes.",
    "seo": {
      "title": "IA para Gelataria Artesanal: Custos de Receita por Sabor, Sazonalidade e Branding | AI Chef Pro",
      "description": "Suite de IA para gelatarias artesanais: Gelataria Criativa, custos de receita por sabor com equilíbrio técnico, APPCC, planeamento sazonal e branding visual. Comece hoje.",
      "keywords": "IA gelataria, software gelataria, custos de receita gelado, gelataria artesanal IA, equilíbrio técnico gelado, gelataria IA, gelataria Espanha",
      "ogImage": "https://aichef.pro/og/use-cases/heladeria.jpg"
    },
    "personalizationTitle": "Personalizado à Sua Gelataria desde o Primeiro Minuto",
    "personalizationBody": "AI Chef Pro arranca com o agente «Quem Sou Eu?», um onboarding conversacional de 2 minutos em que lhe conta que tipo de gelataria opera (gelataria italiana, gelataria artesanal espanhola, gelataria com obrador próprio ou sem obrador, mista com pastelaria), tamanho da equipa, cidade e estilo. Cada agente — desde Gelataria Criativa até Gastro Calendar — responde adaptado ao seu produto, mercado e operativa real.",
    "appsTitle": "Os Agentes de IA que Vai Usar na Sua Gelataria",
    "apps": [
      {
        "name": "Gelataria Criativa",
        "category": "Criatividade Culinária",
        "description": "Agente especializado em gelataria artesanal com equilíbrio técnico de bases, açúcares, sólidos e gorduras."
      },
      {
        "name": "Pastelaria Criativa",
        "category": "Criatividade Culinária",
        "description": "Tartes geladas, semifrios, sobremesas de colher e combinações gelado + pão-de-ló."
      },
      {
        "name": "Chocolataria Criativa",
        "category": "Criatividade Culinária",
        "description": "Coberturas, bombons gelados, pralinés e combinações avançadas com chocolate."
      },
      {
        "name": "Culinária Criativa",
        "category": "Criatividade Culinária",
        "description": "Desenvolvimento de sabores e receitas com receita + ficha de custo CSV."
      },
      {
        "name": "Sosa Ingredients",
        "category": "Fornecedores Gastro",
        "description": "Catálogo Sosa: neutros, estabilizantes, pastas concentradas e texturas profissionais."
      },
      {
        "name": "Mermas Genéricas",
        "category": "Ferramentas e Utilitários",
        "description": "Dados precisos de quebras em mantecadora, abatimento e exposição em montra."
      },
      {
        "name": "ID Alergénios",
        "category": "Ferramentas e Utilitários",
        "description": "Identificação automática de alergénios por sabor: laticínios, frutos secos, glúten, ovo."
      },
      {
        "name": "GastroIMG Gen+",
        "category": "Conhecimento Gastro",
        "description": "Fotografia gastronómica IA de referência para montra, web e redes sociais."
      },
      {
        "name": "InstaFlow AI Pro",
        "category": "Conteúdos e Redes Sociais",
        "description": "Instagram com calendário editorial: a gelataria vive do impacto visual."
      },
      {
        "name": "MenuDish Local SEO",
        "category": "Conteúdos e Redes Sociais",
        "description": "Captar clientes locais que procuram \"gelataria perto de mim\" no Google e Maps."
      },
      {
        "name": "Gastro Calendar",
        "category": "Conteúdos e Redes Sociais",
        "description": "Planeamento sazonal: Dia da Mãe, verão, São Valentim, tartes geladas de Natal."
      },
      {
        "name": "Gerador de Pins Pinterest",
        "category": "Conteúdos e Redes Sociais",
        "description": "O Pinterest captura tráfego orgânico estável para tartes geladas e semifrios."
      }
    ],
    "metrics": [
      {
        "value": "+5 pp",
        "label": "margem após calcular custos de receita"
      },
      {
        "value": "−40 %",
        "label": "quebras em obrador e montra"
      },
      {
        "value": "×3",
        "label": "engagement no Instagram com GastroIMG"
      },
      {
        "value": "12+",
        "label": "agentes para a sua gelataria"
      }
    ],
    "beforeAfter": {
      "beforeTitle": "Sem AI Chef Pro",
      "beforeItems": [
        "Custos de receita sem equilíbrio técnico, sabores que cristalizam ou perdem cremosidade sem saber porquê",
        "Quebras em mantecadora, abatimento e montra sem rastreabilidade real",
        "Montra e redes sociais improvisadas: fotos do telemóvel, sem continuidade",
        "Sazonalidade reativa: o inverno afunda o ticket sem alternativas",
        "APPCC em papel impresso disperso pelo obrador"
      ],
      "afterTitle": "Com AI Chef Pro",
      "afterItems": [
        "Custos de receita profissionais por sabor com equilíbrio técnico e margem real por bola e por kg",
        "Quebras controladas com Mermas Genéricas e modelos específicos de gelataria",
        "GastroIMG Gen+ + InstaFlow AI Pro geram conteúdo visual estável e profissional",
        "Gastro Calendar planeia picos e períodos de baixa com tartes geladas, semifrios e sobremesas de colher",
        "APPCC desde o telemóvel com registos prontos para inspeção"
      ]
    },
    "galleryTitle": "Como Funciona uma Gelataria Artesanal",
    "gallerySubtitle": "O que vai coordenar com AI Chef Pro: montra, mantecadora, obrador, sabores, cones e equipa. Imagens geradas com IA como referência visual do conceito.",
    "galleryImages": [
      "/lovable-uploads/ai-gallery/use-case-heladeria-hero.jpg",
      "/lovable-uploads/ai-gallery/use-case-heladeria-vitrine.jpg",
      "/lovable-uploads/ai-gallery/use-case-heladeria-mantecadora.jpg",
      "/lovable-uploads/ai-gallery/use-case-heladeria-flavors.jpg",
      "/lovable-uploads/ai-gallery/use-case-heladeria-conos.jpg",
      "/lovable-uploads/ai-gallery/use-case-heladeria-team.jpg"
    ]
  },
  "chocolateria": {
    "h1": "IA para Chocolataria e Bombonaria",
    "heroSubtitle": "Custeio por bombom com custo real de cacau e custo hora de produção, planeie produção sazonal e capture branding profissional com uma suite de agentes de IA especializados em chocolataria artesanal.",
    "heroTagline": "Bombom com margem real e sem papelada",
    "badge": "Para chocolatarias e bombonarias artesanais",
    "painsTitle": "O Que uma Chocolataria Não Pode Deixar de Resolver",
    "pains": [
      "Cacau com preço volátil que muda o custo real todas as semanas sem avisar e obriga a recalcular custeios constantemente",
      "Quebras no atelier (temperagem falhada, moldes mal formados, recortes) e na montra (rotação, exposição prolongada)",
      "Sazonalidade extrema: Natal, Dia dos Namorados, Páscoa, Bolo Rei concentram uma elevada percentagem da faturação anual",
      "Rastreabilidade APPCC com produto delicado: cacau, lacticínios, frutos secos, álcoois e temperaturas críticas em cada passo",
      "Diferenciar-se numa zona concorrida com bombons de autor, packaging premium e storytelling visual de marca",
      "Captar pedidos corporativos e casamentos com margem enquanto se gere a chocolataria diária"
    ],
    "featuresTitle": "Como o AI Chef Pro Ajuda na Chocolataria",
    "features": [
      {
        "icon": "Cookie",
        "title": "Chocolataria Criativa",
        "description": "Agente especializado em chocolataria profissional: bombons, ganaches, pralinés, tabletes, coberturas e técnica de temperagem."
      },
      {
        "icon": "Cake",
        "title": "Pastelaria Criativa",
        "description": "Para sobremesas com chocolate, docinhos, brownies e combinações avançadas chocolate + pastelaria que diversificam o catálogo."
      },
      {
        "icon": "Calculator",
        "title": "Custeio por peça com custo hora de produção",
        "description": "A Chocolataria Criativa entrega receita + custeio CSV; o Kit de Escandallos Pro faz a gestão com custo hora de produção integrado na margem real por bombom e por caixa."
      },
      {
        "icon": "CheckSquare",
        "title": "Kit de Tareas Chocolatería",
        "description": "Modelos: temperagem, moldagem, recheio com ganache, montagem, packaging, controlo de temperaturas na câmara."
      },
      {
        "icon": "ShieldCheck",
        "title": "Pack APPCC chocolataria",
        "description": "Rastreabilidade de cacau, lacticínios, frutos secos, álcoois e conservação profissional com curvas de temperagem documentadas."
      },
      {
        "icon": "Calendar",
        "title": "Gastro Calendar",
        "description": "Planeamento sazonal com datas-chave: Natal, Dia dos Namorados, Páscoa, Bolo Rei, Dia da Mãe. Calendário editorial para a montra."
      },
      {
        "icon": "Image",
        "title": "GastroIMG Gen+ + Gerador de Pins Pinterest",
        "description": "Fotografia gastronómica IA + Pinterest, onde a chocolataria premium captura tráfego orgânico estável."
      },
      {
        "icon": "BarChart3",
        "title": "Sosa Ingredients",
        "description": "Assistente do catálogo Sosa para coberturas técnicas, pastas concentradas, frutos secos e aromas profissionais."
      },
      {
        "icon": "Sparkles",
        "title": "Mermas Genéricas",
        "description": "Dados precisos de quebras por processo (temperagem, moldagem, recortes, exposição em montra) integrados no custeio."
      }
    ],
    "workflowTitle": "Um Dia Real numa Chocolataria com AI Chef Pro",
    "workflow": [
      "07:00 · Abertura — checklist Kit de Tareas Chocolatería: revisão da câmara, pré-cristalização do chocolate de cobertura, preparação dos moldes.",
      "08:30 · Chocolataria Criativa — desenvolve um novo bombom para o Dia dos Namorados com ganache de framboesa e baunilha. A Culinária Criativa entrega receita + custeio CSV.",
      "09:30 · Kit de Escandallos Pro — carrega o CSV com os seus preços reais de cacau e custo hora de produção integrado, valida a margem por bombom e por caixa de 12.",
      "11:00 · Produção do dia — temperagem em mármore, moldagem, enchimento de ganache com saco de pasteleiro, abatimento e desenformagem.",
      "14:00 · Reposição da montra com caixas profissionais e etiquetas, controlo de quebras de exposição.",
      "16:00 · Gastro Calendar — prepara o planeamento da produção de Natal (caixas oferta corporativas com 8 semanas de antecedência).",
      "18:00 · GastroIMG Gen+ + Gerador de Pins Pinterest — gera fotografias de referência do novo bombom e pins otimizados para o Pinterest.",
      "20:00 · Encerramento — limpeza profunda, APPCC assinado, planeamento de misturas para abater esta noite."
    ],
    "productsTitle": "Modelos e Kits Descarregáveis para Chocolataria",
    "productIds": [
      "kit-tareas-chocolateria",
      "kit-escandallos",
      "pack-appcc",
      "kit-inventario",
      "kit-gestion-personal",
      "pro-prompts-ebook"
    ],
    "testimonialQuote": "Produzir 12 000 bombons para o Natal sem sistema era caos. Com a Chocolataria Criativa para design, o Kit de Escandallos Pro para margem real com cacau atualizado e o Gastro Calendar para planeamento sazonal, salvámos a época e subimos a margem 7 pontos. A questão das caixas corporativas agora fecha-se numa chamada com proposta profissional.",
    "testimonialAuthor": "Mónica Salazar",
    "testimonialRole": "Mestra chocolatier e proprietária",
    "faqTitle": "Perguntas Frequentes de Chocolatarias",
    "faqs": [
      {
        "q": "Serve para chocolataria artesanal pequena ou cadeia?",
        "a": "Para ambas. Os modelos escalam desde um atelier familiar de 2 pessoas até produção para vários pontos de venda. A metodologia é a mesma: receita → custeio CSV → margem real com custo hora de produção."
      },
      {
        "q": "Cobre bombonaria, tabletes, coberturas e pralinés?",
        "a": "Sim. A Chocolataria Criativa raciocina como chocolatier profissional: temperagem de cobertura por curvas, ganaches com equilíbrio de água e gordura, pralinés com torra de frutos secos, tabletes recheadas com técnica de cristalização."
      },
      {
        "q": "Como é que gerimos o preço volátil do cacau?",
        "a": "O Kit de Escandallos Pro recalcula instantaneamente a margem real quando atualiza o preço da cobertura. As Mermas Genéricas adicionam o custo das quebras por processo. Assim, a margem reflete sempre o custo atual, não o de há três meses."
      },
      {
        "q": "Gera conteúdo para montra, redes e packaging?",
        "a": "Sim. O GastroIMG Gen+ gera imagens de referência profissionais de cada bombom para montra, web e redes; o Gerador de Pins Pinterest + InstaFlow AI Pro programam conteúdo visual; o MenuDish Local SEO capta clientes locais. Lembre-se de que a imagem IA é de referência visual: a foto definitiva é feita por si com o seu bombom empratado real."
      },
      {
        "q": "Como é que me ajuda com a sazonalidade forte?",
        "a": "O Gastro Calendar planeia as épocas-chave (Natal, Dia dos Namorados, Páscoa, Bolo Rei, Dia da Mãe) com 8-12 semanas de antecedência. O Kit Plan Financiero projeta o cash flow sazonal realista para que chegue com produção e caixa a cada pico."
      }
    ],
    "ctaTitle": "A sua chocolataria com margem clara e branding profissional.",
    "ctaSubtitle": "Comece com o onboarding de 2 minutos. Plano Membro por 10 € por mês com 10.000 créditos para usar todos os agentes.",
    "seo": {
      "title": "IA para Chocolataria e Bombonaria: Custeios, Sazonalidade e Branding | AI Chef Pro",
      "description": "Suite de IA para chocolatarias artesanais: Chocolataria Criativa, custeios por bombom com custo hora de produção, APPCC, planeamento sazonal e branding. Comece hoje.",
      "keywords": "IA chocolataria, software chocolataria, custeios bombom, chocolataria artesanal IA, técnica temperagem, bombonaria Espanha, planeamento Natal chocolataria",
      "ogImage": "https://aichef.pro/og/use-cases/chocolateria.jpg"
    },
    "personalizationTitle": "Personalizado para a Sua Chocolataria desde o Primeiro Minuto",
    "personalizationBody": "O AI Chef Pro arranca com o agente «Quem Sou Eu?», um onboarding conversacional de 2 minutos em que lhe conta que tipo de chocolataria opera (artesanal, bombonaria de autor, chocolataria com cafeteria, atelier para venda a restauração), dimensão da equipa, cidade e especialidade. Cada agente — desde a Chocolataria Criativa até ao Gastro Calendar — responde adaptado ao seu produto, mercado e operativa real.",
    "appsTitle": "Os Agentes de IA que Vai Usar na Sua Chocolataria",
    "apps": [
      {
        "name": "Chocolataria Criativa",
        "category": "Criatividade Culinária",
        "description": "Agente especializado em chocolataria profissional: bombons, ganaches, pralinés, tabletes e técnica de temperagem."
      },
      {
        "name": "Pastelaria Criativa",
        "category": "Criatividade Culinária",
        "description": "Sobremesas com chocolate, docinhos, brownies e combinações avançadas."
      },
      {
        "name": "Culinária Criativa",
        "category": "Criatividade Culinária",
        "description": "Desenvolvimento de novas peças com receita + custeio CSV."
      },
      {
        "name": "Sosa Ingredients",
        "category": "Fornecedores Gastro",
        "description": "Catálogo Sosa: coberturas técnicas, pastas concentradas, frutos secos e aromas profissionais."
      },
      {
        "name": "tSpoonLab Agent",
        "category": "Fornecedores Gastro",
        "description": "Assistente do catálogo tSpoonLab para aplicações avançadas de chocolataria."
      },
      {
        "name": "Mermas Genéricas",
        "category": "Ferramentas e Utilitários",
        "description": "Quebras por processo (temperagem, moldagem, recortes, exposição em montra) no custeio."
      },
      {
        "name": "ID Alergénios",
        "category": "Ferramentas e Utilitários",
        "description": "Identificação automática de alergénios por bombom: lacticínios, frutos secos, glúten, álcoois."
      },
      {
        "name": "GastroIMG Gen+",
        "category": "Conhecimento Gastro",
        "description": "Fotografia gastronómica IA de referência para montra, web, packaging e redes."
      },
      {
        "name": "Gerador de Pins Pinterest",
        "category": "Conteúdos e Redes Sociais",
        "description": "O Pinterest capta tráfego orgânico estável para chocolataria premium."
      },
      {
        "name": "InstaFlow AI Pro",
        "category": "Conteúdos e Redes Sociais",
        "description": "Instagram com calendário editorial para chocolataria de autor."
      },
      {
        "name": "MenuDish Local SEO",
        "category": "Conteúdos e Redes Sociais",
        "description": "Captar clientes locais que procuram \"chocolataria artesanal perto\" no Google e no Maps."
      },
      {
        "name": "Gastro Calendar",
        "category": "Conteúdos e Redes Sociais",
        "description": "Planeamento sazonal: Natal, Dia dos Namorados, Páscoa, Bolo Rei, Dia da Mãe."
      }
    ],
    "metrics": [
      {
        "value": "+7 pp",
        "label": "margem após custear bombons"
      },
      {
        "value": "−35 %",
        "label": "quebras no atelier e na montra"
      },
      {
        "value": "×2",
        "label": "pedidos corporativos de Natal"
      },
      {
        "value": "12+",
        "label": "agentes para a sua chocolataria"
      }
    ],
    "beforeAfter": {
      "beforeTitle": "Sem AI Chef Pro",
      "beforeItems": [
        "Custeios sem custo hora de produção, bombons complexos em perdas sem saber",
        "Cacau volátil que desequilibra os preços sem recalcular em tempo real",
        "Quebras na temperagem, moldagem e montra sem rastreabilidade real",
        "Produção sazonal reativa: chega tarde ao Natal e perde pedidos corporativos",
        "APPCC em papel impresso disperso pelo atelier"
      ],
      "afterTitle": "Com AI Chef Pro",
      "afterItems": [
        "Custeio profissional por bombom com custo hora de produção integrado e cacau atualizável",
        "Quebras controladas com Mermas Genéricas e modelos específicos de chocolataria",
        "Gerador de Pins Pinterest + InstaFlow + GastroIMG Gen+ captam tráfego estável e pedidos",
        "Gastro Calendar planeia o Natal e o Dia dos Namorados com 8-12 semanas de antecedência",
        "APPCC a partir do telemóvel com registos prontos para inspeção"
      ]
    },
    "galleryTitle": "Como Funciona uma Chocolataria Artesanal",
    "gallerySubtitle": "O que vai coordenar com o AI Chef Pro: montra, atelier, temperagem, bombons, exposição e equipa. Imagens geradas com IA como referência visual do conceito.",
    "galleryImages": [
      "/lovable-uploads/ai-gallery/use-case-chocolateria-hero.jpg",
      "/lovable-uploads/ai-gallery/use-case-chocolateria-obrador.jpg",
      "/lovable-uploads/ai-gallery/use-case-chocolateria-bonbons.jpg",
      "/lovable-uploads/ai-gallery/use-case-chocolateria-temperado.jpg",
      "/lovable-uploads/ai-gallery/use-case-chocolateria-display.jpg",
      "/lovable-uploads/ai-gallery/use-case-chocolateria-team.jpg"
    ]
  },
  "restaurante-creativo": {
    "h1": "IA para Restaurante Criativo e de Autor",
    "heroSubtitle": "Brainstorming gastronómico, P&D vanguardista, escandallos de técnica avançada, fichas técnicas premium e storytelling para restaurantes de autor com uma suite de agentes de IA gastronómica de nível profissional.",
    "heroTagline": "Criatividade com sistema, vanguardia com margen",
    "badge": "Para restaurantes criativos e de autor",
    "painsTitle": "O Que um Restaurante Criativo Não Pode Deixar de Resolver",
    "pains": [
      "Cartas que cambian cada 6-12 semanas com P&D contínuo e muita experimentação",
      "Escandallos complexos com técnicas avançadas (esferificações, fermentações, coções longas, deshidratados)",
      "Equipas pequenas com dedicação intensa que necessitam documentação profissional, não improvisação",
      "Storytelling e comunicação com cliente, prensa e redes são alavanca chave de marca",
      "Menus degustação longos com escandallo total e sequência coerente de passes",
      "Diferenciar-se num nicho saturado de propostas criativas e captar o comensal exigente"
    ],
    "featuresTitle": "Como AI Chef Pro Ajuda num Restaurante Criativo",
    "features": [
      {
        "icon": "Sparkles",
        "title": "Culinária Criativa + Food Pairing AI",
        "description": "Chuva de ideias para pratos de autor por temporada, ingrediente ou técnica com base científica. Culinária Criativa entrega receita + escandallo CSV."
      },
      {
        "icon": "Beaker",
        "title": "Fermentus Con AI+",
        "description": "P&D gastronómico de vanguardia: koji, kombuchas, shoyus, garums, lactofermentos e técnicas inovadoras com respaldo profissional."
      },
      {
        "icon": "Leaf",
        "title": "VegChef Plant-Based",
        "description": "Culinária plant-based, vegana e vegetariana avançada para pratos de autor com técnica profissional e nutricional."
      },
      {
        "icon": "Calculator",
        "title": "Escandallos de técnica avançada",
        "description": "Kit de Escandallos Pro: cargas o CSV de Culinária Criativa com os seus precios reales para pratos com técnicas custosas e processos longos."
      },
      {
        "icon": "Search",
        "title": "Sonar Deep Research",
        "description": "Investigação profunda de tendências, produtores artesanais, técnicas emergentes e referências da vanguardia mundial."
      },
      {
        "icon": "MessageSquare",
        "title": "BlogPost SEO Gen+",
        "description": "Storytelling para blog do restaurante, dossier de prensa e comunicação com meios gastronómicos."
      },
      {
        "icon": "Image",
        "title": "GastroIMG Gen+",
        "description": "Fotografia gastronómica IA de alto nível para fichas técnicas, prensa, web do restaurante e redes."
      },
      {
        "icon": "BookOpen",
        "title": "Sosa Ingredients + tSpoonLab Agent",
        "description": "Assistentes para seleção de ingredientes técnicos de Sosa e tSpoonLab, essenciais para culinária de autor."
      },
      {
        "icon": "GraduationCap",
        "title": "Léxico Gastronómico + Pro Prompts eBook",
        "description": "Tutor de definições técnicas e científicas + 300+ prompts profissionais para criatividade e comunicação."
      }
    ],
    "workflowTitle": "Um Dia Real num Restaurante Criativo com AI Chef Pro",
    "workflow": [
      "08:30 · Sonar Deep Research — investiga tendências e produtos de temporada em mercados europeos para inspiração da próxima mudança de carta.",
      "10:00 · Culinária Criativa + Food Pairing AI — desenvolve 14 pratos para o novo menu degustação com técnica e escandallo CSV inicial.",
      "12:00 · Fermentus Con AI+ — trabalha a base de um fermentado clave do menu: koji de cevada inoculado para 4 pratos.",
      "14:00 · Sosa Ingredients + tSpoonLab Agent — seleciona ingredientes técnicos para texturas e aplicações.",
      "15:30 · Kit de Escandallos Pro — cargas os CSV com os seus precios reales e descarta 4 pratos que não quadran à margen objetivo (32 %).",
      "17:00 · Pro Prompts eBook — redacta storytelling para os 10 pratos finais: nome, narrativa e ficha técnica completa.",
      "18:30 · GastroIMG Gen+ — genera fotografias de cada prato para dossier de prensa e web do restaurante.",
      "19:30 · Servicio — equipa coordenada com fichas técnicas centralizadas, passes do menu degustação com sequência validada."
    ],
    "productsTitle": "Modelos e Kits Descarregáveis para Restaurante Criativo",
    "productIds": [
      "kit-tareas-restaurante-creativo",
      "kit-escandallos",
      "pro-prompts-ebook",
      "pack-appcc",
      "kit-gestion-personal",
      "kit-inventario"
    ],
    "testimonialQuote": "Cambio a carta cada 6 semanas e antes era uma semana de papelório de encerramento só entre escandallos, fichas e storytelling. Agora com AI Chef Pro esse encerramento faz-se em 2 dias: Culinária Criativa propõe, Fermentus dá-me suporte de P&D, Sonar Deep Research aporta tendências, e o Kit de Escandallos Pro cierra a margen. É literalmente como ter uma equipa de P&D extra.",
    "testimonialAuthor": "Adrián Lago",
    "testimonialRole": "Chef e proprietário, restaurante de autor com 30 lugares",
    "faqTitle": "Perguntas Frequentes de Restaurantes Criativos",
    "faqs": [
      {
        "q": "A IA entende técnica de autor avançada?",
        "a": "Sí. Culinária Criativa, Fermentus Con AI+, Food Pairing AI, VegChef e os receitários por país estão treinados com conhecimento profissional: técnicas como esferificações, fermentações longas, coções controladas, gelificações, espumas, deshidratados e processos de vanguardia."
      },
      {
        "q": "Hay menus degustação específicos?",
        "a": "Sí. O Kit de Tareas Restaurante Creativo e o Kit de Escandallos Pro têm modelos para menus degustação com escandallo total, sequência de passes e maridaje."
      },
      {
        "q": "Cubre P&D e prova de pratos?",
        "a": "Sí. Sonar Deep Research aporta tendências e referências; Culinária Criativa + Fermentus desenvolvem pratos; Pro Prompts eBook tem 300+ prompts específicos para P&D iterativo."
      },
      {
        "q": "Genera storytelling para prensa e guías?",
        "a": "Sí. BlogPost SEO Gen+ + Pro Prompts eBook + GastroIMG Gen+ permiten redactar dossier de prensa, comunicação com guías Michelin/Repsol/50Best e notas para meios gastronómicos."
      },
      {
        "q": "Funciona para fermentação de vanguardia?",
        "a": "Fermentus Con AI+ é o agente mais usado por chefs de autor: cobre koji, kombucha, shoyu, miso, garum, lactofermentos e processos inovadores com respaldo científico."
      },
      {
        "q": "Como se integra com Sosa e outros fornecedores técnicos?",
        "a": "Sosa Ingredients e tSpoonLab Agent são assistentes específicos do catálogo de cada fornecedor: ajudam a selecionar texturas, aditivos e aplicações técnicas com critério profissional."
      }
    ],
    "ctaTitle": "Criatividade com sistema, vanguardia com margen.",
    "ctaSubtitle": "Comece com o onboarding de 2 minutos. Plano Membro por 10 € por mês com 10.000 créditos para usar todos os agentes.",
    "seo": {
      "title": "IA para Restaurante Criativo e de Autor: P&D, Vanguardia e Storytelling | AI Chef Pro",
      "description": "Suite de IA para restaurantes criativos e de autor: Culinária Criativa, Fermentus, Sonar Deep Research, escandallos avançados, fichas técnicas e storytelling profissional.",
      "keywords": "IA restaurante criativo, restaurante autor IA, software restaurante criativo, escandallos criativos, IA gastronómica autor, fermentação criativa IA, Fermentus, restaurante autor Espanha",
      "ogImage": "https://aichef.pro/og/use-cases/restaurante-creativo.jpg"
    },
    "personalizationTitle": "Personalizado à Sua Culinária Criativa desde o Minuto Um",
    "personalizationBody": "AI Chef Pro arranca com o agente «Quem Sou Eu?», um onboarding conversacional de 2 minutos em que lhe conta que tipo de culinária criativa lidera (autor, gastrobotânica, fermentos, vanguardia, fusão), cidade e referentes. A partir desse momento, cada agente —desde Culinária Criativa até Sonar Deep Research— responde adaptado à sua linguagem criativa, técnica habitual e posicionamento real no sector.",
    "appsTitle": "Os Agentes IA que Vai Usar no Seu Restaurante Criativo",
    "apps": [
      {
        "name": "Culinária Criativa",
        "category": "Criatividade Culinária",
        "description": "Desenvolvimento de pratos profissionais com receita + escandallo CSV pronto para o Kit de Escandallos Pro."
      },
      {
        "name": "Food Pairing AI",
        "category": "Criatividade Culinária",
        "description": "Combinações de ingredientes e maridajes com base científica."
      },
      {
        "name": "Fermentus Con AI+",
        "category": "Criatividade Culinária",
        "description": "P&D de vanguardia: fermentações, koji, kombucha, garum, miso."
      },
      {
        "name": "VegChef Plant-Based",
        "category": "Criatividade Culinária",
        "description": "Culinária plant-based, vegana e vegetariana avançada para autor."
      },
      {
        "name": "Pastelaria Criativa",
        "category": "Criatividade Culinária",
        "description": "Sobremesas de autor com técnica de pastelaria profissional."
      },
      {
        "name": "Chef Executivo Pro",
        "category": "Gastro Profile Pro",
        "description": "Estandarização de fichas técnicas e manuais de culinária."
      },
      {
        "name": "Sonar Deep Research",
        "category": "Modelos IA + LLM",
        "description": "Investigação profunda: tendências, produtores, vanguardia mundial."
      },
      {
        "name": "Sosa Ingredients",
        "category": "Fornecedores Gastro",
        "description": "Assistente do catálogo Sosa para texturas e técnicas avançadas."
      },
      {
        "name": "tSpoonLab Agent",
        "category": "Fornecedores Gastro",
        "description": "Assistente do catálogo tSpoonLab para aplicações técnicas."
      },
      {
        "name": "Léxico Gastronómico",
        "category": "Gastro Conhecimento",
        "description": "Tutor com definições de técnicas, processos e ciência gastronómica."
      },
      {
        "name": "GastroIMG Gen+",
        "category": "Gastro Conhecimento",
        "description": "Fotografia gastronómica de alto nível para prensa e web."
      },
      {
        "name": "BlogPost SEO Gen+",
        "category": "Contenidos e RRSS",
        "description": "Posts de blog com storytelling para captar tráfico orgánico."
      }
    ],
    "metrics": [
      {
        "value": "×7",
        "label": "velocidade encerramento carta nova"
      },
      {
        "value": "14",
        "label": "pratos em menu degustação"
      },
      {
        "value": "+5 pp",
        "label": "margen após escandallo real"
      },
      {
        "value": "13+",
        "label": "agentes para culinária autor"
      }
    ],
    "beforeAfter": {
      "beforeTitle": "Sem AI Chef Pro",
      "beforeItems": [
        "Encerramento de carta nova: 15-30 dias entre P&D, escandallos, fichas e storytelling",
        "P&D improvisado sem documentação, técnicas que se esquecen",
        "Storytelling para prensa redactado a contrarreloj cada mudança",
        "Fichas técnicas em caderno inaccesibles durante o servicio",
        "Investigação de tendências por intuição sem acesso a fontes"
      ],
      "afterTitle": "Com AI Chef Pro",
      "afterItems": [
        "Encerramento de carta nova: 1-3 dias com Culinária Criativa, Fermentus e Kit de Escandallos Pro",
        "P&D documentado com fichas iterativas, técnicas traçadas e replicables",
        "Storytelling profissional generado em horas com BlogPost SEO Gen+",
        "Fichas técnicas centralizadas acessibles desde o telemóvil durante o passe",
        "Sonar Deep Research aporta tendências e referências profissionais"
      ]
    },
    "galleryTitle": "Como Funciona um Restaurante Criativo de Autor",
    "gallerySubtitle": "O que vai coordenar com AI Chef Pro: P&D, fermentos, plating de autor, prep de ingredientes especiais e sala intimista.",
    "galleryImages": [
      "/lovable-uploads/ai-gallery/use-case-creativo-hero.jpg",
      "/lovable-uploads/ai-gallery/use-case-creativo-ferment.jpg",
      "/lovable-uploads/ai-gallery/use-case-creativo-plating.jpg",
      "/lovable-uploads/ai-gallery/use-case-creativo-rd.jpg",
      "/lovable-uploads/ai-gallery/use-case-creativo-prep.jpg",
      "/lovable-uploads/ai-gallery/use-case-creativo-room.jpg"
    ]
  },
  "restaurante-gastronomico": {
    "h1": "IA para Restaurante Gastronómico (Michelin/Repsol)",
    "heroSubtitle": "Escandallos premium, menus de degustação longos, brigada alargada, APPCC rigoroso e comunicação com guias e imprensa com uma suite de agentes de IA pensados para alta gastronomia profissional.",
    "heroTagline": "Alta cozinha com sistema, vanguarda com direção",
    "badge": "Para restaurantes gastronómicos Michelin e Repsol",
    "painsTitle": "O Que um Restaurante Gastronómico Não Pode Deixar de Resolver",
    "pains": [
      "Margem exigente com produto premium cujo custo muda todas as semanas na lota e no mercado",
      "Brigada extensa e altamente coordenada com hierarquia estrita e rotação de junior chefs",
      "Menus de degustação longos (8-15 passes) com escandallo total, harmonização e narrativa coerente",
      "Comunicação com guias Michelin/Repsol/50Best e imprensa especializada como alavanca crítica",
      "I&D contínuo de vanguarda com técnicas avançadas e produto da época",
      "Reservas com meses de antecedência com cancelamentos difíceis de gerir e operação de sala impecável"
    ],
    "featuresTitle": "Como a AI Chef Pro Ajuda na Alta Gastronomia",
    "features": [
      {
        "icon": "ChefHat",
        "title": "Chef Executivo Pro",
        "description": "Padronização de fichas técnicas e manuais para uma brigada alargada com hierarquia estrita."
      },
      {
        "icon": "Sparkles",
        "title": "Culinária Criativa + Food Pairing AI",
        "description": "Brainstorming para pratos de menu de degustação com técnica e harmonização. A Culinária Criativa entrega receita + escandallo CSV."
      },
      {
        "icon": "Beaker",
        "title": "Fermentus Con AI+",
        "description": "I&D de vanguarda: koji, kombuchas, shoyus, garums, lactofermentos essenciais na alta gastronomia contemporânea."
      },
      {
        "icon": "Calculator",
        "title": "Escandallos premium",
        "description": "Kit de Escandallos Pro: carrega o CSV da Culinária Criativa com os seus preços reais para produto premium com margem ajustada por passe e por menu de degustação completo."
      },
      {
        "icon": "BookOpen",
        "title": "Sosa Ingredients + tSpoonLab Agent",
        "description": "Assistentes dos catálogos profissionais mais usados na alta cozinha para técnicas e aplicações avançadas."
      },
      {
        "icon": "Search",
        "title": "Sonar Deep Research",
        "description": "Investigação profunda de tendências mundiais, produtores artesanais, técnicas emergentes e referências da vanguarda internacional."
      },
      {
        "icon": "MessageSquare",
        "title": "BlogPost SEO Gen+ + Pro Prompts eBook",
        "description": "Comunicação profissional para guias Michelin/Repsol/50Best, dossiê de imprensa e storytelling de menu de degustação."
      },
      {
        "icon": "Image",
        "title": "GastroIMG Gen+",
        "description": "Fotografia gastronómica de IA de alto nível para site, imprensa especializada e dossiê de candidaturas a guias."
      },
      {
        "icon": "GraduationCap",
        "title": "Léxico Gastronómico",
        "description": "Tutor com definições técnicas, processos e ciência gastronómica para fichas premium e formação da brigada."
      }
    ],
    "workflowTitle": "Um Dia Real num Restaurante Gastronómico com AI Chef Pro",
    "workflow": [
      "08:30 · Sonar Deep Research — investiga tendências e produto da época em mercados europeus para inspiração da próxima alteração do menu de degustação.",
      "10:00 · Culinária Criativa + Food Pairing AI — desenvolve 14 passes para o novo menu de degustação com técnica avançada e escandallo CSV.",
      "12:00 · Fermentus Con AI+ — trabalha a base de um fermentado chave do menu: garum de peixe para 4 passes.",
      "14:00 · Sosa Ingredients + tSpoonLab Agent — seleciona ingredientes técnicos para texturas e aplicações premium.",
      "15:30 · Kit de Escandallos Pro — carrega os CSV com os seus preços de mercado e valida a margem do menu de degustação completo (28 €/pass de custo médio).",
      "17:00 · Pro Prompts eBook + BlogPost SEO Gen+ — redige storytelling para os 14 passes, dossiê para guias Michelin/Repsol e nota de imprensa.",
      "18:30 · GastroIMG Gen+ — gera fotografias de cada passe para o site do restaurante e dossiê de candidatura a guias.",
      "19:30 · Serviço noturno — brigada coordenada com fichas técnicas centralizadas, passes do menu de degustação com sequência validada e harmonização sincronizada com sommelier."
    ],
    "productsTitle": "Modelos, Kits e Guias Descarregáveis para Alta Gastronomia",
    "productIds": [
      "guia-restaurante-gastronomico",
      "kit-escandallos",
      "pro-prompts-ebook",
      "pack-appcc",
      "kit-gestion-personal",
      "kit-inventario"
    ],
    "testimonialQuote": "Ter escandallo, ficha técnica, fermentos documentados e comunicação com guias num único sistema organizou-nos o caos criativo de qualquer alta cozinha. A Guía Restaurante Gastronómico foi fundamental na abertura do segundo projeto: business plan profissional que sustenta a candidatura. Premiação recente com dados na mão.",
    "testimonialAuthor": "David Aramburu",
    "testimonialRole": "Chef executivo, restaurante gastronómico com reconhecimento Michelin/Repsol",
    "faqTitle": "Perguntas Frequentes de Restaurantes Gastronómicos",
    "faqs": [
      {
        "q": "Serve para restaurante com estrela Michelin ou aspirante?",
        "a": "Para ambos. Os modelos e os agentes estão pensados para alta exigência: padronização rigorosa, fichas técnicas premium, escandallo profissional e comunicação com guias."
      },
      {
        "q": "Há guia passo a passo para abrir um gastronómico?",
        "a": "Sim, a Guía Restaurante Gastronómico (85 €): 65 lugares, business plan modelo para candidatura, plano financeiro, plano de cozinha, brigada, sommelier, manuais operativos e comunicação com guias. 20+ entregáveis."
      },
      {
        "q": "Cobre menus de degustação longos de 14-18 passes?",
        "a": "Sim. O Kit de Escandallos Pro e o Kit de Tareas Restaurante Criativo têm modelos específicos para menus de degustação com passes, escandallo total, sequência e harmonização sincronizada com sommelier."
      },
      {
        "q": "Gera comunicação profissional para Michelin, Repsol e 50Best?",
        "a": "Sim. BlogPost SEO Gen+ + Pro Prompts eBook + GastroIMG Gen+ permitem redigir dossiê de candidatura, comunicação com inspetores, notas de imprensa e materiais para os gabinetes das guias."
      },
      {
        "q": "Funciona para fermentação de vanguarda?",
        "a": "O Fermentus Con AI+ é um dos agentes mais usados por chefs Michelin: cobre koji, kombucha, shoyu, miso, garum e lactofermentos com respaldo científico e aplicações reais em passes de alta gastronomia."
      },
      {
        "q": "Como se integra com fornecedores premium?",
        "a": "O Sosa Ingredients e o tSpoonLab Agent são assistentes específicos de catálogos profissionais muito usados na alta gastronomia. Ajudam a selecionar texturas, aditivos e aplicações técnicas com critério de cozinha criativa."
      }
    ],
    "ctaTitle": "Alta cozinha com sistema, vanguarda com direção.",
    "ctaSubtitle": "Comece com o onboarding de 2 minutos. Plano Membro por 10 € por mês com 10.000 créditos para usar todos os agentes.",
    "seo": {
      "title": "IA para Restaurante Gastronómico (Michelin/Repsol): Menu de Degustação, I&D e Comunicação | AI Chef Pro",
      "description": "Suite de IA para alta gastronomia: Culinária Criativa, Fermentus, Sonar Deep Research, escandallos premium, fichas técnicas, comunicação com guias Michelin e Repsol. Comece hoje.",
      "keywords": "IA restaurante gastronómico, software Michelin, restaurante alta cozinha IA, escandallos premium, IA Repsol Soles, IA 50Best, fermentação criativa, Fermentus, menu de degustação IA, gastronomia Espanha",
      "ogImage": "https://aichef.pro/og/use-cases/restaurante-gastronomico.jpg"
    },
    "personalizationTitle": "Personalizado ao Seu Restaurante Gastronómico desde o Primeiro Minuto",
    "personalizationBody": "A AI Chef Pro arranca com o agente «Quem Sou Eu?», um onboarding conversacional de 2 minutos em que lhe conta que tipo de cozinha lidera (Michelin, Repsol Soles, aspirante, alta cozinha contemporânea, fusão vanguardista), número de lugares, cidade e referências. A partir desse momento, cada agente — desde Culinária Criativa até Sonar Deep Research — responde adaptado à sua linguagem, técnica habitual e posicionamento real no setor.",
    "appsTitle": "Os Agentes de IA que Vai Usar no Seu Restaurante Gastronómico",
    "apps": [
      {
        "name": "Chef Executivo Pro",
        "category": "Gastro Profile Pro",
        "description": "Padronização de fichas técnicas e manuais para brigada alargada."
      },
      {
        "name": "Culinária Criativa",
        "category": "Criatividade Culinária",
        "description": "Desenvolvimento de passes do menu de degustação com receita + escandallo CSV."
      },
      {
        "name": "Food Pairing AI",
        "category": "Criatividade Culinária",
        "description": "Combinações de ingredientes e harmonizações com base científica."
      },
      {
        "name": "Fermentus Con AI+",
        "category": "Criatividade Culinária",
        "description": "I&D de vanguarda: koji, kombucha, shoyu, miso, garum, lactofermentos."
      },
      {
        "name": "VegChef Plant-Based",
        "category": "Criatividade Culinária",
        "description": "Cozinha vegetal de alta gama para opções plant-based do menu de degustação."
      },
      {
        "name": "Pastelaria Criativa + Chocolataria Criativa",
        "category": "Criatividade Culinária",
        "description": "Sobremesas de alta cozinha e petit fours de encerramento."
      },
      {
        "name": "Sonar Deep Research",
        "category": "Modelos IA + LLM",
        "description": "Investigação profunda de tendências e vanguarda mundial."
      },
      {
        "name": "Sosa Ingredients",
        "category": "Fornecedores Gastro",
        "description": "Assistente do catálogo Sosa para texturas e técnicas avançadas."
      },
      {
        "name": "tSpoonLab Agent",
        "category": "Fornecedores Gastro",
        "description": "Assistente do catálogo tSpoonLab para aplicações técnicas."
      },
      {
        "name": "Léxico Gastronómico",
        "category": "Gastro Conhecimento",
        "description": "Tutor com definições técnicas e científicas."
      },
      {
        "name": "GastroIMG Gen+",
        "category": "Gastro Conhecimento",
        "description": "Fotografia gastronómica de alto nível para imprensa e guias."
      },
      {
        "name": "BlogPost SEO Gen+",
        "category": "Conteúdos e Redes Sociais",
        "description": "Storytelling e comunicação profissional com guias e imprensa especializada."
      }
    ],
    "metrics": [
      {
        "value": "×7",
        "label": "velocidade de fecho de menu novo"
      },
      {
        "value": "14-18",
        "label": "passes em menu de degustação"
      },
      {
        "value": "+5 pp",
        "label": "margem após escandallo rigoroso"
      },
      {
        "value": "13+",
        "label": "agentes para alta gastronomia"
      }
    ],
    "beforeAfter": {
      "beforeTitle": "Sem AI Chef Pro",
      "beforeItems": [
        "Fecho de menu de degustação novo: 15-30 dias entre I&D, escandallos, fichas e comunicação com guias",
        "I&D de fermentos sem documentação, técnicas que não se replicam",
        "Storytelling para imprensa e guias contra o relógio a cada mudança",
        "Fichas técnicas no caderno do chef, inacessíveis durante o passe",
        "Investigação de tendências por intuição e revistas, sem acesso sistemático"
      ],
      "afterTitle": "Com AI Chef Pro",
      "afterItems": [
        "Fecho de menu de degustação: 1-3 dias com Culinária Criativa, Fermentus e Kit de Escandallos Pro",
        "I&D documentado com fichas iterativas, fermentações rastreadas e replicáveis pela brigada",
        "Storytelling profissional para Michelin/Repsol/50Best gerado em horas",
        "Fichas técnicas centralizadas, acessíveis a partir do telemóvel durante o passe",
        "Sonar Deep Research aporta tendências da vanguarda mundial no instante"
      ]
    },
    "galleryTitle": "Como Funciona um Restaurante Gastronómico de Alta Cozinha",
    "gallerySubtitle": "O que vai coordenar com AI Chef Pro: sala elegante, empratamento de menu de degustação, cozinha premium, sommelier e serviço impecável.",
    "galleryImages": [
      "/lovable-uploads/ai-gallery/use-case-gastronomico-hero.jpg",
      "/lovable-uploads/ai-gallery/use-case-gastronomico-tasting.jpg",
      "/lovable-uploads/ai-gallery/use-case-gastronomico-kitchen.jpg",
      "/lovable-uploads/ai-gallery/use-case-gastronomico-pase.jpg",
      "/lovable-uploads/ai-gallery/use-case-gastronomico-sommelier.jpg",
      "/lovable-uploads/ai-gallery/use-case-gastronomico-cellar.jpg"
    ]
  },
  "restaurante-mexicano": {
    "h1": "IA para Restaurante Mexicano",
    "heroSubtitle": "Desenvolve molhos com equilíbrio preciso, escandallo por taco e por menu com custo real, planeia produção de massa e nixtamalização, e captura branding profissional com uma suite de agentes de IA gastronómica especializados em cozinha mexicana autêntica.",
    "heroTagline": "Sabor mexicano com margem real e técnica autêntica",
    "badge": "Para restaurantes mexicanos e taquerias",
    "painsTitle": "O Que um Restaurante Mexicano Não Pode Deixar de Resolver",
    "pains": [
      "Molhos complexos com muitos chiles, torrefação e equilíbrio preciso (mole, salsa macha, adobos) que requerem consistência turno a turno",
      "Escandallar tacos, antojitos e pratos com muitas variantes de tortilla, recheio, molhos e guarnições mantendo food cost coerente",
      "Mermas em massa, tortillas, marinadas e proteínas com longa cozedura (carnitas, barbacoa, cochinita)",
      "Padronizar nixtamalização e técnica de massa para tortillas, sopes e huaraches com qualidade consistente",
      "Diferenciar-se em zona competitiva com menu autêntico, branding visual de antojitos e storytelling regional (Oaxaca, Yucatán, Puebla)",
      "Captar pedidos de eventos e catering mexicano (casamentos, festas patrias) com margem enquanto se gere o serviço diário"
    ],
    "featuresTitle": "Como o AI Chef Pro Ajuda num Restaurante Mexicano",
    "features": [
      {
        "icon": "UtensilsCrossed",
        "title": "Cozinha Mexicana",
        "description": "Agente especializado em cozinha mexicana autêntica: molhos, moles, marinadas, antojitos, técnica de massa e cozinha regional."
      },
      {
        "icon": "Sparkles",
        "title": "Culinária Criativa",
        "description": "Para pratos contemporâneos e de autor com base mexicana: tacos signature, fusões controladas, sobremesas mexicanas modernas."
      },
      {
        "icon": "Calculator",
        "title": "Escandallos por taco e por prato",
        "description": "Cozinha Mexicana entrega receita + escandallo CSV; Kit de Escandallos Pro gere-o com custo real por taco, food cost % e preço sugerido."
      },
      {
        "icon": "CheckSquare",
        "title": "Kit de Tareas Restaurante Casual",
        "description": "Modelos adaptáveis: preparação de massa, torrefação de chiles, marinadas, comal, mise por estação e encerramento."
      },
      {
        "icon": "ShieldCheck",
        "title": "Pack APPCC mexicano",
        "description": "Rastreabilidade de chiles, massa nixtamalizada, proteínas com longa cozedura e temperaturas críticas."
      },
      {
        "icon": "Calendar",
        "title": "Gastro Calendar",
        "description": "Planeamento com datas-chave: 5 de Maio, Dia de Muertos, Festas Patrias 16 de setembro, Dia da Candelária com tamales."
      },
      {
        "icon": "Image",
        "title": "GastroIMG Gen+ + InstaFlow AI Pro",
        "description": "Fotografia gastronómica IA de referência + Instagram com calendário editorial: o restaurante mexicano vive do impacto visual e storytelling."
      },
      {
        "icon": "BarChart3",
        "title": "Sosa Ingredients",
        "description": "Assistente do catálogo Sosa para texturas avançadas, espessantes, desidratados e técnica aplicada a cozinha mexicana."
      },
      {
        "icon": "BookOpen",
        "title": "Guía Restaurante Mexicano",
        "description": "Guia premium descarregável de 80 lugares com escandallos, fichas técnicas, plano financeiro e operativa específica de cozinha mexicana."
      }
    ],
    "workflowTitle": "Um Dia Real num Restaurante Mexicano com AI Chef Pro",
    "workflow": [
      "08:00 · Abertura — checklist Kit de Tareas: torrefação de chiles para salsa macha, preparação de massa nixtamalizada, marinada de cochinita pibil, mise de toppings frescos.",
      "10:00 · Cozinha Mexicana — desenvolves um novo taco signature de barbacoa com salsa de chile cascabel e abacate. Culinária Criativa entrega receita + escandallo CSV.",
      "11:00 · Kit de Escandallos Pro — carregas o CSV com os teus preços reais de chiles secos, carne, massa e abacate, validas margem por taco e food cost %.",
      "13:00 · Serviço meio-dia — a equipa replica com modelos de mise; o comal funciona a pleno rendimento.",
      "17:00 · Pausa entre serviços — Gastro Calendar planeia o menu especial de Dia de Muertos com pão de muerto e mole negro.",
      "19:00 · GastroIMG Gen+ + InstaFlow AI Pro — geres a imagem de referência do novo taco e os posts para Instagram.",
      "21:00 · Serviço jantar — picos coordenados com Refeição do Pessoal para staff antes do rush.",
      "00:00 · Encerramento — limpeza profunda, APPCC assinado, preparação de massa para amanhã."
    ],
    "productsTitle": "Modelos e Kits Recomendados para Restaurante Mexicano",
    "productIds": [
      "guia-restaurante-mexicano",
      "kit-escandallos",
      "pack-appcc",
      "kit-inventario",
      "kit-gestion-personal",
      "pro-prompts-ebook"
    ],
    "testimonialQuote": "Fizemos escandallo taco a taco e descobrimos que três signature estavam em perdas apesar de serem os mais vendidos. Redesenhámo-los com Cozinha Mexicana ajustando a marinada e o rendimento da carne, sem tocar no preço, e subimos a margem 5 pontos. O planeamento do Dia de Muertos com Gastro Calendar triplicou-nos a faturação dessa semana.",
    "testimonialAuthor": "María José Hernández",
    "testimonialRole": "Chef e proprietária, restaurante mexicano contemporâneo",
    "faqTitle": "Perguntas Frequentes de Restaurantes Mexicanos",
    "faqs": [
      {
        "q": "Serve para taqueria casual, restaurante mexicano contemporâneo ou cozinha regional?",
        "a": "Para os três. Cozinha Mexicana cobre desde taqueria tradicional até alta cozinha mexicana de autor, passando por cozinha regional (Oaxaca, Yucatán, Puebla, Michoacán) com técnica autêntica."
      },
      {
        "q": "Cobre nixtamalização e técnica de massa?",
        "a": "Sim. Cozinha Mexicana raciocina como cozinheiro mexicano profissional: nixtamalização com cal, equilíbrio de massa para tortilla, sope, huarache, gordita e tlacoyo. Não receitas de YouTube."
      },
      {
        "q": "Como me ajuda com a complexidade dos molhos mexicanos?",
        "a": "Cozinha Mexicana entrega molhos com equilíbrio técnico de chiles (torrefação, hidratação, equilíbrio picante-doce-ácido), moles complexos por camadas e marinadas profissionais. Mermas Genéricas adiciona o custo dos chiles secos ao escandallo final."
      },
      {
        "q": "Gera conteúdo visual para Instagram, Glovo e Uber Eats?",
        "a": "Sim. GastroIMG Gen+ gera imagens de referência profissionais para redes e delivery; melhor foto = mais cliques e melhor ranking. Lembra-te que a imagem IA é de referência visual: a foto definitiva fazes tu com o teu prato real empratado."
      },
      {
        "q": "Como me ajuda com as festividades mexicanas?",
        "a": "Gastro Calendar planeia as datas-chave (Dia de Muertos, Dia da Candelária com tamales, Festas Patrias, 5 de Maio) com menus especiais e calendário editorial."
      }
    ],
    "ctaTitle": "O teu restaurante mexicano com margem real e técnica autêntica.",
    "ctaSubtitle": "Começa com o onboarding de 2 minutos. Plano Membro por 10 € por mês com 10.000 créditos para usar todos os agentes.",
    "seo": {
      "title": "IA para Restaurante Mexicano: Molhos, Escandallos e Técnica Autêntica | AI Chef Pro",
      "description": "Suite de IA para restaurantes mexicanos: Cozinha Mexicana, escandallos por taco, planeamento de festividades, branding e APPCC. Começa hoje.",
      "keywords": "IA restaurante mexicano, software taqueria, escandallos taco, cozinha mexicana IA, nixtamalização, molhos mexicanos, Dia de Muertos restaurante",
      "ogImage": "https://aichef.pro/og/use-cases/restaurante-mexicano.jpg"
    },
    "personalizationTitle": "Personalizado para o Teu Restaurante Mexicano desde o Minuto Um",
    "personalizationBody": "O AI Chef Pro arranca com o agente «Quem Sou Eu?», um onboarding conversacional de 2 minutos em que lhe contas que tipo de mexicano operas (taqueria casual, restaurante mexicano contemporâneo, cozinha regional, cantina, taqueria gourmet, food truck mexicano), tamanho da equipa, cidade e especialidade. Cada agente —desde Cozinha Mexicana até Gastro Calendar— responde adaptado ao teu produto, mercado e operativa real.",
    "appsTitle": "Os Agentes IA que Vais Usar no Teu Restaurante Mexicano",
    "apps": [
      {
        "name": "Cozinha Mexicana",
        "category": "Receituários de Latam",
        "description": "Agente especializado em cozinha mexicana autêntica: molhos, moles, marinadas, antojitos, técnica regional."
      },
      {
        "name": "Culinária Criativa",
        "category": "Criatividade Culinária",
        "description": "Desenvolvimento de tacos signature e pratos contemporâneos com receita + escandallo CSV."
      },
      {
        "name": "Restaurantes Casuais AI+",
        "category": "Conceitos de Negócio",
        "description": "Aconselhamento operativo para restaurantes casuais e taquerias profissionais."
      },
      {
        "name": "Sosa Ingredients",
        "category": "Fornecedores Gastro",
        "description": "Catálogo Sosa para texturas, espessantes e técnica aplicada a cozinha mexicana de autor."
      },
      {
        "name": "Mermas Genéricas",
        "category": "Ferramentas e Utilitários",
        "description": "Mermas em massa, chiles, marinadas e proteínas com longa cozedura."
      },
      {
        "name": "ID Alergénios",
        "category": "Ferramentas e Utilitários",
        "description": "Identificação automática de alergénios por prato: glúten, laticínios, frutos secos, soja."
      },
      {
        "name": "GastroIMG Gen+",
        "category": "Gastro Conhecimento",
        "description": "Fotografia gastronómica IA de referência para Instagram, web, carta e delivery."
      },
      {
        "name": "InstaFlow AI Pro",
        "category": "Conteúdos e Redes Sociais",
        "description": "Instagram com calendário editorial profissional para taqueria de autor."
      },
      {
        "name": "MenuDish Local SEO",
        "category": "Conteúdos e Redes Sociais",
        "description": "Captar clientes locais que procuram \"tacos perto\" ou \"restaurante mexicano\" no Google e Maps."
      },
      {
        "name": "Gastro Calendar",
        "category": "Conteúdos e Redes Sociais",
        "description": "Dia de Muertos, Dia da Candelária, Festas Patrias, 5 de Maio."
      },
      {
        "name": "Gerador de Pins Pinterest",
        "category": "Conteúdos e Redes Sociais",
        "description": "Pinterest captura tráfego orgânico para tacos e antojitos com storytelling."
      },
      {
        "name": "Refeição do Pessoal",
        "category": "Gastro Profile Pro",
        "description": "Gerador de menus de staff/família transversal a todos os conceitos."
      }
    ],
    "metrics": [
      {
        "value": "+5 pp",
        "label": "margem após escandallar tacos"
      },
      {
        "value": "×3",
        "label": "faturação no Dia de Muertos"
      },
      {
        "value": "−20 %",
        "label": "mermas em massa e marinadas"
      },
      {
        "value": "12+",
        "label": "agentes para a tua cozinha mexicana"
      }
    ],
    "beforeAfter": {
      "beforeTitle": "Sem AI Chef Pro",
      "beforeItems": [
        "Molhos e moles improvisados, equilíbrio inconsistente turno a turno",
        "Escandallos sem food cost real, signature em perdas sem saber",
        "Mermas em massa, chiles e proteínas longas sem rastreabilidade",
        "Festividades reativas: chegas tarde ao Dia de Muertos sem menu especial",
        "Instagram improvisado e plataformas de delivery com fotos do telemóvel"
      ],
      "afterTitle": "Com AI Chef Pro",
      "afterItems": [
        "Molhos e moles com critério técnico, consistência turno a turno",
        "Escandallo profissional por taco e prato com food cost validado",
        "Mermas controladas com Mermas Genéricas e modelos específicos",
        "Festividades planeadas com 8 semanas de antecedência com Gastro Calendar",
        "GastroIMG Gen+ + InstaFlow + MenuDish Local SEO captam clientes locais"
      ]
    },
    "galleryTitle": "Como Funciona um Restaurante Mexicano",
    "gallerySubtitle": "O que vais coordenar com AI Chef Pro: molhos, tacos, comal, ingredientes e equipa. Imagens geradas com IA como referência visual do conceito.",
    "galleryImages": [
      "/lovable-uploads/ai-gallery/use-case-mexicano-hero.jpg",
      "/lovable-uploads/ai-gallery/use-case-mexicano-salsas.jpg",
      "/lovable-uploads/ai-gallery/use-case-mexicano-tacos.jpg",
      "/lovable-uploads/ai-gallery/use-case-mexicano-comal.jpg",
      "/lovable-uploads/ai-gallery/use-case-mexicano-ingredientes.jpg",
      "/lovable-uploads/ai-gallery/use-case-mexicano-team.jpg"
    ]
  },
  "restaurante-peruano": {
    "h1": "IA para Restaurante Peruano",
    "heroSubtitle": "Desenvolve cebiches, tiraditos e causas com equilíbrio técnico, ficha técnica por prato com custo real de peixe e pimenta, planeia a produção e capta branding profissional com uma suíte de agentes de IA gastronómica especializados em cozinha peruana autêntica.",
    "heroTagline": "Cozinha peruana com margem real e técnica autêntica",
    "badge": "Para restaurantes peruanos e cebicherias",
    "painsTitle": "O Que um Restaurante Peruano Não Pode Deixar de Resolver",
    "pains": [
      "Cebiches e tiraditos com peixe fresco diário e leite de tigre equilibrado em acidez, picante e sal turno a turno",
      "Fazer fichas técnicas de pratos com ingredientes peruanos importados (pimenta amarela, rocoto, panca, huacatay) cujo custo varia por estação",
      "Quebras em peixe fresco, mariscos, milho, batatas peruanas e limas com uso intensivo",
      "Padronizar a técnica de confeção de proteínas (anticucho, frango grelhado, pachamanca) e acompanhamentos (causa, batata à huancaína)",
      "Diferenciar-se em zona competitiva com menu autêntico (crioula, costeña, andina, amazónica), branding visual e storytelling regional",
      "Captar pedidos de delivery e eventos mantendo a qualidade do cebiche fora da sua janela ótima de consumo"
    ],
    "featuresTitle": "Como o AI Chef Pro Ajuda num Restaurante Peruano",
    "features": [
      {
        "icon": "UtensilsCrossed",
        "title": "Culinária Peruana",
        "description": "Agente especializado em cozinha peruana autêntica: cebiches, tiraditos, causas, anticuchos, pachamanca, técnica crioula, costeña, andina e amazónica."
      },
      {
        "icon": "Sparkles",
        "title": "Culinária Criativa",
        "description": "Para pratos contemporâneos e de autor com base peruana: causas signature, fusões controladas, sobremesas peruanas modernas."
      },
      {
        "icon": "Wine",
        "title": "Food Pairing AI",
        "description": "Harmonizações com pisco, vinhos chilenos e cerveja para a tua carta peruana com base científica."
      },
      {
        "icon": "Calculator",
        "title": "Fichas técnicas por prato",
        "description": "Culinária Peruana entrega receita + ficha técnica CSV; o Kit de Escandallos Pro gere-a com custo real por cebiche, custo de comida % e preço sugerido."
      },
      {
        "icon": "CheckSquare",
        "title": "Kit de Tareas Restaurante Casual",
        "description": "Modelos: preparação de leite de tigre, marinadas de anticucho, mise de mariscos, batata à huancaína, encerramento."
      },
      {
        "icon": "ShieldCheck",
        "title": "Pack APPCC peruano",
        "description": "Rastreabilidade de peixe fresco, mariscos, pimentas e temperaturas críticas em cebiche e tiradito."
      },
      {
        "icon": "Calendar",
        "title": "Gastro Calendar",
        "description": "Planeamento com datas-chave: Dia da Independência 28 de julho, Dia do Cebiche, Mistura, Dia do Pisco Sour."
      },
      {
        "icon": "Image",
        "title": "GastroIMG Gen+ + InstaFlow AI Pro",
        "description": "Fotografia de cebiches e tiraditos IA de referência + Instagram: o restaurante peruano vive do impacto visual da cor."
      },
      {
        "icon": "BookOpen",
        "title": "Guía Restaurante Peruano",
        "description": "Guia premium descarregável de 80 lugares com fichas técnicas, ficha técnica, plano financeiro e operação específica de cozinha peruana."
      }
    ],
    "workflowTitle": "Um Dia Real num Restaurante Peruano com AI Chef Pro",
    "workflow": [
      "08:00 · Abertura — checklist Kit de Tareas: receção de peixe fresco diário, preparação de leite de tigre base, marinada de anticucho, hidratação de pimentas secas.",
      "10:00 · Culinária Peruana — desenvolve um novo tiradito de peixe do dia com leite de tigre de rocoto e manga. Culinária Criativa entrega receita + ficha técnica CSV.",
      "11:00 · Kit de Escandallos Pro — carregas o CSV com os teus preços reais de peixe fresco, pimentas, milho e batatas, validas a margem por prato.",
      "12:00 · Food Pairing AI — validas a harmonização do novo tiradito com um pisco sour macerado em ervas.",
      "13:00 · Serviço de almoço — pico forte do cebicheiro, mise impecável.",
      "17:00 · Pausa entre serviços — Gastro Calendar planeia o menu de 28 de julho (Independência) com causa, anticuchos e pisco.",
      "19:00 · GastroIMG Gen+ + InstaFlow AI Pro — geras a imagem de referência do novo tiradito e os posts para Instagram.",
      "23:00 · Encerramento — limpeza profunda, APPCC assinado, descarte controlado de peixe do dia."
    ],
    "productsTitle": "Modelos e Kits Recomendados para Restaurante Peruano",
    "productIds": [
      "guia-restaurante-peruano",
      "kit-escandallos",
      "pack-appcc",
      "kit-inventario",
      "kit-gestion-personal",
      "pro-prompts-ebook"
    ],
    "testimonialQuote": "A Culinária Peruana mudou-nos a cozinha. O leite de tigre tem agora equilíbrio técnico documentado, os cebiches saem iguais em qualquer turno, e as fichas técnicas com peixe fresco ao preço do dia funcionam em tempo real. A preparação do menu especial de 28 de julho com o Gastro Calendar triplicou-nos o faturamento.",
    "testimonialAuthor": "Carlos Fernández",
    "testimonialRole": "Chef e proprietário, cebicheria peruana contemporânea",
    "faqTitle": "Perguntas Frequentes de Restaurantes Peruanos",
    "faqs": [
      {
        "q": "Serve para cebicheria casual, restaurante peruano contemporâneo ou cozinha regional?",
        "a": "Para os três. A Culinária Peruana cobre desde cebicheria tradicional até alta cozinha de autor, passando por cozinha regional (crioula, costeña, andina, amazónica) com técnica autêntica."
      },
      {
        "q": "Cobre técnica de cebiche e leite de tigre profissional?",
        "a": "Sim. A Culinária Peruana raciocina como cebicheiro profissional: equilíbrio de leite de tigre com acidez, picante e sal; janela ótima de marinada por espécie; integração de pimentas com técnica."
      },
      {
        "q": "Como me ajuda com o custo variável do peixe fresco?",
        "a": "O Kit de Escandallos Pro recalcula instantaneamente a margem real quando atualizas o preço do peixe do dia. As Mermas Genéricas adicionam o custo de quebras por processo. Assim o cebiche reflete sempre o custo atual."
      },
      {
        "q": "Gera conteúdo visual para Instagram, Glovo e Uber Eats?",
        "a": "Sim. O GastroIMG Gen+ gera imagens de referência profissionais do cebiche e tiradito para Instagram, web e delivery; melhor foto = mais cliques. Lembra-te que a imagem IA é de referência visual: a foto definitiva és tu que fazes com o teu cebiche empratado real."
      },
      {
        "q": "Como me ajuda com festividades peruanas e eventos?",
        "a": "O Gastro Calendar planeia as datas-chave (28 de julho Dia da Independência, Dia do Cebiche, Dia do Pisco Sour, Mistura) com menus especiais e calendário editorial."
      }
    ],
    "ctaTitle": "O teu restaurante peruano com margem real e técnica autêntica.",
    "ctaSubtitle": "Começa com o onboarding de 2 minutos. Plano Membro por 10 € por mês com 10.000 créditos para usar todos os agentes.",
    "seo": {
      "title": "IA para Restaurante Peruano: Cebiches, Fichas Técnicas e Técnica Autêntica | AI Chef Pro",
      "description": "Suíte de IA para restaurantes peruanos: Culinária Peruana, fichas técnicas por cebiche, planeamento de festividades, branding e APPCC. Começa hoje.",
      "keywords": "IA restaurante peruano, software cebicheria, fichas técnicas cebiche, cozinha peruana IA, leite de tigre, pimenta amarela, 28 de julho peruano",
      "ogImage": "https://aichef.pro/og/use-cases/restaurante-peruano.jpg"
    },
    "personalizationTitle": "Personalizado para o Teu Restaurante Peruano desde o Primeiro Minuto",
    "personalizationBody": "O AI Chef Pro arranca com o agente «Quem Sou Eu?», um onboarding conversacional de 2 minutos em que conta que tipo de peruano operas (cebicheria casual, restaurante peruano contemporâneo, cozinha regional, picantería andina, churrasqueira, restaurante de autor), tamanho da equipa, cidade e especialidade. Cada agente —desde Culinária Peruana até Gastro Calendar— responde adaptado ao teu produto, mercado e operação real.",
    "appsTitle": "Os Agentes de IA que Vais Usar no Teu Restaurante Peruano",
    "apps": [
      {
        "name": "Culinária Peruana",
        "category": "Receituários da América Latina",
        "description": "Agente especializado em cozinha peruana autêntica: cebiches, tiraditos, causas, anticuchos, pachamanca."
      },
      {
        "name": "Culinária Criativa",
        "category": "Criatividade Culinária",
        "description": "Desenvolvimento de tiraditos signature e pratos contemporâneos com receita + ficha técnica CSV."
      },
      {
        "name": "Food Pairing AI",
        "category": "Criatividade Culinária",
        "description": "Harmonizações com pisco, vinhos e cerveja para a tua carta peruana."
      },
      {
        "name": "Restaurantes Casuais AI+",
        "category": "Conceitos de Negócio",
        "description": "Aconselhamento operacional para cebicherias e restaurantes peruanos."
      },
      {
        "name": "Sosa Ingredients",
        "category": "Fornecedores Gastro",
        "description": "Catálogo Sosa para texturas e técnica aplicada à cozinha peruana de autor."
      },
      {
        "name": "Mermas Genéricas",
        "category": "Ferramentas e Utilitários",
        "description": "Quebras em peixe fresco, mariscos, pimentas e limas."
      },
      {
        "name": "ID Alergénios",
        "category": "Ferramentas e Utilitários",
        "description": "Identificação automática de alergénios: peixe, mariscos, glúten, laticínios."
      },
      {
        "name": "GastroIMG Gen+",
        "category": "Conhecimento Gastro",
        "description": "Fotografia gastronómica IA de referência para Instagram, web, carta e delivery."
      },
      {
        "name": "InstaFlow AI Pro",
        "category": "Conteúdos e Redes Sociais",
        "description": "Instagram com calendário editorial profissional para cebicheria de autor."
      },
      {
        "name": "MenuDish Local SEO",
        "category": "Conteúdos e Redes Sociais",
        "description": "Captar clientes locais que procuram \"cebicheria perto\" ou \"restaurante peruano\"."
      },
      {
        "name": "Gastro Calendar",
        "category": "Conteúdos e Redes Sociais",
        "description": "28 de julho, Dia do Cebiche, Mistura, Dia do Pisco Sour."
      },
      {
        "name": "Bar & Lounge AI+",
        "category": "Conceitos de Negócio",
        "description": "Para a bancada de pisco sour e coquetelaria peruana de autor."
      }
    ],
    "metrics": [
      {
        "value": "+6 pp",
        "label": "margem após fichas técnicas de cebiches"
      },
      {
        "value": "×3",
        "label": "faturamento em 28 de julho"
      },
      {
        "value": "−25 %",
        "label": "quebras em peixe fresco"
      },
      {
        "value": "12+",
        "label": "agentes para a tua cozinha peruana"
      }
    ],
    "beforeAfter": {
      "beforeTitle": "Sem AI Chef Pro",
      "beforeItems": [
        "Leite de tigre improvisado, equilíbrio inconsistente turno a turno",
        "Fichas técnicas sem atualizar ao preço diário do peixe fresco",
        "Quebras em peixe, pimentas e mariscos sem rastreabilidade real",
        "Festividades reativas: chegas tarde ao 28 de julho sem menu especial",
        "Instagram improvisado e plataformas de delivery com fotos do telemóvel"
      ],
      "afterTitle": "Com AI Chef Pro",
      "afterItems": [
        "Leite de tigre com equilíbrio técnico documentado, cebiches consistentes",
        "Ficha técnica em tempo real com preço do peixe do dia",
        "Quebras controladas com Mermas Genéricas e modelos específicos",
        "Festividades planeadas com 8 semanas de antecedência",
        "GastroIMG Gen+ + InstaFlow + MenuDish Local SEO captam clientes locais"
      ]
    },
    "galleryTitle": "Como Funciona um Restaurante Peruano",
    "gallerySubtitle": "O que vais coordenar com AI Chef Pro: cebiche, tiradito, anticucho, pimentas e equipa. Imagens geradas com IA como referência visual do conceito.",
    "galleryImages": [
      "/lovable-uploads/ai-gallery/use-case-peruano-hero.jpg",
      "/lovable-uploads/ai-gallery/use-case-peruano-ceviche.jpg",
      "/lovable-uploads/ai-gallery/use-case-peruano-tiradito.jpg",
      "/lovable-uploads/ai-gallery/use-case-peruano-anticucho.jpg",
      "/lovable-uploads/ai-gallery/use-case-peruano-ajies.jpg",
      "/lovable-uploads/ai-gallery/use-case-peruano-team.jpg"
    ]
  },
  "restaurante-japones": {
    "h1": "IA para Restaurante Japonês",
    "heroSubtitle": "Desenvolve sushi, ramen, robata e kaiseki com técnica autêntica, escandallo por peça com custo real de peixe, planeia produção de fermentos e captura branding minimalista com uma suite de agentes de IA gastronómica especializados em cozinha japonesa profissional.",
    "heroTagline": "Cozinha japonesa com margem real e técnica autêntica",
    "badge": "Para restaurantes japoneses, sushi bars e ramen-yas",
    "painsTitle": "O Que um Restaurante Japonês Não Pode Deixar de Resolver",
    "pains": [
      "Peixe fresco diário para sashimi e sushi com custo volátil e mermas estritas por processo de filetagem",
      "Padronizar shari (arroz de sushi), nigiri e maki em cada turno com equilíbrio técnico de vinagre, açúcar e sal",
      "Caldos longos (tonkotsu, dashi, shoyu, miso) que requerem horas de cozedura e planeamento noturno",
      "Fermentos profissionais (koji, miso, shoyu caseiro, tsukemono) que requerem tempo e rastreabilidade",
      "Diferenciar-se em zona competitiva com técnica autêntica vs. sushi industrial, branding minimalista e storytelling japonês",
      "Captar pedidos de delivery sem perder qualidade do sushi (janela ótima 1-2 horas) e eventos omakase com margem"
    ],
    "featuresTitle": "Como o AI Chef Pro Ajuda num Restaurante Japonês",
    "features": [
      {
        "icon": "Fish",
        "title": "Cozinha Japonesa",
        "description": "Agente especializado em cozinha japonesa autêntica: sushi, sashimi, ramen, robata, tempura, kaiseki, técnica de itamae e fermentação."
      },
      {
        "icon": "Beaker",
        "title": "Fermentus Con AI+",
        "description": "Para koji, miso, shoyu caseiro, amazake e fermentos avançados de cozinha japonesa."
      },
      {
        "icon": "Sparkles",
        "title": "Culinária Criativa",
        "description": "Para pratos contemporâneos e omakase com base japonesa: nigiri signature, fusões controladas."
      },
      {
        "icon": "Calculator",
        "title": "Custos por peça",
        "description": "Cozinha Japonesa entrega receita + custo de receita CSV; Kit de Escandallos Pro gere-o com custo real por nigiri, ramen e omakase."
      },
      {
        "icon": "CheckSquare",
        "title": "Kit de Tareas Restaurante Casual",
        "description": "Modelos: filetagem de peixe, preparação de shari, caldos longos noturnos, mise de robata, encerramento."
      },
      {
        "icon": "ShieldCheck",
        "title": "Pack APPCC japonês",
        "description": "Rastreabilidade de peixe para sushi, fermentos, temperaturas críticas e conservação."
      },
      {
        "icon": "Calendar",
        "title": "Gastro Calendar",
        "description": "Planeamento com datas-chave: Hanami (cerejeira), Ano Novo japonês, Hina Matsuri, Dia do Sushi."
      },
      {
        "icon": "Image",
        "title": "GastroIMG Gen+ + InstaFlow AI Pro",
        "description": "Fotografia minimalista IA de referência + Instagram: o restaurante japonês vive do impacto visual zen e limpo."
      },
      {
        "icon": "BookOpen",
        "title": "Guía Restaurante Japonés",
        "description": "Guia premium descarregável de 60 lugares com custos de receita, fichas técnicas, plano financeiro e operativa específica."
      }
    ],
    "workflowTitle": "Um Dia Real num Restaurante Japonês com AI Chef Pro",
    "workflow": [
      "07:00 · Abertura — checklist Kit de Tareas: receção de peixe fresco, filetagem de blocos de sashimi, controlo de caldo tonkotsu cozido toda a noite.",
      "09:00 · Cozinha Japonesa — desenvolve um novo nigiri signature de hamachi com yuzu kosho. Culinária Criativa entrega receita + escandallo CSV.",
      "10:00 · Kit de Escandallos Pro — carrega o CSV com os seus preços reais de peixe do dia e wasabi fresco, valida margem por nigiri e omakase.",
      "11:00 · Fermentus Con AI+ — revê o progresso do miso caseiro (mês 6 de 12) e o koji novo em câmara de fermentação.",
      "13:00 · Serviço meio-dia — sushi bar a pleno com itamae a trabalhar em frente ao cliente.",
      "17:00 · Pausa entre serviços — Gastro Calendar planeia o menu especial de Hanami com sakura mochi e bento de cerejeira.",
      "19:00 · GastroIMG Gen+ + InstaFlow AI Pro — gera a imagem de referência do novo nigiri e os posts minimalistas para Instagram.",
      "23:00 · Encerramento — limpeza profunda, APPCC assinado, preparação de tonkotsu para amanhã (12 horas de cozedura)."
    ],
    "productsTitle": "Modelos e Kits Recomendados para Restaurante Japonês",
    "productIds": [
      "guia-restaurante-japones",
      "kit-escandallos",
      "pack-appcc",
      "kit-inventario",
      "kit-gestion-personal",
      "pro-prompts-ebook"
    ],
    "testimonialQuote": "Cozinha Japonesa mudou a nossa operativa. O equilíbrio do shari é agora consistente, o tonkotsu sai igual todos os dias, e o omakase tem escandallo profissional com margem validada peça a peça. Fermentus ajudou-nos a montar o programa de miso caseiro que diferencia totalmente a nossa proposta.",
    "testimonialAuthor": "Hiroshi Tanaka",
    "testimonialRole": "Itamae e proprietário, restaurante japonês contemporâneo",
    "faqTitle": "Perguntas Frequentes de Restaurantes Japoneses",
    "faqs": [
      {
        "q": "Serve para sushi bar, ramen-ya, izakaya ou kaiseki?",
        "a": "Para todos. Cozinha Japonesa cobre desde sushi tradicional até alta cozinha kaiseki, passando por ramen-ya, robata e izakaya com técnica autêntica."
      },
      {
        "q": "Cobre técnica de itamae e fermentação japonesa?",
        "a": "Sim. Cozinha Japonesa raciocina como itamae profissional: técnica de filetagem, equilíbrio de shari, neta e combinações; Fermentus cobre koji, miso, shoyu caseiro e amazake com técnica profissional."
      },
      {
        "q": "Como me ajuda com o custo variável do peixe para sashimi?",
        "a": "Kit de Escandallos Pro recalcula instantaneamente a margem quando atualiza o preço do peixe do dia. Mermas Genéricas adiciona o custo de perdas por filetagem. O nigiri reflete sempre o custo atual."
      },
      {
        "q": "Gera conteúdo visual para Instagram, Glovo e Uber Eats?",
        "a": "Sim. GastroIMG Gen+ gera imagens de referência profissionais do sushi para Instagram, web e delivery; melhor foto = mais cliques. Lembre-se de que a imagem IA é de referência visual: a foto definitiva é feita por si com a sua peça empratada real."
      },
      {
        "q": "Como me ajuda com festividades japonesas?",
        "a": "Gastro Calendar planeia as datas-chave (Hanami com sakura, Ano Novo japonês com osechi ryori, Hina Matsuri, Dia do Sushi) com menus especiais e calendário editorial minimalista."
      }
    ],
    "ctaTitle": "O seu restaurante japonês com margem real e técnica autêntica.",
    "ctaSubtitle": "Começa com o onboarding de 2 minutos. Plano Membro por 10 € por mês com 10.000 créditos para usar todos os agentes.",
    "seo": {
      "title": "IA para Restaurante Japonês: Sushi, Cálculo de Custos e Técnica Itamae | AI Chef Pro",
      "description": "Suite de IA para restaurantes japoneses: Cozinha Japonesa, Fermentus para koji e miso, cálculo de custos por peça, planeamento de festividades. Comece hoje.",
      "keywords": "IA restaurante japonês, software sushi bar, cálculo de custos sushi, cozinha japonesa IA, koji miso shoyu, ramen tonkotsu, itamae profissional",
      "ogImage": "https://aichef.pro/og/use-cases/restaurante-japones.jpg"
    },
    "personalizationTitle": "Personalizado para o Seu Restaurante Japonês desde o Minuto Um",
    "personalizationBody": "AI Chef Pro arranca com o agente «Quem Sou Eu?», um onboarding conversacional de 2 minutos em que lhe conta que tipo de japonês opera (sushi bar, ramen-ya, izakaya, kaiseki, omakase, japonês contemporâneo de autor), tamanho da equipa, cidade e especialidade. Cada agente —desde Cozinha Japonesa até Gastro Calendar— responde adaptado ao seu produto, mercado e operativa real.",
    "appsTitle": "Os Agentes IA que Vai Usar no Seu Restaurante Japonês",
    "apps": [
      {
        "name": "Cozinha Japonesa",
        "category": "Receituários da Ásia",
        "description": "Agente especializado em cozinha japonesa autêntica: sushi, sashimi, ramen, robata, kaiseki."
      },
      {
        "name": "Fermentus Con AI+",
        "category": "Criatividade Culinária",
        "description": "Koji, miso, shoyu caseiro, amazake e fermentos avançados."
      },
      {
        "name": "Culinária Criativa",
        "category": "Criatividade Culinária",
        "description": "Desenvolvimento de nigiri signature e omakase com receita + ficha técnica CSV."
      },
      {
        "name": "Food Pairing AI",
        "category": "Criatividade Culinária",
        "description": "Maridagens com sake, whisky japonês, cerveja e vinhos para a sua carta."
      },
      {
        "name": "Sosa Ingredients",
        "category": "Fornecedores Gastro",
        "description": "Catálogo Sosa para texturas e técnica aplicada à cozinha japonesa de autor."
      },
      {
        "name": "Mermas Genéricas",
        "category": "Ferramentas e Utilitários",
        "description": "Mermas em filetagem de peixe, sashimi e caldos longos."
      },
      {
        "name": "ID Alergénios",
        "category": "Ferramentas e Utilitários",
        "description": "Identificação automática de alergénios: peixe, mariscos, soja, glúten, sésamo."
      },
      {
        "name": "GastroIMG Gen+",
        "category": "Conhecimento Gastro",
        "description": "Fotografia minimalista IA de referência para Instagram, web, carta e delivery."
      },
      {
        "name": "InstaFlow AI Pro",
        "category": "Conteúdos e Redes Sociais",
        "description": "Instagram com calendário editorial minimalista para sushi bar de autor."
      },
      {
        "name": "MenuDish Local SEO",
        "category": "Conteúdos e Redes Sociais",
        "description": "Atrair clientes locais que procuram \"sushi perto\" ou \"ramen perto\"."
      },
      {
        "name": "Gastro Calendar",
        "category": "Conteúdos e Redes Sociais",
        "description": "Hanami, Ano Novo japonês, Hina Matsuri, Dia do Sushi."
      },
      {
        "name": "Bar & Lounge AI+",
        "category": "Conceitos de Negócio",
        "description": "Para o balcão de sake, whisky japonês e coquetelaria com base japonesa."
      }
    ],
    "metrics": [
      {
        "value": "+6 pp",
        "label": "margem após calcular custos do omakase"
      },
      {
        "value": "×3",
        "label": "engagement no Instagram com GastroIMG"
      },
      {
        "value": "−20 %",
        "label": "perdas no corte de peixe"
      },
      {
        "value": "12+",
        "label": "agentes para a sua cozinha japonesa"
      }
    ],
    "beforeAfter": {
      "beforeTitle": "Sem AI Chef Pro",
      "beforeItems": [
        "Shari e técnica improvisados, equilíbrio inconsistente entre itamae",
        "Custos não atualizados ao preço diário do peixe",
        "Caldos longos (tonkotsu) sem rastreabilidade nem planeamento rigoroso",
        "Fermentos caseiros (miso, shoyu) sem programa documentado",
        "Instagram improvisado e plataformas de entrega com fotos do telemóvel"
      ],
      "afterTitle": "Com AI Chef Pro",
      "afterItems": [
        "Shari, neta e técnica com critério profissional, consistência turno a turno",
        "Cálculo de custos em tempo real com preço do peixe do dia",
        "Caldos longos planeados com modelos específicos e HACCP assinado",
        "Programa de fermentos com Fermentus Con AI+ documentado profissionalmente",
        "GastroIMG Gen+ + InstaFlow + MenuDish SEO local captam clientes locais"
      ]
    },
    "galleryTitle": "Como Funciona um Restaurante Japonês",
    "gallerySubtitle": "O que vai coordenar com AI Chef Pro: sushi, ramen, robata, ingredientes e equipa. Imagens geradas com IA como referência visual do conceito.",
    "galleryImages": [
      "/lovable-uploads/ai-gallery/use-case-japones-hero.jpg",
      "/lovable-uploads/ai-gallery/use-case-japones-sushi.jpg",
      "/lovable-uploads/ai-gallery/use-case-japones-ramen.jpg",
      "/lovable-uploads/ai-gallery/use-case-japones-robata.jpg",
      "/lovable-uploads/ai-gallery/use-case-japones-ingredientes.jpg",
      "/lovable-uploads/ai-gallery/use-case-japones-team.jpg"
    ]
  },
  "restaurante-nikkei": {
    "h1": "IA para Restaurante Nikkei",
    "heroSubtitle": "Desenvolva tiraditos nikkei, sushi de fusão e robata com técnica autêntica peruano-japonesa, escandallo por prato com custo real e capture branding profissional com uma suite de agentes de IA gastronómica especializados em cozinha nikkei.",
    "heroTagline": "Cozinha Nikkei com margem real e técnica autêntica",
    "badge": "Para restaurantes Nikkei e fusão peruano-japonesa",
    "painsTitle": "O Que um Restaurante Nikkei Não Pode Deixar de Resolver",
    "pains": [
      "Combinações complexas peruano-japonesas com equilíbrio preciso de ají amarelo, yuzu, miso, ponzu e shoyu",
      "Peixe fresco diário para tiraditos e sushi com custo volátil, filetagem rigorosa e técnica itamae aplicada à cozinha peruana",
      "Padronizar tiraditos signature, sushi nikkei e anticuchos com marinada miso-ají panca turno a turno",
      "Escandallar pratos com ingredientes importados (ají amarelo, ají panca, yuzu, dashi) cujo custo varia por temporada",
      "Diferenciar-se do japonês tradicional ou peruano puro com storytelling de fusão autêntica e branding visual de autor",
      "Captar pedidos de omakase nikkei e eventos mantendo a qualidade do produto cru"
    ],
    "featuresTitle": "Como o AI Chef Pro Ajuda num Restaurante Nikkei",
    "features": [
      {
        "icon": "Sparkles",
        "title": "Cozinha Japonesa + Culinária Peruana",
        "description": "Combinação de agentes especializados em ambas as culturas: técnica itamae aplicada a tiraditos peruanos, ají amarelo em nigiri, anticuchos miso."
      },
      {
        "icon": "Beaker",
        "title": "Fermentus Con AI+",
        "description": "Para koji, miso, shoyu caseiro adaptados à fusão nikkei com ají panca e huacatay."
      },
      {
        "icon": "Wine",
        "title": "Food Pairing AI",
        "description": "Maridagens com sake, pisco, vinhos chilenos e cerveja japonesa para a sua carta nikkei."
      },
      {
        "icon": "Calculator",
        "title": "Escandallos por prato",
        "description": "Culinária Criativa entrega receita + escandallo CSV; Kit de Escandallos Pro gere-o com custo real por tiradito e omakase nikkei."
      },
      {
        "icon": "CheckSquare",
        "title": "Kit de Tareas Restaurante Casual",
        "description": "Modelos: filetagem de peixe, preparação de leite de tigre com yuzu, marinada nikkei, mise de robata, encerramento."
      },
      {
        "icon": "ShieldCheck",
        "title": "Pack APPCC nikkei",
        "description": "Rastreabilidade de peixe, fermentos, ajíes e temperaturas críticas em produto cru."
      },
      {
        "icon": "Calendar",
        "title": "Gastro Calendar",
        "description": "Planeamento cruzado: festividades japonesas e peruanas, eventos de fusão, omakase nikkei sazonal."
      },
      {
        "icon": "Image",
        "title": "GastroIMG Gen+ + InstaFlow AI Pro",
        "description": "Fotografia editorial IA de referência + Instagram: o nikkei vive do impacto visual da cor e da composição."
      },
      {
        "icon": "BookOpen",
        "title": "Guía Restaurante Nikkei",
        "description": "Guia premium descarregável de 60 lugares com escandallos, fichas técnicas, plano financeiro e operativa específica nikkei."
      }
    ],
    "workflowTitle": "Um Dia Real num Restaurante Nikkei com AI Chef Pro",
    "workflow": [
      "07:00 · Abertura — checklist Kit de Tareas: receção de peixe fresco, filetagem para tiraditos e nigiri, preparação de leite de tigre com yuzu, marinada de anticuchos miso-panca.",
      "09:00 · Cozinha Japonesa + Culinária Peruana — desenvolve um novo tiradito de hamachi com leite de tigre de yuzu e ají amarelo. Culinária Criativa entrega receita + escandallo CSV.",
      "10:00 · Kit de Escandallos Pro — carrega o CSV com os seus preços reais de peixe do dia, ají amarelo e yuzu, valida margem por tiradito e omakase nikkei.",
      "11:00 · Fermentus Con AI+ — revê o progresso do miso caseiro com ají panca (mês 4 de 8).",
      "12:00 · Food Pairing AI — valida a maridagem do novo tiradito com um sake junmai e um pisco macerado em folhas de shiso.",
      "13:00 · Serviço meio-dia — robata a pleno com anticuchos miso, sushi bar a trabalhar tiraditos signature.",
      "19:00 · GastroIMG Gen+ + InstaFlow AI Pro — gera a imagem de referência do novo tiradito nikkei e os posts editoriais para Instagram.",
      "23:00 · Encerramento — limpeza profunda, APPCC assinado, descarte controlado, preparação de amanhã."
    ],
    "productsTitle": "Modelos e Kits Recomendados para Restaurante Nikkei",
    "productIds": [
      "guia-restaurante-nikkei",
      "kit-escandallos",
      "pack-appcc",
      "kit-inventario",
      "kit-gestion-personal",
      "pro-prompts-ebook"
    ],
    "testimonialQuote": "Cozinha Japonesa + Culinária Peruana cruzando agentes mudou a nossa proposta. Os tiraditos têm agora equilíbrio técnico documentado, o omakase nikkei sai com escandallo validado peça a peça, e o programa de miso caseiro com ají panca da Fermentus diferencia-nos totalmente. Subimos a margem 7 pontos.",
    "testimonialAuthor": "Yui Sato",
    "testimonialRole": "Chef e proprietária, restaurante nikkei de autor",
    "faqTitle": "Perguntas Frequentes de Restaurantes Nikkei",
    "faqs": [
      {
        "q": "Serve para nikkei contemporâneo, sushi bar nikkei ou cevicheria com técnica japonesa?",
        "a": "Para os três. Cozinha Japonesa + Culinária Peruana complementam-se para cobrir desde sushi nikkei até tiraditos com leite de tigre fusionado com yuzu ou ponzu."
      },
      {
        "q": "Como me ajuda com o equilíbrio entre técnicas peruana e japonesa?",
        "a": "Culinária Criativa orquestra os dois agentes: raciocina em chave de fusão autêntica (não fusão confusa), respeitando técnica itamae para produto cru e equilíbrio peruano para leite de tigre e marinadas."
      },
      {
        "q": "Como gero o custo variável do peixe e dos ingredientes peruanos importados?",
        "a": "Kit de Escandallos Pro recalcula instantaneamente a margem quando atualiza preços do peixe do dia e de ajíes/yuzu. Mermas Genéricas adiciona o custo de mermas por processo."
      },
      {
        "q": "Gera conteúdo visual para Instagram e delivery?",
        "a": "Sim. GastroIMG Gen+ gera imagens de referência profissionais do tiradito nikkei para Instagram, web e delivery. Lembre-se de que a imagem IA é de referência visual: a foto definitiva é feita por si com o seu prato empratado real."
      },
      {
        "q": "Como me ajuda com festividades cruzadas peruano-japonesas?",
        "a": "Gastro Calendar planeia as datas-chave de ambas as culturas (28 de julho peruano, Hanami japonês, Dia do Cebiche, Ano Novo japonês) com omakase nikkei sazonal e storytelling de fusão."
      }
    ],
    "ctaTitle": "O seu restaurante nikkei com margem real e técnica autêntica.",
    "ctaSubtitle": "Comece com o onboarding de 2 minutos. Plano Membro por 10 € por mês com 10.000 créditos para usar todos os agentes.",
    "seo": {
      "title": "IA para Restaurante Nikkei: Tiraditos, Escandallos e Técnica de Fusão | AI Chef Pro",
      "description": "Suite de IA para restaurantes nikkei: Cozinha Japonesa + Culinária Peruana, escandallos por tiradito, omakase nikkei, branding e APPCC. Comece hoje.",
      "keywords": "IA restaurante nikkei, software nikkei, escandallos tiradito nikkei, cozinha nikkei IA, ají amarelo yuzu, sushi nikkei, fusão peruano japonesa",
      "ogImage": "https://aichef.pro/og/use-cases/restaurante-nikkei.jpg"
    },
    "personalizationTitle": "Personalizado para o Seu Restaurante Nikkei desde o Minuto Um",
    "personalizationBody": "AI Chef Pro arranca com o agente «Quem Sou Eu?», um onboarding conversacional de 2 minutos no qual lhe conta que tipo de nikkei opera (nikkei contemporâneo de autor, sushi bar nikkei, cevicheria com técnica japonesa, omakase nikkei), tamanho da equipa, cidade e especialidade. Cada agente responde adaptado ao seu produto, mercado e operativa real.",
    "appsTitle": "Os Agentes IA que Vai Usar no Seu Restaurante Nikkei",
    "apps": [
      {
        "name": "Cozinha Japonesa",
        "category": "Receituários da Ásia",
        "description": "Técnica itamae, filetagem, sushi, sashimi e robata aplicados à fusão nikkei."
      },
      {
        "name": "Culinária Peruana",
        "category": "Receituários da América Latina",
        "description": "Cebiches, tiraditos, anticuchos e técnica peruana aplicados à fusão nikkei."
      },
      {
        "name": "Culinária Criativa",
        "category": "Criatividade Culinária",
        "description": "Orquestrador de fusão: tiraditos signature, sushi nikkei, omakase com base autêntica."
      },
      {
        "name": "Fermentus Con AI+",
        "category": "Criatividade Culinária",
        "description": "Koji, miso caseiro com ají panca, shoyu e fermentos cruzados."
      },
      {
        "name": "Food Pairing AI",
        "category": "Criatividade Culinária",
        "description": "Maridagens com sake, pisco, vinhos chilenos e cerveja japonesa."
      },
      {
        "name": "Sosa Ingredients",
        "category": "Fornecedores Gastro",
        "description": "Catálogo Sosa para texturas e técnica aplicada à cozinha nikkei de autor."
      },
      {
        "name": "Mermas Genéricas",
        "category": "Ferramentas e Utilitários",
        "description": "Mermas em filetagem de peixe, ajíes e marinadas longas."
      },
      {
        "name": "ID Alergénios",
        "category": "Ferramentas e Utilitários",
        "description": "Identificação automática de alergénios: peixe, mariscos, soja, glúten, sésamo, frutos secos."
      },
      {
        "name": "GastroIMG Gen+",
        "category": "Conhecimento Gastro",
        "description": "Fotografia editorial IA de referência para Instagram, web, carta e delivery."
      },
      {
        "name": "InstaFlow AI Pro",
        "category": "Conteúdos e Redes Sociais",
        "description": "Instagram com calendário editorial profissional para nikkei de autor."
      },
      {
        "name": "MenuDish Local SEO",
        "category": "Conteúdos e Redes Sociais",
        "description": "Captar clientes locais que procuram \"nikkei perto\" no Google e Maps."
      },
      {
        "name": "Gastro Calendar",
        "category": "Conteúdos e Redes Sociais",
        "description": "Festividades cruzadas: Hanami, 28 de julho, Dia do Cebiche, Ano Novo japonês."
      }
    ],
    "metrics": [
      {
        "value": "+7 pp",
        "label": "margem após escandallar omakase nikkei"
      },
      {
        "value": "×3",
        "label": "engagement Instagram com GastroIMG"
      },
      {
        "value": "−25 %",
        "label": "mermas em peixe e ajíes"
      },
      {
        "value": "12+",
        "label": "agentes para a sua cozinha nikkei"
      }
    ],
    "beforeAfter": {
      "beforeTitle": "Sem AI Chef Pro",
      "beforeItems": [
        "Fusão improvisada sem equilíbrio técnico entre culturas",
        "Escandallos sem atualizar ao preço do peixe e dos ajíes",
        "Sushi nikkei e tiraditos com consistência variável entre turnos",
        "Programa de fermentos caseiro sem documentação profissional",
        "Instagram improvisado, sem storytelling de fusão autêntica"
      ],
      "afterTitle": "Com AI Chef Pro",
      "afterItems": [
        "Fusão autêntica com técnica documentada de ambas as culturas",
        "Escandallo em tempo real com preços atualizados",
        "Sushi nikkei e tiraditos com equilíbrio técnico consistente",
        "Programa Fermentus com miso ají panca documentado profissionalmente",
        "GastroIMG Gen+ + InstaFlow + storytelling de fusão nikkei autêntica"
      ]
    },
    "galleryTitle": "Como Funciona um Restaurante Nikkei",
    "gallerySubtitle": "O que vai coordenar com AI Chef Pro: tiraditos, sushi nikkei, anticuchos miso, ingredientes e equipamento. Imagens geradas com IA como referência visual do conceito.",
    "galleryImages": [
      "/lovable-uploads/ai-gallery/use-case-nikkei-hero.jpg",
      "/lovable-uploads/ai-gallery/use-case-nikkei-tiradito.jpg",
      "/lovable-uploads/ai-gallery/use-case-nikkei-sushi.jpg",
      "/lovable-uploads/ai-gallery/use-case-nikkei-anticucho.jpg",
      "/lovable-uploads/ai-gallery/use-case-nikkei-ingredientes.jpg",
      "/lovable-uploads/ai-gallery/use-case-nikkei-team.jpg"
    ]
  },
  "restaurante-plant-based": {
    "h1": "IA para Restaurante Plant-Based e Vegano",
    "heroSubtitle": "Desenvolva menus plant-based com equilíbrio nutricional, custeio por bowl e burger vegana com custo real, planeie fermentos vegetais e capture branding fresco com uma suite de agentes de IA gastronómica especializados em cozinha plant-based profissional.",
    "heroTagline": "Cozinha vegetal com margem real e técnica avançada",
    "badge": "Para restaurantes plant-based, veganos e saudáveis",
    "painsTitle": "O Que um Restaurante Plant-Based Não Pode Deixar de Resolver",
    "pains": [
      "Conseguir umami profundo em cozinha 100% vegetal com fermentos, fumados, koji e técnica avançada (sem atalhos industriais)",
      "Custear bowls, burgers veganas e pratos plant-based com muitas variantes de toppings e proteínas vegetais",
      "Quebras elevadas em produto fresco (legumes da época, frutas, ervas, microgreens) com prazo de validade curto",
      "Padronizar proteínas vegetais caseiras (seitan, tempeh, tofu marinado, mock meats) e coberturas/molhos plant-based",
      "Diferenciar-se em zona concorrida com menu de autor plant-based, branding visual fresco e storytelling sustentável",
      "Captar pedidos de delivery com produtos frescos mantendo apresentação e qualidade do bowl"
    ],
    "featuresTitle": "Como o AI Chef Pro Ajuda num Restaurante Plant-Based",
    "features": [
      {
        "icon": "Sprout",
        "title": "VegChef Plant-Based",
        "description": "Agente especializado em cozinha plant-based, vegana e vegetariana profissional: bowls, burgers, proteínas vegetais, técnica avançada."
      },
      {
        "icon": "Beaker",
        "title": "Fermentus Con AI+",
        "description": "Para koji vegetal, miso caseiro, shoyu, kimchi, kombucha, lactofermentos e umami profundo sem produtos animais."
      },
      {
        "icon": "Sparkles",
        "title": "Culinária Criativa",
        "description": "Para pratos plant-based contemporâneos e de autor com base vegetal: bowls signature, sobremesas veganas, fusões."
      },
      {
        "icon": "Wine",
        "title": "Food Pairing AI",
        "description": "Maridagens com vinhos veganos, kombucha e bebidas funcionais para a sua carta plant-based."
      },
      {
        "icon": "Calculator",
        "title": "Custeio por bowl e burger",
        "description": "VegChef entrega receita + custeio CSV; Kit de Escandallos Pro gere-o com custo real por bowl, food cost % e preço sugerido."
      },
      {
        "icon": "CheckSquare",
        "title": "Kit de Tareas Restaurante Casual",
        "description": "Modelos: preparação de proteínas vegetais, fermentos, mise de toppings frescos, marinadas, encerramento."
      },
      {
        "icon": "ShieldCheck",
        "title": "Pack APPCC plant-based",
        "description": "Rastreabilidade de fermentos, proteínas vegetais caseiras, ervas frescas e temperaturas críticas."
      },
      {
        "icon": "Calendar",
        "title": "Gastro Calendar",
        "description": "Planeamento com datas-chave: Veganuary (janeiro), Dia Mundial Vegano, Earth Day, épocas de legumes locais."
      },
      {
        "icon": "Image",
        "title": "GastroIMG Gen+ + InstaFlow AI Pro",
        "description": "Fotografia vibrante IA de referência + Instagram: o plant-based vive do impacto visual da cor."
      }
    ],
    "workflowTitle": "Um Dia Real num Restaurante Plant-Based com AI Chef Pro",
    "workflow": [
      "07:00 · Abertura — checklist Kit de Tareas: revisão de fermentos em câmara, preparação de proteínas vegetais (seitan, tempeh), marinadas de tofu, mise de microgreens e flores comestíveis.",
      "09:00 · VegChef Plant-Based — desenvolve um novo bowl signature de quinoa, kale, tempeh marinado, kimchi caseiro e tahini de curcuma. Culinária Criativa entrega receita + custeio CSV.",
      "10:00 · Kit de Escandallos Pro — carrega o CSV com os seus preços reais de quinoa, kale, tempeh e tahini, valida margem por bowl e food cost %.",
      "11:00 · Fermentus Con AI+ — revê o progresso do miso caseiro (mês 6 de 12), o koji vegetal e o kimchi novo em câmara de fermentação.",
      "12:00 · Food Pairing AI — valida a maridagem do novo bowl com kombucha de gengibre e um vinho branco vegano.",
      "13:00 · Serviço de meio-dia — bowls a cheio, burgers veganas na chapa, mise de toppings frescos.",
      "19:00 · GastroIMG Gen+ + InstaFlow AI Pro — gera a imagem de referência do novo bowl e os posts vibrantes para Instagram.",
      "22:00 · Encerramento — limpeza profunda, APPCC assinado, preparação de fermentos para fermentação noturna."
    ],
    "productsTitle": "Modelos e Kits Recomendados para Restaurante Plant-Based",
    "productIds": [
      "kit-tareas",
      "kit-escandallos",
      "pack-appcc",
      "kit-inventario",
      "kit-gestion-personal",
      "pro-prompts-ebook"
    ],
    "testimonialQuote": "VegChef + Fermentus mudaram a nossa proposta. Conseguimos umami profundo sem atalhos industriais graças ao miso caseiro e ao koji vegetal, e os custeios por bowl com tempeh marinado confirmam-nos que o plant-based pode ter margem alta. Subimos 6 pontos e a captação pelo Instagram com GastroIMG é x3.",
    "testimonialAuthor": "Lucía Ferrer",
    "testimonialRole": "Chef e proprietária, restaurante plant-based de autor",
    "faqTitle": "Perguntas Frequentes de Restaurantes Plant-Based",
    "faqs": [
      {
        "q": "Serve para casual healthy bowls, vegan fine dining ou cozinha plant-based de autor?",
        "a": "Para os três. VegChef cobre desde bowls casuais até alta cozinha vegana, passando por hamburguerias plant-based, cozinha com técnica avançada e sobremesas veganas profissionais."
      },
      {
        "q": "Como conseguir umami profundo em cozinha 100% vegetal?",
        "a": "Fermentus Con AI+ cobre koji vegetal, miso caseiro, shoyu, kimchi, kombucha e lactofermentos com técnica profissional. VegChef integra fumados controlados, desidratados, crostas de cogumelos e caldos longos vegetais."
      },
      {
        "q": "Cobre proteínas vegetais caseiras (seitan, tempeh, tofu marinado)?",
        "a": "Sim. VegChef raciocina como chef plant-based profissional: técnicas de seitan amassado, tempeh fermentado, tofu marinado e prensado, mock meats com técnica de textura."
      },
      {
        "q": "Gera conteúdo visual para Instagram, Glovo e Uber Eats?",
        "a": "Sim. GastroIMG Gen+ gera imagens vibrantes de referência dos bowls para Instagram, web e delivery; o plant-based vive da cor. Lembre-se de que a imagem IA é de referência visual: a foto definitiva é feita por si com o seu bowl empratado real."
      },
      {
        "q": "Como me ajuda com o Veganuary e eventos plant-based?",
        "a": "Gastro Calendar planeia o Veganuary (janeiro), Dia Mundial Vegano, Earth Day e épocas de legumes locais com menus especiais e calendário editorial."
      }
    ],
    "ctaTitle": "O seu restaurante plant-based com margem real e técnica de autor.",
    "ctaSubtitle": "Comece com o onboarding de 2 minutos. Plano Membro por 10 € por mês com 10.000 créditos para usar todos os agentes.",
    "seo": {
      "title": "IA para Restaurante Plant-Based e Vegano: Bowls, Custeios e Fermentos | AI Chef Pro",
      "description": "Suite de IA para restaurantes plant-based: VegChef, Fermentus para umami vegetal, custeios por bowl, branding e APPCC. Comece hoje.",
      "keywords": "IA restaurante vegano, software plant-based, custeios bowl vegano, cozinha vegana IA, fermentos vegetais, umami vegetal, Veganuary",
      "ogImage": "https://aichef.pro/og/use-cases/restaurante-plant-based.jpg"
    },
    "personalizationTitle": "Personalizado para o Seu Restaurante Plant-Based desde o Minuto Um",
    "personalizationBody": "AI Chef Pro arranca com o agente «Quem Sou Eu?», um onboarding conversacional de 2 minutos em que você conta que tipo de plant-based opera (casual healthy bowls, vegan fine dining, hamburgueria plant-based, restaurante vegano de autor, café vegano, dark kitchen vegana), tamanho da equipa, cidade e especialidade. Cada agente responde adaptado ao seu produto, mercado e operação real.",
    "appsTitle": "Os Agentes de IA que Vai Usar no Seu Restaurante Plant-Based",
    "apps": [
      {
        "name": "VegChef Plant-Based",
        "category": "Criatividade Culinária",
        "description": "Agente especializado em cozinha plant-based, vegana e vegetariana profissional com técnica avançada."
      },
      {
        "name": "Fermentus Con AI+",
        "category": "Criatividade Culinária",
        "description": "Koji vegetal, miso caseiro, shoyu, kimchi, kombucha e lactofermentos para umami profundo."
      },
      {
        "name": "Culinária Criativa",
        "category": "Criatividade Culinária",
        "description": "Desenvolvimento de bowls signature e pratos plant-based contemporâneos."
      },
      {
        "name": "Food Pairing AI",
        "category": "Criatividade Culinária",
        "description": "Maridagens com vinhos veganos, kombucha e bebidas funcionais."
      },
      {
        "name": "Restaurantes Casuais AI+",
        "category": "Conceitos de Negócio",
        "description": "Aconselhamento operativo para restaurantes plant-based casuais."
      },
      {
        "name": "Sosa Ingredients",
        "category": "Fornecedores Gastro",
        "description": "Catálogo Sosa para texturas vegetais, gelificantes plant-based e técnica."
      },
      {
        "name": "Mermas Genéricas",
        "category": "Ferramentas e Utilitários",
        "description": "Quebras em produto fresco vegetal, microgreens e proteínas caseiras."
      },
      {
        "name": "ID Alergénios",
        "category": "Ferramentas e Utilitários",
        "description": "Identificação automática: glúten, frutos secos, soja, sésamo (livres de produtos animais)."
      },
      {
        "name": "GastroIMG Gen+",
        "category": "Conhecimento Gastro",
        "description": "Fotografia vibrante IA de referência para Instagram, web, carta e delivery."
      },
      {
        "name": "InstaFlow AI Pro",
        "category": "Conteúdos e Redes Sociais",
        "description": "Instagram com calendário editorial vibrante para plant-based de autor."
      },
      {
        "name": "MenuDish Local SEO",
        "category": "Conteúdos e Redes Sociais",
        "description": "Captar clientes locais que procuram \"vegano perto\" ou \"plant-based perto\"."
      },
      {
        "name": "Gastro Calendar",
        "category": "Conteúdos e Redes Sociais",
        "description": "Veganuary, Dia Mundial Vegano, Earth Day, épocas de legumes."
      }
    ],
    "metrics": [
      {
        "value": "+6 pp",
        "label": "margem após custear bowls"
      },
      {
        "value": "×3",
        "label": "engagement Instagram com GastroIMG"
      },
      {
        "value": "−30 %",
        "label": "quebras em produto fresco"
      },
      {
        "value": "12+",
        "label": "agentes para a sua cozinha plant-based"
      }
    ],
    "beforeAfter": {
      "beforeTitle": "Sem AI Chef Pro",
      "beforeItems": [
        "Umami superficial sem técnica de fermentação profissional",
        "Custeios sem food cost real, bowls signature em perdas sem saber",
        "Quebras em produto fresco vegetal sem rastreabilidade",
        "Proteínas vegetais caseiras improvisadas sem padronização",
        "Instagram improvisado e plataformas de delivery com fotos do telemóvel"
      ],
      "afterTitle": "Com AI Chef Pro",
      "afterItems": [
        "Umami profundo com Fermentus: miso, koji, kimchi caseiros documentados",
        "Custeio profissional por bowl com margem validada",
        "Quebras controladas com Mermas Genéricas e modelos específicos",
        "Proteínas vegetais com técnica documentada (seitan, tempeh, tofu)",
        "GastroIMG Gen+ + InstaFlow + MenuDish Local SEO captam clientes locais"
      ]
    },
    "galleryTitle": "Como Funciona um Restaurante Plant-Based",
    "gallerySubtitle": "O que vai coordenar com o AI Chef Pro: bowls, burgers veganas, fermentos, mercado e equipa. Imagens geradas com IA como referência visual do conceito.",
    "galleryImages": [
      "/lovable-uploads/ai-gallery/use-case-plantbased-hero.jpg",
      "/lovable-uploads/ai-gallery/use-case-plantbased-burger.jpg",
      "/lovable-uploads/ai-gallery/use-case-plantbased-bowl.jpg",
      "/lovable-uploads/ai-gallery/use-case-plantbased-fermentos.jpg",
      "/lovable-uploads/ai-gallery/use-case-plantbased-mercado.jpg",
      "/lovable-uploads/ai-gallery/use-case-plantbased-team.jpg"
    ]
  },
  "asador-parrilla": {
    "h1": "IA para Churrasqueira, Grelha e Steakhouse",
    "heroSubtitle": "Desenvolve cartas de churrasqueira com técnica de brasas, escandallo por corte com custo real, gere dry-aged e planeia produção com uma suite de agentes de IA gastronómica especializados em cozinha ao fogo, churrasqueira e steakhouse profissional.",
    "heroTagline": "Churrasqueira com margem real e técnica de fogo",
    "badge": "Para churrasqueiras, grelhas, steakhouses e churrascarias",
    "painsTitle": "O Que uma Churrasqueira Não Pode Deixar de Resolver",
    "pains": [
      "Custo volátil da carne (chuletón, picanha, ribeye, T-bone) que muda o escandallo todas as semanas",
      "Padronizar ponto de cozedura e técnica de brasas turno a turno (desmancha, dry-aged, marmoreio, temperatura interna)",
      "Mermas em desmancha, dry-aging (3-12 % por semana), trimming e guarnições",
      "Gestão do dry-aged com câmara, humidade, temperatura e rotação de cortes",
      "Diferenciar-se em zona competitiva com cortes premium, técnica de brasas e storytelling de fornecedores pecuários",
      "Captar clientes corporativos e eventos privados com menus de churrasqueira com margem alta"
    ],
    "featuresTitle": "Como o AI Chef Pro Ajuda numa Churrasqueira",
    "features": [
      {
        "icon": "Flame",
        "title": "Culinária Criativa",
        "description": "Agente para desenvolver cartas de churrasqueira com técnica de brasas, marinadas, molhos e guarnições profissionais."
      },
      {
        "icon": "UtensilsCrossed",
        "title": "Cozinha Argentina + Brasileira",
        "description": "Receituários especializados: asado argentino com sal grosso, picanha brasileira, churrasco, chimichurri autêntico, farofa, vinagretes."
      },
      {
        "icon": "Wine",
        "title": "Bar & Lounge AI+",
        "description": "Harmonizações com vinhos tintos premium, whisky e coquetelaria de carácter para a sua churrasqueira."
      },
      {
        "icon": "Calculator",
        "title": "Escandallos por corte",
        "description": "Culinária Criativa entrega receita + escandallo CSV; Kit de Escandallos Pro gere-o com custo real por chuletón, picanha e T-bone."
      },
      {
        "icon": "CheckSquare",
        "title": "Kit de Tareas Restaurante Casual",
        "description": "Modelos: acendimento de brasas, desmancha, controlo dry-aged, mise de guarnições, encerramento."
      },
      {
        "icon": "ShieldCheck",
        "title": "Pack APPCC churrasqueira",
        "description": "Rastreabilidade da carne, dry-aging, temperaturas críticas em câmara e temperatura interna na cozedura."
      },
      {
        "icon": "Calendar",
        "title": "Gastro Calendar",
        "description": "Planeamento com datas-chave: Dia do Pai (chuletón), Natal, eventos corporativos, lançamento de cortes especiais por temporada."
      },
      {
        "icon": "Image",
        "title": "GastroIMG Gen+ + InstaFlow AI Pro",
        "description": "Fotografia premium IA de referência + Instagram: a churrasqueira vive do impacto visual das brasas e do corte."
      },
      {
        "icon": "BarChart3",
        "title": "Mermas Genéricas",
        "description": "Dados precisos de mermas em desmancha, dry-aging e trimming integrados no escandallo."
      }
    ],
    "workflowTitle": "Um Dia Real numa Churrasqueira com AI Chef Pro",
    "workflow": [
      "09:00 · Abertura — checklist Kit de Tareas: acendimento controlado de brasas (3 horas para chegar ao ponto), controlo da câmara dry-aged, desmancha de cortes para serviço.",
      "11:00 · Culinária Criativa + Cozinha Argentina — desenvolve um novo corte signature de chuletón galego dry-aged 60 dias com sal de Maldon fumada e chimichurri de ervas frescas. Receita + escandallo CSV.",
      "12:00 · Kit de Escandallos Pro — carrega o CSV com os seus preços reais de carne e dry-aged, calcula a merma por aging, valida a margem por corte.",
      "13:00 · Serviço meio-dia — grelha a pleno com cortes premium, mise de chimichurri, molhos e guarnições.",
      "17:00 · Pausa entre serviços — Bar & Lounge AI+ valida harmonizações com tintos para os novos cortes; Gastro Calendar planeia o menu especial do Dia do Pai.",
      "20:00 · Serviço jantar — picos coordenados, grelha com vários cortes simultâneos.",
      "22:00 · GastroIMG Gen+ + InstaFlow AI Pro — gera a imagem de referência do novo chuletón e os posts para Instagram.",
      "00:00 · Encerramento — limpeza profunda das grelhas, APPCC assinado, controlo da câmara dry-aged."
    ],
    "productsTitle": "Modelos e Kits Recomendados para Churrasqueira",
    "productIds": [
      "kit-tareas",
      "kit-escandallos",
      "pack-appcc",
      "kit-inventario",
      "kit-gestion-personal",
      "pro-prompts-ebook"
    ],
    "testimonialQuote": "Fizemos escandallo corte a corte e descobrimos que o T-bone que mais vendíamos na realidade estava em perdas devido à merma do dry-aged que não calculávamos. Redesenhámo-lo com Culinária Criativa ajustando porção e guarnições, sem tocar no preço, e subimos a margem 5 pontos. O planeamento do Dia do Pai com Gastro Calendar triplicou a faturação dessa semana.",
    "testimonialAuthor": "Pedro Aguirre",
    "testimonialRole": "Mestre churrasqueiro e proprietário, churrasqueira premium",
    "faqTitle": "Perguntas Frequentes de Churrasqueiras",
    "faqs": [
      {
        "q": "Serve para churrasqueira casual, grelha argentina, churrascaria brasileira ou steakhouse premium?",
        "a": "Para os quatro. Culinária Criativa + Cozinha Argentina + Cozinha Brasileira cobrem desde churrasqueira casual até steakhouse premium com cortes dry-aged, passando por grelha argentina tradicional e churrascaria brasileira com espetos."
      },
      {
        "q": "Cobre técnica de dry-aged e gestão de câmara?",
        "a": "Sim. Culinária Criativa raciocina como mestre churrasqueiro profissional: condições de câmara dry-aged (1-3 °C, 75-85 % humidade), tempos por corte, controlo de merma semanal, identificação de pellicle e rotação."
      },
      {
        "q": "Como é que eu giro o custo volátil da carne?",
        "a": "Kit de Escandallos Pro recalcula instantaneamente a margem quando atualiza o preço da carne. Mermas Genéricas adiciona o custo de mermas por dry-aging, desmancha e trimming. O corte reflete sempre o custo atual."
      },
      {
        "q": "Gera conteúdo visual para Instagram e eventos corporativos?",
        "a": "Sim. GastroIMG Gen+ gera imagens de referência profissionais de cortes e brasas para Instagram, web e carta; a churrasqueira vive do impacto visual. Lembre-se de que a imagem IA é de referência visual: a foto definitiva é feita por si com o seu corte real."
      },
      {
        "q": "Como é que me ajuda com eventos e festividades?",
        "a": "Gastro Calendar planeia Dia do Pai, Natal, eventos corporativos e lançamentos de cortes especiais com menus de churrasqueira e calendário editorial."
      }
    ],
    "ctaTitle": "A sua churrasqueira com margem real e técnica de fogo.",
    "ctaSubtitle": "Começa com o onboarding de 2 minutos. Plano Membro por 10 € por mês com 10.000 créditos para usar todos os agentes.",
    "seo": {
      "title": "IA para Churrasqueira, Grelha e Steakhouse: Cortes, Escandallos e Dry-Aged | AI Chef Pro",
      "description": "Suite de IA para churrasqueiras e steakhouses: Cozinha Argentina + Brasileira, escandallos por corte, dry-aged, branding e APPCC. Comece hoje.",
      "keywords": "IA churrasqueira, software steakhouse, escandallos chuletón, grelha argentina IA, dry-aged, churrascaria, churrasqueira premium",
      "ogImage": "https://aichef.pro/og/use-cases/asador-parrilla-steakhouse.jpg"
    },
    "personalizationTitle": "Personalizado para a Sua Churrasqueira desde o Primeiro Minuto",
    "personalizationBody": "AI Chef Pro arranca com o agente «Quem Sou Eu?», um onboarding conversacional de 2 minutos em que lhe conta que tipo de churrasqueira opera (grelha argentina, churrascaria brasileira, steakhouse premium com dry-aged, churrasqueira casual de bairro, churrasqueira com cozinha de autor), tamanho da equipa, cidade e especialidade. Cada agente responde adaptado ao seu produto, mercado e operativa real.",
    "appsTitle": "Os Agentes IA que Vai Usar na Sua Churrasqueira",
    "apps": [
      {
        "name": "Culinária Criativa",
        "category": "Criatividade Culinária",
        "description": "Desenvolvimento de cartas de churrasqueira com técnica de brasas, marinadas e guarnições profissionais."
      },
      {
        "name": "Cozinha Argentina",
        "category": "Receituários da América Latina",
        "description": "Asado argentino, chimichurri, provolone, mollejas e técnica de grelha autêntica."
      },
      {
        "name": "Cozinha Brasileira",
        "category": "Receituários da América Latina",
        "description": "Picanha, churrasco, farofa, vinagrete e técnica de churrascaria brasileira."
      },
      {
        "name": "Food Pairing AI",
        "category": "Criatividade Culinária",
        "description": "Harmonizações com tintos potentes, whisky e coquetelaria de carácter para churrasqueira."
      },
      {
        "name": "Bar & Lounge AI+",
        "category": "Conceitos de Negócio",
        "description": "Para a barra da churrasqueira com vinhos tintos premium e coquetelaria de carácter."
      },
      {
        "name": "Sosa Ingredients",
        "category": "Fornecedores Gastro",
        "description": "Catálogo Sosa para texturas, sais temperadas e técnicas aplicadas a molhos e marinadas."
      },
      {
        "name": "Mermas Genéricas",
        "category": "Ferramentas e Utilitários",
        "description": "Mermas em desmancha, dry-aging, trimming e cozedura."
      },
      {
        "name": "ID Alergénios",
        "category": "Ferramentas e Utilitários",
        "description": "Identificação automática de alergénios por corte e guarnição."
      },
      {
        "name": "GastroIMG Gen+",
        "category": "Conhecimento Gastro",
        "description": "Fotografia premium IA de referência para Instagram, web, carta e delivery."
      },
      {
        "name": "InstaFlow AI Pro",
        "category": "Conteúdos e Redes Sociais",
        "description": "Instagram com calendário editorial profissional para churrasqueira premium."
      },
      {
        "name": "MenuDish Local SEO",
        "category": "Conteúdos e Redes Sociais",
        "description": "Captar clientes locais que procuram \"churrasqueira perto\" ou \"grelha argentina\"."
      },
      {
        "name": "Gastro Calendar",
        "category": "Conteúdos e Redes Sociais",
        "description": "Dia do Pai, Natal, eventos corporativos, lançamentos por temporada."
      }
    ],
    "metrics": [
      {
        "value": "+5 pp",
        "label": "margem após escandallar cortes"
      },
      {
        "value": "×3",
        "label": "faturação no Dia do Pai"
      },
      {
        "value": "−15 %",
        "label": "mermas em desmancha e dry-aging"
      },
      {
        "value": "12+",
        "label": "agentes para a sua churrasqueira"
      }
    ],
    "beforeAfter": {
      "beforeTitle": "Sem AI Chef Pro",
      "beforeItems": [
        "Ponto de cozedura improvisado, consistência variável entre grelhador e turno",
        "Escandallos sem merma do dry-aged, cortes premium em perdas sem saber",
        "Câmara dry-aged sem rastreabilidade real nem controlo documentado",
        "Mermas em desmancha e trimming sem rastreabilidade",
        "Instagram improvisado, sem storytelling de fornecedor pecuário"
      ],
      "afterTitle": "Com AI Chef Pro",
      "afterItems": [
        "Ponto de cozedura consistente com critério técnico documentado",
        "Escandallo profissional por corte com merma de dry-aged integrada",
        "Câmara dry-aged com rastreabilidade APPCC e rotação documentada",
        "Mermas controladas com Mermas Genéricas e modelos específicos",
        "GastroIMG Gen+ + InstaFlow + storytelling de fornecedor pecuário"
      ]
    },
    "galleryTitle": "Como Funciona uma Churrasqueira",
    "gallerySubtitle": "O que vai coordenar com AI Chef Pro: grelha, brasas, dry-aged, cortes e equipa. Imagens geradas com IA como referência visual do conceito.",
    "galleryImages": [
      "/lovable-uploads/ai-gallery/use-case-asador-hero.jpg",
      "/lovable-uploads/ai-gallery/use-case-asador-brasas.jpg",
      "/lovable-uploads/ai-gallery/use-case-asador-dryaged.jpg",
      "/lovable-uploads/ai-gallery/use-case-asador-chuleton.jpg",
      "/lovable-uploads/ai-gallery/use-case-asador-despiece.jpg",
      "/lovable-uploads/ai-gallery/use-case-asador-team.jpg"
    ]
  },
  "coffee-shop-specialty": {
    "h1": "IA para Coffee Shop e Specialty Coffee",
    "heroSubtitle": "Desenha carta de cafés de especialidade com critério third-wave, escandallo por bebida com custo real, planifica produção de pastelaria própria e captura branding minimalista com uma suite de agentes de IA gastronómica especializados em specialty coffee profissional.",
    "heroTagline": "Café de especialidade com margem real e técnica third-wave",
    "badge": "Para coffee shops, specialty cafés e third-wave coffee",
    "painsTitle": "O Que um Coffee Shop Não Pode Deixar de Resolver",
    "pains": [
      "Elaborar carta de café de especialidade com critério: single origins, blends, métodos (espresso, V60, Aeropress, Chemex)",
      "Escandallar cada bebida com custo real (gramagem, leite premium, alternativas vegetais) e food cost coerente",
      "Mermas em café moído (degradação rápida), leite e produto fresco de pastelaria",
      "Padronizar técnica de barista turno a turno: extração, latte art, dosagem, calibração",
      "Diferenciar-se em zona competitiva com café de origem rastreada, branding visual minimalista e formação constante",
      "Captar clientes locais recorrentes e vender grãos para casa com margem alta"
    ],
    "featuresTitle": "Como AI Chef Pro Ajuda num Coffee Shop",
    "features": [
      {
        "icon": "Coffee",
        "title": "Culinária Criativa",
        "description": "Para desenvolvimento de signatures: cold brews infusionados, lattes com xarope caseiro, especialidades sazonais."
      },
      {
        "icon": "Cake",
        "title": "Pastelaria Criativa",
        "description": "Para pastelaria própria que diferencia o coffee shop: croissants, brownies, cookies, banana bread, bolo do dia."
      },
      {
        "icon": "Calculator",
        "title": "Escandallos por bebida",
        "description": "Culinária Criativa entrega receita + escandallo CSV; Kit de Escandallos Pro gere-o com custo real por café e leite, food cost % validado."
      },
      {
        "icon": "CheckSquare",
        "title": "Kit de Tareas Cafetería / Brunch",
        "description": "Modelos: prep barra, calibração espresso, prep alternativas vegetais, mise pastelaria, encerramento."
      },
      {
        "icon": "ShieldCheck",
        "title": "Pack APPCC cafetería",
        "description": "Rastreabilidade de café moído, leite, alternativas vegetais e pastelaria própria."
      },
      {
        "icon": "Calendar",
        "title": "Gastro Calendar",
        "description": "Lançamentos sazonais: pumpkin spice latte (outono), cold brew (verão), café especiado Natal."
      },
      {
        "icon": "Image",
        "title": "GastroIMG Gen+ + InstaFlow AI Pro",
        "description": "Fotografia minimalista IA de referência + Instagram: o specialty coffee vive do impacto visual do latte art."
      },
      {
        "icon": "BarChart3",
        "title": "MenuDish Local SEO",
        "description": "Captar clientes locais que procuram \"specialty coffee perto\" no Google e Maps."
      },
      {
        "icon": "BookOpen",
        "title": "BlogPost SEO Gen+",
        "description": "Artigos SEO sobre origem do café, métodos de filtragem e harmonização com pastelaria para captar tráfego orgânico."
      }
    ],
    "workflowTitle": "Um Dia Real num Coffee Shop com AI Chef Pro",
    "workflow": [
      "07:00 · Abertura — checklist Kit de Tareas: calibração de espresso, prep de leites e alternativas vegetais, mise de pastelaria do dia.",
      "08:00 · Serviço manhã — pico da manhã com cafés de qualidade consistente, latte art profissional.",
      "11:00 · Culinária Criativa — desenvolve um novo signature de outono: latte de abóbora com xarope caseiro. Receita + escandallo CSV.",
      "12:00 · Kit de Escandallos Pro — carrega o CSV com os seus preços reais de café, leite e xaropes, valida margem e food cost %.",
      "14:00 · Pastelaria Criativa — desenvolve um novo banana bread vegano para complementar a carta.",
      "17:00 · GastroIMG Gen+ + InstaFlow AI Pro — gera a imagem de referência do novo signature e os posts minimalistas para Instagram.",
      "19:00 · Encerramento — limpeza profunda da máquina, calibração para amanhã, controlo de stock de café e leite.",
      "20:00 · BlogPost SEO Gen+ — programa um artigo sobre métodos de filtragem para captar tráfego orgânico."
    ],
    "productsTitle": "Modelos e Kits Recomendados para Coffee Shop",
    "productIds": [
      "kit-tareas-cafeteria",
      "kit-escandallos",
      "pack-appcc",
      "kit-inventario",
      "kit-gestion-personal",
      "pro-prompts-ebook"
    ],
    "testimonialQuote": "Culinária Criativa + Pastelaria Criativa mudaram-nos a proposta. Lançámos signatures sazonais com escandallo profissional, a pastelaria própria subiu 30% do ticket médio e a formação de baristas é agora consistente. Captação local com MenuDish + GastroIMG Gen+ duplicou em 4 meses.",
    "testimonialAuthor": "Marta Esteve",
    "testimonialRole": "Proprietária, specialty coffee third-wave",
    "faqTitle": "Perguntas Frequentes de Coffee Shops",
    "faqs": [
      {
        "q": "Serve para coffee shop casual, specialty coffee third-wave ou roastery com loja?",
        "a": "Para os três. Culinária Criativa cobre desde signatures simples até carta de specialty com métodos de filtragem avançados."
      },
      {
        "q": "Como escandallar bebidas com leite e alternativas vegetais?",
        "a": "Culinária Criativa raciocina como barista profissional: gramagem exata de café, rácio de leite, custo de aveia premium vs. soja. Kit de Escandallos Pro recalcula instantaneamente."
      },
      {
        "q": "Cobre pastelaria própria para diferenciar?",
        "a": "Sim. Pastelaria Criativa entrega croissants, brownies, banana bread, cookies e especialidades da época com escandallo profissional."
      },
      {
        "q": "Gera conteúdo visual minimalista para Instagram?",
        "a": "Sim. GastroIMG Gen+ gera imagens de referência com paleta cream e warm wood. Lembre-se que a imagem IA é de referência visual: a foto definitiva é feita por si com o seu latte real."
      },
      {
        "q": "Como me ajuda com lançamentos sazonais?",
        "a": "Gastro Calendar planifica pumpkin spice latte (outono), cold brew (verão), café especiado de Natal e signatures por época."
      }
    ],
    "ctaTitle": "O seu coffee shop com margem real e técnica third-wave.",
    "ctaSubtitle": "Comece com o onboarding de 2 minutos. Plano Membro por 10 € por mês com 10.000 créditos.",
    "seo": {
      "title": "IA para Coffee Shop e Specialty Coffee: Cartas, Escandallos e Branding | AI Chef Pro",
      "description": "Suite de IA para coffee shops: Culinária Criativa, Pastelaria própria, escandallos por bebida, branding minimalista e captação local. Comece hoje.",
      "keywords": "IA coffee shop, software specialty coffee, escandallos café, third-wave coffee IA, latte art, café especialidade",
      "ogImage": "https://aichef.pro/og/use-cases/coffee-shop-specialty.jpg"
    },
    "personalizationTitle": "Personalizado ao Seu Coffee Shop desde o Minuto Um",
    "personalizationBody": "AI Chef Pro arranca com o agente «Quem Sou Eu?», um onboarding de 2 minutos em que lhe conta que tipo de coffee shop opera (specialty third-wave, coffee shop casual, roastery com loja, café com pastelaria própria), tamanho da equipa, cidade e especialidade.",
    "appsTitle": "Os Agentes IA que Vai Usar no Seu Coffee Shop",
    "apps": [
      {
        "name": "Culinária Criativa",
        "category": "Criatividade Culinária",
        "description": "Desenvolvimento de signatures: cold brews, lattes especiados, especialidades sazonais."
      },
      {
        "name": "Pastelaria Criativa",
        "category": "Criatividade Culinária",
        "description": "Pastelaria própria: croissants, brownies, banana bread, cookies."
      },
      {
        "name": "Restaurantes Casuais AI+",
        "category": "Conceitos de Negócio",
        "description": "Aconselhamento operativo para cafés e brunches."
      },
      {
        "name": "Sosa Ingredients",
        "category": "Fornecedores Gastro",
        "description": "Catálogo Sosa para xaropes, texturas e aplicações especiais."
      },
      {
        "name": "Mermas Genéricas",
        "category": "Ferramentas e Utilitários",
        "description": "Mermas em café moído e leite."
      },
      {
        "name": "ID Alergénios",
        "category": "Ferramentas e Utilitários",
        "description": "Identificação automática para alternativas vegetais e pastelaria."
      },
      {
        "name": "GastroIMG Gen+",
        "category": "Gastro Conhecimento",
        "description": "Fotografia minimalista IA de referência para Instagram, web e carta."
      },
      {
        "name": "InstaFlow AI Pro",
        "category": "Conteúdos e Redes Sociais",
        "description": "Instagram com calendário editorial minimalista."
      },
      {
        "name": "MenuDish Local SEO",
        "category": "Conteúdos e Redes Sociais",
        "description": "Captar clientes locais que procuram \"specialty coffee perto\"."
      },
      {
        "name": "Gastro Calendar",
        "category": "Conteúdos e Redes Sociais",
        "description": "Lançamentos sazonais e signatures por época."
      },
      {
        "name": "BlogPost SEO Gen+",
        "category": "Conteúdos e Redes Sociais",
        "description": "Artigos SEO sobre origem do café e métodos."
      },
      {
        "name": "Gerador de Pins Pinterest",
        "category": "Conteúdos e Redes Sociais",
        "description": "Pinterest captura tráfego para latte art e pastelaria própria."
      }
    ],
    "metrics": [
      {
        "value": "+5 pp",
        "label": "margem após escandallar bebidas"
      },
      {
        "value": "+30 %",
        "label": "ticket médio com pastelaria própria"
      },
      {
        "value": "×2",
        "label": "captação local com MenuDish"
      },
      {
        "value": "12+",
        "label": "agentes para o seu coffee shop"
      }
    ],
    "beforeAfter": {
      "beforeTitle": "Sem AI Chef Pro",
      "beforeItems": [
        "Cartas sazonais improvisadas, signatures sem escandallo",
        "Pastelaria externa com margem incerta",
        "Calibração variável entre baristas",
        "Instagram improvisado sem paleta minimalista",
        "Captação local sem SEO de Maps"
      ],
      "afterTitle": "Com AI Chef Pro",
      "afterItems": [
        "Signatures sazonais com escandallo profissional",
        "Pastelaria própria com Pastelaria Criativa e margem alta",
        "Calibração consistente com modelos de Kit de Tareas",
        "GastroIMG Gen+ + InstaFlow minimalistas",
        "MenuDish Local SEO captura \"specialty coffee perto\""
      ]
    },
    "galleryTitle": "Como Funciona um Coffee Shop",
    "gallerySubtitle": "O que vai coordenar com AI Chef Pro: latte art, café de origem, pastelaria, barra e equipa. Imagens geradas com IA como referência visual do conceito.",
    "galleryImages": [
      "/lovable-uploads/ai-gallery/use-case-coffee-shop-hero.jpg",
      "/lovable-uploads/ai-gallery/use-case-coffee-shop-pour.jpg",
      "/lovable-uploads/ai-gallery/use-case-coffee-shop-beans.jpg",
      "/lovable-uploads/ai-gallery/use-case-coffee-shop-pastries.jpg",
      "/lovable-uploads/ai-gallery/use-case-coffee-shop-bar.jpg",
      "/lovable-uploads/ai-gallery/use-case-coffee-shop-team.jpg"
    ]
  },
  "sushi-bar": {
    "h1": "IA para Sushi Bar",
    "heroSubtitle": "Domine técnica itamae com cálculo de custos rigoroso por nigiri, gerencie peixe fresco diário, desenhe omakase signature e capture branding minimalista com uma suite de agentes de IA gastronómica especializados em sushi bar profissional.",
    "heroTagline": "Sushi bar com técnica autêntica e margem real",
    "badge": "Para sushi bars, omakase e sushi shops",
    "painsTitle": "O Que um Sushi Bar Não Pode Deixar de Resolver",
    "pains": [
      "Peixe fresco diário para nigiri e sashimi com custo volátil e quebras estritas por processo de filetagem",
      "Padronizar shari (arroz de sushi) em cada turno com equilíbrio técnico de vinagre, açúcar e sal",
      "Coordenar técnica itamae com consistência: corte, pressão, temperatura do arroz, neta a temperatura ótima",
      "Diferenciar-se em zona competitiva com omakase signature, fish-of-the-day e storytelling de fornecedores",
      "Captar clientes premium com experiência em frente ao itamae na barra (não mesa)",
      "Captar pedidos de delivery sem perder qualidade do sushi (janela ótima 1-2 horas)"
    ],
    "featuresTitle": "Como a AI Chef Pro Ajuda num Sushi Bar",
    "features": [
      {
        "icon": "Fish",
        "title": "Cozinha Japonesa",
        "description": "Agente especializado em sushi profissional: técnica itamae, equilíbrio de shari, filetagem, neta a temperatura ótima."
      },
      {
        "icon": "Sparkles",
        "title": "Culinária Criativa",
        "description": "Para nigiri signature e omakase contemporâneo com base autêntica."
      },
      {
        "icon": "Beaker",
        "title": "Fermentus Con AI+",
        "description": "Para fermentos e técnicas avançadas de cozinha japonesa."
      },
      {
        "icon": "Calculator",
        "title": "Cálculo de custos por nigiri e omakase",
        "description": "Cozinha Japonesa entrega receita + cálculo de custos CSV; Kit de Escandallos Pro gere-o com custo real por peça e omakase."
      },
      {
        "icon": "CheckSquare",
        "title": "Kit de Tareas Restaurante Casual",
        "description": "Modelos: filetagem, preparação de shari, mise itamae, encerramento."
      },
      {
        "icon": "ShieldCheck",
        "title": "Pack APPCC sushi",
        "description": "Rastreabilidade de peixe para sushi e temperaturas críticas."
      },
      {
        "icon": "Wine",
        "title": "Bar & Lounge AI+",
        "description": "Para sake, whisky japonês e harmonizações profissionais."
      },
      {
        "icon": "Calendar",
        "title": "Gastro Calendar",
        "description": "Hanami, Ano Novo japonês, Dia do Sushi, eventos premium."
      },
      {
        "icon": "Image",
        "title": "GastroIMG Gen+ + InstaFlow AI Pro",
        "description": "Fotografia minimalista IA de referência + Instagram para sushi bar premium."
      }
    ],
    "workflowTitle": "Um Dia Real num Sushi Bar com AI Chef Pro",
    "workflow": [
      "08:00 · Abertura — checklist Kit de Tareas: receção de peixe fresco diário, filetagem de blocos, preparação de shari (vinagre + açúcar + sal equilibrados).",
      "10:00 · Cozinha Japonesa — desenvolve um novo nigiri signature de hamachi com yuzu kosho e wasabi fresco. Receita + cálculo de custos CSV.",
      "11:00 · Kit de Escandallos Pro — carrega o CSV com os seus preços reais de peixe do dia, valida margem por nigiri e por omakase.",
      "13:00 · Serviço de meio-dia — sushi bar a pleno com itamae a trabalhar em frente ao cliente.",
      "17:00 · Briefing à equipa — explicação do novo nigiri e harmonizações com sake.",
      "20:00 · Serviço de jantar — omakase signature, picos coordenados.",
      "22:00 · GastroIMG Gen+ + InstaFlow AI Pro — gera imagem de referência minimalista do novo nigiri.",
      "23:00 · Encerramento — limpeza profunda, APPCC assinado."
    ],
    "productsTitle": "Modelos e Kits Recomendados para Sushi Bar",
    "productIds": [
      "guia-restaurante-japones",
      "kit-escandallos",
      "pack-appcc",
      "kit-inventario",
      "kit-gestion-personal",
      "pro-prompts-ebook"
    ],
    "testimonialQuote": "Cozinha Japonesa mudou a nossa operativa. O equilíbrio do shari é agora consistente, o omakase tem cálculo de custos profissional com margem validada peça a peça. A captação de clientes premium com GastroIMG Gen+ subiu 40% em 6 meses.",
    "testimonialAuthor": "Akio Yamamoto",
    "testimonialRole": "Itamae e proprietário, sushi bar contemporâneo",
    "faqTitle": "Perguntas Frequentes de Sushi Bars",
    "faqs": [
      {
        "q": "Serve para sushi bar casual ou omakase premium?",
        "a": "Para os dois. Cozinha Japonesa cobre desde sushi tradicional até omakase de autor."
      },
      {
        "q": "Cobre técnica de itamae?",
        "a": "Sim. Cozinha Japonesa raciocina como itamae profissional: técnica de filetagem, equilíbrio de shari, neta e combinações."
      },
      {
        "q": "Como gerencio o custo do peixe fresco?",
        "a": "Kit de Escandallos Pro recalcula instantaneamente a margem quando atualiza preços do dia."
      },
      {
        "q": "Gera conteúdo visual minimalista?",
        "a": "Sim. GastroIMG Gen+ gera imagens de referência. Lembre-se de que a imagem IA é de referência visual: a foto definitiva é feita por si com a sua peça real."
      },
      {
        "q": "Como me ajuda com omakase e eventos premium?",
        "a": "Gastro Calendar planeia omakase sazonal, Hanami, Ano Novo japonês com menus de degustação premium."
      }
    ],
    "ctaTitle": "O seu sushi bar com técnica autêntica e margem real.",
    "ctaSubtitle": "Comece com o onboarding de 2 minutos. Plano Membro por 10 € por mês com 10.000 créditos.",
    "seo": {
      "title": "IA para Sushi Bar: Itamae, Omakase e Cálculo de Custos | AI Chef Pro",
      "description": "Suite de IA para sushi bars: Cozinha Japonesa, Fermentus, cálculo de custos por nigiri, omakase e branding minimalista. Comece hoje.",
      "keywords": "IA sushi bar, software sushi, cálculo de custos sushi, itamae profissional, omakase IA, técnica japonesa",
      "ogImage": "https://aichef.pro/og/use-cases/sushi-bar.jpg"
    },
    "personalizationTitle": "Personalizado para o Seu Sushi Bar desde o Minuto Um",
    "personalizationBody": "AI Chef Pro arranca com o agente «Quem Sou Eu?», um onboarding de 2 minutos em que lhe conta que tipo de sushi bar opera (sushi bar casual, omakase premium, kaiten, sushi bar com cozinha quente), tamanho da equipa, cidade e especialidade.",
    "appsTitle": "Os Agentes de IA que Vai Usar no Seu Sushi Bar",
    "apps": [
      {
        "name": "Cozinha Japonesa",
        "category": "Receituários da Ásia",
        "description": "Sushi profissional: técnica itamae, sashimi, omakase."
      },
      {
        "name": "Culinária Criativa",
        "category": "Criatividade Culinária",
        "description": "Nigiri signature e omakase com receita + cálculo de custos CSV."
      },
      {
        "name": "Fermentus Con AI+",
        "category": "Criatividade Culinária",
        "description": "Fermentos para técnicas avançadas."
      },
      {
        "name": "Food Pairing AI",
        "category": "Criatividade Culinária",
        "description": "Harmonizações com sake, whisky japonês e cerveja."
      },
      {
        "name": "Bar & Lounge AI+",
        "category": "Conceitos de Negócio",
        "description": "Barra de sake e whisky japonês."
      },
      {
        "name": "Mermas Genéricas",
        "category": "Ferramentas e Utilitários",
        "description": "Quebras em filetagem de peixe."
      },
      {
        "name": "ID Alergénios",
        "category": "Ferramentas e Utilitários",
        "description": "Identificação de peixe, mariscos, soja, glúten."
      },
      {
        "name": "GastroIMG Gen+",
        "category": "Gastro Conhecimento",
        "description": "Fotografia minimalista IA de referência."
      },
      {
        "name": "InstaFlow AI Pro",
        "category": "Conteúdos e Redes Sociais",
        "description": "Instagram minimalista para sushi bar premium."
      },
      {
        "name": "MenuDish Local SEO",
        "category": "Conteúdos e Redes Sociais",
        "description": "Captar clientes que procuram \"sushi perto\"."
      },
      {
        "name": "Gastro Calendar",
        "category": "Conteúdos e Redes Sociais",
        "description": "Hanami, Ano Novo japonês, omakase sazonal."
      },
      {
        "name": "Sosa Ingredients",
        "category": "Fornecedores Gastro",
        "description": "Catálogo Sosa para texturas avançadas."
      }
    ],
    "metrics": [
      {
        "value": "+6 pp",
        "label": "margem após cálculo de custos do omakase"
      },
      {
        "value": "+40 %",
        "label": "captação premium em 6 meses"
      },
      {
        "value": "−20 %",
        "label": "quebras em filetagem"
      },
      {
        "value": "12+",
        "label": "agentes para o seu sushi bar"
      }
    ],
    "beforeAfter": {
      "beforeTitle": "Sem AI Chef Pro",
      "beforeItems": [
        "Shari improvisado, equilíbrio inconsistente",
        "Cálculo de custos sem preço do peixe do dia",
        "Omakase improvisado sem cálculo de custos",
        "Instagram sem paleta minimalista",
        "Captação local sem SEO"
      ],
      "afterTitle": "Com AI Chef Pro",
      "afterItems": [
        "Shari e técnica com critério profissional",
        "Cálculo de custos em tempo real com preço do dia",
        "Omakase com cálculo de custos validado peça a peça",
        "GastroIMG Gen+ + InstaFlow minimalistas",
        "MenuDish Local SEO captura \"sushi perto\""
      ]
    },
    "galleryTitle": "Como Funciona um Sushi Bar",
    "gallerySubtitle": "O que vai coordenar com a AI Chef Pro: counter, omakase, peixe, sake e equipa. Imagens geradas com IA como referência visual do conceito.",
    "galleryImages": [
      "/lovable-uploads/ai-gallery/use-case-sushi-bar-hero.jpg",
      "/lovable-uploads/ai-gallery/use-case-sushi-bar-counter.jpg",
      "/lovable-uploads/ai-gallery/use-case-sushi-bar-omakase.jpg",
      "/lovable-uploads/ai-gallery/use-case-sushi-bar-fish.jpg",
      "/lovable-uploads/ai-gallery/use-case-sushi-bar-sake.jpg",
      "/lovable-uploads/ai-gallery/use-case-sushi-bar-team.jpg"
    ]
  },
  "gastrobar-tapas": {
    "h1": "IA para Gastrobar e Bar de Tapas",
    "heroSubtitle": "Crie carta de tapas e pintxos com ficha de custos profissional, gere vermute e vinhos à copa, planeie eventos e capture branding espanhol autêntico com uma suite de agentes de IA gastronómica especializados em gastrobar e cozinha espanhola.",
    "heroTagline": "Tapas com técnica autêntica e margem real",
    "badge": "Para gastrobares, bares de tapas, pintxos e vinotecas",
    "painsTitle": "O Que um Gastrobar Não Pode Deixar de Resolver",
    "pains": [
      "Carta de tapas com muitas variantes (frias, quentes, pintxos, rações) mantendo food cost coerente",
      "Quebras em produto fresco (anchova, presunto, marisco), pão e enchidos com validade curta",
      "Padronizar tapas de assinatura turno a turno com consistência e velocidade de serviço",
      "Gestão de vermute, vinhos à copa e cervejas com margem alta e rotação correta",
      "Diferenciar-se com produto de qualidade, branding espanhol autêntico e storytelling de fornecedores artesanais",
      "Captar eventos privados e provas com maridagens profissionais"
    ],
    "featuresTitle": "Como o AI Chef Pro Ajuda num Gastrobar",
    "features": [
      {
        "icon": "Wine",
        "title": "Restaurantes Casuais AI+",
        "description": "Aconselhamento operativo para gastrobares e bares de tapas."
      },
      {
        "icon": "Sparkles",
        "title": "Cozinha Espanhola + Culinária Criativa",
        "description": "Receituários especializados: tapas tradicionais, pintxos bascos, rações de mercado, fusões."
      },
      {
        "icon": "Calculator",
        "title": "Fichas de custos por tapa e ração",
        "description": "Culinária Criativa entrega receita + ficha de custos CSV; Kit de Escandallos Pro gere-a com custo real por tapa e food cost %."
      },
      {
        "icon": "Wine",
        "title": "Bar & Lounge AI+",
        "description": "Vermutes, vinhos espanhóis à copa, cervejas artesanais e maridagens com tapas."
      },
      {
        "icon": "CheckSquare",
        "title": "Kit de Tareas Bar",
        "description": "Modelos: preparação de tapas, mise da barra, vermute, encerramento."
      },
      {
        "icon": "ShieldCheck",
        "title": "Pack APPCC bar",
        "description": "Rastreabilidade de presunto, enchidos, anchova, marisco fresco."
      },
      {
        "icon": "Calendar",
        "title": "Gastro Calendar",
        "description": "Dia Mundial da Tapa, São Firmino, festas locais, eventos privados."
      },
      {
        "icon": "Image",
        "title": "GastroIMG Gen+ + InstaFlow AI Pro",
        "description": "Fotografia artesanal espanhola IA + Instagram para captar locais e turistas."
      },
      {
        "icon": "BarChart3",
        "title": "MenuDish Local SEO",
        "description": "Captar clientes que procuram \"tapas perto\" ou \"gastrobar [cidade]\"."
      }
    ],
    "workflowTitle": "Um Dia Real num Gastrobar com AI Chef Pro",
    "workflow": [
      "11:00 · Abertura — checklist Kit de Tareas: preparação de tapas frias, montagem do suporte de presunto, mise da barra, controlo de vermute de pressão.",
      "12:30 · Cozinha Espanhola + Culinária Criativa — desenvolve uma nova tapa de assinatura de biqueirão curado em casa com piparra e azeite de tomate. Receita + ficha de custos CSV.",
      "13:30 · Kit de Escandallos Pro — carrega o CSV com os seus preços reais, valida margem por tapa e food cost %.",
      "14:00 · Serviço de meio-dia — pico forte com vermute e tapas, mise impecável.",
      "17:00 · Pausa — Bar & Lounge AI+ valida maridagens com vinhos albariño e verdejo para novas tapas.",
      "19:00 · Serviço de noite — picos com cervejas artesanais e vinhos à copa.",
      "22:00 · GastroIMG Gen+ + InstaFlow AI Pro — gera imagem de referência e posts.",
      "00:00 · Encerramento — limpeza, APPCC assinado, controlo de stock."
    ],
    "productsTitle": "Modelos e Kits Recomendados para Gastrobar",
    "productIds": [
      "kit-tareas-bar",
      "kit-escandallos",
      "pack-appcc",
      "kit-inventario",
      "kit-gestion-personal",
      "pro-prompts-ebook"
    ],
    "testimonialQuote": "Cozinha Espanhola + Bar & Lounge AI+ elevaram o nosso nível. As tapas de assinatura têm agora ficha de custos profissional com margem validada, os maridagens com vinhos à copa são consistentes e subimos o ticket médio 15% em 4 meses. A captação local com MenuDish + GastroIMG é x2.",
    "testimonialAuthor": "Iñaki Etxeberria",
    "testimonialRole": "Proprietário, gastrobar contemporâneo em Donostia",
    "faqTitle": "Perguntas Frequentes de Gastrobares",
    "faqs": [
      {
        "q": "Serve para gastrobar casual, bar de tapas tradicional, pintxos bascos ou vinoteca com tapas?",
        "a": "Para os quatro. Cozinha Espanhola + Restaurantes Casuais AI+ cobrem desde tapas tradicionais até gastrobares contemporâneos."
      },
      {
        "q": "Cobre vermute, vinhos e cervejas com maridagens?",
        "a": "Sim. Bar & Lounge AI+ cobre vermute, vinhos espanhóis à copa, cervejas artesanais e maridagens com tapas."
      },
      {
        "q": "Como gerir quebras em presunto e produto fresco?",
        "a": "Mermas Genéricas entrega dados por processo (corte de presunto, anchova, marisco). Integram-se na ficha de custos."
      },
      {
        "q": "Gera conteúdo visual para Instagram?",
        "a": "Sim. GastroIMG Gen+ gera imagens de referência. Lembre-se de que a imagem IA é de referência visual: a foto definitiva é tirada por si com a sua tapa real."
      },
      {
        "q": "Como me ajuda com eventos privados e provas?",
        "a": "Gastro Calendar planifica provas com adegas, eventos privados, São Firmino e festas locais."
      }
    ],
    "ctaTitle": "O seu gastrobar com margem real e técnica autêntica.",
    "ctaSubtitle": "Comece com o onboarding de 2 minutos. Plano Membro por 10 € por mês com 10.000 créditos.",
    "seo": {
      "title": "IA para Gastrobar e Bar de Tapas: Tapas, Fichas de Custos e Maridagens | AI Chef Pro",
      "description": "Suite de IA para gastrobares: Cozinha Espanhola, Bar & Lounge AI+, fichas de custos por tapa, vermute e vinhos à copa. Comece hoje.",
      "keywords": "IA gastrobar, software bar de tapas, fichas de custos tapa, pintxos IA, vermute tapas, gastrobar contemporâneo",
      "ogImage": "https://aichef.pro/og/use-cases/gastrobar-tapas.jpg"
    },
    "personalizationTitle": "Personalizado para o Seu Gastrobar desde o Minuto Um",
    "personalizationBody": "AI Chef Pro começa com o agente «Quem Sou Eu?», um onboarding de 2 minutos em que lhe conta que tipo de gastrobar opera (gastrobar contemporâneo, bar de tapas tradicional, pintxos bascos, vinoteca com tapas), dimensão da equipa, cidade e especialidade.",
    "appsTitle": "Os Agentes de IA que Vai Usar no Seu Gastrobar",
    "apps": [
      {
        "name": "Cozinha Espanhola",
        "category": "Receituários da Europa",
        "description": "Tapas tradicionais, pintxos, rações de mercado."
      },
      {
        "name": "Culinária Criativa",
        "category": "Criatividade Culinária",
        "description": "Tapas de assinatura contemporâneas com receita + ficha de custos CSV."
      },
      {
        "name": "Bar & Lounge AI+",
        "category": "Conceitos de Negócio",
        "description": "Vermute, vinhos espanhóis, cervejas e maridagens."
      },
      {
        "name": "Restaurantes Casuais AI+",
        "category": "Conceitos de Negócio",
        "description": "Aconselhamento operativo para gastrobares."
      },
      {
        "name": "Food Pairing AI",
        "category": "Criatividade Culinária",
        "description": "Maridagens com vinhos e cervejas para tapas."
      },
      {
        "name": "Sosa Ingredients",
        "category": "Fornecedores Gastro",
        "description": "Catálogo Sosa para texturas e técnica avançada."
      },
      {
        "name": "Mermas Genéricas",
        "category": "Ferramentas e Utilidades",
        "description": "Quebras em presunto, anchova, marisco e enchidos."
      },
      {
        "name": "ID Alergénios",
        "category": "Ferramentas e Utilidades",
        "description": "Identificação por tapa: glúten, lacticínios, mariscos, sulfitos."
      },
      {
        "name": "GastroIMG Gen+",
        "category": "Conhecimento Gastro",
        "description": "Fotografia artesanal espanhola IA de referência."
      },
      {
        "name": "InstaFlow AI Pro",
        "category": "Conteúdos e Redes Sociais",
        "description": "Instagram para captar locais e turistas."
      },
      {
        "name": "MenuDish Local SEO",
        "category": "Conteúdos e Redes Sociais",
        "description": "Captar clientes que procuram \"tapas perto\"."
      },
      {
        "name": "Gastro Calendar",
        "category": "Conteúdos e Redes Sociais",
        "description": "Dia da Tapa, São Firmino, festas locais."
      }
    ],
    "metrics": [
      {
        "value": "+5 pp",
        "label": "margem após custear tapas"
      },
      {
        "value": "+15 %",
        "label": "ticket médio em 4 meses"
      },
      {
        "value": "×2",
        "label": "captação local com MenuDish"
      },
      {
        "value": "12+",
        "label": "agentes para o seu gastrobar"
      }
    ],
    "beforeAfter": {
      "beforeTitle": "Sem AI Chef Pro",
      "beforeItems": [
        "Tapas de assinatura improvisadas sem ficha de custos",
        "Maridagens com vinhos sem base científica",
        "Quebras em presunto e produto fresco sem rastreabilidade",
        "Instagram improvisado",
        "Captação local sem SEO"
      ],
      "afterTitle": "Com AI Chef Pro",
      "afterItems": [
        "Tapas de assinatura com ficha de custos profissional",
        "Maridagens com Bar & Lounge AI+ e Food Pairing AI",
        "Quebras controladas com Mermas Genéricas",
        "GastroIMG Gen+ + InstaFlow artesanal",
        "MenuDish Local SEO captura \"tapas perto\""
      ]
    },
    "galleryTitle": "Como Funciona um Gastrobar",
    "gallerySubtitle": "O que vai coordenar com AI Chef Pro: tapas, vermute, presunto, vinhos e equipa. Imagens geradas com IA como referência visual do conceito.",
    "galleryImages": [
      "/lovable-uploads/ai-gallery/use-case-gastrobar-hero.jpg",
      "/lovable-uploads/ai-gallery/use-case-gastrobar-tapas.jpg",
      "/lovable-uploads/ai-gallery/use-case-gastrobar-vermut.jpg",
      "/lovable-uploads/ai-gallery/use-case-gastrobar-jamon.jpg",
      "/lovable-uploads/ai-gallery/use-case-gastrobar-vinos.jpg",
      "/lovable-uploads/ai-gallery/use-case-gastrobar-team.jpg"
    ]
  },
  "food-truck": {
    "h1": "IA para Food Truck",
    "heroSubtitle": "Desenhe uma ementa compacta com escandallo rigoroso, gerencie a preparação ajustada ao espaço limitado, planeie eventos e rotas e capture branding viral com uma suite de agentes de IA gastronómica especializados em food truck profissional.",
    "heroTagline": "Food truck com margem real e operação ajustada",
    "badge": "Para food trucks, cozinhas móveis e street food",
    "painsTitle": "O Que um Food Truck Não Pode Deixar de Resolver",
    "pains": [
      "Ementa compacta e curada (5-10 pratos máx) com custo otimizado por processo eficiente",
      "Espaço limitado: preparação ajustada, mise compacta, equipamentos partilhados, armazenamento mínimo",
      "Mermas controladas em produto fresco com compra ajustada ao volume do evento",
      "Padronizar técnica turno a turno com pessoal rotativo e equipas em mudança",
      "Diferenciar-se com branding visual icónico, redes sociais ativas e storytelling de hand-painted",
      "Planear rotas de eventos (festivais, feiras, mercados, eventos privados) com margem alta"
    ],
    "featuresTitle": "Como AI Chef Pro Ajuda num Food Truck",
    "features": [
      {
        "icon": "Truck",
        "title": "Food Truck AI+",
        "description": "Agente especializado em food trucks e cozinhas móveis: operação, preparação, eventos, branding e rotas."
      },
      {
        "icon": "Sparkles",
        "title": "Culinária Criativa",
        "description": "Para signatures de food truck: smash burgers, baos, tacos, frangos crocantes com escandallo profissional."
      },
      {
        "icon": "Calculator",
        "title": "Escandallos por prato",
        "description": "Culinária Criativa entrega receita + escandallo CSV; Kit de Escandallos Pro gere-o com custo real ajustado à operação móvel."
      },
      {
        "icon": "CheckSquare",
        "title": "Kit de Tareas Restaurante Casual",
        "description": "Modelos: pré-evento, preparação ajustada, montagem, serviço rápido, encerramento, reposição."
      },
      {
        "icon": "ShieldCheck",
        "title": "Pack APPCC food truck",
        "description": "Rastreabilidade adaptada à operação móvel: temperaturas, água, resíduos."
      },
      {
        "icon": "Calendar",
        "title": "Gastro Calendar",
        "description": "Festivais, feiras, mercados, eventos corporativos privados."
      },
      {
        "icon": "Image",
        "title": "GastroIMG Gen+ + InstaFlow AI Pro",
        "description": "Fotografia street food viral IA + Instagram com calendário editorial ativo."
      },
      {
        "icon": "BarChart3",
        "title": "MenuDish Local SEO",
        "description": "Captar clientes que procuram \"food truck perto\" ou \"street food em [cidade]\"."
      },
      {
        "icon": "Sparkles",
        "title": "Mermas Genéricas",
        "description": "Mermas em produto fresco com compra ajustada ao volume do evento."
      }
    ],
    "workflowTitle": "Um Dia Real de um Food Truck com AI Chef Pro",
    "workflow": [
      "08:00 · Abertura — checklist Kit de Tareas: revisão de equipamentos, montagem de mise compacta, preparação ajustada ao volume do evento.",
      "10:00 · Food Truck AI+ — desenvolve um novo smash burger signature com queijo americano e bacon fumado. Receita + escandallo CSV.",
      "11:00 · Kit de Escandallos Pro — carrega CSV com preços reais e volume estimado do evento, valida margem.",
      "12:00 · Chegada ao evento (festival musical) — montagem, ligação elétrica, controlo APPCC.",
      "13:00 · Serviço de meio-dia — pico forte com filas controladas, preparação eficiente.",
      "17:00 · Pausa — reposição de stock, controlo de mermas e caixa do primeiro serviço.",
      "20:00 · Serviço de noite — pico maior, GastroIMG Gen+ já tem foto do dia programada no Instagram.",
      "00:00 · Encerramento — limpeza, APPCC assinado, planeamento do próximo evento com Gastro Calendar."
    ],
    "productsTitle": "Modelos e Kits Recomendados para Food Truck",
    "productIds": [
      "kit-tareas",
      "kit-escandallos",
      "pack-appcc",
      "kit-inventario",
      "kit-gestion-personal",
      "pro-prompts-ebook"
    ],
    "testimonialQuote": "Food Truck AI+ + Culinária Criativa mudaram a nossa operação. A ementa é mais compacta, os escandallos por prato refletem margem real com compra ajustada ao volume do evento, e a captação com InstaFlow + GastroIMG triplicou as nossas reservas para eventos privados em 6 meses.",
    "testimonialAuthor": "Marcos Bermúdez",
    "testimonialRole": "Proprietário, food truck artesanal",
    "faqTitle": "Perguntas Frequentes de Food Trucks",
    "faqs": [
      {
        "q": "Serve para food truck casual, gourmet ou cozinha móvel para eventos privados?",
        "a": "Para os três. Food Truck AI+ cobre desde casual até gourmet, passando por cozinha móvel para casamentos e eventos corporativos."
      },
      {
        "q": "Como escandallar com compra ajustada ao evento?",
        "a": "Kit de Escandallos Pro recalcula instantaneamente a margem conforme o volume estimado do evento."
      },
      {
        "q": "Cobre operação móvel com espaço limitado?",
        "a": "Sim. Food Truck AI+ raciocina como operador profissional: preparação compacta, mise eficiente, equipamentos partilhados."
      },
      {
        "q": "Gera conteúdo viral para Instagram e TikTok?",
        "a": "Sim. GastroIMG Gen+ + InstaFlow AI Pro geram conteúdo viral com calendário editorial ativo. Lembre-se que a imagem IA é de referência visual: a foto definitiva é feita por si com o seu prato real."
      },
      {
        "q": "Como me ajuda com eventos e rotas?",
        "a": "Gastro Calendar planeia festivais, feiras, mercados e eventos privados com planeamento de rotas."
      }
    ],
    "ctaTitle": "O seu food truck com margem real e operação ajustada.",
    "ctaSubtitle": "Comece com o onboarding de 2 minutos. Plano Membro por 10 € por mês com 10.000 créditos.",
    "seo": {
      "title": "IA para Food Truck: Ementa, Escandallos e Eventos | AI Chef Pro",
      "description": "Suite de IA para food trucks: Food Truck AI+, escandallos por prato, planeamento de eventos, branding viral e APPCC. Comece hoje.",
      "keywords": "IA food truck, software food truck, escandallos food truck, street food IA, cozinha móvel, eventos food truck",
      "ogImage": "https://aichef.pro/og/use-cases/food-truck.jpg"
    },
    "personalizationTitle": "Personalizado ao Seu Food Truck desde o Primeiro Minuto",
    "personalizationBody": "AI Chef Pro arranca com o agente «Quem Sou Eu?», um onboarding de 2 minutos em que lhe conta que tipo de food truck opera (casual, gourmet, eventos privados, mercado, festivais), tamanho da equipa, especialidade e zonas de operação.",
    "appsTitle": "Os Agentes de IA que Vai Usar no Seu Food Truck",
    "apps": [
      {
        "name": "Food Truck AI+",
        "category": "Conceitos de Negócio",
        "description": "Agente especializado em food trucks e cozinhas móveis."
      },
      {
        "name": "Burger Pro AI+",
        "category": "Conceitos de Negócio",
        "description": "Para food trucks de smash burgers e hamburgueria gourmet."
      },
      {
        "name": "Culinária Criativa",
        "category": "Criatividade Culinária",
        "description": "Signatures com receita + escandallo CSV."
      },
      {
        "name": "Restaurantes Casuais AI+",
        "category": "Conceitos de Negócio",
        "description": "Aconselhamento operacional casual."
      },
      {
        "name": "Mermas Genéricas",
        "category": "Ferramentas e Utilitários",
        "description": "Mermas com compra ajustada ao evento."
      },
      {
        "name": "ID Alergénios",
        "category": "Ferramentas e Utilitários",
        "description": "Identificação automática por prato."
      },
      {
        "name": "GastroIMG Gen+",
        "category": "Gastro Conhecimento",
        "description": "Fotografia street food viral IA de referência."
      },
      {
        "name": "InstaFlow AI Pro",
        "category": "Conteúdos e Redes Sociais",
        "description": "Instagram com calendário editorial ativo."
      },
      {
        "name": "MenuDish Local SEO",
        "category": "Conteúdos e Redes Sociais",
        "description": "Captar clientes que procuram \"food truck perto\"."
      },
      {
        "name": "Gastro Calendar",
        "category": "Conteúdos e Redes Sociais",
        "description": "Festivais, feiras, mercados, eventos privados."
      },
      {
        "name": "Gerador de Pins Pinterest",
        "category": "Conteúdos e Redes Sociais",
        "description": "Pinterest captura tráfego para street food."
      },
      {
        "name": "Coach Mental",
        "category": "Ferramentas e Utilitários",
        "description": "Coaching para gestão de stress em eventos massivos."
      }
    ],
    "metrics": [
      {
        "value": "+5 pp",
        "label": "margem após escandallar ementa"
      },
      {
        "value": "×3",
        "label": "reservas eventos privados em 6 meses"
      },
      {
        "value": "−20 %",
        "label": "mermas com compra ajustada"
      },
      {
        "value": "12+",
        "label": "agentes para o seu food truck"
      }
    ],
    "beforeAfter": {
      "beforeTitle": "Sem AI Chef Pro",
      "beforeItems": [
        "Ementa extensa com food cost incerto",
        "Compra de produto sem ajuste ao volume do evento",
        "Mermas elevadas em produto fresco",
        "Instagram improvisado, sem conteúdo viral",
        "Eventos privados fechados à mão"
      ],
      "afterTitle": "Com AI Chef Pro",
      "afterItems": [
        "Ementa compacta com escandallo profissional",
        "Compra ajustada ao volume estimado do evento",
        "Mermas controladas com Mermas Genéricas",
        "GastroIMG Gen+ + InstaFlow conteúdo viral",
        "Eventos privados fechados com proposta profissional"
      ]
    },
    "galleryTitle": "Como Funciona um Food Truck",
    "gallerySubtitle": "O que vai coordenar com AI Chef Pro: truck, preparação, chapa, serviço e equipa. Imagens geradas com IA como referência visual do conceito.",
    "galleryImages": [
      "/lovable-uploads/ai-gallery/use-case-food-truck-hero.jpg",
      "/lovable-uploads/ai-gallery/use-case-food-truck-counter.jpg",
      "/lovable-uploads/ai-gallery/use-case-food-truck-grill.jpg",
      "/lovable-uploads/ai-gallery/use-case-food-truck-prep.jpg",
      "/lovable-uploads/ai-gallery/use-case-food-truck-line.jpg",
      "/lovable-uploads/ai-gallery/use-case-food-truck-team.jpg"
    ]
  },
  "restaurante-italiano": {
    "h1": "IA para Restaurante Italiano",
    "heroSubtitle": "Domine técnica italiana autêntica com escandallo rigoroso por prato, gere massa fresca e molhos tradicionais, desenhe cartas sazonais e capture branding de trattoria com uma suite de agentes de IA gastronómica especializados em cozinha italiana profissional.",
    "heroTagline": "Cozinha italiana com técnica autêntica e margem real",
    "badge": "Para trattorias, ristoranti e restaurantes italianos",
    "painsTitle": "O Que um Restaurante Italiano Não Pode Deixar de Resolver",
    "pains": [
      "Massa fresca diária com equilíbrio preciso de sêmola, ovo e água, técnica de extrusão e formatos regionais",
      "Molhos tradicionais (ragú, carbonara, cacio e pepe, pesto) que requerem consistência técnica turno a turno",
      "Perdas em massa fresca, queijo, enchidos italianos (mortadella, prosciutto), tomate San Marzano",
      "Padronizar pratos signature regionais (Roma, Toscana, Emília, Sicília) com técnica autêntica",
      "Diferenciar-se em zona competitiva com produto italiano importado, branding de trattoria e storytelling regional",
      "Captar pedidos de eventos privados, jantares corporativos e casamentos italianos com margem alta"
    ],
    "featuresTitle": "Como o AI Chef Pro Ajuda num Restaurante Italiano",
    "features": [
      {
        "icon": "UtensilsCrossed",
        "title": "Cozinha Italiana",
        "description": "Agente especializado em cozinha italiana autêntica: massa, molhos, risotto, ossobuco, técnica regional."
      },
      {
        "icon": "Beaker",
        "title": "Fermentus Con AI+",
        "description": "Para massas mãe italianas (focaccia, pane casareccio, pizza alla pala) e técnica de fermentação."
      },
      {
        "icon": "Sparkles",
        "title": "Culinária Criativa",
        "description": "Para pratos signature contemporâneos e degustação com base italiana autêntica."
      },
      {
        "icon": "Wine",
        "title": "Bar & Lounge AI+",
        "description": "Vinhos italianos por copa e harmonizações com cozinha regional (Chianti, Barolo, Amarone, Prosecco)."
      },
      {
        "icon": "Calculator",
        "title": "Escandallos por prato",
        "description": "Cozinha Italiana entrega receita + escandallo CSV; Kit de Escandallos Pro gere com custo real por prato e food cost %."
      },
      {
        "icon": "CheckSquare",
        "title": "Kit de Tareas Restaurante Casual",
        "description": "Modelos: preparação de massa fresca, molhos tradicionais, mise pizza, serviço, encerramento."
      },
      {
        "icon": "ShieldCheck",
        "title": "Pack APPCC italiano",
        "description": "Rastreabilidade de massa fresca, queijos italianos, enchidos e molhos."
      },
      {
        "icon": "Calendar",
        "title": "Gastro Calendar",
        "description": "Festividades italianas (Ferragosto, Carnevale, Pasqua, Natale), eventos privados e casamentos italianos."
      },
      {
        "icon": "Image",
        "title": "GastroIMG Gen+ + InstaFlow AI Pro",
        "description": "Fotografia editorial de trattoria IA + Instagram com storytelling regional."
      }
    ],
    "workflowTitle": "Um Dia Real num Restaurante Italiano com AI Chef Pro",
    "workflow": [
      "08:00 · Abertura — checklist Kit de Tareas: preparação de massa fresca diária (tagliatelle, ravioli, pappardelle), preparação de molhos tradicionais.",
      "10:00 · Cozinha Italiana — desenvolve um novo prato signature de tagliolini al limone com scampi da pesca do dia. Receita + escandallo CSV.",
      "11:00 · Kit de Escandallos Pro — carrega CSV com preços reais de scampi e produto italiano, valida margem e food cost %.",
      "12:00 · Bar & Lounge AI+ — valida a harmonização com um Vermentino di Sardegna.",
      "13:00 · Serviço de meio-dia — pico com massa fresca, molhos tradicionais e vinhos italianos por copa.",
      "17:00 · Briefing à equipa — explicação do novo prato e harmonizações.",
      "19:00 · Serviço de jantar — picos coordenados com cozinha principal.",
      "22:00 · GastroIMG Gen+ + InstaFlow AI Pro — gera imagem editorial de trattoria e posts."
    ],
    "productsTitle": "Modelos e Kits Recomendados para Restaurante Italiano",
    "productIds": [
      "kit-tareas",
      "kit-escandallos",
      "pack-appcc",
      "kit-inventario",
      "kit-gestion-personal",
      "pro-prompts-ebook"
    ],
    "testimonialQuote": "Cozinha Italiana + Bar & Lounge AI+ mudaram o nosso restaurante. Massa fresca consistente, molhos tradicionais com equilíbrio técnico, harmonizações com vinhos italianos por copa documentadas. Subimos a margem 5 pontos e os clientes recorrentes cresceram 30 % em 6 meses.",
    "testimonialAuthor": "Lorenzo Bianchi",
    "testimonialRole": "Chef e proprietário, trattoria contemporânea",
    "faqTitle": "Perguntas Frequentes de Restaurantes Italianos",
    "faqs": [
      {
        "q": "Serve para trattoria casual, ristorante contemporâneo ou cozinha regional italiana?",
        "a": "Para os três. Cozinha Italiana cobre desde trattoria tradicional até alta cozinha italiana de autor com técnica regional autêntica."
      },
      {
        "q": "Cobre massa fresca e molhos tradicionais?",
        "a": "Sim. Cozinha Italiana raciocina como cozinheiro italiano profissional: equilíbrio de massa, formatos regionais, técnica de molhos tradicionais."
      },
      {
        "q": "Cobre vinhos italianos e harmonizações?",
        "a": "Sim. Bar & Lounge AI+ cobre Chianti, Barolo, Amarone, Prosecco e harmonizações com cozinha regional."
      },
      {
        "q": "Gera conteúdo visual para Instagram?",
        "a": "Sim. GastroIMG Gen+ gera imagens editoriais de trattoria. Lembre-se de que a imagem IA é de referência visual: a foto definitiva é feita por si com o seu prato real."
      },
      {
        "q": "Como me ajuda com eventos e festividades italianas?",
        "a": "Gastro Calendar planifica Ferragosto, Carnevale, Pasqua, Natale e eventos privados com menus italianos."
      }
    ],
    "ctaTitle": "O seu restaurante italiano com técnica autêntica e margem real.",
    "ctaSubtitle": "Comece com o onboarding de 2 minutos. Plano Membro por 10 € por mês com 10.000 créditos.",
    "seo": {
      "title": "IA para Restaurante Italiano: Massa, Escandallos e Vinhos | AI Chef Pro",
      "description": "Suite de IA para restaurantes italianos: Cozinha Italiana, escandallos, massa fresca, vinhos italianos e branding de trattoria. Comece hoje.",
      "keywords": "IA restaurante italiano, software trattoria, escandallos massa, cozinha italiana IA, vinhos italianos, ristorante contemporâneo",
      "ogImage": "https://aichef.pro/og/use-cases/restaurante-italiano.jpg"
    },
    "personalizationTitle": "Personalizado para o Seu Restaurante Italiano desde o Minuto Um",
    "personalizationBody": "AI Chef Pro arranca com o agente «Quem Sou Eu?», um onboarding de 2 minutos em que lhe conta que tipo de italiano opera (trattoria, ristorante contemporâneo, cozinha regional, italiano de autor), tamanho da equipa, cidade e especialidade regional.",
    "appsTitle": "Os Agentes de IA que Vai Usar no Seu Restaurante Italiano",
    "apps": [
      {
        "name": "Cozinha Italiana",
        "category": "Receituários da Europa",
        "description": "Massa, molhos, risotto, ossobuco com técnica regional autêntica."
      },
      {
        "name": "Culinária Criativa",
        "category": "Criatividade Culinária",
        "description": "Pratos signature contemporâneos italianos."
      },
      {
        "name": "Fermentus Con AI+",
        "category": "Criatividade Culinária",
        "description": "Massas mãe italianas (focaccia, pane casareccio)."
      },
      {
        "name": "Bar & Lounge AI+",
        "category": "Conceitos de Negócio",
        "description": "Vinhos italianos e harmonizações regionais."
      },
      {
        "name": "Food Pairing AI",
        "category": "Criatividade Culinária",
        "description": "Harmonizações com técnica autêntica italiana."
      },
      {
        "name": "Sosa Ingredients",
        "category": "Fornecedores Gastro",
        "description": "Catálogo Sosa para texturas e técnica avançada."
      },
      {
        "name": "Mermas Genéricas",
        "category": "Ferramentas e Utilitários",
        "description": "Perdas em massa fresca, queijo, enchidos."
      },
      {
        "name": "ID Alergénios",
        "category": "Ferramentas e Utilitários",
        "description": "Identificação por prato."
      },
      {
        "name": "GastroIMG Gen+",
        "category": "Conhecimento Gastro",
        "description": "Fotografia editorial de trattoria IA de referência."
      },
      {
        "name": "InstaFlow AI Pro",
        "category": "Conteúdos e Redes Sociais",
        "description": "Instagram com calendário editorial italiano."
      },
      {
        "name": "MenuDish Local SEO",
        "category": "Conteúdos e Redes Sociais",
        "description": "Captar clientes que procuram \"italiano perto\"."
      },
      {
        "name": "Gastro Calendar",
        "category": "Conteúdos e Redes Sociais",
        "description": "Festividades italianas e eventos privados."
      }
    ],
    "metrics": [
      {
        "value": "+5 pp",
        "label": "margem após escandallar pratos"
      },
      {
        "value": "+30 %",
        "label": "clientes recorrentes em 6 meses"
      },
      {
        "value": "−20 %",
        "label": "perdas em massa e enchidos"
      },
      {
        "value": "12+",
        "label": "agentes para a sua trattoria"
      }
    ],
    "beforeAfter": {
      "beforeTitle": "Sem AI Chef Pro",
      "beforeItems": [
        "Massa fresca improvisada, equilíbrio variável",
        "Molhos tradicionais sem consistência técnica",
        "Harmonizações com vinhos italianos sem base profissional",
        "Perdas em produto italiano importado sem rastreabilidade",
        "Instagram sem storytelling regional"
      ],
      "afterTitle": "Com AI Chef Pro",
      "afterItems": [
        "Massa fresca com equilíbrio técnico documentado",
        "Molhos tradicionais consistentes com critério profissional",
        "Harmonizações com Bar & Lounge AI+ documentadas",
        "Perdas controladas com Mermas Genéricas",
        "GastroIMG Gen+ + InstaFlow editorial de trattoria"
      ]
    },
    "galleryTitle": "Como Funciona um Restaurante Italiano",
    "gallerySubtitle": "O que vai coordenar com AI Chef Pro: massa fresca, pratos, cozinha, vinhos e equipa. Imagens geradas com IA como referência visual do conceito.",
    "galleryImages": [
      "/lovable-uploads/ai-gallery/use-case-italiano-hero.jpg",
      "/lovable-uploads/ai-gallery/use-case-italiano-pasta.jpg",
      "/lovable-uploads/ai-gallery/use-case-italiano-platos.jpg",
      "/lovable-uploads/ai-gallery/use-case-italiano-cocina.jpg",
      "/lovable-uploads/ai-gallery/use-case-italiano-vinos.jpg",
      "/lovable-uploads/ai-gallery/use-case-italiano-team.jpg"
    ]
  },
  "task-escandallos-con-ia": {
    "h1": "Como Fazer Escandallos com IA",
    "heroSubtitle": "Calcule o custo real por prato, food cost % e preço sugerido em minutos em vez de dias: receita + escandallo CSV automático com custo hora de obrador, mermas integradas e margem validada em tempo real com uma suite de agentes de IA gastronómica.",
    "heroTagline": "Escandallos profissionais em minutos, não em horas",
    "badge": "Tarefa: Escandallos e costing",
    "painsTitle": "O Que Custa Escandallar à Mão",
    "pains": [
      "Uma semana de calculadora e guardanapos para escandallar uma nova carta de 30 pratos",
      "Sem custo hora de obrador integrado, pratos complexos em perda sem saber",
      "Mermas estimadas a olho (30 % em alguns cortes), não dados reais por processo",
      "Quando o preço do fornecedor muda, desequilibra tudo e não se atualiza",
      "Falta de critério para decidir food cost objetivo conforme o tipo de prato (signature, entrada, sobremesa)",
      "Sem rastreabilidade do cálculo: se lhe pedirem para auditar, não sabe de onde sai cada número"
    ],
    "featuresTitle": "Como a AI Chef Pro Resolve os Escandallos",
    "features": [
      {
        "icon": "Calculator",
        "title": "Culinária Criativa + escandallo CSV",
        "description": "Qualquer agente criativo (Culinária, Pastelaria, Gelataria, Chocolataria) entrega receita + escandallo CSV com balanço técnico e custo hora de obrador integrado."
      },
      {
        "icon": "BarChart3",
        "title": "Mermas Genéricas",
        "description": "Dados precisos de mermas por processo (desmancha, torrefação, abatimento, vitrina, formado) integrados automaticamente ao CSV."
      },
      {
        "icon": "Beaker",
        "title": "Sosa Ingredients",
        "description": "Catálogo Sosa com preços de referência para ingredientes técnicos profissionais."
      },
      {
        "icon": "Sparkles",
        "title": "Calcula Pax + Conversor Ing",
        "description": "Escala receitas para 2, 6, 12, 100 pax sem perder precisão; conversor automático de pesos e medidas."
      },
      {
        "icon": "CheckSquare",
        "title": "Kit de Escandallos Pro",
        "description": "Modelos Excel descarregáveis que recebem o CSV e calculam margem real, food cost % e preço sugerido instantaneamente."
      },
      {
        "icon": "BookOpen",
        "title": "Fichas Técnicas com Custo",
        "description": "Cada receita entrega ficha técnica completa com custo, alergénios, técnica e storytelling para sala."
      },
      {
        "icon": "Image",
        "title": "GastroIMG Gen+",
        "description": "Imagem de referência gerada com IA do prato escandallado para visualizar antes de cozinhar (não a foto definitiva)."
      },
      {
        "icon": "BookOpen",
        "title": "Pro Prompts eBook",
        "description": "eBook com 300+ prompts profissionais para escandallar, validar e otimizar custos com IA gastronómica."
      },
      {
        "icon": "Wine",
        "title": "Aplicável a Qualquer Conceito",
        "description": "Restaurante, cafetaria, pastelaria, gelataria, chocolataria, pizzaria, bar, catering, hotel: o fluxo é o mesmo."
      }
    ],
    "workflowTitle": "Como Escandallar com IA em 4 Passos",
    "workflow": [
      "1. Culinária Criativa (ou o agente criativo do seu conceito: Pastelaria, Gelataria, Chocolataria, Cozinha Italiana, Cozinha Mexicana, Culinária Peruana, Cozinha Japonesa) — desenvolve ou carrega a receita. O agente IA entrega receita + escandallo CSV com balanço técnico, mermas estimadas e storytelling.",
      "2. Sosa Ingredients + Mermas Genéricas — a IA enriquece o CSV com preços de referência e mermas reais por processo do seu tipo de cozinha.",
      "3. Kit de Escandallos Pro (modelo Excel descarregável, €12) — carrega o CSV com os seus preços reais de fornecedores. O Excel calcula margem real, food cost %, preço sugerido por canal (sala, delivery, eventos) e proposta económica.",
      "4. Calcula Pax + Conversor Ing — se precisar de escalar a receita para banquetes (50, 100, 300 pax) ou converter unidades, os agentes IA fazem-no instantaneamente mantendo o escandallo."
    ],
    "productsTitle": "Modelos e Kits Recomendados para Escandallos",
    "productIds": [
      "kit-escandallos",
      "pro-prompts-ebook",
      "pack-appcc",
      "kit-inventario",
      "kit-tareas",
      "kit-plan-financiero"
    ],
    "testimonialQuote": "O que antes era uma semana de calculadora agora são 30 minutos. Culinária Criativa entrega o escandallo CSV, Mermas Genéricas enriquece-o com dados reais e o Kit de Escandallos Pro dá-me margem validada. Renovamos a carta de 28 pratos num só dia e subimos a margem 6 pontos ao descobrir pratos em perda que não sabíamos.",
    "testimonialAuthor": "Pablo Ruiz",
    "testimonialRole": "Chef e proprietário, restaurante casual com 4 pontos",
    "faqTitle": "Perguntas Frequentes sobre Escandallos com IA",
    "faqs": [
      {
        "q": "Serve para qualquer tipo de cozinha?",
        "a": "Sim. O fluxo é o mesmo para culinária criativa, pastelaria, gelataria, chocolataria, pizzaria, cozinha mexicana, culinária peruana, cozinha japonesa, cozinha italiana, plant-based ou qualquer conceito. Apenas muda o agente criativo de partida."
      },
      {
        "q": "Como gere o custo hora de obrador?",
        "a": "O CSV inclui um campo de tempo de elaboração por processo (mistura, formado, cozedura, decoração). O Kit de Escandallos Pro multiplica pelo seu custo hora real (salário + encargos) e integra-o na margem real."
      },
      {
        "q": "Como reflito preço variável de fornecedores (cacau, peixe, carne)?",
        "a": "O Kit de Escandallos Pro recalcula instantaneamente a margem quando atualiza preços. Mermas Genéricas adiciona o custo de mermas por processo. O prato reflete sempre o custo atual, não o de há três meses."
      },
      {
        "q": "Cobre escalado para banquetes e eventos?",
        "a": "Sim. O Calcula Pax escala receitas para qualquer número de comensais sem perder precisão; o Kit de Escandallos Pro recalcula custo por pessoa e proposta económica para o cliente corporativo."
      },
      {
        "q": "Gera imagem de referência do prato escandallado?",
        "a": "Sim. O GastroIMG Gen+ gera imagem de referência visual do prato. Lembre-se de que a imagem IA é de referência: a foto definitiva do escandallo é feita por si com o seu prato real empratado."
      }
    ],
    "ctaTitle": "Os seus escandallos em minutos com margem real validada.",
    "ctaSubtitle": "Comece com o onboarding de 2 minutos. Plano Membro por 10 € por mês com 10.000 créditos.",
    "seo": {
      "title": "Como Fazer Escandallos com IA: Custo Real, Margem e Food Cost | AI Chef Pro",
      "description": "Suite de IA para escandallos profissionais: receita + CSV com custo hora de obrador, mermas integradas, margem validada. Comece hoje.",
      "keywords": "escandallos com IA, calcular food cost, custo real prato, escandallo CSV, kit escandallos, food cost restaurante",
      "ogImage": "https://aichef.pro/og/use-cases/task-escandallos-con-ia.jpg"
    },
    "personalizationTitle": "Personalizado para a Sua Cozinha desde o Minuto Um",
    "personalizationBody": "A AI Chef Pro arranca com o agente «Quem Sou Eu?», um onboarding de 2 minutos em que você conta que tipo de cozinha trabalha e o fluxo de escandallos adapta-se ao seu conceito: Culinária Criativa para restaurante, Pastelaria Criativa para obrador, Gelataria Criativa para gelataria, etc.",
    "appsTitle": "Os Agentes IA que Usa para Escandallar",
    "apps": [
      {
        "name": "Culinária Criativa",
        "category": "Criatividade Culinária",
        "description": "Receitas + escandallo CSV com balanço técnico e mermas estimadas."
      },
      {
        "name": "Pastelaria Criativa",
        "category": "Criatividade Culinária",
        "description": "Receitas doces com custo hora de obrador integrado."
      },
      {
        "name": "Gelataria Criativa",
        "category": "Criatividade Culinária",
        "description": "Receitas com balanço técnico de açúcares, sólidos e gorduras."
      },
      {
        "name": "Chocolataria Criativa",
        "category": "Criatividade Culinária",
        "description": "Receitas com coberturas, ganaches e técnica de temperagem."
      },
      {
        "name": "Mermas Genéricas",
        "category": "Ferramentas e Utilitários",
        "description": "Dados precisos de mermas por processo integrados ao escandallo."
      },
      {
        "name": "Calcula Pax",
        "category": "Ferramentas e Utilitários",
        "description": "Escalado de receitas para qualquer número de comensais."
      },
      {
        "name": "Conversor Ing",
        "category": "Ferramentas e Utilitários",
        "description": "Conversor automático de pesos e medidas."
      },
      {
        "name": "ID Alergénios",
        "category": "Ferramentas e Utilitários",
        "description": "Identificação automática de alergénios por ingrediente."
      },
      {
        "name": "Sosa Ingredients",
        "category": "Fornecedores Gastro",
        "description": "Preços de referência e técnica com catálogo Sosa."
      },
      {
        "name": "tSpoonLab Agent",
        "category": "Fornecedores Gastro",
        "description": "Preços e técnica com catálogo tSpoonLab."
      },
      {
        "name": "GastroIMG Gen+",
        "category": "Conhecimento Gastro",
        "description": "Imagem de referência do prato escandallado."
      },
      {
        "name": "Sonar Deep Research",
        "category": "Modelos IA + LLM",
        "description": "Pesquisa profunda de fornecedores e preços de mercado."
      }
    ],
    "metrics": [
      {
        "value": "×30",
        "label": "velocidade vs. calculadora manual"
      },
      {
        "value": "+6 pp",
        "label": "margem após escandallar a carta"
      },
      {
        "value": "−25 %",
        "label": "mermas com dados reais"
      },
      {
        "value": "12+",
        "label": "agentes para escandallar"
      }
    ],
    "beforeAfter": {
      "beforeTitle": "Sem AI Chef Pro",
      "beforeItems": [
        "Uma semana por carta nova de 30 pratos",
        "Sem custo hora de obrador, pratos complexos em perda",
        "Mermas estimadas a olho, não dados reais",
        "Preços de fornecedor alterados sem atualizar margem",
        "Sem rastreabilidade do cálculo"
      ],
      "afterTitle": "Com AI Chef Pro",
      "afterItems": [
        "Uma carta nova de 30 pratos escandallada num dia",
        "Custo hora de obrador integrado automaticamente",
        "Mermas reais com Mermas Genéricas e modelos",
        "Preços atualizáveis: margem recalcula instantaneamente",
        "CSV rastreável + ficha técnica com custo para auditoria"
      ]
    },
    "galleryTitle": "Como Funciona o Fluxo de Escandallos com IA",
    "gallerySubtitle": "O que vai coordenar com AI Chef Pro: receita, CSV, mermas, receituário digital e equipa. Imagens geradas com IA como referência visual do conceito.",
    "galleryImages": [
      "/lovable-uploads/ai-gallery/use-case-task-escandallos-hero.jpg",
      "/lovable-uploads/ai-gallery/use-case-task-escandallos-csv.jpg",
      "/lovable-uploads/ai-gallery/use-case-task-escandallos-recipe.jpg",
      "/lovable-uploads/ai-gallery/use-case-task-escandallos-merma.jpg",
      "/lovable-uploads/ai-gallery/use-case-task-escandallos-mise.jpg",
      "/lovable-uploads/ai-gallery/use-case-task-escandallos-team.jpg"
    ]
  },
  "task-menu-degustacion-con-ia": {
    "h1": "Como Desenhar um Menu de Degustação com IA",
    "heroSubtitle": "Desenha menus de degustação com sequência coerente, ficha de custos total validada, harmonizações científicas e storytelling para a sala com uma suite de agentes de IA gastronómica especializados em alta cozinha.",
    "heroTagline": "Menu de degustação profissional em horas, não em semanas",
    "badge": "Tarefa: Menu de degustação",
    "painsTitle": "O Que Custa Desenhar um Menu de Degustação à Mão",
    "pains": [
      "Uma semana de iterações para uma sequência de 7-10 passos coerente sem saturação",
      "Sem ficha de custos total validada por menu, proposta a preço incerto",
      "Harmonizações com vinho propostas sem base científica fundamentada",
      "Storytelling de cada passo improvisado, equipa de sala sem formação constante",
      "Mudanças de passo exigem refazer a ficha de custos completa à mão",
      "Falta de critério para equilibrar textura, temperatura, intensidade e técnica entre passos"
    ],
    "featuresTitle": "Como o AI Chef Pro Resolve o Menu de Degustação",
    "features": [
      {
        "icon": "Sparkles",
        "title": "Culinária Criativa com sequência técnica",
        "description": "Raciocina a sequência completa: entrada ligeira, vegetal, peixe, carne, palate cleanser, sobremesa. Equilíbrio de textura, temperatura e intensidade."
      },
      {
        "icon": "Wine",
        "title": "Food Pairing AI",
        "description": "Harmonizações com base científica para cada passo: análise de acidez, taninos, estrutura, intensidade e harmonia com a cozinha."
      },
      {
        "icon": "Calculator",
        "title": "Ficha de custos total integrada",
        "description": "CSV com ficha de custos de cada passo + total do menu; o Kit de Escandallos Pro valida o custo por pax e a proposta de preço."
      },
      {
        "icon": "BookOpen",
        "title": "Storytelling para a sala",
        "description": "Descrição de cada passo com técnica, produto, fornecedor e história; a equipa de sala recita-o com profissionalismo."
      },
      {
        "icon": "Sparkles",
        "title": "Bar & Lounge AI+",
        "description": "Seleção de vinhos por copa para a harmonização do menu de degustação com critério de sommelier profissional."
      },
      {
        "icon": "CheckSquare",
        "title": "Kit de Tareas Restaurante",
        "description": "Modelos para a mise de cada passo, sequência de serviço e coordenação com a sala."
      },
      {
        "icon": "Image",
        "title": "GastroIMG Gen+",
        "description": "Imagem de referência de cada passo para visualizar a sequência antes de provar e validar a coerência visual."
      },
      {
        "icon": "Calendar",
        "title": "Gastro Calendar",
        "description": "Menus de degustação sazonais e eventos privados com planeamento profissional."
      },
      {
        "icon": "BarChart3",
        "title": "Calcula Pax",
        "description": "Escalonamento de receitas para banquetes e eventos privados sem perder precisão."
      }
    ],
    "workflowTitle": "Como Desenhar um Menu de Degustação em 5 Passos",
    "workflow": [
      "1. Culinária Criativa — define o tema (estação, produto local, ocasião) e o agente de IA entrega uma sequência de 7-10 passos com equilíbrio técnico (textura, intensidade, temperatura).",
      "2. Cada passo com receita + ficha de custos CSV individual + storytelling para a sala com técnica, produto e fornecedor.",
      "3. Food Pairing AI — para cada passo valida a harmonização com vinho ou sake com base científica. O Bar & Lounge AI+ propõe uma seleção concreta de adega.",
      "4. Kit de Escandallos Pro — carrega os CSVs individuais, o Excel calcula o custo total por pax, proposta de preço e margem validada.",
      "5. Calcula Pax — se o menu é para evento privado ou banquete (50, 100, 300 pax), escala as receitas e recalcula o custo para a proposta comercial."
    ],
    "productsTitle": "Modelos e Kits Recomendados para Menu de Degustação",
    "productIds": [
      "kit-escandallos",
      "pro-prompts-ebook",
      "pack-appcc",
      "guia-restaurante-gastronomico",
      "kit-tareas",
      "kit-plan-financiero"
    ],
    "testimonialQuote": "Culinária Criativa + Food Pairing AI mudaram-nos o desenvolvimento de menus de degustação. A sequência de 9 passos sai já com equilíbrio técnico documentado, as harmonizações com vinhos por copa são consistentes e a ficha de custos total com o Kit de Escandallos Pro dá-nos margem validada. O que antes era uma semana é agora um dia.",
    "testimonialAuthor": "Joan Mestre",
    "testimonialRole": "Chef executivo, restaurante com 1 estrela Michelin",
    "faqTitle": "Perguntas Frequentes sobre Menu de Degustação com IA",
    "faqs": [
      {
        "q": "Serve para Michelin, restaurante de autor ou casual com menu de degustação?",
        "a": "Para os três. A Culinária Criativa raciocina como um chef profissional: equilíbrio técnico, sequência coerente, narrativa do menu adaptada ao nível."
      },
      {
        "q": "Como me ajuda com a coerência entre passos?",
        "a": "A Culinária Criativa raciocina a sequência completa com equilíbrio de textura (crocante, sedoso, cremoso), temperatura (frio, ambiente, quente), intensidade (suave a potente) e técnica (cozedura, fermentação, fumo)."
      },
      {
        "q": "Cobre harmonizações com vinhos por copa para o menu?",
        "a": "Sim. O Food Pairing AI valida cada harmonização com base científica; o Bar & Lounge AI+ propõe uma seleção concreta de adega e storytelling para a sala."
      },
      {
        "q": "Gera imagem de referência de cada passo?",
        "a": "Sim. O GastroIMG Gen+ gera uma imagem de referência para visualizar a coerência visual do menu. Lembre-se de que a imagem IA é de referência visual: a foto definitiva é feita por si com o seu prato empratado real."
      },
      {
        "q": "Escalável para banquetes e eventos privados?",
        "a": "Sim. O Calcula Pax escala o menu para qualquer número de comensais; o Kit de Escandallos Pro recalcula o custo por pax e a proposta económica ao cliente."
      }
    ],
    "ctaTitle": "O seu menu de degustação profissional em horas, não em semanas.",
    "ctaSubtitle": "Comece com o onboarding de 2 minutos. Plano Membro por 10 € por mês com 10.000 créditos.",
    "seo": {
      "title": "Como Desenhar um Menu de Degustação com IA: Sequência, Ficha de Custos e Harmonizações | AI Chef Pro",
      "description": "Suite de IA para menu de degustação: sequência técnica, ficha de custos total, harmonizações científicas e storytelling. Comece hoje.",
      "keywords": "menu de degustação IA, desenhar menu de degustação, sequência de passos, harmonizações de menu, ficha de custos de menu de degustação, alta cozinha IA",
      "ogImage": "https://aichef.pro/og/use-cases/task-menu-degustacion-con-ia.jpg"
    },
    "personalizationTitle": "Personalizado para o Seu Restaurante desde o Primeiro Minuto",
    "personalizationBody": "O AI Chef Pro arranca com «Quem Sou Eu?»: conta o tipo de restaurante (gastronómico Michelin, fine dining, casual com menu de degustação, restaurante de autor), número de passos preferido, mercado e estilo de cozinha. Cada agente responde adaptado ao seu nível.",
    "appsTitle": "Os Agentes de IA que Usa para Menu de Degustação",
    "apps": [
      {
        "name": "Culinária Criativa",
        "category": "Criatividade Culinária",
        "description": "Raciocina a sequência técnica do menu de degustação com equilíbrio."
      },
      {
        "name": "Food Pairing AI",
        "category": "Criatividade Culinária",
        "description": "Harmonizações com base científica para cada passo."
      },
      {
        "name": "Bar & Lounge AI+",
        "category": "Conceitos de Negócio",
        "description": "Seleção de vinhos por copa com critério de sommelier."
      },
      {
        "name": "Pastelaria Criativa",
        "category": "Criatividade Culinária",
        "description": "Para sobremesas e palate cleanser do menu."
      },
      {
        "name": "Sosa Ingredients",
        "category": "Fornecedores Gastro",
        "description": "Catálogo Sosa para texturas e técnica avançada."
      },
      {
        "name": "tSpoonLab Agent",
        "category": "Fornecedores Gastro",
        "description": "Catálogo tSpoonLab para aplicações avançadas."
      },
      {
        "name": "Mermas Genéricas",
        "category": "Ferramentas e Utilitários",
        "description": "Mermas por passo integradas na ficha de custos total."
      },
      {
        "name": "Calcula Pax",
        "category": "Ferramentas e Utilitários",
        "description": "Escalonamento para banquetes e eventos privados."
      },
      {
        "name": "ID Alergénios",
        "category": "Ferramentas e Utilitários",
        "description": "Identificação de alergénios por passo para a sala."
      },
      {
        "name": "GastroIMG Gen+",
        "category": "Conhecimento Gastro",
        "description": "Imagem de referência de cada passo do menu."
      },
      {
        "name": "Gastro Calendar",
        "category": "Conteúdos e Redes Sociais",
        "description": "Menus de degustação sazonais e eventos privados."
      },
      {
        "name": "Coach Mental",
        "category": "Ferramentas e Utilitários",
        "description": "Coaching para liderança e gestão de serviço de degustação."
      }
    ],
    "metrics": [
      {
        "value": "×7",
        "label": "velocidade vs. processo manual"
      },
      {
        "value": "+8 pp",
        "label": "margem após o cálculo de custos do menu"
      },
      {
        "value": "×3",
        "label": "velocidade de harmonizações com sommelier"
      },
      {
        "value": "12+",
        "label": "agentes para o seu menu de degustação"
      }
    ],
    "beforeAfter": {
      "beforeTitle": "Sem AI Chef Pro",
      "beforeItems": [
        "Uma semana de iterações por menu novo",
        "Sequência improvisada sem equilíbrio técnico",
        "Harmonizações sem base científica",
        "Ficha de custos total, proposta a preço incerto",
        "Storytelling improvisado, equipa de sala sem formação"
      ],
      "afterTitle": "Com AI Chef Pro",
      "afterItems": [
        "Menu de degustação fechado num dia com sequência coerente",
        "Equilíbrio técnico documentado entre passos",
        "Harmonizações com Food Pairing AI fundamentadas",
        "Ficha de custos total validada e proposta clara ao cliente",
        "Storytelling profissional para o briefing de sala"
      ]
    },
    "galleryTitle": "Como Funciona o Design de Menu de Degustação com IA",
    "gallerySubtitle": "O que vai coordenar com o AI Chef Pro: sequência, passos, harmonizações, mise e equipa. Imagens geradas com IA como referência visual do conceito.",
    "galleryImages": [
      "/lovable-uploads/ai-gallery/use-case-task-menu-degustacion-hero.jpg",
      "/lovable-uploads/ai-gallery/use-case-task-menu-degustacion-pase.jpg",
      "/lovable-uploads/ai-gallery/use-case-task-menu-degustacion-secuencia.jpg",
      "/lovable-uploads/ai-gallery/use-case-task-menu-degustacion-pairing.jpg",
      "/lovable-uploads/ai-gallery/use-case-task-menu-degustacion-mise.jpg",
      "/lovable-uploads/ai-gallery/use-case-task-menu-degustacion-team.jpg"
    ]
  },
  "task-fichas-tecnicas-con-ia": {
    "h1": "Como Criar Fichas Técnicas com IA",
    "heroSubtitle": "Documenta cada prato com ficha técnica profissional: ingredientes, gramagem, técnica passo a passo, alergénios, food cost, plating photo e storytelling para sala. Suite de agentes de IA gastronómica gera ficha completa em minutos.",
    "heroTagline": "Fichas técnicas profissionais em minutos, não em horas",
    "badge": "Tarefa: Fichas técnicas",
    "painsTitle": "O Que Custa Fazer Fichas Técnicas à Mão",
    "pains": [
      "Documentar 30 pratos com ficha técnica profissional pode levar 2 semanas",
      "Sem padronização, cada cozinheiro replica a sua versão e perde consistência",
      "Alergénios calculados à mão por receita, risco legal e de segurança alimentar",
      "Sem storytelling para sala, equipa descreve o prato improvisadamente",
      "Quando se muda um ingrediente, é preciso atualizar a ficha e recalcular alergénios",
      "Falta de modelo profissional com todos os campos críticos (técnica, gramagem, mermas, custo)"
    ],
    "featuresTitle": "Como AI Chef Pro Resolve as Fichas Técnicas",
    "features": [
      {
        "icon": "BookOpen",
        "title": "Culinária Criativa com ficha completa",
        "description": "Cada receita entrega ficha técnica profissional: ingredientes, gramagem, técnica, alergénios, mermas, custo, storytelling, plating."
      },
      {
        "icon": "ShieldCheck",
        "title": "ID Alergénios",
        "description": "Identificação automática de alergénios por receita: lacticínios, glúten, frutos secos, soja, mariscos, sulfitos, etc."
      },
      {
        "icon": "Calculator",
        "title": "Custo integrado",
        "description": "Ficha técnica inclui food cost % e custo por porção calculado automaticamente com custo-hora de obrador."
      },
      {
        "icon": "Image",
        "title": "GastroIMG Gen+",
        "description": "Imagem de referência do prato empratado para incluir na ficha técnica como guia visual."
      },
      {
        "icon": "Sparkles",
        "title": "Storytelling para sala",
        "description": "Cada ficha inclui descrição profissional para que a equipa de sala recite com técnica."
      },
      {
        "icon": "CheckSquare",
        "title": "Modelo estandardizado",
        "description": "Formato uniforme para todas as fichas: técnica, conservação, alergénios, apresentação, custo."
      },
      {
        "icon": "BarChart3",
        "title": "Conversor Ing + Calcula Pax",
        "description": "Conversor de pesos e medidas; escalonamento automático para banquetes e eventos."
      },
      {
        "icon": "BookOpen",
        "title": "Pro Prompts eBook",
        "description": "eBook com 300+ prompts profissionais para fichas técnicas, alergénios e descrições para sala."
      },
      {
        "icon": "Wine",
        "title": "Maridagem na ficha",
        "description": "Food Pairing AI sugere a maridagem recomendada para incluir na ficha técnica."
      }
    ],
    "workflowTitle": "Como Criar Fichas Técnicas em 4 Passos",
    "workflow": [
      "1. Culinária Criativa (ou o seu agente criativo) — desenvolve ou carrega a receita. O agente IA entrega receita + ficha técnica completa com todos os campos profissionais.",
      "2. ID Alergénios — identifica automaticamente os alergénios por receita e integra-os na ficha; quando muda um ingrediente, recalcula no instante.",
      "3. GastroIMG Gen+ — gera imagem de referência do prato empratado para incluir na ficha como guia visual do cozinheiro.",
      "4. Food Pairing AI + storytelling para sala — a ficha inclui maridagem recomendada e descrição profissional para briefing da equipa."
    ],
    "productsTitle": "Modelos e Kits Recomendados para Fichas Técnicas",
    "productIds": [
      "kit-escandallos",
      "pack-appcc",
      "pro-prompts-ebook",
      "kit-inventario",
      "kit-tareas",
      "guia-restaurante-gastronomico"
    ],
    "testimonialQuote": "Documentar 28 pratos com ficha técnica profissional levava-nos 2 semanas. Culinária Criativa entrega já cada ficha completa em minutos: ingredientes, técnica, alergénios automáticos, custo e storytelling para sala. Agora qualquer cozinheiro replica com consistência e quando inspecionam temos tudo rastreado.",
    "testimonialAuthor": "Carla Mendoza",
    "testimonialRole": "Chefe de cozinha, restaurante casual com 3 pontos",
    "faqTitle": "Perguntas Frequentes sobre Fichas Técnicas com IA",
    "faqs": [
      {
        "q": "O que inclui uma ficha técnica profissional?",
        "a": "Ingredientes com gramagem exata, técnica passo a passo, alergénios automáticos, food cost %, custo por porção, conservação, apresentação, maridagem sugerida e descrição para sala."
      },
      {
        "q": "Como gere alergénios automaticamente?",
        "a": "ID Alergénios identifica os alergénios por ingrediente e integra-os na ficha. Quando muda um ingrediente, recalcula no instante e atualiza a informação para sala."
      },
      {
        "q": "Serve para qualquer tipo de cozinha?",
        "a": "Sim. O fluxo é o mesmo para culinária criativa, pastelaria, gelataria, chocolataria, pizzaria, qualquer tipo de cozinha nacional ou conceito."
      },
      {
        "q": "Gera imagem do prato para incluir na ficha?",
        "a": "Sim. GastroIMG Gen+ gera imagem de referência. Lembre-se de que a imagem IA é de referência visual: a foto definitiva na ficha é feita por si com o seu prato real empratado."
      },
      {
        "q": "Como me ajuda com auditorias e certificações?",
        "a": "Cada ficha técnica é rastreável: ingredientes, gramagem, alergénios, custo e técnica. Prontas para auditoria, ISO 22000, BRC e certificações de segurança alimentar."
      }
    ],
    "ctaTitle": "As suas fichas técnicas profissionais em minutos.",
    "ctaSubtitle": "Começa com o onboarding de 2 minutos. Plano Membro por 10 € por mês com 10.000 créditos.",
    "seo": {
      "title": "Como Criar Fichas Técnicas com IA: Alergénios, Custo e Storytelling | AI Chef Pro",
      "description": "Suite de IA para fichas técnicas: alergénios automáticos, custo integrado, plating photo e storytelling. Comece hoje.",
      "keywords": "fichas técnicas IA, ficha técnica prato, alergénios automáticos, custo por porção, ficha técnica restaurante",
      "ogImage": "https://aichef.pro/og/use-cases/task-fichas-tecnicas-con-ia.jpg"
    },
    "personalizationTitle": "Personalizado para a Sua Cozinha desde o Minuto Um",
    "personalizationBody": "AI Chef Pro arranca com «Quem Sou Eu?»: conta tipo de cozinha, especialidade e volume. A estrutura da ficha técnica adapta-se ao seu conceito: restaurante casual, fine dining, pastelaria, gelataria, etc.",
    "appsTitle": "Os Agentes IA que Usa para Fichas Técnicas",
    "apps": [
      {
        "name": "Culinária Criativa",
        "category": "Criatividade Culinária",
        "description": "Receitas + ficha técnica completa com todos os campos."
      },
      {
        "name": "Pastelaria Criativa",
        "category": "Criatividade Culinária",
        "description": "Fichas técnicas doces com custo-hora de obrador."
      },
      {
        "name": "Gelataria Criativa",
        "category": "Criatividade Culinária",
        "description": "Fichas com equilíbrio técnico de açúcares, sólidos e gorduras."
      },
      {
        "name": "ID Alergénios",
        "category": "Ferramentas e Utilitários",
        "description": "Identificação automática de alergénios por receita."
      },
      {
        "name": "Conversor Ing",
        "category": "Ferramentas e Utilitários",
        "description": "Conversor automático de pesos e medidas."
      },
      {
        "name": "Calcula Pax",
        "category": "Ferramentas e Utilitários",
        "description": "Escalonamento de receitas para banquetes e eventos."
      },
      {
        "name": "Mermas Genéricas",
        "category": "Ferramentas e Utilitários",
        "description": "Dados de mermas por processo integrados na ficha."
      },
      {
        "name": "Food Pairing AI",
        "category": "Criatividade Culinária",
        "description": "Maridagem sugerida para incluir na ficha."
      },
      {
        "name": "GastroIMG Gen+",
        "category": "Conhecimento Gastro",
        "description": "Imagem de referência do prato empratado."
      },
      {
        "name": "Léxico Gastronómico",
        "category": "Conhecimento Gastro",
        "description": "Tutor de definições técnicas para validar terminologia."
      },
      {
        "name": "Pro Prompts eBook",
        "category": "Conteúdos e Redes Sociais",
        "description": "300+ prompts para fichas técnicas e descrições."
      },
      {
        "name": "Sosa Ingredients",
        "category": "Fornecedores Gastro",
        "description": "Catálogo Sosa para validar técnica e ingredientes."
      }
    ],
    "metrics": [
      {
        "value": "×20",
        "label": "velocidade vs. ficha à mão"
      },
      {
        "value": "100 %",
        "label": "alergénios identificados automaticamente"
      },
      {
        "value": "ISO",
        "label": "fichas prontas para auditoria 22000"
      },
      {
        "value": "12+",
        "label": "agentes para as suas fichas técnicas"
      }
    ],
    "beforeAfter": {
      "beforeTitle": "Sem AI Chef Pro",
      "beforeItems": [
        "2 semanas para documentar 28 pratos",
        "Alergénios calculados à mão (risco legal)",
        "Storytelling improvisado em sala",
        "Mudanças de ingrediente sem atualizar fichas",
        "Sem modelo profissional estandardizado"
      ],
      "afterTitle": "Com AI Chef Pro",
      "afterItems": [
        "28 pratos documentados num dia com modelo profissional",
        "Alergénios automáticos com ID Alergénios",
        "Storytelling profissional para briefing de sala",
        "Mudanças atualizam ficha e alergénios no instante",
        "Modelo uniforme pronto para auditoria e certificações"
      ]
    },
    "galleryTitle": "Como Funcionam as Fichas Técnicas com IA",
    "gallerySubtitle": "O que vai coordenar com AI Chef Pro: ficha, binder, plating photo, tablet e equipa. Imagens geradas com IA como referência visual do conceito.",
    "galleryImages": [
      "/lovable-uploads/ai-gallery/use-case-task-fichas-tecnicas-hero.jpg",
      "/lovable-uploads/ai-gallery/use-case-task-fichas-tecnicas-document.jpg",
      "/lovable-uploads/ai-gallery/use-case-task-fichas-tecnicas-binder.jpg",
      "/lovable-uploads/ai-gallery/use-case-task-fichas-tecnicas-photo.jpg",
      "/lovable-uploads/ai-gallery/use-case-task-fichas-tecnicas-tablet.jpg",
      "/lovable-uploads/ai-gallery/use-case-task-fichas-tecnicas-team.jpg"
    ]
  },
  "task-maridajes-con-ia": {
    "h1": "Como Validar Maridajes com IA",
    "heroSubtitle": "Valide maridajes com base científica: análise de acidez, taninos, estrutura, intensidade e harmonia. Suite de agentes de IA gastronómica com técnica de sommelier profissional.",
    "heroTagline": "Maridajes científicos em minutos para qualquer carta",
    "badge": "Tarefa: Maridajes profissionais",
    "painsTitle": "O Que Custa Fazer Maridajes à Mano",
    "pains": [
      "Maridajes recomendados por intuição sem base científica fundamentada",
      "Equipa de sala sem formação constante para comunicar maridajes com critério",
      "Cambios em carta ou adega sem revalidar maridajes (fica recomendação obsoleta)",
      "Maridajes só com vinho: faltan opções com cerveza, sake, kombucha, chá e sem álcool",
      "Storytelling de cada maridaje improvisado, sem profundidade técnica",
      "Eventos privados com maridajes ad hoc sem proposta profissional clara"
    ],
    "featuresTitle": "Como AI Chef Pro Resolve os Maridajes",
    "features": [
      {
        "icon": "Wine",
        "title": "Food Pairing AI",
        "description": "Agente especializado em maridajes com base científica: análise de acidez, taninos, estrutura, intensidade, harmonia e contraste."
      },
      {
        "icon": "Sparkles",
        "title": "Bar & Lounge AI+",
        "description": "Seleção concreta de adega para cada maridaje com critério de sommelier profissional: vinhos, sakes, cervezas, espumosos."
      },
      {
        "icon": "BookOpen",
        "title": "Storytelling profissional",
        "description": "Cada maridaje inclui descrição técnica para que a equipa de sala o comunique com base profissional."
      },
      {
        "icon": "Calculator",
        "title": "Escandallo de maridajes",
        "description": "Custo real por copa, food cost do vinho e proposta de preço para o maridaje do menu de degustação."
      },
      {
        "icon": "Sparkles",
        "title": "Maridajes sem álcool",
        "description": "Propostas com kombucha, chá, café, água tónica caseira para clientes que não consumen álcool."
      },
      {
        "icon": "CheckSquare",
        "title": "Pack APPCC adega",
        "description": "Trazabilidade de adega e temperaturas de serviço por tipo de vinho."
      },
      {
        "icon": "Calendar",
        "title": "Gastro Calendar",
        "description": "Catas e eventos com maridaje, lançamentos por temporada."
      },
      {
        "icon": "Image",
        "title": "GastroIMG Gen+",
        "description": "Imagem de referência do maridaje (copa + prato) para Instagram e carta."
      },
      {
        "icon": "BookOpen",
        "title": "Léxico Gastronómico",
        "description": "Tutor de definições técnicas: enologia, vinificação, terroir, denominações."
      }
    ],
    "workflowTitle": "Como Validar Maridajes em 4 Passos",
    "workflow": [
      "1. Food Pairing AI — cargas o prato com técnica e ingredientes. A IA analiza acidez, taninos, intensidade, estrutura e propõe tipo de vinho com base científica.",
      "2. Bar & Lounge AI+ — propõe seleção concreta da sua adega: colheitas, produtores, copa ou botella. Para opções sem álcool propõe kombuchas, chás ou tónicos caseiros.",
      "3. Storytelling para sala — cada maridaje genera descrição profissional para briefing da equipa e comunicação ao cliente.",
      "4. Kit de Escandallos Pro — escandallas o custo real por copa, food cost do vinho e proposta de preço para o maridaje."
    ],
    "productsTitle": "Modelos e Kits Recomendados para Maridajes",
    "productIds": [
      "kit-tareas-bar",
      "kit-escandallos",
      "pack-appcc",
      "pro-prompts-ebook",
      "kit-inventario",
      "kit-gestion-personal"
    ],
    "testimonialQuote": "Food Pairing AI mudou a minha forma de fechar maridajes. Cada prato do menu de degustação agora tem maridaje fundamentado cientificamente que a minha equipa de sala comunica com base profissional. Subimos margen 6 pontos em adega e os clientes recorrentes premium cresceram 35 % em 6 meses.",
    "testimonialAuthor": "Eduardo Lara",
    "testimonialRole": "Head Sommelier, restaurante com 1 estrela Michelin",
    "faqTitle": "Preguntas Frecuentes sobre Maridajes com IA",
    "faqs": [
      {
        "q": "Serve para qualquer estilo de restaurante?",
        "a": "Sí. Food Pairing AI cobre desde casual até fine dining Michelin, passando por gastrobares, vinotecas e restaurantes étnicos."
      },
      {
        "q": "Tem base científica real?",
        "a": "Sí. Razoana como sommelier profissional com fundamento técnico de enologia e bromatologia: acidez, taninos, estrutura, intensidade, harmonia e contraste."
      },
      {
        "q": "Cubre maridajes sem álcool?",
        "a": "Sí. Propõe kombuchas, chás, café, tónicos caseiros e bebidas funcionais com critério profissional para clientes que não consumen álcool."
      },
      {
        "q": "Cubre maridajes com cerveza, sake, espumosos?",
        "a": "Sí. Bar & Lounge AI+ cobre todo o espectro de barra: vinhos, sakes, cervezas artesanales, espumosos e bebidas espirituosas."
      },
      {
        "q": "Genera conteúdo visual do maridaje para Instagram?",
        "a": "Sí. GastroIMG Gen+ genera imagem de referência. Lembra que a imagem IA é de referência visual: a foto definitiva fazes tu com a tua copa e prato real."
      }
    ],
    "ctaTitle": "Os seus maridajes com base científica em minutos.",
    "ctaSubtitle": "Comece com o onboarding de 2 minutos. Plano Membro por 10 € por mês com 10.000 créditos.",
    "seo": {
      "title": "Como Validar Maridajes com IA: Vinhos, Sake e Sem Álcool | AI Chef Pro",
      "description": "Suite de IA para maridajes: Food Pairing AI com base científica, seleção de adega, storytelling para sala. Comece hoje.",
      "keywords": "maridajes com IA, food pairing IA, maridaje vinho prato, IA sommelier, maridajes sem álcool IA, maridaje científico",
      "ogImage": "https://aichef.pro/og/use-cases/task-maridajes-con-ia.jpg"
    },
    "personalizationTitle": "Personalizado à Sua Adega desde o Minuto Uno",
    "personalizationBody": "AI Chef Pro arranca com «Quem Sou Eu?»: conta tipo de restaurante, tamanho de adega, especialidade e nível. Cada maridaje adapta-se ao seu inventário real, não a uma adega genérica.",
    "appsTitle": "Os Agentes IA que Usa para Maridajes",
    "apps": [
      {
        "name": "Food Pairing AI",
        "category": "Criatividade Culinária",
        "description": "Maridajes com base científica para cada prato."
      },
      {
        "name": "Bar & Lounge AI+",
        "category": "Conceitos de Negócio",
        "description": "Seleção concreta de adega com critério de sommelier."
      },
      {
        "name": "Culinária Criativa",
        "category": "Criatividade Culinária",
        "description": "Storytelling profissional do maridaje para sala."
      },
      {
        "name": "Léxico Gastronómico",
        "category": "Conhecimento",
        "description": "Tutor de definições de enologia e vinificação."
      },
      {
        "name": "Mermas Genéricas",
        "category": "Herramientas e Utilities",
        "description": "Mermas por descorche falido integradas."
      },
      {
        "name": "ID Alergénios",
        "category": "Herramientas e Utilities",
        "description": "Identificação de sulfitos para clientes sensibles."
      },
      {
        "name": "GastroIMG Gen+",
        "category": "Conhecimento",
        "description": "Imagem de referência do maridaje."
      },
      {
        "name": "Sonar Deep Research",
        "category": "Modelos IA + LLM",
        "description": "Research profundo de adegas e colheitas."
      },
      {
        "name": "Gastro Calendar",
        "category": "Contenidos e RRSS",
        "description": "Catas e eventos com maridaje."
      },
      {
        "name": "BlogPost SEO Gen+",
        "category": "Contenidos e RRSS",
        "description": "Artículos SEO sobre maridajes e adegas."
      },
      {
        "name": "InstaFlow AI Pro",
        "category": "Contenidos e RRSS",
        "description": "Instagram com maridajes destacados."
      },
      {
        "name": "Pro Prompts eBook",
        "category": "Contenidos e RRSS",
        "description": "300+ prompts para descripciones de maridaje."
      }
    ],
    "metrics": [
      {
        "value": "×10",
        "label": "velocidade vs. validação à mano"
      },
      {
        "value": "+6 pp",
        "label": "margen após escandallar adega"
      },
      {
        "value": "+35 %",
        "label": "clientes recorrentes premium"
      },
      {
        "value": "12+",
        "label": "agentes para maridajes"
      }
    ],
    "beforeAfter": {
      "beforeTitle": "Sem AI Chef Pro",
      "beforeItems": [
        "Maridajes por intuição sem base científica",
        "Sem opções sem álcool profissionais",
        "Equipa de sala sem formação documentada",
        "Cambios em adega sem revalidar maridajes",
        "Maridajes para eventos privados ad hoc"
      ],
      "afterTitle": "Com AI Chef Pro",
      "afterItems": [
        "Maridajes com base científica de Food Pairing AI",
        "Opções com kombucha, chá, tónicas caseiras",
        "Briefing diário à equipa com storytelling profissional",
        "Cambios em adega revalidan maridajes ao instante",
        "Maridajes para eventos cerrados com proposta profissional"
      ]
    },
    "galleryTitle": "Como Funciona a Validação de Maridajes com IA",
    "gallerySubtitle": "O que vai coordenar com AI Chef Pro: copas, pratos, notas, adega e equipa. Imagens generadas com IA como referência visual do conceito.",
    "galleryImages": [
      "/lovable-uploads/ai-gallery/use-case-task-maridajes-hero.jpg",
      "/lovable-uploads/ai-gallery/use-case-task-maridajes-glasses.jpg",
      "/lovable-uploads/ai-gallery/use-case-task-maridajes-plate.jpg",
      "/lovable-uploads/ai-gallery/use-case-task-maridajes-notes.jpg",
      "/lovable-uploads/ai-gallery/use-case-task-maridajes-bottles.jpg",
      "/lovable-uploads/ai-gallery/use-case-task-maridajes-team.jpg"
    ]
  },
  "task-reducir-mermas-con-ia": {
    "h1": "Como Reduzir Perdas na Cozinha com IA",
    "heroSubtitle": "Identifique, meça e reduza perdas por processo (desmancha, moldagem, cozedura, vitrina, entrega) com dados reais integrados na ficha técnica. Suite de agentes de IA gastronómica especializados em operativa zero-waste.",
    "heroTagline": "Perdas reduzidas com dados reais por processo",
    "badge": "Tarefa: Redução de perdas",
    "painsTitle": "O Que Custam as Perdas Sem Controlo",
    "pains": [
      "Perdas estimadas a olho (15-30 % em alguns cortes), não dados reais por processo",
      "Falta de dados por tipo de cozinha (gelataria, padaria, grelhados, sushi têm perdas distintas)",
      "Sem sistema para reaproveitar aparas e cascas (caldos, vinagres infusionados, desidratados)",
      "Quando um fornecedor muda, as perdas mudam sem recalcular a margem",
      "Equipa sem formação constante em técnica de aproveitamento profissional",
      "Sem rastreabilidade para auditorias de sustentabilidade e certificações zero-waste"
    ],
    "featuresTitle": "Como AI Chef Pro Reduz Perdas",
    "features": [
      {
        "icon": "BarChart3",
        "title": "Mermas Genéricas",
        "description": "Dados precisos de perdas por processo por tipo de cozinha: desmancha, dry-aging, moldagem, cozedura, vitrina, entrega."
      },
      {
        "icon": "Sparkles",
        "title": "Culinária Criativa",
        "description": "Raciocina técnicas de reaproveitamento: aparas para caldos, cascas para vinagres infusionados, restos para desidratados com critério profissional."
      },
      {
        "icon": "Calculator",
        "title": "Perdas na ficha técnica",
        "description": "Perdas reais por processo integradas na ficha técnica do Kit de Escandallos Pro: o custo por prato reflete a perda real, não estimada."
      },
      {
        "icon": "CheckSquare",
        "title": "Kit de Tareas Restaurante Casual",
        "description": "Modelos com procedimentos de aproveitamento por estação, controlo de perdas semanal, formação de equipa."
      },
      {
        "icon": "ShieldCheck",
        "title": "Pack APPCC rastreável",
        "description": "Rastreabilidade de perdas por processo para auditorias de sustentabilidade e certificações zero-waste."
      },
      {
        "icon": "Beaker",
        "title": "Fermentus Con AI+",
        "description": "Fermentos para reaproveitar produto: chucrute com sobras de couve, kombucha com cascas de fruta, garum com espinhas de peixe."
      },
      {
        "icon": "Sparkles",
        "title": "VegChef Plant-Based",
        "description": "Para reaproveitamento profissional vegetal: aproveitamento integral do vegetal, técnica de stems-to-roots."
      },
      {
        "icon": "BarChart3",
        "title": "Calcula Pax",
        "description": "Compras ajustadas ao volume real do evento ou serviço para reduzir sobras desde a origem."
      },
      {
        "icon": "Calendar",
        "title": "Gastro Calendar",
        "description": "Planeamento de produção ajustado à procura histórica para reduzir sobreprodução."
      }
    ],
    "workflowTitle": "Como Reduzir Perdas em 4 Passos",
    "workflow": [
      "1. Mermas Genéricas — o agente IA entrega dados reais por processo por tipo de cozinha (desmancha de carne, moldagem de massa, cozedura de pão, vitrina de gelado, entrega de pizza). Carrega o dado real da sua operação.",
      "2. Culinária Criativa + Fermentus Con AI+ — desenvolve técnicas de reaproveitamento: aparas para caldos, cascas para vinagres, restos para desidratados, sobras para fermentos.",
      "3. Kit de Escandallos Pro — a ficha técnica reflete a perda real, não estimada. O custo por prato sobe ligeiramente mas reflete o custo verdadeiro, evitando surpresas na margem.",
      "4. Calcula Pax + Gastro Calendar — compras ajustadas ao volume real do serviço ou evento para reduzir sobras desde a origem, não apenas processar perdas posteriormente."
    ],
    "productsTitle": "Modelos e Kits Recomendados para Reduzir Perdas",
    "productIds": [
      "kit-escandallos",
      "kit-inventario",
      "pack-appcc",
      "pro-prompts-ebook",
      "kit-tareas",
      "kit-gestion-personal"
    ],
    "testimonialQuote": "Mermas Genéricas + Culinária Criativa mudaram-nos a operativa. Passámos de perdas estimadas (assumíamos 12-15%) a dados reais de 22-28% em alguns processos. Reorganizámos a desmancha e o aproveitamento com técnica documentada e baixámos as perdas 35% em 4 meses. A ficha técnica agora reflete o custo real, não o ideal.",
    "testimonialAuthor": "Sofía Cano",
    "testimonialRole": "Sous chef, restaurante casual com compromisso zero-waste",
    "faqTitle": "Perguntas Frequentes sobre Reduzir Perdas com IA",
    "faqs": [
      {
        "q": "Serve para qualquer tipo de cozinha?",
        "a": "Sim. Mermas Genéricas cobre dados por processo por tipo de cozinha: grelhados, sushi, massa, pão, gelado, chocolate, molho, marinada. Cada cozinha tem perdas distintas."
      },
      {
        "q": "Como integro perdas reais na ficha técnica?",
        "a": "Kit de Escandallos Pro tem um campo de perda por ingrediente e por processo. Mermas Genéricas entrega os dados reais para que o custo por prato reflita a realidade."
      },
      {
        "q": "Cobre técnicas de reaproveitamento profissional?",
        "a": "Sim. Culinária Criativa entrega técnicas de aproveitamento: stems-to-roots vegetal, aparas para caldos, cascas para vinagres, fermentos com sobras. Fermentus aprofunda em técnicas avançadas."
      },
      {
        "q": "Gera rastreabilidade para certificações zero-waste?",
        "a": "Sim. Pack APPCC + Mermas Genéricas entregam rastreabilidade documentada para auditorias de sustentabilidade e certificações zero-waste ou B-Corp."
      },
      {
        "q": "Como me ajuda com compras ajustadas?",
        "a": "Calcula Pax + Gastro Calendar planeiam produção e compras ajustadas ao volume real do serviço para reduzir sobras desde a origem."
      }
    ],
    "ctaTitle": "A sua cozinha com perdas reduzidas e dados reais.",
    "ctaSubtitle": "Comece com o onboarding de 2 minutos. Plano Membro por 10 € por mês com 10.000 créditos.",
    "seo": {
      "title": "Como Reduzir Perdas na Cozinha com IA: Dados Reais e Reaproveitamento | AI Chef Pro",
      "description": "Suite de IA para reduzir perdas: Mermas Genéricas com dados reais, reaproveitamento profissional, ficha técnica rastreável. Comece hoje.",
      "keywords": "reduzir perdas restaurante, perdas com IA, food waste IA, zero waste cozinha, perdas na produção, reduzir desperdícios",
      "ogImage": "https://aichef.pro/og/use-cases/task-reducir-mermas-con-ia.jpg"
    },
    "personalizationTitle": "Personalizado à Sua Cozinha desde o Minuto Um",
    "personalizationBody": "AI Chef Pro arranca com «Quem Sou Eu?»: conta o tipo de cozinha e volume. Mermas Genéricas entrega dados por processo adaptados ao seu conceito: grelhados, sushi, massa, pão, gelado, chocolate.",
    "appsTitle": "Os Agentes IA que Usa para Reduzir Perdas",
    "apps": [
      {
        "name": "Mermas Genéricas",
        "category": "Ferramentas e Utilitários",
        "description": "Dados reais de perdas por processo por tipo de cozinha."
      },
      {
        "name": "Culinária Criativa",
        "category": "Criatividade Culinária",
        "description": "Técnicas de reaproveitamento profissional de aparas e sobras."
      },
      {
        "name": "Fermentus Con AI+",
        "category": "Criatividade Culinária",
        "description": "Fermentos para reaproveitar sobras (chucrute, kombucha, garum)."
      },
      {
        "name": "VegChef Plant-Based",
        "category": "Criatividade Culinária",
        "description": "Aproveitamento integral do vegetal (stems-to-roots)."
      },
      {
        "name": "Calcula Pax",
        "category": "Ferramentas e Utilitários",
        "description": "Compras ajustadas ao volume real do serviço."
      },
      {
        "name": "Conversor Ing",
        "category": "Ferramentas e Utilitários",
        "description": "Conversor de pesos e medidas para precisão."
      },
      {
        "name": "ID Alergénios",
        "category": "Ferramentas e Utilitários",
        "description": "Identificação em produtos reaproveitados."
      },
      {
        "name": "Gastro Calendar",
        "category": "Conteúdos e Redes Sociais",
        "description": "Planeamento de produção ajustado à procura histórica."
      },
      {
        "name": "BlogPost SEO Gen+",
        "category": "Conteúdos e Redes Sociais",
        "description": "Artigos SEO sobre sustentabilidade para captar tráfego."
      },
      {
        "name": "GastroIMG Gen+",
        "category": "Conhecimento Gastronómico",
        "description": "Imagem de referência de pratos zero-waste."
      },
      {
        "name": "Coach Mental",
        "category": "Ferramentas e Utilitários",
        "description": "Coaching para liderança de equipa em zero-waste."
      },
      {
        "name": "Sonar Deep Research",
        "category": "Modelos IA + LLM",
        "description": "Investigação sobre técnicas zero-waste de referências."
      }
    ],
    "metrics": [
      {
        "value": "−35 %",
        "label": "perdas em 4 meses"
      },
      {
        "value": "+4 pp",
        "label": "margem após integrar perdas reais"
      },
      {
        "value": "×3",
        "label": "velocidade vs. estimativa manual"
      },
      {
        "value": "12+",
        "label": "agentes para reduzir perdas"
      }
    ],
    "beforeAfter": {
      "beforeTitle": "Sem AI Chef Pro",
      "beforeItems": [
        "Perdas estimadas a olho, ficha técnica com custo subestimado",
        "Sem técnica documentada de reaproveitamento",
        "Compras genéricas sem ajuste ao volume real",
        "Equipa sem formação em aproveitamento profissional",
        "Sem rastreabilidade para auditorias de sustentabilidade"
      ],
      "afterTitle": "Com AI Chef Pro",
      "afterItems": [
        "Perdas reais documentadas por processo",
        "Técnicas de reaproveitamento com Culinária Criativa + Fermentus",
        "Compras ajustadas ao volume real com Calcula Pax",
        "Briefing à equipa com técnica documentada",
        "Rastreabilidade APPCC para auditorias zero-waste"
      ]
    },
    "galleryTitle": "Como Funciona a Redução de Perdas com IA",
    "gallerySubtitle": "O que vai coordenar com AI Chef Pro: pesagem, tracking, organização, reaproveitamento e equipa. Imagens geradas com IA como referência visual do conceito.",
    "galleryImages": [
      "/lovable-uploads/ai-gallery/use-case-task-mermas-hero.jpg",
      "/lovable-uploads/ai-gallery/use-case-task-mermas-scale.jpg",
      "/lovable-uploads/ai-gallery/use-case-task-mermas-tracking.jpg",
      "/lovable-uploads/ai-gallery/use-case-task-mermas-bins.jpg",
      "/lovable-uploads/ai-gallery/use-case-task-mermas-recovery.jpg",
      "/lovable-uploads/ai-gallery/use-case-task-mermas-team.jpg"
    ]
  },
  "task-appcc-digital-con-ia": {
    "h1": "Como Gerir APPCC Digital com IA",
    "heroSubtitle": "Substitua o papel impresso disperso por APPCC a partir do telemóvel com modelos profissionais: temperaturas, limpeza, rastreabilidade, alergénios, pragas, óleo e água. Suite de agentes de IA gastronómica com base regulatória.",
    "heroTagline": "APPCC profissional a partir do telemóvel sem papel",
    "badge": "Tarefa: APPCC e segurança alimentar",
    "painsTitle": "O Que Custa Gerir APPCC em Papel",
    "pains": [
      "Papel impresso disperso pela cozinha, registos incompletos em inspeções",
      "Sem padronização por conceito (gelataria, padaria, grelhados, sushi têm registos distintos)",
      "Alergénios calculados à mão por receita, risco legal e de segurança",
      "Alterações na regulamentação sem atualizar modelos e procedimentos",
      "Equipa rotativa sem formação constante em segurança alimentar",
      "Sem rastreabilidade para auditorias ISO 22000, BRC, IFS ou certificações de qualidade"
    ],
    "featuresTitle": "Como AI Chef Pro Resolve o APPCC",
    "features": [
      {
        "icon": "ShieldCheck",
        "title": "Pack APPCC com modelos Excel",
        "description": "19 registos Excel descarregáveis: temperaturas, limpeza, rastreabilidade, alergénios, pragas, óleo e água."
      },
      {
        "icon": "Sparkles",
        "title": "ID Alergénios",
        "description": "Identificação automática de alergénios por ingrediente e receita. Quando altera um ingrediente, recalcula instantaneamente."
      },
      {
        "icon": "CheckSquare",
        "title": "Kit de Tareas con APPCC",
        "description": "Modelos de tarefas com APPCC integrado por turno: abertura, serviço, fecho."
      },
      {
        "icon": "BarChart3",
        "title": "Rastreabilidade de produtos",
        "description": "Rastreabilidade de peixe fresco, lacticínios, frutos secos, fermentos, conservas com temperaturas críticas."
      },
      {
        "icon": "BookOpen",
        "title": "Culinária Criativa com APPCC",
        "description": "Receitas que incluem procedimentos APPCC integrados na ficha técnica: temperatura, conservação, alergénios."
      },
      {
        "icon": "Calendar",
        "title": "Limpeza programada",
        "description": "Calendário de limpeza profunda por estação e turno com modelos específicos e assinatura digital."
      },
      {
        "icon": "Sparkles",
        "title": "Pro Prompts eBook",
        "description": "300+ prompts profissionais para gestão APPCC, formação de equipa e comunicação com inspetores."
      },
      {
        "icon": "Wine",
        "title": "Pack APPCC para adega",
        "description": "Rastreabilidade de vinhos, descorque, conservação e temperaturas de serviço por tipo."
      },
      {
        "icon": "BarChart3",
        "title": "Sonar Deep Research",
        "description": "Pesquisa profunda de regulamentação sanitária por país, comunidade autónoma e tipo de estabelecimento."
      }
    ],
    "workflowTitle": "Como Implementar APPCC Digital em 4 Passos",
    "workflow": [
      "1. Pack APPCC (€14, modelos Excel descarregáveis) — descarrega os 19 registos profissionais adaptados ao seu tipo de cozinha (pastelaria, gelataria, restaurante, etc.).",
      "2. ID Alergénios — analisa automaticamente as receitas e modelos do seu menu para identificar alergénios por prato. Integra-o nas fichas técnicas e na sala.",
      "3. Culinária Criativa com APPCC integrado — cada receita nova entrega procedimentos APPCC (temperatura crítica, conservação, alergénios, armazenamento) integrados na ficha técnica.",
      "4. Kit de Tareas con APPCC — modelos de turno (abertura, serviço, fecho) com APPCC integrado. A equipa assina digitalmente cada turno a partir do telemóvel."
    ],
    "productsTitle": "Modelos e Kits Recomendados para APPCC",
    "productIds": [
      "pack-appcc",
      "kit-tareas",
      "pro-prompts-ebook",
      "kit-escandallos",
      "kit-inventario",
      "kit-gestion-personal"
    ],
    "testimonialQuote": "Pack APPCC + ID Alergénios transformaram a nossa segurança alimentar. Passámos de papel impresso disperso para 19 registos digitais com APPCC integrado por turno e alergénios automáticos por receita. A inspeção sanitária sai impecável e o risco legal caiu para zero.",
    "testimonialAuthor": "Roberto Castaño",
    "testimonialRole": "Diretor de F&B, hotel 5 estrelas com 4 outlets",
    "faqTitle": "Perguntas Frequentes sobre APPCC com IA",
    "faqs": [
      {
        "q": "Serve para qualquer tipo de estabelecimento?",
        "a": "Sim. Pack APPCC adapta modelos a restaurante, cafetaria, pastelaria, gelataria, chocolataria, pizzaria, dark kitchen, bar, catering, hotel."
      },
      {
        "q": "Como gero alergénios automaticamente?",
        "a": "ID Alergénios identifica alergénios por ingrediente e receita, integra-os em fichas técnicas e modelos APPCC. Quando altera um ingrediente, recalcula instantaneamente."
      },
      {
        "q": "Cobre regulamentação europeia, latino-americana?",
        "a": "Sim. Pack APPCC cobre regulamentação europeia (UE 852/2004 + 178/2002 + 1169/2011 alergénios) e adaptações à América Latina. Sonar Deep Research permite consultar regulamentação específica por país."
      },
      {
        "q": "Gera rastreabilidade para auditorias ISO?",
        "a": "Sim. APPCC a partir do telemóvel com assinatura digital + rastreabilidade de produtos + calendário de limpeza prontos para auditorias ISO 22000, BRC, IFS, FSSC 22000."
      },
      {
        "q": "Como me ajuda com alterações regulamentares?",
        "a": "Sonar Deep Research consulta regulamentação atualizada por país e comunidade autónoma. Culinária Criativa atualiza fichas técnicas e procedimentos quando as normas mudam."
      }
    ],
    "ctaTitle": "O seu APPCC profissional a partir do telemóvel sem papel.",
    "ctaSubtitle": "Comece com o onboarding de 2 minutos. Plano Membro por 10 € por mês com 10.000 créditos.",
    "seo": {
      "title": "Como Gerir APPCC Digital com IA: Modelos, Alergénios e Rastreabilidade | AI Chef Pro",
      "description": "Suite de IA para APPCC digital: modelos Excel, alergénios automáticos, rastreabilidade ISO. Comece hoje.",
      "keywords": "APPCC digital IA, modelos APPCC, alergénios automáticos, ISO 22000 IA, segurança alimentar IA, HACCP digital",
      "ogImage": "https://aichef.pro/og/use-cases/task-appcc-digital-con-ia.jpg"
    },
    "personalizationTitle": "Personalizado ao Seu Estabelecimento desde o Primeiro Minuto",
    "personalizationBody": "AI Chef Pro arranca com «Quem Sou Eu?»: conta o tipo de estabelecimento e país. Pack APPCC adapta modelos ao seu conceito e regulamentação local.",
    "appsTitle": "Os Agentes IA que Usa para APPCC",
    "apps": [
      {
        "name": "ID Alergénios",
        "category": "Ferramentas e Utilitários",
        "description": "Identificação automática de alergénios por receita."
      },
      {
        "name": "Culinária Criativa",
        "category": "Criatividade Culinária",
        "description": "Receitas com procedimentos APPCC integrados."
      },
      {
        "name": "Pastelaria Criativa",
        "category": "Criatividade Culinária",
        "description": "APPCC específico para pastelaria e obradores."
      },
      {
        "name": "Gelataria Criativa",
        "category": "Criatividade Culinária",
        "description": "APPCC específico para gelataria com produto sensível."
      },
      {
        "name": "Chocolataria Criativa",
        "category": "Criatividade Culinária",
        "description": "APPCC específico para chocolataria e bombonaria."
      },
      {
        "name": "Mermas Genéricas",
        "category": "Ferramentas e Utilitários",
        "description": "Rastreabilidade de mermas integrada no APPCC."
      },
      {
        "name": "Conversor Ing",
        "category": "Ferramentas e Utilitários",
        "description": "Conversor de pesos e medidas."
      },
      {
        "name": "Sonar Deep Research",
        "category": "Modelos IA + LLM",
        "description": "Pesquisa profunda de regulamentação por país."
      },
      {
        "name": "Léxico Gastronómico",
        "category": "Conhecimento Gastro",
        "description": "Tutor de definições técnicas regulamentares."
      },
      {
        "name": "Pro Prompts eBook",
        "category": "Conteúdos e Redes Sociais",
        "description": "300+ prompts para gestão APPCC."
      },
      {
        "name": "BlogPost SEO Gen+",
        "category": "Conteúdos e Redes Sociais",
        "description": "Artigos sobre segurança alimentar para tráfego orgânico."
      },
      {
        "name": "Coach Mental",
        "category": "Ferramentas e Utilitários",
        "description": "Coaching para gestão de stress em inspeções."
      }
    ],
    "metrics": [
      {
        "value": "ISO",
        "label": "modelos prontos para 22000, BRC, IFS"
      },
      {
        "value": "100 %",
        "label": "alergénios identificados automaticamente"
      },
      {
        "value": "0 %",
        "label": "risco legal por alergénios não declarados"
      },
      {
        "value": "12+",
        "label": "agentes para o seu APPCC"
      }
    ],
    "beforeAfter": {
      "beforeTitle": "Sem AI Chef Pro",
      "beforeItems": [
        "Papel impresso disperso pela cozinha",
        "Alergénios calculados à mão (risco legal)",
        "Sem modelos adaptados ao tipo de cozinha",
        "Equipa rotativa sem formação documentada",
        "Sem rastreabilidade para auditorias ISO"
      ],
      "afterTitle": "Com AI Chef Pro",
      "afterItems": [
        "APPCC a partir do telemóvel com assinatura digital",
        "Alergénios automáticos com ID Alergénios",
        "Modelos Excel adaptados por conceito",
        "Briefing com APPCC integrado no Kit de Tareas",
        "Rastreabilidade pronta para ISO 22000, BRC, IFS"
      ]
    },
    "galleryTitle": "Como Funciona o APPCC Digital com IA",
    "gallerySubtitle": "O que vai coordenar com AI Chef Pro: termómetro, tablet, câmara, limpeza e equipa. Imagens geradas com IA como referência visual do conceito.",
    "galleryImages": [
      "/lovable-uploads/ai-gallery/use-case-task-appcc-hero.jpg",
      "/lovable-uploads/ai-gallery/use-case-task-appcc-thermometer.jpg",
      "/lovable-uploads/ai-gallery/use-case-task-appcc-tablet.jpg",
      "/lovable-uploads/ai-gallery/use-case-task-appcc-fridge.jpg",
      "/lovable-uploads/ai-gallery/use-case-task-appcc-cleaning.jpg",
      "/lovable-uploads/ai-gallery/use-case-task-appcc-team.jpg"
    ]
  },
  "task-carta-estacional-con-ia": {
    "h1": "Como Criar Carta Sazonal com IA",
    "heroSubtitle": "Desenhe carta sazonal com produto local da época, custo de receita profissional, planeamento com antecedência e storytelling de produtores. Suite de agentes de IA gastronómica com calendário por hemisfério e região.",
    "heroTagline": "Carta de época com critério profissional em horas",
    "badge": "Tarefa: Carta sazonal",
    "painsTitle": "O Que Custa Criar Carta Sazonal à Mão",
    "pains": [
      "Uma semana ou mais para iterar e fechar carta de época com custo de receita validado",
      "Sem critério claro de produto local por época e região (muda entre hemisférios)",
      "Produto fora de época com custo alto e mermas elevadas (importação, refrigeração)",
      "Sem storytelling de produtores locais para a sala e comunicação",
      "Mudanças bruscas entre épocas sem planeamento com antecedência",
      "Sem coordenação com calendário de festividades (Páscoa, Natal, Dia da Mãe, eventos locais)"
    ],
    "featuresTitle": "Como AI Chef Pro Resolve a Carta Sazonal",
    "features": [
      {
        "icon": "Calendar",
        "title": "Gastro Calendar",
        "description": "Planeamento sazonal por hemisfério e região com produto local da época e festividades-chave."
      },
      {
        "icon": "Sparkles",
        "title": "Culinária Criativa sazonal",
        "description": "Raciocina pratos signature com produto local da época: cogumelos de outono, espargos de primavera, hortaliças de verão, raízes de inverno."
      },
      {
        "icon": "Calculator",
        "title": "Custo de receita sazonal",
        "description": "Receita + custo de receita CSV com produto local; Kit de Escandallos Pro recalcula margem ao mudar a época."
      },
      {
        "icon": "BookOpen",
        "title": "Storytelling de produtores",
        "description": "Cada prato inclui storytelling do produtor local: pecuarista, agricultor, padeiro, pescador, para comunicação com a sala e o cliente."
      },
      {
        "icon": "Wine",
        "title": "Bar & Lounge AI+",
        "description": "Vinhos de época e harmonizações ajustadas ao produto sazonal para a sua carta."
      },
      {
        "icon": "Image",
        "title": "GastroIMG Gen+ + Gerador de Pins Pinterest",
        "description": "Fotografia sazonal IA + Pinterest captura tráfego orgânico para produto de época."
      },
      {
        "icon": "CheckSquare",
        "title": "Kit de Tareas Restaurante",
        "description": "Modelos de transição entre épocas: rotação de stock, formação de equipa, lançamento de carta."
      },
      {
        "icon": "Sparkles",
        "title": "VegChef Plant-Based",
        "description": "Para vegetais de época com técnica avançada (fermentos, desidratados, conservas)."
      },
      {
        "icon": "BarChart3",
        "title": "Sosa Ingredients",
        "description": "Catálogo Sosa para complementar produto local com técnica profissional."
      }
    ],
    "workflowTitle": "Como Criar Carta Sazonal em 5 Passos",
    "workflow": [
      "1. Gastro Calendar — define hemisfério, região e época (ex.: outono Hemisfério Norte, Madrid). O agente IA entrega produto local da época e festividades-chave (Dia da Mãe, Natal, São Valentim).",
      "2. Culinária Criativa — desenvolve pratos signature com produto local. Cada receita entrega receita + custo de receita CSV + storytelling do produtor.",
      "3. Kit de Escandallos Pro — carrega os CSVs com os seus preços reais de fornecedores locais, valida margem e food cost % por prato e carta total.",
      "4. Bar & Lounge AI+ + Food Pairing AI — atualiza vinhos de época e harmonizações ajustadas ao produto sazonal.",
      "5. GastroIMG Gen+ + Gerador de Pins Pinterest — gera imagens de referência da nova carta e pins otimizados para captar tráfego orgânico sazonal."
    ],
    "productsTitle": "Modelos e Kits Recomendados para Carta Sazonal",
    "productIds": [
      "kit-escandallos",
      "pack-appcc",
      "pro-prompts-ebook",
      "kit-inventario",
      "kit-tareas",
      "kit-plan-financiero"
    ],
    "testimonialQuote": "Gastro Calendar + Culinária Criativa mudaram-nos o fecho de cartas sazonais. O que antes era uma semana é agora um dia com custo de receita profissional, produto local rastreado e storytelling de produtores para a sala. Subimos margem 6 pontos e a captação com Gerador de Pins Pinterest para produto de época duplicou.",
    "testimonialAuthor": "Marina Lozano",
    "testimonialRole": "Chef executiva, restaurante de autor com produto local",
    "faqTitle": "Perguntas Frequentes sobre Carta Sazonal com IA",
    "faqs": [
      {
        "q": "Serve para hemisfério norte e sul?",
        "a": "Sim. Gastro Calendar adapta produto local e época por hemisfério e região. O que é outono em Espanha é primavera na Argentina."
      },
      {
        "q": "Como gere produto local com custo variável?",
        "a": "Kit de Escandallos Pro recalcula instantaneamente a margem quando atualiza preços. Mermas Genéricas adiciona o custo de mermas sazonais (maior em produto fora de época)."
      },
      {
        "q": "Cobre festividades por região?",
        "a": "Sim. Gastro Calendar planeia festividades-chave por país e região: Páscoa, Natal, Dia da Mãe, São Valentim, festas locais (San Fermín, Fallas, etc.)."
      },
      {
        "q": "Gera conteúdo visual sazonal?",
        "a": "Sim. GastroIMG Gen+ + Gerador de Pins Pinterest geram imagens de referência e pins para captar tráfego orgânico sazonal. Lembre-se de que a imagem IA é de referência visual: a foto definitiva é feita por si com o seu prato real."
      },
      {
        "q": "Como me ajuda com storytelling de produtores?",
        "a": "Culinária Criativa raciocina em chave de produto local: pecuarista de raça autóctone, agricultor ecológico, pescador artesanal, padeiro local. Cada prato inclui storytelling profissional para a sala e comunicação."
      }
    ],
    "ctaTitle": "A sua carta sazonal com produto local e margem real.",
    "ctaSubtitle": "Comece com o onboarding de 2 minutos. Plano Membro por 10 € por mês com 10.000 créditos.",
    "seo": {
      "title": "Como Criar Carta Sazonal com IA: Produto Local, Custo de Receita e Storytelling | AI Chef Pro",
      "description": "Suite de IA para carta sazonal: Gastro Calendar, produto local, custo de receita e storytelling de produtores. Comece hoje.",
      "keywords": "carta sazonal IA, menu sazonal, produto local restaurante, gastro calendar, carta outono primavera IA",
      "ogImage": "https://aichef.pro/og/use-cases/task-carta-estacional-con-ia.jpg"
    },
    "personalizationTitle": "Personalizado ao Seu Restaurante desde o Minuto Um",
    "personalizationBody": "AI Chef Pro arranca com «Quem Sou Eu?»: conta tipo de restaurante, hemisfério, região e foco (km 0, produto local, autoria). Cada agente responde adaptado ao seu mercado real.",
    "appsTitle": "Os Agentes IA que Usa para Carta Sazonal",
    "apps": [
      {
        "name": "Gastro Calendar",
        "category": "Conteúdos e Redes Sociais",
        "description": "Planeamento sazonal por hemisfério e região."
      },
      {
        "name": "Culinária Criativa",
        "category": "Criatividade Culinária",
        "description": "Pratos signature com produto local da época."
      },
      {
        "name": "Pastelaria Criativa",
        "category": "Criatividade Culinária",
        "description": "Sobremesas com fruta e produto sazonal."
      },
      {
        "name": "VegChef Plant-Based",
        "category": "Criatividade Culinária",
        "description": "Vegetais de época com técnica avançada."
      },
      {
        "name": "Food Pairing AI",
        "category": "Criatividade Culinária",
        "description": "Harmonizações ajustadas ao produto sazonal."
      },
      {
        "name": "Bar & Lounge AI+",
        "category": "Conceitos de Negócio",
        "description": "Vinhos de época para a sua carta."
      },
      {
        "name": "Sosa Ingredients",
        "category": "Fornecedores Gastro",
        "description": "Catálogo Sosa para complementar produto local."
      },
      {
        "name": "Mermas Genéricas",
        "category": "Ferramentas e Utilitários",
        "description": "Mermas sazonais integradas ao custo de receita."
      },
      {
        "name": "Calcula Pax",
        "category": "Ferramentas e Utilitários",
        "description": "Dimensionamento para eventos privados de época."
      },
      {
        "name": "GastroIMG Gen+",
        "category": "Conhecimento Gastro",
        "description": "Fotografia sazonal IA de referência."
      },
      {
        "name": "Gerador de Pins Pinterest",
        "category": "Conteúdos e Redes Sociais",
        "description": "Pinterest captura tráfego orgânico sazonal."
      },
      {
        "name": "BlogPost SEO Gen+",
        "category": "Conteúdos e Redes Sociais",
        "description": "Artigos SEO sobre produto local de época."
      }
    ],
    "metrics": [
      {
        "value": "×7",
        "label": "velocidade vs. processo manual"
      },
      {
        "value": "+6 pp",
        "label": "margem após custo de receita da carta"
      },
      {
        "value": "×2",
        "label": "tráfego orgânico sazonal"
      },
      {
        "value": "12+",
        "label": "agentes para carta sazonal"
      }
    ],
    "beforeAfter": {
      "beforeTitle": "Sem AI Chef Pro",
      "beforeItems": [
        "Uma semana de iterações por carta nova",
        "Produto fora de época com custo alto",
        "Sem storytelling de produtores locais",
        "Festividades reativas, sem planeamento",
        "Sem conteúdo visual para captação sazonal"
      ],
      "afterTitle": "Com AI Chef Pro",
      "afterItems": [
        "Carta sazonal fechada em um dia",
        "Produto local da época com custo otimizado",
        "Storytelling profissional de produtores",
        "Festividades planeadas com 8 semanas de antecedência",
        "GastroIMG Gen+ + Pinterest captam tráfego sazonal"
      ]
    },
    "galleryTitle": "Como Funciona o Design de Carta Sazonal com IA",
    "gallerySubtitle": "O que vai coordenar com AI Chef Pro: produto outono, primavera, calendário, tasting e equipa. Imagens geradas com IA como referência visual do conceito.",
    "galleryImages": [
      "/lovable-uploads/ai-gallery/use-case-task-carta-estacional-hero.jpg",
      "/lovable-uploads/ai-gallery/use-case-task-carta-estacional-otono.jpg",
      "/lovable-uploads/ai-gallery/use-case-task-carta-estacional-primavera.jpg",
      "/lovable-uploads/ai-gallery/use-case-task-carta-estacional-calendar.jpg",
      "/lovable-uploads/ai-gallery/use-case-task-carta-estacional-tasting.jpg",
      "/lovable-uploads/ai-gallery/use-case-task-carta-estacional-team.jpg"
    ]
  },
  "task-foto-gastronomica-con-ia": {
    "h1": "Como Fazer Fotografia Gastronómica com IA",
    "heroSubtitle": "Gera imagens de referência profissionais do prato antes de cozinhar para validar empratamento, paleta e composição. Depois tira a foto definitiva do prato real com critério claro da imagem objetivo.",
    "heroTagline": "Imagem de referência primeiro, foto definitiva depois",
    "badge": "Tarefa: Fotografia gastronómica",
    "painsTitle": "O Que Custa a Fotografia Gastronómica Tradicional",
    "pains": [
      "Sessões de food styling sem imagem de referência clara, iterações dispendiosas",
      "Sem critério partilhado entre chef, fotógrafo e stylist sobre composição e paleta",
      "Produto fresco degrada-se durante a sessão, foto não captura o momento ótimo",
      "Alterações na carta requerem nova sessão completa e dispendiosa",
      "Imagens para Instagram, Glovo, web e carta requerem formatos distintos",
      "Imagem industrial vs. imagem de autor: critério inconsistente entre canais"
    ],
    "featuresTitle": "Como o AI Chef Pro Resolve a Fotografia Gastronómica",
    "features": [
      {
        "icon": "Image",
        "title": "GastroIMG Gen+",
        "description": "Agente especializado em fotografia gastronómica com IA: gera imagem de referência profissional do prato."
      },
      {
        "icon": "Sparkles",
        "title": "Culinária Criativa com empratamento",
        "description": "Cada receita entrega instruções de empratamento profissional: composição, paleta, garnish, loiça, vista (de cima, 3/4, frontal)."
      },
      {
        "icon": "BookOpen",
        "title": "Imagem como referência, não foto final",
        "description": "A imagem de IA é o guia visual: contraste de paleta, volume, textura, loiça. A foto definitiva da ficha de custo tira você com o seu prato real."
      },
      {
        "icon": "Calendar",
        "title": "Gerador de Pins Pinterest",
        "description": "O Pinterest captura tráfego orgânico estável para fotografia gastronómica."
      },
      {
        "icon": "Sparkles",
        "title": "InstaFlow AI Pro",
        "description": "Instagram com calendário editorial e composições adaptadas ao feed."
      },
      {
        "icon": "BarChart3",
        "title": "MenuDish Local SEO",
        "description": "Imagens adaptadas ao Glovo, Uber Eats, Just Eat e plataformas com critério profissional para mais cliques."
      },
      {
        "icon": "CheckSquare",
        "title": "Pro Prompts eBook",
        "description": "300+ prompts profissionais para fotografia gastronómica: estilo, paleta, composição, mood."
      },
      {
        "icon": "Image",
        "title": "Variantes e pré-preparações",
        "description": "O GastroIMG gera imagens de variantes: empratamentos alternativos, pré-preparações, mise en place, não só prato final."
      },
      {
        "icon": "BookOpen",
        "title": "BlogPost SEO Gen+",
        "description": "Artigos SEO sobre técnica fotográfica com imagens de referência para tráfego orgânico."
      }
    ],
    "workflowTitle": "Como Fazer Fotografia Gastronómica em 4 Passos",
    "workflow": [
      "1. Culinária Criativa — desenvolve o prato. O agente de IA entrega receita + ficha de custo + instruções de empratamento profissional (composição, paleta, loiça, vista).",
      "2. GastroIMG Gen+ — gera imagem de referência profissional com prompt otimizado: paleta quente, loiça rústica, vista de cima, microgreens. Itera até ter a imagem objetivo clara.",
      "3. Cozinha o prato real com a imagem de referência à frente: mesmo empratamento, paleta, garnish. A foto definitiva da ficha de custo e da carta tira você com o seu prato empratado real.",
      "4. InstaFlow AI Pro + MenuDish + Gerador de Pins Pinterest — adapta a imagem final a cada canal (Instagram, Glovo, web, carta) com critério profissional."
    ],
    "productsTitle": "Modelos e Kits Recomendados para Fotografia Gastronómica",
    "productIds": [
      "pro-prompts-ebook",
      "kit-escandallos",
      "pack-appcc",
      "kit-inventario",
      "kit-tareas",
      "kit-gestion-personal"
    ],
    "testimonialQuote": "O GastroIMG Gen+ mudou-me o fluxo de fotografia. Antes fazia sessões de food styling sem critério claro, agora gero a imagem de referência profissional com IA, valido paleta e composição com a equipa, e depois tiro a foto definitiva com o meu prato real. As sessões baixam 70 % em tempo e a consistência visual do Instagram + Glovo + web é agora profissional.",
    "testimonialAuthor": "Carmen Vera",
    "testimonialRole": "Chef e proprietária, restaurante com presença digital forte",
    "faqTitle": "Perguntas Frequentes sobre Fotografia Gastronómica com IA",
    "faqs": [
      {
        "q": "A imagem de IA é a foto definitiva do prato?",
        "a": "Não. A imagem de IA é de referência visual para validar empratamento, paleta, loiça e composição antes de cozinhar. A foto definitiva da ficha de custo, carta ou ficha técnica tira você com o seu prato real empratado."
      },
      {
        "q": "Serve para qualquer estilo de cozinha?",
        "a": "Sim. O GastroIMG Gen+ adapta o estilo: alta cozinha com minimalismo, casual com calor, mediterrâneo, asiático, latino-americano, fine dining premium."
      },
      {
        "q": "Cobre formatos para Instagram, Glovo, web e carta?",
        "a": "Sim. A imagem base adapta-se a 1:1 (Instagram), 4:5 (feed), 16:9 (carta digital), 9:16 (Stories), 4:3 (Glovo, Uber Eats) com critério profissional."
      },
      {
        "q": "Gera variantes e pré-preparações, não só prato final?",
        "a": "Sim. O GastroIMG Gen+ gera imagens de variantes: empratamentos alternativos, mise en place, pré-preparações, ingredientes em bruto, não só prato final. Útil para storytelling de processo."
      },
      {
        "q": "Como é que me ajuda com captação local em delivery?",
        "a": "O MenuDish Local SEO + GastroIMG Gen+ geram imagens profissionais para Glovo, Uber Eats, Just Eat com critério que aumenta o CTR. Melhor foto = mais cliques e melhor ranking."
      }
    ],
    "ctaTitle": "A sua fotografia gastronómica com critério profissional.",
    "ctaSubtitle": "Comece com o onboarding de 2 minutos. Plano Membro por 10 € por mês com 10.000 créditos.",
    "seo": {
      "title": "Como Fazer Fotografia Gastronómica com IA: Imagem de Referência e Foto Final | AI Chef Pro",
      "description": "Suite de IA para fotografia gastronómica: o GastroIMG Gen+ gera imagem de referência, depois tira a foto definitiva com o seu prato real. Comece hoje.",
      "keywords": "fotografia gastronómica IA, GastroIMG Gen+, food photography IA, imagem referência prato, foto prato delivery",
      "ogImage": "https://aichef.pro/og/use-cases/task-foto-gastronomica-con-ia.jpg"
    },
    "personalizationTitle": "Personalizado ao Seu Estilo desde o Primeiro Minuto",
    "personalizationBody": "O AI Chef Pro arranca com «Quem Sou Eu?»: conta estilo de cozinha, paleta de marca, loiça e canais prioritários (Instagram, Glovo, web, carta). O GastroIMG Gen+ adapta o estilo visual à sua marca.",
    "appsTitle": "Os Agentes de IA que Usa para Fotografia Gastronómica",
    "apps": [
      {
        "name": "GastroIMG Gen+",
        "category": "Gastro Conhecimento",
        "description": "Agente especializado em fotografia gastronómica IA."
      },
      {
        "name": "Culinária Criativa",
        "category": "Criatividade Culinária",
        "description": "Instruções de empratamento profissional para cada receita."
      },
      {
        "name": "Pastelaria Criativa",
        "category": "Criatividade Culinária",
        "description": "Empratamento de sobremesas com técnica francesa."
      },
      {
        "name": "Gelataria Criativa",
        "category": "Criatividade Culinária",
        "description": "Empratamento de gelados e semifrios com técnica."
      },
      {
        "name": "Pro Prompts eBook",
        "category": "Conteúdos e Redes Sociais",
        "description": "300+ prompts profissionais para fotografia gastronómica."
      },
      {
        "name": "InstaFlow AI Pro",
        "category": "Conteúdos e Redes Sociais",
        "description": "Instagram com calendário editorial e formatos adaptados."
      },
      {
        "name": "MenuDish Local SEO",
        "category": "Conteúdos e Redes Sociais",
        "description": "Imagens otimizadas para Glovo, Uber Eats, Just Eat."
      },
      {
        "name": "Gerador de Pins Pinterest",
        "category": "Conteúdos e Redes Sociais",
        "description": "O Pinterest captura tráfego orgânico estável."
      },
      {
        "name": "BlogPost SEO Gen+",
        "category": "Conteúdos e Redes Sociais",
        "description": "Artigos SEO com imagens de referência."
      },
      {
        "name": "Gastro Calendar",
        "category": "Conteúdos e Redes Sociais",
        "description": "Planeamento de sessões por temporada."
      },
      {
        "name": "Sonar Deep Research",
        "category": "Modelos de IA + LLM",
        "description": "Research sobre tendências visuais de referências."
      },
      {
        "name": "Coach Mental",
        "category": "Ferramentas e Utilitários",
        "description": "Coaching para liderança criativa."
      }
    ],
    "metrics": [
      {
        "value": "−70 %",
        "label": "tempo de sessões de food styling"
      },
      {
        "value": "×3",
        "label": "engagement no Instagram com GastroIMG"
      },
      {
        "value": "+CTR",
        "label": "melhor foto = mais cliques em delivery"
      },
      {
        "value": "12+",
        "label": "agentes para fotografia gastronómica"
      }
    ],
    "beforeAfter": {
      "beforeTitle": "Sem AI Chef Pro",
      "beforeItems": [
        "Sessões de food styling sem imagem de referência clara",
        "Sem critério partilhado entre chef e fotógrafo",
        "Alterações de carta requerem nova sessão completa",
        "Imagem inconsistente entre Instagram, Glovo e web",
        "Sem variantes nem pré-preparações para storytelling"
      ],
      "afterTitle": "Com AI Chef Pro",
      "afterItems": [
        "O GastroIMG Gen+ gera imagem de referência profissional",
        "Critério partilhado validado antes de cozinhar",
        "Alterações de carta: nova imagem de IA em minutos",
        "Imagem consistente entre todos os canais",
        "Variantes e pré-preparações para storytelling completo"
      ]
    },
    "galleryTitle": "Como Funciona a Fotografia Gastronómica com IA",
    "gallerySubtitle": "O que vai coordenar com o AI Chef Pro: hero, prato, câmara, ferramentas e equipamento. Imagens geradas com IA como referência visual do conceito.",
    "galleryImages": [
      "/lovable-uploads/ai-gallery/use-case-task-foto-gastronomica-hero.jpg",
      "/lovable-uploads/ai-gallery/use-case-task-foto-gastronomica-plato.jpg",
      "/lovable-uploads/ai-gallery/use-case-task-foto-gastronomica-camera.jpg",
      "/lovable-uploads/ai-gallery/use-case-task-foto-gastronomica-tools.jpg",
      "/lovable-uploads/ai-gallery/use-case-task-foto-gastronomica-comparison.jpg",
      "/lovable-uploads/ai-gallery/use-case-task-foto-gastronomica-team.jpg"
    ]
  }
};
