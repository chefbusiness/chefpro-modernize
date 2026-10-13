# SPEC de las fichas por país — Guía de Equivalencias ES ↔ Hispanoamérica y EE. UU.

> Sesión Claude Code, 13-oct-2026. Plan completo en `PLAN.md` (misma carpeta).

## Para quién y para qué

Cada producto digital de aichef.pro (kits Excel, planes de negocio, guías, manuales) está hecho con el **marco
profesional español**: IVA 10 % en hostelería, APPCC, convenio de hostelería, autónomo/SL, Seguridad Social, escandallo,
camarero… El comprador es un **emprendedor o profesional de hostelería de un país hispanohablante** que tiene que
**usar mañana** ese producto en su país. La ficha le dice, en una página, **qué cambia en su país** y **dónde
comprobarlo**. No es un tratado legal: es la chuleta de un consultor con 29 años de oficio.

## Fichero y formato

Un JSON por país en `fichas/<CÓDIGO>.json` (ISO-3166 alfa-2: MX, GT, HN, SV, NI, CR, PA, DO, PR, CO, VE, EC, PE, BO,
CL, AR, UY, PY, BR, US). UTF-8, válido (`python3 -m json.tool` sin error).

```json
{
  "codigo": "MX",
  "pais": "México",
  "moneda": "peso mexicano (MXN)",
  "consultado": "2026-10",
  "campos": {
    "impuesto_consumo":      {"texto": "…", "fuentes": [{"titulo": "…", "url": "https://…"}], "verificado": true},
    "propina_servicio":      {…},
    "autoridad_sanitaria":   {…},
    "manipulador":           {…},
    "licencias_apertura":    {…},
    "alcohol":               {…},
    "forma_juridica":        {…},
    "laboral":               {…},
    "unidades_mercado":      {…},
    "pagos_delivery":        {…},
    "apoyos_emprendimiento": {…},
    "tipos_local":           {…},
    "adaptar_productos":     {…}
  },
  "trampas": ["«torta» en México es un bocadillo (sándwich), no una tarta", "…"]
}
```

### Qué va en cada campo (40-90 palabras por campo)

| Campo | Contenido |
|---|---|
| `impuesto_consumo` | Impuesto que grava la venta en restauración (IVA, IGV, ITBIS, ITBMS, ISV, impuesto al consumo…), tipo general y, si existe, el especial de restaurantes/bebidas alcohólicas; si los precios de carta se publican con impuesto incluido. Tipos en %, con su fecha si están en transición. |
| `propina_servicio` | Si el cargo por servicio es legal/obligatorio (y %), o voluntario y costumbre; a quién corresponde. |
| `autoridad_sanitaria` | Autoridad (nacional y si aplica local) y **norma de referencia** de higiene en establecimientos de comida (equivalente al APPCC español: p. ej. NOM-251-SSA1-2009 en México). Si se exige HACCP o BPM. |
| `manipulador` | Carné/curso/certificado de manipulador de alimentos: nombre local, quién lo emite, vigencia si se conoce. |
| `licencias_apertura` | Nombre de los permisos típicos para abrir un restaurante/bar (municipal, sanitario, bomberos/protección civil, uso de suelo…). |
| `alcohol` | Licencia o permiso de venta de alcohol: quién lo da; restricciones notables (horarios, ley seca). |
| `forma_juridica` | Formas societarias habituales para un pequeño negocio de hostelería (S.A.S., SpA, SRL, S.A. de C.V.…) y el **régimen fiscal simplificado** equivalente al autónomo/módulos (RESICO, Monotributo, RUS, SIMPLE…). |
| `laboral` | Jornada legal semanal (y reducciones en curso con fechas), prestaciones obligatorias que no existen igual en España (aguinaldo, prima de servicios, CTS, gratificaciones, 13.º/14.º sueldo, PTU…), entidad de seguridad social. **Sin importes de salario mínimo.** |
| `unidades_mercado` | Unidades que se usan de verdad al comprar o vender en hostelería además del sistema métrico (libra y su valor real en ese país, arroba, galón, onza, botella, docena, «cajilla»…) con equivalencia métrica; escala de temperatura si no es °C. |
| `pagos_delivery` | Apps de delivery dominantes y medios de pago habituales en hostelería (efectivo, QR, Pix, Yape/Plin, Nequi, SINPE Móvil, Mercado Pago, transferencias). |
| `apoyos_emprendimiento` | Programas públicos o semipúblicos para emprender/pymes (equivalente a ENISA/ICO), solo los vigentes y oficiales. |
| `tipos_local` | Formatos de negocio y nombres locales de hostelería (fonda, cocina económica, lonchería, picantería, cevichería, asadero, parrilla, pupusería, soda, bodegón, quincho…) con su equivalente español más cercano. |
| `adaptar_productos` | 3-5 cambios concretos al usar una plantilla española en ese país: p. ej. «cambia el IVA del 10 % por el 16 % en la casilla de parámetros», «el plan APPCC se presenta como programa de BPM conforme a la NOM-251», «el convenio de hostelería no aplica: la referencia es la Ley Federal del Trabajo». |
| `trampas` | Falsos amigos con el español de España que pueden confundir en una carta, un pedido o una ficha (lista de 2-6 frases cortas). |

## Reglas no negociables

1. **Fuentes oficiales para todo lo legal/fiscal/sanitario/laboral** (portal del gobierno, autoridad tributaria,
   ministerio, diario oficial, legislación consolidada). Abre de verdad la página (WebFetch) antes de citarla. Las de
   `pagos_delivery`, `tipos_local` y `trampas` pueden no llevar fuente (`"fuentes": []`).
2. Si un dato legal no se puede confirmar con fuente oficial abierta: redáctalo prudente («consulta con…») y pon
   `"verificado": false`. **Nunca inventes una norma, un número de ley ni un porcentaje.**
3. **Nada de importes en moneda local que caducan** (salario mínimo, tasas municipales, multas). Sí porcentajes y
   nombres, con fecha si están en transición (p. ej. reducción de jornada por etapas).
4. Español neutro, claro y profesional; trato de **tú** (nunca «vosotros» ni voseo). Términos locales entre comillas
   latinas «…» la primera vez. Sin relleno ni frases de marketing.
5. Nada de normativa española en la ficha salvo para comparar («equivale al APPCC español»).
6. No toques nada fuera de `fichas/`. No hagas commit ni push.
