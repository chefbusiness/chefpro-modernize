# Google Ads en Pickaxe — qué pegar y dónde

> ID de la etiqueta: **`AW-17829651892`** · Creado el 2026-08-02.
> La parte de `aichef.pro` (la landing) ya está hecha en código: `astro-site/src/components/GoogleTag.astro`.
> Este documento cubre **solo** lo que hay que pegar a mano en Pickaxe.

## Por qué hacen falta las dos mitades

| Dónde | Qué mide | Sin esto… |
|---|---|---|
| **aichef.pro** (ya hecho) | Captura el `gclid` del clic y siembra la cookie `_gcl_aw` | Google Ads no puede atribuir NADA, haya o no evento |
| **Pickaxe** (esto) | Dispara el evento cuando el usuario se registra | Se sabe que hubo clic, pero nunca que hubo alta |

**No hace falta «asociar» el subdominio a la campaña ni configurar cross-domain.**
`aichef.pro`, `app.aichef.pro`, `enapp.aichef.pro`… comparten **dominio
registrable**, así que la cookie que gtag guarda en `.aichef.pro` la leen todos
los subdominios solos. Cruzar de la landing a la app **no es cross-domain**.

## Paso 0 — Crear la acción de conversión (una sola vez)

Sin esto los snippets no tienen a dónde enviar nada.

1. Google Ads → **Objetivos → Conversiones → Nueva acción de conversión → Sitio web**.
2. Dominio: `aichef.pro`. Si pide configurarla a mano, elige **Añadir manualmente**.
3. Categoría: **Registro** (`Sign-up`).
4. Al terminar te da un **`send_to`** con esta forma:
   `AW-17829651892/AbC-D_efGhIjKlMnOp`
5. **Copia esa cadena entera.** Es la que sustituye a `PEGA_AQUI_TU_ETIQUETA` en el snippet B.

## Snippet A — campo «Header» de CADA workspace

**Va en los 7 workspaces** (es, en, fr, it, de, pt, nl), en
`Deployments → Deploy Settings → Workspace Level Custom code → Header`.
Es idéntico en todos: no hay que cambiar nada por idioma.

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

## Snippet B — campo «Confirmation Page Header»

Va en el mismo sitio, en el campo **Confirmation Page Header**. Este es el que
**cuenta la conversión**, y lleva un candado para no contar dos veces si el
usuario recarga la página.

```html
<script>
  (function () {
    // Antirebote: una conversión por usuario cada 30 días, aunque recargue.
    if (/(?:^|; )aichef_conv=1/.test(document.cookie)) return;

    gtag('event', 'conversion', {
      send_to: 'PEGA_AQUI_TU_ETIQUETA',   // <-- AW-17829651892/AbC-D_efGhIjKlMnOp
      value: 0.0,
      currency: 'EUR'
    });

    document.cookie = 'aichef_conv=1; path=/; domain=.aichef.pro; max-age=2592000; SameSite=Lax; Secure';
  })();
</script>
```

> El Snippet A tiene que estar puesto **también** para que exista `gtag` cuando
> corra el B. Si sólo pones el B, no pasa nada: falla en silencio.

## Lo que falta decidir (2 cosas)

### 1. ¿El alta gratuita pasa por una «Confirmation Page»?

En Pickaxe, esos campos se describen como *«product confirmation pages»*, que
suenan a **compra**, no a registro. Si el alta gratuita **no** pasa por ahí, el
Snippet B no se disparará nunca en los registros.

- Si pasa → listo, no hay que hacer nada más.
- Si no pasa → hay que disparar el evento en la **primera visita autenticada**,
  desde el campo **Body**. Para escribir eso necesito ver cómo marca Pickaxe que
  hay sesión iniciada (una clase en el `<body>`, una variable global, una ruta
  concreta). **Dímelo o dame acceso y lo escribo.**

### 2. ¿Banner de cookies también en Pickaxe?

Hoy el consentimiento se pide **solo en la landing**. Quien entre directo a
`app.aichef.pro` (marcador, enlace de email, un anuncio que apunte ahí) nunca ve
el banner, así que se queda en **denegado** y su conversión sólo se modela.

- Si el 100% del tráfico de Ads entra por la landing, da igual.
- Si no, hay que poner un banner también en el campo Body de los 7 workspaces.

## Comprobación cuando esté puesto

1. **Extensión Google Tag Assistant** en `aichef.pro` → debe verse `AW-17829651892`.
2. Navega a la app y haz un alta de prueba → Tag Assistant debe registrar el evento `conversion`.
3. Google Ads → Conversiones → la acción pasa de **«Sin datos recientes»** a
   **«Registrando conversiones»**. Tarda hasta 24 h; no te alarmes antes.
4. En el navegador, consola: `document.cookie` en `app.aichef.pro` debe mostrar
   `_gcl_aw` **si** venías de un clic de anuncio. Si no está, la cadena se rompió.

## Aviso sobre los subdominios

Comprobado el 2026-08-02: responden **200 los siete**, no tres o cuatro —
`app`, `enapp`, `frapp`, `itapp`, `deapp`, `ptapp` y `nlapp`. Si de verdad sólo
quieres cuatro públicos, los otros tres están accesibles y conviene revisarlo
(aunque no estén enlazados, son indexables si alguien los enlaza).
