import { useState, useEffect } from 'react';
import { Helmet } from 'react-helmet-async';
import {
  Download, Loader2, ArrowLeft,
  BookOpen, FileText, Building2, Banknote,
  CalendarRange, Calculator, TrendingUp, ClipboardCheck,
  Wrench, Users, GraduationCap, ScrollText, Star,
} from 'lucide-react';
import { useAuth } from '@/hooks/useAuth';
import SaasDiscoveryBanner from '@/components/shared/SaasDiscoveryBanner';
import ProductChangelog, { ProductVersionBadge } from '@/components/shared/ProductChangelog';
import LogoBadge from '@/components/shared/LogoBadge';
import WhatsAppProductSupport from '@/components/shared/WhatsAppProductSupport';

// 13 claves, las MISMAS que PRODUCT_FILES de netlify/functions/get-download-urls.ts y
// que el mapa `files` de src/data/productos-digitales-config.ts. Cualquier desajuste
// lo caza gate-flujo-postpago.py --offline --only guia-pasteleria-obrador.
const SECTIONS = [
  {
    title: 'Guía Principal',
    templates: [
      { key: 'guia-pdf', icon: BookOpen, title: 'Guía Completa (PDF)', desc: '20 capítulos y un anexo normativo con fecha de corte, con las tablas construidas desde las herramientas Excel y desde la norma citada.', ext: '.pdf' },
      { key: 'guia-docx', icon: FileText, title: 'Guía Completa (DOCX Editable)', desc: 'Mismo contenido en formato editable para anotar, adaptarlo a tu proyecto y llevártelo a la reunión con el técnico.', ext: '.docx' },
    ],
  },
  {
    title: 'Herramientas Excel (8)',
    templates: [
      { key: 'capacidad-obrador', icon: Building2, title: 'Capacidad de Obrador y Local', desc: 'Zonas y metros, capacidad por equipo, cuál es tu cuello de botella, piezas al día del conjunto y la ficha de visita al local con su semáforo eliminatorio.', ext: '.xlsx' },
      { key: 'capex-pasteleria', icon: Banknote, title: 'Calculadora de Coste de Apertura', desc: 'Inversión por bloque y por variante de formato, la columna de impuesto línea a línea, la comparación de traspaso frente a obra nueva a cinco años y el colchón de tesorería.', ext: '.xlsx' },
      { key: 'estacionalidad-picos', icon: CalendarRange, title: 'Estacionalidad y Picos del Año', desc: 'Los seis picos con su peso sobre el año, el déficit de capacidad frente a tu obrador, el coste del refuerzo y la tesorería que inmoviliza el stock de temporada.', ext: '.xlsx' },
      { key: 'carta-escandallo', icon: Calculator, title: 'Carta de Apertura y Escandallo', desc: 'Escandallo por tanda de 30 referencias con la hora de obrador imputada, mix y ticket medio, decisión de surtido y la hoja de decisión de huevo y temperatura con su artículo.', ext: '.xlsx' },
      { key: 'plan-financiero', icon: TrendingUp, title: 'Plan Financiero a 3 Años', desc: 'Cuenta de resultados con estacionalidad mensual y rampa de arranque, punto de equilibrio, escenarios, personal con seguridad social, tesorería a 12 meses, financiación y margen por canal.', ext: '.xlsx' },
      { key: 'checklist-legal', icon: ClipboardCheck, title: 'Checklist Legal y de Licencias', desc: 'Seis fases con contador de avance, árbol de registro sanitario, el árbol de la venta a otros comercios, la ruta doméstica, el registro de formación y el cronograma con su ruta crítica.', ext: '.xlsx' },
      { key: 'checklist-equipamiento', icon: Wrench, title: 'Checklist de Equipamiento y Proveedores', desc: 'Equipamiento con horquilla y prioridad, columna de impuesto y plazo de entrega, proveedores verificados con su enlace, desviación frente al presupuesto y plazo crítico.', ext: '.xlsx' },
      { key: 'turnos-personal', icon: Users, title: 'Turnos y Coste de Personal', desc: 'Turnos semanales por persona, horas y coste mes y año con la seguridad social dentro, aviso si se pasa de jornada, coste del refuerzo de pico y plan de contratación.', ext: '.xlsx' },
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

export default function GuiaPasteleriaDashboard() {
  const { token } = useAuth('guia-pasteleria-obrador-jwt');
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
        <title>Cómo Montar una Pastelería — Dashboard | AI Chef Pro</title>
        <meta name="robots" content="noindex, nofollow" />
      </Helmet>
      <div className="min-h-screen bg-[#0a0a0a]">
        <SaasDiscoveryBanner />
        <header className="sticky top-0 z-50 bg-[#0a0a0a]/95 backdrop-blur-sm border-b border-white/10">
          <div className="max-w-6xl mx-auto px-4 h-14 flex items-center justify-between">
            <a href="/guia-pasteleria-obrador" className="flex items-center gap-2 text-gray-400 hover:text-white transition-colors text-sm"><ArrowLeft className="w-4 h-4" />Cómo Montar una Pastelería</a>
            <div className="flex items-center gap-2"><Star className="w-5 h-5 text-[#FFD700]" /><span className="text-white font-bold text-sm">Tu Dashboard</span></div>
            <a href="https://aichef.pro" className="text-gray-500 hover:text-[#FFD700] text-sm transition-colors">aichef.pro</a>
          </div>
        </header>
        <section className="py-12 md:py-16 px-4 text-center">
          <LogoBadge />
          <h1 className="text-3xl md:text-5xl font-extrabold text-white mb-3 mt-4">Cómo Montar una <span className="text-[#FFD700]">Pastelería</span></h1>
          <div className="mb-3">
            <ProductVersionBadge productId="guia-pasteleria-obrador" />
          </div>
          <p className="text-gray-400 text-base md:text-lg max-w-2xl mx-auto">Tu guía completa + 8 herramientas Excel + los dos bonus, listos para descargar.</p>
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

        <ProductChangelog productId="guia-pasteleria-obrador" />
        <section className="py-10 px-4 border-t border-white/10">
          <div className="max-w-3xl mx-auto text-center space-y-4">
            <p className="text-gray-400 text-sm mb-3">El día que abras, esto es lo que vas a usar cada mañana</p>
            <div className="flex flex-col sm:flex-row items-center justify-center gap-4">
              <a href="/kit-tareas-pasteleria" className="inline-block px-6 py-3 border border-[#FFD700]/50 text-[#FFD700] font-bold rounded-xl hover:bg-[#FFD700]/10 transition-all text-sm">Kit Tareas Pastelería — 12 EUR</a>
              <a href="/pack-appcc" className="inline-block px-6 py-3 border border-[#FFD700]/50 text-[#FFD700] font-bold rounded-xl hover:bg-[#FFD700]/10 transition-all text-sm">Pack Plantillas APPCC — 14 EUR</a>
            </div>
          </div>
        </section>
        <footer className="py-8 px-4 border-t border-white/10">
          <div className="max-w-4xl mx-auto text-center">
            <p className="text-gray-500 text-sm mb-2">© 2026 AI Chef Pro · Cómo Montar una Pastelería · Todos los derechos reservados</p>
          </div>
        </footer>
        <WhatsAppProductSupport />
      </div>
    </>
  );
}
