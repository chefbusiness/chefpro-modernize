#!/usr/bin/env python3
"""Ficha técnica de pratos (PT), modelo Excel GRATIS — lead magnet de /pt/blog/ficha-tecnica-de-pratos.

LowFruits PT (nov-2026): «ficha técnica cozinha excel» 30/mes.
Gemelo portugués de plantilla-ficha-tecnica-gratis.py (ES) con lo ya auditado en los gemelos FR y NL
(plantilla-fiche-technique-fr.py, plantilla-receptuur-nl.py), ADAPTADO al post PT:
  - el ejemplo es el del post (filetes de pescada panados, 10 doses): capitação 160 g limpos de 230 g brutos
    (rendimento 69,6 %, «cerca de 70 %»), 2,30 kg brutos × 7,50 €/kg = 17,25 € + 6,40 € de «ovo, pão ralado, óleo,
    arroz e limão» (valor fechado) = 23,65 € → 2,365 € por dose → 11,00 € sem IVA → food cost 21,5 % · encomenda de
    40 doses = 9,2 kg brutos. Sin tiempos ni temperaturas (el post no los fija);
  - el peso BRUTO se escribe (se pesa una dose una vez, como dice el post) y el rendimento se calcula
    (limpo ÷ bruto); bruto vacío = sin pérdidas. El coste se calcula en la ficha (como el FR) sobre el bruto;
  - IVA editable al 13 % (comida en restauração, continente) con nota de 23 % / Madeira 12 % / Açores 9 %;
  - los 14 alergénios con su nombre oficial PT-PT y dos columnas para marcar con «X»: «Contém» y «Pode conter
    (contaminação cruzada)», más «Qual / em que ingrediente»; nota DL 26/2016, art. 4.º;
  - conservação y pontos críticos remiten al plano HACCP / Código de Boas Práticas da AHRESP (ninguna cifra);
  - aviso visible (fórmula) si una fila tiene cantidad y no tiene precio, o lleva texto en vez de número;
  - 2 hojas: «Exemplo (pescada)» y «Ficha em branco» (activa), mismas celdas y fórmulas (como el FR).
Sale: astro-site/public/descargas/ficha-tecnica-cozinha-excel-gratis-aichef.xlsx
El xlsx pasa por inject_cache.py + caché «texto vacío» (como el NL/DE), un gate data_only, un gate pycel sobre una
COPIA sin caché (las cifras del post salen de las fórmulas), un gate de idioma (nada de español, brasileirismos ni
grafías anteriores al AO90; ninguna temperatura) y parche_xml_xlsx.py --check. `/descargas/*` está en noindex
(netlify.toml). Sesión Claude Code, 25-nov-2026.
"""
import contextlib
import logging
import os
import re
import shutil
import subprocess
import sys
import tempfile
import textwrap
import zipfile
from pathlib import Path

from openpyxl import Workbook, load_workbook
from openpyxl.formatting.rule import FormulaRule
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
from openpyxl.worksheet.datavalidation import DataValidation

RAIZ = Path(__file__).resolve().parents[2]
SALIDA = RAIZ / 'astro-site/public/descargas/ficha-tecnica-cozinha-excel-gratis-aichef.xlsx'
INJECT = RAIZ / 'scripts/productos-digitales/inject_cache.py'
PARCHE = RAIZ / 'scripts/productos-digitales/parche_xml_xlsx.py'
GUIA = 'https://aichef.pro/pt/blog/ficha-tecnica-de-pratos'
CALC = 'https://aichef.pro/pt/calculadora-food-cost-restaurante'
H_EX, H_BR = 'Exemplo (pescada)', 'Ficha em branco'

PRETO, DOURADO, CINZA = '111111', 'FFD700', 'F3F3F3'
fino = Side(style='thin', color='BBBBBB')
borda = Border(left=fino, right=fino, top=fino, bottom=fino)
entrada = PatternFill('solid', fgColor='FFF8D6')
cinza = PatternFill('solid', fgColor=CINZA)
erro = PatternFill('solid', fgColor='FBE3E3')
NB = ' '  # espaço não separável entre o número e a unidade («21,5 %»)
EUR = '#,##0.00 "€"'
EUR3 = '#,##0.000 "€"'  # custo por dose com 3 casas, como no artigo (2,365 €)
EUR_KG = '#,##0.00 "€/kg"'
KG = '#,##0.000'
G = '#,##0'
PCT0 = f'0"{NB}"%'
PCT1 = f'0.0"{NB}"%'
COLS = 9  # A–I

# Exemplo do artigo: (ingrediente, capitação limpa g/dose, bruto g/dose, preço €/kg bruto, alergénios)
EXEMPLO = [('Pescada', 160, 230, 7.50, 'Peixes')]
FORFAIT_EX = ('Ovo, pão ralado, óleo, arroz e limão (valor fechado do exemplo)', 6.40,
              'Ovos; cereais que contêm glúten (pão ralado)')
FORFAIT_BR = 'Sal, temperos e outros (valor fixo)'
PASSOS = ['Temperar a pescada limpa.', 'Passar os filetes por ovo e depois por pão ralado.', 'Fritar.',
          'Servir com o arroz e o limão.']
ALERGENIOS = [
    'Cereais que contêm glúten (trigo, espelta, trigo Khorasan, centeio, cevada, aveia ou estirpes hibridizadas: '
    'indicar qual)',
    'Crustáceos', 'Ovos', 'Peixes', 'Amendoins', 'Soja', 'Leite (incluindo lactose)',
    'Frutos de casca rija (amêndoas, avelãs, nozes, castanhas de caju, nozes pécan, castanhas do Brasil, pistácios, '
    'nozes de macadâmia ou do Queensland: indicar qual)',
    'Aipo', 'Mostarda', 'Sementes de sésamo', 'Dióxido de enxofre e sulfitos (> 10 mg/kg ou 10 mg/l em SO2)',
    'Tremoço', 'Moluscos',
]
assert len(ALERGENIOS) == 14
ROTULO = 'Confirmar no rótulo do pão ralado'
ALERG_EX = {0: ('X', 'Pão ralado: indicar o cereal que está no rótulo'), 2: ('X', 'Ovo do panado'),
            3: ('X', 'Pescada'), 6: (None, ROTULO), 9: (None, ROTULO)}
