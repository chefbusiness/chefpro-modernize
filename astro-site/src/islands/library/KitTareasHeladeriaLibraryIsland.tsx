/**
 * Island de /kit-tareas-heladeria-library (Fase 5, GENERADO por scripts/astro-migration/
 * fase5-generate-zona-app.py — editar el generador, no este fichero).
 * Réplica exacta de la composición de la SPA para esta ruta en App.tsx:
 * storageKey/redirectTo extraídos VERBATIM de App.tsx por el generador.
 */
import ProtectedRoute from '../../../../src/components/shared/ProtectedRoute';
import KitTareasHeladeriaDashboard from '../../../../src/pages/KitTareasHeladeriaDashboard';

export default function KitTareasHeladeriaLibraryIsland() {
  return (
    <ProtectedRoute storageKey="kit-tareas-heladeria-jwt" redirectTo="/kit-tareas-heladeria">
      <KitTareasHeladeriaDashboard />
    </ProtectedRoute>
  );
}
