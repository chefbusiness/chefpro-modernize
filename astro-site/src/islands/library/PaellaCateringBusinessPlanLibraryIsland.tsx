/**
 * Island de /en/digital-products/paella-catering-business-plan/library (tienda EN, escrito a mano: el generador
 * de la zona app salta las entradas con lang ≠ 'es').
 * Copia de MobileBarBusinessPlanLibraryIsland.tsx (EN) / PlanNegocioPaelleroEventosLibraryIsland.tsx (ES):
 * ProtectedRoute + dashboard, con el storageKey y la landing EN de la entrada `paella-catering-business-plan`
 * de astro-site/src/lib/zona-app.ts.
 */
import ProtectedRoute from '../../../../src/components/shared/ProtectedRoute';
import PaellaCateringBusinessPlanDashboard from '../../../../src/pages/PaellaCateringBusinessPlanDashboard';

export default function PaellaCateringBusinessPlanLibraryIsland() {
  return (
    <ProtectedRoute storageKey="paella-catering-business-plan-jwt" redirectTo="/en/digital-products/paella-catering-business-plan">
      <PaellaCateringBusinessPlanDashboard />
    </ProtectedRoute>
  );
}
