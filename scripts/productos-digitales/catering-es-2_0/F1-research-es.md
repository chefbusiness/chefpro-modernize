# Plan de Negocio Catering Temático Eventos ES → 2.0 · F1 research España

> Sesión Claude Code, 11-oct-2026. Una pasada: BOE leído hoy (curl + extracción de texto), Seguridad Social, DataForSEO
> (España) y prensa sectorial. Marca: ✅ = leído hoy en fuente oficial · 🟡 = fuente secundaria · [estimado] = sin fuente,
> criterio de kit. Molde: `planes-v2_0/contenido_plan_negocio_food_truck/a.py` (FT ES, línea A-β); claves de `0. Supuestos`
> de `grupo_a.SUPUESTOS_BASE`. Del ES v1 (línea B) **no se arrastra ninguna cifra** (inventario `business-plans-en-4/F1-inventario-delta.md` §2).

## 0. Los 5 hallazgos que mandan

1. **IVA 10 % a todo el catering con servicio, alcohol incluido**: art. 91.Uno.2.2.º LIVA ✅ no excluye el alcohol (la
   exclusión está en 91.Uno.1.1.º, entregas de bienes ✅); DGT V0499-26 🟡. 21 % solo en drop-off de alcohol/refrescos
   azucarados y en servicios facturados aparte. La recomendación de la CE de subirlo al 21 % (4-jun-2026) no es ley 🟡.
2. **Prohibido cocinar en casa para eventos** (RD 1021/2022 art. 13.5.b ✅) → la cocina autorizada es un coste del modelo
   (corrige L9 del ES v1).
3. **Registro autonómico por declaración responsable, no RGSEAA** (RD 1021/2022 art. 2.a y DF 1.ª, que reescribe el art.
   2.2 del RD 191/2011 ✅). El RD 3484/2000 de comidas preparadas está **derogado** ✅.
4. **Frío y caliente con cifras de BOE**: ≥ 63 °C · ≤ 4/8 °C · ≤ –18 °C · 60→10 °C en < 2 h (art. 30 RD 1086/2020 ✅);
   furgoneta isoterma/frigorífica conforme ATP también en transporte nacional (RD 237/2000 art. 1 ✅).
5. **Personal de eventos = fijo discontinuo** (art. 16.1 ET ✅): el eventual ocasional tiene un tope de 90 días/año por
   empresa (art. 15.2 ET ✅) y la factura de «freelance» con dependencia es falso autónomo (art. 1.1 ET). El ALEH V (art. 4
   ✅) mete el catering en hostelería → convenio provincial de hostelería.

## 1. Marco legal y fiscal España 2026

