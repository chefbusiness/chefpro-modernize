/**
 * Island de /en/digital-products/sushi-restaurant-business-plan/library (tienda EN, escrito a mano: el generador
 * de la zona app salta las entradas con lang ≠ 'es').
 * Copia de la isla gemela EN de la familia Planes / PlanNegocioSushiBarLibraryIsland.tsx (ES):
 * ProtectedRoute + dashboard, con el storageKey y la landing EN de la entrada `sushi-restaurant-business-plan`
 * de astro-site/src/lib/zona-app.ts.
 */
import ProtectedRoute from '../../../../src/components/shared/ProtectedRoute';
import SushiRestaurantBusinessPlanDashboard from '../../../../src/pages/SushiRestaurantBusinessPlanDashboard';

export default function SushiRestaurantBusinessPlanLibraryIsland() {
  return (
    <ProtectedRoute storageKey="sushi-restaurant-business-plan-jwt" redirectTo="/en/digital-products/sushi-restaurant-business-plan">
      <SushiRestaurantBusinessPlanDashboard />
    </ProtectedRoute>
  );
}
