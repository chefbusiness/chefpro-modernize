#!/usr/bin/env python3
"""
check_contrato.py — Wedding Venue Business Plan Kit (EN) · tanda del CONTRATO (SPEC D171; decisiones de orquestador 2 y
4, 27-oct). Solo JSON (Mac). Sesión Claude Code, 27-oct-2026 (F2-EN, paso 1a).

El contrato ES (`../plan-finca-eventos/textos/contrato_es.json`, 150 párrafos `{estilo, texto}`) se reparte en DOS partes
para que cada traductor de la tanda 1 lleve ≈ la mitad de las palabras (D178 + orquestador):
  parte 1 = portada + Modelo 1 (reserva con particulares) + Anexo de empresas   (ES 0-101, ≈ 3,3 K palabras) → traductor B
  parte 2 = Modelo 2 (catering exclusivo)                                       (ES 102-149, ≈ 1,4 K palabras) → traductor A
Salida de cada parte: `textos_en/contrato_en_<n>.json` = lista `[{"estilo": …, "texto": …}]` (mismos estilos que el ES;
`**negrita**`); NO es una traducción 1:1: cláusulas que cruzan, cambian, se quitan o son nuevas (D171). `contrato_wed.py`
(paso 3) concatena 1 + 2 sobre el molde físico del docx ES en Letter.

    python3 bp9.py check_contrato --preparar        # tandas/contrato_{1,2}.entrada.json
    python3 bp9.py check_contrato --parte 1         # valida textos_en/contrato_en_1.json (o --parte 2, o --todas)
"""
import argparse
import json
import os
import re
import sys
from collections import OrderedDict

AQUI = os.path.dirname(os.path.abspath(__file__))
PD = os.path.dirname(AQUI)
sys.path.insert(0, os.path.join(PD, 'business-plans-en'))
os.environ.setdefault('BP_CONJUNTO', 'wed')
import mapas as M                                                                  # noqa: E402

ES = os.path.join(PD, 'plan-finca-eventos', 'textos', 'contrato_es.json')
CORTE = 102                                   # primer párrafo del Modelo 2 (H1 «Modelo 2 · …»)
ESTILOS = ('Kicker', 'Title', 'Subtitle', 'H1', 'H2', 'Normal', 'List Bullet', 'Separador', 'Firma')
CABECERA = ('**Template, not legal advice.** Consumer, deposit, alcohol and tax rules vary by state. Have a licensed '
            'attorney in your state review and adapt it before you use it.')
REL = 'scripts/productos-digitales/business-plans-en-9'

