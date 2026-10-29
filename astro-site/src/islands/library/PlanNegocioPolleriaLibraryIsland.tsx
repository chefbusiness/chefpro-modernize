/**
 * Island de /plan-negocio-polleria-library (Fase 5, GENERADO por scripts/astro-migration/
 * fase5-generate-zona-app.py — editar el generador, no este fichero).
 * Réplica exacta de la composición de la SPA para esta ruta en App.tsx:
 * storageKey/redirectTo extraídos VERBATIM de App.tsx por el generador.
 */
import ProtectedRoute from '../../../../src/components/shared/ProtectedRoute';
import PlanNegocioPolleriaDashboard from '../../../../src/pages/PlanNegocioPolleriaDashboard';

export default function PlanNegocioPolleriaLibraryIsland() {
  return (
    <ProtectedRoute storageKey="plan-negocio-polleria-jwt" redirectTo="/plan-negocio-polleria">
      <PlanNegocioPolleriaDashboard />
    </ProtectedRoute>
  );
}
