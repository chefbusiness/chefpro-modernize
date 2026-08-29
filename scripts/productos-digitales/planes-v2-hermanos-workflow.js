export const meta = {
  name: 'planes-v2-hermanos-a',
  description: 'T7 de planes-v2-SPEC.md: los 4 hermanos de línea A (cafetería, tapas-bar, panadería, food-truck), EN SERIE — contenido_<pid> por sonnet verificando cada id del representante + gates (13/13, blancos contaminados 0) + refutador opus por hermano. SOLO dry-run; el APPLY lo hace el orquestador.',
  phases: [
    { title: 'Hermanos', detail: 'sonnet ×4 en serie: contenido_<pid>/a.py + dry-run 13/13', model: 'sonnet' },
    { title: 'Refutar', detail: 'opus ×4 en serie: analista de riesgos + Excel sobre cada hermano', model: 'opus' },
  ],
}
const REPO = '/Users/johnguerrero/chefpro-modernize'
const SCR = '/private/tmp/claude-501/-Users-johnguerrero-chefpro-modernize/9a6ebdb7-5d45-4ab1-9e93-10b86cb95c42/scratchpad/planes'
const SPEC = `${REPO}/scripts/productos-digitales/planes-v2-SPEC.md`
const PKG = `${REPO}/scripts/productos-digitales/planes-v2_0`
const AUD = `${REPO}/scripts/productos-digitales/auditorias`
const DLALL = `${REPO}/astro-site/public/dl`
const HERMANOS = (args && args.hermanos) || ['plan-negocio-cafeteria', 'plan-negocio-tapas-bar', 'plan-negocio-panaderia', 'plan-negocio-food-truck']
const RULES = `REGLAS DURAS: (1) PROHIBIDO modificar ${DLALL}/** (producción): todo por \`CLAUDE_SCRATCHPAD=${SCR}/h-<pid> python3 ${PKG}/main.py --producto <pid> --dry-run --json ${SCR}/h-<pid>.json\`; nunca PLANES_APPLY. (2) TÉRMICA (el Mac se apaga a 65 °C): \`istats cpu temp\` antes de cada python; ≥ 60 °C → sleep 90; UN python cada vez; sin builds/Playwright/navegador. (3) Nada de git. (4) Cita fichero!hoja!celda con valor leído; devuelve el schema completo. (5) Nada de cifras del sector inventadas: los supuestos de ejemplo de cada hermano salen de su propio docx/xlsx v1.1 (ticket, cubiertos, plantilla) recalibrados según §7-bis.17 (el caso base cumple su propio semáforo o declara pérdidas) — anota la fuente de cada cifra.`
const BUILD = { type: 'object', required: ['pid', 'ficheros_codigo', 'ids_verificados', 'ids_no_aplican', 'gates', 'caso_base', 'pendiente'], properties: { pid: { type: 'string' }, ficheros_codigo: { type: 'array', items: { type: 'string' } }, ids_verificados: { type: 'array', items: { type: 'object', required: ['id', 'estado', 'evidencia'], properties: { id: { type: 'string' }, estado: { type: 'string' }, evidencia: { type: 'string' } } } }, ids_no_aplican: { type: 'array', items: { type: 'object', required: ['id', 'motivo'], properties: { id: { type: 'string' }, motivo: { type: 'string' } } } }, gates: { type: 'object', required: ['dryrun_exit', 'idempotencia', 'censo', 'blancos_contaminados', 'gates_medibles'], properties: { dryrun_exit: { type: 'integer' }, idempotencia: { type: 'integer' }, censo: { type: 'integer' }, blancos_contaminados: { type: 'integer' }, gates_medibles: { type: 'string' } } }, caso_base: { type: 'array', items: { type: 'string' } }, pendiente: { type: 'array', items: { type: 'string' } } } }
const HALL = { type: 'object', required: ['pid', 'listo', 'hallazgos', 'motivo'], properties: { pid: { type: 'string' }, listo: { type: 'boolean' }, motivo: { type: 'string' }, hallazgos: { type: 'array', maxItems: 25, items: { type: 'object', required: ['id', 'severidad', 'celda', 'hallazgo', 'fix'], properties: { id: { type: 'string' }, severidad: { type: 'string', enum: ['alta', 'media', 'baja'] }, celda: { type: 'string' }, hallazgo: { type: 'string' }, fix: { type: 'string' } } } } } }

