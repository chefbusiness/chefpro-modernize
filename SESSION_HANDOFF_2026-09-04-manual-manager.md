# Handoff — Manual del Manager de Restaurante (producto nuevo nº 2) · sesión Claude Code 2026-09-04 → 05 (Mac)

> Segundo producto nuevo del ciclo alternado. John pidió «hoy de nuevo un producto nuevo» tras la primera venta
> de la Guía Food Cost (66 € con IVA, salida del mailing de las 10:00) y eligió el Manual entre los cuatro
> «próximamente» del hub. Método idéntico al de ayer, con dos mejoras: los textos los escriben 24 redactores
> Sonnet en paralelo (regla «bridge no para productos») y el bloque legal lleva refutador propio con el BOE.

## 1. Estado al cierre (02:10 del 5-sep) — **LIVE COMPLETO**: `gate-flujo-postpago.py --only manual-manager-restaurante` = 0 fallos, 0 avisos (landing con `buy.stripe.com` en sus 4 CTA, access/library 200, 11 descargas binarias con tamaño de disco, webhook armado)

| Pieza | Estado |
|---|---|
| Research (5 lentes + síntesis + refutación) | ✅ `scripts/productos-digitales/auditorias/manual-manager-*` · 32 hallazgos (10 altos) resueltos en la SPEC §1 |
| SPEC v1.0 | ✅ `scripts/productos-digitales/manual-manager-SPEC.md` (22 decisiones) |
| Datos únicos | ✅ `scripts/productos-digitales/manual-manager/datos_ejemplo.py` (La Encina: 12 personas, 6 estaciones, 52 semanas ISO, 4 semanas malas; `checks()` cuadra con la Guía Food Cost al −0,58 %) |
| 7 xlsx | ✅ `astro-site/public/dl/manual-manager-restaurante/` (1.885 fórmulas, 0 prohibidas, 0 constantes, 45 notas legales «Verificado el 04-09-2026»; refutación de 19 hallazgos aplicada) · generadores `manual-manager/gen_*.py` + `mapa-*.json` |
| Guion | ✅ `guias-v2_0/guion_manual_manager_restaurante.py` (20 caps + 12 situaciones; 251 referencias a celda, 0 rotas; 42 tablas; 42 prohibiciones) + `manual-manager/verificar_guion.py` |
| Documentos | ✅ manual **77 páginas** (41.235 palabras, 30 tablas) · bonus **28 páginas** (11.530 palabras, 12 tablas); todos los gates en verde al tercer ensamblado. Texto: 54 bloques por 24 agentes Sonnet (`check_bloque.py` en verde), caché espejada en `manual-manager/build/docs/txt/` |
| Capa de producto | ✅ landing `astro-site/src/data/productos/manuales/manual-manager-restaurante.ts` (carpeta nueva de la línea), wrapper, zona app generada (46), 4 functions + config, catálogo 46, hub con «Nuevo» y `comingSoon` retirado, changelog 1.0, linkify, footerLinks cruzados |
| Prefijo `manual-` | ✅ `robots.txt` con sus 10 reglas; `robots-gate.py --live` verde (1.188 públicas / 92 privadas) |
| Imágenes | ✅ 6 galería + OG (`e884a8d`), revisadas a ojo |
| Blog | ✅ 5 posts con banner fijado + enlace contextual (`fase8g-manual-manager-blog.py`, gate de reversibilidad) + `blog-lastmod.json` |
| Email | ✅ `emails/broadcast-manual-manager-lanzamiento-es.html` · prueba enviada a John (`a97f3d1f…`) · **broadcast `3749f084-138d-459b-a027-f377a6d10d0c` programado para el lunes 2026-09-07 08:00 UTC (10:00 Madrid)**, segmento «AI Chef Pro ES», asunto «Nuevo: el Manual del Manager de Restaurante» (lunes por decisión de John; ayer ya salió un mailing a la misma lista) |
| Stripe | ✅ Payment Link creado por John (`https://buy.stripe.com/3cIcMY1C4csC635ejH6oo1p`) · env `VITE_STRIPE_PAYMENT_LINK_MANUAL_MANAGER` puesta por Claude (scope builds, todos los contextos) · `payment-links.ts` regenerado (46) · redeploy `b2957ab` |
| Hotfix colateral | ✅ la landing de la Guía Food Cost servía DOS botones de WhatsApp (faltaba `whatsapp={false}` en el wrapper); corregido en el mismo push |

Descripción de Stripe (John pidió quitar la verificación contra el BOE del copy corto; se mantiene en landing, email y producto): «Manual del Manager de Restaurante: 20 capítulos (77 páginas) para dirigir el día a día del local —operaciones, equipo, números, servicio y obligaciones legales—, 7 plantillas Excel con fórmulas vivas y un bonus de 12 situaciones reales resueltas paso a paso. Pago único, acceso vitalicio y actualizaciones incluidas.»

## 2. Cierre (hecho en el orden previsto; queda solo el punto 4 para John)

