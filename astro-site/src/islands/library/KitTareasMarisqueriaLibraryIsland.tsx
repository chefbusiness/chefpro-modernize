/**
 * Island de /kit-tareas-marisqueria-library (Fase 5, GENERADO por scripts/astro-migration/
 * fase5-generate-zona-app.py — editar el generador, no este fichero).
 * Réplica exacta de la composición de la SPA para esta ruta en App.tsx:
 * storageKey/redirectTo extraídos VERBATIM de App.tsx por el generador.
 */
import ProtectedRoute from '../../../../src/components/shared/ProtectedRoute';
import KitTareasMarisqueriaDashboard from '../../../../src/pages/KitTareasMarisqueriaDashboard';

export default function KitTareasMarisqueriaLibraryIsland() {
  return (
    <ProtectedRoute storageKey="kit-tareas-marisqueria-jwt" redirectTo="/kit-tareas-marisqueria">
      <KitTareasMarisqueriaDashboard />
    </ProtectedRoute>
  );
}
