/**
 * Island de /en/digital-products/catering-checklist-templates/library (tienda EN, escrito a mano:
 * el generador de la zona app salta las entradas con lang ≠ 'es').
 * Copia de RestaurantChecklistsKitLibraryIsland.tsx (EN) / KitTareasCateringLibraryIsland.tsx (ES):
 * ProtectedRoute + dashboard, con el storageKey y la landing EN de la entrada
 * `catering-checklist-templates` de astro-site/src/lib/zona-app.ts.
 */
import ProtectedRoute from '../../../../src/components/shared/ProtectedRoute';
import CateringChecklistsKitDashboard from '../../../../src/pages/CateringChecklistsKitDashboard';

export default function CateringChecklistsKitLibraryIsland() {
  return (
    <ProtectedRoute storageKey="catering-checklist-templates-jwt" redirectTo="/en/digital-products/catering-checklist-templates">
      <CateringChecklistsKitDashboard />
    </ProtectedRoute>
  );
}
