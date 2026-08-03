# Google Ads — gestión de campaña y estructura de cuentas

> Escrito el 2026-08-03, al terminar de montar la medición de `aichef.pro`.
> El **cómo se instaló** está en [`GOOGLE_ADS_PICKAXE.md`](GOOGLE_ADS_PICKAXE.md).
> Esto es el **cómo se gestiona a partir de ahora** y la respuesta a «¿puedo
> anunciar otra marca desde la misma cuenta?».

## Estado a 2026-08-03

| | |
|---|---|
| Cuenta | `907-887-7698` (aichefpro@gmail.com) |
| Etiqueta de Google | `AW-17829651892` |
| Conversión activa | **Registro** — `AW-17829651892/-p23CMHO5docELTL67VC` |
| Campaña | «IA para Chefs Profesionales» · Máximo rendimiento · **5 €/día** · Maximiza las conversiones |
| Objetivo de la campaña | **Registros** (específico de la campaña) |
| Mercado | **Solo España** |

---

## Lo que NO hay que tocar durante 2-3 semanas

**No cambies la puja ni el presupuesto.** Cada modificación reinicia el periodo
de aprendizaje de Smart Bidding. Con 5 €/día vas a estar muy por debajo de las
~30 conversiones/mes que el algoritmo necesita para afinar, así que los primeros
números van a parecer malos **aunque todo esté bien**. La diferencia respecto a
antes es que ahora la señal existe; antes no llegaba ninguna.

**No completes el asistente de la tarjeta «Mide las conversiones».** Google la
muestra automáticamente mientras no registre conversiones, y si la sigues te crea
una **acción de conversión duplicada**. Entonces vuelves al problema de origen:
dos señales compitiendo, una de ellas vacía. Dale a Cancelar, o descarta esa
recomendación concreta desde sus tres puntos. **No uses «Rechazar todas»**: ahí
dentro hay otras recomendaciones que sí conviene leer.

**«Apto (configuración errónea)» no significa que esté mal montado.** Google
muestra el mismo aviso cuando la medición está bien pero todavía no ha entrado
ninguna conversión real. Se irá solo con el primer registro desde un anuncio.

---

## La lección que costó dinero

Descubierto el 2026-08-03: la campaña tenía como objetivo **«Vistas de una
página»**, marcada como **principal**, en estado **Inactivo** y con **0,00
conversiones**. Como el sitio no había tenido nunca una etiqueta instalada,
Smart Bidding llevaba repartiendo el presupuesto **sin una sola señal con la que
aprender**.

**Revisa esto cada vez que crees o heredes una campaña**: Objetivos →
Conversiones → Resumen. Mira la columna *Estado* de las acciones marcadas como
principales. Si pone **Inactivo** o **0,00 conversiones** y la campaña la está
usando, estás pagando a ciegas.

Quedan en la cuenta **3 acciones viejas en la categoría «Suscripción»** que
tampoco han recibido datos nunca. No las usa ninguna campaña, pero conviene
revisarlas o archivarlas para que no se cuelen en el futuro.

---

## Qué mirar, y cuándo

| Cuándo | Dónde | Qué esperas ver |
|---|---|---|
| 24-48 h tras el primer registro real | Objetivos → Conversiones | *Registro* pasa a **«Registrando conversiones»** |
| Semanal | Campaña → Vista general | Conversiones > 0 y coste por conversión |
| Si las conversiones caen a **cero de golpe** | Ver el punto frágil de `GOOGLE_ADS_PICKAXE.md` | Que Pickaxe haya cambiado el formulario de alta |

**Comprobación manual en cualquier momento**: instala la extensión **Google Tag
Assistant**, entra en `aichef.pro`, acepta las cookies y haz un alta de prueba.
Debes ver la etiqueta `AW-17829651892` en la landing y el evento `conversion` al
completar el registro en `app.aichef.pro`.

---

## ¿Puedo anunciar Miselup (u otra marca) desde esta misma cuenta?

**Sí.** Una cuenta de Google Ads admite campañas apuntando a dominios distintos.
No hay restricción técnica ni de política. La única regla es que, **dentro de
cada anuncio**, la URL final y la URL visible coincidan entre sí.

### Si lo haces en la misma cuenta, esto es OBLIGATORIO

En **todas** las campañas, poner los objetivos de conversión como **«Específico
de la campaña»**, no «Predeterminado de la cuenta»:

> Campaña → Configuración → Optimización de presupuesto y puja → Objetivos de
> conversión → **Específico de la campaña**

Si se quedan en el valor por defecto de la cuenta, la campaña de Miselup
optimizaría también hacia los registros de AI Chef Pro y viceversa. Cada marca
necesita además **su propia acción de conversión** (p. ej. *Registro Miselup*).

### Pero para el grupo, la estructura buena es un MCC

Hay **seis marcas** en ChefBusiness Group (aichef.pro, miselup.pro, gastroseo,
gastrolocal, chefbusiness.co, hosply). Esto va a volver a pasar, y **mover
campañas entre cuentas después es caro: se pierde el histórico de conversiones y
el aprendizaje de la puja**. Es una decisión que conviene acertar de entrada.

| | Misma cuenta | Cuenta aparte bajo MCC |
|---|---|---|
| Puesta en marcha | Inmediata | ~15 min |
| Facturación y reporting por marca | Mezclados | **Separados** |
| Contaminación de señales entre campañas | Real; hay que forzar objetivos específicos | Ninguna |
| Añadir más marcas después | Se enreda | Una cuenta más |
| Si vendes o cedes una marca | Lío | La cuenta se va con ella |

### Cómo crear el MCC

1. Ir a **[ads.google.com/home/tools/manager-accounts](https://ads.google.com/home/tools/manager-accounts)** → *Crear una cuenta de administrador*.
2. **Usar un correo DISTINTO** del que gestiona la cuenta actual: un email no
   puede ser a la vez administrador y cliente de la misma jerarquía. Vale un
   alias del dominio (p. ej. `ads@chefbusiness.co`).
3. Elegir «Gestionar las cuentas de otras personas» y rellenar zona horaria
   (Madrid) y moneda (EUR). **La moneda no se puede cambiar después.**
4. Desde el MCC: **Cuentas → + → Vincular cuenta existente**, e introducir el ID
   `907-887-7698`. Llega una solicitud que hay que **aceptar desde la cuenta de
   AI Chef Pro**.
5. Para cada marca nueva: **Cuentas → + → Crear cuenta nueva**.

**Lo que el MCC NO hace**: no mezcla presupuestos ni datos entre cuentas hijas, y
no cambia nada de lo ya configurado. Solo da un login único y reporting agregado.

### Antes de lanzar CUALQUIER campaña de otra marca

Comprobado el 2026-08-03: **`miselup.pro` y `app.miselup.pro` no tienen hoy
ninguna medición** — ni etiqueta de Ads, ni GA4, ni nada. Están exactamente como
estaba `aichef.pro` esta mañana.

**No se lanza una campaña sin medición.** Es repetir el error que costó dinero
aquí. El trabajo previo es el mismo que se hizo hoy:

1. Etiqueta base en el dominio donde aterriza el clic.
2. Consent Mode v2 + banner (es un SaaS europeo, aplica igual).
3. Acción de conversión propia.
4. **Averiguar dónde ocurre el alta de verdad y verificarlo en vivo** — hoy
   quedó demostrado que esto no se puede dar por supuesto: el plan inicial en
   `aichef.pro` habría medido cero porque el registro es un modal, no una página.
