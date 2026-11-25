// Quita los bytes NUL (\x00) de los HTML generados en dist/.
//
// POR QUÉ: el render en streaming de react-dom 18.3 (renderToReadableStream, que usa
// @astrojs/react para los islands) deja bytes NUL de relleno junto a caracteres
// multibyte («50\x00\x00€», «avan\x00çadas», «f\x00ür»). El navegador los ignora, pero
// un rastreador o un LLM que lea el HTML en bruto ve palabras partidas. El carácter
// real sigue a continuación del NUL, así que quitarlos no pierde texto. Un NUL nunca
// es contenido legítimo en HTML.
//
// Se ejecuta después de `astro build` (ver package.json). Imprime el recuento.
import { readdir, readFile, writeFile } from 'node:fs/promises';
import { join } from 'node:path';
import { fileURLToPath } from 'node:url';

const DIST = fileURLToPath(new URL('../dist/', import.meta.url));
const root = process.argv[2] || DIST;

async function* htmlFiles(dir) {
  for (const entry of await readdir(dir, { withFileTypes: true })) {
    const p = join(dir, entry.name);
    if (entry.isDirectory()) yield* htmlFiles(p);
    else if (entry.name.endsWith('.html')) yield p;
  }
}

let files = 0;
let bytes = 0;
for await (const file of htmlFiles(root)) {
  const buf = await readFile(file);
  let n = 0;
  for (const b of buf) if (b === 0) n++;
  if (n === 0) continue;
  await writeFile(file, buf.filter((b) => b !== 0));
  files++;
  bytes += n;
}
console.log(`strip-nul-bytes: ${bytes} bytes NUL quitados en ${files} ficheros HTML`);
