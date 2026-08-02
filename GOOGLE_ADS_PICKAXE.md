# Google Ads en Pickaxe — qué pegar y dónde

> ID de la etiqueta: **`AW-17829651892`** · 2026-08-02.
> Etiqueta del evento de registro: **`AW-17829651892/-p23CMHO5docELTL67VC`**
>
> **Estado**: Snippet A ✅ pegado y verificado en vivo en `app.aichef.pro`.
> Snippet B ⬅ pendiente de pegar en `Confirmation Page Header`.
> Hay un **campo antiguo de confirmación** en Pickaxe con la etiqueta de Google
> pelada (sin Consent Mode y **sin evento**, o sea que no mide nada): vaciarlo.
> **La campaña es solo para el mercado ESPAÑOL** (decisión de John, 2026-08-02),
> así que esto se hace **únicamente en el workspace español** («AI Chef Pro -
> Español», el de `app.aichef.pro`). Los otros seis workspaces (en, fr, it, de,
> pt, nl) **no se tocan**: cuando alguna campaña los necesite, es el mismo
> snippet sin cambios.
>
> La mitad de `aichef.pro` **ya está hecha y desplegada** en código
> (`astro-site/src/components/GoogleTag.astro`), y cubre los 7 idiomas de la
> landing. Este documento es **solo** lo que hay que pegar a mano en Pickaxe.

## Por qué hacen falta las dos mitades

| Dónde | Qué hace | Sin esto… |
|---|---|---|
| **aichef.pro** ✅ hecho | Captura el `gclid` del clic y siembra la cookie `_gcl_aw` | Google Ads no atribuye NADA, haya o no evento |
| **app.aichef.pro** ⬅ esto | Dispara el evento cuando el usuario se registra | Se sabe que hubo clic, nunca que hubo alta |

**No hace falta «asociar» el subdominio a la campaña ni configurar cross-domain.**
`aichef.pro` y `app.aichef.pro` comparten **dominio registrable**, así que la
cookie que gtag guarda en `.aichef.pro` la lee el subdominio solo. Ir de la
landing a la app **no es cross-domain**.

---

## Paso 1 — Crear la acción de conversión (5 min, una sola vez)

Sin esto el Snippet B no tiene a dónde enviar nada.

1. Google Ads → **Objetivos → Conversiones → Nueva acción de conversión → Sitio web**
2. Dominio: **`aichef.pro`** (ver más abajo por qué, aunque el alta ocurra en el subdominio)
3. Cuando pregunte cómo configurarla → **«Añadir manualmente» / con código**.
   **NO** elijas la opción basada en URL («cuando alguien visite una página»):
   esa depende de la dirección concreta de destino, y las URLs internas de
   Pickaxe no las controlamos.
4. Categoría: **Registro** (`Sign-up`)
5. Te dará un `send_to` con esta forma: `AW-17829651892/AbC-D_efGhIjKlMnOp`
6. **Cópialo**: sustituye a `PEGA_AQUI_TU_ETIQUETA` en el Snippet B

### ¿Por qué `aichef.pro` si el registro ocurre en `app.aichef.pro`?

Duda razonable y conviene dejarla zanjada: **ese campo de dominio NO es donde se
cuenta la conversión.**

- Google lo usa para **detectar si ya hay una etiqueta instalada** en ese sitio y
  proponerte la configuración. En `aichef.pro` ya está, así que la encontrará —
  que es lo que hace desaparecer el aviso de «configuración errónea».
- La conversión **se atribuye por el `send_to`**, no por el dominio: el evento
  del Snippet B casa con el clic leyendo la cookie `_gcl_aw`, y ahí el dominio
  que escribiste al crear la acción no interviene.
- `app.aichef.pro` **es** `aichef.pro`: mismo dominio registrable, otro
  subdominio. Google lo trata como un solo sitio.

Pusieras `aichef.pro` o `app.aichef.pro`, la conversión se contaría igual.
`aichef.pro` es mejor porque es donde vive la etiqueta que Google va a detectar.

---

## Paso 2 — Snippet A → campo «Header»

Workspace **español** → `Deployments → Deploy Settings → Workspace Level Custom
code → Header`.