1. John: Payment Link + env var (fila «Stripe» de la tabla). 2. `python3 scripts/productos-digitales/sync-payment-links.py` → `netlify/shared/payment-links.ts` (46) → commit + push → build `ready`.
3. `python3 scripts/productos-digitales/gate-flujo-postpago.py --only manual-manager-restaurante` → 0 fallos (landing con `buy.stripe.com`, access/library 200, 11 descargas binarias con el tamaño de disco).
4. Compra de prueba real (o `aichef.pro/admin/generar-acceso`) — **pendiente de John**; el gate LIVE verifica todo lo demás.
5. Email: `python3 scripts/productos-digitales/emails/resend-broadcast.py --html scripts/productos-digitales/emails/broadcast-manual-manager-lanzamiento-es.html --subject "Verificado contra el BOE (convenio incluido)" --name "Lanzamiento Manual del Manager (ES)" --test john@chefbusiness.co` → revisar → mismo comando con `--scheduled-at <día>T08:00:00Z` (10:00 Madrid).
6. `sitemap-index.xml` reenviado a GSC; pedir indexación de `/manual-manager-restaurante`.

## 3. Trampas nuevas de esta sesión (para la memoria)

- **La calibración de páginas era falsa**: la refutación C4 dijo «330 palabras/página»; la plantilla mete **~530** (Food Cost: 50.265 palabras → 95 págs; manual: 41.235 → 77). El gate de páginas se calibra midiendo, nunca estimando.
- **El guion sobrescribe `erratas_permitidas` al final** (`GUIA['gates']['erratas_permitidas'] = _ERRATAS_OK`): añadir palabras a la tupla del diccionario no sirve; se añaden a `_ERRATAS_OK`. Sin lista blanca, **el reparador automático convierte «cantó» en «cuánto» y «ocurrió» en «ocurrido»** en el texto ensamblado (la caché queda intacta).
- **El detector de fechas exime el año solo si hay una cita entre paréntesis a ±250 caracteres**: una fuente entre comillas «…» o una cita larga fuera de la ventana no cuenta. Se resuelve con un paréntesis corto junto al año.
- **`RX_META` («me piden», «se me pide»…) caza texto legítimo de tablas** («Me piden permisos y no sé qué contestar»). Reformular.
- **`postprocess-transversal.py` en modo real pone «Versión 1.1 · agosto 2026» a fuego** (es de la Fase A): NO aplicarlo a productos nacidos después; solo `--dry-run` como comprobación.
- **`bloque_research` trataba una regla legal con fuente pero sin cifra como «HUECO SIN FUENTE»** y prohibía citarla: parcheado (C2) → «REGLA SIN CIFRA».
- **`fase8f` no vale para un producto nuevo cuyos cross-sell ya están en los posts**: borraría los banners del kit de personal/tareas/APPCC. `fase8g` lleva `NUNCA` propio.
- **`COUNTIF(rango,"< 30 días")` se interpreta como comparación** por empezar en `<`: devolvía 0. Los contadores van sobre la columna numérica.
- **`RANK` y `NETWORKDAYS` no evalúan en pycel** (libro sin caché): `SUMPRODUCT(--(rango>propia))+1` y días naturales.
- **`motor.dv_lista` parte las opciones con coma** («Quejas, reclamaciones y reseñas» → 3 opciones): DV contra rango.
- **DataForSEO en el Mac**: credenciales en `~/chefbusiness-astro/.env` (no chefbusiness-ai) y TLS del python3 3.7 arreglado con `Install Certificates.command`.
- **Bash del tool: `cd` a un directorio en el que ya estás falla** con `&&` y el resto de la cadena no corre; rutas absolutas siempre.

## 4. Presupuesto real (tokens de subagentes)
Research 1,47 M + síntesis 0,39 M + refutación 0,52 M + corrector JSON 0,31 M + datos 0,29 M + constructores 0,94 M + refutador xlsx 0,38 M + fixer 0,44 M + guion 0,40 M + capa de producto 0,29 M + blog 0,17 M + email 0,13 M + imágenes 0,32 M + 24 redactores ≈ 4,4 M ≈ **10,5 M**. Segundo producto nuevo en dos días; muy por encima del techo del calendario, con petición expresa de John.

## 5. Seguimientos (no bloquean)
Los del §9 de la SPEC: «60 % cierra» vivo en 3 sitios del repo · gate de FAQ para las 45 landings · `fase8c-enlaces-vivos.py` a landings · 4 piezas de captación del blog (Verifactu 74.000/mes…) · medir canales con GSC · RD del registro horario → changelog 1.1 · Guía Food Cost v1.1 (`FC-PRIME-01/02` atribuyen a Toast el 60-65 %; `SMI-02` sin acotar) · URL de CaixaBankLab caída (`ECONNREFUSED`) · renombrar la hoja «Plan de Cross-Training» (B3 de la refutación xlsx, no aplicado por la regla de no renombrar hojas).

Via: Claude Code
