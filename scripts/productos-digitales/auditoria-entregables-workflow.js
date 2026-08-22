export const meta = {
  name: 'auditoria-entregables-producto',
  description: 'Ronda 1 adversarial de los entregables de UN producto digital (3 lentes opus: dominio, técnica Excel, coherencia) — args: {productId, familia, dominio?}',
  phases: [
    { title: 'Inventario', detail: 'sonnet: censo determinista del producto + landing/dashboard/functions', model: 'sonnet' },
    { title: 'Ronda 1', detail: '3 lentes opus en paralelo, cada una devuelve JSON de hallazgos (con schema)', model: 'opus' },
  ],
}

// Uso: Workflow({scriptPath: 'scripts/productos-digitales/auditoria-entregables-workflow.js',
//                args: {productId: 'kit-escandallos', familia: 'kit-excel'}})
// familias: 'kit-tareas' | 'guia' | 'plan' | 'kit-excel' | 'ebook'. `dominio` (opcional) afina la
// lente experta: p. ej. 'jefe de cocina de pizzería' o 'controller de costes de restaurante'.
//
// 2026-08-22: TODOS los agent() llevan `schema` — sin él devuelven el JSON como STRING y el script
// lo lee como vacío (memoria feedback_workflow-agentes-sin-schema-devuelven-string). Y la Fase A
// (saneamiento determinista: cache, A4, metadata, bio, casilla, reparaciones exactas) YA ESTÁ
// HECHA y LIVE: las lentes no deben gastar hallazgos en eso (el gate `censo-entregables.py --fail`
// lo cubre); van a CONTENIDO, LÓGICA y COHERENCIA.
const REPO = '/Users/johnguerrero/chefpro-modernize'
const pid = args && args.productId
if (!pid) throw new Error('args.productId obligatorio')
const familia = (args && args.familia) || 'kit-excel'
const DL = `${REPO}/astro-site/public/dl/${pid}`
const OUT = `${REPO}/scripts/productos-digitales/auditorias/${pid}-R1.json`

const DOMINIO = {
  'kit-tareas': 'JEFE/A DE COCINA con 20 años en el sector concreto del kit (lee el nombre del producto): realismo y orden de las tareas, horas, temperaturas, perfiles, zonas, terminología española, campañas del año; ¿lo imprimiría y se lo daría a su equipo mañana?',
  'guia': 'CONSULTOR/A DE APERTURAS DE RESTAURANTES en España: ¿las cifras (inversión, márgenes, ratios, plantillas, licencias, proveedores) son realistas y actuales? ¿qué falta para montar el negocio de verdad? ¿hay afirmaciones legales o económicas falsas o caducas?',
  'plan': 'CONSULTOR/A FINANCIERO de hostelería: coherencia del plan (inversión, P&L, punto de equilibrio, escenarios), fórmulas que enlazan hojas, supuestos razonables para España 2026, textos del docx alineados con el Excel.',
  'kit-excel': 'EXPERTO/A TÉCNICO del tema del kit (escandallos → controller de costes de restaurante que escandalla a diario; APPCC → consultor de seguridad alimentaria (RD 3484/2000, Reg. 852/2004, 1169/2011); inventario → jefe de compras; RRHH → asesor laboral; plan financiero → director financiero): ¿las plantillas resuelven el problema real? ¿fórmulas correctas y completas (mermas, rendimientos, IVA, márgenes, food cost objetivo)? ¿normativa bien citada? ¿qué le faltaría a un profesional exigente que ha pagado por esto?',
  'ebook': 'FORMADOR/A de cocina con IA: ¿los prompts funcionan tal cual copiados? ¿hay caracteres raros, fechas caducas, promesas vacías?',
}
const dominio = (args && args.dominio) ? args.dominio : DOMINIO[familia]

