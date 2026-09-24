#!/usr/bin/env python3
"""Recipe Costing Kit Pro (EN) · textos NUEVOS de Instrucciones que el ES no tiene.

Escribe `instrucciones_extra_en.json` (por fichero) y lo valida. Sesión Claude Code, 24-sep-2026.
Texto redactado por Claude (subagente Anthropic, regla 1bis); nunca bridge.py.

SPEC: D5 (moneda), D6 (impuesto por mercado), D7 (unidades), D11 (precios ilustrativos), D18 (licencia),
D19 (ventas netas), D20 (de la factura al precio por unidad + yield, cooking loss, escalado, subrecetas,
pesar secos), §2.5 (04 medidas y pour cost; 06 service charge y UK/AU; 11 método semanal; BONUS product mix),
remisiones a los libros 12 y 13, rutas de Google Sheets (D16: sin afirmar compatibilidad probada).

Todas las cifras que no son de oficio salen de `mercado_en.json` o de `mapas.py` (nada a mano): si cambia un
precio o una celda de tamaño, se regenera.

Uso:  python3 generar_instrucciones_extra.py [--check]   (--check: valida sin escribir)
"""
import json
import os
import re
import sys
from collections import OrderedDict

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)
import mapas  # noqa: E402

SALIDA = os.path.join(AQUI, 'instrucciones_extra_en.json')
MERCADO = json.load(open(os.path.join(AQUI, 'mercado_en.json'), encoding='utf-8'))
CENSO = json.load(open(os.path.join(AQUI, 'censo_es.json'), encoding='utf-8'))
TEXTOS_ES = json.load(open(os.path.join(AQUI, 'textos_es.json'), encoding='utf-8'))

# ------------------------------------------------------------------ cifras (derivadas, nunca a mano)
CONV = {r['clave']: r for r in mapas.conversions()}


def fila_conv(clave):
    return CONV[clave]['fila']


def factor(clave):
    return CONV[clave]['factor']


def usd(x):
    return '${:,.2f}'.format(x)


CAT = MERCADO['catalogo']
D12 = MERCADO['d12']
REC = {(r['libro'], r['hoja_en']): r for r in MERCADO['recetas']}

cif = OrderedDict()
# harina: saco de 50 lb de la plantilla, usada a 10 oz (D20)
cif['harina_precio'] = CAT['ap_flour']['precio']
assert CAT['ap_flour']['ud_compra'] == '50 lb bag'
cif['harina_10oz'] = round(cif['harina_precio'] / factor('50 lb bag→oz') * 10, 2)
# solomillo en catch weight (01 fila 5)
cif['solomillo_lb'] = CAT['beef_tenderloin']['precio']
r01 = REC[('01', 'Recipe Cost Card')]
f5 = [f for f in r01['filas'] if f['fila'] == 5][0]
assert f5['id'] == 'beef_tenderloin' and f5['ud_compra'] == 'lb'
cif['solomillo_racion_oz'] = f5['cantidad']
# libro 12: merma para la ficha y pérdida bruta
d12t = MERCADO['libro12']['despiece']
cif['merma_ficha_12'] = round(d12t['resultado']['merma_para_ficha'] * 100, 1)
cif['perdida_bruta_12'] = round((1 - d12t['resultado']['peso_util_lb'] / d12t['C8_peso_ap_lb']) * 100, 1)
# fondo de ternera de la 01 (subreceta)
fvs = [f for f in r01['filas'] if f['id'] == 'veal_stock'][0]
assert fvs['ud_compra'] == 'qt'
cif['fondo_qt'] = fvs['precio']
# aceite de freidora en el 08
r08 = REC[('08', 'Loaded Fries')]
assert any(f['id'] == 'fryer_oil' and f['ud_compra'] == 'lb' and f['ud_uso'] == 'oz' for f in r08['filas'])
assert CAT['fryer_oil']['formato13']['contenido'] == 35
# barril de 1/6 bbl del 04 (Bottle Sizes fila 12) a pintas de 16 fl oz
keg = [b for b in MERCADO['bottle_sizes'] if b.get('id') == 'keg'][0]
cif['keg_precio'] = keg['precio_botella']
cif['keg_floz'] = factor('1/6 bbl keg→fl oz')
cif['keg_pinta'] = round(cif['keg_precio'] / cif['keg_floz'] * 16, 2)
# Texas: margarita del 04 a su precio de carta de referencia, menos el 6,7 %
cif['margarita_precio'] = REC[('04', 'Margarita')]['precio_carta_ref']
cif['texas_neto'] = round(cif['margarita_precio'] * (1 - 0.067), 2)
# Aperol Spritz del 04 con el 3-2-1 clásico (2 fl oz de Aperol en lugar del pour de 1.5): pour cost (CHEF-18)
ras = REC[('04', 'Aperol Spritz')]
fap = [f for f in ras['filas'] if f['id'] == 'aperol'][0]
assert fap['ud_compra'] == 'L' and fap['ud_uso'] == 'fl oz' and fap['cantidad'] == 1.5
extra_ap = 0.5 / (1 - fap['merma']) * fap['precio'] / factor('L→fl oz') * (1 + ras['q_factor'])
cif['aperol_321_pc'] = round((ras['coste_racion'] + extra_ap) / ras['precio_carta_ref'] * 100)
cif['aperol_precio'] = ras['precio_carta_ref']
# Macarons del 05: precio mayorista de referencia y food cost en vitrina (CHEF-09)
rmac = REC[('05', 'Macarons')]
cif['macaron_mayorista'] = rmac['precio_carta_ref']
cif['macaron_vitrina'] = 2.75          # [estimado] vitrina en EE. UU., 2,50-3,50 $
cif['macaron_vitrina_fc'] = round(rmac['coste_racion'] / cif['macaron_vitrina'] * 100)
# celdas de tamaño de Conversions (D7): las únicas que edita un británico
cif['celda_bottle'] = 'B{}'.format(fila_conv('bottle→ml'))
cif['celda_can'] = 'B{}'.format(fila_conv('can→ml'))
assert CONV['bottle→ml']['tamano'] and CONV['can→ml']['tamano']
cif['bottle_ml'] = int(factor('bottle→ml'))
cif['can_ml'] = int(factor('can→ml'))
# US frente a imperial (NIST, desde mapas)
FLOZ = float(mapas.FLOZ_ML)
cif['pt_ml'] = round(16 * FLOZ)
cif['gal_l'] = round(128 * FLOZ / 1000, 3)
cif['floz_ml'] = round(FLOZ, 1)
cif['imp_pt_ml'] = round(float(mapas.IMP_GAL_ML) / 8)
cif['uk_floz_ml'] = round(float(mapas.IMP_GAL_ML) / 160, 1)
# BONUS: ración de solomillo del plato 1 en lb AP
pl1 = MERCADO['bonus']['platos'][0]
cif['bonus_solomillo_lb'] = round(pl1['por_racion']['Solomillo ternera'], 4)
# 06: valores por defecto del Event Quote
c06 = MERCADO['catering_06']
cif['c06'] = {k: c06[k] for k in ('C9_invitados_por_camarero', 'C12_coste_hora_camarero',
                                  'C14_coste_hora_jefe_sala', 'C17_rentals_por_invitado', 'C28_minimo')}