```html
<!-- Google tag (gtag.js) — AI Chef Pro, AW-17829651892 -->
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}

  // Lee la decisión de cookies tomada en aichef.pro. La cookie vive en
  // .aichef.pro, así que este subdominio la ve. Si el visitante entró directo
  // aquí sin pasar por la landing, no hay decisión y se queda DENEGADO.
  var m = document.cookie.match(/(?:^|; )aichef_consent=([^;]*)/);
  var ok = m && decodeURIComponent(m[1]) === 'accepted';
  var v  = ok ? 'granted' : 'denied';

  gtag('consent', 'default', {
    ad_storage: v, ad_user_data: v, ad_personalization: v, analytics_storage: v,
    functionality_storage: 'granted', security_storage: 'granted'
  });
  gtag('set', 'ads_data_redaction', !ok);
  gtag('set', 'url_passthrough', true);

  gtag('js', new Date());
  gtag('config', 'AW-17829651892');
</script>
<script async src="https://www.googletagmanager.com/gtag/js?id=AW-17829651892"></script>
```

## Paso 3 — Snippet B → campo «Body» (NO «Confirmation Page Header»)

> ⚠️ **Corregido el 2026-08-02 tras recorrer el flujo real con un navegador.**
> El plan inicial era pegarlo en `Confirmation Page Header`. **No sirve**: el
> alta de Pickaxe es un **modal**, no una página. No hay ninguna «confirmation
> page» en el registro gratuito, así que ese campo no se ejecutaría jamás.

### Lo que se comprobó, paso a paso

| Comprobación | Resultado |
|---|---|
| ¿El alta abre una página propia? | **No.** Es un modal sobre `/invitado` |
| ¿Cambia la URL al completar el alta? | **Sí**: recarga completa a `/invitado?success=login` |
| ¿Y al iniciar sesión un usuario YA existente? | **También `?success=login`** — no distingue |
| ¿El selector de plan («elige tu nivel de acceso») distingue? | **No**, sale en los dos casos |
| ¿Qué SÍ distingue el alta? | El modal de registro es **el único con DOS campos de contraseña** (el de login tiene uno) |

Por eso el snippet no puede limitarse a mirar la URL: **marca la intención de
alta cuando detecta el modal de registro**, y sólo entonces cuenta la conversión
al llegar la redirección de éxito.

Va en el campo **Body** del workspace español (se inyecta en todas las páginas,
que es lo que hace falta para poder escuchar el clic del modal).

Acción de conversión creada el 2026-08-02: **«Registro»**, evento manual,
categoría Registro, marcada como **Principal**. Su etiqueta ya está puesta abajo.

```html
<!-- Conversión "Registro" — AI Chef Pro. Va en el campo BODY del workspace. -->
<script>
(function () {
  var INTENCION = 'aichef_signup_intent';   // el usuario está en el modal de ALTA
  var HECHO     = 'aichef_conv';            // ya se contó en este navegador
  var AMBITO    = /(^|\.)aichef\.pro$/.test(location.hostname) ? '; domain=.aichef.pro' : '';
  var SEGURO    = location.protocol === 'https:' ? '; Secure' : '';

  function leer(n) {
    var m = document.cookie.match(new RegExp('(?:^|; )' + n + '=([^;]*)'));
    return m ? m[1] : null;
  }
  function guardar(n, v, seg) {
    document.cookie = n + '=' + v + '; path=/' + AMBITO + '; max-age=' + seg + '; SameSite=Lax' + SEGURO;
  }

  // 1) MARCAR LA INTENCIÓN DE ALTA.
  //    El modal de registro es el único con DOS campos de contraseña (el de
  //    login tiene uno). Es una señal ESTRUCTURAL: sigue funcionando aunque
  //    Pickaxe traduzca o cambie los textos de los botones. El match por texto
  //    va de refuerzo, no como criterio principal.
  //    15 minutos de margen: suficiente para el rodeo del OAuth de Google.
  document.addEventListener('click', function (ev) {
    var b = ev.target && ev.target.closest ? ev.target.closest('button') : null;
    if (!b) return;
    var t = (b.textContent || '').trim().toLowerCase();
    var esAlta = document.querySelectorAll('input[type=password]').length >= 2
              || t === 'create account' || t === 'crear cuenta'
              || t.indexOf('regístrate con') === 0 || t.indexOf('registrate con') === 0;
    if (esAlta) guardar(INTENCION, '1', 900);
  }, true);

  // 2) CONTAR LA CONVERSIÓN.
  //    Sólo si hay redirección de éxito Y veníamos de un alta. Un login normal
  //    llega igualmente a ?success=login, y por eso la URL sola no basta.
  if (location.search.indexOf('success=login') === -1) return;
  if (!leer(INTENCION)) return;             // era un login, no un registro
  if (leer(HECHO)) return;                   // ya contado en este navegador
  if (typeof gtag !== 'function') return;    // la etiqueta base no cargó

  gtag('event', 'conversion', {
    'send_to': 'AW-17829651892/-p23CMHO5docELTL67VC',
    'value': 1.0,
    'currency': 'EUR'
  });

  guardar(INTENCION, '', 0);                 // consumida
  guardar(HECHO, '1', 63072000);             // 2 años: un alta por navegador
})();
</script>
```

