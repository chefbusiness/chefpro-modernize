/**
 * Island de /mega-pack-tareas-library (Fase 5, GENERADO por scripts/astro-migration/
 * fase5-generate-zona-app.py — editar el generador, no este fichero).
 * Réplica exacta de la composición de la SPA para esta ruta en App.tsx:
 * storageKey/redirectTo extraídos VERBATIM de App.tsx por el generador.
 */
import ProtectedRoute from '../../../../src/components/shared/ProtectedRoute';
import MegaPackTareasDashboard from '../../../../src/pages/MegaPackTareasDashboard';

export default function MegaPackTareasLibraryIsland() {
  return (
    <ProtectedRoute storageKey="mega-pack-tareas-jwt" redirectTo="/mega-pack-tareas">
      <MegaPackTareasDashboard />
    </ProtectedRoute>
  );
}