REGLAS_COMUNES = [
    'Inglés de EE. UU., registro de contrato claro (plain English), segunda persona NO: «the Venue», «the Client», «the '
    'Caterer». Corchetes [ ] para TODO lo editable (nombres, fechas, importes, plazos, porcentajes por defecto, estado, '
    'condado): «[State]», «[14] days», «[25]%», «$[amount]». CERO cifras del caso del kit (ventas, invitados, precios '
    'por invitado) y cero cifras del ES.',
    'Mismos estilos que el ES (Kicker, Title, Subtitle, H1, H2, Normal, List Bullet, Separador, Firma); «**negrita**» '
    'dentro del texto como en el ES. Puedes añadir, quitar o reordenar párrafos dentro de tu parte: NO es una '
    'traducción 1:1 (SPEC D171).',
    'Nada de derecho español: ni TRLGDCU, LAU, Código Civil, IVA, «señal/arras», «fuero del consumidor», SGAE, comida '
    'testigo, Ley 15/2015, «finca», «canon», NIF/CIF/DNI (las firmas: «Name», «Title», «Date», «Signature»).',
    'Jerga (research §9, glosario adjunto): venue rental fee / site fee · retainer (aplicado al precio) · security deposit '
    '(refundable, itemized) · guaranteed guest count · final headcount · venue coordinator · setup / load-out · rain plan '
    '· maximum occupancy (posted by the fire marshal) · outside vendors · COI / additional insured · host liquor liability '
    '· exclusive caterer · caterer commission · service charge vs. gratuity · 9 major food allergens.',
    'NUNCA «non-refundable» / «nonrefundable» solo: el retainer se aplica al precio y lo que se retiene al cancelar lo fija '
    'SOLO la tabla de cancelación; si lo mencionas, en el mismo párrafo remite a esa tabla (el check lo exige).',
    'FTC Cooling-Off Rule (decisión de orquestador 2): la regla excluye los arrendamientos de inmuebles, así que NO se '
    'afirma que aplique a un contrato de venue. Forma permitida, como nota de redacción entre corchetes: «[Drafting note: '
    'if you sign couples at bridal shows or off-site, ask your attorney whether the FTC Cooling-Off Rule or your state\'s '
    'home-solicitation law applies; many venues give a short cancellation window for show-floor signings anyway.]» y, si '
    'quieres, una cláusula OPCIONAL entre corchetes con esa ventana de cancelación. Nada de «16 CFR 429 applies» ni «you '
    'have a legal right under federal law».',
    'Lo marcado «(resumen)» en research (California Civ. Code §1671, NY A20-51S, Missouri, Wisconsin, 40 CFR 141.2) NO se '
    'cita (decisión de orquestador 4): «a reasonable estimate of the Venue\'s loss, not a penalty» sin citar el código; '
    'reglas de alcohol y de sales tax «under [State] law» / «as your state requires».',
    'Unidades y formatos US: $1,000.00, mm/dd/yyyy, «business days». Sin emojis, sin caracteres no latinos, sin español.',
]
DECISIONES = OrderedDict([
    (1, [
        'PORTADA: Kicker «AI CHEF PRO · WEDDING VENUE BUSINESS PLAN KIT», Title «Venue Rental Agreement Templates», '
        'Subtitle «Couples & private events, corporate clients and exclusive caterer». Justo después, un Normal con la '
        'CABECERA FIJA, literal: «%s» (el check la exige tal cual). Luego el «cómo usarlo» del ES adaptado.' % CABECERA,
        'MODELO 1 → H1 «Model 1 · Venue Rental Agreement (Couples & Private Events)». CRUZAN (adaptadas): Reunidos → '
        '«Parties»; 1.ª Objeto → «Rental and included services»; 3.ª → «Guest count, guaranteed minimum and final '
        'headcount»; 9.ª → «Date change»; 11.ª → «Setup, event and load-out hours» (curfew de las condiciones del CUP del '
        'condado); 13.ª → «Maximum occupancy» (la que fija y rotula el fire marshal); 16.ª → «Rain plan» (la lluvia no es '
        'fuerza mayor); 20.ª → «Photos and privacy» (autorización escrita aparte para usar fotos).',
        'CAMBIAN: 2.ª Licencias → «Permits» (el Venue declara que tiene el zoning approval —conditional use permit— y el '
        'certificate of occupancy); 2.ª bis → «2A. Contingent booking before permits»: solo un hold con devolución ÍNTEGRA '
        'en [14] días si el CUP o el certificate of occupancy no llegan antes de [fecha, al menos 6 meses antes del '
        'evento]; 4.ª → «Fees and sales tax» («plus applicable sales tax»); 5.ª → «Payment schedule and receipts» '
        '([25]% al firmar, [35]% [180] días antes, [40]% [30] días antes); 6.ª → «Retainer»: se aplica al precio; lo que '
        'se retiene si el Client cancela lo fija SOLO la tabla de la cláusula de cancelación.',
        '7.ª → «Cancellation by the Client»: tabla de tramos (ES: [10]/[25]/[50]/[75]/[100]% del precio según se cancele '
        'con más de [12] meses, [12-6], [6-3], [3-1] meses o menos de [1] mes) + «rebooking credit» («if the Venue rebooks '
        'the date at an equal or higher fee, it refunds what it retained minus its documented costs») + «the parties agree '
        'these amounts are a reasonable estimate of the Venue\'s loss, not a penalty». 8.ª → «Cancellation by the Venue»: '
        'devolución íntegra en [14] días + [importe pactado] y ayuda para recolocar la fecha.',
        'SE QUITAN las citas españolas: 10.ª (sin desistimiento, art. 103.l) → «Signing away from the Venue» como cláusula '
        'OPCIONAL entre corchetes con la nota de redacción de la FTC Cooling-Off Rule (regla común 6: NO afirmar que aplica); '
        '21.ª (fuero del consumidor) → «Governing law and disputes»: «[State] law; courts of [County], [State]» + «have a '
        'licensed attorney in your state review this clause»; 17.ª (art. 1105 CC) → «Force majeure» genérica con reembolso '
        'o nueva fecha a elección del Client.',
        '12.ª → «Noise and music» (decibel limit, curfew, licencias de música ASCAP/BMI/SESAC del Venue; la música del DJ o '
        'de la banda, del Client o su proveedor); 14.ª → «Outside vendors» (COI con el Venue como additional insured, '
        'bartenders con licencia solamente, nada de llama abierta, sparklers ni fuegos sin permiso del fire marshal); '
        '15.ª → «Damage and security deposit» (reembolsable, deducciones detalladas por escrito en [14] días); 18.ª → '
        '«Insurance» (GL del Venue; el Client, event liability + host liquor liability si hay alcohol); 19.ª → «Food, '
        'alcohol and allergens» (del caterer; alcohol solo por el caterer o un bartender con licencia, ID, nada a menores '
        'ni a personas visiblemente ebrias).',
        'NUEVAS: «Mutual responsibility» (cada parte responde de su propia negligencia; sin indemnidad unilateral) y '
        '«Entire agreement and e-signatures». Firmas: «Venue: ____ Client: ____» · «Name / Title / Date».',
        'ANEXO → H1 «Corporate & Organization Addendum»: W-9 del Venue, orden de compra (PO) y contacto de facturación, '
        'certificado de exención de sales tax si la entidad está exenta, net terms ([30] días), tramos de cancelación '
        '[5]/[15]/[35]/[60]/[100]% y foro pactado; firma «Company: ____ Title: ____».',
    ]),
    (2, [
        'MODELO 2 → H1 «Model 2 · Exclusive Caterer Agreement» + Kicker «BETWEEN THE VENUE AND THE CATERER THAT WORKS IT '
        'EXCLUSIVELY». Es B2B: «the Venue» y «the Caterer».',
        'Objeto y exclusividad (excepción: la tarta de una bakery con licencia, con su COI) · contratación y facturación '
        'DIRECTA del Caterer a la pareja con su sales tax; service charge vs. gratuity a cargo del Caterer (qué es cada uno, '
        'dicho al cliente por escrito) · «Caterer commission»: [10]% of food & beverage sales at the Venue, net of sales '
        'tax, service charge and gratuities; statement mensual en [10] días, derecho de auditoría con [15] días de aviso, '
        'mínimo anual opcional $[amount] (nunca «canon» ni «royalty»).',
        'Uso de la prep & warming kitchen del Venue: el Caterer mantiene su health permit y su plan de seguridad alimentaria '
        'y deja la cocina como la encontró · la «comida testigo» del ES SE QUITA (no es norma US) · alérgenos: «the major '
        'food allergens as defined by federal law and your state or local rules», por escrito en cada menú · personal W-2 '
        'del Caterer (FLSA, I-9), sin relación laboral con el Venue.',
        'Seguros: liquor license / catering permit del Caterer + liquor liability $[1,000,000] + general liability + workers\' '
        'comp + commercial auto, con el Venue como additional insured · horarios, limpieza, residuos y grasa (FOG) · menús '
        'mínimos y tasting · plazo y renovación, resolución por incumplimiento con aviso de [30] días · entrega de la cocina '
        'al terminar · governing law (B2B): «[State] law; courts of [County]». Firmas «Venue: ____ Caterer: ____».',
    ]),
])


