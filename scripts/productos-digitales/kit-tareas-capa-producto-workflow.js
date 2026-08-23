export const meta = {
  name: 'kit-tareas-capa-producto',
  description: 'Capa de producto de los 10 hermanos «▸» v2.0: landing .ts (cifras reales + updateNote + redacción del 07), entrada v2.0 en productos-changelog.ts y emailBody en resend-access.ts — sonnet por kit (2 a la vez), refutador opus al final',
  phases: [
    { title: 'Copy', detail: 'sonnet por kit: landing + changelog + email con cifras firmadas', model: 'sonnet' },
    { title: 'Refutar', detail: 'opus: cruza cifras publicadas vs firmadas en los 10 kits, tsc y coherencia', model: 'opus' },
  ],
}
const PAR = args && args.par ? args.par : 2
const REPO = '/Users/johnguerrero/chefpro-modernize'
const VER = `${REPO}/scripts/productos-digitales/auditorias/kit-tareas-hermanos`
const CIFRAS = {
  'kit-tareas-cafeteria': { tareas_total: 500, tareas_01: 130, hojas_checklist: 33, ficheros_total: 11, bonus02: '22 fechas (fila por fecha)' },
  'kit-tareas-pizzeria': { tareas_total: 373, tareas_01: 76, hojas_checklist: 31, ficheros_total: 11, bonus02: '22 fechas (fila por fecha)' },
  'kit-tareas-hamburgueseria': { tareas_total: 346, tareas_01: 72, hojas_checklist: 31, ficheros_total: 11, bonus02: '22 fechas (fila por fecha)' },
  'kit-tareas-dark-kitchen': { tareas_total: 331, tareas_01: 55, hojas_checklist: 28, ficheros_total: 11, bonus02: '22 fechas (fila por fecha)' },
  'kit-tareas-bar': { tareas_total: 342, tareas_01: 54, hojas_checklist: 28, ficheros_total: 11, bonus02: '23 fechas (fila por fecha)' },
  'kit-tareas-catering': { tareas_total: 346, tareas_01: 38, hojas_checklist: 22, ficheros_total: 11, bonus02: '22 fechas (fila por fecha)' },
  'kit-tareas-chocolateria': { tareas_total: 338, tareas_01: 41, hojas_checklist: 24, ficheros_total: 11, bonus02: 'calendario MENSUAL de 12 meses con las fechas señaladas dentro de cada mes — NO decir «12 fechas»' },
  'kit-tareas-heladeria': { tareas_total: 298, tareas_01: 43, hojas_checklist: 25, ficheros_total: 11, bonus02: 'calendario MENSUAL de 12 meses con las fechas señaladas dentro de cada mes — NO decir «12 fechas»' },
  'kit-tareas-hotel': { tareas_total: 636, tareas_01: 64, hojas_checklist: 53, ficheros_total: 19, bonus02: '24 fechas (fila por fecha)' },
  'kit-tareas-restaurante-creativo': { tareas_total: 477, tareas_01: 55, hojas_checklist: 34, ficheros_total: 13, bonus02: 'calendario MENSUAL de 12 meses — NO decir «12 fechas»' },
}
const PIDS = Object.keys(CIFRAS)
const RULES = `REGLAS: (1) Sólo tocas TRES ficheros: ${REPO}/astro-site/src/data/productos/tareas/<pid>.ts, la entrada '<pid>' de ${REPO}/src/data/productos-changelog.ts y la entrada '<pid>' de ${REPO}/netlify/functions/resend-access.ts. Nada más (ni dl/**, ni otros kits, ni types). (2) No git add/commit. (3) Nada de builds ni tsc de todo el proyecto (regla térmica): comprueba la sintaxis de tu .ts con \`node -e "require('typescript').transpileModule(require('fs').readFileSync('<fichero>','utf8'),{})"\` si typescript está en node_modules, o con una lectura cuidadosa de llaves/comas. (4) Ortografía y tildes perfectas; español de España; Title Case del proyecto (palabras significativas en mayúscula, «y/de/para» en minúscula). (5) Ninguna cifra que no venga de CIFRAS o del informe -real.json; si dudas, no la publiques. (6) Escribe pronto y ve guardando.`
const prompt = (pid) => {
  const c = CIFRAS[pid]
  return `Redactor de la capa de producto del kit «${pid}» (v2.0, ya regenerado y en producción). Modelo a imitar: el representante ${REPO}/astro-site/src/data/productos/tareas/kit-tareas.ts (léelo: líneas 30-40, 110-140, 160-175, 185-195, 250-260 y el updateNote del final) y su entrada 'kit-tareas' en ${REPO}/src/data/productos-changelog.ts (versión 2.0, fecha 2026-08-22: estilo, granularidad, «Contador honesto…», «Línea de autoría…») y 'kit-tareas' en ${REPO}/netlify/functions/resend-access.ts (emailBody con «(v2.0)»).\n\nCIFRAS FIRMADAS (únicas válidas): ${JSON.stringify(c)}. Lo que cambió DE VERDAD en este kit: ${VER}/${pid}-real.json (campo de cambios por fichero, y gates.recuento_tareas.por_fichero) + ${VER}/${pid}-ver4.json (fixes verificados) + el módulo ${REPO}/scripts/productos-digitales/kit-tareas-v2_0/contenido_${pid.replace(/-/g, '_')}.py (docstrings de cada bloque: higiene, gas, anisakis, Trimestral y Anual, calendario, vocabulario del sector…). Léelos antes de escribir.\n\nTAREA: (A) Landing ${REPO}/astro-site/src/data/productos/tareas/${pid}.ts: sustituye cada cifra de tareas/plantillas/ficheros/checklists/fechas por la firmada (busca «~», «tareas», «plantillas», «checklists», «ficheros», «fechas»); añade el total ${c.tareas_total} donde el representante lo pone (hero/seo/grid) si la landing no lo dice; el 01 tiene ${c.tareas_01} tareas; la línea «3 plantillas en blanco» pasa a la redacción del representante (kit-tareas.ts ~169: «3 plantillas maestras ya estructuradas … tú solo escribes tus tareas en las celdas verdes») adaptada a los ejes reales del kit (bar: franja horaria / zona / perfil con zona y responsable precargados; restaurante-creativo: franja horaria / partida / perfil con 3 filas de ejemplo; catering: por fase / zona / perfil sin contador); BONUS-02 según unidad (${c.bonus02}); menciona la hoja nueva «Trimestral y Anual» (mantenimiento legal: DDD, extintores, gas, legionela…) si el -real.json la confirma; updateNote → 'Producto actualizado · Versión 2.0 · agosto 2026'; en hotel corrige «46 checklists en 15 plantillas» → ${c.hojas_checklist} hojas de checklist en ${c.ficheros_total} ficheros y rehaz las comparaciones con Trail con la cifra nueva; en restaurante-creativo unifica «11 checklists/plantillas» y «9 plantillas» → ${c.ficheros_total} ficheros (11 + 2 bonus). No cambies precio, slug, stripeEnvKey, imágenes ni testimonios. (B) Changelog: añade ENCIMA de la entrada 1.1 una entrada { version: '2.0', date: '2026-08-23', title, changes[8-13] } con lo que cambió DE VERDAD en este kit (del -real.json y del módulo), con el vocabulario del sector, y sube version: '2.0', updated: '2026-08-23'. (C) Email: emailBody con el nº de ficheros real y «(v2.0)», como el representante. Devuelve JSON: cifras_publicadas (lista de «línea: texto» de la landing con cifras), cambios_changelog (nº), pendiente (lo que no pudiste confirmar). ${RULES}`
}
const OUTS = { type: 'object', properties: { pid: { type: 'string' }, ficheros: { type: 'array', items: { type: 'string' } }, cifras_publicadas: { type: 'array', items: { type: 'string' } }, cambios_changelog: { type: 'integer' }, pendiente: { type: 'array', items: { type: 'string' } } }, required: ['pid', 'ficheros', 'cifras_publicadas', 'cambios_changelog', 'pendiente'] }

