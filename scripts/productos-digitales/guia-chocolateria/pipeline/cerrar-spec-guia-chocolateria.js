export const meta = {
  name: 'cerrar-spec-guia-chocolateria',
  description: 'Cerrar la SPEC de «Cómo Montar una Chocolatería»: aplicar los 11 hallazgos de la ronda 3 (con la política del orquestador sobre D53: el kit 2.1 es decisión de John, no bloquea) y re-verificar hasta LISTO (máx. 2 rondas más)',
  phases: [
    { title: 'Fix r3', detail: 'fixer opus sobre los 11 hallazgos de la ronda 3' },
    { title: 'Verificar', detail: 're-refutación opus; si no LISTO, un fixer más y última verificación' },
  ],
}
const FECHA = args.fecha
const SP = args.scratchpad
const A = 'scripts/productos-digitales/auditorias'
const PD = 'scripts/productos-digitales'
const SPEC = `${PD}/guia-chocolateria-SPEC.md`
const LEGAL_JSON = `${A}/guia-chocolateria-verificacion-legal-${FECHA}.json`
const R3 = `${A}/guia-chocolateria-SPEC-refutacion-${FECHA}-r3.md`

const CONTEXTO = `
## CONTEXTO
Producto NUEVO nº 5 de AI Chef Pro: «Cómo Montar una Chocolatería», 65 €, slug \`guia-chocolateria-obrador\`, hermana de la Guía «Cómo Montar
una Pastelería» y construida con su MISMO pipeline. Fecha: ${FECHA}. La SPEC \`${SPEC}\` (849 líneas, §0-§10 + Cierre, D1-D53) ya pasó dos
rondas de refutación con fixer (23 + 15 fixes). La ronda 3 (\`${R3}\`) dejó 11 hallazgos (2 altas · 4 medias · 5 bajas) SIN aplicar.
Fuentes de verdad: decisiones firmadas \`${PD}/guia-chocolateria-DECISIONES-${FECHA}.md\` (D1-D18, no se reabren) · verificación legal
\`${LEGAL_JSON}\` + \`${A}/guia-chocolateria-verificacion-legal-${FECHA}.md\` (manda sobre todo lo demás) · JSON común
\`${A}/guias-v2-research-sector.json\` (635 entradas; los ids se citan con sufijo cuando sólo existen con sufijo, D44) · kit publicado
\`astro-site/public/dl/kit-tareas-chocolateria/\` (11 xlsx; openpyxl read_only, UNO cada vez) · molde \`${PD}/guia-pasteleria-SPEC.md\`.
**POLÍTICA DEL ORQUESTADOR SOBRE D53 (kit de Chocolatería 2.0 → 2.1), que el fixer aplica y el verificador respeta:** regenerar un producto
VENDIDO (12 €) es una decisión de John, no del orquestador (precedente: el kit de Pastelería 2.1 fue «decisión de John, preguntado»; regla
«un dictado = sólo ese cambio»). Por tanto D53 se REFORMULA: (a) los ocho alérgenos de CHN-34b y la humedad 50-60 % son lo que la GUÍA
publica, sin discusión; (b) la regeneración del kit a 2.1 (alérgenos en sus tres celdas de declaración + humedad unificada + changelog +
broadcast propio) pasa a §10 como PROPUESTA para John con su coste (≈0,15 M) y su efecto en la cola de Resend; (c) **no bloquea el cap. 12**:
el capítulo publica los ocho alérgenos legales y añade una nota-puente para quien tiene el kit («si usas el Kit de Tareas Chocolatería,
desglosa la celda “frutos secos” en cacahuetes, frutos de cáscara y sésamo, que son entradas independientes del Anexo II»); (d) el gate de
§8.2 sobre las tres celdas del kit y las filas de §8.1 sobre el kit 2.1 se marcan «SI John aprueba D53»; (e) §7.3: el hueco de la guía es
el 24-oct salvo que John apruebe el kit 2.1 (entonces kit 24-oct y guía 29-oct), siempre confirmado con GET /broadcasts.
Repo PÚBLICO. Térmica: \`istats cpu temp\` antes de cada python; un fichero cada vez; si ≥ 63 °C espera 60 s; sin builds ni navegador;
\`/usr/local/bin/python3\`.`

const FIX_SCHEMA = { type: 'object', properties: { aplicados: { type: 'integer' }, descartados: { type: 'array', items: { type: 'string' } }, lineas: { type: 'integer' }, d53_reformulada: { type: 'boolean' }, avisos: { type: 'array', items: { type: 'string' } } }, required: ['aplicados', 'descartados', 'lineas', 'd53_reformulada', 'avisos'] }
const REF_SCHEMA = {
  type: 'object',
  properties: {
    fichero: { type: 'string' }, veredicto: { type: 'string', enum: ['LISTO', 'CORREGIR ANTES', 'NO LISTO'] },
    altas: { type: 'integer' }, medias: { type: 'integer' }, bajas: { type: 'integer' },
    hallazgos: { type: 'array', items: { type: 'object', properties: { id: { type: 'string' }, gravedad: { type: 'string' }, problema: { type: 'string' }, fix: { type: 'string' } }, required: ['id', 'gravedad', 'problema', 'fix'] } },
  },
  required: ['fichero', 'veredicto', 'altas', 'medias', 'bajas', 'hallazgos'],
}

