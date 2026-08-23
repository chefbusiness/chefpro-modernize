export const meta = {
  name: 'kit-gestion-personal-v2',
  description: 'Construcción del Kit de Gestión de Personal v2.0 según kit-gestion-personal-v2-SPEC.md: motor + grupos A/B/C (dry-run) → integración → 3 refutadores → corrección → ronda 2 → crítico. SOLO dry-run: la ejecución real la hace el orquestador.',
  phases: [
    { title: 'Motor', detail: 'opus: motor.py + main.py (§1: taxonomía, verdes, IVA, CF, protección, bio, versión, metadata, gates)', model: 'opus' },
    { title: 'Grupos', detail: 'opus ×3 (2 a la vez): grupo_a (01, 02, B-08) · grupo_b (03, 04, 05) · grupo_c (06, 07, B-09)', model: 'opus' },
    { title: 'Integración', detail: 'sonnet: landing, dashboard, changelog, emails (§5)', model: 'sonnet' },
    { title: 'Refutar', detail: 'opus ×3: dominio, técnica pycel, coherencia — contra la copia dry-run', model: 'opus' },
    { title: 'Corregir', detail: 'opus: aplica los hallazgos de los refutadores', model: 'opus' },
    { title: 'Ronda 2', detail: 'sonnet: re-verifica CADA hallazgo por id + gates completos', model: 'sonnet' },
    { title: 'Crítico', detail: 'opus: listo / no listo', model: 'opus' },
  ],
}
const PAR = args && args.par ? args.par : 2
const REPO = '/Users/johnguerrero/chefpro-modernize'
const SCR = '/private/tmp/claude-501/-Users-johnguerrero-chefpro-modernize/7340312f-b4fe-4aa1-b254-4b0c17c8375f/scratchpad'
const SPEC = `${REPO}/scripts/productos-digitales/kit-gestion-personal-v2-SPEC.md`
const R1 = `${REPO}/scripts/productos-digitales/auditorias/kit-gestion-personal-R1.json`
const PKG = `${REPO}/scripts/productos-digitales/kit-gestion-personal-v2_0`
const DL = `${REPO}/astro-site/public/dl/kit-gestion-personal`
const AUD = `${REPO}/scripts/productos-digitales/auditorias`
const OUT = `${SCR}/kit-gp-v2`
const MODELO = `${REPO}/scripts/productos-digitales/kit-escandallos-v2_0`
const RULES = `REGLAS DURAS: (1) PROHIBIDO modificar ${DL}/** — todo por \`CLAUDE_SCRATCHPAD=${SCR}/propio-<rol> python3 ${PKG}/main.py --dry-run [--solo ...] --json ${OUT}/<rol>.json\` (nunca KIT_GESTION_PERSONAL_APPLY). (2) REGLA TÉRMICA (el Mac se apaga a 65 °C): \`istats cpu temp\` antes de cada python; ≥ 60 °C → \`sleep 90\`; un python a la vez; sin builds/Playwright. (3) No git add/commit/stash/clean. (4) Cita fichero:hoja:celda. (5) Escribe tu código/JSON PRONTO en el repo y ve actualizándolo (el Mac se ha apagado de madrugada dos veces: lo no commiteado se pierde, y el orquestador commitea entre fases). (6) python3 3.7 / openpyxl 3.1.3: sin f-strings con '=' ni walrus; pycel NO implementa COUNTA ni MODE (la SPEC da los sustitutos). (7) Convenciones de familia: verdes E8F5E9 desbloqueados, IFERROR en toda división, parámetros en celda, inject_cache.py al final de main.py, idempotencia (2.ª pasada 0 diferencias), protección de hoja sin contraseña. (8) Modelo de paquete: ${MODELO}/ (motor.py, grupo_a/b/c.py, main.py con --dry-run/--solo/APPLY/respaldo): imita su estructura y sus gates.`

