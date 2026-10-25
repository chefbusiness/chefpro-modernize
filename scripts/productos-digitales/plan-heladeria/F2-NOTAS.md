# Plan de Negocio: Heladería Artesanal ES 1.0 — F2 · calibración, caso final y revisión

> Sesión Claude Code, 25-oct-2026. SPEC: `SPEC.md` (D1-D18). Revisión adversarial final: una pasada, tres lentes (cifras;
> legal y sanitario; editorial y comercial), **0 B / 7 M / 17 m**, todos aplicados en una ronda. Código en el Mac; motor,
> xlsx y docx en el VPS (`/root/wt-heladeria`, venv `/root/venv-guias`, scratch `/root/tmp-hel-f2/`).

## 1. Calibración (lo que se movió respecto del research para pasar los gates D9 y la demo del motor)

- **Préstamo 125.000 → 129.000 €**: la necesidad de caja del libro (183.170 €) sale algo más alta que la cuenta a mano del research (IVA de la inversión y fondo de maniobra). Con 55.000 € propios, la diferencia es de +830 € (0,5 %).
- **Vida de la maquinaria 9 → 10 años**: cumple también el coeficiente del mobiliario (10 %) y abre la ventana de la demo §2.11.5.
- **`PyG!G13` por VALOR** (8,2 % de IVA soportado de la compra de comida): en la panadería era fórmula; la semilla escribe el valor para que el motor no la cuente como fórmula perdida.
- **Umbral de margen bruto 70 %** (research: 72 %): el caso da 71,8 % y gelatomaps publica 60-70 %.
- **Pagas extra en los meses 5 (julio) y 10 (diciembre)** de la tesorería: el Mes 1 es marzo (SPEC D6).

## 2. Cifras finales del caso (`cifras_caso_es.json`, 122 tokens, D9 VERDE)

- **Actividad**: 143 clientes/día × 4,90 € sin IVA × 310 días. Ventas 217.217 / 234.594 / 246.324 €. Margen bruto 71,8 %; mercancía 20,5 %; personal 82.207 € (37,8 %) → 88.207 → 94.207 €; fijos 141.162 €.
- **Resultado**: RAI 14.800 €; neto 12.580 € (5,8 %) / 18.085 € (7,7 %) / 18.606 € (7,6 %).
- **Inversión**: 117.150 € de partidas + 5.100 € de fianza + 3.400 € de renta previa = 125.650 €; + 32.624 € de fondo = 158.274 €. IVA 24.896 €. Necesidad 183.170 €.
- **Financiación**: 55.000 € propios + 129.000 € al 6 %, 7 años con 1 de carencia; cuota 26.234 €. DSCR 1,39 / 1,37 (mín. 1,37).
- **Equilibrio**: contable 130 clientes/día (holgura 10,5 %); caja 120 / 143 / 148 (holguras 19,5 % / 8,7 % / 9,9 %; mínimo del libro 15 %).
- **Tesorería**: saldo mínimo 30.175 € en marzo (Mes 1); cierre 66.345 € en febrero. Payback «Más de 3 años». Cobertura de horas 101 %.
- **Escenarios**: pesimista 120 × 4,60 € × 300 = 165.600 € → neto −22.261 €; optimista 165 × 5,20 € × 320 = 274.560 € → +47.576 €.

**La revisión no movió ninguna cifra**: los `valores` de `cifras_caso_es.json` son idénticos antes y después. El único cambio en los tokens es el glifo del signo de `ESC_PES_NETO` («-» → «−», m12). Hay tres tokens nuevos, leídos de su celda: `IS_GENERAL` (Supuestos «Impuesto de Sociedades, tipo general», 25 %), `HOLGURA_MINIMA` (Supuestos «Holgura mínima…», 15 %) y `SUELDO_TITULAR` (Personal, fila del titular, col. D, 1.750 €).

## 3. Revisión final: qué se hizo con cada hallazgo

