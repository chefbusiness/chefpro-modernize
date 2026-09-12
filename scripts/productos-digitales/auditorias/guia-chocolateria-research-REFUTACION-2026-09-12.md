# REFUTACIÓN — «Cómo Montar una Chocolatería»

**Fecha:** 2026-09-12 · **Objeto:** `scripts/productos-digitales/auditorias/guia-chocolateria-RESEARCH-2026-09-12.md` (1.137 líneas) y las seis lentes `L1`…`L6` del mismo directorio.
**Método:** tres lentes en un pase (rigor · negocio · producto). Verificación directa contra **texto consolidado del BOE descargado con `curl` y extraído con PyMuPDF** (RD 1055/2003, RD 1021/2022, RDLeg 1175/1990, Ley 7/2022, Ley 1/2025, RD 1055/2022), contra el **consolidado de EUR-Lex** del EUDR (`CELEX:02023R1115-20251226`, descargado y leído entero), contra el **repositorio** (fichero:línea), contra los **xlsx del catálogo abiertos con openpyxl**, contra **GSC en vivo** y contra **DataForSEO en vivo**. **Se ha intentado TUMBAR la propuesta, no confirmarla.**

**Veredicto: CORREGIR ANTES.** 28 refutaciones: **8 altas · 14 medias · 6 bajas**.

El núcleo aguanta y es el research mejor verificado de los cinco del ciclo: el censo del repo es exacto entrada a entrada, los 8 posts y sus 24 banners son exactos banner a banner, las cinco keywords que recomprobé salen **idénticas al dígito y con su serie de 6 meses**, GSC devuelve **285 impresiones y 6 clics** clavados, y el bloque de **RD 1055/2003 es impecable literal a literal** — incluida la errata de conversión del IAE, que existe. Pero **no se puede firmar la SPEC tal cual**: el matiz del EUDR que el research llama «el más valioso del bloque» da la fecha equivocada justo al lector al que va dirigido el correo de lanzamiento, el argumento de venta del epígrafe 644.5 se publica sin la condición que lo limita y esa condición choca con 3 de los 5 canales que el producto modela, la tabla de presupuesto **no suma y omite el guion** (y sobre ella se decide D14), el kit de 12 € **ya publica** la tabla de vidas útiles y las temperaturas que dos de los cuatro libros «sin molde previo» iban a construir, y tres libros declaran salidas que sólo se obtienen **cruzando datos entre libros**, que es lo que la propia convención prohíbe.

---

## Lo que SÍ he confirmado letra a letra (para que NO se re-verifique)

**Repo — exacto:** `products-catalog.ts` **48** entradas y **la escalera de precios completa de §11.1 es exacta en sus 14 filas** (9×1 · 12×13 · 14×8 · 18×1 · 18,50×1 · 24×1 · 29×2 · 35×3 · 39×1 · 45×4 · 55×3 · **65×8** · 85×1 · 89×1); los 8 de la franja de 65 € son los que dice · `payment-links.ts` **48** · `zona-app.ts` `grep -c productId:` = **49** y la 49.ª es la declaración de tipo, como afirma la verificación 4 · `comingSoon` con **1** entrada y la descripción literal en `ProductosDigitales.tsx:958-960` y `ProductosDigitalesHubPage.astro:973-975` · la SPA **sí** tiene guarda (`:1227`) y el Astro **no** (`:1448`) · badge en `:1080` y `:1143` · `sinonimos-buscador.json` **8 grupos, 4 frases, 7 alias y cero menciones de chocolate/cacao/bombón/templado** · `robots.txt` con `/guia-*-access` y `/guia-*-library` en los **5** bloques (35-36, 53-54, 71-72, 89-90, 107-108) · `_redirects` no tiene ninguna regla que roce el slug (la genérica está acotada a los subdominios) · `documentos.py:692-698` y `verificar_guion.py:207` tal como los cita · tamaños de `documentos.py` (2.246), `motor.py` (2.135), `dump_prompts.py` (62), `check_bloque.py` (32), `solape.py` (82), `gate_libros.py` (269), guion (4.924), SPEC (330), `datos_ejemplo.py` (3.324) · `fase8i` existe y **`fase8j` está libre** · `fase8e-banners-corpus.py` sólo tiene `--lang/--aplicar/--informe/--limite`: **efectivamente sólo inserta** · `CRYPTO_PRODUCTS` es env var leída por `netlify/functions/crypto-checkout.ts:87` **y** por `GuiaLandingPage.astro:22` → los **dos scopes** que pide son correctos.

**Producción:** `curl https://aichef.pro/guia-chocolateria-obrador` = **404** (slug libre) · `/guia-pasteleria-obrador` = **200**, con «103 páginas», «37 páginas» y `buy.stripe.com/7sY00c5Sk64e1MPejH6oo1r` dentro del HTML · `git rev-list --count origin/main..main` = **0**.

**Kits, medidos por mí con openpyxl:** `kit-tareas-chocolateria` **11 ficheros (9+2)**, **139 fórmulas**, **95 en `09-apertura-cierre-caja.xlsx`** y 44 en los otros diez — exacto · perfiles literales **Chocolatero · Dependiente · Encargado** · `06-eventos-temporada` = Navidad, San Valentín, Pascua · `BONUS-02` marca **agosto «Baja»** · `kit-tareas-chef-privado` entrega **7 + 2** y el hub anuncia «9 checklists» (`…HubPage.astro:844`) — la verificación 8 es correcta · `kit-escandallos` **13 ficheros**.

**Blog — exacto post a post:** los **8** posts existen, los **8** tienen exactamente **3 banners**, los 24 banners coinciden uno a uno con la tabla de §13.2, y las 8 cifras de menciones coinciden **al dígito**: 382 · 364 · 88 · **31** (el coulant, hallazgo propio) · 127 · 18 · 31 · 27.

**GSC en vivo (`sc-domain:aichef.pro`, 2026-06-14 → 2026-09-12, `page contains chocolat`):** **38 URLs, 285 impresiones, 6 clics**; en el dominio vivo **159 impresiones y 3 clics**; `/blog/chocolateria-artesanal-e-ia…` **3 / 30 / 10,00 % / 4,9**; `/kit-tareas-chocolateria` **0 / 13 / 6,0**; `/usos/consultoria/chocolatero-consultor` **0 / 15 / 4,3**. **Las cuatro cifras y los dos totales son exactos.** La verificación 5 queda cerrada.

**DataForSEO en vivo (España, hoy), con su serie de 6 meses:** `chocolate a la taza` **4.400** `1600·1000·1000·1900·2400·3600` · `eudr` **1.900** `480·880·1000·1300·1000·880` · `bomboneria` **880** `590·590·590·880·880·1000` (+69 %, exacto) · `chocolateria artesanal` **390** `260·170·170·260·320·390` · `montar una chocolateria` **10** `10·10·0·10·0·10`. **Los cinco valores y las cinco series son idénticos a los publicados.**

**BOE, leído por mí en consolidado:**
- **RD 1055/2003** (`BOE-A-2003-15599`): «**Última modificación: sin modificaciones**» ✔ · ap. **1.6** (35/18/14 y cobertura 35/31) · **1.10** (exterior ≥25 % del peso total; no aplica a interior de panadería, pastelería, galletería, bollería o helado) · **1.11** (35/18/14 y ≤8 % de harina) · **1.12** (30/18/12 y ≤18 %) · **1.13** («producto del tamaño de un bocado… al menos, el 25 por ciento del peso total») · **2.1** (≤5 %, sin reducir mínimos) · **3.1** (grasa animal no láctea prohibida · harinas sólo en 1.11/1.12 · ≤40 % de materias añadidas) · **3.2** (aromas que no simulen) · **4** (las **dos bases** de cálculo, exactamente como las describe `CHN-10`) · **6.b)** (negrita, mismo tamaño, mismo campo visual) · **6.c)** (surtidos, lista única) · **6.d)** (la lista es **1.4, 1.5, 1.6, 1.7, 1.8, 1.11 y 1.12** — sin blanco, sin relleno, sin bombón) · **6.e)** («para su consumo cocido») · **6.g)** (43/26 · 30/18/4,5 · 16). **Todo exacto.**
- **RD 1021/2022** (`BOE-A-2022-21681`): art. **3** completo (tres condiciones acumulativas; 25 % **o** 500 kg; restringido = no suministrar a inscritos en RGSEAA; 3.5 declaración responsable y registro; 3.6 central y sucursales) · art. **4.1** (**11 filas y ninguna nombra el chocolate**; fila 9 «Productos de pastelería **rellenos**… ≤4 °C») · **4.2** y **4.3** · art. **13** completo (13.5.a-e con sus tres salvedades autonómicas, 13.8 con **cinco** letras, 13.9 los 100 kg). **Todo exacto.**
- **RDLeg 1175/1990** (`BOE-A-1990-23930`, «Última modificación: **21 de marzo de 2026**»): **644.5** con su nota literal, **644.6** («faculta para la elaboración de los productos de churrería»), **644.1** (el único con degustación) y **grupo 676**. Y **la errata de conversión existe**: en el 644.5, «16.560 pesetas (74,65 euros)» cuando en el resto equivale a 99,53 €. `CHN-72` es correcto y su aviso de no reproducir cuotas, también.
- **Ley 7/2022** (`BOE-A-2022-5809`, últ. mod. **02-04-2025**): art. **73.d)** («no están diseñados para ser entregados conjuntamente con dichas mercancías» → los moldes fuera), **75.f)** (importación **o** adquisición intracomunitaria, ≤**5 kg** de plástico no reciclado **en un mes**), **78** (0,45 €/kg) y **82.3** (Registro territorial previo). `CHN-62` exacto.
- **RD 1055/2022** (`BOE-A-2022-22690`): art. **9.3** («Todos los establecimientos de alimentación que vendan **a granel**… **deberán aceptar** el uso de recipientes reutilizables») y **9.4.a).1º** («Desde el 1 de enero de 2027: al menos una referencia de bebida en envase reutilizable, si el establecimiento tiene una superficie comercial **inferior a 120 m2**»). `CHN-63` exacto.

