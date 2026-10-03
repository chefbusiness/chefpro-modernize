# REFUTACIÓN — «Cómo Montar una Churrería-Chocolatería»

**Fecha:** 2026-10-03 · **Sesión:** Claude Code (subagente refutador, F1) · **Objeto:** `scripts/productos-digitales/auditorias/guia-churreria-RESEARCH-2026-10-03.md` (546 líneas) y las cinco lentes `guia-churreria-research-L1…L5-*.md` del mismo directorio.
**Método:** tres lentes en un pase (rigor · negocio · producto). Verificación directa contra el **texto consolidado del BOE descargado con `curl`** (Orden de 26-01-1989 de aceites calentados, RDLeg 1175/1990 del IAE, Ley 12/2012, Ley 7/2022, ET art. 36, análisis del RD 199/2010), contra el **DOUE del Rgto. (UE) 2017/2158** (PDF de la copia del BOE, leído con PyMuPDF), contra el **PDF del BOE de la modificación del ALEH VI** (`BOE-A-2026-18630`), contra la **página de Loomis Pay en HTML**, contra el **repositorio** (fichero:línea), contra **dos xlsx de la hermana abiertos con openpyxl** (`read_only`, `data_only`, uno cada vez), contra **GSC en vivo** (`sc-domain:aichef.pro`, 2026-07-05 → 2026-10-03, por page **y por query**) y contra **Resend en vivo** (`list-broadcasts`). **Se ha intentado TUMBAR la propuesta, no confirmarla.**

**Veredicto: CORREGIR ANTES.** 26 refutaciones: **6 altas · 13 medias · 7 bajas**.

El núcleo aguanta y la parte normativa es la mejor trabajada del ciclo: la norma de aceites calentados, el 644.6 y su nota, el ámbito de la acrilamida, la derogación del RD 199/2010, el aceite usado de la Ley 7/2022 y la vigencia del ALEH VI salen **literales** de su fuente. Pero **no se puede firmar la SPEC tal cual**. La afirmación laboral que sostiene el libro 8 y el dolor nº 1 está mal sumada: quien entra a las 4:00-5:30 **no** es trabajador nocturno. La FAQ pública publica un techo de traspasos de 120.000 € que la propia lista negra prohíbe. La «salida del verano» con media cuota del IAE **no existe** para casi nadie. El «sin licencia previa» del despacho se publica sin la condición de obra que justo choca con el conducto a cubierta que exige la fritura. El presupuesto de redactores está entre **0,7 y 2,6 M por debajo** de lo que da la calibración medida de la hermana. Y dos ciclos entre libros (1 → 4 → 3 → 1 y 2 ↔ 6) impiden rellenar los Excel en un orden válido y cuentan dos veces el fondo de maniobra.

> ⚠️ **Térmica:** `istats cpu temp` entre tandas: 54,1 → 49,3 → 48,4 → 48,1 → 48,1 → 46,6 → 47,9 °C. Dos xlsx con openpyxl, uno tras otro (`read_only`, `data_only`). Dos PDF con PyMuPDF, uno cada vez. Sin builds, navegador ni Playwright. Ningún fichero del repo modificado salvo este informe; sin commits.

---

## Lo que SÍ he confirmado letra a letra (para que NO se re-verifique)

**BOE, consolidado leído por mí:**
- **Orden de 26-01-1989** (`BOE-A-1989-2265`, «Última actualización publicada el 29/03/2013»): art. **3** literal (catering, «freidurías, bares, las cocinas elaboradoras de comida para llevar», permanentes y de temporada, y «ferias» en la vía pública) · art. **6.3** «El contenido en componentes polares será inferior al 25 por 100, determinado de acuerdo con el método analítico que figura como anexo 1» · arts. **7, 8, 10, 11 y 12 derogados** «por el art. 46 del Real Decreto 176/2013» · art. **9** vivo · disposición adicional: **norma básica**. `CUN-01…03` exactos.
- **RDLeg 1175/1990** (`BOE-A-1990-23930`): **644.6** con su nota literal («faculta para la elaboración de los productos de churrería; así como patatas fritas, en el propio establecimiento, siempre que su comercialización se realice en las propias dependencias de venta») · **676** con la nota de media cuota si abre «seis meses o menos al año» · **675** con la misma nota · **663.1** con su nota de masas fritas · **419.3** («churros, buñuelos, etc.») · **673**. `CUN-09…14` exactos en el texto.
- **Ley 12/2012** (`BOE-A-2012-15595`): el Anexo incluye el **epígrafe 644.6** literal; art. 2.1 (750 m²) y 2.2 (patrimonio y dominio público) · art. **3.3 y 3.4** (ver A4).
- **Ley 7/2022** (`BOE-A-2022-5809`): art. 2.a) («hostelería, restauración y análogos») y art. **25.3** literal: residuos comerciales no gestionados por la entidad local, «a excepción del aceite de cocina usado para el que será obligatoria su recogida separada a partir del 30 de junio de 2022». `CUN-27` exacto.
- **RD 199/2010** (`BOE-A-2010-4173`, Análisis): «Fecha de derogación: 07/08/2021 · SE DEROGA, por Real Decreto 538/2021». `CUN-19` exacto.
- **ET art. 36.1** (`BOE-A-2015-11430`): nocturno de 22:00 a 6:00; trabajador nocturno con «no inferior a tres horas» diarias **o** un tercio de la jornada anual; 8 h de promedio en 15 días; sin horas extra. Texto de `CUN-29` exacto; **su aplicación, no** (A1).
- **ALEH VI, modificación** (`BOE-A-2026-18630`, Resolución de 25-08-2026): «nuevo periodo de vigencia … hasta el 31 de diciembre del año 2030». `CUN-32` exacto.

