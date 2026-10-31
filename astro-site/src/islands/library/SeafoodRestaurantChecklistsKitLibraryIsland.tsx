/**
 * Island de /en/digital-products/seafood-restaurant-checklist-templates/library (tienda EN, escrito a mano:
 * el generador de la zona app salta las entradas con lang ≠ 'es').
 * Copia de RestaurantChecklistsKitLibraryIsland.tsx (EN) / KitTareasMarisqueriaLibraryIsland.tsx (ES):
 * ProtectedRoute + dashboard, con el storageKey y la landing EN de la entrada
 * `seafood-restaurant-checklist-templates` de astro-site/src/lib/zona-app.ts.
 */
import ProtectedRoute from '../../../../src/components/shared/ProtectedRoute';
import SeafoodRestaurantChecklistsKitDashboard from '../../../../src/pages/SeafoodRestaurantChecklistsKitDashboard';

export default function SeafoodRestaurantChecklistsKitLibraryIsland() {
  return (
    <ProtectedRoute storageKey="seafood-restaurant-checklist-templates-jwt" redirectTo="/en/digital-products/seafood-restaurant-checklist-templates">
      <SeafoodRestaurantChecklistsKitDashboard />
    </ProtectedRoute>
  );
}
