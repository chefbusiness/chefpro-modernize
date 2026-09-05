// ════════════════════════════════════════════════════════════════════════════
// Normalización + sinónimos del buscador del hub de productos digitales.
//
// POR QUÉ ESTE MÓDULO EXISTE: la normalización estaba DUPLICADA byte a byte en
// el frontmatter de ProductosDigitalesHubPage.astro (que genera `data-search`)
// y en su <script> de cliente (que normaliza lo que teclea el visitante). Dos
// copias que nadie cruzaba: cambiar una y no la otra deja el buscador sin
// encontrar nada, SIN error, sin diff que cante y con el build en verde — el
// patrón «gates que no fallan pero dejan pasar el error» del CLAUDE.md.
//
// Ahora hay una sola definición, importada desde los dos sitios (Astro bundlea
// los imports del <script> igual que los del frontmatter). Los sinónimos viven
// en `sinonimos-buscador.json` para que además los pueda leer sin parsear TS
// scripts/productos-digitales/buscador-report.py (el informe de demanda cruza
// las consultas contra el catálogo con LA MISMA expansión que el buscador; si
// no, marca como «demanda no cubierta» cosas que la tienda sí vende).
//
// ⚠ La normalización del SERVIDOR (netlify/functions/log-search.ts) y la del
// informe (buscador-report.py) tienen que producir la MISMA cadena que ésta, o
// «APPCC.», «appcc?» y «appcc» se agregan como tres consultas distintas y el
// umbral --min-veces no se alcanza nunca. Están alineadas a mano y con un
// comentario recíproco en cada fichero.
// ════════════════════════════════════════════════════════════════════════════
import datos from './sinonimos-buscador.json';

/** Sinónimos de una palabra (prefijo ≥3 letras dispara todo el grupo). */
export const GRUPOS_SINONIMOS: string[][] = datos.grupos;

/** Sinónimos de varias palabras; se expanden sobre la consulta entera. */
export const FRASES_SINONIMAS: string[][] = datos.frases;

/** Términos extra por slug de producto (vocabulario LATAM y palabras ausentes de la ficha). */
export const ALIAS_BUSQUEDA: Record<string, string> = datos.alias;

/** minúsculas · sin acentos (ñ→n) · puntuación y cualquier no-alfanumérico → espacio. */
export function normalizarBusqueda(s: string): string {
  return (s || '')
    .toLowerCase()
    .normalize('NFD')
    .replace(/[\u0300-\u036f]/g, '')
    .replace(/[^a-z0-9]+/g, ' ')
    .trim();
}

/**
 * Índice de búsqueda de una card: normaliza y DEDUPLICA los tokens.
 * El deduplicado no cambia ningún acierto (el matcher pregunta por presencia de
 * token, no por frecuencia) y quita ~9,1 KB de HTML del hub: los nombres de los
 * 46 productos repiten «restaurante», «excel», «plantillas», «tareas»…
 */
export function indiceBusqueda(partes: (string | undefined)[]): string {
  const plano = normalizarBusqueda(partes.filter(Boolean).join(' '));
  if (!plano) return '';
  const vistos = new Set<string>();
  const out: string[] = [];
  for (const token of plano.split(' ')) {
    if (!token || vistos.has(token)) continue;
    vistos.add(token);
    out.push(token);
  }
  return out.join(' ');
}

/**
 * Gate de grupos huérfanos: un grupo de sinónimos cuyos miembros no aparecen en
 * NINGÚN índice no puede disparar jamás — el visitante teclea «planilla», ve
 * «No tenemos nada para…» y el registro anota demanda no cubierta falsa. Le
 * pasaba al grupo nomina/planilla, que llevaba vivo desde el primer día sin que
 * ninguna de sus 4 palabras estuviera en un solo producto.
 * Devuelve los grupos muertos (vacío = todo correcto).
 */
export function gruposHuerfanos(indices: string[]): string[][] {
  const corpus = ' ' + indices.join(' ') + ' ';
  return GRUPOS_SINONIMOS.filter(
    (grupo) => !grupo.some((termino) => corpus.indexOf(' ' + termino + ' ') !== -1),
  );
}