const BUILD = { type: 'object', properties: { rol: { type: 'string' }, ficheros_codigo: { type: 'array', items: { type: 'string' } }, secciones_spec_cubiertas: { type: 'array', items: { type: 'string' } }, pruebas: { type: 'array', items: { type: 'string' } }, dudas: { type: 'array', items: { type: 'string' } }, pendiente: { type: 'array', items: { type: 'string' } } }, required: ['rol', 'ficheros_codigo', 'secciones_spec_cubiertas', 'pruebas', 'dudas', 'pendiente'] }

phase('Motor')
const m = await agent(`Constructor del MOTOR del Kit de Gestión de Personal v2.0. SPEC: ${SPEC} (§1 entero + convenciones de cabecera + §7-bis). R1 de referencia: ${R1}. Ficheros reales: ${DL}/ (9 xlsx — léelos con openpyxl antes de escribir una línea). Escribe ${PKG}/motor.py (utilidades transversales de §1: taxonomía canónica de 10 categorías como constante, estilos y verde de edición, DV de categorías/unidades, IVA por categoría, formato condicional, protección sin contraseña con verdes desbloqueados, bio anclada — OJO: es INSERCIÓN, las Instrucciones actuales no llevan bio —, línea «Versión 2.0 · agosto 2026 · aichef.pro/kit-inventario · info@aichef.pro», metadata title/subject/keywords, contador/gates auxiliares) y ${PKG}/main.py (orquesta: copia a scratchpad en --dry-run, aplica motor + grupo_a/b/c si existen, idempotencia sobre clon, inject_cache al final — reusa ${REPO}/scripts/productos-digitales/inject_cache.py —, verificación data_only, casos de demostración con pycel según la SPEC, censo ${REPO}/scripts/productos-digitales/censo-entregables.py --only kit-gestion-personal --fail, --json). Aborta sin KIT_GESTION_PERSONAL_APPLY=1 si no hay --dry-run. Los módulos de grupo aún no existen: main.py debe funcionar con los que encuentre (--solo motor). Prueba: dry-run --solo motor exit 0, idempotencia 0. Informe también en ${AUD}/kit-gestion-personal-v2-motor.json. ${RULES}`,
  { label: 'motor', phase: 'Motor', model: 'opus', effort: 'high', schema: BUILD })
log(`Motor: ${m ? `dudas ${m.dudas.length} pendiente ${m.pendiente.length}` : 'NULL'}`)

phase('Grupos')
const GRUPOS = [
  { rol: 'grupo_a', que: '§2 — 01-cuadrante-turnos-semanal (las 4 alertas legales por fórmula con su bloque auxiliar, cita legal correcta 12 h art. 34.3 ET), 02-control-horas-extras (horas con cruce de medianoche y ROUND, recargo del convenio en celda de parámetros con nota legal correcta, guarda de H. Contratadas vacía, contador 80 h/año con CF), BONUS-01-briefing-cambio-turno' },
  { rol: 'grupo_b', que: '§3 — 03-coste-laboral-mensual (cotización empresarial en celda 33 %, pagas extra prorrateadas, Previsión por Servicio corregida a cubiertos/SERVICIO coherente con BONUS-02), 04-onboarding-nuevo-empleado (contador sin cabeceras, 0 % recién descargado, 50 tareas §7-bis.3), 05-planificacion-vacaciones (calendario con la geometría nueva de la SPEC, Días Usados cuenta DÍAS, derecho 30 días en celda)' },
  { rol: 'grupo_c', que: '§4 — 06-evaluacion-desempeno (guardas IFERROR/COUNT en media y nivel, ficha en blanco + hoja de ejemplo §7-bis.5), 07-directorio-plantilla (SIN alérgenos del empleado — art. 9 RGPD, sección de protección de datos reescrita, Vencimientos lee 30 empleados, dos páginas A4 §7-bis.6), BONUS-02-calculadora-plantilla-optima (salario 1.500 €/14 pagas, resultados por defecto creíbles y coherentes con 03)' },
]
const conts = []
for (let i = 0; i < GRUPOS.length; i += PAR) {
  const par = GRUPOS.slice(i, i + PAR)
  const r = await parallel(par.map((g) => () => agent(`Constructor del ${g.rol} del Kit de Gestión de Personal v2.0. SPEC: ${SPEC} (lee ENTERA; tu parte: ${g.que}; respeta §6 descartes y §7-bis). R1: ${R1} (tus ids). Motor ya escrito: ${PKG}/motor.py y ${PKG}/main.py (léelos y usa sus utilidades; no dupliques). Ficheros reales en ${DL}/ — ábrelos ANTES de escribir. Escribe ${PKG}/${g.rol}.py exponiendo lo que main.py espere (compruébalo en main.py). Los datos precargados que la SPEC pida deben ser REALES del oficio (categorías/unidades/precios coherentes producto a producto: nada de rotaciones cíclicas). Prueba: \`CLAUDE_SCRATCHPAD=${SCR}/propio-${g.rol} python3 ${PKG}/main.py --dry-run --solo motor,${g.rol} --json ${OUT}/${g.rol}.json\` → exit 0, idempotencia 0; demuestra con pycel los cálculos nuevos de tus ficheros (cambia inputs y comprueba la dirección del resultado); cita cada celda. Informe también en ${AUD}/kit-gestion-personal-v2-${g.rol}.json. ${RULES}`,
    { label: g.rol, phase: 'Grupos', model: 'opus', effort: 'high', schema: BUILD })))
  conts.push(...r)
  log(`grupos ${par.map((g) => g.rol).join(' + ')}: ${r.map((x) => (x ? `${x.rol} dudas ${x.dudas.length} pendiente ${x.pendiente.length}` : 'NULL')).join(' · ')}`)
}

