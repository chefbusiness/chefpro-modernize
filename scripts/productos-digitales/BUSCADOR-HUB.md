# Buscador del hub de productos digitales — registro y lectura de la demanda

> Qué busca la gente en `aichef.pro/productos-digitales`, y qué busca **sin encontrarlo**.
> Esa segunda lista es la única fuente de demanda real y propia que tenemos para decidir el
> siguiente producto: no es un volumen de keyword prestado, es alguien que ya está en la
> tienda con la tarjeta a mano y no encuentra lo que venía a comprar.

> ⚠️ **ADMIN_PASSWORD es una variable SECRETA en Netlify**: `netlify env:get ADMIN_PASSWORD` devuelve un relleno de 20
> caracteres que no es la contraseña (verificado el 2026-09-05: con él, `search-report` y `admin-generate-access`
> responden 401). Para leer el informe hay que exportar la contraseña real: `ADMIN_PASSWORD='…' python3
> scripts/productos-digitales/buscador-report.py --days 30` o `curl -H "x-admin-password: …"`. Los logs de la
> function (`netlify logs --source functions --function log-search --since 10m`) del primer despliegue no muestran
> ningún error de escritura en Blobs (invocaciones de ~330 ms, sin «no se pudo escribir»).

## 1. Las piezas

| Pieza | Fichero | Qué hace |
|---|---|---|
| Buscador (front) | `astro-site/src/components/pages/ProductosDigitalesHubPage.astro` | Filtra las tarjetas en cliente (todas siguen en el DOM, se muestran/ocultan) y avisa al backend |
| Registro | `netlify/functions/log-search.ts` | POST público sin auth: valida y escribe **un blob por evento** |
| Informe | `netlify/functions/search-report.ts` | GET protegido con `x-admin-password`: agrega y devuelve JSON |
| Lectura + cruce | `scripts/productos-digitales/buscador-report.py` | Llama al informe y lo cruza contra el catálogo y la cola de productos |
| Almacén | Netlify Blobs, store **`search-queries`** | Clave `<YYYY-MM-DD>/<timestamp>-<aleatorio>` |
| Sinónimos + normalización | `astro-site/src/lib/sinonimos-buscador.json` + `normalizar-busqueda.ts` | **Fuente única** que leen el frontmatter del hub, el script del cliente y el informe |

**La normalización y los sinónimos NO se duplican.** Estuvieron copiados byte a byte en el
frontmatter y en el `<script>` del hub: dos definiciones que nadie cruzaba, y cambiar una sin
la otra deja el buscador sin encontrar nada **con el build en verde y sin diff que cante**.
Ahora hay un módulo (`normalizar-busqueda.ts`) que importan los dos, y los sinónimos viven en
un `.json` para que además los lea `buscador-report.py` sin parsear TypeScript. `log-search.ts`
y el `norm()` del script de lectura tienen que **producir la misma cadena**; están alineados a
mano y con un comentario recíproco en cada fichero (no hay forma de compartir código entre
Node, el navegador y Python).

La dependencia `@netlify/blobs` va en el **`package.json` de la RAÍZ** (`dependencies`), nunca
en `astro-site/package.json`: las functions se bundlean desde la raíz. Si se pusiera en el
otro sitio el build saldría verde y la function reventaría en producción con
`Cannot find module '@netlify/blobs'`. Al añadirla se actualizó también `package-lock.json`
(la raíz tiene lockfile y Netlify puede instalar con `npm ci`, que aborta si están
desincronizados).

## 2. Qué se registra

Un JSON por búsqueda, con estos campos y nada más:

| Campo | Ejemplo | Notas |
|---|---|---|
| `q` | `"carta de vinos"` | lo tecleado, recortado a 120 caracteres |
| `q_norm` | `"appcc haccp"` | minúsculas, sin acentos (ñ→n), **todo no-alfanumérico → espacio** (misma cadena que produce el buscador: si no, «APPCC.» y «appcc» se agregan por separado) |
| `n` | `0` | productos que casan con el texto **ignorando el chip de categoría** |
| `n_filtrado` | `0` | los que el visitante tenía delante (con el chip aplicado) |
| `coming` | `1` | tarjetas de «próximamente» que quedaron visibles |
| `tag` | `"guias"` | filtro de categoría activo, si lo había |
| `lang` | `"es"` | idioma de la página |
| `path` | `"/productos-digitales"` | página desde la que se buscó |
| `sin_resultados` | `true` | atajo de `n === 0 && coming === 0` — con `n` SIN chip |
| `detalle` | `"Busco plantillas de rotación de bodega"` | solo si el visitante rellena el campo de «no encuentro lo que busco» |
| `email` | `"…@…"` | **solo si lo escribe él**, para avisarle cuando exista el producto |
| `origen` | `"form"` | solo si el evento lo mandó el formulario (el informe no lo cuenta dos veces) |
| `country` | `"MX"` | código de 2 letras de la cabecera de geo de Netlify |
| `ts` | `"2026-09-05T09:12:33.481Z"` | UTC |

