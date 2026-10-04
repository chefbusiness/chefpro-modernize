/**
 * Island de /en/digital-products/restaurant-business-plan/library (tienda EN, escrito a mano: el generador
 * de la zona app salta las entradas con lang ≠ 'es').
 * Copia de RestaurantFinancialPlanKitLibraryIsland.tsx (EN) / PlanNegocioBarRestauranteLibraryIsland.tsx (ES):
 * ProtectedRoute + dashboard, con el storageKey y la landing EN de la entrada `restaurant-business-plan`
 * de astro-site/src/lib/zona-app.ts.
 */
import ProtectedRoute from '../../../../src/components/shared/ProtectedRoute';
import RestaurantBusinessPlanDashboard from '../../../../src/pages/RestaurantBusinessPlanDashboard';

export default function RestaurantBusinessPlanLibraryIsland() {
  return (
    <ProtectedRoute storageKey="restaurant-business-plan-jwt" redirectTo="/en/digital-products/restaurant-business-plan">
      <RestaurantBusinessPlanDashboard />
    </ProtectedRoute>
  );
}
