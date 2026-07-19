/**
 * Island de /kit-inventario-library (Fase 5, GENERADO por scripts/astro-migration/
 * fase5-generate-zona-app.py — editar el generador, no este fichero).
 * Réplica exacta de la composición de la SPA para esta ruta en App.tsx:
 * storageKey/redirectTo extraídos VERBATIM de App.tsx por el generador.
 */
import ProtectedRoute from '../../../../src/components/shared/ProtectedRoute';
import KitInventarioDashboard from '../../../../src/pages/KitInventarioDashboard';

export default function KitInventarioLibraryIsland() {
  return (
    <ProtectedRoute storageKey="kit-inventario-jwt" redirectTo="/kit-inventario">
      <KitInventarioDashboard />
    </ProtectedRoute>
  );
}