### Qué NO se registra, nunca

- **Ni IP ni user-agent.** No se leen esas cabeceras en ningún punto de la function
  (`grep -nE "user-agent|client-ip|x-forwarded-for" netlify/functions/log-search.ts` → 0).
- Ni cookies, ni identificador de sesión, ni nada que permita reconstruir la navegación de una
  persona. Dos búsquedas del mismo visitante son dos eventos independientes.
- El email solo existe si el propio visitante lo escribe pidiendo aviso. Es un dato de
  contacto voluntario, no telemetría.

**Por qué `n` ignora el chip.** Si se registrara lo que había en pantalla, un 0 provocado por
el filtro de categoría entraría en el informe como «demanda no cubierta»: medido sobre el
catálogo real, **178 de 204 estados vacíos** de la matriz chip×consulta son de esta clase
(chip «PDF / eBook» + «pizzeria» → 0 en pantalla y **7 productos** en la tienda). Serían
huecos falsos en la única lista con la que se decide qué se fabrica.

Del país solo se guarda el código ISO de 2 letras, que es lo que permite ver que la demanda
de un producto viene de México o Guatemala y no de España — dato que ya ha cambiado
decisiones de producto en esta tienda.

### Retención y borrado

Los eventos **no caducan solos**. La purga es manual, va autenticada y borra días completos
(con ellos, los emails de contacto):

```bash
curl -s -H "x-admin-password: $ADMIN_PASSWORD" \
  'https://aichef.pro/.netlify/functions/search-report?purge=1&before=2026-06-01'
# → {"ok":true,"purgado":true,"before":"2026-06-01","borrados":N}
```

- **Política:** purgar lo anterior a **12 meses** al menos una vez al año. Sin esto el store
  crece sin techo (invisible en el informe, que solo mira los últimos `days` días) y los
  emails quedan almacenados indefinidamente.
- **Baja a petición de una persona:** localiza su evento con `&raw=1` y borra esa clave
  concreta — `netlify blobs:delete search-queries <clave>` o desde el panel de Netlify.
- `before` tiene que ser **anterior a hoy** y con formato `YYYY-MM-DD`; si no, 400.

El formulario dice en la propia página para qué se usa el email y enlaza a `/privacidad`.

## 3. Contrato de las functions

### `POST /.netlify/functions/log-search`

```json
{ "q": "carta de vinos", "n": 0, "n_filtrado": 0, "coming": 0, "tag": "guias",
  "lang": "es", "path": "/productos-digitales", "sin_resultados": true,
  "detalle": "", "email": "", "origen": "", "website": "" }
```

- **204** siempre que la entrada sea válida — **incluso si Blobs falla**. El buscador de la
  página no puede degradarse por culpa del registro: la llamada es *fire-and-forget* y el
  fallo queda en los logs de la function, no en la cara del visitante.
- **400** si el JSON es inválido o algún campo se sale de rango (`q` de 1 a 120 caracteres
  tras limpiar, `n`/`n_filtrado`/`coming` enteros entre 0 y **10.000**, `tag` ≤ 40,
  `lang` ≤ 5, `path` ≤ 120, `detalle` ≤ 600, email con formato, cuerpo total ≤ 4 KB).
  El techo de los contadores no es decorativo: `Number.isInteger(1e308)` es `true`, y un
  solo POST con ese valor hacía que la media del informe saliera `Infinity`, se serializara
  como `null` y **reventara el formateo del script de lectura**.
- **405** con cualquier método que no sea POST u OPTIONS.
- **429** al pasar de **120 eventos por minuto** en todo el site. Los límites de tamaño
  acotan lo que ocupa cada evento, no cuántos hay: sin cupo, un bucle de `curl` infla la
  factura de Blobs y contamina la señal de demanda, que es el único producto de esto. El
  contador vive en un blob `rl/<YYYY-MM-DDTHH:mm>`, es **aproximado** (dos peticiones a la
  vez pueden leer el mismo valor) y si Blobs falla **se deja pasar**: el buscador nunca debe
  caerse por el registro.
- Todos los campos de texto se limpian de **caracteres de control** antes de validar. El
  regex de email no los bloquea (`\s` no cubre `ESC`), así que `a<ESC>[2JHACK@evil.com`
  pasaba la validación y el informe lo imprimía crudo en la terminal: un visitante anónimo
  podía falsear con secuencias ANSI lo que se lee para decidir el siguiente producto.
