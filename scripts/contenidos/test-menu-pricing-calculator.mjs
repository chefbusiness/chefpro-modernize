// Prueba en node de la lógica de /en/menu-pricing-calculator (sin navegador: el Mac no usa Playwright).
// Extrae las funciones entre MPC-CALC-START/END de la página y comprueba los números del texto.
import { readFileSync } from 'node:fs';
import vm from 'node:vm';
import assert from 'node:assert/strict';
const page = readFileSync(new URL('../../astro-site/src/pages/en/menu-pricing-calculator.astro', import.meta.url), 'utf8');
const code = page.split('/* MPC-CALC-START */')[1].split('/* MPC-CALC-END */')[0];
const ctx = {}; vm.createContext(ctx); vm.runInContext(code + ';this.c=mpcCompute;this.r=mpcRoundUp;this.v=mpcReverse;', ctx);
const r2 = (x) => Math.round(x * 100) / 100, r1 = (x) => Math.round(x * 10) / 10;
let r = ctx.c(4.29, 30, '0.95', 0, false);
assert.equal(r2(r.exactNet), 14.3); assert.equal(r.menu, 14.95); assert.equal(r1(r.realPct), 28.7); assert.equal(r2(r.gp), 10.66); assert.equal(r2(r.markup), 3.33);
for (const [t, p, g] of [[25, 17.16, 12.87], [28, 15.32, 11.03], [30, 14.3, 10.01], [32, 13.41, 9.12], [35, 12.26, 7.97]]) { const x = ctx.c(4.29, t, 'none', 0, false); assert.equal(x.menu, p); assert.equal(r2(x.gp), g); }
assert.equal(ctx.r(14.3, '0.99'), 14.99); assert.equal(ctx.r(14.3, '0.5'), 14.5); assert.equal(ctx.r(14.6, '0.5'), 15); assert.equal(ctx.r(14.51, '0.5'), 15); assert.equal(ctx.r(15, '0.5'), 15); assert.equal(ctx.r(15.01, '0.5'), 15.5); assert.equal(ctx.r(14.3, '0'), 15); assert.equal(ctx.r(15, '0'), 15); assert.equal(ctx.r(14.96, '0.95'), 15.95); assert.equal(ctx.r(14.95, '0.95'), 14.95);
r = ctx.c(4.29, 30, '0.95', 20, true); // UK, IVA incluido 20 %: 14,30 × 1,2 = 17,16 → 17,95; neto 14,958…
assert.equal(r2(r.exactShown), 17.16); assert.equal(r.menu, 17.95); assert.equal(r1(r.realPct), 28.7);
r = ctx.c(4.29, 30, '0.95', 8.875, false); assert.equal(r.menu, 14.95); assert.equal(r2(r.withTax), 16.28); // EE. UU., impuesto aparte
assert.equal(r1(ctx.v(4.29, 14.95, 0, false)), 28.7); assert.equal(r1(ctx.v(4.29, 17.95, 20, true)), 28.7);
assert.equal(ctx.c(0, 30, '0.95', 0, false), null); assert.equal(ctx.c(4.29, 0, '0.95', 0, false), null); assert.equal(ctx.c(4.29, 100, '0.95', 0, false), null);
assert.equal(ctx.c(4.29, 0.5, '0.95', 0, false), null); assert.equal(ctx.c(4.29, 99.5, '0.95', 0, false), null); assert.equal(ctx.c(4.29, 30, '0.95', -5, false), null); assert.equal(ctx.c(4.29, 30, '0.95', 60, false), null); assert.equal(ctx.c(0.001, 30, 'none', 0, false), null);
assert.equal(ctx.v(4.29, 14.95, -1, false), null); assert.ok(Number.isFinite(ctx.c(0.01, 99, 'none', 0, false).realPct));
console.log('OK menu-pricing-calculator: 14,30 → 14,95 · 28,7 % · tabla 25-35 % · redondeos · IVA incluido y aparte · inverso');
