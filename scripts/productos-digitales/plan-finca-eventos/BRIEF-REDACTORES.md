# Finca de Eventos y Bodas ES 1.0 — brief de los redactores del plan de negocio (docx)

> Sesión Claude Code, 25-oct-2026. SPEC: `SPEC.md` D2, D4, D5, D10, D11 · `F2-NOTAS.md` §2 y §7. Dos tandas en paralelo, un
> redactor por tanda: **`fin_es_a`** = §1-5 (29 párrafos, ≈ 2.950 palabras) · **`fin_es_b`** = §6-10 (32 párrafos,
> ≈ 3.765 palabras). Entrada: `tandas/<tanda>.entrada.json`. Salida: `textos/<tanda>.json` = `{"<i>": "<párrafo>", …}`
> con TODOS los `i`.

## Qué es el producto

Plan de negocio de una **finca de eventos y bodas** (casa o masía, jardín, salón y carpa de plan B; aforo de 300 personas)
en una **finca ARRENDADA con edificaciones existentes** (no se compra: comprarla son 1-3 M€) o cedida por la familia con
renta de mercado, con un **catering EXCLUSIVO CONCESIONADO que paga canon**. La finca factura al cliente el espacio y los
servicios del evento (ceremonia, mobiliario, coordinación, limpieza, aparcamiento) con IVA del 21 %; el catering factura
directamente al cliente el menú y la barra (10 %) y paga a la finca un canon (supuesto editable: «negócialo»; IVA del 21 %).
La finca **no tiene cocina de producción ni brigada**: camareros y cocina los pone el catering, y la seguridad alimentaria
del menú es suya. Caso: **120 eventos al año** (30 bodas, 35 de empresa, 40 celebraciones privadas, 15 pequeños). Catering
propio y «solo alquiler» no tienen Excel: van en el Word (§2 y §10) como alternativas razonadas; el catering propio es para
hosteleros, a quienes se remite al Plan de Negocio de Catering Temático para Eventos. Es producto NUEVO (no hay versión
anterior).

**Lector**: alguien con una finca familiar o que quiere arrendar una para hacer eventos, o un hostelero que valora este
modelo frente al catering propio. Probablemente no es hostelero y va a pedir un préstamo. **Tono**: cercano y profesional,
**tuteo**, **español de España**, frases claras, sin relleno ni superlativos vacíos ni anglicismos innecesarios (wedding
planner y team building, sí, porque son los del oficio). Lo que no sabemos se dice («compruébalo en tu ayuntamiento, tu
comunidad o tu asesoría»); no se inventa nada.

## Reglas (las comprueba `python3 scripts/productos-digitales/plan-finca-eventos/tandas_docx.py check --tanda <tanda>`)

1. **Un párrafo por ranura**, en prosa: sin saltos de línea, viñetas, títulos ni Markdown. Longitud: la de
   `palabras_objetivo` ± 20 % (el check avisa fuera de 70-135 %).
2. **Toda cifra del Excel va como token** `{ASI}`, copiado tal cual de `tokens`. Ni importes, ni porcentajes, ni eventos,
   invitados ni precios del caso tecleados a mano: el Excel se puede recalcular y el documento tiene que seguirlo. Escribe
   la unidad que ya trae el token (no añadas «€» ni «%»). `{PAYBACK}` es texto («Más de 3 años»): no le añadas «años».
   `{MES_SALDO_MINIMO_NOMBRE}` es el nombre del mes. `{CARENCIA}` y `{PLAZO_PRESTAMO}` son solo el número: «{CARENCIA} año
   de carencia», «{PLAZO_PRESTAMO} años». `{FIANZA_MESES}` y `{MESES_FONDO}` también (escribe «meses»).
3. **Cifras que SÍ puedes escribir**: artículos y normas de la pista §9; los datos del INE y de Bodas.net de la pista §3 con
   su fuente (Bodas.net es la encuesta a sus usuarios: «según Bodas.net»); las búsquedas de la pista §3; los precios de
   escaparate de las pistas §2 y §3 como tales; la mezcla del caso (30 bodas de 120 invitados a 47 €, 35 de empresa de 80 a
   34 €, 40 privadas de 70 a 29 €, 15 pequeñas de 40 a 30 €, precios sin IVA); la comida testigo (más de 40 personas,
   100 g, 4 °C o −18 °C, 7 días); los umbrales de autoprotección (1.000 y 5.000 personas); los 55/55/45 dBA solo si los
   citas del RD 1367/2007; las 84 tareas del checklist (12/16/15/13/14/14). Cualquier otra cifra, o es token o no va. El
   check avisa de cada cifra escrita que no está en su lista: revísalas una a una.
4. **Prohibido** (el check lo caza): «RD 393/2007» (derogado: la norma es la Directriz Básica, Orden INT/1068/2026), «carné
   de manipulador» (salvo para decir que ya no existe), «España 2026» como sello, «freelance», «validado/a»,
   «tarifa plana», «CNAE», «licencia de apertura», «RGSEAA» sin matiz, «versión 1.1/2.2» o «versión anterior»; el 10 %
   para todo el paquete; el canon del 12 % como dato (es un supuesto: «negócialo»); restos de otros moldes: food truck,
   camión, ventanilla, panadería (pan, harina, hornada…), heladería (helado, obrador, vitrina, cubeta…), parrillero y
   catering propio (parrilla, brasa, carbón, furgoneta, remolque, cocina central, drop-off); frases del motor sin
   traducir: «el local», «del local», «en sala», «ticket», «delivery», «cubierto» y «comensal» (usa «invitado»; para la
   auditoría del canon, «el número de invitados servidos»), «clientes/día», «días de apertura»; y concordancias mal
   hechas de «la finca» (femenino: «la finca arrendada», nunca «el finca»). SÍ puedes escribir «generador» (grupo
   electrógeno) y «aparcamiento» (el de los invitados), que aquí son legítimos.