**DOUE, Rgto. (UE) 2017/2158 (copia del BOE, PyMuPDF):** art. **1.2** con la lista cerrada a)-h) y «churro» ausente · art. **2.2** (minorista → parte A) y **2.3** (franquicia → además parte B) · anexo II parte A, punto 1: «las temperaturas al freír serán inferiores a 175 °C y, en cualquier caso, lo más bajas posible», espumado y guía de colores «a la vista del personal». `CUN-04` y `CUN-05` exactos (matiz de la parte B en A14).

**Fuentes de sector:** Loomis Pay en HTML: «85», «90 %» y «85-90» **no** aparecen; sí «márgenes superiores al 60 % en producto», «Personal (2 operarios + ayudante): 2.400 € – 3.000 €» y «1.600 raciones al mes (≈55/día) para cubrir 5.000 € de gasto fijo». `CUS-01`, `CUS-05` y `CUS-28` exactos, y `CHS-31` va bien a la lista negra.

**La hermana, medida por mí con openpyxl:**
- `calculadora-capex-chocolateria.xlsx!Variante del Formato`: fila 9 «Chocolatería de taza y churros · CHS-46a + CHN-48 + CHN-49c · 527 · Sólo la chocolatera», filas 37-41 (chocolatera 527 € sin IVA; churrera, freidora, extracción y campana «Sin cifra»), fila 47 Maestro Churrero «Sin cifra con id». El 85-90 % sale de `guia-chocolateria/datos_ejemplo.py:2301`. **Verificación 1 confirmada.**
- `plan-financiero-3-anos-chocolateria.xlsx!PyG 3 Años`: B66 **17.268,87** / C66 **20.043,54** · B67 **8,674 %** / C67 **8,605 %** · B68 «La taza y los churros restan: con estos supuestos te ocupan sala y personal para nada» · C54 35 clientes/día, C57 3,50 €, **C58 margen bruto 0,5**, C59 12.462,96 € de personal. **Verificación 2 confirmada al céntimo.**
- `CHN-49b` (JSON de la hermana): «incluye el grupo 644 completo —644.1 … 644.5 y 644.6—» (ver A13) · `CHN-93`: Toledo `45000145011981` «MAZAPAN, MASAS FRITAS, CONFITERIAS Y CHOCOLATES», 01/01/2025-31/12/2026. **Verificación 3 confirmada.** · `CHN-67`: SMI 2026 **1.221 €/mes, 17.094 €/año** (RD 126/2026) · `CHN-73`: IAE exento para personas físicas y sociedades con < 1 M € · `CHS-37b`: 82.000-95.000 €, 74 m², 910 €/mes · `CHS-46a`: Ugolini 527 € sin IVA.

**Repo — exacto:** `products-catalog.ts` **50** entradas y **escalera completa de §11 exacta en sus 14 filas** (9×1 · 12×13 · 14×9 · 18×1 · 18,50×1 · 24×1 · 29×2 · 35×3 · 39×1 · 45×4 · 55×3 · **65×9** · 85×1 · 89×1); los 9 de 65 € son los 6 de restaurante, Panadería, Pastelería, Chef Ejecutivo y la hermana; `kit-gestion-personal` = **14 €** (`:91`) · `comingSoon` arranca en `…HubPage.astro:1014`, nuestra tarjeta en `:1015`, **21** tarjetas; SPA `:997`/`:998` · render del contador en `:1205` y guarda `{comingSoon.length > 0 && (` en `:1511` · `sinonimos-buscador.json:111` alias de la hermana · `PRODUCT_ALIASES` en `src/lib/linkify-use-case.tsx:13` y `astro-site/src/lib/linkify-use-case.ts:17` · `guia-chocolateria-obrador.ts:286` y `:349` son las dos FAQ «¿Cubre la chocolatería de taza y churros, tipo San Ginés?» · `robots.txt` con `/guia-*-access` y `/guia-*-library` en `:44-45, :98-99, :152-153, :206-207, :260-261` · role pages `:1264` y `:3248` con la hermana en 1.ª, `:2255` con `guia-pasteleria-obrador`, `:4240` con `kit-tareas-cafeteria` · **327** posts ES · el post: banners en `:64`, `:123`, `:153`; suelos de la tabla `:53-58` = **26.000 €** y techos = **62.500 €** frente al «12.000-50.000» de `:60`. **Verificación 5 confirmada.**
- Dotación tipo de L4 §4.1 (`L4:169-174`) **recomputada línea a línea**: A = 4.185,45 € y B = 8.618,35 €, con opcionales 5.014,45 € y 9.447,35 €. Exacto.
- Mediana de traspasos «~571 €/m²» con los 11 anuncios: **571** exacto (pero ver A2).
- Calibración de §10: 59.334 / 37.900 = **+56,6 %**, 59.334 / 111 = **534,5** pal/pág, 17.002 / 10.500 = **+61,9 %**, 17.002 / 34 = **500,1**; los capítulos de §10 suman **33.000** exactos; guion de la hermana = **51.900 palabras** (guía 37.900 + business plan 3.500 + bonus 10.500).
- Anclas de §11: 65/290 = 22,4 %, 65/1.290 = 5,0 %, 65/12.000 = 0,54 %. Exactas (pero ver A10).

**GSC en vivo:** `/blog/ia-churrerias-guia-completa` **4 clics · 133 impresiones · 3,01 % · 4,9**; las otras 14 URLs con «churr» son legacy (≤ 8 impresiones, 0 clics). **Verificación 8 confirmada por page** (por query, ver B2).

**Resend en vivo:** cola ES programada Panadería 4-oct · Food Truck 9-oct · Pastelería 14-oct · Kit Pastelería 2.1 19-oct · Chocolatería 24-oct · **Taquería 29-oct (la última)**; no hay ningún broadcast de Escandallos 2.1 ni de Kit Chocolatería 2.1. **Verificación 6 confirmada.**

---

## A — RIGOR