| id | dónde | arreglo aplicado |
|---|---|---|
| M1 | Word §4 y §10 | §4: equilibrio de caja «120 el primer año, y 143 y 148 el segundo y el tercero». §10: el pesimista (−24 % de venta) supera la holgura de los años 2 y 3, que está por debajo del 15 % del libro; un año 2 pesimista cuesta unos 36.000 € de caja, que se pagan con los 66.345 € del cierre del año 1. Cierre: «qué te queda de caja si el segundo verano es el pesimista». La landing no dice «se absorbe». |
| M2 | Word §9, checklist F3!E9, FAQ 6 de la landing | ≤ 25 % de lo que vendes en el año servido a otros negocios, **o** venta TOTAL (público incluido) ≤ 500 kg/semana. También en la pista §9 y en el brief. |
| M3 | Supuestos!C7 (`a.py`) | el % se aplica a los clientes; el personal crece con las incorporaciones de la hoja Personal (6.000 € + 6.000 €). |
| M4 | Word §8 | partidas de 117.150 € a unos **92.000 €** (no 90.000: con el 50 % del ahorro, para que cuadre con la inversión total) e inversión total a unos 133.000 €; «pon los precios reales». |
| M5 | checklist F2 | tarea nueva «Licencia, declaración o comunicación previa de la obra» (semanas 6-8, Ley 12/2012 arts. 3.3 y 4); el certificado final pasa a la tarea del boletín, que se va al final. Siguen siendo 15 tareas (80 en total). E de la 644.4 remite a la tarea anterior. |
| M6 | checklist F5!E7 | «sin lácteos en la receta» para veganos y para quien no toma leche; al alérgico, sólo mantecados antes que los de leche, con máquina limpia y anotado en la ficha. |
| M7 | Tesorería!A34 (`a.py`, `VOCABULARIO` sobre la frase del motor: sin tocar código común) y Word §1 y §8 | trimestres del plan frente a los de Hacienda (303 en abril, julio, octubre y enero); en el caso todos a compensar; unos 17.750 € a devolver en el 303 de enero. §8: hasta diciembre sólo se compensan unos 7.000 €. |
| m1-m17 | Word, checklist, notas | m1 cierre en invierno (unos 8.000 € de ahorro frente a unos 23.000 € de margen) · m2 sueldo de 1.750 € en 14 pagas (token) · m3 IS general «del libro» y tipos de microempresa · m4 Word §8 y Tesorería!O13: verano más barato, hasta unos 10.000 € menos de caja en septiembre · m5 vitrina de 18 cubetas montada con dos módulos de 10 (Word §6 y D17; el rótulo no cambia) · m6 mantecadora en la parte baja de 12.000-35.000 €, dos presupuestos (Word §6 y D13) · m7 kW frente a kWh y la vitrina no guarda tartas · m8 líquidos primero, secos premezclados con el azúcar (Word §2 y §6, checklist F3!E10 y `ORDEN_PROCESO`) · m9 nombres fijos de la inversión (§1, §4, §8) · m10 «más de tres años (unos 4,5…)» en minúscula y sin comillas · m11 ilación del §3 · m12 «millones de litros (o kilos)», «0,87 litros», «busca poco…», «primeros resultados de Google», «del 6 %», «sin bajar del mínimo de marzo», signo «−» · m13 llamamientos: «Septiembre y enero» · m14 declaración sanitaria «antes de la primera tanda (también las de prueba)» · m15 art. 82.1.c LRHL + «confírmalo» y modelo 036 (Word §9 y checklist F1) · m16 Personal!J5: el 33 % sobre 14 pagas como si fuera nómina (unos 8.085 €), lado prudente · m17 Supuestos!C54: intereses de los meses de obra (unos 1.290 €) y la carencia corre desde la firma. |

No aplicado tal cual: en m16 no se dice «pon la cuota real» porque la Seguridad Social es una fórmula (`E5 = D5 × 33 %`), no una celda verde; se remite a la gestoría. En m17 la nota va en `Supuestos!C54` (la celda que alimenta la renta previa) y no en `Inversión!D27`, que es una fórmula del motor y con el texto nuevo pasaría el límite de 255 caracteres por literal.

## 4. Cálculo de las cifras estimadas (no las calcula el Excel: van con «unos»)

- **36.000 €** (M1): margen pesimista 118.900,8 (Escenarios!B16) − fijos de caja del año 2 (147.162,3 − 10.665 de amortización) − principal del año 2 18.493,8 (Financiación!B47) = −36.090 €. **24 %**: 1 − 165.600 / 217.217 = 23,8 %.
- **92.000 / 133.000 €** (M4): cinco equipos del obrador = 50.400 € (Inversión!B12-B17); con un 50 % menos, −25.200 € → 117.150 − 25.200 = 91.950 € y 158.274 − 25.200 = 133.074 € (el fondo no cambia: excluye la amortización).
- **17.750 € y 7.000 €** (M7): IVA repercutido de los meses 1-10 (marzo-diciembre, Tesorería!B16:K16) 20.477,2 € − soportado (B17:K17) 13.335,3 € = 7.142 € compensados; 24.895,5 − 7.142 = 17.753,5 €.
- **8.000 y 23.000 €** (m1): dependiente 1.729 €/mes × 4 = 6.916 €, × 14/12 = 8.069 €; venta de noviembre a febrero = 15 % × 217.217 = 32.583 € × 71,8 % = 23.394 €.
- **10.000 €** (m4): fijos discontinuos 22.996 €/año pagados en 14 partes; a cierre de septiembre el modelo lleva 8/14 (13.141 €) y en la realidad, todo: 9.855 €. Va bajando a 8.213 (oct.), 6.570 (nov.), 3.285 (dic.) y 1.643 € (ene.); marzo es unos 1.643 € mejor en la realidad.
- **4,5 años** (m10): flujos libres 30.984,6 + 36.490,0 + 35.901,4 = 103.376 € frente a 158.274 €; faltan 54.898 € / 35.901 € = 1,53 años más.
- **1.290 €** (m17): 2 meses de obra × 645 € de intereses al mes (Tesorería!B14). **8.085 €** (m16): 577,5 € × 14 (Personal!E5).

## 5. Guía de equivalencias: sin términos nuevos en el glosario

La guía del producto (70 términos, commit `dff23917`) se genera con el glosario común. No se añaden términos del oficio (bola, cucurucho, tarrina, polo…) porque sólo hay variantes para 3 de los 21 países. Un término con 18 filas iguales a España no aporta nada a la guía. Los ejemplos van en la FAQ de países de la landing.

## 6. Gates de cierre (VPS, 25-oct)

`ciclo.sh` TODO VERDE (13/13, idempotencia 0, caché 0 fallos, censo 0, demos 30/30) · `cifras_hel_es.py` D9 VERDE sobre el publicado, valores idénticos · `docx_hel_es.py` 10 H1, A4, 7.061 palabras, 0 tokens · `barrido_es.py` 0 en los 3 · `gate_restos_ft.py` VERDE sobre los 3 rehechos. La guía de equivalencias es Letter, como las 52, y `--excluir` no salta el control de A4: es la única marca, y es legítima. · `gate-no-latinos` 0 · `censo-entregables --fail` 0. Mac = VPS (sha256) en los 3 entregables. Deuda ajena al producto: «modelo 036/037» sigue en el post `como-abrir-restaurante-ia-guia-completa` y en `plan-negocio-food-truck.ts` (carril de Cursor).
