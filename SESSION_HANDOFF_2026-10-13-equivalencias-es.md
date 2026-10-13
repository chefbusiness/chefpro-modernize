# Handoff — 13-oct-2026 (sesión Claude Code): Guía de Equivalencias ES ↔ Hispanoamérica en los 51 productos ES

## Qué se hizo

Idea de John: el documento de equivalencias que se hizo para la tienda EN (US · UK · CA · AU, PR #129), pero **para
todos los productos ES** y **adaptado a cada producto**. Se trabajó en modo plan primero (John: «no se trata de que
salgas corriendo a picar código») y luego **solo con agentes sonnet** (John: «usa tus agentes tuyos, sonnet y haiku»).

- **Datos que lo justifican:** en GSC (90 días) Hispanoamérica suma ≈ 2.500 clics, 2,3 veces España, con mejor posición
  media. En DataForSEO, LatAm busca «HACCP» (MX 8.100) y no «APPCC» (MX 260); México dice «receta estándar» o «costeo
  de recetas» (880/390), pero Argentina y Chile siguen con «escandallo». Conclusión de método: **país a país**.
- **Arquitectura:** un docx por producto (`astro-site/public/dl/<producto>/guia-equivalencias-<slug>.docx`). La capa
  del producto sale de un censo automático de sus docx/xlsx. La capa común lleva el glosario, las medidas y 20 fichas
  de país con fuentes.
- **Fuente de todo:** `scripts/productos-digitales/equivalencias-es/`:
  - `PLAN.md`, `SPEC-FICHAS.md`, `SPEC-GLOSARIO.md` y `SPEC-BUILD.md`;
  - `censo-terminos-es.py` y `build_guia_es.py`;
  - `terminos.json` (206), `glosario/A.json` + `B.json`, `fichas/*.json` (20), `textos.json` y `datos/`.
  - Vista legible: `scripts/productos-digitales/GLOSARIO-JERGA-ES-LATAM.md`.
- **Países:**
  - 20 fichas: los 17 hispanos sin Cuba, Puerto Rico, EE. UU. en español y Brasil (en español).
  - Cuba entra solo en el vocabulario, porque desde allí no se puede pagar. Guinea Ecuatorial queda fuera.
- **Verificación:** 95 de 120 campos prioritarios con fuente abierta (impuestos, propina, laboral, sanidad, manipulador
  y licencias). El resto va marcado «Orientativo: confírmalo con la autoridad local». Hubo una revisión adversarial
  final; sus bloqueantes quedaron corregidos (cifras sin respaldo, importes en moneda local, coherencia interna).
- **Integración (PR #130):**
  - clave `guia-equivalencias` en `PRODUCT_FILES` (51, incluidos el Mega Pack y la rama del eBook);
  - tarjeta en los 51 dashboards;
  - BONUS (€15, imagen `es-guia-equivalencias.jpg`) en las 49 fichas de landing más el eBook. El Mega Pack lleva solo
    la línea del bonus: no tiene sección FAQ y no se añade diseño nuevo sin preguntar;
  - FAQ «¿Sirve en México, Colombia, Argentina…?» con 2 ejemplos del propio producto (`datos/integracion.json`);
  - 14 grupos nuevos en `sinonimos-buscador.json`;
  - recuentos de los correos de acceso de los planes de eventos (10/12).
- **Correo:** `emails/broadcast-guia-equivalencias-es.html`, **jueves 16-oct 08:00Z** (decisión de John), fuera de la
  cola de 5 días. La cola ES de producto no se mueve: siguiente hueco 28-nov.

## Hallazgos que valen para futuros productos

- Muchos portales oficiales de LatAm devuelven 403/DNS a los agentes. Por eso la regla 1bis admite una fuente
  secundaria fiable que afirme el dato de forma explícita: PwC Tax Summaries, NATLEX, FAOLEX, trade.gov, despachos.
- Datos del glosario que pueden romper un pedido o una carta:
  - «pimentón» es el pimiento en CO, VE y CL;
  - «bocadillo» es un dulce de guayaba en CO y VE;
  - «tostada» es una tortilla frita en MX;
  - «garrafa» es la bombona de gas en el Cono Sur;
  - «manteca» es mantequilla en el Río de la Plata y grasa de cerdo en MX;
  - «cuadrante» es geometría en MX.
- Datos fiscales y laborales que cambiaban la plantilla española:
  - Ley 27.802 en Argentina (6-3-2026);
  - reforma de las 40 h en México (DOF 3-3-2026);
  - Ley 21.561 en Chile;
  - IGV reducido para MYPE de restauración en Perú;
  - «Servicio 10 %» obligatorio en Costa Rica (Ley 9116);
  - rebaja de IVA en Uruguay con pago electrónico (Decreto 235/026).

## Pendiente / siguiente

- [ ] Gates contra el preview y LIVE: `gate-flujo-postpago.py`, `tienda-gate.py`, curl de 3 guías y de la FAQ en el
      JSON-LD. Después, merge.
- [ ] Correo: dry-run, prueba a John y `--scheduled-at 2026-10-16T08:00:00Z` (cuando la imagen esté LIVE).
- [ ] F4 (con datos y con visto bueno de John): descriptores LatAm en titles y metas donde haya brecha grande
      (APPCC → HACCP/BPM, escandallo → receta estándar), tras mirar la SERP.
- [ ] F4 confirmada por John: la misma capa por producto para los 13 EN.
- [ ] Revisión anual de las fichas: enero 2027.
- [ ] Gates con fallos previos, ajenos a este cambio: `paginas-gate.py` (29 FALLA) y `nombre-gate.py` (44/49).

## Coste

Subagentes ≈ 3,3 M tokens (techo M = 5 M):
- research de fichas y verificación, ≈ 1,9 M;
- glosario y censo, ≈ 0,5 M;
- generador y textos, ≈ 0,3 M;
- integración y correo, ≈ 0,5 M;
- exploración inicial, ≈ 0,3 M.
