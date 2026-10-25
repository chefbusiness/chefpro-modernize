/**
 * Island de /plan-negocio-heladeria-library (Fase 5, GENERADO por scripts/astro-migration/
 * fase5-generate-zona-app.py — editar el generador, no este fichero).
 * Réplica exacta de la composición de la SPA para esta ruta en App.tsx:
 * storageKey/redirectTo extraídos VERBATIM de App.tsx por el generador.
 */
import ProtectedRoute from '../../../../src/components/shared/ProtectedRoute';
import PlanNegocioHeladeriaDashboard from '../../../../src/pages/PlanNegocioHeladeriaDashboard';

export default function PlanNegocioHeladeriaLibraryIsland() {
  return (
    <ProtectedRoute storageKey="plan-negocio-heladeria-jwt" redirectTo="/plan-negocio-heladeria">
      <PlanNegocioHeladeriaDashboard />
    </ProtectedRoute>
  );
}