phase('Integración')
const integ = await agent(`Integrador del Kit de Gestión de Personal v2.0 (§5 de ${SPEC}, con §7-bis.3/5/6). Con la copia dry-run completa (genera una: \`CLAUDE_SCRATCHPAD=${SCR}/propio-integ python3 ${PKG}/main.py --dry-run --json ${OUT}/integ.json\`): actualiza ${REPO}/astro-site/src/data/productos/kits/kit-gestion-personal.ts (líneas que la SPEC cita: interconexión→coherencia, APPCC matizado, 10 categorías, cifras reales medidas en la copia, «50-100 €/mes», badge §7-bis.6, FAQ licencia §7-bis.5, updateNote 2.0 — NO tocar aggregateRating/reviews/testimonios/precios), ${REPO}/src/pages/KitGestionPersonalDashboard.tsx (tarjetas coherentes con lo que hay), entrada 'kit-gestion-personal' de ${REPO}/src/data/productos-changelog.ts (version 2.0, updated 2026-08-23, entrada encima de la 1.1 con 10-13 cambios REALES en lenguaje de cliente) y ${REPO}/netlify/functions/resend-access.ts si cita cifras. Sintaxis con typescript.transpileModule (node_modules tiene typescript); nada de builds. Devuelve el schema (en pruebas: cada cifra publicada con su medida). ${RULES}`,
  { label: 'integracion', phase: 'Integración', model: 'sonnet', effort: 'high', schema: BUILD })
log(`Integración: ${integ ? `pendiente ${integ.pendiente.length}` : 'NULL'}`)

