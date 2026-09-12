export const meta = {
  name: 'completar-spec-guia-chocolateria',
  description: 'Reanudar la Fase A2 de «Cómo Montar una Chocolatería» tras el corte por límite de cuota: completar la SPEC v1.0 (§2-§10 + cierre) sobre el §0-§1 ya escrito, y someterla a refutación adversarial con corrección hasta LISTO (máx. 3 rondas)',
  phases: [
    { title: 'SPEC', detail: 'un redactor opus anexa §2-§10 por secciones sin tocar §0-§1' },
    { title: 'Refutar SPEC', detail: 'refutador (opus) → fixer (opus) → re-verificación, en serie' },
  ],
}

const FECHA = args.fecha
const SP = args.scratchpad
const A = 'scripts/productos-digitales/auditorias'
const PD = 'scripts/productos-digitales'
const SPEC = `${PD}/guia-chocolateria-SPEC.md`
const LEGAL_JSON = `${A}/guia-chocolateria-verificacion-legal-${FECHA}.json`
const LEGAL_MD = `${A}/guia-chocolateria-verificacion-legal-${FECHA}.md`
const RESULTADOS = `${SP}/resultados-wf_7fcee771.json`

const CONTEXTO = `
## CONTEXTO (léelo entero)
Producto NUEVO nº 5 de AI Chef Pro (aichef.pro): «Cómo Montar una Chocolatería», 65 €, slug \`guia-chocolateria-obrador\`, hermana directa
de la Guía «Cómo Montar una Pastelería» (LIVE v1.0.1 desde el 12-sep) y construida con su MISMO pipeline. Fecha de hoy: ${FECHA}.
**Qué pasó antes:** el agente que escribía la SPEC fue CORTADO a las 15:08 por el límite de cuota tras escribir §0 y §1 (§1.A D1-D18,
§1.B reconciliación con el kit, §1.C D19-D46); el fichero \`${SPEC}\` tiene hoy 213 líneas y termina en la fila D46. **§2-§10 y el cierre
NO existen todavía.** Después se saneó el censo CHS (26 fiabilidades «media-alta/media-baja» colapsadas a «media» con el nivel L4 en la nota;
7 agregados sin fuente única —CHS-02, CHS-11, CHS-25d, CHS-39, CHS-41, CHS-47a, CHS-47b— marcados «baja» con sus componentes declarados) y
se ejecutó la fusión: \`${A}/guias-v2-research-sector.json\` tiene ahora **635** entradas (411 + 109 CHN + 115 CHS), gate verde.
**Research cerrado:** síntesis \`${A}/guia-chocolateria-RESEARCH-${FECHA}.md\` (1.137 líneas) y refutación
\`${A}/guia-chocolateria-research-REFUTACION-${FECHA}.md\` («CORREGIR ANTES»: A1-A12, B1-B5, C1-C11 = 28 hallazgos). Lentes L1-L6 en \`${A}/\`.
**Decisiones FIRMADAS (John delegó):** \`${PD}/guia-chocolateria-DECISIONES-${FECHA}.md\` (D1-D18, precio 65 €). Firmes: no se reabren.
**Verificación legal (manda sobre L3 y sobre la síntesis):** \`${LEGAL_MD}\` + \`${LEGAL_JSON}\` (109 fichas CHN-*, gate de literalidad
81/81) + \`-EXCLUIDOS.json\` (10). Su resultado estructurado (correcciones_clave, prohibiciones, avisos con dos «PENDIENTE PARA LA SPEC») y los
de los agentes de ids y fusión están en \`${RESULTADOS}\` — léelo.
**Moldes de Pastelería (se calcan):** SPEC \`${PD}/guia-pasteleria-SPEC.md\` (11 secciones §0-§10) · juego de datos
\`${PD}/guia-pasteleria/datos_ejemplo.py\` · generadores \`${PD}/guia-pasteleria/gen_*.py\` · guion
\`${PD}/guias-v2_0/guion_guia_pasteleria_obrador.py\` · motor \`${PD}/guias-v2_0/documentos.py\` (\`puntos_por_epigrafe\` en la línea ~1096).
**Kit ya publicado con el que la guía NO puede contradecirse:** \`astro-site/public/dl/kit-tareas-chocolateria/\` (11 xlsx; vidas útiles en
\`02-partidas-produccion.xlsx!Moldeado\`, temperaturas, campañas en \`06-eventos-temporada.xlsx\` y \`BONUS-02-calendario-anual-tareas.xlsx\`) y
\`${PD}/kit-tareas-v2_0/contenido_kit_tareas_chocolateria.py\`. La guía cita el kit; no rehace sus tablas.
**Reglas de la casa:** cada cifra con id CHN-*/CHS-* del JSON común o «supuesto declarado»; **los ids se citan SIEMPRE con su sufijo cuando
sólo existen con sufijo** (D44: CHS-24, CHS-37, CHS-38, CHS-47, CHS-69, CHS-25, CHS-27, CHS-28, CHS-42, CHS-45 y CHS-46 NO existen «bare»);
marco normativo ESPAÑOL con compradores de toda la hispanofonía; en los xlsx prohibido INDIRECT, COUNTA, PMT, OFFSET, XLOOKUP, LET, LAMBDA,
RANK, NETWORKDAYS, IRR y referencias entre libros; cero constantes en fórmulas; parámetros en celda verde; ninguna celda verde vacía; un
concepto = una fuente. Este repo es PÚBLICO. No escribas contenido de producto (ni capítulos ni prosa vendible): esto es especificación.
**Térmica (Mac de John, hoy ya ha hecho kernel panic una vez):** \`istats cpu temp\` antes de cada tanda de python/openpyxl; UN fichero cada vez;
si marca ≥ 63 °C espera 60 s; nada de builds ni navegador; usa \`/usr/local/bin/python3\` (tiene openpyxl).`

