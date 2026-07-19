/**
 * Island de /plan-negocio-food-truck-library (Fase 5, GENERADO por scripts/astro-migration/
 * fase5-generate-zona-app.py — editar el generador, no este fichero).
 * Réplica exacta de la composición de la SPA para esta ruta en App.tsx:
 * storageKey/redirectTo extraídos VERBATIM de App.tsx por el generador.
 */
import ProtectedRoute from '../../../../src/components/shared/ProtectedRoute';
import PlanNegocioFoodTruckDashboard from '../../../../src/pages/PlanNegocioFoodTruckDashboard';

export default function PlanNegocioFoodTruckLibraryIsland() {
  return (
    <ProtectedRoute storageKey="plan-negocio-food-truck-jwt" redirectTo="/plan-negocio-food-truck">
      <PlanNegocioFoodTruckDashboard />
    </ProtectedRoute>
  );
}