### A1 · ALTA — «El churrero que entra a las 4-5 es trabajador nocturno»: la cuenta no da. Entre las 4:00 y las 6:00 hay dos horas, y la ley pide tres

**Afirmación literal:** `L3:142` (`CUN-29`): «El churrero que entra a las 4:00-5:00 **suma ≥3 h nocturnas** → sin horas extra y nocturnidad por convenio». Consolidado §2.1 fila 10 (`RESEARCH:102`): «trabajador nocturno = ≥ 3 h entre 22 y 6 (**el churrero que entra a las 4-5**) … **sin horas extra**». §3.5 (`:156`): «entrada 5:30-5:45 (`CUS-55`, `CUS-48`) **→ trabajador nocturno** (`CUN-29`)». Libro 8 (`:299`) y cap. 16.

**Problema.** El art. 36.1 del ET fija el periodo nocturno **de 22:00 a 6:00**. Entrar a las 4:00 da **2 h**; a las 5:00, **1 h**; a las 5:30-5:45, **15-30 minutos**. Ninguno llega a las tres horas diarias, y tampoco al tercio de la jornada anual (2,67 h de una jornada de 8 h). La plantilla del caso, la de las ofertas reales (`CUS-55`, entrada 5:30) y la de Antonio (`CUS-48`, 5:45) **no son trabajadores nocturnos**. Por eso no se les aplican el tope de 8 h de promedio, la prohibición de horas extra, la evaluación de salud ni el aviso a la autoridad laboral. **Sí** cobran el plus del convenio, que es otra cosa: Madrid paga +25 % de 0:00 a 8:00 (`CUN-40`), así que la entrada a las 5:30 ya genera 2,5 h con plus. El research mezcla las dos figuras.

**Daño.** Es el dolor nº 1 del comprador (§6, fila 1) y el único libro «sin molde» con norma detrás (§9.2: «el libro de turnos se mantiene … tiene norma verificada detrás»). Con la lectura actual, el libro 8 marcaría como nocturno a un churrero que no lo es, y el cap. 16 le diría al lector que **no puede pedir horas extra** a quien sí puede hacerlas. Eso es justo lo que resuelve el refuerzo de domingos y de Navidad.

**Evidencia:** `https://www.boe.es/buscar/act.php?id=BOE-A-2015-11430`, art. 36.1 (leído hoy) · `guia-churreria-research-L3-normativa.md:142` · `RESEARCH:102`, `:156`, `:299`.

**Fix.** Reescribir `CUN-29` con dos figuras separadas. (1) **Trabajador nocturno (ET):** ≥ 3 h diarias entre 22:00 y 6:00, o un tercio de la jornada anual; solo la madrugada de viernes, sábado y festivos del caso (§9.1, «madrugada … supuesto») puede llegar ahí, y hay que contarlo por persona. (2) **Plus de nocturnidad (convenio):** horas dentro de la franja del convenio, en Madrid de 0:00 a 8:00 al +25 % (`CUN-40`). En el libro 8, «¿es trabajador nocturno?» sale de `horas entre 22 y 6 ≥ 3` (más la regla del tercio anual) y el plus sale de otra columna con la franja del convenio en celda verde. Eliminar «el churrero que entra a las 4-5» de todas partes.

---

### A2 · ALTA — La FAQ pública y el §1.1 publican un techo de traspasos de 120.000 € que sale de dos anuncios que la propia lista negra prohíbe

**Afirmación literal:** §1.1 (`RESEARCH:60`): «Traspasos pedidos con sala **82.000-120.000 €** (`CUS-02`, `CUS-31h/i`)» · §3.6 (`:166`): «con sala y terraza en área metropolitana **82-120 k€**» · FAQ 4 (`:421`): «los traspasos que se piden hoy van de **16.000 a 120.000 €**».

**Problema.** Los dos anuncios que ponen el techo son `CUS-31h` (Sant Joan Despí, 107.000 €, 1.698 €/m²) y `CUS-31i` (Santa Coloma de Cervelló, **120.000 €**). L4 los marca como «**>2 años, reeditado “ayer”**» y «Precio inflado o stale» (`L4:115-116`). La lista negra del propio research dice: «**N-13** · Traspasos de más de 2 años reeditados como precio de mercado · Pedido sin cierre» (`RESEARCH:453`). Y la FAQ los presenta como «los que **se piden hoy**». Sin esos dos, el techo verificado con sala es **Vallecas, 82.000 €** (`CUS-02`; 95.000 € como techo pedido en `CHS-37b`), y la mediana baja de 571 a **500 €/m²**.

**Evidencia:** `guia-churreria-research-L4-sector-equipamiento.md:115-116` · `RESEARCH:60`, `:166`, `:421`, `:453`.

**Fix.** Sacar `CUS-31h/i` de cualquier rango y dejarlos solo como ejemplo de «pedido ≠ cierre» en la hoja «Traspaso vs Obra Nueva». FAQ 4: «de unos 16.000 € (churrería de barrio) a unos 82.000-95.000 € (con sala, en Madrid)». §1.1 y §3.6: «con sala, 58.000-95.000 € pedidos (`CHS-37c`, `CHS-37b`, `CUS-02`)». Añadir al gate del guion un `prohibido` con «120.000» y «107.000».

---

### A3 · ALTA — La salida del verano «cierra con media cuota del 676» no existe para casi ningún comprador: está exento del IAE, y cerrar julio y agosto no es abrir seis meses o menos

**Afirmación literal:** §3.5 (`RESEARCH:162`): «Valle de verano: tres salidas con evidencia — … ferias (`CUS-29`) o **cierre con media cuota del 676 si abre ≤ 6 meses** (`CUN-10`)» · libro 5 (`:296`): «resultado de julio-agosto en las tres salidas (**con media cuota del 676 si cierra**)» · cap. 17 (`:345`, `CUN-10`) · bonus, decisión 9 (`:306`, `CUN-10`) · D2/§2.1 fila 2 (`:94`: «676 y 675 pagan media cuota si abren ≤ 6 meses»).

