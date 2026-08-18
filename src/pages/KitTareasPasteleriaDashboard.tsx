import { useState, useEffect } from 'react';
import { Helmet } from 'react-helmet-async';
import {
  Download, Loader2, FileSpreadsheet, ArrowLeft,
  DoorOpen, Croissant, ClipboardList, Users,
  CalendarDays, PartyPopper, FileEdit, Megaphone, Calendar, Building2, Wallet,
  CalendarRange, Cake, ShieldAlert, Thermometer,
} from 'lucide-react';
import { useAuth } from '@/hooks/useAuth';
import SaasDiscoveryBanner from '@/components/shared/SaasDiscoveryBanner';
import SaasCrossSellBanners from '@/components/shared/SaasCrossSellBanners';
import ProductChangelog, { ProductVersionBadge } from '@/components/shared/ProductChangelog';
import LogoBadge from '@/components/shared/LogoBadge';
import WhatsAppProductSupport from '@/components/shared/WhatsAppProductSupport';

// ── Template metadata ────────────────────────────────────────────
interface TemplateCard {
  key: string;
  icon: typeof DoorOpen;
  title: string;
  desc: string;
  /** Marca «NUEVO v2.0» en la tarjeta (novedades de la última versión). */
  isNew?: boolean;
}

const TEMPLATES: TemplateCard[] = [
  { key: 'apertura-cierre', icon: DoorOpen, title: 'Apertura y Cierre', desc: '6 checklists: apertura y cierre de obrador, horno, vitrina y despacho.' },
  { key: 'partidas', icon: Croissant, title: 'Partidas de Producción', desc: 'Masas, fermentación, cremas, rellenos, decoración y montaje vitrina.' },
  { key: 'manager', icon: ClipboardList, title: 'Tareas del Manager', desc: 'Diario, semanal, mensual + handover de turno.' },
  { key: 'perfiles', icon: Users, title: 'Tareas por Perfil', desc: 'Jefe pastelero, oficial, ayudante, dependiente vitrina.' },
  { key: 'periodicas', icon: CalendarDays, title: 'Semanales y Mensuales', desc: 'Limpieza profunda, FIFO, mantenimiento hornos y amasadora.' },
  { key: 'eventos', icon: PartyPopper, title: 'Eventos y Festivos', desc: 'Navidad, Reyes, San Valentín, Semana Santa, Día de la Madre.' },
  { key: 'personalizable', icon: FileEdit, title: 'Plantilla Personalizable', desc: '3 plantillas en blanco para crear las tuyas.' },
  { key: 'apertura-negocio', icon: Building2, title: 'Apertura y Cierre del Negocio', desc: 'Tienda y obrador: vitrinas, etiquetado, encargos del día, sobrante y comprobaciones finales.' },
  { key: 'apertura-caja', icon: Wallet, title: 'Apertura y Cierre de Caja', desc: 'Fondo de caja, arqueo por denominación, cuadre con la Z y registro mensual con descuadre.' },
  { key: 'plan-produccion', icon: CalendarRange, title: 'Plan de Producción Semanal', desc: 'Previsión por producto y partida (Lun–Dom), producido vs vendido, merma en % y € y resumen semanal.', isNew: true },
  { key: 'encargos', icon: Cake, title: 'Control de Encargos', desc: 'Ficha de encargo imprimible con alérgenos, señal y pendiente, registro mensual y agenda de entregas.', isNew: true },
  { key: 'alergenos', icon: ShieldAlert, title: 'Alérgenos de Vitrina (14 UE)', desc: 'Matriz de partida con más de 30 productos (para verificar con tus fichas técnicas), carta de alérgenos, cartel para la tienda y etiquetas de vitrina.', isNew: true },
  { key: 'temperaturas', icon: Thermometer, title: 'Temperaturas, Recepción y Etiquetas', desc: 'Registro mensual de temperaturas por equipo, recepción de mercancía con criterios de rechazo y etiquetas de elaborado con vidas útiles.', isNew: true },
  { key: 'bonus-briefing', icon: Megaphone, title: 'BONUS: Briefing Servicio', desc: 'Plantilla de briefing diario del obrador.' },
  { key: 'bonus-calendario', icon: Calendar, title: 'BONUS: Calendario Anual', desc: '17 fechas clave de pastelería.' },
];

