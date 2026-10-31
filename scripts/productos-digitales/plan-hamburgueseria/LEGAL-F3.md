# LEGAL-F3 — cotejo con el texto vigente (consulta: 31-oct-2026)

## 1. Ley 37/1992 del IVA, art. 91 (BOE consolidado, actualización publicada 07/10/2026)
URL: https://www.boe.es/buscar/act.php?id=BOE-A-1992-28740
- Uno.1.1.º: tipo del 10 % para alimentos «susceptibles de ser habitual e idóneamente utilizados para la nutrición humana»; «Se excluyen: a) Las bebidas alcohólicas. b) Las bebidas refrescantes, zumos y gaseosas con azúcares o edulcorantes añadidos.» (Esas exclusiones van al 21 %. Una «zero» lleva edulcorantes añadidos: queda excluida.)
- Uno.2.2.º (10 %): «Los servicios de hostelería, acampamento y balneario, los de restaurantes y, en general, el suministro de comidas y bebidas para consumir en el acto, incluso si se confeccionan previo encargo del destinatario.»
- Dos.1.1.º (4 %): a) «El pan común…», b) harinas panificables, c) leche (natural, pasterizada, UHT, etc.), d) quesos, e) huevos, f) frutas, verduras, hortalizas, legumbres, tubérculos y cereales naturales, g) «Los aceites de oliva». El de girasol y el pan que no es común, al 10 %. El batido no está en la lista de leche del 4 %.
- Aviso: el BOE marca modificaciones de Uno.2.2.º con efectos 1-dic-2026 (RDL 29/2026, de 6 oct, BOE-A-2026-20823). Leído el RDL (art. 7): solo afecta al alquiler de viviendas amuebladas de corta duración (se incluye en el 10 %); la hostelería y restauración NO cambia.

## 2. Reglamento (CE) 853/2004, anexo III, sección V
Fuente: PDF del DOUE publicado por el BOE (https://www.boe.es/doue/2004/139/L00055-00205.pdf), que es el texto ORIGINAL de 2004. EUR-Lex (consolidado) devolvió 202/vacío desde este entorno; hay que recomprobar en EUR-Lex que el cap. III no se haya retocado.
- Cap. III, 2.b): carne refrigerada para picar: «aves de corral, dentro de los 3 días siguientes al sacrificio; animales distintos de las aves de corral, dentro de los 6 días siguientes al sacrificio; carne de vacuno deshuesada y envasada al vacío, dentro de los 15 días siguientes al sacrificio.»
- Cap. III, 2.c): inmediatamente tras prepararla, envasar y refrigerar a «no superior a 2 °C en el caso de la carne picada, y de 4 °C en el caso de los preparados de carne», o congelar a -18 °C.
- Anexo I, 1.13: carne picada = deshuesada, picada y con «menos de 1 % de sal».

## 3. RD 1021/2022 (BOE-A-2022-21681; NO es 21677, ese id es otra ley)
URL: https://www.boe.es/buscar/act.php?id=BOE-A-2022-21681
- 2.2.a: «establecimiento de comercio al por menor» incluye «establecimientos de restauración y hostelería».
- 4.1 (tabla): «Carne picada. Igual o inferior a 2 °C.» · «Preparados de carne. Igual o inferior a 4 °C.»
- 7.2: «el picado podrá realizarse con carácter previo, con arreglo a las necesidades del despacho diario, no pudiendo conservarse de un día para otro.»
- 7.3: remite a los capítulos II y III de la sección V del anexo III del 853/2004; sin CSM.

## 4. Frase del producto → veredicto
| Frase | Veredicto |
|---|---|
| 2 °C carne picada / 4 °C preparados (ham_es_b 81, 104; landing l.51, 156) | Se sostiene (RD 4.1 y 853 cap. III 2.c) |
| «Picada en el local… no de un día para otro» (7.2; landing 51, 172; ham_es_b 112) | Se sostiene, literal |
| Remisión 7.3 a caps. II y III sección V | Se sostiene |
| Bola sin sal = picada (<1 %); salada = preparado | Se sostiene (anexo I 1.13) |
| Restauración incluida (art. 2.2.a) | Se sostiene |
| Sala al 10 % (91.Uno.2.2.º); bebidas alcohólicas y refrescantes con azúcares/edulcorantes, también zero, al 21 % (91.Uno.1.1.º a y b) | Se sostiene |
| Queso, verdura, patata al 4 %; pan de hamburguesa y girasol al 10 % (ham_es_b 95) | Se sostiene (girasol: solo «aceites de oliva» al 4 %). «Pan de hamburguesa no es pan común» depende de la definición de pan común (RD 308/2019, no del art. 91): conservar solo si el brioche no cumple esa definición |
| «Para llevar, la comida va al 10 %» (ham_es_b 108) | Se sostiene |
| **«No se puede elaborar carne picada con carne madurada más de quince días»** (ham_es_a 50, 57; ham_es_b 104, 112; landing 51, 156; y notas del Excel `Carne!`, `Instrucciones!`, F3 si repiten la frase) | **Cambiar**: el 853 no habla de «madurada»; fija 6 días desde el sacrificio (3 en aves) y 15 solo para vacuno deshuesado y envasado al vacío. Los 15 días de Inf26008 no son una cita literal de la norma |
| «El batido de leche no es una bebida refrescante… al 10 %» (ham_es_b 108) | Cambiar la afirmación a hipótesis: el art. 91 no trata el batido; un batido con azúcares añadidos puede discutirse como «bebida refrescante». Ya remite a la gestoría; retirar el «no es» categórico |

## 5. Texto propuesto
- Sustituir «según Madrid Salud (Inf26008), no se puede elaborar carne picada con carne madurada más de quince días» por: «el Reglamento (CE) 853/2004 (anexo III, sección V, cap. III) exige picar la carne refrigerada dentro de los 6 días siguientes al sacrificio (15 si es vacuno deshuesado y envasado al vacío); una dry aged madurada semanas queda fuera de plazo, y Madrid Salud (Inf26008) lo aplica así». Misma sustitución en las 4 ubicaciones de ham_es_a/ham_es_b, landing y Excel.
- Sustituir «El batido de leche no es una bebida refrescante y el plan lo lleva al 10 %» por: «El art. 91 no recoge el batido de leche entre los productos del 4 %; el plan lo lleva al 10 % como bebida de leche, pero confírmalo con tu gestoría, porque si lleva azúcares o edulcorantes añadidos podría considerarse bebida refrescante (21 %)».
- No tocar `datos_checklist.py`, `a.py` ni el correo más allá de la frase de los 15 días si aparece: grep no halló citas de 91/853 en ellos; el correo cita RD 1021/2022, arts. 4.1 y 7.2 (correcto).
