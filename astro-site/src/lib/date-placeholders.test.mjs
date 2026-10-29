import assert from 'node:assert/strict';
import test from 'node:test';
import {
  applyDatePlaceholdersToHtml,
  findUnresolvedSeoPlaceholders,
  resolveDatePlaceholders,
} from './date-placeholders.mjs';

// 31 dic 23:30 UTC es ya 1 ene en Europe/Madrid (CET, UTC+1).
const MADRID_NEW_YEAR = new Date('2026-12-31T23:30:00.000Z');
// 31 dic 22:30 UTC sigue siendo 31 dic 23:30 en Madrid.
const MADRID_STILL_DECEMBER = new Date('2026-12-31T22:30:00.000Z');

test('31 dic 23:30 UTC es 1 de enero en Madrid', () => {
  assert.equal(resolveDatePlaceholders('año {year}', MADRID_NEW_YEAR, 'es'), 'año 2027');
  assert.equal(resolveDatePlaceholders('mes {month}', MADRID_NEW_YEAR, 'es'), 'mes enero');
  assert.equal(
    resolveDatePlaceholders('{month} {year}', MADRID_NEW_YEAR, 'en'),
    'January 2027',
  );
  assert.equal(resolveDatePlaceholders('{month}', MADRID_NEW_YEAR, 'fr'), 'janvier');
  assert.equal(resolveDatePlaceholders('{month}', MADRID_NEW_YEAR, 'de'), 'Januar');
  assert.equal(resolveDatePlaceholders('{month}', MADRID_NEW_YEAR, 'it'), 'gennaio');
  assert.equal(resolveDatePlaceholders('{month}', MADRID_NEW_YEAR, 'pt'), 'janeiro');
  assert.equal(resolveDatePlaceholders('{month}', MADRID_NEW_YEAR, 'nl'), 'januari');
});

test('31 dic 22:30 UTC sigue siendo diciembre en Madrid', () => {
  assert.equal(
    resolveDatePlaceholders('{month} de {year}', MADRID_STILL_DECEMBER, 'es'),
    'diciembre de 2026',
  );
  assert.equal(resolveDatePlaceholders('{month}', MADRID_STILL_DECEMBER, 'nl'), 'december');
  assert.equal(resolveDatePlaceholders('{month}', MADRID_STILL_DECEMBER, 'fr'), 'décembre');
  assert.equal(resolveDatePlaceholders('{month}', MADRID_STILL_DECEMBER, 'de'), 'Dezember');
});

test('no reescribe años reales, precios ni tokens parecidos', () => {
  const input = 'Guía 2026 por 24 EUR (95,00 €) — RD 1420/2006, desde 2010. {yearly} {Year} { year } {month}';
  const out = resolveDatePlaceholders(input, MADRID_NEW_YEAR, 'es');
  assert.equal(
    out,
    'Guía 2026 por 24 EUR (95,00 €) — RD 1420/2006, desde 2010. {yearly} {Year} { year } enero',
  );
  assert.equal(resolveDatePlaceholders('sin tokens 2024', MADRID_NEW_YEAR, 'es'), 'sin tokens 2024');
});

test('repite tokens y respeta el idioma pedido', () => {
  assert.equal(
    resolveDatePlaceholders('{year}/{year} en {month}', MADRID_NEW_YEAR, 'es'),
    '2027/2027 en enero',
  );
  assert.equal(resolveDatePlaceholders('{month}', MADRID_NEW_YEAR, 'pt-PT'), 'janeiro');
  assert.equal(resolveDatePlaceholders('', MADRID_NEW_YEAR, 'es'), '');
});

test('now inválido no lanza y usa la fecha actual', () => {
  const out = resolveDatePlaceholders('x {year}', new Date('nope'), 'es');
  assert.match(out, /^x 20\d{2}$/);
});

test('el HTML de build resuelve solo los campos SEO', () => {
  const html = `<!doctype html>
<html lang="es">
<head>
<title>Guía {year} — 24 EUR</title>
<meta name="description" content="Actualizado en {month} de {year}. Precio 95,00 €." />
<meta property="og:title" content="OG {year}" />
<meta name="twitter:title" content="TW {month} {year}" />
<meta property="og:description" content="También en {month} de {year}. 24 EUR." />
<meta property="og:image:alt" content="el alt no es un title y conserva {year}" />
<script type="application/ld+json">{"headline":"Post {month} {year}","priceValidUntil":"2026-12-31"}</script>
</head>
<body>
<h1 class="x">Hola {month} <span>de {year}</span></h1>
<p>En 2026 el precio es 24 EUR y el token {year} del cuerpo se queda.</p>
</body>
</html>`;

  assert.ok(findUnresolvedSeoPlaceholders(html).length > 0);
  const out = applyDatePlaceholdersToHtml(html, MADRID_NEW_YEAR);

  assert.match(out, /<title>Guía 2027 — 24 EUR<\/title>/);
  assert.match(out, /content="Actualizado en enero de 2027\. Precio 95,00 €\."/);
  assert.match(out, /property="og:title" content="OG 2027"/);
  assert.match(out, /property="og:description" content="También en enero de 2027\. 24 EUR\."/);
  assert.match(out, /name="twitter:title" content="TW enero 2027"/);
  assert.match(out, /<h1 class="x">Hola enero <span>de 2027<\/span><\/h1>/);
  assert.match(out, /"headline":"Post enero 2027"/);
  assert.match(out, /"priceValidUntil":"2026-12-31"/);
  assert.match(out, /content="el alt no es un title y conserva \{year\}"/);
  assert.match(out, /En 2026 el precio es 24 EUR y el token \{year\} del cuerpo se queda\./);
  assert.deepEqual(findUnresolvedSeoPlaceholders(out), []);
});

test('el mes del HTML sigue el lang de la página', () => {
  const html = '<html lang="fr"><head><title>{month}</title></head><body><h1>{month}</h1></body></html>';
  const out = applyDatePlaceholdersToHtml(html, MADRID_NEW_YEAR);
  assert.match(out, /<title>janvier<\/title>/);
  assert.match(out, /<h1>janvier<\/h1>/);
  assert.deepEqual(findUnresolvedSeoPlaceholders(out), []);
});
