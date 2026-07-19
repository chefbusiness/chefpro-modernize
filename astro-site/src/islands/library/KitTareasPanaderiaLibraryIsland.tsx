/**
 * Island de /kit-tareas-panaderia-library (Fase 5, GENERADO por scripts/astro-migration/
 * fase5-generate-zona-app.py — editar el generador, no este fichero).
 * Réplica exacta de la composición de la SPA para esta ruta en App.tsx:
 * storageKey/redirectTo extraídos VERBATIM de App.tsx por el generador.
 */
import ProtectedRoute from '../../../../src/components/shared/ProtectedRoute';
import KitTareasPanaderiaDashboard from '../../../../src/pages/KitTareasPanaderiaDashboard';

export default function KitTareasPanaderiaLibraryIsland() {
  return (
    <ProtectedRoute storageKey="kit-tareas-panaderia-jwt" redirectTo="/kit-tareas-panaderia">
      <KitTareasPanaderiaDashboard />
    </ProtectedRoute>
  );
}
