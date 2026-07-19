/**
 * Island de /kit-tareas-hotel-library (Fase 5, GENERADO por scripts/astro-migration/
 * fase5-generate-zona-app.py — editar el generador, no este fichero).
 * Réplica exacta de la composición de la SPA para esta ruta en App.tsx:
 * storageKey/redirectTo extraídos VERBATIM de App.tsx por el generador.
 */
import ProtectedRoute from '../../../../src/components/shared/ProtectedRoute';
import KitTareasHotelDashboard from '../../../../src/pages/KitTareasHotelDashboard';

export default function KitTareasHotelLibraryIsland() {
  return (
    <ProtectedRoute storageKey="kit-tareas-hotel-jwt" redirectTo="/kit-tareas-hotel">
      <KitTareasHotelDashboard />
    </ProtectedRoute>
  );
}
