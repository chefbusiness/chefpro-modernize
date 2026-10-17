/**
 * Island de /en/digital-products/restaurant-checklist-templates/library (tienda EN, escrito a mano:
 * el generador de la zona app salta las entradas con lang ≠ 'es').
 * Copia de RestaurantScheduleKitLibraryIsland.tsx (EN) / KitTareasLibraryIsland.tsx (ES):
 * ProtectedRoute + dashboard, con el storageKey y la landing EN de la entrada
 * `restaurant-checklist-templates` de astro-site/src/lib/zona-app.ts.
 */
import ProtectedRoute from '../../../../src/components/shared/ProtectedRoute';
import RestaurantChecklistsKitDashboard from '../../../../src/pages/RestaurantChecklistsKitDashboard';

export default function RestaurantChecklistsKitLibraryIsland() {
  return (
    <ProtectedRoute storageKey="restaurant-checklist-templates-jwt" redirectTo="/en/digital-products/restaurant-checklist-templates">
      <RestaurantChecklistsKitDashboard />
    </ProtectedRoute>
  );
}