**EUR-Lex, consolidado del EUDR a 26-12-2025, leído entero por mí:** art. **2.15** («excluidos los operadores posteriores»), **2.15 bis** («establecida en un país clasificado como de riesgo bajo»), **2.15 ter**, **2.17**, **4 bis**, **5.1 a 5.7**, **37** y **38**. `CHN-21` (30-dic-2026 y la lista «3 a 13, 16 a 24, 26, 31 y 32»), `CHN-22` (**31 de diciembre de 2024**, no 2020), `CHN-23`, `CHN-25` y `CHN-27` son **literalmente correctos**, y `CHN-22` **corrige bien** el error de L2 (`L2:197-200`, que concluía «una chocolatería que abra en 2026 → 30 de junio de 2027»). **No existe consolidado posterior**, y el «paquete de simplificación de mayo de 2026» del que hablan las consultoras **no reabrió el articulado**: el texto vigente es el que el research cita.

---

## A — RIGOR

### A1 · ALTA — El «matiz más valioso del bloque» da la fecha EQUIVOCADA justo al lector del correo de lanzamiento: el art. 38.3 sólo alcanza a los «operadores», y el art. 2.15 excluye de esa palabra a los «operadores posteriores»

**Afirmación literal (`CHN-21/22`, §2.4, FAQ 6, cap. 11, pieza de blog nº 1):** «Art. 38.3: el **30-jun-2027** exige **dos** condiciones acumulativas — ser persona física, microempresa o pequeña empresa **Y** “que estuviesen establecidos como tales a 31 de diciembre de 2024”» · FAQ 6: «**el aplazamiento a junio de 2027 exige haber estado establecido a 31 de diciembre de 2024** — si abres ahora, **tu fecha es el 30 de diciembre de 2026**».

**Problema.** Las dos condiciones son ciertas, pero **falta la primera y decisiva**. Texto literal del art. 38.3, leído en el consolidado:

> «… a los **operadores**, sean personas físicas, microempresas o pequeñas empresas … que estuviesen establecidos como tales a 31 de diciembre de 2024, les serán aplicables los artículos a que se refiere el apartado 2 … a partir del 30 de junio de 2027.»

Y el art. 2.15 —**modificado por el MISMO Reglamento 2025/2650 que reescribió el art. 38**— define:

> «15) “**operador**”, toda persona física o jurídica que … introduce los productos pertinentes en el mercado o los exporta, **excluidos los operadores posteriores**».

El propio research (`CHN-23/24`, FAQ 6, cap. 11) sostiene que el lector **no es operador, es operador posterior**. Literalmente, entonces, **la derogación del 38.3 no le alcanza nunca**: su fecha es la general del 38.2, el **30 de diciembre de 2026**, tenga la antigüedad que tenga.

**Y ahí está el daño, que no es teórico.** Tal como está redactado, el producto le dice a una chocolatería o pastelería **ya establecida antes del 31-12-2024** que su fecha es junio de 2027. Esa lectora es **P5**, «la pastelería/cafetería que AÑADE obrador de chocolate», que el §0.2 y el §6.3 identifican como **«el mejor objetivo del correo de lanzamiento»** porque ya compró la Guía de Pastelería. A esa compradora se le estaría regalando **siete meses de retraso sobre una obligación con sanción**.

**Evidencia:** `CELEX:02023R1115-20251226`, arts. 2.15 y 38.3 (los dos marcados ▼M2, es decir, del mismo acto modificativo) · `guia-chocolateria-RESEARCH-2026-09-12.md` §2.1 `CHN-22` y `CHN-23/24`, §14 FAQ 6 · `guia-chocolateria-research-L3-normativa.md:211` y `:212`, donde las dos entradas están **una debajo de la otra y se contradicen sin que la lente lo note**.

**Gravedad: alta.** Es la afirmación que el research marca como «el más valioso del bloque», está en la FAQ pública, en el capítulo 11, en la hoja «EUDR: ¿te aplica?» del libro 8 y en la pieza de blog nº 1.

**Fix.** Reescribir `CHN-22` con **tres** condiciones y una puerta de entrada: «*el aplazamiento del art. 38.3 es para **operadores**; si compras cobertura ya comercializada en la UE eres **operador posterior** (art. 2.15) y **no entras en esa derogación**: tu fecha es el 30 de diciembre de 2026, hayas abierto cuando hayas abierto.*» Reservar el matiz del 31-12-2024 para el caso **bean-to-bar** (`CHN-25`), que sí es operador y para quien sí decide. Y marcar la interacción 2.15 ↔ 38.3 como **punto que el verificador legal debe firmar** antes del cap. 11: si se opta por la lectura contraria (que el legislador quiso incluir a los operadores posteriores), hay que decir que es **interpretación**, no nivel A.

---

### A2 · ALTA — «Guarda el número de referencia de la DDS de tu proveedor» se publica como obligación universal, y el art. 5.3.a) lo exige SÓLO si el proveedor es un operador — el semáforo del libro 9 suspendería a proveedores que cumplen

**Afirmación literal (`CHN-23/24`, §4.6, FAQ 6, libro 9):** «le obliga el **art. 5** — guardar datos del proveedor **y el número de referencia de su DDS**, **cinco años**…» · §4.6: «*la pregunta que el lector tiene que saber hacer …: «¿me das el **número de referencia de tu declaración de diligencia debida** (EUDR)?»*» · libro 9, columna: «**¿te declara origen y número de DDS (EUDR)?**» con **«semáforo de documentación del proveedor»**.

**Problema.** Texto literal del art. 5.3, leído por mí:

> «a) nombre … de los operadores, operadores posteriores o comerciantes que les hayan suministrado los productos pertinentes, así como, **únicamente en el caso de que su proveedor sea un operador**, los números de referencia de las declaraciones de diligencia debida o los identificadores de declaración correspondientes a dichos productos;
> b) nombre … **de los operadores posteriores o de los comerciantes a los que hayan suministrado** los productos pertinentes.»

Dos cosas se pierden por el camino y las dos bajan al entregable:

1. **La condición.** Una chocolatería pequeña casi nunca compra al operador: compra a un **distribuidor**, que en la cadena del EUDR es *comerciante* u *operador posterior* (art. 2.17 y 2.15 ter). Ese distribuidor **no tiene número de DDS que dar** y **no está obligado a darlo** (el art. 4.7 sólo obliga a comunicarlo a los **operadores**). Un semáforo que lo exija a todos pondría en rojo a proveedores perfectamente conformes, y le haría discutir al comprador con su distribuidor por un papel que la norma no le pide.
2. **El apartado b).** El art. 5.3 obliga también a registrar **a quién suministras** — que es precisamente el canal **B2B hostelería** y el **regalo corporativo** que el libro 7 modela. El libro 9, tal como está especificado, sólo tiene columnas de **proveedor**.

**Y no es un fallo de lectura de la lente: `L3` lo tiene literal.** `guia-chocolateria-research-L3-normativa.md:213` transcribe «**únicamente en el caso de que su proveedor sea un operador**» y el apartado b) entero. **La pérdida ocurre en la síntesis**, que es el documento que alimenta la SPEC y el guion.

**Gravedad: alta.** Va a la FAQ pública, a una columna con semáforo de un xlsx de pago y al argumento de venta «las dos preguntas que separan a quien compra de quien sabe lo que compra» (§4.6 y cap. 13).

**Fix.** (1) Reponer la condición en `CHN-24`, en la FAQ 6 y en §4.6: la pregunta correcta es «**¿mi proveedor es operador o comerciante?**», y sólo en el primer caso se pide el número. (2) Rehacer la hoja de proveedores como **árbol**: tipo de proveedor → si operador, número de DDS obligatorio; si comerciante u operador posterior, basta con sus datos identificativos. (3) Añadir la **segunda tabla del art. 5.3.b)** (clientes B2B y corporativos a los que suministras), que hoy no existe en ningún libro.

---

### A3 · ALTA — El argumento de venta del epígrafe 644.5 se publica SIN la condición que lo limita, y esa condición choca con 3 de los 5 canales que el producto modela

**Afirmación literal (§2.4, uno de los cuatro argumentos que van a landing, FAQ y email):** ««**Hay un epígrafe de IAE que te deja fabricar bombones sin darte de alta como industria**» (`CHN-72`)». Y `CHN-72`: «**644.5** … Nota: “faculta para: **La fabricación de bombones y caramelos en el propio establecimiento, siempre que su comercialización se realice en las propias dependencias de venta**”. **No hace falta el 421.1**, que es el **industrial**».

**Problema.** La nota es exacta —la he leído— pero **la mitad que condiciona desaparece en cuanto el argumento sale de la tabla**. Y esa mitad es incompatible con el modelo de negocio que el propio research construye:

| Canal del libro 7 (§8.2, §9.2, cap. 19) | ¿«en las propias dependencias de venta»? |
|---|---|
| Mostrador | sí |
| Talleres y catas | sí |
| **Online con envío a toda España** | **no** |
| **B2B a hostelería** | **no** |
| **Regalo corporativo** | **no** |

El research declara explícitamente que «**Los canales son 5, no 4**» y que ésa es una de las diferencias propias frente a Pastelería. Tres de esos cinco caen fuera de la facultad del 644.5 tal como está escrita. Un lector que monte el modelo completo de la guía y se dé de alta sólo en el 644.5 **puede necesitar una segunda alta** (mayorista o industrial), y la guía le ha dicho lo contrario en la landing.

**Evidencia:** `BOE-A-1990-23930` consolidado, epígrafe 644.5, nota · `guia-chocolateria-RESEARCH-2026-09-12.md` §2.4, §8.2, §9.2 (libro 7), §10 cap. 19 · `L3:331`, que **sí** recoge la condición completa.

**Gravedad: alta.** Es uno de los cuatro argumentos de venta que el §2.4 autoriza para landing y email, y contradice el capítulo 19 del mismo producto.

**Fix.** Reformular el argumento con su límite dentro: «**Puedes fabricar bombones sin darte de alta como industria mientras los vendas en tu propia tienda; en el momento en que sirves a otros comercios, a empresas o envías fuera, esto cambia — y la guía te dice exactamente cuándo y a qué.**» Añadir al capítulo 19 y a la hoja «Checklist Legal» una fila que cruce **canal → epígrafe de IAE** y marcarla como verificación pendiente para el verificador legal (junto con la Regla 4.ª de la Instrucción, que este research no ha mirado).

---

### A4 · ALTA — La tabla de presupuesto no suma, y el renglón que falta es el guion: sobre ella se decide D14 (el techo del 15 % de la cuota de John)

**Afirmación literal (§15.4):** columna Pastelería **2,06 · 0,88 · 2,79 · 4,90 · 0,71 · ≈1,50**, **TOTAL ≈14,1 M**; columna Chocolatería **2,1 · 1,10 · 3,15 · 5,0-5,2 · 0,80 · 1,25**, **TOTAL ≈13,4-14,6 M**. Y la conclusión: «**Mi estimación queda por debajo de la de L6 (14,8 M) por dos razones medidas, no por optimismo**».

**Problema.** Ninguna de las dos columnas suma su total:

| | Suma real de la columna | Total publicado | Desfase |
|---|---|---|---|
| Pastelería (real) | **12,84 M** | ≈14,1 M | **−1,26 M** |
| Chocolatería (estimado) | **13,40 – 13,60 M** | 13,4 – **14,6** M | el techo sobra **1,0 M** |

Y la causa del primer desfase es identificable: la fila **A2** se titula «verificación legal **+ SPEC + guion**» pero su cifra de Pastelería, **0,88 M**, es exactamente `0,5 (verificación legal) + 0,38 (SPEC)`. **El guion —0,6 M en el desglose real— no está en la columna.** El `+25 %` que produce el 1,10 M de Chocolatería se aplica, por tanto, sobre una base a la que le falta el renglón más largo del bloque (4.924 líneas en Pastelería).

Se sigue una de estas dos cosas, y las dos rompen la conclusión:
- Si la columna de Pastelería es la buena, **el «≈14,1 M» de referencia es falso** y la comparación «cuesta parecido» no se sostiene.
- Si el «≈14,1 M» es el bueno (y `CALENDARIO-V2-SEMANAL.md:144` dice «Coste ≈ **14 M** tokens de subagentes»), entonces **a la estimación de Chocolatería le falta el mismo renglón**, y su total real es **≈14,7-14,9 M**: por encima de Pastelería y **por encima de la estimación de L6 (14,8 M)** que el research presume haber batido.

**Evidencia:** `guia-chocolateria-RESEARCH-2026-09-12.md` §15.4 (tabla y párrafo de aviso) · `scripts/productos-digitales/CALENDARIO-V2-SEMANAL.md:144`.

**Gravedad: alta.** Es la cifra sobre la que John decide **D14** (partir o no en dos sesiones) bajo una regla de presupuesto explícita (~15 % de la cuota semanal). Un producto presentado como «13,4» que sale «14,9» se come la siguiente sesión.

**Fix.** Rehacer la tabla con el guion como **fila propia** (Pastelería 0,60 M · Chocolatería ~0,75 M por las 315+ referencias de celda de tres frentes normativos), recomputar los dos totales **desde la columna**, y publicar la comparación honesta: **≈14,0-14,4 M frente a los ≈13,4 M reales de Pastelería**. Y añadir al gate de la SPEC una comprobación trivial: **que la fila TOTAL sea la suma de su columna**.

---

### A5 · MEDIA — `CHN-44` está clasificada nivel **A** (literal, citable) y su conclusión operativa es una **interpretación**; la letra e) del art. 13.8 no baja al guion

**Afirmación literal (`CHN-44`, nivel **A**):** «Hacer bombones en casa para vender **NO entra en la lista estatal**. El art. 13.8 permite «Productos de **panadería y repostería** estables a temperatura ambiente», y **ni el bombón ni la tableta son repostería**. **Prueba:** el decreto catalán de artesanía tuvo que escribir “confitería, pastelería, bollería y repostería, **incluidos turrones y chocolates**”».

**Problema.** He leído el art. 13 entero. Lo **literal** —y por tanto lo que puede ir a nivel A— es la lista de cinco letras. Lo demás son dos saltos:

1. «**un bombón no es repostería**» no está en ninguna norma: es una interpretación semántica de una palabra que el RD no define. La «prueba» del Decreto 85/2024 no prueba nada sobre el RD 1021/2022: regula **artesanía alimentaria**, otro registro, otra competencia y otro fin; que un decreto autonómico de artesanía enumere para su propio repertorio no dice qué entiende por «repostería» una norma sanitaria estatal.
2. **La letra e) desaparece del nivel A.** El art. 13.8.e) dice «Otros alimentos que **las autoridades competentes de las comunidades autónomas permitan en sus territorios**». El research **sí** la maneja bien en §15.2 y en la FAQ 3 («no entra en el régimen estatal **salvo que tu comunidad lo haya añadido**»), pero la entrada `CHN-*` es lo que leen el verificador legal y los 46 redactores, y ahí la conclusión va sin salvedad y con sello de literalidad.

Es exactamente la **A3 de la refutación de Pastelería** reaparecida un escalón más arriba: allí la afirmación categórica llegó a la FAQ; aquí la FAQ está bien y lo que está mal es la ficha que la alimenta.

**Evidencia:** `BOE-A-2022-21681` consolidado, art. 13.8.a)-e) · `RESEARCH` §2.1 `CHN-44` (nivel A) frente a §15.2 y §14 FAQ 3.

**Fix.** Bajar `CHN-44` a **dos entradas**: `CHN-44` **nivel A** = las cinco letras del 13.8 transcritas, incluida la e) · `CHN-44-int` **interpretación declarada** = «por defecto el chocolate no encaja en la letra b); compruébalo en tu CCAA». Y que la hoja «Ruta Doméstica» del libro 8 lleve la **celda verde «¿tu CCAA ha ampliado la lista por la letra e)?»** con enlace al registro autonómico, como ya se ordenó para Pastelería.

---

### A6 · MEDIA — «Fino», «superior» y «extra» van entrecomillados como si el RD 1055/2003 los nombrara, y no aparecen en la norma

**Afirmación literal (§1.2, concepto nº 5):** ««**Fino**», «**superior**», «**extra**» sólo sobre «chocolate», «chocolate con leche» y «cobertura», y sólo con ≥43 %/≥26 %…».

**Problema.** El ap. 6.g) dice, literalmente: «podrán completarse mediante **menciones o calificativos referentes a criterios de calidad**». **No enumera ninguna palabra.** Los tres términos entrecomillados son un ejemplo razonable, pero están en la columna «**Qué es exactamente**» de la tabla que fija los conceptos que el capítulo 10 va a enseñar, y con comillas. Es incoherente con el rigor del propio documento, que dos filas más arriba (`CHN-53`) se toma el trabajo de demostrar que «artesano» y «casero» **no aparecen** en el texto tras una búsqueda exhaustiva. Detalle menor de la misma fila: la norma dice «**cobertura de chocolate**», no «cobertura».

**Evidencia:** `BOE-A-2003-15599` consolidado, ap. 6.g) · `RESEARCH` §1.2 fila 5.

**Fix.** Reescribir: «*La norma no da una lista de palabras: autoriza “menciones o calificativos referentes a criterios de calidad” —del tipo “fino”, “superior”, “extra”— **sólo** sobre las tres denominaciones y **sólo** por encima de los umbrales del ap. 6.g).*» Y entrecomillar únicamente lo que está en el BOE.

---

### A7 · MEDIA — Dos de los ocho sumandos del CAPEX verificado no son precios verificados: 30 €/molde es una constante sin fuente y «desde 570 €» es un suelo usado como precio

**Afirmación literal (§4.4):** «Selmi One 8.500 + puesta en marcha 1.045 + enrobadora R200 6.800 + placa dosificadora 1.495 + **12 moldes (12 × 30 €) 360** + baño maría 22 L 2.650 + **mantenedor 570** + vitrina Docriluc 2.684,99 = **24.104,99 €**». Y antes: «Es la suma de las líneas con **precio verificado**, y nada más».