cif['w2_servidor'] = round(17.00 * 1.0765, 2)       # OEWS may-2025 + FICA 7,65 % (8b-A §4.4)
# 08: total diario del break-even
cif['be08_total'] = MERCADO['break_even_08']['total']
assert abs(sum(l['valor'] for l in MERCADO['break_even_08']['lineas']) - cif['be08_total']) < 0.01
# D12: rango del bar (pour cost)
cif['bar_min'] = int(round(D12['bar']['min'] * 100))
cif['bar_max'] = int(round(D12['bar']['max'] * 100))
cif['uk_gp_bar'] = '{}-{}%'.format(100 - cif['bar_max'], 100 - cif['bar_min'])
# 13: umbral de alerta
cif['umbral13'] = int(round(MERCADO['libro13']['umbral_alerta'] * 100))
# ejemplos de oficio (ilustrativos, marcados así en el texto)
cif['caja_6x5lb'] = (75.00, 30, round(75.00 / 30, 2))
cif['lata10'] = (105, 5.25, round(5.25 / 105, 2))
cif['lata10_caja_lb'] = 6 * 105 / 16
cif['uk_carta'] = (18.00, round(18.00 / 1.2, 2), round(18.00 * 0.8, 2))
cif['escalado'] = (10, 25, 25 / 10, 3, 3 * 25 / 10)

N_LIC = ("License: one business (all its locations) per purchase — use it with your clients, "
         "but don't hand out copies; schools: info@aichef.pro")
D11 = "Sample prices are illustrative U.S. references — replace them with your own supplier invoices."

# ------------------------------------------------------------------ bloques de texto
V = '▸ '


def b(t):
    return V + t


def d20(ctx):
    """D20 «From invoice to price per unit» (01-08)."""
    tpl01 = 'on "Recipe Cost Card"' if ctx['n'] == '01' else 'in template 01'
    fr08 = 'as "Loaded Fries" does' if ctx['n'] == '08' else 'as the Loaded Fries in template 08 does'
    caja = cif['caja_6x5lb']
    lata = cif['lata10']
    return ('From invoice to price per unit', [
        b("Price/Unit is what you pay for ONE purchase unit: fees included (a split-case fee, for instance), "
          "recoverable tax left out (UK VAT if you're VAT-registered; in the U.S., food bought for resale is "
          "usually exempt from sales tax)."),
        b("Catch weight (meat, fish or cheese billed by actual weight; the invoice line reads 1 case, 50.2 lb × "
          "price per lb): buy in lb or kg at the invoice price per lb or kg. The case doesn't matter. The tenderloin {} is "
          "bought this way, at {}/lb.".format(tpl01, usd(cif['solomillo_lb']))),
        b("Fixed-weight case that's on the dropdown (50 lb bag, 36x1 lb case, 4x1 gal case, 15 dz case…): "
          "pick it as Purchase unit and type the case price exactly as invoiced; the Factor divides it for you. "
          "A {} 50 lb bag of flour used at 10 oz costs {}.".format(usd(cif['harina_precio']), usd(cif['harina_10oz']))),
        b("Any other case: read the pack/size on the invoice (4/10 lb = 4 bags of 10 lb = 40 lb; 6/105 oz = six "
          "105 oz cans) and buy in lb, oz, gal or each, with Price/Unit = case price ÷ contents. Say a 6/5 lb "
          "case costs {}: that's {} lb, so {}/lb. The dropdown won't take a unit that isn't on its list."
          .format(usd(caja[0]), caja[1], usd(caja[2]))),
        b("#10 cans: the net weight depends on the product (96 to 117 oz, per the USDA Food Buying Guide), so "
          "there's no #10 unit. Buy in oz, with Price/Unit = can price ÷ the net weight on the label: a {} oz "
          "can at {} is {} per oz.".format(lata[0], usd(lata[1]), usd(lata[2]))),
        b("Fryer oil is sold by weight (a 35 lb jug-in-box) and shared by everything you fry. Leave it to the "
          "Q-factor, or cost it by weight: buy in lb and use in oz, {}.".format(fr08)),
    ])