phase('SPEC')
const SPEC_SCHEMA = {
  type: 'object',
  properties: {
    fichero: { type: 'string' }, lineas: { type: 'integer' }, secciones_h2: { type: 'integer' }, decisiones: { type: 'integer' }, hallazgos_resueltos: { type: 'integer' },
    libros: { type: 'array', items: { type: 'string' } }, constructores: { type: 'array', items: { type: 'string' } },
    reconciliacion_kit: { type: 'array', items: { type: 'string' } },
    presupuesto: { type: 'string' }, pendientes_john: { type: 'array', items: { type: 'string' } },
    avisos: { type: 'array', items: { type: 'string' } },
  },
  required: ['fichero', 'lineas', 'secciones_h2', 'decisiones', 'hallazgos_resueltos', 'libros', 'constructores', 'reconciliacion_kit', 'presupuesto', 'pendientes_john', 'avisos'],
}
const spec = await agent(`# COMPLETAR LA SPEC v1.0 — «Cómo Montar una Chocolatería» (§2-§10 + cierre)
${CONTEXTO}
## ENCARGO
1. Lee ENTERA la SPEC existente \`${SPEC}\` (213 líneas: §0, §1.A, §1.B, §1.C con D19-D46) — es lo que ya está decidido y **NO se reescribe**.
   Lee ENTERA \`${PD}/guia-pasteleria-SPEC.md\` (el molde: §2-§10 son exactamente las secciones que faltan) y \`${RESULTADOS}\`.
2. Escribe las secciones que faltan **ANEXANDO al final del fichero con \`cat >> ${SPEC} <<'MDEOF'\`, UNA SECCIÓN POR APPEND** (así un corte
   deja siempre una frontera limpia), en este orden y con estos títulos exactos de nivel 2:
   - \`## 2. Entregables (ruta \\\`astro-site/public/dl/guia-chocolateria-obrador/\\\`)\`: los 9 libros (D7) con nombre de fichero, hojas,
     entradas verdes, salidas por fórmula, la decisión que resuelve y la frontera con el kit y con Pastelería; convenciones y prohibiciones
     (C3 resuelto como celda verde «cópialo del libro N» + fila de cuadre); molde de cada libro (qué \`gen_*.py\` de Pastelería se calca y
     qué es nuevo); **reparto en 5 constructores**: [1 clima+capacidad, 2 CAPEX] · [3 sensibilidad al cacao, 5 vida útil y rotación] ·
     [4 carta y escandallo, 6 campañas y valle] · [7 plan financiero, molde planes-v2_0 motor 2.2] · [8 checklist legal, 9 equipamiento y
     proveedores]. Recoge OBLIGATORIAMENTE los dos «PENDIENTE PARA LA SPEC» de la verificación legal: (a) el libro 5 distingue bombón
     etiquetado (art. 4.2 RD 1021/2022, temperatura de la etiqueta) de bombón a granel (sistema de autocontrol); (b) el libro 9 lleva una
     SEGUNDA tabla de clientes B2B/corporativo a los que se suministra (art. 5.3.b EUDR, CHN-24) y la hoja de proveedores es un ÁRBOL
     ¿operador o comerciante?, no una columna con semáforo. Y lo que §1.C ya fijó para cada libro (D19-D46): no lo contradigas, cítalo.
   - \`## 3. Juego de datos único: la bombonería «La Almendra»\`: todo lo que \`datos_ejemplo.py\` contendrá, con procedencia (id CHN/CHS con
     sufijo, o «supuesto declarado»): nombre, ciudad, m² por zona, plantilla con los perfiles LITERALES del kit, convenio según D9/D43, carta
     de 25-30 referencias por familia con denominación legal del RD 1055/2003 y familia de alérgenos (OCHO, CHN-34b), dotación con precios
     verificados y base con/sin IVA declarada (A8), CAPEX por bloque, columna de franquicias (D11), campañas con comuniones (C6) y el valle
     de agosto (C7/D36), canales incluidos talleres y corporativo, financiación, proveedores verificados, checklist legal y Gantt.
     UN concepto = UNA fuente. Antes de fijar un dato del kit, ábrelo (openpyxl read_only, un libro cada vez) o cita lo que §1.B ya dejó leído.
   - \`## 4. Índice: 20 capítulos + anexo, y los dos bonus\`: presupuesto de palabras calibrado (≈545 pal/pág cuerpo, 410 bonus), qué capítulo
     hereda estructura de Pastelería y cuál es nuevo; taza y churros como epígrafe del cap. 01 (D1); bean-to-bar en el cap. 11 (D2); el
     capítulo de normativa con el EUDR según la verificación legal (D5: fecha de revisión explícita); los dos bonus (business plan «La
     Almendra» ≥3.500 palabras y ≥9 tablas, con resumen ejecutivo que da resultado neto, margen y equilibrio; 12 decisiones de apertura).
     Cada decisión legal que un xlsx aplica tiene su capítulo ANTES.
   - \`## 5. Lista negra (va íntegra al \\\`NO_COMUN\\\` del guion como \\\`cifras_ignorar\\\` + \\\`prohibido\\\`)\`: las ~30 prohibiciones de la
     verificación legal (literal, con su id), cifras sin fuente, «carnet de manipulador», «fino/superior/extra», el 644.5 sin su límite, el
     aplazamiento del EUDR mal atribuido, «Junio 2026», «plan gratuito» del SaaS, etc.
   - \`## 6. Vocabulario ES / LATAM (equivalencia en la PRIMERA mención; luego, el término de España)\`.
   - \`## 7. Canales, interenlazado y Resend (regla capital: cero páginas huérfanas)\`: hub ×2 con \`comingSoon\` vaciado y la guarda de D6,
     alias del buscador, 8 posts con sustitución quirúrgica de banners (D46: \`fase8x\` generalizado), página de rol \`/usos/rol/…\`, las SEIS
     FAQ de consultoría a corregir (D12), correo 24-oct 08:00 UTC (D8), colaterales D15.
   - \`## 8. Capa de producto y gates (sesión B/C)\`: ficheros a tocar con ruta (49 en catálogo, payment-links, product-prices, functions,
     zona app, changelog, hub), cripto D16, gates (censo, paginas-gate, gate_libros, verificar_guion, robots-gate, whatsapp-gate, post-pago).
   - \`## 9. Presupuesto por sesión y por fase\`: que SUME (A4, ≈14,7-14,9 M): sesión A2+B1 (verificación legal ✅, SPEC, datos, 9 libros +
     refutación + fixer, guion + verificación) y sesión B2+C.
   - \`## 10. Lo que queda para John\`: Payment Link, compra de prueba, voz opcional (D13), decisión de sembrar «Próximamente» más adelante.
   - Cierre: \`## Cierre: hallazgos resueltos y decisiones\` con la tabla de los 28 hallazgos (id → decisión que lo resuelve, D1-D46 o nuevas
     que numeres desde D47) y el recuento de decisiones.
3. Autocomprobación final, y escríbela en \`avisos\`: \`grep -c '^## ' ${SPEC}\` debe dar **12** (§0-§10 + Cierre); \`wc -l\` ≥ 213 + lo tuyo;
   la fila D46 sigue intacta; ningún id «bare» de la lista de D44 aparece en tus secciones (grep); cada cifra de §3 lleva id o «supuesto
   declarado». Si detectas una contradicción entre tu §2-§10 y algo de §0-§1, NO edites §0-§1: anótala en \`avisos\` con la línea.
Devuelve el objeto estructurado.`,
  { label: 'spec-§2-§10', phase: 'SPEC', schema: SPEC_SCHEMA, model: 'opus', effort: 'xhigh' })