phase('Refutar')
const HALL = { type: 'object', properties: { lente: { type: 'string' }, hallazgos: { type: 'array', maxItems: 30, items: { type: 'object', properties: { id: { type: 'string' }, severidad: { type: 'string', enum: ['alta', 'media', 'baja'] }, fichero: { type: 'string' }, ubicacion: { type: 'string' }, hallazgo: { type: 'string' }, evidencia: { type: 'string' }, fix: { type: 'string' } }, required: ['id', 'severidad', 'fichero', 'ubicacion', 'hallazgo', 'evidencia'] } }, veredicto: { type: 'string', enum: ['listo', 'no listo'] }, motivo: { type: 'string' } }, required: ['lente', 'hallazgos', 'veredicto', 'motivo'] }
const LENTES = [
  { key: 'dominio', pref: 'RD', lente: 'JEFE/A DE COMPRAS Y ALMACÉN de restaurante con 15 años: ¿usaría esto un lunes? Datos precargados realistas producto a producto, temperaturas legales, FIFO seguro, EOQ sensata, unidades correctas.' },
  { key: 'excel', pref: 'RT', lente: 'TÉCNICA EXCEL con openpyxl + pycel: evalúa TODAS las fórmulas nuevas cambiando inputs; rangos completos; IFERROR; DV; CF; protección; formatos; idempotencia; cache.' },
  { key: 'coherencia', pref: 'RC', lente: 'COHERENCIA COMERCIAL: cruza la landing/dashboard/changelog EDITADOS contra la copia dry-run: cada cifra y cada promesa debe ser verificable en una celda; busca promesas retiradas a medias y restos de la v1.1; ortografía.' },
]
const refs = []
for (let i = 0; i < LENTES.length; i += PAR) {
  const par = LENTES.slice(i, i + PAR)
  const r = await parallel(par.map((l) => () => agent(`REFUTADOR (${l.key}) del Kit de Gestión de Personal v2.0. Tu misión es DEMOSTRAR QUE NO ESTÁ LISTO. SPEC: ${SPEC}. R1 original: ${R1} (comprueba que cada id marcado «resuelto en §N» de la tabla final está de verdad resuelto en la copia; los §6/§7-bis no). Genera TU copia (\`CLAUDE_SCRATCHPAD=${SCR}/propio-ref-${l.key} python3 ${PKG}/main.py --dry-run --json ${OUT}/ref-${l.key}.json\`) y aplícale la lente: ${l.lente} Ids ${l.pref}-NN. Máx. 30 hallazgos, cada uno con evidencia (celda o línea REAL). ESCRIBE el JSON completo en ${AUD}/kit-gestion-personal-v2-ref-${l.key}.json y devuelve el schema. ${RULES}`,
    { label: `ref:${l.key}`, phase: 'Refutar', model: 'opus', effort: 'high', schema: HALL })))
  refs.push(...r)
  log(`refutar ${par.map((l) => l.key).join(' + ')}: ${r.map((x) => (x ? `${x.lente.slice(0, 12)}… ${x.hallazgos.length} (${x.hallazgos.filter((h) => h.severidad === 'alta').length} altas) ${x.veredicto}` : 'NULL')).join(' · ')}`)
}
const totalRef = refs.filter(Boolean).reduce((n, r) => n + r.hallazgos.length, 0)

phase('Corregir')
const CORR = { type: 'object', properties: { resueltos: { type: 'array', items: { type: 'string' } }, no_aplicados: { type: 'array', items: { type: 'object', properties: { id: { type: 'string' }, motivo: { type: 'string' } }, required: ['id', 'motivo'] } }, ficheros_codigo: { type: 'array', items: { type: 'string' } }, pruebas: { type: 'array', items: { type: 'string' } } }, required: ['resueltos', 'no_aplicados', 'ficheros_codigo', 'pruebas'] }
const corr = await agent(`Corrector del Kit de Gestión de Personal v2.0. Lee ENTEROS los 3 ficheros ${AUD}/kit-gestion-personal-v2-ref-{dominio,excel,coherencia}.json (${totalRef} hallazgos en total: NO trabajes de memoria ni de un resumen). Para CADA id: o lo resuelves en ${PKG}/*.py / los .ts de integración (con celda/línea de prueba), o lo llevas a no_aplicados con motivo defendible (falso positivo con evidencia, o descartado por §6/§7-bis de la SPEC). Cruza al final: nº de ids de entrada = resueltos + no_aplicados (ninguno perdido). Dry-run completo tras corregir: exit 0, idempotencia 0. Informe también en ${AUD}/kit-gestion-personal-v2-correccion.json. ${RULES}`,
  { label: 'correccion', phase: 'Corregir', model: 'opus', effort: 'high', schema: CORR })
log(`Corrección: ${corr ? `resueltos ${corr.resueltos.length} no_aplicados ${corr.no_aplicados.length}` : 'NULL'}`)

