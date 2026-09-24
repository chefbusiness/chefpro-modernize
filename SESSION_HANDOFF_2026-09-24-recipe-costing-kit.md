# Handoff 24 sep 2026 (tarde-noche) — Tienda internacional en inglés: piloto Recipe Costing Kit Pro (sesión Claude Code)

**Docs canónicos:**
- `scripts/productos-digitales/TIENDA-INTERNACIONAL.md`
- `scripts/productos-digitales/recipe-costing-kit/SPEC.md` (la que manda)

## Decisiones de John (24-sep)

| Tema | Decisión |
|---|---|
| Franja `TiendaStrip` de la portada EN | **Quitada** (PR #97 LIVE). Las 7 portadas llevan los mismos componentes |
| Aviso de pago cripto EN | La renuncia a los 14 días de cancelación dice «where it applies (EU/UK)» |
| Producto EN | **INDEPENDIENTE** del ES: su propio producto y Payment Link en Stripe (USD), su env var en Netlify, su dashboard y sus ficheros |
| Método | Duplicar lo ES y adaptarlo al mercado, con **research como en ES** (8 bloques) y OK de John antes de construir. **OK dado** |
| Anclas comerciales EN | **Igual que en español**, en USD. Sin reseñas, rating ni testimonios (decisión del 23-sep) |
| Hojas nuevas | **Yield Test + Ingredient Price List en ES y EN a la vez** → Kit de Escandallos **v2.1** primero |
| Licencia | **Un negocio (con todos sus locales) por compra**: se usa con clientes, sin entregarles copias. Escuelas: info@aichef.pro |

## Hecho

| Qué | Dónde |
|---|---|
| PR #97: sin franja en la portada EN + aviso cripto EN | `248f92a`, LIVE |
| F1 del piloto: inventario ES, research US/UK, research de 8 bloques, SPEC con 2 rondas adversariales (37 + 46 hallazgos) | `scripts/productos-digitales/recipe-costing-kit/` → `522fd0d` |
| **Kit de Escandallos Pro v2.1 LIVE**: plantillas 12 (Test de Rendimiento: despiece + cocción) y 13 (Lista de Precios con alerta de subidas); Conversiones con filas libres; merma del solomillo de la 01 calculada con el test (estimación declarada, 23,5 %); picada del 08 al 0 %; 11→13 en landing, dashboard, 7 hubs, emails y FAQ de la Guía Food Cost; changelog 2.1 | PR #98 → `dd3c128`. Gates en la preview: tienda-gate (`--esperadas`), gate-flujo-postpago 15 entregables / 0 fallos, pycel 0 errores / 2.800 fórmulas, censo 0 defectos |
| Correo ES de la v2.1 (prueba enviada a John) | `emails/broadcast-kit-escandallos-v2.1-es.html`; **hueco 3-nov 08:00Z, programable desde el 4-oct** |

## En curso al escribir esto

**F2-EN**: workflow `recipe-costing-kit-f2-en` (run `wf_c020cae2-1f9`).
- Fases: cimientos → traducción por grupos → mercado + PDF → instrucciones nuevas → `aplicar_en.py` + `gates_en.py` → revisión chef US/UK + técnica → arreglos.
- Salida dry-run en el scratchpad (`rck-dryrun/`); código y datos en `scripts/productos-digitales/recipe-costing-kit/`; notas en `F2-NOTAS.md`.
- Si la sesión muere, se retoma con `Workflow({scriptPath: <script del run>, resumeFromRunId: 'wf_c020cae2-1f9'})`: los agentes terminados se sirven de la caché. Antes, leer `journal.jsonl`.

## Siguiente

1. **Cerrar la F2-EN**: gates en verde, commit del código y los datos, y pedir a John el Payment Link USD $19 con el bloque de §5.1 de la SPEC (nombre, descripción, `success_url`, `currency_options` GBP/CAD/AUD). Antes, que compruebe en Stripe que USD es moneda de liquidación.
2. **F3 en UN SOLO PR** (SPEC §3). Todo junto:
   - `aplicar_en.py --real` → `dl/recipe-costing-kit/`;
   - data file EN y páginas anidadas;
   - dashboard EN (copia traducida) y componentes con `lang`;
   - backend (verify, resend, downloads, admin y su desplegable);
   - `CryptoPayButton` con `lang` + `/en/crypto-payment`;
   - ajuste de 6 gates;
   - catálogo con precio por idioma + 26 banners + spokes EN;
   - env var dada de alta; `sync-*`; `FAMILIAS.en.vivo = true`.

   Después: merge → compra de prueba → broadcast EN.

## Pendiente de John

- **Payment Link USD $19** (al cerrar la F2).
- **VAT del Reino Unido**: registro desde la primera venta a consumidores; verlo con el asesor antes de la F3.
- **Condiciones de compra EN** para productos digitales (`/en/terminos` solo cubre la suscripción). El ES tiene el mismo hueco.
- **Consentimiento para probar los Excel en Google Sheets** en su Drive.
- `PURCHASE_VALIDATION=strict`, sigue aparcado.
- Si quiere, pesar un solomillo real para sustituir la estimación del test de rendimiento ES.

## ⚠️ Colas de correo que NO son de este piloto y siguen sin programar

Hueco anterior al de la v2.1:
- **Chocolatería 24-oct**: programable desde hoy. Su HTML no está en `emails/`.
- **Taquería 29-oct**: programable desde el 29-sep.

## Consumo (tokens de subagentes)

- F1 del piloto EN: 2,8 M.
- ES v2.1: 1,7 M (casilla «v2.x ES» de la rotación).
- F2-EN: en curso; tope 1,8 M, y es probable que lo pase.