HACCP = 'segundo o seu plano HACCP / Código de Boas Práticas da AHRESP'
IVA_NOTA = (f'IVA na restauração (continente): 13{NB}% na comida; 23{NB}% nas bebidas alcoólicas e nos refrigerantes '
            f'(Código do IVA, Lista II, verba 3.1). Madeira: 12{NB}%. Açores: 9{NB}%.')
NOTA_ING = (f'Peso bruto vazio = sem perdas (rendimento de 100{NB}%). Pese uma dose a sério, uma vez: o bruto é o que '
            'se compra; a capitação é o que vai para o prato.')
NOTA_PREP = 'Os tempos e o ponto são os da sua praça, medidos no serviço: a ficha não os inventa.'
NOTA_ALG = ('A informação de alergénios tem de estar disponível por escrito para o cliente (Decreto-Lei n.º 26/2016, '
            'art. 4.º). Num produto composto, a fonte é o rótulo: mudou a marca, muda a ficha.')
NOTA_CONS = (f'Temperaturas, prazos e limites: {HACCP}. A ficha técnica é uma das entradas do plano HACCP, '
             'não o plano.')
NOTA_FC = ('O food cost calcula-se sobre o preço sem IVA e com os custos das faturas sem IVA: misturar o imposto '
           'baixa o food cost no papel.')
NOTA_TEOR = ('É a conta teórica de uma dose. O food cost do mês (existências, compras e vendas do período) é outra '
             'conta: a diferença é o que se perdeu entre a ficha e a caixa.')
RODAPE_GUIA = 'Modelo gratuito do AI Chef Pro · Guia:'
RODAPE_CALC = 'Calculadora de food cost gratuita:'
BRUTO_KO = 'verifique o bruto'
AVISO_1 = ('Atenção: 1 linha tem quantidade, mas não tem preço (ou tem texto em vez de um número). '
           'O custo está incompleto.')
AVISO_N = (' linhas têm quantidade, mas não têm preço (ou têm texto em vez de um número). '
           'O custo está incompleto.')

# Linhas fixas (as duas folhas têm a mesma estrutura → as mesmas células)
R_DOSES, R_ENC = 7, 8
R_TIT_ING, R_CAB = 14, 15
R_ING1, N_ING = 16, 15
R_INGN = R_ING1 + N_ING - 1          # 30
R_FORF = R_INGN + 1                  # 31
R_AVISO, R_NOTA_ING = R_FORF + 1, R_FORF + 2   # 32, 33
R_TIT_PREP = R_NOTA_ING + 2          # 35
R_PASSO1, N_PASSOS = R_TIT_PREP + 2, 8         # 37–44
R_NOTA_PREP = R_PASSO1 + N_PASSOS    # 45
R_TIT_ALG = R_NOTA_PREP + 2          # 47
R_ALG1 = R_TIT_ALG + 2               # 49
R_ALGN = R_ALG1 + 13                 # 62
R_NOTA_ALG = R_ALGN + 1              # 63
R_TIT_CONS = R_NOTA_ALG + 2          # 65
R_NOTA_CONS = R_TIT_CONS + 4         # 69
R_TIT_EMP = R_NOTA_CONS + 2          # 71
R_TIT_PRECO = R_TIT_EMP + 5          # 76
R_CT, R_CD, R_PV, R_FC, R_IVA, R_PCI = range(R_TIT_PRECO + 1, R_TIT_PRECO + 7)   # 77–82
R_NOTA_FC = R_PCI + 2                # 84
R_RODAPE = R_NOTA_FC + 3             # 87
K = f'IF(N($B${R_DOSES})>1,$B${R_DOSES},1)'
CUSTOS = f'G{R_ING1}:G{R_FORF}'


def n_aviso():
    b, c, g = (f'{x}{R_ING1}:{x}{R_INGN}' for x in 'BCG')
    return f'SUMPRODUCT(SIGN(({b}<>"")+({c}<>""))*(1-ISNUMBER({g})))'


# ---------------------------------------------------------------- estilo
def barra(ws, linha, texto, ate=COLS):
    c = ws.cell(row=linha, column=1, value=texto)
    c.font = Font(bold=True, color='FFFFFF')
    c.fill = PatternFill('solid', fgColor=PRETO)
    ws.merge_cells(start_row=linha, start_column=1, end_row=linha, end_column=ate)


def cel(ws, linha, col, valor=None, fmt=None, inp=False, negrito=False, cinzento=False):
    c = ws.cell(row=linha, column=col, value=valor)
    c.border = borda
    if fmt:
        c.number_format = fmt
    if inp:
        c.fill = entrada
    elif cinzento:
        c.fill = cinza
    if negrito:
        c.font = Font(bold=True)
    c.alignment = Alignment(wrap_text=True, vertical='top')
    return c


def juntar(ws, linha, c0, c1):
    for c in range(c0 + 1, c1 + 1):
        ws.cell(row=linha, column=c).border = borda
    ws.merge_cells(start_row=linha, start_column=c0, end_row=linha, end_column=c1)


def alto(ws, linha, *textos_e_larguras):
    """Altura explícita (15 pt por linha estimada): o Excel não ajusta sozinho as linhas com células juntas."""
    linhas = max(len(textwrap.wrap(t, w)) if t else 1 for t, w in textos_e_larguras)
    if linhas > 1:
        ws.row_dimensions[linha].height = max(ws.row_dimensions[linha].height or 0, 15 * linhas + 2)


