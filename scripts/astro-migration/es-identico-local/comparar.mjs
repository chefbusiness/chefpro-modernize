// ¿Sale BYTE A BYTE igual el HTML de las landings ES tras tocar una plantilla de la tienda? — sin build.
//
// Por qué: la condición dura de la tienda internacional (TIENDA-INTERNACIONAL.md §3.4) es que, al dar `lang`
// a una plantilla, sus landings ES no cambien ni un byte. `tienda-gate.py --es-identico` lo mide contra
// producción, pero solo con un deploy preview. En el Mac no se puede construir el sitio (regla térmica), así
// que esto renderiza la plantilla de antes (git show <ref>) y la de ahora con CADA ficha ES, con el Container
// API de Astro y las mismas opciones de compilación que el build, y compara. Lo usó por primera vez la F3 del
// Restaurant Checklists Kit Pro (17-oct-2026): KitTareasLandingPage, 20 fichas × 2 modos de cripto.
// Alcance: el HTML del COMPONENTE (no el BaseLayout ni el <head>); el gate del preview sigue siendo la prueba final.
//
// Uso (desde la raíz del repo; ~10 s, CPU ligera):
//   node --import ./scripts/astro-migration/es-identico-local/register.mjs \
//        scripts/astro-migration/es-identico-local/comparar.mjs \
//        --plantilla components/pages/KitTareasLandingPage.astro --fichas data/productos/tareas [--ref main] \
//        [--en data/productos-en/tareas --salida <dir>]
//   ASTRO_NM=<node_modules con astro 5.18.2> si no está en la ruta por defecto (ver loader.mjs).
// Sale 1 si alguna ficha ES difiere y enseña el contexto del primer byte distinto. Mutación comprobada: un
// espacio de más en es.json → 40/40 distintas.
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import { execFileSync } from 'node:child_process';
import { fileURLToPath } from 'node:url';

const REPO = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '../../..');
const arg = (k, d) => { const i = process.argv.indexOf(k); return i > 0 ? process.argv[i + 1] : d; };
const plantilla = arg('--plantilla');
const fichasDir = arg('--fichas');
const ref = arg('--ref', 'main');
const enDir = arg('--en');
const salida = arg('--salida');
if (!plantilla || !fichasDir) { console.error('faltan --plantilla y --fichas'); process.exit(2); }

const tmp = fs.mkdtempSync(path.join(os.tmpdir(), 'es-identico-'));
const SRC = path.join(tmp, 'src');
for (const d of ['components', 'lib', 'i18n', 'data']) fs.cpSync(path.join(REPO, 'astro-site/src', d), path.join(SRC, d), { recursive: true });
const nuevoPath = path.join(SRC, plantilla);
const origPath = nuevoPath.replace(/\.astro$/, '.orig.astro');
fs.writeFileSync(origPath, execFileSync('git', ['-C', REPO, 'show', `${ref}:astro-site/src/${plantilla}`]));

const { experimental_AstroContainer } = await import('astro/container');
const Nuevo = (await import(nuevoPath)).default;
const Viejo = (await import(origPath)).default;
const c = await experimental_AstroContainer.create();
const base = path.basename(nuevoPath);
const norm = (h) => h.replace(/astro-cid-[a-z0-9]+/g, 'astro-cid-X').split(base.replace('.astro', '.orig.astro')).join(base);
const fichas = fs.readdirSync(path.join(SRC, fichasDir)).filter((f) => f.endsWith('.ts') && f !== 'types.ts');
let ok = 0, ko = 0;
for (const [modo, cripto] of [['sin-cripto', undefined], ['cripto-all', 'all']]) {
  if (cripto) process.env.CRYPTO_PRODUCTS = cripto; else delete process.env.CRYPTO_PRODUCTS;
  for (const f of fichas) {
    const data = (await import(path.join(SRC, fichasDir, f) + '?' + modo)).default;
    const props = { data, stripeLink: '#comprar' };
    const a = norm(await c.renderToString(Viejo, { props }));
    const b = norm(await c.renderToString(Nuevo, { props }));
    if (a === b) { ok++; continue; }
    ko++;
    let i = 0; while (i < a.length && a[i] === b[i]) i++;
    console.log(`DIFIERE ${modo} ${f} byte ${i}\n  antes: ${JSON.stringify(a.slice(Math.max(0, i - 150), i + 150))}\n  ahora: ${JSON.stringify(b.slice(Math.max(0, i - 150), i + 150))}`);
  }
}
console.log(`ES idénticas: ${ok} · distintas: ${ko} (${fichas.length} fichas × 2 modos de cripto; ref ${ref})`);
if (enDir) {
  process.env.CRYPTO_PRODUCTS = 'all';
  for (const f of fs.readdirSync(path.join(SRC, enDir)).filter((x) => x.endsWith('.ts'))) {
    const data = (await import(path.join(SRC, enDir, f))).default;
    const h = await c.renderToString(Nuevo, { props: { data, stripeLink: '#comprar', lang: 'en' } });
    if (salida) { fs.mkdirSync(salida, { recursive: true }); fs.writeFileSync(path.join(salida, f.replace('.ts', '-en.html')), h); }
    console.log(`EN ${f}: ${h.length} bytes${salida ? ' → ' + salida : ''}`);
  }
}
fs.rmSync(tmp, { recursive: true, force: true });
process.exit(ko ? 1 : 0);
