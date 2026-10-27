/**
 * Island de /en/digital-products/ice-cream-shop-business-plan/library (tienda EN, escrito a mano: el generador
 * de la zona app salta las entradas con lang ≠ 'es').
 * Copia de MobileBarBusinessPlanLibraryIsland.tsx (EN) / PlanNegocioHeladeriaLibraryIsland.tsx (ES):
 * ProtectedRoute + dashboard, con el storageKey y la landing EN de la entrada `ice-cream-shop-business-plan`
 * de astro-site/src/lib/zona-app.ts.
 */
import ProtectedRoute from '../../../../src/components/shared/ProtectedRoute';
import IceCreamShopBusinessPlanDashboard from '../../../../src/pages/IceCreamShopBusinessPlanDashboard';

export default function IceCreamShopBusinessPlanLibraryIsland() {
  return (
    <ProtectedRoute storageKey="ice-cream-shop-business-plan-jwt" redirectTo="/en/digital-products/ice-cream-shop-business-plan">
      <IceCreamShopBusinessPlanDashboard />
    </ProtectedRoute>
  );
}