const out = []
for (const pid of HERMANOS) {
  phase('Hermanos')
  const mod = pid.replace(/-/g, '_')
  const h = await agent(`Hermano «${pid}» (línea A, molde A-β salvo que el censo diga otra cosa) de la familia Planes v2.0 — T7 de §9 de ${SPEC} (lee §1, §2 —incluido §2.12— y §7-bis ENTEROS). El representante plan-negocio-bar-restaurante YA está aplicado en producción; su paquete es ${PKG}/ (motor.py, main.py, grupo_a.py, contenido_plan_negocio_bar_restaurante/a.py — léelos: tu módulo sigue EXACTAMENTE ese contrato). Ficheros reales del hermano en ${DLALL}/${pid}/ (ábrelos con openpyxl y python-docx ANTES de escribir; el molde A-β no tiene input de ticket: §2.12). Escribe ${PKG}/contenido_${mod}/a.py con los supuestos, textos e importes PROPIOS de este negocio (ticket, cubiertos/día, días, mix bebida, plantilla por turnos, alquiler, inversión por partidas, checklist legal vigente) tomados de sus propios ficheros v1.1 y recalibrados según §7-bis.17; luego verifica UNO A UNO cada id del representante (los de ${AUD}/planes-v2-motor-ids.json y los RD/RT/RC resueltos de ${AUD}/planes-v2-correccion.json) contra TU hermano: resuelto (celda, valor) / no aplica (motivo). Gates exigidos en dry-run: exit 0, idempotencia 0, censo 0, blancos_contaminados 0, gates medibles 13/13, caso base que pasa sus 5 ratios (o pérdidas DECLARADAS con nota), P&L personal = hoja Personal, break-even único, tesorería 12 meses numérica, financiación usos = orígenes. Informe también en ${AUD}/planes-v2-hermano-${pid}.json. ${RULES}`,
    { label: `hermano:${pid}`, phase: 'Hermanos', model: 'sonnet', effort: 'high', schema: BUILD })
  log(`${pid}: exit ${h ? h.gates.dryrun_exit : '?'} · blancos ${h ? h.gates.blancos_contaminados : '?'} · ids ${h ? h.ids_verificados.length : '?'}`)
  phase('Refutar')
  const r = await agent(`REFUTADOR del hermano «${pid}» (Planes v2.0, línea A). Informe del constructor: ${JSON.stringify(h).slice(0, 6000)}. Tu misión es DEMOSTRAR que NO está listo: genera TU copia dry-run (scratchpad propio ${SCR}/r-${pid}) y aplícale dos lentes a la vez — ANALISTA DE RIESGOS (supuestos defendibles con fuente en el propio kit, personal = Personal, labour cost ≤ techo o pérdidas declaradas, break-even único con cuota y amortización, tesorería sin blancos, financiación cuadrada, legal vigente) y TÉCNICA EXCEL (pycel cambiando inputs, libro en blanco sin verdes ni «0,0 %», DV, protección, formatos, ortografía, idempotencia). Cruza además los ids que el constructor declara «no aplica». Máx. 25 hallazgos con celda y valor leído. Escribe ${AUD}/planes-v2-hermano-${pid}-ref.json. ${RULES}`,
    { label: `ref:${pid}`, phase: 'Refutar', model: 'opus', effort: 'high', schema: HALL })
  log(`${pid} refutado: listo=${r ? r.listo : '?'} · ${r ? r.hallazgos.length : '?'} hallazgos`)
  out.push({ pid, construccion: h, refutacion: r })
}
return out
