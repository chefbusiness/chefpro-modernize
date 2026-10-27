/**
 * Island de /en/digital-products/wedding-venue-business-plan/library (tienda EN, escrito a mano: el generador
 * de la zona app salta las entradas con lang ≠ 'es').
 * Copia de MobileBarBusinessPlanLibraryIsland.tsx (EN) / PlanNegocioFincaEventosBodasLibraryIsland.tsx (ES):
 * ProtectedRoute + dashboard, con el storageKey y la landing EN de la entrada `wedding-venue-business-plan`
 * de astro-site/src/lib/zona-app.ts.
 */
import ProtectedRoute from '../../../../src/components/shared/ProtectedRoute';
import WeddingVenueBusinessPlanDashboard from '../../../../src/pages/WeddingVenueBusinessPlanDashboard';

export default function WeddingVenueBusinessPlanLibraryIsland() {
  return (
    <ProtectedRoute storageKey="wedding-venue-business-plan-jwt" redirectTo="/en/digital-products/wedding-venue-business-plan">
      <WeddingVenueBusinessPlanDashboard />
    </ProtectedRoute>
  );
}