**Problema, por dos lados:**
1. **El comprador no paga cuota.** `CHN-73`, ya verificado por la hermana: exentos del IAE «todas las personas físicas y las sociedades con cifra de negocios inferior a 1.000.000 €» (art. 82.1.c TRLRHL), además de los dos primeros periodos. Una churrería de 75 m² nunca llega a ese millón. Media cuota de cero es cero.
2. **Aunque pagara, no se cumple la condición.** La nota del 676 dice «permanezcan abiertos al público durante **seis meses o menos al año**» (leído hoy en el BOE). Cerrar julio y agosto deja **diez** meses abiertos. Y el 644.6, que el caso (a) también necesita para vender al peso (`CUN-14`), **no lleva** esa nota.

Además el propio research prohíbe hablar de esto: §2.4 (`:119`): «**No se puede decir** … cuotas del IAE».

**Evidencia:** `https://www.boe.es/buscar/act.php?id=BOE-A-1990-23930` (grupos 676 y 675, epígrafe 644.6) · `guia-chocolateria-verificacion-legal-2026-09-12.json` `CHN-73` · `RESEARCH:94`, `:119`, `:162`, `:296`, `:306`, `:345`.

**Fix.** Borrar la media cuota de las salidas del verano, del libro 5, del cap. 17 y de la decisión 9: el verano tiene **tres** salidas (cerrar, carta de verano, ferias), y en «cerrar» se pagan los fijos sin ingresos. La nota del 676 entra, si acaso, en una línea del cap. 10 («existe; con la exención de `CHN-73` casi nunca te toca») y en ningún Excel.

---

### A4 · ALTA — «El despacho va por declaración responsable» se publica sin la condición de obra de la propia Ley 12/2012, y esa condición choca con el conducto a cubierta que el research exige para freír

**Afirmación literal:** FAQ 7 (`RESEARCH:424`): «un despacho para llevar hasta 750 m² **va por declaración responsable**» · §2.1 fila 1 (`:93`): «declaración responsable, **sin licencia previa** hasta 750 m²» · `CUN-35` (`L3:47`) · D2 y libro 7 («¿Anexo de la Ley 12/2012 sí o no?», `:298`) · §2.4: es «argumento de venta» (`:118`).

**Problema.** El art. 3 de la Ley 12/2012, leído hoy, quita la licencia **de actividad** (3.1), pero acota las obras:

> «3. No será exigible licencia o autorización previa para la realización de las obras ligadas al acondicionamiento de los locales … **cuando no requieran de la redacción de un proyecto de obra** de conformidad con el artículo 2.2 de la Ley 38/1999 … 4. La inexigibilidad de licencia … **no regirá respecto de las obras de edificación** que fuesen precisas conforme al ordenamiento vigente».

El propio research dice que freír en Madrid exige campana y «**conducto de evacuación a cubierta**» (`CUN-23`), que la freidora no tiene exención (`CUN-24`), y que con más de 20 kW el local es de riesgo especial, con conductos EI 30 y registros (`CUN-26`). Un conducto que sube por fachada o patio hasta la cubierta es una intervención en el edificio. Puede necesitar proyecto (LOE art. 2.2), licencia de obra y el permiso de la comunidad. Y el art. 2.2 de la Ley 12/2012 saca del régimen cualquier actividad con «uso privativo y ocupación de los bienes de dominio público», como un conducto sobre la vía pública o una terraza. Es el mismo defecto que la refutación de la hermana tumbó en el 644.5: el argumento se publica **sin la condición que lo limita** (`guia-chocolateria-research-REFUTACION-2026-09-12.md`, A3).

**Daño.** El lector de la variante (b) lee «declaración responsable» en la FAQ, firma el alquiler y descubre después que el conducto necesita proyecto y licencia de obra. Es la sorpresa más cara del sector, y es justo la que la guía promete evitar («si ese local admite una freidora», `:376`).

**Evidencia:** `https://www.boe.es/buscar/act.php?id=BOE-A-2012-15595`, arts. 2.2, 3.3 y 3.4 · `RESEARCH:93`, `:118`, `:424` · `L3:47-50`.

**Fix.** En `CUN-35`, la FAQ 7, el cap. 06 y la primera fila del checklist: «la **actividad** de despacho (644.6, ≤ 750 m²) va por declaración responsable; **las obras no**: si la salida de humos necesita proyecto (casi siempre que hay conducto a cubierta), van con su licencia de obra y su técnico. Con terraza o elementos sobre la vía pública, autorización aparte». En el libro 7, añadir la fila «¿la extracción necesita proyecto? → licencia de obra» delante de «¿Anexo sí o no?».

---

### A5 · MEDIA — La síntesis pierde los 1,20 m de los filtros para aparatos de gas, y el caso de La Rueda fríe con gas

**Afirmación literal:** §2.1 fila 5 (`RESEARCH:97`): «conductos exclusivos EI 30, **filtros a > 0,50 m del foco**, inclinación > 45°».
**Problema.** L3 lo copió bien: «filtros a **>0,50 m** del foco (**1,20 m si son de parrilla o de gas**)» (`L3:134`). La síntesis se quedó con el número pequeño. La dotación B de La Rueda usa la freidora **de gas** EMPLK002 (`L4:163`) y la alternativa de alta fiabilidad es un fogón de gas natural (`CUS-33g`): a ese caso le tocan los **1,20 m**. Una campana montada a 0,50-1,20 m de un fogón de gas no cumpliría.
**Fix.** Copiar la condición entera en §2.1 y en `CUN-26` del guion; en el libro 1, celda «tipo de aparato (gas / parrilla / otro)» → distancia mínima del filtro 1,20 / 1,20 / 0,50 m, con los valores en celda verde.

