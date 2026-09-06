/**
 * Island de /manual-chef-ejecutivo-library (Fase 5, GENERADO por scripts/astro-migration/
 * fase5-generate-zona-app.py — editar el generador, no este fichero).
 * Réplica exacta de la composición de la SPA para esta ruta en App.tsx:
 * storageKey/redirectTo extraídos VERBATIM de App.tsx por el generador.
 */
import ProtectedRoute from '../../../../src/components/shared/ProtectedRoute';
import ManualChefDashboard from '../../../../src/pages/ManualChefDashboard';

export default function ManualChefLibraryIsland() {
  return (
    <ProtectedRoute storageKey="manual-chef-ejecutivo-jwt" redirectTo="/manual-chef-ejecutivo">
      <ManualChefDashboard />
    </ProtectedRoute>
  );
}