def unidades(ctx):
    """D7: oz ≠ fl oz, US ≠ imperial, can ≠ #10, tamaños UK: qué celda editar (01-08)."""
    return ('Units: what to watch', [
        b("oz is weight, fl oz is volume. What you buy by weight (lb, oz, kg, g) you use by weight; what you buy "
          "by volume (gal, qt, pt, cup, fl oz, L, ml) you use by volume. Crossing over shows '?' and "
          "'check units', on purpose."),
        b("U.S. and imperial measures differ. In this kit pt, qt, gal, cup and fl oz are U.S. (1 pt = {} ml, "
          "1 gal = {} L, 1 fl oz = {} ml). An imperial pint is {} ml (use imp pt) and a UK fl oz is {} ml; in "
          "the UK, work in ml and L.".format(cif['pt_ml'], cif['gal_l'], cif['floz_ml'], cif['imp_pt_ml'],
                                             cif['uk_floz_ml'])),
        b("'can' on the list is a 12 fl oz ({} ml) beverage can, not a #10 food can (see above)."
          .format(cif['can_ml'])),
        b("UK sizes, exactly where: on \"Conversions\", cell {} (row bottle→ml, {}: type 700 for a 70 cl "
          "bottle) and cell {} (row can→ml, {}: type 330). Every bottle and can row reads those two cells. "
          "It's one size per workbook: if you buy 70 cl spirits and 75 cl wine, keep 'bottle' for the one you "
          "use most and cost the other in L.".format(cif['celda_bottle'], cif['bottle_ml'], cif['celda_can'],
                                                     cif['can_ml'])),
    ])


def yield_etc(ctx):
    """D20 textos breves: yield propio, cooking loss, escalado, subrecetas, pesar secos + remisión al 13."""
    porc = ctx.get('porciones', 'Number of portions')
    coste = ctx.get('coste', 'COST PER PORTION')
    fondo = 'The dark veal stock on "Recipe Cost Card"' if ctx['n'] == '01' else 'The dark veal stock in template 01'
    esc = cif['escalado']
    secos = ("Weigh dry goods; this template already works in grams, like most U.S. pastry kitchens. "
             if ctx['n'] == '05' else "Weigh dry goods. ")
    return ('Yield, cooking loss, scaling and sub-recipes', [
        b("Your own trim loss: weigh the product as it arrives and again once trimmed; trim loss % = 1 − trimmed "
          "weight ÷ AP weight. For whole cuts with trim you reuse (tips, chain, bones for stock), use template 12 "
          "(Yield Test): it credits those by-products, so the tenderloin's {}% raw loss becomes {}% for the card."
          .format(cif['perdida_bruta_12'], cif['merma_ficha_12'])),
        b("Cooking loss: if the quantity on the card is the COOKED portion (a 4 oz cooked patty), trim loss must "
          "include what's lost on the heat: 1 − (1 − trim loss) × (1 − cooking loss). The Cooking Loss Test tab "
          "of template 12 does the math. Or simply enter the raw weight."),
        b("Scaling: conversion factor = new yield ÷ old yield. Multiply every Quantity by it and set {} to the new "
          "yield (from {} to {}: factor {}, so {} lb becomes {} lb). {} doesn't change; the total does. "
          "Duplicate the tab first (right-click the tab → Move or Copy → Create a copy)."
          .format(porc, esc[0], esc[1], esc[2], esc[3], esc[4], coste.capitalize() if coste.isupper() else coste)),
        b("Sub-recipes ({}): cost the batch on its own card (a copy of the tab) with {} = the batch yield in the "
          "unit you'll use (e.g., {}) and Q-factor at 0%, so it isn't counted twice. On the main card, buy it in "
          "that unit: in Price/Unit type = and click the sub-recipe's {}.{}"
          .format(ctx.get('subrecetas', 'stocks, sauces, doughs'), porc, ctx.get('lote', '6 qt'), coste,
                  '' if ctx['n'] == '05' else
                  ' {} ({} a quart) is a placeholder for exactly that.'.format(fondo, usd(cif['fondo_qt'])))),
        b(secos + "The kit never converts volume to weight: a cup of flour weighs more or less depending on how "
          "it's filled. Enter flour, sugar and the like in oz or g; if a recipe says cups, weigh one cup of YOUR "
          "product once and use that weight. Pinches of salt and spices: weigh them or leave them to the "
          "Q-factor."),
        b("Keep your prices in template 13 (Ingredient Price List): it flags any ingredient that has gone up more "
          "than {}% since your cards were costed, so you know which cards to update.".format(cif['umbral13'])),
    ])


def impuesto(ctx):
    """D6: tabla por mercado, qué escribir y qué imprimir (01-08)."""
    uk = cif['uk_carta']
    return ('Tax by market: what to type and what to print', [
        b("U.S.: leave Tax rate (%) at 0%. Print the pre-tax suggested price; sales tax is added to the check "
          "(about 7.5% on average, state plus local). In Current menu price, type the price as printed."),
        b("UK: set 20% (VAT) and print the price incl. tax, since UK menus show VAT-inclusive prices. In Current "
          "menu price, type your menu price WITHOUT VAT, dividing by 1.20 rather than subtracting 20%: £{:.2f} on "
          "the menu is {:.2f}, not {:.2f}. Your GP % is 100% minus the actual food cost %."
          .format(uk[0], uk[1], uk[2])),
        b("Canada: as in the U.S., menus show prices before GST/HST (5-15%): leave 0%, or type your rate to see "
          "what the guest pays."),
        b("Australia: set 10% (GST) and print the price incl. tax; in Current menu price, type the menu price "
          "÷ 1.10."),
        b("Tips and service charges are never part of the price you cost against."),
    ])


