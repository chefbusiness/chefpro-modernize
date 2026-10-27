/**
 * Island de /en/digital-products/hotel-checklist-templates/library (tienda EN, escrito a mano:
 * el generador de la zona app salta las entradas con lang ≠ 'es').
 * Copia de RestaurantChecklistsKitLibraryIsland.tsx (EN) / KitTareasHotelLibraryIsland.tsx (ES):
 * ProtectedRoute + dashboard, con el storageKey y la landing EN de la entrada
 * `hotel-checklist-templates` de astro-site/src/lib/zona-app.ts.
 */
import ProtectedRoute from '../../../../src/components/shared/ProtectedRoute';
import HotelChecklistsKitDashboard from '../../../../src/pages/HotelChecklistsKitDashboard';

export default function HotelChecklistsKitLibraryIsland() {
  return (
    <ProtectedRoute storageKey="hotel-checklist-templates-jwt" redirectTo="/en/digital-products/hotel-checklist-templates">
      <HotelChecklistsKitDashboard />
    </ProtectedRoute>
  );
}
