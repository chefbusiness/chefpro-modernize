/**
 * Island de /plan-negocio-paellero-eventos-library (Fase 5, GENERADO por scripts/astro-migration/
 * fase5-generate-zona-app.py — editar el generador, no este fichero).
 * Réplica exacta de la composición de la SPA para esta ruta en App.tsx:
 * storageKey/redirectTo extraídos VERBATIM de App.tsx por el generador.
 */
import ProtectedRoute from '../../../../src/components/shared/ProtectedRoute';
import PlanNegocioPaelleroEventosDashboard from '../../../../src/pages/PlanNegocioPaelleroEventosDashboard';

export default function PlanNegocioPaelleroEventosLibraryIsland() {
  return (
    <ProtectedRoute storageKey="plan-negocio-paellero-eventos-jwt" redirectTo="/plan-negocio-paellero-eventos">
      <PlanNegocioPaelleroEventosDashboard />
    </ProtectedRoute>
  );
}