phase('Copy')
const outs = []
for (let i = 0; i < PIDS.length; i += PAR) {
  const par = PIDS.slice(i, i + PAR)
  const r = await parallel(par.map((pid) => () => agent(prompt(pid), { label: `copy:${pid}`, phase: 'Copy', model: 'sonnet', effort: 'high', schema: OUTS })))
  outs.push(...r)
  log(`copy ${par.join(' + ')}: ${r.map((x) => (x ? `${x.pid} changelog ${x.cambios_changelog} pendiente ${x.pendiente.length}` : 'NULL')).join(' · ')}`)
}

phase('Refutar')
const REF = { type: 'object', properties: { ok: { type: 'array', items: { type: 'string' } }, fallos: { type: 'array', items: { type: 'object', properties: { pid: { type: 'string' }, fichero: { type: 'string' }, linea: { type: 'integer' }, problema: { type: 'string' }, corregido: { type: 'boolean' } }, required: ['pid', 'fichero', 'linea', 'problema', 'corregido'] } }, sintaxis_ok: { type: 'boolean' }, notas: { type: 'array', items: { type: 'string' } } }, required: ['ok', 'fallos', 'sintaxis_ok', 'notas'] }
const ref = await agent(`Refutador de la capa de producto de los 10 hermanos «▸». CIFRAS FIRMADAS: ${JSON.stringify(CIFRAS)}. Para cada pid: (1) lee ${REPO}/astro-site/src/data/productos/tareas/<pid>.ts ENTERO y extrae TODA cifra de tareas/plantillas/ficheros/checklists/fechas; cada una debe coincidir con la firmada o ser derivable (p.ej. 9 plantillas + 2 bonus = 11) — cita línea y corrige lo que esté mal; busca restos «~80», «Versión 1.1», «3 plantillas en blanco», «15 plantillas», «46 checklists», «12 fechas» (en chocolatería/heladería/restaurante-creativo el BONUS-02 son MESES); (2) la entrada '<pid>' en ${REPO}/src/data/productos-changelog.ts tiene version '2.0', una entrada 2.0 encima de la 1.1, sin afirmaciones que el ${VER}/<pid>-real.json no respalde (cruza 3 afirmaciones por kit contra el JSON); (3) '<pid>' en ${REPO}/netlify/functions/resend-access.ts dice el nº de ficheros real y «(v2.0)»; (4) ortografía/tildes; (5) sintaxis: carga cada .ts con \`node -e "require('typescript').transpileModule(...)"\` si hay typescript en ${REPO}/node_modules, o revisa llaves/comas con cuidado; NO lances build ni tsc global. Corrige tú lo que encuentres (corregido=true) y devuelve el schema. No git. Regla térmica: nada pesado.`,
  { label: 'refutador', phase: 'Refutar', model: 'opus', effort: 'high', schema: REF })
return { outs, ref }
