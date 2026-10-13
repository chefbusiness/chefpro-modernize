# Guía de Equivalencias España ↔ Hispanoamérica y EE. UU.: bonus adaptado a cada producto ES

> Sesión Claude Code, 13-oct-2026. Modo plan (John: «entremos en modo iteración plan… no se trata de que salgas corriendo a picar código»).

## Contexto

Los 51 productos ES se construyen con el marco profesional español (escandallo, APPCC, cuadrante, camarero, nómina,
IVA 10 %), pero el comprador es hispano. Ya hay compras desde GT, PA, MX, AR, UY y VE (`PAGOS_CRYPTO_NOWPAYMENTS.md:9`),
y la memoria `feedback_productos-marco-espanol-mercado-hispano` lo recoge desde el 5-sep.

John propone llevar al español la idea de la guía EN (PR #129): un documento de equivalencias de **jerga profesional,
medidas y conceptos de negocio** por país, **adjunto a cada producto y adaptado a él** («que no es el mismo, que se adapta
a cada producto digital»). Sus ejemplos: escandallo ↔ costeo; galones en República Dominicana; libras en Colombia.

### Datos que lo respaldan (medidos hoy)

**Search Console, últimos 90 días, en clics:**

| País | Clics | País | Clics |
|---|---|---|---|
| España | 1.077 | Bolivia | 104 |
| México | 834 | Venezuela | 102 |
| Colombia | 333 | Guatemala | 59 |
| Argentina | 329 | El Salvador | 51 |
| EE. UU. | 297 | Uruguay | 50 |
| Perú | 279 | Brasil | 50 |
| Chile | 204 | Costa Rica | 41 |
| Ecuador | 137 | | |

Hispanoamérica suma **unos 2.500 clics, 2,3 veces los de España**, y con mejor posición media (7-8 frente a 13,8).

**DataForSEO, volumen de búsqueda al mes por país** (US-es = EE. UU. en español):

| Término | ES | MX | CO | AR | CL | PE | US-es |
|---|---|---|---|---|---|---|---|
| appcc | **4.400** | 260 | 110 | 70 | 50 | 90 | |
| haccp | 1.600 | **8.100** | **2.900** | 1.300 | **2.900** | **4.400** | |
| escandallo | **5.400** | 210 | 90 | **140** | **210** | 50 | |
| receta estándar | 10 | **880** | **320** | 40 | 20 | 110 | |
| costeo de recetas | 10 | 390 | 10 | 10 | 10 | 30 | |
| rol de turnos (cuadrante: ≤ 50 en todos) | 10 | **260** | 10 | 10 | 30 | **110** | |
| mesero | | **8.100** | 1.600 | 720 | | 1.600 | **18.100** |
| buenas prácticas de manufactura | | **4.400** | 2.400 | 880 | | 1.600 | 110 |
| arqueo de caja / corte de caja | | 2.900 / 1.600 | 1.000 / 140 | 1.300 / 170 | | 880 / 140 | 40 / 140 |
| manipulador de alimentos | | 210 | 720 | **1.900** | | 170 | 320 |

**Tres lecturas que condicionan el método:**
- **No hay un único «término latinoamericano».** Argentina y Chile dicen «escandallo» más que «receta estándar», y México
  usa «arqueo» y «corte de caja» a la vez. Por eso se investiga **país a país**, no por bloque.
- **El volumen engaña si no se mira la SERP.** «Garzón» da 18.100 en Colombia, pero ahí es un municipio del Huila y un
  apellido conocido; el garzón de sala es el chileno. Toda variante dudosa se confirma con la SERP.
- **«HACCP» y «BPM» mezclan intención industrial en LatAm.** Valen para el glosario; para el SEO, solo después de mirar
  la SERP.

## Enfoque recomendado

### 1. Un docx por producto, generado por script: capa del producto + capa común

Cada producto ES recibe **su** «Guía de Equivalencias para tu país», con dos capas.

**Capa del producto** (lo que cambia):
- Se titula «Tu [producto] en tu país».
- Recoge los **términos que aparecen en ESE producto**, extraídos automáticamente de sus docx y xlsx, con su equivalente
  país a país y ordenados por frecuencia.
- Añade una nota según el tipo de producto, sobre qué casillas o supuestos adaptar. Son 5 textos, uno por tipo: kit de
  tareas, kit Excel de gestión, plan de negocio, guía o manual, y eBook.

**Capa común** (la misma en todos):
- **Glosario profesional por temas:**
  - cocina e ingredientes;
  - puestos y oficios;
  - gestión y finanzas;
  - sanidad;
  - local e inmobiliario: traspaso ↔ llave, derecho de llave o prima;
  - conceptos de negocio y tipos de local: bar de tapas ↔ botanero, picada o piqueo; asador ↔ parrilla o asadero;
    hamburguesería; pizzería.
- **Medidas.** Sistema métrico como base, más las unidades de mercado locales: la libra de 500 g en Colombia frente a
  los 454 g; la arroba; el galón en RD, PR y Centroamérica; onzas y °F en EE. UU. y PR; pies² en EE. UU. y PR.
- **Ficha de una página por país**, con estos datos:
  - moneda;
  - impuesto al consumo en restauración (IVA, IGV, ITBIS, ITBMS, ISV, el impuesto al consumo del 8 % en Colombia);
  - propina y cargo por servicio (10 % por ley en Costa Rica y RD);
  - autoridad sanitaria y norma de referencia;
  - carné o curso de manipulador;
  - licencias de apertura;
  - alcohol;
  - formas jurídicas y régimen simplificado;
  - estructura laboral: jornada, prestaciones y entidad de seguridad social;
  - apps de delivery;
  - apoyos públicos al emprendimiento.

  Cada dato legal o fiscal lleva su **fuente oficial y la fecha de consulta**.

**Formato del glosario**, en página vertical y fiel país a país:
`camarero | mesero (MX, CentAm, CO, VE, RD, PR, US) · mozo (AR, UY, PY, PE) · garzón (CL) | nota`

**Coste por producto casi nulo.** El script recorre los 51 productos y genera los 51 docx desde una sola fuente
(`contenido_es.json` + matriz de términos). Los productos nuevos nacen con su guía con solo correr el script. Cada docx va
en la carpeta `dl/` del propio producto, como un entregable más.

### 2. Países

- Los 19 países hispanohablantes de América.
- **Puerto Rico:** habla español y se rige por la normativa de EE. UU.
- **EE. UU. en español.**
- **Brasil:** ficha en español, como pidió John; la tienda PT tendrá su propia guía.
- **Cuba:** solo su vocabulario, en el glosario.
- **Guinea Ecuatorial:** fuera (ver «Decisiones tomadas»).

### 3. Caducidad

- **Sin importes en moneda local que caducan**: salarios mínimos, tasas, inflación argentina.
- Cada dato se da como **estructura, tipo y nombre**, con enlace oficial y «consultado en oct-2026».
- **Revisión anual en enero**, cuando México, Colombia y Chile actualizan los salarios mínimos. Se apunta en
  `CALENDARIO-V2-SEMANAL.md`.

### 4. Capa SEO en las landings ES (la tercera capa que John pidió para EN)

- **FAQ en las 51 landings: «¿Sirve en México, Colombia, Argentina…?».**
  - Dirá que la guía de tu país va incluida y que ofrecemos la adaptación como servicio.
  - Citará los 2-3 términos LatAm del propio producto, sacados de su glosario.
  - Va en `faqs` y en `schema.faqs`.
  - Los 6 productos que ya tienen la FAQ «¿sirve fuera de España?» solo reciben una frase más (`guias/guia-pasteleria-obrador.ts:261`,
    `manuales/manual-manager-restaurante.ts:164`, etc.).
- **Vocabulario LatAm del producto en el cuerpo y en la FAQ.** Los títulos de producto y de marca no se tocan (regla de
  John, 13-oct).
- **Buscador del hub.** Se amplía `astro-site/src/lib/sinonimos-buscador.json` con la matriz, para que entienda «mesero»,
  «corte de caja» o «receta estándar».

## Fases (política de 3 fases, tamaño M: 2 sesiones, techo 5 M; objetivo ≈ 3 M tokens)

### F1 — Fundamentos (Mac para la API; censo en el VPS)

1. **Semilla del glosario.** Se consolidan las 6 fuentes dispersas que ya existen:
   - `astro-site/src/lib/sinonimos-buscador.json`;
   - las tablas §6 de `guia-pasteleria-SPEC.md:203`, `guia-churreria-SPEC.md:501` y `guia-chocolateria-SPEC.md:593`;
   - `manual-manager-SPEC.md:28`;
   - los research con México de `scripts/productos-digitales/auditorias/` (por ejemplo,
     `guia-pasteleria-research-L2-serp-demanda.md:395`).
2. **Censo de términos.** Un script nuevo, `censo-terminos-es.py`, reutiliza el recorrido de
   `scripts/productos-digitales/gate-no-latinos.py`:
   - lee docx y xlsx con zipfile y regex;
   - recorre `astro-site/public/dl/<producto>/`;
   - cuenta por producto los términos de España, con límites de palabra para evitar falsos positivos («sala» en
     «salado», «caja» suelta).

   Sale una matriz de términos × productos con frecuencias, que **decide qué se investiga** en lugar de adivinarlo.
3. **Research en una pasada.** Cuatro agentes sonnet, uno por región:
   - México, Centroamérica, Puerto Rico y EE. UU. en español;
   - RD, Colombia y Venezuela;
   - Perú, Ecuador y Bolivia;
   - Chile, Argentina, Uruguay, Paraguay y Brasil.

   Cada uno entrega las fichas de sus países y las variantes de los términos del censo, con fuente oficial por dato
   legal o fiscal. Las variantes dudosas se confirman con DataForSEO + SERP (`scripts/dataforseo.py --pais <código>
   --idioma es`). Salida: `scripts/productos-digitales/equivalencias-es/contenido_es.json` + `FUENTES.md`.
4. **Gate F1 y commit.** El JSON es válido; todo dato legal tiene URL; todo término tiene variante o «igual que en
   España».

### F2 — Entregables (VPS)

1. **`build_guia_es.py`**, copia parametrizada de `scripts/productos-digitales/equivalents-guide/build_guide.py`:
   - plantilla docx de un producto ES, para heredar estilos en español;
   - `CONTENTS`, `category`, `comments` y `language` (`es-419`) localizados;
   - `check()` invertido: hoy rechaza la ñ y las tildes; en ES prohibirá restos en inglés y exigirá los enlaces a
     aichef.pro/productos-digitales, johnguerrero.es e info@aichef.pro.
   - Genera los 51 docx.
2. **Gates:**
   - `gate-no-latinos.py`;
   - el docx abre (python-docx + LibreOffice);
   - el glosario del producto no está vacío y solo contiene términos presentes en el producto;
   - enlaces.
3. **Una revisión adversarial opus** sobre los datos legales y fiscales de las fichas y 3 docx de muestra de tipos
   distintos. Commit.
4. **Pausa para John:** le paso 2 docx de muestra (un kit de tareas y una guía) antes de cablear nada.

### F3 — Integración y lanzamiento

Patrón: el rollout EN, commit `cef6dab0`, ampliado a unos 105 ficheros. Las ediciones mecánicas las hace un script
revisado por sonnet.

- **`netlify/functions/get-download-urls.ts`.** Clave `guia-equivalencias` en las 49 entradas normales de
  `PRODUCT_FILES`, apuntando al docx de cada producto.
  - Mega Pack: una clave fuera del esquema `<kit>__<key>`, con su docx = la unión de los 13 kits.
  - eBook de prompts: rama especial con env vars (`~línea 1043`).
- **51 dashboards `src/pages/*Dashboard.tsx`.**
  - Tarjeta `{ key: 'guia-equivalencias', icon: Globe, type: '.docx', title, desc }` **literal en cada fichero**: el
    check C del gate compara las claves del dashboard con `PRODUCT_FILES` y no vería una constante importada.
  - Se corrigen los textos fijos tipo «Descarga los archivos .xlsx» o «N Files».
  - Mega Pack: una tarjeta propia bajo los acordeones, sin inflar «13 kits / 155 plantillas».
  - eBook: `DownloadsSection.tsx`.
- **49 fichas de landing en `astro-site/src/data/productos/**`.** Entrada en `bonus.items` (los 4 templates la pintan
  sin cambios), con una imagen Nano Banana común, y la FAQ en `faqs` + `schema.faqs`. Además, `mega-pack-tareas.astro` y
  `ProPromptsEbookPage.astro`.
- **Textos de correo.** Conteos «9/11 entregables» de los 5 planes de eventos en `resend-access.ts:462` y
  `verify-purchase.ts:499`.
- **Gates contra el preview y LIVE:** `gate-flujo-postpago.py` (checks B/C: disco, git, HTTP 200, claves en los dos
  lados), `tienda-gate.py`, `censo-entregables.py` y `paginas-gate.py`.
- **Un único broadcast ES** («nuevo bonus en todos tus productos: la guía de tu país») en el siguiente hueco de la cola,
  ES 28-nov 08:00Z.
- **Persistir:**
  - `GLOSARIO-JERGA-ES-LATAM.md`;
  - regla en la skill `productos-digitales-aichef`: «todo producto ES nace con su guía de equivalencias»;
  - memoria y handoff.

### F4 — Después, con datos y con visto bueno de John

- Descriptores LatAm en los titles y metas de las landings con brecha grande, siempre después de mirar la SERP:
  APPCC → HACCP/BPM, escandallo → receta estándar/costeo, cuadrante → rol de turnos.
- La misma capa por producto en los 13 EN, ya confirmada por John.

## Decisiones tomadas

1. **Capa por producto en los 13 EN: sí, en la F4, cuando el ES esté LIVE.** Lo confirmó John el 13-oct. Usa el mismo
   script y la misma matriz con columnas US · UK · CA · AU.
2. **Cuba y Guinea Ecuatorial.** La propuesta queda así y John puede cambiarla al revisar el plan:
   - **Cuba:** su vocabulario entra en el glosario, porque también lo usa la comunidad cubana de Miami. No lleva ficha
     legal ni fiscal, porque desde Cuba no se puede comprar: las sanciones de EE. UU. bloquean el pago con tarjeta.
   - **Guinea Ecuatorial** (el único país de África con el español como lengua oficial) queda fuera: no es mercado
     para nosotros.

## Verificación

- **Censo.** Control positivo: «escandallo» aparece en el Kit de Escandallos y «APPCC» en el Pack APPCC. Control
  negativo: un término de cocina no aparece en el plan financiero.
- **Cada docx:** abre; su glosario solo contiene términos de su producto; sin caracteres no latinos ni restos en inglés.
- **Preview de Netlify y luego LIVE:**
  - `gate-flujo-postpago.py` en verde sobre 64 productos;
  - `tienda-gate.py`;
  - descarga 200 de 3 guías de tipos distintos;
  - la FAQ visible y en el JSON-LD de 3 landings.
- Una revisión opus final, sin rondas encadenadas.
