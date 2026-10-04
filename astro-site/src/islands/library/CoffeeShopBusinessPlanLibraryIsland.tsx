/**
 * Island de /en/digital-products/coffee-shop-business-plan/library (tienda EN, escrito a mano: el generador
 * de la zona app salta las entradas con lang ≠ 'es').
 * Copia de RestaurantFinancialPlanKitLibraryIsland.tsx (EN) / PlanNegocioCafeteriaLibraryIsland.tsx (ES):
 * ProtectedRoute + dashboard, con el storageKey y la landing EN de la entrada `coffee-shop-business-plan`
 * de astro-site/src/lib/zona-app.ts.
 */
import ProtectedRoute from '../../../../src/components/shared/ProtectedRoute';
import CoffeeShopBusinessPlanDashboard from '../../../../src/pages/CoffeeShopBusinessPlanDashboard';

export default function CoffeeShopBusinessPlanLibraryIsland() {
  return (
    <ProtectedRoute storageKey="coffee-shop-business-plan-jwt" redirectTo="/en/digital-products/coffee-shop-business-plan">
      <CoffeeShopBusinessPlanDashboard />
    </ProtectedRoute>
  );
}