def nota(ws, linha, texto, c0=1, c1=COLS, largura=130):
    c = ws.cell(row=linha, column=c0, value=texto)
    c.font = Font(italic=True, color='555555')
    c.alignment = Alignment(wrap_text=True, vertical='top')
    ws.merge_cells(start_row=linha, start_column=c0, end_row=linha, end_column=c1)
    alto(ws, linha, (texto, largura))


def dv(ws, tipo, op, f1, f2, titulo, msg):
    d = DataValidation(type=tipo, operator=op, formula1=f1, formula2=f2, allow_blank=True, showErrorMessage=True,
                       errorTitle=titulo, error=msg)
    ws.add_data_validation(d)
    return d


# ---------------------------------------------------------------- folha
def folha(wb, nome, ex):
    ws = wb.create_sheet(nome)
    ws['A1'] = 'Ficha técnica de pratos'
    ws['A1'].font = Font(bold=True, size=16, color=DOURADO)
    ws['A1'].fill = PatternFill('solid', fgColor=PRETO)
    ws.merge_cells(start_row=1, start_column=1, end_row=1, end_column=COLS)
    ws.row_dimensions[1].height = 26
    instr = ('Exemplo do artigo: filetes de pescada panados, 10 doses. Os valores são um exemplo, não uma fatura. '
             f'Para os seus pratos, use a folha «{H_BR}».') if ex else \
        ('Preencha as células amarelas. O rendimento, o peso bruto a comprar, o custo e o food cost calculam-se '
         'sozinhos.')
    nota(ws, 2, instr)

    d_num = dv(ws, 'decimal', 'greaterThanOrEqual', '0', None, 'Valor inválido',
               'Escreva só o número, igual ou maior do que 0 (por exemplo 160 ou 7,50).')
    d_doses = dv(ws, 'whole', 'greaterThanOrEqual', '1', None, 'Doses', 'Escreva um número inteiro de doses, de 1 para cima.')

    # Dados gerais (5–12)
    barra(ws, 4, 'Dados gerais')
    dados = [('Prato', 'Filetes de pescada panados, com arroz e limão' if ex else None),
             ('Categoria', 'Peixe' if ex else None),
             ('Doses da ficha', 10 if ex else None), ('Doses para a encomenda', 40 if ex else None),
             ('Tempo de preparação', None), ('Autor', None), ('Verificado por', None),
             ('Data e versão', 'dd-mm-aaaa · v1.0')]
    for i, (k, v) in enumerate(dados):
        f = 5 + i
        cel(ws, f, 1, k, negrito=True)
        if f in (R_DOSES, R_ENC):
            d_doses.add(cel(ws, f, 2, v, '0', inp=True).coordinate)
            txt = ('O custo por porção é o custo das doses da ficha a dividir por este número.' if f == R_DOSES else
                   'As doses que vai preparar: a última coluna dos ingredientes mostra o bruto a encomendar.')
            nota(ws, f, txt, 3, COLS, 100)
        else:
            cel(ws, f, 2, v, inp=True)
            juntar(ws, f, 2, COLS)

    # Ingredientes
    barra(ws, R_TIT_ING, 'Ingredientes: capitação e peso bruto por dose; custo para as doses da ficha')
    cab = ['Ingrediente', 'Capitação: peso limpo por dose (g ou ml)', 'Peso bruto por dose (g ou ml)',
           'Rendimento (limpo ÷ bruto)', 'Bruto para as doses da ficha (kg ou L)',
           'Preço de compra sem IVA (€/kg ou €/L)', 'Custo para as doses da ficha (€)', 'Alergénios que traz',
           'Bruto para a encomenda (kg ou L)']
    for col, txt in enumerate(cab, start=1):
        c = cel(ws, R_CAB, col, txt, negrito=True, cinzento=True)
        c.alignment = Alignment(wrap_text=True, vertical='center', horizontal='center')
    ws.row_dimensions[R_CAB].height = 62
    linhas = (EXEMPLO if ex else []) + [None] * (N_ING - (len(EXEMPLO) if ex else 0))
    for i, item in enumerate(linhas):
        f = R_ING1 + i
        nome_i, limpo, bruto, preco, alg = item if item else (None, None, None, None, None)
        cel(ws, f, 1, nome_i, inp=True)
        d_num.add(cel(ws, f, 2, limpo, G, inp=True).coordinate)
        d_num.add(cel(ws, f, 3, bruto, G, inp=True).coordinate)
        # rendimento = limpo ÷ bruto; bruto vazio = 100 %; bruto com texto ou ≤ 0 → aviso
        cel(ws, f, 4, f'=IF(OR(B{f}="",NOT(ISNUMBER(B{f}))),"",IF(C{f}="",1,'
                      f'IF(AND(ISNUMBER(C{f}),N(C{f})>0),B{f}/C{f},"{BRUTO_KO}")))', PCT1, cinzento=True)
        # bruto para as doses da ficha (kg) = bruto por dose (ou a capitação, se não há bruto) × doses ÷ 1000
        cel(ws, f, 5, f'=IF(C{f}="",IF(ISNUMBER(B{f}),B{f}*{K}/1000,""),'
                      f'IF(AND(ISNUMBER(C{f}),N(C{f})>0),C{f}*{K}/1000,""))', KG, cinzento=True)
        d_num.add(cel(ws, f, 6, preco, EUR_KG, inp=True).coordinate)
        cel(ws, f, 7, f'=IF(OR(E{f}="",NOT(ISNUMBER(F{f}))),"",ROUND(E{f}*F{f},2))', EUR, cinzento=True)
        cel(ws, f, 8, alg, inp=True)
        cel(ws, f, 9, f'=IF(OR(E{f}="",N($B${R_ENC})<=0),"",IF(C{f}="",B{f},C{f})*$B${R_ENC}/1000)', KG,
            cinzento=True)
    # linha de valor fixo: o custo escreve-se à mão (como no artigo: 6,40 € nas 10 doses)
    cel(ws, R_FORF, 1, FORFAIT_EX[0] if ex else FORFAIT_BR, inp=True)
    c = cel(ws, R_FORF, 2, 'Valor fixo: escreva o custo diretamente na coluna «Custo», para as doses da ficha.')
    c.font = Font(italic=True, color='555555')
    juntar(ws, R_FORF, 2, 6)
    d_num.add(cel(ws, R_FORF, 7, FORFAIT_EX[1] if ex else None, EUR, inp=True).coordinate)
    cel(ws, R_FORF, 8, FORFAIT_EX[2] if ex else None, inp=True)
    cel(ws, R_FORF, 9, cinzento=True)
    alto(ws, R_FORF, (FORFAIT_EX[0] if ex else FORFAIT_BR, 33), (FORFAIT_EX[2] if ex else '', 21))
    n = n_aviso()
    av = ws.cell(row=R_AVISO, column=1, value=f'=IF({n}=0,"",IF({n}=1,"{AVISO_1}","Atenção: "&{n}&"{AVISO_N}"))')
    av.font = Font(bold=True, color='9C1C1C')
    av.alignment = Alignment(wrap_text=True, vertical='top')
    ws.merge_cells(start_row=R_AVISO, start_column=1, end_row=R_AVISO, end_column=COLS)
    nota(ws, R_NOTA_ING, NOTA_ING)
    # destaques: quantidade com texto, bruto inválido, preço em falta
    ws.conditional_formatting.add(f'B{R_ING1}:C{R_INGN}', FormulaRule(
        formula=[f'AND(B{R_ING1}<>"",NOT(ISNUMBER(B{R_ING1})))'], fill=erro))
    ws.conditional_formatting.add(f'D{R_ING1}:D{R_INGN}', FormulaRule(
        formula=[f'AND($D{R_ING1}<>"",NOT(ISNUMBER($D{R_ING1})))'], fill=erro, font=Font(bold=True, color='9C1C1C')))
    ws.conditional_formatting.add(f'F{R_ING1}:F{R_INGN}', FormulaRule(
        formula=[f'AND(OR($B{R_ING1}<>"",$C{R_ING1}<>""),NOT(ISNUMBER($F{R_ING1})))'], fill=erro))

    # Modo de preparação
    barra(ws, R_TIT_PREP, 'Modo de preparação')
    for c0, c1, txt in ((1, 1, 'Passo'), (2, 6, 'O que se faz'), (7, 7, 'Tempo'), (8, 9, 'Ponto')):
        cel(ws, R_TIT_PREP + 1, c0, txt, negrito=True, cinzento=True)
        if c1 > c0:
            for c in range(c0 + 1, c1 + 1):
                cel(ws, R_TIT_PREP + 1, c, cinzento=True)
            ws.merge_cells(start_row=R_TIT_PREP + 1, start_column=c0, end_row=R_TIT_PREP + 1, end_column=c1)
    passos = (PASSOS if ex else []) + [None] * (N_PASSOS - (len(PASSOS) if ex else 0))
    for i, txt in enumerate(passos):
        f = R_PASSO1 + i
        cel(ws, f, 1, i + 1)
        cel(ws, f, 2, txt, inp=True)
        juntar(ws, f, 2, 6)
        cel(ws, f, 7, None, inp=True)
        cel(ws, f, 8, None, inp=True)
        juntar(ws, f, 8, 9)
        ws.row_dimensions[f].height = 32
    nota(ws, R_NOTA_PREP, NOTA_PREP)

    # Alergénios: X em «Contém» ou «Pode conter»
    barra(ws, R_TIT_ALG, 'Alergénios (anexo II do Regulamento (UE) n.º 1169/2011): marque com X a coluna certa')
    for c0, c1, txt in ((1, 1, 'Alergénio'), (2, 2, 'Contém'), (3, 4, 'Pode conter (contaminação cruzada)'),
                        (5, 9, 'Qual / em que ingrediente')):
        cel(ws, R_TIT_ALG + 1, c0, txt, negrito=True, cinzento=True)
        if c1 > c0:
            for c in range(c0 + 1, c1 + 1):
                cel(ws, R_TIT_ALG + 1, c, cinzento=True)
            ws.merge_cells(start_row=R_TIT_ALG + 1, start_column=c0, end_row=R_TIT_ALG + 1, end_column=c1)
    ws.row_dimensions[R_TIT_ALG + 1].height = 32
    d_x = dv(ws, 'list', None, '"X"', None, 'Alergénios', 'Escolha X ou deixe a célula vazia.')
    for i, a in enumerate(ALERGENIOS):
        f = R_ALG1 + i
        marca, qual = ALERG_EX.get(i, (None, None)) if ex else (None, None)
        cel(ws, f, 1, a)
        cel(ws, f, 2, marca, inp=True).alignment = Alignment(horizontal='center', vertical='top')
        cel(ws, f, 3, None, inp=True).alignment = Alignment(horizontal='center', vertical='top')
        cel(ws, f, 4, None, inp=True)
        ws.merge_cells(start_row=f, start_column=3, end_row=f, end_column=4)
        cel(ws, f, 5, qual, inp=True)
        juntar(ws, f, 5, 9)
        alto(ws, f, (a, 33))
    d_x.add(f'B{R_ALG1}:C{R_ALGN}')
    nota(ws, R_NOTA_ALG, NOTA_ALG)

    # Conservação e pontos críticos
    barra(ws, R_TIT_CONS, 'Conservação e pontos críticos')
    cons = [('Conservação', 'Pescada limpa refrigerada até ao momento de panar.' if ex else None),
            ('Pontos críticos (HACCP)', 'Frio da pescada; fritura.' if ex else None),
            ('Validade das preparações', f'{HACCP[0].upper()}{HACCP[1:]}.' if ex else None)]
    for i, (k, v) in enumerate(cons):
        f = R_TIT_CONS + 1 + i
        cel(ws, f, 1, k, negrito=True)
        cel(ws, f, 2, v, inp=True)
        juntar(ws, f, 2, COLS)
        alto(ws, f, (k, 33), (v or '', 100))
    nota(ws, R_NOTA_CONS, NOTA_CONS)

    # Empratamento
    barra(ws, R_TIT_EMP, 'Empratamento')
    emp = [('Montagem', 'Filetes de pescada panados, com o arroz e o limão.' if ex else None), ('Loiça', None),
           ('Fotografia de referência', 'Cole aqui a fotografia do empratamento.')]
    for i, (k, v) in enumerate(emp):
        f = R_TIT_EMP + 1 + i
        cel(ws, f, 1, k, negrito=True)
        cel(ws, f, 2, v, inp=True)
        juntar(ws, f, 2, COLS)

    # Custo por porção e preço
    barra(ws, R_TIT_PRECO, 'Custo por porção e preço')
    ct, cd, pv, iva = f'B{R_CT}', f'B{R_CD}', f'B{R_PV}', f'B{R_IVA}'
    bloco = [
        (R_CT, 'Custo das doses da ficha (soma da coluna «Custo»)',
         f'=IF(COUNT({CUSTOS})=0,"",SUM({CUSTOS}))', EUR, False),
        (R_CD, 'Custo por porção (dose)', f'=IF({ct}="","",{ct}/{K})', EUR3, False),
        (R_PV, 'Preço de venda sem IVA', 11.00 if ex else None, EUR, True),
        (R_FC, 'Food cost (custo por dose ÷ preço sem IVA)', f'=IF(OR({cd}="",N({pv})<=0),"",{cd}/{pv})', PCT1, False),
        (R_IVA, 'IVA', 0.13, PCT0, True),
        (R_PCI, 'Preço com IVA (o da ementa)', f'=IF(OR(N({pv})<=0,{iva}=""),"",ROUND({pv}*(1+N({iva})),2))', EUR,
         False),
    ]
    for r, rotulo, valor, fmt, inp in bloco:
        cel(ws, r, 1, rotulo, negrito=True)
        z = cel(ws, r, 2, valor, fmt, inp=inp, negrito=True, cinzento=not inp)
        alto(ws, r, (rotulo, 33))
        if r == R_PV:
            d_num.add(z.coordinate)
        if r == R_IVA:
            dv(ws, 'decimal', 'between', '0', '0.99', 'IVA',
               'Escreva a taxa em percentagem, por exemplo 13 % (ou 0,13).').add(z.coordinate)
    nota(ws, R_IVA, IVA_NOTA, 3, COLS, 100)
    nota(ws, R_NOTA_FC, NOTA_FC)
    nota(ws, R_NOTA_FC + 1, NOTA_TEOR)
    for r, rotulo, url in ((R_RODAPE, RODAPE_GUIA, GUIA), (R_RODAPE + 1, RODAPE_CALC, CALC)):
        ws.cell(row=r, column=1, value=rotulo).font = Font(bold=True)
        link = ws.cell(row=r, column=2, value=url)
        link.hyperlink = url
        link.font = Font(color='0563C1', underline='single')
        ws.merge_cells(start_row=r, start_column=2, end_row=r, end_column=COLS)

    for col, w in {'A': 34, 'B': 12, 'C': 12, 'D': 11, 'E': 12, 'F': 13, 'G': 13, 'H': 22, 'I': 12}.items():
        ws.column_dimensions[col].width = w
    ws.sheet_view.showGridLines = False
    ws.page_setup.orientation = 'landscape'
    ws.page_setup.paperSize = ws.PAPERSIZE_A4
    ws.page_setup.fitToWidth = 1
    ws.page_setup.fitToHeight = 0
    ws.sheet_properties.pageSetUpPr.fitToPage = True
    return ws


