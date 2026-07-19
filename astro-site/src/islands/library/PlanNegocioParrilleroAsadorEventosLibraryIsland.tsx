/**
 * Island de /plan-negocio-parrillero-asador-eventos-library (Fase 5, GENERADO por scripts/astro-migration/
 * fase5-generate-zona-app.py — editar el generador, no este fichero).
 * Réplica exacta de la composición de la SPA para esta ruta en App.tsx:
 * storageKey/redirectTo extraídos VERBATIM de App.tsx por el generador.
 */
import ProtectedRoute from '../../../../src/components/shared/ProtectedRoute';
import PlanNegocioParrilleroAsadorEventosDashboard from '../../../../src/pages/PlanNegocioParrilleroAsadorEventosDashboard';

export default function PlanNegocioParrilleroAsadorEventosLibraryIsland() {
  return (
    <ProtectedRoute storageKey="plan-negocio-parrillero-asador-eventos-jwt" redirectTo="/plan-negocio-parrillero-asador-eventos">
      <PlanNegocioParrilleroAsadorEventosDashboard />
    </ProtectedRoute>
  );
}
