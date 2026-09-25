/**
 * Island de /en/digital-products/restaurant-inventory-templates/library (tienda EN, escrito a mano:
 * el generador de la zona app salta las entradas con lang ≠ 'es').
 * Copia de FoodCostKitLibraryIsland.tsx (piloto) / KitInventarioLibraryIsland.tsx (ES): ProtectedRoute +
 * dashboard, con el storageKey y la landing EN de la entrada `restaurant-inventory-templates` de
 * astro-site/src/lib/zona-app.ts.
 */
import ProtectedRoute from '../../../../src/components/shared/ProtectedRoute';
import RestaurantInventoryKitDashboard from '../../../../src/pages/RestaurantInventoryKitDashboard';

export default function RestaurantInventoryKitLibraryIsland() {
  return (
    <ProtectedRoute storageKey="restaurant-inventory-templates-jwt" redirectTo="/en/digital-products/restaurant-inventory-templates">
      <RestaurantInventoryKitDashboard />
    </ProtectedRoute>
  );
}
