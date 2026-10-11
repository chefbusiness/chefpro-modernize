# SESSION HANDOFF — 11-oct-2026 · productos digitales (sesión Claude Code, Mac + VPS)

> Sesión larga cerrada por ventana de contexto. Todo está en `main` (último commit de esta sesión: el de este fichero),
> Mac y VPS limpios, sin worktrees ni procesos en marcha. Detalle por producto: `scripts/productos-digitales/CALENDARIO-V2-SEMANAL.md`
> (entradas del 11-oct). Regla térmica del Mac vigente (istats, ≤ 2 agentes, lo pesado en el VPS).

## 0. Lo primero al retomar

1. **Comprobar las routines en la nube** (RemoteTrigger `list_runs`, o https://claude.ai/code/routines):
   - `trig_01WdpgX2KtUL9PbTyXHC4dVg` — **19-oct 08:23Z** — programa Churrería 13-nov 08:00Z (`395a7eb1`), Bakery EN 14-nov 14:00Z
     (`68bc8f49`) y **Paellero 2.2** 18-nov 08:00Z (`42ccda21`, nombre «Actualización Plan de Negocio Paellero 2.2 (ES)»).
   - `trig_01W3wg4wmuaSrGazNW6mep1u` — **20-oct 15:07Z** — programa Bar EN 19-nov 14:00Z (`813229ae`).
   - `trig_01RQdZrmsAtKFEUCjWykZQyy` — DESACTIVADO (el Catering EN salió adelante al martes).
   - Si una falló: programar a mano con la API de Resend (`resend-broadcast.py` / skill `resend-aichef`).
2. **Martes 13-oct** ya programados: Catering ES 2.2 08:00Z (`2b60e0ca`) y Catering EN 14:00Z (`dc53426b`). El 14-oct sale la Guía Pastelería.
3. Siguiente hueco libre de correos: **ES 23-nov 08:00Z · EN 24-nov 14:00Z**.

## 1. Qué se hizo hoy (PR → producción)

| PR | Qué |
|---|---|
| #115 · #116 | **Plan Paellero 1.2** (cliente real sin acceso: compró por la réplica de ChefBusiness; acceso reenviado) y manual técnico ampliado |
| #117 | **Tienda EN sin precio tachado** ni «valores» de bonus (FTC 16 CFR 233.1) |
| #118 | **Bar Business Plan Kit (EN, $39)** LIVE — `business-plans-en-3/` |
| #119 · #120 | **Carrusel de 9 logos en las 62/63 landings** (planes EN recortados + 10 guías y Mega Pack sin él); gate `scripts/astro-migration/carrusel-apps-gate.py` |
| #121 | **Bakery EN** también apunta a «pastry business plan» (1.900/mes; su SERP es de bakery) |
| #122 | **Catering Business Plan Kit (EN, $39)** LIVE — `business-plans-en-4/` (molde Food Truck EN con motor permutado eventos/año × $/invitado × invitados/evento + calculadora de precios) |
| #123 | **Plan Catering Temático ES 2.2** — modelo rehecho sobre el motor ES de línea A (`catering-es-2_0/`) |
| #124 | **Plan Paellero ES 2.2** (`paellero-2_2/`) + arreglos del Catering 2.2 LIVE (ver §3) |

**Tienda EN: 12 productos** (6 kits + 6 business plans $39). Gate completo LIVE al cierre: **63 productos / 823 entregables / 0 fallos**.

## 2. Método de la línea B → 2.2 (para parrillero, coctelería, chef privado)

Probado dos veces hoy (catering ≈ 1,9 M tokens, paellero ≈ 2,3 M):
1. **F1** (2 agentes opus en paralelo): arquitecto (inventario de la 1.x en el VPS + camino + lista exacta de afirmaciones falsas en
   landing/dashboard/hubs/email post-compra) ‖ research delta España (lo común ya está en `catering-es-2_0/F1-research-es.md`).
   El orquestador escribe la SPEC corta.
2. **F2**: el arquitecto pasa a implementador: módulo `planes-v2_0/contenido_<pid>/a.py` **clonado del paellero o del catering**
   sobre copia del **Food Truck ES v2.2**, scripts copiados en `scripts/productos-digitales/<pid>-2_2/` (semilla, checklist,
   cifras, tandas, docx, calculadora, `arreglos_d9`, `ciclo.sh`), motor **sin permutar** (invitados/evento × €/invitado ×
   eventos/año), calibración D15. Docx con 2 redactores Sonnet (tandas a/b, 131 ranuras del FT ES).
3. **F3** (opus): landing, dashboard, changelog, tarjetas de los 7 hubs, **email post-compra en `netlify/functions/verify-purchase.ts`**
   (no `productos-digitales-config.ts`, que no se envía) y correo de actualización.
4. **Una revisión opus** final → arreglos por texto → preview → merge → gates LIVE → correo.

**Lo que cazaron las revisiones (aplicarlo desde el principio):** restos del FT en `Instrucciones!A3`/docProps; nota del motor
«el Word sigue en la versión 1.1» (falsa en las 2.2: VOCABULARIO); **comida testigo** (RD 1086/2020 art. 30.8) en eventos > 40
personas; sin «carnet de manipulador» (ya no existe); extras **fijos discontinuos**, nunca «freelance»; contratos con plazos
coherentes, no desistimiento (art. 103.l TRLGDCU) y fuerza mayor; crecimiento del motor = invitados por evento (contarlo así);
holgura del año 2; precios coherentes entre Excel, carta, calculadora y landing; ayuntamientos sin anticipo (LCSP art. 198);
proporción comida/bebida del molde (B11) y «pan común» en Tesorería.

## 3. Deuda abierta (anotada en el calendario)

- **Línea B pendiente**: parrillero, coctelería, chef privado → misma 2.2 (proponer a John uno a uno). Sus tarjetas de hub y su
  email post-compra dicen «DOCX 60+ pp» / «17 CCAA» sin verificar.
- Los 5 planes de línea A: su docx sigue en 1.1 (T9) — ahí la nota del motor es cierta. Panadería: «Transacciones/día previstos /
  necesarios» (concordancia).
- Muchas guías dicen «60+ páginas» en los hubs (probablemente cierto; no medido).
- ChefBusiness (futuro, John): el hub de CB pasa a catálogo de tarjetas que abren la landing de aichef.pro, sin Payment Links propios.
- Candidatos EN con demanda medida: checklists de limpieza/apertura (~1.800/mes, HIGH, requiere motor de Tareas EN), ghost
  kitchen (370), menu engineering (480, informacional).

## 4. Decisiones de John de hoy

- Actualizar = retoques ligeros con sonnet/haiku (salvo que él pida subir a estándar, como el catering y el paellero).
- Tienda EN sin precio tachado; la ES mantiene su capa comercial. Testimonios: **si uno afirma algo falso del kit, se cambia
  solo esa frase** (aprobado 3 veces: Yuki, Marc Esteve, «los contratos B2B»).
- Correos de la 2.2 del catering fuera de la cola (martes 13-oct, el lunes 12 es festivo); el resto, cola de 5 días.
- El carrusel de logos completo va en todas las landings.
