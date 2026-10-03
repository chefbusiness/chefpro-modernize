/**
 * Island de /en/digital-products/restaurant-schedule-templates/library (tienda EN, escrito a mano:
 * el generador de la zona app salta las entradas con lang ≠ 'es').
 * Copia de RestaurantInventoryKitLibraryIsland.tsx (EN) / KitGestionPersonalLibraryIsland.tsx (ES):
 * ProtectedRoute + dashboard, con el storageKey y la landing EN de la entrada
 * `restaurant-schedule-templates` de astro-site/src/lib/zona-app.ts.
 */
import ProtectedRoute from '../../../../src/components/shared/ProtectedRoute';
import RestaurantScheduleKitDashboard from '../../../../src/pages/RestaurantScheduleKitDashboard';

export default function RestaurantScheduleKitLibraryIsland() {
  return (
    <ProtectedRoute storageKey="restaurant-schedule-templates-jwt" redirectTo="/en/digital-products/restaurant-schedule-templates">
      <RestaurantScheduleKitDashboard />
    </ProtectedRoute>
  );
}