- `website` es un **honeypot** REAL: lo pinta `#pd-ask-website` en
  `ProductosDigitalesHubPage.astro` (oculto, `tabindex="-1"`, `aria-hidden`) y lo manda
  `enviarLog()`. Si viene con algo, se responde 204 y **no se escribe nada** (al bot no se le
  dice que ha sido detectado). ⚠ Durante un tiempo este documento y el comentario de la
  function afirmaban que existía **y no existía**: si se toca el formulario, comprobar que el
  campo sigue ahí (`grep -n 'name="website"'`).

Responsabilidad del front (no del backend): **debounce**. Sin él, cada tecla sería un evento
y el informe se llenaría de `k`, `ki`, `kit`, `kit e`… convirtiendo la señal de demanda en
ruido. Se registra la consulta cuando el visitante deja de escribir, no en cada pulsación.

### `GET /.netlify/functions/search-report?days=30`

Cabecera obligatoria `x-admin-password` con el valor de `ADMIN_PASSWORD` (la **misma** env var
que ya usa `admin-generate-access.ts`; no se ha creado ninguna nueva). Sin ella, **401**.

Devuelve `total`, `por_dia`, `top_queries` (consulta, veces, eventos, media de resultados,
`tags`, países), `sin_resultados` (lo mismo + `detalles` y `emails`) y `por_pais`. Con
`&raw=1` devuelve las entradas crudas. `days` se acota a 1-365.

**Techos, y por qué son esos** (una function síncrona de Netlify tiene ~10 s y 6 MB de
respuesta): `MAX_ENTRADAS` 3.000 lecturas, `MAX_RAW` 1.500 entradas crudas (a ~1,3 KB cada
una, las 5.000 de antes daban 6,11 MB y la respuesta se cortaba con un error de plataforma en
vez de con un JSON) y 500 filas por tabla agregada — antes emitía **una fila por consulta
distinta, sin tope**. Cuando algo se recorta la respuesta lo dice: `truncado`,
`top_queries_total`, `sin_resultados_total`. Los `list()` por día van en **paralelo** (eran
365 round-trips en serie *antes* de leer un solo blob) y las lecturas de 50 en 50.

La contraseña se compara con `timingSafeEqual` sobre digests SHA-256 (ni el contenido ni la
longitud filtran por tiempo) y hay un cupo de **5 intentos por minuto** → 429.

## 4. Cómo se lee el informe

```bash
python3 scripts/productos-digitales/buscador-report.py            # 30 días
python3 scripts/productos-digitales/buscador-report.py --days 7
python3 scripts/productos-digitales/buscador-report.py --min-veces 3
python3 scripts/productos-digitales/buscador-report.py --json
```

Necesita `ADMIN_PASSWORD` en el entorno o el CLI de Netlify autenticado (prueba
`netlify env:get ADMIN_PASSWORD` y, si falla, `netlify api getEnvVars`). La contraseña viaja
a `curl` por STDIN, nunca en `argv` (no aparece en `ps`). Se usa `curl` y no `urllib` porque
el `python3` del Mac no trae CA bundle y revienta con SSL — mismo motivo que en
`gate-flujo-postpago.py`.

La tabla cruza cada consulta contra dos fuentes:

- **¿existe?** — los arrays `products` y `comingSoon` del hub. Tres niveles: acierto en el
  **nombre**, acierto en nombre+slug+**tags**+alias, y acierto en **descripción+features**,
  que se marca con **`≈`** (parecido, *no* es ese producto). El cruce usa **el mismo corpus y
  los mismos sinónimos que el buscador** (`sinonimos-buscador.json`) y compara con **límite
  de palabra**. Cuando no lo hacía, la columna contradecía a la página: **22 de 52 consultas
  que el buscador SÍ resuelve** (42 %) salían marcadas como demanda no cubierta —«costeo de
  recetas», «haccp», «gerente», «alérgenos», «mermas»…, justo el vocabulario de
  Hispanoamérica— y «bar» casaba dentro de «barra» o «ia» dentro de «guía».
- **¿en cola?** — los productos ya planificados en `CALENDARIO-V2-SEMANAL.md` §3 y las líneas
  del calendario que nombran una «Guía», «Manual», «Kit», «Plan», «Pack» o «Cómo Montar».

Se marca con **⚠** la consulta buscada **≥ `--min-veces` veces (por defecto 2)** que no está
en la cola y cuyo **buscador LIVE devolvió 0 resultados** (media de resultados = 0, o todas
sus búsquedas registradas fueron sin resultados). **Manda el dato de producción, no el
`grep`**: si la persona no encontró nada en la página da igual lo que diga el cruce, y al
revés — «¿existe?» es una pista de contexto para saber *con qué* se parece, no el criterio.