### A6 · MEDIA — La excepción de la bombona pierde la palabra «móvil», que es la que la limita al puesto de feria

**Afirmación literal:** §2.1 fila 8 (`:100`): «una sola bombona GLP < 15 kg con flexible a un solo aparato **no es instalación receptora**» · libro 7 (`:298`: «bombona < 15 kg o instalación receptora») · bonus, decisión 4 «Gas o eléctrico (`CUN-28` …)» (`:306`).
**Problema.** La cita literal de `CUN-28` dice «a un solo aparato **de utilización móvil**» (`L3:133`). Una freidora fija en un local no es un aparato móvil, así que la excepción no sirve para (a) ni para (b). Tal como queda en la síntesis y en la decisión 4, se lee como una forma de abrir un local sin instalación receptora y sin la inspección quinquenal (`CHN-48`).
**Fix.** Restituir «de utilización móvil» y atar `CUN-28` solo a la variante (c). Para (a) y (b), la decisión 4 se plantea entre «gas con instalación receptora (inspección cada 5 años)» y «eléctrico (potencia contratada)».

### A7 · MEDIA — La horquilla salarial que entra al P&L puede quedar por debajo del SMI 2026, y la fuente secundaria ya lo está

**Afirmación literal:** §3.5 (`:156`): «Ofertas reales **1.300-1.600 €/mes bruto**» · L4 (`:217`): «3 personas = **3.900-4.800 €/mes** sin Seguridad Social», multiplicando por 12 · `CUS-56`: media de churrero «**1.343 €/mes · 16.116 €/año**», «churrero con experiencia **1.200 €**».
**Problema.** SMI 2026 = **17.094 €/año** (`CHN-67`), es decir, 1.424,50 €/mes en 12 pagas. Con 12 pagas, que es como L4 hace la cuenta, **1.300 €/mes = 15.600 €/año: por debajo del SMI**. Los 16.116 €/año de Jooble y los 1.200 € «con experiencia» (14.400 € en 12 pagas; 16.800 € incluso en 14) también lo están. Las ofertas no dicen el número de pagas (`L4:212-213`). Y la tabla de Madrid es de **2025** (`CUN-39`): su nivel V da 1.086,31 × 14 + 191,22 × 11 = **17.311,76 €**, solo un 1,3 % sobre el SMI 2026. Cualquier tabla provincial algo más baja que el lector meta saldría ilegal sin aviso.
**Fix.** En el libro 8 y en el P&L: coste anual por puesto = **MAX(salario del lector; SMI anual en celda verde)**, con semáforo «por debajo del SMI 2026». Las ofertas de JobToday solo como «rango de mercado, pagas sin declarar». `CUS-56` fuera del producto (fiabilidad baja y por debajo del SMI). La tabla de Madrid, etiquetada «2025, convenio vencido» hasta cerrar V-01.

### A8 · MEDIA — «La brecha ×4 entre Granada y el centro de Madrid es el dato» compara una ración SIN chocolate con un gasto por persona CON chocolate, y de años distintos

**Afirmación literal:** §3.2 (`:144`): «**La brecha ×4 entre Granada y el centro de Madrid es el dato**», sobre `CUS-15` (ración de 6 churros 1,20 €, 2026) y `CUS-19` («~5 € por persona **con chocolate**», 22-12-2024).
**Problema.** Son dos magnitudes distintas. Comparando lo mismo con la carta de Granada (`CUS-15`), churros con chocolate cuestan 1,20 + 2,00 = **3,20 €** en barra o 1,20 + 2,50 = **3,70 €** en terraza, frente a ~5 €: entre **×1,35 y ×1,6**, no ×4. Y `CUS-19` es de diciembre de 2024, sin actualizar. La conclusión («parámetro del lector») sobrevive; la cifra de cabecera, no.
**Fix.** «Con chocolate, de 3,20-3,70 € en Granada (2026) a ~5 € en el centro de Madrid (2024): la plaza mueve el ticket alrededor de un 50 %». El año va en cada fila de §3.2.

### A9 · MEDIA — El 50 % que el P&L usa por defecto como «margen» es la «rentabilidad» de una dueña, no un margen sobre materia prima: si entra en la línea de margen bruto y luego se resta el personal, la mano de obra cuenta dos veces

**Afirmación literal:** §3.3 (`:148`): el «un poquito más del 50 %» es «**rentabilidad tras más costes**»; «el P&L usa el del lector (**por defecto, 50 %**, coherente con el P&L de la hermana, que ya modela la línea de taza y churros al 50 %)» · D6 (`:512`).
**Problema.** La hermana usa ese 0,5 como **margen bruto** de la línea (`PyG 3 Años!C58`, leído hoy: «Margen bruto de la línea de taza y churros (%) · 0,5») y resta el personal aparte (`C59`). Si el 50 % es rentabilidad después de aceite y mano de obra, como el research dice que es, ponerlo en la casilla de margen bruto y restar luego la nómina cuenta la mano de obra dos veces. Además choca con el único dato de estructura con fuente: «Ingredientes y aceite ≈ 20 % de la facturación» (`CHS-33`, fiabilidad media), es decir, un 80 % sobre materia prima, y con el «>60 %» de Loomis.
**Fix.** El P&L calcula el margen bruto desde el escandallo del libro 3 (materia prima + aceite por ración), no desde un porcentaje. El 50 % de La Artesana queda solo como contraste en `3!Los Dos Márgenes`, con su definición incierta. Que la hermana lo use no lo valida: es otra razón para incluir `C58` en el parche D7 (B5).

### A10 · MEDIA — El ancla de precio y la FAQ 3 se apoyan en un curso de 290 € que nadie ha visto en su fuente