| Tema | Regla para el plan | Fuente · estado |
|---|---|---|
| IVA repercutido | 10 % catering con servicio (comida + bebida, alcohol incluido); drop-off: comida 10 %, alcohol/refrescos azucarados 21 %; alquileres y decoración facturados aparte 21 % | Ley 37/1992 art. 91.Uno.1.1.º y 2.2.º ✅ (texto consolidado act. 07-10-2026); DGT V0499-26 🟡 |
| IVA soportado | 21 % equipo/servicios; alimentos 10 % (algunos 4 %), recuperable mod. 303 | motor `iva_soportado` |
| Registro sanitario | Declaración responsable → registro autonómico de establecimientos minoristas; RGSEAA solo si suministras a otros establecimientos (actividad no «restringida») | RD 1021/2022 art. 2 y DF 1.ª ✅; RD 191/2011 art. 2.2 ✅ |
| Cocinar en casa | Prohibido para eventos y colectividades | RD 1021/2022 art. 13.5.b ✅ |
| Cocina central / compartida | La cocina tiene que estar autorizada y el operador inscrito; en cocina compartida, contrato de uso + inscripción propia del operador en esa dirección | regla general ✅; **detalle de cocina compartida por CCAA ❌ no verificado** |
| Higiene / APPCC | Autocontrol APPCC (Reg. CE 852/2004 art. 5), formación de manipuladores (anexo II cap. XII), alérgenos en no envasados (Reg. 1169/2011 + RD 126/2015) | RD 1021/2022 los cita ✅; reglamentos no releídos hoy |
| Temperaturas | ≥ 63 °C caliente · ≤ 4/8 °C frío · ≤ –18 °C · 60→10 °C en < 2 h | RD 1086/2020 art. 30 (redacción RD 1021/2022) ✅ |
| Transporte | Furgoneta isoterma/frigorífica conforme ATP, inspección periódica por OCA | RD 237/2000 art. 1-2 ✅; **qué alimentos exigen ATP (RD 2483/1986) ❌ no verificado** |
| IAE / CNAE | **677.9** «otros servicios de alimentación propios de la restauración» (la nota incluye catering y colectividades); alternativa 677.1; CNAE-2025 **56.21** (catering para eventos). Exento con INCN < 1 M € | 🟡 conversoriaecnae / gestoria247 (RDLeg 1175/1990 no releído) |
| Forma jurídica | SL unipersonal (capital mínimo 1 €, Ley 18/2022) como el molde FT; autónomo con tarifa plana 80 €/mes 12 meses como alternativa | conocido, no releído hoy |
| Seguridad Social empresa 2026 | CC 23,60 % · desempleo 5,50 % (indef./fijo disc.) o 6,70 % (temporal) · FOGASA 0,20 % · FP 0,60 % · MEI 0,75 % = **30,65 % + AT/EP** (CNAE 56 ≈ 1,50 % [no releído]) ≈ **32,2 %** → el **33 %** del motor vale. Base mín. 1.424,40 €/mes | seg-social.es ✅ |
| Contratos < 30 días | Cotización adicional **33,62 €** por baja (3 × base mín. diaria grupo 8 × 23,60 %; cuadra al céntimo) → otro motivo para el fijo discontinuo | LGSS art. 151; importe 🟡 (Europa Press) + cálculo ✅ |
| Salarios convenio | Madrid (ultraactividad 2025 en 2026, BOCM 06-04-2024): ayudante cocina ≈ 1.127-1.146 € base, camarero ≈ 1.160 € (2.ª) + plus convenio 191,22 €, **14 pagas**; SMI 2026 17.094 €/año (motor) | 🟡 dos webs con cifras que difieren ~20 €; BOCM no abierto |
| Personal extra | Fijo discontinuo (art. 16 ET) o ETT; nunca facturas de autónomo; eventual ocasional ≤ 90 días/año | ET arts. 1.1, 15.2, 16 ✅ |
| Seguros | RC explotación + producto con **intoxicación alimentaria** (≥ 600.000 € como pedía el checklist v1), furgoneta comercial, equipos | práctica; importes [estimado] |
| Alcohol | Sin licencia estatal de venta: va dentro del servicio de hostelería en un espacio con licencia (finca, hotel, local); prohibido a menores (leyes autonómicas); evento en vía pública → autorización municipal; «descorche» si el cliente pone la bebida | ❌ sin fuente oficial leída hoy |
| Cobro a empresas | Plazo legal máximo 60 días (Ley 3/2004 art. 4) | conocido, no releído |
| IS / IRPF | IS 15 % los 2 primeros ejercicios con base positiva, luego 25 % (micro/reducida dimensión con tipos graduales desde 2025: lo explica la nota del motor); autónomo: IRPF estimación directa + mod. 130 (20 %) | motor `is_nueva`/`is_general`; no releído hoy |

## 2. Benchmarks España

