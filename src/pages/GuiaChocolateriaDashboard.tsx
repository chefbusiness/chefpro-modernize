import { useState, useEffect } from 'react';
import { Helmet } from 'react-helmet-async';
import {
  Download, Loader2, ArrowLeft,
  BookOpen, FileText, Building2, Banknote,
  Coins, Calculator, Timer, CalendarRange,
  TrendingUp, ClipboardCheck, Wrench,
  GraduationCap, ScrollText, Star,
} from 'lucide-react';
import { useAuth } from '@/hooks/useAuth';
import SaasDiscoveryBanner from '@/components/shared/SaasDiscoveryBanner';
import ProductChangelog, { ProductVersionBadge } from '@/components/shared/ProductChangelog';
import LogoBadge from '@/components/shared/LogoBadge';
import WhatsAppProductSupport from '@/components/shared/WhatsAppProductSupport';

// 14 claves (D49 de la SPEC), las MISMAS que PRODUCT_FILES de netlify/functions/get-download-urls.ts
// y que el mapa `files` de src/data/productos-digitales-config.ts. Cualquier desajuste lo caza
// gate-flujo-postpago.py --offline --only guia-chocolateria-obrador.
const SECTIONS = [
  {
    title: 'Guía Principal',
    templates: [
      { key: 'guia-pdf', icon: BookOpen, title: 'Guía Completa (PDF)', desc: '20 capítulos y un anexo normativo con fecha de corte, con las tablas construidas desde los libros de Excel y desde la norma citada.', ext: '.pdf' },
      { key: 'guia-docx', icon: FileText, title: 'Guía Completa (DOCX Editable)', desc: 'Mismo contenido en formato editable para anotar, adaptarlo a tu proyecto y llevártelo a la reunión con el técnico.', ext: '.docx' },
    ],
  },
  {
    title: 'Herramientas Excel (9)',
    templates: [
      { key: 'capacidad-clima', icon: Building2, title: 'Capacidad de Obrador y Clima', desc: 'Zonas y metros, clima del obrador con su semáforo de coherencia frente al agosto de tu ciudad, capacidad por equipo, cuál es tu cuello de botella y la ficha de visita al local con su semáforo eliminatorio.', ext: '.xlsx' },
      { key: 'capex-chocolateria', icon: Banknote, title: 'Calculadora de Coste de Apertura', desc: 'Inversión por bloque y por variante de formato, la columna de impuesto línea a línea, traspaso frente a obra nueva a cinco años y el fondo de maniobra separado de la inversión.', ext: '.xlsx' },
      { key: 'sensibilidad-cacao', icon: Coins, title: 'Sensibilidad al Precio del Cacao', desc: 'El precio de cada cobertura en sus dos bases, escenarios de subida, food cost resultante, cuánto tendrías que subir el PVP para mantener el margen y qué referencia se rompe primero.', ext: '.xlsx' },
      { key: 'carta-escandallo', icon: Calculator, title: 'Carta de Apertura y Escandallo', desc: 'Escandallo por molde y tanda con la hora de obrador imputada, merma de templado recuperable y no recuperable, unidad frente a caja, mix y ticket medio, y qué puedes llamar legalmente a cada referencia.', ext: '.xlsx' },
      { key: 'vida-util-rellenos', icon: Timer, title: 'Vida Útil de Rellenos y Rotación', desc: 'Tipo de relleno y actividad de agua, la vida útil que declaras tú, si la referencia se despacha envasada con etiqueta o a granel, temperatura y humedad de vitrina, lote económico y merma por caducidad en euros al año.', ext: '.xlsx' },
      { key: 'campanas-valle', icon: CalendarRange, title: 'Campañas y Valle del Año', desc: 'Las campañas del año con su peso sobre la facturación, el déficit de capacidad del pico, el coste del refuerzo, la tesorería que inmoviliza el stock de temporada y qué haces en agosto.', ext: '.xlsx' },
      { key: 'plan-financiero', icon: TrendingUp, title: 'Plan Financiero a 3 Años', desc: 'Cuenta de resultados con estacionalidad mensual y rampa de arranque, punto de equilibrio por formato, escenarios, personal con seguridad social, tesorería a 12 meses, financiación, margen por canal y los talleres.', ext: '.xlsx' },
      { key: 'checklist-legal', icon: ClipboardCheck, title: 'Checklist Legal, Licencias y Cacao', desc: 'Seis fases con contador de avance, árbol de registro sanitario, suministro a otros minoristas, cadmio y analíticas, qué papel te toca en la norma del cacao y el cronograma con su ruta crítica.', ext: '.xlsx' },
      { key: 'checklist-equipamiento', icon: Wrench, title: 'Checklist de Equipamiento y Proveedores', desc: 'Equipamiento con horquilla, prioridad, impuesto y plazo de entrega, si tu proveedor de cobertura y cacao es operador o comerciante, la desviación frente al presupuesto y la tabla de clientes a los que suministras.', ext: '.xlsx' },
    ],
  },
  {
    title: 'Bonus (3)',
    templates: [
      { key: 'business-plan-docx', icon: ScrollText, title: 'Business Plan Modelo Relleno (DOCX Editable)', desc: 'El caso completo en el formato que pide un banco: resumen ejecutivo, mercado, concepto y carta, operaciones, plan financiero a tres años y riesgos con escenarios.', ext: '.docx' },
      { key: 'bonus-decisiones-pdf', icon: GraduationCap, title: '12 Decisiones de Apertura Resueltas (PDF)', desc: 'Cada decisión con su contexto, sus opciones, el criterio, la celda del Excel que la resuelve y la norma con su fecha cuando la hay.', ext: '.pdf' },
      { key: 'bonus-decisiones-docx', icon: FileText, title: '12 Decisiones de Apertura Resueltas (DOCX Editable)', desc: 'Mismo bonus en formato editable para trabajarlo con tu socio, tu gestor o tu técnico.', ext: '.docx' },
    ],
  },
];