const RULES = 'No edites nada. Cita fichero:hoja:celda o fichero:línea. REGLA TÉRMICA: python EN SERIE y ligero, `istats cpu temp` antes de cada barrido; nada de builds ni Playwright. Devuelve el JSON según el schema.'
const FASE_A = 'CONTEXTO: la Fase A (determinista) ya está aplicada y LIVE en estos ficheros: cache de valores, A4 completo, metadata AI Chef Pro, bio anclada, línea «Versión 1.1», casilla unificada y reparaciones exactas de fórmulas rotas. NO reportes nada de eso salvo que encuentres un caso que se le escapó (y entonces dilo como tal). Lo que buscamos ahora es lo que un script no ve: contenido erróneo o pobre, lógica de negocio mal planteada, fórmulas que calculan lo que no deben, promesas de landing/dashboard que el fichero no cumple.'

const INV_SCHEMA = {
  type: 'object',
  properties: {
    productId: { type: 'string' },
    ficheros: { type: 'array', items: { type: 'object', properties: { nombre: { type: 'string' }, tipo: { type: 'string' }, bytes: { type: 'integer' }, hojas: { type: 'array', items: { type: 'string' } }, formulas: { type: 'integer' }, resumen: { type: 'string' } }, required: ['nombre', 'tipo'] } },
    dashboard: { type: 'array', items: { type: 'object', properties: { key: { type: 'string' }, title: { type: 'string' }, ruta: { type: 'string' } }, required: ['key'] } },
    landing: { type: 'object', properties: { productName: { type: 'string' }, cifras_prometidas: { type: 'array', items: { type: 'string' } }, entregables_prometidos: { type: 'array', items: { type: 'string' } }, faqs: { type: 'array', items: { type: 'string' } }, bonus: { type: 'array', items: { type: 'string' } } } },
    emails: { type: 'object', properties: { verify: { type: 'string' }, resend: { type: 'string' } } },
    changelog: { type: 'string' },
    gate: { type: 'string' },
    notas: { type: 'array', items: { type: 'string' } },
  },
  required: ['productId', 'ficheros', 'dashboard', 'landing', 'gate'],
}
const HALLAZGOS_SCHEMA = {
  type: 'object',
  properties: {
    lente: { type: 'string' },
    hallazgos: { type: 'array', maxItems: 40, items: { type: 'object', properties: { id: { type: 'string' }, severidad: { type: 'string', enum: ['alta', 'media', 'baja'] }, fichero: { type: 'string' }, ubicacion: { type: 'string' }, hallazgo: { type: 'string' }, evidencia: { type: 'string' }, fix: { type: 'string' } }, required: ['id', 'severidad', 'fichero', 'ubicacion', 'hallazgo', 'evidencia', 'fix'] } },
    veredicto: { type: 'string', enum: ['listo', 'no listo'] },
    motivo: { type: 'string' },
  },
  required: ['lente', 'hallazgos', 'veredicto', 'motivo'],
}

phase('Inventario')
const inv = await agent(`Repo ${REPO}. Producto digital «${pid}» (familia ${familia}). ${FASE_A} Haz un INVENTARIO determinista: (1) ficheros de ${DL}/ (nombre, tipo, bytes; para cada xlsx con openpyxl: hojas, nº fórmulas y un resumen de una línea de qué hace cada hoja; para docx, python-docx: nº párrafos y títulos; pdf: pdftotext si existe). (2) Dashboard: localiza el dashboard en ${REPO}/src/pages/ (busca el productId) y lista TEMPLATES[].key/title, cruzados con PRODUCT_FILES['${pid}'] en ${REPO}/netlify/functions/get-download-urls.ts. (3) Landing: data file en ${REPO}/astro-site/src/data/productos/**/${pid}.ts: productName, cifras prometidas (nº plantillas/ficheros/hojas/fórmulas), nombres de entregables, bonus, FAQ. (4) Emails de verify-purchase.ts / resend-access.ts para '${pid}'. (5) Entrada de ${REPO}/src/data/productos-changelog.ts para '${pid}'. (6) Ejecuta \`python3 ${REPO}/scripts/productos-digitales/gate-flujo-postpago.py --offline --only ${pid}\` y \`python3 ${REPO}/scripts/productos-digitales/censo-entregables.py --only ${pid} --fail --quiet\` y resume ambos. ${RULES}`,
  { label: `inventario:${pid}`, phase: 'Inventario', model: 'sonnet', effort: 'low', schema: INV_SCHEMA })

