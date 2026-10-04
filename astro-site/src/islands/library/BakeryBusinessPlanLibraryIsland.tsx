/**
 * Island de /en/digital-products/bakery-business-plan/library (tienda EN, escrito a mano: el generador
 * de la zona app salta las entradas con lang ≠ 'es').
 * Copia de RestaurantFinancialPlanKitLibraryIsland.tsx (EN) / PlanNegocioPanaderiaLibraryIsland.tsx (ES):
 * ProtectedRoute + dashboard, con el storageKey y la landing EN de la entrada `bakery-business-plan`
 * de astro-site/src/lib/zona-app.ts.
 */
import ProtectedRoute from '../../../../src/components/shared/ProtectedRoute';
import BakeryBusinessPlanDashboard from '../../../../src/pages/BakeryBusinessPlanDashboard';

export default function BakeryBusinessPlanLibraryIsland() {
  return (
    <ProtectedRoute storageKey="bakery-business-plan-jwt" redirectTo="/en/digital-products/bakery-business-plan">
      <BakeryBusinessPlanDashboard />
    </ProtectedRoute>
  );
}