def partes():
    es = json.load(open(ES, encoding='utf-8'))
    return OrderedDict([(1, es[:CORTE]), (2, es[CORTE:])])


def preparar():
    glo = OrderedDict((k, v) for k, v in M.GLOSARIO.items())
    os.makedirs(os.path.join(AQUI, 'tandas'), exist_ok=True)
    for n, items in partes().items():
        obj = OrderedDict([
            ('tanda', 'contrato_%d' % n),
            ('salida', '%s/textos_en/contrato_en_%d.json' % (REL, n)),
            ('formato_salida', '[{"estilo": "<uno de %s>", "texto": "<EN>"}, …] en el orden del documento; puedes '
                               'añadir, quitar o reordenar párrafos dentro de tu parte' % ', '.join(ESTILOS)),
            ('parte', 'portada + Modelo 1 + Anexo de empresas' if n == 1 else 'Modelo 2 · catering exclusivo'),
            ('n_parrafos_es', len(items)), ('n_palabras_es', sum(len(x['texto'].split()) for x in items)),
            ('cabecera_fija (solo parte 1, literal)', CABECERA if n == 1 else None),
            ('reglas', REGLAS_COMUNES), ('decisiones_D171', DECISIONES[n]),
            ('glosario', glo),
            ('verificacion', 'python3 %s/bp9.py check_contrato --parte %d' % (REL, n)),
            ('es', [OrderedDict([('i', i if n == 1 else CORTE + i), ('estilo', x['estilo']), ('texto', x['texto'])])
                    for i, x in enumerate(items)]),
        ])
        p = os.path.join(AQUI, 'tandas', 'contrato_%d.entrada.json' % n)
        with open(p, 'w', encoding='utf-8') as fh:
            json.dump(obj, fh, ensure_ascii=False, indent=1)
            fh.write('\n')
        print('tandas/contrato_%d.entrada.json: %d párrafos ES, %d palabras' % (n, len(items), obj['n_palabras_es']))
    return 0


RX_TOKEN = re.compile(r'__[A-Za-z][\w ]*__|\{\{|\}\}')
RX_NONREF = re.compile(r'(?i)\bnon-?refundable\b')
RX_COOLING_SI = re.compile(r'(?i)(?:cooling-off rule|16 CFR (?:part )?429)[^.]{0,80}\b(?:applies|gives (?:you|the client)|'
                           r'requires (?:us|the venue)|entitles)')