def gerar():
    wb = Workbook()
    wb.remove(wb.active)
    folha(wb, H_EX, True)
    folha(wb, H_BR, False)
    for i, ws in enumerate(wb.worksheets):
        ws.sheet_view.tabSelected = (i == 1)
    wb.active = 1
    wb.properties.creator = 'AI Chef Pro'
    wb.properties.title = 'Ficha técnica de pratos'
    SALIDA.parent.mkdir(parents=True, exist_ok=True)
    wb.save(SALIDA)


# ---------------------------------------------------------------- cache
def cache_texto_vazio(ruta):
    """inject_cache.py não injeta o resultado «""»: a célula fica com cache vazia (<v/>, que um visor sem recálculo
    mostra como 0). Escreve-se como o Excel (t="str" + <v></v>), tocando só o XML das folhas (copiado do gémeo NL)."""
    padrao = re.compile(r'<c r="([A-Z]+[0-9]+)"((?:(?!\st=)[^>])*)>(<f>[^<]*</f>)(?:<v>\s*</v>|<v\s*/>)?</c>')
    with zipfile.ZipFile(ruta) as z:
        partes = [(i, z.read(i.filename)) for i in z.infolist()]
    n = 0
    with zipfile.ZipFile(str(ruta) + '.tmp', 'w', zipfile.ZIP_DEFLATED) as zout:
        for info, dados in partes:
            if re.match(r'xl/worksheets/sheet[0-9]+\.xml$', info.filename):
                xml, k = padrao.subn(r'<c r="\1"\2 t="str">\3<v></v></c>', dados.decode('utf-8'))
                dados, n = xml.encode('utf-8'), n + k
            zout.writestr(info, dados)
    shutil.move(str(ruta) + '.tmp', str(ruta))
    return n


