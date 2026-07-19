/**
 * Island de /plan-negocio-cocteleria-eventos-library (Fase 5, GENERADO por scripts/astro-migration/
 * fase5-generate-zona-app.py — editar el generador, no este fichero).
 * Réplica exacta de la composición de la SPA para esta ruta en App.tsx:
 * storageKey/redirectTo extraídos VERBATIM de App.tsx por el generador.
 */
import ProtectedRoute from '../../../../src/components/shared/ProtectedRoute';
import PlanNegocioCocteleriaEventosDashboard from '../../../../src/pages/PlanNegocioCocteleriaEventosDashboard';

export default function PlanNegocioCocteleriaEventosLibraryIsland() {
  return (
    <ProtectedRoute storageKey="plan-negocio-cocteleria-eventos-jwt" redirectTo="/plan-negocio-cocteleria-eventos">
      <PlanNegocioCocteleriaEventosDashboard />
    </ProtectedRoute>
  );
}
