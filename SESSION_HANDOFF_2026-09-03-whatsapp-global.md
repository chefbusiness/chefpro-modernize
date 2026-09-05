# Handoff — 2026-09-03 · el widget de WhatsApp llegaba a la mitad del sitio (y luego temblaba)

**Estado: TODO CERRADO, desplegado y verificado en producción.** No hay nada a medias.
Commits `d9f79e1` (widget global) y `f080e28` (el temblor del móvil). Cierre documental el
2026-09-05, ya con los 59 commits de la sesión de productos digitales del Mac integrados y el
gate pasado sobre el árbol combinado.

---

## 1. El botón flotante estaba en 655 de las 1.312 páginas

**Reporte de John:** «el widget de WhatsApp está solo en la página de inicio pero no en las
demás páginas en astro, debe estar en todas».

**Alcance real, medido sobre el `dist` y confirmado pidiendo URLs a producción viva: 655 de
1.312.** No era «sólo la home»: lo tenían las 7 portadas de idioma, `/usos`, las pSEO de
ciudades, formación/mentoría/consultoría y las landings de producto. Se quedaban sin él:

- el **blog entero**, ES y EN — el grueso del tráfico de SEO,
- `/precios`, `/contacto`, `/cookies`, el hub de librerías de prompts, los legales,
- y los **44 gates de acceso** de la zona app.

**Causa:** no fallaba nada. Cada página montaba el componente **a mano**, así que la ausencia
no rompía ningún build, no salía en ningún diff y no había forma de que cantara.

**Solución** — `astro-site/src/layouts/BaseLayout.astro`: el botón lo pinta el layout para todo
el sitio, con el `aria-label` del i18n en los 7 idiomas. Retirados los 14 montajes manuales que
quedaban sueltos.

### Lo difícil no era la falta, era el duplicado: hay TRES implementaciones

| Implementación | Dónde | Por qué es distinta |
|---|---|---|
| `components/WhatsAppFloatingButton.astro` | **global, en `BaseLayout`** | `aria-label` del i18n, `bottom-6` |
| `<a>` inline en las plantillas de landing | 46 landings de producto | mensaje **prerellenado** de soporte + `bottom-20` en móvil para no quedar debajo de su barra sticky de compra |
| `WhatsAppProductSupport` (React) | 46 dashboards `-library` | vive en un island `client:only`: **no está en el HTML** |

Esas páginas pasan **`whatsapp={false}`** a `BaseLayout` o saldrían dos botones superpuestos,
con doble animación de pulso y sin un solo aviso en el build. Los `-library` son **generados**:
la plantilla de `scripts/astro-migration/fase5-generate-zona-app.py` ya lo emite — editar el
generador, no los ficheros.

Además, **11 páginas de la SPA que se sirven como islands** (herramientas gratuitas, simulador
de rentabilidad, calculadora de food cost, las de captación…) montaban el botón en React por su
cuenta: retirado de las 11 para que el del layout sea el único.

**Gate nuevo: `python3 scripts/astro-migration/whatsapp-gate.py`.** Exige exactamente 1 botón
flotante por página del `dist` y que las únicas sin él en el HTML sean los dashboards. Probado
contra 4 defectos inyectados a mano: los caza los 4 — uno sólo después de arreglar que leía
`fr.html` como española (con `build.format: 'file'` la portada de cada idioma **no** es
`fr/index.html`, y ese fallo dejaba las 6 homes traducidas sin comprobar).

---

## 2. Y el banner de cookies lo tapaba — el arreglo salió temblando

El banner es `fixed bottom-0` a lo ancho con z-index 100, así que en la primera visita se comía
el botón de la esquina. Pasaba ya en la home, pero al llevar el botón a todo el sitio pasaba a
verse en 1.312 páginas.

**El primer intento salió a producción con un bug.** Lo cazó John en el móvil: *«el widget se
mueve hacia arriba y hacia abajo algunos píxeles cuando haces scroll… algo que no hace el que
está en la página de inicio»*. Dos causas sumadas:

1. **Un `transform` sobre un `position: fixed` lo promociona a capa compuesta** y el navegador
   móvil deja de pintarlo con el scroll asíncrono: se queda a la zaga del viewport.
2. **Estaba aplicado siempre y con `transition`**, hubiera banner o no, así que cada
   micro-reflow se convertía en una animación de 0,25 s. Lo de la home era la caché de su
   móvil, que aún servía el CSS anterior.

**Solución definitiva** — `CookieConsent.astro` + `global.css`:

- **`margin-bottom`, no `transform`.** En un elemento posicionado, `bottom` se mide al borde
  del **margen**, así que un margen inferior lo sube exactamente eso y respeta el anclaje de
  cada una de las tres variantes. Sin tocar la capa de composición.
- **Acotado a `html.aichef-cookies-abierto`**, clase que el banner pone y quita. Sin banner
  —que es casi siempre— el botón no recibe ni una propiedad: `transform: none`,
  `transition-duration: 0s`, `margin-bottom: 0px`, `will-change: auto`.
- **La altura se MIDE**, no se fija: `--aichef-cookie-h` sale de `offsetHeight` (≈90 px en
  escritorio, ≈190 px en móvil, y cambia con el idioma). El publicador **ignora los cambios de
  menos de 4 px**, que son los que provoca la barra de direcciones del móvil al contraerse.

**Verificado en producción** a 390×844, barriendo scroll de 0 a 2.500 px: una única distancia
al borde (24 px) en todas las muestras, y 12 reflows de ±1 px simulados producen **cero**
movimientos del botón.

> **Regla que queda, y sirve para cualquier flotante:** para apartar un `fixed` de otro
> elemento, **margen antes que `transform`**; y no dejes puesta una propiedad de composición
> cuando la condición que la justifica (aquí, un banner que se ve cinco segundos) ya no se da.

---

## 3. Estado al cerrar (2026-09-05, ya con el trabajo del Mac integrado)

Sincronizado con `origin/main` (59 commits de la sesión de productos digitales), reconstruido y
vuelto a pasar el gate sobre el árbol combinado:

```
1.318 páginas · 1.272 con botón · 46 sin él en el HTML (= los 46 dashboards)
✅ GATE WHATSAPP VERDE: 1 botón flotante por página, sin duplicados
```

**Los productos nuevos de esos dos días entraron bien solos** —Guía Food Cost y Manual
Manager—: sus `-library` traen `whatsapp={false}` porque salen del generador, y sus landings
porque se copiaron de una hermana que ya lo tenía. 46/46 landings y 46/46 dashboards con el
opt-out. Es justo lo que el gate está para vigilar.

Otros gates pasados en la sesión: `fase5-gate-s1-s2.py` (zona app, 767 checks, verde contra un
preview local) y `fase7-vigilancia.py` (salud de producción, verde).

### Lo único que hay que recordar

**Si nace una familia de landing de producto con su PROPIO botón flotante de WhatsApp, su
página tiene que pasar `whatsapp={false}`.** Si se olvida, salen dos superpuestos y el build
sigue verde: lo detecta `whatsapp-gate.py`, y por eso conviene correrlo al tocar el layout, las
plantillas de landing o la zona app.
