/**
 * Island de /plan-negocio-taqueria-library (Fase 5, GENERADO por scripts/astro-migration/
 * fase5-generate-zona-app.py — editar el generador, no este fichero).
 * Réplica exacta de la composición de la SPA para esta ruta en App.tsx:
 * storageKey/redirectTo extraídos VERBATIM de App.tsx por el generador.
 */
import ProtectedRoute from '../../../../src/components/shared/ProtectedRoute';
import PlanNegocioTaqueriaDashboard from '../../../../src/pages/PlanNegocioTaqueriaDashboard';

export default function PlanNegocioTaqueriaLibraryIsland() {
  return (
    <ProtectedRoute storageKey="plan-negocio-taqueria-jwt" redirectTo="/plan-negocio-taqueria">
      <PlanNegocioTaqueriaDashboard />
    </ProtectedRoute>
  );
}
