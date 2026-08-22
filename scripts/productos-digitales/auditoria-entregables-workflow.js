export const meta = {
  name: 'auditoria-entregables-producto',
  description: 'Ronda 1 adversarial de los entregables de UN producto digital (3 lentes opus: dominio, técnica Excel, coherencia) — args: {productId, familia, dominio?}',
  phases: [
    { title: 'Inventario', detail: 'sonnet: censo determinista del producto (ficheros, hojas, fórmulas, cache, casilla, bio, A4) + landing/dashboard/functions', model: 'sonnet' },
    { title: 'Ronda 1', detail: '3 lentes opus en paralelo, cada una devuelve JSON de hallazgos', model: 'opus' },
  ],
}

// Uso: Workflow({scriptPath: 'scripts/productos-digitales/auditoria-entregables-workflow.js',
//                args: {productId: 'kit-escandallos', familia: 'kit-excel'}})
// familias: 'kit-tareas' | 'guia' | 'plan' | 'kit-excel' | 'ebook'. `dominio` (opcional) afina la
// lente experta: p. ej. 'jefe de cocina de pizzería' o 'controller de costes de restaurante'.
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
  'kit-excel': 'EXPERTO/A TÉCNICO del tema del kit (escandallos → controller de costes; APPCC → consultor de seguridad alimentaria (RD 3484/2000, Reg. 852/2004, 1169/2011); inventario → jefe de compras; RRHH → asesor laboral; plan financiero → director financiero): ¿las plantillas resuelven el problema real? ¿fórmulas correctas? ¿normativa bien citada? ¿qué le faltaría a un profesional exigente?',
  'ebook': 'FORMADOR/A de cocina con IA: ¿los prompts funcionan tal cual copiados? ¿hay caracteres raros, fechas caducas, promesas vacías?',
}
const dominio = (args && args.dominio) ? args.dominio : DOMINIO[familia]

const RULES = 'No edites nada. Cita fichero:hoja:celda o fichero:línea. REGLA TÉRMICA: python EN SERIE y ligero, `istats cpu temp` antes de cada barrido; nada de builds ni Playwright. Devuelve SOLO JSON.'

phase('Inventario')
const inv = await agent(`Repo ${REPO}. Producto digital «${pid}» (familia ${familia}). Haz un INVENTARIO determinista y devuélvelo como JSON: (1) ficheros de ${DL}/ (nombre, tamaño, tipo); para cada xlsx con openpyxl: hojas, nº fórmulas, nº sin cache (data_only None, separando las que devuelven cadena vacía por diseño), ☐ en columna A, bio caduca («29 años»/«15 años»/«29 anos»), paperSize≠9 en hojas de trabajo, creator, caracteres no latinos, celdas numéricas guardadas como datetime. Para docx: python-docx si está instalado (párrafos, «29 años», tildes ausentes evidentes); para pdf: pdftotext si existe. (2) Claves del dashboard: localiza el dashboard en ${REPO}/src/pages/ (busca el productId o su nombre) y lista TEMPLATES[].key/title; cruza con PRODUCT_FILES['${pid}'] en ${REPO}/netlify/functions/get-download-urls.ts. (3) Landing: data file en ${REPO}/astro-site/src/data/productos/**/ con slug '${pid}' (o la página .astro del eBook): cifras prometidas (nº plantillas/ficheros/hojas), nombres de entregables, bio, FAQ. (4) Emails en verify-purchase.ts / resend-access.ts para '${pid}'. (5) Ejecuta python3 ${REPO}/scripts/productos-digitales/gate-flujo-postpago.py --offline --only ${pid}. ${RULES} Formato: {"productId":"${pid}","ficheros":[...],"dashboard":[...],"landing":{...},"emails":{...},"gate":"..."}`,
  { label: `inventario:${pid}`, phase: 'Inventario', model: 'sonnet', effort: 'low' })

phase('Ronda 1')
const COMMON = `Auditoría ADVERSARIAL de los entregables del producto digital «${pid}» de aichef.pro (familia ${familia}). Ficheros en ${DL}/. Inventario determinista previo: ${JSON.stringify(inv).slice(0, 6000)}. Referencia de calidad alcanzada en otro producto: ${REPO}/scripts/productos-digitales/kit-tareas-pasteleria-v2-SPEC.md (§1.1 y §1.4: metadata, impresión, cache, casilla unificada, autorreferencias, RGPD, alérgenos como borrador). Tu trabajo: intentar REFUTAR que estos ficheros están listos para un cliente que pagó. ${RULES} JSON: {"lente":"…","hallazgos":[{"id":"<PREFIJO>-NN","severidad":"alta|media|baja","fichero":"…","ubicacion":"…","hallazgo":"…","evidencia":"…","fix":"…"}],"veredicto":"listo|no listo","motivo":"…"}. Máximo 40 hallazgos ordenados por severidad; «alta» = reembolso, riesgo legal o fichero roto; no infles severidades; cada hallazgo con evidencia LEÍDA del fichero.`
const lentes = [
  { key: 'dominio', prefijo: 'DOM', prompt: `${COMMON}\n\nLENTE: ${dominio}. Abre TODOS los ficheros (openpyxl para xlsx; python-docx/pdftotext para docx/pdf) y lee el texto como si fueras a usarlos mañana en tu negocio.` },
  { key: 'excel', prefijo: 'TEC', prompt: `${COMMON}\n\nLENTE: TÉCNICA EXCEL. Con openpyxl + pycel: fórmulas (rangos completos, IFERROR, referencias entre hojas con nombres exactos), cache (data_only), evaluación cambiando inputs (el resultado DEBE cambiar), validaciones y formatos condicionales (rangos, guardas de vacío), formatos numéricos y fechas, celdas combinadas con wrap sin alto de fila, freeze panes, page setup, metadata, tildes ausentes, dobles espacios, caracteres no latinos, XML válido.` },
  { key: 'coherencia', prefijo: 'COM', prompt: `${COMMON}\n\nLENTE: COHERENCIA COMERCIAL + CLIENTE ESCÉPTICO. Cruza landing (seo, schema, hero, grid, bonus, faqs, cta), dashboard (tarjetas y claves), emails de acceso y changelog (${REPO}/src/data/productos-changelog.ts, si existe entrada) contra lo que REALMENTE contienen los ficheros: cifras, nombres, promesas de hojas o campos inexistentes, «pre-rellenado» donde está vacío, marcas reales en testimonios, bio caduca, reseñas sin sistema real, ancla de precio permanente.` },
]
const res = await Promise.all(lentes.map((l) => agent(l.prompt, { label: `R1:${l.key}:${pid}`, phase: 'Ronda 1', model: 'opus', effort: 'high' })))

// Persistir en el repo (sobrevive al reinicio; el scratchpad no)
await agent(`Escribe el fichero ${OUT} (crea la carpeta si no existe) con este JSON exacto, formateado con indent=1 y ensure_ascii=False, sin modificar su contenido: ${JSON.stringify({ productId: pid, familia, inventario: inv, rondas: { R1: { dominio: res[0], excel: res[1], coherencia: res[2] } } })}. No hagas commit. Devuelve SOLO {"ok":true,"path":"${OUT}"}.`,
  { label: `persistir:${pid}`, phase: 'Ronda 1', model: 'haiku', effort: 'low' })
return { productId: pid, out: OUT, veredictos: res.map((r) => (typeof r === 'string' ? r.slice(0, 300) : r)) }
