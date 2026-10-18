/**
 * Island de /en/digital-products/ghost-kitchen-checklist-templates/library (tienda EN, escrito a mano:
 * el generador de la zona app salta las entradas con lang ≠ 'es').
 * Copia de RestaurantChecklistsKitLibraryIsland.tsx (EN) / KitTareasDarkKitchenLibraryIsland.tsx (ES):
 * ProtectedRoute + dashboard, con el storageKey y la landing EN de la entrada
 * `ghost-kitchen-checklist-templates` de astro-site/src/lib/zona-app.ts.
 */
import ProtectedRoute from '../../../../src/components/shared/ProtectedRoute';
import GhostKitchenChecklistsKitDashboard from '../../../../src/pages/GhostKitchenChecklistsKitDashboard';

export default function GhostKitchenChecklistsKitLibraryIsland() {
  return (
    <ProtectedRoute storageKey="ghost-kitchen-checklist-templates-jwt" redirectTo="/en/digital-products/ghost-kitchen-checklist-templates">
      <GhostKitchenChecklistsKitDashboard />
    </ProtectedRoute>
  );
}