def injetar(ruta):
    out = subprocess.run([sys.executable, str(INJECT), str(ruta)], check=True, capture_output=True, text=True).stdout
    m = re.search(r'formulas=(\d+) cache_inyectado=(\d+) fallos_pycel=(\d+)', out)
    assert m and m.group(3) == '0', out
    vazias = cache_texto_vazio(ruta)
    assert int(m.group(1)) == int(m.group(2)) + vazias, (out, vazias)  # toda a fórmula leva cache
    return f'formulas={m.group(1)} cache={m.group(2)} vazias={vazias}'


# ---------------------------------------------------------------- gates
def vazio(x):
    return x in (None, '')


def gate_ficheiro():
    wf = load_workbook(SALIDA)
    assert wf.sheetnames == [H_EX, H_BR], wf.sheetnames
    assert wf.active.title == H_BR, wf.active.title
    with zipfile.ZipFile(SALIDA) as zf:
        sel = [n for n in sorted(zf.namelist()) if re.match(r'xl/worksheets/sheet\d+\.xml$', n)
               and 'tabSelected="1"' in zf.read(n).decode('utf-8')]
    assert sel == ['xl/worksheets/sheet2.xml'], sel
    for ws in wf.worksheets:
        assert [ws.cell(row=R_ALG1 + i, column=1).value for i in range(14)] == ALERGENIOS, ws.title
        assert (ws.cell(row=R_ALG1 - 1, column=2).value, ws.cell(row=R_ALG1 - 1, column=3).value) == \
            ('Contém', 'Pode conter (contaminação cruzada)'), ws.title
        lst = [d for d in ws.data_validations.dataValidation if d.type == 'list']
        assert len(lst) == 1 and lst[0].formula1 == '"X"' and str(lst[0].sqref) == f'B{R_ALG1}:C{R_ALGN}', lst
        assert all(d.showErrorMessage for d in ws.data_validations.dataValidation), ws.title
        destinos = {c.hyperlink.target for row in ws.iter_rows() for c in row if c.hyperlink}
        assert destinos == {GUIA, CALC}, (ws.title, destinos)
        assert ws.cell(row=R_RODAPE, column=1).value == RODAPE_GUIA
        assert ws[f'B{R_IVA}'].value == 0.13 and ws[f'C{R_IVA}'].value == IVA_NOTA, ws.title
        assert ws.cell(row=R_NOTA_ALG, column=1).value == NOTA_ALG and ws.cell(row=R_NOTA_CONS, column=1).value == NOTA_CONS
        ps = ws.page_setup
        assert str(ps.paperSize) == str(ws.PAPERSIZE_A4) and ps.fitToWidth == 1 and ps.fitToHeight == 0, ws.title
    ex = wf[H_EX]
    marcas = {(i, c) for i in range(14) for c in (2, 3) if ex.cell(row=R_ALG1 + i, column=c).value == 'X'}
    assert marcas == {(0, 2), (2, 2), (3, 2)}, marcas  # glúten, ovos, peixes: «Contém»
    assert all(ex.cell(row=R_PASSO1 + i, column=7).value is None for i in range(N_PASSOS))  # sem minutos
    # data_only = o que vê um visor que não recalcula
    wv = load_workbook(SALIDA, data_only=True)
    e = wv[H_EX]
    f = R_ING1
    rend, kg, custo, enc = e[f'D{f}'].value, e[f'E{f}'].value, e[f'G{f}'].value, e[f'I{f}'].value
    assert all(isinstance(x, (int, float)) for x in (rend, kg, custo, enc)), (rend, kg, custo, enc)
    assert (round(rend * 100, 1), round(kg, 3), round(custo, 2), round(enc, 3)) == (69.6, 2.3, 17.25, 9.2)
    tot = [e[f'B{r}'].value for r in (R_CT, R_CD, R_FC, R_PCI)]
    assert (round(tot[0], 2), round(tot[1], 3), round(tot[2] * 100, 1), round(tot[3], 2)) == (23.65, 2.365, 21.5, 12.43), tot
    assert vazio(e[f'A{R_AVISO}'].value), e[f'A{R_AVISO}'].value
    for r in range(R_ING1 + 1, R_INGN + 1):
        assert all(vazio(e.cell(row=r, column=c).value) for c in (4, 5, 7, 9)), r
    branco = wv[H_BR]
    for row in wf[H_BR].iter_rows():
        for c in row:
            if c.data_type == 'f':
                assert vazio(branco[c.coordinate].value), (H_BR, c.coordinate, branco[c.coordinate].value)
    return tot