Al final se listan las oportunidades con sus `detalles` y los emails de quien pidió aviso —
ésa es la lista con la que se decide el siguiente producto y a quién avisar cuando salga.

## 5. Cómo probar en producción

Netlify Blobs **solo existe desplegado**: en local no hay store (y aquí no se levanta
`netlify dev`, regla térmica del Mac). La prueba real es contra producción, después del
deploy:

**Paso 0, en el log del deploy** (solo la primera vez): `@netlify/blobs` es la **primera
dependencia externa de runtime** que importa una function de este repo — las otras siete solo
traen `import type` (que desaparece al compilar) e imports de ficheros locales. El `command`
de `netlify.toml` es `cd astro-site && npm install && npm run build`, así que la instalación
en la raíz depende del auto-install de Netlify, ruta que **nunca se había ejercitado para el
bundling de functions**. Comprobar en el log (a) que hay un install en la raíz del repo y
(b) que el bundling de `log-search`/`search-report` **no** dice
`Could not resolve '@netlify/blobs'`. Si falla, cambiar el command a
`npm ci && cd astro-site && npm install && npm run build`.

⚠ El **paso 1 devuelve 204 aunque Blobs esté roto** (el `catch` lo silencia a propósito):
el que verifica de verdad la escritura es el **paso 4**.

```bash
# 1) el registro acepta un evento válido → 204
curl -i -X POST https://aichef.pro/.netlify/functions/log-search \
  -H 'Content-Type: application/json' \
  -d '{"q":"prueba curl","n":0,"coming":0,"sin_resultados":true,"path":"/productos-digitales"}'

# 2) valida de verdad → 400
curl -s -o /dev/null -w '%{http_code}\n' -X POST \
  https://aichef.pro/.netlify/functions/log-search \
  -H 'Content-Type: application/json' -d '{"q":""}'

# 3) el informe está protegido → 401 sin cabecera
curl -s -o /dev/null -w '%{http_code}\n' \
  https://aichef.pro/.netlify/functions/search-report

# 4) y con la contraseña devuelve el evento de la prueba
curl -s -H "x-admin-password: $ADMIN_PASSWORD" \
  'https://aichef.pro/.netlify/functions/search-report?days=1'

# 5) o directamente, con el cruce hecho
python3 scripts/productos-digitales/buscador-report.py --days 1
```

Si el paso 1 devuelve 204 pero el 4 no ve el evento, el sospechoso es Blobs, no el registro:
mira los logs de la function en Netlify (`log-search: no se pudo escribir en Blobs`). Causas
posibles: la dependencia no llegó al bundle, o el store no está habilitado para el site.

## 6. Gotchas

- **Function v1 y `connectLambda`.** Estas functions usan el `Handler` de `@netlify/functions`
  (estilo Lambda). En ese estilo el contexto de Blobs llega en `event.blobs`, así que hay que
  llamar a `connectLambda(event)` **antes** de `getStore`. El tipo público de `HandlerEvent` no
  declara ese campo: de ahí el cast en el código.
- **La versión de `@netlify/blobs` está pinchada a `^10.7.13` a propósito.** La 11 exige
  Node ≥ 22.12 y `netlify.toml` fija `NODE_VERSION = "20"`.
- **Un blob por evento, nunca un JSON que crece.** Leer-modificar-escribir un único fichero
  haría que dos visitantes simultáneos se pisaran y se perdieran búsquedas en silencio.
- **La clave lleva el día por delante** (`2026-09-05/…`) para que el informe pueda listar por
  prefijo y no recorrer el store entero.
- **El informe lee blob a blob y la function tiene ~10 s.** Por eso los `list()` van en
  paralelo y los techos son alcanzables (3.000 entradas, 1.500 en crudo, 500 filas por
  tabla). Si algún día hicieran falta ventanas más largas de verdad, la salida no es subir
  los techos: es que `log-search` mantenga además un **rollup diario** y que el informe lea
  el rollup en vez de los eventos.
- **No hay borrado automático, pero sí purga.** `search-report?purge=1&before=YYYY-MM-DD`
  (ver §2). Para una clave suelta sigue valiendo `netlify blobs:delete search-queries <clave>`.
- **Los contadores del cupo viven en el mismo store con prefijo `rl/`.** No los recoge el
  informe (lista por prefijo de día) y la purga los limpia igual que los eventos.
- **`n` es el conteo SIN chip.** Al leer el JSON crudo, `n_filtrado` es lo que se vio en
  pantalla. Compararlos dice cuántas veces el filtro de categoría estorbó.