**Afirmación literal:** §11 (`:359`): «65 € es el **22 %** del curso de oficio más barato (**290 €**, `CUS-M05`)» · FAQ 3 (`:420`): «cursos presenciales (**290-1.290 €** en Madrid)» · §7 (`:235`): «dato de segunda mano porque su dominio redirige a otro».
**Problema.** La regla de la casa es «cada cifra lleva FUENTE (URL) … o se marca “sin fuente” y NO entra». Un precio cuyo dominio redirige a un sitio ajeno no tiene fuente abierta. Aun así ancla el precio y sale en una FAQ pública.
**Fix.** Ancla con lo verificable: los **1.290 €** (`CUS-M06`, dos anuncios), el canon de Churros Factory y la renta de 910 €/mes. FAQ 3: «cursos presenciales desde unos cientos de euros hasta 1.290 € en Madrid» o, mejor, solo «hasta 1.290 €». El 290 € entra cuando alguien abra la web de la academia.

### A11 · MEDIA — «Con un preparado que no cumple, ni “chocolate a la taza” ni “chocolate”» es una interpretación con nivel A, y la decisión 6 del bonus la vende como decisión resuelta

**Afirmación literal:** §2.1 fila 13 (`:105`): «el RD 1055/2003 define el **producto** …, no la bebida servida; con un preparado que no cumple, **ni «chocolate a la taza» ni «chocolate»**» · bonus, decisión 6 «Qué puedes llamar “chocolate a la taza”» (`:306`) · cap. 03.
**Problema.** La primera mitad es literal (`CUN-42`). La segunda no sale de ningún artículo citado: si la norma define el polvo o la tableta y **no** la bebida, de ella no se deduce qué nombre puede llevar la bebida en la carta. Para eso hay que pasar por la información al consumidor de alimentos no envasados (Rgto. 1169/2011 y RD 126/2015) y por la doctrina de denominaciones, y no está verificado. Puede ser la lectura correcta, pero no es nivel A. Y una «decisión resuelta» de bonus no puede descansar en ella.
**Fix.** Marcarla como **interpretación** para que el verificador legal la firme antes del guion (V-06, nueva). Mientras tanto, la decisión 6 se formula como «qué preparado compras y qué dice su etiqueta», no como «cómo puedes llamarlo».

### A12 · BAJA — El 25 % de polares se mide por cromatografía en columna: un medidor de mano es indicativo, no la prueba legal

`CUN-02` (`L3:64`) propone «lectura del medidor de polares» en el registro, y el libro 4 lleva el Testo 270 (`CUS-38`). El art. 6.3 fija el 25 % «determinado de acuerdo con el método analítico que figura como anexo 1» (cromatografía en columna). **Fix:** en el cap. 11 y en el libro 4, «el medidor de mano te dice cuándo cambiar; el 25 % legal se demuestra en laboratorio».

### A13 · BAJA — Lo «nuevo» del 644.6 ya lo afirmó la hermana

§1.3 (`:73`): «lo nuevo es que el **despacho 644.6 sí está dentro** (`CUN-09`, `CUN-35`), cosa que la hermana **no afirma ni niega**». `CHN-49b` dice: «incluye el grupo 644 completo —644.1, 644.2, 644.3, 644.4, 644.5 y **644.6**—». No hay contradicción, pero tampoco es novedad: citar `CHN-49b` como fuente del dato y `CUN-09` solo para la nota de churrería.

### A14 · BAJA — La parte B de la acrilamida no aplica «a las franquicias» sin más

§2.1 fila 4 y D12 (`:96`, `:518`): «franquicia, además parte B». El art. 2.3 pide además operar «siguiendo las instrucciones del explotador … **que suministra de forma centralizada** los productos alimenticios» (leído hoy). Una franquicia que no suministra centralmente la patata no entra. **Fix:** añadir la condición.

---

## B — NEGOCIO

### B1 · ALTA — El presupuesto de redactores está entre 0,7 y 2,6 M por debajo de lo que da la calibración medida de la hermana, y justifica el recorte con «capítulos más cortos» cuando los BLOQUES son más largos

**Afirmación literal:** §15.4 (`:495`): «Redactores · **30 bloques × 0,12-0,14** (capítulos más cortos que la hermana) · **3,60-4,20**» · total «≈ 9,95-10,9 M (central ≈ 10,4 M)» (`:499`).
**Problema.** La base medida (verificación 4) es **0,162 M por bloque** o, por palabra, 7,3 M / 51.900 palabras de guion = **≈ 141 tokens por palabra** (guion de la hermana sumado por mí: 37.900 + 3.500 + 10.500). Este producto tiene **44.300 palabras** de guion (33.000 + 3.500 + 7.800) en **30** bloques, y cada bloque es **más largo**: guía 1.571 palabras por bloque frente a 1.404, bonus 1.300 frente a 875 y business plan 1.167 frente a 583. Con cualquiera de las dos calibraciones:
- por bloque: 30 × 0,162 = **4,86 M**
- por palabra: 44.300 × 141 = **6,2 M**

frente a los 3,60-4,20 M del research. Así, el total pasa a **≈ 10,6-12,9 M** y roza la parada de los 13 M (D15) **antes** de contar esta refutación y la segunda ronda. La partida no redactora de F2+F3 también cae a la mitad de la de la hermana: 4,25-4,45 M frente a ≈ 8,7 M (16 − 7,3), con 8 libros frente a 9 y sin explicar el ahorro.
**Fix.** Rehacer §15.4 con 0,162 M por bloque como suelo (4,86 M) y presentar el total con su horquilla real. Si se quiere entrar en 10 M, aplicar **desde el diseño** las palancas que el propio research tiene (business plan en 2 bloques, fundir 05 y 09, libro 8 dentro de `6!Personal`, ≈ −0,5 M), o bajar el guion a ≈ 38.000 palabras. D3 (65 €) no depende de las palabras sino de los entregables (§11), así que esto no lo toca.