def bar04(ctx):
    """§2.5 fila 04: medidas US/UK, pour cost por categoría (con cómo costearla) e impuestos del bar."""
    return ('Pours, pour cost and bar taxes', [
        b("U.S. standard pours: spirits 1.5 fl oz · wine 5 fl oz · beer 12 fl oz (bottle or can) · draft beer, "
          "usually a 16 fl oz pint."),
        b("UK legal measures: gin, rum, vodka and whisky in 25 ml or 35 ml (or multiples) · still wine by the "
          "glass in 125 ml or 175 ml (or multiples) · draft beer and cider in ⅓, ½ or ⅔ pint, or multiples of ½ "
          "pint. Pour in ml, and in imp pt for beer."),
        b("Spirits: buy in L (price per liter from \"Bottle Sizes\"), pour in fl oz (UK: ml). Pour cost 18-20%."),
        b("Wine by the glass: the same, from its 750 ml row on \"Bottle Sizes\" (or by the 12x750 ml case). Its "
          "pour cost runs higher than spirits."),
        b("Draft beer: buy in 1/6 bbl keg, 1/2 bbl keg or 50 L keg at the keg price, pour in fl oz (UK: imp pt). "
          "About 20%. A {} sixtel poured in 16 fl oz pints costs {} a pint before foam and line loss: put those "
          "in Trim loss %.".format(usd(cif['keg_precio']).replace('.00', ''), usd(cif['keg_pinta']))),
        b("Bottled and canned beer: buy by the 'can' or the 24x12 fl oz case, sell by the can. About 25%."),
        b("Aperol Spritz: the example uses a 1.5 fl oz house pour of Aperol. The classic 3-2-1 spec (3 parts "
          "prosecco, 2 Aperol, 1 soda) takes 2 fl oz and runs about {}% pour cost at {}: spritzes are wine-based "
          "and cost more than a spirit-forward drink.".format(cif['aperol_321_pc'],
                                                              usd(cif['aperol_precio']).replace('.00', ''))),
        b("Whole bar: {}-{}% pour cost, which a UK bar reads as {} GP. To cost a beer or a glass of wine, "
          "duplicate a cocktail tab (right-click the tab → Move or Copy → Create a copy)."
          .format(cif['bar_min'], cif['bar_max'], cif['uk_gp_bar'])),
        b("Taxes the bar pays on its drink sales come off the price before you judge pour cost. Texas, for "
          "example, charges the permit holder 6.7% of mixed-drink receipts, on top of the 8.25% sales tax the "
          "guest pays: for a {} margarita, type {:.2f} in Current menu price ({:.2f} × 0.933)."
          .format(usd(cif['margarita_precio']), cif['texas_neto'], cif['margarita_precio'])),
        b("UK: Alcohol Duty reaches you through your wholesaler's prices. Re-cost your drinks after each duty "
          "change (recent ones took effect on 1 February)."),
    ])


def catering06(ctx):
    """§2.5 fila 06: service charge opcional (B9), US/UK, UK/AU en Client Proposal, personal."""
    c = cif['c06']
    return ('Service charge, staff and tax on the proposal', [
        b("Markup on services (%) on \"Event Quote\" (C25) is YOUR internal margin on staff, rentals, transport "
          "and setup. It isn't a service charge and never shows on the proposal."),
        b("Optional service charge: if you bill one, give it its own line on \"Client Proposal\": in B9 the item "
          "(e.g., Service charge, 20% on food), in C9 type 1 and in D9 the amount (20% × Menu price for food, "
          "C26 on \"Event Quote\"). U.S. caterers often charge 18-22%. It stays out of the meal food cost % (C35), "
          "as it should: it isn't food revenue."),
        b("Then add one sentence to the note at the bottom, A15 (Review → Unprotect Sheet first): A 20% service "
          "charge on food is added to the final invoice; it is not a gratuity."),
        b("U.S.: a mandatory service charge is not a tip (DOL Fact Sheet #15). It's your revenue (if you pass it "
          "to staff, it's paid as wages) and it can be subject to sales tax: in New York it is, unless it's "
          "stated separately as a gratuity and paid in full to the staff. Check your state. A tip the client "
          "adds on top belongs to the staff and isn't part of your sales."),
        b("UK: under the Employment (Allocation of Tips) Act 2023, in force since 1 October 2024, every tip, "
          "gratuity and service charge, mandatory or optional, goes to the staff in full, so a service charge "
          "can never be your margin. A mandatory service charge carries 20% VAT; a freely given tip doesn't."),
        b("UK and Australia: set Tax rate (%) on \"Event Quote\" (C31) to 20% (VAT) or 10% (GST). Then unprotect "
          "\"Client Proposal\", change A15 to Prices include VAT (or GST) and add incl. VAT to the headings in D7 "
          "and B13."),
        b("U.S. and Canada: keep Tax rate (%) on \"Event Quote\" (C31) at 0%. \"Client Proposal\" takes the price "
          "per guest from C32, which already includes whatever rate C31 holds, and its note A15 says sales tax "
          "(GST/HST in Canada) is added to the final invoice: a rate in C31 would charge it twice."),
        b("Staffing guide, servers per guest: plated dinner 1:10-12 · buffet 1:20 · passed reception 1:{} (the "
          "default in Guests per server) · bar, 1 bartender per 50 guests.".format(c['C9_invitados_por_camarero'])),
        b("Staff rates are placeholders: {}/h per server sits between the W-2 cost of a banquet server (about "
          "{}: {} median wage + 7.65% payroll taxes) and an agency rate (about $30/h, often with a 4-hour "
          "minimum); the floor manager's {}/h keeps the same ratio. Rentals ({} a guest) and the {} minimum are "
          "placeholders too: replace them with what you pay."
          .format(usd(c['C12_coste_hora_camarero']).replace('.00', ''), usd(cif['w2_servidor']), usd(17.00),
                  usd(c['C14_coste_hora_jefe_sala']).replace('.00', ''), usd(c['C17_rentals_por_invitado']),
                  usd(c['C28_minimo']).replace('.00', ''))),
        b("UK staff costs: National Living Wage £12.71/h (21 and over, from April 2026) plus employer NIC."),
    ])


