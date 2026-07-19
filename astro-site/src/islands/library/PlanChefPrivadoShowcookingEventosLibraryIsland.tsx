/**
 * Island de /plan-chef-privado-showcooking-eventos-library (Fase 5, GENERADO por scripts/astro-migration/
 * fase5-generate-zona-app.py — editar el generador, no este fichero).
 * Réplica exacta de la composición de la SPA para esta ruta en App.tsx:
 * storageKey/redirectTo extraídos VERBATIM de App.tsx por el generador.
 */
import ProtectedRoute from '../../../../src/components/shared/ProtectedRoute';
import PlanChefPrivadoShowcookingEventosDashboard from '../../../../src/pages/PlanChefPrivadoShowcookingEventosDashboard';

export default function PlanChefPrivadoShowcookingEventosLibraryIsland() {
  return (
    <ProtectedRoute storageKey="plan-chef-privado-showcooking-eventos-jwt" redirectTo="/plan-chef-privado-showcooking-eventos">
      <PlanChefPrivadoShowcookingEventosDashboard />
    </ProtectedRoute>
  );
}
