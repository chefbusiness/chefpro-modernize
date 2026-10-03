/**
 * Island de /en/digital-products/restaurant-financial-plan-templates/library (tienda EN, escrito a
 * mano: el generador de la zona app salta las entradas con lang ≠ 'es').
 * Copia de RestaurantScheduleKitLibraryIsland.tsx (EN) / KitPlanFinancieroLibraryIsland.tsx (ES):
 * ProtectedRoute + dashboard, con el storageKey y la landing EN de la entrada
 * `restaurant-financial-plan-templates` de astro-site/src/lib/zona-app.ts.
 */
import ProtectedRoute from '../../../../src/components/shared/ProtectedRoute';
import RestaurantFinancialPlanKitDashboard from '../../../../src/pages/RestaurantFinancialPlanKitDashboard';

export default function RestaurantFinancialPlanKitLibraryIsland() {
  return (
    <ProtectedRoute storageKey="restaurant-financial-plan-templates-jwt" redirectTo="/en/digital-products/restaurant-financial-plan-templates">
      <RestaurantFinancialPlanKitDashboard />
    </ProtectedRoute>
  );
}