def calculadora10(ctx):
    return ('Which price goes on the menu', [
        b("U.S. and Canada: print Menu price (pre-tax); tax is added to the check. UK and Australia: print Menu "
          "price incl. tax, with C5 at 20% (VAT) or 10% (GST)."),
        b("UK kitchens talk GP %: GP % = 100% − food cost %, always on the price without VAT."),
    ])


def semanal11(ctx):
    """§2.5 fila 11 + R2-19: método semanal (solo texto)."""
    return ('Tracking by week', [
        b("Weekly works the same way: one row = one week. Count and value your inventory at the same moment every "
          "week (e.g., Sunday night after close), with current prices from template 13 (Ingredient Price List). "
          "Each week's ending inventory is next week's beginning inventory."),
        b("Purchases = invoices for goods delivered that week, minus credit memos, without recoverable tax. Net "
          "food sales = the week's POS food sales (drinks go in their own pour cost) without tax, service charges "
          "or tips."),
        b("To label the rows by week: Review → Unprotect Sheet, type Wk 1 to Wk 12 (or each week's start date) "
          "over the month names in column B (the chart uses them as labels), then Review → Protect Sheet. The "
          "total row already reads TOTAL (12 periods)."),
        b("One copy of the file holds 12 weeks, about a quarter: start a new copy for the next 12 and name each "
          "copy by its weeks."),
        b("Weekly numbers jump around: one Friday delivery can move a week by several points. Judge the 4-week "
          "trend and the 12-week total, not a single week."),
    ])


def pmix_bonus(ctx):
    """§2.5 fila BONUS + R2T-05: product mix del TPV, nunca sobre la columna A."""
    return ('Using your POS product mix', [
        b("Your POS already counts what you sold: Toast (Product mix), Square (Item sales), Clover (Item Sales), "
          "Lightspeed (Product Mix), Epos Now (Sales by Product). Run it for the same dates as your inventory "
          "count."),
        b("Set up \"Sales for the Period\" once: each dish in column A and, across its row, what ONE portion uses "
          "of each product: the AP qty from its recipe cost card, in the unit shown above the product (a {} oz "
          "tenderloin portion is {} lb AP once trim loss is in).".format(cif['solomillo_racion_oz'],
                                                                         cif['bonus_solomillo_lb'])),
        b("Every period, copy ONLY the units sold into column B, on the row of the matching dish. Never paste the "
          "export over column A: it comes in its own order, dishes would land next to another dish's recipe, "
          "and theoretical usage would be wrong with no warning."),
        b("There are 10 dish rows: fill them first with the dishes that use your most expensive products."),
    ])


REL = {
    '09': [b("Trim loss (what you trim off before cooking) goes in the recipe cost card, not in this log: measure "
             "it with template 12 (Yield Test) and type it in Trim loss % on the card. Log here only food that "
             "gets thrown away.")],
    '10': [b("Your cost per portion is only as good as its prices and trim loss: template 13 (Ingredient Price "
             "List) flags ingredients that have gone up more than {}%, and template 12 (Yield Test) measures the "
             "real trim loss of the cuts you break down.".format(cif['umbral13']))],
    '12': [b("Keep the whole cut's AP price in template 13 (Ingredient Price List). Re-run the test when the cut, "
             "the supplier or your trim spec changes, not every time the price moves: the Cost factor covers "
             "price changes."),
           b("Reference yields for many foods (as purchased to ready to cook, raw to cooked): USDA Food Buying "
             "Guide, foodbuyingguide.fns.usda.gov. A starting point; your own test wins.")],
    '13': [b("Whole cuts you break down: list the AP price per lb here. Their trim loss, with the credit for "
             "tips, chain or bones, comes from template 12 (Yield Test), not from this list.")],
    'BONUS': [b("Quantities per portion come from your recipe cost cards (with trim loss measured in template 12, "
                "Yield Test, where you have it); unit prices on \"Inventory\" from template 13 (Ingredient Price "
                "List), in the same unit you count in.")],
}


def unidades13(ctx):
    return ('Units and Invoice Formats', [
        b("Base unit: lb, L or each whenever you can, the units your recipe cost cards buy in. oz is weight and "
          "fl oz is volume: a row never mixes the two."),
        b("From the invoice to Format content: pack/size 4/10 lb = 40 (base unit lb); a catch-weight line billed "
          "per lb = 1, with the price per lb as Price of the format; six #10 cans (6/105 oz) = 630 oz = {:g} "
          "with base unit lb.".format(cif['lata10_caja_lb'])),
    ])


DV_EJEMPLOS = {
    'ficha': 'fl oz, 50 lb bag, Beef & red meat',
    '12': 'Usable, By-product, Trim (no value)',
    '13': 'lb, L, each',
    'BONUS': 'Expired, Spoiled, Overproduction',
}