export default function GuiaChocolateriaDashboard() {
  const { token } = useAuth('guia-chocolateria-obrador-jwt');
  const [files, setFiles] = useState<Record<string, string>>({});
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    if (!token) return;
    fetch('/.netlify/functions/get-download-urls', { headers: { Authorization: `Bearer ${token}` } })
      .then((r) => r.json())
      .then((data) => { if (data.files) setFiles(data.files); })
      .catch(() => {})
      .finally(() => setLoading(false));
  }, [token]);

  return (
    <>
      <Helmet>
        <title>Cómo Montar una Chocolatería Boutique & Atelier — Dashboard | AI Chef Pro</title>
        <meta name="robots" content="noindex, nofollow" />
      </Helmet>
      <div className="min-h-screen bg-[#0a0a0a]">
        <SaasDiscoveryBanner />
        <header className="sticky top-0 z-50 bg-[#0a0a0a]/95 backdrop-blur-sm border-b border-white/10">
          <div className="max-w-6xl mx-auto px-4 h-14 flex items-center justify-between">
            <a href="/guia-chocolateria-obrador" className="flex items-center gap-2 text-gray-400 hover:text-white transition-colors text-sm"><ArrowLeft className="w-4 h-4" />Cómo Montar una Chocolatería Boutique & Atelier</a>
            <div className="flex items-center gap-2"><Star className="w-5 h-5 text-[#FFD700]" /><span className="text-white font-bold text-sm">Tu Dashboard</span></div>
            <a href="https://aichef.pro" className="text-gray-500 hover:text-[#FFD700] text-sm transition-colors">aichef.pro</a>
          </div>
        </header>
        <section className="py-12 md:py-16 px-4 text-center">
          <LogoBadge />
          <h1 className="text-3xl md:text-5xl font-extrabold text-white mb-3 mt-4">Cómo Montar una <span className="text-[#FFD700]">Chocolatería Boutique & Atelier</span></h1>
          <div className="mb-3">
            <ProductVersionBadge productId="guia-chocolateria-obrador" />
          </div>
          <p className="text-gray-400 text-base md:text-lg max-w-2xl mx-auto">Tu guía completa + 9 libros de Excel + los dos bonus, listos para descargar.</p>
        </section>

        {SECTIONS.map((section) => (
          <section key={section.title} className="pb-12 px-4">
            <div className="max-w-5xl mx-auto">
              <p className="text-[#FFD700] text-sm font-bold uppercase tracking-wider mb-4">{section.title}</p>
              <div className="grid sm:grid-cols-2 lg:grid-cols-3 gap-4">
                {section.templates.map((tpl) => {
                  const Icon = tpl.icon;
                  const url = files[tpl.key];
                  return (
                    <div key={tpl.key} className="rounded-xl p-5 bg-white/5 border border-white/10 hover:border-[#FFD700]/30 transition-all">
                      <div className="flex items-start gap-3 mb-3">
                        <div className="w-10 h-10 rounded-lg bg-[#FFD700]/10 flex items-center justify-center flex-shrink-0"><Icon className="w-5 h-5 text-[#FFD700]" /></div>
                        <div><h3 className="text-white font-bold text-sm leading-tight">{tpl.title}</h3><p className="text-gray-500 text-xs mt-0.5">{tpl.ext}</p></div>
                      </div>
                      <p className="text-gray-400 text-sm mb-4 leading-relaxed">{tpl.desc}</p>
                      {loading ? <Loader2 className="w-5 h-5 text-gray-500 animate-spin" /> : url ? (
                        <a href={url} target="_blank" rel="noopener noreferrer" className="inline-flex items-center gap-2 px-4 py-2 rounded-lg text-sm font-bold border border-[#FFD700]/50 text-[#FFD700] hover:bg-[#FFD700]/10 transition-all">
                          <Download className="w-4 h-4" />Descargar
                        </a>
                      ) : <span className="text-gray-500 text-sm">Disponible pronto</span>}
                    </div>
                  );
                })}
              </div>
            </div>
          </section>
        ))}

        <ProductChangelog productId="guia-chocolateria-obrador" />
        <section className="py-10 px-4 border-t border-white/10">
          <div className="max-w-3xl mx-auto text-center space-y-4">
            <p className="text-gray-400 text-sm mb-3">El Kit de Tareas te dice qué hacer cada día cuando ya has abierto. Esta guía es todo lo que hay que decidir antes.</p>
            <div className="flex flex-col sm:flex-row items-center justify-center gap-4">
              <a href="/kit-tareas-chocolateria" className="inline-block px-6 py-3 border border-[#FFD700]/50 text-[#FFD700] font-bold rounded-xl hover:bg-[#FFD700]/10 transition-all text-sm">Kit Tareas Chocolatería — 12 EUR</a>
              <a href="/pack-appcc" className="inline-block px-6 py-3 border border-[#FFD700]/50 text-[#FFD700] font-bold rounded-xl hover:bg-[#FFD700]/10 transition-all text-sm">Pack Plantillas APPCC — 14 EUR</a>
            </div>
          </div>
        </section>
        <footer className="py-8 px-4 border-t border-white/10">
          <div className="max-w-4xl mx-auto text-center">
            <p className="text-gray-500 text-sm mb-2">© 2026 AI Chef Pro · Cómo Montar una Chocolatería Boutique & Atelier · Todos los derechos reservados</p>
          </div>
        </footer>
        <WhatsAppProductSupport />
      </div>
    </>
  );
}