def check(n):
    p = os.path.join(AQUI, 'textos_en', 'contrato_en_%d.json' % n)
    if not os.path.exists(p):
        print('contrato_en_%d.json: no existe (%s)' % (n, p))
        return 1
    try:
        items = json.load(open(p, encoding='utf-8'))
    except ValueError as e:
        print('ERROR contrato_en_%d.json no es JSON válido: %s' % (n, e))
        return 1
    err, avi = [], []
    if not isinstance(items, list) or not items:
        err.append('no es una lista no vacía de {estilo, texto}')
        items = []
    todo = []
    for i, it in enumerate(items):
        if not isinstance(it, dict) or set(it) != {'estilo', 'texto'}:
            err.append('[%d] no es {estilo, texto}: %r' % (i, it))
            continue
        e, t = it['estilo'], it['texto']
        if e not in ESTILOS:
            err.append('[%d] estilo desconocido %r' % (i, e))
        if not isinstance(t, str) or (not t.strip() and e != 'Separador'):
            err.append('[%d] texto vacío' % i)
            continue
        todo.append(t)
        if t.count('**') % 2:
            err.append('[%d] negrita sin cerrar (**)' % i)
        if RX_TOKEN.search(t):
            err.append('[%d] token sin resolver: %r' % (i, RX_TOKEN.findall(t)[:3]))
        r = [x for x in M.restos_espanol(t) if not x[0].startswith('oficio')]
        if r:
            err.append('[%d] español: %s «%s»' % (i, r[0][0], t[:70]))
        if M.no_latinos(t):
            err.append('[%d] caracteres no latinos' % i)
        for motivo, frag in M.cifras_prohibidas(t):
            err.append('[%d] %s «%s»' % (i, motivo, frag))
        if RX_NONREF.search(t) and not re.search(r'(?i)schedule|table|clause|section', t):
            err.append('[%d] «non-refundable» sin remitir a la tabla de cancelación: «%s»' % (i, t[:90]))
        elif RX_NONREF.search(t):
            avi.append('[%d] «non-refundable» con remisión (la revisión D174 lo mira): «%s»' % (i, t[:90]))
        for m in RX_COOLING_SI.finditer(t):
            if 'whether' not in t[max(0, m.start() - 60):m.start()].lower():   # «ask your attorney whether … applies» vale
                err.append('[%d] afirma que la FTC Cooling-Off Rule aplica (decisión de orquestador 2): «%s»' % (i, t[:90]))
        if re.search(r'(?i)1671|A20-51S|141\.2|Wisconsin|Missouri', t):
            err.append('[%d] cita una norma marcada «(resumen)» en research (decisión de orquestador 4)' % i)
    texto = '\n'.join(todo)
    if n == 1:
        if CABECERA not in [it.get('texto') for it in items[:6] if isinstance(it, dict)]:
            err.append('falta la CABECERA FIJA literal en los 6 primeros párrafos')
        for clave in ('Retainer', 'Cancellation by the Client', 'Governing law', 'Mutual responsibility',
                      'Entire agreement', 'Corporate', 'Contingent booking', 'rebooking'):
            if clave.lower() not in texto.lower():
                err.append('falta «%s» (D171)' % clave)
        if 'Cooling-Off' in texto and not re.search(r'(?i)ask your attorney whether', texto):
            err.append('menciona la Cooling-Off Rule sin «ask your attorney whether…» (decisión de orquestador 2)')
    else:
        for clave in ('Exclusive Caterer Agreement', 'commission', 'audit', 'additional insured', 'gratuit',
                      'allergen'):
            if clave.lower() not in texto.lower():
                err.append('falta «%s» (D171)' % clave)
    h = [it['texto'] for it in items if isinstance(it, dict) and it.get('estilo') in ('H1', 'H2')]
    for x in err:
        print('ERROR', x)
    for x in avi:
        print('AVISO', x)
    print('contrato_en_%d.json: %d párrafos · %d palabras · %d títulos · %s' % (
        n, len(items), len(texto.split()), len(h), 'OK' if not err else 'ROJO (%d errores)' % len(err)))
    return 1 if err else 0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--preparar', action='store_true')
    ap.add_argument('--parte', type=int, choices=(1, 2))
    ap.add_argument('--todas', action='store_true')
    a = ap.parse_args()
    if a.preparar:
        return preparar()
    if a.todas:
        return max(check(1), check(2))
    if a.parte:
        return check(a.parte)
    ap.error('--preparar, --parte N o --todas')


if __name__ == '__main__':
    sys.exit(main())