phase('Ronda 1')
const COMMON = `Auditoría ADVERSARIAL de los entregables del producto digital «${pid}» de aichef.pro (familia ${familia}). Ficheros en ${DL}/. ${FASE_A} Inventario determinista previo: ${JSON.stringify(inv).slice(0, 7000)}. Referencia de calidad alcanzada en otro producto: ${REPO}/scripts/productos-digitales/kit-tareas-pasteleria-v2-SPEC.md. Tu trabajo: intentar REFUTAR que estos ficheros están listos para un cliente que pagó. ${RULES} Máximo 40 hallazgos ordenados por severidad; «alta» = reembolso, riesgo legal, cálculo erróneo o fichero inutilizable; no infles severidades; cada hallazgo con evidencia LEÍDA del fichero (valores concretos, fórmula concreta) y un fix accionable.`
const lentes = [
  { key: 'dominio', prefijo: 'DOM', prompt: `${COMMON}\n\nLENTE: ${dominio}. Abre TODOS los ficheros (openpyxl para xlsx; python-docx/pdftotext para docx/pdf) y lee el contenido como si fueras a usarlos mañana en tu negocio: ¿los ejemplos precargados son realistas (precios, mermas, rendimientos, gramajes, tiempos)? ¿faltan columnas o plantillas que cualquier profesional esperaría? ¿hay errores de concepto? Ids ${'DOM'}-NN.` },
  { key: 'excel', prefijo: 'TEC', prompt: `${COMMON}\n\nLENTE: TÉCNICA EXCEL. Con openpyxl + pycel: fórmulas (rangos completos, IFERROR, referencias entre hojas con nombres exactos, celdas que deberían ser fórmula y son valores fijos), evaluación cambiando inputs (el resultado DEBE cambiar y en la dirección correcta), validaciones y formatos condicionales (rangos, guardas de vacío), formatos numéricos y de moneda, celdas combinadas con wrap sin alto de fila, textos cortados por anchos, tildes ausentes, dobles espacios, instrucciones que describen hojas o columnas que no existen. Ids TEC-NN.` },
  { key: 'coherencia', prefijo: 'COM', prompt: `${COMMON}\n\nLENTE: COHERENCIA COMERCIAL + CLIENTE ESCÉPTICO. Cruza landing (seo, schema, hero, grid, bonus, faqs, cta), dashboard (tarjetas y claves), emails de acceso y changelog contra lo que REALMENTE contienen los ficheros: cifras, nombres, promesas de hojas o campos inexistentes, «pre-rellenado» donde está vacío, marcas reales en testimonios, reseñas sin sistema real, ancla de precio permanente, nombres de fichero/hoja que no coinciden con lo que dice la tarjeta. Ids COM-NN.` },
]
const res = await parallel(lentes.map((l) => () => agent(l.prompt, { label: `R1:${l.key}:${pid}`, phase: 'Ronda 1', model: 'opus', effort: 'high', schema: HALLAZGOS_SCHEMA })))
const [dom, tec, com] = res
const total = res.filter(Boolean).reduce((n, r) => n + r.hallazgos.length, 0)
log(`R1 ${pid}: ${total} hallazgos (dominio ${dom ? dom.hallazgos.length : '-'}, excel ${tec ? tec.hallazgos.length : '-'}, coherencia ${com ? com.hallazgos.length : '-'})`)

// Persistencia: NO con un agente (haiku truncaba el JSON). Tras el workflow:
//   python3 scripts/productos-digitales/r1-desde-journal.py <journal.jsonl> <pid> <familia>
return { productId: pid, out: OUT, total, veredictos: res.map((r) => (r ? { lente: r.lente, veredicto: r.veredicto, n: r.hallazgos.length, altas: r.hallazgos.filter((h) => h.severidad === 'alta').length } : null)) }