phase('Ronda 2')
const R2S = { type: 'object', properties: { ids_entrada: { type: 'integer' }, verificados_ok: { type: 'integer' }, mal_resueltos: { type: 'array', items: { type: 'object', properties: { id: { type: 'string' }, evidencia: { type: 'string' } }, required: ['id', 'evidencia'] } }, no_aplicados_injustificados: { type: 'array', items: { type: 'string' } }, gates: { type: 'object', properties: { dryrun_exit: { type: 'integer' }, idempotencia: { type: 'integer' }, censo_exit: { type: 'integer' }, cache_fallos: { type: 'integer' }, ts_diagnosticos: { type: 'integer' } }, required: ['dryrun_exit', 'idempotencia', 'censo_exit', 'cache_fallos', 'ts_diagnosticos'] }, hallazgos_nuevos: { type: 'array', items: { type: 'object', properties: { severidad: { type: 'string', enum: ['alta', 'media', 'baja'] }, donde: { type: 'string' }, hallazgo: { type: 'string' } }, required: ['severidad', 'donde', 'hallazgo'] } }, listo: { type: 'boolean' }, fichero_json: { type: 'string' } }, required: ['ids_entrada', 'verificados_ok', 'mal_resueltos', 'no_aplicados_injustificados', 'gates', 'hallazgos_nuevos', 'listo', 'fichero_json'] }
const r2 = await agent(`Verificador de RONDA 2 del Kit de Gestión de Personal v2.0. Lee los 3 ref-*.json y ${AUD}/kit-gestion-personal-v2-correccion.json. Regenera TU copia (dry-run completo) y comprueba UNO A UNO cada id de los refutadores: resuelto de verdad (celda) / mal resuelto (evidencia) / no_aplicado con motivo que se sostiene o no. Gates: exit, idempotencia, censo --fail, data_only sin fallos, transpileModule de los .ts editados. Además abre el kit como cliente recién pagado: 5 minutos por fichero, hallazgos nuevos máx. 8. listo=true SOLO si 0 mal_resueltos, 0 injustificados, gates limpios y 0 hallazgos nuevos altos. ESCRIBE ${AUD}/kit-gestion-personal-v2-ronda2.json y devuelve el schema. ${RULES}`,
  { label: 'ronda2', phase: 'Ronda 2', model: 'sonnet', effort: 'high', schema: R2S })
log(`Ronda 2: ${r2 ? `${r2.verificados_ok}/${r2.ids_entrada} ok · mal ${r2.mal_resueltos.length} · nuevos ${r2.hallazgos_nuevos.length} · listo=${r2.listo}` : 'NULL'}`)

phase('Crítico')
const CRIT = { type: 'object', properties: { listo_para_real: { type: 'boolean' }, bloqueos: { type: 'array', items: { type: 'string' } }, cifras_capa_producto: { type: 'array', items: { type: 'string' } }, orden_ejecucion_real: { type: 'array', items: { type: 'string' } }, recomendacion: { type: 'string' } }, required: ['listo_para_real', 'bloqueos', 'cifras_capa_producto', 'orden_ejecucion_real', 'recomendacion'] }
const crit = await agent(`Crítico de completitud del Kit de Gestión de Personal v2.0. Lee ${AUD}/kit-gestion-personal-v2-ronda2.json, la corrección, los 3 ref-*.json, ${AUD}/kit-gestion-personal-v2-motor.json y los de grupos, y la tabla id→sección de ${SPEC} cruzada contra la corrección (¿algún id del R1 se perdió por el camino?). Verifica en SOLO LECTURA 5 celdas clave de la última copia dry-run. listo_para_real, bloqueos con celda, cifras para la capa de producto (las que publicará la landing, medidas), orden_ejecucion_real (comandos exactos para el orquestador: apply, censo, gate offline, commit, LIVE). Escribe ${AUD}/kit-gestion-personal-v2-critico.json. ${RULES}`,
  { label: 'critico', phase: 'Crítico', model: 'opus', effort: 'high', schema: CRIT })
return { m, conts, integ, refs: refs.filter(Boolean).map((r) => ({ lente: r.lente.slice(0, 30), n: r.hallazgos.length, veredicto: r.veredicto })), corr, r2, crit }