def sheets(ctx):
    n = ctx['n']
    filas = [b("This file is built for Microsoft Excel. In Google Sheets: upload it to Google Drive, open it and "
               "choose File → Save as Google Sheets (Protect sheets and ranges isn't available while it's still "
               "an .xlsx). To go back: File → Download → Microsoft Excel (.xlsx).")]
    if n in ('01', '02', '03', '04', '05', '06', '07', '08', '09', '13'):
        filas.append(b("Paste values only: Ctrl+Shift+V (Mac: Cmd+Shift+V) or Edit → Paste special → Values only. "
                       "In Excel for Mac, Paste Special is Ctrl+Cmd+V."))
    dv = DV_EJEMPLOS.get('ficha' if n in ('01', '02', '03', '04', '05', '06', '07', '08') else n)
    if dv:
        filas.append(b("Protection: Data → Protect sheets and ranges. Dropdowns: Data → Data validation; if one "
                       "doesn't come across, type the value exactly as it appears on its list ({}): the formulas "
                       "read the text.".format(dv)))
    else:
        filas.append(b("Protection: Data → Protect sheets and ranges."))
    if n in ('01', '02', '03', '04', '05', '06', '07', '08', '12'):
        filas.append(b("Duplicate a tab: right-click the tab → Duplicate."))
    if n == '13':
        filas.append(b("Filter and sort: Data → Create a filter, then sort from the filter arrows so each price "
                       "stays on its ingredient's row."))
    if n in ('09', '11'):
        filas.append(b("If the chart looks different after converting, the numbers in the table don't change: "
                       "the chart only draws them."))
    return ('Using Google Sheets', filas)


def good(ctx):
    n = ctx['n']
    filas = [b("Amounts have no currency symbol: they're in your currency. The examples use U.S. dollars.")]
    if n in ('09', '10', '11'):
        filas.append(b("Sample amounts are illustrative U.S. figures — replace them with your own."))
    else:
        filas.append(b(D11))
    if n == '05':
        filas.append(b("Macarons: the example is priced wholesale to cafés ({} a piece), which is what puts it in the "
                       "25-35% range. At retail ({} in a pastry case) the same macaron runs about {}% food cost: its "
                       "cost is labor, not ingredients, so price retail macarons on labor time, not on the food cost "
                       "target.".format(usd(cif['macaron_mayorista']), usd(cif['macaron_vitrina']),
                                        cif['macaron_vitrina_fc'])))
    if n == '08':
        filas.append(b("The daily costs on \"Break-Even\" ({} a day: commissary, insurance and permits, fuel, "
                       "2 staff, truck depreciation, cleaning) are U.S. placeholders. Replace them with yours."
                       .format(usd(cif['be08_total']).replace('.00', ''))))
    if n == '12':
        filas.append(b("Working in metric (UK): enter weights in kg, the price per kg and the portion in g, and set "
                       "Ounces per pound (for the portion) to 1000 on both tabs; labels that say lb then read kg. "
                       "The formulas only need consistent units."))
    filas.append(N_LIC)          # D18, literal y sin viñeta
    return ('Good to know', filas)


# ------------------------------------------------------------------ composición por fichero
FICHA = ['01', '02', '03', '04', '05', '06', '07', '08']
PLAN = OrderedDict()
for n in FICHA:
    bl = [d20, unidades, yield_etc, impuesto]
    if n == '04':
        bl.append(bar04)
    if n == '06':
        bl.append(catering06)
    bl += [sheets, good]
    PLAN[n] = bl
PLAN['09'] = ['REL', sheets, good]
PLAN['10'] = [calculadora10, 'REL', sheets, good]
PLAN['11'] = [semanal11, sheets, good]
PLAN['12'] = ['REL', sheets, good]
PLAN['13'] = [unidades13, 'REL', sheets, good]
PLAN['BONUS'] = [pmix_bonus, 'REL', sheets, good]

CTX_EXTRA = {'05': {'porciones': 'Yield (units per batch)', 'coste': 'COST PER UNIT',
                    'subrecetas': 'pastry cream, doughs, glazes', 'lote': '2,000 g'}}
TITLE_CASE = {'12', '13'}          # sus Instrucciones ES van en Title Case («Para Qué Sirve»)
_MINUS = {'and', 'or', 'of', 'to', 'the', 'a', 'an', 'in', 'on', 'per', 'by', 'for', 'vs.'}


def titulo(t, n):
    if n not in TITLE_CASE:
        return t
    pal = t.split(' ')
    return ' '.join(p if (i and p in _MINUS) else p[:1].upper() + p[1:] for i, p in enumerate(pal))


def libro_es(n):
    return [f for f in mapas.LIBROS_ES if f.startswith(n)][0]


def construir():
    ficheros = OrderedDict()
    for n, bloques in PLAN.items():
        f_es = libro_es(n)
        f_en = mapas.FICHEROS[f_es]
        ctx = dict(n=n, **CTX_EXTRA.get(n, {}))
        filas = []
        for blo in bloques:
            if blo == 'REL':
                tit, vs = titulo('Related templates', n), REL[n]
                spec = 'remisiones 12/13'
            else:
                tit, vs = blo(ctx)
                tit = titulo(tit, n)
                spec = blo.__name__
            filas.append({'tipo': 'titulo', 'texto': tit, 'bloque': spec})
            filas.append({'tipo': 'vacia'})
            for v in vs:
                filas.append({'tipo': 'linea' if v == N_LIC else 'vineta', 'texto': v, 'bloque': spec})
            filas.append({'tipo': 'vacia'})
        ficheros[f_en] = OrderedDict([
            ('fichero_es', f_es),
            ('hoja', 'Instructions'),
            ('n_filas', len(filas)),
            ('filas', filas),
        ])
    return ficheros


