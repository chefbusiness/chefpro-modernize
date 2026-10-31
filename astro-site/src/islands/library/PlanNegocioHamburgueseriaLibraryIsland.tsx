/**
 * Island de /plan-negocio-hamburgueseria-library (Fase 5, GENERADO por scripts/astro-migration/
 * fase5-generate-zona-app.py — editar el generador, no este fichero).
 * Réplica exacta de la composición de la SPA para esta ruta en App.tsx:
 * storageKey/redirectTo extraídos VERBATIM de App.tsx por el generador.
 */
import ProtectedRoute from '../../../../src/components/shared/ProtectedRoute';
import PlanNegocioHamburgueseriaDashboard from '../../../../src/pages/PlanNegocioHamburgueseriaDashboard';

export default function PlanNegocioHamburgueseriaLibraryIsland() {
  return (
    <ProtectedRoute storageKey="plan-negocio-hamburgueseria-jwt" redirectTo="/plan-negocio-hamburgueseria">
      <PlanNegocioHamburgueseriaDashboard />
    </ProtectedRoute>
  );
}
