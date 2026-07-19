/**
 * Island de /kit-gestion-personal-library (Fase 5, GENERADO por scripts/astro-migration/
 * fase5-generate-zona-app.py — editar el generador, no este fichero).
 * Réplica exacta de la composición de la SPA para esta ruta en App.tsx:
 * storageKey/redirectTo extraídos VERBATIM de App.tsx por el generador.
 */
import ProtectedRoute from '../../../../src/components/shared/ProtectedRoute';
import KitGestionPersonalDashboard from '../../../../src/pages/KitGestionPersonalDashboard';

export default function KitGestionPersonalLibraryIsland() {
  return (
    <ProtectedRoute storageKey="kit-gestion-personal-jwt" redirectTo="/kit-gestion-personal">
      <KitGestionPersonalDashboard />
    </ProtectedRoute>
  );
}
