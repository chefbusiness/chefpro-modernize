/**
 * Island de /en/digital-products/bar-checklist-templates/library (tienda EN, escrito a mano:
 * el generador de la zona app salta las entradas con lang ≠ 'es').
 * Copia de RestaurantChecklistsKitLibraryIsland.tsx (EN) / KitTareasBarLibraryIsland.tsx (ES):
 * ProtectedRoute + dashboard, con el storageKey y la landing EN de la entrada
 * `bar-checklist-templates` de astro-site/src/lib/zona-app.ts.
 */
import ProtectedRoute from '../../../../src/components/shared/ProtectedRoute';
import BarChecklistsKitDashboard from '../../../../src/pages/BarChecklistsKitDashboard';

export default function BarChecklistsKitLibraryIsland() {
  return (
    <ProtectedRoute storageKey="bar-checklist-templates-jwt" redirectTo="/en/digital-products/bar-checklist-templates">
      <BarChecklistsKitDashboard />
    </ProtectedRoute>
  );
}
