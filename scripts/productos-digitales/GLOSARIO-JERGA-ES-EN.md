# Glosario de jerga hostelera ES → EN (US) — documento vivo

> Nace el 13-oct-2026 (sesión Claude Code) por instrucción de John: «la clave está en dar con cómo se usa o se maneja la
> jerga profesional en el inglés con respecto al español». Lo consulta **todo** trabajo en inglés: productos (F1, SPEC,
> redactores, revisión), landings, hub y blog. Cada producto nuevo añade aquí sus términos (el research de su F1 lleva
> una sección «Jerga profesional» con fuente).

## Reglas

1. **Tres capas a la vez**: (1) producto (nombre, slug, ficheros, pestañas, rótulos) · (2) contenido de los entregables ·
   (3) SEO de la landing (title, H1, meta, H2, FAQ en la redacción del comprador, alt, keywords).
2. **Los nombres comerciales, de producto y de marca ya publicados NO se cambian** (Gastro Pro Prompts, «Kit Pro», AI
   Chef Pro, los nombres de los agentes…). La keyword US va como descriptor: en title y H1, el nombre primero y la
   keyword detrás de los dos puntos. Si un nombre ES da en inglés un **calco** que el profesional US no usa, se
   **propone a John caso a caso** con el dato que lo sostiene; el nombre de un producto EN se decide al nacer.
3. **US por defecto** (el mercado de la tienda EN). Los términos UK solo en las notas UK de los entregables.
4. **El volumen no basta**: confirmar la intención con la SERP (p. ej., «kitchen cleaning checklist» es limpieza
   doméstica). Medir con `scripts/dataforseo.py … --pais 2840 --idioma en`.
5. **Estado** de cada fila: **firme** (lo dijo John o está medido y aplicado) · **propuesto** (pendiente de John) ·
   **por verificar** (uso común del sector, sin medir; verificar antes de usarlo en un nombre o en un title).

## Cocina, sala y oficio

| ES | ✗ Calco que NO se usa | ✓ US | Estado y fuente |
|---|---|---|---|
| cocina creativa | creative kitchen | **creative cuisine**; en alta cocina, **avant-garde cuisine** | firme: John, 13-oct. El agente EN se llama «Avant-garde Cuisine» (`agentes-en.json`) |
| obrador (pastelería, panadería, chocolatería) | workshop | según el oficio: **pastry kitchen** · **production bakery / wholesale bakery** · **chocolatier / chocolate kitchen**; central de varias unidades = **commissary kitchen** | propuesto (auditoría 13-oct) |
| dark kitchen | — | **ghost kitchen** (33.100/mes frente a 1.900) | firme (medido); los nombres de producto publicados siguen como están |
| showcooking | showcooking | **live cooking** / **in-home dining** (chef privado) | propuesto |
| gastrobar | gastrobar | **gastropub** | propuesto |
| hotel completo | full hotel | **full-service hotel** | propuesto |
| asador / horno Josper | Josper grill | **steakhouse** · **charcoal grill** (Josper es una marca) | propuesto |
| tareas recurrentes (kit de tareas) | recurring tasks | **opening, closing & cleaning checklists** · **side work** | propuesto (descriptor aplicado en el hub; el nombre, pendiente de John) |
| escandallo | escandallo / recipe scaling | **recipe costing** · **plate cost**; en bar dry hire, **cost per guest** | firme (Food Cost Kit, mobile bar §9) |
| semáforo (indicador) | traffic light | **color-coded status** / **status flag** | por verificar (auditoría 13-oct, capa 2) |
| materias primas (en el P&L) | raw materials | **food & beverage costs** / **COGS** | por verificar (auditoría 13-oct, capa 2) |
| primer plato / segundo | starter / main (UK) | **appetizer / entrée** | por verificar (auditoría, pestañas del Food Cost) |
| margen bruto % (UK «GP %») | GP % | **food cost %** / **gross margin %** | por verificar |

## Gestión y legal

| ES | ✗ | ✓ US | Estado y fuente |
|---|---|---|---|
| cuadrante de turnos | staff rota (UK) | **employee schedule** · **work schedule** (5.400/mes frente a 10) | firme (PR #126) |
| inventario / recuento | stock take (UK) | **inventory count** · **inventory spreadsheet** · **par sheet** | firme (PR #126) |
| registros APPCC | food safety logs (50/mes) | **temperature logs** · **HACCP plan template** | firme (PR #126) |
| autónomo | freelancer | **sole proprietor** · **single-member LLC** | firme (business plans EN) |
| bartender/camarero freelance | freelance | **W-2 event staff**; 1099 = riesgo de mala clasificación (FLSA, CA AB5) | firme (catering y mobile bar EN) |
| licencia de actividad | activity license | **business license** (ciudad/condado) + **sales tax permit** | firme (mobile bar §9) |
| IVA | VAT | **sales tax** (VAT solo en la nota UK) | firme |
| señal / fianza | — | **deposit** | firme (mobile bar §9) |
| convenio colectivo | collective agreement | no hay equivalente general en US: **FLSA + leyes estatales** | firme (PR #126, testimonios) |
| cuota patronal de Seguridad Social | social security contribution | **payroll taxes** (FICA, FUTA/SUTA) | firme (Staff Kit EN) |

## Bar y eventos (detalle y fuentes: `business-plans-en-5/F1-research-us-delta.md` §9)

coctelería para eventos → **mobile bar** (negocio) · barra móvil (mueble) → **portable bar** · el cliente pone el alcohol
→ **dry hire** («you supply the alcohol»; «BYOB» solo como aclaración) · cóctel de autor → **signature cocktails**
(nunca «author cocktails») · experiencias temáticas → **specialty bars / themed bars** · barra de pago → **cash bar** ·
jefe de barra → **lead bartender** · ayudante → **barback** · certificado del seguro → **COI / additional insured** ·
requisitos de la sala → **venue requirements** · temporada alta de bodas → **peak wedding season**.
