// Loader de Node para renderizar .astro sueltos SIN Vite ni build del sitio (ver comparar.mjs).
// Compila con @astrojs/compiler con las MISMAS opciones que astro/dist/core/compile/compile.js
// (compact = compressHTML, internalURL, resolvePath, renderScript) y transpila TS con esbuild.
// Los paquetes se resuelven desde ASTRO_NM: un node_modules con astro 5.18.2 y @astrojs/compiler
// 2.13.1 (las versiones del package-lock de astro-site), porque este repo no instala astro en el Mac.
import fs from 'node:fs';
import { fileURLToPath, pathToFileURL } from 'node:url';

const NM = process.env.ASTRO_NM;
if (!NM) throw new Error('ASTRO_NM sin definir: ruta a un node_modules con astro 5.18.2 y @astrojs/compiler 2.13.1');
const { transform } = await import(NM + '/@astrojs/compiler/dist/node/index.js');
const esb = await import(NM + '/esbuild/lib/main.js');
const esbuildTransform = esb.transform || esb.default.transform;
const NM_PARENT = pathToFileURL(NM + '/../package.json').href;
const SHIM = 'import.meta.env = globalThis.__ENV__ || {};\n';

export async function resolve(spec, ctx, next) {
  if (/^[./]/.test(spec) || spec.startsWith('file:') || spec.startsWith('node:')) {
    if (/\.(astro|ts|tsx|json|mjs|js)$/.test(spec) || spec.startsWith('node:') || spec.includes('?')) return next(spec, ctx);
    try { return await next(spec, ctx); } catch { return next(spec + '.ts', ctx); }
  }
  try { return await next(spec, ctx); } catch { return next(spec, { ...ctx, parentURL: NM_PARENT }); }
}

export async function load(url, ctx, next) {
  if (url.includes('.astro?astro&type=style') || url.endsWith('.css')) return { format: 'module', source: '', shortCircuit: true };
  if (url.endsWith('.astro')) {
    const p = fileURLToPath(url);
    const r = await transform(fs.readFileSync(p, 'utf8'), {
      filename: p, normalizedFilename: p, compact: true, internalURL: 'astro/compiler-runtime',
      resultScopedSlot: true, scopedStyleStrategy: 'attribute', renderScript: true,
      astroGlobalArgs: JSON.stringify('https://aichef.pro'), resolvePath: async (s) => s,
    });
    const errs = r.diagnostics.filter((d) => d.severity === 1);
    if (errs.length) throw new Error('astro compile ' + p + ': ' + errs.map((e) => e.text).join('; '));
    const js = await esbuildTransform(r.code, { loader: 'ts', format: 'esm' });
    return { format: 'module', source: SHIM + js.code, shortCircuit: true };
  }
  if (url.endsWith('.ts')) {
    const js = await esbuildTransform(fs.readFileSync(fileURLToPath(url), 'utf8'), { loader: 'ts', format: 'esm' });
    return { format: 'module', source: SHIM + js.code, shortCircuit: true };
  }
  if (url.endsWith('.json') && url.startsWith('file:') && !url.includes('node_modules')) {
    return { format: 'module', source: 'export default ' + fs.readFileSync(fileURLToPath(url), 'utf8'), shortCircuit: true };
  }
  return next(url, ctx);
}