5. **«Quince años»** en letra, nunca «15 años» con cifra (choca con el censo de biografías antiguas). Vale para el
   arrendamiento y para cualquier otra mención.
6. **Legal**: solo lo de la pista §9, con su cita; es el único marco que se afirma. Las 4 comunidades (Madrid, Andalucía,
   Cataluña y C. Valenciana) con su artículo; el resto, «pregunta en urbanismo qué figura usa tu comunidad». **No vender
   fechas sin licencia** y condición suspensiva en el arrendamiento. Seguro obligatorio: sin cifras salvo Andalucía, y
   como «orientativo». IVA: espacio y canon al 21 %, menú del catering al 10 %; un precio único con todo al 10 % es
   arriesgado (precio propio o consulta vinculante). Todo lo que no esté en la pista: «compruébalo en tu ayuntamiento, tu
   comunidad o tu asesoría». Nunca cifras de ordenanzas ni de tasas locales.
7. **El año 1 (§8)**: cuenta **120 eventos completos**. El texto explica que solo es posible si las fechas de la primera
   temporada se venden **durante los meses de licencia y obra**, y remite al **escenario pesimista del Excel** si no se
   consigue. **Nunca digas que el año 1 da pérdidas** ni que sale «en torno a cero»: el Excel no lo dice (neto del año 1
   = `{NETO_A1}`) y el fondo de maniobra aguanta la caja del primer año. El riesgo real es de ocupación: por debajo de
   `{BE_EVENTOS_ANO_CAJA}` eventos del tamaño medio no hay caja.
8. **Crecimiento y caja (§8)**: el crecimiento de los años 2 y 3 se cuenta en **eventos equivalentes**
   (`{EVENTOS_EQUIVALENTES_A2}` y `{EVENTOS_EQUIVALENTES_A3}`), con el mismo precio por invitado; en el libro lo que crece
   es el tamaño medio del evento (`{INVITADOS_EVENTO_A2}`, `{INVITADOS_EVENTO_A3}`), pero el lector lo entiende mejor en
   eventos. El equilibrio se da en eventos (`{BE_EVENTOS_*}`). La holgura de caja `{HOLGURA_CAJA}` es la del primer año
   (de carencia); desde el segundo se cita `{HOLGURA_CAJA_A2}` con `{BE_EVENTOS_CAJA_A2}`, y en el tercero
   `{HOLGURA_CAJA_A3}` con `{BE_EVENTOS_CAJA_A3}`: son los años que hay que vigilar. Cita DSCR, saldo mínimo y su mes.
9. **Mes 1 = marzo**: cuando hables de tesorería, saldo mínimo o estacionalidad, dilo así («el mes 2, abril») y explica
   por qué: las bodas se reservan con 12-18 meses, la rampa es larga y el primer invierno hay que atravesarlo con el
   fondo de maniobra.
10. **Intermediarios**: `{INTERMEDIARIOS_PCT}` de las ventas llegan por wedding planners y agencias, con comisión de
    `{COMISION_INTERMEDIARIOS}`. **Canon**: un supuesto editable; cada punto vale `{CANON_PUNTO}`. **Plantilla**: sin
    camareros ni cocina; fijos discontinuos (art. 16 ET), nunca autónomos que te facturan.
11. **Fuentes por párrafo**: `molde_ft_es` es el párrafo del food truck que ocupa esa ranura: úsalo SOLO como medida de
    longitud y registro, nunca su contenido. `gemela_formato_heladeria_es` es el párrafo de la Heladería ES 1.0 en la misma
    ranura: sirve para ver **cómo** se escribe una ranura con tokens y qué tipo de contenido le toca (resumen, mercado,
    equipo, cifras…), nunca su contenido (helado, obrador, vitrina, temporada de verano). El research
    (`F1-research-finca.md` §0-§3 y §6) y `F2-NOTAS.md` son material de apoyo: si algo no está en la pista, no lo afirmes.
    La pista de la sección manda.
12. **Ortografía impecable** (tildes, «¿», comillas «»), artículo delante de los porcentajes («un 30 %», «el 10 %»), «−18 °C»
    con el signo menos y espacio antes de «°C», «Mes 1» con mayúscula cuando se refiera a la columna del Excel.

## Cómo trabajar

Lee la entrada entera (secciones con su pista, modelo, tokens y párrafos), escribe la tanda completa en
`textos/<tanda>.json`, pasa `python3 scripts/productos-digitales/plan-finca-eventos/tandas_docx.py check --tanda <tanda>`
desde la raíz del repo y corrige hasta 0 errores (los avisos de longitud y de cifra escrita, revísalos uno a uno). No
toques ningún otro fichero. Devuelve: ruta, nº de párrafos y palabras, y la salida del check. El ensamblado
(`docx_fin_es.py`) corre después en el VPS y añade los gates de 10 H1, A4, ≥ 6.000 palabras, 0 tokens, 0 no latinos y
0 prohibidos.