| Dato | Valor | Fuente |
|---|---|---|
| Boda: coste total medio | **25.183 €** (+6 % vs 2024); 53 % banquete y espacio; gasto **225 €/invitado** (total de la boda, no solo el menú) | Bodas.net, Informe del Sector Nupcial 2026 (act. 12-06-2026) 🟡 |
| Boda: invitados | **115** (millennials) · 118 (Gen Z) · 82 (Gen X) | ídem 🟡 |
| Boda: menú por comensal | 70-150 €, ≈ 120 € con barra libre (IVA incl.); banquete + espacio ≈ 119 €/inv. [derivado: 225 × 53 %] | resumen de buscador 🟡 (no confirmado en la página) |
| Empresa | coffee break 6,35-9,92 € + IVA (tarifa UPF 2026, suelo) · almuerzo de trabajo ≈ 43,50 € (hotel Madrid) · cóctel 30-45 € | 🟡 buscador, no abiertos · cóctel [estimado] |
| Eventos/año · food cost · personal | 100-150 · 28-32 % · 33-38 % de ventas | [estimado] (caso US 30 % / 35,9 %) |
| Margen neto hostelería | 7-8 % | 🟡 lexpress-franchise (sin fuente primaria) |
| Sector | 4.885 M€ en 2025 (+6,0 %), ≈ 950 empresas — perímetro probablemente catering + colectividades | DBK vía lexpress-franchise 🟡 |
| Cocina compartida / obrador | 20-35 €/h o cuota 1.500-2.500 €/mes con cámara y almacén | [estimado] — no se encontró tarifa pública (el «114 €/h» de Barcelona es de espacios para eventos y talleres, **no** de obradores) |
| Furgoneta frigorífica | Usada (Trafic 2021-22): 18.000-21.950 €; nueva 40.000-50.000 €; renting 600-900 €/mes | anuncios de Wallapop/motor.es 🟡 · resto [estimado] |
| Seguros | RC media: 120 € (autónomo) / 575 € (empresa); catering con intoxicación 600-1.200 € | BBVA 🟡 · [estimado] |
| Plataformas B2B | Sin un marketplace dominante tipo ezCater en España; escaparates de pago (Bodas.net, Zankyou) y fincas que cobran canon al catering externo | ❌ no verificado (ni comisiones ni cuotas) |
| Ratio de personal | 1 camarero/10-12 inv. sentados · 1/20-25 en cóctel | [estimado] |

## 3. Caso España 2.0 (molde FT ES, motor eventos × €/invitado × invitados)

**Mezcla que sostiene el promedio** [estimado; reparto 35 % social / 65 % empresa del ES v1, **por eventos**]:

| Tipología | Canal | Eventos | Inv./ev. | €/inv. sin IVA | Ventas |
|---|---|---|---|---|---|
| Coffee break, desayuno y almuerzo de trabajo | Empresa | 35 | 35 | 16 | 19.600 |
| Cóctel o presentación con estaciones en directo | Empresa | 35 | 80 | 40 | 112.000 |
| Comida/cena de empresa y Navidad | Empresa | 15 | 100 | 62 | 93.000 |
| Bodas (cóctel + banquete + barra 2 h) | Particular | 15 | 110 | 98 (≈ 108 con IVA) | 161.700 |
| Comuniones, cumpleaños, aniversarios | Particular | 30 | 45 | 48 | 64.800 |
| **Total** | 65 % empresa | **130** | **65,6** | **52,9** | **451.100** |

Empresa = 65 % de los eventos y ≈ 50 % de las ventas. El caso redondea a **130 × 65 × 53 € = 447.850 €** a régimen.

