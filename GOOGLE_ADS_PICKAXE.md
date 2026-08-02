# Google Ads en Pickaxe — qué pegar y dónde

> ID de la etiqueta: **`AW-17829651892`** · 2026-08-02.
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
2. Dominio: `aichef.pro`. Si pide configurarla a mano → **Añadir manualmente**
3. Categoría: **Registro** (`Sign-up`)
4. Te dará un `send_to` con esta forma: `AW-17829651892/AbC-D_efGhIjKlMnOp`
5. **Cópialo**: sustituye a `PEGA_AQUI_TU_ETIQUETA` en el Snippet B

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

## Paso 3 — Snippet B → campo «Confirmation Page Header»

Mismo sitio, campo **Confirmation Page Header**. Este es el que **cuenta la
conversión**. Lleva un candado para no contarla dos veces si el usuario recarga.

```html
<script>
  (function () {
    if (/(?:^|; )aichef_conv=1/.test(document.cookie)) return;   // antirebote

    gtag('event', 'conversion', {
      send_to: 'PEGA_AQUI_TU_ETIQUETA',   // <-- AW-17829651892/AbC-D_efGhIjKlMnOp
      value: 0.0,
      currency: 'EUR'
    });

    document.cookie = 'aichef_conv=1; path=/; domain=.aichef.pro; max-age=2592000; SameSite=Lax; Secure';
  })();
</script>
```

> El Snippet A tiene que estar puesto **también**, o no existe `gtag` cuando
> corre el B y este falla en silencio.

---

## ⚠️ Lo único que queda por confirmar

**¿El alta GRATUITA pasa por una «Confirmation Page» de Pickaxe?**

Los campos se describen como *«product confirmation pages»*, que suena a
**compra**, no a registro. Si el alta gratuita no pasa por ahí, **el Snippet B
no se disparará nunca en los registros** y la campaña seguirá sin medir nada.

- **Si pasa** → ya está, no hay más que hacer.
- **Si no pasa** → hay que disparar el evento en la **primera visita
  autenticada** desde el campo **Body**. Para escribirlo hace falta saber cómo
  marca Pickaxe que hay sesión iniciada: una clase en el `<body>`, una variable
  global, una ruta concreta tras el login… Con eso, son 6 líneas.

Forma rápida de salir de dudas: date de alta con un correo de prueba en
`app.aichef.pro` y mira **si la URL cambia a algo tipo `/confirmation`,
`/welcome` o similar** en algún momento del proceso.

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