### B2 · MEDIA — «Ya ocupamos la posición 1 … y GSC lo confirma» no lo confirma: GSC no atribuye ninguna impresión del post a una consulta de apertura

**Afirmación literal:** §0 punto 3 (`:46`): «Ya ocupamos la posición 1 en `montar una churreria 2026` con el post propio (L2 §2.1), y **GSC lo confirma por page** (verificación 8)».
**Problema.** GSC por **query** para esa page, en la misma ventana de 90 días, devuelve **una sola consulta visible**: «cuánto presupuesto necesito», 1 impresión, posición 5,0. El resto queda anonimizado. Las 133 impresiones son de la page entera, con una posición media de 4,9. «montar churreria» (50/mes) y «como montar una churreria» (30/mes) suman ≈ 240 búsquedas en 90 días, y con una posición 1 en ellas solas la page tendría más impresiones de las 133 que tiene en total. La posición 1 es de **una captura de SERP** de la variante con «2026», sin volumen medido. En la SERP de «como montar una churreria» el post **ni siquiera aparece** entre los resultados listados (`L2:165`).
**Fix.** «El post aparece en primera posición para “montar una churreria 2026” (SERP del 3-oct, sin volumen medido) y suma 133 impresiones en 90 días; no está entre los resultados de “como montar una churreria”». No usar «posición 1» como argumento de canal en D13/D20 ni en §13.3.

### B3 · BAJA — «Fuera de España no hay demanda de apertura: ≤ 10/mes» lo contradice la propia tabla de L2 en México

§0 punto 2 (`:45`). En `L2:124-125`, México tiene «negocio de churros» **50** y «franquicia de churros» **50**: el mismo orden que «montar churreria» en España. La conclusión (sin captación LATAM) aguanta, pero la frase no. **Fix:** «≤ 10/mes para “montar/poner/abrir”; en México, ~50 para “negocio de churros” y “franquicia de churros”».

### B4 · BAJA — `fase8x-sustituir-banner.py --producto guia-churreria-chocolateria` no puede cambiar los tres banners del post en una pasada

§13.1 (`:392`) asigna los tres banners del post a tres productos en una sola invocación. El script cambia **un** banner por el producto del JSON más, opcionalmente, **un** `miswiring` (`fase8x-sustituir-banner.py:20-24`), y su gate exige que queden 3 banners. **Fix:** dos pasadas, o una con `miswiring` para la hermana y otra con su propio JSON para `pack-appcc`; o dejar el tercer banner como está. Declararlo en el plan de F3.

### B5 · BAJA — El parche D7 de la hermana se queda corto

D7 (`:513`) corrige el 85-90 % y el veredicto de `B68`. Cuando esta guía publique precios de churrera, freidora y extracción (`CUS-32…36`) y 115.000 € para Maestro Churrero, la hermana seguirá diciendo «Sin cifra» en `Variante del Formato!E38-E41` y «Sin cifra con id» en `E47` (leído hoy), y seguirá usando el 0,5 de A9 como margen bruto en `PyG!C58`. **Fix:** ampliar D7 con esas celdas, cada una con su id `CUS-*` o con un «véase la Guía de Churrería-Chocolatería».

---

## C — PRODUCTO

### C1 · ALTA — Dos ciclos entre libros impiden rellenarlos en un orden válido, y uno cuenta dos veces el fondo de maniobra

**Afirmación literal (§9.2, `:292-299`):** libro 1 toma «piezas por kg **(← 3)**» · libro 3 toma «precio del aceite **(← 4)**» · libro 4 toma «kg fritos/día **(← 1)**» · libro 2 toma «fondo de maniobra **(← 6)**» · libro 6 toma «Inversión Inicial **(← 2)**».
**Problema.**
1. **1 → 4 → 3 → 1.** Para tener el aceite por ración (4) hacen falta los kg fritos al día (1), que dependen de las piezas por kg (3), que a su vez necesitan el coste del aceite (4). Con la regla de familia («celda verde “cópialo del libro N” + fila de cuadre», `:284`) no hay ningún libro por el que empezar: el lector rellena uno con un valor provisional y el cuadre sale rojo hasta que itere a mano. Es el defecto C3 de la refutación de la hermana, ahora cerrado en círculo.
2. **2 ↔ 6, y el doble conteo.** Si el CAPEX (2) incluye el fondo de maniobra calculado en el plan (6) y el plan toma la inversión total del CAPEX, el fondo entra **dos veces** en la financiación del libro 6: una dentro de la inversión copiada y otra en su propia tesorería. Rompe «un concepto = una fuente».

**Fix.** Ordenar los libros como un grafo sin ciclos y escribir ese orden en la hoja «Instrucciones» de cada uno: **3** (escandallo con el precio del aceite **en su propia celda verde**, no tomado de 4) → **1** (capacidad) → **4** (aceite, toma kg/día de 1 y devuelve un € por ración que 3 **solo contrasta** en la fila de cuadre) → **5** → **8** → **2** (CAPEX **sin** fondo de maniobra) → **6** (calcula el fondo y suma CAPEX + fondo). Añadir a `gate_libros.py` una comprobación del grafo de «← N» declarado en las hojas, que aborte si encuentra un ciclo.

### C2 · MEDIA — Dos conceptos calculados dos veces: la demanda por franja (libros 1 y 5) y el punto muerto de las ferias (libros 5 y 6)

Libro 1: «Demanda por Franja · raciones/h por franja» · libro 5: «Franjas del Día · % por franja» y «Capacidad contra el Pico (← 1)» · libro 5: «**Punto Muerto por Evento**» · libro 6: «**Canales y Punto Muerto** (sala · para llevar · **ferias**)» (`:292`, `:296`, `:297`). La refutación de Pastelería y la de Chocolatería ya tumbaron conceptos calculados dos veces. **Fix:** la franja nace en 5 (reparto del día) y 1 la recibe como raciones/h; las ferias tienen su punto muerto **solo** en 5, y 6 toma su resultado anual como una línea de canal.