| Clave molde (celda) | Rótulo catering | Valor | Fuente |
|---|---|---|---|
| `cubiertos_dia` B4 | Eventos al año (año 1, a régimen) | **130** | mezcla [estimado] |
| `ticket_medio` B5 | Precio medio por invitado SIN IVA | **53 €** | mezcla [estimado] |
| `dias_apertura` B6 | Invitados medios por evento | **65** | mezcla; boda 110 vs Bodas.net 115 🟡 |
| `crec_a2` / `crec_a3` · líneas comida / bebida | Crecimiento de eventos · peso de ventas | 12 % / 8 % · 82 % / 18 % | [estimado] |
| `coste_comida` / `coste_bebida` | Mercancía de comida / de bebida | 30 % / 28 % | [estimado] |
| `pct_consumibles` | Desechables, gas de estaciones, hielo | 3 % | [estimado] |
| `pct_delivery` / `comision_delivery` | Ventas vía intermediarios (fincas con canon, wedding planners, agencias) / comisión | 20 % / 10 % | [estimado] — ⚠️ ver §5-D1 |
| `comision_tpv` | Cobro (transferencia mayoritaria) | 0,5 % | [estimado] |
| `alquiler_mes` (rótulo fijo del motor) | Cuota de cocina central compartida (≈ 80 h, cámara, almacén, plaza de furgoneta) | **2.000 €** (fianza 2 meses, 1 mes previo) | [estimado] |
| `suministros_mes` | Gas y consumos propios (la cocina incluye luz y agua) | 150 € | [estimado] |
| `seguros_ano` | RC + producto/intoxicación ≥ 600.000 € (900) + furgoneta (1.000) + equipos (300) | **2.200 €** | [estimado] |
| `pct_varios` | Combustible de la furgoneta + imprevistos | 3 % | [estimado] |
| `recursos_propios` · `prestamo` | 35.000 € · **105.000 €** (calibrar en F2 con la necesidad real) | — | [estimado] |
| `tipo` · `plazo` · `carencia` | 6,5 % · 6 años · 1 | — | [estimado] (= FT ES; línea ICO/bancaria) |
| `meses_fondo` | 3 | — | molde |
| `vida_obra` (vehículo) · `vida_maquinaria` | 8 · 10 años | — | art. 12.1 LIS: transporte 16 %, maquinaria 12 %, mobiliario 10 % (= FT ES) |
| `pct_bebida_alc` · `iva_bebida` | 65 % · **10 %** | — | [estimado] · art. 91.Uno.2.2.º ✅ |
| `aforo` → | Capacidad máxima por evento (informativo) | 250 | [estimado] |
| `rampa_mes1` · `meses_rampa` | 0,55 · 6 (bodas reservadas con meses; empresa lenta) | — | molde |
| `dias_cobro` · `dias_pago` | **25** (50 % empresa a 45 días + particulares prepagados a 0) · 30 | — | [derivado]; tope de 60 días Ley 3/2004 |
| `salario_convenio` | 0 + nota «copia tu tabla provincial» (Madrid ≈ 1.337 €/mes en 14 pagas 🟡) | — | como el FT ES |

**Política comercial** (del ES v1, válida): anticipo del 40 % para bloquear la fecha y el resto 7 días antes; cancelación a
más de 21 d sin coste del servicio / 21-7 d 50 % / < 7 d 100 %; empresas a 30-60 días con factura; prueba de menú cobrada y
descontable. El molde no modela anticipos (`dias_cobro` ≥ 0): **conservador**.

**Plantilla** (`PLANTILLA`: puesto, n, € brutos/mes en 14 pagas, jornada) [estimado, por encima del SMI y de las tablas 🟡]:
propietario/a, chef ejecutivo, ventas y degustaciones **1 × 2.000 × 1,0** · jefe/a de cocina de producción **1 × 1.700 ×
1,0** · ayudante de cocina y conductor/a **1 × 1.400 × 1,0** · coordinador/a de eventos y maître (fijo discontinuo) **1 ×
1.600 × 0,5** · equipo de evento: camareros, barra y cocineros de estación (fijos discontinuos) **7 × 1.400 × 0,29** →
bruto 122.388 € + SS 33 % = **162.776 €/año (36,3 %)**. Cobertura: 7 × 0,29 × 1.780 h ≈ 3.610 h frente a 130 eventos ×
4 extras × 7 h = 3.640 h (99 %).

