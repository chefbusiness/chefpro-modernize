/**
 * Island de /en/digital-products/haccp-templates/library (tienda EN, escrito a mano:
 * el generador de la zona app salta las entradas con lang ≠ 'es').
 * Copia de RestaurantInventoryKitLibraryIsland.tsx / PackAppccLibraryIsland.tsx (ES): ProtectedRoute +
 * dashboard, con el storageKey y la landing EN de la entrada `haccp-templates` de
 * astro-site/src/lib/zona-app.ts.
 */
import ProtectedRoute from '../../../../src/components/shared/ProtectedRoute';
import HaccpKitDashboard from '../../../../src/pages/HaccpKitDashboard';

export default function HaccpKitLibraryIsland() {
  return (
    <ProtectedRoute storageKey="haccp-templates-jwt" redirectTo="/en/digital-products/haccp-templates">
      <HaccpKitDashboard />
    </ProtectedRoute>
  );
}
