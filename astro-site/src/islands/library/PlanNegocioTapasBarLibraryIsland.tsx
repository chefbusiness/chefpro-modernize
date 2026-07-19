/**
 * Island de /plan-negocio-tapas-bar-library (Fase 5, GENERADO por scripts/astro-migration/
 * fase5-generate-zona-app.py — editar el generador, no este fichero).
 * Réplica exacta de la composición de la SPA para esta ruta en App.tsx:
 * storageKey/redirectTo extraídos VERBATIM de App.tsx por el generador.
 */
import ProtectedRoute from '../../../../src/components/shared/ProtectedRoute';
import PlanNegocioTapasBarDashboard from '../../../../src/pages/PlanNegocioTapasBarDashboard';

export default function PlanNegocioTapasBarLibraryIsland() {
  return (
    <ProtectedRoute storageKey="plan-negocio-tapas-bar-jwt" redirectTo="/plan-negocio-tapas-bar">
      <PlanNegocioTapasBarDashboard />
    </ProtectedRoute>
  );
}