**Inversión** (15 partidas, 67.000 €) [estimado salvo la furgoneta 🟡]: furgoneta frigorífica usada con ATP **22.000** ·
rotulación y estanterías 1.500 · contenedores isotérmicos GN y carros 3.500 · equipo de producción propio (GN, roner,
sondas, básculas, cuchillería) 4.000 · **estaciones temáticas portátiles** (3 módulos con inducción, plancha, wok) 9.000 ·
chafing dishes y expositores de buffet 3.500 · menaje base para 150 pax 6.000 · mantelería y uniformes 2.000 · mobiliario
de evento (mesas altas, barra plegable) 2.500 · web, fotos, marca y dossier de menús 4.000 · software + tablet + datáfono
1.200 · constitución SL 1.000 · declaración responsable, APPCC, alérgenos y formación 1.800 · stock inicial 2.000 ·
lanzamiento (ferias de novios, directorios, degustaciones) 3.000. **Necesidad ≈ 140.000 €** con fianza 4.000, mes previo
2.000, imprevistos 8 % sobre la furgoneta 1.880, IVA soportado ≈ 12.000 y fondo de 3 meses ≈ 53.200.

**Fijos** (`FIJOS_EXTRA`, €/año) [estimado]: asesoría fiscal-laboral (nóminas de fijos discontinuos) 3.000 · marketing
(escaparates de bodas, Google Ads, 2 ferias, LinkedIn) 9.000 · software de eventos, CRM y teléfono 1.800 · furgoneta
(mantenimiento, ITV, inspección ATP) 1.500 · lavandería de mantelería 3.000 · **degustaciones a clientes** 3.000 ·
residuos 400 · PRL 450 = 22.150. Fuera la SGAE (la música es del espacio).

**Cuenta a mano, a régimen** (F2 recalcula): ventas 447.850 · mercancía 29,6 % · variables totales 38,1 % → contribución
61,9 % (277.000) · personal 36,3 % · cocina 5,4 % · resto de fijos 26.150 → **EBITDA ≈ 64.100 (14,3 %)** · amortización ≈
6.300 · intereses ≈ 6.800 → antes de impuestos ≈ 50.900 (11,4 %). Cuota post-carencia ≈ 25.300 €/año → **DSCR ≈ 2,5**.
**Break-even ≈ 103 eventos/año** (106 con intereses) → **holgura ≈ 21 %** (≥ 15 %). Año 1 con rampa ≈ 85-90 % de la
actividad → EBITDA ≈ 23-36 K, positivo.

**Estacionalidad** (ene→dic, = 100) [estimado; bodas may-oct, comuniones en mayo, Navidad de empresa, agosto flojo]:
4,0 · 5,5 · 7,0 · 7,5 · 10,5 · 12,0 · 9,0 · 5,0 · 11,0 · 10,0 · 7,0 · 11,5 %. **Escenarios**: pesimista 105 eventos ·
50 € · 60 inv.; optimista 150 · 57 · 70. **Umbrales propuestos**: margen bruto ≥ 65 %, mercancía ≤ 33 %, **personal ≤ 38 %**
(catering es intensivo en mano de obra), cocina ≤ 7 %, neto ≥ 4 %.

## 4. Demanda y SERP (DataForSEO España, 11-oct-2026)

Volúmenes/mes: catering para eventos **1.000** · empresa de catering 590 · catering empresas 480 · catering bodas
390 · precio catering por persona 70 · cuánto cuesta un catering para 100 personas 30 · cómo montar un catering 20 ·
plan de negocio (de) catering, montar empresa de catering, precio catering boda por persona, registro sanitario catering 10.
La intención «montar/plan de negocio» es pequeña (≈ 50/mes sumada); el volumen está en la demanda de clientes. SERP
«montar un catering»: 17 orgánicos, local pack, vídeo. **PAA (guion de la FAQ)**: ¿Es rentable un negocio de catering?
· ¿Qué se necesita para montar un catering? · ¿Cómo armar un catering para 100 personas? · ¿Cuánto se cobra por un
servicio de catering? · ¿Cuánto vale un catering para 100 / 50 personas? · ¿Cuánto se gana en catering? · ¿Cómo calcular
el catering para 30 personas? **Hueco**: los primeros resultados (gestordecocina 2023, gasma, curso-manipulador,
emprendedores 2016) siguen citando «licencia de actividad clasificada», «salida de humos» y la «autorización sanitaria de
funcionamiento»; ninguno cita el RD 1021/2022, la prohibición de cocinar en casa para eventos ni el fijo discontinuo.

