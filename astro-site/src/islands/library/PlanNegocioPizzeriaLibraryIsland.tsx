/**
 * Island de /plan-negocio-pizzeria-library (Fase 5, GENERADO por scripts/astro-migration/
 * fase5-generate-zona-app.py — editar el generador, no este fichero).
 * Réplica exacta de la composición de la SPA para esta ruta en App.tsx:
 * storageKey/redirectTo extraídos VERBATIM de App.tsx por el generador.
 */
import ProtectedRoute from '../../../../src/components/shared/ProtectedRoute';
import PlanNegocioPizzeriaDashboard from '../../../../src/pages/PlanNegocioPizzeriaDashboard';

export default function PlanNegocioPizzeriaLibraryIsland() {
  return (
    <ProtectedRoute storageKey="plan-negocio-pizzeria-jwt" redirectTo="/plan-negocio-pizzeria">
      <PlanNegocioPizzeriaDashboard />
    </ProtectedRoute>
  );
}