if (!spec) throw new Error('SPEC sin resultado')
log(`SPEC: ${spec.fichero} (${spec.lineas} líneas, ${spec.secciones_h2} H2) · ${spec.decisiones} decisiones · ${spec.hallazgos_resueltos}/28 · ${spec.libros.length} libros · avisos: ${spec.avisos.length}`)

phase('Refutar SPEC')
const REFSPEC_SCHEMA = {
  type: 'object',
  properties: {
    fichero: { type: 'string' }, veredicto: { type: 'string', enum: ['LISTO', 'CORREGIR ANTES', 'NO LISTO'] },
    altas: { type: 'integer' }, medias: { type: 'integer' }, bajas: { type: 'integer' },
    hallazgos: { type: 'array', items: { type: 'object', properties: { id: { type: 'string' }, gravedad: { type: 'string' }, problema: { type: 'string' }, fix: { type: 'string' } }, required: ['id', 'gravedad', 'problema', 'fix'] } },
  },
  required: ['fichero', 'veredicto', 'altas', 'medias', 'bajas', 'hallazgos'],
}
const refutarSpec = (ronda, extra) => agent(`# REFUTACIÓN DE LA SPEC — «Cómo Montar una Chocolatería» (ronda ${ronda})
${CONTEXTO}
## ENCARGO
Objeto: \`${SPEC}\` (ahora completa, §0-§10 + Cierre; §0-§1 los escribió un agente y §2-§10 otro, tras un corte: busca sobre todo las
COSTURAS entre las dos mitades). Tu trabajo es TUMBARLA antes de que se construya nada encima. Verifica contra los ficheros, no contra tu
memoria: (1) que los 28 hallazgos de \`${A}/guia-chocolateria-research-REFUTACION-${FECHA}.md\` están resueltos con el fix pedido o con
una alternativa argumentada (uno a uno, cita la línea de la SPEC); (2) que las D1-D18 de \`${PD}/guia-chocolateria-DECISIONES-${FECHA}.md\`
se aplican tal cual y que §2-§10 no contradicen ninguna D19-D46 de §1.C; (3) que TODO literal legal de la SPEC casa con \`${LEGAL_JSON}\`
(EUDR: 2.15 ↔ 38.3 ↔ 5.3.a/b y la fecha del operador posterior; 644.5 con su límite y la Regla 4.ª; RD 1055/2003 sin «fino/superior/extra»;
cadmio: el bombón fuera de la nota 14 —CHN-16b—; ocho alérgenos —CHN-34b—; convenio según D9/D43) y que nada de la lista de prohibiciones
del resultado legal (\`${RESULTADOS}\`) aparece como afirmación; (4) que la reconciliación con el kit es real: abre
\`astro-site/public/dl/kit-tareas-chocolateria/02-partidas-produccion.xlsx\` y \`06-eventos-temporada.xlsx\` (openpyxl read_only, uno cada vez)
y compara vidas útiles, temperaturas, campañas y valle con lo que la SPEC fija; (5) que los 9 libros son construibles con las convenciones
de familia, que ninguno declara una salida que exija otro libro, que ninguno rehace una tabla del kit ni copia con otro nombre un libro de
Pastelería, que el reparto de constructores no deja huérfano ningún libro, y que los dos «PENDIENTE PARA LA SPEC» de la verificación legal
(libro 5: etiquetado vs granel; libro 9: tabla de clientes 5.3.b + árbol operador/comerciante) están recogidos; (6) que el juego de datos
«La Almendra» tiene UNA fuente por concepto y que cada cifra lleva id o «supuesto declarado»: grep de los ids citados contra
\`${A}/guias-v2-research-sector.json\` (635 entradas) — **cualquier id inexistente, incluidos los «bare» de D44, es hallazgo ALTO**; (7) que
el índice no duplica al kit ni a Pastelería y que las decisiones legales que un xlsx aplica tienen su capítulo antes; (8) que el presupuesto
de §9 suma y casa con A4; (9) que la FAQ es de compra y no de consumidor (D39); (10) que el slug y las rutas no chocan
(\`curl -sI https://aichef.pro/guia-chocolateria-obrador\` → 404; robots.txt cubre \`guia-*\`). ${extra}
Escribe \`${A}/guia-chocolateria-SPEC-refutacion-${FECHA}${ronda > 1 ? '-r' + ronda : ''}.md\` con veredicto, recuento y cada hallazgo con
id, gravedad, afirmación literal, problema, evidencia y FIX concreto (línea de la SPEC + texto nuevo). Devuelve el objeto.`,
  { label: `refutar-spec-r${ronda}`, phase: 'Refutar SPEC', schema: REFSPEC_SCHEMA, model: 'opus', effort: ronda === 1 ? 'xhigh' : 'high' })

