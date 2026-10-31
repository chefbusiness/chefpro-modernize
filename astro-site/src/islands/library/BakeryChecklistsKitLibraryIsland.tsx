/**
 * Island de /en/digital-products/bakery-checklist-templates/library (tienda EN, escrito a mano:
 * el generador de la zona app salta las entradas con lang ≠ 'es').
 * Copia de RestaurantChecklistsKitLibraryIsland.tsx (EN) / KitTareasPanaderiaLibraryIsland.tsx (ES):
 * ProtectedRoute + dashboard, con el storageKey y la landing EN de la entrada
 * `bakery-checklist-templates` de astro-site/src/lib/zona-app.ts.
 */
import ProtectedRoute from '../../../../src/components/shared/ProtectedRoute';
import BakeryChecklistsKitDashboard from '../../../../src/pages/BakeryChecklistsKitDashboard';

export default function BakeryChecklistsKitLibraryIsland() {
  return (
    <ProtectedRoute storageKey="bakery-checklist-templates-jwt" redirectTo="/en/digital-products/bakery-checklist-templates">
      <BakeryChecklistsKitDashboard />
    </ProtectedRoute>
  );
}