**Problema.** La aritmética es impecable (la he recomputado: 24.104,99 € y 5.740,29 €; el «factor 4,3 en máquina» también sale). Pero dos sumandos no cumplen la regla de la casa:

- **Los moldes.** El único dato medido es `CHS-45a`: Chocolate World, **24,20-42,83 €/ud**. El **30 €** no aparece en ninguna fuente del research: es un punto elegido dentro del rango. Con los extremos publicados, esa línea vale entre **290,40 € y 513,96 €**, y el total del escenario B se mueve un **±3 %**.
- **El mantenedor.** `CHS-41i` dice «**desde** 570 €». Un precio «desde» es un suelo comercial, no el precio de la unidad que se va a comprar.

Y los dos entran en la cifra que **la FAQ 4 publica al cliente** («de ~5.700 € … a ~24.100 €») y en la **decisión nº 2 del bonus** («factor 4 en el total del núcleo»).

**Evidencia:** `RESEARCH` §4.3 `CHS-45a` y `CHS-41i`, §4.4, §9.3 decisión 2, §14 FAQ 4.

**Fix.** Publicar las dos líneas como **rango** (moldes 290-514 €; mantenedor «desde 570 €, presupuestar») y el total como **rango**, no como número único. En el xlsx, las dos van en **celda verde con su rango como nota**, no como valor por defecto cerrado.

---

### A8 · MEDIA — El «contraste que es un argumento de venta en sí mismo» compara una BASE MIXTA declarada contra una base no declarada, que es justo lo que la lista negra `N-7` prohíbe

**Afirmación literal (§4.4):** «🔴 **El contraste que es un argumento de venta en sí mismo:** la única fuente publicada con un número completo sitúa la apertura en **20.000-30.000 €**, y el núcleo de máquina profesional verificado aquí ya son **24.105 €**. **Las dos cifras sólo son compatibles si…**». Y en `N-7`: «Los precios de **Utilcentre interpretados como “con IVA”** y **el total de 24.104,99 € como cifra fiscal** … **El total es BASE MIXTA y así va etiquetado**».

**Problema.** El research aprendió la lección de la A1 de Pastelería a medias: **etiqueta** la base mixta (bien) y luego **la usa igual** para un contraste que pretende ser aritmético. De los ocho sumandos, uno es **sin IVA declarado** (Docriluc, «sin impuestos»), seis son **base no declarada** y uno (los 1.045 € de Utilcentre) lleva un indicio (`/Neto`) que el propio research dice que no puede afirmarse. Al otro lado, el rango de **plandenegocio.es no declara base ninguna**. La frase «las dos cifras sólo son compatibles si…» presenta como demostración una comparación que, en el peor caso, tiene un 21 % de indeterminación en cada lado.

Ese contraste no se queda en el research: es el contenido obligatorio del **capítulo 04** («el rango de “20.000-30.000 €” esconde dos negocios distintos»), la **FAQ 4** y una de las **12 decisiones** del bonus.

**Evidencia:** `RESEARCH` §4.3 (columna «Base IVA»: seis «NO declarada»), §4.4, §10 cap. 04, §14 FAQ 4, §15.1 `N-7`.

**Fix.** Mantener el hallazgo cualitativo —que es bueno y es cierto: **el rango publicado mezcla dos escenarios de máquina distintos**— y **quitarle la aritmética**. Formulación honesta: «*el arranque mínimo con atemperadora de sobremesa y el profesional con continua se diferencian en un factor 4; cualquier cifra publicada que no diga cuál de los dos está describiendo no sirve.*» Y llevar la columna «**¿lleva IVA?**» del libro 2 también a la tabla del research y al capítulo, no sólo al xlsx.

---

### A9 · MEDIA — `CHN-64` (desperdicio alimentario) afirma obligaciones que el artículo que cita elimina: el art. 6.6 de la Ley 1/2025 excluye a la microempresa de TODOS los apartados anteriores, incluidos el 6.2, el 6.3 y el 6.5

**Afirmación literal (`CHN-64`, nivel **A**):** «**Desperdicio: una chocolatería es microempresa y queda fuera del art. 6.** Le siguen obligando el **6.2**, el **6.3** (nula de pleno derecho la cláusula que prohíba donar) y el **6.5**». Idéntico en `L3:307`, cuya «Redacción SEGURA» —la que va al producto— dice: «*Lo que le sigue obligando es no estropear a propósito lo que sobra y saber que ninguna cláusula de contrato puede prohibirte donar*».

**Problema.** Texto literal del art. 6.6, leído por mí en el consolidado:

> «6. **Las microempresas quedan excluidas de las obligaciones a las que se refieren los apartados anteriores del presente artículo.**»

«Los apartados anteriores» son **6.1, 6.2, 6.3, 6.4 y 6.5**. La entrada es autocontradictoria en su propia frase («queda fuera del art. 6 … le siguen obligando el 6.2 … y el 6.5») y contradicha por la letra de la norma. Además, el 6.4.c) ya exceptúa por sí solo a los establecimientos de **≤1.300 m²**: una chocolatería de 75 m² está doblemente fuera.

(Matiz que sí hay que conservar: la **nulidad** del 6.3 opera sobre la cláusula contractual, no como obligación del agente, así que la frase «ninguna cláusula puede prohibirte donar» sigue siendo verdadera — pero no porque el 6.3 «le siga obligando».)

**Evidencia:** `BOE-A-2025-6597` consolidado, art. 6.4.c) y 6.6 · `RESEARCH` §2.1 `CHN-64` · `L3:307`.

**Gravedad: media.** No hay sanción por cumplir de más, pero es una **obligación falsa puesta al lector** en un producto que se vende por citar la norma con su artículo, y baja a la decisión nº 12 del bonus («Qué haces con el chocolate que no se vende»).

**Fix.** Reescribir: «*Si eres microempresa, el art. 6.6 te deja fuera de las obligaciones del art. 6 —plan, convenios de donación, jerarquía— y el 6.4.c) exceptúa además a todo establecimiento de ≤1.300 m². Lo que sigue en pie no es una obligación tuya: es que **cualquier cláusula contractual que prohíba donar es nula de pleno derecho** (art. 6.3).*» Y que el verificador legal firme la entrada **contra el texto**, no contra L3.

---

### A10 · MEDIA — `eudr` = 1.900: el «creció ×2 en el semestre» es ×1,83, la serie lleva tres meses BAJANDO, y la media publicada no aparece en ninguno de los seis meses

**Afirmación literal (§0 tabla, §13.4 pieza nº 1):** «**`eudr` 1.900** ✅ (serie `480·880·1.000·1.300·1.000·880`, **creció ×2 en el semestre**)» · «🟢 **La única keyword de 4 cifras del nicho con intención profesional**… Riesgo: **Bajo**».

**Problema.** He remedido la serie hoy y es idéntica. Pero la lectura no:

- **×2 es ×1,83** (880/480), y se mide del mes **más bajo** a un mes que está **un 32 % por debajo del pico**.
- **La tendencia de los tres últimos meses es descendente**: 1.300 → 1.000 → 880. Llamar a eso «creciendo ×2» describe lo contrario de lo que hace la curva. El pico coincide con la publicación del Rgto. 2025/2650 (23-dic-2025): es **demanda de noticia**, que decae.
- **Ninguno de los seis meses llega a 1.900.** La media anual la sostienen meses fuera de la ventana. Presentarla como «keyword de 4 cifras» del nicho es el mismo tipo de lectura que el research denuncia en `CHS-40` y en la anti-recomendación de `mona de pascua` («la media la hace un pico que ni aparece»).
- Y un cuarto punto que no se dice: **`eudr` no es demanda de chocolate**. Es un acrónimo que buscan responsables de compliance de madera, soja, palma, ganado, café y caucho. El research afirma «Ningún actor gastronómico español lo ha escrito para chocolateros» —cierto— pero de ahí no se sigue que las 1.900 búsquedas sean de chocolateros.

**Evidencia:** `/usr/bin/python3 scripts/dataforseo.py vol "eudr"` (2026-09-12): `1900 MEDIUM 480, 880, 1000, 1300, 1000, 880` · `RESEARCH` §0 y §13.4 · `L2:184`, `:200` y `:503`.

**Fix.** Publicar la serie con su lectura real: «*pico de 1.300 en el mes de la reforma y descenso desde entonces; es demanda de actualidad, no estructural*». Y **antes de escribir la pieza, correr `dataforseo.py serp "eudr"`**: es la única de las cuatro recomendaciones cuya SERP **no se ha abierto** (las 13 SERP clasificadas por el filtro v2 de `L2:228` no la incluyen), y la regla de `CLAUDE.md` es explícita: *«Correr siempre `serp` antes de decidir el enfoque, no sólo `vol`»*. Con una intención de compliance industrial, el riesgo no es «Bajo».

---

### A11 · BAJA — Los 8 `gen_*.py` de Pastelería suman 13.196 líneas, no 12.196

**Afirmación literal (verificación 17 y §8.4):** «los 8 `gen_*.py` de pastelería suman **12.196 líneas**» · «media medida en pastelería: **1.142-2.720** líneas por libro, **12.196 en los ocho**».

**Problema.** Medido: 1.515 + 1.453 + 1.610 + 1.589 + 1.710 + 1.142 + 2.720 + 1.457 = **13.196**. El rango (1.142-2.720) es exacto; el total lleva **1.000 líneas de menos**. Va marcada con ✅ como medición propia y es la base del dimensionado de los 9 constructores del §8.4.

