/**
 * Island de /plan-catering-tematico-eventos-library (Fase 5, GENERADO por scripts/astro-migration/
 * fase5-generate-zona-app.py — editar el generador, no este fichero).
 * Réplica exacta de la composición de la SPA para esta ruta en App.tsx:
 * storageKey/redirectTo extraídos VERBATIM de App.tsx por el generador.
 */
import ProtectedRoute from '../../../../src/components/shared/ProtectedRoute';
import PlanCateringTematicoEventosDashboard from '../../../../src/pages/PlanCateringTematicoEventosDashboard';

export default function PlanCateringTematicoEventosLibraryIsland() {
  return (
    <ProtectedRoute storageKey="plan-catering-tematico-eventos-jwt" redirectTo="/plan-catering-tematico-eventos">
      <PlanCateringTematicoEventosDashboard />
    </ProtectedRoute>
  );
}