export default function KitTareasPasteleriaDashboard() {
  const { token } = useAuth('kit-tareas-pasteleria-jwt');
  const [files, setFiles] = useState<Record<string, string>>({});
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    if (!token) return;
    fetch('/.netlify/functions/get-download-urls', {
      headers: { Authorization: `Bearer ${token}` },
    })
      .then((r) => r.json())
      .then((data) => {
        if (data.files) setFiles(data.files);
      })
      .catch(() => {})
      .finally(() => setLoading(false));
  }, [token]);

  return (
    <>
      <Helmet>
        <title>Kit de Tareas Pastelería — Dashboard | AI Chef Pro</title>
        <meta name="robots" content="noindex, nofollow" />
      </Helmet>

      <div className="min-h-screen bg-[#0a0a0a]">
        <SaasDiscoveryBanner />
        {/* ── Top bar ────────────────────────────────────────── */}
        <header className="sticky top-0 z-50 bg-[#0a0a0a]/95 backdrop-blur-sm border-b border-white/10">
          <div className="max-w-6xl mx-auto px-4 h-14 flex items-center justify-between">
            <a href="/kit-tareas-pasteleria" className="flex items-center gap-2 text-gray-400 hover:text-white transition-colors text-sm">
              <ArrowLeft className="w-4 h-4" />
              Kit de Tareas Pastelería
            </a>
            <div className="flex items-center gap-2">
              <FileSpreadsheet className="w-5 h-5 text-[#FFD700]" />
              <span className="text-white font-bold text-sm">Tu Dashboard</span>
            </div>
            <a href="https://aichef.pro" className="text-gray-500 hover:text-[#FFD700] text-sm transition-colors">
              aichef.pro
            </a>
          </div>
        </header>

        {/* ── Hero ───────────────────────────────────────────── */}
        <section className="py-12 md:py-16 px-4 text-center">
          <LogoBadge />
          <h1 className="text-3xl md:text-5xl font-extrabold text-white mb-3 mt-4">
            Kit de Tareas <span className="text-[#FFD700]">Pastelería</span>
          </h1>
          <div className="mb-3">
            <ProductVersionBadge productId="kit-tareas-pasteleria" />
          </div>
          <p className="text-gray-400 text-base md:text-lg max-w-2xl mx-auto">
            Tus 13 checklists operativos + 2 bonus listos para descargar. Imprime, delega y controla.
          </p>
        </section>

        {/* ── Downloads grid ────────────────────────────────── */}
        <section className="pb-16 px-4">
          <div className="max-w-5xl mx-auto">
            <p className="text-[#FFD700] text-sm font-bold uppercase tracking-wider mb-6">
              13 Checklists + 2 Bonus · Descarga Directa
            </p>

            <div className="grid sm:grid-cols-2 lg:grid-cols-3 gap-4">
              {TEMPLATES.map((tpl, i) => {
                const Icon = tpl.icon;
                const url = files[tpl.key];
                const isPrimary = i === 0;

                return (
                  <div
                    key={tpl.key}
                    className={`rounded-xl p-5 transition-all ${
                      isPrimary
                        ? 'bg-white/5 border-2 border-[#FFD700]/50'
                        : 'bg-white/5 border border-white/10 hover:border-[#FFD700]/30'
                    }`}
                  >
                    <div className="flex items-start gap-3 mb-3">
                      <div className="w-10 h-10 rounded-lg bg-[#FFD700]/10 flex items-center justify-center flex-shrink-0">
                        <Icon className="w-5 h-5 text-[#FFD700]" />
                      </div>
                      <div>
                        <h3 className="text-white font-bold text-sm leading-tight">
                          {tpl.title}
                          {tpl.isNew && (
                            <span className="ml-2 align-middle inline-block px-1.5 py-0.5 rounded bg-[#FFD700] text-black text-[10px] font-extrabold tracking-wide">
                              NUEVO v2.0
                            </span>
                          )}
                        </h3>
                        <p className="text-gray-500 text-xs mt-0.5">.xlsx</p>
                      </div>
                    </div>
                    <p className="text-gray-400 text-sm mb-4 leading-relaxed">{tpl.desc}</p>

                    {loading ? (
                      <Loader2 className="w-5 h-5 text-gray-500 animate-spin" />
                    ) : url ? (
                      <a
                        href={url}
                        target="_blank"
                        rel="noopener noreferrer"
                        className={`inline-flex items-center gap-2 px-4 py-2 rounded-lg text-sm font-bold transition-all ${
                          isPrimary
                            ? 'bg-[#FFD700] text-black hover:bg-[#FFD700]/90'
                            : 'border border-[#FFD700]/50 text-[#FFD700] hover:bg-[#FFD700]/10'
                        }`}
                      >
                        <Download className="w-4 h-4" />
                        Descargar
                      </a>
                    ) : (
                      <span className="text-gray-500 text-sm">Disponible pronto</span>
                    )}
                  </div>
                );
              })}
            </div>

            {/* ── Compatibility banner ────────────────────────── */}
            <div className="mt-8 bg-white/5 border border-white/10 rounded-xl p-6 text-center">
              <p className="text-white font-semibold mb-1">
                Compatibles con Excel, Google Sheets, LibreOffice, Numbers + Imprimible A4
              </p>
              <p className="text-gray-400 text-sm">
                Descarga los archivos .xlsx y ábrelos con tu programa favorito. Todas las fórmulas se mantienen.
              </p>
            </div>
          </div>
        </section>

        {/* ── SaaS hermanos (solo Miselup + Timlup) + novedades de la versión ── */}
        <SaasCrossSellBanners />
        <ProductChangelog productId="kit-tareas-pasteleria" />

        {/* ── Cross-sell banners ──────────────────────────────── */}
        <section className="py-10 px-4 border-t border-white/10">
          <div className="max-w-3xl mx-auto text-center space-y-4">
            <p className="text-gray-400 text-sm mb-3">
              Completa tu toolkit de gestión hostelera
            </p>
            <div className="flex flex-col sm:flex-row items-center justify-center gap-4">
              <a
                href="/kit-tareas"
                className="inline-block px-6 py-3 border border-[#FFD700]/50 text-[#FFD700] font-bold rounded-xl hover:bg-[#FFD700]/10 transition-all text-sm"
              >
                Ver Kit Tareas Restaurante — €14
              </a>
              <a
                href="/kit-tareas-cafeteria"
                className="inline-block px-6 py-3 border border-[#FFD700]/50 text-[#FFD700] font-bold rounded-xl hover:bg-[#FFD700]/10 transition-all text-sm"
              >
                Ver Kit Tareas Cafetería — €12
              </a>
              <a
                href="/kit-escandallos"
                className="inline-block px-6 py-3 border border-[#FFD700]/50 text-[#FFD700] font-bold rounded-xl hover:bg-[#FFD700]/10 transition-all text-sm"
              >
                Ver Kit de Escandallos Pro — €12
              </a>
            </div>
          </div>
        </section>

        {/* ── Footer ───────────────────────────────────────── */}
        <footer className="py-8 px-4 border-t border-white/10">
          <div className="max-w-4xl mx-auto text-center">
            <p className="text-gray-500 text-sm mb-2">
              © 2026 AI Chef Pro · Kit de Tareas Pastelería · Todos los derechos reservados
            </p>
            <div className="flex flex-wrap items-center justify-center gap-2 md:gap-4 text-sm">
              <a href="https://aichef.pro" className="text-gray-500 hover:text-[#FFD700] transition-colors">aichef.pro</a>
              <span className="text-gray-700 hidden md:inline">·</span>
              <a href="mailto:info@aichef.pro" className="text-gray-500 hover:text-[#FFD700] transition-colors">Contacto</a>
            </div>
          </div>
        </footer>
        <WhatsAppProductSupport />
      </div>
    </>
  );
}