**Evidencia:** `wc -l scripts/productos-digitales/guia-pasteleria/gen_*.py`.

**Fix.** Corregir a 13.196 y reestimar el bloque B1 con la media real (**1.650 líneas/libro**, no 1.525).

---

### A12 · BAJA — `N-2` cita la línea del `productIds`, no la de la cifra que prohíbe

**Afirmación literal (`N-2`):** «está publicada en `use-cases-content.es.consultor.ts:386`».

**Problema.** `:386` es la línea `productIds: [...]`. La FAQ con «80.000 € y 250.000 €» está en **`:393`**. (La verificación 6 sí cita bien el bloque, `:348`.) Importa porque `N-2` es la entrada que un agente `sonnet` va a usar para aplicar **D12**, y apuntar a la línea equivocada en siete ficheros es una pasada perdida.

**Fix.** `use-cases-content.es.consultor.ts:393` (ES) y la línea equivalente en los otros seis.

---

## B — NEGOCIO

### B1 · ALTA — D12 arregla 1 de 6: el mismo fichero publica SEIS inversiones de apertura, y las de pastelería y panadería ya contradicen a dos productos de 65 € que están vendiéndose

**Afirmación literal (verificación 6, `N-2`, riesgo 2, D12):** «**HALLAZGO NUEVO, no está en ninguna lente**… `/usos/consultoria/chocolatero-consultor` publica «una chocolatería artesanal premium … **entre 80.000 € y 250.000 €**» … **Si la guía sale con el CAPEX verificado, el mismo dominio publicará dos inversiones incompatibles para el mismo negocio.** Decisión **D12**» · D12: «**Corregirla en el mismo commit del producto 49**».

**Problema.** El diagnóstico es correcto y el hallazgo, bueno. **El alcance no.** Censadas por mí las FAQ de ese mismo fichero que publican una inversión inicial:

| Línea | Pregunta | Rango publicado | ¿Hay producto vivo que lo contradiga? |
|---|---|---|---|
| `:279` | ¿Cuánto cuesta abrir una heladería artesanal? | 60.000 – 180.000 € | — |
| **`:393`** | ¿Cuánto invertir en una chocolatería artesanal? | **80.000 – 250.000 €** | el 49, cuando salga |
| **`:505`** | **¿Cuánto cuesta montar un obrador de pastelería profesional?** | **50.000 – 180.000 €** (90.000-250.000 con punto de venta) | 🔴 **`guia-pasteleria-obrador`, 65 €, LIVE desde el 10-sep** |
| `:618` | ¿Cuánto cuesta abrir una pizzería artesanal? | 80.000 – 250.000 € | — |
| `:731` | ¿Cuánto cuesta abrir una cafetería de especialidad? | 50.000 – 180.000 € | `plan-negocio-cafeteria`, 29 € |
| **`:1070`** | **¿Cuánto cuesta montar una panadería artesanal con obrador?** | **70.000 – 220.000 €** | 🔴 **`guia-panaderia-obrador`, 65 €, LIVE** |

Las seis están **en los siete idiomas**. Es decir: **el problema que el research presenta como futuro ya está ocurriendo**, con dos productos vendidos, desde hace días en un caso y meses en el otro. Y el patrón de las partidas es idéntico en las seis (misma estructura, mismos órdenes de magnitud, «vitrina refrigerada 4.000-18.000 €» en todas): no son seis cifras investigadas, es una plantilla.

**Evidencia:** `src/data/use-cases-content.es.consultor.ts:279, 393, 505, 618, 731, 1070` · `grep -l "80.000" src/data/use-cases-content.*.consultor.ts` → 7 ficheros · `astro-site/public/dl/guia-pasteleria-obrador/` (8 xlsx, LIVE) · `curl https://aichef.pro/guia-pasteleria-obrador` → 200.

**Gravedad: alta.** No es un riesgo del 49: es una contradicción **ya publicada** entre un `FAQPage` y dos guías de 65 € que el mismo dominio vende, y que cualquier comprador puede enseñar.

**Fix.** Reescribir **D12** como decisión de **familia**, no de página: (1) las **seis** FAQ pasan a un formato que no publique un rango cerrado («la inversión depende de X, Y y Z; si vas a abrir, la guía de N € trae el modelo por escenarios») **y enlazan al producto de su vertical** — con lo que además se convierte una deuda en seis enlaces entrantes nuevos; (2) las de **pastelería y panadería** se corrigen **antes** que la de chocolatería, porque ésas ya contradicen a producto vendido; (3) queda como fila del `censo-entregables.py`: **ninguna FAQ de `/usos/` publica una cifra de inversión que un producto vivo contradiga**.

---

### B2 · MEDIA — El «patrón de las hermanas» para el nombre de catálogo no existe: la hermana inmediata se llama «Cómo Montar una Pastelería», y adoptar D17 reabriría el defecto que la hermana ya cerró hace dos días

**Afirmación literal (§12.1 y D17):** «**Nombre de catálogo, banner y email: «Guía Chocolatería con Obrador»** — **calca el patrón de las hermanas** (`products-catalog.ts`: «Guía Panadería con Obrador», «**Guía Pastelería con Obrador**»). Inglés propuesto: «Guide: Chocolate Shop with Production Room»».

**Problema.** Leído el catálogo:

| slug | `name.es` real | `name.en` real |
|---|---|---|
| `guia-panaderia-obrador` | «Guía Panadería con Obrador» | «Guide: Bakery with Production Room» |
| **`guia-pasteleria-obrador`** | **«Cómo Montar una Pastelería»** | **«Guide: How to Open a Pastry Shop»** |

La segunda mitad de la cita **no está en el fichero**. Y no es un detalle: la hermana inmediata —el molde que este producto copia, publicada el 10-sep— **ya abandonó ese patrón y alineó el nombre de catálogo con el H1**, que es exactamente el remedio que el propio §12.1 reclama dos párrafos después («⚠️ *el nombre del enlace debe coincidir con el de la página de destino… o repetimos el defecto de “Biblioteca de Prompts” → `/libreria-de-prompts`*»). Aprobar D17 tal como está redactada significa **reintroducir a sabiendas** el defecto que la hermana cerró, y hacerlo en el hub, el footer, los banners y el email a la vez.

**Evidencia:** `src/data/products-catalog.ts` (bloque `guia-pasteleria-obrador`, `name.es`) · `RESEARCH` §12.1 y D17.

**Fix.** **Un solo nombre: «Cómo Montar una Chocolatería»** en H1, catálogo, banner y email — como hizo Pastelería; EN «Guide: How to Open a Chocolate Shop». Reformular D17 para que John decida con el dato correcto, y anotar el de `guia-panaderia-obrador` como homologación pendiente en una sesión impar.

---

### B3 · MEDIA — El hueco del 24-oct cuelga de dos correos que aún son BORRADOR, y el research lo presenta como «libre» tras haber declarado que no consultó Resend

**Afirmación literal (§13.3 y D8):** tabla con «14-oct **Guía de Pastelería (lanzamiento) — BORRADOR**», «19-oct Kit de Tareas Pastelería 2.1 — **BORRADOR**», «**24-oct ← hueco de la Guía de Chocolatería — libre**». Y en §16: «❌ **No consulté Resend**: el hueco del 24-oct es una previsión sobre lo documentado en el calendario, **no un hueco confirmado por API**».

**Problema.** La regla de John es «el `scheduled_at` **más tardío que haya en Resend** + 5 días». El `scheduled_at` más tardío **que existe en Resend** es el del **9-oct** (food truck, el único confirmado como PROGRAMADO el 10-sep). Los del 14-oct y 19-oct son borradores que **todavía no tienen `scheduled_at`**. Aplicada al pie de la letra, la regla da hoy **14-oct**, no 24-oct; el 24-oct sólo es correcto **si y cuando** los dos borradores se programen. La palabra «libre» en una tabla que además se apoya en una declaración de no-verificación es la clase de dato que se copia al handoff y luego nadie revisa.

Y hay un segundo orden que decidir y no está dicho: si se adelanta (D8), **el 49 se metería delante del lanzamiento de su propia hermana**, que lleva dos días publicada y aún no tiene correo.

**Evidencia:** `scripts/productos-digitales/CALENDARIO-V2-SEMANAL.md:118-121` y `:144-145` · `RESEARCH` §13.3, D8, §16.

**Fix.** Cambiar «libre» por «**condicionado**: 24-oct **si** Pastelería (14-oct) y Kit Pastelería 2.1 (19-oct) se programan a partir del 14-sep y del 19-sep; si no, el hueco real es el 14-oct». Y **confirmarlo por API** (`GET /broadcasts`) antes de escribirlo en el handoff — cuesta una llamada.

---

### B4 · MEDIA — La palanca «bajar a 8 libros: −0,30 M» no es coherente con el coste por libro que el propio presupuesto usa

**Afirmación literal (§15.4):** «0,30 M/libro **medido** × 9» · palanca 1: «**Bajar a 8 libros** (absorber el 3 en el 4): **−0,30 M**».

**Problema.** Absorber el libro 3 en el 4 **no borra su contenido**: las cuatro hojas (coste de cobertura por referencia, escenarios de precio, repercusión al PVP, stock) pasan a ser hojas del libro 4. Lo que se ahorra es el envoltorio del libro (instrucciones, versión, `mapa-*.json`, su pasada de `gate_libros.py`), no los 0,30 M de construir sus fórmulas. El mismo razonamiento se aplicó al revés y bien tres líneas antes para absorber el libro 10 de L6 («son dos hojas, no un libro… **ahorra 0,30 M sin perder nada visible**») — pero ahí el contenido sí se reducía a dos hojas que ya existían en el plan financiero.