NOTAS = [
    OrderedDict([
        ('ficheros', [mapas.FICHEROS[libro_es(n)] for n in FICHA]),
        ('hoja_en', 'Trim Loss Factors'), ('celda', 'A2'), ('spec', 'D9 (yield = 100 % − trim loss)'),
        ('es', 'La «típica» es la que se precarga en las filas vacías del escandallo al elegir categoría. '
               'Ajústala a tu proveedor.'),
        ('en', 'Typical is the trim loss % that preloads in the empty rows of the recipe cost card when you pick '
               'a category. Adjust it to your supplier. Yield % = 100% − trim loss %.'),
    ]),
    OrderedDict([
        ('ficheros', [mapas.FICHEROS[libro_es(n)] for n in FICHA]),
        ('hoja_en', 'Trim Loss Factors'), ('celda', 'A3'), ('spec', 'D20 (remite al 12 y al USDA Food Buying Guide)'),
        ('es', 'Mide tu merma real con la plantilla 12 (Test de Rendimiento) y llévala a «Merma (%)» de la ficha.'),
        ('en', 'Measure your real trim loss with template 12 (Yield Test) and type it in Trim loss % on the cost '
               'card. Reference yields for many foods: USDA Food Buying Guide (foodbuyingguide.fns.usda.gov).'),
    ]),
]

# Celdas NUEVAS (vacías en el ES) en «Trim Loss Factors»: columna E de notas, fuera de la DV (A5:A25) y del
# VLOOKUP (A5:C25). Revisión R1 EN: CHEF-04 (pescado) y CHEF-19 (verdura de hoja con tallos y flores).
NOTAS_NUEVAS = [
    OrderedDict([('ficheros', [mapas.FICHEROS[libro_es(n)] for n in FICHA]), ('hoja_en', 'Trim Loss Factors'),
                 ('celda', 'E4'), ('estilo_de', 'D4'), ('ancho_columna', 62), ('en', 'Notes')]),
    OrderedDict([('ficheros', [mapas.FICHEROS[libro_es(n)] for n in FICHA]), ('hoja_en', 'Trim Loss Factors'),
                 ('celda', 'E7'), ('estilo_de', 'A7'),
                 ('en', 'Gutted, head-on fish cut on the bone. Whole round fish to skin-on fillet loses 50-60%: '
                        'measure it with template 12.')]),
    OrderedDict([('ficheros', [mapas.FICHEROS[libro_es(n)] for n in FICHA]), ('hoja_en', 'Trim Loss Factors'),
                 ('celda', 'E9'), ('estilo_de', 'A9'),
                 ('en', 'Also stems and flowers, such as asparagus and cauliflower.')]),
]

# ------------------------------------------------------------------ gates
NO_LATINO = re.compile('[Ѐ-ӿ֐-׿؀-ۿ฀-๿ᄀ-ᇿ぀-ヿ'
                       '㐀-䶿一-鿿가-힯]')
PERMITIDOS = set('▸—→×÷−≈⅓½⅔£·…é')        # é: café (CHEF-09)
RESTOS_ES = re.compile(r'\b(de|del|la|las|el|los|que|para|con|por|una|ficha|merma|escandallo|plantilla|hoja|'
                       r'ración|raciones|precio|coste|compra|IVA|PVP|ud|docena|botella|lata)\b')
UK_SPELL = re.compile(r'\b(litre|litres|colour|centre|flavour|favourite|organise|analyse)\b', re.I)
ORDEN = re.compile(r'\bentr[ée]e\b', re.I)


def validar(ficheros):
    fallos, avisos = [], []
    hojas_en = {v['nombre_en']: v['hojas_en'] for v in CENSO['libros'].values()}
    for f_en, d in ficheros.items():
        n = f_en.split('-')[0]
        tabs = hojas_en[f_en]
        textos = [r['texto'] for r in d['filas'] if r['tipo'] != 'vacia']
        if N_LIC not in textos:
            fallos.append('%s: falta la línea de licencia D18' % f_en)
        if n not in ('09', '10', '11') and V + D11 not in textos:
            fallos.append('%s: falta la línea D11' % f_en)
        for t in textos:
            ctx = '%s: %s' % (f_en, t[:60])
            if NO_LATINO.search(t):
                fallos.append('carácter no latino · ' + ctx)
            for ch in t:
                if ord(ch) > 127 and ch not in PERMITIDOS:
                    fallos.append('carácter fuera de la lista (%r) · %s' % (ch, ctx))
            if '€' in t or re.search('[¿¡«»ºª]', t):
                fallos.append('signo español o € · ' + ctx)
            m = RESTOS_ES.search(t)
            if m:
                fallos.append('resto de español (%s) · %s' % (m.group(0), ctx))
            if UK_SPELL.search(t):
                fallos.append('ortografía UK · ' + ctx)
            if ORDEN.search(t):
                fallos.append('«entrée» (D8) · ' + ctx)
            if re.search(r'\bwaste\b', t, re.I) and n not in ('09', 'BONUS'):
                fallos.append('«waste» fuera de 09/BONUS (D8) · ' + ctx)
            for q in re.findall(r'"([^"]+)"', t):
                if q not in tabs:
                    fallos.append('comillas dobles que no son una pestaña del libro (%r) · %s' % (q, ctx))
            if len(t) > 420:
                avisos.append('línea larga (%d) · %s' % (len(t), ctx))
            if re.search(r'\d,\d{1,2}\b(?!\d)', t) and not re.search(r'\d{1,3}(,\d{3})+', t):
                fallos.append('posible coma decimal · ' + ctx)
    # notas: la cadena ES existe tal cual en el ES v2.1 y el EN pasa los mismos filtros
    cadenas_es = {c['es'] if isinstance(c, dict) else c for c in
                  (TEXTOS_ES['cadenas'] if isinstance(TEXTOS_ES, dict) and 'cadenas' in TEXTOS_ES else TEXTOS_ES)}
    for nota in NOTAS_NUEVAS:
        if NO_LATINO.search(nota['en']) or RESTOS_ES.search(nota['en']) or '"' in nota['en']:
            fallos.append('nota nueva EN con restos o comillas: ' + nota['en'][:60])
    for nota in NOTAS:
        if nota['es'] not in cadenas_es:
            fallos.append('nota: cadena ES no encontrada en textos_es.json: ' + nota['es'][:60])
        if NO_LATINO.search(nota['en']) or RESTOS_ES.search(nota['en']) or '"' in nota['en']:
            fallos.append('nota EN con restos o comillas: ' + nota['en'][:60])
    return fallos, avisos


