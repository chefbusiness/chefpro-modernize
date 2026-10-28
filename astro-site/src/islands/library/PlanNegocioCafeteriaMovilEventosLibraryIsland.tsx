/**
 * Island de /plan-negocio-cafeteria-movil-eventos-library (Fase 5, GENERADO por scripts/astro-migration/
 * fase5-generate-zona-app.py — editar el generador, no este fichero).
 * Réplica exacta de la composición de la SPA para esta ruta en App.tsx:
 * storageKey/redirectTo extraídos VERBATIM de App.tsx por el generador.
 */
import ProtectedRoute from '../../../../src/components/shared/ProtectedRoute';
import PlanNegocioCafeteriaMovilEventosDashboard from '../../../../src/pages/PlanNegocioCafeteriaMovilEventosDashboard';

export default function PlanNegocioCafeteriaMovilEventosLibraryIsland() {
  return (
    <ProtectedRoute storageKey="plan-negocio-cafeteria-movil-eventos-jwt" redirectTo="/plan-negocio-cafeteria-movil-eventos">
      <PlanNegocioCafeteriaMovilEventosDashboard />
    </ProtectedRoute>
  );
}
