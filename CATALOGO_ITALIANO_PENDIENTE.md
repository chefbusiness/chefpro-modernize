# El catálogo de agentes italiano va 35 agentes por detrás del español

> **Decisión pendiente de John.** Medido el 2026-08-08 contra las plataformas
> **vivas**, con el mismo método en las tres (pares `formid`/`formtitle` del HTML
> del listado público de invitado). No es una deducción del repo — es lo que
> Pickaxe sirve hoy.

## La cifra

| Plataforma | URL del listado público | Agentes |
|---|---|---|
| Español | `app.aichef.pro/invitado` | **89** |
| Inglés | `enapp.aichef.pro/guest` | 80 |
| **Italiano** | `itapp.aichef.pro/ospite` | **54** |

El italiano tiene el **61 %** del catálogo español. La versión que declara es
«AI Chef Pro - Italiano - V1.4».

## Qué falta, por familias

Los **28 recetarios del mundo están completos** en italiano (`Cucina Argentina`,
`Cucina Giapponese`, `Cucina Tedesca`…), igual que en español. El hueco son tres
bloques enteros:

| Bloque | Nº | Estado en italiano |
|---|---|---|
| **Consulenza Gastro Pro** (Chef Consultor Pro, Sommelier Consultor Pro, Pizzero Consultor Pro, Barista, Bartender, Chocolatero, Heladero, Panadero, Pastelero, Consultor Gastronómico) | 10 | **Ninguno existe** |
| **Hotelería** (Buffet Master AI, Hotel Staff Meal Planner, Banquet Event Order AI, F&B Reporting Assistant, In-Room Dining Optimizer, Mini-Bar & Amenities AI, Hotel F&B Cost Controller, Hotel Menu Engineering Pro, Hotel Bar & Lounge Menu AI, Room Service Menu Designer, Outlet Concept Developer, Hotel Pastry & Bakery Pro) | 12 | **Ninguno existe** |
| **Marketing y utilidades** (Gastro Calendar, InstaFlow AI Pro, MenuDish Local SEO, BlogPost SEO Gen+, Keyword Discovery AI+, PinterAI Content Pro, Calcula Pax, Conversor Ing, GastroIMG Gen+, Timlup…) | ~13 | **Ninguno existe** |

## Por qué esto no es cosmético

**1. Ya hay contenido italiano PUBLICADO vendiendo agentes que no existen.**
El sitio tiene 10 páginas vivas bajo `/it/casi-uso/consulenza/` —
`chef-consulente`, `sommelier-consulente`, `pizzaiolo-consulente`,
`barista-consulente`… — cuya premisa entera es el bloque Consulenza Gastro Pro.
Ninguno de esos 10 agentes está en `itapp`. El italiano lee la página, se
registra, entra a la plataforma y no encuentra el agente por el que entró. Es
exactamente el fallo que el `CLAUDE.md` documenta como ya costoso: *«la fuente
autorizada es la PLATAFORMA, no el repo»*.

**2. Los 51 spokes que se están traduciendo citan 7 de los ausentes 411 veces.**

| Agente ausente | Menciones en los 51 spokes |
|---|---|
| Gastro Calendar | 127 |
| InstaFlow AI Pro | 96 |
| MenuDish Local SEO | 73 |
| Calcula Pax | 42 |
| BlogPost SEO Gen+ | 40 |
| Keyword Discovery AI+ | 21 |
| Conversor Ing | 12 |

Comprobado con emparejamiento aproximado contra los 54 nombres italianos: no hay
ni un candidato razonable para ninguno de los 7.

**3. La web italiana promete «55+ strumenti IA» en su `<title>`.** Con 54 en la
plataforma la cifra se sostiene por los pelos, pero el contenido detalla agentes
concretos que no están.

## Las dos salidas

**A. Añadir los agentes que faltan a `itapp`** (trabajo de John en Pickaxe, no de
código). Es lo que hace coherente todo el contenido de golpe, incluido el que ya
está publicado. Prioridad sugerida: primero los **10 de Consulenza**, porque hay
10 páginas vivas vendiéndolos; después los 13 de marketing, que son los que citan
los 51 spokes; los 12 de hotelería al final, salvo que el mercado hotelero
italiano sea objetivo a corto plazo.

**B. Podar del contenido italiano las menciones a lo que no existe.** Son 411
menciones en 51 spokes más las 10 páginas de consulenza enteras. Es destructivo,
deja el italiano por debajo del español, y habría que revertirlo en cuanto se
añadan los agentes.

**Recomendación: A.** La traducción de los 51 spokes se ha hecho **fiel**, sin
inventar nombres italianos ni borrar menciones, precisamente para que la opción A
no exija rehacer nada. Los 21 agentes que **sí** tienen nombre italiano oficial ya
van aplicados como glosario obligatorio (`Gerente de Restaurante Pro` → `Manager
Ristorante Pro`, `Mermas GenCal` → `Sprechi GenCal`, `Casual Restaurants AI+` →
`Ristoranti Casual AI+`, `¿Quién Soy?` → `Chi sono?`…).

## Cómo volver a medirlo

```bash
curl -sL https://itapp.aichef.pro/ospite \
  | grep -oP '"formid"\s*:\s*"[^"]+"\s*,\s*"formtitle"\s*:\s*"\K[^"]+' \
  | sort -u
```

Cambiando el subdominio y la ruta (`app`/`invitado`, `enapp`/`guest`) se obtiene
el catálogo de los otros idiomas. **Es la única fuente autorizada**: ni
`src/lib/linkify-use-case.tsx` ni `src/data/apps.ts` ni el sitemap de la app están
al día.
