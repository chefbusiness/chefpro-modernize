/**
 * Island de /guia-churreria-chocolateria-library (Fase 5, GENERADO por scripts/astro-migration/
 * fase5-generate-zona-app.py — editar el generador, no este fichero).
 * Réplica exacta de la composición de la SPA para esta ruta en App.tsx:
 * storageKey/redirectTo extraídos VERBATIM de App.tsx por el generador.
 */
import ProtectedRoute from '../../../../src/components/shared/ProtectedRoute';
import GuiaChurreriaChocolateriaDashboard from '../../../../src/pages/GuiaChurreriaChocolateriaDashboard';

export default function GuiaChurreriaChocolateriaLibraryIsland() {
  return (
    <ProtectedRoute storageKey="guia-churreria-chocolateria-jwt" redirectTo="/guia-churreria-chocolateria">
      <GuiaChurreriaChocolateriaDashboard />
    </ProtectedRoute>
  );
}