### C3 · MEDIA — El juego de datos deja «sin valor» justo los parámetros de los que dependen el resultado neto y el punto de equilibrio que el business plan tiene que dar

§9.1 (`:281`): «Sin fuente (verde, **sin valor presentado como dato**): absorción de aceite, vida del aceite, piezas por kg, churros/hora, curva mensual, mix de canales» · bonus 1 (`:305`): «**el resumen ejecutivo da el resultado neto, el margen y el punto de equilibrio**». Sin esos seis parámetros, La Rueda no tiene coste por ración, capacidad, ventas por mes ni reparto por canal, y los libros 3, 1, 5 y 6 salen vacíos. La curva mensual ya se resuelve con «12 coeficientes supuestos y declarados» (`:161`); el resto no. **Fix:** una regla única en el SPEC: «**supuesto declarado de La Rueda**», valor en celda verde con la nota «supuesto, sin fuente pública; pon el tuyo». No es un «dato» ni sale en el copy ni en la FAQ, pero permite que el caso cuadre. Listar los seis con su valor y su razonamiento en `datos_ejemplo.py` antes del guion.

### C4 · MEDIA — El capítulo 05 aplica en su ficha de visita las condiciones eliminatorias que el 06 y el 07 aún no han explicado

Cap. 05 → «1 · Ficha de Visita», con «eliminatorios: **conducto a cubierta, gas, potencia**» (`:292`, `:333`). La base de esas tres condiciones está en el cap. 06 (régimen de apertura) y en el 07 (humos, CTE, gas) (`:334-335`). La regla de la casa es que la decisión legal que aplica un xlsx tenga su capítulo **antes**. **Fix:** pasar la ficha de visita al final del 07 (o adelantar 06-07 delante del 05), y que el 05 se quede en metros y zonas con una remisión.

### C5 · MEDIA — La hoja «Comparativa de Aceites» no se puede construir con fuentes: hay un solo precio y la vida del aceite está en la lista negra

Libro 4: «Comparativa de Aceites · coste anual por aceite» (`:295`). Solo hay un precio de aceite (`CUS-23`, 2 €/L, sin decir de qué tipo), y la duración comparada es justo `N-7` («dura el doble»: ficha comercial, `:447`) y `N-20` (vida del aceite sin fuente). **Fix:** quitar la hoja, o convertirla en una plantilla de dos columnas «tu aceite actual / el que te ofrecen», con precio y días entre cambios **del registro del lector**, sin valores de ejemplo.

### C7 · MEDIA — El bonus de 12 decisiones es, tal como está, un índice: cada decisión es un capítulo, y dos capítulos aportan dos decisiones cada uno

Decisiones 1 y 8 → cap. 06 · 6 y 7 → cap. 03 · 2 → 04 · 3 → 08 · 4 → 07 · 5 → 14 · 9 → 17 · 10 → 16 · 11 → 12 · 12 → 19 (`:306` frente a `:327-349`). El research no dice qué aporta cada decisión que no esté ya en su capítulo, y el riesgo de desduplicación por capítulo ya costó ≈ 2,2 M en el Manual del Chef (`:325`). **Fix:** en el SPEC, cada decisión lleva **la resolución con los números de La Rueda** (qué eligió, con qué cifra del libro y cuál es el umbral para elegir lo contrario), y `puntos_por_epigrafe` prohíbe repetir la explicación del capítulo. La decisión 6 se reformula según A11.

### C6 · BAJA — La FAQ de compra incluye una pregunta de oficio y otra de buscador de empleo

§14 (`:414`): «Las de oficio … quedan fuera». La FAQ 6 («¿Cuántos churros salen de 1 kg de harina?», `:423`) es de oficio, y la segunda mitad de la 5 («¿Cuánto gana un churrero?», `:422`) es la de quien busca trabajo, y la respuesta no la contesta. **Fix:** FAQ 6 → «¿Los Excel parten de mi receta o de una receta vuestra?»; FAQ 5 → «¿Es rentable una churrería?».

---

## Resumen para la SPEC

| Id | Gravedad | Qué cambia en la SPEC |
|---|---|---|
| A1 | ALTA | `CUN-29` en dos figuras (trabajador nocturno ET 22-6 ≥ 3 h / plus de convenio); libro 8 con dos columnas; fuera «el que entra a las 4-5» |
| A2 | ALTA | Fuera `CUS-31h/i` de rangos; FAQ 4 hasta 82.000-95.000 €; `prohibido` 120.000 y 107.000 |
| A3 | ALTA | Fuera la media cuota del IAE de verano, libro 5, cap. 17 y decisión 9 (`CHN-73`) |
| A4 | ALTA | Ley 12/2012 art. 3.3-3.4 en `CUN-35`, FAQ 7, cap. 06 y 1.ª fila del checklist |
| B1 | ALTA | §15.4 con 0,162 M por bloque; total ≈ 10,6-12,9 M; palancas desde el diseño |
| C1 | ALTA | Grafo de libros sin ciclos; fondo de maniobra solo en 6; gate de ciclos |
| A5-A11 | MEDIA | 1,20 m gas · «móvil» · suelo SMI · ×4 → ~×1,5 · margen desde el escandallo · sin el 290 € · V-06 para la denominación de la taza |
| B2 | MEDIA | Sin «posición 1» como argumento de canal |
| C2-C5, C7 | MEDIA | Una fuente por concepto · supuestos declarados de La Rueda · ficha de visita tras el 07 · sin comparativa de aceites · decisiones con número propio |
| A12-A14, B3-B5, C6 | BAJA | Ver cada una |

**Estado: refutación ronda 1 cerrada. Queda una ronda (tope de 2), que debe comprobar las seis altas sobre el SPEC corregido.**

**Via: Claude Code**
