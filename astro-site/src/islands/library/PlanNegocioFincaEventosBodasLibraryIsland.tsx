/**
 * Island de /plan-negocio-finca-eventos-bodas-library (Fase 5, GENERADO por scripts/astro-migration/
 * fase5-generate-zona-app.py — editar el generador, no este fichero).
 * Réplica exacta de la composición de la SPA para esta ruta en App.tsx:
 * storageKey/redirectTo extraídos VERBATIM de App.tsx por el generador.
 */
import ProtectedRoute from '../../../../src/components/shared/ProtectedRoute';
import PlanNegocioFincaEventosBodasDashboard from '../../../../src/pages/PlanNegocioFincaEventosBodasDashboard';

export default function PlanNegocioFincaEventosBodasLibraryIsland() {
  return (
    <ProtectedRoute storageKey="plan-negocio-finca-eventos-bodas-jwt" redirectTo="/plan-negocio-finca-eventos-bodas">
      <PlanNegocioFincaEventosBodasDashboard />
    </ProtectedRoute>
  );
}
