# «Cómo Montar una Chocolatería» — decisiones FIRMADAS el 2026-09-12 (John delegó: «decide tú, adelante!»)

Las 18 decisiones que la síntesis (`auditorias/guia-chocolateria-RESEARCH-2026-09-12.md` §15) dejaba para John quedan resueltas con la
recomendación de la síntesis, salvo donde se indica. La SPEC las recoge como decisiones firmadas y NO se reabren al construir.

| # | Decisión | Firmada |
|---|---|---|
| D1 | Alcance | **Bombonería artesana / chocolatería CON OBRADOR** como caso central («La Almendra», ~75 m², obrador + tienda a calle). La chocolatería de taza y churros va como **epígrafe del cap. 01** («qué negocio estás montando») + **columna de escenario** en CAPEX y P&L + párrafo en landing y FAQ. Ni capítulo ni producto aparte |
| D2 | Bean-to-bar | **Dentro como VARIANTE**: columna de CAPEX «tren bean-to-bar» SIN cifras de maquinaria (no hay precio público verificado: la guía da la lista de la compra y las preguntas que hacer) + epígrafe propio en el capítulo de normativa (EUDR como OPERADOR con diligencia debida completa, cadmio del grano) |
| D3 | Cola futura | «Cómo Montar una Churrería-Chocolatería» se ANOTA como candidato en `CALENDARIO-V2-SEMANAL.md` §3; no se hace ahora ni se anuncia |
| D4 | Descripción del hub | La tarjeta real dirá «proveedores de cobertura y cacao»; el libro 9 cubre las dos cosas |
| D5 | EUDR | Fecha de revisión explícita DENTRO de la guía y del libro 8 («verificado a 12-09-2026; comprueba el estado del EUDR antes de comprar cacao»); todo lo movible al anexo. **Fecha para el «operador posterior» (lo que es una chocolatería que compra cobertura): 30-12-2026, SIEMPRE** (el aplazamiento del art. 38.3 a 30-06-2027 sólo alcanza a operadores micro/pequeños); el nº de DDS del proveedor sólo se exige si el proveedor es operador (art. 5.3.a) y hay que registrar a quién se suministra (5.3.b) — refutación A1/A2 |
| D6 | `comingSoon` vacío | **NO se siembra otro producto** (anunciar sin research produjo 3-4 meses de retraso visible con Pastelería y Chocolatería). Se retira la tarjeta y se añade la guarda server-side `{comingSoon.length > 0 && …}` en `ProductosDigitalesHubPage.astro:1448` (la SPA ya la tiene). Si John quiere sembrar algo más adelante, lo decide él |
| D7 | Libros de Excel | **9** (sensibilidad al precio del cacao como libro propio; talleres y regalo corporativo como hojas del plan financiero). Cero salidas que crucen libros (refutación C3): donde haga falta el dato de otro libro, celda verde «cópialo del libro N» con valor por defecto declarado, como en Pastelería D21 |
| D8 | Resend | Borrador para el **24-oct-2026 08:00 UTC** (primer hueco libre: Pastelería 14-oct, kit 19-oct). Programable desde el 24-sep. Los dos anteriores son todavía borradores (refutación B3): se programan en orden |
| D9 | Convenio | Una pasada por el REGCON (Ministerio de Trabajo) dentro de la verificación legal. Si no aparece convenio propio del chocolate: **UNA tabla, la de Madrid, marcada como ejemplo**, más el método para identificar el convenio del lector; sin afirmar que exista uno estatal |
| D10 | Artesanía | Cataluña con articulado (Decreto 85/2024, incluye «chocolates»); el resto como enlace al registro autonómico |
| D11 | Franquicias en el CAPEX | Columna «franquicia vs independiente» con las fichas verificadas, citando marca, portal y fecha, como **orden de magnitud publicado**, nunca como dato auditado (L1 y L4 dan cifras distintas de Valor y Chök: se publican las dos con su fuente o ninguna) |
| D12 | FAQ de consultoría | Las **SEIS** FAQ de `src/data/use-cases-content.*.consultor.ts` con inversiones inventadas (heladería, chocolatería, pastelería, pizzería, cafetería, panadería; 7 idiomas) se corrigen en el mismo commit de la capa de producto (sesión B/C), sustituyendo las cifras por el rango verificado del producto correspondiente o por texto sin cifra |
| D13 | Voz de John | No bloquea. El hueco de evidencia en primera persona (redes bloqueadas) se declara en la SPEC; si John graba los 5-10 minutos, entra en la v1.1 |
| D14 | Ritmo | **DOS sesiones**: hoy A2 + B1 (verificación legal → SPEC → datos → 9 xlsx refutados → guion verificado); la siguiente B2 + C (redactores → documentos → refutación de documentos → capa de producto → Payment Link → gates LIVE → borrador de Resend) |
| D15 | Colaterales | Con el 49: tarjeta del kit de chocolatería («9 checklists» → «9 checklists + 2 bonus») y los dos posts de chocolate con banners de sushi/peruano/asador. `kit-tareas-chef-privado` (anuncia 9, entrega 7+2) → sesión impar |
| D16 | Cripto | Nace con NOWPayments: slug en `CRYPTO_PRODUCTS` (scope builds + functions) |
| D17 | Nombre | H1 y promesa: «Cómo Montar una Chocolatería». Nombre de catálogo, banner y email: **«Cómo Montar una Chocolatería»** también (refutación B2: la hermana inmediata se llama «Cómo Montar una Pastelería» en catálogo; el subtítulo lleva «con obrador»). Slug `guia-chocolateria-obrador` |
| D18 | Retraso | No se menciona «Junio 2026»; tarjeta real con badge «Nuevo» |

**Precio: 65 €**, sin tachado, sin ratings, `testimonials.items: []`. **Presupuesto**: ≈14,7-14,9 M (refutación A4), repartido en las dos sesiones.