**Evidencia:** `RESEARCH` §15.4, palancas 1 y 2, y §9.2 (arbitraje contra L6).

**Fix.** Poner a la palanca su coste real (**−0,05/0,10 M**, no −0,30) y quedarse con la conclusión, que no cambia: **no se recomienda**.

---

### B5 · BAJA — «Es el segundo paquete más grande de los cinco» con 9 libros frente a 8, 8, 7 y 7

**Afirmación literal (§9.4):** «Es el **segundo paquete más grande** de los cinco productos nuevos del ciclo, **por detrás sólo del que Pastelería llegó a proponer**: Food Cost entregó 8 xlsx, el Manual del Manager 7, el Manual del Chef Ejecutivo 7 y la Guía de Pastelería **8**. Aquí son **9**».

**Problema.** Con los números de la propia frase, **9 es el mayor de los cinco**. Comparar lo que este producto va a **entregar** con lo que otro **llegó a proponer** y no entregó es cambiar de unidad a mitad de frase — y el §11.2 argumento 3 usa la comparación correcta («9 libros frente a los 8 de Pastelería») para sostener el precio.

**Fix.** «**Es el paquete más grande de los cinco: 9 libros frente a los 8 de Pastelería y Food Cost y los 7 de los dos manuales.**»

---

## C — PRODUCTO

### C1 · ALTA — El libro 5 iba a construir una tabla de vidas útiles que el kit de 12 € YA publica, con números incompatibles — y las seis reglas de frontera, declaradas «verificadas hoja a hoja», no tienen ninguna para eso

**Afirmación literal (§8.1):** «Medido por mí: **11 ficheros**… **139 fórmulas**… **El kit es papel, no calculadora**» y las seis reglas **K1-K6** (templado/moldeado · campañas · perfiles · vitrina · caja · temperaturas), presentadas en §15.3 riesgo 5 como «**las 6 reglas K1-K6 del §8.1, verificadas hoja a hoja**». Y el **libro 5** (`vida-util-rellenos-y-rotacion.xlsx`) es uno de los cuatro «**sin molde previo**» que sostienen el precio: «plazo orientativo por familia… 🔴 **El hueco funcional de la “decisión del huevo” de pastelería**».

**Problema.** Abierto `02-partidas-produccion.xlsx`, hoja **Moldeado**, el kit de 12 € publica esto:

> «**VIDA ÚTIL Y CONSERVACIÓN ORIENTATIVAS A 15-18 °C Y 50-60 % DE HUMEDAD — ajústala a tu fórmula y a tu obrador**
> Tabletas y chocolate sin relleno — **12-18 meses** · **Bombones de ganache con nata fresca — 10-15 días** · **Bombones de ganache con nata UHT, sorbato o alcohol — 4-8 semanas** · Frutos secos garrapiñados y frutas confitadas bañadas — 1-3 meses · Chocolate acabado: NO congelar»

Es **exactamente** el entregable del libro 5, con el mismo descargo («orientativas… ajústala») y con **números distintos de los que el research quiere publicar**:

| | Kit de 12 €, publicado | `CHS-56`, lo que iría al libro 5 y al cap. 16 |
|---|---|---|
| Ganache sin conservante | **10-15 días** | «máximo **8 días**» |
| Ganache con sorbitol/conservante | **4-8 semanas** | «**5 o 6 semanas**» |
| Factor entre extremos | ×3,7 | **«factor 5»** (el titular del hallazgo) |

Es decir: el **hallazgo de modelo de negocio nº 1 del research** («§3.5 (a) La vida útil del relleno es una decisión de MODELO DE NEGOCIO, y **el factor es 5**»), que sostiene un libro, un capítulo, un dolor y una decisión del bonus, **ya está publicado por la misma casa con otras cifras y otro factor**, en el producto que la guía cross-sella y cuya frontera se declara verificada hoja a hoja. Es el patrón exacto de la **A4 de Pastelería** (el kit publicando 48-72 h donde la guía enseña 24 h), esta vez sin ilegalidad de por medio pero con el mismo efecto comercial: el comprador de los dos productos lee dos respuestas del mismo autor.

**Evidencia:** `astro-site/public/dl/kit-tareas-chocolateria/02-partidas-produccion.xlsx`, hoja `Moldeado` (leída con openpyxl) · `RESEARCH` §3.5(a) `CHS-56`, §8.1 K1-K6, §9.2 libro 5, §10 cap. 16, §15.3 riesgo 5.

**Fix.** (1) Añadir **K7 — vida útil**: la tabla por familia **ya existe en el kit**; la guía **no la reescribe**, la **cita** y construye lo que el kit no tiene: **aw, lote económico, merma por caducidad en €/año y la vida útil que TÚ declaras** (celda verde, nunca calculada). (2) Decidir **una** fuente para los plazos orientativos: o el kit o `CHS-56`, y si es `CHS-56`, **corregir el kit en el mismo commit** y anotarlo en su changelog. (3) Volver a pasar las seis reglas K abriendo **todas** las hojas, no las primeras filas.

---

### C2 · ALTA — Tres juegos distintos de temperatura y humedad para el mismo obrador: el kit publica unos, el capítulo 07 y el libro 1 se escribirían con otros, y el semáforo del libro 5 suspendería a la vitrina que el kit manda tener

**Afirmación literal (§4.2, verificación 15, cap. 07, libro 1, libro 5, decisión nº 6 del bonus):** «Sala de trabajo **18-22 °C**» · «Humedad relativa de sala **< 55 %**» · «Cámara ✅ **15-18 °C**» · cap. 07: «**18-22 °C de sala, 15-18 °C de cámara**» · «🔴 **La vitrina de chocolate va a +14/+17 °C, no a +2/+4 °C**» · libro 5: «**semáforo de vitrina refrigerada (+14/+17 °C) vs climatizada**».

**Problema.** El kit de 12 €, abierto por mí, ya fija estos valores — y no son los mismos:

| Concepto | Kit `kit-tareas-chocolateria` (publicado) | Research → cap. 07 / libro 1 / libro 5 |
|---|---|---|
| Obrador al templar | «objetivo **18-20 °C** y **menos del 60 %** de humedad» (`02!Templado`) | **18-22 °C**, HR **< 55 %** |
| Sala de tienda | «mantener sala **20-22 °C**» (`01!Apertura`) | — |
| Cámara de conservación | «**15-18 °C** y **50-60 %** de humedad» (`01!Apertura`, `01!Cierre`) | **15-18 °C**, humedad «controlada» |
| **Vitrina de bombonería** | «**mantiene 16-18 °C** y no condensa… por encima de 20 °C la manteca funde» (`01!Apertura`) | **+14/+17 °C** |
| Almacén de producto acabado | «**15-18 °C y 50-60 %**, en oscuridad» (`02!Moldeado`) | — |

Dos consecuencias concretas:

1. **El semáforo del libro 5 pondría en rojo la vitrina del propio kit.** 18 °C está dentro del objetivo del kit y fuera del rango que el research declara correcto. Un cliente de los dos productos tiene un checklist diario que le manda mantener 16-18 °C y un xlsx que le dice que eso está mal.
2. **El capítulo 07 es «el criterio del chocolate»**, el capítulo nuevo que más justifica el precio, y su título lleva las cifras dentro. Escribirlo sin reconciliar con lo que la casa ya publica es garantizar la contradicción.

Además, la verificación 15 presenta los 15-18 °C de cámara como un **arbitraje entre lentes** resuelto con una fuente externa (Llevats21), cuando **la propia casa ya los publica desde hace meses** en dos ficheros del kit. No es un error, pero indica que el §8.1 no abrió esos ficheros.

**Evidencia:** `kit-tareas-chocolateria/01-apertura-cierre.xlsx` (hojas `Apertura` y `Cierre`) y `/02-partidas-produccion.xlsx` (hojas `Templado` y `Moldeado`) · `RESEARCH` §4.2, verificación 15, §9.2 libros 1 y 5, §10 cap. 07, §9.3 decisión 6.

**Fix.** **Un concepto, una fuente, y la fuente incluye lo ya publicado.** Fijar en `datos_ejemplo.py` **cuatro** valores únicos —sala de trabajo, HR de sala, cámara, vitrina— reconciliados con el kit; donde difieran, decidir cuál es el bueno y **corregir el kit en el mismo commit** (es una celda de texto por fichero) o ajustar la guía. La vitrina es la que más urge: **+14/+17 °C** es el rango de un producto real (Docriluc WB-6-6-R) y **16-18 °C** el que el kit pide verificar cada mañana; no pueden convivir con un semáforo de por medio.

---

### C3 · ALTA — Tres libros declaran salidas que sólo se obtienen cruzando datos ENTRE libros, que es lo que la convención de familia prohíbe y lo que produjo el hallazgo alto de Pastelería

**Afirmación literal (§9.2, columnas «Salidas por fórmula»):**
- Libro 6: «**déficit de capacidad** (**contra el libro 1**)»
- Libro 7: «**fecha límite de cierre de pedidos de Navidad calculada hacia atrás desde la capacidad del libro 1**»
- Libro 9: «**desviación contra el CAPEX del libro 2**»