def main():
    ficheros = construir()
    fallos, avisos = validar(ficheros)
    out = OrderedDict([
        ('_leeme', [
            'Recipe Costing Kit Pro (EN): textos de Instrucciones que el ES no tiene. Lo genera '
            'generar_instrucciones_extra.py (no se edita a mano); cifras de mercado_en.json y mapas.py. '
            'Sesión Claude Code, 2026-09-24. Redactado por Claude (regla 1bis), sin bridge.py.',
            'aplicar_en.py: en la hoja Instructions de cada libro, insertar «filas» en la columna B justo ANTES de '
            'la fila del pie de marca (ancla), después de traducir. La fila en blanco que ya precede al ancla separa '
            'lo existente del primer título nuevo; cada sección acaba con su propia fila vacía. Solo texto: ninguna '
            'fórmula, DV, CF ni área de impresión (Instructions no tiene).',
            'Estilos: copiar los de las filas ES (titulo = el de «Cómo usar esta plantilla»; vineta y linea = el de '
            'una fila «▸»); altura automática; ajuste de texto y alineación superior, como el ES.',
            '«notas_existentes»: sustituyen a la traducción de textos_en de esa cadena ES en esa hoja (misma regla que '
            'textos_cifra_derivada de mercado_en.json).',
            'Comillas: las dobles rectas solo citan pestañas DEL MISMO libro (D9, R2T-18); las pestañas de otro libro '
            'y los rótulos van sin comillas; los valores a teclear, entre comillas simples.',
        ]),
        ('fecha', '2026-09-24'),
        ('insercion', OrderedDict([
            ('hoja', 'Instructions'),
            ('columna', 'B'),
            ('posicion', 'antes_del_ancla'),
            ('ancla_es', '— Kit de Escandallos Pro · AI Chef Pro · aichef.pro'),
            ('ancla_en', '— Recipe Costing Kit Pro · AI Chef Pro · aichef.pro'),
            ('estilos', OrderedDict([
                ('titulo', {'font': 'Calibri', 'size': 12, 'bold': True, 'color': '001A1A1A', 'wrap': True,
                            'vertical': 'top'}),
                ('vineta', {'font': 'Calibri', 'size': 11, 'bold': False, 'color': '00333333', 'wrap': True,
                            'vertical': 'top'}),
                ('linea', {'font': 'Calibri', 'size': 11, 'bold': False, 'color': '00333333', 'wrap': True,
                           'vertical': 'top'}),
            ])),
        ])),
        ('cifras', OrderedDict((k, v) for k, v in cif.items())),
        ('linea_licencia_d18', N_LIC),
        ('linea_d11', D11),
        ('rangos_para_lista_blanca', [
            {'rango': '18-20%', 'contexto': '04, pour cost de destilados'},
            {'rango': '%d-%d%%' % (cif['bar_min'], cif['bar_max']), 'contexto': '04, bar entero (D12 bar)'},
            {'rango': cif['uk_gp_bar'], 'contexto': '04, GP UK equivalente al pour cost D12 (100 − 18-24)'},
            {'rango': '5-15%', 'contexto': '01-08, GST/HST de Canadá (D6)'},
            {'rango': '18-22%', 'contexto': '06, service charge de catering en EE. UU.'},
            {'rango': '1:10-12 · 1:20 · 1:25', 'contexto': '06, ratios de personal'},
            {'rango': '96 to 117 oz', 'contexto': '01-08, peso neto de la lata #10 (USDA FBG)'},
            {'rango': '50-60%', 'contexto': '01-08 Trim Loss Factors!E7, merma de pescado entero a filete'},
        ]),
        ('ficheros', ficheros),
        ('notas_existentes', NOTAS),
        ('notas_nuevas', NOTAS_NUEVAS),
        ('validacion', OrderedDict([('fallos', fallos), ('avisos', avisos)])),
    ])
    total = sum(d['n_filas'] for d in ficheros.values())
    print('ficheros: %d · filas nuevas: %d · notas: %d · fallos: %d · avisos: %d'
          % (len(ficheros), total, len(NOTAS), len(fallos), len(avisos)))
    for f_en, d in ficheros.items():
        tx = sum(1 for r in d['filas'] if r['tipo'] in ('vineta', 'linea'))
        print('  %-44s %3d filas (%d de texto)' % (f_en, d['n_filas'], tx))
    for x in fallos:
        print('FALLO', x)
    for x in avisos:
        print('aviso', x)
    if '--check' not in sys.argv:
        with open(SALIDA, 'w', encoding='utf-8') as fh:
            json.dump(out, fh, ensure_ascii=False, indent=1)
            fh.write('\n')
        print('escrito', SALIDA)
    return 1 if fallos else 0


if __name__ == '__main__':
    sys.exit(main())