def gate_pycel():
    """As cifras do artigo saem das FÓRMULAS: cópia sem cache (o openpyxl não guarda os <v>) + pycel; depois, casos de
    lógica e de células vazias na folha em branco."""
    logging.disable(logging.CRITICAL)
    from pycel import ExcelCompiler
    wf = load_workbook(SALIDA)
    tmp = tempfile.TemporaryDirectory()
    copia = str(Path(tmp.name) / 'sem-cache.xlsx')
    wf.save(copia)
    with zipfile.ZipFile(copia) as z:
        for n in z.namelist():
            if re.match(r'xl/worksheets/sheet\d+\.xml$', n):
                assert not re.search(r'</f><v>[^<]+</v>', z.read(n).decode('utf-8')), 'a cópia conserva cache'

    def novo(nome):
        xl = ExcelCompiler(filename=copia)

        def val(ref):
            with open(os.devnull, 'w') as dn, contextlib.redirect_stderr(dn):
                x = xl.evaluate(f"'{nome}'!{ref}")
            return x.item() if hasattr(x, 'item') else x

        # Aquecimento: o pycel só recalcula, depois de set_value, as fórmulas que já avaliou.
        for row in wf[nome].iter_rows():
            for c in row:
                if c.data_type == 'f':
                    val(c.coordinate)

        def definir(valores):
            # «Apagar» = '' (o pycel ignora set_value(None)); aqui '' e a célula vazia comportam-se igual.
            for ref, x in valores.items():
                val(ref)
                xl.set_value(f"'{nome}'!{ref}", '' if x is None else x)
        return val, definir

    f = R_ING1
    # 1) Exemplo: as cifras do artigo
    val, _ = novo(H_EX)
    assert round(val(f'D{f}') * 100, 1) == 69.6 and round(val(f'E{f}'), 3) == 2.3
    assert round(val(f'G{f}'), 2) == 17.25 and round(val(f'I{f}'), 3) == 9.2
    assert round(val(f'B{R_CT}'), 2) == 23.65 and round(val(f'B{R_CD}'), 3) == 2.365
    assert round(val(f'B{R_FC}') * 100, 1) == 21.5 and round(val(f'B{R_PCI}'), 2) == 12.43
    res = (val(f'B{R_CT}'), val(f'B{R_CD}'), val(f'B{R_FC}'))
    # 2) O exemplo copiado para a folha em branco dá o mesmo
    val, definir = novo(H_BR)
    definir({f'B{R_DOSES}': 10, f'B{R_ENC}': 40, f'B{f}': 160, f'C{f}': 230, f'F{f}': 7.5, f'G{R_FORF}': 6.4,
         f'B{R_PV}': 11})
    assert round(val(f'G{f}'), 2) == 17.25 and round(val(f'I{f}'), 3) == 9.2
    assert round(val(f'B{R_CD}'), 3) == 2.365 and round(val(f'B{R_FC}') * 100, 1) == 21.5
    assert vazio(val(f'A{R_AVISO}'))
    # 3) Sem bruto = sem perdas: rendimento 100 %, bruto = capitação
    definir({f'B{f + 1}': 80, f'F{f + 1}': 2.0})
    assert val(f'D{f + 1}') == 1 and round(val(f'E{f + 1}'), 3) == 0.8 and round(val(f'G{f + 1}'), 2) == 1.6
    assert round(val(f'B{R_CT}'), 2) == 25.25
    # 4) Quantidade sem preço → custo vazio (não 0) e aviso; texto na capitação → aviso; bruto 0 → «verifique»
    definir({f'B{f + 2}': 50})
    assert vazio(val(f'G{f + 2}')) and val(f'A{R_AVISO}') == AVISO_1, val(f'A{R_AVISO}')
    definir({f'B{f + 3}': '160 g', f'F{f + 3}': 7.5})
    assert vazio(val(f'D{f + 3}')) and vazio(val(f'E{f + 3}')) and vazio(val(f'G{f + 3}'))
    assert val(f'A{R_AVISO}') == 'Atenção: 2' + AVISO_N, val(f'A{R_AVISO}')
    definir({f'B{f + 4}': 100, f'C{f + 4}': 0, f'F{f + 4}': 3})
    assert val(f'D{f + 4}') == BRUTO_KO and vazio(val(f'E{f + 4}')) and vazio(val(f'G{f + 4}'))
    assert val(f'A{R_AVISO}') == 'Atenção: 3' + AVISO_N
    definir({f'C{f + 4}': '230 g'})  # bruto com texto
    assert val(f'D{f + 4}') == BRUTO_KO and vazio(val(f'G{f + 4}'))
    definir({f'C{f + 5}': 200})  # só o bruto, sem capitação nem preço: rendimento vazio, aviso
    assert vazio(val(f'D{f + 5}')) and round(val(f'E{f + 5}'), 3) == 2.0
    assert val(f'A{R_AVISO}') == 'Atenção: 4' + AVISO_N
    for r in range(f + 2, f + 6):
        definir({f'B{r}': None, f'C{r}': None, f'F{r}': None})
    assert vazio(val(f'A{R_AVISO}')) and round(val(f'B{R_CT}'), 2) == 25.25
    # 5) Doses vazias → conta para 1 dose; encomenda vazia → coluna vazia
    definir({f'B{R_DOSES}': None, f'B{R_ENC}': None})
    assert round(val(f'E{f}'), 3) == 0.23 and round(val(f'E{f + 1}'), 3) == 0.08 and vazio(val(f'I{f}'))
    assert val(f'B{R_CD}') == val(f'B{R_CT}') and round(val(f'G{f + 1}'), 2) == 0.16
    # 6) Sem preço de venda → food cost e preço com IVA vazios (sem #DIV/0!); IVA vazio → preço com IVA vazio
    definir({f'B{R_PV}': None})
    assert vazio(val(f'B{R_FC}')) and vazio(val(f'B{R_PCI}'))
    definir({f'B{R_PV}': 11, f'B{R_IVA}': None})
    assert vazio(val(f'B{R_PCI}')) and not vazio(val(f'B{R_FC}'))
    definir({f'B{R_IVA}': 0.23})
    assert round(val(f'B{R_PCI}'), 2) == 13.53
    # 7) Só o valor fixo: custo por dose = valor fixo ÷ doses
    val, definir = novo(H_BR)
    definir({f'G{R_FORF}': 6.4, f'B{R_DOSES}': 10})
    assert round(val(f'B{R_CT}'), 2) == 6.4 and round(val(f'B{R_CD}'), 3) == 0.64
    # 8) Folha em branco intacta: tudo vazio
    val, _ = novo(H_BR)
    for ref in (f'B{R_CT}', f'B{R_CD}', f'B{R_FC}', f'B{R_PCI}', f'A{R_AVISO}', f'D{f}', f'E{f}', f'G{f}', f'I{f}'):
        assert vazio(val(ref)), (ref, val(ref))
    tmp.cleanup()
    return res


