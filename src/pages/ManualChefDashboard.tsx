import { useState, useEffect } from 'react';
import { Helmet } from 'react-helmet-async';
import {
  Download, Loader2, ArrowLeft,
  BookOpen, FileText, BarChart3, CalendarRange,
  ScrollText, Users, UtensilsCrossed, ClipboardList,
  ClipboardCheck, GraduationCap, Star,
} from 'lucide-react';
import { useAuth } from '@/hooks/useAuth';
import SaasDiscoveryBanner from '@/components/shared/SaasDiscoveryBanner';
import ProductChangelog, { ProductVersionBadge } from '@/components/shared/ProductChangelog';
import LogoBadge from '@/components/shared/LogoBadge';
import WhatsAppProductSupport from '@/components/shared/WhatsAppProductSupport';

const SECTIONS = [
  {
    title: 'Manual Principal',
    templates: [
      { key: 'manual-pdf', icon: BookOpen, title: 'Manual Completo (PDF)', desc: '20 capítulos con las tablas construidas desde las herramientas Excel y desde la norma citada.', ext: '.pdf' },
      { key: 'manual-docx', icon: FileText, title: 'Manual Completo (DOCX Editable)', desc: 'Mismo contenido en formato editable para anotar y adaptarlo a tu cocina.', ext: '.docx' },
    ],
  },
  {
    title: 'Herramientas Excel (7)',
    templates: [
      { key: 'cuadro-cocina', icon: BarChart3, title: 'Cuadro de Mando de Cocina', desc: '52 semanas ISO con merma y producción por partida, tiempos de pase, incidencias de alérgenos, horas de cocina, hoja de definiciones de los KPI y comparativa entre unidades.', ext: '.xlsx' },
      { key: 'planificacion-produccion', icon: CalendarRange, title: 'Planificación de Producción Semanal', desc: 'Previsión de cubiertos, producción por partida, lista de producción diaria imprimible y ajuste por desviación para decidir cuánto se produce hoy.', ext: '.xlsx' },
      { key: 'ficha-tecnica', icon: ScrollText, title: 'Ficha Técnica de Proceso', desc: 'Receta estándar de proceso: pasos, tiempos, punto, temperatura de servicio, montaje, alérgenos de proceso, conservación, versión y su índice de fichas.', ext: '.xlsx' },
      { key: 'brigada-evaluacion', icon: Users, title: 'Brigada: Puestos y Evaluación', desc: 'Organigrama por partidas, 10 fichas de puesto con las funciones del convenio, matriz RACI, rúbrica de competencias técnicas, prueba práctica y plan de desarrollo individual.', ext: '.xlsx' },
      { key: 'desarrollo-carta', icon: UtensilsCrossed, title: 'Desarrollo de Carta y Control de Calidad', desc: 'Calendario de temporada de probar a lanzar, registro de pruebas de plato y control de calidad del pase, con alerta si un plato lleva demasiado sin ficha cerrada.', ext: '.xlsx' },
      { key: 'banquetes-testigo', icon: ClipboardList, title: 'Banquetes y Comidas Testigo', desc: 'Registro de comidas testigo con la alerta de obligatoriedad y la cuenta atrás de conservación, más la producción y la ficha de banquete con timing y personal.', ext: '.xlsx' },
      { key: 'auditoria-cocina', icon: ClipboardCheck, title: 'Auditoría Interna de Cocina', desc: 'Unos 50 puntos de control de la disciplina de cocina con puntuación, resumen por área, histórico, histórico por unidad y una hoja de estado normativo con fecha de corte.', ext: '.xlsx' },
    ],
  },
  {
    title: 'Bonus (2)',
    templates: [
      { key: 'bonus-pdf', icon: GraduationCap, title: '12 Situaciones Resueltas en Cocina (PDF)', desc: 'Situación con datos, qué NO hacer, protocolo, norma aplicable, herramienta usada y guion de la conversación cuando la hay.', ext: '.pdf' },
      { key: 'bonus-docx', icon: FileText, title: '12 Situaciones Resueltas en Cocina (DOCX Editable)', desc: 'Mismo bonus en formato editable para trabajarlo con tu brigada.', ext: '.docx' },
    ],
  },
];

export default function ManualChefDashboard() {
  const { token } = useAuth('manual-chef-ejecutivo-jwt');
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
        <title>Manual del Chef Ejecutivo — Dashboard | AI Chef Pro</title>
        <meta name="robots" content="noindex, nofollow" />
      </Helmet>
      <div className="min-h-screen bg-[#0a0a0a]">
        <SaasDiscoveryBanner />
        <header className="sticky top-0 z-50 bg-[#0a0a0a]/95 backdrop-blur-sm border-b border-white/10">
          <div className="max-w-6xl mx-auto px-4 h-14 flex items-center justify-between">
            <a href="/manual-chef-ejecutivo" className="flex items-center gap-2 text-gray-400 hover:text-white transition-colors text-sm"><ArrowLeft className="w-4 h-4" />Manual del Chef Ejecutivo</a>
            <div className="flex items-center gap-2"><Star className="w-5 h-5 text-[#FFD700]" /><span className="text-white font-bold text-sm">Tu Dashboard</span></div>
            <a href="https://aichef.pro" className="text-gray-500 hover:text-[#FFD700] text-sm transition-colors">aichef.pro</a>
          </div>
        </header>
        <section className="py-12 md:py-16 px-4 text-center">
          <LogoBadge />
          <h1 className="text-3xl md:text-5xl font-extrabold text-white mb-3 mt-4">Manual del <span className="text-[#FFD700]">Chef Ejecutivo</span></h1>
          <div className="mb-3">
            <ProductVersionBadge productId="manual-chef-ejecutivo" />
          </div>
          <p className="text-gray-400 text-base md:text-lg max-w-2xl mx-auto">Tu manual completo + 7 herramientas Excel + el bonus de situaciones resueltas, listos para descargar.</p>
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

        <ProductChangelog productId="manual-chef-ejecutivo" />
        <section className="py-10 px-4 border-t border-white/10">
          <div className="max-w-3xl mx-auto text-center space-y-4">
            <p className="text-gray-400 text-sm mb-3">Si diriges el negocio y la cocina, necesitas los dos</p>
            <div className="flex flex-col sm:flex-row items-center justify-center gap-4">
              <a href="/manual-manager-restaurante" className="inline-block px-6 py-3 border border-[#FFD700]/50 text-[#FFD700] font-bold rounded-xl hover:bg-[#FFD700]/10 transition-all text-sm">Manual del Manager de Restaurante</a>
              <a href="/pack-appcc" className="inline-block px-6 py-3 border border-[#FFD700]/50 text-[#FFD700] font-bold rounded-xl hover:bg-[#FFD700]/10 transition-all text-sm">Pack Plantillas APPCC — 14 EUR</a>
            </div>
          </div>
        </section>
        <footer className="py-8 px-4 border-t border-white/10">
          <div className="max-w-4xl mx-auto text-center">
            <p className="text-gray-500 text-sm mb-2">© 2026 AI Chef Pro · Manual del Chef Ejecutivo · Todos los derechos reservados</p>
          </div>
        </footer>
        <WhatsAppProductSupport />
      </div>
    </>
  );
}
