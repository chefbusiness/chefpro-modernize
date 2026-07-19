/**
 * Island de /kit-tareas-hamburgueseria-library (Fase 5, GENERADO por scripts/astro-migration/
 * fase5-generate-zona-app.py — editar el generador, no este fichero).
 * Réplica exacta de la composición de la SPA para esta ruta en App.tsx:
 * storageKey/redirectTo extraídos VERBATIM de App.tsx por el generador.
 */
import ProtectedRoute from '../../../../src/components/shared/ProtectedRoute';
import KitTareasHamburgueseriaDashboard from '../../../../src/pages/KitTareasHamburgueseriaDashboard';

export default function KitTareasHamburgueseriaLibraryIsland() {
  return (
    <ProtectedRoute storageKey="kit-tareas-hamburgueseria-jwt" redirectTo="/kit-tareas-hamburgueseria">
      <KitTareasHamburgueseriaDashboard />
    </ProtectedRoute>
  );
}
