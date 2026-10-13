/**
 * Island de /en/digital-products/mobile-bar-business-plan/library (tienda EN, escrito a mano: el generador
 * de la zona app salta las entradas con lang ≠ 'es').
 * Copia de CateringBusinessPlanLibraryIsland.tsx (EN) / PlanNegocioCocteleriaEventosLibraryIsland.tsx (ES):
 * ProtectedRoute + dashboard, con el storageKey y la landing EN de la entrada `mobile-bar-business-plan`
 * de astro-site/src/lib/zona-app.ts.
 */
import ProtectedRoute from '../../../../src/components/shared/ProtectedRoute';
import MobileBarBusinessPlanDashboard from '../../../../src/pages/MobileBarBusinessPlanDashboard';

export default function MobileBarBusinessPlanLibraryIsland() {
  return (
    <ProtectedRoute storageKey="mobile-bar-business-plan-jwt" redirectTo="/en/digital-products/mobile-bar-business-plan">
      <MobileBarBusinessPlanDashboard />
    </ProtectedRoute>
  );
}