Y en el mismo documento, §9.1: «**prohibidos `INDIRECT`, `COUNTA`, `PMT`, `OFFSET`, `XLOOKUP`, `LET`, `LAMBDA` y las referencias entre libros**» · §8.1: «**Cero fórmulas entre libros**» · §9.1 otra vez: «🔴 **Un concepto, UNA fuente** (A3 de la refutación de Pastelería: el fondo de maniobra calculado dos veces publicó **dos inversiones totales distintas** en el mismo pack)» · y la **FAQ 11**, que se lo promete al comprador: «*no hay referencias entre libros*».

**Problema.** Sólo hay dos maneras de producir esas tres salidas, y las dos están prohibidas:
- **con una referencia externa** → viola la convención, el `gate_libros.py` y la promesa de la FAQ 11;
- **reintroduciendo el dato a mano en el segundo libro** → el mismo concepto (capacidad de obrador; CAPEX total) queda calculado en dos sitios, que es **literalmente el defecto ALTO que la refutación de Pastelería cazó** y que este research cita como lección aprendida en la línea de arriba.

Y no es teórico: la «fecha límite de cierre de pedidos de Navidad» es una de las salidas que el research más vende (§3.5(b), decisión nº 7 del bonus, cap. 19), y la «desviación contra el CAPEX» es la razón de ser de la hoja de contador del libro 9.

**Evidencia:** `RESEARCH` §9.2 (filas 6, 7 y 9), §9.1 (restricciones y regla «un concepto, una fuente»), §8.1 (regla transversal D21), §14 FAQ 11.

**Fix.** Aplicar la misma regla D21 que el research define para el kit, pero **hacia dentro del pack**: cada cruce se materializa como **celda verde de entrada en el libro receptor**, etiquetada «*trae aquí la cifra de `<libro>!<hoja>!<celda>`*», **más una fila de CUADRE con semáforo** que avise si el valor tecleado se aleja del de origen. Tres celdas verdes y tres filas de cuadre, declaradas en la SPEC como decisión, y el `gate_libros.py` con una comprobación nueva: **ninguna fórmula menciona otro fichero**.

---

### C4 · MEDIA — La hoja «Clima del Obrador» promete calcular la carga térmica de la cámara y el research no tiene un solo coeficiente con fuente para hacerlo

**Afirmación literal (§9.2, libro 1):** entradas «m³ de cámara a 15-18 °C… **T y HR objetivo**; **T exterior de tu ciudad en agosto**; potencia instalada» → salidas «**carga térmica de la cámara y si el equipo la sostiene en agosto**».

**Problema.** Para convertir m³ + ΔT en una carga térmica hacen falta, como mínimo: transmitancia del cerramiento (W/m²K) o un coeficiente empírico por m³, superficie de cada paramento, aportes internos (personas, iluminación, producto entrante y su calor específico) y renovaciones de aire. **El research no tiene ninguno de esos datos con fuente**: el §4.2 no publica un solo coeficiente, el deshumidificador va «precio sin fuente», y el §15.1 `N-9` elimina el único climatizador con precio que apareció. Con la regla de la casa —«**cero constantes tecleadas dentro de una fórmula**»— sólo quedan dos salidas, y las dos son malas: meter coeficientes inventados (prohibido, y es la clase de cifra que el verificador tumba), o ponerlos en celda verde y dejar que los rellene un lector que no los tiene.

Es la hoja que el research declara «**el** criterio del chocolate» y «nada equivalente en el catálogo». Si no se puede calcular, el libro 1 pierde su diferencial.

**Evidencia:** `RESEARCH` §9.2 libro 1 (columna «Salidas por fórmula»), §4.2 (tabla entera sin un solo coeficiente), §15.1 `N-9`, §9.1 (restricciones de familia).

**Fix.** Cambiar la salida por lo que **sí** es construible y sigue siendo útil: **(a)** semáforo de coherencia entre T objetivo, T exterior de agosto de su ciudad y la potencia frigorífica **que le ofrezca el instalador** (entrada en celda verde, con la unidad); **(b)** una **ficha de preguntas al instalador** (m³, ΔT de diseño, aportes, renovaciones) como hoja de checklist, que es exactamente el patrón que el research usa y defiende bien para el bean-to-bar sin precio público; **(c)** si se quiere un número, buscar y **citar** una fuente de coeficientes (IDAE o un fabricante) y pasarla por el verificador. Lo que no puede es salir sin ninguna de las tres.

---

### C5 · MEDIA — El libro 8 reproduce el defecto que la refutación de Pastelería ya marcó: «tres umbrales acumulativos» no son tres umbrales, y las entradas de la hoja no permiten comprobar dos de los tres requisitos

**Afirmación literal (§9.2, libro 8):** hoja «**Suministro a Otros Minoristas**», entradas «**¿suministras a otros minoristas?; kg/semana y a quién**», salida «**semáforo de los tres umbrales acumulativos**».

**Problema.** El texto del art. 3, que he leído entero, dice otra cosa — y el research **lo cuenta bien en la prosa** (§1.2 nº 11 y `CHN-41` son correctos: tres condiciones acumulativas y el que mata es «restringido»), pero **la especificación de la hoja vuelve a la formulación defectuosa**:

- Son **tres condiciones** (marginal · localizado · restringido), no tres umbrales. Dentro de «marginal» hay **dos vías ALTERNATIVAS**: «a) … ≤ 25 % del volumen anual, **o** b) … máximo 500 kg a la semana».
- Las entradas declaradas **no incluyen el % del volumen anual**, así que una chocolatería que despache 600 kg/semana pero suministre sólo el 10 % de su volumen anual a la tienda de al lado —**marginal por la vía a)**— saldría en rojo.
- Tampoco incluyen **distancia ni zona de salud**, así que «localizado» (art. 3.3, con su regla de **50 km** sólo para el caso interautonómico) no se puede evaluar.
- Y no aparece como salida la obligación del **art. 3.5**: declaración responsable más registro de destinatarios, cantidades y fechas.

Es la **A2 de la refutación de Pastelería** copiada al nuevo libro con otro nombre de hoja.

**Evidencia:** `BOE-A-2022-21681` consolidado, art. 3.1 a 3.6 · `RESEARCH` §9.2 libro 8 · `guia-pasteleria-research-REFUTACION-2026-09-09.md` A2.

**Fix.** Rehacer la hoja como **árbol**: «¿suministras a otros minoristas de distinta titularidad?» → **no** ⇒ no te aplica el art. 3; **sí** ⇒ tres semáforos independientes — **marginal** (por a) **o** por b): entradas «% del volumen anual» **y** «kg/semana»), **localizado** (zona de salud / ≤50 km interautonómico), **restringido** (¿alguno de tus clientes está inscrito en el RGSEAA?) — **más** la fila del art. 3.5.

---

### C6 · MEDIA — El juego de datos declara que las campañas «salen del BONUS-02 del kit» y deja fuera COMUNIONES, que es lo que sostiene tres de los meses «Alta» de ese mismo calendario

**Afirmación literal (§9.1):** «**Campañas:** Navidad+Reyes · San Valentín · Pascua (monas y huevos) · Día de la Madre · Halloween · Todos los Santos + valle de junio-agosto. **Salen del `BONUS-02` del kit, que ya declara Alta/Media/Baja mes a mes. Así el lector reconoce el calendario y la guía pone los euros**».

**Problema.** Abierto el `BONUS-02`, su calendario nombra como acciones clave, además de las seis recogidas: **Día del Padre (19-mar)**, **las COMUNIONES («arrancan las COMUNIONES (abril-junio)» en abril, «**pico de COMUNIONES**» en mayo, «últimas comuniones» en junio)**, **Black Friday** y el **puente de la Constitución y la Inmaculada**. Las comuniones son el motor declarado de **tres de los cinco meses «Alta»** del calendario y, en una bombonería española, una línea de detalle de mesa y caja personalizada con pedido anticipado — exactamente el tipo de campaña cuya economía el libro 6 dice que va a poner en euros. Si el lector «reconoce el calendario», lo primero que verá es que **falta el pico de primavera**.

**Evidencia:** `kit-tareas-chocolateria/BONUS-02-calendario-anual-tareas.xlsx`, hoja `Calendario`, filas Marzo, Abril, Mayo y Junio · `RESEARCH` §9.1 (fila «Campañas»), §9.2 libro 6, §10 cap. 18.

**Fix.** Añadir **Comuniones (abril-junio)** al juego de datos como campaña propia —con su antelación de pedido, que es lo que la hace distinta de Pascua— y **Día del Padre** y **Black Friday** como fechas menores. Y cerrar el círculo: si el calendario del kit es la fuente, que el `datos_ejemplo.py` lo declare fila a fila y un gate compruebe que **no falta ninguna de las 12 filas**.

---

### C7 · MEDIA — «El valle de junio-agosto» contradice el calendario que la casa ya publica, donde sólo agosto es baja y julio es temporada turística con la tienda abierta

**Afirmación literal (§9.1, §6.2 D1, §9.2 libro 6, §10 cap. 18):** «+ **valle de junio-agosto**» · «un valle de **tres meses**» (D7) · «en pastelería el verano es “menos venta”; **aquí es IMPOSIBILIDAD TÉCNICA de producir + parada de canal**» · libro 6: «**coste del valle: fijos que siguen corriendo con la caja parada**».

**Problema.** El `BONUS-02` del kit, leído fila a fila, dice:

| Mes | Temporada | Acciones clave |
|---|---|---|
| Junio | **Media** | «adaptar catálogo (menos ganache fresca, más tableta y producto estable)» |
| Julio | **Media** | «**Temporada turística: packs souvenir y colaboraciones locales**» |
| Agosto | **Baja** | «**la tienda abre para el turista aunque el obrador pare**» |

**Un mes «Baja», no tres.** Y el matiz del kit es mejor que el del research: lo que para en verano es **el obrador**, no la caja — julio es temporada turística y en agosto la tienda sigue abierta. «Fijos que siguen corriendo **con la caja parada**» describe un negocio distinto del que la propia casa documenta, y es la salida que da sentido a la hoja «El Valle de Verano», uno de los cuatro libros «sin molde previo» con los que se defiende el precio de 65 €.

(El dato que sí es sólido y hay que conservar es el de Equimercado: **apagar los ENVÍOS** el 12 de junio. Eso es una parada de **canal online**, no del mostrador — y así hay que contarlo.)

**Evidencia:** `kit-tareas-chocolateria/BONUS-02-calendario-anual-tareas.xlsx`, filas Junio, Julio y Agosto · `RESEARCH` §3.4, §6.2 D1, §9.1, §9.2 libro 6, §10 cap. 18, D7.

**Fix.** Reformular el valle como lo que las dos fuentes propias sostienen: **producción parada en agosto · envío parado de junio a septiembre · mostrador vivo con mix distinto (tableta y producto estable en lugar de ganache) y con turista en julio y agosto**. La hoja deja de llamarse «el coste de la caja parada» y pasa a calcular lo que de verdad duele: **la caída del margen al cambiar el mix** y los fijos contra una facturación menor pero no nula. Es un entregable mejor y, además, verdadero.

---

### C8 · MEDIA — La hoja «Denominaciones y Mínimos Legales» no puede decidir la denominación con los datos que un chocolatero tiene: la etiqueta de una cobertura no publica el desglose que la norma exige

**Afirmación literal (§9.2, libro 4):** entradas «… **% de cacao y de manteca por referencia**…» → salidas «**qué puedes LLAMAR legalmente a cada referencia y qué menciones debe llevar**». Y `CHN-02`/`CHN-07`/`CHN-08` como contenido del cap. 10.

**Problema.** Verificado el texto: la norma no trabaja con «% de cacao» sino con **tres magnitudes distintas** —materia seca **total** de cacao, **manteca** de cacao y materia seca **desgrasada**— y con **dos bases de cálculo** (ap. 4: para 1.10 y 1.13 el mínimo se calcula **deduciendo el relleno**, mientras que el 25 % del chocolate se calcula **sobre el peso total, relleno incluido**). Una bolsa de Callebaut 811 publica «**54,5 %**» y nada más; el desglose manteca/desgrasada está en la **ficha técnica**, que hay que pedir. Sin esos dos números por referencia, la hoja no puede decidir si algo es «chocolate», «cobertura» o si admite un calificativo del ap. 6.g).

**Evidencia:** `BOE-A-2003-15599`, aps. 1.6, 1.10, 1.13, 4 y 6.g) · `RESEARCH` §9.2 libro 4, §10 cap. 10, `CHS-28a`.

**Fix.** Partir la hoja en dos capas: **(a) lo que SÍ se calcula con el escandallo** —el **25 % de chocolate sobre el peso total** del bombón o del relleno (art. 1.10/1.13), que sale solo de los gramajes que el lector ya mete— y **(b) lo que se COPIA de la ficha técnica del proveedor**: materia seca total, manteca y desgrasada, en tres celdas verdes, con la nota «*pídesela a tu proveedor; la bolsa sólo trae el total*». Esa petición encaja además con la ficha de proveedor del libro 9 y refuerza el argumento de venta de §4.6 sin inventar nada.

---

### C9 · BAJA — «`kit-escandallos`: 13 ficheros y NINGUNO de chocolate» es cierto por fichero y falso por hoja: la 05 tiene una hoja llamada «Tarta Chocolate»

**Afirmación literal (§8.3):** «`kit-escandallos` (12 €) — **13 ficheros y NINGUNO de chocolate** (verificado: la 05 es de pastelería por lote) | **CITAR** como cross-sell. **El escandallo de chocolate se CONSTRUYE porque no existe en el catálogo**».

**Problema.** Abierto `05-pasteleria.xlsx`, sus hojas son: `Instrucciones`, **`Tarta Chocolate`**, `Croissants`, `Macarons`, `Conversiones`, `Mermas`. La frontera sigue siendo defendible —una tarta de chocolate no es un escandallo por molde y tanda con merma de templado— pero la frase tal como está la puede refutar cualquier comprador que abra el kit de 12 €, y es una frase que va a la **FAQ 2** y a la landing.

**Evidencia:** `astro-site/public/dl/kit-escandallos/05-pasteleria.xlsx` (hojas leídas con openpyxl) · `RESEARCH` §8.3.

**Fix.** «*El Kit de Escandallos trae una hoja de tarta de chocolate dentro de su libro de pastelería: costea una elaboración por unidad. Lo que no existe en el catálogo es el escandallo del obrador de bombonería —por molde y por tanda, con merma de templado, recorte recuperable y la caja como unidad de venta—, y eso es lo que construye esta guía.*»

---

### C10 · BAJA — La FAQ contempla incorporar dos preguntas del PAA que son definicionales, contra la regla que la propia FAQ abre

**Afirmación literal (§14):** «Las de **oficio**… y las de **consumidor**… **quedan fuera**: no son nuestras» y, doce líneas después: «del PAA medido, **elegir UNA sola** entre «¿Cuáles son los 3 tipos de chocolate?» y «¿Cuáles son los 4 tipos de chocolate?»».

**Problema.** «¿Cuáles son los N tipos de chocolate?» es una pregunta **definicional de consumidor**, la categoría que la propia FAQ acaba de excluir; la instrucción operativa es «elegir una», no «descartarlas». Las 12 preguntas redactadas son buenas y **todas son de compra** — el defecto está sólo en esa nota, pero es la nota que un redactor va a seguir.

**Evidencia:** `RESEARCH` §14 (encabezado y párrafo de JSON-LD).

**Fix.** Sustituir por: «**Ninguna de las dos entra**; si el PAA definicional interesa, su sitio es una pieza de blog, no el `FAQPage` de una landing de compra». Y mantener el gate `clasifica()` sobre los pares 2/7 y 6/8, que sí está bien visto.

---

### C11 · BAJA — El «recorte recuperable» se presenta como contenido propio frente a Pastelería y la regla ya está escrita en el kit de 12 €

**Afirmación literal (§8.2):** «Es **CONTENIDO PROPIO (nunca se copia)**: **La merma de templado y el recorte recuperable** (el chocolate mal templado **se vuelve a fundir**; la masa fallida no)».

**Problema.** El kit ya lo dice, y con el matiz que falta: «*El chocolate **sin relleno y sin contaminar** se puede refundir; **el que lleva ganache o fruta, a residuo*»* (`02-partidas-produccion.xlsx!Moldeado`). La frontera sigue siendo correcta —el kit da la regla, la guía pone los euros— pero la novedad es menor de lo que se vende, y **el matiz del kit (relleno = no recuperable) es justo lo que hace que la hoja de merma tenga dos tasas y no una**.

**Evidencia:** `kit-tareas-chocolateria/02-partidas-produccion.xlsx!Moldeado` · `RESEARCH` §8.2, §9.2 libro 4.

**Fix.** Reformular como «**la guía cuantifica** la regla que el kit enuncia», y modelar en el libro 4 **dos tasas de merma**: recuperable (chocolate limpio) y no recuperable (con relleno o fruta). Sale mejor hoja y se le da la razón al kit en vez de ignorarlo.

---

## Resumen para la SPEC

**Antes de firmar, siete cosas y ninguna es cara:**

1. `CHN-22` reescrito con las **tres** condiciones del art. 38.3 y la puerta «operador ≠ operador posterior» (A1) — y que el verificador legal firme la interacción 2.15 ↔ 38.3.
2. El número de DDS con su condición («sólo si tu proveedor es operador») y la tabla del art. 5.3.b) en el libro 9 (A2).
3. El 644.5 con su límite y una fila **canal → epígrafe** en el checklist legal (A3).
4. La tabla de presupuesto **con el guion** y sumando (A4) — es lo que John necesita para D14.
5. **D12 ampliada a las seis FAQ de `/usos/`**, empezando por pastelería y panadería, que ya contradicen a producto vendido (B1).
6. **Reconciliar con el kit de 12 € antes de escribir una línea**: vidas útiles (C1), temperaturas y vitrina (C2), campañas (C6) y valle (C7). Son cuatro celdas de texto en el kit o cuatro decisiones en el juego de datos, pero hay que tomarlas **antes** del `datos_ejemplo.py`.
7. Los **tres cruces entre libros** resueltos como celda verde + fila de cuadre, y `gate_libros.py` con la comprobación de que ninguna fórmula nombra otro fichero (C3).

Lo que **no** hace falta re-verificar está en la primera sección: el censo del repo, la escalera de precios, los 24 banners, las cinco keywords con su serie, los 285/6 de GSC, el RD 1055/2003 entero, el art. 3, el 4 y el 13 del RD 1021/2022, el 644.5/644.6/676 del IAE con su errata, los cuatro artículos de la Ley 7/2022, el 9.3/9.4 del RD 1055/2022 y los artículos del EUDR **salvo** la interacción del 38.3.

**Via: Claude Code**
