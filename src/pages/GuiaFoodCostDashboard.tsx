import { useState, useEffect } from 'react';
import { Helmet } from 'react-helmet-async';
import {
  Download, Loader2, FileSpreadsheet, ArrowLeft,
  BookOpen, FileText, Calculator, BarChart3,
  Scale, Wine, Truck, Target, CalendarRange,
  GraduationCap, Star,
} from 'lucide-react';
import { useAuth } from '@/hooks/useAuth';
import SaasDiscoveryBanner from '@/components/shared/SaasDiscoveryBanner';
import ProductChangelog, { ProductVersionBadge } from '@/components/shared/ProductChangelog';
import LogoBadge from '@/components/shared/LogoBadge';
import WhatsAppProductSupport from '@/components/shared/WhatsAppProductSupport';

const SECTIONS = [
  {
    title: 'Guía Principal',
    templates: [
      { key: 'guia-pdf', icon: BookOpen, title: 'Guía Completa (PDF)', desc: '20 capítulos con las tablas construidas desde las herramientas Excel.', ext: '.pdf' },
      { key: 'guia-docx', icon: FileText, title: 'Guía Completa (DOCX Editable)', desc: 'Mismo contenido en formato editable para anotar y adaptar.', ext: '.docx' },
    ],
  },
  {
    title: 'Herramientas Excel (8)',
    templates: [
      { key: 'ficha-escandallo', icon: FileSpreadsheet, title: 'Ficha de Escandallo Base', desc: 'Coste por ración con merma línea a línea y PVP objetivo con IVA.', ext: '.xlsx' },
      { key: 'rendimiento-mermas', icon: Scale, title: 'Rendimiento y Mermas por Producto', desc: 'Test de rendimiento, merma de cocción y tu propia tabla de mermas.', ext: '.xlsx' },
      { key: 'precio-objetivo', icon: Calculator, title: 'Precio Objetivo Multi-Método', desc: 'Cuatro formas de fijar el precio de venta de cada plato y su food cost.', ext: '.xlsx' },
      { key: 'matriz-multimetodo', icon: BarChart3, title: 'Matriz Multi-Método de Carta', desc: 'Kasavana-Smith, Miller, Pavesic y Goal Value con hoja de discrepancias.', ext: '.xlsx' },
      { key: 'simulador-multicanal', icon: Truck, title: 'Simulador de Repricing Multicanal', desc: 'Sala, take away y delivery con comisión, packaging e IVA por canal.', ext: '.xlsx' },
      { key: 'carta-bebidas', icon: Wine, title: 'Carta de Bebidas y Beverage Cost', desc: 'Vinos, cervezas, destilados y cócteles con coste por copa y margen.', ext: '.xlsx' },
      { key: 'cuadro-prime-cost', icon: Target, title: 'Cuadro de Mando Prime Cost', desc: 'Food cost y coste de personal mes a mes con semáforo frente al objetivo.', ext: '.xlsx' },
      { key: 'plan-90-dias', icon: CalendarRange, title: 'Plan de Acción 90 Días', desc: 'Decisiones con responsable y fecha, calendario de 13 semanas y KPI.', ext: '.xlsx' },
    ],
  },
  {
    title: 'Bonus (2)',
    templates: [
      { key: 'bonus-pdf', icon: GraduationCap, title: '12 Ejercicios Resueltos (PDF)', desc: 'Enunciado con datos, resolución paso a paso, tabla y lectura del resultado.', ext: '.pdf' },
      { key: 'bonus-docx', icon: FileText, title: '12 Ejercicios Resueltos (DOCX Editable)', desc: 'Mismo bonus en formato editable para trabajarlo con tu equipo.', ext: '.docx' },
    ],
  },
];

export default function GuiaFoodCostDashboard() {
  const { token } = useAuth('guia-food-cost-ingenieria-menu-jwt');
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
        <title>Guía Food Cost + Ingeniería de Menú — Dashboard | AI Chef Pro</title>
        <meta name="robots" content="noindex, nofollow" />
      </Helmet>
      <div className="min-h-screen bg-[#0a0a0a]">
        <SaasDiscoveryBanner />
        <header className="sticky top-0 z-50 bg-[#0a0a0a]/95 backdrop-blur-sm border-b border-white/10">
          <div className="max-w-6xl mx-auto px-4 h-14 flex items-center justify-between">
            <a href="/guia-food-cost-ingenieria-menu" className="flex items-center gap-2 text-gray-400 hover:text-white transition-colors text-sm"><ArrowLeft className="w-4 h-4" />Guía Food Cost + Ingeniería de Menú</a>
            <div className="flex items-center gap-2"><Star className="w-5 h-5 text-[#FFD700]" /><span className="text-white font-bold text-sm">Tu Dashboard</span></div>
            <a href="https://aichef.pro" className="text-gray-500 hover:text-[#FFD700] text-sm transition-colors">aichef.pro</a>
          </div>
        </header>
        <section className="py-12 md:py-16 px-4 text-center">
          <LogoBadge />
          <h1 className="text-3xl md:text-5xl font-extrabold text-white mb-3 mt-4">Food Cost + <span className="text-[#FFD700]">Ingeniería de Menú</span></h1>
          <div className="mb-3">
            <ProductVersionBadge productId="guia-food-cost-ingenieria-menu" />
          </div>
          <p className="text-gray-400 text-base md:text-lg max-w-2xl mx-auto">Tu guía completa + 8 herramientas Excel + el bonus de ejercicios, listos para descargar.</p>
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

        <ProductChangelog productId="guia-food-cost-ingenieria-menu" />
        <section className="py-10 px-4 border-t border-white/10">
          <div className="max-w-3xl mx-auto text-center space-y-4">
            <p className="text-gray-400 text-sm mb-3">¿Ya tienes la guía? Completa tu toolkit</p>
            <div className="flex flex-col sm:flex-row items-center justify-center gap-4">
              <a href="/kit-escandallos" className="inline-block px-6 py-3 border border-[#FFD700]/50 text-[#FFD700] font-bold rounded-xl hover:bg-[#FFD700]/10 transition-all text-sm">Kit de Escandallos Pro — 12 EUR</a>
              <a href="/kit-gestion-personal" className="inline-block px-6 py-3 border border-[#FFD700]/50 text-[#FFD700] font-bold rounded-xl hover:bg-[#FFD700]/10 transition-all text-sm">Kit Gestión de Personal — 14 EUR</a>
            </div>
          </div>
        </section>
        <footer className="py-8 px-4 border-t border-white/10">
          <div className="max-w-4xl mx-auto text-center">
            <p className="text-gray-500 text-sm mb-2">© 2026 AI Chef Pro · Guía Food Cost + Ingeniería de Menú · Todos los derechos reservados</p>
          </div>
        </footer>
        <WhatsAppProductSupport />
      </div>
    </>
  );
}
