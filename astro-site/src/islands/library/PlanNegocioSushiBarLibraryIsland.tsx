/**
 * Island de /plan-negocio-sushi-bar-library (Fase 5, GENERADO por scripts/astro-migration/
 * fase5-generate-zona-app.py — editar el generador, no este fichero).
 * Réplica exacta de la composición de la SPA para esta ruta en App.tsx:
 * storageKey/redirectTo extraídos VERBATIM de App.tsx por el generador.
 */
import ProtectedRoute from '../../../../src/components/shared/ProtectedRoute';
import PlanNegocioSushiBarDashboard from '../../../../src/pages/PlanNegocioSushiBarDashboard';

export default function PlanNegocioSushiBarLibraryIsland() {
  return (
    <ProtectedRoute storageKey="plan-negocio-sushi-bar-jwt" redirectTo="/plan-negocio-sushi-bar">
      <PlanNegocioSushiBarDashboard />
    </ProtectedRoute>
  );
}