# Gate de idioma: espanhol (do gerador ES), brasileirismos e grafias anteriores ao AO90.
ESPANHOL = ['ración', 'raciones', 'porción', 'merma', 'mermas', 'alérgeno', 'alérgenos', 'contiene', 'trazas',
            'elaboración', 'conservación', 'emplatado', 'montaje', 'menaje', 'plato', 'platos', 'coste', 'costes',
            'pvp', 'appcc', 'escandallo', 'rellena', 'guía', 'plantilla', 'cocina', 'salmón', 'pescado', 'fuego',
            'plancha', 'aove', 'fecha', 'versión', 'cantidad', 'unidad', 'tiempo', 'categoría', 'precio', 'precios',
            'restauración', 'españa', 'reglamento', 'limón', 'ajo', 'cebolla', 'pimiento', 'pimienta', 'perejil',
            'puntos', 'con', 'del', 'los', 'las', 'una', 'sin', 'y', 'el', 'huevo', 'huevos', 'leche', 'gluten',
            'cacahuetes', 'apio', 'mostaza', 'altramuces', 'cereales', 'granos', 'rendimiento', 'margen', 'venta',
            'neto', 'neta', 'paso', 'pasos', 'hoja', 'celda', 'celdas', 'amarillas', 'aceite', 'rallado', 'freír',
            'bacalao', 'patata', 'ración', 'escriba', 'usted']
