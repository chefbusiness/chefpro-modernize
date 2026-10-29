/**
 * Island de /en/digital-products/rotisserie-chicken-restaurant-business-plan/library (tienda EN, escrito a mano: el generador
 * de la zona app salta las entradas con lang ≠ 'es').
 * Copia de la isla gemela EN de la familia Planes / PlanNegocioPolleriaLibraryIsland.tsx (ES):
 * ProtectedRoute + dashboard, con el storageKey y la landing EN de la entrada `rotisserie-chicken-restaurant-business-plan`
 * de astro-site/src/lib/zona-app.ts.
 */
import ProtectedRoute from '../../../../src/components/shared/ProtectedRoute';
import RotisserieChickenRestaurantBusinessPlanDashboard from '../../../../src/pages/RotisserieChickenRestaurantBusinessPlanDashboard';

export default function RotisserieChickenRestaurantBusinessPlanLibraryIsland() {
  return (
    <ProtectedRoute storageKey="rotisserie-chicken-restaurant-business-plan-jwt" redirectTo="/en/digital-products/rotisserie-chicken-restaurant-business-plan">
      <RotisserieChickenRestaurantBusinessPlanDashboard />
    </ProtectedRoute>
  );
}