## 5. Sin verificar y decisiones para la SPEC

- ❌ Cocina compartida: tarifas reales y cómo se inscribe cada operador por CCAA · qué comidas exigen vehículo ATP (RD
  2483/1986) · alcohol en eventos (sin norma leída) · AT/EP del CNAE 56 · tablas del BOCM (dos fuentes secundarias
  discrepan ~20 €) · cuotas de Bodas.net/Zankyou y cánones de fincas · precios de coffee break y almuerzo (de buscador).
- **D1 · `pct_delivery` reutilizado como «intermediarios»**: en el motor el alcohol del canal delivery va al **21 %**
  (entrega de bienes). Para intermediarios eso es falso (siguen siendo servicio, 10 %). O se neutraliza esa rama, o el canal
  se rotula «drop-off sin servicio» (donde el 21 % sí es correcto) y el canon de fincas va a `pct_varios`. Recomiendo la
  segunda: cero cambios de motor.
- **D2 · Anticipos**: `dias_cobro` no admite negativos. Se modela 25 días (conservador) y la nota lo dice.
- **D3 · Personal de evento**: va como plantilla fija discontinua con jornada parcial (el molde ES no tiene cobertura por
  evento). En el pesimista el coste real baja; la nota lo dice.
- **D4 · Cifras prohibidas (heredadas del ES v1)**: 173 eventos · 2.200/4.500 € de ticket · 10.560 € · 8.520/21.410/54.440 € ·
  margen del 50-55 % · «14 eventos/mes» · «5.500/11.500 €» · «sin licencia de actividad clasificada».

Fuentes: [Ley 37/1992](https://www.boe.es/buscar/act.php?id=BOE-A-1992-28740) · [RD 1021/2022](https://www.boe.es/eli/es/rd/2022/12/13/1021/con) · [RD 237/2000](https://www.boe.es/eli/es/rd/2000/02/18/237/con) · [ET](https://www.boe.es/eli/es/rdlg/2015/10/23/2/con) · [ALEH V](https://www.boe.es/diario_boe/txt.php?id=BOE-A-2015-5613) · [Seg. Social 2026](https://www.seg-social.es/wps/portal/wss/internet/Trabajadores/CotizacionRecaudacionTrabajadores/36537) · [DGT V0499-26](https://primeralecturaediciones.com/?p=20250411) · [CE IVA](https://www.copilotgestoria.com/blog/iva-hosteleria-21-bruselas-2026-guia-gestorias) · [IAE 677.9](https://www.conversoriaecnae.es/iae/6779/otros-servicios-alimentacion-restauracion)
· [Bodas.net 2026](https://www.bodas.net/articulos/cuanto-cuesta-banquete-boda--c8700) · [Convenio Madrid](https://turnozo.com/es/blog/tablas-salariales-hosteleria-madrid) · [< 30 días](https://www.bolsamania.com/noticias_print/economia/economialaboral--la-penalizacion-a-contratos-temporales-de-menos-de-30-dias-sube-hasta-los-3362-euros-un-31-mas--22217128.html) · [DBK vía lexpress](https://lexpress-franchise.com/es/articulos/montar-catering/) · [Furgonetas](https://www.motor.es/segunda-mano/renault/trafic/) · [RC BBVA](https://www.bbva.com/es/salud-financiera/que-es-y-cuanto-cuesta-un-seguro-de-responsabilidad-civil-para-autonomos-coberturas-obligatoriedad-y-precios/)