BRASIL = ['planilha', 'planilhas', 'cardápio', 'cardápios', 'arquivo', 'usuário', 'usuários', 'tela', 'time',
          'equipe', 'registro', 'registros', 'controle', 'contato', 'fato', 'seção', 'recepção', 'geladeira',
          'freezer', 'açougue', 'xícara', 'garçom', 'gerenciar', 'gerenciamento', 'digite', 'baixar', 'celular',
          'ônibus', 'você', 'vocês', 'salvar', 'deletar', 'cadastro', 'esquentar', 'suco', 'aluguel', 'faturamento',
          'insumos', 'creme de leite', 'a gente']
PRE_AO90 = ['objectivo', 'factura', 'facturas', 'acção', 'actual', 'actualizar', 'actualizado', 'exacto', 'óptimo',
            'direcção', 'selecção', 'protecção', 'inspecção', 'efectivo', 'colecção', 'electrónico', 'adoptar',
            'correcto', 'correcta', 'projecto']
TIPOGRAFIA_OK = set('·€≥÷×«»–—’…')
PCT_OK = {'9', '12', '13', '23', '100'}


def textos_xlsx():
    wf = load_workbook(SALIDA)
    out = list(wf.sheetnames)
    for ws in wf.worksheets:
        for row in ws.iter_rows():
            for c in row:
                if isinstance(c.value, str):
                    # das fórmulas, só os literais de texto (o que o utilizador vê)
                    out += re.findall(r'"([^"]*)"', c.value) if c.data_type == 'f' else [c.value]
        for d in ws.data_validations.dataValidation:
            out += [x for x in (d.error, d.errorTitle, d.prompt, d.promptTitle) if x]
    return [t for t in out if t]


def gate_idioma():
    textos = textos_xlsx()
    tudo = '\n'.join(t for t in textos if not t.startswith('https://'))
    for w in ESPANHOL + BRASIL + PRE_AO90:
        m = re.search(rf'(?<![\w]){re.escape(w)}(?![\w])', tudo, flags=re.IGNORECASE)
        assert not m, f'palavra proibida «{w}»: …{tudo[max(0, m.start() - 40):m.end() + 40]}…'
    ger = {g for g in re.findall(r'\b\w+(?:ando|endo|indo)\b', tudo, flags=re.IGNORECASE)} - {'quando', 'Quando', 'incluindo'}  # «incluindo lactose» = nome oficial
    assert not ger, f'gerúndio (estrutura brasileira): {ger}'
    assert '°' not in tudo and not re.search(r'\d\s?º', tudo), 'temperatura nos textos'
    for t in textos:
        for pct in re.findall(r'(\d+(?:,\d+)?)\s?%', t):
            assert pct in PCT_OK, ('percentagem não prevista', t)
    raros = {ch for ch in tudo if ord(ch) > 0x24F and ch not in TIPOGRAFIA_OK}
    assert not raros, f'caracteres fora do alfabeto latino: {sorted(raros)}'
    return len(textos)


def gate_parche():
    r = subprocess.run([sys.executable, str(PARCHE), '--check', str(SALIDA)], capture_output=True, text=True, cwd=RAIZ)
    assert r.returncode == 0, r.stdout + r.stderr
    return r.stdout.strip().splitlines()[-1] if r.stdout.strip() else 'ok'


def main():
    gerar()
    cache = injetar(SALIDA)
    ct, cd, fc, pci = gate_ficheiro()
    gate_pycel()
    n = gate_idioma()
    parche = gate_parche()
    pt = lambda x, d=2: f'{x:.{d}f}'.replace('.', ',')  # noqa: E731
    print(f'OK {SALIDA.relative_to(RAIZ)} · {cache} · Exemplo pescada: 160 g limpos de 230 g brutos (rendimento '
          f'69,6 %) · 10 doses = 2,300 kg × 7,50 € = 17,25 € + 6,40 € = {pt(ct)} € → {pt(cd, 3)} €/dose → '
          f'{pt(fc * 100, 1)} % sobre 11,00 € sem IVA ({pt(pci)} € com IVA a 13 %) · encomenda 40 doses = 9,200 kg')
    print(f'   gates: data_only OK · pycel sem cache OK (exemplo + 8 blocos de lógica/células vazias) · idioma OK '
          f'({n} textos: sem espanhol, brasileirismos, pré-AO90 nem temperaturas) · parche --check: {parche}')


if __name__ == '__main__':
    main()