let ref = await refutarSpec(1, '')
if (!ref) throw new Error('refutación de la SPEC sin resultado')
log(`Refutación SPEC r1: ${ref.veredicto} · ${ref.altas}/${ref.medias}/${ref.bajas}`)
const rondas = [ref]
const fixes = []
let ronda = 1
while (ref.veredicto !== 'LISTO' && ronda < 3) {
  const FIX_SCHEMA = { type: 'object', properties: { aplicados: { type: 'integer' }, descartados: { type: 'array', items: { type: 'string' } }, lineas: { type: 'integer' } }, required: ['aplicados', 'descartados', 'lineas'] }
  const fix = await agent(`# FIXER DE LA SPEC — ronda ${ronda}
${CONTEXTO}
## ENCARGO
Aplica en \`${SPEC}\` TODOS los hallazgos de \`${ref.fichero}\` (léelo entero; lista resumida abajo), editando la SPEC en el sitio
(no reescribas secciones que no toca un hallazgo; aquí SÍ puedes tocar §0-§1 si un hallazgo lo exige). Si un hallazgo es incorrecto,
descártalo con motivo (id → motivo) y NO lo apliques. Mantén las 12 secciones H2 y actualiza la tabla del Cierre. Verifica los literales
legales contra \`${LEGAL_JSON}\` y los ids contra \`${A}/guias-v2-research-sector.json\` antes de escribirlos. Hallazgos:
${ref.hallazgos.map((h) => `- ${h.id} [${h.gravedad}] ${h.problema.slice(0, 300)} → FIX: ${h.fix.slice(0, 300)}`).join('\n')}
Devuelve el objeto.`,
    { label: `fix-spec-r${ronda}`, phase: 'Refutar SPEC', schema: FIX_SCHEMA, model: 'opus', effort: 'high' })
  fixes.push(fix)
  log(`Fixer SPEC r${ronda}: ${fix ? fix.aplicados : 0} aplicados · ${fix ? fix.descartados.length : '?'} descartados`)
  ronda += 1
  ref = await refutarSpec(ronda, `Esta es una RE-VERIFICACIÓN: comprueba sobre todo que los ${rondas[rondas.length - 1].hallazgos.length} hallazgos de la ronda anterior (\`${rondas[rondas.length - 1].fichero}\`) quedaron aplicados sin abrir contradicciones nuevas, y sólo después busca lo que se te escapó.`)
  if (!ref) throw new Error('re-refutación sin resultado')
  rondas.push(ref)
  log(`Refutación SPEC r${ronda}: ${ref.veredicto} · ${ref.altas}/${ref.medias}/${ref.bajas}`)
}

return { spec, refutaciones: rondas, fixes, veredicto_final: ref.veredicto }