### Comportamiento, caso por caso (validado en el navegador)

| Escenario | ¿Cuenta? |
|---|---|
| Alta nueva desde el modal de registro | **Sí** ✅ |
| Login de un usuario ya existente | No ✅ |
| Alta y luego F5 / botón atrás | No ✅ (candado `aichef_conv`) |
| Navegación normal por la app | No ✅ |
| Abre el modal de alta y desiste | No ✅ |

### Tres diferencias con el fragmento que da Google, y las tres importan

1. **No dispara en cada carga.** El de Google cuenta una conversión cada vez que
   se carga la página. Aquí un F5 contaría otra alta e inflaría la señal con la
   que aprende Smart Bidding.
2. **Distingue alta de login.** Sin la marca de intención, cada vez que un
   cliente existente entrase desde un anuncio contaría como registro nuevo.
3. **Comprueba que `gtag` exista.** Si un bloqueador impide cargar la etiqueta
   base, el código de Google lanzaría un error de JS en mitad de la app. Este no
   mide y sigue.

> **Punto frágil, para que quede escrito**: si Pickaxe algún día pone un solo
> campo de contraseña en el alta (sin confirmación), la señal estructural deja de
> funcionar y sólo quedaría el match por texto. Si las conversiones caen a cero
> de golpe sin motivo, mirar esto lo primero.

> El Snippet A tiene que estar puesto **también**, o no existe `gtag` cuando
> corre el B y este falla en silencio.

---

## Limpieza pendiente

1. **Borrar la cuenta de prueba** `test-gads-20260802@mailinator.com`, creada el
   2026-08-02 para recorrer el flujo de alta.
2. **Vaciar el campo antiguo de confirmación** de Pickaxe: tiene la etiqueta de
   Google pelada, sin Consent Mode y **sin evento**, así que no mide nada y sólo
   carga la etiqueta una segunda vez.
3. `Confirmation Page Header` y `Confirmation Page Footer` se quedan **vacíos**:
   no intervienen en el registro gratuito.

## Ya había un GA4 en la plataforma

Al inspeccionar `app.aichef.pro` aparecieron dos etiquetas conviviendo:

- **`G-KVMQGZ1PH4`** — una propiedad de **Google Analytics 4** que ya estaba
  (cookies `_ga` y `_ga_KVMQGZ1PH4`). No la hemos tocado.
- **`AW-17829651892`** — la nuestra, del Snippet A.

No entran en conflicto. Pero conviene saber que existe: si algún día se quiere
importar conversiones desde GA4 en vez de medirlas con la etiqueta de Ads, la
propiedad ya está ahí. Ojo con no acabar contando la misma alta dos veces.

---

## Comprobación cuando esté puesto

1. Extensión **Google Tag Assistant** en `aichef.pro` → debe verse `AW-17829651892`.
2. Alta de prueba en la app → Tag Assistant debe registrar el evento `conversion`.
3. Google Ads → Conversiones: la acción pasa de **«Sin datos recientes»** a
   **«Registrando conversiones»**. Tarda hasta 24 h.
4. En consola, dentro de `app.aichef.pro`: `document.cookie` debe mostrar
   `_gcl_aw` **si** venías de un clic de anuncio. Si no está, la cadena se rompió.

---

## Nota aparte, no urgente

Comprobado el 2026-08-02: responden **200 los siete** subdominios de app
(`app`, `enapp`, `frapp`, `itapp`, `deapp`, `ptapp`, `nlapp`). Si solo querías
tener cuatro públicos, los otros están accesibles. No afecta a la campaña
española; queda anotado por si interesa revisarlo más adelante.
