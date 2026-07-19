/**
 * Island de /kit-tareas-bar-library (Fase 5, GENERADO por scripts/astro-migration/
 * fase5-generate-zona-app.py — editar el generador, no este fichero).
 * Réplica exacta de la composición de la SPA para esta ruta en App.tsx:
 * storageKey/redirectTo extraídos VERBATIM de App.tsx por el generador.
 */
import ProtectedRoute from '../../../../src/components/shared/ProtectedRoute';
import KitTareasBarDashboard from '../../../../src/pages/KitTareasBarDashboard';

export default function KitTareasBarLibraryIsland() {
  return (
    <ProtectedRoute storageKey="kit-tareas-bar-jwt" redirectTo="/kit-tareas-bar">
      <KitTareasBarDashboard />
    </ProtectedRoute>
  );
}
