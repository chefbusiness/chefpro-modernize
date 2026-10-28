#!/usr/bin/env python3
"""
check_contrato.py — Coffee Cart Business Plan Kit (EN) · tanda del CONTRATO (SPEC D230). Solo JSON. Sesión Claude Code,
28-oct-2026 (paso 1a). Clon de `../business-plans-en-9/check_contrato.py` con UNA parte (el contrato ES del café tiene
≈ 92 párrafos y ≈ 3,0 K palabras: un traductor).

El contrato ES (`../plan-cafeteria-movil/textos/contrato_es.json`, `{estilo, texto}`; en el VPS, durante la F2 del ES, el
de COF_FUENTE_ES) se traduce-adapta a `textos_en/contrato_en.json` = lista `[{"estilo": …, "texto": …}]` (mismos estilos que
el ES; `**negrita**`); NO es una traducción 1:1: cláusulas que cruzan, cambian, se quitan o son nuevas (D230).
`contrato_cof.py` (paso 3) lo escribe sobre el molde físico del docx ES en Letter.

    python3 bp11.py check_contrato --preparar        # tandas/contrato.entrada.json
    python3 bp11.py check_contrato --todas           # valida textos_en/contrato_en.json
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
os.environ.setdefault('BP_CONJUNTO', 'cof')
import mapas as M                                                                  # noqa: E402

CAF = os.environ.get('COF_FUENTE_ES') or os.path.join(PD, 'plan-cafeteria-movil')
ES = os.path.join(CAF, 'textos', 'contrato_es.json')
SALIDA = os.path.join(AQUI, 'textos_en', 'contrato_en.json')
ESTILOS = ('Kicker', 'Title', 'Subtitle', 'H1', 'H2', 'Normal', 'List Bullet', 'Separador', 'Firma')
CABECERA = ('**Template, not legal advice.** Consumer, deposit, food safety and tax rules vary by state. Have a licensed '
            'attorney in your state review and adapt it before you use it.')
REL = 'scripts/productos-digitales/business-plans-en-11'

REGLAS_COMUNES = [
    'Inglés de EE. UU., registro de contrato claro (plain English), sin segunda persona: «the Coffee Caterer», «the '
    'Client» (y «the Organizer» en el anexo de festivales). Corchetes [ ] para TODO lo editable (nombres, fechas, '
    'importes, plazos, porcentajes por defecto, estado, condado, voltaje y amperios): «[State]», «[14] days», «[30]%», '
    '«$[amount]», «[110V or 220V], [20] amps, within [50] ft». CERO cifras del caso del kit (ventas, invitados, precio por '
    'invitado) y cero cifras del ES.',
    'Mismos estilos que el ES (Kicker, Title, Subtitle, H1, H2, Normal, List Bullet, Separador, Firma); «**negrita**» '
    'dentro del texto como en el ES. Puedes añadir, quitar o reordenar párrafos: NO es una traducción 1:1 (SPEC D230).',
    'Nada de derecho español: ni TRLGDCU (arts. 85, 87, 90, 102, 103), LIVA art. 75, Código Civil, IVA, «señal / arras», '
    '«fuero del consumidor», RGPD, Ley 7/2022, registro sanitario, NIF / CIF / DNI, «feria», «cafetería» (falso amigo: di '
    '«coffee caterer», «mobile espresso bar»), Bizum. Firmas: «Name», «Title», «Date», «Signature».',
    'Jerga (research §9, glosario adjunto): coffee catering · mobile espresso bar · espresso cart · full-service espresso '
    'bar · service window · additional hour · base fee + hourly rate · per guest · hosted / guest-pay · minimum sales '
    'guarantee · retainer (aplicado al precio) · balance due · final guest count · travel fee (free radius) · alt milk / '
    'oat milk · compostable cups · dedicated circuit / standard 110V outlet · COI / additional insured · service charge vs. '
    'gratuity · 9 major food allergens.',
    'NUNCA «non-refundable» / «nonrefundable» solo: el retainer se aplica al precio y lo que se retiene al cancelar lo fija '
    'SOLO la tabla de cancelación; si lo mencionas, en el mismo párrafo remite a esa tabla (el check lo exige).',
    'FTC Cooling-Off Rule: NO se afirma que aplique. Forma permitida, como nota de redacción entre corchetes: «[Drafting '
    'note: if you sign clients at a bridal show or anywhere away from your place of business, ask your attorney whether '
    'the FTC Cooling-Off Rule or your state\'s home-solicitation law applies.]» y, si quieres, una cláusula OPCIONAL entre '
    'corchetes con una ventana de cancelación de [3] business days. Nada de «16 CFR 429 applies».',
    'Tramos de cancelación SIN huecos: «[60] days or more before the event», «from [30] to less than [60] days», «from '
    '[14] to less than [30] days», «less than [14] days»; «the parties agree these amounts are a reasonable estimate of '
    'the Coffee Caterer\'s loss, not a penalty» + crédito si se recoloca la fecha. Sin citar códigos estatales.',
    'Unidades y formatos US: $1,000.00, mm/dd/yyyy, «business days», °F (41 °F para la leche), ft. Sin emojis, sin '
    'caracteres no latinos, sin español.',
]
DECISIONES = [
    'PORTADA: Kicker «AI CHEF PRO · COFFEE CART BUSINESS PLAN KIT», Title «Coffee Catering Service Agreement», Subtitle '
    '«For private events and weddings, with an addendum for corporate clients and festival organizers». Justo después, un '
    'Normal con la CABECERA FIJA, literal: «%s» (el check la exige tal cual). Luego el «cómo usarlo» del ES adaptado (qué '
    'rellenar entre corchetes; anexar la carta y el presupuesto de la calculadora del kit).' % CABECERA,
    'CRUZAN (adaptadas): Reunidos → «Parties»; 1.ª → «Service, location and service hours» (service window, montaje ≈ 1 h '
    'antes, «additional hour» a $[amount]); 2.ª → «Pricing model» (por invitado, base fee + hourly rate o guest-pay con '
    'minimum sales guarantee); 3.ª → «Drink menu, allergens and cups» (carta anexa, leches incluida la de avena, alérgenos: '
    'leche, soja, frutos de cáscara, y trigo y huevo en la bollería de un obrador con licencia; vasos compostables o la '
    'loza del Client donde la sala lo pida); 10.ª → «Date change»; 11.ª → «Rain plan» (la lluvia NO es fuerza mayor: zona '
    'cubierta o interior a cargo del Client); 15.ª → «Photos and privacy» (autorización escrita aparte).',
    'CAMBIAN: 4.ª → «Site requirements and power»: superficie nivelada de [10 × 10] ft, acceso para el carro (rampa o '
    'ascensor), aparcamiento del remolque, y POR ESCRITO un circuito dedicado ([110V or 220V], [20] amps) a ≤ [50] ft; si '
    'no lo hay, generator fee $[amount] y su ubicación la decide el venue o el fire marshal; 5.ª → «Permits: who handles '
    'each one» (Coffee Caterer: health permit de la unidad móvil, food handler cards, seguro y COI; Client: normas y '
    'aprobación de la sala; Organizer: permiso del evento y coordinación de los temporary food event permits); 6.ª → '
    '«Fees and sales tax» («plus applicable sales tax»; service charge ≠ gratuity; tip jar solo con permiso del Client); '
    '7.ª → «Payments, retainer and receipts» (retainer del [30-50]% aplicado al precio, saldo [14] días antes, recuento '
    'final [10] días antes, recibo de cada pago); 8.ª → «Cancellation by the Client» (tabla sin huecos, regla común 7); '
    '9.ª → «Cancellation by the Coffee Caterer» (devolución íntegra en [14] días y ayuda para encontrar sustituto: '
    'reciprocidad); 12.ª → «Force majeure» genérica (reembolso o nueva fecha a elección del Client).',
    'SE QUITAN las citas españolas: 13.ª (sin desistimiento, art. 103.l) → cláusula OPCIONAL entre corchetes con la nota '
    'de redacción de la FTC Cooling-Off Rule (regla común 6); 16.ª (fuero del consumidor, art. 90.2) → «Governing law and '
    'disputes»: «[State] law; courts of [County], [State]» + «have a licensed attorney in your state review this clause»; '
    '14.ª → «Damage, insurance and responsibility»: general liability $[1,000,000] / $[2,000,000] del Coffee Caterer con '
    'COI que nombre a la sala como additional insured; el Client responde de los daños de sus invitados al equipo.',
    'NUEVAS: «Mutual responsibility» (cada parte responde de su propia negligencia; sin indemnidad unilateral) y «Entire '
    'agreement and e-signatures». Firmas: «Coffee Caterer: ____ Client: ____» · «Name / Title / Date».',
    'ANEXO → H1 «Corporate & Festival Organizer Addendum» + Kicker «FOR CORPORATE EVENTS, AGENCIES, CONFERENCES, '
    'FESTIVALS AND FARMERS MARKETS»: W-9 del Coffee Caterer, orden de compra (PO) y contacto de facturación, certificado de '
    'exención de sales tax si la entidad está exenta, net [15 / 30] terms, «Late amounts bear interest at [1.5]% per '
    'month, or the highest rate the law allows if that is lower»; para guest-pay: «minimum sales guarantee» (el Organizer '
    'paga la diferencia entre las ventas de bebidas y $[minimum]), vendor / booth fee, quién aporta la electricidad y el '
    'agua, horario de montaje; tramos de cancelación corporativos; firma «Company / Organizer: ____ Title: ____».',
]


def es():
    return json.load(open(ES, encoding='utf-8'))


def preparar():
    items = es()
    glo = OrderedDict((k, v) for k, v in M.GLOSARIO.items())
    os.makedirs(os.path.join(AQUI, 'tandas'), exist_ok=True)
    obj = OrderedDict([
        ('tanda', 'contrato'),
        ('salida', '%s/textos_en/contrato_en.json' % REL),
        ('formato_salida', '[{"estilo": "<uno de %s>", "texto": "<EN>"}, …] en el orden del documento; puedes añadir, '
                           'quitar o reordenar párrafos' % ', '.join(ESTILOS)),
        ('fuente_es', os.path.relpath(ES, PD) if ES.startswith(PD) else ES),
        ('n_parrafos_es', len(items)), ('n_palabras_es', sum(len(x['texto'].split()) for x in items)),
        ('cabecera_fija (literal)', CABECERA),
        ('reglas', REGLAS_COMUNES), ('decisiones_D230', DECISIONES),
        ('glosario', glo),
        ('verificacion', 'python3 %s/bp11.py check_contrato --todas' % REL),
        ('es', [OrderedDict([('i', i), ('estilo', x['estilo']), ('texto', x['texto'])]) for i, x in enumerate(items)]),
    ])
    p = os.path.join(AQUI, 'tandas', 'contrato.entrada.json')
    with open(p, 'w', encoding='utf-8') as fh:
        json.dump(obj, fh, ensure_ascii=False, indent=1)
        fh.write('\n')
    print('tandas/contrato.entrada.json: %d párrafos ES, %d palabras (fuente %s)' % (len(items), obj['n_palabras_es'],
                                                                                     obj['fuente_es']))
    return 0


RX_TOKEN = re.compile(r'__[A-Za-z][\w ]*__|\{\{|\}\}')
RX_NONREF = re.compile(r'(?i)\bnon-?refundable\b')
RX_COOLING_SI = re.compile(r'(?i)(?:cooling-off rule|16 CFR (?:part )?429)[^.]{0,80}\b(?:applies|gives (?:you|the client)|'
                           r'requires (?:us|the coffee caterer)|entitles)')
CLAVES = ('Retainer', 'Cancellation by the Client', 'Cancellation by the Coffee Caterer', 'not a penalty', 'Governing law',
          'Mutual responsibility', 'Entire agreement', 'Addendum', 'minimum sales guarantee', 'dedicated circuit',
          'additional insured', 'allergen', 'Rain plan', 'Force majeure', 'gratuit')


def check():
    if not os.path.exists(SALIDA):
        print('contrato_en.json: no existe (%s)' % SALIDA)
        return 1
    try:
        items = json.load(open(SALIDA, encoding='utf-8'))
    except ValueError as e:
        print('ERROR contrato_en.json no es JSON válido: %s' % e)
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
            avi.append('[%d] «non-refundable» con remisión (la revisión lo mira): «%s»' % (i, t[:90]))
        for m in RX_COOLING_SI.finditer(t):
            if 'whether' not in t[max(0, m.start() - 60):m.start()].lower():   # «ask your attorney whether … applies» vale
                err.append('[%d] afirma que la FTC Cooling-Off Rule aplica: «%s»' % (i, t[:90]))
        if re.search(r'(?i)\b\d+ to \d+ days\b(?! or)', t):
            avi.append('[%d] tramo «X to Y days»: ¿sin huecos? (usa «from X to less than Y»): «%s»' % (i, t[:90]))
    texto = '\n'.join(todo)
    if CABECERA not in [it.get('texto') for it in items[:6] if isinstance(it, dict)]:
        err.append('falta la CABECERA FIJA literal en los 6 primeros párrafos')
    for clave in CLAVES:
        if clave.lower() not in texto.lower():
            err.append('falta «%s» (D230)' % clave)
    if 'Cooling-Off' in texto and not re.search(r'(?i)ask your attorney whether', texto):
        err.append('menciona la Cooling-Off Rule sin «ask your attorney whether…»')
    h = [it['texto'] for it in items if isinstance(it, dict) and it.get('estilo') in ('H1', 'H2')]
    for x in err:
        print('ERROR', x)
    for x in avi:
        print('AVISO', x)
    print('contrato_en.json: %d párrafos · %d palabras · %d títulos · %s' % (
        len(items), len(texto.split()), len(h), 'OK' if not err else 'ROJO (%d errores)' % len(err)))
    return 1 if err else 0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--preparar', action='store_true')
    ap.add_argument('--todas', action='store_true')
    a = ap.parse_args()
    if a.preparar:
        return preparar()
    if a.todas:
        return check()
    ap.error('--preparar o --todas')


if __name__ == '__main__':
    sys.exit(main())
