/**
 * Island de /kit-tareas-asador-library (Fase 5).
 * Réplica exacta de la composición de la SPA (src/App.tsx, ruta -library):
 *   <ProtectedRoute storageKey redirectTo><Dashboard/></ProtectedRoute>
 * Los componentes se importan de la SPA TAL CUAL (fuente de verdad única).
 * storageKey/redirectTo: VERBATIM de App.tsx — gate S2: byte-compare.
 */
import ProtectedRoute from '../../../../src/components/shared/ProtectedRoute';
import KitTareasAsadorDashboard from '../../../../src/pages/KitTareasAsadorDashboard';

export default function KitTareasAsadorLibrary() {
  return (
    <ProtectedRoute storageKey="kit-tareas-asador-jwt" redirectTo="/kit-tareas-asador">
      <KitTareasAsadorDashboard />
    </ProtectedRoute>
  );
}
