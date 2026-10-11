/**
 * Island de /en/digital-products/bar-business-plan/library (tienda EN, escrito a mano: el generador
 * de la zona app salta las entradas con lang ≠ 'es').
 * Copia de RestaurantBusinessPlanLibraryIsland.tsx (EN) / PlanNegocioTapasBarLibraryIsland.tsx (ES):
 * ProtectedRoute + dashboard, con el storageKey y la landing EN de la entrada `bar-business-plan`
 * de astro-site/src/lib/zona-app.ts.
 */
import ProtectedRoute from '../../../../src/components/shared/ProtectedRoute';
import BarBusinessPlanDashboard from '../../../../src/pages/BarBusinessPlanDashboard';

export default function BarBusinessPlanLibraryIsland() {
  return (
    <ProtectedRoute storageKey="bar-business-plan-jwt" redirectTo="/en/digital-products/bar-business-plan">
      <BarBusinessPlanDashboard />
    </ProtectedRoute>
  );
}