const fixer = (ronda, informe, hallazgosTxt) => agent(`# FIXER DE LA SPEC — ronda ${ronda}
${CONTEXTO}
## ENCARGO
Aplica en \`${SPEC}\` TODOS los hallazgos de \`${informe}\` (léelo entero), editando en el sitio (no reescribas secciones que no toca un
hallazgo). Si un hallazgo es incorrecto, descártalo con motivo (id → motivo). Aplica ADEMÁS la política del orquestador sobre D53
(reformular D53, §7.3, §8.1 filas del kit, §8.2 gates del kit, §10, cap. 12 de §4 y la lista negra si cita el bloqueo). Mantén las 12
secciones H2 y actualiza la tabla del Cierre y el recuento de decisiones. Verifica literales legales contra \`${LEGAL_JSON}\` y los ids
contra el JSON común antes de escribirlos. Al terminar, autocomprobación: \`grep -c '^## '\` = 12; cero ids «bare» de D44 fuera de la fila
D44; la lista de cruces entre libros es UNA sola (misma cifra en D32, §2.3, §2.5 y §8.2); D20 y §9 y §10 dan las mismas cifras de
presupuesto; §0 y §7.1/§8.1 dan el mismo número de páginas /usos/; §0 y §7.3 dan la misma fecha de Resend. Hallazgos:
${hallazgosTxt}
Devuelve el objeto.`, { label: `fix-spec-r${ronda}`, phase: ronda === 3 ? 'Fix r3' : 'Verificar', schema: FIX_SCHEMA, model: 'opus', effort: 'high' })

const verificar = (ronda, prevInforme, n) => agent(`# RE-VERIFICACIÓN DE LA SPEC — ronda ${ronda}
${CONTEXTO}
## ENCARGO
Objeto: \`${SPEC}\`. Comprueba PRIMERO que los ${n} hallazgos de \`${prevInforme}\` quedaron aplicados sin abrir contradicciones nuevas
(cita línea), y que la política del orquestador sobre D53 está aplicada en D53, §4 (cap. 12), §7.3, §8.1, §8.2 y §10 de forma coherente.
DESPUÉS, sólo lo transversal que una costura puede haber roto: (1) una sola lista de cruces entre libros con la misma cifra en D32, §2.3,
§2.5 y §8.2, y que el cruce 7←2 no vuelve a producir dos inversiones totales (el fondo de maniobra se cuenta UNA vez); (2) presupuesto:
D20 = §9 = §10, sumado fila a fila; (3) §0 ↔ §7 ↔ §8 (páginas /usos/, fecha de Resend, 49 en catálogo, 14 claves de PRODUCT_FILES = los
9 nombres de fichero de D49 + PDF/DOCX); (4) cero ids «bare» de D44 fuera de la fila D44 y cero ids inexistentes en el JSON común
(grep de todos los CHN-/CHS- de la SPEC contra el JSON); (5) ningún literal legal contradice \`${LEGAL_JSON}\` (muestra: D5/EUDR, D37
bases del RD 1055/2003 con CHN-10, D47, D48, convenio CHN-65c, alérgenos CHN-34b). No reabras lo que la ronda 3 dio por verificado
(su tabla «Lo que SÍ está verificado») salvo que un fix lo haya tocado. Veredicto LISTO si no queda ninguna alta ni media; las bajas
residuales se listan igualmente con su fix. Escribe \`${A}/guia-chocolateria-SPEC-refutacion-${FECHA}-r${ronda}.md\`. Devuelve el objeto.`,
  { label: `verificar-spec-r${ronda}`, phase: 'Verificar', schema: REF_SCHEMA, model: 'opus', effort: 'high' })

phase('Fix r3')
const fix3 = await fixer(3, R3, '(los 11 del informe: R3-A1, R3-A2, R3-M1…M4, R3-B1…B5)')
if (!fix3) throw new Error('fixer r3 sin resultado')
log(`Fixer r3: ${fix3.aplicados} aplicados · ${fix3.descartados.length} descartados · D53 reformulada: ${fix3.d53_reformulada} · ${fix3.lineas} líneas`)

phase('Verificar')
let ref = await verificar(4, R3, 11)
if (!ref) throw new Error('verificación r4 sin resultado')
log(`Verificación r4: ${ref.veredicto} · ${ref.altas}/${ref.medias}/${ref.bajas}`)
const rondas = [ref]
const fixes = [fix3]
if (ref.veredicto !== 'LISTO') {
  const txt = ref.hallazgos.map((h) => `- ${h.id} [${h.gravedad}] ${h.problema.slice(0, 300)} → FIX: ${h.fix.slice(0, 300)}`).join('\n')
  const fix4 = await fixer(4, ref.fichero, txt)
  fixes.push(fix4)
  log(`Fixer r4: ${fix4 ? fix4.aplicados : 0} aplicados`)
  const ref5 = await verificar(5, ref.fichero, ref.hallazgos.length)
  if (!ref5) throw new Error('verificación r5 sin resultado')
  rondas.push(ref5)
  ref = ref5
  log(`Verificación r5: ${ref.veredicto} · ${ref.altas}/${ref.medias}/${ref.bajas}`)
}
return { fixes, verificaciones: rondas, veredicto_final: ref.veredicto, bajas_residuales: ref.hallazgos }